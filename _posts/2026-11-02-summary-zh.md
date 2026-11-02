---
layout: default
title: "Horizon Summary: 2026-11-02 (ZH)"
date: 2026-11-02
lang: zh
---

> 从 148 条内容中筛选出 5 条重要资讯。

<nav id="ah-toc" class="ah-toc" aria-label="目录"><span class="ah-toc-title">目录</span><ul><li><a href="#sec-harness-arch"><span class="ah-toc-name">Harness 架构</span><span class="ah-toc-count">2条</span></a></li><li><a href="#sec-agent-engineer"><span class="ah-toc-name">Agent 工程师日报</span><span class="ah-toc-count">1条</span></a></li><li><a href="#sec-ai-daily"><span class="ah-toc-name">AI 日报</span><span class="ah-toc-count">1条</span></a></li><li><a href="#sec-ai-deals"><span class="ah-toc-name">AI 羊毛</span><span class="ah-toc-count">1条</span></a></li></ul></nav>

---

**[Harness 架构](#sec-harness-arch)**
1. [fastmcp v4.2.0a2 发布](#item-harness-arch-1) ⭐️ 6.8/10
2. [crewAI 1.15.34 发布](#item-harness-arch-2) ⭐️ 5.3/10

**[Agent 工程师日报](#sec-agent-engineer)**
1. [单 RTX 3090 Ti 本地 LLM 解码提速实践](#item-agent-engineer-1) ⭐️ 6.0/10

**[AI 日报](#sec-ai-daily)**
1. [Fysiverse-UniWAM 24 项真机评测双第一](#item-ai-daily-1) ⭐️ 5.5/10

**[AI 羊毛](#sec-ai-deals)**
1. [HikerApi 免费爬虫额度分享](#item-ai-deals-1) ⭐️ 6.0/10

---

## Harness 架构
{: #sec-harness-arch .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-harness-arch" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-harness-arch-1"></a>
### [fastmcp v4.2.0a2 发布](https://github.com/PrefectHQ/fastmcp/releases/tag/v4.2.0a2) ⭐️ 6.8/10

fastmcp v4.2.0a2 发布，这是第二个 4.2 alpha，包含 4.1.5 全部修复及 4.2 专属变更。Skills 发现支持通过代理后端分页、Prefab 后端地址在 4.2 代理中重绑定、大型工具目录 schema 展开加速、kept-alive stdio 传输按客户端超时管理。行为上，JSON Schema 的 const 和 enum 改为 JSON 相等性比较，\`true\` 不再匹配 \`1\`；\`prompts/get\` 缺参数返回 \`-32602\`；OpenAPI 上游错误截断至 1 KB 并丢弃 HTML 正文；严格输入验证拒绝未声明参数。该预发布仍标记为实验性，用于集成测试，发布前已针对 pydantic-ai、langchain、agno、Microsoft Agent Framework 和 OpenAI Agents SDK 验证。

github · zzstoatzz · 11月1日 22:58

**「设计要点」** fastmcp 将 Skill 设计为 storage-neutral 对象，folders 作为唯一加载器，并通过代理后端分页实现 Skills 发现。运行时上，kept-alive stdio 子进程按各客户端超时管理，不同超时的后续客户端会重启空闲进程，嵌套客户端则共享会话超时并记录警告；工具层在严格输入验证下拒绝未声明的 OpenAPI 参数，同时 /marvin App token 被限制在最小权限范围内。

**「改了什么」** 相对 v4.2.0a1，本版本将 JSON Schema 的 const 和 enum 比较改为 JSON 相等性，\`true\` 不再通过 \`1\` 验证；\`prompts/get\` 缺参数返回 \`-32602\`；OpenAPI 上游错误截断至 1 KB 并丢弃 HTML；严格输入验证拒绝未声明参数。Skill 变为 storage-neutral 对象，folders 作为唯一加载器；大型工具目录 schema 展开速度提升；kept-alive stdio 子进程按客户端超时管理，不同超时客户端重启空闲进程，嵌套客户端共享会话超时。

**标签**: `#mcp`, `#tools`, `#runtime`

---

<a id="item-harness-arch-2"></a>
### [crewAI 1.15.34 发布](https://github.com/crewAIInc/crewAI/releases/tag/1.15.34) ⭐️ 5.3/10

这是 crewAI agent 框架的官方 1.15.34 版本小版本发布，属于增量更新，无重大架构变更。本次更新新增 LiteLLM 目录集成、组织级技能搜索、部署 zip 支持、crewai run --inputs 透传至 Python flow 等功能，同时修复了工具执行、LLM 提供商兼容性、上下文窗口管理、登录流程等多项运行时问题，还补充了 1.15.29 版 agent executor 移除的迁移文档。

github · joaomdmoura · 11月1日 21:21

**「设计要点」** 本次更新无核心运行时、权限或记忆模块的重大架构调整，改动集中在工具链、LLM 集成和运行时行为优化层面。

**「改了什么」** 相对上一版本，新增 LiteLLM 目录集成、组织技能搜索、部署 zip 创建与对应提交哈希输出、crewai run --inputs 透传至 Python flow 能力；修复 OpenAI 兼容提供商缺 API key 报错、LiteLLM 流式错误保留原始异常、重复工具调用告警、上下文窗口回退提示、AMP 登录重试等多项运行时问题；同时移除 1.15.29 版 agent executor 并补充迁移文档。

**「评论」** 暂无社区用户反馈或讨论内容。

**标签**: `#tools`, `#runtime`

---

## Agent 工程师日报
{: #sec-agent-engineer .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-agent-engineer" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-agent-engineer-1"></a>
### [单 RTX 3090 Ti 本地 LLM 解码提速实践](https://www.reddit.com/r/LocalLLaMA/comments/1xlec67/getting_incredible_results_with_a_single_rtx/) ⭐️ 6.0/10

2026 年 11 月 1 日，Reddit 用户/u/uniVocity 分享其 6 年旧硬件的本地 LLM 推理优化实践：硬件为 AMD Ryzen Threadripper 3990X、128GB DDR4、单张 RTX 3090 Ti 24GB，通过 gpu-unlock 解除消费级 Ampere 卡的 FP16/BF16 矩阵指令固件 throttles，搭配 Xolotl 推理引擎、XQ/GSQ V2 量化、FP4 KV 缓存、Engram NVMe 表及 DSpark 投机解码，实现 DeepSeek-V4.1-Flash-1017（552B MoE，~39B 激活）约 35 tok/s 解码速度，Qwen3.8-Flash-Next（125B MoE+51B N-gram，~3.5B 激活）约 138-140 tok/s 解码速度。该方案为个人非官方实践，未提供 Agent 场景评估数据，仅适用于消费级 Ampere 卡本地推理场景。

reddit · r/LocalLLaMA · /u/uniVocity · 11月1日 21:01

**「为什么重要」** 该实践为低配消费级硬件运行大参数 MoE 模型提供了可参考的优化路径，对本地推理优化的工程师有参考价值，但尚未经过官方验证，也未覆盖 Agent 场景的性能表现。

**「可关注」** 可关注：消费级 Ampere 卡可通过 gpu-unlock 解除 FP16/BF16 矩阵指令 throttles，搭配 Xolotl 的多级内存管理与 DSpark 投机解码逻辑，可在单张 24GB 显存卡上运行大参数 MoE 模型。

**标签**: `#inference-optimization`, `#local-llm`, `#quantization`

---

## AI 日报
{: #sec-ai-daily .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-daily" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-daily-1"></a>
### [Fysiverse-UniWAM 24 项真机评测双第一](https://mp.weixin.qq.com/s?__biz=MzA3MzI4MjgzMw==&amp;mid=2651071440&amp;idx=1&amp;sn=913d398a504d3e029db48cde218437a2) ⭐️ 5.5/10

飞捷科思（Fysics AI）联合复旦大学认知与智能技术实验室（CITLab）提出统一世界动作模型 Fysiverse-UniWAM，未采用大规模机器人预训练的传统路线，基于预训练视频世界模型，通过共享骨干网络实现自主导航、移动操作与固定工位灵巧操作的联合学习，同时提出 MAP（Manipulation Anchor Pose，操作锚定位姿）方法，构建了超 150 万条轨迹、累计约 7500 小时的 MAP-Data 数据集。在 MAP-Bench 基准测试中，该模型平均位置误差 9.85 厘米，平均朝向误差 2.30°，较最强外部基线分别降低 30.1%和 44.0%。在覆盖 4 种机器人平台的 24 项真机测试中，13 项导航任务的位置误差全部排名第一，4 项移动操作任务的成功率全部第一，平均成功率达 80.0%，领先当前最强机器人预训练基线π₀.₅ 17.5 个百分点，复杂固定工位操作的整体表现也接近π₀.₅。本次信息来自机器之心的二手报道，未附官方一手链接且正文严重截断，仅能确认上述评测成绩，无更多可核对的官方发布细节。

rss · 机器之心 · 11月1日 04:00

**「为什么重要」** 该模型未依赖大规模机器人预训练即取得多类具身智能任务的领先成绩，为具身智能技术路线提供了新的可行验证方向，降低了相关技术的预训练门槛。

**「可关注」** 可关注：其从预训练视频世界模型出发、通过共享骨干网络联合学习导航与操作能力的路线，以及配套的 MAP-Data 数据集构建方式。

**标签**: `#model`, `#eval`, `#industry`

---

## AI 羊毛
{: #sec-ai-deals .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-deals" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-deals-1"></a>
### [HikerApi 免费爬虫额度分享](https://news.ycombinator.com/item?id=50327394) ⭐️ 6.0/10

Hacker News 用户 aziktazik 分享称，HikerApi 的 Instagram 公开数据抓取 API 可提供 100 次免费测试请求，付费请求单价为 0.001 美元/次；该免费额度的公开普适性、有效期及区域限制均无官方信息确认。

rss · HN Free API / Credits · 11月1日 17:00

**「为什么重要」** 该信息仅为个人使用体验分享，无官方渠道证实免费额度的公开开放规则，参考价值有限，若需使用可优先核实官方活动规则。

**「可关注」** 可关注：HikerApi 的 Instagram 抓取 API 付费单价 0.001 美元/次，使用前需验证其服务稳定性与数据抓取的合规性。

**标签**: `#credits`, `#api`, `#promo`

---