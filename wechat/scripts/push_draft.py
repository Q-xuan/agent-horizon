#!/usr/bin/env python3
"""Push a local markdown post to the WeChat official-account draft box.

Requires WECHAT_APPID / WECHAT_SECRET and a cover image when pushing.
Creates a draft only. Does not mass-send.
Use --html-out to write the typeset HTML and exit without pushing.
"""

from __future__ import annotations

import argparse
import html
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from digest_items import load_local_env


# WeChat keeps a CSS whitelist. No theme hex, no media queries, no dark/light vars.
# Clean Astro Nano on WeChat: PingFang / Hiragino / YaHei + Monospace.
FONT = "-apple-system, BlinkMacSystemFont, 'PingFang SC', 'Hiragino Sans GB', 'Microsoft YaHei', sans-serif"
CODE_FONT = "ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, 'Courier New', monospace"

# Plain <a href> is stripped after publish. Editor-shaped tags survive.
MD_LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
YUANYWEN_RE = re.compile(r"原文[：:]\s*\[[^\]]*\]\((https://[^)\s]+)\)")
YUANYWEN_LINE_RE = re.compile(r"^原文[：:]")
HTTPS_RE = re.compile(r"https://[^\s)>\]]+")
H2_NUM_RE = re.compile(r"^(\d+)\.\s+(.*)$")


def https_only(url: str) -> str:
    """Return url if it is https://, else empty. Never emit http/javascript hrefs."""
    url = (url or "").strip()
    if url.startswith("https://") and len(url) > len("https://"):
        return url
    return ""


def wechat_anchor(label: str, url: str) -> str:
    """WeChat-editor <a> that survives publish sanitizer. https href only."""
    safe_label = html.escape(label, quote=True)
    href = https_only(url)
    if not href:
        return safe_label
    safe_href = html.escape(href, quote=True)
    return (
        f'<a target="_blank" href="{safe_href}" textvalue="{safe_label}" '
        f'data-linktype="2" style="font-family:{FONT} !important;'
        f'text-decoration:underline !important;'
        f'text-underline-offset:3px !important;'
        f'word-break:break-word !important;">{safe_label}</a>'
    )


def first_https_url(text: str) -> str:
    """First https:// URL in markdown, preferring a 原文：[title](url) line."""
    m = YUANYWEN_RE.search(text)
    if m:
        return https_only(m.group(1))
    m = HTTPS_RE.search(text)
    return https_only(m.group(0)) if m else ""


def content_source_url(meta: dict[str, str], body: str) -> str:
    """阅读原文 URL: frontmatter source: if https, else first https in the body."""
    source = https_only(meta.get("source", ""))
    if source:
        return source
    return first_https_url(body)


def is_cjk(ch: str) -> bool:
    """True for CJK letters and punctuation so wrapped Chinese is not spaced."""
    if not ch:
        return False
    cp = ord(ch)
    return (
        0x2E80 <= cp <= 0x2EFF
        or 0x2F00 <= cp <= 0x2FDF
        or 0x3000 <= cp <= 0x303F
        or 0x3040 <= cp <= 0x30FF
        or 0x3400 <= cp <= 0x4DBF
        or 0x4E00 <= cp <= 0x9FFF
        or 0xF900 <= cp <= 0xFAFF
        or 0xFF00 <= cp <= 0xFFEF
        or 0x20000 <= cp <= 0x2A6DF
    )


def join_wrapped_lines(lines: list[str]) -> str:
    """Join hard-wrapped source lines. No English space between CJK and CJK."""
    parts = [x.strip() for x in lines if x.strip()]
    if not parts:
        return ""
    out = parts[0]
    for nxt in parts[1:]:
        if is_cjk(out[-1]) and is_cjk(nxt[0]):
            out += nxt
        else:
            out += " " + nxt
    return out


def hairline() -> str:
    """1px currentColor rule, thinned with scaleY(~0.45). Used after lede and for ---."""
    return (
        '<p style="margin:18px 0 6px !important;font-size:0 !important;'
        "line-height:0 !important;border-top:1px solid currentColor !important;"
        'transform:scaleY(0.45) !important;transform-origin:center center !important;">'
        "&nbsp;</p>"
    )


def _font_style() -> str:
    return f"font-family:{FONT} !important;"


def md_to_html(md: str) -> str:
    """Clean Astro Nano type: lede / hairline / footnote / CJK join. No theme colors."""
    md = re.sub(r"^---\n.*?\n---\n", "", md, count=1, flags=re.S)
    out: list[str] = []
    buf: list[str] = []
    lede_emitted = False
    h2_count = 0

    def inline(text: str) -> str:
        text = MD_LINK_RE.sub(lambda m: wechat_anchor(m.group(1), m.group(2)), text)
        text = re.sub(
            r"`([^`]+)`",
            lambda m: (
                f'<span style="font-family:{CODE_FONT} !important;font-size:14px !important;'
                f'font-weight:600 !important;word-break:break-all !important;">{m.group(1)}</span>'
            ),
            text,
        )
        text = re.sub(
            r"\*\*([^*]+)\*\*",
            r'<strong style="font-weight:700 !important;">\1</strong>',
            text,
        )
        return text

    def format_h2_title(title: str) -> str:
        m = H2_NUM_RE.match(title)
        if not m:
            return inline(title)
        return (
            f'<span style="font-size:14px !important;font-family:{CODE_FONT} !important;'
            f'font-weight:700 !important;opacity:0.6 !important;">{m.group(1)}.</span> {inline(m.group(2))}'
        )

    def emit_p(text: str, kind: str) -> None:
        if kind == "lede":
            style = (
                f"{_font_style()}font-size:16.5px !important;"
                f"line-height:1.8 !important;"
                f"margin:0 0 12px !important;"
            )
        elif kind == "footnote":
            style = (
                f"{_font_style()}font-size:14px !important;"
                f"line-height:1.6 !important;"
                f"margin:10px 0 24px !important;opacity:0.75 !important;"
            )
        elif kind == "badge":
            style = (
                f"font-family:{CODE_FONT} !important;font-size:12.5px !important;"
                f"line-height:1.5 !important;margin:0 0 10px !important;opacity:0.65 !important;"
            )
        else:
            style = (
                f"{_font_style()}font-size:16px !important;"
                f"line-height:1.8 !important;"
                f"margin:0 0 16px !important;"
            )
        out.append(f'<p style="{style}">{text}</p>')

    def flush_p() -> None:
        nonlocal lede_emitted
        if not buf:
            return
        raw = join_wrapped_lines(buf)
        text = inline(raw)
        buf.clear()
        if YUANYWEN_LINE_RE.match(raw):
            emit_p(text, "footnote")
            return
        if not lede_emitted:
            emit_p(text, "lede")
            out.append(hairline())
            lede_emitted = True
            return
        if raw.startswith("`") and ("·" in raw or "/" in raw) and len(raw) < 80:
            emit_p(text, "badge")
            return
        emit_p(text, "body")

    for line in md.splitlines():
        if line.startswith("## "):
            flush_p()
            h2_count += 1
            top = 20 if h2_count == 1 else 38
            out.append(
                f'<h2 style="{_font_style()}font-size:17px !important;'
                f"font-weight:700 !important;"
                f'line-height:1.45 !important;margin:{top}px 0 8px !important;">'
                f"{format_h2_title(line[3:].strip())}</h2>"
            )
        elif line.startswith("### "):
            flush_p()
            out.append(
                f'<h3 style="{_font_style()}font-size:15.5px !important;'
                f'font-weight:600 !important;margin:20px 0 6px !important;">'
                f"{inline(line[4:])}</h3>"
            )
        elif line.startswith("# "):
            flush_p()
        elif line.startswith("> "):
            flush_p()
            out.append(
                f'<p style="{_font_style()}font-size:15px !important;'
                f"line-height:1.75 !important;"
                f"margin:0 0 16px !important;padding:0 0 0 10px !important;"
                f'border-left:2px solid currentColor !important;opacity:0.85 !important;">{inline(line[2:])}</p>'
            )
        elif line.strip() == "---":
            flush_p()
            out.append(hairline())
        elif YUANYWEN_LINE_RE.match(line.strip()):
            flush_p()
            emit_p(inline(line.strip()), "footnote")
        elif line.startswith("- "):
            flush_p()
            out.append(
                f'<p style="{_font_style()}font-size:16px !important;'
                f"line-height:1.8 !important;"
                f'margin:0 0 6px !important;">· {inline(line[2:])}</p>'
            )
        elif not line.strip():
            flush_p()
        else:
            buf.append(line)
    flush_p()
    return f"<section>{chr(10).join(out)}</section>"


def parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    if not m:
        return {}, text
    meta: dict[str, str] = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip()
    return meta, m.group(2)


def api(url: str, data: bytes | None = None, headers: dict[str, str] | None = None) -> dict:
    req = urllib.request.Request(url, data=data, headers=headers or {})
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", "replace")
        raise SystemExit(f"HTTP {exc.code}: {body}") from exc


def token(appid: str, secret: str) -> str:
    q = urllib.parse.urlencode({"grant_type": "client_credential", "appid": appid, "secret": secret})
    data = api(f"https://api.weixin.qq.com/cgi-bin/token?{q}")
    if "access_token" not in data:
        raise SystemExit(f"token failed: {data}")
    return data["access_token"]


def upload_cover(tok: str, cover: Path) -> str:
    boundary = "----agenthorizon"
    raw = cover.read_bytes()
    filename = cover.name
    mime = "image/png" if cover.suffix.lower() == ".png" else "image/jpeg"
    head = (
        f"--{boundary}\r\n"
        f'Content-Disposition: form-data; name="media"; filename="{filename}"\r\n'
        f"Content-Type: {mime}\r\n\r\n"
    ).encode()
    tail = f"\r\n--{boundary}--\r\n".encode()
    body = head + raw + tail
    data = api(
        f"https://api.weixin.qq.com/cgi-bin/material/add_material?access_token={tok}&type=thumb",
        data=body,
        headers={"Content-Type": f"multipart/form-data; boundary={boundary}"},
    )
    media_id = data.get("media_id")
    if not media_id:
        raise SystemExit(f"cover upload failed: {data}")
    return media_id


def add_draft(tok: str, article: dict) -> dict:
    payload = json.dumps({"articles": [article]}, ensure_ascii=False).encode("utf-8")
    return api(
        f"https://api.weixin.qq.com/cgi-bin/draft/add?access_token={tok}",
        data=payload,
        headers={"Content-Type": "application/json; charset=utf-8"},
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("markdown")
    parser.add_argument("--cover", help="Cover image. Required only when pushing a draft.")
    parser.add_argument("--html-out", help="Write typeset HTML and exit. Does not push.")
    args = parser.parse_args()

    text = Path(args.markdown).read_text(encoding="utf-8")
    meta, body = parse_frontmatter(text)
    article_html = md_to_html(body)

    if args.html_out:
        Path(args.html_out).write_text(article_html, encoding="utf-8")
        print(f"Wrote {args.html_out}")
        return

    if not args.cover:
        raise SystemExit("--cover is required when pushing a draft")

    load_local_env()
    appid = os.environ.get("WECHAT_APPID", "").strip()
    secret = os.environ.get("WECHAT_SECRET", "").strip()
    if not appid or not secret:
        raise SystemExit("Set WECHAT_APPID and WECHAT_SECRET in the environment or wechat/.env.local. Do not put them in git.")

    source_url = content_source_url(meta, body)
    tok = token(appid, secret)
    thumb = upload_cover(tok, Path(args.cover))
    article = {
        "title": meta.get("title") or Path(args.markdown).stem,
        "author": meta.get("author") or "yuseus",
        "digest": meta.get("digest") or "",
        "content": article_html,
        "thumb_media_id": thumb,
        "need_open_comment": 1,
        "only_fans_can_comment": 0,
    }
    if source_url:
        article["content_source_url"] = source_url
    result = add_draft(tok, article)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    if result.get("errcode") not in (None, 0) and "media_id" not in result:
        sys.exit(1)
    print("Draft created. Publish it yourself in the WeChat admin.")


if __name__ == "__main__":
    main()
