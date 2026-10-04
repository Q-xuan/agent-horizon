---
layout: default
title: "Horizon Summary: 2026-10-04 (EN)"
date: 2026-10-04
lang: en
---

> From 139 items, 3 important content pieces were selected

---

**Agent Harness Architecture**
1. [pydantic/pydantic-ai released v2.54.0](#item-harness-arch-1) ⭐️ 6.3/10
2. [Claude Code 2.1.289 发布](#item-harness-arch-2) ⭐️ 6.3/10

**AI Agent Engineer**
1. [ThinkingBox 按数据库终态评估](#item-agent-engineer-1) ⭐️ 8.8/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [pydantic/pydantic-ai released v2.54.0](https://github.com/pydantic/pydantic-ai/releases/tag/v2.54.0) ⭐️ 6.3/10

pydantic-ai v2.54.0 is an official minor release fixing JSON schema edge cases, durable execution constraints, hook lifecycles, and Temporal error handling.

github · dsfaccini · Oct 3, 03:21

**Tags**: `#runtime`, `#tools`, `#eval`

---

<a id="item-harness-arch-2"></a>
### [Claude Code 2.1.289 发布](https://code.claude.com/docs/en/changelog#2-1-289) ⭐️ 6.3/10

Claude Code 发布 2.1.289 补丁，集中修复权限规则、终端渲染与插件加载缺陷。权限侧补齐了复合 shell 命令、环境变量前缀及 symlink 路径下 deny/ask 规则被绕过的问题。渲染侧解决了短代码块中未闭合 &lt;script&gt; 或深层 $\{ 导致终端冻结、文本绘制串行等问题。插件侧修复了升级后 mod 不加载、本地 marketplace 插件副本过期及 --plugin-dir 热重载失效。

rss · Claude Code Changelog · Oct 3, 23:19

**「设计要点」** 权限判定在 sandbox auto-allow 场景下会解析命令前的环境变量赋值与复合命令嵌套，确保 deny/ask 规则穿透用户安装的 mod 审批。终端渲染引擎改为在最终宽度一次性布局高亮视图，并让 mod 的 Client 区域故障隔离，单点绘制失败只抛 ui.fault 而不拖垮整个会话。

**「改了什么」** 2.1.289 回滚了 2.1.288 中可能导致频繁登出的 claude auth status 变更，并新增 agent.spawn 接口与 $.agent.list\(\) 的 idle/waiting 状态。其余为缺陷修复，无破坏性变更。

**Tags**: `#permissions`, `#runtime`, `#tools`, `#sandbox`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [ThinkingBox 按数据库终态评估](https://huggingface.co/blog/microsoft/thinkingbox) ⭐️ 8.8/10

Microsoft 与 Hugging Face 推出 ThinkingBox，在隔离 MCP 工具会话结束后，按终端后端状态与残留副作用评估 Agent。基准含 507 个有状态业务流程，每任务重复 20 次。在 12 个 LLM 模型的 121,680 次有效试验里，79,853 次未通过可执行检查；其中 67.24% 的失败仍干净终止、调用了状态变更工具且未报最终工具错误，错误字段值占 77.61%，多余副作用占 43.30%，缺失必需效果占 25.36%。Claude Opus 5.5 以 67.16% pass@1 领先，Kimi-K3 是最强开放权重模型（57.37%），但仅 13.41% 的任务能在 20 次里全部通过。

rss · Hugging Face Blog · Oct 3, 22:56

**「为什么重要」** 现有评估多看工具调用与最终回复，ThinkingBox 直接检查数据库留下的字段值与副作用，把“说对了”和“做对了”分开。对接触真实业务记录的 Agent，单次通过率无法说明可靠性，20 次重复后仍全对的任务数才是可依赖性的硬指标。

**「可关注」** 可关注：为涉及真实状态变更的 Agent 选型时，pass@1 与 pass@20 会大幅背离，应把 observed 20/20 作为主指标，并重点排查那些干净终止、调用成功但字段值错误的失败轨迹。

**Tags**: `#eval`, `#mcp`, `#observability`, `#harness`

---