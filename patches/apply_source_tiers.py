"""Patch Horizon to apply source-authority score knobs after analysis.

Horizon rejects unknown config.json fields (extra=forbid), so the policy
file is data/source_tiers.json and this hook runs between analyze and
digest selection.
"""
from pathlib import Path
import sys

NEEDLE = '''            analyzed_items = await self.analyze_items(merged_items)
            self.console.print(
                f"{self.icons['ai']} Analyzed {len(analyzed_items)} items with AI\\n"
            )
'''
PATCH = '''            analyzed_items = await self.analyze_items(merged_items)
            from src.apply_source_tiers import apply_source_tiers
            analyzed_items = apply_source_tiers(
                analyzed_items,
                "data/source_tiers.json",
                printer=self.console.print,
            )
            self.console.print(
                f"{self.icons['ai']} Analyzed {len(analyzed_items)} items with AI\\n"
            )
'''


def main() -> None:
    path = Path(sys.argv[1] if len(sys.argv) > 1 else "src/orchestrator.py")
    text = path.read_text()
    if "apply_source_tiers(" in text:
        print(f"already patched: {path}")
        return
    if NEEDLE not in text:
        raise SystemExit(f"patch target not found in {path}")
    path.write_text(text.replace(NEEDLE, PATCH, 1))
    print(f"patched {path} with source-tier score adjustments")


if __name__ == "__main__":
    main()
