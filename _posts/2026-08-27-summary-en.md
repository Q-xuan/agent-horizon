---
layout: default
title: "Horizon Summary: 2026-08-27 (EN)"
date: 2026-08-27
lang: en
---

> From 153 items, 14 important content pieces were selected

---

**Agent Harness Architecture**
1. [Codex rust-v0.150.0 发布](#item-harness-arch-1) ⭐️ 7.5/10
2. [Cline SDK v0.0.81 Released](#item-harness-arch-2) ⭐️ 7.5/10
3. [Cline desktop-v0.0.19 Released](#item-harness-arch-3) ⭐️ 7.5/10
4. [google/adk-python v2.8.0 发布](#item-harness-arch-4) ⭐️ 7.5/10
5. [mastra-ai/mastra @mastra/core@1.62.0 release](#item-harness-arch-5) ⭐️ 7.5/10
6. [Cline SDK v0.0.80](#item-harness-arch-6) ⭐️ 6.5/10
7. [Cline CLI v3.0.60 发布](#item-harness-arch-7) ⭐️ 6.5/10

**AI Agent Engineer**
1. [Qwen3.8-Flash-Next multimodal MoE model preview](#item-agent-engineer-1) ⭐️ 6.0/10
2. [研究人员适应 Dolma 改进泰语模型](#item-agent-engineer-2) ⭐️ 5.5/10

**AI Daily**
1. [OpenAI Expands ChatGPT for Teachers to 55 U.S. School Districts](#item-ai-daily-1) ⭐️ 7.5/10
2. [OpenAI 报告：AI 让学习持续进行](#item-ai-daily-2) ⭐️ 6.5/10

**AI Deals**
1. [Unreal Tournament 2004 Now Free with Modern PC Update](#item-ai-deals-1) ⭐️ 6.0/10
2. [Free API Joins Six Dutch Government Datasets into One REST Endpoint](#item-ai-deals-2) ⭐️ 5.0/10
3. [Superwhisper Launches Free Dictation](#item-ai-deals-3) ⭐️ 5.0/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [Codex rust-v0.150.0 发布](https://github.com/openai/codex/releases/tag/rust-v0.150.0) ⭐️ 7.5/10

OpenAI Codex rust-v0.150.0 has been released. It adds task referencing with @ mentions from the terminal to read, create, or message other tasks, along with terminal enhancements like auto descriptive titles for unnamed tasks and a /copy response picker. New Interrupt hooks run commands or MCP handlers when a top-level turn is interrupted. Bug fixes include untrusted projects no longer supplying project-level AGENTS.md and improved credential redaction in diagnostics.

github · github-actions\[bot\] · Aug 26, 19:37

**「改了什么」** This release adds @ task referencing, terminal auto-titling, /copy pickers, permission mode cycling shortcuts, and Interrupt hooks. It also fixes AGENTS.md restrictions for untrusted projects and improves MCP bearer token handling while preserving compatibility with older executors.

**Tags**: `#runtime`, `#permissions`, `#tools`, `#subagents`, `#mcp`

---

<a id="item-harness-arch-2"></a>
### [Cline SDK v0.0.81 Released](https://github.com/cline/cline/releases/tag/sdk/sdk/v0.0.81) ⭐️ 7.5/10

Cline SDK v0.0.81 optimizes session event payloads by stripping full conversation history from snapshots and routing transcripts through a dedicated messages command. Session snapshot events no longer embed the full conversation transcript. Snapshots are now state-only \(status, usage, model, workspace, checkpoint\); transcripts are fetched separately via the session.messages command.

github · github-actions\[bot\] · Aug 26, 09:38

**「Design Points」** The change optimizes runtime memory usage. Previously, each event carried the full transcript, leading to large memory copies and potential process bloat \(reported as a 25 GB cline process on a 16 GB machine\). Snapshots are now state-only to reduce per-event memory overhead.

**「What Changed」** Session snapshot events no longer carry the full conversation transcript. Snapshots are now state-only \(status, usage, model, workspace, checkpoint\); transcripts are fetched with the session.messages command. Checkpoint-restore replies, which carry messages in their own field, are unaffected.

**Tags**: `#runtime`, `#memory`

---

<a id="item-harness-arch-3"></a>
### [Cline desktop-v0.0.19 Released](https://github.com/cline/cline/releases/tag/desktop-v0.0.19) ⭐️ 7.5/10

Cline desktop-v0.0.19 is released. It optimizes memory usage in the background process for extended sessions and refreshes supported AI model providers. The key technical change is the runtime memory model update: session status updates now carry only state \(status, usage, model, workspace, checkpoint\); the transcript is fetched on demand to prevent process ballooning in long sessions. The model catalog has been refreshed with seven new providers and updated model lists and pricing.

github · github-actions\[bot\] · Aug 26, 09:31

**「Design Points」** The release modifies the runtime memory model for the background process. Status updates now carry only state; the transcript is fetched on demand to prevent the process from ballooning to tens of gigabytes in long sessions.

**「What Changed」** Relative to desktop-v0.0.18, the background Cline process no longer balloons in memory during long sessions. The model catalog was refreshed, adding seven providers and changing default models for several platforms.

**Tags**: `#runtime`, `#memory`, `#tools`

---

<a id="item-harness-arch-4"></a>
### [google/adk-python v2.8.0 发布](https://github.com/google/adk-python/releases/tag/v2.8.0) ⭐️ 7.5/10

Google ADK Python v2.8.0 is released. It adds data agent management tools including create\_data\_agent, delete\_data\_agent, update\_data\_agent, and list\_accessible\_data\_agents with location parameter support. The release introduces the ADK\_MAX\_LLM\_CALLS environment variable to configure max LLM calls limit, native A2A task mode support for RemoteA2aAgent, and Model Armor guardrail plugin integration.

github · wukath · Aug 26, 23:25

**「改了什么」** Relative to v2.7.1, v2.8.0 adds data agent management tools, ADK\_MAX\_LLM\_CALLS environment variable, RemoteA2aAgent A2A native task mode, and Model Armor guardrail plugin.

**Tags**: `#tools`, `#runtime`, `#a2a`, `#guardrail`

---

<a id="item-harness-arch-5"></a>
### [mastra-ai/mastra @mastra/core@1.62.0 release](https://github.com/mastra-ai/mastra/releases/tag/%40mastra/core%401.62.0) ⭐️ 7.5/10

mastra-ai/mastra releases @mastra/core@1.62.0 introducing Elasticsearch + Valkey storage backends, computer-use sandboxes, and sandbox lifecycle/runtime env controls. The release adds @mastra/elasticsearch for a unified cluster powering memory, workflow snapshots, scores, and semantic recall. New @mastra/valkey and @mastra/valkey-streams packages provide GLIDE-backed storage, cache, PubSub, and lease providers.

github · PaulieScanlon · Aug 26, 13:40

**「Design Points」** Sandboxes now own their runtime environment through MastraSandbox with getEnv/setEnv methods that merge into process spawns. Computer-use sandboxes expose optional SandboxComputer capability for screenshots, mouse/keyboard control, and noVNC via E2B Desktop provider.

**「What&\#x27;s Changed」** Added Elasticsearch and Valkey storage backends with metadata filtering and count support. Introduced computer-use sandboxes, runtime env controls for dynamic updates, safer shutdowns, and suspend/resume on workspaces.

**Tags**: `#runtime`, `#sandbox`, `#storage`, `#tools`, `#memory`

---

<a id="item-harness-arch-6"></a>
### [Cline SDK v0.0.80](https://github.com/cline/cline/releases/tag/sdk/sdk/v0.0.80) ⭐️ 6.5/10

Cline SDK v0.0.80 has been released. It enables file-writing tools to use native line endings, fixes search\_codebase crashes on files with a single enormous line, redacts git credentials from prompts, marks Claude Code as a subscription-billed provider, updates MCP server install, adds scheduling config to the tasks tool, and refreshes the model catalog with seven new providers and default model changes.

github · github-actions\[bot\] · Aug 26, 08:45

**「What changed」** Relative to v0.0.79, Cline SDK v0.0.80 changes file tools to use native line endings, fixes search\_codebase crash on large lines, redacts git credentials in prompts, treats Claude Code as subscription provider, updates MCP install to ignore -- separator, adds scheduling-only mode to tasks tool, and refreshes model catalog with seven new providers and updated defaults.

**Tags**: `#runtime`, `#tools`, `#mcp`, `#permissions`, `#eval`

---

<a id="item-harness-arch-7"></a>
### [Cline CLI v3.0.60 发布](https://github.com/cline/cline/releases/tag/cli-v3.0.60) ⭐️ 6.5/10

Cline CLI v3.0.60 is released. It fixes memory ballooning in the background hub during long sessions by stopping the broadcasting of full conversation transcripts to connected clients. The release also resolves codebase search crashes on files with enormous lines, fixes MCP server installation argument parsing, stops showing costs for Claude Code, redacts git credentials from workspace info sent to models, and refreshes the model catalog with new providers and updated defaults.

github · github-actions\[bot\] · Aug 26, 09:43

**「改了什么」** Relative to v3.0.59, the update retires the running hub to apply the memory fix for long sessions. It prevents crashes in the codebase search tool for large lines, corrects MCP install parsing, removes Claude Code cost estimates, redacts git credentials, and refreshes the model catalog with seven new providers and changed defaults for several providers.

**Tags**: `#runtime`, `#memory`, `#tools`, `#mcp`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [Qwen3.8-Flash-Next multimodal MoE model preview](https://simonwillison.net/2026/Aug/26/qwen38-flash-next/) ⭐️ 6.0/10

Simon Willison reviews Qwen3.8-Flash-Next, a new open-weights multimodal Mixture-of-Experts model with 125B total parameters and 6B active parameters, serving as an early preview of the Qwen4 architecture. The model was tested on NVIDIA DGX Spark hardware using Unsloth GGUF quantized versions, including a 72.5GB UD-IQ1\_S variant and a 78.9GB UD-Q2\_K\_XL variant, which generated image examples such as pelicans riding bicycles.

rss · Simon Willison · Aug 26, 23:52

**「What to watch」** Watch: Unsloth GGUF quantized versions of Qwen3.8-Flash-Next on DGX Spark hardware for local multimodal experiments.

**Tags**: `#coding-agent`, `#harness`, `#orchestration`, `#eval`

---

<a id="item-agent-engineer-2"></a>
### [研究人员适应 Dolma 改进泰语模型](https://allenai.org/blog/thai-llm-dolma) ⭐️ 5.5/10

泰语研究人员采用了 Allen AI 开放的 Dolma 工具包，构建了 Mangosteen，一个包含 47 亿 token 的泰语语料库。该语料库通过过滤低质量网络数据生成，同时保持或提升了模型性能，并加强了泰语文化知识。该工作在 Allen AI 博客中公布，可能为 harness 和 eval 中的多语言数据 curation 提供见解。

rss · Allen AI · Aug 26, 08:00

**「为什么重要」** 这一改动确认了 Dolma 工具包可用于特定语言的语料库构建，并展示了质量过滤带来的性能优势。创建 Mangosteen 并保持性能是已确认的变化，但其对 AI Agent harness 的实际影响尚未被证实。

**「可关注」** 可关注：研究人员使用 Dolma 工具包过滤低质量数据，构建了 47 亿 token 的泰语 Mangosteen 语料库，同时保持或提升了模型性能。

**Tags**: `#harness`, `#eval`, `#orchestration`

---

## AI Daily

<a id="item-ai-daily-1"></a>
### [OpenAI Expands ChatGPT for Teachers to 55 U.S. School Districts](https://openai.com/index/bringing-chatgpt-for-teachers-to-more-us-school-districts) ⭐️ 7.5/10

OpenAI is expanding ChatGPT for Teachers to 55 additional U.S. school districts. This brings secure AI tools, training, and support to over 100,000 more educators and staff.

rss · OpenAI Blog · Aug 26, 10:00

**「Watch」** Watch: Secure AI tools, training, and support now available for over 100,000 educators and staff in 55 new U.S. school districts.

**Tags**: `#lab`, `#industry`, `#policy`, `#product`

---

<a id="item-ai-daily-2"></a>
### [OpenAI 报告：AI 让学习持续进行](https://openai.com/index/learning-never-stops) ⭐️ 6.5/10

OpenAI released a report exploring how students and educators use ChatGPT to make learning continuous, with support extending beyond the classroom. The report examines current usage patterns of ChatGPT in educational settings. This is not a new model or policy release but an analysis of AI applications in ongoing learning.

rss · OpenAI Blog · Aug 26, 10:00

**「为什么重要」** The report is important because it provides insights into how AI can support continuous learning outside traditional classroom hours, potentially influencing educational tool development.

**「可关注」** 可关注：ChatGPT is used by students and educators to extend learning beyond the classroom.

**Tags**: `#lab`, `#industry`, `#product`

---

## AI Deals

<a id="item-ai-deals-1"></a>
### [Unreal Tournament 2004 Now Free with Modern PC Update](https://www.pcgamer.com/games/fps/unreal-tournament-2004-is-now-available-for-free-thanks-to-its-fan-community-and-theyve-even-updated-the-game-for-modern-pcs-this-is-the-first-public-patch-for-unreal-tournament-2004-in-over-20-years/) ⭐️ 6.0/10

The fan community has made Unreal Tournament 2004 available for free. The game has received its first public update in over 20 years, optimized for modern PCs.

rss · HN Free API / Credits · Aug 26, 15:54

**「Why It Matters」** The update allows players to enjoy the classic FPS on modern hardware.

**「Note」** Note: The patch is for modern PCs, suitable for current hardware.

**Tags**: `#promo`, `#limited-free`

---

<a id="item-ai-deals-2"></a>
### [Free API Joins Six Dutch Government Datasets into One REST Endpoint](https://lookaal.dev/) ⭐️ 5.0/10

Lookaal.dev offers a free API that joins six Dutch government datasets into one REST endpoint.

The service is promoted as free with no specific quota, model, or price details mentioned.

No claiming conditions or deadlines are provided in the material.

rss · HN Free API / Credits · Aug 26, 21:52

**Tags**: `#free-tier`, `#api`, `#promo`

---

<a id="item-ai-deals-3"></a>
### [Superwhisper Launches Free Dictation](https://twitter.com/superwhisper/status/2092660873311436832) ⭐️ 5.0/10

Superwhisper just launched free dictation. This is a free-tier feature. No specific quotas, expiration dates, access conditions, or restrictions are mentioned. The announcement came from their official Twitter account.

rss · HN Free API / Credits · Aug 26, 18:46

**Tags**: `#free-tier`, `#promo`, `#limited-free`

---