---
layout: default
title: "Horizon Summary: 2026-09-26 (EN)"
date: 2026-09-26
lang: en
---

> From 185 items, 16 important content pieces were selected

---

**Agent Harness Architecture**
1. [Mastra Core 1.71.0 Adds Observability Negotiation](#item-harness-arch-1) ⭐️ 8.8/10
2. [mastra-ai/mastra released @mastra/core@1.70.0](#item-harness-arch-2) ⭐️ 8.8/10
3. [anthropics/claude-code released v2.1.283](#item-harness-arch-3) ⭐️ 8.3/10
4. [Codex rust-v0.157.0 发布](#item-harness-arch-4) ⭐️ 8.3/10
5. [google/adk-python v2.10.0 released](#item-harness-arch-5) ⭐️ 8.3/10
6. [pydantic/pydantic-ai released v2.50.0](#item-harness-arch-6) ⭐️ 7.8/10
7. [stanfordnlp/dspy released 3.4.0](#item-harness-arch-7) ⭐️ 7.8/10

**AI Agent Engineer**
1. [Rufus-Air 开源八阶段后训练配方](#item-agent-engineer-1) ⭐️ 8.0/10
2. [HF 论文：LLM 线性叠加证据](#item-agent-engineer-2) ⭐️ 5.5/10
3. [OmniEchoBench：具身空间音频基准](#item-agent-engineer-3) ⭐️ 5.5/10
4. [AEWM 论文：以状态编辑替代工具模拟](#item-agent-engineer-4) ⭐️ 5.5/10
5. [Qwengram-0.8B 困惑度降 5.05%](#item-agent-engineer-5) ⭐️ 5.5/10

**AI Daily**
1. [Proaction boosts sales 60% and saves 75+ hours with Codex](#item-ai-daily-1) ⭐️ 6.3/10
2. [GitHub Copilot app for Beginners: How to build custom workflows with canvases](#item-ai-daily-2) ⭐️ 6.3/10

**Technology News**
1. [@simonw: I&\#x27;m on stage for the keynote in ten minutes time\!](#item-tech-news-1) ⭐️ 0.0/10
2. [Simon Willison retweets Hillel Wayne on skill and speed](#item-tech-news-2) ⭐️ 0.0/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [Mastra Core 1.71.0 Adds Observability Negotiation](https://github.com/mastra-ai/mastra/releases/tag/%40mastra/core%401.71.0) ⭐️ 8.8/10

Mastra Core 1.71.0 introduces observability capabilities negotiation between storage, server, and client. Servers now expose \`observabilityStorageCapabilities\` via \`GET /system/packages\` and a new \`GET /observability/capabilities\` endpoint, letting Studio detect which observability APIs a configured store supports without forcing storage upgrades. Observability stores can declare supported features through \`getFeatures\(\)\`, including per-endpoint discovery flags for entity, service, environment, tag, and metric discovery. The release also adds \`planTraceAggregate\(\)\`, which validates and converts an \`aggregateTraces\(\)\` request into a \`TrustedTraceAggregatePlan\` that any storage backend can execute without re-validating.

github · PaulieScanlon · Sep 25, 10:07

**「Design Points」** Eager tool execution is now on by default: tools start as soon as their own arguments are complete instead of waiting for the model to finish streaming the whole step, cutting idle time in multi-tool steps. Runs can opt out with \`eagerToolExecution: false\`, and stored agent default options now support the flag; tools that need approval, declare a suspend schema, run on the provider or client, or run in the background still wait for the model to finish.

**「What Changed」** Added \`@mastra/discord\` for connecting agents to Discord and \`@mastra/connect environment\(\)\` to materialize Platform connection credentials into \`\{ env, onStart \}\` for authenticated tooling inside sandbox providers including e2b, Modal, Daytona, Docker, and subprocess. \`MongoDBVector\` now supports Automated Embeddings via \`autoEmbed\` indexes, and dataset schema validation moved regex patterns to a linear-time RE2 engine to close a denial-of-service risk.

**Tags**: `#runtime`, `#eval`, `#planning`, `#memory`

---

<a id="item-harness-arch-2"></a>
### [mastra-ai/mastra released @mastra/core@1.70.0](https://github.com/mastra-ai/mastra/releases/tag/%40mastra/core%401.70.0) ⭐️ 8.8/10

@mastra/core@1.70.0 introduces per-request model routing, cross-process cancellation of queued thread input, and multi-tenant-safe observability scoping.

github · PaulieScanlon · Sep 25, 10:06

**Tags**: `#runtime`, `#planning`, `#memory`, `#permissions`, `#eval`

---

<a id="item-harness-arch-3"></a>
### [anthropics/claude-code released v2.1.283](https://github.com/anthropics/claude-code/releases/tag/v2.1.283) ⭐️ 8.3/10

Claude Code v2.1.283 adds managed model controls, gateway hint headers, OTEL tool-content logging, and a prompt-audit command.

github · ashwin-ant · Sep 25, 21:50

**Tags**: `#runtime`, `#tools`, `#mcp`, `#permissions`, `#eval`

---

<a id="item-harness-arch-4"></a>
### [Codex rust-v0.157.0 发布](https://github.com/openai/codex/releases/tag/rust-v0.157.0) ⭐️ 8.3/10

OpenAI Codex Rust 发布 rust-v0.157.0。新增 GPT-6 Sol 与 Luna 模型，接入 Amazon Bedrock 并提供旧模型迁移提示。交互式会话默认自动启动后台服务，设置不兼容时给出恢复选项；TUI 增加 \`f\` 快捷键分叉正在其他应用打开的会话，保留草稿与排队提示。\`/import\` 扩展到远程会话和本地后台服务会话，终端渲染改用 Unicode 项目符号、复选框并对齐公式与优化记号。

github · github-actions\[bot\] · Sep 25, 02:31

**「设计要点」** 运行时上，符合条件的交互式会话默认拉起 background server/daemon，本地与远程会话统一走 daemon 路径。网络层在代理、重定向和持续 HTTP/WebSocket 流量上执行限制，策略撤销时取消进行中的请求。

**「改了什么」** 相对 rust-v0.156.0，后台服务从手动转为默认自动启动并带不兼容恢复；会话分叉扩展到被其他应用锁定的场景；\`/import\` 覆盖远程与本地 daemon 会话。文件上传超时从 60 秒提高到 5 分钟，并增加瞬时失败重试。

**Tags**: `#runtime`, `#tools`

---

<a id="item-harness-arch-5"></a>
### [google/adk-python v2.10.0 released](https://github.com/google/adk-python/releases/tag/v2.10.0) ⭐️ 8.3/10

google/adk-python v2.10.0 introduces experimental skill lifecycle management, a MongoDB toolset for vector and hybrid search, and new efficiency metrics for agent evaluation. Skill lifecycle features—including ephemeral modes, active-skill caps, and an unload\_skill tool—are disabled by default and require ADK\_ENABLE\_SKILL\_LIFECYCLE=1. The release also adds automated request adaptation and reasoning token reporting for OpenAI reasoning models, and changes BigQuery protected mode to keep sessions in process memory.

github · wyf7107 · Sep 25, 19:00

**「设计要点」** SkillToolset gains programmatic activation APIs and an active-skill cap to dynamically control tool persistence and resource usage. BigQuery protected mode now stores its session in process memory instead of session state, so temporary tables do not survive restarts or carry across replicas.

**「改了什么」** Added experimental skill lifecycle controls \(ephemeral mode, active-skill limit, unload\_skill tool\) behind ADK\_ENABLE\_SKILL\_LIFECYCLE=1. Added a MongoDB toolset supporting vector and hybrid search. Added duration, token consumption, and model call count metrics to ADK eval, and made AgentEvaluator raise ValueError on empty eval sets. Added OpenAI reasoning model parameter adaptation and reasoning token reporting, deprecating thinking\_config in favor of OpenAIGenerateContentConfig.effort.

**Tags**: `#tools`, `#eval`, `#runtime`

---

<a id="item-harness-arch-6"></a>
### [pydantic/pydantic-ai released v2.50.0](https://github.com/pydantic/pydantic-ai/releases/tag/v2.50.0) ⭐️ 7.8/10

pydantic-ai v2.50.0 adds DecisionModel routing abstractions, durable context hooks, and OpenAI service\_tier support with breaking changes to model selection APIs.

github · DouweM · Sep 25, 04:47

**Tags**: `#runtime`, `#planning`, `#tools`

---

<a id="item-harness-arch-7"></a>
### [stanfordnlp/dspy released 3.4.0](https://github.com/stanfordnlp/dspy/releases/tag/3.4.0) ⭐️ 7.8/10

DSPy 3.4.0 adds native LM engines, async ReActV2, and experimental TypeSafe decision types while introducing a deprecation path for legacy LM integrations ahead of 3.5.

github · isaacbmiller · Sep 25, 04:06

**Tags**: `#runtime`, `#tools`, `#eval`, `#planning`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [Rufus-Air 开源八阶段后训练配方](https://huggingface.co/papers/2609.29421) ⭐️ 8.0/10

Rufus-Air 在 GLM-4.5-Air-Base（106B-A12B）上给出开源、可复现的八阶段后训练流程，覆盖 SFT、Reasoning RL、Coding RL、Instruction-Following RL、General Agent、Coding Agent、Search Agent 与 RLHF。论文公开数据、奖励设计、基础设施、阶段顺序及分阶段结果，训练全程使用开源组件与公开数据，未新增人工标注或内部蒸馏教师。阶段从基础能力向高级能力推进，奖励从硬可验证信号过渡到软评判信号。已公开的主要发现包括：多样且高质量的 SFT 建立强能力下限；难度过滤使 RL 提示保持在有效学习区间（原文此处截断）。

rss · Hugging Face Daily Papers · Sep 26, 01:50

**「为什么重要」** 该配方对 coding agent 与 harness 工程师生要，因为它把 Coding Agent、Search Agent 与 RLHF 阶段的数据、奖励与基础设施全部公开，提供了可直接对照的训练与评估管线细节。已发生的变化是文档开放；尚未证实的影响是这些阶段细节能否在自有环境中复现同等效果。

**「可关注」** 可关注：八阶段串行管线中，奖励信号从硬可验证向软评判迁移的顺序，以及难度过滤对 RL 提示分布的控制，可能为自建 agent 后训练提供阶段划分参考。

**Tags**: `#coding-agent`, `#eval`, `#orchestration`

---

<a id="item-agent-engineer-2"></a>
### [HF 论文：LLM 线性叠加证据](https://huggingface.co/papers/2609.29845) ⭐️ 5.5/10

Hugging Face Daily Papers 收录论文《Your Transformer Can Hold Two Thoughts at Once》，提出 Superposition Linearity Hypothesis：当不同文本流的输入被线性组合时，LLM 输出对应 next-token 分布的叠加。论文称该特性是 Transformer 架构的内在属性，而非训练涌现，且随预训练推进而减弱；轻量微调可大幅恢复线性，缩小预测分布与单个分布平均值的差异。论文于 2026-09-26 发布，获 55 次 upvote，属于机制可解释性基础研究，未提供可直接落地的工具或基准。

rss · Hugging Face Daily Papers · Sep 26, 01:50

**「为什么重要」** 对 coding agent / harness 开发者而言，这解释了模型在混合上下文或并行指令下可能出现的分布叠加现象，但论文未验证其对 agent 工作流、工具调用或评测指标的具体影响，暂不能作为工程决策依据。

**「可关注」** 可关注：论文报告轻量微调能显著恢复 Transformer 的线性叠加特性，降低预测分布与平均分布的差异；这一发现与预训练中线性减弱形成张力，但尚未给出对 agent 场景的直接影响。

**Tags**: `#llm`, `#interpretability`, `#transformer`, `#fine-tuning`

---

<a id="item-agent-engineer-3"></a>
### [OmniEchoBench：具身空间音频基准](https://huggingface.co/papers/2609.23407) ⭐️ 5.5/10

HF 每日论文上线 OmniEchoBench，面向具身智能体的空间音频-视觉感知与音频-视觉-语言导航统一基准。基准含 6 项任务、197 个真实场景、2,972 个问答对，以及来自 30 个真实环境、带一阶 Ambisonics（FOA）音频的 900 个导航样本。论文配套可控空间音频渲染管线，用于规模化训练监督。该工作聚焦具身多模态 agent，对主流 coding agent 与通用工具链的直接影响有限。

rss · Hugging Face Daily Papers · Sep 26, 01:50

**「为什么重要」** 空间音频理解此前缺乏统一基准，OmniEchoBench 用具体数据规模和渲染管线补齐了这一环，为具身 agent 的音频-视觉联合推理提供可复现评测起点。但材料明确指出，其影响范围目前集中在具身多模态场景，尚未证明对更广泛的 agent 工程有直接推动作用。

**「可关注」** 可关注：OmniEchoBench 将 FOA 音频与真实视觉场景对齐，并配套可控渲染管线，做具身 agent 或空间感知评测的团队可以参考其几何一致性约束与数据生成方式，但需先判断与自身任务的相关性。

**Tags**: `#eval`, `#benchmark`, `#embodied-agents`

---

<a id="item-agent-engineer-4"></a>
### [AEWM 论文：以状态编辑替代工具模拟](https://huggingface.co/papers/2609.28416) ⭐️ 5.5/10

Hugging Face Daily Papers 于 2026-09-26 收录论文 Agent-Editing World Model（AEWM），主张语言世界模型应建模推理与行动如何塑造任务进度，而非模拟高熵、依赖执行的工具响应。论文提出 Action Judge 区分 Critical、Exploratory 与 Noisy 决策，并用 State Revision 编辑噪声推理与任务状态，以缓解任务状态污染。目前仅见摘要，未公开代码、基准数据或生产 Trace，可验证性与影响面有限。该论文在 HF 获得 13 次 upvote。

rss · Hugging Face Daily Papers · Sep 26, 01:50

**「为什么重要」** 现有语言世界模型多聚焦预测环境观测，AEWM 转向编辑任务状态，直指历史中未支持假设与过时计划对后续决策的扭曲。这一转向若成立，可能改变 agent 在长程任务中的记忆与规划机制，但尚未有实验或代码支撑。

**「可关注」** 可关注：AEWM 用 Action Judge 与 State Revision 替代工具响应模拟，思路区别于主流世界模型，但在缺乏开源实现与基准对比前，不宜作为工程选型依据。

**Tags**: `#memory`, `#eval`, `#orchestration`

---

<a id="item-agent-engineer-5"></a>
### [Qwengram-0.8B 困惑度降 5.05%](https://www.reddit.com/r/LocalLLaMA/comments/1wpvep4/qwengram08b_i_transferred_qwen38_flashnexts_ngram/) ⭐️ 5.5/10

作者 Nicolodeva 报告将 Qwen3.8-Flash-Next 的约 51B 参数 PLE n-gram 记忆迁移至 Qwen3.5-0.8B。主干与 PLE 记忆保持冻结，仅在 decoder 第 3、9 层训练 R=1 reader，并以 token 级线性门控后续注入。冻结全验证集上，NLL 从 2.905585 降至 2.853786，PPL 从 18.2759 降至 17.3534，降幅 5.05%。作者明确这是语言模型验证结果，并非基准测试精度提升。

reddit · r/LocalLLaMA · /u/Nicolodeva · Sep 25, 12:46

**「为什么重要」** 该实验在不微调主干的前提下，用小型 reader 和动态门控复用大模型预训练记忆，为小模型低成本获取长程记忆提供了可复现路径。结果来自单一 Reddit 实验，尚未经独立验证，且作者披露实验开发使用了 coding agents 辅助。

**「可关注」** 可关注：PLE 记忆以外部量化 sidecar 形式与 GGUF 分离部署，以及 Q8\_0 量化在独立 WikiText-2 运行时测试中保留 99.1% BF16 reader NLL 增益的实测，为本地推理集成提供了工程参考。

**Tags**: `#memory`, `#eval`, `#model-architecture`

---

## AI Daily

<a id="item-ai-daily-1"></a>
### [Proaction boosts sales 60% and saves 75+ hours with Codex](https://openai.com/index/proaction) ⭐️ 6.3/10

OpenAI Blog publishes a brief customer case study claiming Proaction boosted sales by 60% and saved over 75 hours using Codex, GPT-Live-1, and GPT-6 Astra.

rss · OpenAI Blog · Sep 25, 19:00

**Tags**: `#model`, `#lab`, `#industry`, `#product`

---

<a id="item-ai-daily-2"></a>
### [GitHub Copilot app for Beginners: How to build custom workflows with canvases](https://github.blog/ai-and-ml/github-copilot/github-copilot-app-for-beginners-how-to-build-custom-workflows-with-canvases/) ⭐️ 6.3/10

GitHub publishes a beginner tutorial on building custom workflows with canvases in the GitHub Copilot app.

rss · GitHub Blog · Sep 25, 18:00

**Tags**: `#product`, `#lab`

---

## Technology News

<a id="item-tech-news-1"></a>
### [@simonw: I&\#x27;m on stage for the keynote in ten minutes time\!](https://twitter.com/simonw/status/tweet-2103641180923978031) ⭐️ 0.0/10

Simon Willison posts that he is about to go on stage for a keynote, without sharing any technical details or news.

twitter · Simon Willison · Sep 26, 00:21

**Tags**: `#social media`, `#personal update`, `#keynote`

---

<a id="item-tech-news-2"></a>
### [Simon Willison retweets Hillel Wayne on skill and speed](https://twitter.com/simonw/status/tweet-2103495582048555120) ⭐️ 0.0/10

Simon Willison retweeted a quote from Hillel Wayne stating, &quot;It doesn&\#x27;t get easier, you just get faster.&quot; The post contains no technical substance, timely news value, or substantive analysis relevant to software engineering, AI, or systems.

twitter · Simon Willison · Sep 25, 14:43

**「Background」** The item is a social media retweet without additional commentary, and the quoted text is a general aphorism about practice and performance rather than a specific technical claim or product update.

**Tags**: `#software engineering`, `#developer productivity`, `#twitter`, `#social media`

---