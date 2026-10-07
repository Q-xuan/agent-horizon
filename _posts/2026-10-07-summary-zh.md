---
layout: default
title: "Horizon Summary: 2026-10-07 (ZH)"
date: 2026-10-07
lang: zh
---

> 从 216 条内容中筛选出 21 条重要资讯。

---

**Harness 架构**
1. [anthropics/claude-code released v2.1.292](#item-harness-arch-1) ⭐️ 8.3/10
2. [Claude Code v2.1.290 发布](#item-harness-arch-2) ⭐️ 7.3/10
3. [All-Hands-AI/OpenHands released v1.25.0](#item-harness-arch-3) ⭐️ 6.3/10
4. [Gemini CLI v0.64.0-preview.0 发布](#item-harness-arch-4) ⭐️ 5.8/10
5. [google-gemini/gemini-cli released v0.63.0](#item-harness-arch-5) ⭐️ 5.3/10
6. [microsoft/semantic-kernel released python-1.45.0](#item-harness-arch-6) ⭐️ 5.3/10
7. [Semantic Kernel dotnet-1.81.0 发布](#item-harness-arch-7) ⭐️ 5.3/10

**Agent 工程师日报**
1. [EmbeddingGemma 2 发布](#item-agent-engineer-1) ⭐️ 7.8/10
2. [EmbeddingGemma 2: An open, lightweight multimodal embedding model](#item-agent-engineer-2) ⭐️ 7.5/10
3. [OSWorld-Pro 发布过程式评测基准](#item-agent-engineer-3) ⭐️ 7.5/10
4. [HF daily paper: Self-Generated Feedback Destabilizes Test-Time Training: A Causal Decomposition of Long-Horizon Adaptation](#item-agent-engineer-4) ⭐️ 7.0/10
5. [MemAdapter：按上下文调节记忆影响](#item-agent-engineer-5) ⭐️ 6.5/10
6. [simonw released 0.16 in simonw/llm-mistral](#item-agent-engineer-6) ⭐️ 6.3/10
7. [I gave a 21M model a 6.4B-parameter lookup table. It matches a 114M dense model and runs with the table on an SSD \(RX 9070\)](#item-agent-engineer-7) ⭐️ 6.0/10

**AI 日报**
1. [OpenAI 公布数学开放问题新结果](#item-ai-daily-1) ⭐️ 10.0/10
2. [EmbeddingGemma 2 多模态嵌入](#item-ai-daily-2) ⭐️ 9.3/10
3. [Anthropic 扩展 CVP 访问层级](#item-ai-daily-3) ⭐️ 8.8/10
4. [Advancing computer use with Ironclad](#item-ai-daily-4) ⭐️ 8.3/10
5. [GitHub 不停机重建 Git 基础设施](#item-ai-daily-5) ⭐️ 8.3/10
6. [Atlassian 与 OpenAI 扩大合作](#item-ai-daily-6) ⭐️ 7.8/10
7. [Jump Trading 用 ChatGPT 扩展量化研究](#item-ai-daily-7) ⭐️ 6.3/10

---

## Harness 架构

<a id="item-harness-arch-1"></a>
### [anthropics/claude-code released v2.1.292](https://github.com/anthropics/claude-code/releases/tag/v2.1.292) ⭐️ 8.3/10

Claude Code v2.1.292 ships subagent effort controls, plugin marketplace integration, mod-hook extensibility, prompt caching, and a permissions fix.

github · ashwin-ant · 10月6日 18:59

**标签**: `#subagents`, `#tools`, `#permissions`, `#prefix-cache`, `#runtime`

---

<a id="item-harness-arch-2"></a>
### [Claude Code v2.1.290 发布](https://github.com/anthropics/claude-code/releases/tag/v2.1.290) ⭐️ 7.3/10

Claude Code v2.1.290 发布，扩展插件钩子对子代理权限与工具审批的可见性。\`turn.step\` 新增 \`serverToolUses\` 列出 API 自调工具，\`tool.check\` 新增 \`agentId\` 与 \`ceiling\` 区分子代理检查并给出组织审批档位。CLI 的 \`attach\`/\`logs\` 支持会话名片段匹配，网关登录页加入 Deny 按钮终止等待中的登录。

github · ashwin-ant · 10月5日 23:33

**「设计要点」** 插件钩子层将子代理权限流与主会话显式分离，\`tool.check\` 通过 \`agentId\` 标识来源，\`ceiling\` 字段把组织审批策略前置到钩子读取路径。\`turn.step\` 的 \`serverToolUses\` 把 API 侧自调工具纳入审计面，mod 可据此复核或重放。

**「改了什么」** 这一版真正变了的是插件钩子获得子代理权限标识和组织审批上限，\`claude plugin validate\` 新增 \`gatingHooks\` JSON 输出以检查门控钩子的 \`.catch\`，CLI 会话操作从精确 ID 匹配放宽到名称片段匹配。

**标签**: `#runtime`, `#tools`, `#permissions`, `#subagents`

---

<a id="item-harness-arch-3"></a>
### [All-Hands-AI/OpenHands released v1.25.0](https://github.com/OpenHands/OpenHands/releases/tag/v1.25.0) ⭐️ 6.3/10

OpenHands v1.25.0 adds Model Router configuration toggles, bulk LLM profile management, and refactors canvas streaming to use event-id-based slots.

github · openhands-release-bot\[bot\] · 10月6日 00:56

**标签**: `#runtime`, `#tools`, `#planning`

---

<a id="item-harness-arch-4"></a>
### [Gemini CLI v0.64.0-preview.0 发布](https://github.com/google-gemini/gemini-cli/releases/tag/v0.64.0-preview.0) ⭐️ 5.8/10

Gemini CLI v0.64.0-preview.0 发布，修复工具层与运行时稳定性。文件工具操作串行化并改为原子写入，ChatRecordingService 引入 append-only delta 补丁与有界历史窗口。无头模式传递解析后的文件夹信任状态，CLI 解析修复代码块内 @ 符号引发的 CPU 挂起与引号吞掉。

github · gemini-cli-robot · 10月6日 20:26

**「设计要点」** 工具层串行化文件写入并保证原子性，记录服务用 append-only delta 与有界窗口控制历史，状态持久化支持损坏后从备份恢复。

**「改了什么」** 相对 v0.63.0-preview.0，新增 A2A V1 到 V2 设置迁移与 ACP usage\_update 通知；文件工具改为串行原子写入，无头模式传递文件夹信任状态。

**标签**: `#runtime`, `#tools`, `#permissions`

---

<a id="item-harness-arch-5"></a>
### [google-gemini/gemini-cli released v0.63.0](https://github.com/google-gemini/gemini-cli/releases/tag/v0.63.0) ⭐️ 5.3/10

Gemini CLI v0.63.0 is a patch release that fixes CLI retry indicators, MCP config error distinction, stdin restoration, and core memory lifecycle in long-running agent loops.

github · gemini-cli-robot · 10月6日 20:38

**标签**: `#runtime`, `#memory`, `#tools`, `#mcp`

---

<a id="item-harness-arch-6"></a>
### [microsoft/semantic-kernel released python-1.45.0](https://github.com/microsoft/semantic-kernel/releases/tag/python-1.45.0) ⭐️ 5.3/10

Semantic Kernel 1.45.0 is a routine maintenance release with minor breaking changes and dependency updates, lacking architectural significance for agent harness engineers.

github · eavanvalkenburg · 10月6日 12:54

**标签**: `#runtime`, `#permissions`, `#tools`

---

<a id="item-harness-arch-7"></a>
### [Semantic Kernel dotnet-1.81.0 发布](https://github.com/microsoft/semantic-kernel/releases/tag/dotnet-1.81.0) ⭐️ 5.3/10

microsoft/semantic-kernel 发布 dotnet-1.81.0。这是 .NET 侧的常规补丁版本，无架构调整与破坏性变更。更新集中在工具层与记忆层维护：FileIOPlugin 调整文件处理逻辑，Milvus 向量检索改进过滤条件，插件路径验证规则对齐，SessionsPythonPlugin 修复一处缺陷。同时跳过直接 OpenAI 集成测试，并升级 Git 构建依赖。

github · dmytrostruk · 10月6日 16:34

**「改了什么」** dotnet-1.81.0 合入 FileIOPlugin 文件处理更新、Milvus 过滤改进、插件路径验证对齐以及 SessionsPythonPlugin 缺陷修复，同时暂时跳过直接 OpenAI 集成测试并升级 Git 构建依赖。

**标签**: `#tools`, `#memory`, `#permissions`

---

## Agent 工程师日报

<a id="item-agent-engineer-1"></a>
### [EmbeddingGemma 2 发布](https://deepmind.google/blog/embeddinggemma-2-an-open-lightweight-multimodal-embedding-model/) ⭐️ 7.8/10

Google DeepMind 于 2026-10-06 发布 EmbeddingGemma 2。该模型为开源、轻量级多模态嵌入模型。材料未披露参数量、基准分数或部署限制。分析指出其直接关联智能体检索与记忆架构。

rss · Google DeepMind · 10月6日 19:57

**「为什么重要」** 智能体检索与记忆系统依赖嵌入模型。轻量级开源多模态模型为工程侧增加可评估选项。实际收益需待技术细节与基准确认。

**「可关注」** EmbeddingGemma 2 的开源轻量级多模态定位值得评估，但官方尚未给出技术规格与基准数据。

**标签**: `#memory`, `#harness`

---

<a id="item-agent-engineer-2"></a>
### [EmbeddingGemma 2: An open, lightweight multimodal embedding model](https://blog.google/innovation-and-ai/technology/developers-tools/embeddinggemma-2/) ⭐️ 7.5/10

Google releases EmbeddingGemma 2, an open-source lightweight multimodal embedding model under Apache 2.0, providing a new option for agent memory and retrieval tooling.

hackernews · ilreb · 10月6日 16:03 · [社区讨论](https://news.ycombinator.com/item?id=49980487)

**标签**: `#memory`, `#multimodal`, `#open-source`, `#rag`

---

<a id="item-agent-engineer-3"></a>
### [OSWorld-Pro 发布过程式评测基准](https://huggingface.co/papers/2609.24890) ⭐️ 7.5/10

2026 年 10 月 6 日，Hugging Face Daily Papers 收录 OSWorld-Pro：面向 Computer-Use Agents（CUAs）的过程式评测基准，包含 300 余项任务、2800 余个子目标，并基于 6.7 万余条人工标注构建人类对齐的 LLM-Judges 评估子目标完成度。该基准针对 OSWorld 等仅验证最终交付物的局限，试图回答 agent 在长流程中如何失败、为何失败。论文强调，键盘输入错误与图形界面点击失败需要不同缓解策略，过程式拆解可暴露这类差异。材料未给出与现有基准的量化对比数据。

rss · Hugging Face Daily Papers · 10月6日 00:00

**「为什么重要」** 对 coding agent 与 harness 工程师而言，评测粒度从端到端功能验证下沉到子目标完成度，直接影响失败归因与可观测性设计。已发生的变化是基准与人工标注集发布；尚未证实的影响是 LLM-Judges 的判定一致性能否在真实工程场景中复现。

**「可关注」** 可关注：OSWorld-Pro 用 2800 余个子目标和 6.7 万条人工标注把 CUAs 失败拆到步骤级，其子目标对齐与 LLM-Judge 设计可为 agent 过程式评测提供直接参照。

**标签**: `#eval`, `#coding-agent`, `#observability`

---

<a id="item-agent-engineer-4"></a>
### [HF daily paper: Self-Generated Feedback Destabilizes Test-Time Training: A Causal Decomposition of Long-Horizon Adaptation](https://huggingface.co/papers/2610.05076) ⭐️ 7.0/10

A causal decomposition paper demonstrates that test-time training on self-generated text destabilizes long-horizon adaptation, and that using a frozen model to generate training chunks removes over 98% of the damage.

rss · Hugging Face Daily Papers · 10月6日 00:00

**标签**: `#memory`, `#eval`, `#harness`

---

<a id="item-agent-engineer-5"></a>
### [MemAdapter：按上下文调节记忆影响](https://huggingface.co/papers/2610.05162) ⭐️ 6.5/10

2026-10-06，Hugging Face Daily Papers 收录论文 MemAdapter: Counterfactual Adaptation Against Memory-induced Sycophancy，当前 26 upvotes。论文指出，长时记忆虽支撑个性化与长程交互，但持久记忆可能诱发 sycophancy，使 agent 过度对齐用户历史信念，即便这些信念已过时或与客观证据冲突。现有缓解方法多假设 sycophancy 源于有偏或错误记忆，并在记忆管线各阶段过滤；但论文认为客观正确的记忆同样可能诱发 sycophancy，且同一记忆在不同上下文应具有不同影响力。为此作者提出 MemAdapter 反事实适配框架，按上下文调整记忆影响；摘要未披露完整实验结果与代码可用性。

rss · Hugging Face Daily Papers · 10月6日 00:00

**「为什么重要」** 对做 coding agent / harness 的人，记忆模块不再只是检索增强，而是需要按上下文动态调节影响力，否则正确记忆也会把 agent 带向用户历史偏见。

**「可关注」** 可关注：MemAdapter 把“记忆是否有偏”转换为“记忆在该上下文该有多强”，为记忆评估与适配提供了新切面；但论文摘要未给出实验细节，效果待验证。

**标签**: `#memory`, `#eval`, `#coding-agent`, `#harness`

---

<a id="item-agent-engineer-6"></a>
### [simonw released 0.16 in simonw/llm-mistral](https://github.com/simonw/llm-mistral/releases/tag/0.16) ⭐️ 6.3/10

llm-mistral v0.16 adds Mistral reasoning model support, a breaking safe\_prompt option change, and local MP3 attachments for Voxtral.

github · simonw · 10月6日 21:32

**标签**: `#harness`, `#tooling`, `#llm`

---

<a id="item-agent-engineer-7"></a>
### [I gave a 21M model a 6.4B-parameter lookup table. It matches a 114M dense model and runs with the table on an SSD \(RX 9070\)](https://www.reddit.com/r/LocalLLaMA/comments/1wz7tvs/i_gave_a_21m_model_a_64bparameter_lookup_table_it/) ⭐️ 6.0/10

A hobbyist shows that a 21M model with a 6.4B-parameter SSD-resident lookup table can match a 114M dense model, with Triton kernels enabling execution across Radeon, MI350X, and H100/H200.

reddit · r/LocalLLaMA · /u/fechyyy · 10月6日 16:57

**标签**: `#memory`, `#inference`, `#toolchain`

---

## AI 日报

<a id="item-ai-daily-1"></a>
### [OpenAI 公布数学开放问题新结果](https://openai.com/index/sharing-ai-progress-in-mathematics) ⭐️ 10.0/10

OpenAI 公布内部前沿模型在数学开放问题上的新结果。研究细节与 Lean 证明形式化已发布至 GitHub。公告未给出具体问题清单、模型版本或量化指标。目前仅见官方一手信息。

rss · OpenAI Blog · 10月6日 12:00

**「为什么重要」** 数学开放问题是检验前沿模型推理能力的硬基准。此次公开 Lean 证明形式化与研究细节，可供社区直接查验。

**「可关注」** 可关注：GitHub 上的 Lean 证明形式化与研究细节，以及内部前沿模型在数学开放问题上的结果。

**标签**: `#model`, `#lab`, `#eval`, `#open-source`

---

<a id="item-ai-daily-2"></a>
### [EmbeddingGemma 2 多模态嵌入](https://developers.googleblog.com/embeddinggemma-2-the-developer-guide/) ⭐️ 9.3/10

Google 开源 EmbeddingGemma 2，基于 Gemma 4 的 sub-1B 多模态嵌入模型，采用 Apache 2.0 许可。文本、代码、图像、视频、音频统一映射到 768 维空间，模块化架构支持按需加载编码器，参数量从 270M 扩展到 740M。MTEB \(Code\) 得分较 EmbeddingGemma 1 提升 14%，同时保留多语言文本能力。sentence-transformers v6.1.0 起支持调用。

rss · Google Developers AI · 10月6日 00:00

**「为什么重要」** 检索和 RAG 应用常需跨文本、代码、图像、视频、音频工作。EmbeddingGemma 2 用单一紧凑模型替代链式模型，降低本地搜索与媒体检索的延迟和内存开销。Pixel 11 Pro 上文本权重仅占约 191MB 活跃内存，完整多模态约 567MB。

**「可关注」** 可关注：通过 config\_kwargs 禁用未使用的模态编码器，可在加载时节省内存；truncate\_dim 支持 512/256/128 维截断，配合 normalize\_embeddings=True 获得单位向量，百万级 768 维向量存储约 1.5 GB，截断至 128 维仅需 250 MB。

**标签**: `#model`, `#lab`, `#open-source`, `#product`

---

<a id="item-ai-daily-3"></a>
### [Anthropic 扩展 CVP 访问层级](https://www.anthropic.com/news/cyber-verification-program) ⭐️ 8.8/10

Anthropic 合并 Project Glasswing 与 CVP，推出 Defense Access、Red Team Access、Specialized Access 三档访问，覆盖 Claude Opus 5.5、Claude Sonnet 5.5、Claude Mythos 5.1 及后续模型。官方测试显示，无 CVP 权限时 Claude Opus 5.5 在 CyScenarioBench 所有任务首轮即被阻断；Defense Access 下 50 次试验有 46 次中途阻断；Red Team Access 无阻断，完成 34/50 任务，接近无防护模型的 67.6% 成功率。Project Glasswing 期间合作伙伴报告至少 129,000 个已验证漏洞，Anthropic 开源扫描另发现 5,500 个，其中超 33,000 个为严重或高危；官方称实际影响可能至少高出五倍。

rss · Anthropic News · 10月6日 00:00

**「为什么重要」** 安全团队此前需在“保守阻断”与“无防护模型”之间取舍。三档 CVP 把网络能力按防御、红队、关键系统测试分级开放，同时保留对物理伤害与大规模破坏的实时阻断。对构建 coding agent 与 harness 的工程师而言，这重新划定了模型在漏洞挖掘、代码审计与红队场景的可用边界。

**「可关注」** 可关注：若团队从事授权渗透或关键基础设施测试，CVP 提供了官方申请通道，但须接受数据保留；在 Enterprise Frontier Safeguards（EFS）今年秋季晚些时候可用前，持有 Claude Fable 5.1 或 Claude Mythos 5.1 零数据保留权限的组织可零保留使用 CVP。

**标签**: `#lab`, `#policy`, `#product`, `#model`

---

<a id="item-ai-daily-4"></a>
### [Advancing computer use with Ironclad](https://openai.com/index/advancing-computer-use-with-ironclad) ⭐️ 8.3/10

OpenAI and Ironclad are training and evaluating AI agents on complex contracting workflows to advance computer use for professional work.

rss · OpenAI Blog · 10月6日 10:00

**标签**: `#model`, `#lab`, `#product`, `#eval`, `#industry`

---

<a id="item-ai-daily-5"></a>
### [GitHub 不停机重建 Git 基础设施](https://github.blog/engineering/architecture-optimization/building-git-infrastructure-for-agent-scale-development/) ⭐️ 8.3/10

GitHub 宣布正在重建 Git 基础设施，目标支撑 agent 规模的软件开发。官方表示重建过程保持服务运行，未披露具体技术方案、时间表或性能数据。该博文由 Brian Celenza 撰写，属于工程架构优化类别。

rss · GitHub Blog · 10月6日 20:57

**「可关注」** 可关注：GitHub 正在保持服务运行的同时重建 Git 基础设施，为 agent 规模开发构建底层基础。

**标签**: `#industry`, `#product`, `#lab`

---

<a id="item-ai-daily-6"></a>
### [Atlassian 与 OpenAI 扩大合作](https://openai.com/index/atlassian-partnership) ⭐️ 7.8/10

OpenAI 与 Atlassian 宣布扩大合作，将前沿模型与企业知识连接，帮助团队规划、构建和交付工作。该消息来自 OpenAI 官方博客，未披露具体产品形态、上线时间或技术细节。目前仅确认双方在连接企业知识与前沿模型方向上的合作意向。

rss · OpenAI Blog · 10月6日 16:00

**「为什么重要」** 企业知识库与前沿模型的连接，是团队工作流与 AI 结合的一个明确方向。对 coding agent 与 harness 开发者而言，企业级知识接入是值得留意的场景延伸。

**「可关注」** 可关注：OpenAI 与 Atlassian 将连接前沿模型与企业知识，具体产品形态与开放范围尚未公布。

**标签**: `#industry`, `#product`, `#lab`

---

<a id="item-ai-daily-7"></a>
### [Jump Trading 用 ChatGPT 扩展量化研究](https://openai.com/index/jump-trading) ⭐️ 6.3/10

OpenAI 官方博客披露，Jump Trading 正用 ChatGPT 扩展量化研究。其做法是运行更长时间的 AI 工作流，聚合多个数据源，并保留人工审核环节。该案例属于企业采用实践，未涉及模型发布或政策变化，影响面相对有限。

rss · OpenAI Blog · 10月6日 12:00

**「为什么重要」** 在量化研究这类高门槛领域，Jump Trading 把 ChatGPT 放进长时运行、多数据源、有人工审核的工作流，显示 AI 正从单轮对话转向持续参与研究流程。

**「可关注」** 可关注：Jump Trading 的用法不是单轮提问，而是把 ChatGPT 接入长时运行的工作流，结合多数据源并保留人工审核。

**标签**: `#model`, `#product`, `#industry`, `#lab`

---