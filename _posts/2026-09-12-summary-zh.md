---
layout: default
title: "Horizon Summary: 2026-09-12 (ZH)"
date: 2026-09-12
lang: zh
---

> 从 149 条内容中筛选出 16 条重要资讯。

---

**Harness 架构**
1. [Cloudflare agents 0.23.0 发布](#item-harness-arch-1) ⭐️ 8.8/10
2. [Cloudflare agents @cloudflare/ai-chat@0.12.0 发布](#item-harness-arch-2) ⭐️ 8.8/10
3. [DSPy 3.4.0b1 发布](#item-harness-arch-3) ⭐️ 8.8/10
4. [Mastra @mastra/core 1.66.0 发布](#item-harness-arch-4) ⭐️ 7.8/10
5. [Agent Framework dotnet-1.21.0 发布](#item-harness-arch-5) ⭐️ 7.8/10
6. [Claude Code v2.1.269 发布](#item-harness-arch-6) ⭐️ 6.8/10
7. [Cloudflare Agents @cloudflare/codemode@0.5.2 发布](#item-harness-arch-7) ⭐️ 6.8/10
8. [huggingface/speech-to-speech 语音代理](#item-harness-arch-8) ⭐️ 5.0/10
9. [Letta Code GitHub trending](#item-harness-arch-9) ⭐️ 5.0/10

**Agent 工程师日报**
1. [Devin Desktop &amp; CLI 引入 Fusion](#item-agent-engineer-1) ⭐️ 8.8/10
2. [OpenRouter 路由不一致 需显式选择](#item-agent-engineer-2) ⭐️ 6.0/10
3. [wrapture Python 包发布](#item-agent-engineer-3) ⭐️ 6.0/10

**AI 日报**
1. [OpenAI 存储扩展服务 10 亿 ChatGPT](#item-ai-daily-1) ⭐️ 9.8/10
2. [GPT-6 Astra 助力 Devin 测试](#item-ai-daily-2) ⭐️ 7.8/10
3. [GitHub 营销 ops 代码化](#item-ai-daily-3) ⭐️ 5.8/10

**AI 羊毛**
1. [Epic Games 送 LUFTRAUSERS Astral Ascent Alone With You](#item-ai-deals-1) ⭐️ 6.0/10

---

## Harness 架构

<a id="item-harness-arch-1"></a>
### [Cloudflare agents 0.23.0 发布](https://github.com/cloudflare/agents/releases/tag/agents%400.23.0) ⭐️ 8.8/10

Cloudflare agents 0.23.0 重构了 facet/sub-agent 机制，提取约 2400 行代码到 dynamic-agents 模块，作为 Lifecycle capability 注册，并添加了 this.dynamicAgents facade，将 facets 定位为隔离原语。新增 RoutedAgents 能力，支持用户 hub 与每个聊天一个 Durable Object 的拓扑。Lifecycle 拥有 durable job queue，由 alarm event loop 驱动，移除了 pull-based alarm 模型。

github · github-actions\[bot\] · 9月11日 10:42

**「设计要点」** 将 facet 路由和 WebSocket 转发等代码提取到专用模块，并作为 Lifecycle 能力注册；新增 RoutedAgents 能力用于 Durable Object 路由；Lifecycle 驱动模式改为 job queue 事件循环。

**「改了什么」** 将 sub-agent 机制重构为 dynamic-agents 能力 facade，新增 RoutedAgents 能力，并将 Lifecycle 驱动改为 durable job queue，移除了 pull-based alarm 模型。

**标签**: `#runtime`, `#subagents`, `#dynamic-agents`, `#capability`, `#facets`

---

<a id="item-harness-arch-2"></a>
### [Cloudflare agents @cloudflare/ai-chat@0.12.0 发布](https://github.com/cloudflare/agents/releases/tag/%40cloudflare/ai-chat%400.12.0) ⭐️ 8.8/10

Cloudflare agents 发布了 @cloudflare/ai-chat@0.12.0 版本。该版本将 AIChatAgent 消息存储切换到 agents/sessions 模块，同时保留 mutable messages 数组、destructive regeneration 等功能。运行时行为变更包括构造函数不再同步加载消息 transcript，直到 onStart 回调才初始化消息数组。流处理和恢复机制也进行了优化。

github · github-actions\[bot\] · 9月11日 10:42

**「改了什么」** AIChatAgent 消息存储从 legacy table 切换到 sessions，支持迁移策略。运行时变更包括消息数组在构造函数中为空直到 onStart，流处理从 buffer sweeps 改为 rollover block log，恢复机制改为 chained Tasks。

**标签**: `#runtime`, `#memory`, `#sessions`, `#migration`

---

<a id="item-harness-arch-3"></a>
### [DSPy 3.4.0b1 发布](https://github.com/stanfordnlp/dspy/releases/tag/3.4.0b1) ⭐️ 8.8/10

DSPy 3.4.0b1 beta 版发布。这是 3.4 系列首个 beta 版。DSPy 将语言模型执行移动到共享引擎接口，添加本地 CPython 解释器，并为 ReActV2 带来异步执行。修复了评估、流式传输和演示采样 bug。

github · isaacbmiller · 9月11日 22:24

**「设计要点」** LM 执行使用共享引擎接口。LocalInterpreter 提供持久 CPython 环境。ReActV2 支持异步调用。

**「改了什么」** 3.4.0b1 替换 3.3 实验 LM 类型。引入 LocalInterpreter 和 async ReActV2。GEPA 支持自定义代码提案。

**标签**: `#runtime`, `#sandbox`, `#eval`, `#tools`, `#planning`

---

<a id="item-harness-arch-4"></a>
### [Mastra @mastra/core 1.66.0 发布](https://github.com/mastra-ai/mastra/releases/tag/%40mastra/core%401.66.0) ⭐️ 7.8/10

Mastra 发布了 @mastra/core 1.66.0 版本。该版本引入了通过 workers.json 进行云端 worker 预配的功能，支持专用 orchestration/scheduler/background/custom workers。还丰富了 trace 过滤，支持 span 字段、metadata、feedback 和 scores 的谓词，并添加了 feedback/scores 的删除功能。

github · PaulieScanlon · 9月11日 09:37

**「设计要点」** 新增了 Observational Memory transform hooks，允许应用在 observation 和 reflection 前后进行异步 transform 以支持消息过滤、redact 或 reshape。

**「改了什么」** 1.66.0 版本相对上一版，新增了云 worker provisioning via workers.json、richer trace filtering 以及 feedback/scores deletion 等能力。

**标签**: `#runtime`, `#eval`, `#storage`

---

<a id="item-harness-arch-5"></a>
### [Agent Framework dotnet-1.21.0 发布](https://github.com/microsoft/agent-framework/releases/tag/dotnet-1.21.0) ⭐️ 7.8/10

Agent Framework dotnet-1.21.0 发布。更新了 A2A 协议和运行时，包括文件访问的重大变更。新增了文件访问读取行数功能，并将行号记录合同移至 AgentFileStore。

github · SergeyMenshykh · 9月11日 17:31

**「改了什么」** 1.21.0 相比 1.20.0，增加了文件访问读取行数支持和 A2A 任务状态跟踪。Azure AI Projects 更新至 3.0 beta，AWS Bedrock SDK 替换完成。

**标签**: `#mcp`, `#runtime`, `#breaking`, `#tools`, `#azure`

---

<a id="item-harness-arch-6"></a>
### [Claude Code v2.1.269 发布](https://github.com/anthropics/claude-code/releases/tag/v2.1.269) ⭐️ 6.8/10

Claude Code v2.1.269 发布。新增 \`claude plugin eval\` 工具，可运行插件的评估套件并生成可复现的 JSON + HTML 报告。新增 \`/output-style \[name\]\` 命令，支持在远程控制和云端会话中切换输出样式。新增 \`CLAUDE\_CODE\_WORKFLOW\_MAX\_CONCURRENT\_AGENTS\` 配置（范围 1–256），以调整 Workflow 工具的并发代理限制。

github · ashwin-ant · 9月11日 19:17

**「改了什么」** 相对于上一版，新增了插件评估功能、输出样式切换、Bash 工具文件编辑差异显示、OTEL 指标仓库标签以及 Workflow 工具并发代理限制。修复了多个终端兼容性、会话恢复和插件加载问题。

**标签**: `#eval`, `#tools`, `#subagents`, `#runtime`

---

<a id="item-harness-arch-7"></a>
### [Cloudflare Agents @cloudflare/codemode@0.5.2 发布](https://github.com/cloudflare/agents/releases/tag/%40cloudflare/codemode%400.5.2) ⭐️ 6.8/10

Cloudflare Agents 发布了 @cloudflare/codemode@0.5.2 版本。
该版本改进工具结果的结构化截断。
之前 truncateResult 和 transformResult 使用 JSON 切片，留下半份 JSON 文档。
现在改为原地结构化截断，字符串加 --- TRUNCATED --- 后缀，数组和对象按预算优先级截断，输出始终有效 JSON。

github · github-actions\[bot\] · 9月11日 10:42

**「设计要点」** 工具层 truncateResult 结构化截断保持 JSON 形状，减少模型 token 浪费。Code Mode 工具投影 calls 出模型上下文并界定 sandbox logs。

**「改了什么」** @cloudflare/codemode@0.5.2 改进了工具结果截断方式，修复了 oversized JSON 相关问题。

**标签**: `#runtime`, `#tools`, `#mcp`

---

<a id="item-harness-arch-8"></a>
### [huggingface/speech-to-speech 语音代理](https://github.com/huggingface/speech-to-speech) ⭐️ 5.0/10

huggingface/speech-to-speech 是 hugging Face 的语音代理项目。它提供低延迟全模块化语音代理管道，通过 OpenAI Realtime API 事件在 WebSocket/WebRTC 上暴露。管道由 VAD -&gt; STT -&gt; LLM -&gt; TTS 组成，每个组件可替换。LLM 支持 OpenAI 兼容协议，可指向托管提供商或本地 vLLM/llama.cpp 服务器。

rss · GitHub Trending Daily · 9月12日 00:50

**「设计要点」** 运行时通过 WebSocket/WebRTC 暴露 OpenAI Realtime API。组件可互换，LLM 部分支持 vLLM 和 llama.cpp。

**标签**: `#runtime`, `#tools`, `#subagents`

---

<a id="item-harness-arch-9"></a>
### [Letta Code GitHub trending](https://github.com/letta-ai/letta-code) ⭐️ 5.0/10

Letta Code 在 GitHub trending 榜单上走红。这是一个状态化代理 harness，代理更像人而非工具。Letta Code 代理拥有记忆、身份和随时间积累的经验。他们通过重写自己的记忆、技能、提示甚至 harness（通过 mods）在长期范围内学习和进化。

rss · GitHub Trending Daily · 9月12日 00:50

**标签**: `#memory`, `#runtime`

---

## Agent 工程师日报

<a id="item-agent-engineer-1"></a>
### [Devin Desktop &amp; CLI 引入 Fusion](https://cognition.ai/blog/local-fusion) ⭐️ 8.8/10

Cognition 在 Devin Desktop 和 CLI 中引入 Fusion 双模型 harness。
Fusion 采用 frontier lead 模型进行规划和审查，搭配 cost-effective sidekick 执行模型。
Fusion 在多个 coding benchmarks 上实现最高 46% 成本节省，同时维持 frontier 性能。
该功能已于今日在 Devin Desktop 和 CLI 中可用。

rss · Cognition Blog · 9月11日 17:00

**「为什么重要」** Fusion 降低 Devin Desktop 和 CLI 的 coding 任务运行成本。

**「可关注」** 可关注：使用更强 sidekick 模型可降低整体成本。

**标签**: `#harness`, `#eval`, `#coding-agent`, `#orchestration`

---

<a id="item-agent-engineer-2"></a>
### [OpenRouter 路由不一致 需显式选择](https://simonwillison.net/2026/Sep/11/so-you-want-to-use-openrouter/) ⭐️ 6.0/10

OpenRouter 提供自动路由和成本优化，但不同提供商的服务软件和优化设置不同，导致同一端点行为不一致。部分提供商不支持视觉模型，推理努力选项处理方式也存在差异。使用 provider.only 选项可显式选择提供商以确保一致模型行为。这直接影响代理编排和评估 harness 的可靠性。

rss · Simon Willison · 9月11日 22:49

**「为什么重要」** OpenRouter 的路由不一致可能导致代理行为不稳定，影响评估 harness 的可重复性。显式提供商选择是可靠的解决方案。

**「可关注」** 可关注：使用 provider.only 显式指定提供商以避免路由不一致。

**标签**: `#orchestration`, `#coding-agent`, `#eval`, `#provider-routing`, `#harness`

---

<a id="item-agent-engineer-3"></a>
### [wrapture Python 包发布](https://simonwillison.net/2026/Sep/11/wrapture/) ⭐️ 6.0/10

Graham Dumpleton 发布了 wrapture Python 包，这是一个支持猴子补丁的库，可同时用于单元测试和 New Relic 风格的观测性追踪。自 2026 年 8 月 31 日初始发布以来，Graham 每天发布新教程。目前为 alpha 软件，可通过 TOML 文件配置无需修改 Python 代码。

rss · Simon Willison · 9月11日 13:51

**「为什么重要」** wrapture 包已发布，值得 Python 开发者关注其在测试和观测性中的应用。

**「可关注」** 可关注：wrapture 支持通过 TOML 文件配置追踪，无需修改 Python 代码。

**标签**: `#harness`, `#observability`, `#coding-agent`, `#eval`, `#testing`

---

## AI 日报

<a id="item-ai-daily-1"></a>
### [OpenAI 存储扩展服务 10 亿 ChatGPT](https://openai.com/index/scaling-storage-one-billion-users-part-one) ⭐️ 9.8/10

OpenAI 将 Habitat 库从 Python 库演变为全球分布式存储平台。目前平台服务于超过 10 亿 ChatGPT 用户，每秒处理 2200 万次请求。

rss · OpenAI Blog · 9月11日 10:00

**「为什么重要」** OpenAI 分享了存储扩展的内部实践，对理解 ChatGPT 后端基础设施有参考价值。

**「可关注」** 可关注：Habitat 库从 Python 库演变为全球分布式存储平台。

**标签**: `#openai`, `#chatgpt`, `#infrastructure`, `#storage`, `#scaling`

---

<a id="item-ai-daily-2"></a>
### [GPT-6 Astra 助力 Devin 测试](https://openai.com/index/cognition-devin-testing-with-astra) ⭐️ 7.8/10

GPT-6 Astra 提升 Devin 测试软件的能力，并展示其工作有效性。目标是帮助工程师审查更少代码，从而更快发布。

rss · OpenAI Blog · 9月11日 16:00

**「为什么重要」** Devin 测试软件并展示其工作有效性有助于工程师审查更少代码，加快发布。

**「可关注」** 可关注：使用 GPT-6 Astra 提升 Devin 测试软件的能力

**标签**: `#model`, `#lab`, `#product`

---

<a id="item-ai-daily-3"></a>
### [GitHub 营销 ops 代码化](https://github.blog/ai-and-ml/github-copilot/marketing-ops-as-code-automating-events-from-planning-to-follow-up-on-github/) ⭐️ 5.8/10

GitHub blog post 介绍了 APAC 营销团队如何使用 GitHub 工具自动化事件从规划到跟进。团队通过代码化方式支持营销运营。

rss · GitHub Blog · 9月11日 18:26

**「为什么重要」** GitHub 营销自动化案例展示了 GitHub 工具在营销运营中的实际应用。

**「可关注」** 可关注：使用 GitHub 工具自动化营销活动

**标签**: `#product`, `#github`, `#copilot`, `#marketing`, `#automation`

---

## AI 羊毛

<a id="item-ai-deals-1"></a>
### [Epic Games 送 LUFTRAUSERS Astral Ascent Alone With You](https://www.appinn.com/eggs-26911/) ⭐️ 6.0/10

Epic Games 9.11~9.17 免费送出 LUFTRAUSERS、Astral Ascent 和 Alone With You 三款游戏。两款是电脑游戏，一款是手机游戏。电脑游戏为《天空奇兵 / LUFTRAUSERS》和《星界战士 / Astral Ascent》，手机游戏为《Alone With You》。

rss · 小众软件 · 9月11日 07:48

**标签**: `#promo`, `#limited-free`, `#free-game`

---