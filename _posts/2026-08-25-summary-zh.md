---
layout: default
title: "Horizon Summary: 2026-08-25 (ZH)"
date: 2026-08-25
lang: zh
---

> 从 143 条内容中筛选出 11 条重要资讯。

---

**Harness 架构**
1. [MCP Python SDK v2.1.0 发布](#item-harness-arch-1) ⭐️ 7.5/10
2. [mem0 CLI v0.2.12 发布](#item-harness-arch-2) ⭐️ 7.5/10
3. [Cline SDK v0.0.79 发布](#item-harness-arch-3) ⭐️ 6.5/10
4. [Mastra Core 1.61.0 发布](#item-harness-arch-4) ⭐️ 6.5/10
5. [mem0-strands-v0.1.0 发布](#item-harness-arch-5) ⭐️ 6.5/10
6. [mem0 deepseek-plugin-v0.1.0 发布](#item-harness-arch-6) ⭐️ 6.5/10
7. [Cline CLI v3.0.58 发布](#item-harness-arch-7) ⭐️ 5.5/10

**Agent 工程师日报**
1. [llm-anthropic 0.27 发布](#item-agent-engineer-1) ⭐️ 7.5/10

**AI 日报**
1. [ADK 支持用模拟音频评测 live agent](#item-ai-daily-1) ⭐️ 8.5/10
2. [GPT-5.6 现已上线 Kiro](#item-ai-daily-2) ⭐️ 6.5/10
3. [Claude Code 每周个性化更新](#item-ai-daily-3) ⭐️ 5.5/10

---

## Harness 架构

<a id="item-harness-arch-1"></a>
### [MCP Python SDK v2.1.0 发布](https://github.com/modelcontextprotocol/python-sdk/releases/tag/v2.1.0) ⭐️ 7.5/10

modelcontextprotocol/python-sdk v2.1.0 发布了。它更新了 Client 以直接接受 StdioServerParameters，添加了 Image 和 Audio 到提示消息，prompt 函数可返回裸内容块，并将 4MiB 请求体限制扩展到 SSE/OAuth 传输。同时，处理程序异常行为发生变化。

github · maxisbey · 8月24日 19:00

**「设计要点」** 设计要点：请求体限制扩展到 SSE 和 OAuth 端点，处理程序异常被记录一次并包含 traceback，客户端仅接收 Error executing tool &lt;name&gt; 消息。

**「改了什么」** 相比 v2.0.0，Client 直接接受 StdioServerParameters，提示支持 Image/Audio，4MiB 限制覆盖 SSE/OAuth，以及处理程序异常被记录为 ERROR 一次。

**标签**: `#mcp`, `#runtime`, `#tools`

---

<a id="item-harness-arch-2"></a>
### [mem0 CLI v0.2.12 发布](https://github.com/mem0ai/mem0/releases/tag/cli-v0.2.12) ⭐️ 7.5/10

mem0 CLI v0.2.12 发布了新版本，新增 version 子命令和 add 命令的 --agent-custom-instructions 标志。这使得脚本和 agent harness 可以作为子命令读取版本，并支持 agent-scoped 内存的自定义指令。文档也更新了 search --filter 的 JSON 示例。

github · kartik-mem0 · 8月24日 13:15

**「改了什么」** 相比上一版，新增 version 子命令而非仅使用 --version 标志，支持 harness 集成。add 命令新增 --agent-custom-instructions 标志，用于 agent-scoped 内存的额外提取。

**标签**: `#cli`, `#memory`, `#agent`, `#version`, `#filter`

---

<a id="item-harness-arch-3"></a>
### [Cline SDK v0.0.79 发布](https://github.com/cline/cline/releases/tag/sdk/sdk/v0.0.79) ⭐️ 6.5/10

Cline SDK v0.0.79 已发布。该版本为运行时存储引入了 durable event log 容量限制，限制在 64 MiB。旧事件按顺序删除，并通过 vacuuming 回收空间，修剪逻辑改为每 16 MiB 追加后立即执行。此外，修复了 task.completed 遥测在大多数交互会话中被丢弃的问题，现在在所有会话结束路径中精确发送一次。还刷新了模型目录，添加了 AgentRouter 和 Opper 两个提供商，并更新了定价和默认模型。

github · github-actions\[bot\] · 8月24日 23:01

**「设计要点」** 运行时存储的关键设计是 durable event log 现在被硬性限制在 64 MiB，通过 oldest events first 删除并 vacuuming 释放空间。修剪逻辑从每小时扫描改为每 16 MiB 追加后立即执行。

**「改了什么」** 相比 v0.0.78，Cline SDK v0.0.79 限制了 durable event log 的大小为 64 MiB，并引入了 vacuuming 机制来回收空间。task.completed 遥测现在在所有会话结束时被发送，并刷新了模型提供商和默认模型。

**标签**: `#runtime`, `#memory`, `#planning`

---

<a id="item-harness-arch-4"></a>
### [Mastra Core 1.61.0 发布](https://github.com/mastra-ai/mastra/releases/tag/%40mastra/core%401.61.0) ⭐️ 6.5/10

Mastra Core 1.61.0 发布了 Caller-Driven Experiments，支持外部编排器（如 Temporal）拥有实验循环，而 Mastra 保持系统记录。新增了可配置的服务器优雅关闭选项，支持 drainTimeout 和 handleShutdownSignals。会话消息发送时自动标记 delivery: &\#x27;while-active&\#x27;，简化客户端实现。

github · PaulieScanlon · 8月24日 09:02

**「改了什么」** 新增 Caller-Driven Experiments API 让外部 orchestrator 控制实验流程。会话消息自动标记 while-active 状态，修复并发 resume\(\) 调用导致下游步骤多次执行的问题。

**标签**: `#runtime`, `#eval`, `#sessions`, `#experiments`, `#shutdown`

---

<a id="item-harness-arch-5"></a>
### [mem0-strands-v0.1.0 发布](https://github.com/mem0ai/mem0/releases/tag/mem0-strands-v0.1.0) ⭐️ 6.5/10

mem0-strands-v0.1.0 正式发布，原生 MemoryStore 集成到 Strands Agents MemoryManager 中。该版本提供自动召回和注入功能，服务器端提取，逐字写入和实体作用域支持。用户可通过 api\_key 使用托管 Mem0，或提供 config 进行自托管。构建时采用异步线程懒加载，避免阻塞事件循环。

github · kartik-mem0 · 8月24日 20:06

**「设计要点」** Mem0MemoryStore 在首次使用时通过 asyncio.to\_thread 懒加载构建 Mem0 客户端，避免事件循环阻塞。支持 user\_id、agent\_id、run\_id 和 app\_id 实体作用域，至少需要提供一个。

**标签**: `#memory`, `#runtime`

---

<a id="item-harness-arch-6"></a>
### [mem0 deepseek-plugin-v0.1.0 发布](https://github.com/mem0ai/mem0/releases/tag/deepseek-plugin-v0.1.0) ⭐️ 6.5/10

mem0 发布了 @mem0/deepseek-plugin v0.1.0，这是 DeepSeek Harness \(Cordis\) 的原生插件，将 Mem0 注册为两个代理可调用的工具：search\_memory（记忆搜索，支持可选 limit 默认 10 和 per-call userId/agentId/runId 覆盖）和 add\_memory（存储事实，标记 source: &quot;DEEPSEEK\_HARNESS&quot;，提取在服务器端异步完成）。插件在 Cordis 生命周期中通过 apply\(ctx, config\) 声明 inject = \[&\#x27;tools&\#x27;\]，使用 ctx.tools.register\(\) 注册工具，在插件卸载时自动注销。配置要求 userId，apiKey 默认 $MEM0\_API\_KEY，host 可选指向 Mem0 Platform 基 URL。开发者预览的自动捕获和自动召回计划中但尚未实现。

github · kartik-mem0 · 8月24日 14:19

**「设计要点」** 插件通过 apply\(ctx, config\) 声明 inject = \[&\#x27;tools&\#x27;\]，等待工具注册表存在，并使用 ctx.tools.register\(\) 注册工具，在插件卸载时自动注销。

**「改了什么」** 这是 @mem0/deepseek-plugin 的初始发布，新增了 search\_memory 和 add\_memory 两个工具接口。

**标签**: `#tools`, `#memory`

---

<a id="item-harness-arch-7"></a>
### [Cline CLI v3.0.58 发布](https://github.com/cline/cline/releases/tag/cli-v3.0.58) ⭐️ 5.5/10

Cline CLI v3.0.58 发布了此次更新。该版本将 hub 事件日志的存储上限设为 64 MiB，并通过修剪来管理空间。首次启动时的 &quot;Try ClinePass&quot; 对话框不再宣传 $4.99 首月促销，该促销即将结束。模型目录也得到刷新，新增了 AgentRouter 和 Opper 两个提供商，并更新了默认模型。

github · github-actions\[bot\] · 8月24日 23:07

**「改了什么」** 相对上一版，Cline CLI v3.0.58 改进了 hub 事件日志的存储管理，将其上限设为 64 MiB 并启用修剪功能。模型目录得到刷新，新增了 AgentRouter 和 Opper 两个提供商，并更新了默认模型。

**标签**: `#runtime`, `#memory`, `#tools`

---

## Agent 工程师日报

<a id="item-agent-engineer-1"></a>
### [llm-anthropic 0.27 发布](https://github.com/simonw/llm-anthropic/releases/tag/0.27) ⭐️ 7.5/10

Simon Willison 发布了 llm-anthropic 0.27 版本。该版本将 Anthropic SDK 升级到 anthropic&gt;=1，并修复了 --no-stream 模式下使用流式 API 的错误，解决了大模型默认 max\_tokens 过长导致的 SDK 错误。此外，修复了 temperature=None 和 top\_p 的验证错误，添加了对 Claude Haiku 4.5 的结构化输出支持，并支持 Claude Opus 4.8 和 Claude 5 系列模型在对话中 inline 发送 system messages，同时保留了 thinking blocks 和 redacted\_thinking blocks。

github · simonw · 8月24日 16:27

**「可关注」** 可关注：Claude Opus 4.8 和 Claude 5 系列模型支持 mid-conversation system messages。

**标签**: `#coding-agent`, `#orchestration`, `#harness`, `#eval`

---

## AI 日报

<a id="item-ai-daily-1"></a>
### [ADK 支持用模拟音频评测 live agent](https://developers.googleblog.com/how-to-evaluate-live-voice-agents-in-adk/) ⭐️ 8.5/10

Google 在 ADK 里加了原生 live 评测：用模拟用户把每一轮用户话合成音频，驱动语音 live agent，并在现有文本 eval 循环里打分。示例把三个单职责 live agent 用 Workflow 串起来，模型都是 gemini-live-2.5-flash-native-audio；音频流全程保持打开，ADK 会把会话状态和对话历史带到下一阶段。评测集是 JSON，可以写带目标和 persona 的 conversation\_scenario（模拟用户即兴，conversation\_plan 完成后自行收束），也可以写死用户轮次；test\_config.json 配上 live\_model\_config 才走 live，不配则同一套用例跑文本。跑法是 uv run adk eval，也可以用 AgentEvaluator 接到 CI/CD；需要安装 eval extras，并配置 Live API 与 Gemini TTS 凭证。

rss · Google Developers AI · 8月24日 00:00

**「为什么重要」** 博客写明，live agent 不能只看 demo：工具不触发、跨轮丢上下文、插话被忽略，会在下次改 prompt 或换模型时出现。现在语音多轮可以放进和文本同一套可重复评测里。

**「可关注」** 同一套 eval case 靠有没有 live\_model\_config 在 live 和文本之间切换；llm\_audio 模拟器里 model 管用户轮次逻辑，audio\_model 管 TTS，max\_allowed\_invocations 给动态对话设轮次上限。

**标签**: `#ADK`, `#Google`, `#voice`, `#eval`, `#product`

---

<a id="item-ai-daily-2"></a>
### [GPT-5.6 现已上线 Kiro](https://openai.com/index/gpt-5-6-in-kiro) ⭐️ 6.5/10

GPT-5.6 现已可用在 Kiro，帮助开发者规划、构建、审查和测试软件。
该版本强调更好的价格性能。

rss · OpenAI Blog · 8月24日 12:00

**「为什么重要」** OpenAI 推出 GPT-5.6 在 Kiro，帮助开发者提升价格性能。

**「可关注」** 可关注：GPT-5.6 现已上线 Kiro，帮助开发者规划、构建、审查和测试软件，提升价格性能。

**标签**: `#model`, `#lab`, `#industry`, `#product`

---

<a id="item-ai-daily-3"></a>
### [Claude Code 每周个性化更新](https://claude.com/blog/how-an-anthropic-field-marketer-uses-claude-code-to-send-weekly-personalized-updates-to-every-sales-rep) ⭐️ 5.5/10

Anthropic 市场团队的 Adam Ward 使用 Claude Code，将每周销售报告转化为每个销售代表的个性化周报。通过黑客松 hackathon，他花一小时与团队讨论问题，逐步完善提示词和规则。最终每周一通过 Slack 向销售代表发送个性化简报，包括三项优先行动、相关活动和内容。已将此功能扩展到多个销售团队，并使某活动注册量翻倍。

rss · Claude Blog · 8月24日 00:00

**「可关注」** 可关注：从手动任务开始，用 Claude Code 重建流程，并通过用户反馈迭代提示词。

**标签**: `#anthropic`, `#claude`, `#marketing`, `#ai-application`, `#productivity`

---