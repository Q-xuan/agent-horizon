---
layout: default
title: "Horizon Summary: 2026-09-26 (ZH)"
date: 2026-09-26
lang: zh
---

> 从 185 条内容中筛选出 16 条重要资讯。

---

**Harness 架构**
1. [Mastra 1.71.0 发布：能力协商](#item-harness-arch-1) ⭐️ 8.8/10
2. [mastra-ai/mastra released @mastra/core@1.70.0](#item-harness-arch-2) ⭐️ 8.8/10
3. [anthropics/claude-code released v2.1.283](#item-harness-arch-3) ⭐️ 8.3/10
4. [Codex rust-v0.157.0 发布](#item-harness-arch-4) ⭐️ 8.3/10
5. [ADK v2.10.0 技能生命周期与 MongoDB 工具集](#item-harness-arch-5) ⭐️ 8.3/10
6. [pydantic/pydantic-ai released v2.50.0](#item-harness-arch-6) ⭐️ 7.8/10
7. [stanfordnlp/dspy released 3.4.0](#item-harness-arch-7) ⭐️ 7.8/10

**Agent 工程师日报**
1. [Rufus-Air 开源 8 阶段后训练配方](#item-agent-engineer-1) ⭐️ 8.0/10
2. [论文称 Transformer 具线性叠加特性](#item-agent-engineer-2) ⭐️ 5.5/10
3. [OmniEchoBench：具身智能体音频基准](#item-agent-engineer-3) ⭐️ 5.5/10
4. [AEWM 论文：以状态编辑替代模拟工具响应](#item-agent-engineer-4) ⭐️ 5.5/10
5. [Qwengram-0.8B 迁移 PLE 记忆降 5.05% 困惑度](#item-agent-engineer-5) ⭐️ 5.5/10

**AI 日报**
1. [Proaction boosts sales 60% and saves 75+ hours with Codex](#item-ai-daily-1) ⭐️ 6.3/10
2. [GitHub Copilot app for Beginners: How to build custom workflows with canvases](#item-ai-daily-2) ⭐️ 6.3/10

**科技新闻**
1. [@simonw: I&\#x27;m on stage for the keynote in ten minutes time\!](#item-tech-news-1) ⭐️ 0.0/10
2. [Simon Willison 转发技能习得格言](#item-tech-news-2) ⭐️ 0.0/10

---

## Harness 架构

<a id="item-harness-arch-1"></a>
### [Mastra 1.71.0 发布：能力协商](https://github.com/mastra-ai/mastra/releases/tag/%40mastra/core%401.71.0) ⭐️ 8.8/10

Mastra 1.71.0 发布，重点在可观测性存储的能力协商与查询规划。服务器新增 \`GET /observability/capabilities\`，存储端通过 \`getFeatures\(\)\` 声明支持的发现与反馈接口，Studio 据此调用兼容端点。新增 \`planTraceAggregate\(\)\`，把 \`aggregateTraces\(\)\` 请求校验并转换为 \`TrustedTraceAggregatePlan\`，后端直接执行。工具执行默认改为参数就绪即启动，减少多工具步骤的空闲时间。

github · PaulieScanlon · 9月25日 10:07

**「设计要点」** 可观测性存储用 \`getFeatures\(\)\` 声明能力，服务器通过 \`GET /observability/capabilities\` 暴露给客户端；不支持的发现路由返回空结果而非 500。\`planTraceAggregate\(\)\` 统一校验 \`timeRange\`、\`groupBy\`、\`having\`、\`orderBy\` 与桶数限制，错误码与 \`planTraceQuery\(\)\` 一致。

**「改了什么」** 新增存储能力协商端点与 \`getFeatures\(\)\` 发现声明；\`planTraceAggregate\(\)\` 提供聚合查询规划；工具执行默认改为 eager 模式；数据集 schema 正则切换到 RE2 引擎，拒绝 lookaround 与 backreference。

**标签**: `#runtime`, `#eval`, `#planning`, `#memory`

---

<a id="item-harness-arch-2"></a>
### [mastra-ai/mastra released @mastra/core@1.70.0](https://github.com/mastra-ai/mastra/releases/tag/%40mastra/core%401.70.0) ⭐️ 8.8/10

@mastra/core@1.70.0 introduces per-request model routing, cross-process cancellation of queued thread input, and multi-tenant-safe observability scoping.

github · PaulieScanlon · 9月25日 10:06

**标签**: `#runtime`, `#planning`, `#memory`, `#permissions`, `#eval`

---

<a id="item-harness-arch-3"></a>
### [anthropics/claude-code released v2.1.283](https://github.com/anthropics/claude-code/releases/tag/v2.1.283) ⭐️ 8.3/10

Claude Code v2.1.283 adds managed model controls, gateway hint headers, OTEL tool-content logging, and a prompt-audit command.

github · ashwin-ant · 9月25日 21:50

**标签**: `#runtime`, `#tools`, `#mcp`, `#permissions`, `#eval`

---

<a id="item-harness-arch-4"></a>
### [Codex rust-v0.157.0 发布](https://github.com/openai/codex/releases/tag/rust-v0.157.0) ⭐️ 8.3/10

OpenAI Codex Rust 实现发布 rust-v0.157.0。新增 GPT-6 Sol 与 Luna 模型，接入 Amazon Bedrock，并为旧模型提供迁移提示。符合条件的交互式会话默认启用后台服务器自动启动，设置不兼容时提供显式恢复选项；TUI 新增 \`f\` 快捷键分叉被其他应用锁定的对话，保留草稿与排队提示。\`/import\` 扩展至远程会话和本地 daemon 会话，终端渲染加入 Unicode 项目符号、复选框与对齐公式。

github · github-actions\[bot\] · 9月25日 02:31

**「设计要点」** 后台 daemon 自动启动与不兼容时的显式恢复路径，以及跨重定向和 WebSocket 的网络策略强制执行，构成运行时与权限层的主要调整。

**「改了什么」** 默认开启全屏转录与后台 daemon 自动启动。新增 \`f\` 快捷键分叉被其他应用锁定的对话，保留草稿与排队提示。\`/import\` 从本地扩展到远程和本地 daemon 会话。模型侧新增 GPT-6 Sol/Luna 与 Bedrock 支持。

**标签**: `#runtime`, `#tools`

---

<a id="item-harness-arch-5"></a>
### [ADK v2.10.0 技能生命周期与 MongoDB 工具集](https://github.com/google/adk-python/releases/tag/v2.10.0) ⭐️ 8.3/10

google/adk-python v2.10.0 发布。新增实验性技能生命周期管理，通过 \`ADK\_ENABLE\_SKILL\_LIFECYCLE=1\` 启用 ephemeral 模式与 active skill 上限，控制工具持久化与资源占用。引入 MongoDB toolset，支持向量与混合检索。评测框架加入 duration、token 消耗与模型调用次数指标。OpenAI 推理模型接入增加请求参数自动适配与 reasoning token 上报。

github · wyf7107 · 9月25日 19:00

**「设计要点」** SkillToolset 增加生命周期模式与激活上限，卸载技能时同步丢弃其指令，属于工具层的动态加载设计。BigQuery protected mode 将 BigQuery session 移至进程内存而非 session state，临时表不再跨重启或副本存活。

**「改了什么」** 相对 v2.9.2，SkillToolset 支持 ephemeral 生命周期、主动卸载工具与激活数量上限；新增 MongoDB toolset；eval 增加效率指标；OpenAIResponsesLlm 弃用 \`thinking\_config\`，改用 \`OpenAIGenerateContentConfig.effort\`；AgentEvaluator 在无用例时抛 \`ValueError\`。

**标签**: `#tools`, `#eval`, `#runtime`

---

<a id="item-harness-arch-6"></a>
### [pydantic/pydantic-ai released v2.50.0](https://github.com/pydantic/pydantic-ai/releases/tag/v2.50.0) ⭐️ 7.8/10

pydantic-ai v2.50.0 adds DecisionModel routing abstractions, durable context hooks, and OpenAI service\_tier support with breaking changes to model selection APIs.

github · DouweM · 9月25日 04:47

**标签**: `#runtime`, `#planning`, `#tools`

---

<a id="item-harness-arch-7"></a>
### [stanfordnlp/dspy released 3.4.0](https://github.com/stanfordnlp/dspy/releases/tag/3.4.0) ⭐️ 7.8/10

DSPy 3.4.0 adds native LM engines, async ReActV2, and experimental TypeSafe decision types while introducing a deprecation path for legacy LM integrations ahead of 3.5.

github · isaacbmiller · 9月25日 04:06

**标签**: `#runtime`, `#tools`, `#eval`, `#planning`

---

## Agent 工程师日报

<a id="item-agent-engineer-1"></a>
### [Rufus-Air 开源 8 阶段后训练配方](https://huggingface.co/papers/2609.29421) ⭐️ 8.0/10

Hugging Face 每日论文推荐 Rufus-Air，一套面向 GLM-4.5-Air-Base（106B-A12B）的开源可复现后训练配方，目前获得 7 次点赞。配方由 SFT、Reasoning RL、Coding RL、Instruction-Following RL、General Agent、Coding Agent、Search Agent 和 RLHF 共 8 个阶段串行组成，论文公开了数据、奖励设计、基础设施与各阶段结果。训练基于开源组件与公开数据，未引入新人工标注或内部蒸馏教师，阶段从基础能力推进到高级能力，奖励从硬可验证信号过渡到软评判信号。主要发现包括多样高质量 SFT 奠定能力下限，以及难度过滤使 RL 提示保持在有效区间。

rss · Hugging Face Daily Papers · 9月26日 01:50

**「为什么重要」** 该配方完整公开从 SFT 到 RLHF 的 8 阶段流程、奖励设计与基础设施，且不依赖新人工标注或内部蒸馏教师。对 agent 工程师而言，Coding Agent、Search Agent 和 RLHF 阶段提供了可直接参考的训练与评估管线细节。

**「可关注」** 可关注：Rufus-Air 将 Agent 训练拆为 General Agent、Coding Agent、Search Agent 等独立阶段，并采用从硬可验证奖励到软评判信号的渐进策略，为 agent 后训练提供了可复用的阶段划分与奖励设计参照。

**标签**: `#coding-agent`, `#eval`, `#orchestration`

---

<a id="item-agent-engineer-2"></a>
### [论文称 Transformer 具线性叠加特性](https://huggingface.co/papers/2609.29845) ⭐️ 5.5/10

2026-09-26，Hugging Face Daily Papers 收录一篇机制可解释性论文，提出「Superposition Linearity Hypothesis」。论文称，尽管 LLM 依赖高度非线性组件，但当两路不同文本流的输入被线性组合时，模型输出会呈现单路 next-token 分布的叠加。作者认为该特性是 Transformer 架构的内在属性，而非训练涌现；且随预训练推进而减弱，但可通过轻量微调显著恢复，降低预测分布与单路分布均值之间的散度。论文未提供面向 agent、harness 或评测的工具与基准变更。

rss · Hugging Face Daily Papers · 9月26日 01:50

**「为什么重要」** 该研究为理解 Transformer 的线性行为提供了架构层面的证据，可能影响后续对模型内部表示与微调策略的讨论。但论文属于基础模型行为分析，尚未给出可直接落地的工程方案，对 AI Agent 工程师的即时价值有限。

**「可关注」** 可关注：论文指出线性叠加是 Transformer 架构内在属性且随预训练减弱，后续可在自有模型上复现轻量微调恢复线性度的实验，再评估其对 agent 场景的实际意义。

**标签**: `#llm`, `#interpretability`, `#transformer`, `#fine-tuning`

---

<a id="item-agent-engineer-3"></a>
### [OmniEchoBench：具身智能体音频基准](https://huggingface.co/papers/2609.23407) ⭐️ 5.5/10

Hugging Face Daily Papers 收录论文 OmniEcho，提出空间音频-视觉基准 OmniEchoBench。该基准面向具身智能体，包含 6 个任务、197 个真实世界空间音频-视觉场景、2,972 个问答对，以及来自 30 个真实环境的 900 个带一阶 ambisonics（FOA）音频的导航样本。论文同时给出可控空间音频渲染管线，用于生成训练监督并保持几何一致性。其影响范围集中于具身多模态智能体，对主流 coding agent、harness 及通用工具链的相关性有限。

rss · Hugging Face Daily Papers · 9月26日 01:50

**「为什么重要」** 具身智能体在空间音频理解上长期缺乏统一评测，OmniEchoBench 提供了带真实场景和可控渲染管线的具体基线。不过，该工作尚未覆盖主流编码智能体或通用工具链场景。

**「可关注」** 可关注：OmniEchoBench 以 197 个真实场景、2,972 个问答对和 900 个 FOA 导航样本，为具身智能体的空间音频理解提供了可量化基线；其可控渲染管线也展示了合成训练监督的可行路径，但适用范围仍限于具身多模态场景。

**标签**: `#eval`, `#benchmark`, `#embodied-agents`

---

<a id="item-agent-engineer-4"></a>
### [AEWM 论文：以状态编辑替代模拟工具响应](https://huggingface.co/papers/2609.28416) ⭐️ 5.5/10

Hugging Face Daily Papers 收录论文 Agent-Editing World Model（AEWM）。论文认为，真实反馈可得时，重建高熵、依赖执行的工具响应价值有限，主张建模推理与行动如何塑造任务进度。AEWM 结合 Action Judge 区分 Critical、Exploratory 与 Noisy 决策，并用 State Revision 编辑噪声推理，缓解任务状态污染。目前仅见摘要，无开源代码、基准数据或生产 Trace，影响面待验证。

rss · Hugging Face Daily Papers · 9月26日 01:50

**「为什么重要」** 现有语言世界模型多聚焦预测环境观测，AEWM 把建模对象换成任务进度与状态编辑，为长程 Agent 的记忆与规划提供另一条路径。不过论文尚未公开代码与实验，实际效果仍待社区复核。

**「可关注」** 可关注：若工具响应已能实时获取，世界模型是否还应消耗算力去模拟它；AEWM 将编辑噪声推理作为替代方向，但缺乏可复现基线，暂不宜直接接入生产流程。

**标签**: `#memory`, `#eval`, `#orchestration`

---

<a id="item-agent-engineer-5"></a>
### [Qwengram-0.8B 迁移 PLE 记忆降 5.05% 困惑度](https://www.reddit.com/r/LocalLLaMA/comments/1wpvep4/qwengram08b_i_transferred_qwen38_flashnexts_ngram/) ⭐️ 5.5/10

Reddit 用户 Nicolodeva 将 Qwen3.8-Flash-Next 的约 51B 参数预训练 PLE n-gram 记忆迁移进 Qwen3.5-0.8B，得到 Qwengram-0.8B。主干与 PLE 均冻结，仅在解码器第 3、9 层训练 R=1 reader，并以 token 依赖线性门控动态注入。冻结全验证集上，NLL 从 2.905585 降至 2.853786，PPL 从 18.2759 降至 17.3534，降幅 5.05%。作者说明这是语言模型验证结果，非基准测试准确率提升；20M reader 虽进一步降低总体 loss 但数学退化，15M 为平衡检查点。

reddit · r/LocalLLaMA · /u/Nicolodeva · 9月25日 12:46

**「为什么重要」** 实验证明预训练 PLE 记忆可跨规模迁移，并在 llama.cpp 中提供可复现的推理路径与量化保留数据。不过这是模型层验证结果，对 agent 工程的影响仍属间接且未经下游任务证实。

**「可关注」** 可关注：动态 token 级门控在记忆注入中比固定注入更能平衡总体 loss 与 LAMBADA，且相同记忆预算下学习到的 token 放置优于随机放置。

**标签**: `#memory`, `#eval`, `#model-architecture`

---

## AI 日报

<a id="item-ai-daily-1"></a>
### [Proaction boosts sales 60% and saves 75+ hours with Codex](https://openai.com/index/proaction) ⭐️ 6.3/10

OpenAI Blog publishes a brief customer case study claiming Proaction boosted sales by 60% and saved over 75 hours using Codex, GPT-Live-1, and GPT-6 Astra.

rss · OpenAI Blog · 9月25日 19:00

**标签**: `#model`, `#lab`, `#industry`, `#product`

---

<a id="item-ai-daily-2"></a>
### [GitHub Copilot app for Beginners: How to build custom workflows with canvases](https://github.blog/ai-and-ml/github-copilot/github-copilot-app-for-beginners-how-to-build-custom-workflows-with-canvases/) ⭐️ 6.3/10

GitHub publishes a beginner tutorial on building custom workflows with canvases in the GitHub Copilot app.

rss · GitHub Blog · 9月25日 18:00

**标签**: `#product`, `#lab`

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [@simonw: I&\#x27;m on stage for the keynote in ten minutes time\!](https://twitter.com/simonw/status/tweet-2103641180923978031) ⭐️ 0.0/10

Simon Willison posts that he is about to go on stage for a keynote, without sharing any technical details or news.

twitter · Simon Willison · 9月26日 00:21

**标签**: `#social media`, `#personal update`, `#keynote`

---

<a id="item-tech-news-2"></a>
### [Simon Willison 转发技能习得格言](https://twitter.com/simonw/status/tweet-2103495582048555120) ⭐️ 0.0/10

Simon Willison 转发了一条 @hillelogram 的帖子，其中引用了他的一句话：“It doesn&\#x27;t get easier, you just get faster.” 该内容是一则关于技能习得的励志格言，不包含任何技术细节、产品发布或实质性分析，也没有提供有关软件工程、AI 或系统的新闻价值。

twitter · Simon Willison · 9月25日 14:43

**「背景」** 该推文是 Simon Willison 对 @hillelogram 一条引述自己言论的帖子的转发。这句话反映了技术工作中一种常见的观点，即专业能力的提升体现在速度加快，而非任务本身变得更容易。

**标签**: `#software engineering`, `#developer productivity`, `#twitter`, `#social media`

---