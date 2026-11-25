---
layout: default
title: "Horizon Summary: 2026-11-25 (ZH)"
date: 2026-11-25
lang: zh
---

> 从 193 条内容中筛选出 12 条重要资讯。

<nav id="ah-toc" class="ah-toc" aria-label="目录"><span class="ah-toc-title">目录</span><ul><li><a href="#sec-harness-arch"><span class="ah-toc-name">Harness 架构</span><span class="ah-toc-count">3条</span></a></li><li><a href="#sec-agent-engineer"><span class="ah-toc-name">Agent 工程师日报</span><span class="ah-toc-count">5条</span></a></li><li><a href="#sec-ai-daily"><span class="ah-toc-name">AI 日报</span><span class="ah-toc-count">3条</span></a></li><li><a href="#sec-ai-deals"><span class="ah-toc-name">AI 羊毛</span><span class="ah-toc-count">1条</span></a></li></ul></nav>

---

**[Harness 架构](#sec-harness-arch)**
1. [Goose v1.61.0 发布](#item-harness-arch-1) ⭐️ 7.8/10
2. [pydantic-ai v2.74.0 发布](#item-harness-arch-2) ⭐️ 6.8/10
3. [fastmcp v4.2.6 发布](#item-harness-arch-3) ⭐️ 5.3/10

**[Agent 工程师日报](#sec-agent-engineer)**
1. [Cognition 发布 SWE-2.1 模型](#item-agent-engineer-1) ⭐️ 8.8/10
2. [LLM 12 个月三个能力拐点梳理](#item-agent-engineer-2) ⭐️ 7.0/10
3. [CUA-SEE 自进化评估框架提出](#item-agent-engineer-3) ⭐️ 7.0/10
4. [NightWatch 为 CUA 补连续时间感知](#item-agent-engineer-4) ⭐️ 6.0/10
5. [Microduck 避障 Sim2Real](#item-agent-engineer-5) ⭐️ 5.8/10

**[AI 日报](#sec-ai-daily)**
1. [GPT-6 模型具备蛋白质设计能力](#item-ai-daily-1) ⭐️ 7.8/10
2. [爱好者用 Codex、Astra 寻系外行星](#item-ai-daily-2) ⭐️ 7.8/10
3. [阿里达摩院具身策略登顶六项真机任务](#item-ai-daily-3) ⭐️ 5.5/10

**[AI 羊毛](#sec-ai-deals)**
1. [SoYiNote 终身会员兑换码放送](#item-ai-deals-1) ⭐️ 7.0/10

---

## Harness 架构
{: #sec-harness-arch .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-harness-arch" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-harness-arch-1"></a>
### [Goose v1.61.0 发布](https://github.com/aaif-goose/goose/releases/tag/v1.61.0) ⭐️ 7.8/10

block/goose v1.61.0 正式发布，引入 MCP 配置与扩展增强、goose-agent 上下文压缩、两种新的声明式 LLM 提供商，以及运行时首 token 时延（TTFT）测量修复。MCP 层面新增 ACP 协议下 header secrecy、server.json 格式导入，以及 goose-agent 的 MCP extension operation。上下文压缩通过 Compaction operation 实现，支持丢弃 Claude 模型拒绝的 &lt;analysis&gt; scratchpad。新增 llmman（Ollama 兼容）和 amazee.ai 声明式提供商，Gemini 4 Neon 加入模型目录。

github · github-actions\[bot\] · 11月25日 03:31

**「设计要点」** goose-agent 新增 MCP extension 与 Compaction 两种 operation，分别扩展工具调用边界和实现上下文压缩。声明式 LLM provider 机制（llmman、amazee.ai）将提供商配置迁移到配置驱动，MCP 集成通过 ACP 统一 header secrecy 并支持导入 server.json。

**「改了什么」** goose-agent 新增 MCP extension 与 Compaction operation，分别扩展工具调用和实现上下文压缩。MCP 配置支持导入 server.json 并在 ACP 下统一处理 header secrecy，新增 llmman 与 amazee.ai 声明式提供商，修复 TTFT 测量逻辑，工具审批改为可选。

**标签**: `#mcp`, `#memory`, `#runtime`

---

<a id="item-harness-arch-2"></a>
### [pydantic-ai v2.74.0 发布](https://github.com/pydantic/pydantic-ai/releases/tag/v2.74.0) ⭐️ 6.8/10

pydantic-ai v2.74.0 与 pydantic-ai-harness 0.74.0 发布，包含 6 项中危安全修复。PlaywrightBrowser 修复 5 个 SSRF/沙箱绕过漏洞，覆盖 IPv6 site-local 地址、NAT64/ISATAP 嵌入、反斜杠 URL 解析错误及 WebRTC 等出口策略遗漏。新增 computer use 全链路支持，包括 ComputerTool 核心契约、ComputerUse 能力、Display 协议，以及 DockerContainer、DaytonaSandbox 等 11 种 Sandbox 的 desktop 模式。兼容性变更包括 GPT-6.2 静态指令缓存策略调整、Gemini streaming 使用量统计逻辑变更，以及 ElevenLabs 和 pydantic-evals 的 OpenTelemetry 敏感数据泄露修复。

github · dsfaccini · 11月24日 23:22

**「设计要点」** PlaywrightBrowser 默认启用强制出口策略，通过禁用 RTCPeerConnection、WebTransport、WebSocketStream 和 FedCM API 实现网络隔离。Computer use 架构新增 ComputerTool 核心契约、ComputerUse 能力及 Display 协议，支持多 Sandbox 桌面模式。OpenTelemetry instrumentation 在实时会话和在线评估中分别处理敏感字段和 baggage 属性，避免跨上下文污染。

**「改了什么」** PlaywrightBrowser 修复 5 个中危 SSRF/沙箱绕过漏洞，包括 IPv6 私有地址绕过、NAT64/ISATAP 嵌入、反斜杠 URL 解析错误及 WebRTC 等出口策略遗漏，并收紧 OpenTelemetry 敏感数据记录。新增 computer use 全链路支持，涵盖 ComputerTool 核心契约、ComputerUse 能力、Display 协议及 11 种 Sandbox 的 desktop 模式。GPT-6.2 静态指令缓存策略调整，Gemini streaming 使用量统计逻辑变更，pydantic-evals 修复 OpenTelemetry baggage 属性污染。

**标签**: `#tools`, `#sandbox`, `#permissions`

---

<a id="item-harness-arch-3"></a>
### [fastmcp v4.2.6 发布](https://github.com/PrefectHQ/fastmcp/releases/tag/v4.2.6) ⭐️ 5.3/10

fastmcp v4.2.6 发布。本次版本新增实验性 CodeModeClient，可在客户端侧执行 CodeMode，为原生不支持 CodeMode 的 MCP 服务器提供 search、schema 和 execute 元工具，并支持单个 execute 块跨服务器链式调用工具。服务端 span 新增 network.transport 属性，HTTP 传输下还携带 network.protocol.name 和 network.protocol.version。同时移除 Authlib 依赖，并将实验性事件系统拆分为独立包 fastmcp-events，事件类型改为 Pydantic 模型，支持通过 DocketEventLog 持久化到 Redis。

github · github-actions\[bot\] · 11月25日 00:40

**「设计要点」** fastmcp 运行于 asyncio，采用客户端-服务器架构。服务端 span 暴露网络传输层属性，支持可观测性。事件系统支持通过 Docket 将事件日志持久化到 Redis，实现跨副本分发和重启恢复。

**「改了什么」** 新增实验性 CodeModeClient，支持客户端侧元工具和跨服务器工具链。移除 Authlib 依赖，客户端和服务器不再使用该包。实验性事件拆分为 fastmcp-events 独立包，API 从 check 函数改为 Pydantic 模型加 reader 模式，支持 for\_subscription 方法。

**标签**: `#mcp`, `#tools`, `#runtime`, `#experimental`, `#breaking-change`

---

## Agent 工程师日报
{: #sec-agent-engineer .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-agent-engineer" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-agent-engineer-1"></a>
### [Cognition 发布 SWE-2.1 模型](https://cognition.ai/blog/swe-2-1) ⭐️ 8.8/10

2026 年 11 月 24 日 Cognition AI 发布 SWE-2.1，为 SWE-2 的重大升级版本，基于 Kimi K3 采用纯强化学习训练。相比 SWE-2，其在 FrontierCode 2.0、Terminal-Bench 4.1 等基准测试有显著提升，网络安全方向得分基于 Muse Wonder Full 配置，达到 ExploitBench 80%得分、ExploitGym 27.3%旗标捕获率，且测试时计算随 rollout 时长对数线性提升。训练过程中配套红队测试、持续安全监控与沙箱逃逸 canary 评估，累计发现 4 次训练环境沙箱新漏洞并即时响应。官方同步推出面向防御场景的 SWE-2.1 Cyber 版本（已集成至 Devin Security），以及与 Cerebras 合作实现 10 倍推理加速的 SWE-2.1 Ultrafast 版本，前者面向合法防御工作调整护栏策略，后者免费至 2026 年 12 月 8 日，全版本折扣价截至 2026 年 1 月 30 日。

rss · Cognition Blog · 11月24日 16:00

**「为什么重要」** SWE-2.1 首次将纯强化学习训练的长时程自主工作流能力同时落地到软件工程和网络安全场景，且配套了分版本的安全护栏策略，为 coding agent 的能力边界和安全治理提供了新的参考。其对下游开发工具的实际效率提升效果、护栏策略对合法防御工作的实际影响尚未有公开验证。

**「可关注」** 可关注：SWE-2.1 通过降低训练时 rollout 长度振荡，实现了从分钟级到小时级任务的稳定训练，同时测试时计算随时长对数线性提升，且配套 10 倍推理加速版本适配紧急场景的时效需求。

**标签**: `#coding-agent`, `#eval`, `#orchestration`

---

<a id="item-agent-engineer-2"></a>
### [LLM 12 个月三个能力拐点梳理](https://simonwillison.net/2026/Nov/24/llm-inflection-points/) ⭐️ 7.0/10

2026 年 11 月 24 日，Simon Willison 在 AI Engineer Code Summit 主题演讲中回顾过去 12 个月 LLM 与 coding agent 的能力变化，提出三个关键拐点，锚定 2025 年 11 月 24 日发布的 Claude Opus 4.5 为起点。第一拐点为 2025 年 11 月 Opus 4.5、GPT-5.1 Instant/Thinking/Codex/Codex-Max 系列模型发布，其中 Opus 4.5 是 Simon Willison 使用的第一个能让 Claude Code 默认结果大多正确的模型，此前他因需要频繁修正而未将其作为日常开发工具，该模型发布后 Claude Code、OpenAI Codex 等 coding agent 从不够可靠变为日常开发可用工具。第二拐点为 2026 年 6 月 Claude Fable 5 发布，其作为「去危险化」的 Claude Mythos，在给定明确目标和必要工具时可通过 brute force 解决复杂问题，但发布三天后被美国出口管制，直到 7 月 1 日才恢复可用。第三拐点为 2026 年 9-10 月前沿模型 3D 建模与游戏开发能力大幅提升，Claude Opus 5.5 甚至能通过 12 小时 playtest 优化游戏可玩性。该总结为一线实践者的个人 retrospective，未附官方 benchmark，主要影响 coding agent 工程师与 AI 工具使用者。

rss · Simon Willison · 11月24日 23:02

**「为什么重要」** 这份 retrospective 来自长期深度使用 coding agent 的一线实践者，其总结的三个拐点直接对应 agent 可靠性与能力边界的实际变化，可用来校准团队对前沿模型能力的预期，避免被官方宣传误导。

**「可关注」** 可关注：前沿模型已出现「给定明确目标与必要工具即可 brute force 解决问题」的能力档位，同时 3D 空间建模能力的提升可能同步利好机器人视觉场景的 agent 开发。

**标签**: `#coding-agent`, `#llm`, `#agent-engineering`, `#inflection-points`

---

<a id="item-agent-engineer-3"></a>
### [CUA-SEE 自进化评估框架提出](https://huggingface.co/papers/2611.30962) ⭐️ 7.0/10

2026 年 11 月 25 日，Hugging Face Daily Papers 收录论文提出 CUA-SEE，一种面向计算机使用代理的闭环自进化评估环境。该框架通过共同演化评估任务与可执行验证器，解决传统静态基准因固定难度上限、有限特征覆盖与粗略聚合分数导致的判别力衰退问题。CUA-SEE 将演化目标解耦为基准演化、诊断演化与验证器演化三部分，分别扩展评估范围、提升能力边界探测分辨率、以及将变化需求转化为状态锚定的检查点。当前摘要内容被截断，完整技术细节与实验结果尚未披露。

rss · Hugging Face Daily Papers · 11月25日 00:00

**「为什么重要」** 该框架直接针对 coding agent 与计算机使用代理评测体系的核心痛点——静态基准随代理能力提升而快速贬值。若其共同演化机制与可执行验证器设计在后续完整论文中得到验证，可能为 eval harness 设计提供新的范式参考。

**「可关注」** 可关注：静态基准的判别力衰减问题已获明确，闭环自进化评估中任务与验证器的共同演化机制值得在 harness 设计中验证其工程可行性。

**标签**: `#eval`, `#coding-agent`, `#harness`

---

<a id="item-agent-engineer-4"></a>
### [NightWatch 为 CUA 补连续时间感知](https://huggingface.co/papers/2611.28947) ⭐️ 6.0/10

2026 年 11 月 25 日 Hugging Face 每日论文收录 arXiv 论文 2611.28947，提出即插即用框架 NightWatch，针对基于视觉语言模型的计算机使用代理（CUA）的感知陈旧问题，通过搭配轻量辅助模型 NightWatch-0.8B 为其增加连续时间感知能力，无需修改 CUA 原有模型、提示词或动作空间。该框架面向构建 UI 交互代理（含编码代理）的工程师，但当前提供的材料为截断版本，缺少完整技术细节、性能基准、代码发布信息与评估结果，实际落地效用暂无法完全评估。

rss · Hugging Face Daily Papers · 11月25日 00:00

**「为什么重要」** 该框架针对 VLM 推理延迟与动态界面叠加导致的感知-动作间隙这一实际痛点，提出无需改动现有 CUA 核心组件的补丁方案，对构建 UI 交互代理的工程师有参考价值。但当前缺乏完整性能数据与开源信息，其实际效果尚未得到验证。

**「可关注」** 可关注：NightWatch 采用即插即用设计，无需修改现有 CUA 的核心模型、提示词与动作空间即可补充连续时间感知能力，但需等待完整技术细节与评估结果发布后再判断落地可行性。

**标签**: `#coding-agent`, `#harness`

---

<a id="item-agent-engineer-5"></a>
### [Microduck 避障 Sim2Real](https://huggingface.co/blog/nvidia/microduck-obstacle-avoidance) ⭐️ 5.8/10

2026 年 11 月 24 日 Hugging Face 官方博客发布 Microduck 四足机器人 Sim2Real 避障控制器开发教程，基于 Isaac Lab exp/microduck 分支与 Newton 物理引擎实现。教程复用已训练好的固定行走策略，单独训练基于 ToF 传感的避障控制器，模拟 VL53L5CX 传感器（8×8 网格、15Hz 更新率、45°视场角、0.12-4m 量程），支持在 16384 个并行仿真环境用 PPO 训练 1500 轮，也可在 NVIDIA DGX Spark 上用 4096 环境跑 3000 轮完成训练。流程覆盖仿真训练、评估、ONNX 导出与真机部署，依赖 SimReady Central pinned 版本资产（commit 9d4556bfe80868c1d27a7a7ba1c2774e63e8cedd）构建随机化障碍场地。该教程仅面向 Microduck 硬件与 Isaac Lab 工具链开发者，对通用 AI Agent 工程师无直接参考价值。

rss · Hugging Face Blog · 11月24日 16:34

**「为什么重要」** 该教程完整公开了特定四足机器人的 Sim2Real 避障控制全链路工程实现，包括传感器建模、并行训练与真机部署的细节，为同类具身智能机器人项目提供了可复用的工具链参考。

**「可关注」** 可关注：避障控制与底层行走策略解耦、冻结行走权重单独训练上层导航策略的设计，以及仿真传感器加入噪声、延迟、缺失测量以对齐真机数据分布的工程实践。

**标签**: `#eval`, `#simulation`, `#embodied-ai`

---

## AI 日报
{: #sec-ai-daily .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-daily" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-daily-1"></a>
### [GPT-6 模型具备蛋白质设计能力](https://openai.com/index/gpt-6-models-demonstrate-intrinsic-protein-design-capabilities) ⭐️ 7.8/10

OpenAI 官方博客称 GPT-6 模型可通过推理与代码设计蛋白质结构和序列，实验室测试在 5 个靶标上发现结合证据。该公告内容极简，未披露详细方法论、与既有蛋白质折叠模型的对比或具体差异。

rss · OpenAI Blog · 11月24日 13:00

**「为什么重要」** 若该能力属实，将拓展大模型在生物计算领域的应用边界；但当前披露信息不足，尚无法验证其实际突破程度。

**「可关注」** 可关注：后续公开的详细实验设计与性能对比数据，以验证该能力的实际水平。

**标签**: `#model`, `#lab`, `#industry`

---

<a id="item-ai-daily-2"></a>
### [爱好者用 Codex、Astra 寻系外行星](https://openai.com/index/searching-for-distant-planets-with-astra) ⭐️ 7.8/10

OpenAI 官方博客披露，两名业余天文学爱好者使用 Codex 与 Astra 工具，分析 NASA Kepler 与 TESS 空间望远镜的公开数据，识别出潜在系外行星候选。目前未披露具体识别到的候选数量及后续验证进展。

rss · OpenAI Blog · 11月24日 11:00

**「为什么重要」** 这验证了 Codex 与 Astra 在科研场景的可用性，为业余天文爱好者参与系外行星搜寻提供了低门槛工具路径。

**「可关注」** 可关注：公开科研数据集与 AI 工具结合的平民化科研场景拓展。

**标签**: `#lab`, `#product`, `#industry`

---

<a id="item-ai-daily-3"></a>
### [阿里达摩院具身策略登顶六项真机任务](https://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw==&amp;mid=2247948323&amp;idx=3&amp;sn=f554a3311a9945f2a61b4c13d2f3313c) ⭐️ 5.5/10

阿里达摩院等团队提出具身智能策略 RynnVLA-Latent，以潜在动作作为共享监督接口，将 3.01 万小时异构人类视频转化为策略训练信号，无需原生机器人控制标签。配套 4B 参数模型 LIBERO 在六项真机任务中登顶，单任务最高准确率达 98.8%。当前披露内容为二手科技媒体报道，未提供官方一手发布链接与完整技术细节。

rss · 量子位 · 11月24日 06:27

**「为什么重要」** 该工作针对人类视频缺乏机器人控制指令、跨硬件示教数据难以通用的行业痛点，采用共享运动学习+下游适配的路线降低具身智能训练门槛，其真机登顶结果对具身智能落地路径有参考价值。

**「可关注」** 可关注：潜在动作共享监督接口、残差式未来特征预测与三维几何约束的设计，为跨硬件具身策略训练提供了可复用的技术思路。

**标签**: `#model`, `#lab`, `#industry`, `#eval`

---

## AI 羊毛
{: #sec-ai-deals .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-deals" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-deals-1"></a>
### [SoYiNote 终身会员兑换码放送](https://www.v2ex.com/t/1259471#reply20) ⭐️ 7.0/10

开发者 W20NY 在 V2EX 分享自制拟物风格 iOS 便签 APP「所以便签（SoYiNote）」，放出 20 个终身会员兑换码，领取规则为每 5 楼赠送 1 个，材料未标注活动截止时间。

rss · V2EX Hot · 11月24日 07:43

**「为什么重要」** 该 APP 以拟物交互为核心特色，支持待办一键生成锁屏壁纸或长图，未来还将上线桌面小组件、锁屏实时活动与灵动岛功能，终身会员兑换码属于稀缺福利。

**「可关注」** 可关注：兑换码按 V2EX 帖子每 5 楼规则发放，需前往对应帖子楼层回复领取，仅适配 iOS 设备。

**标签**: `#promo`, `#coupon`, `#limited-free`

---