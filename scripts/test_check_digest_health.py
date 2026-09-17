#!/usr/bin/env python3
"""Unit checks for Daily Agent Digest post-run health gate."""

from __future__ import annotations

from pathlib import Path
import sys
import tempfile

sys.path.insert(0, str(Path(__file__).resolve().parent))

from check_digest_health import FAIL_MESSAGE, evaluate, main, zh_is_empty


def assert_true(cond: bool, msg: str) -> None:
    if not cond:
        raise SystemExit(f"FAIL: {msg}")


GOOD_ZH = """---
layout: default
title: "Horizon Summary: 2026-09-17 (ZH)"
date: 2026-09-17
lang: zh
---

> 从 40 条内容中筛选出 8 条重要资讯。

### [Codex rust-v0.148.0 发布](https://github.com/openai/codex/releases/tag/rust-v0.148.0) ⭐️ 8.0/10

Codex 增加 exec fork。
"""

EMPTY_ZH = """---
layout: default
title: "Horizon Summary: 2026-09-17 (ZH)"
date: 2026-09-17
lang: zh
---

> 已分析 217 条内容，但没有达到重要性阈值的条目。

今日暂无重要动态，可能原因：
- 今天关注的信息源较平静
- AI 评分阈值设置过高
"""


AI_DEAD_LOG = """
Fetched 217 items from all sources
Merged 16 cross-source duplicates → 201 unique items
WARNING  Error fetching RSS feed OpenAI Engineering: Client
         error '429 Too Many Requests' for url
         https://openai.com/news/engineering/rss.xml
ERROR    Error analyzing item github:release:390230711:
         RetryError[<Future state=finished raised InternalServerError>]
ERROR    Error analyzing item github:release:389942465:
         RetryError[<Future state=finished raised InternalServerError>]
ERROR    Error analyzing item github:release:389928130:
         RetryError[<Future state=finished raised InternalServerError>]
ERROR    Error analyzing item github:release:390317660:
         RetryError[<Future state=finished raised InternalServerError>]
ERROR    Error analyzing item github:release:390373039:
         RetryError[<Future state=finished raised InternalServerError>]
ERROR    Error analyzing item hackernews:story:49724881:
         RetryError[<Future state=finished raised InternalServerError>]
🤖 Analyzed 201 items with AI
⭐️ Selected 0 items with profile filters
⚖️ Balanced digest selected 0/0 items
"""

RSS_ONLY_LOG = """
WARNING  Error fetching RSS feed OpenAI Engineering: Client
         error '429 Too Many Requests' for url
         https://openai.com/news/engineering/rss.xml
WARNING  Error fetching RSS feed Latent Space: Client
         error '429 Too Many Requests' for url
Fetched 80 items from all sources
🤖 Analyzed 70 items with AI
⭐️ Selected 12 items with profile filters
⚖️ Balanced digest selected 12/12 items
"""

QUIET_LOG = """
Fetched 0 items from all sources
[yellow]No new content found. Exiting.[/yellow]
"""

HEALTHY_LOG = """
Fetched 90 items from all sources
🤖 Analyzed 80 items with AI
⭐️ Selected 18 items with profile filters
"""

TRANSIENT_AI_LOG = """
Fetched 90 items from all sources
ERROR    Error analyzing item github:release:1:
         RetryError[<Future state=finished raised InternalServerError>]
ERROR    Error analyzing item github:release:2:
         RetryError[<Future state=finished raised InternalServerError>]
🤖 Analyzed 80 items with AI
⭐️ Selected 15 items with profile filters
"""


def _write(dir_path: Path, name: str, text: str) -> Path:
    path = dir_path / name
    path.write_text(text, encoding="utf-8")
    return path


def test_ai_dead_and_selected_zero() -> None:
    reasons = evaluate(AI_DEAD_LOG)
    assert_true(any("AI/gateway" in r for r in reasons), reasons)
    assert_true(any("Selected 0 items" in r for r in reasons), reasons)


def test_rss_429_alone_does_not_fail() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        zh = _write(Path(tmp), "summary-zh.md", GOOD_ZH)
        reasons = evaluate(RSS_ONLY_LOG, zh_path=zh)
    assert_true(reasons == [], reasons)


def test_quiet_day_ok() -> None:
    reasons = evaluate(QUIET_LOG)
    assert_true(reasons == [], reasons)


def test_empty_zh_after_items_fails() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        zh = _write(Path(tmp), "summary-zh.md", EMPTY_ZH)
        reasons = evaluate(AI_DEAD_LOG, zh_path=zh)
        assert_true(zh_is_empty(zh) is True, "empty ZH should be detected")
    assert_true(any("empty ZH summary" in r for r in reasons), reasons)


def test_healthy_digest_ok() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        zh = _write(Path(tmp), "summary-zh.md", GOOD_ZH)
        reasons = evaluate(HEALTHY_LOG, zh_path=zh)
        assert_true(zh_is_empty(zh) is False, "good ZH should pass")
    assert_true(reasons == [], reasons)


def test_few_ai_errors_with_selection_ok() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        zh = _write(Path(tmp), "summary-zh.md", GOOD_ZH)
        reasons = evaluate(TRANSIENT_AI_LOG, zh_path=zh)
    assert_true(reasons == [], reasons)


def test_selected_zero_without_gateway_errors_fails() -> None:
    log = """
Fetched 164 items from all sources
🤖 Analyzed 164 items with AI
⭐️ Selected 0 items with profile filters
"""
    reasons = evaluate(log)
    assert_true(any("Selected 0 items" in r for r in reasons), reasons)
    assert_true(not any("AI/gateway" in r for r in reasons), reasons)


def test_cli_prints_fail_message() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        log = _write(Path(tmp), "horizon-run.log", AI_DEAD_LOG)
        code = main(["--log", str(log)])
    assert_true(code == 1, f"cli exit {code}")


def test_cli_ok_and_missing_log() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        log = _write(Path(tmp), "horizon-run.log", HEALTHY_LOG)
        zh = _write(Path(tmp), "summary-zh.md", GOOD_ZH)
        code = main(["--log", str(log), "--zh", str(zh)])
        assert_true(code == 0, f"healthy cli exit {code}")
        missing = main(["--log", str(Path(tmp) / "nope.log")])
        assert_true(missing == 1, f"missing log exit {missing}")


def main_tests() -> None:
    test_ai_dead_and_selected_zero()
    test_rss_429_alone_does_not_fail()
    test_quiet_day_ok()
    test_empty_zh_after_items_fails()
    test_healthy_digest_ok()
    test_few_ai_errors_with_selection_ok()
    test_selected_zero_without_gateway_errors_fails()
    test_cli_prints_fail_message()
    test_cli_ok_and_missing_log()
    print("ok")


if __name__ == "__main__":
    # FAIL_MESSAGE is part of the public contract used by Actions.
    assert_true(FAIL_MESSAGE == "Digest AI failed or selected 0 items", FAIL_MESSAGE)
    main_tests()
