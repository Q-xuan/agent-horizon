---
layout: default
title: "Horizon Summary: 2026-11-08 (ZH)"
date: 2026-11-08
lang: zh
---

> 从 161 条内容中筛选出 10 条重要资讯。

<nav id="ah-toc" class="ah-toc" aria-label="目录"><span class="ah-toc-title">目录</span><ul><li><a href="#sec-harness-arch"><span class="ah-toc-name">Harness 架构</span><span class="ah-toc-count">4条</span></a></li><li><a href="#sec-agent-engineer"><span class="ah-toc-name">Agent 工程师日报</span><span class="ah-toc-count">6条</span></a></li></ul></nav>

---

**[Harness 架构](#sec-harness-arch)**
1. [ADK Python v2.14.0 发布](#item-harness-arch-1) ⭐️ 8.8/10
2. [Agent Framework Python 1.25.0 发布](#item-harness-arch-2) ⭐️ 7.8/10
3. [opencode v2.2.6 发布](#item-harness-arch-3) ⭐️ 5.5/10
4. [Cloudflare security-audit-skill 登 GitHub Trending](#item-harness-arch-4) ⭐️ 5.5/10

**[Agent 工程师日报](#sec-agent-engineer)**
1. [Anthropic 发布 Agent 记忆组件研究](#item-agent-engineer-1) ⭐️ 8.0/10
2. [Harness-S 论文提出 sibling harness 训练框架](#item-agent-engineer-2) ⭐️ 7.0/10
3. [BestRand 提出稳定低耗基准压缩](#item-agent-engineer-3) ⭐️ 7.0/10
4. [Drex 非自回归决策模型发布](#item-agent-engineer-4) ⭐️ 7.0/10
5. [EvoMemState 记忆框架论文入选 HF 日报](#item-agent-engineer-5) ⭐️ 6.0/10
6. [Obsessive-1.7B 搜索子智能体发布](#item-agent-engineer-6) ⭐️ 5.5/10

---

## Harness 架构
{: #sec-harness-arch .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-harness-arch" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-harness-arch-1"></a>
### [ADK Python v2.14.0 发布](https://github.com/google/adk-python/releases/tag/v2.14.0) ⭐️ 8.8/10

Google ADK Python v2.14.0 正式发布，核心沙箱、A2A、评估与运行时模块从实验性升级为稳定版。新增 \`MultiRunConfig\` 多轮次评估、\`ToolArgsMatcher\` 语义工具参数匹配，以及 Microsoft Teams 和 OpenAI Decisions 集成。长多轮工作流性能提升，30 节点 200 轮运行耗时降低 23%、峰值内存降低 9%。同时引入破坏性变更：Enum 工具参数改为传递成员而非原始字符串，\`VertexAiSessionService.create\_session\` 仅接受有限会话配置关键字。

github · haranrk · 11月7日 00:58

**「设计要点」** 运行时通过分块流式处理降低长多轮工作流内存峰值，30 节点 200 轮场景内存降 9%。工具层 \`ToolArgsMatcher\` 支持精确、大小写不敏感、数值容差或 LLM 语义检查，\`RunSkillScriptTool\` 改为验证路径执行；记忆层 \`MongoDbMemoryService\` 新增向量检索与 TTL；评测框架支持运行时构建图直接接入且结果可外置存储。

**「改了什么」** 相对 v2.13.0，v2.14.0 将执行环境、A2A、评估与运行时模块从实验性升级为稳定版，新增多轮次并发评估、语义工具参数匹配、Microsoft Teams 与 OpenAI Decisions 集成及 MongoDB 向量记忆，长多轮工作流 30 节点 200 轮场景耗时降 23%、内存降 9%。同步引入三项破坏性变更：Enum 工具参数改为传递成员、\`VertexAiSessionService.create\_session\` 限制关键字参数、\`RunSkillScriptTool\` 在环境模式下移除 \`command\` 参数。

**标签**: `#sandbox`, `#runtime`, `#a2a`, `#eval`, `#tools`

---

<a id="item-harness-arch-2"></a>
### [Agent Framework Python 1.25.0 发布](https://github.com/microsoft/agent-framework/releases/tag/python-1.25.0) ⭐️ 7.8/10

microsoft/agent-framework 发布 python-1.25.0。核心新增可调用 MCP 发现审批策略与 Foundry Toolbox 审批元数据细粒度控制，支持工具名/只读过滤、调用者覆盖及保留工具策略刷新。同步移除 Python 3.10 支持，要求 Python 3.11+；MCP 发现限制为每目录 100 页/1000 项，默认请求超时 30 秒；工作流执行器绑定单一授权范围并拒绝跨范围执行；OpenTelemetry 追踪对齐 GenAI 约定；Hyperlight 沙箱默认脱敏异常详情。

github · eavanvalkenburg · 11月7日 15:52

**「设计要点」** 运行时层收紧权限边界：工作流执行器绑定单一授权范围并前置拦截跨范围执行。MCP 发现默认限流（100 页/1000 项/30 秒）并支持可调用审批策略，Hyperlight 默认脱敏异常，OpenTelemetry 追踪对齐 GenAI 语义约定。

**「改了什么」** 新增可调用 MCP discovery approval policies 与 Foundry Toolbox 审批元数据控制（工具名/只读过滤器、调用者覆盖、保留工具策略刷新）。多项破坏性变更：最低 Python 版本升至 3.11，MCP 发现加页/项上限与默认超时，工作流执行器强制单授权域，OpenTelemetry span 命名切换至 gen\_ai 语义，MCP 协议会话改为每次调用新建，Foundry Local 迁移至 SDK 2.3.1，Hyperlight 默认脱敏异常。

**标签**: `#mcp`, `#permissions`, `#tools`

---

<a id="item-harness-arch-3"></a>
### [opencode v2.2.6 发布](https://github.com/anomalyco/opencode/releases/tag/v2.2.6) ⭐️ 5.5/10

opencode v2.2.6 正式发布。本次更新引入共享 MCP 连接池（\`pool: true\`）和 git worktree 支持的脚本化运行（\`opencode run -w\` / \`--worktree=&lt;name&gt;\`，不可与 \`--continue\` 或 \`--session\` 共用），同时改进了非交互式 \`opencode run\` 的后台作业等待与 SIGTERM 处理。新增 \`--archived\` 参数使脚本化与 CI 会话默认归档，跳过 \`--continue\` 并隐藏于 TUI 列表。安全方面，服务器 API 现在以沙盒下载方式提供文件读取，并限制跨域请求；实验性 Code Mode 字节码 VM 默认关闭，可通过 \`experimental.codemode\_vm\` 开启。

github · github-actions\[bot\] · 11月6日 23:37

**「设计要点」** 非交互式运行路径重写了参数解析、WebSocket 升级和服务关闭逻辑，SIGTERM 现统一取消会话及后台作业并以 143 退出。MCP 工具层增加连接等待与动态注册的 \`logo\_uri\` 传递，文件与媒体访问改为服务器端沙盒下载，从边界减少客户端直接暴露。

**「改了什么」** 新增共享 MCP 连接池、\`opencode run --worktree\` 与 \`--archived\` 参数，以及实验性 Code Mode 字节码 VM。非交互式 \`opencode run\` 现可靠等待后台作业完成，SIGTERM 统一取消会话及作业并以 143 退出。

**标签**: `#mcp`, `#runtime`, `#tools`

---

<a id="item-harness-arch-4"></a>
### [Cloudflare security-audit-skill 登 GitHub Trending](https://github.com/cloudflare/security-audit-skill) ⭐️ 5.5/10

本次 GitHub Trending 收录 Cloudflare 开源的 coding-agent skill \`security-audit-skill\`，该工具可将普通 agent 转化为安全审计器，通过编排隔离 agent 执行多阶段安全审计流程。它是 Cloudflare 漏洞发现 harness 的核心基础组件，相关实现逻辑在《Build your own vulnerability harness》中有对应描述。

rss · GitHub Trending Daily · 11月7日 23:00

**「设计要点」** 该 skill 采用多阶段隔离子 agent 编排架构，覆盖侦察、覆盖引导狩猎、候选验证、结构化输出、独立记录验证、目标中性报告全流程，最终输出机器可读、经独立验证的安全发现。

**标签**: `#tools`, `#subagents`, `#sandbox`, `#security`

---

## Agent 工程师日报
{: #sec-agent-engineer .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-agent-engineer" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-agent-engineer-1"></a>
### [Anthropic 发布 Agent 记忆组件研究](https://www.anthropic.com/research/components-of-agent-memory) ⭐️ 8.0/10

2026 年 11 月 7 日，Anthropic 发布研究博客《The Components of Agent Memory》，提出将 Agent 记忆定义为“用于预测未来需求的机制”，并分析不同记忆组件的设计权衡。该内容面向 Agent 工程领域，社区讨论中指出 wiki+搜索的记忆组合收益优于 dreaming 机制，同时多位 harness 实践者反馈自动记忆创建的实用性不足。

hackernews · geoffbp · 11月7日 06:39 · [社区讨论](https://news.ycombinator.com/item?id=50402212)

**「为什么重要」** 该研究首次从官方层面系统梳理了 Agent 记忆的组件框架与权衡，为 harness 和 Agent 编排设计提供参考基准。目前社区反馈的自动记忆管理问题，说明理论框架与实际工程落地仍存在待验证的 gap。

**「可关注」** 可关注：wiki+搜索的记忆组合在实测中收益优于 dreaming 机制，且多数 harness 自动生成的记忆仅对单次任务有效，需评估自动记忆创建的投入产出比。

**「评论」** 社区对 Anthropic 将记忆定义为“预测未来需求”存在分歧，部分用户认为该定义回避了模型无法持续学习（权重更新）的核心问题；多位 harness 使用者反馈自动记忆创建实用性低，普遍需要手动清理无效记忆以避免上下文污染。另有用户分享了自己实现的带“梦周期”的 AI 系统，长期运行后生成的梦境内容逐渐偏向无意义重复。

**标签**: `#memory`, `#harness`, `#orchestration`

---

<a id="item-agent-engineer-2"></a>
### [Harness-S 论文提出 sibling harness 训练框架](https://huggingface.co/papers/2611.04277) ⭐️ 7.0/10

Hugging Face Daily Papers 2026-11-07 介绍 Harness-S 预印本。该论文提出可泛化 agent 训练框架，利用固定 Sibling Harness Pool 修复基础 harness 执行失败，并将恢复能力迁移至单个策略。核心观察指出 harness 演化呈现 Locality、Complementarity、Nonstationarity 三属性。Directional Harness Evolution 沿不同修复方向形成该池，Complementary Harness Rescue Training 仅在基础 harness 下所有初始尝试失败时调用。该框架直接适用于 agent harness 设计与训练流程，但尚未经过生产环境验证。

rss · Hugging Face Daily Papers · 11月7日 23:00

**「为什么重要」** 论文首次系统化提出 harness 演化三属性诊断框架，为 coding agent 的 harness 组合策略提供可操作依据。其 rescue 机制表明无需追求单一最优 harness，而是通过互补专门化提升策略鲁棒性。实际效果取决于具体任务域与实现细节，需进一步实证。

**「可关注」** Harness-S 提出的 Locality、Complementarity、Nonstationarity 三属性可作为诊断现有 harness 设计有效性的检查清单，尤其适用于评估 coding agent 在失败模式分布变化时的适应能力。

**标签**: `#harness`, `#coding-agent`, `#eval`

---

<a id="item-agent-engineer-3"></a>
### [BestRand 提出稳定低耗基准压缩](https://huggingface.co/papers/2611.00883) ⭐️ 7.0/10

Hugging Face Daily Papers 2026-11-07 收录论文《Random Is Almost Enough? Stable and Low-Cost Benchmark Compression via BestRand》，提出 BestRand 基准压缩方法。论文通过分析误差分布近似，揭示随机子集采样估计全基准分数时存在长尾不稳定性：多数子集误差小，但少数子集产生远大于平均的误差。该方法面向构建高效可靠评估流程的工程师，但材料中 BestRand 具体实现细节被截断。

rss · Hugging Face Daily Papers · 11月7日 23:00

**「为什么重要」** 基准测试成本高是 agent 评估的常见瓶颈。该论文从误差分布机理层面解释随机采样的不稳定性，为设计低成本且稳定的评估流程提供了理论依据。

**「可关注」** 可关注：随机子集采样在基准压缩中多数情况有效，但长尾大误差不可忽视，需引入稳定机制。

**标签**: `#eval`

---

<a id="item-agent-engineer-4"></a>
### [Drex 非自回归决策模型发布](https://huggingface.co/papers/2611.07854) ⭐️ 7.0/10

Hugging Face Daily Papers 于 2026-11-07 推介 Drex 开放非自回归决策模型家族，包含 8B \(DLM\)、9B \(v1.5\)、35B with 3B active \(v2.0\)、27B \(Max\) 四个规格。该家族针对自回归 LLM 链式思考在 agent 决策任务中的不一致输出、解析开销与高成本/延迟问题，输入状态（文档、记录或 agent 上下文，可选带图像）及问题后，直接返回选项上的概率分布，无需自回归解码。目前材料未提供具体准确率、延迟对比数字或开源许可证细节。

rss · Hugging Face Daily Papers · 11月7日 23:00

**「为什么重要」** 非自回归决策形式若成立，可降低 agent 推理链的解析复杂度与端到端时延，但材料未给出与 autoregressive baseline 的量化对比，实际收益仍待验证。

**「可关注」** 可关注：Drex 的选项概率输出可能减少 agent harness 中的输出解析代码量，但需确认其在不同离散决策任务上的准确率是否满足替换 LLM chain-of-thought 的阈值。

**标签**: `#orchestration`, `#coding-agent`, `#harness`

---

<a id="item-agent-engineer-5"></a>
### [EvoMemState 记忆框架论文入选 HF 日报](https://huggingface.co/papers/2611.03743) ⭐️ 6.0/10

2026 年 11 月 7 日，Hugging Face Daily Papers 收录 arXiv 论文 2611.03743，提出面向个人 LLM Agent 的状态中心记忆框架 EvoMemState，该论文在 HF Daily Papers 获 26 次 upvote。该框架在传统事实记忆之外新增关系状态与推理状态，用于建模随用户交互演化的信息。当前公开内容仅为截断摘要，无具体技术细节、性能数据、实现信息或评估结果。

rss · Hugging Face Daily Papers · 11月7日 23:00

**标签**: `#memory`

---

<a id="item-agent-engineer-6"></a>
### [Obsessive-1.7B 搜索子智能体发布](https://www.reddit.com/r/LocalLLaMA/comments/1xq4yju/obsessive17b_a_11_gb_websearch_subagent/) ⭐️ 5.5/10

2026 年 11 月 7 日，Reddit 用户/u/MuzafferMahi 开源了基于 LFM3-1.7B 微调的 Obsessive-1.7B 搜索子智能体，模型体积 1.1GB，定位为上层大模型的子智能体，执行单次网页搜索任务，输出短答案、原文引语和来源 URL，搜索结果无答案时返回固定提示。训练采用 LoRA rank 16，使用约 9k 条工具调用对话在 RTX 4060 笔记本上完成，训练数据为维基百科和 FineWeb 的搜索结果，要求答案与引语逐字匹配，约四分之一样本用于训练“未找到”的返回逻辑。发布者自报的固定结果基准（131 道 SimpleQA 留出题，其中 29 道答案被从搜索结果中移除）显示：基础模型找到答案率为 50%，Obsessive 找到答案时正确返回、无答案时返回“未找到”的比例为 0%，编造答案的比例为 10%，单题平均耗时 5.1 秒；实时维基搜索基准（120 道题+40 道多事实请求，搜索后端为训练时未接触过的）显示：返回任意回复的比例为 38%，回复中正确答案占比 37/120，多事实请求仅答对 1/40，编造事实值 4 次。已知限制包括：仅支持单轮对话，多轮会混淆；仅支持英语；约 1/10 实际存在于结果中的答案会被误判为未找到；偶尔引用相邻年份等相邻事实；会将“X 声称解决 Y”直接报告为肯定事实。所有基准结果均为发布者自报，无第三方验证，模型未经过官方发布，仅开源了 Hugging Face 上的 GGUF 格式文件。

reddit · r/LocalLLaMA · /u/MuzafferMahi · 11月7日 12:13

**「为什么重要」** 它提供了一个轻量级单工具调用子智能体的可参考实现，验证了 1.7B 参数级小模型在限定场景下可通过低消费级硬件完成微调并具备可用性，但自报基准未经第三方验证，实际效果依赖上层编排逻辑和搜索后端，目前无官方评估流程。

**「可关注」** 可关注：1.7B 参数小模型在强制单次工具调用、要求逐字引用来源的限定场景下，可通过低秩微调（LoRA rank 16、9k 样本、RTX 4060 训练）实现基础可用性，但需处理单轮限制、事实归因偏差、答案漏判等已知缺陷。

**标签**: `#eval`, `#orchestration`

---