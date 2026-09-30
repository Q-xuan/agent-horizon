---
layout: default
title: "Horizon Summary: 2026-09-30 (ZH)"
date: 2026-09-30
lang: zh
---

> 从 211 条内容中筛选出 20 条重要资讯。

---

**Harness 架构**
1. [anthropics/claude-code released v2.1.285](#item-harness-arch-1) ⭐️ 7.8/10
2. [Cline SDK v0.0.88 发布](#item-harness-arch-2) ⭐️ 7.8/10
3. [2.1.285](#item-harness-arch-3) ⭐️ 7.8/10
4. [Cline SDK v0.0.87 发布](#item-harness-arch-4) ⭐️ 6.8/10
5. [Codex rust-v0.159.0 发布](#item-harness-arch-5) ⭐️ 6.3/10
6. [Cline CLI v3.0.66 发布](#item-harness-arch-6) ⭐️ 6.3/10
7. [Gemini CLI v0.64.0-nightly 发布](#item-harness-arch-7) ⭐️ 6.3/10
8. [microsoft/SkillOpt 开源](#item-harness-arch-8) ⭐️ 5.0/10

**Agent 工程师日报**
1. [Getting the Source Right, Not Just the Fact: Source-Aware Verification for MCP Agents](#item-agent-engineer-1) ⭐️ 7.8/10
2. [NVIDIA Kumo Tabular Sets a New Accuracy-Efficiency Frontier for Tabular Prediction](#item-agent-engineer-2) ⭐️ 6.3/10
3. [HF daily paper: TGRL: Temperature-Grouped Reinforcement Learning for Efficient Exploration in LLMs](#item-agent-engineer-3) ⭐️ 6.0/10
4. [GPT 6.1 Sol 发布，缓存输入降价](#item-agent-engineer-4) ⭐️ 5.5/10
5. [OpenAI 发布 Dots 常驻代理](#item-agent-engineer-5) ⭐️ 5.5/10
6. [GLM-5.3 二进制利用成功率 4%](#item-agent-engineer-6) ⭐️ 5.5/10
7. [GRAFT：异构模型互学改进 RLVR 训练](#item-agent-engineer-7) ⭐️ 5.5/10
8. [SAKI 改进 on-policy 蒸馏监督](#item-agent-engineer-8) ⭐️ 5.5/10
9. [HF daily paper: When Does Dense Retrieval Need Asymmetric Geometry? A Bias-Variance Theory of Shared and Dual Projections](#item-agent-engineer-9) ⭐️ 5.5/10

**AI 日报**
1. [OpenAI DevDay 2026 回顾](#item-ai-daily-1) ⭐️ 10.0/10
2. [OpenAI 推出 GPT-6.1 Sol](#item-ai-daily-2) ⭐️ 9.8/10
3. [Developer policy update: Transparency, state policy, and what’s ahead](#item-ai-daily-3) ⭐️ 6.3/10

---

## Harness 架构

<a id="item-harness-arch-1"></a>
### [anthropics/claude-code released v2.1.285](https://github.com/anthropics/claude-code/releases/tag/v2.1.285) ⭐️ 7.8/10

Claude Code v2.1.285 adds provider restrictions, MCP install-time configuration, tool toggles, and runtime timeout controls.

github · ashwin-ant · 9月29日 19:27

**标签**: `#tools`, `#mcp`, `#permissions`, `#runtime`, `#subagents`

---

<a id="item-harness-arch-2"></a>
### [Cline SDK v0.0.88 发布](https://github.com/cline/cline/releases/tag/sdk/sdk/v0.0.88) ⭐️ 7.8/10

Cline SDK v0.0.88 修复 agent 运行时的 abort 竞态，补上 Anthropic 供应商回退，并新增 content-filter 结束原因。此前在 runTurn\(\) 入口到 run 启动之间发出的 Stop 会被丢弃，LocalRuntimeHost 现在会在 run 存在后重发 abort，并在新 turn 开始时清理残留的 between-turns abort 标记。0.0.87 的重复启动守卫被回退，桌面端和 TUI 恢复会话不再被 &quot;session already exists&quot; 拒绝。模型目录刷新，GPT-6.1 Sol 成为多家供应商默认模型。

github · github-actions\[bot\] · 9月30日 02:32

**「设计要点」** LocalRuntimeHost 在 run 尚未创建时缓存 abort，run 启动后补发，避免 Stop 在会话持久化、git 元数据刷新、凭据同步期间丢失。AI SDK 与 ApiHandler 适配器统一映射新的 AgentModelFinishReason，content-filter 会以 run-failed sdk.error 事件透出。

**「改了什么」** 相对 0.0.87，回退了阻止会话恢复的重复启动守卫；Anthropic 直连与 OpenRouter/Cline 转发支持 provider fallback；Bedrock 适配器升级到 ^5.0.98 以支持 Nova 2 Lite 高推理强度。

**标签**: `#runtime`, `#tools`

---

<a id="item-harness-arch-3"></a>
### [2.1.285](https://code.claude.com/docs/en/changelog#2-1-285) ⭐️ 7.8/10

Claude Code 2.1.285 adds tool disablement, plugin/MCP install-time config, and provider permission controls.

rss · Claude Code Changelog · 9月29日 19:37

**标签**: `#tools`, `#mcp`, `#permissions`

---

<a id="item-harness-arch-4"></a>
### [Cline SDK v0.0.87 发布](https://github.com/cline/cline/releases/tag/sdk/sdk/v0.0.87) ⭐️ 6.8/10

Cline SDK v0.0.87 发布，修复 Windows hub 启动失败与 token 重复计数。新增 \`ensureLoopbackProxyBypass\(\)\`，在系统代理环境下为 Bun fetch 添加 loopback 绕过，并识别 Windows 编译 Bun 入口路径。Bedrock 路由与 provider-settings 迁移同步修正，模型目录扩至 211 个 provider、6,447 个模型。

github · github-actions\[bot\] · 9月29日 05:30

**「设计要点」** Hub daemon 跑在 Bun 上，靠 \`NO\_PROXY\` 绕过系统代理完成 loopback 探测；socket close 与端口占用日志补齐了 daemon 可观测性。\`normalizeUsage\(\)\` 把 reasoning tokens 从 \`outputTokens\` 中剥离，避免会话统计与遥测重复计费。

**「改了什么」** Windows 下 hub 启动不再因系统代理失败；Bedrock 上裸 OpenAI 模型走 inference profile 并适配 \`reasoning.effort\`；\`./cloud\` 支持本地与云端 agent 双向移交及持久工作区挂起恢复。

**标签**: `#runtime`, `#tools`, `#networking`, `#windows`, `#observability`

---

<a id="item-harness-arch-5"></a>
### [Codex rust-v0.159.0 发布](https://github.com/openai/codex/releases/tag/rust-v0.159.0) ⭐️ 6.3/10

Codex Rust v0.159.0 发布。新增 opt-in \`instant\_interrupt\`，允许在模型响应或长 code-mode 调用期间用新输入抢占当前轮次。App-server 客户端可通过 item anchors 从特定项分页线程历史。Windows 启动修复抑制 MCP 服务器、code-mode 主机和管道命令的杂散控制台窗口，限制性启动器回退到 embedded mode。沙盒默认保护 \`.aws\` 目录，已批准命令保留显式文件系统拒绝。同时移除自动后续提示建议和 \`plugin-creator\` 技能。

github · github-actions\[bot\] · 9月29日 08:05

**「设计要点」** \`instant\_interrupt\` 在模型响应和 code-mode 执行期间接收新输入并抢占当前轮次；App-server 通过 item anchors 扩展 \`thread/items/list\` 分页；Windows 启动层在限制性环境下回退到 embedded mode。

**「改了什么」** 新增 opt-in \`instant\_interrupt\` 输入引导；App-server 支持从特定项分页线程历史；Windows MCP 与 code-mode 启动修复，抑制杂散控制台窗口并支持 embedded mode 回退；沙盒默认保护 \`.aws\` 目录，已批准命令保留文件系统拒绝；移除 \`tui.prompt\_suggestions\` 设置与 \`plugin-creator\` 技能。

**标签**: `#runtime`, `#mcp`, `#sandbox`, `#planning`

---

<a id="item-harness-arch-6"></a>
### [Cline CLI v3.0.66 发布](https://github.com/cline/cline/releases/tag/cli-v3.0.66) ⭐️ 6.3/10

Cline CLI v3.0.66 发布，修复 Windows 系统代理下 hub 启动失败、回合设置期间 Esc 停止失效、Anthropic 模型故障转移缺失及推理 token 重复计算。构建切换到 Bun 1.4.2，x64 二进制支持无 AVX2 的 CPU，macOS 27 启动终止问题同步解决。Bedrock 侧补上 GPT-6/GPT-5.6 推理配置文件路由与印度区域 \`in.\` 配置文件解析，模型目录更新多提供商默认模型。

github · github-actions\[bot\] · 9月30日 02:41

**「设计要点」** 本地 hub 用环回发现请求探测运行时，Windows 系统代理会拦截这些请求并造成启动误判；模型路由层为 Bedrock 和混合端点提供商维护独立的推理配置文件与 API 协议，避免回退到提供商级默认值。

**「改了什么」** 相对 v3.0.65，CLI 增加 Anthropic 拒绝回退与多上游故障转移，Bedrock 支持推理配置文件路由和印度区域；工具层扩展 PHP 检索并排除 Composer \`vendor\`，Windows 执行层收紧 shell 路径解析以防工作区植入的可执行文件被拾取。

**标签**: `#runtime`, `#tools`

---

<a id="item-harness-arch-7"></a>
### [Gemini CLI v0.64.0-nightly 发布](https://github.com/google-gemini/gemini-cli/releases/tag/v0.64.0-nightly.20260930.g38700b4b3) ⭐️ 6.3/10

Gemini CLI 发布 v0.64.0-nightly.20260930.g38700b4b3。本次 nightly 修复非交互模式下的自主计划执行、工具输出截断、A2A 设置迁移，以及 headless 模式下的文件夹信任传播。ACP 层同时桥接 PromptResponse.usage 并发出 usage\_update 通知。

github · gemini-cli-robot · 9月30日 01:33

**「设计要点」** 自主计划执行在非交互模式下启用，headless 模式会传播解析后的文件夹信任状态。A2A server 实现 V1 到 V2 的设置迁移逻辑。

**「改了什么」** 非交互模式启用自主计划执行，formatTruncatedToolOutput 在 maxChars &lt;= 0 时禁用截断，A2A server 增加 V1 到 V2 设置迁移，headless 模式传播文件夹信任状态，ACP 桥接 PromptResponse.usage 并发出 usage\_update 通知。

**标签**: `#runtime`, `#planning`, `#tools`, `#permissions`, `#a2a`

---

<a id="item-harness-arch-8"></a>
### [microsoft/SkillOpt 开源](https://github.com/microsoft/SkillOpt) ⭐️ 5.0/10

微软开源 SkillOpt，一个面向冻结 LLM agent 的文本空间优化器。它通过轨迹驱动编辑和验证门控训练可复用的自然语言技能，产出可部署的 best\_skill.md。项目把技能优化类比为神经网络训练，引入 epoch、mini-batch、学习率与验证门，但不更新模型权重。当前信息来自 GitHub Trending 二手描述，缺少代码路径、架构图与实现约束。

rss · GitHub Trending Daily · 9月30日 02:42

**「设计要点」** SkillOpt 将 agent 技能视为可训练文本，在冻结模型权重的前提下，用轨迹驱动编辑迭代自然语言指令，并以验证门控筛选更新，最终固化为 best\_skill.md。

**标签**: `#tools`, `#eval`, `#memory`

---

## Agent 工程师日报

<a id="item-agent-engineer-1"></a>
### [Getting the Source Right, Not Just the Fact: Source-Aware Verification for MCP Agents](https://huggingface.co/blog/MultiverseComputingCAI/getting-the-source-right-not-just-the-fact-source) ⭐️ 7.8/10

Hugging Face 博客介绍 ProvenanceGuard 论文，提出 MCP Agent 的‘跨源混淆’失败模式，倡导源感知的事实校验以提升回答归因准确性。

rss · Hugging Face Blog · 9月29日 13:07

**标签**: `#mcp`, `#eval`, `#observability`

---

<a id="item-agent-engineer-2"></a>
### [NVIDIA Kumo Tabular Sets a New Accuracy-Efficiency Frontier for Tabular Prediction](https://huggingface.co/blog/nvidia/kumo-tabular) ⭐️ 6.3/10

NVIDIA releases Kumo Tabular, an open tabular foundation model claiming SOTA zero-shot accuracy on four benchmarks, but its impact on agent engineering is limited.

rss · Hugging Face Blog · 9月29日 15:30

**标签**: `#foundation-model`, `#tabular-data`, `#eval`

---

<a id="item-agent-engineer-3"></a>
### [HF daily paper: TGRL: Temperature-Grouped Reinforcement Learning for Efficient Exploration in LLMs](https://huggingface.co/papers/2609.33589) ⭐️ 6.0/10

论文提出 Temperature-Grouped Reinforcement Learning（TGRL），通过将温度-induced 的 rollout 多样性转化为显式训练信号，以提升 RLVR 中的探索效率。

rss · Hugging Face Daily Papers · 9月30日 00:00

**标签**: `#rl`, `#llm-training`, `#rlvr`, `#exploration`

---

<a id="item-agent-engineer-4"></a>
### [GPT 6.1 Sol 发布，缓存输入降价](https://openai.com/index/introducing-gpt-6-1-sol/) ⭐️ 5.5/10

OpenAI 发布 GPT 6.1 Sol，标题称智能接近 Astra，价格约为其五分之一。HN 讨论中最具体的可验证细节是缓存输入定价：每百万 token 0.10 美元，较标准输入低 95%，较 GPT-6 Sol 缓存输入低 50%。用户对编码可靠性反馈分歧，有报告称 Sol 6 相比 Sol 5.6 出现退化，也有用户因成本因素转向 DeepSeek。官方公告原文未在材料中提供，技术细节有限。

hackernews · crorella · 9月29日 17:06 · [社区讨论](https://news.ycombinator.com/item?id=49896586)

**「为什么重要」** 缓存输入再降 50% 直接降低 Codex 等编码 agent 的长上下文调用成本。但模型编码质量尚未形成一致结论，成本优势能否抵消可靠性风险仍待观察。

**「可关注」** 可关注：GPT 6.1 Sol 缓存输入较 GPT-6 Sol 再降 50%，在长上下文编码场景中值得重新评估其与 Opus 5.5 等替代方案的成本-质量平衡。

**「评论」** 社区对编码能力看法分裂：有用户称 Sol 6 相比 Sol 5.6 大幅退化并转向 Opus 5.5，也有用户认为 DeepSeek 智能差异已可忽略；缓存降价则被明确视为对 Codex 使用者的重要成本改善。

**标签**: `#coding-agent`, `#eval`, `#harness`

---

<a id="item-agent-engineer-5"></a>
### [OpenAI 发布 Dots 常驻代理](https://openai.com/index/introducing-dots/) ⭐️ 5.5/10

OpenAI 于 2026 年 9 月 29 日宣布推出 Dots，定位为 always-on agent 产品。当前材料未包含架构说明、技术规格或可复现基准，仅提供 Hacker News 社区讨论。评论围绕产品线重叠、平台锁定与订阅策略展开，缺乏工程实现细节。

hackernews · alvis · 9月29日 17:07 · [社区讨论](https://news.ycombinator.com/item?id=49896604)

**「为什么重要」** OpenAI 进入常驻代理领域，但缺乏公开技术细节，对 coding agent 工程师的即时影响仍不明确。社区对平台锁定的担忧提示，若代理依赖深度集成与长期记忆，跨平台迁移与数据可携带性可能成为核心设计约束。

**「可关注」** 可关注：Dots 与 Codex、ChatGPT Work 的产品边界在社区讨论中已显模糊，常驻代理若依赖平台集成与工作历史，工程上需提前评估数据可携带性与供应商锁定风险。

**「评论」** Hacker News 评论对 Dots 定位存在分歧。一方认为 always-on agent 会通过平台集成与工作历史锁定用户，形成“云上计算机”式的迁移壁垒；另一方则指出 Codex、ChatGPT Work 与 Dots 的界限日益模糊，并对比 Meta 的 Muse，认为后者在消费端更具分发优势。

**标签**: `#coding-agent`, `#orchestration`, `#memory`

---

<a id="item-agent-engineer-6"></a>
### [GLM-5.3 二进制利用成功率 4%](https://simonwillison.net/2026/Sep/29/anthropic-frontier-red-team/) ⭐️ 5.5/10

Anthropic Frontier Red Team 在内部 Binary Exploitation benchmark 的 100 个随机任务上评估多个模型，发现 GLM-5.3 在 4% 的试验中完成完整控制流劫持，Claude Mythos Preview 为 6%。早期模型 Claude Opus 4.6 和 GLM-5.2 在这些任务上均未成功。报告认为这标志着一个有意义的能力阈值已被跨过。

rss · Simon Willison · 9月29日 22:20

**「为什么重要」** 这是 Anthropic 官方第一方 benchmark 数据，用具体成功率（4% vs 6% vs 0%）标出二进制利用能力的阈值变化。对 coding agent 工程工作流、harness 或工具链的直接影响仍间接且狭窄，目前更像一个能力信号而非可操作的变更。

**「可关注」** 可关注：GLM-5.3 与 Claude Mythos Preview 在内部 Binary Exploitation benchmark 上取得非零成功率（4% 与 6%），而 Claude Opus 4.6 和 GLM-5.2 为 0%，能力阈值已现，但绝对水平仍低。

**标签**: `#eval`, `#coding-agent`, `#ai-security-research`, `#benchmark`

---

<a id="item-agent-engineer-7"></a>
### [GRAFT：异构模型互学改进 RLVR 训练](https://huggingface.co/papers/2609.37868) ⭐️ 5.5/10

GRAFT 框架针对 RLVR 训练中 rollout 预算有限导致的全失败组（all-fail groups）问题，用异构模型的 peer trajectories 替换这些组以恢复策略梯度信号。论文观察到不同模型在互补提示上成功，无需指定更强教师即可互学。GRAFT 全称 Gated Replacement of Answer-Failed groups with peer Trajectories，采用 off-policy-aware 设计。论文于 2026-09-30 发布，获 13 个 upvotes。

rss · Hugging Face Daily Papers · 9月30日 00:00

**「为什么重要」** RLVR 训练依赖成功轨迹产生奖励信号，全失败组会浪费 rollout 预算。GRAFT 提供了一条不增加 rollout 成本、利用异构模型互补性的路径。目前材料未提供生产环境 trace 或工具链变更，影响面仍限于方法论层面。

**「可关注」** GRAFT 在不增加 rollout 成本的前提下，用异构模型轨迹替换 RLVR 全失败组以恢复策略梯度信号，其 off-policy-aware 设计未指定更强教师。

**标签**: `#eval`, `#coding-agent`, `#rlvr`

---

<a id="item-agent-engineer-8"></a>
### [SAKI 改进 on-policy 蒸馏监督](https://huggingface.co/papers/2609.36601) ⭐️ 5.5/10

2026-09-30，Hugging Face Daily Papers 收录论文 SAKI（Supervision Allocation with KL-constrained Interpolation）。针对 on-policy 蒸馏中弱学生可能进入教师未对齐前缀的问题，SAKI 将 KL 约束的教师引导 rollout 与最大耦合结合，按实际接受/纠正事件路由 token 级监督：接受位置保留采样 token 的反向 KL 监督，纠正位置直接监督教师最高概率 token。在最大耦合下，纠正概率恰为 TV\(p\_t, q\_t\)，因此同一信任域半径可同时控制 rollout 偏差并上界干预与专用监督。该论文提供理论保证，但属于模型训练方法论，对 agent 工程工作流的直接影响有限。

rss · Hugging Face Daily Papers · 9月30日 00:00

**「为什么重要」** 对 coding agent / harness 工程师而言，这不是工具链或协议变更，而是上游训练方法的改进。只有当你负责学生模型训练或 on-policy 蒸馏时，才需要深入；否则只需了解其存在。

**「可关注」** SAKI 用同一 trust-region 半径统一约束 rollout 偏差与监督干预，理论边界明确；若当前工作聚焦 agent 编排、协议或评测框架，本篇不构成直接依赖。

**标签**: `#distillation`, `#training`, `#on-policy`, `#llm`

---

<a id="item-agent-engineer-9"></a>
### [HF daily paper: When Does Dense Retrieval Need Asymmetric Geometry? A Bias-Variance Theory of Shared and Dual Projections](https://huggingface.co/papers/2609.32488) ⭐️ 5.5/10

Introduces a bias-variance theory for choosing between shared and dual query-document projections in dense retrieval and proposes the Cross-fitted Asymmetry Risk Selector \(CARS\).

rss · Hugging Face Daily Papers · 9月30日 00:00

**标签**: `#retrieval`, `#rag`, `#eval`

---

## AI 日报

<a id="item-ai-daily-1"></a>
### [OpenAI DevDay 2026 回顾](https://openai.com/index/devday-2026-recap) ⭐️ 10.0/10

OpenAI 官方博客发布 DevDay 2026 回顾，汇总超过 20 项发布，涉及 GPT-6 Astra、ChatGPT、Codex、API、安全工具及面向开发者的新工具。官方摘要未展开具体参数、基准或可用性细节。

rss · OpenAI Blog · 9月29日 10:00

**「为什么重要」** 该回顾来自 OpenAI 官方，汇总了模型、API 与安全工具等多个方向的更新，是开发者了解其生态变化的直接材料。

**「可关注」** 可关注：官方摘要提到的 GPT-6 Astra、Codex 与 API 更新，后续是否会释放更具体的接入方式与限制。

**标签**: `#model`, `#lab`, `#product`, `#industry`

---

<a id="item-ai-daily-2"></a>
### [OpenAI 推出 GPT-6.1 Sol](https://openai.com/index/introducing-gpt-6-1-sol) ⭐️ 9.8/10

OpenAI 发布 GPT-6.1 Sol，面向编程、computer use 和专业工作。官方称其智能水平接近 Astra，API 输入与输出 token 价格均为 Astra 标准价格的五分之一。目前仅有一句官方描述，尚无基准测试或详细规格。

rss · OpenAI Blog · 9月29日 10:00

**「为什么重要」** 若定价与能力描述属实，编程和 computer use 场景的调用成本会大幅下降。对 coding agent 与 harness 开发者来说，模型选型可能多一个低价候选。

**「可关注」** 可关注：GPT-6.1 Sol 的 API 价格定为 Astra 的五分之一，可先在小规模编程与 computer use 任务上测试其实际表现，再评估是否纳入现有工作流。

**标签**: `#model`, `#lab`, `#product`

---

<a id="item-ai-daily-3"></a>
### [Developer policy update: Transparency, state policy, and what’s ahead](https://github.blog/news-insights/policy-news-and-insights/developer-policy-update-transparency-state-policy-and-whats-ahead/) ⭐️ 6.3/10

GitHub 官方博客发布开发者政策更新，提及透明度数据及影响开发者和开源的政策变化，但所给内容缺乏具体细节。

rss · GitHub Blog · 9月29日 15:00

**标签**: `#policy`, `#industry`, `#open-source`

---