---
layout: default
title: "Horizon Summary: 2026-09-01 (ZH)"
date: 2026-09-01
lang: zh
---

> 从 164 条内容中筛选出 11 条重要资讯。

---

**Harness 架构**
1. [FastMCP v4.0.0 发布](#item-harness-arch-1) ⭐️ 7.8/10
2. [agent-framework dotnet-1.20.0 发布](#item-harness-arch-2) ⭐️ 7.8/10
3. [Cline desktop-v0.0.21 发布](#item-harness-arch-3) ⭐️ 6.8/10
4. [Claude Code v2.1.252 发布](#item-harness-arch-4) ⭐️ 5.8/10
5. [Cline desktop-v0.0.21-beta.2 发布](#item-harness-arch-5) ⭐️ 5.8/10
6. [OmniParser GitHub trending](#item-harness-arch-6) ⭐️ 5.0/10

**Agent 工程师日报**
1. [LoopArena 循环工程基准](#item-agent-engineer-1) ⭐️ 7.0/10
2. [StarHarness 发布](#item-agent-engineer-2) ⭐️ 7.0/10

**AI 日报**
1. [ChatGPT Ads 突破 10 亿美元 ARR](#item-ai-daily-1) ⭐️ 8.8/10
2. [Polimill 构建日本公共 AI 基础设施](#item-ai-daily-2) ⭐️ 6.8/10
3. [Gemini 3.7、Jalapeño、Qwen 3.8 发布](#item-ai-daily-3) ⭐️ 5.0/10

---

## Harness 架构

<a id="item-harness-arch-1"></a>
### [FastMCP v4.0.0 发布](https://github.com/PrefectHQ/fastmcp/releases/tag/v4.0.0) ⭐️ 7.8/10

FastMCP 4.0.0 稳定发布，支持新的 MCP 协议，包括无会话请求和协议协商。基于 MCP Python SDK v2 构建，现代请求是无会话且自包含的，任何负载均衡器后的副本都能回答。一个 FastMCP 4 部署在每个连接上协商最佳协议版本，新客户端使用新协议，老客户端继续工作。

github · zzstoatzz · 8月31日 18:19

**「设计要点」** 依赖注入可绑定到调用参数，保持在工具 schema 外。ClientGroup 管理每个服务器一个客户端，碰撞检查命名空间。

**「改了什么」** FastMCP 4 迁移到 MCP SDK v2，支持新协议的无会话和协商机制，移除 3.x 弃用 API 并将背景任务移至 fastmcp-tasks 包。大多数 FastMCP 3 应用无需代码修改即可升级。

**标签**: `#mcp`, `#runtime`, `#tools`

---

<a id="item-harness-arch-2"></a>
### [agent-framework dotnet-1.20.0 发布](https://github.com/microsoft/agent-framework/releases/tag/dotnet-1.20.0) ⭐️ 7.8/10

Microsoft agent-framework .NET 1.20.0 发布。新增 Mem0Sharp 内存集成，支持 Responses API 用于托管 Web 搜索，并修复 Foundry 托管工作流的取消支持和 logprobs 字段。更新多个依赖包并简化 A2A 样本。

github · SergeyMenshykh · 8月31日 18:53

**「改了什么」** 新增 Mem0Sharp 内存集成。使用 Responses API 替换托管 Web 搜索实现，并修复 Foundry 托管工作流的取消支持和 logprobs 字段。简化 A2A 样本并添加等待完成超时。

**标签**: `#runtime`, `#tools`, `#memory`

---

<a id="item-harness-arch-3"></a>
### [Cline desktop-v0.0.21 发布](https://github.com/cline/cline/releases/tag/desktop-v0.0.21) ⭐️ 6.8/10

Cline desktop-v0.0.21 发布。该版本新增两面板市场资源管理器，支持子代理和团队成员的中止操作传播，聊天输入区支持文件拖放，模型提供商列表实时刷新，并将 401/403 认证错误分类为认证问题。Langfuse 追踪在发布版中修复。

github · github-actions\[bot\] · 8月31日 21:41

**「设计要点」** 中止操作现在能正确传播到子代理和团队成员，避免后台残留任务。

**「改了什么」** 相比 v0.0.20，新增两面板市场资源管理器，支持子代理中止传播到子代理和团队成员，以及聊天文件拖拽支持。模型提供商列表实时刷新和认证错误分类也已实现。Langfuse 追踪修复。

**标签**: `#subagents`, `#tools`, `#runtime`

---

<a id="item-harness-arch-4"></a>
### [Claude Code v2.1.252 发布](https://github.com/anthropics/claude-code/releases/tag/v2.1.252) ⭐️ 5.8/10

Claude Code v2.1.252 发布。针对 Mac 上 Bash 命令输出交换失败、always allow 设置持久化、远程控制会话卡顿以及大型失败输出超 API 大小限制等问题进行了修复。

github · ashwin-ant · 8月31日 19:46

**「改了什么」** 修复了 Mac 上 Bash 命令输出交换被拒的问题。修复了 always allow 设置未保存、远程控制会话卡顿以及大型失败输出导致对话超 API 请求大小限制的问题。

**标签**: `#runtime`, `#tools`, `#memory`

---

<a id="item-harness-arch-5"></a>
### [Cline desktop-v0.0.21-beta.2 发布](https://github.com/cline/cline/releases/tag/desktop-v0.0.21-beta.2) ⭐️ 5.8/10

Cline desktop app v0.0.21-beta.2 发布。支持会话从本地无缝接管到云端，继续在云端工作区中操作，并保留提示词、附件和会话状态。新增多环境选择，包括本地、SSH 远程和云端环境，并集成实时语音和头像叠加体验。

github · github-actions\[bot\] · 8月31日 21:08

**「改了什么」** 相比上一版，Cline desktop v0.0.21-beta.2 增加了会话云端接管功能，支持中断转移后的恢复，并新增 SSH 沙箱环境选择和实时语音头像体验。

**标签**: `#memory`, `#sandbox`, `#runtime`, `#tools`

---

<a id="item-harness-arch-6"></a>
### [OmniParser GitHub trending](https://github.com/microsoft/OmniParser) ⭐️ 5.0/10

microsoft/OmniParser 在 GitHub trending，作为纯视觉基础 GUI 代理的屏幕解析工具。
OmniParser 是一种将用户界面截图解析为结构化元素的综合方法，这显著提升了 GPT-4V 生成可准确锚定界面区域动作的能力。

rss · GitHub Trending Daily · 9月1日 01:32

**标签**: `#tools`, `#gui-agent`, `#vision`, `#parsing`

---

## Agent 工程师日报

<a id="item-agent-engineer-1"></a>
### [LoopArena 循环工程基准](https://huggingface.co/papers/2608.28281) ⭐️ 7.0/10

LoopArena 是一个基准，用于评估一个模型如何引导另一个单独的编码代理完成长期任务。该基准区分了循环指导与编码代理能力的贡献。最终一次端到端运行的结果无法区分成功或失败是由于循环指导还是代理能力。

rss · Hugging Face Daily Papers · 9月1日 01:32

**「为什么重要」** 该基准为评估模型作为运行时控制器在循环工程中的表现提供了标准化工具。这对 coding agent harness 开发者有直接相关性。

**「可关注」** 可关注：循环设计需警惕依赖陈旧进度、跳过验证、错误预算分配或在任务未安全提交前停止。

**标签**: `#eval`, `#harness`, `#coding-agent`, `#orchestration`

---

<a id="item-agent-engineer-2"></a>
### [StarHarness 发布](https://huggingface.co/papers/2608.24804) ⭐️ 7.0/10

StarHarness 框架通过分层搜索演化固定权重代理 harness。演化 harness 可包括提示和任务 framing、工具接口、技能、MCP-backed providers、subagent 结构和 agent-loop 配置。在 ITBench SRE、EnterpriseOps-Gym ITSM 和 AutomationBench Finance 基准上，harness 演化比默认 harness 提升 20-35 个百分点，需 4-12 次 accepted changes。这些提升在 held-out 任务上持久存在。

rss · Hugging Face Daily Papers · 9月1日 01:32

**「为什么重要」** StarHarness 框架已实现 20-35pp 提升，已在指定企业基准验证。这为 harness 演化和 eval 改进提供了可验证的方法。

**「可关注」** 可关注：harness 演化池通过分层搜索构建，包含提示和任务 framing、工具接口、技能、MCP-backed providers、subagent 结构和 agent-loop 配置。

**标签**: `#harness`, `#eval`, `#orchestration`, `#coding-agent`, `#MCP`

---

## AI 日报

<a id="item-ai-daily-1"></a>
### [ChatGPT Ads 突破 10 亿美元 ARR](https://openai.com/index/expanding-access-to-ai-with-chatgpt-ads) ⭐️ 8.8/10

ChatGPT Ads 达到 10 亿美元年化收入跑率。产品全球扩张。支持通过免费和可负担选项更广泛访问 AI。

rss · OpenAI Blog · 8月31日 04:00

**「为什么重要」** ChatGPT Ads 达到 10 亿美元 ARR，标志着 AI 广告模式的里程碑。全球扩张支持免费和可负担 AI 访问。

**「可关注」** 可关注：ChatGPT Ads 全球扩张，支持免费和可负担 AI 访问。

**标签**: `#openai`, `#ads`, `#revenue`, `#access`, `#product`

---

<a id="item-ai-daily-2"></a>
### [Polimill 构建日本公共 AI 基础设施](https://openai.com/index/polimill) ⭐️ 6.8/10

Polimill 构建日本公共 AI 基础设施。Polimill 部署 OpenAI GPT 模型和 Codex 协助 municipalities 搜索行政知识并加速发展。

rss · OpenAI Blog · 8月31日 07:00

**「可关注」** 可关注：Polimill 使用 OpenAI GPT 模型和 Codex 协助 municipalities 搜索行政知识并加速发展。

**标签**: `#openai`, `#gpt`, `#industry`, `#public-ai`, `#partnership`

---

<a id="item-ai-daily-3"></a>
### [Gemini 3.7、Jalapeño、Qwen 3.8 发布](https://lastweekin.ai/p/lwiai-podcast-255-gemini-37-jalapeno) ⭐️ 5.0/10

本期 LWiAI Podcast \#255 报道了谷歌发布 Gemini 3.7 Flash。Jalapeño 的首发结果显示行业领先速度。还介绍了 Qwen 3.8 以及一起由 AI 完全引导导致三名乌克兰人死亡的无人机事件。

rss · Last Week in AI · 8月31日 08:20

**「可关注」** 可关注：Jalapeño 首发结果显示行业领先速度。

**标签**: `#model`, `#gemini`, `#google`, `#qwen`, `#drone`, `#podcast`

---