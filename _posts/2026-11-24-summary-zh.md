---
layout: default
title: "Horizon Summary: 2026-11-24 (ZH)"
date: 2026-11-24
lang: zh
---

> 从 205 条内容中筛选出 14 条重要资讯。

<nav id="ah-toc" class="ah-toc" aria-label="目录"><span class="ah-toc-title">目录</span><ul><li><a href="#sec-harness-arch"><span class="ah-toc-name">Harness 架构</span><span class="ah-toc-count">3条</span></a></li><li><a href="#sec-agent-engineer"><span class="ah-toc-name">Agent 工程师日报</span><span class="ah-toc-count">7条</span></a></li><li><a href="#sec-ai-daily"><span class="ah-toc-name">AI 日报</span><span class="ah-toc-count">2条</span></a></li><li><a href="#sec-ai-deals"><span class="ah-toc-name">AI 羊毛</span><span class="ah-toc-count">2条</span></a></li></ul></nav>

---

**[Harness 架构](#sec-harness-arch)**
1. [Codex rust-v0.172.0 发布](#item-harness-arch-1) ⭐️ 7.8/10
2. [pydantic-ai v2.73.0 发布](#item-harness-arch-2) ⭐️ 7.8/10
3. [Agents SDK v1.0.0a2 发布](#item-harness-arch-3) ⭐️ 7.8/10

**[Agent 工程师日报](#sec-agent-engineer)**
1. [NariQ 发布 Qwen3.8-27B 3-bit 量化](#item-agent-engineer-1) ⭐️ 8.0/10
2. [AutoPILOT 实时游戏 Agent harness 提出](#item-agent-engineer-2) ⭐️ 7.0/10
3. [Self-WSP 语言模型自改权重](#item-agent-engineer-3) ⭐️ 7.0/10
4. [HF 每日论文：GameAnything 发布](#item-agent-engineer-4) ⭐️ 7.0/10
5. [GameDojo 实时交互智能体基准发布](#item-agent-engineer-5) ⭐️ 7.0/10
6. [datasette-charts 0.2a0 发布](#item-agent-engineer-6) ⭐️ 6.8/10
7. [RoboTrack 机器人操控点追踪基准发布](#item-agent-engineer-7) ⭐️ 6.3/10

**[AI 日报](#sec-ai-daily)**
1. [OpenAI 与 Cisco 联合发布 Shirudo](#item-ai-daily-1) ⭐️ 7.8/10
2. [OpenAI 博客探讨内部法务 AI 用例](#item-ai-daily-2) ⭐️ 5.8/10

**[AI 羊毛](#sec-ai-deals)**
1. [Koofr 1TB 终身 129.9 美元](#item-ai-deals-1) ⭐️ 7.0/10
2. [Gemini 土区 Pro/Plus 年付半价](#item-ai-deals-2) ⭐️ 7.0/10

---

## Harness 架构
{: #sec-harness-arch .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-harness-arch" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-harness-arch-1"></a>
### [Codex rust-v0.172.0 发布](https://github.com/openai/codex/releases/tag/rust-v0.172.0) ⭐️ 7.8/10

OpenAI Codex CLI 发布 rust-v0.172.0。本次更新引入 MCP stdio 服务器延迟启动、per-app tool approval 配置、终端内嵌套 agent 导航，以及跨操作系统远程会话工作区一致性修复。Code Mode 全面切换至 gRPC 主机连接，\`code\_mode\_host\_grpc\` 设置已弃用。

github · github-actions\[bot\] · 11月24日 00:03

**「设计要点」** MCP 运行时采用延迟启动策略，带缓存工具列表的 stdio 服务器推迟到首次工具调用时启动。沙盒权限和工作区根目录在 \`codex exec resume\` 及跨平台远程会话中持久化，依赖平台后端统一管理。

**「改了什么」** 新增终端内线程链接跳转、斜杠命令 Tab 补全、任务组 Shift 键导航，支持为单个 app 工具配置审批审查员及 Bedrock Runtime 选择。修复 \`codex exec resume\` 丢失沙盒权限、远程跨 OS 会话工作区路径不一致等问题。

**标签**: `#runtime`, `#mcp`, `#sandbox`, `#tools`, `#permissions`

---

<a id="item-harness-arch-2"></a>
### [pydantic-ai v2.73.0 发布](https://github.com/pydantic/pydantic-ai/releases/tag/v2.73.0) ⭐️ 7.8/10

pydantic-ai v2.73.0 正式发布。本次更新向 Agent.override 加入 capabilities 参数，导出 AgentInstructions 与 SourcedInstruction，并为 GPT-Live 语音模型新增 RealtimeSession.append\_voice\_instructions。OpenAI Responses 的 input\_transformations 现在可见于 provider\_details 与模型请求 span，SubAgents 支持将延迟工具调用传递给调用者并在回答后恢复；私有上下文变量 Agent.\_override\_root\_capability 的结构改为 \(capability, injected\) 元组，直接读取该变量的代码需更新。此外，Coder 读取的图像缩小至最长边 1024 像素，Dataset 序列化排除 init=False 字段，boxd extra 升级至 0.3。

github · dsfaccini · 11月24日 03:53

**「改了什么」** Agent.override 新增 capabilities 字段，RealtimeSession 新增 append\_voice\_instructions 方法，SubAgents 可传递并恢复延迟工具调用；OpenAI input\_transformations 缓存信息现在暴露在 provider\_details 与模型请求 span 中，Agent.\_override\_root\_capability 上下文变量改为存储 \(capability, injected\) 元组。Coder 图像读取上限降至 1024 像素，Dataset 排除 init=False 字段，boxd 依赖升至 0.3.3，安装 openai 的 extra 最低要求从 3.31.0 升至 3.50.0。

**标签**: `#runtime`, `#prefix-cache`, `#compatibility`

---

<a id="item-harness-arch-3"></a>
### [Agents SDK v1.0.0a2 发布](https://github.com/openai/openai-agents-python/releases/tag/v1.0.0-alpha.2) ⭐️ 7.8/10

Agents SDK v1.0.0a2 发布。该预览版新增跨 worker 对话与待处理 approval 恢复、Codex 原生命令/编辑 approval 恢复、工具执行 hooks 与声明过滤、Runner 文本脱敏及操作追踪。持久化状态格式升级，RunState schema 升至 1.24，ResumableSession checkpoint 升至 version 2，要求先升级 reader 再升级 writer。支持 CPython 3.10–3.14，提供四平台预编译 wheel 并带 SHA-256 哈希校验。

github · markstuart-oai · 11月23日 20:11

**「设计要点」** 运行时嵌入 Codex Core rust-v0.166.0，同步 PreToolUse 处理失败或超时即阻断原生 dispatch。会话层采用 ResumableSession 配合原子条件写入的 ResumableSessionStore 或 RedisSessionStore 实现跨 worker 恢复；工具层提供 prepare\_tool\_input/output 及 prepare\_tool\_declaration 回调，支持执行前后修改参数、结果或过滤声明，sdk\_only\_tool\_hooks=True 可禁用原生 Codex 工作区工具。

**「改了什么」** 相对 v1.0.0-alpha.1，新增 ResumableSession 跨 worker 恢复对话与 pending approvals、Codex 原生 exec\_command/apply\_patch approval 恢复、ToolExecutionConfig 输入输出钩子与声明过滤，以及 RunConfig.redact\_text 文本脱敏与 operation\_detail 追踪配置。持久化状态格式不兼容变更，RunState schema 从 1.22 升至 1.24，ResumableSession checkpoint 升至 version 2，alpha.1 无法读取新快照。

**标签**: `#runtime`, `#tools`, `#memory`, `#permissions`, `#sandbox`

---

## Agent 工程师日报
{: #sec-agent-engineer .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-agent-engineer" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-agent-engineer-1"></a>
### [NariQ 发布 Qwen3.8-27B 3-bit 量化](https://huggingface.co/nari-labs/Qwen3.8-27B-NariQ-GGUF) ⭐️ 8.0/10

NariQ 发布 Qwen3.8-27B 的 3-bit 及更低比特 GGUF 量化文件，文件大小约 10 GB。官方声称 DeepSWE 39.8→41.0、Terminal-Bench 2.1 62.6→63.8（3-bit），在 agentic 任务上保持接近 BF16 性能。运行当前需配合 nari-labs/nari-llama.cpp fork；在 RTX PRO 6000 上解码速度与其他量化相当，M3 Pro 上 3.0bpw 约 3.8 tok/s。社区对 benchmark 收益是否来自模型本身或 harness 差异存在分歧，且该量化尚未在通用 llama.cpp 主支验证。

hackernews · toebee · 11月23日 13:42 · [社区讨论](https://news.ycombinator.com/item?id=50611402)

**「为什么重要」** 这是首个声称在长程 agentic 任务上保持 BF16 级别性能的 3-bit 及更低量化，若复现可显著降低 coding-agent 部署显存门槛。但社区已指出 benchmark 可能受 harness 差异影响，且需专用 fork，实际 workload 表现仍需独立验证。

**「可关注」** 可关注：NariQ 当前绑定 nari-labs/nari-llama.cpp fork，通用 llama.cpp 主支尚不支持，部署时需评估运行时维护成本。

**「评论」** 社区分歧集中在 benchmark 可信度：WithinReason 认为收益主要来自 harness 差异；rao-v 虽认可其测试了多类长程任务，但仍担心 QAT 量化过拟合 benchmark。实际体验方面，jedbrooke 报告 M3 Pro 上 3.0bpw 解码约 3.8 tok/s，显著慢于 CUDA 路径。

**标签**: `#eval`, `#coding-agent`, `#harness`, `#toolchain`

---

<a id="item-agent-engineer-2"></a>
### [AutoPILOT 实时游戏 Agent harness 提出](https://huggingface.co/papers/2611.28202) ⭐️ 7.0/10

2026 年 11 月 24 日 Hugging Face 每日论文收录 AutoPILOT 相关研究，该研究提出面向实时游戏场景的视觉 Agent harness，解决现有 VISTA 等 harness 每次模型调用最多生成 1 个动作、无法匹配不等待模型输出的游戏节奏的核心问题。AutoPILOT 支持单次模型调用输出原始动作、启动开环宏或写入可自主执行的闭环控制器，无需额外模型调用即可持续运行直到交还控制权。研究同时发布 AFK-Bench 基准，包含 120 个多类别浏览器游戏，用于评估实时交互 Agent。

rss · Hugging Face Daily Papers · 11月24日 00:00

**「为什么重要」** 当前多数 Agent harness 未针对实时非等待式交互场景优化动作输出粒度，AutoPILOT 的控制器级输出机制与配套基准，为 AI Agent 工程师的 harness 设计、实时 Agent 评估提供了新的可验证参考路径。

**「可关注」** 可关注：实时交互场景下，Agent harness 可将单次模型调用的输出从单动作扩展为可自主执行的控制器/宏，可能改变现有 Agent 的推理调度与延迟适配逻辑。

**标签**: `#harness`, `#eval`, `#orchestration`

---

<a id="item-agent-engineer-3"></a>
### [Self-WSP 语言模型自改权重](https://huggingface.co/papers/2611.28833) ⭐️ 7.0/10

Hugging Face Daily Papers 2026-11-24 介绍 Self-WSP 论文。该技术让 Qwen3.5-0.8B 通过 Weight-Space Programming 读取并编辑自身权重，同时担任解题者与编辑者。GSM8K 准确率从 11.8% 升至 62.2%，MATH500 从 7.0% 升至 32.2%，有时仅修改 16 个参数，重复自编辑可继续提升性能。但编辑过程缺乏可解释性，模型对自身修改内容理解有限。

rss · Hugging Face Daily Papers · 11月24日 00:00

**「为什么重要」** 该研究验证了语言模型通过极少量权重修改实现自我改进的可行性，为 LLM 自进化提供新思路。但编辑不可解释，当前无法用于生产部署，对模型可观测性提出挑战。

**「可关注」** 可关注：Self-WSP 以最少 16 个参数修改实现数学基准大幅提升，但编辑黑箱特性与模型可解释性要求存在张力，需评估对 eval 和 harness 设计的影响。

**标签**: `#eval`, `#observability`, `#harness`

---

<a id="item-agent-engineer-4"></a>
### [HF 每日论文：GameAnything 发布](https://huggingface.co/papers/2611.29238) ⭐️ 7.0/10

2026 年 11 月 24 日 Hugging Face 每日论文收录 GameAnything 相关研究，该研究提出开源智能体平台，可将多模态灵感转化为现有游戏的可玩扩展，支持迭代开发。平台核心集成编码智能体、独立试玩评判器、持久开发状态与可复用经验记忆，同时配套跨多模态参考、多种创作目标与游戏环境的 GameAnything-Bench 评估基准。目前公开内容仅包含摘要，无详细性能数据与实现细节，主要面向 coding agent 研发、游戏自动化开发、智能体评估方向的工程师。

rss · Hugging Face Daily Papers · 11月24日 00:00

**「为什么重要」** 该研究首次提出面向多模态灵感到可玩游戏转化的开源智能体平台框架与专用基准，为 coding agent 的游戏场景落地、迭代开发状态管理与评估设计提供了可参考的落地方向；但具体性能表现与实现细节尚未公开，实际工程价值待验证。

**「可关注」** 可关注：GameAnything 将编码智能体、试玩评判器、持久开发状态与可复用经验记忆耦合的迭代开发框架，对 coding agent 的场景化落地与评估设计有参考价值。

**标签**: `#coding-agent`, `#eval`, `#memory`, `#harness`

---

<a id="item-agent-engineer-5"></a>
### [GameDojo 实时交互智能体基准发布](https://huggingface.co/papers/2611.30771) ⭐️ 7.0/10

2026 年 11 月 24 日 Hugging Face Daily Papers 推送 arXiv 预印本《GameDojo: Benchmarking Real-Time Interactive Agents in Video Games》，提出覆盖 20 款游戏 120 场 Boss 战的可控交互游戏基准 GameDojo，用于评估实时智能体能力、学习算法与 Agent harness。配套公开 600 小时游戏轨迹数据集 GameDojo-Data，基于该数据集训练的 4B 参数模型 GameDojo-4B 达到前沿实时交互性能；实验同时发现当前前沿模型在实时交互场景存在明显能力短板，联合训练可提升单任务表现。

rss · Hugging Face Daily Papers · 11月24日 00:00

**「为什么重要」** 该基准首次提供标准化的实时交互智能体评估场景与公开轨迹数据集，填补了当前领域缺乏可控实时交互评估工具的空白；预印本结论尚未经同行评审，其实证发现的泛化性仍需后续研究验证。

**「可关注」** 可关注：GameDojo 的公开轨迹数据集、联合训练增益结论，以及编码智能体复现环境生成游戏脚本的产数路径，可复用于实时交互智能体的训练与评估流程。

**标签**: `#eval`, `#harness`, `#coding-agent`, `#interactive-agents`

---

<a id="item-agent-engineer-6"></a>
### [datasette-charts 0.2a0 发布](https://github.com/datasette/datasette-charts/releases/tag/0.2a0) ⭐️ 6.8/10

2026 年 11 月 24 日，simonw 发布 datasette-charts 0.2a0 早期 alpha 版本。该版本新增与 Datasette Agent 的集成：同时安装两个插件时，Agent 可获得对话内绘图工具（链接至面板图表构建器）和图表建议工具（针对表或查询）。此外新增 \`decade\` 时间单位，适配跨世纪列的分桶需求；跳过分桶的折线图（如按年分桶但仅每十年有数据）现在会绘制连线而非孤立点。当前为早期 alpha 版本，功能稳定性未经验证。

github · simonw · 11月24日 04:24

**「为什么重要」** 该版本是 coding agent 与可视化工具集成的可验证参考案例，展示了插件向 Agent 暴露工具的标准模式。目前仍处于早期 alpha 阶段，实际集成效果和稳定性尚未得到大规模验证。

**「可关注」** 可关注：插件可通过预定义工具接口向 coding agent 暴露可视化能力，无需 agent 自行实现图表生成逻辑。

**标签**: `#coding-agent`, `#harness`

---

<a id="item-agent-engineer-7"></a>
### [RoboTrack 机器人操控点追踪基准发布](https://huggingface.co/blog/allenai/robotrack) ⭐️ 6.3/10

2026 年 11 月 23 日，Hugging Face 博客发布 Allen AI 的 RoboTrack 项目，配套开源技术报告、代码、数据集与基准，面向真实世界机器人操控场景的点追踪需求。RoboTrack-Bench 包含 307 段来自 DROID、Ego-Exo4D、MolmoAct 2、EgoVerse 的人工标注真实操控视频，共 2522 条经二次校验的点轨迹，覆盖杂乱场景、遮挡、第一/第三人称视角，包含机器人、人手、被操作物体、静态物体的类别标注，另有 33 对同步多视角视频子集。评估显示 CoTracker3、BootsTAPNext、AllTracker、CoWTracker 四款主流追踪器在 RoboTrack-Bench 上的平均 Jaccard（AJ）得分比现有机器人基准低 3.0 至 6.6，加入 RoboTrack-15M 模拟操控轨迹数据训练可提升模型在真实操控视频上的表现，新发布的 RoboTracker-Warp 在 5 个评估基准中 4 个达到当前最优。该项目主要服务于具身智能、机器人操控方向的感知模块研发与评测工程师。

rss · Hugging Face Blog · 11月23日 17:20

**「为什么重要」** 已发生的变化是：RoboTrack 填补了真实世界机器人操控场景点追踪的专用评测空白，验证了现有通用点追踪基准无法反映模型在杂乱、遮挡、多视角场景下的实际性能，现有 SOTA 模型在该场景下出现明显性能下滑。尚未证实的影响是：该项目的训练数据与模型是否能直接落地到实际机器人操控系统，当前仅对具身智能/机器人操控细分领域工程师有直接参考价值，对通用 Agent 工程参考意义有限。

**「可关注」** 可关注：RoboTrack-15M 的模拟操控轨迹数据可提升点追踪模型在真实机器人操作视频上的表现，RoboTrack-Bench 的多类别、多视角标注也可用于现有追踪器的场景化性能诊断。

**标签**: `#eval`

---

## AI 日报
{: #sec-ai-daily .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-daily" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-daily-1"></a>
### [OpenAI 与 Cisco 联合发布 Shirudo](https://openai.com/index/introducing-shirudo) ⭐️ 7.8/10

OpenAI 与 Cisco 联合发布开源 Linux 运行时 Shirudo。该工具用于在补丁 rollout 过程中保护正在运行的系统。相关发布信息来自 OpenAI 官方博客，发布时间为 2026 年 11 月 23 日。

rss · OpenAI Blog · 11月23日 21:20

**「可关注」** 可关注：开源 Linux 运行时 Shirudo 可用于补丁 rollout 场景下的运行系统保护。

**标签**: `#lab`, `#industry`, `#open-source`, `#product`

---

<a id="item-ai-daily-2"></a>
### [OpenAI 博客探讨内部法务 AI 用例](https://openai.com/business/learn/connected-intelligence-for-in-house-legal) ⭐️ 5.8/10

2026 年 11 月 23 日 OpenAI 发布官方博客，由 Stacey Wang、Craig Bruney 与 LECG 的 Mary O’Carroll、Cooley 的 Richard Segal 展开讨论，梳理 AI 在内部法务团队的三大应用方向：关联业务背景、搭建可复用工作流、优化外部律所使用效率。本次内容未发布新的模型、产品或政策调整。

rss · OpenAI Blog · 11月23日 08:00

**「为什么重要」** 该讨论属于法律垂直行业的 AI 应用探索内容，梳理了内部法务团队的 AI 落地方向。

**「可关注」** 可关注：AI 在内部法务场景的落地重点围绕业务上下文关联、工作流复用与外部资源优化三个方向。

**标签**: `#lab`, `#industry`

---

## AI 羊毛
{: #sec-ai-deals .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-deals" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-deals-1"></a>
### [Koofr 1TB 终身 129.9 美元](https://www.appinn.com/koofr-1tb/) ⭐️ 7.0/10

你看到的内容可能由第三方 AI 基于小众软件文章提炼总结而成，可能与原文真实意图存在偏差。不代表小众软件观点和立场。请&lt;a href=&quot;https://www.appinn.com/koofr-1tb/&quot; target=&quot;\_blank&quot;&gt;点击链接阅读原文&lt;/a&gt;细致比对和校验。&lt;br /&gt;&lt;br /&gt;Koofr 云存储提供永久免费 10GB 存储空间，支持 WebDAV、Rclone 功能；当前可通过 StackSocial 使用优惠码 KOOFR 以 129.9 美元购买 1TB 终身订阅，该优惠为年内再次放出。

rss · 小众软件 · 11月24日 03:24

**「为什么重要」** 该优惠为年内第三次放出，相比官网 100GB 年付 19.67 欧元、500GB 年付 68.85 欧元的定价，终身 1TB 方案长期使用成本更低；免费 10GB 空间可先验证服务兼容性，适合有服务器备份、跨云同步需求的用户。

**「可关注」** 可关注：Koofr 原生支持 Rclone 与 WebDAV，可直接对接命令行备份脚本，适合需要低成本长期备份服务器小文件、跨云同步的场景。

**标签**: `#free-tier`, `#promo`, `#coupon`

---

<a id="item-ai-deals-2"></a>
### [Gemini 土区 Pro/Plus 年付半价](https://www.v2ex.com/t/1259288#reply22) ⭐️ 7.0/10

V2EX 用户 spediacn 分享土耳其区 Google Gemini AI Pro/Plus 年付半价促销信息：Pro 年付 3599.99 土耳其里拉，Plus 年付 999.99 土耳其里拉；到期后续费价格分别为 8999.99、1999.99 土耳其里拉/年，材料未明确活动有效期与领取限制。

rss · V2EX Hot · 11月23日 18:35

**「可关注」** 可关注：土耳其区用户可留意该地区性年付半价促销，需注意后续续费价格较首年有明显上涨。

**标签**: `#promo`, `#limited-region`

---