#!/usr/bin/env python3
"""Write a WeChat article from a Horizon digest using wechat/STYLE.md.

Calls the same OpenAI-compatible endpoint Horizon uses
(data/config.github.json: provider / model / base_url / api_key_env).
Does not read or write WeChat secrets. Does not push a draft.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from digest_items import (
    REPO_ROOT,
    STYLE_PATH,
    default_posts_dir,
    load_local_env,
    pick_items,
    preview_items,
    render_materials,
    split_items,
    today_shanghai,
)


def load_ai_config() -> dict:
    for name in ("data/config.github.json", "data/config.json"):
        path = REPO_ROOT / name
        if path.is_file():
            data = json.loads(path.read_text(encoding="utf-8"))
            ai = data.get("ai") or {}
            if ai.get("base_url") and ai.get("model"):
                return ai
    raise SystemExit("No ai.base_url / ai.model in data/config.github.json")


def chat(cfg: dict, messages: list[dict[str, str]]) -> str:
    key_env = str(cfg.get("api_key_env") or "OPENAI_API_KEY")
    key = os.environ.get(key_env, "").strip()
    if not key:
        raise SystemExit(f"Set {key_env} first. Do not put it in git.")

    base = str(cfg["base_url"]).rstrip("/")
    url = f"{base}/chat/completions"
    payload = {
        "model": cfg["model"],
        "temperature": cfg.get("temperature", 0.3),
        "messages": messages,
        "max_tokens": min(int(cfg.get("max_tokens") or 4096), 8192),
    }
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=180) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", "replace")
        raise SystemExit(f"HTTP {exc.code}: {body}") from exc

    try:
        text = data["choices"][0]["message"]["content"]
    except (KeyError, IndexError, TypeError) as exc:
        raise SystemExit(f"unexpected response: {data}") from exc
    if not text or not str(text).strip():
        raise SystemExit(f"empty model output: {data}")
    return str(text).strip() + "\n"


def build_messages(style: str, materials: str) -> list[dict[str, str]]:
    return [
        {
            "role": "system",
            "content": (
                "按下面这份写法，把日报原料写成一篇公众号成稿。"
                "只输出成稿 markdown，不要解释过程。"
                "不要编造原料里没有的数字、版本、人名。"
                "动词主导，短句利落，严禁翻译腔（如「这就意味着」「值得一提的是」「在……方面」）与公文套话。"
                "中英文与数字之间保留空格（盘古之白）。"
                "不要写「我的疑问」「我的判断」。"
                "每条有出处的结尾必须是一行：原文：[标题](https://...)。"
                "不要只写裸 URL。不要手写裸 <a href>。"
                "frontmatter 加 author: yuseus，以及 source:，填第一条 https 原文，供阅读原文使用。\n\n"
                f"{style}"
            ),
        },
        {
            "role": "user",
            "content": (
                "原料如下。选出 4–6 条能写成四拍的，写成一篇。"
                "标题不超过 22 个字。开头两三句只说今天发生了什么。"
                "每条结尾保留 原文：[标题](https://...) 这一行。\n\n"
                f"{materials}"
            ),
        },
    ]


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--digest", required=True, help="Path to a Horizon Chinese daily markdown")
    parser.add_argument("--pick", default="all", help="1-based indexes or title fragments, comma-separated")
    parser.add_argument("--limit", type=int, default=6, help="Max items when --pick is all")
    parser.add_argument("--out", help="Output article markdown path")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print the STYLE.md prompt and selected items, do not call the model",
    )
    args = parser.parse_args(argv)

    load_local_env()
    digest_path = Path(args.digest)
    if not digest_path.is_file():
        raise SystemExit(f"Digest not found: {digest_path}")
    if not STYLE_PATH.is_file():
        raise SystemExit(f"Missing style guide: {STYLE_PATH}")

    items = split_items(digest_path.read_text(encoding="utf-8"))
    if not items:
        raise SystemExit("No titled sections found in digest.")
    selected = pick_items(items, args.pick, limit=args.limit)
    if not selected:
        raise SystemExit(f"No items matched --pick={args.pick!r}. Available:\n{preview_items(items)}")

    date = today_shanghai()
    style = STYLE_PATH.read_text(encoding="utf-8")
    materials = render_materials(selected, date, str(digest_path))
    messages = build_messages(style, materials)

    if args.dry_run:
        print(f"style: {STYLE_PATH}")
        print(f"items ({len(selected)}):")
        print(preview_items(selected))
        print()
        print(messages[0]["content"])
        return

    cfg = load_ai_config()
    article = chat(cfg, messages)
    out = Path(args.out) if args.out else default_posts_dir() / f"{date}.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(article, encoding="utf-8")
    print(article)
    print(f"Wrote {out}")
    print("先看这篇成稿。再在固定 IP 机器上：")
    print(f"  python3 wechat/scripts/push_draft.py {out} --cover wechat/cover.png")


if __name__ == "__main__":
    main()
