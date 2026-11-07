---
layout: default
title: "Horizon Summary: 2026-11-08 (EN)"
date: 2026-11-08
lang: en
---

> From 161 items, 10 important content pieces were selected

---

**Agent Harness Architecture**
1. [ADK Python v2.14.0 发布](#item-harness-arch-1) ⭐️ 8.8/10
2. [Agent Framework Python 1.25.0 发布](#item-harness-arch-2) ⭐️ 7.8/10
3. [OpenCode v2.2.6 发布](#item-harness-arch-3) ⭐️ 5.5/10
4. [Cloudflare 发布安全审计技能](#item-harness-arch-4) ⭐️ 5.5/10

**AI Agent Engineer**
1. [Anthropic 记忆组件研究发布](#item-agent-engineer-1) ⭐️ 8.0/10
2. [Harness-S 利用 sibling harnesses 改进 agent 训练](#item-agent-engineer-2) ⭐️ 7.0/10
3. [BestRand 稳定低开销评测压缩方案](#item-agent-engineer-3) ⭐️ 7.0/10
4. [Drex 非自回归决策模型开源](#item-agent-engineer-4) ⭐️ 7.0/10
5. [EvoMemState 状态记忆框架提出](#item-agent-engineer-5) ⭐️ 6.0/10
6. [Obsessive-1.7B 搜索子代理开源](#item-agent-engineer-6) ⭐️ 5.5/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [ADK Python v2.14.0 发布](https://github.com/google/adk-python/releases/tag/v2.14.0) ⭐️ 8.8/10

Google ADK Python v2.14.0 is released, graduating execution environments, A2A, evaluation, and core runtime modules from experimental to stable. It adds multi-run evaluation via \`MultiRunConfig\`, semantic tool argument matching via \`ToolArgsMatcher\`, and new integrations for Microsoft Teams and OpenAI Decisions. Long multi-turn workflows see a 23% speedup and 9% lower peak memory on a 30-node, 200-turn benchmark.

github · haranrk · Nov 7, 00:58

**「设计要点」** The release stabilizes the environment abstraction layer with chunked file streaming and timeout handling, and adds vector search to \`MongoDbMemoryService\`. Evaluation and tool layers gain parallel multi-run scoring and LLM-backed semantic argument comparison.

**「改了什么」** Key capability changes include: stable graduation of 26 auth/environment/app/CLI/cache modules and 16 toolset/integration features; new \`adk eval --num\_runs\` with \`--parallelism\` for concurrent multi-run scoring; \`ToolArgsMatcher\` for evaluation and simulation; \`TeamsRunner\` and \`OpenAIDecisionsClassifier\` integrations; chunked file streaming via \`BaseEnvironment.read\_file\_stream\` and chunked large-file I/O for \`AgentEngineEnvironment\`; and \`ContainerCodeExecutor\` input/output file support. Breaking changes require \`Enum\` tool arguments to arrive as members, restrict \`VertexAiSessionService.create\_session\` kwargs to \`display\_name\`, \`ttl\`, \`expire\_time\`, and \`labels\`, and remove the \`command\` parameter from \`RunSkillScriptTool\` in environment mode.

**Tags**: `#sandbox`, `#runtime`, `#a2a`, `#eval`, `#tools`

---

<a id="item-harness-arch-2"></a>
### [Agent Framework Python 1.25.0 发布](https://github.com/microsoft/agent-framework/releases/tag/python-1.25.0) ⭐️ 7.8/10

微软发布 agent-framework Python 1.25.0。核心新增可调用 MCP 发现审批策略，以及 Foundry Toolbox 细粒度审批元数据控制，支持工具名/只读过滤器、调用方覆盖和保留工具策略刷新。该版本包含多项破坏性变更：最低 Python 版本提升至 3.11，MCP 发现默认限制 100 页/1000 项，工作流执行器绑定单一授权范围，OpenTelemetry 跨度命名对齐 GenAI 规范，声明式 MCP 会话强制隔离，Foundry Local 迁移至 SDK 2.3.1，Hyperlight 沙箱异常详情脱敏。

github · eavanvalkenburg · Nov 7, 15:52

**「设计要点」** 运行时层面，工作流执行器与会话绑定单一授权范围，模型调用前拦截跨域执行。工具层新增可调用 MCP 发现审批策略，支持工具名/只读过滤、调用方覆盖及保留工具策略刷新；声明式 MCP 每次调用创建新协议会话，消除跨工作流状态共享。

**「改了什么」** 新增可调用 MCP 发现审批策略与 Foundry Toolbox 细粒度审批元数据控制。多项破坏性变更落地：移除 Python 3.10 支持，MCP 发现分页/条目数默认限制 100/1000，工作流执行器跨域执行拦截，OpenTelemetry 跨度命名切换至 gen\_ai.operation.name，声明式 MCP 会话缓存移除，Foundry Local 升级至 SDK 2.3.1，Hyperlight 异常详情默认脱敏。

**Tags**: `#mcp`, `#permissions`, `#tools`

---

<a id="item-harness-arch-3"></a>
### [OpenCode v2.2.6 发布](https://github.com/anomalyco/opencode/releases/tag/v2.2.6) ⭐️ 5.5/10

OpenCode v2.2.6 正式发布。新增共享 MCP 连接池。通过 \`pool: true\` 跨项目复用连接。减少进程开销并加快启动。\`opencode run\` 新增 \`--worktree\`（\`-w\`）参数。支持在 git worktree 中启动会话。另有 \`--archived\` 参数自动归档 CI 运行。非交互式运行重构后可靠等待后台任务。处理 SIGTERM 取消。服务器 API 收紧跨域与凭据过滤。

github · github-actions\[bot\] · Nov 6, 23:37

**「设计要点」** MCP 连接池跨项目复用同一连接。模型调用前最多等待 2 秒。确保快速连接的服务器工具可达。非交互式运行等待后台任务完成。SIGTERM 级联取消会话及任务。返回退出码 143。服务器 API 以沙盒下载提供文件，拒绝跨站请求。

**「改了什么」** 新增 \`opencode run --worktree\`（\`-w\`）与 \`--archived\` 参数。支持 git worktree 会话，但不可与 \`--continue\` 或 \`--session\` 组合。自动归档 CI 运行。MCP 连接池通过 \`pool: true\` 跨项目共享连接，减少进程数。非交互式运行重构后可靠等待后台任务、处理 SIGTERM 取消，并收紧 \`/api/\*\` 跨域与凭据过滤。

**Tags**: `#mcp`, `#runtime`, `#tools`

---

<a id="item-harness-arch-4"></a>
### [Cloudflare 发布安全审计技能](https://github.com/cloudflare/security-audit-skill) ⭐️ 5.5/10

Cloudflare 发布 security-audit-skill。这是一个 coding-agent 技能，可将 agent 转变为安全审计员。技能编排隔离 agent 执行多阶段审计流程。流程包括侦察、覆盖驱动狩猎、候选验证、结构化输出、独立记录验证和目标中性报告。该技能曾作为 Cloudflare 漏洞发现 harness 的基础。

rss · GitHub Trending Daily · Nov 7, 23:00

**「设计要点」** 技能采用多阶段流水线架构。各阶段由独立隔离的 agent 执行。阶段间输出结构化结果。最终通过独立记录验证确保发现可信度。生成目标中性的机器可读报告。

**「改了什么」** 该技能现已发布。它曾作为 Cloudflare 漏洞发现 harness 的基础。agent 可使用该技能自主完成从侦察到报告的全流程安全审计。

**Tags**: `#tools`, `#subagents`, `#sandbox`, `#security`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [Anthropic 记忆组件研究发布](https://www.anthropic.com/research/components-of-agent-memory) ⭐️ 8.0/10

Anthropic 于 2026-11-07 由 geoffbp 发布研究博客《The Components of Agent Memory》。文章提出将 agent memory 定义为预测未来需求，并分析多种记忆机制。社区讨论聚焦 coding harness 中自动记忆创建与删除的实际问题，涉及 harness 开发者与 agent 工程师。原文未提供，具体机制细节无法核实。

hackernews · geoffbp · Nov 7, 06:39 · [Discussion](https://news.ycombinator.com/item?id=50402212)

**「为什么重要」** 该文直接回应 agent 工程中的记忆架构设计问题，社区反馈揭示理论定义与 harness 实践之间的张力。尚未证实这些机制是否可迁移到现有 coding agent 工作流。

**「可关注」** 可关注：自动记忆创建在 harness 中常产生仅对当前任务有效的噪声，工程师普遍关闭该功能或删除 95% 以上记忆。

**「评论」** 社区对“记忆即预测未来需求”的定义存在分歧，aszen 认为这回避了模型无法持续学习的根本问题。andai 据 fig. 10 称 wiki 加搜索优于 dreaming，yfontana 则反馈自动记忆多为当前任务而建且 95% 被删除。

**Tags**: `#memory`, `#harness`, `#orchestration`

---

<a id="item-agent-engineer-2"></a>
### [Harness-S 利用 sibling harnesses 改进 agent 训练](https://huggingface.co/papers/2611.04277) ⭐️ 7.0/10

2026-11-07，Hugging Face Daily Papers 发布论文《Harness-S: Learning from Sibling Harnesses for Generalizable Agent Training》。该论文提出 Harness-S 训练框架，针对从共同基座演化出的 harness 变体识别出局部性、互补性和非平稳性三个核心属性，设计固定专业 sibling harness 池在基础执行失败时进行救援，并将恢复的能力迁移到单个策略中。Directional Harness Evolution 沿不同修复方向开发专门 sibling harnesses，Complementary Harness Rescue Training 仅在基础 harness 下所有初始尝试失败时调用该池。该研究为 coding agent 的 harness 设计和训练流程提供新思路，但仍是预印本，尚未在主流工具中落地。

rss · Hugging Face Daily Papers · Nov 7, 23:00

**「为什么重要」** 该研究首次系统化识别了 harness 演化的三个可复用属性，并给出可操作的训练框架，直接影响 coding agent 的 harness 设计和评估系统构建。但论文尚未经过大规模生产环境验证，其泛化声明仍需更多实验支撑。

**「可关注」** 可关注：Harness-S 的互补救援机制提示，在 agent 训练中维护一个固定但多样化的 sibling harness 池，可能比持续优化单一 harness 更有效地覆盖失败模式。

**Tags**: `#harness`, `#coding-agent`, `#eval`

---

<a id="item-agent-engineer-3"></a>
### [BestRand 稳定低开销评测压缩方案](https://huggingface.co/papers/2611.00883) ⭐️ 7.0/10

2026-11-07，Hugging Face Daily Papers 收录论文《Random Is Almost Enough? Stable and Low-Cost Benchmark Compression via BestRand》，提出 BestRand 评测基准压缩方法。该工作推导出从子集估计全基准得分的误差分布解析近似。随机子集采样存在长尾不稳定性：多数子集误差小，但少数子集产生大幅误差。论文进一步指出该不稳定性是现代基础模型固有特性，即使评估更多模型仍持续存在。当前来源内容截断于方法介绍部分，完整算法细节未披露。

rss · Hugging Face Daily Papers · Nov 7, 23:00

**「为什么重要」** 该工作直接针对 agent 工程师构建高效可靠评测流程的需求。它证明随机采样在概率意义上已接近足够，但长尾误差导致稳定性不足，这对追求可重复、低成本 eval 的工程实践有直接指导意义。尚未证实 BestRand 在具体 agent 任务上的实际收益。

**「可关注」** 可关注：随机子集采样的长尾误差分布表明，仅靠增加采样次数无法根除不稳定。工程上需设计显式稳定性机制。

**Tags**: `#eval`

---

<a id="item-agent-engineer-4"></a>
### [Drex 非自回归决策模型开源](https://huggingface.co/papers/2611.07854) ⭐️ 7.0/10

2026-11-07，Hugging Face Daily Papers 推介 Drex。Drex 是开源非自回归决策模型家族。定位为自回归 LLM 链式思维在离散选项决策任务上的替代方案。包含四款尺寸：8B（DLM）、9B（v1.5）、35B 总参数 / 3B 激活（v2.0）及 27B（Max）。输入支持 agent 上下文与多模态（可选图像），输出为选项概率分布。材料指其可缓解自回归方案的不一致输出、解析开销与高成本延迟问题，但未提供独立复现的精度或延迟基准数据。

rss · Hugging Face Daily Papers · Nov 7, 23:00

**「为什么重要」** 该工作直接针对生产级 agent 系统中 LLM 推理的稳定性与成本痛点，提供了一条可量化的架构优化路径。但实际部署收益取决于具体任务场景，材料未给出端到端延迟或精度对比的独立验证。

**「可关注」** 可关注：Drex 以非自回归方式直接输出选项概率分布，理论上可省去 LLM 链式思维的解析步骤。v2.0 的 35B 总参数 / 3B 激活配置提示稀疏架构可能用于决策模型。但实际延迟与精度权衡需对照基线验证。

**Tags**: `#orchestration`, `#coding-agent`, `#harness`

---

<a id="item-agent-engineer-5"></a>
### [EvoMemState 状态记忆框架提出](https://huggingface.co/papers/2611.03743) ⭐️ 6.0/10

2026-11-07，Hugging Face Daily Papers spotlight arXiv 论文 2611.03743，提出 EvoMemState 状态记忆框架。该框架为个人 LLM agent 设计，在传统事实记忆之外新增关系状态与推理状态，以建模动态用户信息。当前公开材料仅为截断摘要，未披露具体技术实现、性能对比或评估数据，当日 upvote 数为 26。需阅读完整论文才能判断其对 agent 记忆系统的实际改进。

rss · Hugging Face Daily Papers · Nov 7, 23:00

**「为什么重要」** 该工作试图弥补事实记忆在动态用户信息建模中的不足，但摘要未提供可验证的性能增益或适用场景边界。对 coding agent 工程而言，需等待完整论文的复现细节与基准测试结果，才能评估是否值得纳入记忆模块设计。

**「可关注」** 可关注：当前公开信息仅含概念框架，缺乏实现代码与量化评估，尚不能转化为工程实践。

**Tags**: `#memory`

---

<a id="item-agent-engineer-6"></a>
### [Obsessive-1.7B 搜索子代理开源](https://www.reddit.com/r/LocalLLaMA/comments/1xq4yju/obsessive17b_a_11_gb_websearch_subagent/) ⭐️ 5.5/10

On 2026-11-07, Reddit user /u/MuzafferMahi open-sourced Obsessive-1.7B, a 1.1GB web-search subagent fine-tuned from LFM3-1.7B. It is designed to run as a subagent under a larger model, performing exactly one web\_search call per factual query, then returning a short answer, verbatim quote, and source URL, or a fixed &\#x27;Not found in the search results&\#x27; prompt if no match exists. The model was trained with LoRA rank 16 on ~9k tool-calling conversations on an RTX 4060 laptop, using Wikipedia and FineWeb search results with all answers and quotes verified verbatim, roughly a quarter of training data teaching the &\#x27;not found&\#x27; behavior. The model is hosted on Hugging Face as banyohavlusu23/Obsessive-1.7B-GGUF, with run configs for Pi, OpenCode and Hermes provided, and can be launched via llama-server -hf banyohavlusu23/Obsessive-1.7B-GGUF --jinja -c 16384 with temperature set to 0. Known limitations include English-only support, single-turn only \(multi-turn input degrades performance\), ~1 in 10 actually present answers being misclassified as not found, and occasional quoting of adjacent unrelated facts. Self-reported fixed-results benchmark \(131 held-out SimpleQA questions, 29 with answers removed from search results\): 50% answer found when present, 0% false positive &\#x27;not found&\#x27; when absent, 10% hallucinated answers, median 5.1s per question on 4060 laptop. Self-reported live Wikipedia search benchmark \(120 questions + 40 multi-fact requests on an unseen search backend\): 37/120 correct answers, 1/40 multi-fact requests correct, 4 hallucinated fact values. All benchmark results are self-reported by the author, with no third-party verification or official verifiable artifacts released.

reddit · r/LocalLLaMA · /u/MuzafferMahi · Nov 7, 12:13

**「为什么重要」** It offers a reference implementation of a lightweight 1.1GB single-search subagent, validating that small-parameter models can be tuned for narrow, well-defined tool-use tasks; however, its unverified self-reported benchmarks and narrow use case scope mean it currently has no proven large-scale impact beyond community experimentation.

**「可关注」** Note that constraining subagents to single search calls and enforcing verbatim source quoting can reduce hallucination rates, but there is a clear tradeoff between single-call recall and the higher recall of base models that run multi-turn search, which must be weighed against specific orchestration requirements.

**Tags**: `#eval`, `#orchestration`

---