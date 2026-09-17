#!/usr/bin/env python3
"""Fail Daily Agent Digest when AI scoring is dead or the digest is empty.

Parses Horizon stdout (and optional ZH summary). Does not fail solely
because some RSS feeds returned 429.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

FAIL_MESSAGE = "Digest AI failed or selected 0 items"
DEFAULT_MIN_AI_ERRORS = 5

ANSI_RE = re.compile(r"\x1b\[[0-9;]*[mK]")
ANALYZED_RE = re.compile(r"Analyzed (\d+) items with AI")
SELECTED_RE = re.compile(r"Selected (\d+) items")
FETCHED_RE = re.compile(r"Fetched (\d+) items from all sources")

EMPTY_ZH_MARKERS = (
    "没有达到重要性阈值",
    "今日暂无重要动态",
)


def strip_ansi(text: str) -> str:
    return ANSI_RE.sub("", text)


def last_int(pattern: re.Pattern[str], text: str) -> int | None:
    matches = pattern.findall(text)
    if not matches:
        return None
    return int(matches[-1])


def count_ai_failures(text: str) -> tuple[int, int]:
    """Return (error-analyzing count, InternalServerError count)."""
    analyze_errors = len(re.findall(r"Error analyzing item", text))
    gateway_errors = len(re.findall(r"InternalServerError", text))
    retry_errors = len(re.findall(r"RetryError", text))
    # RetryError is the wrapper around exhausted analyze retries.
    gateway_errors = max(gateway_errors, retry_errors)
    return analyze_errors, gateway_errors


def is_quiet_day(text: str, fetched: int | None, analyzed: int | None) -> bool:
    if "No new content found" in text:
        return True
    if fetched == 0 and (analyzed is None or analyzed == 0):
        return True
    return False


def zh_is_empty(path: Path | None) -> bool | None:
    """True if ZH digest is missing/placeholder. None if no path given."""
    if path is None:
        return None
    if not path.is_file():
        return True
    body = path.read_text(encoding="utf-8")
    if any(marker in body for marker in EMPTY_ZH_MARKERS):
        return True
    # Front matter only, or no scored items.
    stripped = re.sub(r"^---\n.*?\n---\n", "", body, count=1, flags=re.S).strip()
    if not stripped:
        return True
    if "⭐️" not in body and not re.search(r"^### \[", body, re.M):
        return True
    return False


def evaluate(
    log_text: str,
    zh_path: Path | None = None,
    min_ai_errors: int = DEFAULT_MIN_AI_ERRORS,
) -> list[str]:
    """Return failure reasons. Empty list means the digest looks healthy."""
    text = strip_ansi(log_text)
    fetched = last_int(FETCHED_RE, text)
    analyzed = last_int(ANALYZED_RE, text)
    selected = last_int(SELECTED_RE, text)
    analyze_errors, gateway_errors = count_ai_failures(text)
    ai_errors = max(analyze_errors, gateway_errors)
    quiet = is_quiet_day(text, fetched, analyzed)
    empty_zh = zh_is_empty(zh_path)

    reasons: list[str] = []
    items_available = (analyzed or 0) > 0 or (fetched or 0) > 0 or (
        analyzed is None and fetched is None and not quiet and "Analyzing content with AI" in text
    )

    if ai_errors >= min_ai_errors:
        reasons.append(
            f"AI/gateway failures: Error analyzing={analyze_errors} "
            f"InternalServerError/RetryError={gateway_errors}"
        )

    if not quiet and items_available and selected == 0:
        reasons.append(
            f"Selected 0 items after analyzing {analyzed if analyzed is not None else '?'} "
            f"(fetched {fetched if fetched is not None else '?'})"
        )

    if not quiet and items_available and empty_zh is True:
        zh_name = zh_path.as_posix() if zh_path else "summary-zh"
        reasons.append(f"empty ZH summary: {zh_name}")

    if not quiet and selected is None and analyzed is None and fetched is None:
        # Horizon exited 0 but produced no scrape/AI summary lines.
        if empty_zh is True or empty_zh is None:
            reasons.append("Horizon log has no Analyzed/Selected lines")

    return reasons


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--log", required=True, type=Path, help="Horizon stdout/stderr capture")
    parser.add_argument("--zh", type=Path, help="Today's _posts/YYYY-MM-DD-summary-zh.md")
    parser.add_argument(
        "--min-ai-errors",
        type=int,
        default=DEFAULT_MIN_AI_ERRORS,
        help="Fail when analyze/gateway errors reach this count (default 5)",
    )
    args = parser.parse_args(argv)

    if not args.log.is_file():
        print(FAIL_MESSAGE, file=sys.stderr)
        print(f"missing Horizon log: {args.log}", file=sys.stderr)
        return 1

    reasons = evaluate(
        args.log.read_text(encoding="utf-8", errors="replace"),
        zh_path=args.zh,
        min_ai_errors=args.min_ai_errors,
    )
    if not reasons:
        print("Digest health ok")
        return 0

    print(FAIL_MESSAGE, file=sys.stderr)
    for reason in reasons:
        print(reason, file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
