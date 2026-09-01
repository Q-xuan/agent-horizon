---
layout: default
title: "Horizon Summary: 2026-09-01 (EN)"
date: 2026-09-01
lang: en
---

> From 164 items, 11 important content pieces were selected

---

**Agent Harness Architecture**
1. [FastMCP v4.0.0 released](#item-harness-arch-1) ⭐️ 7.8/10
2. [agent-framework dotnet-1.20.0 released](#item-harness-arch-2) ⭐️ 7.8/10
3. [Cline desktop v0.0.21 released](#item-harness-arch-3) ⭐️ 6.8/10
4. [Claude Code v2.1.252 Released](#item-harness-arch-4) ⭐️ 5.8/10
5. [Cline desktop-v0.0.21-beta.2 发布](#item-harness-arch-5) ⭐️ 5.8/10
6. [OmniParser Trending on GitHub](#item-harness-arch-6) ⭐️ 5.0/10

**AI Agent Engineer**
1. [LoopArena: Benchmarking Models as Runtime Controllers for Loop Engineering](#item-agent-engineer-1) ⭐️ 7.0/10
2. [StarHarness：分层搜索演化企业环境 harness](#item-agent-engineer-2) ⭐️ 7.0/10

**AI Daily**
1. [ChatGPT Ads Hits $1B ARR and Expands Globally](#item-ai-daily-1) ⭐️ 8.8/10
2. [Polimill 构建日本公共 AI 基础设施](#item-ai-daily-2) ⭐️ 6.8/10
3. [Gemini 3.7 Flash &amp; Jalapeño Announced](#item-ai-daily-3) ⭐️ 5.0/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [FastMCP v4.0.0 released](https://github.com/PrefectHQ/fastmcp/releases/tag/v4.0.0) ⭐️ 7.8/10

FastMCP v4.0.0 is the stable release supporting the new MCP protocol with sessionless self-contained requests and per-connection version negotiation. It is built on the rewritten Python SDK v2 and the MCP protocol revision released on July 28. Most FastMCP 3 applications upgrade without code changes.

github · zzstoatzz · Aug 31, 18:19

**「Architecture note」** FastMCP 4.0.0 uses the new protocol engine for sessionless requests that can be handled by any load-balanced replica. It provides high-level surfaces including interactive tools, background tasks via the io.modelcontextprotocol/tasks extension, server extensions, argument completion, and auth features. Dependency injection binds to call arguments and ClientGroup manages one client per server with per-connection protocol negotiation.

**「What changed」** FastMCP 4.0.0 adds support for the new MCP protocol including sessionless requests and version negotiation. Breaking changes remove server-initiated sampling and roots, deprecated FastMCP 3 APIs, migrate to MCP SDK v2, and move background tasks to the separate fastmcp-tasks package.

**Tags**: `#mcp`, `#runtime`, `#tools`

---

<a id="item-harness-arch-2"></a>
### [agent-framework dotnet-1.20.0 released](https://github.com/microsoft/agent-framework/releases/tag/dotnet-1.20.0) ⭐️ 7.8/10

Microsoft released agent-framework dotnet-1.20.0. The update features API integrations, response handling fixes, and memory component updates. Key changes include Mem0Sharp integration for in-memory storage and Responses API usage for hosted web search.

github · SergeyMenshykh · Aug 31, 18:53

**「What Changed」** Stabilizes Foundry recovery tests and adds Mem0Sharp integration. Updates Responses API handling for web search and adds cancellation support for hosted workflows.

**Tags**: `#runtime`, `#tools`, `#memory`

---

<a id="item-harness-arch-3"></a>
### [Cline desktop v0.0.21 released](https://github.com/cline/cline/releases/tag/desktop-v0.0.21) ⭐️ 6.8/10

Cline desktop v0.0.21 is released. It adds a two-pane marketplace explorer, ensures session aborts propagate to child and delegated subagents as well as teammates, enables file drops in chat, refreshes live provider models, classifies auth errors, and fixes Langfuse tracing. The model catalog was refreshed with new providers like TokenGo and Volcengine Ark, and updates to model lists and pricing for ~36 providers.

github · github-actions\[bot\] · Aug 31, 21:41

**「Changes」** Relative to desktop-v0.0.20, this version adds a two-pane marketplace explorer, file drop support anywhere in the chat, live refresh of provider models, classification of auth errors, and propagation of session aborts to subagents and teammates. Langfuse tracing was fixed in release builds.

**Tags**: `#subagents`, `#tools`, `#runtime`

---

<a id="item-harness-arch-4"></a>
### [Claude Code v2.1.252 Released](https://github.com/anthropics/claude-code/releases/tag/v2.1.252) ⭐️ 5.8/10

Claude Code v2.1.252 is released with targeted bug fixes for runtime task handling, settings persistence, remote control stability, and output management.
The update resolves Bash command failures on macOS due to task output swap issues, ensures &\#x27;always allow&\#x27; settings save in new projects, fixes remote control session stalling after tool completion during claude.ai connection degradation, and prevents large failure outputs from exceeding API request size limits.

github · ashwin-ant · Aug 31, 19:46

**「What changed」** This release fixes Bash task output swap refused errors on some Macs, makes &\#x27;always allow&\#x27; settings persist in projects without .claude/settings.local.json, prevents remote control sessions hosted by Claude Desktop or VS Code from stalling for minutes after tool finish when claude.ai connection is degraded, and avoids API request size limit issues from very large failure outputs in background task notifications.

**Tags**: `#runtime`, `#tools`, `#memory`

---

<a id="item-harness-arch-5"></a>
### [Cline desktop-v0.0.21-beta.2 发布](https://github.com/cline/cline/releases/tag/desktop-v0.0.21-beta.2) ⭐️ 5.8/10

Cline desktop app v0.0.21-beta.2 released. Enhances session continuity to Cline Cloud with recovery for interrupted transfers and preservation of prompt, attachments, and session state. Adds multi-environment selection including SSH sandbox and realtime voice/avatar experiences. GitHub onboarding available behind feature flag.

github · github-actions\[bot\] · Aug 31, 21:08

**「改了什么」** Relative to v0.0.20, added session handoff to cloud, choice of local/SSH/Cloud environments, and realtime voice/avatar overlay.

**Tags**: `#memory`, `#sandbox`, `#runtime`, `#tools`

---

<a id="item-harness-arch-6"></a>
### [OmniParser Trending on GitHub](https://github.com/microsoft/OmniParser) ⭐️ 5.0/10

OmniParser is a simple screen parsing tool for pure vision-based GUI agents. It parses user interface screenshots into structured and easy-to-understand elements, significantly enhancing GPT-4V&\#x27;s ability to generate actions grounded in interface regions. The tool trends on GitHub with project page, V2 blog post, models V2, models V1.5, and HuggingFace Space demo.

rss · GitHub Trending Daily · Sep 1, 01:32

**Tags**: `#tools`, `#gui-agent`, `#vision`, `#parsing`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [LoopArena: Benchmarking Models as Runtime Controllers for Loop Engineering](https://huggingface.co/papers/2608.28281) ⭐️ 7.0/10

Hugging Face Daily Papers introduces LoopArena, a benchmark to test how well one model can guide a separate coding agent through long-running tasks in loop-based development. The model under evaluation is the Controller, which after each coding step decides what the agent should do next. This setup allows distinguishing whether success or failure reflects the loop&\#x27;s guidance or the coding agent&\#x27;s execution ability. It impacts eval and harness for agent loops with technical problem framing and benchmark definition.

rss · Hugging Face Daily Papers · Sep 1, 01:32

**「Why it matters」** The benchmark is directly relevant to evaluating agent loops, as it separates controller guidance quality from agent task performance.

**「Observable」** Observable: LoopArena enables isolated evaluation of the runtime controller&\#x27;s decision-making independent of the coding agent&\#x27;s capabilities.

**Tags**: `#eval`, `#harness`, `#coding-agent`, `#orchestration`

---

<a id="item-agent-engineer-2"></a>
### [StarHarness：分层搜索演化企业环境 harness](https://huggingface.co/papers/2608.24804) ⭐️ 7.0/10

StarHarness 框架在保持模型权重不变的情况下，演化环境特定 harness，包括提示、工具、技能、MCP 提供者、子代理和代理循环。框架通过按基线失败行为分层任务，构建紧凑演化池。在 ITBench SRE、EnterpriseOps-Gym ITSM 和 AutomationBench Finance 基准上，演化 harness 相比默认 harness 提升 20-35 个百分点，需 4-12 次接受变化。这些提升在排除的 held-out 任务上持久存在。

rss · Hugging Face Daily Papers · Sep 1, 01:32

**「为什么重要」** StarHarness 框架为 harness 演化提供可重复的方法，在企业 IT/ops/finance 环境中直接可应用。已报告的 20-35pp 提升在多个基准上可验证。

**「可关注」** 可关注：分层搜索和失败池可用于演化 harness，包括 MCP providers 和子代理结构。

**Tags**: `#harness`, `#eval`, `#orchestration`, `#coding-agent`, `#MCP`

---

## AI Daily

<a id="item-ai-daily-1"></a>
### [ChatGPT Ads Hits $1B ARR and Expands Globally](https://openai.com/index/expanding-access-to-ai-with-chatgpt-ads) ⭐️ 8.8/10

OpenAI reports that ChatGPT Ads has reached a $1 billion annualized revenue run rate. The service is expanding globally to support free and affordable AI access options.

rss · OpenAI Blog · Aug 31, 04:00

**「Why it matters」** This milestone reflects growing revenue from ChatGPT Ads and supports broader global access to AI.

**「Key takeaway」** Takeaway: ChatGPT Ads has reached a $1 billion annualized revenue run rate and is expanding globally.

**Tags**: `#openai`, `#ads`, `#revenue`, `#access`, `#product`

---

<a id="item-ai-daily-2"></a>
### [Polimill 构建日本公共 AI 基础设施](https://openai.com/index/polimill) ⭐️ 6.8/10

Polimill 部署 OpenAI GPT 模型和 Codex，帮助日本各 municipalities 搜索和管理行政知识，同时加速地方发展。Polimill 正在构建日本的下一代公共 AI 基础设施。

rss · OpenAI Blog · Aug 31, 07:00

**「为什么重要」** Polimill 的这一合作将 OpenAI 技术引入日本公共 AI 基础设施建设，有助于提升地方行政效率。

**「可关注」** 可关注：Polimill 集成 OpenAI GPT 模型和 Codex 构建日本公共 AI 基础设施。

**Tags**: `#openai`, `#gpt`, `#industry`, `#public-ai`, `#partnership`

---

<a id="item-ai-daily-3"></a>
### [Gemini 3.7 Flash &amp; Jalapeño Announced](https://lastweekin.ai/p/lwiai-podcast-255-gemini-37-jalapeno) ⭐️ 5.0/10

LWiAI Podcast \#255 covers Google&\#x27;s announcement of Gemini 3.7 Flash. Jalapeño&\#x27;s first results show industry-leading speed. The episode also discusses Qwen 3.8 and an AI-guided drone incident that killed three Ukrainians.

rss · Last Week in AI · Aug 31, 08:20

**「Key Takeaway」** Jalapeño&\#x27;s first results show industry-leading speed.

**Tags**: `#model`, `#gemini`, `#google`, `#qwen`, `#drone`, `#podcast`

---