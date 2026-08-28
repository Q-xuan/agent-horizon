#!/usr/bin/env python3
"""Scrape listing pages / public APIs that have no official RSS and emit feeds.

Used by Actions (and local runs) as a tiny collector in front of Horizon:
the daily job serves these files on 127.0.0.1:8766 and config points at them.

Existing official-blog scrapes stay here. Hot/trending families are also
emitted here so we can stamp a 24h-safe pubDate, keyword-guard, and cap
volume before grok scoring — Horizon's RSS scraper drops items with no
per-item date, which is why the raw mshibanami GitHub Trending feed
never reached the scorer.
"""

from __future__ import annotations

import argparse
import html
import json
import os
import re
import sys
import time
from datetime import datetime, timedelta, timezone
from email.utils import format_datetime
from pathlib import Path
from typing import Callable
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from xml.etree import ElementTree as ET

UA = "AgentHorizon/1.0 (+https://github.com/Q-xuan/agent-horizon)"

# Agent / harness / coding-agent guard. Short tokens use word boundaries so
# "continue" / "ai" firehoses stay out. Applied to GitHub trending only.
GITHUB_HOT_PATTERNS = (
    r"\bagents?\b",
    r"\bharness\b",
    r"\bmcp\b",
    r"claude[- ]?code",
    r"\bclaude\b",
    r"\bcodex\b",
    r"openhands",
    r"\baider\b",
    r"\bcline\b",
    r"roo[- ]?code",
    r"\bgoose\b",
    r"swe[- ]?agent",
    r"\bopencode\b",
    r"\bcursor\b",
    r"langgraph",
    r"langchain",
    r"smolagents",
    r"fastmcp",
    r"\bautogen\b",
    r"crewai",
    r"\bmastra\b",
    r"\bdspy\b",
    r"\bletta\b",
    r"browser-use",
    r"pydantic-ai",
    r"coding[- ]agent",
    r"model context protocol",
)

GITHUB_HOT_RE = re.compile("|".join(f"(?:{p})" for p in GITHUB_HOT_PATTERNS), re.I)

GITHUB_TRENDING_FEEDS = (
    "https://mshibanami.github.io/GitHubTrendingRSS/daily/python.xml",
    "https://mshibanami.github.io/GitHubTrendingRSS/daily/typescript.xml",
    "https://mshibanami.github.io/GitHubTrendingRSS/daily/jupyter-notebook.xml",
    "https://mshibanami.github.io/GitHubTrendingRSS/daily/all.xml",
)

HF_MODEL_PIPELINE_ALLOW = frozenset(
    {
        "text-generation",
        "image-text-to-text",
        "any-to-any",
        "text2text-generation",
        "reinforcement-learning",
    }
)

# X search is not a follow-list. Horizon's Twitter collector only does
# profiles; Nitter / RSSHub search feeds are dead. Reuse the same Apify
# scweet actor Horizon already uses for replies (source_mode=search).
X_HOT_QUERY = (
    '("Claude Code" OR "coding agent" OR OpenHands OR "claude-code" '
    'OR "MCP server" OR "model context protocol" OR "agent harness" '
    'OR "Codex CLI" OR Cline OR Aider)'
)
X_HOT_FETCH_LIMIT = 40
X_HOT_MAX_ITEMS = 15
X_HOT_MIN_LIKES = 15
APIFY_ACTOR = "altimis~scweet"
APIFY_MAX_WAIT = 180
APIFY_POLL = 3.0

GITHUB_HOT_MAX = 20
HF_PAPERS_MAX = 15
HF_MODELS_MAX = 10


def now_utc() -> datetime:
    return datetime.now(timezone.utc)


def fetch(url: str, timeout: int = 25, accept: str = "text/html") -> str:
    req = Request(url, headers={"User-Agent": UA, "Accept": accept})
    with urlopen(req, timeout=timeout) as resp:
        return resp.read().decode("utf-8", errors="replace")


def fetch_json(url: str, timeout: int = 25) -> object:
    raw = fetch(url, timeout=timeout, accept="application/json")
    return json.loads(raw)


def rfc822(dt: datetime) -> str:
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return format_datetime(dt)


def parse_month_day_year(text: str) -> datetime | None:
    match = re.search(
        r"(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s+(\d{1,2}),\s+(20\d{2})",
        text,
    )
    if not match:
        return None
    return datetime.strptime(
        f"{match.group(1)[:3]} {match.group(2)} {match.group(3)}",
        "%b %d %Y",
    ).replace(tzinfo=timezone.utc)


def parse_iso(text: str) -> datetime | None:
    if not text:
        return None
    match = re.search(r"(20\d{2}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:[.+]\d{2}:\d{2}|Z)?)", text)
    if match:
        raw = match.group(1).replace("Z", "+00:00")
        try:
            return datetime.fromisoformat(raw).astimezone(timezone.utc)
        except ValueError:
            return None
    try:
        return datetime.fromisoformat(text.replace("Z", "+00:00")).astimezone(timezone.utc)
    except ValueError:
        return None


def strip_html(text: str) -> str:
    text = html.unescape(text or "")
    text = re.sub(r"(?i)<br\s*/?>", "\n", text)
    text = re.sub(r"(?i)</p>", "\n", text)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def short_title(text: str, fallback: str) -> str:
    first = re.split(r"(?<=[.!?])\s+", text.strip(), maxsplit=1)[0].strip()
    if len(first) > 90:
        first = first[:87].rstrip() + "..."
    return first or fallback


def matches_github_hot(text: str) -> bool:
    return bool(GITHUB_HOT_RE.search(text or ""))


def write_rss(path: Path, title: str, home: str, items: list[dict]) -> None:
    rows = []
    for item in items:
        desc = html.escape(item.get("description") or item["title"])
        rows.append(
            "    <item>\n"
            f"      <title>{html.escape(item['title'])}</title>\n"
            f"      <link>{html.escape(item['link'])}</link>\n"
            f"      <guid isPermaLink=\"true\">{html.escape(item['link'])}</guid>\n"
            f"      <pubDate>{rfc822(item['published'])}</pubDate>\n"
            f"      <description>{desc}</description>\n"
            "    </item>"
        )
    body = "\n".join(rows)
    path.write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<rss version="2.0">\n'
        "  <channel>\n"
        f"    <title>{html.escape(title)}</title>\n"
        f"    <link>{html.escape(home)}</link>\n"
        f"    <description>{html.escape(title)}</description>\n"
        f"{body}\n"
        "  </channel>\n"
        "</rss>\n",
        encoding="utf-8",
    )


def scrape_cursor_changelog() -> list[dict]:
    page = fetch("https://cursor.com/changelog")
    found: dict[str, dict] = {}
    for match in re.finditer(
        r'href="(/changelog/([a-z0-9][a-z0-9-]+))"[^>]*>',
        page,
    ):
        href, slug = match.group(1), match.group(2)
        if slug in {"page", "rss", "feed"}:
            continue
        window = page[match.start() : match.start() + 1800]
        published = parse_month_day_year(window) or now_utc()
        lead = re.search(r"<p[^>]*>(.*?)</p>", window, re.S)
        raw = re.sub("<[^>]+>", "", lead.group(1)).strip() if lead else slug
        description = html.unescape(raw)
        title = short_title(description, slug.replace("-", " "))
        found.setdefault(
            href,
            {
                "title": f"Cursor changelog: {title}",
                "link": f"https://cursor.com{href}",
                "description": description or title,
                "published": published,
            },
        )
    items = list(found.values())
    items.sort(key=lambda x: x["published"], reverse=True)
    return items[:12]


def scrape_cognition() -> list[dict]:
    page = fetch("https://cognition.ai/blog")
    items = []
    seen = set()
    for match in re.finditer(
        r'"@type":"BlogPosting".*?"headline":"(.*?)".*?"url":"(https://cognition\.(?:ai|com)/blog/([a-z0-9-]+))".*?"datePublished":"([^"]+)"',
        page,
        re.S,
    ):
        title = html.unescape(match.group(1).replace("\\u0026", "&"))
        slug = match.group(3)
        if slug in seen:
            continue
        seen.add(slug)
        published = parse_iso(match.group(4)) or now_utc()
        items.append(
            {
                "title": title,
                "link": f"https://cognition.ai/blog/{slug}",
                "description": title,
                "published": published,
            }
        )
    return items[:12]


def parse_github_trending_rss(xml_text: str, published: datetime | None = None) -> list[dict]:
    """Parse mshibanami trending RSS. Items have no pubDate; caller stamps one."""
    published = published or now_utc()
    try:
        root = ET.fromstring(xml_text)
    except ET.ParseError:
        return []
    items: list[dict] = []
    for item_el in root.iter("item"):
        title = strip_html(item_el.findtext("title") or "")
        link = (item_el.findtext("link") or "").strip()
        raw_desc = item_el.findtext("description") or ""
        desc = strip_html(raw_desc)
        if not title or not link:
            continue
        items.append(
            {
                "title": title,
                "link": link,
                "description": desc[:500],
                "published": published,
                "haystack": f"{title} {desc[:500]}",
            }
        )
    return items


def filter_github_hot(items: list[dict], max_items: int = GITHUB_HOT_MAX) -> list[dict]:
    seen: set[str] = set()
    kept: list[dict] = []
    for item in items:
        link = item["link"].rstrip("/")
        if link in seen:
            continue
        if not matches_github_hot(item.get("haystack") or f"{item['title']} {item.get('description', '')}"):
            continue
        seen.add(link)
        kept.append(
            {
                "title": f"GitHub trending: {item['title']}",
                "link": item["link"],
                "description": item.get("description") or item["title"],
                "published": item["published"],
            }
        )
        if len(kept) >= max_items:
            break
    return kept


def scrape_github_com_trending() -> list[dict]:
    """Fallback if mshibanami feeds fail. Public HTML, no token."""
    page = fetch("https://github.com/trending?since=daily")
    published = now_utc()
    items: list[dict] = []
    seen: set[str] = set()
    for match in re.finditer(
        r'href="/(?P<owner>[A-Za-z0-9_.-]+)/(?P<repo>[A-Za-z0-9_.-]+)"[^>]*>\s*'
        r"(?:<span[^>]*>.*?</span>\s*)?(?P<name>[^<]+)",
        page,
        re.S,
    ):
        owner, repo = match.group("owner"), match.group("repo")
        if owner in {"topics", "settings", "features", "orgs", "login"}:
            continue
        link = f"https://github.com/{owner}/{repo}"
        if link in seen:
            continue
        seen.add(link)
        window = page[match.start() : match.start() + 1200]
        desc_match = re.search(r"<p[^>]*>(.*?)</p>", window, re.S)
        desc = strip_html(desc_match.group(1)) if desc_match else ""
        title = f"{owner}/{repo}"
        items.append(
            {
                "title": title,
                "link": link,
                "description": desc[:500],
                "published": published,
                "haystack": f"{title} {desc[:500]}",
            }
        )
    return items


def scrape_github_trending() -> list[dict]:
    published = now_utc()
    collected: list[dict] = []
    failed = 0
    for url in GITHUB_TRENDING_FEEDS:
        try:
            xml_text = fetch(url, accept="application/rss+xml, application/xml, text/xml")
            collected.extend(parse_github_trending_rss(xml_text, published=published))
        except (URLError, TimeoutError, OSError, ValueError):
            failed += 1
    if failed == len(GITHUB_TRENDING_FEEDS):
        collected = scrape_github_com_trending()
    return filter_github_hot(collected, GITHUB_HOT_MAX)


def hf_paper_item(row: dict, fallback_published: datetime) -> dict | None:
    paper = row.get("paper") if isinstance(row.get("paper"), dict) else {}
    arxiv_id = str(paper.get("id") or "").strip()
    title = (row.get("title") or paper.get("title") or "").strip()
    if not arxiv_id or not title:
        return None
    summary = (row.get("summary") or paper.get("summary") or paper.get("ai_summary") or "").strip()
    published = (
        parse_iso(str(paper.get("submittedOnDailyAt") or ""))
        or parse_iso(str(row.get("publishedAt") or ""))
        or parse_iso(str(paper.get("publishedAt") or ""))
        or fallback_published
    )
    upvotes = paper.get("upvotes") if paper.get("upvotes") is not None else row.get("upvotes")
    desc_parts = [summary[:800] if summary else title]
    if upvotes is not None:
        desc_parts.append(f"HF daily paper upvotes: {upvotes}")
    return {
        "title": f"HF daily paper: {title}",
        "link": f"https://huggingface.co/papers/{arxiv_id}",
        "description": "\n".join(desc_parts),
        "published": published,
    }


def scrape_hf_daily_papers() -> list[dict]:
    published = now_utc()
    data = fetch_json(
        "https://huggingface.co/api/daily_papers?"
        + urlencode({"limit": str(HF_PAPERS_MAX), "sort": "trending"})
    )
    if not isinstance(data, list):
        return []
    items: list[dict] = []
    seen: set[str] = set()
    for row in data:
        if not isinstance(row, dict):
            continue
        item = hf_paper_item(row, published)
        if item is None or item["link"] in seen:
            continue
        seen.add(item["link"])
        items.append(item)
        if len(items) >= HF_PAPERS_MAX:
            break
    return items


def hf_model_item(row: dict, fallback_published: datetime) -> dict | None:
    model_id = str(row.get("id") or row.get("modelId") or "").strip()
    if not model_id or "/" not in model_id:
        return None
    pipeline = str(row.get("pipeline_tag") or "").strip()
    if pipeline and pipeline not in HF_MODEL_PIPELINE_ALLOW:
        return None
    likes = row.get("likes")
    score = row.get("trendingScore")
    tags = row.get("tags") or []
    tag_str = ", ".join(str(t) for t in tags[:8]) if isinstance(tags, list) else ""
    desc = f"Trending Hugging Face model ({pipeline or 'unknown'})."
    extras = []
    if score is not None:
        extras.append(f"trendingScore={score}")
    if likes is not None:
        extras.append(f"likes={likes}")
    if tag_str:
        extras.append(tag_str)
    if extras:
        desc = desc + " " + "; ".join(extras)
    return {
        "title": f"HF trending model: {model_id}",
        "link": f"https://huggingface.co/{model_id}",
        "description": desc,
        "published": fallback_published,
    }


def scrape_hf_trending_models() -> list[dict]:
    published = now_utc()
    data = fetch_json(
        "https://huggingface.co/api/models?"
        + urlencode(
            {
                "sort": "trendingScore",
                "direction": "-1",
                "limit": "30",
            }
        )
    )
    if not isinstance(data, list):
        return []
    items: list[dict] = []
    seen: set[str] = set()
    for row in data:
        if not isinstance(row, dict):
            continue
        item = hf_model_item(row, published)
        if item is None or item["link"] in seen:
            continue
        seen.add(item["link"])
        items.append(item)
        if len(items) >= HF_MODELS_MAX:
            break
    return items


def parse_twitter_time(raw: str) -> datetime | None:
    if not raw:
        return None
    try:
        return datetime.strptime(raw, "%a %b %d %H:%M:%S %z %Y").astimezone(timezone.utc)
    except ValueError:
        return parse_iso(raw)


def x_hot_item(row: dict, since: datetime) -> dict | None:
    if not isinstance(row, dict) or row.get("noResults"):
        return None
    if row.get("is_reply"):
        return None
    text = html.unescape(str(row.get("full_text") or row.get("text") or "")).strip()
    if not text:
        return None
    published = parse_twitter_time(str(row.get("created_at") or ""))
    if published is None or published < since:
        return None
    likes = 0
    try:
        likes = int(row.get("favorite_count") or 0)
    except (TypeError, ValueError):
        likes = 0
    if likes < X_HOT_MIN_LIKES:
        return None
    user = row.get("user") if isinstance(row.get("user"), dict) else {}
    handle = (
        user.get("screen_name")
        or user.get("username")
        or user.get("handle")
        or row.get("handle")
        or row.get("username")
        or "unknown"
    )
    tweet_id = str(row.get("id_str") or row.get("id") or "")
    tweet_id = tweet_id.replace("tweet-", "")
    url = str(row.get("url") or "").strip()
    if not url and tweet_id and handle != "unknown":
        url = f"https://x.com/{handle}/status/{tweet_id}"
    if not url:
        return None
    retweets = row.get("retweet_count") or 0
    title_body = text[:50].replace("\n", " ").strip()
    if len(text) > 50:
        title_body += "..."
    return {
        "title": f"@{handle}: {title_body}",
        "link": url,
        "description": f"{text}\n\nX hot: ❤️ {likes} · 🔁 {retweets}",
        "published": published,
        "likes": likes,
    }


def apify_search_tweets(token: str, query: str, max_items: int) -> list[dict]:
    start_url = f"https://api.apify.com/v2/acts/{APIFY_ACTOR}/runs?token={token}"
    payload = json.dumps(
        {
            "source_mode": "search",
            "search_query": query,
            "search_sort": "Latest",
            "max_items": max_items,
        }
    ).encode("utf-8")
    req = Request(
        start_url,
        data=payload,
        headers={"User-Agent": UA, "Content-Type": "application/json", "Accept": "application/json"},
        method="POST",
    )
    with urlopen(req, timeout=30) as resp:
        started = json.loads(resp.read().decode("utf-8"))
    data = started.get("data") or {}
    run_id = data.get("id")
    dataset_id = data.get("defaultDatasetId")
    if not run_id or not dataset_id:
        raise RuntimeError("Apify run did not return id/dataset")

    status_url = f"https://api.apify.com/v2/actor-runs/{run_id}?token={token}"
    elapsed = 0.0
    while elapsed < APIFY_MAX_WAIT:
        time.sleep(APIFY_POLL)
        elapsed += APIFY_POLL
        status_req = Request(status_url, headers={"User-Agent": UA, "Accept": "application/json"})
        with urlopen(status_req, timeout=15) as resp:
            status = (json.loads(resp.read().decode("utf-8")).get("data") or {}).get("status")
        if status == "SUCCEEDED":
            break
        if status in {"FAILED", "ABORTED", "TIMED-OUT"}:
            raise RuntimeError(f"Apify run {run_id} ended with {status}")
    else:
        raise RuntimeError(f"Apify run {run_id} timed out after {APIFY_MAX_WAIT}s")

    items_url = f"https://api.apify.com/v2/datasets/{dataset_id}/items?token={token}"
    items_req = Request(items_url, headers={"User-Agent": UA, "Accept": "application/json"})
    with urlopen(items_req, timeout=30) as resp:
        rows = json.loads(resp.read().decode("utf-8"))
    return rows if isinstance(rows, list) else []


def scrape_x_hot() -> list[dict]:
    token = (os.environ.get("APIFY_TOKEN") or "").strip()
    if not token:
        print(
            "x-hot.xml: skipped (APIFY_TOKEN missing; follow-list still uses Horizon Twitter)",
            file=sys.stderr,
        )
        return []
    since = now_utc() - timedelta(hours=24)
    rows = apify_search_tweets(token, X_HOT_QUERY, X_HOT_FETCH_LIMIT)
    items: list[dict] = []
    seen: set[str] = set()
    for row in rows:
        item = x_hot_item(row, since)
        if item is None or item["link"] in seen:
            continue
        seen.add(item["link"])
        items.append(item)
    items.sort(key=lambda x: int(x.get("likes") or 0), reverse=True)
    cleaned = []
    for item in items[:X_HOT_MAX_ITEMS]:
        cleaned.append({k: item[k] for k in ("title", "link", "description", "published")})
    return cleaned


def print_items(filename: str, items: list[dict]) -> None:
    print(f"{filename}: {len(items)} items")
    for item in items:
        print(f"  - {item['title'][:90]} | {item['link']}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", default="scraped-feeds")
    parser.add_argument(
        "--print-items",
        action="store_true",
        help="Print titles/links after each feed (dry-collect sanity check)",
    )
    args = parser.parse_args()
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)

    jobs: list[tuple[str, str, str, Callable[[], list[dict]]]] = [
        ("cursor-changelog.xml", "Cursor Changelog", "https://cursor.com/changelog", scrape_cursor_changelog),
        ("cognition-blog.xml", "Cognition Blog", "https://cognition.ai/blog", scrape_cognition),
        (
            "github-trending.xml",
            "GitHub Trending Daily",
            "https://github.com/trending",
            scrape_github_trending,
        ),
        (
            "hf-daily-papers.xml",
            "Hugging Face Daily Papers",
            "https://huggingface.co/papers",
            scrape_hf_daily_papers,
        ),
        (
            "hf-trending-models.xml",
            "Hugging Face Trending Models",
            "https://huggingface.co/models?sort=trending",
            scrape_hf_trending_models,
        ),
        ("x-hot.xml", "X Hot", "https://x.com/search", scrape_x_hot),
    ]
    failed = 0
    for filename, title, home, fn in jobs:
        try:
            items = fn()
            write_rss(out / filename, title, home, items)
            if args.print_items:
                print_items(filename, items)
            else:
                print(f"{filename}: {len(items)} items")
        except (URLError, HTTPError, TimeoutError, OSError, ValueError, RuntimeError, json.JSONDecodeError) as exc:
            write_rss(out / filename, title, home, [])
            print(f"{filename}: failed ({exc})", file=sys.stderr)
            # Missing APIFY_TOKEN is a skip, not a hard fail.
            if filename != "x-hot.xml":
                failed += 1
    return 1 if failed == len(jobs) else 0


if __name__ == "__main__":
    raise SystemExit(main())
