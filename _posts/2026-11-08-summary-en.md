---
layout: default
title: "Horizon Summary: 2026-11-08 (EN)"
date: 2026-11-08
lang: en
---

> From 158 items, 6 important content pieces were selected

---

**Agent Harness Architecture**
1. [Agent Framework 1.25.0](#item-harness-arch-1) ⭐️ 7.8/10
2. [Cloudflare security-audit-skill 发布](#item-harness-arch-2) ⭐️ 5.0/10

**AI Agent Engineer**
1. [Anthropic 发布 Memory 研究](#item-agent-engineer-1) ⭐️ 7.0/10
2. [Claude Code 本地设置泄露密码](#item-agent-engineer-2) ⭐️ 6.0/10

**AI Deals**
1. [RenderPixels Offers 50 Free MCP AI Image Generations](#item-ai-deals-1) ⭐️ 7.0/10
2. [Certadomain 免费域名安全检测上线](#item-ai-deals-2) ⭐️ 6.0/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [Agent Framework 1.25.0](https://github.com/microsoft/agent-framework/releases/tag/python-1.25.0) ⭐️ 7.8/10

Microsoft Agent Framework Python 1.25.0 正式发布。新增可调用 MCP 发现审批策略，支持 Foundry Toolbox 审批元数据，提供工具名/只读过滤、调用方覆盖及保留工具策略刷新。同步引入多项破坏性变更：最低 Python 版本升至 3.11，MCP 发现限制每目录 100 页/1000 项，工作流执行器绑定单一授权域，OpenTelemetry 跨度重命名对齐 GenAI 规范，MCP 协议会话改为每次调用新建。

github · eavanvalkenburg · Nov 7, 15:52

**「设计要点」** 运行时要求 Python 3.11+，移除 3.10 兼容分支。权限控制新增可调用 MCP 发现审批策略，支持工具名/只读过滤、调用方显式覆盖及策略刷新。安全边界收紧：工作流执行器与会话绑定单一授权域，拒绝跨域执行；Hyperlight 沙箱默认脱敏异常详情；MCP 工具处理器每次调用新建协议会话，禁止跨工作流状态共享。观测层将工作流调用跨度重命名为 gen\_ai.operation.name == &quot;invoke\_workflow&quot; 并调整属性名。

**「改了什么」** 新增可调用 MCP 发现审批策略及 Foundry Toolbox 审批元数据支持。破坏性变更：要求 Python 3.11+；MCP 发现默认限制 100 页/1000 项，框架默认请求超时 30 秒；工作流执行器与会话绑定单一授权域，AG-UI 端点拒绝 WorkflowAgent.as\_tool\(\)；OpenTelemetry 跨度命名对齐 GenAI 约定；MCP 工具处理器每次调用新建协议会话，废弃 cache\_max\_size；Foundry Local 迁移至 SDK 2.3.1；Hyperlight 默认脱敏异常详情。

**Tags**: `#mcp`, `#permissions`, `#tools`

---

<a id="item-harness-arch-2"></a>
### [Cloudflare security-audit-skill 发布](https://github.com/cloudflare/security-audit-skill) ⭐️ 5.0/10

Cloudflare open-sourced security-audit-skill, a coding-agent skill that orchestrates isolated subagents for multi-phase security audits. It covers reconnaissance, coverage-led hunting, candidate validation, structured output, independent record verification, and target-neutral reporting. The skill seeded Cloudflare&\#x27;s internal vulnerability discovery harness. No implementation details, version numbers, or interface specifications appear in the source.

rss · GitHub Trending Daily · Nov 8, 02:38

**「改了什么」** Initial open-source release. No prior version exists for comparison.

**Tags**: `#subagents`, `#sandbox`, `#tools`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [Anthropic 发布 Memory 研究](https://www.anthropic.com/research/components-of-agent-memory) ⭐️ 7.0/10

Anthropic 于 2026-11-07 发布研究 &quot;The Components of Agent Memory&quot;，引发 HN 技术讨论。讨论聚焦当前 coding agent harness（Claude Code、Cursor）的记忆管理痛点：跨项目记忆缺失、自动记忆产生过多且仅对单次任务有用、记忆膨胀。社区反馈显示，项目级记忆限制是主要障碍，跨项目会话转录比 harness 内置记忆更实用；另有用户指出自动记忆 95% 可删除，并引用文中图 10 质疑 &quot;dreaming&quot; 机制相比 wiki+search 的边际收益。

hackernews · geoffbp · Nov 7, 06:39 · [Discussion](https://news.ycombinator.com/item?id=50402212)

**「为什么重要」** 研究公开了 agent 记忆组件的设计框架，社区讨论立即转向生产环境中的跨项目记忆缺失与记忆膨胀问题。这表明记忆架构的学术定义与 harness 实际可用性之间存在可验证的落差，涉及使用 Claude Code、Cursor 及类似工具的开发者。

**「可关注」** 可关注：社区反馈显示自动记忆 95% 可删除，且跨项目记忆缺失是比记忆容量更突出的实际障碍，当前 harness 记忆系统在项目边界与检索范围上存在张力。

**「评论」** 社区共识指向当前 harness 记忆系统的实用性不足，尤其是跨项目记忆缺失和自动记忆膨胀；分歧在于是否应通过外部记忆组件弥补模型权重无法持续学习的限制（如 Opus 5.5 的权重固定问题），以及 &quot;dreaming&quot; 机制相比 wiki+search 的成本收益。

**Tags**: `#memory`, `#harness`, `#coding-agent`, `#observability`

---

<a id="item-agent-engineer-2"></a>
### [Claude Code 本地设置泄露密码](https://apiiro.com/blog/coding-agents-leaking-secrets-github-dont-ask-again) ⭐️ 6.0/10

2026-11-07，第三方安全机构报告称 Claude Code 的本地设置文件 \`.claude/settings.local.json\` 中持久化的 &quot;don&\#x27;t ask again&quot; 审批记录包含密钥或密码，且该文件已被提交至 1,122 个公开 GitHub 仓库。Claude Code 团队回应称该文件本应保持本地，Claude 创建时会自动加入 \`.gitignore\`，但涉事文件为用户手动创建并提交；团队正考虑增加密钥清理功能。研究标题夸大了直接因果关系，实际泄露路径要求用户手动提交包含敏感信息的本地设置。

hackernews · shmulc · Nov 7, 20:45 · [Discussion](https://news.ycombinator.com/item?id=50407882)

**「为什么重要」** 这暴露了 coding agent 的本地权限持久化设计与源代码管理流程之间的安全边界：agent 为减少重复询问而保存的审批记录若含敏感输入，且被意外纳入版本控制，即形成可被扫描的泄露面。目前仅观察到第三方研究结果与团队非官方回应，尚无证据表明 Claude Code 主动外传数据。

**「可关注」** 可关注：agent 本地持久化的审批或记忆文件若可能承载敏感输入，应在设计上默认排除出版本控制，并优先考虑自动清理或脱敏，而非仅依赖文档提醒用户手动规避。

**「评论」** 社区共识认为标题夸大其词：仅按下 &quot;Don&\#x27;t Ask Again&quot; 不会直接导致密码泄露，实际泄露需要用户手动提交包含敏感命令的本地设置到公开仓库。部分用户分享通过临时 VM 配合 API 代理限制 agent 权限，或使用密码管理器 CLI 隔离凭证的实践。

**Tags**: `#coding-agent`, `#permissions`, `#memory`

---

## AI Deals

<a id="item-ai-deals-1"></a>
### [RenderPixels Offers 50 Free MCP AI Image Generations](https://renderpixels.com/) ⭐️ 7.0/10

HN user vivgui launched RenderPixels, a tool that supports generating images from any AI model via MCP. It currently offers 50 free render credits, with no public disclosure of expiration date, region restrictions, or claim requirements as of the announcement.

rss · HN Free API / Credits · Nov 8, 01:12

**「为什么重要」** It provides a low-barrier trial option for developers testing MCP-based AI image generation integration, removing upfront cost for initial use, though the lack of disclosed usage rules means offer terms may be adjusted later.

**「可关注」** 可关注：RenderPixels supports calling multiple AI models for image generation via the MCP protocol, and the 50 free credits can be used for lightweight integration testing, but no expiration date, region restriction or other official usage rules have been announced yet.

**Tags**: `#credits`, `#promo`, `#limited-free`, `#api`

---

<a id="item-ai-deals-2"></a>
### [Certadomain 免费域名安全检测上线](https://certadomain.com/en/index.html) ⭐️ 6.0/10

Hacker News 用户 ytkoka 通过 Show HN 帖子发布 Certadomain 免费域名安全检测服务，可提供 DMARC 校验、子域名接管检测、相似域名检查三类能力；当前公开材料未披露具体调用额度、使用限制及服务截止时间。

rss · HN Free API / Credits · Nov 7, 14:47

**「为什么重要」** 域名安全场景中，DMARC 配置校验、子域名接管排查、相似域名监测都是高频需求，多数同类工具需付费或仅提供单次检测，该服务免费开放可降低个人开发者及小团队的安全排查成本。

**「可关注」** 可关注：该服务当前免费开放，但未公开调用配额、服务有效期及使用限制，使用前建议先查阅官方说明确认规则。

**Tags**: `#free-tier`, `#promo`, `#limited-free`

---