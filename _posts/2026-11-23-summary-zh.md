---
layout: default
title: "Horizon Summary: 2026-11-23 (ZH)"
date: 2026-11-23
lang: zh
---

> 从 191 条内容中筛选出 6 条重要资讯。

<nav id="ah-toc" class="ah-toc" aria-label="目录"><span class="ah-toc-title">目录</span><ul><li><a href="#sec-agent-engineer"><span class="ah-toc-name">Agent 工程师日报</span><span class="ah-toc-count">3条</span></a></li><li><a href="#sec-ai-deals"><span class="ah-toc-name">AI 羊毛</span><span class="ah-toc-count">3条</span></a></li></ul></nav>

---

**[Agent 工程师日报](#sec-agent-engineer)**
1. [OpenAI 发布困惑度与智能相关性研究](#item-agent-engineer-1) ⭐️ 7.5/10
2. [datasette-agent 0.7a0 发布](#item-agent-engineer-2) ⭐️ 6.3/10
3. [HF 日报：Duopra 全双工代理模型](#item-agent-engineer-3) ⭐️ 6.0/10

**[AI 羊毛](#sec-ai-deals)**
1. [Gemini 黑五 Pro 年付半价 99 刀](#item-ai-deals-1) ⭐️ 8.0/10
2. [ChatGPT Pro 日区学生版 750 日元/月](#item-ai-deals-2) ⭐️ 8.0/10
3. [FLEY AI 语音助手免费开源](#item-ai-deals-3) ⭐️ 8.0/10

---

## Agent 工程师日报
{: #sec-agent-engineer .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-agent-engineer" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-agent-engineer-1"></a>
### [OpenAI 发布困惑度与智能相关性研究](https://openai.com/index/perplexity-and-intelligence/) ⭐️ 7.5/10

2026 年 11 月 22 日 OpenAI 发布官方博客，实证大语言模型困惑度与模型智能存在强相关性，为模型能力评估提供简单可复用的基准。文章未明确定义困惑度，社区补充其指模型对序列下一个 token 预测的惊讶程度，最优值为 1，最差等于词表大小。该发现对 AI Agent 选型、评估管线设计的工程师有直接参考价值，微软已跟进在 OpenAI 公开评估集上报告 MAI-2 Base 的困惑度数据，与 GPT-5.6 Sol base 模型处于同一区间。

hackernews · acossta · 11月22日 17:06 · [社区讨论](https://news.ycombinator.com/item?id=50601525)

**「为什么重要」** 该研究首次由官方实证困惑度与智能的强关联，为 Agent 工程师绕开日益复杂的评估套件提供了低成本基准；但该相关性是否适用于所有经强化学习训练的推理模型，目前尚无公开验证。

**「可关注」** 可关注：困惑度可作为模型能力快速筛选的低成本指标，但需注意官方未公开评估集细节与计算规范，跨模型对比时需确认基准一致性。

**「评论」** 社区共识认可困惑度作为简单、低成本模型能力基准的价值；讨论焦点集中在三点：一是强化学习训练普及后困惑度与智能的强关联仍清晰，让部分用户感到意外，二是官方未公开评估集细节与困惑度计算规范，跨厂商模型对比的可靠性待验证，另有用户疑惑 o1 是否为真正推理模型的起点，以及 GPT-4.5 的相关表现。

**标签**: `#eval`

---

<a id="item-agent-engineer-2"></a>
### [datasette-agent 0.7a0 发布](https://github.com/datasette/datasette-agent/releases/tag/0.7a0) ⭐️ 6.3/10

2026 年 11 月 23 日，simonw 发布 datasette-agent 0.7a0 alpha 版本，最低兼容要求提升至\`datasette&gt;=1.0a44\`。本次更新新增\`system\_prompt\`插件配置项，用户自定义内容会追加到默认系统提示词后方，默认工具使用指引仍生效，该配置同时适用于聊天助手、后台代理及带\`-c\`配置文件的\`datasette agent chat\`命令。此外，代理首页、对话页和后台代理页的消息输入框会在页面加载时自动获取焦点，支持直接输入内容。相关贡献来自 Niall Smart，对应 PR \#26、\#24。

github · simonw · 11月23日 02:38

**「为什么重要」** 该版本首次提供官方原生的系统提示词自定义能力，降低了 Datasette 生态内用户定制代理行为的门槛；目前没有证据显示该变更会延伸到 Datasette 生态之外，也没有涉及性能或架构层面的调整。

**「可关注」** 可关注：\`system\_prompt\`配置项采用追加默认提示词的设计，不会覆盖内置工具使用指引，若需调整核心行为仍需修改默认提示词。

**标签**: `#harness`

---

<a id="item-agent-engineer-3"></a>
### [HF 日报：Duopra 全双工代理模型](https://huggingface.co/papers/2611.25773) ⭐️ 6.0/10

2026 年 11 月 23 日 Hugging Face 每日论文更新一篇 arXiv 预印本，提出 Duopra 全双工代理模型与配套评估基准 FDB v3。该研究指出，采用前后端分离架构的实时代理 harness（如 Realtime-Venus-Audio + Harness）在流式管线中的多数失败发生在领域工具执行前，根因是未发送请求无法被执行、不完整请求会误导后端执行逻辑。Duopra 旨在同时学习对话控制与任务执行能力，整合对话代理与任务代理功能。当前公开内容为截断版本，缺少性能数据、完整技术细节与可复现信息，主要面向代理工程、harness 设计、评估方向的研究者与工程师。

rss · Hugging Face Daily Papers · 11月23日 00:00

**「为什么重要」** 该研究明确了现有实时代理 harness 的一个可定位的具体失败节点（工具执行前），对 harness 架构优化有直接参考价值。但 Duopra 的实际性能提升、技术实现细节尚未公开完整数据，其效果暂未得到验证。

**「可关注」** 可关注：现有前后端分离架构的实时代理 harness，可优先排查工具执行前的请求发送链路、请求完整性校验环节的失效问题。

**标签**: `#harness`, `#eval`, `#coding-agent`

---

## AI 羊毛
{: #sec-ai-deals .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-deals" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-deals-1"></a>
### [Gemini 黑五 Pro 年付半价 99 刀](https://www.v2ex.com/t/1258863#reply82) ⭐️ 8.0/10

V2EX 用户 B1ankCat 分享谷歌 Gemini 黑五 Pro 订阅优惠实操流程，年付半价 99 美元，可退此前低价订阅的剩余费用，需通过手机端 Gemini APP 切换年付订阅触发优惠，后续需在 Google Play 取消自动订阅，分享者表示无需转区即可参与。

rss · V2EX Hot · 11月22日 03:49

**「为什么重要」** 分享者表示 99 美元一年的正规渠道 Gemini Pro 订阅是当前较低价格的付费选项，对有长期使用需求的用户有吸引力。

**「可关注」** 可关注：需通过手机端 Gemini APP 切换年付订阅才能触发半价优惠，完成后需在 Google Play 取消自动订阅，避免后续按原价 199 美元续费。

**标签**: `#promo`, `#subscription`, `#gemini`

---

<a id="item-ai-deals-2"></a>
### [ChatGPT Pro 日区学生版 750 日元/月](https://www.v2ex.com/t/1258879#reply12) ⭐️ 8.0/10

V2EX 用户 mouseman 分享羊毛：完成谷歌日区学生认证后可订阅 ChatGPT Pro 学生版，每月费用 750 日元（约 30 元人民币），可使用全系列 4 模型，权益与 20 美元正价 Pro 一致，据称该优惠可持续 4 年，领取条件为谷歌日区学生认证，材料未提及截止时间。

rss · V2EX Hot · 11月22日 05:44

**「为什么重要」** 正价 ChatGPT Pro 每月需支付 20 美元，该学生版优惠价仅约 30 元人民币，价格优势显著，且权益与正价版本完全一致，对持有谷歌日区学生认证资质的用户性价比极高。

**「可关注」** 可关注：仅需谷歌日区学生认证资质即可订阅，权益与正价 Pro 无差异，但优惠可持续 4 年的说法未获官方证实。

**标签**: `#student`, `#promo`, `#limited-free`, `#api`

---

<a id="item-ai-deals-3"></a>
### [FLEY AI 语音助手免费开源](https://news.ycombinator.com/item?id=50603477) ⭐️ 8.0/10

Hacker News 用户 Drfoxi 分享免费的跨平台 FLEY AI 语音助手，支持 Windows、Linux、Android 三端，可语音交互、控制设备与生成代码等，无公开费用或使用限制，可通过官网或对应平台 GitHub 仓库直接下载使用；配套开源智能眼镜项目 FLEY Glasses 1.0 基于 ESP32-S3，支持语音交互、实时视频分析等功能，代码已公开。

rss · HN Free API / Credits · 11月22日 20:17

**「为什么重要」** 当前无公开费用或使用限制，跨平台覆盖主流桌面与移动端，配套开源硬件项目可二次开发，适合需要免费语音交互工具或智能硬件试水的用户。

**「可关注」** 可关注：三端客户端与智能眼镜代码均已公开，可基于现有仓库二次开发适配自定义需求。

**标签**: `#free-tier`, `#open-source`, `#cross-platform`

---