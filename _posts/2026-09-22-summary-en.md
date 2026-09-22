---
layout: default
title: "Horizon Summary: 2026-09-22 (EN)"
date: 2026-09-22
lang: en
---

> From 200 items, 11 important content pieces were selected

---

**Agent Harness Architecture**
1. [Why we built the Responses API](#item-harness-arch-1) ⭐️ 6.3/10

**AI Agent Engineer**
1. [CodeMidas 将源码转为 RL 环境](#item-agent-engineer-1) ⭐️ 7.5/10
2. [Jev 决策模型：文本输入，浮点输出](#item-agent-engineer-2) ⭐️ 7.0/10
3. [HF daily paper: RecreationWorld: Scalable and Verifiable Environments for Hybrid Computer-Use Agents](#item-agent-engineer-3) ⭐️ 7.0/10
4. [HF daily paper: Designer-RSI: Evolving Procedural Memory from User Traffic for Agentic Graphic Design](#item-agent-engineer-4) ⭐️ 7.0/10
5. [Code2Skill Synthesizes Verifiable Skills from Source Code](#item-agent-engineer-5) ⭐️ 6.0/10

**AI Daily**
1. [OpenAI 呼吁建立全球 AI 标准](#item-ai-daily-1) ⭐️ 8.3/10
2. [Meta 开源 Rebalancer 分配问题求解库](#item-ai-daily-2) ⭐️ 8.3/10
3. [Meta 发布 Petal 跨洋海缆](#item-ai-daily-3) ⭐️ 8.3/10
4. [Advisory Group on Mathematics and Artificial Intelligence](#item-ai-daily-4) ⭐️ 6.8/10
5. [OpenAI Academy 新增学习路径](#item-ai-daily-5) ⭐️ 5.8/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [Why we built the Responses API](https://developers.openai.com/blog/responses-api) ⭐️ 6.3/10

OpenAI publishes a design rationale for the Responses API, positioning it as the preferred integration surface for reasoning models and agentic workflows.

rss · OpenAI Developer · Sep 22, 00:00

**Tags**: `#runtime`, `#tools`, `#planning`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [CodeMidas 将源码转为 RL 环境](https://huggingface.co/papers/2609.22068) ⭐️ 7.5/10

2026-09-22，Hugging Face Daily Papers 收录 CodeMidas 论文。该工作提出 agentic pipeline，仅以源码为任务特定输入，把现有代码库中已实现的功能转化为可执行 RL 环境，用于训练和评测 coding agent。pipeline 在环境构建各阶段分配 agentic compute：agent 探索已实现功能以形成行为规约，基于原始代码执行构造测试，并验证和过滤候选任务。论文指出现有方法多依赖 issue 和 commit 等开发产物，限制了可提取任务的范围；CodeMidas 属于研究方法，尚未发布破坏性变更，HF 页面获 90 次 upvote。

rss · Hugging Face Daily Papers · Sep 22, 02:01

**「为什么重要」** 对做 coding agent 评测与训练的人，这篇论文提供了一条不依赖 issue、commit 等开发产物、直接从源码规模化生成 RL 环境的路径。其实际效果尚未在更大范围验证，但方法本身对工具体系有直接参考价值。

**「可关注」** 环境构建各阶段都分配 agentic compute，从探索功能、生成测试到过滤任务，算力投入与最终任务质量之间的权衡需要实测数据支撑。

**Tags**: `#coding-agent`, `#eval`, `#orchestration`

---

<a id="item-agent-engineer-2"></a>
### [Jev 决策模型：文本输入，浮点输出](https://simonwillison.net/2026/Sep/21/jev/) ⭐️ 7.0/10

TypeSafe AI 近日发布 Jev，官方称 System One 模型，实践者更习惯叫决策模型。接口仍收文本，但返回浮点数，对应类别、是非、评分及置信度。输出不计费，输入每百万 token $0.042，低于 GPT-5 Nano 的 $0.05。单个 state 可携带多个问题并行求值。适合垃圾识别、打标、优先级排序、搜索结果重排等分类场景。Simon Willison 提醒，Jev 比 LLM 更黑盒——只回浮点数，不给理由，偏见风险需靠前置评测约束。

rss · Simon Willison · Sep 21, 23:09

**「为什么重要」** agent 工程师可用它替换路由、过滤、重排里的「生成再解析」，直接拿概率，降低延迟与成本。但它不提供任何解释输出，接入前必须自建评测集与结构化实验，不能只靠 prompt 试错。

**「可关注」** 可关注：Jev 将模型输出压缩为类型化概率值，适合嵌入 agent 流水线做中间决策；由于缺乏可解释性，需为具体业务场景建立离线评测与偏见审计机制，再决定是否替换现有 LLM 分类链路。

**Tags**: `#orchestration`, `#eval`, `#decision-models`

---

<a id="item-agent-engineer-3"></a>
### [HF daily paper: RecreationWorld: Scalable and Verifiable Environments for Hybrid Computer-Use Agents](https://huggingface.co/papers/2609.22000) ⭐️ 7.0/10

A new paper presents RecreationWorld, a scalable five-platform framework and unified harness for evaluating hybrid computer-use agents that interleave GUI interaction with coding.

rss · Hugging Face Daily Papers · Sep 22, 02:01

**Tags**: `#harness`, `#eval`, `#coding-agent`

---

<a id="item-agent-engineer-4"></a>
### [HF daily paper: Designer-RSI: Evolving Procedural Memory from User Traffic for Agentic Graphic Design](https://huggingface.co/papers/2609.22086) ⭐️ 7.0/10

Introduces a procedural memory framework that enables a frozen frontier model to accumulate and refine reusable design procedures from real user traffic while operating professional graphic design software.

rss · Hugging Face Daily Papers · Sep 22, 02:01

**Tags**: `#memory`, `#eval`, `#orchestration`, `#harness`

---

<a id="item-agent-engineer-5"></a>
### [Code2Skill Synthesizes Verifiable Skills from Source Code](https://huggingface.co/papers/2609.05571) ⭐️ 6.0/10

Hugging Face Daily Papers featured Code2Skill, a fully automated pipeline that turns selected code units into implementation-anchored records of atomic operations, composite workflows, and recurring patterns. It verifies each record through source-body-blind reconstruction and source-aware comparison. The paper argues that source code requires no prior agent experience and supplies executable evidence, filling gaps left by trajectory-based synthesis and document-derived skills. The experiment covers 19,769 popular, active code units. The abstract reports no production traces or benchmark breakthroughs, so impact on existing agent toolchains is unverified.

rss · Hugging Face Daily Papers · Sep 22, 02:01

**「Why It Matters」** For coding agent and harness builders, skill acquisition moves from environment-dependent trajectories to code-as-evidence, with automated reconstruction replacing manual checks. If the method holds up, it could reduce the cost of curating agent skill libraries. Current evidence is limited to the paper&\#x27;s own claims.

**「Watch」** Watch: Code2Skill replaces trajectories with source code as the skill source and verifies output via source-body-blind reconstruction. Without production traces, its fit with existing agent memory and eval workflows remains unconfirmed.

**Tags**: `#memory`, `#eval`, `#coding-agent`

---

## AI Daily

<a id="item-ai-daily-1"></a>
### [OpenAI 呼吁建立全球 AI 标准](https://openai.com/index/building-standards-next-phase-ai) ⭐️ 8.3/10

OpenAI 发布政策倡议，呼吁建立全球共享的 AI 标准，提出围绕评估、报告与治理开展国际协调，以提升安全性。该文为治理框架倡议，并非产品或模型发布。

rss · OpenAI Blog · Sep 21, 10:00

**「为什么重要」** 作为头部 AI 实验室的公开政策表态，该倡议为行业安全治理提供了协调方向，但具体标准与执行机制仍待明确。

**「可关注」** OpenAI 提出围绕评估、报告与治理开展国际协调，具体标准内容与执行机制尚未公布。

**Tags**: `#policy`, `#lab`, `#industry`, `#eval`

---

<a id="item-ai-daily-2"></a>
### [Meta 开源 Rebalancer 分配问题求解库](https://engineering.fb.com/2026/09/21/open-source/rebalancer-generic-high-performance-library-assignment-problems/) ⭐️ 8.3/10

Meta 开源 Rebalancer，一个通用高性能分配问题求解库。该库已在 Meta 内部用于资源分配超过九年。Rebalancer 将问题定义、内存存储、求解与调试分离，便于独立优化各环节。

rss · Engineering at Meta · Sep 21, 16:00

**「为什么重要」** 对需要处理资源分配或任务调度系统的工程师而言，这是一个经过长期生产验证的求解库。其关注点分离设计提供了可复用的架构参考。

**「可关注」** Rebalancer 将分配问题的定义、存储、求解与调试分层解耦，替换求解算法时无需改动上层接口。

**Tags**: `#open-source`, `#lab`, `#industry`

---

<a id="item-ai-daily-3"></a>
### [Meta 发布 Petal 跨洋海缆](https://engineering.fb.com/2026/09/21/connectivity/petal-petabit-transoceanic-subsea-cable/) ⭐️ 8.3/10

Meta 宣布推出 Petal，首条跨洋 Petabit 级海底电缆，连接法国与美国，全长约 7,000 km。Meta 称该系统预计 2029 年投入服务，并成为首个规模部署多芯光纤技术的海底电缆系统。

rss · Engineering at Meta · Sep 21, 12:00

**「为什么重要」** Petal 首次在跨洋海底电缆中规模部署多芯光纤，目标容量达到 Petabit 级。这为该技术路线进入工程实施阶段提供了已公布的案例。

**「可关注」** 可关注：Petal 预计 2029 年投运，是首个规模部署多芯光纤的跨洋海底电缆系统，连接法国与美国，全长约 7,000 km。

**Tags**: `#industry`, `#product`, `#lab`

---

<a id="item-ai-daily-4"></a>
### [Advisory Group on Mathematics and Artificial Intelligence](https://openai.com/index/advisory-group-on-mathematics-and-ai) ⭐️ 6.8/10

OpenAI announced an independent advisory group to guide the review and communication of emerging AI results in mathematics.

rss · OpenAI Blog · Sep 21, 12:00

**Tags**: `#lab`, `#industry`, `#policy`

---

<a id="item-ai-daily-5"></a>
### [OpenAI Academy 新增学习路径](https://openai.com/index/expanding-openai-academy-with-new-learning-paths) ⭐️ 5.8/10

OpenAI 宣布在 Academy 中新增面向员工、开发者、领导者、教育工作者和学生的学习路径。官方表示，这些路径用于帮助用户构建并展示实用 AI 技能。公告未提及具体课程数量、时长或认证细节。该更新属于教育产品扩展，对核心模型与行业格局影响有限。

rss · OpenAI Blog · Sep 21, 07:00

**「为什么重要」** 对于需要系统学习 AI 工具的开发者，OpenAI 提供了官方学习路径作为参考。但此次更新不涉及模型能力或 API 变化，实际价值需视后续课程质量而定。

**「可关注」** 可关注：OpenAI Academy 新增了面向开发者的学习路径，但公告未披露课程大纲、实验环境及认证标准，可等待官方进一步公布细节后再评估投入。

**Tags**: `#product`, `#lab`

---