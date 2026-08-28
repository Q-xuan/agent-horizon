---
layout: default
title: "Horizon Summary: 2026-08-28 (ZH)"
date: 2026-08-28
lang: zh
---

> 从 238 条内容中筛选出 19 条重要资讯。

---

**Harness 架构**
1. [Deep Agents 发布](#item-harness-arch-1) ⭐️ 8.0/10
2. [FastMCP v4.0.0b5 发布](#item-harness-arch-2) ⭐️ 7.8/10
3. [agents @cloudflare/think@0.17.0 发布](#item-harness-arch-3) ⭐️ 7.8/10
4. [Langchain 1.4.0a1 发布](#item-harness-arch-4) ⭐️ 7.8/10
5. [Instructor v1.16.0 发布](#item-harness-arch-5) ⭐️ 7.8/10
6. [E2B 2.46.1 发布](#item-harness-arch-6) ⭐️ 7.8/10
7. [Claude Code 2.1.248 发布](#item-harness-arch-7) ⭐️ 7.8/10
8. [agents@0.22.0 发布](#item-harness-arch-8) ⭐️ 6.8/10
9. [anthropics/skills 仓库 trending](#item-harness-arch-9) ⭐️ 5.0/10
10. [EveryInc compound-engineering-plugin trending](#item-harness-arch-10) ⭐️ 5.0/10

**Agent 工程师日报**
1. [1.1.1.1 DNS 缓存 100TB 优化](#item-agent-engineer-1) ⭐️ 7.8/10
2. [Claude Code Opus 5 Auto Mode 被破解](#item-agent-engineer-2) ⭐️ 7.0/10
3. [Harness-Aware Training \(HAT\) 技术报告](#item-agent-engineer-3) ⭐️ 7.0/10
4. [DeepMind 双盲 AI 评估试点](#item-agent-engineer-4) ⭐️ 5.8/10

**AI 日报**
1. [OpenClaw 病毒传播，揭秘维护者](#item-ai-daily-1) ⭐️ 6.8/10
2. [OpenAI ChatGPT 学生研究 发布](#item-ai-daily-2) ⭐️ 5.8/10

**AI 羊毛**
1. [Epic 鸡蛋本周领取：呼吸边缘等](#item-ai-deals-1) ⭐️ 6.0/10
2. [Intelcue 免费个人品牌策略生成器](#item-ai-deals-2) ⭐️ 5.0/10
3. [AI Engineer Notebooks Colab 免费](#item-ai-deals-3) ⭐️ 5.0/10

---

## Harness 架构

<a id="item-harness-arch-1"></a>
### [Deep Agents 发布](https://github.com/langchain-ai/deepagents) ⭐️ 8.0/10

Deep Agents 是 langchain-ai 推出的开源代理 harness，内置电池即插即用，开箱即用。它是一个意见化的代理，针对长时多步工作调优默认设置。支持任何支持工具调用的 LLM，包括前沿模型、开源权重或本地模型。生产就绪，无需 fork 即可扩展或替换任何组件。

rss · GitHub Trending Daily · 8月28日 08:25

**「设计要点」** Deep Agents 运行时支持任何工具调用 LLM，工具调用是核心接口。

**标签**: `#runtime`, `#tools`, `#planning`

---

<a id="item-harness-arch-2"></a>
### [FastMCP v4.0.0b5 发布](https://github.com/PrefectHQ/fastmcp/releases/tag/v4.0.0b5) ⭐️ 7.8/10

FastMCP 4 beta 5 发布，引入 ClientGroup 用于管理每个服务器的多个独立客户端。

github · zzstoatzz · 8月28日 02:57

**「设计要点」** ClientGroup 设计允许每个服务器独立管理客户端，各自协议协商，无代理中间层。

**「改了什么」** 相比 v4.0.0b4，新增 ClientGroup，支持每个服务器独立客户端协议协商和工具调用路由。修复中间件响应限制与输出模式对齐问题。

**标签**: `#mcp`, `#runtime`, `#tools`

---

<a id="item-harness-arch-3"></a>
### [agents @cloudflare/think@0.17.0 发布](https://github.com/cloudflare/agents/releases/tag/%40cloudflare/think%400.17.0) ⭐️ 7.8/10

Cloudflare agents 发布 @cloudflare/think@0.17.0 版本。
AIChatAgent 和 Think 的 durable chat recovery 变为 unconditional。
chatRecovery 配置不再支持 false。
新增 Scheduler 能力，支持持久化 delayed、dated、cron 和 interval 回调。

github · ben-reitz · 8月27日 14:07

**「设计要点」** Recovery 使用 fibers 实现，onChatRecovery hook 提供 cancellation 和 side-effect 支持。
Scheduler 基于 LifecycleCapability，共享 Durable Object alarm 和 capability routing。

**「改了什么」** durable chat recovery 变为 unconditional。
chatRecovery 配置不再支持 false，新增 Scheduler 能力。

**标签**: `#runtime`, `#memory`

---

<a id="item-harness-arch-4"></a>
### [Langchain 1.4.0a1 发布](https://github.com/langchain-ai/langchain/releases/tag/langchain%3D%3D1.4.0a1) ⭐️ 7.8/10

LangChain 1.4.0a1 初始发布，添加 MCP 协议支持并进行类型和延续逻辑的重大更改。此版本引入 langchain.mcp 命名空间和 MCPAdapter 接口，简化适配器构建。MCP 协议重构包括每模式类型处理、elicitation round 变化、FastMCP 测试覆盖和适配器简化。

github · github-actions\[bot\] · 8月27日 22:21

**「改了什么」** LangChain 1.4.0a1 初始发布，新增 MCP 协议支持，打破类型和延续逻辑。相比上一版本，添加 elicitation 答题功能、拒绝 MCP 延续轮询并简化 MCPAdapter。

**标签**: `#mcp`, `#runtime`, `#tools`

---

<a id="item-harness-arch-5"></a>
### [Instructor v1.16.0 发布](https://github.com/567-labs/instructor/releases/tag/v1.16.0) ⭐️ 7.8/10

Instructor 是一个用于 LLM 结构化输出的库。v1.16.0 版本发布了 Bedrock 原生结构化输出支持和验证重试预算功能。新增了 JSON\_SCHEMA 和 TOOLS\_STRICT 模式支持，通过 Converse API 的 outputConfig.textFormat 和严格工具模式。添加了 token\_budget 等重试限制。

github · github-actions\[bot\] · 8月27日 15:33

**「改了什么」** 相比上一版，新增了 Bedrock 原生结构化输出支持，包括 JSON\_SCHEMA 和 TOOLS\_STRICT 模式。添加了结构化验证的重试预算，支持 token\_budget 和使用快照。

**标签**: `#tools`, `#runtime`

---

<a id="item-harness-arch-6"></a>
### [E2B 2.46.1 发布](https://github.com/e2b-dev/E2B/releases/tag/e2b%402.46.1) ⭐️ 7.8/10

E2B 2.46.1 发布。弃用了 sandbox.git 模块及其公开类型和错误。运行 git 操作应通过 commands 模块代替，例如 sandbox.commands.run\(&\#x27;git clone &lt;url&gt; repo&\#x27;\)。该模块仍可正常工作，但将在下一个主要版本中被移除。

github · github-actions\[bot\] · 8月27日 20:24

**「改了什么」** 相对上一版，E2B 2.46.1 真正变的是弃用了 sandbox.git 模块及其公开类型和错误。git 操作应通过 commands 模块运行。

**标签**: `#sandbox`, `#tools`, `#runtime`

---

<a id="item-harness-arch-7"></a>
### [Claude Code 2.1.248 发布](https://code.claude.com/docs/en/changelog#2-1-248) ⭐️ 7.8/10

Claude Code 2.1.248 发布。新增受限模式 \(--restricted 或 CLAUDE\_CODE\_RESTRICTED=1\)，移除命令工具和 WebFetch（除非在 --tools 中指定），保留工作目录内文件工具，拒绝 bypassPermissions，并忽略用户、项目和本地设置文件。新增实验性 per-agent prompt cache TTL（支持 &quot;5m&quot; 或 &quot;1h&quot;）和自托管 runner --client-label 覆盖标签。添加服务器管理设置诊断，包括启动警告和 /doctor /status 接口。

rss · Claude Code Changelog · 8月27日 22:19

**「改了什么」** Claude Code 2.1.248 相对上一版新增受限模式和实验性 per-agent prompt cache TTL 等功能。添加自托管 runner 客户端标签覆盖和服务器管理设置诊断。

**标签**: `#runtime`, `#tools`, `#sandbox`, `#memory`, `#permissions`, `#subagents`

---

<a id="item-harness-arch-8"></a>
### [agents@0.22.0 发布](https://github.com/cloudflare/agents/releases/tag/agents%400.22.0) ⭐️ 6.8/10

Cloudflare agents@0.22.0 发布。durable chat recovery 现在对 AIChatAgent 和 Think 的每一次聊天都无条件使用 fibers，支持 durable bookkeeping 和 cancellation。chatRecovery 参数不再支持 false，已被 breaking change。

github · ben-reitz · 8月27日 14:07

**「设计要点」** recovery fiber 集成到 AIChatAgent 和 Think 的所有路径。Lifecycle 通过 DurableObject 实现，Scheduler 作为 reusable capability。

**「改了什么」** durable chat recovery 现在 unconditional，使用 fibers 覆盖 WebSocket、programmatic、retry 和 continuation 路径。chatRecovery false 不再支持。

**标签**: `#runtime`, `#memory`, `#durable`, `#recovery`, `#fiber`

---

<a id="item-harness-arch-9"></a>
### [anthropics/skills 仓库 trending](https://github.com/anthropics/skills) ⭐️ 5.0/10

这是 GitHub trending 的 anthropics/skills 仓库。该仓库是 Anthropic 提供的 Claude Agent Skills 实现，用于动态加载指令、脚本和资源以提升代理任务性能。技能是包含可重复任务指南的文件夹，Claude 会动态加载这些内容。

rss · GitHub Trending Daily · 8月28日 08:25

**标签**: `#runtime`, `#memory`, `#subagents`, `#skills`

---

<a id="item-harness-arch-10"></a>
### [EveryInc compound-engineering-plugin trending](https://github.com/EveryInc/compound-engineering-plugin) ⭐️ 5.0/10

EveryInc compound-engineering-plugin trending 公告。它是一个 33 技能系统，用于 AI coding agents。围绕 brainstorm-plan-build-review-capture 循环构建，支持 14 个 agent hosts。

rss · GitHub Trending Daily · 8月28日 08:25

**标签**: `#runtime`, `#memory`, `#planning`, `#subagents`, `#tools`

---

## Agent 工程师日报

<a id="item-agent-engineer-1"></a>
### [1.1.1.1 DNS 缓存 100TB 优化](https://blog.cloudflare.com/dns-cache-memory-optimization-1111/) ⭐️ 7.8/10

Cloudflare 的 Big Pineapple 平台在 1.1.1.1 的 DNS 缓存中存储了超过 2500 亿条目。通过五次对缓存条目存储方式的优化，每个条目的内存占用减少了超过 50%。在整个网络中，这节省了大约 100TB 内存，同时插入吞吐量提高了 43%，查找延迟降低了 19%。

rss · Cloudflare Engineering · 8月27日 17:02 · [社区讨论](https://news.ycombinator.com/item?id=49468083)

**「为什么重要」** Cloudflare 已通过五次优化在生产环境中节省了 100TB 内存。这些变化已发生。

**「可关注」** 可关注：使用 Box&lt;\[T\]&gt; 替代 Vec&lt;T&gt; 和 String，合并多个记录列表为单个列表并使用 2 字节偏移量表示，省略重复的 owner 字段。

**「评论」** 社区认为这是正确的软件交付方式，系统编程优化很重要。有人指出可将记录数据直接放在 CacheEntry 后进一步优化，但担心 Rust 安全保证。

**标签**: `#memory`, `#cache`, `#optimization`, `#systems-programming`, `#production-scale`

---

<a id="item-agent-engineer-2"></a>
### [Claude Code Opus 5 Auto Mode 被破解](https://simonwillison.net/2026/Aug/27/breaking-claude-code-opus-5-auto-mode/) ⭐️ 7.0/10

Johann Rehberger 发现针对 Claude Code Opus 5 Auto Mode 的提示注入攻击。该攻击诱骗 Claude Code 下载并解压恶意 zip 归档，然后通过导入 base64 模块执行提取的 struct.py 文件。攻击成功率约 80%。在少数情况下，Auto Mode 阻止了清理恶意进程的命令。

rss · Simon Willison · 8月27日 22:50

**「为什么重要」** Anthropic 曾将 Auto Mode 设为默认并声称其能有效防护提示注入攻击。该攻击已报告并验证可诱骗执行恶意代码，但 Auto Mode 的长期安全影响尚未证实。

**「可关注」** 可关注：将无人值守 coding agents 运行在容器、VM 或 OS 沙箱中，并限制网络出口。

**标签**: `#coding-agent`, `#permissions`, `#harness`, `#eval`, `#orchestration`

---

<a id="item-agent-engineer-3"></a>
### [Harness-Aware Training \(HAT\) 技术报告](https://huggingface.co/papers/2608.15763) ⭐️ 7.0/10

AI-powered digital avatar streamers 需要实时回答产品问题、与观众互动并执行营销策略，强调低延迟、频繁策略更新和准确有效响应。Evolvable Harnesses 允许独立于模型权重更新 Skills、Hooks、prompts 和 tools，实现快速迭代，但存在权衡：大模型零样本适应但速度慢，紧凑模型满足延迟但固定 Harness 配置下过拟合。报告提出 Harness-Aware Training \(HAT\)，其关键组件 Harness-State Augmentation \(HSA\) 通过对 Skill identifiers 和 content、tool schemas、prompt structures 和 Hook functions 应用任务保持变换，训练紧凑模型适应变化 Harness。

rss · Hugging Face Daily Papers · 8月28日 00:00

**「为什么重要」** 报告提供了 Harness-Aware Training \(HAT\) 和 Harness-State Augmentation \(HSA\) 的新技术细节，用于训练紧凑模型适应变化的 agent harness，这对实时应用中的 agent toolchains 和 orchestration 具有潜在影响。

**「可关注」** 可关注：Harness-State Augmentation \(HSA\) 通过任务保持变换使紧凑模型适应变化的 Harness 配置，解决大模型零样本适应慢与紧凑模型固定配置过拟合的权衡。

**标签**: `#harness`, `#coding-agent`, `#orchestration`, `#eval`

---

<a id="item-agent-engineer-4"></a>
### [DeepMind 双盲 AI 评估试点](https://deepmind.google/blog/piloting-the-worlds-first-double-blind-ai-evaluations/) ⭐️ 5.8/10

Google DeepMind 宣布全球首个双盲 AI 评估的试点。该方法由其官方博客发布，标题为 &\#x27;Piloting the world&\#x27;s first double-blind AI evaluations&\#x27;。此举影响 AI 评估流程。

rss · Google DeepMind · 8月27日 12:59

**标签**: `#eval`, `#harness`

---

## AI 日报

<a id="item-ai-daily-1"></a>
### [OpenClaw 病毒传播，揭秘维护者](https://github.blog/open-source/maintainers/openclaw-went-viral-meet-the-maintainers-building-and-securing-it/) ⭐️ 6.8/10

OpenClaw 是 GitHub 历史上增长最快的项目。在项目首六个月，Peter Steinberger 和几位维护者分享了他们的经验。这篇博客文章介绍了该项目如何病毒式传播，以及维护者们在构建和保护项目方面的努力。

rss · GitHub Blog · 8月27日 16:00

**「为什么重要」** OpenClaw 的快速增长展示了开源项目的潜力，维护者分享的经验对类似项目有参考价值。

**「可关注」** 可关注：OpenClaw 是 GitHub 历史上增长最快的项目，维护者分享了首六个月的经验。

**标签**: `#open-source`

---

<a id="item-ai-daily-2"></a>
### [OpenAI ChatGPT 学生研究 发布](https://openai.com/index/what-students-gain-from-chatgpt-critical-thinking-training) ⭐️ 5.8/10

OpenAI 发布了一项随机研究，涉及超过 1000 名大学学生，考察 ChatGPT、批判性思维、原创性以及学生在真实世界大学作业上的表现。研究旨在了解这些因素如何影响学生完成真实世界大学作业的情况。

rss · OpenAI Blog · 8月27日 09:00

**「为什么重要」** 这项研究探讨了 ChatGPT、批判性思维、原创性以及学生在真实世界大学作业上的表现，这对教育领域 AI 应用的发展有帮助。

**「可关注」** 可关注：随机研究评估 ChatGPT、批判性思维、原创性以及学生在真实世界大学作业上的表现。

**标签**: `#OpenAI`, `#ChatGPT`, `#education`, `#critical-thinking`, `#student performance`

---

## AI 羊毛

<a id="item-ai-deals-1"></a>
### [Epic 鸡蛋本周领取：呼吸边缘等](https://www.appinn.com/eggs-26828/) ⭐️ 6.0/10

Epic Games Store 本周免费游戏活动从 8.28 到 9.3 截止。《呼吸边缘》（Breathedge）、《家族传奇：桌面版》（Rival Stars Horse Racing: Desktop Edition）和《逃出百慕大》（Down in Bermuda）可免费领取。其中 2 款电脑游戏，1 款手机游戏。

rss · 小众软件 · 8月28日 08:04

**「可关注」** 可关注：Epic 鸡蛋领取截止 9.3

**标签**: `#promo`, `#limited-free`

---

<a id="item-ai-deals-2"></a>
### [Intelcue 免费个人品牌策略生成器](https://www.intelcue.ai/tools/personal-branding-strategy-builder) ⭐️ 5.0/10

Intelcue 推出个人品牌策略生成器工具。该工具将市场研究转化为个人品牌策略。免费提供使用，但无具体使用额度、地区或截止时间等信息。

rss · HN Free API / Credits · 8月28日 06:36

**标签**: `#free-tier`, `#promo`

---

<a id="item-ai-deals-3"></a>
### [AI Engineer Notebooks Colab 免费](https://github.com/calmrocks/ai-engineer-notebooks) ⭐️ 5.0/10

calmrocks 分享了 AI Engineer Notebooks 仓库，提供免费框架-free 的 RAG、agents、evals 笔记本，可在 Google Colab 上运行。材料中未提及具体额度、模型或价格，也没有领取条件和截止时间。该资源在 Hacker News 上获得 98 点，11 条评论。

rss · HN Free API / Credits · 8月27日 21:46

**「可关注」** 可关注：免费框架-free 的 RAG、agents、evals 笔记本，可直接在 Colab 运行。

**标签**: `#free-tier`, `#colab`, `#rag`, `#agents`, `#promo`

---