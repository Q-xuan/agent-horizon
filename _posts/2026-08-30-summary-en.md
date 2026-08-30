---
layout: default
title: "Horizon Summary: 2026-08-30 (EN)"
date: 2026-08-30
lang: en
---

> From 146 items, 6 important content pieces were selected

---

**Agent Harness Architecture**
1. [Codex rust-v0.151.0 发布](#item-harness-arch-1) ⭐️ 7.8/10
2. [pydantic-ai v2.36.0 released](#item-harness-arch-2) ⭐️ 7.8/10
3. [GitHub Trending: EveryInc/compound-engineering-plugin](#item-harness-arch-3) ⭐️ 5.5/10

**AI Deals**
1. [StemDeck 免费开源本地 AI 茎分离工具](#item-ai-deals-1) ⭐️ 7.0/10
2. [Lumify 体育智能 API 发布](#item-ai-deals-2) ⭐️ 5.0/10
3. [Agentic SQL for Free: Qwen3.8 27B and DuckDB](#item-ai-deals-3) ⭐️ 5.0/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [Codex rust-v0.151.0 发布](https://github.com/openai/codex/releases/tag/rust-v0.151.0) ⭐️ 7.8/10

OpenAI Codex Rust v0.151.0 is released. It adds a configurable grace period for discovering tools from optional MCP servers. Extensions now support inspecting or replacing MCP tool results before they reach the model. Plugin catalogs combine per-repository configuration and report invalid project marketplaces without hiding valid plugins. Bug fixes preserve permission profiles across TUI turns, improve remote sandbox enforcement using executor home directories and OS, and count nested subagent token usage toward root goals.

github · github-actions\[bot\] · Aug 29, 09:55

**「设计要点」** Remote sandbox enforcement propagates the executor’s actual home directory, operating system, and path conventions into turn environments. Permission profiles are preserved across TUI turns and prevent weakening of sandbox restrictions.

**「改了什么」** Relative to v0.150.0 this release adds configurable grace period for optional MCP tool discovery and extensions to inspect or replace MCP tool results. It also fixes plugin catalog handling and resolves bugs in permission profile restoration, remote sandbox enforcement, and nested subagent token budgeting.

**Tags**: `#mcp`, `#sandbox`, `#permissions`, `#subagents`, `#tools`, `#runtime`

---

<a id="item-harness-arch-2"></a>
### [pydantic-ai v2.36.0 released](https://github.com/pydantic/pydantic-ai/releases/tag/v2.36.0) ⭐️ 7.8/10

Pydantic AI v2.36.0 adds @durable\_operation support for durable execution engines along with a public backend API. It provides stable InstructionPart.id and accepts async iterables in RealtimeSession.send\_audio\(\). Breaking changes include requiring explicit operation names on @durable\_operation and adding --mcp-config with tool-call streaming to clai.

github · dsfaccini · Aug 29, 01:25

**「Design notes」** The @durable\_operation enables third-party durable execution engines via a public backend API, allowing for capabilities such as retry logic and state persistence in long-running operations.

**「What changed」** v2.36.0 introduces @durable\_operation for durable execution engines and stable InstructionPart.id. It requires explicit operation names for @durable\_operation and adds async iterable support in RealtimeSession.send\_audio\(\).

**Tags**: `#mcp`, `#runtime`, `#tools`, `#planning`

---

<a id="item-harness-arch-3"></a>
### [GitHub Trending: EveryInc/compound-engineering-plugin](https://github.com/EveryInc/compound-engineering-plugin) ⭐️ 5.5/10

EveryInc&\#x27;s Compound Engineering plugin is trending on GitHub. It features 33 skills and a brainstorm-plan-build-review-capture loop for AI coding agents including Claude Code, Codex, and Cursor. It runs on 14 agent hosts.

rss · GitHub Trending Daily · Aug 30, 00:57

**「设计要点」** The plugin uses a persistent memory loop \(brainstorm-plan-build-review-capture\) to capture learnings after each change so the next iteration can read prior knowledge. It runs across 14 agent hosts.

**Tags**: `#tools`, `#planning`, `#memory`, `#runtime`

---

## AI Deals

<a id="item-ai-deals-1"></a>
### [StemDeck 免费开源本地 AI 茎分离工具](https://github.com/stemdeckapp/stemdeck) ⭐️ 7.0/10

StemDeck is a free, open-source and local AI stem separator. It is available immediately via GitHub download with no restrictions. The project has 205 HN points.

rss · HN Free API / Credits · Aug 29, 01:24

**「为什么重要」** This free local AI tool is worth claiming today because it provides immediate access without any costs or limitations.

**「可关注」** Takeaway: Free open-source local AI stem separator with no usage restrictions, suitable for users requiring privacy or offline capabilities.

**Tags**: `#free-tier`, `#limited-free`, `#promo`

---

<a id="item-ai-deals-2"></a>
### [Lumify 体育智能 API 发布](https://lumify.ai/docs/ai) ⭐️ 5.0/10

Lumify is a sports intelligence API for agents. The Show HN post announces it&\#x27;s available to try without signup. No quota amounts, limits, expiration, or restrictions are specified in the announcement. Documentation is available at https://lumify.ai/docs/ai.

rss · HN Free API / Credits · Aug 29, 18:12

**「Takeaway」** Takeaway: Lumify sports intelligence API is available for agents to try without any signup required.

**Tags**: `#api`, `#promo`, `#free-tier`

---

<a id="item-ai-deals-3"></a>
### [Agentic SQL for Free: Qwen3.8 27B and DuckDB](https://motherduck.com/blog/Agentic-SQL-for-Free-with-Qwen3.8-27B-and-DuckDB/) ⭐️ 5.0/10

MotherDuck blog post explains free Agentic SQL setup with Qwen3.8 27B and DuckDB. The guide covers integration of these tools for agentic SQL tasks. No specific quotas, pricing, regions, or expiration details are provided.

rss · HN Free API / Credits · Aug 29, 13:50

**Tags**: `#free-tier`, `#promo`, `#api`

---