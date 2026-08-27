---
layout: default
title: "Horizon Summary: 2026-08-27 (EN)"
date: 2026-08-27
lang: en
---

> From 132 items, 11 important content pieces were selected

---

**Agent Harness Architecture**
1. [Cline SDK v0.0.81](#item-harness-arch-1) ⭐️ 7.5/10
2. [mastra/core 1.62.0 Release](#item-harness-arch-2) ⭐️ 7.5/10
3. [Codex rust-v0.150.0 发布](#item-harness-arch-3) ⭐️ 6.5/10
4. [Cline SDK v0.0.80 发布](#item-harness-arch-4) ⭐️ 6.5/10
5. [google/adk-python v2.8.0 发布](#item-harness-arch-5) ⭐️ 6.5/10
6. [Claude Code v2.1.247 发布](#item-harness-arch-6) ⭐️ 5.5/10
7. [Cline v4.1.16 Released](#item-harness-arch-7) ⭐️ 5.5/10

**AI Agent Engineer**
1. [Gemini 3.5 Transcribe Released](#item-agent-engineer-1) ⭐️ 5.5/10
2. [Dolma adapted for Thai Mangosteen corpus](#item-agent-engineer-2) ⭐️ 5.5/10

**AI Daily**
1. [OpenAI Expands ChatGPT for Teachers to 55 U.S. School Districts](#item-ai-daily-1) ⭐️ 8.5/10
2. [OpenAI报告：AI让学习永不止步](#item-ai-daily-2) ⭐️ 6.5/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [Cline SDK v0.0.81](https://github.com/cline/cline/releases/tag/sdk/sdk/v0.0.81) ⭐️ 7.5/10

Cline SDK v0.0.81 optimizes session event payloads by separating state snapshots from conversation transcripts, reducing memory usage in large tasks. Session snapshot events no longer carry the full conversation transcript. Snapshots are now state-only \(status, usage, model, workspace, checkpoint\); transcripts are fetched with the \`session.messages\` command.

github · github-actions\[bot\] · Aug 26, 09:38

**「设计要点」** Session events now use state-only snapshots to reduce memory footprint in large tasks. Full transcripts are fetched on-demand via the new \`session.messages\` command.

**「改了什么」** Session snapshot events no longer embed the full conversation transcript, preventing memory bloat in multi-megabyte tasks. Transcripts are now fetched separately using the \`session.messages\` command.

**Tags**: `#memory`, `#runtime`, `#protocol`

---

<a id="item-harness-arch-2"></a>
### [mastra/core 1.62.0 Release](https://github.com/mastra-ai/mastra/releases/tag/%40mastra/core%401.62.0) ⭐️ 7.5/10

mastra/core 1.62.0 adds ElasticsearchStore and Valkey/GLIDE-backed storage for memory, workflow snapshots, scores, and semantic recall from a single cluster. It introduces computer-use sandboxes with E2B and Daytona providers that support screenshots, mouse, and keyboard control. Sandboxes now own their runtime environment via MastraSandbox constructor and getEnv/setEnv methods, with safer shutdowns and improved observability for in-progress traces.

github · PaulieScanlon · Aug 26, 13:40

**「Design notes」** Sandboxes own their runtime environment through the MastraSandbox constructor option and getEnv/setEnv methods. This environment merges into every process spawn by the base SandboxProcessManager, reaching executeCommand on any provider without VM-level changes.

**「What changed」** New storage backends and computer-use sandbox capabilities were added, along with runtime environment control for sandboxes and observability upgrades including in-progress traces.

**Tags**: `#sandbox`, `#memory`, `#runtime`, `#tools`

---

<a id="item-harness-arch-3"></a>
### [Codex rust-v0.150.0 发布](https://github.com/openai/codex/releases/tag/rust-v0.150.0) ⭐️ 6.5/10

Codex rust-v0.150.0 release from OpenAI adds @-task referencing so agents can read, create, or message other tasks from the terminal. It introduces permission shortcuts to cycle modes and new Interrupt hooks for commands and MCP handlers. Additional updates include auto-titles for unnamed terminal tasks and picker for /copy responses. Fixes address untrusted projects and various runtime issues.

github · github-actions\[bot\] · Aug 26, 19:37

**「设计要点」** Key design points include updates to the permissions model with deny-read rules and cycling modes, new Interrupt hooks in the runtime for commands and MCP, and task referencing in the terminal UI.

**「改了什么」** Relative to rust-v0.149.0, this release adds @-task referencing and permission cycling shortcuts. It implements Interrupt hooks and changes untrusted project handling by ignoring project-level AGENTS.md instructions.

**Tags**: `#permissions`, `#runtime`, `#mcp`, `#tools`, `#interrupt`

---

<a id="item-harness-arch-4"></a>
### [Cline SDK v0.0.80 发布](https://github.com/cline/cline/releases/tag/sdk/sdk/v0.0.80) ⭐️ 6.5/10

Cline SDK v0.0.80 has been released. It includes runtime fixes for file-writing tools using native line endings and preventing crashes in search\_codebase on large files. Tool enhancements cover MCP server installation and tasks scheduling configuration. The model catalog was refreshed with seven new providers and updated defaults.

github · github-actions\[bot\] · Aug 26, 08:45

**「改了什么」** This release updates file-writing to use platform native line endings, fixes search\_codebase crashes on enormous lines, redacts git credentials from prompts, marks Claude Code as subscription-billed, improves installMcpServer argument parsing, adds scheduled-only mode to tasks, and refreshes the model catalog with new providers and changed defaults.

**Tags**: `#runtime`, `#tools`, `#mcp`, `#planning`, `#providers`

---

<a id="item-harness-arch-5"></a>
### [google/adk-python v2.8.0 发布](https://github.com/google/adk-python/releases/tag/v2.8.0) ⭐️ 6.5/10

Google ADK Python v2.8.0 release adds native task mode support to RemoteA2aAgent, data agent tools, LLM call limit configuration, and Model Armor guardrail integration. Additional updates include Vertex AI API version support, streaming tools scheduling, telemetry enhancements, and various bug fixes.

github · wukath · Aug 26, 23:25

**「改了什么」** Adds native task mode support in RemoteA2aAgent, new data\_agent tools for create/delete/update/list, ADK\_MAX\_LLM\_CALLS environment variable, Model Armor guardrail plugin, nvidia nim integration sample, and skill state injection support.

**Tags**: `#runtime`, `#tools`, `#guardrails`, `#task-mode`, `#data-agents`

---

<a id="item-harness-arch-6"></a>
### [Claude Code v2.1.247 发布](https://github.com/anthropics/claude-code/releases/tag/v2.1.247) ⭐️ 5.5/10

Claude Code v2.1.247 is released. The release introduces the SendFeedback tool, allowing Claude to draft feedback reports for review and sending from /feedback \(turn off with the feedbackDrafts setting\). It adds support for custom spinner tips through spinnerTipsOverride with new entries like id, text, cooldownSessions, priority, tipsFile, and label. A new /claude-api cost-optimize command is added to profile existing project API spend and optimize levers like caching and token hygiene. The /claude-api skill is updated with admin API coverage for organization members, invites, workspaces, API keys, rate limit reports, workload identity federation, and CMEK. Multiple bug fixes address sub-agent model 404 handling, keyboard shortcuts, Bash sandbox cleanup, session stability, and other issues.

github · ashwin-ant · Aug 26, 23:06

**「改了什么」** This release adds the SendFeedback tool and the /claude-api cost-optimize command. It updates the /claude-api skill with admin features and includes minor config changes like spinnerTipsOverride support and Bash permission prompt improvements.

**Tags**: `#tools`, `#permissions`

---

<a id="item-harness-arch-7"></a>
### [Cline v4.1.16 Released](https://github.com/cline/cline/releases/tag/v4.1.16) ⭐️ 5.5/10

Cline v4.1.16 fixes hook workspace handling by resolving from the active VS Code window instead of global state in ~/.cline. This resolves discovery and state issues for hooks in multi-window scenarios. Additional fixes address subscription provider billing display, git credential redaction in workspace metadata, native line endings for new files, and other runtime improvements.

github · github-actions\[bot\] · Aug 26, 08:42

**「设计要点」** Hooks now resolve their workspace from the active VS Code window context rather than shared global state. This is a runtime change affecting sub-agent/hook discovery and state in multi-window VS Code setups.

**「改了什么」** The per-tool MCP auto-approve checkboxes are hidden. MCP auto-approval is now governed solely by the global &\#x27;Use MCP servers&\#x27; toggle.

**Tags**: `#runtime`, `#memory`, `#hooks`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [Gemini 3.5 Transcribe Released](https://deepmind.google/blog/intelligent-transcription-with-gemini-3-5-transcribe/) ⭐️ 5.5/10

Google DeepMind announces Gemini 3.5 Transcribe for more intelligent speech-to-text transcription. The announcement states that this feature is now available. This is based on the official DeepMind blog post.

rss · Google DeepMind · Aug 26, 17:01

**「Why it matters」** The announcement of Gemini 3.5 Transcribe is a change that has occurred. Its potential impact on AI agent development involving audio is not yet confirmed in the supplied material.

**「What to watch」** What to watch: Gemini 3.5 Transcribe for more intelligent speech-to-text transcription.

**Tags**: `#orchestration`, `#coding-agent`, `#eval`

---

<a id="item-agent-engineer-2"></a>
### [Dolma adapted for Thai Mangosteen corpus](https://allenai.org/blog/thai-llm-dolma) ⭐️ 5.5/10

Thai researchers adapted Ai2’s open Dolma toolkit to build Mangosteen, a 47-billion-token Thai corpus. Allen AI’s blog says the pipeline filters low-quality web data while maintaining or improving model performance and strengthening Thai cultural knowledge. The item does not name the teams, methods, models, evals, or dates behind those claims.

rss · Allen AI · Aug 26, 08:00

**「Why it matters」** This is an official note that Dolma is being reused for a language-specific web corpus with quality filtering. Performance and cultural-knowledge gains are asserted in the blog, not evidenced with numbers here, and no change to agent harnesses is described.

**「Worth watching」** Dolma is being adapted as a filter-and-pack pipeline for a 47-billion-token Thai corpus rather than only scaling raw web text; this write-up does not show effects on coding-agent evals or toolchains.

**Tags**: `#eval`, `#orchestration`, `#coding-agent`

---

## AI Daily

<a id="item-ai-daily-1"></a>
### [OpenAI Expands ChatGPT for Teachers to 55 U.S. School Districts](https://openai.com/index/bringing-chatgpt-for-teachers-to-more-us-school-districts) ⭐️ 8.5/10

OpenAI is expanding ChatGPT for Teachers to 55 additional U.S. school districts. This brings secure AI tools, training, and support to over 100,000 more educators and staff. The initiative provides safe AI assistance in educational settings.

rss · OpenAI Blog · Aug 26, 10:00

**「Why It Matters」** This expansion increases access to secure AI tools for a large number of educators across the U.S.

**「Key Takeaway」** Key Takeaway: OpenAI is expanding ChatGPT for Teachers to 55 U.S. school districts, delivering secure AI tools, training, and support to over 100,000 more educators and staff.

**Tags**: `#openai`, `#chatgpt`, `#education`, `#product`, `#policy`

---

<a id="item-ai-daily-2"></a>
### [OpenAI报告：AI让学习永不止步](https://openai.com/index/learning-never-stops) ⭐️ 6.5/10

OpenAI发布了一份新报告。报告探讨了学生和教育工作者如何使用ChatGPT来支持持续学习，超出课堂范围。

rss · OpenAI Blog · Aug 26, 10:00

**「可关注」** 可关注：学生和教育工作者如何使用ChatGPT来支持持续学习，超出课堂范围。

**Tags**: `#openai`, `#chatgpt`, `#education`, `#industry`, `#product`

---