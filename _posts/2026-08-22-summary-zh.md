---
layout: default
title: "Horizon Summary: 2026-08-22 (ZH)"
date: 2026-08-22
lang: zh
---

> 从 148 条内容中筛选出 20 条重要资讯。

---

**Harness 架构**
1. [Cline SDK v0.0.77 发布](#item-harness-arch-1) ⭐️ 7.0/10
2. [DSPy 3.3.1 发布](#item-harness-arch-2) ⭐️ 7.0/10
3. [Agent Framework Python 1.15.0 发布](#item-harness-arch-3) ⭐️ 7.0/10
4. [Cline SDK v0.0.76 发布](#item-harness-arch-4) ⭐️ 6.0/10
5. [anomalyco/opencode v1.18.20 发布](#item-harness-arch-5) ⭐️ 6.0/10
6. [Claude Code 2.1.239 发布](#item-harness-arch-6) ⭐️ 6.0/10
7. [Cline v4.1.12 发布](#item-harness-arch-7) ⭐️ 5.0/10

**Agent 工程师日报**
1. [Claudette：让 Claude 停止 BuzzFeed 风格](#item-agent-engineer-1) ⭐️ 7.0/10
2. [DeepSeek Harness v0.1.1 发布](#item-agent-engineer-2) ⭐️ 7.0/10
3. [llm-openrouter 0.7 发布](#item-agent-engineer-3) ⭐️ 6.0/10

**AI 日报**
1. [美国企业 AI 债务激增 投资者信心受压](#item-ai-daily-1) ⭐️ 7.0/10
2. [明尼苏达律师使用 AI 假引文被吊销律师资格](#item-ai-daily-2) ⭐️ 7.0/10
3. [墨奇 Agentic-Native 重构具身大脑 提交 WRC](#item-ai-daily-3) ⭐️ 6.0/10
4. [DeepSense 桌面 AI：科学家提问题](#item-ai-daily-4) ⭐️ 5.0/10
5. [玻尔科学空间桌面接管科研体力活](#item-ai-daily-5) ⭐️ 5.0/10
6. [端到端论文生成系统：92%假结论检出](#item-ai-daily-6) ⭐️ 5.0/10
7. [ICML 2026 \| 浙大 BEACON 让长程 Agent 成功率近翻倍](#item-ai-daily-7) ⭐️ 5.0/10
8. [科技巨头厌倦 AI slop](#item-ai-daily-8) ⭐️ 5.0/10

**AI 羊毛**
1. [Epic Games 8.21~8.27 免费游戏](#item-ai-deals-1) ⭐️ 6.0/10
2. [青小蛙 26/27 英超赛程日历上线](#item-ai-deals-2) ⭐️ 5.0/10

---

## Harness 架构

<a id="item-harness-arch-1"></a>
### [Cline SDK v0.0.77 发布](https://github.com/cline/cline/releases/tag/sdk/sdk/v0.0.77) ⭐️ 7.0/10

这是 Cline SDK v0.0.77 的发布。任务工具现在仅限于可服务的客户端。通过基于声明的客户端类型的集中解析实现。主机声明其客户端类型，核心工具目录集中解析可用性。CLI 和 VS Code 会话不再注册它们无法操作的工具，集线器会话从请求客户端的元数据中以相同方式解析。

github · github-actions\[bot\] · 8月21日 04:56

**「设计要点」** 工具层通过集中目录解析基于客户端类型的可用性。主机声明其客户端类型，CLI/VS Code/hub 分别处理元数据。

**「改了什么」** 相对上一版，tasks 工具现在仅限于可服务的客户端。主机声明客户端类型，核心工具目录集中解析可用性，CLI 和 VS Code 会话不再注册它们无法操作的工具。

**标签**: `#runtime`, `#tools`

---

<a id="item-harness-arch-2"></a>
### [DSPy 3.3.1 发布](https://github.com/stanfordnlp/dspy/releases/tag/3.3.1) ⭐️ 7.0/10

DSPy 3.3.1 发布了，主要针对 PythonInterpreter 运行时进行了改进。它提供了托管运行时安装选项，增强了沙箱隔离和执行完整性，并添加了端到端的执行可见性。该版本还提升了优化器吞吐量、结构化适配器正确性和 MCP 兼容性。

github · isaacbmiller · 8月21日 23:07

**「设计要点」** PythonInterpreter 采用托管 Deno/Pyodide 运行时，优先使用 managed binary 并隔离 ambient 配置。沙箱通过保护文件、拒绝递归工具调用等方式强化隔离。新增回调 API 暴露解释器生命周期事件，包括 start/end 和工具调用。

**「改了什么」** PythonInterpreter 安装更简单，支持 dspy\[deno\] 包，沙箱隔离和请求处理得到加强，添加了执行生命周期回调。优化器支持多提案 GEPA 并发，结构化适配器处理默认输出，MCP SDK v2 兼容性增强。

**标签**: `#runtime`, `#sandbox`, `#mcp`, `#tools`, `#interpreter`

---

<a id="item-harness-arch-3"></a>
### [Agent Framework Python 1.15.0 发布](https://github.com/microsoft/agent-framework/releases/tag/python-1.15.0) ⭐️ 7.0/10

Microsoft Agent Framework Python 1.15.0 版本发布。该版本新增了 A2UI 接口支持、MiddlewareFailure 作为 first-class fatal signal、进程级别的 checkpoint type registry，以及 Foundry 托管代理的 resilient 特性。

github · giles17 · 8月21日 23:08

**「改了什么」** 新增了 A2UI 接口支持、MiddlewareFailure 信号、进程级别的 checkpoint 注册表，并增强了 Foundry 托管代理的弹性支持。

**标签**: `#runtime`, `#memory`, `#tools`

---

<a id="item-harness-arch-4"></a>
### [Cline SDK v0.0.76 发布](https://github.com/cline/cline/releases/tag/sdk/sdk/v0.0.76) ⭐️ 6.0/10

Cline SDK v0.0.76 发布了。该版本新增了模型驱动图像生成功能，支持代理创建和管理计划任务以及持久待办事项。技能命令加载方式通过技能工具加载，而不是直接粘贴到用户消息中。

github · github-actions\[bot\] · 8月21日 02:39

**「设计要点」** 运行时增加了 PreToolUse hook 的 contextModification 交付机制，作为 &lt;hook\_context&gt; 块发送给模型。PostToolUse hooks 现在被等待执行并支持 contextModification 控制。

**「改了什么」** 相比上一版，Cline SDK v0.0.76 增加了模型驱动图像生成和计划任务支持。修复了技能命令加载和提供程序工具活动可见性等问题。

**标签**: `#runtime`, `#tools`, `#memory`, `#planning`

---

<a id="item-harness-arch-5"></a>
### [anomalyco/opencode v1.18.20 发布](https://github.com/anomalyco/opencode/releases/tag/v1.18.20) ⭐️ 6.0/10

anomalyco/opencode v1.18.20 是针对 subagent 失败、权限和网络错误重试的 bugfix 发布。重点修复了 subagent tool call 处理中的 resumable task\_id 支持，以及在 opencode run 中处理 subagent 触发的权限请求。同时增加了网络错误 provider responses 的重试逻辑，包括 finish\_reason: network\_error 和 network\_error 等变体。

github · opencode-agent\[bot\] · 8月21日 08:09

**「改了什么」** 此版本改进了 subagent tool call 的 resumable task\_id 处理，并增加了 opencode run 中 subagent 权限请求的响应逻辑，以及更多网络错误的重试变体。

**标签**: `#subagents`, `#permissions`, `#runtime`

---

<a id="item-harness-arch-6"></a>
### [Claude Code 2.1.239 发布](https://code.claude.com/docs/en/changelog#2-1-239) ⭐️ 6.0/10

Claude Code 2.1.239 发布了更新版本。该版本新增了成本估算包含 US-only-inference 推理 premium 的功能，添加了 fullscreen renderer 渲染器 rollout，并提供了 /claude-api upgrade 工具用于 Python 项目从 anthropic 0.x 迁移到 1.x。云会话插件同步处理改进，支持 name@synced 格式和 enable/disable 操作。Alpine/musl 构建支持原生插件添加功能。

rss · Claude Code Changelog · 8月21日 21:09

**「设计要点」** Alpine/musl 构建支持原生 image paste、clipboard 和 audio-capture add-ons 加载，使用 musl 构建的二进制文件替代 glibc 版本。

**「改了什么」** 相比上一版本，主要新增了成本估算包含 US-only-inference 推理 premium 的支持、全屏渲染器 rollout，以及 /claude-api upgrade 工具。云会话插件同步处理和 Alpine/musl 构建支持也已更新。

**标签**: `#tools`, `#runtime`, `#sandbox`, `#permissions`, `#plugins`

---

<a id="item-harness-arch-7"></a>
### [Cline v4.1.12 发布](https://github.com/cline/cline/releases/tag/v4.1.12) ⭐️ 5.0/10

Cline v4.1.12 发布了新版本。该版本强制企业 MCP 控制在 Customize 市场，MCP 条目在远程配置禁用市场时被隐藏，并在配置 allowlist 时限制为 allowedMCPServers。同时，恢复了自定义 OpenAI-Compatible 模型的工具调用功能，这些模型之前存储的 capability list 为空。

github · github-actions\[bot\] · 8月21日 22:39

**「改了什么」** Cline v4.1.12 强制企业 MCP 控制在 Customize 市场，MCP 条目在远程配置禁用市场时被隐藏，并在配置 allowlist 时限制为 allowedMCPServers。恢复了自定义 OpenAI-Compatible 模型的工具调用功能，这些模型之前存储的 capability list 为空。

**标签**: `#mcp`, `#permissions`, `#tools`, `#runtime`

---

## Agent 工程师日报

<a id="item-agent-engineer-1"></a>
### [Claudette：让 Claude 停止 BuzzFeed 风格](https://github.com/adnanakil/nobuzz/blob/main/README.md) ⭐️ 7.0/10

GitHub 仓库 Claudette 提供了让 Claude 输出简洁、非 BuzzFeed 风格的提示词工程技巧。通过限制注释块长度不超过 7 个词、函数名不超过 4 个词、用户消息不超过 10 个词，并使用主动语态来清理输出。这项技术直接适用于代理 harness、评估和编排场景，与最近的 &\#x27;Vomit&\#x27; 帖子相关。

hackernews · aakil · 8月21日 14:31 · [社区讨论](https://news.ycombinator.com/item?id=49388752)

**「为什么重要」** 这项提示词工程技巧通过严格风格规则直接帮助代理 harness、评估和编排，减少 verbosity，与最近的 Vomit 帖子相关。

**「可关注」** 可关注：限制词数是清理 Claude 输出最有效的因素。

**「评论」** 社区成员分享了类似提示词的成功经验，强调词数限制是最强的因素。有人提到与 Vomit 帖子相关，并讨论了 Claude 输出风格的问题。

**标签**: `#orchestration`, `#eval`, `#coding-agent`, `#harness`

---

<a id="item-agent-engineer-2"></a>
### [DeepSeek Harness v0.1.1 发布](https://www.reddit.com/r/LocalLLaMA/comments/1vugyfe/deepseek_harness_v011_released/) ⭐️ 7.0/10

DeepSeek Harness v0.1.1 发布了。该版本添加了对多模态视觉理解模型 DeepSeek-V4-Flash-Vision-Exp 的支持，并增强了命令和附件的图像处理能力。命令如 /goal 和 /plan 可以接受文本和图像输入，@ 菜单可以引用文件和会话。MCP/ACP 也支持持久图像附件，PTC 模式支持转发嵌套图像。

reddit · r/LocalLLaMA · /u/Fun-Doctor6855 · 8月21日 13:51

**「为什么重要」** 此更新值得今天阅读，因为它为代理系统引入了多模态视觉理解模型支持和图像附件功能。已发生的变化是添加了 DeepSeek-V4-Flash-Vision-Exp 支持和原生图像请求配置，尚未证实的是对命令执行和附件处理的工作流影响。

**「可关注」** 可关注：支持原生图像请求配置、命令接受图像输入以及持久图像附件的特性。

**标签**: `#harness`, `#mcp`, `#orchestration`, `#coding-agent`

---

<a id="item-agent-engineer-3"></a>
### [llm-openrouter 0.7 发布](https://simonwillison.net/2026/Aug/21/llm-openrouter/) ⭐️ 6.0/10

llm-openrouter 0.7 发布，支持与 LLM 0.32 兼容，并使用 OpenRouter 的 Responses API 实现。
新增三个服务器端工具：Shell、WebFetch 和 WebSearch，可通过选项如 -T WebSearch 启用。
这些更新使该插件在 OpenRouter 上的 reasoning LLMs 中表现更好，适用于 agent 工作流。

rss · Simon Willison · 8月21日 16:58

**「为什么重要」** 这个版本的更新值得今天关注，因为它增加了对 OpenRouter Responses API 的支持，并新增了服务器端工具，适用于 coding agent 和 harness 工作流。

**「可关注」** 可关注：新增的服务器端工具 Shell、WebFetch 和 WebSearch 可通过 -T WebSearch 等选项启用。

**标签**: `#orchestration`, `#coding-agent`, `#harness`, `#tool-use`

---

## AI 日报

<a id="item-ai-daily-1"></a>
### [美国企业 AI 债务激增 投资者信心受压](https://news.google.com/rss/articles/CBMivAFBVV95cUxNR0I5VXZyeVp4RlV6cnhVdXFwZ2RNZUU0Q1czQ2c0WkpZUUJuRV9PNEg0VHkzLVlnSUdZMWVOalJzNkNXdlNtamlGSzRLbVRXb0VkVzl3dm5Uc3hPV21Cb3BIdTNyOWZQSDRGQ1ZvV2xUVUZ6eExfeGpRM0hQck8wSDlzR3ViRDJHS25NaGxwNHdVYWN5cHRUcWJvb0hybjRtclNxMFFGT18tMmc2SEw5RFNYb3ZrSWZpS0VYTw?oc=5) ⭐️ 7.0/10

美国企业正在积累大量 AI 相关债务。这加剧了投资者对 AI 投资的疲劳。随着疲劳显现，投资者信心受到考验。

google\_news · Reuters · 8月21日 15:07

**「为什么重要」** 这反映了 AI 投资领域的新行业趋势。

**「可关注」** 可关注：美国企业 AI 债务激增测试投资者极限。

**标签**: `#industry`, `#AI`, `#finance`, `#investment`, `#debt`

---

<a id="item-ai-daily-2"></a>
### [明尼苏达律师使用 AI 假引文被吊销律师资格](https://news.google.com/rss/articles/CBMinwFBVV95cUxPbDU2dVoya2VUT2pDdnA3bVZ3UlQyOE0xeEpueDJONGl0MUpEWFBpeXVGRHZtblU2OWVuYnhncmJ2WmlUeE5uUEtnRUtOMWpKalhtakpQLUE0N3ZSdFYwWU1GSmZrR3pMVTkxSWtaanlvUmk2UElqMnpHdDd1Q0FWbmJxalplMzQzNGRJcWZoRGswWjNUc1B1TE1pQmpNR28?oc=5) ⭐️ 7.0/10

明尼苏达州一名律师因使用人工智能生成的虚假案例引文而被吊销律师资格。该事件由 MPR News 报道。目前尚不清楚具体引文或案件细节。

google\_news · MPR News · 8月21日 21:56

**「为什么重要」** 该事件提供了 AI 在法律实践中滥用的新事实。

**「可关注」** 可关注：使用 AI 生成的虚假案例引文

**标签**: `#industry`, `#policy`, `#model`

---

<a id="item-ai-daily-3"></a>
### [墨奇 Agentic-Native 重构具身大脑 提交 WRC](https://mp.weixin.qq.com/s?__biz=MzA3MzI4MjgzMw==&amp;mid=2651051506&amp;idx=1&amp;sn=d1eb5c88e5a7ebfb2d81c68804684eed) ⭐️ 6.0/10

墨奇使用 Agentic-Native 方法重构机器人具身大脑，实现连续长程任务执行，并提交至 WRC。
这比会做一个动作更难的，是把一整件事连续做完。
目前该方法正处于提交阶段，具体效果有待验证。

rss · 机器之心 · 8月21日 03:19

**「为什么重要」** 机器人长程任务的连续执行比单个动作更具挑战性，墨奇的 Agentic-Native 方法提供了新思路。

**「可关注」** 可关注：墨奇通过 Agentic-Native 重构具身大脑以支持长程任务连续执行。

**标签**: `#robotics`, `#embodied-ai`, `#product`, `#industry`

---

<a id="item-ai-daily-4"></a>
### [DeepSense 桌面 AI：科学家提问题](https://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw==&amp;mid=2247913892&amp;idx=2&amp;sn=cf9d597946f8f0987109569128cf0bc6) ⭐️ 5.0/10

DeepSense 科技开发桌面 AI 系统，将科学研究的全部流程搬到桌面。科学家只需提出问题，AI 负责跑实验。让科学家的时间回到科学创造。

rss · 量子位 · 8月21日 03:02

**「可关注」** 可关注：科学家只管提问题，AI 负责跑实验。

**标签**: `#product`, `#industry`

---

<a id="item-ai-daily-5"></a>
### [玻尔科学空间桌面接管科研体力活](https://mp.weixin.qq.com/s?__biz=MzA3MzI4MjgzMw==&amp;mid=2651051506&amp;idx=2&amp;sn=7492c796da65176af0bf9bcce332eae7) ⭐️ 5.0/10

玻尔科学空间精选多学科 AI 科学家，服务你的科研。文章称其在桌面接管科研「体力活」，把时间还给科学创造。

rss · 机器之心 · 8月21日 03:19

**「可关注」** 可关注：玻尔科学空间精选多学科 AI 科学家，服务你的科研。

**标签**: `#product`, `#industry`, `#AI`

---

<a id="item-ai-daily-6"></a>
### [端到端论文生成系统：92%假结论检出](https://mp.weixin.qq.com/s?__biz=MzA3MzI4MjgzMw==&amp;mid=2651051506&amp;idx=3&amp;sn=aa2e1f4dd425cf0a52631efb49e2f182) ⭐️ 5.0/10

报道了一款端到端研究论文生成系统。该系统支持自动运行实验、绘制图表，并直接输出论文初稿。假结论检出率达到 92%。但系统具体实现细节尚未公开。

rss · 机器之心 · 8月21日 03:19

**「可关注」** 可关注：端到端论文生成系统支持自动跑实验、画图并直出论文初稿

**标签**: `#product`, `#industry`, `#model`

---

<a id="item-ai-daily-7"></a>
### [ICML 2026 \| 浙大 BEACON 让长程 Agent 成功率近翻倍](https://mp.weixin.qq.com/s?__biz=MzIwMTc4ODE0Mw==&amp;mid=2247722361&amp;idx=2&amp;sn=5a006b50943113b0c6017e795dbada36) ⭐️ 5.0/10

浙江大学 BEACON 方法据称能近乎翻倍长程 Agent 成功率。该方法通过按里程碑分配信用来提升性能。材料中未提供具体实验数据和对比基线。

rss · PaperWeekly · 8月21日 14:31

**「可关注」** 可关注：按里程碑分配信用

**标签**: `#lab`, `#model`, `#agent`, `#eval`, `#industry`

---

<a id="item-ai-daily-8"></a>
### [科技巨头厌倦 AI slop](https://news.google.com/rss/articles/CBMiakFVX3lxTFBOWjV4Szg4bEFBdlVDNGxjNE5ocy1wMnN1ZkRUMUlkazNTV21NdzhwMGlMT3hsVzBKeXNHOEJoMnB3NERSZ2xYMEFKa25ISF9fRGJvV01hNWc4VExHb19xb0N4WE00YzA1Vnc?oc=5) ⭐️ 5.0/10

《纽约时报》报道称，科技巨头对 AI slop 感到不满。行业对低质量 AI 生成内容的疲劳普遍存在。报道未提供具体公司名称或量化数据。

google\_news · The New York Times · 8月21日 19:39

**「可关注」** 可关注：科技巨头对 AI slop 感到不满。

**标签**: `#industry`

---

## AI 羊毛

<a id="item-ai-deals-1"></a>
### [Epic Games 8.21~8.27 免费游戏](https://www.appinn.com/eggs-26821/) ⭐️ 6.0/10

Epic Games 本周赛博领鸡蛋，送出《卡牌末日》和《阿尔比恩在线》两款电脑游戏，以及《沙漠房车漫游》一款手机游戏。活动时间为 8.21~8.27。领取需 Epic Games 账号。

rss · 小众软件 · 8月21日 10:48

**「可关注」** 可关注：游戏免费领取，需在活动期间 8.21~8.27 内完成。

**标签**: `#promo`, `#limited-free`, `#coupon`

---

<a id="item-ai-deals-2"></a>
### [青小蛙 26/27 英超赛程日历上线](https://www.appinn.com/26-27-premier-league-calendar/) ⭐️ 5.0/10

青小蛙维护的 2026～2027 赛季英超赛程、比分、进球日历已上线。
可订阅到手机或电脑日历应用中，会自动更新比分。
这是免费订阅，无到期限制。
订阅后可在手机、电脑日历应用中看到每周的英超对阵，比赛结束后比分自动更新。

rss · 小众软件 · 8月21日 12:06

**「为什么重要」** 英超即将开赛，青小蛙维护的赛程日历已赶在开赛前做好。
可立即订阅使用，查看每周对阵和比分更新。

**「可关注」** 可关注：订阅手机或电脑日历应用查看英超赛程和比分。

**标签**: `#free`, `#calendar`, `#football`, `#tool`

---