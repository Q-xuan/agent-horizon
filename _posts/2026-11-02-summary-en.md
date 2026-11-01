---
layout: default
title: "Horizon Summary: 2026-11-02 (EN)"
date: 2026-11-02
lang: en
---

> From 132 items, 3 important content pieces were selected

---

**Agent Harness Architecture**
1. [fastmcp v4.2.0a2 发布](#item-harness-arch-1) ⭐️ 7.8/10
2. [crewAI 1.15.34 发布](#item-harness-arch-2) ⭐️ 5.3/10

**AI Agent Engineer**
1. [ChatGPT HTML 预览沙箱逃逸漏洞](#item-agent-engineer-1) ⭐️ 7.0/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [fastmcp v4.2.0a2 发布](https://github.com/PrefectHQ/fastmcp/releases/tag/v4.2.0a2) ⭐️ 7.8/10

fastmcp v4.2.0a2 是 PrefectHQ 发布的第二个 4.2 版 alpha，携带 4.1.5 全部修复及 4.2 专属协议修正。MCP 协议层调整 JSON Schema 校验语义：\`const\` 与 \`enum\` 按 JSON 等值比较，\`prompts/get\` 缺必填参数返回 \`-32602\`，OpenAPI 上游错误截断至 1 KB 并丢弃 HTML 体，严格模式拒绝未声明参数。stdio 传输层修复保活子进程超时忽略问题，支持多客户端超时隔离与嵌套会话共享。Skills 发现扩展至代理透传与挂载服务器，Prefab 后端地址支持 4.2 代理重绑定，大型工具目录 schema 展开加速。该版本已通过 pydantic-ai、langchain、agno、Microsoft Agent Framework 及 OpenAI Agents SDK 的兼容性验证，Skills 仍为实验性功能，仅建议集成测试使用。

github · zzstoatzz · Nov 1, 22:58

**「设计要点」** 运行时层将保活 stdio 子进程的超时控制权交还客户端，允许不同超时配置的客户端共享会话或触发重启；工具层将 Skill 抽象为存储中立对象，通过文件夹加载器与资源清单回退机制实现跨后端发现；Prefab 渲染器改为按需构建页面而非在资源列表时预生成。

**「改了什么」** 相对 v4.2.0a1，协议行为发生三处 breaking change：JSON Schema \`const\`/\`enum\` 改为 JSON 等值比较（\`true\` 不再匹配 \`1\`）；\`prompts/get\` 缺参返回 \`invalid params \(-32602\)\`；严格输入校验拒绝未声明 OpenAPI 参数，上游错误响应截断至 1 KB。stdio 传输支持多客户端超时隔离，Skills 发现新增代理透传、ClientGroup 集成及 CLI \`--skills\` 参数，Skill 对象重构为存储中立模型。

**Tags**: `#mcp`, `#tools`, `#runtime`

---

<a id="item-harness-arch-2"></a>
### [crewAI 1.15.34 发布](https://github.com/crewAIInc/crewAI/releases/tag/1.15.34) ⭐️ 5.3/10

这是crewAI agent harness的官方1.15.34 minor版本发布，新增LiteLLM独立目录支持、组织级技能搜索、部署zip提交追踪、规划配置文档与推理页迁移，同时修复工具调用处理、上下文窗口回退、LLM提供商兼容性、运行时错误韧性等20余项问题，并补充1.15.29版agent executor移除的迁移说明。

github · joaomdmoura · Nov 1, 21:21

**「设计要点」** 运行时层优化上下文窗口回退提示、工具调用停止计数与异常保留逻辑；工具层新增LiteLLM目录适配与结构化输出token统计能力；兼容层修复Python 3.10/3.12的导入与JSON渲染问题，同时保留已移除导入路径的弃用警告。

**「改了什么」** 相对上一版本新增LiteLLM catalog独立PR支持、组织技能搜索、部署zip提交追踪、规划配置文档与推理页迁移；修复工具调用停止计数、上下文窗口回退提示、OpenAI兼容提供商MissingAPIKeyError、LiteLLM流式错误保留原始异常、结构化输出工具调用token统计等20余项问题；移除1.15.29版agent executor并补充迁移文档。

**Tags**: `#runtime`, `#tools`, `#planning`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [ChatGPT HTML 预览沙箱逃逸漏洞](https://simonwillison.net/2026/Oct/31/how-we-took-over-chatgpt-accounts/) ⭐️ 7.0/10

2026 年 10 月 31 日，Parameter Labs 披露 ChatGPT HTML 预览功能的账户接管漏洞。攻击链利用 MathLive 库的虚拟键盘 postMessage 接口，从沙箱 iframe 向父页面发送消息；父页面接收代码使用 innerHTML 处理消息，导致未受信 HTML 注入。攻击者随后可插入无沙箱限制的 iframe，并借助 YouTube oEmbed 端点绕过 CSP 执行 JavaScript，最终窃取已登录用户私有数据或代其执行操作。OpenAI 已修复漏洞并发放 5000 美元 bug bounty，报告作者认为该金额对漏洞严重性而言偏低。

rss · Simon Willison · Oct 31, 23:15

**「为什么重要」** 该漏洞证明第三方库的 postMessage 接口可突破 iframe 沙箱假设，对依赖 HTML 预览或类似沙箱机制的 AI 产品构成直接风险。修复已部署，但攻击链揭示了 CSP 配置与跨帧消息验证的复合失效模式。

**「可关注」** 沙箱 iframe 的 postMessage 接收端若使用 innerHTML 且未校验消息来源，即使 CSP 限制严格，仍可能被链式利用至代码执行。

**Tags**: `#permissions`, `#coding-agent`, `#observability`

---