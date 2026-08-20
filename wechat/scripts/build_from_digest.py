#!/usr/bin/env python3
"""Turn selected digest items into WeChat draft markdown.

Each sourced item ends with 原文：[title](https://...). No empty 我的疑问 sections.
"""

from __future__ import annotations

import argparse
import datetime as dt
import re
from pathlib import Path


ITEM_RE = re.compile(
    r"^#{2,3}\s+(?P<title>.+?)\s*$",
    re.MULTILINE,
)
MD_LINK_RE = re.compile(r"\[([^\]]+)\]\((https://[^)]+)\)")
HTTPS_RE = re.compile(r"https://[^\s)>\]]+")
SCORE_RE = re.compile(r"\s*⭐️?\s*\d+(?:\.\d+)?/10\s*$")


def item_title_and_url(item: dict[str, str]) -> tuple[str, str]:
    """Display title plus first https source (heading link, then body)."""
    raw = SCORE_RE.sub("", item["title"]).strip()
    m = MD_LINK_RE.search(raw)
    if m:
        return m.group(1).strip(), m.group(2).strip()
    title = raw
    blob = f"{raw}\n{item.get('body', '')}"
    m = MD_LINK_RE.search(blob)
    if m:
        return title, m.group(2).strip()
    m = HTTPS_RE.search(blob)
    return title, (m.group(0) if m else "")


def yuanywen_line(title: str, url: str) -> str:
    """Sourced items must end with 原文：[title](https://...). Never a bare URL."""
    if not url.startswith("https://"):
        return ""
    label = title or url
    return f"原文：[{label}]({url})"


def split_items(text: str) -> list[dict[str, str]]:
    """Best-effort split of a Horizon digest into titled sections."""
    lines = text.splitlines()
    items: list[dict[str, str]] = []
    current: dict[str, str] | None = None
    body: list[str] = []

    def flush() -> None:
        nonlocal current, body
        if current is None:
            return
        current["body"] = "\n".join(body).strip()
        if current["title"] and not current["title"].startswith("Horizon"):
            items.append(current)
        current = None
        body = []

    for line in lines:
        m = re.match(r"^#{2,3}\s+(.+?)\s*$", line)
        if m and not re.match(r"^#{1}\s+", line):
            title = m.group(1).strip()
            # skip language / toc style headers
            if title.lower() in {"en", "zh", "english", "中文", "sources", "引用", "目录"}:
                continue
            flush()
            current = {"title": title, "body": ""}
            continue
        if current is not None:
            body.append(line)
    flush()
    return items


def pick_items(items: list[dict[str, str]], pick: str) -> list[dict[str, str]]:
    if pick.strip() in {"", "all"}:
        return items[:8]
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
    return chosen


def render_post(items: list[dict[str, str]], date: str) -> str:
    sourced = [item_title_and_url(it) for it in items]
    first_source = next((url for _, url in sourced if url.startswith("https://")), "")
    blocks = [
        "---",
        f"title: {date} Agent 笔记",
        "author: pengyu",
        "digest: 从每日雷达里挑出的几条。",
    ]
    if first_source:
        blocks.append(f"source: {first_source}")
    blocks += [
        "---",
        "",
        f"# {date} Agent 笔记",
        "",
        "> 原料来自 [Agent Horizon](https://q-xuan.github.io/agent-horizon/)。下面只写我真正停下来想过的几条。",
        "",
        "## 今天为什么写这些",
        "",
        "（用两三句说清楚：今天被什么卡住，或想验证什么。）",
        "",
    ]
    for i, (item, (title, url)) in enumerate(zip(items, sourced), 1):
        snippet = item["body"].strip()
        if len(snippet) > 500:
            snippet = snippet[:500].rstrip() + "…"
        blocks += [
            "---",
            "",
            f"## {i}. {title}",
            "",
            snippet or "（摘要待补）",
            "",
        ]
        extra = yuanywen_line(title, url)
        if extra:
            blocks += [extra, ""]
    blocks += [
        "---",
        "",
        "## 收束",
        "",
        "（今天这些东西，会不会改你自己做 agent 的方式？改哪一步？）",
        "",
    ]
    return "\n".join(blocks)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--digest", required=True, help="Path to a Horizon daily markdown")
    parser.add_argument("--pick", default="all", help="1-based indexes or title fragments, comma-separated")
    parser.add_argument("--out", help="Output markdown path")
    args = parser.parse_args()

    digest_path = Path(args.digest)
    text = digest_path.read_text(encoding="utf-8")
    items = split_items(text)
    if not items:
        raise SystemExit("No titled sections found in digest.")
    selected = pick_items(items, args.pick)
    if not selected:
        preview = "\n".join(f"{i}. {it['title']}" for i, it in enumerate(items, 1))
        raise SystemExit(f"No items matched --pick={args.pick!r}. Available:\n{preview}")

    date = dt.date.today().isoformat()
    out = Path(args.out) if args.out else Path(__file__).resolve().parents[1] / "posts" / f"{date}.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(render_post(selected, date), encoding="utf-8")
    print(f"Wrote {out} ({len(selected)} items)")
    for i, it in enumerate(selected, 1):
        print(f"  {i}. {it['title']}")


if __name__ == "__main__":
    main()
