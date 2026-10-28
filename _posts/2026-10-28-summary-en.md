---
layout: default
title: "Horizon Summary: 2026-10-28 (EN)"
date: 2026-10-28
lang: en
---

> From 188 items, 14 important content pieces were selected

---

**Agent Harness Architecture**
1. [Agents 0.31.0 发布](#item-harness-arch-1) ⭐️ 8.3/10
2. [Codex rust-v0.165.0 发布](#item-harness-arch-2) ⭐️ 7.8/10
3. [OpenHands v1.34.0 发布](#item-harness-arch-3) ⭐️ 7.8/10

**AI Agent Engineer**
1. [LFM3 2B 多模态模型发布](#item-agent-engineer-1) ⭐️ 7.8/10
2. [Allen AI 发布新颖性评判基准](#item-agent-engineer-2) ⭐️ 7.8/10
3. [Anthropic 分享 Claude 大脑 Hands 分离架构](#item-agent-engineer-3) ⭐️ 7.0/10
4. [HF每日论文：RSI Arena 递归自改进](#item-agent-engineer-4) ⭐️ 7.0/10
5. [推理努力未必提升 Agent 表现](#item-agent-engineer-5) ⭐️ 7.0/10
6. [Memory Tax 论文：专用记忆系统净价值为负](#item-agent-engineer-6) ⭐️ 7.0/10
7. [LiquidAI LFM3-1.7B 发布](#item-agent-engineer-7) ⭐️ 5.5/10
8. [Qwen 3.8 Flash Next 外泄指控驳斥](#item-agent-engineer-8) ⭐️ 5.5/10

**AI Daily**
1. [OpenAI 与 Oracle 扩大合作](#item-ai-daily-1) ⭐️ 9.8/10
2. [Retell 用 OpenAI 模型支撑月均 1 亿次通话](#item-ai-daily-2) ⭐️ 6.8/10
3. [文心Unlimited OCR 2 开源发布](#item-ai-daily-3) ⭐️ 5.0/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [Agents 0.31.0 发布](https://github.com/cloudflare/agents/releases/tag/agents%400.31.0) ⭐️ 8.3/10

Cloudflare Agents 0.31.0 发布，引入浏览器内部主机名代理，允许模型通过浏览器访问本地开发服务器、工作区文件夹或同账号 Worker，browserRun\(\) 支持最多 8 个 internalHosts。MCP 相关包变为可选 peer dependency，非 MCP 应用不再强制安装。agents/models/ai-sdk 与 agents/models/pi-ai 脱离实验状态。

github · github-actions\[bot\] · Oct 27, 13:29

**「设计要点」** 浏览器工具运行时迁移至独立 Dynamic Worker，模型代码在隔离环境中执行并支持外部超时终止。内部主机名通过 browserRun\(\) 的 internalHosts 参数注入，模型可用 browser.assignHost\(\) 将主机映射到容器端口或工作区路径，实现本地服务发现。

**「改了什么」** 新增 internalHosts（最多 8 个）与 browser.assignHost\(\) API，支持模型访问本地服务；@modelcontextprotocol/sdk 与 @modelcontextprotocol/server 变为可选依赖，非 MCP 应用需手动声明版本。browserTool 弃用 createBrowserTools、createBrowserRuntime 与 BrowserConnector，模型代码调用从 cdp.send 改为 browser.cdp，agents/models/ai-sdk 与 agents/models/pi-ai 稳定化。

**Tags**: `#runtime`, `#tools`, `#mcp`

---

<a id="item-harness-arch-2"></a>
### [Codex rust-v0.165.0 发布](https://github.com/openai/codex/releases/tag/rust-v0.165.0) ⭐️ 7.8/10

OpenAI Codex CLI ships rust-v0.165.0, defaulting fresh profiles to Memory v2 and adding a built-in Google Cloud Vertex AI provider configured via \`model\_provider = &quot;gcp&quot;\`. The release enables dynamic reasoning effort adjustments during conversations by default, backports GPT-6.1 Terra to model catalogs, introduces experimental attached thread forks in the app-server API, and adds repository filtering and directory grouping to the session picker and agent command center. Runtime fixes cancel remote MCP tool requests when local response futures drop, prevent queued agent messages from resuming after interrupts or Plan mode switches, and close a marketplace URL validation gap that could permit Git host mismatches.

github · github-actions\[bot\] · Oct 27, 20:09

**「设计要点」** Memory v2 replaces the previous default for new profiles, changing the baseline memory model and adding external-agent memory import support. Experimental attached thread forks expose subagent spawning through the app-server API, while remote MCP cancellation now binds tool request lifetimes to local future ownership.

**「改了什么」** Fresh profiles now default to Memory v2 rather than the prior version, and the app-server API exposes experimental attached thread forks for subagent orchestration. Remote MCP tool requests cancel when their local response futures drop, and reasoning effort adjusts dynamically mid-conversation for supported models without manual toggles.

**Tags**: `#memory`, `#mcp`, `#subagents`, `#runtime`, `#tools`

---

<a id="item-harness-arch-3"></a>
### [OpenHands v1.34.0 发布](https://github.com/OpenHands/OpenHands/releases/tag/v1.34.0) ⭐️ 7.8/10

OpenHands v1.34.0 于 2026-10-27 发布，引入 per-conversation Docker runtime，每个对话可绑定独立容器，并新增 Runtime 设置页统一管理。侧边栏支持在对应行沙箱内直接启动新对话，自动化模块增加标签过滤与编辑能力，团队组织内分享开关重命名为 &quot;Share with Org users&quot;。修复将 session API key 通过环境变量而非命令行参数传递给 static-server，并固定自动化 KV secret 以兼容 session-key 轮转。最低 agent server 版本要求提升至 1.57.0，\`@openhands/extensions\` 升至 0.36.0，automation 升至 1.26.0。

github · openhands-release-bot\[bot\] · Oct 27, 14:35

**「设计要点」** Per-conversation Docker runtime 将容器生命周期与对话绑定，Runtime 设置页集中管理运行时参数。自动化 KV secret 固定确保 session-key 轮转时数据可读，static-server 通过环境变量接收 API key 避免命令行参数泄露风险。

**「改了什么」** 相对 v1.33.0，v1.34.0 新增 per-conversation Docker runtime、Runtime 设置页、行级沙箱新建对话、自动化标签管理，以及 API key 传递方式修复。最低 agent server 版本要求提升至 1.57.0。

**Tags**: `#runtime`, `#sandbox`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [LFM3 2B 多模态模型发布](https://huggingface.co/blog/LiquidAI/lfm3) ⭐️ 7.8/10

Liquid AI 于 2026-10-27 发布 LFM3 系列 2B 参数多模态基础模型，包含文本、视觉、音频、全模态和决策六个变体，共享 LFM3-1.7B-Base 主干。LFM3-1.7B 采用 tri-hybrid 架构，在 WebArena-Verified 上得分 38.42， predecessor LFM2.5-2.6B 得分 3.02，参数减少 35%。视觉模型 LFM3-VL-2B 集成 164M 参数自研编码器，在 62 个视觉基准上平均分 71.4，与 Gemma 4 12B 持平；文本模型 4-bit 量化后约 1GB，支持 256K 上下文，可在单 GPU 上微调并部署到边缘设备。博客未提供完整基准对比细节和集成文档链接。

rss · Hugging Face Blog · Oct 27, 17:16

**「为什么重要」** 这组模型把多模态能力压缩到 2B 参数级，并明确针对 agent 场景优化，为本地化、低资源部署的 coding agent 提供了新的基础模型选项。单 GPU 可微调和边缘可部署的特性，降低了 specialized agent 的硬件门槛。

**「可关注」** 可关注：LFM3 通过 tri-hybrid 层混合（13 层门控短卷积、5 层滑动窗口注意力、6 层全局注意力）和 head-wise gated attention 实现 2B 参数下的长上下文推理，8K 上下文时比前代快约 25%。

**Tags**: `#coding-agent`

---

<a id="item-agent-engineer-2"></a>
### [Allen AI 发布新颖性评判基准](https://allenai.org/blog/novelty-bench) ⭐️ 7.8/10

Allen AI 于 2026-10-27 发布 Old Ideas, Novel Problems 基准，评估 LLM 对科研想法新颖性的评判稳定性。实验显示，仅修改 prompt 措辞即可使 GPT-5.4 在 Human+Generated 设定下的准确率从 93.5% 降至 40.9%，波动超 50 个百分点；Claude Opus 4.6 在 Human-Only 设定下也出现 21 个百分点的变动。检索增强与增加推理预算未稳定提升效果，两款专用新颖性评估系统表现低于简单 prompt 的 Claude Opus 4.6 基线。基准基于 ICLR 2026 评审构建，含 Human-Only（299 条人工想法：154 条高新颖性已接收论文、145 条低新颖性拒稿）与 Human+Generated（154 对人工与简单 LLM 生成想法对比）两套设定，其中生成想法的新颖性标签为弱假设、未逐条验证。

rss · Allen AI · Oct 27, 08:00

**「为什么重要」** 科研自动化系统中，novelty judge 常被用于评估 AI 生成的 idea，但该基准显示其 verdict 对配置极度敏感。不同团队报告的“新颖性通过率”可能仅因 prompt 或推理预算差异而不可比，使依赖 LLM-as-judge 的 agent eval harness 面临 verdict 稳定性风险。

**「可关注」** 可关注：构建 LLM-as-judge eval harness 时，必须固定 prompt、推理预算、检索策略与 verdict 聚合方式，并在报告中披露配置敏感度测试，否则 novelty 评估结果缺乏复现性。

**Tags**: `#eval`, `#harness`

---

<a id="item-agent-engineer-3"></a>
### [Anthropic 分享 Claude 大脑 Hands 分离架构](https://latent.space/p/how_anthropic_ships_the_1_llm_in_the_world_safely_separating_the_brain_from_the_hands/) ⭐️ 7.0/10

2026-10-27 Latent Space发布播客节目笔记，邀请Anthropic平台工程师Katelyn Lesse、Angela Jiang分享Claude平台工程实践。内容涵盖Opus 5.5发布、核心的“模型大脑与Agent执行能力分离”架构、托管Agent扩展、安全管控（凭证隔离、沙箱、网络控制）、Rust重写Messages API、长运行Agent Harness设计等一手细节，附官方相关资源链接，对Agent工程师的Harness设计、编排、权限管控、评测体系构建有直接参考价值。

rss · Latent Space · Oct 27, 18:40

**「为什么重要」** 这期内容为Anthropic官方平台工程实践的一手汇总，覆盖Agent架构设计、安全管控、API性能优化等核心环节，是当前少有的公开Claude平台底层实现细节的资料。

**「可关注」** 可关注：Anthropic将模型大脑与Agent执行能力解耦的设计思路，以及用Rust重写Messages API、长运行Agent Harness维护上下文窗口进度的工程实践。

**Tags**: `#harness`, `#coding-agent`, `#orchestration`, `#permissions`, `#eval`

---

<a id="item-agent-engineer-4"></a>
### [HF每日论文：RSI Arena 递归自改进](https://huggingface.co/papers/2610.33624) ⭐️ 7.0/10

2026年10月28日Hugging Face每日论文频道发布arXiv预印本研究，提出RSI Arena框架，验证AI Agent可自主利用人类反馈完成递归自我改进。实验设置10个前沿模型作为训练Agent，统一从NVIDIA Nemotron 3.5 Lightning 30B-A3B Base起步，在6天第一阶段内各获得1000 GPU小时与300美元API额度，在64卡共享集群上自主完成数据选择、训练实现、checkpoint选择全流程。最终所有10个Agent均产出可用助手，其中GPT-6 Astra训练的Agent产出模型在12项能力基准上闭合约76%的Base到Instruct性能差距，配套20项基准测试与盲人人类评估，相关结论尚未经过同行评审。

rss · Hugging Face Daily Papers · Oct 28, 00:00

**「为什么重要」** 该研究提供了可复现的Agent自主训练实验设计与可量化的递归自改进结果，对Agent自改进系统、评测体系与训练编排有直接参考价值。目前结论仅基于预印本，框架在大规模落地或更复杂任务上的效果尚未验证。

**「可关注」** 可关注：在固定资源约束下，前沿模型作为训练Agent的自主训练能力存在明显差异，最强模型可闭合约76%的Base到Instruct能力差距，但全流程自主训练的稳定性仍需更多实验验证。

**Tags**: `#eval`, `#orchestration`, `#harness`

---

<a id="item-agent-engineer-5"></a>
### [推理努力未必提升 Agent 表现](https://huggingface.co/papers/2610.34491) ⭐️ 7.0/10

2026-10-28，Hugging Face Daily Papers 收录论文 2610.34491《What Effort Level Should I Choose? On the Economics of Reasoning Effort in LLM Agents》。该实证研究在 4 个基准（含单步推理与长程 Agent 任务）上测量了推理努力程度的反事实效应，覆盖专有模型与开源模型。结果显示，提高推理努力并不总能保留低努力已解任务，可能造成过度支出，并改变任务轨迹。当前信息来自 HF Daily Papers 的二次摘要，原文内容部分截断，未直接获取主论文。

rss · Hugging Face Daily Papers · Oct 28, 00:00

**「为什么重要」** 该研究针对 LLM Agent 核心参数——推理努力程度——提供实证约束，直接关联 harness 调参与评估设计。实验表明，增加推理时计算量并非提升性能的可靠手段，且可能推高成本并改变任务执行路径。

**「可关注」** 推理努力属于 credence good，其边际收益需按任务类型单独校准；harness 调参与评估设计应显式测试不同努力水平下的任务保留率与轨迹稳定性，而非默认更高努力更优。

**Tags**: `#eval`, `#harness`

---

<a id="item-agent-engineer-6"></a>
### [Memory Tax 论文：专用记忆系统净价值为负](https://huggingface.co/papers/2610.34073) ⭐️ 7.0/10

2026-10-28，Hugging Face Daily Papers 收录论文《Memory Tax: Dissecting the Net Value of Agent Memory》。该论文提出大规模评估框架，定义 memory tax 衡量专用记忆系统与 naive RAG 的净性能权衡。跨多个 benchmark 和模型 backbone 的实验显示，许多专用记忆系统相比直接从原始历史检索表现更差，净价值为负。研究者将净价值拆分为 memory benefit（收益）与 memory tax（成本），指出记忆处理对原始信息的组织和访问方式改变是双重偏差的来源。

rss · Hugging Face Daily Papers · Oct 28, 00:00

**「为什么重要」** 该工作提供了专用记忆层在 long-horizon agent 中净价值的系统量化，为记忆组件选型提供实证基线。它表明增加记忆处理模块可能引入信息损失，抵消其组织收益，这对设计需要持久记忆的 coding agent 有直接参考意义。

**「可关注」** 可关注：在 agent 记忆系统设计中，应以 naive RAG（直接检索原始历史）为性能基线，量化专用记忆模块的 memory tax，避免引入净价值为负的记忆层。

**Tags**: `#memory`, `#eval`

---

<a id="item-agent-engineer-7"></a>
### [LiquidAI LFM3-1.7B 发布](https://www.reddit.com/r/LocalLLaMA/comments/1xgy8s3/liquidailfm317b_hugging_face/) ⭐️ 5.5/10

2026年10月27日Reddit社区转发LiquidAI官方发布的LFM3-1.7B文本模型规格，该模型为1.73B参数的三混合架构，针对本地agent与专用场景做agentic后训练，支持256K token上下文窗口，4-bit精度下内存占用约1GB，可部署于手机、笔记本等边缘设备，支持单GPU快速微调。官方明确说明该模型不推荐用于agentic编程或复杂多步推理场景，目前未公开性能基准数据，无法评估其面向coding agent工程场景的实际效用。

reddit · r/LocalLLaMA · /u/jacek2023 · Oct 27, 17:04

**「为什么重要」** 该模型是少有的面向本地agent场景优化的1B级边缘可部署小模型，单GPU微调能力与256K上下文特性对轻量化coding agent harness的定制化有潜在价值，但缺乏公开性能数据，其工具调用、结构化输出等核心agent能力的实际表现尚未得到验证。

**「可关注」** 可关注：LFM3-1.7B的低内存占用与单GPU微调特性适合轻量本地agent场景的定制化需求，但需等待公开性能基准验证其agent核心能力是否满足工程要求。

**Tags**: `#harness`, `#coding-agent`, `#local-llm`

---

<a id="item-agent-engineer-8"></a>
### [Qwen 3.8 Flash Next 外泄指控驳斥](https://www.reddit.com/r/LocalLLaMA/comments/1xgopmj/debunking_coheres_claim_of_qwen_38_flash_next/) ⭐️ 5.5/10

2026年10月27日，Reddit社区发布分析驳斥Cohere关于开放权重模型Qwen 3.8 Flash Next（Q38FN）向阿里远程URL外泄数据的指控，指出Cohere公开的测试数据集存在两个核心设计缺陷。第一，测试将输入模型trace截断至目标URL生成前的2323个token前缀，强制模型扮演URL生成器，而非模拟正常使用场景。第二，测试使用的检测prompt无任何上下文、表述高度模糊，实质诱导模型从训练数据中幻觉生成URL。分析者还提到自Q38FN发布以来，其个人使用日志中从未出现过阿里相关URL。Cohere CEO此前回应称无证据表明该行为是故意的，该行为出现频率低于十万分之一次调用，且此类测试设计仅适用于开放权重模型，闭源模型因权重不公开无法复现。该分析仅针对这一具体指控，为AI Agent开发者的模型评估设计提供避坑参考。

reddit · r/LocalLLaMA · /u/feelspeaceman · Oct 27, 10:19

**「为什么重要」** 该帖子提供了安全相关模型评估设计缺陷导致假阳性结论的具体实例，对构建Agent测试框架的团队有参考价值。它未证实Q38FN或其他模型存在更广泛的安全问题，且是社区对Cohere公开数据集的二次分析，非一手验证结论。

**「可关注」** 设计模型安全行为相关评估时，需保留完整的输入上下文trace，并使用清晰、带上下文的prompt，避免诱导模型产生幻觉，进而被误判为恶意行为。

**Tags**: `#eval`, `#permissions`

---

## AI Daily

<a id="item-ai-daily-1"></a>
### [OpenAI 与 Oracle 扩大合作](https://openai.com/index/oracle-apps-in-chatgpt) ⭐️ 9.8/10

2026 年 10 月 27 日，OpenAI 官方宣布与 Oracle 扩大合作。核心动作是将 Oracle 的企业业务应用及 AI Agent 整合进 ChatGPT，同时为 Oracle 的新产品、服务提供 AI 能力支撑。

rss · OpenAI Blog · Oct 27, 07:00

**「为什么重要」** 该合作是头部 AI 实验室与主流云服务厂商的深度绑定，将推动企业级 AI Agent 与现有业务系统的融合落地，是当前 AI 行业 To B 赛道的重要动态。

**「可关注」** 可关注：Oracle 企业应用接入 ChatGPT 后的 AI Agent 交互逻辑与数据权限设计。

**Tags**: `#lab`, `#industry`, `#product`

---

<a id="item-ai-daily-2"></a>
### [Retell 用 OpenAI 模型支撑月均 1 亿次通话](https://openai.com/index/retell-ai) ⭐️ 6.8/10

OpenAI 博客发布 Retell 客户案例。该公司用 OpenAI 模型支撑月均 1 亿次通话。GPT-6 Astra 在其语音智能体基准测试中排名第一。Codex 帮助其达到每位员工每年 160 万美元收入运行率，该案例未涉及新模型发布或政策变更。

rss · OpenAI Blog · Oct 27, 15:00

**「为什么重要」** 该案例提供 OpenAI 模型在语音 AI 场景的商用验证，包含具体性能与收入指标，可作为同类产品选型参考。

**「可关注」** 可关注：GPT-6 Astra 在语音智能体基准测试中的排名表现。

**Tags**: `#model`, `#lab`, `#industry`, `#product`

---

<a id="item-ai-daily-3"></a>
### [文心Unlimited OCR 2 开源发布](https://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw==&amp;mid=2247936488&amp;idx=2&amp;sn=286b1f5cae20ebec0f56b4ef14b6d081) ⭐️ 5.0/10

百度正式发布并开源文心Unlimited OCR 2，该产品提出稀疏参考滑动窗口注意力机制SR-SWA与持续解码机制，支持无上限页数的长文档连续识别；在百页级单序列测试中，峰值KV缓存占用从标准解码的47GB降至1.77GB，降幅约96%，可连续处理3600+页的《哈利·波特》全集、1200+页的《三体》全集。

rss · 量子位 · Oct 27, 06:13

**「为什么重要」** 上一代文心Unlimited OCR已在开源社区积累超1000万次下载、约2.86万GitHub Star，本次升级解决了长文档OCR推理的显存瓶颈，可降低长文档识别场景的部署与使用门槛。

**「可关注」** 可关注：文心Unlimited OCR 2提出的SR-SWA机制通过按需选取相关页面与视觉信息减少重复计算，目前已开源至GitHub与Hugging Face平台。

**Tags**: `#model`, `#industry`, `#open-source`, `#product`

---