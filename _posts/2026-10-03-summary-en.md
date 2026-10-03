---
layout: default
title: "Horizon Summary: 2026-10-03 (EN)"
date: 2026-10-03
lang: en
---

> From 209 items, 16 important content pieces were selected

---

**Agent Harness Architecture**
1. [Cline SDK v0.0.90 Released](#item-harness-arch-1) ⭐️ 8.8/10
2. [MCP TypeScript SDK v2.3.0 Released](#item-harness-arch-2) ⭐️ 8.8/10
3. [MCP TypeScript SDK Hono 2.0.2 Enforces One Connection Per Server](#item-harness-arch-3) ⭐️ 8.8/10
4. [modelcontextprotocol/python-sdk released v2.3.0](#item-harness-arch-4) ⭐️ 8.3/10
5. [cloudflare/agents released agents@0.25.0](#item-harness-arch-5) ⭐️ 8.3/10
6. [modelcontextprotocol/typescript-sdk released 1.32.0](#item-harness-arch-6) ⭐️ 8.3/10
7. [modelcontextprotocol/typescript-sdk released @modelcontextprotocol/fastify@2.0.1](#item-harness-arch-7) ⭐️ 8.3/10

**AI Agent Engineer**
1. [PoS：用显式信念状态治理长程 Agent](#item-agent-engineer-1) ⭐️ 8.0/10
2. [Hugging Face 论文：后训练的锐化税](#item-agent-engineer-2) ⭐️ 8.0/10
3. [HF daily paper: ActiveSaddler: Automated Curriculum Learning for Agent Harness Optimization](#item-agent-engineer-3) ⭐️ 7.5/10
4. [RASO 框架：跨 harness 技能优化](#item-agent-engineer-4) ⭐️ 7.5/10
5. [AutoSynthData: Generating Training Data for Enterprise Agents](#item-agent-engineer-5) ⭐️ 7.3/10
6. [Open-sourcing AstaBrief, the fast report-generation model in Asta](#item-agent-engineer-6) ⭐️ 6.3/10
7. [microsoft/FrogNano-4B-2609 · Hugging Face](#item-agent-engineer-7) ⭐️ 6.0/10
8. [Pi 1.0 稳定版与 TypeScript](#item-agent-engineer-8) ⭐️ 5.5/10

**AI Daily**
1. [OpenAI 发布 GPT-6 模型选用指南](#item-ai-daily-1) ⭐️ 8.3/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [Cline SDK v0.0.90 Released](https://github.com/cline/cline/releases/tag/sdk/sdk/v0.0.90) ⭐️ 8.8/10

Cline SDK v0.0.90 stops agent-team state from bloating during long sessions. Stream chunks and 2-second heartbeats no longer persist or trigger full-team rewrites; only changed entities batch into one SQLite transaction every ~300 ms. Run records keep summaries instead of transcripts, and team\_events caps at 2000 rows or 30 days per team. SQLite team storage migrates to schema v2 with one-time compaction, failed writes retry, and standalone provider requests resolve surface headers with optional sessionId.

github · github-actions\[bot\] · Oct 2, 04:35

**「Design Points」** Live streaming data stays in memory for UIs, while durable SQLite schema v2 stores compacted run summaries and bounded event logs. Explicit vacuum reclaims freed space after migration.

**「What Changed」** Persistence moves from full-team-state rewrites on every chunk to batched changed-entity writes. The standalone provider header API makes sessionId optional and omits empty X-Task-ID. Default models refresh for DigitalOcean, GMI Cloud, NanoGPT, Nvidia, and Ofox.

**Tags**: `#runtime`, `#memory`, `#subagents`

---

<a id="item-harness-arch-2"></a>
### [MCP TypeScript SDK v2.3.0 Released](https://github.com/modelcontextprotocol/typescript-sdk/releases/tag/v2.3.0) ⭐️ 8.8/10

modelcontextprotocol/typescript-sdk v2.3.0 introduces breaking changes to server lifecycle and HTTP transport security. Stateless Streamable HTTP now handles one server per request, and Server.connect\(\) rejects an already-connected instance. HTTP client transports follow redirects only within the same origin, with an opt-out via redirectPolicy: &\#x27;follow&\#x27;. The release also adds opt-in guards for tool input size and bearer token audience, and requires eventsource-parser 3.0.8 or later.

github · felixweinberger · Oct 2, 17:55

**「Design Points」** Servers must be instantiated inside the request handler or createMcpHandler factory rather than shared across requests; server creation is cheap after \#2889. Transport and auth layers now enforce stricter boundaries: same-origin redirects by default and audience-restricted bearer tokens when expectedResource is set.

**「What Changed」** Breaking: one server per request for stateless Streamable HTTP, and same-origin-only redirects for HTTP client transports. New capabilities include maxToolInputElements, expectedResource, wildcard origin entries like &lt;scheme&gt;://\* for browser-extension clients, and tasks/get and tasks/cancel on 2026-07-28 connections. Large single SSE events now parse dramatically faster with eventsource-parser 3.0.8+.

**Tags**: `#mcp`, `#runtime`, `#tools`

---

<a id="item-harness-arch-3"></a>
### [MCP TypeScript SDK Hono 2.0.2 Enforces One Connection Per Server](https://github.com/modelcontextprotocol/typescript-sdk/releases/tag/%40modelcontextprotocol/hono%402.0.2) ⭐️ 8.8/10

@modelcontextprotocol/hono@2.0.2 ships a breaking change to MCP server and transport lifecycles. A Server or McpServer now serves one connection at a time, and a Streamable HTTP transport without sessions \(sessionIdGenerator: undefined\) serves one request. Code that reuses a single server object or stateless transport across HTTP requests fails on the second request. The migration path is to build the server and transport per request or per session.

github · github-actions\[bot\] · Oct 2, 17:43

**「设计要点」** The runtime now rejects reuse at the transport layer: connect\(\) throws SdkError ALREADY\_CONNECTED when a server is already connected, and WebStandardStreamableHTTPServerTransport.handleRequest\(\) rejects stateless transports with a reuse error. NodeStreamableHTTPServerTransport returns 500. Express 5, Fastify, and Hono surface these failures as 500 responses; a bare node:http listener without error handling crashes on unhandled rejection.

**「改了什么」** The SDK moved from implicit sharing to strict per-request or per-session instantiation for stateless HTTP transports. Package manifests now declare Apache-2.0, and the bundled @modelcontextprotocol/server dependency is bumped to 2.3.0.

**Tags**: `#runtime`, `#mcp`, `#tools`

---

<a id="item-harness-arch-4"></a>
### [modelcontextprotocol/python-sdk released v2.3.0](https://github.com/modelcontextprotocol/python-sdk/releases/tag/v2.3.0) ⭐️ 8.3/10

MCP Python SDK v2.3.0 introduces breaking changes to tool header annotation validation and dependency requirements, plus minor fixes and new options.

github · maxisbey · Oct 2, 22:02

**Tags**: `#tools`, `#mcp`, `#runtime`

---

<a id="item-harness-arch-5"></a>
### [cloudflare/agents released agents@0.25.0](https://github.com/cloudflare/agents/releases/tag/agents%400.25.0) ⭐️ 8.3/10

Cloudflare Agents 0.25.0 changes async RPC lifecycle initialization and fixes agent-tool child failure reporting.

github · github-actions\[bot\] · Oct 2, 12:30

**Tags**: `#runtime`, `#tools`, `#subagents`

---

<a id="item-harness-arch-6"></a>
### [modelcontextprotocol/typescript-sdk released 1.32.0](https://github.com/modelcontextprotocol/typescript-sdk/releases/tag/1.32.0) ⭐️ 8.3/10

MCP TypeScript SDK 1.32.0 restricts HTTP redirects to same-origin by default and adds options to limit tool input size and validate bearer token audience.

github · felixweinberger · Oct 2, 17:28

**Tags**: `#mcp`, `#tools`, `#permissions`, `#runtime`

---

<a id="item-harness-arch-7"></a>
### [modelcontextprotocol/typescript-sdk released @modelcontextprotocol/fastify@2.0.1](https://github.com/modelcontextprotocol/typescript-sdk/releases/tag/%40modelcontextprotocol/fastify%402.0.1) ⭐️ 8.3/10

MCP TypeScript SDK Fastify 2.0.1 patch documents a breaking change requiring per-request server and stateless transport instantiation, breaking apps that reuse a single server object across HTTP requests.

github · github-actions\[bot\] · Oct 2, 17:43

**Tags**: `#mcp`, `#runtime`, `#tools`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [PoS：用显式信念状态治理长程 Agent](https://huggingface.co/papers/2610.01415) ⭐️ 8.0/10

Hugging Face Daily Papers 收录论文《Beyond Memory: Harnessing Long-Horizon Agents with Explicit Belief States》，提出推理时框架 PoS，为长程 LLM agent 构建并持续维护显式信念状态作为决策上下文。每个信念融合当前世界状态估计与未解决的任务需求，显式暴露 agent 仍需学习和完成的内容；PoS 同时校验信念一致性，监控任务进度以检测 Belief Trapping，即 agent 持续行动却未朝目标取得实质进展，并依据陷落模式与未解决需求类型定制恢复策略。论文认为，仅把交互历史组织成记忆，无法保证 agent 对当前世界形成连贯理解。该论文目前获得 69 次 upvotes。

rss · Hugging Face Daily Papers · Oct 3, 03:03

**「为什么重要」** 长程 agent 的失效往往不是记忆容量不足，而是世界模型未能随交互持续更新。PoS 将信念状态作为可校验、可监控的决策上下文，让 harness 在检测到 Belief Trapping 时有明确恢复依据，而非仅依赖历史检索。这对做长程任务编排与记忆架构的工程师，提供了一条不依赖模型微调的推理时干预路径。

**「可关注」** PoS 把「未解决的任务需求」纳入信念状态并做一致性校验，这提示 harness 设计可将显式世界状态与任务进度监控从 prompt 工程中抽离，作为独立运行时组件。

**Tags**: `#memory`, `#harness`, `#orchestration`

---

<a id="item-agent-engineer-2"></a>
### [Hugging Face 论文：后训练的锐化税](https://huggingface.co/papers/2610.01509) ⭐️ 8.0/10

Hugging Face 论文《Sharpening Tax in Post-Training》发现，预训练 LLM 加上轻量推理 harness，就能承担 agent 任务。虽然 pass@1 远低于后训练模型，但在测试时预算充足时，其 pass@K 解覆盖率常常更高。论文将机制归结为 RL 后训练对已有行为的锐化：它提升单次准确率，却牺牲解覆盖率，且这一权衡同样适用于 agentic 场景。

rss · Hugging Face Daily Papers · Oct 3, 03:03

**「为什么重要」** 如果后训练只是锐化分布，那么 agent 系统的瓶颈可能不在模型权重，而在 harness 与测试时预算的分配。这为重新评估 RL 后训练的必要性提供了实证依据。

**「可关注」** 可关注：在 agent 评测与 harness 设计中，pass@1 与 pass@K 需分开度量；若测试时预算充足，预训练模型配合轻量 harness 可能是比后训练模型更优的基线。

**Tags**: `#harness`, `#eval`, `#coding-agent`

---

<a id="item-agent-engineer-3"></a>
### [HF daily paper: ActiveSaddler: Automated Curriculum Learning for Agent Harness Optimization](https://huggingface.co/papers/2610.00906) ⭐️ 7.5/10

A new paper proposes ActiveSaddler, formulating agent harness optimization as an automated curriculum learning problem that adapts training scenarios alongside harness updates using a non-stationary bandit.

rss · Hugging Face Daily Papers · Oct 3, 03:03

**Tags**: `#harness`, `#eval`, `#coding-agent`, `#orchestration`

---

<a id="item-agent-engineer-4"></a>
### [RASO 框架：跨 harness 技能优化](https://huggingface.co/papers/2609.38024) ⭐️ 7.5/10

Hugging Face Daily Papers 收录论文《Retrieval-Augmented Skill Optimization via Cross-Harness Adaptation》，提出 RASO 框架。RASO 从外部技能语料库检索已有 agent skill，跨 harness 适配后用于优化新技能，降低对昂贵 rollout 的依赖。论文指出现有技能优化方法忽视数百万公开共享的技能，仅靠迭代 rollout 精炼目标技能。RASO 将外部语料作为先验知识贯穿优化全程。该论文获 41 次 upvote。

rss · Hugging Face Daily Papers · Oct 3, 03:03

**「为什么重要」** 对 coding agent / harness 从业者，技能优化长期受限于 rollout 成本。RASO 提供复用公开技能积累的路径，可能改变技能冷启动与迭代方式。目前仅为论文提案，尚未验证产品级效果。

**「可关注」** 可关注：RASO 将外部技能语料作为先验，检索后跨 harness 适配，或可减少从零优化技能所需的 rollout 次数。

**Tags**: `#harness`, `#eval`, `#coding-agent`, `#memory`

---

<a id="item-agent-engineer-5"></a>
### [AutoSynthData: Generating Training Data for Enterprise Agents](https://huggingface.co/blog/ServiceNow-AI/autosynthdata) ⭐️ 7.3/10

ServiceNow CoreAI presents AutoSynthData, a system that generates enterprise-specific agent training data by mining target model failures to create environment-aware, verifiable tasks.

rss · Hugging Face Blog · Oct 2, 04:01

**Tags**: `#eval`, `#harness`, `#coding-agent`

---

<a id="item-agent-engineer-6"></a>
### [Open-sourcing AstaBrief, the fast report-generation model in Asta](https://huggingface.co/blog/allenai/astabrief) ⭐️ 6.3/10

AllenAI open-sources AstaBrief, a fast report-generation model used in its agentic scientific platform Asta.

rss · Hugging Face Blog · Oct 2, 15:19

**Tags**: `#orchestration`, `#harness`, `#agent`

---

<a id="item-agent-engineer-7"></a>
### [microsoft/FrogNano-4B-2609 · Hugging Face](https://www.reddit.com/r/LocalLLaMA/comments/1ww40o2/microsoftfrognano4b2609_hugging_face/) ⭐️ 6.0/10

Microsoft&\#x27;s FrogNano-4B is a compact agentic model post-trained via reinforcement learning on synthetic SWE tasks using a five-tool Leaf harness, targeting repository-level coding on modest hardware.

reddit · r/LocalLLaMA · /u/jacek2023 · Oct 2, 20:16

**Tags**: `#coding-agent`, `#harness`, `#eval`

---

<a id="item-agent-engineer-8"></a>
### [Pi 1.0 稳定版与 TypeScript](https://www.latent.space/p/ainews-pi-10-pi-durable-and-aie-nyc) ⭐️ 5.5/10

Latent Space AINews 提到，极简 harness Pi 进入 1.0 稳定版，并支持 TypeScript。该摘要未给出主仓库、变更日志或破坏性变更说明，同期还提及 Pi Durable 与 AIE NYC，但无细节。工程影响暂无法从现有片段确认。

rss · Latent Space · Oct 2, 06:40

**「为什么重要」** 对使用 TypeScript 的 agent 团队，稳定版 harness 可能提供一个轻量接入选项。但该价值尚未经一手资料确认。

**「可关注」** Pi 1.0 稳定版与 TypeScript 支持的具体变更范围，等待主仓库或发布说明披露后再评估是否采用。

**Tags**: `#harness`, `#coding-agent`

---

## AI Daily

<a id="item-ai-daily-1"></a>
### [OpenAI 发布 GPT-6 模型选用指南](https://openai.com/index/practical-guide-building-gpt-6) ⭐️ 8.3/10

OpenAI 发布 GPT-6 家族模型实践指南，面向初创公司说明如何选择模型、调节推理强度、优化提示词与技能、协同工具，以及准备生产工作流。内容聚焦部署与调用层面的操作指引，并非模型发布公告。材料未提供具体基准或性能数字。

rss · OpenAI Blog · Oct 2, 16:15

**「为什么重要」** 对构建 coding agent 或 harness 的团队，这份指南给出了官方对 GPT-6 家族差异与推理强度调节的说明，可直接用于模型选型与生产配置。

**「可关注」** 可关注：OpenAI 官方给出了 GPT-6 家族推理强度调节、提示词优化、工具协同的建议，可直接作为生产环境参数配置的参考依据。

**Tags**: `#model`, `#lab`, `#product`

---