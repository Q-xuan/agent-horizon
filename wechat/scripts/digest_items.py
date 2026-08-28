#!/usr/bin/env python3
"""Split a Horizon Chinese digest into titled items."""

from __future__ import annotations

import datetime as dt
import os
import re
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
WECHAT_DIR = Path(__file__).resolve().parents[1]
STYLE_PATH = WECHAT_DIR / "STYLE.md"

SKIP_TITLES = {
    "en",
    "zh",
    "english",
    "中文",
    "sources",
    "引用",
    "目录",
    "harness 架构",
    "agent 工程师日报",
    "ai 日报",
}

HEADING_RE = re.compile(
    r"^#{2,3}\s+(?:\[(?P<link_title>[^\]]+)\]\((?P<url>[^)]+)\)|(?P<title>.+?))"
    r"(?:\s+(?:⭐️|⭐)\s*(?P<score>[\d.]+)\s*/\s*10)?"
    r"\s*$"
)

NEXT_STEP = """下一步：按 wechat/STYLE.md 写成稿。不要补「我的疑问」。
不要在正文打印「原文：」。日报成稿存成 wechat/posts/YYYY-MM-DD.md，「阅读原文」会指向当天中文日报。
人写：把成稿存到 wechat/posts/YYYY-MM-DD.md
或：python3 wechat/scripts/write_from_digest.py --digest <日报.md>

先打开成稿看一遍。再在固定 IP 机器上推草稿。不要在 GitHub Actions 上推微信。
"""


MD_LINK_RE = re.compile(r"\[([^\]]+)\]\((https://[^)]+)\)")
HTTPS_RE = re.compile(r"https://[^\s)>\]]+")


def https_only(url: str) -> str:
    url = (url or "").strip()
    if url.startswith("https://") and len(url) > len("https://"):
        return url
    return ""


def item_source_url(item: dict[str, str]) -> str:
    """First https source: heading url, then a markdown link, then a bare https."""
    url = https_only(item.get("url", ""))
    if url:
        return url
    blob = f"{item.get('title', '')}\n{item.get('body', '')}"
    m = MD_LINK_RE.search(blob)
    if m:
        return https_only(m.group(2))
    m = HTTPS_RE.search(blob)
    return https_only(m.group(0)) if m else ""


def yuanywen_line(title: str, url: str) -> str:
    """Sourced items must end with 原文：[title](https://...). Never a bare URL."""
    href = https_only(url)
    if not href:
        return ""
    label = (title or href).strip()
    return f"原文：[{label}]({href})"


def load_dotenv(path: Path) -> None:
    if not path.is_file():
        return
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


def load_local_env() -> None:
    load_dotenv(REPO_ROOT / ".env")
    load_dotenv(WECHAT_DIR / ".env.local")


def split_items(text: str) -> list[dict[str, str]]:
    """Best-effort split of a Horizon digest into titled item sections."""
    items: list[dict[str, str]] = []
    current: dict[str, str] | None = None
    body: list[str] = []

    def flush() -> None:
        nonlocal current, body
        if current is None:
            return
        current["body"] = "\n".join(body).strip()
        title = current["title"]
        if title and not title.startswith("Horizon"):
            items.append(current)
        current = None
        body = []

    for line in text.splitlines():
        m = HEADING_RE.match(line)
        if m:
            title = (m.group("link_title") or m.group("title") or "").strip()
            if title.lower() in SKIP_TITLES:
                flush()
                continue
            flush()
            current = {
                "title": title,
                "url": (m.group("url") or "").strip(),
                "score": (m.group("score") or "").strip(),
                "body": "",
            }
            continue
        if current is not None:
            body.append(line)
    flush()
    return items


def score_value(item: dict[str, str]) -> float:
    try:
        return float(item.get("score") or 0)
    except ValueError:
        return 0.0


def pick_items(items: list[dict[str, str]], pick: str, limit: int = 6) -> list[dict[str, str]]:
    if pick.strip() in {"", "all"}:
        ranked = sorted(items, key=score_value, reverse=True)
        return ranked[:limit] if any(score_value(it) for it in items) else items[:limit]
    chosen: list[dict[str, str]] = []
    for part in pick.split(","):
        part = part.strip()
        if not part:
            continue
        if part.isdigit():
            idx = int(part)
            if 1 <= idx <= len(items):
                chosen.append(items[idx - 1])
            continue
        lowered = part.lower()
        match = next((it for it in items if lowered in it["title"].lower()), None)
        if match:
            chosen.append(match)
    return chosen[:limit]


def render_materials(items: list[dict[str, str]], date: str, digest_path: str) -> str:
    blocks = [
        f"# 原料 {date}",
        "",
        NEXT_STEP.strip(),
        "",
        f"日报：{digest_path}",
        f"写法：{STYLE_PATH.relative_to(REPO_ROOT) if STYLE_PATH.is_relative_to(REPO_ROOT) else STYLE_PATH}",
        "",
    ]
    first_source = next((item_source_url(it) for it in items if item_source_url(it)), "")
    if first_source:
        blocks += [f"source: {first_source}", ""]
    for i, item in enumerate(items, 1):
        blocks += [f"## {i}. {item['title']}", ""]
        extra = yuanywen_line(item["title"], item_source_url(item))
        if extra:
            blocks.append(extra)
        if item.get("score"):
            blocks.append(f"分数：{item['score']}/10")
        if extra or item.get("score"):
            blocks.append("")
        snippet = item["body"].strip() or "（摘要待补）"
        blocks += [snippet, "", ""]
    return "\n".join(blocks).rstrip() + "\n"


def preview_items(items: list[dict[str, str]]) -> str:
    lines = []
    for i, item in enumerate(items, 1):
        score = f"  {item['score']}/10" if item.get("score") else ""
        lines.append(f"{i}. {item['title']}{score}")
    return "\n".join(lines)


def today_shanghai() -> str:
    return dt.datetime.now(dt.timezone(dt.timedelta(hours=8))).date().isoformat()


def default_posts_dir() -> Path:
    return WECHAT_DIR / "posts"
