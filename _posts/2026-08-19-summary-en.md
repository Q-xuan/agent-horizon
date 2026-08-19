---
layout: default
title: "Horizon Summary: 2026-08-19 (EN)"
date: 2026-08-19
lang: en
---

> From 101 items, 4 important content pieces were selected

---

**Agent Harness Architecture**
1. [openai/codex rust-v0.148.0](#item-harness-arch-1) ⭐️ 7.0/10
2. [cloudflare/agents released @cloudflare/voice@0.3.6](#item-harness-arch-2) ⭐️ 7.0/10
3. [Cloudflare Agents @cloudflare/ai-chat 0.10.2](#item-harness-arch-3) ⭐️ 7.0/10

**AI Agent Engineer**
1. [Agent Memory Dose Calibration by Model Tier](#item-agent-engineer-1) ⭐️ 7.0/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [openai/codex rust-v0.148.0](https://github.com/openai/codex/releases/tag/rust-v0.148.0) ⭐️ 7.0/10

OpenAI released Codex TUI rust-v0.148.0. This update adds session fork/restore with archiving, asynchronous MCP tool hooks, Markdown conversation export, and Amazon Bedrock Runtime provider support. Key enhancements include improved session management, async tool invocation, and multi-LLM compatibility in the TUI.

github · github-actions\[bot\] · Aug 18, 22:26

**「What Changed」** Relative to rust-v0.147.0, this release adds session forking with archive/restore via the resume picker, asynchronous command hooks that invoke MCP tools, and Markdown export of complete TUI conversations. It also introduces Amazon Bedrock as a built-in LLM provider with AWS profile and region configuration.

**Tags**: `#runtime`, `#tools`, `#memory`, `#mcp`

---

<a id="item-harness-arch-2"></a>
### [cloudflare/agents released @cloudflare/voice@0.3.6](https://github.com/cloudflare/agents/releases/tag/%40cloudflare/voice%400.3.6) ⭐️ 7.0/10

Cloudflare Agents released @cloudflare/voice@0.3.6. This patch release updates VoiceTurnContext to treat messages as pre-transcript history for both text and audio turns, with guidance on onTurn\(\) prompt construction to avoid duplicate user messages. It also passes the full keyterms array to Workers AI Flux and Nova-3 STT and preserves spacing between streamed text segments separated by tool calls. The package requires agents &gt;=0.20.2, and when installing @cloudflare/think@0.16.0 or @cloudflare/voice@0.3.6 requires agents@0.21.0.

github · github-actions\[bot\] · Aug 18, 09:08

**「Architecture Note」** The update focuses on runtime memory handling in VoiceTurnContext, defining messages as completed history before the current transcript to improve context management for voice interactions.

**「What Changed」** This release defines VoiceTurnContext.messages as completed history before the current transcript for text and audio turns, preventing duplicate user messages. Existing onTurn\(\) implementations must append the transcript exactly once if passing context.messages directly to the LLM.

**Tags**: `#runtime`, `#memory`, `#voice`

---

<a id="item-harness-arch-3"></a>
### [Cloudflare Agents @cloudflare/ai-chat 0.10.2](https://github.com/cloudflare/agents/releases/tag/%40cloudflare/ai-chat%400.10.2) ⭐️ 7.0/10

Cloudflare agents ai-chat 0.10.2 is a patch release for the @cloudflare/ai-chat package. It documents observer error handling as terminal responses and exposes framework-neutral transport. The release treats useAgentChat observer error frames as terminal responses, clearing observer streaming, replay, recovery, and tool-continuation state even when they omit &\#x27;done&\#x27;. It also accepts AI SDK flexible schemas in agentTool while removing Zod as a peer requirement.

github · github-actions\[bot\] · Aug 18, 09:08

**「What Changed」** This patch release changes error-frame treatment in useAgentChat to be terminal responses with state clearing, exposes WebSocketChatTransport from the framework-neutral agents/chat/transport entry point, and accepts flexible schemas in agentTool without requiring Zod as a peer dependency.

**Tags**: `#runtime`, `#transport`, `#error-handling`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [Agent Memory Dose Calibration by Model Tier](https://huggingface.co/blog/ibm-research/altk-evolve-hmm) ⭐️ 7.0/10

ALTK-Evolve enables agents to distill reusable behavioral guidelines from their own past trajectories without weight updates or human annotation. Evaluation across eight models on the AppWorld benchmark \(585 multi-step tasks\) identified three patterns: strong models with headroom benefit from the full guideline set, weaker models perform best with curated retrieval, and saturated models show no measurable gains. gpt-oss-120b gained +16.1 percentage points task goal completion with curated retrieval at +5% token overhead, while DeepSeek-V3.2 gained +9.5pp with the full set.

rss · Hugging Face Blog · Aug 18, 18:09

**「Why It Matters」** The findings show that optimal agent memory dose depends on model capability rather than a fixed approach, directly informing memory design and evaluation workflows for self-improving agents. This calibration method was observed to improve performance across tested models without retraining.

**「Engineer Takeaway」** Attention: Calibrate memory dose to model tier and benchmark headroom, not parameter count.

**Tags**: `#memory`, `#eval`, `#orchestration`, `#coding-agent`, `#retrieval`

---