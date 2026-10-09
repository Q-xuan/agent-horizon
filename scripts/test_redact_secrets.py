#!/usr/bin/env python3
import importlib.util
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

spec = importlib.util.spec_from_file_location("redact_secrets", ROOT / "redact_secrets.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

spec2 = importlib.util.spec_from_file_location("scrape_no_rss", ROOT / "scrape_no_rss.py")
scrape = importlib.util.module_from_spec(spec2)
spec2.loader.exec_module(scrape)

# Shape matches real Apify tokens: apify_api_ + alphanumerics only.
FAKE = "apify_api_" + ("DEADBEEF" * 4)  # synthetic; not a real credential
URL = f"https://api.apify.com/v2/acts/altimis~scweet/runs?token={FAKE}"


class RedactTest(unittest.TestCase):
    def test_query_param(self):
        out = mod.redact(f"Failed: Client error 402 for url '{URL}'")
        self.assertNotIn(FAKE, out)
        self.assertIn("token=<redacted>", out)

    def test_wrapped_lines(self):
        # Actions logger wraps mid-URL so token= starts a new line.
        a, b = FAKE[:40], FAKE[40:]
        line1 = f"token={a}"
        line2 = f"{b}'"
        out1, out2 = mod.redact(line1), mod.redact(line2)
        self.assertNotIn(a, out1)
        self.assertIn("token=<redacted>", out1)
        # leftover suffix alone is not the secret; joined view must not reconstruct it
        self.assertNotIn(FAKE, out1 + out2)

    def test_bearer(self):
        out = mod.redact(f"Authorization: Bearer {FAKE}")
        self.assertNotIn(FAKE, out)
        self.assertIn("Bearer <redacted>", out)

    def test_scrape_helper(self):
        out = scrape.redact_secrets(URL)
        self.assertNotIn(FAKE, out)

    def test_apify_urls_have_no_token_query(self):
        src = (ROOT / "scrape_no_rss.py").read_text(encoding="utf-8")
        self.assertNotIn("?token={token}", src)
        self.assertIn('Authorization": f"Bearer {token}"', src)


if __name__ == "__main__":
    unittest.main()
