---
layout: default
title: "Horizon Summary: 2026-10-11 (EN)"
date: 2026-10-11
lang: en
---

> From 141 items, 2 important content pieces were selected

---

**Agent Harness Architecture**
1. [Anthropic knowledge-work-plugins Released](#item-harness-arch-1) ⭐️ 5.5/10
2. [OpenCode v1.19.0 Released](#item-harness-arch-2) ⭐️ 5.3/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [Anthropic knowledge-work-plugins Released](https://github.com/anthropics/knowledge-work-plugins) ⭐️ 5.5/10

Anthropic open-sourced knowledge-work-plugins, a plugin repository built for Claude Cowork and compatible with Claude Code. The plugins configure Claude for specialized roles and teams by defining how tasks are executed. Configurations specify which tools and data sources to query, how to manage critical workflows, and available slash commands.

rss · GitHub Trending Daily · Oct 11, 02:01

**Tags**: `#tools`, `#runtime`, `#planning`

---

<a id="item-harness-arch-2"></a>
### [OpenCode v1.19.0 Released](https://github.com/anomalyco/opencode/releases/tag/v1.19.0) ⭐️ 5.3/10

OpenCode released v1.19.0, introducing migration commands for the upcoming OpenCode 2 transition and removing automatic update installations in favor of explicit user triggers. The core CLI adds \`opencode upgrade --major\`, while the TUI exposes the \`/update\` command. The release also enables the OpenAI \`ultrafast\` service tier and tightens PTY connection security.

github · opencode-agent\[bot\] · Oct 11, 01:39

**「Architecture Note」** Hardened PTY runtime connection handling by validating incoming connection origins and authentication tickets before checking whether target PTY instances exist.

**「What Changed」** Added \`opencode upgrade --major\` and TUI \`/update\` commands to handle OpenCode 2 upgrades while disabling background auto-updates. Enabled the OpenAI \`ultrafast\` service tier.

**Tags**: `#runtime`, `#permissions`, `#tools`

---