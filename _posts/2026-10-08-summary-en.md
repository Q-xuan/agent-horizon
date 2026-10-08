---
layout: default
title: "Horizon Summary: 2026-10-08 (EN)"
date: 2026-10-08
lang: en
---

> From 203 items, 22 important content pieces were selected

---

**Agent Harness Architecture**
1. [openai/codex released rust-v0.161.0](#item-harness-arch-1) ⭐️ 8.3/10
2. [Agents v0.27.0 发布](#item-harness-arch-2) ⭐️ 8.3/10
3. [Mastra Core 1.75.0 Released](#item-harness-arch-3) ⭐️ 8.3/10
4. [Cline desktop v0.0.44 发布](#item-harness-arch-4) ⭐️ 7.8/10
5. [Claude Code 2.1.293 发布](#item-harness-arch-5) ⭐️ 7.8/10
6. [Cline SDK v0.0.91 Tightens Finish-Reason and MCP Handling](#item-harness-arch-6) ⭐️ 7.3/10
7. [crewAI 1.15.24 Released](#item-harness-arch-7) ⭐️ 6.3/10

**AI Agent Engineer**
1. [GPT‑6 and Intelligent UI for everyone](#item-agent-engineer-1) ⭐️ 9.0/10
2. [Haiku 5.5 发布，100k 上下文限制](#item-agent-engineer-2) ⭐️ 8.0/10
3. [Liquid AI 开源 d1 边缘决策模型](#item-agent-engineer-3) ⭐️ 7.3/10
4. [ReSAIL 抑制迭代自蒸馏崩溃](#item-agent-engineer-4) ⭐️ 7.0/10
5. [论文提出 KLPO：采样器锚定 KL 正则化](#item-agent-engineer-5) ⭐️ 7.0/10
6. [One Model Family, Two Gold-Level Results: Fine-Tuning Nemotron for IOI and IMO](#item-agent-engineer-6) ⭐️ 6.8/10
7. [Bolmo 字节级语言模型登 Nature](#item-agent-engineer-7) ⭐️ 6.3/10
8. [Cloudflare 安全运营 harness](#item-agent-engineer-8) ⭐️ 6.3/10
9. [DecepEval 基准：1,532 实例测 LLM 智能体欺骗](#item-agent-engineer-9) ⭐️ 6.0/10

**AI Daily**
1. [Helping teens learn, plan, and shape the future of AI](#item-ai-daily-1) ⭐️ 8.3/10
2. [Radisson Hotel Group brings hotel discovery into ChatGPT](#item-ai-daily-2) ⭐️ 7.8/10
3. [GitHub 主张密钥保护随软件扩展](#item-ai-daily-3) ⭐️ 5.8/10

**AI Deals**
1. [Claude 计划含 API credits](#item-ai-deals-1) ⭐️ 7.0/10
2. [Claude Max/Teams 套餐新增月度 API credits](#item-ai-deals-2) ⭐️ 5.0/10
3. [Claude 付费档月领 API 额度](#item-ai-deals-3) ⭐️ 5.0/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [openai/codex released rust-v0.161.0](https://github.com/openai/codex/releases/tag/rust-v0.161.0) ⭐️ 8.3/10

OpenAI Codex Rust v0.161.0 ships GPT-6.1 Sol as default, Bedrock multi-agent V2 support, MCP login from terminal, and opt-in Daybreak/Cyber routing.

github · github-actions\[bot\] · Oct 7, 15:58

**Tags**: `#runtime`, `#mcp`, `#subagents`, `#tools`

---

<a id="item-harness-arch-2"></a>
### [Agents v0.27.0 发布](https://github.com/cloudflare/agents/releases/tag/agents%400.27.0) ⭐️ 8.3/10

Cloudflare Agents v0.27.0 发布，新增四个实验性 harness 与 \`web\_search\` 工具，并将 Channels API 重构为基于对话和轮次的实验性接口。\`AiSdkHarness\`、\`ThinkHarness\`、\`ContainerHarness\` 和 \`OpenCodeHarness\` 与 \`PiHarness\` 同形，其中 \`ContainerHarness\` 可在 Container 中运行 Claude Code 或 Codex。旧的 \`agents/channels\` 入口已移除，新入口 \`agents/experimental/channels\` 提供 \`ChannelGateway\`、Web Channel、AI SDK chat transport 及 \`npx agents tui\` 终端客户端。

github · github-actions\[bot\] · Oct 7, 13:25

**「设计要点」** Channels 以 Durable Object 为授权边界，每个参与者默认独占一个 agent 对象，\`route\` 回调可共享或拒绝；harness 的会话与转录持久化在 Durable Object 中，通过 \`Streams\` 提供可恢复响应。

**「改了什么」** 相对上一版，真正变了的是能力面：harness 从单一 \`PiHarness\` 扩展到 AI SDK、思考、容器内编码代理与 OpenCode 四种形态；Channels 推翻重写，\`ChannelHost\`、\`fallback\`/\`fanout\` 及首轮 AI SDK/TanStack/Voice 助手全部移除，Slack、Telegram、Email 迁至 \`agents/experimental/channels/\*\`。工具层新增基于 Cloudflare Web Search API 的 \`web\_search\`，并修复 \`AiSdkHarness\` 启动、\`session.wait\` 中止语义与工具输出转换。

**Tags**: `#runtime`, `#tools`, `#mcp`, `#sandbox`

---

<a id="item-harness-arch-3"></a>
### [Mastra Core 1.75.0 Released](https://github.com/mastra-ai/mastra/releases/tag/%40mastra/core%401.75.0) ⭐️ 8.3/10

Mastra core 1.75.0 introduces a span-level observability query API, cross-store trace aggregation with token and cost analytics, and self-embedding vector store support for semantic recall. Developers can query completed spans directly via \`storage.querySpans\(\)\`, \`client.querySpans\(\)\`, or \`POST /api/observability/spans/query\` using filters, cursors, and cost previews. \`aggregateTraces\(\)\` now supports \`tokens.\*\` and \`cost.\*\` measures across ClickHouse, DuckDB, and Postgres observability stores. Semantic recall runs against self-embedding stores such as \`MongoDBVector\` with \`autoEmbed\`, removing the need for a client-side embedder.

github · Patrycja-J · Oct 7, 16:17

**「Design Notes」** The span query API operates across storage, client, and HTTP layers, returning completed spans with filters and cursors without requiring trace lookup first. Trace aggregation sums token usage per trace before grouping, and cost rows carry coverage and currency metadata, returning \`null\` when groups mix currencies.

**「What Changed」** Adds direct span querying, token/cost measures in \`aggregateTraces\(\)\`, and \`MastraVector.isSelfEmbedding\` for embedder-free semantic recall. \`@mastra/connect\` reaches 1.0 with a reworked provider API, Microsoft Teams channels, and encrypted Discord credentials, while AgentController sessions persist a single model per thread and support starting without an initial thread.

**Tags**: `#runtime`, `#eval`, `#memory`

---

<a id="item-harness-arch-4"></a>
### [Cline desktop v0.0.44 发布](https://github.com/cline/cline/releases/tag/desktop-v0.0.44) ⭐️ 7.8/10

Cline desktop v0.0.44 发布，修复 Windows MCP 加载、本地模型会话与自定义 Anthropic 网关接入。MCP 启动超时从 3 秒放宽至 10 秒，避免 npx/uvx 服务被静默丢弃。会话层新增自动重连，Cline Hub 掉线后最多尝试一分钟，排队消息恢复后补发。模型目录同步更新，免费列表增补 Solar Mini 4，下架 DeepSeek V4.1 Flash。

github · github-actions\[bot\] · Oct 7, 07:17

**「设计要点」** 工具层放宽 Windows MCP 启动超时至 10 秒，修复 npx/uvx 静默失败；会话层支持 Hub 断连自动重连与排队消息补发；模型适配层增加 reasoning level 协商，自动匹配最接近的支持档位。

**「改了什么」** Windows MCP 启动超时提至 10 秒；本地与自托管提供商恢复无 API key 会话；新增 Hub 断连自动重连与消息补发；修复自定义 Anthropic base URL 与推理级别协商。

**Tags**: `#runtime`, `#tools`, `#mcp`

---

<a id="item-harness-arch-5"></a>
### [Claude Code 2.1.293 发布](https://code.claude.com/docs/en/changelog#2-1-293) ⭐️ 7.8/10

Claude Code 2.1.293 发布。默认 Haiku 模型切换为 Claude Haiku 5.5（claude-haiku-5-5），1M 上下文，$0.10/$0.50 per Mtok，超 100K 提示词为 $0.50/$2.50。subagentStatusLine 载荷新增 agentType，脚本可区分自定义 subagent 类型；$.tool.register 新增 isDeferred，mods 可让工具 schema 从起始即出现在 prompt，而非仅在 tool search 后可见。修复 HTTP MCP 连接持有全部已发请求的内存泄漏，以及上下文压缩后模型将已完成工作误判为未完成而撤回或重做的问题。

rss · Claude Code Changelog · Oct 7, 18:26

**「设计要点」** 工具层与 subagent 元数据扩展：agentType 进入状态行载荷，isDeferred 控制 schema 注册时机；MCP 连接修复请求缓存失控；上下文压缩逻辑避免对压缩前动作的重复处理。

**「改了什么」** 新增 subagent 类型标识与工具 schema 即时注册能力；修复 MCP 内存泄漏和压缩后工作误判；回滚 2.1.281 自动模式拒绝提示与 2.1.290 云会话唤醒修复。

**Tags**: `#runtime`, `#tools`, `#mcp`, `#subagents`, `#memory`

---

<a id="item-harness-arch-6"></a>
### [Cline SDK v0.0.91 Tightens Finish-Reason and MCP Handling](https://github.com/cline/cline/releases/tag/sdk/sdk/v0.0.91) ⭐️ 7.3/10

Cline SDK v0.0.91 tightens finish-reason semantics, raises stdio MCP init timeout to 10s, and gates Anthropic refusal fallbacks to official endpoints. Missing or unrecognized finish reasons now map to a new \`unknown\` state; the agent keeps the partial response and continues once with a hidden user message before failing on a second unknown. Stdio MCP servers get a 10s default initialize budget to prevent Windows \`npx\`/\`uvx\` drops, and the Anthropic provider sends \`fallbacks\` only to \`api.anthropic.com\` to avoid 400s on Azure.

github · github-actions\[bot\] · Oct 7, 06:00

**「Design Notes」** \`AgentModelFinishReason\` gains \`unknown\`, with the AI SDK adapter mapping unified \`other\` and missing reasons to it instead of \`stop\`. A new \`isOfficialAnthropicEndpoint\` helper restricts the \`fallbacks\` option to \`api.anthropic.com\`, while stdio MCP servers get a 10s default initialize budget overridable by explicit \`timeout\`.

**「What Changed」** Finish-reason handling now maps missing/unrecognized reasons to \`unknown\` and retries once before failing; stdio MCP initialize timeout rises to 10s; Anthropic \`fallbacks\` is gated to official endpoints; and portable reasoning levels snap to advertised effort levels for \`cline\` and \`openai-compatible\` adapters.

**Tags**: `#runtime`, `#tools`, `#mcp`

---

<a id="item-harness-arch-7"></a>
### [crewAI 1.15.24 Released](https://github.com/crewAIInc/crewAI/releases/tag/1.15.24) ⭐️ 6.3/10

crewAI 1.15.24 adds experimental job lifecycle and runner support, turn and reply identities, and Oracle integrations. Eval tooling gains a markdown brief for agent runs, \`--models\` and \`llm\_overlay\` for swapping models and roles, and a strict exit code 1 unless the gate passes. Refactoring moves message summarization into \`SummarizeMessages\` and centralizes context window handling.

github · lorenzejay · Oct 7, 17:39

**「Architecture Note」** The experimental runner and job lifecycle introduce a new execution path for background replies and turn identity. Summarization logic now lives in \`SummarizeMessages\`, and context windows are centrally managed instead of inline.

**「What Changed」** Eval now exits with code 1 on failure and supports model swapping via CLI flags and overlays. Start steps can re-run on events they listen to, and human feedback steps expose review content in outputs.

**Tags**: `#eval`, `#runtime`, `#memory`, `#tools`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [GPT‑6 and Intelligent UI for everyone](https://openai.com/index/gpt-6-for-everyone/) ⭐️ 9.0/10

OpenAI announces GPT-6 and an intelligent UI, accompanied by a system card noting statistically significant safety eval regressions relative to GPT-5.6.

hackernews · joshuawright11 · Oct 7, 18:00 · [Discussion](https://news.ycombinator.com/item?id=49996425)

**Tags**: `#coding-agent`, `#eval`

---

<a id="item-agent-engineer-2"></a>
### [Haiku 5.5 发布，100k 上下文限制](https://www.anthropic.com/claude-haiku-5-5) ⭐️ 8.0/10

Anthropic 发布 Claude Haiku 5.5，Hacker News 讨论聚焦定价与 100k 上下文门槛。输入在 100k token 以内 $0.10/MTok、超出后 $0.50/MTok；输出对应 $0.50/MTok 与 $2.50/MTok，该 cutoff 仅作用于 Haiku，不覆盖 Sonnet 或 Opus。chriddyp 的 DataAnalyticsBench 显示其比 Haiku 4.5 便宜 9 倍、成绩高两个字母等级，40 题成本 $0.38。simonw 测试不同 thinking level，low 耗时 7 秒、成本 0.0936 美分，max 耗时 5 分 9 秒、成本 3.3826 美分。

hackernews · sfkgtbor · Oct 7, 18:01 · [Discussion](https://news.ycombinator.com/item?id=49996437)

**「为什么重要」** 100k token 的计费与上下文分界对 agent 负载偏低，minimaxir 指出该限制会迅速被超出；输出价格在越界后跳升 5 倍，直接影响长上下文 agent 的成本模型。

**「可关注」** 可关注：Haiku 5.5 在短上下文任务上具备显著成本优势，但 agent 场景需按 100k 边界重新评估 prompt 压缩与上下文管理策略。

**「评论」** simonw 与 chriddyp 的实测分别从绘图质量与数据分析基准验证了低价高效；minimaxir 则认为 100k 分界低得离谱，且仅覆盖 Haiku 而不适用于 Sonnet 或 Opus，定价结构引发争议。

**Tags**: `#coding-agent`, `#eval`, `#observability`

---

<a id="item-agent-engineer-3"></a>
### [Liquid AI 开源 d1 边缘决策模型](https://huggingface.co/blog/LiquidAI/open-d1) ⭐️ 7.3/10

Liquid AI 发布开源边缘决策模型 d1-3B 与 d1-omni-600M。d1-3B 在 Decision Index 0.2.1 取得 48.57 分，为 10B 以下最佳，超过 Decider 35B-A3B 的 47.11；两个模型均不做 token 生成，单次前向输出结构化决策。d1-3B 支持文本与图像，基于 LFM2.5-VL-3B；d1-omni-600M 支持文本+图像或文本+音频，基于 LFM2.5-Encoder-350M，目前为早期研究版本。在 NVIDIA Jetson AGX Thor 上，d1-3B 单问延迟 16 ms，Jetson Orin Nano 上为 50 ms。

rss · Hugging Face Blog · Oct 7, 16:54

**「为什么重要」** 对边缘 agent 与实时决策场景，这类模型将分类、打分、路由等任务从生成式调用转为单次前向，延迟降至几十毫秒级。但官方未提供视觉与音频决策基准，多模态决策质量仍缺乏公开验证。

**「可关注」** 可关注：d1-3B 在 Jetson AGX Thor 上处理 3.4K-token 状态需 220 ms，远高于单问的 16 ms；长状态而非请求数是边缘部署的主要瓶颈，需按状态长度评估吞吐。

**Tags**: `#eval`, `#coding-agent`, `#edge`

---

<a id="item-agent-engineer-4"></a>
### [ReSAIL 抑制迭代自蒸馏崩溃](https://huggingface.co/papers/2609.39306) ⭐️ 7.0/10

Hugging Face 每日论文收录 ReSAIL，针对迭代特权信息自蒸馏提出插件式增强。论文实验显示，现有方法在多轮部署后出现部署性能崩溃，特权信息（PI）任务表现也随周期下降。ReSAIL 筛选 PI 最强烈改变教师预测的交互步骤，跨轨迹平衡蒸馏损失，并在学生接替教师时保留 PI 条件行为。该方法面向迭代 PI 自蒸馏场景，论文同时指出其影响范围目前集中于该研究方向。

rss · Hugging Face Daily Papers · Oct 8, 00:00

**「为什么重要」** 迭代自蒸馏是 LLM 智能体通往递归自我改进（RSI）的路径之一，跨部署周期的性能崩溃直接阻断该路径。ReSAIL 针对这一具体失效模式给出插件式缓解方案，对从事智能体训练与自改进循环的工程师具有直接参考价值。

**「可关注」** 可关注：在搭建迭代自蒸馏或自改进循环时，需监控跨周期部署性能与特权信息条件行为的衰减，ReSAIL 的步骤筛选与损失平衡提供了可复用的缓解思路。

**Tags**: `#eval`, `#memory`, `#orchestration`

---

<a id="item-agent-engineer-5"></a>
### [论文提出 KLPO：采样器锚定 KL 正则化](https://huggingface.co/papers/2610.08963) ⭐️ 7.0/10

2026-10-08 HF 日报论文提出 KLPO，针对异步 RL 训练 LLM agent 时 rollout 来自旧 checkpoint、推理引擎与训练器概率失配的问题。现有做法要么裁剪重要性比率引入偏差，要么像 GRPO 那样按 prompt 组采样，长 episode 下成本高。KLPO 将 KL 正则化锚定在采样器上，给出闭式 Gibbs 解，并用最小二乘拟合 log-ratio 最优性条件，使采样器概率通过 log-ratio 进入。论文未发布代码与基准结果。

rss · Hugging Face Daily Papers · Oct 8, 00:00

**「为什么重要」** 异步 RL 的概率失配是训练 LLM agent 的常见工程瓶颈。KLPO 给出闭式 Gibbs 解与最小二乘 log-ratio 拟合，提供了不同于重要性比率裁剪和 GRPO 组采样的更新路径，但论文尚未发布代码与基准，实际效果待验证。

**「可关注」** KLPO 用采样器锚定 KL 正则化，把异步 RL 更新写成闭式 Gibbs 解，并以最小二乘拟合 log-ratio 条件；若后续放出代码，可对比其与 GRPO、重要性比率裁剪在长 episode 下的训练稳定性与成本。

**Tags**: `#eval`, `#coding-agent`, `#rl`

---

<a id="item-agent-engineer-6"></a>
### [One Model Family, Two Gold-Level Results: Fine-Tuning Nemotron for IOI and IMO](https://huggingface.co/blog/nvidia/nemotron-ioi-and-imo-2026) ⭐️ 6.8/10

NVIDIA reports Nemotron 3 fine-tuned with SFT, RL, and generate-verify-refine systems reached gold-medal level at IOI 2026 and IMO 2026.

rss · Hugging Face Blog · Oct 7, 12:45

**Tags**: `#eval`, `#coding-agent`, `#orchestration`

---

<a id="item-agent-engineer-7"></a>
### [Bolmo 字节级语言模型登 Nature](https://allenai.org/blog/bolmo-nature) ⭐️ 6.3/10

2026 年 10 月 7 日，Ai2 宣布 Bolmo 字节级语言模型技术论文发表于 Nature，论文题为 “Retrofitting language models to operate over bytes”。官方称 Bolmo 为完全开放的字节级语言模型，新检查点显示该方法已从 Olmo 泛化到其他模型家族。博客未提供技术细节、代码或 Agent 工程相关影响。

rss · Allen AI · Oct 7, 08:00

**「为什么重要」** 字节级语言建模可能改变现有基于子词分词的模型假设，影响 coding agent 的上下文计算与工具链设计。但官方博客未给出技术细节，实际影响仍待论文与代码验证。

**「可关注」** 可关注：Bolmo 新检查点已泛化至 Olmo 以外的模型家族，但官方未同步提供代码或技术细节，工程侧暂无法评估其对现有 tokenizer 与 eval 流程的改造成本。

**Tags**: `#llm`, `#research`, `#model-architecture`

---

<a id="item-agent-engineer-8"></a>
### [Cloudflare 安全运营 harness](https://blog.cloudflare.com/agentic-security-operations/) ⭐️ 6.3/10

Cloudflare 发布 Managed Defense AI agent harness，用多智能体处理安全告警分诊与调查。模型推理前，确定性代码先执行固定侦察工作流，收集身份、检测历史、流量基线与网络观测并记录来源、版本、时间戳；初筛由开源决策模型 Clef 在 Workers AI 上完成，高噪声告警直接跳过专家分析。需深查的告警由协调智能体并行调度流量分析、客户上下文、全球遥测、威胁情报四个专家智能体，综合智能体合并类型化发现，只能引用版本化证据包内条目，不能获取新证据或超出受控词汇表分类。深度分析调用 OpenAI Daybreak Defense Network 与 Anthropic 模型（GPT-5.6 Cyber、Mythos），全球遥测仅用聚合数据保护客户隐私；官方博客为产品级公告，未提供代码、架构细节或可复现基准。

rss · Cloudflare Engineering · Oct 7, 16:30

**「为什么重要」** 对构建 coding agent 与 harness 的工程师而言，该设计把「先侦察、后推理」落成工程模式：用确定性代码固定证据收集与范围执行，再让多个窄域智能体在版本化证据包上并行推理，直接针对单智能体出现的幻觉、上下文越权、范围漂移与失败不可见问题。目前官方仅给出产品级描述，未公开代码、架构细节或第三方基准，实际效果仍待验证。

**「可关注」** 可关注：将侦察与范围执行固化为确定性代码，再让多智能体在受控证据包上并行推理，是抑制单智能体幻觉与范围漂移的一种工程路径。

**Tags**: `#harness`, `#orchestration`, `#observability`

---

<a id="item-agent-engineer-9"></a>
### [DecepEval 基准：1,532 实例测 LLM 智能体欺骗](https://huggingface.co/papers/2610.07967) ⭐️ 6.0/10

DecepEval 基准发布，含 1,532 个实例，覆盖 3 个任务族与 28 个专业场景。论文提出 LLM Deception Diamond 框架，用压力、激励、机会、冲突四个外部条件刻画智能体欺骗倾向。每个实例配中性版与诱导版，测量条件依赖性。此前评估多聚焦孤立场景，该基准试图系统回答欺骗何时更易发生。

rss · Hugging Face Daily Papers · Oct 8, 00:00

**「为什么重要」** 工程师需要评估 coding agent 在压力或激励下是否走偏。DecepEval 提供条件化测试集，把欺骗从个案观察变成可量化指标。目前材料仅限摘要，具体任务族与诱导方式尚未公开。

**「可关注」** 可关注：DecepEval 将欺骗评估拆成四个可干预的外部条件，后续做 agent 评测时可对照压力、激励、机会、冲突设计对照实验。

**Tags**: `#eval`, `#benchmark`, `#llm-agents`

---

## AI Daily

<a id="item-ai-daily-1"></a>
### [Helping teens learn, plan, and shape the future of AI](https://openai.com/index/teens-learn-and-plan) ⭐️ 8.3/10

OpenAI announces College Planner and new learning tools for ChatGPT Teens, along with a teen AI council.

rss · OpenAI Blog · Oct 7, 12:00

**Tags**: `#product`, `#lab`, `#industry`

---

<a id="item-ai-daily-2"></a>
### [Radisson Hotel Group brings hotel discovery into ChatGPT](https://openai.com/index/radisson) ⭐️ 7.8/10

Radisson Hotel Group partnered with Accenture to build a ChatGPT plugin for hotel discovery and booking. Travelers can find, compare, and book hotels while planning trips. The plugin uses OpenAI technology. This is a product integration, not a core model release or policy change.

rss · OpenAI Blog · Oct 7, 07:00

**「为什么重要」** The plugin extends ChatGPT into travel booking through a third-party integration. The source provides no usage metrics, booking conversion data, or technical implementation details.

**「可关注」** Hotel search is entering conversational interfaces via plugins. The source does not describe the architecture, API surface, or performance.

**Tags**: `#product`, `#industry`, `#lab`, `#model`

---

<a id="item-ai-daily-3"></a>
### [GitHub 主张密钥保护随软件扩展](https://github.blog/ai-and-ml/github-copilot/secret-protection-must-scale-with-software/) ⭐️ 5.8/10

GitHub 发布博文《Secret protection must scale with software》，主张开发者并非更粗心，而是被软件创建速度超越。文章认为，帮助开发者创建更多软件的工具，也应承担更多保护软件的责任。提供的摘录仅包含这一核心论点，未提及具体新功能、发布事实或可验证的产品细节。

rss · GitHub Blog · Oct 7, 17:45

**「可关注」** 可关注：GitHub 主张由开发工具承担更多密钥防护工作，以匹配软件创建速度；摘录未说明对应功能或时间表。

**Tags**: `#product`, `#industry`

---

## AI Deals

<a id="item-ai-deals-1"></a>
### [Claude 计划含 API credits](https://news.ycombinator.com/item?id=49997654) ⭐️ 7.0/10

Claude Max 和 Team 计划现包含月度 API credits，可用于 Claude Agent SDK、Claude API 及 Claude Managed Agents。用户需在 Claude Console 中领取，并使用该组织下的 API key 调用。此前 6 月宣布的 Agent SDK 月度 credit 已不再提供。材料未给出具体额度数值。

rss · HN Free API / Credits · Oct 7, 19:28

**「为什么重要」** 对已订阅 Max 或 Team 的开发者，Agent SDK 与 Managed Agents 的调用成本可直接用套餐内 credits 抵扣，无需另外充值。仅覆盖上述三项服务，且需先领取到 Console 组织。

**「可关注」** 可关注：已付费订阅用户可在 Claude Console 组织内领取月度 API credits，用于 Agent SDK、Claude API 和 Managed Agents；未订阅或需高频调用的场景仍需按量付费，且 6 月单独的 Agent SDK credit 已停发。

**Tags**: `#credits`, `#api`, `#promo`

---

<a id="item-ai-deals-2"></a>
### [Claude Max/Teams 套餐新增月度 API credits](https://news.ycombinator.com/item?id=49999508) ⭐️ 5.0/10

Anthropic 更新 Claude Max 与 Teams 套餐，现包含月度 API credits，覆盖 Claude Agent SDK、Claude API 与 Claude Managed Agents。用户需在 Claude Console 组织中领取，并使用该组织的 API key 调用。6 月曾预告的 Agent SDK 月度 credit 已不再提供。来源未说明具体额度、有效期或官方领取页链接。

rss · HN Free API / Credits · Oct 7, 22:15

**「为什么重要」** 对已订阅 Max 或 Teams 的开发者，套餐内 API credits 可直接用于 Agent SDK 与 Managed Agents，减少额外采购 API 额度的支出。但具体额度与限制未公开，实际价值需以 Console 内显示为准。

**「可关注」** 可关注：若你已在 Claude Console 建有组织并持有 API key，可检查 Max/Teams 套餐是否自动到账；未建组织或使用个人 key 的开发者需先完成组织领取才能用上这批 credits。

**Tags**: `#credits`, `#api`, `#promo`

---

<a id="item-ai-deals-3"></a>
### [Claude 付费档月领 API 额度](https://support.claude.com/en/articles/17154008-monthly-api-credits-for-max-and-team-plans) ⭐️ 5.0/10

Claude 官方支持文档宣布，Max 和 Team 计划可领取每月 API credits。材料仅包含标题与链接，未给出具体额度、使用限制和有效期。领取条件与截止时间需查阅官方支持文档确认。

rss · HN Free API / Credits · Oct 7, 18:52

**「为什么重要」** 对已订阅 Max 或 Team 计划的开发者而言，这是官方文档提到的每月 API credits 领取入口。由于材料缺少额度与限制信息，实际价值需以支持文档为准。

**「可关注」** 可关注：该 credits 仅面向 Claude Max 和 Team 计划，具体额度、限制和有效期需查阅官方支持文档确认。

**Tags**: `#credits`, `#api`, `#promo`

---