---
layout: default
title: "Horizon Summary: 2026-08-30 (EN)"
date: 2026-08-30
lang: en
---

> From 147 items, 7 important content pieces were selected

---

**Agent Harness Architecture**
1. [Codex rust-v0.151.0 released](#item-harness-arch-1) ⭐️ 8.8/10
2. [Pydantic AI v2.36.0 Released](#item-harness-arch-2) ⭐️ 7.8/10
3. [gemini-cli v0.59.0-nightly.20260829.g0bd1d4397 发布](#item-harness-arch-3) ⭐️ 5.8/10
4. [Claude Code 插件目录 trending](#item-harness-arch-4) ⭐️ 5.0/10

**AI Deals**
1. [StemDeck: Free Open-Source Local AI Stem Separator](#item-ai-deals-1) ⭐️ 6.0/10
2. [Simurg Free Web Search for AI Agents](#item-ai-deals-2) ⭐️ 5.0/10
3. [Lumify 体育智能 API 立即试用](#item-ai-deals-3) ⭐️ 5.0/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [Codex rust-v0.151.0 released](https://github.com/openai/codex/releases/tag/rust-v0.151.0) ⭐️ 8.8/10

OpenAI Codex Rust v0.151.0 is released. It adds configurable grace periods for discovering tools from optional MCP servers. Extensions now support inspecting or replacing MCP tool results. Sandbox enforcement is improved using executor home directories, OS, and path conventions. Permission profiles are preserved across TUI turns, and nested subagent tokens are counted toward root goals.

github · github-actions\[bot\] · Aug 29, 09:55

**「What changed」** Relative to v0.150.0, this release adds configurable MCP tool discovery grace periods, enables extensions to inspect or replace tool results, improves remote sandbox enforcement, preserves permission profiles in TUI, and counts nested subagent token usage toward root budgets.

**Tags**: `#runtime`, `#sandbox`, `#permissions`, `#tools`, `#mcp`, `#subagents`

---

<a id="item-harness-arch-2"></a>
### [Pydantic AI v2.36.0 Released](https://github.com/pydantic/pydantic-ai/releases/tag/v2.36.0) ⭐️ 7.8/10

Pydantic AI v2.36.0 adds durable execution support with @durable\_operation and a public backend API for third-party engines. It introduces MCP configuration and tool-call streaming support. Breaking changes include requiring an explicit operation name for durable operations and providing stable InstructionPart.id.

github · dsfaccini · Aug 29, 01:25

**「What Changed」** Pydantic AI v2.36.0 adds @durable\_operation for third-party durable execution engines and public backend API. It introduces MCP configuration support, tool-call streaming, and stable InstructionPart.id.

**Tags**: `#runtime`, `#mcp`, `#tools`, `#memory`

---

<a id="item-harness-arch-3"></a>
### [gemini-cli v0.59.0-nightly.20260829.g0bd1d4397 发布](https://github.com/google-gemini/gemini-cli/releases/tag/v0.59.0-nightly.20260829.g0bd1d4397) ⭐️ 5.8/10

Google Gemini CLI v0.59.0-nightly.20260829.g0bd1d4397 is released. This minor core update enforces fail-closed workspace trust and filters MCP servers under restricted mode. The change is a bugfix in permissions and sandboxing. It does not involve major runtime rewrite, feature addition, or architecture-level changes.

github · gemini-cli-robot · Aug 29, 01:56

**「改了什么」** Relative to v0.59.0-nightly.20260828.g3c311beac, this release enforces fail-closed workspace trust and filters mcpServers in restricted mode.

**Tags**: `#permissions`, `#sandbox`, `#mcp`, `#runtime`, `#tools`

---

<a id="item-harness-arch-4"></a>
### [Claude Code 插件目录 trending](https://github.com/anthropics/claude-plugins-official) ⭐️ 5.0/10

The anthropics/claude-plugins-official repo is trending on GitHub. It is the official Anthropic-managed directory of high-quality Claude Code Plugins including MCP servers. This is a curated directory of high-quality plugins for Claude Code. Important: trust a plugin before installing, updating, or using it as Anthropic does not control included MCP servers, files, or software and cannot verify they will work as intended.

rss · GitHub Trending Daily · Aug 30, 01:23

**Tags**: `#mcp`, `#tools`

---

## AI Deals

<a id="item-ai-deals-1"></a>
### [StemDeck: Free Open-Source Local AI Stem Separator](https://github.com/stemdeckapp/stemdeck) ⭐️ 6.0/10

StemDeck is a free, open-source, and local AI stem separator tool. It is available on GitHub with no quota or pricing details provided. No claiming conditions or deadline are specified.

rss · HN Free API / Credits · Aug 29, 01:24

**「Takeaway」** Takeaway: Free, open-source, local AI stem separator tool available on GitHub.

**Tags**: `#free-tier`, `#limited-free`, `#promo`

---

<a id="item-ai-deals-2"></a>
### [Simurg Free Web Search for AI Agents](https://pypi.org/project/simurg/) ⭐️ 5.0/10

Simurg is a Python package providing free web search for AI agents to abort hallucinations. Released by lebagetdefrance. No quota, model, price, claiming conditions, or deadline mentioned.

rss · HN Free API / Credits · Aug 29, 21:43

**「Takeaway」** Takeaway: Integrate Simurg into Python AI agents for free web search to prevent hallucinations.

**Tags**: `#free-tier`, `#api`, `#python`, `#ai-agent`

---

<a id="item-ai-deals-3"></a>
### [Lumify 体育智能 API 立即试用](https://lumify.ai/docs/ai) ⭐️ 5.0/10

Lumify 提供体育智能 API，专为代理设计。根据 Show HN 帖子，用户无需注册即可立即尝试。API 链接至 lumify.ai/docs/ai。材料未提供配额、限额或定价信息。

rss · HN Free API / Credits · Aug 29, 18:12

**「可关注」** 无需注册即可立即尝试 Lumify 体育智能 API。

**Tags**: `#api`, `#free-tier`, `#promo`

---