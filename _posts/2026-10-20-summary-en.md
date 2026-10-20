---
layout: default
title: "Horizon Summary: 2026-10-20 (EN)"
date: 2026-10-20
lang: en
---

> From 157 items, 7 important content pieces were selected

---

**Agent Harness Architecture**
1. [MCP Servers v2.0.0 发布](#item-harness-arch-1) ⭐️ 6.8/10
2. [OpenHands v1.28.0 发布](#item-harness-arch-2) ⭐️ 6.3/10
3. [Cloudflare Cuts Inference Bill 68%](#item-harness-arch-3) ⭐️ 5.8/10
4. [Claude Code 2.1.304 发布](#item-harness-arch-4) ⭐️ 5.5/10
5. [Anthropic Launches Official Claude Code Plugins Directory](#item-harness-arch-5) ⭐️ 5.0/10

**AI Daily**
1. [OpenAI 提升低资源编程语言模型能力](#item-ai-daily-1) ⭐️ 7.8/10
2. [GitHub Copilot 应用会话迁移至 VS Code 教程发布](#item-ai-daily-2) ⭐️ 5.8/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [MCP Servers v2.0.0 发布](https://github.com/modelcontextprotocol/servers/releases/tag/v2.0.0) ⭐️ 6.8/10

modelcontextprotocol/servers 发布 v2.0.0。全部服务器重构以支持 modern era MCP 规约，同时保持对 legacy era 客户端的兼容。TypeScript 服务器迁移至 TS SDK v2，Node 运行版本下限提升至 24。Python 服务器（mcp-server-fetch、mcp-server-git、mcp-server-time）改用 MCP Python SDK 高级 MCPServer 构建，调整错误返回格式，time 服务器工具新增 outputSchema 与 structuredContent。

github · cliffhall · Oct 19, 06:46

**「设计要点」** 服务器运行时层保留双规约时代兼容逻辑，modern era 服务器可直接响应 legacy era 客户端请求。TypeScript 服务器统一依赖 Node &gt;=24，Python 服务器则接入 MCP Python SDK 高级抽象层。

**「改了什么」** TypeScript 服务器完成 TS SDK v2 迁移，Node 版本下限提升至 24。Python 服务器切换至 MCP Python SDK 高级 MCPServer，未知工具调用从 isError 结果改为返回 JSON-RPC -32602 错误，time 服务器工具补充 outputSchema 与 structuredContent 字段。全部服务器现在均声明 prompts 与 resources 能力，且 listChanged 为 false。

**Tags**: `#mcp`, `#tools`, `#runtime`

---

<a id="item-harness-arch-2"></a>
### [OpenHands v1.28.0 发布](https://github.com/OpenHands/OpenHands/releases/tag/v1.28.0) ⭐️ 6.3/10

OpenHands v1.28.0 was released on 2026-10-19. This minor release introduces two capabilities relevant to agent harnesses: an inline secret request flow where agents can ask for secrets via an in-conversation modal, and adoption of a shared known-bug contract for repeatable evaluation verification. The remainder consists of UI fixes, theme readability improvements, automation refinements, and addition of the Bahasa Indonesia locale. No breaking changes or major architectural shifts are included.

github · openhands-release-bot\[bot\] · Oct 19, 14:29

**「改了什么」** Relative to v1.27.x, the release adds the inline secret request modal for agents and the shared known-bug contract for harness verification. It also adds Bahasa Indonesia \(id\) locale, smooth reading-pace streaming with word fade-in in chat, and hides overlapping automation templates on self-hosted instances. Bug fixes focus on theme readability, keyboard accessibility, automation draft handling, and cloud sandbox resume behavior.

**「评论」** No community comments are available for this release.

**Tags**: `#permissions`, `#eval`

---

<a id="item-harness-arch-3"></a>
### [Cloudflare Cuts Inference Bill 68%](https://blog.cloudflare.com/obsessive-inference-optimization/) ⭐️ 5.8/10

Cloudflare optimized their multi-agent AI code review system, cutting average inference cost per review by 68% \(from $2.46 to $0.77\) and median latency from 4m09s to 1m32s. The coordinator pattern with specialist reviewers and risk tiers stayed unchanged. About 40% of savings came from code optimizations; the rest from model and effort experimentation. Key technical moves: splitting the system prompt to enable cross-repository prefix caching on Anthropic&\#x27;s cache, reducing LLM calls per session, and migrating to OpenCode v2.

rss · Cloudflare AI · Oct 19, 19:12

**「Architecture」** The system uses a coordinator agent dispatching to specialist reviewers, with review intensity decided by risk tiers. The reviewer runs on OpenCode v2, a ground-up rewrite of v1. Anthropic&\#x27;s prompt cache is critical: prefix caching requires cache breakpoints at shared boundaries. The harness was modified to split the OpenCode v1 system block so the shared agent prompt gets its own breakpoint, enabling cross-repository cache hits. Cloudflare is also experimenting with running the reviewer solely on Durable Objects using pi-durable.

**「What Changed」** Since the April baseline, the main changes were: 1\) Splitting the OpenCode v1 system prompt to place a cache breakpoint after the shared agent prompt, enabling cross-repository prefix caching and raising cache hit rates from 85.7% to 97%. 2\) Moving the Codex reviewer&\#x27;s reference index into its prompt, cutting its LLM calls per run from 15.9 to 9.6 and cost from $1.12 to $0.72. 3\) Removing inaccessible tools from sub-reviewers to eliminate wasted calls and reduce tool definitions by ~2.9k tokens. 4\) Parallelizing file reads up to 150 KB. 5\) Skipping reviewers on re-reviews when nothing changed. 6\) Migrating from OpenCode v1 to v2, which agreed on 98% of merge requests and finished full-tier reviews 13% faster.

**「Community」** No community comments available.

**Tags**: `#runtime`, `#tools`, `#planning`

---

<a id="item-harness-arch-4"></a>
### [Claude Code 2.1.304 发布](https://github.com/anthropics/claude-code/releases/tag/v2.1.304) ⭐️ 5.5/10

Claude Code 2.1.304 发布，核心改进集中在 mod 权限模型与工具调用检测。新增 \`decider: &quot;person&quot;\` 字段强制仅通过人工权限对话框或主机回调批准工具请求，拒绝时使用 mod 提供的理由；\`tool.check\` 事件新增 \`e.isReadOnly\` 布尔值标识只读操作。新增 \`/auto-mode-setup\` 引导式环境配置命令（支持 Bedrock、Vertex、Foundry 及 telemetry-disabled 会话）和 \`/claude-api managed-agents-secure\` 安全审计命令，后者对照 Anthropic 安全指南检查托管代理配置且不修改设置。Pro 与 Max 计划恢复闲置对话时，若消耗超过 5 小时限额的显著份额将弹出警告。

github · ashwin-ant · Oct 19, 21:34

**「设计要点」** mod 权限层通过 \`decider\` 字段分离人工决策路径与自动批准路径，\`isReadOnly\` 为工具拦截提供只读语义。转录压缩摘要现在包含历史工具名称，增强长会话的可追溯性。

**「改了什么」** 本版本新增 mod 人工专属决策权限与只读工具检测接口；新增自动模式环境引导和托管代理安全审计两条命令；修复插件钩子跳过时转录日志缺失、mod 重载失败导致工具丢失、sandbox 文件系统 glob 中非字符类括号解析错误、挂载卷删除缺少安全提示等多项问题。

**Tags**: `#permissions`, `#tools`, `#sandbox`, `#memory`, `#subagents`

---

<a id="item-harness-arch-5"></a>
### [Anthropic Launches Official Claude Code Plugins Directory](https://github.com/anthropics/claude-plugins-official) ⭐️ 5.0/10

Anthropic launched an official curated directory of high-quality plugins for the Claude Code agent harness. The directory lists third-party plugins but includes a disclaimer that Anthropic does not verify their safety, functionality, or MCP server contents. Engineers should trust a plugin before installing it. The source provides no technical implementation details or runtime changes for Claude Code itself.

rss · GitHub Trending Daily · Oct 20, 01:27

**Tags**: `#tools`, `#mcp`, `#ecosystem`

---

## AI Daily

<a id="item-ai-daily-1"></a>
### [OpenAI 提升低资源编程语言模型能力](https://openai.com/index/low-resource-programming-languages) ⭐️ 7.8/10

OpenAI 发布博客文章，宣布改进 ChatGPT 在低资源编程语言上的表现。文章介绍新推出的软件工程评估基准，以及 SQLite 和 COBOL 迁移任务相关工作。目前未披露具体性能数字或上线时间。

rss · OpenAI Blog · Oct 19, 12:00

**「可关注」** 可关注：OpenAI 将低资源语言纳入模型评估范围，后续可跟踪 SQLite 与 COBOL 迁移任务的基准结果。

**Tags**: `#model`, `#lab`, `#eval`, `#industry`

---

<a id="item-ai-daily-2"></a>
### [GitHub Copilot 应用会话迁移至 VS Code 教程发布](https://github.blog/ai-and-ml/github-copilot/how-to-continue-a-github-copilot-app-session-in-vs-code/) ⭐️ 5.8/10

GitHub 官方博客发布操作教程，讲解如何将 GitHub Copilot 应用中的代理会话无缝迁移至 VS Code。迁移过程可保留原有对话记录、代码变更及工作上下文，无需用户手动重建上下文。

rss · GitHub Blog · Oct 19, 18:47

**「为什么重要」** 该教程为同时使用 GitHub Copilot 应用与 VS Code 的开发者提供跨端会话 continuity 的操作路径，降低切换工具时的上下文丢失成本。

**「可关注」** 可关注：GitHub Copilot 应用与 VS Code 已支持会话迁移，可保留对话、代码变更及工作上下文。

**Tags**: `#product`, `#lab`

---