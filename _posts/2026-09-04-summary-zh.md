---
layout: default
title: "Horizon Summary: 2026-09-04 (ZH)"
date: 2026-09-04
lang: zh
---

> 从 168 条内容中筛选出 15 条重要资讯。

---

**Harness 架构**
1. [Claude Code v2.1.260 发布](#item-harness-arch-1) ⭐️ 7.8/10
2. [Cline desktop-v0.0.23 发布](#item-harness-arch-2) ⭐️ 7.8/10
3. [pydantic-ai v2.38.0 发布](#item-harness-arch-3) ⭐️ 7.8/10
4. [Agent Framework Python 1.17.0 发布](#item-harness-arch-4) ⭐️ 7.8/10
5. [Cline desktop-v0.0.23-beta.1 发布](#item-harness-arch-5) ⭐️ 6.8/10
6. [Codex rust-v0.153.1 发布](#item-harness-arch-6) ⭐️ 5.8/10
7. [Codex rust-v0.153.0 发布](#item-harness-arch-7) ⭐️ 5.8/10

**Agent 工程师日报**
1. [NeoMME 260M/800M 多模态编码器发布](#item-agent-engineer-1) ⭐️ 7.8/10
2. [GPT-6 Astra 发布，ARC-AGI 99.9%](#item-agent-engineer-2) ⭐️ 7.0/10

**AI 日报**
1. [OpenAI Daybreak $1B 防前线捍卫者](#item-ai-daily-1) ⭐️ 7.8/10
2. [ZGateway 代理上线 ZippyDB](#item-ai-daily-2) ⭐️ 7.8/10
3. [Legora GPT-6 Astra 审查 41 份财报](#item-ai-daily-3) ⭐️ 6.8/10
4. [Playco GPT-6 Astra 原型游戏 手动修复减半](#item-ai-daily-4) ⭐️ 6.8/10
5. [Copilot App 同时运行多个 agents](#item-ai-daily-5) ⭐️ 5.8/10

**AI 羊毛**
1. [CloudCone SSD VPS 补货](#item-ai-deals-1) ⭐️ 7.0/10

---

## Harness 架构

<a id="item-harness-arch-1"></a>
### [Claude Code v2.1.260 发布](https://github.com/anthropics/claude-code/releases/tag/v2.1.260) ⭐️ 7.8/10

Claude Code v2.1.260 发布。该版本在对话界面新增 diff 面板，支持展示 Claude 编辑时的未提交变更并通过 /diff 命令切换。添加 prompt-cache 缺失原因解释，更新 /cost 命令和状态行的 prompt\_cache 字段。新增 /reload-plugins 命令，支持桌面应用和 SDK 会话。

github · ashwin-ant · 9月3日 23:48

**「改了什么」** 新增 diff 面板和 /reload-plugins 命令。新增 advisor 文本命令形式，支持桌面应用、Remote Control 和 headless 会话。

**标签**: `#memory`, `#permissions`, `#tools`, `#runtime`

---

<a id="item-harness-arch-2"></a>
### [Cline desktop-v0.0.23 发布](https://github.com/cline/cline/releases/tag/desktop-v0.0.23) ⭐️ 7.8/10

Cline desktop-v0.0.23 发布了。Agent Plugins 现在由共享的 Hub 发现和执行，使用 plugin.json 验证有效 Agent Skills，并自动启动 stdio/Streamable HTTP/SSE MCP 服务器。Workspace .agents/plugins 目录被忽略。

github · github-actions\[bot\] · 9月3日 18:33

**「设计要点」** Agent Plugins 由共享 Hub 发现和执行。使用 plugin.json 验证，Agent Skills 可用，MCP 服务器自动启动。Workspace .agents/plugins 目录被忽略。

**「改了什么」** Agent Plugins 切换到共享 Hub 管理，使用 plugin.json 验证并自动启动 MCP 服务器。修复了 Hub 更新对话框在每次启动时弹出的问题，以及语音输入设置引导问题。解决了已完成运行的 scheduled-task report 消失问题，以及 wedged MCP 服务器阻塞其他服务器的问题。

**标签**: `#mcp`, `#tools`, `#runtime`, `#plugins`, `#hub`

---

<a id="item-harness-arch-3"></a>
### [pydantic-ai v2.38.0 发布](https://github.com/pydantic/pydantic-ai/releases/tag/v2.38.0) ⭐️ 7.8/10

Pydantic AI v2.38.0 发布。添加运行时事件系统，支持应用代码和能力发射 typed CustomEvent 和 CapabilityEvent，并通过 @on\_event 订阅。新增 context\_window 到 ModelProfile 和 RunContext，更新模型配置文件，支持新 Claude/Gemini 模型。

github · adtyavrdhn · 9月3日 07:48

**「改了什么」** 新增 context\_window 指标和 profile flag，支持 gemini-3.8-flash、claude-fable-5-1、claude-mythos-5-1 模型以及 VLLMProvider。添加 typed CustomEvent 和 CapabilityEvent 发射订阅机制。

**标签**: `#runtime`, `#events`, `#memory`, `#models`, `#capabilities`

---

<a id="item-harness-arch-4"></a>
### [Agent Framework Python 1.17.0 发布](https://github.com/microsoft/agent-framework/releases/tag/python-1.17.0) ⭐️ 7.8/10

Microsoft Agent Framework Python 1.17.0 发布。添加 Foundry 托管 Telegram 代理样本。代理框架核心恢复序列仅代理中间件输入并移除实验性 agent-hooks。支持 OpenAI SDK 3.x 并记录相同事件循环并发合同。

github · moonbox3 · 9月3日 09:49

**「设计要点」** 记录相同事件循环并发合同。

**「改了什么」** 恢复序列仅代理中间件输入并移除实验性 agent-hooks。添加 Foundry Telegram 样本并支持 OpenAI SDK 3.x。

**标签**: `#runtime`, `#tools`, `#memory`

---

<a id="item-harness-arch-5"></a>
### [Cline desktop-v0.0.23-beta.1 发布](https://github.com/cline/cline/releases/tag/desktop-v0.0.23-beta.1) ⭐️ 6.8/10

Cline desktop-v0.0.23-beta.1 发布了。用户可在 Customize → Tools 下配置并选择加入图像生成，凭据保留在服务器端，生成的图像保留在会话历史中。计划运行按本地与 SSH 运行时环境分组。

github · github-actions\[bot\] · 9月3日 01:46

**「改了什么」** 相对于上一版，新增可选图像生成工具。计划运行按本地与 SSH 运行时环境分组。

**标签**: `#tools`, `#runtime`, `#memory`

---

<a id="item-harness-arch-6"></a>
### [Codex rust-v0.153.1 发布](https://github.com/openai/codex/releases/tag/rust-v0.153.1) ⭐️ 5.8/10

Codex rust-v0.153.1 发布了。新增了通过 API 配置 GPT-6-Astra 的支持，不改变默认模型也不在模型选择器中显示。

github · github-actions\[bot\] · 9月3日 21:02

**「改了什么」** 相比 rust-v0.153.0，新增了通过 API 配置 GPT-6-Astra 的支持，不改变默认模型也不在模型选择器中显示。

**标签**: `#tools`, `#planning`, `#memory`

---

<a id="item-harness-arch-7"></a>
### [Codex rust-v0.153.0 发布](https://github.com/openai/codex/releases/tag/rust-v0.153.0) ⭐️ 5.8/10

Codex Rust v0.153.0 发布。新增 Vim 模式支持撤销和重做，保留完整草稿和附件。插件 CLI 支持列出安装移除远程市场插件。TUI 历史显示完整补丁、后台终端输入和完成命令。

github · github-actions\[bot\] · 9月3日 01:37

**「改了什么」** 新增 Vim 模式支持撤销重做。添加插件管理 CLI 和 TUI 历史增强。

**标签**: `#tools`, `#runtime`, `#memory`

---

## Agent 工程师日报

<a id="item-agent-engineer-1"></a>
### [NeoMME 260M/800M 多模态编码器发布](https://huggingface.co/blog/Hcompany/neomme) ⭐️ 7.8/10

NeoMME 引入 260M 和 800M 多语言多模态编码器家族，使用单个双向 Transformer 处理文本 token 和原始图像 patch，并从头开始用 masked discrete-diffusion 目标训练。NeoMME-Retriever 在 ViDoRe v3 Pareto frontier 取得竞争力，在 L40S GPU 上 260M 模型每秒编码约 51 页，存储减少 255 倍。影响评估 harnesses 和多模态工具链。

rss · Hugging Face Blog · 9月3日 13:13

**「为什么重要」** NeoMME 已在 ViDoRe v3 Pareto frontier 取得竞争力，已发生的变化包括高效架构和 255 倍存储减少。影响评估 harnesses 和多模态工具链。

**「可关注」** 可关注：NeoMME-260M 每秒编码约 51 页，是 ColModernVBERT throughput 的两倍；晚期交互索引存储减少 255 倍。

**标签**: `#eval`, `#harness`, `#orchestration`, `#efficiency`, `#retrieval`

---

<a id="item-agent-engineer-2"></a>
### [GPT-6 Astra 发布，ARC-AGI 99.9%](https://simonwillison.net/2026/Sep/3/gpt6-astra/) ⭐️ 7.0/10

GPT-6 Astra 今日开始向 ChatGPT Plus、Pro、Business 和 Enterprise 用户以及 OpenAI API 有限组织 rollout，未来几天将全面开放至所有用户。API 定价为每百万输入 $10、输出 $50，与 Claude Fable 5 相同。ARC-AGI 3 基准测试得分达到 99.9%，使用 Provider Adapter harness 实现，该 harness 保留不透明推理状态并使用 compaction 支持长对话。

rss · Simon Willison · 9月3日 20:18

**「为什么重要」** GPT-6 Astra 发布影响 ChatGPT Plus/Pro/Business/Enterprise 用户和 OpenAI API 用户。ARC-AGI 3 99.9% 得分和长上下文处理能力提升值得关注。

**「可关注」** 可关注：ARC-AGI 3 99.9% 得分使用 Provider Adapter harness 实现，支持长对话。

**「评论」** 评论：社区对 ARC-AGI 3 99.9% 得分存在质疑，有人认为 harness 使用不透明导致分数 misleading；部分用户建议关注 OpenAI 官方公告。

**标签**: `#eval`, `#harness`, `#benchmark`, `#api-pricing`, `#model-release`

---

## AI 日报

<a id="item-ai-daily-1"></a>
### [OpenAI Daybreak $1B 防前线捍卫者](https://openai.com/index/daybreak-for-frontline-defenders) ⭐️ 7.8/10

OpenAI 推出 Daybreak for Frontline Defenders 计划。
该计划投入 10 亿美元，扩大对前沿网络安全 AI、培训和支持的访问。
服务对象是前线捍卫者和关键服务。

rss · OpenAI Blog · 9月3日 13:15

**「可关注」** 可关注：$1B 投入前沿网络安全 AI、培训和支持。

**标签**: `#openai`, `#policy`, `#industry`, `#product`

---

<a id="item-ai-daily-2"></a>
### [ZGateway 代理上线 ZippyDB](https://engineering.fb.com/2026/09/03/core-infra/zgateway-proxy-zippydb-meta/) ⭐️ 7.8/10

Meta 推出 ZGateway 代理，用于统一通过 ZippyDB 的流量。ZippyDB 是 Meta 最广泛使用的键值存储，支持产品元数据、计数器和配置，可服务数十亿请求。作为额外功能，ZGateway 还提供了准入控制、负载均衡、跨区域弹性和更丰富的操作。

rss · Engineering at Meta · 9月3日 16:00

**「为什么重要」** ZGateway 代理的引入有助于 Meta 提升核心 KV 存储的流量管理能力。

**「可关注」** 可关注：准入控制、负载均衡、跨区域弹性和更丰富操作。

**标签**: `#lab`, `#industry`, `#product`

---

<a id="item-ai-daily-3"></a>
### [Legora GPT-6 Astra 审查 41 份财报](https://openai.com/index/legora-financial-statement-review-with-astra) ⭐️ 6.8/10

Legora 使用 GPT-6 Astra 审查 41 份财务文件，仅用几分钟就完成。检测到所有 4 个植入错误。工作流性能提升近 40%。

rss · OpenAI Blog · 9月3日 12:00

**「为什么重要」** Legora 的案例展示了 GPT-6 Astra 在财务审查工作流中的高效应用。

**「可关注」** Legora 使用 GPT-6 Astra 审查 41 份财务文件，检测到所有 4 个植入错误，提升工作流性能近 40%。

**标签**: `#model`, `#lab`, `#industry`, `#eval`, `#product`

---

<a id="item-ai-daily-4"></a>
### [Playco GPT-6 Astra 原型游戏 手动修复减半](https://openai.com/index/playco-game-prototyping-with-astra) ⭐️ 6.8/10

Playco 使用 GPT-6 Astra，从一个灰盒基础构建了三个主题游戏原型。与前一个模型相比，手动修复数量减少了 50%。

rss · OpenAI Blog · 9月3日 12:00

**「为什么重要」** Playco 的案例展示了 GPT-6 Astra 在游戏原型制作中的效率提升。

**「可关注」** 「可关注：Playco 使用 GPT-6 Astra 构建游戏原型，手动修复减少 50%。」

**标签**: `#model`, `#lab`, `#industry`, `#product`

---

<a id="item-ai-daily-5"></a>
### [Copilot App 同时运行多个 agents](https://github.blog/ai-and-ml/github-copilot/github-copilot-app-for-beginners-run-several-agents-at-once/) ⭐️ 5.8/10

GitHub 博客发布 Copilot App 教程，教用户如何同时运行多个 agents。文章强调使用并行 agents 后，工具从“可怕”变成“强大”。这是官方入门指南，帮助初学者掌握多 agents 功能。

rss · GitHub Blog · 9月3日 16:00

**「为什么重要」** 这篇博客帮助初学者快速上手 Copilot App 的多 agents 功能，让工具从“可怕”变成“强大”。

**「可关注」** 可关注：Copilot App 支持同时运行多个 agents

**标签**: `#github`, `#copilot`, `#agents`, `#product`, `#ai`

---

## AI 羊毛

<a id="item-ai-deals-1"></a>
### [CloudCone SSD VPS 补货](https://www.appinn.com/cloudcone-ssd-vps/) ⭐️ 7.0/10

CloudCone 发来 Turns 9 Sale 活动补货提醒。最低档年付只需 96 元（14.24 美元），支持支付宝。推荐两个套餐，均包含 1 个 IPv4 和 3 个 IPv6。

rss · 小众软件 · 9月3日 09:07

**「可关注」** 可关注：关注 CloudCone Turns 9 Sale 补货，最低 96 元/年，年付支持支付宝。

**标签**: `#promo`, `#coupon`, `#sale`

---