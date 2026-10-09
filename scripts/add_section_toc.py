#!/usr/bin/env python3
"""Add a section table of contents and stable section anchors to a digest post.

Runs on Horizon's generated Jekyll post (e.g. _posts/2026-10-09-summary-zh.md):

* every ``## <section>`` heading gets a stable kramdown id
  (``sec-<profile>`` taken from the section's ``item-<profile>-N`` anchors,
  else a Chinese-safe slug of the heading) plus a small ``#`` share link;
* a compact ``<nav id="ah-toc">`` with each section and its item count is
  inserted after the opening blockquote;
* the bold section labels in the overview list link to their sections;
* each section heading carries a small "回到目录" link.

The ``## <section>`` lines stay unchanged so wechat/scripts/digest_items.py
still splits items the same way.

Idempotent: a post that already has ``id="ah-toc"`` is left alone.
"""

from __future__ import annotations

import argparse
import html
import re
import sys
import unicodedata
from pathlib import Path

H2_RE = re.compile(r"^## (?!#)(.+?)\s*$")
ITEM_ANCHOR_RE = re.compile(r'<a id="item-([a-z0-9][a-z0-9-]*?)-\d+"></a>')
TOC_MARK = 'id="ah-toc"'

LABELS = {
    "zh": {"toc": "目录", "back": "↑ 回到目录", "anchor": "链接到本节", "unit": "条"},
    "en": {"toc": "Contents", "back": "↑ Back to contents", "anchor": "Link to this section", "unit": ""},
}


def slugify(text: str) -> str:
    """Lowercase, keep letters/digits (incl. CJK), join the rest with '-'."""
    text = unicodedata.normalize("NFKC", text).strip().lower()
    out: list[str] = []
    for ch in text:
        cat = unicodedata.category(ch)
        if cat[0] in ("L", "N"):
            out.append(ch)
        else:
            out.append("-")
    slug = re.sub(r"-+", "-", "".join(out)).strip("-")
    return slug or "section"


def find_sections(lines: list[str]) -> list[dict]:
    sections: list[dict] = []
    for i, line in enumerate(lines):
        m = H2_RE.match(line)
        if m:
            sections.append({"line": i, "title": m.group(1).strip()})
    for idx, sec in enumerate(sections):
        end = sections[idx + 1]["line"] if idx + 1 < len(sections) else len(lines)
        sec["end"] = end
        body = "\n".join(lines[sec["line"] + 1 : end])
        profiles = ITEM_ANCHOR_RE.findall(body)
        sec["count"] = len(profiles)
        sec["profile"] = profiles[0] if profiles else None
    used: set[str] = set()
    for sec in sections:
        base = f"sec-{sec['profile']}" if sec["profile"] else f"sec-{slugify(sec['title'])}"
        sid, n = base, 2
        while sid in used:
            sid, n = f"{base}-{n}", n + 1
        used.add(sid)
        sec["id"] = sid
    return sections


def render(text: str, lang: str = "zh") -> str:
    if TOC_MARK in text:
        return text
    lab = LABELS.get(lang, LABELS["zh"])
    lines = text.split("\n")
    sections = find_sections(lines)
    if not sections:
        return text
    by_title = {s["title"]: s for s in sections}

    toc_items = []
    for s in sections:
        count = f'{s["count"]}{lab["unit"]}' if s["count"] else ""
        toc_items.append(
            f'<li><a href="#{s["id"]}"><span class="ah-toc-name">{html.escape(s["title"])}</span>'
            + (f'<span class="ah-toc-count">{count}</span>' if count else "")
            + "</a></li>"
        )
    toc = (
        f'<nav id="ah-toc" class="ah-toc" aria-label="{lab["toc"]}">'
        f'<span class="ah-toc-title">{lab["toc"]}</span>'
        f'<ul>{"".join(toc_items)}</ul></nav>'
    )

    # The "## <section>" line itself is kept byte-for-byte: wechat/scripts/
    # digest_items.py keys on it. Extra markup only goes right after it
    # (before the first item), where that parser ignores lines.
    out: list[str] = []
    starts = {s["line"]: s for s in sections}
    toc_inserted = False
    in_front = lines[:1] == ["---"]
    for i, line in enumerate(lines):
        if in_front:
            out.append(line)
            if i > 0 and line == "---":
                in_front = False
            continue
        if i in starts:
            s = starts[i]
            out.append(line)
            out.append(f'{{: #{s["id"]} .ah-section}}')
            out.append("")
            out.append(
                f'<p class="ah-sec-meta"><a class="ah-anchor" href="#{s["id"]}" '
                f'aria-label="{lab["anchor"]}">#</a><a class="ah-back" href="#ah-toc">{lab["back"]}</a></p>'
            )
            continue
        bold = re.fullmatch(r"\*\*(.+?)\*\*\s*", line)
        if bold and bold.group(1) in by_title:
            out.append(f'**[{bold.group(1)}](#{by_title[bold.group(1)]["id"]})**')
            continue
        out.append(line)
        # TOC goes right after the first blockquote ("从 N 条内容中筛选出…").
        if not toc_inserted and line.startswith(">"):
            nxt = lines[i + 1] if i + 1 < len(lines) else ""
            if not nxt.startswith(">"):
                out.extend(["", toc])
                toc_inserted = True
    if not toc_inserted:
        try:
            close = out.index("---", 1)
        except ValueError:
            close = -1
        out[close + 1 : close + 1] = ["", toc, ""]
    return "\n".join(out)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("posts", nargs="+", type=Path)
    ap.add_argument("--lang", default=None, help="zh or en (default: from filename)")
    args = ap.parse_args(argv)
    rc = 0
    for p in args.posts:
        if not p.is_file():
            print(f"skip (missing): {p}", file=sys.stderr)
            continue
        lang = args.lang or ("en" if p.stem.endswith("-en") else "zh")
        src = p.read_text(encoding="utf-8")
        dst = render(src, lang)
        if dst != src:
            p.write_text(dst, encoding="utf-8")
            print(f"toc added: {p}")
        else:
            print(f"unchanged: {p}")
    return rc


if __name__ == "__main__":
    raise SystemExit(main())
