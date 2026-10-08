---
layout: default
title: "Horizon Summary: 2026-10-08 (ZH)"
date: 2026-10-08
lang: zh
---

> 从 203 条内容中筛选出 22 条重要资讯。

---

**Harness 架构**
1. [openai/codex released rust-v0.161.0](#item-harness-arch-1) ⭐️ 8.3/10
2. [Cloudflare Agents 0.27.0 发布](#item-harness-arch-2) ⭐️ 8.3/10
3. [Mastra core 1.75.0 发布](#item-harness-arch-3) ⭐️ 8.3/10
4. [Cline desktop v0.0.44 发布](#item-harness-arch-4) ⭐️ 7.8/10
5. [Claude Code 2.1.293 发布](#item-harness-arch-5) ⭐️ 7.8/10
6. [Cline SDK v0.0.91 发布](#item-harness-arch-6) ⭐️ 7.3/10
7. [crewAI 1.15.24 发布](#item-harness-arch-7) ⭐️ 6.3/10

**Agent 工程师日报**
1. [GPT‑6 and Intelligent UI for everyone](#item-agent-engineer-1) ⭐️ 9.0/10
2. [Claude Haiku 5.5 发布](#item-agent-engineer-2) ⭐️ 8.0/10
3. [Liquid AI 开源 d1 决策模型](#item-agent-engineer-3) ⭐️ 7.3/10
4. [ReSAIL 缓解迭代自蒸馏崩溃](#item-agent-engineer-4) ⭐️ 7.0/10
5. [KLPO 提出采样器锚定 KL 正则化](#item-agent-engineer-5) ⭐️ 7.0/10
6. [One Model Family, Two Gold-Level Results: Fine-Tuning Nemotron for IOI and IMO](#item-agent-engineer-6) ⭐️ 6.8/10
7. [Bolmo 字节级模型登上 Nature](#item-agent-engineer-7) ⭐️ 6.3/10
8. [Cloudflare 安全运营 harness 上线](#item-agent-engineer-8) ⭐️ 6.3/10
9. [DecepEval：LLM 智能体欺骗评估基准](#item-agent-engineer-9) ⭐️ 6.0/10

**AI 日报**
1. [Helping teens learn, plan, and shape the future of AI](#item-ai-daily-1) ⭐️ 8.3/10
2. [Radisson 推出 ChatGPT 插件](#item-ai-daily-2) ⭐️ 7.8/10
3. [GitHub：密钥保护须随软件扩展](#item-ai-daily-3) ⭐️ 5.8/10

**AI 羊毛**
1. [Claude Max/Team 含 API credits](#item-ai-deals-1) ⭐️ 7.0/10
2. [Claude Max 与 Teams 改发 API credits](#item-ai-deals-2) ⭐️ 5.0/10
3. [Claude 两档计划开放 credits](#item-ai-deals-3) ⭐️ 5.0/10

---

## Harness 架构

<a id="item-harness-arch-1"></a>
### [openai/codex released rust-v0.161.0](https://github.com/openai/codex/releases/tag/rust-v0.161.0) ⭐️ 8.3/10

OpenAI Codex Rust v0.161.0 ships GPT-6.1 Sol as default, Bedrock multi-agent V2 support, MCP login from terminal, and opt-in Daybreak/Cyber routing.

github · github-actions\[bot\] · 10月7日 15:58

**标签**: `#runtime`, `#mcp`, `#subagents`, `#tools`

---

<a id="item-harness-arch-2"></a>
### [Cloudflare Agents 0.27.0 发布](https://github.com/cloudflare/agents/releases/tag/agents%400.27.0) ⭐️ 8.3/10

Cloudflare Agents 0.27.0 发布，新增四个实验性 harness 和 web\_search 工具，并重构实验性 Channels API。AiSdkHarness、ThinkHarness、ContainerHarness、OpenCodeHarness 与 PiHarness 同形；其中 ContainerHarness 可在 Container 中运行 Claude Code 或 Codex。新增 agents/websearch，为 pi、AI SDK 和 TanStack AI 提供基于 Cloudflare Web Search API 的 web\_search 工具。Channels 从 agents/channels 迁移到 agents/experimental/channels，围绕 conversation 和 turn 重建，旧入口已移除。

github · github-actions\[bot\] · 10月7日 13:25

**「设计要点」** Channels 以 Durable Object 为授权边界，每个 participant 默认独占一个 agent object，也可通过 route 回调共享或拒绝。ChannelGateway 作为 Worker 入口验证 webhook、处理 Web Channel 升级并路由到对应 agent object。Web Channel 通过 agent 的 WebSocket 传输实时 transcript、turn、审批与客户端工具结果。

**「改了什么」** 相对上一版，真正变化是 Channels 第一轮实现被移除，Slack、Telegram、Email 接入点移至 agents/experimental/channels 下；同时新增 ChannelGateway、Web Channel 客户端、AI SDK ChatTransport 与 npx agents tui 终端客户端。harness 层新增 AiSdkHarness 等四个实验实现，工具层新增 web\_search。

**标签**: `#runtime`, `#tools`, `#mcp`, `#sandbox`

---

<a id="item-harness-arch-3"></a>
### [Mastra core 1.75.0 发布](https://github.com/mastra-ai/mastra/releases/tag/%40mastra/core%401.75.0) ⭐️ 8.3/10

Mastra core 1.75.0 发布，核心包新增 span 级可观测查询 API：\`storage.querySpans\(\)\`、\`client.querySpans\(\)\` 与 \`POST /api/observability/spans/query\` 支持按过滤条件、游标和模型成本预览直接检索已完成 span，无需先定位 trace。\`aggregateTraces\(\)\` 扩展 token 与 cost 度量，并在 ClickHouse、DuckDB、Postgres 三个 observability store 落地，支持跨存储聚合。语义召回新增自嵌入向量存储支持，\`MastraVector.isSelfEmbedding\` 为 true 时无需客户端 embedder，\`MongoDBVector\` 通过 \`autoEmbed\` 接入。

github · Patrycja-J · 10月7日 16:17

**「设计要点」** 可观测性从 trace 级下沉到 span 级，查询与聚合经 storage 抽象统一，但聚合实现按 store 分别落地。记忆层的向量存储通过 \`isSelfEmbedding\` 把嵌入责任交回存储端，自嵌入消息写入独立索引，与客户端向量隔离。

**「改了什么」** 新增 span 查询与跨 store 的 token/cost 聚合；\`@mastra/connect\` 进入 1.0，\`integrations\` 更名 \`providers\`，Discord 改用单一加密 bot-token，发现的 MCP 工具默认不再要求审批。AgentController 移除 \`modeId\`/\`scope\`，\`session.model.switch\` 改为 \`switch\(modelId, options?\)\`，会话按线程持久化单一当前模型。

**标签**: `#runtime`, `#eval`, `#memory`

---

<a id="item-harness-arch-4"></a>
### [Cline desktop v0.0.44 发布](https://github.com/cline/cline/releases/tag/desktop-v0.0.44) ⭐️ 7.8/10

Cline desktop v0.0.44 修复 Windows MCP server 加载与本地模型会话，并加入断线自动重连。Windows 上 npx/uvx 启动的 MCP server 超时从 3s 放宽到 10s，避免静默丢弃。LM Studio、Ollama、vLLM 等无需 API key 的本地 provider 恢复会话。Cline Hub 断线后自动重连最多一分钟，排队消息在恢复后补发。Mermaid 图表改为内联交互渲染，外链需确认后打开。

github · github-actions\[bot\] · 10月7日 07:17

**「设计要点」** 工具层调整 MCP server 启动超时与本地 provider 的 API key 校验逻辑。会话层增加重连窗口与消息队列，模型响应无 finish reason 时主动请求续写。

**「改了什么」** 相对 desktop-v0.0.43，Windows MCP 启动超时从 3s 提升至 10s，本地/自托管 provider 恢复会话，Cline Hub 断线自动重连并补发排队消息，同时修复自定义 Anthropic base URL 与模型推理级别适配。

**标签**: `#runtime`, `#tools`, `#mcp`

---

<a id="item-harness-arch-5"></a>
### [Claude Code 2.1.293 发布](https://code.claude.com/docs/en/changelog#2-1-293) ⭐️ 7.8/10

Claude Code 2.1.293 发布。新增默认 Haiku 模型 \`claude-haiku-5-5\`，1M 上下文，定价 $0.10/$0.50 per Mtok，超过 100K 的 prompt 为 $0.50/$2.50。\`subagentStatusLine\` payload 增加 \`agentType\`，脚本可区分自定义 subagent 类型。\`$.tool.register\` 增加 \`isDeferred\`，mods 设 \`false\` 可让工具 schema 从起始进入 prompt，而非藏在 tool search 后。修复 HTTP MCP 连接在关闭前保留所有已发送请求的内存泄漏，以及上下文压缩后 Claude 有时撤回或重做已完成工作的问题。

rss · Claude Code Changelog · 10月7日 18:26

**「设计要点」** 工具层与 subagent 运行时调整明显。\`isDeferred\` 让 mod 控制工具 schema 的 prompt 可见性，\`agentType\` 让状态栏脚本识别自定义 subagent。MCP 连接泄漏和压缩后动作回退都直接影响长会话稳定性。

**「改了什么」** 新增 Haiku 5.5 默认模型与 \`subagentStatusLine\` 的 \`agentType\` 字段；\`$.tool.register\` 支持 \`isDeferred\` 控制工具 schema 注册时机；修复 HTTP MCP 连接内存泄漏、上下文压缩后重做或撤回已完成工作、后台会话丢失未发送消息等问题。

**标签**: `#runtime`, `#tools`, `#mcp`, `#subagents`, `#memory`

---

<a id="item-harness-arch-6"></a>
### [Cline SDK v0.0.91 发布](https://github.com/cline/cline/releases/tag/sdk/sdk/v0.0.91) ⭐️ 7.3/10

Cline SDK v0.0.91 发布，收紧运行时与 MCP 行为。缺失或未识别的 finish reason 不再视为成功完成，\`AgentModelFinishReason\` 新增 \`unknown\`，AI SDK adapter 将统一 \`other\` 与缺失原因映射到它；无工具活动时保留部分响应并以隐藏 user message 重试一次，第二次 unknown 才失败。Stdio MCP 默认 initialize 预算从 3s 提到 10s，修复 Windows 下 \`npx\`/\`uvx\` 经 cmd.exe 启动被静默丢弃的问题。Anthropic 的 refusal \`fallbacks\` 选项只发往 \`api.anthropic.com\`，Azure 等自定义端点不再收到导致 400 的字段。

github · github-actions\[bot\] · 10月7日 06:00

**「设计要点」** 运行时把 finish reason 当作显式状态处理，并在每个请求边界消费排队 user message；工具层为 stdio MCP 设置 10s 初始化预算，显式 \`timeout\` 仍可覆盖。Provider 侧新增 \`isOfficialAnthropicEndpoint\` 与 \`apiKeyOptional\` 事实，把端点能力与密钥可选性下沉到 provider 元数据。

**「改了什么」** 相对 v0.0.90，SDK 补齐失败语义与跨 provider 兼容：finish reason 未知时进入一次隐藏重试而非直接判成功；MCP stdio 初始化超时从 3s 提高到 10s；Anthropic fallbacks 与 reasoning effort 按官方端点和模型 advertised levels 收敛；OpenAI-compatible providerOptions 统一 camelCase 别名以消除 deprecation 警告。

**标签**: `#runtime`, `#tools`, `#mcp`

---

<a id="item-harness-arch-7"></a>
### [crewAI 1.15.24 发布](https://github.com/crewAIInc/crewAI/releases/tag/1.15.24) ⭐️ 6.3/10

crewAI 1.15.24 发布。新增实验性 job lifecycle 与 runner，引入 turn 和 reply 身份标识，接入 Oracle 集成。eval 工具支持输出 markdown brief，通过 --models 和 llm\_overlay 交换模型与角色，未通过 gate 时退出码固定为 1。消息摘要逻辑移入 SummarizeMessages，context window 改为集中刷新。

github · lorenzejay · 10月7日 17:39

**「设计要点」** 运行时新增实验性 job lifecycle 与 runner，以 turn/reply 身份标识跟踪任务状态。消息摘要收敛至 SummarizeMessages，context window 集中刷新，影响长程上下文与记忆管理。

**「改了什么」** 新增实验性 job lifecycle/runner 与 turn/reply 身份；eval 支持模型与角色交换及 markdown 输出；消息摘要移入 SummarizeMessages，context window 集中管理。

**标签**: `#eval`, `#runtime`, `#memory`, `#tools`

---

## Agent 工程师日报

<a id="item-agent-engineer-1"></a>
### [GPT‑6 and Intelligent UI for everyone](https://openai.com/index/gpt-6-for-everyone/) ⭐️ 9.0/10

OpenAI announces GPT-6 and an intelligent UI, accompanied by a system card noting statistically significant safety eval regressions relative to GPT-5.6.

hackernews · joshuawright11 · 10月7日 18:00 · [社区讨论](https://news.ycombinator.com/item?id=49996425)

**标签**: `#coding-agent`, `#eval`

---

<a id="item-agent-engineer-2"></a>
### [Claude Haiku 5.5 发布](https://www.anthropic.com/claude-haiku-5-5) ⭐️ 8.0/10

Anthropic 发布 Claude Haiku 5.5，Hacker News 讨论聚焦定价与 100k 上下文上限。输入 $0.10/MTok（100k tokens 以下）、$0.50/MTok（超过 100k tokens），输出 $0.50/MTok（100k tokens 以下）、$2.50/MTok（超过 100k tokens）；该分档仅用于 Haiku，Sonnet 和 Opus 不适用。simonw 测试不同 thinking level 的 SVG 生成：low 档耗时 7 秒、花费 0.0936 美分，max 档耗时 5 分 9 秒、花费 3.3826 美分。chriddyp 用 DataAnalyticsBench 测试，称比 Haiku 4.5 便宜 9 倍、成绩高两个字母等级，40 题成本 $0.38。

hackernews · sfkgtbor · 10月7日 18:01 · [社区讨论](https://news.ycombinator.com/item?id=49996437)

**「为什么重要」** 100k tokens 的上下文分档对 agent 工作负载构成硬限制，minimaxir 指出该阈值在 agent 场景中会快速超出。chriddyp 的基准测试显示 Haiku 5.5 比 Haiku 4.5 便宜 9 倍且成绩高两个字母等级，为低成本模型选型提供了新数据点。

**「可关注」** 可关注：Haiku 5.5 的 100k 上下文分档与 Sonnet/Opus 不同，构建长上下文 agent 时需重新评估 token 预算与分档成本；thinking level 从 low 到 max 的延迟与花费差异显著，可按任务复杂度分级调用。

**「评论」** simonw 的 SVG 测试显示 medium 及以上 thinking level 可正确渲染自行车框架，low 档出错；minimaxir 认为 100k 分档上限过低且仅限 Haiku，chriddyp 则报告 DataAnalyticsBench 中比 Haiku 4.5 便宜 9 倍、成绩高两个字母等级。charlesabarnes 提到 Max 和 Team 订阅者将获得月度 API 额度，但评论未完整。

**标签**: `#coding-agent`, `#eval`, `#observability`

---

<a id="item-agent-engineer-3"></a>
### [Liquid AI 开源 d1 决策模型](https://huggingface.co/blog/LiquidAI/open-d1) ⭐️ 7.3/10

Liquid AI 开源 d1-3B 与 d1-omni-600M 边缘决策模型。d1-3B 在 Decision Index 0.2.1 得 48.57，为 10B 以下最佳，高于 Decider 35B-A3B 的 47.11。模型不生成 token，单次前向输出决策。d1-3B 支持文本与图像，基于 LFM2.5-VL-3B；d1-omni-600M 支持文本加图像或文本加音频，基于 LFM2.5-Encoder-350M，仍属早期研究版本。Jetson AGX Thor 单次推理 16 ms，Jetson Orin Nano 50 ms。

rss · Hugging Face Blog · 10月7日 16:54

**「为什么重要」** 对边缘 agent 与实时决策场景，d1-3B 用 3B 参数达到 35B 模型的决策分数，并把 Jetson 端延迟压到 50 ms 以内。d1-omni-600M 以 600M 参数取得 78.4 分，超过 Decider 2B 的 77.1，但尚未公布速度数据。

**「可关注」** 可关注：d1-3B 需 \`transformers&gt;=5.14\` 并以 \`trust\_remote\_code=True\` 加载；\`system\_one\` 可在一次前向里对同一状态回答多个命名问题，\`system\_one\_batch\` 支持无填充打包多请求。

**标签**: `#eval`, `#coding-agent`, `#edge`

---

<a id="item-agent-engineer-4"></a>
### [ReSAIL 缓解迭代自蒸馏崩溃](https://huggingface.co/papers/2609.39306) ⭐️ 7.0/10

Hugging Face 每日论文于 2026-10-08 收录 ReSAIL，针对迭代特权信息自蒸馏中的性能崩溃提出插件式增强。实验显示，现有方法在多轮部署后出现部署性能下降，特权信息条件下的任务表现同步衰退。ReSAIL 筛选教师预测受特权信息影响最强的交互步骤，并在轨迹间平衡蒸馏损失，以在学生成为下一轮教师时保留特权条件行为。论文将其定位为插件式方法，当前影响范围限于自蒸馏研究路径，尚未涉及更广泛的协议或工具变更。

rss · Hugging Face Daily Papers · 10月8日 00:00

**「为什么重要」** 迭代自蒸馏为 LLM agent 递归自我改进提供路径，但跨周期崩溃是实验观察到的实际问题。ReSAIL 的筛选与损失平衡机制为训练循环中的稳定性问题提供了具体技术对照。

**「可关注」** 可关注：在构建多轮自蒸馏或自改进训练管线时，可将交互步骤的影响力度量与蒸馏损失的轨迹级平衡作为独立模块评估，而非直接套用现有自蒸馏流程。

**标签**: `#eval`, `#memory`, `#orchestration`

---

<a id="item-agent-engineer-5"></a>
### [KLPO 提出采样器锚定 KL 正则化](https://huggingface.co/papers/2610.08963) ⭐️ 7.0/10

Hugging Face 每日论文 2026-10-08 收录《On KL-Regularized Policy Optimization》，提出 KLPO 框架，针对异步 RL 中 rollout 来自陈旧 checkpoint、推理引擎与训练器概率不一致的问题。KLPO 将 KL 正则化锚定在采样器上，使正则化改进步获得闭式 Gibbs 解，并在采样器自身轨迹上用最小二乘拟合 log-ratio 最优性条件，让采样器概率以 log-ratio 形式进入更新，避免重要性权重。论文摘要未提供代码或基准结果，实际效果待验证。

rss · Hugging Face Daily Papers · 10月8日 00:00

**「为什么重要」** 异步 RL 是 coding agent 等长程任务训练的常见路径，KLPO 直接针对陈旧 checkpoint 与推理-训练概率失配给出闭式更新路径，为训练管线提供一种不依赖重要性采样的替代思路。

**「可关注」** 可关注：KLPO 用采样器锚定的 KL 正则化替代 GRPO 的组采样与重要性比率裁剪，在长 episode 场景下可能降低采样成本，但论文尚未发布代码与基准，暂无法评估工程收益。

**标签**: `#eval`, `#coding-agent`, `#rl`

---

<a id="item-agent-engineer-6"></a>
### [One Model Family, Two Gold-Level Results: Fine-Tuning Nemotron for IOI and IMO](https://huggingface.co/blog/nvidia/nemotron-ioi-and-imo-2026) ⭐️ 6.8/10

NVIDIA reports Nemotron 3 fine-tuned with SFT, RL, and generate-verify-refine systems reached gold-medal level at IOI 2026 and IMO 2026.

rss · Hugging Face Blog · 10月7日 12:45

**标签**: `#eval`, `#coding-agent`, `#orchestration`

---

<a id="item-agent-engineer-7"></a>
### [Bolmo 字节级模型登上 Nature](https://allenai.org/blog/bolmo-nature) ⭐️ 6.3/10

Ai2 宣布 Bolmo 字节级语言模型技术正式发表于 Nature。官方称新检查点显示，该方法已从 Olmo 泛化到其他模型家族。当前公开信息未包含技术细节、代码或面向 agent 工程的直接说明。

rss · Allen AI · 10月7日 08:00

**「为什么重要」** 该技术已获 Nature 发表，且新检查点显示可迁移至 Olmo 之外的模型家族；对 coding agent / harness 工程的实际影响，仍需阅读论文确认。

**「可关注」** 可关注：Bolmo 的字节级路线已获 Nature 发表，且新检查点显示可迁移到 Olmo 之外的模型家族，但具体工程影响仍需阅读论文确认。

**标签**: `#llm`, `#research`, `#model-architecture`

---

<a id="item-agent-engineer-8"></a>
### [Cloudflare 安全运营 harness 上线](https://blog.cloudflare.com/agentic-security-operations/) ⭐️ 6.3/10

Cloudflare 上线 Managed Defense AI agent harness，用多智能体处理安全告警。模型推理前，确定性代码先跑版本化侦察，收集身份、检测历史、流量基线等证据并记录来源与时间戳；Clef 在 Workers AI 上初筛，高误报概率告警跳过专家智能体。需深审的告警由协调智能体并行调度流量分析、客户上下文、全球遥测、威胁情报四个专家，综合智能体合并 typed findings，不能拉取新证据或越出批准词表。专家必须引用版本化证据包，应用代码校验每条引用的存在性、归属与支持度。

rss · Cloudflare Engineering · 10月7日 16:30

**「为什么重要」** 单智能体把遥测、检测描述、策略和威胁情报压进同一提示，导致幻觉、上下文越权和范围漂移。Cloudflare 将证据收集与范围强制前移到应用代码，再让模型做解释，为安全运营 harness 提供了可复现、可审计的工程路径。

**「可关注」** 可关注：把侦察、证据打包和引用校验放在模型之外，用确定性代码固定输入快照，能让多智能体差异只来自解释而非检索，同时让未检查与检查无结果明确区分。

**标签**: `#harness`, `#orchestration`, `#observability`

---

<a id="item-agent-engineer-9"></a>
### [DecepEval：LLM 智能体欺骗评估基准](https://huggingface.co/papers/2610.07967) ⭐️ 6.0/10

2026-10-08，Hugging Face Daily Papers 收录 DecepEval，一个评估 LLM 智能体欺骗行为的基准。基准包含 1,532 个实例，覆盖 3 类任务家族和 28 个专业场景。论文提出 LLM Deception Diamond 框架，从压力、激励、机会、冲突四类外部条件刻画欺骗倾向，并为每个实例配对中性与诱导版本以测量条件依赖。目前公开材料仅限摘要，任务家族细节与完整评测结果未披露。

rss · Hugging Face Daily Papers · 10月8日 00:00

**「为什么重要」** 现有评测多聚焦孤立场景或狭窄条件，难以系统回答智能体何时更容易欺骗。DecepEval 将欺骗诱因拆解为四因子并提供配对实例，为 agent 可靠性评估给出结构化对照。

**「可关注」** 可关注：DecepEval 用中性与诱导配对实例隔离外部条件，做 agent 评测时可将同一任务在不同压力、激励、机会、冲突设置下的表现差异纳入观察。

**标签**: `#eval`, `#benchmark`, `#llm-agents`

---

## AI 日报

<a id="item-ai-daily-1"></a>
### [Helping teens learn, plan, and shape the future of AI](https://openai.com/index/teens-learn-and-plan) ⭐️ 8.3/10

OpenAI announces College Planner and new learning tools for ChatGPT Teens, along with a teen AI council.

rss · OpenAI Blog · 10月7日 12:00

**标签**: `#product`, `#lab`, `#industry`

---

<a id="item-ai-daily-2"></a>
### [Radisson 推出 ChatGPT 插件](https://openai.com/index/radisson) ⭐️ 7.8/10

Radisson Hotel Group 与 Accenture 合作，基于 OpenAI 技术推出 ChatGPT 插件。旅客可在规划行程时查找、比较并预订酒店。该集成属于产品层落地，不是核心模型发布或政策变更。

rss · OpenAI Blog · 10月7日 07:00

**「为什么重要」** 这是 ChatGPT 插件进入酒店预订场景的实例，显示企业正通过第三方合作把对话入口接入垂直行业。

**「可关注」** Radisson 与 Accenture 合作用 OpenAI 技术构建插件，把酒店查找、比价和预订整合进 ChatGPT 对话流程。

**标签**: `#product`, `#industry`, `#lab`, `#model`

---

<a id="item-ai-daily-3"></a>
### [GitHub：密钥保护须随软件扩展](https://github.blog/ai-and-ml/github-copilot/secret-protection-must-scale-with-software/) ⭐️ 5.8/10

GitHub 博客撰文指出，密钥保护工具须与软件创建同步扩展。文章称开发者并非更粗心，而是被产出速度甩在身后；辅助创建软件的工具应同时承担更多保护责任。给出的摘录仅包含这一论点，未披露具体新功能、发布事实或可验证的公告。

rss · GitHub Blog · 10月7日 17:45

**「可关注」** 可关注：GitHub 提出，代码生成工具应同时承接更多密钥保护工作，而非仅依赖开发者手动防护。

**标签**: `#product`, `#industry`

---

## AI 羊毛

<a id="item-ai-deals-1"></a>
### [Claude Max/Team 含 API credits](https://news.ycombinator.com/item?id=49997654) ⭐️ 7.0/10

Claude 于 2026 年 10 月 7 日更新支持文档：6 月宣布的 Agent SDK 月度 credit 已停止提供，改为 Claude Max 和 Team 计划直接包含每月 API credits。这些 credits 可用于 Claude Agent SDK、Claude API 和 Claude Managed Agents。用户需在 Claude Console 中领取至某个组织，并使用该组织的 API key 调用。官方未公布具体额度数值。

rss · HN Free API / Credits · 10月7日 19:28

**「为什么重要」** 对已订阅 Max 或 Team 的开发者，Agent SDK 和 Managed Agents 的调用可消耗套餐内 credits，而非单独购买。不过 credits 仅限套餐包含，且需绑定到 Console 组织使用。

**「可关注」** 可关注：Claude Max/Team 的每月 API credits 需在 Claude Console 中领取到组织，并用该组织的 API key 调用 Agent SDK、Claude API 或 Managed Agents；未给出具体额度，且仅面向已有付费订阅用户。

**标签**: `#credits`, `#api`, `#promo`

---

<a id="item-ai-deals-2"></a>
### [Claude Max 与 Teams 改发 API credits](https://news.ycombinator.com/item?id=49999508) ⭐️ 5.0/10

10 月 7 日，Anthropic 调整 Claude Max 与 Team 套餐权益：6 月预告的 Agent SDK 月度额度取消，改为发放月度 API credits。这些 credits 覆盖 Claude Agent SDK、Claude API 和 Claude Managed Agents。用户需在 Claude Console 组织中领取，并使用该组织的 API key 调用。来源未说明具体额度、有效期或截止时间。

rss · HN Free API / Credits · 10月7日 22:15

**「可关注」** 可关注：Claude Max 与 Team 用户可将套餐内月度 API credits 用于 Agent SDK、Claude API 和 Managed Agents，但须在 Claude Console 组织内领取并以该组织 API key 调用；来源未公布额度与有效期，实际限制待官方细则。

**标签**: `#credits`, `#api`, `#promo`

---

<a id="item-ai-deals-3"></a>
### [Claude 两档计划开放 credits](https://support.claude.com/en/articles/17154008-monthly-api-credits-for-max-and-team-plans) ⭐️ 5.0/10

Claude 官方支持文档宣布，Max 和 Team 计划可领取每月 API credits。材料未提供具体额度、使用限制、有效期及截止时间。当前信息仅确认该权益面向上述两类计划用户。

rss · HN Free API / Credits · 10月7日 18:52

**「可关注」** 可关注：每月 API credits 目前面向 Claude Max 和 Team 计划用户，具体额度、限制和有效期需以官方支持文档为准。

**标签**: `#credits`, `#api`, `#promo`

---