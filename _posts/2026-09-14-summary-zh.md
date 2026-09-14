---
layout: default
title: "Horizon Summary: 2026-09-14 (ZH)"
date: 2026-09-14
lang: zh
---

> 从 137 条内容中筛选出 3 条重要资讯。

---

**Harness 架构**
1. [LangChain Academy GitHub trending](#item-harness-arch-1) ⭐️ 5.0/10

**Agent 工程师日报**
1. [shot-scraper 1.12 发布](#item-agent-engineer-1) ⭐️ 5.8/10

**AI 日报**
1. [Perplexity 使用 Astra 实现端到端系统](#item-ai-daily-1) ⭐️ 5.8/10

---

## Harness 架构

<a id="item-harness-arch-1"></a>
### [LangChain Academy GitHub trending](https://github.com/langchain-ai/langchain-academy) ⭐️ 5.0/10

LangChain Academy 仓库在 GitHub trending。该仓库提供了一系列教育笔记本，专注于通过 LangGraph 模块构建代理的基础概念。模块从基本设置到部署，逐步介绍 LangGraph 主题。内容仅为介绍性描述，无发布说明或架构细节。

rss · GitHub Trending Daily · 9月14日 00:36

**标签**: `#runtime`, `#planning`, `#memory`, `#subagents`, `#eval`

---

## Agent 工程师日报

<a id="item-agent-engineer-1"></a>
### [shot-scraper 1.12 发布](https://github.com/simonw/shot-scraper/releases/tag/1.12) ⭐️ 5.8/10

simonw 发布了 shot-scraper 1.12，新增 WebP 支持并提供质量设置。示例：\`shot-scraper http://www.example.com/ -o shot.webp --quality 80\`。WebP 文件大小通常显著小于 JPEG 和 PNG。修复了 WebKit 对本地文件 URI 的处理。

github · simonw · 9月13日 23:58

**「为什么重要」** 此更新对使用 shot-scraper 的 harness 工具链有直接影响。已发生 WebP 支持和 URI 修复，尚未证实对 agent 性能的具体影响。

**「可关注」** 可关注：使用 \`--quality\` 参数设置 WebP 质量以减小文件大小。

**标签**: `#harness`, `#coding-agent`

---

## AI 日报

<a id="item-ai-daily-1"></a>
### [Perplexity 使用 Astra 实现端到端系统](https://openai.com/index/perplexity-improving-accuracy-with-astra) ⭐️ 5.8/10

Perplexity 使用 Astra 编写沟通、修改软件并监控生产系统。与早期模型相比，Perplexity 的检查频率大幅降低。

rss · OpenAI Blog · 9月14日 00:00

**「可关注」** 可关注：Perplexity 使用 Astra 编写沟通、修改软件并监控生产系统，与早期模型相比检查频率大幅降低。

**标签**: `#openai`, `#product`, `#perplexity`, `#astra`, `#industry`

---