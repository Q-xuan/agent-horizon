#!/usr/bin/env python3
"""Regression tests: WeChat publishes HTML and strips plain <a href>.

Run: python3 wechat/scripts/test_wechat_links.py
"""

from __future__ import annotations

import os
import subprocess
import sys
import tempfile
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
        self.assertIn("text-underline-offset:3px", html)
        self.assertIn("word-break:", html)
        self.assertNotIn("color:", html)

    def test_cjk_wrapped_lines_do_not_get_english_spaces(self) -> None:
        html = push.md_to_html("今天发了\n新版本。\n")
        self.assertIn("今天发了新版本。", html)
        self.assertNotIn("今天发了 新版本。", html)
        html_en = push.md_to_html("today Codex\nreleased a build\n")
        self.assertIn("today Codex released a build", html_en)
        self.assertEqual(push.join_wrapped_lines(["他说，", "不要慌。"]), "他说，不要慌。")
        self.assertEqual(push.join_wrapped_lines(["发布了", "Codex"]), "发布了 Codex")

    def test_lede_hairline_body_and_footnote(self) -> None:
        html = push.md_to_html(
            "开头两三句。\n\n后段继续。\n\n原文：[标题](https://example.com/a)\n"
        )
        self.assertIn("font-size:17px", html)
        self.assertIn("line-height:1.95", html)
        self.assertIn("letter-spacing:0.14em", html)
        self.assertIn("font-size:16px", html)
        self.assertIn("line-height:1.9", html)
        self.assertIn("letter-spacing:0.12em", html)
        self.assertIn("font-size:14px", html)
        self.assertIn("letter-spacing:0.04em", html)
        self.assertIn("scaleY(0.45)", html)
        self.assertIn("1px solid currentColor", html)
        self.assertGreaterEqual(html.count("scaleY(0.45)"), 1)

    def test_markdown_hr_uses_same_hairline(self) -> None:
        html = push.md_to_html("开头。\n\n---\n\n后段。\n")
        self.assertEqual(html.count("scaleY(0.45)"), 2)

    def test_h2_number_shrink_and_margins(self) -> None:
        html = push.md_to_html("导语。\n\n## 1. 第一条\n\n## 2. 第二条\n")
        self.assertIn("margin:28px 0 12px", html)
        self.assertIn("margin:44px 0 12px", html)
        self.assertIn("letter-spacing:0.08em", html)
        self.assertIn("font-size:13px", html)
        self.assertIn("letter-spacing:0.18em", html)
        self.assertIn("1.</span>", html)

    def test_blockquote_and_inline_code_have_no_fill(self) -> None:
        html = push.md_to_html("导语。\n\n> 引用一句\n\n见 `fork`。\n")
        self.assertIn("border-left:2px solid currentColor", html)
        self.assertIn("border:1px solid currentColor", html)
        self.assertIn("font-size:13px", html)
        self.assertNotIn("background", html.lower())
        self.assertNotIn("background-color", html.lower())

    def test_no_theme_colors_media_queries_or_css_vars(self) -> None:
        html = push.md_to_html(
            "开头。\n\n## 1. 标题\n\n见 `code` 和 [链](https://example.com/x)。\n\n"
            "原文：[t](https://example.com/x)\n"
        )
        self.assertNotRegex(html, r"#[0-9a-fA-F]{3,8}\b")
        self.assertNotIn("@media", html)
        self.assertNotIn("var(--", html)
        self.assertNotIn("Georgia", html)
        self.assertNotIn("Songti", html)
        self.assertNotIn("Optima", html)
        self.assertNotIn("Helvetica", html)
        self.assertIn("PingFang SC", html)
        self.assertIn("Hiragino Sans GB", html)
        self.assertIn("Microsoft YaHei", html)


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
        self.assertIn("doocs", style)
        self.assertIn("wenyan", style)
        self.assertIn("彩色 H2 胶囊", style)
        self.assertIn("Mac 代码窗", style)
        self.assertIn("普通 `<a href", readme)
        self.assertIn("write_from_digest.py", readme)
        self.assertIn("Nano-on-WeChat", readme)
        daily = (root.parent / ".github" / "workflows" / "daily.yml").read_text(encoding="utf-8")
        self.assertIn("shanghai_digest_date.py", daily)
        self.assertNotIn("WECHAT_SECRET=", daily)
        self.assertNotIn("draft/add", daily)


class HtmlOutTests(unittest.TestCase):
    def test_html_out_writes_without_cover_or_secrets(self) -> None:
        script = Path(__file__).resolve().parent / "push_draft.py"
        with tempfile.TemporaryDirectory() as tmp:
            src = Path(tmp) / "p.md"
            dest = Path(tmp) / "out.html"
            src.write_text(
                "---\ntitle: t\n---\n\n开头两三句。\n\n## 1. 标题\n\n正文。\n",
                encoding="utf-8",
            )
            env = dict(**os.environ)
            env.pop("WECHAT_APPID", None)
            env.pop("WECHAT_SECRET", None)
            subprocess.check_call(
                [sys.executable, str(script), str(src), "--html-out", str(dest)],
                env=env,
            )
            html = dest.read_text(encoding="utf-8")
            self.assertIn("font-size:17px", html)
            self.assertIn("scaleY(0.45)", html)
            self.assertTrue(dest.is_file())

    def test_cover_required_only_when_pushing(self) -> None:
        script = Path(__file__).resolve().parent / "push_draft.py"
        with tempfile.TemporaryDirectory() as tmp:
            src = Path(tmp) / "p.md"
            src.write_text("开头。\n", encoding="utf-8")
            proc = subprocess.run(
                [sys.executable, str(script), str(src)],
                capture_output=True,
                text=True,
            )
            self.assertNotEqual(proc.returncode, 0)
            self.assertIn("--cover is required when pushing a draft", proc.stderr + proc.stdout)


if __name__ == "__main__":
    unittest.main()
