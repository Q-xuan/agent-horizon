---
layout: default
title: "Horizon Summary: 2026-09-02 (ZH)"
date: 2026-09-02
lang: zh
---

> 从 178 条内容中筛选出 12 条重要资讯。

---

**Harness 架构**
1. [Claude Code v2.1.257 发布](#item-harness-arch-1) ⭐️ 7.8/10
2. [Codex rust-v0.152.0 发布](#item-harness-arch-2) ⭐️ 7.8/10
3. [LangChain 1.4.0a3 发布](#item-harness-arch-3) ⭐️ 7.8/10
4. [Cline desktop-v0.0.22-beta.1 发布](#item-harness-arch-4) ⭐️ 6.8/10
5. [Gemini CLI v0.59.0-preview.0 发布](#item-harness-arch-5) ⭐️ 6.8/10
6. [pydantic-ai v2.37.0 发布](#item-harness-arch-6) ⭐️ 5.8/10
7. [fastmcp v4.0.1 发布](#item-harness-arch-7) ⭐️ 5.8/10

**Agent 工程师日报**
1. [BenchMIRT 揭示 LLM 基准实际测量](#item-agent-engineer-1) ⭐️ 6.8/10
2. [Claude Fable 5.1 Mythos 5.1 发布](#item-agent-engineer-2) ⭐️ 6.0/10

**AI 日报**
1. [OpenAI Astra 达关键网络安全能力阈值](#item-ai-daily-1) ⭐️ 7.8/10
2. [ChatGPT 连接医疗数据源](#item-ai-daily-2) ⭐️ 7.8/10
3. [OpenAI：AI 原生公司工作流转运营能力](#item-ai-daily-3) ⭐️ 6.8/10

---

## Harness 架构

<a id="item-harness-arch-1"></a>
### [Claude Code v2.1.257 发布](https://github.com/anthropics/claude-code/releases/tag/v2.1.257) ⭐️ 7.8/10

Claude Code v2.1.257 发布。该版本将 Claude Fable 5.1 设为默认模型，并支持 1M 上下文和缓存读取。新增时间格式和时区设置选项。添加 CLAUDE\_CODE\_SUBAGENT\_MODEL\_FORCE 环境变量以强制子代理模型。

github · ashwin-ant · 9月1日 17:53

**「改了什么」** Claude Code v2.1.257 相比上一版，新增 Claude Fable 5.1 默认模型、时间格式配置选项，以及 CLAUDE\_CODE\_SUBAGENT\_MODEL\_FORCE 环境变量。

**标签**: `#subagents`, `#sandbox`, `#runtime`, `#tools`, `#permissions`

---

<a id="item-harness-arch-2"></a>
### [Codex rust-v0.152.0 发布](https://github.com/openai/codex/releases/tag/rust-v0.152.0) ⭐️ 7.8/10

Codex rust-v0.152.0 发布了 Vim 模式搜索支持。终端 UI 显示凭证刷新进度。MCP 服务器名称支持特殊字符，单个工具支持 output\_token\_limit 设置，app-server 客户端可配置 thread/shellCommand 超时。

github · github-actions\[bot\] · 9月1日 01:58

**「改了什么」** rust-v0.152.0 相比上一版，新增 Vim 搜索功能和速率限制横幅操作。MCP 工具支持输出令牌限制，app-server 客户端可配置 thread/shellCommand 超时。

**标签**: `#mcp`, `#tools`, `#runtime`, `#permissions`

---

<a id="item-harness-arch-3"></a>
### [LangChain 1.4.0a3 发布](https://github.com/langchain-ai/langchain/releases/tag/langchain%3D%3D1.4.0a3) ⭐️ 7.8/10

LangChain 1.4.0a3 发布，新增 langchain.mcp 命名空间，用于将 MCP 服务器适配为 LangChain 工具。MCPAdapter 支持多种客户端类型，包括 URL、本地脚本、预构建客户端和 ClientGroup。list\_tools 方法支持缓存模式，工具元数据分组在 mcp 命名空间下。

github · github-actions\[bot\] · 9月1日 17:19

**「改了什么」** 1.4.0 系列的第三个 alpha 版本，重点新增 langchain.mcp 命名空间，支持 MCPAdapter 适配工具，并实现 list\_tools 缓存和 elicitation 中断功能。

**标签**: `#mcp`, `#tools`, `#runtime`

---

<a id="item-harness-arch-4"></a>
### [Cline desktop-v0.0.22-beta.1 发布](https://github.com/cline/cline/releases/tag/desktop-v0.0.22-beta.1) ⭐️ 6.8/10

Cline desktop-v0.0.22-beta.1 发布。Composio 连接器现在直接注册到打包桌面运行时，支持 OAuth 更安全撤销和更稳健的连接断开重构行为。网页搜索默认在新桌面会话中启用。包含 0.0.21 版的所有稳定改进。

github · github-actions\[bot\] · 9月1日 22:39

**「改了什么」** Cline desktop-v0.0.22-beta.1 引入 Composio 连接器直接注册到桌面运行时，支持 OAuth 更安全撤销和更稳健的连接断开重构。默认启用网页搜索功能。

**标签**: `#runtime`, `#tools`, `#subagents`

---

<a id="item-harness-arch-5"></a>
### [Gemini CLI v0.59.0-preview.0 发布](https://github.com/google-gemini/gemini-cli/releases/tag/v0.59.0-preview.0) ⭐️ 6.8/10

Google Gemini CLI v0.59.0-preview.0 发布。包含 MCP OAuth 元数据处理的权限和安全修复，以及受限模式下工作区信任强制执行。保留版本号、接口和限制。

github · gemini-cli-robot · 9月1日 20:19

**「设计要点」** 设计要点：修复 MCP OAuth SSRF 漏洞并在受限模式下强制工作区信任，增强权限控制和沙箱安全。

**「改了什么」** 改了什么：修复 MCP OAuth 元数据发现和认证的 SSRF 问题，并强制受限模式下工作区信任和过滤 mcpServers。

**标签**: `#mcp`, `#permissions`, `#sandbox`, `#security`, `#runtime`

---

<a id="item-harness-arch-6"></a>
### [pydantic-ai v2.37.0 发布](https://github.com/pydantic/pydantic-ai/releases/tag/v2.37.0) ⭐️ 5.8/10

pydantic-ai v2.37.0 发布。新增 GLM-5.3-flash 支持，并修复了 pruned span queries、tool call UI emission 和 GoogleModel API routing 等问题。

github · dsfaccini · 9月1日 01:48

**「改了什么」** v2.37.0 相比 v2.36.0 增加了 GLM-5.3-flash 支持，并修复了 pruned span queries、tool call UI emission 和 GoogleModel API routing 等问题。

**标签**: `#runtime`, `#tools`

---

<a id="item-harness-arch-7"></a>
### [fastmcp v4.0.1 发布](https://github.com/PrefectHQ/fastmcp/releases/tag/v4.0.1) ⭐️ 5.8/10

fastmcp v4.0.1 发布。ClientGroup 现在以引用计数方式管理上下文，支持嵌套块和并发任务。适配器针对 Client 的 reentrancy 编写可直接使用 ClientGroup。

github · zzstoatzz · 9月2日 00:20

**「改了什么」** ClientGroup 上下文管理改为引用计数，支持从嵌套块或并发任务进入连接的组。相比 v4.0.0，此修复避免了 reentrancy 错误。

**标签**: `#runtime`, `#mcp`, `#memory`

---

## Agent 工程师日报

<a id="item-agent-engineer-1"></a>
### [BenchMIRT 揭示 LLM 基准实际测量](https://huggingface.co/blog/allenai/benchmirt) ⭐️ 6.8/10

BenchMIRT 是 Hugging Face 推出的 LLM 基准审计新方法，在提示级别分析单个问题。使用多维项目反应理论，分析 100 个 LLM 在 16 个基准的 34K 问题表现，独立恢复安全和通用推理两个维度。BBQ 信号更与通用推理关联，WMDP 也与推理关联，HarmBench 混合不同信号。保持 10% 问题可保留能力测量，预测准确率 79%。模型数据截至 2025 年 3 月。

rss · Hugging Face Blog · 9月1日 21:39

**「为什么重要」** BenchMIRT 已帮助分离基准中混合的信号。尚未证实其是否会改变 LLM 评估实践。

**「可关注」** 可关注：BenchMIRT 可预测未观察问题正确率 79%，优于简单基线 70%。

**标签**: `#eval`, `#harness`, `#benchmark`, `#auditing`, `#llm`

---

<a id="item-agent-engineer-2"></a>
### [Claude Fable 5.1 Mythos 5.1 发布](https://www.anthropic.com/claude-fable-and-mythos-5-1) ⭐️ 6.0/10

Claude Fable 5.1 和 Claude Mythos 5.1 发布。更新强调更自然的写作风格和指令遵循能力。官方提供了 What&\#x27;s new 文档和系统卡 PDF。

hackernews · denysvitali · 9月1日 17:53 · [社区讨论](https://news.ycombinator.com/item?id=49525378)

**「为什么重要」** Fable 5.1 的自然风格可能提升代理交互，但尚未有生产跟踪数据。

**「可关注」** 可关注：Fable 5.1 写作风格更自然，指令遵循更可靠。

**「评论」** 社区成员指出 Fable 5.1 写作风格更自然，指令遵循更好。异步任务中模型可能描述下一步或询问许可，需特定提示。

**标签**: `#coding-agent`, `#eval`, `#orchestration`

---

## AI 日报

<a id="item-ai-daily-1"></a>
### [OpenAI Astra 达关键网络安全能力阈值](https://openai.com/index/path-to-astra) ⭐️ 7.8/10

OpenAI 宣布 Astra 是首个达到关键网络安全能力阈值的模型。根据 Preparedness Framework，Astra 发布了更强的保障措施。

rss · OpenAI Blog · 9月1日 13:00

**「为什么重要」** OpenAI 的 Astra 达到关键网络安全能力阈值，标志着 AI 安全框架的重要进展。

**「可关注」** 可关注：Astra 是首个达到关键网络安全能力阈值的模型。

**标签**: `#model`, `#OpenAI`, `#Astra`, `#cybersecurity`, `#policy`

---

<a id="item-ai-daily-2"></a>
### [ChatGPT 连接医疗数据源](https://openai.com/index/chatgpt-connects-health-records-and-healthcare-sources) ⭐️ 7.8/10

OpenAI 允许 ChatGPT 连接可信医疗数据，帮助临床医生安全访问患者上下文和医学研究。
数据源包括 EHR 和其他行业数据。
连接过程确保数据安全。

rss · OpenAI Blog · 9月1日 12:00

**「为什么重要」** 这一功能支持医疗组织安全整合 EHR 等数据到 ChatGPT。

**「可关注」** 可关注：ChatGPT 可连接医疗数据源，包括 EHR。

**标签**: `#product`, `#industry`, `#OpenAI`, `#healthcare`, `#ChatGPT`

---

<a id="item-ai-daily-3"></a>
### [OpenAI：AI 原生公司工作流转运营能力](https://openai.com/index/ai-native-company-workflows) ⭐️ 6.8/10

OpenAI 博客文章分析 AI 原生公司如何通过 AI 代理将工作流转化为运营能力。Basis、Clay 和 Exa Labs 等公司利用 AI 代理改善入职、账户管理和开发者集成。企业领导者可借鉴这些案例提升运营效率。

rss · OpenAI Blog · 9月1日 17:00

**「为什么重要」** 这些实践展示了 AI 代理在企业运营中的落地应用，为企业数字化转型提供了可操作的路径。

**「可关注」** 可关注：企业可通过 AI 代理优化入职、账户管理和开发者集成流程。

**标签**: `#openai`, `#ai-agents`, `#workflows`, `#enterprise`, `#industry`

---