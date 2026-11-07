---
layout: default
title: "Horizon Summary: 2026-11-07 (ZH)"
date: 2026-11-07
lang: zh
---

> 从 204 条内容中筛选出 12 条重要资讯。

<nav id="ah-toc" class="ah-toc" aria-label="目录"><span class="ah-toc-title">目录</span><ul><li><a href="#sec-harness-arch"><span class="ah-toc-name">Harness 架构</span><span class="ah-toc-count">3条</span></a></li><li><a href="#sec-agent-engineer"><span class="ah-toc-name">Agent 工程师日报</span><span class="ah-toc-count">5条</span></a></li><li><a href="#sec-ai-daily"><span class="ah-toc-name">AI 日报</span><span class="ah-toc-count">2条</span></a></li><li><a href="#sec-ai-deals"><span class="ah-toc-name">AI 羊毛</span><span class="ah-toc-count">2条</span></a></li></ul></nav>

---

**[Harness 架构](#sec-harness-arch)**
1. [google/adk-python v2.14.0 发布](#item-harness-arch-1) ⭐️ 8.8/10
2. [Agent Framework dotnet-1.28.0 发布](#item-harness-arch-2) ⭐️ 7.8/10
3. [OpenHands v1.37.0 发布](#item-harness-arch-3) ⭐️ 5.8/10

**[Agent 工程师日报](#sec-agent-engineer)**
1. [Harness-S 提升 agent 泛化](#item-agent-engineer-1) ⭐️ 8.0/10
2. [Arete-27B 开源发布](#item-agent-engineer-2) ⭐️ 7.0/10
3. [BestRand 实现稳定低成本基准压缩](#item-agent-engineer-3) ⭐️ 6.0/10
4. [EvoMemState 状态中心记忆框架提出](#item-agent-engineer-4) ⭐️ 6.0/10
5. [VisSearch-Bench 多模态视觉搜索评测基准](#item-agent-engineer-5) ⭐️ 6.0/10

**[AI 日报](#sec-ai-daily)**
1. [OpenAI 与 Hacktron 开展安全测试合作](#item-ai-daily-1) ⭐️ 8.8/10
2. [GitHub 发布 Copilot 智能体工程指南](#item-ai-daily-2) ⭐️ 7.8/10

**[AI 羊毛](#sec-ai-deals)**
1. [本周 Epic 限免 11.6~11.12](#item-ai-deals-1) ⭐️ 8.0/10
2. [Handbrake 免费无追踪驾驶日志上线](#item-ai-deals-2) ⭐️ 6.0/10

---

## Harness 架构
{: #sec-harness-arch .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-harness-arch" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-harness-arch-1"></a>
### [google/adk-python v2.14.0 发布](https://github.com/google/adk-python/releases/tag/v2.14.0) ⭐️ 8.8/10

google/adk-python v2.14.0 将核心运行时、执行环境、A2A 和评估模块从实验性提升至稳定，新增多运行评估（\`adk eval --num\_runs\` 与 \`--parallelism\`）、语义工具参数匹配（\`ToolArgsMatcher\`）以及分块文件流式传输（\`BaseEnvironment.read\_file\_stream\`）。多轮工作流性能提升，30 节点 200 轮运行耗时降低 23%，峰值内存降低 9%。同时新增 Microsoft Teams、OpenAI Decisions 集成及 MongoDB 记忆服务的向量搜索与 TTL 支持。破坏性变更包括：\`Enum\` 工具参数现在以枚举成员形式传递，\`VertexAiSessionService.create\_session\` 仅接受 \`display\_name\`、\`ttl\`、\`expire\_time\` 和 \`labels\` 关键字参数，\`RunSkillScriptTool\` 在环境模式下不再接受 \`command\` 参数。

github · haranrk · 11月7日 00:58

**「设计要点」** 核心运行时与执行环境稳定化，\`BaseEnvironment.read\_file\_stream\` 采用分块流式传输避免大文件全量加载，\`ContainerCodeExecutor\` 与 \`RunSkillScriptTool\` 改为基于验证路径和参数的执行模型。评测层引入 \`MultiRunConfig\` 并发多跑与 \`ToolArgsMatcher\` 多策略匹配，记忆层通过 \`MongoDbMemoryService\` 支持向量检索与 TTL 过期。

**「改了什么」** 相对 v2.13.0，v2.14.0 将执行环境、A2A、评估和核心运行时模块从实验性转为稳定，新增多运行评估、语义工具参数匹配、分块文件流式传输、Microsoft Teams 与 OpenAI Decisions 集成，以及 MongoDB 记忆服务的向量搜索与 TTL。同时优化长多轮工作流性能（30 节点 200 轮快 23%、内存低 9%），并引入三项破坏性变更：\`Enum\` 工具参数改为枚举成员传递、\`VertexAiSessionService.create\_session\` 限制关键字参数、\`RunSkillScriptTool\` 移除 \`command\` 参数。

**标签**: `#runtime`, `#sandbox`, `#a2a`, `#eval`, `#tools`

---

<a id="item-harness-arch-2"></a>
### [Agent Framework dotnet-1.28.0 发布](https://github.com/microsoft/agent-framework/releases/tag/dotnet-1.28.0) ⭐️ 7.8/10

Microsoft Agent Framework 发布 dotnet-1.28.0。本次更新覆盖 .NET 与 Python 双运行时，核心变更包括 MCP 协议支持并发调用且携带请求级 headers、收紧未作用域 URL session 的审批权限、修复 .NET 声明式工作流公式的 InvariantCulture 解析，以及为 Python 3.15 启用 Redis 集成。版本同时包含多项 \[BREAKING\] 变更，涉及 A2A agent 创建简化、MCP 会话按调用作用域隔离、声明式 MCP 会话作用域调整，以及 .NET 侧强制要求配置允许的 HTTP 主机。

github · dmytrostruk · 11月6日 22:00

**「设计要点」** 框架采用多语言运行时设计，.NET 与 Python 侧共享 MCP 协议层与会话管理抽象。权限模型通过 invocation-scoped 作用域隔离收紧 MCP 客户端与 URL session 的访问边界，工作流引擎在 .NET 侧采用 InvariantCulture 保证公式解析的跨文化一致性。

**「改了什么」** MCP 协议层新增并发调用能力，请求可携带独立 headers；Python 侧未作用域 URL session 的自动审批权限被收紧；.NET 工作流公式解析修复为使用 InvariantCulture；Python 3.15 获得 Redis 集成支持。多项 \[BREAKING\] 变更落地，包括 .NET 强制配置 allowed HTTP hosts、A2A agent 创建与 payload 处理简化、MCP 客户端与会话按调用作用域隔离。

**标签**: `#mcp`, `#permissions`, `#runtime`, `#tools`

---

<a id="item-harness-arch-3"></a>
### [OpenHands v1.37.0 发布](https://github.com/OpenHands/OpenHands/releases/tag/v1.37.0) ⭐️ 5.8/10

OpenHands 发布 v1.37.0。本次更新为自动化流程新增 Mermaid 图表可视化功能。聊天模块优化历史扫描逻辑，提升实时更新性能。同时修复会话恢复、标题显示、首页路径等 UI 问题。

github · openhands-release-bot\[bot\] · 11月6日 12:54

**「改了什么」** 自动化流程新增 Mermaid 图表解释。聊天历史实时更新避免重复扫描以提升性能，同时修复恢复会话排序、标题可见性、空建议等待及首页 trailing slash 等 UI 问题。

**标签**: `#runtime`, `#tools`

---

## Agent 工程师日报
{: #sec-agent-engineer .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-agent-engineer" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-agent-engineer-1"></a>
### [Harness-S 提升 agent 泛化](https://huggingface.co/papers/2611.04277) ⭐️ 8.0/10

2026-11-07 Hugging Face Daily Papers 收录论文 2611.04277，提出 Harness-S。该方法通过 Directional Harness Evolution 构建可重用的 Sibling Harness Pool，并在 Complementary Harness Rescue Training 中仅在基础 harness 所有初始尝试失败时调用该池，将救援能力迁移到单一策略。论文指出 harness 从共同基础演化表现出 Locality、Complementarity 和 Nonstationarity，即不同变体修复不同失败，且效用随策略学习变化。目标策略在原始 harness 下仍保持有效。该方法面向 coding agent 与 harness 开发者，标签：harness、coding-agent、orchestration。

rss · Hugging Face Daily Papers · 11月7日 02:30

**「为什么重要」** 该论文提供了与 agent harness 及训练系统设计直接相关的具体技术组件，但尚未证实其在实际 harness 工程中的落地效果或性能增益。

**「可关注」** 可关注：Harness-S 将 sibling harness 的救援能力迁移到单一策略，且救援池在策略训练期间保持固定，这为 harness 设计与策略训练的解耦提供了可验证路径。

**标签**: `#harness`, `#coding-agent`, `#orchestration`

---

<a id="item-agent-engineer-2"></a>
### [Arete-27B 开源发布](https://www.reddit.com/r/LocalLLaMA/comments/1xpmj33/nousresearcharete27b_hugging_face_qwen_finetune/) ⭐️ 7.0/10

2026 年 11 月 6 日，NousResearch 发布开源 Arete-27B 模型，基于阿里巴巴 Qwen3.8-27B 做监督微调（SFT），未使用强化学习、偏好优化或架构修改，训练上下文长度为 64k，仅使用文本数据。模型方自评估显示，事实得分从 2.32/5 提升至 2.98/5，含宣传内容的回答占比从 22%降至 0.9%，7 个价值类别均有所改善，通用能力与智能体基准无显著回退。目前 Hugging Face 已提供该模型的 GGUF 版本供本地使用，但评估数据为模型方自报告，相关博客链接已失效，未经过独立第三方验证，模型定位为面向需要调整价值倾向的通用辅助、智能体工作及价值对齐研究场景。

reddit · r/LocalLLaMA · /u/jacek2023 · 11月6日 19:58

**「为什么重要」** 它给需要特定价值倾向的本地智能体部署提供了新的开源基座选项，也展示了仅通过 SFT 调整大模型价值倾向的可行性；但所有性能指标均为 NousResearch 自报告，尚未得到独立第三方验证。

**「可关注」** 可关注：仅通过监督微调（无强化学习、偏好优化、架构修改）调整 27B 级模型价值倾向，且未造成通用与智能体基准显著回退的结论，需要社区独立复现验证。

**标签**: `#eval`, `#coding-agent`

---

<a id="item-agent-engineer-3"></a>
### [BestRand 实现稳定低成本基准压缩](https://huggingface.co/papers/2611.00883) ⭐️ 6.0/10

2026-11-07，Hugging Face Daily Papers 介绍论文《Random Is Almost Enough? Stable and Low-Cost Benchmark Compression via BestRand》。该论文提出 BestRand 方法，旨在解决随机采样选择评估子集时的长尾不稳定性问题。研究推导出从子集估计全基准分数的误差分布解析近似，证明大多数子集误差小但少数产生大误差，形成长尾分布；随机采样虽能以高概率取得好效果，但罕见大误差导致不稳定。该不稳定性被证明是现代基础模型固有特性，且随评估模型数量增加仍持续存在。论文内容在材料中截断，未披露 BestRand 具体技术实现与性能对比数据。

rss · Hugging Face Daily Papers · 11月7日 02:30

**「为什么重要」** 该研究揭示了随机采样在基准压缩中的固有局限，为评估工作流提供了理论依据。若 BestRand 经复现验证有效，可降低 AI Agent 评估的样本量与计算成本。

**「可关注」** 可关注：随机采样在基准压缩中虽能以高概率接近全基准结果，但长尾大误差导致结果不稳定，且该现象在现代基础模型上具有固有性。

**标签**: `#eval`

---

<a id="item-agent-engineer-4"></a>
### [EvoMemState 状态中心记忆框架提出](https://huggingface.co/papers/2611.03743) ⭐️ 6.0/10

2026-11-07，Hugging Face Daily Papers 介绍论文《EvoMemState: Evolving Memory State for Personal Agents》。该研究针对 LLM 个人智能体长期记忆，提出状态中心（state-centric）框架 EvoMemState。框架在持久事实基础上增加两类状态：关系状态（Relational States）捕获事实随记忆演化的有效性及相互关系；推理状态（Reasoning State）决定事实应用方式。传统事实中心（fact-centric）记忆将记忆视为独立事实，可能忽略新事实对旧事实的更新、约束或冲突关系。当前提供内容为截断摘要，无完整技术细节、性能数据或实现资源。

rss · Hugging Face Daily Papers · 11月7日 02:30

**「为什么重要」** 该框架代表 LLM 智能体长期记忆从事实存储向状态建模的转向，可能影响个人智能体记忆系统的设计思路。但具体性能提升与实现成本尚未证实。

**「可关注」** 传统事实中心记忆将事实视为独立单元，EvoMemState 通过关系状态显式建模事实间的动态约束与演化，这为长期记忆系统的状态更新机制提供了新参考。

**标签**: `#memory`

---

<a id="item-agent-engineer-5"></a>
### [VisSearch-Bench 多模态视觉搜索评测基准](https://huggingface.co/papers/2611.04894) ⭐️ 6.0/10

2026 年 11 月 7 日 Hugging Face Daily Papers 汇总了 arXiv 论文 2611.04894 提出的 VisSearch-Bench 评测基准，用于评估多模态智能体的长程视觉搜索与跨步骤视觉上下文管理能力，该日报条目获得 17 次用户点赞。该基准包含 204 个人工编写的任务，覆盖 7 大领域、25 个子领域，涵盖集合式视觉搜索、序列式视觉搜索、混合宽深搜索、竞争性视觉消歧四类任务类型，对多模态智能体能力评测与迭代工作有参考价值。当前仅公开二次聚合的截断摘要，无基准访问方式、完整技术细节或落地使用信息，需查阅全文获取可落地内容，影响面目前较窄。

rss · Hugging Face Daily Papers · 11月7日 02:30

**「为什么重要」** 该基准针对现有多模态智能体评测缺少跨图像、跨步骤视觉信息关联评估维度的空白设计，若后续公开完整测试集与评分规则，可成为相关能力迭代的参考标尺，但目前该影响尚未证实。

**「可关注」** 可关注：当前多模态智能体视觉能力评测普遍未覆盖跨图像、跨步骤的视觉信息关联评估，VisSearch-Bench 的任务设计可作为相关能力补全的参考。

**标签**: `#eval`, `#memory`, `#multimodal-agent`

---

## AI 日报
{: #sec-ai-daily .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-daily" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-daily-1"></a>
### [OpenAI 与 Hacktron 开展安全测试合作](https://openai.com/index/partnering-with-hacktron) ⭐️ 8.8/10

OpenAI 官方宣布与安全厂商 Hacktron 达成合作，将开展系统漏洞扫描、第三方服务连接验证工作，同时借助前沿 AI 技术强化自身安全防御体系。本次合作暂未公开披露测试时间表与具体覆盖范围细节。

rss · OpenAI Blog · 11月6日 08:00

**「为什么重要」** 这是头部 AI 实验室首次公开披露与专业安全厂商开展系统性漏洞测试合作，测试范围覆盖第三方服务连接，对 AI 系统安全防护的落地实践有参考价值。

**「可关注」** 可关注：头部 AI 厂商将前沿 AI 能力纳入安全防御体系的落地实践。

**标签**: `#lab`, `#policy`, `#industry`

---

<a id="item-ai-daily-2"></a>
### [GitHub 发布 Copilot 智能体工程指南](https://github.blog/ai-and-ml/github-copilot/beyond-code-generation-a-developers-guide-to-agentic-engineering/) ⭐️ 7.8/10

GitHub 官方博客发布面向 Copilot 用户的智能体工程开发者指南，提出从单一代码生成转向覆盖软件全生命周期的端到端智能体工作流。指南引用的数据显示，2026 年 10 月单周 GitHub 提交量达 12 亿次，同比提升超 400%，超过 2025 年全年提交总量；Faros AI 研究显示高 AI 采用率团队的 PR 审查时长上升了 441%。指南围绕 Plan、Build、Verify、Observe 四个阶段，给出了 Copilot 对应的功能用法，包括跨设备会话续接、云沙箱运行任务、共享记忆复用项目知识等。

rss · GitHub Blog · 11月6日 22:15

**「为什么重要」** 当前 AI 编码普及已带来提交量暴涨但 PR 审查效率下滑的新瓶颈，该指南是 GitHub 官方给出的面向全开发流程的智能体工程实操方案，配套最新行业 adoption 数据，对做 coding agent 的开发者有参考价值。

**「可关注」** 可关注：Copilot 已支持会话跨设备续接、云沙箱异步运行任务、共享记忆复用项目知识，可覆盖 Plan 到 Observe 的全开发流程智能体工作流。

**标签**: `#product`, `#industry`

---

## AI 羊毛
{: #sec-ai-deals .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-deals" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-deals-1"></a>
### [本周 Epic 限免 11.6~11.12](https://www.appinn.com/eggs-261106/) ⭐️ 8.0/10

你看到的内容可能由第三方 AI 基于小众软件文章提炼总结而成，可能与原文真实意图存在偏差。不代表小众软件观点和立场。请点击链接阅读原文细致比对和校验。

本周（11.6~11.12）Epic 平台开展限时免费福利活动，电脑端可免费领取《浮游世界/Flotsam》，移动端可免费领取锁区的《巴别塔圣歌/Chants of Sennaar》；《遗忘国度：放置勇士/Idle Champions of the Forgotten Realms》本体长期免费，此前曾免费提供过，本周登录 Epic 版可领取限时 Morte’s Renown Pack 礼包，内含 Morte 等 5 名角色、每名角色 32 个白金宝箱、药水及专属魔宠，需进入游戏内领取，活动截止时间为 11 月 12 日。

rss · 小众软件 · 11月6日 08:21

**「为什么重要」** 三款游戏在 Steam 平台均获得玩家正面评价，其中《浮游世界》支持简体中文、《巴别塔圣歌》支持繁体中文，且均为近年上线的新作，限免窗口期短，值得优先领取。

**「可关注」** 可关注：《巴别塔圣歌》移动端领取存在区域锁限制，需提前确认 Epic 账号所在区域是否在可领取范围内；《遗忘国度：放置勇士》限时礼包仅需登录 Epic 版本游戏即可领取，无额外付费门槛。

**标签**: `#promo`, `#limited-free`, `#game`

---

<a id="item-ai-deals-2"></a>
### [Handbrake 免费无追踪驾驶日志上线](https://apps.apple.com/us/app/handbrake-driving-log/id6822426461) ⭐️ 6.0/10

开发者 hcabral 在 Hacker News 分享自研的 iOS 驾驶日志应用 Handbrake，完全免费、无广告无追踪，所有驾驶数据存储于用户个人 iCloud 账户，iOS 用户可直接免费下载使用，无明确失效时间与付费限制说明。

rss · HN Free API / Credits · 11月6日 23:02

**「为什么重要」** 当前面向普通用户的免费无广告驾驶日志工具供给较少，Handbrake 的隐私优先设计可避免用户驾驶数据被第三方获取，适合有驾驶记录或新手学车需求的 iOS 用户。

**「可关注」** 可关注：该应用仅适配 iOS 平台，数据存储完全依赖用户 iCloud，无公开的付费或广告规划说明。

**标签**: `#free-tier`, `#limited-free`

---