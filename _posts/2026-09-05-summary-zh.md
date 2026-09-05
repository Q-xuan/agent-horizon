---
layout: default
title: "Horizon Summary: 2026-09-05 (ZH)"
date: 2026-09-05
lang: zh
---

> 从 158 条内容中筛选出 12 条重要资讯。

---

**Harness 架构**
1. [mastra-ai/mastra @mastra/core@1.64.0 发布](#item-harness-arch-1) ⭐️ 8.8/10
2. [browser-use 0.13.10 发布](#item-harness-arch-2) ⭐️ 7.8/10
3. [Claude Code v2.1.261 发布](#item-harness-arch-3) ⭐️ 6.8/10
4. [pydantic-ai v2.40.0 发布](#item-harness-arch-4) ⭐️ 6.8/10
5. [pydantic-ai v2.39.0 发布](#item-harness-arch-5) ⭐️ 6.8/10
6. [Gemini CLI v0.60.0-nightly.20260904.g87a9c71d5 发布](#item-harness-arch-6) ⭐️ 6.8/10
7. [crewAI 1.15.19 发布](#item-harness-arch-7) ⭐️ 5.8/10
8. [anthropics/skills 发布](#item-harness-arch-8) ⭐️ 5.0/10

**Agent 工程师日报**
1. [Anthropic AI 形式化费马大定理](#item-agent-engineer-1) ⭐️ 9.0/10

**AI 日报**
1. [HydraFusion 多模型编排发布](#item-ai-daily-1) ⭐️ 7.8/10

**AI 羊毛**
1. [Epic Games 免费游戏：《与你独处》《寻找埃文》](#item-ai-deals-1) ⭐️ 8.0/10

**AI 创作者雷达**
1. [Simon Willison 分享 Astra pelicans 生成转录](#item-ai-creator-1) ⭐️ 0.0/10

---

## Harness 架构

<a id="item-harness-arch-1"></a>
### [mastra-ai/mastra @mastra/core@1.64.0 发布](https://github.com/mastra-ai/mastra/releases/tag/%40mastra/core%401.64.0) ⭐️ 8.8/10

mastra-ai/mastra 发布了 @mastra/core@1.64.0。该版本新增可复用沙箱模板，支持 E2B 和平台预克隆仓库并背景重建，降低冷启动时间。统一所有沙箱提供者的 workingDirectory 配置。客户端工具支持服务器定义的 toModelOutput 转换。

github · PaulieScanlon · 9月4日 13:14

**「设计要点」** 所有沙箱提供者通过 workingDirectory 统一默认工作目录配置。

**「改了什么」** 沙箱 factory 配置从 options 对象改为回调函数。新增 observability 反馈 reviewStatus 支持和更新接口。客户端工具支持服务器定义的 toModelOutput。

**标签**: `#sandbox`, `#runtime`, `#tools`

---

<a id="item-harness-arch-2"></a>
### [browser-use 0.13.10 发布](https://github.com/browser-use/browser-use/releases/tag/0.13.10) ⭐️ 7.8/10

browser-use 0.13.10 发布了新版本，升级 Browser Harness 到 0.1.13，并迁移到 MCP Python SDK 2.1.1。精确固定了所有运行时、选修、开发和构建依赖，并添加了 pydantic-settings 2.15.0 作为显式运行时依赖。更新了错误处理，将未知 MCP 工具调用报告为应用错误。

github · MagMueller · 9月4日 03:28

**「改了什么」** browser-use 0.13.10 版本相对于上一版，升级了 Browser Harness 到 0.1.13，迁移到 MCP Python SDK 2.1.1，并将未知 MCP 工具调用报告为应用错误。

**标签**: `#mcp`, `#runtime`, `#tools`

---

<a id="item-harness-arch-3"></a>
### [Claude Code v2.1.261 发布](https://github.com/anthropics/claude-code/releases/tag/v2.1.261) ⭐️ 6.8/10

Claude Code v2.1.261 补丁版本新增 bashOutputMaxChars 和 taskOutputMaxChars 设置，允许命令和任务输出大小提高至 128K 字符。添加 --append-subagent-system-prompt-file 支持以及 /skill-doctor 命令，用于诊断未使用技能和成本。修复了输入字符顺序、Bedrock 向导挂起、云会话同步以及多项 Remote Control 问题。

github · ashwin-ant · 9月4日 19:58

**「改了什么」** 新增 bashOutputMaxChars/taskOutputMaxChars 设置和 --append-subagent-system-prompt-file 标志。添加 /skill-doctor 诊断命令。修复输入和集成相关 bug。

**标签**: `#subagents`, `#tools`, `#settings`

---

<a id="item-harness-arch-4"></a>
### [pydantic-ai v2.40.0 发布](https://github.com/pydantic/pydantic-ai/releases/tag/v2.40.0) ⭐️ 6.8/10

pydantic-ai v2.40.0 发布。新增实时音频会话 barge-in 支持，包括 handle\_barge\_in=True、interrupt\(played\_bytes=...\) 和 played\_audio\_bytes。添加 RealtimeSession.enqueue\(\) 用于 out-of-band prompts，以及 Agent 的 @agent.on\_event 事件监听器和 send\(\) 的 respond= 参数。这些功能提升运行时交互处理能力。

github · DouweM · 9月5日 00:09

**「改了什么」** 新增 RealtimeSession barge-in 支持（handle\_barge\_in=True、interrupt\(played\_bytes=...\)、played\_audio\_bytes）、enqueue\(\) 方法，以及 Agent.on\_event 事件监听器和 send\(\) 的 respond= 参数。

**标签**: `#runtime`, `#realtime`, `#session`, `#events`

---

<a id="item-harness-arch-5"></a>
### [pydantic-ai v2.39.0 发布](https://github.com/pydantic/pydantic-ai/releases/tag/v2.39.0) ⭐️ 6.8/10

pydantic-ai v2.39.0 发布了 OpenAI gpt-6-astra 模型支持。修复了上下文子树导出器缓存泄漏问题，恢复了 Instrumentation spec 选项，并修复了 Azure 内容过滤器错误、语音最终化以及工具返回媒体归因。还恢复了能力组合不变性。

github · dsfaccini · 9月4日 04:18

**「改了什么」** 相比 v2.38.0，新增了 OpenAI gpt-6-astra 模型支持。修复了上下文子树导出器缓存泄漏问题，恢复了 Instrumentation spec 选项，并修复了 Azure 内容过滤器错误、语音最终化以及工具返回媒体归因，还恢复了能力组合不变性。

**标签**: `#runtime`, `#tools`, `#memory`

---

<a id="item-harness-arch-6"></a>
### [Gemini CLI v0.60.0-nightly.20260904.g87a9c71d5 发布](https://github.com/google-gemini/gemini-cli/releases/tag/v0.60.0-nightly.20260904.g87a9c71d5) ⭐️ 6.8/10

gemini-cli v0.60.0-nightly.20260904.g87a9c71d5 发布。更新 MCP 协议和沙箱硬化。技术上新在 MCP OAuth 流强制执行 RFC 9207 发行者识别，以及 macOS Seatbelt 沙箱临时目录隔离。扩展加载器路径边界验证和 chrome-devtools-mcp 安全 sanitization 也得到硬化。

github · gemini-cli-robot · 9月4日 01:40

**「改了什么」** 相对 v0.59.0-nightly.20260902.g4963a4456 版，此次发布修复了 MCP OAuth 流中的 RFC 9207 合规问题，并隔离了 macOS Seatbelt 沙箱临时目录。扩展加载器和 chrome-devtools-mcp 也进行了路径和安全硬化。

**标签**: `#mcp`, `#sandbox`, `#runtime`, `#tools`

---

<a id="item-harness-arch-7"></a>
### [crewAI 1.15.19 发布](https://github.com/crewAIInc/crewAI/releases/tag/1.15.19) ⭐️ 5.8/10

这是 crewAI 1.15.19 发布。技术上新增 Clipper 集成客户端、CEL 表达式 now\(\) 函数、运行记录、机器大小报告和平台工具注入客户端。修复 URL 读取工具、Gemini 提供者 trailing turn、Ollama 基础 URL 规范化、内存可复用作用域配置、pypdf 和 nltk 安全版本、Claude 结构化输出以及模型调用 hook 拒绝传播等问题。文档更新包括移除 CodeInterpreterTool 示例、更新 prompt-template 链接和 Gemini 模型 ID。

github · joaomdmoura · 9月4日 11:28

**「改了什么」** 新增 Clipper 集成客户端、CEL 表达式 now\(\) 函数、运行结束记录、机器大小粗粒度报告以及平台工具可注入客户端。修复 URL 读取 octet-stream 和 xlsx URLs、Gemini 提供者 trailing user turn、Ollama 基础 URL scheme 和 port、内存可复用作用域配置、pypdf 6.16.2 和 nltk 3.10.3 安全版本、Claude 结构化输出以及模型调用 hook 拒绝传播。

**标签**: `#tools`, `#memory`, `#permissions`

---

<a id="item-harness-arch-8"></a>
### [anthropics/skills 发布](https://github.com/anthropics/skills) ⭐️ 5.0/10

Anthropic 发布了 skills 仓库。该仓库包含 Anthropic 对 Claude 的 skills 实现，Skills 是指令、脚本和资源的文件夹，Claude 可动态加载以提升特定任务性能。Skills 教 Claude 完成可重复的任务，例如创建带品牌指南的文档或使用组织数据分析。参考 agentskills.io 获取 Agent Skills 标准。

rss · GitHub Trending Daily · 9月5日 00:33

**「设计要点」** Skills 实现动态加载机制，Claude 在运行时加载特定任务的指令、脚本和资源。

**标签**: `#runtime`, `#memory`, `#tools`

---

## Agent 工程师日报

<a id="item-agent-engineer-1"></a>
### [Anthropic AI 形式化费马大定理](https://www.anthropic.com/research/formalizing-fermats-last-theorem) ⭐️ 9.0/10

Anthropic 的多代理系统在 Lean 中形式化了费马大定理，生成 1300 万行代码，证明了 29500 个中间定理，用时不到两天。这项工作展示了 AI 代理在大型数学形式化与证明搜索中的能力，对 coding-agent harness、编排和评估基准具有直接相关性。

hackernews · jlebar · 9月4日 18:42 · [社区讨论](https://news.ycombinator.com/item?id=49568506)

**「为什么重要」** 这项工作已发生，展示了 AI 代理在数学形式化中的能力，但其对数学研究的实际影响尚未被证实。

**「可关注」** 可关注：AI 代理在 Lean 中形式化大型数学定理的速度。

**「评论」** 评论中提到 Kevin Buzzard 的博客提供了此成就的上下文，解释了其含义但也指出了局限。部分用户指出证明速度的描述应放在开头段落。

**标签**: `#coding-agent`, `#eval`, `#orchestration`, `#formalization`, `#lean`

---

## AI 日报

<a id="item-ai-daily-1"></a>
### [HydraFusion 多模型编排发布](https://github.blog/ai-and-ml/github-copilot/project-hydrafusion-frontier-quality-via-multi-model-orchestration/) ⭐️ 7.8/10

GitHub 宣布 Project HydraFusion 多模型编排方法，作为 GitHub Copilot 研究预览提供。在离线评估中，HydraFusion 选择性编码工作流匹配或超过 Opus 5 基线，同时降低工作流成本。

rss · GitHub Blog · 9月4日 16:04

**「为什么重要」** 该方法提升 Copilot 编码工作流质量并降低成本。

**「可关注」** 可关注：HydraFusion 选择性编码工作流匹配 Opus 5 基线并降低工作流成本。

**标签**: `#model`, `#lab`, `#product`, `#eval`

---

## AI 羊毛

<a id="item-ai-deals-1"></a>
### [Epic Games 免费游戏：《与你独处》《寻找埃文》](https://www.appinn.com/eggs-2694/) ⭐️ 8.0/10

Epic Games 商城本周限时免费提供电脑游戏《与你独处》和手机游戏《寻找埃文》。其中《寻找埃文》同时提供 Android 和 iOS 版本。截止 9 月 10 日 09:00。

rss · 小众软件 · 9月4日 07:03

**「可关注」** 可关注：免费领取，截止 9 月 10 日 09:00；《与你独处》限 PC，《寻找埃文》限 Android/iOS。

**标签**: `#free-tier`, `#promo`, `#limited-free`

---

## AI 创作者雷达

<a id="item-ai-creator-1"></a>
### [Simon Willison 分享 Astra pelicans 生成转录](https://twitter.com/simonw/status/tweet-2095997113423519902) ⭐️ 0.0/10

Simon Willison 在推特上分享了生成“Astra pelicans”的转录，并链接了“gpt-6-astra max”版本。关键细节是转录和版本的链接。受影响的是关注 AI 生成和 GPT 模型的人。

twitter · Simon Willison · 9月4日 22:07

**标签**: `#Simon Willison`, `#AI generation`, `#Astra pelicans`, `#transcript`, `#GPT-6 Astra`

---