---
layout: default
title: "Horizon Summary: 2026-09-05 (EN)"
date: 2026-09-05
lang: en
---

> From 158 items, 12 important content pieces were selected

---

**Agent Harness Architecture**
1. [Mastra @mastra/core@1.64.0 Released](#item-harness-arch-1) ⭐️ 8.8/10
2. [browser-use 0.13.10 发布](#item-harness-arch-2) ⭐️ 7.8/10
3. [Claude Code v2.1.261 发布](#item-harness-arch-3) ⭐️ 6.8/10
4. [pydantic-ai v2.40.0 released](#item-harness-arch-4) ⭐️ 6.8/10
5. [pydantic-ai v2.39.0 released](#item-harness-arch-5) ⭐️ 6.8/10
6. [gemini-cli v0.60.0-nightly.20260904.g87a9c71d5 released](#item-harness-arch-6) ⭐️ 6.8/10
7. [crewAI 1.15.19 发布](#item-harness-arch-7) ⭐️ 5.8/10
8. [anthropics/skills 仓库 trending](#item-harness-arch-8) ⭐️ 5.0/10

**AI Agent Engineer**
1. [Anthropic AI agents 形式化费马大定理](#item-agent-engineer-1) ⭐️ 9.0/10

**AI Daily**
1. [Project HydraFusion Multi-Model Orchestration](#item-ai-daily-1) ⭐️ 7.8/10

**AI Deals**
1. [Epic Games Free Eggs This Week \(Sep 4-10\): Alone With You and Searching for Evan](#item-ai-deals-1) ⭐️ 8.0/10

**AI Creator Radar**
1. [Simon Willison shares transcript of Astra pelicans generation](#item-ai-creator-1) ⭐️ 0.0/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [Mastra @mastra/core@1.64.0 Released](https://github.com/mastra-ai/mastra/releases/tag/%40mastra/core%401.64.0) ⭐️ 8.8/10

Mastra releases @mastra/core@1.64.0. Reusable sandbox templates let E2B and platform providers start sessions from pre-cloned, pre-built repo images with background rebuilds. A new workingDirectory option standardizes defaults across all sandbox providers. Client tools now support server-defined toModelOutput for transforming payloads into model content.

github · PaulieScanlon · Sep 4, 13:14

**「Design Points」** Reusable sandbox templates enable warm checkouts and background rebuilds for reduced cold starts. workingDirectory is now a standard option honored by every provider for consistent command execution defaults.

**「What Changed」** Added review workflow status to observability feedback with filtering and update API. Added support for server-defined toModelOutput on client tools. Added workingDirectory option to MastraSandboxOptions. Breaking change: sandbox config is now a callback function.

**Tags**: `#sandbox`, `#runtime`, `#tools`

---

<a id="item-harness-arch-2"></a>
### [browser-use 0.13.10 发布](https://github.com/browser-use/browser-use/releases/tag/0.13.10) ⭐️ 7.8/10

browser-use 0.13.10 upgrades the Browser Harness to 0.1.13 and migrates to the MCP Python SDK 2.1.1. All declared dependencies are pinned exactly. It adds pydantic-settings 2.15.0 as a runtime dependency, pins Pydantic to 2.13.5 and Hatchling to 1.32.0, and upgrades pypdf to 6.16.2. Unknown MCP tool calls are reported as application errors instead of successful results.

github · MagMueller · Sep 4, 03:28

**「改了什么」** browser-use 0.13.10 upgrades Browser Harness to 0.1.13 and migrates to MCP Python SDK 2.1.1. It pins multiple dependencies including adding pydantic-settings 2.15.0, Pydantic 2.13.5, and Hatchling 1.32.0, upgrades pypdf to 6.16.2, and changes unknown MCP tool calls to application errors.

**Tags**: `#mcp`, `#runtime`, `#tools`

---

<a id="item-harness-arch-3"></a>
### [Claude Code v2.1.261 发布](https://github.com/anthropics/claude-code/releases/tag/v2.1.261) ⭐️ 6.8/10

Claude Code v2.1.261 is a patch release from Anthropics. It introduces bashOutputMaxChars and taskOutputMaxChars settings to raise command and background-task output limits up to 128K characters. It adds --append-subagent-system-prompt-file support for large subagent prompts and /skill-doctor to show unused loaded skills and their context costs. It also includes various fixes for input handling, Bedrock setup, Remote Control, and other issues.

github · ashwin-ant · Sep 4, 19:58

**「改了什么」** This patch release adds bashOutputMaxChars and taskOutputMaxChars settings, --append-subagent-system-prompt-file CLI flag, /skill-doctor diagnostic command, and multiple bug fixes including input character ordering, Bedrock wizard hanging, Remote Control session handling, and more.

**Tags**: `#subagents`, `#tools`, `#settings`

---

<a id="item-harness-arch-4"></a>
### [pydantic-ai v2.40.0 released](https://github.com/pydantic/pydantic-ai/releases/tag/v2.40.0) ⭐️ 6.8/10

pydantic-ai v2.40.0 adds realtime audio session features including barge-in support, out-of-band enqueue, event listeners on Agent, and respond= to send\(\) for improved runtime interaction handling. It also includes minor provider and pricing updates. The release targets enhancements to RealtimeSession and Agent event handling without major protocol changes.

github · DouweM · Sep 5, 00:09

**「What changed」** Relative to v2.39.0, v2.40.0 adds barge-in handling to RealtimeSession sessions, out-of-band enqueue support, and event listener registration on Agent instances. It also introduces a respond parameter to send\(\) and a provider factory for inferring realtime models.

**Tags**: `#runtime`, `#realtime`, `#session`, `#events`

---

<a id="item-harness-arch-5"></a>
### [pydantic-ai v2.39.0 released](https://github.com/pydantic/pydantic-ai/releases/tag/v2.39.0) ⭐️ 6.8/10

pydantic-ai v2.39.0 released. Adds support for the OpenAI gpt-6-astra model. Includes fixes for exporter cache leaks, span-processor leaks, Instrumentation spec, Azure errors, speech emission, and tool media attribution.

github · dsfaccini · Sep 4, 04:18

**「What changed」** v2.39.0 adds support for the OpenAI gpt-6-astra model and restores the include\_model\_request\_parameters option in Instrumentation spec. It fixes cache leaks in the context\_subtree exporter, Azure content-filter errors, speech emission on stream\_transcripts, and tool media attribution.

**Tags**: `#runtime`, `#tools`, `#memory`

---

<a id="item-harness-arch-6"></a>
### [gemini-cli v0.60.0-nightly.20260904.g87a9c71d5 released](https://github.com/google-gemini/gemini-cli/releases/tag/v0.60.0-nightly.20260904.g87a9c71d5) ⭐️ 6.8/10

gemini-cli v0.60.0-nightly.20260904.g87a9c71d5 released. Enforces RFC 9207 issuer identification in MCP OAuth flow. Isolates temporary directory for macOS Seatbelt sandbox. Hardens path resolution and boundary validation in extension loader. Sanitizes and removes hardcoded Google CrUX API key in chrome-devtools-mcp.

github · gemini-cli-robot · Sep 4, 01:40

**「Design notes」** Runtime enforces RFC 9207 issuer identification in MCP OAuth. Tool layer hardens extension loader path resolution and boundary validation. Permissions isolate temporary directories in macOS Seatbelt sandbox. Security sanitizes hardcoded Google CrUX API key in chrome-devtools-mcp.

**「What changed」** Relative to v0.59.0-nightly.20260902.g4963a4456, this release enforces RFC 9207 issuer identification in MCP OAuth flow and isolates temporary directories for macOS Seatbelt sandbox. It hardens extension loader path resolution and boundary validation while sanitizing hardcoded Google CrUX API key in chrome-devtools-mcp.

**Tags**: `#mcp`, `#sandbox`, `#runtime`, `#tools`

---

<a id="item-harness-arch-7"></a>
### [crewAI 1.15.19 发布](https://github.com/crewAIInc/crewAI/releases/tag/1.15.19) ⭐️ 5.8/10

crewAI 1.15.19 发布。添加 Clipper 集成客户端、CEL 表达式 now\(\) 函数、平台工具可注入客户端、run recording 和机器大小报告。修复 urlreadtool 中 octet-stream 和 xlsx URL 的读取、Gemini 提供程序 trailing user turn、Ollama 基础 URL scheme 和 port、内存 scope configs、模型调用 hooks deny，并升级 pypdf 和 nltk 修复安全漏洞。

github · joaomdmoura · Sep 4, 11:28

**「改了什么」** crewAI 1.15.19 改了什么。添加 Clipper 集成客户端、CEL now\(\) 函数、平台工具可注入客户端、run recording 和机器大小报告。修复 urlreadtool、Gemini 提供程序 trailing user turn、Ollama 基础 URL、内存 scope configs、模型调用 hooks deny，并升级 pypdf 到 6.16.2 和 nltk 到 3.10.3。

**Tags**: `#tools`, `#memory`, `#permissions`

---

<a id="item-harness-arch-8"></a>
### [anthropics/skills 仓库 trending](https://github.com/anthropics/skills) ⭐️ 5.0/10

anthropics/skills is Anthropic&\#x27;s public repository implementing the Agent Skills standard for Claude agents. Skills consist of folders containing instructions, scripts, and resources that Claude loads dynamically to handle specialized tasks. This enables repeatable performance on tasks such as creating documents with company brand guidelines or analyzing data using organizational standards. The repository was announced via GitHub Trending Daily with no official release or changelog provided.

rss · GitHub Trending Daily · Sep 5, 00:33

**「设计要点」** Skills load dynamically at runtime into Claude agents, with built-in support for memory management and tool integration to enable specialized task execution.

**Tags**: `#runtime`, `#memory`, `#tools`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [Anthropic AI agents 形式化费马大定理](https://www.anthropic.com/research/formalizing-fermats-last-theorem) ⭐️ 9.0/10

Anthropic&\#x27;s AI agents formalized Fermat&\#x27;s Last Theorem in Lean, producing 13 million lines of code and proving 29,500 intermediate theorems in under two days. A team of agents completed the proof using a multi-agent system, consuming about six billion output tokens from a model comparable to Claude 3.5. This is the first demonstration of AI agents for large-scale mathematical formalization and proof search, directly relevant to coding-agent harness, orchestration, and evaluation benchmarks.

hackernews · jlebar · Sep 4, 18:42 · [Discussion](https://news.ycombinator.com/item?id=49568506)

**「为什么重要」** The formalization was completed in under two days, showing AI agents can now handle large-scale math proof search. Broader impacts on mathematical research and refereeing remain unconfirmed.

**「可关注」** 可关注：AI agents wrote 13 million lines of Lean code and proved 29,500 intermediate theorems in under two days.

**「评论」** Community members suggest reading Kevin Buzzard&\#x27;s blog post for context on what the achievement means and does not mean. Comments also highlight the scale of the proof generation and estimate token costs around $300k.

**Tags**: `#coding-agent`, `#eval`, `#orchestration`, `#formalization`, `#lean`

---

## AI Daily

<a id="item-ai-daily-1"></a>
### [Project HydraFusion Multi-Model Orchestration](https://github.blog/ai-and-ml/github-copilot/project-hydrafusion-frontier-quality-via-multi-model-orchestration/) ⭐️ 7.8/10

GitHub has announced Project HydraFusion, a multi-model orchestration method for improved coding workflows in GitHub Copilot. It is now available as a research preview. In controlled offline evaluations, HydraFusion’s selective coding workflows matched or exceeded the evaluated Opus 5 baseline while reducing estimated workflow cost.

rss · GitHub Blog · Sep 4, 16:04

**「Why it matters」** The approach delivers frontier quality at lower cost through selective multi-model orchestration, which is relevant for coding workflows.

**「Takeaway」** Takeaway: HydraFusion’s selective coding workflows matched or exceeded the Opus 5 baseline while reducing estimated workflow cost.

**Tags**: `#model`, `#lab`, `#product`, `#eval`

---

## AI Deals

<a id="item-ai-deals-1"></a>
### [Epic Games Free Eggs This Week \(Sep 4-10\): Alone With You and Searching for Evan](https://www.appinn.com/eggs-2694/) ⭐️ 8.0/10

Epic Games Store is offering Alone With You \(PC\) and Searching for Evan \(Android/iOS\) as free games until September 10, 2024 at 09:00. The giveaway is part of the weekly free game promotion. Claim through an Epic account.

rss · 小众软件 · Sep 4, 07:03

**「Why it matters」** These free games can be claimed before the deadline with no additional cost, giving users the chance to add them to their library immediately.

**「Takeaway」** Takeaway: Claim before September 10, 2024 at 09:00. Applies to PC for Alone With You and Android/iOS for Searching for Evan.

**Tags**: `#free-tier`, `#promo`, `#limited-free`

---

## AI Creator Radar

<a id="item-ai-creator-1"></a>
### [Simon Willison shares transcript of Astra pelicans generation](https://twitter.com/simonw/status/tweet-2095997113423519902) ⭐️ 0.0/10

Simon Willison posted a tweet stating &\#x27;Transcript from generating the Astra pelicans here...&\#x27; and linking to &\#x27;Here&\#x27;s the gpt-6-astra max one...&\#x27;. The links point to a transcript and a gpt-6-astra max generation. No additional text, technical details, or claims are provided in the tweet.

twitter · Simon Willison · Sep 4, 22:07

**Tags**: `#Simon Willison`, `#AI generation`, `#Astra pelicans`, `#transcript`, `#GPT-6 Astra`

---