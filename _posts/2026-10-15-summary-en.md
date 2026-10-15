---
layout: default
title: "Horizon Summary: 2026-10-15 (EN)"
date: 2026-10-15
lang: en
---

> From 216 items, 12 important content pieces were selected

---

**Agent Harness Architecture**
1. [Mastra Core 1.77.0 发布](#item-harness-arch-1) ⭐️ 8.8/10
2. [Agent Framework 1.25.0](#item-harness-arch-2) ⭐️ 7.8/10
3. [Graphiti v0.31.0 发布](#item-harness-arch-3) ⭐️ 6.8/10

**AI Agent Engineer**
1. [HF 论文：CoSIR 多智能体训练](#item-agent-engineer-1) ⭐️ 7.0/10
2. [Agent-Reflex 三阶段反思训练框架提出](#item-agent-engineer-2) ⭐️ 7.0/10
3. [Tev-Gym 开源长时程 Agent 数据集](#item-agent-engineer-3) ⭐️ 7.0/10
4. [Harness^2: Recursive Agent Harnessing Framework](#item-agent-engineer-4) ⭐️ 7.0/10

**AI Daily**
1. [Block 用 OpenAI 技术构建 AI 安全](#item-ai-daily-1) ⭐️ 6.8/10
2. [SentinelOne 恶意软件分析耗时从周降至小时](#item-ai-daily-2) ⭐️ 5.8/10

**AI Deals**
1. [CoScreen 原团队开源 Petal 工具](#item-ai-deals-1) ⭐️ 9.0/10
2. [Show HN 免费远程工作 API 上线](#item-ai-deals-2) ⭐️ 6.0/10
3. [GoPuzzleGo 免费拼图生成器上线](#item-ai-deals-3) ⭐️ 5.0/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [Mastra Core 1.77.0 发布](https://github.com/mastra-ai/mastra/releases/tag/%40mastra/core%401.77.0) ⭐️ 8.8/10

Mastra Core 1.77.0 发布。新增 FactorySandbox 提供商契约，支持 Docker、E2B 和 Mastra Platform 三种实现，提供可调设置、仓库模板和预构建环境。Factory 支持多仓库会话管理和 source\_control\_\* 工具。Durable agent 跨 Cloudflare DO/D1、Convex、DynamoDB 等 11 种存储后端实现 run fencing，防止崩溃恢复后状态覆盖。观测记忆修复并发冲突，链路追踪新增 span links。

github · PaulieScanlon · Oct 14, 08:29

**「设计要点」** FactorySandbox 将沙箱配置、模板和构建生命周期抽象为 provider 接口，provider 包实现该契约即可接入 Factory。多存储适配器统一实现 run fencing 语义，Observational Memory 引入 generation 保护和冲突感知写入，保证分布式部署状态一致性。

**「改了什么」** AgentController 的 steer 和 followUp 方法新增文件附件支持，FactorySandbox 契约及 Docker、E2B、Mastra Platform 实现上线以支持预构建环境。Durable agent 在 Cloudflare DO/D1、Convex、DynamoDB 等 11 种存储后端启用 run fencing，@mastra/server 的 workflow HTTP 路由禁止启动内部工作流。

**Tags**: `#sandbox`, `#tools`, `#runtime`, `#memory`

---

<a id="item-harness-arch-2"></a>
### [Agent Framework 1.25.0](https://github.com/microsoft/agent-framework/releases/tag/dotnet-1.25.0) ⭐️ 7.8/10

Microsoft Agent Framework .NET 1.25.0 发布。A2A 协议升级至 1.0.0-preview3，工具审批新增超时自动拒绝与复用逻辑，SSE 流修复终止帧，Purview 检查纳入引用与错误详情，子代理流程修复推理残留与 handoff 回弹。包含 Cosmos 聊天元数据与分区键策略解耦的 breaking change。

github · dmytrostruk · Oct 14, 19:10

**「改了什么」** A2A 包升级至 1.0.0-preview3；未响应工具审批请求超时后自动拒绝并支持复用；SSE 流以 data: \[DONE\] 正确终止；Purview 检查包含引用与错误详情；修复子代理 handoff 回弹与推理残留；Cosmos 聊天元数据与分区键策略解耦（breaking）。

**Tags**: `#runtime`, `#tools`, `#permissions`, `#subagents`, `#planning`

---

<a id="item-harness-arch-3"></a>
### [Graphiti v0.31.0 发布](https://github.com/getzep/graphiti/releases/tag/v0.31.0) ⭐️ 6.8/10

getzep/graphiti v0.31.0 将 MCP server 升级至 SDK 2.x，并新增按 group\_id 路由 MCP 工具到对应图实例的能力。版本同时引入 LLMRuntime 实现 prompt 与模型动态路由，并将默认 OpenAI 模型切换为 gpt-6-luna、关闭 prompt caching。此外，C2 prompt 成为默认组合提取提示，FalkorDB 6.x 全文索引修复，以及多项依赖安全更新。

github · pevans · Oct 14, 23:58

**「设计要点」** MCP server 升级至 SDK 2.x 后，工具层协议与传输实现随之更新。group\_id 参数现在决定 MCP 工具路由到哪个图实例，实现多图隔离。LLMRuntime 将 prompt 模板与模型选择解耦，支持运行时动态路由。

**「改了什么」** MCP server 从 SDK 1.x 升级至 2.x；MCP 工具现在按请求的 group\_id 路由到对应图实例；新增 LLMRuntime 支持 prompt 和模型动态路由；默认 OpenAI 调用从 gpt-4.1-nano 改为 gpt-6-luna 并关闭 prompt caching；C2 prompt 成为默认组合提取提示；FalkorDB 6.x 全文索引改用 DDL 形式创建；升级 pyjwt、sentence-transformers、urllib3、tornado 等依赖修复安全通告。

**Tags**: `#mcp`, `#tools`, `#runtime`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [HF 论文：CoSIR 多智能体训练](https://huggingface.co/papers/2610.17893) ⭐️ 7.0/10

2026年10月15日Hugging Face每日论文收录多智能体LLM协作训练研究论文，提出CoSIR后训练方法。该方法采用可验证的基于惊讶度的信息奖励机制，搭配贝叶斯评估器以团队惊讶度下降幅度评估共享信息价值，解决多智能体协作中最终任务反馈稀疏的痛点。训练出的协作行为可泛化至未见过的复杂任务，当前属于研究阶段成果，非生产级发布。

rss · Hugging Face Daily Papers · Oct 15, 00:00

**「为什么重要」** 该研究针对多智能体LLM协作训练的核心反馈稀疏问题提出可验证的技术路径，为后续多智能体系统的训练方案与编排设计提供了研究层面的参考方向。

**「可关注」** 可关注：CoSIR通过可验证的信息奖励机制解决多智能体协作训练反馈稀疏问题，其贝叶斯评估器以团队惊讶度下降作为信息价值度量，为相关训练方案设计提供了可复现的研究参考。

**Tags**: `#orchestration`, `#eval`

---

<a id="item-agent-engineer-2"></a>
### [Agent-Reflex 三阶段反思训练框架提出](https://huggingface.co/papers/2610.17953) ⭐️ 7.0/10

2026-10-15，Hugging Face Daily Papers 收录论文《Agent-Reflex: Teaching Language Agents to Act Reflectively》，提出同名三阶段训练框架。该框架教 LLM agent 在长程任务中主动反思，以处理 noisy MCP 工具反馈与用户纠正。第一阶段 Environment Reflection Skill Discovery \(RSD\) 向环境注入工具反馈扰动，从多样化 LLM 池采样，挖掘成功-失败配对并总结可复用反思元技能；后续阶段内容在提供的摘要中被截断。研究面向 coding agent 与 harness 工程师，但完整技术细节、性能指标及开源计划尚未公开。

rss · Hugging Face Daily Papers · Oct 15, 01:51

**「为什么重要」** 该论文针对 agent 部署中的高优先级痛点——MCP 工具反馈噪声与用户干预后的恢复能力，为 harness 设计与评估系统提供新训练范式参考。目前仅见框架概述，尚无可验证的性能数据或实现代码。

**「可关注」** 可关注：RSD 阶段通过环境扰动自动挖掘成功-失败配对生成反思元技能的方法，可能为 agent 训练数据构造提供新思路。

**Tags**: `#coding-agent`, `#mcp`, `#harness`, `#eval`

---

<a id="item-agent-engineer-3"></a>
### [Tev-Gym 开源长时程 Agent 数据集](https://huggingface.co/papers/2610.18868) ⭐️ 7.0/10

Hugging Face Daily Papers 于 2026-10-15 介绍论文《Tev: Scaling Long-Horizon Agentic Environments with Dense Progress Rewards》，提出 Tev-Gym。这是首个开源长时程 agent 训练数据集，提供可验证的密集渐进奖励，包含 1,170 个经验证的任务环境，覆盖 7 个领域。该数据集采用 latent-world-first 方法构建，旨在解决长时程 agent 开发中训练数据稀缺与奖励稀疏的核心瓶颈。目前未公开具体模型性能提升数据或使用限制。

rss · Hugging Face Daily Papers · Oct 15, 01:51

**「为什么重要」** 长时程 agent 是自动化发现和递归自我改进（RSI ）的关键能力，而开源模型在此类任务上表现不佳，主要受限于数据与奖励机制。Tev-Gym 提供了可规模化的训练与评估基础设施，可能降低长时程 agent 的研究门槛。

**「可关注」** 可关注：Tev-Gym 的 latent-world-first 构建流程与密集奖励标注机制，可作为长时程 agent 训练数据集的工程模板，但需验证其任务环境在真实编码场景中的迁移效果。

**Tags**: `#eval`, `#coding-agent`, `#harness`

---

<a id="item-agent-engineer-4"></a>
### [Harness^2: Recursive Agent Harnessing Framework](https://huggingface.co/papers/2610.14224) ⭐️ 7.0/10

On 2026-10-15, Hugging Face Daily Papers featured the paper &\#x27;Harness^2: Recursive Agent Harnessing for an Open World,&\#x27; proposing a plug-and-play recursive agent harnessing framework. The framework addresses two critical challenges in deploying recursive self-improvement \(RSI\) for agent harnesses in open-world settings: \(1\) open-world tasks are typically unseen during harness design and novel at test time, leaving no ground-truth verifiers to reliably guide online harness edits; \(2\) RSI processes remain highly task-specific and fail to generalize to novel scenarios. It introduces two interconnected levels of recursion, where task-level recursion refines the current task&\#x27;s harness using a contrastive Propose... \(abstract truncated\). The work targets agent engineers working on harness and orchestration design. Full technical details, implementation, and performance data are not available for verification from the provided abstract snippet.

rss · Hugging Face Daily Papers · Oct 15, 01:51

**「Why It Matters」** The framework directly targets core bottlenecks in scaling agent harnesses for open-world environments, though the complete mechanism and empirical results remain undisclosed.

**「Engineer Takeaway」** Watch for: the separation of task-level recursion from contrastive verification, which may offer a new approach to online harness optimization without ground-truth verifiers.

**Tags**: `#harness`, `#orchestration`, `#eval`

---

## AI Daily

<a id="item-ai-daily-1"></a>
### [Block 用 OpenAI 技术构建 AI 安全](https://openai.com/index/block-ai-powered-security) ⭐️ 6.8/10

OpenAI 官方博客公布，Block 正在采用 OpenAI 技术构建 AI 驱动的安全能力。其安全团队的威胁调查与补丁提案耗时已缩短至分钟级。

rss · OpenAI Blog · Oct 14, 07:00

**「可关注」** 可关注：Block 基于 OpenAI 技术将安全威胁调查与补丁提案耗时压缩至分钟级。

**Tags**: `#industry`, `#product`, `#lab`

---

<a id="item-ai-daily-2"></a>
### [SentinelOne 恶意软件分析耗时从周降至小时](https://openai.com/index/sentinelone) ⭐️ 5.8/10

OpenAI 官方博客报道，网络安全公司 SentinelOne 使用 OpenAI Daybreak 将恶意软件分析时间从数周缩短至数小时，从而提升威胁调查容量。该报道仅一句话，未披露具体技术实现、量化指标或更广泛的行业影响。

rss · OpenAI Blog · Oct 14, 12:00

**Tags**: `#industry`, `#product`

---

## AI Deals

<a id="item-ai-deals-1"></a>
### [CoScreen 原团队开源 Petal 工具](https://petal.live/) ⭐️ 9.0/10

CoScreen 原团队成员 Jason Thomas 等人发布开源免费结对编程工具 Petal，替代已关停的 CoScreen 服务，无付费、绑卡等使用限制。用户可通过官方 GitHub 仓库 kiruna-labs/petal 或官网直接获取，支持 macOS、Windows 及网页端，Linux 版本后续上线；也可通过 docker-compose 自托管 LiveKit 服务端，将流量保留在内网。工具支持共享窗口以真实桌面窗口形式呈现，可移动调整大小，多人共享时带标注光标，支持点击共享窗口输入、滚动，房间持久化无需反复传递链接。

rss · HN Free API / Credits · Oct 14, 18:23

**「为什么重要」** 过去 Screenhero、CoScreen、Around 等多人协作共享工具均因被收购后关停，Petal 采用开源免费模式且支持自托管、fork，可避免用户再次面临服务突然停用的问题，填补了 CoScreen 关停后的免费替代空白。

**「可关注」** 可关注：Petal 支持通过 docker-compose 自托管 LiveKit 服务端，可将流量保留在内网；Linux 版本仍在开发中，可参与贡献。

**Tags**: `#free-tier`, `#open-source`, `#developer-tool`

---

<a id="item-ai-deals-2"></a>
### [Show HN 免费远程工作 API 上线](https://remote-jobs-api.tten.no/) ⭐️ 6.0/10

开发者 earnnovadev 在 Show HN 发布免费无认证远程工作 API，收录 63 万条来自 16 个招聘板的实时职位列表，无公开使用限制，也未公布有效期。

rss · HN Free API / Credits · Oct 14, 08:04

**「为什么重要」** 目前该 API 尚未经过社区验证，若后续稳定可用，可免去自行爬取多平台远程职位的成本。

**「可关注」** 可关注：该 API 无公开使用限制与有效期，但作为未经验证的个人项目，稳定性待观察。

**Tags**: `#api`, `#free-tier`

---

<a id="item-ai-deals-3"></a>
### [GoPuzzleGo 免费拼图生成器上线](https://gopuzzlego.com/generator) ⭐️ 5.0/10

GoPuzzleGo 上线免费拼图生成工具，支持导出 SVG、PDF、STL 三种格式，拼块基于 Voronoi 算法生成，无需注册账号即可直接使用，无明确使用限制与截止时间。

rss · HN Free API / Credits · Oct 14, 11:02

**「为什么重要」** 若需定制拼图素材，该工具无需账号、无付费门槛，可直接导出多格式文件用于打印或 3D 建模，省去注册与付费步骤。

**「可关注」** 可关注：工具支持导出 STL 格式，生成的 Voronoi 拼块可直接用于 3D 打印拼图，无需额外建模操作。

**Tags**: `#free-tier`, `#no-account`, `#utility`

---