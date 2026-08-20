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

sys.path.insert(0, str(Path(__file__).resolve().parent))

from digest_items import load_local_env


# WeChat keeps a CSS whitelist. Inter/Georgia/rgba/text-underline-offset get dropped.
# Nano, mapped to fonts the editor actually paints: 宋体 body, 苹方 headings, stone colors.
SANS = "PingFang SC, Hiragino Sans GB, Microsoft YaHei, Helvetica, sans-serif"
SERIF = "Optima, Georgia, Songti SC, STSong, serif"
INK = "#111111"
MUTED = "#78716c"
LINE = "#e7e5e4"
CHIP = "#e7e5e4"
STONE = "#f5f5f4"


def md_to_html(md: str) -> str:
    """Astro Nano colors/type, written for WeChat's inline-style whitelist."""
    md = re.sub(r"^---\n.*?\n---\n", "", md, count=1, flags=re.S)
    out: list[str] = []
    buf: list[str] = []

    def flush_p() -> None:
        if not buf:
            return
        text = inline(" ".join(x.strip() for x in buf))
        out.append(
            f'<p style="font-family:{SERIF} !important;font-size:16px !important;'
            f'line-height:1.85 !important;letter-spacing:0.5px !important;'
            f'margin:0 0 18px !important;color:{MUTED} !important;">{text}</p>'
        )
        buf.clear()

    def inline(text: str) -> str:
        text = re.sub(
            r"\[([^\]]+)\]\(([^)]+)\)",
            rf'<a href="\2" style="font-family:{SANS} !important;color:{INK} !important;'
            rf'text-decoration:underline !important;'
            rf'text-decoration-color:{LINE} !important;">\1</a>',
            text,
        )
        text = re.sub(
            r"`([^`]+)`",
            rf'<span style="font-family:{SANS} !important;font-size:14px !important;'
            rf'background-color:{CHIP} !important;color:{INK} !important;'
            rf'padding:1px 6px !important;">{chr(92)}1</span>'.replace(chr(92)+"1", r"\1"),
            text,
        )
        text = re.sub(
            r"\*\*([^*]+)\*\*",
            rf'<strong style="color:{INK} !important;font-weight:600 !important;">\1</strong>',
            text,
        )
        return text

    for line in md.splitlines():
        if line.startswith("## "):
            flush_p()
            out.append(
                f'<h2 style="font-family:{SANS} !important;font-size:16px !important;'
                f'font-weight:600 !important;line-height:1.4 !important;'
                f'margin:36px 0 12px !important;padding:0 0 8px !important;'
                f'border-bottom:1px solid {LINE} !important;color:{INK} !important;">'
                f'{inline(line[3:])}</h2>'
            )
        elif line.startswith("### "):
            flush_p()
            out.append(
                f'<h3 style="font-family:{SANS} !important;font-size:15px !important;'
                f'font-weight:600 !important;margin:24px 0 8px !important;'
                f'color:{INK} !important;">{inline(line[4:])}</h3>'
            )
        elif line.startswith("# "):
            flush_p()
        elif line.startswith("> "):
            flush_p()
            out.append(
                f'<p style="font-family:{SERIF} !important;font-size:15px !important;'
                f'line-height:1.8 !important;margin:0 0 18px !important;'
                f'color:{MUTED} !important;">{inline(line[2:])}</p>'
            )
        elif line.strip() == "---":
            flush_p()
            out.append(
                f'<p style="border-top:1px solid {LINE} !important;margin:28px 0 !important;'
                f'font-size:0 !important;line-height:0 !important;">&nbsp;</p>'
            )
        elif line.startswith("- "):
            flush_p()
            out.append(
                f'<p style="font-family:{SERIF} !important;font-size:16px !important;'
                f'line-height:1.85 !important;margin:0 0 6px !important;'
                f'color:{MUTED} !important;">· {inline(line[2:])}</p>'
            )
        elif not line.strip():
            flush_p()
        else:
            buf.append(line)
    flush_p()
    inner = "\n".join(out)
    return (
        f'<section style="background-color:{STONE} !important;padding:12px 4px !important;">'
        f"{inner}</section>"
    )


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

    load_local_env()
    appid = os.environ.get("WECHAT_APPID", "").strip()
    secret = os.environ.get("WECHAT_SECRET", "").strip()
    if not appid or not secret:
        raise SystemExit("Set WECHAT_APPID and WECHAT_SECRET in the environment or wechat/.env.local. Do not put them in git.")

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
