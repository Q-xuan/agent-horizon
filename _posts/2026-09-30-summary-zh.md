---
layout: default
title: "Horizon Summary: 2026-09-30 (ZH)"
date: 2026-09-30
lang: zh
---

> 从 190 条内容中筛选出 16 条重要资讯。

---

**Harness 架构**
1. [Claude Code v2.1.285 发布](#item-harness-arch-1) ⭐️ 8.3/10
2. [pydantic/pydantic-ai released v2.52.0](#item-harness-arch-2) ⭐️ 8.3/10
3. [Claude Code 2.1.285 发布](#item-harness-arch-3) ⭐️ 8.3/10
4. [openai/codex released rust-v0.159.0](#item-harness-arch-4) ⭐️ 7.3/10
5. [Gemini CLI nightly 发布](#item-harness-arch-5) ⭐️ 6.3/10
6. [google-gemini/gemini-cli released v0.63.0-preview.0](#item-harness-arch-6) ⭐️ 6.3/10
7. [Pydantic-AI v1.107.7 发布](#item-harness-arch-7) ⭐️ 5.8/10
8. [SkillOpt：文本空间训练技能](#item-harness-arch-8) ⭐️ 5.0/10

**Agent 工程师日报**
1. [HF daily paper: TraceDance: An Automated System for Building Agent Behavior Benchmarks from Real-World Agent Deployment Traces](#item-agent-engineer-1) ⭐️ 8.0/10
2. [Getting the Source Right, Not Just the Fact: Source-Aware Verification for MCP Agents](#item-agent-engineer-2) ⭐️ 7.8/10
3. [小推理模型思考瓶颈与 FlyBy 框架](#item-agent-engineer-3) ⭐️ 7.5/10
4. [HF daily paper: CompoWorld: Compositional Environment Scaling for General Agents](#item-agent-engineer-4) ⭐️ 7.5/10
5. [HF daily paper: Groupwise Agentic Grading and Advantage Redistribution for Code Agent RL](#item-agent-engineer-5) ⭐️ 7.0/10

**AI 日报**
1. [OpenAI 发布 GPT-6.1 Sol](#item-ai-daily-1) ⭐️ 9.8/10
2. [OpenAI DevDay 2026 回顾](#item-ai-daily-2) ⭐️ 9.8/10
3. [GitHub 更新开发者政策与透明度数据](#item-ai-daily-3) ⭐️ 7.8/10

---

## Harness 架构

<a id="item-harness-arch-1"></a>
### [Claude Code v2.1.285 发布](https://github.com/anthropics/claude-code/releases/tag/v2.1.285) ⭐️ 8.3/10

Claude Code v2.1.285 引入环境级工具与权限控制、安装期 MCP 服务器配置、API provider 限制及运行时超时重试设置。新增 \`CLAUDE\_CODE\_DISABLE\_WEB\_FETCH\` 关闭 WebFetch，\`allowedProviders\` 托管设置限定可用 API provider，\`claude plugin install --config\` 支持在安装 \`.mcpb\` 服务器时直接写入 \`&lt;server&gt;.&lt;key&gt;=&lt;value&gt;\`。\`CLAUDE\_CODE\_NONSTREAMING\_TIMEOUT\_RETRIES\` 限制非流式回退请求超时后的重发次数。版本同时修复 subagent 前台执行、fork 权限模式继承、SSH 安装忽略 \`GIT\_SSH\`、托管设置读取失败拒绝启动等大量运行问题。

github · ashwin-ant · 9月29日 19:27

**「设计要点」** 工具层通过环境变量和托管设置实现细粒度开关，MCP 服务器配置前移到安装阶段。权限模型上，fork subagent 继承父会话的 permission mode 且不能退出 plan mode，后台 subagent 的权限请求路由到 prompt tool。

**「改了什么」** 新增 provider 限定、安装期 MCP 配置、WebFetch 环境开关及非流式超时重试上限。修复覆盖 subagent 前台化、fork 权限继承、SSH 安装、托管设置容错、Remote Control 消息状态、Artifact 发布冲突与 \`/ultrareview\` 上传等运行时行为。

**标签**: `#tools`, `#mcp`, `#permissions`, `#runtime`, `#subagents`

---

<a id="item-harness-arch-2"></a>
### [pydantic/pydantic-ai released v2.52.0](https://github.com/pydantic/pydantic-ai/releases/tag/v2.52.0) ⭐️ 8.3/10

Pydantic AI v2.52.0 integrates the harness into the main repository, introduces a workspace abstraction for sandboxed/local tool execution, and fixes a moderate web\_fetch security issue.

github · dsfaccini · 9月30日 00:54

**标签**: `#runtime`, `#sandbox`, `#tools`

---

<a id="item-harness-arch-3"></a>
### [Claude Code 2.1.285 发布](https://code.claude.com/docs/en/changelog#2-1-285) ⭐️ 8.3/10

Claude Code 2.1.285 发布。新增 \`CLAUDE\_CODE\_DISABLE\_WEB\_FETCH\` 环境变量关闭 WebFetch 工具，\`claude --desktop\` 可在当前目录或指定会话打开桌面端。插件体系加入 \`claude plugin configure\` 命令，并支持在 \`claude plugin install --config\` 时用 \`&lt;server&gt;.&lt;key&gt;=&lt;value&gt;\` 直接写入 \`.mcpb\` 服务器配置。托管设置新增 \`allowedProviders\`，限制机器可用的 API 提供商。

rss · Claude Code Changelog · 9月29日 19:37

**「设计要点」** 工具层与权限面收紧：环境变量和托管设置分别控制 WebFetch 出口与 API 提供商白名单。插件配置命令把 MCP 服务器设置从 \`/plugin\` 界面前移到安装期，减少交互步骤。fork subagent 改为继承父级权限模式，且不能自行退出 plan mode。

**「改了什么」** 新增 WebFetch 禁用开关、桌面端目录/会话联动、插件配置查询与安装期 MCP 注入、API 提供商托管白名单、非流式超时重试上限。修复覆盖 subagent 前台执行、SSH 安装忽略 \`GIT\_SSH\`、MCP 服务器关闭后工具残留、Artifact 发布覆盖、Remote Control 消息已读状态等 harness 缺陷。

**标签**: `#runtime`, `#tools`, `#mcp`, `#permissions`

---

<a id="item-harness-arch-4"></a>
### [openai/codex released rust-v0.159.0](https://github.com/openai/codex/releases/tag/rust-v0.159.0) ⭐️ 7.3/10

Codex Rust v0.159.0 adds opt-in instant-interrupt steering, app-server history pagination, and Windows launcher fixes for MCP/code-mode hosts.

github · github-actions\[bot\] · 9月29日 08:05

**标签**: `#runtime`, `#tools`, `#sandbox`, `#mcp`

---

<a id="item-harness-arch-5"></a>
### [Gemini CLI nightly 发布](https://github.com/google-gemini/gemini-cli/releases/tag/v0.64.0-nightly.20260930.g38700b4b3) ⭐️ 6.3/10

Gemini CLI 发布 v0.64.0-nightly.20260930.g38700b4b3。本次 nightly 集中在非交互模式自主计划执行、A2A 服务器 V1 到 V2 设置迁移、ACP 使用量通知桥接，以及 headless 模式下的文件夹信任状态传播。改动横跨 runtime、planning、permissions 与 protocol 层，均为增量修复与重构，无破坏性变更。

github · gemini-cli-robot · 9月30日 01:33

**「设计要点」** 非交互模式启用自主计划执行，影响 runtime 的规划回路。A2A 服务器引入 V1 到 V2 设置迁移逻辑，调整协议层配置兼容。ACP 桥接 PromptResponse.usage 并发出 usage\_update 通知，补齐使用量回传路径。Headless 模式传播解析后的文件夹信任状态，修正权限判定链路。

**「改了什么」** 相对 v0.63.0-nightly，新增非交互模式下的自主计划执行能力。formatTruncatedToolOutput 在 maxChars &lt;= 0 时禁用截断。A2A 服务器完成 V1 到 V2 设置迁移重构。ACP 支持 PromptResponse.usage 桥接与 usage\_update 通知。Headless 模式修复文件夹信任状态传播。

**标签**: `#runtime`, `#planning`, `#permissions`, `#tools`

---

<a id="item-harness-arch-6"></a>
### [google-gemini/gemini-cli released v0.63.0-preview.0](https://github.com/google-gemini/gemini-cli/releases/tag/v0.63.0-preview.0) ⭐️ 6.3/10

Gemini CLI v0.63.0-preview.0 is a bug-fix release with minor improvements to connection recovery, MCP config handling, and memory lifecycle in long-running agent loops.

github · gemini-cli-robot · 9月29日 20:58

**标签**: `#runtime`, `#memory`, `#mcp`, `#tools`

---

<a id="item-harness-arch-7"></a>
### [Pydantic-AI v1.107.7 发布](https://github.com/pydantic/pydantic-ai/releases/tag/v1.107.7) ⭐️ 5.8/10

Pydantic-AI v1.107.7 是 v1 线的维护版本，回移了 2.52.0 的安全修复，并限制了 genai-prices 依赖。本地 web\_fetch 工具解析攻击者控制的深度嵌套 HTML 时可能过度消耗 CPU 和内存，provider-native 网页抓取不受影响。同时将 genai-prices 锁定在 0.1 以下，保证 token 用量提取与限额功能正常。

github · dsfaccini · 9月30日 00:54

**「设计要点」** 本地 web\_fetch 工具与 provider-native 抓取在实现上分离，安全修复仅影响前者；依赖上限用于稳定 token 计量链路。

**「改了什么」** 相对 v1.107.6，本次回移了 web\_fetch 的 HTML 解析 DoS 修复，并将 genai-prices 依赖限制在 0.1 以下。

**标签**: `#tools`, `#runtime`, `#security`

---

<a id="item-harness-arch-8"></a>
### [SkillOpt：文本空间训练技能](https://github.com/microsoft/SkillOpt) ⭐️ 5.0/10

microsoft/SkillOpt 是一个文本空间优化器，为冻结的 LLM agent 训练可复用的自然语言技能。它通过轨迹驱动编辑和验证门控更新迭代技能，最终产出可部署的 best\_skill.md 工件。项目把技能训练类比为神经网络训练，引入 epochs、mini-batchsize、learning rates 和 validation gates，但不触碰模型权重。当前信息来自 GitHub trending 聚合，缺少官方发布说明、代码路径与架构细节。

rss · GitHub Trending Daily · 9月30日 01:47

**「设计要点」** SkillOpt 在冻结模型之上运行，把技能表示为自然语言文本，通过轨迹数据驱动编辑并用验证门筛选更新，最终以 best\_skill.md 形式部署。训练循环借鉴神经网络范式，但优化对象是文本技能而非模型权重。

**标签**: `#memory`, `#planning`, `#eval`

---

## Agent 工程师日报

<a id="item-agent-engineer-1"></a>
### [HF daily paper: TraceDance: An Automated System for Building Agent Behavior Benchmarks from Real-World Agent Deployment Traces](https://huggingface.co/papers/2609.33295) ⭐️ 8.0/10

TraceDance 是一个从真实 agent 部署 trace 中自动构建针对性行为基准的评测系统，通过可编程检索与候选确认生成测试，并在决策点用 rubric 评估 LLM 下一步行为。

rss · Hugging Face Daily Papers · 9月30日 01:47

**标签**: `#eval`, `#observability`, `#coding-agent`, `#harness`

---

<a id="item-agent-engineer-2"></a>
### [Getting the Source Right, Not Just the Fact: Source-Aware Verification for MCP Agents](https://huggingface.co/blog/MultiverseComputingCAI/getting-the-source-right-not-just-the-fact-source) ⭐️ 7.8/10

Hugging Face 博客发布 ProvenanceGuard 论文介绍，提出通过源感知验证解决 MCP Agent 的跨源事实混淆问题。

rss · Hugging Face Blog · 9月29日 13:07

**标签**: `#mcp`, `#eval`, `#harness`

---

<a id="item-agent-engineer-3"></a>
### [小推理模型思考瓶颈与 FlyBy 框架](https://huggingface.co/papers/2609.34327) ⭐️ 7.5/10

2026 年 9 月 30 日，Hugging Face Daily Papers 收录研究，发现小推理模型（sRMs）的自我修正主要把概率质量巩固到已可达的解，而非让新解变得可达。研究者在两个模型家族、多个规模上干预中间推理状态，区分出执行瓶颈与知识瓶颈：前者正确路径本就可达，反思可恢复；后者需外部信息介入。作者据此提出 FlyBy 选择性查询框架。该论文目前获 32 次点赞。

rss · Hugging Face Daily Papers · 9月30日 01:47

**「为什么重要」** 这项工作用干预实验拆穿了「思考越多越好」的直觉，为 agent 编排中何时继续反思、何时调用外部工具提供了判别依据。已确认的是自我修正的机理局限，尚未确认的是 FlyBy 在真实生产链路中的增益幅度。

**「可关注」** 可关注：构建小推理模型 harness 时，先诊断失败属于执行瓶颈还是知识瓶颈，再决定加深反思或触发外部查询，避免盲目堆叠测试时算力。

**标签**: `#eval`, `#orchestration`, `#harness`

---

<a id="item-agent-engineer-4"></a>
### [HF daily paper: CompoWorld: Compositional Environment Scaling for General Agents](https://huggingface.co/papers/2609.33665) ⭐️ 7.5/10

CompoWorld 论文提出通过组合可复用服务与依赖图来自动生成并验证跨服务任务环境，为通用智能体训练提供可扩展的交互数据来源。

rss · Hugging Face Daily Papers · 9月30日 01:47

**标签**: `#eval`, `#orchestration`, `#coding-agent`, `#harness`

---

<a id="item-agent-engineer-5"></a>
### [HF daily paper: Groupwise Agentic Grading and Advantage Redistribution for Code Agent RL](https://huggingface.co/papers/2609.32577) ⭐️ 7.0/10

A new paper proposes GAGAR, an agentic grading framework that redistributes advantages in GRPO for code agent RL to favor higher-quality, targeted implementations.

rss · Hugging Face Daily Papers · 9月30日 01:47

**标签**: `#coding-agent`, `#eval`, `#rl`

---

## AI 日报

<a id="item-ai-daily-1"></a>
### [OpenAI 发布 GPT-6.1 Sol](https://openai.com/index/introducing-gpt-6-1-sol) ⭐️ 9.8/10

OpenAI 发布 GPT-6.1 Sol，官方定位为面向编程、计算机操作和专业工作的模型，并称其具备接近 Astra 的智能水平。该模型的 API 输入与输出 token 价格均为 Astra 标准价格的五分之一。目前官方仅给出定位与定价，未披露基准测试、上下文长度或架构细节。

rss · OpenAI Blog · 9月29日 10:00

**「为什么重要」** 官方将编程与计算机操作列为核心场景，并给出明确的价格锚点，为 agent 相关成本评估提供直接参照。

**「可关注」** 可关注：GPT-6.1 Sol 的 API 输入与输出 token 价格均为 Astra 标准价格的五分之一，官方定位覆盖编程与计算机操作。

**标签**: `#model`, `#lab`, `#product`, `#industry`

---

<a id="item-ai-daily-2"></a>
### [OpenAI DevDay 2026 回顾](https://openai.com/index/devday-2026-recap) ⭐️ 9.8/10

OpenAI 官方博客发布 DevDay 2026 回顾，汇总超过 20 项公告，涉及 GPT-6 Astra、ChatGPT、Codex、API、安全及开发者工具。官方未在摘要中给出具体性能指标或发布时间表。目前仅见官方通稿，缺乏第三方验证。

rss · OpenAI Blog · 9月29日 10:00

**「可关注」** 可关注：DevDay 2026 公布超过 20 项更新，其中 Codex 与 API 部分值得后续跟进官方细节。

**标签**: `#model`, `#lab`, `#product`, `#industry`

---

<a id="item-ai-daily-3"></a>
### [GitHub 更新开发者政策与透明度数据](https://github.blog/news-insights/policy-news-and-insights/developer-policy-update-transparency-state-policy-and-whats-ahead/) ⭐️ 7.8/10

GitHub 发布开发者政策更新，涵盖透明度数据与州政策变化，影响开发者及开源项目。官方博客称将公布最新透明度数据，但现有摘录未提供具体条款、数字或生效时间。政策变化对开发者的实际影响尚不明确。

rss · GitHub Blog · 9月29日 15:00

**「为什么重要」** 此次更新涉及开发者与开源项目，但现有摘录未披露具体政策条款与数据细节。

**「可关注」** 可关注：GitHub 后续披露的透明度数据与州政策具体内容，当前信息不足以评估影响。

**标签**: `#policy`, `#industry`, `#open-source`

---