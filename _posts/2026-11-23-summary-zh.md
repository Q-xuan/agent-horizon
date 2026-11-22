---
layout: default
title: "Horizon Summary: 2026-11-23 (ZH)"
date: 2026-11-23
lang: zh
---

> 从 125 条内容中筛选出 3 条重要资讯。

<nav id="ah-toc" class="ah-toc" aria-label="目录"><span class="ah-toc-title">目录</span><ul><li><a href="#sec-harness-arch"><span class="ah-toc-name">Harness 架构</span><span class="ah-toc-count">1条</span></a></li><li><a href="#sec-agent-engineer"><span class="ah-toc-name">Agent 工程师日报</span><span class="ah-toc-count">1条</span></a></li><li><a href="#sec-ai-daily"><span class="ah-toc-name">AI 日报</span><span class="ah-toc-count">1条</span></a></li></ul></nav>

---

**[Harness 架构](#sec-harness-arch)**
1. [browser-use 1.0.8 发布](#item-harness-arch-1) ⭐️ 5.3/10

**[Agent 工程师日报](#sec-agent-engineer)**
1. [OpenAI 困惑度与智能文章引讨论](#item-agent-engineer-1) ⭐️ 7.0/10

**[AI 日报](#sec-ai-daily)**
1. [OpenAI 发布困惑度评估方法博客](#item-ai-daily-1) ⭐️ 6.8/10

---

## Harness 架构
{: #sec-harness-arch .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-harness-arch" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-harness-arch-1"></a>
### [browser-use 1.0.8 发布](https://github.com/browser-use/browser-use/releases/tag/1.0.8) ⭐️ 5.3/10

browser-use 1.0.8 是浏览器代理工具链的补丁版本，针对运行时、工具、安全、评测流程做定向修复，无重大架构或破坏性变更。修复内容包括：judge 多轮调用时复用缓存避免重复计费；无头机/SSH 场景支持跨设备链接授权；DeepSeek 和 Qwen 思考模式下遇到步数限制不再强制最终调用，可正常返回答案；同时修复密码字段值泄露、CDP 地址连接时错误打开新标签页、网关输出 token 预留过高导致小额余额中断运行的问题。

github · gregpr07 · 11月22日 03:30

**「改了什么」** 本次补丁共修复 6 个具体问题，覆盖计费逻辑、无头机授权、思考模式模型适配、敏感信息防护、CDP 连接行为、额度预留策略，无破坏性变更。

**标签**: `#runtime`, `#tools`, `#permissions`, `#eval`

---

## Agent 工程师日报
{: #sec-agent-engineer .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-agent-engineer" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-agent-engineer-1"></a>
### [OpenAI 困惑度与智能文章引讨论](https://openai.com/index/perplexity-and-intelligence/) ⭐️ 7.0/10

2026 年 11 月 22 日 OpenAI 发布《Perplexity and Intelligence》文章，提出模型困惑度与智能存在正相关，可作为模型能力的简单基准，即便在强化学习训练的推理模型兴起的背景下，困惑度仍能清晰反映模型能力趋势。该内容在 Hacker News 获得 424 点、292 条评论，引发社区对评估方法的讨论，相关结论尚未被广泛验证，对模型评估、AI agent 工具链开发有参考意义。

hackernews · acossta · 11月22日 17:06 · [社区讨论](https://news.ycombinator.com/item?id=50601525)

**「为什么重要」** 当前模型评估方法日益复杂，该文章提出的简单基准思路引发高热度讨论，但困惑度与智能的普适对应关系、以及是否适用于 agent 工具链的评估场景，尚未得到证实。

**「可关注」** 可关注：困惑度作为轻量评估指标与强化学习训练范式的能力反映一致性，以及该指标是否适配 agent 工具链的观测与评估场景。

**「评论」** 社区存在共识与分歧：部分用户认同困惑度作为简单基准的合理性，也有用户质疑专项训练模型的通用困惑度与特定能力的对应关系，同时有用户对 GPT 4.5 的相关表现提出疑问。

**标签**: `#eval`, `#observability`, `#orchestration`

---

## AI 日报
{: #sec-ai-daily .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-daily" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-daily-1"></a>
### [OpenAI 发布困惑度评估方法博客](https://openai.com/index/perplexity-and-intelligence) ⭐️ 6.8/10

2026 年 11 月 22 日，OpenAI 发布官方博客，解释困惑度（perplexity）衡量 AI 模型进展的机制，提出该指标可帮助开发者建立评估新兴能力的共享方法。

rss · OpenAI Blog · 11月22日 00:00

**「为什么重要」** 当前 AI 能力评估标准分散，该博客提出的困惑度评估思路或为行业提供统一的参考框架。

**「可关注」** 可关注：困惑度作为评估指标在衡量模型新兴能力上的应用思路。

**标签**: `#eval`, `#lab`, `#model`

---