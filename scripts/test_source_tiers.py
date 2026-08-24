#!/usr/bin/env python3
"""Unit checks for source-authority score adjustments."""

from __future__ import annotations

from types import SimpleNamespace
from pathlib import Path
import json
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))

from apply_source_tiers import (
    apply_item,
    apply_source_tiers,
    classify_tier,
    has_primary_official_url,
    load_policy,
)


def assert_true(cond: bool, msg: str) -> None:
    if not cond:
        raise SystemExit(f"FAIL: {msg}")


def item(
    *,
    source_type: str,
    score: float | None,
    url: str = "https://example.com/x",
    content: str = "",
    item_id: str = "x:1",
    feed_name: str | None = None,
    event_type: str | None = None,
) -> SimpleNamespace:
    meta: dict = {}
    if feed_name:
        meta["feed_name"] = feed_name
    if event_type:
        meta["event_type"] = event_type
    analysis = SimpleNamespace(score=score, reason="ok")
    processing = SimpleNamespace(analysis=analysis)
    return SimpleNamespace(
        id=item_id,
        source_type=source_type,
        url=url,
        content=content,
        metadata=meta,
        processing=processing,
    )


def test_classify_and_official_url() -> None:
    policy = load_policy()
    release = item(
        source_type="github",
        score=7.0,
        item_id="github:release:99",
        url="https://github.com/cline/cline/releases/tag/v1.2.3",
    )
    assert_true(classify_tier(release, policy) == "official", "github release is official")
    assert_true(has_primary_official_url(release, policy), "watched github owner is official URL")

    event = item(
        source_type="github",
        score=6.0,
        item_id="github:event:1",
        event_type="PushEvent",
        url="https://github.com/someone/random",
    )
    assert_true(classify_tier(event, policy) == "community", "github user event is community")

    wechat = item(
        source_type="rss",
        score=7.2,
        feed_name="机器之心",
        url="https://mp.weixin.qq.com/s/abc",
    )
    assert_true(classify_tier(wechat, policy) == "secondary", "wechat2rss is secondary")
    assert_true(not has_primary_official_url(wechat, policy), "wechat host is never official")

    wechat_with_primary = item(
        source_type="rss",
        score=7.2,
        feed_name="量子位",
        url="https://mp.weixin.qq.com/s/abc",
        content="原文 https://openai.com/index/something",
    )
    assert_true(has_primary_official_url(wechat_with_primary, policy), "body official URL counts")

    deals = item(
        source_type="rss",
        score=6.0,
        feed_name="少数派",
        url="https://sspai.com/post/1",
    )
    assert_true(classify_tier(deals, policy) == "deals", "deals stay deals")

    gn = item(source_type="google_news", score=6.8, url="https://www.theverge.com/ai")
    assert_true(classify_tier(gn, policy) == "secondary", "google news is secondary")


def test_adjustments() -> None:
    policy = load_policy()

    official = item(
        source_type="github",
        score=7.0,
        item_id="github:release:1",
        url="https://github.com/openai/codex/releases/tag/v1",
    )
    decision = apply_item(official, policy)
    assert_true(decision["action"] == "boost", decision)
    assert_true(official.processing.analysis.score == 7.5, official.processing.analysis.score)

    rumor = item(
        source_type="google_news",
        score=7.8,
        url="https://www.theverge.com/rumor",
        content="sources say a lab might ship something",
    )
    decision = apply_item(rumor, policy)
    assert_true(decision["action"] == "drop", decision)
    assert_true(rumor.processing.analysis.score == 0.0, rumor.processing.analysis.score)
    assert_true("source_tier=secondary" in rumor.processing.analysis.reason, rumor.processing.analysis.reason)

    cited = item(
        source_type="rss",
        score=7.2,
        feed_name="机器之心",
        url="https://mp.weixin.qq.com/s/abc",
        content="参见 https://anthropic.com/news/example",
    )
    decision = apply_item(cited, policy)
    assert_true(decision["action"] == "unchanged", decision)
    assert_true(cited.processing.analysis.score == 7.2, cited.processing.analysis.score)

    reddit = item(
        source_type="reddit",
        score=8.0,
        url="https://www.reddit.com/r/LocalLLaMA/comments/x",
    )
    decision = apply_item(reddit, policy)
    assert_true(decision["action"] == "drop", decision)
    assert_true(reddit.processing.analysis.score == 0.0, reddit.processing.analysis.score)

    reddit_official = item(
        source_type="reddit",
        score=7.0,
        url="https://www.reddit.com/r/ClaudeAI/comments/x",
        content="release notes https://github.com/anthropics/claude-code/releases/tag/v2",
    )
    decision = apply_item(reddit_official, policy)
    assert_true(decision["action"] == "unchanged", decision)
    assert_true(reddit_official.processing.analysis.score == 7.0, reddit_official.processing.analysis.score)

    deal = item(
        source_type="rss",
        score=6.0,
        feed_name="HN Free API / Credits",
        url="https://news.ycombinator.com/item?id=1",
    )
    decision = apply_item(deal, policy)
    assert_true(decision["tier"] == "deals", decision)
    assert_true(decision["action"] == "unchanged", decision)
    assert_true(deal.processing.analysis.score == 6.0, deal.processing.analysis.score)

    blog = item(
        source_type="rss",
        score=8.0,
        feed_name="Anthropic Engineering",
        url="https://www.anthropic.com/engineering/foo",
    )
    decision = apply_item(blog, policy)
    assert_true(decision["tier"] == "official", decision)
    assert_true(blog.processing.analysis.score == 8.5, blog.processing.analysis.score)


def test_config_rss_names_are_classified() -> None:
    policy = load_policy()
    config_path = Path(__file__).resolve().parents[1] / "data" / "config.github.json"
    feeds = {
        entry["name"]
        for entry in json.loads(config_path.read_text(encoding="utf-8"))["sources"]["rss"]
    }
    classified = set()
    for key in (
        "official_rss_names",
        "practitioner_rss_names",
        "secondary_rss_names",
        "community_rss_names",
        "deals_rss_names",
    ):
        classified.update(policy[key])
    missing = sorted(feeds - classified)
    extra = sorted(classified - feeds)
    assert_true(not missing, f"RSS in config missing from source_tiers.json: {missing}")
    assert_true(not extra, f"source_tiers.json RSS not in config: {extra}")


def test_batch_and_policy_file() -> None:
    items = [
        item(
            source_type="github",
            score=6.0,
            item_id="github:release:2",
            url="https://github.com/block/goose/releases/tag/v1",
        ),
        item(source_type="google_news", score=6.2, url="https://example.net/blurb"),
    ]
    logs: list[str] = []
    apply_source_tiers(items, printer=logs.append)
    assert_true(items[0].processing.analysis.score == 6.5, items[0].processing.analysis.score)
    assert_true(items[1].processing.analysis.score == 0.0, items[1].processing.analysis.score)
    assert_true(logs and "boost=1" in logs[0] and "drop=1" in logs[0], logs)


def main() -> None:
    test_classify_and_official_url()
    test_adjustments()
    test_config_rss_names_are_classified()
    test_batch_and_policy_file()
    print("ok")


if __name__ == "__main__":
    main()
