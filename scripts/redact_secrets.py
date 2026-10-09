#!/usr/bin/env python3
"""Stream-filter stdin → stdout, redacting Apify/API token leakage.

Used by Actions around Horizon and scrape_no_rss so wrapped log lines cannot
reassemble a secret that ::add-mask:: missed.
"""
from __future__ import annotations

import re
import sys

TOKEN_PARAM = re.compile(r"(?i)(\b(?:token|access_token)=)([^\s&<>]+)")
BEARER = re.compile(r"(?i)(Bearer\s+)(\S+)")
APIFY = re.compile(r"\bapify_api_[A-Za-z0-9]+")


def redact(text: str) -> str:
    text = TOKEN_PARAM.sub(r"\1<redacted>", text)
    text = BEARER.sub(r"\1<redacted>", text)
    text = APIFY.sub("apify_api_<redacted>", text)
    return text


def main() -> int:
    for line in sys.stdin:
        sys.stdout.write(redact(line))
        sys.stdout.flush()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
