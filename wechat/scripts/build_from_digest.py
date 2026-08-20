#!/usr/bin/env python3
"""Extract Horizon digest items. Next step is a rewrite with wechat/STYLE.md."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from digest_items import (
    NEXT_STEP,
    default_posts_dir,
    pick_items,
    preview_items,
    render_materials,
    split_items,
    today_shanghai,
)


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--digest", required=True, help="Path to a Horizon Chinese daily markdown")
    parser.add_argument("--pick", default="all", help="1-based indexes or title fragments, comma-separated")
    parser.add_argument("--limit", type=int, default=6, help="Max items when --pick is all")
    parser.add_argument("--list", action="store_true", help="Print extracted titles and exit")
    parser.add_argument("--out", help="Output materials markdown path")
    args = parser.parse_args(argv)

    digest_path = Path(args.digest)
    if not digest_path.is_file():
        raise SystemExit(f"Digest not found: {digest_path}")

    items = split_items(digest_path.read_text(encoding="utf-8"))
    if not items:
        raise SystemExit("No titled sections found in digest.")

    if args.list:
        print(preview_items(items))
        return

    selected = pick_items(items, args.pick, limit=args.limit)
    if not selected:
        raise SystemExit(f"No items matched --pick={args.pick!r}. Available:\n{preview_items(items)}")

    date = today_shanghai()
    out = Path(args.out) if args.out else default_posts_dir() / f"{date}.materials.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(render_materials(selected, date, str(digest_path)), encoding="utf-8")
    print(f"Wrote {out} ({len(selected)} items)")
    print(preview_items(selected))
    print()
    print(NEXT_STEP.strip())


if __name__ == "__main__":
    main()
