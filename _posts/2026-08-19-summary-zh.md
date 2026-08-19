---
layout: default
title: "Horizon Summary: 2026-08-19 (ZH)"
date: 2026-08-19
lang: zh
---

> 从 95 条内容中筛选出 5 条重要资讯。

---

**Harness 架构**
1. [openai/codex rust-v0.148.0 发布](#item-harness-arch-1) ⭐️ 7.0/10
2. [pydantic-ai v2.32.0 发布](#item-harness-arch-2) ⭐️ 7.0/10
3. [cloudflare/agents @cloudflare/ai-chat@0.10.2 发布](#item-harness-arch-3) ⭐️ 7.0/10
4. [Cline 桌面 v0.0.14 发布](#item-harness-arch-4) ⭐️ 6.0/10

**Agent 工程师日报**
1. [ALTK-Evolve：Agent 内存剂量随模型能力变化](#item-agent-engineer-1) ⭐️ 7.0/10

---

## Harness 架构

<a id="item-harness-arch-1"></a>
### [openai/codex rust-v0.148.0 发布](https://github.com/openai/codex/releases/tag/rust-v0.148.0) ⭐️ 7.0/10

openai/codex rust-v0.148.0 版本发布。该版本新增了 TUI 会话导出到 Markdown 的功能，支持通过 /export 命令导出到剪贴板或新文件。还增加了会话 fork 和归档功能，使用 codex exec fork 命令，并支持从 TUI 恢复选择器中恢复或归档会话。同时新增了 Amazon Bedrock Runtime 提供商支持和异步 MCP 工具钩子。

github · github-actions\[bot\] · 8月18日 22:26

**「设计要点」** 运行时支持异步 MCP 工具钩子和命令执行，内存管理通过持久化工作目录和审批策略恢复。权限方面，沙箱限制现在对被拒绝或不可读路径 fail closed，支持 Linux 和 Windows。

**「改了什么」** 相比 rust-v0.147.0，主要新增了 TUI Markdown 导出、会话 fork/归档功能以及 Amazon Bedrock 支持。修复了模型切换导致的指令残留和会话恢复问题。

**标签**: `#runtime`, `#tools`, `#mcp`, `#memory`, `#permissions`

---

<a id="item-harness-arch-2"></a>
### [pydantic-ai v2.32.0 发布](https://github.com/pydantic/pydantic-ai/releases/tag/v2.32.0) ⭐️ 7.0/10

pydantic-ai v2.32.0 发布，更新了 agent harness 的运行时 instrumentation、工具结果发射和同步钩子处理。技术上新在 instrumentation version 6（工具结果使用 role: &\#x27;tool&\#x27;）、线程池同步钩子 + timeout enforcement，以及 xAI/OpenRouter provider 变化。

github · dsfaccini · 8月19日 03:51

**「设计要点」** 运行时 instrumentation 升级至 v6，工具结果以 role: &\#x27;tool&\#x27; 形式发射。同步钩子在线程池中运行并强制执行 timeout。

**「改了什么」** 相对于 v2.31.1，v2.32.0 增加了 instrumentation version 6，支持 xAI 附件搜索生命周期，并将 OpenRouter web-search sources 包含在 provider\_details 中。修复了同步钩子在线程池中的处理、RunContext.cancel\(\) 在 setup 阶段钩子中的逻辑，以及响应为空文本部分的处理。

**标签**: `#runtime`, `#tools`, `#instrumentation`, `#hooks`

---

<a id="item-harness-arch-3"></a>
### [cloudflare/agents @cloudflare/ai-chat@0.10.2 发布](https://github.com/cloudflare/agents/releases/tag/%40cloudflare/ai-chat%400.10.2) ⭐️ 7.0/10

这是 cloudflare/agents 框架的 @cloudflare/ai-chat@0.10.2 补丁更新。它将 useAgentChat observer 错误帧视为终端响应，并清除流式传输、重放、恢复和工具延续状态。同时暴露了 WebSocketChatTransport，支持框架中立的客户端和服务器。agentTool 接受 AI SDK 灵活模式，包括 Valibot 适配器，Zod 不再是 @cloudflare/ai-chat 的对等依赖。

github · github-actions\[bot\] · 8月18日 09:08

**「设计要点」** 工具层暴露了 WebSocketChatTransport，支持框架中立的客户端和服务器。错误帧处理将 observer 流式传输、重放、恢复和工具延续状态清空。

**「改了什么」** 此版本相对上一版，新增了将 observer 错误帧作为终端响应的处理逻辑。同时暴露了 WebSocketChatTransport，并支持 AI SDK 灵活模式，包括 Valibot 适配器。

**标签**: `#runtime`, `#memory`, `#streaming`, `#transport`

---

<a id="item-harness-arch-4"></a>
### [Cline 桌面 v0.0.14 发布](https://github.com/cline/cline/releases/tag/desktop-v0.0.14) ⭐️ 6.0/10

Cline 桌面端发布了 desktop-v0.0.14。命令输出改为边跑边流进 transcript，保留终端颜色，长命令可用 “Proceed while running” 丢到后台，让 agent 继续往下走。新增麦克风听写（走当前配置的 provider 和模型），支持图像生成的模型可在任务中出图并内联渲染；任务结束或需要输入时会发 macOS 原生通知，可在 Settings → Notifications 里配置。跑完的 agent run 会收成一条可展开摘要，写明工作时长和 tool call 次数，最终回答不再被工作行压住。

github · github-actions\[bot\] · 8月19日 06:18

**「设计要点」** 命令执行改成流式写入 transcript，并支持把长命令放到后台、agent 不阻塞。Auto-approval 现在是独立的 tool policy，不再改写 advertised mode，Act 模式下打开 auto-approve 也不会再套上 Yolo 系统提示。/skill 和 /workflow 不再把技能正文塞进用户消息，改由 skills tool 加载指令，会话标题也不再取技能 markdown 的第一行。

**「改了什么」** 相对 desktop-v0.0.13，加上了流式带色命令输出、后台继续、语音听写、内联出图和 macOS 通知，并提供可并排安装的 “Cline Code Beta” 应用跟踪实验分支。同时修了 event stream 结束后仍卡在 shimmer、整行带空格命令 ENOENT、checkpoint 恢复后 transcript 不裁、Gemini 自定义 base URL 缺 API version 段导致 404、LiteLLM 输入 token 上限被覆盖成 128K 等问题。

**标签**: `#runtime`, `#tools`, `#permissions`, `#memory`

---

## Agent 工程师日报

<a id="item-agent-engineer-1"></a>
### [ALTK-Evolve：Agent 内存剂量随模型能力变化](https://huggingface.co/blog/ibm-research/altk-evolve-hmm) ⭐️ 7.0/10

ALTK-Evolve 让 Agent 从自身过去轨迹中提取行为指导原则，并在推理时注入，无需更新模型权重或人工标注。在 AppWorld 基准（585 个多步任务）上评估八个模型发现，内存剂量需按模型能力校准：强模型（如 DeepSeek-V3.2）使用全指导原则集提升任务完成率 +9.5pp，弱模型（如 gpt-oss-120b）使用精选检索提升 +16.1pp，而饱和模型（如 GLM-5）无收益。精选检索还能将成本开销控制在 +5% 以内。

rss · Hugging Face Blog · 8月18日 18:09

**「为什么重要」** 该方法在不改变模型的情况下提供了可验证的性能提升，已在八个模型上观察到不同能力水平的校准效果。

**「可关注」** 可关注：弱模型通过精选检索可将性能提升与 token 成本控制在 +5% 内。

**标签**: `#memory`, `#eval`, `#orchestration`, `#retrieval`

---