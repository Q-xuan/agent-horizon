---
layout: default
title: "Horizon Summary: 2026-08-28 (EN)"
date: 2026-08-28
lang: en
---

> From 234 items, 18 important content pieces were selected

---

**Agent Harness Architecture**
1. [Claude Code v2.1.248 Released](#item-harness-arch-1) ⭐️ 8.5/10
2. [FastMCP v4.0.0b5 发布](#item-harness-arch-2) ⭐️ 8.5/10
3. [Cloudflare Agents 0.22.0 Released](#item-harness-arch-3) ⭐️ 7.5/10
4. [cloudflare/agents @cloudflare/think@0.17.0 发布](#item-harness-arch-4) ⭐️ 7.5/10
5. [Cloudflare Agents @cloudflare/ai-chat 0.11.0 Released](#item-harness-arch-5) ⭐️ 7.5/10
6. [LangChain 1.4.0a1 Released](#item-harness-arch-6) ⭐️ 7.5/10
7. [Instructor v1.16.0 发布](#item-harness-arch-7) ⭐️ 7.5/10
8. [anthropics/skills GitHub trending](#item-harness-arch-8) ⭐️ 5.0/10

**AI Agent Engineer**
1. [DeepMind Pilots the World&\#x27;s First Double-Blind AI Evaluations](#item-agent-engineer-1) ⭐️ 8.5/10
2. [Gemini Omni 1.1 Flash 发布](#item-agent-engineer-2) ⭐️ 7.5/10
3. [Breaking Claude Code Opus 5 Auto Mode](#item-agent-engineer-3) ⭐️ 7.0/10
4. [PILOT: Live Self-Improvement for Long-Horizon Agents](#item-agent-engineer-4) ⭐️ 7.0/10
5. [Gemini-3.5-Transcribe 发布](#item-agent-engineer-5) ⭐️ 6.0/10

**AI Daily**
1. [ChatGPT and Critical-Thinking Training: Better Answers and Broader Thinking](#item-ai-daily-1) ⭐️ 7.5/10
2. [Ruanyifeng Weekly 410: Three AI Mechanisms You Need to Know](#item-ai-daily-2) ⭐️ 5.0/10

**AI Deals**
1. [Zhipu AI Open Sources GLM-5.3-Flash Native Multimodal Model](#item-ai-deals-1) ⭐️ 6.0/10
2. [AI Engineer Notebooks：Colab 免费 RAG/agents/evals](#item-ai-deals-2) ⭐️ 5.0/10
3. [Junie Local Launch on Mac – No Credits, No Cloud](#item-ai-deals-3) ⭐️ 5.0/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [Claude Code v2.1.248 Released](https://github.com/anthropics/claude-code/releases/tag/v2.1.248) ⭐️ 8.5/10

Claude Code v2.1.248 has been released. It adds restricted harness mode, prompt cache TTL, runner label customization, and config diagnostics.

Restricted mode limits command tools and WebFetch while preserving working-dir file tools and refusing bypassPermissions. Experimental per-agent cacheTtl is added to agent frontmatter. Self-hosted runner client-label override and settings load diagnostics are also included.

github · ashwin-ant · Aug 27, 22:12

**「Design Points」** Restricted mode enforces sandboxing by limiting tools and permissions while preserving working directory file access. Experimental per-agent prompt cache TTL manages memory usage. Self-hosted runners support custom client labels for runtime identification.

**「What&\#x27;s Changed」** Added restricted mode \(--restricted or CLAUDE\_CODE\_RESTRICTED=1\) that removes built-in command tools and WebFetch unless named, keeps file tools inside the working directory, refuses bypassPermissions, and ignores user/project/local settings. Added experimental.cacheTtl to agent frontmatter. Added claude self-hosted-runner --client-label to override the runner label. Added server-managed settings diagnostics on startup.

**Tags**: `#tools`, `#permissions`, `#sandbox`, `#memory`, `#runtime`

---

<a id="item-harness-arch-2"></a>
### [FastMCP v4.0.0b5 发布](https://github.com/PrefectHQ/fastmcp/releases/tag/v4.0.0b5) ⭐️ 8.5/10

FastMCP v4.0.0b5 introduces ClientGroup for independent multi-server client management with tool namespacing and routing. It also aligns middleware response limits with output schemas.

github · zzstoatzz · Aug 28, 02:57

**「设计要点」** ClientGroup enables one client per server with independent protocol eras, collision-checked tool namespacing/routing, and no proxy. Middleware response limits aligned with output schemas.

**「改了什么」** Added independent client groups for multi-server management. Aligned middleware response limits with output schemas.

**Tags**: `#mcp`, `#tools`, `#runtime`, `#ClientGroup`

---

<a id="item-harness-arch-3"></a>
### [Cloudflare Agents 0.22.0 Released](https://github.com/cloudflare/agents/releases/tag/agents%400.22.0) ⭐️ 7.5/10

Cloudflare Agents 0.22.0 is released. Durable chat recovery is now unconditional for AIChatAgent and Think, with every turn running in recovery fibers across WebSocket, retry, and continuation paths. chatRecovery accepts true or a configuration object; false is no longer supported. To keep durable bookkeeping while preventing automatic inference after an interruption, return \{ continue: false \} from onChatRecovery\(\).

github · ben-reitz · Aug 27, 14:07

**「Design notes」** Agent now directly extends Cloudflare&\#x27;s DurableObject and composes the same lifecycle used by standalone objects. Scheduler is a reusable Lifecycle capability for persistent delayed, dated, cron, and interval callbacks.

**「Changes」** Durable chat recovery is now unconditional, removing support for false in chatRecovery. The published agents CLI binary is removed and MCPClientManager is made a reusable Durable Object lifecycle capability.

**Tags**: `#runtime`, `#memory`, `#durable`, `#recovery`

---

<a id="item-harness-arch-4"></a>
### [cloudflare/agents @cloudflare/think@0.17.0 发布](https://github.com/cloudflare/agents/releases/tag/%40cloudflare/think%400.17.0) ⭐️ 7.5/10

Cloudflare agents @cloudflare/think@0.17.0 has been released. Think 0.17.0 makes durable chat recovery unconditional for AIChatAgent and Think. Every chat turn now runs in a recovery fiber, including WebSocket, programmatic, retry, and continuation paths. chatRecovery accepts true or a configuration object; false is no longer supported. Previously compiled JavaScript that still supplies false safely receives the default recovery configuration.

github · ben-reitz · Aug 27, 14:07

**「改了什么」** This release makes durable chat recovery unconditional for AIChatAgent and Think, with every chat turn running in a recovery fiber across all paths. chatRecovery now accepts true or a configuration object instead of a boolean, with false no longer supported. It also preserves orphaned durable execution outcomes as framework-authored notes and projects them to user context for inference.

**Tags**: `#runtime`, `#memory`, `#recovery`, `#durable`, `#chat`

---

<a id="item-harness-arch-5"></a>
### [Cloudflare Agents @cloudflare/ai-chat 0.11.0 Released](https://github.com/cloudflare/agents/releases/tag/%40cloudflare/ai-chat%400.11.0) ⭐️ 7.5/10

Cloudflare Agents @cloudflare/ai-chat 0.11.0 is released. This minor update makes durable chat recovery unconditional for AIChatAgent and Think. Every chat turn now runs in a recovery fiber, including WebSocket, programmatic, retry, and continuation paths.

github · ben-reitz · Aug 27, 14:07

**「Design notes」** AIChatAgent now runs every chat turn in a recovery fiber to ensure durable bookkeeping. The onChatRecovery hook allows custom recovery logic, such as returning \{ continue: false \} to prevent automatic inference after interruptions. The chatRecovery option accepts true or a configuration object.

**「What changed」** Durable chat recovery is now unconditional for AIChatAgent and Think. The chatRecovery parameter accepts true or a configuration object; false is no longer supported. Previously compiled JavaScript supplying false will receive the default recovery configuration.

**Tags**: `#runtime`, `#memory`, `#durable`, `#recovery`, `#chat`

---

<a id="item-harness-arch-6"></a>
### [LangChain 1.4.0a1 Released](https://github.com/langchain-ai/langchain/releases/tag/langchain%3D%3D1.4.0a1) ⭐️ 7.5/10

LangChain 1.4.0a1 is an alpha release centered on MCP adapter refactors for type safety and protocol handling across servers. Key updates restructure elicitation request and response types to one per mode, refuse continuation rounds instead of polling, and provide multi-server test coverage for both protocol eras through a single adapter. The release ports MCP tool conversion from langchain-mcp-adapters, simplifies MCPAdapter construction, and requires FastMCP 4.0.0b4 for the mcp extra.

github · github-actions\[bot\] · Aug 27, 22:21

**「What Changed」** This alpha release relative to 1.3.x series introduces MCP protocol refactors including elicitation type changes per mode, refusal of continuation rounds, and simplified adapter internals. It also ports tool conversion logic and adds multi-server test coverage for protocol eras.

**Tags**: `#mcp`, `#runtime`, `#protocol`, `#refactor`, `#test`

---

<a id="item-harness-arch-7"></a>
### [Instructor v1.16.0 发布](https://github.com/567-labs/instructor/releases/tag/v1.16.0) ⭐️ 7.5/10

567-labs/instructor v1.16.0 adds native AWS Bedrock structured outputs and a cumulative token\_budget for validation retries. Bedrock now exposes Mode.JSON\_SCHEMA and Mode.TOOLS\_STRICT through Converse outputConfig.textFormat and strict tool schemas, with recursive schema normalization and a boto3 1.42.42 minimum; model selection stays caller-controlled. token\_budget applies to structured non-streaming retries, keeps immutable completion:usage snapshots with sync/async cutoff parity, and a failed attempt with unavailable usage stops before another provider call—valid responses still win after the budget is crossed.

github · github-actions\[bot\] · Aug 27, 15:33

**「设计要点」** Bedrock structured output is wired through Converse: JSON\_SCHEMA via outputConfig.textFormat, TOOLS\_STRICT via strict tool schemas, plus recursive schema normalization. Retry control is a positive cumulative token\_budget on structured non-streaming attempts; usage snapshots are immutable, sync and async share the same cutoff, and a failed attempt with no usage does not trigger another provider call.

**「改了什么」** Native Bedrock JSON\_SCHEMA and TOOLS\_STRICT modes landed, along with token\_budget retry accounting that still accepts a valid response after the cap. Notable fixes include parsing Bedrock JSON after reasoning or &lt;think&gt; blocks, keeping OpenAI TOOLS/JSON/JSON\_SCHEMA/MD\_JSON streaming retries after the one-shot marker, member-by-member PEP 604 iterable unions, mistralai 2.x on Python 3.10+ with a 1.x fallback on 3.9, and a 30-second timeout on remote image, audio, and PDF fetches.

**Tags**: `#runtime`, `#tools`, `#structured-outputs`, `#bedrock`, `#retry`

---

<a id="item-harness-arch-8"></a>
### [anthropics/skills GitHub trending](https://github.com/anthropics/skills) ⭐️ 5.0/10

Anthropic&\#x27;s Agent Skills repository is trending on GitHub. Skills are defined as dynamically loaded folders containing instructions, scripts, and resources that Claude uses for specialized tasks. The repo implements the Agent Skills standard and links to agentskills.io for details.

rss · GitHub Trending Daily · Aug 28, 05:56

**Tags**: `#tools`, `#memory`, `#planning`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [DeepMind Pilots the World&\#x27;s First Double-Blind AI Evaluations](https://deepmind.google/blog/piloting-the-worlds-first-double-blind-ai-evaluations/) ⭐️ 8.5/10

Google DeepMind is piloting the world&\#x27;s first double-blind AI evaluations. This new methodology for AI assessments keeps both evaluators and evaluated systems unaware of each other&\#x27;s identities. The initiative affects AI evaluation harnesses and agent benchmarking workflows.

rss · Google DeepMind · Aug 27, 12:59

**「Why it matters」** The piloting of double-blind AI evaluations is directly relevant to improving eval harnesses and agent benchmarking workflows.

**「What to watch」** What to watch: Double-blind AI evaluations.

**Tags**: `#eval`, `#harness`, `#benchmark`

---

<a id="item-agent-engineer-2"></a>
### [Gemini Omni 1.1 Flash 发布](https://deepmind.google/blog/gemini-omni-1-1-flash-lets-you-build-with-more-control/) ⭐️ 7.5/10

Google DeepMind 发布了 Gemini Omni 1.1 Flash，这是一个旨在提供更大构建控制的模型版本。官方 DeepMind 博客公告强调了这一更新。该模型版本针对代理架构、工具集成和编排 harness 提供支持。

rss · Google DeepMind · Aug 27, 16:11

**「为什么重要」** Google DeepMind 发布了 Gemini Omni 1.1 Flash。影响开发者在代理架构、工具集成和编排 harness 中的使用。

**「可关注」** 可关注：Gemini Omni 1.1 Flash 提供了更大的构建控制。

**Tags**: `#coding-agent`, `#orchestration`, `#harness`

---

<a id="item-agent-engineer-3"></a>
### [Breaking Claude Code Opus 5 Auto Mode](https://simonwillison.net/2026/Aug/27/breaking-claude-code-opus-5-auto-mode/) ⭐️ 7.0/10

Researchers demonstrated a practical attack that bypasses Anthropic&\#x27;s Claude Code auto mode 80% of the time by tricking it into downloading and uncompressing a malicious zip archive. The code then executes via local imports such as base64, which pulls in a struct.py file from the archive. In some cases, the auto mode blocks the agent&\#x27;s cleanup commands, allowing harmful execution to continue. This affects users of the Claude Code coding agent who depend on auto mode for protection against prompt injection attacks.

rss · Simon Willison · Aug 27, 22:50

**「Why it matters」** The attack undermines Anthropic&\#x27;s default auto mode claims for protecting against prompt injection. While the bypass works in most runs, the exact impact on agent deployments is still uncertain.

**「Takeaway」** Takeaway: The safety mechanism itself can become part of the failure when it blocks cleanup commands for the malware process. The only safe way to run agents if there&\#x27;s any risk of attracting the attention of an adversarial attack is with a sandbox.

**Tags**: `#coding-agent`, `#permissions`

---

<a id="item-agent-engineer-4"></a>
### [PILOT: Live Self-Improvement for Long-Horizon Agents](https://huggingface.co/papers/2608.26530) ⭐️ 7.0/10

The paper proposes PILOT, a supervisor-worker harness for live self-improvement in long-horizon agents. It uses emerging experience in real time to redirect active runs and update persistent harnesses. This addresses limitations in single-agent self-correction and subagent delegation, which cannot redirect an active run or immediately apply lessons learned. The approach impacts agent architecture, harness design, and self-improvement workflows.

rss · Hugging Face Daily Papers · Aug 28, 00:00

**「Why it matters」** Live self-improvement enables real-time redirection of active runs using emerging experience, shifting from post-execution methods. This could improve long-horizon agent performance, though broader validation of the approach remains needed.

**「What to watch」** What to watch: The coupled live redirection and harness update mechanisms in PILOT for self-improvement.

**Tags**: `#harness`, `#orchestration`, `#eval`, `#coding-agent`

---

<a id="item-agent-engineer-5"></a>
### [Gemini-3.5-Transcribe 发布](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5-transcribe/) ⭐️ 6.0/10

Google 发布了 Gemini-3.5-Transcribe STT 模型。该模型在准确性上优于其他替代模型，但在实时翻译应用中的延迟存在担忧。模型支持通过函数调用委托复杂任务，如图像生成和文件分析，目前在 Gemini macOS 应用中可用。

hackernews · k9294 · Aug 27, 18:03 · [Discussion](https://news.ycombinator.com/item?id=49468818)

**「为什么重要」** 该模型的发布为实时 STT 应用提供了高准确性的选项，尽管延迟仍是关键因素。

**「可关注」** 可关注：尽管准确性高，但实时应用中需关注延迟性能。

**「评论」** 社区测试显示 Soniox STT v5 在延迟方面表现最佳，Gemini-3.5-Transcribe 在准确性上胜出。部分用户对 STT 模型能否进行函数调用感到困惑。

**Tags**: `#eval`, `#orchestration`, `#coding-agent`

---

## AI Daily

<a id="item-ai-daily-1"></a>
### [ChatGPT and Critical-Thinking Training: Better Answers and Broader Thinking](https://openai.com/index/what-students-gain-from-chatgpt-critical-thinking-training) ⭐️ 7.5/10

OpenAI published findings from a randomized study of more than 1,000 students. The study examined what students gain from ChatGPT and critical-thinking training. Researchers focused on better answers, broader thinking, originality, and performance on real-world university assignments.

rss · OpenAI Blog · Aug 27, 09:00

**「Key takeaway」** Key takeaway: Students who used ChatGPT with critical-thinking training gained better answers, broader thinking, originality, and improved performance on real-world university assignments.

**Tags**: `#OpenAI`, `#ChatGPT`, `#education`, `#study`, `#critical thinking`

---

<a id="item-ai-daily-2"></a>
### [Ruanyifeng Weekly 410: Three AI Mechanisms You Need to Know](http://www.ruanyifeng.com/blog/2026/08/weekly-issue-410.html) ⭐️ 5.0/10

Ruanyifeng&\#x27;s 410th weekly tech newsletter discusses three AI mechanisms that enthusiasts need to know. The issue is a regular Friday publication compiling tech content worth sharing. The provided material offers only a high-level overview with no specific details, mechanisms described, or comparisons included.

rss · 阮一峰 · Aug 27, 23:56

**Tags**: `#industry`, `#model`, `#eval`

---

## AI Deals

<a id="item-ai-deals-1"></a>
### [Zhipu AI Open Sources GLM-5.3-Flash Native Multimodal Model](https://sspai.com/post/113922) ⭐️ 6.0/10

Zhipu AI has open-sourced its GLM-5.3-Flash native multimodal model. The model is available for free download and use. This announcement is part of their open-source initiative.

rss · 少数派 · Aug 28, 00:29

**Tags**: `#free-tier`, `#promo`, `#open-source`

---

<a id="item-ai-deals-2"></a>
### [AI Engineer Notebooks：Colab 免费 RAG/agents/evals](https://github.com/calmrocks/ai-engineer-notebooks) ⭐️ 5.0/10

calmrocks 在 GitHub 分享了免费、框架-free 的 RAG、agents 和 evals 笔记本，可直接在 Google Colab 上运行。

rss · HN Free API / Credits · Aug 27, 21:46

**「可关注」** 可关注：这些笔记本无需任何特定框架，适用于所有使用 Google Colab 的开发者。

**Tags**: `#free-tier`, `#colab`, `#rag`, `#agents`, `#evals`

---

<a id="item-ai-deals-3"></a>
### [Junie Local Launch on Mac – No Credits, No Cloud](https://blog.jetbrains.com/junie/2026/08/junie-local-launch/) ⭐️ 5.0/10

JetBrains announces that Junie can now run locally on Mac without credits or cloud. The feature is detailed in an official blog post. No quotas, models, pricing, or deadlines are mentioned.

rss · HN Free API / Credits · Aug 27, 11:30

**Tags**: `#promo`, `#free-tier`, `#api`, `#mac`

---