---
layout: default
title: "Horizon Summary: 2026-11-09 (EN)"
date: 2026-11-09
lang: en
---

> From 150 items, 6 important content pieces were selected

---

**Agent Harness Architecture**
1. [OpenAI Agents SDK v0.24.0-alpha.7 发布](#item-harness-arch-1) ⭐️ 8.8/10
2. [agents-js v0.22.0a2 发布](#item-harness-arch-2) ⭐️ 7.8/10
3. [Cloudflare security-audit-skill 发布](#item-harness-arch-3) ⭐️ 5.5/10

**AI Agent Engineer**
1. [CS146S 课程迭代与 Monaco Agent 实践](#item-agent-engineer-1) ⭐️ 6.0/10
2. [HF 每日论文：Sketchpad 小 VLM 精确算术](#item-agent-engineer-2) ⭐️ 6.0/10
3. [Kimi K3.1 Pro Coder 单卡量化](#item-agent-engineer-3) ⭐️ 6.0/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [OpenAI Agents SDK v0.24.0-alpha.7 发布](https://github.com/openai/openai-agents-python/releases/tag/v0.24.0-alpha.7) ⭐️ 8.8/10

OpenAI Agents SDK v0.24.0-alpha.7 splits runtime execution into classic and native paths via \`agents.classic\`, changes executor write policy defaults to \`strict\`, and introduces durable session storage through \`CustomStorage\` and \`SQLiteSessionStore\`. Hosted tools \(\`FileSearch\`, \`CodeInterpreter\`, \`ImageGeneration\`\) and voice workflows \(\`NativeSessionVoiceWorkflow\`\) are now available for compatible Responses providers, while new hooks for context transformation, completion control, and \`RunBudget\` usage limits add operational control. The release includes breaking changes to MCP approval mode values, \`NativeAgents.before\_step\` signatures, and default reasoning effort for bundled models, requiring migration review before upgrading.

github · markstuart-oai · Nov 8, 07:05

**「设计要点」** Classic and native runtimes now operate as separate import paths with distinct checkpoint and object lifecycles, while executor write policies enforce strict or legacy modes at the environment level. Session state is managed through pluggable storage backends that decouple durable history from model context, and hosted tools integrate via provider-managed APIs requiring API-key authentication.

**「改了什么」** Compared to v0.24.0-alpha.6, the release defaults new Environments to \`write\_policy=&quot;strict&quot;\`, renames MCP approval modes to \`native\`/\`preapproved\`, and changes \`NativeAgents.before\_step\` to accept a single \`ChildStepContext\`. It adds \`CustomStorage\` for durable sessions, hosted tools \(\`FileSearch\`, \`CodeInterpreter\`, \`ImageGeneration\`\), \`RunBudget\` for limiting root request admissions, and \`Environment.local\(\)\` for local executor tool execution.

**Tags**: `#runtime`, `#tools`, `#memory`, `#sandbox`, `#permissions`

---

<a id="item-harness-arch-2"></a>
### [agents-js v0.22.0a2 发布](https://github.com/openai/openai-agents-js/releases/tag/v0.22.0-alpha.2) ⭐️ 7.8/10

openai-agents-js v0.22.0-alpha.2 is a preview release that adds native tools \(fileSearch, codeInterpreter, imageGeneration\) with streaming progress and retained provider results, plus enhanced webSearch with filters and citation details. It introduces run control via maxModelSteps and optional RunBudget limiting work by root requests, observed tokens, and estimated cost. Application-owned SessionStore enables durable conversation recovery with fileSessionStore adapter, while A2A 1.0 support via @openai/agents/a2a provides JSON-RPC polling for remote agent calls. VoicePipeline and NativeSessionVoiceWorkflow enable speech workflows. This preview excludes MCP, manual tools, environments, native children, goals, and portable checkpoints.

github · markstuart-oai · Nov 8, 08:27

**「设计要点」** The native runtime is packaged in @openai/agents-codex while public imports remain at @openai/agents, keeping native and classic agent runtimes separate. New environments default to writePolicy: &\#x27;strict&\#x27;, and the application retains ownership of authorization, durable storage, execution, and reconciliation for both SessionStore and A2A operations.

**「改了什么」** This release adds native streaming tools, exact-step turn steering with StaleTurnError, RunBudget gating, durable application-owned SessionStore with file adapter, A2A 1.0 JSON-RPC adapter, and VoicePipeline. It removes the experimental SDKRunner bridge and migration imports, defaults environments to strict write policy, and introduces prepareRequest sampling control and MCP resource operations.

**Tags**: `#runtime`, `#tools`, `#memory`, `#permissions`, `#a2a`

---

<a id="item-harness-arch-3"></a>
### [Cloudflare security-audit-skill 发布](https://github.com/cloudflare/security-audit-skill) ⭐️ 5.5/10

Cloudflare open-sourced \`security-audit-skill\`, a coding-agent skill that orchestrates isolated subagents through structured security audit phases. The skill guides agents through reconnaissance, coverage-led hunting, candidate validation, structured output, independent record verification, and target-neutral reporting. It previously seeded Cloudflare&\#x27;s vulnerability discovery harness, as described in &quot;Build your own vulnerability harness.&quot; The release provides no implementation details, code paths, or official version numbers.

rss · GitHub Trending Daily · Nov 9, 02:48

**「设计要点」** The skill operates as an orchestration layer within coding agents, spawning isolated subagents per audit phase. It enforces structured output and independent record verification to produce machine-readable findings, though isolation mechanisms remain unspecified.

**「改了什么」** This marks the initial open-source release of the skill that powered Cloudflare&\#x27;s internal vulnerability discovery harness. It introduces a multi-phase audit workflow with isolated subagent orchestration and machine-readable output as a reusable coding-agent skill.

**Tags**: `#subagents`, `#eval`, `#planning`, `#tools`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [CS146S 课程迭代与 Monaco Agent 实践](https://latent.space/p/cs146s/) ⭐️ 6.0/10

Latent Space 发布对斯坦福 CS146S 讲师 Mihail Eric 的访谈，内容涵盖 AI 原生工程课程迭代及 Monaco 的 Agent 实践。CS146S 上一轮九项作业加 Capstone 已被学生用 Agent 一次性完成，本轮改为向开源项目提交补丁并由维护者评审，以训练沟通与影响评估能力。Monaco 购买 Devin 处理代码评审，但自建 Agent 工作区以适配自身云环境，并开发 Hal 系统同时服务工程师排查故障和销售解释产品。访谈引用 Faros 研究称高 AI 采用团队合并 PR 多 98%，评审时间多 91%；同时预测开源仓库将演变为 Agent 运行的软件工厂，但该观点未证实。

rss · Latent Space · Nov 8, 21:41

**「为什么重要」** 学生已普遍用 Agent 完成课程作业，AI 原生工程教育的瓶颈从“生成代码”转向“评审、沟通与历史决策上下文”。对构建 Coding Agent 的工程师而言，Monaco “买来学习、自建留存”的基础设施取舍，以及 Basis Authority Map 对 Agent 记忆机制的讨论，提供了可对照的工业参考。

**「可关注」** Monaco 对代码评审工具和 Agent 工作区采取分离策略：评审环节外购 Devin，运行与测试环境因云架构差异自建。这反映了当前 Agent 基础设施中“通用能力可采购、执行环境需定制”的分层思路。

**Tags**: `#coding-agent`, `#orchestration`, `#eval`, `#harness`

---

<a id="item-agent-engineer-2"></a>
### [HF 每日论文：Sketchpad 小 VLM 精确算术](https://huggingface.co/papers/2611.04434) ⭐️ 6.0/10

2026年11月9日HF每日论文收录Sketchpad预印本，提出一种基于小视觉语言模型的可验证精确算术方法。该方法将模型每步对外部工作内存的读取限制为有界视图，使模型精确性成为有限可检查属性。具体实现为Qwen3.5-0.8B搭载低秩适配器，在渲染作业纸上执行算术流程：每次前向传播读取3格视图，输出一步运算（数字、进位/借位、下一操作），固定运行时仅移动视图、不写入结果数字。研究者用Lean证明，模型在所有长度输入上精确当且仅当在有限视图集合上精确。当前工作仅覆盖算术任务，为预印本且无配套生产工具，对多数agent开发者暂无直接可用的变更。

rss · Hugging Face Daily Papers · Nov 9, 00:00

**「为什么重要」** 该工作提出的「有界外部内存视图让模型精确性可有限检查」原则，对可验证agent推理、内存设计有潜在参考价值；但当前仅验证算术场景，是预印本无生产工具，尚未证实对其他agent工作流的实际影响。

**「可关注」** 可关注：当前可验证精确性的证明仅绑定算术任务，且依赖固定运行时、有限视图读取的约束，若要做agent场景适配需先验证这类约束在通用推理任务中的可迁移性。

**Tags**: `#eval`, `#memory`

---

<a id="item-agent-engineer-3"></a>
### [Kimi K3.1 Pro Coder 单卡量化](https://www.reddit.com/r/LocalLLaMA/comments/1xr777l/kimik31procoder_28t_177_tb_775_gb_56_368_tps/) ⭐️ 6.0/10

Reddit用户/u/Grawnch分享了2.8T参数Kimi-K3.1-Pro-Coder MoE模型的实验性量化与部署方案，该模型每层包含384个路由专家，原生权重约1.77 TB（MXFP4/BF16格式）。方案通过3级路由专家差异化量化（平均1.92 bpw，较原生4.0 bpw压缩超一半）搭配自研Strata三级卸载引擎与dr-triton融合反量化内核，将权重压缩至775 GB，支持单GPU+系统RAM+NVMe运行。该方案在1x RTX PRO 6000 Blackwell（96 GB VRAM）+176 GB RAM的Colab环境下测得批处理吞吐36.8 TPS、单流解码10.8 TPS，自报告AIME 2025与LiveCodeBench准确率均为96.67%，与原生1.77 TB版本表现一致，但该数据为自报告结果，方案未获官方验证，属于实验性实现，且压缩后权重采用自定义打包张量布局，无法直接接入llama.cpp、vLLM等现有推理框架。

reddit · r/LocalLLaMA · /u/Grawnch · Nov 8, 19:45

**「为什么重要」** 若该实验数据可复现，这是目前公开的首个将2.8T级MoE模型压缩至单卡可运行范围且保持coding/math推理性能的实验方案，为本地部署超大参数coding专用MoE模型提供了可参考的技术路径，但目前尚未有第三方验证结果。

**「可关注」** 可关注：该方案采用的路由专家差异化量化+路由器预取三级卸载的技术路径，为超大MoE模型的轻量化部署提供了实验参考，但当前权重采用自定义打包张量布局，无法直接接入llama.cpp、vLLM等现有通用推理框架。

**Tags**: `#eval`, `#coding-agent`, `#model-quantization`

---