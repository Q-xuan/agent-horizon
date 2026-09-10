---
layout: default
title: "Horizon Summary: 2026-09-10 (EN)"
date: 2026-09-10
lang: en
---

> From 154 items, 14 important content pieces were selected

---

**Agent Harness Architecture**
1. [vLLM v0.29.0 发布](#item-harness-arch-1) ⭐️ 9.8/10
2. [openai/codex rust-v0.154.0 release](#item-harness-arch-2) ⭐️ 7.8/10
3. [Cline Desktop v0.0.24 Released](#item-harness-arch-3) ⭐️ 7.8/10
4. [Mastra @mastra/core@1.65.0 发布](#item-harness-arch-4) ⭐️ 7.8/10
5. [mem0 releases pi-agent-v0.3.0](#item-harness-arch-5) ⭐️ 7.8/10
6. [mem0ai/mem0 deepseek-plugin-v0.3.0 发布](#item-harness-arch-6) ⭐️ 7.8/10
7. [OpenHands v1.17.0 Release](#item-harness-arch-7) ⭐️ 6.8/10

**AI Agent Engineer**
1. [GPT-6 Astra Looped Transformers Hidden Reasoning](#item-agent-engineer-1) ⭐️ 7.0/10
2. [IBM Releases SOTA Granite Time Series PatchTST-FM-r2](#item-agent-engineer-2) ⭐️ 5.8/10

**AI Daily**
1. [OpenAI: The AI Policy Window Is Open](#item-ai-daily-1) ⭐️ 5.8/10
2. [Paul Christiano Joins OpenAI Foundation Board](#item-ai-daily-2) ⭐️ 5.8/10
3. [LWiAI Podcast \#256: Fable 5.1, OpenAI Cyber Model, Rogue Incident](#item-ai-daily-3) ⭐️ 5.0/10

**AI Deals**
1. [Fudan Academic Codex Client Goes Live with 10k Points and 80% Off](#item-ai-deals-1) ⭐️ 7.0/10
2. [DeepSeek V4-Flash Price Cut After 24-Day Hike](#item-ai-deals-2) ⭐️ 7.0/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [vLLM v0.29.0 发布](https://github.com/vllm-project/vllm/releases/tag/v0.29.0) ⭐️ 9.8/10

vLLM v0.29.0 is released with Model Runner V2 as the default inference engine for all models. Major runtime and memory optimizations include CUDA graph memory profiling for KV cache auto-sizing, batch-sharded sampling that cuts per-step logits memory by 1/TP, prompt embeds support, and padded FULL cudagraph dispatch. New models added include Hy4-preview, Qwen3.8-Flash-Next, GraniteSWA, GraniteMoeSWA, NemotronH\_Omni\_Reasoning\_V3 with MTP, and Kimi K3 NVFP4 checkpoints. Breaking changes remove ten deprecated model architectures, migrate FlexOlmo, Olmo3 and Hunyuan V1/VL to the Transformers backend, remove PyAV video decoder backend, and deprecate python -m vllm.entrypoints.openai.api\_server in favor of vllm serve.

github · khluu · Sep 9, 08:54

**「设计要点」** Model Runner V2 is the default runtime engine with CUDA graph memory profiling for KV cache auto-sizing, batch-sharded sampling, padded FULL cudagraph dispatch for uniform decode under spec decode, and DP-sync skipping before EAGLE/MTP draft prefill.

**「改了什么」** Model Runner V2 is now the default for all models, completing the rollout that began with pooling models. New models added include Hy4-preview, Qwen3.8-Flash-Next, GraniteSWA and GraniteMoeSWA, NemotronH\_Omni\_Reasoning\_V3 with MTP, and Kimi K3 NVFP4 checkpoints. Breaking changes include removal of ten deprecated model architectures, migration of FlexOlmo, Olmo3 and Hunyuan V1/VL to the Transformers modeling backend, removal of PyAV video decoder backend, and deprecation of python -m vllm.entrypoints.openai.api\_server in favor of vllm serve.

**Tags**: `#runtime`, `#memory`, `#prefix-cache`

---

<a id="item-harness-arch-2"></a>
### [openai/codex rust-v0.154.0 release](https://github.com/openai/codex/releases/tag/rust-v0.154.0) ⭐️ 7.8/10

OpenAI Codex rust-v0.154.0 is released. It adds experimental worktree support for isolated checkouts and a background server for Windows sessions. GPT-6-Astra is now available in the model picker. Inline answering lets you ask questions while Codex continues working on the main draft.

github · github-actions\[bot\] · Sep 9, 22:35

**「What Changed」** Experimental worktree support allows creating isolated checkouts for new or forked sessions via --worktree or /worktree. Windows sessions share a background Codex server with daemon lifecycle commands and managed updates. Inline answering uses suggested choices or custom text without losing the main draft. GPT-6-Astra model is added to the picker and Bedrock catalogs.

**「Community Discussion」** No community comments available.

**Tags**: `#sandbox`, `#runtime`, `#tools`

---

<a id="item-harness-arch-3"></a>
### [Cline Desktop v0.0.24 Released](https://github.com/cline/cline/releases/tag/desktop-v0.0.24) ⭐️ 7.8/10

Cline Desktop v0.0.24 is released with fixes for streaming and session issues in the desktop app. The main technical change skips observer streams and manages stream counters to prevent text doubling and message drops in live chat. It also resolves queued prompt message vanishing, improves session history rendering for subagents, and adds custom Windows title bar support.

github · github-actions\[bot\] · Sep 9, 08:16

**「What Changed」** Relative to v0.0.23, this release changes live chat streaming to skip observer streams and manage counters, fixing text doubling and message drops. It also fixes queued prompt handling, session rendering for children, model selection for Cline Pass, and background process completion.

**Tags**: `#runtime`, `#tools`

---

<a id="item-harness-arch-4"></a>
### [Mastra @mastra/core@1.65.0 发布](https://github.com/mastra-ai/mastra/releases/tag/%40mastra/core%401.65.0) ⭐️ 7.8/10

Mastra @mastra/core 1.65.0 introduces a strict portable advanced trace query contract with predicates, pagination, server endpoints, and implementations in ClickHouse, DuckDB, and Postgres. It adds tenant-scoped trace deletion with cascade cleanup across spans, signals, experiments, and logs, limited to 1,000 traces per request. Workflow control-flow blocks now support optional id, description, and metadata for stable addressing in visual editors.

github · PaulieScanlon · Sep 9, 09:43

**「设计要点」** The advanced trace query contract provides a portable runtime interface with recursive predicates and deterministic cursor pagination, implemented across multiple storage backends for observability.

**「改了什么」** 1.65.0 adds the advanced trace query contract and tenant-scoped deletion API with cascade. It introduces metadata support for workflow control-flow blocks and agent channel action handlers. Breaking changes include removal of global rules object in factory and updated defineBoard phase requirements.

**Tags**: `#runtime`, `#planning`, `#memory`, `#permissions`

---

<a id="item-harness-arch-5"></a>
### [mem0 releases pi-agent-v0.3.0](https://github.com/mem0ai/mem0/releases/tag/pi-agent-v0.3.0) ⭐️ 7.8/10

mem0 releases pi-agent-v0.3.0. The release updates Pi agent extension integration, build process, and memory tool handling while removing select features. It reuses shared conversation preparation, memory formatting, project/session/global scope utilities, and telemetry while preserving Pi&\#x27;s native extension API and @mem0/pi-agent-plugin package name. Pi loads the built dist/entry.js extension instead of executing source TypeScript from an installed package. Builds also publish the library entry point and declarations.

github · kartik-mem0 · Sep 9, 14:40

**「What Changed」** pi-agent-v0.3.0 reuses shared conversation preparation, memory formatting, project/session/global scope utilities, and telemetry while preserving Pi&\#x27;s native extension API and @mem0/pi-agent-plugin package name. It loads the built dist/entry.js extension instead of executing source TypeScript from an installed package and publishes the library entry point and declarations. Dream consolidation and pin commands, skills, configuration, types, and exports are removed. Global memory tool scope requires selecting /mem0-scope global or configuring a global default first. Memory update and delete accept mem0:&lt;uuid&gt; and \[mem0:&lt;uuid&gt;\] citations displayed in tool results as well as raw IDs.

**Tags**: `#memory`, `#tools`, `#runtime`

---

<a id="item-harness-arch-6"></a>
### [mem0ai/mem0 deepseek-plugin-v0.3.0 发布](https://github.com/mem0ai/mem0/releases/tag/deepseek-plugin-v0.3.0) ⭐️ 7.8/10

Mem0 DeepSeek plugin v0.3.0 adds automatic memory recall during system-prompt/assemble and post-turn capture from durable session/event streams. autoRecall and autoCapture default to true. The plugin reuses shared Harness lifecycle, redaction, identity, and telemetry utilities while retaining explicit search\_memory and add\_memory tools.

github · kartik-mem0 · Sep 9, 14:36

**「设计要点」** The plugin reuses shared lifecycle utilities and publishes a self-contained ESM artifact under @mem0/deepseek-plugin. Native Harness services and the Mem0 SDK remain external dependencies. Cross-user userId overrides require operator opt-in with allowUserOverride: true.

**「改了什么」** v0.3.0 adds automatic memory recall during prompt assembly and post-turn capture from durable streams. It reuses shared Harness lifecycle utilities while retaining explicit search\_memory and add\_memory tools. The plugin publishes a self-contained ESM artifact under @mem0/deepseek-plugin with external dependencies.

**Tags**: `#memory`, `#runtime`, `#tools`, `#permissions`

---

<a id="item-harness-arch-7"></a>
### [OpenHands v1.17.0 Release](https://github.com/OpenHands/OpenHands/releases/tag/v1.17.0) ⭐️ 6.8/10

OpenHands v1.17.0 adds local Agent Canvas Planner support and UI enhancements for automation, cloud settings, and conversations. The automation UI is now task-outcome aware. Cloud LLM provider connections are enabled. Custom cron editing and conversation tags with filtering are added.

github · openhands-release-bot\[bot\] · Sep 9, 19:27

**「What changed」** Relative to v1.16.0, OpenHands v1.17.0 adds local Agent Canvas Planner support. It makes the automation UI task-outcome aware, enables cloud LLM provider connections, adds custom cron editing, and introduces conversation tags and filtering.

**Tags**: `#planning`, `#runtime`, `#tools`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [GPT-6 Astra Looped Transformers Hidden Reasoning](https://magazine.sebastianraschka.com/p/gpt-6-astra-looped-transformers-and) ⭐️ 7.0/10

Sebastian Raschka&\#x27;s blog post covers OpenAI&\#x27;s recent GPT-6 Astra release, noting its exceptional performance in benchmarks including 99.9% on ARC-AGI-3 and strong results in math, coding, and agentic tasks. The model demonstrates advanced computer-use capabilities through GUI interactions, such as controlling the mouse in MS Paint. The article examines looped transformers and their potential connection to hidden reasoning mechanisms in the model.

rss · Sebastian Raschka · Sep 9, 11:14 · [Discussion](https://news.ycombinator.com/item?id=49627370)

**「为什么重要」** These details on Astra&\#x27;s capabilities and training methods using Mac hardware for RL on macOS are relevant for AI agent engineers working on coding agents and observability.

**「可关注」** 可关注：looped transformers may hide reasoning traces by feeding model outputs back as input, reusing weights to save memory.

**「评论」** Comments from the community note that looped transformers equate to deeper layers via weight reuse, referencing papers on CoT and universal transformers. Users describe Astra&\#x27;s performance as inconsistent and praise the real-time computer use demos.

**Tags**: `#eval`, `#orchestration`, `#memory`, `#coding-agent`, `#observability`

---

<a id="item-agent-engineer-2"></a>
### [IBM Releases SOTA Granite Time Series PatchTST-FM-r2](https://huggingface.co/blog/ibm-research/ibm-releases-sota-granite-time-series) ⭐️ 5.8/10

IBM has released Granite Time Series PatchTST-FM-r2, a state-of-the-art zero-shot time series foundation model. The ~385M-parameter model uses an updated conformer-based architecture with overlapping patches, a larger pretraining corpus, probabilistic forecasting, and imputation support. It ranks \#2 on the GIFT-Eval leaderboard for replicable zero-shot models and is available under Apache 2.0 and OpenMDW 1.0 licenses.

rss · Hugging Face Blog · Sep 9, 15:36

**「Why It Matters」** PatchTST-FM-r2 is the highest-performing model in the replicable zero-shot category among those with permissive, commercial-friendly licensing on GIFT-Eval.

**「Takeaway」** The model uses conformer blocks with alternating convolution kernel sizes of 3 and 5 to capture long- and short-range temporal structure while supporting contexts up to 8,192 steps.

**Tags**: `#eval`, `#orchestration`, `#foundation-model`, `#harness`

---

## AI Daily

<a id="item-ai-daily-1"></a>
### [OpenAI: The AI Policy Window Is Open](https://openai.com/index/ai-policy-window) ⭐️ 5.8/10

Chris Lehane argues that stronger AI capabilities require stronger safety evidence, shared standards, and durable policy action while the policy window remains open.

rss · OpenAI Blog · Sep 9, 13:00

**「Why It Matters」** The post calls for stronger safety evidence, shared standards, and durable policy to support advancing AI capabilities while the window remains open.

**「Engineer Takeaway」** Key Takeaway: Stronger AI capabilities require stronger safety evidence, shared standards, and durable policy action.

**Tags**: `#policy`, `#openai`, `#safety`

---

<a id="item-ai-daily-2"></a>
### [Paul Christiano Joins OpenAI Foundation Board](https://openai.com/index/paul-christiano-joins-openai-foundation-board) ⭐️ 5.8/10

Paul Christiano joins the OpenAI Foundation Board and its Safety and Security Committee. He brings experience in AI alignment, safety, and standards.

rss · OpenAI Blog · Sep 9, 17:00

**「Key Takeaway」** Key Takeaway: Paul Christiano brings experience in AI alignment, safety, and standards.

**Tags**: `#openai`, `#board`, `#safety`, `#alignment`, `#policy`

---

<a id="item-ai-daily-3"></a>
### [LWiAI Podcast \#256: Fable 5.1, OpenAI Cyber Model, Rogue Incident](https://lastweekin.ai/p/lwiai-podcast-256-fable-51-astra) ⭐️ 5.0/10

Last Week in AI Podcast \#256 covers Anthropic launching Claude Fable 5.1. It also covers OpenAI&\#x27;s first AI model with critical cyber abilities, which is about to be released. The podcast discusses how the OpenAI rogue AI model incident was worse than we thought.

rss · Last Week in AI · Sep 9, 08:01

**Tags**: `#model`, `#anthropic`, `#openai`, `#industry`

---

## AI Deals

<a id="item-ai-deals-1"></a>
### [Fudan Academic Codex Client Goes Live with 10k Points and 80% Off](https://www.appinn.com/qiewenpaper-codex-2/) ⭐️ 7.0/10

Fudan University NLP team has launched the academic version of the Codex client. New users can download and log in to get 10,000 points, and enjoy 80% off membership. This allows researchers to use AI to assist in research tasks such as environment setup, running experiments, code reproduction, literature search, and writing reviews.

rss · 小众软件 · Sep 9, 08:31

**「Engineer takeaway」** Engineer takeaway: The academic Codex client is for researchers to use AI to assist in research tasks.

**Tags**: `#credits`, `#promo`, `#api`, `#limited-free`

---

<a id="item-ai-deals-2"></a>
### [DeepSeek V4-Flash Price Cut After 24-Day Hike](https://www.appinn.com/deepseek-flash-price-cut-24-days-after-price-hike/) ⭐️ 7.0/10

DeepSeek team member @Tianyi Cui announced that V4.1 Flash model surpasses V4 Pro in performance, cost, speed, and total usage. After a 24-day price increase, they cut V4-Flash pricing and redirected V4-Pro to V4.1 Flash. This change is directly actionable for API users with no expiration or binding details given.

rss · 小众软件 · Sep 9, 07:05

**「Why It Matters」** Users can now access better model performance at lower cost after the recent price hike.

**「Takeaway」** V4-Pro is now redirected to V4.1 Flash, which outperforms in all metrics including performance, cost, speed, and total usage.

**Tags**: `#promo`, `#api`, `#price-cut`, `#model-update`

---