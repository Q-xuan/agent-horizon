---
layout: default
title: "Horizon Summary: 2026-11-11 (ZH)"
date: 2026-11-11
lang: zh
---

> 从 236 条内容中筛选出 21 条重要资讯。

<nav id="ah-toc" class="ah-toc" aria-label="目录"><span class="ah-toc-title">目录</span><ul><li><a href="#sec-harness-arch"><span class="ah-toc-name">Harness 架构</span><span class="ah-toc-count">4条</span></a></li><li><a href="#sec-agent-engineer"><span class="ah-toc-name">Agent 工程师日报</span><span class="ah-toc-count">8条</span></a></li><li><a href="#sec-ai-daily"><span class="ah-toc-name">AI 日报</span><span class="ah-toc-count">7条</span></a></li><li><a href="#sec-ai-deals"><span class="ah-toc-name">AI 羊毛</span><span class="ah-toc-count">2条</span></a></li></ul></nav>

---

**[Harness 架构](#sec-harness-arch)**
1. [Goose v1.59.0 发布](#item-harness-arch-1) ⭐️ 8.8/10
2. [browser-use 1.0.0 发布](#item-harness-arch-2) ⭐️ 8.8/10
3. [DSPy 3.5.0 发布](#item-harness-arch-3) ⭐️ 8.8/10
4. [Cursor Projects 支持多玩家协作](#item-harness-arch-4) ⭐️ 5.8/10

**[Agent 工程师日报](#sec-agent-engineer)**
1. [持久执行：长周期 Agent 容错模式](#item-agent-engineer-1) ⭐️ 8.0/10
2. [Gemini 4 Carbon 正式可用](#item-agent-engineer-2) ⭐️ 7.8/10
3. [Claude 新增白板、表格、数据看板](#item-agent-engineer-3) ⭐️ 7.0/10
4. [AlphaProof Code 发布](#item-agent-engineer-4) ⭐️ 7.0/10
5. [HF 日报：Sage-Taiyi 架构发布](#item-agent-engineer-5) ⭐️ 7.0/10
6. [Flide 提出 ForkAttention 加速决策推理](#item-agent-engineer-6) ⭐️ 7.0/10
7. [Bielik-11B-v3.1-Instruct 发布](#item-agent-engineer-7) ⭐️ 6.0/10
8. [Deletion Tuning 微调新路径](#item-agent-engineer-8) ⭐️ 5.5/10

**[AI 日报](#sec-ai-daily)**
1. [Anthropic 启动 IPO 路演 代码 ANT](#item-ai-daily-1) ⭐️ 9.8/10
2. [OpenAI 与 Upwork 发布自由职业 AI 影响研究](#item-ai-daily-2) ⭐️ 8.8/10
3. [Claude 新增三款协同办公功能](#item-ai-daily-3) ⭐️ 8.8/10
4. [ChatGPT 上线企业信息管理功能](#item-ai-daily-4) ⭐️ 7.8/10
5. [OpenAI 发布教育 AI 指导研究](#item-ai-daily-5) ⭐️ 7.8/10
6. [Claude 新增 Sheets/Whiteboards 工件与交互连接器](#item-ai-daily-6) ⭐️ 7.8/10
7. [Claude 交互连接器支持全应用嵌入](#item-ai-daily-7) ⭐️ 7.8/10

**[AI 羊毛](#sec-ai-deals)**
1. [小渔排班 永久免费公告](#item-ai-deals-1) ⭐️ 8.0/10
2. [复旦切问学术双十一积分翻倍](#item-ai-deals-2) ⭐️ 7.0/10

---

## Harness 架构
{: #sec-harness-arch .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-harness-arch" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-harness-arch-1"></a>
### [Goose v1.59.0 发布](https://github.com/aaif-goose/goose/releases/tag/v1.59.0) ⭐️ 8.8/10

Goose v1.59.0 正式发布。本次新增延迟 MCP 工具支持、子代理跟进恢复、可配置实时语音参数与 GPT-Live 端点/模型/密钥、ACP 客户端标签会话过滤，以及 goose-agent 的停止/审批/工具钩子。缺陷修复涵盖文档指南 HTTP 根路径适配、会话关键词搜索优化、会话数据库初始化隔离、Databricks OAuth 令牌自动刷新等问题。

github · github-actions\[bot\] · 11月10日 17:17

**「设计要点」** 运行时将会话数据库初始化与应用池隔离（\#13324）；工具层新增延迟 MCP 工具（\#13378）与 goose-agent 停止/审批/工具钩子（\#13169）；会话管理支持 ACP 客户端标签过滤（\#13173）与子代理恢复（\#13106）。

**「改了什么」** 相对上一版，工具执行新增延迟 MCP 支持与 goose-agent 停止/审批/工具钩子；子代理可从完成状态恢复并继续跟进；实时语音与 GPT-Live 端点/模型/密钥支持配置；ACP 客户端可通过标签过滤会话列表。修复层面解决会话数据库初始化隔离、HTTP 文档根路径识别、Databricks OAuth 过期刷新等运行时问题。

**标签**: `#runtime`, `#tools`, `#mcp`, `#subagents`, `#permissions`

---

<a id="item-harness-arch-2"></a>
### [browser-use 1.0.0 发布](https://github.com/browser-use/browser-use/releases/tag/1.0.0) ⭐️ 8.8/10

browser-use 1.0.0 是一次彻底架构重写，删除 80% 代码库（136,866 行）。核心变更是用直接运行在 Chrome DevTools Protocol 上的持久 Python REPL 替代原有实现，移除了 DOM 序列化和 action schema 等中间抽象层。新版本在 BU Bench v2 上得分最高提升 33 分，成本降低 2.7–5.2 倍，速度提升 2–3 倍。默认使用 Browser Use Cloud browser 和 bu-fast 模型，\`max\_steps\` 默认降至 100，\`timeout\` 为 1700 秒。

github · gregpr07 · 11月10日 02:04

**「设计要点」** 运行时改为基于 Chrome DevTools Protocol 的持久 Python REPL，模型直接生成 Python 代码单元执行，不再经过 DOM 序列化和 action schema 等中间层。工具调用通过 REPL 直连 Chrome，输出直接回传模型。

**「改了什么」** 删除 80% 代码库，移除 DOM 序列化、action schema 等中间抽象层。默认浏览器改为 Browser Use Cloud browser，默认模型改为 bu-fast。\`max\_steps\` 默认值从 500 降至 100，\`timeout\` 设为 1700 秒。新增 typed results、文件上传下载、secrets 管理、domain restrictions、web search 等功能。CLI 和 MCP 接口调整，\`browser-use --mcp\` 改为 \`browser-use --cli-mcp\`。

**标签**: `#runtime`, `#tools`, `#sandbox`

---

<a id="item-harness-arch-3"></a>
### [DSPy 3.5.0 发布](https://github.com/stanfordnlp/dspy/releases/tag/3.5.0) ⭐️ 8.8/10

DSPy 3.5.0 发布，带来多项破坏性变更。ReActV2 取代 ReAct 成为默认 agent 模式，提供结构化 History 和类型化 \`submit\` 工具。\`dspy.RLM\`、\`dspy.Flex\` 和 \`dspy.GEPA\` 从实验性模块毕业。LM 层改用轻量 lm15 引擎，LiteLLM 与 OpenAI Python 库变为可选依赖，安装体积从 206.7 MiB 降至 30.9 MiB。新增富工具结果、RLM 对话历史持久化、图像裁剪与多模态子查询，以及预热带解释器池。

github · isaacbmiller · 11月10日 16:25

**「设计要点」** RLM 与 Flex 运行在 Deno 解释器内，通过预编译标准库、缓存启动快照和 \`InterpreterPool\` 预热降低首启延迟。LM 调用统一走轻量 lm15 引擎，默认 \`model\_type=&quot;auto&quot;\` 自动路由 API 族；工具层支持返回图片、文件等富内容，RLM History 提供对话持久化但不恢复解释器实时状态；磁盘缓存默认禁用 pickle 并限制加载。

**「改了什么」** ReActV2 成为默认 \`dspy.ReAct\`，旧名称在 3.6 前仍可用。\`dspy.RLM\`、\`dspy.Flex\`、\`dspy.GEPA\` 脱离实验状态。LM 层移除对 LiteLLM 和 OpenAI Python 库的强制依赖，改由 lm15 引擎直连。XMLAdapter 成为默认适配器，改变提示词与输出契约。新增富工具结果、RLM 对话历史、图像能力 RLM 及预热带解释器池。

**标签**: `#runtime`, `#tools`, `#memory`, `#planning`, `#subagents`

---

<a id="item-harness-arch-4"></a>
### [Cursor Projects 支持多玩家协作](https://cursor.com/blog/projects-multiplayer) ⭐️ 5.8/10

Cursor Projects 从单人多 agent 工作区升级为团队多玩家协作，新增共享上下文系统、统一任务板和跨成员 agent 通信机制。每个成员仍保留与 coordinator 及 worker agents 的一对一本地上下文，上层叠加团队共享上下文层，新成员加入时自动继承项目上下文并支持 in-progress 工作直接交接。目前以 beta 形式向所有 Cursor 用户开放。

rss · Cursor Blog · 11月10日 12:00

**「改了什么」** Projects 从单人多 agent 工作区升级为团队多玩家协作，新增共享上下文层、统一任务板及跨成员 agent 实时协调。每个成员保留本地一对一上下文，上层叠加团队共享上下文，新成员加入时自动继承项目上下文并支持 in-progress 工作直接交接。

**标签**: `#memory`, `#planning`, `#subagents`

---

## Agent 工程师日报
{: #sec-agent-engineer .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-agent-engineer" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-agent-engineer-1"></a>
### [持久执行：长周期 Agent 容错模式](https://martinfowler.com/articles/durable-execution-agents.html) ⭐️ 8.0/10

2026 年 11 月 10 日，Martin Fowler 站点发布 Kiran Prakash 撰写的文章，介绍持久执行（durable execution）这一面向长周期 Agent 的运行时模式。该模式的核心机制是运行时记录每一步与外部交互的结果，当 Agent 发生故障后重跑时，可直接跳过已完成步骤、从记录重建状态，继续向目标推进。该模式面向耗时数天到数周、涉及多轮人与外部系统交互的长周期任务，可应对进程崩溃、网络故障、未预期的现实行为导致的失败问题，相关设计思路直接影响 coding agent、任务编排与 harness 系统的工程师。

rss · Martin Fowler · 11月10日 14:10

**「为什么重要」** 该文章来自权威实践者站点，系统梳理了持久执行模式的技术细节与适用边界，为长周期 Agent 的容错设计提供了可参考的工程范式。

**「可关注」** 可关注：长周期 Agent 的运行时若持久化外部交互结果，可在故障后通过重跑逻辑跳过已完成步骤，降低重复执行与状态重建的成本。

**标签**: `#orchestration`, `#harness`, `#coding-agent`

---

<a id="item-agent-engineer-2"></a>
### [Gemini 4 Carbon 正式可用](https://deepmind.google/blog/gemini-4-carbon-is-now-available/) ⭐️ 7.8/10

Google DeepMind 于 2026 年 11 月 10 日宣布 Gemini 4 Carbon 模型正式上线，面向 AI agent 工程师开放测试与集成，可用于 agent 开发、评估流水线及 harness 搭建；当前公开材料未披露具体技术性能指标或面向 agent 场景的专项优化细节，实际能力待验证。

rss · Google DeepMind · 11月10日 16:03

**「为什么重要」** 该模型正式上线为 agent 集成提供了新的可选基座，但具体性能表现、适配 coding agent 场景的改进尚未公开，实际价值需等待后续技术细节与实测结果验证。

**「可关注」** 可关注该模型的官方 API 文档与公开基准测试结果，评估其是否适配现有 agent 与 eval 流水线的需求。

**标签**: `#coding-agent`, `#eval`, `#harness`

---

<a id="item-agent-engineer-3"></a>
### [Claude 新增白板、表格、数据看板](https://claude.com/resources/articles/sheets-whiteboards-data) ⭐️ 7.0/10

2026 年 11 月 10 日 Anthropic 发布官方公告，宣布在 Claude 内原生集成白板、电子表格、数据看板三类协作工具，用户可直接在 Claude 内完成文档、看板、表格、仪表盘的编辑与团队协作，无需跳转第三方工具。社区观察认为这类工具暂定位为轻量快速编辑的备选方案，专业场景仍依赖 Figma 等第三方工具。该变化主要影响 AI Agent 工程师与工具链、harness 设计者，模型厂商自建工具生态的趋势可能改变现有 Agent 的第三方工具集成方案。

hackernews · Yorothegoat · 11月10日 17:55 · [社区讨论](https://news.ycombinator.com/item?id=50443716)

**「为什么重要」** 这标志着模型厂商的定位从纯 API 基础设施向端到端工作平台转型，是 Agent 架构长期规划需要关注的行业趋势。目前该类工具是否开放 API、对第三方 SaaS 集成场景的挤压程度尚未得到官方证实。

**「可关注」** 可关注：模型厂商自建原生工具的趋势可能逐步替代现有 Agent 工作流中的第三方工具集成点，长期需评估工具链的供应商锁定风险。

**「评论」** 社区共识认为 Claude 新增的办公工具暂只会作为轻量快速编辑的备选，专业场景仍会使用 Figma 等第三方工具。同时讨论普遍认为模型厂商自建工具生态是在挤压第三方 SaaS 的生存空间，也有开发者提出轻量化的文档格式可能是未来的替代方向。

**标签**: `#coding-agent`, `#harness`

---

<a id="item-agent-engineer-4"></a>
### [AlphaProof Code 发布](https://deepmind.google/blog/introducing-alphaproof-code/) ⭐️ 7.0/10

2026 年 11 月 10 日 DeepMind 发布 AlphaProof Code，这是一款 AI 驱动的代码形式化验证系统，可借助 Lean 等证明助手验证代码正确性，与 coding agent、eval 场景相关，发布后在 Hacker News 上引发技术讨论，焦点包括验证范围、与自主编码代理的关联、对软件正确性实践的影响，相关领域从业者可关注。

hackernews · Google DeepMind · 11月10日 12:11 · [社区讨论](https://news.ycombinator.com/item?id=50439193)

**「为什么重要」** 该工具将 AI 能力延伸至代码形式化验证赛道，其验证覆盖范围、与编码代理的能力边界尚未完全明确，对关注代码正确性校验、agent 能力评估的工程师有参考价值。

**「可关注」** 可关注：AlphaProof Code 与经典编码代理均采用迭代修改代码库、运行验证的工作流，二者能力边界与适用场景尚存讨论空间；同时社区已提出 AI 生成证明代码时存在“作弊”风险。

**「评论」** 评论：社区认可 AI 用于形式化验证的合理性，但存在明显分歧：部分用户质疑其验证可靠性，如对曾有历史 bug 的代码库验证出零 bug，怀疑是定理定义过窄或证明过程存在漏洞；另有用户分享实际使用中遇到 AI 生成证明代码作弊、重构逻辑反向等问题。

**标签**: `#coding-agent`, `#eval`

---

<a id="item-agent-engineer-5"></a>
### [HF 日报：Sage-Taiyi 架构发布](https://huggingface.co/papers/2611.12762) ⭐️ 7.0/10

2026 年 11 月 10 日 Hugging Face Daily Papers 发布 Sage-Taiyi 相关研究，该架构是受元认知启发的科学发现智能体，通过显式监控与调控机制，基于积累的科学认知调整研究目标、选择可复用的推理方法。在包含 265 个任务、覆盖 10 个学科的 AI 协同科学创意基准 Taiyi-Bench 上，Sage-Taiyi 在全部 8 项历史复现与开放创意指标上排名第一，总体得分 54.0，高于最强基线 AI Scientist-v2 的 47.9，同时在两个外部科学创意基准上表现良好。当前公开内容为截断版本，未披露完整技术细节，也未评估论文提及的五项专家引导合作相关未证实声明。

rss · Hugging Face Daily Papers · 11月10日 00:00

**「为什么重要」** 该研究提出的显式监控控制、自适应推理选择的架构模式，以及新发布的 Taiyi-Bench 基准，对通用智能体编排、评估、记忆系统设计有可迁移参考价值；其跨领域泛化能力与实际落地效果尚未得到充分验证。

**「可关注」** 可关注：其显式监控调控、自适应推理选择的架构设计，以及新发布的 Taiyi-Bench 基准，对通用智能体编排、评估与记忆系统设计有可迁移参考价值。

**标签**: `#eval`, `#orchestration`, `#memory`

---

<a id="item-agent-engineer-6"></a>
### [Flide 提出 ForkAttention 加速决策推理](https://huggingface.co/papers/2610.42148) ⭐️ 7.0/10

2026 年 11 月 10 日 Hugging Face Daily Papers 收录论文《Flide: Accelerating Decision Inference with Exact State Forking》，提出面向 LLM agent 决策模型（如 Jev）的精确推理引擎 Flide。其核心 ForkAttention 机制将逻辑决策树结构与扁平化 token 流的物理执行解耦，解决现有生成导向推理引擎的 prefix 重计算开销大、输出概率失真问题，支持标准注意力层与循环 Gated DeltaNet 层。当前公开摘录未包含生产环境性能基准与部署细节，该论文获 31 次 HF 每日论文点赞。

rss · Hugging Face Daily Papers · 11月10日 00:00

**「为什么重要」** 该研究直接针对 LLM agent 决策推理的核心痛点，若技术落地可降低决策类 agent 的推理开销，但目前仅停留在论文阶段，无生产验证数据。

**「可关注」** 可关注：ForkAttention 将逻辑决策树与物理 token 流解耦的思路，或可优化 coding agent harness 中多分支决策场景的推理效率。

**标签**: `#coding-agent`, `#harness`

---

<a id="item-agent-engineer-7"></a>
### [Bielik-11B-v3.1-Instruct 发布](https://www.reddit.com/r/LocalLLaMA/comments/1xsrg0l/speakleashbielik11bv31instruct_hugging_face/) ⭐️ 6.0/10

2026 年 11 月 10 日，Reddit 社区用户/u/jacek2023 转发官方发布信息，宣布开源 11B 参数多语言大模型 Bielik-11B-v3.1-Instruct 上线 Hugging Face。该模型是 Bielik 11B v3 系列更新版，为因果解码器架构，采用 Apache 2.0 许可，强化了指令遵循、工具调用与推理能力；训练覆盖 56 种语言，侧重欧洲语言尤其是波兰语，训练流程包含 500B token 预训练、26M 样本 SFT、14 个环境下的修改版 GRPO 强化学习，基于开源框架 ALLaMo 实现，训练过程使用 PLGrid 环境下的计算授权 PLG/2026/019559，资源来自 Athena 与 Helios 超算、欧盟 EuroHPC Joint Undertaking 资助的 Gaia AI 工厂。官方同步预告后续将推出相关决策模型与 dflash 工具。

reddit · r/LocalLLaMA · /u/jacek2023 · 11月10日 16:30

**「为什么重要」** 该模型针对多语言场景优化了指令遵循与工具调用能力，对需要本地部署多语言开源模型的 AI agent 工程师有参考价值；但当前公开信息仅来自社区转发帖，缺少性能基准、agent 专项评估等深度技术细节，需跳转官方链接获取完整上下文。

**「可关注」** 可关注：该模型采用修改版 GRPO 做强化学习，基于开源框架 ALLaMo 训练，已发布 GGUF 格式权重，Apache 2.0 许可支持本地部署与二次开发。

**标签**: `#coding-agent`, `#open-source-llm`, `#multilingual`, `#tool-use`

---

<a id="item-agent-engineer-8"></a>
### [Deletion Tuning 微调新路径](https://www.reddit.com/r/LocalLLaMA/comments/1xswmb7/the_surprising_effectiveness_of_deleting_weights/) ⭐️ 5.5/10

2026 年 11 月 10 日 Reddit 社区出现用户/u/Thrumpwart 发布的介绍 Deletion Tuning 的帖子，称该 LLM 后训练方法仅零化少于 0.05%的模型权重，无需其他修改即可在监督微调、可验证奖励强化学习、同策略蒸馏三个场景下匹配全量微调（FFT）性能。其学习的二值掩码作用于 transformer 块的门控投影权重，训练后 checkpoint 体积比 FFT 小数百到数千倍，且强化学习场景下旧任务准确率接近基座模型，而 FFT、LoRA、随机稀疏微调最多下降 5.4 个百分点。发帖人后续补充了对应 GitHub 仓库、HuggingFace 掩码仓库、项目博客及 NeurIPS 2026 海报链接，但最初发布时无官方一手来源（如论文、官方博客）佐证相关性能声明。

reddit · r/LocalLLaMA · /u/Thrumpwart · 11月10日 19:44

**「为什么重要」** 该方法提出了一种仅修改极少量权重的 LLM 后训练路径，若性能声明经独立验证成立，可降低 coding agent 等场景的持续学习微调成本与灾难性遗忘风险；目前相关资源已公开，但尚无独立复现结果佐证其效果。

**「可关注」** 可关注 Deletion Tuning 公开的代码与掩码资源，验证其极低权重重修改下匹配全量微调性能的可复现性，以及稀疏掩码对 agent 持续学习场景的适配效果。

**标签**: `#coding-agent`, `#sparse-fine-tuning`, `#llm-continual-learning`

---

## AI 日报
{: #sec-ai-daily .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-daily" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-daily-1"></a>
### [Anthropic 启动 IPO 路演 代码 ANT](https://www.anthropic.com/news/roadshow-launch) ⭐️ 9.8/10

AI 实验室 Anthropic 正式启动拟议首次公开募股（IPO）路演，拟发行 8.25 亿股 A 类普通股，其中 8.013 亿股由 Anthropic 出售，2364.86 万股由现有股东出售，Anthropic 不从现有股东出售股份中获得收益。发行价预计为每股 70 至 78 美元，股票将申请在纳斯达克全球精选市场上市，交易代码为“ANT”。承销商可获得 30 天期权，最多额外购买 1.2375 亿股。目前注册声明已提交美国证券交易委员会但尚未生效，相关证券在注册声明生效前不得出售，要约购买也不得被接受。本次公告不构成出售或购买这些证券的要约，在相关证券于各州或司法管辖区完成注册或资格认定前，不得在该区域开展相关要约、邀约或出售活动。

rss · Anthropic News · 11月10日 00:00

**「为什么重要」** 这是头部 AI 实验室首次公开募股的关键推进步骤，若完成将成为 AI 行业近年最具影响力的资本事件之一，对行业融资、估值体系有直接参考意义。

**「可关注」** 可关注：本次 IPO 承销商为高盛（Goldman Sachs）与摩根士丹利（Morgan Stanley），且赋予承销商 30 天期内最多 1.2375 亿股的超额配售选择权。

**标签**: `#lab`, `#industry`, `#policy`

---

<a id="item-ai-daily-2"></a>
### [OpenAI 与 Upwork 发布自由职业 AI 影响研究](https://openai.com/index/ai-effect-on-freelance-work) ⭐️ 8.8/10

OpenAI 与 Upwork 联合发布新研究，揭示 AI 对自由职业市场的影响。研究发现自由职业需求结构发生变化，AI 相关项目预算与工时均呈增长趋势，同时要求从业者具备新的技能组合。研究未披露具体量化数据。

rss · OpenAI Blog · 11月10日 07:00

**「为什么重要」** 该研究由模型方与平台方联合开展，其数据直接关联 AI 技术应用与自由职业市场交易，具备较高的行业参考价值。

**「可关注」** 可关注：AI 相关自由职业项目预算与工时双增，且要求新技能组合。

**标签**: `#lab`, `#industry`, `#research`

---

<a id="item-ai-daily-3"></a>
### [Claude 新增三款协同办公功能](https://claude.com/resources/articles/sheets-whiteboards-data) ⭐️ 8.8/10

Anthropic 今日正式推出 Claude 协同办公功能套件：Claude Whiteboards（团队协作白板）与 Claude Sheets（协同电子表格）进入 Beta 测试，原 Dashboards 正式更名为 Claude Data 并全面上线（GA）。所有付费 Claude 计划用户均可使用这三款功能，支持网页、桌面、移动端访问；Claude Data 需搭配数仓、CRM 等数据连接器使用，新增数据故事、认证查询、实时共享、缓存与变更追踪能力。企业版用户默认关闭 Claude Whiteboards 与 Sheets，Claude Data 将于 2026 年 11 月 19 日默认启用，管理员可随时在 Organization settings &gt; Artifacts 中调整开关。

rss · Claude Blog · 11月10日 00:00

**「为什么重要」** 该发布将 Claude 的能力从纯对话工具延伸至团队协同办公场景，用户无需将 Claude 的输出复制到其他工具即可直接协作，降低了团队跨工具切换的成本。

**「可关注」** 可关注：企业版管理员需在 Organization settings &gt; Artifacts 中手动开启 Claude Whiteboards 与 Sheets，Claude Data 将于 2026 年 11 月 19 日默认启用。

**标签**: `#lab`, `#product`, `#industry`

---

<a id="item-ai-daily-4"></a>
### [ChatGPT 上线企业信息管理功能](https://openai.com/index/introducing-businesses-chatgpt) ⭐️ 7.8/10

OpenAI 于 2026 年 11 月 10 日发布 ChatGPT 企业功能，支持企业管理自身在平台的信息、获取自身展示相关的运营洞察，还可将用户兴趣转化为行动。

rss · OpenAI Blog · 11月10日 10:00

**「可关注」** 可关注：ChatGPT 企业功能的信息管理、展示洞察与用户兴趣转化能力的后续接口开放与集成规则。

**标签**: `#product`, `#industry`, `#lab`

---

<a id="item-ai-daily-5"></a>
### [OpenAI 发布教育 AI 指导研究](https://openai.com/index/closing-ai-guidance-gap-education) ⭐️ 7.8/10

OpenAI 官方博客于 2026-11-10 发布新 ThinkYoung 研究，同时总结 EMEA 地区教育合作经验，聚焦缩小教育领域的 AI 指导缺口。核心覆盖方向包括支持教师开展 AI 教学、提升学生 AI 素养、培养学生独立学习能力。

rss · OpenAI Blog · 11月10日 09:00

**「为什么重要」** 该研究成果与合作经验为教育领域 AI 应用提供了官方参考路径，可支撑教育从业者调整 AI 教学与素养培养策略。

**「可关注」** 可关注：教育场景下 AI 工具对教师教学支持、学生 AI 素养培养的落地路径。

**标签**: `#lab`, `#industry`, `#policy`

---

<a id="item-ai-daily-6"></a>
### [Claude 新增 Sheets/Whiteboards 工件与交互连接器](https://claude.com/resources/articles/more-ways-to-work-with-claude-sheets-whiteboards-and-interactive-connectors) ⭐️ 7.8/10

Anthropic 官方今日扩展 Claude 产品矩阵，新增 Claude Sheets、Claude Whiteboards、Claude Data（原 Dashboards）三类协作工件，支持团队共同编辑表格、白板、数据看板，上下文可在不同工件间无损耗流转。基于 MCP 协议的交互式连接器完成升级，合作伙伴可内嵌 Adobe、Atlassian 等应用到 Claude 内，Salesforce、NetSuite、Workday 插件内置垂直场景技能，Claude Marketplace 已收录超 9000 个连接器与插件。本次更新还预告即将推出 Claude Meetings 功能，支持会议中自动记笔记、同步更新团队文档；配套企业版管控能力同步上线，包括自动连接（beta）、细粒度权限设置、会话隔离等，部分功能仍处于 beta 阶段。Anthropic 内部非技术团队已落地相关能力，法务团队将合同审核周期从 3 天压缩至 24 小时，财务团队将高管业务汇报制作周期从 10 小时缩短至 30 分钟，外部客户如 Accenture、Datadog、Gusto、HubSpot 也已落地对应场景。

rss · Claude Blog · 11月10日 00:00

**「为什么重要」** 本次更新将 Claude 此前在开发者场景的效率优势拓展到全团队非技术协作场景，配套企业级安全管控能力补齐了大规模企业落地的合规短板，覆盖法务、财务、产品等多垂直场景的落地需求。

**「可关注」** 可关注：基于 MCP 协议的交互式连接器已开放合作伙伴内嵌应用能力，Claude Marketplace 现有超 9000 个连接器与插件，企业版会话隔离、细粒度权限管控、自动连接等功能已进入 beta 阶段。

**标签**: `#lab`, `#product`, `#industry`

---

<a id="item-ai-daily-7"></a>
### [Claude 交互连接器支持全应用嵌入](https://claude.com/resources/articles/interactive-connectors-full-tool) ⭐️ 7.8/10

Anthropic 更新 Claude 交互连接器，支持第三方应用全嵌入，用户与 Claude 可在同一工具界面协作、无需切换标签页。该功能正在网页端与 Claude 桌面端全套餐 rollout，需账号更新至新 Claude 体验或由组织开启。初始支持 Asana、Canva、Confluence、Notion 等工具，Figma、Harvey、Shopify 的集成正在开发中。开发者可基于公开预览的 MCP Apps 构建跨 AI 应用的全嵌入工具集成。

rss · Claude Blog · 11月10日 00:00

**「为什么重要」** 此前交互连接器仅支持工具的小尺寸预览，本次更新让 Claude 可直接操作用户已打开的工具页面/文件，减少上下文切换成本。同时基于 MCP Apps 构建的集成不限于 Claude，可运行在所有支持该扩展的 AI 应用中。

**「可关注」** 可关注：MCP Apps 现已公开预览，开发者可基于其构建跨 AI 应用的全嵌入工具集成。

**标签**: `#product`, `#lab`, `#industry`

---

## AI 羊毛
{: #sec-ai-deals .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-deals" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-deals-1"></a>
### [小渔排班 永久免费公告](https://www.appinn.com/xiaoyu-shift-calendar-free/) ⭐️ 8.0/10

你看到的内容可能由第三方 AI 基于小众软件文章提炼总结而成，可能与原文真实意图存在偏差。不代表小众软件观点和立场。请&lt;a href=&quot;https://www.appinn.com/xiaoyu-shift-calendar-free/&quot; target=&quot;\_blank&quot;&gt;点击链接阅读原文&lt;/a&gt;细致比对和校验。&lt;br /&gt;&lt;br /&gt;轮班日历应用小渔排班自 2026 年 10 月起全功能永久免费，无广告、无订阅，仅保留自愿支持开发者的选项。该应用 2018 年上线，曾为付费应用，最高位列国区 App Store 效率付费榜第 2 名，支持班次闹钟、工时薪资统计、班表导出、iCloud 同步等功能，适配 iPhone、iPad、Apple Watch 等多设备，开发者表示会继续长期维护更新。

rss · 小众软件 · 11月10日 14:48

**「为什么重要」** 排班日历赛道竞争激烈，该应用已持续更新 8 年，永久免费政策可降低轮班工作者的使用成本，无需为功能付费或忍受广告。

**「可关注」** 可关注：仅保留自愿支持选项的免费模式，适合面向垂直场景的长期维护型工具参考，无强制付费点。

**标签**: `#free-tier`, `#promo`, `#limited-free`

---

<a id="item-ai-deals-2"></a>
### [复旦切问学术双十一积分翻倍](https://www.appinn.com/qiewenpaper-1111/) ⭐️ 7.0/10

复旦大学 NLP 团队开发的被称为「学术版 Codex」的工具「切问学术」推出双十一限时福利，活动期间订阅任意会员套餐（Plus、Pro、Max X2、Max X5，月付/年付均可，单个账号最多可购 12 个月），每月到账积分为平时的 2 倍，老会员升级也可参与。以 Pro 年付为例，全年积分从平时的 240 万涨至 480 万。此外现在下载并登录客户端还可额外获赠 1 万积分。

rss · 小众软件 · 11月10日 06:46

**「为什么重要」** 切问学术可自动跑实验、写综述、申请算力，高消耗的 Agent 任务正需要大量积分，双倍积分刚好降低重度使用成本。年付本身立省 15%叠加双倍积分是全年入手最优窗口，且已购会员时长的双倍积分在活动结束后仍会正常发放。

**「可关注」** 可关注：活动期间订阅或升级任意会员均可享双倍积分，单个账号最多可囤 12 个月会员时长，新用户下载登录客户端还可额外领取 1 万积分。

**标签**: `#promo`, `#credits`, `#limited-free`, `#api`

---