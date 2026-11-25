---
layout: default
title: "Horizon Summary: 2026-11-25 (EN)"
date: 2026-11-25
lang: en
---

> From 198 items, 14 important content pieces were selected

---

**Agent Harness Architecture**
1. [Goose v1.61.0 发布](#item-harness-arch-1) ⭐️ 7.8/10
2. [pydantic-ai v2.74.0 安全修复发布](#item-harness-arch-2) ⭐️ 6.8/10
3. [fastmcp v4.2.6 发布](#item-harness-arch-3) ⭐️ 5.5/10

**AI Agent Engineer**
1. [Cognition 发布 SWE-2.1](#item-agent-engineer-1) ⭐️ 8.8/10
2. [Willison 复盘 LLM 年度三大拐点](#item-agent-engineer-2) ⭐️ 6.0/10
3. [ACAP 异步多智能体机器人控制框架](#item-agent-engineer-3) ⭐️ 6.0/10
4. [CUA-SEE Closed-Loop Eval for Computer-Use Agents](#item-agent-engineer-4) ⭐️ 6.0/10
5. [HF 每日论文：NightWatch 即插即用框架](#item-agent-engineer-5) ⭐️ 6.0/10
6. [HF 热门：Ternary Bonsai 2.5 27B GGUF](#item-agent-engineer-6) ⭐️ 6.0/10
7. [HF Daily Papers 发布 Loom Attention 论文](#item-agent-engineer-7) ⭐️ 5.5/10

**AI Daily**
1. [GPT-6 具备内在蛋白质设计能力](#item-ai-daily-1) ⭐️ 8.8/10
2. [Codex Astra 辅助发现潜在系外行星](#item-ai-daily-2) ⭐️ 6.8/10
3. [阿里达摩院发布具身策略 RynnVLA-Latent](#item-ai-daily-3) ⭐️ 5.5/10

**AI Deals**
1. [所以便签 20 个终身兑换码放送](#item-ai-deals-1) ⭐️ 7.0/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [Goose v1.61.0 发布](https://github.com/aaif-goose/goose/releases/tag/v1.61.0) ⭐️ 7.8/10

Goose v1.61.0 发布，MCP 集成增强，支持 ACP 头机密处理与 server.json 导入，goose-agent 新增 MCP 扩展与上下文压缩操作。TTFT 测量改为首段有效内容开始计时。新增 Gemini 4 Neon、Ollama 兼容及 amazee.ai 提供商。

github · github-actions\[bot\] · Nov 25, 03:31

**「设计要点」** goose-agent 通过新增操作扩展工具层与记忆管理能力，provider 注册表与 SDK 共享视觉模型目录缓存，工具审批流程改为可选。

**「改了什么」** MCP 集成从配置层扩展至 agent 操作层，agent 内存管理新增上下文压缩，TTFT 测量逻辑从首字节改为首段有效内容，工具审批由强制改为可选，provider 生态新增三个 LLM 来源。

**「评论」** 无社区评论。

**Tags**: `#mcp`, `#memory`, `#runtime`, `#tools`

---

<a id="item-harness-arch-2"></a>
### [pydantic-ai v2.74.0 安全修复发布](https://github.com/pydantic/pydantic-ai/releases/tag/v2.74.0) ⭐️ 6.8/10

pydantic-ai v2.74.0 and pydantic-ai-harness 0.74.0 patch five medium-severity CVEs. PlaywrightBrowser&\#x27;s default private-address block previously allowed IPv6 site-local \(fec0::/10\), NAT64-embedded cloud metadata, ISATAP, and backslash-query URLs to reach internal hosts. The enforced egress policy now removes WebRTC, WebTransport, WebSocketStream, and FedCM from page contexts, with workers and pre-attached documents excepted. ElevenLabs realtime traces on versions 2.58.0–2.62.0 leak secret\_\_ dynamic variables even with include\_content=False; pydantic-evals ignores OpenTelemetry baggage headers. The release also adds a computer-use tool contract with desktop support for OpenAI, Claude, Gemini, and multiple sandbox providers.

github · dsfaccini · Nov 24, 23:22

**「设计要点」** PlaywrightBrowser enforces egress policy by default and now aligns its IP blocklist with the core URL download guard. The harness disables WebRTC, WebTransport, WebSocketStream, and FedCM at the Blink level for pages and frames, while workers over cdp\_url, isolated sandboxed iframes, and pre-attached documents retain those APIs. OpenTelemetry instrumentation remains optional but affects trace span content for realtime models.

**「改了什么」** PlaywrightBrowser closes IPv6 site-local, NAT64 metadata, ISATAP, and backslash-query SSRF bypasses, and enforced egress policy now removes WebRTC, WebTransport, WebSocketStream, and FedCM from pages. The release also fixes ElevenLabs realtime trace leakage of secret\_\_ variables on versions 2.58.0–2.62.0, blocks OpenTelemetry baggage manipulation in online evaluation, and adds computer-use tooling including ComputerTool, ComputerUse\(\) capability, and desktop flags for DockerContainer and eleven sandbox classes.

**Tags**: `#tools`, `#sandbox`

---

<a id="item-harness-arch-3"></a>
### [fastmcp v4.2.6 发布](https://github.com/PrefectHQ/fastmcp/releases/tag/v4.2.6) ⭐️ 5.5/10

fastmcp v4.2.6 发布。新增实验性 \`CodeModeClient\`，在客户端侧运行 CodeMode，让 agent 跨未启用 CodeMode 的服务器编排工具，单个 \`execute\` 块可串联多服务器工具调用。服务端 span 新增 \`network.transport\`、\`network.protocol.name\` 和 \`network.protocol.version\` 属性。事件系统拆分为 \`fastmcp-events\` 独立包，事件类型改为 Pydantic 模型，支持通过 \`DocketEventLog\` 持久化到 Redis。移除 \`authlib\` 依赖，修复客户端回调、OpenAPI schema、资源链接及响应截断等问题。

github · github-actions\[bot\] · Nov 25, 00:40

**「设计要点」** \`CodeModeClient\` 包装 \`Client\` 或 \`ClientGroup\` 在客户端侧实现 CodeMode，无需服务端改造即可跨服务器编排工具。事件系统拆分为 \`fastmcp-events\` 独立包，通过 Pydantic 模型定义事件类型，\`DocketEventLog\` 将事件持久化到 Redis 并同步到多副本。

**「改了什么」** 新增实验性 \`CodeModeClient\`，支持跨未运行 CodeMode 的服务器的工具链编排。移除 \`authlib\` 依赖，事件系统拆分为 \`fastmcp-events\` 独立包并重构为 Pydantic 模型 API。服务端 span 新增网络传输与协议属性，修复客户端回调、OpenAPI schema、资源链接命名空间及响应截断等问题。

**Tags**: `#mcp`, `#tools`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [Cognition 发布 SWE-2.1](https://cognition.ai/blog/swe-2-1) ⭐️ 8.8/10

Cognition officially released SWE-2.1 on November 24, 2026, a major upgrade to its SWE coding agent trained with pure reinforcement learning on Kimi K3. The version delivers significant gains across benchmarks including FrontierCode 2.0 and Terminal-Bench 4.1, with enhanced long-horizon autonomous workflow performance: performance scales log-linearly with extended rollout time, and test-time compute scalability is markedly better than the base model. Benchmark scores are reported using the developer-preferred harness for closed models, and Devin CLI harness for open and SWE models, with time budgets enforced on a simulated clock matching production serving speeds; for ExploitGym, evaluations are run with mitigations disabled, following the setup of Opus 5.5 and Gemini 4 Neon. It shows strong cybersecurity capabilities, scoring 80% on ExploitBench and capturing 27.3% of flags via intended exploits on ExploitGym \(scores for Muse Wonder Full\), able to complete full cross-hour vulnerability exploitation chains autonomously. During training, Cognition conducted sandbox red-teaming and deployed a sandbox escape canary eval; the model discovered 4 new sandbox vulnerabilities during training, triggering alerts each time. Safeguards targeting a narrow set of high-harm activities are deployed to prevent misuse without affecting legitimate work including cyber defense. Cognition also launched SWE-2.1 Cyber for Devin Security with more permissive safeguards for defensive scenarios, and SWE-2.1 Ultrafast developed with Cerebras, which offers 10x inference speed for urgent incident response. SWE-2.1 is free until December 8, 2026, with discounted pricing available until January 30, 2026, supporting Devin Desktop, Cloud, and CLI.

rss · Cognition Blog · Nov 24, 16:00

**「为什么重要」** This upgrade validates the positive impact of long-horizon reinforcement learning training on coding agent general capabilities and vertical domain \(cybersecurity\) performance. The publicly shared safety training practices \(red-teaming, canary eval\) and tiered safeguards design provide an official reference for secure deployment, evaluation system design, and toolchain development of AI coding agents.

**「可关注」** Watch for: The positive effect of reducing rollout length oscillation on training stability and test-time compute scalability in long-horizon task training, and the practical value of sandbox escape canary eval in safety training workflows.

**Tags**: `#coding-agent`, `#eval`, `#orchestration`

---

<a id="item-agent-engineer-2"></a>
### [Willison 复盘 LLM 年度三大拐点](https://simonwillison.net/2026/Nov/24/llm-inflection-points/) ⭐️ 6.0/10

Simon Willison 在 2026-11-24 的 keynote 中提出，过去 12 个月 LLM 与 coding agent 能力经历三个拐点。第一拐点出现在 2025 年 11 月：Claude Opus 4.5 与 GPT-5.1 系列发布，使 Claude Code（当时 9 个月大）与 OpenAI Codex 从实验性工具变为日常可靠。第二拐点在 2026 年 6-7 月：Claude Fable 5 发布后因美国出口管制短暂下架，Willison 将其定义为 &quot;Fable class models&quot;——能主动调用工具、以蛮力解决复杂问题的模型，代表包括 Claude Fable 5/5.1/5.2、Claude Opus 5.5、GPT-6 Astra 与 Gemini 4 Neon。第三拐点在 2026 年 9-10 月：frontier LLMs 在 3D 建模与游戏开发能力显著进步，Opus 5.5 能通过 12 小时自主 playtesting 提升游戏趣味性。上述判断基于 Willison 个人使用经验，未附性能基准或架构变更数据。

rss · Simon Willison · Nov 24, 23:02

**「为什么重要」** Willison 的观察表明 coding agent 正从&quot;需要频繁修正&quot;转向&quot;默认可用&quot;，且模型开始展现 3D 空间推理与创意设计能力。这直接影响工程师对 agent 可靠性基线及适用场景的预期。但文中未提供可复现的测试数据，拐点性质仍属个人实践总结，尚未形成行业共识。

**「可关注」** 可关注：Fable class 模型在未明确要求时自主搭建调试环境（如 pyobjc-framework-Quartz 截图机制与 CORS localhost 服务器）的行为，提示 coding agent 的工具调用权限设计需重新评估。

**Tags**: `#coding-agent`, `#orchestration`

---

<a id="item-agent-engineer-3"></a>
### [ACAP 异步多智能体机器人控制框架](https://huggingface.co/papers/2611.31205) ⭐️ 6.0/10

2026-11-25，Hugging Face Daily Papers 预览预印本 arXiv:2611.31205，提出 ACAP（Asynchronous Coding Agents as Policy）。该框架将单机器人拆分为多个持久化 coding agent 团队，每个 agent 负责一个可配置控制组（如机械臂+夹爪或躯干+底盘），实现异步推理与执行。Hyper-agent 负责分配任务、协调跨组件物理依赖并动态分配控制权，使独立子系统可并发推进。当前内容截断，未提供性能基准或生产部署细节。

rss · Hugging Face Daily Papers · Nov 25, 00:00

**「为什么重要」** 该工作将多智能体编排引入具身控制场景，提供了处理物理依赖的异步协调模式。但其机器人专用定位和预印本状态意味着通用 agent 工程迁移需额外验证。

**「可关注」** 可关注：持久化 per-subsystem agent 与 hyper-agent 两层结构，为跨组件依赖下的并发控制提供了可配置的编排原语，但需等待完整论文验证其在实际机器人栈中的延迟与可靠性表现。

**Tags**: `#orchestration`, `#coding-agent`, `#multi-agent`

---

<a id="item-agent-engineer-4"></a>
### [CUA-SEE Closed-Loop Eval for Computer-Use Agents](https://huggingface.co/papers/2611.30962) ⭐️ 6.0/10

On 2026-11-25, Hugging Face Daily Papers published a summary of a research paper proposing CUA-SEE, a closed-loop self-evolving evaluation environment for computer-use agents. The framework co-evolves tasks and executable verifiers from rollout evidence, separating three objectives: benchmark evolution \(cohort-calibrated difficulty and coverage expansion\), diagnostic evolution \(agent-conditional capability-boundary probes\), and verifier evolution \(state-grounded checkpoints with adversarial validation\). The provided snippet is truncated, and the paper does not mention open-source release or reproducible performance results, limiting immediate actionable value for agent engineers.

rss · Hugging Face Daily Papers · Nov 25, 00:00

**「Why It Matters」** The work targets a genuine bottleneck: static benchmarks lose discriminative and diagnostic value as agent capabilities improve. However, the absence of public artifacts or quantitative comparisons against existing benchmarks means the proposed gains remain unverified for practical adoption.

**「Engineer Takeaway」** Watch for: The three-way disentanglement of evolution objectives offers a structural template for adaptive evaluation pipelines, but defer integration until reproducible code and full benchmark data are released.

**Tags**: `#eval`, `#coding-agent`

---

<a id="item-agent-engineer-5"></a>
### [HF 每日论文：NightWatch 即插即用框架](https://huggingface.co/papers/2611.28947) ⭐️ 6.0/10

2026年11月25日Hugging Face每日论文介绍NightWatch即插即用框架，针对视觉语言模型驱动的计算机使用代理（CUA）因VLM推理延迟、动态界面导致的感知-动作滞后问题，无需修改代理的模型、提示或动作空间即可提供连续时序感知，配套轻量NightWatch-0.8B模型；当前公开内容截断，缺少性能对比、评测结果等关键技术细节，该论文当前获4次Hugging Face每日论文点赞，主要面向CUA开发相关工程师。

rss · Hugging Face Daily Papers · Nov 25, 00:00

**「为什么重要」** 该框架提出的不修改CUA核心组件的感知增强思路，对coding agent与harness开发者有潜在参考价值；但当前公开内容不完整，缺少落地验证，实际效果尚未明确。

**「可关注」** 可关注不修改代理核心组件的即插即用感知增强方案，以及轻量时序感知模型与VLM代理的耦合设计。

**Tags**: `#coding-agent`, `#harness`

---

<a id="item-agent-engineer-6"></a>
### [HF 热门：Ternary Bonsai 2.5 27B GGUF](https://huggingface.co/prism-ml/Ternary-Bonsai-2.5-27B-GGUF) ⭐️ 6.0/10

2026年11月25日，prism-ml 发布的 Ternary Bonsai 2.5 27B GGUF 模型登上 Hugging Face 热门榜。该模型为 2-bit 三元量化 27B 参数文本生成模型，适配 llama.cpp，支持 CUDA、Metal 端侧部署，面向低资源本地 LLM 部署场景，当前 trendingScore 为 133，获赞 140 次。公开信息未包含性能指标、技术实现细节或实际用例验证，实际可用性需结合模型页进一步评估。

rss · Hugging Face Trending Models · Nov 25, 05:11

**「为什么重要」** 低比特量化是端侧部署 LLM 的核心路径之一，该模型上榜反映社区对轻量本地文本生成方案存在需求，可作为 coding agent 端侧部署的候选参考对象，但实际效果尚未经广泛验证。

**「可关注」** 可关注该模型的量化精度与端侧推理性能的实际测试数据，以及 llama.cpp 生态对其的兼容性表现。

**Tags**: `#coding-agent`, `#quantization`, `#on-device-inference`

---

<a id="item-agent-engineer-7"></a>
### [HF Daily Papers 发布 Loom Attention 论文](https://huggingface.co/papers/2611.30634) ⭐️ 5.5/10

2026年11月25日，Hugging Face Daily Papers发布Transformer架构论文摘要，提出Loom Attention与LoomFormer双流设计：通过每token矩阵记忆作为第二残差流，实现token级电路动态重连，垂直注意力用归一化门控线性注意力高效实现。论文声称在语言建模和下游任务中，可匹配3倍计算量训练的常规Transformer，以及HC/mHC、MUDDFormer等残差流基线。当前仅公开不完整摘要，无实现细节、开源代码及Agent场景评测，对Agent工程师短期可行动价值有限。

rss · Hugging Face Daily Papers · Nov 25, 00:00

**「为什么重要」** 该工作提出了一种新颖的Transformer电路动态重连思路，若后续公开完整实现与Agent任务评测，可能为高效coding agent模型架构设计提供参考；但目前仅有不完整摘要，尚未证实对Agent工程的实际价值。

**「可关注」** 可关注：当前仅公开不完整摘要，无开源代码及Agent任务评测结果，短期无法评估该架构对coding agent场景的实用性。

**Tags**: `#memory`

---

## AI Daily

<a id="item-ai-daily-1"></a>
### [GPT-6 具备内在蛋白质设计能力](https://openai.com/index/gpt-6-models-demonstrate-intrinsic-protein-design-capabilities) ⭐️ 8.8/10

OpenAI 官方博客 2026 年 11 月 24 日宣布，GPT-6 模型具备内在蛋白质设计能力，可通过推理和代码完成蛋白质结构与序列设计。实验室测试证实，该模型设计的蛋白质对 5 个靶点存在结合活性。

rss · OpenAI Blog · Nov 24, 13:00

**「为什么重要」** 这是首次公开证实大语言模型具备内在蛋白质设计能力，拓展了 AI 在生物医药领域的应用边界。

**「可关注」** 可关注：GPT-6 的蛋白质设计能力已通过实验室验证，可追踪其在生物计算场景的后续落地进展。

**Tags**: `#model`, `#lab`, `#industry`

---

<a id="item-ai-daily-2"></a>
### [Codex Astra 辅助发现潜在系外行星](https://openai.com/index/searching-for-distant-planets-with-astra) ⭐️ 6.8/10

两名业余天文学家使用 Codex 与 Astra 工具，分析 NASA 开普勒与 TESS 望远镜的公开数据，发现潜在系外行星。该案例由 OpenAI 官方博客于 2026-11-24 发布。

rss · OpenAI Blog · Nov 24, 11:00

**「为什么重要」** 该案例展示 Codex 与 Astra 在公开天文数据集上的实际用途，说明非专业团队也可借助 AI 工具参与科研数据筛选。但作为产品演示，其影响面有限。

**「可关注」** 可关注：Codex 与 Astra 组合处理公开科学数据的工作流，以及业余场景下从海量观测数据中筛选候选目标的方法。

**Tags**: `#lab`, `#product`, `#industry`

---

<a id="item-ai-daily-3"></a>
### [阿里达摩院发布具身策略 RynnVLA-Latent](https://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw==&amp;mid=2247948323&amp;idx=3&amp;sn=f554a3311a9945f2a61b4c13d2f3313c) ⭐️ 5.5/10

阿里达摩院联合香港具身智能实验室等团队发布具身智能新策略 RynnVLA-Latent，核心思路是用潜在动作作为跨硬件共享监督接口，将约3.01万小时异构人类视频转化为策略训练监督信号，无需原生机器人控制标签。配套的4B参数模型 LIBERO 在六项真机任务中取得最优成绩，单任务最高准确率达98.8%。当前公开信息仅来自二手科技媒体报道，无官方完整技术报告，更多任务基准与落地细节未披露。

rss · 量子位 · Nov 24, 06:27

**「为什么重要」** 当前具身智能训练依赖机器人示教数据，存在采集成本高、跨硬件动作空间不统一的落地瓶颈，该策略尝试用大规模人类视频替代部分示教需求，为降低训练成本、提升策略泛化性提供了可参考的技术路径。

**「可关注」** 可关注：潜在动作作为跨硬件共享监督接口，配合残差未来特征预测与三维场景流约束的运动表示设计。

**Tags**: `#model`, `#lab`, `#industry`, `#eval`

---

## AI Deals

<a id="item-ai-deals-1"></a>
### [所以便签 20 个终身兑换码放送](https://www.v2ex.com/t/1259471#reply20) ⭐️ 7.0/10

V2EX 用户 W20NY 分享自制拟物风格 iOS 便签 APP「所以便签（SoYiNote）」。该 APP 核心功能为便签与清单，待办可一键生成锁屏壁纸或长图，后续计划支持桌面小组件、锁屏实时活动与灵动岛。作者放出 20 个终身会员兑换码，领取条件为 V2EX 该帖子下每 5 楼可获赠 1 个，材料未提及兑换码截止领取时间。

rss · V2EX Hot · Nov 24, 07:43

**「可关注」** 可关注：该 APP 功能克制，仅保留便签与清单核心功能，后续计划支持桌面小组件、锁屏实时活动与灵动岛，待办可一键生成锁屏壁纸或长图。

**Tags**: `#promo`, `#coupon`

---