---
layout: default
title: "Horizon Summary: 2026-11-04 (EN)"
date: 2026-11-04
lang: en
---

> From 194 items, 15 important content pieces were selected

---

**Agent Harness Architecture**
1. [FastMCP v4.2.0a3 发布](#item-harness-arch-1) ⭐️ 7.8/10
2. [Cloudflare Agents 0.33.0 发布](#item-harness-arch-2) ⭐️ 7.8/10
3. [openai-agents-js v0.22.0-alpha.1 发布](#item-harness-arch-3) ⭐️ 6.8/10

**AI Agent Engineer**
1. [StateBench 发布 长文档状态追踪基准](#item-agent-engineer-1) ⭐️ 7.8/10
2. [CUA-Master 嵌套双循环框架提出](#item-agent-engineer-2) ⭐️ 7.0/10
3. [SWE-Trail 历史引导轨迹收集框架发布](#item-agent-engineer-3) ⭐️ 7.0/10
4. [Datasette-apps 0.3a0 发布](#item-agent-engineer-4) ⭐️ 6.8/10
5. [Datasette-agent 0.5a0 发布](#item-agent-engineer-5) ⭐️ 6.8/10
6. [LLM 读写权重与 DeepSeek 代理](#item-agent-engineer-6) ⭐️ 6.0/10
7. [RoboColosseum 提出具身 AI 评估框架](#item-agent-engineer-7) ⭐️ 6.0/10
8. [IBM Palette 小模型幻灯片生成](#item-agent-engineer-8) ⭐️ 5.8/10
9. [Cognition 发布 11 月安全实践指南](#item-agent-engineer-9) ⭐️ 5.8/10

**AI Daily**
1. [思科结合OpenAI模型强化企业安全](#item-ai-daily-1) ⭐️ 6.8/10
2. [OpenAI 博客：Codex 加速物理工程](#item-ai-daily-2) ⭐️ 6.3/10

**AI Deals**
1. [Epic 13款小游戏限免 11月9日截止](#item-ai-deals-1) ⭐️ 9.0/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [FastMCP v4.2.0a3 发布](https://github.com/PrefectHQ/fastmcp/releases/tag/v4.2.0a3) ⭐️ 7.8/10

FastMCP 发布 v4.2.0a3 alpha 预发布版本，整合实验性 skills 子系统，将 \`Skill\` 改为存储中性对象并引入严格目录加载验证。新增 \`SkillsDirectoryProvider\`，弃用 4.1 版 skills 提供者并计划 4.3 移除。修复代理发现缓存过期、OpenAPI Schema 引用与显式 null 值保留、客户端连接恢复等运行时问题。skills 功能仍处实验阶段，面向集成测试。

github · zzstoatzz · Nov 3, 23:39

**「设计要点」** Skills 子系统以存储中性的 \`Skill\` 对象为核心，目录加载时逐项验证后发布；\`experimental\_skills=True\` 重定向到新提供者并拒绝子类以保留访问控制。客户端通过 \`client.read\_skill\(\)\` 下载并校验完整 skill，资源型服务器通过 \`skill://&lt;name&gt;/\_manifest\` 读取清单元数据。

**「改了什么」** 相对 a2，\`Skill\` 变为存储中性对象，新增严格 \`SkillsDirectoryProvider\`、\`ClientGroup\` 技能发现、\`Client.read\_skill\(\)\` 接口及 \`--skills\` CLI 参数。修复 OpenAPI 工具输入 omit \`readOnly\` 属性、OAuth 同意绑定并发保持、异常中间件匹配子类等问题，同时将 4.1 skills API 标记为弃用。

**「评论」** 无可用社区评论。

**Tags**: `#mcp`, `#tools`, `#runtime`

---

<a id="item-harness-arch-2"></a>
### [Cloudflare Agents 0.33.0 发布](https://github.com/cloudflare/agents/releases/tag/agents%400.33.0) ⭐️ 7.8/10

Cloudflare Agents 0.33.0 upgrades the Pi harness to Pi 1.5, introducing batched storage writes that cut SQLite transactions by about 27x and CPU by approximately 25%. The scheduler eliminates per-commit conversation rechecks and batches concurrent commits into single storage calls, raising throughput from 88 to 459 agent runs per second with 2048 sessions. New APIs include \`session.watch\(\)\` for live conversation views, \`session.continue\(\)\` for resuming runs after model errors or turn limits, and \`defaults.maxTurns\` to cap tool rounds. Streaming large answers now appends text instead of copying it, preventing heap spikes above 100 MB, though a crash can lose up to roughly one second of streamed output.

github · github-actions\[bot\] · Nov 3, 13:14

**「设计要点」** The Pi harness batches streamed answers and tool output at 1-second intervals rather than on every update, and appends text instead of copying it to reduce heap usage. The scheduler removes per-commit conversation rechecks and batches concurrent commits into single storage calls, while crash-looping tasks now end with an error result or \`restart\_limit\` reason instead of parking.

**「改了什么」** Pi 1.5 support replaces \`session.events\(\)\` with \`session.watch\(\)\` and adds \`session.entries\(\)\` for paging, while \`session.continue\(\)\` resumes runs without new messages and \`submit\(\)\` gains \`whenIdle: &quot;reject&quot;\`. \`retry\(\)\` and the \`parked\` status are removed, Pi tool schemas now require \`@earendil-works/pi-schema\` instead of TypeBox exports from \`pi-ai\`, and browser tools gain \`Browser.functionDocs\(\)\`, scope locks, and \`conversationScope\(\)\`.

**Tags**: `#runtime`, `#memory`

---

<a id="item-harness-arch-3"></a>
### [openai-agents-js v0.22.0-alpha.1 发布](https://github.com/openai/openai-agents-js/releases/tag/v0.22.0-alpha.1) ⭐️ 6.8/10

OpenAI 发布 openai-agents-js v0.22.0-alpha.1，这是其 JavaScript 与 TypeScript Agents SDK 的官方 alpha 版本。该版本引入嵌入式 Codex harness 支持，用于 agent 开发。发布包要求 Node.js 24 及其自带 npm，提供 Linux x64、macOS Apple silicon 与 Windows x64 三套 starter 压缩包及对应 SHA-256 校验和。部署时需设置 OPENAI\_API\_KEY，执行 npm ci --ignore-scripts，再运行 node hello.mjs 启动示例，示例会发起一次在线模型请求并打印问候语。

github · markstuart-oai · Nov 3, 15:36

**「改了什么」** 本次 alpha 在 openai-agents-js SDK 中新增嵌入式 Codex harness 支持，覆盖 JavaScript 与 TypeScript 场景。发布物包含三平台预构建 starter 压缩包及校验和文件，配套示例程序可执行在线模型调用。

**Tags**: `#runtime`, `#subagents`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [StateBench 发布 长文档状态追踪基准](https://allenai.org/blog/statebench) ⭐️ 7.8/10

Allen AI 于 2026-11-03 发布 StateBench，一个含四个难度层级的基准，用于评估大语言模型在长文档中追踪实体状态变化的能力。四个层级分别为 R-trivial（不可变赋值）、Aperiodic（按值重赋值）、Soluble（自引用更新）和 General finite（按引用赋值），对应 Krohn–Rhodes 理论中的不同复杂度类别。测试基线包括 Olmo 3（Transformer）、Olmo Hybrid 及 2.75 亿、2.7B 与 7B 参数模型，这些模型训练时未见超过 64,000 token 的上下文。结果显示，预训练模型在 R-trivial 上表现良好，但在 General finite 上准确率降至随机水平；前沿模型 Gemini 3.8 Flash、Claude Opus 5.5、GPT-6 Sol 与 Luna 在最长 General finite 问题上准确率降至 13% 以下。定向训练的循环与混合架构（如 Gated DeltaNet）在长序列状态追踪上显著优于 Transformer。

rss · Allen AI · Nov 3, 08:00

**「为什么重要」** 状态追踪是长运行 AI Agent 的核心能力，StateBench 提供了可对比的难度梯度来诊断架构瓶颈。定向训练结果直接表明，Transformer 在硬状态追踪任务上的局限可通过架构选择缓解，这对 Agent 评估设计、模型选型和记忆系统开发有直接影响。尚未证实的是，这些实验室结果能否迁移到真实 Agent 工作流中。

**「可关注」** 在构建需要跨长上下文追踪实体状态的 Agent 时，除常规上下文长度测试外，应补充 StateBench 的 Soluble 与 General finite 难度评估，因为现有预训练 Transformer 与前沿 API 模型在这些层级上存在显著性能断崖。

**Tags**: `#eval`, `#memory`

---

<a id="item-agent-engineer-2"></a>
### [CUA-Master 嵌套双循环框架提出](https://huggingface.co/papers/2611.03126) ⭐️ 7.0/10

2026-11-04，Hugging Face Daily Papers 推送论文 CUA-Master（arXiv:2611.03126），提出嵌套双循环递归改进框架，用于扩展 computer-use agents。该框架外层为世界-数据-模型飞轮，持续纳入开放世界语料并利用模型弱点指导数据构建与优化迭代；内层耦合开放世界播种与自催化传播。论文指出现有 CUA 开发受限于交互数据多样性、可控性与可靠性不足，且传统优化 pipeline 缺乏迭代反馈，自生成经验改进方法已现回报递减。该工作与 coding-agent、orchestration、eval 标签相关，但摘要被截断，具体实验设计与效果未披露。

rss · Hugging Face Daily Papers · Nov 4, 02:51

**「为什么重要」** 论文直指 CUA 规模化开发的核心瓶颈——数据与反馈机制，提出的双循环结构试图从开放世界语料和模型自身弱点两端同时撬动改进。这为 agent 工程师提供了除自生成经验之外的另一条优化思路，但框架实际效果与可复现性仍有待完整论文验证。

**「可关注」** 可关注：现有基于自生成经验的 CUA 改进已出现回报递减，新框架尝试通过开放世界语料挖掘与模型弱点分析构建外循环，可能改变数据飞轮的构建方式。

**Tags**: `#coding-agent`, `#orchestration`, `#eval`

---

<a id="item-agent-engineer-3"></a>
### [SWE-Trail 历史引导轨迹收集框架发布](https://huggingface.co/papers/2611.02074) ⭐️ 7.0/10

2026-11-04，Hugging Face Daily Papers 收录论文《SWE-Trail: History-Guided Trajectory Collection for Coding Agent Training》（arXiv:2611.02074）。该论文提出历史引导的轨迹收集框架，针对 coding agent 训练中独立多轨迹采样导致的冗余问题，以及因在训练中引入推理时不可用的历史建议而产生的 train-test mismatch。论文主张利用历史轨迹指导后续收集，而非将其作为模型输入，但具体实现细节未在提供的摘要中完全展示。主要影响 coding agent 训练数据管道的构建者。

rss · Hugging Face Daily Papers · Nov 4, 02:51

**「为什么重要」** 当前 coding agent 训练普遍采用独立多轨迹采样，该框架直接针对这一主流范式的效率与泛化缺陷。论文指出的 train-test mismatch 问题在现有 pipeline 中客观存在，但解决方案的实际效果与采纳成本尚未有广泛验证。

**「可关注」** 可关注：在构建 coding agent 训练数据收集 pipeline 时，需区分「利用历史轨迹指导采样策略」与「将历史信息作为模型输入」两种做法，后者可能引入推理时不可用的依赖。

**Tags**: `#coding-agent`

---

<a id="item-agent-engineer-4"></a>
### [Datasette-apps 0.3a0 发布](https://github.com/datasette/datasette-apps/releases/tag/0.3a0) ⭐️ 6.8/10

2026年11月4日，simonw 发布 Datasette-apps 0.3a0 官方alpha版本，核心优化Datasette Agent的应用创建与管理能力。新增聊天内输入\`\#\`自动补全有权限的应用 tagging 能力；新增\`app\_add\_stored\_queries\(\)\`、\`app\_remove\_stored\_queries\(\)\`两个工具，支持agent管理应用可调用的存储查询，授予写查询需用户先审批；\`app\_create\(\)\`现在会校验请求的存储查询是否存在、用户是否有查看权限，创建应用前需用户审批写查询。UI层面，应用工具结果新增相对路径字段，agent可直接生成应用链接，查看应用按钮与\`\#\`引用链接现在会在Datasette Agent面板全屏打开应用。该版本要求Datasette 1.0a41及以上，新增支持Python 3.15，停止支持Python 3.10。

github · simonw · Nov 4, 00:29

**「为什么重要」** 这是Datasette Agent生态的官方alpha迭代，首次将存储查询的细粒度权限管控、写操作审批流和聊天内应用 tagging 能力落地到agent工具链，但当前改进仅覆盖Datasette 生态内的应用创建与管理场景，且发布内容存在截断迹象，未涉及通用agent工作流。

**「可关注」** 可关注：Datasette Agent 的工具调用已开始将存储查询权限管控与写操作用户审批耦合，这类权限-审批联动的工具设计模式可参考。

**Tags**: `#permissions`, `#orchestration`, `#agent`

---

<a id="item-agent-engineer-5"></a>
### [Datasette-agent 0.5a0 发布](https://github.com/datasette/datasette-agent/releases/tag/0.5a0) ⭐️ 6.8/10

simonw 于 2026-11-03 发布 datasette-agent 0.5a0（alpha 版本），新增会话级模型锁定、\# 标签权限感知上下文注入、自定义引用类型插件钩子、Datasette 页面侧边栏渲染、停止按钮、会话后台运行、系统提示优化、SQL 查询工具增强等特性；该版本最低要求 Python 3.11，支持 Python 3.15，依赖版本为 datasette&gt;=1.0a41、datasette-llm&gt;=0.1a9、llm&gt;=0.37.1，面向 Datasette 数据探索生态的用户与开发者。

github · simonw · Nov 3, 23:13

**「为什么重要」** 该版本深化了 agent 与 Datasette 数据资产的交互能力，其中自定义引用类型的插件钩子设计可复用到其他 agent 的上下文扩展场景；但 datasette-agent 仍属 niche 的 alpha 阶段工具，对通用 AI agent 工程师的直接影响尚未证实。

**「可关注」** 可关注：其 \`register\_agent\_reference\_types\(\)\` 插件钩子将自定义引用类型的搜索、上下文注入能力开放给插件，是 agent 上下文扩展的一种可参考实现。

**Tags**: `#coding-agent`, `#orchestration`, `#permissions`, `#memory`, `#harness`

---

<a id="item-agent-engineer-6"></a>
### [LLM 读写权重与 DeepSeek 代理](https://latent.space/p/ainews-llms-can-read-write-neural-network-weights-weight-space-programming-cuts-autoresearch-out-of/) ⭐️ 6.0/10

2026-11-03 的 AI 新闻汇总两项研究进展。论文 &quot;Weight Space Programming&quot; 展示大模型可直接读写小模型权重，实现单步修复 bug、50 步内定向优化，甚至从零写出完整网络权重并超越部分独立训练模型；但目前仅验证于简单游戏和强化学习策略，尚未证明可扩展至更复杂任务。DeepSeek 开源 \`dsh-superagent-prototype\` 代理 harness，采用长生命周期路由器会话加隔离 worker 架构，自称 p95 完成时间从 29.5 分钟降至 15.7 分钟；但跨会话长期记忆、状态/计算/环境分离、安全隐私及 agent 间通信仍为未解决问题。

rss · Latent Space · Nov 3, 05:35

**「为什么重要」** 权重空间编程将模型操作从代码层推进到参数层，若可扩展，可能改变代理自优化和评估工具链的构建方式。DeepSeek harness 的并行 worker 架构针对代理任务吞吐量提出具体优化路径，但两者均处于原型阶段，缺乏生产环境验证。

**「可关注」** 可关注：权重空间编程世界首次实现 LLM 直接读写权重，但材料明确其当前仅适用于简单游戏和强化学习策略，尚未验证在通用编码任务中的有效性。

**Tags**: `#coding-agent`, `#eval`

---

<a id="item-agent-engineer-7"></a>
### [RoboColosseum 提出具身 AI 评估框架](https://huggingface.co/papers/2611.02497) ⭐️ 6.0/10

2026-11-04，Hugging Face Daily Papers 介绍预印本 RoboColosseum，提出分布式 in-the-wild 评估框架，用于标准化测试视觉-语言-动作（VLA）机器人大模型与前沿 AI agent。该框架在多样环境本地运营的机器人网络上提供统一策略服务与标准化协议，初始研究评估 5 个 VLA 策略与 3 个前沿 agent，跨 SO-101、Franka、Bimanual-YAM、G1 Humanoid 四种本体。Open Track 在匹配本地条件下以 blinded、pairwise 方式比较无任务特定适配的模型；Fine-tune Track 测量 VLA 策略在 20 个任务上跨四种本体的适应能力。当前材料文本截断，未提供完整技术细节、性能指标或代码链接。

rss · Hugging Face Daily Papers · Nov 4, 00:00

**「为什么重要」** 该框架试图解决具身 AI 测试的可复现性缺口，通过标准化协议与分布式真实机器人网络，可能缩小实验室到真实世界的评估差距。但框架的实际可复现性提升、成本效益与社区采纳效果尚未证实，需等待完整论文与代码发布。

**「可关注」** 可关注：RoboColosseum 的 Open Track 采用 blinded pairwise 设计与匹配本地条件，为跨本体 VLA 策略比较提供了可复用的协议模板，但需等待完整论文验证其标准化程度与执行开销。

**Tags**: `#eval`

---

<a id="item-agent-engineer-8"></a>
### [IBM Palette 小模型幻灯片生成](https://huggingface.co/blog/ibm-research/palette-deck-building) ⭐️ 5.8/10

IBM Research 发布 Palette 项目，通过 LoRA 微调 20B 开放权重模型，使其能按 IBM Design Language 生成 pptxgenjs 代码绘制幻灯片。项目将工作分为设计师与编码器两个角色：设计师输出包含调色板、字体系统和每页布局的结构化 JSON 简报，编码器并行生成各页代码，再由 harness 检查渲染错误并修复。训练数据约 1000 套幻灯片（约 10,000 页），采用反事实推理标注设计决策，模型在 PresentBench 三个领域中的两个排名第一。用户可在计划中插入 \[\[directive\]\] 指令控制布局、语气等设计选择。

rss · Hugging Face Blog · Nov 3, 16:35

**「为什么重要」** 该项目验证了通过合成数据与 harness 检查训练小模型，可在保持设计语言所有权的同时接近前沿系统效果。对需要本地部署、数据不出域的团队而言，这提供了一条可复现的评测与训练路径。但当前仅展示 PresentBench 部分领域结果，尚未证实泛化到其他设计语言或更大规模部署的稳定性。

**「可关注」** 小模型生成结构化代码时，将编辑判断与几何计算拆分为两个阶段，并在推理时加入渲染检查与自动修复，可降低布局错误率。

**Tags**: `#eval`, `#harness`

---

<a id="item-agent-engineer-9"></a>
### [Cognition 发布 11 月安全实践指南](https://cognition.ai/blog/practical-guide-to-security-november-2026) ⭐️ 5.8/10

Cognition 于 2026-11-03 发布 11 月安全实践指南，汇总近两周多起重大安全事件。指南提到，攻击者通过伪造面试和篡改安装程序入侵 Binance 工程师笔记本，进而窃取 63.4 亿美元；10 月 29 日 Cursor 披露 Claude Code 扩展遭投毒，恶意版本试图在开发者机器上安装持久化后门并开启 SSH 访问，安装量低于 5,000，且该版本与 Open VSX registry 上的版本不一致，提示扩展发布流程下游可能被篡改。此外，PHP2Shell、GitLab 远程代码执行、KVM 逃逸、Linux 多路径 TCP 栈 CVE-2026-98432 等漏洞也被列出。文章给出立即执行和 30 天内完成的安全加固建议，但所提供摘录为截断版，缺乏技术深度、可复现分析或超出高层评论的可操作指导。

rss · Cognition Blog · Nov 3, 17:00

**「为什么重要」** 开发环境依赖的编辑器扩展、MCP 服务器与本地 AI agent 若遭投毒，即可继承开发者全部权限。该指南将 Claude Code 扩展事件与 Binance 黑客案并列，强调基础攻击面依然有效，但攻击紧迫性已提升；然而摘录仅提供高层评论，未给出技术根因或验证方法。

**「可关注」** 编辑器扩展的自动更新机制与发布流程下游被篡改的风险，以及开发机上的 MCP 服务器、本地 AI agent 等第三方组件可能继承开发者全部权限。

**Tags**: `#coding-agent`, `#permissions`

---

## AI Daily

<a id="item-ai-daily-1"></a>
### [思科结合OpenAI模型强化企业安全](https://openai.com/index/cisco-cyber) ⭐️ 6.8/10

OpenAI官方博客2026年11月3日发布行业合作案例，介绍思科将网络情报与OpenAI模型结合，用于构建更自适应的企业安全防御体系。该案例未披露具体技术实现细节与性能对比数据。

rss · OpenAI Blog · Nov 3, 08:00

**「为什么重要」** 该案例呈现了生成式AI在企业安全防御场景的落地实践，为同类安全产品的技术迭代提供了可参考的行业方向。

**「可关注」** 可关注：网络情报与大模型结合构建自适应安全防御的落地路径。

**Tags**: `#industry`, `#product`, `#lab`

---

<a id="item-ai-daily-2"></a>
### [OpenAI 博客：Codex 加速物理工程](https://openai.com/index/accelerating-engineering-for-the-physical-world) ⭐️ 6.3/10

OpenAI 官方博客发布文章，介绍 ChatGPT 与 Codex 在物理工程领域的应用。文章展示这两款工具如何帮助工程师加速 CAD、PCB 设计、仿真等工作流。本次发布未涉及具体新功能、版本更新或产品公告。

rss · OpenAI Blog · Nov 3, 12:00

**「可关注」** ChatGPT 与 Codex 正被用于加速 CAD、PCB 设计、仿真等物理工程工作流。

**Tags**: `#model`, `#lab`, `#industry`, `#product`

---

## AI Deals

<a id="item-ai-deals-1"></a>
### [Epic 13款小游戏限免 11月9日截止](https://www.appinn.com/eggs-261103/) ⭐️ 9.0/10

你看到的内容可能由第三方 AI 基于小众软件文章提炼总结而成，可能与原文真实意图存在偏差。不代表小众软件观点和立场。请&lt;a href=&quot;https://www.appinn.com/eggs-261103/&quot; target=&quot;\_blank&quot;&gt;点击链接阅读原文&lt;/a&gt;细致比对和校验。&lt;br /&gt;&lt;br /&gt;Epic 商店开启 13 款 Yash Future Tech Solutions 出品的小游戏限时免费领取活动，领取后永久入库，截止时间为北京时间 2026 年 11 月 9 日凌晨 2:30。用户登录 Epic 账户进入对应游戏页面，点击获取确认金额为 0 元后即可入库，无需立即下载安装。

rss · 小众软件 · Nov 3, 13:13

**「为什么重要」** 这批游戏均为永久入库资格，错过本次限免后后续大概率需付费获取，且截止时间临近，剩余领取窗口不足一周。

**「可关注」** 可关注：网页版领取时若遇到「与当前设备不兼容」提示仍可继续完成入库，下载安装操作可后续再进行。

**Tags**: `#free-tier`, `#promo`, `#limited-free`, `#game`

---