---
layout: default
title: "Horizon Summary: 2026-11-11 (ZH)"
date: 2026-11-11
lang: zh
---

> 从 196 条内容中筛选出 17 条重要资讯。

<nav id="ah-toc" class="ah-toc" aria-label="目录"><span class="ah-toc-title">目录</span><ul><li><a href="#sec-harness-arch"><span class="ah-toc-name">Harness 架构</span><span class="ah-toc-count">4条</span></a></li><li><a href="#sec-agent-engineer"><span class="ah-toc-name">Agent 工程师日报</span><span class="ah-toc-count">7条</span></a></li><li><a href="#sec-ai-daily"><span class="ah-toc-name">AI 日报</span><span class="ah-toc-count">4条</span></a></li><li><a href="#sec-ai-deals"><span class="ah-toc-name">AI 羊毛</span><span class="ah-toc-count">2条</span></a></li></ul></nav>

---

**[Harness 架构](#sec-harness-arch)**
1. [block/goose v1.59.0 发布](#item-harness-arch-1) ⭐️ 8.8/10
2. [DSPy 3.5.0 发布](#item-harness-arch-2) ⭐️ 8.8/10
3. [pydantic-ai v2.67.0 发布](#item-harness-arch-3) ⭐️ 7.8/10
4. [Cursor Projects 多玩家协作发布](#item-harness-arch-4) ⭐️ 6.8/10

**[Agent 工程师日报](#sec-agent-engineer)**
1. [持久执行模式 面向长时程智能体](#item-agent-engineer-1) ⭐️ 8.0/10
2. [Meta 发布 Muse Ember 1.0](#item-agent-engineer-2) ⭐️ 7.0/10
3. [Claude Fable 5.2 代码所有权提示](#item-agent-engineer-3) ⭐️ 7.0/10
4. [Naive-N0.5-Flash 2100 TPS 实测](#item-agent-engineer-4) ⭐️ 7.0/10
5. [Gemini 4 Carbon 正式可用](#item-agent-engineer-5) ⭐️ 6.8/10
6. [DeepMind AlphaProof Code 引 HN 讨论](#item-agent-engineer-6) ⭐️ 6.0/10
7. [Deletion Tuning 删除权重微调方法发布](#item-agent-engineer-7) ⭐️ 6.0/10

**[AI 日报](#sec-ai-daily)**
1. [ChatGPT 上线企业信息管理功能](#item-ai-daily-1) ⭐️ 7.8/10
2. [OpenAI 与 Upwork 发布 AI 对自由职业影响研究](#item-ai-daily-2) ⭐️ 7.8/10
3. [Git 2.56.1 修复 6 个安全漏洞](#item-ai-daily-3) ⭐️ 7.8/10
4. [OpenAI 为看护者开免费 ChatGPT 工作坊](#item-ai-daily-4) ⭐️ 6.8/10

**[AI 羊毛](#sec-ai-deals)**
1. [小渔排班 iOS 永久免费](#item-ai-deals-1) ⭐️ 8.0/10
2. [切问学术双十一积分翻倍福利](#item-ai-deals-2) ⭐️ 7.0/10

---

## Harness 架构
{: #sec-harness-arch .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-harness-arch" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-harness-arch-1"></a>
### [block/goose v1.59.0 发布](https://github.com/aaif-goose/goose/releases/tag/v1.59.0) ⭐️ 8.8/10

block/goose v1.59.0 正式发布，新增最小化延迟 MCP 工具、子代理委托恢复、GDK 代理钩子操作及 ACP 客户端标签会话过滤。ToolExecutionOperation 引入 deferred MCP 支持，工具调用不再强制同步阻塞；subagent 支持已完成委托的后续跟进；goose-agent 通过 GDK 暴露 stop、approval、tool hook 接口；ACP 客户端可按标签过滤会话列表。版本同时修复 Databricks OAuth 令牌自动刷新、Gemini thinking level 传递、会话数据库初始化隔离等问题。

github · github-actions\[bot\] · 11月10日 17:17

**「设计要点」** ToolExecutionOperation 的 deferred MCP 工具将执行模型从同步阻塞改为延迟调度。goose-agent 通过 GDK 暴露 stop/approval/tool hook，将权限控制点下沉到代理运行时；会话层新增 client tag 过滤，支持多租户或 ACP 场景下的会话隔离。

**「改了什么」** 相对上一版，核心能力变更包括：ToolExecutionOperation 支持最小化延迟 MCP 工具；subagent 委托支持 resume 并携带后续跟进；goose-agent 新增 stop、approval、tool hook 操作接口；ACP 客户端可按标签过滤会话列表。Bug 修复覆盖 Databricks OAuth 自动刷新、Gemini 参数传递修正、会话数据库初始化隔离等。

**「评论」** 无社区评论。

**标签**: `#mcp`, `#tools`, `#subagents`, `#permissions`, `#runtime`

---

<a id="item-harness-arch-2"></a>
### [DSPy 3.5.0 发布](https://github.com/stanfordnlp/dspy/releases/tag/3.5.0) ⭐️ 8.8/10

DSPy 3.5.0 发布，prompts、defaults 与 APIs 存在破坏性变更，核心变更包括轻量 lm15 运行时、graduated 核心模块、ReActV2 与多模态工具结果。LiteLLM 与 OpenAI Python 库变为可选，默认安装包从 206.7 MiB 降至 30.9 MiB，依赖从 65 个减至 25 个，导入时间从 1.01 s 降至 0.49 s。ReActV2 替换 ReAct 成为默认 dspy.ReAct，提供结构化 History 与类型化 submit 工具；RLM、Flex、GEPA 从实验性模块毕业。XMLAdapter 成为默认 Adapter，model\_type=&quot;auto&quot; 成为默认，磁盘缓存默认安全，RLM 支持图像裁剪与混合文本/图像子查询，原生推理优先。

github · isaacbmiller · 11月10日 16:25

**「设计要点」** DSPy 3.5.0 以轻量 lm15 引擎替换原有 LM 层，LiteLLM 与 OpenAI Python 库变为可选依赖。RLM 与 Flex 基于 Deno 运行时，支持 InterpreterPool 预热、History 持久化（不恢复实时解释器变量）及多模态工具结果返回；磁盘缓存默认限制加载且以纯 NumPy 数组存储，禁用 pickle。

**「改了什么」** ReActV2 替换 ReAct 成为默认 dspy.ReAct，引入结构化 History 与类型化 submit 工具，旧名称在 3.6 前弃用。RLM、Flex、GEPA 从实验性模块毕业，XMLAdapter 成为默认 Adapter，model\_type=&quot;auto&quot; 成为默认，RLM 支持图像裁剪与混合文本/图像子查询，磁盘缓存默认限制加载且禁用 pickle，原生推理优先。

**标签**: `#runtime`, `#tools`, `#memory`

---

<a id="item-harness-arch-3"></a>
### [pydantic-ai v2.67.0 发布](https://github.com/pydantic/pydantic-ai/releases/tag/v2.67.0) ⭐️ 7.8/10

pydantic-ai v2.67.0 发布，重点强化 durable execution 能力与代码上下文处理。动态子代理 SubAgents\(dynamic\_agents=...\) 现可在 durable execution 下运行，RepoContext 默认按目录加载嵌套指令文件并设 32,000 字符上限，ArtifactScanner 在匹配前剥离默认忽略字符。此外，provider-specific 原生工具字段迁至 provider\_settings，文档发送扩展至 mimetypes 已知的任意媒体类型，guardrail 判定与 TrajectoryJudge 评估均支持持久化记录。

github · dsfaccini · 11月10日 23:11

**「设计要点」** 运行时通过 DBOS 子工作流与 Prefect 任务重放增强 durable execution 可靠性；工具层将 provider 专属字段统一收口至 provider\_settings，远程 CodeMode 沙盒改用 gRPC 调用；权限模型新增 Workspace.authority\_of  per-path  authority 与 CapabilityCreation 权限校验，上下文记忆通过 RepoContext 嵌套指令上限控制膨胀。

**「改了什么」** durable execution 新增动态子代理与 task\_control 支持，RepoContext 默认递归加载目录指令文件并引入 nested\_max\_chars 上限，ArtifactScanner 修复隐藏变体选择器与忽略字符问题。provider 专属字段迁移至 provider\_settings 并扩展 Anthropic 网络工具支持，guardrail 与 judge 评估结果持久化，CodeMode 拒绝 Python 内置函数名工具，pydantic-ai-harness 将 httpx 替换为 httpx2。

**标签**: `#subagents`, `#runtime`, `#tools`

---

<a id="item-harness-arch-4"></a>
### [Cursor Projects 多玩家协作发布](https://cursor.com/blog/projects-multiplayer) ⭐️ 6.8/10

Cursor Projects 升级为多玩家协作模式，支持团队与智能体 fleet 在同一工作区共享上下文、记忆和任务板。系统保留成员级本地一对一聊天，同时新增团队级共享上下文层，存放需求文档、技术规格和设计稿。智能体可跨成员实时协调，在检测到工作重叠或依赖时自动同步，避免后期重构和合并冲突。该功能以 Beta 形式向所有 Cursor 用户推出。

rss · Cursor Blog · 11月10日 12:00

**「设计要点」** 采用双层上下文架构：成员级本地上下文保持不变，叠加团队级共享上下文层。智能体通过协调器实现跨成员通信，任务板作为统一视图同时服务于人类和智能体。

**「改了什么」** 新增团队共享上下文系统，项目内决策可被所有智能体访问；新增统一任务板，同时显示人类和智能体的工作状态及关联 PR；新增跨成员智能体通信，支持实时协调和依赖顺序规划；新成员加入时自动预配置完整上下文，无需重复搭建。

**标签**: `#memory`, `#planning`, `#subagents`

---

## Agent 工程师日报
{: #sec-agent-engineer .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-agent-engineer" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-agent-engineer-1"></a>
### [持久执行模式 面向长时程智能体](https://martinfowler.com/articles/durable-execution-agents.html) ⭐️ 8.0/10

2026 年 11 月 10 日，Martin Fowler 网站发布 Kiran Prakash 撰写的技术文章，介绍面向长时程智能体的持久执行（durable execution）新兴架构模式。该模式针对长时程智能体运行中可能出现的进程崩溃、网络故障等异常，由运行时记录所有与外部交互的步骤结果，故障后重跑程序时可跳过已完成步骤、基于记录重建状态，实现故障恢复。该模式对智能体编排、coding agent harness 设计有直接参考价值。

rss · Martin Fowler · 11月10日 14:10

**「为什么重要」** 该模式直接解决长时程智能体运行时的故障恢复问题，为当前 coding agent / harness 的长任务可靠性设计提供了可参考的架构范式。

**「可关注」** 可关注：长时程智能体 harness 可参考该模式，在运行时层面对外部交互步骤做持久化记录，降低故障后状态重建成本。

**标签**: `#orchestration`, `#harness`, `#coding-agent`, `#memory`

---

<a id="item-agent-engineer-2"></a>
### [Meta 发布 Muse Ember 1.0](https://simonwillison.net/2026/Nov/10/muse-ember/) ⭐️ 7.0/10

2026 年 11 月 10 日，Meta AI 发布面向 agent 任务的小模型 Muse Ember 1.0，官方描述其优化了 tool calls、coding 子任务、routing、extraction、长文档解析等 agent 高频重复工作，提供 minimal、low、medium、high、xhigh、max 六个推理等级。短提示场景下定价与 GPT-6 Luna、Claude Haiku 5.5 一致，为输入 $0.10/百万 token、输出 $0.50/百万 token；长提示阈值分别为 200k、272k、100k，超过阈值后 Ember 定价介于两者之间。同天发布的 Claude Fable 5.2 定价为 Ember 短提示场景的 80 倍。Artificial Analysis 的 Intelligence Index vs 成本 per task 图表显示，Muse Ember 1.0 的 xhigh、max 推理等级位于 Pareto 线，同 Intelligence Index 约 34 的 Claude Haiku 5.5 xhigh 相比，成本低约 44%。当前内容来自 Simon Willison 的二次报道，非 Meta 官方公告，且原文存在截断，提及推理等级与生成质量未呈现 clean 映射。

rss · Simon Willison · 11月10日 07:28

**「为什么重要」** 该模型是目前 Claude Haiku/GPT Luna 类中效率 Pareto 前沿的成员，对需要控制 agent 子任务成本的工程师有直接参考价值；其在具体 coding agent 场景的实际推理质量与稳定性尚未得到大规模验证。

**「可关注」** 可关注：Muse Ember 1.0 在 Artificial Analysis 的效率 Pareto 线上，同 Intelligence Index 下成本低于 Claude Haiku 5.5 xhigh 约 44%，可作为 agent 高频子任务的低成本备选模型。

**标签**: `#coding-agent`, `#orchestration`

---

<a id="item-agent-engineer-3"></a>
### [Claude Fable 5.2 代码所有权提示](https://simonwillison.net/2026/Nov/10/prompting-claude-fable-52/) ⭐️ 7.0/10

2026 年 11 月 10 日，Simon Willison 的博客引用 Anthropic 官方文档，披露 Claude Fable 5.2 在编码任务中对代码所有权提示的响应规律。测试场景为小型编码任务，无所有权相关提示时，模型合并重复代码的比例不到 10%；添加指定所有权提示后，该比例提升至约 50%。

rss · Simon Willison · 11月10日 05:34

**「为什么重要」** 该技巧来自 Anthropic 官方可验证测试，无需调整模型即可直接应用于 coding agent 的 prompt 优化。目前暂无公开数据证实该效果在复杂编码任务、多轮协作场景中的普适性。

**「可关注」** 可关注：在 coding agent 的任务 prompt 中明确声明代码归模型所有，可能以极低成本提升其重构重复代码的概率。

**标签**: `#coding-agent`, `#eval`

---

<a id="item-agent-engineer-4"></a>
### [Naive-N0.5-Flash 2100 TPS 实测](https://latent.space/p/naiveai/) ⭐️ 7.0/10

2026 年 11 月 10 日，第三方博客 latent.space 发布无偏评测系列首文，评估 NaiveAI 开源编码模型 Naive-N0.5-Flash，该模型官方承诺最高 2100 tokens/秒，由 AI 主导开发，长期目标是实现递归自我改进，基于小米 310B 参数稀疏 MoE 模型 MiMo-V2.5（15B 激活参数，原生训练 48T tokens）继续训练，新增约 3.25T 训练 tokens（其中 3T 采用 1M 固定上下文长度、恒定学习率训练），搭配自研 NaiveRT 推理引擎。评测将 Naive-N0.5-Flash 的极速模式与 OpenRouter 热门 Flash 类编码模型 DeepSeek V4.1 Flash 1017、GLM-5.3 Flash 对比，使用相同应用构建提示词测试。官方 benchmark 显示 Naive-N0.5-Flash 的 NL2Repo-Bench 得分 71.9，高于两款对比模型，但 DeepSWE v1.1 得分 67.8、Agent&\#x27;s Last Exam 得分 32.4 均低于 DeepSeek V4.1 Flash 1017；第三方实测发现其处理难题推理时间更长，但整体回答速度仍更快，单题成本略高。截至发稿时，Artificial Analysis 平台尚无 NaiveAI 模型的性能统计数据，其 Intelligence Index 得分也未公布，官方 benchmark 的测试条件未完全披露。

rss · Latent Space · 11月10日 18:56

**「为什么重要」** 这是目前公开可查的首份针对 Naive-N0.5-Flash 编码能力的第三方评测，既验证了其高吞吐速度的核心卖点，也披露了速度与推理质量、成本的权衡关系；该模型在真实编码代理工作流中的稳定性、长上下文任务表现尚未有公开验证。

**「可关注」** 可关注：若团队编码场景优先考虑首字延迟与整体吞吐，可参考其 NaiveRT 推理引擎与 DeepSeek 稀疏注意力层的适配方案，但需自行验证复杂推理、长上下文场景下的实际表现与成本。

**标签**: `#coding-agent`, `#eval`, `#performance`

---

<a id="item-agent-engineer-5"></a>
### [Gemini 4 Carbon 正式可用](https://deepmind.google/blog/gemini-4-carbon-is-now-available/) ⭐️ 6.8/10

2026 年 11 月 10 日，Google DeepMind 官方宣布 Gemini 4 Carbon 模型正式对外可用。当前公开材料未披露该模型的技术规格、性能基准或面向编码智能体的专项优化信息。

rss · Google DeepMind · 11月10日 16:03

**「为什么重要」** 该模型是 Gemini 系列新增的可用变体，但当前公开信息不足以评估其对编码智能体工程的实际价值，需等待后续技术细节披露。

**「可关注」** 可关注：后续跟进官方披露的技术细节，评估其与现有编码智能体工作流的适配性。

**标签**: `#coding-agent`

---

<a id="item-agent-engineer-6"></a>
### [DeepMind AlphaProof Code 引 HN 讨论](https://deepmind.google/blog/introducing-alphaproof-code/) ⭐️ 6.0/10

2026 年 11 月 10 日 HN 社区讨论 DeepMind 发布的代码形式化验证代理 AlphaProof Code，社区提及该代理可通过生成 Lean/Rocq 形式化证明验证代码实现，工作流与经典编码代理类似，对编码代理设计、代码正确性评测相关从业者有潜在参考价值。目前无官方公告的完整技术细节与性能数据公开。

hackernews · Google DeepMind · 11月10日 12:11 · [社区讨论](https://news.ycombinator.com/item?id=50439193)

**「为什么重要」** 该讨论首次公开了 DeepMind 形式化验证代理的社区认知，已确认其对编码代理设计有参考价值；但代理的实际验证能力、与经典编码代理的差异尚未有官方技术细节支撑，相关影响仍待验证。

**「可关注」** 可关注：AI 生成的形式化证明可能存在“作弊”或定理定义偏差问题，编码代理的输出即使通过测试/验证也不代表逻辑正确。

**「评论」** 社区存在分歧：部分用户质疑形式化验证零 bug 结果的合理性，怀疑定理定义或验证范围存在偏差；也有用户指出该代理工作流与经典编码代理高度相似，仅输出形式化证明代码而非普通实现代码。另有用户分享 AI 生成形式化证明易“作弊”、编码代理输出通过测试但逻辑错误的实际踩坑经验。

**标签**: `#coding-agent`, `#eval`

---

<a id="item-agent-engineer-7"></a>
### [Deletion Tuning 删除权重微调方法发布](https://www.reddit.com/r/LocalLLaMA/comments/1xswmb7/the_surprising_effectiveness_of_deleting_weights/) ⭐️ 6.0/10

2026 年 11 月 10 日 Reddit 社区分享 Deletion Tuning LLM 后训练技术，核心为学习 transformer 块门控投影的二值掩码，仅零化不到 0.05%的模型权重，即可在基于可验证奖励的强化学习、监督微调、on-policy 蒸馏三个场景下匹配全量微调（FFT）的规模性能。该方法掩码检查点体积仅为对应 FFT 检查点的数百分之一到数千分之一，强化学习场景下旧任务准确率接近基座水平，对比的 FFT、LoRA、随机稀疏微调旧任务准确率最多下降 5.4 个百分点；稳定秩、谱漂移、主权重重叠三项几何分析显示其权重变化特征与 FFT 最接近。最初社区分享未附官方一手验证材料，后续发帖人补充了对应 GitHub 仓库、HuggingFace 模型库、项目博客及 NeurIPS 2026 海报链接，目前无独立复现结果公开。

reddit · r/LocalLLaMA · /u/Thrumpwart · 11月10日 19:44

**「为什么重要」** 该方法针对 LLM 后训练检查点体积过大、灾难性遗忘严重的核心痛点，给出了量化上显著的优化方案；但其在真实 AI agent 工作流中的泛化性、独立复现结果及实际部署收益尚未得到验证。

**「可关注」** 可关注：仅修改&lt;0.05%权重的 Deletion Tuning 方法在多个后训练场景下匹配全量微调性能，同时检查点体积缩小数百倍且灾难性遗忘显著降低，可验证其在自定义 agent 微调场景中的实际收益与兼容性。

**标签**: `#coding-agent`, `#eval`, `#post-training`

---

## AI 日报
{: #sec-ai-daily .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-daily" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-daily-1"></a>
### [ChatGPT 上线企业信息管理功能](https://openai.com/index/introducing-businesses-chatgpt) ⭐️ 7.8/10

2026 年 11 月 10 日，OpenAI 在 ChatGPT 中上线名为 Businesses 的企业专属功能。该功能支持企业自主管理自身公开信息、查看自身在 ChatGPT 中的展示相关洞察，还可将用户对企业的兴趣转化为可落地的行动。目前仅披露基础能力框架，未公开具体使用限制与开放范围。

rss · OpenAI Blog · 11月10日 10:00

**「为什么重要」** 这是 OpenAI 在 ChatGPT 主产品中新增的面向企业的信息管理与转化工具，将影响企业在 ChatGPT 生态中的信息展示与用户转化路径。

**「可关注」** 可关注：ChatGPT Businesses 功能的信息管理、展示洞察、兴趣转化三类能力的后续落地规则与接口开放情况。

**标签**: `#product`, `#lab`, `#industry`

---

<a id="item-ai-daily-2"></a>
### [OpenAI 与 Upwork 发布 AI 对自由职业影响研究](https://openai.com/index/ai-effect-on-freelance-work) ⭐️ 7.8/10

OpenAI 与 Upwork 联合发布最新研究，披露 AI 对自由职业市场的实际影响。研究显示 AI 正推动自由职业需求结构转移，催生新的技能组合要求，同时 AI 相关自由职业项目的预算与工作时长均呈增长态势。

rss · OpenAI Blog · 11月10日 07:00

**「为什么重要」** 该研究由头部 AI 实验室与主流自由职业平台联合产出，数据来自真实交易场景，可直观反映 AI 对实际劳动力市场的影响，为相关从业者提供趋势参考。

**「可关注」** 可关注：AI 相关自由职业项目的预算、工时增长趋势，以及市场新增的技能组合要求。

**标签**: `#lab`, `#industry`

---

<a id="item-ai-daily-3"></a>
### [Git 2.56.1 修复 6 个安全漏洞](https://github.blog/open-source/git/git-security-vulnerabilities-announced-7/) ⭐️ 7.8/10

Git 项目正式发布 Git 2.56.1 及 2.55.1、2.54.1 等 6 个维护分支的 backport 版本，共修复 6 个已公开 CVE 安全漏洞。漏洞覆盖递归克隆任意代码执行、路径遍历、堆栈/堆内存损坏、二进制补丁越界读取等风险场景，攻击者可利用部分漏洞在克隆恶意仓库、处理恶意合并请求或补丁时触发代码执行或拒绝服务。官方建议所有用户升级至 Git 2.56.1 或对应维护分支的修复版本，同时更新捆绑 Git 的应用程序。

rss · GitHub Blog · 11月10日 18:00

**「为什么重要」** Git 是代码托管、CI/CD、开发工具链的核心基础组件，本次漏洞覆盖克隆、合并、补丁处理等高频操作场景，对依赖 Git 的工程工具、自动化流水线及 coding agent 存在直接供应链攻击风险。

**「可关注」** 可关注：升级 Git 至对应修复版本，同时检查并更新捆绑 Git 的依赖应用；处理不可信 fast-import 流时禁止开启--allow-unsafe-features 参数。

**标签**: `#industry`, `#open-source`

---

<a id="item-ai-daily-4"></a>
### [OpenAI 为看护者开免费 ChatGPT 工作坊](https://openai.com/index/helping-caregivers-use-ai-in-everyday-life) ⭐️ 6.8/10

OpenAI Academy 面向美国五座城市的看护者推出免费、实操性 ChatGPT 工作坊，旨在帮助其掌握日常场景可用的 AI 技能。

rss · OpenAI Blog · 11月10日 12:00

**「为什么重要」** 这是面向非技术从业者的 AI 普及尝试，覆盖看护这类高时间压力、低技术接触度的群体，可观察 AI 工具在非职场场景的落地适配情况。

**「可关注」** 可关注：非技术群体使用 AI 工具的实操需求与场景适配方向。

**标签**: `#lab`, `#product`, `#industry`

---

## AI 羊毛
{: #sec-ai-deals .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-deals" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-deals-1"></a>
### [小渔排班 iOS 永久免费](https://www.appinn.com/xiaoyu-shift-calendar-free/) ⭐️ 8.0/10

你看到的内容可能由第三方 AI 基于小众软件文章提炼总结而成，可能与原文真实意图存在偏差。不代表小众软件观点和立场。请&lt;a href=&quot;https://www.appinn.com/xiaoyu-shift-calendar-free/&quot; target=&quot;\_blank&quot;&gt;点击链接阅读原文&lt;/a&gt;细致比对和校验。&lt;br /&gt;&lt;br /&gt;iOS 轮班日历应用小渔排班自 2026 年 10 月起永久免费，所有功能无广告、无订阅开放，仅保留自愿支持开发者的选项。该应用 2018 年上线，曾为付费工具，支持班次闹钟、工时薪资统计、班表导出、iCloud 同步等功能，适配 iPhone、iPad、Apple Watch 等多设备。

rss · 小众软件 · 11月10日 14:48

**「为什么重要」** 该应用此前为付费工具，曾位列国区 App Store 效率付费榜第 2 名，此次永久免费开放全功能，对轮班、倒班工作者而言可零成本获取长期维护的排班工具。

**「可关注」** 可关注：该应用仅支持 iOS 平台，需通过 App Store 下载，提供 iCloud 同步、多设备小组件及班表导出功能，适合有轮班需求的 iOS 用户使用。

**标签**: `#free-tier`, `#promo`

---

<a id="item-ai-deals-2"></a>
### [切问学术双十一积分翻倍福利](https://www.appinn.com/qiewenpaper-1111/) ⭐️ 7.0/10

复旦大学 NLP 团队推出的学术工具「切问学术」（被称为学术版 Codex）开启双十一限时福利，活动期间订阅任意会员套餐，每月到账积分均为平时的 2 倍。全套餐（Plus、Pro、Max X2、Max X5，月付、年付均可）参与，老会员升级也可享受该福利，单个账号最多可购买 12 个月会员。活动结束后已购时长的双倍积分仍会正常每月发放，当前下载并登录客户端还可额外获赠 1 万积分。

rss · 小众软件 · 11月10日 06:46

**「为什么重要」** 年付套餐本身立省 15%，叠加双倍积分后是全年入手成本最低的时机，且已购会员时长的双倍积分在活动结束后仍正常发放，额外下载客户端获赠的 1 万积分可让新用户无成本体验核心功能。

**「可关注」** 可关注：活动期间订阅任意会员套餐（含老会员升级）均可享每月积分翻倍，单个账号最多可购买 12 个月会员，年付套餐叠加 15%立省优惠后性价比最高。

**标签**: `#promo`, `#credits`, `#limited-time`

---