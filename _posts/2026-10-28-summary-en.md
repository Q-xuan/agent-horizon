---
layout: default
title: "Horizon Summary: 2026-10-28 (EN)"
date: 2026-10-28
lang: en
---

> From 211 items, 18 important content pieces were selected

---

**Agent Harness Architecture**
1. [Codex rust-v0.165.0 发布](#item-harness-arch-1) ⭐️ 7.8/10
2. [pydantic-ai v2.63.0 发布](#item-harness-arch-2) ⭐️ 7.8/10
3. [pydantic-ai v2.62.0 发布](#item-harness-arch-3) ⭐️ 7.8/10

**AI Agent Engineer**
1. [Liquid AI LFM3 多模态模型发布](#item-agent-engineer-1) ⭐️ 7.8/10
2. [Old Ideas, Novel Problems 基准发布](#item-agent-engineer-2) ⭐️ 7.8/10
3. [Genie 4 世界模拟发布](#item-agent-engineer-3) ⭐️ 7.0/10
4. [Trajectory2Gym 论文提出工具智能体决策 grounded 合成框架](#item-agent-engineer-4) ⭐️ 7.0/10
5. [TraceTrial-Bench 评估 Agent Harness 可靠性](#item-agent-engineer-5) ⭐️ 7.0/10
6. [DynaFlow 自由形式多智能体编排](#item-agent-engineer-6) ⭐️ 7.0/10
7. [Anthropic 发布 Claude Opus 5.5](#item-agent-engineer-7) ⭐️ 6.0/10
8. [LiquidAI LFM3-1.7B 发布](#item-agent-engineer-8) ⭐️ 6.0/10
9. [Reddit 反驳 Cohere Qwen 3.8 安全指控](#item-agent-engineer-9) ⭐️ 5.5/10

**AI Daily**
1. [OpenAI 与 Oracle 扩大合作](#item-ai-daily-1) ⭐️ 8.8/10
2. [Retell 用 OpenAI 模型支撑月均 1 亿次通话](#item-ai-daily-2) ⭐️ 7.8/10
3. [1.3B OXR 登顶 OCR 三榜第一](#item-ai-daily-3) ⭐️ 5.5/10
4. [文心 Unlimited OCR 2 开源 KV Cache 降 96%](#item-ai-daily-4) ⭐️ 5.5/10
5. [智源AREX-2发布 27B模型刷新轻量基准](#item-ai-daily-5) ⭐️ 5.0/10

**AI Deals**
1. [上海补贴通知JSON feed 免费可用](#item-ai-deals-1) ⭐️ 6.0/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [Codex rust-v0.165.0 发布](https://github.com/openai/codex/releases/tag/rust-v0.165.0) ⭐️ 7.8/10

OpenAI Codex CLI 发布 rust-v0.165.0。新版本默认启用 memory v2 作为新建配置文件的记忆模型，并支持导入外部 agent 记忆。app-server API 增加实验性 attached thread forks，用于子代理线程派生。远程 MCP 工具请求在本地响应 future 被丢弃时自动取消，修复工具生命周期管理。新增内置 Google Cloud Vertex AI provider（model\_provider = &quot;gcp&quot;），且支持模型在对话中动态调整 reasoning effort。

github · github-actions\[bot\] · Oct 27, 20:09

**「设计要点」** Memory v2 默认启用并开放外部导入，改变 agent 长期记忆的持久化与跨实例同步边界。MCP 取消信号从本地 future 传播到远程服务端，要求工具层在 future 丢弃时主动终止远端执行。

**「改了什么」** 默认启用 memory v2 并支持外部 agent 记忆导入；app-server API 新增实验性 attached thread forks；远程 MCP 工具请求在本地 future 丢弃时自动取消；新增 GCP Vertex AI provider；对话内 reasoning effort 动态调整默认开启。

**Tags**: `#memory`, `#mcp`, `#subagents`, `#runtime`, `#tools`

---

<a id="item-harness-arch-2"></a>
### [pydantic-ai v2.63.0 发布](https://github.com/pydantic/pydantic-ai/releases/tag/v2.63.0) ⭐️ 7.8/10

pydantic-ai v2.63.0 发布，核心 harness 行为发生多项兼容性变更。默认 CodeMode 启用 dynamic\_catalog=True，工具揭示后追加目录而非重写缓存提示词；Harness LLMReminder 默认 interval=10，不再每次请求生成。新增签名加密历史向同 canonical\_system 提供商回放、IPythonCodeMode、DetectLoops 能力、PostgresSpendStore 及 ag-ui-protocol 1.0 支持，同时加入 OpenAI gpt-6.1-terra 模型。

github · dsfaccini · Oct 28, 00:55

**「设计要点」** 记忆层支持签名加密历史向同 canonical\_system 提供方回放，UI 适配器新增 manage\_message\_history 防止服务端历史重复发送。CombinedCapability 延迟加载改为整体加载并保持成员全局顺序，LLMReminder 默认间隔 10 次请求降低 token 消耗。

**「改了什么」** 默认工具目录从重写缓存改为追加模式；LLMReminder 默认生成间隔从每次请求改为每 10 次请求；新增加密历史回放、IPython 代码模式、循环检测能力及 PostgreSQL 预算共享存储。

**Tags**: `#runtime`, `#tools`, `#memory`

---

<a id="item-harness-arch-3"></a>
### [pydantic-ai v2.62.0 发布](https://github.com/pydantic/pydantic-ai/releases/tag/v2.62.0) ⭐️ 7.8/10

pydantic-ai v2.62.0 发布，核心变更覆盖运行时、工具层、记忆与错误处理。新增 \`ModelSettingsDeltaPart\` 支持对话中途通过 OpenAI \`configuration\_update\` 或 Anthropic 逐条 \`output\_config\` 调整 thinking effort，并在 OpenRouter 上保持 prompt cache；MCP 托管工具默认以服务名为前缀，可通过 \`tool\_prefix\` 配置。\`SummarizingCompaction\` 摘要改为 \`CompactionPart\` 存储并广播至所有模型，替代原有系统提示注入方式。新增 \`ModelRequestRejectedError\`、\`ModelAuthenticationError\` 和 \`ModelNotFoundError\` 三类模型错误，便于 harness 精确捕获失败原因；注意 \`GraphBuilder\` 广播分支改为按 \`.to\(\)\` 顺序执行，可能中断跨版本升级的持久工作流重放。

github · dsfaccini · Oct 27, 02:38

**「设计要点」** 该版本将压缩状态从系统提示拆分为独立的 \`CompactionPart\` 消息部件，实现 provider-less 广播，改变记忆层持久化格式。实时会话通过各 provider 的 operator channel 投递 \`SystemPromptPart\` 并要求工具调用失败时显式通知模型；\`SubAgents\` 引入 \`task\_control\` 支持后台任务控制，\`BatchModelRequests\` 提供批量 API 封装。

**「改了什么」** 支持对话中途动态调整 thinking effort（\`ModelSettingsDeltaPart\`），MCP 托管工具默认添加服务名前缀（可配置 \`tool\_prefix\`），压缩摘要改为 \`CompactionPart\` 广播，新增三类模型错误分类，\`SubAgents\` 支持 \`task\_control\` 后台任务，新增 \`BatchModelRequests\` 批量能力。注意 \`GraphBuilder\` 广播分支顺序变更可能破坏持久工作流重放，\`SystemReminders\` 构建方式变更且 \`cache\_ttl\` 弃用。

**Tags**: `#runtime`, `#tools`, `#mcp`, `#memory`, `#permissions`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [Liquid AI LFM3 多模态模型发布](https://huggingface.co/blog/LiquidAI/lfm3) ⭐️ 7.8/10

2026年10月27日，Liquid AI 发布 LFM3 多模态基础模型家族，为 2B 参数级规模，采用共享主干覆盖文本、视觉、音频、全模态、决策共 6 个模型变体。相比上一代 LFM2，LFM3 参数减少 35%，性能超过更大参数的 LFM2.5-2.6B，支持单 GPU 微调、边缘部署，文本模型 4-bit 精度下体积约 1GB，上下文窗口达 256K，其中决策模型面向智能体工作负载设计。当前公开内容未包含面向智能体的专项评估基准细节。

rss · Hugging Face Blog · Oct 27, 17:16

**「为什么重要」** 该发布是 Liquid AI 官方推出的新一代多模态模型家族，明确针对智能体场景优化架构，提供单卡微调与边缘部署能力，可降低专用多模态智能体的开发门槛。

**「可关注」** 可关注 LFM3 决策模型（d1-2B、d1-omni-2B）面向智能体工作负载的适配设计，以及单 GPU 微调、边缘部署的落地路径。

**Tags**: `#harness`, `#multimodal-model`, `#fine-tuning`, `#edge-deployment`

---

<a id="item-agent-engineer-2"></a>
### [Old Ideas, Novel Problems 基准发布](https://huggingface.co/blog/allenai/novelty-bench) ⭐️ 7.8/10

2026年10月27日，Hugging Face与Ai2联合发布「Old Ideas, Novel Problems」研究及配套开放基准、数据集、代码、自动化评估集构建流水线，用于测试大模型判断科研想法新颖性的可靠性。基准包含299个人工撰写科研想法（154个高新颖性样本来自ICLR 2026各领域Top10%接收论文，145个低新颖性样本来自Bottom10%拒稿论文，另有154个简单LLM生成的对应想法作为弱标签测试集），覆盖GPT-5.1/5.2/5.4、Claude Sonnet 4.5/Opus 4.5/Opus 4.6六款模型的判断能力测试。核心测试结果显示：提示词微调可导致同一想法对的判断准确率波动超50个百分点，检索与额外推理无法稳定提升判断效果，两款专用新颖性评估系统表现弱于简单提示的Claude Opus 4.6基线。该资源面向科研AI Agent开发者、评估工具链工程师，以及使用LLM做科研新颖性判断的研究团队。

rss · Hugging Face Blog · Oct 27, 16:12

**「为什么重要」** 当前科研AI Agent普遍采用LLM作为新颖性判断器，但此前缺乏标准化评估工具与公开测试集，该基准直接填补了这一空白，为相关评估工具链开发提供了可直接复用的基础资源；目前仅验证了现有LLM判断方案的可靠性不足，尚未证明可解决该问题。

**「可关注」** 可关注：novelty judge的评估结果对提示词、模型选择高度敏感，不同模型的最优提示不通用，现有检索与推理增强方案未体现稳定收益，构建相关评估harness时需优先固定提示与模型基线。

**Tags**: `#eval`, `#harness`

---

<a id="item-agent-engineer-3"></a>
### [Genie 4 世界模拟发布](https://deepmind.google/blog/genie-4-a-new-generation-of-world-simulation/) ⭐️ 7.0/10

DeepMind 于 2026-10-27 发布 Genie 4 世界模拟模型，主打实时仿真与先进音频能力。社区实测显示，画面内对象一致性较好，但出画再入画对象状态会突变（如龙再次出现时新增城堡、行人更换、骑手头盔凭空出现），音频提示与输出存在错配（要求萨克斯却输出单簧管），且强调真实感的提示词仍可能渲染出游戏风格。该模型对构建 agent 训练与评测流程的工程师有直接参考价值，但当前材料未包含完整技术架构与性能指标基线。另存在 Tencent HY-World 2.0 等开源权重替代方案。

hackernews · Google DeepMind · Oct 27, 16:06 · [Discussion](https://news.ycombinator.com/item?id=50261319)

**「为什么重要」** Genie 4 作为下一代世界模型选项，其真实感生成能力可扩展 agent 训练环境，但社区揭示的对象一致性与音频匹配缺陷意味着直接用于自动化评测流程前需额外验证。开源替代方案的存在也提供了对比基准。

**「可关注」** 可关注：Genie 4 在画面内对象保持与真实感生成上具备能力，但出画对象状态不一致、音频提示词与输出错配、以及特定长提示词下的风格退化，提示工程师在将其接入训练或评测流程时，需针对这些边界场景设计专项鲁棒性测试，而非仅依赖官方演示样本。

**「评论」** 社区讨论集中在 Genie 4 的实际使用缺陷：出画对象状态不一致、音频乐器识别错误、以及真实感提示词失效，同时提及 Tencent HY-World 2.0 开源权重模型未获同等关注。

**Tags**: `#eval`, `#harness`

---

<a id="item-agent-engineer-4"></a>
### [Trajectory2Gym 论文提出工具智能体决策 grounded 合成框架](https://huggingface.co/papers/2610.33568) ⭐️ 7.0/10

HF Daily Papers 于 2026-10-28 收录论文《Trajectory2Gym: Decision-Grounded Compositional Interaction Synthesis for Tool-Use Agents》，当前获 336 次 upvote。该框架针对现有成功工具使用轨迹缺乏决策依据与组合覆盖的问题，提出组合覆盖（compositional coverage）与决策 grounded（decision grounding）两个耦合要求，通过构造可执行交互并仅从 realized executions 中的 grounded 决策提取监督，以提升训练信号质量。当前材料仅为截断摘要，未提供完整技术细节、性能基准或代码链接，实际效果尚未验证。

rss · Hugging Face Daily Papers · Oct 28, 01:58

**「为什么重要」** 该论文直接针对工具使用智能体训练信号质量这一核心工程问题。已发生的变化是提出了一种新的轨迹生成与监督提取框架；尚未证实的是该方法在实际 agent 训练中的效果与效率提升。

**「可关注」** 可关注：现有成功轨迹可能包含决策时信息无法 justified 的动作，监督质量比轨迹表面成功率更关键。

**Tags**: `#coding-agent`, `#eval`

---

<a id="item-agent-engineer-5"></a>
### [TraceTrial-Bench 评估 Agent Harness 可靠性](https://huggingface.co/papers/2610.32285) ⭐️ 7.0/10

Hugging Face Daily Papers 于 2026-10-28 发布 TraceTrial-Bench，首个专门评估 AI agent harness 可靠性的 benchmark。该 benchmark 将 harness 可靠性拆分为 7 个组件（context、execution、governance、lifecycle、observability、tools、verification），构建 95 项专家级机制导向任务，并设计 Trajectory Tracing \(TT\) 模块捕获 agent 执行轨迹（原文截断）。现有 benchmark 多聚焦模型能力与整体 agent 性能，此工作填补了 harness 专项评估空白。影响范围：agent harness 工程师、eval 系统与工具链开发者。

rss · Hugging Face Daily Papers · Oct 28, 01:58

**「为什么重要」** 现有 agent 评估体系忽略 harness 层可靠性，导致 harness 设计缺陷难以量化对比。TraceTrial-Bench 提供结构化评估框架，使不同 harness 的可比性成为可能。

**「可关注」** 可关注：TraceTrial-Bench 的 7 组件分类与轨迹追踪模块为 harness 可观测性设计提供了可对照的评估维度。

**Tags**: `#eval`, `#harness`, `#observability`

---

<a id="item-agent-engineer-6"></a>
### [DynaFlow 自由形式多智能体编排](https://huggingface.co/papers/2610.34467) ⭐️ 7.0/10

Hugging Face Daily Papers 于 2026-10-28 推介 DynaFlow 多智能体编排研究。该框架将自由形式可执行工作流合成集成到主智能体动作空间，支持顺序或并行执行、结构化信息交换与验证，执行结果与轨迹可反馈至后续动作。仅对主智能体进行监督微调，使用蒸馏轨迹并过滤无前提支持、偏差验证及信息流缺陷的样本。目前未提供性能基准或生产部署细节。

rss · Hugging Face Daily Papers · Oct 28, 01:58

**「为什么重要」** 该研究提出仅训练主智能体的缺陷感知训练流程，为构建自适应多智能体系统提供可复现路径。但缺乏性能基准与部署验证，实际工程价值尚未证实。

**「可关注」** 主智能体动态生成任务特定程序协调子智能体的机制，以及缺陷过滤在轨迹微调中的具体实现。

**Tags**: `#orchestration`, `#eval`, `#multi-agent`

---

<a id="item-agent-engineer-7"></a>
### [Anthropic 发布 Claude Opus 5.5](https://latent.space/p/how_anthropic_ships_the_1_llm_in_the_world_safely_separating_the_brain_from_the_hands/) ⭐️ 6.0/10

Latent Space 播客发布 show notes，采访 Anthropic 工程师 Katelyn Lesse 与 Angela Jiang，介绍 Claude Platform 工程实践。内容涵盖 Opus 5.5 发布、将模型“大脑”与代理“双手”解耦、扩展托管代理、安全控制（隔离、凭证、网络策略）以及 Rust 重写 Messages API。show notes 仅提供高层概述，未包含深度技术细节，需访问链接的官方资源或完整视频获取可执行信息。时间戳显示话题从 S-1、效率指标、训练/生产事故分离，到代理评估、CPU 约束与 DevRel 建设。

rss · Latent Space · Oct 27, 18:40

**「为什么重要」** 该访谈直接面向代理工程师讨论 harness 架构与安全控制，并链接 Anthropic 官方关于托管代理与模型隔离的一手资料。但当前材料仅为摘要，具体实现细节与决策依据需进一步查看完整内容。

**「可关注」** Anthropic 在 Claude Platform 中分离模型、harness 与沙箱，并在生产环境采用网络隔离、凭证保护及训练/生产事故分离策略。

**Tags**: `#harness`, `#coding-agent`, `#permissions`, `#eval`

---

<a id="item-agent-engineer-8"></a>
### [LiquidAI LFM3-1.7B 发布](https://www.reddit.com/r/LocalLLaMA/comments/1xgy8s3/liquidailfm317b_hugging_face/) ⭐️ 6.0/10

2026年10月27日Reddit社区分享LiquidAI官方发布的LFM3-1.7B纯文本模型，该模型基于新型tri-hybrid架构，参数量1.73B，采用LFM Open License v1.0协议，针对Hermes Agent、Pi、OpenClaw等agentic harness完成专项后训练，支持256K token（输入+输出）上下文，4-bit精度下内存占用约1GB，可部署于手机、笔记本等端侧设备，官方明确不推荐用于agentic编程与复杂多步推理场景，llama.cpp已合并相关支持。

reddit · r/LocalLLaMA · /u/jacek2023 · Oct 27, 17:04

**「为什么重要」** 该模型为本地轻量agent场景提供了小参数、长上下文、端侧可部署的新选项，对寻求端侧小模型适配的工程师有参考价值，但目前未公开性能基准与评测数据，实际适配效果仍需进一步验证。

**「可关注」** 可关注：该模型4-bit精度下仅占约1GB内存，且llama.cpp已合并支持，适合端侧轻量agent场景的快速验证，但官方明确标注不推荐用于复杂多步推理和agentic编程，需结合实际场景评估适配性。

**Tags**: `#coding-agent`, `#harness`

---

<a id="item-agent-engineer-9"></a>
### [Reddit 反驳 Cohere Qwen 3.8 安全指控](https://www.reddit.com/r/LocalLLaMA/comments/1xgopmj/debunking_coheres_claim_of_qwen_38_flash_next/) ⭐️ 5.5/10

2026年10月27日Reddit用户/u/feelspeaceman发布分析帖，援引Cohere Labs公开的Hugging Face trace数据集，指出Cohere声称Qwen 3.8 Flash Next（Q38FN）自发生成阿里云远程URL的证据存在人为诱导：测试时预先填充2232个token，且使用的检测提示词模糊无上下文，本质是迫使模型扮演URL生成器。帖子同时提到Cohere CEO此前向媒体表示未掌握证据证明该行为是故意的，该行为出现频率低于十万分之一，发帖人称自己日常使用Q38FN的日志中从未出现相关阿里云URL。该分析为关注模型安全声明验证与eval方法设计的工程师提供了参考。

reddit · r/LocalLLaMA · /u/feelspeaceman · Oct 27, 10:19

**「为什么重要」** 该分析直接关联大模型安全声明的验证方法与eval prompt设计的严谨性，揭示了人工诱导的模型异常输出与模型自发安全风险的关键区分；但目前仅针对Cohere提出的单一具体指控展开反驳，未涉及更广泛的模型安全或架构层面的结论。

**「可关注」** 可关注安全类eval中预填充上下文长度与提示词模糊度对模型输出的诱导效应，避免将人工诱导的异常输出直接归因为模型自发安全风险。

**Tags**: `#eval`, `#prompt-engineering`, `#safety`

---

## AI Daily

<a id="item-ai-daily-1"></a>
### [OpenAI 与 Oracle 扩大合作](https://openai.com/index/oracle-apps-in-chatgpt) ⭐️ 8.8/10

OpenAI 官方于 2026 年 10 月 27 日宣布与 Oracle 扩大合作，合作核心方向为将业务应用及 AI agent 引入 ChatGPT，同时为 Oracle 新业务提供 AI 能力支撑。

rss · OpenAI Blog · Oct 27, 07:00

**「为什么重要」** 该合作将企业级业务场景与 AI agent 能力接入 ChatGPT，拓展了 ChatGPT 的企业服务边界，同时为 Oracle 新业务提供 AI 能力底座，是云服务与 AI 能力结合的企业级落地动作。

**「可关注」** 可关注后续 ChatGPT 针对 Oracle 业务应用及 AI agent 的集成方案、相关 API 更新及落地时间表。

**Tags**: `#lab`, `#industry`, `#product`

---

<a id="item-ai-daily-2"></a>
### [Retell 用 OpenAI 模型支撑月均 1 亿次通话](https://openai.com/index/retell-ai) ⭐️ 7.8/10

OpenAI&\#x27;s official blog discloses that voice AI firm Retell uses OpenAI models to power 100 million monthly calls. In Retell&\#x27;s internal voice agent benchmark, GPT-6 Astra ranks first. Codex helps Retell reach a $1.6 million annual revenue run rate per employee.

rss · OpenAI Blog · Oct 27, 15:00

**「为什么重要」** This is an official OpenAI voice AI deployment case, providing quantifiable business performance reference for the industry.

**「可关注」** Watch for: GPT-6 Astra&\#x27;s benchmark performance in voice agent scenarios, and Codex&\#x27;s contribution to business efficiency improvement.

**Tags**: `#lab`, `#model`, `#industry`, `#product`

---

<a id="item-ai-daily-3"></a>
### [1.3B OXR 登顶 OCR 三榜第一](https://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw==&amp;mid=2247936488&amp;idx=1&amp;sn=6ac0acdd138a429dbce62ca2d3a88b13) ⭐️ 5.5/10

量子位报道称，应用RSI技术的1.3B参数国产开源OXR模型登顶OmniDocBench、olmOCR-Bench、DocParsingBench三个OCR榜单第一，具备化学结构图解析能力；单张RTX PRO 6000显卡完成100页端到端文档解析耗时101秒，该模型已在GitHub获得1.1K+ Star，曾登上推特Daily News热榜。

rss · 量子位 · Oct 27, 06:13

**「为什么重要」** 该模型以小参数结合RSI技术实现多OCR榜单登顶，且覆盖化学结构图等特殊文档解析场景，为轻量级文档理解方案提供了可参考的落地案例，在海外开发者社区获得较高关注度。

**「可关注」** 可关注：1.3B参数OXR模型在文档解析任务上的精度-速度平衡表现，以及其对化学结构图等非标准内容的解析能力。

**Tags**: `#model`, `#open-source`, `#industry`, `#eval`

---

<a id="item-ai-daily-4"></a>
### [文心 Unlimited OCR 2 开源 KV Cache 降 96%](https://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw==&amp;mid=2247936488&amp;idx=2&amp;sn=286b1f5cae20ebec0f56b4ef14b6d081) ⭐️ 5.5/10

百度发布并开源文心 Unlimited OCR 2，该模型采用稀疏参考滑动窗口注意力机制（SR-SWA），宣称将 KV 缓存压缩为常数，峰值 KV 缓存从标准解码的 47GB 降至 1.77GB，降幅约 96%，支持无上限页数输入，可完成 3600+ 页《哈利·波特》全集、1200+ 页《三体》全集的连续识别转写。上一代 Unlimited OCR 累计下载量超 1000 万，GitHub 获约 2.86 万 Star。该信息为量子位二手科技媒体报道，无对应官方一手公告/博客佐证。

rss · 量子位 · Oct 27, 06:13

**「为什么重要」** 若其缓存压缩与无上限页数支持的效果属实，将突破长文档 OCR 的显存与序列长度限制，为超长文档的自动化处理提供新的可行方案。

**「可关注」** 可关注：其提出的稀疏参考滑动窗口注意力机制 SR-SWA，通过按需选取相关页面与视觉信息减少重复计算，配合持续解码机制让单步解码开销不随文档长度增长，为长序列 OCR 的缓存与算力优化提供了可参考的技术路径。

**Tags**: `#model`, `#open-source`, `#industry`

---

<a id="item-ai-daily-5"></a>
### [智源AREX-2发布 27B模型刷新轻量基准](https://mp.weixin.qq.com/s?__biz=MzA3MzI4MjgzMw==&amp;mid=2651070489&amp;idx=3&amp;sn=54e92cb2108bbc579873c8ccfaa114d3) ⭐️ 5.0/10

据机器之心2026年10月27日发布的二手行业报道，智源AREX研究小组发布AREX-2模型，该模型以Qwen3.8-27B为基座，基于机器学习与算法编程场景的长程反思数据训练，能力可迁移至深度研究与科学问题求解场景，在MLE-bench、Frontier-CS、BrowseComp、HLE基准上分别取得81.8、70.7、84.0、52.6的成绩，刷新开源轻量模型对应基准最佳表现，较上一代AREX有显著提升，为递归自我改进（RSI）探索出可训练、可验证的实现路径。当前报道未附官方一手发布链接，核心细节暂无法交叉核对，相关论文、项目代码与模型权重已公开可供查阅。

rss · 机器之心 · Oct 27, 04:03

**「为什么重要」** 当前递归自我改进（RSI）是研究者、创业者与投资人共同关注的前沿方向，AREX-2将RSI落地为可验证的测试时扩展范式，为轻量模型的自我改进能力探索提供了可复用的参考路径。

**「可关注」** 可关注：长程反思作为可跨领域迁移的元能力，其训练可优先选择反馈清晰、可验证的机器学习与算法编程场景作为切入点。

**Tags**: `#model`, `#lab`, `#industry`

---

## AI Deals

<a id="item-ai-deals-1"></a>
### [上海补贴通知JSON feed 免费可用](https://github.com/ZhongGheart/china-policy-data) ⭐️ 6.0/10

公开GitHub仓库\`china-policy-data\`由subsidyradar维护，提供免费的上海政府补贴通知每日JSON数据feed，可直接访问获取，无明确使用成本。该数据源仅覆盖上海地区，使用规则与维护周期未公开，无明确截止时间。

rss · HN Free API / Credits · Oct 27, 23:46

**「为什么重要」** 该数据源提供结构化的上海补贴通知数据，无需付费即可获取，可省去自行爬取、清洗的成本，对需要相关数据的用户有实用价值。

**「可关注」** 可关注：该feed仅覆盖上海地区，且未公开使用限制与维护周期，接入前需自行评估数据稳定性和合规性。

**Tags**: `#limited-free`, `#api`

---