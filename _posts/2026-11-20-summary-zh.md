---
layout: default
title: "Horizon Summary: 2026-11-20 (ZH)"
date: 2026-11-20
lang: zh
---

> 从 185 条内容中筛选出 13 条重要资讯。

<nav id="ah-toc" class="ah-toc" aria-label="目录"><span class="ah-toc-title">目录</span><ul><li><a href="#sec-harness-arch"><span class="ah-toc-name">Harness 架构</span><span class="ah-toc-count">3条</span></a></li><li><a href="#sec-agent-engineer"><span class="ah-toc-name">Agent 工程师日报</span><span class="ah-toc-count">6条</span></a></li><li><a href="#sec-ai-daily"><span class="ah-toc-name">AI 日报</span><span class="ah-toc-count">4条</span></a></li></ul></nav>

---

**[Harness 架构](#sec-harness-arch)**
1. [ADK Python v2.15.0 发布](#item-harness-arch-1) ⭐️ 8.8/10
2. [pydantic-ai v2.71.0 发布](#item-harness-arch-2) ⭐️ 7.8/10
3. [adk-go v1.10.0 发布](#item-harness-arch-3) ⭐️ 5.8/10

**[Agent 工程师日报](#sec-agent-engineer)**
1. [HF Daily Papers 提出 Resolution Hypothesis](#item-agent-engineer-1) ⭐️ 7.0/10
2. [llm-gemini 0.38 支持 Gemini 4 Neon](#item-agent-engineer-2) ⭐️ 6.3/10
3. [Gemini 4 Neon 发布 旧模型退役](#item-agent-engineer-3) ⭐️ 6.0/10
4. [ALIVE 交互式流视频模型论文公开](#item-agent-engineer-4) ⭐️ 6.0/10
5. [StatePortal 提出 GUI 测试 checkpoint 合成](#item-agent-engineer-5) ⭐️ 6.0/10
6. [StrideWorld 基准发布](#item-agent-engineer-6) ⭐️ 5.5/10

**[AI 日报](#sec-ai-daily)**
1. [OpenAI 公开 Performance Factory 系统](#item-ai-daily-1) ⭐️ 7.8/10
2. [Tunix 多轮智能体 RL 流水线发布](#item-ai-daily-2) ⭐️ 7.8/10
3. [Streaming DiLoCo 登陆 MaxText 支持跨地域训练](#item-ai-daily-3) ⭐️ 7.8/10
4. [GitHub 2026 开源贡献数据公布](#item-ai-daily-4) ⭐️ 5.8/10

---

## Harness 架构
{: #sec-harness-arch .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-harness-arch" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-harness-arch-1"></a>
### [ADK Python v2.15.0 发布](https://github.com/google/adk-python/releases/tag/v2.15.0) ⭐️ 8.8/10

ADK Python v2.15.0 发布。新增 per-user/session 沙箱隔离、6x 加速的 RAG 内存搜索、Google Maps 与 BigQuery 新工具、multi-run 可靠性与部分工具调用准确率评测指标。同时移除 Visual Agent Builder，并将 \`run\_live\` 工具调用移至后台任务以保持语音流响应。实验性 \`BufferedSessionService\` 与 \`FsspecArtifactService\` 分别优化会话写入延迟和统一制品存储后端。

github · Jacksunwei · 11月19日 22:59

**「设计要点」** \`BaseEnvironment\` 通过 \`ctx: Context\` 与 \`scope\` 枚举实现 user/session 级沙箱初始化锁，避免并发等待。\`BufferedSessionService\` 将慢速 I/O 移出关键路径，\`FsspecArtifactService\` 统一本地与云存储接口，评测层新增 \`pass\_hat\_k\` 与 \`tool\_parameter\_match\`。

**「改了什么」** 新增 \`GoogleMapsToolset\` 与支持项目级表发现的 \`BigQueryToolset.ask\_data\_insights\`，\`run\_live\` 后台执行工具调用并支持 \`send\_context\_update\` 热更新，\`VertexAiRagMemoryService\` 搜索延迟降低最多 6 倍。破坏性变更包括移除 Visual Agent Builder 及 \`McpInstructionProvider\` 不再自动注入 \`session.state\` 参数。

**标签**: `#sandbox`, `#memory`, `#tools`, `#eval`, `#runtime`

---

<a id="item-harness-arch-2"></a>
### [pydantic-ai v2.71.0 发布](https://github.com/pydantic/pydantic-ai/releases/tag/v2.71.0) ⭐️ 7.8/10

pydantic-ai v2.71.0 正式发布，引入多项破坏性 API 变更与运行时改进。PeerNetwork 重命名为 PeerConnection，StackOne 弃用 api\_key 转而使用 auth 字段。新增 Stav、Otari 两个 MCP 网关提供商，并将远程 CodeMode 执行改为 Temporal activity 以避免长代码片段触发死锁检测。同时扩展工具输出限制、权限规则与 harness 能力集。

github · dsfaccini · 11月19日 02:13

**「设计要点」** 远程 CodeMode 回合通过 Temporal activity 执行，将长任务与主运行线程解耦，避免死锁检测器误判。MCPToolsetClient 的进程内服务器臂改为协议类型化，兼容 FastMCP 3 与 4 的严格 pyright 检查。

**「改了什么」** PeerNetwork 更名为 PeerConnection，StackOne 的 api\_key 参数弃用。新增 StavProvider、OtariProvider 两个 MCP 网关，ToolOutputLimits 支持 grep\_tool\_result 与字节单位读取，远程 CodeMode 改为 Temporal activity 执行。

**标签**: `#runtime`, `#tools`, `#mcp`

---

<a id="item-harness-arch-3"></a>
### [adk-go v1.10.0 发布](https://github.com/google/adk-go/releases/tag/v1.10.0) ⭐️ 5.8/10

google/adk-go 发布 v1.10.0，发布日期 2026-11-16。本次更新仅包含 bug fix backport，未声明新功能或 breaking changes。修复覆盖 adkrest REST server、A2A remote agent/server、llminternal（instruction、live connection、streaming、tool call 等）、runner、session、artifact/memory 等组件。changelog 内容被截断，session 部分描述不完整。

github · adk-go-bot · 11月19日 13:38

**「改了什么」** 相对 v1.9.0 仅做问题修复。adkrest 组件 backport REST server、trigger 及 Agent Engine 修复；A2A 组件修复 remote agent 与 server 行为；llminternal 修复 instruction 处理、live connection 输入、streaming aggregator、tool call 与 callback 逻辑；runner 修复 run loop；configurable 组件为 workflow node refs 应用 config\_path 限制。CLI、launcher、CI、依赖、文档、模型、插件、遥测及 memory 相关组件同步修复。无新增公开接口。

**标签**: `#runtime`, `#a2a`

---

## Agent 工程师日报
{: #sec-agent-engineer .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-agent-engineer" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-agent-engineer-1"></a>
### [HF Daily Papers 提出 Resolution Hypothesis](https://huggingface.co/papers/2611.23068) ⭐️ 7.0/10

2026 年 11 月 19 日 Hugging Face Daily Papers 汇总了一篇 Agent 进化领域的实证研究论文，该论文获 35 次 upvote，提出 Resolution Hypothesis，核心结论是 Agent 进化停滞的核心瓶颈是噪声评测（noisy evaluation）无法可靠区分优质与有害候选产物，而非提案质量不足。该结论通过覆盖 7 种进化方法、6 款模型、累计超 1000 万次 LLM 调用的大规模实验验证，在候选选择（筛选效果与随机选择无差异）与更高层级的评测分数使用场景均得到支持，对 Agent 评测体系设计与进化工具链优化有直接参考价值。

rss · Hugging Face Daily Papers · 11月19日 00:00

**「为什么重要」** 当前 Agent 进化方法在不同任务上表现波动大、难以自举，该研究通过大规模实证明确了瓶颈根因是评测噪声而非提案质量，可指导后续优化方向。

**「可关注」** 可关注：当前 Agent 进化 pipeline 的候选选择环节，若依赖现有 noisy evaluation 打分，筛选效果可能接近随机，需优先优化评测可靠性。

**标签**: `#eval`, `#harness`, `#agent-evolution`

---

<a id="item-agent-engineer-2"></a>
### [llm-gemini 0.38 支持 Gemini 4 Neon](https://github.com/simonw/llm-gemini/releases/tag/0.38) ⭐️ 6.3/10

simonw 发布 llm-gemini 0.38。该版本在 llm CLI 中新增 Gemini 4 Neon 模型支持，用户可通过 \`llm -m gemini-4-neon\` 直接调用。此次更新合并了 \#164，但发布说明未展开具体 API 行为或限制。

github · simonw · 11月18日 23:59

**「为什么重要」** llm 插件生态持续跟进新模型发布。当前仅确认模型可用，尚未看到性能基准或兼容性说明。

**「可关注」** 可关注：独立 llm 插件仓库成为新模型接入的快速通道，但需自行验证输出格式与限流策略。

**标签**: `#llm`, `#gemini`, `#harness`, `#tooling`

---

<a id="item-agent-engineer-3"></a>
### [Gemini 4 Neon 发布 旧模型退役](https://latent.space/p/ainews-gemini-4-neon-gdm-s-opus-sol-contender/) ⭐️ 6.0/10

Google DeepMind 于 2026 年 11 月 19 日发布 Gemini 4 Neon，这是其 7 周内推出的第 4 款 Gemini 4 系列模型，体积小于同系列更早的 Carbon 模型，但在部分蒸馏、强化学习相关的基准测试中表现更优。同期退役 1.5 个月前发布的 Argon 模型，以及 Gemini 1-3 代的 Pro、Flash 全产品线，调整了以化学元素命名的系列层级规则。该模型支持 100 万 token 上下文窗口，定价为输入每百万 token 3 美元、缓存输入 0.15 美元、输出 15 美元，已上线付费 Gemini API、AI Studio、Android Studio 等平台，首日集成 Cursor、GitHub Copilot、LangChain Managed Deep Agents 等开发工具。

rss · Latent Space · 11月19日 07:07

**「为什么重要」** 这是 Google DeepMind 近期核心的基座模型更新，直接面向 coding agent 开发者和企业用户，旧 Gemini 1-3 及 Argon 模型的退役将推动现有集成方进行模型迁移。其首日即接入 Cursor、GitHub Copilot 等主流编码工具，Agent Arena 等专项基准的表现也为 coding agent 基座选型提供了新的可验证参考。

**「可关注」** Gemini 4 Neon 在 Agent Arena 中得分 1336 分、steerability 排名第二，median 任务成本 2.82 美元；其 Code Migration 任务平均轮次仅 160 轮，低于同系列更早的 Carbon、Hydrogen 模型，但对应任务得分低于二者，早期测试中还出现 57 次容量错误与 4 次运行停滞，需结合实际场景验证稳定性与效率的平衡。

**标签**: `#coding-agent`

---

<a id="item-agent-engineer-4"></a>
### [ALIVE 交互式流视频模型论文公开](https://huggingface.co/papers/2611.21366) ⭐️ 6.0/10

2026 年 11 月 19 日，Hugging Face Daily Papers 公开 arXiv 论文《ALIVE: Making Streaming Video Models Interactive》，提出支持主动监控、流任务协调、反馈寻求交互的交互式流视频 LLM ALIVE。研究团队构建 ALIVE-SFT-288K、ALIVE-RL-3K 两套数据集开展两阶段训练：对比监督微调学习响应时机与方式，基于行为对齐信用分配（BACA）的强化学习优化多轮交互中的决策、回复与沉默策略。同时提出 FSI-Bench 评估基准，用于测试反馈寻求能力与后续任务完成效果，ALIVE 在四个公开基准及 FSI-Bench 上取得当前最优成绩。目前公开内容缺少深度技术实现细节、生产级性能数据，对编码智能体、工具链开发的直接指导有限。

rss · Hugging Face Daily Papers · 11月19日 00:00

**「为什么重要」** 该研究的多轮交互设计模式、BACA 训练方法、FSI-Bench 评估思路有潜力迁移至通用智能体架构、训练与评估流程，但当前公开内容尚未提供可直接应用于编码智能体、Harness 开发的可操作细节，需阅读全文进一步验证。

**「可关注」** 可关注：ALIVE 的多轮交互设计、BACA 信用分配方法及 FSI-Bench 评估思路，或可迁移至通用智能体训练与评估场景。

**标签**: `#eval`, `#orchestration`, `#multi-turn-interaction`

---

<a id="item-agent-engineer-5"></a>
### [StatePortal 提出 GUI 测试 checkpoint 合成](https://huggingface.co/papers/2611.23257) ⭐️ 6.0/10

Hugging Face Daily Papers 于 2026-11-19 介绍预印本论文《StatePortal: Agentic Checkpoint Synthesis for Testing Deep States in Interactive Software》。该论文提出 StatePortal agent，可从自然语言功能测试用例和目标源代码的只读访问中自动合成 checkpoint，用于恢复 GUI 交互软件的深度状态（deep state）。Checkpoint 通过 onboarding agent 自动绑定或合成的 per-application hook 恢复，无需手写 hook 代码。该工作为未经过同行评审的预印本，缺乏完整技术细节和性能数据，非生产就绪工具，对 eval 和 harness 设计的实际影响待验证。

rss · Hugging Face Daily Papers · 11月19日 00:00

**「为什么重要」** 对于需要反复到达深度 GUI 状态的测试流程，StatePortal 的 checkpoint 合成思路理论上可降低重复交互成本。但论文未提供性能基准或与现有方案的对比，实际收益尚未证实。

**「可关注」** 可关注：per-application hook 的自动绑定机制，或可减少 GUI agent 测试中手写状态恢复代码的工作量。

**标签**: `#eval`, `#harness`, `#coding-agent`

---

<a id="item-agent-engineer-6"></a>
### [StrideWorld 基准发布](https://huggingface.co/papers/2611.24408) ⭐️ 5.5/10

2026-11-19，Hugging Face Daily Papers 介绍 StrideWorld benchmark，用于评估交互式视频世界模型。该基准针对现有评估方法使用 post-hoc fitted references（从测试视频自身帧重建场景或自由尺度对齐相机轨迹）的缺陷——这类参考会吸收渐进式场景变形与步速、路线长度变化，导致错误被掩盖。StrideWorld 改用运动前固定的参考，分别以起始视图的真实几何评估场景刚性，以每个动作的步幅评估动作一致性。当前材料为截断摘要，未提供完整技术细节、性能数据或实现指针。

rss · Hugging Face Daily Papers · 11月19日 00:00

**「为什么重要」** StrideWorld 针对现有基准的评估盲区提出固定参考方案，但当前材料仅为截断摘要，未披露具体性能指标或实现方式，对多数 agent 工程师暂无直接可执行价值。

**「可关注」** 可关注：现有交互式视频世界模型基准使用 post-hoc fitted references 可能掩盖场景变形与动作不一致，StrideWorld 改用运动前固定参考分别评估场景刚性与动作一致性，但需查阅完整论文获取可复现的实现细节。

**标签**: `#eval`

---

## AI 日报
{: #sec-ai-daily .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-daily" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-daily-1"></a>
### [OpenAI 公开 Performance Factory 系统](https://openai.com/index/how-openai-performance-factory-keeps-chatgpt-fast) ⭐️ 7.8/10

OpenAI 官方博客首次公开其打造的 Performance Factory 系统。该系统是基于 Codex 驱动的工作流，可自动发现并修复性能问题，用于保障 ChatGPT 的运行速度。

rss · OpenAI Blog · 11月19日 08:00

**「为什么重要」** 这是 OpenAI 首次公开其内部用于保障 ChatGPT 服务速度的自动化性能优化体系，为行业大模型服务的性能治理提供了可参考的实践样本。

**「可关注」** 可关注：Codex 驱动的工作流在自动化性能排查与修复场景的落地实践。

**标签**: `#lab`, `#product`, `#industry`

---

<a id="item-ai-daily-2"></a>
### [Tunix 多轮智能体 RL 流水线发布](https://developers.googleblog.com/multi-turn-agentic-reinforcement-learning-with-tunix-and-gemma-4-on-google-tpus/) ⭐️ 7.8/10

Google Developers 官方发布 Tunix 框架多轮智能体强化学习（RL）流水线，新增多轮工具调用 LLM 智能体训练能力，支持在单块 Cloud TPU v6e-8 上运行 Gemma 4 E2B 完成训练，完整代码已公开。此前 Tunix 仅支持监督微调（SFT）与单轮组相对策略优化（GRPO），本次扩展了多轮 agentic RL 能力。实测 Plane Strike 棋盘游戏场景中，未微调 Gemma 4 E2B 胜率仅 9.4%、平均耗时 22.44 步；经 100 步多轮智能体 GRPO 训练后，胜率提升至 95%，平均步数降至约 16 步。

rss · Google Developers AI · 11月19日 00:00

**「为什么重要」** 这是 Tunix 框架首次官方支持多轮工具调用智能体的强化学习训练，配套完整可运行代码与实测效果验证，降低了多轮智能体 RL 的落地门槛。

**「可关注」** 可关注：Tunix 已封装 Gemma 4 原生工具调用模板与多轮对话消息拼接逻辑，并提供现成 ToolEnvironment、ToolAgent 抽象，无需自定义即可适配工具调用智能体训练。

**标签**: `#model`, `#lab`, `#product`, `#open-source`

---

<a id="item-ai-daily-3"></a>
### [Streaming DiLoCo 登陆 MaxText 支持跨地域训练](https://developers.googleblog.com/distributed-llm-training-across-metros-streaming-diloco-in-maxtext/) ⭐️ 7.8/10

Google DeepMind 与 Google Research 联合开发的分布式低通信优化算法 DiLoCo 已在开源 JAX LLM 训练框架 MaxText 中实现原生支持，包含 Streaming DiLoCo 变体，可解决广域网高延迟、低带宽场景下的跨地域数据中心 LLM 训练通信瓶颈。该方案将模型参数拆分为 P 个不重叠碎片，每 H 步同步单个碎片，避免全模型同步的周期性带宽尖峰。在 Qwen3-32B 跨 2 个 TPU v5p-32 切片的测试中，10Gbit/s 严重拥塞场景下 Streaming DiLoCo 步时为 5.76s，较标准数据并行提升 9.57 倍，且消除每 H 步的同步气泡；针对 Qwen3-30B-A3B、Gemma4-26B-A4B 两种 MoE 架构的 4000 步预训练测试显示，其验证损失与同步数据并行持平甚至略优。启用需配置 \`enable\_diloco: true\`、\`enable\_streaming\_diloco: true\`，推荐将参数碎片数、同步周期设为模型层数+1，搭配 Nesterov 动量外优化器。

rss · Google Developers AI · 11月19日 00:00

**「为什么重要」** 传统大模型训练依赖单地域高带宽紧耦合集群，物理与成本约束下扩展难度大，DiLoCo 将训练与单地域高带宽 fabric 解耦，为跨地域低成本算力调度提供了可行路径，且开源集成到 MaxText 降低了落地门槛。

**「可关注」** MaxText 已原生集成 Vanilla 与 Streaming DiLoCo，无需额外中心参数服务器，仅需修改 YAML 配置或 CLI 参数即可启用，推荐将参数碎片数、同步周期设为模型层数+1，外优化器采用学习率 0.3-0.7、动量 0.9 的 Nesterov 动量 SGD。

**标签**: `#lab`, `#open-source`, `#model`, `#industry`

---

<a id="item-ai-daily-4"></a>
### [GitHub 2026 开源贡献数据公布](https://github.blog/open-source/maintainers/the-best-things-in-open-source-are-built-together/) ⭐️ 5.8/10

GitHub 官方博客公布 2026 年平台公开贡献达 25 亿次，为 2025 年 11.2 亿次的两倍以上。过去一年全类型仓库代码提交次数达 179 亿次，合并 PR 达 13 亿次，较此前两年大幅增长。同期 GitHub 发布两款新开源工具：由内部项目转开源的、可与 Copilot 协同做原型设计的 Replica 设计 harness，以及含 ACCESSIBILITY.md 文件用于追踪无障碍进度的 Open Source Accessibility Framework。

rss · GitHub Blog · 11月19日 16:00

**「为什么重要」** 公开贡献与提交量的大幅增长，印证开源仍是开发者构建、共享工具的核心载体；两款新工具分别覆盖设计协作与无障碍合规需求，适配当前 AI 辅助开发与代码量激增的场景。

**「可关注」** 可关注：两款新开源工具均支持自定义修改，可依据团队工作流直接取用或二次开发。

**标签**: `#open-source`, `#industry`

---