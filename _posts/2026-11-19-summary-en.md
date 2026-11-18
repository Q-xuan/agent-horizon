---
layout: default
title: "Horizon Summary: 2026-11-19 (EN)"
date: 2026-11-19
lang: en
---

> From 213 items, 17 important content pieces were selected

---

**Agent Harness Architecture**
1. [Mastra core 1.84.0 发布](#item-harness-arch-1) ⭐️ 8.8/10
2. [Codex rust-v0.170.0 发布](#item-harness-arch-2) ⭐️ 7.8/10
3. [openai-agents-python v0.25.0 发布](#item-harness-arch-3) ⭐️ 7.8/10

**AI Agent Engineer**
1. [Gemini 4 Neon 发布](#item-agent-engineer-1) ⭐️ 8.8/10
2. [DaisyRose-27B 发布 后训练效率提升](#item-agent-engineer-2) ⭐️ 8.3/10
3. [MoE SSD流式推理实现180B模型32GB运行](#item-agent-engineer-3) ⭐️ 7.8/10
4. [Genie 4 正式可用](#item-agent-engineer-4) ⭐️ 7.8/10
5. [OpenAI 芯片设计案例发布](#item-agent-engineer-5) ⭐️ 7.0/10
6. [curl C 转 Rust：AI 重写滞后维护](#item-agent-engineer-6) ⭐️ 7.0/10
7. [GPT-6.2 Astra/Sol 发布，效率领先](#item-agent-engineer-7) ⭐️ 7.0/10
8. [Xing 4 系列模型 Ascend 训练细节公开](#item-agent-engineer-8) ⭐️ 7.0/10
9. [SIM 机制支持 Harness 持续自改进](#item-agent-engineer-9) ⭐️ 7.0/10

**AI Daily**
1. [Codex Sandbox 支持三平台](#item-ai-daily-1) ⭐️ 7.8/10
2. [OpenAI 披露前沿AI全周期风险管理实践](#item-ai-daily-2) ⭐️ 7.8/10
3. [OpenAI模型推进芯片设计优化](#item-ai-daily-3) ⭐️ 7.8/10
4. [OpenAI 合作 Le Groupe Figaro 引入法媒内容](#item-ai-daily-4) ⭐️ 6.8/10

**AI Deals**
1. [Gemini Tasks 个人助理免费开放](#item-ai-deals-1) ⭐️ 7.0/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [Mastra core 1.84.0 发布](https://github.com/mastra-ai/mastra/releases/tag/%40mastra/core%401.84.0) ⭐️ 8.8/10

Mastra core 1.84.0 发布实验性 Storage Version 2。agent 与 evented workflow 的持久化格式改为 header 加逐步骤行，仅写入增量数据。在 @mastra/pg 环境下，16 次工具调用的运行发布消息从 98 MB 降至 11 MB，存储写入从 75 MB 降至 3.1 MB，运行时间从 3.9 秒降至 2.7 秒。同步引入自动 workflow 崩溃恢复循环，通过 leader election lease 与 broker-aware 重递机制恢复分布式执行。

github · PaulieScanlon · Nov 18, 10:36

**「设计要点」** Storage Version 2 运行时消息仅携带上一步结果与状态变更，引擎按需从存储加载完整上下文，降低序列化与传输开销。恢复循环由 \`startWorkers\(\)\` 启动，leader 通过存储适配器中的租约行选举，仅 leader 执行扫描；Redis/Valkey Streams 与 Google Cloud Pub/Sub 通过 \`pubsub.redeliversUnacked\` 标志委托 broker 重递未确认消息，避免多实例重复执行。

**「改了什么」** agent 与 evented workflow 支持 \`storageVersion: 2\` 增量持久化，\`result.steps\(\)\` 与 \`getState\(\)\` 标准化为异步；\`startWorkers\(\)\` 启动崩溃恢复循环，通过存储租约选举 leader，Redis/Valkey/Google Pub/Sub 委托 broker 重递未确认消息。Knowledge 新增 \`movePage\(\)\` 与 \`reembed\(\)\` API，发布 \`@mastra/platform\` 托管客户端，MCP server 支持 Studio 视图嵌入。Breaking changes: Knowledge 作用域匹配改为精确单段，\`@mastra/factory\` 移除 \`newestOpenPullRequestNumber\` 与 \`intake.evaluator\`，\`@mastra/playground-ui\` 移除 \`ListSearch\`、\`SearchFieldBlock\`、\`SectionCard\`、\`CardHeading\`。

**Tags**: `#runtime`, `#memory`, `#subagents`

---

<a id="item-harness-arch-2"></a>
### [Codex rust-v0.170.0 发布](https://github.com/openai/codex/releases/tag/rust-v0.170.0) ⭐️ 7.8/10

OpenAI Codex 发布 rust-v0.170.0，核心更新覆盖 MCP、sandbox、runtime 与 TUI 四个组件。MCP 新增跨环境同名服务器隔离与 OAuth 竞态修复；sandbox 修复 Windows 权限保留、子线程限制继承及权限配置文档；runtime 优化 Cloud 会话断流重连与恢复轮次保留；TUI 新增 WebRTC 实时语音通话支持。此外修复 WebSocket 超大请求回退 HTTP、文件搜索去重等问题。

github · github-actions\[bot\] · Nov 18, 03:40

**「设计要点」** 权限模型通过 permission profiles 统一 TUI 与会话 admission 的沙盒权限转换，修复子线程继承与 Windows 文件权限保留问题。网络与工具层分别针对 WebSocket 消息大小限制做显式回退、MCP 服务器按环境隔离，减少无效重传与跨环境配置冲突。

**「改了什么」** 新增 WebRTC TUI 实时语音通话协商、实验性跨环境同名 MCP 服务器隔离、OpenTelemetry HTTP 导出器自动刷新认证头。修复 MCP OAuth 凭证竞态、Cloud 会话断流自动重连、Windows 沙盒文件权限与运行时注册恢复、WebSocket oversized 请求立即回退 HTTP、文件搜索去重及线程搜索片段空白处理。

**Tags**: `#mcp`, `#sandbox`, `#runtime`, `#permissions`, `#tools`

---

<a id="item-harness-arch-3"></a>
### [openai-agents-python v0.25.0 发布](https://github.com/openai/openai-agents-python/releases/tag/v0.25.0) ⭐️ 7.8/10

openai-agents-python v0.25.0 正式发布，移除 beta Runloop 沙箱提供方，调整 Pydantic 运行上下文检查点行为。RunState schema 升级至 1.22，支持嵌套 agent-tool 审批恢复与输出防护。OpenAIResponsesCompactionSession 默认模型从 gpt-4.1 改为 gpt-6-luna，MCP v2 Streamable HTTP 支持并发请求，演示 REPL 现可单独批准或拒绝工具调用。Runloop 用户需在切换前备份工作区数据，跨 worker 共享检查点的应用需先升级读取端。

github · openai-sdks\[bot\] · Nov 18, 00:22

**「设计要点」** Pydantic 检查点现保留默认值与原地编辑，进程本地资源需自定义序列化。Runner handoff 通过 failure\_error\_function 提供可选错误恢复，省略时保持原有异常传播。

**「改了什么」** 移除 Runloop 沙箱提供方，用户需迁移至 Modal 等替代方案或停留在 0.24.0，提供方特定会话与快照需单独数据迁移。Pydantic 检查点语义变更，跨 worker 场景需先升级读取端。OpenAIResponsesCompactionSession 默认模型改为 gpt-6-luna，gpt-6-sol 与 gpt-6-luna 的 Chat Completions 工具请求在未指定 effort 时默认非推理模式。演示 REPL 现支持单独批准或拒绝工具调用，失败与未完成的 Responses 调用保留提供方上报的 token 用量。

**Tags**: `#sandbox`, `#memory`, `#runtime`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [Gemini 4 Neon 发布](https://deepmind.google/blog/introducing-gemini-4-neon/) ⭐️ 8.8/10

Google DeepMind 于 2026-11-18 正式发布 Gemini 4 Neon。社区信息显示，Neon 整体智能评分高于 Carbon，但 Carbon 仍定位为长程推理模型；Neon 在 CritPt 等研究级推理评估中得分较低。OpenRouter 实测吞吐量约 127 token/秒，约为 Carbon（46 token/秒）的 2.7 倍。官方未公开完整技术规格、API 变更或具体能力边界。

rss · Google DeepMind · Nov 18, 21:35

**「为什么重要」** Gemini 4 Neon 可能成为 agent 工程的新骨干模型选项。其速度优势与能力定位差异，直接影响 harness 配置、工具链选择和评估基准设计。但官方细节缺失，具体影响仍待验证。

**「可关注」** 可关注：若 agent 工作流对吞吐量敏感，Neon 的实测速度显著优于 Carbon；若任务依赖长程研究级推理，需自行验证 Neon 在 CritPt 类评估中的实际表现。

**「评论」** Hacker News 用户对频繁的新模型命名表示疲劳，难以快速对应使用场景。讨论聚焦于 Neon 与 Carbon 的定位分化：frontier 模型正走向「整体智能」与「长程专用能力」的细分。有用户对比 Anthropic Opus 5.5，认为后者在通用智能体感上仍更优。

**Tags**: `#coding-agent`, `#eval`, `#harness`

---

<a id="item-agent-engineer-2"></a>
### [DaisyRose-27B 发布 后训练效率提升](https://huggingface.co/blog/RadixArk/daisyrose-27b-pushing-the-frontier-of-post-trainin) ⭐️ 8.3/10

2026年11月18日，RadixArk 发布其首个模型 DaisyRose-27B，基于 Qwen3.8-27B 打造，采用 Apache 2.0 许可证，使用自研 Miles 框架做强化学习训练，针对长周期智能体任务优化。该模型保留基座的架构、分词器、对话模板、图像理解能力与 256K token 上下文窗口，训练耗时 18 天、使用 144 张 H200 GPU，仅用 1200 个精选任务，支持最长 1M token 的训练会话，核心 eval 指标 Terminal-Bench 4.1 pass@1 从 5.6% 提升至 12.0%，其余推理、指令遵循、编码基准均有提升。官方推荐使用 SGLang 搭配 DSpark 推测解码部署该模型，各基准得分取 BF16 与 FP8 运行结果的较高值，两者差异均小于 1 分，训练过程中通过 harness summarization 折叠长轨迹以提升效率。

rss · Hugging Face Blog · Nov 18, 19:54

**「为什么重要」** 该模型验证了少量精选长周期 agent 任务结合异步强化学习，就能在 27B 参数规模上实现 agent 核心性能翻倍，同时开源了训练框架 Miles 和可复用的部署方案；尚未证实的影响是该性能提升是否可泛化到非训练任务集，以及是否存在针对 Terminal-Bench 4.1 的过拟合风险，社区已出现相关讨论。

**「可关注」** RadixArk 自研异步 RL 框架 Miles 在 144 张 H200 上跑出 37% MFU，较开源 Megatron 实现节省 57% GPU 时间、端到端吞吐高 2 倍，且长周期训练效率稳定。

**「评论」** 社区存在分歧：部分用户认可性能提升，但质疑仅用 1200 个任务训练可能存在基准过拟合风险；另有用户指出当前无 GGUF 格式暂无法本地测试，同时提到同赛道有 Sabi-noema 等竞品模型。

**Tags**: `#coding-agent`, `#eval`, `#harness`

---

<a id="item-agent-engineer-3"></a>
### [MoE SSD流式推理实现180B模型32GB运行](https://huggingface.co/blog/moe-expert-streaming) ⭐️ 7.8/10

2026年11月18日Hugging Face官方博客发布MoE推理优化技术，通过SSD流式传输MoE专家，支持180B参数MoE模型在32GB内存设备上运行，token生成性能仅比Strata推理引擎基线低6%。方案基于Transformers PR \#50717实现，通过预分配设备张量槽池复用现有grouped\_mm内核，支持专家3比特离线量化、8线程异步读取与路由器预取下一层专家，适配标准MoE专家布局模型。此前Transformers原生Accelerate offload路径对MoE模型支持极差，同场景下OLMoE-1B-7B的推理速度仅为0.16 tok/s，该方案将其提升至34.6 tok/s，接近vanilla Transformers的38.1 tok/s水平。当前API仍在与Transformers维护者讨论，仅验证了Qwen3.8-Flash-Next在32GB Mac M5上的运行效果，dense层8比特量化比BF16高0.2%困惑度，模型转换耗时约5小时，该方案降低了本地大MoE模型的硬件门槛，面向需要本地部署模型的Agent工程师。

rss · Hugging Face Blog · Nov 18, 00:00

**「为什么重要」** 该方案首次让Transformers原生支持大参数MoE模型的SSD专家流式推理，将本地运行180B MoE模型的内存门槛从数百GB降至32GB，且性能损失控制在6%以内，为依赖本地模型的Agent工具链提供了可落地的优化路径。

**「可关注」** 可关注：通过预分配槽池复用现有grouped\_mm内核、搭配8线程异步SSD读取与路由器预取，可在不修改核心推理内核的前提下实现MoE专家流式offload，平衡开发成本与推理性能。

**Tags**: `#memory`, `#harness`, `#inference`, `#model-optimization`

---

<a id="item-agent-engineer-4"></a>
### [Genie 4 正式可用](https://deepmind.google/blog/genie-4-is-now-available/) ⭐️ 7.8/10

Google DeepMind 于 2026-11-18 正式发布 Genie 4。该版本是其面向 AI agent 开发与评估的交互式环境生成平台的最新主要版本。当前公开材料未披露具体技术改进、性能数据或迁移限制。受影响群体包括 AI agent 工程师及评估 harness 开发者。

rss · Google DeepMind · Nov 18, 18:13

**「为什么重要」** 作为头部实验室的核心基础设施更新，Genie 4 可能影响 agent 训练与评估工具链的选型方向。但具体能力变化与兼容性细节尚未公开，实际影响待验证。

**「可关注」** 可关注：官方已发布主要版本，但技术细节与性能数据尚未公开，实际迁移或集成需等待后续披露。

**Tags**: `#eval`, `#harness`

---

<a id="item-agent-engineer-5"></a>
### [OpenAI 芯片设计案例发布](https://openai.com/index/advancing-chip-design-with-our-models/) ⭐️ 7.0/10

2026 年 11 月 18 日，OpenAI 发布案例研究《Advancing chip design with our models》，展示模型在芯片设计中的应用。HN 讨论透露具体 Agent 用法：将芯片设计视为软件设计问题，用 Agent 编写电路生成与 EDA 流程自动化软件，并 babysit 多轮数小时仿真。从业者 skyberrys 确认该模式有效，但指出设计以模拟电路为主，RTL 仅占小部分；用户 zardo 指出未公开 RISC-V 设计。原文章缺乏深层技术实现细节、基准测试或可复现工件。

hackernews · vighneshiyer · Nov 18, 17:45 · [Discussion](https://news.ycombinator.com/item?id=50549493)

**「为什么重要」** 该案例提供了 Agent 在 EDA 自动化与长时仿真监控中的实际使用模式，对 Coding Agent 工程师有参考价值。但原文章未提供可复现的实现细节，目前影响仍限于思路验证阶段。

**「可关注」** 将芯片设计转化为软件设计任务，用 Agent 生成电路脚本与 EDA 自动化代码，并接管多轮长时仿真的监控与干预。

**「评论」** 讨论呈现分歧：部分用户关注 AI 公司与客户竞争及模型 withheld 的问题，而芯片设计从业者 skyberrys 确认了 Agent 辅助 EDA 与仿真 babysitting 的实用性，同时指出设计主体为模拟电路。另有用户质疑未公开 RISC-V 设计。

**Tags**: `#coding-agent`, `#orchestration`

---

<a id="item-agent-engineer-6"></a>
### [curl C 转 Rust：AI 重写滞后维护](https://simonwillison.net/2026/Nov/18/daniel-stenberg/) ⭐️ 7.0/10

2026年11月17日curl项目负责人Daniel Stenberg在官方博客披露，AI代理耗时约3周完成18.5万行curl C代码向34万行Rust代码的重写，同期人类团队合并300+提交、修复200+缺陷与多个安全漏洞，AI重写未覆盖这些同期迭代内容。

rss · Simon Willison · Nov 18, 15:58

**「为什么重要」** 该案例是活跃维护代码库的AI重写真实对照实证，清晰展示当前AI代码迁移工具无法同步跟踪上游持续迭代的核心局限，为AI编码代理开发、代码迁移工作流设计、代理能力评测提供可参考依据。

**「可关注」** 可关注：活跃代码库的AI重写任务需额外设计上游变更同步机制，避免重写结果与上游维护进度脱节。

**Tags**: `#coding-agent`, `#eval`, `#security`

---

<a id="item-agent-engineer-7"></a>
### [GPT-6.2 Astra/Sol 发布，效率领先](https://latent.space/p/ainews-gpt-6-2-astra-the-2-frontier-model-is-better-and-20-600-cheaper-but-has-mixed-reviews-6-2-sol/) ⭐️ 7.0/10

OpenAI 于 2026-11-18 发布 GPT-6.2 Astra 与 Sol。Astra 在 Artificial Analysis Intelligence Index 中得 62 分，排名第二，仅次于 Fable 5.2 的 65 分；Sol 在该测试中每任务成本约为 Astra 的 15%。API 定价为 Astra 输入 $8/M、缓存输入 $0.40/M、输出 $40/M，Sol 为 $2/M、$0.10/M、$10/M，两者均支持 1M 上下文与 128K 输出上限。模型已上线 ChatGPT Work、Codex 及 API（gpt-6.2-astra、gpt-6.2-sol）。早期测试者对输出质量有分歧，部分指出 RL 伪影明显。

rss · Latent Space · Nov 18, 10:19

**「为什么重要」** 对 AI agent 工程师而言，Sol 的低成本可能显著降低高吞吐量工作负载的推理开销，但需权衡 Astra 更高智能与潜在 RL 伪影之间的取舍。Anthropic 的 Fable 5.2 仍保持智能指数领先，而 OpenAI 在单位智能成本上暂时占优。

**「可关注」** 可关注：Sol 的 $2/M 输入与 $10/M 输出定价在长输出或批量 agent 任务中可能具备成本优势，但建议先在小范围工作流中验证其输出稳定性，因早期测试者报告了 RL 伪影和子代理协作问题。

**Tags**: `#coding-agent`, `#eval`

---

<a id="item-agent-engineer-8"></a>
### [Xing 4 系列模型 Ascend 训练细节公开](https://huggingface.co/papers/2611.22115) ⭐️ 7.0/10

Xing 4 is a large language model series extending the TeleChat lineage, presented in a technical report covering architecture design and training infrastructure on Ascend chips using MindSpore. The report examines tradeoffs in sparse activation, attention design, model depth and width, and speculative decoding for reasoning and agentic tasks. Pretraining infrastructure builds on MindSpore HyperParallel with topology-aware hybrid sharding, efficient distributed optimizer execution, and coordinated management of long-sequence workloads and activation memory, including CPU affinity and core isolation. The work also details reasoning and agentic post-training approaches.

rss · Hugging Face Daily Papers · Nov 18, 00:00

**「为什么重要」** This report provides concrete technical details on building frontier agentic models on domestic AI hardware and frameworks, relevant for engineers working with alternative training stacks. The specific infrastructure choices around sharding strategies, memory management, and CPU isolation offer actionable reference points for large-scale training system design on specialized hardware.

**「可关注」** Note: The topology-aware hybrid sharding and CPU affinity configurations in MindSpore HyperParallel offer direct reference value for deploying long-sequence agent training on Ascend.

**Tags**: `#coding-agent`, `#eval`, `#architecture`

---

<a id="item-agent-engineer-9"></a>
### [SIM 机制支持 Harness 持续自改进](https://huggingface.co/papers/2611.18856) ⭐️ 7.0/10

该论文提出 Self-Improvement Memory （SIM） 机制，用于 harness 优化器，解决策略模型或基准变化时优化过程难以延续的问题。SIM 按重复出现的 harness 问题对编辑进行分组，记录编辑理由、预测与实际结果及评估上下文，支持持续递归自改进 （CRSI）。实验在四个领域验证该机制。论文 2026-11-18 发布于 Hugging Face Daily Papers，获 29 次点赞，尚无社区评论。

rss · Hugging Face Daily Papers · Nov 18, 00:00

**「为什么重要」** 当前 harness 优化研究常假设策略模型与基准固定，但实际部署中二者常变化。SIM 通过为优化器建立可复用的编辑历史，使优化过程能在模型或基准演进时延续，减少从零开始的重复试错。

**「可关注」** 可关注：SIM 将记忆机制附着于优化器而非策略模型，通过记录编辑理由与评估上下文，尝试解决 harness 在模型迭代中的知识继承问题。

**Tags**: `#harness`, `#memory`, `#eval`

---

## AI Daily

<a id="item-ai-daily-1"></a>
### [Codex Sandbox 支持三平台](https://openai.com/index/inside-the-codex-sandbox) ⭐️ 7.8/10

OpenAI 官方博客发文介绍 Codex 沙箱功能。该功能支持在 macOS、Linux、Windows 三平台运行用户机器指令，同时执行用户自定义控制的文件系统与网络访问限制。

rss · OpenAI Blog · Nov 18, 08:00

**「可关注」** 可关注：Codex 沙箱支持 macOS、Linux、Windows 三平台，文件系统与网络访问限制由用户自定义控制。

**Tags**: `#lab`, `#product`

---

<a id="item-ai-daily-2"></a>
### [OpenAI 披露前沿AI全周期风险管理实践](https://openai.com/index/managing-frontier-ai-risk) ⭐️ 7.8/10

OpenAI 发布官方博客，披露前沿AI从训练到部署的全周期风险管理实践。文章披露四项核心措施：模型对齐、沙箱隔离、阻断式 safeguards 及监控。这是头部实验室系统性公开全生命周期风控细节。

rss · OpenAI Blog · Nov 18, 06:00

**「为什么重要」** 该披露为行业提供前沿AI安全实践框架，回应监管与公众对AI风险的关切。

**「可关注」** 可关注：OpenAI 将 safeguards 设为&quot;阻断式&quot;而非仅 advisory，体现从预防到拦截的思路转变。

**Tags**: `#lab`, `#policy`, `#industry`

---

<a id="item-ai-daily-3"></a>
### [OpenAI模型推进芯片设计优化](https://openai.com/index/advancing-chip-design-with-our-models) ⭐️ 7.8/10

OpenAI官方博客发布案例研究，披露其旗下模型（含GPT-6 Astra）已完成Jalapeño硅片的电路优化，同时实现RISC-V核心设计改进。该成果展示了AI辅助芯片设计领域的最新进展。

rss · OpenAI Blog · Nov 18, 00:00

**「为什么重要」** 这是官方公开的AI大模型在芯片设计场景的落地成果，证明大模型已具备硬件设计领域的实用能力，为AI辅助芯片研发提供了可参考的实践案例。

**「可关注」** 可关注：OpenAI模型已在芯片电路优化、RISC-V核心设计等硬件设计场景落地应用。

**Tags**: `#model`, `#lab`, `#industry`

---

<a id="item-ai-daily-4"></a>
### [OpenAI 合作 Le Groupe Figaro 引入法媒内容](https://openai.com/index/le-groupe-figaro-and-openai-announce-partnership) ⭐️ 6.8/10

OpenAI 与法国媒体集团 Le Groupe Figaro 达成合作，将《费加罗报》新闻内容引入 ChatGPT。系统生成摘要与摘录，并附上指向原始报道的链接。该消息于 2026 年 11 月 18 日由 OpenAI 官方博客发布。

rss · OpenAI Blog · Nov 18, 00:00

**Tags**: `#lab`, `#industry`, `#product`

---

## AI Deals

<a id="item-ai-deals-1"></a>
### [Gemini Tasks 个人助理免费开放](https://blog.google/innovation-and-ai/products/gemini-app/tasks-in-gemini-free-new-features/) ⭐️ 7.0/10

Google has officially made the Tasks personal assistant feature in the Gemini app free for all users. Publicly available materials do not specify usage quotas, region restrictions, or an expiration date for this free offering.

rss · HN Free API / Credits · Nov 18, 20:20

**「为什么重要」** This is a free launch of a practical feature from a mainstream consumer AI product, allowing users to access basic personal assistant task management capabilities at no extra cost, which has tangible utility for ordinary users.

**「可关注」** 可关注：The free feature has no publicly announced usage limits, region coverage scope, or follow-up paid adjustment plans yet. Users are advised to confirm whether their region supports the function before use.

**Tags**: `#free-tier`, `#promo`

---