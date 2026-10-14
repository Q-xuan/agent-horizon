---
layout: default
title: "Horizon Summary: 2026-10-15 (ZH)"
date: 2026-10-15
lang: zh
---

> 从 196 条内容中筛选出 15 条重要资讯。

<nav id="ah-toc" class="ah-toc" aria-label="目录"><span class="ah-toc-title">目录</span><ul><li><a href="#sec-harness-arch"><span class="ah-toc-name">Harness 架构</span><span class="ah-toc-count">3条</span></a></li><li><a href="#sec-agent-engineer"><span class="ah-toc-name">Agent 工程师日报</span><span class="ah-toc-count">4条</span></a></li><li><a href="#sec-ai-daily"><span class="ah-toc-name">AI 日报</span><span class="ah-toc-count">8条</span></a></li></ul></nav>

---

**[Harness 架构](#sec-harness-arch)**
1. [Mastra Core 1.77.0 发布](#item-harness-arch-1) ⭐️ 8.8/10
2. [pydantic-ai v2.56.0 发布](#item-harness-arch-2) ⭐️ 7.8/10
3. [agent-framework dotnet-1.25.0 发布](#item-harness-arch-3) ⭐️ 7.8/10

**[Agent 工程师日报](#sec-agent-engineer)**
1. [Tev-Gym 长时程智能体数据集发布](#item-agent-engineer-1) ⭐️ 8.0/10
2. [HF 每日论文：Jeva 原生决策模型](#item-agent-engineer-2) ⭐️ 7.0/10
3. [Harness² 提出递归 Agent 进化框架](#item-agent-engineer-3) ⭐️ 7.0/10
4. [WorkRover 递归环境演化框架提出](#item-agent-engineer-4) ⭐️ 7.0/10

**[AI 日报](#sec-ai-daily)**
1. [Anthropic 开新加坡办公室 签 MOU](#item-ai-daily-1) ⭐️ 8.8/10
2. [SentinelOne 用 Daybreak 压缩恶意软件分析周期](#item-ai-daily-2) ⭐️ 7.8/10
3. [GitHub Star 历史 API 请求数降至 24](#item-ai-daily-3) ⭐️ 7.8/10
4. [Anthropic 升级 Claude 2026 美中期选举防护](#item-ai-daily-4) ⭐️ 7.8/10
5. [Claude Platform 支持 OpenTelemetry 追踪](#item-ai-daily-5) ⭐️ 7.8/10
6. [Apigee hybrid 1.17.0 上线 MCP 支持](#item-ai-daily-6) ⭐️ 7.8/10
7. [Block 用 OpenAI 技术构建 AI 安全能力](#item-ai-daily-7) ⭐️ 6.3/10
8. [OpenAI 发布欧盟智能体 AI 采用分析](#item-ai-daily-8) ⭐️ 5.8/10

---

## Harness 架构
{: #sec-harness-arch .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-harness-arch" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-harness-arch-1"></a>
### [Mastra Core 1.77.0 发布](https://github.com/mastra-ai/mastra/releases/tag/%40mastra/core%401.77.0) ⭐️ 8.8/10

Mastra Core 1.77.0 引入 FactorySandbox 提供者契约，支持 Docker、E2B 和 Mastra Platform 三种沙箱实现。新增环境预构建与多仓库会话能力，允许提前构建模板并在会话中启动全部仓库。Durable agent 获得跨 12 种存储后端的 run fencing 保护，Observational Memory 增加并发冲突防护，Span 支持跨追踪链接。

github · PaulieScanlon · 10月14日 08:29

**「设计要点」** Mastra Factory 通过 FactorySandbox 契约抽象沙箱生命周期，将设置、模板和构建能力下沉到提供者实现。Durable agent 的 run fencing 在 Cloudflare DO/D1、Convex、DynamoDB 等存储适配器层实现，通过所有权标记防止分布式部署下的状态覆盖。

**「改了什么」** 新增 FactorySandbox 契约及 Docker/E2B/Platform 三种实现，AgentController 的 steer 和 followUp 方法接受文件附件，多存储适配器支持 run fencing，Observational Memory 增加并发冲突保护与新的写入 API，Span 支持跨追踪链接。@mastra/server 工作流 HTTP 路由不再允许启动内部工作流，需通过 agent 路由调用。

**标签**: `#sandbox`, `#tools`, `#runtime`, `#memory`, `#permissions`

---

<a id="item-harness-arch-2"></a>
### [pydantic-ai v2.56.0 发布](https://github.com/pydantic/pydantic-ai/releases/tag/v2.56.0) ⭐️ 7.8/10

pydantic-ai v2.56.0 发布，引入 SmolSandbox 本地 smolvm 微 VM 沙箱、PGTaskDurability 与 Render Workflows 持久执行集成，以及 Skills 项目与个人库分层机制。BrowserUse 默认改为在 host model 运行且遥测 opt-in，harness Coder 移除 WarnNearLimits 能力。新增 ZaiProvider base\_url 参数，支持 Gemini 4 Argon 长解码、Python 3.15，并将 Google providers 默认超时提升至 20 分钟。

github · dsfaccini · 10月13日 23:35

**「设计要点」** SmolSandbox 在本地 smolvm 微 VM 中隔离运行 harness 能力，Skills 分层支持 project 与 personal libraries 叠加，BrowserUse 默认切至 host model 并调整遥测权限，持久执行通过 PGTaskDurability 与 Render Workflows 接入外部运行时。

**「改了什么」** 新增 SmolSandbox 本地微 VM 沙箱、PGTaskDurability 与 Render Workflows 持久执行集成；Skills 支持项目与个人库分层及 host command 渲染；移除 harness Coder 的 WarnNearLimits；BrowserUse 默认改 host model 运行且遥测 opt-in；ZaiProvider 新增 base\_url 参数；支持 Gemini 4 Argon 与 Python 3.15；Google providers 默认超时提升至 20 分钟。

**标签**: `#sandbox`, `#runtime`, `#tools`, `#subagents`

---

<a id="item-harness-arch-3"></a>
### [agent-framework dotnet-1.25.0 发布](https://github.com/microsoft/agent-framework/releases/tag/dotnet-1.25.0) ⭐️ 7.8/10

Microsoft agent-framework .NET 1.25.0 正式发布，核心升级 A2A 协议至 1.0.0-preview3，并调整工具审批模型为自动拒绝未响应的过期请求。运行时层面修复 SSE 流终止格式（改为 data: \[DONE\]）及 handoff 弹回问题，同时包含 Cosmos chat 元数据分区键策略解耦等 breaking changes。

github · dmytrostruk · 10月14日 19:10

**「设计要点」** 运行时层统一 SSE 流终止语义，修复 handoff 状态机弹回；工具层引入审批超时自动拒绝机制，减少挂起审批占用；协议层跟进 A2A preview3 规范；记忆层更新 agent-memory 依赖组。

**「改了什么」** A2A 包升级至 1.0.0-preview3；工具审批增加自动拒绝超时未响应请求；SSE 流以 data: \[DONE\] 标记终止；修复 handoff bounce-back 与推理残留；Cosmos chat 元数据与分区键策略解耦（breaking）。

**标签**: `#runtime`, `#protocol`, `#tools`, `#approvals`, `#A2A`, `#.NET`

---

## Agent 工程师日报
{: #sec-agent-engineer .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-agent-engineer" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-agent-engineer-1"></a>
### [Tev-Gym 长时程智能体数据集发布](https://huggingface.co/papers/2610.18868) ⭐️ 8.0/10

Hugging Face Daily Papers 于 2026-10-14 介绍 Tev-Gym，首个具备可验证密集渐进奖励的长时程智能体训练数据集。该数据集包含 1,170 个经验证的任务环境，覆盖 7 个领域，采用 latent-world-first 方法构建。它直接针对长时程智能体开发中的训练数据稀缺与奖励稀疏两大瓶颈，为开源模型提供可规模化的训练与评估资源。

rss · Hugging Face Daily Papers · 10月14日 00:00

**「为什么重要」** 长时程智能体（工作周期从小时到天）是自动化发现与递归自我改进（RSI）的核心能力，但开源模型在此类任务上表现不佳。Tev-Gym 通过可验证的密集奖励和规模化环境验证，填补了数据与 recipe 双重缺失的空白。

**「可关注」** 可关注：Tev-Gym 的 latent-world-first 构建方式可能为长时程任务的环境验证和奖励设计提供新范式。

**标签**: `#eval`, `#coding-agent`, `#harness`

---

<a id="item-agent-engineer-2"></a>
### [HF 每日论文：Jeva 原生决策模型](https://huggingface.co/papers/2610.18773) ⭐️ 7.0/10

2026 年 10 月 14 日，Hugging Face Daily Papers 收录论文《Jeva: System One Models from First Principles》，提出决策原生架构 Jeva。该架构针对现有文本预测类决策模型的四个结构缺陷给出解决方案：空值感知、排列不变性、选项可扩展、可缓存。成果对 AI agent 低延迟决策组件、agent 编排、决策模型评估方向有参考价值，目前仅为研究阶段成果，无已落地的生产细节。

rss · Hugging Face Daily Papers · 10月14日 00:00

**「为什么重要」** 当前多数 coding agent 的快速决策模块仍基于文本预测实现，Jeva 指出的四个结构缺陷是现有方案的共性盲区。该架构为低延迟决策组件的设计提供了可验证的结构性改进方向，但实际效果仍需后续实验复现。

**「可关注」** 可关注：现有基于文本预测的快速决策模块是否存在空值区分、排列不变性、选项扩展、计算复用四个结构层面的未覆盖场景。

**标签**: `#orchestration`, `#eval`, `#coding-agent`

---

<a id="item-agent-engineer-3"></a>
### [Harness² 提出递归 Agent 进化框架](https://huggingface.co/papers/2610.14224) ⭐️ 7.0/10

2026-10-14，Hugging Face Daily Papers 收录论文《Harness²: Recursive Agent Harnessing for an Open World》。该论文提出即插即用递归框架 Harness²，解决开放世界场景下 LLM agent harness 自动进化的两个关键问题：未见任务缺少真实验证器，以及现有递归自改进（RSI）方法任务特定、难以泛化到新场景。框架通过两层递归机制实现，任务级递归使用对比 Propose 方法细化当前任务 harness。该工作对构建或优化 agent harness 及评估管道的工程师有参考价值，但属于学术研究贡献，非生产工具或官方发布。

rss · Hugging Face Daily Papers · 10月14日 00:00

**「为什么重要」** 开放世界场景下 agent 能力进化依赖 harness 设计，但未见任务缺乏验证器、RSI 泛化差是当前核心瓶颈。该论文直接针对这两个问题提出技术方案，对评估 pipeline 和 harness 自动化设计有参考意义。

**「可关注」** 可关注：若需在开放世界场景下自动进化 agent harness，可参考该论文的两层递归设计，分别解决任务级验证器缺失和跨任务泛化问题。

**标签**: `#harness`, `#eval`

---

<a id="item-agent-engineer-4"></a>
### [WorkRover 递归环境演化框架提出](https://huggingface.co/papers/2610.18067) ⭐️ 7.0/10

2026 年 10 月 14 日，Hugging Face Daily Papers 收录论文《WorkRover: Scaling Long-Horizon Cowork Agent Training Via Recursive Environment Evolution》。该论文提出 WorkRover 框架，通过 harness 驱动的递归环境演化训练长期协作者智能体。框架使构建智能体联合构建语义对齐的工作上下文、可执行任务与基于证据的验证器，并根据工作空间状态和执行反馈调整行动。当前材料为截断内容，缺乏完整技术实现与性能验证细节。

rss · Hugging Face Daily Papers · 10月14日 00:00

**「为什么重要」** 该框架直接针对交互式强化学习训练环境的扩展难题，其 harness 驱动迭代细化机制对编码智能体的评估与训练环境设计有参考价值。但论文尚未提供完整性能验证，实际效果待进一步确认。

**「可关注」** 可关注：WorkRover 将工作上下文、任务与验证器的联合构建与验证纳入递归演化循环，这提示编码智能体训练环境可考虑把 harness 反馈直接接入环境迭代而非仅用于最终评估。

**标签**: `#harness`, `#eval`, `#coding-agent`

---

## AI 日报
{: #sec-ai-daily .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-daily" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-daily-1"></a>
### [Anthropic 开新加坡办公室 签 MOU](https://www.anthropic.com/news/singapore-office-opening) ⭐️ 8.8/10

Anthropic 于 2026 年 10 月 14 日开设位于新加坡的办公室，为其亚太区第五个办公室，同时与新加坡数字发展与信息部签署谅解备忘录（MOU），合作方向涵盖 AI 安全、模型评估、AI 应用研究、公私部门负责任 AI 采用等。其 Claude 已支撑 GovTech Singapore、Grab、DBS 等机构的服务，每日覆盖数百万用户。关键数据：新加坡是 Claude 全球最活跃市场之一，按人均 Claude.ai 使用量在 121 个国家中排名第二，达人口规模预期水平的近 6 倍；目前已有超 1500 名 GovTech Singapore 工程师和技术人员使用 Claude Code 现代化政府系统，Grab 的销售助手 BriX 使用 Claude 后每季度节省约 4 万小时人力。

rss · Anthropic News · 10月14日 00:00

**「为什么重要」** Anthropic 此次在新加坡的布局是其亚太区域扩张的重要落点，MOU 聚焦 AI 安全、公共部门能力建设等方向，叠加新加坡已有的政府、金融、科技企业落地案例，可支撑区域 AI 合规与规模化应用。

**「可关注」** 可关注：新加坡地区已实现 Claude Code 在 GovTech 等公共部门、DBS 等金融机构的规模化落地，且支持通过 Amazon Bedrock 提供区域内推理服务，满足受监管行业的数据处理合规要求。

**标签**: `#lab`, `#industry`, `#policy`

---

<a id="item-ai-daily-2"></a>
### [SentinelOne 用 Daybreak 压缩恶意软件分析周期](https://openai.com/index/sentinelone) ⭐️ 7.8/10

OpenAI 官方博客披露，网络安全公司 SentinelOne 已部署 OpenAI Daybreak 开展恶意软件分析。该方案将分析周期从数周压缩至数小时，同时扩大了可调查的威胁总量。

rss · OpenAI Blog · 10月14日 12:00

**「为什么重要」** 这是大模型在网络安全垂直场景的明确落地案例，给出了可量化的效率提升基准，对同类安全分析场景有参考价值。

**「可关注」** 可关注：OpenAI Daybreak 在恶意软件分析场景的落地效率表现。

**标签**: `#lab`, `#industry`, `#product`

---

<a id="item-ai-daily-3"></a>
### [GitHub Star 历史 API 请求数降至 24](https://github.blog/engineering/architecture-optimization/from-2500-requests-to-24-rebuilding-star-history-without-the-stargazers/) ⭐️ 7.8/10

GitHub 发布新版仓库 Star 历史 API，可在不返回用户个人身份、无需无界数据库操作的前提下提供 Star 趋势数据。该 API 所需请求数从 2500 次降至 24 次。GitHub 同时公开了该方案的相关工程权衡。

rss · GitHub Blog · 10月14日 19:11

**「为什么重要」** 该更新在保护用户隐私的同时降低了 Star 趋势数据的获取成本，公开的工程权衡细节也可为同类数据接口的架构设计提供参考。

**「可关注」** 可关注：新版 Star 历史 API 通过放弃返回个体用户身份，实现请求数大幅降低与数据库操作边界可控的工程权衡路径。

**标签**: `#product`, `#industry`

---

<a id="item-ai-daily-4"></a>
### [Anthropic 升级 Claude 2026 美中期选举防护](https://www.anthropic.com/news/2026-us-midterms) ⭐️ 7.8/10

Anthropic 发布公告称已升级 Claude 针对 2026 年美国中期选举的防护体系。其分析近一周 25 万条美国用户对话发现，约 5.75% 涉及政治话题，0.51% 涉及选举或投票，要求推荐投票对象的请求仅占 0.01%，违反选举诚信政策的请求占 0.002%；随着选举日临近，该占比预计会进一步上升。Claude Opus 5.5、Sonnet 5.5、Haiku 5.5 在政治中立性评估中得分 99%，为历代模型最高，已修复此前版本对右倾立场论点过度软化的问题。本月内 Claude 将开始从 Democracy Works 拉取官方投票信息直接回复美国用户，选举夜及之后会展示实时官方计票结果；Anthropic 还新增分类器识别多步骤选举滥用，此前与 ISD、麦凯恩研究所的测试显示，分散在多个无害请求中的恶意竞选操作可能被原有防护漏检。

rss · Anthropic News · 10月14日 00:00

**「为什么重要」** 这是 AI 实验室公开的选举场景模型安全与信息供给的完整更新，覆盖政治中立性测试、权威选举信息接入、滥用防护的实际验证逻辑，对从事 AI 选举合规、模型安全治理的从业者有直接参考价值。

**「可关注」** 可关注：Anthropic 新增的多步骤选举滥用分类器，以及其将官方选举信息直接注入对话回复的落地方式。

**标签**: `#lab`, `#policy`, `#industry`

---

<a id="item-ai-daily-5"></a>
### [Claude Platform 支持 OpenTelemetry 追踪](https://claude.com/resources/articles/agent-observability-on-the-claude-platform) ⭐️ 7.8/10

Anthropic 宣布 Claude Platform 现已上线 OpenTelemetry（OTel）追踪公开测试版，覆盖 Claude 托管 Agent、Messages API 及 Claude SDKs。开发者可将 Agent 的模型调用、工具使用、MCP 服务器调用等全链路数据发送至任意支持 OTLP 端点的 OTel 可观测工具，追踪数据遵循 OpenTelemetry GenAI 语义约定，可对接 Grafana Cloud、Datadog、Langfuse 等主流工具。使用限制为：托管 Agent 与 Messages API 需在 Claude Console 配置目标地址，Claude SDKs 自动导出追踪数据。

rss · Claude Blog · 10月14日 00:00

**「为什么重要」** 该能力打通 Agent 全链路操作与现有可观测体系，无需额外埋点即可统一排查 Agent 故障、评估运行效果，同时满足审计场景下对 Agent 操作可追溯的要求，降低 Agent 开发与运维成本。

**「可关注」** 可关注：Claude SDK 已默认开启 OTel 追踪自动导出，托管 Agent 与 Messages API 需在 Claude Console 手动配置可观测工具目标地址，追踪数据遵循 OpenTelemetry GenAI 语义约定，可直接对接支持 OTLP 端点的工具。

**标签**: `#product`, `#lab`

---

<a id="item-ai-daily-6"></a>
### [Apigee hybrid 1.17.0 上线 MCP 支持](https://developers.googleblog.com/announcing-mcp-support-in-apigee-hybrid-agentic-tools-that-run-in-your-own-cluster/) ⭐️ 7.8/10

谷歌 2026 年 9 月 14 日发布 Apigee hybrid 1.17.0，正式上线模型上下文协议（MCP）支持。用户可在自有 Kubernetes 集群、本地机房或其他公有云环境中运行 MCP 数据面，无需迁移现有 API 运行时、自行搭建 MCP 服务器或编写代码，即可将已受治理的 API 转为 AI agent 可调用的工具。MCP 为可选功能，默认未启用，需通过 Helm 升级现有集群开启，且必须优先升级 apigee-operator chart、再升级 apigee-org chart，否则不会生成 MCP 相关 Pod。MCP 请求流量全程留在用户集群内，配置由集群内侧边容器主动拉取，无需谷歌侧向用户网络开放入向路径。

rss · Google Developers AI · 10月14日 00:00

**「为什么重要」** 此前 Apigee 的 MCP 预览仅支持谷歌托管基础设施，无法满足因监管要求、本地系统部署、多云架构等需将运行时放在自有环境的客户需求，本次更新填补了该空白，让这类客户也能无代码将现有 API 转为 AI agent 可调用工具。

**「可关注」** 可关注：升级 Apigee hybrid 开启 MCP 时需先升级 apigee-operator chart 再升级 apigee-org chart，顺序错误会导致升级后无 MCP Pod 生成。

**标签**: `#product`, `#model`, `#industry`, `#lab`

---

<a id="item-ai-daily-7"></a>
### [Block 用 OpenAI 技术构建 AI 安全能力](https://openai.com/index/block-ai-powered-security) ⭐️ 6.3/10

OpenAI 官方博客发布的客户案例显示，Block 采用 OpenAI 技术构建 AI 驱动的安全能力，其安全团队威胁调查与补丁提案的耗时缩短至分钟级。该案例未披露具体技术实现、所用模型及可量化的效果数据。

rss · OpenAI Blog · 10月14日 07:00

**「可关注」** 可关注：Block 基于 OpenAI 技术落地 AI 安全场景的后续技术细节披露。

**标签**: `#industry`, `#product`

---

<a id="item-ai-daily-8"></a>
### [OpenAI 发布欧盟智能体 AI 采用分析](https://openai.com/index/the-eus-next-chapter-in-ai-is-agentic) ⭐️ 5.8/10

OpenAI 官方博客发布分析，称欧盟地区企业与中小企业的智能体 AI 采用规模正在增长。分析同时指出更深度的智能体 AI 使用有望为相关主体释放更多价值。当前公开的内容片段未披露具体数据、落地场景或核心研究发现细节。

rss · OpenAI Blog · 10月14日 00:00

**标签**: `#lab`, `#industry`

---