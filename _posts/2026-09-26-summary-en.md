---
layout: default
title: "Horizon Summary: 2026-09-26 (EN)"
date: 2026-09-26
lang: en
---

> From 189 items, 11 important content pieces were selected

---

**Agent Harness Architecture**
1. [Mastra Core 1.70.0 Released](#item-harness-arch-1) ⭐️ 8.8/10
2. [Claude Code 2.1.283 发布](#item-harness-arch-2) ⭐️ 8.8/10
3. [anthropics/claude-code released v2.1.283](#item-harness-arch-3) ⭐️ 8.3/10
4. [Pydantic-AI v2.51.0 Adds GPT-Live and Realtime Checks](#item-harness-arch-4) ⭐️ 8.3/10
5. [pydantic-ai v2.50.0 Adds DecisionModel and Durable Context](#item-harness-arch-5) ⭐️ 8.3/10
6. [DSPy 3.4.0 Adds Jev Decision Types and Native LM Engines](#item-harness-arch-6) ⭐️ 8.3/10
7. [openai/codex released rust-v0.157.0](#item-harness-arch-7) ⭐️ 7.8/10

**AI Agent Engineer**
1. [Qwengram-0.8B 迁移 PLE 记忆，PPL 降 5.05%](#item-agent-engineer-1) ⭐️ 5.5/10
2. [Mica v0.1 4B got an iron pickaxe in real Minecraft without generating a single token](#item-agent-engineer-2) ⭐️ 5.5/10

**AI Daily**
1. [GitHub Copilot app for Beginners: How to build custom workflows with canvases](#item-ai-daily-1) ⭐️ 6.8/10

**Technology Blog**
1. [@simonw: RT @hillelogram: @simonw &quot;It doesn&\#x27;t get easier, y...](#item-tech-blog-1) ⭐️ 0.0/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [Mastra Core 1.70.0 Released](https://github.com/mastra-ai/mastra/releases/tag/%40mastra/core%401.70.0) ⭐️ 8.8/10

Mastra released @mastra/core@1.70.0. The release adds ModelSelectionProcessor for dynamic per-request model routing using a classifier, with fallback to the agent&\#x27;s configured model and options like scope: &\#x27;first-step&\#x27; and minProbability. It also introduces cross-process cancellation of queued thread inputs via cancelQueuedMessages\(\{ signalIds \}\) across agents sharing runtime and memory, and multi-tenant safe observability queries with trusted \{organizationId, resourceId?\} scopes enforced by stores and bound into cursors.

github · PaulieScanlon · Sep 25, 10:06

**「Design Notes」** ModelSelectionProcessor runs as an input processor that builds a classifier from model descriptions and criteria; the selected model serves the entire run unless scope: &\#x27;first-step&\#x27; is set. Observability queries now require a trusted tenant scope that stores enforce and bind into pagination cursors, failing fast on conflicts.

**「What Changed」** Durable agent streams gain closeOnSuspend to terminate at tool-suspension boundaries, matching non-durable behavior and fixing hung fullStream loops. Memory now filters client-echoed history on existing threads, retaining only new trailing user messages and pending tool outcomes unless retainFullInput is set.

**Tags**: `#runtime`, `#memory`, `#eval`, `#permissions`

---

<a id="item-harness-arch-2"></a>
### [Claude Code 2.1.283 发布](https://code.claude.com/docs/en/changelog#2-1-283) ⭐️ 8.8/10

Claude Code 2.1.283 为 LLM 网关新增 \`x-claude-code-prompt-id\` 提示头，用 \`CLAUDE\_CODE\_GATEWAY\_HINT\_HEADERS=1\` 开启后可按用户提示归组请求。托管设置新增 \`availableModelsMatch\` 与 \`deniedModels\`，前者在 \`&quot;exact&quot;\` 模式下仅放行条目写明的模型版本，后者直接屏蔽特定模型。可观测性上，\`OTEL\_LOG\_TOOL\_CONTENT=1\` 会把 MCP 工具、WebFetch 和 WebSearch 输出写入 \`tool.output\` span 事件。诊断侧新增 \`/doctor prompt-audit\`（别名 \`/checkup prompt-audit\`），审计 CLAUDE.md、skills、agents 和 commands 中面向旧模型的提示模式。

rss · Claude Code Changelog · Sep 25, 22:00

**「设计要点」** 网关层通过 opt-in hint header 把同一提示的多轮请求显式关联，便于网关侧做聚合与限流。托管模型策略改为白名单加黑名单双轨，\`availableModelsMatch\` 精确匹配时未列出的新版本默认拒绝，权限判定更收敛。

**「改了什么」** 相比前一版，2.1.283 把网关请求归组、模型版本管控和工具输出遥测从默认行为改为显式开关或托管配置，同时补上 prompt-audit 这类面向旧提示模式的静态检查。插件与 MCP 侧修复集中在缓存失效、配置读写和后台任务进度丢失，属于稳定性修补。

**Tags**: `#runtime`, `#permissions`, `#eval`, `#tools`, `#mcp`

---

<a id="item-harness-arch-3"></a>
### [anthropics/claude-code released v2.1.283](https://github.com/anthropics/claude-code/releases/tag/v2.1.283) ⭐️ 8.3/10

Claude Code v2.1.283 adds managed model permission controls, gateway request-grouping headers, OTEL tool-content logging, and a prompt-audit diagnostic.

github · ashwin-ant · Sep 25, 21:50

**Tags**: `#runtime`, `#tools`, `#permissions`, `#eval`, `#mcp`

---

<a id="item-harness-arch-4"></a>
### [Pydantic-AI v2.51.0 Adds GPT-Live and Realtime Checks](https://github.com/pydantic/pydantic-ai/releases/tag/v2.51.0) ⭐️ 8.3/10

Pydantic-AI v2.51.0 introduces \`OpenAILiveModel\` for OpenAI GPT-Live and exposes \`context\_window\_used\` on realtime sessions. The release raises \`UserError\` for realtime \`tool\_choice\` that forces a tool call on OpenAI, Azure OpenAI, and xAI. It also matches dated \`gemini-3.8-live\` IDs, rejects \`google\_affective\_dialog\` on Gemini 3.1 Flash Live and 3.8 Live at connect, and raises \`RealtimeError\` for Gemini Live close codes. Runtime fixes reduce \`RunContext\` copying, cache the agent graph, and avoid spawning task groups for single-child fan-outs.

github · DouweM · Sep 25, 23:19

**「Design Notes」** Realtime sessions now surface \`context\_window\_used\` from GPT-Live&\#x27;s reported ratio or response usage, giving capability hooks direct visibility into context consumption. Validation shifts earlier in the connection lifecycle, rejecting invalid \`tool\_choice\` and Gemini options before the session establishes.

**「What Changed」** Adds \`OpenAILiveModel\` and \`context\_window\_used\` on realtime sessions. Enforces stricter \`tool\_choice\` and Gemini Live compatibility checks, and cuts runtime overhead by caching the agent graph, reducing \`RunContext\` copies, and eliminating single-child task groups.

**Tags**: `#runtime`, `#tools`

---

<a id="item-harness-arch-5"></a>
### [pydantic-ai v2.50.0 Adds DecisionModel and Durable Context](https://github.com/pydantic/pydantic-ai/releases/tag/v2.50.0) ⭐️ 8.3/10

pydantic-ai v2.50.0 introduces DecisionModel as a base for Decisions-protocol models and makes TypeSafeModel one. The release adds RunContext.in\_durable\_context so hooks can detect durable workflow execution, and refines ModelSelectionContext with breaking changes to message ordering plus a new prompt field. It also adds gemini-3.8-live and gemini-3.8-live-extended-thinking realtime support and fixes pricing and realtime session bugs.

github · DouweM · Sep 25, 04:47

**「Design Notes」** DecisionModel emits a decide span for every request and asks route fields under a route premise with nested-field context and a done state after tool calls. The previous tool-call lean is replaced by an opt-in decision\_route\_threshold. RunContext.in\_durable\_context lets hooks branch behavior when running inside durable workflow code.

**「What Changed」** Breaking changes include DecisionModel asking which route to take by name with one label per route, ModelSelectionContext.messages ending with the request being routed, the addition of ModelSelectionContext.prompt, and replacing the decision model&\#x27;s tool-call lean with an opt-in decision\_route\_threshold. New features include exposing OpenAI service\_tier in provider details and adding gemini-3.8-live realtime support.

**Tags**: `#runtime`, `#planning`, `#tools`

---

<a id="item-harness-arch-6"></a>
### [DSPy 3.4.0 Adds Jev Decision Types and Native LM Engines](https://github.com/stanfordnlp/dspy/releases/tag/3.4.0) ⭐️ 8.3/10

DSPy 3.4.0 introduces Jev integration through the TypeSafe client, adding experimental decision types \`Noul\`, \`Choice\`, and \`Score\` that return probability evidence alongside values. The release adds native LM engines built on bundled \`lm15\` types, a local CPython interpreter for trusted code, async ReActV2, and versioned documentation. It is also the LM transition release: experimental LM types from 3.3 are replaced, legacy custom-LM integrations and OpenAI-style \`messages=\` calls remain with deprecation warnings, and 3.5 is the migration deadline. RLM&\#x27;s call-time interpreter API changes to require a keyword-only \`interpreter\_factory=\`.

github · isaacbmiller · Sep 25, 04:06

**「Design Notes」** The LM layer now defaults to \`engine=&quot;auto&quot;\`, preferring native execution for supported routes and falling back to LiteLLM only before inference; authentication failures, timeouts, and provider errors never trigger a backend switch. Decision thresholds, Score cuts, and Choice weights are applied locally in the predictor rather than sent to the backend, so identical requests can reuse cached evidence.

**「What Changed」** Jev integration lands through the TypeSafe client with experimental \`Noul\`, \`Choice\`, and \`Score\` types, and the new \`ReAnchor\` optimizer calibrates their thresholds against the program metric. The LM layer gains native \`lm15\` engines and \`register\_provider\(...\)\` for compatible HTTP services, while RLM switches to a keyword-only \`interpreter\_factory=\` and the LM API enters its transition period with a 3.5 migration deadline.

**Tags**: `#runtime`, `#tools`, `#eval`

---

<a id="item-harness-arch-7"></a>
### [openai/codex released rust-v0.157.0](https://github.com/openai/codex/releases/tag/rust-v0.157.0) ⭐️ 7.8/10

Codex Rust v0.157.0 adds background-server auto-start, conversation forking, and remote import support alongside GPT-6 model updates.

github · github-actions\[bot\] · Sep 25, 02:31

**Tags**: `#runtime`, `#tools`, `#planning`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [Qwengram-0.8B 迁移 PLE 记忆，PPL 降 5.05%](https://www.reddit.com/r/LocalLLaMA/comments/1wpvep4/qwengram08b_i_transferred_qwen38_flashnexts_ngram/) ⭐️ 5.5/10

作者将 Qwen3.8-Flash-Next 的 51B 参数 PLE n-gram 记忆迁移进 Qwen3.5-0.8B，保持骨干与记忆冻结，仅在 decoder 第 3、9 层训练 R=1 reader 并加 token-dependent linear gate。冻结全验证集上 PPL 从 18.2759 降至 17.3534，降幅 5.05%，NLL 从 2.905585 降至 2.853786；真实预训练 PLE 优于随机与置换记忆对照。作者明确这是语言模型验证结果，非基准准确率提升；15M token 为平衡检查点，20M 虽改善总体 loss 但数学回退。llama.cpp 推理路径已实现，GGUF 含骨干与 reader，PLE 作为外部量化 sidecar；Q8\_0 在独立 WikiText-2 测试中保留 99.1% 的 BF16 reader NLL 增益。

reddit · r/LocalLLaMA · /u/Nicolodeva · Sep 25, 12:46

**「为什么重要」** 对做 coding agent 与 harness 的人，这展示了一条不微调骨干、用轻量 reader 和动态门控把大模型记忆迁移到小模型的路径，且随机与置换对照说明增益来自预训练 PLE 本身。但证据目前只有 Reddit 一手实验，缺乏独立复现；5.05% 的困惑度增益较窄，尚未验证对 agent 任务或工具链的实际影响。

**「可关注」** 可关注：PLE 以外部量化 sidecar 存在、GGUF 只打包骨干与 reader 的部署方式，以及动态 token 级门控相比固定注入在 LAMBADA 上的恢复效果；作者计划放大到 35B-A3B MoE，reader 扩展与 PLE 缓存策略值得跟踪。

**Tags**: `#memory`, `#eval`, `#orchestration`

---

<a id="item-agent-engineer-2"></a>
### [Mica v0.1 4B got an iron pickaxe in real Minecraft without generating a single token](https://www.reddit.com/r/LocalLLaMA/comments/1wqahbz/mica_v01_4b_got_an_iron_pickaxe_in_real_minecraft/) ⭐️ 5.5/10

A 4B model plays Minecraft by scoring candidate commands with zero generated tokens in ~90–150 ms per step, but the Reddit-only source limits it to browse-level priority.

reddit · r/LocalLLaMA · /u/Top-Evidence174 · Sep 25, 22:55

**Tags**: `#coding-agent`, `#eval`, `#harness`, `#observability`

---

## AI Daily

<a id="item-ai-daily-1"></a>
### [GitHub Copilot app for Beginners: How to build custom workflows with canvases](https://github.blog/ai-and-ml/github-copilot/github-copilot-app-for-beginners-how-to-build-custom-workflows-with-canvases/) ⭐️ 6.8/10

GitHub&\#x27;s official blog offers a beginner guide to creating custom workflows with canvases in the GitHub Copilot app.

rss · GitHub Blog · Sep 25, 18:00

**Tags**: `#product`, `#lab`, `#model`

---

## Technology Blog

<a id="item-tech-blog-1"></a>
### [@simonw: RT @hillelogram: @simonw &quot;It doesn&\#x27;t get easier, y...](https://twitter.com/simonw/status/tweet-2103495582048555120) ⭐️ 0.0/10

A retweeted quote about programming speed that lacks technical substance or transferable lessons.

twitter · Simon Willison · Sep 25, 14:43

**Tags**: `#software engineering`, `#productivity`, `#quotation`, `#social media`

---