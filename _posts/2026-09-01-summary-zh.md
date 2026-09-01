---
layout: default
title: "Horizon Summary: 2026-09-01 (ZH)"
date: 2026-09-01
lang: zh
---

> 从 174 条内容中筛选出 15 条重要资讯。

---

**Harness 架构**
1. [FastMCP v4.0.0 发布](#item-harness-arch-1) ⭐️ 7.8/10
2. [Cline desktop-v0.0.21-beta.2 发布](#item-harness-arch-2) ⭐️ 6.8/10
3. [anthropics/claude-code v2.1.252 发布](#item-harness-arch-3) ⭐️ 5.8/10
4. [Cline desktop-v0.0.21 发布](#item-harness-arch-4) ⭐️ 5.8/10
5. [pydantic-ai v2.37.0 发布](#item-harness-arch-5) ⭐️ 5.8/10
6. [microsoft/agent-framework dotnet-1.20.0 发布](#item-harness-arch-6) ⭐️ 5.8/10
7. [OmniParser 登 GitHub trending](#item-harness-arch-7) ⭐️ 5.0/10
8. [anthropics/claude-cookbooks trending](#item-harness-arch-8) ⭐️ 5.0/10

**Agent 工程师日报**
1. [StarHarness：分层搜索演化企业 harness](#item-agent-engineer-1) ⭐️ 8.0/10
2. [Wrapture 发布](#item-agent-engineer-2) ⭐️ 7.0/10
3. [DART-SD 多轮工具调用自蒸馏框架](#item-agent-engineer-3) ⭐️ 6.0/10
4. [ElephantBench 发布：LLM 长尾知识探针](#item-agent-engineer-4) ⭐️ 6.0/10

**AI 日报**
1. [ChatGPT Ads 突破 10 亿年化收入](#item-ai-daily-1) ⭐️ 6.8/10
2. [Polimill 构建日本公共 AI 基础设施](#item-ai-daily-2) ⭐️ 5.8/10
3. [Gemini 3.7 Flash 发布，Jalapeño 首测](#item-ai-daily-3) ⭐️ 5.0/10

---

## Harness 架构

<a id="item-harness-arch-1"></a>
### [FastMCP v4.0.0 发布](https://github.com/PrefectHQ/fastmcp/releases/tag/v4.0.0) ⭐️ 7.8/10

FastMCP v4.0.0 发布，作为 July 2026 MCP 协议修订的参考实现，支持无会话自包含请求和负载均衡友好部署。

单个部署可为每个连接协商最佳协议版本，新客户端使用新协议，老客户端保持兼容。

交互工具返回输入请求，并在客户端提供答案后重新执行，背景任务通过扩展支持。

github · zzstoatzz · 8月31日 18:19

**「设计要点」** 单个部署支持协议版本协商，负载均衡器可直接路由无会话请求。交互工具通过上下文传递实现多轮交互。

**「改了什么」** FastMCP 3 应用大多无需代码修改即可升级。重大变更包括移除服务器发起的采样和根，ctx.elicit\(\) 仅限旧协议，背景任务移至 fastmcp-tasks 包，模型字段改为 snake\_case。

**标签**: `#mcp`, `#runtime`, `#tools`, `#permissions`, `#memory`

---

<a id="item-harness-arch-2"></a>
### [Cline desktop-v0.0.21-beta.2 发布](https://github.com/cline/cline/releases/tag/desktop-v0.0.21-beta.2) ⭐️ 6.8/10

Cline desktop-v0.0.21-beta.2 发布。桌面应用新增云端会话交接 beta 功能，支持本地会话无缝切换到 Cline Cloud 并继续工作，保留提示词、附件和会话状态。新增环境选择功能，可在本地、SSH 远程和 Cloud 环境间切换。包含此前稳定版改进，包括 Windows 支持和工具结果处理。

github · github-actions\[bot\] · 8月31日 21:08

**「改了什么」** 相对上一版，新增云端会话交接 beta 功能，支持本地会话切换到 Cline Cloud 并保留状态。新增环境选择功能，可在本地、SSH 远程和 Cloud 环境间切换，GitHub onboarding 功能置于 \`code-onboarding-github\` feature flag 后，默认禁用。

**标签**: `#memory`, `#runtime`, `#tools`

---

<a id="item-harness-arch-3"></a>
### [anthropics/claude-code v2.1.252 发布](https://github.com/anthropics/claude-code/releases/tag/v2.1.252) ⭐️ 5.8/10

anthropics/claude-code v2.1.252 发布。修复了 Mac 上 Bash 命令失败的问题。修复了 always allow 设置持久化问题。修复了远程会话卡顿。修复了大型失败输出超限。

github · ashwin-ant · 8月31日 19:46

**「改了什么」** 修复了 Mac 上 Bash 命令 &\#x27;task output swap refused&\#x27; 失败，以及 always allow 设置在无 .claude/settings.local.json 项目中不保存。修复了 Remote Control 会话卡顿以及大型失败输出导致 API 请求超限。

**标签**: `#runtime`, `#tools`, `#permissions`

---

<a id="item-harness-arch-4"></a>
### [Cline desktop-v0.0.21 发布](https://github.com/cline/cline/releases/tag/desktop-v0.0.21) ⭐️ 5.8/10

Cline desktop-v0.0.21 发布。市场界面升级为双窗格浏览模式，支持分类过滤。会话停止功能增强，可终止子代理和队友。提供商模型目录实时刷新，并修复多项工具和追踪问题。

github · github-actions\[bot\] · 8月31日 21:41

**「改了什么」** 市场界面升级为双窗格浏览模式。会话停止功能增强，可终止子代理和队友。

**标签**: `#subagents`, `#tools`, `#runtime`

---

<a id="item-harness-arch-5"></a>
### [pydantic-ai v2.37.0 发布](https://github.com/pydantic/pydantic-ai/releases/tag/v2.37.0) ⭐️ 5.8/10

pydantic-ai v2.37.0 发布了。新增 glm-5.3-flash 模型并重构了 Z.AI 测试套件。修复了模型路由、UI 消息、span 查询和能力钩子相关问题。

github · dsfaccini · 9月1日 01:48

**「改了什么」** 新增 glm-5.3-flash 模型并重构了 Z.AI 测试套件。

**标签**: `#runtime`, `#tools`, `#eval`

---

<a id="item-harness-arch-6"></a>
### [microsoft/agent-framework dotnet-1.20.0 发布](https://github.com/microsoft/agent-framework/releases/tag/dotnet-1.20.0) ⭐️ 5.8/10

microsoft/agent-framework .NET 1.20.0 发布。新增 Mem0Sharp 集成，用于代理样本中的内存存储。使用 Responses API 实现 AG-UI 的托管 Web 搜索。修复了 Responses logprobs 字段保留、Foundry 托管工作流取消支持等问题。

github · SergeyMenshykh · 8月31日 18:53

**「改了什么」** 相对上一版，新增 Mem0Sharp 集成和 Responses API 用于 AG-UI web search。修复了 Responses logprobs 字段保留、Foundry 托管工作流取消支持等问题。

**标签**: `#memory`, `#runtime`, `#tools`

---

<a id="item-harness-arch-7"></a>
### [OmniParser 登 GitHub trending](https://github.com/microsoft/OmniParser) ⭐️ 5.0/10

OmniParser 是 Microsoft 推出的屏幕解析工具，针对纯视觉 GUI 代理设计。该工具将用户界面截图解析为结构化且易于理解的元素，显著增强 GPT-4V 生成可 grounding 的动作。目前在 GitHub trending 榜单上。项目页面、V2 博客、模型 V2、模型 V1.5 以及 HuggingFace Space Demo 已上线。

rss · GitHub Trending Daily · 9月1日 01:54

**标签**: `#tools`, `#subagents`, `#vision`

---

<a id="item-harness-arch-8"></a>
### [anthropics/claude-cookbooks trending](https://github.com/anthropics/claude-cookbooks) ⭐️ 5.0/10

anthropics/claude-cookbooks 仓库在 GitHub trending。该仓库提供 Claude AI 笔记本和 recipes，包含可复制的代码片段，帮助开发者集成 Claude。代码示例主要使用 Python，但概念可适配任何编程语言。使用前需准备 Claude API key。

rss · GitHub Trending Daily · 9月1日 01:54

**标签**: `#tools`, `#planning`, `#notebooks`

---

## Agent 工程师日报

<a id="item-agent-engineer-1"></a>
### [StarHarness：分层搜索演化企业 harness](https://huggingface.co/papers/2608.24804) ⭐️ 8.0/10

StarHarness 框架通过分层任务搜索演化企业特定 agent harness，保持模型权重不变。演化 harness 可包含提示词和任务 framing、工具接口、技能、MCP-backed providers、子代理结构以及 agent 循环配置。在 ITBench SRE、EnterpriseOps-Gym ITSM 和 AutomationBench Finance 基准上，演化后性能较默认 harness 提升 20-35 个百分点（4-12 次 accepted changes 后）。这些提升在 held-out 任务上仍保持。

rss · Hugging Face Daily Papers · 9月1日 01:54

**「为什么重要」** StarHarness 框架已验证演化后性能提升 20-35pp，这已发生。尚未证实的是其对 harness/eval/toolchain 设计的长期影响。

**「可关注」** 可关注：演化后性能在 held-out 任务上仍保持。

**标签**: `#harness`, `#mcp`, `#eval`, `#orchestration`, `#coding-agent`

---

<a id="item-agent-engineer-2"></a>
### [Wrapture 发布](https://simonwillison.net/2026/Aug/31/introducing-wrapture/) ⭐️ 7.0/10

Wrapture 是一个 Python 函数包装库，由 Graham Dumpleton 开发。它允许对函数或方法进行包装，实现追踪或覆盖返回值为不同值。作为 unittest.mock 替代方案和现有项目追踪工具。项目包含 OpenTelemetry 支持，并提供配置化追踪机制。项目仅数周前发布。

rss · Simon Willison · 8月31日 23:59

**「为什么重要」** Wrapture 发布后，将影响代理 harness、评估和观测工具链。

**「可关注」** 可关注：Wrapture 支持通过 TOML 配置添加追踪。

**标签**: `#harness`, `#eval`, `#tracing`, `#observability`, `#mocking`

---

<a id="item-agent-engineer-3"></a>
### [DART-SD 多轮工具调用自蒸馏框架](https://huggingface.co/papers/2608.18524) ⭐️ 6.0/10

DART-SD 框架提出解决多轮工具调用中的拓扑塌缩问题。该框架针对包含多个顺序独立子目标的任务，通过钻石拓扑感知检索和自蒸馏，从全局强制转向拓扑引导的局部纠正。DART-SD 模型化执行过程以保留策略多样性。

rss · Hugging Face Daily Papers · 9月1日 01:54

**「为什么重要」** DART-SD 框架的提出针对自主代理中多轮工具调用的核心限制。该方法在今天的 agent 构建中具有相关性。

**「可关注」** 可关注：多轮工具调用中全长轨迹模仿导致拓扑塌缩，策略多样性下降。

**标签**: `#coding-agent`, `#orchestration`, `#eval`, `#tool-calling`, `#self-distillation`

---

<a id="item-agent-engineer-4"></a>
### [ElephantBench 发布：LLM 长尾知识探针](https://huggingface.co/papers/2608.28478) ⭐️ 6.0/10

HF 日报发布 ElephantBench，包含 1,094 个多账号 QA 记录。通过可审计图谱管道从低曝光 web 语料生成，测试 LLM 在长尾事实上的认知盲区。32 个模型测试显示，最强模型仅在 52.4% 问题上同时召回两个账号，在剩余问题中通常只召回一个。

rss · Hugging Face Daily Papers · 9月1日 01:54

**「为什么重要」** ElephantBench 提供新工具评估 LLM 知识一致性，直接影响 eval 和 harness 的改进。

**「可关注」** 可关注：32 个模型中，最强模型双账号召回率仅 52.4%。

**标签**: `#eval`, `#harness`, `#benchmark`, `#knowledge-probing`

---

## AI 日报

<a id="item-ai-daily-1"></a>
### [ChatGPT Ads 突破 10 亿年化收入](https://openai.com/index/expanding-access-to-ai-with-chatgpt-ads) ⭐️ 6.8/10

OpenAI 宣布 ChatGPT Ads 年化收入跑率达到 10 亿美元。该业务全球扩展。该扩展支持通过免费和实惠选项扩大 AI 访问。

rss · OpenAI Blog · 8月31日 04:00

**「为什么重要」** ChatGPT Ads 的全球扩展支持通过免费和实惠选项扩大 AI 访问。

**「可关注」** 可关注：ChatGPT Ads 年化收入跑率达到 10 亿美元。

**标签**: `#openai`, `#chatgpt`, `#ads`, `#revenue`, `#access`

---

<a id="item-ai-daily-2"></a>
### [Polimill 构建日本公共 AI 基础设施](https://openai.com/index/polimill) ⭐️ 5.8/10

Polimill 正在构建日本下一代公共 AI 基础设施。OpenAI GPT 模型和 Codex 被用于帮助 municipalities 搜索和应用行政知识，同时加速开发。这是 OpenAI 官方博客宣布的合作项目。

rss · OpenAI Blog · 8月31日 07:00

**「为什么重要」** OpenAI 官方博客宣布与 Polimill 合作，将 GPT 模型和 Codex 引入日本公共 AI 基础设施。

**「可关注」** 可关注：Polimill 使用 OpenAI GPT 模型和 Codex 帮助 municipalities 搜索和应用行政知识。

**标签**: `#openai`, `#product`, `#industry`, `#japan`, `#partnership`

---

<a id="item-ai-daily-3"></a>
### [Gemini 3.7 Flash 发布，Jalapeño 首测](https://lastweekin.ai/p/lwiai-podcast-255-gemini-37-jalapeno) ⭐️ 5.0/10

Google 发布 Gemini 3.7 Flash 模型。Jalapeño 首测速度领先行业。Qwen 3.8 发布。一架 AI 引导的无人机在乌克兰导致三人死亡。

rss · Last Week in AI · 8月31日 08:20

**「为什么重要」** 这些模型发布和事件反映了 AI 技术在速度、安全方面的最新进展。

**「可关注」** Jalapeño 首测速度领先行业。

**标签**: `#model`, `#lab`, `#industry`, `#product`

---