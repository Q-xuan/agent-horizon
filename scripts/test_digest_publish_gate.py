#!/usr/bin/env python3
"""Checks for the daily publish gate and schedule contract.

Run: python3 scripts/test_digest_publish_gate.py
"""

from __future__ import annotations

from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo
import io
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parent))

from digest_publish_gate import (
    should_skip,
    summary_zh_url,
    today_shanghai,
    parse_force,
    main,
)

ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github" / "workflows" / "daily.yml"


class GateLogicTests(unittest.TestCase):
    def test_schedule_skips_when_page_is_live(self) -> None:
        self.assertTrue(
            should_skip(event_name="schedule", force=False, http_code=200)
        )

    def test_schedule_runs_on_404_or_unknown(self) -> None:
        self.assertFalse(
            should_skip(event_name="schedule", force=False, http_code=404)
        )
        self.assertFalse(
            should_skip(event_name="schedule", force=False, http_code=None)
        )

    def test_manual_dispatch_always_runs(self) -> None:
        self.assertFalse(
            should_skip(
                event_name="workflow_dispatch", force=False, http_code=200
            )
        )

    def test_force_rebuilds_even_if_live(self) -> None:
        self.assertFalse(
            should_skip(event_name="schedule", force=True, http_code=200)
        )
        self.assertTrue(parse_force("true"))
        self.assertFalse(parse_force("false"))

    def test_shanghai_url_and_date(self) -> None:
        self.assertEqual(
            summary_zh_url("2026-09-17"),
            "https://q-xuan.github.io/agent-horizon/2026/09/17/summary-zh.html",
        )
        now = datetime(2026, 9, 16, 23, 10, tzinfo=ZoneInfo("UTC"))
        self.assertEqual(today_shanghai(now), "2026-09-17")

    def test_cli_schedule_200_skips(self) -> None:
        buf = io.StringIO()
        old = sys.stdout
        sys.stdout = buf
        try:
            rc = main(
                [
                    "--event",
                    "schedule",
                    "--http-code",
                    "200",
                    "--date",
                    "2026-09-17",
                ]
            )
        finally:
            sys.stdout = old
        self.assertEqual(rc, 0)
        self.assertIn("skip=true", buf.getvalue())


class WorkflowContractTests(unittest.TestCase):
    def test_early_retry_crons_and_no_wechat(self) -> None:
        text = WORKFLOW.read_text(encoding="utf-8")
        self.assertIn('cron: "13 20 * * *"', text)
        self.assertIn('cron: "17 21 * * *"', text)
        self.assertIn('cron: "23 22 * * *"', text)
        self.assertIn('cron: "37 23 * * *"', text)
        self.assertNotIn('cron: "0 23 * * *"', text)
        self.assertNotIn('cron: "30 23 * * *"', text)
        self.assertIn("digest_publish_gate.py", text)
        self.assertIn("needs.gate.outputs.skip", text)
        self.assertIn("shanghai_digest_date.py", text)
        self.assertNotIn("WECHAT_SECRET=", text)
        self.assertNotIn("draft/add", text)
        self.assertIn("cancel-in-progress: false", text)
        self.assertIn("group: daily-digest", text)


if __name__ == "__main__":
    unittest.main()
