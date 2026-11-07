---
layout: default
title: "Horizon Summary: 2026-11-07 (EN)"
date: 2026-11-07
lang: en
---

> From 180 items, 12 important content pieces were selected

---

**Agent Harness Architecture**
1. [google/adk-python v2.14.0 发布](#item-harness-arch-1) ⭐️ 8.8/10
2. [OpenHands v1.37.0 发布](#item-harness-arch-2) ⭐️ 6.3/10
3. [Agent Framework .NET 1.28.0 发布](#item-harness-arch-3) ⭐️ 5.8/10

**AI Agent Engineer**
1. [Harness-S 通用智能体训练框架](#item-agent-engineer-1) ⭐️ 7.0/10
2. [Drex 非自回归决策模型发布](#item-agent-engineer-2) ⭐️ 7.0/10
3. [ChatGPT 工具调用跨 Connector 静默路由](#item-agent-engineer-3) ⭐️ 6.0/10
4. [BestRand 稳定低开销基准压缩](#item-agent-engineer-4) ⭐️ 6.0/10
5. [VisSearch-Bench 多模态视觉搜索基准发布](#item-agent-engineer-5) ⭐️ 6.0/10
6. [Arete-27B Qwen3 微调版发布](#item-agent-engineer-6) ⭐️ 6.0/10

**AI Daily**
1. [OpenAI 与 Hacktron 安全合作](#item-ai-daily-1) ⭐️ 7.8/10
2. [GitHub 发布智能体工程开发指南](#item-ai-daily-2) ⭐️ 6.8/10

**AI Deals**
1. [Epic 11.6~11.12 免费游戏福利](#item-ai-deals-1) ⭐️ 8.0/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [google/adk-python v2.14.0 发布](https://github.com/google/adk-python/releases/tag/v2.14.0) ⭐️ 8.8/10

google/adk-python v2.14.0 将核心运行时、沙箱执行环境、A2A 协议支持和评测模块从实验性标记毕业为稳定。新增分块文件流式读取（BaseEnvironment.read\_file\_stream）、多轮次并发评测（MultiRunConfig、--parallelism）和语义化工具参数匹配（ToolArgsMatcher）。集成新增 Microsoft Teams（TeamsRunner）和 OpenAI Decisions（OpenAIDecisionsClassifier）支持，长多轮工作流性能提升 23% 且峰值内存降低 9%。

github · haranrk · Nov 7, 00:58

**「设计要点」** 运行时层通过 BaseEnvironment 抽象统一 Local、E2B、Daytona 和 AgentEngine 沙箱，文件工具采用分块流式传输避免全量加载内存。评测框架支持运行时构建的 BaseNode 或 App 作为输入，并通过 --eval\_storage\_uri 将评测文件外置存储。

**「改了什么」** 相对 v2.13.0，核心模块全面去实验标记，新增分块文件流、多轮次并发评测、语义工具参数匹配、Teams 与 OpenAI Decisions 集成。同时引入三项破坏性变更：Enum 工具参数以成员对象而非原始字符串传入、VertexAiSessionService.create\_session 仅接受有限会话配置键、RunSkillScriptTool 在环境模式下不再接受 command 参数。

**Tags**: `#runtime`, `#sandbox`, `#a2a`, `#eval`, `#tools`

---

<a id="item-harness-arch-2"></a>
### [OpenHands v1.37.0 发布](https://github.com/OpenHands/OpenHands/releases/tag/v1.37.0) ⭐️ 6.3/10

OpenHands v1.37.0 released 2026-11-06. Minor release adding Mermaid diagram visualization for automations, optimizing chat history scan performance, and fixing session management issues. Changes focus on UI/UX refinements without architectural modifications.

github · openhands-release-bot\[bot\] · Nov 6, 12:54

**「改了什么」** Added Mermaid diagram generation for automation explanations. Fixed chat session resume ordering, conversation title visibility during handoff, empty suggestion timing, and base path routing. Optimized live update performance by eliminating redundant history scans. Updated dependencies including lucide-react and driver.js.

**Tags**: `#chat`, `#session-management`, `#performance`, `#automations`, `#memory`

---

<a id="item-harness-arch-3"></a>
### [Agent Framework .NET 1.28.0 发布](https://github.com/microsoft/agent-framework/releases/tag/dotnet-1.28.0) ⭐️ 5.8/10

Microsoft Agent Framework .NET v1.28.0 is a minor maintenance release. The .NET runtime fix addresses declarative workflow formula parsing using InvariantCulture. Python-side updates include support for concurrent MCP calls with request-owned headers, narrowed unscoped URL session approval rules, and Redis integration for Python 3.15. The release also bundles numerous spelling fixes, test corrections, dependency bumps, and several breaking changes across both SDKs.

github · dmytrostruk · Nov 6, 22:00

**「改了什么」** \- .NET: Parse declarative workflow formulas and values with InvariantCulture.
\- Python: Allow concurrent MCP calls with request-owned headers.
\- Python: Narrow unscoped URL session approvals.
\- Python: Enable Redis integration on Python 3.15.
\- Breaking changes: Python scopes declarative MCP sessions, AG-UI workflow agent executors, and MCP catalog discovery to a single authorization scope; .NET simplifies A2A agent creation and payload handling, requires allowed HTTP hosts, and scopes workflow MCP clients to invocations; Python migrates Foundry Local integration to SDK 2.3.1.
\- Other fixes: Quarantine unreadable memory state files instead of failing, fix empty local shell calls leaving orphaned history, preserve AG-UI citations through client and agent streaming, and add Foundry toolbox token scope configuration.

**Tags**: `#runtime`, `#mcp`, `#permissions`, `#memory`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [Harness-S 通用智能体训练框架](https://huggingface.co/papers/2611.04277) ⭐️ 7.0/10

Hugging Face Daily Papers 于 2026-11-07 介绍 Harness-S 通用智能体训练框架。论文提出 harness 演化具有局部性（locality）、互补性（complementarity）和非平稳性（nonstationarity）三个属性。Harness-S 通过 Directional Harness Evolution 构建固定的 Sibling Harness Pool，并在 Complementary Harness Rescue Training 中仅在基础 harness 所有初始尝试失败时调用该池，将 rescue 能力迁移到单一策略。该框架直接针对 AI agent 的 harness 设计与训练工作流。

rss · Hugging Face Daily Papers · Nov 7, 03:13

**「为什么重要」** 该研究系统识别了 harness 演化的三个关键属性，为 agent 训练中的 harness 设计提供理论框架。Harness-S 通过复用 sibling harness 池而非追求单一最优 harness，可能降低多 harness 维护成本并提升策略鲁棒性，但论文结论尚未经大规模工业场景验证。

**「可关注」** 可关注：Harness-S 将 sibling harness 池固定并在 base harness 全失败时才 rescue 的设计，暗示 agent 训练中「失败触发迁移」可能比「并行尝试所有 harness」更高效，但需验证 rescue 调用频率对训练吞吐量的实际影响。

**Tags**: `#harness`

---

<a id="item-agent-engineer-2"></a>
### [Drex 非自回归决策模型发布](https://huggingface.co/papers/2611.07854) ⭐️ 7.0/10

Hugging Face Daily Papers 于 2026-11-07 介绍 Drex，一个开源的决策模型家族，包含 8B（DLM）、9B（v1.5）、35B（3B 激活，v2.0）和 27B（Max）四个版本。该模型采用非自回归架构，原生接受 agent context（可含图像）作为输入，直接输出选项的概率分布，旨在替代用于 agent 决策步骤的自回归 LLM。论文称自回归 LLM 在生产中存在输出不一致、需解析输出、成本与延迟较高等问题。现有材料未提供性能基准、详细架构拆解、训练数据或许可证信息。

rss · Hugging Face Daily Papers · Nov 7, 03:13

**「为什么重要」** Drex 针对 agent 决策环节的工程痛点提供非自回归替代方案。若在实际 harness 中验证有效，可能简化 coding agent 的决策链路。但目前缺乏性能对比数据，生产可行性尚未证实。

**「可关注」** 非自回归架构将 agent context 直接映射到选项概率分布，理论上可消除传统 LLM 决策步骤中的输出解析环节，但需验证其在不同工具调用场景下的准确率与延迟表现。

**Tags**: `#coding-agent`, `#harness`, `#eval`

---

<a id="item-agent-engineer-3"></a>
### [ChatGPT 工具调用跨 Connector 静默路由](https://community.openai.com/t/security-follow-up-tool-call-silently-routed-to-a-different-connector/1413053) ⭐️ 6.0/10

2026年11月6日Hacker News讨论OpenAI社区安全帖，指出ChatGPT可静默将工具调用路由到不同connector；评论者澄清该行为是OpenAI与MCP系统的预期表现，因二者未对独立工具调用做作用域或绑定限制；同时提及OpenAI漏洞赏金计划现已要求所有提交者完成身份验证。该讨论涉及MCP、OpenAI工具调用集成及安全研究相关从业者，原帖完整技术细节未在本次讨论中披露。

hackernews · Aldipower · Nov 6, 22:50 · [Discussion](https://news.ycombinator.com/item?id=50399569)

**「为什么重要」** 该路由行为暴露了OpenAI与MCP系统在工具调用作用域上的设计限制，对依赖工具调用隔离的agent架构设计有直接参考价值；同时赏金计划身份验证要求的调整，改变了安全研究者的准入门槛。

**「可关注」** 若集成OpenAI或MCP工具调用，需明确当前系统无原生工具调用作用域绑定能力，无法保证不同工具调用的执行上下文隔离。

**「评论」** 社区共识认为该路由行为是OpenAI与MCP系统的设计限制而非异常，此前普遍高估了二者的工具调用作用域保证；同时有评论澄清赏金计划ID验证要求是Bugcrowd平台为降低低质量提交推出的统一规则，并非针对特定地区的制裁合规要求。

**Tags**: `#mcp`, `#orchestration`, `#permissions`

---

<a id="item-agent-engineer-4"></a>
### [BestRand 稳定低开销基准压缩](https://huggingface.co/papers/2611.00883) ⭐️ 6.0/10

2026-11-07，Hugging Face Daily Papers 收录论文《Random Is Almost Enough? Stable and Low-Cost Benchmark Compression via BestRand》（获 50 个 upvote）。该论文提出 BestRand 基准压缩方法，通过解析近似子集评估误差分布，解释纯随机采样虽多数情况误差小但存在长尾大误差的不稳定性。研究表明该不稳定性在现代基础模型中固有存在，且不随评估模型数量增加而消失。当前材料内容截断，未披露具体压缩率、精度对比及实现细节，完整方案需查阅原论文。

rss · Hugging Face Daily Papers · Nov 7, 03:13

**「为什么重要」** 该工作为模型评估的成本-稳定性权衡提供了理论解释，对需要频繁运行 eval 的 agent 工程师有直接参考价值。但材料未给出实际压缩比例与误差 bound 的量化关系，其实用效果仍需原论文数据验证。

**「可关注」** 可关注：误差分布的长尾特性提示随机采样子集存在不可忽视的失败概率，BestRand 的稳定机制或可纳入现有 eval harness 的 subset 选择流程，但需原论文确认实现开销与精度增益。

**Tags**: `#eval`

---

<a id="item-agent-engineer-5"></a>
### [VisSearch-Bench 多模态视觉搜索基准发布](https://huggingface.co/papers/2611.04894) ⭐️ 6.0/10

Hugging Face Daily Papers 于 2026-11-07 分享 VisSearch-Bench 摘要。该基准包含 204 个人工编写任务，覆盖 7 个领域与 25 个子领域，评估多模态 Agent 的长程视觉搜索与跨模态视觉上下文管理能力。摘要内容在 &quot;Competitive Visual Disambigu&quot; 处截断，未披露完整任务类型、技术实现、性能基线或数据集可用性。

rss · Hugging Face Daily Papers · Nov 7, 03:13

**「为什么重要」** 现有视觉搜索任务多通过图像识别初始实体后转向文本检索，难以评估 Agent 跨图像、对象与搜索步骤关联信息的能力。VisSearch-Bench 强调视觉上下文管理，试图填补该评估空白。但完整任务集、难度分布与公开访问方式尚未确认。

**「可关注」** 可关注：视觉上下文管理被明确为评估维度，后续需跟踪其是否引入空间关系、局部细节等需要跨步保持视觉信息的任务设计。

**Tags**: `#eval`, `#memory`

---

<a id="item-agent-engineer-6"></a>
### [Arete-27B Qwen3 微调版发布](https://www.reddit.com/r/LocalLLaMA/comments/1xpmj33/nousresearcharete27b_hugging_face_qwen_finetune/) ⭐️ 6.0/10

NousResearch 发布 Arete-27B，基于 Qwen3 27B 的 SFT 微调版本，已在 Hugging Face 以 GGUF 格式提供（bartowski/NousResearch\_Arete-27B-GGUF）。官方自评显示，事实性得分从 2.32/5 提升至 2.98/5，宣传类回答从 22% 降至 0.9%，七个价值类别均有改善，且通用与 agentic 基准无显著回退。训练仅使用 SFT，未采用 RL、偏好优化或架构修改，上下文长度 64k。该模型面向需要调整政治敏感话题立场的通用辅助与 agentic 工作场景，但博客评估链接已失效，数据为单方面自评，缺乏第三方验证。

reddit · r/LocalLLaMA · /u/jacek2023 · Nov 6, 19:58

**「为什么重要」** 这代表一次明确的价值对齐后训练实践：在 27B 规模上仅通过 SFT 调整模型立场，同时声称保持 agentic 能力。但自评指标、失效的博客链接以及 Reddit 二手来源的性质，使结论仍需官方材料交叉验证。

**「可关注」** 27B 模型通过纯 SFT 实现价值倾向调整并声称保持 agentic 基准，但自评数据与失效博客链接导致可复现性存疑，部署前需独立验证。

**Tags**: `#coding-agent`, `#eval`

---

## AI Daily

<a id="item-ai-daily-1"></a>
### [OpenAI 与 Hacktron 安全合作](https://openai.com/index/partnering-with-hacktron) ⭐️ 7.8/10

OpenAI 官方宣布与安全厂商 Hacktron 建立合作。合作核心目标包括挖掘系统漏洞、测试与第三方服务的连接安全性，最终用于强化前沿 AI 系统的防御能力。

rss · OpenAI Blog · Nov 6, 08:00

**「为什么重要」** 前沿 AI 系统的安全风险是行业长期关注的重点，此次公开合作是头部实验室主动披露安全加固动作的案例，可参考其安全运营思路。

**「可关注」** 可关注：OpenAI 将第三方服务连接测试纳入安全合作范围，提示相关集成方需同步关注接口安全风险。

**Tags**: `#lab`, `#industry`, `#policy`

---

<a id="item-ai-daily-2"></a>
### [GitHub 发布智能体工程开发指南](https://github.blog/ai-and-ml/github-copilot/beyond-code-generation-a-developers-guide-to-agentic-engineering/) ⭐️ 6.8/10

GitHub Blog 发布面向开发者的智能体工程指南，梳理了 Plan、Build、Verify、Observe 四阶段的工作流。文中提到 2026 年 10 月 GitHub 单周提交量达 12 亿次，同比提升 400%，超过 2025 年全年提交总量；同时引用 Faros AI 研究称，团队 AI 采用率从低到高时，PR 平均审查时长上涨 441%。指南还介绍了 Copilot 在规划、跨设备会话、云沙箱运行、企业策略同步等场景的能力。

rss · GitHub Blog · Nov 6, 22:15

**「为什么重要」** 该指南是 GitHub 官方输出的智能体工程实践参考，既给出了 AI 编码普及下的真实效率数据，也提供了可落地的四阶段工作流方案，对做 coding agent 相关开发的工程师有直接参考价值。

**「可关注」** 可关注：高 AI 采用率下 PR 审查时长显著上升的问题，以及指南中提出的 Plan、Build、Verify、Observe 四阶段智能体工程工作流设计。

**Tags**: `#lab`, `#industry`, `#product`

---

## AI Deals

<a id="item-ai-deals-1"></a>
### [Epic 11.6~11.12 免费游戏福利](https://www.appinn.com/eggs-261106/) ⭐️ 8.0/10

你看到的内容可能由第三方 AI 基于小众软件文章提炼总结而成，可能与原文真实意图存在偏差。不代表小众软件观点和立场。请&lt;a href=&quot;https://www.appinn.com/eggs-261106/&quot; target=&quot;\_blank&quot;&gt;点击链接阅读原文&lt;/a&gt;细致比对和校验。&lt;br /&gt;&lt;br /&gt;本周Epic平台11月6日至12日开放3项游戏福利：电脑端可免费领取支持中文的《浮游世界/Flotsam》，手机端可免费领取《巴别塔圣歌/Chants of Sennaar》的Android与iOS版本（该版本锁区，Epic页面列有繁体中文支持）；《遗忘国度：放置勇士/Idle Champions of the Forgotten Realms》本体全平台长期免费，活动期间登录Epic版本可领取限时Morte’s Renown Pack礼包，内含5名角色、每名角色32个白金宝箱、药水及专属魔宠，礼包需在游戏内领取。

rss · 小众软件 · Nov 6, 08:21

**「可关注」** 可关注：《巴别塔圣歌》Epic手机版存在锁区限制，领取前需确认账号所在区域是否开放；《遗忘国度：放置勇士》的限时礼包需启动Epic版本游戏后于游戏内领取，其本体在电脑端和手机端均长期免费，该游戏此前曾在Epic免费提供过本体，电脑版不支持中文。

**Tags**: `#limited-free`, `#promo`, `#game`

---