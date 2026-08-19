#!/usr/bin/env python3
"""Push a local markdown post to the WeChat official-account draft box.

Requires WECHAT_APPID / WECHAT_SECRET and a cover image.
Creates a draft only. Does not mass-send.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path


def md_to_html(md: str) -> str:
    """Small WeChat-safe converter: headings, quotes, lists, paragraphs, links."""
    md = re.sub(r"^---\n.*?\n---\n", "", md, count=1, flags=re.S)
    out: list[str] = []
    buf: list[str] = []

    def flush_p() -> None:
        if not buf:
            return
        text = inline(" ".join(x.strip() for x in buf))
        out.append(
            f'<p style="font-size:16px;line-height:1.8;margin:0 0 16px;color:#1f1f1f;">{text}</p>'
        )
        buf.clear()

    def inline(text: str) -> str:
        text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', text)
        text = re.sub(r"`([^`]+)`", r'<code>\1</code>', text)
        text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
        return text

    for line in md.splitlines():
        if line.startswith("## "):
            flush_p()
            out.append(
                f'<h2 style="font-size:18px;margin:28px 0 12px;color:#111;">{inline(line[3:])}</h2>'
            )
        elif line.startswith("### "):
            flush_p()
            out.append(
                f'<h3 style="font-size:16px;margin:20px 0 8px;color:#333;">{inline(line[4:])}</h3>'
            )
        elif line.startswith("# "):
            flush_p()
        elif line.startswith("> "):
            flush_p()
            out.append(
                f'<blockquote style="border-left:3px solid #ddd;margin:0 0 16px;padding:0 0 0 12px;color:#555;">{inline(line[2:])}</blockquote>'
            )
        elif line.strip() == "---":
            flush_p()
            out.append('<hr style="border:none;border-top:1px solid #eee;margin:24px 0;" />')
        elif line.startswith("- "):
            flush_p()
            out.append(
                f'<p style="font-size:16px;line-height:1.8;margin:0 0 8px;color:#1f1f1f;">• {inline(line[2:])}</p>'
            )
        elif not line.strip():
            flush_p()
        else:
            buf.append(line)
    flush_p()
    return "\n".join(out)


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
    parser.add_argument("--cover", required=True)
    args = parser.parse_args()

    appid = os.environ.get("WECHAT_APPID", "").strip()
    secret = os.environ.get("WECHAT_SECRET", "").strip()
    if not appid or not secret:
        raise SystemExit("Set WECHAT_APPID and WECHAT_SECRET first.")

    text = Path(args.markdown).read_text(encoding="utf-8")
    meta, body = parse_frontmatter(text)
    html = md_to_html(body)
    tok = token(appid, secret)
    thumb = upload_cover(tok, Path(args.cover))
    result = add_draft(
        tok,
        {
            "title": meta.get("title") or Path(args.markdown).stem,
            "author": meta.get("author") or "pengyu",
            "digest": meta.get("digest") or "",
            "content": html,
            "thumb_media_id": thumb,
            "need_open_comment": 1,
            "only_fans_can_comment": 0,
        },
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))
    if result.get("errcode") not in (None, 0) and "media_id" not in result:
        sys.exit(1)
    print("Draft created. Publish it yourself in the WeChat admin.")


if __name__ == "__main__":
    main()
