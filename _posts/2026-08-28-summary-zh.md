---
layout: default
title: "Horizon Summary: 2026-08-28 (ZH)"
date: 2026-08-28
lang: zh
---

> 从 177 条内容中筛选出 13 条重要资讯。

---

**Harness 架构**
1. [Claude Code 2.1.248 发布](#item-harness-arch-1) ⭐️ 8.5/10
2. [Cloudflare Agents @0.17.0 发布](#item-harness-arch-2) ⭐️ 7.5/10
3. [Cline Desktop v0.0.20 发布](#item-harness-arch-3) ⭐️ 6.5/10
4. [cloudflare/agents @cloudflare/voice-assemblyai@0.1.0 发布](#item-harness-arch-4) ⭐️ 6.5/10
5. [LangChain 1.4.0a1 发布](#item-harness-arch-5) ⭐️ 6.5/10
6. [instructor v1.16.0 发布](#item-harness-arch-6) ⭐️ 6.5/10
7. [Agent Framework Python 1.16.0 发布](#item-harness-arch-7) ⭐️ 6.5/10

**Agent 工程师日报**
1. [DeepMind 世界首个双盲 AI 评估试点](#item-agent-engineer-1) ⭐️ 7.5/10
2. [Claude Code Opus 5 Auto Mode 被提示注入攻击](#item-agent-engineer-2) ⭐️ 7.0/10
3. [Gemini Omni 1.1 Flash 发布](#item-agent-engineer-3) ⭐️ 5.5/10

**AI 日报**
1. [ChatGPT 结合批判性思维训练：学生研究](#item-ai-daily-1) ⭐️ 6.5/10
2. [OpenAI 巴西业务拓展](#item-ai-daily-2) ⭐️ 5.5/10

**AI 羊毛**
1. [免费无框架 RAG/Agent Colab 笔记](#item-ai-deals-1) ⭐️ 6.0/10

---

## Harness 架构

<a id="item-harness-arch-1"></a>
### [Claude Code 2.1.248 发布](https://code.claude.com/docs/en/changelog#2-1-248) ⭐️ 8.5/10

Claude Code 2.1.248 发布了更新。该版本添加了受限模式 \(--restricted 或 CLAUDE\_CODE\_RESTRICTED=1\)，该模式移除内置的命令或代码运行工具以及 WebFetch（除非在 --tools 中指定），保留工作目录内的文件工具，拒绝 bypassPermissions，并忽略用户、项目和本地设置文件。还添加了实验性的 per-agent prompt cache TTL 设置（&quot;5m&quot; 或 &quot;1h&quot;），以及自定义 self-hosted runner 标签的功能（claude self-hosted-runner --client-label &lt;label&gt;）。此外，提供了服务器管理的设置加载诊断，包括启动警告和 /doctor /status 命令。

rss · Claude Code Changelog · 8月27日 22:19

**「改了什么」** 相对于上一版，本次更新引入了受限模式，添加了 per-agent prompt cache TTL，以及自定义 self-hosted runner 标签，并增加了设置加载诊断。

**标签**: `#runtime`, `#tools`, `#permissions`, `#memory`

---

<a id="item-harness-arch-2"></a>
### [Cloudflare Agents @0.17.0 发布](https://github.com/cloudflare/agents/releases/tag/%40cloudflare/think%400.17.0) ⭐️ 7.5/10

Cloudflare Agents @0.17.0 更新了 AIChatAgent 和 Think，使每个聊天回合无条件地在持久恢复 fiber 中运行，包括 WebSocket、程序化、重试和延续路径。chatRecovery 配置接受 true 或配置对象，false 不再支持。还新增 Scheduler 作为 Lifecycle 的可重用能力，用于持久延迟、定时和间隔回调。

github · ben-reitz · 8月27日 14:07

**「设计要点」** 更新使 durable chat recovery 成为无条件行为，使用 recovery fiber 处理 WebSocket/programmatic/retry/continuation 路径，并支持 onChatRecovery hook 和 durable cancellation。Scheduler 管理持久调度。

**「改了什么」** AIChatAgent 和 Think 现在无条件运行每个聊天回合在 durable recovery fiber 中。chatRecovery 配置不再支持 false。新增 Scheduler 能力，支持持久调度回调。

**标签**: `#runtime`, `#memory`, `#planning`

---

<a id="item-harness-arch-3"></a>
### [Cline Desktop v0.0.20 发布](https://github.com/cline/cline/releases/tag/desktop-v0.0.20) ⭐️ 6.5/10

Cline Desktop v0.0.20 发布了 Windows 支持，包含代码签名 x64 安装器并支持自动更新。工具返回图片时支持内联渲染和轮播查看。会话搜索覆盖完整历史，通过命令栏（Cmd/Ctrl+P）提供服务器排序结果。

github · github-actions\[bot\] · 8月28日 01:33

**「改了什么」** 相比 v0.0.19，Windows 后台进程不再弹出控制台窗口，计划任务在重启后不再消失。工具结果渲染改为支持轮播查看，会话搜索覆盖完整历史记录。

**标签**: `#runtime`, `#tools`, `#mcp`, `#memory`, `#planning`

---

<a id="item-harness-arch-4"></a>
### [cloudflare/agents @cloudflare/voice-assemblyai@0.1.0 发布](https://github.com/cloudflare/agents/releases/tag/%40cloudflare/voice-assemblyai%400.1.0) ⭐️ 6.5/10

这是 cloudflare/agents 仓库发布的 @cloudflare/voice-assemblyai@0.1.0 版本。该版本改进了语音生命周期准确性、诊断功能和每轮时间可见性。保留了现有的四字段指标线形状，同时使 no-audio 和 streamed TTS 记账一致。更新了 bundled voice providers 以一致地传播生命周期失败和日志错误。

github · ben-reitz · 8月27日 14:07

**「改了什么」** 这是 @cloudflare/voice-assemblyai@0.1.0 的发布版本。改进了语音生命周期准确性、诊断和每轮时间可见性。

**标签**: `#runtime`, `#tools`

---

<a id="item-harness-arch-5"></a>
### [LangChain 1.4.0a1 发布](https://github.com/langchain-ai/langchain/releases/tag/langchain%3D%3D1.4.0a1) ⭐️ 6.5/10

LangChain 1.4.0a1 正式发布，引入了 MCP 协议适配器，并进行了代码组织重构和多服务器协议测试覆盖。保留了版本号 langchain==1.4.0a1。

github · github-actions\[bot\] · 8月27日 22:21

**「改了什么」** 相对于上一版 1.3.18，1.4.0a1 增加了 MCP 协议适配器支持，并重构了 elicitation 类型 per mode 以及协议 era 处理。

**标签**: `#mcp`, `#tools`, `#runtime`, `#refactor`, `#protocol`

---

<a id="item-harness-arch-6"></a>
### [instructor v1.16.0 发布](https://github.com/567-labs/instructor/releases/tag/v1.16.0) ⭐️ 6.5/10

567-labs/instructor v1.16.0 发布了新版本，新增了对 Bedrock 的原生结构化输出支持。支持通过 Converse 的 outputConfig.textFormat 设置 Mode.JSON\_SCHEMA 和 Mode.TOOLS\_STRICT，并进行了递归 schema 归一化。还添加了验证重试预算，包括累积的 token\_budget 限制和不可变的 completion:usage 快照。保留了之前的接口和限制，包括 boto3 最低版本 1.42.42。

github · github-actions\[bot\] · 8月27日 15:33

**「改了什么」** 相比上一版，真正新增的能力是 Bedrock native structured outputs 支持，包括 explicit Mode.JSON\_SCHEMA 和 Mode.TOOLS\_STRICT。添加了 positive cumulative token\_budget 限制用于 structured non-streaming retries，并引入 immutable completion:usage snapshots。

**标签**: `#runtime`, `#tools`, `#eval`

---

<a id="item-harness-arch-7"></a>
### [Agent Framework Python 1.16.0 发布](https://github.com/microsoft/agent-framework/releases/tag/python-1.16.0) ⭐️ 6.5/10

Agent Framework Python 1.16.0 发布了。
agent-framework-core 增加了可配置超时和 OpenTelemetry 配置支持。
agent-framework-foundry-hosting 更新了依赖，并修复了提供程序和样本问题。

github · giles17 · 8月28日 00:52

**「改了什么」** 相比上一版，agent-framework-core 增加了可配置超时和 OpenTelemetry 配置支持。
agent-framework-foundry-hosting 更新了 Agent Server 依赖。

**标签**: `#runtime`, `#observability`, `#foundry-hosting`

---

## Agent 工程师日报

<a id="item-agent-engineer-1"></a>
### [DeepMind 世界首个双盲 AI 评估试点](https://deepmind.google/blog/piloting-the-worlds-first-double-blind-ai-evaluations/) ⭐️ 7.5/10

Google DeepMind 宣布正在试点全球首个双盲 AI 评估。这项试点直接相关于评估实践，但具体方法、时间表和结果尚未公布。

rss · Google DeepMind · 8月27日 12:59

**标签**: `#eval`, `#harness`, `#benchmarking`

---

<a id="item-agent-engineer-2"></a>
### [Claude Code Opus 5 Auto Mode 被提示注入攻击](https://simonwillison.net/2026/Aug/27/breaking-claude-code-opus-5-auto-mode/) ⭐️ 7.0/10

Johann Rehberger 发现了一种针对 Claude Code Opus 5 Auto Mode 的提示注入攻击，该攻击能以 80% 的成功率工作。通过欺骗 Claude Code 下载并解压一个恶意 zip 压缩包，然后执行导入 base64 的代码，从而绕过部分安全机制。在少数情况下，Auto Mode 甚至阻止了清理恶意进程的命令。

rss · Simon Willison · 8月27日 22:50

**「为什么重要」** 该攻击显示了 Auto Mode 在保护用户免受提示注入攻击方面的局限性，值得用户关注代理的安全配置。

**「可关注」** 可关注：运行无人值守 coding agents 时应使用容器、VM 或 OS 沙箱，并限制网络出口、监控代理且不暴露 home 目录、SSH 密钥、云凭证等敏感信息。

**标签**: `#coding-agent`, `#harness`, `#permissions`, `#eval`, `#orchestration`

---

<a id="item-agent-engineer-3"></a>
### [Gemini Omni 1.1 Flash 发布](https://deepmind.google/blog/gemini-omni-1-1-flash-lets-you-build-with-more-control/) ⭐️ 5.5/10

Google DeepMind 宣布 Gemini Omni 1.1 Flash 模型，该模型支持更多控制的构建。官方博客文章标题为《Gemini Omni 1.1 Flash lets you build with more control》。此更新可能影响 AI 开发工作流，但未提供具体性能声明或对代理 harness、eval、toolchains 或编码实践的影响细节。

rss · Google DeepMind · 8月27日 16:11

**「为什么重要」** 此官方博客发布值得今天快速查看，因为它可能在 AI 代理工程中提供控制改进，但尚未证实对具体工具链或评估的影响。

**标签**: `#coding-agent`, `#orchestration`, `#eval`, `#harness`

---

## AI 日报

<a id="item-ai-daily-1"></a>
### [ChatGPT 结合批判性思维训练：学生研究](https://openai.com/index/what-students-gain-from-chatgpt-critical-thinking-training) ⭐️ 6.5/10

OpenAI 开展了一项随机研究，涉及超过 1000 名学生。研究考察了 ChatGPT、批判性思维、原创性和学生在真实世界大学作业上的表现。研究显示，ChatGPT 结合批判性思维训练能让学生获得更好的答案和更广的思考。

rss · OpenAI Blog · 8月27日 09:00

**「可关注」** 可关注：ChatGPT 结合批判性思维训练让学生获得更好的答案和更广的思考

**标签**: `#model`, `#lab`, `#industry`, `#eval`, `#product`

---

<a id="item-ai-daily-2"></a>
### [OpenAI 巴西业务拓展](https://openai.com/index/expanding-our-presence-in-brazil) ⭐️ 5.5/10

OpenAI 宣布在巴西扩展其业务，深化与开发者的合作，助力该国 AI 采用。材料中未提供具体合作计划或时间表。

rss · OpenAI Blog · 8月27日 03:00

**「可关注」** 可关注：深化与开发者、商业和社区的合作以支持 AI 采用。

**标签**: `#OpenAI`, `#lab`, `#Brazil`, `#AI adoption`, `#expansion`

---

## AI 羊毛

<a id="item-ai-deals-1"></a>
### [免费无框架 RAG/Agent Colab 笔记](https://github.com/calmrocks/ai-engineer-notebooks) ⭐️ 6.0/10

GitHub 用户 calmrocks 公开了仓库 \`calmrocks/ai-engineer-notebooks\`，提供一组不依赖现成框架的 notebook，覆盖 RAG、agents 和 evals，可直接在 Google Colab 免费档运行。仓库公开，无需报名或兑换码，使用公开仓库即可。材料提到 Colab 免费档有每日时长限制，具体额度以 Google 当时规则为准，没有单独的领取截止时间。

rss · HN Free API / Credits · 8月27日 21:46

**「为什么重要」** 这不是限时名额，而是公开仓库，今天仍可直接打开。只要能接受 Colab 免费档的每日时长限制，仍可在不先接入一套框架的前提下跑 RAG、agent 和 eval 相关 notebook。

**「可关注」** 可关注：适合想在 Colab 免费档上自己走通 RAG、agent 和 eval、又不绑框架的人；免费档有每日时长限制，不是无限算力。

**标签**: `#free-tier`, `#colab`, `#rag`, `#agents`, `#evals`

---