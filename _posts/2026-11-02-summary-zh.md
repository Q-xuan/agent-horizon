---
layout: default
title: "Horizon Summary: 2026-11-02 (ZH)"
date: 2026-11-02
lang: zh
---

> 从 132 条内容中筛选出 3 条重要资讯。

<nav id="ah-toc" class="ah-toc" aria-label="目录"><span class="ah-toc-title">目录</span><ul><li><a href="#sec-harness-arch"><span class="ah-toc-name">Harness 架构</span><span class="ah-toc-count">2条</span></a></li><li><a href="#sec-agent-engineer"><span class="ah-toc-name">Agent 工程师日报</span><span class="ah-toc-count">1条</span></a></li></ul></nav>

---

**[Harness 架构](#sec-harness-arch)**
1. [fastmcp v4.2.0a2 发布](#item-harness-arch-1) ⭐️ 7.8/10
2. [crewAI 1.15.34 发布](#item-harness-arch-2) ⭐️ 5.3/10

**[Agent 工程师日报](#sec-agent-engineer)**
1. [ChatGPT HTML 预览沙箱逃逸漏洞修复](#item-agent-engineer-1) ⭐️ 7.0/10

---

## Harness 架构
{: #sec-harness-arch .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-harness-arch" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-harness-arch-1"></a>
### [fastmcp v4.2.0a2 发布](https://github.com/PrefectHQ/fastmcp/releases/tag/v4.2.0a2) ⭐️ 7.8/10

这是 PrefectHQ 开发的 fastmcp MCP 框架的 v4.2.0a2 alpha 预发布版本，包含 4.1.5 全部修复及 4.2 专属更新，新增 Skills 代理发现、Prefab 后端地址重绑定、大型工具目录 schema 加速生成、保活 stdio 传输客户端超时支持等能力，同时调整了 JSON Schema 校验、prompts/get 错误返回、OpenAPI 错误截断等协议级行为。Skills 功能仍处于实验阶段，该版本仅建议用于集成测试，不适用于生产环境。

github · zzstoatzz · 11月1日 22:58

**「设计要点」** Skills 设计为存储中立对象，支持文件夹作为加载器之一；保活 stdio 传输实现不同超时客户端的子进程重启与共享会话超时警告机制；发布前已验证与 pydantic-ai、langchain、agno、Microsoft Agent Framework、OpenAI Agents SDK 的跨 SDK 兼容性。

**「改了什么」** 相对 v4.2.0a1，核心变更包括：JSON Schema 的 const 和 enum 按 JSON 相等规则比较（true 不再匹配 1）；prompts/get 缺失必填参数时返回-32602 无效参数错误；OpenAPI 上游错误截断至 1KB 并丢弃 HTML 响应体，严格输入校验拒绝未声明的 OpenAPI 参数；保活 stdio 传输支持不同超时客户端重启空闲子进程，嵌套在活跃客户端内的子进程共享会话超时并输出警告。

**「评论」** 无可用社区评论。

**标签**: `#mcp`, `#tools`, `#runtime`

---

<a id="item-harness-arch-2"></a>
### [crewAI 1.15.34 发布](https://github.com/crewAIInc/crewAI/releases/tag/1.15.34) ⭐️ 5.3/10

crewAI 1.15.34 发布，新增 LiteLLM 目录支持、组织技能搜索、部署包提交追踪及规划配置文档，支持 crewai run --inputs 传递输入。修复工具调用处理、上下文窗口回退、LLM 提供商兼容性与运行时错误恢复等缺陷，crewai\[litellm\] 要求 Python 3.10 及以上并提升 joserfc、pyasn1、pypdf 最低版本，同时文档化移除 1.15.29 agent executor 的迁移路径。

github · joaomdmoura · 11月1日 21:21

**「改了什么」** 新增 LiteLLM 目录集成、组织技能搜索、部署包提交追踪与规划配置文档；修复工具调用结构化输出、上下文窗口回退警告、LLM 提供商 API 密钥校验及 AMP 登录恢复等运行时行为，并文档化移除 1.15.29 agent executor。

**标签**: `#runtime`, `#tools`, `#planning`

---

## Agent 工程师日报
{: #sec-agent-engineer .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-agent-engineer" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-agent-engineer-1"></a>
### [ChatGPT HTML 预览沙箱逃逸漏洞修复](https://simonwillison.net/2026/Oct/31/how-we-took-over-chatgpt-accounts/) ⭐️ 7.0/10

2026 年 10 月 31 日，安全研究机构 Parameter Labs 披露 ChatGPT HTML 预览（原称 Canvas）功能的沙箱逃逸漏洞，该功能用于在沙箱 iframe 中渲染交互式 HTML 应用。攻击链利用功能嵌入的 MathLive 库虚拟键盘的 postMessage 接口，父页面接收消息时使用 innerHTML 注入无沙箱限制的 iframe，再结合 YouTube oEmbed 端点绕过内容安全策略执行 JavaScript，最终可窃取已登录用户的私有数据或代其执行操作。攻击者只需构造恶意分享链接，已登录用户访问即可触发攻击。OpenAI 已修复该漏洞，并向披露方支付 5000 美元漏洞赏金，披露者认为该金额与漏洞严重程度不匹配。

rss · Simon Willison · 10月31日 23:15

**「为什么重要」** 该漏洞直接涉及 iframe 沙箱隔离、agent 权限边界与安全工具执行架构的核心风险，其攻击路径展示了即使配置内容安全策略，若未严格校验跨域消息来源，仍可能被突破，对构建隔离的代码执行环境有参考价值。

**「可关注」** 可关注：沙箱 iframe 向父页面发送 postMessage 时，必须校验消息来源与消息类型，避免未授权调用父页面的敏感接口。

**标签**: `#permissions`, `#coding-agent`, `#observability`

---