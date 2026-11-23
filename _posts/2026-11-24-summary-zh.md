---
layout: default
title: "Horizon Summary: 2026-11-24 (ZH)"
date: 2026-11-24
lang: zh
---

> 从 219 条内容中筛选出 20 条重要资讯。

<nav id="ah-toc" class="ah-toc" aria-label="目录"><span class="ah-toc-title">目录</span><ul><li><a href="#sec-harness-arch"><span class="ah-toc-name">Harness 架构</span><span class="ah-toc-count">4条</span></a></li><li><a href="#sec-agent-engineer"><span class="ah-toc-name">Agent 工程师日报</span><span class="ah-toc-count">7条</span></a></li><li><a href="#sec-ai-daily"><span class="ah-toc-name">AI 日报</span><span class="ah-toc-count">6条</span></a></li><li><a href="#sec-ai-deals"><span class="ah-toc-name">AI 羊毛</span><span class="ah-toc-count">3条</span></a></li></ul></nav>

---

**[Harness 架构](#sec-harness-arch)**
1. [OpenCode v2.4.0 发布](#item-harness-arch-1) ⭐️ 8.3/10
2. [OpenAI Agents Python v1.0.0-alpha.2 发布](#item-harness-arch-2) ⭐️ 7.8/10
3. [Graphiti v0.32.0 发布](#item-harness-arch-3) ⭐️ 7.8/10
4. [SWE-agent mini-swe-agent](#item-harness-arch-4) ⭐️ 5.0/10

**[Agent 工程师日报](#sec-agent-engineer)**
1. [NariQ 发布 Qwen3.8-27B 低比特量化](#item-agent-engineer-1) ⭐️ 8.0/10
2. [Clover-35B-A3B-Preview 技术报告发布](#item-agent-engineer-2) ⭐️ 8.0/10
3. [Hugging Face 发布 Agentic Eval 构建指南](#item-agent-engineer-3) ⭐️ 7.8/10
4. [AgentRoboCritic 动作级评估框架提出](#item-agent-engineer-4) ⭐️ 7.0/10
5. [HF Intent Contracts 授权](#item-agent-engineer-5) ⭐️ 7.0/10
6. [HF 每日论文：MemOnce 可扩展 LLM 记忆架构](#item-agent-engineer-6) ⭐️ 6.0/10
7. [RoboTrack 开源 点跟踪模型与基准发布](#item-agent-engineer-7) ⭐️ 5.8/10

**[AI 日报](#sec-ai-daily)**
1. [OpenAI 与 Cisco 联合推出开源运行时 Shirudo](#item-ai-daily-1) ⭐️ 7.8/10
2. [Anthropic EFS 公测 支持零数据留存](#item-ai-daily-2) ⭐️ 7.8/10
3. [Claude Ship beta 发布](#item-ai-daily-3) ⭐️ 7.8/10
4. [Anthropic 发布 Claude Code 企业安全指南](#item-ai-daily-4) ⭐️ 7.8/10
5. [Google 语义治理策略防御代理劫持](#item-ai-daily-5) ⭐️ 7.8/10
6. [KPMG 谈客户敏感数据场景的 AI 应用](#item-ai-daily-6) ⭐️ 5.8/10

**[AI 羊毛](#sec-ai-deals)**
1. [Google Gemini 黑五五折 AI Pro/Plus 年费](#item-ai-deals-1) ⭐️ 8.0/10
2. [DevSwarm 创业团队 1 年 10 席免费](#item-ai-deals-2) ⭐️ 6.0/10
3. [Fly.io 免费计划上线](#item-ai-deals-3) ⭐️ 6.0/10

---

## Harness 架构
{: #sec-harness-arch .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-harness-arch" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-harness-arch-1"></a>
### [OpenCode v2.4.0 发布](https://github.com/anomalyco/opencode/releases/tag/v2.4.0) ⭐️ 8.3/10

OpenCode agent harness 发布 v2.4.0，引入内置持久化桌面浏览器运行时、MCP 事件触发自动化及视频生成能力。浏览器运行时基于 Chromium，支持导入 Chrome、Edge、Firefox、Safari 的登录态与历史记录，标签页重启后存活，agent 可直接读写和驱动页面。自动化支持定时器、cron 及 MCP 事件触发，通过 \`/automation\` 命令管理，\`&quot;automations&quot;: false\` 可全局关闭，视频生成默认模型由 \`experimental.video\_generate.model\` 指定。

github · github-actions\[bot\] · 11月23日 09:22

**「设计要点」** 插件加载恢复异步非阻塞，SDK 端点不再等待插件初始化完成，直接返回已加载结果，客户端需通过 \`\*.updated\` 事件或轮询 \`plugin.list\` 感知就绪。存储层将 assistant parts 拆分为独立行写入，\`experimental.part\_rows: false\` 可回退。

**「改了什么」** 新增内置 Chromium 浏览器运行时与 MCP 事件驱动自动化，\`generate\_video\` 工具支持后台视频渲染。插件自动更新扩展至版本范围与 Git 分支，图像工具重命名为 \`generate\_image\`，Code Mode 会话工具路径迁移至 \`tools.opencode.session.\*\`，TUI 插件需 OpenTUI 0.9.4+，GitHub Copilot 改用 \`COPILOT\_GITHUB\_TOKEN\`。

**标签**: `#runtime`, `#tools`, `#mcp`

---

<a id="item-harness-arch-2"></a>
### [OpenAI Agents Python v1.0.0-alpha.2 发布](https://github.com/openai/openai-agents-python/releases/tag/v1.0.0-alpha.2) ⭐️ 7.8/10

OpenAI 发布 Python Agents SDK v1.0.0-alpha.2，这是一个 GitHub 专属预览版，捆绑 openai-agents 与原生 Codex 运行时。本次更新引入持久化状态格式 breaking change：读取 alpha.1 的 schema 1.22，但总是写入 schema 1.24，导致 alpha.1 无法读取新快照。新增跨 worker 会话恢复、原生 Codex 审批恢复、工具执行钩子与过滤、Runner 文本脱敏及 OpenTelemetry 追踪。运行时嵌入 Codex Core rust-v0.166.0，支持 CPython 3.10–3.14，提供 Linux x86-64/ARM64、macOS Apple silicon 与 Windows x64 预编译 wheel。

github · markstuart-oai · 11月23日 20:11

**「设计要点」** 运行时嵌入 Codex Core rust-v0.166.0，通过 RunConfig.tool\_execution 的 ToolExecutionConfig 控制工具执行钩子与声明过滤。记忆层采用 ResumableSession 配合 ResumableSessionStore 或 RedisSessionStore 实现跨 worker 状态恢复，持久化状态格式升级至 schema 1.24。权限与追踪层支持原生 Codex 审批恢复、文本脱敏回调及 OpenTelemetry 导出，Agent.as\_tool\(\) 在取消时保留 250 ms 清理窗口。

**「改了什么」** 相对 v1.0.0-alpha.1，alpha.2 变更持久化状态格式（读取 schema 1.22、写入 schema 1.24），导致 alpha.1 无法读取新快照。新增 ResumableSession 跨 worker 恢复对话与待处理审批、原生 Codex exec\_command/apply\_patch 审批恢复、prepare\_tool\_input/output 与 prepare\_tool\_declaration 钩子、RunConfig.redact\_text 文本脱敏，以及 operation\_detail 和 trace\_include\_sensitive\_data 追踪控制。

**标签**: `#runtime`, `#tools`, `#memory`, `#permissions`

---

<a id="item-harness-arch-3"></a>
### [Graphiti v0.32.0 发布](https://github.com/getzep/graphiti/releases/tag/v0.32.0) ⭐️ 7.8/10

Graphiti v0.32.0 发布。该版本移除 Kuzu driver，新增嵌入式 Relate graph driver；强制 group-based UUID 验证，覆盖 episodes、facts（EntityEdge.get\_by\_uuid/get\_by\_uuids）、sagas（summarize\_saga）及 add\_triplet；独立 MCP 服务器升级至 1.1.3 并移除 neo4j extra；修复 LLM 客户端 Anthropic 默认模型、Gemini schema 重复及 temperature 发送问题。跨 group UUID 访问现触发 NodeNotFoundError 或 EdgeNotFoundError，add\_episode\(uuid=...\) 不传 group\_id 时仅检索 default group，未知 predecessor episode UUID 同样报错而非跳过。

github · mehulp93 · 11月23日 21:16

**「设计要点」** 存储层替换 Kuzu driver 为嵌入式 Relate graph driver。权限模型引入 group-scoped UUID 校验，阻断跨组数据访问。MCP 工具层独立镜像升级至 server 1.1.3 并剥离 neo4j 依赖。LLM 客户端层修正 Anthropic 与 Gemini 配置，将 httpx 声明为直接依赖并移除 langchain-anthropic。

**「改了什么」** 移除 Kuzu driver，新增嵌入式 Relate graph driver。强制 group-based UUID 验证，修复 episode UUID 跨组访问漏洞，未知 predecessor UUID 现报错。独立 MCP 镜像升级至 1.1.3 并移除 neo4j extra。LLM 客户端修复 Anthropic 默认模型、停止发送 temperature、移除重复 Gemini schema 文本、声明 httpx 直接依赖。新增单图并发摄取，修复身份属性节点合并。

**标签**: `#runtime`, `#permissions`, `#mcp`, `#memory`

---

<a id="item-harness-arch-4"></a>
### [SWE-agent mini-swe-agent](https://github.com/SWE-agent/mini-swe-agent) ⭐️ 5.0/10

mini-swe-agent 是一个 100 行代码的极简 AI 软件工程 agent，由 SWE-agent 组织开发。该项目登顶 GitHub Trending，声称在 SWE-bench verified 上得分超过 74%，并在 DeepSWE 基准上击败 Claude Code 与 Codex。它支持 Ramp SWE-Bench 与新的 ProgramBench 基准测试，同时提供构建极简 AI agent 的教程。项目未公开具体技术实现细节与完整版本号。

rss · GitHub Trending Daily · 11月23日 23:00

**标签**: `#eval`, `#runtime`

---

## Agent 工程师日报
{: #sec-agent-engineer .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-agent-engineer" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-agent-engineer-1"></a>
### [NariQ 发布 Qwen3.8-27B 低比特量化](https://huggingface.co/nari-labs/Qwen3.8-27B-NariQ-GGUF) ⭐️ 8.0/10

NariQ 发布 Qwen3.8-27B 的 3 比特及更低量化版本，文件大小约 10GB，需配合其自定义 llama.cpp  fork 运行。公开的 agentic 任务、数学推理等多维度基准测试显示，3 比特版本性能接近 BF16 精度，2.5 比特版本性能小幅回落，2 比特版本性能下降明显。该方案面向本地部署大模型的工程师与研究者，目前仅支持定制版推理框架。

hackernews · toebee · 11月23日 13:42 · [社区讨论](https://news.ycombinator.com/item?id=50611402)

**「为什么重要」** 这是首个公开声称在长程 agentic 任务上保留 BF16 级性能的 3 比特及更低量化方案，10GB 的文件大小降低了本地部署 27B 参数模型的硬件门槛。不过实际性能在非 benchmark 场景的落地效果尚未有大规模验证。

**「可关注」** 可关注：该量化方案需绑定自定义 llama.cpp  fork，2 比特版本性能较 3 比特版本出现明显回落，且社区已有对其 benchmark 与实际场景性能匹配度的质疑。

**「评论」** 社区认可该量化方案覆盖了长程 agentic 任务等多维度测试，而非仅优化 benchmark 分数；同时存在对低比特量化信息丢失程度、与其他量化方法对比、非 benchmark 场景实际性能的讨论，也有用户关注其在 Apple M 系列芯片上的部署体验。

**标签**: `#coding-agent`, `#eval`, `#harness`

---

<a id="item-agent-engineer-2"></a>
### [Clover-35B-A3B-Preview 技术报告发布](https://huggingface.co/papers/2611.24636) ⭐️ 8.0/10

2026 年 11 月 23 日 Hugging Face Daily Papers 发布 Clover-35B-A3B-Preview 技术报告，该成果为首个公开的 agent 导向混合专家（MoE）扩散语言模型 arXiv 论文公告。该模型总参数 35B、激活参数 3B，支持思维链生成，采用将 Gated Delta Networks 适配到块扩散的架构，结合历史上下文循环记忆与当前块双向 softmax 注意力，配套可学习块大小校准、零初始化右上下文卷积分支。其在 7 项 agent 基准测试中成绩领先，SWE-bench Verified 得分 73.6，Terminal-Bench 2.1 得分 51.7，报告的单张 NVIDIA GB300 显卡 BF16 精度下内部 agent 工作负载生成速度达 680 tokens/s。该成果面向 coding agent 研发、模型架构设计、agent 效果评估的工程师群体。

rss · Hugging Face Daily Papers · 11月23日 00:00

**「为什么重要」** 该模型是首个公开披露具体架构细节与多项主流 agent 基准领先成绩的 agent 导向 MoE 扩散模型，为相关领域的模型选型、架构设计提供了新的可参考基准。

**「可关注」** 可关注：Clover 采用的 Gated Delta Networks 块扩散架构、循环记忆机制与可学习块大小校准设计，为低激活参数 MoE 模型提升 agent 任务性能提供了可参考的架构路径。

**标签**: `#coding-agent`, `#eval`, `#memory`, `#model-architecture`

---

<a id="item-agent-engineer-3"></a>
### [Hugging Face 发布 Agentic Eval 构建指南](https://huggingface.co/blog/agentic-evals) ⭐️ 7.8/10

Hugging Face 2026 年 11 月 23 日发布构建与维护智能体评估的实操指南，梳理了评估从问答、智能体到多智能体团队的三个演进阶段，拆解了智能体评估 8 步构建流程，并给出组件级开源策略参考。指南披露其 Hub 当前托管约 3500 个评估排行榜、17000 个评估数据集，过去一年数据集规模增长约 16 倍，同时新增 Traces、Benchmarks、Environments 三类智能体评估相关抽象支持。指南指出当评测的方法、代码、数据保持私有时，其他人难以审查或复用，开源可解决该问题；多智能体团队评测因 agent 间交互引入额外复杂度，暂不纳入本次指南范围。材料提及固定模型在不同 agent harness 下跑同一任务，准确率差异最高达 29.9 个百分点，当前 98.2%的模型-基准分数仅由单方报告，指南附带完整实操附录与术语表解决社区术语不一致问题，面向构建 coding agent 评测系统、模型评估体系的工程师。

rss · Hugging Face Blog · 11月23日 00:00

**「为什么重要」** 当前智能体评测领域存在结果可复现性差、单方报告占比高、术语不统一等普遍痛点，该指南作为官方发布的实操参考，直接覆盖 agent harness 与评测系统的构建、维护全流程，对相关工程师有直接参考价值。

**「可关注」** 可关注：同一固定模型在不同 agent harness 下跑同一任务，准确率差异最高达 29.9 个百分点，评测结果受 harness 实现影响显著。

**标签**: `#eval`, `#harness`

---

<a id="item-agent-engineer-4"></a>
### [AgentRoboCritic 动作级评估框架提出](https://huggingface.co/papers/2611.26613) ⭐️ 7.0/10

2026-11-23，Hugging Face Daily Papers 介绍 AgentRoboCritic，一个动作级意图导向批评框架。该框架针对 GPT-6 Astra 等前沿多模态智能体在直接机器人控制任务上的表现，在 12 个操作基准上开展系统评估。策略智能体在每个动作旁声明局部意图，批评者据此评估动作结果与失败模式，克服现有基准仅报告回合级成功率的局限。论文摘要被截断，完整实验结果未完全披露。

rss · Hugging Face Daily Papers · 11月23日 00:00

**「为什么重要」** 现有机器人控制基准仅提供回合级成功率，无法定位智能体失败的具体环节。AgentRoboCritic 的动作级细粒度分析为构建 agent 评估系统的工程师提供了失败模式分类与批评机制的设计参考。

**「可关注」** 可关注：将局部意图声明嵌入策略输出，并让批评者基于该意图做动作级结果评估，可作为设计细粒度 agent 评估系统的技术参考。

**标签**: `#eval`

---

<a id="item-agent-engineer-5"></a>
### [HF Intent Contracts 授权](https://huggingface.co/papers/2611.24025) ⭐️ 7.0/10

2026 年 11 月 23 日 Hugging Face 每日论文收录代理授权方向研究，提出面向工具调用型 LLM Agent 的 Intent Contracts 授权接口。该方案将规划模型与工具访问完全隔离，规划模型每步仅提交包含目标、用户原话、范围字段的日志化契约；在代码校验与分发逻辑正确的前提下，所有执行的工具调用均由小型可信模型检查用户原话后直接写入，规划模型对调用的影响仅限提交前的日志化契约，可信侧决定请求的执行范围。论文将 Intent Contracts 与两种仅查看用户原话和命令的审查方案对比，其中一种对应推理盲权限分类器的信息边界，另一种对比细节因论文内容截断未公开。该研究直接面向 Agent 权限设计、harness 开发群体。

rss · Hugging Face Daily Papers · 11月23日 00:00

**「为什么重要」** 当前多数工具调用型 Agent 仍由规划模型直接生成工具调用，Intent Contracts 提出的“规划-执行解耦”模式为降低规划阶段越权风险提供了可参考的设计路径，但实际安全收益与性能开销还需完整评估结果验证。

**「可关注」** 可关注：工具调用型 Agent 可将规划模型与工具访问权限隔离，通过日志化契约约束规划模型的输出范围，由可信侧完成最终工具调用写入，降低规划阶段越权风险。

**标签**: `#permissions`, `#harness`, `#coding-agent`, `#eval`

---

<a id="item-agent-engineer-6"></a>
### [HF 每日论文：MemOnce 可扩展 LLM 记忆架构](https://huggingface.co/papers/2611.27973) ⭐️ 6.0/10

2026 年 11 月 23 日 Hugging Face Daily Papers 推送论文《MemOnce: A Scalable Memory Architecture for Large Language Models》，提出面向大语言模型的可扩展记忆架构 MemOnce。该架构针对标准 Transformer 逐层逐 token KV 缓存导致的线性 GPU 内存增长、上下文扩展时的二次计算开销，以及现有线性时间架构的细粒度细节丢失问题，采用记忆编码器-解码器设计，仅缓存少量最终层隐藏状态作为紧凑记忆表示，动态解码回 KV 缓存供推理使用。当前仅能获取该论文的摘要片段，无性能基准、实现细节、可复现评估结果，无法完成完整技术评估，主要面向长时程智能体系统的记忆与上下文管理场景。

rss · Hugging Face Daily Papers · 11月23日 00:00

**「为什么重要」** 该研究直接针对长时程智能体系统记忆与上下文管理的核心痛点，提出了区别于现有方案的新技术思路；目前仅公开摘要片段，实际性能收益、实现成本、框架兼容性等影响尚未得到验证。

**「可关注」** 可关注：MemOnce 通过缓存紧凑隐藏状态、动态解码回 KV 缓存的思路，为长上下文场景下的 KV 缓存扩展问题提供了新的技术方向，但当前无公开实现与性能基准，暂无法评估落地可行性。

**标签**: `#memory`

---

<a id="item-agent-engineer-7"></a>
### [RoboTrack 开源 点跟踪模型与基准发布](https://huggingface.co/blog/allenai/robotrack) ⭐️ 5.8/10

2026 年 11 月 23 日，Hugging Face 博客发布开源机器人点跟踪项目 RoboTrack，包含基准、训练数据、两个新模型及技术报告。RoboTrack-Bench 收录 307 个人工标注、二次校验的真实机器人操作视频，共 2522 条点轨迹，覆盖 DROID、Ego-Exo4D、MolmoAct 2、EgoVerse 数据集，包含杂乱场景、第一/第三人称视角、机器人/人手操作及遮挡场景，其中 33 对为同步双视角视频。配套的 RoboTrack-15M 是基于 MolmoSpaces 生成的 1500 万条机器人操作合成点轨迹训练集。同时发布的 RoboTracker（微调 AllTracker）和 RoboTracker-Warp（基于 CoWTracker 训练）均优于对应基线，其中 RoboTracker-Warp 在 5 个评估基准中的 4 个达到 SOTA。评估显示主流跟踪器在 RoboTrack-Bench 上的平均 Jaccard（AJ）得分比现有机器人基准低 3.0 至 6.6，例如 CoWTracker 从 RoboTAP 的 70.5 AJ 降至 RoboTrack-Bench 的 63.9 AJ。

rss · Hugging Face Blog · 11月23日 17:20

**「为什么重要」** 该发布填补了真实机器人操作场景点跟踪评估的空白，已证实现有通用跟踪基准无法反映模型在杂乱、遮挡、多视角操作场景的实际表现，同时验证了面向机器人操作的合成训练数据可有效提升真实场景跟踪效果。目前尚未有证据表明这些改进可直接迁移到通用 AI Agent 系统、非机器人领域的评估框架或工具链中，其价值目前明确限定在机器人操作感知领域。

**「可关注」** 可关注：若项目涉及机器人操作感知模块，现有通用点跟踪基准的评分无法直接对应真实场景表现，建议优先用 RoboTrack-Bench 做针对性评估，而非仅依赖通用跟踪测试集。

**标签**: `#eval`

---

## AI 日报
{: #sec-ai-daily .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-daily" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-daily-1"></a>
### [OpenAI 与 Cisco 联合推出开源运行时 Shirudo](https://openai.com/index/introducing-shirudo) ⭐️ 7.8/10

OpenAI 与 Cisco 联合发布开源 Linux 运行时 Shirudo。该工具用于帮助团队在滚动部署补丁时保护运行中的系统。

rss · OpenAI Blog · 11月23日 21:20

**「可关注」** 可关注：Shirudo 是面向 Linux 的开源运行时，可应用于补丁滚动部署场景下的运行系统保护。

**标签**: `#open-source`, `#product`, `#lab`, `#industry`

---

<a id="item-ai-daily-2"></a>
### [Anthropic EFS 公测 支持零数据留存](https://claude.com/resources/articles/zero-data-retention-with-enterprise-frontier-safeguards) ⭐️ 7.8/10

Anthropic 发布 Enterprise Frontier Safeguards（EFS）公开测试版，面向企业客户提供零数据留存（ZDR）兼容的前沿模型滥用检测能力，Anthropic 及云服务商均不保留企业数据。该功能已与超 100 家企业客户联合开发，覆盖四分之一财富 100 强及医疗、金融服务、法律等强监管行业。EFS 通过客户自有的云存储运行自动化安全监控，可识别跨多请求的复杂滥用模式，仅分析客户控制基础设施中的数据，不存储、不使用客户数据训练模型，且无人工审核环节。

rss · Claude Blog · 11月23日 00:00

**「为什么重要」** 该方案平衡了企业数据主权与前沿模型安全防护需求，解决了强监管行业使用高级 AI 的数据合规顾虑，可推动安全敏感组织更放心地落地前沿 AI 应用。

**「可关注」** 可关注：EFS 已支持 Claude Platform、Claude Platform on AWS、Amazon Bedrock、Claude on Google Cloud，微软 Foundry 支持即将上线，生成的安全事件（Safety Case）可通过 API 读取并集成 SIEM 系统，且不包含输入输出内容。

**标签**: `#lab`, `#policy`, `#product`, `#industry`

---

<a id="item-ai-daily-3"></a>
### [Claude Ship beta 发布](https://claude.com/resources/articles/introducing-claude-ship) ⭐️ 7.8/10

Anthropic 发布 Claude Ship beta，支持 Claude 按团队预设策略自主完成 PR 审查、修复与合并批准，产品由已 GA 的 Code Review 及两个新 beta 代理 PR Steward、Claude Approvals 构成。 eligible 的 Claude Enterprise 组织可领取至少 10000 美元的 Claude Ship credits，需在领取后 30 天内使用，领取截止日期为 2027 年 1 月 15 日。该功能目前仅支持 GitHub 仓库，不面向启用零数据保留、HIPAA 配置或客户管理加密密钥的组织开放，使用按 token 计费，管理员可分别为 Code Review 和 PR Steward 设置消费上限。

rss · Claude Blog · 11月23日 00:00

**「为什么重要」** Claude Ship 将 PR 全流程自动化能力整合为开箱即用的产品，Claude Code 团队内部试用期间，合并 PR 数量较 6 月至 9 月翻倍，回滚率下降超 40%，可减少团队在 PR 流转环节的人工耗时。

**「可关注」** 可关注：团队可先以观察模式运行审批策略，积累信任后再开启分支保护强制要求 Claude Approvals 通过。

**标签**: `#product`, `#industry`, `#agent`

---

<a id="item-ai-daily-4"></a>
### [Anthropic 发布 Claude Code 企业安全指南](https://claude.com/resources/articles/enterprise-guide-to-securing-coding-agents) ⭐️ 7.8/10

Anthropic 官方发布面向企业的编码代理安全指南，介绍如何通过权限检查、隔离环境等分层控制保障 Claude Code 等编码代理的安全，并提及 Salesforce 的采用情况。Salesforce 标准化采用 Claude Code 后披露了 79% 与 5% 两项采用数据。该指南面向 Claude Team 和 Enterprise 计划用户，通过 AWS、谷歌云、微软 Azure 等云服务商使用 Claude 的用户也可适用相同安全原则。

rss · Claude Blog · 11月23日 00:00

**「为什么重要」** 这是 Anthropic 首份面向企业的编码代理安全框架，给出了可落地的分层控制方案与评估标准，能降低企业规模化部署编码代理的安全顾虑。

**「可关注」** 可关注：企业部署编码代理时可优先落地权限最小化、会话级隔离、集中策略管控的分层控制，同时配套会话遥测导出与审计能力满足合规要求。

**标签**: `#product`, `#industry`, `#lab`

---

<a id="item-ai-daily-5"></a>
### [Google 语义治理策略防御代理劫持](https://developers.googleblog.com/did-the-user-ask-for-this-securing-ai-agents-against-intent-hijacking-with-semantic-governance-policies/) ⭐️ 7.8/10

Google 研究人员披露 AI 代理面临的间接提示注入意图劫持风险：攻击者可隐藏在工具返回的非信任内容中，诱导代理执行攻击者意图而非用户指令。研究团队以 ETH Zurich 与 Invariant Labs 开发、已被 NIST 代理创新中心纳入劫持评估的开源基准 AgentDojo v1.2.2（含 97 个用户任务、949 次攻击运行，采用 important\_instructions 攻击向量）测试验证，提出语义治理策略作为缓解方案，测试基于 gemini-2.5-flash 代理，全基准跑 6 次取平均值。关键数据：默认仅开启用户意图匹配功能时，工具调用类攻击成功率从 48.7%降至 0.9%，六次运行中稳定在 0.84%-0.95%区间，正常任务效用仅下降 2.6 个百分点；无策略时 Slack 场景超 90%攻击可成功，开启策略后银行、Slack、工作空间场景攻击成功率降至 0；但不涉及工具调用的纯文本响应操纵类攻击无法被该策略防御。

rss · Google Developers AI · 11月23日 00:00

**「为什么重要」** 间接提示注入是 AI 代理落地部署的核心安全风险，该策略可在几乎不影响正常任务效用的前提下，将工具调用类意图劫持攻击的成功率压至 1%以下，相关基准已被 NIST 纳入官方评估，对代理安全架构设计有直接参考价值。

**「可关注」** 可关注：语义治理策略默认开启的用户意图匹配功能无需额外配置，即可将工具调用类意图劫持攻击成功率从 48.7%降至 0.9%，但纯文本响应操纵类攻击需配合响应过滤等其他控制措施防御。

**标签**: `#lab`, `#industry`, `#eval`, `#policy`, `#open-source`

---

<a id="item-ai-daily-6"></a>
### [KPMG 谈客户敏感数据场景的 AI 应用](https://claude.com/resources/articles/kpmg-todd-lohr-on-ai-when-your-data-is-also-your-clients-data) ⭐️ 5.8/10

Claude Blog 发布 KPMG 美国副董事长、客户技术与创新负责人 Todd Lohr 的截断访谈预览，讨论专业服务机构在处理客户敏感数据、强监管行业场景下落地前沿 AI 的平衡思路。KPMG 是全球性专业服务机构，拥有超 27.6 万名员工，业务覆盖 138 个国家和地区，目前已将 Claude 集成至税务数字平台 Digital Gateway，推出对应版本，同时推进自有 Trusted AI 框架，并测试 Anthropic 的 Enterprise Frontier Safeguards 以满足数据管控要求，KPMG 方表示该方案可让其更有信心地加速强监管客户项目中的 AI 部署。

rss · Claude Blog · 11月23日 00:00

**「为什么重要」** KPMG 业务涉及大量受监管行业的客户敏感数据，其平衡前沿 AI 能力与数据安全、合规要求的实践，对同类型专业服务机构及强监管行业的企业 AI 落地有直接参考价值。

**「可关注」** 可关注：KPMG 正在测试 Anthropic 的 Enterprise Frontier Safeguards，该方案支持在机构自有控制的云基础设施中留存数据的同时调用前沿模型，可匹配强监管场景的数据管控要求。

**标签**: `#industry`, `#policy`, `#enterprise`

---

## AI 羊毛
{: #sec-ai-deals .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-deals" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-deals-1"></a>
### [Google Gemini 黑五五折 AI Pro/Plus 年费](https://www.appinn.com/google-ai-pro-black-friday-2026/) ⭐️ 8.0/10

你看到的内容可能由第三方 AI 基于小众软件文章提炼总结而成，可能与原文真实意图存在偏差。不代表小众软件观点和立场。请&lt;a href=&quot;https://www.appinn.com/google-ai-pro-black-friday-2026/&quot; target=&quot;\_blank&quot;&gt;点击链接阅读原文&lt;/a&gt;细致比对和校验。&lt;br /&gt;&lt;br /&gt;Google 推出 AI Pro/Plus 黑五五折优惠，Plus 年费 24.99 美元（原价 49.99 美元），Pro 年费 99.99 美元（原价 199.99 美元），优惠仅限首年，次年续费恢复原价，不同账户显示的折扣可能不同，最终以 Google 结算页面为准。领取分两批次：11 月 20～26 日现有 Google One、Google AI 订阅用户可提前参与，11 月 27 日起向符合条件的新用户开放，目前主要面向美区账户。Plus 无 Antigravity 权限与 YouTube Premium Lite，400G 存储可共享 5 位家庭成员，提供 50 计算单元/月的 Colab 额度；Pro 提供 5TB 存储、200 计算单元/月的 Colab 额度及更多高级功能权限。

rss · 小众软件 · 11月23日 05:53

**「为什么重要」** 本次优惠向已有 Google One/Google AI 订阅的老用户开放，11 月 20 日即可参与无需等待；Plus 24.99 美元/年的首年价格对轻度用户性价比突出，Pro 则覆盖 5TB 存储、高级模型权限及 Colab 等开发者工具额度，适合对应需求的用户。

**「可关注」** 已有 Google One 年费订阅的用户可直接升级至 AI Pro 年付方案，按比例抵扣旧套餐剩余费用，无需先取消原订阅；Plus 无 Antigravity 权限、无 YouTube Premium Lite，需按需选择。

**标签**: `#promo`, `#limited-free`, `#coupon`

---

<a id="item-ai-deals-2"></a>
### [DevSwarm 创业团队 1 年 10 席免费](https://devswarm.ai/startups/) ⭐️ 6.0/10

DevSwarm 官方推出创业团队专属优惠，最多可领取 10 个席位免费使用 1 年，领取无需提供投资方证明。当前公开内容仅披露基础优惠信息，完整 eligibility 条件、具体领取流程、活动截止时间均未明确，实际可领取性待确认。

rss · HN Free API / Credits · 11月23日 20:21

**标签**: `#promo`, `#limited-free`

---

<a id="item-ai-deals-3"></a>
### [Fly.io 免费计划上线](https://fly.io/changelog/introducing-the-free-plan/) ⭐️ 6.0/10

Fly.io 于 2026 年 11 月 23 日在官方更新日志中宣布推出免费计划，当前公开的 RSS 内容未披露该计划的具体资源额度、有效期、区域限制、领取条件及截止时间等细节。

rss · HN Free API / Credits · 11月23日 17:02

**「为什么重要」** 该计划面向开发者群体，但具体可用性依赖后续官方披露的规则，目前仅能确认其已正式官宣。

**「可关注」** 可关注：后续 Fly.io 官方公开免费计划的具体限制规则后，再评估其是否适配个人开发测试场景。

**标签**: `#free-tier`, `#promo`, `#api`

---