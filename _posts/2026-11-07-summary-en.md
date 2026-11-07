---
layout: default
title: "Horizon Summary: 2026-11-07 (EN)"
date: 2026-11-07
lang: en
---

> From 204 items, 12 important content pieces were selected

---

**Agent Harness Architecture**
1. [google/adk-python v2.14.0 发布](#item-harness-arch-1) ⭐️ 8.8/10
2. [Agent Framework dotnet-1.28.0 发布](#item-harness-arch-2) ⭐️ 7.8/10
3. [OpenHands v1.37.0 发布](#item-harness-arch-3) ⭐️ 5.8/10

**AI Agent Engineer**
1. [Harness-S: Sibling Harness Pool for Agent Training](#item-agent-engineer-1) ⭐️ 8.0/10
2. [Arete-27B 开源发布 基于Qwen3.8-27B微调](#item-agent-engineer-2) ⭐️ 7.0/10
3. [BestRand 实现稳定低成本基准压缩](#item-agent-engineer-3) ⭐️ 6.0/10
4. [EvoMemState 状态中心记忆框架](#item-agent-engineer-4) ⭐️ 6.0/10
5. [VisSearch-Bench 多模态视觉搜索评测基准发布](#item-agent-engineer-5) ⭐️ 6.0/10

**AI Daily**
1. [OpenAI 与 Hacktron 合作开展系统漏洞测试](#item-ai-daily-1) ⭐️ 8.8/10
2. [GitHub Copilot 智能体工程指南发布](#item-ai-daily-2) ⭐️ 7.8/10

**AI Deals**
1. [Epic 11.6-11.12 限免游戏汇总](#item-ai-deals-1) ⭐️ 8.0/10
2. [Handbrake 免费iOS驾驶日志上线](#item-ai-deals-2) ⭐️ 6.0/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [google/adk-python v2.14.0 发布](https://github.com/google/adk-python/releases/tag/v2.14.0) ⭐️ 8.8/10

google/adk-python v2.14.0 正式发布。本次将核心运行时、执行环境、A2A 和评估模块从实验性转为稳定 API，新增多轮评估并行执行（\`adk eval --num\_runs\` 配合 \`--parallelism\`）、语义工具参数匹配（\`ToolArgsMatcher\`）、沙箱工具分块文件流式读取，以及 Microsoft Teams、OpenAI Decisions 和 MongoDB 记忆服务集成。长多轮工作流性能优化后，30 节点 200 轮场景耗时降低 23%、峰值内存降低 9%。包含枚举工具参数传递方式、Vertex AI 会话服务配置限制和 \`RunSkillScriptTool\` 命令参数的破坏性变更。

github · haranrk · Nov 7, 00:58

**「设计要点」** 核心运行时与执行环境抽象层稳定化，\`BaseEnvironment\` 提供跨本地与远程沙箱的分块文件流式读取。长多轮工作流通过内部状态管理优化，在 30 节点 200 轮场景下耗时降低 23%、峰值内存降低 9%。

**「改了什么」** 相对 v2.13.0，v2.14.0 将执行环境、A2A、评估和核心运行时模块从实验性转为稳定，新增多轮评估并行执行、语义工具参数匹配、分块文件流式读取，以及 Microsoft Teams 和 OpenAI Decisions 集成。同时调整枚举工具参数传递行为、Vertex AI 会话服务配置限制和 RunSkillScriptTool 命令参数，构成破坏性变更。

**Tags**: `#runtime`, `#sandbox`, `#a2a`, `#eval`, `#tools`

---

<a id="item-harness-arch-2"></a>
### [Agent Framework dotnet-1.28.0 发布](https://github.com/microsoft/agent-framework/releases/tag/dotnet-1.28.0) ⭐️ 7.8/10

Microsoft Agent Framework dotnet-1.28.0 发布。本次更新核心包括 MCP 协议并发调用支持、URL 会话权限收紧、.NET 工作流公式解析修复，以及 Python 3.15 Redis 集成。同时引入多项 BREAKING 变更，涉及 MCP 会话作用域、A2A 代理创建简化及 HTTP 主机限制，升级时需评估兼容性。

github · dmytrostruk · Nov 6, 22:00

**「设计要点」** MCP 客户端和会话默认按调用作用域，减少跨请求状态泄漏；.NET Foundry Hosting 启用源生成日志；内存状态文件不可读时隔离处理而非直接失败。

**「改了什么」** Python 端新增 MCP 并发调用支持，请求携带独立 headers；收紧未作用域 URL 会话的自动审批范围；修复 .NET 声明式工作流公式解析的 InvariantCulture 问题；新增 Python 3.15 Redis 集成。同时引入多项 BREAKING 变更：声明式 MCP 会话按调用作用域、A2A 代理创建与负载处理简化、要求配置允许的 HTTP 主机、工作流 MCP 客户端按调用作用域、AG-UI 工作流代理执行器绑定单一授权作用域、MCP 目录发现行为强化。

**Tags**: `#mcp`, `#permissions`, `#runtime`, `#tools`

---

<a id="item-harness-arch-3"></a>
### [OpenHands v1.37.0 发布](https://github.com/OpenHands/OpenHands/releases/tag/v1.37.0) ⭐️ 5.8/10

OpenHands v1.37.0 于 2026-11-06 发布，属于小版本迭代。automation 模块新增 Mermaid 图可视化能力，可解释自动化流程。chat 模块优化 live 历史更新性能，避免重复扫描；同时修复会话恢复、标题显示、空建议加载和首页路径问题。发布说明未提供实现细节、代码路径或架构解释。

github · openhands-release-bot\[bot\] · Nov 6, 12:54

**「改了什么」** 相对 v1.36.0，automation 增加 Mermaid 图解释功能，chat 历史 live 更新避免重复扫描；同时修复 resumed session 排序、conversation title 启动可见性、replay 前空建议及 base path 首页加载。依赖升级 lucide-react 至 1.64.0、driver.js 至 1.10.2、@types/node 至 26.6.6。

**Tags**: `#runtime`, `#tools`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [Harness-S: Sibling Harness Pool for Agent Training](https://huggingface.co/papers/2611.04277) ⭐️ 8.0/10

The Hugging Face Daily Papers feed \(2026-11-07\) highlights the paper &quot;Harness-S: Learning from Sibling Harnesses for Generalizable Agent Training&quot; \(arXiv:2611.04277, 55 upvotes\). The authors identify three properties of harness evolution from a common base: Locality, Complementarity, and Nonstationarity—variants repair different failure types, and their utility shifts as the policy learns. Harness-S maintains a reusable Sibling Harness Pool of specialized harnesses developed along distinct repair directions via Directional Harness Evolution. During training, Complementary Harness Rescue Training invokes this pool only when all initial attempts under the base harness fail, then transfers the rescued capabilities into a single policy that remains effective under the original harness. The pool stays fixed throughout policy training.

rss · Hugging Face Daily Papers · Nov 7, 02:30

**「Why It Matters」** The work provides a concrete architecture for failure-specific rescue in agent training systems, directly relevant to coding agent harness design. The Nonstationarity finding—that harness utility changes during learning—challenges static harness selection and implies training pipelines must account for evolving environment-policy interactions.

**「Engineer Takeaway」** The fixed Sibling Harness Pool during policy training enforces a separation between environment diversification and policy optimization, which may simplify the engineering of distributed training pipelines for coding agents.

**Tags**: `#harness`, `#coding-agent`, `#orchestration`

---

<a id="item-agent-engineer-2"></a>
### [Arete-27B 开源发布 基于Qwen3.8-27B微调](https://www.reddit.com/r/LocalLLaMA/comments/1xpmj33/nousresearcharete27b_hugging_face_qwen_finetune/) ⭐️ 7.0/10

2026年11月6日，NousResearch发布开源Arete-27B模型，该模型基于Alibaba Qwen3.8-27B做监督微调（SFT）后训练，针对原模型在政治敏感话题的回避、CCP框架回答等问题调整价值对齐，面向需要对应价值偏好的通用辅助和智能体场景，同时支持研究用途。发布方自评显示，模型事实得分从2.32/5提升至2.98/5，含宣传内容的回答占比从22%降至0.9%，7个价值类别均有提升，通用能力与智能体基准无显著回退。训练仅使用SFT，未采用强化学习、偏好优化或架构修改，提供GGUF格式供本地部署；博客中的评估链接已失效，所有指标均为发布方自评，未经过独立验证。

reddit · r/LocalLLaMA · /u/jacek2023 · Nov 6, 19:58

**「为什么重要」** 这是目前公开少数针对Qwen系列完成西方价值对齐调整的开源27B模型，为需要调整模型价值偏好的本地智能体部署提供了可选基座。但其对齐效果、基准表现及价值调整的普适性仍需社区独立验证，尚未形成共识。

**「可关注」** 可关注：Arete-27B仅通过SFT实现价值对齐调整，未使用RL或架构修改，若自评指标属实，可作为轻量价值对齐的参考实现。

**Tags**: `#eval`, `#coding-agent`

---

<a id="item-agent-engineer-3"></a>
### [BestRand 实现稳定低成本基准压缩](https://huggingface.co/papers/2611.00883) ⭐️ 6.0/10

2026-11-07，Hugging Face Daily Papers 分享论文 2611.00883，提出 BestRand 方法。该方法针对随机采样选择评估子集时的长尾不稳定性问题，通过分析误差分布发现大多数子集误差小但少数产生大误差，导致随机采样虽成本低却不稳定。BestRand 旨在提供稳定且低成本的基准压缩方案，但摘要未披露具体实现细节、性能对比数据或使用指南，完整信息需查阅原文。该研究对 AI Agent 工程师的模型评估工作流有潜在价值。

rss · Hugging Face Daily Papers · Nov 7, 02:30

**「为什么重要」** 基准压缩直接影响模型评估的时间与成本。BestRand 若验证有效，可为 agent 评估提供更可靠的子集选择策略，减少随机采样带来的结果波动，但具体效果仍需原文确认。

**「可关注」** 随机采样在基准压缩中存在固有长尾不稳定性，BestRand 提供稳定替代方案，但具体实现与效果需参考论文 2611.00883。

**Tags**: `#eval`

---

<a id="item-agent-engineer-4"></a>
### [EvoMemState 状态中心记忆框架](https://huggingface.co/papers/2611.03743) ⭐️ 6.0/10

2026 年 11 月 7 日发布的研究提出 EvoMemState 状态中心记忆框架，通过引入关系状态与推理状态优化 LLM 个人智能体的长期记忆能力。该框架将记忆从独立事实升级为动态状态，显式建模新事实对旧事实的更新、约束与冲突关系。材料未提供完整技术细节、性能数据或实现资源。

rss · Hugging Face Daily Papers · Nov 7, 02:30

**「为什么重要」** 该框架将记忆表示从静态事实转向动态状态，可能改变个人智能体的记忆管理方式。但材料未提供实验数据或落地资源，实际效果待验证。

**「可关注」** 可关注：传统事实中心记忆忽略事实间的动态约束与优先级，EvoMemState 通过关系状态和推理状态显式建模这些维度。

**Tags**: `#memory`

---

<a id="item-agent-engineer-5"></a>
### [VisSearch-Bench 多模态视觉搜索评测基准发布](https://huggingface.co/papers/2611.04894) ⭐️ 6.0/10

2026年11月7日Hugging Face Daily Papers汇总了arXiv论文2611.04894提出的VisSearch-Bench评测基准，该基准用于评估多模态智能体的长程视觉搜索与跨步骤视觉上下文管理能力，包含204个人工编写的7大领域、25个子领域任务，覆盖集合式视觉搜索、序列视觉搜索等任务类型。当前公开信息仅为二次聚合的截断摘要，无基准访问方式、完整技术细节或落地使用信息，需查阅全文才能获取可落地内容，影响面目前较窄，主要面向多模态智能体评测研究者。

rss · Hugging Face Daily Papers · Nov 7, 02:30

**「为什么重要」** 该基准针对现有智能体评测在跨图像、跨步骤视觉信息关联能力评估上的空白设计，对多模态智能体评测工作有参考价值；但具体基准可用性、实际评测效果等尚未证实，需查阅全文确认。

**「可关注」** 可关注：当前多数多模态智能体视觉搜索任务仅用图像识别初始实体后转向文本检索，对跨图像、跨步骤的视觉上下文关联能力评估覆盖不足，VisSearch-Bench针对该空白设计。

**Tags**: `#eval`, `#memory`, `#multimodal-agent`

---

## AI Daily

<a id="item-ai-daily-1"></a>
### [OpenAI 与 Hacktron 合作开展系统漏洞测试](https://openai.com/index/partnering-with-hacktron) ⭐️ 8.8/10

OpenAI 官方宣布与安全厂商 Hacktron 达成合作，将开展系统漏洞扫描、第三方服务连接测试两项核心工作，同时借助前沿 AI 技术强化自身安全防御能力。本次合作暂无公开的测试范围、时间周期及漏洞披露细则。

rss · OpenAI Blog · Nov 6, 08:00

**「为什么重要」** 这是 OpenAI 首次公开披露与外部安全厂商开展系统性漏洞测试合作，直接指向前沿 AI 系统的供应链安全与防御能力建设，对行业安全实践有参考意义。

**「可关注」** 可关注：第三方安全厂商参与前沿 AI 系统漏洞测试的协作模式与披露边界。

**Tags**: `#lab`, `#policy`, `#industry`

---

<a id="item-ai-daily-2"></a>
### [GitHub Copilot 智能体工程指南发布](https://github.blog/ai-and-ml/github-copilot/beyond-code-generation-a-developers-guide-to-agentic-engineering/) ⭐️ 7.8/10

GitHub 官方博客发布面向 Copilot 用户的智能体工程开发者指南。文章称 2026 年 10 月单周 GitHub 提交量达 12 亿次，同比增长超 400%，超过 2025 全年总量；Faros AI 研究显示高 AI 采用团队的 PR 审查时长上升 441%。指南建议将工作流从独立代码生成扩展至 Plan、Build、Verify、Observe 全阶段，以缓解 AI 加速实现后出现的审查与运维瓶颈。文中未对引用的统计数据提供第三方验证。

rss · GitHub Blog · Nov 6, 22:15

**「为什么重要」** 这标志着 GitHub 将 Copilot 定位从代码补全工具推向全生命周期智能体协作，同时用 adoption 与审查效率的负相关数据，为团队重新评估 AI 工作流提供参考。

**「可关注」** 可关注：Copilot 云沙箱与会话连续性允许任务在关闭本机后继续执行，并在多客户端间恢复同一会话。

**Tags**: `#product`, `#industry`

---

## AI Deals

<a id="item-ai-deals-1"></a>
### [Epic 11.6-11.12 限免游戏汇总](https://www.appinn.com/eggs-261106/) ⭐️ 8.0/10

你看到的内容可能由第三方 AI 基于小众软件文章提炼总结而成，可能与原文真实意图存在偏差。不代表小众软件观点和立场。请点击链接阅读原文细致比对和校验。

本周（11.6-11.12）Epic平台开展限时免费福利活动：电脑端可免费领取支持中文的《浮游世界/Flotsam》；移动端可免费领取锁区的《巴别塔圣歌/Chants of Sennaar》Android及iOS版本，该作Epic页面列有繁体中文支持；《遗忘国度：放置勇士/Idle Champions of the Forgotten Realms》本体长期免费，电脑版不支持中文，本周登录Epic版本可领取限时Morte’s Renown Pack礼包，内含5名角色、每名角色32个白金宝箱、药水及专属魔宠，礼包需在游戏内领取。活动周期为11月6日至11月12日，具体截止时间以Epic平台页面为准。

rss · 小众软件 · Nov 6, 08:21

**「为什么重要」** 三款游戏在Steam均获得玩家正向评价，《巴别塔圣歌》好评率97%，《浮游世界》好评率88%，偏好对应品类的玩家可零成本体验。

**「可关注」** 可关注：《巴别塔圣歌》移动端锁区，领取前需确认Epic账号所在区域是否在支持范围内；《遗忘国度：放置勇士》本体长期免费，可常驻持有，本次限时礼包需登录Epic版游戏内领取。

**Tags**: `#promo`, `#limited-free`, `#game`

---

<a id="item-ai-deals-2"></a>
### [Handbrake 免费iOS驾驶日志上线](https://apps.apple.com/us/app/handbrake-driving-log/id6822426461) ⭐️ 6.0/10

HN用户hcabral分享免费iOS驾驶日志应用Handbrake，该应用由开发者受家中孩子开始开车的启发制作，无广告、无追踪、无分析工具，所有数据存储于用户个人iCloud账号，iOS用户可直接免费下载使用，材料未提及付费限制与失效时间。

rss · HN Free API / Credits · Nov 6, 23:02

**「为什么重要」** 该应用完全由用户掌控数据所有权，无第三方数据采集与广告干扰，同时支持加速、刹车、地图等驾驶数据记录，适配注重隐私的iOS驾驶者需求。

**「可关注」** 可关注：该应用仅适配iOS平台，数据存储依赖用户iCloud账号，无安卓版本及本地存储选项。

**Tags**: `#free-tier`, `#limited-free`

---