---
layout: default
title: "Horizon Summary: 2026-11-20 (EN)"
date: 2026-11-20
lang: en
---

> From 185 items, 13 important content pieces were selected

---

**Agent Harness Architecture**
1. [ADK Python v2.15.0 发布](#item-harness-arch-1) ⭐️ 8.8/10
2. [pydantic-ai v2.71.0 发布](#item-harness-arch-2) ⭐️ 7.8/10
3. [adk-go v1.10.0 发布](#item-harness-arch-3) ⭐️ 5.8/10

**AI Agent Engineer**
1. [HF Daily Papers 提出 Resolution Hypothesis](#item-agent-engineer-1) ⭐️ 7.0/10
2. [llm-gemini 0.38 支持 Gemini 4 Neon](#item-agent-engineer-2) ⭐️ 6.3/10
3. [Gemini 4 Neon 发布](#item-agent-engineer-3) ⭐️ 6.0/10
4. [ALIVE 流视频交互模型论文公开](#item-agent-engineer-4) ⭐️ 6.0/10
5. [StatePortal 论文：GUI 深度状态测试的智能体检查点合成](#item-agent-engineer-5) ⭐️ 6.0/10
6. [StrideWorld 基准评估交互式世界模型](#item-agent-engineer-6) ⭐️ 5.5/10

**AI Daily**
1. [OpenAI 公开 Performance Factory](#item-ai-daily-1) ⭐️ 7.8/10
2. [Tunix 多轮 Agentic RL 支持](#item-ai-daily-2) ⭐️ 7.8/10
3. [MaxText 支持 Streaming DiLoCo 跨地域训练](#item-ai-daily-3) ⭐️ 7.8/10
4. [GitHub 2026 开源数据发布](#item-ai-daily-4) ⭐️ 5.8/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [ADK Python v2.15.0 发布](https://github.com/google/adk-python/releases/tag/v2.15.0) ⭐️ 8.8/10

ADK Python v2.15.0 发布。引入按用户或会话隔离的沙箱，RAG 内存搜索延迟降低最多 6 倍。\`adk eval\` 新增多运行可靠性指标和部分工具参数评分，同时集成 \`GoogleMapsToolset\` 与扩展 \`BigQueryToolset\`。ADK Web 移除 Visual Agent Builder，\`McpInstructionProvider\` 改为显式传递提示参数。

github · Jacksunwei · Nov 19, 22:59

**「设计要点」** \`BaseEnvironment\` 通过 \`scope\`（\`SHARED\`/\`USER\`/\`SESSION\`）将初始化锁粒度从全局细化到用户或会话，避免并发启动等待。\`BufferedSessionService\` 将慢速存储写入移出 agent turn 关键路径，\`run\_live\` 将工具调用移入后台任务以保持语音流响应，\`BaseLlmConnection.send\_context\_update\` 支持 mid-session 更新系统指令和工具。

**「改了什么」** v2.15.0 细化沙箱隔离到用户或会话，RAG 内存搜索加速最多 6 倍，\`adk eval\` 新增多运行可靠性和部分工具参数评分。\`run\_live\` 后台执行工具调用以保持语音流响应，同时移除 Visual Agent Builder、硬化 \`McpInstructionProvider\` 参数传递，并默认启用动态指令路由。

**Tags**: `#sandbox`, `#memory`, `#tools`, `#eval`, `#runtime`

---

<a id="item-harness-arch-2"></a>
### [pydantic-ai v2.71.0 发布](https://github.com/pydantic/pydantic-ai/releases/tag/v2.71.0) ⭐️ 7.8/10

pydantic-ai v2.71.0 发布，含破坏性 API 变更、MCP 网关扩展与运行时改进。\`PeerNetwork\` 重命名为 \`PeerConnection\`，\`StackOne\` 弃用 \`api\_key\` 改用 \`auth\`。新增 \`StavProvider\`、\`Otari\` 网关，\`ToolOutputLimits\` 支持 \`grep\_tool\_result\` 与字节读取。远程 \`CodeMode\` 改由 Temporal activity 执行，避免长片段触发死锁检测器。

github · dsfaccini · Nov 19, 02:13

**「设计要点」** 远程 CodeMode 执行迁移至 Temporal activity 层，隔离长片段运行。Harness 新增 \`PermissionRule\`、\`ReportToolErrors\`、\`RequireVerification\` 等运行时控制能力，统一工具审批与错误处理流程。

**「改了什么」** 本版本重命名 \`PeerNetwork\` 为 \`PeerConnection\`，弃用 \`StackOne.api\_key\`，新增 \`StavProvider\`、\`Otari\` 网关与 \`ToolBridge\` 机制。远程 \`CodeMode\` 改由 Temporal activity 执行，Harness 层新增 \`PermissionRule\`、\`ReportToolErrors\`、\`RequireVerification\`、\`Goal\` 等运行时控制能力。

**Tags**: `#runtime`, `#tools`, `#mcp`

---

<a id="item-harness-arch-3"></a>
### [adk-go v1.10.0 发布](https://github.com/google/adk-go/releases/tag/v1.10.0) ⭐️ 5.8/10

google/adk-go 发布 v1.10.0 正式版。本次更新仅包含 backport 的 bug fix，覆盖 adkrest REST server、A2A remote agent/server、llminternal、runner、session 等组件。未公布新功能或 breaking changes，完整 changelog 被截断，无法获取各修复的详细描述。该版本对 agent harness runtime 与 A2A 协议实现有参考价值。

github · adk-go-bot · Nov 19, 13:38

**「改了什么」** v1.10.0 从 v1.9.0 backport 了多组 bug fix，涉及 adkrest \(REST server、trigger、Agent Engine\)、A2A remote agent/server、agent/llmagent/workflow agent、artifact/memory/preloadmemorytool、CLI/launcher/CI/dependency/docs、model/plugin/telemetry、configurable workflow node refs、llminternal \(instruction、live connection、streaming、tool call\)、runner run loop 及 session service。未引入新功能或 breaking changes。

**Tags**: `#runtime`, `#a2a`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [HF Daily Papers 提出 Resolution Hypothesis](https://huggingface.co/papers/2611.23068) ⭐️ 7.0/10

2026年11月19日，Hugging Face Daily Papers汇总了一篇Agent进化领域的实证研究，提出Resolution Hypothesis，核心结论是Agent进化停滞的主因是noisy evaluation无法可靠区分优质与有害候选产物，而非提案质量不足。研究通过覆盖7种进化方法、6款模型、累计超1000万次LLM调用的大规模实验，在候选选择与更高层级的评估得分使用两个场景均验证了该假设，其中候选选择环节的筛选效果不优于随机。该结论直接影响Agent评测体系设计与进化pipeline的优化方向。

rss · Hugging Face Daily Papers · Nov 19, 00:00

**「为什么重要」** 当前Agent进化方法普遍存在跨论文效果波动、特定任务无法自举的实践痛点，该研究将进化停滞的核心瓶颈从「提案生成能力不足」转移到「评估信号不可靠」，直接指向现有评测harness的噪声问题，为优化Agent进化流程提供了明确的归因方向，尚未验证具体优化方案的效果。

**「可关注」** 可关注：当前Agent进化pipeline的性能瓶颈可能不在proposer模块，而在评估环节的噪声控制，可优先排查评测信号的区分度与稳定性。

**Tags**: `#eval`, `#harness`, `#agent-evolution`

---

<a id="item-agent-engineer-2"></a>
### [llm-gemini 0.38 支持 Gemini 4 Neon](https://github.com/simonw/llm-gemini/releases/tag/0.38) ⭐️ 6.3/10

simonw 于 2026-11-18 发布 llm-gemini 0.38，为 llm CLI 插件新增 Gemini 4 Neon 模型支持，调用命令为 \`llm -m gemini-4-neon\`。本次更新未披露其他代码变更或兼容性调整，技术细节有限。该变更直接影响通过 llm 工具链调用 Gemini 模型的开发者。

github · simonw · Nov 18, 23:59

**「为什么重要」** Gemini 4 Neon 接入 llm CLI 工具链，扩展了本地开发环境的模型选项。但当前版本说明未提供性能基准或 API 差异信息，实际效果待验证。

**「可关注」** 可关注：Gemini 4 Neon 在 llm 插件中的实际调用延迟、token 计费及输出格式是否与现有 Gemini 模型保持一致。

**Tags**: `#llm`, `#gemini`, `#harness`, `#tooling`

---

<a id="item-agent-engineer-3"></a>
### [Gemini 4 Neon 发布](https://latent.space/p/ainews-gemini-4-neon-gdm-s-opus-sol-contender/) ⭐️ 6.0/10

Google DeepMind 发布 Gemini 4 Neon，这是七周内推出的第四款 Gemini 4 模型。前代 Argon 已退役，Gemini 1-3 的 Pro 与 Flash 线路停止服务。Neon 定价为每百万 tokens 输入 $3、缓存输入 $0.15、输出 $15，上下文窗口 1M tokens，提供四级 effort 设置。该模型已上线付费 Gemini API、AI Studio、Android Studio、Gemini for business 及 Antigravity，并首日接入 Cursor、GitHub Copilot 与 LangChain Managed Deep Agents。独立基准测试显示，Neon 在 Agent Arena 以 1,336 分位居第二，Vals Index 得分 70.9% 排名第二，CursorBench 4.1 得分 63.7%；但在 Code Migration 任务中平均 160 轮即结束，得分低于 Carbon 与 Hydrogen。

rss · Latent Space · Nov 19, 07:07

**「为什么重要」** Gemini 4 Neon 以每任务 $2.82 的中位数成本进入 Agent Arena，并首日接入 Cursor、GitHub Copilot 等主流编码工具，直接影响 coding agent 的模型选型与成本结构。其七周内第四款模型的发布节奏显示 base model 迭代加速，但真实 agent 工作流中的稳定性与容量表现仍需更多验证。

**「可关注」** 可关注：Neon 在 Antigravity 早期测试中实现 93% 输入缓存命中率且能遵循避免终端的指令，但出现 57 次容量错误与 4 次 stalled runs，提示 agent harness 需准备重试与降级策略。

**Tags**: `#coding-agent`

---

<a id="item-agent-engineer-4"></a>
### [ALIVE 流视频交互模型论文公开](https://huggingface.co/papers/2611.21366) ⭐️ 6.0/10

2026年11月19日Hugging Face Daily Papers推送arXiv论文2611.21366，提出名为ALIVE的交互式流视频模型，支持主动监控、流式任务协调、反馈寻求三类交互能力，对AI Agent工程师、流视频模型研究者及智能体训练评估方向从业者有参考价值。该模型采用两阶段训练流程：先用规模为288K的ALIVE-SFT数据集做对比监督微调，再用规模为3K的ALIVE-RL数据集配合行为对齐信用分配（BACA）强化学习方法优化多轮交互中的决策、响应与沉默策略，同时推出面向反馈寻求类视频任务的评估基准FSI-Bench。目前公开信息显示ALIVE在4个公开基准与FSI-Bench上取得当前最优成绩，但未披露深度技术实现细节、生产级性能数据，对coding agent、harness开发者的直接落地指导有限。

rss · Hugging Face Daily Papers · Nov 19, 00:00

**「为什么重要」** 虽然流视频是垂直 niche 场景，但ALIVE的多轮交互设计逻辑、BACA强化学习信用分配方法、FSI-Bench评估设计，有潜力迁移到通用智能体的架构设计、训练流程与评估体系，不过目前仅处于论文公开阶段，实际落地效果尚未验证。

**「可关注」** 可关注：ALIVE的多轮交互设计、BACA信用分配方法及FSI-Bench评估思路，或可迁移至通用agent的训练与评估流程，但需跟进全文获取可落地细节。

**Tags**: `#eval`, `#orchestration`, `#multi-turn-interaction`

---

<a id="item-agent-engineer-5"></a>
### [StatePortal 论文：GUI 深度状态测试的智能体检查点合成](https://huggingface.co/papers/2611.23257) ⭐️ 6.0/10

StatePortal 是一个智能体，通过合成可复用检查点来降低 GUI 交互软件深度状态测试的成本。它接受自然语言功能测试用例和只读源代码访问作为输入，生成可版本化、可重放的检查点工件。状态恢复依赖一个每应用钩子，由引导智能体一次性绑定或合成，无需手写钩子代码。该工作为未审稿预印本（arXiv 2611.23257，2026-11-19），当前摘要 truncated，缺少完整技术细节、性能数据和评估方法。

rss · Hugging Face Daily Papers · Nov 19, 00:00

**「为什么重要」** 深度 GUI 状态测试的瓶颈在于到达深度状态需要长交互历史，且该成本在多次提交中重复出现。若 StatePortal 的方法如描述般有效，可能为自渲染引擎（不暴露标准 DOM 或辅助功能树）的 harness 设计者减少手写钩子代码的工作量，但此收益尚未在现有摘要中得到验证。

**「可关注」** 可关注：两阶段设计——从自然语言和源代码合成检查点，随后一次性绑定钩子——暗示了一种无需每次提交手写自动化代码即可摊销深度状态访问成本的设计模式。

**Tags**: `#eval`, `#harness`, `#coding-agent`

---

<a id="item-agent-engineer-6"></a>
### [StrideWorld 基准评估交互式世界模型](https://huggingface.co/papers/2611.24408) ⭐️ 5.5/10

Hugging Face Daily Papers 于 2026-11-19 推介 StrideWorld 基准，针对交互式视频世界模型提出固定运动前参考的评估方案。该基准以起始视图真实几何评估场景刚性，以动作步幅评估动作一致性，旨在解决现有基准使用事后拟合参考掩盖渐进变形与节奏偏差的问题。当前材料为截断二次摘要，未包含完整技术细节、性能数据或实现指针，对基于世界模型的 agent 工程师有窄相关但需查阅原文获取可操作信息。

rss · Hugging Face Daily Papers · Nov 19, 00:00

**「为什么重要」** 该基准指出现有评估方法存在系统性漏检风险，对依赖交互式世界模型的 agent 系统可靠性评估有直接参考价值。但材料未提供具体性能指标或开源实现，实际影响尚待完整论文验证。

**「可关注」** 可关注：若当前评估交互式世界模型时使用事后拟合参考，可能漏检场景变形与动作不一致，需核查基准的参考生成时机。

**Tags**: `#eval`

---

## AI Daily

<a id="item-ai-daily-1"></a>
### [OpenAI 公开 Performance Factory](https://openai.com/index/how-openai-performance-factory-keeps-chatgpt-fast) ⭐️ 7.8/10

OpenAI 官方博客公开 Performance Factory 系统。该系统基于 Codex 驱动的工作流，可自动发现并修复性能问题，用于保障 ChatGPT 的运行速度。博客文章详细介绍了这套性能优化系统的构建方式。

rss · OpenAI Blog · Nov 19, 08:00

**「为什么重要」** 这是 OpenAI 公开的 ChatGPT 性能优化系统具体实现，属于一手实验室产品动态，揭示了 Codex 在工作流自动化中的实际应用案例。

**「可关注」** 可关注：Codex 驱动的工作流在性能优化自动化中的具体实现方式。

**Tags**: `#lab`, `#product`, `#industry`

---

<a id="item-ai-daily-2"></a>
### [Tunix 多轮 Agentic RL 支持](https://developers.googleblog.com/multi-turn-agentic-reinforcement-learning-with-tunix-and-gemma-4-on-google-tpus/) ⭐️ 7.8/10

Google Developers 发布 Tunix 多轮智能体强化学习流水线，支持在 Cloud TPU v6e-8 上用 Gemma 4 E2B 训练工具调用型 LLM 智能体。该流水线扩展了 Tunix 此前仅有的监督微调（SFT）与单轮 GRPO 能力。在 Plane Strike 任务上，Gemma 4 E2B-it 原生胜率 9.4%、平均 22.44 步；经 100 步 agentic GRPO 训练后胜率升至 95%，平均步数降至约 16 步。完整代码已公开。

rss · Google Developers AI · Nov 19, 00:00

**「为什么重要」** 这是 Google 首次为 Tunix 提供官方多轮智能体 RL 流水线，填补了此前仅支持单轮优化的空白。实验显示，该流水线在 Cloud TPU v6e-8 上完成 100 步训练后，可将 Gemma 4 E2B 在 Plane Strike 任务上的胜率从 9.4% 提升至 95%。

**「可关注」** 多轮 rollout 的变长生成瓶颈可通过 vllm-tpu 的 server 模式与 prefix caching 缓解，Tunix 已将其封装为默认配置。

**Tags**: `#model`, `#lab`, `#product`, `#open-source`

---

<a id="item-ai-daily-3"></a>
### [MaxText 支持 Streaming DiLoCo 跨地域训练](https://developers.googleblog.com/distributed-llm-training-across-metros-streaming-diloco-in-maxtext/) ⭐️ 7.8/10

Google DeepMind与Google Research联合开发的分布式低通信优化算法DiLoCo已集成至开源JAX LLM训练框架MaxText，包含基础版与Streaming升级版，解决跨地域数据中心广域网高延迟、低带宽场景下的LLM训练通信瓶颈。在Qwen3-32B（bfloat16精度）测试中，将2块TPU v5p-32切片跨切片带宽限速至10Gbit/s时，标准数据并行每步耗时7.55秒，Streaming DiLoCo（参数分片数P=同步周期H=65）稳定在5.76秒/步，相对DP实现9.57倍加速，且消除了每H步的全模型同步气泡。目前已在Qwen3-30B-A3B、Gemma4-26B-A4B两个MoE架构上完成4000步预训练验证，验证损失持平甚至略优于同步数据并行，无需额外中心参数服务器。

rss · Google Developers AI · Nov 19, 00:00

**「为什么重要」** 该方案首次在开源框架中验证了低通信优化算法在跨地域WAN场景下训练大模型的可行性，打破了传统LLM训练对单集群高带宽互联 fabric 的规模限制，为分布式训练提供了可落地的低成本路径。

**「可关注」** 可关注：在MaxText中开启Streaming DiLoCo仅需配置enable\_diloco、enable\_streaming\_diloco为true，同时将num\_diloco\_fragments与diloco\_sync\_period设为模型层数+1，outer优化器采用Nesterov动量SGD（学习率0.3-0.7，动量0.9）即可运行，无需额外参数服务器。

**Tags**: `#lab`, `#open-source`, `#model`, `#industry`

---

<a id="item-ai-daily-4"></a>
### [GitHub 2026 开源数据发布](https://github.blog/open-source/maintainers/the-best-things-in-open-source-are-built-together/) ⭐️ 5.8/10

GitHub 官方博客 2026 年 11 月 19 日发布文章，公布 2026 年公开 GitHub 贡献达 25 亿次，为上一年 11.2 亿次的两倍以上。过去一年全类型仓库代码提交次数达 179 亿次，合并 PR 达 13 亿次，分别较两年前增长超 3 倍。文章同时开源发布设计工具 Replica 与开源无障碍框架两个新项目，提及 2025 年增长最快的开源项目中 60% 为 AI 相关。

rss · GitHub Blog · Nov 19, 16:00

**「为什么重要」** 本次公开的 2026 年开源贡献数据是官方发布的行业量化基准，两个新开源项目分别覆盖 AI 设计原型、开源无障碍落地场景，为相关领域开发者提供可参考的落地案例。

**「可关注」** 可关注：GitHub 新开源的 Replica 设计工具支持与 Copilot 协同迭代原型，且开源可自定义适配团队工作流；新推出的 ACCESSIBILITY.md 文件为项目无障碍目标提供了统一的公开落点。

**Tags**: `#open-source`, `#industry`

---