---
layout: default
title: "Horizon Summary: 2026-09-09 (EN)"
date: 2026-09-09
lang: en
---

> From 182 items, 17 important content pieces were selected

---

**Agent Harness Architecture**
1. [Claude Code v2.1.265 发布](#item-harness-arch-1) ⭐️ 7.8/10
2. [agents-js v0.17.1 发布](#item-harness-arch-2) ⭐️ 7.8/10
3. [Goose v1.50.0 发布](#item-harness-arch-3) ⭐️ 6.8/10
4. [openai-agents-python v0.22.1 发布](#item-harness-arch-4) ⭐️ 6.8/10
5. [Gemini CLI v0.59.0 Released](#item-harness-arch-5) ⭐️ 6.8/10
6. [pydantic-ai v2.41.0 发布](#item-harness-arch-6) ⭐️ 5.8/10
7. [Gemini CLI v0.60.0-preview.0 Released](#item-harness-arch-7) ⭐️ 5.8/10
8. [browser-use/browser-use GitHub Trending](#item-harness-arch-8) ⭐️ 5.0/10
9. [EveryInc Compound Engineering 插件 登 GitHub Trending](#item-harness-arch-9) ⭐️ 5.0/10

**AI Agent Engineer**
1. [OpenAI Internal Model Solves Navier-Stokes Millennium Prize Problem](#item-agent-engineer-1) ⭐️ 7.0/10
2. [Safety for Whom? Narrow-Boundary LLM Safety](#item-agent-engineer-2) ⭐️ 5.8/10

**AI Daily**
1. [OpenAI Blog: The Work Now Within Reach](#item-ai-daily-1) ⭐️ 8.8/10
2. [OpenAI AI Solution to Navier-Stokes Problem](#item-ai-daily-2) ⭐️ 8.8/10
3. [OpenAI $5M Grant for AI Teen Development Research](#item-ai-daily-3) ⭐️ 7.8/10
4. [GPT-5.6 Sol Runs MIT Quantum Experiments](#item-ai-daily-4) ⭐️ 5.8/10
5. [ChatGPT Images 2.5 Released](#item-ai-daily-5) ⭐️ 5.8/10

**Technology News**
1. [Simon Willison on OpenAI Navier-Stokes Millennium Prize Problem](#item-tech-news-1) ⭐️ 0.0/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [Claude Code v2.1.265 发布](https://github.com/anthropics/claude-code/releases/tag/v2.1.265) ⭐️ 7.8/10

Claude Code v2.1.265 is released by Anthropic. The update adds support for pointing --plugin-dir at a folder of plugins, with each child folder containing a manifest dynamically loading and updating as children are added or removed. It enhances telemetry by sending user.email and user.groups through the Claude apps gateway to match terminal sessions and introduces a 1GB cap on tool results saved to disk with truncation notices in previews. Bug fixes address subagent resuming, prompt cache reuse, session recovery, and multiple other issues in sandboxing, UI, and MCP servers.

github · ashwin-ant · Sep 8, 20:37

**「设计要点」** The release touches runtime state machines for subagent resuming and process recovery, memory and prefix-cache for prompt reuse after tool list or system prompt changes, tools for artifact publishing and advisor decisions, and sandboxing for plugin paths, symlink containment, and container management.

**「改了什么」** v2.1.265 adds dynamic plugin folder loading via --plugin-dir and a 1GB limit on tool results saved to disk. It fixes subagent prompt-cache reuse after tool list or system prompt updates and improves session resuming after process death or interrupted tool calls.

**Tags**: `#runtime`, `#tools`, `#sandbox`, `#memory`, `#subagents`, `#prefix-cache`

---

<a id="item-harness-arch-2"></a>
### [agents-js v0.17.1 发布](https://github.com/openai/openai-agents-js/releases/tag/v0.17.1) ⭐️ 7.8/10

openai-agents-js v0.17.1 is a patch of the OpenAI JS Agents SDK over v0.17.0. It adds server-wide MCP tool guardrails, custom blocked messages for output guardrails, labels on Docker sandbox containers, and image results for web search tools. Fixes recover failed resumed Session writes, preserve approval ownership across resume and handoff, keep Chat Completions tool turns during replay, isolate cached MCP tool definitions, and block sandbox Git repository argument injection.

github · seratch · Sep 8, 10:04

**「设计要点」** MCP tool guardrails can run server-wide; cached MCP tool definitions are isolated and MCP server lifecycle ownership is deduplicated. Session writes, approval ownership, and deferred tool identity persist across resume, handoff, and compaction; Chat Completions replay preserves tool turns.

**「改了什么」** Relative to v0.17.0, the SDK adds server-wide MCP tool guardrails, custom output-guardrail blocked messages, web-search image results, and Docker sandbox container labels. Resume, handoff, and replay keep approval ownership, deferred tool identity, session writes, and Chat Completions tool turns.

**Tags**: `#mcp`, `#sandbox`, `#tools`, `#runtime`, `#guardrails`

---

<a id="item-harness-arch-3"></a>
### [Goose v1.50.0 发布](https://github.com/aaif-goose/goose/releases/tag/v1.50.0) ⭐️ 6.8/10

Goose v1.50.0 supports GPT-6 Astra models and enhances tool calling for agents. It includes Kotlin Databricks AI Gateway configuration and bug fixes for Snowflake HTTPS, subagent guards, permissions, and UI issues.

github · github-actions\[bot\] · Sep 8, 19:32

**Tags**: `#tools`, `#subagents`, `#permissions`, `#runtime`

---

<a id="item-harness-arch-4"></a>
### [openai-agents-python v0.22.1 发布](https://github.com/openai/openai-agents-python/releases/tag/v0.22.1) ⭐️ 6.8/10

openai/openai-agents-python v0.22.1 is released. The update adds configurable Unix-local sandbox isolation for the sandbox environment. It also introduces server-wide guardrails for MCP tools, support for image results in web search tools, and includes minor fixes to core, voice, and other components.

github · seratch · Sep 8, 09:18

**「改了什么」** The v0.22.1 release adds configurable Unix-local sandbox isolation and server-wide guardrails for MCP tools. It also supports image results in web search tools along with minor fixes to core runtime, voice, and session management.

**Tags**: `#sandbox`, `#mcp`, `#runtime`, `#tools`

---

<a id="item-harness-arch-5"></a>
### [Gemini CLI v0.59.0 Released](https://github.com/google-gemini/gemini-cli/releases/tag/v0.59.0) ⭐️ 6.8/10

google-gemini/gemini-cli v0.59.0 is released. The update prevents SSRF in MCP OAuth metadata discovery and authentication. It also enforces fail-closed workspace trust and mcpServers filtering in restricted mode.

github · gemini-cli-robot · Sep 8, 21:13

**「What Changed」** Fixed SSRF in MCP OAuth metadata discovery and authentication. Enforced fail-closed workspace trust and filtered mcpServers in restricted mode.

**Tags**: `#mcp`, `#permissions`, `#tools`, `#sandbox`, `#runtime`

---

<a id="item-harness-arch-6"></a>
### [pydantic-ai v2.41.0 发布](https://github.com/pydantic/pydantic-ai/releases/tag/v2.41.0) ⭐️ 5.8/10

pydantic-ai v2.41.0 introduces the ImageGenerator API for direct image generation. It deprecates fallback\_model in favor of fallback\_subagent\_model on ImageGeneration and XSearch classes. The update also adds an openai-codex provider for ChatGPT and Codex authentication and includes bug fixes.

github · dsfaccini · Sep 8, 04:15

**「改了什么」** Deprecates fallback\_model in favor of fallback\_subagent\_model on ImageGeneration and XSearch. Adds direct image generation API with ImageGenerator, openai-codex provider, and fixes bugs in web search reporting, Bedrock error handling, and Gemini thinking levels.

**Tags**: `#subagents`, `#tools`, `#image-generation`, `#providers`

---

<a id="item-harness-arch-7"></a>
### [Gemini CLI v0.60.0-preview.0 Released](https://github.com/google-gemini/gemini-cli/releases/tag/v0.60.0-preview.0) ⭐️ 5.8/10

Google Gemini CLI v0.60.0-preview.0 is released. It includes minor updates to core utilities for improved destination validation and connection routing. Key technical changes cover MCP OAuth flow enforcement following RFC 9207, macOS Seatbelt sandbox temporary directory isolation, and hardened path resolution in the extensions loader. The release aggregates changelogs from prior versions.

github · gemini-cli-robot · Sep 8, 21:04

**「What Changed」** Relative to v0.59.0-preview.0, this version adds RFC 9207 issuer checks in the MCP OAuth flow, macOS Seatbelt sandbox directory isolation, extension loader boundary validation, and core safety fixes including NTFS 8.3 short name path mitigation and workspace boundary checks.

**Tags**: `#mcp`, `#sandbox`, `#runtime`, `#extensions`

---

<a id="item-harness-arch-8"></a>
### [browser-use/browser-use GitHub Trending](https://github.com/browser-use/browser-use) ⭐️ 5.0/10

browser-use/browser-use is trending on GitHub. It enables AI agents to automate web browser tasks by opening pages, clicking buttons, typing, and filling forms like humans do. Users describe the task in natural language and it completes it automatically. Examples include filling job applications with resume details and extracting structured data about followers.

rss · GitHub Trending Daily · Sep 9, 01:20

**Tags**: `#tools`, `#sandbox`, `#runtime`

---

<a id="item-harness-arch-9"></a>
### [EveryInc Compound Engineering 插件 登 GitHub Trending](https://github.com/EveryInc/compound-engineering-plugin) ⭐️ 5.0/10

EveryInc Compound Engineering plugin is trending on GitHub. It is an official plugin for Claude Code, Codex, Cursor, and more. It offers 33 skills for AI coding agents structured in a brainstorm-plan-build-review-capture loop with persistent knowledge capture across changes. It runs on 14 agent hosts.

rss · GitHub Trending Daily · Sep 9, 01:20

**「设计要点」** The plugin implements persistent knowledge capture across changes in the agent loop. It runs on 14 agent hosts.

**Tags**: `#planning`, `#memory`, `#tools`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [OpenAI Internal Model Solves Navier-Stokes Millennium Prize Problem](https://openai.com/index/navier-stokes-solution/) ⭐️ 7.0/10

OpenAI announces that an internal AI model has solved the Navier-Stokes existence and smoothness problem, one of the Millennium Prize Problems. The proof shows that the dynamics of the Navier-Stokes equations for fluid motion can develop a singularity in finite time. This is produced by an internal OpenAI system. The model, trained for less than two weeks, is more than twice as capable in mathematics as the Astra model, which was only made public a week ago.

hackernews · tedsanders · Sep 8, 17:13 · [Discussion](https://news.ycombinator.com/item?id=49613262)

**「Why it matters」** This development highlights the accelerating pace of AI progress in complex mathematical domains and raises questions about research incentives in theoretical physics.

**「Engineer takeaway」** OpenAI&\#x27;s internal model, trained for less than two weeks, is more than twice as capable in mathematics as the recently public Astra model.

**「Community discussion」** Community members note the rapid gains in AI mathematical capabilities and discuss the drama around the announcement, including Terence Tao&\#x27;s observations on how rumors of AI work can trigger massive effort and affect sharing of research directions. Some question if the solution is based on others&\#x27; actual work.

**Tags**: `#eval`, `#coding-agent`, `#orchestration`

---

<a id="item-agent-engineer-2"></a>
### [Safety for Whom? Narrow-Boundary LLM Safety](https://huggingface.co/blog/MultiverseComputingCAI/safety-for-whom) ⭐️ 5.8/10

The Hugging Face blog critiques topic-level LLM safety guardrails, noting that real deployments require different boundaries within the same topic. It introduces the paper &quot;Safety for Whom? Boundary-Aware Self-Distillation for Controlled LLM Safety Refusal,&quot; which studies narrow-boundary safety by refusing only the harmful subset of a topic while answering the benign complement. The work identifies issues with self-generated safety tuning, such as coverage gaps and over-refusal, and proposes solutions like escalating retries, in-distribution benign data, and held-out boundary pairs. This has implications for agent permissions and safety harnesses.

rss · Hugging Face Blog · Sep 8, 14:23

**「Why it matters」** This framing allows for more precise safety that respects specific deployment policies, avoiding the bluntness of topic-level guards like LlamaGuard-3, and emphasizes measuring both sides of the boundary for accurate trade-off assessment.

**「What to watch」** Data composition, including boundary pairs, controls the trade-off between harmful refusal and over-refusal on benign prompts; both sides of the intended boundary must be evaluated.

**Tags**: `#eval`, `#harness`, `#permissions`

---

## AI Daily

<a id="item-ai-daily-1"></a>
### [OpenAI Blog: The Work Now Within Reach](https://openai.com/index/the-work-now-within-reach) ⭐️ 8.8/10

OpenAI blog post titled The Work Now Within Reach explores how more capable and affordable AI can expand the work people and businesses can accomplish and make growth more economical.

rss · OpenAI Blog · Sep 8, 13:00

**Tags**: `#openai`, `#model`, `#industry`

---

<a id="item-ai-daily-2"></a>
### [OpenAI AI Solution to Navier-Stokes Problem](https://openai.com/index/navier-stokes-solution) ⭐️ 8.8/10

OpenAI is sharing an AI-generated solution to the Navier–Stokes Millennium Prize Problem, including a writeup and a formal proof in Lean. This is the first official release from OpenAI with verifiable original content. The announcement was made on the OpenAI blog.

rss · OpenAI Blog · Sep 8, 10:00

**Tags**: `#OpenAI`, `#model`, `#industry`, `#eval`, `#open-source`

---

<a id="item-ai-daily-3"></a>
### [OpenAI $5M Grant for AI Teen Development Research](https://openai.com/index/teen-development-research-grants) ⭐️ 7.8/10

OpenAI is launching a $5 million grant program to support independent research examining how generative AI affects adolescent development, well-being, and safety.

rss · OpenAI Blog · Sep 8, 09:00

**「Key Takeaway」** Key takeaway: Researchers can apply for OpenAI&\#x27;s $5 million grant to study generative AI&\#x27;s impact on teen development, well-being, and safety.

**Tags**: `#lab`, `#policy`, `#industry`

---

<a id="item-ai-daily-4"></a>
### [GPT-5.6 Sol Runs MIT Quantum Experiments](https://openai.com/index/codex-quantum-computing-experiments) ⭐️ 5.8/10

An MIT researcher uses GPT-5.6 Sol integrated with Codex to autonomously run quantum computing experiments, analyze results, and calibrate qubits.

rss · OpenAI Blog · Sep 8, 17:00

**「Focus on」** Focus on: GPT-5.6 Sol integrated with Codex enables autonomous running of quantum computing experiments along with result analysis and qubit calibration.

**Tags**: `#openai`, `#quantum-computing`, `#gpt`, `#ai-application`, `#industry`

---

<a id="item-ai-daily-5"></a>
### [ChatGPT Images 2.5 Released](https://openai.com/index/introducing-chatgpt-images-2-5) ⭐️ 5.8/10

OpenAI introduces ChatGPT Images 2.5. It helps turn your ideas, sketches, and reference photos into more personalized, polished images that better reflect your ideas.

rss · OpenAI Blog · Sep 8, 11:30

**Tags**: `#openai`, `#product`, `#chatgpt`, `#image-generation`

---

## Technology News

<a id="item-tech-news-1"></a>
### [Simon Willison on OpenAI Navier-Stokes Millennium Prize Problem](https://twitter.com/simonw/status/tweet-2097474703380365698) ⭐️ 0.0/10

Simon Willison shared his thoughts on the OpenAI Navier-Stokes Millennium Prize Problem story. This highlights the still confusing question of what using data &quot;to improve model performance&quot; actually means. The tweet connects this to the broader context of AI development. It matters as it addresses the ambiguous nature of data usage in model training. Willison&\#x27;s analysis offers insightful commentary on these technical aspects.

twitter · Simon Willison · Sep 8, 23:58

**「Navier-Stokes Millennium Prize Problem」** The Navier-Stokes equations, formulated in the 19th century, describe the motion of viscous fluid substances. The Millennium Prize Problem, one of the seven unsolved challenges selected by the Clay Mathematics Institute in 2000, asks whether the solutions to these equations remain smooth for all time or can develop singularities in finite time. OpenAI&\#x27;s internal AI system has claimed a proof that singularities can occur in finite time, using computational resources equivalent to $15 million in AI effort, as detailed in their writeup and Lean formalization.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/navier-stokes-solution/">On the Navier-Stokes Millennium Prize Problem | OpenAI</a></li>
<li><a href="https://www.newscientist.com/article/2588063-openai-has-solved-the-navier-stokes-millennium-problem-using-15m-of-ai-effort/">OpenAI has solved the Navier-Stokes Millennium problem using $15m of AI ...</a></li>
<li><a href="https://www.nature.com/articles/d41586-026-02842-5">OpenAI claims huge maths breakthrough on a famed &#x27;Millennium Problem ...</a></li>

</ul>
</details>

**Tags**: `#OpenAI`, `#Navier-Stokes`, `#Millennium Prize Problem`, `#AI Data Usage`, `#Tech Analysis`

---