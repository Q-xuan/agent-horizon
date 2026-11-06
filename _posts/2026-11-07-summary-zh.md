---
layout: default
title: "Horizon Summary: 2026-11-07 (ZH)"
date: 2026-11-07
lang: zh
---

> 从 195 条内容中筛选出 15 条重要资讯。

<nav id="ah-toc" class="ah-toc" aria-label="目录"><span class="ah-toc-title">目录</span><ul><li><a href="#sec-harness-arch"><span class="ah-toc-name">Harness 架构</span><span class="ah-toc-count">4条</span></a></li><li><a href="#sec-agent-engineer"><span class="ah-toc-name">Agent 工程师日报</span><span class="ah-toc-count">5条</span></a></li><li><a href="#sec-ai-daily"><span class="ah-toc-name">AI 日报</span><span class="ah-toc-count">5条</span></a></li><li><a href="#sec-ai-deals"><span class="ah-toc-name">AI 羊毛</span><span class="ah-toc-count">1条</span></a></li></ul></nav>

---

**[Harness 架构](#sec-harness-arch)**
1. [Codex rust-v0.167.0 发布](#item-harness-arch-1) ⭐️ 7.8/10
2. [Agent Framework dotnet-1.28.0 发布](#item-harness-arch-2) ⭐️ 6.8/10
3. [Anthropic agent memory 组件架构阐述](#item-harness-arch-3) ⭐️ 6.8/10
4. [Claude Code v2.1.319 发布](#item-harness-arch-4) ⭐️ 5.5/10

**[Agent 工程师日报](#sec-agent-engineer)**
1. [Anthropic 公布 Agent 记忆架构研究](#item-agent-engineer-1) ⭐️ 8.8/10
2. [Harness-S 提出 sibling harness 训练框架](#item-agent-engineer-2) ⭐️ 7.0/10
3. [HF Daily Papers：Drex 开源决策模型发布](#item-agent-engineer-3) ⭐️ 7.0/10
4. [Open ASR Leaderboard 新增埃及、尼日利亚英语评测集](#item-agent-engineer-4) ⭐️ 6.8/10
5. [HF daily paper: Random Is Almost Enough? Stable and Low-Cost Benchmark Compression via BestRand](#item-agent-engineer-5) ⭐️ 6.0/10

**[AI 日报](#sec-ai-daily)**
1. [OpenAI 与 Hacktron 合作挖漏洞](#item-ai-daily-1) ⭐️ 7.8/10
2. [OpenAI 发布 BioBasicsBench 基准](#item-ai-daily-2) ⭐️ 7.8/10
3. [AI 编程代理分心与 TODO 清理方案](#item-ai-daily-3) ⭐️ 7.8/10
4. [GitHub 发布智能体工程开发者指南](#item-ai-daily-4) ⭐️ 5.8/10
5. [GPT-6 Cyber 传闻发布](#item-ai-daily-5) ⭐️ 5.5/10

**[AI 羊毛](#sec-ai-deals)**
1. [本周 Epic 三游免费 11.6-12](#item-ai-deals-1) ⭐️ 8.0/10

---

## Harness 架构
{: #sec-harness-arch .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-harness-arch" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-harness-arch-1"></a>
### [Codex rust-v0.167.0 发布](https://github.com/openai/codex/releases/tag/rust-v0.167.0) ⭐️ 7.8/10

OpenAI Codex CLI 发布 rust-v0.167.0。新增 agent command center（\`codex agents --no-daemon\`）、终端内跨后端切换保留草稿、本地图片预览与点击打开、GCP Vertex AI 引导（\`gcp\_setup\_wizard\`）及系统代理实验性开关。修复跨模型提供商切换后聊天丢失、\`Ctrl+L\` 清除终端保留历史、网络审批并发控制、实时 V3 转录保存及上下文压缩边界情况。文档补充托管网络约束与模型迁移指引，Linux musl 构建优化空闲内存。

github · github-actions\[bot\] · 11月6日 01:40

**「设计要点」** 独立 Web 搜索使用 turn-scoped 权限，托管网络要求通过 \`permissions.network\` 配置；Code Mode 输出采用有界收集与服务器端截断。Guardian 审查新增注入线程命令与自适应评估，MXC 沙箱跳过只读卷根扩展，子代理关系在创建子存储前持久化。

**「改了什么」** 新增 agent command center 与嵌入式会话支持，终端内切换后端保留草稿。Code Mode 实现有界输出与服务器端截断，Guardian 审查扩展，网络审批支持并发控制，实时 V3 转录保存至历史。

**标签**: `#runtime`, `#permissions`, `#subagents`

---

<a id="item-harness-arch-2"></a>
### [Agent Framework dotnet-1.28.0 发布](https://github.com/microsoft/agent-framework/releases/tag/dotnet-1.28.0) ⭐️ 6.8/10

Microsoft Agent Framework .NET 1.28.0 官方小版本发布。本次更新以琐碎提交为主，包含少量功能修复与特性：.NET 端修复声明式工作流公式解析的 InvariantCulture 问题；Python 端支持并发 MCP 调用且携带请求自有 headers、收窄无作用域 URL 会话的审批范围、以及在 Python 3.15 上启用 Redis 集成。无重大架构变更或破坏性变更。

github · dmytrostruk · 11月6日 22:00

**「改了什么」** .NET 端修复声明式工作流公式与值的解析，改用 InvariantCulture。Python 端支持并发 MCP 调用并携带请求自有 headers，同时收窄无作用域 URL 会话的审批范围，并在 Python 3.15 上启用 Redis 集成。

**标签**: `#mcp`, `#runtime`, `#permissions`, `#tools`

---

<a id="item-harness-arch-3"></a>
### [Anthropic agent memory 组件架构阐述](https://www.anthropic.com/research/components-of-agent-memory) ⭐️ 6.8/10

这是 Anthropic Engineering 发布的 agent 记忆架构概念文章，核心借鉴生物记忆的分工机制设计 agent 记忆系统，相关思路源自 Letta 与 UC Berkeley 提出的 sleep-time compute 概念。文章明确定义的 agent 记忆排除模型权重更新、单会话上下文学习、上下文压缩等机制，特指跨会话保留的可读记忆；同时提出通过“dreaming”离线重放机制整合会话日志为长期记忆，通过 CL-Bench 1.0 和宝可梦红两项评测验证了记忆重要性标记、分层存储、学习闭环的实际价值，未公开具体实现代码或接口。

rss · Anthropic Engineering · 11月6日 00:00

**「设计要点」** 设计采用生物记忆分层类比，在线捕获的瞬时记忆通过离线“dreaming”重放整合为长期记忆；运行时对关键事件做重要性标记，优先重放高显著性内容，记忆存储采用分层文件结构，区分全局规则、局部策略与临时记录，避免冗余存储可实时获取的信息。

**标签**: `#memory`, `#runtime`

---

<a id="item-harness-arch-4"></a>
### [Claude Code v2.1.319 发布](https://github.com/anthropics/claude-code/releases/tag/v2.1.319) ⭐️ 5.5/10

Claude Code v2.1.319 发布，调整 auto mode 在遥测关闭或 LLM 网关后的行为，新增服务器端检查逻辑。MCP 工具调用支持后台任务，新增 \`permissions.denyInsteadOfPrompting\` 权限设置。Claude apps gateway 新增 spend 显示、预算冲突规则、JSON 日志格式等功能，同时修复多项 MCP 连接、diff 显示及权限处理 bug。

github · claude-code-publisher\[bot\] · 11月6日 17:04

**「设计要点」** 运行时通过 \`CLAUDE\_CODE\_AUTO\_MODE\_SERVER\` 在客户端内置分类器与服务器端检查间切换，LLM 网关（Bedrock、Vertex、Foundry）行为独立；权限层新增 deny-instead-of-prompt 开关，MCP 层引入任务后台化与同步等待 toggle，功能标志系统可独立关闭获取而不影响遥测。

**「改了什么」** Auto mode 在遥测关闭或 LLM 网关后改为服务器端检查或拒绝并移除内置分类器回退，新增 \`CLAUDE\_CODE\_AUTO\_MODE\_SERVER\` 控制；MCP 任务默认后台运行，新增 \`CLAUDE\_CODE\_DISABLE\_MCP\_TASK\_BACKGROUND\` 切换同步等待；权限系统新增 \`permissions.denyInsteadOfPrompting\` 实现直接拒绝；Claude apps gateway 新增 spend 统计、预算优先级规则、登录通知及 \`CLAUDE\_GATEWAY\_LOG\_FORMAT=json\`。

**标签**: `#runtime`, `#mcp`, `#permissions`, `#tools`

---

## Agent 工程师日报
{: #sec-agent-engineer .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-agent-engineer" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-agent-engineer-1"></a>
### [Anthropic 公布 Agent 记忆架构研究](https://www.anthropic.com/research/components-of-agent-memory) ⭐️ 8.8/10

2026 年 11 月 6 日 Anthropic Research 发布官方研究，提出受人类神经科学启发的 AI agent 记忆架构，核心包含“睡眠期计算（sleep-time compute）”机制：agent 在交互空闲时通过复盘会话日志（称为“dreaming”）整理跨会话记忆，区别于权重更新、单会话上下文学习或上下文压缩。研究通过自研 CL-Bench 1.0 长期任务评测、宝可梦红游戏导航两项测试验证组件效果：无差别记录所有细节的 Claude Sonnet 3.7 在宝可梦任务中仅获得 1 枚徽章，精简记录策略性知识的 Claude Fable 5 获得 4 枚徽章；Claude Opus 5.5 是首个实现“记忆-验证-规则沉淀”闭环的模型，其带记忆的得分与 Opus 5 持平，无记忆基线得分略高于 Opus 5。该框架目前仅通过 Anthropic 内部两项评测验证，跨场景通用性尚未公开，面向 AI agent 设计与知识沉淀场景的开发者。

rss · Anthropic Research · 11月6日 00:00

**「为什么重要」** Anthropic 官方首次系统提出可落地的 agent 记忆分层设计框架，将生物记忆的“实时编码-离线整理-长期沉淀”逻辑映射到 agent 系统，填补了此前 agent 记忆设计缺乏系统参考的空白；该架构在 coding agent 长周期任务、知识复用场景的实际效果尚未有第三方验证。

**「可关注」** agent 记忆需区分“实时可获取的细节”和“需主动沉淀的策略性知识”，过度记录前者会挤占上下文资源，拖慢长周期任务执行。

**标签**: `#memory`, `#architecture`, `#research`

---

<a id="item-agent-engineer-2"></a>
### [Harness-S 提出 sibling harness 训练框架](https://huggingface.co/papers/2611.04277) ⭐️ 7.0/10

2026-11-06，Hugging Face Daily Papers 收录论文《Harness-S: Learning from Sibling Harnesses for Generalizable Agent Training》。该工作提出 Harness-S 训练框架：通过 Directional Harness Evolution 沿不同修复方向演化专业 sibling harnesses，构成训练期间固定的 Sibling Harness Pool；策略训练时仅在基础 harness 下所有初始执行失败时，才调用池中 sibling harnesses 进行 rescue，最终将修复能力迁移到单一策略，使其在原始 harness 下仍有效。论文指出 harness evolution 呈现 Locality、Complementarity 与 Nonstationary 特性，即不同变体修复不同失败，且其效用随策略学习而变化。材料未给出具体性能数字或实验规模。

rss · Hugging Face Daily Papers · 11月6日 00:00

**「为什么重要」** 该论文直接针对 coding agent 训练中的 harness 设计问题，提出可复用的 sibling harness 池与 rescue 训练机制，为优化训练 pipeline 提供了具体技术路径。其非平稳性观察对设计动态适应策略具有参考价值。

**「可关注」** 可关注：Harness-S 不追求单一通用 harness，而是利用固定 sibling harness 池在基础执行全失败时做 rescue，再将能力迁移回原始 harness 的策略训练思路。

**标签**: `#harness`, `#coding-agent`, `#eval`

---

<a id="item-agent-engineer-3"></a>
### [HF Daily Papers：Drex 开源决策模型发布](https://huggingface.co/papers/2611.07854) ⭐️ 7.0/10

2026 年 11 月 6 日，Hugging Face Daily Papers 发布论文介绍开源非自回归决策模型家族 Drex，包含 4 个参数版本：8B（DLM）、9B（v1.5）、35B 含 3B 激活参数（v2.0）、27B（Max）。该模型针对自回归大模型在决策任务的生产痛点设计，输入支持状态（文档、记录、智能体上下文，可选配图像）与带选项的问题，直接输出选项概率分布，无需自回归解码，可规避输出不一致、解析开销、高成本高时延问题。当前公开内容未包含详细性能基准与实现细节，该论文当日获得 18 次 upvote，暂无社区评论。

rss · Hugging Face Daily Papers · 11月6日 00:00

**「为什么重要」** Drex 明确针对决策场景优化，且原生支持智能体上下文输入，为 coding agent 的决策模块设计提供了区别于默认自回归 LLM 的新选项，但当前缺乏公开性能数据，实际生产适配效果尚未验证。

**「可关注」** 可关注：非自回归决策模型对自回归 LLM 在决策场景的解析、时延、成本痛点的替代路径，以及其智能体上下文输入能力与现有 agent 框架的兼容性。

**标签**: `#coding-agent`

---

<a id="item-agent-engineer-4"></a>
### [Open ASR Leaderboard 新增埃及、尼日利亚英语评测集](https://huggingface.co/blog/open-asr-leaderboard-liva) ⭐️ 6.8/10

2026 年 11 月 6 日，Hugging Face 官方博客宣布与 Liva AI 合作，向 Open ASR Leaderboard 新增两组私有英语口音测试集：埃及英语对话自发语音 1.34 小时、尼日利亚英语对话自发语音 1.55 小时，转录格式均为带标点、区分大小写、保留口吃等不流畅表达。两组数据均来自 Liva AI 消费级产品的真实用户交互，属于自然高语境的自发语音，非人工诱导的任务式交互。此次更新旨在提升低资源口音的 ASR 评测覆盖度，同时通过引入新数据提供方减少 benchmark 刷分行为。目前 Open ASR Leaderboard 已可按 Kachru 三圈模型拆分不同口音的模型性能结果，新增资源主要面向构建或评估语音 AI Agent、ASR 评测 harness 的工程师。

rss · Hugging Face Blog · 11月6日 00:00

**「为什么重要」** 已发生的变化是此前覆盖不足的埃及、尼日利亚英语口音获得专属 ASR 测试集，低资源口音评测的代表性与可信度得到提升。尚未证实的影响是此次更新仅对语音相关 AI Agent、ASR 评测场景有直接价值，对更广泛的 Agent 工程社区影响有限。

**「可关注」** 可关注：若你的 ASR 评测场景覆盖埃及、尼日利亚英语口音，可直接复用该组真实产品场景下的自发语音测试集补充评测维度；同时 Open ASR Leaderboard 已按 Kachru 三圈模型拆分口音结果，可针对性对比目标口音下的模型性能表现。

**标签**: `#eval`

---

<a id="item-agent-engineer-5"></a>
### [HF daily paper: Random Is Almost Enough? Stable and Low-Cost Benchmark Compression via BestRand](https://huggingface.co/papers/2611.00883) ⭐️ 6.0/10

A research paper proposes BestRand, a stable and low-cost benchmark compression method for model evaluation, based on the finding that random subset sampling for benchmarks yields small errors with high probability but rare large errors due to a long-tailed error distribution.

rss · Hugging Face Daily Papers · 11月6日 00:00

**标签**: `#eval`

---

## AI 日报
{: #sec-ai-daily .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-daily" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-daily-1"></a>
### [OpenAI 与 Hacktron 合作挖漏洞](https://openai.com/index/partnering-with-hacktron) ⭐️ 7.8/10

OpenAI 官方宣布与安全厂商 Hacktron 达成合作，将开展系统漏洞挖掘、第三方服务连接测试，同步强化前沿 AI 安全防御能力。本次合作覆盖 OpenAI 自有系统及对接的第三方服务场景。

rss · OpenAI Blog · 11月6日 08:00

**「为什么重要」** 前沿 AI 系统安全风险是行业共性关注点，此次官方合作明确第三方安全测试路径，可降低潜在漏洞被恶意利用的概率。

**「可关注」** 可关注：OpenAI 后续公开的第三方安全测试范围与漏洞披露规则。

**标签**: `#lab`, `#policy`, `#industry`

---

<a id="item-ai-daily-2"></a>
### [OpenAI 发布 BioBasicsBench 基准](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science) ⭐️ 7.8/10

OpenAI 正式推出 BioBasicsBench 基准，该基准共设置 100 项任务，用于衡量 AI 代理解读原始实验数据、处理日常湿实验室科学任务的能力。

rss · OpenAI Blog · 11月6日 00:00

**「为什么重要」** 该基准为 AI 代理湿实验室日常任务能力提供了可量化的评估标准，可用于相关能力迭代的对照参考。

**「可关注」** 可关注 BioBasicsBench 对 AI 代理湿实验室任务能力的量化评估维度设计。

**标签**: `#eval`, `#lab`, `#industry`

---

<a id="item-ai-daily-3"></a>
### [AI 编程代理分心与 TODO 清理方案](https://developers.googleblog.com/agent-distraction/) ⭐️ 7.8/10

Google 开发者博客发布研究指出，AI 编程代理会将代码中的过时 TODO 注释、已修复缺陷记录、滞后文档等误判为有效指令，导致执行分心，额外消耗 token、步骤与时间，甚至引发错误实现。研究通过控制开发者、代码库复杂度、任务类型等变量的多变量回归验证，该问题的统计显著性达 p&lt;0.0001。Google 还开发了自动化 TODO 清理工具，过去 6 个月已清理数千条过时引用，人类审核通过率超 95%。

rss · Google Developers AI · 11月6日 00:00

**「为什么重要」** 该研究首次量化了过时代码上下文对 AI 编程代理的隐性执行成本，提供了从代码本身提取客观信号度量该问题的方法，也为团队重新评估遗留代码清理优先级、构建对 AI 友好的代码库提供了实践参考。

**「可关注」** 可关注：通过将代码中的 TODO\(bug/...\)与对应 bug 跟踪系统的状态交叉验证，结合多年代码历史确认 TODO 意图已过时后自动清理，可降低 AI 编程代理的无效分心。

**标签**: `#agent`, `#industry`, `#eval`

---

<a id="item-ai-daily-4"></a>
### [GitHub 发布智能体工程开发者指南](https://github.blog/ai-and-ml/github-copilot/beyond-code-generation-a-developers-guide-to-agentic-engineering/) ⭐️ 5.8/10

2026 年 11 月 6 日 GitHub 官方博客发布《超越代码生成：开发者智能体工程指南》，属于思想领导类内容，未发布新模型、产品或政策。2026 年 10 月单周 GitHub 提交量达 12 亿次，同比提升 400%，超过 2025 年全年提交总量；引用 Faros AI 研究显示，团队 AI 采用率从低到高时，PR 平均审查时长上升 441%。该指南围绕规划、构建、验证、观测四个阶段，介绍如何通过 GitHub Copilot 系列能力落地智能体工程工作流。

rss · GitHub Blog · 11月6日 22:15

**「为什么重要」** 该指南是 GitHub 官方首次系统输出智能体工程落地方法论，配套的行业统计数据可帮助开发团队客观评估 AI 引入对研发效率的正反双向影响。

**「可关注」** 可关注：团队高 AI 采用率下 PR 审查时长上升 441%的行业数据，以及指南中 Plan、Build、Verify、Observe 四阶段智能体工作流设计。

**标签**: `#industry`, `#agent`, `#product`

---

<a id="item-ai-daily-5"></a>
### [GPT-6 Cyber 传闻发布](https://mp.weixin.qq.com/s?__biz=MzIwNzc2NTk0NQ==&amp;mid=2247623182&amp;idx=1&amp;sn=1e4cc2b38d10ed51b771c1772c2770f6) ⭐️ 5.5/10

自媒体夕小瑶科技说报道称 OpenAI 已正式发布网络安全专用模型 GPT-6 Cyber，该模型基于 GPT-6 Astra 打造，接替 GPT-5.6 Cyber。报道称该模型在 Firefox 代码库审计中据称发现 81 个此前未知的高危漏洞，并在 Linux 内核研究中据称复现 1724 个漏洞、生成 948 个可用的提权利用程序。但截至发稿，OpenAI 尚未发布官方公告佐证上述信息，相关能力与数字均无法通过官方渠道核实，属于传闻类信息。

rss · 夕小瑶科技说 · 11月6日 01:50

**「可关注」** 可关注：AI 在代码审计中从漏洞发现、验证到提供候选补丁的全链路能力进展，但当前报道尚未经官方渠道证实，需等待官方信息确认。

**标签**: `#model`, `#lab`, `#industry`

---

## AI 羊毛
{: #sec-ai-deals .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-deals" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-deals-1"></a>
### [本周 Epic 三游免费 11.6-12](https://www.appinn.com/eggs-261106/) ⭐️ 8.0/10

你看到的内容可能由第三方 AI 基于小众软件文章提炼总结而成，可能与原文真实意图存在偏差。不代表小众软件观点和立场。请点击链接阅读原文细致比对和校验。本周（11.6~11.12）Epic 平台开放 3 款内容免费领取，电脑端可领取《浮游世界/Flotsam》本体，安卓及 iOS 端可领取《巴别塔圣歌/Chants of Sennaar》本体（该移动端限免存在锁区限制）；《遗忘国度：放置勇士/Idle Champions of the Forgotten Realms》本体此前曾免费提供，本次全端可领取限时游戏内礼包 Morte’s Renown Pack。《浮游世界》《巴别塔圣歌》需前往 Epic 对应页面直接领取，《遗忘国度》的礼包需登录 Epic 版本游戏内领取，活动周期为 11 月 6 日至 11 月 12 日。

rss · 小众软件 · 11月6日 08:21

**「为什么重要」** 三款游戏在 Steam 平台均获得玩家正面评价，《巴别塔圣歌》好评率高达 97%，《浮游世界》近期好评率达 88%；《遗忘国度》的限时礼包包含 5 名角色、每名角色 32 个白金宝箱及药水、专属魔宠等资源，适合对应题材爱好者领取。

**「可关注」** 可关注：《巴别塔圣歌》移动端限免存在锁区限制，部分用户无法领取；《遗忘国度》的限时礼包需登录 Epic 版本游戏内领取，非 Epic 本体用户需注意版本对应。

**标签**: `#promo`, `#limited-free`, `#free-game`

---