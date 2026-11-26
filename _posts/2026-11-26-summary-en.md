---
layout: default
title: "Horizon Summary: 2026-11-26 (EN)"
date: 2026-11-26
lang: en
---

> From 177 items, 7 important content pieces were selected

---

**Agent Harness Architecture**
1. [Mastra core 1.86.0 released](#item-harness-arch-1) ⭐️ 8.8/10
2. [pydantic-ai v2.75.0 发布](#item-harness-arch-2) ⭐️ 7.8/10
3. [Cloudflare Search for Agents 发布](#item-harness-arch-3) ⭐️ 5.8/10
4. [Cloudflare Agents 0.34.1 发布](#item-harness-arch-4) ⭐️ 5.5/10

**AI Agent Engineer**
1. [CUGA Indic 农业语音代理案例发布](#item-agent-engineer-1) ⭐️ 6.8/10

**AI Daily**
1. [GitHub Copilot 应用现代化证据优先指南](#item-ai-daily-1) ⭐️ 6.8/10

**AI Deals**
1. [林易API 回帖加群送$18额度](#item-ai-deals-1) ⭐️ 7.0/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [Mastra core 1.86.0 released](https://github.com/mastra-ai/mastra/releases/tag/%40mastra/core%401.86.0) ⭐️ 8.8/10

Mastra core 1.86.0 ships durable crash-safe execution for experiments and agents, plus experimental knowledge importer infrastructure. Experiments accept \`durable: true\` on \`startExperimentAsync\(\)\` and trigger APIs, running as evented workflows where pubsub workers \(e.g., Redis Streams\) pick up unacked items after redeploys or crashes. Agents can select native durable execution via \`durable.executionEngine\` \(agent-level or \`Mastra.durable\` defaults\) while keeping streaming APIs; the prerelease value \`executionEngine: &\#x27;durable&\#x27;\` is now \`executionEngine: &\#x27;default&\#x27;\`. The experimental Knowledge importer introduces a \`KnowledgeImporter\` contract, \`knowledge.importers.run\(\)\`, and persisted bookkeeping in in-memory, LibSQL, and Postgres stores, delivering batching, leases, replay protection, and settle/repair semantics. The release also adds \`createChannelTools\(\)\` and \`@mastra/slack\`&\#x27;s \`createSlackTools\(\)\`, the \`knowledge\_activity\` tool for date-range change queries, and host-run \`principals\`/\`author\` for MCP scenarios. Breaking changes: \`get\_process\_output\` removes \`wait: true\` \(use \`waitSeconds\` 1–300\); \`@mastra/connect\` replaces legacy events exports with a \`ConnectEvents\` iterator API; \`@mastra/mcp-apps-components\` renames \`projectId\` to \`project\`; \`@mastra/playground-ui\` traces components undergo major breaking API changes.

github · PaulieScanlon · Nov 25, 10:00

**「Architecture Note」** Durable execution relies on evented workflows with pubsub redelivery to recover from crashes, letting any worker resume unacked items. Knowledge importer bookkeeping lives in the same database and namespace as pages, committing atomically in \`knowledge.transaction\(\)\` and supporting optional \`deadlineAt\` timeouts \(enforced on Postgres\). The durable Agent engine integrates at the agent or global level without breaking existing streaming interfaces.

**「What Changed」** Adds durable crash-safe dataset experiments \(\`startExperimentAsync\` with \`durable: true\`\), native durable Agent execution engine \(\`executionEngine: &\#x27;default&\#x27;\`\), experimental Knowledge importer infrastructure with persisted bookkeeping and reliability guarantees, \`createChannelTools\(\)\` and Slack toolset, \`knowledge\_activity\` tool, host-run \`principals\`/\`author\` for Knowledge tools, \`interrupted\` thread run status, \`getWorkingMemoryInstruction\(\)\` on \`MastraMemory\`, optimistic concurrency via \`expected\` on \`Knowledge.removePage\`/\`upsertPage\`, and Knowledge storage transaction \`deadlineAt\`. Breaking changes: \`get\_process\_output\` drops \`wait: true\` \(use \`waitSeconds\` 1–300\); \`@mastra/connect\` swaps \`EventsClient\`/\`connectEvents\(\)\` for \`ConnectEvents\` iterator; MCP boundary field \`projectId\` becomes \`project\`; playground-ui traces components shift to slot-based APIs with data-in/no-fetch patterns and navigation callbacks.

**Tags**: `#runtime`, `#agent-execution`, `#workflow`, `#knowledge`

---

<a id="item-harness-arch-2"></a>
### [pydantic-ai v2.75.0 发布](https://github.com/pydantic/pydantic-ai/releases/tag/v2.75.0) ⭐️ 7.8/10

pydantic-ai v2.75.0 发布，引入工作区文件权限注入、技能工具接口、内存快照及持久化运行行为的破坏性变更。低于 \`operator\` 权限的工作区文件不再进入 \`RepoContext\`、\`Skills\` 和 \`Memory\` 的指令，\`Skills\` 工具从 \`load\_capability\` 改为 \`list\_skills\` 与 \`load\_skill\`。持久化运行启动时记录额外 \`realpath\` 工作区调用，需完成在途运行或通过 Temporal worker 版本控制/DBOS 应用版本升级。空模型响应与无效响应改为 \`ModelEmptyResponseError\` 与 \`ModelInvalidResponseError\`，\`FallbackModel\` 与 \`ModelFallback\` 默认触发回退。

github · dsfaccini · Nov 25, 18:21

**「设计要点」** 框架通过 \`lowest\_authority\_under\` 实现权限分级上下文注入，低于阈值的工作区文件仅以 framing data 或工具形式提供。持久化运行在 Temporal、DBOS、Prefect 及 AWS Lambda 上通过 \`HandleDeferredToolCalls\` 令牌处理器和 \`ExternalEventWaiter\` 管理工具审批与恢复。

**「改了什么」** 工作区文件权限低于 \`operator\` 时，\`RepoContext\`、\`Skills\` 和 \`Memory\` 不再将其内容注入系统提示，\`Skills\` 工具接口替换为 \`list\_skills\` 与 \`load\_skill\`。空流、无 \`choices\` 的 OpenAI 响应及非 JSON 响应改为 \`ModelEmptyResponseError\` 与 \`ModelInvalidResponseError\` 并纳入回退链，Gemini 思考令牌计入 \`OpenAIChatModel\` 输出令牌，\`Coder\` 的禁止未请求子代理指令仅发送给设置 \`delegates\_unprompted\` 的模型，\`gemini-2.5-flash\` 的 \`thinking=False\` 在 2026-12-01 前发送 \`thinking\_budget=128\`。

**Tags**: `#permissions`, `#tools`, `#memory`, `#runtime`

---

<a id="item-harness-arch-3"></a>
### [Cloudflare Search for Agents 发布](https://blog.cloudflare.com/search-for-agents/) ⭐️ 5.8/10

Cloudflare 推出 Search for Agents，将 AI Search 实例创建、内容索引和 Agent 可发现性配置封装为控制台一键开关。服务在边缘网络层自动为域名创建索引，并通过 \`/.well-known/search\` 端点暴露搜索能力，同时原生支持新 HTTP QUERY 方法（RFC 10008）。Agent 可通过 HTML \`&lt;head&gt;\` 元数据或 Markdown YAML front matter 自动发现搜索接口，返回 Markdown 格式检索结果而非生成式回答。

rss · Cloudflare AI · Nov 25, 14:00

**「设计要点」** 服务运行在 Cloudflare 边缘网络，通过内容协商和网络层转换实现自动索引与端点暴露，无需用户搭建检索基础设施。搜索能力受域名现有 bot management、AI Crawl Control 及 WAF 配置约束。

**「改了什么」** 相对此前需手动创建 AI Search 实例并自行集成端点，Search for Agents 将初始化、索引和发现机制全部自动化，开箱即用。新增对 HTTP QUERY 方法的原生支持，允许 Agent 以安全且幂等的方式发送搜索请求体。

**「评论」** 无社区评论。

**Tags**: `#tools`

---

<a id="item-harness-arch-4"></a>
### [Cloudflare Agents 0.34.1 发布](https://github.com/cloudflare/agents/releases/tag/agents%400.34.1) ⭐️ 5.5/10

Cloudflare Agents 发布 0.34.1 patch 版本。本次更新包含 Pi 工具接口的破坏性变更、Pi AI 1.6.1 集成调整及 SSE 解码器性能改进。Pi 工具停车接口从 \`\{ sleep: \{ ... \} \}\` 改为 \`\{ kind: &quot;sleep&quot;, signals, until \}\`，信号状态改为 \`\{ kind: &quot;value&quot;, value \}\` 或 \`\{ kind: &quot;expired&quot; \}\`；旧接口仍可编译但返回空结果。\`agents/models/pi-ai\` 升级至 pi-ai 1.6.1，流式聊天补全以 \`finish\_reason: &quot;error&quot;\` 结束时触发错误并进入重试，\`rawStopReason\` 记录提供方原始停止原因，OpenRouter 无输出且原生原因失败时视为可重试错误，\`onResponse\` 回调现在接收全部响应（含失败）。\`agents/models\` SSE 解码器改为线性时间读取大型流式事件。

github · github-actions\[bot\] · Nov 25, 20:07

**「改了什么」** Pi 工具停车接口发生破坏性变更，旧返回结构仍编译但结果为空，需同步更新工具实现。Pi AI 模型集成升级至 1.6.1，调整流式错误处理与重试逻辑，SSE 解码器优化大型事件读取性能。

**Tags**: `#tools`, `#runtime`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [CUGA Indic 农业语音代理案例发布](https://huggingface.co/blog/ibm-research/an-indic-voice-agent-with-cuga) ⭐️ 6.8/10

IBM Research 开源 CUGA（Configurable Generalist Agent） 代理框架，并在 Hugging Face Spaces 发布 Indic 语言农业语音代理示例。代理采用语音-文本-语音双层架构，核心为文本输入输出的 CUGA 引擎，支持 Sarvam AI 云端 API 或 SraVaani/Svara 开源语音模型。关键设计包括采用 intfloat/multilingual-e5-large 多语言嵌入模型解决印地语问题检索英文文档的跨语言检索问题，以及 OFF\_TOPIC guardrail 直接重定向至农业话题，避免二次 LLM 调用。文章未包含该语音代理的完整代码实现或性能基准数据。

rss · Hugging Face Blog · Nov 25, 10:22

**「为什么重要」** 该案例展示了语音接口与文本代理框架解耦的实用模式，对构建多语言语音代理的工程师有直接参考价值。CUGA 作为开源框架且在 AppWorld 基准测试中处于领先地位，为语音代理开发提供了可复用的基础组件。

**「可关注」** 可关注：多语言嵌入模型替换是跨语言 RAG 的关键路径，应在调优提示词前先验证非英语查询的检索召回率。

**Tags**: `#harness`, `#eval`

---

## AI Daily

<a id="item-ai-daily-1"></a>
### [GitHub Copilot 应用现代化证据优先指南](https://github.blog/ai-and-ml/github-copilot/how-to-choose-the-next-safe-step-in-application-modernization/) ⭐️ 6.8/10

GitHub 官方 AI 博客发布应用现代化证据优先方法论，作者 Sam Quakenbush 在 4 个公开应用（从小型 Node.js 游戏到大型 Java ERP 系统）上验证了该流程的可重复性。文章要求先建立包含清单文件、运行时锁定版本、外部契约和已终止维护依赖的证据清单，并标注「已记录/推断/未验证」三种不确定性状态；再按「保留、升级、替换、包装、重写」的决策顺序选择最小改动的处理方式。根据限时可行性检查结果，流程分为「先捕获行为再升级」和「先构建小型现代切片」两条路径，并引入 L0 到 L4 五级回归保护强度。文章同时演示了如何将该流程编码为 GitHub Copilot agent skill，同时保留架构决策权给系统负责人。

rss · GitHub Blog · Nov 25, 15:00

**「为什么重要」** 该指南将应用现代化从技术选型提问转为可重复的证据收集流程，并直接演示了如何将其固化为 GitHub Copilot agent skill，对正在评估 AI 辅助重构的团队有直接参考价值。

**「可关注」** 可关注：文章提出的五级回归保护强度（L0–L4）和「保留、升级、替换、包装、重写」决策顺序，可直接用于评估自动化重构脚本的安全边界。

**Tags**: `#product`, `#industry`, `#open-source`

---

## AI Deals

<a id="item-ai-deals-1"></a>
### [林易API 回帖加群送$18额度](https://www.v2ex.com/t/1259773#reply52) ⭐️ 7.0/10

林易API团队在V2EX发布推广活动，用户完成回帖、加群操作可分别领取8美元、10美元API调用额度，合计18美元；领取条件为在推广帖回帖留注册邮箱前缀或用户名、加入指定QQ群发送完整注册信息，每个V2EX账号、每个林易账号每份福利各限领1次；额度无有效期，可用于平台所有按量计费模型，活动长期有效（帖子存在即持续生效）。

rss · V2EX Hot · Nov 25, 09:12

**「为什么重要」** 额度无有效期，且平台支持Claude Code、Codex CLI等常用客户端，仅需修改Base URL和Key即可接入，GPT按量最低达官方1.35折，适合有API调用需求的开发者低成本试用。

**「可关注」** 可关注：赠送额度仅可用于按量计费模型，不可购买套餐或退款；创建API Key时需选择分组，分组决定可调用模型范围和计费倍率；每个V2EX账号、林易账号每份福利各限领1次，批量注册小号会被扣除额度。

**Tags**: `#credits`, `#promo`, `#api`

---