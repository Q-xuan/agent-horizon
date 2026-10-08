---
layout: default
title: "Horizon Summary: 2026-10-08 (ZH)"
date: 2026-10-08
lang: zh
---

> 从 208 条内容中筛选出 21 条重要资讯。

---

**Harness 架构**
1. [anthropics/claude-code released v2.1.293](#item-harness-arch-1) ⭐️ 8.3/10
2. [Codex rust-v0.161.0 发布](#item-harness-arch-2) ⭐️ 8.3/10
3. [Cloudflare Agents v0.27.0 发布](#item-harness-arch-3) ⭐️ 8.3/10
4. [Claude Code 2.1.293 发布](#item-harness-arch-4) ⭐️ 8.3/10
5. [Cline SDK v0.0.91 发布](#item-harness-arch-5) ⭐️ 7.8/10
6. [Mastra 1.75.0 发布](#item-harness-arch-6) ⭐️ 7.8/10
7. [crewAIInc/crewAI released 1.15.24](#item-harness-arch-7) ⭐️ 6.8/10

**Agent 工程师日报**
1. [One Model Family, Two Gold-Level Results: Fine-Tuning Nemotron for IOI and IMO](#item-agent-engineer-1) ⭐️ 8.3/10
2. [HF daily paper: DecepEval: A Benchmark for Evaluating Deception in LLM Agents](#item-agent-engineer-2) ⭐️ 8.0/10
3. [nanoMuse 开源个人智能体发布](#item-agent-engineer-3) ⭐️ 7.5/10
4. [Haiku 5.5 发布，定价分层](#item-agent-engineer-4) ⭐️ 7.0/10
5. [HF daily paper: Mechanics of Long-Context Hybrid Models Part 1.1: From Hybrid Attention to Hybrid Position](#item-agent-engineer-5) ⭐️ 7.0/10
6. [Claude Haiku 5.5 发布](#item-agent-engineer-6) ⭐️ 6.5/10
7. [HF 论文：自进化推理模型自训练崩溃机制](#item-agent-engineer-7) ⭐️ 6.5/10
8. [Liquid AI 开源 d1 边缘决策模型](#item-agent-engineer-8) ⭐️ 6.3/10
9. [Cloudflare 安全运营 harness](#item-agent-engineer-9) ⭐️ 6.3/10

**AI 日报**
1. [OpenAI 为 Teens 增加学习功能](#item-ai-daily-1) ⭐️ 8.3/10
2. [Secret protection must scale with software](#item-ai-daily-2) ⭐️ 6.3/10

**AI 羊毛**
1. [Claude Max/Team 计划含 API 额度](#item-ai-deals-1) ⭐️ 7.0/10
2. [Claude: Monthly API credits for Max and Team plans](#item-ai-deals-2) ⭐️ 6.0/10
3. [Claude Max and Teams plans now forced to API \(Oct 7th update\)](#item-ai-deals-3) ⭐️ 5.0/10

---

## Harness 架构

<a id="item-harness-arch-1"></a>
### [anthropics/claude-code released v2.1.293](https://github.com/anthropics/claude-code/releases/tag/v2.1.293) ⭐️ 8.3/10

Claude Code v2.1.293 adds Haiku 5.5 as the default Haiku model, extends subagent status and tool registration APIs, and fixes context compaction, MCP memory leak, and background session message loss bugs.

github · ashwin-ant · 10月7日 18:10

**标签**: `#runtime`, `#tools`, `#mcp`, `#subagents`, `#memory`

---

<a id="item-harness-arch-2"></a>
### [Codex rust-v0.161.0 发布](https://github.com/openai/codex/releases/tag/rust-v0.161.0) ⭐️ 8.3/10

Codex Rust v0.161.0 发布。新增终端内 MCP 服务器登录 \`/mcp login &lt;name&gt;\`，Bedrock 支持 multi-agent V2 与 Ultra reasoning，GPT-6.1 Sol 成为默认模型。Daybreak 与 Cyber routing 改为显式 opt-in，需 \`cli\_daybreak\` 标志及符合条件的 ChatGPT 登录。修复文件系统升级、线程恢复与重试逻辑。

github · github-actions\[bot\] · 10月7日 15:58

**「设计要点」** 权限模型细化：批准的文件系统升级可扩大写访问，同时保留拒绝的读取和网络限制；后台任务继承发起回合的权限。线程恢复返回权威重放历史，启动时检测 SQLite 损坏并备份。

**「改了什么」** 新增 \`/mcp login\` 终端登录 MCP 服务器，Bedrock 接入 multi-agent V2 与 Ultra reasoning，Daybreak/Cyber routing 改为显式 opt-in 并默认隐藏控件。

**标签**: `#runtime`, `#tools`, `#mcp`, `#subagents`, `#planning`

---

<a id="item-harness-arch-3"></a>
### [Cloudflare Agents v0.27.0 发布](https://github.com/cloudflare/agents/releases/tag/agents%400.27.0) ⭐️ 8.3/10

Cloudflare Agents v0.27.0 发布，新增四个实验性 harness 和 web\_search 工具，并将 Channels API 重构为以对话和回合为中心。AiSdkHarness、ThinkHarness、ContainerHarness 和 OpenCodeHarness 与 PiHarness 同形，其中 ContainerHarness 可在容器中运行 Claude Code 或 Codex。agents/websearch 为 pi、AI SDK 和 TanStack AI 提供基于 Cloudflare Web Search API 的 web\_search 工具。Channels 从 agents/channels 迁移到 agents/experimental/channels，旧入口已移除。

github · github-actions\[bot\] · 10月7日 13:25

**「设计要点」** Channels 作为 Lifecycle capability，通过 Channels.forHarness 将 harness 的会话暴露为对话，依赖 Streams 提供可恢复响应。ChannelGateway 作为 Worker 入口验证 webhook 并路由到持有对话的 agent object，agent object 即授权边界，默认每个参与者独立，route 回调可共享或拒绝。

**「改了什么」** 相对上一版，harness 层扩展到 AI SDK、思考、容器和 OpenCode 四种形态，工具层新增 web\_search，Channels 从稳定入口降级为实验性并重写为对话/回合模型，同时提供 Web Channel、AI SDK ChatTransport 和 npx agents tui 终端客户端。

**标签**: `#runtime`, `#tools`, `#sandbox`, `#mcp`

---

<a id="item-harness-arch-4"></a>
### [Claude Code 2.1.293 发布](https://code.claude.com/docs/en/changelog#2-1-293) ⭐️ 8.3/10

Claude Code 2.1.293 发布。默认 Haiku 模型换为 claude-haiku-5-5，支持 1M 上下文，输入/输出价格为 $0.10/$0.50 per Mtok，超过 100K 的 prompt 为 $0.50/$2.50。subagentStatusLine payload 增加 agentType，$.tool.register 增加 isDeferred，mod 可让工具 schema 从起始就进入 prompt，而不是只在 tool search 后可见。修复上下文压缩后 Claude 把压缩前最后动作当作已完成而重做或撤回、HTTP MCP 连接保留全部已发请求的内存泄漏，以及 ← 把会话转后台时丢失正在处理中收到的消息。

rss · Claude Code Changelog · 10月7日 18:26

**「设计要点」** 工具层用 isDeferred 控制 schema 曝光：false 让工具 schema 从起始进入 prompt，而不是放在 tool search 之后；subagentStatusLine 带 agentType，脚本可区分自定义 subagent 类型。

**「改了什么」** 新增 claude-haiku-5-5 为默认 Haiku 模型；subagentStatusLine 增加 agentType，$.tool.register 增加 isDeferred；修复上下文压缩后重做或撤回已完成工作、HTTP MCP 连接请求堆积、后台会话丢消息等运行时问题。

**标签**: `#runtime`, `#tools`, `#mcp`, `#subagents`, `#memory`

---

<a id="item-harness-arch-5"></a>
### [Cline SDK v0.0.91 发布](https://github.com/cline/cline/releases/tag/sdk/sdk/v0.0.91) ⭐️ 7.8/10

Cline SDK v0.0.91 收紧 agent loop 的完成判定与 MCP 握手容错。finish reason 缺失或未识别时不再视为成功结束，状态机新增 unknown 态，无工具活动下允许一次隐藏消息重试，第二次失败即终止。stdio MCP initialize 超时从 3s 提高到 10s，避免 Windows 下 npx/uvx 启动被静默丢弃。Anthropic provider 将 server-side fallbacks 限定在官方端点，自定义端点不再触发 400。

github · github-actions\[bot\] · 10月7日 06:00

**「设计要点」** 运行时在请求边界统一消耗排队用户消息，包括首次迭代，保证状态机推进与输入消费同步。工具层把 MCP 握手超时作为可覆盖默认值，显式 timeout 优先。适配层按 provider 声明 apiKeyOptional 与官方端点判定，把协议差异收敛在 provider fact 里。

**「改了什么」** finish-reason 状态机区分 unknown 与 stop，增加单次隐藏消息重试。stdio MCP initialize 默认预算升至 10s。Anthropic server-side fallbacks 仅对 api.anthropic.com 开启。portable reasoning level 对齐模型 advertised effort levels，修复 Kimi K3 等模型的参数拒绝。OpenAI-compatible 适配器统一 camelCase providerOptions，消除弃用警告。新增 apiKeyOptional provider fact 与 Langfuse BYOK tracing 开关。

**标签**: `#runtime`, `#mcp`, `#tools`

---

<a id="item-harness-arch-6"></a>
### [Mastra 1.75.0 发布](https://github.com/mastra-ai/mastra/releases/tag/%40mastra/core%401.75.0) ⭐️ 7.8/10

Mastra 1.75.0 发布，核心包 @mastra/core 升至 1.75.0。新增 Span Query API，可通过 storage.querySpans\(\)、client.querySpans\(\) 或 POST /api/observability/spans/query 直接查询已完成的 span，支持过滤、游标、预览与模型成本，无需先定位 trace。aggregateTraces\(\) 增加 token 与 cost 度量，覆盖 ClickHouse、DuckDB、Postgres 可观测性存储。语义召回支持自嵌入向量存储，MastraVector.isSelfEmbedding 为 true 时无需客户端 embedder。

github · Patrycja-J · 10月7日 16:17

**「设计要点」** 可观测性从 trace 级下沉到 span 级，查询与聚合在存储层统一实现；记忆层通过 isSelfEmbedding 把嵌入生成下沉到向量存储，客户端 embedder 变为可选且仍优先。

**「改了什么」** 相对旧版，新增 span 查询与跨存储 token/cost 聚合，语义召回可运行在自嵌入存储上；@mastra/connect 进入 1.0，providers 取代 integrations，发现的 MCP 工具默认不再需要审批。会话默认每线程只保留一个当前模型，并支持 createInitialThread: false 免建空线程。

**标签**: `#runtime`, `#memory`, `#eval`

---

<a id="item-harness-arch-7"></a>
### [crewAIInc/crewAI released 1.15.24](https://github.com/crewAIInc/crewAI/releases/tag/1.15.24) ⭐️ 6.8/10

crewAI 1.15.24 adds experimental job lifecycle and runner, eval model overlay support, and Oracle integrations, alongside message summarization and context window refactoring.

github · lorenzejay · 10月7日 17:39

**标签**: `#eval`, `#runtime`, `#tools`, `#memory`

---

## Agent 工程师日报

<a id="item-agent-engineer-1"></a>
### [One Model Family, Two Gold-Level Results: Fine-Tuning Nemotron for IOI and IMO](https://huggingface.co/blog/nvidia/nemotron-ioi-and-imo-2026) ⭐️ 8.3/10

Nemotron 3 achieves gold-medal level at IOI and IMO 2026 via supervised fine-tuning, reinforcement learning, and feedback-driven inference, with detailed scores and system designs disclosed in an official blog post.

rss · Hugging Face Blog · 10月7日 12:45

**标签**: `#eval`, `#coding-agent`, `#orchestration`

---

<a id="item-agent-engineer-2"></a>
### [HF daily paper: DecepEval: A Benchmark for Evaluating Deception in LLM Agents](https://huggingface.co/papers/2610.07967) ⭐️ 8.0/10

DecepEval introduces a 1,532-instance benchmark and a four-condition framework to systematically evaluate when LLM agents are likely to deceive, offering a new tool for agent reliability assessment.

rss · Hugging Face Daily Papers · 10月8日 00:00

**标签**: `#eval`, `#agent`, `#benchmark`, `#safety`

---

<a id="item-agent-engineer-3"></a>
### [nanoMuse 开源个人智能体发布](https://huggingface.co/papers/2610.08699) ⭐️ 7.5/10

2026 年 9 月，Meta 发布 Muse。该智能体面向单一个体，可操作账户与设备，跨周记忆，主动开口，并回应自身行为；它闭源，托管在单一国家的一家云厂商。论文用五个问题与三个视界定义个人智能体，建立评估框架，依据 Meta 公开记录及一份生产 prompt 副本逐条溯源 Muse 架构，随后给出开源实现 nanoMuse，采用 GPL-3.0，可在每台设备本地运行。论文未展示基准突破或协议变更，对 agent 架构、记忆与工具有实际参考价值。

rss · Hugging Face Daily Papers · 10月8日 00:00

**「为什么重要」** Muse 此前没有开源对应物。nanoMuse 提供可本地部署的替代实现，工程师能直接研究个人智能体的记忆、工具与编排设计。

**「可关注」** 可关注：nanoMuse 以 GPL-3.0 开源，可在每台设备本地运行，与闭源且托管于单一国家云厂商的 Muse 形成对照，对 agent 架构、记忆与工具有实际参考价值。

**标签**: `#harness`, `#memory`, `#orchestration`, `#eval`

---

<a id="item-agent-engineer-4"></a>
### [Haiku 5.5 发布，定价分层](https://www.anthropic.com/claude-haiku-5-5) ⭐️ 7.0/10

Anthropic 发布 Claude Haiku 5.5。社区实测显示，该模型在 DataAnalyticsBench 上较 Haiku 4.5 便宜 9 倍且成绩高两个字母等级，也是默认速度下完成测试最快的模型；定价以 100k tokens 为界，输入 $0.10/$0.50 每 MTok，输出 $0.50/$2.50 每 MTok。不同 thinking level 的成本与延迟差异显著，low 档约 0.0936 美分、7 秒，max 档约 3.3826 美分、5 分 9 秒。评论提及 Max 与 Team 订阅用户将获得每月 API 额度。

hackernews · sfkgtbor · 10月7日 18:01 · [社区讨论](https://news.ycombinator.com/item?id=49996437)

**「为什么重要」** 对 agent 工程师而言，Haiku 5.5 的低价与速度分层提供了新的成本-延迟选择空间，但 100k tokens 的定价分档对长上下文 agent 场景构成明显限制，需重新评估预算模型。

**「可关注」** 可关注：100k tokens 的定价断点对 agent 场景偏低，长上下文任务可能迅速触发高价档；同时 thinking level 的延迟跨度极大，需按任务类型选择档位。

**「评论」** simonw 测试不同 thinking level 的 SVG 生成，low 档画错自行车车架但仅 7 秒、0.0936 美分，max 档正确但耗时 5 分 9 秒、3.3826 美分。minimaxir 认为 100k tokens 定价断点过低，且仅 Haiku 适用。chriddyp 的基准显示其比 Haiku 4.5 便宜 9 倍、成绩高两个字母等级。

**标签**: `#coding-agent`, `#eval`, `#observability`, `#harness`

---

<a id="item-agent-engineer-5"></a>
### [HF daily paper: Mechanics of Long-Context Hybrid Models Part 1.1: From Hybrid Attention to Hybrid Position](https://huggingface.co/papers/2610.10114) ⭐️ 7.0/10

A research paper analyzing hybrid attention architectures for long-context LLMs, identifying a &\#x27;Seesaw Effect&\#x27; where linear-attention hybrids benefit more from continual pretraining while sliding-window hybrids perform better under length extrapolation.

rss · Hugging Face Daily Papers · 10月8日 00:00

**标签**: `#memory`, `#eval`, `#architecture`

---

<a id="item-agent-engineer-6"></a>
### [Claude Haiku 5.5 发布](https://simonwillison.net/2026/Oct/7/claude-haiku-5-5/) ⭐️ 6.5/10

Anthropic 发布 Claude Haiku 5.5，输入/输出定价 $0.10/$0.50 每百万 token，与 GPT-6 Luna 持平至 100,000 token；超过后涨至 $0.50/$2.50，Luna 则到 272,000 token 才涨至 $0.20/$0.75。新模型换用新 tokenizer，相同长提示比 Haiku 4.5 多消耗约 1.25 倍 token，形成隐性涨价；且无法关闭推理，默认 medium。100,000 token 内 Haiku 5.5 与 Luna 同价且基准分更高，超出后 Luna 更划算。Anthropic 同时将 Sonnet 5.5 缓存读取价格减半，并向 Max 和 Team 订阅者发放每月 API 额度（$100/$200/最高 $500），额度不结转。

rss · Simon Willison · 10月7日 20:56

**「为什么重要」** 对 coding agent 与 harness 团队，100,000 token 是新的关键阈值；短上下文任务可直接对标 Luna，长上下文流水线则需同时核算阶梯价差与 tokenizer 膨胀。

**「可关注」** 可关注：上下文稳定在 100,000 token 内的任务可切换至 Haiku 5.5，与 Luna 同价且基准分更高；超出该阈值需按 5 倍价差和 1.25 倍 tokenizer 膨胀重新评估路由。

**标签**: `#coding-agent`, `#orchestration`, `#observability`

---

<a id="item-agent-engineer-7"></a>
### [HF 论文：自进化推理模型自训练崩溃机制](https://huggingface.co/papers/2610.04299) ⭐️ 6.5/10

论文分析了自进化推理模型重复自训练导致性能崩溃的机制。研究识别出两个关键瓶颈：无效问题随训练轮次增多，且答案一致性过滤会进一步提高其在训练数据中的占比；基于词汇相似度的多样性控制会漏检数学等价但表述不同的问题，导致后期训练出现多样性崩溃。该论文由 Hugging Face Daily Papers 发布，截至 2026-10-08 获得 47 个 upvotes，属于研究分析而非生产环境验证。

rss · Hugging Face Daily Papers · 10月8日 00:00

**「为什么重要」** 自改进 agent 依赖自生成问题持续训练，论文指出的数据质量退化路径对这类训练管线的稳定性有直接参考意义。已确认的瓶颈是无效问题累积与多样性崩溃，其对具体生产系统的影响仍待验证。

**「可关注」** 可关注：自进化训练管线中，仅靠答案一致性过滤和词汇相似度去重不足以维持问题质量，需额外处理数学等价但表述不同的问题。

**标签**: `#eval`, `#reasoning`, `#training-data`, `#self-evolution`

---

<a id="item-agent-engineer-8"></a>
### [Liquid AI 开源 d1 边缘决策模型](https://huggingface.co/blog/LiquidAI/open-d1) ⭐️ 6.3/10

Liquid AI 开源 d1-3B 与 d1-omni-600M 两个决策模型，面向边缘推理。d1-3B 在 Decision Index 0.2.1 得 48.57，为 10B 以下最高分，超过 Decider 35B-A3B 的 47.11；七项公开基准均分 82.9。模型不生成 token，单次前向传播直接输出决策，d1-3B 支持文本与图像，d1-omni-600M 支持文本+图像或文本+音频且仍处早期研究阶段。边缘延迟：Jetson AGX Thor 16 ms，AGX Orin 64 GB 26 ms，Orin Nano 50 ms；三问耗时为一问的 1.3 倍。需 transformers&gt;=5.14，且以 trust\_remote\_code=True 加载。

rss · Hugging Face Blog · 10月7日 16:54

**「为什么重要」** 对 coding agent 与 harness 开发者，单次前向传播的决策模型提供了低延迟的结构化判断路径，可嵌入 agent 循环承担路由、分类、打分等轻量任务，而非替代生成式模型。但 d1-omni-600M 仍是早期研究版本，官方未公布其速度数据与视觉/音频决策基准，多模态决策能力仍待验证。

**「可关注」** 可关注：d1-3B 在边缘设备上以 16–50 ms 完成单次决策，三问仅增 30% 耗时，适合作为 agent 中的轻量分类/路由层；但需注意其依赖 trust\_remote\_code=True 与 transformers&gt;=5.14，集成前应评估远程代码执行与版本约束风险。

**标签**: `#eval`, `#model-release`, `#edge-computing`, `#multimodal`, `#inference`

---

<a id="item-agent-engineer-9"></a>
### [Cloudflare 安全运营 harness](https://blog.cloudflare.com/agentic-security-operations/) ⭐️ 6.3/10

Cloudflare 介绍 Managed Defense AI agent harness，用多智能体系统聚合安全警报并做分析。模型推理前，确定性代码先跑固定侦察流程，收集客户身份、检测历史、流量基线、执行结果与网络观测，每项数据带来源、版本和时间戳。初始评分用运行在 Workers AI 的开源决策模型 Clef 过滤高噪声警报；需深查的警报由协调智能体并行分派给流量分析、客户上下文、全球遥测、威胁情报四个专家智能体。合成智能体将各专家的类型化发现汇总为一条建议，不能拉取新证据或选用批准词汇表外的分类；应用代码校验每条引用是否存在于版本化证据包中。

rss · Cloudflare Engineering · 10月7日 16:30

**「为什么重要」** 早期单智能体把遥测、检测描述、策略和威胁情报压进同一 prompt，导致上下文越权、范围漂移与失败消失。Cloudflare 将证据收集与范围强制移入应用代码，让模型只在固定证据包上解释。这为构建 agent harness 提供了可复制的分层边界：检索确定、推理受控、引用可查。全球遥测专家仅用聚合数据，不接触其他客户记录，兼顾全局信号与隐私隔离。

**「可关注」** 可关注：把侦察、证据打包与引用校验写进应用代码，让专家智能体在版本化快照上做解释，既使评估可复现，也让无依据论断更易暴露。

**标签**: `#harness`, `#orchestration`, `#observability`, `#security`

---

## AI 日报

<a id="item-ai-daily-1"></a>
### [OpenAI 为 Teens 增加学习功能](https://openai.com/index/teens-learn-and-plan) ⭐️ 8.3/10

OpenAI 宣布 College Planner 将登陆 ChatGPT Teens，协助学生管理大学申请。同时推出 flashcards、quizzes 等学习工具，并组建 teen AI council。官方称这些功能面向青少年的学习与规划场景。

rss · OpenAI Blog · 10月7日 12:00

**「为什么重要」** 青少年是 AI 产品的核心用户群之一。OpenAI 同时上线教育工具与 teen AI council，体现其在功能扩展与合规治理上的同步布局。

**「可关注」** 可关注：teen AI council 作为青少年反馈渠道，其权责范围与运作方式值得追踪。

**标签**: `#product`, `#lab`, `#model`

---

<a id="item-ai-daily-2"></a>
### [Secret protection must scale with software](https://github.blog/ai-and-ml/github-copilot/secret-protection-must-scale-with-software/) ⭐️ 6.3/10

GitHub Blog argues that development tools must take on more responsibility for secret protection as software creation scales, though the excerpt lacks concrete product details.

rss · GitHub Blog · 10月7日 17:45

**标签**: `#product`, `#lab`, `#industry`

---

## AI 羊毛

<a id="item-ai-deals-1"></a>
### [Claude Max/Team 计划含 API 额度](https://news.ycombinator.com/item?id=49997654) ⭐️ 7.0/10

2026 年 10 月 7 日，Claude 停止提供 6 月宣布的 Agent SDK 月度额度。Max 和 Team 计划改为包含月度 API 额度，覆盖 Claude Agent SDK、Claude API 与 Claude Managed Agents。领取方式为在 Claude Console 中建立组织并存入额度，调用时需使用该组织的 API key。材料未给出具体额度数值。

rss · HN Free API / Credits · 10月7日 19:28

**「为什么重要」** 对依赖 Agent SDK 或 Managed Agents 的订阅用户，这笔月度 API 额度可直接抵扣调用成本；但必须手动在 Console 领取并换用组织 API key，否则无法生效。

**「可关注」** 可关注：已订阅 Claude Max 或 Team 的开发者，若在使用 Agent SDK、Claude API 或 Managed Agents，现在应前往 Claude Console 创建组织并领取月度 API 额度，后续请求需使用该组织的 API key；具体额度需查阅官方支持文档。

**标签**: `#credits`, `#api`, `#promo`, `#free-tier`

---

<a id="item-ai-deals-2"></a>
### [Claude: Monthly API credits for Max and Team plans](https://support.claude.com/en/articles/17154008-monthly-api-credits-for-max-and-team-plans) ⭐️ 6.0/10

Claude 官方公告 Max 和 Team 套餐每月可领 API credits，但正文未给出具体额度与限制。

rss · HN Free API / Credits · 10月7日 18:52

**标签**: `#credits`, `#api`, `#promo`

---

<a id="item-ai-deals-3"></a>
### [Claude Max and Teams plans now forced to API \(Oct 7th update\)](https://news.ycombinator.com/item?id=49999508) ⭐️ 5.0/10

Claude Max 和 Team 付费计划现包含每月 API credits，用户可在 Claude Console 组织中领取并用于 Claude Agent SDK、Claude API 和 Managed Agents。

rss · HN Free API / Credits · 10月7日 22:15

**标签**: `#credits`, `#api`

---