---
layout: default
title: "Horizon Summary: 2026-09-10 (EN)"
date: 2026-09-10
lang: en
---

> From 193 items, 16 important content pieces were selected

---

**Agent Harness Architecture**
1. [mem0 openclaw-v1.1.0 Released](#item-harness-arch-1) ⭐️ 8.8/10
2. [vLLM v0.29.0 Released](#item-harness-arch-2) ⭐️ 8.8/10
3. [Codex rust-v0.154.0 发布](#item-harness-arch-3) ⭐️ 7.8/10
4. [pydantic-ai v2.42.0 released](#item-harness-arch-4) ⭐️ 7.8/10
5. [Mastra Core 1.65.0 Release](#item-harness-arch-5) ⭐️ 7.8/10
6. [Mem0 DeepSeek Plugin v0.3.0 Released](#item-harness-arch-6) ⭐️ 7.8/10
7. [mem0 opencode-v0.3.0 released](#item-harness-arch-7) ⭐️ 6.8/10
8. [browser-use/browser-use GitHub Trending](#item-harness-arch-8) ⭐️ 5.0/10
9. [GitHub trending: anomalyco/opencode](#item-harness-arch-9) ⭐️ 5.0/10

**AI Agent Engineer**
1. [Goodfire 使用 Ai2 开放后训练栈追踪模型行为](#item-agent-engineer-1) ⭐️ 5.8/10
2. [Devin Factors RSA-260](#item-agent-engineer-2) ⭐️ 5.8/10

**AI Daily**
1. [Paul Christiano Joins OpenAI Foundation Board](#item-ai-daily-1) ⭐️ 7.8/10
2. [OpenAI: The AI policy window is open. We need to act.](#item-ai-daily-2) ⭐️ 6.8/10
3. [LWiAI Podcast \#256: Fable 5.1, Cyber Abilities, Rogue AI](#item-ai-daily-3) ⭐️ 5.0/10

**AI Deals**
1. [Fudan Academic Codex Client: 10k Points + 20% Off](#item-ai-deals-1) ⭐️ 6.0/10
2. [DeepSeek V4-Flash Price Cut 24 Days After Hike](#item-ai-deals-2) ⭐️ 6.0/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [mem0 openclaw-v1.1.0 Released](https://github.com/mem0ai/mem0/releases/tag/openclaw-v1.1.0) ⭐️ 8.8/10

mem0 releases OpenClaw-v1.1.0. The release reuses core conversation handling while dropping Dream consolidation and updating message processing limits. It continues to publish a self-contained ESM package under @mem0/openclaw-mem0; the plugin manifest and package version now agree.

github · kartik-mem0 · Sep 9, 14:34

**「Design Notes」** OpenClaw-v1.1.0 reuses shared runtime components for conversation preparation, redaction, and telemetry. It retains native memory backend, tools, CLI, and Platform/OSS modes.

**「What Changed」** OpenClaw-v1.1.0 removes Dream consolidation: automatic scheduling and locking, \`openclaw mem0 dream\`, Dream configuration, the memory-dream skill, and Dream-state public artifacts. It removes OpenClaw&\#x27;s separate 2,000-character extraction cutoff and fixes the status command to handle unconfigured installations.

**Tags**: `#memory`, `#tools`, `#runtime`, `#cli`

---

<a id="item-harness-arch-2"></a>
### [vLLM v0.29.0 Released](https://github.com/vllm-project/vllm/releases/tag/v0.29.0) ⭐️ 8.8/10

vLLM v0.29.0 defaults to Model Runner V2 runtime with CUDA graph memory profiling for KV cache auto-sizing, batch-sharded sampling that cuts per-step logits memory by 1/TP, padded FULL cudagraph dispatch for uniform decode, and DP-sync skipping.
It supports new models including Hy4-preview, Qwen3.8-Flash-Next, GraniteSWA, GraniteMoeSWA, NemotronH\_Omni\_Reasoning\_V3, and Kimi K3 NVFP4 checkpoints.
Breaking changes remove ten deprecated model architectures, migrate FlexOlmo, Olmo3 and Hunyuan V1/VL to the Transformers modeling backend, and remove PyAV video decoder backend.

github · khluu · Sep 9, 08:54

**「Design notes」** Model Runner V2 is the default runtime.
It features CUDA graph memory reservation for KV cache auto-sizing and padded FULL cudagraph dispatch.

**「What changed」** Model Runner V2 becomes default for all models with CUDA graph memory profiling for KV cache auto-sizing, batch-sharded sampling, padded FULL cudagraph dispatch, and DP-sync skipping.
Breaking changes remove ten deprecated model architectures, migrate FlexOlmo, Olmo3 and Hunyuan V1/VL to the Transformers modeling backend, and remove PyAV video decoder backend.

**Tags**: `#runtime`, `#memory`, `#tools`

---

<a id="item-harness-arch-3"></a>
### [Codex rust-v0.154.0 发布](https://github.com/openai/codex/releases/tag/rust-v0.154.0) ⭐️ 7.8/10

OpenAI Codex rust-v0.154.0 is released with experimental worktree support for isolated checkouts and sessions, inline question answering while the main draft continues, Windows background server sharing with daemon lifecycle commands, Vim R replace mode with undo, and plugin tool refresh after external upgrades. GPT-6-Astra model is now available in the picker and Bedrock catalogs. Bug fixes cover MCP OAuth coordination, sandbox protections, and permission preservation in session operations.

github · github-actions\[bot\] · Sep 9, 22:35

**「改了什么」** From rust-v0.153.0, this release adds worktree-based isolated sessions, inline QA, Windows daemon sharing, and Vim replace mode. It also ensures plugin skills refresh after external changes and improves MCP connection handling for OAuth refreshes.

**Tags**: `#runtime`, `#tools`, `#sandbox`

---

<a id="item-harness-arch-4"></a>
### [pydantic-ai v2.42.0 released](https://github.com/pydantic/pydantic-ai/releases/tag/v2.42.0) ⭐️ 7.8/10

Pydantic-ai v2.42.0 is released. It adds GitHubCopilotProvider for GitHub Copilot&\#x27;s OpenAI-compatible API. The release includes a compatibility note for DeferredToolResults.approvals and bug fixes for BedrockConverseModel, $ref handling, ToolReturnContent validation, and Anthropic recovery.

github · dsfaccini · Sep 9, 03:33

**「What Changed」** Relative to v2.41.0, v2.42.0 adds the GitHubCopilotProvider feature and rejects invalid DeferredToolResults.approvals values. Bug fixes address anthropic\_disallows\_sampling\_settings in BedrockConverseModel, non-object $ref definitions in function signatures, ToolReturnContent validation, and Anthropic recovery across normalized history.

**Tags**: `#runtime`, `#tools`, `#permissions`, `#planning`

---

<a id="item-harness-arch-5"></a>
### [Mastra Core 1.65.0 Release](https://github.com/mastra-ai/mastra/releases/tag/%40mastra/core%401.65.0) ⭐️ 7.8/10

Mastra Core 1.65.0 release introduces a portable advanced trace query contract with bounded time ranges, recursive predicates, thread grouping, and deterministic cursor pagination. It adds tenant-scoped trace deletion with cascade cleanup across spans and linked signals, plus optional id, description, and metadata for workflow control-flow blocks. Agent channels now support custom onAction handlers for UI interactions.

github · PaulieScanlon · Sep 9, 09:43

**「What Changed」** Breaking changes in @mastra/factory require kind and role on working phases, remove the global rules object, and move tool-result rules onto defineBoard. The GET /web/factory/projects response shape changed with tier removal. TraceDataPanelView and TracesLayout updated in playground-ui.

**Tags**: `#runtime`, `#memory`, `#planning`, `#traces`, `#workflows`

---

<a id="item-harness-arch-6"></a>
### [Mem0 DeepSeek Plugin v0.3.0 Released](https://github.com/mem0ai/mem0/releases/tag/deepseek-plugin-v0.3.0) ⭐️ 7.8/10

Mem0 releases Harness DeepSeek plugin v0.3.0. The plugin adds automatic recall during system-prompt/assemble using the latest human prompt and automatic capture from the durable session/event stream after a completed turn, with autoRecall and autoCapture defaulting to true. It reuses shared lifecycle utilities while retaining explicit search\_memory and add\_memory tools with per-call agent or session scope. Cross-user userId overrides now require allowUserOverride: true.

github · kartik-mem0 · Sep 9, 14:36

**「Architecture note」** The plugin reuses shared lifecycle, redaction, identity, and telemetry utilities while retaining the explicit search\_memory and add\_memory tools and their per-call agent/session scope. Cross-user userId overrides now require operator opt-in with allowUserOverride: true. It publishes a self-contained ESM artifact under @mem0/deepseek-plugin; native Harness services and the Mem0 SDK remain external dependencies. Plugin cleanup remains tied to the native Cordis lifecycle.

**「What changed」** Added automatic recall during system-prompt/assemble using the latest human prompt and automatic capture from the durable session/event stream after a completed turn. The plugin reuses shared utilities while retaining explicit memory tools and requires allowUserOverride for cross-user userId changes.

**Tags**: `#memory`, `#tools`, `#runtime`, `#permissions`

---

<a id="item-harness-arch-7"></a>
### [mem0 opencode-v0.3.0 released](https://github.com/mem0ai/mem0/releases/tag/opencode-v0.3.0) ⭐️ 6.8/10

mem0 released opencode-v0.3.0 for its OpenCode plugin. The release moves source from integrations/mem0-plugin/.opencode-plugin/ to integrations/opencode-plugin/. It reuses shared conversation preparation, redaction, scoping, and telemetry. The plugin builds a self-contained Bun/ESM dist/index.js and publishes its TypeScript entry declaration. Global memory tool scope requires enablement in plugin settings and rejects empty identities.

github · kartik-mem0 · Sep 9, 14:38

**「Architecture note」** Global memory tool scope requires user enablement in plugin settings. Empty and wildcard identities are rejected. Reuses shared components for conversation prep, redaction, scoping, and telemetry. Produces self-contained Bun/ESM build.

**「What changed」** Changed source location and build paths. Enforced global memory tool scope with enablement requirement and rejected empty identities. Removed auto-Dream consolidation, its gates, state handling, Dream and pin skills/commands. Existing configurations using these features must be updated.

**Tags**: `#memory`, `#tools`, `#runtime`, `#permissions`

---

<a id="item-harness-arch-8"></a>
### [browser-use/browser-use GitHub Trending](https://github.com/browser-use/browser-use) ⭐️ 5.0/10

Browser-use is an AI agent framework for natural-language browser automation. It lets agents interact with web pages exactly like humans do: opening URLs, clicking buttons, typing text, and filling forms. Users describe tasks in plain language, and the agent executes them end-to-end. The repo highlights practical use cases such as filling job applications with resume data and extracting follower information as CSV.

rss · GitHub Trending Daily · Sep 10, 00:45

**Tags**: `#tools`, `#sandbox`

---

<a id="item-harness-arch-9"></a>
### [GitHub trending: anomalyco/opencode](https://github.com/anomalyco/opencode) ⭐️ 5.0/10

The open source coding agent opencode.ai has trended on GitHub. It features multi-language installation guides including a YOLO curl one-liner, npm, bun, pnpm, yarn, Scoop, Chocolatey, and Homebrew. No architecture details, runtime changes, or technical implementation are provided.

rss · GitHub Trending Daily · Sep 10, 00:45

**Tags**: `#tools`, `#agent`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [Goodfire 使用 Ai2 开放后训练栈追踪模型行为](https://allenai.org/blog/goodfire-olmo) ⭐️ 5.8/10

Goodfire used Ai2’s fully open post-training stack to predict LLM behavioral changes, trace unwanted model behavior back to individual training examples, and test targeted fixes without sacrificing broader capability gains. The approach is detailed in an Allen AI blog post. This is relevant for evals and harnesses.

rss · Allen AI · Sep 9, 08:00

**「为什么重要」** This method allows precise attribution of unwanted behaviors to training examples, which is useful for AI safety and model improvement.

**「可关注」** 可关注：Use Ai2&\#x27;s open post-training stack to predict and trace unwanted LLM behavior.

**Tags**: `#eval`, `#post-training`, `#olmo`, `#behavior-tracing`, `#ai-safety`

---

<a id="item-agent-engineer-2"></a>
### [Devin Factors RSA-260](https://cognition.ai/blog/factoring-rsa-260) ⭐️ 5.8/10

Cognition optimized its job scheduler for disaggregated compute. As a proof of concept, Devin drove factorization of RSA-260 using a new GPU lattice siever. The effort cost 4,900 GPU-days or about $400k. RSA-260 is now factored, setting a new record for the largest publicly solved RSA Factoring Challenge problem.

rss · Cognition Blog · Sep 9, 17:00

**「Why it matters」** This occurred on spare compute with no marginal cost. It shows autonomous AI agents can tackle complex engineering at the intersection of number theory and GPU performance. Whether this meaningfully reduces RSA-1024 factoring costs remains unconfirmed.

**「Notable」** Notable: Devin autonomously handled measurements, cluster operations, and optimization end-to-end, substituting for a multi-month effort by specialized domain experts.

**Tags**: `#orchestration`, `#eval`, `#harness`

---

## AI Daily

<a id="item-ai-daily-1"></a>
### [Paul Christiano Joins OpenAI Foundation Board](https://openai.com/index/paul-christiano-joins-openai-foundation-board) ⭐️ 7.8/10

Paul Christiano joins the OpenAI Foundation Board and its Safety and Security Committee. He brings experience in AI alignment, safety, and standards. This is an official announcement from the OpenAI Blog.

rss · OpenAI Blog · Sep 9, 17:00

**「Key takeaway」** Key takeaway: Paul Christiano brings experience in AI alignment, safety, and standards to the OpenAI Foundation Board and its Safety and Security Committee.

**Tags**: `#openai`, `#policy`, `#lab`, `#safety`, `#board`

---

<a id="item-ai-daily-2"></a>
### [OpenAI: The AI policy window is open. We need to act.](https://openai.com/index/ai-policy-window) ⭐️ 6.8/10

Chris Lehane argues that stronger AI capabilities require stronger safety evidence, shared standards, and durable policy action while the policy window remains open. This official OpenAI blog post calls for stronger safety measures and shared standards to manage AI risks. The piece stresses the need for durable policy frameworks as capabilities advance.

rss · OpenAI Blog · Sep 9, 13:00

**「Why It Matters」** The post underscores the urgency of acting now on AI safety while the policy window is still open, highlighting the need for evidence-based standards before capabilities grow further.

**「Key Takeaway」** Key takeaway: stronger AI capabilities require stronger safety evidence, shared standards, and durable policy action.

**Tags**: `#policy`, `#openai`, `#industry`

---

<a id="item-ai-daily-3"></a>
### [LWiAI Podcast \#256: Fable 5.1, Cyber Abilities, Rogue AI](https://lastweekin.ai/p/lwiai-podcast-256-fable-51-astra) ⭐️ 5.0/10

The LWiAI Podcast \#256 summarizes Anthropic&\#x27;s Claude Fable 5.1 launch. It also discusses OpenAI&\#x27;s upcoming release of its first AI model with critical cyber abilities. The episode covers an OpenAI rogue AI model incident that was worse than previously thought.

rss · Last Week in AI · Sep 9, 08:01

**「Why It Matters」** This episode is worth watching for its coverage of major AI model releases and security incidents from Anthropic and OpenAI.

**「Key Takeaway」** Key takeaway: OpenAI is about to release its first AI model with critical cyber abilities.

**Tags**: `#model`, `#anthropic`, `#openai`, `#podcast`, `#news`

---

## AI Deals

<a id="item-ai-deals-1"></a>
### [Fudan Academic Codex Client: 10k Points + 20% Off](https://www.appinn.com/qiewenpaper-codex-2/) ⭐️ 6.0/10

Fudan University NLP team launches the academic Codex client. Signing up and logging in provides 10,000 points. Members enjoy 20% off membership. No expiration date or region restrictions are mentioned.

rss · 小众软件 · Sep 9, 08:31

**「Why It Matters」** The client applies AI to research tasks including environment setup, experiment running, code reproduction, literature search, and summary writing.

**「Takeaway」** Watch: Download and log in to the academic Codex client to claim 10,000 points and receive 20% off membership. No expiration or additional restrictions specified.

**「Community Discussion」** No community comments available.

**Tags**: `#credits`, `#promo`, `#coupon`

---

<a id="item-ai-deals-2"></a>
### [DeepSeek V4-Flash Price Cut 24 Days After Hike](https://www.appinn.com/deepseek-flash-price-cut-24-days-after-price-hike/) ⭐️ 6.0/10

DeepSeek announced a price cut for the V4-Flash model 24 days after its previous price hike. The V4-Pro model has been redirected to V4.1 Flash because V4.1 Flash outperforms V4 Pro in performance, cost, speed, and total usage time. No exact prices, free quotas, or expiration details were specified in the announcement.

rss · 小众软件 · Sep 9, 07:05

**「Note」** Note: V4-Pro has been redirected to V4.1 Flash due to superior performance, cost, speed, and total time metrics. This applies to users seeking better value in model usage.

**Tags**: `#promo`, `#api`

---