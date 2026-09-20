---
layout: default
title: "Horizon Summary: 2026-09-20 (EN)"
date: 2026-09-20
lang: en
---

> From 159 items, 8 important content pieces were selected

---

**Agent Harness Architecture**
1. [PydanticAI v2.46.0 发布](#item-harness-arch-1) ⭐️ 7.8/10
2. [Claude Code 2.1.278 发布](#item-harness-arch-2) ⭐️ 7.3/10
3. [Agent Lightning v1.0](#item-harness-arch-3) ⭐️ 5.5/10
4. [Claude Code 终端代理](#item-harness-arch-4) ⭐️ 5.2/10

**AI Agent Engineer**
1. [halogen 0.12.0 长上下文实测](#item-agent-engineer-1) ⭐️ 7.3/10
2. [Datasette Explain 0.2.2 发布](#item-agent-engineer-2) ⭐️ 6.3/10

**AI Deals**
1. [HTTPS Capture Free](#item-ai-deals-1) ⭐️ 6.0/10
2. [Kuvu AI UGC 视频免费一个月](#item-ai-deals-2) ⭐️ 6.0/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [PydanticAI v2.46.0 发布](https://github.com/pydantic/pydantic-ai/releases/tag/v2.46.0) ⭐️ 7.8/10

PydanticAI v2.46.0 improves typed tool and output handling. TypeSafeModel can fill tool arguments when Jev can express them, choose a union output type first, and reject more options than Jev can select. The release also adds realtime playback synchronization, model capability handling for evaluations, and agent event streaming through Temporal Workflow Streams.

github · DouweM · Sep 19, 03:51

**「设计要点」** ModelProfile.supports\_text\_output lets LLMJudge and GEval run with models that lack text output. RealtimeSession.wait\_for\_playback\(\) coordinates reply completion, while TemporalDurability.event\_stream\_topic publishes agent events through Workflow Streams.

**「改了什么」** Compared with v2.45.0, v2.46.0 adds typed tool-argument filling, union output selection, and a runtime Choices helper for described options. It also adds evaluation support for non-text-output models, realtime playback waiting and cost tracking, plus Temporal Workflow Streams for agent events.

**Tags**: `#runtime`, `#tools`, `#eval`, `#planning`

---

<a id="item-harness-arch-2"></a>
### [Claude Code 2.1.278 发布](https://code.claude.com/docs/en/changelog#2-1-278) ⭐️ 7.3/10

Claude Code 2.1.278 changes auto mode to use the server-side classifier by default for Claude API and Enterprise users, plus Bedrock, Vertex, Foundry, and gateway deployments. The server-side classifier does not charge classifier overhead. Bedrock, Vertex, Foundry, and gateways can opt out with \`CLAUDE\_CODE\_AUTO\_MODE\_SERVER=0\`; Claude Code now warns when it falls back to a billed classifier.

rss · Claude Code Changelog · Sep 19, 03:19

**「设计要点」** Auto mode classification now moves to a server-side path by default across the listed runtimes and providers, with an environment-variable escape hatch for Bedrock, Vertex, Foundry, and gateways. \`/status\` exposes an \`Auto mode server\` row so a session can report which classifier path it is using.

**「改了什么」** Compared with the previous behavior, auto mode defaults to the server-side classifier and reports billed fallback instead of leaving the billing path implicit. The new \`/status\` row makes the active classifier location observable per session.

**Tags**: `#runtime`, `#tools`, `#observability`

---

<a id="item-harness-arch-3"></a>
### [Agent Lightning v1.0](https://github.com/microsoft/agent-lightning) ⭐️ 5.5/10

GitHub Trending highlighted Microsoft’s agent-lightning, a lightweight agentic RL framework for training agents with real agent harnesses. Its README describes roughly 3,500 lines of code and names simplicity as a design principle. The project states that it was completely refactored in v1.0, with releases before v1.0 kept on a separate legacy branch. The supplied RSS excerpt is incomplete, so it does not establish deeper architectural novelty or operational limits.

rss · GitHub Trending Daily · Sep 20, 02:06

**「设计要点」** The available material only establishes the training target: agentic RL with real agent harnesses. It does not expose runtime boundaries, tool interfaces, memory behavior, permission handling, or evaluation design.

**Tags**: `#runtime`, `#planning`, `#tools`

---

<a id="item-harness-arch-4"></a>
### [Claude Code 终端代理](https://github.com/anthropics/claude-code) ⭐️ 5.2/10

Claude Code is a terminal-based agentic coding tool that understands a codebase and accepts natural-language commands. It executes routine coding tasks, explains complex code, and handles Git workflows. The source provides no release version, implementation details, or operational constraints.

rss · GitHub Trending Daily · Sep 20, 02:06

**「设计要点」** The available description only establishes a terminal runtime, codebase understanding, natural-language interaction, and Git workflow execution. It does not provide enough evidence to assess the agent loop, tool interfaces, memory, permissions, or evaluation design.

**Tags**: `#runtime`, `#tools`, `#planning`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [halogen 0.12.0 长上下文实测](https://www.reddit.com/r/LocalLLaMA/comments/1wkyny9/qwen38flashnext_at_1m_context_on_strix_halo_38/) ⭐️ 7.3/10

On September 19, 2026, a Reddit post reported Qwen3.8-Flash-Next results with halogen 0.12.0 on a Ryzen AI Max+ 395 system with 128 GB RAM. Compared with halogen 0.11.10, decode at 1,004,581 tokens rose from 27.3 to 38.3 tok/s, while cold prefill fell from 21.2 to 17.9 minutes; at 258,794 tokens, decode rose from 42.9 to 45.0 tok/s. The 1M figures came from one cold request each, used \`HALOGEN\_ROPE\_YARN=4\` and \`HALOGEN\_CTX=1048576\`, and still require repository-based reproduction.

reddit · r/LocalLLaMA · /u/peonist-ai · Sep 19, 21:49

**「为什么重要」** Local coding-agent workloads that approach 1M-token contexts may care because the reported cold path improved on the stated hardware, while a cached follow-up reached its first token in about 0.55 seconds. The evidence does not establish a general gain: the 1M measurements each used one cold request, and the standard 32k ten-prompt served mean did not change.

**「可关注」** 可关注：Separate cold-prefill and cached-turn measurements when evaluating halogen 0.12.0, because the reported 1M gains apply to a one-shot cold path while cached first-token latency was reported separately.

**Tags**: `#harness`, `#long-context`, `#observability`, `#coding-agent`

---

<a id="item-agent-engineer-2"></a>
### [Datasette Explain 0.2.2 发布](https://github.com/simonw/datasette-explain/releases/tag/0.2.2) ⭐️ 6.3/10

On September 20, 2026, simonw released Datasette Explain 0.2.2. Explain plans now work on read-only stored-query pages, extending SQL debugging and observability to that page type. The supplied material reports no broader impact on agent architecture, harnesses, or evaluations.

github · simonw · Sep 20, 00:22

**「为什么重要」** This removes a narrow usability gap for inspecting SQL plans on read-only stored queries. The release note does not establish broader performance, architecture, or workflow effects.

**「可关注」** 可关注：Whether read-only query surfaces expose the same observability signals as editable query pages.

**Tags**: `#observability`, `#debugging`, `#tooling`, `#datasette`

---

## AI Deals

<a id="item-ai-deals-1"></a>
### [HTTPS Capture Free](https://www.appinn.com/https-capture-for-apple/) ⭐️ 6.0/10

HTTPS Capture is reported as a lifetime-free App Store offer outside mainland China. It supports iPhone, iPad, and Mac for HTTPS capture, decryption, LAN traffic inspection, and API debugging. It is not listed in the mainland China App Store, so availability and the offer status should be checked on the relevant App Store page.

rss · 小众软件 · Sep 19, 06:06

**「Why it matters」** The tool combines HTTPS decryption, API debugging, URL rewriting, JavaScript scripts, Mock, Hosts, breakpoint debugging, and WebSocket support for Apple-device network testing. The main limitation is its App Store region availability.

**「Watch」** Watch: This fits Apple-device developers who need HTTPS capture or API debugging, but users in mainland China cannot rely on the local App Store listing.

**Tags**: `#limited-free`, `#promo`, `#api`

---

<a id="item-ai-deals-2"></a>
### [Kuvu AI UGC 视频免费一个月](https://kuvu.ai/marketing/ai-ugc) ⭐️ 6.0/10

Kuvu presents an AI UGC video creator with one month of free use. The supplied material does not state the signup steps, usage quota, regional limits, card requirement, or an end date.

rss · HN Free API / Credits · Sep 19, 13:55

**「为什么重要」** This is an explicitly time-limited free offer, so it may be worth checking while the promotion is active. Its actual redemption terms remain unconfirmed.

**「可关注」** 可关注：This suits readers evaluating AI UGC video generation; confirm the quota and account requirements before relying on it.

**Tags**: `#promo`, `#limited-free`, `#free-tier`

---