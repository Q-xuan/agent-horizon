---
layout: default
title: "Horizon Summary: 2026-10-15 (ZH)"
date: 2026-10-15
lang: zh
---

> 从 216 条内容中筛选出 12 条重要资讯。

<nav id="ah-toc" class="ah-toc" aria-label="目录"><span class="ah-toc-title">目录</span><ul><li><a href="#sec-harness-arch"><span class="ah-toc-name">Harness 架构</span><span class="ah-toc-count">3条</span></a></li><li><a href="#sec-agent-engineer"><span class="ah-toc-name">Agent 工程师日报</span><span class="ah-toc-count">4条</span></a></li><li><a href="#sec-ai-daily"><span class="ah-toc-name">AI 日报</span><span class="ah-toc-count">2条</span></a></li><li><a href="#sec-ai-deals"><span class="ah-toc-name">AI 羊毛</span><span class="ah-toc-count">3条</span></a></li></ul></nav>

---

**[Harness 架构](#sec-harness-arch)**
1. [@mastra/core 1.77.0 发布](#item-harness-arch-1) ⭐️ 8.8/10
2. [Agent Framework 1.25.0](#item-harness-arch-2) ⭐️ 7.8/10
3. [Graphiti v0.31.0 发布](#item-harness-arch-3) ⭐️ 6.8/10

**[Agent 工程师日报](#sec-agent-engineer)**
1. [CoSIR 多智能体协作训练论文](#item-agent-engineer-1) ⭐️ 7.0/10
2. [Agent-Reflex 论文提出三阶段反思训练框架](#item-agent-engineer-2) ⭐️ 7.0/10
3. [Tev-Gym 开源长时程智能体训练数据集](#item-agent-engineer-3) ⭐️ 7.0/10
4. [Harness^2 提出递归 Agent Harnessing 框架](#item-agent-engineer-4) ⭐️ 7.0/10

**[AI 日报](#sec-ai-daily)**
1. [Block 用 OpenAI 做 AI 安全](#item-ai-daily-1) ⭐️ 6.8/10
2. [SentinelOne 用 Daybreak 将恶意软件分析缩至数小时](#item-ai-daily-2) ⭐️ 5.8/10

**[AI 羊毛](#sec-ai-deals)**
1. [Petal 开源结对工具发布](#item-ai-deals-1) ⭐️ 9.0/10
2. [Show HN 免费远程工作 API 上线](#item-ai-deals-2) ⭐️ 6.0/10
3. [gopuzzlego 免费拼图生成工具](#item-ai-deals-3) ⭐️ 5.0/10

---

## Harness 架构
{: #sec-harness-arch .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-harness-arch" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-harness-arch-1"></a>
### [@mastra/core 1.77.0 发布](https://github.com/mastra-ai/mastra/releases/tag/%40mastra/core%401.77.0) ⭐️ 8.8/10

Mastra Core 1.77.0 引入 \`FactorySandbox\` provider 合同，配套 Docker、E2B 与 Mastra Platform 实现，支持可调设置、仓库模板和预构建环境。Factory 支持提前构建模板和多仓库会话，通过 \`source\_control\_\*\` 工具跨仓库操作。durable agent 获得跨多种存储后端的 run fencing 保护，防止恢复运行覆盖状态。Observational Memory 增加 generation 保护与冲突感知写入，Span 与 MCP 追踪实现跨系统关联。

github · PaulieScanlon · 10月14日 08:29

**「设计要点」** 运行时通过 FactorySandbox 抽象统一沙箱生命周期，预构建模板降低冷启动；存储层在 Cloudflare D1、DynamoDB、MongoDB 等后端实现 durable execution 互斥恢复。记忆层引入 \`supersededBy\` 与冲突感知 API，可观测层通过 Span links 和 MCP 双向关联打通跨系统追踪。

**「改了什么」** 新增 FactorySandbox 合同及 Docker/E2B/Platform 实现，支持预构建环境与多仓库会话；durable agent 获得跨存储后端的 run fencing。Observational Memory 修复并发覆盖，Span 与 MCP 实现跨系统关联。Breaking changes 包括 \`@mastra/server\` workflow HTTP routes 返回 404、session 与 pending item API 弃用，以及 \`@mastra/playground-ui\` 组件控制方式变更。

**标签**: `#sandbox`, `#tools`, `#runtime`, `#memory`

---

<a id="item-harness-arch-2"></a>
### [Agent Framework 1.25.0](https://github.com/microsoft/agent-framework/releases/tag/dotnet-1.25.0) ⭐️ 7.8/10

Microsoft Agent Framework .NET 1.25.0 发布，A2A 协议升级至 1.0.0-preview3。工具审批层新增超时自动拒绝与复用逻辑，SSE 流终止改为 data: \[DONE\] 标记。运行时修复子代理 handoff 回弹与推理残留，Purview 检查扩展引用与错误详情。Cosmos 聊天元数据与分区键策略解耦（BREAKING）。

github · dmytrostruk · 10月14日 19:10

**「设计要点」** 运行时层集中处理工具审批超时与子代理 handoff 逻辑；Purview 合规检查扩展至引用与错误链路；Cosmos 存储层引入分区键策略解耦，影响现有数据布局。

**「改了什么」** 工具审批增加超时自动拒绝与复用机制；A2A 协议升级至 1.0.0-preview3；SSE 流终止改为 data: \[DONE\]；修复子代理 handoff 回弹与推理残留；Purview 检查纳入引用与错误详情；Cosmos 聊天元数据与分区键策略解耦（BREAKING）。

**标签**: `#runtime`, `#tools`, `#permissions`, `#subagents`, `#planning`

---

<a id="item-harness-arch-3"></a>
### [Graphiti v0.31.0 发布](https://github.com/getzep/graphiti/releases/tag/v0.31.0) ⭐️ 6.8/10

Graphiti v0.31.0 正式发布，核心技术变更包括将 MCP 服务端升级至 MCP SDK 2.x，新增基于 group\_id 的 MCP 工具路由能力，同时引入 LLMRuntime 组件实现提示词与模型的动态路由，配套多项依赖安全更新与功能修复。

github · pevans · 10月14日 23:58

**「设计要点」** MCP 服务端底层协议栈升级至 MCP SDK 2.x，工具路由层新增按请求携带的 group\_id 匹配目标知识图谱的逻辑；新增 LLMRuntime 统一处理提示词分发与模型选择。

**「改了什么」** MCP 服务端升级至 SDK 2.x，MCP 工具支持按请求携带的 group\_id 路由到对应知识图谱；新增 LLMRuntime 实现提示词与模型动态路由；修复 FalkorDB 6.x 节点全文索引 DDL 创建问题，默认组合提取提示词切换为 C2 版本，OpenAI 默认调用模型调整为 gpt-6-luna 并关闭提示词缓存；多项依赖升级修复安全告警。

**标签**: `#mcp`, `#tools`, `#runtime`

---

## Agent 工程师日报
{: #sec-agent-engineer .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-agent-engineer" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-agent-engineer-1"></a>
### [CoSIR 多智能体协作训练论文](https://huggingface.co/papers/2610.17893) ⭐️ 7.0/10

Hugging Face Daily Papers 于 2026-10-15 收录论文 arXiv:2610.17893，提出 CoSIR 后训练方法。该方法用简单可验证环境，通过基于惊讶度的信息奖励与贝叶斯评估器训练 LLM 智能体协作。贝叶斯评估器以团队惊讶度（各智能体对正确选项负对数概率之和的降低）评分共享信息。论文声称该方法可泛化至未见任务，但属研究阶段成果，非生产级发布，且摘要中方法描述存在截断。

rss · Hugging Face Daily Papers · 10月15日 00:00

**「为什么重要」** 该研究针对多智能体协作中最终任务反馈稀疏的痛点，提出可验证奖励 shaping 思路。若复现成功，可为编排设计提供新训练范式，但目前仅为论文提案，尚未有生产级验证或社区复现报告。

**「可关注」** 可关注：CoSIR 以团队惊讶度降低作为可验证信号，为稀疏反馈下的多智能体后训练提供了一种 reward shaping 思路，但该成果尚未经过生产级验证。

**标签**: `#orchestration`, `#eval`

---

<a id="item-agent-engineer-2"></a>
### [Agent-Reflex 论文提出三阶段反思训练框架](https://huggingface.co/papers/2610.17953) ⭐️ 7.0/10

Hugging Face Daily Papers 于 2026-10-15 介绍 Agent-Reflex 论文，提出一个三阶段训练框架，用于教 LLM agent 在长期任务执行中主动反思。第一阶段 Environment Reflection Skill Discovery \(RSD\) 向环境扩展中注入工具反馈扰动，从能力多样化的 LLM 池中采样，挖掘匹配的成功-失败对，并总结可复用的反思元技能。该框架直接针对 MCP 工具服务返回噪声反馈及用户中途纠正的部署痛点。当前材料为截断版本，未披露完整技术细节、性能指标或消融实验结果。

rss · Hugging Face Daily Papers · 10月15日 01:51

**「为什么重要」** 该研究直击 coding agent 部署中的高优先级可靠性问题：MCP 工具反馈噪声、用户干预和失败恢复。对正在设计 agent harness 或评估系统的工程师而言，提出的反思元技能提取方法可能为提升长期任务成功率提供新思路。但论文完整实验验证尚未公开，实际效果待确认。

**「可关注」** 可关注：RSD 阶段通过向环境扩展注入受控扰动，从多样化 LLM 池中挖掘成功-失败对来构建反思技能库的方法，这可能为现有 agent 训练数据构造提供新范式。

**标签**: `#coding-agent`, `#mcp`, `#harness`, `#eval`

---

<a id="item-agent-engineer-3"></a>
### [Tev-Gym 开源长时程智能体训练数据集](https://huggingface.co/papers/2610.18868) ⭐️ 7.0/10

2026-10-15，Hugging Face Daily Papers 发布论文，介绍 Tev-Gym。这是首个具备可验证密集渐进奖励的长时程智能体训练数据集，包含 1,170 个经人工验证的任务环境，覆盖 7 个领域。数据集采用 latent-world-first 方法构建，先建立领域完整且正确的隐式规范，再生成可验证环境。该工作针对长时程智能体开发中训练数据稀缺与奖励稀疏两大核心瓶颈，为 eval、coding-agent 和 harness 方向提供新的训练与评估资源。

rss · Hugging Face Daily Papers · 10月15日 01:51

**「为什么重要」** 长时程智能体（数小时至数天自主执行经济价值任务）是自动化发现与递归自我改进（RSI）的关键能力，但开源模型在此类任务上表现挣扎。Tev-Gym 通过可验证的密集渐进奖励机制，首次为长时程 agent 训练提供了规模化、可验证的数据基础，可能改变当前依赖稀疏奖励或人工标注的现状。

**「可关注」** 可关注：Tev-Gym 的 latent-world-first 构建流程与 1,170 个跨 7 域验证环境，为长时程 agent 的训练数据构造提供了可复用的工程范式，其密集渐进奖励设计可直接用于现有 coding-agent 和 harness 的评估指标优化。

**标签**: `#eval`, `#coding-agent`, `#harness`

---

<a id="item-agent-engineer-4"></a>
### [Harness^2 提出递归 Agent Harnessing 框架](https://huggingface.co/papers/2610.14224) ⭐️ 7.0/10

Hugging Face Daily Papers 于 2026-10-15 收录论文《Harness^2: Recursive Agent Harnessing for an Open World》。该论文提出 Harness^2，一个即插即用递归 agent harnessing 框架，针对开放世界环境中递归自我改进（RSI）的两项关键限制：测试时任务新颖导致缺乏真实值验证器，以及 RSI 过程高度任务特定、难以泛化。框架通过两层相互关联的递归层级解决上述问题，但摘要片段未完整披露第二层递归的具体机制。当前仅能确认框架设计方向，完整技术实现、性能数据及对比基线尚未披露。

rss · Hugging Face Daily Papers · 10月15日 01:51

**「为什么重要」** 该框架直接针对 agent harness 与编排设计的核心痛点——如何在无真实验证器的开放任务中实现 harness 的自动演化与泛化。对正在设计递归改进或在线演化机制的工程师有直接参考价值，但具体效果需等待全文验证。

**「可关注」** 可关注：Harness^2 尝试用双层递归分离任务特定改进与通用 harness 演化，这可能是解决开放世界无验证器场景下在线 harness 编辑的一个方向。但需注意当前仅披露摘要，具体算法与效果待验证。

**标签**: `#harness`, `#orchestration`, `#eval`

---

## AI 日报
{: #sec-ai-daily .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-daily" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-daily-1"></a>
### [Block 用 OpenAI 做 AI 安全](https://openai.com/index/block-ai-powered-security) ⭐️ 6.8/10

OpenAI 官方博客发布消息，Block 正采用 OpenAI 技术构建 AI 驱动的安全能力，其安全团队可更快开展威胁调查，并在数分钟内提出补丁方案。

rss · OpenAI Blog · 10月14日 07:00

**「为什么重要」** 这是 OpenAI 技术在企业安全运营场景的落地用例，为 AI 安全工具开发、安全自动化流程设计提供了可参考的行业实践。

**「可关注」** 可关注：OpenAI 技术在企业安全运营场景的落地实践，尤其是威胁调查与补丁生成的自动化流程。

**标签**: `#industry`, `#product`, `#lab`

---

<a id="item-ai-daily-2"></a>
### [SentinelOne 用 Daybreak 将恶意软件分析缩至数小时](https://openai.com/index/sentinelone) ⭐️ 5.8/10

OpenAI 官方博客披露，网络安全公司 SentinelOne 接入 OpenAI Daybreak 后，将恶意软件分析耗时从数周压缩至数小时，可调查的威胁总量得到提升。当前公开信息未披露具体技术路径、量化指标及更广泛的行业影响。

rss · OpenAI Blog · 10月14日 12:00

**「可关注」** 可关注：OpenAI Daybreak 在恶意软件分析场景的效率提升实践。

**标签**: `#industry`, `#product`

---

## AI 羊毛
{: #sec-ai-deals .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-deals" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-deals-1"></a>
### [Petal 开源结对工具发布](https://petal.live/) ⭐️ 9.0/10

CoScreen 原团队成员 Jason Thomas 等人发布开源免费结对编程工具 Petal，替代 2026 年 7 月 31 日 Datadog 关停的 CoScreen 服务，无付费、绑卡等使用限制，用户可通过官方 GitHub 仓库和官网直接获取使用。工具当前支持 macOS、Windows 及网页端，Linux 版本后续开发，媒体流基于 LiveKit 传输，支持使用官方托管实例或通过 docker-compose 自托管部署。其首版仅用 8 周、借助 Fable 和 Astra 等前沿模型从零构建，开发周期远短于此前 CoScreen 的近 6 年。

rss · HN Free API / Credits · 10月14日 18:23

**「为什么重要」** 此前 Screenhero、CoScreen、Around 等同类结对工具均因收购后终止服务，Petal 采用开源免费模式，即使开发团队停止维护，用户也可自行托管或 fork 代码，避免服务再次被关停。

**「可关注」** 可关注：Petal 支持通过 docker-compose 自托管，可对接自有 LiveKit 服务器或替换其他视频后端，适合对音视频数据留内网有需求的团队。

**标签**: `#free-tier`, `#open-source`, `#developer-tool`

---

<a id="item-ai-deals-2"></a>
### [Show HN 免费远程工作 API 上线](https://remote-jobs-api.tten.no/) ⭐️ 6.0/10

Show HN 用户 earnnovadev 发布免费无认证远程工作 API，提供 63 万条覆盖 16 个招聘板的实时职位列表，未公开使用限制、有效期，无领取门槛，截止时间未披露。

rss · HN Free API / Credits · 10月14日 08:04

**「为什么重要」** 该 API 无需认证即可调用，可快速获取多平台远程职位数据，目前未披露调用限制与有效期，适合轻量集成需求，但项目尚未经过社区验证，稳定性待观察。

**「可关注」** 可关注：该 API 为未经验证的个人项目，未公开调用频率、数据更新周期等限制，集成前需自行验证数据合规性与稳定性。

**标签**: `#api`, `#free-tier`

---

<a id="item-ai-deals-3"></a>
### [gopuzzlego 免费拼图生成工具](https://gopuzzlego.com/generator) ⭐️ 5.0/10

由 alixai 分享的 gopuzzlego 免费拼图生成工具，支持导出 SVG、PDF、STL 三种格式，拼图块采用 Voronoi 算法生成，无需注册账号即可直接使用，目前无明确使用限制。

rss · HN Free API / Credits · 10月14日 11:02

**「为什么重要」** 对于需要定制拼图素材的用户，该工具省去了注册账号的步骤，可直接导出适配手工制作、3D 打印、教学演示等场景的多格式文件，使用门槛极低。

**「可关注」** 可关注：该工具无需账号、无明确使用限制，支持直接导出多格式 Voronoi 拼图文件，适合快速生成定制化拼图素材。

**标签**: `#free-tier`, `#no-account`, `#utility`

---