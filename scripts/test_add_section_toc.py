import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "wechat" / "scripts"))

import add_section_toc as toc  # noqa: E402

SAMPLE = """---
layout: default
title: "Horizon Summary: 2026-10-09 (ZH)"
lang: zh
---

> 从 3 条内容中筛选出 3 条重要资讯。

---

**Harness 架构**
1. [A](#item-harness-arch-1) ⭐️ 8.1/10
2. [B](#item-harness-arch-2) ⭐️ 8.0/10

**AI 日报**
1. [C](#item-ai-daily-1) ⭐️ 5.8/10

---

## Harness 架构

<a id="item-harness-arch-1"></a>
### [A](https://example.com/a) ⭐️ 8.1/10

body a

---

<a id="item-harness-arch-2"></a>
### [B](https://example.com/b) ⭐️ 8.0/10

body b

---

## AI 日报

<a id="item-ai-daily-1"></a>
### [C](https://example.com/c) ⭐️ 5.8/10

body c

---"""


class AddSectionTocTest(unittest.TestCase):
    def test_toc_ids_counts(self):
        out = toc.render(SAMPLE)
        self.assertIn('id="ah-toc"', out)
        self.assertIn('href="#sec-harness-arch"', out)
        self.assertIn(">2条<", out)
        self.assertIn(">1条<", out)
        self.assertIn("{: #sec-harness-arch .ah-section}", out)
        self.assertIn("{: #sec-ai-daily .ah-section}", out)
        self.assertIn("**[AI 日报](#sec-ai-daily)**", out)
        self.assertEqual(out.count('href="#ah-toc"'), 2)
        # section heading lines stay intact
        self.assertIn("\n## Harness 架构\n", out)
        self.assertIn("\n## AI 日报\n", out)

    def test_idempotent(self):
        once = toc.render(SAMPLE)
        self.assertEqual(toc.render(once), once)

    def test_slug_fallback_chinese(self):
        self.assertEqual(toc.slugify("AI 日报"), "ai-日报")
        text = "---\nx: 1\n---\n\n## 今日 观察！\n\n正文\n"
        self.assertIn("{: #sec-今日-观察 .ah-section}", toc.render(text))

    def test_wechat_items_unchanged(self):
        try:
            import digest_items
        except ImportError:
            self.skipTest("wechat digest_items not importable")
        self.assertEqual(digest_items.split_items(SAMPLE), digest_items.split_items(toc.render(SAMPLE)))


if __name__ == "__main__":
    unittest.main()
