---
layout: default
title: "Horizon Summary: 2026-10-21 (ZH)"
date: 2026-10-21
lang: zh
---

> 从 231 条内容中筛选出 17 条重要资讯。

<nav id="ah-toc" class="ah-toc" aria-label="目录"><span class="ah-toc-title">目录</span><ul><li><a href="#sec-harness-arch"><span class="ah-toc-name">Harness 架构</span><span class="ah-toc-count">3条</span></a></li><li><a href="#sec-agent-engineer"><span class="ah-toc-name">Agent 工程师日报</span><span class="ah-toc-count">11条</span></a></li><li><a href="#sec-ai-daily"><span class="ah-toc-name">AI 日报</span><span class="ah-toc-count">2条</span></a></li><li><a href="#sec-ai-deals"><span class="ah-toc-name">AI 羊毛</span><span class="ah-toc-count">1条</span></a></li></ul></nav>

---

**[Harness 架构](#sec-harness-arch)**
1. [Cloudflare Agents 0.29.0 发布](#item-harness-arch-1) ⭐️ 7.8/10
2. [openai-agents-js 0.21.0 发布](#item-harness-arch-2) ⭐️ 7.8/10
3. [OpenHands v1.29.0 发布](#item-harness-arch-3) ⭐️ 6.8/10

**[Agent 工程师日报](#sec-agent-engineer)**
1. [ALTK-Evolve 登顶 τ²-bench 零售榜](#item-agent-engineer-1) ⭐️ 8.8/10
2. [DeepSeek 开源 DeepInfer 推理框架](#item-agent-engineer-2) ⭐️ 7.0/10
3. [OR-License 运筹学 Agent 基准发布](#item-agent-engineer-3) ⭐️ 7.0/10
4. [Self-HPO 联合优化 harness 与 policy](#item-agent-engineer-4) ⭐️ 7.0/10
5. [Interlock 长时程智能体框架论文](#item-agent-engineer-5) ⭐️ 7.0/10
6. [决策模型 Eval 实践指南发布](#item-agent-engineer-6) ⭐️ 7.0/10
7. [FairStress 公平性评测基准发布](#item-agent-engineer-7) ⭐️ 6.8/10
8. [Cloudflare tsrs：TypeScript 编译器移植 Rust](#item-agent-engineer-8) ⭐️ 6.0/10
9. [MemT-1.0 内存原生架构发布](#item-agent-engineer-9) ⭐️ 6.0/10
10. [Ornith-1.5-122B 发布](#item-agent-engineer-10) ⭐️ 6.0/10
11. [llm-public-ai 0.1 发布](#item-agent-engineer-11) ⭐️ 5.8/10

**[AI 日报](#sec-ai-daily)**
1. [Terminal X 用 GPT-6.1 匹配投资者判断 88.6%](#item-ai-daily-1) ⭐️ 6.8/10
2. [ChatGPT Work 餐饮客户案例发布](#item-ai-daily-2) ⭐️ 5.8/10

**[AI 羊毛](#sec-ai-deals)**
1. [全国在职教师可领 WorkBuddy 教育版一年免费](#item-ai-deals-1) ⭐️ 8.0/10

---

## Harness 架构
{: #sec-harness-arch .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-harness-arch" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-harness-arch-1"></a>
### [Cloudflare Agents 0.29.0 发布](https://github.com/cloudflare/agents/releases/tag/agents%400.29.0) ⭐️ 7.8/10

官方 Cloudflare Agents 0.29.0 发布。Agent Skills 改为读写 @cloudflare/computer Workspace（projection 和 skills.runner\(\)），属 breaking change。Browser tool 改用 typed acquire\(\)/closeSession\(\) 管理 session，本地开发回退 HTTP API。createAI 支持跨账户 gateway（\{ accountId, apiToken \}）、@cf/deepgram/nova-3 转录音频、流式恢复、catalog ids。Chat recovery 默认 5 次中断后封存 turn，废弃 maxOomRetries。Pi 1.3 支持、PiHarness entry 选项、openPiSessionStore 改用 pi-durable SQLite adapter。

github · github-actions\[bot\] · 10月20日 15:20

**「改了什么」** Agent Skills 强制迁移至 @cloudflare/computer Workspace。Browser session 管理改为 typed binding API。createAI 新增跨账户 gateway、nova-3 转录、流式恢复、catalog ids。Chat recovery 默认 5 次中断后封存 turn。Pi 1.3 支持、PiHarness entry 选项、openPiSessionStore 改用 pi-durable SQLite adapter。

**「评论」** 无社区评论。

**标签**: `#tools`, `#runtime`, `#memory`

---

<a id="item-harness-arch-2"></a>
### [openai-agents-js 0.21.0 发布](https://github.com/openai/openai-agents-js/releases/tag/%40openai/agents-core%400.21.0) ⭐️ 7.8/10

openai-agents-js 0.21.0 正式发布。本次更新包含一个破坏性变更：移除 Runloop sandbox provider 及其公共 API，需按迁移指南切换替代方案。运行时修复了嵌套数值 token 使用统计在流式运行、使用统计和保存运行状态中的保留问题，schema 升级至 1.23 并向后兼容早期快照。此外新增对 GPT-6 Astra、Sol、Luna 及 GPT-6.1 Sol 的沙箱动态压缩阈值识别。

github · openai-sdks\[bot\] · 10月20日 22:07

**「设计要点」** 沙箱层采用可插拔 provider 架构，Runloop 移除后需通过官方迁移指南切换至受支持的替代实现。运行时使用统计采用 schema 1.23 版本，通过有界嵌套数值结构保留 token 使用明细，并在算术运算前强制类型收窄为数字。

**「改了什么」** 移除 Runloop sandbox provider 公共 API，需迁移至替代方案。修复嵌套数值 token 使用明细在流式运行和状态保存中的丢失问题，schema 升级至 1.23。新增 GPT-6 系列模型（Astra、Sol、Luna、GPT-6.1 Sol）的沙箱动态压缩阈值支持。

**「评论」** 无社区评论。

**标签**: `#sandbox`, `#runtime`

---

<a id="item-harness-arch-3"></a>
### [OpenHands v1.29.0 发布](https://github.com/OpenHands/OpenHands/releases/tag/v1.29.0) ⭐️ 6.8/10

OpenHands v1.29.0 发布，新增 agent 配置文件的 per-profile 多维度配置能力，包括从服务器目录选择技能、编辑冷凝器/验证规则、选择 Model Router。优化后端选择器显示完整组织名、启动器读取 bundled 扩展公共技能。修复云对话保存连接仓库、模型同步时间从 10 秒降至 1 秒、浅色主题 git chip 图标等问题。

github · openhands-release-bot\[bot\] · 10月20日 22:22

**「改了什么」** agent-profiles 支持按 profile 选择技能、配置冷凝器/验证规则、选择 Model Router。后端选择器显示完整组织名。启动器读取 bundled 扩展公共技能。模型同步时间从 10 秒降至 1 秒。

**标签**: `#agent-profiles`, `#skills`, `#memory`, `#model-routing`

---

## Agent 工程师日报
{: #sec-agent-engineer .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-agent-engineer" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-agent-engineer-1"></a>
### [ALTK-Evolve 登顶 τ²-bench 零售榜](https://huggingface.co/blog/ibm-research/altk-evolve-bc) ⭐️ 8.8/10

2026 年 10 月 20 日，IBM Research 发布 ALTK-Evolve 方法，通过将智能体在训练任务上的试错轨迹用 GPT-4.1 蒸馏为简短行为准则，追加到基础 ReAct 智能体的系统提示中，使用 GPT-4.1 作为智能体模型、GPT-5.5 作为用户模拟器模型，无需模型权重更新、无人工标注，即可在τ²-bench 零售基准拿到 67.5%的 Pass^4，超过 2026 年 10 月 12 日该基准所有历史零售条目。该方法运行在τ²-bench 原生 ReAct 框架，仅调整系统提示内容；零售域全量准则配置的 Pass^4 比无准则基线提升 10 个百分点，航空域高支持度核心准则的 Pass^4 比基线提升 10 个百分点。

rss · Hugging Face Blog · 10月20日 15:19

**「为什么重要」** 它证明客户服务类 agent 的 SOTA 性能无需依赖前沿推理模型或模型微调，仅通过提示词层面的记忆蒸馏即可实现，为 agent 记忆设计、评估框架搭建提供了可复现的工程路径。该方法在其他任务域、其他模型上的泛化效果尚未在公开材料中得到验证。

**「可关注」** 可关注：learned memory 的准则规模需按域调整，零售域全量准则的收益最高，航空域高支持度核心准则的 Pass^4 更优，且性能提升的成本增量来自输入 token 而非对话轮数。

**标签**: `#memory`, `#eval`, `#harness`, `#coding-agent`

---

<a id="item-agent-engineer-2"></a>
### [DeepSeek 开源 DeepInfer 推理框架](https://github.com/deepseek-ai/DeepInfer) ⭐️ 7.0/10

2026 年 10 月 20 日，DeepSeek 官方开源专为其模型系列设计的高性能推理框架 DeepInfer，仓库地址为 https://github.com/deepseek-ai/DeepInfer，相关发布与 AI agent 部署工具链场景相关。当前公开帖子缺乏框架深度技术细节，社区存在未经验证的性能声称，包括称该框架支撑 DeepSeek V4.1 Flash 实现单集群日吞吐 155 万亿 token、单卡每小时非高峰定价收入 38 美元，同时社区评论包含大量无关政治讨论。

hackernews · ggcr · 10月20日 09:08 · [社区讨论](https://news.ycombinator.com/item?id=50163277)

**「为什么重要」** 这是 DeepSeek 官方首次公开自有模型系列的高性能推理框架，填补了其官方推理工具链的公开空白，但当前公开信息不足以评估实际性能与落地价值，社区声称均未获官方证实。

**「可关注」** 可关注：当前官方仓库未公开框架核心实现细节，社区提及的华为升腾 950 NPU 支持、单集群吞吐等声称均未获官方验证，需以仓库后续正式更新为准。

**「评论」** 社区评论中混杂大量无关政治讨论，部分用户转发了未经验证的框架性能数据，也有用户关注到该框架开源升腾 NPU 支持可能对全球 AI 硬件市场格局产生潜在影响，但相关影响尚未得到证实。

**标签**: `#inference`, `#toolchain`, `#open-source`

---

<a id="item-agent-engineer-3"></a>
### [OR-License 运筹学 Agent 基准发布](https://huggingface.co/papers/2610.24087) ⭐️ 7.0/10

2026 年 10 月 21 日，Hugging Face Daily Papers 介绍 OR-License 基准测试与 ORSim 模拟器，用于评估 LLM agents 在真实运筹学任务上的端到端表现。OR-License 包含 31 个实例、10 个工业场景，材料来自价值 368 万美元的付费 OR 项目，经过去识别处理，保留原始需求、输入数据、交付格式及信息边界。ORSim 作为受控客户端模拟器，仅披露业务事实而不提供 OR 专业知识，用于研究 agent 信息获取能力。当前摘要片段截断，未提供具体性能对比数据。

rss · Hugging Face Daily Papers · 10月21日 01:47

**「为什么重要」** 现有 OR 基准多从自包含描述或预定义优化任务出发，缺乏对原始业务材料到专业解决方案翻译过程的评估。OR-License 提供生产环境对齐的端到端评估资源，但完整性能数据尚未披露，实际效用需等待全文。

**「可关注」** 可关注：OR-License 保留了原始业务材料到交付物的完整信息边界，适合测试 agent 在非结构化需求下的任务拆解与信息获取能力。

**标签**: `#eval`, `#orchestration`

---

<a id="item-agent-engineer-4"></a>
### [Self-HPO 联合优化 harness 与 policy](https://huggingface.co/papers/2610.22791) ⭐️ 7.0/10

2026-10-21 发布的论文提出 Self-HPO 递归框架，交替优化 coding agent 的 harness 与 policy，用演化中的 policy 自身作为 harness 提议者。核心论点是两者相互强化，仅优化单一组件会导致次优：为旧 policy 调优的 harness 无法适配新 policy 的失败模式，而 policy 学习又受限于固定 harness 产生的轨迹。该研究影响构建 coding agent、harness 及 eval 系统的工程师，但材料未给出完整性能基准数据。

rss · Hugging Face Daily Papers · 10月21日 01:47

**「为什么重要」** 该框架直接针对 coding agent 系统设计中的常见张力：policy 与 harness 的耦合优化。对构建 eval 系统或 agent harness 的工程师而言，这提供了一种避免单组件瓶颈的改进路径，但具体效果仍需完整基准验证。

**「可关注」** 可关注：当 policy 与 harness 由不同团队或阶段独立迭代时，可能产生适配错位，Self-HPO 的交替优化思路可参考。

**标签**: `#coding-agent`, `#harness`, `#eval`, `#orchestration`

---

<a id="item-agent-engineer-5"></a>
### [Interlock 长时程智能体框架论文](https://huggingface.co/papers/2610.19686) ⭐️ 7.0/10

2026-10-21，Hugging Face Daily Papers 收录一篇 arXiv 预印本，提出 Interlock 图结构任务合成框架。该框架将任务建模为类型化完成图，通过接地边连接公共证据与决策、耦合超边对组件施加联合约束、实现边连接决策与结果，旨在解决长时程 LLM 智能体&quot;局部正确但整体不完整&quot;的失败模式。当前材料为截断片段，未提供实证性能数据或实现细节，对 coding agent 编排与 eval 的实际影响尚不明确。

rss · Hugging Face Daily Papers · 10月21日 01:47

**「为什么重要」** 该框架直接针对长时程智能体在碎片化证据与跨资源依赖环境中的普遍失败模式，提供了类型化完成图与耦合超边的具体结构设计，对 agent 编排和架构设计有参考价值。但论文片段被截断，尚无实证性能数据或实现细节，实际效果与工程落地成本待验证。

**「可关注」** 可关注：长时程任务中，局部正确不等于任务完成，显式建模证据-决策-效果之间的依赖关系（如耦合超边）可能是降低不完整率的关键结构设计。

**标签**: `#orchestration`, `#coding-agent`, `#eval`

---

<a id="item-agent-engineer-6"></a>
### [决策模型 Eval 实践指南发布](https://hamel.dev/blog/posts/decision-model-evals/) ⭐️ 7.0/10

2026 年 10 月 20 日，技术博客发布决策模型用于自动化 Eval 的实践指南，测试了 Jev 1.13、Perplexity Decider 1.1 27B、Liquid d1/d1-ultra、Cloudflare Clef Flash、OpenAI Decisions（GPT-6 Luna）共 6 款决策模型，基于 100 条公寓租赁 Agent 的对话 trace 开展二分类（通过/失败）评估，核心验证默认 0.5 决策阈值常导致性能损失，调优阈值后不同模型的 F1 分数与成本差异显著。该指南面向搭建 Eval pipeline 或 Agent harness 的工程师，未纳入延迟维度对比，结论仅适用于本次测试的失败检测场景。

rss · Hamel Husain · 10月20日 07:00

**「为什么重要」** 当前决策模型作为 LLM 裁判的低成本替代方案在 Eval 场景的落地缺乏实操规范，该指南提供了阈值调优、成本性能权衡、分数校准的可复用方法，为工程师搭建自动化评估管线提供了参考。

**「可关注」** Eval 场景使用决策模型时需针对自身数据集调优决策阈值，避免直接使用默认 0.5 阈值导致性能损失，同时需结合业务对精确率/召回率的要求选择阈值，而非盲目最大化 F1。

**标签**: `#eval`, `#observability`, `#harness`

---

<a id="item-agent-engineer-7"></a>
### [FairStress 公平性评测基准发布](https://huggingface.co/blog/allenai/fairstress) ⭐️ 6.8/10

2026 年 10 月 20 日，Hugging Face 与 Allen AI 联合发布 FairStress 公平性评测基准，用于测试 LLM 在高风险决策场景中的人口统计公平性，已集成至开源评测工作台 Olmo-eval。该基准包含 300 个双候选决策场景，覆盖 29 个领域，通过对抗前缀压力测试模型决策的对称稳定性，可扩展至超 1300 万测试用例，同时推出 50K 条目的轻量子集 FairStress-Core 降低评测成本。实验覆盖 Olmo、Llama、Qwen、Gemma、Claude 及 GPT 系列等不同训练阶段的开源与闭源模型，发现多数存在“反刻板印象过度纠正”现象：当对抗前缀支持少数群体编码候选时，模型更易放弃证据更充分的正确决策，平均放弃正确决策的差距在隐含身份场景下达 6.9 个百分点，在明确身份标签场景下达 9.3 个百分点。该基准不覆盖基于历史歧视补偿的公平性定义。

rss · Hugging Face Blog · 10月20日 16:09

**「为什么重要」** 它首次将公平性评测从最终决策结果延伸到决策抗干扰的对称性，填补了现有基准仅测身份交换后最终选择的空白；目前该基准已开源可用，但尚未形成行业统一的公平性评估标准，其对高风险 LLM 部署的实际约束力仍待观察。

**「可关注」** 可关注：FairStress 的对抗前缀测试逻辑和 FairStress-Core 轻量子集可直接接入现有 LLM 评测 harness，补充传统公平性基准未覆盖的决策稳定性测试维度。

**标签**: `#eval`, `#harness`

---

<a id="item-agent-engineer-8"></a>
### [Cloudflare tsrs：TypeScript 编译器移植 Rust](https://blog.cloudflare.com/typescript-rust-port/) ⭐️ 6.0/10

2026 年 10 月 20 日，Cloudflare 公开 tsrs 项目，将 TypeScript 编译器移植到 Rust，用于适配仅支持 WASM 的沙箱运行环境。项目采用自定义 never-freed arena 内存模型，规避 Rust 无垃圾回收机制带来的移植障碍，公开性能对比显示其编译速度快于 Go 导出的 tsc WASM 版本。TypeScript 团队正与项目维护者合作，评估将相关优化 upstream 到 TypeScript 7.1，目前该项目对 AI Agent 工程师的核心工作流影响面较窄，属于编译器/工具链性能优化参考。

hackernews · hnisjafx40 · 10月20日 13:18 · [社区讨论](https://news.ycombinator.com/item?id=50165953)

**「为什么重要」** 该项目公开了 Rust arena 内存模型在编译器移植中的具体落地实践，同时是 AI 辅助完成大规模代码移植的公开案例；TypeScript 团队已启动优化评估，可能影响后续 TypeScript 编译器的性能迭代方向。

**「可关注」** 可关注：tsrs 通过 never-freed arena 模拟 GC 解决 Rust 无 GC 场景下的编译器移植障碍，同时该项目是 AI 辅助完成大规模代码移植的公开实践案例。

**「评论」** 社区认可 tsrs 的性能提升与 arena 内存模型的创新思路，TypeScript 团队已公开与维护者合作评估优化合并；部分开发者对 AI 生成的大规模移植代码的可维护性表示担忧，也有大型代码库使用者反馈当前 TypeScript 本地编译性能不足，期待优化落地。

**标签**: `#coding-agent`

---

<a id="item-agent-engineer-9"></a>
### [MemT-1.0 内存原生架构发布](https://huggingface.co/papers/2610.26825) ⭐️ 6.0/10

2026 年 10 月 21 日 Hugging Face Daily Papers 分享 MemT-1.0 研究，该工作提出将内存内化为基础模型计算一部分的 MemT-1.0 架构。架构基于 Metis，经过刻意的主干模型准备，采用 Gated DeltaNet-2 实现稳定 token 级内存更新，通过 Mixture-of-Storage 扩展原生内存容量，训练过程使用 34B tokens，采用持续预训练+后训练的两阶段流程，已发布 MemT-1.0-Nano 和 MemT-1.0-Flash 两个版本。当前仅公开摘要片段，缺少性能基准、Agent 专属评测及生产集成细节。

rss · Hugging Face Daily Papers · 10月21日 01:47

**「为什么重要」** 该架构将内存作为基础模型原生能力的设计方向，与 Agent 内存系统设计直接相关；但当前仅公开摘要，落地价值与性能表现需阅读全文验证。

**「可关注」** 可关注：MemT-1.0 的 token 级稳定内存更新机制与 Mixture-of-Storage 容量扩展设计，待全文公开后验证其对 Agent 内存管理的实际适配效果。

**标签**: `#memory`

---

<a id="item-agent-engineer-10"></a>
### [Ornith-1.5-122B 发布](https://www.reddit.com/r/LocalLLaMA/comments/1xatebw/ornithaiornith15122b_qwen_finetune/) ⭐️ 6.0/10

2026 年 10 月 20 日，Reddit 用户/u/jacek2023 发布 Ornith-1.5-122B 的公开信息，该模型为 Qwen 微调大模型，在 Ornith-1.0 基础上将端到端自改进循环从 scaffold 与 rollout 优化，扩展为联合优化任务生成、scaffold 构建、解决方案 rollout 三个环节，不再依赖固定人工整理的任务集与手动设计的 harness，相关权重已上传至 HuggingFace，包含 GGUF、NVFP4 等格式版本，未披露技术实现细节、性能基准，也未附上官方博客链接。

reddit · r/LocalLLaMA · /u/jacek2023 · 10月20日 14:19

**「为什么重要」** 该模型的自改进框架覆盖 coding agent 涉及的 harness、eval、编排等核心概念，绕开人工任务与手动 harness 的设计思路有潜在参考价值，但当前缺少技术细节与性能数据，实际效果尚未得到验证。

**「可关注」** 可关注其端到端自改进循环绕开固定人工任务和手动 harness 的设计思路，但需等待官方披露技术细节与性能基准后，再评估其在 coding agent 场景的落地可行性。

**标签**: `#harness`, `#eval`, `#orchestration`, `#coding-agent`

---

<a id="item-agent-engineer-11"></a>
### [llm-public-ai 0.1 发布](https://github.com/simonw/llm-public-ai/releases/tag/0.1) ⭐️ 5.8/10

simonw 于 2026-10-20 发布 llm-public-ai 0.1 初始版本。该版本为 LLM 工具添加对 Public AI 托管模型的支持。当前无技术细节、性能数据或架构说明。

github · simonw · 10月20日 15:45

**「可关注」** 可关注：llm-public-ai 0.1 为初始版本，当前仅确认支持 Public AI 托管模型，无性能数据或架构细节。

**标签**: `#toolchain`, `#llm`

---

## AI 日报
{: #sec-ai-daily .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-daily" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-daily-1"></a>
### [Terminal X 用 GPT-6.1 匹配投资者判断 88.6%](https://openai.com/index/terminal-x) ⭐️ 6.8/10

OpenAI 官方博客披露，Terminal X 的 Eval Agent 基于 GPT-6.1 Sol 运行，采用 54 项评分标准对基金投资相关输出进行评估，可多捕捉 25% 偏离基金投资 mandate 的情况。该条目标题声称该工具匹配高级投资者判断的准确率达 88.6%，但当前披露内容未提及该数据，也未说明 25% 提升的对比基线。

rss · OpenAI Blog · 10月20日 07:00

**「为什么重要」** 这是 GPT-6.1 Sol 在金融合规评估场景的公开落地案例，为同类 eval 工具的效果验证提供了可参考的标尺。

**「可关注」** 可关注：54 项评分标准下 GPT-6.1 Sol 在基金 mandate 合规校验场景的表现，以及后续公开的基线对比数据与 88.6% 准确率的测算说明。

**标签**: `#model`, `#industry`, `#eval`, `#product`

---

<a id="item-ai-daily-2"></a>
### [ChatGPT Work 餐饮客户案例发布](https://openai.com/index/ted-taylor-restaurant) ⭐️ 5.8/10

OpenAI 官方博客发布客户案例，独立经营 Schlotzsky’s 与 Cinnabon 的特许经营商用 ChatGPT Work 优化工作流，案例显示其现金对账耗时缩短 94%，菜单重新定价耗时缩短 95%，声称可释放 10 万美元现金流；该案例仅覆盖单个特许经营商用例，未披露更广泛的技术细节或落地规模。

rss · OpenAI Blog · 10月20日 10:00

**「为什么重要」** 这是 OpenAI 首次公开餐饮垂直场景下 ChatGPT Work 的具体效率数据，为行业工作流自动化提供了可参考的商用样本。

**「可关注」** 可关注：重复性财务、运营类任务在 ChatGPT Work 支持下的效率提升空间。

**标签**: `#industry`, `#product`

---

## AI 羊毛
{: #sec-ai-deals .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-deals" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-deals-1"></a>
### [全国在职教师可领 WorkBuddy 教育版一年免费](https://www.appinn.com/workbuddy-education/) ⭐️ 8.0/10

腾讯于 10 月 19 日正式发布 WorkBuddy 教育公益版，面向全国在职教师发放为期一年的免费使用权益，该 AI 助手可支持备课、制作课件、设计作业、家校沟通、学情分析等教学相关场景。

rss · 小众软件 · 10月20日 13:57

**「为什么重要」** 当前面向教师群体的专属 AI 教学工具免费权益较少，该版本预置教学专属场景，可降低教师日常办公的 AI 使用成本。

**「可关注」** 可关注：仅限全国在职教师领取，需核验教师身份，权益有效期为一年。

**标签**: `#promo`, `#free-tier`, `#limited-free`, `#edu`

---