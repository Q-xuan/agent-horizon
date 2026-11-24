---
layout: default
title: "Horizon Summary: 2026-11-24 (EN)"
date: 2026-11-24
lang: en
---

> From 205 items, 14 important content pieces were selected

---

**Agent Harness Architecture**
1. [Codex rust-v0.172.0 发布](#item-harness-arch-1) ⭐️ 7.8/10
2. [pydantic-ai v2.73.0 发布](#item-harness-arch-2) ⭐️ 7.8/10
3. [Agents SDK alpha.2 发布](#item-harness-arch-3) ⭐️ 7.8/10

**AI Agent Engineer**
1. [NariQ 发布 Qwen3 3-bit 量化](#item-agent-engineer-1) ⭐️ 8.0/10
2. [AutoPILOT 实时游戏 Agent 发布](#item-agent-engineer-2) ⭐️ 7.0/10
3. [Self-WSP 模型自改权重提升数学能力](#item-agent-engineer-3) ⭐️ 7.0/10
4. [GameAnything 多模态游戏开发平台论文发布](#item-agent-engineer-4) ⭐️ 7.0/10
5. [GameDojo 实时交互智能体基准发布](#item-agent-engineer-5) ⭐️ 7.0/10
6. [datasette-charts 0.2a0 发布](#item-agent-engineer-6) ⭐️ 6.8/10
7. [RoboTrack 点追踪基准发布](#item-agent-engineer-7) ⭐️ 6.3/10

**AI Daily**
1. [OpenAI 与 Cisco 发布 Shirudo](#item-ai-daily-1) ⭐️ 7.8/10
2. [OpenAI 探讨内部法务AI应用](#item-ai-daily-2) ⭐️ 5.8/10

**AI Deals**
1. [Koofr 1TB Lifetime Plan $129.9 Return](#item-ai-deals-1) ⭐️ 7.0/10
2. [土区 Gemini Pro/Plus 年付半价](#item-ai-deals-2) ⭐️ 7.0/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [Codex rust-v0.172.0 发布](https://github.com/openai/codex/releases/tag/rust-v0.172.0) ⭐️ 7.8/10

OpenAI Codex CLI 发布 rust-v0.172.0。本次更新为 MCP 运行时添加懒启动机制，缓存工具列表的 stdio 服务器默认延迟到首次工具调用时启动。新增 per-app tool approval reviewer 配置、嵌套 agent 导航与任务组切换快捷键，并修复 \`codex exec resume\` 的沙箱权限丢失及跨操作系统远程会话工作区一致性问题。Code Mode 主机连接全面迁移至 gRPC，弃用 \`code\_mode\_host\_grpc\` 配置。

github · github-actions\[bot\] · Nov 24, 00:03

**「设计要点」** MCP 运行时将工具目录缓存与进程生命周期解耦，空闲 stdio 服务器无需常驻。工具审批策略从全局配置下沉到单个 connected app 维度，支持独立 reviewer。

**「改了什么」** 可选 stdio MCP 服务器默认改为首次工具调用时懒启动，\`codex exec resume\` 恢复保存的沙箱权限、工作目录与 workspace roots，远程会话跨操作系统时保持工作目录、可写路径和 workspace roots 一致。终端内新增线程链接打开嵌套 agent、任务组 \`Shift+Up\`/\`Shift+Down\` 切换及 slash 命令 \`Tab\` 参数补全。

**Tags**: `#runtime`, `#mcp`, `#sandbox`, `#tools`, `#permissions`

---

<a id="item-harness-arch-2"></a>
### [pydantic-ai v2.73.0 发布](https://github.com/pydantic/pydantic-ai/releases/tag/v2.73.0) ⭐️ 7.8/10

pydantic-ai v2.73.0 发布。本次更新引入 agent 能力覆写、OpenAI 输入转换缓存可见性、GPT-Live 实时语音会话支持，并包含一处破坏性变更：私有上下文变量 \`Agent.\_override\_root\_capability\` 的取值从单一 capability 改为 \`\(capability, injected\)\` 元组，直接读取该变量的代码需要修改。同时默认模型调整为 \`openai:gpt-6.1-sol\`，并废弃 Claude、Gemini、Grok 的统一设置下发。

github · dsfaccini · Nov 24, 03:53

**「设计要点」** \`Agent.override\` 新增 \`capabilities\` 字段，配套导出 \`AgentInstructions\` 与 \`SourcedInstruction\`，将能力覆写与指令溯源显式化。私有上下文变量 \`Agent.\_override\_root\_capability\` 改为携带注入状态的元组，表明运行时在能力解析层增加了注入来源追踪。OpenAI Responses 的 \`input\_transformations\` 现在暴露于 \`provider\_details\` 与模型请求 span，便于 harness 观测前缀缓存命中细节。

**「改了什么」** 破坏性变更：\`Agent.\_override\_root\_capability\` 上下文变量改为 \`\(capability, injected\)\` 元组，直接读取需更新。功能层面，\`Agent.override\` 新增 \`capabilities\` 字段并导出 \`AgentInstructions\` 与 \`SourcedInstruction\`；\`RealtimeSession.append\_voice\_instructions\` 与 Twilio Media Streams 桥接示例上线，支持 GPT-Live 语音模型；OpenAI \`input\_transformations\` 暴露到 \`provider\_details\` 与请求 span，\`openai\` 依赖 floor 提升至 3.50.0；\`SubAgents\` 可传递延迟工具调用，\`E2BSandbox\` 新增 \`idle\_timeout\`。配置与依赖层面，\`clai\` 默认模型改为 \`openai:gpt-6.1-sol\`，废弃 Claude、Gemini、Grok 统一设置下发；\`coder\` 额外依赖增加 \`pillow&gt;=12.3.0\` 且图片最长边默认限 1024 像素；\`boxd\` 额外要求 \`&gt;=0.3.3,&lt;0.4\`。

**Tags**: `#runtime`, `#prefix-cache`, `#compatibility`

---

<a id="item-harness-arch-3"></a>
### [Agents SDK alpha.2 发布](https://github.com/openai/openai-agents-python/releases/tag/v1.0.0-alpha.2) ⭐️ 7.8/10

OpenAI Agents SDK v1.0.0-alpha.2 预览版新增跨worker对话恢复、Codex原生批准恢复、工具执行钩子与过滤、Runner文本脱敏及操作追踪。持久化状态格式从schema 1.22升级到1.24，ResumableSession checkpoint升级到版本2，要求先升级reader再升级writer。运行时嵌入Codex Core rust-v0.166.0，支持CPython 3.10-3.14虚拟环境。

github · markstuart-oai · Nov 23, 20:11

**「设计要点」** 运行时嵌入Codex Core rust-v0.166.0。状态恢复通过ResumableSession和ResumableSessionStore实现，支持Redis或原子条件写入存储。工具层提供ToolExecutionConfig，含prepare\_tool\_input/output/declaration钩子，同步PreToolUse失败会阻止原生调度。追踪支持OpenTelemetry导出，文本脱敏通过RunConfig.redact\_text回调实现。

**「改了什么」** 新增ResumableSession支持跨worker恢复对话和待处理批准，可恢复本地单环境中的原生Codex exec\_command和apply\_patch批准。新增ToolExecutionConfig配置工具执行钩子及过滤可用函数工具。新增Runner文本脱敏和操作追踪选项，支持OpenTelemetry导出。持久化状态格式升级，RunState schema从1.22变为1.24，ResumableSession checkpoint升级到版本2，alpha.1无法读取新快照。

**Tags**: `#runtime`, `#tools`, `#memory`, `#permissions`, `#sandbox`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [NariQ 发布 Qwen3 3-bit 量化](https://huggingface.co/nari-labs/Qwen3.8-27B-NariQ-GGUF) ⭐️ 8.0/10

2026年11月23日，NariQ发布Qwen3.8-27B的3-bit及更低比特量化模型，文件大小约10GB，公开benchmark显示3-bit版本在DeepSWE（41.0 vs BF16 39.8）、Terminal-Bench 2.1（63.8 vs BF16 62.6）等长周期agentic任务上性能接近或超过BF16基线，同时覆盖数学、多语言推理、图像理解场景。当前运行该量化模型需要专属的nari-labs llama.cpp fork，在RTX PRO 6000上解码速度与其他公开量化相当，4K/16K/64K上下文长度下的性能也有公开数据，2-bit版本性能出现明显下降。该成果对coding agent轻量化部署、eval基准测试、工具链适配有直接参考价值。

hackernews · toebee · Nov 23, 13:42 · [Discussion](https://news.ycombinator.com/item?id=50611402)

**「为什么重要」** 它首次公开了3-bit及以下量化在长周期agentic任务上保持BF16级别性能的可验证benchmark，为低资源场景下的coding agent部署提供了新的可选方案，但专属运行时的依赖增加了落地适配成本，实际效果仍需更多 workload 验证。

**「可关注」** 可关注：3-bit及以下量化在agentic任务上的精度保持上限，以及专属llama.cpp fork的兼容性、性能损耗与长期维护成本。

**「评论」** 社区对量化精度提出质疑，有用户认为benchmark中的性能增益可能来自评估harness差异而非模型本身，也有用户关注该量化版本在16GB Mac等消费级硬件上的适配可能性，同时期待不同量化方法的标准化横向对比基准。

**Tags**: `#eval`, `#coding-agent`, `#harness`, `#toolchain`

---

<a id="item-agent-engineer-2"></a>
### [AutoPILOT 实时游戏 Agent 发布](https://huggingface.co/papers/2611.28202) ⭐️ 7.0/10

2026年11月24日Hugging Face Daily Papers发布论文介绍AutoPILOT实时游戏视觉Agent Harness，该论文当日获得26次upvote。该工具针对现有Harness（如VISTA）每次模型调用最多输出1个动作、无法匹配不等待模型输出的实时游戏环境的问题，支持单次模型调用输出原始动作、开环宏或自包含闭环控制器，无需额外模型调用即可持续执行直到交还控制权。配套的AFK-Bench基准包含120款浏览器游戏用于评估实时Agent，但原文对游戏分类维度的描述被截断，信息不完整。该成果属于Harness、评估、编排方向，主要面向交互式Agent Harness设计、游戏AI研发的工程师。

rss · Hugging Face Daily Papers · Nov 24, 00:00

**「为什么重要」** 已发生的变化是AutoPILOT填补了现有Agent Harness在实时不等待环境下的动作输出频率匹配空白，这是交互式Agent落地的关键瓶颈之一。尚未证实的是该设计能否迁移到游戏外的实时交互场景（如实时网页操作、物理控制）并带来同等收益。

**「可关注」** 可关注：现有Agent Harness普遍将单次模型调用与单次动作输出绑定，是实时交互环境下的核心性能瓶颈，可参考AutoPILOT的解耦思路设计更适配高频率环境的输出接口。

**Tags**: `#harness`, `#eval`, `#orchestration`

---

<a id="item-agent-engineer-3"></a>
### [Self-WSP 模型自改权重提升数学能力](https://huggingface.co/papers/2611.28833) ⭐️ 7.0/10

Hugging Face Daily Papers 2026-11-24 介绍 Self-WSP 论文。Qwen3.5-0.8B 通过 Weight-Space Programming 读取并编辑自身权重，GSM8K 从 11.8% 升至 62.2%，MATH500 从 7.0% 升至 32.2%，部分案例仅改 16 个参数，重复自编辑可继续提升。但编辑不可解释，模型对修改缺乏理解，离生产部署仍有距离。

rss · Hugging Face Daily Papers · Nov 24, 00:00

**「为什么重要」** 该工作展示极简权重编辑即可让小模型数学能力大幅跃升，对 LLM 自改进与 eval 设计有参考价值。但编辑不可解释，对模型可观测性与生产安全构成未解决风险。

**「可关注」** 可关注：Self-WSP 以极少参数改动实现数学 benchmark 大幅提升，但编辑不可解释，eval 分数跃升未必对应真实能力提升。

**Tags**: `#eval`, `#observability`, `#harness`

---

<a id="item-agent-engineer-4"></a>
### [GameAnything 多模态游戏开发平台论文发布](https://huggingface.co/papers/2611.29238) ⭐️ 7.0/10

2026年11月24日Hugging Face Daily Papers收录GameAnything相关论文，该论文提出开源智能体平台GameAnything，可将多模态灵感转化为现有游戏的可玩扩展，核心集成编码智能体、独立试玩评判器、持久开发状态与可复用经验记忆以支持迭代优化，同时配套跨多模态参考、游戏创建目标与游戏环境的GameAnything-Bench基准；当前仅公开摘要，无详细性能数据与实现细节。

rss · Hugging Face Daily Papers · Nov 24, 00:00

**「为什么重要」** 该工作明确了多模态游戏开发智能体的组件组合方案与配套评估基准，为相关方向的智能体架构设计、记忆机制实现、评估体系构建提供了可参考的公开方向，但具体性能与落地效果暂无公开数据验证。

**「可关注」** 可关注其编码智能体、试玩评判器、持久开发状态、可复用经验记忆的组合架构，以及GameAnything-Bench的评估维度设计。

**Tags**: `#coding-agent`, `#eval`, `#memory`, `#harness`

---

<a id="item-agent-engineer-5"></a>
### [GameDojo 实时交互智能体基准发布](https://huggingface.co/papers/2611.30771) ⭐️ 7.0/10

2026年11月24日 Hugging Face 日报收录 arXiv 预印本，发布 GameDojo 实时交互游戏智能体基准，覆盖 20 款游戏的 120 个 Boss 遭遇场景，由 coding agent 重建游戏环境并编写脚本生成配套 600 小时游戏轨迹数据集。实验显示前沿模型在实时交互场景存在明显能力短板，基于数据集训练的 4B 参数 GameDojo-4B 模型达到前沿实时交互性能，同时验证联合训练可提升单任务表现。该基准面向智能体评估、agent harness 开发、coding agent 环境构建等场景开放。

rss · Hugging Face Daily Papers · Nov 24, 00:00

**「为什么重要」** 该基准直接面向实时交互 agent 评估场景，公开的数据集与模型结果为相关开发者提供了可复用的对照基线，尚未证实对具体生产项目的直接增益。

**「可关注」** 可关注：GameDojo 公开的 600 小时游戏轨迹数据集与 GameDojo-4B 基线可作为实时交互 agent 的对照参考，联合训练提升单任务表现的结论可纳入多任务 agent 训练的设计考量。

**Tags**: `#eval`, `#harness`, `#coding-agent`, `#interactive-agents`

---

<a id="item-agent-engineer-6"></a>
### [datasette-charts 0.2a0 发布](https://github.com/datasette/datasette-charts/releases/tag/0.2a0) ⭐️ 6.8/10

simonw 于 2026-11-24 发布 datasette-charts 0.2a0。该 alpha 版本集成 Datasette Agent，为 agent 提供绘图工具（链接到面板图表构建器）与图表建议工具；新增 \`decade\` 时间单位，适用于跨世纪列；同时修复跳桶折线图渲染，使数据点以连接线呈现而非孤立点。

github · simonw · Nov 24, 04:24

**「为什么重要」** 这是 Datasette 生态中 agent 与可视化插件集成的具体案例，可作为 coding agent 工具调用模式的参考。当前为 alpha 版本，功能与稳定性尚未完全验证。

**「可关注」** 可关注：Datasette Agent 通过插件向 agent 暴露工具（绘图、建议）的集成方式，以及 alpha 版本中时间粒度与稀疏数据渲染的边界处理。

**Tags**: `#coding-agent`, `#harness`

---

<a id="item-agent-engineer-7"></a>
### [RoboTrack 点追踪基准发布](https://huggingface.co/blog/allenai/robotrack) ⭐️ 6.3/10

2026年11月23日，Hugging Face博客发布Allen AI的RoboTrack项目，包含面向真实世界机器人操控的点追踪基准、1500万条合成训练数据、两款新模型及开源技术报告。核心基准RoboTrack-Bench覆盖307段来自DROID、Ego-Exo4D等数据集的人工标注视频，共2522条点轨迹，包含杂乱场景、多视角、目标遮挡等真实操控难点；配套的RoboTrack-15M来自MolmoSpaces仿真环境，用于点追踪模型训练。评估显示4款主流追踪器在该基准上的平均Jaccard（AJ）得分比现有机器人基准低3.0至6.6分，使用RoboTrack-15M训练可提升真实操控视频的追踪表现，且增益可泛化到其他追踪基准，其中RoboTracker-Warp在5个评估基准中4个达到SOTA。该项目主要服务于具身智能、机器人Agent的感知模块研发与评测工程师。

rss · Hugging Face Blog · Nov 23, 17:20

**「为什么重要」** 它首次针对真实机器人操控场景构建了专用点追踪评测基准，揭示了现有追踪器在杂乱、遮挡场景下的普遍性能缺口，为相关感知模块的优化提供了可量化的评估标准。目前该项目仅对具身智能、机器人Agent的感知细分领域有直接参考价值，对通用Agent工程的影响尚未证实。

**「可关注」** 可关注：使用RoboTrack-15M合成数据对现有点追踪模型进行微调，可提升其在真实机器人操控视频上的追踪精度，且增益可泛化到其他追踪基准。

**Tags**: `#eval`

---

## AI Daily

<a id="item-ai-daily-1"></a>
### [OpenAI 与 Cisco 发布 Shirudo](https://openai.com/index/introducing-shirudo) ⭐️ 7.8/10

OpenAI 与 Cisco 联合发布开源 Linux runtime Shirudo。该工具用于在补丁 rollout 期间保护运行中的系统。官方博客确认发布，暂无版本号、性能指标及社区讨论。

rss · OpenAI Blog · Nov 23, 21:20

**「可关注」** 可关注：Shirudo 作为开源 Linux runtime，可在补丁 rollout 时保护运行中系统。

**Tags**: `#lab`, `#industry`, `#open-source`, `#product`

---

<a id="item-ai-daily-2"></a>
### [OpenAI 探讨内部法务AI应用](https://openai.com/business/learn/connected-intelligence-for-in-house-legal) ⭐️ 5.8/10

OpenAI published an official blog post on November 23, 2026, featuring a discussion with legal industry partners LECG and Cooley on AI use cases for in-house legal teams. The discussion covers three core directions: connecting business context, building reusable workflows, and optimizing outside counsel usage. No new models, products, or policy adjustments were announced in the content.

rss · OpenAI Blog · Nov 23, 08:00

**「为什么重要」** The discussion outlines practical paths for AI adoption in vertical legal scenarios, offering reference value for teams building in-house legal AI workflows.

**「可关注」** Focus: AI implementation for in-house legal scenarios can prioritize two core needs: associating business context and building reusable workflows.

**Tags**: `#lab`, `#industry`

---

## AI Deals

<a id="item-ai-deals-1"></a>
### [Koofr 1TB Lifetime Plan $129.9 Return](https://www.appinn.com/koofr-1tb/) ⭐️ 7.0/10

The content you see may be summarized by third-party AI based on an Appinn article, and may deviate from the original intent. It does not represent the views and positions of Appinn. Please &lt;a href=&quot;https://www.appinn.com/koofr-1tb/&quot; target=&quot;\_blank&quot;&gt;click the link to read the original article&lt;/a&gt; for careful comparison and verification.&lt;br /&gt;&lt;br /&gt;Appinn shares a Koofr cloud storage promotion. The service offers a permanent free 10GB storage tier. Users can purchase a 1TB lifetime subscription for $129.9 via StackSocial with coupon code KOOFR. It supports WebDAV and Rclone.

rss · 小众软件 · Nov 24, 03:24

**「Why It Matters」** This is a returning promotion. The $129.9 lifetime 1TB plan has far lower long-term costs than Koofr&\#x27;s official annual tiers \(100GB for €19.67/year, 500GB for €68.85/year\). It suits users needing low-cost long-term backup or cross-cloud sync.

**「Engineer Takeaway」** Pay attention: Rclone natively supports Koofr, so you can use it for server file backup directly. The free 10GB tier lets you test compatibility before purchasing the lifetime plan.

**Tags**: `#free-tier`, `#promo`, `#coupon`

---

<a id="item-ai-deals-2"></a>
### [土区 Gemini Pro/Plus 年付半价](https://www.v2ex.com/t/1259288#reply22) ⭐️ 7.0/10

V2EX用户spediacn分享土耳其区Google Gemini AI Pro/Plus年付半价促销，Pro年付3599.99土耳其里拉，Plus年付999.99土耳其里拉，到期后续费分别涨至8999.99、1999.99土耳其里拉/年。该促销未明确标注活动有效期与参与限制，仅面向土耳其区用户。

rss · V2EX Hot · Nov 23, 18:35

**「可关注」** 可关注：土耳其区用户可留意该地区性年付半价促销，注意后续续费价格较首年涨幅明显，且需确认活动规则与自身账号归属地是否符合要求。

**Tags**: `#promo`, `#limited-region`

---