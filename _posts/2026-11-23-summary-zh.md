---
layout: default
title: "Horizon Summary: 2026-11-23 (ZH)"
date: 2026-11-23
lang: zh
---

> 从 189 条内容中筛选出 5 条重要资讯。

<nav id="ah-toc" class="ah-toc" aria-label="目录"><span class="ah-toc-title">目录</span><ul><li><a href="#sec-agent-engineer"><span class="ah-toc-name">Agent 工程师日报</span><span class="ah-toc-count">4条</span></a></li><li><a href="#sec-ai-deals"><span class="ah-toc-name">AI 羊毛</span><span class="ah-toc-count">1条</span></a></li></ul></nav>

---

**[Agent 工程师日报](#sec-agent-engineer)**
1. [OpenAI 发布困惑度与智能关联文章](#item-agent-engineer-1) ⭐️ 8.0/10
2. [Clover-35B-A3B-Preview 技术报告发布](#item-agent-engineer-2) ⭐️ 8.0/10
3. [Duopra 全双工代理论文发布](#item-agent-engineer-3) ⭐️ 6.0/10
4. [datasette-agent 0.7a0 发布](#item-agent-engineer-4) ⭐️ 5.8/10

**[AI 羊毛](#sec-ai-deals)**
1. [ChatGPT Pro 日区学生版优惠](#item-ai-deals-1) ⭐️ 7.0/10

---

## Agent 工程师日报
{: #sec-agent-engineer .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-agent-engineer" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-agent-engineer-1"></a>
### [OpenAI 发布困惑度与智能关联文章](https://openai.com/index/perplexity-and-intelligence/) ⭐️ 8.0/10

2026 年 11 月 22 日，OpenAI 官方博客发布题为《Perplexity and Intelligence》的文章，提出困惑度与智能存在正相关，核心观察到即便模型经过强化学习（RL）训练，交叉熵损失对应的困惑度趋势仍保持清晰，讨论覆盖大模型评估指标、推理模型能力评估方向，相关讨论影响 LLM 研发、eval 领域的工程师与研究者。社区反馈显示微软已跟进采用该评估集报告基座模型困惑度，例如 MAI-2 Base 的 log 困惑度为 0.819，与 GPT-5.6 Sol 基座模型同量级。

hackernews · acossta · 11月22日 17:06 · [社区讨论](https://news.ycombinator.com/item?id=50601525)

**「为什么重要」** 已发生的是 OpenAI 官方提出困惑度-智能关联的评估思路，且已有其他厂商跟进采用相同评估集报告基座模型困惑度；尚未证实的是该指标能否成为行业通用评估标准，以及其对不同架构、任务类型模型的适用边界。

**「可关注」** 可关注：即便模型普遍采用强化学习（RL）训练，交叉熵损失对应的困惑度趋势仍保持清晰，且已有厂商尝试在统一评估集上报告基座模型困惑度，可留意该指标在自身 eval 流程中的参考价值。

**「评论」** 社区共识是困惑度作为简单可复现的评估指标具备实用价值；分歧点在于部分用户对文章未明确定义困惑度、GPT-4.5 在推理模型谱系中的定位、困惑度与推理能力的关联细节存在疑问。

**标签**: `#eval`, `#llm`, `#metrics`, `#reasoning`, `#openai`

---

<a id="item-agent-engineer-2"></a>
### [Clover-35B-A3B-Preview 技术报告发布](https://huggingface.co/papers/2611.24636) ⭐️ 8.0/10

2026 年 11 月 23 日 Hugging Face Daily Papers 发布 Clover-35B-A3B-Preview 技术报告。该模型为 35B 总参数、3B 激活参数的混合专家（MoE）扩散语言模型，支持思维链生成，采用修改后的块扩散架构：结合 Gated Delta Networks，将历史生成上下文的循环记忆与当前块内双向 softmax 注意力融合，历史记忆读出现与当前块 token 在共享 softmax 中竞争，同时配备可学习块大小校准模块与零初始化的右上下文卷积分支。该模型在 7 项 agent 基准测试中领先，SWE-bench Verified 得分 73.6，Terminal-Bench 2.1 得分 51.7，报告称单块 NVIDIA GB300 GPU、BF16 精度下内部 agent 工作负载生成速度达 680 tokens/s。该成果为 AI agent、coding agent 及 agent 评估领域的工程师提供了性能参考基线。

rss · Hugging Face Daily Papers · 11月23日 00:00

**「为什么重要」** 该模型同时公开 agent 基准得分与报告称单卡可量化的生成速度指标，相关数据直接关联 AI agent 工程改进需求，为后续模型优化与评估场景提供了可直接对比的参考基线。

**「可关注」** 可关注：其块扩散架构将历史记忆读出现与当前块 token 置于共享 softmax 竞争，同时引入独立零初始化右上下文卷积分支，该设计在 agent 任务性能与单卡生成速度上均取得正向结果，可参考其架构设计思路。

**标签**: `#coding-agent`, `#eval`, `#memory`

---

<a id="item-agent-engineer-3"></a>
### [Duopra 全双工代理论文发布](https://huggingface.co/papers/2611.25773) ⭐️ 6.0/10

2026 年 11 月 23 日 Hugging Face 每日论文更新，发布 Duopra 全双工代理模型研究预览。该研究提出 Duopra 可同步学习对话控制与任务执行，同时指出在 Full-Duplex-Bench v3 基准上，现有 Realtime-Venus-Audio + Harness 流式管线的多数失败发生在领域工具执行前。当前预览为截断版本，未公开完整技术规格、性能基准与实现细节，相关结论对实时代理 harness 优化有参考价值，需查阅完整论文验证。

rss · Hugging Face Daily Papers · 11月23日 00:00

**「为什么重要」** 现有实时代理 harness 的失败节点集中在工具执行前，这一发现直接指向代理编排的前置环节缺陷，突破了此前默认故障多出在工具层的认知。但当前仅为论文预览，Duopra 的实际性能与可复用方案尚未经完整论文验证。

**「可关注」** 可关注：前后端分离的全双工代理架构中，前置请求生成环节的完整性、及时性直接影响后续工具执行成功率，现有流式代理管线的故障高发点可能不在工具层而在请求调度层。

**标签**: `#agent`, `#harness`, `#eval`, `#tool-use`, `#orchestration`

---

<a id="item-agent-engineer-4"></a>
### [datasette-agent 0.7a0 发布](https://github.com/datasette/datasette-agent/releases/tag/0.7a0) ⭐️ 5.8/10

2026 年 11 月 23 日，simonw 发布 datasette-agent 0.7a0 alpha 版本。本次更新兼容 \`datasette&gt;=1.0a44\`，新增 \`system\_prompt\` 插件设置，支持在默认 agent 系统提示词后追加自定义指令，默认工具使用指引仍生效，覆盖聊天助手、后台 agent 及带 \`-c\` 配置文件的 \`datasette agent chat\` 场景；同时优化了 agent 索引、对话、后台 agent 页面的消息输入框自动聚焦体验。该版本无性能数据或架构变更，影响面较窄。

github · simonw · 11月23日 02:38

**「为什么重要」** 该更新为需要自定义 datasette agent 指令的开发者提供了原生配置入口，无需修改默认提示词即可追加定制规则；但当前为 alpha 版本，稳定性尚未验证，实际收益取决于具体使用场景。

**「可关注」** 可关注新增的 \`system\_prompt\` 插件配置项，支持在保留默认工具使用指引的前提下追加自定义 agent 指令，可覆盖多类 agent 运行场景。

**标签**: `#coding-agent`, `#harness`

---

## AI 羊毛
{: #sec-ai-deals .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-deals" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-deals-1"></a>
### [ChatGPT Pro 日区学生版优惠](https://www.v2ex.com/t/1258879#reply12) ⭐️ 7.0/10

V2EX 用户 mouseman 分享谷歌日区 ChatGPT Pro 学生版订阅优惠：完成日区学生认证后，可享 750 日元/月（约 30 元人民币）价格，权益与 20 美元正价 Pro 一致，支持 4 系列模型，据称该优惠可持续 4 年。

rss · V2EX Hot · 11月22日 05:44

**「为什么重要」** 该优惠价格约为正价的四分之一，且据称可持续 4 年，对需要 Pro 权益的用户成本优势明显。

**「可关注」** 可关注：需完成谷歌日区学生认证，订阅权益与正价 Pro 一致，支持 4 系列模型。

**标签**: `#student`, `#promo`

---