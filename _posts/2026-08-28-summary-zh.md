---
layout: default
title: "Horizon Summary: 2026-08-28 (ZH)"
date: 2026-08-28
lang: zh
---

> 从 234 条内容中筛选出 18 条重要资讯。

---

**Harness 架构**
1. [Claude Code v2.1.248 发布](#item-harness-arch-1) ⭐️ 8.5/10
2. [FastMCP v4.0.0b5 发布](#item-harness-arch-2) ⭐️ 8.5/10
3. [Cloudflare Agents agents@0.22.0 发布](#item-harness-arch-3) ⭐️ 7.5/10
4. [Cloudflare agents 的 @cloudflare/think@0.17.0 版本发布](#item-harness-arch-4) ⭐️ 7.5/10
5. [cloudflare/agents @cloudflare/ai-chat@0.11.0 发布](#item-harness-arch-5) ⭐️ 7.5/10
6. [LangChain 1.4.0a1 发布](#item-harness-arch-6) ⭐️ 7.5/10
7. [Instructor v1.16.0 发布](#item-harness-arch-7) ⭐️ 7.5/10
8. [anthropics/skills 仓库 trending](#item-harness-arch-8) ⭐️ 5.0/10

**Agent 工程师日报**
1. [DeepMind 世界首个双盲 AI 评估试点](#item-agent-engineer-1) ⭐️ 8.5/10
2. [Gemini Omni 1.1 Flash 构建控制增强](#item-agent-engineer-2) ⭐️ 7.5/10
3. [Claude Code Opus 5 Auto Mode 被突破](#item-agent-engineer-3) ⭐️ 7.0/10
4. [PILOT：长时序代理的实时自我改进](#item-agent-engineer-4) ⭐️ 7.0/10
5. [Gemini-3.5-Transcribe 语音识别模型发布](#item-agent-engineer-5) ⭐️ 6.0/10

**AI 日报**
1. [ChatGPT 与批判性思维训练：学生获得更好答案和更广思考](#item-ai-daily-1) ⭐️ 7.5/10
2. [阮一峰周刊 410 期：AI 三种机制](#item-ai-daily-2) ⭐️ 5.0/10

**AI 羊毛**
1. [派早报：智谱开源 GLM-5.3-Flash 原生多模态模型等](#item-ai-deals-1) ⭐️ 6.0/10
2. [AI Engineer Notebooks：免费 Colab RAG/agents/evals 笔记本](#item-ai-deals-2) ⭐️ 5.0/10
3. [JetBrains Junie Mac 本地运行发布](#item-ai-deals-3) ⭐️ 5.0/10

---

## Harness 架构

<a id="item-harness-arch-1"></a>
### [Claude Code v2.1.248 发布](https://github.com/anthropics/claude-code/releases/tag/v2.1.248) ⭐️ 8.5/10

Claude Code v2.1.248 版本发布。该版本添加了受限 harness 模式、提示缓存 TTL、运行器标签自定义和配置诊断。保留了工作目录文件工具，拒绝绕过权限。

github · ashwin-ant · 8月27日 22:12

**「改了什么」** 新增受限模式，该模式移除命令工具和 WebFetch（除非在 --tools 中指定），保留工作目录文件工具并拒绝 bypassPermissions。添加 experimental.cacheTtl 配置以及自托管 runner 客户端标签覆盖。

**标签**: `#tools`, `#permissions`, `#sandbox`, `#memory`, `#runtime`

---

<a id="item-harness-arch-2"></a>
### [FastMCP v4.0.0b5 发布](https://github.com/PrefectHQ/fastmcp/releases/tag/v4.0.0b5) ⭐️ 8.5/10

FastMCP v4.0.0b5 引入 ClientGroup，支持独立管理多个服务器的客户端。
每个客户端可独立协商协议时代，工具名称空间和调用路由支持碰撞检查，且没有代理中间层。
同时，中间件响应限制与输出模式对齐。

github · zzstoatzz · 8月28日 02:57

**「设计要点」** ClientGroup 每个服务器一个客户端，独立协议时代，工具名称空间和调用路由支持碰撞检查，无代理中间层。

**「改了什么」** 相比 v4.0.0b4，新增 ClientGroup 支持独立多服务器客户端管理。
修复了中间件响应限制与输出模式不匹配的问题。

**标签**: `#mcp`, `#tools`, `#runtime`, `#ClientGroup`

---

<a id="item-harness-arch-3"></a>
### [Cloudflare Agents agents@0.22.0 发布](https://github.com/cloudflare/agents/releases/tag/agents%400.22.0) ⭐️ 7.5/10

Cloudflare Agents 0.22.0 发布了 durable chat recovery 的无条件支持，使 AIChatAgent 和 Think 的聊天恢复在 WebSocket、retry 和 continuation 路径上都运行在 recovery fibers 中。Agent 直接扩展 Cloudflare DurableObject，并将 PartyServer 运行时集成到 agents/lifecycle 中。还添加了 Scheduler 作为 Lifecycle 能力，并默认在 useAgentChat 中节流 UI 更新以防止 React 渲染限制。移除已发布的 agents CLI 二进制，使用 C3 starter 和 Wrangler 替代。

github · ben-reitz · 8月27日 14:07

**「设计要点」** Agent 直接扩展 Cloudflare DurableObject，使用 Lifecycle 统一管理启动、请求拦截、报警和 WebSocket；WebSockets 始终使用 Hibernation API。Scheduler 作为可重用的 Lifecycle 能力，管理持久延迟、cron 和 interval 回调。

**「改了什么」** durable chat recovery 现在对所有路径无条件运行，chatRecovery 配置不再支持 false；添加 Scheduler 能力；移除 agents CLI 二进制；优化 useAgentChat 的 UI 更新节流。

**标签**: `#runtime`, `#memory`, `#durable`, `#recovery`

---

<a id="item-harness-arch-4"></a>
### [Cloudflare agents 的 @cloudflare/think@0.17.0 版本发布](https://github.com/cloudflare/agents/releases/tag/%40cloudflare/think%400.17.0) ⭐️ 7.5/10

Cloudflare agents 的 @cloudflare/think@0.17.0 版本发布。Think 0.17.0 将 durable chat recovery 设为 AIChatAgent 和 Think 的无条件操作。所有聊天路径现在使用 recovery fibers，包括 WebSocket、程序化、重试和 continuation 路径。chatRecovery 接受 true 或配置对象；false 不再支持。

github · ben-reitz · 8月27日 14:07

**「设计要点」** 添加 Scheduler，一个可重用的 Lifecycle 能力，用于持久化延迟、日期、cron 和 interval 回调。Scheduler 集成到 Agent 的调度 API 中。

**「改了什么」** durable chat recovery 现在对 AIChatAgent 和 Think 是无条件的。所有聊天路径使用 recovery fibers。chatRecovery 接口不再支持 false 值。

**标签**: `#runtime`, `#memory`, `#recovery`, `#durable`, `#chat`

---

<a id="item-harness-arch-5"></a>
### [cloudflare/agents @cloudflare/ai-chat@0.11.0 发布](https://github.com/cloudflare/agents/releases/tag/%40cloudflare/ai-chat%400.11.0) ⭐️ 7.5/10

cloudflare/agents 发布了 @cloudflare/ai-chat@0.11.0 版本。AIChatAgent 现在在每次聊天回合中运行恢复 fiber，包括 WebSocket、编程、重试和延续路径。chatRecovery 接受 true 或配置对象，false 不再支持。之前编译的 JavaScript 仍会安全接收默认配置。

github · ben-reitz · 8月27日 14:07

**「设计要点」** 运行时使用恢复 fiber 进行无条件持久簿记。onChatRecovery hook 用于处理中断，允许返回 \{ continue: false \} 防止自动推断。使用 durable cancellation、side-effect 或 spend state。

**「改了什么」** 将 AIChatAgent 的持久聊天恢复改为无条件。每个聊天回合现在都在恢复 fiber 中运行。chatRecovery 不再支持 false。

**标签**: `#runtime`, `#memory`, `#durable`, `#recovery`, `#chat`

---

<a id="item-harness-arch-6"></a>
### [LangChain 1.4.0a1 发布](https://github.com/langchain-ai/langchain/releases/tag/langchain%3D%3D1.4.0a1) ⭐️ 7.5/10

LangChain 发布了 1.4.0a1 alpha 版本，重点重构了 MCP 适配器以提升类型安全性和跨服务器协议处理。elicitation 请求类型现在每个模式一个，拒绝 MCP 继续轮询而非轮询。添加了多服务器测试覆盖，并简化了适配器构造。

github · github-actions\[bot\] · 8月27日 22:21

**「设计要点」** MCPAdapter 现在使用单一 elicitation 类型 per mode，提高了类型安全。协议处理在运行时通过 FastMCP 工具驱动多服务器测试覆盖。

**「改了什么」** 相比 1.3.18 版本，1.4.0a1 引入了 MCP 适配器重构：elicitation 类型分离到 per mode/action，拒绝 continuation rounds，简化了适配器构造，并添加了多服务器测试覆盖。

**标签**: `#mcp`, `#runtime`, `#protocol`, `#refactor`, `#test`

---

<a id="item-harness-arch-7"></a>
### [Instructor v1.16.0 发布](https://github.com/567-labs/instructor/releases/tag/v1.16.0) ⭐️ 7.5/10

567-labs/instructor 发布了 v1.16.0。Bedrock 侧补上原生结构化输出：经 Converse 的 \`outputConfig.textFormat\` 显式支持 \`Mode.JSON\_SCHEMA\` 和 \`Mode.TOOLS\_STRICT\`，并做递归 schema 规范化，boto3 最低 \`1.42.42\`，模型仍由调用方选择。校验重试新增正向累计的 \`token\_budget\`，只覆盖结构化非流式路径；\`completion:usage\` 快照不可变，同步与异步截止对齐。有效响应越过预算后仍可返回；一旦配置了预算，失败尝试若拿不到 usage，会在下一次 provider 调用前停掉。

github · github-actions\[bot\] · 8月27日 15:33

**「设计要点」** Bedrock 结构化输出走 Converse 的 \`outputConfig.textFormat\` 和严格 tool schema，schema 会递归规范化。\`token\_budget\` 是跨次重试的累计上限，usage 元数据稳定累加且快照不可变；预算用尽后，已经通过校验的响应仍然有效。

**「改了什么」** 相对上一版，Bedrock 结构化输出改为 Converse 原生 \`Mode.JSON\_SCHEMA\` / \`Mode.TOOLS\_STRICT\`，非流式校验重试可设累计 \`token\_budget\`。同步修了推理文本或 \`&lt;think&gt;\` 块之后的完整 JSON 解析（保留转义、不改调用方消息）、OpenAI 流式 TOOLS/JSON/JSON\_SCHEMA/MD\_JSON 重试、PEP 604 iterable union 按成员解析，以及远程图片/音频/PDF 拉取套用已有 30 秒超时。

**标签**: `#runtime`, `#tools`, `#structured-outputs`, `#bedrock`, `#retry`

---

<a id="item-harness-arch-8"></a>
### [anthropics/skills 仓库 trending](https://github.com/anthropics/skills) ⭐️ 5.0/10

这是 Anthropic 的 Agent Skills 仓库 trending。该仓库定义 skills 为 Claude 动态加载的文件夹，用于特定任务。技能包含指令、脚本和资源，帮助 Claude 重复完成特定任务。

rss · GitHub Trending Daily · 8月28日 05:56

**标签**: `#tools`, `#memory`, `#planning`

---

## Agent 工程师日报

<a id="item-agent-engineer-1"></a>
### [DeepMind 世界首个双盲 AI 评估试点](https://deepmind.google/blog/piloting-the-worlds-first-double-blind-ai-evaluations/) ⭐️ 8.5/10

Google DeepMind 正在试点世界首个双盲 AI 评估。这项举措由官方博客发布，旨在提高 AI 评估的透明度和可靠性。相关领域包括评估 harness 和代理基准测试工作流。目前尚无具体实施细节。

rss · Google DeepMind · 8月27日 12:59

**「为什么重要」** 此试点已发生，将影响 AI 代理工程师和基准测试团队，但其对评估 harness 的影响尚未证实。

**「可关注」** 可关注：世界首个双盲 AI 评估的试点进展。

**标签**: `#eval`, `#harness`, `#benchmark`

---

<a id="item-agent-engineer-2"></a>
### [Gemini Omni 1.1 Flash 构建控制增强](https://deepmind.google/blog/gemini-omni-1-1-flash-lets-you-build-with-more-control/) ⭐️ 7.5/10

Google DeepMind 发布了 Gemini Omni 1.1 Flash，这是一个设计用于提供构建更多控制的模型版本。该更新强调了在构建过程中更大的控制能力。这项发布影响了 AI 代理工程师和工具集成工作流。

rss · Google DeepMind · 8月27日 16:11

**「为什么重要」** 这项更新值得今天关注，因为它提供了构建更多控制的模型版本，可能影响代理的工具集成和架构设计。已发生的是模型版本的发布，尚未证实其对具体工作流的直接影响。

**「可关注」** 可关注：Gemini Omni 1.1 Flash 强调构建控制，这可能影响代理架构和工具集成。

**标签**: `#coding-agent`, `#orchestration`, `#harness`

---

<a id="item-agent-engineer-3"></a>
### [Claude Code Opus 5 Auto Mode 被突破](https://simonwillison.net/2026/Aug/27/breaking-claude-code-opus-5-auto-mode/) ⭐️ 7.0/10

2026 年 8 月 27 日，安全研究员 Johann Rehberger 演示了针对 Claude Code Opus 5 Auto Mode 的攻击方法。该方法诱骗 Claude Code 下载并解压恶意 zip 压缩包，然后执行包含本地 struct.py 文件的代码，成功率约 80%。在部分情况下，Auto Mode 会阻止清理恶意进程的命令，导致有害代码继续执行。这直接挑战了 Anthropic 对 Auto Mode 的保护效果，影响使用 Claude Code 的开发者。

rss · Simon Willison · 8月27日 22:50

**「为什么重要」** 该漏洞显示 Auto Mode 在面对复杂 prompt injection 时仍存在绕过风险，建议用户在运行未托管代理时采用容器或 VM 沙箱以限制网络和权限。

**「可关注」** 可关注：未托管的 coding agents 运行时必须使用容器、VM 或 OS 沙箱，并限制网络出口、监控代理且不暴露敏感目录。

**标签**: `#coding-agent`, `#permissions`

---

<a id="item-agent-engineer-4"></a>
### [PILOT：长时序代理的实时自我改进](https://huggingface.co/papers/2608.26530) ⭐️ 7.0/10

PILOT 是一种用于长时序代理的实时自我改进系统。该系统利用实时涌现的经验来重定向活跃运行并更新持久的 harness，解决了现有方法在执行结束后才处理经验的局限性。单代理自我纠正将任务执行和轨迹评估结合在一个上下文中，而子代理委托则分离了执行但通常无法重定向活跃子代理。PILOT 通过监督者-工作者 harness 实现这一目标，使用两个耦合机制。

rss · Hugging Face Daily Papers · 8月28日 00:00

**「为什么重要」** HF daily paper 提出了 PILOT，这是一项已发生的变化。材料中指出其直接影响代理架构、harness 设计和自我改进工作流，但尚未证实具体影响。

**「可关注」** 可关注：PILOT 采用监督者-工作者 harness，通过两个耦合机制实现 live self-improvement。

**标签**: `#harness`, `#orchestration`, `#eval`, `#coding-agent`

---

<a id="item-agent-engineer-5"></a>
### [Gemini-3.5-Transcribe 语音识别模型发布](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5-transcribe/) ⭐️ 6.0/10

Google 发布了 Gemini-3.5-Transcribe STT 模型。该模型在准确性上优于其他替代方案，但在实时翻译应用中存在延迟问题。模型支持通过 function calling 将复杂任务委托给其他 Gemini 模型，目前在 Gemini macOS 应用中可用。

hackernews · k9294 · 8月27日 18:03 · [社区讨论](https://news.ycombinator.com/item?id=49468818)

**「可关注」** 可关注：Gemini-3.5-Transcribe 准确性突出，但实时应用中延迟是主要挑战。

**「评论」** 用户反馈显示该模型准确性高但延迟较高，部分人推荐 Soniox STT v5 或本地模型 Voxtral。部分用户对模型的 function calling 功能感到困惑。

**标签**: `#eval`, `#orchestration`, `#coding-agent`

---

## AI 日报

<a id="item-ai-daily-1"></a>
### [ChatGPT 与批判性思维训练：学生获得更好答案和更广思考](https://openai.com/index/what-students-gain-from-chatgpt-critical-thinking-training) ⭐️ 7.5/10

OpenAI 发布了一项随机对照研究，涉及超过 1000 名学生。研究考察了 ChatGPT 和批判性思维训练对学生的影响，发现使用这些工具的学生能获得更好答案、更广的思考以及更高的原创性。学生在完成真实世界大学作业时的表现也得到了提升。

rss · OpenAI Blog · 8月27日 09:00

**「可关注」** 可关注：ChatGPT 与批判性思维训练能帮助学生获得更好答案、更广思考和更高原创性，并在真实大学作业中表现更好。

**标签**: `#OpenAI`, `#ChatGPT`, `#education`, `#study`, `#critical thinking`

---

<a id="item-ai-daily-2"></a>
### [阮一峰周刊 410 期：AI 三种机制](http://www.ruanyifeng.com/blog/2026/08/weekly-issue-410.html) ⭐️ 5.0/10

阮一峰科技爱好者周刊第 410 期于本周发布。该期周刊的主题是“你需要知道的 AI 三种机制”。本期作为固定刊物，每周记录值得分享的科技内容。

rss · 阮一峰 · 8月27日 23:56

**「为什么重要」** 本期周刊讨论了 AI 的三种机制，对于科技爱好者了解相关领域很有帮助。

**标签**: `#industry`, `#model`, `#eval`

---

## AI 羊毛

<a id="item-ai-deals-1"></a>
### [派早报：智谱开源 GLM-5.3-Flash 原生多模态模型等](https://sspai.com/post/113922) ⭐️ 6.0/10

智谱 AI 开源 GLM-5.3-Flash 原生多模态模型。该模型支持原生多模态能力，用户可以免费下载使用。

rss · 少数派 · 8月28日 00:29

**标签**: `#free-tier`, `#promo`, `#open-source`

---

<a id="item-ai-deals-2"></a>
### [AI Engineer Notebooks：免费 Colab RAG/agents/evals 笔记本](https://github.com/calmrocks/ai-engineer-notebooks) ⭐️ 5.0/10

calmrocks 分享了 AI Engineer Notebooks 仓库，包含免费且框架-free 的 RAG、agents 和 evals 笔记本。这些可以在 Google Colab 上直接运行，无需额外框架。资源为免费领取。

rss · HN Free API / Credits · 8月27日 21:46

**「可关注」** 可关注：这些笔记本是框架-free 的，直接在 Google Colab 上运行 RAG、agents 和 evals。

**标签**: `#free-tier`, `#colab`, `#rag`, `#agents`, `#evals`

---

<a id="item-ai-deals-3"></a>
### [JetBrains Junie Mac 本地运行发布](https://blog.jetbrains.com/junie/2026/08/junie-local-launch/) ⭐️ 5.0/10

JetBrains 宣布 Junie 可以在 Mac 上本地运行。
无需积分或云端服务。

rss · HN Free API / Credits · 8月27日 11:30

**「可关注」** 可关注：Junie 现可在 Mac 上本地运行，无需积分或云端。

**标签**: `#promo`, `#free-tier`, `#api`, `#mac`

---