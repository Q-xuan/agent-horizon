---
layout: default
title: "Horizon Summary: 2026-10-24 (EN)"
date: 2026-10-24
lang: en
---

> From 175 items, 12 important content pieces were selected

---

**Agent Harness Architecture**
1. [Codex CLI rust-v0.164.0 发布](#item-harness-arch-1) ⭐️ 8.3/10
2. [Goose v1.56.0 发布](#item-harness-arch-2) ⭐️ 7.8/10
3. [pydantic-ai v2.60.0 发布](#item-harness-arch-3) ⭐️ 7.8/10
4. [Anthropic 开源 Claude 知识工作插件集](#item-harness-arch-4) ⭐️ 5.0/10

**AI Agent Engineer**
1. [Kimi K3.1 Pro 发布](#item-agent-engineer-1) ⭐️ 7.0/10
2. [Nemotron 3.5 Bolt 4GB 发布](#item-agent-engineer-2) ⭐️ 6.0/10

**AI Daily**
1. [OpenAI  frontier 训练环境加固](#item-ai-daily-1) ⭐️ 7.8/10
2. [OpenAI 详解 ChatGPT 十亿用户存储扩展](#item-ai-daily-2) ⭐️ 6.8/10
3. [ReasoningShield 获 NeurIPS 2026 录用](#item-ai-daily-3) ⭐️ 5.0/10

**AI Deals**
1. [智谱 ZCode 1024 领 5 亿 Tokens](#item-ai-deals-1) ⭐️ 8.0/10
2. [Epic 本周限免《斯盖尔仪式》《归家》](#item-ai-deals-2) ⭐️ 8.0/10
3. [Show HN 免费Python SQL课](#item-ai-deals-3) ⭐️ 5.0/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [Codex CLI rust-v0.164.0 发布](https://github.com/openai/codex/releases/tag/rust-v0.164.0) ⭐️ 8.3/10

OpenAI Codex CLI rust-v0.164.0 adds enterprise MCP OAuth support, inline model and permission controls, terminal image previews, and credential masking for remote sessions. The release fixes compaction leaving partial summaries in conversation history and improves session resume after compression. Additional changes include a default-enabled Amazon Bedrock setup wizard and hardened sandbox path checks on macOS.

github · github-actions\[bot\] · Oct 23, 04:48

**「设计要点」** Remote Bash and Zsh snapshot sessions mask credentials from custom providers during execution, while memory compaction failures fall back without panicking and no longer retain partial summaries in conversation history. The MCP layer supports OAuth authentication requiring secrets via eligible Codex account grants or dedicated sign-in flows.

**「改了什么」** The release introduces ten \`/presets\` slots for reusable prompts, inline \`/model\` and \`/permissions\` controls, Kitty/Sixel image previews, enterprise MCP OAuth authentication, and credential masking in remote Bash and Zsh sessions. The Amazon Bedrock setup wizard now defaults to enabled, while fixes address compaction partial summaries, session resume after compression, Windows proxy authentication, and macOS sandbox path checks.

**Tags**: `#mcp`, `#permissions`, `#memory`, `#sandbox`

---

<a id="item-harness-arch-2"></a>
### [Goose v1.56.0 发布](https://github.com/aaif-goose/goose/releases/tag/v1.56.0) ⭐️ 7.8/10

Goose v1.56.0 发布，核心改进覆盖子代理编排、运行时推理、缓存与记忆。新增失败或取消的委托子代理恢复能力，支持通过 \`GOOSE\_MAX\_CONCURRENT\_SUBAGENTS\` 限制并发子代理数量，并在 UI 中提供只读子代理会话链接。运行时引入自动思维层级操作以提升模型推理质量；缓存层支持提供商定义的价格与 OpenAI Responses 的 \`prompt\_cache\_key\`；记忆层增加危险历史包含选项，并修复上下文压缩时冻结消息的可见性问题。桌面端新增 Windows NSIS 安装包，JavaScript 执行环境由 PCTX 切换为 Boa 运行时。

github · github-actions\[bot\] · Oct 23, 15:49

**「设计要点」** GDK 承担技能发现与前台子代理运行，子代理轮次限制回退到全局设置。CLI 通过 OSC 7501 上报会话状态，桌面端提供 Windows NSIS 安装包。

**「改了什么」** 子代理管理新增恢复失败/取消任务、并发数环境变量控制及 UI 会话链接。运行时增加自动思维层级操作，JavaScript 代码模式由 PCTX 迁移至 Boa。缓存支持提供商定价与 OpenAI Responses 会话级缓存键。记忆层新增危险历史包含选项，并修正压缩过程中冻结消息的保留行为。

**Tags**: `#subagents`, `#runtime`, `#memory`, `#prefix-cache`, `#tools`

---

<a id="item-harness-arch-3"></a>
### [pydantic-ai v2.60.0 发布](https://github.com/pydantic/pydantic-ai/releases/tag/v2.60.0) ⭐️ 7.8/10

pydantic-ai v2.60.0 发布，核心变更包括工具重试 API 重构、记忆压缩标注改进、模型选择上下文扩展以及 Bedrock 流式默认行为调整。\`RetryPromptPart\` 被弃用，改用 \`ToolReturnPart\(outcome=&\#x27;retried&\#x27;\)\` 与 \`RetryFeedbackPart\`。\`SummarizingCompaction\` 将 harness 添加的用户频道内容标记为 \`&lt;harness\_data&gt;\` 而非普通用户消息。\`ModelSelectionContext\` 新增 \`usage\_limits\`、\`deadline\`、\`run\_id\` 和 \`conversation\_id\` 字段，Bedrock 模型的 \`maxTokens\` 默认设为 Claude 最大输出长度并在后台流式处理。

github · dsfaccini · Oct 23, 01:44

**「设计要点」** 工具层统一重试结果表达，记忆压缩层区分 harness 数据与用户消息，模型选择层暴露更多运行时上下文。Bedrock 运行时默认启用流式传输并调整 token 上限，影响输出长度控制逻辑。

**「改了什么」** 工具重试机制弃用 \`RetryPromptPart\`，改用 \`ToolReturnPart\(outcome=&\#x27;retried&\#x27;\)\` 与 \`RetryFeedbackPart\`。记忆压缩将 harness 数据标记为 \`&lt;harness\_data&gt;\`，模型选择上下文新增 \`usage\_limits\`、\`deadline\`、\`run\_id\`、\`conversation\_id\`。Bedrock 模型默认 \`maxTokens\` 对齐 Claude 上限并后台流式传输。

**Tags**: `#runtime`, `#tools`, `#memory`, `#model-selection`

---

<a id="item-harness-arch-4"></a>
### [Anthropic 开源 Claude 知识工作插件集](https://github.com/anthropics/knowledge-work-plugins) ⭐️ 5.0/10

这是Anthropic官方开源的Claude知识工作插件集，面向Claude Cowork与Claude Code，用于将Claude定制为适配角色、团队、公司的专属知识工作工具，支持自定义工作规范、工具与数据源接入、关键工作流处理及斜杠命令。当前公开内容仅包含高层定位描述，无具体技术实现、接口定义或版本信息。

rss · GitHub Trending Daily · Oct 24, 01:19

**Tags**: `#tools`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [Kimi K3.1 Pro 发布](https://www.kimi.ai/blog/kimi-k3-1-pro) ⭐️ 7.0/10

2026年10月23日Moonshot发布Kimi K3.1 Pro及Highspeed版本，当前未开放权重，官方承诺2026年11月4日前发布完整模型权重。API输入定价2美元/百万token、输出10美元/百万token，与GPT-6.1 Sol持平，为Claude Opus 5.5的一半；Highspeed版推理速度提升2-3倍，价格翻倍，输入缓存命中价格不变。Artificial Analysis评分55，高于Claude Fable 5.1、GPT-6 Astra、Gemini 4 Argon（均为53），低于Claude Opus 5.5（58），是首个评分接近前沿闭源模型的即将开源模型。社区实测发现该模型数据任务工具调用冗余（如某数据排查任务调用73次，GPT-6.1 Sol仅18次），推理链存在身份泄露问题，会自称为Kimi by Moonshot或ChatGPT，还提及非预期的“评估员”“全局系统指南”等指令；另有用户反馈99美元/月订阅套餐47分钟即耗尽5小时配额。官方说明该模型刻意将 offensive cyber capability 控制在低于自身管线可产出上限、且低于前沿闭源模型的水平，后续会逐步提升开源模型的网络能力。本次信息来自Hacker News社区讨论及官方公开链接，非官方完整技术博客内容。

hackernews · Jowsey · Oct 23, 16:59 · [Discussion](https://news.ycombinator.com/item?id=50212065)

**「为什么重要」** 这是目前公开评分最高的即将开源大模型，定价具备竞争力，但社区已发现工具调用冗余、推理链身份泄露等直接影响 agent 工作流稳定性的问题，同时官方对网络能力的限制说明也引发开源安全性的讨论。

**「可关注」** 可关注：Kimi K3.1 Pro 推理链存在身份泄露、工具调用冗余的问题，接入 agent 工作流前需评估适配成本。

**「评论」** 社区实测确认模型推理链存在身份泄露（自称为Kimi/ChatGPT、输出非预期系统指令），数据任务工具调用次数远高于同类模型；另有用户反馈订阅配额消耗速度远超预期，还有社区用户对官方刻意限制开源模型 offensive cyber capability 的说明提出疑问。

**Tags**: `#coding-agent`, `#eval`, `#observability`, `#tool-use`, `#permissions`

---

<a id="item-agent-engineer-2"></a>
### [Nemotron 3.5 Bolt 4GB 发布](https://www.reddit.com/r/LocalLLaMA/comments/1xdiecx/nvidianvidianemotron35bolte4b4gb_hugging_face/) ⭐️ 6.0/10

2026年10月23日，社区Reddit帖子分享NVIDIA官方发布的4GB小语言模型NVIDIA-Nemotron-3.5-Bolt-E4B-4GB，该模型基于Gemma-4-E4B-it进一步后训练，优化多轮工具调用、指令遵循与输入接地能力，面向低延迟本地语音助手、交互 persona、边缘接口等场景设计，支持低内存、低首token时延（TTFT）运行，可保留资源给周边应用或模型管线。配套提供用于推测解码的DFlash草稿模型，另有BF16全精度版本，模型权重、技术报告已公开，支持商业与非商业用途。

reddit · r/LocalLLaMA · /u/jacek2023 · Oct 23, 16:13

**「为什么重要」** 该模型针对低延迟本地/边缘智能体场景专项优化，改进多轮工具调用能力并配套推测解码组件，为边缘agent的低延迟部署提供了新的可选方案。

**「可关注」** 可关注：该模型配套DFlash推测解码草稿模型，可尝试集成到低延迟本地agent harness中验证实际推理性能与工具调用表现。

**Tags**: `#coding-agent`, `#harness`

---

## AI Daily

<a id="item-ai-daily-1"></a>
### [OpenAI  frontier 训练环境加固](https://openai.com/index/securing-our-frontier-model-training-environment) ⭐️ 7.8/10

OpenAI 官方博客 10 月 23 日发布 frontier model 训练环境安全加固措施。方案涵盖离线训练环境部署与高算力红队测试两项 containment 增强手段。文章未披露具体技术参数或实施时间表。

rss · OpenAI Blog · Oct 23, 10:00

**「为什么重要」** 这是 OpenAI 首次公开训练环境隔离的具体工程方案，将实验室安全政策从原则性声明推进到可执行控制层。

**「可关注」** 可关注：离线训练环境与高算力红队测试的具体实现方式及适用范围。

**Tags**: `#policy`, `#lab`, `#industry`

---

<a id="item-ai-daily-2"></a>
### [OpenAI 详解 ChatGPT 十亿用户存储扩展](https://openai.com/index/scaling-storage-one-billion-users-part-two) ⭐️ 6.8/10

OpenAI 发布技术博客，详解 ChatGPT 存储基础设施如何扩展以支持超过 10 亿用户。核心方案包括 Habitat 的可靠多租户架构、全局缓存层，以及集成 Azure Cosmos DB。官方称读取速度提升 12 倍。材料未披露具体基线、成本变化或覆盖区域细节。

rss · OpenAI Blog · Oct 23, 17:00

**「为什么重要」** 这篇博客直接来自 OpenAI，提供了大规模存储系统设计的可参考工程细节。对于构建类似规模服务的工程师，这些架构选择具有实际参考价值。

**「可关注」** 可关注：Habitat 结合多租户与全局缓存，再对接 Azure Cosmos DB 的读取优化路径。

**Tags**: `#lab`, `#industry`, `#product`

---

<a id="item-ai-daily-3"></a>
### [ReasoningShield 获 NeurIPS 2026 录用](https://mp.weixin.qq.com/s?__biz=MzIwMTc4ODE0Mw==&amp;mid=2247723647&amp;idx=2&amp;sn=b2602c1652494088a4365422d4b76d88) ⭐️ 5.0/10

据科技媒体PaperWeekly报道，上海创智学院与复旦大学团队提出ReasoningShield研究，首次定义思维链安全审核任务，构建专用数据集与评测基准，开源ReasoningShield-1B/3B审核模型。相关研究已被NeurIPS 2026 Evaluations and Datasets Track录用，核心观点为AI最终答案安全不意味着推理过程安全，拒答不等于无安全风险。

rss · PaperWeekly · Oct 23, 12:20

**「为什么重要」** 推理模型落地过程中，仅审核最终答案无法覆盖思维链中交替出现的安全声明与有害细节，该工作首次明确了思维链安全审核的评估框架，为推理模型安全治理提供了可参考的方向。

**「可关注」** 可关注：ReasoningShield已开源1B/3B版本审核模型、对应数据集与评测基准，可参考其框架补充推理模型的安全审核流程。

**Tags**: `#eval`, `#safety`, `#research`

---

## AI Deals

<a id="item-ai-deals-1"></a>
### [智谱 ZCode 1024 领 5 亿 Tokens](https://www.appinn.com/zcode-1024-free-500-million-tokens/) ⭐️ 8.0/10

你看到的内容可能由第三方 AI 基于小众软件文章提炼总结而成，可能与原文真实意图存在偏差。不代表小众软件观点和立场。请点击链接阅读原文细致比对和校验。智谱 ZCode 推出 1024 程序员节活动，用户可免费领取 5 亿 Tokens 额度，适用于 GLM-5.3 及 GLM-5.3-Flash 模型。领取无新老用户限制，需下载 ZCode 客户端登录后点击活动入口领取。额度 2026 年 10 月 23 日 23:00 生效，2026 年 10 月 26 日 09:00 到期，仅限本周末有效；领取成功后生效前客户端会显示「待生效」。

rss · 小众软件 · Oct 23, 15:17

**「为什么重要」** 该额度无新老用户领取门槛，且有效期覆盖本周末，适合有短期模型调用、小项目调试需求的用户及时领取使用。

**「可关注」** 可关注：5 亿 Tokens 为活动总额度，未说明两款模型各自分配比例，不能理解为每款模型各得 5 亿 Tokens；同时不可与 ZCode Start Plan 的每日额度混淆，需注意区分活动套餐与常规套餐。

**Tags**: `#credits`, `#free-tier`, `#promo`, `#limited-free`, `#api`

---

<a id="item-ai-deals-2"></a>
### [Epic 本周限免《斯盖尔仪式》《归家》](https://www.appinn.com/eggs-261023/) ⭐️ 8.0/10

你看到的内容可能由第三方 AI 基于小众软件文章提炼总结而成，可能与原文真实意图存在偏差。不代表小众软件观点和立场。请点击链接阅读原文细致比对和校验。

Epic Games 于 2026 年 10 月 23 日至 29 日开展限时免费游戏领取活动，PC 端可领取《斯盖尔仪式 / Sker Ritual》《归家 / Home – A Unique Horror Adventure》2 款游戏，移动端可领取《归家》1 款游戏，领取需前往对应 Epic 商店页面，多平台版本需分别领取。

rss · 小众软件 · Oct 23, 07:34

**「可关注」** 可关注：《归家》的 PC、Android、iOS 三个平台版本需分别领取，均支持浏览器端完成领取流程。

**Tags**: `#promo`, `#limited-free`

---

<a id="item-ai-deals-3"></a>
### [Show HN 免费Python SQL课](https://www.runtime.school/) ⭐️ 5.0/10

A Show HN post by user shadowdevil announces that free interactive Python and SQL courses running directly in the browser are available at runtime.school. The source material does not include details on course scope, access restrictions, or the duration of the free offering.

rss · HN Free API / Credits · Oct 23, 14:44

**「为什么重要」** The offering is listed in the wool column as a free dev-focused interactive learning resource for Python and SQL, but the lack of published details on access rules and course length means it has limited actionable value as of the post date.

**「可关注」** 可关注：The post provides no information on access restrictions, course content coverage, or an end date for the free tier, so verify official terms on runtime.school before spending time on the courses.

**Tags**: `#promo`, `#free-course`, `#python`, `#sql`, `#show-hn`

---