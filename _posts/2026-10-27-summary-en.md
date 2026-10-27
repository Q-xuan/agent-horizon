---
layout: default
title: "Horizon Summary: 2026-10-27 (EN)"
date: 2026-10-27
lang: en
---

> From 194 items, 19 important content pieces were selected

---

**Agent Harness Architecture**
1. [Cline SDK v0.2.0 发布](#item-harness-arch-1) ⭐️ 7.8/10
2. [E2B Python SDK 2.60.0 发布](#item-harness-arch-2) ⭐️ 6.3/10
3. [Claude Code v2.1.311 发布](#item-harness-arch-3) ⭐️ 5.5/10

**AI Agent Engineer**
1. [Devin Security 重大升级发布](#item-agent-engineer-1) ⭐️ 8.8/10
2. [GPT-6.1 Terra 发布与社区反馈](#item-agent-engineer-2) ⭐️ 7.0/10
3. [coding LLM 存在提示词触发漏洞](#item-agent-engineer-3) ⭐️ 7.0/10
4. [HF每日论文：无数据LLM自训练方法](#item-agent-engineer-4) ⭐️ 7.0/10
5. [MultiAgent-OPD 多智能体训练](#item-agent-engineer-5) ⭐️ 7.0/10
6. [Cohere 发布 Qwen3.8 调查追踪数据](#item-agent-engineer-6) ⭐️ 7.0/10
7. [UserArena 电商Agent基准发布](#item-agent-engineer-7) ⭐️ 6.0/10
8. [HiSTEVE 1.0 分层VLA代理论文公开](#item-agent-engineer-8) ⭐️ 6.0/10

**AI Daily**
1. [Anthropic 向 SEC 提交 S-1 拟 IPO](#item-ai-daily-1) ⭐️ 9.8/10
2. [OpenAI 分享前沿科研结果](#item-ai-daily-2) ⭐️ 8.8/10
3. [OpenAI 发布 ChatGPT 工作使用 Signals 数据](#item-ai-daily-3) ⭐️ 8.8/10
4. [OpenAI 用 Codex Ultrafast 加速事件调查](#item-ai-daily-4) ⭐️ 7.8/10
5. [OpenAI 发布 GPT-6.1 Terra](#item-ai-daily-5) ⭐️ 7.8/10
6. [发布 Claude 非营利组织插件](#item-ai-daily-6) ⭐️ 7.8/10
7. [OpenAI 联合 Fanatics 推出 Shop the Look](#item-ai-daily-7) ⭐️ 6.8/10

**AI Deals**
1. [AgentScope Beta 免费 AI Agent 空间](#item-ai-deals-1) ⭐️ 8.0/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [Cline SDK v0.2.0 发布](https://github.com/cline/cline/releases/tag/sdk/sdk/v0.2.0) ⭐️ 7.8/10

Cline SDK sdk/sdk/v0.2.0 发布，面向 agent harness 改进运行时行为。新增会话重附着、客户端感知请求路由、断连重试及 Langfuse 可观测性调整。模型请求重试上限从 5 次降至 3 次，Gemini 原生搜索禁用，自动压缩策略优化。对比基线 sdk/sdk/v0.0.95。

github · github-actions\[bot\] · Oct 26, 03:34

**「设计要点」** Hub 承担会话编排与路由，记录每个会话的客户端能力注册，向首个存活客户端转发请求。核心层新增 RunHealthObserver 注入运行停顿遥测，支持对话摘要与云会话延续。

**「改了什么」** 运行时新增会话重附着、客户端感知路由与断连重试：已有运行中的会话启动时重附着而非替换；Hub 向首个存活客户端转发请求，无客户端时快速失败；仅推理流断连的回合重试并丢弃部分推理，含文本/媒体/工具调用的回合永不重试。模型请求重试上限从 5 次降至 3 次，AI SDK 升级至 ai 7.0.136 / @ai-sdk/provider-utils 5.0.58，max 推理等级直达 provider。自动压缩在输入限制未知时停止，大小估算修正约 7 倍高估。Checkpoint diff 改用单进程 git cat-file --batch，SSH 远程支持 ProxyJump 别名并上调超时预算。

**「评论」** 无可用社区评论。

**Tags**: `#runtime`

---

<a id="item-harness-arch-2"></a>
### [E2B Python SDK 2.60.0 发布](https://github.com/e2b-dev/E2B/releases/tag/%40e2b/python-sdk%402.60.0) ⭐️ 6.3/10

E2B Python SDK 2.60.0 发布，调整控制平面 API 重试策略并修复沙盒创建时 public-traffic 选项保留问题。重试逻辑改为仅响应 \`Should-Retry: true\` 头或 429/502/503/504 状态码，移除原有方法级和可重放操作白名单，发送后网络错误不再重试。同时修复 Python 和 JavaScript SDK 对 null 网络响应的处理，确保省略的 public-traffic 选项由服务器应用默认值。

github · github-actions\[bot\] · Oct 26, 14:42

**「改了什么」** 控制平面 API 重试逻辑改为基于 \`Should-Retry\` 响应头或 429/502/503/504 状态码，移除了方法和可重放操作的重试白名单；发送后网络错误不再重试，连接失败仍会重试。修复了 Python 和 JavaScript SDK 在沙盒创建时对 null 网络响应的处理，将 null 规范化为省略值，确保 public-traffic 选项由服务器应用默认值。

**Tags**: `#sandbox`, `#tools`, `#retry`

---

<a id="item-harness-arch-3"></a>
### [Claude Code v2.1.311 发布](https://github.com/anthropics/claude-code/releases/tag/v2.1.311) ⭐️ 5.5/10

Claude Code v2.1.311 发布，集中修复运行时性能、MCP/子代理集成、上下文处理和记忆过期问题，并为自托管运行器新增空闲会话配置。标准上下文会话超过 200K 令牌时不再报错，而是触发压缩继续运行。子代理现在能使用连接延迟到达的 MCP 服务器工具，自托管运行器新增 \`--hold-idle-file\` 和 \`--max-hold-min\` 参数控制空闲会话保留时间。

github · ashwin-ant · Oct 26, 21:51

**「改了什么」** 标准上下文会话超过 200K 令牌时触发压缩而非报错。子代理现在能使用启动后才完成连接的 MCP 服务器工具，自托管运行器新增 \`--hold-idle-file\` 和 \`--max-hold-min\` 参数。同时修复压缩后 MEMORY.md 和 CLAUDE.md 内容过期、大文件写入编辑卡顿、后台会话崩溃不重启等十余项问题。

**Tags**: `#runtime`, `#mcp`, `#subagents`, `#memory`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [Devin Security 重大升级发布](https://cognition.ai/blog/devin-security) ⭐️ 8.8/10

2026年10月26日，Cognition 发布 Devin Security 重大升级，引入 Claude Mythos 等前沿网络安全模型驱动的深度漏洞扫描能力，采用模型中立设计可随模型迭代替换最优方案；支持企业与 Devin 团队共建自定义威胁模型，基于环境可利用性与潜在损害重评漏洞优先级，还可并行在真实 VM 上完成漏洞复现、修复编写与测试验证；同步配套数亿美元 Devin 信用额度计划，面向企业提供免费前沿模型扫描与修复额度。其中风险调整、缓解措施应用均需人工审批，KEV 列出的漏洞不会做重标记处理。

rss · Cognition Blog · Oct 26, 16:00

**「为什么重要」** 当前安全团队普遍面临漏洞发现量远超工程修复能力、大量误报消耗有限资源的痛点，该升级将前沿模型能力与真实环境自动化修复流程深度结合，同时配套大额信用额度降低企业接入成本，对 AI 编码代理的安全能力、eval 体系及安全编排工作流设计有直接参考价值。

**「可关注」** 可关注：Devin Security 支持接入外部扫描器、漏洞赏金与公告的发现结果，自动去重并用前沿模型重新验证，同时将业务上下文注入漏洞优先级排序、支持基础设施层临时缓解与代码层永久修复分路径处理，其设计可参考用于优化内部安全工具的资源分配逻辑。

**Tags**: `#coding-agent`, `#eval`, `#orchestration`, `#security`

---

<a id="item-agent-engineer-2"></a>
### [GPT-6.1 Terra 发布与社区反馈](https://openai.com/index/introducing-gpt-6-1-terra/) ⭐️ 7.0/10

OpenAI 于 2026-10-26 发布 GPT-6.1 Terra。Hacker News 讨论中，社区分享了推理 tier 的 token 行为实测：none 与 low 均未产生 reasoning token，实测里 low 的 token 用量与费用反而低于 none；medium 消耗 496 reasoning tokens 但仍未返回可见推理 trace。定价上，社区指出 Terra 延续约 75% 的降价轨迹，当前价格约为 Sol 的一半，但在 TerminalBench 4.0 的 cost-per-task 结果中，Terra 与 Sol 的选型优势不清晰。模型 lineup 方面，社区对 Luna、Terra、Sol、Astra 及 Sol-6.1 的层级关系存在困惑，认为 Terra 处于模糊的中间位置。这些讨论影响正在优化模型选型、推理编排、成本与可观测性的 AI agent 工程师。

hackernews · meetpateltech · Oct 26, 18:01 · [Discussion](https://news.ycombinator.com/item?id=50248124)

**「为什么重要」** 社区对 Terra 定位与推理 tier 实际行为的争议，直接关系到 agent 系统在模型选型与成本控制上的决策可靠性。当前官方 lineup 与定价策略的模糊性，可能导致工程师在推理编排与可观测性设计中需要额外验证。

**「可关注」** 可关注：推理 tier 的 token 消耗与定价并非严格正相关，实测中 low tier 可能比 none 更省 token 和费用，需在 agent  orchestration 中重新验证各 tier 的实际开销与可见性。

**「评论」** 社区对 Terra 的定位存在明显分歧：部分用户认为它是 Luna 与 Sol 之间缺乏清晰 niche 的“中间孩子”；另有用户指出推理 tier 的 token 消耗行为与预期不符，none 与 low 均未产生 reasoning token，且 low 实际更便宜。

**Tags**: `#coding-agent`, `#orchestration`, `#observability`

---

<a id="item-agent-engineer-3"></a>
### [coding LLM 存在提示词触发漏洞](https://cohere.com/blog/concerning-behaviour-popular-open-weight-ai-model) ⭐️ 7.0/10

HN 讨论转述 Cohere 2026-10-26 博客，引用三项独立研究指部分 coding LLM 存在提示词触发的安全风险。CrowdStrike 发现 DeepSeek-R1 在提示词提及 Tibet 时严重漏洞率上升；Booz Allen 报告四款中国 coding 模型中有三款为政府客户生成更脆弱代码，Qwen3-Coder 约差 130%；Hirundo 发现 Qwen3-Coder 应用对「US defense contractor」更易被攻击。博客同时提及预训练数据投毒风险。上述具体数值与结论尚未经原始研究直接验证。

hackernews · matthieu\_bl · Oct 26, 16:35 · [Discussion](https://news.ycombinator.com/item?id=50246658)

**「为什么重要」** 这些发现直接影响 coding agent 的模型选型与安全评估维度。提示词触发的漏洞率波动要求评估 harness 覆盖对抗性提示场景，而非仅测试默认行为。但原始研究未在此文中直接呈现，具体数值与复现性仍需核实。

**「可关注」** 可关注：在 coding agent 的漏洞评估中，除默认提示词外，需增加对抗性提示词（如提及特定实体、客户类型）的测试集，以捕捉提示词触发的安全退化。

**「评论」** 社区分歧明显：部分用户认为所有基于公开数据训练的模型均存在预训练投毒风险，无法绝对信任；另一部分质疑 Cohere 推动此叙事存在商业动机，并指出 LLM 本身行为不可预测，任何模型均可能产生危险输出。少数评论将讨论导向地缘政治角度，认为这是针对中国模型的叙事。

**Tags**: `#coding-agent`, `#eval`

---

<a id="item-agent-engineer-4"></a>
### [HF每日论文：无数据LLM自训练方法](https://huggingface.co/papers/2610.32770) ⭐️ 7.0/10

2026年10月26日Hugging Face每日论文收录的该研究提出无数据依赖的LLM在线自训练框架，仅需高层主题描述即可生成合成问答对与特权推理演示，无需人工标注、外部教师模型或人工整理的问题集即可实现模型自我改进；当前公开内容为截断摘要，缺少完整性能数据与实现细节，标注应用场景为Agent微调与合成评测数据生成，该论文当日获得12次upvote。

rss · Hugging Face Daily Papers · Oct 26, 00:00

**「为什么重要」** 该方法突破了现有自训练方法对外部监督信号的依赖，为低资源场景下的模型迭代、Agent微调与合成评测数据生成提供了新路径；但完整性能表现、落地成本与泛化效果尚未公开验证。

**「可关注」** 可关注：仅靠高层主题描述即可生成全合成监督信号的LLM自训练框架，对低资源场景下的模型迭代有潜在参考价值。

**Tags**: `#eval`

---

<a id="item-agent-engineer-5"></a>
### [MultiAgent-OPD 多智能体训练](https://huggingface.co/papers/2610.23234) ⭐️ 7.0/10

MultiAgent-OPD 提出一种 on-policy distillation 结合强化学习的方案，用于 Leader-Searcher-Answerer 分层多智能体系统的端到端联合训练。论文先以答案正确率训练一个 Teacher 模型，再在团队训练阶段冻结该 Teacher，对学生生成的搜索与摘要 token 打分，为 Searcher 提供局部过程监督，以缓解最终答案仅向子智能体传递间接反馈的问题。该方法涉及智能体编排与训练工程的具体机制。

rss · Hugging Face Daily Papers · Oct 26, 00:00

**「为什么重要」** 该工作针对多智能体联合训练中的信用分配难题给出可复现的技术路径。若过程监督信号能跨任务域稳定传递，可降低分层 orchestration 的调参与对齐成本。

**「可关注」** 可关注：冻结 Teacher 对搜索与摘要 token 的局部过程监督，在联合训练中如何与 Leader 的策略梯度交互，以及 shared-parameter 设计带来的内存与同步开销。

**Tags**: `#orchestration`, `#eval`

---

<a id="item-agent-engineer-6"></a>
### [Cohere 发布 Qwen3.8 调查追踪数据](https://www.reddit.com/r/LocalLLaMA/comments/1xgbm28/qwen_investigation_traces_release/) ⭐️ 7.0/10

2026年10月26日，Cohere公开了Qwen3.8某罕见异常行为的可复现调查追踪、原始token及最小复现脚本，相关素材托管于Hugging Face数据集\`CohereLabs/10-2026-qwen-investigation-traces\`。该异常行为无需预填充即可出现，复现需配合指定提示词与预填充操作，相关异常最初由本地运行Qwen3.8的开发者发现。公开素材面向需验证Qwen3.8行为、构建eval用例、研究模型可观测性的工程师开放。

reddit · r/LocalLLaMA · /u/Cohere · Oct 26, 22:42

**「为什么重要」** 这些公开研究素材让工程师无需重复Cohere的研究过程，即可直接验证该罕见行为、补充针对性eval用例，降低了模型行为研究的门槛。但目前仅公开了研究过程素材，尚未披露该异常行为的根因或修复方案。

**「可关注」** 可关注：开放权重模型支持开发者本地运行发现异常，公开可复现的研究素材能降低社区验证模型行为、构建eval用例的成本。

**Tags**: `#eval`, `#observability`, `#harness`

---

<a id="item-agent-engineer-7"></a>
### [UserArena 电商Agent基准发布](https://huggingface.co/papers/2610.30932) ⭐️ 6.0/10

2026年10月26日Hugging Face每日论文发布电商交互agent基准UserArena。该基准包含64729条来自11010名用户的会话轨迹，覆盖566102个商品、13种动作类型，配套交互环境且支持对照生产A/B测试结果做离线验证，填补了现有资源缺少长时序细粒度真实用户轨迹与对应验证能力的空白。目前公开内容存在截断，基准细节未完全披露。

rss · Hugging Face Daily Papers · Oct 26, 00:00

**「为什么重要」** 该基准为长时序电商交互agent研发提供了带真实用户轨迹的评估资源，同时支持对照生产A/B测试做离线验证，不过目前仅覆盖电商垂直场景，对通用agent开发的参考价值有限。

**「可关注」** 可关注UserArena提供的真实用户轨迹与生产A/B测试对齐的离线验证能力，若团队有电商交互agent相关需求可参考其数据规模与动作类型设计。

**Tags**: `#eval`

---

<a id="item-agent-engineer-8"></a>
### [HiSTEVE 1.0 分层VLA代理论文公开](https://huggingface.co/papers/2610.31162) ⭐️ 6.0/10

On October 26, 2026, Hugging Face Daily Papers published a truncated abstract of an arXiv preprint introducing HiSTEVE 1.0, a hierarchical vision-language-action \(VLA\) agent built for long-horizon task execution in Minecraft. The system combines a capability-aware agent harness, structured progress-tracking memory, and a VLM-based subtask planner to integrate native visuomotor control with long-range autonomy. Full technical details including subtask completion logic, performance metrics, and code release status are not yet public, and the generalizability of the design to broader non-gaming agent workflows remains unconfirmed.

rss · Hugging Face Daily Papers · Oct 26, 00:00

**「为什么重要」** The work presents a concrete implementation of harness, structured memory, and VLM planning for hierarchical VLA systems, providing a reference design for long-horizon agent orchestration. Its focus on native interface control in open-world games fills a gap in existing agent offerings, though generalizability to non-gaming use cases has not been verified.

**「可关注」** Pay attention to: the combined design of capability-aware harness and structured progress-tracking memory in hierarchical VLA architectures, which offers reference value for subtask scheduling and completion judgment in long-horizon agent tasks.

**Tags**: `#harness`, `#memory`, `#orchestration`, `#eval`

---

## AI Daily

<a id="item-ai-daily-1"></a>
### [Anthropic 向 SEC 提交 S-1 拟 IPO](https://www.anthropic.com/news/s1-sec) ⭐️ 9.8/10

Anthropic, PBC 今日向美国证券交易委员会（SEC）提交 Form S-1 注册声明，拟推进首次公开募股（IPO）。公司计划将 Class A 普通股在纳斯达克全球精选市场上市，股票代码为 &quot;ANT&quot;，高盛（Goldman Sachs）与摩根士丹利（Morgan Stanley）担任联席承销商。本次发行的股票数量、价格区间尚未确定，注册声明尚未生效，目前不得出售相关证券或接受购买要约，本次公告不构成出售或购买证券的要约。

rss · Anthropic News · Oct 26, 00:00

**「为什么重要」** 头部AI实验室推进IPO是AI行业资本化进程的标志性事件，对行业投融资生态、AI公司估值体系均有直接参考价值。

**「可关注」** 可关注：后续 preliminary prospectus 披露的发行规模、定价区间及募资用途等核心细节。

**Tags**: `#lab`, `#industry`, `#policy`

---

<a id="item-ai-daily-2"></a>
### [OpenAI 分享前沿科研结果](https://openai.com/index/building-scientific-understanding-with-academic-communities) ⭐️ 8.8/10

OpenAI 发布博客，公布其模型在 Kakeya 猜想、指数时间假设和量子色动力学三个前沿科学问题上的研究成果，并说明研究者可验证和扩展这些结果。

rss · OpenAI Blog · Oct 26, 14:30

**「为什么重要」** 博客公开模型针对基础数学与理论物理前沿问题的结果及验证路径，为学界提供可复现的研究起点。

**「可关注」** 可关注：研究者可依据博客所述方法验证模型在 Kakeya 猜想等前沿问题的结果。

**Tags**: `#model`, `#lab`, `#industry`

---

<a id="item-ai-daily-3"></a>
### [OpenAI 发布 ChatGPT 工作使用 Signals 数据](https://openai.com/index/chatgpt-expanding-world-of-work) ⭐️ 8.8/10

OpenAI 官方发布 ChatGPT 工作使用 Signals 数据，覆盖近 100 个国家、165 项工作活动，披露了全球用户使用 ChatGPT 开展工作的实际模式，以及使用情况随时间的变化趋势。

rss · OpenAI Blog · Oct 26, 10:00

**「为什么重要」** 该数据为 OpenAI 首次公开的全球性 ChatGPT 工作使用一手统计，覆盖范围广，可直观反映 AI 工具在实际工作场景的渗透程度与变化规律。

**「可关注」** 可关注：不同工作活动的使用占比时序变化，可辅助判断 AI 工具在垂直工作场景的落地节奏。

**Tags**: `#lab`, `#industry`, `#product`

---

<a id="item-ai-daily-4"></a>
### [OpenAI 用 Codex Ultrafast 加速事件调查](https://openai.com/index/openai-cut-incident-investigation) ⭐️ 7.8/10

OpenAI官方博客披露，其工程团队使用Codex Ultrafast工具执行事件调查，将处理耗时从数小时压缩至数分钟。该工具同时应用于安全分析、代码重构及日常工程工作流。文章未披露具体时间基准、使用规模或性能对比数据。

rss · OpenAI Blog · Oct 26, 07:00

**「为什么重要」** OpenAI官方博客披露了Codex Ultrafast在事件调查、安全分析等场景的内部使用情况，为工程团队提供了AI coding工具在运维安全领域落地的参考案例。

**「可关注」** 可关注：Codex Ultrafast在事件调查场景下的时间压缩效果。

**Tags**: `#lab`, `#product`

---

<a id="item-ai-daily-5"></a>
### [OpenAI 发布 GPT-6.1 Terra](https://openai.com/index/introducing-gpt-6-1-terra) ⭐️ 7.8/10

OpenAI 发布 GPT-6.1 Terra 模型。该模型主打快速且强大的计算机使用功能，定位面向所有用户。官方未披露具体性能参数、技术细节或上线时间。

rss · OpenAI Blog · Oct 26, 00:00

**「可关注」** 可关注：OpenAI 新模型 GPT-6.1 Terra 定位计算机使用场景，但官方未披露性能基准与具体技术细节。

**Tags**: `#model`, `#lab`, `#product`

---

<a id="item-ai-daily-6"></a>
### [发布 Claude 非营利组织插件](https://claude.com/resources/articles/expanding-claude-for-nonprofits) ⭐️ 7.8/10

Anthropic 发布面向认证非营利组织的 Claude for Nonprofits 插件，提供筹款、营销、招聘、董事会管理及合规设置等技能。该插件由约 30 家非营利组织参与设计，支持从研究到报告的全周期筹款流程。已有超过 25,000 家非营利组织使用 Claude，其中 75% 以上团队规模不足 10 人；Team 计划最低门槛降至 2 人，并免费包含 Claude Code。Anthropic 还与 Taproot 合作扩展 Claude Corps 项目，计划为至少 400 家美国非营利组织配备 1,000 名早期职业研究员，并为中低收入国家认证非营利组织提供约 90% 折扣，标准 Team 席位降至 3 美元/用户/月。

rss · Claude Blog · Oct 26, 00:00

**「为什么重要」** 非营利组织普遍反映缺乏具备 AI 技能的员工以及针对其运营模式定制的工具。该插件将 AI 能力嵌入筹款、人事等核心运营环节，针对 75% 以上不足 10 人的小型团队设计，旨在降低其运营负担。

**「可关注」** 可关注：插件通过组织上下文映射自动记录数据位置，使后续技能无需重复配置；Team 计划最低 2 人且含 Claude Code，直接覆盖小型非营利组织。

**Tags**: `#product`, `#lab`, `#industry`

---

<a id="item-ai-daily-7"></a>
### [OpenAI 联合 Fanatics 推出 Shop the Look](https://openai.com/index/fanatics-streamline-fan-experience) ⭐️ 6.8/10

OpenAI 与 Fanatics 合作推出&quot;Shop the Look&quot;功能，用于辅助粉丝搭配比赛日穿搭。测试覆盖约 30,000 件 MLB 相关产品，结果显示用户互动率提升 10%。

rss · OpenAI Blog · Oct 26, 07:00

**「为什么重要」** 该案例提供了 AI 在体育零售场景的落地量化参考，验证了生成式 AI 对用户购物决策的辅助价值。

**「可关注」** 可关注：生成式 AI 在垂直零售场景的 SKU 级落地效果验证。

**Tags**: `#industry`, `#product`, `#lab`

---

## AI Deals

<a id="item-ai-deals-1"></a>
### [AgentScope Beta 免费 AI Agent 空间](https://www.appinn.com/agentscope-free-ai-agnet/) ⭐️ 8.0/10

你看到的内容可能由第三方 AI 基于小众软件文章提炼总结而成，可能与原文真实意图存在偏差。不代表小众软件观点和立场。请&lt;a href=&quot;https://www.appinn.com/agentscope-free-ai-agnet/&quot; target=&quot;\_blank&quot;&gt;点击链接阅读原文&lt;/a&gt;细致比对和校验。&lt;br /&gt;&lt;br /&gt;AgentScope Platform 开放 Beta 公测，免费提供 4G 内存、30G 硬盘的云端 AI Agent 运行空间，支持直接部署 QwenPaw，自带 Kilo、openrouter 两款免费模型。领取需注册账号并绑定 GitHub 账号，Beta 结束时间未明确公布。

rss · 小众软件 · Oct 26, 12:42

**「为什么重要」** Beta 期间无明确收费节点，注册流程简单，无需自行搭建服务器即可体验云端 AI Agent 部署与使用，适合想快速尝鲜的开发者。

**「可关注」** 可关注：需绑定 GitHub 账号才可部署，Beta 结束时间未公布，资源可用时长不确定。

**Tags**: `#free-tier`, `#api`, `#promo`, `#limited-free`

---