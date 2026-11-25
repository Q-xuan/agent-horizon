---
layout: default
title: "Horizon Summary: 2026-11-26 (ZH)"
date: 2026-11-26
lang: zh
---

> 从 183 条内容中筛选出 13 条重要资讯。

<nav id="ah-toc" class="ah-toc" aria-label="目录"><span class="ah-toc-title">目录</span><ul><li><a href="#sec-harness-arch"><span class="ah-toc-name">Harness 架构</span><span class="ah-toc-count">3条</span></a></li><li><a href="#sec-agent-engineer"><span class="ah-toc-name">Agent 工程师日报</span><span class="ah-toc-count">8条</span></a></li><li><a href="#sec-ai-daily"><span class="ah-toc-name">AI 日报</span><span class="ah-toc-count">2条</span></a></li></ul></nav>

---

**[Harness 架构](#sec-harness-arch)**
1. [Mastra Core 1.86.0 发布](#item-harness-arch-1) ⭐️ 8.8/10
2. [pydantic-ai v2.75.0 发布](#item-harness-arch-2) ⭐️ 7.8/10
3. [Cloudflare Search for Agents 发布](#item-harness-arch-3) ⭐️ 5.8/10

**[Agent 工程师日报](#sec-agent-engineer)**
1. [Inkling 2 Mini 单卡 RTX PRO 6000 推理调优实测](#item-agent-engineer-1) ⭐️ 8.8/10
2. [RLVB 提出可验证信念强化学习](#item-agent-engineer-2) ⭐️ 7.0/10
3. [NightWatch 解决 CUA 感知-动作差](#item-agent-engineer-3) ⭐️ 7.0/10
4. [HF 每日论文：具身 AI 镜像基准发布](#item-agent-engineer-4) ⭐️ 7.0/10
5. [ICLWorld 跨域 agent ICL 基准发布](#item-agent-engineer-5) ⭐️ 7.0/10
6. [Ai2 调研：科学家划定科研 AI agent 边界](#item-agent-engineer-6) ⭐️ 6.8/10
7. [IBM CUGA 开源语音代理实践](#item-agent-engineer-7) ⭐️ 6.8/10
8. [LLM 与 coding agent 年度三个拐点](#item-agent-engineer-8) ⭐️ 6.0/10

**[AI 日报](#sec-ai-daily)**
1. [GitHub 发布应用现代化证据优先指南](#item-ai-daily-1) ⭐️ 6.3/10
2. [Gemini 4 Neon 登顶 LiveBench 长流程榜](#item-ai-daily-2) ⭐️ 5.5/10

---

## Harness 架构
{: #sec-harness-arch .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-harness-arch" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-harness-arch-1"></a>
### [Mastra Core 1.86.0 发布](https://github.com/mastra-ai/mastra/releases/tag/%40mastra/core%401.86.0) ⭐️ 8.8/10

Mastra Core 1.86.0 引入 durable crash-safe 实验、experimental Knowledge importer 基础设施与 native durable Agent 执行引擎。实验通过 \`durable: true\` 启用事件化工作流，worker 崩溃或重新部署可由其他 worker 接续未确认项。Knowledge importer 提供端到端契约与 \`knowledge.importers.run\(\)\` 接口，支持 in-memory、LibSQL、Postgres，具备 batching、leases、replay protection 与 settle/repair 语义。此外新增 \`interrupted\` 线程运行状态，durable agent 被 \`mastra.shutdown\(\)\` 中断后恢复不再显示为 \`failed\`；\`executionEngine: &\#x27;durable&\#x27;\` 已改为 \`executionEngine: &\#x27;default&\#x27;\`，\`get\_process\_output\` 移除 \`wait: true\` 改用 \`waitSeconds\` \(1–300\)。

github · PaulieScanlon · 11月25日 10:00

**「设计要点」** 运行时层面，durable 实验与 Agent 执行依赖 pubsub（如 Redis Streams）实现事件重放与跨 worker 接续；Knowledge importer 的 bookkeeping 与页面数据同库同事务写入，通过 \`unsettled\` 标记与 writer guard 保证导入幂等与冲突检测。权限层面，host 可通过固定 \`principals\` 与 \`author\` 在 agent 外运行 Knowledge 工具，遵循与 agent 相同的 scope 规则。

**「改了什么」** 新增 durable 实验、Knowledge importer 基础设施、native durable Agent 执行引擎、\`createChannelTools\(\)\`/Slack 工具集、\`knowledge\_activity\` 查询与 host-run principals/author 支持。破坏性变更包括 \`get\_process\_output\` 移除 \`wait: true\`、\`@mastra/connect\` 替换为 \`ConnectEvents\` iterator API、MCP 字段 \`projectId\` 重命名为 \`project\`，以及 playground-ui traces 组件重大 API 调整。

**标签**: `#runtime`, `#memory`

---

<a id="item-harness-arch-2"></a>
### [pydantic-ai v2.75.0 发布](https://github.com/pydantic/pydantic-ai/releases/tag/v2.75.0) ⭐️ 7.8/10

pydantic-ai v2.75.0 发布，引入工作区文件权限分级、模型响应错误分类、Pax 权限批准流程、指令共享、Gemini thinking tokens 计费及能力指令权限绑定等变更。工作区文件权限调整为 breaking change：低于 &\#x27;operator&\#x27; 权限的文件不再注入 RepoContext、Skills、Memory 指令，新增 \`lowest\_authority\_under\` 参数，各组件改为通过工具或框架数据提供。Durable runs 记录额外 \`realpath\` 工作区调用，升级需处理进行中运行；Gemini thinking tokens 现计入输出统计，影响 UsageLimits 计算。

github · dsfaccini · 11月25日 18:21

**「设计要点」** 运行时采用权限分级注入机制，核心上下文组件根据文件权限决定是否将工作区文件内容注入系统提示或作为框架数据发送。Durable run 通过记录 \`realpath\` 工作区调用实现状态一致性，Pax 权限批准采用 token-taking 处理器模式与 harness \`approval\_ask\` 集成。

**「改了什么」** 工作区文件权限处理改为 breaking change：低于 &\#x27;operator&\#x27; 权限的文件不再注入核心上下文组件指令，新增 \`lowest\_authority\_under\` 参数，Durable runs 记录额外 \`realpath\` 调用。模型响应错误分类细化，FallbackModel 和 ModelFallback 现对空响应和不可读响应回退。新增 \`RunContext.submit\_output\(\)\`、Temporal \`ExternalEventWaiter\`、\`ClearToolResults\` 工具过滤及能力指令权限绑定，Gemini thinking tokens 计入输出统计。

**标签**: `#permissions`, `#memory`, `#tools`, `#runtime`

---

<a id="item-harness-arch-3"></a>
### [Cloudflare Search for Agents 发布](https://blog.cloudflare.com/search-for-agents/) ⭐️ 5.8/10

Cloudflare 发布 Search for Agents，通过在控制台添加开关自动为 zone 创建 AI Search 实例并索引内容。该功能在网络层自动暴露 \`/.well-known/search\` 端点，使 agent 可发现并搜索网站内容。技术上新增对 RFC 10008 HTTP QUERY 方法的原生支持，返回 Markdown 格式检索结果而非生成式答案。

rss · Cloudflare AI · 11月25日 14:00

**「设计要点」** 功能运行于 Cloudflare 边缘网络，自动为 zone 创建独立 AI Search 实例。通过 content negotiation 与 Markdown for Agents 协同，在 HTML 头部或 Markdown YAML front matter 中注入可发现性元数据。搜索 API 默认暴露于 \`/.well-known/search\`，支持 GET 与 QUERY 方法。

**「改了什么」** 新增控制台开关，自动完成 AI Search 实例创建、内容爬取索引及 API 暴露。引入 \`/.well-known/search\` 统一搜索入口，支持自然语言查询。新增 HTTP QUERY 方法支持，允许在请求体中传递搜索条件。通过在页面头部自动注入元数据标签实现端点自动发现。

**标签**: `#tools`

---

## Agent 工程师日报
{: #sec-agent-engineer .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-agent-engineer" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-agent-engineer-1"></a>
### [Inkling 2 Mini 单卡 RTX PRO 6000 推理调优实测](https://huggingface.co/blog/inkling-2-mini-inference-hillclimb) ⭐️ 8.8/10

Hugging Face 2026 年 11 月 25 日发布博客，公布 Inkling 2 Mini 在单张 RTX PRO 6000 96GB 上的推理优化实测结果。Inkling 2 Mini 为 looped MoE 架构，24 物理层、中间 12 层循环 3 次形成 48 有效层，总参数量约 26B、单 token 激活 3B，支持 1M token 上下文，在 Artificial Analysis Intelligence Index v5 及 32/48 个基准测试中领先同权重级模型。官方发布的 vLLM、SGLang nightly 构建支持该模型，但配方仅针对 sm100 架构的 B200、GB300，sm120 的 RTX PRO 6000 存在内核兼容性差异。团队用配备推理优化技能的 coding agent，通过 Hugging Face Jobs 开展对照实验，最终采用 vLLM nightly 搭配 DSpark 推测解码、7 个草稿 token 加概率采样的配置，单用户解码速度从基线 136 tok/s 提升至 190.6 tok/s（+40%），8 用户聚合吞吐从~570 tok/s 提升至 716 tok/s（+26%），贪心输出字节级一致，250K token 长上下文 needle 检索 3/3 通过，最优配置已部署为推理端点，全部日志、脚本、原始测量数据公开于 NielsRogge/inkling-2-mini-hillclimb 仓库。

rss · Hugging Face Blog · 11月25日 00:00

**「为什么重要」** 该博客填补了 Inkling 2 Mini 在 sm120 架构 GPU 上的官方调优空白，提供了可复现的对照实验流程与验证通过的启动参数，对评估本地部署 coding agent、工具调用场景可行性的工程师有直接参考价值。

**「可关注」** 可关注：Inkling 2 Mini 的 checkpoint 固定草稿长度为 7，无法使用更短的草稿数做推测解码，且温度 1.0 下概率采样比贪心采样快 11%。

**标签**: `#coding-agent`, `#eval`, `#harness`

---

<a id="item-agent-engineer-2"></a>
### [RLVB 提出可验证信念强化学习](https://huggingface.co/papers/2611.32884) ⭐️ 7.0/10

2026 年 11 月 25 日，Hugging Face Daily Papers 分享了一篇 arXiv 预印本论文（2611.32884），提出 Reinforcement Learning with Verifiable Beliefs（RLVB）方法。该方法针对长任务智能体过早承诺答案的失败模式，通过奖励机制让智能体在证据不足时继续收集证据，在证据充分时提交答案。论文在训练阶段利用模拟器计算每一步的精确后验分布，以判断证据是否足够。目前该研究仅处于预印本阶段，尚未有官方生产版本发布。

rss · Hugging Face Daily Papers · 11月25日 00:00

**「为什么重要」** 该研究直接针对长运行智能体的常见失败模式，提供了可量化的训练框架。但预印本尚未经过同行评审，实际效果需待复现验证。

**「可关注」** 可关注：长任务智能体的&quot;过早承诺&quot;问题可通过验证信念后验的奖励信号缓解，但需确认该方法在真实环境而非模拟器中的泛化能力。

**标签**: `#coding-agent`, `#eval`

---

<a id="item-agent-engineer-3"></a>
### [NightWatch 解决 CUA 感知-动作差](https://huggingface.co/papers/2611.28947) ⭐️ 7.0/10

2026 年 11 月 25 日 Hugging Face Daily Papers 发布论文，提出即插即用框架 NightWatch，用于解决基于视觉语言模型（VLM）的计算机使用代理（CUAs）的感知-动作差问题。当前 CUAs 通过离散快照感知环境，叠加 VLM 推理延迟与动态界面变化，常导致观测状态在执行动作前过时。NightWatch 无需修改 CUAs 的模型、提示词或动作空间，搭配轻量组件 NightWatch-0.8B 为代理提供连续、时间锚定的感知能力。当前内容来自二次聚合器的截断摘要，原文完整细节未完全披露。

rss · Hugging Face Daily Papers · 11月25日 00:00

**「为什么重要」** 该框架直指 CUAs 在动态桌面、网页、移动场景中的核心感知痛点，且即插即用特性无需改动现有代理核心逻辑，对构建计算机使用代理及对应 harness 的工程师有直接参考价值。

**「可关注」** 可关注：NightWatch 采用即插即用设计，无需修改现有 CUA 的模型、提示词或动作空间即可接入连续感知能力，降低了感知升级的改造成本。

**标签**: `#coding-agent`, `#harness`

---

<a id="item-agent-engineer-4"></a>
### [HF 每日论文：具身 AI 镜像基准发布](https://huggingface.co/papers/2611.33010) ⭐️ 7.0/10

2026 年 11 月 25 日 Hugging Face 每日论文条目发布相关研究，提出可复现的 RoboDojo-Mirror 具身 AI 机器人操作策略鲁棒性评估基准。该基准基于 RoboDojo 构建，保留原任务目标、成功判定标准与策略检查点，设置无镜基线、单面镜、双面镜、镜像桌面共 4 种测试条件。测试覆盖视觉语言动作模型（VLA）、世界动作模型、智能体策略共 5 类策略，所有镜像条件下聚合成功率均下降，3 种镜像条件的平均降幅为 10.8 至 56.7 个百分点，最高单策略降幅达 62.5 个百分点。该基准目前仅面向具身 AI 子领域的机器人操作策略评估，不影响通用编码智能体相关方向。

rss · Hugging Face Daily Papers · 11月25日 00:00

**「为什么重要」** 该基准首次系统量化了镜像场景对主流机器人操作策略的鲁棒性冲击，为具身 AI 策略评估提供了新的可复现测试靶点，目前影响范围限于具身 AI 子领域。

**「可关注」** 可关注：RoboDojo-Mirror 基准已公开且覆盖多类主流策略类型，可作为具身 AI 操作策略鲁棒性评估的复现测试集。

**标签**: `#eval`

---

<a id="item-agent-engineer-5"></a>
### [ICLWorld 跨域 agent ICL 基准发布](https://huggingface.co/papers/2611.32649) ⭐️ 7.0/10

2026-11-25，Hugging Face Daily Papers 介绍了一篇预印本，提出 ICLWorld 与 UIverse。ICLWorld 是在线基准，覆盖数字世界（计算机使用）与物理世界（机器人）的 agent 上下文学习评估；UIverse 作为统一工具包，将各类环境转化为用户界面以标准化测试接口。该工作构建 30 个环境、录制 630 段演示视频（累计 10+ 小时）、设计 160 个含定制化反直觉规则的任务，直接针对现有基准多为离线、依赖文本或静态图像、存在训练数据污染风险、机器人评估限于方法级消融等缺陷。目前仅为预印本，尚未经过同行评审。

rss · Hugging Face Daily Papers · 11月25日 00:00

**「为什么重要」** 现有 agent 评估工具普遍存在离线测试与数据污染风险，难以衡量 agent 在真实交互中的上下文学习能力。ICLWorld 提供了跨数字与物理世界的在线评估框架，但作为预印本，其任务设计质量与基准稳定性尚未经社区验证。

**「可关注」** 可关注：UIverse 将异构环境统一为 UI 接口的设计思路，可能降低多环境 agent 测试的适配成本；ICLWorld 中 160 个含反直觉规则的任务，对检验 agent 的真实上下文学习能力有直接参考价值。

**标签**: `#eval`, `#harness`, `#coding-agent`

---

<a id="item-agent-engineer-6"></a>
### [Ai2 调研：科学家划定科研 AI agent 边界](https://huggingface.co/blog/allenai/where-scientists-draw-the-line-on-ai-agents) ⭐️ 6.8/10

2026 年 11 月 25 日 Hugging Face 博客发布艾伦 AI 研究所（Ai2）的调研结果。该调研访谈 17 名自然、应用、社会科学领域科学家，明确科研场景 AI agent 需满足验证、隐私、客观性、问责、透明五大信任维度，提出科学家应参与决定 agent 承担的研究任务、运行规则与评估标准。当前提出的参与式评估方案仍为待和科学家共同测试的提案，未形成落地标准，影响科研场景 AI agent 开发者、科研机构及伦理合规团队的设计思路。

rss · Hugging Face Blog · 11月25日 18:52

**「为什么重要」** 该调研来自一线科研 AI 团队的实地访谈，明确了高约束科研场景下 AI agent 的责任边界与信任要求，为相关 agent 的合规设计提供了直接参考；其提出的参与式评估方向仍处于提案阶段，尚未形成可复用的行业标准。

**「可关注」** 可关注：科研场景 AI agent 需同时保障任务正确性与研究合规性，当前无统一行业评估标准，需优先设计可追溯的操作日志、细粒度权限边界，适配不同科研领域对 AI 参与度的差异化要求。

**标签**: `#permissions`, `#observability`, `#eval`

---

<a id="item-agent-engineer-7"></a>
### [IBM CUGA 开源语音代理实践](https://huggingface.co/blog/ibm-research/an-indic-voice-agent-with-cuga) ⭐️ 6.8/10

2026 年 11 月 25 日 Hugging Face 博客发布 IBM Research 开源代理框架 CUGA 的应用案例，将其用于印度区域语言农业语音代理，该框架为 AppWorld Benchmark 当前领先方案。CUGA 作为嵌入式 SDK 封装模型接线、工具管理、状态与护栏逻辑，采用“文本入、文本出”核心设计，语音仅作为语音转文本、文本转语音两层薄封装，支持调用浏览器端 Sarvam AI 云 API 或自有服务器的开源 SraVaani、Svara 语音模型。案例中团队踩过默认英文嵌入模型导致非英语查询跨语言检索静默失效的坑，换用 intfloat/multilingual-e5-large 多语言嵌入模型后解决，同时用 OFF\_TOPIC 标签实现离题重定向无需二次 LLM 调用。该架构也被 IBM 定位为 Bharat Core Indic AI 工作负载的配套代理方案，面向印度大规模区域语言场景提供数据主权合规能力，案例附带可直接试用的 CUGA Apps Spaces 与从零搭建的教程。

rss · Hugging Face Blog · 11月25日 10:22

**「为什么重要」** 该案例验证了“文本核心+语音薄封装”的代理架构在多语言语音场景的可行性，开源框架与可直接试用的示例降低了多语言代理的开发门槛。目前材料未提及该方案在大规模企业场景下的性能数据、实际用户反馈与合规落地细节，相关影响尚未证实。

**「可关注」** 可关注：多语言代理场景下需优先验证嵌入模型的跨语言语义对齐能力，避免默认英文模型导致的静默检索失效；同时将代理核心设计为文本入文本出可解耦语音层，降低后续替换语音服务的成本。

**标签**: `#harness`, `#eval`, `#orchestration`

---

<a id="item-agent-engineer-8"></a>
### [LLM 与 coding agent 年度三个拐点](https://simonwillison.net/2026/Nov/24/llm-inflection-points/) ⭐️ 6.0/10

2026 年 11 月 24 日，Simon Willison 发布 AI Engineer Code Summit 主题演讲回顾，提出过去 12 个月 LLM 与 coding agent 能力存在三个拐点。第一个拐点是 2025 年 11 月 Claude Opus 4.5 发布，该模型让 Claude Code 从需要频繁修正的辅助工具变为多数日常编码场景下默认结果正确的生产力工具，同期 OpenAI 发布的 GPT-5.1 系列也让 Codex agent 可靠性大幅提升。第二个拐点是 2026 年 6-7 月出现的 Fable 级模型（包括 Claude Fable 5 系列、Claude Opus 5.5、GPT-6 Astra 等），可在给定目标和工具的前提下通过 brute force 解决复杂问题，主动性显著强于此前模型。第三个拐点是 2026 年 9-10 月 frontier 模型 3D 建模与游戏开发能力跃升，Claude Opus 5.5 甚至可通过 12 小时 playtest 优化游戏可玩性。该回顾为 coding agent 工程师提供了一线实践视角的能力演进梳理，但未附可复现基准测试或代码级改进细节，相关能力增益的实际普适性尚未验证。

rss · Simon Willison · 11月24日 23:02

**「为什么重要」** 这份 retrospective 补充了厂商官方发布之外的一线使用者视角，帮助 agent 工程师快速对齐过去一年的核心能力跃迁节点；但文中提及的能力提升均来自个人实践案例，未经过公开标准化基准验证，实际落地增益需结合自身场景验证。

**「可关注」** frontier 模型在工具调用自主性上的提升已出现自主安装依赖、搭建辅助服务解决非预设问题的案例，复杂任务的目标拆解与执行能力可能已突破此前预期。

**标签**: `#coding-agent`, `#eval`, `#orchestration`

---

## AI 日报
{: #sec-ai-daily .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-daily" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-daily-1"></a>
### [GitHub 发布应用现代化证据优先指南](https://github.blog/ai-and-ml/github-copilot/how-to-choose-the-next-safe-step-in-application-modernization/) ⭐️ 6.3/10

GitHub 官方博客发布应用现代化实践指南，提出证据优先的可复用决策流程，覆盖从证据收集、改造方案选择到回归保护设计的全步骤。该指南同时演示了如何将该流程编码为 GitHub Copilot agent skill，无新模型、政策或核心产品发布，属于产品实践类内容。

rss · GitHub Blog · 11月25日 15:00

**「为什么重要」** 该指南提供了可直接落地的应用现代化决策框架，同时展示了 Copilot agent skill 的编码实践，对使用 Copilot 进行应用改造的开发者有实操参考价值。

**「可关注」** 可关注：应用现代化优先按「保留、升级、替换、包装、重写」的 disruptive 程度由低到高选择方案，决策前需先建包含运行时 pin、外部契约、端到端依赖的证据清单。

**标签**: `#product`, `#industry`

---

<a id="item-ai-daily-2"></a>
### [Gemini 4 Neon 登顶 LiveBench 长流程榜](https://mp.weixin.qq.com/s?__biz=MzI3MTA0MTk1MA==&amp;mid=2652745183&amp;idx=2&amp;sn=9e2398515e5d4f23adafd26dd399519e) ⭐️ 5.5/10

新智元 11 月 25 日报道称 Gemini 4 Neon 以 87.4 分登顶 LiveBench 2.0 长流程总榜，领先 Claude Fable 5.2、GPT-6.2 Astra 2.5 分，该榜单为 10 月重构的长流程评测，含 7 个子项 471 道题。该说法无官方一手来源佐证，且模型在 Artificial Analysis 智力指数 v5.0.1 中仅排总榜第三，单任务成本 2.654 美元高于 Astra 的 1.941 美元。

rss · 新智元 · 11月25日 09:40

**「为什么重要」** LiveBench 2.0 聚焦长流程智能体任务，其排名表现可参考对应场景下的模型能力差异，适合做 coding agent 选型的工程师参考。

**「可关注」** 可关注：Gemini 4 Neon 在浏览器操作、研究、编程、推理等长流程工具调用场景得分突出，但跨榜单泛化能力与成本优势不突出。

**标签**: `#model`, `#eval`, `#industry`

---