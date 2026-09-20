---
layout: default
title: "Horizon Summary: 2026-09-20 (ZH)"
date: 2026-09-20
lang: zh
---

> 从 161 条内容中筛选出 8 条重要资讯。

---

**Harness 架构**
1. [pydantic-ai v2.46.0 发布](#item-harness-arch-1) ⭐️ 7.8/10
2. [Claude Code 2.1.278](#item-harness-arch-2) ⭐️ 7.3/10
3. [Gemini CLI v0.62.0](#item-harness-arch-3) ⭐️ 6.3/10
4. [Agent Lightning v1.0](#item-harness-arch-4) ⭐️ 5.5/10
5. [Anthropic 知识插件仓库](#item-harness-arch-5) ⭐️ 5.0/10

**Agent 工程师日报**
1. [halogen 0.12.0 长上下文提速](#item-agent-engineer-1) ⭐️ 6.0/10

**AI 羊毛**
1. [Kuvu AI UGC 视频免费一个月](#item-ai-deals-1) ⭐️ 7.0/10
2. [HTTPS Capture 终身限免](#item-ai-deals-2) ⭐️ 5.0/10

---

## Harness 架构

<a id="item-harness-arch-1"></a>
### [pydantic-ai v2.46.0 发布](https://github.com/pydantic/pydantic-ai/releases/tag/v2.46.0) ⭐️ 7.8/10

pydantic-ai v2.46.0 强化工具参数与结构化输出处理。TypeSafeModel 可自动填充工具参数，也能先选择联合输出类型；ModelProfile 新增 supports\_text\_output，支持 LLMJudge 和 GEval 处理不支持文本输出的模型。TemporalDurability 新增 Workflow Streams 事件主题，RealtimeSession 新增 wait\_for\_playback\(\)，用于等待语音播放完成。

github · DouweM · 9月19日 03:51

**「设计要点」** 工具层新增运行时参数补全、联合类型选择、Choices 选项描述和布尔阈值配置，并拒绝超过选择器能力的选项数量。运行时增加 Workflow Streams 事件转发与 RealtimeSession 播放同步；评测层用 ModelProfile 显式声明文本输出能力。

**「改了什么」** 相较 v2.45.0，本版把 TypeSafeModel 从单纯类型约束扩展到工具参数填充和联合输出选择，并补充了 Enum 文档与 Choices 辅助器。Realtime 工具失败、工具调用与语音响应归属、Bedrock 自适应思考与强制工具选择、实时会话计费等问题得到修复。

**标签**: `#tools`, `#eval`, `#runtime`, `#planning`

---

<a id="item-harness-arch-2"></a>
### [Claude Code 2.1.278](https://code.claude.com/docs/en/changelog#2-1-278) ⭐️ 7.3/10

Claude Code 将 auto mode 默认切到服务端分类器，支持范围内不收取分类器开销；若回退到计费路径，会发出告警。\`/status\` 新增 \`Auto mode server\`，显示本次会话的分类器是否运行在服务端。

rss · Claude Code Changelog · 9月19日 03:19

**「设计要点」** 服务端分类器覆盖 Claude API、Enterprise，以及 Bedrock、Vertex、Foundry 和 gateways。Bedrock、Vertex、Foundry 和 gateways 可用 \`CLAUDE\_CODE\_AUTO\_MODE\_SERVER=0\` 退出服务端路径；\`/status\` 补充分类器位置可观测性。

**「改了什么」** auto mode 的默认分类位置改为服务端，并增加计费回退告警。\`/status\` 增加 \`Auto mode server\` 状态行。

**标签**: `#runtime`, `#tools`, `#observability`, `#billing`

---

<a id="item-harness-arch-3"></a>
### [Gemini CLI v0.62.0](https://github.com/google-gemini/gemini-cli/releases/tag/v0.62.0-nightly.20260919.gcfbcaa8df) ⭐️ 6.3/10

Gemini CLI 发布 v0.62.0-nightly.20260919.gcfbcaa8df。版本聚焦 Windows ConPTY 进程退出、PTY 输出收尾、终端缓冲区内存管理和请求取消日志，修复运行时稳定性问题。

github · gemini-cli-robot · 9月19日 01:25

**「设计要点」** 改动集中在终端工具链运行时：同步 ConPTY 进程退出生命周期，强化 PTY 输出终结流程，并改善终端缓冲区内存管理。请求取消时抑制未捕获 AbortError 日志，减少正常取消造成的噪声。

**「改了什么」** 相对上一 nightly 版本，新增 Windows PTY 生命周期同步与输出收尾修复，补强终端内存管理和 Windows 诊断路径格式化；同时修复请求取消日志、VS Code diff 标签关闭后的终端焦点，以及认证错误文档链接。

**标签**: `#runtime`, `#tools`, `#memory`

---

<a id="item-harness-arch-4"></a>
### [Agent Lightning v1.0](https://github.com/microsoft/agent-lightning) ⭐️ 5.5/10

GitHub Trending 收录了 Microsoft 的 Agent Lightning，一个面向 agentic reinforcement learning 的轻量框架。项目称代码规模约 3,500 行，支持让 agent 通过真实 harness 与模型交互；v1.0 已完成重构，旧版本另见 legacy 分支。

rss · GitHub Trending Daily · 9月20日 00:33

**「设计要点」** 现有材料明确的设计重点是把真实 agent harness 接入训练流程，并以约 3,500 行代码控制实现规模。RSS 摘要未提供运行时、工具层、记忆、权限或评测细节。

**标签**: `#runtime`, `#tools`, `#eval`, `#planning`

---

<a id="item-harness-arch-5"></a>
### [Anthropic 知识插件仓库](https://github.com/anthropics/knowledge-work-plugins) ⭐️ 5.0/10

GitHub Trending 收录了 Anthropic 的 knowledge-work-plugins 开源仓库。仓库提供面向知识工作的 Claude 插件集合，把 Claude 定制成适配角色、团队和公司的专业助手。插件面向 Claude Cowork，也兼容 Claude Code；现有材料未提供具体运行时、权限模型或实现路径。

rss · GitHub Trending Daily · 9月20日 00:33

**「设计要点」** 插件可注入角色规范、工具与数据源、关键工作流和 slash commands，形成面向任务的工作流扩展层。仓库简介未说明插件加载、执行隔离、数据访问控制和状态管理方式。

**标签**: `#tools`, `#planning`, `#runtime`

---

## Agent 工程师日报

<a id="item-agent-engineer-1"></a>
### [halogen 0.12.0 长上下文提速](https://www.reddit.com/r/LocalLLaMA/comments/1wkyny9/qwen38flashnext_at_1m_context_on_strix_halo_38/) ⭐️ 6.0/10

9 月 19 日，社区作者报告 halogen 0.12.0 在 Ryzen AI Max+ 395、128 GB 内存上运行 Qwen3.8-Flash-Next，将 1,004,581 tokens 上下文的解码速度从 0.11.10 的 27.3 提升到 38.3 tok/s。冷 prefill 从 21.2 分钟降至 17.9 分钟，吞吐从 790 提升到 937 tok/s；这些数据来自同机、同会话、同提示词的对比。1M 配置每档只有一次冷请求，结果由作者自报，且需要 128 GB 主机，尚未证明能推广到其他硬件或工作负载。

reddit · r/LocalLLaMA · /u/peonist-ai · 9月19日 21:49

**「为什么重要」** 这为本地 coding agent 的百万上下文服务提供了一个明确的版本基线：长上下文冷路径出现了可测变化，但 32k 标准十提示词均值未变，影响范围仍需更多复测确认。

**「可关注」** 可关注：评估长上下文推理时，应分开记录冷 prefill、缓存命中和 decode；该测试中 1M 缓存命中请求约 0.55 秒出首 token，不能与冷路径耗时直接比较。

**标签**: `#coding-agent`, `#memory`, `#observability`, `#performance`

---

## AI 羊毛

<a id="item-ai-deals-1"></a>
### [Kuvu AI UGC 视频免费一个月](https://kuvu.ai/marketing/ai-ugc) ⭐️ 7.0/10

Kuvu 推出 AI UGC 视频生成器，提供一个月免费使用。材料未说明领取条件、功能额度、地区限制、到期规则和具体截止日期。

rss · HN Free API / Credits · 9月19日 13:55

**「可关注」** 可关注：适合想试用 AI UGC 视频生成器的用户，但使用前需确认额度、领取条件和到期后的收费规则。

**标签**: `#promo`, `#limited-free`, `#free-tier`

---

<a id="item-ai-deals-2"></a>
### [HTTPS Capture 终身限免](https://www.appinn.com/https-capture-for-apple/) ⭐️ 5.0/10

HTTPS Capture 面向 iPhone、iPad 和 Mac，提供抓包、HTTPS 解密与 API 调试。App Store 部分地区现可终身限免，但中国区未上架，无法直接获取。材料未给出具体限免截止时间、领取条件或官方领取页。

rss · 小众软件 · 9月19日 06:06

**「为什么重要」** 如果你使用 Apple 设备调试接口，这个工具支持局域网抓包、URL 重写、Mock、Hosts、断点调试、WebSocket 和 JS 脚本。中国区用户暂时无法直接获取。

**「可关注」** 可关注：适合需要在 iPhone、iPad 或 Mac 上做 HTTPS 抓包与 API 调试的用户；中国区不可直接领取，具体限制也尚未披露。

**标签**: `#limited-free`, `#api`, `#promo`

---