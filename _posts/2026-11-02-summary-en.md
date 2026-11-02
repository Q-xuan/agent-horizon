---
layout: default
title: "Horizon Summary: 2026-11-02 (EN)"
date: 2026-11-02
lang: en
---

> From 145 items, 2 important content pieces were selected

---

**Agent Harness Architecture**
1. [FastMCP v4.2.0a2 发布](#item-harness-arch-1) ⭐️ 7.8/10
2. [crewAI 1.15.34 发布](#item-harness-arch-2) ⭐️ 5.3/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [FastMCP v4.2.0a2 发布](https://github.com/PrefectHQ/fastmcp/releases/tag/v4.2.0a2) ⭐️ 7.8/10

FastMCP v4.2.0a2 ships as an alpha prerelease of the MCP protocol implementation. It enforces breaking behavior changes: JSON Schema \`const\` and \`enum\` now compare by JSON equality, \`prompts/get\` returns \`-32602\` invalid params for missing arguments, OpenAPI upstream errors truncate to 1 KB with HTML bodies dropped, and strict input validation rejects undeclared OpenAPI arguments. Kept-alive stdio transports respect each client&\#x27;s timeout and restart idle subprocesses when a later client with a different timeout connects. Skills support remains experimental; the build validates against pydantic-ai, langchain, agno, Microsoft Agent Framework, and OpenAI Agents SDK for integration testing only.

github · zzstoatzz · Nov 1, 22:58

**「设计要点」** Runtime layer isolates kept-alive stdio subprocesses per client timeout, restarting idle transports when timeout settings change. Skills system uses storage-neutral \`Skill\` objects with folder-based loaders and proxy-aware discovery through mounted servers, while Prefab renderer shares resources across equivalent tools and rebinds pre-4.2 backend addresses through 4.2 proxies.

**「改了什么」** Since v4.2.0a1, JSON Schema \`const\` and \`enum\` validation switched to JSON equality, \`prompts/get\` missing arguments return \`-32602\`, OpenAPI errors truncate to 1 KB without HTML, and strict mode rejects undeclared OpenAPI arguments. Kept-alive stdio transports now enforce per-client timeouts and restart idle subprocesses, while skills discovery extends through proxies with bounded backend pagination and \`list\_skills\` renames to \`list\_skill\_summaries\`.

**Tags**: `#mcp`, `#tools`, `#runtime`

---

<a id="item-harness-arch-2"></a>
### [crewAI 1.15.34 发布](https://github.com/crewAIInc/crewAI/releases/tag/1.15.34) ⭐️ 5.3/10

crewAI 1.15.34 发布。新增 LiteLLM 目录、组织 skill 搜索、\`crewai deploy create --zip\`、planning 配置文档及 \`crewai run --inputs\` 传递。修复工具调用停止计数、空 LLM 回答重试、工具调用代理结构化输出、上下文窗口 honoring、LiteLLM 流式错误保留原始异常、登录拒绝重试等 20 余项问题。文档化移除 1.15.29 agent executor。

github · joaomdmoura · Nov 1, 21:21

**「设计要点」** 变更日志未附实现细节、PR 链接或代码路径，无法评估架构影响。改动覆盖运行时（上下文窗口、工具调用）、工具层（LiteLLM 集成、部署）和规划组件。

**「改了什么」** 新增独立 LiteLLM 目录、组织级 skill 搜索、zip 部署及 planning 配置文档。修复重复工具调用停止计数、空 LLM 回答单次重试并抛出类型化错误、工具调用代理完成时请求结构化输出、上下文窗口大小 honoring 与 fallback 告警、LiteLLM 流式错误保留提供方异常、AMP 登录拒绝后重试、Python 3.12 深层嵌套 JSON 在 TUI 中保持文本等。Breaking change：移除 1.15.29 agent executor 并提供迁移笔记。

**「评论」** 无社区评论。

**Tags**: `#runtime`, `#tools`, `#planning`

---