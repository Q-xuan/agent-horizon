---
layout: default
title: "Horizon Summary: 2026-10-21 (EN)"
date: 2026-10-21
lang: en
---

> From 231 items, 17 important content pieces were selected

---

**Agent Harness Architecture**
1. [Cloudflare Agents 0.29.0 发布](#item-harness-arch-1) ⭐️ 7.8/10
2. [openai-agents-js 0.21.0 发布](#item-harness-arch-2) ⭐️ 7.8/10
3. [OpenHands v1.29.0 发布](#item-harness-arch-3) ⭐️ 6.8/10

**AI Agent Engineer**
1. [ALTK-Evolve 以 GPT-4.1 登顶 τ²-bench](#item-agent-engineer-1) ⭐️ 8.8/10
2. [DeepSeek 开源 DeepInfer 推理框架](#item-agent-engineer-2) ⭐️ 7.0/10
3. [OR-License 工业OR基准发布](#item-agent-engineer-3) ⭐️ 7.0/10
4. [Self-HPO 提出编码 Agent 自进化框架](#item-agent-engineer-4) ⭐️ 7.0/10
5. [Interlock 图框架提升长时程 Agent 完成](#item-agent-engineer-5) ⭐️ 7.0/10
6. [决策模型 Eval 使用指南](#item-agent-engineer-6) ⭐️ 7.0/10
7. [FairStress 公平性基准发布](#item-agent-engineer-7) ⭐️ 6.8/10
8. [Cloudflare tsrs 项目发布](#item-agent-engineer-8) ⭐️ 6.0/10
9. [HF 每日论文：MemT-1.0 发布](#item-agent-engineer-9) ⭐️ 6.0/10
10. [Ornith-1.5-122B 发布 Qwen微调自改进](#item-agent-engineer-10) ⭐️ 6.0/10
11. [simonw/llm-public-ai 0.1 发布](#item-agent-engineer-11) ⭐️ 5.8/10

**AI Daily**
1. [Terminal X 用 GPT-6.1 Sol 提升合规检出](#item-ai-daily-1) ⭐️ 6.8/10
2. [特许经营商用 ChatGPT Work 降本](#item-ai-daily-2) ⭐️ 5.8/10

**AI Deals**
1. [腾讯WorkBuddy教育版教师免费领一年](#item-ai-deals-1) ⭐️ 8.0/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [Cloudflare Agents 0.29.0 发布](https://github.com/cloudflare/agents/releases/tag/agents%400.29.0) ⭐️ 7.8/10

Cloudflare Agents 0.29.0 正式发布。Agent Skills 必须改用 @cloudflare/computer Workspace 处理投影与 skills.runner\(\) 状态操作，旧方式失效。Browser 工具改用类型化 binding 的 acquire\(\) 与 closeSession\(\) 管理 Run 会话，本地开发回退到 HTTP API。createAI 支持 \{ accountId, apiToken \} 直连配置以跨账号运行或脱离 Worker，转录改用 @cf/deepgram/nova-3，支持流式断点续传，并移除对 AI Gateway Universal Endpoint 的依赖。

github · github-actions\[bot\] · Oct 20, 15:20

**「设计要点」** Agent Skills 的状态读写统一迁移至 @cloudflare/computer Workspace，投影与运行期共享同一存储层。Browser 工具通过类型化 binding API 管理会话生命周期，本地开发无 binding 时降级为 HTTP 调用。createAI 支持直连配置绕过 Worker 内 binding 限制，模型路由切换至 provider-native 路径。

**「改了什么」** Agent Skills 强制迁移至 @cloudflare/computer Workspace，旧投影与 runner 调用方式破坏。Browser 工具会话管理改为类型化 acquire/closeSession，本地开发自动回退 HTTP。createAI 新增跨账号 gateway 配置、Deepgram nova-3 转录、流式断点续传，移除对 AI Gateway Universal Endpoint 的依赖。

**Tags**: `#tools`, `#runtime`, `#memory`

---

<a id="item-harness-arch-2"></a>
### [openai-agents-js 0.21.0 发布](https://github.com/openai/openai-agents-js/releases/tag/%40openai/agents-core%400.21.0) ⭐️ 7.8/10

\`@openai/agents-core\` 0.21.0 发布。Runloop sandbox provider 已移除，需按迁移指南切换替代方案。运行时修复嵌套数值型 token 用量明细在流式运行、用量核算和保存状态中的保持问题，schema 升至 1.23 并向后兼容旧快照。sandbox 动态压缩阈值新增识别 GPT-6 Astra、Sol、Luna 及 GPT-6.1 Sol。

github · openai-sdks\[bot\] · Oct 20, 22:07

**「设计要点」** sandbox 提供者从核心包移除，公共 API 同步下线。运行时 token 核算链路改为保持边界嵌套的数值型用量明细，调用方需将值收窄为数值类型后再做算术。

**「改了什么」** 移除 Runloop sandbox provider 及其公共 API，提供官方迁移路径。修复嵌套数值 token 用量明细在流式运行和保存状态中的丢失，schema 1.23 保持向后读取，sandbox 动态压缩阈值支持 GPT-6 Astra、Sol、Luna 和 GPT-6.1 Sol。

**Tags**: `#sandbox`, `#runtime`

---

<a id="item-harness-arch-3"></a>
### [OpenHands v1.29.0 发布](https://github.com/OpenHands/OpenHands/releases/tag/v1.29.0) ⭐️ 6.8/10

OpenHands 官方发布 v1.29.0，核心新增 agent 配置文件的 per-profile 多维度配置能力。支持按 profile 选择技能、配置冷凝器与验证规则、选择 Model Router，并让 profile 独立拥有设置。同时优化后端选择器显示完整组织名、启动器读取 bundled 扩展公共技能，以及多项 UI 与云同步修复。

github · openhands-release-bot\[bot\] · Oct 20, 22:22

**「改了什么」** 相对 v1.28.1，v1.29.0 将 agent 配置从全局拆到 per-profile 维度，新增技能、冷凝器、验证规则和模型路由的 profile 级选择；启动器读取 bundled 扩展公共技能，后端选择器展示完整组织名，uvx 锁定 Python 3.12-3.14。修复了云对话仓库关联保存、浅色主题 git 图标、模型同步延迟从十秒降至一秒等 10 个问题。

**Tags**: `#agent-profiles`, `#skills`, `#memory`, `#model-routing`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [ALTK-Evolve 以 GPT-4.1 登顶 τ²-bench](https://huggingface.co/blog/ibm-research/altk-evolve-bc) ⭐️ 8.8/10

IBM Research 于 2026-10-20 发布 ALTK-Evolve，该方法将智能体在训练任务上的成功与失败轨迹蒸馏为简短行为准则，追加到基础 ReAct 智能体的系统提示中。使用 GPT-4.1 在 τ²-bench 零售基准上达到 67.5% Pass^4（4 次独立尝试全部成功），超过 2026-10-12 排行榜所有条目，且未更新模型权重或使用人工标注。在航空域中，高支持度准则子集（sup3，14 条）将 Pass^4 从 35.0% 提升至 45.0%，而全量准则（lossless，101 条）虽将平均准确率提升至 65.0%，但 Pass^4 降至 40.0%。准则增加输入 token 成本（零售 lossless 单次对话成本 +65%），但不增加对话轮数。

rss · Hugging Face Blog · Oct 20, 15:19

**「为什么重要」** 它表明非推理模型可通过学习到的提示准则而非模型规模登顶严格策略评估排行榜。零售与航空域对准则剂量的最优选择相反（零售需全量准则，航空需高支持度子集），说明准则数量是需按域调优的旋钮，而非固定常量。

**「可关注」** 可关注：准则蒸馏同时提升平均准确率与 Pass^4 可靠性，且成本增量仅来自输入 token，不增加对话轮数；但准则剂量需按域调优，零售需全量准则而航空域高支持度子集在可靠性上更优。

**Tags**: `#memory`, `#eval`, `#harness`, `#coding-agent`

---

<a id="item-agent-engineer-2"></a>
### [DeepSeek 开源 DeepInfer 推理框架](https://github.com/deepseek-ai/DeepInfer) ⭐️ 7.0/10

2026年10月20日，DeepSeek 在 GitHub 开源了专为其模型系列设计的高性能推理框架 DeepInfer，仓库地址为 https://github.com/deepseek-ai/DeepInfer，属于 AI 推理工具链组件。社区存在未经验证的声称，称该框架支撑 DeepSeek V4.1 Flash 实现单集群日吞吐 155 万亿 token、单卡每小时收入 38 美元（非高峰定价），但官方未披露相关技术细节与性能基准。该框架主要面向需要部署 DeepSeek 模型的工程师与 AI 推理优化团队。

hackernews · ggcr · Oct 20, 09:08 · [Discussion](https://news.ycombinator.com/item?id=50163277)

**「为什么重要」** 这是 DeepSeek 首次公开官方自有模型的高性能推理框架，补齐了其模型部署工具链的公开组件。社区提及的高吞吐若经官方验证，可为大模型推理成本优化提供新参考，但目前无官方数据支撑该性能声称。

**「可关注」** 可关注该框架的多硬件适配进展，目前社区提及其已支持华为昇腾 950 NPU，可跟进官方后续披露的性能基准数据。

**「评论」** 社区讨论存在明显分化：一部分用户关注框架对打破英伟达推理生态垄断、降低中小实验室部署成本的潜在价值；另一部分讨论围绕该开源项目发布时间与美国 DHS 相关禁令的时间关联展开政治性推测，未形成技术层面的共识。

**Tags**: `#inference`, `#toolchain`, `#open-source`

---

<a id="item-agent-engineer-3"></a>
### [OR-License 工业OR基准发布](https://huggingface.co/papers/2610.24087) ⭐️ 7.0/10

2026-10-21，Hugging Face Daily Papers 介绍 OR-License 端到端基准。该基准含 31 个实例、10 个工业场景，源自付费 OR engagements 总计 USD 3.68M，保留原始需求、输入数据、交付格式及去识别后的信息边界。论文同步提出 ORSim 受控客户端模拟器，仅披露业务事实而不提供 OR 专业知识，用于研究 agent 信息获取能力。该资源面向领域特定 agent 系统工程师，但当前材料截断，未提供性能对比数据。

rss · Hugging Face Daily Papers · Oct 21, 01:47

**「为什么重要」** 该基准使用真实脱敏客户材料而非合成任务，填补现有 OR 基准在业务材料翻译环节的空白。对构建领域特定 agent 系统的工程师而言，这是少有的生产对齐评估资源，但实际性能表现尚待完整论文验证。

**「可关注」** 现有 OR 基准多从自包含描述或预定义优化任务起步，OR-License 要求 agent 直接处理原始业务材料，这对信息抽取与任务翻译链路提出更高要求。

**Tags**: `#eval`, `#orchestration`

---

<a id="item-agent-engineer-4"></a>
### [Self-HPO 提出编码 Agent 自进化框架](https://huggingface.co/papers/2610.22791) ⭐️ 7.0/10

一篇研究论文提出 Self-HPO，一种用于编码 Agent 的递归自改进框架，交替优化 harness 与 policy。该框架以演化中的策略作为自身的 harness 生成器，避免单独优化单一组件导致的次优问题。论文指出 harness 与 policy 相互强化：为某一策略 checkpoint 调优的 harness 可能无法针对更新后策略的失败模式，而策略学习也受限于固定 harness 所采集的轨迹。该文发布于 2026-10-21 的 Hugging Face Daily Papers，但可用摘要未提供具体性能基准数据。

rss · Hugging Face Daily Papers · Oct 21, 01:47

**「为什么重要」** 该工作直接针对编码 Agent 工程中的核心张力——策略模型与评估 harness 的协同演化。它提供了联合优化的具体算法思路，可能影响工程师设计编码 Agent 迭代改进循环的方式。目前缺乏完整性能验证，实际效果尚未证实。

**「可关注」** 可关注：在设计编码 Agent 评估系统时，harness 与 policy 的协同演化可能需要交替优化调度，而非独立调优。

**Tags**: `#coding-agent`, `#harness`, `#eval`, `#orchestration`

---

<a id="item-agent-engineer-5"></a>
### [Interlock 图框架提升长时程 Agent 完成](https://huggingface.co/papers/2610.19686) ⭐️ 7.0/10

Hugging Face Daily Papers 于 2026-10-21 介绍 arXiv 预印本《Interlock: From Local Correctness to Task Completion in Long-Horizon Agents》。该论文提出 Interlock，一种图结构任务合成框架，将任务表示为类型化完成图（typed completion graph），通过 grounding edges、coupling hyperedges 与 realization edges 等结构显式建模环境证据、决策与所需效果之间的依赖关系。框架针对长时程 LLM agent 的常见失败模式——局部步骤正确但整体任务不完整——提供结构化解决方案。当前材料为截断的摘要片段，未包含实证性能数据、实现细节或与基线系统的量化对比，实际效果尚未验证。该工作主要影响 agent 编排、架构设计与长时程任务评估领域的研究者与工程师。

rss · Hugging Face Daily Papers · Oct 21, 01:47

**「为什么重要」** 长时程 agent 的局部正确但整体不完整是当前部署中的常见痛点，Interlock 提出的显式关系建模提供了一种可检验的架构方向。但论文仅提供概念框架，缺乏实现与评测，其实际收益仍需后续实证研究确认。

**「可关注」** 可关注：类型化完成图与耦合超边的设计可能为长时程任务的状态追踪与跨组件依赖约束提供新的建模原语，但当前缺乏可执行实现与性能基准，尚无法直接用于工程决策。

**Tags**: `#orchestration`, `#coding-agent`, `#eval`

---

<a id="item-agent-engineer-6"></a>
### [决策模型 Eval 使用指南](https://hamel.dev/blog/posts/decision-model-evals/) ⭐️ 7.0/10

本文分享了使用决策模型做自动化二分类eval的实践，测试了Jev 1.13、Perplexity Decider 1.1 27B、Liquid d1/d1-ultra、Cloudflare Clef Flash、OpenAI Decisions \(GPT-6 Luna\)共6款模型，数据集为100条公寓租赁agent的对话trace，任务是识别包含失败（如预订失败、未转人工）的trace。核心结论包括：默认0.5决策阈值可能不适用具体任务，需结合业务对精确率、召回率的要求调优，调优过程采用分层五折交叉验证且各模型使用相同数据splits，本次调优要求精确率和召回率均不低于80%；调优后Perplexity Decider每100次eval成本0.82美分，F1 0.79，OpenAI Decisions F1 0.87，成本3.72美分每100次，约为前者的4.5倍；决策模型输出的概率需经过校准才能作为可靠的置信度估计，校准分析中每个统计点对应约20条相似分数的trace。实验未纳入延迟对比，因延迟受实验外因素影响。实践覆盖eval pipeline和agent harness工程师群体。

rss · Hamel Husain · Oct 20, 07:00

**「为什么重要」** 当前决策模型品类快速扩张，但多数工程师直接使用默认阈值和原始概率输出，这篇提供了可直接复用的阈值调优、成本性能选型、概率校准方法，直接降低eval pipeline的搭建和调优成本。

**「可关注」** 可关注：决策模型eval不要直接使用默认0.5阈值，需结合业务对精确率、召回率的最低要求调优，再通过成本-F1帕累托前沿选择适配的模型。

**Tags**: `#eval`, `#observability`, `#harness`

---

<a id="item-agent-engineer-7"></a>
### [FairStress 公平性基准发布](https://huggingface.co/blog/allenai/fairstress) ⭐️ 6.8/10

Hugging Face 与 Allen AI 于 2026-10-20 发布 FairStress 公平性评测基准。该基准包含 300 个高风险决策场景，覆盖 29 个领域，并扩展为 1300 万+测试用例，通过“对抗性前缀”压力测试测量 LLM 在人口统计公平性上的隐藏不对称。实验覆盖 15 个模型（包括 Olmo、Llama、Qwen、Gemma、Claude、GPT 系列及 Tülu 3.1 8B），发现当说服性论证支持少数群体编码候选人时，模型更易放弃原本正确的选择，平均差距为 6.9（隐含身份）至 9.3（显式标签）个百分点，文中称此现象为“反刻板印象过度纠正”。5 万项子集 FairStress-Core 已集成至 Olmo-eval 开源评测工作台，但基准不涵盖基于历史补偿的公平定义。

rss · Hugging Face Blog · Oct 20, 16:09

**「为什么重要」** 该基准首次系统量化了模型在说服性挑战下的公平性退化，为高风险决策场景的模型选型提供新维度。但反刻板印象过度纠正是否构成实际危害仍需领域特定验证。

**「可关注」** 可关注：对抗性前缀揭示的决策稳定性差异补充了静态身份交换测试，评测 harness 可纳入此类压力测试以覆盖高风险场景。

**Tags**: `#eval`, `#harness`

---

<a id="item-agent-engineer-8"></a>
### [Cloudflare tsrs 项目发布](https://blog.cloudflare.com/typescript-rust-port/) ⭐️ 6.0/10

Cloudflare 于 2026 年 10 月 20 日发布 tsrs 项目，将 TypeScript 编译器移植至 Rust，核心目标是为仅支持 WASM 的沙箱提供可运行的 TS 编译器，避免 Go 移植 tsc 带来的完整 Go 运行时开销，附带实现比 Go 版更快的编译性能；项目采用自定义 never-freed arena 内存模型解决 Rust 无原生 GC 下的内存管理问题，TypeScript 团队正与维护者合作验证优化安全性，计划将部分优化 upstream 至 TypeScript 7.1。

hackernews · hnisjafx40 · Oct 20, 13:18 · [Discussion](https://news.ycombinator.com/item?id=50165953)

**「为什么重要」** 当前公开信息仅表明该项目属于编译器/工具链性能优化参考，对 AI Agent 工程师的 agent、harness、eval 等核心工作流影响面较窄；若后续 TS 7.1 合入相关优化，大型 TypeScript 项目的本地编译耗时有望降低，但该影响尚未证实。

**「可关注」** 可关注：tsrs 采用 never-freed arena 模拟 GC 的方案，解决了 Rust 无原生 GC 环境下移植 GC 语言编译器的内存管理重构问题，该思路可参考用于 WASM 沙箱内的工具链性能优化场景。

**「评论」** 社区讨论存在分歧：部分开发者认可编译速度提升对大型 TypeScript 项目的实用价值，也有开发者担忧 AI 生成的大规模移植代码的可维护性；TypeScript 团队已公开确认正与维护者合作验证优化安全性。

**Tags**: `#coding-agent`

---

<a id="item-agent-engineer-9"></a>
### [HF 每日论文：MemT-1.0 发布](https://huggingface.co/papers/2610.26825) ⭐️ 6.0/10

2026年10月21日Hugging Face Daily Papers分享了MemT-1.0内存原生基础模型架构研究。该架构将内存内化为模型计算的一部分，基于Metis采用Gated DeltaNet-2实现稳定token级内存更新，引入Mixture-of-Storage扩展原生内存容量，训练过程使用34B tokens，分为继续预训练和后训练两阶段，目前已发布MemT-1.0-Nano和MemT-1.0-Flash两个版本。当前公开信息仅包含摘要片段，缺少性能基准、Agent专属评测及生产集成细节。

rss · Hugging Face Daily Papers · Oct 21, 01:47

**「为什么重要」** 该工作探索了将内存内化为基础模型原生能力的架构方向，与Agent内存系统设计存在潜在关联，但当前公开信息仅覆盖架构设计与训练框架，缺少性能基准与Agent场景适配细节，落地价值尚需全文验证。

**「可关注」** 可关注：MemT-1.0的内存内化架构方向与Agent内存系统设计存在关联，但需等待全文公开的性能基准与Agent专属评测结果，再评估落地可行性。

**Tags**: `#memory`

---

<a id="item-agent-engineer-10"></a>
### [Ornith-1.5-122B 发布 Qwen微调自改进](https://www.reddit.com/r/LocalLLaMA/comments/1xatebw/ornithaiornith15122b_qwen_finetune/) ⭐️ 6.0/10

2026年10月20日，Reddit用户/u/jacek2023发布Ornith-1.5-122B公告，该模型为基于Qwen的微调大模型，是Ornith-1.0的升级版本。Ornith-1.5将自改进循环从原有的scaffold与rollout优化，扩展为联合优化任务生成、scaffold构建、解决方案rollout三个环节，不再依赖固定人工整理的任务集与手动设计的harness，通过强化学习持续生成新训练任务、发现有效解决策略、迭代优化模型策略。目前模型权重已在HuggingFace发布，提供GGUF、NVFP4等版本，官方博客未附带具体技术细节与性能基准数据。

reddit · r/LocalLLaMA · /u/jacek2023 · Oct 20, 14:19

**「为什么重要」** 该模型首次将自改进范围覆盖coding agent相关的任务生成、harness构建、rollout全链路，为自动化agent训练与评估提供了新的设计参考，但目前缺乏公开性能基准与官方技术细节，实际效果尚未得到验证。

**「可关注」** 可关注：其端到端自改进框架绕开固定人工任务与手动harness，联合优化任务生成、scaffold构建与rollout全链路的实现思路。

**Tags**: `#harness`, `#eval`, `#orchestration`, `#coding-agent`

---

<a id="item-agent-engineer-11"></a>
### [simonw/llm-public-ai 0.1 发布](https://github.com/simonw/llm-public-ai/releases/tag/0.1) ⭐️ 5.8/10

simonw 于 2026-10-20 发布 llm-public-ai 0.1 初始版本。该版本为 LLM 工具链新增 Public AI 托管模型支持，用户可通过该插件访问 publicai.co 上的模型。当前无技术细节、性能基准或架构说明，影响面限于使用 Public AI 模型的开发者。

github · simonw · Oct 20, 15:45

**「为什么重要」** 这是 Public AI 模型首次进入 simonw 的 LLM 工具生态，但缺乏性能与兼容性说明，实际接入成本尚不明确。

**「可关注」** 该插件目前仅声明支持 Public AI，未公开模型调用格式、鉴权方式及延迟基准，接入前需自行验证兼容性。

**Tags**: `#toolchain`, `#llm`

---

## AI Daily

<a id="item-ai-daily-1"></a>
### [Terminal X 用 GPT-6.1 Sol 提升合规检出](https://openai.com/index/terminal-x) ⭐️ 6.8/10

OpenAI官方博客报道，Terminal X的Eval Agent接入GPT-6.1 Sol模型，采用54项评分rubric对输出进行评级，可多检出25%偏离基金投资mandate的情况。当前披露内容未说明25%提升的对比基线，也未解释标题提及的88.6%资深投资者判断匹配率的来源。

rss · OpenAI Blog · Oct 20, 07:00

**「可关注」** 可关注：Terminal X基于54项rubric的合规偏离检测方案可作为金融领域模型效果验证的参考范式。

**Tags**: `#model`, `#industry`, `#eval`, `#product`

---

<a id="item-ai-daily-2"></a>
### [特许经营商用 ChatGPT Work 降本](https://openai.com/index/ted-taylor-restaurant) ⭐️ 5.8/10

OpenAI 发布客户案例，显示一家独立 Schlotzsky&\#x27;s 与 Cinnabon 特许经营商使用 ChatGPT Work 将现金对账时间缩短 94%，菜单重新定价时间缩短 95%。该案例声称释放 10 万美元现金流。此案例仅代表单一客户用例，未涉及更广泛模型发布或技术细节。

rss · OpenAI Blog · Oct 20, 10:00

**「为什么重要」** OpenAI 官方博客发布餐饮行业客户案例，展示 ChatGPT Work 在运营自动化中的效率提升声明。但该案例仅为单一特许经营商用例，尚未形成普遍验证。

**「可关注」** 可关注：单一特许经营商用例显示 ChatGPT Work 可将现金对账时间缩短 94%，菜单重新定价时间缩短 95%。

**Tags**: `#industry`, `#product`

---

## AI Deals

<a id="item-ai-deals-1"></a>
### [腾讯WorkBuddy教育版教师免费领一年](https://www.appinn.com/workbuddy-education/) ⭐️ 8.0/10

腾讯向全国在职教师发放为期一年的WorkBuddy教育公益版AI助手，可用于备课、制作课件、设计作业、家校沟通、学情分析等教学相关场景，该产品由腾讯SSV数字教育实验室与WorkBuddy团队联合研发。

rss · 小众软件 · Oct 20, 13:57

**「为什么重要」** 该权益为腾讯官方发布的全国在职教师专属公益福利，发放主体、适用场景均明确，属于可核对的群体专属福利，符合羊毛栏收录标准。

**「可关注」** 可关注：全国在职教师可申领为期一年的WorkBuddy教育公益版AI助手，覆盖备课、课件制作等教学相关场景。

**Tags**: `#promo`, `#free-tier`, `#limited-free`, `#edu`

---