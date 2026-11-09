---
layout: default
title: "Horizon Summary: 2026-11-10 (EN)"
date: 2026-11-10
lang: en
---

> From 215 items, 16 important content pieces were selected

---

**Agent Harness Architecture**
1. [browser-use 1.0.0rc4 发布](#item-harness-arch-1) ⭐️ 8.8/10
2. [Goose v1.58.0 发布](#item-harness-arch-2) ⭐️ 6.8/10
3. [Claude Code v2.1.321 发布](#item-harness-arch-3) ⭐️ 5.5/10
4. [Google Agent Skills 仓库登 GitHub Trending](#item-harness-arch-4) ⭐️ 5.0/10

**AI Agent Engineer**
1. [HF Daily Paper: Agent Harness 进化权衡](#item-agent-engineer-1) ⭐️ 7.0/10
2. [Frontier3DBench 统一 3D 编码智能体评估](#item-agent-engineer-2) ⭐️ 7.0/10
3. [Nemotron 日本金融合成数据集发布](#item-agent-engineer-3) ⭐️ 6.3/10
4. [FinDendro Benchmark Tests LLM Temporal Knowledge](#item-agent-engineer-4) ⭐️ 6.0/10
5. [HF 每日论文：权重空间编程研究](#item-agent-engineer-5) ⭐️ 6.0/10

**AI Daily**
1. [Anthropic 发布 Claude Fable 5.2 与 Mythos 5.2](#item-ai-daily-1) ⭐️ 9.8/10
2. [Pathways 单控制器训练系统 GA](#item-ai-daily-2) ⭐️ 8.8/10
3. [OpenAI 发布 Control Room](#item-ai-daily-3) ⭐️ 8.3/10
4. [ChatGPT Enterprise 上线 AWS Marketplace](#item-ai-daily-4) ⭐️ 7.8/10
5. [Google AI Studio 支持自然语言构建地图应用](#item-ai-daily-5) ⭐️ 7.8/10
6. [MaxText 支持 TPU 长上下文训练](#item-ai-daily-6) ⭐️ 7.8/10
7. [Kuken 搜70年图纸降至4.5分钟](#item-ai-daily-7) ⭐️ 6.3/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [browser-use 1.0.0rc4 发布](https://github.com/browser-use/browser-use/releases/tag/1.0.0rc4) ⭐️ 8.8/10

browser-use 发布 1.0.0rc4，这是 1.0 首个可用候选版本。核心运行时从逐步 DOM 快照动作选择重写为持久 Python REPL 代码执行，基于 browser-harness 助手、原始 CDP 与 Pydantic AI。常用 0.x 公开 API（Agent、Browser、Tools、run\(\)、final\_result\(\)）保持向后兼容。需 Python 3.11+，显式安装 \`--pre\` 或 \`--prerelease allow\`，默认 pip 仍安装 0.13.14 直至 1.0.0 正式发布。

github · gregpr07 · Nov 9, 20:55

**「设计要点」** 运行时改为持久 REPL，模型通过 Pydantic AI 驱动，浏览器控制混合使用 browser-harness 助手与原始 CDP。默认走 Browser Use Cloud 浏览器，本地 Chromium 需显式指定 \`Browser\(&\#x27;chromium&\#x27;\)\`。结果对象统一携带 structured\_output、downloads、cost\_usd 等字段，工具结果始终保留在对话中，不再支持 include\_in\_memory 过滤。

**「改了什么」** 核心执行模型从逐步 DOM 转储改为持久 Python REPL，代码行数从 68,815 降至 13,154。默认浏览器切至云端，模型默认改为 bu-fast，max\_steps 默认值从 500 降至 100，timeout 1700 秒。认证统一为 Browser Use key（BROWSER\_USE\_API\_KEY）。新增结构化输出、文件上传下载、敏感数据脱敏、域名限制、联网搜索，CLI 与 MCP 工具集重构，console 脚本从 bu/browser 合并为 browser-use/browseruse。

**Tags**: `#runtime`, `#tools`

---

<a id="item-harness-arch-2"></a>
### [Goose v1.58.0 发布](https://github.com/aaif-goose/goose/releases/tag/v1.58.0) ⭐️ 6.8/10

Goose agent harness 发布 v1.58.0。本次更新新增上下文相关性操作、上下文窗口报告与查看器，以及 AIHubMix、RouterPlex、Lemonade 三个声明式模型提供商支持。运行时修复了工具轮次推理重放、会话重放快速路径、Bedrock 无文档块模型回退、429 Retry-After 处理等 bug，并将 Agent 与 AgentManager 合并为每进程一个 StateMachineServices。桌面端新增 thinking 折叠默认设置，同时移除 jsonwebtoken 依赖并升级 zstd 至 0.14.3。

github · github-actions\[bot\] · Nov 9, 19:07

**「设计要点」** 每进程将 Agent 与 AgentManager 合并为单一 StateMachineServices，简化状态管理。桌面端会话重放保留快速路径，ACP 客户端委托开发工具被移除，工具调用标题去特定化。

**「改了什么」** 新增上下文相关性操作、上下文窗口报告、三个新提供商及 thinking 折叠默认开关。修复工具轮次推理重放、会话重放性能、Bedrock 回退逻辑、429 限流处理、OpenRouter 上下文溢出分类等运行时问题，移除 jsonwebtoken 依赖。

**Tags**: `#runtime`, `#tools`, `#context`, `#providers`

---

<a id="item-harness-arch-3"></a>
### [Claude Code v2.1.321 发布](https://github.com/anthropics/claude-code/releases/tag/v2.1.321) ⭐️ 5.5/10

Claude Code v2.1.321 发布，默认模型切换至 Claude Fable 5.2（1M 上下文，$8/$40 per Mtok）。修复 MCP OAuth 重定向泄露 refresh token 的安全漏洞，以及多例 sandbox 逃逸、权限判断错误、网络路径编辑异常等 bug。新增 \`claude remote-control --settings &lt;file&gt;\` 支持批量应用会话配置。

github · claude-code-publisher\[bot\] · Nov 9, 19:22

**「设计要点」** Claude Code 通过 MCP 协议扩展工具生态，使用 sandbox 隔离 Bash 执行，以 PreToolUse/PostToolUse hook 链实现权限拦截。Remote Control 维持 WebSocket 长连接，支持会话级设置继承与后台子代理报告传递。

**「改了什么」** 默认模型切换至 Claude Fable 5.2，上下文窗口扩至 1M。MCP 客户端修复 OAuth 重定向时向第三方主机发送 refresh token 的漏洞。sandbox 层修复只读 Bash 无提示逃逸、权限判断目录错位、\`cp\`/\`mv\` 目标文件未受保护文件规则约束等问题。Remote Control 新增 \`--settings\` 参数实现配置热加载。

**「评论」** 无社区评论。

**Tags**: `#runtime`, `#mcp`, `#sandbox`, `#permissions`, `#tools`

---

<a id="item-harness-arch-4"></a>
### [Google Agent Skills 仓库登 GitHub Trending](https://github.com/google/skills) ⭐️ 5.0/10

2026年11月9日，Google 开源的 \`google/skills\` 仓库登上 GitHub Trending，该仓库提供面向 Google 产品与技术的 Agent Skills，支持将 Google 服务集成到各类 agent 系统中，当前已覆盖 Google Cloud 等产品。公开资料仅披露基础安装与更新指引，未提供技术架构、代码实现或官方变更日志。用户可通过 \`npx skills add google/skills\` 完成安装，安装时可选择特定技能、目标 agent 及安装范围（项目级或全局），无 npx 环境需先安装 Node.js。

rss · GitHub Trending Daily · Nov 9, 23:00

**Tags**: `#tools`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [HF Daily Paper: Agent Harness 进化权衡](https://huggingface.co/papers/2611.07624) ⭐️ 7.0/10

A Hugging Face Daily Paper from 2026-11-09 analyzes agent harness evolution enabling recursive self-improvement without model weight updates. Evaluating four methods across harnesses, general tasks, and coding tasks, the study finds all sixteen evolved agents gained previously uncovered tasks while losing previously covered ones. In one general-task case, reliability rose by 5.2 points despite losing ten previously covered tasks, and most reliability gains increased deployment cost. Specific interventions usually outperformed generic reminders, though their benefits changed when combined.

rss · Hugging Face Daily Papers · Nov 9, 00:00

**「为什么重要」** This research provides empirical evidence that benchmark score improvements in agent harnesses often involve tradeoffs with task coverage and deployment cost, directly relevant to engineers designing and evaluating coding agents. The finding that specific changes outperform generic reminders offers a concrete optimization direction, while the variable effects of combining interventions indicate unresolved complexity in harness design.

**「可关注」** When optimizing agent harnesses, specific component interventions generally outperform generic reminders, but combined effects should be validated as benefits may shift with different combinations.

**Tags**: `#harness`, `#eval`, `#coding-agent`, `#orchestration`

---

<a id="item-agent-engineer-2"></a>
### [Frontier3DBench 统一 3D 编码智能体评估](https://huggingface.co/papers/2611.09017) ⭐️ 7.0/10

Frontier3DBench 是一个统一基准，覆盖 145 个任务、9 个类别，面向对象、场景和交互式开放世界 3D 创建。它联合评估外观、结构和行为，测试 11 个模型-harness 配置。实验显示 GPT-6.1-sol 在对象和场景层级领先，总分 66.02/100。该基准面向编码智能体、harness 及评估开发者，填补现有碎片化基准的空白。

rss · Hugging Face Daily Papers · Nov 9, 00:00

**「为什么重要」** 现有 3D 编码智能体基准碎片化，缺乏跨层级统一评估。Frontier3DBench 提供可复现的对比基线，但 11 个配置的性能差异是否稳定仍需更多实验验证。

**「可关注」** 可关注：Frontier3DBench 的 11 个模型-harness 配置在对象、场景和交互式开放世界层级表现分化，提示评估结果依赖具体组合。

**Tags**: `#eval`, `#coding-agent`, `#harness`

---

<a id="item-agent-engineer-3"></a>
### [Nemotron 日本金融合成数据集发布](https://huggingface.co/blog/nvidia/nemotron-personas-finance-japan) ⭐️ 6.3/10

2026年11月9日，NVIDIA与Elith联合发布开源合成数据集Nemotron-Personas-Finance-Japan，这是首个百万级日本金融领域开放合成人格数据集，基于日本官方人口、劳动力、家庭财务及金融素养统计数据生成，采用NeMo SDG-PGMs与NeMo Data Designer构建，所有记录均为完全合成、不映射真实个人以降低隐私风险，单数据集含900万条人格记录、50个字段，总token约15亿，较前代Nemotron-Personas-Japan记录量多50%、字段数从22个提升至50个，采用CC BY 4.0许可可商用，主要面向日本金融机构、相关初创企业及集成商，用于金融AI开发、用户模拟、模型评测等场景，同时可与NeMo User Sim框架无缝集成。

rss · Hugging Face Blog · Nov 9, 15:05

**「为什么重要」** 该数据集填补了日本金融场景大规模开源合成人格数据的空白，采用CC BY 4.0许可可商用，降低了金融AI开发过程中使用真实数据的隐私合规门槛；其对日本金融Agent的实际评测与开发效果，仍有待后续用户验证。

**「可关注」** 可关注：该数据集可与NeMo User Sim框架直接集成，支持基于真实世界分布的用户模拟，适合需要合规测试日本金融场景AI Agent的团队快速搭建评测环境。

**Tags**: `#eval`, `#synthetic-data`, `#finance`

---

<a id="item-agent-engineer-4"></a>
### [FinDendro Benchmark Tests LLM Temporal Knowledge](https://huggingface.co/papers/2611.06808) ⭐️ 6.0/10

On 2026-11-09, Hugging Face Daily Papers highlighted FinDendro, a new benchmark of 2,226 dated U.S. facts spanning 1999–2026 to evaluate LLM temporal self-knowledge for financial backtesting. The benchmark covers monthly macroeconomic series, month-end stock prices, and Federal Reserve decisions, generating four prompt types per fact: value questions, Recall and Predict questions without declared dates, and Predict questions with historical dates. The source material is truncated and drawn from a curated feed rather than the original paper, limiting actionable detail.

rss · Hugging Face Daily Papers · Nov 9, 00:00

**「Why It Matters」** The work addresses a reliability gap for time-sensitive agent tasks by testing whether standard safeguards—vendor-stated knowledge cutoffs, self-reported knowledge, or date-conditioned prompting—actually prevent data leakage in financial backtesting. However, the niche financial use case and truncated source content constrain immediate broad applicability without access to the full paper.

**「Engineer Takeaway」** Time-sensitive agent tasks require explicit temporal boundary validation rather than reliance on vendor-stated knowledge cutoffs or self-reported awareness.

**Tags**: `#eval`

---

<a id="item-agent-engineer-5"></a>
### [HF 每日论文：权重空间编程研究](https://huggingface.co/papers/2611.09382) ⭐️ 6.0/10

2026年11月9日Hugging Face每日论文频道公开了一篇关于Weight-Space Programming（WSP，无梯度模型适配方法）的预印本研究截断摘要。该研究在Qwen3.5-0.8B与Qwen3.5-9B两个模型规模上，通过16条编辑轨迹覆盖7个基准开展系统性实验，结果显示仅修改1023个参数即可在MATH-500上实现最高29.45个百分点的准确率提升，同时在GPQA Diamond、IFEval、SciBench等基准上也取得4.42至36.72个百分点的性能增益。当前公开摘要未呈现完整核心洞见与详细限制，该研究目前仅对从事模型适配、推理评估的agent工程师有初步参考价值，生产端落地采用度极窄。

rss · Hugging Face Daily Papers · Nov 9, 00:00

**「为什么重要」** 该研究首次公开了无梯度参数级模型适配在多类推理与指令遵循基准上的量化提升结果，为agent工程师提供了模型适配的新思路参考；但受限于摘要内容截断，其泛化能力、实际落地限制等关键信息尚未公开，暂无法评估生产可用性。

**「可关注」** 无梯度权重空间编程已展现出通过极少量参数修改实现推理与指令遵循基准显著提升的潜力，但完整实验边界与局限性需待全文公开后进一步验证。

**Tags**: `#eval`

---

## AI Daily

<a id="item-ai-daily-1"></a>
### [Anthropic 发布 Claude Fable 5.2 与 Mythos 5.2](https://www.anthropic.com/claude-fable-and-mythos-5-2) ⭐️ 9.8/10

Anthropic 于 2026-11-09 发布 Claude Fable 5.2 与 Claude Mythos 5.2。两者基于同一底层模型，但 Fable 内置网络安全与生物安全防护，面向所有用户开放；Mythos 需通过生命科学与网络安全验证计划申请。新模型生成速度较 5.1 快 30%，标准定价为每百万输入 token 8 美元、输出 40 美元，fast mode 以双倍价格提供 2.5 倍速度。绝大多数基准测试显示 Fable 5.2 超过 Opus 5.5。内部测试中曾用其将 Python 服务迁移至 Rust，启动速度提升 26 倍，并协调千余子代理在 8 天内设计出可启动的原型操作系统。

rss · Anthropic News · Nov 9, 00:00

**「为什么重要」** 这是 Anthropic 首次通过安全与访问策略区分同源模型，同时以 30% 提速和降价降低高投入推理门槛，fast mode 进一步提供可选的加速层。

**「可关注」** 可关注：Fable 5.2 在 High effort 下以约一半任务成本达到 Opus 5.5 Max effort 水平，fast mode 以 2 倍价格提供 2.5 倍速度；Mythos 5.2 网络安全能力最强但需通过验证计划申请。

**Tags**: `#model`, `#lab`, `#product`

---

<a id="item-ai-daily-2"></a>
### [Pathways 单控制器训练系统 GA](https://developers.googleblog.com/what-is-pathways-single-controller-training-for-large-models/) ⭐️ 8.8/10

Google 宣布 Pathways 在 Google Cloud 正式 GA。Pathways 是 Google 自研的分布式训练系统，用于训练 Gemini 等大模型，采用单控制器架构：一个客户端将整个计算描述为图，由分布式运行时负责节点放置、张量移动和依赖排序。相比 SPMD，Pathways 处理非均匀任务（如流水线并行、RL 循环）和硬件故障更高效——Gemini 2.5 训练期间每小时因硬件故障中断多次，SPMD 下单机故障会阻塞所有进程并回滚到检查点，而 Pathways 允许作业继续。系统已在 Google Cloud 上线，支持 TPU 上运行 JAX 程序，用户通过虚拟设备编写代码，由资源管理器映射到物理芯片。

rss · Google Developers AI · Nov 9, 00:00

**「为什么重要」** 这标志着大模型训练从锁步 SPMD 向图式单控制器架构的转变正式进入生产可用阶段。对于需要处理非均匀任务（如流水线并行、RL 后训练）的团队，Pathways 提供了减少协调代码、提升硬件利用率的具体路径。

**「可关注」** 可关注：单控制器架构通过将计算声明为图并集中管理依赖，绕开 SPMD 跨组 collectives 的带宽瓶颈——以 TPU v5p 为例，片内带宽 1,200 GB/s，跨数据中心网络仅约 6 GB/s，差两个数量级。

**Tags**: `#model`, `#lab`, `#product`, `#industry`

---

<a id="item-ai-daily-3"></a>
### [OpenAI 发布 Control Room](https://openai.com/index/control-room) ⭐️ 8.3/10

OpenAI 发布 Control Room，一套用于监控研究基础设施中模型工作负载的中央系统。该系统可在出现安全或安保顾虑时快速停止相关模型工作负载。这是 OpenAI 研究基础设施中的安全系统组件。

rss · OpenAI Blog · Nov 9, 13:00

**「为什么重要」** 这为 AI 安全治理提供了工程化的基础设施样本。对于关注 AI 安全的从业者，这种集中式监控与中断机制值得跟踪。

**「可关注」** 可关注：Control Room 作为中央监控与中断系统的设计。

**Tags**: `#lab`, `#industry`, `#safety`, `#policy`

---

<a id="item-ai-daily-4"></a>
### [ChatGPT Enterprise 上线 AWS Marketplace](https://openai.com/index/chatgpt-enterprise-aws-marketplace) ⭐️ 7.8/10

OpenAI 正式将 ChatGPT Enterprise 上架 AWS Marketplace。企业可通过现有 AWS 采购与计费关系完成该服务的采购，无需额外对接新的供应商流程。目前未披露具体定价、可用区域等额外限制信息。

rss · OpenAI Blog · Nov 9, 19:00

**「为什么重要」** 企业级 AI 服务的采购门槛降低，已在 AWS 生态内的组织可复用现有采购体系，无需额外走供应商准入流程，加快 ChatGPT Enterprise 的落地速度。

**「可关注」** 可关注：已在 AWS 生态内部署业务的企业可优先评估通过 AWS Marketplace 采购 ChatGPT Enterprise 的流程适配性。

**Tags**: `#product`, `#industry`, `#lab`

---

<a id="item-ai-daily-5"></a>
### [Google AI Studio 支持自然语言构建地图应用](https://developers.googleblog.com/from-prompt-to-app-build-with-google-maps-in-ai-studio/) ⭐️ 7.8/10

Google 宣布 Google Maps Platform 现已接入 Google AI Studio，开发者可通过自然语言提示直接构建带地理空间功能的应用，平台自动完成配置与 API 密钥管理，无需信用卡即可免费试用。内置示例包括 3D 城市漫游、多站点路线规划、门店查找等场景。免费试用受每日配额限制，配额每 24 小时自动重置，生产环境需绑定付费 Cloud 账单账户。

rss · Google Developers AI · Nov 9, 00:00

**「为什么重要」** 这一集成降低了地理空间应用的原型开发门槛，开发者无需手动配置 Maps API 即可快速验证产品想法。

**「可关注」** 可关注：AI Studio 画廊已提供可 remix 的 Maps 应用示例，可直接复用快速启动开发。

**Tags**: `#product`, `#industry`, `#lab`

---

<a id="item-ai-daily-6"></a>
### [MaxText 支持 TPU 长上下文训练](https://developers.googleblog.com/announcing-long-context-training-on-tpus-with-maxtext-context-parallelism/) ⭐️ 7.8/10

Google 在开源 JAX 框架 MaxText 中新增长上下文训练支持，提供四种上下文并行策略：All-gather、A2A/Ulysses、P2P/Ring Attention 及 USP 混合方案，均基于 Tokamax Splash Attention 内核运行于 Cloud TPU。基准测试显示，Llama 3.1 8B 在 TPU 5p 上处理 400 万 token 序列时达到 70% MFU；TPU 7 可将上下文扩展至 1400 万 token，在 600 万 token 以下维持 50% MFU，1400 万 token 时达到 48.7% MFU。该功能已随 MaxText v0.2.4 发布，但 Ulysses 策略的上下文并行度受模型 KV 头数量上限约束。

rss · Google Developers AI · Nov 9, 00:00

**「为什么重要」** 长上下文训练正从数十万 token 向千万级扩展，系统效率成为 frontier 模型的核心瓶颈。MaxText 在 TPU 上提供四种可选的上下文并行方案，为开源社区提供了可验证的长上下文训练路径。

**「可关注」** 可关注：P2P（Ring Attention）在 64K 至 14M token 范围内多数场景下优于 All-gather，且 TPU 7 凭借更大 HBM 在 1400 万 token 下达到 48.7% MFU；内存不足时优先 offload attention 输出，可隐藏传输开销并维持 MFU 平稳。

**Tags**: `#lab`, `#open-source`, `#product`

---

<a id="item-ai-daily-7"></a>
### [Kuken 搜70年图纸降至4.5分钟](https://openai.com/index/kuken) ⭐️ 6.3/10

OpenAI Blog 发布案例研究，Kuken Industries 使用 OpenAI API 检索 70 年历史冷却塔图纸。工程师查找维修图纸的时间从近一小时降至 4.5 分钟。该案例仅展示单一客户实施效果，未涉及新模型能力或行业推广。

rss · OpenAI Blog · Nov 9, 08:00

**「为什么重要」** 该案例展示了生成式 API 在工业文档检索中的效率提升，但影响范围目前仅限单一客户实施。

**「可关注」** 可关注：OpenAI API 在非结构化工程图纸检索中实现了从近一小时到 4.5 分钟的量级优化。

**Tags**: `#industry`, `#product`

---