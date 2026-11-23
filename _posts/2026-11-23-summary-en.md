---
layout: default
title: "Horizon Summary: 2026-11-23 (EN)"
date: 2026-11-23
lang: en
---

> From 191 items, 6 important content pieces were selected

---

**AI Agent Engineer**
1. [OpenAI 发布困惑度与智能关联报告](#item-agent-engineer-1) ⭐️ 7.5/10
2. [datasette-agent 0.7a0](#item-agent-engineer-2) ⭐️ 6.3/10
3. [HF 日报：Duopra 全双工代理模型](#item-agent-engineer-3) ⭐️ 6.0/10

**AI Deals**
1. [Gemini 黑五 Pro 年付半价开放](#item-ai-deals-1) ⭐️ 8.0/10
2. [ChatGPT Pro 日区学生版 月付750日元](#item-ai-deals-2) ⭐️ 8.0/10
3. [FLEY AI 语音助手开源免费](#item-ai-deals-3) ⭐️ 8.0/10

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [OpenAI 发布困惑度与智能关联报告](https://openai.com/index/perplexity-and-intelligence/) ⭐️ 7.5/10

OpenAI 官方博客（2026-11-22）发布实证研究，记录 LLM 困惑度与模型智能的强相关性。社区讨论将其定位为简单、实用的模型能力基准，对 agent 开发有直接参考价值。该趋势出乎意料，因 RL 训练推理模型已兴起，但相关性依然清晰。微软跟进报告 MAI-2 Base 在 OpenAI 评估集上的对数困惑度为 0.819，与 GPT-5.6 Sol base 模型处于同一区间。文章未公开具体实验细节、数据集或相关系数。

hackernews · acossta · Nov 22, 17:06 · [Discussion](https://news.ycombinator.com/item?id=50601525)

**「为什么重要」** 评估套件日益复杂，困惑度提供轻量、可复现的替代指标。对 agent 工程师选型或评估流程有直接参考价值，但尚未证实可替代下游任务评估。

**「可关注」** 可关注：困惑度作为预训练进度指标已被多方在同一保留集上对比，适合纳入模型选型流程的早期筛选阶段。

**「评论」** 社区对 RL 训练模型下困惑度仍与智能相关的趋势感到惊讶，但认可其作为简单基准的实用性。讨论涉及 o1 系列可能标志推理模型起点，并关注 GPT-4.5 的定位。

**Tags**: `#eval`

---

<a id="item-agent-engineer-2"></a>
### [datasette-agent 0.7a0](https://github.com/datasette/datasette-agent/releases/tag/0.7a0) ⭐️ 6.3/10

simonw 于 2026-11-23 发布 datasette-agent 0.7a0。该版本将兼容性基线提升至 datasette &gt;= 1.0a44，新增 system\_prompt 插件配置项，允许在默认系统提示后追加自定义指令，覆盖聊天助手、后台 agent 及带 -c 配置文件的 datasette agent chat。同时，agent 索引、对话和后台 agent 页面的消息输入框在页面加载时自动获得焦点。变更范围限于 Datasette 生态，未涉及更广泛的架构或性能调整。

github · simonw · Nov 23, 02:38

**「为什么重要」** 该版本提供了 agent 系统提示自定义能力，但影响面仍局限于 Datasette 插件生态，尚未看到跨框架的通用性扩展。

**「可关注」** system\_prompt 配置项将自定义文本追加到默认系统提示之后，保留了默认工具使用规范，这种扩展顺序决定了 agent 行为不会偏离既有约束。

**Tags**: `#harness`

---

<a id="item-agent-engineer-3"></a>
### [HF 日报：Duopra 全双工代理模型](https://huggingface.co/papers/2611.25773) ⭐️ 6.0/10

2026年11月23日Hugging Face每日论文更新一篇arXiv预印本，提出Duopra全双工代理模型与Full-Duplex-Bench v3（FDB v3）评估基准。研究验证了现有实时代理harness的多数失败发生在领域工具执行前，Duopra将全双工对话控制与任务执行学习整合到同一交互模型中，对代理工程、实时代理harness设计与评估领域的从业者有参考价值。当前公开内容为截断版本，缺少性能数据、完整技术细节与可复现信息，暂无法评估实际工程落地价值。

rss · Hugging Face Daily Papers · Nov 23, 00:00

**「为什么重要」** 该研究针对实时代理harness的工具执行前失败模式提出新建模思路，对相关领域的基准设计与harness优化有参考意义，但当前公开内容截断，缺少可验证的性能数据与复现信息，实际效果尚未证实。

**「可关注」** 可关注：实时代理harness的工具执行前失败是当前可验证的共性痛点，Duopra将对话控制与任务执行联合学习的思路可作为后续harness设计的参考方向。

**Tags**: `#harness`, `#eval`, `#coding-agent`

---

## AI Deals

<a id="item-ai-deals-1"></a>
### [Gemini 黑五 Pro 年付半价开放](https://www.v2ex.com/t/1258863#reply82) ⭐️ 8.0/10

V2EX 用户 B1ankCat 分享谷歌 Gemini 黑五 Pro 订阅优惠实操流程，年付半价 99 美元，可退此前低价订阅的剩余费用，需通过手机端 Gemini APP 切换年付订阅触发优惠，后续需取消自动订阅，作者表示无需转区即可参与。

rss · V2EX Hot · Nov 22, 03:49

**「为什么重要」** 该优惠为官方黑五活动，年付 99 美元的 Pro 订阅价格较常规年付 199 美元低一半，作者认为这是当前正规付费 Gemini Pro 的最优价格选择。

**「可关注」** 可关注：需通过手机端 Gemini APP 切换年付订阅才能触发半价优惠，操作完成后需在 Google Play 取消自动订阅，避免后续产生非预期扣费。

**Tags**: `#promo`, `#subscription`, `#gemini`

---

<a id="item-ai-deals-2"></a>
### [ChatGPT Pro 日区学生版 月付750日元](https://www.v2ex.com/t/1258879#reply12) ⭐️ 8.0/10

V2EX用户分享谷歌日区学生认证后可订阅ChatGPT Pro学生版，每月750日元（约30元），可使用全系列4模型，权益与20美元正价Pro一致，该优惠据称可持续4年。

rss · V2EX Hot · Nov 22, 05:44

**「为什么重要」** 该优惠为已验证可落地的羊毛，价格远低于正价Pro，适合持有谷歌日区学生认证资质的学生用户。

**「可关注」** 可关注：需持有谷歌日区学生认证资质，可使用全系列4模型，优惠据称可持续4年。

**Tags**: `#student`, `#promo`, `#limited-free`, `#api`

---

<a id="item-ai-deals-3"></a>
### [FLEY AI 语音助手开源免费](https://news.ycombinator.com/item?id=50603477) ⭐️ 8.0/10

Hacker News 用户 Drfoxi 分享免费的 FLEY AI 跨平台语音助手及配套开源智能眼镜项目。该助手支持 Windows、Linux、Android 三端，可通过 https://fleyai.base44.app/ 直接下载使用，未提及费用或使用限制，各端源码分别托管在对应 GitHub 仓库。配套 FLEY Glasses 1.0 基于 ESP32-S3 开发，支持语音指令识别、实时视频分析、照片存储、音频反馈等功能。

rss · HN Free API / Credits · Nov 22, 20:17

**「为什么重要」** 当前无公开费用或使用门槛，跨平台覆盖主流桌面与移动端，配套硬件项目也完全开源，适合想低成本体验 AI 语音交互或进行二次开发的用户。

**「可关注」** 可关注：项目全端代码已公开在 GitHub，可基于现有仓库二次开发适配自定义需求，但未提及长期维护计划。

**Tags**: `#free-tier`, `#open-source`, `#cross-platform`

---