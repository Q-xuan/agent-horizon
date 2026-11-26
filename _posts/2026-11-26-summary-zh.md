---
layout: default
title: "Horizon Summary: 2026-11-26 (ZH)"
date: 2026-11-26
lang: zh
---

> 从 177 条内容中筛选出 7 条重要资讯。

<nav id="ah-toc" class="ah-toc" aria-label="目录"><span class="ah-toc-title">目录</span><ul><li><a href="#sec-harness-arch"><span class="ah-toc-name">Harness 架构</span><span class="ah-toc-count">4条</span></a></li><li><a href="#sec-agent-engineer"><span class="ah-toc-name">Agent 工程师日报</span><span class="ah-toc-count">1条</span></a></li><li><a href="#sec-ai-daily"><span class="ah-toc-name">AI 日报</span><span class="ah-toc-count">1条</span></a></li><li><a href="#sec-ai-deals"><span class="ah-toc-name">AI 羊毛</span><span class="ah-toc-count">1条</span></a></li></ul></nav>

---

**[Harness 架构](#sec-harness-arch)**
1. [Mastra core 1.86.0 发布](#item-harness-arch-1) ⭐️ 8.8/10
2. [pydantic-ai v2.75.0 发布](#item-harness-arch-2) ⭐️ 7.8/10
3. [Cloudflare Search for Agents 发布](#item-harness-arch-3) ⭐️ 5.8/10
4. [Cloudflare Agents 0.34.1 发布](#item-harness-arch-4) ⭐️ 5.5/10

**[Agent 工程师日报](#sec-agent-engineer)**
1. [CUGA 多语言语音代理用例公开](#item-agent-engineer-1) ⭐️ 6.8/10

**[AI 日报](#sec-ai-daily)**
1. [GitHub 发布应用现代化安全步骤指南](#item-ai-daily-1) ⭐️ 6.8/10

**[AI 羊毛](#sec-ai-deals)**
1. [林易 API 回帖加群送$18 额度](#item-ai-deals-1) ⭐️ 7.0/10

---

## Harness 架构
{: #sec-harness-arch .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-harness-arch" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-harness-arch-1"></a>
### [Mastra core 1.86.0 发布](https://github.com/mastra-ai/mastra/releases/tag/%40mastra/core%401.86.0) ⭐️ 8.8/10

Mastra core 1.86.0 正式发布，核心引入 durable crash-safe 执行模型。实验与 Agent 均支持事件化工作流，崩溃或重部署后可由其他 worker 继续未完成项，线程状态新增 \`interrupted\`。新增实验性 Knowledge importer 基础设施，提供持久化 bookkeeping、batching、leases 与 settle/repair 语义。同时扩展 channel 工具与 Knowledge 活动查询能力，并包含多项 breaking changes。

github · PaulieScanlon · 11月25日 10:00

**「设计要点」** 运行时采用 pubsub 驱动的 durable evented workflow，worker 崩溃后通过 redeliver 恢复未 ack 项，线程状态区分 \`interrupted\` 与 \`failed\`。Knowledge 层引入 importer-runner 与持久化 bookkeeping，与 page 数据同库同事务；Agent 执行引擎支持 durable/default 切换，记忆层新增 \`getWorkingMemoryInstruction\(\)\` 注入机制。

**「改了什么」** \`startExperimentAsync\(\)\` 支持 \`durable: true\`，实验变为事件化工作流。Agent 可通过 \`durable.executionEngine\` 选择原生 durable 引擎，旧值 \`executionEngine: &\#x27;durable&\#x27;\` 改为 \`&\#x27;default&\#x27;\`。新增 \`knowledge.importers.run\(\)\`、\`KnowledgeImporter\` 契约、\`knowledge\_activity\` 工具、\`createChannelTools\(\)\` 及 Slack 工具集。\`get\_process\_output\` 移除 \`wait: true\`，改用 \`waitSeconds\` \(1–300\)。

**标签**: `#runtime`, `#agent-execution`, `#workflow`, `#knowledge`

---

<a id="item-harness-arch-2"></a>
### [pydantic-ai v2.75.0 发布](https://github.com/pydantic/pydantic-ai/releases/tag/v2.75.0) ⭐️ 7.8/10

pydantic-ai v2.75.0 发布，核心变更包括工作区文件权限与上下文注入规则重构、模型响应错误分类细化、Pax 权限审批改为 token 驱动，以及 Gemini 模型思考 token 计入输出统计。低于 \`&\#x27;operator&\#x27;\` 权限的工作区文件不再进入 \`RepoContext\`、\`Skills\` 和 \`Memory\` 的系统指令，改为通过 framed data 或工具接口传递；\`RepoContext\(autoload\_instructions=False\)\` 升级后首次请求会错过 prompt cache。Durable run 在启动时记录额外 \`realpath\` 调用，跨引擎（Temporal、DBOS、Prefect、Lambda）行为存在差异；已降低 MCP 能力的 in-flight runs 在 Temporal/DBOS 上可能遇到不确定性错误。新增 \`RunContext.submit\_output\(\)\`、Temporal \`ExternalEventWaiter\`，\`ClearToolResults\` 支持目标工具和保留回合；Gemini \`thinking=False\` 临时发送 \`thinking\_budget=128\` 直至 2026-12-01 重定向，\`Coder\` 的 delegation 禁令改为按模型 \`delegates\_unprompted\` 标志发送。

github · dsfaccini · 11月25日 18:21

**「设计要点」** 权限分层（\`operator\` 及以下）现在决定工作区文件是进入系统指令还是作为 framed data 传递，影响 \`RepoContext\`、\`Skills\`、\`Memory\` 和 MCP 能力的上下文注入路径。Durable run 引擎对 token handler 和审批流程有差异化实现：Temporal/DBOS 支持持久等待，Lambda 不支持，Prefect 重试可能重复执行已完成请求。指令现在可以按模型分支：\`Coder\` 的 delegation 规则仅对设置 \`delegates\_unprompted\` 的模型发送，且 \`ModelMessagesTypeAdapter\` 在历史中共享相同 \`instructions\` 字符串对象。

**「改了什么」** 工作区文件权限低于 \`&\#x27;operator&\#x27;\` 后，\`RepoContext\` 改发祖先文件 framed data，\`Skills\` 改由 \`list\_skills\`/\`load\_skill\` 提供，\`Memory\` 改归因到 \`MEMORY.md\`，并新增 \`lowest\_authority\_under\`；\`FallbackModel\` 和 \`ModelFallback\` 现在回退空响应、无 \`choices\` 的 OpenAI 完成及非 JSON 响应，对应新错误 \`ModelEmptyResponseError\` 和 \`ModelInvalidResponseError\` 均继承 \`ModelAPIError\`，注意 \`except ModelAPIError\` 若置于 \`except UnexpectedModelBehavior\` 之前将优先捕获；Pax 审批 handler 改为接收 resume token，非 Lambda durable run 中抛出 \`UserError\`。新增 \`RunContext.submit\_output\(\)\`、Temporal \`ExternalEventWaiter\`，\`ClearToolResults\` 支持目标工具和保留回合；Gemini \`thinking=False\` 临时发送 \`thinking\_budget=128\` 直至 2026-12-01 重定向，\`Coder\` 的 delegation 禁令改为按模型 \`delegates\_unprompted\` 标志发送。

**标签**: `#permissions`, `#tools`, `#memory`, `#runtime`

---

<a id="item-harness-arch-3"></a>
### [Cloudflare Search for Agents 发布](https://blog.cloudflare.com/search-for-agents/) ⭐️ 5.8/10

Cloudflare 于 2026-11-25 发布 Search for Agents，这是一项面向 AI Agent 的托管搜索服务。用户可在 Cloudflare Dashboard 一键启用，系统自动创建 AI Search 实例、爬取索引站点内容，并在每个页面通过 &lt;meta&gt; 标签或 YAML front matter advertise 搜索端点。Agent 可通过 /.well-known/search 端点以 GET 或 QUERY（RFC 10008）方法发起关键词或自然语言查询，返回 Markdown 格式的检索结果而非生成式回答。该服务对所有客户开放（Free 套餐含限制），并支持与 Markdown for Agents 及现有 WAF、Bot Management 策略协同。

rss · Cloudflare AI · 11月25日 14:00

**「设计要点」** 服务运行在 Cloudflare 边缘网络，通过内容协商（content negotiation）在请求层面自动注入 Agent 可发现的搜索元数据，无需修改源站内容。AI Search 实例默认创建，支持后续调整 reranking 与缓存配置，权限边界受域名级 Bot Management、AI Crawl Control 及 WAF 规则约束。

**「改了什么」** 相对此前需手动创建 AI Search 实例并自行集成搜索端点的模式，新功能将实例创建、内容索引、端点暴露及可发现性配置全部自动化，Agent 可直接通过标准化的 /.well-known/search 接口消费站点内容。同时新增对 HTTP QUERY 方法（RFC 10008）的原生支持，允许 Agent 以安全、幂等的方式在请求体中传递查询条件。

**标签**: `#tools`

---

<a id="item-harness-arch-4"></a>
### [Cloudflare Agents 0.34.1 发布](https://github.com/cloudflare/agents/releases/tag/agents%400.34.1) ⭐️ 5.5/10

Cloudflare Agents 发布 0.34.1 patch 版本。本次更新包含 Pi 工具接口破坏性变更，parking 工具需改用 \`\{ kind: &quot;sleep&quot;, signals, until \}\` 结构，signal 状态改为 \`\{ kind: &quot;value&quot;, value \}\` 或 \`\{ kind: &quot;expired&quot; \}\`。同步升级 Pi AI 1.6.1 集成，\`agents/models\` SSE 解码器改为线性时间读取大型流式事件。

github · github-actions\[bot\] · 11月25日 20:07

**「设计要点」** Pi harness 内置重试逻辑处理 \`finish\_reason: &quot;error&quot;\` 及 OpenRouter 无输出失败场景，\`onResponse\` 回调暴露全部响应（含失败）供上层处理。SSE 解码器采用线性时间算法处理大型流式事件。

**「改了什么」** Pi 工具 parking 接口改为 \`\{ kind: &quot;sleep&quot;, signals, until \}\` 结构，旧格式返回空结果。\`agents/models/pi-ai\` 升级至 pi-ai 1.6.1，新增 \`finish\_reason: &quot;error&quot;\` 失败重试、\`rawStopReason\` 记录及 \`onResponse\` 全量响应可见，SSE 解码器优化为线性时间读取大型流式事件。

**标签**: `#tools`, `#runtime`

---

## Agent 工程师日报
{: #sec-agent-engineer .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-agent-engineer" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-agent-engineer-1"></a>
### [CUGA 多语言语音代理用例公开](https://huggingface.co/blog/ibm-research/an-indic-voice-agent-with-cuga) ⭐️ 6.8/10

2026 年 11 月 25 日 Hugging Face 博客公开 IBM Research 开源代理框架 CUGA 的 Indic 语言（印度地方语言）农业语音代理用例。该用例将 CUGA 作为文本核心大脑，前后端仅叠加语音转文字、文字转语音薄层，解决 CUGA 默认英文嵌入模型导致的跨语言检索失效问题：替换为 intfloat/multilingual-e5-large 多语言嵌入后，单份英文农业手册即可支持多语言查询检索；同时设置 OFF\_TOPIC 话题护栏标记，对农业外问题直接重定向，无需二次 LLM 调用，保障响应速度。CUGA 曾在 AppWorld 代理基准测试中排名第一，当前博客已提供可在线试用的 CUGA Apps 示例与从零搭建的配套教程，同时提及 CUGA 可与 IBM Bharat Core 搭配构建符合印度数据主权要求的合规 AI 方案；但公开内容截断，未包含该语音代理的完整技术实现细节与专属性能数据。

rss · Hugging Face Blog · 11月25日 10:22

**「为什么重要」** 这是目前少有的公开多语言语音 agent 落地全路径的官方用例，明确给出了跨语言检索的典型问题与低成本解决方案，同时配套可在线试用实例与从零教程，降低了相关场景的复现门槛。目前尚未公开该代理在真实农业场景的落地效果数据，也未披露 CUGA 框架的后续迭代计划。

**「可关注」** 可关注：多语言 agent 开发中优先验证跨语言检索准确性，再调整 prompt；同时可将语音能力作为独立薄层与文本核心 agent 解耦，用轻量标记实现话题护栏避免额外 LLM 调用成本。

**标签**: `#harness`, `#eval`

---

## AI 日报
{: #sec-ai-daily .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-daily" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-daily-1"></a>
### [GitHub 发布应用现代化安全步骤指南](https://github.blog/ai-and-ml/github-copilot/how-to-choose-the-next-safe-step-in-application-modernization/) ⭐️ 6.8/10

GitHub 官方 AI 博客发布证据优先的应用现代化指南，配套教程演示如何将该流程编码为 GitHub Copilot agent skill。该方法已在 4 个公开应用（涵盖小型 Node.js 游戏到大型 Java ERP 系统）上完成验证，整体流程可复现。该内容不涉及新模型发布、重大政策或产品更新，新闻价值为中等。

rss · GitHub Blog · 11月25日 15:00

**「为什么重要」** 该指南提供了可复现的应用现代化决策框架，配套 Copilot agent skill 教程降低了团队落地证据优先改造流程的门槛，对做 AI 辅助开发的技术团队有直接参考价值。

**「可关注」** 可关注：应用现代化优先按「保留、升级、替换、包装、重写」的渐进顺序决策，仅在存在已知未修复漏洞、依赖不兼容或可靠性不达标等明确证据时才选择更高侵入性的改造方案。

**标签**: `#product`, `#industry`, `#open-source`

---

## AI 羊毛
{: #sec-ai-deals .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-deals" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-deals-1"></a>
### [林易 API 回帖加群送$18 额度](https://www.v2ex.com/t/1259773#reply52) ⭐️ 7.0/10

林易 API 团队在 V2EX 推出推广活动，用户完成回帖、加群操作可分别领取 8 美元、10 美元 API 调用额度，合计 18 美元。该额度无有效期，可用于平台所有按量计费模型，平台支持 Claude、GPT、Gemini 等多家模型，GPT 最低至官方 1.35 折。领取需满足每个 V2EX 账号、每个林易账号每份福利各限领 1 次，回帖需留注册邮箱前缀，加群需进指定 QQ 群发送指定信息，活动长期有效。

rss · V2EX Hot · 11月25日 09:12

**「为什么重要」** 额度无有效期，且支持 Claude Code、Codex CLI 等常用客户端，仅需修改 Base URL 和 Key 即可接入，适合需要低成本调用多模型 API 的开发者快速试用。

**「可关注」** 可关注：赠送额度仅可用于按量计费模型，不能购买套餐或退款，批量注册小号领额度的行为会被扣除额度。

**标签**: `#credits`, `#promo`, `#api`

---