---
layout: default
title: "Horizon Summary: 2026-09-13 (ZH)"
date: 2026-09-13
lang: zh
---

> 从 140 条内容中筛选出 2 条重要资讯。

---

**Harness 架构**
1. [Claude Code v2.1.270 发布](#item-harness-arch-1) ⭐️ 5.8/10
2. [gemini-cli v0.61.0-nightly.20260912.g9c1b0a610 发布](#item-harness-arch-2) ⭐️ 5.8/10

---

## Harness 架构

<a id="item-harness-arch-1"></a>
### [Claude Code v2.1.270 发布](https://github.com/anthropics/claude-code/releases/tag/v2.1.270) ⭐️ 5.8/10

这是 Anthropic 的 Claude Code v2.1.270 版本发布。修复了 v2.1.269 中 Bash 只读 git 命令在长时间运行会话后意外请求权限的回归问题。

github · ashwin-ant · 9月12日 19:45

**「改了什么」** 修复了 Bash 中只读 git 命令在长时间运行会话后意外请求权限的回归问题。

**标签**: `#tools`, `#runtime`, `#sandbox`, `#permissions`

---

<a id="item-harness-arch-2"></a>
### [gemini-cli v0.61.0-nightly.20260912.g9c1b0a610 发布](https://github.com/google-gemini/gemini-cli/releases/tag/v0.61.0-nightly.20260912.g9c1b0a610) ⭐️ 5.8/10

gemini-cli v0.61.0-nightly.20260912.g9c1b0a610 发布。修复了通过构建文件修改和不受信任标志进行间接提示注入的漏洞。加强了文件系统边界和运行时状态隔离。

github · gemini-cli-robot · 9月12日 01:25

**「改了什么」** 相比上一版，修复了通过构建文件修改和不受信任标志进行间接提示注入的漏洞，并加强了文件系统边界和运行时状态隔离。

**标签**: `#sandbox`, `#runtime`, `#permissions`

---