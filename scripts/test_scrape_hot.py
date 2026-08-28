#!/usr/bin/env python3
"""Unit checks for hot/trending collectors (GitHub / HF / X)."""

from __future__ import annotations

from datetime import datetime, timedelta, timezone
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))

from scrape_no_rss import (
    GITHUB_HOT_MAX,
    HF_MODELS_MAX,
    HF_PAPERS_MAX,
    X_HOT_MAX_ITEMS,
    X_HOT_MIN_LIKES,
    filter_github_hot,
    hf_model_item,
    hf_paper_item,
    matches_github_hot,
    parse_github_trending_rss,
    x_hot_item,
)


def assert_true(cond: bool, msg: str) -> None:
    if not cond:
        raise SystemExit(f"FAIL: {msg}")


NOW = datetime(2026, 8, 28, 4, 0, tzinfo=timezone.utc)


def test_github_keyword_guard() -> None:
    assert_true(matches_github_hot("Official Claude Code plugins"), "claude code matches")
    assert_true(matches_github_hot("A new coding agent harness"), "coding agent matches")
    assert_true(matches_github_hot("browser-use Python SDK"), "browser-use matches")
    assert_true(not matches_github_hot("awesome-gpt-image-2 prompt pack"), "image pack stays out")
    assert_true(not matches_github_hot("Please continue reading the tutorial"), "continue is not a keyword")


def test_github_ignores_mcp_buried_in_readme() -> None:
    xml = """<?xml version="1.0"?>
    <rss version="2.0"><channel>
      <item>
        <title>OpenCut-app/OpenCut</title>
        <link>https://github.com/OpenCut-app/OpenCut</link>
        <description>The open-source CapCut alternative. A free video editor for web and desktop.
        """ + ("padding " * 40) + """Later the README mentions an MCP server for AI agents.</description>
      </item>
      <item>
        <title>owner/mcp-agent-kit</title>
        <link>https://github.com/owner/mcp-agent-kit</link>
        <description>MCP toolkit for coding agents.</description>
      </item>
    </channel></rss>
    """
    kept = filter_github_hot(parse_github_trending_rss(xml, published=NOW))
    links = [item["link"] for item in kept]
    assert_true(any("mcp-agent-kit" in link for link in links), kept)
    assert_true(not any("OpenCut" in link for link in links), kept)


def test_github_trending_rss_stamps_date_and_filters() -> None:
    xml = """<?xml version="1.0"?>
    <rss version="2.0"><channel>
      <title>GitHub Daily Trending</title>
      <pubDate>Thu, 27 Aug 2026 10:47:53 GMT</pubDate>
      <item>
        <title>anthropics/claude-plugins-official</title>
        <link>https://github.com/anthropics/claude-plugins-official</link>
        <description>Official Claude Code plugins.</description>
      </item>
      <item>
        <title>freestylefly/awesome-gpt-image-2</title>
        <link>https://github.com/freestylefly/awesome-gpt-image-2</link>
        <description>Prompt pack for image models.</description>
      </item>
    </channel></rss>
    """
    parsed = parse_github_trending_rss(xml, published=NOW)
    assert_true(len(parsed) == 2, parsed)
    assert_true(all(item["published"] == NOW for item in parsed), "items must get a 24h-safe date")
    kept = filter_github_hot(parsed, max_items=GITHUB_HOT_MAX)
    assert_true(len(kept) == 1, kept)
    assert_true("claude-plugins-official" in kept[0]["link"], kept[0])
    assert_true(kept[0]["title"].startswith("GitHub trending:"), kept[0]["title"])


def test_github_hot_cap() -> None:
    items = [
        {
            "title": f"owner/agent-repo-{i}",
            "link": f"https://github.com/owner/agent-repo-{i}",
            "description": "an agent harness",
            "published": NOW,
            "haystack": "an agent harness",
        }
        for i in range(GITHUB_HOT_MAX + 8)
    ]
    kept = filter_github_hot(items)
    assert_true(len(kept) == GITHUB_HOT_MAX, len(kept))


def test_hf_paper_and_model_caps() -> None:
    paper = hf_paper_item(
        {
            "title": "Prime Agent: A Self-Improving RLM Harness",
            "summary": "A harness paper.",
            "publishedAt": "2026-08-20T20:00:00.000Z",
            "paper": {
                "id": "2608.23552",
                "submittedOnDailyAt": "2026-08-28T00:00:00.000Z",
                "upvotes": 43,
            },
        },
        NOW,
    )
    assert_true(paper is not None, "paper parsed")
    assert_true(paper["link"] == "https://huggingface.co/papers/2608.23552", paper)
    assert_true(paper["published"].day == 28, paper["published"])
    stale = hf_paper_item(
        {
            "title": "Old classic",
            "paper": {
                "id": "2309.06180",
                "submittedOnDailyAt": "2023-09-01T00:00:00.000Z",
            },
        },
        NOW,
    )
    assert_true(stale is not None and stale["published"] == NOW, "old arXiv date must not miss the 24h window")
    assert_true(paper["title"].startswith("HF daily paper:"), paper["title"])

    model = hf_model_item(
        {
            "id": "Qwen/Qwen3.8-Flash-Next",
            "pipeline_tag": "text-generation",
            "likes": 100,
            "trendingScore": 90,
        },
        NOW,
    )
    assert_true(model is not None, "text-generation model kept")
    image = hf_model_item(
        {
            "id": "someone/sd-turbo",
            "pipeline_tag": "text-to-image",
            "likes": 9999,
            "trendingScore": 9999,
        },
        NOW,
    )
    assert_true(image is None, "image models are not a datasets-style firehose but still skipped")
    junk = hf_model_item(
        {
            "id": "someone/Qwen-Uncensored",
            "pipeline_tag": "text-generation",
            "likes": 999,
            "trendingScore": 999,
        },
        NOW,
    )
    assert_true(junk is None, "uncensored fine-tunes are skipped")
    junk2 = hf_model_item(
        {
            "id": "huihui-ai/Huihui-Qwen3.8-27B-abliterated-GGUF",
            "pipeline_tag": "text-generation",
            "likes": 50,
            "trendingScore": 50,
        },
        NOW,
    )
    assert_true(junk2 is None, "abliterated fine-tunes are skipped")
    assert_true(HF_PAPERS_MAX <= 25, HF_PAPERS_MAX)
    assert_true(HF_MODELS_MAX <= 15, HF_MODELS_MAX)
    assert_true(HF_PAPERS_MAX + HF_MODELS_MAX <= 25, "HF family cap")


def test_x_hot_popularity_and_no_replies() -> None:
    since = NOW - timedelta(hours=24)
    created = NOW.strftime("%a %b %d %H:%M:%S +0000 %Y")
    hot = x_hot_item(
        {
            "id_str": "1",
            "created_at": created,
            "full_text": "Claude Code just shipped a harness change",
            "favorite_count": X_HOT_MIN_LIKES,
            "retweet_count": 3,
            "user": {"screen_name": "someone"},
            "url": "https://x.com/someone/status/1",
        },
        since,
    )
    assert_true(hot is not None, "popular recent tweet kept")
    quiet = x_hot_item(
        {
            "id_str": "2",
            "created_at": created,
            "full_text": "Claude Code just shipped a harness change",
            "favorite_count": X_HOT_MIN_LIKES - 1,
            "user": {"screen_name": "someone"},
            "url": "https://x.com/someone/status/2",
        },
        since,
    )
    assert_true(quiet is None, "low-like tweets are not 热点")
    reply = x_hot_item(
        {
            "id_str": "3",
            "created_at": created,
            "full_text": "yeah",
            "favorite_count": 99,
            "is_reply": True,
            "user": {"screen_name": "someone"},
            "url": "https://x.com/someone/status/3",
        },
        since,
    )
    assert_true(reply is None, "replies stay out")
    old = x_hot_item(
        {
            "id_str": "4",
            "created_at": (NOW - timedelta(hours=30)).strftime("%a %b %d %H:%M:%S +0000 %Y"),
            "full_text": "old viral Claude Code thread",
            "favorite_count": 500,
            "user": {"screen_name": "someone"},
            "url": "https://x.com/someone/status/4",
        },
        since,
    )
    assert_true(old is None, "outside 24h window dropped")
    assert_true(X_HOT_MAX_ITEMS <= 15, X_HOT_MAX_ITEMS)


def main() -> None:
    test_github_keyword_guard()
    test_github_ignores_mcp_buried_in_readme()
    test_github_trending_rss_stamps_date_and_filters()
    test_github_hot_cap()
    test_hf_paper_and_model_caps()
    test_x_hot_popularity_and_no_replies()
    print("ok")


if __name__ == "__main__":
    main()
