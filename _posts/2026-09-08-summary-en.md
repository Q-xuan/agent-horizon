---
layout: default
title: "Horizon Summary: 2026-09-08 (EN)"
date: 2026-09-08
lang: en
---

> From 176 items, 10 important content pieces were selected

---

**Agent Harness Architecture**
1. [MCP Python SDK v2.2.0 Released](#item-harness-arch-1) ⭐️ 7.8/10
2. [modelcontextprotocol/python-sdk v1.30.0 released](#item-harness-arch-2) ⭐️ 6.8/10
3. [browser-use/browser-use GitHub Trending](#item-harness-arch-3) ⭐️ 5.0/10

**AI Agent Engineer**
1. [OpenAI Coding Agents Reshape Research Workflows](#item-agent-engineer-1) ⭐️ 7.0/10
2. [Iris 搜索代理发布](#item-agent-engineer-2) ⭐️ 7.0/10

**AI Daily**
1. [OpenAI AI Program for Ukrainian Journalism](#item-ai-daily-1) ⭐️ 6.8/10
2. [Last Week in AI \#343 GPT-6 发布](#item-ai-daily-2) ⭐️ 5.0/10

**AI Deals**
1. [Free WhatsApp Abandoned Cart Recovery for WooCommerce](#item-ai-deals-1) ⭐️ 5.0/10
2. [DepWarden: Free Anonymous Dependency Vulnerability Scanner](#item-ai-deals-2) ⭐️ 5.0/10
3. [PicFiddle 始终免费隐私图像编辑器](#item-ai-deals-3) ⭐️ 5.0/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [MCP Python SDK v2.2.0 Released](https://github.com/modelcontextprotocol/python-sdk/releases/tag/v2.2.0) ⭐️ 7.8/10

MCP Python SDK v2.2.0 is released. HTTP client redirects are now only followed within the endpoint&\#x27;s origin. Idle Streamable HTTP sessions expire after 30 minutes by default. New options include session\_idle\_timeout and max\_sessions. Deprecations warn about missing issuer and validate\_token\_resource settings.

github · maxisbey · Sep 7, 15:53

**「What Changed」** Breaking changes: HTTP redirects limited to endpoint origin; idle sessions expire after 30 minutes. New: AuthSettings.validate\_token\_resource, issuer= on OAuth providers, session\_idle\_timeout and max\_sessions. Fixes: DELETE frees session immediately; output schema $ref resolution within schema only.

**Tags**: `#mcp`, `#runtime`, `#protocol`, `#http-client`, `#breaking-changes`

---

<a id="item-harness-arch-2"></a>
### [modelcontextprotocol/python-sdk v1.30.0 released](https://github.com/modelcontextprotocol/python-sdk/releases/tag/v1.30.0) ⭐️ 6.8/10

The modelcontextprotocol/python-sdk v1.30.0 maintenance release updates the 1.x line. Default HTTP client redirects are now origin-restricted only. Idle Streamable HTTP sessions expire after 30 minutes. OAuth providers validate issuer metadata. FastMCP gains session idle timeout and max sessions parameters.

github · maxisbey · Sep 7, 14:03

**「Design points」** HTTP clients follow redirects only within the endpoint origin. Idle sessions are closed after 30 minutes of inactivity.

**「What changed」** Redirects are restricted to the endpoint origin. Idle sessions expire by default after 30 minutes. Issuer validation added to OAuth flows. Deprecation warnings introduced for missing issuer and unset resource validation.

**Tags**: `#mcp`, `#runtime`

---

<a id="item-harness-arch-3"></a>
### [browser-use/browser-use GitHub Trending](https://github.com/browser-use/browser-use) ⭐️ 5.0/10

GitHub is trending the browser-use repository, which enables AI agents to interact with websites by opening pages, clicking buttons, typing, and filling forms. Browser Use lets an AI agent use a web browser the same way humans do. You describe the task, and it completes it. Examples include filling forms with resume information and extracting structured data about followers.

rss · GitHub Trending Daily · Sep 7, 23:17

**Tags**: `#tools`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [OpenAI Coding Agents Reshape Research Workflows](https://simonwillison.net/2026/Sep/6/research-acceleration-the-view-inside-openai/) ⭐️ 7.0/10

OpenAI&\#x27;s research team uses coding agents to transform daily workflows, per an internal view shared by Simon Willison. A chart tracks median daily productivity gains measured in USD per researcher, starting near zero in February 2026, rising to about 150 by June, plateauing through July, and reaching roughly 600 by late August. The acceleration in late July is speculated to relate to access to the GPT-6 Astra model. This provides verifiable details on agent adoption at a leading AI lab, relevant for coding agent harnesses and evaluations.

rss · Simon Willison · Sep 6, 23:57

**「Why it matters」** The chart offers a rare verifiable metric of productivity gains from coding agents in a major research setting.

**「What to watch」** Median daily researcher productivity reached roughly 600 USD per researcher by late August 2026.

**Tags**: `#coding-agent`, `#harness`, `#eval`, `#orchestration`

---

<a id="item-agent-engineer-2"></a>
### [Iris 搜索代理发布](https://huggingface.co/papers/2609.04304) ⭐️ 7.0/10

Hugging Face introduces Iris-mini and Iris-pro search agents at 35B-A3B and 397B-A17B scales. They are trained via reverse-constructed multi-hop trajectories from web hyperlink entity graphs, filtered SFT, and RL against live search with reward judge and observation summarizer. This impacts agent training, tool-use harnesses, and evaluation systems.

rss · Hugging Face Daily Papers · Sep 7, 00:00

**「为什么重要」** The paper provides an explicit training recipe and multi-hop web corpus data pipeline for search agents. It delivers technical details with clear impact on agent training, tool-use harnesses, and evaluation systems.

**「可关注」** 可关注：Reverse-constructed multi-hop trajectories from web entity graphs enable RL-optimized search agents at 397B-A17B scale.

**Tags**: `#eval`, `#orchestration`, `#coding-agent`, `#memory`, `#harness`

---

## AI Daily

<a id="item-ai-daily-1"></a>
### [OpenAI AI Program for Ukrainian Journalism](https://openai.com/index/supporting-independent-journalism-in-ukraine) ⭐️ 6.8/10

OpenAI, AIRPPU and WAN-IFRA launch an AI program to help Ukrainian news organizations strengthen innovation, resilience, and independent journalism.

rss · OpenAI Blog · Sep 7, 00:00

**「Why It Matters」** The program supports independent journalism in Ukraine by helping news organizations build innovation and resilience.

**「Key Takeaway」** The AI program targets Ukrainian news organizations to strengthen their innovation, resilience, and independent journalism capabilities.

**Tags**: `#lab`, `#industry`, `#policy`

---

<a id="item-ai-daily-2"></a>
### [Last Week in AI \#343 GPT-6 发布](https://lastweekin.ai/p/last-week-in-ai-343-gpt-6-openais) ⭐️ 5.0/10

本期 Last Week in AI \#343 报道了 GPT-6 Astra 发布、OpenAI agents 在 wiki 上的聊天，以及 Anthropic Claude Fable 5.1 的新版本。Claude Fable 5.1 宣称 agentic work 成本可降低高达 45%。该总结基于次级来源，未提供原始实验室链接。

rss · Last Week in AI · Sep 7, 13:02

**「可关注」** 可关注：Claude Fable 5.1 宣称 agentic work 成本降低高达 45%

**Tags**: `#model`, `#lab`, `#product`

---

## AI Deals

<a id="item-ai-deals-1"></a>
### [Free WhatsApp Abandoned Cart Recovery for WooCommerce](https://wordpress.org/plugins/6rsh-messaging-notifications/) ⭐️ 5.0/10

sixrsh released the free WordPress plugin 6rsh-messaging-notifications. It enables WhatsApp notifications for abandoned cart recovery in WooCommerce stores. The plugin is available on WordPress.org with no quota or expiration details. It is suitable for WooCommerce stores.

rss · HN Free API / Credits · Sep 7, 19:00

**「Why It Matters」** This free plugin provides a tool for WooCommerce stores to recover abandoned carts through WhatsApp notifications without any cost or expiration.

**「Takeaway」** Takeaway: The plugin is free and suitable for WooCommerce stores seeking to recover abandoned carts via WhatsApp.

**「Community Discussion」** No community comments available.

**Tags**: `#free`, `#plugin`, `#woocommerce`, `#whatsapp`, `#abandoned-cart`

---

<a id="item-ai-deals-2"></a>
### [DepWarden: Free Anonymous Dependency Vulnerability Scanner](https://depwarden.in/blog/npm-pypi-typosquatting-2026-report) ⭐️ 5.0/10

DepWarden is a free, anonymous dependency vulnerability scanner for npm and PyPI packages. No account or source upload is required — paste a manifest or lockfile into a session-isolated workspace to receive OSV+KEV+EPSS-prioritized findings. The tool also ran a typosquatting study on the 30 most popular packages, finding that 32.7% of registered npm look-alikes are already confirmed malicious.

rss · HN Free API / Credits · Sep 7, 10:03

**「Why It Matters」** The tool needs no account or data upload, enabling developers to scan dependencies for vulnerabilities on npm and PyPI without barriers.

**「Takeaway」** Takeaway: Paste your npm or PyPI manifest/lockfile for OSV+KEV+EPSS-prioritized findings in a session-isolated workspace. Applies to any user checking for malicious look-alikes without signing up.

**Tags**: `#free-tier`, `#promo`, `#api`

---

<a id="item-ai-deals-3"></a>
### [PicFiddle 始终免费隐私图像编辑器](https://picfiddle.com/) ⭐️ 5.0/10

PicFiddle 是一款始终免费且注重隐私的图像编辑器。
无需限额、注册或使用限制，直接访问即可。
适用于所有用户，无截止时间。

rss · HN Free API / Credits · Sep 7, 01:09

**「可关注」** 可关注：始终免费且注重隐私的图像编辑器，适用于所有用户。

**Tags**: `#free-tier`, `#promo`, `#image-editor`

---