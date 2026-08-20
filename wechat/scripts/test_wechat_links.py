#!/usr/bin/env python3
"""Regression tests: WeChat publishes HTML and strips plain <a href>.

Run: python3 wechat/scripts/test_wechat_links.py
"""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import digest_items as digest  # noqa: E402
import push_draft as push  # noqa: E402


class WechatAnchorTests(unittest.TestCase):
    def test_editor_shaped_https_link(self) -> None:
        html = push.wechat_anchor("原文标题", "https://example.com/a?q=1&x=2")
        self.assertIn('target="_blank"', html)
        self.assertIn('href="https://example.com/a?q=1&amp;x=2"', html)
        self.assertIn('textvalue="原文标题"', html)
        self.assertIn('data-linktype="2"', html)
        self.assertNotRegex(html, r"<a href=")

    def test_escapes_label_and_url(self) -> None:
        html = push.wechat_anchor('a<b>"c', 'https://example.com/"x"')
        self.assertIn("a&lt;b&gt;&quot;c", html)
        self.assertIn("&quot;x&quot;", html)
        self.assertNotIn("<b>", html)

    def test_http_and_javascript_are_not_hrefs(self) -> None:
        self.assertEqual(push.wechat_anchor("x", "http://evil.example"), "x")
        self.assertNotIn("href=", push.wechat_anchor("x", "javascript:alert(1)"))
        self.assertEqual(push.https_only("https://"), "")


class ContentSourceUrlTests(unittest.TestCase):
    def test_frontmatter_source_wins(self) -> None:
        body = "原文：[二](https://example.com/second)\nhttps://example.com/third"
        url = push.content_source_url({"source": "https://example.com/first"}, body)
        self.assertEqual(url, "https://example.com/first")

    def test_first_yuanywen_https_when_no_source(self) -> None:
        body = (
            "原料来自 [Agent Horizon](https://q-xuan.github.io/agent-horizon/)。\n\n"
            "原文：[Mastra 1.60](https://github.com/mastra-ai/mastra)\n"
            "原文：[其它](https://example.com/other)\n"
        )
        self.assertEqual(
            push.content_source_url({}, body),
            "https://github.com/mastra-ai/mastra",
        )

    def test_first_https_in_body_as_last_resort(self) -> None:
        body = "见 https://example.com/only 和 https://example.com/later"
        self.assertEqual(push.content_source_url({}, body), "https://example.com/only")

    def test_http_source_is_ignored(self) -> None:
        self.assertEqual(push.content_source_url({"source": "http://nope"}, ""), "")


class MdToHtmlTests(unittest.TestCase):
    def test_markdown_link_becomes_editor_tag(self) -> None:
        html = push.md_to_html("见 [OpenRouter](https://openrouter.ai/blog)。")
        self.assertIn('data-linktype="2"', html)
        self.assertIn('textvalue="OpenRouter"', html)
        self.assertIn('target="_blank"', html)
        self.assertIn('href="https://openrouter.ai/blog"', html)
        self.assertNotRegex(html, r"<a href=")


class DigestEmitTests(unittest.TestCase):
    def test_emits_yuanywen_and_source_not_empty_questions(self) -> None:
        items = [
            {
                "title": "Mastra 1.60",
                "url": "https://github.com/mastra-ai/mastra",
                "score": "8.0",
                "body": "durable agents。",
            },
            {
                "title": "无链接小节",
                "url": "",
                "score": "",
                "body": "没有出处。",
            },
        ]
        post = digest.render_materials(items, "2026-08-20", "digest.md")
        self.assertIn("source: https://github.com/mastra-ai/mastra", post)
        self.assertIn("原文：[Mastra 1.60](https://github.com/mastra-ai/mastra)", post)
        self.assertNotIn("原文：https://", post)
        self.assertNotIn("### 我的疑问", post)
        self.assertNotIn("### 我的判断", post)


class ProcessDocsTests(unittest.TestCase):
    def test_template_and_guides_spell_yuanywen(self) -> None:
        root = Path(__file__).resolve().parents[1]
        template = (root / "template.md").read_text(encoding="utf-8")
        style = (root / "STYLE.md").read_text(encoding="utf-8")
        readme = (root / "README.md").read_text(encoding="utf-8")
        self.assertIn("原文：[标题](https://", template)
        self.assertIn("从前怎样", template)
        self.assertNotIn("### 我的疑问", template)
        self.assertIn("data-linktype", style)
        self.assertIn("阅读原文", style)
        self.assertIn("从前怎样", style)
        self.assertIn("所以怎样", style)
        self.assertIn("这次改了什么", style)
        self.assertIn("普通 `<a href", readme)
        self.assertIn("write_from_digest.py", readme)
        daily = (root.parent / ".github" / "workflows" / "daily.yml").read_text(encoding="utf-8")
        self.assertIn("shanghai_digest_date.py", daily)
        self.assertNotIn("WECHAT_SECRET=", daily)


if __name__ == "__main__":
    unittest.main()
