---
layout: default
title: "Horizon Summary: 2026-11-23 (EN)"
date: 2026-11-23
lang: en
---

> From 189 items, 5 important content pieces were selected

---

**AI Agent Engineer**
1. [OpenAI 提出困惑度与智能关联](#item-agent-engineer-1) ⭐️ 8.0/10
2. [Clover-35B-A3B 技术报告发布](#item-agent-engineer-2) ⭐️ 8.0/10
3. [HF 论文：Duopra 全双工代理模型](#item-agent-engineer-3) ⭐️ 6.0/10
4. [datasette-agent 0.7a0 发布](#item-agent-engineer-4) ⭐️ 5.8/10

**AI Deals**
1. [ChatGPT Pro 日区学生版 750 日元/月](#item-ai-deals-1) ⭐️ 7.0/10

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [OpenAI 提出困惑度与智能关联](https://openai.com/index/perplexity-and-intelligence/) ⭐️ 8.0/10

OpenAI 于 2026-11-22 发布博客文章《Perplexity and Intelligence》，讨论模型困惑度与智能的关联。据 Hacker News 讨论引述，文章提出交叉熵损失趋势在强化学习训练后仍持续存在，为 LLM 评估提供简单基准，并直接影响推理模型评估方法。社区评论中，微软 Mustafa Suleyman 分享 MAI-2 Base 在 OpenAI 评估集上的 log-perplexity 为 0.819，称与 GPT-5.6 Sol base 处于同一区间。该文章具体实验细节与定义未在材料中完整披露。

hackernews · acossta · Nov 22, 17:06 · [Discussion](https://news.ycombinator.com/item?id=50601525)

**「为什么重要」** 该文将困惑度与智能直接关联，为 LLM 评估提供新视角。交叉熵损失在 RL 训练后仍呈现清晰趋势这一观察，对推理模型评估基准的选择具有参考价值。

**「可关注」** 可关注：即便在强化学习训练广泛使用后，交叉熵损失趋势仍清晰可辨，提示简单语言建模指标在推理模型评估中仍具参考价值。

**「评论」** 社区认可困惑度作为智能代理指标的直观性，并讨论交叉熵趋势在 RL 时代仍持续存在的意外性。微软通过 Mustafa Suleyman 公开 MAI-2 Base 的 log-perplexity 数据，显示行业对共享评估基准的兴趣上升。

**Tags**: `#eval`, `#llm`, `#metrics`, `#reasoning`, `#openai`

---

<a id="item-agent-engineer-2"></a>
### [Clover-35B-A3B 技术报告发布](https://huggingface.co/papers/2611.24636) ⭐️ 8.0/10

2026年11月23日Hugging Face Daily Papers发布Clover-35B-A3B-Preview技术报告，该模型为35B总参数、3B激活参数的混合专家扩散语言模型，支持思维模式生成。其采用修改后的块扩散架构，将门控Delta网络适配至块扩散框架，结合先前生成上下文的循环记忆与当前块内双向softmax注意力，历史记忆读出与当前块token在共享softmax中竞争，同时配备可学习块大小校准与零初始化右上下文卷积分支。该模型在7项agent基准测试中领先，SWE-bench Verified得分73.6、Terminal-Bench 2.1得分51.7，单块NVIDIA GB300 GPU以BF16精度运行内部agent工作负载时，reported生成速度达680 tokens/s。

rss · Hugging Face Daily Papers · Nov 23, 00:00

**「为什么重要」** 该模型首次将混合专家与扩散架构结合并落地到agent场景，公开的基准得分与reported单卡生成速度指标为coding agent的模型选型、推理优化提供了可直接参考的实测数据；目前公开数据未披露其训练成本、开源计划及公开工作负载下的实际表现，相关影响尚未证实。

**「可关注」** 可关注：Clover的块扩散架构设计（门控Delta网络适配、循环记忆与双向注意力结合、双分支结构）以及reported单GB300卡680 tokens/s的生成速度，可作为coding agent模型优化与性能评估的参考基准。

**Tags**: `#coding-agent`, `#eval`, `#memory`

---

<a id="item-agent-engineer-3"></a>
### [HF 论文：Duopra 全双工代理模型](https://huggingface.co/papers/2611.25773) ⭐️ 6.0/10

2026年11月23日，Hugging Face每日论文发布arXiv论文截断预览，介绍Duopra全双工代理模型。该模型统一学习对话控制与任务执行能力。可验证关键细节：现有实时代理harness（含Realtime-Venus-Audio + Harness）在Full-Duplex-Bench v3（FDB v3）测试中，大部分失败发生在领域工具执行之前。前后端分离的全双工代理架构中，前端负责决定是否发起请求、请求内容，后端负责执行，未发送或不完整的请求会误导后端执行。当前预览缺少完整技术规格、性能基准与实现细节，无法验证Duopra的实际效果，主要影响代理开发、harness搭建、工具调用与编排方向的工程师。

rss · Hugging Face Daily Papers · Nov 23, 00:00

**「为什么重要」** 该研究明确指出现有实时代理harness的高频故障点位于工具执行前的请求发起环节，可直接指导现有harness的故障定位与优化方向。但Duopra的具体性能与落地可行性尚未公开，暂无法确认其实际价值。

**「可关注」** 可关注：前后端分离架构的全双工代理中，前端请求生成与补全逻辑是现有harness的主要故障来源，优化时可优先排查该环节的稳定性。

**Tags**: `#agent`, `#harness`, `#eval`, `#tool-use`, `#orchestration`

---

<a id="item-agent-engineer-4"></a>
### [datasette-agent 0.7a0 发布](https://github.com/datasette/datasette-agent/releases/tag/0.7a0) ⭐️ 5.8/10

datasette-agent 0.7a0 alpha版本于2026-11-23由simonw发布，最低兼容datasette&gt;=1.0a44。本次更新新增system\_prompt插件设置，用户自定义的指令会追加在默认系统提示词之后，默认工具使用指引仍生效，该配置适用于聊天助手、后台agent以及带-c配置文件启动的datasette agent chat。同时优化了agent索引、对话和后台agent页面的消息输入框，页面加载时自动聚焦。该版本为alpha小功能更新，无性能数据或架构变更，影响面较窄。

github · simonw · Nov 23, 02:38

**「为什么重要」** 新增的system\_prompt配置项为开发者自定义agent指令提供了官方支持，对agent配置设计有参考价值，但当前仅为alpha版本的小范围功能更新，尚未验证大规模使用效果。

**「可关注」** 该版本的system\_prompt配置将自定义内容追加在默认提示词后，未覆盖默认工具使用指引，自定义agent系统提示词时可参考这种优先级保留的设计。

**Tags**: `#coding-agent`, `#harness`

---

## AI Deals

<a id="item-ai-deals-1"></a>
### [ChatGPT Pro 日区学生版 750 日元/月](https://www.v2ex.com/t/1258879#reply12) ⭐️ 7.0/10

V2EX 用户 mouseman 分享，谷歌日区完成学生认证后可订阅 ChatGPT Pro 学生版，月费 750 日元（约 30 元人民币），权益与 20 美元正价版一致，支持 4 系列模型，据称该优惠可持续 4 年。

rss · V2EX Hot · Nov 22, 05:44

**「为什么重要」** 该优惠月费仅为正价的约四分之一，权益无差异，对符合谷歌日区学生认证条件的用户有实际订阅价值。

**「可关注」** 可关注：需先完成谷歌日区学生认证，优惠据称可持续 4 年，支持 4 系列模型，权益与 20 美元正价版一致。

**Tags**: `#student`, `#promo`

---