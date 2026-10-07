---
layout: default
title: "Horizon Summary: 2026-10-07 (EN)"
date: 2026-10-07
lang: en
---

> From 216 items, 21 important content pieces were selected

---

**Agent Harness Architecture**
1. [anthropics/claude-code released v2.1.292](#item-harness-arch-1) ⭐️ 8.3/10
2. [Claude Code v2.1.290 发布](#item-harness-arch-2) ⭐️ 7.3/10
3. [All-Hands-AI/OpenHands released v1.25.0](#item-harness-arch-3) ⭐️ 6.3/10
4. [Gemini CLI v0.64.0-preview.0 Released](#item-harness-arch-4) ⭐️ 5.8/10
5. [google-gemini/gemini-cli released v0.63.0](#item-harness-arch-5) ⭐️ 5.3/10
6. [microsoft/semantic-kernel released python-1.45.0](#item-harness-arch-6) ⭐️ 5.3/10
7. [Semantic Kernel 1.81.0 发布](#item-harness-arch-7) ⭐️ 5.3/10

**AI Agent Engineer**
1. [EmbeddingGemma 2 发布](#item-agent-engineer-1) ⭐️ 7.8/10
2. [EmbeddingGemma 2: An open, lightweight multimodal embedding model](#item-agent-engineer-2) ⭐️ 7.5/10
3. [OSWorld-Pro：过程化评测计算机操作智能体](#item-agent-engineer-3) ⭐️ 7.5/10
4. [HF daily paper: Self-Generated Feedback Destabilizes Test-Time Training: A Causal Decomposition of Long-Horizon Adaptation](#item-agent-engineer-4) ⭐️ 7.0/10
5. [MemAdapter 提出反事实记忆适配框架](#item-agent-engineer-5) ⭐️ 6.5/10
6. [simonw released 0.16 in simonw/llm-mistral](#item-agent-engineer-6) ⭐️ 6.3/10
7. [I gave a 21M model a 6.4B-parameter lookup table. It matches a 114M dense model and runs with the table on an SSD \(RX 9070\)](#item-agent-engineer-7) ⭐️ 6.0/10

**AI Daily**
1. [OpenAI 公布数学开放问题新结果](#item-ai-daily-1) ⭐️ 10.0/10
2. [EmbeddingGemma 2 端侧嵌入](#item-ai-daily-2) ⭐️ 9.3/10
3. [Anthropic CVP 扩展至三档访问](#item-ai-daily-3) ⭐️ 8.8/10
4. [Advancing computer use with Ironclad](#item-ai-daily-4) ⭐️ 8.3/10
5. [GitHub 重建 Git 基础设施](#item-ai-daily-5) ⭐️ 8.3/10
6. [Atlassian 扩展 OpenAI 合作](#item-ai-daily-6) ⭐️ 7.8/10
7. [Jump Trading 用 ChatGPT 扩展量化研究](#item-ai-daily-7) ⭐️ 6.3/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [anthropics/claude-code released v2.1.292](https://github.com/anthropics/claude-code/releases/tag/v2.1.292) ⭐️ 8.3/10

Claude Code v2.1.292 ships subagent effort controls, plugin marketplace integration, mod-hook extensibility, prompt caching, and a permissions fix.

github · ashwin-ant · Oct 6, 18:59

**Tags**: `#subagents`, `#tools`, `#permissions`, `#prefix-cache`, `#runtime`

---

<a id="item-harness-arch-2"></a>
### [Claude Code v2.1.290 发布](https://github.com/anthropics/claude-code/releases/tag/v2.1.290) ⭐️ 7.3/10

Claude Code v2.1.290 发布，聚焦插件钩子与子代理权限流。\`turn.step\` 钩子结果新增 \`serverToolUses\`，记录 API 自行执行的工具调用及其 id、name、input 与起止时间。\`tool.check\` 事件新增 \`agentId\`，使钩子可区分子代理与主会话的权限检查；同时新增 \`ceiling\`，标明组织对工具的审批上限。CLI 与网关同步更新：\`claude attach &lt;name&gt;\` 和 \`claude logs &lt;name&gt;\` 接受会话名片段，网关登录审批页加入 Deny 按钮。

github · ashwin-ant · Oct 5, 23:33

**「设计要点」** 插件钩子层通过 \`agentId\` 与 \`ceiling\` 直接读取子代理权限检查和组织审批上限，配合 \`serverToolUses\` 将 API 侧工具调用纳入 \`turn.step\` 观测，权限判定与执行轨迹在 mod 层打通。

**「改了什么」** 相对前版，插件钩子获得子代理权限上下文（\`agentId\`、\`ceiling\`）与 API 工具调用明细（\`serverToolUses\`），\`claude plugin validate\` 可列出 gating 钩子的 \`.catch\` 状态；CLI 加入会话名片段匹配与 Managed Agents 快速入门，网关登录审批支持显式拒绝。

**Tags**: `#runtime`, `#tools`, `#permissions`, `#subagents`

---

<a id="item-harness-arch-3"></a>
### [All-Hands-AI/OpenHands released v1.25.0](https://github.com/OpenHands/OpenHands/releases/tag/v1.25.0) ⭐️ 6.3/10

OpenHands v1.25.0 adds Model Router configuration toggles, bulk LLM profile management, and refactors canvas streaming to use event-id-based slots.

github · openhands-release-bot\[bot\] · Oct 6, 00:56

**Tags**: `#runtime`, `#tools`, `#planning`

---

<a id="item-harness-arch-4"></a>
### [Gemini CLI v0.64.0-preview.0 Released](https://github.com/google-gemini/gemini-cli/releases/tag/v0.64.0-preview.0) ⭐️ 5.8/10

Gemini CLI v0.64.0-preview.0 ships incremental fixes for A2A settings migration, ACP usage notifications, headless trust propagation, CLI parsing, and atomic file tool writes. The A2A server implements V1-to-V2 settings migration. ACP bridges PromptResponse.usage and emits usage\_update notifications. Core file tools serialize operations and make writes atomic. ChatRecordingService adopts append-only delta patching with bounded history windowing. CLI state persists atomically and recovers from backup on corruption.

github · gemini-cli-robot · Oct 6, 20:26

**「设计要点」** The A2A server migrates V1 settings to V2 at runtime. ACP resolves sessions by exact ID and cleans up listeners on failure. File tool writes are serialized and atomic to avoid partial state. ChatRecordingService uses append-only deltas and a bounded window to cap memory. Headless mode propagates resolved folder trust to child processes.

**「改了什么」** A2A settings migration moves from V1 to V2. ACP emits usage\_update notifications from PromptResponse.usage. Headless mode propagates resolved folder trust. File tool operations are serialized and writes are atomic. ChatRecordingService switches to append-only delta patching with bounded history. CLI state persists atomically and recovers from backup on corruption. Ctrl+C aborts reach cancellation handlers during active operations. @file:line references resolve and ghost text wrap hangs are prevented. Windows ConPTY forwards IME cursor position. Windows extension updates retry directory removal on locking errors. ACP resolves sessions by exact ID. Scroll position is preserved and pending height budget partitioned. Enter and Spacebar reliably confirm selection list options.

**Tags**: `#runtime`, `#tools`, `#permissions`

---

<a id="item-harness-arch-5"></a>
### [google-gemini/gemini-cli released v0.63.0](https://github.com/google-gemini/gemini-cli/releases/tag/v0.63.0) ⭐️ 5.3/10

Gemini CLI v0.63.0 is a patch release that fixes CLI retry indicators, MCP config error distinction, stdin restoration, and core memory lifecycle in long-running agent loops.

github · gemini-cli-robot · Oct 6, 20:38

**Tags**: `#runtime`, `#memory`, `#tools`, `#mcp`

---

<a id="item-harness-arch-6"></a>
### [microsoft/semantic-kernel released python-1.45.0](https://github.com/microsoft/semantic-kernel/releases/tag/python-1.45.0) ⭐️ 5.3/10

Semantic Kernel 1.45.0 is a routine maintenance release with minor breaking changes and dependency updates, lacking architectural significance for agent harness engineers.

github · eavanvalkenburg · Oct 6, 12:54

**Tags**: `#runtime`, `#permissions`, `#tools`

---

<a id="item-harness-arch-7"></a>
### [Semantic Kernel 1.81.0 发布](https://github.com/microsoft/semantic-kernel/releases/tag/dotnet-1.81.0) ⭐️ 5.3/10

Microsoft released Semantic Kernel .NET 1.81.0, a routine patch that bumps the package version and applies minor maintenance across tools, memory, and validation. Updates include FileIOPlugin file handling, Milvus filtering, plugin path validation, and a SessionsPythonPlugin bug fix. The release also temporarily skips direct OpenAI integration tests and upgrades a Git build dependency. No breaking or architectural changes are introduced.

github · dmytrostruk · Oct 6, 16:34

**「改了什么」** FileIOPlugin file handling is updated, Milvus filtering is improved, and plugin path validation is aligned. A SessionsPythonPlugin bug is fixed, direct OpenAI integration tests are temporarily skipped, and the Git build dependency is upgraded.

**Tags**: `#tools`, `#memory`, `#permissions`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [EmbeddingGemma 2 发布](https://deepmind.google/blog/embeddinggemma-2-an-open-lightweight-multimodal-embedding-model/) ⭐️ 7.8/10

Google DeepMind 于 2026-10-06 发布 EmbeddingGemma 2，一款开放、轻量的多模态嵌入模型。现有材料未披露参数量、基准数据与部署限制。标签指向 memory 与 harness，提示其可能服务于 agent 检索与记忆场景。

rss · Google DeepMind · Oct 6, 19:57

**「为什么重要」** 做 coding agent 与 harness 的工程师今天多了一个开放嵌入组件可选。已发生的变化是模型发布；对现有检索与记忆架构的实际影响尚未证实。

**「可关注」** EmbeddingGemma 2 的开放性与轻量定位，或为本地及多模态检索提供新选项；但在缺乏基准与限制说明前，替换现有嵌入层需谨慎评估。

**Tags**: `#memory`, `#harness`

---

<a id="item-agent-engineer-2"></a>
### [EmbeddingGemma 2: An open, lightweight multimodal embedding model](https://blog.google/innovation-and-ai/technology/developers-tools/embeddinggemma-2/) ⭐️ 7.5/10

Google releases EmbeddingGemma 2, an open-source lightweight multimodal embedding model under Apache 2.0, providing a new option for agent memory and retrieval tooling.

hackernews · ilreb · Oct 6, 16:03 · [Discussion](https://news.ycombinator.com/item?id=49980487)

**Tags**: `#memory`, `#multimodal`, `#open-source`, `#rag`

---

<a id="item-agent-engineer-3"></a>
### [OSWorld-Pro：过程化评测计算机操作智能体](https://huggingface.co/papers/2609.24890) ⭐️ 7.5/10

2026 年 10 月 6 日，Hugging Face Daily Papers 收录论文 OSWorld-Pro。该基准包含 300 余项任务、2800 余个子目标，基于 67000 余条人工标注，用与人类对齐的 LLM 评判子目标完成度。论文对比 OSWorld 的端到端功能验证，指出后者无法解释智能体在键盘输入、图形界面点击等环节的失败原因，过程化拆解可暴露不同修复路径。

rss · Hugging Face Daily Papers · Oct 6, 00:00

**「为什么重要」** 计算机操作智能体的失败常发生在中间步骤，只看最终交付物会掩盖关键诊断信息。OSWorld-Pro 把评测粒度压到子目标，让工程师能区分输入方式错误与任务规划错误，直接影响后续修复策略。

**「可关注」** OSWorld-Pro 将 CUAs 评测拆到 2800 余个子目标，用 67000 余条人工标注对齐 LLM 评判，使键盘输入错误与图形界面点击错误可被区分，对应不同修复路径。

**Tags**: `#eval`, `#coding-agent`, `#observability`

---

<a id="item-agent-engineer-4"></a>
### [HF daily paper: Self-Generated Feedback Destabilizes Test-Time Training: A Causal Decomposition of Long-Horizon Adaptation](https://huggingface.co/papers/2610.05076) ⭐️ 7.0/10

A causal decomposition paper demonstrates that test-time training on self-generated text destabilizes long-horizon adaptation, and that using a frozen model to generate training chunks removes over 98% of the damage.

rss · Hugging Face Daily Papers · Oct 6, 00:00

**Tags**: `#memory`, `#eval`, `#harness`

---

<a id="item-agent-engineer-5"></a>
### [MemAdapter 提出反事实记忆适配框架](https://huggingface.co/papers/2610.05162) ⭐️ 6.5/10

2026-10-06，Hugging Face Daily Papers 收录论文 MemAdapter，提出反事实适配框架，用于缓解 LLM 智能体中的记忆诱发谄媚。论文指出，长期记忆虽支持个性化和长程交互，但即使客观、正确的记忆也可能导致智能体过度迎合用户历史信念。现有缓解方法多通过过滤有偏或错误记忆来降低风险，而该框架主张同一记忆在不同上下文应具有不同影响力。摘要未展示完整实验结果与代码可用性，论文页获 26 次 upvote。

rss · Hugging Face Daily Papers · Oct 6, 00:00

**「为什么重要」** 对做 coding agent 与 harness 的工程师而言，该文把记忆治理从‘筛掉坏记忆’推向‘按上下文调节记忆影响’，直接触及智能体记忆架构与评估设计。不过，其实际效果尚未经完整实验验证。

**「可关注」** 可关注：同一记忆在不同上下文需要差异化影响，而非简单过滤。

**Tags**: `#memory`, `#eval`, `#coding-agent`, `#harness`

---

<a id="item-agent-engineer-6"></a>
### [simonw released 0.16 in simonw/llm-mistral](https://github.com/simonw/llm-mistral/releases/tag/0.16) ⭐️ 6.3/10

llm-mistral v0.16 adds Mistral reasoning model support, a breaking safe\_prompt option change, and local MP3 attachments for Voxtral.

github · simonw · Oct 6, 21:32

**Tags**: `#harness`, `#tooling`, `#llm`

---

<a id="item-agent-engineer-7"></a>
### [I gave a 21M model a 6.4B-parameter lookup table. It matches a 114M dense model and runs with the table on an SSD \(RX 9070\)](https://www.reddit.com/r/LocalLLaMA/comments/1wz7tvs/i_gave_a_21m_model_a_64bparameter_lookup_table_it/) ⭐️ 6.0/10

A hobbyist shows that a 21M model with a 6.4B-parameter SSD-resident lookup table can match a 114M dense model, with Triton kernels enabling execution across Radeon, MI350X, and H100/H200.

reddit · r/LocalLLaMA · /u/fechyyy · Oct 6, 16:57

**Tags**: `#memory`, `#inference`, `#toolchain`

---

## AI Daily

<a id="item-ai-daily-1"></a>
### [OpenAI 公布数学开放问题新结果](https://openai.com/index/sharing-ai-progress-in-mathematics) ⭐️ 10.0/10

OpenAI 公布内部前沿模型在数学开放问题上的新结果，并在 GitHub 公开 Lean 证明形式化与研究细节。官方未披露具体模型版本、问题清单或量化指标，结果范围待外部验证。

rss · OpenAI Blog · Oct 6, 12:00

**「可关注」** 可关注：OpenAI 在 GitHub 公开了 Lean 证明形式化与研究细节，可直接查阅。

**Tags**: `#model`, `#lab`, `#eval`, `#open-source`

---

<a id="item-ai-daily-2"></a>
### [EmbeddingGemma 2 端侧嵌入](https://developers.googleblog.com/embeddinggemma-2-the-developer-guide/) ⭐️ 9.3/10

Google Developers 博客发布 EmbeddingGemma 2，基于 Gemma 4 的 sub-1B 开源多模态嵌入模型，采用 Apache 2.0 许可，将文本、代码、图像、视频和音频映射到统一的 768 维向量空间。模块化架构支持 270M 到 740M 参数按需加载，兼容 sentence-transformers v6.1.0 及以上版本，可在加载时禁用未使用的模态编码器以降低内存。官方称其在 MTEB \(Code\) 上较 EmbeddingGemma 1 提升 14%，同时保留多语言文本能力；在 Pixel 11 Pro 上，纯文本权重约 191MB 活跃内存，全模态约 567MB。模型共享 8192 token 上下文，向量可截断至 512/256/128 维，百万条 768 维向量在 bfloat16 下约 1.5GB，截断到 128 维仅需 250MB。

rss · Google Developers AI · Oct 6, 00:00

**「为什么重要」** 对构建本地搜索与 RAG 的工程师，EmbeddingGemma 2 用单一模型替代图像描述、语音转文本加文本嵌入的链式方案，直接跨模态计算语义相似度。它无需训练数据即可做零样本意图路由，并可在端侧运行，适合隐私优先的场景。

**「可关注」** 可关注：所有编码器配置共用同一 checkpoint 与向量空间，纯文本索引可直接匹配全模态文档；后续新增图像或音频时，只需重载模型并启用对应编码器，已有向量无需重算。

**Tags**: `#model`, `#lab`, `#open-source`, `#product`

---

<a id="item-ai-daily-3"></a>
### [Anthropic CVP 扩展至三档访问](https://www.anthropic.com/news/cyber-verification-program) ⭐️ 8.8/10

Anthropic 将 Cyber Verification Program（CVP）扩展为 Defense Access、Red Team Access、Specialized Access 三档，安全团队可按工作范围申请，使用 Claude Opus 5.5、Claude Sonnet 5.5、Claude Mythos 5.1 等模型并降低网络防护拦截。Project Glasswing 并入该计划，现有成员直接转入 Specialized Access。项目要求数据留存，Enterprise Frontier Safeguards（EFS）今秋推出后支持零数据留存。

rss · Anthropic News · Oct 6, 00:00

**「为什么重要」** CVP 把前沿模型的网络能力与组织资质绑定，向专业防御者开放。CyScenarioBench 测试显示，无 CVP 权限时所有任务在首次提示即被拦截；Defense Access 下 50 次试验有 46 次被拦截；Red Team Access 下无拦截，Claude Opus 5.5 完成 34/50 任务，与无防护时的 67.6% 成功率相当。

**「可关注」** 可关注：当前 CVP 强制数据留存以监控滥用；Enterprise Frontier Safeguards（EFS）今秋推出后，符合资质的组织可在自主控制的云基础设施中零数据留存。

**Tags**: `#lab`, `#policy`, `#product`, `#model`

---

<a id="item-ai-daily-4"></a>
### [Advancing computer use with Ironclad](https://openai.com/index/advancing-computer-use-with-ironclad) ⭐️ 8.3/10

OpenAI and Ironclad are training and evaluating AI agents on complex contracting workflows to advance computer use for professional work.

rss · OpenAI Blog · Oct 6, 10:00

**Tags**: `#model`, `#lab`, `#product`, `#eval`, `#industry`

---

<a id="item-ai-daily-5"></a>
### [GitHub 重建 Git 基础设施](https://github.blog/engineering/architecture-optimization/building-git-infrastructure-for-agent-scale-development/) ⭐️ 8.3/10

GitHub 工程博客宣布，将在保持服务运行的同时重建 Git 基础设施，为智能体规模的软件开发打下基础。文章作者 Brian Celenza 指出，这次重构面向 agent-scale development，但未公布具体技术路线、时间表或性能指标。目前仅确认底层替换会与线上服务并行推进，更多细节尚未披露。

rss · GitHub Blog · Oct 6, 20:57

**「为什么重要」** Git 是 GitHub 代码托管与协作的核心底层，这次重建决定了平台未来承载智能体高并发开发的能力上限。

**「可关注」** 可关注：GitHub 如何做到在不中断服务的前提下替换 Git 基础设施，其在线升级思路对同类大规模系统具有参考价值。

**Tags**: `#industry`, `#product`, `#lab`

---

<a id="item-ai-daily-6"></a>
### [Atlassian 扩展 OpenAI 合作](https://openai.com/index/atlassian-partnership) ⭐️ 7.8/10

OpenAI 与 Atlassian 宣布扩大合作，将前沿模型与企业知识连接，帮助团队规划、构建和交付工作。官方未披露具体集成形式、上线时间或覆盖的产品范围。目前信息仅来自 OpenAI 单方公告，缺少独立细节。

rss · OpenAI Blog · Oct 6, 16:00

**「为什么重要」** Atlassian 承载大量企业项目与知识数据，OpenAI 提供前沿模型，两者扩大合作意味着企业工作流可能更深度接入 AI 规划与交付能力。目前公告未给出技术细节，实际效果待观察。

**「可关注」** 可关注：Atlassian 与 OpenAI 将如何把企业知识接入前沿模型，以及哪些工作流会优先落地。

**Tags**: `#industry`, `#product`, `#lab`

---

<a id="item-ai-daily-7"></a>
### [Jump Trading 用 ChatGPT 扩展量化研究](https://openai.com/index/jump-trading) ⭐️ 6.3/10

OpenAI 官方博客发布 Jump Trading 客户案例。案例称其用量化研究工作流结合多数据源与人工审核，扩展研究能力。该内容为企业采用案例，非模型发布或政策变化。

rss · OpenAI Blog · Oct 6, 12:00

**「为什么重要」** 对 coding agent / harness 从业者而言，这展示了长时运行 AI 工作流在专业研究场景的落地形态。案例强调多数据源整合与人工审核环节，而非全自动决策。

**「可关注」** 可关注：OpenAI 官方博客描述的长时运行 AI 工作流，将多数据源与人工审核结合用于量化研究。

**Tags**: `#model`, `#product`, `#industry`, `#lab`

---