---
layout: default
title: "Horizon Summary: 2026-09-13 (EN)"
date: 2026-09-13
lang: en
---

> From 140 items, 2 important content pieces were selected

---

**Agent Harness Architecture**
1. [Claude Code v2.1.270 发布](#item-harness-arch-1) ⭐️ 5.8/10
2. [Gemini CLI v0.61.0-nightly.20260912.g9c1b0a610 发布](#item-harness-arch-2) ⭐️ 5.8/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [Claude Code v2.1.270 发布](https://github.com/anthropics/claude-code/releases/tag/v2.1.270) ⭐️ 5.8/10

Claude Code v2.1.270 is released. It fixes a regression in v2.1.269 where read-only git commands in Bash unexpectedly requested permissions after a long-running session.

github · ashwin-ant · Sep 12, 19:45

**「改了什么」** Fixed read-only git commands in Bash unexpectedly asking for permission after a session had been running for a while \(regression in 2.1.269\)

**Tags**: `#tools`, `#runtime`, `#sandbox`, `#permissions`

---

<a id="item-harness-arch-2"></a>
### [Gemini CLI v0.61.0-nightly.20260912.g9c1b0a610 发布](https://github.com/google-gemini/gemini-cli/releases/tag/v0.61.0-nightly.20260912.g9c1b0a610) ⭐️ 5.8/10

Gemini CLI v0.61.0-nightly.20260912.g9c1b0a610 is released. It hardens sandbox filesystem isolation and blocks indirect prompt injection via build files and untrusted flags. The changes are in core and sandbox modules. This is a minor nightly bug-fix release without breaking changes.

github · gemini-cli-robot · Sep 12, 01:25

**「设计要点」** Hardens filesystem boundaries and isolates runtime state in the sandbox. Targets agent runtime sandbox and permissions models.

**「改了什么」** Fixes indirect prompt injection via build file modifications and untrusted flags. Hardens filesystem boundaries and isolates runtime state.

**Tags**: `#sandbox`, `#runtime`, `#permissions`

---