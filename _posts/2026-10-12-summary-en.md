---
layout: default
title: "Horizon Summary: 2026-10-12 (EN)"
date: 2026-10-12
lang: en
---

> From 135 items, 4 important content pieces were selected

---

**Agent Harness Architecture**
1. [modelcontextprotocol/servers v1.0.0 Released](#item-harness-arch-1) ⭐️ 7.3/10
2. [Anthropic knowledge-work-plugins](#item-harness-arch-2) ⭐️ 5.0/10

**AI Agent Engineer**
1. [ProgramGym 提出长程程序复现训练环境](#item-agent-engineer-1) ⭐️ 6.0/10
2. [RSI-Anything 递归自我改进框架](#item-agent-engineer-2) ⭐️ 5.5/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [modelcontextprotocol/servers v1.0.0 Released](https://github.com/modelcontextprotocol/servers/releases/tag/v1.0.0) ⭐️ 7.3/10

modelcontextprotocol/servers released v1.0.0, marking the first stable release for core reference implementations including @modelcontextprotocol/server-filesystem, server-memory, server-everything, and server-sequential-thinking. The release stabilizes root lifecycle management, session cleanup across HTTP and SSE transports, and data integrity safeguards. Python packages \(mcp-server-fetch, mcp-server-git, mcp-server-time\) were concurrently published under calendar version 2026.10.10.

github · cliffhall · Oct 11, 02:40

**「Architecture Note」** server-filesystem introduces a root refresh barrier that blocks tool execution until initial directories are verified and properly revokes unauthorized roots. server-memory serializes graph mutations to eliminate concurrent write races during JSONL persistence and rejects dangling relations on disk loading.

**「What Changed」** server-filesystem explicitly declares JSON Schema 2020-12 across all tools, preserves indentation and line endings in edit\_file, and resolves Unicode normalization differences alongside UNC paths. server-everything cleans up subscriptions on session disconnect, isolates async tasks to client boundaries, and reports port binding collisions instead of false-positive startup messages.

**Tags**: `#mcp`, `#tools`, `#memory`, `#runtime`

---

<a id="item-harness-arch-2"></a>
### [Anthropic knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) ⭐️ 5.0/10

Anthropic open-sourced the \`knowledge-work-plugins\` repository, introducing role- and workflow-specific plugin support for Claude Cowork and Claude Code. The plugins define task procedures, integrated tools, data sources, and slash commands to adapt Claude to specialized knowledge work. The repository provides high-level workflow configurations and prompt packages rather than agent harness runtime or sandbox infrastructure.

rss · GitHub Trending Daily · Oct 12, 01:59

**Tags**: `#tools`, `#planning`, `#subagents`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [ProgramGym 提出长程程序复现训练环境](https://huggingface.co/papers/2610.13395) ⭐️ 6.0/10

研究人员提出 ProgramGym 框架，由 Program-Env 与 Program-Agent 两部分组成，专为长程程序复现任务设计。现有 coding agent 训练环境多聚焦于 issue 修复或给定需求文档生成代码，缺少让 agent 自主探索参考代码、推导需求并完成系统设计的可验证训练场景。该框架尝试直接基于已有代码仓库构建可验证环境，支持 agent 在实际编码前展开探索。

rss · Hugging Face Daily Papers · Oct 12, 00:00

**「为什么重要」** 多数评测与强化学习环境仍局限于修补局部 issue，无法覆盖软件工程中从零复现系统的长程规划需求。若能通过代码仓库规模化构建验证闭环，将有助于拓展 coding agent 在架构设计层面的能力评估。

**「可关注」** 可关注：在搭建代码生成 harness 时，如何把参考项目探索与自动化校验结合，支持更长周期的开发工作流训练。

**Tags**: `#coding-agent`, `#harness`, `#eval`

---

<a id="item-agent-engineer-2"></a>
### [RSI-Anything 递归自我改进框架](https://huggingface.co/papers/2610.13912) ⭐️ 5.5/10

研究提出通用递归自我改进框架 RSI-Anything，基于 JEPA-Anything 构建预测世界模型来指导动作与训练数据筛选。系统依赖观测反馈驱动策略优化和条件式世界模型自适应，并通过兼容性检查决定更新组件的留存。在代码修复任务中，固定生成模型时，任务成功率从静态验证器的 26.3% 提升至预测选择的 29.2%，并在世界模型自适应后达到 31.2%；目前公开材料存在文本截断，对实际 Agent 工程的落地效果仍有待验证。

rss · Hugging Face Daily Papers · Oct 12, 00:00

**「为什么重要」** 该研究尝试在昂贵外部反馈受限时，用预测世界模型替代人工或环境真值进行数据自选。代码修复场景已验证单点成功率提升，但泛化至复杂软件工程工作流的稳定性尚未证实。

**「可关注」** 可关注：在固定代码模型的前提下，引入预测性选择与自适应世界模型可将修复率从 26.3% 提至 31.2%，可评估在无外监督测试环境下用预测模型做数据过滤的可行性。

**Tags**: `#coding-agent`, `#orchestration`, `#eval`

---