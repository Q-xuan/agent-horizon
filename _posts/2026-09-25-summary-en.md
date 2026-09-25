---
layout: default
title: "Horizon Summary: 2026-09-25 (EN)"
date: 2026-09-25
lang: en
---

> From 226 items, 17 important content pieces were selected

---

**Agent Harness Architecture**
1. [Mastra Core 1.69.0 Adds Classifiers, Policy Gates, and Background Tools](#item-harness-arch-1) ⭐️ 8.8/10
2. [cline/cline released sdk/sdk/v0.0.86](#item-harness-arch-2) ⭐️ 8.3/10
3. [pydantic/pydantic-ai released v2.49.0](#item-harness-arch-3) ⭐️ 8.3/10
4. [Cline Desktop v0.0.35 Adds Linux Builds and Plugin Command Fixes](#item-harness-arch-4) ⭐️ 7.3/10
5. [Cline CLI v3.0.65 Patch](#item-harness-arch-5) ⭐️ 6.3/10
6. [Gemini CLI v0.61.0 Released](#item-harness-arch-6) ⭐️ 6.3/10
7. [2.1.282](#item-harness-arch-7) ⭐️ 6.3/10
8. [Anthropic financial-services Repo Ships Reference Agents](#item-harness-arch-8) ⭐️ 5.5/10

**AI Agent Engineer**
1. [HF daily paper: Schrödinger&\#x27;s Code Repository: Have LLMs Learned SWE-bench or Memorized It?](#item-agent-engineer-1) ⭐️ 8.0/10
2. [JIT Memory 论文：查询时再筛选记忆](#item-agent-engineer-2) ⭐️ 7.0/10
3. [Paper Extracts Hidden CoT from Frontier Models via API Tools](#item-agent-engineer-3) ⭐️ 7.0/10
4. [VHD-Play 论文：先解模型再造环境](#item-agent-engineer-4) ⭐️ 7.0/10
5. [LFM2.5-VL-DSpark 发布](#item-agent-engineer-5) ⭐️ 6.8/10

**AI Daily**
1. [Claude Opus 5.5 降价 40%](#item-ai-daily-1) ⭐️ 9.8/10
2. [Meta AI Glasses 隐私处理](#item-ai-daily-2) ⭐️ 8.8/10
3. [AI-powered fuzzing with the GitHub Security Lab Taskflow Agent](#item-ai-daily-3) ⭐️ 7.8/10
4. [Claude Tag 频道支持个人连接器](#item-ai-daily-4) ⭐️ 7.8/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [Mastra Core 1.69.0 Adds Classifiers, Policy Gates, and Background Tools](https://github.com/mastra-ai/mastra/releases/tag/%40mastra/core%401.69.0) ⭐️ 8.8/10

Mastra Core 1.69.0 promotes classifiers, policy enforcement, and background tool execution to first-class runtime primitives. Developers register classifiers on \`new Mastra\(\{ classifiers \}\)\`, manage them through \`getClassifier\`/\`listClassifiers\`/\`addClassifier\`/\`removeClassifier\`, and use them as typed workflow steps with token usage for branching. A new \`ClassifierProcessor\` applies typed policies to agent input, output, and streaming content, failing closed by default with an opt-in \`errorStrategy: &\#x27;warn&\#x27;\`. Tools can hand long-running operations to Mastra via \`context.background.adopt\(\{ completion, cancel \}\)\` and return immediately, though adopted handles remain in-memory and do not survive restarts.

github · PaulieScanlon · Sep 24, 06:58

**「Design Notes」** Classifier evaluations without an active trace start a root \`CLASSIFIER\_EVALUATION\` span through the configured observability provider. Background adoption decouples \`execute\(\)\` return from operation completion, letting the runtime track cancellation without holding the call open.

**「What Changed」** The release adds classifier registration and management APIs, a \`ClassifierProcessor\` for input/output/streaming gates with fail-closed defaults, and native background tool adoption via \`context.background.adopt\(\)\`. It also introduces \`rootSpanName\` in \`tracingOptions\` for per-run root span naming and deprecates trace-query \`group\` in favor of the \`queryThreads\` contract.

**Tags**: `#runtime`, `#tools`, `#permissions`, `#planning`, `#eval`

---

<a id="item-harness-arch-2"></a>
### [cline/cline released sdk/sdk/v0.0.86](https://github.com/cline/cline/releases/tag/sdk/sdk/v0.0.86) ⭐️ 8.3/10

Cline SDK v0.0.86 adds a compact-and-retry recovery path for output-token truncation on local model servers and improves hub startup error reporting.

github · github-actions\[bot\] · Sep 24, 05:43

**Tags**: `#runtime`, `#memory`

---

<a id="item-harness-arch-3"></a>
### [pydantic/pydantic-ai released v2.49.0](https://github.com/pydantic/pydantic-ai/releases/tag/v2.49.0) ⭐️ 8.3/10

pydantic-ai v2.49.0 adds GitHub Copilot OAuth device flow, TypeSafeModel structured-output refinements, and a RealtimeSession reply-wait API, plus logprobs and model-support fixes.

github · DouweM · Sep 24, 03:09

**Tags**: `#runtime`, `#permissions`, `#eval`

---

<a id="item-harness-arch-4"></a>
### [Cline Desktop v0.0.35 Adds Linux Builds and Plugin Command Fixes](https://github.com/cline/cline/releases/tag/desktop-v0.0.35) ⭐️ 7.3/10

Cline Desktop v0.0.35 adds Linux support with x64 .deb and .rpm packages, fixes plugin slash commands to execute registered handlers rather than send plain text to the model, and introduces a Diagnostics export that strips sensitive data. The release also restores voice input with provider-backed streaming transcription, remembers reasoning effort per provider, and surfaces actual endpoint errors for several model providers. First launch after install or update can take 8 to 13 seconds on Windows while the new binary is scanned.

github · github-actions\[bot\] · Sep 24, 08:34

**「Design Notes」** The desktop runtime now supports Linux with native GTK pickers and background updates that install on restart. Plugin slash commands execute registered handlers, the slash menu sources skills and workflows from the conversation&\#x27;s own workspace including worktrees, and Diagnostics export strips API keys, credential-shaped values, prompts, and home directory paths before writing a single text file.

**「What Changed」** Linux packaging \(.deb/.rpm\) is new, plugin slash commands now run registered handlers instead of sending text to the model, and a Diagnostics export writes sanitized logs and session manifests to Downloads. Voice input returns with provider-backed streaming transcription, reasoning effort persists per provider, and model lists surface real endpoint errors.

**Tags**: `#runtime`, `#tools`, `#plugins`

---

<a id="item-harness-arch-5"></a>
### [Cline CLI v3.0.65 Patch](https://github.com/cline/cline/releases/tag/cli-v3.0.65) ⭐️ 6.3/10

Cline CLI v3.0.65 patches local model reliability and hub startup behavior. When llama.cpp, Ollama, or LM Studio cap generation at the remaining context, the CLI compacts the conversation and retries the turn once before falling back to concise-retry recovery, preserving partial answers if all attempts fail. Hub startup errors now state the cause instead of a generic message, and the CLI waits up to 15 seconds for a fresh hub instead of 8. Session error messages persist across resumes without being sent to the model or counted by compaction.

github · github-actions\[bot\] · Sep 24, 05:54

**「设计要点」** Runtime recovery now handles output-token exhaustion by compacting context and retrying once, while failed plugin loads avoid repeated sandbox spawns by retrying after 30 seconds. Session state keeps error transcripts across resumes without feeding them back into the model context.

**「改了什么」** Local model runs survive output-token limits via compaction and retry, hub startup failures now report causes with a 15-second wait, and session errors persist across resumes. \`cline history update\` metadata now persists for hub-managed sessions, the ai&amp; provider joins the catalog, and Yolo mode \(\`-y\`\) enforces tighter output rules.

**Tags**: `#runtime`, `#memory`, `#tools`

---

<a id="item-harness-arch-6"></a>
### [Gemini CLI v0.61.0 Released](https://github.com/google-gemini/gemini-cli/releases/tag/v0.61.0) ⭐️ 6.3/10

Gemini CLI v0.61.0 is a minor maintenance release published on 2026-09-23. It focuses on security hardening and core runtime fixes rather than architectural changes. Key corrections include blocking indirect prompt injection through build file modifications and untrusted flags, hardening sandbox filesystem boundaries, and preserving explicit versioned Flash model IDs. The release notes also include a cherry-picked patch that produced v0.61.0-preview.1.

github · gemini-cli-robot · Sep 23, 23:59

**「Design Points」** The sandbox fix isolates runtime state and tightens filesystem boundaries. A core fix ensures AgentLoopContext properties are preserved across object spread operations. These adjustments affect the tool execution layer and agent loop context without adding new capabilities.

**「What Changed」** Relative to v0.60.0, v0.61.0 introduces indirect prompt injection prevention for build files and untrusted flags, hardens sandbox filesystem isolation, preserves explicit versioned Flash model IDs, and fixes AgentLoopContext property loss during object spread. A patch cherry-pick also generated v0.61.0-preview.1.

**Tags**: `#sandbox`, `#permissions`, `#runtime`

---

<a id="item-harness-arch-7"></a>
### [2.1.282](https://code.claude.com/docs/en/changelog#2-1-282) ⭐️ 6.3/10

Claude Code 2.1.282 adds minor terminal, telemetry, MCP, and gateway settings plus a web-history 400 error fix.

rss · Claude Code Changelog · Sep 24, 18:46

**Tags**: `#runtime`, `#mcp`, `#permissions`, `#sandbox`, `#tools`

---

<a id="item-harness-arch-8"></a>
### [Anthropic financial-services Repo Ships Reference Agents](https://github.com/anthropics/financial-services) ⭐️ 5.5/10

Anthropic open-sourced \`anthropics/financial-services\`, a reference repository of agents, skills, and data connectors for investment banking, equity research, private equity, and wealth management workflows. The same system prompts and skills ship from one source and run in two modes: installed as a Claude Cowork plugin or deployed through the Claude Managed Agents API behind a custom workflow engine. The repo is domain-specific reference material rather than a harness architecture or protocol update.

rss · GitHub Trending Daily · Sep 24, 23:19

**「Design Notes」** Agent definitions are decoupled from runtime: identical prompts and skills execute either locally via the Cowork plugin or remotely via the Managed Agents API, so teams can choose execution location without rewriting logic.

**Tags**: `#agents`, `#tools`, `#runtime`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [HF daily paper: Schrödinger&\#x27;s Code Repository: Have LLMs Learned SWE-bench or Memorized It?](https://huggingface.co/papers/2609.27891) ⭐️ 8.0/10

A new paper introduces SchrodingerRepo, an evaluation framework that dynamically instantiates repository representations to combat data leakage and memorization in coding agent benchmarks like SWE-bench.

rss · Hugging Face Daily Papers · Sep 24, 00:00

**Tags**: `#eval`, `#coding-agent`, `#memory`

---

<a id="item-agent-engineer-2"></a>
### [JIT Memory 论文：查询时再筛选记忆](https://huggingface.co/papers/2609.27334) ⭐️ 7.0/10

Hugging Face Daily Papers 收录论文 Just-in-Time Memory，提出保留原始轨迹、在查询时再学习 curation 的 agent memory 新范式。现有系统多在任务完成后把轨迹蒸馏成反思、工作流、技能或推理策略等固定工件，在查询到来前就不可逆地丢弃信息；学习 write-time curator 也受长程信用分配制约，存储决策的价值可能要等很多任务之后的相关查询出现才显现。论文主张把筛选推迟到查询时，生成 task-adaptive memory。该文于 2026-09-24 发布，获 33 upvotes，但摘要未展示基准突破或生产数据。

rss · Hugging Face Daily Papers · Sep 24, 00:00

**「为什么重要」** 对做 coding agent / harness 的人，这直接质疑了当前主流的 write-time memory 设计：如果记忆在写入时就被压成 query-independent 摘要，长程任务里真正有用的细节可能已经丢失。论文把问题从“怎么摘要更好”转向“什么时候筛选”，但尚未给出基准或生产验证，实际收益仍待观察。

**「可关注」** 如果你们的 agent memory 也在任务结束时做 reflection 或 workflow 蒸馏，可以评估保留原始轨迹、把筛选逻辑移到查询时是否会减少信息损失，尤其关注长程信用分配导致的存储决策难题。

**Tags**: `#memory`, `#eval`, `#coding-agent`

---

<a id="item-agent-engineer-3"></a>
### [Paper Extracts Hidden CoT from Frontier Models via API Tools](https://huggingface.co/papers/2609.26637) ⭐️ 7.0/10

A Hugging Face daily paper \(2026-09-24\) introduces a method to externalize hidden chain-of-thought in closed-source frontier models by registering a custom tool through a standard API feature. Validated against native CoT on open-source models and extended to closed frontier models including GPT-6 Astra, the extracted reasoning matches native performance and substantially outperforms no-reasoning baselines across competition mathematics, science, and code generation. The authors caution that these traces may reflect post-hoc rationalization rather than genuine reasoning, and characterize how frontier models structure intermediate steps. The work targets agent evaluation and observability; it is a research finding, not a change to mainstream coding agents, protocols, or benchmarks.

rss · Hugging Face Daily Papers · Sep 24, 00:00

**「为什么重要」** Engineers gain a concrete, reproducible way to inspect intermediate reasoning in closed models via standard API tool calls, addressing an observability gap for agent evaluation. The authors caution, however, that externalized traces may be post-hoc rationalizations and should not be treated as verified ground-truth reasoning.

**「可关注」** Registering a custom API tool can induce frontier models to externalize hidden CoT with parity to native reasoning, but the traces require careful interpretation as potential post-hoc rationalizations.

**Tags**: `#eval`, `#observability`, `#coding-agent`, `#harness`

---

<a id="item-agent-engineer-4"></a>
### [VHD-Play 论文：先解模型再造环境](https://huggingface.co/papers/2609.27321) ⭐️ 7.0/10

VHD-Play 反转了环境生成依赖：先采样并求解数学模型，再由语料约束的 setter 将决策过程渲染为有状态工具。可执行动力学与轨迹打分参考来自同一已解模型，无需事后对齐。该 pipeline 以每个环境几美分的成本产出 3,300 个多样化 agentic RL 环境。材料提及在 Qwen3.6-35B-A3B 上开展训练，但具体结果被截断，未给出。

rss · Hugging Face Daily Papers · Sep 24, 00:00

**「为什么重要」** 对做 coding agent / harness 的人来说，环境构造与评估规则的事后对齐是常见成本。VHD-Play 把动力学和评分参考绑定到同一个已解模型，为低成本、可扩展的 agentic RL 环境生成提供了一条可复现路径。已发生的变化是 pipeline 设计本身，尚未证实的影响是其训练收益。

**「可关注」** 可关注：若需批量构造可验证的 agentic 训练环境，可评估「先解模型、后渲染工具」的路线，尤其关注其已解模型如何同时提供动力学与评分参考。

**Tags**: `#eval`, `#orchestration`, `#harness`

---

<a id="item-agent-engineer-5"></a>
### [LFM2.5-VL-DSpark 发布](https://huggingface.co/blog/LiquidAI/lfm2-5-vl-dspark) ⭐️ 6.8/10

Liquid AI 发布 LFM2.5-VL-DSpark，为 LFM2.5-VL-3B 配套视觉草稿模型，通过投机解码加速 VLM 推理。草稿模型约 280M 参数，增加 8.9% 部署开销，采用 4 层简化注意力结构，推荐块大小 8 或 9。官方基准显示，设备端解码最高加速 3.13x，H100 上为 20.4x–2.66x；端到端提升最高分别达 2.62x 和 2.27x。llama.cpp、MLX-VLM、SGLang 首日支持，但需合入对应 PR；投机解码保持精确，贪心输出与单独运行目标模型一致。

rss · Hugging Face Blog · Sep 24, 14:08

**「为什么重要」** 视觉编码与 prefill 仍占用大量端到端时延，投机解码只加速 decode 阶段。对多模态 agent 推理栈，这提供了可复用的加速路径，但收益受 Amdahl 定律限制。

**「可关注」** 可关注：视觉草稿模型复用文本 DSpark 架构，图像 patch 与文本 token 在 hidden states 层前统一表征，推理算法不变；SGLang、llama.cpp、MLX-VLM 均已提供启用路径，但需合入对应 PR 并配置块大小。

**Tags**: `#toolchain`, `#inference`, `#vlm`

---

## AI Daily

<a id="item-ai-daily-1"></a>
### [Claude Opus 5.5 降价 40%](https://claude.com/blog/claude-opus-5-5-built-for-coding-sessions-that-use-more-context) ⭐️ 9.8/10

Claude 发布 Opus 5.5，官方称按 token 计费的典型负载运行成本比 Opus 5 低约 40%，其中输入输出 token 降价 20%，缓存读取降价 60%。官方数据显示，2026 年 3 月至 9 月 Claude Code 单次请求上下文增长约 2.6 倍，缓存未命中率下降超 50%。Zeta Labs 实测任务轮次和工具调用减少，成本近乎减半，最难任务完成量翻倍；Addy 指出开放式任务收益更明显，范围明确的任务差距不大。

rss · Claude Blog · Sep 24, 00:00

**「为什么重要」** 编程会话正从短交互转向长时程、高上下文 agent 任务，缓存读取占 agent 任务成本大头。Opus 5.5 的降价和 Claude Code harness 优化针对这一趋势，且允许会话中切换 effort 级别而不重置缓存。

**「可关注」** 可关注：在 Claude Code 中运行 /usage 查看缓存读取占比，把 Opus 5.5 用于开放式、高上下文任务；范围明确的短任务可能只享受降价，轮次不会明显减少。

**Tags**: `#model`, `#lab`, `#product`, `#industry`

---

<a id="item-ai-daily-2"></a>
### [Meta AI Glasses 隐私处理](https://engineering.fb.com/2026/09/23/security/private-processing-meta-ai-glasses/) ⭐️ 8.8/10

Meta 官方工程博客宣布为 Meta AI Glasses 带来隐私处理能力。文章称眼镜是全天候获得 AI 协助的最佳形态，能更好理解个人上下文，并让用户无需拿起手机即可保持在场。目前公开信息仅确认该功能发布，未披露具体技术实现、部署范围或性能数据。

rss · Engineering at Meta · Sep 24, 00:00

**「为什么重要」** Meta 将隐私处理作为 AI Glasses 的官方能力发布，对关注可穿戴设备隐私架构的工程师具有参考价值。

**「可关注」** 可关注：Meta AI Glasses 隐私处理的具体技术路径尚未公开，需等待后续官方文档或论文披露实现细节。

**Tags**: `#product`, `#industry`, `#policy`

---

<a id="item-ai-daily-3"></a>
### [AI-powered fuzzing with the GitHub Security Lab Taskflow Agent](https://github.blog/security/application-security/ai-powered-fuzzing-with-the-github-security-lab-taskflow-agent/) ⭐️ 7.8/10

GitHub Security Lab announced an AI-powered fuzzing taskflow agent in an official blog post.

rss · GitHub Blog · Sep 24, 18:26

**Tags**: `#product`, `#open-source`, `#lab`, `#industry`

---

<a id="item-ai-daily-4"></a>
### [Claude Tag 频道支持个人连接器](https://claude.com/blog/claude-tag-now-supports-personal-connectors-in-channels) ⭐️ 7.8/10

Claude Tag（beta）在 Slack 频道中支持个人连接器，用户可调用自己账号下已连接的日历、云盘、CRM 等服务，此前频道仅能使用管理员挂载的共享连接器。输出可由用户逐条预览，或开启自动模式（Claude 判定敏感时仍需确认），企业版管理员可强制全员审核。该功能正于 Team 计划推出，Enterprise 随后；个人连接器不适用于无人值守任务，定时及自主发起的动作仍依赖管理员连接器。通过个人连接器的操作记录在用户账号下，频道自身操作仍归属服务账号。

rss · Claude Blog · Sep 24, 00:00

**「为什么重要」** 频道内 agent 的权限模型从单一服务账号身份，扩展为「用户身份 + 服务账号身份」混合。个人连接器让 agent 能访问频道成员各自的私有数据，但无人值守任务仍须依赖共享连接器。

**「可关注」** 可关注：个人连接器与共享连接器的审计路径分离。用户通过个人连接器的操作计入其个人账号日志，频道操作留在服务账号日志。若需在频道内运行定时或自主发起的 CI 分诊、值班响应，应为 runbook、监控和部署历史配置共享连接器，个人连接器不覆盖此类场景。

**Tags**: `#product`, `#lab`, `#model`

---