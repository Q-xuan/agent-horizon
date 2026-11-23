---
layout: default
title: "Horizon Summary: 2026-11-24 (EN)"
date: 2026-11-24
lang: en
---

> From 219 items, 20 important content pieces were selected

---

**Agent Harness Architecture**
1. [OpenCode v2.4.0 发布](#item-harness-arch-1) ⭐️ 8.3/10
2. [openai-agents-python α2 发布](#item-harness-arch-2) ⭐️ 7.8/10
3. [Graphiti v0.32.0 弃 Kuzu](#item-harness-arch-3) ⭐️ 7.8/10
4. [mini-swe-agent 登上 GitHub Trending 榜](#item-harness-arch-4) ⭐️ 5.0/10

**AI Agent Engineer**
1. [NariQ 发布 Qwen3.8-27B 3-bit 量化](#item-agent-engineer-1) ⭐️ 8.0/10
2. [Clover-35B-A3B-Preview 发布](#item-agent-engineer-2) ⭐️ 8.0/10
3. [Hugging Face 发布智能体评估指南](#item-agent-engineer-3) ⭐️ 7.8/10
4. [HF 论文：AgentRoboCritic 机器人控制评估](#item-agent-engineer-4) ⭐️ 7.0/10
5. [HF 论文：Intent Contracts 工具授权隔离](#item-agent-engineer-5) ⭐️ 7.0/10
6. [HF 每日论文：MemOnce 架构提出](#item-agent-engineer-6) ⭐️ 6.0/10
7. [RoboTrack 开源 机器人操作跟踪基准](#item-agent-engineer-7) ⭐️ 5.8/10

**AI Daily**
1. [OpenAI 与 Cisco 联合发布 Shirudo](#item-ai-daily-1) ⭐️ 7.8/10
2. [EFS beta 上线 支持零数据保留](#item-ai-daily-2) ⭐️ 7.8/10
3. [Claude Ship beta 发布](#item-ai-daily-3) ⭐️ 7.8/10
4. [Anthropic 发布编码代理安全指南](#item-ai-daily-4) ⭐️ 7.8/10
5. [语义治理策略防御 AI Agent 意图劫持](#item-ai-daily-5) ⭐️ 7.8/10
6. [KPMG 谈 frontier AI 与客户数据 safeguard](#item-ai-daily-6) ⭐️ 5.8/10

**AI Deals**
1. [Google Gemini 黑五五折 AI Pro/Plus 年费 100/24 美元](#item-ai-deals-1) ⭐️ 8.0/10
2. [DevSwarm 创业团队免费席位开放](#item-ai-deals-2) ⭐️ 6.0/10
3. [Fly.io 免费计划上线](#item-ai-deals-3) ⭐️ 6.0/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [OpenCode v2.4.0 发布](https://github.com/anomalyco/opencode/releases/tag/v2.4.0) ⭐️ 8.3/10

OpenCode agent harness v2.4.0 引入内置持久化桌面浏览器运行时，支持导入 Chrome、Edge、Firefox、Safari 的登录状态与扩展，会话跨重启保持。新增自动化系统，支持定时器、cron 及 MCP 事件触发，通过 /automation 命令管理。视频生成工具 generate\_video 上线，后台渲染并保存至工作区。TUI 采用新设计，Windows 任务栏显示会话进度。

github · github-actions\[bot\] · Nov 23, 09:22

**「设计要点」** 桌面浏览器以独立持久化配置文件运行，与 agent 共享会话状态。自动化系统通过 MCP Events beta 实现事件驱动，支持心跳与自动重连。SDK 采用异步插件加载，端点立即返回部分结果，客户端通过事件监听完成刷新。

**「改了什么」** 内置持久化桌面浏览器，支持多浏览器配置导入与扩展管理，聊天链接在浏览器窗格打开。自动化框架支持 prompt、脚本、shell 命令的定时、cron 及 MCP 事件触发。新增 generate\_video 工具，后台渲染视频并保存到工作区。插件自动更新机制支持版本范围与 Git 引用，每 24 小时检查。SDK 端点不再等待插件加载，立即返回已加载内容，通过 \*.updated 事件通知变更。多项工具路径与配置项重命名：experimental\_image\_generate 改为 generate\_image，session 工具路径下移。MCP 服务器默认协商最新协议，GitHub Copilot 认证改为 COPILOT\_GITHUB\_TOKEN。

**Tags**: `#runtime`, `#tools`, `#mcp`

---

<a id="item-harness-arch-2"></a>
### [openai-agents-python α2 发布](https://github.com/openai/openai-agents-python/releases/tag/v1.0.0-alpha.2) ⭐️ 7.8/10

openai/openai-agents-python 发布 v1.0.0-alpha.2。这是 OpenAI Python Agents SDK 的 GitHub 预览版，捆绑 openai-agents 与原生 Codex 运行时。支持跨 worker 恢复对话和待处理审批，可恢复原生 Codex 的 exec\_command 与 apply\_patch 审批。新增工具执行钩子、Runner 文本脱敏、操作追踪及 OpenTelemetry 导出。Alpha.2 引入新的持久化状态格式（schema 1.24），Alpha.1 无法读取新快照，升级时必须先更新读取器。安装包支持 CPython 3.10–3.14，提供 Linux x86/ARM64、macOS ARM64、Windows x64 的 SHA-256 验证 wheel。

github · markstuart-oai · Nov 23, 20:11

**「设计要点」** 运行时捆绑 openai-agents 与嵌入式 Codex Core rust-v0.166.0。ResumableSession 通过 ResumableSessionStore（原子条件写入或 Redis）持久化对话历史与待处理审批，checkpoint 版本为 2。工具执行层提供 prepare\_tool\_input、prepare\_tool\_output、prepare\_tool\_declaration 钩子，sdk\_only\_tool\_hooks=True 禁用原生 Codex 工作区工具。观测层支持 RunConfig.redact\_text 文本脱敏、operation\_detail 追踪级别，以及 OpenTelemetryTracingProcessor 导出。权限机制限制原生审批仅支持一个待处理的直接 exec\_command 或 apply\_patch，需恢复相同工作区路径、权限和钩子。

**「改了什么」** 持久化状态格式从 Alpha.1 的 schema 1.22 升级到 1.24，Alpha.1 读取器无法读取新快照。新增 ResumableSession 跨 worker 恢复能力，支持 Responses 和 Codex provider。原生 Codex 审批恢复支持一种待处理的 exec\_command 或 apply\_patch 审批。工具执行新增 prepare\_tool\_input、prepare\_tool\_output、prepare\_tool\_declaration 钩子及 sdk\_only\_tool\_hooks 开关。Runner 文本脱敏与操作追踪（metadata/content 模式）变为可选。Codex Core rust-v0.166.0 补丁阻止同步 PreToolUse 处理器失败或超时时进行原生调度。

**「评论」** 无社区评论。

**Tags**: `#runtime`, `#tools`, `#memory`, `#permissions`

---

<a id="item-harness-arch-3"></a>
### [Graphiti v0.32.0 弃 Kuzu](https://github.com/getzep/graphiti/releases/tag/v0.32.0) ⭐️ 7.8/10

Graphiti v0.32.0 发布，移除 Kuzu 图数据库驱动，新增嵌入式 Relate 图驱动。UUID 查询现在强制按 group\_id 校验边界，跨组 UUID 直接返回 NodeNotFoundError 或 EdgeNotFoundError，影响 episodes、facts（EntityEdge.get\_by\_uuid/get\_by\_uuids）、sagas（summarize\_saga）和 add\_triplet。独立部署的 MCP server 升级至 1.1.3 并移除 neo4j 依赖，同时修正 Anthropic 默认模型配置及 temperature 参数传递问题。

github · mehulp93 · Nov 23, 21:16

**「设计要点」** 存储层从 Kuzu 切换为嵌入式 Relate 驱动，运行时依赖简化。权限模型从全局 UUID 可见改为强 group 边界校验，episodes/facts/sagas 的 UUID 查找现在受 group\_id 约束，未传 group\_id 时 add\_episode 仅查默认组。新增单图并发摄取能力。

**「改了什么」** 移除 Kuzu driver 和 neo4j 额外依赖，UUID 操作增加 group 边界检查，未知前驱 episode UUID 从跳过改为报 NodeNotFoundError。独立 MCP 镜像升级 server 到 1.1.3，LLM 客户端修正 Anthropic 默认模型、停止发送 temperature 参数，并新增嵌入式 Relate 驱动与单图并发摄取。

**Tags**: `#runtime`, `#permissions`, `#mcp`, `#memory`

---

<a id="item-harness-arch-4"></a>
### [mini-swe-agent 登上 GitHub Trending 榜](https://github.com/SWE-agent/mini-swe-agent) ⭐️ 5.0/10

这是GitHub Trending收录的SWE-agent团队推出的极简AI软件工程代理mini-swe-agent，核心特点为仅100行代码、无复杂配置与大型单体仓库依赖，声称在SWE-bench验证集上得分超过74%，且在DeepSWE基准上表现优于Claude Code与Codex，支持GitHub issue修复与命令行辅助任务，目前已作为Ramp SWE-Bench的底层运行组件，同时官方推出了构建极简AI代理的配套教程，还发布了新的高难度基准ProgramBench。

rss · GitHub Trending Daily · Nov 23, 23:00

**「设计要点」** 采用100行代码的极简实现，无大型配置文件和单体仓库依赖，主打轻量化部署与运行，可直接用于GitHub issue修复和命令行辅助场景。

**「改了什么」** 作为新推出的轻量化AI软件工程代理，无传统代理工具的复杂配置与大型仓库依赖，配套发布构建极简AI代理的教程，同时被集成至Ramp SWE-Bench评测体系，还推出了新的高难度基准ProgramBench。

**Tags**: `#eval`, `#runtime`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [NariQ 发布 Qwen3.8-27B 3-bit 量化](https://huggingface.co/nari-labs/Qwen3.8-27B-NariQ-GGUF) ⭐️ 8.0/10

NariQ 发布 Qwen3.8-27B 的 3-bit 及更低比特量化版本，文件大小约 10GB。公开的基准数据显示其在 DeepSWE、Terminal-Bench 2.1、AIME 等 agentic 与推理基准上接近 BF16 精度，当前需配合 nari-labs 维护的 llama.cpp 分叉运行，解码速度在 RTX PRO 6000 上与其他量化版本相当，4K 至 64K 上下文长度下的表现也已公开。

hackernews · toebee · Nov 23, 13:42 · [Discussion](https://news.ycombinator.com/item?id=50611402)

**「为什么重要」** 这是首个公开宣称在长周期 agentic 任务上保留 BF16 级别性能的 3-bit 及更低比特量化方案，可降低本地部署 coding agent 的存储与显存占用，但目前仅支持自定义 llama.cpp 分叉，Apple M 系列等非 CUDA 硬件的兼容性与实际 workload 表现尚未得到充分验证。

**「可关注」** 可关注其自定义 llama.cpp 分叉对不同硬件（尤其是 Apple M 系列）的适配进展，以及后续公开的更多真实业务场景下的性能表现。

**「评论」** 社区对量化效果存在正向反馈与谨慎态度，部分用户认可其覆盖多类长周期任务的基准设计，也有用户质疑低比特量化丢失的信息无法被现有基准完全覆盖，同时还有用户关注其与同类量化方法（如 lookatmyquant、TCQ 等）的对比以及 Apple M 系列设备的运行表现。

**Tags**: `#coding-agent`, `#eval`, `#harness`

---

<a id="item-agent-engineer-2"></a>
### [Clover-35B-A3B-Preview 发布](https://huggingface.co/papers/2611.24636) ⭐️ 8.0/10

2026年11月23日，Hugging Face Daily Papers发布Clover-35B-A3B-Preview技术报告。该模型是总参35B、激活参3B的MoE扩散语言模型，支持思维模式生成，采用Gated Delta Networks适配块扩散架构，将之前生成上下文的循环记忆与当前块内的双向softmax注意力结合，历史记忆读出与当前块token在共享softmax中竞争，配备可学习块大小校准与零初始化的右上下文卷积分支，在7项agent基准测试中取得领先成绩，其中SWE-bench Verified得分73.6，Terminal-Bench 2.1得分51.7；单块NVIDIA GB300 GPU以BF16精度跑内部agent工作负载时，生成速度达680 tokens/s。

rss · Hugging Face Daily Papers · Nov 23, 00:00

**「为什么重要」** 该模型的块扩散架构创新与agent基准测试表现，为coding agent的模型选型、架构设计、效果评估工作提供了可直接参考的实证依据。

**「可关注」** 可关注：Clover将循环记忆与块内双向softmax注意力结合，搭配零初始化右上下文卷积分支的块扩散架构，在仅激活3B参数的情况下实现了agent任务的领先性能，为低激活参数量agent模型设计提供了新思路。

**Tags**: `#coding-agent`, `#eval`, `#memory`, `#model-architecture`

---

<a id="item-agent-engineer-3"></a>
### [Hugging Face 发布智能体评估指南](https://huggingface.co/blog/agentic-evals) ⭐️ 7.8/10

Hugging Face 于 2026 年 11 月 23 日发布构建与维护智能体评估（agentic evaluation）指南。文章梳理评估从问答、智能体到团队/集群的三代演进，拆解智能体评估的八个构建步骤，并指出 98.2% 的模型-基准分数仅由单方报告。文中引用 Terminal-Bench 审计：固定模型仅更换智能体 harness，准确率波动可达 29.9 个百分点；Artificial Analysis 称其 2026 年 10 月发布的 Intelligence Index v5 中 60% 依赖私有测试集。Hugging Face Hub 目前托管约 3500 个评估排行榜与约 17000 个评估数据集（过去一年增长 16 倍），并新增 Traces、Benchmarks、Environments 三类抽象。

rss · Hugging Face Blog · Nov 23, 00:00

**「为什么重要」** 该指南直接面向构建评估系统的工程师，系统化拆解智能体评估的软件栈与误差来源。针对单方报告与 harness 偏差等已暴露问题，文中提出开源协作与组件级开放策略，为提升评估可验证性提供了具体路径。

**「可关注」** 可关注：智能体评估分数受 harness、环境、验证器全栈影响，Terminal-Bench 审计显示固定模型仅更换 harness 即可导致 29.9 个百分点的准确率波动，复现实验需同步披露完整配置。

**Tags**: `#eval`, `#harness`

---

<a id="item-agent-engineer-4"></a>
### [HF 论文：AgentRoboCritic 机器人控制评估](https://huggingface.co/papers/2611.26613) ⭐️ 7.0/10

2026年11月23日Hugging Face每日论文收录arXiv论文2611.26613，提出AgentRoboCritic动作级意图导向评判框架，用于评估前沿多模态智能体在直接机器人控制场景下的能力。该框架要求策略智能体为每个动作声明局部意图，评判器对照意图评估动作结果与失败模式，覆盖12项操作基准，解决了现有基准仅统计回合级成功率、无细粒度失败分析的问题。相关结论对构建智能体评估系统的工程师有参考价值。

rss · Hugging Face Daily Papers · Nov 23, 00:00

**「为什么重要」** 当前前沿智能体机器人控制能力缺乏细粒度评估工具，该框架填补了现有回合级成功率基准的分析空白。其意图导向的动作级评判思路若验证有效，或可复用到其他需要细粒度智能体行为评估的场景。

**「可关注」** 可关注：现有智能体评估基准普遍缺少细粒度失败归因能力，该框架的动作级意图对齐评判思路可作为同类评估系统的设计参考。

**Tags**: `#eval`

---

<a id="item-agent-engineer-5"></a>
### [HF 论文：Intent Contracts 工具授权隔离](https://huggingface.co/papers/2611.24025) ⭐️ 7.0/10

2026年11月23日Hugging Face每日论文分享了一篇针对工具调用LLM Agent的授权接口研究，提出Intent Contracts模式，核心是将规划模型与工具访问隔离：规划模型不持有工具，每步仅提交包含目标、用户原话、范围字段的日志化合同，代码校验后由小型可信模型对照用户原话检查并直接写入工具调用，且规划模型对工具调用的影响被限制在预先提交的合同范围内，执行粒度由可信侧决定。研究将该方案与两种人工审核规划模型直接生成命令的方案做了对比，但当前公开内容被截断，完整评估细节暂不可查。该研究直接面向Agent权限与工具调用管控场景，相关工程师可参考其隔离设计思路。

rss · Hugging Face Daily Papers · Nov 23, 00:00

**「为什么重要」** 该研究针对工具调用Agent的权限管控痛点提出了可落地的隔离设计思路，对Agent harness与权限设计有直接参考价值，但完整评估结果未公开，实际安全性与可用性尚待验证。

**「可关注」** 可关注：工具调用Agent可将规划逻辑与工具执行权限做隔离，通过前置合同校验+可信侧写入工具调用的方式，降低规划模型直接操作工具带来的越权风险。

**Tags**: `#permissions`, `#harness`, `#coding-agent`, `#eval`

---

<a id="item-agent-engineer-6"></a>
### [HF 每日论文：MemOnce 架构提出](https://huggingface.co/papers/2611.27973) ⭐️ 6.0/10

2026年11月23日Hugging Face Daily Papers收录论文《MemOnce: A Scalable Memory Architecture for Large Language Models》，该论文当前获得17次每日论文点赞，提出面向大语言模型的可扩展记忆架构MemOnce。该架构针对标准Transformer逐层逐token KV缓存引发的线性GPU内存增长、二次计算复杂度问题，以及现有线性时间架构细粒度细节丢失的缺陷，采用记忆编码器-解码器设计，仅缓存少量最终层隐藏状态作为紧凑记忆表示，动态解码回KV缓存供推理使用。当前公开内容仅为截断摘要，无性能基准、实现细节与可复现评估结果，完整技术价值需查阅完整论文。该研究主要面向长时程交互、持续交互场景下的LLM部署，以及agent系统的记忆与上下文管理需求。

rss · Hugging Face Daily Papers · Nov 23, 00:00

**「为什么重要」** 该研究直击长时程agent系统记忆管理的核心痛点，若后续完整论文验证设计有效性，有望降低长上下文场景下的GPU内存占用与推理计算开销。当前仅公开截断摘要，实际效果与落地可行性尚未证实。

**「可关注」** 可关注：记忆编码器-解码器压缩KV缓存的折中思路，若后续公开实现与评估结果，可评估其在长上下文agent场景下的内存占用与细节保留的trade-off。

**Tags**: `#memory`

---

<a id="item-agent-engineer-7"></a>
### [RoboTrack 开源 机器人操作跟踪基准](https://huggingface.co/blog/allenai/robotrack) ⭐️ 5.8/10

2026-11-23，Hugging Face 博客发布 RoboTrack，一套面向真实世界机器人操作的点跟踪基准与训练数据套件。RoboTrack-Bench 包含 307 段人工标注视频（2,522 条点轨迹），覆盖 DROID、Ego-Exo4D、MolmoAct 2 与 EgoVerse，场景含 clutter、遮挡及第一/第三人称视角。配套的 RoboTrack-15M 基于 Ai2 MolmoSpaces 仿真环境生成 1,500 万条合成点轨迹。评估显示主流跟踪器在 RoboTrack-Bench 上的 AJ 分数比 RoboTAP 低 3.0–6.6 分，CoWTracker 从 70.5 降至 63.9；基于 AllTracker 微调的 RoboTracker 与基于 CoWTracker 训练的 RoboTracker-Warp 均超越各自基线，后者在五个基准中的四个达到 SOTA。代码、数据集、技术报告与模型权重已公开。

rss · Hugging Face Blog · Nov 23, 17:20

**「为什么重要」** 现有机器人跟踪基准无法反映真实操作场景中的遮挡与视角变化。RoboTrack-Bench 上所有测试模型的 AJ 分数均低于 RoboTAP，且 BootsTAPNext 在真实视频训练的增益未能在仿真基准 RGB-Stacking 上保持，反而出现排名反转，说明当前训练数据与真实操作存在分布不匹配。RoboTrack-15M 的加入能提升真实视频跟踪效果，为机器人操作感知提供了可复用的训练与评测组件。

**「可关注」** 可关注：主流跟踪器在 RoboTrack-Bench 上的 AJ 分数普遍低于 RoboTAP 3.0–6.6 分，且 CoWTracker 对 CoTracker3 的领先优势从 4.7 AJ 缩小至 2.1 AJ，说明现有模型在真实操作场景中的泛化能力不足，仿真到真实的迁移仍是瓶颈。

**Tags**: `#eval`

---

## AI Daily

<a id="item-ai-daily-1"></a>
### [OpenAI 与 Cisco 联合发布 Shirudo](https://openai.com/index/introducing-shirudo) ⭐️ 7.8/10

OpenAI 与 Cisco 联合发布开源 Linux 运行时 Shirudo。该工具旨在帮助团队在滚动更新补丁期间保护正在运行的系统。公告未披露具体版本号、许可证类型或系统兼容性要求。

rss · OpenAI Blog · Nov 23, 21:20

**「可关注」** 开源 Linux 运行时 Shirudo 为补丁滚动更新场景提供运行中系统保护能力。

**Tags**: `#open-source`, `#product`, `#lab`, `#industry`

---

<a id="item-ai-daily-2"></a>
### [EFS beta 上线 支持零数据保留](https://claude.com/resources/articles/zero-data-retention-with-enterprise-frontier-safeguards) ⭐️ 7.8/10

Anthropic 发布 Enterprise Frontier Safeguards（ EFS ）公测版，为企业客户提供 零数据保留（ ZDR ） 环境下的高级滥用检测能力。EFS 在超过 100 家企业客户（含四分之一 Fortune 100 强）的协作下开发，覆盖医疗、金融、法律等强监管行业。系统通过自动化安全监控分析客户自有存储中的请求模式，生成不包含输入输出的 Safety Case 供客户审查；Anthropic 与云服务商均不保留客户数据，且数据不用于模型训练。目前 EFS 已在 Claude Platform、Claude Platform on AWS、Amazon Bedrock 及 Claude on Google Cloud 上线，Microsoft Foundry 支持即将推出。

rss · Claude Blog · Nov 23, 00:00

**「为什么重要」** EFS 解决强监管行业使用前沿模型时的数据主权与合规矛盾，使企业无需泄露敏感数据即可获得自动化滥用检测。这标志着 Anthropic 从单纯提供模型能力转向构建企业级安全基础设施，可能加速 AI 在金融、医疗等高风险场景的部署。

**「可关注」** 可关注：EFS 的自动化安全监控直接在客户控制的存储（ Amazon S3 或 Google Cloud Storage ）上运行，Safety Case 通过 API 或云存储输出，可对接现有 SIEM 系统，且全程不暴露原始输入输出给 Anthropic 人员。

**Tags**: `#lab`, `#policy`, `#product`, `#industry`

---

<a id="item-ai-daily-3"></a>
### [Claude Ship beta 发布](https://claude.com/resources/articles/introducing-claude-ship) ⭐️ 7.8/10

Anthropic 于 2026-11-23 发布 Claude Ship（beta），让 Claude 能按团队策略自动审查、修复并合并 PR。该功能由已 GA 的 Code Review 及新增的 PR Steward 和 Claude Approvals 组成，前者负责多维度审查，后者负责修复 CI 失败和审批决策。目前仅支持 Claude Team 与 Enterprise 计划及 GitHub 仓库，且不面向 Zero Data Retention、HIPAA 或客户管理加密密钥的团队。符合条件的 Enterprise 组织可在 2027 年 1 月 15 日前申领至少 $10,000 额度。

rss · Claude Blog · Nov 23, 00:00

**「为什么重要」** 当团队已普遍使用 AI 编码代理时，Claude Ship 旨在填补 PR 创建后的手动审查与合并瓶颈，将代码交付速度与编写速度对齐。团队可通过策略文件与观察模式保留控制权，同时兼容现有分支保护规则。

**「可关注」** 可关注：Claude Approvals 通过仓库内的策略文件定义审批规则，Anthropic 建议先以 observe-only 模式运行并积累信任，再将其设为分支保护的强制检查。

**Tags**: `#product`, `#industry`, `#agent`

---

<a id="item-ai-daily-4"></a>
### [Anthropic 发布编码代理安全指南](https://claude.com/resources/articles/enterprise-guide-to-securing-coding-agents) ⭐️ 7.8/10

Anthropic 发布企业级编码代理安全指南，针对 Claude Team 与 Enterprise 计划用户。指南列出评估编码代理的六个问题，界定凭证泄露、未审查依赖、数据外泄、提示注入四类风险，并建议通过权限检查、内核级沙箱、网络出站白名单实施分层控制。Salesforce 标准化采用 Claude Code 后报告 79% 与 5% 两项指标。指南适用于直接使用 Claude 或通过 AWS、Google Cloud、Azure 等云平台访问的用户。

rss · Claude Blog · Nov 23, 00:00

**「为什么重要」** 该指南由 Anthropic 官方发布，为企业提供编码代理安全框架，直接回应代理规模化部署中的提示注入与权限滥用风险。其将 SOC 2、ISO 27001 及 BAA 等合规要求纳入编码代理管理，表明安全合规在企业级编码代理部署中的重要性。

**「可关注」** Claude Code Enterprise 提供技能与插件恶意内容扫描、审计 API 及会话遥测导出，可在集中管理界面设置硬拒绝规则。

**Tags**: `#product`, `#industry`, `#lab`

---

<a id="item-ai-daily-5"></a>
### [语义治理策略防御 AI Agent 意图劫持](https://developers.googleblog.com/did-the-user-ask-for-this-securing-ai-agents-against-intent-hijacking-with-semantic-governance-policies/) ⭐️ 7.8/10

Google 研究人员演示 AI Agent 的意图劫持攻击：攻击者将恶意指令嵌入工具返回的非信任内容（如账单文件），诱使 Agent 执行未授权操作。在 AgentDojo v1.2.2 基准（97 个用户任务、949 次攻击运行）中，无防护时攻击成功率为 48.7%，启用 Semantic governance policies 后降至 0.9%，良性任务效用平均下降 2.6 个百分点。该策略在工具调用执行前比对用户意图，将工具返回内容视为数据而非指令；剩余成功案例均为不涉及工具调用的纯文本操纵，而 929 次需要工具调用的攻击在六次运行中均未成功。

rss · Google Developers AI · Nov 23, 00:00

**「为什么重要」** 该工作识别出 Agent 系统的关键攻击面——非信任工具输出可覆盖用户意图——并提供开放基准（AgentDojo）与可部署缓解方案及量化权衡。对于构建 coding agent 或执行 harness 的团队，这强调需将外部数据视为数据而非指令，并在执行前验证动作是否符合原始用户请求。

**「可关注」** 可关注：在 Agent 网关层对工具调用做用户意图匹配，将工具返回内容标记为数据而非指令，可大幅降低间接提示注入成功率，同时需评估良性任务的过度拦截率。

**Tags**: `#lab`, `#industry`, `#eval`, `#policy`, `#open-source`

---

<a id="item-ai-daily-6"></a>
### [KPMG 谈 frontier AI 与客户数据 safeguard](https://claude.com/resources/articles/kpmg-todd-lohr-on-ai-when-your-data-is-also-your-clients-data) ⭐️ 5.8/10

Claude Blog 发布了 KPMG 美国副董事长、客户技术与创新负责人 Todd Lohr 的访谈预览，聚焦专业服务机构在持有客户敏感数据的前提下落地 frontier AI 的实践。KPMG 拥有超27.6万名员工，业务覆盖138个国家和地区，其与 Anthropic 合作将 Claude 集成至税务业务平台 Digital Gateway，推出 Digital Gateway Powered by Claude。KPMG 的 Trusted AI 框架包含严格测试、持续监控、人工监督与独立 assurance 要求，同时正在评估 Anthropic 的 Enterprise Frontier Safeguards，该方案支持在自有云基础设施中保留数据，可加速强监管场景下的 AI 部署。

rss · Claude Blog · Nov 23, 00:00

**「为什么重要」** 该访谈披露了头部专业服务机构在强监管、高敏感数据场景下落地 frontier AI 的实操路径与合规思路，对同类型处理客户敏感数据的企业有参考价值。

**「可关注」** 可关注：Enterprise Frontier Safeguards 支持在组织自有云基础设施中保留数据的能力，可解决强监管场景下 frontier AI 部署的数据合规痛点。

**Tags**: `#industry`, `#policy`, `#enterprise`

---

## AI Deals

<a id="item-ai-deals-1"></a>
### [Google Gemini 黑五五折 AI Pro/Plus 年费 100/24 美元](https://www.appinn.com/google-ai-pro-black-friday-2026/) ⭐️ 8.0/10

你看到的内容可能由第三方 AI 基于小众软件文章提炼总结而成，可能与原文真实意图存在偏差。不代表小众软件观点和立场。请&lt;a href=&quot;https://www.appinn.com/google-ai-pro-black-friday-2026/&quot; target=&quot;\_blank&quot;&gt;点击链接阅读原文&lt;/a&gt;细致比对和校验。&lt;br /&gt;&lt;br /&gt;Google 推出 AI Pro/Plus 黑五五折优惠，Plus 年费 24.99 美元、Pro 年费 99.99 美元，均为首年优惠价，次年续费分别恢复 49.99 美元/年、199.99 美元/年。Plus 无 Antigravity 权限与 YouTube Premium Lite 权益，400GB 存储可共享 5 位家庭成员；Pro 包含 5TB 存储、Antigravity 高级模型权限、YouTube Premium Lite 等权益。11 月 20～26 日现有 Google One/AI 订阅老用户可提前参与，11 月 27 日起向符合条件的新用户开放，不同账户折扣可能不同，以结算页为准，当前活动主要面向美区账户。

rss · 小众软件 · Nov 23, 05:53

**「为什么重要」** 当前处于老用户优惠窗口期（11 月 20～26 日），符合条件的美区账户可提前锁定五折首年价，错过需等待新用户开放或后续活动，适合已有 Google 订阅或高频使用 Gemini 系列工具的用户。

**「可关注」** 可关注：已有未到期 Google One 订阅的用户升级 AI Pro/Plus 时无需先取消原套餐，系统会按比例抵扣剩余费用，避免权益中断。

**Tags**: `#promo`, `#limited-free`, `#coupon`

---

<a id="item-ai-deals-2"></a>
### [DevSwarm 创业团队免费席位开放](https://devswarm.ai/startups/) ⭐️ 6.0/10

DevSwarm officially offers a startup promotion: up to 10 free seats for 1 year, with no requirement to provide investor proof. The official page has not disclosed the specific claim deadline or full eligibility details, so the current claimability needs to be confirmed on the official page.

rss · HN Free API / Credits · Nov 23, 20:21

**「为什么重要」** If the offer is still active, it can save early-stage startups a year&\#x27;s worth of tool costs. However, there is currently insufficient information to confirm the validity of the activity.

**「可关注」** Pay attention: this offer has no investor threshold, but you need to visit devswarm.ai/startups on your own to verify whether it is still claimable, as well as the full rules and scope of application.

**Tags**: `#promo`, `#limited-free`

---

<a id="item-ai-deals-3"></a>
### [Fly.io 免费计划上线](https://fly.io/changelog/introducing-the-free-plan/) ⭐️ 6.0/10

Fly.io 官方在 changelog 宣布推出新的免费计划，当前公开内容未披露具体资源额度、使用限制、领取条件、有效期及截止时间等细节。

rss · HN Free API / Credits · Nov 23, 17:02

**「为什么重要」** Fly.io 是面向开发者的应用部署服务，新增免费计划对个人开发者、小型测试场景有潜在价值，但当前无公开细则，暂无法确认实际可用性。

**「可关注」** 可关注：官方后续补充免费计划的资源上限、区域限制、有效期等规则后，再评估是否适合个人测试或小型项目使用。

**Tags**: `#free-tier`, `#promo`, `#api`

---