---
layout: default
title: "Horizon Summary: 2026-09-08 (ZH)"
date: 2026-09-08
lang: zh
---

> 从 139 条内容中筛选出 4 条重要资讯。

---

**Harness 架构**
1. [MCP Python SDK v2.2.0 发布](#item-harness-arch-1) ⭐️ 7.8/10
2. [MCP Python SDK v1.30.0 发布](#item-harness-arch-2) ⭐️ 5.8/10
3. [ADK-Go v1.6.1 发布](#item-harness-arch-3) ⭐️ 5.8/10

**AI 日报**
1. [GPT-6 Astra 发布 OpenAI agents 聊天室](#item-ai-daily-1) ⭐️ 5.0/10

---

## Harness 架构

<a id="item-harness-arch-1"></a>
### [MCP Python SDK v2.2.0 发布](https://github.com/modelcontextprotocol/python-sdk/releases/tag/v2.2.0) ⭐️ 7.8/10

MCP Python SDK v2.2.0 发布。HTTP 客户端重定向仅跟随端点同源。空闲 Streamable HTTP 会话默认 30 分钟后过期。新增 issuer 参数和会话管理选项。

github · maxisbey · 9月7日 15:53

**「改了什么」** HTTP 客户端重定向仅跟随端点同源。Streamable HTTP 会话默认 30 分钟后过期。OAuth 提供者检查 issuer。

**标签**: `#mcp`, `#runtime`

---

<a id="item-harness-arch-2"></a>
### [MCP Python SDK v1.30.0 发布](https://github.com/modelcontextprotocol/python-sdk/releases/tag/v1.30.0) ⭐️ 5.8/10

MCP Python SDK v1.30.0 发布。更新 HTTP 客户端重定向策略，仅在端点源内跟随重定向。空闲 Streamable HTTP 会话默认在 30 分钟后过期。

github · maxisbey · 9月7日 14:03

**「改了什么」** HTTP 客户端重定向仅限于端点 origin 内。空闲 Streamable HTTP 会话默认过期。

**标签**: `#mcp`, `#runtime`, `#http-client`

---

<a id="item-harness-arch-3"></a>
### [ADK-Go v1.6.1 发布](https://github.com/google/adk-go/releases/tag/v1.6.1) ⭐️ 5.8/10

ADK-Go v1.6.1 发布。Google 官方发布了补丁版本。修复了运行时、工具和信任机制的多个问题。包括配置加载器对非字符串参数的 panic 修复、base flow nil-deref 修复、tool results/content 修复、A2A peer metadata trust 修复等。所有变更均为 backport PRs，无新功能。

github · wolo-lab · 9月7日 08:22

**「改了什么」** v1.6.1 相比 v1.6.0，修复了运行时、工具和信任机制的多个问题。具体包括 config loader 对非字符串参数的 panic 修复、base flow nil-deref 修复、tool results/content 修复、A2A peer metadata trust 修复等。

**标签**: `#runtime`, `#tools`, `#permissions`

---

## AI 日报

<a id="item-ai-daily-1"></a>
### [GPT-6 Astra 发布 OpenAI agents 聊天室](https://lastweekin.ai/p/last-week-in-ai-343-gpt-6-openais) ⭐️ 5.0/10

GPT-6 Astra 发布，OpenAI 开发了新的 agents 聊天室，Anthropic 推出 Claude Fable 5.1 并表示其在 agentic 工作中价格低至 45% 更便宜。

rss · Last Week in AI · 9月7日 13:02

**「可关注」** Claude Fable 5.1 在 agentic 工作中价格低至 45% 更便宜。

**标签**: `#gpt-6`, `#openai`, `#anthropic`, `#claude`, `#newsletter`

---