---
layout: default
title: "Horizon Summary: 2026-09-13 (ZH)"
date: 2026-09-13
lang: zh
---

> 从 138 条内容中筛选出 2 条重要资讯。

---

**Harness 架构**
1. [pydantic-ai v2.43.0 发布](#item-harness-arch-1) ⭐️ 5.8/10
2. [Gemini CLI v0.61.0-nightly.20260912 发布](#item-harness-arch-2) ⭐️ 5.8/10

---

## Harness 架构

<a id="item-harness-arch-1"></a>
### [pydantic-ai v2.43.0 发布](https://github.com/pydantic/pydantic-ai/releases/tag/v2.43.0) ⭐️ 5.8/10

pydantic-ai v2.43.0 发布。OpenAIChatModel 更新工具调用。新增首次运行横幅。支持 clai 会话。修复文本边界。修正 temporal MCP 检查。

github · DouweM · 9月12日 00:54

**「改了什么」** 新增首次运行横幅并支持 clai 会话。修复 OpenAIChatModel 文本边界并修正 temporal MCP 检查。

**标签**: `#mcp`, `#tools`, `#runtime`

---

<a id="item-harness-arch-2"></a>
### [Gemini CLI v0.61.0-nightly.20260912 发布](https://github.com/google-gemini/gemini-cli/releases/tag/v0.61.0-nightly.20260912.g9c1b0a610) ⭐️ 5.8/10

Google Gemini CLI v0.61.0-nightly.20260912.g9c1b0a610 已发布，包含针对间接提示注入和沙箱隔离的安全修复。
主要通过构建文件修改和不受信任标志来防止间接提示注入，并加固文件系统边界并隔离运行时状态。

github · gemini-cli-robot · 9月12日 01:25

**「改了什么」** 修复了间接提示注入问题，通过构建文件修改和不受信任标志。
加固了沙箱的文件系统边界并隔离运行时状态。

**标签**: `#sandbox`, `#runtime`, `#permissions`

---