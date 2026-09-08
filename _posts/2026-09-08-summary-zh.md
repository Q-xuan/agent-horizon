---
layout: default
title: "Horizon Summary: 2026-09-08 (ZH)"
date: 2026-09-08
lang: zh
---

> 从 142 条内容中筛选出 5 条重要资讯。

---

**Harness 架构**
1. [MCP Python SDK v2.2.0 发布](#item-harness-arch-1) ⭐️ 7.8/10
2. [MCP Python SDK v1.30.0 发布](#item-harness-arch-2) ⭐️ 7.8/10
3. [google/adk-go v1.6.1 发布](#item-harness-arch-3) ⭐️ 5.8/10
4. [browser-use 库 trending](#item-harness-arch-4) ⭐️ 5.0/10

**AI 日报**
1. [Last Week in AI \#343 GPT-6 发布](#item-ai-daily-1) ⭐️ 5.0/10

---

## Harness 架构

<a id="item-harness-arch-1"></a>
### [MCP Python SDK v2.2.0 发布](https://github.com/modelcontextprotocol/python-sdk/releases/tag/v2.2.0) ⭐️ 7.8/10

MCP Python SDK v2.2.0 发布。HTTP 客户端重定向仅限于端点 origin 内。闲置 Streamable HTTP 会话在 30 分钟后过期，服务器并发会话上限为 10000。新增 session\_idle\_timeout 和 max\_sessions 参数以控制会话行为。

github · maxisbey · 9月7日 15:53

**「改了什么」** 相比 v2.1.1，HTTP 重定向收紧至 origin 内，闲置 Streamable HTTP 会话默认过期。新增 session\_idle\_timeout 和 max\_sessions 参数。

**标签**: `#mcp`, `#runtime`, `#tools`

---

<a id="item-harness-arch-2"></a>
### [MCP Python SDK v1.30.0 发布](https://github.com/modelcontextprotocol/python-sdk/releases/tag/v1.30.0) ⭐️ 7.8/10

MCP Python SDK 1.x 维护版本 v1.30.0 发布。更新了客户端重定向策略和空闲会话处理。streamable\_http\_client 和 sse\_client 仅在端点 origin 内跟随重定向，空闲 Streamable HTTP 会话在 30 分钟后过期。新增了 OAuth issuer 校验和相关配置。

github · maxisbey · 9月7日 14:03

**「改了什么」** HTTP 客户端重定向仅限端点 origin 内，空闲 Streamable HTTP 会话在 30 分钟后过期。OAuth 客户端检查授权服务器 metadata issuer，并新增了相关配置和弃用警告。

**标签**: `#mcp`, `#runtime`

---

<a id="item-harness-arch-3"></a>
### [google/adk-go v1.6.1 发布](https://github.com/google/adk-go/releases/tag/v1.6.1) ⭐️ 5.8/10

google/adk-go v1.6.1 发布了补丁版本。
此版本修复了 A2A 对等元数据、工具确认、工件处理和配置加载器的问题。
这是基于 v1.6.0 的回溯更新，无重大架构变更。

github · wolo-lab · 9月7日 08:22

**「改了什么」** 此版本修复了配置加载器在非字符串参数上的 panic 问题，并回溯修复了 A2A 对等元数据、工具结果、工件 delta 和会话服务等多个问题。
版本常量更新为 1.6.1。

**标签**: `#a2a`, `#tools`, `#runtime`, `#fix`, `#backport`

---

<a id="item-harness-arch-4"></a>
### [browser-use 库 trending](https://github.com/browser-use/browser-use) ⭐️ 5.0/10

browser-use 库让 AI 代理控制网页浏览器。代理打开页面、点击按钮、输入文字、填写表单。描述任务后，代理自动完成任务。

rss · GitHub Trending Daily · 9月8日 01:15

**标签**: `#tools`, `#browser`, `#ai-agent`

---

## AI 日报

<a id="item-ai-daily-1"></a>
### [Last Week in AI \#343 GPT-6 发布](https://lastweekin.ai/p/last-week-in-ai-343-gpt-6-openais) ⭐️ 5.0/10

OpenAI 发布了 GPT-6 Astra。OpenAI 的代理在 wiki 上聊天。Anthropic 推出 Claude Fable 5.1，声称代理工作成本降低高达 45%。

rss · Last Week in AI · 9月7日 13:02

**「可关注」** 可关注：Claude Fable 5.1 代理工作成本降低高达 45%

**标签**: `#model`, `#lab`, `#industry`, `#product`

---