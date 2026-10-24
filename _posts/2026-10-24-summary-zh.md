---
layout: default
title: "Horizon Summary: 2026-10-24 (ZH)"
date: 2026-10-24
lang: zh
---

> 从 175 条内容中筛选出 12 条重要资讯。

<nav id="ah-toc" class="ah-toc" aria-label="目录"><span class="ah-toc-title">目录</span><ul><li><a href="#sec-harness-arch"><span class="ah-toc-name">Harness 架构</span><span class="ah-toc-count">4条</span></a></li><li><a href="#sec-agent-engineer"><span class="ah-toc-name">Agent 工程师日报</span><span class="ah-toc-count">2条</span></a></li><li><a href="#sec-ai-daily"><span class="ah-toc-name">AI 日报</span><span class="ah-toc-count">3条</span></a></li><li><a href="#sec-ai-deals"><span class="ah-toc-name">AI 羊毛</span><span class="ah-toc-count">3条</span></a></li></ul></nav>

---

**[Harness 架构](#sec-harness-arch)**
1. [Codex rust-v0.164.0 发布](#item-harness-arch-1) ⭐️ 8.3/10
2. [Goose v1.56.0 发布](#item-harness-arch-2) ⭐️ 7.8/10
3. [pydantic-ai v2.60.0 发布](#item-harness-arch-3) ⭐️ 7.8/10
4. [Anthropic 开源 knowledge-work-plugins 插件集](#item-harness-arch-4) ⭐️ 5.0/10

**[Agent 工程师日报](#sec-agent-engineer)**
1. [Kimi K3.1 Pro 发布](#item-agent-engineer-1) ⭐️ 7.0/10
2. [NVIDIA Nemotron 3.5 Bolt 4GB 发布](#item-agent-engineer-2) ⭐️ 6.0/10

**[AI 日报](#sec-ai-daily)**
1. [OpenAI frontier 训练安全](#item-ai-daily-1) ⭐️ 7.8/10
2. [OpenAI 披露 ChatGPT 亿级用户存储方案](#item-ai-daily-2) ⭐️ 6.8/10
3. [ReasoningShield 获 NeurIPS 2026 录用](#item-ai-daily-3) ⭐️ 5.0/10

**[AI 羊毛](#sec-ai-deals)**
1. [智谱 ZCode 1024 免费领 5 亿 Tokens](#item-ai-deals-1) ⭐️ 8.0/10
2. [Epic 10.23~10.29 限免游戏汇总](#item-ai-deals-2) ⭐️ 8.0/10
3. [Show HN：runtime.school 上线免费交互式 Python SQL 课](#item-ai-deals-3) ⭐️ 5.0/10

---

## Harness 架构
{: #sec-harness-arch .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-harness-arch" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-harness-arch-1"></a>
### [Codex rust-v0.164.0 发布](https://github.com/openai/codex/releases/tag/rust-v0.164.0) ⭐️ 8.3/10

OpenAI Codex CLI 发布 rust-v0.164.0。本次更新新增企业 MCP OAuth 认证、内联模型与权限控制、Kitty/Sixel 图像全屏预览、远程 Bash/Zsh 会话凭证掩码，以及 Amazon Bedrock 设置向导默认启用。修复 compaction 失败遗留部分摘要、会话恢复丢失压缩历史与线程设置、Windows 代理认证、多级配置覆盖保留，以及 macOS 沙盒路径检查加固。

github · github-actions\[bot\] · 10月23日 04:48

**「改了什么」** 新增 /presets 槽位、/model 与 /permissions 内联参数、企业 MCP OAuth 认证、远程会话凭证掩码及 Bedrock 向导默认启用。修复 compaction 残留部分摘要、resume 丢失压缩历史与线程设置、Windows 代理认证、多级 -c 配置覆盖保留，以及 macOS 沙盒路径检查加固。减少磁盘使用并更新嵌入式 JavaScript 运行时。

**标签**: `#mcp`, `#permissions`, `#memory`, `#sandbox`

---

<a id="item-harness-arch-2"></a>
### [Goose v1.56.0 发布](https://github.com/aaif-goose/goose/releases/tag/v1.56.0) ⭐️ 7.8/10

Goose v1.56.0 发布，核心改进覆盖 subagent 编排、运行时推理、缓存与记忆。新增自动 thinking level 调节、失败或取消 delegate subagent 恢复、UI 只读 subagent 会话链接。新增 GOOSE\_MAX\_CONCURRENT\_SUBAGENTS 并发限制、OSC 7501 会话状态上报、IO Intelligence provider、provider-defined cache prices、Boa JavaScript runtime 替代 PCTX code mode。同时修复 Windows 构建错误、Bedrock 空白文本、模型列表顺序等多项问题。

github · github-actions\[bot\] · 10月23日 15:49

**「设计要点」** subagent 运行时分入 GDK，全局 turn limit 作为 subagent 回退；MCP tools 提供 provider-safe 公开名称；prefix-cache 支持 provider-defined 价格；会话状态通过 OSC 7501 协议上报。

**「改了什么」** 新增 GOOSE\_MAX\_CONCURRENT\_SUBAGENTS 环境变量控制 subagent 并发上限，支持恢复失败或取消的 delegate subagent，自动调节 thinking level 改善模型推理，以 Boa JavaScript runtime 替代原有 PCTX code mode，provider 可定义缓存价格，Windows 桌面端新增 NSIS 安装器，MCP tools 名称改为 provider-safe 公开名。

**标签**: `#subagents`, `#runtime`, `#memory`, `#prefix-cache`, `#tools`

---

<a id="item-harness-arch-3"></a>
### [pydantic-ai v2.60.0 发布](https://github.com/pydantic/pydantic-ai/releases/tag/v2.60.0) ⭐️ 7.8/10

pydantic-ai v2.60.0 发布，重构工具重试 API，弃用 RetryPromptPart，改用 ToolReturnPart\(outcome=&\#x27;retried&\#x27;\) 与 RetryFeedbackPart。SummarizingCompaction 将 harness 添加的用户频道内容标记为 &lt;harness\_data&gt; 而非用户消息。ModelSelectionContext 新增 usage\_limits、deadline、run\_id、conversation\_id，BedrockConverseModel 默认 maxTokens 设为 Claude 最大输出并后台流式。新增 DockerSandbox、BoxLiteSandbox、RelevanceCompaction 等 harness 能力。

github · dsfaccini · 10月23日 01:44

**「设计要点」** 运行时层调整 Bedrock 默认 maxTokens 至 Claude 上限并后台流式。工具层弃用 RetryPromptPart，改用 ToolReturnPart\(outcome=&\#x27;retried&\#x27;\) 与 RetryFeedbackPart；记忆层在 SummarizingCompaction 中引入 &lt;harness\_data&gt; 标签隔离 harness 注入内容。

**「改了什么」** 工具重试 API 弃用 RetryPromptPart，改用 ToolReturnPart\(outcome=&\#x27;retried&\#x27;\) 与 RetryFeedbackPart；ModelSelectionContext 新增 usage\_limits、deadline、run\_id、conversation\_id。BedrockConverseModel 默认 maxTokens 提升至 Claude 上限并后台流式，同时新增 DockerSandbox、BoxLiteSandbox、RelevanceCompaction 等 harness 能力。

**标签**: `#runtime`, `#tools`, `#memory`, `#model-selection`

---

<a id="item-harness-arch-4"></a>
### [Anthropic 开源 knowledge-work-plugins 插件集](https://github.com/anthropics/knowledge-work-plugins) ⭐️ 5.0/10

这是 Anthropic 官方开源的 knowledge-work-plugins 插件集，面向知识工作者适配 Claude Cowork 与 Claude Code。该插件集用于定制工作流、工具访问与数据集成规则，当前公开内容仅含高层描述，无技术实现、版本号与架构细节。

rss · GitHub Trending Daily · 10月24日 01:19

**「改了什么」** Anthropic 首次公开该官方插件仓库，支持为 Claude 定制知识工作流、工具调用与数据集成规则，暂无版本号、接口规范与兼容性说明。

**标签**: `#tools`

---

## Agent 工程师日报
{: #sec-agent-engineer .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-agent-engineer" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-agent-engineer-1"></a>
### [Kimi K3.1 Pro 发布](https://www.kimi.ai/blog/kimi-k3-1-pro) ⭐️ 7.0/10

2026 年 10 月 23 日，Kimi K3.1 Pro 上线 Kimi API，尚未开放权重，Moonshot 承诺 2026 年 11 月 4 日前发布完整模型权重；同步推出 Highspeed 版本，速度为普通版 2-3 倍，价格翻倍（输入缓存命中价格不变）。API 定价为输入 2 美元/百万 token、输出 10 美元/百万 token，与 GPT-6.1 Sol 持平，为 Claude Opus 5.5 的一半。Moonshot 自研基准显示该模型与 Opus 5.5、GPT-6 Astra 水平相当，Artificial Analysis 给出 55 分的评分，高于 Claude Fable 5.1、GPT-6 Astra、Gemini 4 Argon 的 53 分，低于 Opus 5.5 的 58 分，是首个接近前沿的待开源权重模型。社区反馈显示该模型存在推理痕迹身份泄露（自称 Kimi by moonshot、ChatGPT，提及“评估员”、系统指令等）、数据场景工具调用过量（73 次 vs 其他模型 18 次）的问题，另有用户反馈 99 美元/月订阅套餐 47 分钟即耗尽 5 小时配额。当前材料为 Hacker News 二手讨论，非官方技术博客原文。

hackernews · Jowsey · 10月23日 16:59 · [社区讨论](https://news.ycombinator.com/item?id=50212065)

**「为什么重要」** 该模型是首个在公开基准上接近前沿的待开源权重模型，API 已上线且定价具备竞争力，Highspeed 版本提供速度选择；尚未证实的是社区报告的身份泄露、工具调用过量问题是否普遍，开源权重版本的能力是否会与 API 版本存在差异。

**「可关注」** 可关注：Kimi K3.1 Pro API 已开放调用，待开源权重模型首次在基准上接近前沿，但社区已报告推理痕迹身份泄露、数据场景工具调用过量两类 agent 相关风险，可优先验证其对现有工具链的兼容性与行为稳定性。

**「评论」** 社区反馈呈现三类观察：一是模型回复风格更直接尖锐，推理痕迹存在自称不同身份、泄露系统指令的问题；二是数据场景工具调用次数远高于同类模型（73 次 vs 18 次）是普遍观察；三是用户关注到 Moonshot 声明不会开源超过当前前沿网络攻击能力的权重，会逐步提升开源权重的网络能力，引发对开源范围限制的讨论；另有用户反馈 99 美元/月订阅套餐 47 分钟即耗尽 5 小时配额。

**标签**: `#coding-agent`, `#eval`, `#observability`, `#tool-use`, `#permissions`

---

<a id="item-agent-engineer-2"></a>
### [NVIDIA Nemotron 3.5 Bolt 4GB 发布](https://www.reddit.com/r/LocalLLaMA/comments/1xdiecx/nvidianvidianemotron35bolte4b4gb_hugging_face/) ⭐️ 6.0/10

2026 年 10 月 23 日，社区转发 NVIDIA 官方发布的 Nemotron 3.5 Bolt E4B 4GB 小语言模型。该模型基于 Gemma-4-E4B-it 进一步后训练，针对低内存、低首 Token 延迟（TTFT）场景优化，提升多轮工具调用、指令遵循与输入接地能力，面向本地/边缘低延迟 agent、设备端语音助手、嵌入式接口等场景。模型配套用于推测解码的 DFlash drafter，另有 BF16 全精度版本，权重已在 Hugging Face 公开，支持商用与非商用用途。当前无公开第三方性能基准数据，实际表现需开发者自行验证。

reddit · r/LocalLLaMA · /u/jacek2023 · 10月23日 16:13

**「为什么重要」** 该模型是官方首次针对低延迟本地/边缘 agent 场景推出的商用授权小体量模型，配套推测解码组件可降低部署时的算力与延迟优化成本，但核心能力的实际表现尚未有公开基准验证。

**「可关注」** 可关注 DFlash drafter 与该 4GB 量化版本的适配效果，以及模型多轮工具调用能力在现有 coding agent harness 中的实际通过率。

**标签**: `#coding-agent`, `#harness`

---

## AI 日报
{: #sec-ai-daily .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-daily" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-daily-1"></a>
### [OpenAI frontier 训练安全](https://openai.com/index/securing-our-frontier-model-training-environment) ⭐️ 7.8/10

OpenAI 官方博客于 2026-10-23 发布 frontier model 训练环境安全加固方案，重点加强训练与评估阶段的 containment。具体措施包括部署离线训练环境，以及开展高算力红队测试。材料未披露实施范围、受影响模型或具体技术参数。

rss · OpenAI Blog · 10月23日 10:00

**「为什么重要」** 这标志着 AI 实验室在模型训练阶段的安全隔离策略从理论框架走向具体落地。对关注 AI 安全与合规的从业者而言，这是可核对的官方政策更新。

**「可关注」** 可关注：离线环境与算力红队测试作为 containment 增强手段的具体实现方式。

**标签**: `#policy`, `#lab`, `#industry`

---

<a id="item-ai-daily-2"></a>
### [OpenAI 披露 ChatGPT 亿级用户存储方案](https://openai.com/index/scaling-storage-one-billion-users-part-two) ⭐️ 6.8/10

OpenAI 发布技术博客，披露 ChatGPT 存储基础设施扩容至支持超 10 亿用户的实现细节。方案基于 Habitat 实现可靠多租户，搭配全局缓存与 Azure Cosmos DB 优化，实现读性能提升 12 倍。

rss · OpenAI Blog · 10月23日 17:00

**「为什么重要」** 该方案是官方公开的超大规模用户存储架构工程实践，可为同类高并发场景的后端基础设施设计提供可落地的参考。

**「可关注」** 可关注：超大规模多租户存储场景下，结合全局缓存与 Azure Cosmos DB 可实现读性能数量级提升。

**标签**: `#lab`, `#industry`, `#product`

---

<a id="item-ai-daily-3"></a>
### [ReasoningShield 获 NeurIPS 2026 录用](https://mp.weixin.qq.com/s?__biz=MzIwMTc4ODE0Mw==&amp;mid=2247723647&amp;idx=2&amp;sn=b2602c1652494088a4365422d4b76d88) ⭐️ 5.0/10

上海创智学院与复旦大学团队提出 ReasoningShield，针对大推理模型思维链存在安全盲区的问题，首次定义思维链安全审核任务，构建专用数据集与评测基准，并开源 ReasoningShield-1B/3B 审核模型。该工作已被 NeurIPS 2026 Evaluations and Datasets Track 录用。当前信息来自科技媒体 PaperWeekly 的二手转述，未附官方一手发布链接，无更多可核实的核心事实细节。

rss · PaperWeekly · 10月23日 12:20

**「为什么重要」** 大推理模型普及后，仅审核最终答案无法覆盖思维链中提前泄露的有害信息，ReasoningShield 首次针对该盲区提出审核方案，为推理模型安全评估提供了新方向。

**「可关注」** 可关注：ReasoningShield 已开源 1B/3B 审核模型、专用数据集，以及论文、项目主页与 GitHub 仓库，可复现其思维链安全审核方案。

**标签**: `#eval`, `#safety`, `#research`

---

## AI 羊毛
{: #sec-ai-deals .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-deals" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-deals-1"></a>
### [智谱 ZCode 1024 免费领 5 亿 Tokens](https://www.appinn.com/zcode-1024-free-500-million-tokens/) ⭐️ 8.0/10

你看到的内容可能由第三方 AI 基于小众软件文章提炼总结而成，可能与原文真实意图存在偏差。不代表小众软件观点和立场。请点击链接阅读原文细致比对和校验。
智谱 ZCode 推出 1024 程序员节活动，用户可免费领取 5 亿 Tokens 额度，适用于 GLM-5.3 与 GLM-5.3-Flash 模型。领取无新老用户限制，额度 2026 年 10 月 23 日 23:00 生效，10 月 26 日 09:00 到期，仅本周末有效。领取方式为下载 ZCode 客户端登录后，点击左下角活动入口打开礼包即可；领取成功后若未到生效时间，客户端会显示「待生效」。

rss · 小众软件 · 10月23日 15:17

**「为什么重要」** 该额度有效期仅覆盖本周末，若近期有 coding 相关调试、小项目测试需求，刚好可在有效期内消耗，避免过期浪费。

**「可关注」** 可关注：5 亿 Tokens 为两款模型的总额度，未公布单模型分配规则，领取时需注意不要和 ZCode Start Plan 的每日 300 万/500 万 Tokens 额度混淆。

**标签**: `#credits`, `#free-tier`, `#promo`, `#limited-free`, `#api`

---

<a id="item-ai-deals-2"></a>
### [Epic 10.23~10.29 限免游戏汇总](https://www.appinn.com/eggs-261023/) ⭐️ 8.0/10

你看到的内容可能由第三方 AI 基于小众软件文章提炼总结而成，可能与原文真实意图存在偏差。不代表小众软件观点和立场。请&lt;a href=&quot;https://www.appinn.com/eggs-261023/&quot; target=&quot;\_blank&quot;&gt;点击链接阅读原文&lt;/a&gt;细致比对和校验。&lt;br /&gt;&lt;br /&gt;Epic Games 于 2026 年 10 月 23 日至 29 日开展限时免费游戏领取活动，PC 端可领取《斯盖尔仪式 / Sker Ritual》《归家 / Home – A Unique Horror Adventure》共 2 款，移动端可领取《归家》1 款；《归家》的 PC、Android、iOS 三个平台版本需分别领取才可集齐，领取流程可在浏览器中完成。

rss · 小众软件 · 10月23日 07:34

**「为什么重要」** 活动为本周限时福利，10 月 29 日后将无法免费领取；两款游戏分别主打多人合作波次生存、多结局像素恐怖叙事，可满足不同玩家的玩法需求。

**「可关注」** 可关注：《归家》三个平台版本需分别领取共 3 次才可集齐，无需安装对应客户端，浏览器即可完成领取流程。

**标签**: `#promo`, `#limited-free`

---

<a id="item-ai-deals-3"></a>
### [Show HN：runtime.school 上线免费交互式 Python SQL 课](https://www.runtime.school/) ⭐️ 5.0/10

Hacker News 用户 shadowdevil 发布 Show HN 帖，宣布 runtime.school 提供免费交互式 Python 与 SQL 课程，课程可直接在浏览器中运行。当前公开信息未披露课程具体范围、访问限制及免费时长。

rss · HN Free API / Credits · 10月23日 14:44

**「可关注」** 可关注：目前公开信息未披露课程范围、访问限制及免费时长，暂不具备可操作领取价值。

**标签**: `#promo`, `#free-course`, `#python`, `#sql`, `#show-hn`

---