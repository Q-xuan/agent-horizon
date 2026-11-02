---
layout: default
title: "Horizon Summary: 2026-11-03 (EN)"
date: 2026-11-03
lang: en
---

> From 197 items, 13 important content pieces were selected

---

**Agent Harness Architecture**
1. [Mastra core 1.81.0 发布](#item-harness-arch-1) ⭐️ 8.8/10
2. [google/adk-go v2.7.0 发布](#item-harness-arch-2) ⭐️ 8.8/10
3. [vLLM v0.33.0rc3 候选版发布](#item-harness-arch-3) ⭐️ 6.8/10
4. [Anthropic Skills 发布](#item-harness-arch-4) ⭐️ 6.0/10

**AI Agent Engineer**
1. [Legora 无观测法律Agent 实践](#item-agent-engineer-1) ⭐️ 7.0/10
2. [SimpleLoRIF 识别微调安全退化数据](#item-agent-engineer-2) ⭐️ 7.0/10
3. [R²Orch 递归自博弈编排范式提出](#item-agent-engineer-3) ⭐️ 6.0/10
4. [HF 每日论文：CEPO 多智能体提示优化](#item-agent-engineer-4) ⭐️ 6.0/10
5. [CaPtain 开源 CaP 智能体流水线](#item-agent-engineer-5) ⭐️ 6.0/10

**AI Daily**
1. [OpenAI 发布 LifeVal 基准](#item-ai-daily-1) ⭐️ 7.8/10
2. [Qodo 推出 Codex 官方插件](#item-ai-daily-2) ⭐️ 7.8/10
3. [Claude Message Threads 公测上线](#item-ai-daily-3) ⭐️ 7.8/10
4. [OpenAI 发布 Grid Protectors Program](#item-ai-daily-4) ⭐️ 6.8/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [Mastra core 1.81.0 发布](https://github.com/mastra-ai/mastra/releases/tag/%40mastra/core%401.81.0) ⭐️ 8.8/10

Mastra 发布 @mastra/core@1.81.0。@mastra/mcp 引入实验性存储-backed MCP 任务，长运行工具/智能体/工作流可立即返回 task ID，通过轮询/应答/取消跨实例协作，并在共享存储与统一追踪下重启恢复。后台任务扩展至非智能体所有者（如 MCP 服务器），支持 per-task \`expiresAt\`/\`metadata\` 保留、per-owner 并发覆盖，以及 \`\{ onNoSlot: &\#x27;queue&\#x27; \}\` 排队恢复，存储适配器已更新持久化新字段。可观测性新增执行 \`outcome\` 与 typed \`stopReason\`，导出 \`model\`/\`provider\`，测量 \`timeToFirstTokenMs\`，支持 ClickHouse/DuckDB/Postgres 查询分组，便于失败分析与成本/性能拆分。

github · PaulieScanlon · Nov 2, 12:33

**「设计要点」** 任务状态与后台元数据通过共享存储适配器持久化，实现跨实例和重启后的恢复；可观测性字段统一注入各层 trace，由存储后端提供查询与分组能力。

**「改了什么」** 本版新增存储-backed MCP 任务、后台任务非 agent 所有者支持、可观测性 outcome/stopReason/TTFT 字段、仪表盘与保存视图 schema、浏览器 cookie 注入、工厂作用域沙箱环境，以及频道附件下载与工作区文件 UX 改进。同时 @mastra/playground-ui 清理 Metrics chart card API 并移除 fluid-hover 工具，@mastra/core 移除 \`network/vNext\` 与 \`telemetry/otel-vendor\` 子路径，@mastra/factory 废弃 \`defineBoard\(\)\` 及相关字段。

**Tags**: `#mcp`, `#runtime`, `#tools`, `#memory`, `#observability`

---

<a id="item-harness-arch-2"></a>
### [google/adk-go v2.7.0 发布](https://github.com/google/adk-go/releases/tag/v2.7.0) ⭐️ 8.8/10

google/adk-go v2.7.0 发布。新增 Anthropic Claude 首方模型支持、搜索门控 MCP 工具发现、实验性分类器 API 和单次调用模型预算上限。默认切换至 OpenTelemetry GenAI 语义约定 v2 作为追踪格式，对现有遥测消费者构成破坏性变更。同时修复 MCP 多用户会话隔离、ADC 凭证 mint 失败、LoopAgent 上下文取消行为等问题，并要求 Go 1.26.10。

github · wolo-lab · Nov 2, 10:37

**「设计要点」** 运行时通过 RunConfig.MaxLLMCalls 在单次 invocation 层面对模型调用做硬上限，默认 500 次，超出返回 agent.ErrLLMCallsLimitExceeded。工具层新增 tool/toolsearch 包装器，将大型 MCP 目录从每轮请求中剥离，改为按需动态声明；遥测层默认采用 OpenTelemetry GenAI semantic conventions v2，消息内容以结构化值写入 span，可通过环境变量回退至旧格式至 2027-03-31。

**「改了什么」** 相对上一版，新增 model/anthropicmodel 实现 Anthropic Messages API 与 Vertex AI 接入，支持流式、工具调用、图片/PDF 输入、提示缓存；exp/classifier 提供类型化分类器与工作流路由节点；tool/toolsearch 实现搜索门控工具发现。RunConfig.MaxLLMCalls 引入单次调用预算，默认 500 次；追踪格式迁移至 OpenTelemetry GenAI v2；MCP 在启用 Config.Auth 后按用户隔离会话；新增 Gemini 内置工具；OpenAI 兼容模型修复图片/文件发送与 schema 回退逻辑；修复 ADC 凭证、LoopAgent 取消行为及可选指令占位符错误传播等问题。

**「评论」** 无社区评论。

**Tags**: `#runtime`, `#tools`, `#mcp`, `#planning`, `#prefix-cache`

---

<a id="item-harness-arch-3"></a>
### [vLLM v0.33.0rc3 候选版发布](https://github.com/vllm-project/vllm/releases/tag/v0.33.0rc3) ⭐️ 6.8/10

vLLM 发布 v0.33.0rc3 候选版，本版包含 927 个提交。技术更新包括升级至 PyTorch 2.14 与 Triton 3.8，停止发布 CUDA 12.9 镜像与 wheel，仅提供 CUDA 13.0 制品。新增 ABI 稳定的 CUDA wheel、\`vllm/vllm\` 镜像别名、AWS EFA 镜像，以及 OpenAI 兼容的 \`/v1/decisions\` 端点。移除 Medusa 与 MLP speculator，废弃 legacy Ray compiled-graph executor 与 \`--mamba-cache-mode\`。

github · khluu · Nov 2, 10:10

**「设计要点」** CUDA wheel 现与 libtorch 保持 ABI 稳定，降低自定义集成兼容成本。Rust 前端改进包括长对话不再返回 HTTP 500、不支持的启动时参数直接报错，以及 TP&gt;1 时并发 worker 启动。

**「改了什么」** 依赖基线升至 PyTorch 2.14/Triton 3.8，CUDA 12.9 支持终止。推理接口新增 \`/v1/decisions\` 与 \`/v1/embeddings\` 延迟分块，\`/inference/v1/generate\` 支持 \`output\_mode=&quot;derender&quot;\`。speculative decoding 引入 XPress refiner 与 FLy 有损验证策略，DeepSeek-V4.1-Flash + DSpark 在 GB300 上输出吞吐从 1373 提升至 3390 tok/s。

**Tags**: `#runtime`

---

<a id="item-harness-arch-4"></a>
### [Anthropic Skills 发布](https://github.com/anthropics/skills) ⭐️ 6.0/10

Anthropic has publicly released its official Agent Skills implementation in the \`anthropics/skills\` repository. The system dynamically loads folders of instructions, scripts, and resources to extend Claude&\#x27;s capabilities for specialized, repeatable tasks. Skills teach Claude to complete specific tasks consistently, such as creating documents with brand guidelines or analyzing data using organizational tools, conforming to the \`agentskills.io\` standard. The published material is truncated and contains no technical implementation details, code paths, or version-specific change information.

rss · GitHub Trending Daily · Nov 2, 23:00

**Tags**: `#tools`, `#runtime`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [Legora 无观测法律Agent 实践](https://latent.space/p/building_legal_agents_when_you_can_t_see_the_data_-_jacob_lauritzen_cto_of_legora/) ⭐️ 7.0/10

2026年11月2日Latent Space发布对Legora CTO Jacob Lauritzen的访谈，分享其团队在客户数据隐私约束下无法读取任何Agent执行trace时，构建法律Agent的生产实践。团队采用模拟客户工作流的测试环境、paraphrase trace收敛故障类型、设计不依赖trace的产品指标验证效果，同时公开模型选型策略、曾因隐私要求全量部署于Azure、一次发布后引用准确率从70%升至99%且无需额外改动等细节，相关经验面向法律科技Agent的构建、测试与合规团队。

rss · Latent Space · Nov 2, 22:54

**「为什么重要」** 这是目前公开的少数严格受数据隐私约束、完全无法获取Agent运行trace场景下的一手生产案例，其中的测试环境设计、无trace指标验证方法可复用于其他同类隐私敏感Agent场景，但尚未有公开 benchmark 验证其普适性。

**「可关注」** 可关注：受隐私约束无法获取原始trace的场景下，可通过paraphrase trace收敛故障类型、构建模拟客户工作流的测试环境替代真实观测，同时设计不依赖trace的产品指标验证Agent效果。

**Tags**: `#observability`, `#eval`, `#harness`, `#permissions`, `#orchestration`

---

<a id="item-agent-engineer-2"></a>
### [SimpleLoRIF 识别微调安全退化数据](https://huggingface.co/papers/2610.37481) ⭐️ 7.0/10

2026年11月2日Hugging Face Daily Papers收录一篇研究论文，提出SimpleLoRIF可扩展梯度嵌入方法，可通过梯度分析识别看似无害但会导致大模型安全退化的微调数据。该方法简化低秩归因流程，仅对最后4个transformer块做反向传播，可处理百万级规模数据集，将小规模梯度归因工具升级为全后训练数据集的实用过滤器，目前已在emergent misalignment场景完成初步验证，该论文当前获得24次社区点赞。该技术为Agent模型的训练数据安全审计、微调数据筛选提供了可落地的技术方案。

rss · Hugging Face Daily Papers · Nov 2, 00:00

**「为什么重要」** 该研究填补了微调阶段安全退化数据难以被常规内容过滤器筛查的空白，已为Agent工程师提供可落地的训练数据安全审计技术路径；目前尚未公开其跨模型家族、跨任务场景的泛化性验证结果，实际落地效果待进一步观察。

**「可关注」** 可关注SimpleLoRIF仅针对最后4个transformer块做反向传播的梯度归因设计，以及其百万级规模数据集的处理效率实测数据。

**Tags**: `#eval`, `#harness`

---

<a id="item-agent-engineer-3"></a>
### [R²Orch 递归自博弈编排范式提出](https://huggingface.co/papers/2610.22740) ⭐️ 6.0/10

Hugging Face Daily Papers 于 2026-11-02 发布该论文摘要，当前获得 87 次 upvote，提出 R²Orch（Recursive Self-Play Orchestration）编排范式及 Recursive Learnability 训练目标。该范式采用双层循环：内循环通过自博弈改进编排器，外循环优化内循环的改进策略。Recursive Learnability 奖励 Proposer 选择在技能撤回时 rollout 结果持续分化的任务，以缓解 hand-designed curricula、advantage collapse 及 noisy skill evaluation 问题。当前材料为截断摘要，未披露完整技术细节、实验验证及可复现性信息。

rss · Hugging Face Daily Papers · Nov 2, 00:00

**「为什么重要」** 该工作针对 agent orchestration 学习中的课程设计、优势崩溃和评估噪声三个痛点，提出系统性递归改进框架，可能为编排器训练提供新方向。但论文仅发布摘要，实际效果、计算开销及泛化能力尚未经完整实验验证。

**「可关注」** 可关注：Recursive Learnability 通过奖励&quot;技能撤回后结果分化&quot;的任务选择，尝试耦合解决 advantage collapse 与 noisy evaluation，但其训练稳定性、计算成本及与现有编排框架的兼容性需待完整论文验证。

**Tags**: `#orchestration`, `#eval`

---

<a id="item-agent-engineer-4"></a>
### [HF 每日论文：CEPO 多智能体提示优化](https://huggingface.co/papers/2610.34722) ⭐️ 6.0/10

2026年11月2日Hugging Face Daily Papers发布多智能体提示优化论文，提出CEPO（Coordinator-Executor Prompt Optimization）通用框架。该框架将系统级协调的共享协调器提示与智能体专属执行器提示分离，分别按角色引导更新，复用现有提示优化器完成底层搜索。当前仅公开论文摘要，无性能评估、实现细节或开源发布信息，相关设计面向多智能体编排与agent harness工程师。

rss · Hugging Face Daily Papers · Nov 2, 00:00

**「为什么重要」** 该框架首次提出多智能体场景下协调提示与执行提示分离的优化结构，为agent编排与harness设计的提示工程提供了新思路。但目前仅公开摘要，无实证性能数据或落地案例，相关价值尚未得到验证。

**「可关注」** 可关注：多智能体系统中协调层与执行层提示分离的框架设计，需等待完整论文发布后验证实际效果与落地可行性。

**Tags**: `#orchestration`, `#harness`, `#multi-agent`

---

<a id="item-agent-engineer-5"></a>
### [CaPtain 开源 CaP 智能体流水线](https://huggingface.co/papers/2610.40799) ⭐️ 6.0/10

2026年11月2日，Hugging Face Daily Papers发布开源Code-as-Policy（CaP）机器人智能体后训练流水线CaPtain。该流水线可将小型开源视觉语言模型（VLM）转化为可用的CaP智能体，测试时无需视觉语言动作模型（VLA）、闭源前沿大模型或特权状态输入，采用监督微调（SFT）加多轮强化学习（RL）的统一后训练范式，解决了此前小型开源VLM无法胜任CaP任务、现有方案普遍绕过后训练依赖闭源模型或预训练VLA的问题。当前公开内容仅包含高层摘要，无技术实现细节、性能指标与评估结果，用例范围也相对较窄。

rss · Hugging Face Daily Papers · Nov 2, 00:00

**「为什么重要」** 该工作首次验证了小型开源VLM可通过统一后训练范式胜任CaP任务，打破了该领域此前对闭源模型或预训练VLA的依赖路径。但目前无公开性能数据，实际效果与泛化能力尚未得到充分验证，对多数智能体工程师的即时实用价值有限，需获取完整论文进一步确认。

**「可关注」** 可关注：CaPtain尝试将编码、工具类任务通用的SFT+多轮RL后训练范式迁移到机器人Code-as-Policy场景，且测试时零外部依赖，若验证有效可降低该类智能体的训练门槛。

**Tags**: `#coding-agent`

---

## AI Daily

<a id="item-ai-daily-1"></a>
### [OpenAI 发布 LifeVal 基准](https://openai.com/index/lifeval) ⭐️ 7.8/10

OpenAI 正式发布 LifeVal 基准测试，用于衡量 AI 系统完成 childcare、财务管理和政府 paperwork 等日常任务的能力。该基准聚焦生活实用场景，与侧重专业领域的现有评测形成互补。具体评分标准与数据集细节未在材料中披露。

rss · OpenAI Blog · Nov 2, 09:00

**「为什么重要」** LifeVal 聚焦日常真实任务，与侧重专业场景的现有评测形成互补，为评估 AI 生活辅助能力提供了新视角。

**「可关注」** 可关注：LifeVal 覆盖 childcare、财务管理和政府文书三类日常场景，可作为评估 AI 日常辅助能力的参考基准。

**Tags**: `#eval`, `#lab`, `#product`

---

<a id="item-ai-daily-2"></a>
### [Qodo 推出 Codex 官方插件](https://openai.com/index/qodo-codex-plugin) ⭐️ 7.8/10

Qodo 发布 OpenAI Codex 官方插件，将企业编码标准与代码库上下文嵌入 AI 代码审查流程，支持开发者在提交拉取请求前捕获 P0 级严重问题。该更新面向开发者工具细分领域，影响面有限。

rss · OpenAI Blog · Nov 2, 00:00

**「为什么重要」** 该插件为 Codex 增加了企业编码标准与代码库上下文支持，扩展了 AI 审查的适用场景。但更新仅面向开发者工具细分领域，影响面有限。

**「可关注」** 可关注：Qodo Codex 插件支持在提交拉取请求前，将企业编码标准与代码库上下文注入审查流程，用于捕获 P0 级问题。

**Tags**: `#product`, `#industry`

---

<a id="item-ai-daily-3"></a>
### [Claude Message Threads 公测上线](https://claude.com/resources/articles/message-threads) ⭐️ 7.8/10

Anthropic发布Claude Messages API的Message Threads公开测试版，面向长时间运行的智能体场景优化，目前默认对大多数Claude Code用户开启。启用后每轮请求仅需发送自上一轮新增的消息及上一轮响应ID，无需重发完整对话历史，500k至1M token的请求中位首token时间（TTFT）降低约35%。线程在服务端内存中加密存储，5分钟无请求后过期，需重新发送完整对话开启新线程，token消耗与原有逻辑一致。

rss · Claude Blog · Nov 2, 00:00

**「为什么重要」** 该功能直接针对长运行编码智能体、计算机使用智能体、多模态文档/图像工作流等长会话场景的高延迟痛点，无需重构现有对话逻辑即可降低交互等待时间，提升长会话下的响应效率。

**「可关注」** 可关注：在Claude Messages API请求中添加thread参数即可启用Message Threads，长会话场景下无需调整对话发送逻辑即可获得首token延迟优化。

**Tags**: `#product`, `#lab`, `#api`, `#performance`

---

<a id="item-ai-daily-4"></a>
### [OpenAI 发布 Grid Protectors Program](https://openai.com/index/grid-protectors-program) ⭐️ 6.8/10

OpenAI 正式发布 Grid Protectors Program，计划与电力公司开展合作，目标是支撑未来 AI 计算园区的电网可靠性，同时保护消费者用电成本。当前公开信息未披露具体合作方、实施路径与落地时间线。

rss · OpenAI Blog · Nov 2, 15:00

**「为什么重要」** AI 算力基础设施的扩张对电网承载能力提出新要求，该计划尝试协调产业需求与公共电网稳定、民生用电成本的关系。

**「可关注」** 可关注：该计划后续是否会出台配套的电力配套要求，影响 AI 计算园区的选址、建设与运营成本。

**Tags**: `#lab`, `#industry`, `#policy`

---