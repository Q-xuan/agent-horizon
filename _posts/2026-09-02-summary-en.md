---
layout: default
title: "Horizon Summary: 2026-09-02 (EN)"
date: 2026-09-02
lang: en
---

> From 200 items, 16 important content pieces were selected

---

**Agent Harness Architecture**
1. [LangChain 1.4.0a3 发布](#item-harness-arch-1) ⭐️ 8.8/10
2. [Claude Code v2.1.257 Released](#item-harness-arch-2) ⭐️ 7.8/10
3. [Codex rust-v0.152.0 released](#item-harness-arch-3) ⭐️ 7.8/10
4. [gemini-cli v0.59.0-preview.0 released](#item-harness-arch-4) ⭐️ 7.8/10
5. [opencode v1.18.26 released](#item-harness-arch-5) ⭐️ 7.8/10
6. [Graphiti v0.30.0 released](#item-harness-arch-6) ⭐️ 7.8/10
7. [Gemini CLI v0.58.0 发布](#item-harness-arch-7) ⭐️ 6.8/10

**AI Agent Engineer**
1. [Gemini Agentic Video Understanding](#item-agent-engineer-1) ⭐️ 7.8/10
2. [Claude Fable 5.1 and Claude Mythos 5.1 released](#item-agent-engineer-2) ⭐️ 7.0/10
3. [BenchMIRT: Auditing LLM Benchmarks at Prompt Level](#item-agent-engineer-3) ⭐️ 6.8/10

**AI Daily**
1. [ChatGPT Connects to EHR and Healthcare Data](#item-ai-daily-1) ⭐️ 9.8/10
2. [Path to Astra: Critical Capabilities and Frontier Safeguards](#item-ai-daily-2) ⭐️ 7.8/10
3. [AI-native Companies Turn Workflows into Operating Capability](#item-ai-daily-3) ⭐️ 6.8/10

**AI Deals**
1. [Browser Free Preview for Background Noise Removal](#item-ai-deals-1) ⭐️ 5.0/10
2. [DaemonCore Academy 127 Free Cybersecurity Lessons](#item-ai-deals-2) ⭐️ 5.0/10
3. [Sketchometry.org 免费几何草图](#item-ai-deals-3) ⭐️ 5.0/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [LangChain 1.4.0a3 发布](https://github.com/langchain-ai/langchain/releases/tag/langchain%3D%3D1.4.0a3) ⭐️ 8.8/10

LangChain 1.4.0a3 is the third alpha release in the 1.4.0 series. It introduces the langchain.mcp namespace to adapt MCP servers into LangChain tools. MCPAdapter handles URLs, scripts, configs, clients, and ClientGroup. list\_tools supports caching modes \(use, refresh, bypass\). as\_langchain\_tool converts single tools. Metadata groups annotations and server info under mcp namespace. Requires mcp extra and fastmcp&gt;=4.0.0.

github · github-actions\[bot\] · Sep 1, 17:19

**「改了什么」** This release adds the langchain.mcp namespace for adapting MCP servers into LangChain tools. Key additions are MCPAdapter, list\_tools with caching, as\_langchain\_tool, and mcp metadata grouping.

**Tags**: `#mcp`, `#tools`, `#runtime`

---

<a id="item-harness-arch-2"></a>
### [Claude Code v2.1.257 Released](https://github.com/anthropics/claude-code/releases/tag/v2.1.257) ⭐️ 7.8/10

Anthropic released Claude Code v2.1.257. The update sets claude-fable-5-1 as the new default Fable model with 1M context and updated pricing. It adds subagent model forcing, sandbox escape prevention in auto mode, time format and timezone settings, and /doctor warnings for stale sandbox mask files.

github · ashwin-ant · Sep 1, 17:53

**「What&\#x27;s Changed」** Claude Code v2.1.257 changes the default Fable model to claude-fable-5-1. It adds timeFormat and timeZone settings, Containment Escape rules in auto mode, and CLAUDE\_CODE\_SUBAGENT\_MODEL\_FORCE for subagents.

**Tags**: `#subagents`, `#sandbox`, `#permissions`, `#runtime`, `#planning`

---

<a id="item-harness-arch-3"></a>
### [Codex rust-v0.152.0 released](https://github.com/openai/codex/releases/tag/rust-v0.152.0) ⭐️ 7.8/10

openai/codex rust-v0.152.0 is released. It updates MCP tools and app-server clients with output limits, package-style server name support, and long timeouts. New features include Vim search in drafts and rate-limit action banners. App-server clients now support thread and shellCommand timeouts over one hour.

github · github-actions\[bot\] · Sep 1, 01:58

**「设计要点」** MCP server names support package-style characters including :, @, /, and . for CLI commands and authentication. Per-tool output\_token\_limit ensures consistent truncation across session resumes. App-server clients support thread/shellCommand timeouts longer than one hour.

**「改了什么」** From rust-v0.151.0, support for package-style MCP server names and per-tool output limits is added. Configurable timeouts exceeding one hour for threads and shell commands are now available, along with Vim search motions in the composer.

**Tags**: `#mcp`, `#tools`, `#runtime`

---

<a id="item-harness-arch-4"></a>
### [gemini-cli v0.59.0-preview.0 released](https://github.com/google-gemini/gemini-cli/releases/tag/v0.59.0-preview.0) ⭐️ 7.8/10

gemini-cli v0.59.0-preview.0 is released. It includes fixes to prevent SSRF in MCP OAuth metadata discovery and authentication. It enforces fail-closed workspace trust with mcpServer filtering in restricted mode. This preview release focuses on security enhancements for MCP and workspace management.

github · gemini-cli-robot · Sep 1, 20:19

**「Design Note」** Prevents SSRF in MCP OAuth metadata discovery and authentication. Enforces fail-closed workspace trust with mcpServer filtering in restricted mode.

**「What Changed」** Fixes prevent SSRF in MCP OAuth metadata discovery/authentication and enforce fail-closed workspace trust with mcpServer filtering in restricted mode. Version bumped to 0.59.0-preview.0.

**「Community Discussion」** No community comments available.

**Tags**: `#mcp`, `#permissions`, `#runtime`, `#tools`

---

<a id="item-harness-arch-5"></a>
### [opencode v1.18.26 released](https://github.com/anomalyco/opencode/releases/tag/v1.18.26) ⭐️ 7.8/10

opencode v1.18.26 is released featuring bugfixes for Claude session thinking blocks, Bedrock reasoning, tool call timing, and apply\_patch permission metadata. Bedrock GPT-5.6 models now accept \`none\` reasoning effort and Bedrock reasoning and replay handling is more reliable. Tool call timing now stays accurate when tools update their metadata while still running, and \`apply\_patch\` no longer emits an empty move path in permission metadata. Additional improvements include Azure CLI sign-in asking for the resource name directly instead of querying Azure management APIs and session renames saving reliably from the title editor.

github · opencode-agent\[bot\] · Sep 1, 21:52

**「What Changed」** opencode v1.18.26 fixes Claude 5 sessions to tolerate stale thinking blocks instead of failing after prompt or tool changes. It makes Bedrock reasoning and replay handling more reliable, tool call timing accurate with metadata updates, and apply\_patch permission metadata without empty move path. Azure CLI sign-in now asks for the resource name directly, and session renames save reliably from the title editor and tab context menu.

**Tags**: `#runtime`, `#tools`, `#permissions`

---

<a id="item-harness-arch-6"></a>
### [Graphiti v0.30.0 released](https://github.com/getzep/graphiti/releases/tag/v0.30.0) ⭐️ 7.8/10

Graphiti v0.30.0 corrects Neo4j query execution to honor the configured database \(default neo4j\) and documents affected self-hosted multi-database deployments.

github · prasmussen15 · Sep 1, 18:20

**「What changed」** Graphiti v0.30.0 routes Neo4j queries to the configured database instead of the home database.

**Tags**: `#runtime`, `#tools`, `#memory`

---

<a id="item-harness-arch-7"></a>
### [Gemini CLI v0.58.0 发布](https://github.com/google-gemini/gemini-cli/releases/tag/v0.58.0) ⭐️ 6.8/10

Google Gemini CLI v0.58.0 is released. The update includes sandbox isolation for Docker and container runtimes on macOS using Seatbelt. A2A server now clears stale cancellation errors on new message turns. Core refactors improve ignore path handling and shell execution consistency.

github · gemini-cli-robot · Sep 1, 20:51

**「设计要点」** Sandbox isolation uses macOS Seatbelt to protect Docker and container runtime sockets and binaries. A2A server handles cancellation errors at the message turn level.

**「改了什么」** v0.58.0 adds macOS Seatbelt sandbox isolation for containers and fixes A2A server cancellation errors. It also refactors ignore path symlink evaluation and write policy safety checkers.

**Tags**: `#sandbox`, `#runtime`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [Gemini Agentic Video Understanding](https://deepmind.google/blog/introducing-agentic-video-in-gemini/) ⭐️ 7.8/10

Google DeepMind announces agentic video understanding integrated with Gemini.
The feature enables the model to understand video content in an agentic manner.
It is an official DeepMind blog announcement.
It affects AI agent engineers working on multimodal tasks.

rss · Google DeepMind · Sep 1, 17:08

**「Why it matters」** The announcement expands Gemini&\#x27;s multimodal agent capabilities.
Impacts coding agents, evaluation, and orchestration workflows.
Specific technical details and effects remain unconfirmed.

**Tags**: `#coding-agent`, `#eval`, `#orchestration`

---

<a id="item-agent-engineer-2"></a>
### [Claude Fable 5.1 and Claude Mythos 5.1 released](https://www.anthropic.com/claude-fable-and-mythos-5-1) ⭐️ 7.0/10

Anthropic released Claude Fable 5.1 and Claude Mythos 5.1. Stylistic upgrades, better instruction adherence, and halved cache costs are included. A system card PDF and benchmark insights accompany the release.

hackernews · denysvitali · Sep 1, 17:53 · [Discussion](https://news.ycombinator.com/item?id=49525378)

**「Why it matters」** Cache read pricing has dropped from $1/M to $0.25/M. Effects on agent harness costs remain unconfirmed.

**「Attention」** Fable 5.1 shows more natural prose and reliable style instruction response. Cache read costs are now half of Opus cache read costs.

**「Community discussion」** Anthropic staff praised Fable 5.1 for natural style and instruction following. Simon Willison shared Pelican traces indicating improvement in high-effort reasoning. Users noted price reduction and questioned benchmark gains.

**Tags**: `#eval`, `#coding-agent`, `#harness`, `#orchestration`, `#memory`

---

<a id="item-agent-engineer-3"></a>
### [BenchMIRT: Auditing LLM Benchmarks at Prompt Level](https://huggingface.co/blog/allenai/benchmirt) ⭐️ 6.8/10

BenchMIRT is a new method for auditing LLM benchmarks at the individual prompt level using multidimensional Item Response Theory. It was trained on results from 100 LLMs across 16 benchmarks and more than 34K questions. The analysis recovered two dominant dimensions: safety and general reasoning. BBQ aligned more strongly with general reasoning than safety. HarmBench mixes safety and reasoning signals across its question groups. BenchMIRT can identify the most informative questions and predict held-out performance 79% of the time.

rss · Hugging Face Blog · Sep 1, 21:39

**「Why it matters」** BenchMIRT reveals that many benchmarks combine multiple capabilities, such as BBQ measuring social bias plus reasoning demands, allowing clearer interpretation of scores.

**「What to watch」** BenchMIRT can predict whether a model would answer a held-out question correctly 79% of the time, outperforming a simpler baseline at 70%.

**Tags**: `#eval`, `#harness`, `#benchmarks`

---

## AI Daily

<a id="item-ai-daily-1"></a>
### [ChatGPT Connects to EHR and Healthcare Data](https://openai.com/index/chatgpt-connects-health-records-and-healthcare-sources) ⭐️ 9.8/10

OpenAI has enabled ChatGPT to connect to trusted healthcare data sources. Healthcare organizations can now integrate their Electronic Health Records \(EHR\) and additional industry data with ChatGPT. This allows clinicians to securely access patient context and medical research directly in the ChatGPT interface.

rss · OpenAI Blog · Sep 1, 12:00

**「Key Takeaway」** Clinicians can securely access patient context and medical research through ChatGPT connected to trusted healthcare data sources.

**Tags**: `#openai`, `#chatgpt`, `#healthcare`, `#ehr`, `#integration`, `#product`

---

<a id="item-ai-daily-2"></a>
### [Path to Astra: Critical Capabilities and Frontier Safeguards](https://openai.com/index/path-to-astra) ⭐️ 7.8/10

OpenAI details the path to releasing Astra, its first model meeting critical cybersecurity standards plus enhanced safeguards. Astra is the first OpenAI model to meet the Critical cybersecurity capability threshold under the Preparedness Framework. The release includes stronger safeguards.

rss · OpenAI Blog · Sep 1, 13:00

**「Why It Matters」** Meeting the Critical cybersecurity capability threshold under the Preparedness Framework with enhanced safeguards marks a key advancement in AI model safety.

**「Key Takeaway」** Key Takeaway: Astra is the first OpenAI model to meet the Critical cybersecurity capability threshold under the Preparedness Framework with stronger safeguards for release.

**Tags**: `#model`, `#openai`, `#policy`, `#product`, `#eval`

---

<a id="item-ai-daily-3"></a>
### [AI-native Companies Turn Workflows into Operating Capability](https://openai.com/index/ai-native-company-workflows) ⭐️ 6.8/10

OpenAI blog outlines how AI-native firms turn workflows into operating capability via AI agents for onboarding, account management, and integrations, with enterprise applications. Basis, Clay, and Exa Labs use AI agents to improve onboarding, account management, and developer integrations. The post provides actionable insights for enterprise leaders.

rss · OpenAI Blog · Sep 1, 17:00

**「Why it matters」** Enterprise leaders can apply these AI agent strategies to improve their onboarding, account management, and developer integrations.

**「Key takeaway」** AI agents can automate onboarding, account management, and developer integrations in AI-native companies.

**Tags**: `#openai`, `#ai-agents`, `#ai-native`, `#workflows`, `#enterprise`

---

## AI Deals

<a id="item-ai-deals-1"></a>
### [Browser Free Preview for Background Noise Removal](https://removebackgroundnoise.app/) ⭐️ 5.0/10

jieliu\_rbn released a browser-based free preview application for removing background noise from audio and video files. The tool is immediately usable with no restrictions or expiration listed in the item. It is a free preview with no quota or credit offer details provided.

rss · HN Free API / Credits · Sep 2, 00:02

**「Why It Matters」** This free tool allows direct removal of background noise from audio and video in the browser without any cost or signup.

**「Engineer Takeaway」** 可关注：The tool is browser-based and immediately usable with no installation required.

**Tags**: `#free-tier`, `#limited-free`, `#promo`, `#tool`, `#audio`

---

<a id="item-ai-deals-2"></a>
### [DaemonCore Academy 127 Free Cybersecurity Lessons](https://academy.daemoncore.app/) ⭐️ 5.0/10

DaemonCore Academy offers 127 free cybersecurity lessons. Disposable Docker ranges are also available. These resources are for cybersecurity practice.

rss · HN Free API / Credits · Sep 1, 20:30

**Tags**: `#promo`, `#free-tier`, `#limited-free`

---

<a id="item-ai-deals-3"></a>
### [Sketchometry.org 免费几何草图](https://start.sketchometry.org/) ⭐️ 5.0/10

Sketchometry.org 是一款免费的网页几何草图工具。用户可通过手指在浏览器中直接绘制几何图形。无需任何注册或限制。

rss · HN Free API / Credits · Sep 1, 14:23

**「为什么重要」** 该工具立即可用，无需注册或限制，适合日常几何练习。

**「可关注」** 可关注：手指草图绘制无需额外软件或注册。

**Tags**: `#free-tier`, `#promo`, `#free-tool`

---