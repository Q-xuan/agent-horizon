---
layout: default
title: "Horizon Summary: 2026-11-24 (ZH)"
date: 2026-11-24
lang: zh
---

> 从 221 条内容中筛选出 17 条重要资讯。

<nav id="ah-toc" class="ah-toc" aria-label="目录"><span class="ah-toc-title">目录</span><ul><li><a href="#sec-harness-arch"><span class="ah-toc-name">Harness 架构</span><span class="ah-toc-count">3条</span></a></li><li><a href="#sec-agent-engineer"><span class="ah-toc-name">Agent 工程师日报</span><span class="ah-toc-count">9条</span></a></li><li><a href="#sec-ai-daily"><span class="ah-toc-name">AI 日报</span><span class="ah-toc-count">3条</span></a></li><li><a href="#sec-ai-deals"><span class="ah-toc-name">AI 羊毛</span><span class="ah-toc-count">2条</span></a></li></ul></nav>

---

**[Harness 架构](#sec-harness-arch)**
1. [Codex rust-v0.172.0 发布](#item-harness-arch-1) ⭐️ 8.8/10
2. [pydantic-ai v2.73.0 发布](#item-harness-arch-2) ⭐️ 7.8/10
3. [openai-agents-python v1.0.0-alpha.2 发布](#item-harness-arch-3) ⭐️ 7.8/10

**[Agent 工程师日报](#sec-agent-engineer)**
1. [RoboTrack 发布：机器人操作点跟踪基准](#item-agent-engineer-1) ⭐️ 7.8/10
2. [NariQ 3-bit Qwen3.8-27B 量化发布](#item-agent-engineer-2) ⭐️ 7.0/10
3. [Anthropic formal-math 发布 VP≠VNP 域上证明](#item-agent-engineer-3) ⭐️ 7.0/10
4. [AutoPILOT 实时游戏 harness 发布](#item-agent-engineer-4) ⭐️ 7.0/10
5. [RUIBench 发布：RUI 设计可提升 agent 成功率](#item-agent-engineer-5) ⭐️ 7.0/10
6. [GameAnything 平台与基准论文发布](#item-agent-engineer-6) ⭐️ 7.0/10
7. [SWE-Gym 训练数据假负向标签研究](#item-agent-engineer-7) ⭐️ 7.0/10
8. [datasette-charts 0.2a0 发布](#item-agent-engineer-8) ⭐️ 6.3/10
9. [Z.ai GLM-5.4 发布 首用循环 Transformer](#item-agent-engineer-9) ⭐️ 5.5/10

**[AI 日报](#sec-ai-daily)**
1. [OpenAI 与 Cisco 开源 Linux 运行时 Shirudo](#item-ai-daily-1) ⭐️ 6.8/10
2. [Richpanel 30 天实现 50%客服自动化](#item-ai-daily-2) ⭐️ 6.8/10
3. [OpenAI 探讨内部法务 AI 应用](#item-ai-daily-3) ⭐️ 5.8/10

**[AI 羊毛](#sec-ai-deals)**
1. [Koofr 1TB 终身版 129.99 美元](#item-ai-deals-1) ⭐️ 8.0/10
2. [DevSwarm 创业公司免费 1 年 10 席位](#item-ai-deals-2) ⭐️ 6.0/10

---

## Harness 架构
{: #sec-harness-arch .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-harness-arch" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-harness-arch-1"></a>
### [Codex rust-v0.172.0 发布](https://github.com/openai/codex/releases/tag/rust-v0.172.0) ⭐️ 8.8/10

OpenAI Codex 发布 rust-v0.172.0。本次更新为 agent harness 引入多项核心能力：缓存工具列表的 stdio MCP 服务器默认延迟启动；\`codex exec resume\` 恢复保存的沙箱权限、工作目录与 workspace roots；\`config.toml\` 支持为单个 connected app 工具配置 approval reviewer；新增 Amazon Bedrock Runtime 支持；改进子代理与命令中心导航。同步修复 provider 错误流式上报、跨平台远程会话路径保留等 bug。

github · github-actions\[bot\] · 11月24日 00:03

**「设计要点」** Code Mode 全面迁移至 gRPC host 连接，原 \`code\_mode\_host\_grpc\` 配置项弃用。沙箱准备逻辑下沉至 platform backends，Guardian V3 支持可配置路由与检索策略，并提供 opt-in 内存消息板。

**「改了什么」** stdio MCP 服务器从预启动改为首次工具调用时启动。\`codex exec resume\` 恢复沙箱权限、工作目录与 workspace roots，除非显式覆盖。父轮次中断后，子代理队列消息保留至下一轮。远程会话跨操作系统保留工作目录、可写路径与 workspace roots。

**标签**: `#mcp`, `#tools`, `#sandbox`, `#subagents`, `#permissions`

---

<a id="item-harness-arch-2"></a>
### [pydantic-ai v2.73.0 发布](https://github.com/pydantic/pydantic-ai/releases/tag/v2.73.0) ⭐️ 7.8/10

pydantic-ai v2.73.0 发布。\`Agent.override\`新增\`capabilities\`参数，同时导出\`AgentInstructions\`与\`SourcedInstruction\`类型。OpenAI Responses 的\`input\_transformations\`现在暴露于\`provider\_details\`和模型请求 span，\`openai\`依赖地板升至 3.50.0。新增\`DeprecatedModelWarning\`警告已弃用模型，\`RealtimeSession.append\_voice\_instructions\`支持 GPT-Live 语音交互。

github · dsfaccini · 11月24日 03:53

**「设计要点」** 私有上下文变量\`Agent.\_override\_root\_capability\`改为存储\`\(capability, injected\)\`元组，直接读取需适配。模型请求 span 携带 OpenAI 输入转换元数据，提升可观测性。

**「改了什么」** \`Agent.override\`支持能力配置，\`RealtimeSession\`新增语音指令接口。OpenAI 依赖地板升至 3.50.0，弃用模型触发警告。私有覆盖根能力上下文变量存储结构变更。

**标签**: `#runtime`, `#prefix-cache`, `#permissions`

---

<a id="item-harness-arch-3"></a>
### [openai-agents-python v1.0.0-alpha.2 发布](https://github.com/openai/openai-agents-python/releases/tag/v1.0.0-alpha.2) ⭐️ 7.8/10

OpenAI 发布 Python Agents SDK v1.0.0-alpha.2，引入跨 worker 会话恢复、原生 Codex 审批恢复、工具执行钩子与过滤、Runner 文本脱敏及操作追踪。该版本变更持久化状态格式为 breaking change：alpha.2 读取 alpha.1 的 RunState schema 1.22，但始终写入 schema 1.24，ResumableSession checkpoint 升级至 version 2，alpha.1 无法读取新快照。运行时嵌入 Codex Core rust-v0.166.0，支持 CPython 3.10–3.14，提供 Linux、macOS、Windows 预编译 wheel 并附带 SHA-256 校验。

github · markstuart-oai · 11月23日 20:11

**「设计要点」** 状态管理采用 ResumableSession 配合 ResumableSessionStore（支持 Redis）实现原子条件写入，checkpoint 与 schema 版本绑定，跨 worker 恢复需重建匹配的 model provider、tool declaration、authorization policy、hooks 与 redactor。工具层通过 ToolExecutionConfig 暴露 prepare\_tool\_input、prepare\_tool\_output、prepare\_tool\_declaration 三个钩子，sdk\_only\_tool\_hooks=True 可切断原生 Codex 工作区工具及其审批恢复；manager run 取消时，活跃 Agent.as\_tool\(\) 调用有 250 ms 清理窗口，超时仍会继续运行并产生副作用。追踪层支持 metadata/content 两级 operation\_detail，OpenTelemetry 通过 extra 依赖导出 spans，redact\_text 与 trace\_include\_sensitive\_data 控制敏感数据暴露。

**「改了什么」** 相对 v1.0.0-alpha.1，持久化状态格式升级为 breaking change：RunState schema 从 1.22 升至 1.24，ResumableSession checkpoint 升至 version 2，旧版本无法读取新快照。新增 ResumableSession 跨 worker 恢复会话与待处理审批，支持恢复一个本地原生 Codex exec\_command 或 apply\_patch 审批。新增 ToolExecutionConfig 工具钩子与函数工具过滤，支持 Runner 文本脱敏及 operation\_detail 追踪，嵌入 Codex Core rust-v0.166.0 并加入同步 PreToolUse 失败时阻止原生调度的补丁。

**标签**: `#runtime`, `#tools`, `#permissions`, `#memory`, `#subagents`

---

## Agent 工程师日报
{: #sec-agent-engineer .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-agent-engineer" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-agent-engineer-1"></a>
### [RoboTrack 发布：机器人操作点跟踪基准](https://huggingface.co/blog/allenai/robotrack) ⭐️ 7.8/10

2026 年 11 月 23 日，Allen AI 团队通过 Hugging Face 博客发布 RoboTrack 开源资源包，包含点跟踪基准 RoboTrack-Bench、1500 万条合成训练数据集 RoboTrack-15M、两个新模型 RoboTracker 与 RoboTracker-Warp，以及技术报告、代码和人工标注数据。RoboTrack-Bench 包含 307 段来自 DROID、Ego-Exo4D、MolmoAct 2、EgoVerse 的真实机器人操作视频，共 2522 条人工校验的点轨迹，覆盖杂乱场景、第一/第三人称视角、机械臂与人类手部操作，包含遮挡、小物体跟踪等难点。评估显示 4 款主流跟踪器在该基准上的平均 Jaccard（AJ）得分比现有机器人基准 RoboTAP 低 3.0 至 6.6 分，新发布的 RoboTracker-Warp 在参与评估的 5 个基准中的 4 个上达到当前最优性能，且 AllTracker 得分基于修复其官方评估代码 bug 的结果，RoboTAP 与 Kinetics 的评估采用全标注点方案而非 AllTracker 官方协议。

rss · Hugging Face Blog · 11月23日 17:20

**「为什么重要」** 该基准首次系统覆盖真实机器人操作场景的点跟踪评估需求，现有主流跟踪器在该基准上的普遍性能下降，说明此前机器人跟踪相关基准的评估结果无法直接外推到真实操作场景；目前尚无公开证据证明基于 RoboTrack-15M 训练的跟踪器性能增益可稳定泛化到更多下游机器人任务。

**「可关注」** 现有主流点跟踪模型在真实机器人操作场景下的性能普遍弱于其在现有基准上的表现，且训练数据与目标场景的匹配度对真实场景跟踪效果的影响超过数据规模。

**标签**: `#eval`, `#harness`, `#robotic-manipulation`, `#perception`

---

<a id="item-agent-engineer-2"></a>
### [NariQ 3-bit Qwen3.8-27B 量化发布](https://huggingface.co/nari-labs/Qwen3.8-27B-NariQ-GGUF) ⭐️ 7.0/10

2026 年 11 月 23 日，nari-labs 发布 NariQ 量化方案，为 Qwen3.8-27B 提供 3-bit 及更低比特量化版本，文件大小约 10GB，声称在智能体长程任务、数学、多语言推理、图像理解等场景保留接近 BF16 的性能。公开自测基准显示 3-bit 版本在 DeepSWE、Terminal-Bench 2.1 等智能体任务上得分高于 BF16 基线，2-bit 版本性能明显回落。当前运行需使用其 fork 的 llama.cpp 仓库，暂未支持 Volta/sm\_70 架构显卡，Apple M 系列需自行编译且解码速度慢于 CUDA 方案。

hackernews · toebee · 11月23日 13:42 · [社区讨论](https://news.ycombinator.com/item?id=50611402)

**「为什么重要」** 若该量化方案性能声明可复现，将首次实现 3-bit 及以下量化保留 BF16 级长程智能体任务性能，可大幅降低本地部署大模型智能体的硬件门槛。但当前基准为发布方自报告，且需专用推理框架 fork，实际效果与兼容性尚未得到社区广泛验证。

**「可关注」** 可关注该量化方案的基准性能增益是否来自评估 harness 差异，以及定制 fork 的 llama.cpp 的长期维护与兼容性风险。

**「评论」** 社区对高计算量量化方案的基准可信度普遍存疑，该方案因覆盖多类长程任务、提及 held out 数据获得部分认可；另有用户反馈 Volta 架构不支持、Apple M 系列解码速度慢，还有用户指出 2-bit 版本存在未明确的信息损失问题。

**标签**: `#eval`, `#coding-agent`, `#harness`

---

<a id="item-agent-engineer-3"></a>
### [Anthropic formal-math 发布 VP≠VNP 域上证明](https://github.com/anthropics/formal-math/tree/main/vp-vnp) ⭐️ 7.0/10

2026 年 11 月 23 日，Anthropic 官方 formal-math 项目发布经社区验证的 LLM 辅助原创形式化证明，核心结论为「VP≠VNP 在所有域上成立」，配套开源 LLM 辅助形式化推理工具链。证明基于 Lean 形式化框架完成，社区用户 fons 已公开复现校验仓库，论文未分析该结论与相对化、代数化屏障的关联。该成果对构建推理 Agent、形式化验证工具链及推理评测基准有参考价值，但核心数学结论受众较窄，当前披露的技术细节有限。

hackernews · mikeryan52 · 11月23日 22:09 · [社区讨论](https://news.ycombinator.com/item?id=50620102)

**「为什么重要」** 这是目前公开的少数 LLM 辅助产出的可复核原创形式化数学证明之一，首次在计算复杂度理论核心命题上取得可验证进展；但其对通用数学证明能力的泛化价值尚未得到验证，配套工具链的可复用工程细节披露不足。

**「可关注」** 可关注：Anthropic formal-math 项目开源的 LLM+形式化验证工具链，以及社区已公开的 VP≠VNP 证明复现校验流程，可作为推理 Agent 与形式化工具链建设的参考样本。

**「评论」** 社区普遍认可该证明的原创性与可复现性，部分用户认为这是 LLM 攻克 P vs NP 难题的阶段性成果，也有用户担忧此类成果会冲击传统数学研究生培养；另有用户指出论文未说明结论与相对化、代数化屏障的关联，还有用户将此视为 Anthropic 与 OpenAI 的 AI 能力竞赛产物。

**标签**: `#eval`, `#coding-agent`, `#orchestration`, `#harness`

---

<a id="item-agent-engineer-4"></a>
### [AutoPILOT 实时游戏 harness 发布](https://huggingface.co/papers/2611.28202) ⭐️ 7.0/10

2026-11-24，Hugging Face Daily Papers 收录的论文提出 AutoPILOT，一种面向实时游戏视觉 agent 的 harness。现有 harness（如 VISTA）将每次模型调用限制为至多一个动作，agent 行动频率受限于模型推理速度。AutoPILOT 允许模型在单次调用中输出 primitive action、open-loop macro 或 closed-loop controller，后者可在无进一步模型调用的情况下持续执行。论文同步发布 AFK-Bench，包含 120 款浏览器游戏，用于评估实时游戏 agent。该研究面向 agent harness 与 eval 工程。

rss · Hugging Face Daily Papers · 11月24日 00:00

**「为什么重要」** 当前实时游戏 agent 的性能瓶颈常被归因于模型能力，该论文指出 harness 设计（动作映射与记忆机制）同样关键。AutoPILOT 将模型输出从动作层扩展到控制策略层，为降低端到端延迟提供了新思路。AFK-Bench 的发布也为实时场景下的 agent 评估提供了测试集。

**「可关注」** 可关注：harness 将模型输出从动作层扩展到控制策略层，这一设计选择对实时 agent 延迟的影响。

**标签**: `#harness`, `#eval`, `#coding-agent`

---

<a id="item-agent-engineer-5"></a>
### [RUIBench 发布：RUI 设计可提升 agent 成功率](https://huggingface.co/papers/2611.31115) ⭐️ 7.0/10

Hugging Face Daily Papers 于 2026-11-24 介绍 RUIBench 与 RUIKit。RUIBench 包含 30 个操作任务，覆盖世界知识、上下文学习、发现、动态交互和接触丰富操作 5 个套件。RUIKit 提供 13 种接口，由 6 种动作抽象与 2 种交互形式组合而成。在仿真环境中，仅改变机器人使用接口（RUI），前沿 agent 的操作任务成功率从 45% 提升至 81%；原文对微调模型的数据描述不完整。

rss · Hugging Face Daily Papers · 11月24日 00:00

**「为什么重要」** 该研究表明接口设计可能是 embodied agent 系统中被低估的性能杠杆。仿真结果提示 harness 层的接口选择可能比模型能力本身带来更大的性能波动，但尚未证实对真实机器人系统的实际影响。

**「可关注」** 可关注：在 embodied agent 的 harness 设计中，接口抽象层的选择可能对任务成功率产生显著影响，其权重可能超过模型能力本身的边际提升。

**标签**: `#eval`, `#harness`

---

<a id="item-agent-engineer-6"></a>
### [GameAnything 平台与基准论文发布](https://huggingface.co/papers/2611.29238) ⭐️ 7.0/10

2026 年 11 月 24 日 Hugging Face 每日论文推荐开源智能体平台 GameAnything 及配套基准 GameAnything-Bench，该条目获得 8 次点赞。平台可将多模态灵感转化为现有游戏的可玩扩展，集成编程智能体、独立试玩批评器、持久化开发状态、可复用经验记忆支持迭代开发。基准覆盖多模态参考、游戏创建目标、游戏环境三类维度。公开摘要未提供性能对比或生产环境运行 Trace 等验证信息，相关成果对智能体架构、游戏开发、评测体系方向的研究者与工程师有参考价值。

rss · Hugging Face Daily Papers · 11月24日 00:00

**「为什么重要」** 该工作同时覆盖智能体编排、记忆机制设计与游戏开发评测基准，对相关方向的工程实践有直接参考价值，但尚未有公开性能数据支撑其实际效果。

**「可关注」** 可关注：其整合编程智能体、独立试玩批评器、持久化开发状态与可复用经验记忆的迭代开发架构，以及配套的多模态多环境游戏开发基准设计。

**标签**: `#coding-agent`, `#eval`, `#memory`, `#orchestration`

---

<a id="item-agent-engineer-7"></a>
### [SWE-Gym 训练数据假负向标签研究](https://huggingface.co/papers/2611.30207) ⭐️ 7.0/10

2026 年 11 月 24 日 Hugging Face 每日论文收录了一项编码智能体训练数据质量研究，针对广泛用于强化学习训练的 SWE-Gym 数据集开展审计。研究发现，审计使用两个 LLM 家族筛选疑似错误，且仅当执行复现错误时才计入统计，74%的 9B 基模型从未解决的任务存在假负向奖励标签，即正确修复会被隐藏测试拒绝，该比例在模型偶尔能解决的任务中为 20%。研究通过修复或移除这类问题任务后，等规模、匹配难度的模型在 SWE-bench Verified 等 hold-out 基准上得分提升 2.4 至 2.7 分。

rss · Hugging Face Daily Papers · 11月24日 00:00

**「为什么重要」** 该研究揭示了 SWE-Gym 数据集的系统性假负向标签问题，修正后可稳定提升编码智能体基准表现，对训练数据策展、评测流程设计有直接参考价值。

**「可关注」** 可关注：基于隐藏测试打分的编码智能体训练数据集可能存在系统性假负向标签，需通过执行复现验证任务标签正确性。

**标签**: `#coding-agent`, `#eval`, `#harness`

---

<a id="item-agent-engineer-8"></a>
### [datasette-charts 0.2a0 发布](https://github.com/datasette/datasette-charts/releases/tag/0.2a0) ⭐️ 6.3/10

datasette-charts 0.2a0 于 2026-11-24 发布。该版本新增与 Datasette Agent 的集成，agent 获得绘图工具与图表建议工具。同时新增 decade 时间单位，用于跨越世纪的列分桶。折线图在稀疏数据场景下改为绘制连接线而非孤立点。

github · simonw · 11月24日 04:24

**「为什么重要」** Datasette Agent 集成将图表能力嵌入 agent 工作流，但当前仅影响同时使用两个插件的用户，尚未证实对通用 agent 工程的影响。

**「可关注」** 可关注：datasette-charts 通过 decade 时间单位和稀疏折线图修复，展示了针对特定数据分布（跨世纪、稀疏桶）的渐进式优化路径。

**标签**: `#coding-agent`, `#harness`

---

<a id="item-agent-engineer-9"></a>
### [Z.ai GLM-5.4 发布 首用循环 Transformer](https://simonwillison.net/2026/Nov/23/glm-54/) ⭐️ 5.5/10

2026 年 11 月 23 日，中国 AI 实验室 Z.ai 发布 GLM-5.4 模型，这是其首款面向通用编码任务的循环 Transformer 架构模型，核心机制为权重共享的层组在单次前向传播中多次迭代优化隐状态，可在不增加参数量的前提下加深网络深度。这是近一周内第二款公开采用该架构的模型，此前 11 月 20 日 Thinking Machines Lab 发布的 Inkling 2 Mini 已实现中间层每 token 迭代 3 次，并称该架构对依赖推理质量的 agent coding 任务有潜在收益。目前 GLM-5.4 未开源权重，仅可通过 Z.ai Coding Plan 订阅后访问其 OpenAI 兼容 API（端点 https://api.z.ai/api/v1）使用，暂无法通过常规 API 调用，具体迭代次数等实现细节尚未公开。

rss · Simon Willison · 11月23日 23:40

**「为什么重要」** 该架构在两周内被两家独立实验室落地，说明循环 Transformer 可能是当前提升模型推理深度的可行路径；但 GLM-5.4 尚未公开 coding 任务基准测试、具体迭代次数等关键信息，其实际效果还需进一步验证。

**「可关注」** 可关注：Z.ai OpenAI 兼容 API 已支持 GLM-5.4，但现有主流 LLM 插件（如 llm-zai）尚未适配该模型，若需调用可优先跟踪插件更新或临时自建适配层。

**标签**: `#coding-agent`

---

## AI 日报
{: #sec-ai-daily .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-daily" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-daily-1"></a>
### [OpenAI 与 Cisco 开源 Linux 运行时 Shirudo](https://openai.com/index/introducing-shirudo) ⭐️ 6.8/10

2026 年 11 月 23 日 OpenAI 官方博客发布公告，OpenAI 与 Cisco 联合推出开源 Linux 运行时 Shirudo，该工具用于在团队部署补丁过程中保护正在运行的系统。

rss · OpenAI Blog · 11月23日 21:20

**「为什么重要」** 该工具面向 Linux 系统补丁部署场景的基础设施防护需求，为运维团队提供了新的开源可选方案。

**「可关注」** 可关注：Shirudo 可用于补丁 rollout 阶段的运行系统防护场景。

**标签**: `#lab`, `#industry`, `#open-source`, `#product`

---

<a id="item-ai-daily-2"></a>
### [Richpanel 30 天实现 50%客服自动化](https://openai.com/business/customer-stories/richpanel-ai-customer-support) ⭐️ 6.8/10

OpenAI 官方博客发布客户案例，显示 Richpanel 通过使用 GPT-6 Astra、GPT-6.1 Sol 和 GPT-6 Luna 模型，在 30 天内实现了 50%的客户支持自动化。该案例未披露具体行业细分场景、客服环节覆盖范围及自动化效果的持续稳定性。

rss · OpenAI Blog · 11月23日 08:00

**「为什么重要」** 该案例为 GPT 系列模型在客服自动化场景的落地效果提供了可量化的参考样本，补充了相关模型在商业支持场景的实用验证。

**「可关注」** 可关注：GPT 系列模型在客服场景中工具调用、流程配置与对话能力的结合落地效果。

**标签**: `#lab`, `#model`, `#product`, `#industry`

---

<a id="item-ai-daily-3"></a>
### [OpenAI 探讨内部法务 AI 应用](https://openai.com/business/learn/connected-intelligence-for-in-house-legal) ⭐️ 5.8/10

OpenAI 于 2026 年 11 月 23 日发布官方博客，收录了 OpenAI 员工 Stacey Wang、Craig Bruney，LECG 的 Mary O’Carroll 与 Cooley 的 Richard Segal 的专题讨论。讨论聚焦 AI 在内部法务工作流中的应用，明确提及三个核心方向：帮助团队连接业务上下文、构建可复用工作流、提升外部律所协作效率。

rss · OpenAI Blog · 11月23日 08:00

**「为什么重要」** 该内容是 OpenAI 面向企业法务垂直场景的 AI 应用实践探讨，属于其行业落地探索的一部分。

**「可关注」** 可关注：AI 在内部法务场景的落地路径，包括业务上下文关联、可复用工作流构建、外部律所协作提效三个方向。

**标签**: `#lab`, `#industry`, `#product`

---

## AI 羊毛
{: #sec-ai-deals .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-deals" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-deals-1"></a>
### [Koofr 1TB 终身版 129.99 美元](https://www.appinn.com/koofr-1tb/) ⭐️ 8.0/10

你看到的内容可能由第三方 AI 基于小众软件文章提炼总结而成，可能与原文真实意图存在偏差。不代表小众软件观点和立场。请&lt;a href=&quot;https://www.appinn.com/koofr-1tb/&quot; target=&quot;\_blank&quot;&gt;点击链接阅读原文&lt;/a&gt;细致比对和校验。&lt;br /&gt;&lt;br /&gt;Koofr 云存储提供 10GB 免费额度，支持 WebDAV、Rclone 对接，免费版文件分享限 10 次。当前通过 Stacksocial 使用优惠码 KOOFR 可 129.99 美元购入 1TB 终身版，购买链接已公开。

rss · 小众软件 · 11月24日 03:24

**「为什么重要」** 该优惠为多次返场的限时促销，适合需要低成本长期云存储、或需通过 WebDAV/Rclone 对接备份工具的用户，免费 10GB 额度可先试用再决定是否购入终身版。

**「可关注」** 可关注：rclone 原生支持 Koofr，适合批量备份小文件、或对接自建服务场景，免费 10GB 额度可先验证兼容性。

**标签**: `#free-tier`, `#promo`, `#coupon`, `#api`

---

<a id="item-ai-deals-2"></a>
### [DevSwarm 创业公司免费 1 年 10 席位](https://devswarm.ai/startups/) ⭐️ 6.0/10

DevSwarm 面向创业公司推出免费席位促销，提供最多 10 个席位免费使用 1 年，领取无需投资方资质。当前公开页面未披露优惠有效期、完整申请要求等关键细节。

rss · HN Free API / Credits · 11月23日 20:21

**「为什么重要」** 目前仅见官方单方发布的促销公告，无社区验证的领取案例，适合有 DevSwarm 使用需求的创业公司关注后续细节补充。

**「可关注」** 可关注：该优惠面向创业公司，无需投资方资质，但当前缺少有效期、完整申请要求等关键信息，建议等待官方补充细节后再申请。

**标签**: `#promo`, `#free-tier`, `#limited-free`

---