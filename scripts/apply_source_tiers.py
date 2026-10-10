#!/usr/bin/env python3
"""Apply source-authority score adjustments after Horizon analysis.

Horizon's Config model forbids unknown fields, so knobs live in
``data/source_tiers.json`` (not config.json). This module is the
deterministic enforcement layer: analysis.md can bias the model, but
caps / boosts here actually change who survives profile thresholds.
A second pass (release_policy) collapses same-day same-product releases,
downweights pure patches, and caps harness-zone release slots.
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



SEMVER_RE = re.compile(
    r"(?i)(?:^|[^0-9])v?(\d+)\.(\d+)\.(\d+)(?:[-+][0-9A-Za-z.-]+)?(?:[^0-9]|$)"
)
RELEASE_TITLE_RE = re.compile(
    r"(?i)(\breleased?\b|\brelease\b|发布|changelog|version\s+v?\d)"
)


def _published_day(item: Any) -> str:
    raw = getattr(item, "published_at", None)
    if raw is None:
        meta = _metadata(item)
        raw = meta.get("published_at") or meta.get("published")
    if raw is None:
        return "unknown"
    if hasattr(raw, "strftime"):
        try:
            return raw.strftime("%Y-%m-%d")
        except Exception:
            return "unknown"
    text = str(raw)
    return text[:10] if len(text) >= 10 else "unknown"


def _classification_profile(item: Any) -> str:
    processing = getattr(item, "processing", None)
    classification = getattr(processing, "classification", None) if processing else None
    profile = getattr(classification, "profile", None) if classification else None
    if profile:
        return str(profile)
    # Source-config override may still be on the item.
    raw = getattr(item, "profile", None)
    if isinstance(raw, str) and raw and raw != "auto":
        return raw
    if isinstance(raw, list) and raw:
        return str(raw[0])
    return ""


def _category(item: Any) -> str:
    return str(_metadata(item).get("category") or "").strip().lower()


def github_owner_repo(url: str) -> str:
    try:
        parsed = urlparse(url)
    except ValueError:
        return ""
    host = (parsed.hostname or "").lower()
    if host not in {"github.com", "www.github.com"}:
        return ""
    parts = [part for part in parsed.path.split("/") if part]
    if len(parts) < 2:
        return ""
    return f"{parts[0]}/{parts[1]}".lower()


def extract_semver(text: str) -> tuple[int, int, int] | None:
    match = SEMVER_RE.search(text or "")
    if not match:
        return None
    return int(match.group(1)), int(match.group(2)), int(match.group(3))


def is_patch_release(item: Any) -> bool:
    """True when the best version we see is a pure patch (x.y.Z with Z>0)."""
    blob = " ".join(
        [
            str(getattr(item, "title", "") or ""),
            str(getattr(item, "url", "") or ""),
            str(getattr(item, "content", "") or "")[:500],
        ]
    )
    ver = extract_semver(blob)
    if ver is None:
        return False
    _major, _minor, patch = ver
    return patch > 0


def is_release_like(item: Any, policy: dict[str, Any]) -> bool:
    if is_github_release(item):
        return True
    feed = _feed_name(item)
    aliases = (policy.get("release_policy") or {}).get("product_aliases") or {}
    if feed in aliases:
        return True
    if feed.lower().endswith("changelog") or "changelog" in feed.lower():
        return True
    title = str(getattr(item, "title", "") or "")
    url = str(getattr(item, "url", "") or "")
    if "/releases/" in url or "/tags/" in url:
        return True
    if extract_semver(title) and RELEASE_TITLE_RE.search(title):
        return True
    return False


def release_product_key(item: Any, policy: dict[str, Any]) -> str:
    aliases = (policy.get("release_policy") or {}).get("product_aliases") or {}
    feed = _feed_name(item)
    if feed in aliases:
        return str(aliases[feed]).lower()
    for url in extract_urls(item):
        repo = github_owner_repo(url)
        if repo:
            return str(aliases.get(repo, repo)).lower()
        host = _host(url)
        # code.claude.com changelog pages → claude-code product
        if host in {"code.claude.com", "www.code.claude.com"}:
            return str(aliases.get("code.claude.com/claude-code", "anthropics/claude-code")).lower()
    title = str(getattr(item, "title", "") or "").lower()
    if feed:
        return str(aliases.get(feed, f"feed:{feed}")).lower()
    return f"title:{title[:60]}"


def is_harness_zone(item: Any, policy: dict[str, Any]) -> bool:
    rp = policy.get("release_policy") or {}
    profiles = {p.lower() for p in rp.get("harness_profiles") or ["harness-arch"]}
    categories = {c.lower() for c in rp.get("harness_categories") or []}
    if _classification_profile(item).lower() in profiles:
        return True
    if _category(item) in categories:
        return True
    raw = getattr(item, "profile", None)
    if isinstance(raw, str) and raw.lower() in profiles:
        return True
    if isinstance(raw, list) and any(str(x).lower() in profiles for x in raw):
        return True
    return False


def _set_score(item: Any, new_score: float, policy: dict[str, Any], action: str) -> None:
    analysis = _analysis(item)
    if analysis is None or getattr(analysis, "score", None) is None:
        return
    old = float(analysis.score)
    new_score = _clamp(new_score, policy)
    if new_score == old:
        return
    analysis.score = new_score
    reason = getattr(analysis, "reason", "") or ""
    note = f"[release_policy {action} {old:.1f}->{new_score:.1f}]"
    if note not in reason:
        analysis.reason = f"{reason} {note}".strip()
    _annotate(item, release_policy_action=action, release_policy_score=new_score)


def apply_release_policy(
    items: list[Any],
    policy: dict[str, Any],
    printer: Printer | None = None,
) -> list[Any]:
    """Same-day product dedupe, patch downweight, harness release cap."""
    rp = policy.get("release_policy") or {}
    if not rp.get("enabled", False):
        return items

    patch_penalty = float(rp.get("patch_penalty", 1.5))
    patch_cap = float(rp.get("patch_score_cap", 5.5))
    harness_cap = int(rp.get("harness_release_cap", 3))
    do_dedupe = bool(rp.get("same_day_dedupe", True))

    counts = {"patch_down": 0, "dedupe_drop": 0, "harness_cap_drop": 0}

    # 1) Downweight pure patches first so dedupe/cap see adjusted scores.
    if patch_penalty > 0:
        for item in items:
            if not is_release_like(item, policy):
                continue
            if not is_patch_release(item):
                continue
            analysis = _analysis(item)
            if analysis is None or getattr(analysis, "score", None) is None:
                continue
            old = float(analysis.score)
            new = min(old - patch_penalty, patch_cap)
            if new < old:
                _set_score(item, new, policy, "patch_down")
                counts["patch_down"] += 1

    # 2) Same calendar day + same product → keep highest score only.
    if do_dedupe:
        groups: dict[tuple[str, str], list[Any]] = {}
        for item in items:
            if not is_release_like(item, policy):
                continue
            key = (_published_day(item), release_product_key(item, policy))
            groups.setdefault(key, []).append(item)
        for _key, group in groups.items():
            if len(group) < 2:
                continue

            def score_of(it: Any) -> float:
                analysis = _analysis(it)
                if analysis is None or getattr(analysis, "score", None) is None:
                    return -1.0
                return float(analysis.score)

            ranked = sorted(group, key=score_of, reverse=True)
            for loser in ranked[1:]:
                _set_score(loser, 0.0, policy, "same_day_dedupe")
                counts["dedupe_drop"] += 1

    # 3) Cap how many release-like items can survive in the harness zone.
    if harness_cap >= 0:
        harness_releases = [
            item
            for item in items
            if is_release_like(item, policy) and is_harness_zone(item, policy)
        ]

        def score_of(it: Any) -> float:
            analysis = _analysis(it)
            if analysis is None or getattr(analysis, "score", None) is None:
                return -1.0
            return float(analysis.score)

        # Skip already-zeroed (deduped) items when counting survivors.
        alive = [it for it in harness_releases if score_of(it) > 0]
        ranked = sorted(alive, key=score_of, reverse=True)
        for loser in ranked[harness_cap:]:
            _set_score(loser, 0.0, policy, "harness_cap")
            counts["harness_cap_drop"] += 1

    if printer:
        printer(
            "release_policy: "
            f"patch_down={counts['patch_down']} "
            f"dedupe_drop={counts['dedupe_drop']} "
            f"harness_cap_drop={counts['harness_cap_drop']}"
        )
    return items


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
    return apply_release_policy(items, policy, printer=printer)


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
