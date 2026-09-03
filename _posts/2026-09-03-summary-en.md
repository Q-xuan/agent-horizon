---
layout: default
title: "Horizon Summary: 2026-09-03 (EN)"
date: 2026-09-03
lang: en
---

> From 207 items, 23 important content pieces were selected

---

**Agent Harness Architecture**
1. [Claude Code v2.1.259 发布](#item-harness-arch-1) ⭐️ 7.8/10
2. [LangChain 1.4.0a4 released](#item-harness-arch-2) ⭐️ 7.8/10
3. [Cline v4.1.17 Release](#item-harness-arch-3) ⭐️ 6.8/10
4. [openai/codex rust-v0.153.0 released](#item-harness-arch-4) ⭐️ 5.8/10
5. [Cline SDK v0.0.82 发布](#item-harness-arch-5) ⭐️ 5.8/10
6. [Cline desktop-v0.0.22 released](#item-harness-arch-6) ⭐️ 5.8/10
7. [Cline cli-v3.0.61 发布](#item-harness-arch-7) ⭐️ 5.8/10
8. [browser-use/video-use GitHub trending](#item-harness-arch-8) ⭐️ 5.0/10

**AI Agent Engineer**
1. [llm-gemini 0.34 发布](#item-agent-engineer-1) ⭐️ 7.0/10
2. [HF Daily: Consolidating 200+ Apps to Self-Hosted LLM](#item-agent-engineer-2) ⭐️ 7.0/10
3. [Harness-of-Harness: Multi-Day Autonomous Software Development with Continual Improvement](#item-agent-engineer-3) ⭐️ 7.0/10
4. [llm 0.34 日志增加耗时并加速](#item-agent-engineer-4) ⭐️ 6.8/10
5. [Gemini 3.8 Flash 发布](#item-agent-engineer-5) ⭐️ 6.0/10
6. [H3-World: Language-Native World Control](#item-agent-engineer-6) ⭐️ 6.0/10
7. [llm-openrouter 0.7.1 released with OpenRouter model loading performance fix](#item-agent-engineer-7) ⭐️ 5.8/10
8. [IBM TSFM on Confluent Enables Real-Time Intelligence](#item-agent-engineer-8) ⭐️ 5.8/10

**AI Daily**
1. [GitHub Copilot Makes AI Coding More Cost Efficient](#item-ai-daily-1) ⭐️ 7.8/10
2. [Meta Builds Organizational Second Brain AI](#item-ai-daily-2) ⭐️ 7.8/10
3. [GitHub Podcast Decodes New AI Lingo](#item-ai-daily-3) ⭐️ 6.8/10
4. [ATV Big Air Tour Uses ChatGPT to Cut Marketing Time](#item-ai-daily-4) ⭐️ 5.8/10

**AI Deals**
1. [LongCat-2.0 Free to Try in Cline](#item-ai-deals-1) ⭐️ 6.0/10
2. [Éclat Blue One-Click Auth：SDK-free OIDC Beta](#item-ai-deals-2) ⭐️ 5.0/10
3. [Free Phone Number Live-Interprets Calls in 47 Languages](#item-ai-deals-3) ⭐️ 5.0/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [Claude Code v2.1.259 发布](https://github.com/anthropics/claude-code/releases/tag/v2.1.259) ⭐️ 7.8/10

Claude Code v2.1.259 is released by Anthropic. It adds managedMcpServers to let organizations provide HTTP/SSE MCP servers to users. --permission-prompts none is added for headless hosts and GitLab MR support is added for glab commands. Concurrent sessions no longer revert each other&\#x27;s ~/.claude.json changes.

github · ashwin-ant · Sep 2, 22:33

**「改了什么」** v2.1.259 adds managedMcpServers allowing organizations to provide HTTP/SSE MCP servers and --permission-prompts none for headless hosts. GitLab MR support and concurrent session fixes are included.

**Tags**: `#mcp`, `#permissions`, `#tools`, `#runtime`, `#memory`

---

<a id="item-harness-arch-2"></a>
### [LangChain 1.4.0a4 released](https://github.com/langchain-ai/langchain/releases/tag/langchain%3D%3D1.4.0a4) ⭐️ 7.8/10

LangChain 1.4.0a4 alpha release updates MCP client handling, interrupt routing, and reentrant groups for fastmcp compatibility.

It refactors the adapter by inlining client arming into \_\_init\_\_, stamping an arm marker instead of introspecting the handler closure, gating interrupt routing on the negotiated protocol era, dropping the elicitation flag, and adding \_ReentrantClientGroup.

This builds on the prior 1.4.0a3 MCP namespace feature.

github · github-actions\[bot\] · Sep 2, 05:35

**「What changed」** Relative to 1.4.0a3, this release adds \_ReentrantClientGroup, inlines MCP client arming into \_\_init\_\_, uses arm marker stamping, gates interrupt routing on protocol era, and drops the elicitation flag.

It updates tests to cover mixed-era ClientGroup and group elicitation.

**Tags**: `#mcp`, `#runtime`, `#tools`

---

<a id="item-harness-arch-3"></a>
### [Cline v4.1.17 Release](https://github.com/cline/cline/releases/tag/v4.1.17) ⭐️ 6.8/10

Cline v4.1.17 is a patch release for the Cline AI coding agent. It surfaces ClinePass UI elements and fixes background Hub process memory growth plus related crashes. The release includes fixes for long session memory ballooning by using snapshots instead of broadcasting full transcripts, hook script crash prevention, and various other stability and credential issues.

github · github-actions\[bot\] · Sep 2, 05:40

**「Design points」** The memory fix changes session status updates to carry only state snapshots instead of full conversation transcripts, preventing process ballooning to tens of gigabytes during long tasks. Hook script failures no longer crash the core process.

**「Changed」** Relative to v4.1.16, the key change is the memory optimization for long sessions using snapshots. Other changes include surfacing ClinePass UI, improved credential handling, and a refreshed model catalog.

**Tags**: `#runtime`, `#memory`, `#tools`

---

<a id="item-harness-arch-4"></a>
### [openai/codex rust-v0.153.0 released](https://github.com/openai/codex/releases/tag/rust-v0.153.0) ⭐️ 5.8/10

openai/codex rust-v0.153.0 is released. It adds Vim mode undo/redo support with \`u\` and \`Ctrl+R\`, a plugin CLI for listing/installing/removing plugins, an option to disable automatic recaps in TUI while keeping manual \`/recap\`, TUI history showing patches/commands, and automatic TUI session reconnect after app-server drops. Bug fixes include preserving drafts/transcripts on reconnect, skipping Guardian reviews for Full Access, and handling rollouts/MCP approvals. Plus and Team users receive earlier allowance warnings.

github · github-actions\[bot\] · Sep 3, 01:37

**「What Changed」** This release adds Vim mode undo/redo support, plugin CLI, auto recap disable option, TUI history, and session reconnect compared to rust-v0.152.1. It also includes fixes for TUI reconnection, Guardian review history, permission scoping, and configuration updates.

**Tags**: `#tools`, `#runtime`

---

<a id="item-harness-arch-5"></a>
### [Cline SDK v0.0.82 发布](https://github.com/cline/cline/releases/tag/sdk/sdk/v0.0.82) ⭐️ 5.8/10

Cline SDK v0.0.82 has been released with bug fixes and new features. The release resolves tool calling issues for gateway models, prevents image input stripping from empty capability lists, and supports Langfuse tracing in minified builds. It introduces SessionImportService to import sessions from Claude Code, Codex, and opencode, and refreshes the model catalog with new providers and changed defaults for 57 providers.

github · github-actions\[bot\] · Sep 2, 04:40

**「改了什么」** Relative to v0.0.81, v0.0.82 adds SessionImportService for importing conversation history from Claude Code, Codex, and opencode. It fixes capability handling for gateway models and empty lists, enables Langfuse tracing in minified builds, and refreshes the model catalog.

**Tags**: `#tools`, `#runtime`

---

<a id="item-harness-arch-6"></a>
### [Cline desktop-v0.0.22 released](https://github.com/cline/cline/releases/tag/desktop-v0.0.22) ⭐️ 5.8/10

Cline desktop v0.0.22 is released. It adds history import from Claude Code, Codex, and opencode into sessions. Schedule runs are now collapsed into a single collapsible sidebar row. Voice input is enabled on macOS.

github · github-actions\[bot\] · Sep 2, 05:20

**「What Changed」** History import now supports multiple tools with grouped sessions. Schedule runs are grouped into one sidebar row. Bug fixes include tool calling for Dify, SAP AI Core, opencode, and Codex CLI models.

**Tags**: `#tools`, `#runtime`, `#memory`

---

<a id="item-harness-arch-7"></a>
### [Cline cli-v3.0.61 发布](https://github.com/cline/cline/releases/tag/cli-v3.0.61) ⭐️ 5.8/10

Cline CLI v3.0.61 is released. It fixes hub replacement for older running hubs with a replacement prompt, unreachable remote MCP servers with a 10s timeout, Windows binaries Authenticode signing, and tool calling for Dify/SAP/opencode/Codex models. The model catalog is refreshed with new providers and updated defaults.

github · github-actions\[bot\] · Sep 2, 04:49

**「改了什么」** Relative to v3.0.60, changes include older hub replacement prompt, MCP server timeout handling, Windows signing, tool calling re-enable for specific models, checkpoint restore refusal on post-commit state, and model catalog refresh with ten new providers plus default updates for 57 providers.

**Tags**: `#mcp`, `#runtime`, `#tools`

---

<a id="item-harness-arch-8"></a>
### [browser-use/video-use GitHub trending](https://github.com/browser-use/video-use) ⭐️ 5.0/10

Announcement of open-source video-use tool for editing videos with coding agents and Claude Code. Drop raw footage in a folder, chat with Claude Code, get final.mp4 back. Works for any content — talking heads, montages, tutorials, travel, interviews — without presets or menus. The tool cuts out filler words and dead space between takes and auto color grades every segment.

rss · GitHub Trending Daily · Sep 3, 01:41

**Tags**: `#tools`, `#subagents`, `#planning`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [llm-gemini 0.34 发布](https://simonwillison.net/2026/Sep/2/llm-gemini/) ⭐️ 7.0/10

llm-gemini 0.34 adds support for Gemini 3.8 Flash model with low, medium, and high thinking levels. It fixes an async responses issue that failed to record the resolved model version. This update impacts users of the llm library in coding agents and harnesses.

rss · Simon Willison · Sep 2, 16:39

**「为什么重要」** Gemini 3.8 Flash is fast, cheap, and competent at HTML and JavaScript. The release enables integration with this new model in llm-based toolchains.

**「可关注」** 可关注：Support for Gemini 3.8 Flash with low, medium, and high thinking levels.

**Tags**: `#coding-agent`, `#harness`, `#orchestration`, `#model-integration`

---

<a id="item-agent-engineer-2"></a>
### [HF Daily: Consolidating 200+ Apps to Self-Hosted LLM](https://huggingface.co/papers/2609.01572) ⭐️ 7.0/10

HF daily paper describes consolidating traffic from over 200 internal applications onto a single self-hosted LLM by training separate GRPO experts per axis \(instruction following, function calling, internal task distribution\) and merging via two-stage SLERP. Quality is tracked by offline benchmarks stratified to production traffic and scored by deterministic verifiers or calibrated LLM judges. This approach addresses data-residency constraints by reducing the serving fleet while covering corporate request mixes.

rss · Hugging Face Daily Papers · Sep 3, 01:41

**「为什么重要」** Data-residency constraints force enterprises to self-host LLMs, expanding the serving fleet and fragmenting a finite GPU pool. Consolidating onto one model optimizes GPU resources for internal applications.

**「可关注」** Train separate GRPO experts per quality axis to avoid cross-domain reward interference, then merge via two-stage SLERP.

**Tags**: `#eval`, `#orchestration`, `#harness`, `#coding-agent`

---

<a id="item-agent-engineer-3"></a>
### [Harness-of-Harness: Multi-Day Autonomous Software Development with Continual Improvement](https://huggingface.co/papers/2609.01481) ⭐️ 7.0/10

Harness-of-Harness \(HoH\) is a framework that organizes coding-agent executions into iterative planning-coding-testing loops. It enables multi-day autonomous software development by balancing repair with capability growth, scoping development into small verifiable increments, separating implementation-time testing from independent evaluation, and constraining verifiable outputs rather than prescribing agent workflows. HoH operates on existing coding-agent harnesses and impacts agent harnesses, orchestration, and evals.

rss · Hugging Face Daily Papers · Sep 3, 01:41

**「Why it matters」** HoH provides concrete techniques for sustaining improvement across loops in LLM coding agents. These techniques directly affect how harnesses are built, orchestrated, and evaluated for multi-day autonomous development.

**「Attention」** Attention: Balance repair with capability growth across iterative loops while scoping to small verifiable increments and separating testing.

**Tags**: `#harness`, `#coding-agent`, `#eval`, `#orchestration`

---

<a id="item-agent-engineer-4"></a>
### [llm 0.34 日志增加耗时并加速](https://github.com/simonw/llm/releases/tag/0.34) ⭐️ 6.8/10

simonw 发布 llm 0.34。\`llm logs --usage\` 的 Markdown 现写入响应耗时，同时给出毫秒和可读时长；\`llm logs --short\` 增加 \`duration\_ms\` 字段。长对话里，\`llm logs\` 缓存重复的 message 与 model 查找；动态生成的 OpenAI options 类也改为缓存，避免 \`llm-openrouter\` 等插件反复构造 Pydantic 类。传给 \`llm prompt --schema\` 的非法 schema DSL 改为命令行报错，\`llm --extract\` 识别 CRLF 围栏代码块，\`monotonic\_ulid\(\)\` 在时钟回拨或并发时间戳乱序时仍保持单调，并直接依赖 \`typing-extensions\`。

github · simonw · Sep 2, 19:23

**「为什么重要」** \`llm logs\` 能直接读到单次响应耗时。长对话日志查找和插件反复构造 OpenAI options 类已做缓存，材料未给加速数字。

**「可关注」** 可关注：长对话上 \`llm logs\` 的重复查找，以及 \`llm-openrouter\` 一类插件对 OpenAI options Pydantic 类的重复构造，现已缓存。

**Tags**: `#coding-agent`, `#orchestration`, `#observability`

---

<a id="item-agent-engineer-5"></a>
### [Gemini 3.8 Flash 发布](https://blog.google/innovation-and-ai/models-and-research/gemini-models/3-8-flash-and-3-8-flash-cyber/) ⭐️ 6.0/10

Google released Gemini 3.8 Flash, a fast model competitive with larger ones in benchmarks. It is useful for tasks like HTML generation. The intelligence score is 59, the same as Opus 5 medium.

hackernews · bratao · Sep 2, 15:12 · [Discussion](https://news.ycombinator.com/item?id=49537553)

**「为什么重要」** This release is worth paying attention today because it is competitive with larger models in speed and benchmarks. The long-term impact in actual coding agent tasks remains to be seen.

**「可关注」** 可关注：Gemini 3.8 Flash performs well in HTML generation tasks.

**「评论」** Community discussion highlights excitement about the speed and HTML JavaScript capabilities from SimonW, positive experiences with trip planning from Jampa, and leaderboard leadership over Opus 5 from MattLondon.

**Tags**: `#coding-agent`, `#eval`, `#harness`

---

<a id="item-agent-engineer-6"></a>
### [H3-World: Language-Native World Control](https://www.reddit.com/r/LocalLLaMA/comments/1w5akpy/h3world_turning_language_understanding_into_world/) ⭐️ 6.0/10

H3-World converts language instructions into temporally grounded character and camera actions in video and game scenarios. It achieves this using only 8,000 gameplay samples, 10,000 LoRA steps, and 0.199% trainable parameters on MiniMax-H3. The method supports unseen action compositions and visual scenarios. Details appear in arXiv paper 2609.01560 and the GitHub repository at https://github.com/Danzer1xxxxChan/H3-World.

reddit · r/LocalLLaMA · /u/sachasayan · Sep 2, 13:35

**「Why it matters」** The paper demonstrates language-native world control with minimal trainable parameters. This advances agent systems that require precise character and camera control in dynamic environments.

**「Engineer takeaway」** Note: 0.199% trainable parameters suffice for controllable character and camera motion using 8,000 samples and 10,000 LoRA steps.

**Tags**: `#orchestration`, `#coding-agent`, `#harness`, `#eval`

---

<a id="item-agent-engineer-7"></a>
### [llm-openrouter 0.7.1 released with OpenRouter model loading performance fix](https://github.com/simonw/llm-openrouter/releases/tag/0.7.1) ⭐️ 5.8/10

Simonw released llm-openrouter 0.7.1. The update includes a performance fix for loading OpenRouter models. The fix was contributed by waveplate.

github · simonw · Sep 2, 20:23

**「What to watch」** What to watch: Performance fix for loading OpenRouter models.

**Tags**: `#orchestration`, `#coding-agent`

---

<a id="item-agent-engineer-8"></a>
### [IBM TSFM on Confluent Enables Real-Time Intelligence](https://huggingface.co/blog/ibm-research/real-time-intelligence) ⭐️ 5.8/10

IBM integrates its Time Series Foundation Models with Confluent to enable real-time intelligence. Models generalize to unseen series for forecasting, anomaly detection, similarity search, classification, gap-filling, and optimization. They run via Flink SQL functions in Confluent Cloud, with benefits including real-time processing on live data, zero configuration, fresh enriched context, built-in governance, cost efficiency, and enhanced security. A portfolio of four models is in Early Access.

rss · Hugging Face Blog · Sep 2, 13:49

**「Why it matters」** This bridges operational and analytical estates to turn live business events into actionable intelligence. Flink handles stateful forecasting and detection with per-series history, so signals retain value before they decay.

**「Observable」** Observable: Switch between the four TSFM models with one SQL parameter in the AI\_FORECAST function, no pipeline redesign required.

**Tags**: `#orchestration`, `#observability`, `#real-time`, `#time-series`, `#foundation-model`

---

## AI Daily

<a id="item-ai-daily-1"></a>
### [GitHub Copilot Makes AI Coding More Cost Efficient](https://github.blog/ai-and-ml/github-copilot/how-we-make-ai-coding-more-cost-efficient-without-sacrificing-task-quality/) ⭐️ 7.8/10

GitHub explains how to make AI coding more cost-efficient without sacrificing task quality using GitHub Copilot. Shorter outputs can cost more, and GitHub Copilot reduces wasted work across the complete coding task.

rss · GitHub Blog · Sep 2, 18:00

**「Why it matters」** This approach helps teams optimize costs in AI-assisted coding while keeping high task quality.

**「Engineer takeaway」** Key takeaway: Shorter outputs can cost more, and GitHub Copilot reduces wasted work across the complete coding task.

**Tags**: `#lab`, `#product`, `#industry`

---

<a id="item-ai-daily-2"></a>
### [Meta Builds Organizational Second Brain AI](https://engineering.fb.com/2026/09/02/ml-applications/organizational-second-brain-ai-learns-from-experts/) ⭐️ 7.8/10

Meta has built an AI agent that acts as a secondary expert for a given domain, making deep specialist knowledge readily available and preserved for anyone in an organization to access, share, and build upon. Its novelty comes from integrating two layers: a structured, auditable knowledge architecture.

rss · Engineering at Meta · Sep 2, 09:00

**「Why It Matters」** This approach enables organizations to preserve and share specialist knowledge through an integrated structured and auditable architecture.

**「Takeaway」** The system integrates a structured, auditable knowledge architecture to preserve specialist knowledge.

**Tags**: `#lab`, `#product`, `#industry`

---

<a id="item-ai-daily-3"></a>
### [GitHub Podcast Decodes New AI Lingo](https://github.blog/ai-and-ml/decoding-the-new-ai-lingo-loops-harnesses-squads-hill-climbing-oh-my/) ⭐️ 6.8/10

GitHub Blog published a post decoding new AI lingo from the GitHub Podcast. The terms include loops, harnesses, squads, and hill climbing. The post explains these terms as they appear in developer conversations. It covers loop engineering to open weights.

rss · GitHub Blog · Sep 2, 21:00

**「Why it matters」** Understanding these new AI terms helps developers follow GitHub Podcast and community discussions.

**「Engineer takeaway」** Takeaway: GitHub Podcast breaks down AI terms like loops, harnesses, squads, and hill climbing from loop engineering to open weights.

**Tags**: `#github`, `#industry`, `#ai-terms`

---

<a id="item-ai-daily-4"></a>
### [ATV Big Air Tour Uses ChatGPT to Cut Marketing Time](https://openai.com/index/atv-big-air-tour) ⭐️ 5.8/10

ATV Big Air Tour used ChatGPT to accelerate marketing and merchandising. This reduced three days of work to three hours. They created an inventory website from merchandise photos in 15 minutes.

rss · OpenAI Blog · Sep 2, 12:00

**「Why It Matters」** The case demonstrates how ChatGPT can transform manual marketing and inventory tasks into fast automated processes.

**「Takeaway」** Use ChatGPT to generate inventory websites from photos in 15 minutes and cut marketing work from three days to three hours.

**Tags**: `#industry`, `#product`, `#ChatGPT`

---

## AI Deals

<a id="item-ai-deals-1"></a>
### [LongCat-2.0 Free to Try in Cline](https://twitter.com/Meituan_LongCat/status/2094996391387111865) ⭐️ 6.0/10

Meituan announces LongCat-2.0 is now free to try in Cline. No specific quota, duration or access limits are provided.

rss · HN Free API / Credits · Sep 2, 09:58

**「Note」** LongCat-2.0 is available for free trial in Cline without specified limits.

**Tags**: `#free-tier`, `#promo`, `#model`

---

<a id="item-ai-deals-2"></a>
### [Éclat Blue One-Click Auth：SDK-free OIDC Beta](https://news.ycombinator.com/item?id=49543502) ⭐️ 5.0/10

Éclat Blue One-Click Auth is a lightweight OIDC identity provider in small-scale beta. It allows frontend apps to be secured directly through native browser APIs without bulky SDKs or exposed client secrets. The tool is currently ready for small-scale beta use and can be inspected without an account via the Try Me link.

rss · HN Free API / Credits · Sep 2, 22:32

**「为什么重要」** This beta provides a simple alternative for public clients, avoiding heavy SDKs and secret management for frontend authentication.

**「可关注」** Note: It is suitable for frontend applications and enforces strict authorization code flows with PKCE protocols natively.

**Tags**: `#free-tier`, `#promo`, `#api`, `#beta`, `#limited-free`

---

<a id="item-ai-deals-3"></a>
### [Free Phone Number Live-Interprets Calls in 47 Languages](https://translatemycall.com/) ⭐️ 5.0/10

Show HN post announces a free phone number service that live-interprets calls in 47 languages. The service is hosted at translatemycall.com. No signup details, usage limits, expiration dates, or restrictions are provided.

rss · HN Free API / Credits · Sep 2, 17:24

**Tags**: `#free-tier`, `#promo`

---