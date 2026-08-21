---
layout: default
title: "Horizon Summary: 2026-08-22 (EN)"
date: 2026-08-22
lang: en
---

> From 148 items, 20 important content pieces were selected

---

**Agent Harness Architecture**
1. [Cline SDK v0.0.77 Released](#item-harness-arch-1) ⭐️ 7.0/10
2. [DSPy 3.3.1 发布](#item-harness-arch-2) ⭐️ 7.0/10
3. [microsoft/agent-framework python-1.15.0 发布](#item-harness-arch-3) ⭐️ 7.0/10
4. [Cline SDK v0.0.76](#item-harness-arch-4) ⭐️ 6.0/10
5. [anomalyco/opencode v1.18.20 发布](#item-harness-arch-5) ⭐️ 6.0/10
6. [Claude Code 2.1.239](#item-harness-arch-6) ⭐️ 6.0/10
7. [Cline v4.1.12 Released](#item-harness-arch-7) ⭐️ 5.0/10

**AI Agent Engineer**
1. [Claudette: Make Claude stop talking like a BuzzFeed article](#item-agent-engineer-1) ⭐️ 7.0/10
2. [DeepSeek Harness v0.1.1 released](#item-agent-engineer-2) ⭐️ 7.0/10
3. [llm-openrouter 0.7 released](#item-agent-engineer-3) ⭐️ 6.0/10

**AI Daily**
1. [US Corporate AI Debt Surge Tests Investor Limits as Fatigue Emerges](#item-ai-daily-1) ⭐️ 7.0/10
2. [Minnesota Lawyer Suspended Over Fake AI Case Citations](#item-ai-daily-2) ⭐️ 7.0/10
3. [Moqi Uses Agentic-Native to Reconstruct Robot Embodiment Brain for Long-Term Tasks, Submits to WRC](#item-ai-daily-3) ⭐️ 6.0/10
4. [DeepSense 桌面 AI 系统：AI 跑实验](#item-ai-daily-4) ⭐️ 5.0/10
5. [Bohr Science Space: AI Scientists for Scientific Research](#item-ai-daily-5) ⭐️ 5.0/10
6. [End-to-End Paper Generation System: 92% Fake Conclusion Detection Rate, Auto Experiments, Figures, Drafts](#item-ai-daily-6) ⭐️ 5.0/10
7. [ICML 2026: BEACON Nearly Doubles Long-Range Agent Success Rates](#item-ai-daily-7) ⭐️ 5.0/10
8. [Tech Giants Frustrated with AI Slop](#item-ai-daily-8) ⭐️ 5.0/10

**AI Deals**
1. [Epic Games Free Games: Cardpocalypse, Albion Online, Desert Caravan \(Aug 21-27\)](#item-ai-deals-1) ⭐️ 6.0/10
2. [26/27 Premier League Schedule Calendar Live\!](#item-ai-deals-2) ⭐️ 5.0/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [Cline SDK v0.0.77 Released](https://github.com/cline/cline/releases/tag/sdk/sdk/v0.0.77) ⭐️ 7.0/10

Cline SDK v0.0.77 has been released. It scopes the tasks tool to only serviceable clients via centralized resolution based on declared client types. Hosts declare their client type and the core tool catalog resolves availability centrally, so CLI and VS Code sessions no longer register a tool they cannot act on; hub sessions resolve the same way from the requesting client&\#x27;s metadata.

github · github-actions\[bot\] · Aug 21, 04:56

**「改了什么」** Relative to v0.0.76, the tasks tool is now scoped to the clients that can service it. Hosts declare their client type and the core tool catalog resolves availability centrally.

**Tags**: `#runtime`, `#tools`

---

<a id="item-harness-arch-2"></a>
### [DSPy 3.3.1 发布](https://github.com/stanfordnlp/dspy/releases/tag/3.3.1) ⭐️ 7.0/10

DSPy 3.3.1 strengthens PythonInterpreter runtime with managed sandboxed execution, isolation hardening, and visibility into interpreter runs. It improves optimizer throughput, adapter correctness, and MCP compatibility. CodeAct and ProgramOfThought are deprecated.

github · isaacbmiller · Aug 21, 23:07

**「设计要点」** PythonInterpreter now supports optional managed runtime with Deno and Pyodide, hardened isolation, and callback API for execution lifecycle visibility.

**「改了什么」** Relative to prior versions, DSPy 3.3.1 adds managed runtime for PythonInterpreter, multi-proposal GEPA optimization, reliable structured adapter outputs, and MCP SDK v2 compatibility. It deprecates CodeAct and ProgramOfThought.

**Tags**: `#runtime`, `#sandbox`, `#mcp`, `#tools`, `#interpreter`

---

<a id="item-harness-arch-3"></a>
### [microsoft/agent-framework python-1.15.0 发布](https://github.com/microsoft/agent-framework/releases/tag/python-1.15.0) ⭐️ 7.0/10

Microsoft Agent Framework Python 1.15.0 introduces UI, middleware, checkpointing, and resilient hosting features. The release adds A2UI interface support, first-class MiddlewareFailure signals, process-wide checkpoint registry, and Foundry hosting resilience with long-running samples.

github · giles17 · Aug 21, 23:08

**「改了什么」** This release adds A2UI support for agent-generated interfaces, first-class MiddlewareFailure signals, process-wide workflow checkpoint type registry, and resilient Foundry Hosted Agents support with long-running workflow samples. It includes breaking changes to OpenTelemetry GenAI semantic-convention support.

**Tags**: `#runtime`, `#memory`, `#tools`

---

<a id="item-harness-arch-4"></a>
### [Cline SDK v0.0.76](https://github.com/cline/cline/releases/tag/sdk/sdk/v0.0.76) ⭐️ 6.0/10

Cline SDK v0.0.76 is released. It adds model-driven image generation where supported models can generate images during a turn, with images persisted in session history and exports. Agents can create and manage scheduled tasks and a durable todo agenda, with schedules scoped to the workspace. It also fixes skill command loading through the skills tool and makes provider-executed tool activities visible in runtime events, transcripts, and the UI.

github · github-actions\[bot\] · Aug 21, 02:39

**「Design Notes」** Provider-executed tool activities are now surfaced as observational events in runtime, transcripts, and UI instead of being dropped. PreToolUse hooks deliver contextModification as a hidden &lt;hook\_context&gt; block stamped with the tool name and call ID.

**「What Changed」** This release adds model-driven image generation with session persistence and scheduled tasks with durable todo agenda. It fixes skill command loading via the skills tool, records typed commands in transcripts, surfaces provider tool activities, and updates PreToolUse/PostToolUse hook handling to await outputs and honor controls.

**Tags**: `#runtime`, `#tools`, `#memory`, `#planning`

---

<a id="item-harness-arch-5"></a>
### [anomalyco/opencode v1.18.20 发布](https://github.com/anomalyco/opencode/releases/tag/v1.18.20) ⭐️ 6.0/10

anomalyco/opencode v1.18.20 is a bugfix release focusing on subagent failures, permissions, and network error retries. It surfaces failed subagent tool calls with a resumable task\_id and answers permission requests triggered by subagents during opencode run. The release also improves retry logic for network errors and preserves Cerebras max\_completion\_tokens.

github · opencode-agent\[bot\] · Aug 21, 08:09

**「改了什么」** v1.18.20 adds resumable task\_ids for subagent tool call failures and handles permission requests from subagents. It includes retry logic for network errors such as finish\_reason: network\_error and xAI stream errors.

**「评论」** No community comments available.

**Tags**: `#subagents`, `#permissions`, `#runtime`

---

<a id="item-harness-arch-6"></a>
### [Claude Code 2.1.239](https://code.claude.com/docs/en/changelog#2-1-239) ⭐️ 6.0/10

Claude Code 2.1.239 release covers cost estimate inclusion of US inference premium, fullscreen renderer rollout, Python API migration tool, synced plugin handling, and Alpine build support for native add-ons. The /claude-api upgrade command helps migrate Python projects from anthropic 0.x to 1.x. Cloud sessions now show synced plugins as name@synced and support enable/disable without overriding user-installed plugins. Alpine/musl builds allow native image paste, clipboard, and audio-capture add-ons to load.

rss · Claude Code Changelog · Aug 21, 21:09

**「Design notes」** Runtime sandbox changes enable Alpine/musl builds for native add-ons, fixing glibc compatibility for paste, clipboard, and audio features. Cloud sessions handle plugin syncing from claude.ai with specific permission rules to avoid overrides.

**「What changed」** This release adds the US inference premium to cost estimates, the Python API migration tool, and fullscreen renderer to previously excluded platforms. It also enables Alpine/musl support for native add-ons and improves plugin syncing in cloud sessions.

**Tags**: `#tools`, `#runtime`, `#sandbox`, `#permissions`, `#plugins`

---

<a id="item-harness-arch-7"></a>
### [Cline v4.1.12 Released](https://github.com/cline/cline/releases/tag/v4.1.12) ⭐️ 5.0/10

Cline v4.1.12 enforces enterprise MCP controls on the Customize marketplace and restores tool calling for custom OpenAI-Compatible models. This patch release applies to the SDK bundle, including on Windows. It hides MCP entries in the marketplace when remote config disables the marketplace and limits them to \`allowedMCPServers\` when an allowlist is configured. Tool calling is restored for custom OpenAI-Compatible models whose stored capability list was empty.

github · github-actions\[bot\] · Aug 21, 22:39

**「Changes」** Enforces enterprise MCP controls on the Customize marketplace by hiding entries based on remote config and limiting to \`allowedMCPServers\` when an allowlist is configured. Restores tool calling for custom OpenAI-Compatible models with an empty stored capability list.

**Tags**: `#mcp`, `#permissions`, `#tools`, `#runtime`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [Claudette: Make Claude stop talking like a BuzzFeed article](https://github.com/adnanakil/nobuzz/blob/main/README.md) ⭐️ 7.0/10

The Claudette repository and accompanying instructions make Claude outputs concise and non-BuzzFeed style. They enforce strict limits including comment blocks &lt;= 7 words, function names &lt;= 4 words, and user-facing messages &lt;= 10 words, while requiring active voice and avoiding stage performances. This practical prompt-engineering technique aids coding agents, evals, and orchestration when chaining models to reduce verbosity, as shared on Hacker News alongside related discussions.

hackernews · aakil · Aug 21, 14:31 · [Discussion](https://news.ycombinator.com/item?id=49388752)

**「Why it matters」** The instructions provide a simple method to clean up Claude outputs for better agent harnesses and model chaining. While the repo and rules are now available, their impact on reducing verbosity in practice is still being verified through community use.

**「Takeaway」** Takeaway: Limiting the number of words is the strongest factor in cleaning up the output.

**「Comments」** Community members report success with these instructions, especially the word limits for generating clear output. Related discussions note similar techniques like the Vomit post and suggest chaining models as an alternative to long prompts.

**Tags**: `#orchestration`, `#eval`, `#coding-agent`, `#harness`

---

<a id="item-agent-engineer-2"></a>
### [DeepSeek Harness v0.1.1 released](https://www.reddit.com/r/LocalLLaMA/comments/1vugyfe/deepseek_harness_v011_released/) ⭐️ 7.0/10

DeepSeek Harness v0.1.1 has been released. The update adds support for the multimodal visual understanding model DeepSeek-V4-Flash-Vision-Exp. Commands such as /goal and /plan can now accept text and image input, and the @ menu can reference files and sessions. MCP/ACP supports persistent image attachments, and PTC Mode supports forwarding nested images.

reddit · r/LocalLLaMA · /u/Fun-Doctor6855 · Aug 21, 13:51

**「为什么重要」** The release enables multimodal capabilities in the harness for agent systems using vision models. The change has occurred, but its impact on workflows is not yet confirmed.

**「可关注」** Attention: Harness now supports native image requests in commands and attachments.

**Tags**: `#harness`, `#mcp`, `#orchestration`, `#coding-agent`

---

<a id="item-agent-engineer-3"></a>
### [llm-openrouter 0.7 released](https://simonwillison.net/2026/Aug/21/llm-openrouter/) ⭐️ 6.0/10

llm-openrouter 0.7 has been released. It adds support for OpenRouter&\#x27;s Responses API and three new server-side tools: Shell, WebFetch, and WebSearch. The plugin is now compatible with LLM 0.32, improving integration with reasoning LLMs available through OpenRouter for agent workflows.

rss · Simon Willison · Aug 21, 16:58

**「Why it matters」** This update enhances tool use in agent workflows by providing new server-side tools and better compatibility with reasoning models via OpenRouter.

**「Engineer takeaway」** Notable: The new server-side tools can be enabled with options like -T WebSearch.

**Tags**: `#orchestration`, `#coding-agent`, `#harness`, `#tool-use`

---

## AI Daily

<a id="item-ai-daily-1"></a>
### [US Corporate AI Debt Surge Tests Investor Limits as Fatigue Emerges](https://news.google.com/rss/articles/CBMivAFBVV95cUxNR0I5VXZyeVp4RlV6cnhVdXFwZ2RNZUU0Q1czQ2c0WkpZUUJuRV9PNEg0VHkzLVlnSUdZMWVOalJzNkNXdlNtamlGSzRLbVRXb0VkVzl3dm5Uc3hPV21Cb3BIdTNyOWZQSDRGQ1ZvV2xUVUZ6eExfeGpRM0hQck8wSDlzR3ViRDJHS25NaGxwNHdVYWN5cHRUcWJvb0hybjRtclNxMFFGT18tMmc2SEw5RFNYb3ZrSWZpS0VYTw?oc=5) ⭐️ 7.0/10

US companies are accumulating large AI-related debt, straining investor confidence as fatigue with AI investments grows. This represents a clear new industry trend. The development is testing the limits of investor support for AI projects.

google\_news · Reuters · Aug 21, 15:07

**「Why It Matters」** This trend matters because it signals growing investor skepticism toward the rapid pace of AI spending by corporations.

**「Key Takeaway」** Key Takeaway: US corporate AI debt is surging, testing investor limits amid emerging fatigue.

**Tags**: `#industry`, `#AI`, `#finance`, `#investment`, `#debt`

---

<a id="item-ai-daily-2"></a>
### [Minnesota Lawyer Suspended Over Fake AI Case Citations](https://news.google.com/rss/articles/CBMinwFBVV95cUxPbDU2dVoya2VUT2pDdnA3bVZ3UlQyOE0xeEpueDJONGl0MUpEWFBpeXVGRHZtblU2OWVuYnhncmJ2WmlUeE5uUEtnRUtOMWpKalhtakpQLUE0N3ZSdFYwWU1GSmZrR3pMVTkxSWtaanlvUmk2UElqMnpHdDd1Q0FWbmJxalplMzQzNGRJcWZoRGswWjNUc1B1TE1pQmpNR28?oc=5) ⭐️ 7.0/10

A Minnesota lawyer was suspended after using fabricated case citations generated by AI in legal documents. The incident was reported by MPR News. This case illustrates the risks of AI misuse in legal practice.

google\_news · MPR News · Aug 21, 21:56

**「为什么重要」** The case highlights the potential dangers of using AI-generated content in legal settings without proper verification.

**「可关注」** 可关注：A Minnesota lawyer was suspended for using AI-generated fake case citations.

**Tags**: `#industry`, `#policy`, `#model`

---

<a id="item-ai-daily-3"></a>
### [Moqi Uses Agentic-Native to Reconstruct Robot Embodiment Brain for Long-Term Tasks, Submits to WRC](https://mp.weixin.qq.com/s?__biz=MzA3MzI4MjgzMw==&amp;mid=2651051506&amp;idx=1&amp;sn=d1eb5c88e5a7ebfb2d81c68804684eed) ⭐️ 6.0/10

Moqi has developed Agentic-Native, a method to reconstruct the robot&\#x27;s embodiment brain. This enables continuous execution of long-term tasks, which is more difficult than performing a single action. The method has been submitted to WRC.

rss · 机器之心 · Aug 21, 03:19

**「Why it matters」** Continuous long-term task execution is a key challenge in embodied AI, as highlighted by the difficulty of maintaining tasks over time.

**「Key Takeaway」** Pay attention to: Reconstructing the robot embodiment brain using Agentic-Native for continuous long-term task execution.

**Tags**: `#robotics`, `#embodied-ai`, `#product`, `#industry`

---

<a id="item-ai-daily-4"></a>
### [DeepSense 桌面 AI 系统：AI 跑实验](https://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw==&amp;mid=2247913892&amp;idx=2&amp;sn=cf9d597946f8f0987109569128cf0bc6) ⭐️ 5.0/10

DeepSense Technology 开发了桌面 AI 系统，自动化科学研究的完整工作流程。科学家只需提出问题，AI 负责运行实验。系统让科学家的精力回到科学创造上。

rss · 量子位 · Aug 21, 03:02

**「为什么重要」** 这一系统让科学家专注于创造性工作，而非繁琐的实验操作。

**「可关注」** 可关注：AI 负责跑实验，让科学家时间回到科学创造。

**Tags**: `#product`, `#industry`

---

<a id="item-ai-daily-5"></a>
### [Bohr Science Space: AI Scientists for Scientific Research](https://mp.weixin.qq.com/s?__biz=MzA3MzI4MjgzMw==&amp;mid=2651051506&amp;idx=2&amp;sn=7492c796da65176af0bf9bcce332eae7) ⭐️ 5.0/10

Bohr Science Space is a desktop service. It selects AI scientists from multiple disciplines. The scientists serve scientific research. The service is designed to handle the physical labor of research on the desktop and free up time for scientific creation.

rss · 机器之心 · Aug 21, 03:19

**Tags**: `#product`, `#industry`, `#AI`

---

<a id="item-ai-daily-6"></a>
### [End-to-End Paper Generation System: 92% Fake Conclusion Detection Rate, Auto Experiments, Figures, Drafts](https://mp.weixin.qq.com/s?__biz=MzA3MzI4MjgzMw==&amp;mid=2651051506&amp;idx=3&amp;sn=aa2e1f4dd425cf0a52631efb49e2f182) ⭐️ 5.0/10

An end-to-end system for generating research papers has been developed. It features a 92% fake conclusion detection rate. The system can automatically run experiments, draw figures, and directly output paper drafts.

rss · 机器之心 · Aug 21, 03:19

**Tags**: `#product`, `#industry`, `#model`

---

<a id="item-ai-daily-7"></a>
### [ICML 2026: BEACON Nearly Doubles Long-Range Agent Success Rates](https://mp.weixin.qq.com/s?__biz=MzIwMTc4ODE0Mw==&amp;mid=2247722361&amp;idx=2&amp;sn=5a006b50943113b0c6017e795dbada36) ⭐️ 5.0/10

Zhejiang University’s BEACON method is claimed to nearly double long-range agent success rates. The method assigns credits according to milestones. This is presented at ICML 2026. No original verifiable announcement or major lab details are provided.

rss · PaperWeekly · Aug 21, 14:31

**「可关注」** 可关注：Assign credits according to milestones

**Tags**: `#lab`, `#model`, `#agent`, `#eval`, `#industry`

---

<a id="item-ai-daily-8"></a>
### [Tech Giants Frustrated with AI Slop](https://news.google.com/rss/articles/CBMiakFVX3lxTFBOWjV4Szg4bEFBdlVDNGxjNE5ocy1wMnN1ZkRUMUlkazNTV21NdzhwMGlMT3hsVzBKeXNHOEJoMnB3NERSZ2xYMEFKa25ISF9fRGJvV01hNWc4VExHb19xb0N4WE00YzA1Vnc?oc=5) ⭐️ 5.0/10

The New York Times reports that major tech giants are frustrated with low-quality AI-generated content, often called AI slop. This sentiment is widespread in the industry as companies contend with the volume of poor AI outputs. The article notes the frustration but does not name specific companies, describe new model releases, or mention policy changes.

google\_news · The New York Times · Aug 21, 19:39

**「Why It Matters」** The report captures growing industry-wide concerns about AI content quality and its effects on production and user experience.

**Tags**: `#industry`

---

## AI Deals

<a id="item-ai-deals-1"></a>
### [Epic Games Free Games: Cardpocalypse, Albion Online, Desert Caravan \(Aug 21-27\)](https://www.appinn.com/eggs-26821/) ⭐️ 6.0/10

Epic Games is offering Cardpocalypse, Albion Online, and Desert Caravan as free games from August 21 to 27. Cardpocalypse is a card-building RPG where players collect cards in the 1990s school, challenge classmates, and upgrade cards. Albion Online is an MMORPG, and Desert Caravan is a mobile game. These can be claimed via an Epic account.

rss · 小众软件 · Aug 21, 10:48

**「Why It Matters」** This time-limited promotion allows Epic users to try these games for free, providing good value during the week.

**「What to Watch」** Pay attention to: The games are free only during August 21-27 and require an Epic Games account to claim.

**Tags**: `#promo`, `#limited-free`, `#coupon`

---

<a id="item-ai-deals-2"></a>
### [26/27 Premier League Schedule Calendar Live\!](https://www.appinn.com/26-27-premier-league-calendar/) ⭐️ 5.0/10

The 2026/27 Premier League schedule and score calendar is maintained by 青小蛙. It&\#x27;s free to subscribe to mobile or computer calendar apps, and scores will auto-update after matches. No quota, price, or expiration is mentioned, and it&\#x27;s immediately usable for fans.

rss · 小众软件 · Aug 21, 12:06

**「Why it matters」** The calendar is ready before the 2026/27 Premier League season starts, so fans can subscribe and get automatic updates right away.

**「Takeaway」** Takeaway: Subscribe to the calendar for automatic score updates in your calendar app. It&\#x27;s free and works on both mobile and computer.

**Tags**: `#free`, `#calendar`, `#football`, `#tool`

---