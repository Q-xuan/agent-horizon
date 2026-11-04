---
layout: default
title: "Horizon Summary: 2026-11-04 (ZH)"
date: 2026-11-04
lang: zh
---

> 从 194 条内容中筛选出 15 条重要资讯。

<nav id="ah-toc" class="ah-toc" aria-label="目录"><span class="ah-toc-title">目录</span><ul><li><a href="#sec-harness-arch"><span class="ah-toc-name">Harness 架构</span><span class="ah-toc-count">3条</span></a></li><li><a href="#sec-agent-engineer"><span class="ah-toc-name">Agent 工程师日报</span><span class="ah-toc-count">9条</span></a></li><li><a href="#sec-ai-daily"><span class="ah-toc-name">AI 日报</span><span class="ah-toc-count">2条</span></a></li><li><a href="#sec-ai-deals"><span class="ah-toc-name">AI 羊毛</span><span class="ah-toc-count">1条</span></a></li></ul></nav>

---

**[Harness 架构](#sec-harness-arch)**
1. [FastMCP v4.2.0a3 发布](#item-harness-arch-1) ⭐️ 7.8/10
2. [Cloudflare Agents 0.33.0 发布](#item-harness-arch-2) ⭐️ 7.8/10
3. [openai-agents-js v0.22.0-alpha.1 发布](#item-harness-arch-3) ⭐️ 6.8/10

**[Agent 工程师日报](#sec-agent-engineer)**
1. [Allen AI 发布 StateBench 基准](#item-agent-engineer-1) ⭐️ 7.8/10
2. [CUA-Master 嵌套双循环框架提出](#item-agent-engineer-2) ⭐️ 7.0/10
3. [SWE-Trail 历史引导轨迹收集框架发布](#item-agent-engineer-3) ⭐️ 7.0/10
4. [datasette-apps 0.3a0 发布](#item-agent-engineer-4) ⭐️ 6.8/10
5. [datasette-agent 0.5a0 发布](#item-agent-engineer-5) ⭐️ 6.8/10
6. [权重空间编程与 DeepSeek Super-Agent 原型](#item-agent-engineer-6) ⭐️ 6.0/10
7. [RoboColosseum 论文提出野外评估框架](#item-agent-engineer-7) ⭐️ 6.0/10
8. [Palette 小模型生成自定义幻灯片](#item-agent-engineer-8) ⭐️ 5.8/10
9. [Cognition 发布 2026 年 11 月安全指南](#item-agent-engineer-9) ⭐️ 5.8/10

**[AI 日报](#sec-ai-daily)**
1. [思科整合 OpenAI 模型强化企业安全](#item-ai-daily-1) ⭐️ 6.8/10
2. [OpenAI 博客：ChatGPT 与 Codex 加速实体工程](#item-ai-daily-2) ⭐️ 6.3/10

**[AI 羊毛](#sec-ai-deals)**
1. [E 宝 13 款小游戏限免 11 月 9 日截止](#item-ai-deals-1) ⭐️ 9.0/10

---

## Harness 架构
{: #sec-harness-arch .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-harness-arch" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-harness-arch-1"></a>
### [FastMCP v4.2.0a3 发布](https://github.com/PrefectHQ/fastmcp/releases/tag/v4.2.0a3) ⭐️ 7.8/10

PrefectHQ 官方发布 FastMCP v4.2.0a3 alpha 预发布版本，核心调整为整合实验性 skills 子系统，新增带严格目录加载验证的 SkillsDirectoryProvider，弃用 4.1 版 skills 提供者并计划于 4.3 版本移除，同时修复代理发现缓存、OpenAPI Schema 处理、客户端连接恢复、技能安全验证等多项运行时问题。该版本仍将 skills 支持标记为实验性，仅面向集成测试场景。

github · zzstoatzz · 11月3日 23:39

**「设计要点」** skills 子系统围绕 Skill、SkillCatalogProvider、SkillsDirectoryProvider 重构，目录加载阶段逐技能验证后才发布，支持结构化元数据或 YAML allowed-tools 列表的技能无需修改值即可接受；legacy 4.1 skills 提供者与旧版 Skill 构造仍兼容但触发警告，experimental\_skills 路径重定向到新提供者并拒绝子类以保留访问控制，线缆层用 MCPSkill 处理条目、注解与检查，Skill 用于编写；ClientGroup 退出上下文后保留已知工具路由，OAuth 同意绑定支持并发批准，异常中间件匹配子类，空日志方法过滤器表示不记录日志。

**「改了什么」** 相对上一版本，新增严格 SkillsDirectoryProvider 实现目录加载验证，整合 skills 相关提供者，明确弃用 4.1 版 skills 提供者并预告 4.3 移除；新增 Client.read\_skill、fastmcp list --skills、ClientGroup 技能发现等能力，修复代理发现缓存过期、OpenAPI Schema 引用与显式空值保留、客户端连接恢复、keep-alive stdio 传输忽略客户端超时、技能前置内容验证与文件读取限制等多项运行时与安全问题，旧版 skills API 与 Skill 构造仍兼容但触发警告。

**「评论」** 无可用社区评论。

**标签**: `#mcp`, `#tools`, `#runtime`

---

<a id="item-harness-arch-2"></a>
### [Cloudflare Agents 0.33.0 发布](https://github.com/cloudflare/agents/releases/tag/agents%400.33.0) ⭐️ 7.8/10

Cloudflare Agents 0.33.0 发布，核心升级 PiHarness 至 Pi 1.5。通过存储批处理、调度器优化和追加式内存管理，SQLite 存储事务减少最多 27 倍，2048 会话吞吐量从 88 提升至 459 agent runs/秒，大答案内存占用从 &gt;100 MB 大幅降低。新增 session.watch\(\)、session.continue\(\)、defaults.maxTurns 等接口，支持继续运行和轮次限制。Pi 1.4 无法读取 Pi 1.5 对话，部署后无法回滚。

github · github-actions\[bot\] · 11月3日 13:14

**「设计要点」** PiHarness 采用批量存储写入（每秒最多一次）和追加式文本更新，替代逐事件复制，降低 SQLite 事务和堆内存压力。调度器改为按提交聚合检查会话状态，正常 run 零存储读取，session.watch\(\) 分离活跃状态流与持久化转录分页。

**「改了什么」** PiHarness 升级至 Pi 1.5，存储批处理使 SQLite 事务减少最多 27 倍，调度器优化使 2048 会话吞吐量从 88 提升至 459 agent runs/秒，大答案内存占用从 &gt;100 MB 降至接近线性增长。API 层面：session.watch\(\) 替换 session.events\(\)，新增 session.continue\(\) 和 defaults.maxTurns，移除 retry\(\) 和 parked 状态；浏览器工具新增作用域锁与外部访问能力。

**标签**: `#runtime`, `#memory`

---

<a id="item-harness-arch-3"></a>
### [openai-agents-js v0.22.0-alpha.1 发布](https://github.com/openai/openai-agents-js/releases/tag/v0.22.0-alpha.1) ⭐️ 6.8/10

OpenAI 发布 openai-agents-js v0.22.0-alpha.1，这是其 JavaScript/TypeScript Agent SDK 的官方 alpha 版本。本次更新引入嵌入式 Codex harness，为 JS/TS agent 开发提供新的运行支持。发布包覆盖 Linux x64、macOS Apple silicon 和 Windows x64 三套平台，要求 Node.js 24 环境并设置 OPENAI\_API\_KEY。该版本为不稳定 alpha，未提供详细架构分解或破坏性变更说明。

github · markstuart-oai · 11月3日 15:36

**标签**: `#runtime`, `#subagents`

---

## Agent 工程师日报
{: #sec-agent-engineer .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-agent-engineer" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-agent-engineer-1"></a>
### [Allen AI 发布 StateBench 基准](https://allenai.org/blog/statebench) ⭐️ 7.8/10

Allen AI 于 2026 年 11 月 3 日发布 StateBench 基准，用于评估大语言模型在长文档中跟踪实体状态变化的能力，包含 4 个难度等级，对应不同复杂度的变量赋值操作。测试覆盖开源预训练模型、前沿闭源模型及针对任务直接训练的模型，结果显示循环架构与混合架构在长序列状态跟踪任务上的泛化距离远优于 Transformer，前沿模型在更高难度任务上随输入长度增长准确率骤降，最长通用有限难度下准确率跌至 13%以下。该基准面向长运行 AI Agent 开发、模型选型、记忆系统研发的工程师。

rss · Allen AI · 11月3日 08:00

**「为什么重要」** StateBench 填补了长上下文状态跟踪多难度分层的评估空白，首次系统对比了不同架构在各类状态跟踪任务上的性能边界，为长运行 AI Agent 的状态管理、记忆系统设计提供了可直接参考的评估框架。

**「可关注」** 可关注：针对状态跟踪任务做定向训练可显著提升循环及混合架构的长序列状态跟踪表现，同时需注意同一底层问题不同表述格式会对模型得分产生明显干扰。

**标签**: `#eval`, `#memory`

---

<a id="item-agent-engineer-2"></a>
### [CUA-Master 嵌套双循环框架提出](https://huggingface.co/papers/2611.03126) ⭐️ 7.0/10

2026-11-04，Hugging Face Daily Papers 收录论文提出 CUA-Master，一个嵌套双循环递归改进框架，用于扩展计算机使用代理（CUA）。该框架针对现有 CUA 开发中交互数据多样性、可控性与可靠性有限，以及传统优化管道缺乏迭代反馈、自生成经验方法收益递减等问题，设计两层飞轮结构。外层系统级 world-data-model 飞轮持续纳入开放世界语料库，并利用模型弱点指导后续数据构建与优化迭代；内层数据级飞轮耦合开放世界播种与自催化传播。论文标签为 coding-agent、orchestration、eval。

rss · Hugging Face Daily Papers · 11月4日 02:51

**「为什么重要」** 该框架针对 CUA 开发中的数据与优化瓶颈提出双循环方案，与 coding-agent 的构建、优化与评估流程相关。但材料未提供实验数据或性能基准，实际收益尚未验证。

**「可关注」** 可关注：现有 CUA 递归改进多依赖自生成经验且收益递减，CUA-Master 改用开放世界语料库与模型弱点驱动迭代，这一数据获取策略转变值得跟踪其可复现性。

**标签**: `#coding-agent`, `#orchestration`, `#eval`

---

<a id="item-agent-engineer-3"></a>
### [SWE-Trail 历史引导轨迹收集框架发布](https://huggingface.co/papers/2611.02074) ⭐️ 7.0/10

SWE-Trail 论文提出历史引导的轨迹收集框架，用于 coding agent 训练。该框架通过复用已采样轨迹指导后续收集，降低独立采样冗余。同时避免将推理时不可用的历史建议作为模型输入，消除训练-测试不匹配。论文 2026-11-04 发布，获 34 次 upvote，具体方法细节在材料中未完全展示。

rss · Hugging Face Daily Papers · 11月4日 02:51

**「为什么重要」** coding agent 训练数据质量直接决定模型行为。独立采样策略既浪费计算资源，又因历史建议依赖导致分布偏移，该框架针对这两点提出系统化方案。

**「可关注」** 可关注：轨迹收集阶段的历史利用需与推理阶段信息条件对齐，否则训练数据会引入模型无法依赖的偏差。

**标签**: `#coding-agent`

---

<a id="item-agent-engineer-4"></a>
### [datasette-apps 0.3a0 发布](https://github.com/datasette/datasette-apps/releases/tag/0.3a0) ⭐️ 6.8/10

2026 年 11 月 4 日 simonw 发布 datasette-apps 0.3a0 alpha 版本，核心改进围绕 Datasette Agent 的应用创建与编辑能力，发布内容存在截断迹象。新增聊天输入\#触发已授权应用自动补全打标签功能，新增 app\_add\_stored\_queries、app\_remove\_stored\_queries 两个工具用于管理应用可调用的存储查询，授权写查询需用户先审批；app\_create 现在会校验请求的存储查询是否存在且用户可查看，创建应用前需用户审批写查询。此外，应用查看按钮与\#引用链接现在全屏在 Datasette Agent 面板打开，工具结果新增应用相对路径，该版本要求 Datasette≥1.0a41，支持 Python 3.15、不再支持 Python 3.10。

github · simonw · 11月4日 00:29

**「为什么重要」** 该版本是 Datasette 生态内针对 Agent 工具链的官方 alpha 更新，首次落地权限管控的存储查询管理、写操作审批流与聊天内应用标签能力，但改进范围仅覆盖 Datasette Agent 相关场景，且发布内容存在截断迹象。

**「可关注」** 可关注：该版本将写查询授权与用户审批流程绑定，同时收窄 Python 版本支持范围（仅支持 3.15+，要求 Datasette≥1.0a41），升级时需注意依赖兼容性。

**标签**: `#permissions`, `#orchestration`, `#agent`

---

<a id="item-agent-engineer-5"></a>
### [datasette-agent 0.5a0 发布](https://github.com/datasette/datasette-agent/releases/tag/0.5a0) ⭐️ 6.8/10

2026 年 11 月 3 日，simonw 发布 datasette-agent 0.5a0 版本，该工具属于 Datasette 数据探索生态的 alpha 阶段 AI agent 工具。本次更新新增会话级模型锁定、\# 引用标签（带权限感知的上下文注入）、自定义引用类型插件钩子、Datasette 页面侧边栏渲染、停止按钮、会话后台运行等能力，同时优化了系统提示逻辑、SQL 查询工具功能与 UI 细节。该版本要求 Python 3.11 及以上，最低依赖为 datasette&gt;=1.0a41、datasette-llm&gt;=0.1a9、llm&gt;=0.37.1，仅对使用 Datasette 做数据探索的用户有直接价值。

github · simonw · 11月3日 23:13

**「为什么重要」** 该版本的功能迭代聚焦 Datasette 生态内的 agent 交互体验，其中自定义引用类型的插件钩子设计具备跨场景的可迁移性，适合做 agent 扩展能力的参考。但作为 alpha 阶段的 niche 工具，其功能对通用 AI agent 工程师的直接影响有限，尚未形成大范围验证的行业影响。

**「可关注」** 可关注：自定义引用类型的 register\_agent\_reference\_types\(\) 插件钩子，支持扩展 \# 引用的搜索、上下文注入逻辑，可作为 agent 工具扩展能力的参考实现。

**标签**: `#coding-agent`, `#orchestration`, `#permissions`, `#memory`, `#harness`

---

<a id="item-agent-engineer-6"></a>
### [权重空间编程与 DeepSeek Super-Agent 原型](https://latent.space/p/ainews-llms-can-read-write-neural-network-weights-weight-space-programming-cuts-autoresearch-out-of/) ⭐️ 6.0/10

2026 年 11 月 3 日 AINews 汇总两项 AI Agent 相关进展：一是新研究论文提出“权重空间编程（Weight Space Programming）”能力，支持大模型直接读写更小模型的神经网络权重，可完成权重缺陷修复、单步生成完整网络权重等任务，已有独立复现案例，绕开了此前自动化模型研究需编写 PyTorch/Jax 代码、运行实验监控指标的流程，被视为 0 到 1 突破的新型递归自我改进（RSI）相关能力，目前仅验证于简单游戏与强化学习策略场景，无生产级实现；二是 DeepSeek 开源 super-agent harness 原型仓库\`dsh-superagent-prototype\`，采用长生命周期路由会话对接人类、分发任务给隔离并行 worker 的架构，官方测试显示 p95 任务完成时间较单会话子代理方案从 29.5 分钟降至 15.7 分钟，当前无内置跨会话长期记忆，状态/计算/环境分离、安全隐私、agent 间通信等仍为未实现项。

rss · Latent Space · 11月3日 05:35

**「为什么重要」** 权重空间编程首次验证了大模型直接操作神经网络权重的可行性，为未来 agent 自适配、模型自动化研究、eval 工具提供了新路径，但目前仍处于早期研究阶段，无生产级落地；DeepSeek 开源的 super-agent harness 原型是少有的公开长生命周期多 agent 路由架构实现，其性能数据与未实现项清单可为 coding agent harness 设计提供直接参考。

**「可关注」** 可关注：DeepSeek super-agent 原型明确将跨任务连续性与吞吐量作为核心权衡，其未实现的长期记忆、状态隔离等项可对应到现有 harness 的待补全能力；权重空间编程的独立复现已出现，可跟踪其后续场景扩展进展。

**标签**: `#coding-agent`, `#eval`

---

<a id="item-agent-engineer-7"></a>
### [RoboColosseum 论文提出野外评估框架](https://huggingface.co/papers/2611.02497) ⭐️ 6.0/10

2026-11-04，Hugging Face Daily Papers 介绍 RoboColosseum  preprint。该框架在本地运营的异构机器人网络上，通过统一策略服务与标准化协议，测试视觉-语言-动作策略与前沿 AI agent。研究评估 5 个 VLA 策略与 3 个前沿 agent，横跨 SO-101、Franka、Bimanual-YAM、G1 Humanoid 四种形态，设置 Open Track（blinded pairwise，无任务特定适配）与 Fine-tune Track（20 个任务跨形态适配）两个赛道。当前材料截断，未披露完整技术细节、性能指标或官方代码链接。

rss · Hugging Face Daily Papers · 11月4日 00:00

**「为什么重要」** 它针对具身 AI 测试的可复现性缺口提出标准化方案，但完整技术细节与性能数据尚未公开，实际影响需待全文验证。

**「可关注」** RoboColosseum 的 Open Track 采用 blinded pairwise 设计，Fine-tune Track 覆盖 20 任务与 4 种形态，可参考其赛道划分做对照实验。

**标签**: `#eval`

---

<a id="item-agent-engineer-8"></a>
### [Palette 小模型生成自定义幻灯片](https://huggingface.co/blog/ibm-research/palette-deck-building) ⭐️ 5.8/10

IBM Research 发布 Palette，通过 LoRA 微调 20B 开放权重模型，使其按 IBM Design Language 生成 pptxgenjs 代码构建幻灯片。项目合成约 1000 套 deck、约 10,000 张 slide 的训练数据，并为每步决策附带反事实推理标注。推理阶段引入 harness，先做规则修复，再经几何检查器检测重叠与溢出，最后由编辑器模型重写问题 slide。在 PresentBench 评测中，该方法在三个领域中的两个排名第一。用户可在计划中插入 \[\[directives\]\] 控制布局、语气、受众等设计选择。

rss · Hugging Face Blog · 11月3日 16:35

**「为什么重要」** Frontier 模型生成多 slide deck 时风格固化，且敏感内容无法出域。Palette 证明通过合成数据、双角色分解与 harness 检查，小模型可在保持设计语言所有权的同时接近 frontier 质量。

**「可关注」** 可关注：将复杂生成任务拆成&quot;规划-编码&quot;两阶段，用结构化 brief 隔离 editorial 与 geometry 决策，可降低小模型单次推理负担并支持并行。

**标签**: `#eval`, `#harness`

---

<a id="item-agent-engineer-9"></a>
### [Cognition 发布 2026 年 11 月安全指南](https://cognition.ai/blog/practical-guide-to-security-november-2026) ⭐️ 5.8/10

2026 年 11 月 3 日，Cognition 发布 11 月安全实践指南，汇总了近期多起安全事件，包括 10 月 29 日披露的恶意 Claude Code Cursor 扩展入侵事件：Cursor 指出该扩展版本与 Open VSX registry 上的官方版本存在差异，推测攻击者入侵了 Open VSX 下游的扩展发布流程，该恶意版本试图在开发者机器上安装持久化后门以允许攻击者 SSH 访问，Cursor 报告安装量不足 5000。指南同时提及 Binance 63.4 亿美元被盗、PHP2Shell、GitLab 未授权远程代码执行等漏洞，将安全措施分为即时执行和 30 天内落地两类，但当前公开内容为截断版，缺乏深度技术细节、可复现分析及完整可操作指引。

rss · Cognition Blog · 11月3日 17:00

**「为什么重要」** 已证实的针对编码 Agent 生态（Cursor 扩展、MCP 服务器、本地 AI 代理）的攻击表明相关工具链已是攻击者目标，指南提出的攻击面审计、扩展白名单、密钥脱离开发者机器等措施直接对应这类风险；但当前公开内容为截断版，未提供完整技术验证方法与可复现的分析路径，措施的实际落地效果尚未得到充分验证。

**「可关注」** 可关注：编码 Agent 相关扩展、MCP 服务器的发布流程完整性，以及对文件系统、shell、凭证有访问权限的插件的审计优先级。

**标签**: `#coding-agent`, `#permissions`

---

## AI 日报
{: #sec-ai-daily .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-daily" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-daily-1"></a>
### [思科整合 OpenAI 模型强化企业安全](https://openai.com/index/cisco-cyber) ⭐️ 6.8/10

OpenAI 官方博客 2026 年 11 月 3 日发布行业合作案例，介绍思科将网络情报与 OpenAI 模型结合，用于构建更自适应的企业安全防御体系。该案例未披露具体技术实现、性能数据或落地范围等细节。

rss · OpenAI Blog · 11月3日 08:00

**「可关注」** 可关注：思科结合网络情报与 OpenAI 模型的企业安全防御方案后续公开的技术细节与落地效果。

**标签**: `#industry`, `#product`, `#lab`

---

<a id="item-ai-daily-2"></a>
### [OpenAI 博客：ChatGPT 与 Codex 加速实体工程](https://openai.com/index/accelerating-engineering-for-the-physical-world) ⭐️ 6.3/10

OpenAI 官方博客发布文章，介绍 ChatGPT 与 Codex 正被用于加速 CAD、PCB 设计、仿真等实体工程相关的工作流。该文未提及具体新功能、版本更新或独立产品发布信息。

rss · OpenAI Blog · 11月3日 12:00

**「为什么重要」** 该文是 OpenAI 官方公开的 AI 实体工程落地案例，覆盖设计到仿真的全流程场景，可作为相关领域从业者的参考。

**「可关注」** 可关注：ChatGPT 与 Codex 在 CAD、PCB 设计、仿真等实体工程场景的落地进展。

**标签**: `#model`, `#lab`, `#industry`, `#product`

---

## AI 羊毛
{: #sec-ai-deals .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-deals" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-deals-1"></a>
### [E 宝 13 款小游戏限免 11 月 9 日截止](https://www.appinn.com/eggs-261103/) ⭐️ 9.0/10

你看到的内容可能由第三方 AI 基于小众软件文章提炼总结而成，可能与原文真实意图存在偏差。不代表小众软件观点和立场。请&lt;a href=&quot;https://www.appinn.com/eggs-261103/&quot; target=&quot;\_blank&quot;&gt;点击链接阅读原文&lt;/a&gt;细致比对和校验。&lt;br /&gt;&lt;br /&gt;Epic 商店开启 13 款由 Yash Future Tech Solutions 开发的小游戏限时免费领取活动，领取后游戏永久入库，无消费门槛，截止时间为北京时间 2026 年 11 月 9 日凌晨 2:30，支持网页端操作。

rss · 小众软件 · 11月3日 13:13

**「为什么重要」** 这批免费游戏覆盖赛车、平台跳跃、解谜、数学益智等多品类，领取后永久入库且无需即时下载安装，适合补充轻量休闲游戏库。

**「可关注」** 可关注：网页端领取时若遇“与当前设备不兼容”提示仍可完成入库，操作时需注意区分免费游戏本体与 Demo，确认金额为 0 元后再添加到库。

**标签**: `#free-tier`, `#promo`, `#limited-free`, `#game`

---