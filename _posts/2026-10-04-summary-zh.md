---
layout: default
title: "Horizon Summary: 2026-10-04 (ZH)"
date: 2026-10-04
lang: zh
---

> 从 139 条内容中筛选出 3 条重要资讯。

---

**Harness 架构**
1. [pydantic/pydantic-ai released v2.54.0](#item-harness-arch-1) ⭐️ 6.3/10
2. [Claude Code 2.1.289 发布](#item-harness-arch-2) ⭐️ 6.3/10

**Agent 工程师日报**
1. [ThinkingBox 用后端终态评估 Agent](#item-agent-engineer-1) ⭐️ 8.8/10

---

## Harness 架构

<a id="item-harness-arch-1"></a>
### [pydantic/pydantic-ai released v2.54.0](https://github.com/pydantic/pydantic-ai/releases/tag/v2.54.0) ⭐️ 6.3/10

pydantic-ai v2.54.0 is an official minor release fixing JSON schema edge cases, durable execution constraints, hook lifecycles, and Temporal error handling.

github · dsfaccini · 10月3日 03:21

**标签**: `#runtime`, `#tools`, `#eval`

---

<a id="item-harness-arch-2"></a>
### [Claude Code 2.1.289 发布](https://code.claude.com/docs/en/changelog#2-1-289) ⭐️ 6.3/10

Claude Code 发布 2.1.289 补丁，集中修复权限规则执行、终端渲染与插件/mod 加载缺陷。权限侧收紧复合 shell 命令、环境变量前缀和 symlink 路径下的 deny/ask 规则覆盖，并阻止用户插件改写组织管理的 MCP 登录工具描述。渲染侧修复短代码块中未闭合 \`&lt;script&gt;\` 或深层 \`$\{\` 替换导致的终端与浏览器冻结，以及 mod 绘制失败引发的会话中断。插件侧处理本地 marketplace 缓存、升级后首会话 mod 不加载、\`claude plugin validate\` 误判等问题，并新增 \`agent.spawn\` 与 \`$.agent.list\(\)\` 的 idle/waiting 状态。

rss · Claude Code Changelog · 10月3日 23:19

**「设计要点」** 权限判定在 sandbox auto-allow 下需要解析环境变量前缀与复合命令嵌套，否则 deny/ask 规则会被绕过；mod 运行时通过 \`ui.fault\` 隔离单个 Client 绘制失败，避免拖垮整个会话。

**「改了什么」** 相对 2.1.288，权限执行覆盖了 symlink、环境变量前缀和复合命令嵌套场景；终端渲染修复了未闭合标签、控制字符与右对齐内容溢出；插件系统修复升级后加载、本地 marketplace 缓存与 validate 误判，并回滚了 VSCode 端可能导致频繁登出的 \`claude auth status\` 改动。

**标签**: `#permissions`, `#runtime`, `#tools`, `#sandbox`

---

## Agent 工程师日报

<a id="item-agent-engineer-1"></a>
### [ThinkingBox 用后端终态评估 Agent](https://huggingface.co/blog/microsoft/thinkingbox) ⭐️ 8.8/10

Microsoft 与 Hugging Face 发布 ThinkingBox，在隔离 MCP 工具会话后检查 Agent 留下的后端终态与副作用，覆盖 507 个有状态业务流程，每任务运行 20 次。在 121,680 次有效试验中，79,853 次未通过可执行检查，其中 67.24% 干净终止且无最终工具错误；失败案例中 77.61% 字段值错误、43.30% 有意外额外效果、25.36% 缺少必要效果。框架报告 pass@1、pass@20 与 observed 20/20：Claude Opus 5.5 以 67.16% 的 pass@1 领先，Kimi-K3 是开源最强且 pass@20 达 93.89%，但仅 13.41% 任务能 20 次全过；Claude Opus 5.5 与 Opus 5 的 20/20 任务数同为 241 个。

rss · Hugging Face Blog · 10月3日 22:56

**「为什么重要」** 对读写真实数据库和业务记录的 Agent，“工具调用合法”和“最终回复看起来正确”都不足以证明任务完成。ThinkingBox 把评估锚定在后端可执行断言上，并用 20 次重复区分“能做一次”与“每次都对”。

**「可关注」** 可关注：若 Agent 操作真实记录，评估基线应从“工具调用是否合法”改为“后端终态断言”，并以 20/20 通过率而非单次 pass@1 作为可靠性依据。

**标签**: `#eval`, `#mcp`, `#observability`, `#harness`

---