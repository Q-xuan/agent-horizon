---
layout: default
title: "Horizon Summary: 2026-10-03 (EN)"
date: 2026-10-03
lang: en
---

> From 183 items, 15 important content pieces were selected

---

**Agent Harness Architecture**
1. [Cline SDK v0.0.90 重构存储](#item-harness-arch-1) ⭐️ 8.8/10
2. [MCP TypeScript SDK 2.0.2 Enforces Per-Request Server Lifecycle](#item-harness-arch-2) ⭐️ 8.8/10
3. [MCP TypeScript SDK fastify 2.0.1 Enforces Per-Request Servers](#item-harness-arch-3) ⭐️ 8.8/10
4. [MCP TypeScript SDK Client 2.3.0 Released](#item-harness-arch-4) ⭐️ 8.8/10
5. [modelcontextprotocol/typescript-sdk released v2.3.0](#item-harness-arch-5) ⭐️ 8.3/10
6. [microsoft/agent-framework released python-1.20.0](#item-harness-arch-6) ⭐️ 8.3/10
7. [MCP Python SDK v2.3.0 Released](#item-harness-arch-7) ⭐️ 7.8/10

**AI Agent Engineer**
1. [AutoSynthData 失败转训练数据](#item-agent-engineer-1) ⭐️ 8.3/10
2. [后训练锐化税：基座模型 agent 反超](#item-agent-engineer-2) ⭐️ 8.0/10
3. [Llama3/Qwen2.5 蒸馏动力学](#item-agent-engineer-3) ⭐️ 7.0/10
4. [RASO 框架：检索增强技能优化](#item-agent-engineer-4) ⭐️ 7.0/10
5. [PoS 用显式信念状态改进长程 Agent](#item-agent-engineer-5) ⭐️ 6.5/10
6. [Open-sourcing AstaBrief, the fast report-generation model in Asta](#item-agent-engineer-6) ⭐️ 5.8/10
7. [FrogNano-4B-2609 后训练细节](#item-agent-engineer-7) ⭐️ 5.5/10

**AI Daily**
1. [OpenAI 发布 GPT-6 实用指南](#item-ai-daily-1) ⭐️ 8.3/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [Cline SDK v0.0.90 重构存储](https://github.com/cline/cline/releases/tag/sdk/sdk/v0.0.90) ⭐️ 8.8/10

Cline SDK v0.0.90 重构 agent team 状态持久化，消除流式分片和心跳写库造成的数据库膨胀。此前每次流式分片和 2 秒心跳都会重写整个团队状态，含已完成队友的完整 transcript，本地 teams.db 曾达 1.66 GB，单条运行记录被重写约 339k 次。现在分片和心跳只推送给实时 UI，不再落库；仅变更实体以约 300 ms 批量事务写入，运行记录只保留 summary，team\_events 按团队限制 2000 行 / 30 天。SQLite 团队存储升级到 schema v2，一次性迁移压缩存量数据，显式调用 SqliteTeamStore.vacuum\(\) 可回收空间；团队写入失败改为重试而非丢弃。

github · github-actions\[bot\] · Oct 2, 04:35

**「设计要点」** 持久化层改为 schema v2，只写变更实体并批量提交，team\_events 设 2000 行 / 30 天上限；resolveProviderRequestHeaders 将 sessionId 设为可选，支持会话外请求解析 Cline surface headers。

**「改了什么」** 相对 v0.0.89，流式分片与心跳不再落库，运行记录只存 summary，team\_events 限制 2000 行 / 30 天，SQLite 升级 schema v2 并支持 vacuum。resolveProviderRequestHeaders 的 sessionId 变为可选，X-Task-ID 为空时省略；模型目录刷新，DigitalOcean、GMI Cloud、NanoGPT、Nvidia、Ofox 默认模型变更。

**Tags**: `#runtime`, `#memory`, `#subagents`

---

<a id="item-harness-arch-2"></a>
### [MCP TypeScript SDK 2.0.2 Enforces Per-Request Server Lifecycle](https://github.com/modelcontextprotocol/typescript-sdk/releases/tag/%40modelcontextprotocol/hono%402.0.2) ⭐️ 8.8/10

The MCP TypeScript SDK released @modelcontextprotocol/hono@2.0.2, tightening the server connection lifecycle. A \`Server\` or \`McpServer\` now serves one connection at a time, and a stateless Streamable HTTP transport \(\`sessionIdGenerator: undefined\`\) serves one request. Reusing a single server object or stateless transport across HTTP requests fails on the second request. Build the server and transport per request.

github · github-actions\[bot\] · Oct 2, 17:43

**「Design Points」** Stateless Streamable HTTP deployments must instantiate the server and transport inside each request handler. Session-based transports still allow one server and one transport per session, but sharing one server across sessions now fails at \`initialize\` with \`ALREADY\_CONNECTED\`.

**「What Changed」** Shared-server and shared-stateless-transport patterns now hard-fail: \`connect\(\)\` rejects with \`ALREADY\_CONNECTED\`, \`WebStandardStreamableHTTPServerTransport.handleRequest\(\)\` rejects with a reuse error, and \`NodeStreamableHTTPServerTransport.handleRequest\(\)\` returns \`500\`. Package license metadata moved to \`Apache-2.0\` with no code change, and \`@modelcontextprotocol/server\` bumped to \`2.3.0\`.

**Tags**: `#runtime`, `#mcp`, `#tools`

---

<a id="item-harness-arch-3"></a>
### [MCP TypeScript SDK fastify 2.0.1 Enforces Per-Request Servers](https://github.com/modelcontextprotocol/typescript-sdk/releases/tag/%40modelcontextprotocol/fastify%402.0.1) ⭐️ 8.8/10

The MCP TypeScript SDK shipped @modelcontextprotocol/fastify@2.0.1, a patch that enforces single-connection servers and single-request stateless transports. A Server or McpServer now serves only one connection at a time, and a Streamable HTTP transport without sessions \(sessionIdGenerator: undefined\) serves only one request. Applications that reuse one server object or one stateless transport across HTTP requests fail on the second request; the migration path is to build the server and transport per request. The release also updates the package license field to Apache-2.0 with no code change.

github · github-actions\[bot\] · Oct 2, 17:43

**「Design Notes」** The SDK now rejects shared server instances and stateless transport reuse at runtime. Session-based transports with a sessionIdGenerator, per-request handlers, stdio servers, and clients remain unaffected. Failure modes vary by host: Express 5, Fastify, and Hono return 500, while a plain node:http listener without error handling crashes on unhandled rejection.

**「What Changed」** The SDK now enforces one-connection-per-server and one-request-per-stateless-transport at runtime, breaking shared-instance patterns that previously worked. Documentation examples across the express, fastify, hono, and node packages now build a server and transport per request, the license field changed to Apache-2.0 with no code change, and @modelcontextprotocol/server moved to 2.3.0.

**Tags**: `#runtime`, `#mcp`, `#tools`

---

<a id="item-harness-arch-4"></a>
### [MCP TypeScript SDK Client 2.3.0 Released](https://github.com/modelcontextprotocol/typescript-sdk/releases/tag/%40modelcontextprotocol/client%402.3.0) ⭐️ 8.8/10

The MCP TypeScript SDK shipped @modelcontextprotocol/client@2.3.0. HTTP client transports and OAuth helpers now follow redirects only within the request origin and only when the method is preserved. Cross-origin attempts fail the request with a named target, keep the session alive, and let OAuth discovery fall back to the next well-known URL. The release also speeds up large SSE messages, adds Tasks extension methods, and clarifies version negotiation failures.

github · github-actions\[bot\] · Oct 2, 17:43

**「Design Notes」** Transport security is enforced at the fetch boundary: same-origin checks cover scheme, host, and port, with http-to-https upgrades allowed on default ports. Node permits up to five consecutive same-origin method-preserving redirects, while browsers fail redirected requests because the target is not exposed; \`redirectPolicy: &\#x27;follow&\#x27;\` delegates handling back to fetch.

**「What Changed」** Redirects are now restricted to same-origin targets that preserve the method, with explicit errors for cross-origin attempts and OAuth discovery falling back to the next well-known URL. Large single SSE events over Streamable HTTP parse from about 13 seconds to under one second, and \`SSEClientTransport\` retries once after \`onUnauthorized\(\)\` before rejecting with \`SdkHttpError\`.

**Tags**: `#mcp`, `#runtime`, `#tools`

---

<a id="item-harness-arch-5"></a>
### [modelcontextprotocol/typescript-sdk released v2.3.0](https://github.com/modelcontextprotocol/typescript-sdk/releases/tag/v2.3.0) ⭐️ 8.3/10

MCP TypeScript SDK v2.3.0 introduces a breaking one-server-per-request constraint and a same-origin redirect policy for HTTP client transports.

github · felixweinberger · Oct 2, 17:55

**Tags**: `#mcp`, `#runtime`, `#tools`

---

<a id="item-harness-arch-6"></a>
### [microsoft/agent-framework released python-1.20.0](https://github.com/microsoft/agent-framework/releases/tag/python-1.20.0) ⭐️ 8.3/10

microsoft/agent-framework python-1.20.0 adds Foundry hosting, vector-store connectors, and runtime/sandbox improvements.

github · eavanvalkenburg · Oct 2, 14:40

**Tags**: `#runtime`, `#tools`, `#sandbox`, `#memory`, `#permissions`

---

<a id="item-harness-arch-7"></a>
### [MCP Python SDK v2.3.0 Released](https://github.com/modelcontextprotocol/python-sdk/releases/tag/v2.3.0) ⭐️ 7.8/10

MCP Python SDK v2.3.0 lands with mostly fixes and three new options. The release raises the httpx2 requirement to &gt;=2.10.0 and tightens tool registration: invalid x-mcp-header annotations now raise InvalidSignature instead of letting the server start while clients silently drop the tool. On 2025-11-25 and earlier connections, outbound requests omit empty \_meta and params, and initialize no longer sends an empty experimental capability.

github · maxisbey · Oct 2, 22:02

**「Design Points」** Header validation shifts to registration time. MCPServer stops running tools/list for every tools/call; Mcp-Param-\* checks now look up the registered schema by name, so middleware that filters or rewrites tools/list no longer influences validation. Low-level servers can pass Server\(get\_tool\_input\_schema=...\) to supply schemas without a tools/list handler.

**「What Changed」** httpx2&gt;=2.10.0 replaces the old &gt;=2.5.0 floor. Invalid x-mcp-header annotations now fail at registration with InvalidSignature; only plain str, int, and bool parameters pass, header names must be valid tokens, and case-only duplicates are refused. Empty \_meta and params are omitted on 2025-11-25 and earlier connections, so ctx.meta and ctx.params become None. initialize drops an empty experimental capability. Mcp-Param-\* validation looks up the registered schema by name instead of running tools/list. Interactive OAuth logins pause request timeouts. New options: max\_sse\_event\_size on streamable\_http\_client and StreamableHttpParameters \(default 1 MiB\), MCPServer\(subscriptions=False\), Server\(get\_tool\_input\_schema=...\), and Client.call\_tool retrying once after HeaderMismatch \(-32020\). Fixes include Context\[AppState\] on prompts and resource templates, explicit null structuredContent checked against the output schema, raising progress\_callback contained on in-process Client\(server\), OpenTelemetry spans recording JSON-RPC errors, and stdio\_client resolving the executable off the event loop on Windows.

**Tags**: `#tools`, `#mcp`, `#runtime`, `#permissions`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [AutoSynthData 失败转训练数据](https://huggingface.co/blog/ServiceNow-AI/autosynthdata) ⭐️ 8.3/10

ServiceNow CoreAI 提出 AutoSynthData，将企业 Agent 的失败转化为合成训练任务。方法在目标环境中评估模型，结合更强教师的成功轨迹定位能力缺口，再生成并验证新任务。任务定义为 system specification、user prompt、verifier 三元组，需满足可行、真实、有难度；验证器需一致、可靠、完整。流程分 Target 与 Multiply 两阶段，后者从已接受样本扩展变体，且禁止变体再衍生变体。

rss · Hugging Face Blog · Oct 2, 04:01

**「为什么重要」** 企业 Agent 的短板常藏在特定工作流、工具组合或约束中，通用能力无法直接覆盖。AutoSynthData 给出从失败到课程化训练数据的工程路径，并分离生成控制与环境执行。

**「可关注」** 可关注：AutoSynthData 将能力缺口蒸馏为脱敏的 capability specification cards，生成器只接收卡片，不接触原始 prompt、实体、轨迹和验证器细节，以此限制跨代漂移。

**Tags**: `#eval`, `#coding-agent`, `#harness`

---

<a id="item-agent-engineer-2"></a>
### [后训练锐化税：基座模型 agent 反超](https://huggingface.co/papers/2610.01509) ⭐️ 8.0/10

Hugging Face Daily Papers 于 2026-10-03 收录论文《Sharpening Tax in Post-Training》，获 63 赞。论文认为 RL 后训练只是在锐化基座模型已有行为，以 pass@K 覆盖率为代价提升 pass@1。作者发现，预训练模型加轻量推理 harness 即可作为 agent；测试时预算充足时，其 agentic 任务覆盖率常超过后训练模型，尽管 pass@1 远低。该 trade-off 此前见于数学和代码任务，本文将其扩展到多轮工具使用场景。

rss · Hugging Face Daily Papers · Oct 3, 01:39

**「为什么重要」** 它挑战「RL 后训练是获得可用 agent 的必要条件」这一假设。对 coding agent 与 harness 开发者，论文证据表明测试时预算和 harness 设计可能比后训练更影响 pass@K 覆盖率，但该影响尚未在生产环境验证。

**「可关注」** 可关注：在 pass@K 覆盖率优先的 agent 任务中，可对比测试基座模型加轻量 harness 与后训练模型的表现，尤其是测试时预算充足时。

**Tags**: `#harness`, `#eval`, `#coding-agent`

---

<a id="item-agent-engineer-3"></a>
### [Llama3/Qwen2.5 蒸馏动力学](https://huggingface.co/papers/2609.35259) ⭐️ 7.0/10

2026 年 10 月 3 日，Hugging Face Daily Papers 收录一篇系统研究蒸馏动力学的论文。研究在 Llama3 与 Qwen2.5 上独立变化 rollout 策略、token 级 KL 方向和学习率，覆盖科学、医疗、算术推理任务。论文发现 rollout 策略未必是核心因素，token 级 KL 方向更清晰地塑造蒸馏结果。该论文获得 122 次 upvote。

rss · Hugging Face Daily Papers · Oct 3, 01:39

**「为什么重要」** 此前对比监督微调与强化学习时，多个因素同时变化，难以分离 rollout 策略的贡献。该研究通过受控实验挑战了 on-policy 必然更优的假设，指出 token 级 KL 方向才是更关键的影响因素。

**「可关注」** 可关注：在强到弱蒸馏或微调中，调 token 级 KL 方向可能比对齐 rollout 策略更影响最终效果；实验设计需独立控制这些变量。

**Tags**: `#eval`, `#memory`, `#distillation`

---

<a id="item-agent-engineer-4"></a>
### [RASO 框架：检索增强技能优化](https://huggingface.co/papers/2609.38024) ⭐️ 7.0/10

Hugging Face Daily Papers 于 2026-10-03 收录论文《Retrieval-Augmented Skill Optimization via Cross-Harness Adaptation》，提出 RASO 框架。该框架把外部技能语料库当作先验知识，在技能优化全过程中检索相关已有技能，并跨 harness 适配到目标任务。论文指出现有方法主要依赖昂贵的 agent rollouts 迭代精炼技能，忽略了公开积累的百万级技能。材料未提供实验细节、量化对比或生产环境验证。

rss · Hugging Face Daily Papers · Oct 3, 01:39

**「为什么重要」** 对 coding agent 与 harness 工程师而言，论文提出了复用公开技能资产、降低 rollout 成本的路径；但跨 harness 适配的实际收益与限制仍待实验证实。

**「可关注」** 可关注：RASO 将外部技能语料库作为先验注入技能优化，若实验验证其跨 harness 适配有效，或改变当前依赖昂贵 rollout 的技能迭代方式。

**Tags**: `#harness`, `#eval`, `#memory`, `#orchestration`

---

<a id="item-agent-engineer-5"></a>
### [PoS 用显式信念状态改进长程 Agent](https://huggingface.co/papers/2610.01415) ⭐️ 6.5/10

HF Daily Papers 于 2026-10-03 推荐论文《Beyond Memory: Harnessing Long-Horizon Agents with Explicit Belief States》，提出推理时框架 PoS。该框架持续维护显式信念状态，将当前世界状态估计与未解决任务需求结合，作为 Agent 决策上下文。PoS 校验信念一致性并监控任务进度，检测 Belief Trapping——Agent 持续行动但未朝目标取得实质进展——再依据困住模式与未解决需求类型定制恢复策略。论文未提供可复现基准或代码，实际效果需结合全文评估。

rss · Hugging Face Daily Papers · Oct 3, 01:39

**「为什么重要」** 长程 Agent 仅将交互历史组织为记忆，未必保证对当前世界的连贯理解。PoS 把隐式历史转为显式信念并加入进度监控，为 memory/harness 设计提供了新思路；但摘要未给出实验数据，其相对现有记忆方案的增益仍待验证。

**「可关注」** 可关注：PoS 将信念状态作为决策上下文并检测 Belief Trapping，若后续给出可复现基准或代码，可评估其在长程任务中的恢复效果。

**Tags**: `#memory`, `#harness`, `#orchestration`, `#eval`

---

<a id="item-agent-engineer-6"></a>
### [Open-sourcing AstaBrief, the fast report-generation model in Asta](https://huggingface.co/blog/allenai/astabrief) ⭐️ 5.8/10

AllenAI open-sources AstaBrief, a fast report-generation model for its agentic scientific platform Asta, designed to produce cited reports grounded in evidence.

rss · Hugging Face Blog · Oct 2, 15:19

**Tags**: `#agent`, `#model-release`, `#scientific-ai`, `#report-generation`, `#open-source`

---

<a id="item-agent-engineer-7"></a>
### [FrogNano-4B-2609 后训练细节](https://www.reddit.com/r/LocalLLaMA/comments/1ww40o2/microsoftfrognano4b2609_hugging_face/) ⭐️ 5.5/10

2026 年 10 月 2 日，Reddit 用户 /u/jacek2023 分享了 Microsoft FrogNano-4B-2609 的技术细节。该模型派生自 Qwen/Qwen3.5-4B，在约 1,500 个合成 SWE 任务环境上用强化学习做后训练，配合五工具 Leaf harness 与可执行测试奖励，聚焦仓库级软件工程。原帖未提供官方发布链接或基准测试结果，仅指向第三方 GGUF 量化，模型性能与官方状态仍不确定。

reddit · r/LocalLLaMA · /u/jacek2023 · Oct 2, 20:16

**「为什么重要」** 对 coding agent 开发者而言，这展示了在 4B 尺寸上用合成环境和 RL 专攻仓库级编码的路径，且明确不使用行为蒸馏。但缺乏基准和官方渠道，暂时只能作为技术参考。

**「可关注」** 可关注：FrogNano 在 4B 尺寸上用约 1,500 个合成 SWE 环境和 Leaf harness 做 RL，且不使用行为蒸馏，但原帖缺少基准与官方发布信息，效果待验证。

**Tags**: `#coding-agent`, `#harness`, `#eval`

---

## AI Daily

<a id="item-ai-daily-1"></a>
### [OpenAI 发布 GPT-6 实用指南](https://openai.com/index/practical-guide-building-gpt-6) ⭐️ 8.3/10

OpenAI 发布 GPT-6 系列官方实用指南。文档面向初创团队，覆盖模型选择、reasoning effort 调节、提示词与技能优化、工具协同及生产工作流准备。这是权威使用指导，非新模型或政策发布。

rss · OpenAI Blog · Oct 2, 16:15

**「为什么重要」** GPT-6 家族首份官方工程指南，为模型选型与推理成本控制提供一手依据。

**「可关注」** 可关注：指南将 reasoning effort 作为可调参数，与工具协同、生产工作流并列，工程侧需重新评估延迟与成本的平衡。

**Tags**: `#model`, `#lab`, `#product`

---