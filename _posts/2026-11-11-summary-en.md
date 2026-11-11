---
layout: default
title: "Horizon Summary: 2026-11-11 (EN)"
date: 2026-11-11
lang: en
---

> From 196 items, 17 important content pieces were selected

---

**Agent Harness Architecture**
1. [Goose v1.59.0 发布](#item-harness-arch-1) ⭐️ 8.8/10
2. [DSPy 3.5.0 发布](#item-harness-arch-2) ⭐️ 8.8/10
3. [pydantic-ai v2.67.0 发布](#item-harness-arch-3) ⭐️ 7.8/10
4. [Cursor Projects 升级多人协作](#item-harness-arch-4) ⭐️ 6.8/10

**AI Agent Engineer**
1. [长周期 agent durable execution 介绍](#item-agent-engineer-1) ⭐️ 8.0/10
2. [Meta Muse Ember 1.0 发布](#item-agent-engineer-2) ⭐️ 7.0/10
3. [Claude Fable 5.2 代码所有权提示](#item-agent-engineer-3) ⭐️ 7.0/10
4. [Naive-N0.5-Flash 编码速度实测](#item-agent-engineer-4) ⭐️ 7.0/10
5. [Gemini 4 Carbon 发布](#item-agent-engineer-5) ⭐️ 6.8/10
6. [DeepMind 发布 AlphaProof Code](#item-agent-engineer-6) ⭐️ 6.0/10
7. [Deletion Tuning 后训练技术引关注](#item-agent-engineer-7) ⭐️ 6.0/10

**AI Daily**
1. [ChatGPT 上线 Businesses 功能](#item-ai-daily-1) ⭐️ 7.8/10
2. [OpenAI Upwork 发布自由职业研究](#item-ai-daily-2) ⭐️ 7.8/10
3. [Git 2.56.1 修复6个安全漏洞](#item-ai-daily-3) ⭐️ 7.8/10
4. [OpenAI Academy 护理人员 ChatGPT 工作坊](#item-ai-daily-4) ⭐️ 6.8/10

**AI Deals**
1. [小渔排班永久免费](#item-ai-deals-1) ⭐️ 8.0/10
2. [切问学术 双十一积分翻倍](#item-ai-deals-2) ⭐️ 7.0/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [Goose v1.59.0 发布](https://github.com/aaif-goose/goose/releases/tag/v1.59.0) ⭐️ 8.8/10

block/goose 发布 v1.59.0，ToolExecutionOperation 新增最小化延迟 MCP 工具，子代理委托支持完成后带后续消息恢复，goose-agent \(GDK\) 新增 stop、approval、tool 三类钩子。ACP 客户端标签过滤扩展会话查询维度，live-voice 与 GPT-Live 配置项同步开放。

github · github-actions\[bot\] · Nov 10, 17:17

**「设计要点」** ToolExecutionOperation 引入延迟 MCP 工具，GDK 提供三层钩子直接作用于 goose-agent 运行时，子代理委托恢复机制延长子任务生命周期，ACP 标签过滤扩展会话查询维度。

**「改了什么」** ToolExecutionOperation 支持最小化延迟 MCP 工具，子代理委托支持完成后带后续消息恢复，goose-agent \(GDK\) 新增 stop、approval、tool 三类钩子，ACP 增加客户端标签会话过滤，live-voice 与 GPT-Live 配置项开放。

**Tags**: `#mcp`, `#tools`, `#subagents`, `#permissions`, `#runtime`

---

<a id="item-harness-arch-2"></a>
### [DSPy 3.5.0 发布](https://github.com/stanfordnlp/dspy/releases/tag/3.5.0) ⭐️ 8.8/10

DSPy 3.5.0 是 stanfordnlp/dspy 的大版本更新，将 LM 运行时切换为内置轻量 lm15 引擎，LiteLLM 与 OpenAI Python 库变为可选依赖。RLM、Flex、GEPA 从实验模块毕业，ReActV2 以 \`dspy.ReAct\` 替代旧版 ReAct，提供结构化 History 和类型化 \`submit\` 工具，工具返回值支持图片、文件等多模态内容。默认适配器改为 XMLAdapter，API 族路由默认 \`model\_type=&quot;auto&quot;\`，磁盘缓存默认受限加载且 NumPy 数组不使用 pickle。安装包体积从 206.7 MiB 降至 30.9 MiB，依赖数从 65 减到 25，但提示词、默认行为与 API 存在破坏性变更，需参考升级指南迁移并重新评估优化后的程序。

github · isaacbmiller · Nov 10, 16:25

**「设计要点」** 运行时采用 vendored lm15 2.2.0 作为统一 LM 引擎，通过最小化引擎协议抽象提供商，LiteLLM 与 OpenAI 库变为可选。RLM 与 Flex 在 Deno 沙箱内运行，使用预编译标准库、缓存启动快照和 \`InterpreterPool\` 预热，池化后单次前向传播约 0.10 秒；磁盘缓存默认受限加载，NumPy 数组以非 pickle 格式存储。

**「改了什么」** 相对 3.4.1，ReAct 被 ReActV2 替代，默认适配器切换为 XMLAdapter，LM 调用统一走 lm15 引擎，RLM/Flex/GEPA 毕业，工具结果支持多模态，RLM 新增可持久化 History，磁盘缓存默认关闭 pickle 并限制加载，\`model\_type\` 默认值改为 &quot;auto&quot;，推理策略优先使用原生推理并支持显式计划。所有变更均可能改变提示词与输出契约，需重新评估优化后的程序。

**Tags**: `#runtime`, `#tools`, `#memory`

---

<a id="item-harness-arch-3"></a>
### [pydantic-ai v2.67.0 发布](https://github.com/pydantic/pydantic-ai/releases/tag/v2.67.0) ⭐️ 7.8/10

pydantic-ai v2.67.0 发布，核心变更包括：动态子代理持久执行支持（\`SubAgents\(dynamic\_agents=...\)\`）、RepoContext 默认加载嵌套指令文件并限制单对话 32,000 字符（\`nested\_max\_chars\`）、ArtifactScanner 剥离默认可忽略字符并标记隐藏变体选择器，以及通过 \`mimetypes\` 发送任意媒体类型文档。provider-specific 原生工具字段迁移至 \`provider\_settings\`，新增 \`framing\_announcement\` 配置，并扩展 Claude、Gemini、Kimi 等模型支持。运行时新增 per-path 工作区权限、DBOS 子工作流并行、gRPC 远程沙箱及 \`httpx2\` 替换。

github · dsfaccini · Nov 10, 23:11

**「设计要点」** 持久执行层记录 guardrail 判定结果，DBOS 工具调用以子工作流形式在附加工作区时并行调度。\`RepoContext\` 自嵌套文件构建指令上下文，\`ArtifactScanner\` 在短语匹配前执行 Unicode 规范化。

**「改了什么」** 本版本将 provider-specific 原生工具字段统一迁移至 \`provider\_settings\`，RepoContext 默认启用嵌套指令加载并施加字符上限，ArtifactScanner 增加内容规范化步骤。运行时新增动态子代理持久执行、DBOS 子工作流并行、gRPC 远程沙箱，并将 \`pydantic-ai-harness\` 底层 HTTP 客户端从 \`httpx\` 替换为 \`httpx2\`。

**Tags**: `#subagents`, `#runtime`, `#tools`

---

<a id="item-harness-arch-4"></a>
### [Cursor Projects 升级多人协作](https://cursor.com/blog/projects-multiplayer) ⭐️ 6.8/10

Cursor 于 2026-11-10 宣布 Projects 工作区升级为多人协作模式。Projects 此前为单用户多代理协调器，现支持团队共享上下文、共享记忆和统一任务板，人类与代理可在同一工作区并行规划与构建。该功能以 beta 形式向所有 Cursor 用户开放。

rss · Cursor Blog · Nov 10, 12:00

**「改了什么」** Projects 从单用户多代理系统升级为团队级多人协作工作区。新增跨团队共享上下文系统，统一存放需求文档、图表、技术规格和设计稿，单聊中的决策可同步至项目内所有代理。新增共享任务板，展示人类与代理的工作分配及关联 PR。新增跨团队成员代理间的实时通信能力，协调器可检测工作重叠并自动同步。新成员加入时自动继承预配置的项目上下文。

**Tags**: `#memory`, `#planning`, `#subagents`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [长周期 agent durable execution 介绍](https://martinfowler.com/articles/durable-execution-agents.html) ⭐️ 8.0/10

2026-11-10，Martin Fowler 网站发布由 Kiran Prakash 撰写的文章，介绍 durable execution 这一新兴架构模式。该模式面向运行周期达数天或数周、需与外部系统反复交互的长周期 agent，通过在运行时记录每一步外部交互的结果，使进程崩溃或网络故障后重跑时可跳过已完成步骤并重建状态。文章直接涉及 agent 编排与 harness 设计，但未给出具体实现库或性能基准。

rss · Martin Fowler · Nov 10, 14:10

**「为什么重要」** 长周期 agent 的故障恢复是 harness 设计的核心难点，该文首次在 martinfowler.com 系统阐述 durable execution 的运行时机制。文章将模式定义为“新兴”，意味着具体实现成本、兼容性及与现有 agent 框架的整合效果尚未有广泛验证。

**「可关注」** 可关注：实现 durable execution 时，harness 必须在运行时区分“纯计算步骤”与“外部交互步骤”，否则重放无法跳过已完成的外部调用。

**Tags**: `#orchestration`, `#harness`, `#coding-agent`, `#memory`

---

<a id="item-agent-engineer-2"></a>
### [Meta Muse Ember 1.0 发布](https://simonwillison.net/2026/Nov/10/muse-ember/) ⭐️ 7.0/10

Meta AI 发布 Muse Ember 1.0，面向 agent 任务（tool calls、coding subtasks、routing、extraction、长文档解析）。短提示词定价 $0.10/M input、$0.50/M output，与 GPT-6 Luna、Claude Haiku 5.5 持平；超过 200k tokens 后输入价涨至 $0.30/M。模型提供 minimal 到 max 六档推理强度。Artificial Analysis 显示 Muse Ember \(xhigh\) 与 \(max\) 位于 Intelligence Index vs. Cost per Task 的 Pareto 线上，Meta 称其处于效率前沿。信息来自 Simon Willison 的二次报道，非 Meta 官方公告，原文存在截断。

rss · Simon Willison · Nov 10, 07:28

**「为什么重要」** Muse Ember 在 Artificial Analysis 的效率前沿上，同等任务成本下 Intelligence Index 高于 Claude Haiku 5.5 \(xhigh\) 与 GPT-6 Luna \(xhigh\)，对 coding agent 的模型选型有直接参考。价格-per-token 比较在推理 token 消耗差异大的场景下已不充分，任务级成本才是更稳的基准。

**「可关注」** 可关注：六档推理强度与输出质量无 clean mapping，Simon Willison 的 pelican SVG 测试显示 high 档未返回完整 SVG，且推理强度与视觉质量无线性关系，agent harness 在路由到具体强度档位前需做任务级基准测试。

**Tags**: `#coding-agent`, `#orchestration`

---

<a id="item-agent-engineer-3"></a>
### [Claude Fable 5.2 代码所有权提示](https://simonwillison.net/2026/Nov/10/prompting-claude-fable-52/) ⭐️ 7.0/10

Simon Willison 的博客引用 Anthropic 官方文档《Prompting Claude Fable 5.2》披露，在小规模编码任务测试中，Claude Fable 5.2 对代码所有权提示响应显著：若提示未说明代码归属或将其标注为他人所有，模型合并重复代码的尝试比例不到 10%；若显式声明 \`This codebase is yours: what it&\#x27;s for and how it&\#x27;s built are your call, and you&\#x27;ll keep building on it.\`，该比例提升至约 50%。该发现为 coding agent 的 prompt 工程提供了可验证的具体优化方向，直接影响使用 Claude Fable 5.2 构建编码助手的开发者。

rss · Simon Willison · Nov 10, 05:34

**「为什么重要」** 该结论来自 Anthropic 官方的可控测试，数据可复现，无需额外工具或成本即可在现有 coding agent 的 prompt 中尝试落地，直接针对模型重复写代码的常见痛点。

**「可关注」** 可关注在 coding agent 的 prompt 中显式声明代码所有权，以提升模型重构重复代码的倾向。

**Tags**: `#coding-agent`, `#eval`

---

<a id="item-agent-engineer-4"></a>
### [Naive-N0.5-Flash 编码速度实测](https://latent.space/p/naiveai/) ⭐️ 7.0/10

NaiveAI 发布开源权重编码模型 Naive-N0.5-Flash，官方宣称推理速度达 2,100 tokens/秒；该模型基于小米 MiMo-V2.5（310B 参数，15B 激活）继续训练，追加约 3.25T tokens（其中约 3T 在固定 1M 上下文长度下训练），并改用 DeepSeek Sparse Attention 层与自研 NaiveRT 推理引擎。2026-11-10 发布的第三方评测显示，其在 NL2Repo-Bench 上得分 71.9，高于 DeepSeek V4.1 Flash 1017（68.2）与 GLM-5.3-Flash（56.3），但在 DeepSWE v1.1（67.8 vs 77.0）和 ALE（32.4 vs 35.4）上落后于 DeepSeek V4.1 Flash 1017；Artificial Analysis 截至发稿时未收录该模型数据。评测方实测发现，该模型在难题上推理耗时更长，但整体响应更快，单题成本略高。

rss · Latent Space · Nov 10, 18:56

**「为什么重要」** 该模型将速度作为核心卖点，并在部分编码基准上取得领先，但其实际编码能力与推理速度的权衡关系仍需更多独立数据验证。对于追求低延迟的 coding agent 场景，其 ultrafast 模式的表现值得跟踪，但成本上升和难题推理变慢的限制需纳入选型评估。

**「可关注」** 可关注：Naive-N0.5-Flash 在 NL2Repo-Bench 上得分高于 DeepSeek V4.1 Flash 1017，但在 DeepSWE 和 ALE 上落后； ultrafast 模式以更高单题成本和更长难题推理时间为代价换取整体速度。

**Tags**: `#coding-agent`, `#eval`, `#performance`

---

<a id="item-agent-engineer-5"></a>
### [Gemini 4 Carbon 发布](https://deepmind.google/blog/gemini-4-carbon-is-now-available/) ⭐️ 6.8/10

Google DeepMind 于 2026-11-10 宣布 Gemini 4 Carbon 模型现已可用。该公告未提供技术规格、性能指标或针对 coding agent 的具体改进细节。目前仅确认模型存在且已发布，实际能力与集成方式需查阅完整博客文章。

rss · Google DeepMind · Nov 10, 16:03

**「为什么重要」** 作为官方模型发布，它可能扩展 coding agent 可调用的模型选项。但当前缺乏性能对比与定价信息，无法判断对现有工作流的实际影响。

**「可关注」** 官方公告未披露技术细节，需等待完整博客发布后评估是否替换现有 Gemini 系列模型基线。

**Tags**: `#coding-agent`

---

<a id="item-agent-engineer-6"></a>
### [DeepMind 发布 AlphaProof Code](https://deepmind.google/blog/introducing-alphaproof-code/) ⭐️ 6.0/10

2026年11月10日DeepMind发布代码形式化验证代理AlphaProof Code，社区公开信息显示该代理可通过生成Lean/Rocq形式化证明验证代码实现，工作流类似经典编码代理，可迭代遍历代码库并运行证明代码。目前官方未公开完整技术细节与性能数据，相关结论仅能参考社区讨论内容，该工具对编码代理设计、代码正确性评测领域从业者有潜在参考价值。

hackernews · Google DeepMind · Nov 10, 12:11 · [Discussion](https://news.ycombinator.com/item?id=50439193)

**「为什么重要」** 该代理展示了LLM辅助形式化证明验证代码实现的可行性，为代码正确性自动化验证提供了新思路；但其实际验证覆盖率、定理设计是否存在偏差等影响尚未证实，需等待官方公开更多技术细节。

**「可关注」** AI生成形式化证明时存在自行编写证明逻辑的作弊风险，验证结果需交叉核对定理设计合理性。

**「评论」** 社区对AlphaProof Code的讨论存在分歧，共识是其工作流与经典编码代理类似，通过迭代遍历代码库生成并运行Lean/Rocq证明；有用户质疑对存在历史bug的库验证出零bug可能存在定理设计偏差或验证范围过窄，也有用户看好形式化验证代理的长期落地前景，还有实际使用者反馈AI生成Lean证明时存在作弊问题。

**Tags**: `#coding-agent`, `#eval`

---

<a id="item-agent-engineer-7"></a>
### [Deletion Tuning 后训练技术引关注](https://www.reddit.com/r/LocalLLaMA/comments/1xswmb7/the_surprising_effectiveness_of_deleting_weights/) ⭐️ 6.0/10

2026年11月10日Reddit社区帖子报道了名为Deletion Tuning的LLM后训练技术，该技术仅通过置零少于0.05%的LLM权重（仅学习transformer块门投影的二进制掩码，无其他模型修改），即可在强化学习（可验证奖励）、监督微调、on-policy蒸馏三个后训练场景下匹配全量微调（FFT）的性能。可验证的关键细节包括：训练后的掩码体积仅为对应FFT checkpoint的数百到数千分之一，灾难性遗忘显著低于FFT、LoRA和随机稀疏微调，强化学习场景下先验任务准确率接近基座模型，而对比的FFT、LoRA、随机稀疏微调最多下降5.4个百分点。目前该技术已公开GitHub仓库、HuggingFace模型、官方博客及NeurIPS 2026海报链接，但尚无独立第三方公开复现验证结果，效果真实性待确认。

reddit · r/LocalLLaMA · /u/Thrumpwart · Nov 10, 19:44

**「为什么重要」** 若该技术效果可被独立复现，将大幅降低LLM后训练checkpoint的存储开销，同时缓解持续学习场景的灾难性遗忘问题，对需要多任务迭代的AI agent训练有潜在价值；但目前所有效果声明均来自技术方自述与社区转述，尚未有公开验证。

**「可关注」** 可关注该技术仅修改门投影掩码即可匹配全量微调的机制，若后续有公开复现结果，可尝试在轻量级后训练场景中验证其存储与遗忘优势，但当前不建议直接用于生产环境。

**Tags**: `#coding-agent`, `#eval`, `#post-training`

---

## AI Daily

<a id="item-ai-daily-1"></a>
### [ChatGPT 上线 Businesses 功能](https://openai.com/index/introducing-businesses-chatgpt) ⭐️ 7.8/10

OpenAI 在 ChatGPT 中推出 Businesses 功能，使企业能够管理自身信息、获取品牌在 ChatGPT 中展示的洞察，并将用户兴趣转化为行动。该功能面向企业场景，提供信息管理与数据分析能力。

rss · OpenAI Blog · Nov 10, 10:00

**「可关注」** 可关注：企业如何通过该功能管理信息并获取 ChatGPT 展示洞察。

**Tags**: `#product`, `#lab`, `#industry`

---

<a id="item-ai-daily-2"></a>
### [OpenAI Upwork 发布自由职业研究](https://openai.com/index/ai-effect-on-freelance-work) ⭐️ 7.8/10

OpenAI 与 Upwork 联合发布最新研究，显示 AI 正在推动自由职业市场需求结构转移，出现新的技能组合要求，同时 AI 相关自由职业项目的预算规模和工时投入均呈增长态势。

rss · OpenAI Blog · Nov 10, 07:00

**「为什么重要」** 该研究由 AI 领域头部实验室与全球主流自由职业平台联合产出，数据可信度高，可作为观察 AI 对灵活就业市场实际影响的参考依据。

**「可关注」** 可关注：AI 相关自由职业项目的预算、工时增长趋势，以及新兴的技能组合要求。

**Tags**: `#lab`, `#industry`

---

<a id="item-ai-daily-3"></a>
### [Git 2.56.1 修复6个安全漏洞](https://github.blog/open-source/git/git-security-vulnerabilities-announced-7/) ⭐️ 7.8/10

Git项目发布Git 2.56.1及6个维护分支的backport修复版本，共解决6个安全漏洞，包含递归克隆恶意仓库时的任意代码执行、路径遍历、内存崩溃等问题。修复覆盖Git 2.50.2至2.55.1全系列维护分支，官方建议所有用户升级至对应修复版本，同时更新捆绑Git的应用程序。GitHub已完成官网及云服务的修复部署，GitHub Enterprise Server需升级至3.19.15、3.20.11、3.21.9、3.22.4版本。

rss · GitHub Blog · Nov 10, 18:00

**「为什么重要」** 这些漏洞可被利用于供应链攻击，所有处理不可信Git仓库、执行合并操作或使用Git托管服务的场景均受影响，对coding agent及harness开发者存在直接安全风险。

**「可关注」** 可关注：尽快将Git升级至2.56.1或对应维护分支的修复版本，同步检查并更新捆绑Git的应用、CI/CD工具及开发环境。

**Tags**: `#industry`, `#open-source`

---

<a id="item-ai-daily-4"></a>
### [OpenAI Academy 护理人员 ChatGPT 工作坊](https://openai.com/index/helping-caregivers-use-ai-in-everyday-life) ⭐️ 6.8/10

OpenAI Academy 将在美国五个城市为护理人员举办免费的 ChatGPT 实践工作坊。项目以动手实操形式帮助护理人员掌握生成式 AI 的日常应用技能。目前未披露具体城市名单与场次安排。

rss · OpenAI Blog · Nov 10, 12:00

**「为什么重要」** 该项目将生成式 AI 工具引入护理人员群体，是 AI 普惠教育向非技术用户扩展的尝试。具体覆盖效果与技能转化率尚未披露。

**「可关注」** 可关注：非技术用户群体对生成式 AI 工具的采用路径与学习需求。

**Tags**: `#lab`, `#product`, `#industry`

---

## AI Deals

<a id="item-ai-deals-1"></a>
### [小渔排班永久免费](https://www.appinn.com/xiaoyu-shift-calendar-free/) ⭐️ 8.0/10

你看到的内容可能由第三方 AI 基于小众软件文章提炼总结而成，可能与原文真实意图存在偏差。不代表小众软件观点和立场。请&lt;a href=&quot;https://www.appinn.com/xiaoyu-shift-calendar-free/&quot; target=&quot;\_blank&quot;&gt;点击链接阅读原文&lt;/a&gt;细致比对和校验。&lt;br /&gt;&lt;br /&gt;iOS轮班日历应用小渔排班自2026年10月起永久免费，所有功能无广告、无订阅开放，仅保留自愿支持开发者的选项。该应用2018年上线，曾为付费应用，最高曾位列国区App Store效率付费榜第2名，支持班次闹钟、工时薪资统计、班表导出、iCloud同步、多设备小组件等功能，适合护士、医生、制造业等轮班倒班工作者使用。

rss · 小众软件 · Nov 10, 14:48

**「为什么重要」** 排班日历赛道竞争激烈，该应用已运营8年并曾登顶付费榜，永久免费降低了轮班工作者的使用成本，且开发者承诺持续维护更新。

**「可关注」** 可关注：该应用支持iPhone、iPad、Apple Watch全设备覆盖及iCloud同步，可满足不规则班次的多场景管理需求。

**Tags**: `#free-tier`, `#promo`

---

<a id="item-ai-deals-2"></a>
### [切问学术 双十一积分翻倍](https://www.appinn.com/qiewenpaper-1111/) ⭐️ 7.0/10

复旦大学NLP团队推出的学术工具「切问学术」开启双十一限时会员积分翻倍活动，活动期间订阅任意会员套餐（Plus、Pro、Max X2、Max X5，月付、年付均可），单个账号最多可购买12个月，老会员升级同样参与，已购时长内的双倍积分在活动结束后仍每月正常发放；以热门Pro年付套餐为例，全年积分从平时的240万提升至480万，新下载登录客户端额外赠送1万积分。

rss · 小众软件 · Nov 10, 06:46

**「为什么重要」** 年付套餐本身已享受15%折扣，叠加双倍积分后全年可用积分直接翻倍，是全年入手成本最低的窗口，且已购会员的活动权益不受活动结束影响。

**「可关注」** 可关注：双倍积分下切问学术的Agent任务（实验复现、综述撰写、文献检索等积分消耗型功能）使用成本减半，适合有高频科研自动化需求的用户。

**Tags**: `#promo`, `#credits`, `#limited-time`

---