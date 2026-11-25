---
layout: default
title: "Horizon Summary: 2026-11-25 (ZH)"
date: 2026-11-25
lang: zh
---

> 从 198 条内容中筛选出 14 条重要资讯。

<nav id="ah-toc" class="ah-toc" aria-label="目录"><span class="ah-toc-title">目录</span><ul><li><a href="#sec-harness-arch"><span class="ah-toc-name">Harness 架构</span><span class="ah-toc-count">3条</span></a></li><li><a href="#sec-agent-engineer"><span class="ah-toc-name">Agent 工程师日报</span><span class="ah-toc-count">7条</span></a></li><li><a href="#sec-ai-daily"><span class="ah-toc-name">AI 日报</span><span class="ah-toc-count">3条</span></a></li><li><a href="#sec-ai-deals"><span class="ah-toc-name">AI 羊毛</span><span class="ah-toc-count">1条</span></a></li></ul></nav>

---

**[Harness 架构](#sec-harness-arch)**
1. [Goose v1.61.0 发布](#item-harness-arch-1) ⭐️ 7.8/10
2. [pydantic-ai v2.74.0 发布](#item-harness-arch-2) ⭐️ 6.8/10
3. [fastmcp v4.2.6 发布](#item-harness-arch-3) ⭐️ 5.5/10

**[Agent 工程师日报](#sec-agent-engineer)**
1. [SWE-2.1 编码智能体发布](#item-agent-engineer-1) ⭐️ 8.8/10
2. [Simon Willison 总结 LLM 与 coding agent 三大拐点](#item-agent-engineer-2) ⭐️ 6.0/10
3. [ACAP 异步多 Agent 机器人控制框架](#item-agent-engineer-3) ⭐️ 6.0/10
4. [CUA-SEE 自演化评估框架论文发布](#item-agent-engineer-4) ⭐️ 6.0/10
5. [NightWatch 即插即用感知框架](#item-agent-engineer-5) ⭐️ 6.0/10
6. [HF 热门：27B 三元量化 GGUF](#item-agent-engineer-6) ⭐️ 6.0/10
7. [HF 日报：Loom Attention 与 LoomFormer](#item-agent-engineer-7) ⭐️ 5.5/10

**[AI 日报](#sec-ai-daily)**
1. [GPT-6 展示内在蛋白质设计能力](#item-ai-daily-1) ⭐️ 8.8/10
2. [Codex 与 Astra 辅助发现潜在系外行星](#item-ai-daily-2) ⭐️ 6.8/10
3. [LIBERO 登顶六项真机具身任务](#item-ai-daily-3) ⭐️ 5.5/10

**[AI 羊毛](#sec-ai-deals)**
1. [所以便签 SoYiNote 兑换码放送](#item-ai-deals-1) ⭐️ 7.0/10

---

## Harness 架构
{: #sec-harness-arch .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-harness-arch" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-harness-arch-1"></a>
### [Goose v1.61.0 发布](https://github.com/aaif-goose/goose/releases/tag/v1.61.0) ⭐️ 7.8/10

Goose agent harness 发布 v1.61.0。MCP 集成增强：通过 ACP 传输 mcpServers 配置时所有请求头自动标记为 secret，支持导入 MCP server.json 格式，goose-agent 新增 MCP 扩展操作。新增 goose-agent 的 compaction 操作管理对话记忆，模型目录新增 Gemini 4 Neon、Ollama-compatible 及 amazee.ai provider。运行时修复 TTFT 统计时机（首段文本/thinking/tool call 即终止）、provider 刷新接口同步等待、Databricks OAuth 超时等问题，工具审批改为可选，并升级 @agentclientprotocol/sdk 至 2.6.0、Node 24.22.3 与 Electron Forge 8.0.1。

github · github-actions\[bot\] · 11月25日 03:31

**「设计要点」** Goose 作为 agent harness，通过 MCP 扩展层与外部工具交互，支持 ACP 协议传输。上下文压缩（compaction）机制直接作用于 goose-agent 的记忆管理。前端基于 Electron Forge，后端采用多 provider 注册制，支持声明式 provider 配置。

**「改了什么」** 新增 ACP 传输 mcpServers 配置时 headers 全部视为 secret、MCP server.json 配置导入、goose-agent 的 compaction 与 MCP 扩展操作。工具审批流程改为可选。TTFT 统计现在在首段文本、thinking 或 tool call 开始时终止。新增三个 LLM providers，升级 SDK 与 Node/Electron 依赖。

**标签**: `#mcp`, `#memory`, `#runtime`, `#tools`

---

<a id="item-harness-arch-2"></a>
### [pydantic-ai v2.74.0 发布](https://github.com/pydantic/pydantic-ai/releases/tag/v2.74.0) ⭐️ 6.8/10

pydantic-ai v2.74.0 与 pydantic-ai-harness 0.74.0 正式发布，修复 PlaywrightBrowser 工具中 6 个中危安全漏洞，包括 IPv6 站点本地地址与 NAT64 嵌入地址绕过、反斜杠 URL 解析绕过、WebRTC/WebTransport/WebSocketStream/FedCM 出口策略遗漏，以及 ElevenLabs 实时会话 OpenTelemetry 凭据泄露和在线评估 baggage 属性篡改。补丁同步将 \`ComputerTool\` 纳入核心契约，并为 DockerContainer、DaytonaSandbox、E2BSandbox 等 11 种沙箱添加 \`desktop=True\` 支持，以驱动 Anthropic、OpenAI、Google 的原生 computer use 工具。

github · dsfaccini · 11月24日 23:22

**「设计要点」** PlaywrightBrowser 默认启用强制出口策略，在页面和框架层移除 \`RTCPeerConnection\`、\`WebTransport\`、\`WebSocketStream\` 和 FedCM 并以 Blink 特性关闭启动 Chromium，但 workers 的 \`WebTransport\`、通过 \`cdp\_url\` 的 workers 中的 \`WebSocketStream\`、隔离沙盒 iframe 及附件前加载的文档仍保持开放；核心层新增 \`ComputerTool\` 契约并纳入 \`NATIVE\_TOOLS\_REQUIRING\_CONFIG\`，要求运行时提供 \`computer\` 工具驱动调用。

**「改了什么」** 修复 PlaywrightBrowser 在 IPv6 站点本地地址、NAT64 嵌入地址、反斜杠 URL 解析及 WebRTC/WebTransport 等协议上的私有地址封锁绕过漏洞，同时移除强制策略下页面和框架的对应 API。新增 \`ComputerTool\` 契约及 11 种沙箱的 \`desktop=True\` 支持，覆盖 Anthropic、OpenAI、Google 的原生 computer use 工具发送。

**标签**: `#tools`, `#sandbox`

---

<a id="item-harness-arch-3"></a>
### [fastmcp v4.2.6 发布](https://github.com/PrefectHQ/fastmcp/releases/tag/v4.2.6) ⭐️ 5.5/10

fastmcp v4.2.6 发布，新增实验性 \`CodeModeClient\`，允许 agent 跨多个 MCP 服务器链式调用工具，即使目标服务器未运行 CodeMode。事件系统拆分为独立包 \`fastmcp-events\`，事件类型从 check function 改为 Pydantic model，注册使用 \`@events.event\`，发射使用 \`await events.emit\`，并支持通过 \`DocketEventLog\` 持久化到 Redis。同时移除 \`authlib\` 依赖，服务端 span 增加 \`network.transport\` 等网络属性，并修复客户端回调、OpenAPI schema 序列化等 15 个技术问题。

github · github-actions\[bot\] · 11月25日 00:40

**「设计要点」** 客户端运行在 asyncio 上，事件通过 \`DocketEventLog\` 写入 Redis 实现跨副本持久化与分发。跨服务器工具编排在客户端侧通过 \`CodeModeClient\` 实现，不依赖服务端 CodeMode。

**「改了什么」** 新增实验性 \`CodeModeClient\` 支持跨服务器工具链式执行，事件系统拆分为 \`fastmcp-events\` 包并变更注册与发射 API，同时移除 \`authlib\` 依赖。服务端 span 增加网络传输属性，并修复客户端回调、OpenAPI schema、资源链接命名空间、响应截断序列化等 15 个 bug。

**标签**: `#mcp`, `#tools`

---

## Agent 工程师日报
{: #sec-agent-engineer .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-agent-engineer" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-agent-engineer-1"></a>
### [SWE-2.1 编码智能体发布](https://cognition.ai/blog/swe-2-1) ⭐️ 8.8/10

2026 年 11 月 24 日，Cognition 官方发布编码智能体 SWE-2.1，为 SWE-2 的重大升级版本，基于 Kimi K3 采用纯强化学习训练。该版本在 FrontierCode 2.0、Terminal-Bench 4.1 等编码基准，以及 ExploitBench、ExploitGym 等网络安全长程自主任务基准上均有显著提升：SWE-2.1 在 ExploitBench 取得 80%的得分，在 ExploitGym 中通过预期利用捕获 27.3%的旗帜，长时自主运行性能随 rollout 时间延长呈对数线性提升，测试时 scaling 曲线斜率较基础模型明显提升。训练过程中 Cognition 通过红队测试、持续安全监控和沙箱逃逸 canary 评估拦截风险，累计发现并修复 4 次训练环境新漏洞。Cognition 同时推出 safeguards 更宽松的 SWE-2.1 Cyber 版本向 Devin Security 开放，还与 Cerebras 合作发布 10 倍推理速度的 SWE-2.1 Ultrafast 版本；SWE-2.1 目前免费开放至 2026 年 12 月 8 日（Desktop 与 CLI 版本），折扣价有效期至 2026 年 1 月 30 日，面向编码、网络安全领域的开发者及 AI agent 工程、评估、工具链设计人员。

rss · Cognition Blog · 11月24日 16:00

**「为什么重要」** 该发布验证了纯强化学习训练长时自主编码、网络安全任务智能体的可行性，其长时 rollout 性能随计算量提升的 scaling 特性，对 AI agent 的测试时计算分配、长程任务设计有直接参考价值。目前这些能力在实际工程、安全场景中的落地效果尚未有公开验证。

**「可关注」** 可关注：长时自主编码、安全任务的性能随 rollout 时间对数线性提升，测试时计算分配策略会直接影响长程任务完成率；训练阶段优化 rollout 长度控制减少震荡，可提升模型对跨时长任务的训练稳定性与测试时计算利用率。

**标签**: `#coding-agent`, `#eval`, `#orchestration`

---

<a id="item-agent-engineer-2"></a>
### [Simon Willison 总结 LLM 与 coding agent 三大拐点](https://simonwillison.net/2026/Nov/24/llm-inflection-points/) ⭐️ 6.0/10

2026 年 11 月 24 日，Simon Willison 发布 AI Engineer Code Summit 主题演讲 recap，以 Claude Opus 4.5 发布一周年为节点，梳理过去 12 个月 LLM 与 coding agent 能力的三个拐点。第一个拐点为 2025 年 11 月，Claude Opus 4.5、GPT-5.1 系列模型发布，让 Claude Code、OpenAI Codex 等 coding agent 从「需频繁修正的辅助」变为日常开发中可可靠使用的工具。第二个拐点为 2026 年 6-7 月，Claude Fable 5 等「Fable 类模型」发布，这类模型在给定明确目标和必要工具时可自主拆解任务、brute force 解决复杂问题，成为作者认知中的前沿模型新基线。第三个拐点为 2026 年 9-10 月，frontier 模型 3D 建模与游戏开发能力大幅提升，不仅能生成可信的 3D 内容，还能通过长时间 playtest 优化游戏可玩性。文中未提供可复现的性能基准数据，所有能力判断均来自作者个人实践观察，且部分模型发布时间与当前公开信息存在差异，未经验证。

rss · Simon Willison · 11月24日 23:02

**「为什么重要」** 作为一线实践者的第一手观察，梳理了 coding agent 从「不可靠辅助」到「日常可用」再到「可自主完成复杂多步骤任务」的演进路径，为工程师评估当前模型能力提供了实践参考。但文中对模型能力的判断无公开基准数据支撑，部分模型信息未经验证，相关能力结论需结合实际测试确认。

**「可关注」** 可关注：前沿模型已从「需频繁修正的辅助工具」转向「给定目标和工具即可自主完成复杂任务」的基线，3D 空间理解与多步骤目标拆解能力是近期 coding agent 能力的突出变化点。

**标签**: `#coding-agent`, `#orchestration`

---

<a id="item-agent-engineer-3"></a>
### [ACAP 异步多 Agent 机器人控制框架](https://huggingface.co/papers/2611.31205) ⭐️ 6.0/10

2026-11-25，Hugging Face Daily Papers 发布 preprint 介绍 ACAP（Asynchronous Coding Agents as Policy）。该框架将机器人组织为持久化 coding agent 团队，每个 agent 负责一个可配置控制组（如机械臂与夹爪、躯干与底盘），实现异步推理与执行；另引入 hyper-agent 分配任务、协调跨组件物理依赖并动态分配控制权。当前内容截断，未提供性能基准或生产部署细节，且机器人专用场景限制了对通用 agent 工程工作流的直接迁移。

rss · Hugging Face Daily Papers · 11月25日 00:00

**「为什么重要」** 该工作提出了一种分层异步多智能体编排模式，将并发控制与依赖协调分离，对复杂系统 agent 工程有潜在参考价值；但 preprint 缺乏实证数据，实际效果尚未证实。

**「可关注」** 可关注：ACAP 用持久化 per-subsystem agent 加 hyper-agent 分层，解耦独立子系统的并发执行与跨组件依赖协调；但该框架面向机器人控制，通用 agent 工程场景的直接迁移性受限。

**标签**: `#orchestration`, `#coding-agent`, `#multi-agent`

---

<a id="item-agent-engineer-4"></a>
### [CUA-SEE 自演化评估框架论文发布](https://huggingface.co/papers/2611.30962) ⭐️ 6.0/10

2026-11-25，Hugging Face Daily Papers 收录论文《Self-Evolving Evaluation Environments for Computer-Use Agents》，提出 CUA-SEE 自演化评估环境。该框架针对 computer-use agents 设计，通过 rollout evidence 共同演化任务与可执行验证器，拆分为 benchmark evolution、diagnostic evolution、verifier evolution 三个目标。论文指出现有静态基准存在固定难度上限、特征覆盖有限、聚合分数粗略等问题，导致 discriminative 与 diagnostic value 逐渐减弱。当前材料为截断内容，未提及开源发布或可复现性能数据。

rss · Hugging Face Daily Papers · 11月25日 00:00

**「为什么重要」** 静态基准测试在 computer-use agents 能力快速提升背景下 discriminative 能力下降，CUA-SEE 提供了任务-验证器协同演化的解决思路。但论文未公开可复现结果，其实践价值尚待完整论文验证。

**「可关注」** 可关注：现有 agent 评估 harness 多依赖静态验证规则，CUA-SEE 提出的从 rollout 证据中演化验证器的思路，可能改变评估环境的设计假设。

**标签**: `#eval`, `#coding-agent`

---

<a id="item-agent-engineer-5"></a>
### [NightWatch 即插即用感知框架](https://huggingface.co/papers/2611.28947) ⭐️ 6.0/10

这篇 Hugging Face 每日论文（2026-11-25）介绍 NightWatch 即插即用框架，旨在解决视觉语言模型计算机使用代理（CUA）的感知-动作滞后问题。该框架通过耦合轻量级 NightWatch-0.8B 模型，为现有 CUA 提供连续时序感知，无需修改代理的模型、提示或动作空间。材料未提供性能对比或具体评测数据。

rss · Hugging Face Daily Papers · 11月25日 00:00

**「为什么重要」** 该框架针对 VLM 推理延迟与动态界面导致的感知 stale 问题，提供了一种不侵入现有代理架构的补丁方案。对正在开发或维护 CUA 的工程师而言，这可能降低集成环境感知模块的门槛。但缺少量化结果，实际效果待验证。

**「可关注」** 可关注：NightWatch 以独立轻量模型耦合主代理的设计，可能为现有 CUA 系统增加时序感知能力提供低侵入路径。

**标签**: `#coding-agent`, `#harness`

---

<a id="item-agent-engineer-6"></a>
### [HF 热门：27B 三元量化 GGUF](https://huggingface.co/prism-ml/Ternary-Bonsai-2.5-27B-GGUF) ⭐️ 6.0/10

2026 年 11 月 25 日，Hugging Face 热门榜新增 prism-ml/Ternary-Bonsai-2.5-27B-GGUF 模型，trendingScore 达 133，获 140 个赞，为 27B 参数的 2-bit 三元量化 GGUF 格式文本生成模型，适配 llama.cpp，支持 CUDA、Metal 端侧部署，面向低资源本地 LLM 部署场景；当前公开信息未披露性能指标、技术实现细节与实际用例验证，模型实际可用性需进一步评估。

rss · Hugging Face Trending Models · 11月25日 05:11

**「为什么重要」** 该模型作为高热度量化端侧模型进入 HF 热门榜，为低资源本地 LLM 部署（含 coding agent 本地运行场景）提供了新的量化方案参考；但目前公开信息不足，实际推理性能、精度损失与落地可行性尚未得到验证。

**「可关注」** 可关注：该 2-bit 三元量化 27B GGUF 模型在 llama.cpp 上的端侧推理吞吐、显存占用与精度表现，可对照现有同参数量级量化方案评估本地部署价值。

**标签**: `#coding-agent`, `#quantization`, `#on-device-inference`

---

<a id="item-agent-engineer-7"></a>
### [HF 日报：Loom Attention 与 LoomFormer](https://huggingface.co/papers/2611.30634) ⭐️ 5.5/10

2026 年 11 月 25 日，Hugging Face Daily Papers 发布论文摘要，提出 Loom Attention 与 LoomFormer 架构。该架构采用双流设计，以每 token 矩阵记忆作为第二残差流，通过交织垂直注意力（基于归一化门控线性注意力访问矩阵记忆）与水平注意力，实现 Transformer 每 token 动态重连电路。论文声称该架构在语言建模和下游任务中，可匹配 3 倍计算量训练的常规 Transformer，以及 HC/mHC、MUDDFormer、AttnRe 等近期残差流基线。当前公开内容仅为不完整摘要片段，无实现细节、开源代码、面向 Agent 任务的评测结果，来源为二手聚合内容，无官方论文仓库、作者博客等一手链接，对 Agent 工程师短期可行动价值有限。

rss · Hugging Face Daily Papers · 11月25日 00:00

**「为什么重要」** 该工作为高效 Transformer 架构设计提供了新的双流矩阵记忆思路，属于架构层面的新颖探索；但其对 Agent 场景的实际增益、实现成本、可复现性均未得到验证，短期无法直接落地到 coding agent 相关开发中。

**「可关注」** 可关注：后续若公开完整论文、开源实现及 Agent 场景评测结果，可再评估该架构对 coding agent 推理效率的实际提升空间。

**标签**: `#memory`

---

## AI 日报
{: #sec-ai-daily .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-daily" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-daily-1"></a>
### [GPT-6 展示内在蛋白质设计能力](https://openai.com/index/gpt-6-models-demonstrate-intrinsic-protein-design-capabilities) ⭐️ 8.8/10

OpenAI 官方博客于 2026 年 11 月 24 日宣布，GPT-6 模型具备内在蛋白质设计能力，可通过推理与代码完成蛋白质结构、序列设计。实验室测试证实其对 5 个靶点存在结合活性。

rss · OpenAI Blog · 11月24日 13:00

**「为什么重要」** 这是大语言模型蛋白质设计能力首次获得官方公布的实验室验证，拓展了 AI 在生物计算领域的应用场景。

**「可关注」** 可关注：GPT-6 通过推理与代码完成蛋白质设计的技术路径，以及其 5 个靶点结合活性的实验室验证结果。

**标签**: `#model`, `#lab`, `#industry`

---

<a id="item-ai-daily-2"></a>
### [Codex 与 Astra 辅助发现潜在系外行星](https://openai.com/index/searching-for-distant-planets-with-astra) ⭐️ 6.8/10

OpenAI 官方博客 2026 年 11 月 24 日发布应用案例，两名业余天文学家使用 Codex 和 Astra 工具分析 NASA 开普勒与 TESS 望远镜的公开数据，发现潜在系外行星。

rss · OpenAI Blog · 11月24日 11:00

**标签**: `#lab`, `#product`, `#industry`

---

<a id="item-ai-daily-3"></a>
### [LIBERO 登顶六项真机具身任务](https://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw==&amp;mid=2247948323&amp;idx=3&amp;sn=f554a3311a9945f2a61b4c13d2f3313c) ⭐️ 5.5/10

阿里达摩院、香港具身智能实验室等团队提出具身智能策略 RynnVLA-Latent，核心是用潜在动作作为共享监督接口，将 3.01 万小时异构人类视频转化为策略监督信号，先学习共享运动经验再适配具体机器人。基于该策略训练的 4B 模型 LIBERO 在六项真机任务中登顶，单任务成绩达 98.8%。该报道为二手科技媒体转载，正文截断，无对应官方一手公告链接，技术细节无法进一步核对。

rss · 量子位 · 11月24日 06:27

**「为什么重要」** 现有具身训练依赖昂贵的机器人示教数据，且不同硬件的动作空间难以统一。该策略尝试绕开原生控制标签需求，从海量人类视频中提取可跨硬件复用的运动经验，可能降低具身智能的训练数据门槛。

**「可关注」** 可关注：潜在动作表示结合残差式未来特征预测与三维场景流约束，可在无原生机器人控制标签条件下从人类视频学习运动经验。

**标签**: `#model`, `#lab`, `#industry`, `#eval`

---

## AI 羊毛
{: #sec-ai-deals .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-deals" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-deals-1"></a>
### [所以便签 SoYiNote 兑换码放送](https://www.v2ex.com/t/1259471#reply20) ⭐️ 7.0/10

V2EX 用户 W20NY 分享自制拟物风格 iOS 便签应用「所以便签（SoYiNote）」，放出 20 个终身会员兑换码，按原帖楼层每 5 楼赠送 1 个。

rss · V2EX Hot · 11月24日 07:43

**「可关注」** 可关注：该兑换码仅通过 V2EX 原帖楼层活动发放，无其他公开领取渠道，需在对应帖子下参与互动按规则领取。

**标签**: `#promo`, `#coupon`

---