---
layout: default
title: "Horizon Summary: 2026-09-12 (EN)"
date: 2026-09-12
lang: en
---

> From 149 items, 16 important content pieces were selected

---

**Agent Harness Architecture**
1. [Cloudflare Agents agents@0.23.0 发布](#item-harness-arch-1) ⭐️ 8.8/10
2. [Cloudflare agents @0.12.0 release](#item-harness-arch-2) ⭐️ 8.8/10
3. [DSPy 3.4.0b1 发布](#item-harness-arch-3) ⭐️ 8.8/10
4. [Mastra @mastra/core@1.66.0 发布](#item-harness-arch-4) ⭐️ 7.8/10
5. [Microsoft Agent Framework .NET 1.21.0 Released](#item-harness-arch-5) ⭐️ 7.8/10
6. [Claude Code v2.1.269 发布](#item-harness-arch-6) ⭐️ 6.8/10
7. [Cloudflare agents @cloudflare/codemode@0.5.2 released](#item-harness-arch-7) ⭐️ 6.8/10
8. [Hugging Face Speech-to-Speech: Modular Voice Agent Pipeline](#item-harness-arch-8) ⭐️ 5.0/10
9. [GitHub Trending: Letta Code](#item-harness-arch-9) ⭐️ 5.0/10

**AI Agent Engineer**
1. [Devin Fusion 发布](#item-agent-engineer-1) ⭐️ 8.8/10
2. [OpenRouter provider routing inconsistencies](#item-agent-engineer-2) ⭐️ 6.0/10
3. [Don&\#x27;t sleep on wrapture](#item-agent-engineer-3) ⭐️ 6.0/10

**AI Daily**
1. [OpenAI Scales Storage for 1 Billion ChatGPT Users](#item-ai-daily-1) ⭐️ 9.8/10
2. [Cognition Helps Devin Test Its Own Work with GPT-6 Astra](#item-ai-daily-2) ⭐️ 7.8/10
3. [GitHub Blog: Marketing Ops as Code](#item-ai-daily-3) ⭐️ 5.8/10

**AI Deals**
1. [Epic Games Free Games Sept 11-17](#item-ai-deals-1) ⭐️ 6.0/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [Cloudflare Agents agents@0.23.0 发布](https://github.com/cloudflare/agents/releases/tag/agents%400.23.0) ⭐️ 8.8/10

Cloudflare Agents 0.23.0 refactors sub-agent \(facet\) machinery into dynamic-agents capability facade, repositioning it as isolation primitive rather than multi-chat modeling. The ~2400 LOC of facet routing, WebSocket forwarding, and registry are extracted into a dedicated module registered as Lifecycle capability with id &quot;dynamic-agents&quot;. Added this.dynamicAgents facade with get, abort, delete, has, list methods. SubAgentClass and SubAgentStub remain as compatibility aliases. No wire- or storage-visible identifier changes.

github · github-actions\[bot\] · Sep 11, 10:42

**「设计要点」** The facet machinery is now a Lifecycle capability with capabilityId &quot;dynamic-agents&quot;. Hot paths stay composition-root wired since the capability-runner hook contract can&\#x27;t express request-rewrite-and-continue or post-claim WebSocket forwarding. No wire- or storage-visible identifier changes.

**「改了什么」** Refactored sub-agent \(facet\) machinery into dynamic-agents module and added this.dynamicAgents facade, repositioning facets as isolation primitive. Introduced Lifecycle-owned durable job queue and RoutedAgents capability for user hub with one Durable Object per chat.

**Tags**: `#runtime`, `#subagents`, `#dynamic-agents`, `#capability`, `#facets`

---

<a id="item-harness-arch-2"></a>
### [Cloudflare agents @0.12.0 release](https://github.com/cloudflare/agents/releases/tag/%40cloudflare/ai-chat%400.12.0) ⭐️ 8.8/10

Cloudflare agents @0.12.0 updates AIChatAgent message storage to use sessions with migration from legacy table and runtime behavior changes. Migration on first wake, no rollback. this.messages is empty until onStart. HydrationByteBudget bounds wake-time hydration. Streams use mutable rollover blocks for chunk logging with atomic cutover.

github · github-actions\[bot\] · Sep 11, 10:42

**「Design points」** Uses Durable Objects for sessions and streams with SQLite for message and chunk storage. Recovery continuations run as chained Tasks instead of schedule rows.

**「What changed」** Migrates AIChatAgent messages to sessions with first-wake import and drops legacy table after import. Constructor behavior changes so this.messages is empty until onStart. Stream chunk logging uses mutable rollover blocks with atomic settlement. Recovery continuations run as chained Tasks.

**Tags**: `#runtime`, `#memory`, `#sessions`, `#migration`

---

<a id="item-harness-arch-3"></a>
### [DSPy 3.4.0b1 发布](https://github.com/stanfordnlp/dspy/releases/tag/3.4.0b1) ⭐️ 8.8/10

DSPy 3.4.0b1 is the first beta of 3.4. It moves language-model execution to a shared engine interface, adds a local CPython interpreter for trusted code, brings async execution to ReActV2, and fixes evaluation, streaming, and demonstration-sampling bugs. This is a prerelease, not the stable 3.4.0 release. APIs and behavior may change. Install explicitly with \`pip install --upgrade &quot;dspy==3.4.0b1&quot;\`.

github · isaacbmiller · Sep 11, 22:24

**「设计要点」** DSPy uses shared LM engine interface with lm15 request, response, and streaming types. Custom engines implement complete\(request\) -&gt; response. LocalInterpreter runs generated Python in persistent CPython subprocess.

**「改了什么」** Experimental 3.3 LM types are replaced with lm15. ReActV2 gains async support for await agent.acall. GEPA adds custom code proposers. Evaluation is fixed to align outputs and scores on crashes.

**「评论」** No community comments available.

**Tags**: `#runtime`, `#sandbox`, `#eval`, `#tools`, `#planning`

---

<a id="item-harness-arch-4"></a>
### [Mastra @mastra/core@1.66.0 发布](https://github.com/mastra-ai/mastra/releases/tag/%40mastra/core%401.66.0) ⭐️ 7.8/10

Mastra releases @mastra/core 1.66.0. The update enables deploy-scoped worker provisioning for Mastra Cloud using a versioned workers.json manifest when shared storage and PubSub are configured. It adds advanced trace queries with predicates for span fields, metadata, feedback, and scores. Observability now supports deletion of feedback and scores.

github · PaulieScanlon · Sep 11, 09:37

**「设计要点」** Runtime worker configuration is exposed via Mastra.getWorkerConfig\(\) to allow deployment tools to compare live topology against build-time manifests. Observational memory adds async transform hooks for beforeObservation, afterObservation, beforeReflection, and afterReflection.

**「改了什么」** This release adds support for static emission of versioned workers.json manifests to provision dedicated orchestration workers. It introduces richer filtering predicates in trace queries for feedback and scores, along with batch delete operations for observability signals.

**Tags**: `#runtime`, `#eval`, `#storage`

---

<a id="item-harness-arch-5"></a>
### [Microsoft Agent Framework .NET 1.21.0 Released](https://github.com/microsoft/agent-framework/releases/tag/dotnet-1.21.0) ⭐️ 7.8/10

Microsoft Agent Framework .NET 1.21.0 is released. The release details protocol \(A2A\) and runtime changes including breaking file-access updates. It also updates Azure AI Projects to 3.0 beta, replaces AWS Bedrock SDK, and includes multiple dependency bumps.

github · SergeyMenshykh · Sep 11, 17:31

**「What Changed」** Breaking changes include file access contract updates, A2A run mode clarification, and MCP skill archive format restriction to ZIP. New runtime features add A2A task state tracking, LocalCodeAct subprocess isolation, and Azure AI Projects 3.0 support.

**Tags**: `#mcp`, `#runtime`, `#breaking`, `#tools`, `#azure`

---

<a id="item-harness-arch-6"></a>
### [Claude Code v2.1.269 发布](https://github.com/anthropics/claude-code/releases/tag/v2.1.269) ⭐️ 6.8/10

Claude Code v2.1.269 is released. It adds a plugin eval suite for running and scoring plugin tests, support for switching output styles, Bash tool diffs for file edits, OTEL metrics with repository tagging, and Workflow tool concurrency controls. The release also includes multiple bug fixes for terminal interactions, prompt caching, session resuming, and plugin handling.

github · ashwin-ant · Sep 11, 19:17

**「改了什么」** This release adds the plugin eval suite, output style switching, Bash tool diffs, OTEL metrics, and Workflow tool concurrency controls. It fixes several issues with terminals, caching, and session resuming.

**Tags**: `#eval`, `#tools`, `#subagents`, `#runtime`

---

<a id="item-harness-arch-7"></a>
### [Cloudflare agents @cloudflare/codemode@0.5.2 released](https://github.com/cloudflare/agents/releases/tag/%40cloudflare/codemode%400.5.2) ⭐️ 6.8/10

Cloudflare agents @cloudflare/codemode@0.5.2 released.

Improved in-place structural truncation of oversized tool results \(strings/arrays/objects\) to preserve valid JSON shape and reduce model token waste.

truncateResult \(default transformResult in execute/browser tools\) and codeMcpServer/openApiMcpServer response paths now shrink oversized values in place.

The output is always valid JSON of the original shape.

github · github-actions\[bot\] · Sep 11, 10:42

**「Design notes」** Truncation is applied structurally in tool execution paths for execute and browser tools and in MCP server response paths.

The Code Mode tool uses toModelOutput to project calls out of the model&\#x27;s context and bounds sandbox logs the same way results are bounded.

Durable call logs remain on the persisted tool part for UIs and audit.

**「What changed」** Truncate structured results structurally instead of slicing their JSON.

Arrays keep leading items and end with a truncation element; objects lose entries \(largest first\) with a placeholder; strings append a suffix.

**Tags**: `#runtime`, `#tools`, `#mcp`

---

<a id="item-harness-arch-8"></a>
### [Hugging Face Speech-to-Speech: Modular Voice Agent Pipeline](https://github.com/huggingface/speech-to-speech) ⭐️ 5.0/10

Hugging Face&\#x27;s speech-to-speech provides a low-latency, fully modular voice-agent pipeline. It chains VAD -&gt; STT -&gt; LLM -&gt; TTS and exposes OpenAI Realtime GA events over WebSocket and WebRTC. Components are swappable, with the LLM supporting OpenAI-compatible protocols for hosted providers, HF Inference, vLLM, or llama.cpp.

rss · GitHub Trending Daily · Sep 12, 00:50

**「Design Points」** The pipeline exposes OpenAI Realtime GA events over WebSocket and WebRTC. Every component is swappable including the LLM slot for different providers.

**Tags**: `#runtime`, `#tools`, `#subagents`

---

<a id="item-harness-arch-9"></a>
### [GitHub Trending: Letta Code](https://github.com/letta-ai/letta-code) ⭐️ 5.0/10

Letta Code is a stateful agent harness for creating agents that are more like people than tools. Letta Code agents have memory, identity, and a sense of experience over time. They learn and evolve over long horizons through rewriting their own memory, skills, prompts, and even the harness itself through mods. Letta Code can be used interactively or to power autonomous agents.

rss · GitHub Trending Daily · Sep 12, 00:50

**Tags**: `#memory`, `#runtime`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [Devin Fusion 发布](https://cognition.ai/blog/local-fusion) ⭐️ 8.8/10

Cognition 推出 Fusion 双模型 harness，用于 Devin Desktop 和 CLI。Fusion 将前沿模型作为 lead 进行规划和审查，搭配成本较低的 sidekick 执行。Fusion 在主要 coding benchmarks 上比其他 harness 更高效，最高可达 39%。与 Artificial Analysis 和 Vals AI 合作验证，Fusion 在 DeepSWE 1.1 等基准上可节省高达 46% 成本，同时维持前沿性能。影响 Devin 用户，通过安装 Devin CLI 可尝试 Fusion harness，降低 coding agent 成本。

rss · Cognition Blog · Sep 11, 17:00

**「为什么重要」** Fusion 已验证在多个基准上降低成本并维持性能。影响当前使用 Devin 的开发者。

**「可关注」** 可关注：使用更昂贵的模型作为 lead 或 sidekick 可能使整个系统更便宜，因为 frontier 模型 token 效率更高，且减少了 lead 和 sidekick 之间的来回工作。

**Tags**: `#harness`, `#eval`, `#coding-agent`, `#orchestration`

---

<a id="item-agent-engineer-2"></a>
### [OpenRouter provider routing inconsistencies](https://simonwillison.net/2026/Sep/11/so-you-want-to-use-openrouter/) ⭐️ 6.0/10

Simon Willison highlights OpenRouter&\#x27;s automatic fallback and provider selection, which picks the most cost-effective option for each request. Different providers run different serving software with varying optimizations and settings, so the same OpenRouter endpoint can serve model requests that behave differently. Some providers lack vision capability for vision models, and the reasoning effort option is processed differently. To control the routed provider, use the provider.only option. The /endpoints method returns the list of available providers for a specific model ID.

rss · Simon Willison · Sep 11, 22:49

**「Why it matters」** This matters for agent orchestration and eval harness reliability because inconsistent routing can affect model behavior consistency.

**「Engineer takeaway」** Use the provider.only option to explicitly select a provider for consistent model behavior.

**Tags**: `#orchestration`, `#coding-agent`, `#eval`, `#provider-routing`, `#harness`

---

<a id="item-agent-engineer-3"></a>
### [Don&\#x27;t sleep on wrapture](https://simonwillison.net/2026/Sep/11/wrapture/) ⭐️ 6.0/10

Graham Dumpleton&\#x27;s wrapture package enables monkey patching for both testing like unittest.mock and New Relic-style observability tracing. Simon Willison recommends it after seeing daily tutorials since the August 31 release. Wrapture is still alpha software but already very usable, especially when configured via TOML without modifying any Python code.

rss · Simon Willison · Sep 11, 13:51

**「为什么重要」** Wrapture combines testing and tracing in one tool and supports configuration via TOML with no code changes. This could simplify development for Python applications needing both.

**「可关注」** 可关注： Configure wrapture using a TOML file to enable tracing without modifying application code.

**Tags**: `#harness`, `#observability`, `#coding-agent`, `#eval`, `#testing`

---

## AI Daily

<a id="item-ai-daily-1"></a>
### [OpenAI Scales Storage for 1 Billion ChatGPT Users](https://openai.com/index/scaling-storage-one-billion-users-part-one) ⭐️ 9.8/10

OpenAI evolved the Habitat library from a Python library into a globally distributed storage platform. This platform serves over 1 billion ChatGPT users and processes 22 million requests per second.

rss · OpenAI Blog · Sep 11, 10:00

**「Why It Matters」** Scaling storage infrastructure to support 1 billion users at 22M requests per second is essential for ChatGPT&\#x27;s performance and availability.

**「Key Takeaway」** Key takeaway: Habitat library evolved into a globally distributed storage platform serving 1 billion users and 22M requests per second.

**Tags**: `#openai`, `#chatgpt`, `#infrastructure`, `#storage`, `#scaling`

---

<a id="item-ai-daily-2"></a>
### [Cognition Helps Devin Test Its Own Work with GPT-6 Astra](https://openai.com/index/cognition-devin-testing-with-astra) ⭐️ 7.8/10

GPT-6 Astra improves Devin’s ability to test software and show that it works. The goal is to help engineers review less code and ship more.

rss · OpenAI Blog · Sep 11, 16:00

**「Why It Matters」** This helps engineers review less code and ship more.

**「Key Takeaway」** Key Takeaway: Devin can test its own work with GPT-6 Astra.

**Tags**: `#model`, `#lab`, `#product`

---

<a id="item-ai-daily-3"></a>
### [GitHub Blog: Marketing Ops as Code](https://github.blog/ai-and-ml/github-copilot/marketing-ops-as-code-automating-events-from-planning-to-follow-up-on-github/) ⭐️ 5.8/10

GitHub blog post describes how the APAC marketing team automated events from planning to follow-up using GitHub tools. The team documented their work processes to enable automation of the entire event lifecycle. This case study shows the use of code in marketing operations.

rss · GitHub Blog · Sep 11, 18:26

**Tags**: `#product`, `#github`, `#copilot`, `#marketing`, `#automation`

---

## AI Deals

<a id="item-ai-deals-1"></a>
### [Epic Games Free Games Sept 11-17](https://www.appinn.com/eggs-26911/) ⭐️ 6.0/10

Epic Games is distributing LUFTRAUSERS, Astral Ascent, and Alone With You for free from September 11 to 17. The PC games are LUFTRAUSERS \(天空奇兵\) and Astral Ascent \(星界战士\), and the mobile game is Alone With You. The giveaway runs from September 11 to 17.

rss · 小众软件 · Sep 11, 07:48

**Tags**: `#promo`, `#limited-free`, `#free-game`

---