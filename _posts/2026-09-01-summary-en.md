---
layout: default
title: "Horizon Summary: 2026-09-01 (EN)"
date: 2026-09-01
lang: en
---

> From 174 items, 15 important content pieces were selected

---

**Agent Harness Architecture**
1. [FastMCP v4.0.0 released](#item-harness-arch-1) ⭐️ 7.8/10
2. [Cline desktop-v0.0.21-beta.2 发布](#item-harness-arch-2) ⭐️ 6.8/10
3. [Claude Code v2.1.252 发布](#item-harness-arch-3) ⭐️ 5.8/10
4. [Cline desktop-v0.0.21 发布](#item-harness-arch-4) ⭐️ 5.8/10
5. [pydantic-ai v2.37.0 发布](#item-harness-arch-5) ⭐️ 5.8/10
6. [microsoft/agent-framework dotnet-1.20.0 发布](#item-harness-arch-6) ⭐️ 5.8/10
7. [OmniParser GitHub trending](#item-harness-arch-7) ⭐️ 5.0/10
8. [Claude Cookbooks GitHub trending](#item-harness-arch-8) ⭐️ 5.0/10

**AI Agent Engineer**
1. [StarHarness: 分层搜索演化 harness](#item-agent-engineer-1) ⭐️ 8.0/10
2. [Wrapture Python library for function wrapping and tracing](#item-agent-engineer-2) ⭐️ 7.0/10
3. [DART-SD 多轮工具调用自蒸馏框架](#item-agent-engineer-3) ⭐️ 6.0/10
4. [ElephantBench: Probing LLMs&\#x27; Epistemic Myopia on Long-Tail Knowledge](#item-agent-engineer-4) ⭐️ 6.0/10

**AI Daily**
1. [ChatGPT Ads Hits $1B ARR and Expands Globally](#item-ai-daily-1) ⭐️ 6.8/10
2. [Polimill Builds Japan&\#x27;s Next-Generation Public AI Infrastructure](#item-ai-daily-2) ⭐️ 5.8/10
3. [LWiAI Podcast \#255: Gemini 3.7 Flash, Jalapeño, Qwen 3.8, Drones](#item-ai-daily-3) ⭐️ 5.0/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [FastMCP v4.0.0 released](https://github.com/PrefectHQ/fastmcp/releases/tag/v4.0.0) ⭐️ 7.8/10

FastMCP 4.0.0 ships as the reference implementation for the July 2026 MCP revision. It enables load-balancer-friendly sessionless requests and interactive tools with context passing. One FastMCP 4 deployment negotiates the best protocol version per connection. New clients get the new protocol while old clients keep working.

github · zzstoatzz · Aug 31, 18:19

**「Design notes」** FastMCP 4 runs on the modern MCP protocol with sessionless requests and per-connection version negotiation. It uses extensions for background tasks and provides server-level cache hints and routing headers.

**「Changed」** Most FastMCP 3 applications upgrade without code changes. Breaking changes include removal of server-initiated sampling and roots, deprecated APIs, and migration to MCP SDK v2.0.0b2.

**Tags**: `#mcp`, `#runtime`, `#tools`, `#permissions`, `#memory`

---

<a id="item-harness-arch-2"></a>
### [Cline desktop-v0.0.21-beta.2 发布](https://github.com/cline/cline/releases/tag/desktop-v0.0.21-beta.2) ⭐️ 6.8/10

Cline desktop v0.0.21-beta.2 is released.
New beta features include cloud session handoff with state preservation.
Environment selection supports local, SSH, and Cloud.
GitHub onboarding is behind the code-onboarding-github feature flag.

github · github-actions\[bot\] · Aug 31, 21:08

**「改了什么」** This release adds beta features for handoff of local sessions to Cline Cloud with session state preservation and environment selection between local, SSH, and Cloud. It includes all stable improvements from version 0.0.20.

**Tags**: `#memory`, `#runtime`, `#tools`

---

<a id="item-harness-arch-3"></a>
### [Claude Code v2.1.252 发布](https://github.com/anthropics/claude-code/releases/tag/v2.1.252) ⭐️ 5.8/10

Claude Code v2.1.252 is released by Anthropics.
Four bug fixes address Bash command failures on Macs, always allow settings persistence, remote session stalling, and large failure output notifications.

github · ashwin-ant · Aug 31, 19:46

**「改了什么」** v2.1.252 fixes Bash commands failing with task output swap refused \(tasks dir moved or linked\) on some Macs.
Always allow settings now persist in projects without .claude/settings.local.json.
Remote Control sessions hosted by Claude Desktop or VS Code no longer stall for minutes after a tool finished when the connection to claude.ai was degraded.
Background task notifications with very large failure output \(for example git errors on a full disk\) no longer make the conversation exceed the API request size limit.

**Tags**: `#runtime`, `#tools`, `#permissions`

---

<a id="item-harness-arch-4"></a>
### [Cline desktop-v0.0.21 发布](https://github.com/cline/cline/releases/tag/desktop-v0.0.21) ⭐️ 5.8/10

Cline desktop v0.0.21 has been released. The marketplace is now a two-pane explorer with a browsable list on the left and full catalog metadata on the right. Session stopping now propagates to child agents and teammates with cancelled tasks persisting. Provider models refresh from the live catalog and the model catalog has been refreshed with new providers and updated defaults.

github · github-actions\[bot\] · Aug 31, 21:41

**「What changed」** Relative to v0.0.20, the two-pane marketplace explorer and robust session stopping that affects subagents and teammates are the main changes. Additional updates include ask-a-question tool fixes, file attachment support anywhere in the chat, provider model catalog refresh, improved 401/403 error classification, and Langfuse tracing fix in release builds.

**Tags**: `#subagents`, `#tools`, `#runtime`

---

<a id="item-harness-arch-5"></a>
### [pydantic-ai v2.37.0 发布](https://github.com/pydantic/pydantic-ai/releases/tag/v2.37.0) ⭐️ 5.8/10

Pydantic-ai v2.37.0 is released. It adds the glm-5.3-flash model and reworks the Z.AI test suite onto cassettes. It fixes issues in model routing, UI messaging for tool calls, span queries, and capability hooks.

github · dsfaccini · Sep 1, 01:48

**「改了什么」** Added glm-5.3-flash model and reworked Z.AI test suite onto cassettes. Fixed bugs in model routing, UI messaging for tool calls, span queries, and capability hooks.

**Tags**: `#runtime`, `#tools`, `#eval`

---

<a id="item-harness-arch-6"></a>
### [microsoft/agent-framework dotnet-1.20.0 发布](https://github.com/microsoft/agent-framework/releases/tag/dotnet-1.20.0) ⭐️ 5.8/10

Microsoft Agent Framework .NET 1.20.0 is released. The release adds Mem0Sharp integration for in-memory storage in agent samples and includes minor fixes such as preserving Responses logprobs, honoring cancellation for Foundry-hosted workflow responses, and using the Responses API for hosted web search in AG-UI. Dependency bumps, test stabilizations, and other updates were performed with no major runtime rewrites or breaking changes.

github · SergeyMenshykh · Aug 31, 18:53

**「改了什么」** Added Mem0Sharp integration for in-memory storage in agent samples. Enabled Responses API usage for hosted web search in AG-UI. Added cancellation support for Foundry-hosted workflow responses. Preserved the Responses logprobs field.

**Tags**: `#memory`, `#runtime`, `#tools`

---

<a id="item-harness-arch-7"></a>
### [OmniParser GitHub trending](https://github.com/microsoft/OmniParser) ⭐️ 5.0/10

microsoft/OmniParser is a screen parsing tool for pure vision based GUI agents.

It parses user interface screenshots into structured and easy-to-understand elements.

This enhances GPT-4V ability to generate grounded actions.

Currently trending on GitHub.

rss · GitHub Trending Daily · Sep 1, 01:54

**Tags**: `#tools`, `#subagents`, `#vision`

---

<a id="item-harness-arch-8"></a>
### [Claude Cookbooks GitHub trending](https://github.com/anthropics/claude-cookbooks) ⭐️ 5.0/10

Claude Cookbooks is a trending collection of Claude AI notebooks and recipes for developers to build with Claude. The repo offers code and guides with copy-able code snippets that can be integrated into projects. Prerequisites include a Claude API key. Code examples are primarily written in Python.

rss · GitHub Trending Daily · Sep 1, 01:54

**Tags**: `#tools`, `#planning`, `#notebooks`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [StarHarness: 分层搜索演化 harness](https://huggingface.co/papers/2608.24804) ⭐️ 8.0/10

StarHarness is a framework for evolving environment-specific agent harnesses while keeping model weights fixed. The evolved harness can include prompt and task framing, tool interfaces, skills, MCP-backed providers, subagent structure, and agent-loop configuration. StarHarness constructs a compact evolution pool by stratifying tasks according to baseline failure behavior, separates proposer-visible search tasks from proposer-hidden selection tasks, and reserves held-out tasks for evaluating generalization. Across ITBench SRE, EnterpriseOps-Gym ITSM, and AutomationBench Finance, harness evolution improves full-benchmark performance by 20-35 percentage points over the default harness after 4-12 accepted changes per environment. These gains persist on tasks excluded from evolution.

rss · Hugging Face Daily Papers · Sep 1, 01:54

**「为什么重要」** StarHarness enables rapid adaptation of agent harnesses to enterprise environments with minimal changes, delivering 20-35pp performance gains on held-out tasks. This directly impacts harness, evaluation, and toolchain design for coding agents.

**「可关注」** 可关注：harness evolution pool is constructed by stratifying tasks according to baseline failure behavior, separating proposer-visible search tasks from proposer-hidden selection tasks.

**Tags**: `#harness`, `#mcp`, `#eval`, `#orchestration`, `#coding-agent`

---

<a id="item-agent-engineer-2"></a>
### [Wrapture Python library for function wrapping and tracing](https://simonwillison.net/2026/Aug/31/introducing-wrapture/) ⭐️ 7.0/10

Wrapture is a new Python library by Graham Dumpleton for wrapping functions and methods to support tracing or overriding return values. It extends ideas from the wrapt library and acts as an alternative to unittest.mock for both testing and tracing existing projects without code changes. Wrapture includes OpenTelemetry support and a TOML-based configuration for adding tracing to projects. This young project, only a few weeks old, was entirely written by an AI assistant under the author&\#x27;s direction.

rss · Simon Willison · Aug 31, 23:59

**「Why it matters」** Wrapture provides non-intrusive tracing and controlled mocking relevant to agent harnesses, evals, testing, and observability toolchains.

**「Takeaway」** Wrapture enables tracing without modifying the watched program and supports transforms\_result for modifying return values in unit tests.

**Tags**: `#harness`, `#eval`, `#tracing`, `#observability`, `#mocking`

---

<a id="item-agent-engineer-3"></a>
### [DART-SD 多轮工具调用自蒸馏框架](https://huggingface.co/papers/2608.18524) ⭐️ 6.0/10

HF Daily Papers introduces DART-SD, a diamond-topology aware retrieval and tuning method for self-distillation to improve multi-turn tool-calling in LLMs by preserving policy diversity in order-independent sub-goal tasks. The framework addresses topological collapse in multi-turn tool-calling trajectories via diamond-aware retrieval and self-distillation. It shifts the paradigm from global forcing to topology-guided localized correction.

rss · Hugging Face Daily Papers · Sep 1, 01:54

**「为什么重要」** It tackles a key limitation in autonomous agent development where forcing rich combinatorial solution spaces into monolithic trajectories degrades policy diversity.

**「可关注」** 可关注：DART-SD shifts from global forcing to topology-guided localized correction for self-distillation in multi-turn tool-calling.

**Tags**: `#coding-agent`, `#orchestration`, `#eval`, `#tool-calling`, `#self-distillation`

---

<a id="item-agent-engineer-4"></a>
### [ElephantBench: Probing LLMs&\#x27; Epistemic Myopia on Long-Tail Knowledge](https://huggingface.co/papers/2608.28478) ⭐️ 6.0/10

HF Daily Papers introduces ElephantBench, a closed-book knowledge probe benchmark with 1,094 multi-account QA records generated from web corpus disagreements to test LLMs&\#x27; epistemic myopia on long-tail facts. The benchmark is created through an auditable graph-based pipeline that retrieves related documents from a low-exposure web corpus, identifies naturally occurring disagreements, and converts them into multi-account QA records. Each answer is verified against the originating documents and authoritative public web sources and reviewed by human annotators. Across 32 models, even the strongest model recovers both accounts on only 52.4% of questions, while on nearly all remaining questions it recalls one account but omits the other.

rss · Hugging Face Daily Papers · Sep 1, 01:54

**「Why it matters」** This benchmark is directly relevant to eval and harness improvements as it exposes LLMs&\#x27; limitations in handling divergent long-tail knowledge that arises in real-world web data.

**「What to watch」** What to watch: LLMs exhibit high epistemic myopia on long-tail facts, recovering both divergent accounts on only 52.4% of ElephantBench questions even in the strongest model.

**Tags**: `#eval`, `#harness`, `#benchmark`, `#knowledge-probing`

---

## AI Daily

<a id="item-ai-daily-1"></a>
### [ChatGPT Ads Hits $1B ARR and Expands Globally](https://openai.com/index/expanding-access-to-ai-with-chatgpt-ads) ⭐️ 6.8/10

OpenAI reports that ChatGPT Ads has reached $1 billion in annualized revenue run rate. The service is expanding globally. This supports broader access to AI through free and affordable options.

rss · OpenAI Blog · Aug 31, 04:00

**「Why It Matters」** The global expansion with free and affordable options supports broader AI access.

**「Engineer Takeaway」** Key Takeaway: ChatGPT Ads global expansion supports free and affordable AI access.

**Tags**: `#openai`, `#chatgpt`, `#ads`, `#revenue`, `#access`

---

<a id="item-ai-daily-2"></a>
### [Polimill Builds Japan&\#x27;s Next-Generation Public AI Infrastructure](https://openai.com/index/polimill) ⭐️ 5.8/10

Polimill is building Japan&\#x27;s next-generation public AI infrastructure. The company uses OpenAI GPT models and Codex to help municipalities search and use administrative knowledge. This helps accelerate development.

rss · OpenAI Blog · Aug 31, 07:00

**「Why it matters」** This collaboration demonstrates OpenAI GPT models and Codex being applied to municipal public services in Japan.

**「Key takeaway」** Key takeaway: Polimill uses OpenAI GPT models and Codex to help municipalities search and use administrative knowledge while accelerating development.

**Tags**: `#openai`, `#product`, `#industry`, `#japan`, `#partnership`

---

<a id="item-ai-daily-3"></a>
### [LWiAI Podcast \#255: Gemini 3.7 Flash, Jalapeño, Qwen 3.8, Drones](https://lastweekin.ai/p/lwiai-podcast-255-gemini-37-jalapeno) ⭐️ 5.0/10

Last Week in AI podcast recaps Google&\#x27;s Gemini 3.7 Flash launch. Jalapeño&\#x27;s first results show industry-leading speed. The episode also covers Qwen 3.8. An AI-guided drone killed three Ukrainians.

rss · Last Week in AI · Aug 31, 08:20

**「Key Takeaway」** Jalapeño shows industry-leading speed in its first results.

**Tags**: `#model`, `#lab`, `#industry`, `#product`

---