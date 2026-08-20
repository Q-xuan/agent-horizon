"""Patch Horizon so digest/post dates use Asia/Shanghai, not UTC.

Scheduled daily.yml runs at 23:00 UTC = 07:00 Asia/Shanghai. Horizon names
_posts/YYYY-MM-DD-summary-*.md from datetime.now(timezone.utc), so a morning
Shanghai run still writes yesterday's UTC date.

Fetch-window `now - hours` stays UTC.
"""
from pathlib import Path
import sys

IMPORT_NEEDLE = """from datetime import datetime, timedelta, timezone
from pathlib import Path
"""
IMPORT_PATCH = """from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo
from pathlib import Path
"""

DATE_NEEDLE = 'datetime.now(timezone.utc).strftime("%Y-%m-%d")'
DATE_PATCH = 'datetime.now(ZoneInfo("Asia/Shanghai")).strftime("%Y-%m-%d")'


def main() -> None:
    path = Path(sys.argv[1] if len(sys.argv) > 1 else "src/orchestrator.py")
    text = path.read_text()
    if 'ZoneInfo("Asia/Shanghai")' in text:
        print(f"already patched: {path}")
        return
    if IMPORT_NEEDLE not in text:
        raise SystemExit(f"import patch target not found in {path}")
    if DATE_NEEDLE not in text:
        raise SystemExit(f"date patch target not found in {path}")
    count = text.count(DATE_NEEDLE)
    text = text.replace(IMPORT_NEEDLE, IMPORT_PATCH, 1)
    text = text.replace(DATE_NEEDLE, DATE_PATCH)
    path.write_text(text)
    print(f"patched {path} digest dates to Asia/Shanghai ({count} occurrence(s))")


if __name__ == "__main__":
    main()
