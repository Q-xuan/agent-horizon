---
layout: default
title: "Horizon Summary: 2026-11-03 (EN)"
date: 2026-11-03
lang: en
---

> From 181 items, 16 important content pieces were selected

---

**Agent Harness Architecture**
1. [ADK Go v2.7.0 发布](#item-harness-arch-1) ⭐️ 8.8/10
2. [Mastra Core 1.81.0 发布](#item-harness-arch-2) ⭐️ 7.8/10
3. [pydantic-ai v2.65.0 发布](#item-harness-arch-3) ⭐️ 6.8/10
4. [微软 mcp-for-beginners 开源](#item-harness-arch-4) ⭐️ 5.0/10

**AI Agent Engineer**
1. [TinyAstral 两阶段自进化 harness 蒸馏](#item-agent-engineer-1) ⭐️ 7.0/10
2. [HF 论文：ReTrace 评估智能体恢复](#item-agent-engineer-2) ⭐️ 7.0/10
3. [ProVe 提出者-验证者推测解码](#item-agent-engineer-3) ⭐️ 7.0/10
4. [OpenAI Scaling Git 发布](#item-agent-engineer-4) ⭐️ 7.0/10
5. [llm 0.37 发布：多模态嵌入与端点管理](#item-agent-engineer-5) ⭐️ 6.0/10
6. [HF 论文：ReGap-Bench 多模态推理基准](#item-agent-engineer-6) ⭐️ 6.0/10
7. [ISTA 发布 DeepSeek-V4.1-Flash-1017 1bpp Coder 剪枝版](#item-agent-engineer-7) ⭐️ 5.5/10

**AI Daily**
1. [OpenAI 提高漏洞赏金并新增奖金](#item-ai-daily-1) ⭐️ 8.8/10
2. [OpenAI 发布 LifeVal 基准测试](#item-ai-daily-2) ⭐️ 8.8/10
3. [OpenAI 发布 Pando Git 后端](#item-ai-daily-3) ⭐️ 7.8/10
4. [OpenAI 推出电网保护者计划](#item-ai-daily-4) ⭐️ 7.8/10
5. [OpenAI 联合 Cathedral Systems 开展安全冲刺](#item-ai-daily-5) ⭐️ 6.8/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [ADK Go v2.7.0 发布](https://github.com/google/adk-go/releases/tag/v2.7.0) ⭐️ 8.8/10

Google ADK Go v2.7.0 introduces Anthropic Claude as a first-party model, search-gated tool discovery for large MCP catalogs, an experimental classifier API for workflow routing, and per-invocation model call budgets. Telemetry switches to OpenTelemetry GenAI semantic conventions v2 by default, breaking existing trace consumers. Go 1.26.10 is required.

github · wolo-lab · Nov 2, 10:37

**「设计要点」** Search-gated tool discovery defers large MCP catalog expansion until the model requests tools, reducing per-request token overhead. Telemetry now emits structured gen\_ai spans with one inference event per model call, replacing legacy log events and JSON-string message content.

**「改了什么」** Added Anthropic Claude model support via model/anthropicmodel, search-gated tool discovery via tool/toolsearch, and an experimental classifier API in exp/classifier. Added RunConfig.MaxLLMCalls defaulting to 500. Telemetry now defaults to OpenTelemetry GenAI semantic conventions v2. Fixed auth.ADC and auth.ServiceAccount token minting context cancellation. Added per-user MCP sessions when Config.Auth is set.

**Tags**: `#tools`, `#runtime`, `#mcp`, `#planning`

---

<a id="item-harness-arch-2"></a>
### [Mastra Core 1.81.0 发布](https://github.com/mastra-ai/mastra/releases/tag/%40mastra/core%401.81.0) ⭐️ 7.8/10

Mastra Core 1.81.0 正式发布，核心新增三项运行时与可观测性能力，同时包含多项破坏性 API 变更。实验性存储支持的 MCP 任务实现重启安全的长任务执行，支持跨实例轮询、应答、取消及状态恢复。后台任务扩展至非 Agent 所有者，新增 per-task 过期时间、元数据保留、所有者级并发覆盖及无槽位排队恢复能力。可观测性新增执行结果、类型化停止原因、模型/提供商导出及首 token 耗时（TTFT）测量，支持 ClickHouse、DuckDB、Postgres 等主流存储的查询与分组。

github · PaulieScanlon · Nov 2, 12:33

**「设计要点」** 存储-backed MCP 任务依赖共享存储实现跨实例状态持久与重启恢复；后台任务新增的过期、元数据等字段由存储适配器统一持久化；可观测性字段原生支持多存储查询聚合，无需额外适配层。

**「改了什么」** 相对上一版本新增多项能力并调整部分 API：新增实验性存储支持的 MCP 长任务、非 Agent 所有者可用的后台任务（含保留/并发/排队恢复能力）、可观测性结果/停止原因/TTFT 测量及多存储查询支持；同时包含破坏性变更：\`@mastra/playground-ui\` 清理 Metrics 图表 API、移除 fluid-hover 工具与 \`CommandList.highlightClassName\`，\`@mastra/core\` 移除 \`@mastra/core/network/vNext\` 与 \`@mastra/core/telemetry/otel-vendor\` 子路径，\`@mastra/factory\` 废弃 \`defineBoard\(\)\` 及 \`boards\`/\`includeDefaultBoards\` 字段，需迁移至存储化 boards API 与新字段命名。

**Tags**: `#mcp`, `#runtime`, `#tools`, `#subagents`, `#eval`

---

<a id="item-harness-arch-3"></a>
### [pydantic-ai v2.65.0 发布](https://github.com/pydantic/pydantic-ai/releases/tag/v2.65.0) ⭐️ 6.8/10

pydantic-ai v2.65.0 发布，带来运行时行为调整与工具功能增量。ModelFallback 在模型拒绝时自动回退，Z.ai 配额超限错误类型从 ModelRateLimitError 改为 ModelQuotaExceededError，Temporal 默认停止重试不可恢复的模型错误。工具层新增 BrowserUse 用量统计、AskUserAnswer 多模态支持、ConversationStore 消息日志存储，以及 OpenAI Responses WebSocket 传输。同时包含 Daytona 依赖升级至 &gt;=0.226.1 等破坏性变更。

github · dsfaccini · Nov 3, 01:25

**「设计要点」** 无核心架构改动。运行时通过 non\_retryable\_model\_errors 控制 Temporal 重试边界，工具层事件通过 PrefixTools 统一转发，ConversationStore 以单写日志形式管理对话历史并支持 revision 冲突检测。

**「改了什么」** ModelFallback 对模型拒绝触发回退并扩展 fallback\_on 匹配范围；Z.ai 429 错误分类调整；Temporal 默认不重试模型错误。BrowserUse 调用计入 UsageLimits；AskUserAnswer 支持多模态输入；新增 ConversationStore 与 Conversation.revision；OpenAI Responses 支持 WebSocket 传输与 12h 提示缓存；Daytona 依赖要求提升至 &gt;=0.226.1。

**「评论」** 无社区评论。

**Tags**: `#runtime`, `#tools`

---

<a id="item-harness-arch-4"></a>
### [微软 mcp-for-beginners 开源](https://github.com/microsoft/mcp-for-beginners) ⭐️ 5.0/10

微软在 GitHub Trending 开源了面向初学者的 MCP 入门课程 \`microsoft/mcp-for-beginners\`。该课程通过 .NET、Java、TypeScript、JavaScript、Rust 和 Python 六种语言的真实示例，讲解 Model Context Protocol 基础。内容聚焦模块化、可扩展且安全的 AI 工作流构建，覆盖从会话建立到服务编排的完整流程。此资源仅作学习参考，未涉及现有 agent harness 的架构变更或协议更新。

rss · GitHub Trending Daily · Nov 3, 03:48

**Tags**: `#mcp`, `#tools`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [TinyAstral 两阶段自进化 harness 蒸馏](https://huggingface.co/papers/2610.41216) ⭐️ 7.0/10

2026-11-03，Hugging Face Daily Papers 收录论文《TinyAstral: Transferring Self-Evolving Harnesses to Tiny Generalist Manipulation Agents》，提出两阶段方法将大模型教师的 harness 改进迁移至紧凑型操作智能体：第一阶段冻结教师模型，通过递归自改进（RSI）进化 harness，前沿 LLM 智能体读取教师轨迹并提出 harness 编辑，仅当编辑通过配对统计检验时才被接受；第二阶段冻结最终 harness，收集含推理与故障恢复的教师轨迹，蒸馏小规模学生智能体以在相同 harness 中替换教师。该方法在 RoboTwin 基准评估，但原文截断，具体成功率数字缺失。

rss · Hugging Face Daily Papers · Nov 3, 00:00

**「为什么重要」** 该工作证明 harness 层面的改进可通过统计验证机制迁移，而非仅依赖模型权重蒸馏，为降低智能体推理成本提供新路径。但迁移效果是否泛化至其他机器人任务或软件工具场景尚未证实。

**「可关注」** 可关注：harness 编辑的配对统计检验机制可能为工具链优化提供可验证的自动化路径，避免直接蒸馏带来的策略丢失。

**Tags**: `#harness`, `#eval`, `#orchestration`

---

<a id="item-agent-engineer-2"></a>
### [HF 论文：ReTrace 评估智能体恢复](https://huggingface.co/papers/2610.27954) ⭐️ 7.0/10

2026年11月3日Hugging Face Daily Papers发布论文摘要，介绍可扩展评估框架ReTrace，用于系统研究长时序计算机使用智能体的故障恢复行为，对智能体评测、工具链及计算机使用智能体开发有直接参考价值。现有恢复方案存在明显不足：专有场景下环境重置不可行、长时序动作回放成本极高、API回滚仅适用于Web环境，ReTrace填补了该领域研究空白。当前公开的摘要内容截断，未包含完整技术细节、实验验证数据与框架使用方法。

rss · Hugging Face Daily Papers · Nov 3, 00:00

**「为什么重要」** 该框架的提出填补了计算机使用智能体恢复能力评估的研究空白，为相关开发与评测提供了新的思路。但目前公开内容仅为截断摘要，完整技术细节、实验效果与框架可用性尚未披露，实际落地价值仍需后续验证。

**「可关注」** 可关注：ReTrace 针对长时序计算机使用智能体的恢复能力评估填补了现有方案空白，后续可跟进其完整技术细节与实验数据。

**Tags**: `#eval`, `#coding-agent`, `#harness`

---

<a id="item-agent-engineer-3"></a>
### [ProVe 提出者-验证者推测解码](https://huggingface.co/papers/2610.27815) ⭐️ 7.0/10

2026-11-03，Hugging Face Daily Papers 收录 ProVe（Proposer-Verifier Decoding）论文。该方案反转传统推测解码分工：将大语言模型微调为提议者，单次前向传播输出一整块 token，再由验证者（较小 AR 模型或提议者自身）并行验证。当验证者为提议者自身时，ProVe-lossless 模式可复现原模型贪婪 AR 解码。论文报告，块大小设为 16 时，GSM8K 上提议块平均包含 6.6 个与 AR 匹配的前缀 token；另在六个基准测试中使用 32B 参数模型作为提议者（原文截断，未披露完整结果）。该工作面向 LLM 推理加速，目前仅提供初步基准验证。

rss · Hugging Face Daily Papers · Nov 3, 00:00

**「为什么重要」** ProVe 允许用单一模型同时完成提议与验证，理论上可减少对外部 draft 模型的依赖。但材料仅展示初步 benchmark，未给出延迟、吞吐量或长序列下的实际加速比，生产价值尚未证实。

**「可关注」** 可关注：块大小与 AR 匹配前缀长度的关系（如 GSM8K 上 16 块对应 6.6 token 前缀）如何随任务类型变化，这直接影响并行验证的有效 token 比例。

**Tags**: `#eval`, `#llm-inference`, `#speculative-decoding`

---

<a id="item-agent-engineer-4"></a>
### [OpenAI Scaling Git 发布](https://openai.com/index/scaling-git-at-openai/) ⭐️ 7.0/10

OpenAI 于 2026-11-03 发布工程博客《Scaling Git at OpenAI》，讨论大规模内部代码库的 Git 扩展策略。该文来自 OpenAI 工程团队，对构建依赖 Git 操作的 coding agent 与 harness 具有潜在参考价值。当前材料未包含具体技术实现、性能数据或限制条件。

rss · Lobsters · Nov 3, 02:18

**「为什么重要」** Git 操作是 coding agent 与 harness 工具链的基础组件。OpenAI 公开其内部大规模 Git 实践经验，可能为相关系统优化提供生产级参考。但具体方案的可复用性及效果需以全文内容为准。

**Tags**: `#coding-agent`, `#harness`

---

<a id="item-agent-engineer-5"></a>
### [llm 0.37 发布：多模态嵌入与端点管理](https://simonwillison.net/2026/Nov/2/llm/) ⭐️ 6.0/10

llm 0.37 于 2026-11-02 发布，新增 gpt-6.1-sol、gpt-6.1-terra 与 chat-latest 模型，并新增 \`llm openai endpoint add\`、\`list\`、\`remove\`、\`path\` 命令管理 OpenAI 兼容端点（存储于 extra-openai-models.yaml）。默认模型从 gpt-5.6-luna 切换为价格减半的 gpt-6-luna。嵌入功能支持带 MIME 类型的附件（文本、音频、图像、视频），\`llm embed\`、\`llm embed-multi\` 与 \`llm similar\` 新增 \`-a/--attachment\` 与 \`--at/--attachment-type\` 选项，向量集合新增 \`content\_type\` 列。本次更新移除已停用的 OpenAI 模型（如 gpt-3.5-turbo、gpt-4、o1 等），支持 Python 3.15 并放弃 Python 3.10，同时修复日志、工具链、UTF-8 编码与 SQLITE\_BUSY 等错误。

rss · Simon Willison · Nov 2, 23:49

**「为什么重要」** OpenAI 兼容端点管理简化了多模型配置，多模态嵌入使 agent 能直接处理图像、音频等非文本输入，工具链日志与链限制的修复则关系到长任务稳定性。

**「可关注」** 可关注：\`llm openai endpoint add\` 提供了一种无需插件即可接入 OpenAI 兼容模型的便捷方式；\`chain.on\_response\(callback\)\` 允许在每次响应完成后注入自定义逻辑，可用于工具调用审计或拦截。

**Tags**: `#harness`, `#memory`

---

<a id="item-agent-engineer-6"></a>
### [HF 论文：ReGap-Bench 多模态推理基准](https://huggingface.co/papers/2610.39419) ⭐️ 6.0/10

2026年11月3日Hugging Face每日论文收录了针对多模态推理参考缺口的研究，该研究提出成对多模态推理基准ReGap-Bench，覆盖5类视觉推理任务，固定场景、问题与答案，仅变化视觉参考类型。实验显示，与任务匹配的视觉参考（如编号标注）可将模型准确率提升最多25%，不匹配的参考几乎无收益甚至降低表现。该基准为多模态推理场景的模型评估与优化提供了可复用的工具，主要面向多模态agent相关工程师，其结论目前不覆盖主流代码agent或工具链优化场景。

rss · Hugging Face Daily Papers · Nov 3, 00:00

**「为什么重要」** 该研究提供了视觉参考对齐影响多模态推理准确率的可量化证据，以及控制变量严谨的公开基准，方便工程师做针对性优化。但目前结论仅验证于5类视觉推理任务，对更广泛的多模态场景、代码类agent的适用性尚未证实。

**「可关注」** 可关注：在构建或评估多模态推理agent时，可优先用ReGap-Bench验证视觉参考类型与任务的匹配度，避免不匹配的参考引入额外误差。

**Tags**: `#eval`

---

<a id="item-agent-engineer-7"></a>
### [ISTA 发布 DeepSeek-V4.1-Flash-1017 1bpp Coder 剪枝版](https://www.reddit.com/r/LocalLLaMA/comments/1xlys6k/release_ista_deepseekv41flash1017_gsqrco_coder_a/) ⭐️ 5.5/10

2026年11月2日，ISTA DASLab在Reddit r/LocalLLaMA发布DeepSeek-V4.1-Flash-1017的Coder剪枝量化版本，采用GSQ与RCO技术，每层保留192/384个路由专家，总参数量763.2B，其中transformer权重551.9B，剪枝后transformer权重体积72.1GB，按原始transformer参数量计算等效1.05比特每参数（四舍五入为1），保留的2801亿个参数平均存储为2.06比特，移除的专家参数计为0比特。公开基准显示该版本LiveCodeBench v6得分88.57，为基础版的98.7%；SWE-bench Verified得分77.00，为基础版的94.8%。该版本为实验性发布，需llama.cpp b11870及以上版本或Strata运行，面向本地编码Agent构建者，共享的110.6GB Engram文件与视觉投影仪与未剪枝版通用无需重复下载。

reddit · r/LocalLLaMA · /u/Loginhe · Nov 2, 14:33

**「为什么重要」** 这是目前公开首个将DeepSeek-V4.1-Flash-1017 Coder压缩至等效1比特每参数的本地可部署版本，大幅降低了本地运行的存储与显存门槛；但目前仅公开了代码生成与长Agent轨迹的有限基准数据，未覆盖更多实际编码场景的能力验证，且仍处于实验阶段。

**「可关注」** 可关注：该剪枝版在长Agent轨迹任务上的能力保留率低于单轮代码生成，且需llama.cpp b11870及以上版本才可运行。

**Tags**: `#coding-agent`

---

## AI Daily

<a id="item-ai-daily-1"></a>
### [OpenAI 提高漏洞赏金并新增奖金](https://openai.com/index/rewarding-defenders-with-bigger-bug-bounties) ⭐️ 8.8/10

OpenAI 于 2026-11-02 更新安全漏洞赏金计划，提高基础赏金，并为独立安全研究人员新增报告质量、忠诚度、优先活动三类奖金。具体赏金数额、漏洞类型范围及奖金发放细则未在材料中披露。

rss · OpenAI Blog · Nov 2, 18:00

**「为什么重要」** 作为头部 AI 实验室，OpenAI 此次系统性地将质量与忠诚度纳入赏金激励，可能重塑行业对安全研究资源的分配逻辑。

**「可关注」** 可关注：报告质量评估标准、忠诚度奖励计算方式及优先活动覆盖范围尚未公开。

**Tags**: `#lab`, `#policy`, `#industry`

---

<a id="item-ai-daily-2"></a>
### [OpenAI 发布 LifeVal 基准测试](https://openai.com/index/lifeval) ⭐️ 8.8/10

OpenAI 发布 LifeVal 基准测试，用于评估 AI 系统协助用户完成日常任务的能力。测试覆盖托儿所查找、财务管理、政府文件处理等真实场景。

rss · OpenAI Blog · Nov 2, 09:00

**Tags**: `#eval`, `#lab`

---

<a id="item-ai-daily-3"></a>
### [OpenAI 发布 Pando Git 后端](https://openai.com/index/scaling-git-at-openai) ⭐️ 7.8/10

OpenAI 官方博客发布文章，介绍其构建的 Git 兼容后端 Pando。该系统专为支撑 Codex 所实现的大规模开发而设计。

rss · OpenAI Blog · Nov 2, 15:30

**Tags**: `#product`, `#lab`

---

<a id="item-ai-daily-4"></a>
### [OpenAI 推出电网保护者计划](https://openai.com/index/grid-protectors-program) ⭐️ 7.8/10

OpenAI 宣布推出 Grid Protectors Program（电网保护者计划），将与电力公司开展合作。该计划旨在为未来的 AI 算力园区提供电网可靠性支持，同时保护消费者的用电成本。

rss · OpenAI Blog · Nov 2, 15:00

**「为什么重要」** AI 算力用电需求持续增长，算力园区的电网接入稳定性与用电成本已成为产业落地的核心约束之一，该计划是行业针对该痛点的早期协作探索。

**「可关注」** 可关注：该计划后续公开的电力公司合作案例，以及电网适配要求是否会被纳入 AI 算力园区的行业建设规范。

**Tags**: `#policy`, `#industry`, `#lab`

---

<a id="item-ai-daily-5"></a>
### [OpenAI 联合 Cathedral Systems 开展安全冲刺](https://openai.com/index/preparing-our-next-security-sprint-to-harden-openai) ⭐️ 6.8/10

On November 2, 2026, OpenAI announced via its official blog that it is preparing its next internal security sprint, partnering with Cathedral Systems to test and strengthen its defensive capabilities using AI.

rss · OpenAI Blog · Nov 2, 18:00

**「为什么重要」** This public disclosure of an AI-driven defensive security testing initiative from OpenAI provides a tangible reference for security practices across the AI industry.

**「可关注」** Watch for: OpenAI&\#x27;s practical approach to combining external security vendor expertise with AI for defensive capability testing.

**Tags**: `#lab`, `#security`, `#industry`

---