---
layout: default
title: "Horizon Summary: 2026-09-20 (ZH)"
date: 2026-09-20
lang: zh
---

> 从 159 条内容中筛选出 8 条重要资讯。

---

**Harness 架构**
1. [PydanticAI v2.46.0 发布](#item-harness-arch-1) ⭐️ 7.8/10
2. [Claude Code 2.1.278 发布](#item-harness-arch-2) ⭐️ 7.3/10
3. [Agent Lightning v1.0](#item-harness-arch-3) ⭐️ 5.5/10
4. [Claude Code GitHub 热榜](#item-harness-arch-4) ⭐️ 5.2/10

**Agent 工程师日报**
1. [halogen 0.12.0 提升 1M 解码](#item-agent-engineer-1) ⭐️ 7.3/10
2. [Datasette Explain 0.2.2 支持只读查询](#item-agent-engineer-2) ⭐️ 6.3/10

**AI 羊毛**
1. [HTTPS Capture 终身限免](#item-ai-deals-1) ⭐️ 6.0/10
2. [Kuvu AI UGC 视频免费 1 个月](#item-ai-deals-2) ⭐️ 6.0/10

---

## Harness 架构

<a id="item-harness-arch-1"></a>
### [PydanticAI v2.46.0 发布](https://github.com/pydantic/pydantic-ai/releases/tag/v2.46.0) ⭐️ 7.8/10

PydanticAI v2.46.0 强化了类型安全工具调用与输出选择。TypeSafeModel 可填写可由 Jev 表达的工具参数，也可先选择 union 成员再生成输出；LLMJudge 和 GEval 可运行在不支持文本输出的模型上。RealtimeSession 新增 wait\_for\_playback\(\)，TemporalDurability 新增 event\_stream\_topic，可经 Workflow Streams 转发 agent 事件。

github · DouweM · 9月19日 03:51

**「设计要点」** 工具层把参数填充、union 类型选择和选项数量约束交给 TypeSafeModel，并用 ModelProfile.supports\_text\_output 描述评测模型能力。RealtimeSession 补齐播放完成同步、工具失败记录、语音与工具调用合并及会话计费；TemporalDurability 则提供 Workflow Streams 事件出口。

**「改了什么」** 相较 v2.45.0，本版新增类型化工具参数填充、union 输出选择、运行时 Choices 选项和 typesafe\_boolean\_threshold。评测、RealtimeSession 与 Temporal 工作流也补上了模型能力兼容、播放等待、会话成本统计和 agent 事件流能力。

**标签**: `#runtime`, `#tools`, `#eval`, `#planning`

---

<a id="item-harness-arch-2"></a>
### [Claude Code 2.1.278 发布](https://code.claude.com/docs/en/changelog#2-1-278) ⭐️ 7.3/10

Claude Code 2.1.278 调整 auto mode：Claude API、Enterprise，以及 Bedrock、Vertex、Foundry 和 gateways 默认使用服务端分类器。服务端分类器不收取分类器开销；若回退到计费路径，系统会发出告警。\`CLAUDE\_CODE\_AUTO\_MODE\_SERVER=0\` 可在 Bedrock、Vertex、Foundry 和 gateways 上退出该默认设置，\`/status\` 新增 \`Auto mode server\` 行显示当前会话是否使用服务端分类器。

rss · Claude Code Changelog · 9月19日 03:19

**「设计要点」** \`auto mode\` 的分类器位置成为运行时状态，可通过 \`/status\` 查看当前会话是否走服务端。服务端路径免收分类器开销，回退到计费分类器时发出告警；Bedrock、Vertex、Foundry 和 gateways 可用环境变量关闭默认服务端路径。

**「改了什么」** Claude API 和 Enterprise 用户，以及 Bedrock、Vertex、Foundry、gateways，改为默认使用服务端分类器；Bedrock 等路径仍可用 \`CLAUDE\_CODE\_AUTO\_MODE\_SERVER=0\` 退出。新增计费回退告警和 \`/status\` 的 \`Auto mode server\` 状态行。

**标签**: `#runtime`, `#tools`, `#observability`

---

<a id="item-harness-arch-3"></a>
### [Agent Lightning v1.0](https://github.com/microsoft/agent-lightning) ⭐️ 5.5/10

microsoft/agent-lightning 是一个面向真实 agent harness 的轻量级 agentic RL 训练框架，代码规模约 3,500 行。项目说明 v1.0 已完全重构，早于 v1.0 的版本放在独立分支；当前材料没有给出具体接口或运行限制。

rss · GitHub Trending Daily · 9月20日 02:06

**「设计要点」** 项目以真实 agent harness 作为训练对象，强调用约 3,500 行代码保持实现轻量。现有材料未交代运行时、工具接口、权限边界或评测方法。

**标签**: `#runtime`, `#planning`, `#tools`

---

<a id="item-harness-arch-4"></a>
### [Claude Code GitHub 热榜](https://github.com/anthropics/claude-code) ⭐️ 5.2/10

GitHub Trending 收录 anthropics/claude-code。Claude Code 是运行在终端中的 coding agent，能理解代码库，执行例行任务、解释复杂代码，并处理 Git 工作流。该条目只有产品定位和文档链接，未提供版本、实现路径或具体限制。

rss · GitHub Trending Daily · 9月20日 02:06

**「设计要点」** 材料确认终端是主要运行入口，用户用自然语言驱动代码库理解、任务执行和 Git 操作。未披露运行时组件、工具接口、记忆机制、权限模型或评测方法。

**标签**: `#runtime`, `#tools`, `#planning`

---

## Agent 工程师日报

<a id="item-agent-engineer-1"></a>
### [halogen 0.12.0 提升 1M 解码](https://www.reddit.com/r/LocalLLaMA/comments/1wkyny9/qwen38flashnext_at_1m_context_on_strix_halo_38/) ⭐️ 7.3/10

Reddit 作者报告，halogen 0.12.0 在 Ryzen AI Max+ 395（128 GB）上运行 Qwen3.8-Flash-Next 时，1,004,581 tokens 冷请求解码从 0.11.10 的 27.3 提升到 38.3 tok/s；258,794 tokens 从 42.9 提升到 45.0 tok/s。1M 冷 prefilling 从 21.2 分钟缩至 17.9 分钟，吞吐从 790 提升到 937 tok/s；1M 配置需设置 \`HALOGEN\_ROPE\_YARN=4\` 和 \`HALOGEN\_CTX=1048576\`，并使用 128 GB 机器。1M 数据各仅来自一次冷请求，结果为作者自报，仍需按仓库说明复核。

reddit · r/LocalLLaMA · /u/peonist-ai · 9月19日 21:49

**「为什么重要」** 这为本地长上下文推理工具链提供了具体的 1M 配置实测，但证据只覆盖单台机器和冷路径。32k 标准十提示均值未变，1M 缓存后续 turn 的首 token 约需 0.55 秒，因此这些结果尚不能代表其他硬件或工作负载。

**「可关注」** 可关注：长上下文基准应分开记录冷 prefilling、缓存命中后的首 token 与 decode；本次 32k 均值未变，1M 单次冷测却出现了不同幅度的变化。

**标签**: `#harness`, `#long-context`, `#observability`, `#coding-agent`

---

<a id="item-agent-engineer-2"></a>
### [Datasette Explain 0.2.2 支持只读查询](https://github.com/simonw/datasette-explain/releases/tag/0.2.2) ⭐️ 6.3/10

Datasette Explain 于 2026 年 9 月 20 日发布 0.2.2。该版本让只读 stored-query 页面也支持 explain plan，补上这类页面的 SQL 执行计划查看能力。改动直接服务 SQL 调试与可观测性；材料未说明它对 coding agent、harness 或 evals 有更广影响。

github · simonw · 9月20日 00:22

**「为什么重要」** 只读 stored-query 页面现在可以直接查看执行计划，调试路径少一个页面能力缺口。当前材料只支持这一项窄范围的可用性改进，尚无性能或更广架构影响的证据。

**「可关注」** 可关注：explain plan 的可用范围已覆盖只读 stored-query 页面，但这次发布没有扩展到 agent 架构、harness 或 evals。

**标签**: `#observability`, `#debugging`, `#tooling`, `#datasette`

---

## AI 羊毛

<a id="item-ai-deals-1"></a>
### [HTTPS Capture 终身限免](https://www.appinn.com/https-capture-for-apple/) ⭐️ 6.0/10

HTTPS Capture 目前在非国区 App Store 提供终身限免，支持 iPhone、iPad 和 Mac。它可用于 HTTPS 解密、局域网抓包、API 调试，也支持 URL 重写、JS 脚本、Mock、Hosts、断点调试和 WebSocket。应用未上架国区，活动有效性和具体领取状态需以 App Store 页面为准；材料未提供截止时间。

rss · 小众软件 · 9月19日 06:06

**「为什么重要」** 需要在 Apple 设备上做网络测试或 API 调试的人，可关注这款终身限免工具。它覆盖抓包、解密、Mock 和断点调试等常用能力，但地区限制会影响领取。

**「可关注」** 可关注：适合在 Apple 设备上做 HTTPS 抓包、解密和 API 调试；应用未上架国区，领取前需确认 App Store 地区与活动状态。

**标签**: `#limited-free`, `#promo`, `#api`

---

<a id="item-ai-deals-2"></a>
### [Kuvu AI UGC 视频免费 1 个月](https://kuvu.ai/marketing/ai-ugc) ⭐️ 6.0/10

Kuvu 提供 AI UGC 视频生成器 1 个月免费使用。帖子未说明领取步骤、具体额度、地区限制、绑卡要求或截止时间。

rss · HN Free API / Credits · 9月19日 13:55

**「为什么重要」** 这是一个明确写明免费 1 个月的限时促销，适合近期想试用 AI UGC 视频生成的用户。

**「可关注」** 可关注：适合需要快速试用 AI UGC 视频生成的用户，但领取前需确认额度、使用限制和注册要求。

**标签**: `#promo`, `#limited-free`, `#free-tier`

---