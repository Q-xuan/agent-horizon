#!/usr/bin/env python3
"""Checks for digest extraction and the WeChat writing flow."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from digest_items import STYLE_PATH, WECHAT_DIR, pick_items, render_materials, split_items


FIXTURE = WECHAT_DIR / "testdata" / "digest-zh.md"


def assert_true(cond: bool, msg: str) -> None:
    if not cond:
        raise SystemExit(f"FAIL: {msg}")


def test_style_is_process() -> None:
    text = STYLE_PATH.read_text(encoding="utf-8")
    for needle in ("从前怎样", "所以怎样", "这次改了什么", "停"):
        assert_true(needle in text, f"STYLE.md missing {needle}")
    assert_true("背景 / 变化 / 影响" in text, "STYLE.md should forbid labeled beats")
    assert_true("往后会碰到" in text, "STYLE.md should forbid 往后会碰到")
    assert_true("OpenRouter" not in text, "STYLE.md must not bake in a day's story")
    assert_true("我的疑问" in text and "不要" in text, "STYLE.md should reject 我的疑问")


def test_extract_fixture() -> None:
    items = split_items(FIXTURE.read_text(encoding="utf-8"))
    titles = [it["title"] for it in items]
    assert_true("Harness 架构" not in titles, f"group header leaked: {titles}")
    assert_true("Agent 工程师日报" not in titles, f"group header leaked: {titles}")
    assert_true("Codex rust-v0.148.0 发布" in titles, f"missing Codex: {titles}")
    assert_true(any("加水印" in t for t in titles), f"missing watermark item: {titles}")
    codex = next(it for it in items if it["title"].startswith("Codex"))
    assert_true(codex["score"] == "8.0", codex)
    assert_true("openai/codex" in codex["url"], codex["url"])

    picked = pick_items(items, "all", limit=6)
    assert_true(1 <= len(picked) <= 6, f"pick size {len(picked)}")
    assert_true(picked[0]["title"].startswith("Codex"), picked[0]["title"])

    materials = render_materials(picked, "2026-01-02", str(FIXTURE))
    assert_true("### 我的疑问" not in materials, "materials must not add 我的疑问 sections")
    assert_true("### 我的判断" not in materials, "materials must not add 我的判断 sections")
    assert_true("wechat/STYLE.md" in materials, "next step must point at STYLE.md")
    assert_true("write_from_digest.py" in materials, "next step must point at writer")
    assert_true("原文：[Codex rust-v0.148.0 发布](https://" in materials, materials)
    assert_true("原文：https://" not in materials, "原文 must be a markdown link, not a bare URL")


def test_cli_list_and_polish() -> None:
    scripts = Path(__file__).resolve().parent
    listed = subprocess.check_output(
        [sys.executable, str(scripts / "polish_post.py"), "--digest", str(FIXTURE), "--list"],
        text=True,
    )
    assert_true("Codex rust-v0.148.0 发布" in listed, listed)
    assert_true("我的疑问" not in listed, listed)

    dry = subprocess.check_output(
        [sys.executable, str(scripts / "write_from_digest.py"), "--digest", str(FIXTURE), "--dry-run"],
        text=True,
    )
    assert_true("从前怎样" in dry, "dry-run must load STYLE.md")
    assert_true("data-linktype" in dry, "dry-run must load the WeChat link rule")
    assert_true("不要在正文打印「原文：」" in dry, dry)
    assert_true("原文：[标题](https://" not in dry, "writer prompt must not require a 原文 line")
    assert_true("Codex rust-v0.148.0 发布" in dry, dry)


def main() -> None:
    test_style_is_process()
    test_extract_fixture()
    test_cli_list_and_polish()
    print("ok")


if __name__ == "__main__":
    main()
