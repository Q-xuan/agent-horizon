---
layout: default
title: "Horizon Summary: 2026-09-30 (EN)"
date: 2026-09-30
lang: en
---

> From 211 items, 20 important content pieces were selected

---

**Agent Harness Architecture**
1. [anthropics/claude-code released v2.1.285](#item-harness-arch-1) ⭐️ 7.8/10
2. [Cline SDK v0.0.88 Fixes Abort Race and Adds Provider Fallbacks](#item-harness-arch-2) ⭐️ 7.8/10
3. [2.1.285](#item-harness-arch-3) ⭐️ 7.8/10
4. [Cline SDK v0.0.87 发布](#item-harness-arch-4) ⭐️ 6.8/10
5. [Codex rust-v0.159.0 发布](#item-harness-arch-5) ⭐️ 6.3/10
6. [Cline CLI v3.0.66 Fixes Windows Proxy and Turn Cancellation](#item-harness-arch-6) ⭐️ 6.3/10
7. [Gemini CLI v0.64.0-nightly Released](#item-harness-arch-7) ⭐️ 6.3/10
8. [Microsoft SkillOpt Text-Space Optimizer](#item-harness-arch-8) ⭐️ 5.0/10

**AI Agent Engineer**
1. [Getting the Source Right, Not Just the Fact: Source-Aware Verification for MCP Agents](#item-agent-engineer-1) ⭐️ 7.8/10
2. [NVIDIA Kumo Tabular Sets a New Accuracy-Efficiency Frontier for Tabular Prediction](#item-agent-engineer-2) ⭐️ 6.3/10
3. [HF daily paper: TGRL: Temperature-Grouped Reinforcement Learning for Efficient Exploration in LLMs](#item-agent-engineer-3) ⭐️ 6.0/10
4. [GPT 6.1 Sol Cuts Cached Input Pricing](#item-agent-engineer-4) ⭐️ 5.5/10
5. [OpenAI 发布 Dots 常驻代理](#item-agent-engineer-5) ⭐️ 5.5/10
6. [GLM-5.3 二进制利用成功率 4%](#item-agent-engineer-6) ⭐️ 5.5/10
7. [GRAFT：RLVR 训练引入跨模型轨迹交换](#item-agent-engineer-7) ⭐️ 5.5/10
8. [SAKI 用最大耦合路由 token 级监督](#item-agent-engineer-8) ⭐️ 5.5/10
9. [HF daily paper: When Does Dense Retrieval Need Asymmetric Geometry? A Bias-Variance Theory of Shared and Dual Projections](#item-agent-engineer-9) ⭐️ 5.5/10

**AI Daily**
1. [OpenAI 发布 GPT-6 Astra](#item-ai-daily-1) ⭐️ 10.0/10
2. [OpenAI Announces GPT-6.1 Sol](#item-ai-daily-2) ⭐️ 9.8/10
3. [Developer policy update: Transparency, state policy, and what’s ahead](#item-ai-daily-3) ⭐️ 6.3/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [anthropics/claude-code released v2.1.285](https://github.com/anthropics/claude-code/releases/tag/v2.1.285) ⭐️ 7.8/10

Claude Code v2.1.285 adds provider restrictions, MCP install-time configuration, tool toggles, and runtime timeout controls.

github · ashwin-ant · Sep 29, 19:27

**Tags**: `#tools`, `#mcp`, `#permissions`, `#runtime`, `#subagents`

---

<a id="item-harness-arch-2"></a>
### [Cline SDK v0.0.88 Fixes Abort Race and Adds Provider Fallbacks](https://github.com/cline/cline/releases/tag/sdk/sdk/v0.0.88) ⭐️ 7.8/10

Cline SDK v0.0.88 patches the agent runtime and provider adapters. It closes an abort race in \`LocalRuntimeHost\`, adds Anthropic fallback flags, and maps a new \`content-filter\` finish reason through the AI SDK and ApiHandler adapters. The release also restores session resume, registers client version and PID in \`NodeHubClient\`, and refreshes the model catalog.

github · github-actions\[bot\] · Sep 30, 02:32

**「设计要点」** \`LocalRuntimeHost\` re-sends an abort once the run exists and clears a leftover between-turns abort flag when a new turn starts, so a Stop issued during session persistence, git metadata refresh, or credential sync no longer leaves the turn running while the host shows it stopped. The \`content-filter\` finish reason propagates to the run-failed \`sdk.error\` event.

**「改了什么」** Version 0.0.87&\#x27;s duplicate-start guard is reverted so existing session IDs can resume on desktop and TUI; the cloud controller instead stores initial thinking and reasoning-effort preferences in session metadata. Anthropic requests now opt into server-side refusal fallbacks, and \`@ai-sdk/amazon-bedrock\` moves to \`^5.0.98\` to fix Nova 2 Lite high-reasoning-effort 400 errors.

**Tags**: `#runtime`, `#tools`

---

<a id="item-harness-arch-3"></a>
### [2.1.285](https://code.claude.com/docs/en/changelog#2-1-285) ⭐️ 7.8/10

Claude Code 2.1.285 adds tool disablement, plugin/MCP install-time config, and provider permission controls.

rss · Claude Code Changelog · Sep 29, 19:37

**Tags**: `#tools`, `#mcp`, `#permissions`

---

<a id="item-harness-arch-4"></a>
### [Cline SDK v0.0.87 发布](https://github.com/cline/cline/releases/tag/sdk/sdk/v0.0.87) ⭐️ 6.8/10

Cline SDK v0.0.87 修复 Windows hub 启动失败与 token 重复计数。新增 \`ensureLoopbackProxyBypass\(\)\`，在检测到代理变量时把 loopback 地址写入 \`NO\_PROXY\`/\`no\_proxy\`，使 hub 探测绕过 Clash、v2ray 等系统代理；编译态 Bun 入口同时识别 Windows \`B:\\~BUN\\\` 路径，daemon 以 \`--cline-hub-daemon\` 标记启动。\`normalizeUsage\(\)\` 不再让 reasoning tokens 同时出现在 \`outputTokens\` 与 \`reasoningTokenCount\` 中，成本仍按完整 output 计费。

github · github-actions\[bot\] · Sep 29, 05:30

**「设计要点」** Hub daemon 按 socket 记录关闭码、原因、心跳未响应标记与停机状态；\`EADDRINUSE\` 时遥测和日志输出占用者 PID、命令行、实例锁及健康探测结果。Bedrock 将裸 OpenAI GPT-6/GPT-5.6 id 纳入 inference profile 路由，印度区域解析 \`in.\` geo profile，\`@ai-sdk/amazon-bedrock\` 升至 \`^5.0.96\` 后对 profile 内模型改用 \`reasoning.effort\`。

**「改了什么」** hub 在 Windows 系统代理下可稳定启动，token 统计不再双计 reasoning；模型目录扩到 211 个 provider、6,447 个模型，新增 \`bee\` 与 \`pareto\`。\`./cloud\` 导出支持本地会话与 cloud agent 双向移交及可挂起恢复的持久 workspace。

**Tags**: `#runtime`, `#tools`, `#networking`, `#windows`, `#observability`

---

<a id="item-harness-arch-5"></a>
### [Codex rust-v0.159.0 发布](https://github.com/openai/codex/releases/tag/rust-v0.159.0) ⭐️ 6.3/10

Codex Rust v0.159.0 发布。新增 opt-in \`instant\_interrupt\`，可在模型响应或长 code-mode 调用期间用新输入 steer 会话；app-server \`thread/items/list\` 支持从指定 item 起分页。Windows 启动 MCP server、code-mode host 和 piped 命令不再弹出多余控制台，限制性 launcher 可回退 embedded mode。其余为 UI 打磨与权限修复，无破坏性变更。

github · github-actions\[bot\] · Sep 29, 08:05

**「设计要点」** \`instant\_interrupt\` 通过 preempt model responses 和 code-mode yielding 实现输入抢占，需显式开启。approved commands 保留显式文件系统拒绝项，\`.aws\` 目录在可写根目录下默认受保护；exec-server 为每个请求生成唯一进程 ID，MCP 凭据边界在重连后保持。

**「改了什么」** 新增 opt-in \`instant\_interrupt\` 输入抢占和 app-server thread history 分页锚点。Windows MCP 启动修复控制台泄漏并支持 embedded 回退；\`.aws\` 目录纳入默认沙箱保护，macOS 网络沙箱恢复 TLS 信任评估。

**Tags**: `#runtime`, `#mcp`, `#sandbox`, `#planning`

---

<a id="item-harness-arch-6"></a>
### [Cline CLI v3.0.66 Fixes Windows Proxy and Turn Cancellation](https://github.com/cline/cline/releases/tag/cli-v3.0.66) ⭐️ 6.3/10

Cline CLI v3.0.66 is a patch release that fixes Windows proxy startup, turn cancellation, provider failover, and token accounting. Binaries now build with Bun 1.4.2, which stops macOS 27 from killing them at launch and lets x64 builds run on CPUs without AVX2. On Windows, the hub no longer routes loopback discovery through a system proxy, so Clash, v2ray, or corporate proxies no longer trigger &quot;No compatible hub runtime is available&quot;. Pressing Esc right after sending a prompt now stops the turn even while it is still being set up.

github · github-actions\[bot\] · Sep 30, 02:41

**「Design Notes」** The hub daemon logs why each socket closed, reports the process holding a port on EADDRINUSE, and shows connected client version and PID in the web app. Gateway models on providers that mix endpoints keep their own API protocol instead of falling back to the provider-wide default, and direct Anthropic requests use server-side refusal fallback with upstream failover on OpenRouter and Cline.

**「What Changed」** Reasoning tokens are no longer double-counted in output totals, content-filter blocks now suggest rephrasing, and Bedrock inference-profile routing, India \`in.\` profile resolution, and legacy \`awsProfile\` migration are fixed. Yolo mode drops plan/act instructions, UTF-8 BOM cron and task specs parse, \`search\_codebase\` covers PHP and excludes Composer \`vendor\`, Windows \`pwsh -Command\` wrappers preserve the configured shell path, and the model catalog adds Bee and Pareto while making GPT-6.1 Sol the default for many gateways.

**Tags**: `#runtime`, `#tools`

---

<a id="item-harness-arch-7"></a>
### [Gemini CLI v0.64.0-nightly Released](https://github.com/google-gemini/gemini-cli/releases/tag/v0.64.0-nightly.20260930.g38700b4b3) ⭐️ 6.3/10

Gemini CLI published nightly v0.64.0-nightly.20260930.g38700b4b3, an incremental build fixing autonomous plan execution, tool output truncation, A2A settings migration, and folder trust propagation. The release enables non-interactive plan execution, disables truncation when maxChars &lt;= 0, and migrates A2A server settings from V1 to V2. It also bridges PromptResponse.usage into ACP usage\_update notifications and carries resolved folder trust state into headless sessions.

github · gemini-cli-robot · Sep 30, 01:33

**「Design Points」** Non-interactive plan execution now runs without user prompts, and tool output formatting treats maxChars &lt;= 0 as a sentinel to disable truncation. Folder trust decisions resolved at startup propagate into headless mode, while the A2A server adds a V1-to-V2 settings migration path and the ACP layer forwards token usage metadata.

**「What Changed」** This nightly enables autonomous plan execution outside interactive sessions, stops truncating tool output when maxChars is zero or negative, and adds V1-to-V2 settings migration for the A2A server. It also wires PromptResponse.usage into ACP usage\_update notifications and propagates folder trust state in headless mode.

**Tags**: `#runtime`, `#planning`, `#tools`, `#permissions`, `#a2a`

---

<a id="item-harness-arch-8"></a>
### [Microsoft SkillOpt Text-Space Optimizer](https://github.com/microsoft/SkillOpt) ⭐️ 5.0/10

Microsoft&\#x27;s SkillOpt is an open-source text-space optimizer that trains reusable natural-language skills for frozen LLM agents. It applies trajectory-driven edits and validation-gated updates to produce deployable \`best\_skill.md\` artifacts without modifying model weights. The framework treats skill optimization like neural network training, using epochs, mini-batch sizes, learning rates, and validation gates.

rss · GitHub Trending Daily · Sep 30, 02:42

**「Design Points」** SkillOpt freezes the underlying LLM and optimizes skill representations purely in text space. Validation gates filter trajectory-driven edits, and the final output is a standalone markdown artifact rather than updated model parameters.

**Tags**: `#tools`, `#eval`, `#memory`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [Getting the Source Right, Not Just the Fact: Source-Aware Verification for MCP Agents](https://huggingface.co/blog/MultiverseComputingCAI/getting-the-source-right-not-just-the-fact-source) ⭐️ 7.8/10

Hugging Face 博客介绍 ProvenanceGuard 论文，提出 MCP Agent 的‘跨源混淆’失败模式，倡导源感知的事实校验以提升回答归因准确性。

rss · Hugging Face Blog · Sep 29, 13:07

**Tags**: `#mcp`, `#eval`, `#observability`

---

<a id="item-agent-engineer-2"></a>
### [NVIDIA Kumo Tabular Sets a New Accuracy-Efficiency Frontier for Tabular Prediction](https://huggingface.co/blog/nvidia/kumo-tabular) ⭐️ 6.3/10

NVIDIA releases Kumo Tabular, an open tabular foundation model claiming SOTA zero-shot accuracy on four benchmarks, but its impact on agent engineering is limited.

rss · Hugging Face Blog · Sep 29, 15:30

**Tags**: `#foundation-model`, `#tabular-data`, `#eval`

---

<a id="item-agent-engineer-3"></a>
### [HF daily paper: TGRL: Temperature-Grouped Reinforcement Learning for Efficient Exploration in LLMs](https://huggingface.co/papers/2609.33589) ⭐️ 6.0/10

论文提出 Temperature-Grouped Reinforcement Learning（TGRL），通过将温度-induced 的 rollout 多样性转化为显式训练信号，以提升 RLVR 中的探索效率。

rss · Hugging Face Daily Papers · Sep 30, 00:00

**Tags**: `#rl`, `#llm-training`, `#rlvr`, `#exploration`

---

<a id="item-agent-engineer-4"></a>
### [GPT 6.1 Sol Cuts Cached Input Pricing](https://openai.com/index/introducing-gpt-6-1-sol/) ⭐️ 5.5/10

OpenAI released GPT 6.1 Sol, positioning it as near-Astra intelligence at a fifth of the price. The concrete pricing change is cached input at $0.10 per million tokens, which a Hacker News commenter notes is 95% below standard input pricing and 50% below GPT-6 Sol&\#x27;s cached rate. The supplied HN discussion offers no production benchmarks or reproducible traces, only mixed anecdotal reports on coding reliability after earlier Sol 6 regressions.

hackernews · crorella · Sep 29, 17:06 · [Discussion](https://news.ycombinator.com/item?id=49896586)

**「Why It Matters」** Long-context agent workflows that rely on prompt caching face an immediate cost variable change. Whether GPT 6.1 Sol resolves the coding reliability issues users attributed to Sol 6 remains unverified in the thread.

**「Engineer Takeaway」** Watch: Teams running Codex or comparable harnesses with heavy prompt caching can re-evaluate GPT 6.1 Sol on cost alone, yet the absence of reproducible coding benchmarks in the discussion means quality remains unconfirmed.

**「Community Discussion」** HN commenters are split. One user reports switching to Opus 5.5 after Sol 6 coding regressions and is skeptical of 6.1; another calls the cache price the &quot;actual big announcement&quot; for Codex mileage. A third frames token price as the industry&\#x27;s new battleground.

**Tags**: `#coding-agent`, `#eval`, `#harness`

---

<a id="item-agent-engineer-5"></a>
### [OpenAI 发布 Dots 常驻代理](https://openai.com/index/introducing-dots/) ⭐️ 5.5/10

OpenAI 于 2026 年 9 月 29 日公布 always-on agent 产品 Dots。官方公告未披露架构、技术细节或基准；现有材料仅包含 Hacker News 评论，讨论集中于产品策略与平台锁定，无工程实质内容。

hackernews · alvis · Sep 29, 17:07 · [Discussion](https://news.ycombinator.com/item?id=49896604)

**「为什么重要」** 对 coding agent 与 harness 开发者而言，Dots 是 OpenAI 在常驻代理方向的公开动作，但当前信息不足以判断其技术路线、记忆机制或与现有工具的互操作性。

**「可关注」** 可关注：Dots 与 Codex、ChatGPT Work 的边界在社区中已显模糊，在官方给出架构说明或 API 变化前，不宜将其纳入现有 agent 工作流假设。

**「评论」** 评论认为 always-on agent 会借集成与工作历史加深平台绑定，并猜测封闭模型厂商意在模型之上构建抽象层；亦有用户对比 Muse，认为其更贴近消费者且具备 Meta 应用分发优势。

**Tags**: `#coding-agent`, `#orchestration`, `#memory`

---

<a id="item-agent-engineer-6"></a>
### [GLM-5.3 二进制利用成功率 4%](https://simonwillison.net/2026/Sep/29/anthropic-frontier-red-team/) ⭐️ 5.5/10

Anthropic Frontier Red Team 从内部 Binary Exploitation 基准随机抽取 100 个任务，测得 GLM-5.3 完整控制流劫持成功率为 4%，Claude Mythos Preview 为 6%。此前模型 Claude Opus 4.6 与 GLM-5.2 在这些任务上均未成功。报告认为一个有意义的能力阈值已被跨过。

rss · Simon Willison · Sep 29, 22:20

**「为什么重要」** 这是官方一方基准数据，给出 4%、6% 与 0% 的具体对比，显示二进制利用能力出现代际跃升。对 agent 工程工作流、harness 与工具链的直接影响仍间接且狭窄，但可作为能力边界的参考基线。

**「可关注」** 可关注：二进制利用从 0% 到 4%/6% 的跨越，表明模型已能完成完整控制流劫持，但当前成功率仍低，距离可靠工程化应用尚有距离。

**Tags**: `#eval`, `#coding-agent`, `#ai-security-research`, `#benchmark`

---

<a id="item-agent-engineer-7"></a>
### [GRAFT：RLVR 训练引入跨模型轨迹交换](https://huggingface.co/papers/2609.37868) ⭐️ 5.5/10

2026-09-30，Hugging Face Daily Papers 收录论文《Learning Beyond What You Sample: Off-Policy-Aware Cross-Model Trajectory Exchange for RLVR》，提出 GRAFT 框架。该方法针对 GRPO 等 RLVR 训练中有限 rollout 预算产生的 all-fail groups，用异构模型的 peer trajectories 替换，以恢复 policy-gradient 信号。论文指出异构模型常在互补 prompt 上成功，无需指定更强教师即可互学。目前仅为论文方法，未提供生产 trace 或工具链变更。

rss · Hugging Face Daily Papers · Sep 30, 00:00

**「为什么重要」** RLVR 训练受 rollout 预算限制，all-fail groups 会直接丢失梯度信号。GRAFT 提供了一条不依赖更强教师模型的信号恢复路径，对受此困扰的训练者有参考价值。但论文尚未给出生产环境验证或可复用工具链，实际效果待观察。

**「可关注」** 可关注：GRAFT 用异构模型的 peer trajectories 填补 all-fail groups，把互补成功轨迹转化为 RLVR 的 policy-gradient 信号，但论文未提供生产 trace 或立即可用的工具链变更。

**Tags**: `#eval`, `#coding-agent`, `#rlvr`

---

<a id="item-agent-engineer-8"></a>
### [SAKI 用最大耦合路由 token 级监督](https://huggingface.co/papers/2609.36601) ⭐️ 5.5/10

Hugging Face 每日论文发布 SAKI，一种面向 on-policy 蒸馏的最大耦合路由 token 级监督方法。论文指出弱学生可能进入教师未覆盖的前缀，监督信号失真；SAKI 将 KL 约束的教师引导 rollout 与最大耦合结合，按接受/修正事件路由监督：接受位置保留采样 token 的反向 KL，修正位置直接监督教师最高概率 token。理论层面，最大耦合下修正概率恰为 TV\(p\_t, q\_t\)，同一信任域半径同时控制 rollout 偏差并给出干预与专门化监督的上界（原文截断）。论文发布于 2026-09-30，获 7 次 upvote，暂无社区评论。

rss · Hugging Face Daily Papers · Sep 30, 00:00

**「为什么重要」** coding agent 与 harness 工程不直接受此影响，论文属于上游模型训练方法。若团队正在做学生模型蒸馏或 on-policy 训练，其信任域与干预概率的对应关系值得调研；否则今日扫描即可。

**「可关注」** 可关注：SAKI 将修正概率与 TV\(p\_t, q\_t\) 精确绑定，用同一信任域半径同时约束 rollout 偏差和监督干预，为 on-policy 蒸馏的干预强度提供可计算的理论上界。

**Tags**: `#distillation`, `#training`, `#on-policy`, `#llm`

---

<a id="item-agent-engineer-9"></a>
### [HF daily paper: When Does Dense Retrieval Need Asymmetric Geometry? A Bias-Variance Theory of Shared and Dual Projections](https://huggingface.co/papers/2609.32488) ⭐️ 5.5/10

Introduces a bias-variance theory for choosing between shared and dual query-document projections in dense retrieval and proposes the Cross-fitted Asymmetry Risk Selector \(CARS\).

rss · Hugging Face Daily Papers · Sep 30, 00:00

**Tags**: `#retrieval`, `#rag`, `#eval`

---

## AI Daily

<a id="item-ai-daily-1"></a>
### [OpenAI 发布 GPT-6 Astra](https://openai.com/index/devday-2026-recap) ⭐️ 10.0/10

OpenAI 在 DevDay 2026 上公布超过 20 项更新，重点包括 GPT-6 Astra 模型，以及 ChatGPT、Codex、API 和安全工具的改进。官方回顾同时提到面向开发者的新工具。当前信息仅来自 OpenAI 博客，尚无社区讨论或第三方验证。

rss · OpenAI Blog · Sep 29, 10:00

**「为什么重要」** Codex 与 API 的更新会直接影响 coding agent 与 harness 的集成方式，GPT-6 Astra 的发布也可能改变现有模型选型基线。

**「可关注」** 可关注：Codex 与 API 的具体变更，以及 GPT-6 Astra 在编码场景下的实际表现，需等待官方文档与社区实测补充。

**Tags**: `#model`, `#lab`, `#product`, `#industry`

---

<a id="item-ai-daily-2"></a>
### [OpenAI Announces GPT-6.1 Sol](https://openai.com/index/introducing-gpt-6-1-sol) ⭐️ 9.8/10

OpenAI announced GPT-6.1 Sol, a model for coding, computer use, and professional work. The company prices it at one-fifth of Astra&\#x27;s standard API input and output token rates. OpenAI claims near-Astra intelligence.

rss · OpenAI Blog · Sep 29, 10:00

**「Why It Matters」** The pricing targets Astra&\#x27;s capability tier at a fraction of the cost, which could shift budget calculations for coding and computer-use agent workloads.

**「Engineer Takeaway」** Watch: GPT-6.1 Sol&\#x27;s standard API input and output tokens are priced at one-fifth of Astra&\#x27;s rates.

**Tags**: `#model`, `#lab`, `#product`

---

<a id="item-ai-daily-3"></a>
### [Developer policy update: Transparency, state policy, and what’s ahead](https://github.blog/news-insights/policy-news-and-insights/developer-policy-update-transparency-state-policy-and-whats-ahead/) ⭐️ 6.3/10

GitHub官方博客发布开发者政策更新，提及透明度数据及影响开发者和开源的政策变化，但所给内容缺乏具体细节。

rss · GitHub Blog · Sep 29, 15:00

**Tags**: `#policy`, `#industry`, `#open-source`

---