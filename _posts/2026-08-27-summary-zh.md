---
layout: default
title: "Horizon Summary: 2026-08-27 (ZH)"
date: 2026-08-27
lang: zh
---

> 从 153 条内容中筛选出 14 条重要资讯。

---

**Harness 架构**
1. [Codex rust-v0.150.0 发布](#item-harness-arch-1) ⭐️ 7.5/10
2. [Cline SDK v0.0.81 发布](#item-harness-arch-2) ⭐️ 7.5/10
3. [Cline desktop-v0.0.19 发布](#item-harness-arch-3) ⭐️ 7.5/10
4. [google/adk-python v2.8.0 发布](#item-harness-arch-4) ⭐️ 7.5/10
5. [mastra-ai/mastra @mastra/core@1.62.0 发布](#item-harness-arch-5) ⭐️ 7.5/10
6. [Cline SDK v0.0.80 发布](#item-harness-arch-6) ⭐️ 6.5/10
7. [Cline CLI v3.0.60 发布](#item-harness-arch-7) ⭐️ 6.5/10

**Agent 工程师日报**
1. [Qwen3.8-Flash-Next 多模态 MoE 模型](#item-agent-engineer-1) ⭐️ 6.0/10
2. [研究者改编 Dolma 构建 Mangosteen 泰国语料库](#item-agent-engineer-2) ⭐️ 5.5/10

**AI 日报**
1. [ChatGPT for Teachers 扩展至 55 个美国学区](#item-ai-daily-1) ⭐️ 7.5/10
2. [OpenAI 报告：AI 让学习持续不断](#item-ai-daily-2) ⭐️ 6.5/10

**AI 羊毛**
1. [Unreal Tournament 2004 免费获取](#item-ai-deals-1) ⭐️ 6.0/10
2. [lookaal.dev 免费 API 聚合荷兰政府数据集](#item-ai-deals-2) ⭐️ 5.0/10
3. [Superwhisper 免费语音输入功能上线](#item-ai-deals-3) ⭐️ 5.0/10

---

## Harness 架构

<a id="item-harness-arch-1"></a>
### [Codex rust-v0.150.0 发布](https://github.com/openai/codex/releases/tag/rust-v0.150.0) ⭐️ 7.5/10

这是 Codex 的 rust-v0.150.0 版本。该版本新增了任务引用、终端增强、权限控制和中断钩子等功能。保留了之前的接口和限制。

github · github-actions\[bot\] · 8月26日 19:37

**「改了什么」** 相比 rust-v0.149.0，主要增加了任务 @-mentions 支持、终端任务自动标题和权限快捷键绑定。修复了 AGENTS.md 指令限制和 deny-read 规则 enforcement。

**标签**: `#runtime`, `#permissions`, `#tools`, `#subagents`, `#mcp`

---

<a id="item-harness-arch-2"></a>
### [Cline SDK v0.0.81 发布](https://github.com/cline/cline/releases/tag/sdk/sdk/v0.0.81) ⭐️ 7.5/10

Cline SDK v0.0.81 发布了。该版本将 session snapshot 事件中的完整对话历史移除，仅保留状态信息。转录内容通过 \`session.messages\` 命令单独获取。这减少了事件大小，减轻了 durable event log flooding，并降低了 per-event 内存拷贝。

github · github-actions\[bot\] · 8月26日 09:38

**「设计要点」** 会话快照事件现在仅包含状态信息（status/usage/model/workspace/checkpoint），转录通过 \`session.messages\` 命令获取。这减少了事件大小、durable log flooding 和 per-event 内存拷贝。

**「改了什么」** 相对 v0.0.80，\`session.updated\`（以及 \`session.created\` / \`session.detached\` / \`run.started\`）事件不再嵌入完整消息历史。快照现在仅为状态信息，转录通过 \`session.messages\` 命令获取。

**标签**: `#runtime`, `#memory`

---

<a id="item-harness-arch-3"></a>
### [Cline desktop-v0.0.19 发布](https://github.com/cline/cline/releases/tag/desktop-v0.0.19) ⭐️ 7.5/10

Cline desktop-v0.0.19 发布了。该版本优化了后台进程在长会话中的内存使用，并刷新了支持的 AI 模型提供商。
状态更新现在只携带状态，转录在需要时才获取，以防止进程在长会话中膨胀。
模型目录已刷新，新增七个提供商并更新了默认模型。

github · github-actions\[bot\] · 8月26日 09:31

**「设计要点」** 设计要点是运行时内存模型的更改。状态更新现在只携带状态（status, usage, model, workspace, checkpoint），转录在需要时才获取。

**「改了什么」** 此版本修复了后台进程在长会话中的内存膨胀问题。状态更新现在只携带状态，转录在需要时才获取。此外，刷新了模型目录，新增了七个提供商并更新了默认模型。

**标签**: `#runtime`, `#memory`, `#tools`

---

<a id="item-harness-arch-4"></a>
### [google/adk-python v2.8.0 发布](https://github.com/google/adk-python/releases/tag/v2.8.0) ⭐️ 7.5/10

Google ADK Python v2.8.0 发布。该版本新增数据代理管理工具，包括创建、删除、列出和更新数据代理的功能。添加了 ADK\_MAX\_LLM\_CALLS 环境变量来配置 LLM 调用限制，并支持 A2A 原生任务模式和 Model Armor guardrail 插件。

github · wukath · 8月26日 23:25

**「改了什么」** 相比 v2.7.1，主要增加了数据代理管理工具和 A2A 原生任务支持，并允许通过环境变量配置 LLM 调用限制。

**标签**: `#tools`, `#runtime`, `#a2a`, `#guardrail`

---

<a id="item-harness-arch-5"></a>
### [mastra-ai/mastra @mastra/core@1.62.0 发布](https://github.com/mastra-ai/mastra/releases/tag/%40mastra/core%401.62.0) ⭐️ 7.5/10

mastra-ai/mastra 发布了 @mastra/core@1.62.0 版本。该版本新增了 Elasticsearch + Valkey 存储后端，支持内存、工作流快照、评分和语义召回等功能。同时引入了计算机使用沙箱能力，并提供了新的 E2B Desktop 提供者。沙箱还增加了运行时环境控制和更安全的关闭行为。

github · PaulieScanlon · 8月26日 13:40

**「改了什么」** 相比上一版，新增了 Elasticsearch + Valkey 存储后端和计算机使用沙箱支持。沙箱拥有了运行时 env 控制功能，并改进了 shutdown 行为。

**标签**: `#runtime`, `#sandbox`, `#storage`, `#tools`, `#memory`

---

<a id="item-harness-arch-6"></a>
### [Cline SDK v0.0.80 发布](https://github.com/cline/cline/releases/tag/sdk/sdk/v0.0.80) ⭐️ 6.5/10

Cline SDK v0.0.80 已发布。该版本支持文件工具使用平台原生换行符，修复了 search\_codebase 工具在处理单一大行文件时崩溃的问题，并对 git 远程 URL 中的凭证进行了重定向处理。还更新了 Claude Code 的订阅处理方式，并刷新了模型目录，添加了七个新的 AI 提供商。

github · github-actions\[bot\] · 8月26日 08:45

**「改了什么」** 相对于上一版，Cline SDK v0.0.80 增加了文件工具的原生换行支持，并修复了 search\_codebase 工具的崩溃问题。模型目录也进行了刷新，添加了七个提供商并调整了默认模型。

**标签**: `#runtime`, `#tools`, `#mcp`, `#permissions`, `#eval`

---

<a id="item-harness-arch-7"></a>
### [Cline CLI v3.0.60 发布](https://github.com/cline/cline/releases/tag/cli-v3.0.60) ⭐️ 6.5/10

Cline CLI v3.0.60 发布了。该版本修复了后台 hub 进程在长会话中的内存膨胀问题，之前会话状态更新会广播完整对话记录到所有客户端，导致进程占用数十 GB 内存。还修复了代码库搜索工具在含巨大单行文件的崩溃问题，并修复了 MCP 服务器安装参数解析错误。

github · github-actions\[bot\] · 8月26日 09:43

**「设计要点」** 后台 hub 进程通过广播完整会话 transcript 导致内存膨胀，v3.0.60 版本通过升级重启运行中的 hub 来应用修复。

**「改了什么」** v3.0.60 相比 v3.0.59 修复了后台 hub 内存膨胀问题，并修复了代码库搜索工具崩溃以及 MCP 安装解析错误。模型目录刷新，添加了七个提供商并更新了默认模型。

**标签**: `#runtime`, `#memory`, `#tools`, `#mcp`

---

## Agent 工程师日报

<a id="item-agent-engineer-1"></a>
### [Qwen3.8-Flash-Next 多模态 MoE 模型](https://simonwillison.net/2026/Aug/26/qwen38-flash-next/) ⭐️ 6.0/10

Simon Willison 评测了 Qwen3.8-Flash-Next 多模态 MoE 模型，该模型是 Qwen4 架构的早期预览。该模型总大小 125B tokens，仅激活 6B。作者在 DGX Spark 上使用 Unsloth GGUF 量化版本进行了实验，生成图像示例。

rss · Simon Willison · 8月26日 23:52

**「可关注」** 可关注：Qwen3.8-Flash-Next 的 GGUF 量化版本在 DGX Spark 硬件上可用于图像生成。

**标签**: `#coding-agent`, `#harness`, `#orchestration`, `#eval`

---

<a id="item-agent-engineer-2"></a>
### [研究者改编 Dolma 构建 Mangosteen 泰国语料库](https://allenai.org/blog/thai-llm-dolma) ⭐️ 5.5/10

研究者改编了 Ai2 的开源 Dolma 工具包，构建了 Mangosteen，一个包含 47 亿 token 的泰国语料库。该语料库通过过滤低质量网络数据来保持或改善模型性能，并加强了泰国文化知识。

rss · Allen AI · 8月26日 08:00

**「为什么重要」** 该改编展示了如何使用开源 Dolma 工具包优化特定语言的语料库，这对构建支持多语言的语言模型有参考价值。

**「可关注」** 可关注：使用 Dolma 工具包过滤低质量数据来构建多语言语料库。

**标签**: `#harness`, `#eval`, `#orchestration`

---

## AI 日报

<a id="item-ai-daily-1"></a>
### [ChatGPT for Teachers 扩展至 55 个美国学区](https://openai.com/index/bringing-chatgpt-for-teachers-to-more-us-school-districts) ⭐️ 7.5/10

OpenAI 将 ChatGPT for Teachers 扩展至 55 个美国学区。该计划将为超过 10 万名教育工作者和员工提供安全 AI 工具、培训和支持。

rss · OpenAI Blog · 8月26日 10:00

**「可关注」** 可关注：ChatGPT for Teachers 扩展至 55 个美国学区，服务超过 10 万名教育工作者和员工。

**标签**: `#lab`, `#industry`, `#policy`, `#product`

---

<a id="item-ai-daily-2"></a>
### [OpenAI 报告：AI 让学习持续不断](https://openai.com/index/learning-never-stops) ⭐️ 6.5/10

OpenAI 发布了新报告，探讨了学生和教育工作者如何使用 ChatGPT 实现持续学习。该报告强调学习支持可以超越课堂范围。报告基于实际使用案例，展示了 AI 在教育中的应用。

rss · OpenAI Blog · 8月26日 10:00

**「为什么重要」** 报告为教育领域提供了 AI 应用的参考案例，有助于理解 AI 如何支持持续学习。

**标签**: `#lab`, `#industry`, `#product`

---

## AI 羊毛

<a id="item-ai-deals-1"></a>
### [Unreal Tournament 2004 免费获取](https://www.pcgamer.com/games/fps/unreal-tournament-2004-is-now-available-for-free-thanks-to-its-fan-community-and-theyve-even-updated-the-game-for-modern-pcs-this-is-the-first-public-patch-for-unreal-tournament-2004-in-over-20-years/) ⭐️ 6.0/10

Unreal Tournament 2004 现由粉丝社区免费提供，已更新以适配现代 PC。这是 20 多年来首次公开补丁。可通过粉丝社区免费领取，适用于现代 PC。

rss · HN Free API / Credits · 8月26日 15:54

**「可关注」** 可关注：游戏已更新以支持现代 PC，适用于现代电脑。

**标签**: `#promo`, `#limited-free`

---

<a id="item-ai-deals-2"></a>
### [lookaal.dev 免费 API 聚合荷兰政府数据集](https://lookaal.dev/) ⭐️ 5.0/10

lookaal.dev 提供了一个免费 API，将六个荷兰政府数据集整合成一个 REST 端点。
目前未提供公开的额度限制、模型或价格信息。
领取条件和截止时间未在材料中提及。

rss · HN Free API / Credits · 8月26日 21:52

**标签**: `#free-tier`, `#api`, `#promo`

---

<a id="item-ai-deals-3"></a>
### [Superwhisper 免费语音输入功能上线](https://twitter.com/superwhisper/status/2092660873311436832) ⭐️ 5.0/10

Superwhisper 刚刚上线免费语音输入功能。用户可以免费使用该功能进行语音转文字。材料中未提及具体额度、截止时间或领取条件。

rss · HN Free API / Credits · 8月26日 18:46

**「可关注」** 可关注：Superwhisper 免费语音输入功能已上线，用户可免费使用进行语音转文字。

**标签**: `#free-tier`, `#promo`, `#limited-free`

---