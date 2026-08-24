#!/usr/bin/env python3
"""Apply source-authority score adjustments after Horizon analysis.

Horizon's Config model forbids unknown fields, so knobs live in
``data/source_tiers.json`` (not config.json). This module is the
deterministic enforcement layer: analysis.md can bias the model, but
caps / boosts here actually change who survives profile thresholds.
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any, Callable, Iterable
from urllib.parse import urlparse


DEFAULT_POLICY_PATH = Path(__file__).resolve().parents[1] / "data" / "source_tiers.json"
URL_RE = re.compile(r"https?://[^\s)\]>\"'<>]+", re.IGNORECASE)

Printer = Callable[[str], None]


def load_policy(path: str | Path | None = None) -> dict[str, Any]:
    policy_path = Path(path) if path else DEFAULT_POLICY_PATH
    return json.loads(policy_path.read_text(encoding="utf-8"))


def _source_type(item: Any) -> str:
    value = getattr(item, "source_type", "")
    if hasattr(value, "value"):
        value = value.value
    return str(value or "").strip().lower()


def _item_id(item: Any) -> str:
    return str(getattr(item, "id", "") or "")


def _metadata(item: Any) -> dict[str, Any]:
    meta = getattr(item, "metadata", None)
    return meta if isinstance(meta, dict) else {}


def _feed_name(item: Any) -> str:
    return str(_metadata(item).get("feed_name") or "").strip()


def _host(url: str) -> str:
    try:
        host = (urlparse(url).hostname or "").lower()
    except ValueError:
        return ""
    if host.startswith("www."):
        host = host[4:]
    return host


def _host_matches(host: str, suffixes: Iterable[str]) -> bool:
    host = (host or "").lower()
    if not host:
        return False
    for suffix in suffixes:
        suffix = suffix.lower().lstrip(".")
        if host == suffix or host.endswith("." + suffix):
            return True
    return False


def extract_urls(item: Any) -> list[str]:
    found: list[str] = []
    raw_url = str(getattr(item, "url", "") or "")
    if raw_url:
        found.append(raw_url)
    blob = str(getattr(item, "content", "") or "")
    found.extend(URL_RE.findall(blob))
    # Preserve order, drop empties.
    seen: set[str] = set()
    urls: list[str] = []
    for url in found:
        url = url.rstrip(".,;]")
        if url and url not in seen:
            seen.add(url)
            urls.append(url)
    return urls


def github_owner(url: str) -> str:
    try:
        parsed = urlparse(url)
    except ValueError:
        return ""
    host = (parsed.hostname or "").lower()
    if host not in {"github.com", "www.github.com"}:
        return ""
    parts = [part for part in parsed.path.split("/") if part]
    return parts[0] if parts else ""


def has_primary_official_url(item: Any, policy: dict[str, Any]) -> bool:
    official_hosts = policy.get("official_hosts") or []
    official_owners = {owner.lower() for owner in policy.get("official_github_owners") or []}
    never_hosts = policy.get("never_official_hosts") or []
    for url in extract_urls(item):
        host = _host(url)
        if not host or _host_matches(host, never_hosts):
            continue
        owner = github_owner(url)
        if owner and owner.lower() in official_owners:
            return True
        if host in {"github.com", "www.github.com"}:
            continue
        if _host_matches(host, official_hosts):
            return True
    return False


def is_github_release(item: Any) -> bool:
    item_id = _item_id(item)
    if ":release:" in item_id:
        return True
    event_type = str(_metadata(item).get("event_type") or "")
    return event_type == "ReleaseEvent"


def classify_tier(item: Any, policy: dict[str, Any]) -> str:
    source = _source_type(item)
    feed = _feed_name(item)

    if source == "google_news":
        return "secondary"
    if source in {"reddit", "twitter", "ossinsight"}:
        return "community"
    if source == "hackernews":
        return "community"
    if source == "github":
        return "official" if is_github_release(item) else "community"

    if source == "rss":
        if feed in set(policy.get("official_rss_names") or []):
            return "official"
        if feed in set(policy.get("secondary_rss_names") or []):
            return "secondary"
        if feed in set(policy.get("community_rss_names") or []):
            return "community"
        if feed in set(policy.get("deals_rss_names") or []):
            return "deals"
        if feed in set(policy.get("practitioner_rss_names") or []):
            return "practitioner"
        return "practitioner"

    return "practitioner"


def _analysis(item: Any) -> Any:
    processing = getattr(item, "processing", None)
    if processing is None:
        return None
    return getattr(processing, "analysis", None)


def _clamp(score: float, policy: dict[str, Any]) -> float:
    lo = float(policy.get("score_min", 0.0))
    hi = float(policy.get("score_max", 10.0))
    return max(lo, min(hi, score))


def _annotate(item: Any, **fields: Any) -> None:
    meta = _metadata(item)
    if not isinstance(getattr(item, "metadata", None), dict):
        try:
            item.metadata = meta
        except Exception:
            return
    meta.update(fields)


def apply_item(item: Any, policy: dict[str, Any]) -> dict[str, Any]:
    """Adjust one item. Returns a small decision record."""
    analysis = _analysis(item)
    score = getattr(analysis, "score", None) if analysis is not None else None
    tier = classify_tier(item, policy)
    official_url = has_primary_official_url(item, policy)
    decision = {
        "tier": tier,
        "has_primary_official_url": official_url,
        "original_score": score,
        "adjusted_score": score,
        "action": "unchanged",
    }
    _annotate(
        item,
        source_tier=tier,
        has_primary_official_url=official_url,
    )
    if analysis is None or score is None:
        return decision

    boost = float(policy.get("official_boost", 0.0))
    new_score = float(score)
    action = "unchanged"

    if tier == "official":
        new_score = _clamp(new_score + boost, policy)
        action = "boost" if new_score != float(score) else "unchanged"
    elif tier in {"secondary", "community"} and not official_url:
        knobs = policy.get(f"{tier}_without_primary") or {}
        cap = knobs.get("score_cap")
        min_keep = knobs.get("min_score_to_keep")
        if cap is not None:
            new_score = min(new_score, float(cap))
            if new_score != float(score):
                action = "cap"
        if min_keep is not None and new_score < float(min_keep):
            new_score = 0.0
            action = "drop"
    else:
        action = "unchanged"

    new_score = _clamp(new_score, policy)
    if new_score != float(score):
        analysis.score = new_score
        reason = getattr(analysis, "reason", "") or ""
        note = f"[source_tier={tier} {action} {float(score):.1f}->{new_score:.1f}]"
        if note not in reason:
            analysis.reason = f"{reason} {note}".strip()
    decision["adjusted_score"] = new_score
    decision["action"] = action
    _annotate(item, source_tier_action=action, source_tier_score=new_score)
    return decision


def apply_source_tiers(
    items: list[Any],
    policy: dict[str, Any] | str | Path | None = None,
    printer: Printer | None = None,
) -> list[Any]:
    if not isinstance(policy, dict):
        policy = load_policy(policy)
    counts = {"boost": 0, "cap": 0, "drop": 0, "unchanged": 0}
    for item in items:
        action = apply_item(item, policy)["action"]
        counts[action] = counts.get(action, 0) + 1
    if printer:
        printer(
            "source_tiers: "
            f"boost={counts['boost']} cap={counts['cap']} "
            f"drop={counts['drop']} unchanged={counts['unchanged']}"
        )
    return items


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser(description="Validate source-tier policy JSON")
    parser.add_argument(
        "--policy",
        default=str(DEFAULT_POLICY_PATH),
        help="Path to source_tiers.json",
    )
    args = parser.parse_args()
    policy = load_policy(args.policy)
    required = (
        "official_boost",
        "secondary_without_primary",
        "community_without_primary",
        "official_rss_names",
        "secondary_rss_names",
    )
    missing = [key for key in required if key not in policy]
    if missing:
        raise SystemExit(f"source_tiers.json missing keys: {missing}")
    print(f"ok {args.policy}")


if __name__ == "__main__":
    main()
