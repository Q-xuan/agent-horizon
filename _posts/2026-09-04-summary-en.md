---
layout: default
title: "Horizon Summary: 2026-09-04 (EN)"
date: 2026-09-04
lang: en
---

> From 168 items, 15 important content pieces were selected

---

**Agent Harness Architecture**
1. [Claude Code v2.1.260 released](#item-harness-arch-1) ⭐️ 7.8/10
2. [Cline desktop v0.0.23 released](#item-harness-arch-2) ⭐️ 7.8/10
3. [pydantic-ai v2.38.0 released](#item-harness-arch-3) ⭐️ 7.8/10
4. [Microsoft Agent Framework python-1.17.0 发布](#item-harness-arch-4) ⭐️ 7.8/10
5. [Cline desktop-v0.0.23-beta.1 发布](#item-harness-arch-5) ⭐️ 6.8/10
6. [Codex rust-v0.153.1 released](#item-harness-arch-6) ⭐️ 5.8/10
7. [Codex rust-v0.153.0 发布](#item-harness-arch-7) ⭐️ 5.8/10

**AI Agent Engineer**
1. [NeoMME: Efficient Multilingual Multimodal Encoder](#item-agent-engineer-1) ⭐️ 7.8/10
2. [GPT-6 Astra Rolls Out with 99.9% ARC-AGI 3 Score](#item-agent-engineer-2) ⭐️ 7.0/10

**AI Daily**
1. [OpenAI Introduces Daybreak $1B for Frontline Defenders](#item-ai-daily-1) ⭐️ 7.8/10
2. [ZGateway: Proxy for Meta&\#x27;s ZippyDB](#item-ai-daily-2) ⭐️ 7.8/10
3. [Legora Reviews 41 Documents with GPT-6 Astra](#item-ai-daily-3) ⭐️ 6.8/10
4. [Playco Cuts Manual Fixes 50% with GPT-6 Astra](#item-ai-daily-4) ⭐️ 6.8/10
5. [GitHub Copilot: Run Several Agents at Once](#item-ai-daily-5) ⭐️ 5.8/10

**AI Deals**
1. [CloudCone SSD VPS Turns 9 Sale Restock 96 RMB/Year](#item-ai-deals-1) ⭐️ 7.0/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [Claude Code v2.1.260 released](https://github.com/anthropics/claude-code/releases/tag/v2.1.260) ⭐️ 7.8/10

Claude Code v2.1.260 is released. It adds a diff panel that opens beside the conversation and shows uncommitted changes as Claude edits. It also provides explanations for prompt cache misses in the status line and adds /reload-plugins support for headless sessions. Additional changes include text commands for the advisor feature, OIDC configuration updates, and desktop policy key improvements.

github · ashwin-ant · Sep 3, 23:48

**「What changed」** v2.1.260 adds a diff panel, prompt cache miss explanations, and /reload-plugins support. It includes fixes for Bash permission rules, Bedrock credential calls, session management, model switching, and several other bugs.

**Tags**: `#memory`, `#permissions`, `#tools`, `#runtime`

---

<a id="item-harness-arch-2"></a>
### [Cline desktop v0.0.23 released](https://github.com/cline/cline/releases/tag/desktop-v0.0.23) ⭐️ 7.8/10

Cline desktop v0.0.23 integrates Agent Plugins with the shared Hub for discovery, validation, and execution. Plugins under ~/.agents/plugins are validated via plugin.json, their skills are made available, and MCP servers start automatically. Settings are separated for Agent Plugins and Cline Plugins, with Hub-managed controls. Build-mismatch dialogs are fixed.

github · github-actions\[bot\] · Sep 3, 18:33

**「Architecture Note」** The shared Hub now handles Agent Plugin discovery and execution. Valid plugins are validated from plugin.json, making Agent Skills available, and stdio/Streamable HTTP/SSE MCP servers auto-start. Agent Plugin settings are separate from Cline Plugins, with per-plugin enable/disable managed by the Hub. Workspace .agents/plugins directories are intentionally ignored.

**「Changes」** The &\#x27;Cline Hub was updated&\#x27; dialog no longer appears on every launch and reconnect. Signing in now shows the device confirmation code in the app for matching. Voice input failures caused by provider setup now take you to voice settings. Fixed the scheduled-task report vanishing when a finished run&\#x27;s step collapsed and one wedged MCP server blocking the rest from shutting down.

**「Comments」** No community comments available.

**Tags**: `#mcp`, `#tools`, `#runtime`, `#plugins`, `#hub`

---

<a id="item-harness-arch-3"></a>
### [pydantic-ai v2.38.0 released](https://github.com/pydantic/pydantic-ai/releases/tag/v2.38.0) ⭐️ 7.8/10

Pydantic AI v2.38.0 is released. It adds runtime event system enhancements for custom and capability events, context window metrics, model profile updates, and support for new Claude/Gemini models.

github · adtyavrdhn · Sep 3, 07:48

**「What changed」** v2.38.0 adds typed event emission and subscription for CustomEvent and CapabilityEvent using @on\_event. It introduces context\_window to ModelProfile and context\_window\_used to RunContext, along with support for new models including gemini-3.8-flash, claude-fable-5-1, claude-mythos-5-1, and VLLMProvider.

**Tags**: `#runtime`, `#events`, `#memory`, `#models`, `#capabilities`

---

<a id="item-harness-arch-4"></a>
### [Microsoft Agent Framework python-1.17.0 发布](https://github.com/microsoft/agent-framework/releases/tag/python-1.17.0) ⭐️ 7.8/10

Microsoft Agent Framework Python 1.17.0 is released. It introduces runtime middleware updates, Foundry hosting improvements, and a Telegram agent sample. Breaking changes restore sequence-only agent middleware inputs and remove the experimental agent-hooks core extra. OpenAI SDK 3.x support and same-event-loop concurrency contract documentation are added.

github · moonbox3 · Sep 3, 09:49

**「设计要点」** Agent middleware inputs are restricted to sequence-only format. Experimental hooks are removed from core. Same-event-loop concurrency contract is documented for shared chat clients.

**「改了什么」** Relative to 1.16.0, sequence-only agent middleware inputs are restored and experimental agent-hooks core extra is removed. OpenAI SDK 3.x support is added, Mistral clients are migrated to official SDK, and a new end-to-end Foundry-hosted Telegram agent sample is included.

**Tags**: `#runtime`, `#tools`, `#memory`

---

<a id="item-harness-arch-5"></a>
### [Cline desktop-v0.0.23-beta.1 发布](https://github.com/cline/cline/releases/tag/desktop-v0.0.23-beta.1) ⭐️ 6.8/10

Cline desktop-v0.0.23-beta.1 adds opt-in image generation and groups scheduled runs by local vs SSH runtime environment. This is the official Cline desktop GitHub Release with incremental harness changes: opt-in image-generation tool \(server-side credentials, images kept in session history\) and schedule grouping scoped by local vs SSH runtime.

github · github-actions\[bot\] · Sep 3, 01:46

**「设计要点」** Image generation is opt-in with server-side credentials and images stored in session history. Scheduled runs are grouped within their runtime environment to keep local and SSH schedules separate.

**「改了什么」** Adds opt-in image generation under Customize → Tools. Groups scheduled runs within their runtime environment so similarly named local and SSH schedules stay separate.

**「评论」** No community comments available.

**Tags**: `#tools`, `#runtime`, `#memory`

---

<a id="item-harness-arch-6"></a>
### [Codex rust-v0.153.1 released](https://github.com/openai/codex/releases/tag/rust-v0.153.1) ⭐️ 5.8/10

Codex rust-v0.153.1 released. Added support for configuring GPT-6-Astra through the API without changing the default model or showing it in the model picker. This backports the GPT-6-Astra model catalog to 0.153.

github · github-actions\[bot\] · Sep 3, 21:02

**「What changed」** Added support for configuring GPT-6-Astra through the API without changing the default model or showing it in the model picker.

**Tags**: `#tools`, `#planning`, `#memory`

---

<a id="item-harness-arch-7"></a>
### [Codex rust-v0.153.0 发布](https://github.com/openai/codex/releases/tag/rust-v0.153.0) ⭐️ 5.8/10

Codex Rust v0.153.0 release adds Vim mode support with undo and redo in the TUI composer. The plugin CLI allows listing, installing, and removing plugins from remote marketplaces. TUI history enhancements show complete patches and individual commands. Additional features include disabling automatic recaps and experimental context management.

github · github-actions\[bot\] · Sep 3, 01:37

**「改了什么」** This release adds Vim undo/redo support, plugin CLI for marketplace management, and TUI history tracking improvements. It also includes fixes for TUI reconnection and Guardian review history preservation.

**Tags**: `#tools`, `#runtime`, `#memory`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [NeoMME: Efficient Multilingual Multimodal Encoder](https://huggingface.co/blog/Hcompany/neomme) ⭐️ 7.8/10

NeoMME is a family of 260M and 800M multilingual multimodal encoders. It uses a single bidirectional Transformer to process text tokens and raw image patches, trained from scratch with a masked discrete-diffusion objective. Fine-tuned for visual document retrieval via ColPali&\#x27;s page-image approach, NeoMME-Retriever returns dense and late-interaction embeddings in one forward pass. On ViDoRe v3, the 260M model reaches 0.523 nDCG@10 \(within 0.002 of ColQwen2.5\) at 51 pages/sec throughput and enables 255x storage reduction for late-interaction indexes.

rss · Hugging Face Blog · Sep 3, 13:13

**「Why it matters」** The architecture eliminates separate vision towers and causal decoders, directly benefiting eval harnesses and multimodal toolchains by lowering parameter and compute overhead while maintaining Pareto frontier performance on document retrieval.

**「Engineer takeaway」** Observe: Hierarchical token pooling and asymmetric quantization reduce late-interaction index storage from roughly 1.5 MB to 6 kB per page \(255× smaller\) while retaining more than 95% of baseline nDCG@10.

**Tags**: `#eval`, `#harness`, `#orchestration`, `#efficiency`, `#retrieval`

---

<a id="item-agent-engineer-2"></a>
### [GPT-6 Astra Rolls Out with 99.9% ARC-AGI 3 Score](https://simonwillison.net/2026/Sep/3/gpt6-astra/) ⭐️ 7.0/10

GPT-6 Astra is rolling out to a limited set of organizations and will become available to all ChatGPT Plus, Pro, Business, and Enterprise users as well as the OpenAI API and AWS. It is priced at $10 per million input tokens and $50 per million output tokens, matching Claude Fable 5. The model scores 99.9% on ARC-AGI 3 using OpenAI&\#x27;s custom Provider Adapter harness that preserves opaque reasoning state between requests and uses compaction for longer conversations.

rss · Simon Willison · Sep 3, 20:18

**「Why It Matters」** The rollout and pricing details are now public, enabling users to plan integrations and cost modeling. The 99.9% ARC-AGI 3 score is confirmed with the custom harness, though the default harness scored 62.7% for $26K.

**「Engineer Takeaway」** Note: The Provider Adapter harness preserves opaque reasoning state between requests and uses compaction for longer conversations, enabling the 99.9% ARC-AGI 3 score.

**「Community Discussion」** Hacker News comments debate whether the ARC-AGI 3 score is misleading due to the custom harness, as GPT-5.6 Sol would score around 30% under the same setup. Some users question if the closed-source model will open source in the future.

**Tags**: `#eval`, `#harness`, `#benchmark`, `#api-pricing`, `#model-release`

---

## AI Daily

<a id="item-ai-daily-1"></a>
### [OpenAI Introduces Daybreak $1B for Frontline Defenders](https://openai.com/index/daybreak-for-frontline-defenders) ⭐️ 7.8/10

OpenAI introduces Daybreak for Frontline Defenders. A $1 billion commitment expands access to frontier cyber AI, training, and support for essential services.

rss · OpenAI Blog · Sep 3, 13:15

**「Key takeaway」** Focus on: expanding access to frontier cyber AI, training, and support for essential services.

**Tags**: `#openai`, `#policy`, `#industry`, `#product`

---

<a id="item-ai-daily-2"></a>
### [ZGateway: Proxy for Meta&\#x27;s ZippyDB](https://engineering.fb.com/2026/09/03/core-infra/zgateway-proxy-zippydb-meta/) ⭐️ 7.8/10

Meta is introducing ZGateway, the proxy used to unify traffic through ZippyDB, its most widely used key-value store. This proxy adds admission control, load balancing, cross-region resilience, and richer operations as a bonus. ZippyDB serves billions of requests for product metadata, counters, and configuration.

rss · Engineering at Meta · Sep 3, 16:00

**「Why It Matters」** This proxy unifies traffic to a core internal service at massive scale, improving management and resilience.

**「Takeaway」** Takeaway: Proxies in front of key-value stores can provide admission control and cross-region resilience.

**Tags**: `#lab`, `#industry`, `#product`

---

<a id="item-ai-daily-3"></a>
### [Legora Reviews 41 Documents with GPT-6 Astra](https://openai.com/index/legora-financial-statement-review-with-astra) ⭐️ 6.8/10

Legora used GPT-6 Astra to review 41 financial documents in minutes. The system detected all four planted errors. Workflow performance improved by nearly 40%.

rss · OpenAI Blog · Sep 3, 12:00

**「Why it matters」** This case study shows GPT-6 Astra handling real financial document reviews with high accuracy.

**「Takeaway」** Watch: GPT-6 Astra reviewed 41 documents in minutes and detected all four planted errors.

**Tags**: `#model`, `#lab`, `#industry`, `#eval`, `#product`

---

<a id="item-ai-daily-4"></a>
### [Playco Cuts Manual Fixes 50% with GPT-6 Astra](https://openai.com/index/playco-game-prototyping-with-astra) ⭐️ 6.8/10

Playco used GPT-6 Astra to build three themed game prototypes from one grey box foundation. The team reported 50% fewer manual fixes than with the previous model.

rss · OpenAI Blog · Sep 3, 12:00

**「Why it matters」** This achievement highlights GPT-6 Astra&\#x27;s effectiveness in streamlining game prototyping by reducing manual fixes by half.

**「Engineer takeaway」** Playco reduced manual fixes by 50% with GPT-6 Astra when prototyping games from a grey box foundation.

**Tags**: `#model`, `#lab`, `#industry`, `#product`

---

<a id="item-ai-daily-5"></a>
### [GitHub Copilot: Run Several Agents at Once](https://github.blog/ai-and-ml/github-copilot/github-copilot-app-for-beginners-run-several-agents-at-once/) ⭐️ 5.8/10

The GitHub blog post explains how to run parallel agents in the Copilot app. The guide targets beginners. It describes running several agents at once to make the app feel more powerful. No specific technical details, comparisons, or metrics are provided.

rss · GitHub Blog · Sep 3, 16:00

**「Why it matters」** The post helps beginners understand and use multiple agents in the Copilot app.

**「Takeaway」** Takeaway: Run several agents at once in the Copilot app.

**Tags**: `#github`, `#copilot`, `#agents`, `#product`, `#ai`

---

## AI Deals

<a id="item-ai-deals-1"></a>
### [CloudCone SSD VPS Turns 9 Sale Restock 96 RMB/Year](https://www.appinn.com/cloudcone-ssd-vps/) ⭐️ 7.0/10

CloudCone SSD VPS restock promotion for Turns 9 Sale offers 96 RMB per year with Alipay support. Recommended packages include 1 IPv4 and 3 IPv6. Purchase through the provided links in the email.

rss · 小众软件 · Sep 3, 09:07

**「Takeaway」** Takeaway: Recommended packages include 1 IPv4 + 3 IPv6 with Alipay support. Suitable for users requiring IPv6 addresses.

**Tags**: `#promo`, `#coupon`, `#sale`

---