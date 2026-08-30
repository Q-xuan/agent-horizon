---
layout: default
title: "Horizon Summary: 2026-08-30 (ZH)"
date: 2026-08-30
lang: zh
---

> 从 146 条内容中筛选出 6 条重要资讯。

---

**Harness 架构**
1. [Codex rust-v0.151.0 发布](#item-harness-arch-1) ⭐️ 7.8/10
2. [Pydantic AI v2.36.0 发布](#item-harness-arch-2) ⭐️ 7.8/10
3. [EveryInc Compound Engineering 插件 trending](#item-harness-arch-3) ⭐️ 5.5/10

**AI 羊毛**
1. [StemDeck 免费开源本地 AI 分离器](#item-ai-deals-1) ⭐️ 7.0/10
2. [Lumify 体育智能 API for agents 发布](#item-ai-deals-2) ⭐️ 5.0/10
3. [Qwen3.8 27B DuckDB 免费 Agentic SQL](#item-ai-deals-3) ⭐️ 5.0/10

---

## Harness 架构

<a id="item-harness-arch-1"></a>
### [Codex rust-v0.151.0 发布](https://github.com/openai/codex/releases/tag/rust-v0.151.0) ⭐️ 7.8/10

OpenAI codex Rust v0.151.0 发布。新增可选 MCP 服务器工具发现的可配置 grace period。扩展支持检查或替换 MCP tool results。修复了 TUI turns 权限配置文件恢复、远程 sandbox 执行器 home 目录和路径语义、嵌套子代理 token 使用计入 root goal budget 等问题。

github · github-actions\[bot\] · 8月29日 09:55

**「改了什么」** 相比 rust-v0.150.0，新增了 MCP 工具发现 grace period 配置和 tool result inspect/replace 扩展。修复了 sandbox 远程执行器路径语义对齐、TUI 权限配置文件持久化、子代理 token 预算等问题。

**标签**: `#mcp`, `#sandbox`, `#permissions`, `#subagents`, `#tools`, `#runtime`

---

<a id="item-harness-arch-2"></a>
### [Pydantic AI v2.36.0 发布](https://github.com/pydantic/pydantic-ai/releases/tag/v2.36.0) ⭐️ 7.8/10

Pydantic AI v2.36.0 发布了。该版本新增了 @durable\_operation 支持，支持与持久化执行引擎集成并提供公共后端 API。指令部分获得稳定的 InstructionPart.id 接口。还添加了 MCP 配置支持和工具调用流式传输功能。

github · dsfaccini · 8月29日 01:25

**「改了什么」** v2.36.0 相比 v2.35.3，新增了 @durable\_operation 功能和稳定的 InstructionPart.id 接口。还要求 @durable\_operation 显式指定 operation name，并添加了 --mcp-config 支持。

**标签**: `#mcp`, `#runtime`, `#tools`, `#planning`

---

<a id="item-harness-arch-3"></a>
### [EveryInc Compound Engineering 插件 trending](https://github.com/EveryInc/compound-engineering-plugin) ⭐️ 5.5/10

EveryInc Compound Engineering 插件 trending。该插件为 Claude Code、Codex、Cursor 等 AI coding agents 提供 33 个技能。工作围绕 brainstorm-plan-build-review-capture 循环展开。每次变更的知识被捕获以供下次使用。插件运行在 14 个 agent hosts 上。

rss · GitHub Trending Daily · 8月30日 00:57

**「设计要点」** 该插件通过 brainstorm-plan-build-review-capture 循环实现知识捕获和记忆复用。运行在 14 个 agent hosts 上。

**标签**: `#tools`, `#planning`, `#memory`, `#runtime`

---

## AI 羊毛

<a id="item-ai-deals-1"></a>
### [StemDeck 免费开源本地 AI 分离器](https://github.com/stemdeckapp/stemdeck) ⭐️ 7.0/10

StemDeck 是一个免费开源的本地 AI 音频分离器。用户无需支付任何费用即可从 GitHub 下载使用。工具支持完全本地运行，无需依赖外部服务。

rss · HN Free API / Credits · 8月29日 01:24

**「为什么重要」** 工具免费开源且在 Hacker News 上获得 205 热度，值得下载尝试。

**「可关注」** 可关注：StemDeck 适用于本地运行的音频分离，用户可直接从 GitHub 下载使用，无需任何限制。

**标签**: `#free-tier`, `#limited-free`, `#promo`

---

<a id="item-ai-deals-2"></a>
### [Lumify 体育智能 API for agents 发布](https://lumify.ai/docs/ai) ⭐️ 5.0/10

Lumify 提供体育智能 API，专为 agents 设计。用户无需注册即可尝试该 API。材料中未提及具体额度、模型、价格或使用限制。

rss · HN Free API / Credits · 8月29日 18:12

**「为什么重要」** 无需注册即可试用，适合开发体育智能 agents 的工程师。

**「可关注」** 可关注：无需注册即可试用 Lumify 体育智能 API，适用于开发 agents 的工程师。

**标签**: `#api`, `#promo`, `#free-tier`

---

<a id="item-ai-deals-3"></a>
### [Qwen3.8 27B DuckDB 免费 Agentic SQL](https://motherduck.com/blog/Agentic-SQL-for-Free-with-Qwen3.8-27B-and-DuckDB/) ⭐️ 5.0/10

MotherDuck 博客发布 Qwen3.8 27B 和 DuckDB 的 Agentic SQL 教程。
该教程提供 Agentic SQL 的实现方法。

rss · HN Free API / Credits · 8月29日 13:50

**标签**: `#free-tier`, `#promo`, `#api`

---