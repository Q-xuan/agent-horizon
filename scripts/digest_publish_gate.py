#!/usr/bin/env python3
"""Decide whether Daily Agent Digest should run Horizon again.

Scheduled ticks are retries. If today's Asia/Shanghai summary-zh is already
HTTP 200 on Pages, skip the 30–50 minute Horizon run. Manual dispatch and
--force always build.

Prints GitHub Actions outputs:
  skip=true|false
  date=YYYY-MM-DD
  url=https://...
"""

from __future__ import annotations

import argparse
import os
import sys
import urllib.error
import urllib.request
from datetime import datetime
from zoneinfo import ZoneInfo

PAGES_TEMPLATE = (
    "https://q-xuan.github.io/agent-horizon/{year}/{month}/{day}/summary-zh.html"
)
UA = "AgentHorizonDigestGate/1.0 (+https://github.com/Q-xuan/agent-horizon)"
SHANGHAI = ZoneInfo("Asia/Shanghai")


def today_shanghai(now: datetime | None = None) -> str:
    stamp = now.astimezone(SHANGHAI) if now else datetime.now(SHANGHAI)
    return stamp.strftime("%Y-%m-%d")


def summary_zh_url(date: str) -> str:
    year, month, day = date.split("-")
    return PAGES_TEMPLATE.format(year=year, month=month, day=day)


def parse_force(raw: str | None) -> bool:
    return (raw or "").strip().lower() in {"1", "true", "yes", "on"}


def should_skip(*, event_name: str, force: bool, http_code: int | None) -> bool:
    if force or event_name == "workflow_dispatch":
        return False
    return http_code == 200


def fetch_status(url: str, timeout: float = 20.0) -> int | None:
    headers = {"User-Agent": UA}
    for method in ("HEAD", "GET"):
        req = urllib.request.Request(url, method=method, headers=headers)
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return int(resp.status)
        except urllib.error.HTTPError as exc:
            return int(exc.code)
        except Exception:
            if method == "GET":
                return None
    return None


def emit(values: dict[str, str]) -> None:
    for key, value in values.items():
        print(f"{key}={value}")
    output_path = os.environ.get("GITHUB_OUTPUT")
    if output_path:
        with open(output_path, "a", encoding="utf-8") as handle:
            for key, value in values.items():
                handle.write(f"{key}={value}\n")
    env_path = os.environ.get("GITHUB_ENV")
    if env_path and "date" in values:
        with open(env_path, "a", encoding="utf-8") as handle:
            handle.write(f"DATE={values['date']}\n")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--event",
        default=os.environ.get("DIGEST_EVENT_NAME", "schedule"),
        help="GitHub event name (schedule or workflow_dispatch)",
    )
    parser.add_argument(
        "--force",
        default=os.environ.get("DIGEST_FORCE", "false"),
        help="Rebuild even if today's page is already live",
    )
    parser.add_argument(
        "--http-code",
        type=int,
        default=None,
        help="Skip the live probe and use this status (tests / offline)",
    )
    parser.add_argument(
        "--date",
        default=None,
        help="YYYY-MM-DD (defaults to Asia/Shanghai today)",
    )
    args = parser.parse_args(argv)

    date = args.date or today_shanghai()
    url = summary_zh_url(date)
    force = parse_force(str(args.force))
    http_code = args.http_code
    if http_code is None and not force and args.event != "workflow_dispatch":
        http_code = fetch_status(url)
    skip = should_skip(event_name=args.event, force=force, http_code=http_code)
    emit(
        {
            "skip": "true" if skip else "false",
            "date": date,
            "url": url,
            "http_code": "" if http_code is None else str(http_code),
        }
    )
    if skip:
        print(f"Already live ({http_code}): {url}", file=sys.stderr)
    else:
        print(f"Will publish ({http_code}): {url}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
