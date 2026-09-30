---
layout: default
title: "Horizon Summary: 2026-09-30 (EN)"
date: 2026-09-30
lang: en
---

> From 190 items, 16 important content pieces were selected

---

**Agent Harness Architecture**
1. [Claude Code v2.1.285 发布](#item-harness-arch-1) ⭐️ 8.3/10
2. [pydantic/pydantic-ai released v2.52.0](#item-harness-arch-2) ⭐️ 8.3/10
3. [Claude Code 2.1.285 发布](#item-harness-arch-3) ⭐️ 8.3/10
4. [openai/codex released rust-v0.159.0](#item-harness-arch-4) ⭐️ 7.3/10
5. [Gemini CLI v0.64.0-nightly.20260930 Released](#item-harness-arch-5) ⭐️ 6.3/10
6. [google-gemini/gemini-cli released v0.63.0-preview.0](#item-harness-arch-6) ⭐️ 6.3/10
7. [Pydantic-AI v1.107.7 Patches web\_fetch DoS](#item-harness-arch-7) ⭐️ 5.8/10
8. [microsoft/SkillOpt Optimizes Agent Skills in Text Space](#item-harness-arch-8) ⭐️ 5.0/10

**AI Agent Engineer**
1. [HF daily paper: TraceDance: An Automated System for Building Agent Behavior Benchmarks from Real-World Agent Deployment Traces](#item-agent-engineer-1) ⭐️ 8.0/10
2. [Getting the Source Right, Not Just the Fact: Source-Aware Verification for MCP Agents](#item-agent-engineer-2) ⭐️ 7.8/10
3. [FlyBy: Selective Querying for Small Reasoning Models](#item-agent-engineer-3) ⭐️ 7.5/10
4. [HF daily paper: CompoWorld: Compositional Environment Scaling for General Agents](#item-agent-engineer-4) ⭐️ 7.5/10
5. [HF daily paper: Groupwise Agentic Grading and Advantage Redistribution for Code Agent RL](#item-agent-engineer-5) ⭐️ 7.0/10

**AI Daily**
1. [OpenAI 发布 GPT-6.1 Sol](#item-ai-daily-1) ⭐️ 9.8/10
2. [OpenAI DevDay 2026 回顾](#item-ai-daily-2) ⭐️ 9.8/10
3. [GitHub 发布开发者政策更新](#item-ai-daily-3) ⭐️ 7.8/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [Claude Code v2.1.285 发布](https://github.com/anthropics/claude-code/releases/tag/v2.1.285) ⭐️ 8.3/10

Claude Code v2.1.285 发布，新增环境级工具与权限控制、安装期 MCP 配置、Provider 限制和运行时超时重试设置。\`CLAUDE\_CODE\_DISABLE\_WEB\_FETCH\` 可关闭 WebFetch；\`allowedProviders\` 托管设置限定机器可用的 API Provider；\`claude plugin install --config\` 支持在安装时为 \`.mcpb\` 服务器写入 \`&lt;server&gt;.&lt;key&gt;=&lt;value&gt;\`。版本还修复了 fork subagent 权限模式继承、托管设置读取失败启动拒绝、Remote Control 消息已读状态等大量问题。

github · ashwin-ant · Sep 29, 19:27

**「设计要点」** 权限与工具控制下沉到环境变量和托管设置：\`allowedProviders\` 在机器级限制 Provider，\`CLAUDE\_CODE\_DISABLE\_WEB\_FETCH\` 直接关停工具；MCP 服务器配置前移到安装阶段，减少运行时手动配置。fork subagent 现在继承父会话的权限模式且不能退出 plan mode，托管设置文件读取失败时降级为警告启动而非整体拒绝。

**「改了什么」** 相对旧版，新增 \`claude --desktop\`、\`claude plugin configure\` 与 \`--values-stdin\`、\`CLAUDE\_CODE\_NONSTREAMING\_TIMEOUT\_RETRIES\`；修复 SSH 安装忽略 \`GIT\_SSH\`/\`core.sshCommand\`、mid-session 关停 MCP 后工具仍可用、Bedrock 流式错误显示原始 JSON、Artifact 发布覆盖未重读文件等数十项缺陷。

**Tags**: `#tools`, `#mcp`, `#permissions`, `#runtime`, `#subagents`

---

<a id="item-harness-arch-2"></a>
### [pydantic/pydantic-ai released v2.52.0](https://github.com/pydantic/pydantic-ai/releases/tag/v2.52.0) ⭐️ 8.3/10

Pydantic AI v2.52.0 integrates the harness into the main repository, introduces a workspace abstraction for sandboxed/local tool execution, and fixes a moderate web\_fetch security issue.

github · dsfaccini · Sep 30, 00:54

**Tags**: `#runtime`, `#sandbox`, `#tools`

---

<a id="item-harness-arch-3"></a>
### [Claude Code 2.1.285 发布](https://code.claude.com/docs/en/changelog#2-1-285) ⭐️ 8.3/10

Claude Code 2.1.285 发布，新增 WebFetch 禁用开关、桌面端目录/会话集成、插件选项查看与 stdin 配置命令。\`claude plugin install --config\` 支持 \`&lt;server&gt;.&lt;key&gt;=&lt;value&gt;\`，在安装 \`.mcpb\` 时直接写入 MCP 服务器配置。新增 \`allowedProviders\` 托管设置限定 API 提供商，新增 \`CLAUDE\_CODE\_NONSTREAMING\_TIMEOUT\_RETRIES\` 控制非流式回退重试上限。修复 fork 子代理前台执行、托管设置读取失败启动、SSH 插件安装忽略 git 配置、会话中切换模型后输出上限不重置等问题。

rss · Claude Code Changelog · Sep 29, 19:37

**「设计要点」** 工具层通过 \`CLAUDE\_CODE\_DISABLE\_WEB\_FETCH\` 直接关闭 WebFetch；\`claude plugin install --config\` 在安装期写入 \`.mcpb\` MCP 配置，免去 \`/plugin\` → Configure。权限层新增 \`allowedProviders\` 限定 Anthropic API、Bedrock、Vertex AI 等提供商；fork 子代理继承父级权限模式且不能退出 plan mode。状态层修复 cloud session 压缩重启后拒绝更新已读 artifact、Remote Control 消息在 Claude 开始处理时才标记已读且退出后队列消息下次 resume 到达。

**「改了什么」** 新增 \`CLAUDE\_CODE\_DISABLE\_WEB\_FETCH\`、\`CLAUDE\_CODE\_NONSTREAMING\_TIMEOUT\_RETRIES\` 环境变量与 \`allowedProviders\` 托管设置；新增 \`claude --desktop\`、\`claude plugin configure\` 及 \`claude plugin install --config\` 的 MCP 安装期配置。修复 fork 子代理前台执行与权限模式继承、托管设置读取失败启动、SSH 插件安装忽略 \`GIT\_SSH\`/\`core.sshCommand\`、会话中 \`set\_model\` 后输出上限不重置、MCP 中途关闭后工具残留、沙箱内联脚本重复审批、Remote Control 消息已读与队列、artifact 重写越权等关键 harness 问题。

**Tags**: `#runtime`, `#tools`, `#mcp`, `#permissions`

---

<a id="item-harness-arch-4"></a>
### [openai/codex released rust-v0.159.0](https://github.com/openai/codex/releases/tag/rust-v0.159.0) ⭐️ 7.3/10

Codex Rust v0.159.0 adds opt-in instant-interrupt steering, app-server history pagination, and Windows launcher fixes for MCP/code-mode hosts.

github · github-actions\[bot\] · Sep 29, 08:05

**Tags**: `#runtime`, `#tools`, `#sandbox`, `#mcp`

---

<a id="item-harness-arch-5"></a>
### [Gemini CLI v0.64.0-nightly.20260930 Released](https://github.com/google-gemini/gemini-cli/releases/tag/v0.64.0-nightly.20260930.g38700b4b3) ⭐️ 6.3/10

Gemini CLI shipped nightly build v0.64.0-nightly.20260930.g38700b4b3 with targeted fixes across planning, protocol, and permissions layers. The release enables autonomous plan execution in non-interactive mode, migrates A2A server settings from V1 to V2, bridges ACP usage notifications, and propagates resolved folder trust state in headless mode. It also disables output truncation when maxChars is zero or negative. These are incremental fixes in a nightly channel, not a breaking major release.

github · gemini-cli-robot · Sep 30, 01:33

**「Design Points」** Non-interactive mode now executes autonomous plans without an interactive session. Headless runs propagate the resolved folder trust state so permission checks remain consistent outside the TUI. The A2A server implements V1-to-V2 settings migration to keep agent-to-agent configuration compatible.

**「What Changed」** Autonomous plan execution is enabled in non-interactive mode. Tool output truncation is disabled when maxChars &lt;= 0. A2A server adds V1 to V2 settings migration logic. ACP bridges PromptResponse.usage and emits usage\_update notifications. Headless mode propagates resolved folder trust state.

**Tags**: `#runtime`, `#planning`, `#permissions`, `#tools`

---

<a id="item-harness-arch-6"></a>
### [google-gemini/gemini-cli released v0.63.0-preview.0](https://github.com/google-gemini/gemini-cli/releases/tag/v0.63.0-preview.0) ⭐️ 6.3/10

Gemini CLI v0.63.0-preview.0 is a bug-fix release with minor improvements to connection recovery, MCP config handling, and memory lifecycle in long-running agent loops.

github · gemini-cli-robot · Sep 29, 20:58

**Tags**: `#runtime`, `#memory`, `#mcp`, `#tools`

---

<a id="item-harness-arch-7"></a>
### [Pydantic-AI v1.107.7 Patches web\_fetch DoS](https://github.com/pydantic/pydantic-ai/releases/tag/v1.107.7) ⭐️ 5.8/10

Pydantic-AI v1.107.7 is a maintenance release for the v1 line, backporting a security fix from v2.52.0. It patches GHSA-v36g-jcw9-x7cw, a moderate vulnerability where deeply nested attacker-controlled HTML could cause excessive CPU and memory consumption in the local \`web\_fetch\` tool. Provider-native web fetching is not affected. The release also caps the \`genai-prices\` dependency below 0.1 to keep token usage extraction and limits working.

github · dsfaccini · Sep 30, 00:54

**「Architecture Note」** The denial-of-service vector is confined to the local \`web\_fetch\` tool&\#x27;s HTML conversion path; provider-native fetching uses a separate implementation and is unaffected.

**「What Changed」** Patches the local \`web\_fetch\` HTML parsing DoS and caps \`genai-prices\` below 0.1. No new capabilities or architectural changes.

**Tags**: `#tools`, `#runtime`, `#security`

---

<a id="item-harness-arch-8"></a>
### [microsoft/SkillOpt Optimizes Agent Skills in Text Space](https://github.com/microsoft/SkillOpt) ⭐️ 5.0/10

Microsoft&\#x27;s SkillOpt trains reusable natural-language skills for frozen LLM agents through text-space optimization. It uses trajectory-driven edits and validation-gated updates to produce deployable best\_skill.md artifacts. The approach mirrors neural network training with epochs, batch sizes, and learning rates, but modifies only the skill text, not model weights. The trending summary lacks implementation details.

rss · GitHub Trending Daily · Sep 30, 01:47

**「设计要点」** The system keeps the base LLM frozen and evolves a separate natural-language skill layer. Validation gates filter trajectory-driven text edits before they are written to the deployable artifact.

**Tags**: `#memory`, `#planning`, `#eval`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [HF daily paper: TraceDance: An Automated System for Building Agent Behavior Benchmarks from Real-World Agent Deployment Traces](https://huggingface.co/papers/2609.33295) ⭐️ 8.0/10

TraceDance 是一个从真实 agent 部署 trace 中自动构建针对性行为基准的评测系统，通过可编程检索与候选确认生成测试，并在决策点用 rubric 评估 LLM 下一步行为。

rss · Hugging Face Daily Papers · Sep 30, 01:47

**Tags**: `#eval`, `#observability`, `#coding-agent`, `#harness`

---

<a id="item-agent-engineer-2"></a>
### [Getting the Source Right, Not Just the Fact: Source-Aware Verification for MCP Agents](https://huggingface.co/blog/MultiverseComputingCAI/getting-the-source-right-not-just-the-fact-source) ⭐️ 7.8/10

Hugging Face 博客发布 ProvenanceGuard 论文介绍，提出通过源感知验证解决 MCP Agent 的跨源事实混淆问题。

rss · Hugging Face Blog · Sep 29, 13:07

**Tags**: `#mcp`, `#eval`, `#harness`

---

<a id="item-agent-engineer-3"></a>
### [FlyBy: Selective Querying for Small Reasoning Models](https://huggingface.co/papers/2609.34327) ⭐️ 7.5/10

Hugging Face Daily Papers \(published 2026-09-30, 32 upvotes\) reports that self-refinement in small reasoning models \(sRMs\) largely consolidates probability mass onto solutions already reachable from the current state, rather than making new ones reachable. By intervening at intermediate reasoning states across two model families and multiple scales, the authors distinguish execution bottlenecks—where reflection can recover a reachable correct path—from knowledge bottlenecks—where relevant external information makes it reachable. They introduce FlyBy, a selective querying framework for sRMs.

rss · Hugging Face Daily Papers · Sep 30, 01:47

**「Why It Matters」** The finding challenges the assumption that additional test-time compute alone improves reasoning in cheap-to-serve sRMs. It gives agent builders a concrete diagnostic split between execution and knowledge failures before adding more inference steps.

**「Engineer Takeaway」** Watch: when evaluating sRM agents, separate execution bottlenecks from knowledge bottlenecks before scaling test-time compute; for knowledge-bound cases, selective external querying may be more effective than deeper self-refinement.

**Tags**: `#eval`, `#orchestration`, `#harness`

---

<a id="item-agent-engineer-4"></a>
### [HF daily paper: CompoWorld: Compositional Environment Scaling for General Agents](https://huggingface.co/papers/2609.33665) ⭐️ 7.5/10

CompoWorld 论文提出通过组合可复用服务与依赖图来自动生成并验证跨服务任务环境，为通用智能体训练提供可扩展的交互数据来源。

rss · Hugging Face Daily Papers · Sep 30, 01:47

**Tags**: `#eval`, `#orchestration`, `#coding-agent`, `#harness`

---

<a id="item-agent-engineer-5"></a>
### [HF daily paper: Groupwise Agentic Grading and Advantage Redistribution for Code Agent RL](https://huggingface.co/papers/2609.32577) ⭐️ 7.0/10

A new paper proposes GAGAR, an agentic grading framework that redistributes advantages in GRPO for code agent RL to favor higher-quality, targeted implementations.

rss · Hugging Face Daily Papers · Sep 30, 01:47

**Tags**: `#coding-agent`, `#eval`, `#rl`

---

## AI Daily

<a id="item-ai-daily-1"></a>
### [OpenAI 发布 GPT-6.1 Sol](https://openai.com/index/introducing-gpt-6-1-sol) ⭐️ 9.8/10

OpenAI 发布 GPT-6.1 Sol，面向编码、计算机操作与专业工作。官方称其智能水平接近 Astra，API 输入与输出 token 价格为 Astra 标准价格的五分之一。现阶段信息仅来自官方博客，缺乏第三方基准与独立验证。

rss · OpenAI Blog · Sep 29, 10:00

**「为什么重要」** 若官方定价与能力描述成立，编码与 computer use 场景的模型成本结构将显著变化。该影响目前仍属单方面声明，待独立评测确认。

**「可关注」** 可关注：GPT-6.1 Sol 以五分之一 token 价格对标 Astra 级编码与 computer use 能力，可在成本敏感任务中作为候选模型进行对比。

**Tags**: `#model`, `#lab`, `#product`, `#industry`

---

<a id="item-ai-daily-2"></a>
### [OpenAI DevDay 2026 回顾](https://openai.com/index/devday-2026-recap) ⭐️ 9.8/10

OpenAI 官方博客发布 DevDay 2026 回顾，汇总超过 20 项发布，涵盖 GPT-6 Astra、ChatGPT、Codex、API、安全及开发者工具。官方未在文中提供各单项的技术细节或基准数据。

rss · OpenAI Blog · Sep 29, 10:00

**「为什么重要」** 发布清单同时覆盖 GPT-6 Astra、Codex 与 API，显示 OpenAI 在同步迭代模型与开发者工具。对 coding agent / harness 开发者，这是观察官方工具链走向的密集信号。

**「可关注」** 可关注：官方回顾确认 Codex 有更新，但未给出具体变更，需等待后续技术文档才能评估对现有 harness 的影响。

**Tags**: `#model`, `#lab`, `#product`, `#industry`

---

<a id="item-ai-daily-3"></a>
### [GitHub 发布开发者政策更新](https://github.blog/news-insights/policy-news-and-insights/developer-policy-update-transparency-state-policy-and-whats-ahead/) ⭐️ 7.8/10

GitHub 发布开发者政策更新，涉及透明度数据与影响开发者、开源项目的政策调整。官方标题另提及 state policy 及后续动向，但公开摘要未展开具体条款与数据细节。

rss · GitHub Blog · Sep 29, 15:00

**「为什么重要」** 此次更新直接影响开发者与开源项目的使用环境，官方提示需关注透明度数据与政策变化。

**「可关注」** 开发者需查阅 GitHub 官方透明度数据与政策更新全文，评估对现有开源项目的影响。

**Tags**: `#policy`, `#industry`, `#open-source`

---