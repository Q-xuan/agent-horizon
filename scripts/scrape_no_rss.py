#!/usr/bin/env python3
"""Scrape listing pages that have no official RSS and emit Atom/RSS files."""

from __future__ import annotations

import argparse
import html
import re
import sys
from datetime import datetime, timezone
from email.utils import format_datetime
from pathlib import Path
from urllib.error import URLError
from urllib.request import Request, urlopen

UA = "AgentHorizon/1.0 (+https://github.com/Q-xuan/agent-horizon)"


def fetch(url: str) -> str:
    req = Request(url, headers={"User-Agent": UA, "Accept": "text/html"})
    with urlopen(req, timeout=25) as resp:
        return resp.read().decode("utf-8", errors="replace")


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
        published = parse_month_day_year(window) or datetime.now(timezone.utc)
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


def parse_iso(text: str) -> datetime | None:
    match = re.search(r"(20\d{2}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:[+-]\d{2}:\d{2}|Z)?)", text)
    if not match:
        return None
    raw = match.group(1).replace("Z", "+00:00")
    return datetime.fromisoformat(raw).astimezone(timezone.utc)


def short_title(text: str, fallback: str) -> str:
    first = re.split(r"(?<=[.!?])\s+", text.strip(), maxsplit=1)[0].strip()
    if len(first) > 90:
        first = first[:87].rstrip() + "..."
    return first or fallback


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
        published = parse_iso(match.group(4)) or datetime.now(timezone.utc)
        items.append(
            {
                "title": title,
                "link": f"https://cognition.ai/blog/{slug}",
                "description": title,
                "published": published,
            }
        )
    return items[:12]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", default="scraped-feeds")
    args = parser.parse_args()
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)

    jobs = [
        ("cursor-changelog.xml", "Cursor Changelog", "https://cursor.com/changelog", scrape_cursor_changelog),
        ("cognition-blog.xml", "Cognition Blog", "https://cognition.ai/blog", scrape_cognition),
    ]
    failed = 0
    for filename, title, home, fn in jobs:
        try:
            items = fn()
            write_rss(out / filename, title, home, items)
            print(f"{filename}: {len(items)} items")
        except (URLError, TimeoutError, OSError, ValueError) as exc:
            write_rss(out / filename, title, home, [])
            print(f"{filename}: failed ({exc})", file=sys.stderr)
            failed += 1
    return 1 if failed == len(jobs) else 0


if __name__ == "__main__":
    raise SystemExit(main())
