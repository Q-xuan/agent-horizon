---
layout: default
title: "Horizon Summary: 2026-08-25 (EN)"
date: 2026-08-25
lang: en
---

> From 143 items, 11 important content pieces were selected

---

**Agent Harness Architecture**
1. [MCP Python SDK v2.1.0 Released](#item-harness-arch-1) ⭐️ 7.5/10
2. [mem0 CLI v0.2.12 发布](#item-harness-arch-2) ⭐️ 7.5/10
3. [Cline SDK v0.0.79 发布](#item-harness-arch-3) ⭐️ 6.5/10
4. [mastra/core@1.61.0 released](#item-harness-arch-4) ⭐️ 6.5/10
5. [mem0-strands v0.1.0 released](#item-harness-arch-5) ⭐️ 6.5/10
6. [mem0 deepseek-plugin-v0.1.0 发布](#item-harness-arch-6) ⭐️ 6.5/10
7. [Cline CLI v3.0.58 发布](#item-harness-arch-7) ⭐️ 5.5/10

**AI Agent Engineer**
1. [llm-anthropic 0.27 released](#item-agent-engineer-1) ⭐️ 7.5/10

**AI Daily**
1. [ADK adds native live voice evaluation](#item-ai-daily-1) ⭐️ 8.5/10
2. [GPT-5.6 in Kiro: Better Price-Performance for Developers](#item-ai-daily-2) ⭐️ 6.5/10
3. [Anthropic Field Marketer Uses Claude Code for Weekly Sales Updates](#item-ai-daily-3) ⭐️ 5.5/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [MCP Python SDK v2.1.0 Released](https://github.com/modelcontextprotocol/python-sdk/releases/tag/v2.1.0) ⭐️ 7.5/10

MCP Python SDK v2.1.0 has been released. The Client now accepts StdioServerParameters directly for spawning servers. Prompt messages support Image and Audio media types, and prompt functions may return bare content blocks. The 4 MiB request body limit now covers SSE and OAuth transports. Handler exceptions are logged once at ERROR level with traceback, while clients receive only generic error messages.

github · maxisbey · Aug 24, 19:00

**「Design notes」** The Client accepts StdioServerParameters directly. Request body limits now apply to SSE and OAuth transports.

**「What changed」** Client accepts StdioServerParameters directly. Prompt messages accept Image and Audio, and prompt functions may return bare content blocks. The 4 MiB request body limit now covers SSE transport and OAuth endpoints. Handler exceptions are logged once at ERROR with traceback; clients see only generic error messages instead of exception text.

**Tags**: `#mcp`, `#runtime`, `#tools`

---

<a id="item-harness-arch-2"></a>
### [mem0 CLI v0.2.12 发布](https://github.com/mem0ai/mem0/releases/tag/cli-v0.2.12) ⭐️ 7.5/10

mem0 CLI v0.2.12 has been released. It adds a new \`mem0 version\` subcommand that allows scripts and agent harnesses to read the CLI version as a regular subcommand instead of a root-level flag. The \`add\` command now supports a new \`--agent-custom-instructions\` flag passed to the \`/v3/memories/add/\` payload for agent-scoped memories. The search --filter documentation was updated with JSON shape examples and commands.

github · kartik-mem0 · Aug 24, 13:15

**「设计要点」** The version subcommand is designed for harness and script integration by exposing version info as a standard CLI command. The --agent-custom-instructions flag supports agent-scoped memory extraction by adding a second instruction set to the memory add payload.

**「改了什么」** Relative to the previous version, the CLI now includes a version subcommand for script and harness integration and a new --agent-custom-instructions flag for the add command. The --filter help text and docs were updated with JSON structure examples and example commands.

**Tags**: `#cli`, `#memory`, `#agent`, `#version`, `#filter`

---

<a id="item-harness-arch-3"></a>
### [Cline SDK v0.0.79 发布](https://github.com/cline/cline/releases/tag/sdk/sdk/v0.0.79) ⭐️ 6.5/10

Cline SDK v0.0.79 introduces event log size limits and vacuuming for runtime storage. The durable event log is capped at 64 MiB, with pruning after every 16 MiB and vacuuming to reclaim space. It ensures task.completed telemetry is emitted in all session teardowns. The model catalog has been refreshed, adding providers like AgentRouter and Opper, and updating pricing and defaults.

github · github-actions\[bot\] · Aug 24, 23:01

**「设计要点」** The runtime storage now features a capped durable event log at 64 MiB with automatic vacuuming after every 16 MiB of new events to prevent disk bloat from accumulating session snapshots.

**「改了什么」** Relative to v0.0.78, the durable event log now has a 64 MiB cap with pruning and vacuuming after every 16 MiB. task.completed telemetry is emitted from every session teardown path. The model catalog was refreshed with new providers and updated defaults.

**Tags**: `#runtime`, `#memory`, `#planning`

---

<a id="item-harness-arch-4"></a>
### [mastra/core@1.61.0 released](https://github.com/mastra-ai/mastra/releases/tag/%40mastra/core%401.61.0) ⭐️ 6.5/10

mastra/core 1.61.0 has been released. It adds caller-driven experiments that let external orchestrators own the experiment loop while Mastra remains the system of record. Generated servers now support configurable drainTimeout and handleShutdownSignals for graceful shutdown. Sessions automatically mark messages as delivery: &\#x27;while-active&\#x27; when sent during active runs.

github · PaulieScanlon · Aug 24, 09:02

**「Design Points」** Experiments support external orchestrators with idempotent createExperiment and finalizeExperiment for result counts. Servers allow drainTimeout for in-flight request draining and handleShutdownSignals to disable built-in signal handlers.

**「What Changed」** This release adds caller-driven experiments for external orchestrators, configurable server shutdown draining, automatic while-active message delivery in sessions, atomic workflow resume with 409 conflicts, and createMultiTurnJudgeScorer for multi-turn evals.

**Tags**: `#runtime`, `#eval`, `#sessions`, `#experiments`, `#shutdown`

---

<a id="item-harness-arch-5"></a>
### [mem0-strands v0.1.0 released](https://github.com/mem0ai/mem0/releases/tag/mem0-strands-v0.1.0) ⭐️ 6.5/10

mem0-strands v0.1.0 is the initial release of a native MemoryStore that integrates Mem0 with Strands Agents MemoryManager. It enables automatic recall and injection of relevant memories every turn via Mem0MemoryStore.search\(\) with no explicit tool call required. Server-side extraction happens in add\_messages\(\) by rendering conversation turns and calling Mem0&\#x27;s extraction pipeline with infer=True.

github · kartik-mem0 · Aug 24, 20:06

**「Design notes」** The Mem0 client is constructed lazily inside asyncio.to\_thread on first use to avoid blocking the event loop. It defaults to the hosted Mem0 Platform via api\_key or $MEM0\_API\_KEY but can use a self-hosted config dict instead. At least one scoping parameter \(user\_id, agent\_id, run\_id, or app\_id\) is required at construction.

**「Changes」** This release adds automatic recall and injection to Strands Agents MemoryManager, server-side extraction in add\_messages\(\), verbatim writes via add\(\) with infer=False, and entity scoping support.

**Tags**: `#memory`, `#runtime`

---

<a id="item-harness-arch-6"></a>
### [mem0 deepseek-plugin-v0.1.0 发布](https://github.com/mem0ai/mem0/releases/tag/deepseek-plugin-v0.1.0) ⭐️ 6.5/10

这是 mem0 deepseek-plugin v0.1.0 的初始发布，一个原生 DeepSeek Harness \(Cordis\) 插件，将 Mem0 作为两个可调用的代理工具注册。新增的 search\_memory 工具可召回与查询相关的记忆，支持可选 limit 和作用域覆盖；add\_memory 工具存储事实以供未来会话使用，提取在服务器端异步进行。插件通过 apply\(ctx, config\) 声明 inject = \[&\#x27;tools&\#x27;\]，在工具注册表存在后使用 ctx.tools.register\(\) 注册工具，实现自动卸载。配置要求 userId，apiKey 默认从环境变量获取。

github · kartik-mem0 · Aug 24, 14:19

**「设计要点」** 插件在 Cordis 生命周期中使用 apply\(ctx, config\) 方法，声明 inject = \[&\#x27;tools&\#x27;\]，等待 harness 工具注册表存在后通过 ctx.tools.register\(\) 注册 search\_memory 和 add\_memory 工具。工具注册后会在插件卸载时自动注销。配置中 userId 是必需的，apiKey 默认使用 MEM0\_API\_KEY，host 可选指向专用 Mem0 Platform 基 URL。

**「改了什么」** 初始发布了 deepseek-plugin v0.1.0，新增了 search\_memory 和 add\_memory 两个工具。存储的记忆会标记 source: &quot;DEEPSEEK\_HARNESS&quot;，提取在服务器端异步运行，可能需要时间才能被搜索到。开发者预览的自动捕获和自动召回功能尚未实现。

**Tags**: `#tools`, `#memory`

---

<a id="item-harness-arch-7"></a>
### [Cline CLI v3.0.58 发布](https://github.com/cline/cline/releases/tag/cli-v3.0.58) ⭐️ 5.5/10

Cline CLI v3.0.58 发布了。它将 hub 事件日志上限设置为 64 MiB，并通过修剪机制来管理空间，避免日志无限增长。模型目录已刷新，新增了 AgentRouter 和 Opper 两个提供商，并更新了各提供商的模型列表和定价。

github · github-actions\[bot\] · Aug 24, 23:07

**「改了什么」** 相对上一版，hub 事件日志被限制在 64 MiB 并启用修剪机制。模型目录刷新，新增了 AgentRouter 和 Opper 提供商，并更新了定价和默认模型。

**Tags**: `#runtime`, `#memory`, `#tools`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [llm-anthropic 0.27 released](https://github.com/simonw/llm-anthropic/releases/tag/0.27) ⭐️ 7.5/10

Simon Willison released llm-anthropic 0.27. The update upgrades the Anthropic SDK to anthropic&gt;=1, fixes streaming errors for large models that previously errored on the streaming API, adds structured outputs support for Claude Haiku, enables inline system messages for Claude Opus 4.8 and the Claude 5 family, and preserves thinking blocks with redacted content in conversation history. This affects developers building coding agents and orchestration harnesses that integrate with Anthropic APIs.

github · simonw · Aug 24, 16:27

**「Why it matters」** The changes improve reliability for long-running API calls and enable better conversation management with newer Claude models.

**「Watch」** Watch: Support for mid-conversation system messages in Claude 4.8/5 family models and preservation of thinking blocks for tool continuations.

**Tags**: `#coding-agent`, `#orchestration`, `#harness`, `#eval`

---

## AI Daily

<a id="item-ai-daily-1"></a>
### [ADK adds native live voice evaluation](https://developers.googleblog.com/how-to-evaluate-live-voice-agents-in-adk/) ⭐️ 8.5/10

Google Developers says ADK now supports native live evaluation for voice agents. A simulated user speaks its turns as audio, spoken replies are scored, and the run uses the same eval loop as text agents. Cases are JSON—either a conversation\_scenario \(goal, persona, improvised turns; the simulator ends when the plan is done\) or a fixed script of user turns—and live mode is opt-in via live\_model\_config. The sample three-agent Workflow on gemini-live-2.5-flash-native-audio uses an llm\_audio simulator with max\_allowed\_invocations 10, timeout\_seconds 300, and rubric\_based\_multi\_turn\_trajectory\_quality\_v1 at threshold 0.7; you run it with \`adk eval\` or AgentEvaluator, after installing eval extras and configuring Live API plus Gemini TTS credentials.

rss · Google Developers AI · Aug 24, 00:00

**「Why it matters」** The same JSON eval cases can be pointed at a live voice agent instead of a separate audio harness. The post says AgentEvaluator can call that pipeline from CI/CD.

**「Watch for」** Watch for: omitting live\_model\_config runs the exact same cases in standard text mode. For type llm\_audio, model is the simulated user’s turn-taking logic \(sample: gemini-3.7-flash\) and audio\_model synthesizes speech \(sample: gemini-3.1-flash-tts-preview\); voice\_name and language\_code are how you vary voice and accent.

**Tags**: `#ADK`, `#Google`, `#voice`, `#eval`, `#product`

---

<a id="item-ai-daily-2"></a>
### [GPT-5.6 in Kiro: Better Price-Performance for Developers](https://openai.com/index/gpt-5-6-in-kiro) ⭐️ 6.5/10

OpenAI has made GPT-5.6 available in Kiro. This helps developers plan, build, review, and test software with better price-performance.

rss · OpenAI Blog · Aug 24, 12:00

**「Why It Matters」** The new availability of GPT-5.6 in Kiro provides developers with improved price-performance for software development tasks.

**「Takeaway」** Takeaway: GPT-5.6 in Kiro offers better price-performance when developers plan, build, review, and test software.

**Tags**: `#model`, `#lab`, `#industry`, `#product`

---

<a id="item-ai-daily-3"></a>
### [Anthropic Field Marketer Uses Claude Code for Weekly Sales Updates](https://claude.com/blog/how-an-anthropic-field-marketer-uses-claude-code-to-send-weekly-personalized-updates-to-every-sales-rep) ⭐️ 5.5/10

Anthropic field marketer Adam Ward uses Claude Code to convert one weekly sales report into a personalized Monday briefing for every account executive he supports. He set this up during a marketing hackathon by explaining the business problem to Claude and connecting it to BigQuery via MCP for data from HubSpot, Clay, and Salesforce. After testing with a small team of 10 and refining the prompt based on feedback, the digest is now sent to all sales reps every Monday, with some events seeing doubled registrations.

rss · Claude Blog · Aug 24, 00:00

**「Why it matters」** This case study shows how marketers can use Claude Code to automate personalized content creation, cutting manual effort and making updates more relevant for sales teams.

**「Takeaway」** Takeaway: Start small with a repetitive task you already do manually and ask Claude to rebuild it. You don&\#x27;t need to code; you need to explain the problem clearly to Claude.

**Tags**: `#anthropic`, `#claude`, `#marketing`, `#ai-application`, `#productivity`

---