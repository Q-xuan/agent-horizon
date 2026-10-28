---
layout: default
title: "Horizon Summary: 2026-10-28 (ZH)"
date: 2026-10-28
lang: zh
---

> 从 211 条内容中筛选出 18 条重要资讯。

<nav id="ah-toc" class="ah-toc" aria-label="目录"><span class="ah-toc-title">目录</span><ul><li><a href="#sec-harness-arch"><span class="ah-toc-name">Harness 架构</span><span class="ah-toc-count">3条</span></a></li><li><a href="#sec-agent-engineer"><span class="ah-toc-name">Agent 工程师日报</span><span class="ah-toc-count">9条</span></a></li><li><a href="#sec-ai-daily"><span class="ah-toc-name">AI 日报</span><span class="ah-toc-count">5条</span></a></li><li><a href="#sec-ai-deals"><span class="ah-toc-name">AI 羊毛</span><span class="ah-toc-count">1条</span></a></li></ul></nav>

---

**[Harness 架构](#sec-harness-arch)**
1. [Codex rust-v0.165.0 发布](#item-harness-arch-1) ⭐️ 7.8/10
2. [pydantic-ai v2.63.0 发布](#item-harness-arch-2) ⭐️ 7.8/10
3. [pydantic-ai v2.62.0 发布](#item-harness-arch-3) ⭐️ 7.8/10

**[Agent 工程师日报](#sec-agent-engineer)**
1. [Liquid AI LFM3 多模态模型发布](#item-agent-engineer-1) ⭐️ 7.8/10
2. [LLM 科研新颖性判断基准发布](#item-agent-engineer-2) ⭐️ 7.8/10
3. [DeepMind Genie 4 发布](#item-agent-engineer-3) ⭐️ 7.0/10
4. [Trajectory2Gym 论文提出工具智能体训练框架](#item-agent-engineer-4) ⭐️ 7.0/10
5. [TraceTrial-Bench 评估 harness 可靠性](#item-agent-engineer-5) ⭐️ 7.0/10
6. [DynaFlow 多智能体编排研究](#item-agent-engineer-6) ⭐️ 7.0/10
7. [Latent Space 播客梳理：Anthropic 脑手分离](#item-agent-engineer-7) ⭐️ 6.0/10
8. [LiquidAI LFM3-1.7B 发布](#item-agent-engineer-8) ⭐️ 6.0/10
9. [Qwen 3.8 Flash Next 指控复盘](#item-agent-engineer-9) ⭐️ 5.5/10

**[AI 日报](#sec-ai-daily)**
1. [OpenAI 与 Oracle 扩大合作](#item-ai-daily-1) ⭐️ 8.8/10
2. [Retell 用 OpenAI 模型支撑月 1 亿次通话](#item-ai-daily-2) ⭐️ 7.8/10
3. [1.3B OXR 登顶 OCR 三榜第一](#item-ai-daily-3) ⭐️ 5.5/10
4. [百度开源文心 Unlimited OCR 2 缓存降 96%](#item-ai-daily-4) ⭐️ 5.5/10
5. [智源 AREX-2 长程反思提升 27B 模型性能](#item-ai-daily-5) ⭐️ 5.0/10

**[AI 羊毛](#sec-ai-deals)**
1. [上海政府补贴通知 JSON feed 免费公开](#item-ai-deals-1) ⭐️ 6.0/10

---

## Harness 架构
{: #sec-harness-arch .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-harness-arch" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-harness-arch-1"></a>
### [Codex rust-v0.165.0 发布](https://github.com/openai/codex/releases/tag/rust-v0.165.0) ⭐️ 7.8/10

OpenAI Codex CLI 发布 rust-v0.165.0。本次更新默认启用 memory v2（新配置文件支持外部 agent 记忆导入），app-server API 新增实验性 attached thread forks，MCP 工具请求在本地响应 future 被 drop 时自动取消。同时内置 Google Cloud Vertex AI provider（\`model\_provider = &quot;gcp&quot;\`），默认开放 reasoning effort 动态调整，并新增 GPT-6.1 Terra 模型。

github · github-actions\[bot\] · 10月27日 20:09

**「设计要点」** 新配置文件默认启用 memory v2 并支持外部 agent 记忆导入，app-server API 提供实验性 attached thread forks 用于子代理线程派生，MCP 工具请求与本地 future 绑定实现 drop 即取消远程请求。

**「改了什么」** 相对 rust-v0.164.0，新配置文件默认启用 memory v2 并支持外部记忆导入；app-server API 增加实验性 attached thread forks；MCP 远程工具请求在本地 future 丢弃时取消；新增内置 GCP Vertex AI provider；reasoning effort 调整默认对支持模型开放。

**标签**: `#memory`, `#mcp`, `#subagents`, `#runtime`, `#tools`

---

<a id="item-harness-arch-2"></a>
### [pydantic-ai v2.63.0 发布](https://github.com/pydantic/pydantic-ai/releases/tag/v2.63.0) ⭐️ 7.8/10

pydantic-ai v2.63.0 发布，核心 harness 行为多项兼容性变更。默认 \`CodeMode\` 启用 \`dynamic\_catalog=True\`，揭示工具追加而非重写缓存提示词。新增 \`IPythonCodeMode\`、\`DetectLoops\` 能力、\`PostgresSpendStore\`、\`ag-ui-protocol\` 1.0 支持及 \`gpt-6.1-terra\` 模型。\`Dataset.evaluate\` 新增 \`task\_timeout\` 限制单任务尝试，Harness \`LLMReminder\` 默认 \`interval=10\` 且不再每个请求生成，加密历史数据可重放至相同 \`canonical\_system\` 的提供者。

github · dsfaccini · 10月28日 00:55

**「设计要点」** 运行时支持延迟能力加载与动态工具目录，Gemini Live 通过 \`GoogleRealtimeConnection.dial\` 的 \`replay\` 参数重连。历史数据以签名加密形式存储，仅向相同 \`canonical\_system\` 的提供者重放，UI 适配器新增 \`manage\_message\_history\` 防止服务器持有历史重复发送。

**「改了什么」** 默认 \`CodeMode\` 启用 \`dynamic\_catalog=True\`，揭示工具追加而非重写缓存提示词。Harness \`LLMReminder\` 默认 \`interval=10\`，延迟 \`CombinedCapability\` 改为单能力加载并保持成员顺序，GPT-Live 回复延至 Live 下次暂停时结束。无中途系统消息模型上转义 \`&lt;system&gt;\` 标签。

**标签**: `#runtime`, `#tools`, `#memory`

---

<a id="item-harness-arch-3"></a>
### [pydantic-ai v2.62.0 发布](https://github.com/pydantic/pydantic-ai/releases/tag/v2.62.0) ⭐️ 7.8/10

pydantic-ai v2.62.0 发布，核心更新覆盖运行时、工具层、记忆压缩与错误处理。运行时新增 \`ModelSettingsDeltaPart\` 支持对话中途调整 thinking effort，并新增 \`ModelRequestRejectedError\` 等模型错误类型；工具层引入可配置 \`tool\_prefix\` 的 MCP 能力、\`SubAgents\` 任务控制及 \`allowed\_tools\` 缓存保留。记忆系统将 \`SummarizingCompaction\` 改为 \`CompactionPart\` 存储，并支持模型主动请求压缩。\`GraphBuilder\` 广播分支顺序变更可能破坏持久工作流重放，\`cache\_ttl\` 与 \`monty\_sandbox\_url\` 被弃用。

github · dsfaccini · 10月27日 02:38

**「设计要点」** 运行时通过 \`ModelSettingsDeltaPart\` 将模型设置增量变更持久化为对话历史，实现无状态切换；记忆层将压缩摘要拆分为独立 \`CompactionPart\` 并按运行快照追加，保证请求仅追加不变性；工具层通过 \`tool\_prefix\` 隔离 MCP 命名空间，并通过 \`task\_control\` 将子代理委托转为模型可调度任务。

**「改了什么」** 新增对话中途动态调整 thinking effort 能力（支持 OpenAI 与 Anthropic，保留 OpenRouter 缓存），MCP 工具默认添加服务前缀，压缩摘要改为 \`CompactionPart\` 并支持模型主动触发压缩。同时新增 \`ModelRequestRejectedError\` 等错误类型、\`SubAgents\` 任务控制、批量 API 支持及 \`Coder\(task\_control=\)\` 接口。

**标签**: `#runtime`, `#tools`, `#mcp`, `#memory`, `#permissions`

---

## Agent 工程师日报
{: #sec-agent-engineer .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-agent-engineer" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-agent-engineer-1"></a>
### [Liquid AI LFM3 多模态模型发布](https://huggingface.co/blog/LiquidAI/lfm3) ⭐️ 7.8/10

Liquid AI 于 2026 年 10 月 27 日发布 LFM3 多模态基础模型家族，全部基于 2B 参数量级的共享骨干网络，覆盖文本、视觉、音频、全模态、决策 5 类共 6 个模型变体。相比上一代 LFM2，LFM3-1.7B 参数减少 35%，性能超过更大的 LFM2.5-2.6B，支持单 GPU 微调、4-bit 精度下文本模型体积约 1GB、边缘设备部署，面向智能体场景优化。新增决策模型变体可输出校准答案，视觉模型首次支持视频输入，在 62 个视觉基准上的平均分从上一代的 57.6 提升至 71.4，与参数量 6 倍于它的 Gemma 4 12B 相当；音频模型支持 18 种语言语音翻译与流式解码，首 token 延迟低至 50ms，其文本模型在 WebArena-Verified 上得分 38.42，远高于上一代 LFM2 的 3.02。

rss · Hugging Face Blog · 10月27日 17:16

**「为什么重要」** 这是 Liquid AI 首次官方发布 LFM3 多模态模型家族，2B 参数量级下实现跨模态共享骨干、单卡微调与边缘部署能力，直接面向智能体场景设计。但目前公开材料未披露针对智能体场景的专项评测基准，实际落地效果尚未得到第三方验证。

**「可关注」** 可关注 LFM3 系列新增专门面向智能体工作负载的决策模型变体，且全系列支持单 GPU 微调与边缘部署，可优先评估其在本地 agent 场景下的适配成本与推理性能。

**标签**: `#harness`, `#multimodal-model`, `#fine-tuning`, `#edge-deployment`

---

<a id="item-agent-engineer-2"></a>
### [LLM 科研新颖性判断基准发布](https://huggingface.co/blog/allenai/novelty-bench) ⭐️ 7.8/10

2026-10-27 Hugging Face 与 Ai2 联合发布名为《Old Ideas, Novel Problems》的科研新颖性判断可靠性研究及配套开源资源，包含论文、基准数据集、代码与自动构建评估集的流水线。基准设置两个测试场景：Human-Only 场景包含 299 条来自 ICLR 2026 高/低新颖性人类论文的科研想法，用于测试判断器区分人类想法的能力；Human+Generated 场景将 154 条经评审信号校验的人类想法与 154 条仅接收研究领域和「提出新颖想法」指令、无文献检索/工具/迭代/反馈的基础 LLM 生成的弱标签想法配对，模拟判断 AI 生成想法的实际场景。额外校验中，专家独立审查 30 对 Human+Generated 样本（优先覆盖最强判断器出错的案例），全部偏好人类想法，未认定任何生成想法具有新颖性；同时将两类想法改写为统一结构测试，排除写作风格干扰。测试覆盖 GPT-5.1、GPT-5.2、GPT-5.4、Claude Sonnet 4.5、Claude Opus 4.5、Claude Opus 4.6 六款模型，结果显示提示词微调可导致同一模型准确率波动超 50 个百分点，检索与额外推理未稳定提升判断效果，两款专用新颖性评估系统表现不如简单提示的 Claude Opus 4.6 基线。该资源面向科研 AI Agent、eval 工具链开发者开放。

rss · Hugging Face Blog · 10月27日 16:12

**「为什么重要」** 当前 LLM 已被广泛用作科研 AI 系统的新颖性判断器，但此前缺乏标准化的可靠性评估方案。该基准首次系统量化了不同设置下 LLM 判断的波动性，为科研类 AI Agent 的 eval 模块开发提供了可直接复用的测试集与构建工具，填补了细分场景的开源空白。

**「可关注」** 可关注：LLM 新颖性判断结果对提示词、输入格式等细微改动极度敏感，在构建科研 AI Agent 的 eval 模块时，需将提示词鲁棒性、不同生成源想法的判断一致性纳入必测项。

**标签**: `#eval`, `#harness`

---

<a id="item-agent-engineer-3"></a>
### [DeepMind Genie 4 发布](https://deepmind.google/blog/genie-4-a-new-generation-of-world-simulation/) ⭐️ 7.0/10

DeepMind 于 2026 年 10 月 27 日发布 Genie 4 世界模拟模型，主打实时仿真的高真实感生成。社区实测显示该模型帧内对象一致性表现较好，但出画后返回的对象会出现细节变化（如龙示例新增城堡、站台行人变化、香港踏板车手头盔状态变化）；音频提示存在不匹配问题（要求萨克斯输出单簧管声音）；要求写实的魔法棒孔雀变猫示例输出仍有游戏感。目前官方未公开完整技术架构与性能指标，该工具主要面向 AI agent 训练、评估流程的工程师群体。

hackernews · Google DeepMind · 10月27日 16:06 · [社区讨论](https://news.ycombinator.com/item?id=50261319)

**「为什么重要」** 它是当前少有的面向实时仿真的世界模型产品，但社区实测暴露的生成缺陷能帮助工程师避免过度预期，更理性判断其适配的训练/评估场景。

**「可关注」** 可关注：Genie 4 帧内一致性表现较好，但出画对象的状态一致性、音频提示对齐、复杂写实生成场景的稳定性存在明确短板，评估其用于 agent 训练/评测时需针对性设计边界用例。

**「评论」** 社区讨论集中在 Genie 4 的实际生成缺陷，同时有用户提及腾讯开源的 HY-World 2.0 世界模型未获得足够关注，也有用户对视频游戏与影视内容生成边界的未来走向表示期待。

**标签**: `#eval`, `#harness`

---

<a id="item-agent-engineer-4"></a>
### [Trajectory2Gym 论文提出工具智能体训练框架](https://huggingface.co/papers/2610.33568) ⭐️ 7.0/10

Hugging Face Daily Papers 于 2026-10-28 介绍 Trajectory2Gym 框架论文，该框架针对工具使用智能体训练中的监督质量问题，提出生成决策 grounded 且组合多样化的交互轨迹。论文指出现有成功轨迹常缺乏多步依赖表示，或包含决策时信息无法证明的动作，因此需同时满足组合覆盖与决策 grounded 两个耦合要求。Trajectory2Gym 围绕支持不足的组合结构构建可执行交互，仅从 realized execution 中的 grounded 决策推导监督，并通过结构支持选择分配经验。当前材料为截断摘要，未提供完整技术细节、性能基准或代码链接，该论文获 336 次 upvotes，标签为 coding-agent 与 eval。

rss · Hugging Face Daily Papers · 10月28日 01:58

**「为什么重要」** 工具智能体训练常因轨迹缺乏决策 grounded 和组合覆盖而收到低质量监督信号。Trajectory2Gym 直接针对该核心限制提出数据生成方案，但完整技术细节与基准验证尚未公开，实际效果待确认。

**「可关注」** 可关注：训练工具使用智能体时，现有成功轨迹可能因未满足决策 grounded 与组合覆盖而成为低质量监督；Trajectory2Gym 提出通过构建可执行交互并仅提取 grounded 决策来提升训练信号质量，但需等待完整论文与代码验证。

**标签**: `#coding-agent`, `#eval`

---

<a id="item-agent-engineer-5"></a>
### [TraceTrial-Bench 评估 harness 可靠性](https://huggingface.co/papers/2610.32285) ⭐️ 7.0/10

2026-10-28，Hugging Face Daily Papers 收录论文《Trial by Trace: Benchmarking AI Agent Harnesses for Reliability and Failure Attribution》，提出 TraceTrial-Bench 基准测试。该基准将 harness 可靠性拆分为 context、execution、governance、lifecycle、observability、tools、verification 七类组件，配套 95 个专家级机制导向任务，并提供可执行或状态式 ground truth 与 Trajectory Tracing \(TT\) 模块。现有基准多聚焦模型能力与整体 agent 性能，对 harness 本身评估不足。该工作直接影响 harness、eval 系统及工具链工程师，但论文具体发表日期与 TT 模块实现细节未在摘要中披露。

rss · Hugging Face Daily Papers · 10月28日 01:58

**「为什么重要」** 现有 agent 基准多测模型能力，忽略 harness 本身对可靠性的贡献。TraceTrial-Bench 提供结构化组件划分与可复现任务集，为工程师提供了可对比 harness 性能的公共标尺，但该基准是否被社区采纳、能否覆盖实际生产场景尚未证实。

**「可关注」** 可关注：TraceTrial-Bench 将 harness 可靠性拆为七类组件，并保留各 harness 本地行为做语义等效比较，这种设计可能影响后续 eval 系统的组件化拆分与轨迹审计实现。

**标签**: `#eval`, `#harness`, `#observability`

---

<a id="item-agent-engineer-6"></a>
### [DynaFlow 多智能体编排研究](https://huggingface.co/papers/2610.34467) ⭐️ 7.0/10

Hugging Face 每日论文 2026-10-28 收录 DynaFlow 多智能体编排框架研究，该条目获得 189 次赞同。该框架将自由格式可执行工作流合成纳入主智能体动作空间，主智能体可自主判断协作需求，生成任务专属程序，通过串行/并行执行、结构化信息交换与验证协调子智能体，执行结果与轨迹可反哺后续决策。训练仅针对主智能体，采用蒸馏轨迹监督微调，并过滤无依据前提、偏倚验证、信息流缺陷三类问题轨迹。当前未公开性能基准与生产部署相关信息。

rss · Hugging Face Daily Papers · 10月28日 01:58

**「为什么重要」** 该研究给出了动态多智能体编排的可实现技术路径，其缺陷感知的训练流程对自适应多智能体系统的工程构建有参考价值，但尚未公开性能验证与落地案例。

**「可关注」** 可关注：主智能体动态生成编排程序、缺陷过滤轨迹微调的训练范式，可参考用于自适应多智能体系统的原型设计。

**标签**: `#orchestration`, `#eval`, `#multi-agent`

---

<a id="item-agent-engineer-7"></a>
### [Latent Space 播客梳理：Anthropic 脑手分离](https://latent.space/p/how_anthropic_ships_the_1_llm_in_the_world_safely_separating_the_brain_from_the_hands/) ⭐️ 6.0/10

2026-10-27 发布的 Latent Space 播客邀请 Anthropic 工程师 Katelyn Lesse 与 Angela Jiang，分享 Claude 平台工程实践，覆盖 Opus 5.5 发布、模型“脑”与 agent “手”解耦、托管 agent 扩缩容、安全管控等主题。节目附带 5 项 Anthropic 官方资源链接，分别对应 Opus 5.5 发布说明、托管 agent 研究、Claude 隔离方案、长运行 agent harness 设计、Anthropic S-1 拆解。当前提供的材料仅为节目大纲与资源索引，无深度技术细节，需跳转官方材料或完整节目获取可执行信息。

rss · Latent Space · 10月27日 18:40

**「为什么重要」** 该内容聚焦 agent 平台架构、harness 设计、安全管控等 AI agent 工程师核心关切的主题，附带 Anthropic 官方一手实践资源，是当前少有的公开平台工程实践分享。但当前提供的材料仅为节目大纲与资源索引，具体技术细节与落地经验需跳转官方材料或完整节目验证。

**「可关注」** 可关注：Anthropic 公开的模型-执行层解耦架构思路，以及配套的托管 agent、安全管控、长运行 agent harness 官方实践文档。

**标签**: `#harness`, `#coding-agent`, `#permissions`, `#eval`

---

<a id="item-agent-engineer-8"></a>
### [LiquidAI LFM3-1.7B 发布](https://www.reddit.com/r/LocalLLaMA/comments/1xgy8s3/liquidailfm317b_hugging_face/) ⭐️ 6.0/10

2026 年 10 月 27 日，Reddit 社区用户分享 LiquidAI 官方发布的 LFM3-1.7B 文本模型。该模型为 1.73B 参数规模，基于 24 层三混合架构（含 13 个门控短卷积、5 个滑动窗口注意力、6 个全局注意力），针对 Hermes Agent、Pi、OpenClaw 等常见智能体 harness 后训练，支持 256K token 上下文窗口，词汇表规模 128K tokens，覆盖英语、中文等 14 种语言。4-bit 精度下内存占用约 1GB，可部署于手机、笔记本等边缘设备，支持单 GPU 快速微调适配领域、格式与工具需求，目前已合并 llama.cpp 相关支持。官方说明该模型不推荐用于智能体编程或多步复杂推理场景。

reddit · r/LocalLLaMA · /u/jacek2023 · 10月27日 17:04

**「为什么重要」** 该模型正式推出填补了边缘端本地智能体场景小参数量长上下文文本模型的空白，为 harness 工程师提供了新的轻量本地选项。目前公开材料未包含性能基准、实际评测数据，其在真实智能体任务中的工具调用、推理表现尚未得到验证。

**「可关注」** 可关注：LFM3-1.7B 4-bit 精度下约 1GB 内存占用，可作为边缘端轻量智能体 harness 的候选文本基座，但需自行验证其工具调用、结构化输出等实际能力是否符合需求。

**标签**: `#coding-agent`, `#harness`

---

<a id="item-agent-engineer-9"></a>
### [Qwen 3.8 Flash Next 指控复盘](https://www.reddit.com/r/LocalLLaMA/comments/1xgopmj/debunking_coheres_claim_of_qwen_38_flash_next/) ⭐️ 5.5/10

2026 年 10 月 27 日 Reddit 用户/u/feelspeaceman 发布分析，反驳 Cohere 关于 Qwen 3.8 Flash Next（Q38FN）自发生成阿里云远程 URL 的安全指控。分析基于 Cohere 公开的 Hugging Face 追踪数据集，指出其测试脚本强制预填充 2232 个 token，恰好停在 URL 生成前的位置，人为诱导模型输出 URL；同时测试所用提示词模糊无上下文，本质是诱导模型幻觉。Cohere CEO 此前已承认无证据证明该行为是模型故意输出，该行为在 Q38FN 日常使用日志中未出现，出现频率低于十万分之一，且类似诱导方法理论上也可作用于其他开源或闭源模型。

reddit · r/LocalLLaMA · /u/feelspeaceman · 10月27日 10:19

**「为什么重要」** 该分析厘清了安全测试中人为诱导幻觉与模型自发异常行为的边界，对模型安全评估的 prompt 设计、测试流程严谨性有参考价值，但仅针对单一具体指控，无更广泛的架构或安全结论。

**「可关注」** 可关注：安全 eval 需排除预填充 token、模糊诱导提示词等人为干扰因素，避免将诱导产生的幻觉输出判定为模型自发异常行为。

**标签**: `#eval`, `#prompt-engineering`, `#safety`

---

## AI 日报
{: #sec-ai-daily .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-daily" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-daily-1"></a>
### [OpenAI 与 Oracle 扩大合作](https://openai.com/index/oracle-apps-in-chatgpt) ⭐️ 8.8/10

OpenAI 官方宣布与 Oracle 扩大合作，核心方向为将 Oracle 业务应用及 AI agent 接入 ChatGPT，同时为 Oracle 新业务提供 AI 能力支撑。

rss · OpenAI Blog · 10月27日 07:00

**「为什么重要」** 该合作将企业级业务场景与 AI agent 能力直接融入 ChatGPT，拓展了 ChatGPT 的 To B 应用边界，同时为 Oracle 新业务提供 AI 能力底座。

**「可关注」** 可关注：Oracle 业务应用及 AI agent 接入 ChatGPT 的具体落地形态与后续开放节奏。

**标签**: `#lab`, `#industry`, `#product`

---

<a id="item-ai-daily-2"></a>
### [Retell 用 OpenAI 模型支撑月 1 亿次通话](https://openai.com/index/retell-ai) ⭐️ 7.8/10

OpenAI 官方博客披露，语音 AI 公司 Retell 使用 OpenAI 模型支撑每月 1 亿次通话。GPT-6 Astra 在 Retell 内部语音智能体基准测试中排名第一，Codex 助力 Retell 实现人均年化收入运行率 160 万美元。

rss · OpenAI Blog · 10月27日 15:00

**「为什么重要」** 这是 OpenAI 官方公开的客户落地案例，可直观反映其模型在语音交互场景的商用落地效果，以及 Codex 对企业开发效率与营收增长的实际支撑价值。

**「可关注」** 可关注：GPT-6 Astra 在语音智能体基准测试中表现领先，Codex 可支撑企业级开发效率与营收增长。

**标签**: `#lab`, `#model`, `#industry`, `#product`

---

<a id="item-ai-daily-3"></a>
### [1.3B OXR 登顶 OCR 三榜第一](https://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw==&amp;mid=2247936488&amp;idx=1&amp;sn=6ac0acdd138a429dbce62ca2d3a88b13) ⭐️ 5.5/10

量子位报道称，参数量 1.3B 的国产开源 OXR 模型登顶 OmniDocBench、olmOCR-Bench、DocParsingBench 三个 OCR 榜单第一，支持化学结构图解析、手写笔记转 Markdown；单张 RTX PRO 6000 完成 100 页端到端文档解析耗时 101 秒，海外 GitHub Star 达 1.1K+，曾登推特最热 Daily News。该内容为二手科技资讯，无对应官方一手发布链接，缺乏可核对的官方细节与模型对比内容。

rss · 量子位 · 10月27日 06:13

**「为什么重要」** 1.3B 参数小体量模型拿下 OCR 三榜第一，且支持化学结构图等特殊内容解析，证明轻量方案在文档理解场景的落地可能性，相关能力已引发海外开发者社区关注。

**「可关注」** 可关注：该 OXR 模型对化学结构图、手写笔记等非标准文档内容的解析效果，以及 1.3B 参数下的端到端推理速度表现。

**标签**: `#model`, `#open-source`, `#industry`, `#eval`

---

<a id="item-ai-daily-4"></a>
### [百度开源文心 Unlimited OCR 2 缓存降 96%](https://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw==&amp;mid=2247936488&amp;idx=2&amp;sn=286b1f5cae20ebec0f56b4ef14b6d081) ⭐️ 5.5/10

量子位报道百度发布并开源文心 Unlimited OCR 2，该模型采用稀疏参考滑动窗口注意力机制 SR-SWA 与持续解码机制，宣称将峰值 KV 缓存占用从标准解码的 47GB 降至 1.77GB，降幅约 96%，支持无限页数输入，可完成 3600+页《哈利·波特》全集、1200+页《三体》全集的连续识别转写。该信息为二手科技媒体报道，暂无官方一手来源佐证。

rss · 量子位 · 10月27日 06:13

**「为什么重要」** 上一代 Unlimited OCR 已在开源社区积累超 1000 万次下载、约 2.86 万 GitHub Star，第二代在长文档处理场景降低显存门槛，有望进一步降低超长文档 OCR 的部署与使用成本。

**「可关注」** 可关注：稀疏参考滑动窗口注意力机制 SR-SWA 对长序列 KV 缓存的压缩效果，以及其在超长文档推理场景的落地验证。

**标签**: `#model`, `#open-source`, `#industry`

---

<a id="item-ai-daily-5"></a>
### [智源 AREX-2 长程反思提升 27B 模型性能](https://mp.weixin.qq.com/s?__biz=MzA3MzI4MjgzMw==&amp;mid=2651070489&amp;idx=3&amp;sn=54e92cb2108bbc579873c8ccfaa114d3) ⭐️ 5.0/10

智源 AREX 研究小组发布 AREX-2 模型，以 27B 参数的 Qwen3.8-27B 为基座，基于机器学习与算法编程场景的长程反思数据训练，在 MLE-bench、Frontier-CS、BrowseComp、HLE 等基准上分别取得 81.8、70.7、84.0、52.6 的成绩，刷新开源轻量模型最佳表现，较上一代 AREX 显著提升，为递归自我改进（RSI）探索出可训练、可验证的实现路径。当前仅公开论文、项目仓库与模型权重链接，未披露更多训练细节与对比基线。

rss · 机器之心 · 10月27日 04:03

**「为什么重要」** AREX-2 验证了长程反思作为跨领域可迁移元能力的可行性，首次为递归自我改进（RSI）给出可训练、可验证的实现路径，填补了该方向从理论到实践的关键空白。

**「可关注」** 可关注：长程反思训练在提供清晰可验证反馈的场景下，有望成为提升模型测试时扩展能力的可行方向。

**标签**: `#model`, `#lab`, `#industry`

---

## AI 羊毛
{: #sec-ai-deals .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-deals" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-deals-1"></a>
### [上海政府补贴通知 JSON feed 免费公开](https://github.com/ZhongGheart/china-policy-data) ⭐️ 6.0/10

GitHub 用户 subsidyradar 公开维护的 china-policy-data 仓库，提供免费的上海政府补贴通知每日 JSON 数据 feed，可直接访问仓库获取。该资源仅覆盖上海地区，未公开明确的使用限制、维护周期等信息。

rss · HN Free API / Credits · 10月27日 23:46

**「为什么重要」** 对于需要批量获取上海地区政府补贴通知的开发者或相关从业者，该免费数据源可省去自行爬取、整理的成本，目前无公开使用费用。

**「可关注」** 可关注：该数据源仅覆盖上海地区，且未公开维护周期与使用规则，接入前需自行评估数据稳定性和合规性。

**标签**: `#limited-free`, `#api`

---