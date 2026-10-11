---
layout: default
title: "Horizon Summary: 2026-10-11 (ZH)"
date: 2026-10-11
lang: zh
---

> 从 141 条内容中筛选出 2 条重要资讯。

<nav id="ah-toc" class="ah-toc" aria-label="目录"><span class="ah-toc-title">目录</span><ul><li><a href="#sec-harness-arch"><span class="ah-toc-name">Harness 架构</span><span class="ah-toc-count">2条</span></a></li></ul></nav>

---

**[Harness 架构](#sec-harness-arch)**
1. [Anthropic 开源 knowledge-work-plugins](#item-harness-arch-1) ⭐️ 5.5/10
2. [OpenCode v1.19.0 发布](#item-harness-arch-2) ⭐️ 5.3/10

---

## Harness 架构
{: #sec-harness-arch .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-harness-arch" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-harness-arch-1"></a>
### [Anthropic 开源 knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) ⭐️ 5.5/10

Anthropic 开源 knowledge-work-plugins 插件仓库。该项目主要面向 Claude Cowork，同时向下兼容 Claude Code。仓库提供按团队角色定制的扩展包，允许定义工作流偏好、数据源检索工具和专属 slash 命令。

rss · GitHub Trending Daily · 10月11日 02:01

**「设计要点」** 插件统一抽象了 Claude Cowork 与 Claude Code 的交互规范，把角色提示词、工具接入点与斜杠指令封装为可复用的配置单元。

**标签**: `#tools`, `#runtime`, `#planning`

---

<a id="item-harness-arch-2"></a>
### [OpenCode v1.19.0 发布](https://github.com/anomalyco/opencode/releases/tag/v1.19.0) ⭐️ 5.3/10

OpenCode 发布 v1.19.0。新版本提供升级至 OpenCode 2 的命令入口，TUI 停止静默自动安装更新，改由 \`/update\` 显式触发。运行时支持 OpenAI \`ultrafast\` 服务层，并在检查终端实例存在前前置收紧 PTY 连接凭证校验。

github · opencode-agent\[bot\] · 10月11日 01:39

**「设计要点」** 调整 PTY 会话接入流程：在检查 PTY 实例是否存在之前，强制先验证连接来源（origins）和 ticket 凭证，避免未授权请求探测系统内 PTY 会话状态。

**「改了什么」** CLI 新增 \`opencode upgrade --major\` 用于升级到大版本 OpenCode 2；TUI 改为用 \`/update\` 手动更新；放行 OpenAI \`ultrafast\` 服务层参数。

**标签**: `#runtime`, `#permissions`, `#tools`

---