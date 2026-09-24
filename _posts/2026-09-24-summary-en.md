---
layout: default
title: "Horizon Summary: 2026-09-24 (EN)"
date: 2026-09-24
lang: en
---

> From 220 items, 17 important content pieces were selected

---

**Agent Harness Architecture**
1. [Claude Code v2.1.281 发布](#item-harness-arch-1) ⭐️ 8.8/10
2. [Mastra Core 1.68.0 Ships MCP v2, New Vector Backends, and Trace Pagination](#item-harness-arch-2) ⭐️ 8.8/10
3. [modelcontextprotocol/typescript-sdk released @modelcontextprotocol/node@2.1.0](#item-harness-arch-3) ⭐️ 8.8/10
4. [block/goose released v1.52.0](#item-harness-arch-4) ⭐️ 7.8/10
5. [mem0 v2.2.0 发布](#item-harness-arch-5) ⭐️ 7.3/10
6. [Improved token efficiency for longer agent runs](#item-harness-arch-6) ⭐️ 7.3/10
7. [fastmcp v4.0.6 修复多项缺陷](#item-harness-arch-7) ⭐️ 6.8/10

**AI Agent Engineer**
1. [Advancing Private AI Compute with secure, server-side memory](#item-agent-engineer-1) ⭐️ 6.3/10

**AI Daily**
1. [OpenAI 向乌克兰开放 Daybreak](#item-ai-daily-1) ⭐️ 8.8/10
2. [OpenAI 发布 MentalHealthBench](#item-ai-daily-2) ⭐️ 8.8/10
3. [GitHub Copilot app 渲染百万行 PR](#item-ai-daily-3) ⭐️ 7.8/10
4. [Sam Altman’s remarks at the United Nations Security Council](#item-ai-daily-4) ⭐️ 6.8/10
5. [Ringg 部署 GPT-5.6 客服代理](#item-ai-daily-5) ⭐️ 6.8/10
6. [GitHub 调研：开发者要求减少算力浪费](#item-ai-daily-6) ⭐️ 6.8/10
7. [Bringing Private Processing to Meta AI Glasses](#item-ai-daily-7) ⭐️ 6.8/10
8. [OpenAI Academy 成立两周年](#item-ai-daily-8) ⭐️ 6.3/10

**AI Creator Radar**
1. [Simon Willison Reports New Gemini 3.8 TTS Models](#item-ai-creator-1) ⭐️ 0.0/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [Claude Code v2.1.281 发布](https://github.com/anthropics/claude-code/releases/tag/v2.1.281) ⭐️ 8.8/10

Claude Code v2.1.281 发布。Gateway 新增桌面端策略 \`blockReadsOutsideWorkingDirectories\` 与 \`disableBypassPermissionsMode\`；Bedrock 上游支持 \`assume\_role\` 经 STS 代入 IAM 角色，可跨 AWS 账号并按开发者分配会话，\`guardrail: \{id, version\}\` 对请求统一应用 Amazon Bedrock guardrail。MCP 在 2026-07-28 协议上支持 URL-mode elicitation，服务端可要求打开浏览器流程。\`settings.json\` 增加 \`&quot;attribution&quot;: false\` 关闭提交与 PR 署名，旧版 CLI 会跳过含该键的文件，跨版本共享需保留对象形式。

github · ashwin-ant · Sep 23, 19:19

**「设计要点」** Gateway 把桌面端策略、Bedrock 身份与 guardrail 收敛到上游配置；MCP elicitation 从本地弹窗扩展到浏览器流程。权限与沙箱修复集中在路径解析、命令替换递归删除、NUL 字节规则匹配和 \`$TMPDIR\` 写入。

**「改了什么」** Gateway 可管 Bedrock 跨账号角色与 guardrail，MCP 支持 URL-mode elicitation；权限系统补掉递归 \`rm\`、NUL 字节规则和 macOS \`/.vol\` 路径绕过，并修掉代理截断、MCP 断连导致的 prompt cache 丢失和恢复会话历史错乱。

**Tags**: `#runtime`, `#mcp`, `#permissions`, `#sandbox`

---

<a id="item-harness-arch-2"></a>
### [Mastra Core 1.68.0 Ships MCP v2, New Vector Backends, and Trace Pagination](https://github.com/mastra-ai/mastra/releases/tag/%40mastra/core%401.68.0) ⭐️ 8.8/10

Mastra 1.68.0 rebuilds the MCP server on the 2026-07-28 revision in @mastra/mcp@2.0.0, dropping the initialize handshake for first-class suspend/resume with signed continuation state. It adds Azure AI Search and Weaviate vector stores, page-based trace pagination with delta polling, and token-budgeted messageHistory trimming. Durable agents stop writing running checkpoints by default. Breaking changes rework Agent Controller stream events and remove legacy MCP transport surfaces.

github · Patrycja-J · Sep 23, 08:40

**「Design Points」** MCP v2 server routes return explicit \{ status: &\#x27;suspended&\#x27;, suspendPayload, resumeSchema \} or \{ status: &\#x27;completed&\#x27;, output \}, using signed self-contained requestState for resumption. Trace queries gain list-compatible page pagination with totals, bounded discovery APIs, and delta polling cursors across core, server, client, and ClickHouse/DuckDB/PG. Memory trimming persists a per-thread boundary so future turns stay within budget without deleting stored messages.

**「What Changed」** @mastra/mcp@2.0.0 removes the initialize handshake and session headers, replaces elicitation with context.suspend\(\)/context.resumeData, and deletes legacy transport surfaces. Agent Controller streams now emit one full message\_start, then ID-addressed message\_update deltas, with message\_end containing only the message ID. Durable agents skip running snapshots unless recovery.durableAgents is &\#x27;auto&\#x27; or shouldPersistSnapshot is overridden.

**Tags**: `#mcp`, `#runtime`, `#tools`, `#memory`, `#eval`

---

<a id="item-harness-arch-3"></a>
### [modelcontextprotocol/typescript-sdk released @modelcontextprotocol/node@2.1.0](https://github.com/modelcontextprotocol/typescript-sdk/releases/tag/%40modelcontextprotocol/node%402.1.0) ⭐️ 8.8/10

MCP TypeScript SDK v2.1.0 introduces request-time OAuth scope challenges for tools, resources, and prompts, enforcing insufficient\_scope via HTTP 403 preflight.

github · github-actions\[bot\] · Sep 23, 15:43

**Tags**: `#mcp`, `#permissions`, `#tools`

---

<a id="item-harness-arch-4"></a>
### [block/goose released v1.52.0](https://github.com/aaif-goose/goose/releases/tag/v1.52.0) ⭐️ 7.8/10

Goose v1.52.0 adds live voice conversations, new provider implementations, recipe parameter limits, and support for additional models.

github · github-actions\[bot\] · Sep 23, 14:59

**Tags**: `#runtime`, `#tools`, `#planning`, `#permissions`

---

<a id="item-harness-arch-5"></a>
### [mem0 v2.2.0 发布](https://github.com/mem0ai/mem0/releases/tag/v2.2.0) ⭐️ 7.3/10

mem0 v2.2.0 为 MemoryClient 和 AsyncMemoryClient 引入 User Profiles。Profile 是按项目配置的 JSON Schema 约束的结构化用户摘要，由 LLM 从该用户记忆中异步生成。生成任务通过 Idempotency-Key 保证重试不重复建 job。同时修复 Valkey 向量库 insert\(\)/update\(\) 中 None 时间戳导致的 TypeError。

github · kartik-mem0 · Sep 23, 19:03

**「设计要点」** Profile 作为常新的 JSON 摘要，把用户记忆压缩为 Schema 驱动的结构化视图；生成走异步 job，客户端用 idempotency\_key 控制重试语义。

**「改了什么」** 新增 get\_profile\(\)、generate\_profile\(\)、get\_profile\_settings\(\)、update\_profile\_settings\(\)、sample\_profiles\(\)、get\_profile\_job\(\) 六个接口；Valkey 存储的 created\_at/updated\_at 判空改为 .get\(\) 真值检查，None 回落默认值，与 Redis provider 对齐。

**Tags**: `#memory`, `#runtime`, `#tools`

---

<a id="item-harness-arch-6"></a>
### [Improved token efficiency for longer agent runs](https://cursor.com/blog/improved-token-efficiency) ⭐️ 7.3/10

Cursor details harness optimizations that cut token costs by 7% via improved context assembly, system prompt trimming, and agent work division.

rss · Cursor Blog · Sep 23, 12:00

**Tags**: `#runtime`, `#memory`, `#tools`, `#mcp`, `#subagents`

---

<a id="item-harness-arch-7"></a>
### [fastmcp v4.0.6 修复多项缺陷](https://github.com/PrefectHQ/fastmcp/releases/tag/v4.0.6) ⭐️ 6.8/10

fastmcp v4.0.6 发布，修复 Client 取消退出时的会话泄漏。资源模板现在匹配客户端实际发送的原始或百分号编码字面量，列表查询参数支持展开式与逗号连接两种形式。补全仅返回调用方可列出的引用；JSON Schema 可加载 float 或超长 length 限制；认证侧缓存 OIDC discovery，并避免 Google access token 进入请求 URL。

github · zzstoatzz · Sep 23, 18:54

**「设计要点」** 会话层在上下文退出前先释放 Client 的会话持有，避免取消场景泄漏；资源匹配按 RFC 6570 §3.1 处理 URI 模板字面量编码；补全可见性与调用方的 list 权限对齐。

**「改了什么」** 相比 v4.0.5，v4.0.6 调整了取消场景下的会话与 stdio 子进程生命周期，扩展资源模板匹配以覆盖百分号编码与逗号连接查询参数，为补全增加可见性校验，并缓存 OIDC discovery 配置。

**Tags**: `#runtime`, `#tools`, `#mcp`, `#permissions`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [Advancing Private AI Compute with secure, server-side memory](https://deepmind.google/blog/advancing-private-ai-compute-with-secure-server-side-memory/) ⭐️ 6.3/10

Google DeepMind announces private, server-side memory for its Private AI Compute platform.

rss · Google DeepMind · Sep 23, 16:00

**Tags**: `#memory`, `#security`, `#infrastructure`

---

## AI Daily

<a id="item-ai-daily-1"></a>
### [OpenAI 向乌克兰开放 Daybreak](https://openai.com/index/openai-extends-cyber-access-to-ukraine-for-civilian-defense) ⭐️ 8.8/10

OpenAI 宣布将 Daybreak 项目扩展至乌克兰政府，支持民用基础设施网络防御。公告发布于 2026 年 9 月 23 日，属官方第一方政策行动，非模型发布。公开信息未披露技术细节与部署规模。

rss · OpenAI Blog · Sep 23, 13:00

**「为什么重要」** 主要 AI 实验室正以具体政策行动介入国家网络防御，而非仅发布模型，对跟踪 AI 政策与安全交叉领域的从业者有参考价值。

**「可关注」** 可关注：OpenAI Daybreak 项目扩展至乌克兰政府，用于民用基础设施网络防御。

**Tags**: `#policy`, `#lab`, `#industry`

---

<a id="item-ai-daily-2"></a>
### [OpenAI 发布 MentalHealthBench](https://openai.com/index/introducing-mentalhealthbench) ⭐️ 8.8/10

OpenAI 发布 MentalHealthBench。这是一个由专家提供依据的基准测试，用于评估 AI 在真实心理健康对话中的有用性与安全性。官方称其覆盖现实场景下的心理健康交流。

rss · OpenAI Blog · Sep 23, 10:00

**「为什么重要」** 心理健康对话对 AI 安全边界要求严格。该基准为此类敏感场景提供了标准化的评估工具。

**「可关注」** 可关注：MentalHealthBench 将有用性与安全性纳入同一评估框架，可用于检验模型在心理健康对话中的表现。

**Tags**: `#lab`, `#eval`, `#product`

---

<a id="item-ai-daily-3"></a>
### [GitHub Copilot app 渲染百万行 PR](https://github.blog/engineering/user-experience/rendering-huge-pull-requests-in-the-github-copilot-app/) ⭐️ 7.8/10

GitHub 工程博客发文，介绍 Copilot app 中 diff 表面的重建。官方称新方案可打开百万行 pull request，并同时处理数百条行内评审评论。目前仅公开标题与摘要，具体实现与性能数据尚未披露。该文属于第一方工程实践分享。

rss · GitHub Blog · Sep 23, 18:29

**「为什么重要」** 对构建 coding agent 与 harness 的工程师来说，超大 diff 的渲染能力直接影响大型 PR 的评审与自动化处理体验。GitHub 作为平台方，其前端承载边界为同类工具提供了参考。

**「可关注」** 可关注：GitHub 将 diff 表面重建以支撑百万行 PR 与数百条行内评论，这是前端层面处理超大代码变更的工程实践。

**Tags**: `#product`, `#engineering`, `#industry`

---

<a id="item-ai-daily-4"></a>
### [Sam Altman’s remarks at the United Nations Security Council](https://openai.com/index/sam-altman-un-security-council-remarks) ⭐️ 6.8/10

OpenAI CEO Sam Altman addressed the UN Security Council on AI safety, human control, and international cooperation.

rss · OpenAI Blog · Sep 23, 12:00

**Tags**: `#lab`, `#policy`, `#industry`

---

<a id="item-ai-daily-5"></a>
### [Ringg 部署 GPT-5.6 客服代理](https://openai.com/index/ringg) ⭐️ 6.8/10

OpenAI 官方博客称，Ringg 使用 GPT-5.6 驱动多语言客服代理，覆盖语音、聊天、WhatsApp 和网页渠道。该代理最高可解决 65% 的客户通话，成本较 GPT-4.1 降低 90%。数据来自 OpenAI 第一方案例，尚未提供第三方验证。

rss · OpenAI Blog · Sep 23, 12:00

**「为什么重要」** 案例给出 GPT-5.6 在客服场景的具体部署数据，可作为多语言语音与文本混合场景的成本与解决率参考。

**「可关注」** OpenAI 称 GPT-5.6 在 Ringg 客服场景实现最高 65% 通话自动解决，成本较 GPT-4.1 降低 90%，可作为多语言语音+文本混合链路的参考基线。

**Tags**: `#model`, `#product`, `#industry`, `#eval`

---

<a id="item-ai-daily-6"></a>
### [GitHub 调研：开发者要求减少算力浪费](https://github.blog/news-insights/research/developers-want-more-efficient-software-heres-what-over-1000-github-users-told-us-they-need/) ⭐️ 6.8/10

GitHub 与耶鲁大学气候变化传播项目发布联合调研，覆盖超过 1000 名开发者。调研发现，开发者强烈需要工具、度量与实践指导，以减少算力浪费。该报告为研究性质，未发布具体产品或模型。

rss · GitHub Blog · Sep 23, 13:00

**「为什么重要」** 对 coding agent 与 harness 开发者而言，算力浪费直接影响成本与能效。这份调研为效率工具的需求提供了数据支撑。

**「可关注」** 可关注：开发者对算力度量与浪费治理的需求明确，但具体工具形态仍待观察。

**Tags**: `#industry`, `#research`, `#product`

---

<a id="item-ai-daily-7"></a>
### [Bringing Private Processing to Meta AI Glasses](https://engineering.fb.com/2026/09/23/security/private-processing-meta-ai-glasses/) ⭐️ 6.8/10

Meta Engineering announces private processing for AI glasses, but the provided excerpt is too truncated to evaluate concrete technical details or impact.

rss · Engineering at Meta · Sep 24, 00:00

**Tags**: `#product`, `#industry`, `#lab`

---

<a id="item-ai-daily-8"></a>
### [OpenAI Academy 成立两周年](https://openai.com/index/two-years-of-openai-academy) ⭐️ 6.3/10

OpenAI 官方博客发文纪念 OpenAI Academy 成立两周年，称将把 AI 技能带给更多社区。原文仅确认这一里程碑和扩张方向，未披露具体学员规模、课程数量或新增社区名单。

rss · OpenAI Blog · Sep 23, 16:00

**「为什么重要」** 这反映 OpenAI 在开发者教育与社区覆盖上的持续投入。不过材料未涉及模型、API 或 coding agent 相关的技术更新，对工程实践暂无直接影响。

**「可关注」** 可关注：OpenAI Academy 向更多社区扩展 AI 技能的具体路径与资源形式。

**Tags**: `#lab`, `#industry`, `#product`

---

## AI Creator Radar

<a id="item-ai-creator-1"></a>
### [Simon Willison Reports New Gemini 3.8 TTS Models](https://twitter.com/simonw/status/tweet-2102861892549279922) ⭐️ 0.0/10

On September 23, 2026, Simon Willison posted on Twitter that the new Gemini 3.8 TTS models are &quot;super-cheap&quot; and can generate conversations between multiple voices, offering 2,000+ preset voices or the option to clone your own. He stated that he built a small UI for the models and used Claude to write a script in which two pelicans debate moving to Pacifica Pier. The provided material notes that this is currently a single social media report lacking official documentation, pricing details, and version confirmation.

twitter · Simon Willison · Sep 23, 20:45

**「Why Now」** This is an early social media report from a prominent developer about potentially low-cost multi-voice TTS capabilities. However, the claimed features and cost advantages remain unverified by official sources in the supplied material.

**「Content Angle」** Content angle: Use Simon Willison&\#x27;s demo as a lead to outline the reported Gemini 3.8 TTS features—multi-voice dialogue, 2,000+ preset voices, and voice cloning—while clearly stating that the information comes from a single tweet without official documentation or pricing details.

**Tags**: `#Gemini TTS`, `#Text-to-Speech`, `#Voice Cloning`, `#Multi-voice Dialogue`, `#AI Content Creation`

---