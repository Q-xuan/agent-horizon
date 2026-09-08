---
layout: default
title: "Horizon Summary: 2026-09-08 (EN)"
date: 2026-09-08
lang: en
---

> From 142 items, 5 important content pieces were selected

---

**Agent Harness Architecture**
1. [MCP Python SDK v2.2.0 released](#item-harness-arch-1) ⭐️ 7.8/10
2. [MCP Python SDK v1.30.0 发布](#item-harness-arch-2) ⭐️ 7.8/10
3. [google/adk-go v1.6.1 发布](#item-harness-arch-3) ⭐️ 5.8/10
4. [browser-use/browser-use GitHub Trending](#item-harness-arch-4) ⭐️ 5.0/10

**AI Daily**
1. [Last Week in AI \#343: GPT-6, OpenAI agents chatted on a wiki, Fable 5.1](#item-ai-daily-1) ⭐️ 5.0/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [MCP Python SDK v2.2.0 released](https://github.com/modelcontextprotocol/python-sdk/releases/tag/v2.2.0) ⭐️ 7.8/10

The modelcontextprotocol/python-sdk Python SDK has been released in version 2.2.0. It enforces stricter origin-based redirect policies for HTTP clients and servers while introducing idle session expiration for Streamable HTTP sessions. Redirects are now only followed within the endpoint&\#x27;s origin, idle sessions expire after 30 minutes by default, and the maximum sessions is capped at 10,000.

github · maxisbey · Sep 7, 15:53

**「What changed」** HTTP client redirects are now only followed within the endpoint&\#x27;s origin. Idle Streamable HTTP sessions now expire after 30 minutes by default.

**Tags**: `#mcp`, `#runtime`, `#tools`

---

<a id="item-harness-arch-2"></a>
### [MCP Python SDK v1.30.0 发布](https://github.com/modelcontextprotocol/python-sdk/releases/tag/v1.30.0) ⭐️ 7.8/10

The modelcontextprotocol/python-sdk v1.30.0 maintenance release updates client-side redirect policy and idle session handling for streamable\_http\_client and sse\_client. It enforces stricter HTTP redirect following within the same origin and expires idle sessions after 30 minutes. New parameters include session\_idle\_timeout and max\_sessions on FastMCP. OAuth providers now validate the authorization server&\#x27;s issuer.

github · maxisbey · Sep 7, 14:03

**「改了什么」** HTTP client redirects are only followed within the same origin. Idle Streamable HTTP sessions now expire after 30 minutes. Authorization server metadata issuer is validated on every discovery path. AuthSettings.validate\_token\_resource added to check a bearer token&\#x27;s resource.

**Tags**: `#mcp`, `#runtime`

---

<a id="item-harness-arch-3"></a>
### [google/adk-go v1.6.1 发布](https://github.com/google/adk-go/releases/tag/v1.6.1) ⭐️ 5.8/10

google/adk-go v1.6.1 patches Google&\#x27;s ADK-Go. It backports fixes for A2A peer metadata, tool confirmation, artifacts, and config loading. It also fixes config loader panic on non-string args, copyright path matching, and multiple backported issues.

github · wolo-lab · Sep 7, 08:22

**「改了什么」** v1.6.1 backports fixes for A2A peer metadata trust, tool confirmation, artifact handling, and session services. It corrects config loader panic on non-string arguments and copyright skip list matching.

**Tags**: `#a2a`, `#tools`, `#runtime`, `#fix`, `#backport`

---

<a id="item-harness-arch-4"></a>
### [browser-use/browser-use GitHub Trending](https://github.com/browser-use/browser-use) ⭐️ 5.0/10

GitHub is trending browser-use, a library that enables AI agents to control web browsers like humans do. It opens pages, clicks buttons, types, and fills forms. The library makes websites accessible for AI agents, allowing them to automate tasks online by describing the task and having it complete it.

rss · GitHub Trending Daily · Sep 8, 01:15

**Tags**: `#tools`, `#browser`, `#ai-agent`

---

## AI Daily

<a id="item-ai-daily-1"></a>
### [Last Week in AI \#343: GPT-6, OpenAI agents chatted on a wiki, Fable 5.1](https://lastweekin.ai/p/last-week-in-ai-343-gpt-6-openais) ⭐️ 5.0/10

Last Week in AI \#343 reports on the release of GPT-6 Astra, the discovery of an OpenAI agent message board, and Anthropic&\#x27;s launch of Claude Fable 5.1. The newsletter states that Fable 5.1 is up to 45% cheaper for agentic work. It also covers additional AI developments.

rss · Last Week in AI · Sep 7, 13:02

**「可关注」** 可关注：Claude Fable 5.1 is up to 45% cheaper for agentic work.

**Tags**: `#model`, `#lab`, `#industry`, `#product`

---