---
layout: default
title: "Horizon Summary: 2026-11-15 (ZH)"
date: 2026-11-15
lang: zh
---

> 从 186 条内容中筛选出 8 条重要资讯。

<nav id="ah-toc" class="ah-toc" aria-label="目录"><span class="ah-toc-title">目录</span><ul><li><a href="#sec-harness-arch"><span class="ah-toc-name">Harness 架构</span><span class="ah-toc-count">1条</span></a></li><li><a href="#sec-agent-engineer"><span class="ah-toc-name">Agent 工程师日报</span><span class="ah-toc-count">3条</span></a></li><li><a href="#sec-ai-daily"><span class="ah-toc-name">AI 日报</span><span class="ah-toc-count">1条</span></a></li><li><a href="#sec-ai-deals"><span class="ah-toc-name">AI 羊毛</span><span class="ah-toc-count">3条</span></a></li></ul></nav>

---

**[Harness 架构](#sec-harness-arch)**
1. [browser-use 1.0.5 发布](#item-harness-arch-1) ⭐️ 5.5/10

**[Agent 工程师日报](#sec-agent-engineer)**
1. [Antigravity /teamwork 功能更新](#item-agent-engineer-1) ⭐️ 7.0/10
2. [datasette-llm 0.1a11 支持 OpenAI 兼容端点](#item-agent-engineer-2) ⭐️ 5.8/10
3. [inspect\_ai 0.3.290 发布](#item-agent-engineer-3) ⭐️ 5.5/10

**[AI 日报](#sec-ai-daily)**
1. [收购后李飞飞苏姿丰 CoRL 2026 首次同台](#item-ai-daily-1) ⭐️ 5.0/10

**[AI 羊毛](#sec-ai-deals)**
1. [aidou.studio 语音面试陪练 100 分钟免费](#item-ai-deals-1) ⭐️ 7.0/10
2. [x6o4 RSS Cloud 送 Kindle 推送试用码](#item-ai-deals-2) ⭐️ 7.0/10
3. [免费 Wiktionary 词典 API 上线](#item-ai-deals-3) ⭐️ 7.0/10

---

## Harness 架构
{: #sec-harness-arch .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-harness-arch" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-harness-arch-1"></a>
### [browser-use 1.0.5 发布](https://github.com/browser-use/browser-use/releases/tag/1.0.5) ⭐️ 5.5/10

browser-use 1.0.5 为浏览器代理运行流程新增内置模型评判机制。每次运行自动调用用户配置的模型对任务完成情况进行评判，结果写入 \`result.judgement\` 字段，包含成功状态、失败原因、提示词注入检测、机器人拦截检测及站点反制细节（gotchas）。评判者可访问运行轨迹、最终截图和页面内容（除非禁用视觉），并通过 \`judge\_context\` 注入自定义标准或通过 \`judge=False\` 关闭该功能。

github · sarath-menon · 11月14日 08:24

**「设计要点」** 评判器直接读取运行时的 trace、截图和最终页面。配置层通过 \`judge\_context\` 注入标准、\`judge=False\` 关闭，并恢复 0.x 版本 \`use\_judge\` / \`ground\_truth\` 兼容。

**「改了什么」** 新增默认开启的模型评判通道，自动填充结构化评判结果。站点反制边缘检测从 6/15 提升至 15/15，clean run 误报率 2/24，同时恢复 0.x 版本 \`use\_judge\` / \`ground\_truth\` 配置兼容。

**标签**: `#eval`, `#tools`

---

## Agent 工程师日报
{: #sec-agent-engineer .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-agent-engineer" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-agent-engineer-1"></a>
### [Antigravity /teamwork 功能更新](https://research.google/blog/advancing-science-engineering-with-antigravitys-teamwork-feature/) ⭐️ 7.0/10

2026 年 11 月 14 日 Google Research 发布博客，更新 Antigravity /teamwork 多 agent 协作功能在复杂科研、数学、编码、工程任务上的落地用例。Antigravity 团队成员确认该功能正在持续迭代，相关更新将逐步推送给外部用户，后续会公开动态组建 agent 团队的更多细节。当前公开材料未披露该功能的深层技术实现细节或性能数据，相关更新主要面向 agent 编排与 harness 设计领域的工程师。

hackernews · acossta · 11月14日 13:20 · [社区讨论](https://news.ycombinator.com/item?id=50496811)

**「为什么重要」** 这是官方公开的 Antigravity 多 agent 协作功能在复杂技术任务场景的落地案例，为 agent 编排与 harness 设计提供了可参考的实践方向；后续公开的动态 agent 组队细节若正式落地，可能进一步降低多 agent 系统的搭建成本。

**「可关注」** 可关注：Antigravity /teamwork 的动态 agent 组队方案细节尚未公开，当前公开材料也未披露其技术实现与性能数据，社区对其与 Claude 动态工作流的能力差异存在讨论。

**「评论」** 社区共识是团队式多 agent 工作流在复杂任务上有实用价值，已有相关研究与实践验证；分歧点在于 Antigravity /teamwork 与 Claude 动态工作流的能力差异、该功能当前的成熟度，以及多 agent 流程中审计环节的可靠性问题。

**标签**: `#harness`, `#coding-agent`, `#orchestration`

---

<a id="item-agent-engineer-2"></a>
### [datasette-llm 0.1a11 支持 OpenAI 兼容端点](https://github.com/datasette/datasette-llm/releases/tag/0.1a11) ⭐️ 5.8/10

datasette-llm 0.1a11 于 2026-11-14 发布，新增 OpenAI 兼容端点直接配置能力。用户可通过 YAML 的 \`endpoints\` 字段注册本地或第三方模型，指向 Chat Completions 或 Responses API，无需额外 LLM 插件。该版本要求 LLM 0.37.1 或更高版本，且仍处于 alpha 阶段，主要面向 Datasette 数据探索生态，对主流 agent 工程框架的影响面较窄。配置中显式 \`key\` 不再回退到 provider 默认凭证，需通过 \`datasette-secrets\` 或 LLM stored keys 显式管理。

github · simonw · 11月14日 23:59

**「可关注」** 可关注：配置 OpenAI 兼容端点时，\`key\` 字段优先查找 \`datasette-secrets\` 与 LLM stored keys，且显式指定 \`key\` 后不再回退到 provider 默认凭证，需显式管理密钥以避免 \`NeedsKeyException\`。

**标签**: `#harness`

---

<a id="item-agent-engineer-3"></a>
### [inspect\_ai 0.3.290 发布](https://github.com/UKGovernmentBEIS/inspect_ai/releases/tag/0.3.290) ⭐️ 5.5/10

英国政府 BEIS 官方于 2026 年 11 月 14 日发布 inspect\_ai 0.3.290 版本，该版本标记日期为 2026-11-13。本次更新聚焦 agent 可观测性、评估准确性和模型覆盖三个方向：新增 in-flight 模型调用事件 ID 查询能力，保证消息在 agent bridge 与日志中 ID 唯一，工具事件可关联对应消息；修正排除 epoch 不参与聚合的问题，为排除/归零结果增加分数原因，修复错误/取消评估的总样本数丢失问题；新增 Gemini 4 Carbon、Gemini 4 Hydrogen、Meta Muse Ember 1.0、Muse Wonder 1.0、Mistral Large 4 的模型支持；同时修复桥接代理达调用限制后无法发起模型调用、异步 fsspec 读阻塞事件循环等多项 bug。该版本面向使用 inspect\_ai 开展 agent 评估、harness 开发、agent 工具链建设的工程师。

github · github-actions\[bot\] · 11月14日 21:14

**「为什么重要」** 本次更新的改动均直接对应 agent 评估与 harness 场景的核心生产痛点，可观测性、评估可信度、模型覆盖的改进无需额外适配即可落地到现有 eval pipeline，可降低调试成本、提升结果可信度。

**「可关注」** 可关注桥接代理调用限制后的模型调用 bug 修复、排除 epoch 聚合逻辑修正、分数原因状态扩展三类改动，可优先用于提升现有 eval 流程的稳定性和结果可解释性。

**标签**: `#harness`, `#eval`, `#observability`, `#orchestration`

---

## AI 日报
{: #sec-ai-daily .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-daily" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-daily-1"></a>
### [收购后李飞飞苏姿丰 CoRL 2026 首次同台](https://mp.weixin.qq.com/s?__biz=MzA3MzI4MjgzMw==&amp;mid=2651074456&amp;idx=2&amp;sn=96fd9bd0e55a35b655b0a2dddd61264d) ⭐️ 5.0/10

二手媒体报道，2026 年 11 月 12 日 CoRL 2026 大会第三天，刚被 AMD 以约 82 亿美元全股票收购的 World Labs 创始人李飞飞，与 AMD 董事长兼 CEO 苏姿丰完成收购后首次公开同台对谈，对谈时长约半小时。苏姿丰称物理 AI 尤其是机器人是未来几年数千亿美元量级的机会，收购 World Labs 是为加深对工作负载的理解以推动软硬件协同优化。李飞飞提出 AI 与计算已根本融合，直言「AI 就是计算，计算就是 AI」，多模态模型正走向融合，需软硬件协同演化，同时提及 AI 正成为科研工具。本次对谈未披露全部核心细节，交易预计 2026 年底前完成交割，届时李飞飞将出任 AMD 执行副总裁兼首席科学家，直接向苏姿丰汇报。

rss · 机器之心 · 11月14日 03:34

**「为什么重要」** 这是 AMD 收购 World Labs 后双方核心人物的首次公开同台，释放了 AMD 加注物理 AI、推动软硬件协同优化的战略信号，对谈覆盖学界算力短缺、机器人技术路线等当前行业核心议题。

**「可关注」** 可关注：机器人物理 AI 领域的软硬件协同设计、学界算力供给缺口正成为行业公开讨论的核心议题。

**标签**: `#industry`, `#event`, `#lab`

---

## AI 羊毛
{: #sec-ai-deals .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-deals" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-deals-1"></a>
### [aidou.studio 语音面试陪练 100 分钟免费](https://www.v2ex.com/t/1257121#reply10) ⭐️ 7.0/10

独立开发者 cryptitalk 推出 AI 语音面试陪练工具 aidou.studio，提供最高 100 分钟免费通话额度：无登录可直接体验 10 分钟，完成 Google 账号验证后额外赠送 90 分钟。用户打开指定链接即可参与体验，材料未提及额度有效期。

rss · V2EX Hot · 11月14日 15:19

**「为什么重要」** 该工具采用全双工实时对话模式，支持用户停顿思考时等待、AI 发言过长时可随时打断，区别于传统分段回复的 AI 面试工具，目前提供技术面试官 Alex、英语口语私教 Emma 两类陪练角色，可适配系统设计、项目深挖、英语口语练习等不同面试练习需求。

**「可关注」** 可关注：无登录即可体验 10 分钟全双工对话功能，完成 Google 账号验证后额外获得 90 分钟时长，开发者设置 5 分钟真人验证环节是为避免语音模型计费被薅，未说明额度有效期与使用限制。

**标签**: `#free-tier`, `#promo`, `#limited-free`

---

<a id="item-ai-deals-2"></a>
### [x6o4 RSS Cloud 送 Kindle 推送试用码](https://www.v2ex.com/t/1257010#reply6) ⭐️ 7.0/10

V2EX 开发者 VeeSong 发放 100 个 x6o4 RSS Cloud 7 天试用码，该工具支持将 RSS 内容推送至 Kindle 阅读，还可对接 AI agent 实现自动化推送。领取需通过微信小程序扫码登录，无公开截止时间，用完的试用名额后续会释放。此外还放出 20 个 x6o4 Reader 去广告会员兑换码，可直接使用。

rss · V2EX Hot · 11月14日 03:18

**「为什么重要」** 当前主流自部署 RSS 服务（如 miniflux、FreshRSS）在 Kindle 上的阅读体验不佳，该工具专门优化了电纸书适配页面，还支持通过 AI agent 简化推送流程，适合有 Kindle 阅读 RSS 需求的用户零成本体验。

**「可关注」** 可关注：该工具配套 skill 已开源至 GitHub，可 fork 后对接自部署 RSS 服务器，调整适配其他电纸书设备。

**标签**: `#limited-free`, `#promo`

---

<a id="item-ai-deals-3"></a>
### [免费 Wiktionary 词典 API 上线](https://api.suvankar.cc/docs/dictionary) ⭐️ 7.0/10

HN 用户 suvankar\_m 发布免费词典 API，数据源自 Wiktionary，无需 API 密钥即可调用。当前公开材料未提及该 API 的配额、速率限制及服务过期时间。

rss · HN Free API / Credits · 11月14日 06:30

**「为什么重要」** 当前公开可用的无密钥词典 API 较少，该服务基于开源 Wiktionary 数据，可免配置直接接入开发测试，但无官方限流与长期可用性承诺。

**「可关注」** 可关注：该 API 无需 API 密钥即可调用，但未公开配额、速率限制与过期规则，生产环境使用前需自行验证稳定性。

**标签**: `#free-tier`, `#api`

---