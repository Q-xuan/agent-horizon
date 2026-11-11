---
layout: default
title: "Horizon Summary: 2026-11-11 (EN)"
date: 2026-11-11
lang: en
---

> From 236 items, 21 important content pieces were selected

---

**Agent Harness Architecture**
1. [Goose v1.59.0 发布](#item-harness-arch-1) ⭐️ 8.8/10
2. [browser-use 1.0.0 架构重写](#item-harness-arch-2) ⭐️ 8.8/10
3. [DSPy 3.5.0 发布](#item-harness-arch-3) ⭐️ 8.8/10
4. [Cursor Projects 多人协作升级](#item-harness-arch-4) ⭐️ 5.8/10

**AI Agent Engineer**
1. [Durable execution 长程恢复](#item-agent-engineer-1) ⭐️ 8.0/10
2. [Gemini 4 Carbon 正式可用](#item-agent-engineer-2) ⭐️ 7.8/10
3. [Claude 新增 Sheets 等工具](#item-agent-engineer-3) ⭐️ 7.0/10
4. [AlphaProof Code 发布](#item-agent-engineer-4) ⭐️ 7.0/10
5. [Sage-Taiyi 元认知架构登顶 Taiyi-Bench](#item-agent-engineer-5) ⭐️ 7.0/10
6. [Flide 提出 ForkAttention 解耦决策推理](#item-agent-engineer-6) ⭐️ 7.0/10
7. [Bielik-11B-v3.1-Instruct 开源发布](#item-agent-engineer-7) ⭐️ 6.0/10
8. [Deletion Tuning 稀疏掩码微调引关注](#item-agent-engineer-8) ⭐️ 5.5/10

**AI Daily**
1. [Anthropic 路演 定价 $70–78](#item-ai-daily-1) ⭐️ 9.8/10
2. [OpenAI Upwork：AI改变自由职业需求](#item-ai-daily-2) ⭐️ 8.8/10
3. [Claude 发布 Whiteboards、Sheets 与 Data](#item-ai-daily-3) ⭐️ 8.8/10
4. [ChatGPT 新增商家管理功能](#item-ai-daily-4) ⭐️ 7.8/10
5. [OpenAI 发布教育 AI 指导研究](#item-ai-daily-5) ⭐️ 7.8/10
6. [Claude 扩展工件与 MCP 连接器](#item-ai-daily-6) ⭐️ 7.8/10
7. [Claude 交互连接器支持全应用嵌入](#item-ai-daily-7) ⭐️ 7.8/10

**AI Deals**
1. [小渔排班 永久免费公告](#item-ai-deals-1) ⭐️ 8.0/10
2. [切问学术双十一会员积分翻倍](#item-ai-deals-2) ⭐️ 7.0/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [Goose v1.59.0 发布](https://github.com/aaif-goose/goose/releases/tag/v1.59.0) ⭐️ 8.8/10

这是Goose agent harness的v1.59.0正式版本发布，核心新增延迟MCP工具支持、子代理跟进恢复能力、可配置实时语音参数、可配置GPT-Live端点/模型/密钥、ACP客户端标签会话过滤、goose-agent停止/审批/工具钩子；缺陷修复涵盖文档指南HTTP根路径适配、会话关键词搜索优化、会话数据库初始化隔离、Databricks OAuth令牌自动刷新等问题。

github · github-actions\[bot\] · Nov 10, 17:17

**「设计要点」** 运行时层面将会话数据库初始化与应用池隔离，避免初始化冲突；goose-agent新增停止/审批/工具钩子，支持扩展执行流控制；MCP工具新增延迟执行模式，适配异步工具场景。

**「改了什么」** 相对上一版本新增6项核心能力：延迟MCP工具执行、子代理完成后可跟进恢复、实时语音启动参数可配置、GPT-Live端点/模型/密钥可配置、ACP会话列表支持按客户端标签过滤、goose-agent开放停止/审批/工具钩子；修复7项问题，包括文档指南HTTP根路径适配、会话关键词搜索性能优化、会话数据库初始化隔离、Databricks OAuth令牌过期前自动刷新、调整compaction提示词避免被Opus 5.5判定为蒸馏等。

**Tags**: `#runtime`, `#tools`, `#mcp`, `#subagents`, `#permissions`

---

<a id="item-harness-arch-2"></a>
### [browser-use 1.0.0 架构重写](https://github.com/browser-use/browser-use/releases/tag/1.0.0) ⭐️ 8.8/10

browser-use 1.0.0 发布，彻底重写核心架构。版本删除 136,866 行代码（占库 80%），用直接运行在 Chrome DevTools Protocol 上的持久 Python REPL 替代原有实现，移除 DOM 序列化和 action schema 中间层。默认模型改为 Browser Use 网关的 \`bu-fast\`，默认浏览器改为云端实例，API key 统一为 \`BROWSER\_USE\_API\_KEY\`。基准测试显示得分最高提升 33 点，成本降低 2.7–5.2 倍，速度提升 2–3 倍。

github · gregpr07 · Nov 10, 02:04

**「设计要点」** 运行时改为基于 Chrome DevTools Protocol 的持久 Python REPL，模型直接生成 Python 代码单元并在浏览器执行，消除 DOM 序列化和 action schema 抽象层。工具调用通过 CDP 直连浏览器，结果直接回传模型，无中间序列化步骤。

**「改了什么」** 相对 0.x，1.0.0 删除全部中间抽象层，将运行时替换为 CDP 上的持久 Python REPL，默认模型改为 \`bu-fast\`、浏览器改为云端、\`max\_steps\` 默认值从 500 降至 100。新增流式响应、瞬态重试、上下文压缩、类型化结果、上传下载、密钥脱敏、域名限制、Web 搜索、Docker 镜像及 MCP 服务器。

**Tags**: `#runtime`, `#tools`, `#sandbox`

---

<a id="item-harness-arch-3"></a>
### [DSPy 3.5.0 发布](https://github.com/stanfordnlp/dspy/releases/tag/3.5.0) ⭐️ 8.8/10

DSPy 3.5.0 发布，包含破坏性 API 变更。ReActV2 取代 ReAct 成为默认 agent 模式，提供结构化 History 与类型化 submit 工具；RLM、Flex、GEPA 从实验性状态毕业。工具结果支持图片、文件等富媒体，RLM 新增可保存/重载的对话 History 与图像裁剪能力。底层 LM 层切换为轻量 lm15 引擎，LiteLLM 与 OpenAI Python 库变为可选依赖，安装体积从 206.7 MiB 降至 30.9 MiB，依赖数从 65 减至 25，导入耗时从 1.01 s 降至 0.49 s。XMLAdapter 成为默认适配器，model\_type=&quot;auto&quot; 成为默认路由，磁盘缓存默认禁用 pickle 且启用受限加载。

github · isaacbmiller · Nov 10, 16:25

**「设计要点」** RLM 与 Flex 在 Deno 沙箱中执行真实 DSPy 代码，通过 InterpreterPool 预热解释器，支持将图片裁剪与文本/图像混合子查询嵌入工具调用链。LM 调用统一走 lm15 轻量引擎，按 model\_type=&quot;auto&quot; 自动路由到原生 API family，绕过 LiteLLM/OpenAI 库。

**「改了什么」** ReActV2 成为默认 agent 模式，结构化 History 与类型化 submit 工具替换旧版 ReAct。RLM、Flex、GEPA 毕业为稳定 API。LM 层重构为可选依赖的 lm15 引擎，安装体积与导入耗时大幅下降。XMLAdapter 成为默认适配器，磁盘缓存默认安全化。

**Tags**: `#runtime`, `#tools`, `#memory`, `#planning`, `#subagents`

---

<a id="item-harness-arch-4"></a>
### [Cursor Projects 多人协作升级](https://cursor.com/blog/projects-multiplayer) ⭐️ 5.8/10

Cursor Projects 于 2026-11-10 宣布升级为多人协作模式。此前 Projects 仅支持单人多智能体工作区，现在团队可共享上下文、记忆和统一任务面板，人类与智能体在同一 workspace 协作。成员仍保留与协调器及 worker agent 的一对一本地上下文，上层新增共享上下文层存放需求文档、图表、技术规格和原型，决策对所有项目内 agent 可见。智能体可跨成员实时通信、自动协调任务顺序以避免合并冲突，新成员加入时上下文已预配置，该功能已向所有 Cursor 用户开放 beta 测试。

rss · Cursor Blog · Nov 10, 12:00

**「改了什么」** 相对单用户版本，Projects 新增团队共享上下文层、跨成员智能体实时通信与协调，以及统一任务看板。成员仍保留本地一对一 agent 上下文，但共享层使决策和文档对所有项目内 agent 可见，新成员加入时上下文已预配置。

**Tags**: `#memory`, `#planning`, `#subagents`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [Durable execution 长程恢复](https://martinfowler.com/articles/durable-execution-agents.html) ⭐️ 8.0/10

2026-11-10，Martin Fowler 网站发布 Kiran Prakash 的文章，解释 durable execution 模式。该模式要求运行时记录每次与外部世界交互步骤的结果；当进程崩溃、网络故障或出现未预期的现实行为时，程序重跑可跳过已完成步骤并基于记录重建状态。该模式面向耗时数天至数周、涉及多轮人与外部系统交互的长周期 Agent。文章未提供具体实现版本、性能数据或限制条件。

rss · Martin Fowler · Nov 10, 14:10

**「为什么重要」** 这是一篇来自权威实践者的架构模式解析，直接关联 coding agent 与 harness 的容错设计。文章将 durable execution 定位为运行时层面的恢复机制，而非应用层补丁，对长周期任务架构有参考价值。

**「可关注」** 可关注：运行时必须持久化外部交互结果，才能让重跑时跳过已完成步骤并重建状态。

**Tags**: `#orchestration`, `#harness`, `#coding-agent`

---

<a id="item-agent-engineer-2"></a>
### [Gemini 4 Carbon 正式可用](https://deepmind.google/blog/gemini-4-carbon-is-now-available/) ⭐️ 7.8/10

Google DeepMind 于 2026-11-10 宣布 Gemini 4 Carbon 模型正式可用（GA）。该公告为官方第一方发布，面向 AI agent 工程师开放测试与集成。当前未披露具体技术性能指标或 agent 定向改进细节。

rss · Google DeepMind · Nov 10, 16:03

**「为什么重要」** Gemini 4 Carbon 进入 GA，为 agent 评估管线增加新模型选项。但公告未附性能基准，实际效果需后续验证。

**「可关注」** 可关注：官方未提供性能对比基线，接入前需确认 latency 与 cost 及 coding 任务表现。

**Tags**: `#coding-agent`, `#eval`, `#harness`

---

<a id="item-agent-engineer-3"></a>
### [Claude 新增 Sheets 等工具](https://claude.com/resources/articles/sheets-whiteboards-data) ⭐️ 7.0/10

Anthropic 于 2026-11-10 在 Claude 内正式上线原生白板、表格与数据看板工具。此举发出模型厂商从纯 API 基础设施转向端到端工作平台的信号。对 AI agent 工程师而言，现有工具链与 harness 集成设计可能受影响，因为厂商可能用原生功能替代第三方工具，且这些工具未来或开放为 API 资源。目前尚不清楚这些原生工具的功能完整度与长期采用情况。

hackernews · Yorothegoat · Nov 10, 17:55 · [Discussion](https://news.ycombinator.com/item?id=50443716)

**「为什么重要」** 这值得今天看，因为它显示模型厂商正从提供能力转向直接承载工作流，可能重新定义 agent 可调用的工具边界。已发生的变化是 Anthropic 发布原生办公组件；尚未证实的影响是这些组件是否会成为 agent 工作流的标准接口，以及第三方工具集成是否会被逐步边缘化。

**「可关注」** 可关注：模型厂商正把第三方办公工具能力内建为原生功能，agent 工具链需评估长期依赖外部 SaaS 集成的风险，并跟踪这些原生组件开放 API 的节奏。

**「评论」** 社区存在分歧：一部分人基于 Claude Design 的先例，认为原生工具只会成为快速查看的备选，专业工作仍会留在 Figma 等专用工具；另一部分人则将其视为模型厂商全面替代 SaaS 套件的战略前奏，担忧 API 客户的业务场景被蚕食。

**Tags**: `#coding-agent`, `#harness`

---

<a id="item-agent-engineer-4"></a>
### [AlphaProof Code 发布](https://deepmind.google/blog/introducing-alphaproof-code/) ⭐️ 7.0/10

DeepMind 于 2026 年 11 月 10 日发布 AlphaProof Code，一个基于 AI 的形式化验证系统，使用证明助手（如 Lean）验证代码正确性。官方博客发布后，Hacker News 社区围绕其方法论及与自主编码代理的关联展开技术讨论。目前公开技术细节有限，具体实现机制和基准对比尚未披露。

hackernews · Google DeepMind · Nov 10, 12:11 · [Discussion](https://news.ycombinator.com/item?id=50439193)

**「为什么重要」** 该工作把形式化验证与 LLM 编码能力结合，可能改变代码正确性评估方式。社区已开始讨论其与经典编码代理的边界，这对设计验证型 agent 有直接参考价值。

**「可关注」** 可关注：形式化验证代理与经典编码代理的边界尚不清晰，社区已提出验证范围（spec 对比 implementation）和证明正确性的质疑。

**「评论」** 社区对 AlphaProof Code 的验证范围持谨慎态度，有人质疑在过往有 bug 的库上得出零缺陷结论的可靠性，也有人指出其可能仅验证实现而非规格。另有用户分享 AI 编写 Lean 证明时可能“作弊”或产生反向实现的实践经验，整体讨论集中在验证边界与代理能力定义上。

**Tags**: `#coding-agent`, `#eval`

---

<a id="item-agent-engineer-5"></a>
### [Sage-Taiyi 元认知架构登顶 Taiyi-Bench](https://huggingface.co/papers/2611.12762) ⭐️ 7.0/10

Hugging Face Daily Papers 于 2026-11-10 发布 Sage-Taiyi，一种用于科学发现的元认知 agent 架构。该架构通过显式监控与控制循环修订对证据、假设和未解决问题的理解，并据此自适应调整研究目标与推理方法选择。在 Taiyi-Bench（涵盖 265 个任务、50 篇论文、十个学科）上，Sage-Taiyi 在历史性再发现与开放式创意的全部八个指标上排名第一，总体得分 54.0，超过最强基线 AI Scientist-v2 的 47.9。原文内容截断，完整技术细节与五名专家指导的合作声明未获评估。

rss · Hugging Face Daily Papers · Nov 10, 00:00

**「为什么重要」** 该工作展示了元认知监控与自适应推理选择在 agent 编排中的可迁移设计模式，同时 Taiyi-Bench 为科学创意任务提供了新的标准化评估基准。这些模式对通用 agent 的记忆系统与评估框架设计有直接参考价值。

**「可关注」** 可关注：显式监控-控制循环结合自适应推理选择，为 agent 编排提供了可复用的设计模式，尤其适用于需要动态调整研究目标的复杂任务场景。

**Tags**: `#eval`, `#orchestration`, `#memory`

---

<a id="item-agent-engineer-6"></a>
### [Flide 提出 ForkAttention 解耦决策推理](https://huggingface.co/papers/2610.42148) ⭐️ 7.0/10

2026-11-10，Hugging Face Daily Papers 收录论文《Flide: Accelerating Decision Inference with Exact State Forking》（获 31 次 upvote）。Flide 是针对 LLM agent 决策模型（如 Jev）的精确推理引擎，通过 ForkAttention 将逻辑决策树结构与物理 flattened token 流执行解耦，消除 prefix recomputation 开销并避免输出概率失真。该引擎支持 standard attention 与 recurrent Gated DeltaNet 层，以 GPU-resident 索引导航请求依赖，保证精确算术。当前摘录 truncated，未提供生产环境性能基准或部署细节。

rss · Hugging Face Daily Papers · Nov 10, 00:00

**「为什么重要」** 决策模型正成为 LLM agent 快速 System One 执行的重要范式，但现有生成导向推理引擎无法有效支持此类工作负载。Flide 提出的解耦机制提供精确推理保证，可能影响后续 agent 推理引擎设计方向。不过该工作仍处论文阶段，缺乏实际部署验证。

**「可关注」** 可关注：ForkAttention 通过 GPU-resident 索引在 flattened token 流中维护逻辑树依赖的机制，是否可复用于其他需要树状推理的 coding agent 场景。

**Tags**: `#coding-agent`, `#harness`

---

<a id="item-agent-engineer-7"></a>
### [Bielik-11B-v3.1-Instruct 开源发布](https://www.reddit.com/r/LocalLLaMA/comments/1xsrg0l/speakleashbielik11bv31instruct_hugging_face/) ⭐️ 6.0/10

2026年11月10日，Reddit用户/u/jacek2023分享Bielik-11B-v3.1-Instruct的开源发布信息。该模型是11B参数多语言因果解码器模型，为Bielik 11B v3系列的更新版本，优化指令遵循、工具调用与推理能力，覆盖56种语言，侧重欧洲语言尤其是波兰语。模型训练采用三阶段流程：500B token预训练、26M样本SFT、基于修改版GRPO的跨14环境强化学习，使用SpeakLeash团队实现的ALLaMo开源框架完成，采用Apache 2.0许可，Hugging Face已提供GGUF格式权重。官方同时预告后续将推出相关决策模型与dflash工具。

reddit · r/LocalLLaMA · /u/jacek2023 · Nov 10, 16:30

**「为什么重要」** 该模型是当前少有的开源多语言工具调用友好型11B参数模型，对需要本地部署多语言coding agent的工程师有直接参考价值。但当前Reddit分享内容未提供性能基准、agent专项评估数据，具体能力表现需参考官方博客与模型卡片确认。

**「可关注」** 可关注：该模型提供GGUF格式权重、Apache 2.0许可，原生支持工具调用，覆盖56种语言且侧重欧洲语种，适合本地多语言agent场景的初步适配。

**Tags**: `#coding-agent`, `#open-source-llm`, `#multilingual`, `#tool-use`

---

<a id="item-agent-engineer-8"></a>
### [Deletion Tuning 稀疏掩码微调引关注](https://www.reddit.com/r/LocalLLaMA/comments/1xswmb7/the_surprising_effectiveness_of_deleting_weights/) ⭐️ 5.5/10

Reddit 帖子转述了 Deletion Tuning 方法：仅置零少于 0.05% 的权重（学习 transformer block gate projection 上的二值掩码），即能在监督微调、强化学习（可验证奖励）和 on-policy 蒸馏三个后训练场景下匹配全参数微调性能。该方法检查点体积缩小数百至数千倍，且强化学习场景中 prior-task 准确率接近基座，而 FFT、LoRA 及随机稀疏微调最多下降 5.4 分。作者通过 stable rank、spectrum drift 和 principal-weight overlap 分析，称 Deletion Tuning 的权重变更几何结构最接近 FFT。帖子附有 GitHub、HuggingFace、博客及 NeurIPS 2026 海报链接，但当前仅为社区转述，缺乏独立第三方复现报告。

reddit · r/LocalLLaMA · /u/Thrumpwart · Nov 10, 19:44

**「为什么重要」** 若结论可复现，该方法将后训练检查点体积压缩数个数量级，同时缓解灾难性遗忘，对需要持续更新能力的 coding agent 和长期运行系统有潜在效率收益。但目前仅见 Reddit 转述及作者自托管链接，尚未有独立论文或代码评审确认。

**「可关注」** 可关注：gate projection 上的极稀疏二值掩码（&lt;0.05%）被报告为足以匹配全参数微调，这提示后训练中权重改动的结构和位置可能比幅度更重要，但需独立验证其跨模型、跨任务的稳定性。

**Tags**: `#coding-agent`, `#sparse-fine-tuning`, `#llm-continual-learning`

---

## AI Daily

<a id="item-ai-daily-1"></a>
### [Anthropic 路演 定价 $70–78](https://www.anthropic.com/news/roadshow-launch) ⭐️ 9.8/10

Anthropic 启动 Class A 普通股 IPO 路演，拟发行 8.25 亿股，其中公司出售 8.0135 亿股，现有股东出售 2365 万股。发行价预计每股 70–78 美元，代码 ANT，拟在纳斯达克全球精选市场上市；承销商获 30 天期权，可额外购买最多 1.2375 亿股。SEC 注册声明已提交但尚未生效，生效前不得出售或接受购买要约。

rss · Anthropic News · Nov 10, 00:00

**「为什么重要」** 作为头部 AI 实验室的拟议 IPO，该事件属于 AI 行业具有高影响力的重大事件。

**「可关注」** 可关注：本次发行的 SEC 注册声明已提交但尚未生效，股票正式交易前需等待该声明生效。

**Tags**: `#lab`, `#industry`, `#policy`

---

<a id="item-ai-daily-2"></a>
### [OpenAI Upwork：AI改变自由职业需求](https://openai.com/index/ai-effect-on-freelance-work) ⭐️ 8.8/10

OpenAI与Upwork联合发布最新研究，揭示AI对自由职业市场的影响。研究发现自由职业工作需求发生转变，出现新的技能组合要求，且AI相关项目的预算与工时均呈增长趋势。该研究基于双方平台数据，未披露具体数值范围。

rss · OpenAI Blog · Nov 10, 07:00

**「为什么重要」** 该研究由OpenAI与Upwork联合开展，基于实际平台数据，为理解AI对劳动力市场的即时影响提供了可核对的一手观察。

**「可关注」** 可关注：AI相关自由职业项目呈现预算与工时双增，技能组合要求正在变化。

**Tags**: `#lab`, `#industry`, `#research`

---

<a id="item-ai-daily-3"></a>
### [Claude 发布 Whiteboards、Sheets 与 Data](https://claude.com/resources/articles/sheets-whiteboards-data) ⭐️ 8.8/10

Anthropic 正式推出 Claude Whiteboards 与 Claude Sheets 的 Beta 测试，同时将 Claude Dashboards 更名为 Claude Data 并全面上线。三款功能均面向所有付费 Claude 用户开放。Whiteboards 支持团队实时头脑风暴与主题聚类。Sheets 可生成带公式与格式的电子表格并追踪修改。Data 新增认证查询（Beta）、实时共享（Beta），支持缓存、设计系统与变更追踪。Team 计划默认开启全部功能，Enterprise 计划中 Whiteboards 与 Sheets 默认关闭，Data 于 2026 年 11 月 19 日自动开启。

rss · Claude Blog · Nov 10, 00:00

**「为什么重要」** 这三项功能将 Claude 从对话工具扩展为团队协同办公平台，减少跨工具切换成本。用户可在 Claude 内完成从头脑风暴、表格处理到数据可视化的全流程，并通过合作伙伴工具继续后续工作。

**「可关注」** 可关注：交互式连接器支持全屏或侧边栏模式，Whiteboards、Sheets、Data 均通过 Artifacts 嵌入对话流，Enterprise 管理员可在 Organization settings &gt; Artifacts 中调整默认开关。

**Tags**: `#lab`, `#product`, `#industry`

---

<a id="item-ai-daily-4"></a>
### [ChatGPT 新增商家管理功能](https://openai.com/index/introducing-businesses-chatgpt) ⭐️ 7.8/10

On November 10, 2026, OpenAI officially announced the launch of a business-focused feature in ChatGPT. The feature enables businesses to manage their information on the platform, gain insights into how their business is presented to users, and convert user interest into actionable results.

rss · OpenAI Blog · Nov 10, 10:00

**「为什么重要」** This marks ChatGPT&\#x27;s first dedicated service expansion to business scenarios, filling the gap of business information control and user interest conversion in AI conversation interfaces.

**「可关注」** Pay attention to: ChatGPT has added business information management and user interest conversion capabilities, extending its service coverage from individual users to commercial scenarios.

**Tags**: `#product`, `#industry`, `#lab`

---

<a id="item-ai-daily-5"></a>
### [OpenAI 发布教育 AI 指导研究](https://openai.com/index/closing-ai-guidance-gap-education) ⭐️ 7.8/10

OpenAI官方博客于2026年11月10日发布新的ThinkYoung研究，同时总结其EMEA地区教育合作项目的实践经验，核心聚焦缩小教育领域的AI指导缺口，明确将支持教师、提升AI素养、培养自主学习能力作为核心推进方向。

rss · OpenAI Blog · Nov 10, 09:00

**「为什么重要」** 当前教育场景AI应用快速普及但配套指导规范存在缺口，该研究为教育类AI产品的落地设计、教育机构的AI应用规划提供了官方参考方向。

**「可关注」** 可关注：教育类AI产品可参考教师支持、AI素养培养、自主学习引导三个方向设计功能。

**Tags**: `#lab`, `#industry`, `#policy`

---

<a id="item-ai-daily-6"></a>
### [Claude 扩展工件与 MCP 连接器](https://claude.com/resources/articles/more-ways-to-work-with-claude-sheets-whiteboards-and-interactive-connectors) ⭐️ 7.8/10

Anthropic 今日宣布扩展 Claude 产品矩阵，新增 Claude Sheets、Whiteboards、Data 三类协作工件，并升级基于 MCP 协议的交互式连接器。Claude Marketplace 已收录 9,000 余个连接器与插件，合作伙伴现可将 Adobe、Atlassian 等应用直接嵌入 Claude。Salesforce、NetSuite、Workday 插件（部分 beta）内置行业技能，支持销售、财务、HR 场景。企业版新增自动连接（beta）、细粒度权限管控、审计日志及隔离虚拟机，Claude Meetings 功能即将推出。

rss · Claude Blog · Nov 10, 00:00

**「为什么重要」** 此轮更新将 Claude 从开发者工具推向全团队知识工作场景，MCP 生态的 9,000 连接器标志着开放标准进入规模化落地阶段。企业级管控与隔离架构的完善，为 Claude 进入受监管行业提供了合规基础。

**「可关注」** 可关注：MCP 协议正成为 AI 与应用集成的开放标准，交互式连接器与工件类型的扩展意味着 coding agent 的上下文边界将从代码库延伸至企业全链路数据与协作工具。

**Tags**: `#lab`, `#product`, `#industry`

---

<a id="item-ai-daily-7"></a>
### [Claude 交互连接器支持全应用嵌入](https://claude.com/resources/articles/interactive-connectors-full-tool) ⭐️ 7.8/10

Anthropic 更新 Claude 交互连接器，支持第三方应用完整嵌入。用户可在 Claude 内打开 Asana、Notion、Adobe 等工具，与 Claude 同屏协作并实时审批修改。功能基于 MCP Apps 构建，面向开发者公开预览，支持跨 AI 应用运行。目前正在 Web 和 Claude 桌面端推出，覆盖所有套餐。

rss · Claude Blog · Nov 10, 00:00

**「为什么重要」** 这使用户无需切换标签页即可在原生应用环境中完成人机协作，减少上下文切换成本。基于开放 MCP 协议，开发者可构建跨平台的嵌入式应用，降低多 AI 应用集成门槛。

**「可关注」** 可关注：MCP Apps 公开预览已开放，开发者可基于 Model Context Protocol 构建跨 AI 应用的嵌入式界面。

**Tags**: `#product`, `#lab`, `#industry`

---

## AI Deals

<a id="item-ai-deals-1"></a>
### [小渔排班 永久免费公告](https://www.appinn.com/xiaoyu-shift-calendar-free/) ⭐️ 8.0/10

你看到的内容可能由第三方 AI 基于小众软件文章提炼总结而成，可能与原文真实意图存在偏差。不代表小众软件观点和立场。请&lt;a href=&quot;https://www.appinn.com/xiaoyu-shift-calendar-free/&quot; target=&quot;\_blank&quot;&gt;点击链接阅读原文&lt;/a&gt;细致比对和校验。&lt;br /&gt;&lt;br /&gt;轮班日历应用小渔排班（开发8年）自2026年10月起全功能永久免费，无广告、无订阅，仅保留自愿支持开发者的选项。该应用2018年上线，曾为付费应用，支持班次闹钟、工时薪资统计、班表导出、iCloud同步等功能，适配iPhone、iPad、Apple Watch等多设备，开发者承诺会继续长期维护更新。

rss · 小众软件 · Nov 10, 14:48

**「为什么重要」** 此前小渔排班为付费应用，曾进入国区App Store效率付费榜前2名，此次永久免费且无广告、无订阅，可降低轮班、倒班工作者的使用成本。

**「可关注」** 该应用支持iCloud同步、多设备小组件，适配苹果全系设备，开发者承诺长期维护更新，适合苹果生态内有轮班需求的用户。

**Tags**: `#free-tier`, `#promo`, `#limited-free`

---

<a id="item-ai-deals-2"></a>
### [切问学术双十一会员积分翻倍](https://www.appinn.com/qiewenpaper-1111/) ⭐️ 7.0/10

复旦大学 NLP 团队开发的学术工具「切问学术」推出双十一限时会员积分翻倍福利。活动期间订阅任意会员套餐（Plus、Pro、Max X2、Max X5，月付、年付均可）即可享受每月积分翻倍，单个账号最多可购买 12 个月，活动期间升级的老会员同样适用该福利，已购时长内的双倍积分在活动结束后仍按月发放；以 Pro 年付为例，全年积分从平时的 240 万提升至 480 万。新下载并登录客户端的用户额外赠送 1 万积分。

rss · 小众软件 · Nov 10, 06:46

**「为什么重要」** 双十一期间年付会员本身已有 15% 折扣，叠加积分翻倍后是全年入手的最优窗口。翻倍积分可支撑更多 Agent 任务、实验复现、综述撰写等高消耗学术操作，无需再刻意节省积分。

**「可关注」** 可关注：单个账号最多可购买 12 个月会员，活动期间升级的老会员同样享受双倍积分，新下载登录客户端额外赠送 1 万积分。

**Tags**: `#promo`, `#credits`, `#limited-free`, `#api`

---