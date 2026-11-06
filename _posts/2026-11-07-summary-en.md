---
layout: default
title: "Horizon Summary: 2026-11-07 (EN)"
date: 2026-11-07
lang: en
---

> From 195 items, 15 important content pieces were selected

---

**Agent Harness Architecture**
1. [Codex CLI rust-v0.167.0 发布](#item-harness-arch-1) ⭐️ 7.8/10
2. [dotnet-1.28.0 发布](#item-harness-arch-2) ⭐️ 6.8/10
3. [Anthropic 发布 Agent Memory 架构概念](#item-harness-arch-3) ⭐️ 6.8/10
4. [Claude Code 2.1.319 发布](#item-harness-arch-4) ⭐️ 5.5/10

**AI Agent Engineer**
1. [Anthropic 发布 Agent 记忆组件研究](#item-agent-engineer-1) ⭐️ 8.8/10
2. [Harness-S 论文：同级 Harness 救援训练](#item-agent-engineer-2) ⭐️ 7.0/10
3. [HF Daily Papers 发布 Drex 决策模型](#item-agent-engineer-3) ⭐️ 7.0/10
4. [ASR 榜单新增埃及、尼日利亚英语测试集](#item-agent-engineer-4) ⭐️ 6.8/10
5. [HF daily paper: Random Is Almost Enough? Stable and Low-Cost Benchmark Compression via BestRand](#item-agent-engineer-5) ⭐️ 6.0/10

**AI Daily**
1. [OpenAI 合作 Hacktron 挖漏洞](#item-ai-daily-1) ⭐️ 7.8/10
2. [OpenAI 发布 BioBasicsBench 湿实验室基准](#item-ai-daily-2) ⭐️ 7.8/10
3. [AI编程代理易被过时TODO分心](#item-ai-daily-3) ⭐️ 7.8/10
4. [GitHub 发布代理工程开发者指南](#item-ai-daily-4) ⭐️ 5.8/10
5. [GPT-6 Cyber 传闻发布](#item-ai-daily-5) ⭐️ 5.5/10

**AI Deals**
1. [本周Epic免费游戏 11.6~11.12](#item-ai-deals-1) ⭐️ 8.0/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [Codex CLI rust-v0.167.0 发布](https://github.com/openai/codex/releases/tag/rust-v0.167.0) ⭐️ 7.8/10

OpenAI Codex CLI rust-v0.167.0 正式发布。新功能包括 agent 命令中心（\`codex agents --daemon\`）、跨后端切换并保留草稿、审批流程体验改进，以及通过 \`gcp\_setup\_wizard\` 接入 GCP Vertex AI。技术层面新增 bounded Code Mode 输出收集与渲染、服务端输出截断、共享 MCP 连接的 per-chat 租约，以及 \`\[permissions.network\]\` 下的托管网络约束。未进行重大架构重构，改动聚焦于 harness 可用性与功能完整性。

github · github-actions\[bot\] · Nov 6, 01:40

**「设计要点」** 本次发布引入共享 MCP 连接的 per-chat 租约与独立 web 搜索的 turn-scoped 权限，收窄 agent 运行时的资源隔离粒度。服务端输出截断与 bounded Code Mode 集合将渲染限制从客户端移至服务端，降低长会话下的 TUI 内存压力。

**「改了什么」** 新增带未读标记的 agent 命令中心、会话选择器中的跨后端草稿保留，以及审批提示时的内联补丁审查。引入 GCP Vertex AI 配置、实验性系统代理支持、保留 realtime V3 语音转录，并修复跨模型提供商切换时的聊天可见性与网络审批并发问题，同时通过减少 allocator arenas 降低 Linux musl 空闲内存。

**Tags**: `#runtime`, `#permissions`, `#subagents`

---

<a id="item-harness-arch-2"></a>
### [dotnet-1.28.0 发布](https://github.com/microsoft/agent-framework/releases/tag/dotnet-1.28.0) ⭐️ 6.8/10

Microsoft Agent Framework .NET 1.28.0 发布。本次为官方小版本更新，以琐碎提交为主。.NET 运行时修复声明式工作流公式解析的 InvariantCulture 问题。Python SDK 新增并发 MCP 调用支持（请求级头部）、收窄无作用域 URL 会话审批范围，并支持 Python 3.15 的 Redis 集成。无重大架构或破坏性变更。

github · dmytrostruk · Nov 6, 22:00

**「改了什么」** .NET 修复工作流公式解析的区域性依赖。Python 实现并发 MCP 调用、收紧 URL 会话审批策略、添加 Python 3.15 Redis 集成支持。其余变更包括拼写修正、依赖升级及仓库管理调整。

**Tags**: `#mcp`, `#runtime`, `#permissions`, `#tools`

---

<a id="item-harness-arch-3"></a>
### [Anthropic 发布 Agent Memory 架构概念](https://www.anthropic.com/research/components-of-agent-memory) ⭐️ 6.8/10

Anthropic Engineering 发布概念文章，提出受生物记忆启发的 agent memory 架构。系统分实时编码与离线整合两个阶段，通过 salience tagging 组织跨 session 持久化知识。文章以 CL-Bench 1.0 与 Pokémon Red 两项评测，展示从 Sonnet 3.7 到 Opus 5.5 在记忆管理上的行为差异，但未披露具体实现代码或接口。

rss · Anthropic Engineering · Nov 6, 00:00

**「设计要点」** Memory 以文件系统外存持久化，排除权重更新、in-context learning 与 compaction。Dreaming 利用交互间隙重放会话日志，提炼验证规则并修正错误。评测 harness 通过跨 session memory directory 测试 agent 长时序任务学习能力。

**Tags**: `#memory`, `#runtime`

---

<a id="item-harness-arch-4"></a>
### [Claude Code 2.1.319 发布](https://github.com/anthropics/claude-code/releases/tag/v2.1.319) ⭐️ 5.5/10

Claude Code v2.1.319 调整了 auto mode 在关闭遥测或功能标志、以及位于 LLM 网关后的行为：服务器无法检查的调用会被询问或拒绝，不再回退到内置分类器，可通过 \`CLAUDE\_CODE\_AUTO\_MODE\_SERVER=0\` 保留旧行为（Bedrock、Vertex 和 Foundry 不受影响）。新增 MCP 任务后台运行支持，配置开关 \`CLAUDE\_CODE\_DISABLE\_MCP\_TASK\_BACKGROUND\` 可改为同步等待。同时引入 \`permissions.denyInsteadOfPrompting\` 设置，使工具调用在权限提示时直接拒绝并继续回合，适用于终端会话、子代理和队友。

github · claude-code-publisher\[bot\] · Nov 6, 17:04

**「设计要点」** Auto mode 的检查逻辑从客户端迁移到服务端，通过 \`CLAUDE\_CODE\_AUTO\_MODE\_SERVER\` 环境变量控制回退。MCP 任务后台化通过配置开关切换，影响终端、子代理和队友会话中的权限处理流程。

**「改了什么」** Auto mode 在遥测或功能标志关闭、以及 LLM 网关后默认启用服务端检查，不再回退到内置分类器。MCP 工具调用作为任务时立即转入后台，完成后通知 Claude；新增 \`permissions.denyInsteadOfPrompting\` 设置，在终端、子代理和队友会话中直接拒绝权限请求而非弹出提示。

**Tags**: `#runtime`, `#mcp`, `#permissions`, `#tools`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [Anthropic 发布 Agent 记忆组件研究](https://www.anthropic.com/research/components-of-agent-memory) ⭐️ 8.8/10

On November 6, 2026, Anthropic Research published a study on AI agent memory architecture inspired by human neuroscience, proposing a division of labor between real-time event tagging and offline &quot;sleep-time compute \(dreaming\)&quot; for consolidating experiences into long-term knowledge. Key verifiable details include two evaluation scenarios: on the CL-Bench 1.0 benchmark, Claude Opus 5 became the first model to close the learning loop by capturing validated rules for future questions, while on the Pokémon Red gameplay test, Claude Fable 5 outperformed Claude Sonnet 3.7 by writing only 9 targeted memory files \(compared to Sonnet 3.7&\#x27;s 413 indiscriminate files\) and earning 4 badges \(compared to Sonnet 3.7&\#x27;s 1\). The research explicitly excludes weight updates, in-context learning, and context compaction from its definition of agent memory, and targets engineers building long-horizon AI agents.

rss · Anthropic Research · Nov 6, 00:00

**「为什么重要」** The published neuroscience-inspired memory architecture and validated sleep-time compute mechanism provide concrete design references for reducing context redundancy and improving knowledge consolidation in long-horizon agent systems. The actual performance impact of implementing these patterns in custom agent frameworks remains unverified as of now.

**「可关注」** 可关注：sleep-time compute \(dreaming\) workflows and salient event filtering logic, as the research shows they directly reduce unnecessary memory overhead and improve long-horizon task performance for agents.

**Tags**: `#memory`, `#architecture`, `#research`

---

<a id="item-agent-engineer-2"></a>
### [Harness-S 论文：同级 Harness 救援训练](https://huggingface.co/papers/2611.04277) ⭐️ 7.0/10

Hugging Face Daily Papers 于 2026-11-06 收录论文《Harness-S: Learning from Sibling Harnesses for Generalizable Agent Training》。该论文提出 Harness-S 框架，通过 Directional Harness Evolution 沿不同修复方向演化出专业同级 harness 并形成固定池，再经 Complementary Harness Rescue Training 在基础 harness 所有初始尝试失败时选择性调用该池救援。研究表明从共同基础演化的 harness 表现出局部性、互补性和非平稳性——变体修复不同失败，且效用随策略学习变化。该方法面向 coding agent 训练，旨在将救援获得的能力迁移到在原始 harness 下仍有效的单一策略。

rss · Hugging Face Daily Papers · Nov 6, 00:00

**「为什么重要」** 该论文提供了 directional harness evolution 与 rescue training 的具体技术细节，直接关联 agent harness 设计与训练流水线优化。不同于追求普遍最优 harness，Harness-S 接受 harness 效用随策略学习非平稳变化的事实，通过固定同级池选择性救援失败，可能为训练 pipeline 提供新思路。

**「可关注」** 可关注：Harness-S 的 sibling harness 池在策略训练期间固定，且仅在基础 harness 所有初始尝试失败时触发救援，这种&quot;失败即救援&quot;机制可能改变训练流水线的资源分配与延迟预期。

**Tags**: `#harness`, `#coding-agent`, `#eval`

---

<a id="item-agent-engineer-3"></a>
### [HF Daily Papers 发布 Drex 决策模型](https://huggingface.co/papers/2611.07854) ⭐️ 7.0/10

2026年11月6日，Hugging Face Daily Papers发布论文，介绍开源非自回归决策模型家族Drex，包含4个规格：8B（DLM）、9B（v1.5）、35B含3B激活参数（v2.0）、27B（Max）。该模型针对自回归LLM在决策任务中的生产痛点（输出不一致、需解析输出、成本与延迟高）设计，输入支持状态（文档、记录、智能体上下文，可选配图像）及带选项的问题，直接输出选项的概率分布，无需自回归解码。当前公开内容未包含详细性能基准与实现细节，主要面向需要决策模块的AI应用（含coding agent场景）开发者。

rss · Hugging Face Daily Papers · Nov 6, 00:00

**「为什么重要」** Drex作为开源非自回归决策模型，明确支持智能体上下文输入，为coding agent等场景的决策模块提供了绕开自回归LLM生产痛点的可选方案；但当前公开内容缺少性能基准与实现细节，实际生产表现尚未得到验证。

**「可关注」** 可关注：Drex 支持智能体上下文输入，可评估其适配 coding agent 决策模块的可行性。

**Tags**: `#coding-agent`

---

<a id="item-agent-engineer-4"></a>
### [ASR 榜单新增埃及、尼日利亚英语测试集](https://huggingface.co/blog/open-asr-leaderboard-liva) ⭐️ 6.8/10

2026年11月6日，Hugging Face官方博客宣布与Liva AI合作，向Open ASR Leaderboard新增两套私有对话式自发语音测试数据集，分别对应埃及英语、尼日利亚英语口音，时长1.34小时、1.55小时，转录格式为带标点、区分大小写、保留口吃等不流畅表达。本次是该榜单扩充口音覆盖的增量更新，此前已覆盖5种口音的脚本化与对话式语音数据，以及印度口音英语测试集。新增数据集上线后，榜单将基于Kachru的三圈理论拆分口音类别呈现更细粒度的性能 breakdown，面向ASR模型评估、语音AI Agent开发场景开放，用于补充低资源口音的评估覆盖。

rss · Hugging Face Blog · Nov 6, 00:00

**「为什么重要」** 本次更新填补了Open ASR Leaderboard在埃及、尼日利亚英语口音上的评估空白，新增的私有held-out数据集可降低基准刷分行为，让ASR模型性能对比更可信。

**「可关注」** 可关注：Open ASR Leaderboard新增的埃及、尼日利亚英语对话式测试集已开放用于ASR模型评估，可补充现有评估 harness 对低资源口音的覆盖。

**Tags**: `#eval`

---

<a id="item-agent-engineer-5"></a>
### [HF daily paper: Random Is Almost Enough? Stable and Low-Cost Benchmark Compression via BestRand](https://huggingface.co/papers/2611.00883) ⭐️ 6.0/10

A research paper proposes BestRand, a stable and low-cost benchmark compression method for model evaluation, based on the finding that random subset sampling for benchmarks yields small errors with high probability but rare large errors due to a long-tailed error distribution.

rss · Hugging Face Daily Papers · Nov 6, 00:00

**Tags**: `#eval`

---

## AI Daily

<a id="item-ai-daily-1"></a>
### [OpenAI 合作 Hacktron 挖漏洞](https://openai.com/index/partnering-with-hacktron) ⭐️ 7.8/10

OpenAI 官方宣布与安全厂商 Hacktron 达成合作，将开展系统漏洞挖掘、第三方服务连接测试工作，以此强化前沿 AI 系统的安全防御能力。

rss · OpenAI Blog · Nov 6, 08:00

**「为什么重要」** 本次是 OpenAI 官方公开的前沿 AI 安全防御新动作，反映出行业对 AI 系统安全性的重视程度持续提升。

**「可关注」** 可关注：OpenAI 后续公开的漏洞挖掘规则、测试范围及相关安全改进公告。

**Tags**: `#lab`, `#policy`, `#industry`

---

<a id="item-ai-daily-2"></a>
### [OpenAI 发布 BioBasicsBench 湿实验室基准](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science) ⭐️ 7.8/10

OpenAI 官方发布 100 任务基准 BioBasicsBench，用于测量 AI agent 解读原始实验数据、处理日常湿实验室科学任务的能力。

rss · OpenAI Blog · Nov 6, 00:00

**「为什么重要」** 当前针对 AI agent 湿实验室能力的标准化评估工具稀缺，该基准为相关能力量化对比提供了可复用的框架。

**「可关注」** 可关注：BioBasicsBench 的 100 项任务覆盖日常湿实验室场景，可作为相关 AI agent 湿实验室能力的量化评估参考。

**Tags**: `#eval`, `#lab`, `#industry`

---

<a id="item-ai-daily-3"></a>
### [AI编程代理易被过时TODO分心](https://developers.googleblog.com/agent-distraction/) ⭐️ 7.8/10

Google开发者博客发布内容指出，AI编程代理会将代码中的过时规格、已解决bug的TODO注释、滞后文档等误判为有效指令，导致执行分心，浪费token、时间甚至引发错误逻辑与决策。由于每月数百万次代理会话中手动统计分心频率不可行，Google团队提出通过TODO注释与对应bug工单状态的交叉比对，作为可自动提取的客观信号度量该问题，多变量回归分析（控制开发者、代码库复杂度等变量）显示无提示的bug绕路会带来统计显著的开销（p&lt;0.0001）。团队通过数千名工程师、数亿次代理步骤的分布式追踪量化了该问题，两类典型分心场景包括：代理调查无关bug时被2023年已修复的遗留TODO分心绕路，以及代理在调查目标bug时无提示“修复”关联旧bug导致范围蔓延，均需人类介入纠正。团队开发的TODO清理代理过去6个月已删除数千个确认过时的TODO引用，人类审核通过率超95%。

rss · Google Developers AI · Nov 6, 00:00

**「为什么重要」** 随着AI编程代理承担更复杂的编码任务，代码库中被长期遗忘的过时内容会给代理执行带来可量化的额外成本，此前因感知价值低被搁置的遗留TODO清理工作需重新评估优先级。

**「可关注」** 可关注：通过TODO\(bug/...\)注释与对应bug工单状态的交叉比对，可客观度量AI编程代理的分心问题，全代码库扫描器、presubmit分析器与自动化清理代理是当前可落地的解决方案。

**Tags**: `#agent`, `#industry`, `#eval`

---

<a id="item-ai-daily-4"></a>
### [GitHub 发布代理工程开发者指南](https://github.blog/ai-and-ml/github-copilot/beyond-code-generation-a-developers-guide-to-agentic-engineering/) ⭐️ 5.8/10

GitHub 发布《Beyond code generation: A developer&\#x27;s guide to agentic engineering》开发者指南，提出将 AI 代理整合进软件开发生命周期的 Plan、Build、Verify、Observe 四阶段。文章引用数据称，2026 年 10 月 GitHub 单周提交量超过 12 亿次，同比增长 400%，超过 2025 全年总量；同时引用 Faros AI 研究指出，团队从低 AI 采用转向高 AI 采用时，PR 评审耗时增加 441%。该指南为思想领导力文章，未发布新模型或产品。

rss · GitHub Blog · Nov 6, 22:15

**「为什么重要」** 这篇指南用提交量增长和 PR 评审延迟数据，论证了单纯代码生成不等于生产力提升，代理工程可能解决 AI 采用带来的流程瓶颈。对正在评估 AI 代理落地策略的团队，它提供了一个可操作的四阶段框架。

**「可关注」** 可关注：GitHub 将代理工程拆分为 Plan、Build、Verify、Observe 四阶段，并配套 Copilot 会话连续性、云沙箱、共享记忆、Copilot Dreaming 等特性，支撑跨设备、跨任务的持续开发。

**Tags**: `#industry`, `#agent`, `#product`

---

<a id="item-ai-daily-5"></a>
### [GPT-6 Cyber 传闻发布](https://mp.weixin.qq.com/s?__biz=MzIwNzc2NTk0NQ==&amp;mid=2247623182&amp;idx=1&amp;sn=1e4cc2b38d10ed51b771c1772c2770f6) ⭐️ 5.5/10

自媒体夕小瑶科技说称OpenAI正式发布网络安全专用模型GPT-6 Cyber，该模型基于GPT-6 Astra打造，是上一代GPT-5.6 Cyber的继任者。据其描述，GPT-6 Cyber在Firefox代码审查中发现81个此前未知的高危漏洞，还为30个已知漏洞标注了更高严重程度并提供候选补丁；在Linux内核研究中复现了1724个漏洞，其中948个产出可用提权利用程序。但目前无OpenAI官方发布信息佐证，相关内容属于传闻。

rss · 夕小瑶科技说 · Nov 6, 01:50

**「为什么重要」** 若该模型能力属实，其在高危漏洞挖掘、验证及补丁辅助生成上的表现，将体现AI在网络安全工程场景的实用化进展，为代码安全审计、漏洞响应流程提供新参考。但需注意当前信息未获官方验证。

**「可关注」** 可关注：OpenAI官方后续是否会对GPT-6 Cyber的发布及能力做公开说明，以核实相关传闻的真实性。

**Tags**: `#model`, `#lab`, `#industry`

---

## AI Deals

<a id="item-ai-deals-1"></a>
### [本周Epic免费游戏 11.6~11.12](https://www.appinn.com/eggs-261106/) ⭐️ 8.0/10

你看到的内容可能由第三方 AI 基于小众软件文章提炼总结而成，可能与原文真实意图存在偏差。不代表小众软件观点和立场。请&lt;a href=&quot;https://www.appinn.com/eggs-261106/&quot; target=&quot;\_blank&quot;&gt;点击链接阅读原文&lt;/a&gt;细致比对和校验。&lt;br /&gt;&lt;br /&gt;本周（11.6~11.12）Epic平台开放限时免费领取活动：电脑端可领取《浮游世界/Flotsam》，安卓及iOS端可领取《巴别塔圣歌/Chants of Sennaar》（本次移动端限免存在锁区情况）；《遗忘国度：放置勇士/Idle Champions of the Forgotten Realms》全端本体长期免费，本周登录Epic版本可领取限时Morte’s Renown Pack礼包，内含5名角色、每名角色32个白金宝箱、药水及专属魔宠，需进入游戏内领取。活动截止时间为11月12日。

rss · 小众软件 · Nov 6, 08:21

**「为什么重要」** 本次限免及礼包领取窗口仅11月6日至12日有效，《浮游世界》《巴别塔圣歌》为平时需付费购买的游戏，《遗忘国度》的限时角色礼包也为周期性免费获取，错过本次机会后将无法免费领取。

**「可关注」** 可关注：Epic平台本周限免的《巴别塔圣歌》移动端支持繁体中文，《浮游世界》PC端支持简体中文，领取后永久入库可离线游玩；《遗忘国度：放置勇士》本体全端长期免费，需登录Epic版本游戏内领取限时礼包。

**Tags**: `#promo`, `#limited-free`, `#free-game`

---