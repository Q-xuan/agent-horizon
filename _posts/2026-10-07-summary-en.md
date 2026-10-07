---
layout: default
title: "Horizon Summary: 2026-10-07 (EN)"
date: 2026-10-07
lang: en
---

> From 186 items, 23 important content pieces were selected

---

**Agent Harness Architecture**
1. [Claude Code v2.1.292 发布](#item-harness-arch-1) ⭐️ 8.3/10
2. [Gemini CLI v0.64.0-preview.0 Hardens Protocols and File Tools](#item-harness-arch-2) ⭐️ 7.8/10
3. [Claude Code v2.1.291 Fixes Session and Permission Regressions](#item-harness-arch-3) ⭐️ 6.8/10
4. [gemini-cli v0.65.0-nightly.20261007.gef59c532f Released](#item-harness-arch-4) ⭐️ 6.3/10
5. [Gemini CLI v0.63.0 Released](#item-harness-arch-5) ⭐️ 6.3/10
6. [microsoft/semantic-kernel released python-1.45.0](#item-harness-arch-6) ⭐️ 6.3/10
7. [microsoft/semantic-kernel released dotnet-1.81.0](#item-harness-arch-7) ⭐️ 6.3/10

**AI Agent Engineer**
1. [自生成反馈破坏测试时训练稳定性](#item-agent-engineer-1) ⭐️ 8.0/10
2. [Decisions API 进入公测](#item-agent-engineer-2) ⭐️ 7.5/10
3. [Introducing Mistral Large 4: Le chonk](#item-agent-engineer-3) ⭐️ 7.5/10
4. [HF daily paper: Harness Engineering for Software Engineering via Modular Executable Dev-Primitives](#item-agent-engineer-4) ⭐️ 7.5/10
5. [OSWorld-Pro 引入子目标过程评估](#item-agent-engineer-5) ⭐️ 7.5/10
6. [EmbeddingGemma 2: An open, lightweight multimodal embedding model](#item-agent-engineer-6) ⭐️ 7.0/10
7. [llm-mistral 0.16 发布](#item-agent-engineer-7) ⭐️ 6.8/10
8. [LMBuild 评估可建造 3D 结构](#item-agent-engineer-8) ⭐️ 6.0/10
9. [EmbeddingGemma 2 开源：740M 多模态嵌入](#item-agent-engineer-9) ⭐️ 6.0/10
10. [I gave a 21M model a 6.4B-parameter lookup table. It matches a 114M dense model and runs with the table on an SSD \(RX 9070\)](#item-agent-engineer-10) ⭐️ 5.5/10

**AI Daily**
1. [OpenAI 发布数学开放问题新结果](#item-ai-daily-1) ⭐️ 10.0/10
2. [OpenAI 与 Ironclad 训练合同智能体](#item-ai-daily-2) ⭐️ 8.3/10
3. [Building Git infrastructure for agent-scale development](#item-ai-daily-3) ⭐️ 7.8/10
4. [Jump Trading 用 ChatGPT 扩展研究](#item-ai-daily-4) ⭐️ 6.8/10
5. [OpenAI 扩展 Atlassian 合作](#item-ai-daily-5) ⭐️ 6.8/10
6. [Meta NTS 认证时间服务上线](#item-ai-daily-6) ⭐️ 6.8/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [Claude Code v2.1.292 发布](https://github.com/anthropics/claude-code/releases/tag/v2.1.292) ⭐️ 8.3/10

Claude Code v2.1.292 发布。\`claude plugin install\` 新增 \`--marketplace &lt;source&gt;\`，先按 \`claude plugin marketplace add\` 的策略检查添加市场，再安装插件。Agent 工具加入 \`effort\` 参数，可指定子代理运行力度。Mod 侧新增 \`prompt.autocomplete\` 事件，\`$.model.complete\` 支持 prompt caching，\`agent.spawn\` 可拦截 workflow agents。另修复沙箱、UNC 路径读取、auto mode 误入等安全问题。

github · ashwin-ant · Oct 6, 18:59

**「设计要点」** Runtime 扩展 mod hook 事件与模型调用缓存；工具层通过 \`effort\` 细分 subagent 档位；权限侧收紧沙箱与网络路径读取，并阻止 auto mode 在不可用时启用。

**「改了什么」** 插件安装支持指定 marketplace 并复用策略检查；mod 获得 autocomplete 与 prompt caching；subagent 支持 effort 控制；529 重试基础延迟可经 \`CLAUDE\_CODE\_OVERLOADED\_RETRY\_BASE\_DELAY\_MS\` 配置。

**Tags**: `#runtime`, `#tools`, `#subagents`, `#permissions`, `#prefix-cache`

---

<a id="item-harness-arch-2"></a>
### [Gemini CLI v0.64.0-preview.0 Hardens Protocols and File Tools](https://github.com/google-gemini/gemini-cli/releases/tag/v0.64.0-preview.0) ⭐️ 7.8/10

google-gemini/gemini-cli v0.64.0-preview.0 ships a2a and acp protocol fixes, headless trust propagation, and atomic file-tool serialization. The a2a-server implements V1 to V2 settings migration. The acp layer bridges PromptResponse.usage and emits usage\_update notifications. Headless mode now propagates resolved folder trust state.

github · gemini-cli-robot · Oct 6, 20:26

**「Architecture Note」** Core file tools serialize operations and make writes atomic, preventing concurrent write races. ChatRecordingService adopts append-only delta patching with a bounded history window. CLI state persists atomically and recovers from backup on corruption.

**「What Changed」** Against v0.63.0-preview.0, the release adds a2a V1→V2 settings migration, acp usage bridging, and headless folder trust propagation. It also fixes a CPU hang on @ within code and ensures Ctrl+C emergency aborts reach cancellation handlers during active operations.

**Tags**: `#runtime`, `#tools`, `#permissions`

---

<a id="item-harness-arch-3"></a>
### [Claude Code v2.1.291 Fixes Session and Permission Regressions](https://github.com/anthropics/claude-code/releases/tag/v2.1.291) ⭐️ 6.8/10

anthropics/claude-code released v2.1.291 as a patch. It fixes two regressions: cloud sessions dropping answers to permission prompts introduced in v2.1.290, and loss of the last session messages on quit introduced in v2.1.288. The release contains no new capabilities or architectural changes.

github · ashwin-ant · Oct 6, 03:55

**「Design Notes」** The fixes target the permission-prompt round trip in cloud sessions and the session persistence path during shutdown. Both are runtime and memory concerns rather than tool-layer or evaluation changes.

**「What Changed」** Cloud sessions no longer drop answers to permission prompts. The final messages of a session are preserved when quitting.

**Tags**: `#permissions`, `#runtime`, `#memory`

---

<a id="item-harness-arch-4"></a>
### [gemini-cli v0.65.0-nightly.20261007.gef59c532f Released](https://github.com/google-gemini/gemini-cli/releases/tag/v0.65.0-nightly.20261007.gef59c532f) ⭐️ 6.3/10

Google shipped gemini-cli v0.65.0-nightly.20261007.gef59c532f. This nightly hardens security and fixes session resume. It enforces read-only workspace settings in untrusted folders. It also prevents duplicate tool-response turns when resuming sessions and stops deletion of resumed session history on quick exit. OAuth callback issuer validation now aligns with RFC 9207. Expanding output with Ctrl+O no longer triggers unnecessary terminal clears.

github · gemini-cli-robot · Oct 7, 01:31

**「Design Points」** The CLI layer enforces read-only workspace settings when the current folder is untrusted, tightening sandbox permissions. Core session-resume logic avoids duplicate tool responses and preserves history on abrupt exits.

**「What Changed」** The release enforces read-only workspaces in untrusted folders, fixes duplicate tool responses and history deletion during session resume, aligns OAuth issuer validation with RFC 9207, and prevents terminal scroll resets on Ctrl+O expansion.

**Tags**: `#runtime`, `#permissions`, `#sandbox`, `#tools`

---

<a id="item-harness-arch-5"></a>
### [Gemini CLI v0.63.0 Released](https://github.com/google-gemini/gemini-cli/releases/tag/v0.63.0) ⭐️ 6.3/10

Gemini CLI v0.63.0 is a patch release that hardens long-running agent loops by bounding tool output size and optimizing memory lifecycle. It fixes MCP configuration error handling, authentication loops, stdin restoration, and non-interactive plan execution. The release contains no breaking changes or new architectural capabilities.

github · gemini-cli-robot · Oct 6, 20:38

**「Architecture Note」** The core agent loop now enforces bounds on tool output size and optimizes memory lifecycle to sustain long-running sessions. MCP configuration handling distinguishes missing enablement from malformed JSON, and ACP sessions resolve before config initialization to avoid same-minute filename collisions.

**「What Changed」** The release bounds tool output size and optimizes memory lifecycle in long-running agent loops, while disabling truncation when maxChars &lt;= 0. It also fixes MCP config error distinction, prevents infinite auth loops, restores paused stdin, and enables autonomous plan execution in non-interactive mode.

**Tags**: `#runtime`, `#memory`, `#tools`, `#mcp`

---

<a id="item-harness-arch-6"></a>
### [microsoft/semantic-kernel released python-1.45.0](https://github.com/microsoft/semantic-kernel/releases/tag/python-1.45.0) ⭐️ 6.3/10

Semantic Kernel 1.45.0 is a routine maintenance release with minor breaking changes and dependency updates, lacking significant architectural innovations.

github · eavanvalkenburg · Oct 6, 12:54

**Tags**: `#runtime`, `#tools`, `#permissions`

---

<a id="item-harness-arch-7"></a>
### [microsoft/semantic-kernel released dotnet-1.81.0](https://github.com/microsoft/semantic-kernel/releases/tag/dotnet-1.81.0) ⭐️ 6.3/10

Semantic Kernel .NET 1.81.0 is a routine minor release with incremental plugin, file handling, and vector store filtering improvements.

github · dmytrostruk · Oct 6, 16:34

**Tags**: `#runtime`, `#tools`, `#permissions`, `#memory`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [自生成反馈破坏测试时训练稳定性](https://huggingface.co/papers/2610.05076) ⭐️ 8.0/10

2026 年 10 月 7 日的论文显示，测试时训练（TTT）在推理阶段把信息写入权重；当模型从自身输出学习时，每次更新都会改变生成下一条训练样本的模型。研究者在 128K token 流上发现，保留生成文本的更新会损害对人类独立文本的预测，覆盖 125M、760M、3B 三个 TTT-E2E 配置，用 Adam 更新 Qwen3-4B 现有权重也复现同样失败。相同更新机制在真实文本上能带来提升，说明“写”本身不是问题。三项匹配对比显示，Fixed Generation 用冻结模型生成训练块，在 125M 和 760M 上消除超过 98% 的损害。

rss · Hugging Face Daily Papers · Oct 7, 01:58

**「为什么重要」** 对做 coding agent 和长程记忆的人来说，这解释了自改进循环为何会在长上下文里退化。论文给出可量化的因果拆解和缓解基线，但尚未验证这些结论在更大规模或真实 agent 场景中的普适性。

**「可关注」** 可关注：长程测试时训练中，用冻结模型生成训练块可消除超过 98% 的自生成反馈损害。

**Tags**: `#memory`, `#eval`, `#harness`, `#observability`

---

<a id="item-agent-engineer-2"></a>
### [Decisions API 进入公测](https://developers.openai.com/api/docs/guides/decisions) ⭐️ 7.5/10

OpenAI 官方文档宣布 Decisions API 进入 public beta，面向 agent 决策场景提供快速的是/否/置信度评分。社区已出现基于 OpenRouter 的实测，对比 Jev、Mercury Decide 等模型，累计调用少于 600 次，覆盖 UI 组件选择、聊天图表、标签筛选、PKM 等任务。开发者给出的初步结论是：与 responses API 相比，decisions 速度快约 10 倍，成本持平（每 1M tokens 0.10 美元），质量与 luna 相当。

hackernews · chiefstorm · Oct 6, 20:57 · [Discussion](https://news.ycombinator.com/item?id=49984025)

**「为什么重要」** 对 coding agent 与 harness 构建者而言，决策分类是编排链路里的高频操作。decisions 把这类调用从通用 responses API 中拆出，以约 10 倍速度差和持平成本提供了替代路径。若该延迟优势在自有任务上复现，agent 的决策节点吞吐将直接受益。

**「可关注」** 可关注：在 agent harness 中，将高频、轻量的决策分类从 responses API 迁移到 decisions 端点，可能用持平成本换取约 10 倍延迟优势；但实测样本尚少（少于 600 次调用），且质量对比仅基于 luna 等个别模型，接入前需按自身任务复测。

**「评论」** 评论显示，decisions 的核心优势被定位在速度而非成本或质量：ashu1461 给出量化对比，称其比 responses API 快约 10 倍，成本持平（每 1M tokens 0.10 美元），质量与 luna 相当；Topfi 则通过 OpenRouter 对 Jev、Mercury Decide 做了少于 600 次调用的初步实测，覆盖 UI 组件选择、标签筛选等场景，但强调结论仍属初步。

**Tags**: `#eval`, `#harness`, `#orchestration`, `#coding-agent`

---

<a id="item-agent-engineer-3"></a>
### [Introducing Mistral Large 4: Le chonk](https://simonwillison.net/2026/Oct/6/le-chonk/) ⭐️ 7.5/10

Mistral Large 4 preview released: 1T parameter / 49B active model with only &\#x27;none&\#x27; and &\#x27;high&\#x27; reasoning levels, open weights promised by end of month.

rss · Simon Willison · Oct 6, 20:18

**Tags**: `#coding-agent`, `#eval`, `#harness`, `#observability`

---

<a id="item-agent-engineer-4"></a>
### [HF daily paper: Harness Engineering for Software Engineering via Modular Executable Dev-Primitives](https://huggingface.co/papers/2610.07832) ⭐️ 7.5/10

该论文提出 Dev-Primitives，一种将仓库组件转化为可执行抽象以缓解长程软件工程任务中上下文爆炸和语义漂移的模块化方案。

rss · Hugging Face Daily Papers · Oct 7, 00:00

**Tags**: `#coding-agent`, `#harness`, `#memory`, `#orchestration`

---

<a id="item-agent-engineer-5"></a>
### [OSWorld-Pro 引入子目标过程评估](https://huggingface.co/papers/2609.24890) ⭐️ 7.5/10

OSWorld-Pro 推出过程化评估基准，面向 Computer-Use Agents。基准含 300+ 任务、2800+ 子目标，基于 67,000+ 人工标注。采用与人类对齐的 LLM-Judges 评估子目标完成度，替代 OSWorld 只看最终交付物的功能验证。键盘输入错误与点击错误可被区分，指向不同修复策略。

rss · Hugging Face Daily Papers · Oct 7, 01:58

**「为什么重要」** OSWorld 的端到端功能验证无法解释 Agent 在数百步中如何失败。OSWorld-Pro 将评估粒度降到子目标，让失败原因可定位。对做 coding agent / harness 的人，调试 CUA 时能区分输入方式错误与任务理解错误。

**「可关注」** 评估 CUA 时，子目标完成度比最终交付物更能定位失败原因，键盘输入与点击输入错误需不同缓解策略。

**Tags**: `#eval`, `#coding-agent`, `#observability`

---

<a id="item-agent-engineer-6"></a>
### [EmbeddingGemma 2: An open, lightweight multimodal embedding model](https://blog.google/innovation-and-ai/technology/developers-tools/embeddinggemma-2/) ⭐️ 7.0/10

Google releases EmbeddingGemma 2, an open-source multimodal embedding model that agent engineers can use for local RAG and memory systems.

hackernews · ilreb · Oct 6, 16:03 · [Discussion](https://news.ycombinator.com/item?id=49980487)

**Tags**: `#memory`, `#toolchain`, `#multimodal`

---

<a id="item-agent-engineer-7"></a>
### [llm-mistral 0.16 发布](https://github.com/simonw/llm-mistral/releases/tag/0.16) ⭐️ 6.8/10

simonw/llm-mistral 0.16 于 2026-10-06 发布，支持 Mistral 推理模型（含 Mistral Large 4）的 reasoning\_effort 控制，通过 \`-o reasoning\_effort high\` 设置，可选值随模型包括 \`none\`、\`minimal\`、\`low\`、\`medium\`、\`high\`、\`xhigh\`。底层切换至官方 mistralai Python 库。Breaking change：移除 \`safe\_mode\`，改用与 Mistral API 同名的 \`-o safe\_prompt 1\`。Voxtral 音频模型现支持本地 MP3 附件，此前仅支持 URL。

github · simonw · Oct 6, 21:32

**「为什么重要」** 对 llm-mistral 插件用户，这次更新改变了命令行参数和依赖库，\`safe\_mode\` 相关调用必须调整。推理强度与本地音频支持扩展了使用场景，但影响范围仍限于该插件。

**「可关注」** 可关注：现有脚本需将 \`safe\_mode\` 迁移到 \`-o safe\_prompt 1\`，并确认目标模型实际支持的 \`reasoning\_effort\` 档位。

**Tags**: `#harness`, `#coding-agent`, `#tools`

---

<a id="item-agent-engineer-8"></a>
### [LMBuild 评估可建造 3D 结构](https://huggingface.co/papers/2610.04292) ⭐️ 6.0/10

Hugging Face Daily Papers 上线 LMBuild 基准，评估 LLM Agent 生成物理可建造且功能性 3D 结构的能力。现有评测多聚焦几何质量，忽视物理可实现性。LMBuild 将对象表示为包含零件分解、关节、材料与装配顺序的组装结构，并提供带工具调用能力的交互式环境以支持复现评估。论文发表于 2026-10-07，目前获 27 次点赞。

rss · Hugging Face Daily Papers · Oct 7, 01:58

**「为什么重要」** Agent 评测正从几何质量转向物理可实现性。LMBuild 把可建造性和功能性纳入基准，对做 3D 或具身生成场景的 Harness 设计有直接参考。影响面目前集中在 3D 结构生成，尚未看到跨领域复现数据。

**「可关注」** 可关注：LMBuild 用零件分解、关节、材料和装配顺序显式建模物理约束，做 3D 生成类 Agent 的 Harness 时，可参考其将可建造性拆解为可验证的结构要素，而非仅比对几何输出。

**Tags**: `#eval`, `#harness`

---

<a id="item-agent-engineer-9"></a>
### [EmbeddingGemma 2 开源：740M 多模态嵌入](https://www.reddit.com/r/LocalLLaMA/comments/1wz7faa/introducing_embeddinggemma_2_a_bestinclass_open/) ⭐️ 6.0/10

Google DeepMind 开源 EmbeddingGemma 2。模型共 740M 参数，将文本（含代码）、图像、视频、音频映射到统一的 768 维向量空间。结构上由 270M 文本模型、170M 视觉编码器与 300M 音频编码器组成。设计目标为手机、笔记本等消费级硬件，提供低延迟语义表示，支持端侧搜索、RAG、分类与聚类。材料未提供基准数据，&quot;best-in-class&quot; 说法暂无法验证。

reddit · r/LocalLLaMA · /u/Recoil42 · Oct 6, 16:42

**「为什么重要」** 对 coding agent 的检索与记忆链路，统一多模态向量空间减少了跨模态对齐的工程负担。端侧部署能力为本地 RAG 提供新选项。但它是组件级模型，不直接改变 agent 协议或 harness。

**「可关注」** 可关注：EmbeddingGemma 2 把代码、图像、音频压进同一 768 维空间，且面向端侧；材料未附基准，实际检索效果需自行验证。

**Tags**: `#memory`, `#rag`, `#coding-agent`, `#eval`

---

<a id="item-agent-engineer-10"></a>
### [I gave a 21M model a 6.4B-parameter lookup table. It matches a 114M dense model and runs with the table on an SSD \(RX 9070\)](https://www.reddit.com/r/LocalLLaMA/comments/1wz7tvs/i_gave_a_21m_model_a_64bparameter_lookup_table_it/) ⭐️ 5.5/10

A hobbyist reports that a 21M model with a 6.4B-parameter SSD-resident lookup table matches a 114M dense model on a small Wikipedia corpus, running at ~140 tok/s on a consumer AMD GPU with minimal VRAM.

reddit · r/LocalLLaMA · /u/fechyyy · Oct 6, 16:57

**Tags**: `#memory`, `#eval`, `#toolchain`

---

## AI Daily

<a id="item-ai-daily-1"></a>
### [OpenAI 发布数学开放问题新结果](https://openai.com/index/sharing-ai-progress-in-mathematics) ⭐️ 10.0/10

OpenAI 公布内部前沿模型在数学开放问题上的新结果，并在 GitHub 分享 Lean 证明形式化代码与研究细节。材料未提及具体问题清单、量化指标或对比基线。

rss · OpenAI Blog · Oct 6, 12:00

**「为什么重要」** Lean 证明形式化代码随研究细节一并开源，外部研究者能直接检查证明步骤，而非仅阅读自然语言论述。

**「可关注」** 可关注：OpenAI 此次公开的 Lean 形式化文件与研究细节已托管在 GitHub，可直接拉取审查其在开放问题上的形式化证明。

**Tags**: `#model`, `#lab`, `#open-source`, `#eval`

---

<a id="item-ai-daily-2"></a>
### [OpenAI 与 Ironclad 训练合同智能体](https://openai.com/index/advancing-computer-use-with-ironclad) ⭐️ 8.3/10

OpenAI 与 Ironclad 合作，在复杂合同流程上训练并评估 AI 智能体，推动面向专业工作的计算机使用能力。公开信息仅确认双方合作方向，未披露模型细节、评估基准或上线时间。

rss · OpenAI Blog · Oct 6, 10:00

**「为什么重要」** OpenAI 与 Ironclad 将计算机使用智能体用于复杂合同流程，是该能力进入专业工作场景的具体案例。不过目前公开信息较少，实际效果仍待观察。

**「可关注」** 可关注：OpenAI 与 Ironclad 在复杂合同流程上训练和评估计算机使用智能体，但技术细节和评估结果尚未公开。

**Tags**: `#lab`, `#product`, `#eval`, `#industry`

---

<a id="item-ai-daily-3"></a>
### [Building Git infrastructure for agent-scale development](https://github.blog/engineering/architecture-optimization/building-git-infrastructure-for-agent-scale-development/) ⭐️ 7.8/10

GitHub is rebuilding its Git infrastructure to create a foundation for agent-scale software development.

rss · GitHub Blog · Oct 6, 20:57

**Tags**: `#industry`, `#product`, `#open-source`

---

<a id="item-ai-daily-4"></a>
### [Jump Trading 用 ChatGPT 扩展研究](https://openai.com/index/jump-trading) ⭐️ 6.8/10

OpenAI 官方博客发布案例，介绍 Jump Trading 使用 ChatGPT 扩展量化研究。该案例描述通过更长时程的 AI 工作流，结合多个数据源与人工审查来推进研究流程。这是单一客户的企业应用实例，并非模型发布或政策变更。

rss · OpenAI Blog · Oct 6, 12:00

**「为什么重要」** 案例展示了 ChatGPT 在专业量化场景中的一种部署形态：长时程 AI 工作流配合人工审查。对构建 coding agent 或 harness 的工程师而言，可参考其在多数据源整合与人工节点介入上的组织方式。

**「可关注」** 可关注：长时程 AI 工作流在金融量化场景的落地方式，特别是多数据源整合与人工审查节点的设计。

**Tags**: `#model`, `#industry`, `#product`

---

<a id="item-ai-daily-5"></a>
### [OpenAI 扩展 Atlassian 合作](https://openai.com/index/atlassian-partnership) ⭐️ 6.8/10

OpenAI 与 Atlassian 宣布扩大合作，目标是将前沿模型与企业知识连接，帮助团队规划、构建和交付工作。目前官方仅发布高层级公告，未披露具体模型、集成方式或上线时间。

rss · OpenAI Blog · Oct 6, 16:00

**「为什么重要」** OpenAI 与 Atlassian 宣布扩大合作，把前沿模型与企业知识连接，企业级 AI 集成方向出现新进展，但具体技术方案尚未公布。

**「可关注」** 可关注：Atlassian 与 OpenAI 将前沿模型接入企业知识，具体产品形态和技术方案尚未公布。

**Tags**: `#lab`, `#industry`, `#model`, `#product`

---

<a id="item-ai-daily-6"></a>
### [Meta NTS 认证时间服务上线](https://engineering.fb.com/2026/10/06/production-engineering/nts-authenticated-time-at-meta/) ⭐️ 6.8/10

Meta 公共时间服务 nts.meta.com 支持 NTS（RFC 8915）。时间包带认证，设备可验证来源并发现传输中的篡改。服务端不保存每客户端状态，Cookie 密钥采用派生而非存储或复制。相关实现已开源。

rss · Engineering at Meta · Oct 6, 16:00

**「为什么重要」** 对分布式系统，认证时间同步可降低中间人篡改风险。无状态架构减少了服务端存储与复制负担。

**「可关注」** 可关注：Meta 开源了该 NTS 实现，其无状态 Cookie 密钥派生方案可避免存储和复制密钥。

**Tags**: `#industry`, `#lab`, `#open-source`, `#product`

---