---
layout: default
title: "Horizon Summary: 2026-09-13 (EN)"
date: 2026-09-13
lang: en
---

> From 138 items, 2 important content pieces were selected

---

**Agent Harness Architecture**
1. [pydantic-ai v2.43.0 released](#item-harness-arch-1) ⭐️ 5.8/10
2. [Gemini CLI v0.61.0-nightly.20260912.g9c1b0a610 released](#item-harness-arch-2) ⭐️ 5.8/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [pydantic-ai v2.43.0 released](https://github.com/pydantic/pydantic-ai/releases/tag/v2.43.0) ⭐️ 5.8/10

pydantic-ai v2.43.0 released. Small updates to OpenAIChatModel tool call handling and temporal MCP integration. Preserves text part boundaries after tool calls in OpenAIChatModel. Fixes key tool opt-out checks on operation kind, not an MCP import.

github · DouweM · Sep 12, 00:54

**「改了什么」** Added first-run banner describing the run and opening clai sessions with it. Preserved text part boundaries after tool calls in OpenAIChatModel. Fixed key tool opt-out checks on operation kind, not an MCP import.

**Tags**: `#mcp`, `#tools`, `#runtime`

---

<a id="item-harness-arch-2"></a>
### [Gemini CLI v0.61.0-nightly.20260912.g9c1b0a610 released](https://github.com/google-gemini/gemini-cli/releases/tag/v0.61.0-nightly.20260912.g9c1b0a610) ⭐️ 5.8/10

Gemini CLI v0.61.0-nightly.20260912.g9c1b0a610 released. Core fix prevents indirect prompt injection via build file modifications and untrusted flags. Sandbox fix hardens filesystem boundaries and isolates runtime state.

github · gemini-cli-robot · Sep 12, 01:25

**「Design notes」** Sandbox hardens filesystem boundaries and isolates runtime state. Build uses untrusted flags to prevent indirect prompt injection.

**「What changed」** Fixed indirect prompt injection prevention by build file modifications and untrusted flags. Hardened sandbox filesystem boundaries and isolated runtime state.

**Tags**: `#sandbox`, `#runtime`, `#permissions`

---