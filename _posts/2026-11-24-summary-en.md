---
layout: default
title: "Horizon Summary: 2026-11-24 (EN)"
date: 2026-11-24
lang: en
---

> From 221 items, 17 important content pieces were selected

---

**Agent Harness Architecture**
1. [Codex rust-v0.172.0 发布](#item-harness-arch-1) ⭐️ 8.8/10
2. [pydantic-ai v2.73.0 发布](#item-harness-arch-2) ⭐️ 7.8/10
3. [OpenAI Agents Python v1.0.0-alpha.2 发布](#item-harness-arch-3) ⭐️ 7.8/10

**AI Agent Engineer**
1. [RoboTrack 发布 含基准与合成训练数据](#item-agent-engineer-1) ⭐️ 7.8/10
2. [NariQ 发布 Qwen3.8-27B 3-bit 量化](#item-agent-engineer-2) ⭐️ 7.0/10
3. [Anthropic formal-math 发布 VP≠VNP 形式化证明](#item-agent-engineer-3) ⭐️ 7.0/10
4. [AutoPILOT 实时游戏 Harness 与 AFK-Bench 发布](#item-agent-engineer-4) ⭐️ 7.0/10
5. [RUIBench: Interface Design Doubles Agent Success Rates](#item-agent-engineer-5) ⭐️ 7.0/10
6. [GameAnything 论文与基准发布](#item-agent-engineer-6) ⭐️ 7.0/10
7. [SWE-Gym 标签错误研究](#item-agent-engineer-7) ⭐️ 7.0/10
8. [datasette-charts 0.2a0 发布](#item-agent-engineer-8) ⭐️ 6.3/10
9. [GLM-5.4 发布 首用循环Transformer](#item-agent-engineer-9) ⭐️ 5.5/10

**AI Daily**
1. [OpenAI 与 Cisco 推出 Shirudo](#item-ai-daily-1) ⭐️ 6.8/10
2. [Richpanel 用 GPT 系列实现 30 天 50% 客服自动化](#item-ai-daily-2) ⭐️ 6.8/10
3. [OpenAI 探讨内部法务 AI 应用](#item-ai-daily-3) ⭐️ 5.8/10

**AI Deals**
1. [Koofr 1TB 终身订阅 129.9美元 再开](#item-ai-deals-1) ⭐️ 8.0/10
2. [DevSwarm Free Seats Offer](#item-ai-deals-2) ⭐️ 6.0/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [Codex rust-v0.172.0 发布](https://github.com/openai/codex/releases/tag/rust-v0.172.0) ⭐️ 8.8/10

OpenAI Codex 发布 rust-v0.172.0。本次更新覆盖 MCP 工具链、沙箱恢复、工具审批、运行时支持和终端导航。stdio MCP 服务器默认改为首次工具调用时懒启动；\`codex exec resume\` 恢复保存的沙箱权限、工作目录和 workspace roots；支持在 \`config.toml\` 中为单个 app 工具配置审批 reviewer。终端内新增 Amazon Bedrock Runtime 选择，以及 Tab 补全 slash 命令、Shift+Up/Down 切换任务组、PageUp/PageDown 翻页长选项。

github · github-actions\[bot\] · Nov 24, 00:03

**「设计要点」** Code Mode 全部 host 连接切换至 gRPC，原 \`code\_mode\_host\_grpc\` 配置项弃用。Guardian V3 策略刷新与 MCP 解耦，授权证据限制在 agent fork 内部，MCP 消息板改为可选内存实现。

**「改了什么」** 相对 rust-v0.171.0，新增线程链接跳转、slash 命令补全、任务组导航、stdio MCP 懒启动、per-app 审批 reviewer、Amazon Bedrock Runtime 支持，以及 GPT-6.2 迁移文档。修复 \`codex exec resume\` 沙箱权限丢失、跨平台路径不一致、provider 错误延迟上报、父 turn 中断丢失子回复、长选项翻页和云回复乱序。

**Tags**: `#mcp`, `#tools`, `#sandbox`, `#subagents`, `#permissions`

---

<a id="item-harness-arch-2"></a>
### [pydantic-ai v2.73.0 发布](https://github.com/pydantic/pydantic-ai/releases/tag/v2.73.0) ⭐️ 7.8/10

pydantic-ai v2.73.0 发布。本次更新向 \`Agent.override\` 添加 \`capabilities\` 参数，导出 \`AgentInstructions\` 与 \`SourcedInstruction\` 类型，并在 OpenAI Responses 的 \`provider\_details\` 及模型请求 span 中暴露 \`input\_transformations\`。版本将 \`openai\` 依赖下限提升至 3.50.0，新增 \`DeprecatedModelWarning\` 提示 Anthropic 或 OpenAI 已弃用模型，并引入 \`RealtimeSession.append\_voice\_instructions\` 支持 GPT-Live 语音模型。私有上下文变量 \`Agent.\_override\_root\_capability\` 的存储格式从单一值改为 \`\(capability, injected\)\` 元组，直接读取该变量的代码需要更新。

github · dsfaccini · Nov 24, 03:53

**「设计要点」** 框架通过上下文变量管理 agent 覆盖状态，并在 harness 压缩时保留最新工作区响应。\`boxd\` 沙箱升级至 0.3.3，\`E2BSandbox\` 支持 \`idle\_timeout\` 配置，\`Coder\` 组件通过 \`pillow&gt;=12.3.0\` 将输入图像最长边限制为 1024 像素。可观测性层统一输出 Logfire 5 与 6 的在线评估事件。

**「改了什么」** \`Agent.override\` 新增 \`capabilities\` 参数，私有变量 \`Agent.\_override\_root\_capability\` 改为存储 \`\(capability, injected\)\` 元组。OpenAI Responses 的 \`input\_transformations\` 现在出现在 \`provider\_details\` 和模型请求 span 中，\`openai\` 依赖下限升至 3.50.0。新增 \`DeprecatedModelWarning\`、\`RealtimeSession.append\_voice\_instructions\`、\`E2BSandbox\(idle\_timeout=...\)\`、\`SubAgents\` 延迟工具调用传递，以及 GPT-Live 自定义语音对象。Claude、Gemini、Grok 模型不再发送统一设置。\`boxd\` 依赖升至 \`&gt;=0.3.3,&lt;0.4\`，\`coder\` 额外依赖新增 \`pillow&gt;=12.3.0\`。

**Tags**: `#runtime`, `#prefix-cache`, `#permissions`

---

<a id="item-harness-arch-3"></a>
### [OpenAI Agents Python v1.0.0-alpha.2 发布](https://github.com/openai/openai-agents-python/releases/tag/v1.0.0-alpha.2) ⭐️ 7.8/10

OpenAI 发布 Python Agents SDK v1.0.0-alpha.2， bundled 原生 Codex 运行时。新增跨 worker 恢复对话与待处理审批、工具执行钩子、文本脱敏及操作追踪。引入破坏性持久化状态格式变更：alpha.2 读取 alpha.1 的 RunState schema 1.22，但即使关闭脱敏也始终写入 schema 1.24。受保护的 ResumableSession 检查点升级为版本 2，要求先升级读取器再升级写入器。

github · markstuart-oai · Nov 23, 20:11

**「设计要点」** 运行时通过 ResumableSession 与 ResumableSessionStore（支持原子条件写入或 Redis）持久化会话历史与待处理审批，要求每 session 单写入者。工具层提供 prepare\_tool\_input、prepare\_tool\_output、prepare\_tool\_declaration 三个钩子，Runner 在审批前后重新检查工具资格。嵌入的 Codex Core rust-v0.166.0 补丁在同步 PreToolUse 处理器失败或超时时阻止原生分发，取消操作给予 Agent.as\_tool\(\) 最多 250 ms 清理时间。

**「改了什么」** 相对 alpha.1，新增 ResumableSession 跨 worker 恢复能力，支持恢复原生 Codex 的 exec\_command 与 apply\_patch 审批。新增 ToolExecutionConfig 配置项，支持 prepare\_tool\_input/output/declaration 钩子及函数工具过滤。引入 RunConfig.redact\_text 文本脱敏和 operation\_detail 追踪配置。持久化状态格式从 schema 1.22 升级到 1.24，检查点版本升至 2，构成破坏性变更。

**Tags**: `#runtime`, `#tools`, `#permissions`, `#memory`, `#subagents`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [RoboTrack 发布 含基准与合成训练数据](https://huggingface.co/blog/allenai/robotrack) ⭐️ 7.8/10

Allen AI 团队通过 Hugging Face Blog 发布 RoboTrack，包含 RoboTrack-Bench 基准、RoboTrack-15M 合成训练数据集、两套新点跟踪模型（RoboTracker、RoboTracker-Warp）及技术报告。RoboTrack-Bench 收录 307 段来自 DROID、Ego-Exo4D、MolmoAct 2、EgoVerse 的真实机械臂操作视频，人工标注 2,522 条点轨迹，覆盖杂乱场景、第一/第三人称视角及遮挡情况，其中 33 对视频提供同步双视角标注。评估显示 CoWTracker、AllTracker、CoTracker3、BootsTAPNext 等主流跟踪器在该基准上的 Average Jaccard \(AJ\) 得分较 RoboTAP 下降 3.0–6.6 分，CoWTracker 从 70.5 降至 63.9 AJ；使用 RoboTrack-15M 补充训练可提升真实操作视频上的跟踪效果，RoboTracker-Warp 在五个评估基准中的四个达到最优。团队已将跟踪器部署到真实机器人上，用于指导湿实验室任务中的移液管操作。AllTracker 的复现得分与原文略有差异，因修复了其发布评估代码中的计分错误。

rss · Hugging Face Blog · Nov 23, 17:20

**「为什么重要」** 现有机器人跟踪基准主要基于受控桌面场景，无法反映真实操作中的遮挡、杂乱背景和视角变化。RoboTrack-Bench 揭示了主流跟踪器在实际机械臂任务中的性能缺口，而 RoboTrack-15M 提供了针对操作交互的合成训练数据，两者共同为开发可部署的机器人感知组件提供了可复现的评估与训练资源。

**「可关注」** 可关注：现有跟踪器在真实杂乱场景下的 AJ 得分普遍下降 3–7 分，说明基于合成桌面数据训练的模型在真实机器人操作中存在泛化缺口；RoboTrack-15M 的模拟轨迹生成 pipeline 展示了如何从机器人操作仿真中提取监督信号以缩小该缺口。

**Tags**: `#eval`, `#harness`, `#robotic-manipulation`, `#perception`

---

<a id="item-agent-engineer-2"></a>
### [NariQ 发布 Qwen3.8-27B 3-bit 量化](https://huggingface.co/nari-labs/Qwen3.8-27B-NariQ-GGUF) ⭐️ 7.0/10

NariQ 是 Qwen3.8-27B 的 3-bit 及更低比特量化版本，发布方称其在智能体任务、数学、多语言推理、图像理解上接近 BF16 性能，且是首个在长周期智能体任务上保留 BF16 级别表现的 3-bit 及以下量化。公开基准显示，3-bit 版本在 DeepSWE、Terminal-Bench 2.1 等智能体任务上得分高于 BF16 基线，文件大小约 10GB，解码速度在 RTX PRO 6000 上与其他量化相当，同时提供了 4K 到 64K 上下文长度的表现对比。运行需配套 nari-labs 维护的自定义 llama.cpp fork，所有基准数据为发布方自报告，未经过第三方独立验证。该量化方案为本地部署 coding agent、做小模型量化评估的工程师提供了新的选项，但存在额外适配成本与性能不确定性。

hackernews · toebee · Nov 23, 13:42 · [Discussion](https://news.ycombinator.com/item?id=50611402)

**「为什么重要」** 已发生的变化是它首次公开了声称在长周期智能体任务上接近 BF16 的 3-bit 及以下 Qwen3.8-27B 量化方案，将模型显存门槛降至 10GB 级别，同时公开了智能体相关基准数据，填补了该方向的可参考案例。尚未证实的影响包括其实际泛化性、第三方复现结果、对非智能体任务的表现均未确认，且强制依赖自定义 llama.cpp fork 增加了部署摩擦。

**「可关注」** NariQ 的 3-bit 量化将 Qwen3.8-27B 的显存占用压到 10GB 级别，但需适配其自定义 llama.cpp fork，且基准数据为发布方自报告，实际部署前建议自行验证智能体任务表现。

**「评论」** 社区反馈存在分歧：部分用户认可其覆盖多类长周期任务的基准设计，也有用户质疑高计算量量化易过拟合 benchmark、实际泛化性存疑，另有用户关注旧款 GPU、Apple M 系列芯片的兼容性与性能表现，还有用户指出其性能增益可能来自评估 harness 差异而非模型本身。

**Tags**: `#eval`, `#coding-agent`, `#harness`

---

<a id="item-agent-engineer-3"></a>
### [Anthropic formal-math 发布 VP≠VNP 形式化证明](https://github.com/anthropics/formal-math/tree/main/vp-vnp) ⭐️ 7.0/10

2026年11月23日，Anthropic官方formal-math项目发布经社区验证的LLM辅助原创形式化证明，结论为VP≠VNP在所有域上成立，相关证明文件与工具链已开源托管于GitHub的\`anthropic/formal-math\`仓库\`vp-vnp\`目录。该成果是计算复杂度理论领域可复核的原创证明，对推理Agent、形式化验证工具链及推理评测基准建设有参考价值。当前披露的技术细节有限，论文未说明该结论与相对化、代数化屏障的关联，核心数学结论受众范围较窄。

hackernews · mikeryan52 · Nov 23, 22:09 · [Discussion](https://news.ycombinator.com/item?id=50620102)

**「为什么重要」** 这是目前公开少数由LLM辅助产出、且经社区复现校验的原创形式化数学证明，验证了大语言模型在专业数学证明场景的可用性。配套开源工具链可为相关工程实践提供参考，但核心数学结论本身受众较窄，尚未看到广泛的落地应用信号。

**「可关注」** 可关注：Anthropic formal-math项目开源的VP≠VNP证明工具链与复现流程，可作为LLM辅助形式化推理的参考实现。

**「评论」** 社区观点存在分歧：部分用户认为这是向P vs NP问题推进的阶段性成果，也有用户担忧LLM会降低数学研究门槛；另有开发者已完成证明声明的复现校验，确认定理可推导出对应公开声明。

**Tags**: `#eval`, `#coding-agent`, `#orchestration`, `#harness`

---

<a id="item-agent-engineer-4"></a>
### [AutoPILOT 实时游戏 Harness 与 AFK-Bench 发布](https://huggingface.co/papers/2611.28202) ⭐️ 7.0/10

2026-11-24，Hugging Face Daily Papers 收录论文《AutoPILOT: A Visual Agent Harness for Real-Time Gameplay》，提出同名视觉 Agent Harness 及 AFK-Bench 实时游戏评估基准。AutoPILOT 改变现有 Harness（如 VISTA）每次模型调用至多产生一个动作的限制，允许模型在单次调用中输出原始动作、启动开环宏或编写闭环控制器，从而在游戏持续运行时无需频繁调用模型。AFK-Bench 包含 120 款浏览器游戏，用于评估实时游戏 Agent。该研究直接影响游戏 Agent Harness 与自动化评测的工程实现，但论文具体性能数据与游戏分组细节在提供材料中不完整。

rss · Hugging Face Daily Papers · Nov 24, 00:00

**「为什么重要」** 实时游戏场景暴露了现有 Harness 的调度瓶颈：模型推理速度跟不上游戏帧率时，Agent 表现急剧下降。AutoPILOT 将控制权从“每步必询模型”改为“模型下发策略后自主执行”，为降低调用频率提供了可验证的设计路径；AFK-Bench 则填补了实时浏览器游戏 Agent 的系统化评测空白。实际效果与泛化性仍需后续实验验证。

**「可关注」** 可关注：实时游戏 Agent 的端到端延迟可能受限于 Harness 的动作发射频率而非模型单步推理速度；将模型输出从 primitive action 扩展为 macro 或 closed-loop controller，是减少模型调用次数的可行工程方向，但需处理控制器安全回退与状态同步。

**Tags**: `#harness`, `#eval`, `#coding-agent`

---

<a id="item-agent-engineer-5"></a>
### [RUIBench: Interface Design Doubles Agent Success Rates](https://huggingface.co/papers/2611.31115) ⭐️ 7.0/10

A preprint published November 24, 2026, introduces RUIBench, a benchmark for evaluating robot-use interfaces \(RUI\) for embodied agents, alongside RUIKit, a unified interface framework. The benchmark includes 30 manipulation tasks across five suites. Simulation results show that changing only the RUI shifts a frontier agent&\#x27;s success rate from 45% to 81% on manipulation tasks.

rss · Hugging Face Daily Papers · Nov 24, 00:00

**「Why it matters」** The work quantifies how interface design alone can nearly double frontier agent performance, highlighting a critical bottleneck in deploying foundation models for physical tasks. This offers actionable insights for agent and harness design in embodied systems.

**「Engineer takeaway」** The action abstraction and interaction form choices in the interface layer can dominate overall task success, indicating that RUI design should be prioritized alongside model selection in embodied AI development.

**Tags**: `#eval`, `#harness`

---

<a id="item-agent-engineer-6"></a>
### [GameAnything 论文与基准发布](https://huggingface.co/papers/2611.29238) ⭐️ 7.0/10

2026 年 11 月 24 日，Hugging Face 每日论文推荐开源智能体平台 GameAnything，可将多模态灵感转化为现有游戏的可玩扩展。该平台集成编程智能体、独立试玩批评器、持久化开发状态与可复用经验记忆，支持迭代开发。同期发布的 GameAnything-Bench 覆盖多模态参考、游戏创建目标及游戏环境。摘要未提供性能对比或生产环境 Trace 等进一步验证信息。

rss · Hugging Face Daily Papers · Nov 24, 00:00

**「为什么重要」** 该工作提供了智能体游戏开发的端到端参考实现，其记忆机制与评测基准对 coding agents 的持续迭代设计有直接参考价值。但实际效果与工程落地成本仍需后续验证。

**「可关注」** 可关注：GameAnything 将编程智能体、试玩批评器与可复用经验记忆耦合的迭代架构，以及 GameAnything-Bench 对多模态、多目标、多环境的覆盖方式。

**Tags**: `#coding-agent`, `#eval`, `#memory`, `#orchestration`

---

<a id="item-agent-engineer-7"></a>
### [SWE-Gym 标签错误研究](https://huggingface.co/papers/2611.30207) ⭐️ 7.0/10

论文系统审计了 SWE-Gym 数据集的奖励标签正确性。发现 74% 的 9B 基模型从未解决的任务存在假负向奖励标签（正确修复被测试拒绝），而有时解决的任务中该比例为 20%。修复或移除这些错误任务后，在等量数据、匹配难度下，模型在 SWE-bench Verified 和 SWE-bench 上得分分别提升 2.4 和 2.7 分。这影响所有使用 SWE-Gym 进行编码智能体强化学习训练的研究与工程实践。

rss · Hugging Face Daily Papers · Nov 24, 00:00

**「为什么重要」** SWE-Gym 是编码智能体 RL 训练的主流数据源。74% 的假负向标签比例意味着大量训练信号错误。修正后性能提升证实了数据质量对训练效果的直接影响，对数据策展流程和基准评测可靠性有直接参考价值。

**「可关注」** 可关注：在构建或清洗编码智能体训练数据时，应对未解决任务执行测试套件复核，优先排查假负向奖励标签，因为错误负样本会显著降低策略学习效率。

**Tags**: `#coding-agent`, `#eval`, `#harness`

---

<a id="item-agent-engineer-8"></a>
### [datasette-charts 0.2a0 发布](https://github.com/datasette/datasette-charts/releases/tag/0.2a0) ⭐️ 6.3/10

simonw 于 2026-11-24 发布 datasette-charts 0.2a0。该版本新增与 Datasette Agent 的集成，当两个插件同时安装时，agent 可获得绘图工具及图表建议工具。同时新增 decade 时间单位，适用于跨世纪列的数据分桶；并改进了稀疏数据折线图渲染，使跳过分桶的数据点以连线而非孤立点显示。

github · simonw · Nov 24, 04:24

**「为什么重要」** 该更新属于 Datasette 生态内的增量改进，对通用 AI agent 工程、工具链设计或评估系统的直接影响有限。

**「可关注」** 可关注：Datasette Agent 通过插件集成获得领域特定工具（图表创建与建议）的扩展模式，以及 decade 时间单位对长期跨度稀疏数据分桶的处理方式。

**Tags**: `#coding-agent`, `#harness`

---

<a id="item-agent-engineer-9"></a>
### [GLM-5.4 发布 首用循环Transformer](https://simonwillison.net/2026/Nov/23/glm-54/) ⭐️ 5.5/10

2026年11月23日，Z.ai 发布 GLM-5.4，这是其首个采用循环Transformer架构的模型。该架构通过权重共享的层组多次迭代 refining 隐藏状态，可在不增加参数量的前提下提升网络深度。当前 GLM-5.4 未开放权重，仅能通过 Z.ai Coding Plan 订阅访问 API，接口地址为 https://api.z.ai/api/v1，兼容 OpenAI Responses API。这是近一周内第二个公开的循环Transformer实现，前一个为 11 月 20 日 Thinking Machines Lab 发布的 Inkling 2 Mini，后者会对模型中间层运行 3 次以提升推理质量。目前无公开的编码任务基准测试数据，仅作者生成的鹈鹕骑自行车图像测试显示，GLM-5.4 生成风格与 5.3 接近，和 5.1、5.2 差异显著。

rss · Simon Willison · Nov 23, 23:40

**「为什么重要」** 循环Transformer架构在两周内出现两个公开实现，是模型架构探索的新动向。但目前两类实现均未公开针对编码任务的量化性能数据，其对 coding agent 的实际增益尚未得到验证。

**「可关注」** GLM-5.4 当前仅通过 Z.ai Coding Plan 开放 API，接口兼容 OpenAI Responses 格式，现有通用 LLM 插件（如 llm-zai）尚未支持该模型，第三方工具适配滞后于发布节奏。

**Tags**: `#coding-agent`

---

## AI Daily

<a id="item-ai-daily-1"></a>
### [OpenAI 与 Cisco 推出 Shirudo](https://openai.com/index/introducing-shirudo) ⭐️ 6.8/10

OpenAI 与 Cisco 联合发布开源 Linux 运行时 Shirudo。该工具旨在帮助团队在补丁部署期间保护正在运行的系统。目前公开信息有限，仅确认了项目存在及基本定位。

rss · OpenAI Blog · Nov 23, 21:20

**「可关注」** 可关注：Shirudo 作为开源 Linux 运行时，可在补丁 rollout 时提供运行中系统保护。

**Tags**: `#lab`, `#industry`, `#open-source`, `#product`

---

<a id="item-ai-daily-2"></a>
### [Richpanel 用 GPT 系列实现 30 天 50% 客服自动化](https://openai.com/business/customer-stories/richpanel-ai-customer-support) ⭐️ 6.8/10

OpenAI官方博客发布客户案例，Richpanel通过使用GPT-6 Astra、GPT-6.1 Sol及GPT-6 Luna，在30 天内实现了50% 的客户支持自动化。该案例展示了GPT系列模型在客服场景的应用效果，但未披露具体技术架构与基线对比数据。

rss · OpenAI Blog · Nov 23, 08:00

**「为什么重要」** 此案例提供了GPT系列模型在客服自动化领域的量化落地样本，展示了多模型分工在业务场景中的实际效果，但影响面局限于单一客户实践。

**「可关注」** 可关注：GPT-6 Astra与Sol承担工具及流程支持、Luna负责对话的分工设计，以及30 天内达到50% 自动化率的落地周期。

**Tags**: `#lab`, `#model`, `#product`, `#industry`

---

<a id="item-ai-daily-3"></a>
### [OpenAI 探讨内部法务 AI 应用](https://openai.com/business/learn/connected-intelligence-for-in-house-legal) ⭐️ 5.8/10

OpenAI 官方博客发布内容，收录了 OpenAI 的 Stacey Wang、Craig Bruney，LECG 的 Mary O’Carroll 与 Cooley 的 Richard Segal 的专题讨论，探讨 AI 如何帮助内部法务团队串联业务上下文、搭建可复用工作流、提升外部律所协作效率。

rss · OpenAI Blog · Nov 23, 08:00

**「为什么重要」** 该讨论聚焦企业内部法务的 AI 落地场景，为关注 toB 垂直领域 AI 应用的从业者提供了行业实践参考。

**「可关注」** 可关注：内部法务场景的 AI 工作流搭建与跨主体协作效率优化方向。

**Tags**: `#lab`, `#industry`, `#product`

---

## AI Deals

<a id="item-ai-deals-1"></a>
### [Koofr 1TB 终身订阅 129.9美元 再开](https://www.appinn.com/koofr-1tb/) ⭐️ 8.0/10

你看到的内容可能由第三方 AI 基于小众软件文章提炼总结而成，可能与原文真实意图存在偏差。不代表小众软件观点和立场。请点击链接阅读原文细致比对和校验。Koofr云存储提供10GB免费存储空间，支持WebDAV、Rclone及多平台客户端，可连接Dropbox、Google Drive、OneDrive等主流云盘。当前1TB终身订阅优惠再次上线，通过Stacksocial指定链接购买并使用优惠码KOOFR，可享129.9美元（部分更新记录显示为129.99美元）特价，官方原价为199美元，官网年付100GB档位价格为19.67欧元/年、500GB档位为68.85欧元/年。

rss · 小众软件 · Nov 24, 03:24

**「为什么重要」** 该优惠为再次上线，价格低于Koofr官网年付档位；免费10GB空间支持WebDAV、Rclone，可先体验适配服务器备份、跨云同步需求。

**「可关注」** 可关注：使用rclone做服务器备份、跨云同步的用户可先试用免费10GB版，注意免费版文件分享有10次限制，终身订阅需通过指定链接使用KOOFR优惠码购买。

**Tags**: `#free-tier`, `#promo`, `#coupon`, `#api`

---

<a id="item-ai-deals-2"></a>
### [DevSwarm Free Seats Offer](https://devswarm.ai/startups/) ⭐️ 6.0/10

DevSwarm is offering startups up to 10 seats free for 1 year, with no investor requirement. The offer is listed on the DevSwarm website, but key details such as the offer expiration date, full eligibility criteria, and product-specific information are not provided in the source material.

rss · HN Free API / Credits · Nov 23, 20:21

**「Why it matters」** The no-investor requirement removes a common eligibility barrier for early-stage startups, but the absence of a stated expiration date means the offer could be withdrawn without warning.

**「Note」** Watch for: DevSwarm&\#x27;s startup promo provides up to 10 free seats for 1 year with no investor requirement, but lacks an expiration date and full eligibility details in the current listing.

**Tags**: `#promo`, `#free-tier`, `#limited-free`

---