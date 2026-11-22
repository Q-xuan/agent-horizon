---
layout: default
title: "Horizon Summary: 2026-11-23 (EN)"
date: 2026-11-23
lang: en
---

> From 125 items, 3 important content pieces were selected

---

**Agent Harness Architecture**
1. [browser-use 1.0.8 发布](#item-harness-arch-1) ⭐️ 5.3/10

**AI Agent Engineer**
1. [OpenAI 讨论困惑度与智能相关性](#item-agent-engineer-1) ⭐️ 7.0/10

**AI Daily**
1. [OpenAI 博客：困惑度与智能](#item-ai-daily-1) ⭐️ 6.8/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [browser-use 1.0.8 发布](https://github.com/browser-use/browser-use/releases/tag/1.0.8) ⭐️ 5.3/10

这是浏览器代理框架browser-use的1.0.8补丁版本，发布于2026年11月22日，聚焦运行时行为、工具链、安全、评测流程的定向修复，无重大架构或破坏性变更。本次更新修复了judge多轮调用重复计费、无头机/SSH环境无API key时的授权流程、DeepSeek与Qwen思考模式步数限制下无法返回答案、\`bu.type\`泄露密码字段值、\`Browser\(cdp\_url=...\)\`连接时打开新空白标签页、网关输出token预留过高导致小额余额运行中断的问题。

github · gregpr07 · Nov 22, 03:30

**「改了什么」** \1. 修复judge作为额外运行轮次调用时重复计费问题，复用缓存运行结果返回相同判决字段；2. 新增无头机/SSH环境下无API key的授权流程，运行打印链接和验证码供其他设备审批后继续；3. 修复DeepSeek、Qwen思考模式下步数限制时强制最终调用导致无法返回答案的问题，改为非强制重试；4. 修复\`bu.type\`打印密码字段值、\`Browser\(cdp\_url=...\)\`连接时打开新空白标签页的问题；5. 调整Browser Use网关输出token预留量从32768降至16384，避免小额余额运行中途被拒。

**Tags**: `#runtime`, `#tools`, `#permissions`, `#eval`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [OpenAI 讨论困惑度与智能相关性](https://openai.com/index/perplexity-and-intelligence/) ⭐️ 7.0/10

2026年11月22日OpenAI发布官方文章，讨论模型困惑度与智能的相关性，提出困惑度可作为模型能力的简单基准，背景是RL训练的推理模型逐步普及。该文章在Hacker News获得424点、292条评论，社区围绕困惑度定义、交叉熵损失在RL时代的有效性、特定能力与困惑度的对应关系展开讨论。目前尚无公开信息确认该结论对AI Agent工具链的具体落地影响。

hackernews · acossta · Nov 22, 17:06 · [Discussion](https://news.ycombinator.com/item?id=50601525)

**「为什么重要」** 该讨论挑战了“RL训练将完全取代交叉熵损失”的行业预期，为模型能力评估提供了极简替代指标，目前已被社区广泛讨论。但困惑度与具体任务能力的普适对应关系、对Agent场景的适用性均未得到实证确认。

**「可关注」** 可关注：困惑度作为轻量模型能力指标的可行性，以及交叉熵损失在RL训练流程中的实际权重变化，这两点目前存在社区认知与实证趋势的张力。

**「评论」** 社区共识倾向于认可困惑度作为通用预测指标的合理性，但分歧集中在“特定能力在固定困惑度阈值下涌现”的普适性，以及困惑度对不同领域任务的适配性。部分开发者认为困惑度定义简单，比当前复杂的评估基准更易落地。

**Tags**: `#eval`, `#observability`, `#orchestration`

---

## AI Daily

<a id="item-ai-daily-1"></a>
### [OpenAI 博客：困惑度与智能](https://openai.com/index/perplexity-and-intelligence) ⭐️ 6.8/10

OpenAI 发布博客文章，解释困惑度（perplexity）衡量 AI 模型进展的机制，并探讨其作为评估新兴能力共享指标的可能性。该文属方法论探讨，未发布新模型或具体技术细节。

rss · OpenAI Blog · Nov 22, 00:00

**「为什么重要」** 文章提出建立统一评估框架的思路，但当前仅为概念性讨论，尚无落地实现或行业共识。

**「可关注」** 可关注：困惑度作为语言模型评估指标的适用边界与跨能力泛化讨论。

**Tags**: `#eval`, `#lab`, `#model`

---