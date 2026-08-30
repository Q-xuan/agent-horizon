---
layout: default
title: "Horizon Summary: 2026-08-30 (ZH)"
date: 2026-08-30
lang: zh
---

> 从 147 条内容中筛选出 7 条重要资讯。

---

**Harness 架构**
1. [Codex rust-v0.151.0 发布](#item-harness-arch-1) ⭐️ 8.8/10
2. [pydantic-ai v2.36.0 发布](#item-harness-arch-2) ⭐️ 7.8/10
3. [Gemini CLI v0.59.0-nightly.20260829.g0bd1d4397 发布](#item-harness-arch-3) ⭐️ 5.8/10
4. [Claude Code 插件 trending](#item-harness-arch-4) ⭐️ 5.0/10

**AI 羊毛**
1. [StemDeck 免费开源本地 AI 茎分离器](#item-ai-deals-1) ⭐️ 6.0/10
2. [Simurg 免费 Web 搜索发布](#item-ai-deals-2) ⭐️ 5.0/10
3. [Lumify 体育智能 API 立即试用](#item-ai-deals-3) ⭐️ 5.0/10

---

## Harness 架构

<a id="item-harness-arch-1"></a>
### [Codex rust-v0.151.0 发布](https://github.com/openai/codex/releases/tag/rust-v0.151.0) ⭐️ 8.8/10

Codex Rust v0.151.0 发布。新增可配置的 MCP 工具发现 grace period，支持扩展检查或替换 MCP 工具结果。提升了远程沙箱强制执行，TUI 会话中保留权限配置文件，并将嵌套子代理的 token 使用计入根目标预算。

github · github-actions\[bot\] · 8月29日 09:55

**「改了什么」** 相比上一版，此次更新增加了可选 MCP 服务器工具发现的配置 grace period，并支持扩展对 MCP 工具结果的检查或替换。沙箱执行和权限配置文件保留也得到改进。

**标签**: `#runtime`, `#sandbox`, `#permissions`, `#tools`, `#mcp`, `#subagents`

---

<a id="item-harness-arch-2"></a>
### [pydantic-ai v2.36.0 发布](https://github.com/pydantic/pydantic-ai/releases/tag/v2.36.0) ⭐️ 7.8/10

pydantic-ai v2.36.0 发布。新增 durable\_operation 用于 durable execution，支持第三方 durable execution 引擎的公共后端 API。同时支持 MCP 配置和 tool-call streaming。InstructionPart.id 现在是稳定的。

github · dsfaccini · 8月29日 01:25

**「改了什么」** 新增 durable\_operation 支持、MCP 配置和 tool-call streaming。InstructionPart.id 变为稳定。

**标签**: `#runtime`, `#mcp`, `#tools`, `#memory`

---

<a id="item-harness-arch-3"></a>
### [Gemini CLI v0.59.0-nightly.20260829.g0bd1d4397 发布](https://github.com/google-gemini/gemini-cli/releases/tag/v0.59.0-nightly.20260829.g0bd1d4397) ⭐️ 5.8/10

Google Gemini CLI v0.59.0-nightly.20260829.g0bd1d4397 发布。核心更新强制 workspace trust fail-closed 模式，并过滤受限模式下的 mcpServers。

github · gemini-cli-robot · 8月29日 01:56

**「改了什么」** 从上一版 nightly，真正变的是强制 workspace trust fail-closed 模式，并过滤受限模式下的 mcpServers。

**标签**: `#permissions`, `#sandbox`, `#mcp`, `#runtime`, `#tools`

---

<a id="item-harness-arch-4"></a>
### [Claude Code 插件 trending](https://github.com/anthropics/claude-plugins-official) ⭐️ 5.0/10

Claude Code claude-plugins-official 官方插件目录 trending。该目录由 Anthropic 管理，包含高质量 Claude Code 插件和 MCP 服务器。使用前请确保信任插件，Anthropic 不控制插件内容。

rss · GitHub Trending Daily · 8月30日 01:23

**标签**: `#mcp`, `#tools`

---

## AI 羊毛

<a id="item-ai-deals-1"></a>
### [StemDeck 免费开源本地 AI 茎分离器](https://github.com/stemdeckapp/stemdeck) ⭐️ 6.0/10

StemDeck 是一款免费、开源且本地的 AI 茎分离器。用户可直接从 GitHub 下载该工具，并在本地环境中运行。

rss · HN Free API / Credits · 8月29日 01:24

**「可关注」** 可关注：该工具完全开源且支持本地运行，适用于隐私保护需求。

**标签**: `#free-tier`, `#limited-free`, `#promo`

---

<a id="item-ai-deals-2"></a>
### [Simurg 免费 Web 搜索发布](https://pypi.org/project/simurg/) ⭐️ 5.0/10

Simurg 是一个 Python 包，提供免费的 Web 搜索功能，用于 AI 代理防止幻觉。该工具帮助 AI 代理避免幻觉。用户可直接从 PyPI 安装使用。无特定额度、模型或价格限制。

rss · HN Free API / Credits · 8月29日 21:43

**「可关注」** 可关注：免费 Web 搜索，用于 AI 代理防止幻觉。

**标签**: `#free-tier`, `#api`, `#python`, `#ai-agent`

---

<a id="item-ai-deals-3"></a>
### [Lumify 体育智能 API 立即试用](https://lumify.ai/docs/ai) ⭐️ 5.0/10

Lumify 推出体育智能 API，专为 agents 设计。无需注册即可立即试用。材料中未提供使用额度、模型或价格信息。

rss · HN Free API / Credits · 8月29日 18:12

**「可关注」** 可关注：无需注册即可试用 Lumify 体育智能 API，适用于 agents 开发者。

**标签**: `#api`, `#free-tier`, `#promo`

---