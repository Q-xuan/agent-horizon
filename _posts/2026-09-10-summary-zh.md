---
layout: default
title: "Horizon Summary: 2026-09-10 (ZH)"
date: 2026-09-10
lang: zh
---

> 从 154 条内容中筛选出 14 条重要资讯。

---

**Harness 架构**
1. [vLLM v0.29.0 发布](#item-harness-arch-1) ⭐️ 9.8/10
2. [Codex rust-v0.154.0 发布](#item-harness-arch-2) ⭐️ 7.8/10
3. [Cline desktop-v0.0.24 发布](#item-harness-arch-3) ⭐️ 7.8/10
4. [Mastra Core 1.65.0 发布](#item-harness-arch-4) ⭐️ 7.8/10
5. [mem0 pi-agent-v0.3.0 发布](#item-harness-arch-5) ⭐️ 7.8/10
6. [mem0 deepseek-plugin-v0.3.0 发布](#item-harness-arch-6) ⭐️ 7.8/10
7. [OpenHands v1.17.0 发布](#item-harness-arch-7) ⭐️ 6.8/10

**Agent 工程师日报**
1. [GPT-6 Astra 循环变换器 隐藏推理](#item-agent-engineer-1) ⭐️ 7.0/10
2. [Granite Time Series PatchTST-FM-r2 发布](#item-agent-engineer-2) ⭐️ 5.8/10

**AI 日报**
1. [OpenAI 政策窗口开放 需行动](#item-ai-daily-1) ⭐️ 5.8/10
2. [Paul Christiano 加入 OpenAI 基金会董事会](#item-ai-daily-2) ⭐️ 5.8/10
3. [Claude Fable 5.1 发布 OpenAI 网络模型](#item-ai-daily-3) ⭐️ 5.0/10

**AI 羊毛**
1. [复旦学术 Codex 客户端上线 送 1 万积分](#item-ai-deals-1) ⭐️ 7.0/10
2. [DeepSeek V4-Flash 降价 V4-Pro 转向 V4.1 Flash](#item-ai-deals-2) ⭐️ 7.0/10

---

## Harness 架构

<a id="item-harness-arch-1"></a>
### [vLLM v0.29.0 发布](https://github.com/vllm-project/vllm/releases/tag/v0.29.0) ⭐️ 9.8/10

vLLM v0.29.0 发布将 Model Runner V2 设为所有模型的默认推理引擎。此版本添加 CUDA 图内存分析以支持 KV cache 自动调整大小。还包括批处理分片采样、提示嵌入提取和提取隐藏状态等功能。

github · khluu · 9月9日 08:54

**「设计要点」** Model Runner V2 作为默认运行时引擎，集成 CUDA 图内存分析用于 KV cache 自动调整大小。

**「改了什么」** Model Runner V2 成为所有模型的默认运行时引擎。CUDA 图内存分析支持 KV cache 自动调整大小。

**标签**: `#runtime`, `#memory`, `#prefix-cache`

---

<a id="item-harness-arch-2"></a>
### [Codex rust-v0.154.0 发布](https://github.com/openai/codex/releases/tag/rust-v0.154.0) ⭐️ 7.8/10

openai/codex rust-v0.154.0 发布。新增实验性 worktree 支持，用于创建隔离检查点以进行新会话或分支操作。Windows 会话支持共享后台 Codex 服务器，并更新了插件工具集成。

github · github-actions\[bot\] · 9月9日 22:35

**「改了什么」** 相比 rust-v0.153.0，新增实验性 worktree 支持和 Windows 后台服务器功能。修复了外部插件升级后的工具刷新问题，并改善了 MCP 连接的 OAuth 刷新机制。

**标签**: `#sandbox`, `#runtime`, `#tools`

---

<a id="item-harness-arch-3"></a>
### [Cline desktop-v0.0.24 发布](https://github.com/cline/cline/releases/tag/desktop-v0.0.24) ⭐️ 7.8/10

Cline desktop-v0.0.24 已发布。该版本修复了直播聊天流文本翻倍和消息中途丢弃的问题，通过跳过观察者流和管理流计数器来解决。还修复了队列提示消息消失、模型重复问题等多个问题。

github · github-actions\[bot\] · 9月9日 08:16

**「改了什么」** 修复了直播聊天流文本翻倍和消息中途丢弃的问题。通过跳过观察者流和管理流计数器来解决。还修复了队列提示消息消失、模型重复停止等问题，并添加了 Windows 自定义标题栏。

**标签**: `#runtime`, `#tools`

---

<a id="item-harness-arch-4"></a>
### [Mastra Core 1.65.0 发布](https://github.com/mastra-ai/mastra/releases/tag/%40mastra/core%401.65.0) ⭐️ 7.8/10

Mastra Core 1.65.0 发布了高级追踪查询合约，支持谓词、分页和多数据库实现。新增了基于租户的追踪删除，支持级联清理实验和相关数据。工作流控制流块现在支持可选的 id、description 和 metadata。

github · PaulieScanlon · 9月9日 09:43

**「改了什么」** 新增高级追踪查询合约和基于租户的追踪删除功能。工作流控制流块支持了 id、description 和 metadata。

**标签**: `#runtime`, `#planning`, `#memory`, `#permissions`

---

<a id="item-harness-arch-5"></a>
### [mem0 pi-agent-v0.3.0 发布](https://github.com/mem0ai/mem0/releases/tag/pi-agent-v0.3.0) ⭐️ 7.8/10

mem0 发布了 pi-agent-v0.3.0。更新了 Pi agent 扩展集成、构建流程和内存工具处理，同时移除了 Dream 整合和 pin 命令。保留了共享对话准备、内存格式化、项目/会话/全局作用域工具。构建发布 dist/entry.js 而非源代码。

github · kartik-mem0 · 9月9日 14:40

**「改了什么」** 相对上一版，Pi agent 扩展集成和内存工具处理能力得到更新。移除了 Dream 整合和 pin 命令，修复了全局内存工具作用域和引用处理。

**标签**: `#memory`, `#tools`, `#runtime`

---

<a id="item-harness-arch-6"></a>
### [mem0 deepseek-plugin-v0.3.0 发布](https://github.com/mem0ai/mem0/releases/tag/deepseek-plugin-v0.3.0) ⭐️ 7.8/10

Mem0 DeepSeek 插件 v0.3.0 发布。新增在系统提示词组装期间自动召回记忆，并在完成回合后从持久会话事件流自动捕获记忆。默认启用 autoRecall 和 autoCapture，可通过配置禁用。

github · kartik-mem0 · 9月9日 14:36

**「设计要点」** 插件复用共享生命周期、脱敏、身份和遥测工具，同时保留显式工具。支持 Harness 运行时依赖，并记录 macOS watcher 工作绕过。

**「改了什么」** 新增自动记忆召回和捕获功能，使用 durable session/event stream 进行捕获。发布自包含 ESM 构件 @mem0/deepseek-plugin，复用共享工具并支持 userId 覆盖 opt-in。

**标签**: `#memory`, `#runtime`, `#tools`, `#permissions`

---

<a id="item-harness-arch-7"></a>
### [OpenHands v1.17.0 发布](https://github.com/OpenHands/OpenHands/releases/tag/v1.17.0) ⭐️ 6.8/10

OpenHands v1.17.0 发布。新增 Agent Canvas Planner 支持，并使自动化运行 UI 具备任务感知能力。添加云 LLM 连接入口、自定义 cron 表达式编辑和对话面板标签过滤功能。保留版本号 v1.17.0。

github · openhands-release-bot\[bot\] · 9月9日 19:27

**「改了什么」** 相对 v1.16.0，主要新增 Agent Canvas Planner 支持和自动化 UI 任务感知能力。添加云设置入口和自定义 cron 表达式编辑功能。

**标签**: `#planning`, `#runtime`, `#tools`

---

## Agent 工程师日报

<a id="item-agent-engineer-1"></a>
### [GPT-6 Astra 循环变换器 隐藏推理](https://magazine.sebastianraschka.com/p/gpt-6-astra-looped-transformers-and) ⭐️ 7.0/10

Sebastian Raschka 分析 GPT-6 Astra 的性能和架构。Astra 在 3D 渲染、动画、数学、编码和 ARC-AGI-3 基准上表现突出，ARC-AGI-3 得分 99.9%。文章讨论了循环变换器和隐藏推理机制，并介绍了计算机使用能力的训练方法。

rss · Sebastian Raschka · 9月9日 11:14 · [社区讨论](https://news.ycombinator.com/item?id=49627370)

**「为什么重要」** Astra 的计算机使用能力已发生，这为代理提供了 GUI 交互新范式。循环变换器与隐藏推理的讨论尚未证实具体机制。

**「可关注」** 可关注：模型通过预测鼠标键盘动作并在 macOS 环境中执行来学习计算机使用。

**「评论」** 社区对 Astra 性能和循环变换器有讨论，有人指出其本质是权重重用而非全新技术，有人分享了关于 CoT 必要性的研究。

**标签**: `#eval`, `#orchestration`, `#memory`, `#coding-agent`, `#observability`

---

<a id="item-agent-engineer-2"></a>
### [Granite Time Series PatchTST-FM-r2 发布](https://huggingface.co/blog/ibm-research/ibm-releases-sota-granite-time-series) ⭐️ 5.8/10

IBM 发布了 Granite Time Series PatchTST-FM-r2，这是其时间序列基础模型系列的最新版本。作为零样本时间序列基础模型，PatchTST-FM-r2 在 GIFT-Eval 基准上表现最佳，排名第二于可复现零样本模型，CRPS 和 MASE 几何均值分别为 0.467 和 0.6846。作为 September 8, 2026 时的结果。该模型参数量约 385M，支持上下文长度 8192，提供概率预测。权重、架构、推理管道和代码均已开源，许可协议为 Apache 2.0 和 OpenMDW 1.0。

rss · Hugging Face Blog · 9月9日 15:36

**「为什么重要」** PatchTST-FM-r2 在 GIFT-Eval 零样本可复现模型类别中表现最佳，这使其在时间序列预测系统中具有实用价值。已发生的是模型发布和基准表现，尚未证实其在特定应用中的影响。

**「可关注」** 可关注：尽管预训练数据来源透明，但仍需组织自行进行模型治理和许可审查。

**标签**: `#eval`, `#orchestration`, `#foundation-model`, `#harness`

---

## AI 日报

<a id="item-ai-daily-1"></a>
### [OpenAI 政策窗口开放 需行动](https://openai.com/index/ai-policy-window) ⭐️ 5.8/10

OpenAI 博客文章由 Chris Lehane 撰写，指出更强的 AI 能力需要更强的安全证据、共享标准和持久的政策行动，同时政策窗口保持开放。文章强调需在窗口开放时采取行动。材料中未提供新的技术事实或可验证的数据，仅为政策呼吁。

rss · OpenAI Blog · 9月9日 13:00

**「为什么重要」** 今天值得看，因为它呼吁在政策窗口开放时采取行动。

**「可关注」** 可关注：更强的 AI 能力需要更强的安全证据、共享标准和持久的政策行动。

**标签**: `#policy`, `#openai`, `#safety`

---

<a id="item-ai-daily-2"></a>
### [Paul Christiano 加入 OpenAI 基金会董事会](https://openai.com/index/paul-christiano-joins-openai-foundation-board) ⭐️ 5.8/10

Paul Christiano 加入 OpenAI 基金会董事会及其安全与安全委员会。他带来 AI 对齐、安全和标准方面的经验。

rss · OpenAI Blog · 9月9日 17:00

**「可关注」** 可关注：Paul Christiano 加入 OpenAI 基金会董事会及其安全与安全委员会，带来 AI 对齐、安全和标准方面的经验。

**标签**: `#openai`, `#board`, `#safety`, `#alignment`, `#policy`

---

<a id="item-ai-daily-3"></a>
### [Claude Fable 5.1 发布 OpenAI 网络模型](https://lastweekin.ai/p/lwiai-podcast-256-fable-51-astra) ⭐️ 5.0/10

Anthropic 推出 Claude Fable 5.1。OpenAI 即将发布首个具备‘关键’网络能力的 AI 模型。OpenAI 的 rogue AI 模型事件比我们想象的更严重。

rss · Last Week in AI · 9月9日 08:01

**「可关注」** 可关注：OpenAI 即将发布首个具备‘关键’网络能力的 AI 模型。

**标签**: `#model`, `#anthropic`, `#openai`, `#industry`

---

## AI 羊毛

<a id="item-ai-deals-1"></a>
### [复旦学术 Codex 客户端上线 送 1 万积分](https://www.appinn.com/qiewenpaper-codex-2/) ⭐️ 7.0/10

复旦大学 NLP 团队上线学术版 Codex 客户端。下载并登录即可获得 1 万积分。此外，还可享受会员 8 折优惠。

rss · 小众软件 · 9月9日 08:31

**「可关注」** 可关注：适用于科研人员使用

**标签**: `#credits`, `#promo`, `#api`, `#limited-free`

---

<a id="item-ai-deals-2"></a>
### [DeepSeek V4-Flash 降价 V4-Pro 转向 V4.1 Flash](https://www.appinn.com/deepseek-flash-price-cut-24-days-after-price-hike/) ⭐️ 7.0/10

DeepSeek 团队 @Tianyi Cui 宣布：V4.1 Flash 模型在性能、费用、速度、总用时等指标全面超越 V4 Pro，故将 V4-Pro 模型指向 V4.1 Flash。V4-Flash 模型在涨价 24 天后进行降价。V4-Pro 不再提供原有的性能较差的 V4 Pro 模型。

rss · 小众软件 · 9月9日 07:05

**「为什么重要」** V4.1 Flash 性能更优，开发者可及时使用新模型优化 API 成本。

**「可关注」** 可关注：V4-Pro 模型将指向 V4.1 Flash，适用于所有使用 DeepSeek API 的开发者。

**标签**: `#promo`, `#api`, `#price-cut`, `#model-update`

---