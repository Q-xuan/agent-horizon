---
layout: default
title: "Horizon Summary: 2026-09-02 (ZH)"
date: 2026-09-02
lang: zh
---

> 从 200 条内容中筛选出 16 条重要资讯。

---

**Harness 架构**
1. [Langchain 1.4.0a3 发布](#item-harness-arch-1) ⭐️ 8.8/10
2. [claude-code v2.1.257 发布](#item-harness-arch-2) ⭐️ 7.8/10
3. [Codex rust-v0.152.0 发布](#item-harness-arch-3) ⭐️ 7.8/10
4. [gemini-cli v0.59.0-preview.0 发布](#item-harness-arch-4) ⭐️ 7.8/10
5. [opencode v1.18.26 发布](#item-harness-arch-5) ⭐️ 7.8/10
6. [Graphiti v0.30.0 发布](#item-harness-arch-6) ⭐️ 7.8/10
7. [Gemini CLI v0.58.0 发布](#item-harness-arch-7) ⭐️ 6.8/10

**Agent 工程师日报**
1. [Gemini agentic video understanding 发布](#item-agent-engineer-1) ⭐️ 7.8/10
2. [Claude Fable 5.1 发布](#item-agent-engineer-2) ⭐️ 7.0/10
3. [BenchMIRT 发布：LLM 基准测什么](#item-agent-engineer-3) ⭐️ 6.8/10

**AI 日报**
1. [ChatGPT 连接 EHR 医疗数据](#item-ai-daily-1) ⭐️ 9.8/10
2. [Astra 首达关键网络安全能力门槛](#item-ai-daily-2) ⭐️ 7.8/10
3. [OpenAI：AI-native 公司工作流转运营](#item-ai-daily-3) ⭐️ 6.8/10

**AI 羊毛**
1. [浏览器免费预览：移除音频视频背景噪音](#item-ai-deals-1) ⭐️ 5.0/10
2. [DaemonCore Academy 127 免费网络安全课程](#item-ai-deals-2) ⭐️ 5.0/10
3. [Sketchometry.org 指尖几何草图工具](#item-ai-deals-3) ⭐️ 5.0/10

---

## Harness 架构

<a id="item-harness-arch-1"></a>
### [Langchain 1.4.0a3 发布](https://github.com/langchain-ai/langchain/releases/tag/langchain%3D%3D1.4.0a3) ⭐️ 8.8/10

LangChain 1.4.0a3 alpha 发布，新增 langchain.mcp 命名空间，用于将 MCP 服务器适配为 LangChain 工具。
MCPAdapter 支持 URL、脚本、MCPConfig 或客户端作为后端，list\_tools 支持缓存模式（SEP-2549），as\_langchain\_tool 转换单个工具。
工具元数据分组在 mcp 命名空间下，elicitation=&quot;interrupt&quot; 支持 LangGraph 中断。
需要 mcp 额外包：pip install &quot;langchain\[mcp\]&quot;。

github · github-actions\[bot\] · 9月1日 17:19

**「改了什么」** 引入 langchain.mcp 命名空间，支持 MCPAdapter、工具发现与缓存（SEP-2549）、as\_langchain\_tool 以及 mcp 命名空间下的工具元数据。

**标签**: `#mcp`, `#tools`, `#runtime`

---

<a id="item-harness-arch-2"></a>
### [claude-code v2.1.257 发布](https://github.com/anthropics/claude-code/releases/tag/v2.1.257) ⭐️ 7.8/10

claude-code v2.1.257 是 Anthropic 发布的 Claude Code 工具。新增默认 Fable 模型 claude-fable-5-1，支持 1M 上下文，定价 $10/$50 per Mtok，缓存读取 $0.25/Mtok。添加了时间格式和时区设置、子代理模型强制选项 CLAUDE\_CODE\_SUBAGENT\_MODEL\_FORCE、沙箱逃逸防止规则以及自动模式文件读取提示。添加了 /doctor 警告功能。

github · ashwin-ant · 9月1日 17:53

**「改了什么」** 本次发布新增默认 Fable 模型 claude-fable-5-1 和子代理模型强制选项。添加了时间格式和时区设置、沙箱逃逸防止规则以及 /doctor 警告功能。

**标签**: `#subagents`, `#sandbox`, `#permissions`, `#runtime`, `#planning`

---

<a id="item-harness-arch-3"></a>
### [Codex rust-v0.152.0 发布](https://github.com/openai/codex/releases/tag/rust-v0.152.0) ⭐️ 7.8/10

OpenAI Codex Rust v0.152.0 发布。MCP 服务器名称支持冒号、@、/ 和 .，符合包样式的命名。每个 MCP 工具支持 output\_token\_limit 设置，并保持会话恢复时的截断一致性。App-server 客户端可配置 thread/shellCommand 超时，包括超过一小时的截止时间。

github · github-actions\[bot\] · 9月1日 01:58

**「改了什么」** 相对上一版，新增支持包样式的 MCP 服务器名称，并添加 per-tool output\_token\_limit 配置，确保截断一致性。App-server 客户端支持配置超过一小时的线程和 shellCommand 超时。

**标签**: `#mcp`, `#tools`, `#runtime`

---

<a id="item-harness-arch-4"></a>
### [gemini-cli v0.59.0-preview.0 发布](https://github.com/google-gemini/gemini-cli/releases/tag/v0.59.0-preview.0) ⭐️ 7.8/10

gemini-cli v0.59.0-preview.0 发布。修复了 MCP OAuth 元数据发现和认证中的 SSRF 漏洞。强制执行受限模式下的工作区信任和 mcpServer 过滤。

github · gemini-cli-robot · 9月1日 20:19

**「设计要点」** 受限模式下强制 fail-closed 工作区信任，并通过 mcpServer 过滤。

**「改了什么」** 修复了 MCP OAuth 元数据发现和认证中的 SSRF 漏洞。强制执行受限模式下的工作区信任和 mcpServer 过滤。

**标签**: `#mcp`, `#permissions`, `#runtime`, `#tools`

---

<a id="item-harness-arch-5"></a>
### [opencode v1.18.26 发布](https://github.com/anomalyco/opencode/releases/tag/v1.18.26) ⭐️ 7.8/10

opencode v1.18.26 发布。修复了 Claude 5 会话思考块过时问题、Bedrock GPT-5.6 模型 reasoning effort 支持、工具调用计时准确性以及 apply\_patch 权限元数据空路径问题。Azure CLI 登录现在直接询问资源名称。

github · opencode-agent\[bot\] · 9月1日 21:52

**「改了什么」** Claude 会话思考块和 Bedrock 推理处理得到修复，工具调用计时更准确，apply\_patch 权限元数据不再包含空路径。Azure CLI 登录直接询问资源名称，会话重命名在标题编辑器和标签上下文菜单中可靠保存。

**标签**: `#runtime`, `#tools`, `#permissions`

---

<a id="item-harness-arch-6"></a>
### [Graphiti v0.30.0 发布](https://github.com/getzep/graphiti/releases/tag/v0.30.0) ⭐️ 7.8/10

Graphiti v0.30.0 发布。
Neo4j 查询执行现在尊重配置的数据库（默认 neo4j）。
并记录了受影响的自托管多数据库部署。
支持通过 execute\_query\(..., database\_=&quot;name&quot;\) 进行 per-call override。

github · prasmussen15 · 9月1日 18:20

**「改了什么」** 修正 Neo4j 查询执行以尊重配置的数据库（默认 neo4j）。
这是针对自托管 Neo4j Enterprise 多数据库部署的行为变更。

**标签**: `#runtime`, `#tools`, `#memory`

---

<a id="item-harness-arch-7"></a>
### [Gemini CLI v0.58.0 发布](https://github.com/google-gemini/gemini-cli/releases/tag/v0.58.0) ⭐️ 6.8/10

Google Gemini CLI v0.58.0 发布。修复了 macOS Seatbelt 下的沙箱隔离问题和 A2A 服务器的取消错误。核心重构移除 ESLint 禁用和类型断言。

github · gemini-cli-robot · 9月1日 20:51

**「设计要点」** macOS 上通过 Seatbelt 隔离 Docker 和容器运行时套接字及二进制文件。

**「改了什么」** 相对上一版 v0.57.0，沙箱隔离修复和 A2A 服务器取消错误修复。核心重构移除 ESLint 禁用和类型断言。

**标签**: `#sandbox`, `#runtime`

---

## Agent 工程师日报

<a id="item-agent-engineer-1"></a>
### [Gemini agentic video understanding 发布](https://deepmind.google/blog/introducing-agentic-video-in-gemini/) ⭐️ 7.8/10

Google DeepMind 宣布将 agentic video understanding 功能集成到 Gemini 模型中。
这一新特性由官方博客介绍。
它影响 coding-agent、eval 和 orchestration 领域。

rss · Google DeepMind · 9月1日 17:08

**「为什么重要」** Google DeepMind 官方博客发布了这一公告。
尚未证实其在代理系统中的具体影响。

**「可关注」** 可关注：Gemini 集成 agentic video understanding 功能。

**标签**: `#coding-agent`, `#eval`, `#orchestration`

---

<a id="item-agent-engineer-2"></a>
### [Claude Fable 5.1 发布](https://www.anthropic.com/claude-fable-and-mythos-5-1) ⭐️ 7.0/10

Anthropic 发布了 Claude Fable 5.1 和 Claude Mythos 5.1。模型在写作风格上获得升级，指令遵循能力增强，缓存读取成本从 $1/M 降至 $0.25/M。系统卡 PDF 和基准测试洞察已发布。

hackernews · denysvitali · 9月1日 17:53 · [社区讨论](https://news.ycombinator.com/item?id=49525378)

**「为什么重要」** 已发生的变更包括缓存读取价格从 $1/M 降至 $0.25/M。尚未证实其对代理 harness 的长期影响。

**「可关注」** 可关注：缓存读取成本降至 $0.25/M，这可能影响代理内存管理的成本。

**「评论」** Felix Rieseberg 表示 Fable 5.1 写作风格更自然，指令遵循更可靠。Simon Willison 分享了 Pelican 评估的思考努力痕迹，显示高努力级别有显著改进。GodelNumbering 分析了价格变化对 Terminal-Bench-Science 的影响。

**标签**: `#eval`, `#coding-agent`, `#harness`, `#orchestration`, `#memory`

---

<a id="item-agent-engineer-3"></a>
### [BenchMIRT 发布：LLM 基准测什么](https://huggingface.co/blog/allenai/benchmirt) ⭐️ 6.8/10

BenchMIRT 是 AllenAI 提出的新方法，用于逐个提示审计 LLM 基准。研究者用其分析了 100 个 LLM 在 16 个基准上的 34000 多个问题，独立恢复出安全和一般推理两个维度。BBQ 基准与推理能力关联更强，WMDP 得分也与推理相关而非安全，HarmBench 信号混合。这些发现显示单个基准分数可结合多个信号，BenchMIRT 可帮助分离信号。模型数据截至 2025 年 3 月，分析结果稳定但影响实践待验证。

rss · Hugging Face Blog · 9月1日 21:39

**「为什么重要」** BenchMIRT 已发布，可帮助分离基准中的不同信号，使分数解释更清晰。但其在实际基准设计中的影响尚未证实。

**「可关注」** 可关注：使用 BenchMIRT 能从 10% 问题中保留近似能力测量。

**标签**: `#eval`, `#harness`, `#benchmarks`

---

## AI 日报

<a id="item-ai-daily-1"></a>
### [ChatGPT 连接 EHR 医疗数据](https://openai.com/index/chatgpt-connects-health-records-and-healthcare-sources) ⭐️ 9.8/10

OpenAI 让 ChatGPT 连接可信医疗数据，帮助临床医生安全访问患者上下文和医学研究。
这一集成允许医疗机构将 EHR 和行业数据接入 ChatGPT。
该功能提供安全访问患者上下文和医疗研究的途径。

rss · OpenAI Blog · 9月1日 12:00

**「可关注」** 可关注：ChatGPT 集成 EHR 数据后，临床医生可安全访问患者上下文和医疗研究。

**标签**: `#openai`, `#chatgpt`, `#healthcare`, `#ehr`, `#integration`, `#product`

---

<a id="item-ai-daily-2"></a>
### [Astra 首达关键网络安全能力门槛](https://openai.com/index/path-to-astra) ⭐️ 7.8/10

Astra 是 OpenAI 首个达到关键网络安全能力门槛的模型。根据 Preparedness Framework，Astra 配备更强的保障措施以便发布。

rss · OpenAI Blog · 9月1日 13:00

**「为什么重要」** OpenAI 首次满足关键网络安全能力门槛，标志着模型安全标准的新水平。

**「可关注」** 可关注：Astra 配备更强的保障措施

**标签**: `#model`, `#openai`, `#policy`, `#product`, `#eval`

---

<a id="item-ai-daily-3"></a>
### [OpenAI：AI-native 公司工作流转运营](https://openai.com/index/ai-native-company-workflows) ⭐️ 6.8/10

OpenAI 博客介绍了 AI-native 公司如何将工作流转化为运营能力。Basis、Clay 和 Exa Labs 通过 AI 代理优化了入职、账户管理和开发者集成。企业领导者可以应用这些方法。

rss · OpenAI Blog · 9月1日 17:00

**「为什么重要」** 企业可通过 AI 代理提升工作流效率。

**「可关注」** 可关注：AI 代理在入职、账户管理和开发者集成中的应用。

**标签**: `#openai`, `#ai-agents`, `#ai-native`, `#workflows`, `#enterprise`

---

## AI 羊毛

<a id="item-ai-deals-1"></a>
### [浏览器免费预览：移除音频视频背景噪音](https://removebackgroundnoise.app/) ⭐️ 5.0/10

浏览器免费预览工具 removebackgroundnoise.app 提供音频和视频文件背景噪音移除功能。无需下载或安装，即可直接使用。材料中未列出具体额度或截止时间，描述为立即可用。

rss · HN Free API / Credits · 9月2日 00:02

**「可关注」** 可关注：浏览器直接使用，无需安装。

**标签**: `#free-tier`, `#limited-free`, `#promo`, `#tool`, `#audio`

---

<a id="item-ai-deals-2"></a>
### [DaemonCore Academy 127 免费网络安全课程](https://academy.daemoncore.app/) ⭐️ 5.0/10

DaemonCore Academy 提供 127 个免费的网络安全课程。课程包括可丢弃的 Docker 镜像。这些镜像用于网络安全练习。

rss · HN Free API / Credits · 9月1日 20:30

**标签**: `#promo`, `#free-tier`, `#limited-free`

---

<a id="item-ai-deals-3"></a>
### [Sketchometry.org 指尖几何草图工具](https://start.sketchometry.org/) ⭐️ 5.0/10

Sketchometry.org 提供免费的指尖几何草图工具。用户可直接用手指在网页上绘制几何图形。无需注册、无限使用、无截止时间。

rss · HN Free API / Credits · 9月1日 14:23

**「为什么重要」** 这款工具立即可用且完全免费，适合快速绘制几何图形。

**「可关注」** 可关注：无需注册即可使用。

**标签**: `#free-tier`, `#promo`, `#free-tool`

---