---
layout: default
title: "Horizon Summary: 2026-08-19 (ZH)"
date: 2026-08-19
lang: zh
---

> 从 90 条内容中筛选出 6 条重要资讯。

---

**Harness 架构**
1. [openai/codex rust-v0.148.0 发布](#item-harness-arch-1) ⭐️ 7.0/10
2. [pydantic-ai v2.32.0 发布](#item-harness-arch-2) ⭐️ 7.0/10
3. [cloudflare/agents 发布了 hono-agents@3.0.12](#item-harness-arch-3) ⭐️ 7.0/10
4. [Cloudflare Agents 0.21.0 发布](#item-harness-arch-4) ⭐️ 7.0/10
5. [@cloudflare/ai-chat 0.10.2：观察者错误终态与 WebSocketChatTransport](#item-harness-arch-5) ⭐️ 7.0/10

**Agent 工程师日报**
1. [代理实际需要多少内存？](#item-agent-engineer-1) ⭐️ 7.0/10

---

## Harness 架构

<a id="item-harness-arch-1"></a>
### [openai/codex rust-v0.148.0 发布](https://github.com/openai/codex/releases/tag/rust-v0.148.0) ⭐️ 7.0/10

OpenAI codex v0.148.0 发布了 Rust 版本更新。该系统是一个 AI 编码工具，支持 TUI 界面。新增功能包括 TUI 会话导出到 Markdown、会话分叉/归档、异步 MCP 工具钩子、状态恢复和 AWS Bedrock 支持。保留了之前的版本号 rust-v0.148.0 和相关接口限制。

github · github-actions\[bot\] · 8月18日 22:26

**「变更内容」** 相对于上一版 rust-v0.147.0，新增了会话分叉（codex exec fork）和归档功能，支持异步命令钩子调用 MCP 工具，恢复会话时保留工作目录和审批策略，并添加了 Amazon Bedrock 提供商支持。模型切换和设置更新不再留下过时指令。

**标签**: `#runtime`, `#tools`, `#memory`, `#permissions`, `#mcp`

---

<a id="item-harness-arch-2"></a>
### [pydantic-ai v2.32.0 发布](https://github.com/pydantic/pydantic-ai/releases/tag/v2.32.0) ⭐️ 7.0/10

pydantic-ai v2.32.0 版本发布，涵盖运行时仪器更新、工具生命周期增强以及钩子和上下文取消的错误修复。新增支持 xAI 附件搜索生命周期，并将 OpenRouter web-search 来源公开到 provider\_details\[&quot;annotations&quot;\] 。添加 instrumentation version 6，工具结果通过 role: &\#x27;tool&\#x27; 发出。保留版本号 v2.32.0。

github · dsfaccini · 8月19日 03:51

**「架构信息」** 运行时仪器版本升级至 v6，工具结果通过 role: &\#x27;tool&\#x27; 发出。

**「变更内容」** 相比 v2.31.1，真正改变的能力包括同步钩子在线程池中运行并强制设置超时，以及 RunContext.cancel\(\) 在 setup-phase for\_run hooks 中的记录。

**标签**: `#runtime`, `#tools`, `#hooks`, `#instrumentation`

---

<a id="item-harness-arch-3"></a>
### [cloudflare/agents 发布了 hono-agents@3.0.12](https://github.com/cloudflare/agents/releases/tag/hono-agents%403.0.12) ⭐️ 7.0/10

这是 cloudflare/agents 发布的 hono-agents 3.0.12 版本。这是一个补丁发布，保留了 onBeforeConnect HTTP 拒绝响应的内容，以避免下游 Hono 处理程序的回退。这要求现有应用程序将 agentsMiddleware 挂载到更窄的路径上或配置不同的 Agent 路由前缀。hono-agents@3.0.12 还要求 agents &gt;=0.17.1。

github · github-actions\[bot\] · 8月18日 09:08

**「变更内容」** hono-agents 3.0.12 补丁保留了 onBeforeConnect 返回的 HTTP 拒绝响应，而不是继续通过下游 Hono 处理程序。这要求现有应用程序将 agentsMiddleware 挂载到更窄的路径上或配置不同的 Agent 路由前缀，hono-agents@3.0.12 还要求 agents &gt;=0.17.1。

**「社区讨论」** 没有社区评论可用。

**标签**: `#runtime`, `#middleware`, `#hono`, `#agents`

---

<a id="item-harness-arch-4"></a>
### [Cloudflare Agents 0.21.0 发布](https://github.com/cloudflare/agents/releases/tag/agents%400.21.0) ⭐️ 7.0/10

Cloudflare Agents 0.21.0 是次要版本更新。它从框架中立的 agents/chat/transport 入口点公开了 WebSocketChatTransport，使 React 对等方成为可选。还改进了 agentTool 中的工具模式处理，支持灵活的 AI SDK 模式，包括 Valibot，移除了 Zod 的对等依赖。

github · github-actions\[bot\] · 8月18日 09:08

**「架构说明」** 该版本通过框架中立的 agents/chat/transport 入口点支持聊天传输，使 React 对等方可选。工具模式处理使用 AI SDK 灵活模式。

**「变更内容」** 此版本从 agents/chat/transport 入口点公开了 WebSocketChatTransport，使 React 对等方可选，并接受 AI SDK 灵活模式在 agentTool 中，包括 Valibot。还添加了 buildAgentPath\(\) 和 buildAgentUrl\(\) 函数以及浏览器工具的 Kitesurf 支持。

**标签**: `#runtime`, `#tools`, `#chat`, `#transport`

---

<a id="item-harness-arch-5"></a>
### [@cloudflare/ai-chat 0.10.2：观察者错误终态与 WebSocketChatTransport](https://github.com/cloudflare/agents/releases/tag/%40cloudflare/ai-chat%400.10.2) ⭐️ 7.0/10

Cloudflare agents 发布了 @cloudflare/ai-chat@0.10.2 补丁。useAgentChat 的观察者错误帧现被当作终态响应：明文错误体不再解析为流式分片，也不会合并进空的助手消息；即使帧省略 done，也会清空观察者的 streaming、replay、recovery 与 tool-continuation 状态，以对齐传输层自有流的行为。同时从框架无关入口 agents/chat/transport 导出 WebSocketChatTransport 及其连接类型，并使 agentTool 接受 AI SDK FlexibleSchema（含 Valibot 适配器），Zod 不再是 @cloudflare/ai-chat 的 peer 依赖。

github · github-actions\[bot\] · 8月18日 09:08

**「架构要点」** 运行时上，观察者错误路径与传输层拥有的流行为对齐，错误帧终止流并清理续跑状态。工具层仍保留 schema 驱动的输入推断与结构化输出校验，但校验-only 的 Standard Schema 不够用，因为工具输入必须向模型暴露 JSON Schema；自定义 schema 需使用对应库的 AI SDK 适配器，或用 jsonSchema\(\) 包装原始 JSON Schema。

**「相对上版变化」** 观察者错误不再进入助手消息流，既有把错误体当助手消息展示的 UI 必须改到独立错误界面。框架无关客户端与服务端不再强制 React peer，但继续使用 agents/chat/react 或 @cloudflare/ai-chat/react 的项目仍须显式声明兼容的 react 与 @ai-sdk/react；agentTool 现接受 Valibot 等灵活 schema，Zod 不再作为 peer 要求。

**标签**: `#runtime`, `#streaming`, `#transport`, `#error-handling`, `#observer`

---

## Agent 工程师日报

<a id="item-agent-engineer-1"></a>
### [代理实际需要多少内存？](https://huggingface.co/blog/ibm-research/altk-evolve-hmm) ⭐️ 7.0/10

Hugging Face 博客报道 IBM Research 的 ALTK-Evolve 方法，通过模型大小校准代理记忆剂量实现最佳性能，无需重新训练。在八个模型上测试，从 30B 密集模型到前沿系统，发现代理记忆不是开关功能，而是需根据模型校准的剂量。强模型使用完整指南集，弱模型使用紧凑核心加任务相关检索，饱和模型无增益。实验在 AppWorld 基准上，包含 585 个多步任务。

rss · Hugging Face Blog · 8月18日 18:09

**「为什么值得关注」** 材料展示了不同模型的最佳记忆配置，这对代理编排和评估设计有直接影响。实验结果已发生，但未证实其在生产环境中的长期影响。

**「工程含义」** 可关注：模型能力影响记忆剂量校准

**标签**: `#memory`, `#eval`, `#harness`, `#orchestration`, `#coding-agent`

---