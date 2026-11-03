---
layout: default
title: "Horizon Summary: 2026-11-04 (ZH)"
date: 2026-11-04
lang: zh
---

> 从 180 条内容中筛选出 16 条重要资讯。

<nav id="ah-toc" class="ah-toc" aria-label="目录"><span class="ah-toc-title">目录</span><ul><li><a href="#sec-harness-arch"><span class="ah-toc-name">Harness 架构</span><span class="ah-toc-count">3条</span></a></li><li><a href="#sec-agent-engineer"><span class="ah-toc-name">Agent 工程师日报</span><span class="ah-toc-count">9条</span></a></li><li><a href="#sec-ai-daily"><span class="ah-toc-name">AI 日报</span><span class="ah-toc-count">3条</span></a></li><li><a href="#sec-ai-deals"><span class="ah-toc-name">AI 羊毛</span><span class="ah-toc-count">1条</span></a></li></ul></nav>

---

**[Harness 架构](#sec-harness-arch)**
1. [Cloudflare Agents 0.33.0 发布](#item-harness-arch-1) ⭐️ 8.3/10
2. [pydantic-ai v2.65.0 发布](#item-harness-arch-2) ⭐️ 6.8/10
3. [openai-agents-js v0.22.0-alpha.1 发布](#item-harness-arch-3) ⭐️ 5.8/10

**[Agent 工程师日报](#sec-agent-engineer)**
1. [CWE-bench v2 发布 含 100 项安全漏洞评测任务](#item-agent-engineer-1) ⭐️ 8.8/10
2. [StateBench 长上下文状态跟踪基准上线](#item-agent-engineer-2) ⭐️ 7.8/10
3. [Qwen 3.8 27B 实现权重解读](#item-agent-engineer-3) ⭐️ 7.0/10
4. [CUA-Master 论文提出嵌套双循环改进框架](#item-agent-engineer-4) ⭐️ 7.0/10
5. [NorthCUA 技术报告：规模化经验加速 GUI 智能体](#item-agent-engineer-5) ⭐️ 7.0/10
6. [datasette-agent 0.5a0 发布](#item-agent-engineer-6) ⭐️ 6.8/10
7. [Transformers 发布 MIC 捕获 SDPA 注意力 bug](#item-agent-engineer-7) ⭐️ 6.8/10
8. [CoworkOS 长期自动化 harness 提出](#item-agent-engineer-8) ⭐️ 6.0/10
9. [uni-robot-agent 开源框架论文](#item-agent-engineer-9) ⭐️ 6.0/10

**[AI 日报](#sec-ai-daily)**
1. [Heimstaden 落地 ChatGPT Enterprise 与 Codex 改造物业](#item-ai-daily-1) ⭐️ 6.8/10
2. [OpenAI 任命 Jill Hazelbaker 为企业事务官](#item-ai-daily-2) ⭐️ 6.8/10
3. [Google 用轻量分类器路由 Gemini 降本](#item-ai-daily-3) ⭐️ 6.8/10

**[AI 羊毛](#sec-ai-deals)**
1. [Epic 13 款小游戏限免 11 月 9 日截止](#item-ai-deals-1) ⭐️ 9.0/10

---

## Harness 架构
{: #sec-harness-arch .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-harness-arch" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-harness-arch-1"></a>
### [Cloudflare Agents 0.33.0 发布](https://github.com/cloudflare/agents/releases/tag/agents%400.33.0) ⭐️ 8.3/10

Cloudflare Agents 0.33.0 正式发布，核心变更为新增 Pi 1.5 全链路支持（覆盖 PiHarness、pi-ai 模型、Pi 工具），运行时优化实现流式存储事务最多降低 27 倍、2048 并发会话下 agent 运行吞吐从 88 次/秒提升至 459 次/秒；同时迭代会话 API，session.watch\(\) 替代 session.events\(\)、新增 session.continue\(\) 续跑能力与 defaults.maxTurns 工具轮次限制，移除 retry\(\)、parked 状态等旧逻辑。该版本存在 breaking changes，Pi 依赖需统一升级至 ~1.5.0，升级后无法回滚至 1.4 版本，需按官方指南调整代码。

github · github-actions\[bot\] · 11月3日 13:14

**「设计要点」** 流式输出改为按最长 1 秒间隔批量写入存储，避免逐更新触发写库；调度器移除每次提交全量重检所有会话的逻辑，批量提交共享存储调用，正常运行无存储读；大内容流式采用追加写入而非全量拷贝，降低内存峰值。

**「改了什么」** \1. 完成 Pi 1.5 适配，覆盖 PiHarness、pi-ai 模型、Pi 工具全链路，支持运行中断后无需新消息即可续跑；2. 流式存储批处理、调度器逻辑优化，带来存储事务、吞吐、内存的量化提升；3. 会话 API 迭代，session.watch\(\) 替代 session.events\(\) 返回实时会话视图，新增 session.continue\(\)、defaults.maxTurns，移除 retry\(\) 和 parked 状态；4. 浏览器工具新增 Browser.functionDocs\(\)、作用域锁等能力，browserTool 支持 harness 中止调用。

**「评论」** 暂无社区评论内容。

**标签**: `#runtime`, `#tools`, `#scalability`

---

<a id="item-harness-arch-2"></a>
### [pydantic-ai v2.65.0 发布](https://github.com/pydantic/pydantic-ai/releases/tag/v2.65.0) ⭐️ 6.8/10

pydantic-ai 官方 v2.65.0 版本于 2026 年 11 月 3 日发布，面向 agent harness 工程师提供运行时、工具、权限相关的增量更新。新增 OpenAI Responses 的 WebSocket 传输、ConversationStore 会话日志存储、Anthropic web 工具调用方配置、AskUserAnswer 多模态备注、12 小时 OpenAI 提示缓存保留、OpenRouter 与 Claude 模型的原生中途系统提示发送能力。修复模型回退逻辑、多提供商错误分类、工具调用统计、Temporal 重试策略、会话捕获保护等多项问题，同时调整了 Bedrock、Google 等模型提供商的兼容性与错误处理逻辑。

github · dsfaccini · 11月3日 01:25

**「设计要点」** 运行时新增 non\_retryable\_model\_errors 配置，默认禁止 Temporal 重试不可恢复的模型错误；工具层新增 ConversationStore 单次存储会话日志与 revision 冲突检测机制，gh-aw 规范会话捕获受工具层保护，FileSystem 工具支持在 PrefixTools 下转发事件；模型层细化错误分类，区分内容过滤、配额超限等场景的触发逻辑。

**「改了什么」** 相对 v2.64.0，新增 OpenAI Responses WebSocket 传输、ConversationStore 会话存储、Anthropic web 工具 allowed\_callers 配置、AskUserAnswer 多模态备注、12 小时 OpenAI 提示缓存保留、OpenRouter 与 Claude 模型的原生中途系统提示发送能力；修复模型回退逻辑、多提供商错误分类、工具调用统计、Temporal 默认重试策略、会话捕获保护等多项问题。

**标签**: `#runtime`, `#tools`, `#permissions`

---

<a id="item-harness-arch-3"></a>
### [openai-agents-js v0.22.0-alpha.1 发布](https://github.com/openai/openai-agents-js/releases/tag/v0.22.0-alpha.1) ⭐️ 5.8/10

这是 OpenAI 官方发布的 openai-agents-js（JavaScript/TypeScript 版 OpenAI Agents SDK）的首个 alpha 版本 v0.22.0-alpha.1。本次发布核心新增内嵌 Codex harness，同时提供 Linux x64、macOS Apple silicon、Windows x64 三个平台的预置启动归档包，安装需使用 Node.js 24 及其自带 npm，校验归档 SHA-256 校验和后解压，配置 OPENAI\_API\_KEY 即可运行示例，还支持将四个预构建 SDK 包集成到现有应用。

github · markstuart-oai · 11月3日 15:36

**「设计要点」** 该 alpha 将 Codex harness 直接内嵌到 OpenAI Agents JS/TS SDK 中，同时提供可集成到现有应用的四个预构建 SDK 包，是官方首次推出的 JS/TS 端 Agent harness 集成方案。

**「改了什么」** 本次 alpha 发布首次在 OpenAI Agents JS/TS SDK 中内嵌 Codex harness，新增三个平台的预置启动归档包，同时公开安装指南、alpha 版更新日志与构建测试结果链接。

**标签**: `#runtime`, `#tools`

---

## Agent 工程师日报
{: #sec-agent-engineer .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-agent-engineer" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-agent-engineer-1"></a>
### [CWE-bench v2 发布 含 100 项安全漏洞评测任务](https://huggingface.co/blog/cwe-bench) ⭐️ 8.8/10

2026 年 11 月 3 日，Hugging Face 博客发布由 Collinear AI 开发的 CWE-bench v2，公开 100 项面向编码智能体的安全漏洞评测任务，所有任务基于真实开源仓库，要求智能体定位并修复安全漏洞且不破坏原有功能。关键细节包括：评分全程序化可复现，LLM 评审团参与校验校验器的难度与公平性，保留未公开 held-out 集用于追踪模型在未见过任务上的进展（需联系 cyber@collinear.ai 申请），100 项任务覆盖 91 种不同 CWE 漏洞类型，任务环境同时可用于训练防御型智能体的奖励信号；当前公开评测中，Gemini 4 Argon 以 67.8% pass@1、81.0% pass@4 位列第一，11 个被评测模型中已有 95 项任务被至少一个模型解决，但榜首模型仍有 19%的任务无法完成，长尾问题尚未解决。该基准面向 coding agent 开发者、安全研究者开放，数据集需在 Hugging Face 页面接受访问条件后获取，支持通过 Harbor 工具直接运行评测。

rss · Hugging Face Blog · 11月3日 00:00

**「为什么重要」** 这是目前少数聚焦真实仓库安全漏洞修复场景的编码智能体公开基准，程序化评分+held-out 集的设计可减少评测中的记忆化水分，方便社区客观对比不同模型在安全防御场景的实际能力。

**「可关注」** 可关注：公开任务采用 Harbor 容器化环境+确定性校验器，可直接通过\`harbor run\`命令从 Hugging Face 仓库拉取运行，无需手动克隆代码；若使用 Git 拉取任务，需提前通过\`hf auth login\`将 HF token 添加到 Git 凭据助手，降低评测接入成本。

**标签**: `#eval`, `#coding-agent`

---

<a id="item-agent-engineer-2"></a>
### [StateBench 长上下文状态跟踪基准上线](https://huggingface.co/blog/allenai/statebench) ⭐️ 7.8/10

2026 年 11 月 3 日 Hugging Face 官方博客发布 StateBench 长上下文状态跟踪基准，配套公开技术报告、数据集与代码，包含 4 个递进难度等级，覆盖从不可变赋值到变量引用赋值的不同状态更新场景。测试显示循环架构与混合架构（如 Gated DeltaNet）在超长序列状态跟踪任务上泛化性显著优于 Transformer，前沿大模型在更长输入下的高难度状态跟踪任务上准确率跌至 13%以下；所有测试的预训练模型最长训练上下文不超过 64000 token，测试输入远长于该长度。该基准直接对应 AI Agent 开发中的核心状态跟踪需求，可为 Agent 评估 harness 提供标准化测试能力。

rss · Hugging Face Blog · 11月3日 17:15

**「为什么重要」** StateBench 首次系统化覆盖不同复杂度的长上下文状态跟踪任务，填补了该领域标准化评估工具的空白，直接匹配 AI Agent 对状态跟踪能力的核心需求。当前无公开社区案例证明其已被集成到主流 Agent 评估 harness 中，实际落地效果待验证。

**「可关注」** 可关注：StateBench 同时提供多种问题格式（如 RULER 风格、电子表格编辑格式）与 4 个难度等级，可针对性补充现有 Agent 评估 harness 的状态跟踪测试覆盖。

**标签**: `#eval`, `#coding-agent`, `#memory`, `#harness`

---

<a id="item-agent-engineer-3"></a>
### [Qwen 3.8 27B 实现权重解读](https://simonwillison.net/2026/Nov/3/qwen-can-interpret-model-weights/) ⭐️ 7.0/10

2026 年 11 月 3 日，Simon Willison 发布实测记录，显示本地运行的 Qwen 3.8 27B（采用 lmstudio-community/Qwen3.8-27B-GGUF 的 Q4\_K\_M 量化版，体积 17GB）可复现论文《Sparks of Weight-Space Programming》中仅前沿模型展示的权重空间编程能力：在无代码执行、无计算工具辅助的前提下，仅通过输入原始权重文本即可识别对应训练的简化 Atari 游戏类型，最长单任务推理耗时 46 分 12 秒、消耗 43506 个推理 token，可正确识别 Pac-Man 等任务，输出置信度 72%。该能力此前仅 GPT-6 Astra 等前沿模型被证实具备，目前仅验证了游戏识别场景，未公开权重修改能力的实测结果。

rss · Simon Willison · 11月3日 16:29 · [社区讨论](https://news.ycombinator.com/item?id=50355251)

**「为什么重要」** 该实测首次证明小尺寸开源模型也可原生读取模型权重，打破了该能力仅前沿模型垄断的认知，为 AI agent 工程师低成本研究模型内部可解释性提供了可行路径。目前该能力的泛化性、结果正确性尚未得到独立验证，实际工程价值仍待观察。

**「可关注」** 当前小模型完成权重解读任务依赖超过默认 8192 的长上下文支持，单任务推理耗时可达 40 分钟以上，token 消耗超 4 万，结果正确性尚无独立验证，距离实际工程应用仍有距离。

**「评论」** 社区对该能力存在明显分歧，部分用户认为 Qwen 3.8 27B 已具备接近前沿模型的权重处理能力，仅需高层架构指导即可替代付费前沿模型；另一部分用户质疑权重解读的正确性，认为当前演示仅复现了人类研究者可完成的常规步骤，未证明模型真正理解权重逻辑，且未验证同代模型的权重修改能力。

**标签**: `#observability`, `#memory`

---

<a id="item-agent-engineer-4"></a>
### [CUA-Master 论文提出嵌套双循环改进框架](https://huggingface.co/papers/2611.03126) ⭐️ 7.0/10

Hugging Face Daily Papers 于 2026-11-03 介绍 CUA-Master 论文，提出嵌套双循环递归改进框架以扩展计算机使用代理（CUA）开发。外层系统级循环采用 world-data-model 飞轮，持续纳入开放世界语料库并利用模型弱点指导数据构建与优化迭代；内层数据级循环耦合开放世界播种与自催化传播。该框架针对现有 CUA 交互数据多样性、可控性和可靠性有限，以及传统优化管道缺乏迭代反馈的问题。当前材料为截断摘要，完整技术细节与性能数据未提供。

rss · Hugging Face Daily Papers · 11月3日 00:00

**「为什么重要」** 现有 CUA 开发受限于数据质量与优化管道迭代能力，该框架提供了系统化的递归改进思路。但具体效果与可复现性需等待完整论文验证。

**「可关注」** 可关注：嵌套双循环中&quot;利用模型弱点指导数据构建&quot;的机制，可能为 coding agent 的自我改进数据 pipeline 提供新思路。

**标签**: `#coding-agent`, `#eval`, `#orchestration`

---

<a id="item-agent-engineer-5"></a>
### [NorthCUA 技术报告：规模化经验加速 GUI 智能体](https://huggingface.co/papers/2611.02102) ⭐️ 7.0/10

2026 年 11 月 3 日 HF 每日论文收录 NorthCUA 技术报告，该条目获得 30 次点赞；报告提出面向 GUI 操作的计算机使用智能体系统 NorthCUA，核心设计包括经验飞轮、专用智能体 Harness、递归自改进机制与分阶段学习 pipeline，目标是提升长时程 GUI 任务的表现。Experience Flywheel 为 NorthCUA Harness 提供多样可执行任务，Harness 负责维持长交互、记录决策、校验任务结果，飞轮基于这些记录整理验证通过的轨迹；针对未解决任务，递归自改进机制演化可复用技能，同时保留已验证里程碑，供后续尝试复用前期进展；分阶段学习结合飞轮经验与 grounding 数据，通过中间训练和长时程监督微调提升 GUI 能力。目前公开的摘要内容被截断，未披露性能评估数据，相关设计覆盖 harness、eval、memory 等 coding agent 核心环节，主要面向 GUI 智能体、coding agent 工程师群体。

rss · Hugging Face Daily Papers · 11月3日 00:00

**「为什么重要」** 这是目前公开较少完整披露计算机使用智能体经验流转链路、递归自改进与分阶段学习全流程设计的技术报告，对 GUI 智能体与 coding agent 工程有直接参考价值；但当前公开内容缺少性能验证数据，实际效果尚未得到证实。

**「可关注」** NorthCUA 将经验飞轮、任务执行 Harness、递归自改进、分阶段学习串为完整的 GUI 智能体训练流程，其中保留已验证里程碑供后续尝试复用的设计，对长时程 GUI 任务的 agent 工程有直接参考价值。

**标签**: `#harness`, `#coding-agent`, `#eval`, `#memory`

---

<a id="item-agent-engineer-6"></a>
### [datasette-agent 0.5a0 发布](https://github.com/datasette/datasette-agent/releases/tag/0.5a0) ⭐️ 6.8/10

2026 年 11 月 3 日，simonw 正式发布 datasette-agent 0.5a0，面向 Datasette 生态的 AI 代理工具。本次更新新增会话级模型选择能力，模型在会话创建时锁定并随会话标题展示，模型列表来自 datasette-llm 的 agent 配置；新增 \# 引用标签功能，支持自动补全关联表、数据库、存储查询，权限校验跟随发送消息的用户执行，标签可点击跳转至对应 Datasette 页面并为模型提供 schema、查询详情等上下文；新增 register\_agent\_reference\_types\(\) 插件钩子，支持插件自定义 \# 引用类型的搜索、链接、模型指令与上下文逻辑，search 和 context 函数支持异步实现；新增 Datasette 页面侧边栏，代理可通过 show\_in\_panel 工具在侧边栏打开页面，窄屏下支持 Chat 与 Panel 切换。该版本要求 Python 3.11 及以上，最低依赖为 datasette&gt;=1.0a41、datasette-llm&gt;=0.1a9、llm&gt;=0.37.1，新增停止按钮、会话后台运行、消息框运行时可编辑等交互特性，修复了系统提示未传递到部分模型的兼容问题，增强了 SQL 工具的参数与统计能力，移除了原「Explore with AI agent」功能及对应权限。

github · simonw · 11月3日 22:58

**「为什么重要」** 本次更新提供的用户级权限校验、插件化引用类型扩展等模式，对通用 agent 工程有参考价值；但目前功能影响主要局限于 Datasette 生态，暂无更广泛的性能或落地数据。

**「可关注」** 可关注：新增的 register\_agent\_reference\_types\(\) 插件钩子支持自定义 \# 引用类型的搜索、上下文注入逻辑，为 agent 上下文扩展提供了可复用的插件化模式。

**标签**: `#permissions`, `#memory`, `#coding-agent`, `#orchestration`

---

<a id="item-agent-engineer-7"></a>
### [Transformers 发布 MIC 捕获 SDPA 注意力 bug](https://huggingface.co/blog/transformers-mic) ⭐️ 6.8/10

2026 年 11 月 3 日 Hugging Face 发布 Transformers 模型集成契约（MIC）规范，该规范源于 2026 年 7 月 30 日 Transformers 为 T5 启用 PyTorch 缩放点积注意力（SDPA）后引入的回归 bug：UMT5 解码器可在训练时关注未来 token，且无崩溃报错，在 main 分支留存近两个月未检出。MIC 通过将真实模型配置缩小为 CPU 可运行的 fixture，搭配使用路径和人工审核的基线输出，重放 5 个月 Transformers 提交时成功捕获该回归，对应 T5 契约的 CPU runner 单步耗时 13.4 秒（不含 setup）。关键细节包括：该 bug 仅出现在 SDPA 路径，仅运行 eager 注意力路径无法检出；fixture 保留原始 tokenizer、processor 字节级文件和权重格式，覆盖加载转换代码；UMT5 fixture 仅 66MB，远小于原始 1.227GB checkpoint。

rss · Hugging Face Blog · 11月3日 00:00

**「为什么重要」** Transformers 当前支持 750+模型类型，全量 GPU 集成测试无法在 PR 阶段全量运行，回归往往在定时跑完才进入 main 分支。MIC 将大模型缩小为 CPU 可运行的 fixture，可在 PR 阶段提前捕获回归，同时覆盖过大无法放入标准 GPU runner 的超大模型测试场景。

**「可关注」** 可关注：模型测试 fixture 必须覆盖实际使用的执行路径（如 SDPA 而非仅 eager 注意力），且需保留原始预处理、权重加载逻辑，否则会漏掉对应路径的回归。

**标签**: `#eval`, `#harness`, `#observability`

---

<a id="item-agent-engineer-8"></a>
### [CoworkOS 长期自动化 harness 提出](https://huggingface.co/papers/2611.03178) ⭐️ 6.0/10

2026-11-03，Hugging Face Daily Papers 收录 CoworkOS 论文，提出面向长期 horizon 的通用 agent coworker 自动化 harness。该系统采用三层架构，将任务策略（模型决定动作、委托与接受）与执行管理（运行时维护状态与反馈）分离，支持直接执行或同步/异步子代理委托。论文内容被截断，未披露性能数据、评估结果或完整实现细节，实际工程可用性待验证。

rss · Hugging Face Daily Papers · 11月3日 00:00

**「为什么重要」** 该设计将策略决策与运行时状态管理解耦，对构建 agent harness 与 orchestration 系统具有参考价值。但缺乏性能基准与实现细节，其实际效果尚未证实。

**「可关注」** 可关注：CoworkOS 三层架构中模型决策与运行时状态管理的分离方式，以及同步/异步子代理委托的职责划分。

**标签**: `#harness`, `#orchestration`

---

<a id="item-agent-engineer-9"></a>
### [uni-robot-agent 开源框架论文](https://huggingface.co/papers/2611.01560) ⭐️ 6.0/10

2026 年 11 月 3 日 HF 每日论文收录机器人使用代理（RUA）领域开源统一框架 uni-robot-agent，该框架支持开源权重 RUA 的进一步训练。无特权输入条件下，开箱即用的 Qwen3.8-Flash-Next 在 RoboDojo 基准获得 31.39 分，超过此前 GPT-6 Astra-RoboProbe 的 28.97 分及多数 VLA/WAM 基线，在 19 项真实任务上表现有竞争力。研究同时总结出驱动 RUA 有效运作的 4 项通用能力，提示后续训练需联合发展这 4 项能力。

rss · Hugging Face Daily Papers · 11月3日 00:00

**「为什么重要」** 该开源框架降低了机器人使用代理的研究门槛，开源模型在 RoboDojo 基准超越此前专有模型 SOTA 的结果具备可复现性；但研究场景仅覆盖机器人代理领域，对通用代理工程的参考价值需结合具体需求判断。

**「可关注」** 可关注：uni-robot-agent 开源框架支持开源权重机器人使用代理的进一步训练，其跨模型分析结论提示后续 RUA 训练可联合发展关联有效性的 4 项通用能力。

**标签**: `#harness`, `#eval`

---

## AI 日报
{: #sec-ai-daily .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-daily" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-daily-1"></a>
### [Heimstaden 落地 ChatGPT Enterprise 与 Codex 改造物业](https://openai.com/index/heimstaden) ⭐️ 6.8/10

OpenAI 官方博客发布案例，欧洲住宅地产管理公司 Heimstaden 落地 ChatGPT Enterprise 与 Codex 改造物业管理业务，声称实现降本、提升员工工作效率。该案例未披露具体量化指标，也未提及更广泛的行业落地影响。

rss · OpenAI Blog · 11月3日 08:00

**「为什么重要」** 这是 OpenAI 官方发布的首个物业场景企业级 AI 落地案例，验证了 ChatGPT Enterprise 与 Codex 在非科技行业的应用可能性，但未披露具体效果数据，暂无法评估实际落地价值。

**「可关注」** 可关注：非科技行业企业落地 ChatGPT Enterprise 与 Codex 的场景适配与效果验证进展。

**标签**: `#lab`, `#industry`, `#product`

---

<a id="item-ai-daily-2"></a>
### [OpenAI 任命 Jill Hazelbaker 为企业事务官](https://openai.com/index/jill-hazelbaker-chief-corporate-affairs-officer) ⭐️ 6.8/10

2026 年 11 月 3 日，OpenAI 官方博客发布人事任命公告，宣布 Jill Hazelbaker 出任公司首席企业事务官，负责领导全球沟通与企业定位相关工作。

rss · OpenAI Blog · 11月3日 00:00

**「为什么重要」** 该信息为 OpenAI 官方公开的一手人事任命，可核对官方原文，属于公司治理层面的人事变动，并非模型或行业新事实，影响面一般。

**「可关注」** 可关注：OpenAI 后续全球沟通与企业定位相关的官方发布动态。

**标签**: `#lab`, `#industry`, `#policy`

---

<a id="item-ai-daily-3"></a>
### [Google 用轻量分类器路由 Gemini 降本](https://developers.googleblog.com/cost-per-task-using-cheap-classifiers-to-route-across-gemini-models-and-thinking-levels/) ⭐️ 6.8/10

Google Developers 官方博客发布面向自主编码 agent 的成本优化方案，提出用轻量级分类器（以 TypeSafe Jev 为例）前置在 Google Antigravity 的模型调用层前，在 Gemini 模型与不同推理级别间路由请求，将核心经济性指标从「每 token 价格」切换为「每成功任务成本」。Jev 是专为高吞吐决策流水线设计的结构化输出分类器，单次前向传播即可完成选项选择、数值评分、Noul 二元概率判断等原子分类任务。在 50 题的编码 agent 基准测试中，Jev 路由方案与全量使用低推理配置的 Gemini 3.8 Flash 均达成 100%任务正确率，且相比全量低推理方案可同时降低成本和响应时延。测试为单轮实验，实际生产中的延迟、token 消耗与成本会随提示长度、上下文缓存、生产负载波动；若路由的低成本选项无法减少简单任务的模型思考量，哪怕零成本的完美路由器也无法降低总成本。Google 同时声明与 TypeSafe 无合作，该路由模式也可用其他分类器实现。

rss · Google Developers AI · 11月3日 00:00

**「为什么重要」** 当前 token 单价持续下降，但自主编码 agent 的工程成本仍在上涨，「每成功任务成本」正成为更核心的经济性指标，该方案给出了可落地的轻量路由实践。

**「可关注」** 可关注：路由分类器需拆分为原子判断，宽泛分类易导致简单任务误判；给推理模型设低输出上限不会降低简单任务的思考 token 消耗，反而可能中断复杂任务推理。

**标签**: `#model`, `#industry`, `#product`

---

## AI 羊毛
{: #sec-ai-deals .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-deals" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-deals-1"></a>
### [Epic 13 款小游戏限免 11 月 9 日截止](https://www.appinn.com/eggs-261103/) ⭐️ 9.0/10

你看到的内容可能由第三方 AI 基于小众软件文章提炼总结而成，可能与原文真实意图存在偏差。不代表小众软件观点和立场。请&lt;a href=&quot;https://www.appinn.com/eggs-261103/&quot; target=&quot;\_blank&quot;&gt;点击链接阅读原文&lt;/a&gt;细致比对和校验。&lt;br /&gt;&lt;br /&gt;Epic 商店正在免费发放 Yash Future Tech Solutions 旗下的 13 款小游戏，领取后永久入库，无需立即下载安装，截止时间为北京时间 2026 年 11 月 9 日凌晨 2:30。

rss · 小众软件 · 11月3日 13:13

**「为什么重要」** 这批限免游戏覆盖射气球、横版解谜、闯关、赛车、走迷宫、数学答题等多品类，已确认可 0 元入库，适合想扩充轻量游戏库的用户在截止前领取。

**「可关注」** 可关注：网页版领取时若遇设备不兼容提示仍可继续完成入库，下载安装可后续操作。

**标签**: `#limited-free`, `#promo`, `#free-tier`

---