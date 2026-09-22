---
layout: default
title: "Horizon Summary: 2026-09-22 (ZH)"
date: 2026-09-22
lang: zh
---

> 从 200 条内容中筛选出 11 条重要资讯。

---

**Harness 架构**
1. [Why we built the Responses API](#item-harness-arch-1) ⭐️ 6.3/10

**Agent 工程师日报**
1. [CodeMidas 从源码构建 RL 环境](#item-agent-engineer-1) ⭐️ 7.5/10
2. [Jev 决策模型：文本进，概率出](#item-agent-engineer-2) ⭐️ 7.0/10
3. [HF daily paper: RecreationWorld: Scalable and Verifiable Environments for Hybrid Computer-Use Agents](#item-agent-engineer-3) ⭐️ 7.0/10
4. [HF daily paper: Designer-RSI: Evolving Procedural Memory from User Traffic for Agentic Graphic Design](#item-agent-engineer-4) ⭐️ 7.0/10
5. [Code2Skill：从源码规模化合成可验证技能](#item-agent-engineer-5) ⭐️ 6.0/10

**AI 日报**
1. [OpenAI 呼吁共建全球 AI 标准](#item-ai-daily-1) ⭐️ 8.3/10
2. [Meta 开源 Rebalancer 分配库](#item-ai-daily-2) ⭐️ 8.3/10
3. [Meta 宣布 Petal 跨洋海缆](#item-ai-daily-3) ⭐️ 8.3/10
4. [Advisory Group on Mathematics and Artificial Intelligence](#item-ai-daily-4) ⭐️ 6.8/10
5. [OpenAI Academy 新增学习路径](#item-ai-daily-5) ⭐️ 5.8/10

---

## Harness 架构

<a id="item-harness-arch-1"></a>
### [Why we built the Responses API](https://developers.openai.com/blog/responses-api) ⭐️ 6.3/10

OpenAI publishes a design rationale for the Responses API, positioning it as the preferred integration surface for reasoning models and agentic workflows.

rss · OpenAI Developer · 9月22日 00:00

**标签**: `#runtime`, `#tools`, `#planning`

---

## Agent 工程师日报

<a id="item-agent-engineer-1"></a>
### [CodeMidas 从源码构建 RL 环境](https://huggingface.co/papers/2609.22068) ⭐️ 7.5/10

CodeMidas 论文提出一种 agentic pipeline，仅以源码为输入，将现有代码库转化为可执行的 RL 环境，用于训练和评测 coding agent。该方法把 agentic compute 分配到环境构建各阶段：agent 探索已实现功能以形成行为规范，基于原始代码执行构建测试，并验证和过滤候选任务。论文指出现有方法通常依赖 issues 和 commits 等开发产物，限制了可提取任务的范围。该论文于 2026-09-22 由 Hugging Face Daily Papers 收录，获得 90 个 upvotes。

rss · Hugging Face Daily Papers · 9月22日 02:01

**「为什么重要」** 对 coding agent 的 RL 训练与评测而言，这提供了一条不依赖 issues、commits 等开发产物、直接从源码扩展任务环境的路径。目前材料仅描述研究方法，尚未给出已发布工具或大规模验证结果。

**「可关注」** 可关注：现有方法多依赖 issues 和 commits 提取任务，CodeMidas 则仅以源码为输入，由 agent 分阶段完成行为规范制定、测试构建与任务过滤。

**标签**: `#coding-agent`, `#eval`, `#orchestration`

---

<a id="item-agent-engineer-2"></a>
### [Jev 决策模型：文本进，概率出](https://simonwillison.net/2026/Sep/21/jev/) ⭐️ 7.0/10

TypeSafe AI 发布 Jev，称其为 System One 模型，Simon Willison 认为「决策模型」更贴切。该模型接受文本输入，返回浮点数而非文本，覆盖类别、是非、评分及置信度；计费仅按输入，$0.042 每百万 token，低于 GPT-5 Nano 的 $0.05，输出免费。单个 state 可携带多个问题并行求值，适合分类、垃圾检测、打标签、排序与重排。Simon Willison 提醒，Jev 的黑盒程度超过 LLM——只给分数，不给理由，偏差风险更需警惕。

rss · Simon Willison · 9月21日 23:09

**「为什么重要」** 对 coding agent 与 harness 工程师，Jev 提供了比 LLM 更便宜、更快的决策原语，可用于路由、过滤、重排等环节；但它把可解释性压缩成一个浮点数，eval 与结构化实验比以往更重要。

**「可关注」** 可关注：Jev 类决策模型在分类、打分、重排等环节比 LLM 文本生成更经济，但只返回浮点数、无法追问理由，需配套 eval 与结构化实验来控制偏差。

**标签**: `#orchestration`, `#eval`, `#decision-models`

---

<a id="item-agent-engineer-3"></a>
### [HF daily paper: RecreationWorld: Scalable and Verifiable Environments for Hybrid Computer-Use Agents](https://huggingface.co/papers/2609.22000) ⭐️ 7.0/10

A new paper presents RecreationWorld, a scalable five-platform framework and unified harness for evaluating hybrid computer-use agents that interleave GUI interaction with coding.

rss · Hugging Face Daily Papers · 9月22日 02:01

**标签**: `#harness`, `#eval`, `#coding-agent`

---

<a id="item-agent-engineer-4"></a>
### [HF daily paper: Designer-RSI: Evolving Procedural Memory from User Traffic for Agentic Graphic Design](https://huggingface.co/papers/2609.22086) ⭐️ 7.0/10

Introduces a procedural memory framework that enables a frozen frontier model to accumulate and refine reusable design procedures from real user traffic while operating professional graphic design software.

rss · Hugging Face Daily Papers · 9月22日 02:01

**标签**: `#memory`, `#eval`, `#orchestration`, `#harness`

---

<a id="item-agent-engineer-5"></a>
### [Code2Skill：从源码规模化合成可验证技能](https://huggingface.co/papers/2609.05571) ⭐️ 6.0/10

HF 日报论文提出 Code2Skill，一条全自动流水线，把选定代码单元转成实现锚定的原子操作、复合工作流与重复模式记录，再通过 source-body-blind reconstruction 与 source-aware comparison 逐条验证。论文称源码不需要先验 agent 经验，却能提供可执行证据来锚定抽象，已在 19,769 个代码单元上应用。相比依赖特定环境交互的轨迹合成、缺乏可执行证据的文档派生技能，这条路径试图补上技能获取的缺口。不过摘要被截断，未展示生产环境轨迹或基准突破，对现有 agent 工具链的实际影响仍不确定。

rss · Hugging Face Daily Papers · 9月22日 02:01

**「为什么重要」** 对做 coding agent 与 harness 的人，这把技能获取的来源从环境交互和文档解析扩展到源码本身，用可执行证据做锚定。但论文尚未给出生产环境验证或基准对比，能否融入现有工具链仍是开放问题。

**「可关注」** 可关注：源码作为 agent 技能记忆来源的可行性，以及 source-body-blind reconstruction 这类验证机制能否在现有记忆与评测框架中复用。

**标签**: `#memory`, `#eval`, `#coding-agent`

---

## AI 日报

<a id="item-ai-daily-1"></a>
### [OpenAI 呼吁共建全球 AI 标准](https://openai.com/index/building-standards-next-phase-ai) ⭐️ 8.3/10

OpenAI 发布政策文章，提出构建共享的全球 AI 标准，以提升安全性。文章将协同评估、报告与治理列为三个核心方向。该文为治理框架倡议，并非产品或模型发布。

rss · OpenAI Blog · 9月21日 10:00

**「为什么重要」** OpenAI 以官方身份提出全球标准框架，为行业安全治理讨论提供明确立场。文章聚焦评估、报告与治理的协同，而非单一技术方案。

**「可关注」** 可关注：OpenAI 将协同评估、报告与治理列为全球 AI 标准化的三个方向。

**标签**: `#policy`, `#lab`, `#industry`, `#eval`

---

<a id="item-ai-daily-2"></a>
### [Meta 开源 Rebalancer 分配库](https://engineering.fb.com/2026/09/21/open-source/rebalancer-generic-high-performance-library-assignment-problems/) ⭐️ 8.3/10

Meta 开源 Rebalancer，一个通用高性能分配问题求解库。该库已在 Meta 内部用于资源分配超过九年。Rebalancer 将问题定义、内存存储、求解与调试四个关注点分离。

rss · Engineering at Meta · 9月21日 16:00

**「为什么重要」** 对需要处理分配问题的团队，Rebalancer 提供了在 Meta 内部验证九年的高性能实现。其关注点分离设计允许独立调整问题定义、存储与求解逻辑。

**「可关注」** 可关注：若你的系统涉及资源分配或任务匹配，可评估 Rebalancer 的通用接口与内部分离式存储设计。

**标签**: `#open-source`, `#lab`, `#industry`

---

<a id="item-ai-daily-3"></a>
### [Meta 宣布 Petal 跨洋海缆](https://engineering.fb.com/2026/09/21/connectivity/petal-petabit-transoceanic-subsea-cable/) ⭐️ 8.3/10

Meta 宣布建设 Petal 跨洋海底光缆，连接法国与美国，全长约 7,000 km。该光缆预计 2029 年投入使用，将成为首条在跨洋距离实现 petabit 级容量的海底光缆，并首次大规模部署多芯光纤技术。

rss · Engineering at Meta · 9月21日 12:00

**「为什么重要」** Petal 是首条跨洋 petabit 级海缆，也是多芯光纤首次在海底场景规模化部署。Meta 将其定位为海底创新的下一步。

**「可关注」** 多芯光纤在跨洋海缆中的首次规模化部署，以及 2029 年 petabit 级容量投入服务的时间点。

**标签**: `#industry`, `#product`, `#lab`

---

<a id="item-ai-daily-4"></a>
### [Advisory Group on Mathematics and Artificial Intelligence](https://openai.com/index/advisory-group-on-mathematics-and-ai) ⭐️ 6.8/10

OpenAI announced an independent advisory group to guide the review and communication of emerging AI results in mathematics.

rss · OpenAI Blog · 9月21日 12:00

**标签**: `#lab`, `#industry`, `#policy`

---

<a id="item-ai-daily-5"></a>
### [OpenAI Academy 新增学习路径](https://openai.com/index/expanding-openai-academy-with-new-learning-paths) ⭐️ 5.8/10

OpenAI 官方博客宣布扩展 OpenAI Academy，新增面向员工、开发者、领导者、教育工作者和学生的学习路径，目标是帮助用户构建并展示实践 AI 技能。官方未公布具体课程数量、时长或技术细节。该更新属于教育产品边缘调整，对核心模型或行业新闻影响有限。

rss · OpenAI Blog · 9月21日 07:00

**标签**: `#product`, `#lab`

---