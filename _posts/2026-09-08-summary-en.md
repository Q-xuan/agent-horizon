---
layout: default
title: "Horizon Summary: 2026-09-08 (EN)"
date: 2026-09-08
lang: en
---

> From 139 items, 4 important content pieces were selected

---

**Agent Harness Architecture**
1. [MCP Python SDK v2.2.0 发布](#item-harness-arch-1) ⭐️ 7.8/10
2. [modelcontextprotocol/python-sdk v1.30.0 发布](#item-harness-arch-2) ⭐️ 5.8/10
3. [ADK-Go v1.6.1 Released](#item-harness-arch-3) ⭐️ 5.8/10

**AI Daily**
1. [Last Week in AI \#343 GPT-6 Astra 发布](#item-ai-daily-1) ⭐️ 5.0/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [MCP Python SDK v2.2.0 发布](https://github.com/modelcontextprotocol/python-sdk/releases/tag/v2.2.0) ⭐️ 7.8/10

MCP Python SDK v2.2.0 is released. HTTP client redirects are now only followed within the endpoint&\#x27;s origin. Idle Streamable HTTP sessions expire after 30 minutes by default. New parameters session\_idle\_timeout and max\_sessions added. OAuth providers require issuer URL.

github · maxisbey · Sep 7, 15:53

**「改了什么」** HTTP redirects are now only followed within the same origin as the endpoint, failing with MCPError for other redirects. Idle Streamable HTTP sessions expire after 30 minutes by default, and deprecation warnings added for OAuth clients without issuer.

**Tags**: `#mcp`, `#runtime`

---

<a id="item-harness-arch-2"></a>
### [modelcontextprotocol/python-sdk v1.30.0 发布](https://github.com/modelcontextprotocol/python-sdk/releases/tag/v1.30.0) ⭐️ 5.8/10

modelcontextprotocol/python-sdk v1.30.0 is a maintenance release for the Python MCP SDK 1.x line. It restricts HTTP client redirects to the endpoint&\#x27;s origin only and expires idle Streamable HTTP sessions after 30 minutes by default. OAuth authorization server issuer validation was added along with deprecation warnings.

github · maxisbey · Sep 7, 14:03

**「改了什么」** HTTP client redirects are now only followed within the endpoint&\#x27;s origin, failing requests otherwise with HTTPStatusError. Idle Streamable HTTP sessions expire after 30 minutes by default.

**Tags**: `#mcp`, `#runtime`, `#http-client`

---

<a id="item-harness-arch-3"></a>
### [ADK-Go v1.6.1 Released](https://github.com/google/adk-go/releases/tag/v1.6.1) ⭐️ 5.8/10

ADK-Go v1.6.1 is a patch release of the Google ADK-Go library. It delivers targeted fixes to runtime, tools, and trust mechanisms via backported PRs. No new architectural features or breaking changes; version bumped to 1.6.1 with no interface or limitation updates.

github · wolo-lab · Sep 7, 08:22

**「What Changed」** This release backports fixes for config loader panics on non-string args, base flow nil-deref, tool results and content, A2A peer metadata trust, tool-confirmation trust, artifact handling, session services, runner and REST server issues, and remote agent card source validation.

**Tags**: `#runtime`, `#tools`, `#permissions`

---

## AI Daily

<a id="item-ai-daily-1"></a>
### [Last Week in AI \#343 GPT-6 Astra 发布](https://lastweekin.ai/p/last-week-in-ai-343-gpt-6-openais) ⭐️ 5.0/10

本周 AI 新闻 \#343 报道了 GPT-6 Astra 的发布、OpenAI 代理在 wiki 上聊天，以及 Anthropic Claude Fable 5.1 的推出。Claude Fable 5.1 声称在代理工作中比之前便宜高达 45%。该新闻是每周总结，包含具体产品提及但缺乏官方来源。

rss · Last Week in AI · Sep 7, 13:02

**「可关注」** 可关注：Claude Fable 5.1 在代理工作中比之前便宜高达 45%。

**Tags**: `#gpt-6`, `#openai`, `#anthropic`, `#claude`, `#newsletter`

---