---
layout: default
title: "Horizon Summary: 2026-08-24 (ZH)"
date: 2026-08-24
lang: zh
---

> 从 101 条内容中筛选出 16 条重要资讯。

---

**Harness 架构**
1. [Cline SDK v0.0.78 发布](#item-harness-arch-1) ⭐️ 8.0/10
2. [Cline CLI v3.0.57 发布](#item-harness-arch-2) ⭐️ 8.0/10
3. [Cline v4.1.15 MCP 自动批准](#item-harness-arch-3) ⭐️ 5.0/10
4. [Cline desktop-v0.0.16 发布](#item-harness-arch-4) ⭐️ 5.0/10

**Agent 工程师日报**
1. [Harness 是什么？](#item-agent-engineer-1) ⭐️ 7.0/10
2. [Fable 发布：harness 优化值得关注](#item-agent-engineer-2) ⭐️ 7.0/10
3. [Kimi K3 2.8T 在 8x B300 上部署](#item-agent-engineer-3) ⭐️ 6.0/10

**AI 日报**
1. [量子位：双足人形一体化大脑，机器人自主开卡丁车](#item-ai-daily-1) ⭐️ 5.0/10
2. [匿名大模型智谱血缘曝光，Cursor 疑 GLM](#item-ai-daily-2) ⭐️ 5.0/10
3. [OpenAI 领导警告“持久”AI 网络攻击威胁](#item-ai-daily-3) ⭐️ 5.0/10
4. [好莱坞 AI 秘密对话公开](#item-ai-daily-4) ⭐️ 5.0/10
5. [Workday 呼吁国会就 AI 代理行动](#item-ai-daily-5) ⭐️ 5.0/10
6. [Epic 或考虑 AI 直接患者 EHR 访问](#item-ai-daily-6) ⭐️ 5.0/10
7. [Gemini 免费一年，学生学术人士可领](#item-ai-daily-7) ⭐️ 5.0/10

**AI 羊毛**
1. [Box Blanks 免费参数化纸箱模板生成器](#item-ai-deals-1) ⭐️ 5.0/10
2. [shopat.lol 免费全球收藏板](#item-ai-deals-2) ⭐️ 5.0/10

---

## Harness 架构

<a id="item-harness-arch-1"></a>
### [Cline SDK v0.0.78 发布](https://github.com/cline/cline/releases/tag/sdk/sdk/v0.0.78) ⭐️ 8.0/10

Cline SDK v0.0.78 增加了在 drain hub 或升级时不丢失工作的能力。通过 durable event logs 实现重放和去重，queued runs 避免丢弃工作。修复了自定义 OpenAI-Compatible 模型的 tool calling 问题，并改进了 Langfuse traces 的 session 和 client identity 处理。同时刷新了模型目录，更新了多个提供商的默认模型。

github · github-actions\[bot\] · 8月22日 23:58

**「设计要点」** 运行时使用 durable event logs 进行 replay 和 deduping，durable runs 采用 queued 方式处理。支持在 hub 升级或 drain 时无缝切换客户端。

**「改了什么」** 支持 hub draining 和升级而不丢失工作；修复了自定义 OpenAI-Compatible 模型的 tool calling 问题；改进了 Langfuse traces 的身份处理；刷新了模型目录并更新了默认模型。

**标签**: `#runtime`, `#memory`, `#tools`

---

<a id="item-harness-arch-2"></a>
### [Cline CLI v3.0.57 发布](https://github.com/cline/cline/releases/tag/cli-v3.0.57) ⭐️ 8.0/10

Cline CLI v3.0.57 发布了，添加了 \`cline hub drain\` 和 \`cline hub upgrade\` 命令。会话在 hub 重启后幸存，通过去重事件重放确保不重复交付。修复了自定义 OpenAI 兼容模型工具调用被静默禁用的问题，并改进了 Langfuse 追踪和刷新了模型目录。

github · github-actions\[bot\] · 8月23日 00:04

**「设计要点」** hub 管理通过 drain 和 upgrade 命令实现优雅停止和重启。会话在重启后通过去重事件重放幸存。Langfuse 追踪携带会话和客户端身份信息。

**「改了什么」** 改了什么：相对上一版 v3.0.56，主要新增了 hub drain 和 upgrade 命令，会话在重启后幸存，修复了自定义模型工具调用被静默禁用，并更新了 Langfuse 追踪和模型目录。

**标签**: `#runtime`, `#tools`, `#hub`, `#memory`, `#tracing`

---

<a id="item-harness-arch-3"></a>
### [Cline v4.1.15 MCP 自动批准](https://github.com/cline/cline/releases/tag/v4.1.15) ⭐️ 5.0/10

Cline 发布 v4.1.15，修了 MCP 工具的自动批准逻辑。打开「Use MCP servers」开关后，现在会自动批准每一次 MCP 工具调用；此前该开关只对已经单独 opt-in 的工具生效，打开后看起来没反应。改动经 SDK bundle 下发，作用于跑该 bundle 的 Windows。

github · github-actions\[bot\] · 8月23日 19:56

**「设计要点」** MCP 工具权限现在由「Use MCP servers」总开关单独管辖，不再叠加上逐工具 opt-in。改动走 SDK bundle，覆盖使用该 bundle 的 Windows。

**「改了什么」** 相对 v4.1.14，打开「Use MCP servers」即自动批准全部 MCP 工具调用，不再要求工具先被单独 opt-in。

**标签**: `#mcp`, `#tools`, `#permissions`, `#runtime`

---

<a id="item-harness-arch-4"></a>
### [Cline desktop-v0.0.16 发布](https://github.com/cline/cline/releases/tag/desktop-v0.0.16) ⭐️ 5.0/10

Cline 桌面版 desktop-v0.0.16 发布了。该版本添加了 Hub 实例之间的无缝代理切换功能，支持断开重连时重放之前未完成的工作。还修复了自定义 OpenAI 兼容模型的工具调用问题，并刷新了模型目录和功能标志。

github · github-actions\[bot\] · 8月22日 23:45

**「设计要点」** 代理切换在运行时处理 Hub 重启时拒绝新工作，通过重放机制在断开后恢复之前的工作。工具调用修复解决了自定义模型 capability list 推断导致的静默禁用。

**「改了什么」** desktop-v0.0.16 相比上一版添加了 Hub 实例间代理切换与工作重放能力。修复了自定义模型工具调用的静默禁用问题，并更新了模型目录和服务器功能标志。

**标签**: `#runtime`, `#memory`, `#tools`

---

## Agent 工程师日报

<a id="item-agent-engineer-1"></a>
### [Harness 是什么？](https://earendil.com/posts/what-is-a-harness/) ⭐️ 7.0/10

earendil.com 的博客文章探讨了 AI 代理“harness”（模型引擎的底盘）的概念，通过构建 CLI 工具和 handoff 机制进行了说明，在 Hacker News 上引发了对实用代理工具的讨论。这篇文章强调了 harness 作为 LLM、工具和环境的集成层，提供了内部 CLI、技能和跨模态 handoff 的实际例子。这一内容直接相关于 coding agent 工程师和代理架构设计。

hackernews · tosh · 8月23日 14:24 · [社区讨论](https://news.ycombinator.com/item?id=49409092)

**「为什么重要」** 这篇文章提供了 harness 的实用定义和构建建议，虽然 hype 词在 2026 年可能流行，但它帮助理解代理工具链的 orchestration。

**「可关注」** 可关注：Harness 作为模型引擎的底盘，强调内部 CLI 工具和 handoff 机制，这些是代理与工具交互的关键张力。

**「评论」** 评论中，用户分享了为会计代理构建 harness 的经验，推荐内部 CLI 工具；另有讨论 handoff 机制和比喻，Pi 被提及为拥有出色扩展系统的 harness 例子。

**标签**: `#harness`, `#orchestration`, `#coding-agent`

---

<a id="item-agent-engineer-2"></a>
### [Fable 发布：harness 优化值得关注](https://simonwillison.net/2026/Aug/23/drew-breunig/) ⭐️ 7.0/10

Drew Breunig 解释说，Fable 发布后其高成本使得优化 coding harness 和上下文策略变得有价值。之前，由于新模型会以相同或更低价格出现，改进 coding harness 的时间被认为不值得。但 Fable 改变了这一情况。虽然 Opus 等模型对大多数代码任务足够好（包括 5.6、K3 和 GLM），我们开始思考哪些工作该放在哪里。

rss · Simon Willison · 8月23日 19:55

**「为什么重要」** Fable 的高成本改变了优化 coding harness 和上下文策略的优先级，这对 coding agent 的架构和 workflow 优先级有直接影响。

**「可关注」** 可关注：Fable 高成本下，coding harness 和上下文策略优化值得关注，因为 Opus 等模型对大多数代码足够好。

**标签**: `#harness`, `#orchestration`, `#coding-agent`, `#context`

---

<a id="item-agent-engineer-3"></a>
### [Kimi K3 2.8T 在 8x B300 上部署](https://www.reddit.com/r/LocalLLaMA/comments/1vw1j2p/i_hosted_kimi_k3_28t_parameters_using_8_b300s_92/) ⭐️ 6.0/10

用户在 Modal 平台使用 8 块 B300 GPU，通过 vLLM 运行 Kimi K3 \(2.8T 参数\) 模型。冷启动约 27 分钟，TTFT 0.92-1.02 秒，解码速度 92 tok/s，平均 83 tok/s。输出成本为每百万 tokens $190。一键运行约 $36 GPU 时间。还测试了 Unsloth 1-bit 量化版本，在 8x A100 上运行约 9 tok/s，成本更高但质量可接受。

reddit · r/LocalLLaMA · /u/OtherRaisin3426 · 8月23日 08:25

**「为什么重要」** 这个报告提供了使用 B300 GPU 运行 2.8T 模型的 benchmark 数据和成本对比，对于关注大模型部署优化的工程师有实际参考。

**「可关注」** 可关注：vLLM 在 8x B300 上的 tensor parallel 8 配置、MXFP4 量化选项以及具体 benchmark 结果。

**标签**: `#harness`, `#orchestration`, `#coding-agent`, `#eval`

---

## AI 日报

<a id="item-ai-daily-1"></a>
### [量子位：双足人形一体化大脑，机器人自主开卡丁车](https://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw==&amp;mid=2247914338&amp;idx=1&amp;sn=16a9f30f149a5a43faae07ae23e67c48) ⭐️ 5.0/10

量子位报道，几名读博年轻人团队押注双足人形机器人的一体化大脑，展示其自主驾驶卡丁车的演示。机器人连续过弯，全程自主驾驶，无需人工干预。项目强调一体化大脑概念，但未公开具体实验室名称或重大技术发布细节。

rss · 量子位 · 8月23日 05:30

**「为什么重要」** 这个演示展示了人形机器人一体化大脑在实际驾驶场景中的应用。

**「可关注」** 可关注：一体化大脑在双足人形机器人中的应用。

**标签**: `#robotics`, `#humanoid`, `#AI`, `#industry`, `#product`

---

<a id="item-ai-daily-2"></a>
### [匿名大模型智谱血缘曝光，Cursor 疑 GLM](https://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw==&amp;mid=2247914338&amp;idx=2&amp;sn=2ff9bfd49e1df185bba2332ffe2db8de) ⭐️ 5.0/10

量子位技术调查发现，匿名大模型与智谱 AI 存在血缘关系。通过 tokenizer、视频编码和 API 报错等特征被识别。同时，有人怀疑 Cursor 使用开源 GLM 进行训练。

rss · 量子位 · 8月23日 05:30

**「可关注」** 可关注：匿名大模型通过 tokenizer、视频编码和 API 报错被扒出智谱血缘。

**标签**: `#model`, `#lab`, `#industry`, `#open-source`, `#product`

---

<a id="item-ai-daily-3"></a>
### [OpenAI 领导警告“持久”AI 网络攻击威胁](https://news.google.com/rss/articles/CBMilgFBVV95cUxQTU9VbHZPQ2czTUlfNVZMVk53TkZRbUhPTTJJQ3o3SjE4VEpiZWx2UHBpWG5MZkN6aG9ZVWsycTk1ME9pNFNmaWFybG1oMmxlY2NoZEEyZlZwT09SY2dxdWZIYjFmSGRLNG91dkJLU1ZrYV8yRHY0eHc5TnR1UktESUpUR1l6SlRueXlIbU9aeW5TYTZqR0E?oc=5) ⭐️ 5.0/10

OpenAI 一位领导人在接受采访时表示，他们正进入一个不同的章节，警告存在“持久”的 AI 网络攻击威胁。材料中未提供具体领导人的姓名或引用的确切内容。没有关键数字或具体限制。

google\_news · The Guardian · 8月23日 19:00

**标签**: `#openai`, `#lab`, `#industry`, `#policy`

---

<a id="item-ai-daily-4"></a>
### [好莱坞 AI 秘密对话公开](https://news.google.com/rss/articles/CBMijgFBVV95cUxON0tuS1ZzQ1JHS05JU01LT0pOTEttZi1XRktqUkRkd2RxMGFlVkk0d0EzRlBzOUgyX2J1WlZtVzNRTEN6a3owYWF5Z1ZVZjVRZ19CbjF1T0o1djRHQVQ5WGdISURHNGd4RGd0TEpsV2thbXVONU9DOElxeExGUnoxcXE3MmZqYjY2QnQwNGdn?oc=5) ⭐️ 5.0/10

好莱坞的秘密 AI 对话现在公开了。这些对话的实施计划也一并公布。根据 The Ankler 的报道，这涉及好莱坞娱乐行业的 AI 应用。

google\_news · The Ankler · 8月23日 17:02

**标签**: `#industry`, `#hollywood`, `#ai`, `#entertainment`

---

<a id="item-ai-daily-5"></a>
### [Workday 呼吁国会就 AI 代理行动](https://news.google.com/rss/articles/CBMiigFBVV95cUxONjNpdS1EN3hhWkdRQ19nZGd3eU9JcVlaZ25hTHB3NUZ2dzdPdm5RZHpIdHQ4RXQ3cEIzTUhlVGc0d1UzNGp6TVdjeEpsM1BUR0l4T0FIUmF0ZVpmemZWbGJ3aUVZU0MzU1FienlpSWlrb3gycmw5Sy1acVlvT0tXQXJjY2NCdTVTMGc?oc=5) ⭐️ 5.0/10

Workday 呼吁美国国会就 AI 代理采取行动。Punchbowl News 报道了这则消息。报道中未提供具体行动建议或公司细节。

google\_news · Punchbowl News · 8月23日 21:42

**「可关注」** 可关注：Workday 呼吁国会就 AI 代理采取行动。

**标签**: `#policy`, `#industry`, `#AI agents`

---

<a id="item-ai-daily-6"></a>
### [Epic 或考虑 AI 直接患者 EHR 访问](https://news.google.com/rss/articles/CBMisAFBVV95cUxQREgwc2YxWENscG94Ukdlb0h6bWlLdXlNUndmMnEwdXdyc25GSWpCdThXd3NFOE1xM0g2SWs3UDl0Y21mbnJlSlZzMnZMMjc5ZjMya3lQRGtkcVFNc1VZX3drNEpXd0gtcUkxcFVURXppOUlVRmNvenFLenl5a1lHVXFZS2FKbFE3NVZ2dWd2c2g3TjBjS1htQkJKQ2hLR3R1ZmZ6bW5fWmJZZ1BHNFV1bQ?oc=5) ⭐️ 5.0/10

Forbes 报道称，Epic Systems 可能正在探索直接 AI 驱动的患者 EHR 数据访问。Epic 是主要的电子健康记录提供商。报道仅为标题，未提供更多细节或时间表。

google\_news · Forbes · 8月23日 19:15

**「可关注」** 可关注：Epic Systems 可能探索直接 AI 驱动的患者 EHR 数据访问。

**标签**: `#industry`, `#product`, `#AI`

---

<a id="item-ai-daily-7"></a>
### [Gemini 免费一年，学生学术人士可领](https://news.google.com/rss/articles/CBMimgFBVV95cUxON1JsSFlCN2t3dnVTS3VXdmhTODZnaUlKQ04tMDV0YS02NEZnM0Z3S1V5QU5GMkRudmJUUmtGZlhXaXo2d1IzRFFjNEtDMEhXSHpwTXJocm8wTVpIMm9LNnQtV3BBX2FrU2VxSElWaHplbElCTi1nenBVMll5R2FtcG1zN1Uzd1dlQ0ZmQVB0c1RsQUZVWU9najd3?oc=5) ⭐️ 5.0/10

Google 宣布为学生和学术人士提供一年 Gemini 免费使用权。新学年开始之际，此活动让更多人接触 Gemini。领取方式是通过 blog.google 提供的链接。

google\_news · blog.google · 8月23日 20:32

**「为什么重要」** 这一举措有助于学生和研究者在学术年初期接触前沿 AI 工具。

**「可关注」** 可关注：学生和学术人士可免费获得一年 Gemini 使用权。

**标签**: `#model`, `#lab`, `#product`, `#policy`, `#industry`

---

## AI 羊毛

<a id="item-ai-deals-1"></a>
### [Box Blanks 免费参数化纸箱模板生成器](https://boxblanks.com/) ⭐️ 5.0/10

Show HN 发布了 Box Blanks，这是一个免费的参数化纸箱模板生成器，支持 479 种盒子样式。
工具完全免费，用户可以立即访问 boxblanks.com 使用。
无使用额度限制，适用于包装设计和印刷制作。

rss · HN Free API / Credits · 8月23日 14:02

**「为什么重要」** Box Blanks 提供免费参数化纸箱模板生成器，479 种样式立即可用。
对于需要定制纸箱的用户来说，今天可以直接使用。

**「可关注」** 可关注：479 种盒子样式的参数化生成，适用于包装设计和印刷行业。

**标签**: `#free-tier`, `#promo`, `#limited-free`

---

<a id="item-ai-deals-2"></a>
### [shopat.lol 免费全球收藏板](https://shopat.lol/) ⭐️ 5.0/10

affixio 在 shopat.lol 发布了免费全球收藏产品和商店的板子。材料中未提供访问额度、模型或价格的具体信息。领取条件为免费，但没有截止时间。

rss · HN Free API / Credits · 8月23日 12:21

**标签**: `#free-tier`, `#promo`

---