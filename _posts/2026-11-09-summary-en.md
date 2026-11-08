---
layout: default
title: "Horizon Summary: 2026-11-09 (EN)"
date: 2026-11-09
lang: en
---

> From 133 items, 7 important content pieces were selected

---

**Agent Harness Architecture**
1. [openai-agents-js v0.22.0-alpha.2 发布](#item-harness-arch-1) ⭐️ 8.8/10
2. [Agents SDK v0.24.0 发布](#item-harness-arch-2) ⭐️ 7.8/10
3. [Google 官方 agent skills 仓库 google/skills 发布](#item-harness-arch-3) ⭐️ 5.0/10
4. [Cloudflare 安全审计技能](#item-harness-arch-4) ⭐️ 5.0/10

**AI Agent Engineer**
1. [CS146S 调整 Monaco 工具选型](#item-agent-engineer-1) ⭐️ 7.0/10
2. [SQLite parse\_number C/Rust 对比](#item-agent-engineer-2) ⭐️ 6.0/10
3. [Kimi-K3.1 三级量化单卡实验](#item-agent-engineer-3) ⭐️ 5.5/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [openai-agents-js v0.22.0-alpha.2 发布](https://github.com/openai/openai-agents-js/releases/tag/v0.22.0-alpha.2) ⭐️ 8.8/10

OpenAI 发布 JS Agents SDK v0.22.0-alpha.2。该 alpha 版本新增原生工具执行（fileSearch、codeInterpreter、imageGeneration）、运行预算控制（RunBudget、maxModelSteps）、应用拥有的 SessionStore 会话恢复，以及 A2A 1.0 协议连接。预览版暂不支持 MCP、手动工具、环境、原生子代理、目标及可移植检查点。

github · markstuart-oai · Nov 8, 08:27

**「设计要点」** 原生运行时由 @openai/agents-codex 承载，与经典运行时分离。SessionStore 由应用拥有以支持持久化恢复。A2A 1.0 适配器使用 JSON-RPC 轮询，授权、存储与执行由应用管理。执行器写入默认采用 strict 策略。

**「改了什么」** 新增 fileSearch\(\)、codeInterpreter\(\)、imageGeneration\(\) 原生工具及 webSearch\(\) 过滤与引用能力。新增 RunBudget 与 maxModelSteps 控制运行开销。新增应用拥有的 SessionStore 与 fileSessionStore\(\) 适配器。新增 A2A 1.0 连接。移除实验性 SDKRunner 桥接与 migration 导入，原生与经典工作流分离。

**「评论」** 无社区评论。

**Tags**: `#runtime`, `#tools`, `#a2a`, `#memory`, `#sandbox`

---

<a id="item-harness-arch-2"></a>
### [Agents SDK v0.24.0 发布](https://github.com/openai/openai-agents-python/releases/tag/v0.24.0-alpha.7) ⭐️ 7.8/10

OpenAI Agents Python SDK v0.24.0-alpha.7 发布，支持 Classic 工作流与原生执行并行、应用侧自定义 Session 存储、托管工具及更严格的默认写入策略。新版本通过 \`agents.classic\` 保留旧运行时，同时扩展原生代理的语音、上下文钩子和运行预算能力。Environment 默认 \`write\_policy=&quot;strict&quot;\`，仅本地执行强制启用，远程及 Windows 环境需显式设置 \`write\_policy=&quot;legacy&quot;\`。

github · markstuart-oai · Nov 8, 07:05

**「设计要点」** 运行时分 Classic 与 Native 双轨。Session 支持 \`CustomStorage\` 和 \`SQLiteSessionStore\` 持久化根历史，托管工具需 API-key provider 与标准 Responses 模型。执行器写入策略默认收紧，本地执行强制 strict 模式，远程执行需显式选择 legacy。

**「改了什么」** 相对 v0.24.0-alpha.6，新增 Classic 工作流导入路径、应用侧持久化 Session 存储、语音工作流 \`NativeSessionVoiceWorkflow\`、托管工具（FileSearch、CodeInterpreter、ImageGeneration）、上下文与完成钩子（\`transform\_context\`、\`before\_complete\`）、运行预算 \`RunBudget\`、MCP 资源/提示词支持、本地执行 \`Environment.local\(\)\` 及 A2A 适配器。MCP 审批模式重命名（\`auto\`→\`native\`，\`approve\`→\`preapproved\`），\`NativeAgents.before\_step\` 回调签名变更，默认推理 effort 从 \`low\` 调至 \`medium\`，Environment 默认写入策略改为 \`strict\`。

**「评论」** 无社区评论。

**Tags**: `#runtime`, `#tools`, `#sandbox`, `#memory`

---

<a id="item-harness-arch-3"></a>
### [Google 官方 agent skills 仓库 google/skills 发布](https://github.com/google/skills) ⭐️ 5.0/10

这是 Google 发布的官方预构建 agent 技能仓库，覆盖 Google 产品及技术（含 Google Cloud），支持通过 npx 安装；若环境无 npx 需先安装 Node.js。当前公开内容仅包含基础安装、更新说明，未披露技能架构、harness 集成、权限模型等技术实现细节。

rss · GitHub Trending Daily · Nov 8, 23:00

**「改了什么」** 新增官方可安装的 Google 产品预构建 agent 技能包，支持通过 \`npx skills add google/skills\` 安装，用户可选择安装特定技能或全量技能，同时可配置目标 agent 与安装范围（项目级/全局）。

**Tags**: `#tools`, `#skills`

---

<a id="item-harness-arch-4"></a>
### [Cloudflare 安全审计技能](https://github.com/cloudflare/security-audit-skill) ⭐️ 5.0/10

Cloudflare open-sourced security-audit-skill, a coding-agent skill that orchestrates isolated subagents through multi-phase security audits. The pipeline includes reconnaissance, coverage-led hunting, candidate validation, structured output, independent record verification, and target-neutral reporting. This skill seeded Cloudflare&\#x27;s production vulnerability discovery harness.

rss · GitHub Trending Daily · Nov 8, 23:00

**「设计要点」** The skill employs isolated subagent orchestration across multiple phases to produce independently verified, machine-readable findings. However, the available documentation offers only high-level functional descriptions without technical implementation details, code paths, or architecture deep dives, making it insufficient for direct harness implementation reference.

**Tags**: `#subagents`, `#sandbox`, `#tools`, `#planning`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [CS146S 调整 Monaco 工具选型](https://latent.space/p/one_million_ai_engineer_special_how_stanford_teaches_ai-native_engineering_mihail_eric_monaco/) ⭐️ 7.0/10

2026-11-08 Latent.Space 发布对 Mihail Eric 的采访。斯坦福 CS146S（The Modern Software Developer）第二期调整作业：学生需向真实开源项目提交 patch，由维护者评审，替代上一期可被 coding agent 一键完成的传统作业。Monaco 的工程实践包括为每个 agent 建独立 workspace、代码评审工具采用购买而非自建、on-call agent 接入 Datadog 与 GitHub，决策原则为 &quot;You buy to learn, and you build to keep&quot;。内容面向 coding agent 工程师、eval 与 harness 开发者。

rss · Latent Space · Nov 8, 21:23

**「为什么重要」** CS146S 的作业调整直接回应 coding agent 能力提升对传统编程训练的冲击，为 eval 设计提供参考。Monaco 的 build-vs-buy 决策与 on-call agent 集成展示了生产环境工具链的具体取舍。

**「可关注」** 可关注：CS146S 用真实开源 patch 评审替代传统作业，提示 coding agent eval 设计需考虑 agent 已能一键完成旧题型的现实。

**Tags**: `#coding-agent`, `#eval`, `#harness`

---

<a id="item-agent-engineer-2"></a>
### [SQLite parse\_number C/Rust 对比](https://simonwillison.net/2026/Nov/8/sqlite-parse-number-c-vs-rust/) ⭐️ 6.0/10

Simon Willison 于 2026-11-08 发布研究，记录使用 Claude Opus 5.5 辅助开发 SQLite parse\_number\(\) 扩展的过程，对比 C 与 Rust 实现的性能与代码体积。C 扩展最终版在混合数据、纯整数、纯小数场景下的单行净成本分别为 19 ns、16 ns、18 ns，低于 rusqlite 的 46 ns/36 ns/55 ns 及 sqlite-loadable-rs 的 41 ns/32 ns/47 ns。C 扩展体积 14 KB，显著小于 Rust 实现的 321 KB 与 298 KB。该研究由 AI 辅助生成，未提及独立复现结果。

rss · Simon Willison · Nov 8, 22:26

**「为什么重要」** 该研究提供了 AI 辅助开发 SQLite 扩展的实证案例，并量化了 C 与 Rust 在文本解析函数上的性能与体积权衡。但主题聚焦于特定数据库函数扩展，对 AI Agent 工程师的核心工作（agent 架构、harness、eval、工具链）影响面较窄。

**「可关注」** 可关注：AI 辅助生成系统级代码时，初始实现的性能未必最优，需通过针对性基准测试与底层函数替换（如优化数字解析逻辑）才能逼近硬件极限。

**Tags**: `#coding-agent`, `#tooling`, `#performance`

---

<a id="item-agent-engineer-3"></a>
### [Kimi-K3.1 三级量化单卡实验](https://www.reddit.com/r/LocalLLaMA/comments/1xr777l/kimik31procoder_28t_177_tb_775_gb_56_368_tps/) ⭐️ 5.5/10

/u/Grawnch 发布 2.8T Kimi-K3.1-Pro-Coder 三级 MoE 专家量化实验，将模型从 1.77 TB 压缩至 775 GB（-56%），在单张 RTX PRO 6000 Blackwell（96 GB VRAM）+ 176 GB RAM + NVMe 上运行。路由专家按 2.81/2.56/1.44 bpw 分三级量化（平均 ~1.92 bpw），共享专家、注意力层保持 BF16/F32；配套 Strata 三级卸载引擎（路由器预取命中率 97.9%）与 dr-triton 融合反量化内核。在 93 层全量 AIME 2025 与 LiveCodeBench 测试中，量化版与原生版均得 29/30（96.7%），但困惑度上升 1–2.7%；批量吞吐 36.8 TPS，单流解码 10.8 TPS。该方案因自定义打包张量布局无法直接用于 llama.cpp 或 vLLM，且为社区实验，结果未经官方复现。

reddit · r/LocalLLaMA · /u/Grawnch · Nov 8, 19:45

**「为什么重要」** 证明超大 MoE 模型可通过分层卸载在单卡硬件上运行并保持编码与数学推理能力，但自定义运行时与硬件门槛限制了可复现性。

**「可关注」** 可关注：MoE 路由专家三级量化配合路由器预取卸载，可在单卡上运行 2.8T 模型，但需自定义加载器且对 PCIe/NVMe 带宽敏感。

**Tags**: `#coding-agent`, `#eval`

---