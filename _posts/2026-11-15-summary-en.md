---
layout: default
title: "Horizon Summary: 2026-11-15 (EN)"
date: 2026-11-15
lang: en
---

> From 185 items, 7 important content pieces were selected

---

**Agent Harness Architecture**
1. [browser-use 1.0.5 发布](#item-harness-arch-1) ⭐️ 5.5/10

**AI Agent Engineer**
1. [Antigravity /teamwork 多智能体功能更新](#item-agent-engineer-1) ⭐️ 7.0/10
2. [datasette-llm 0.1a11 发布](#item-agent-engineer-2) ⭐️ 6.0/10
3. [HF趋势榜 Qwen3 DSpine草稿模型](#item-agent-engineer-3) ⭐️ 6.0/10

**AI Deals**
1. [AI 语音面试陪练 领 90 分钟时长](#item-ai-deals-1) ⭐️ 8.0/10
2. [免费 Dictionary API 上线](#item-ai-deals-2) ⭐️ 7.0/10
3. [免费 GitHub 仓库安全扫描工具](#item-ai-deals-3) ⭐️ 5.0/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [browser-use 1.0.5 发布](https://github.com/browser-use/browser-use/releases/tag/1.0.5) ⭐️ 5.5/10

这是browser-use agent harness的1.0.5官方补丁版本发布。新增可配置的结构化运行判定系统，由用户自有模型对每次运行做任务匹配判定，结果回填至result.judgement字段，包含success、failure\_reason等6类结构化字段。同时恢复0.x版本的use\_judge、ground\_truth legacy参数兼容，优化站点反制检测能力，安装命令为pip install &\#x27;browser-use==1.0.5&\#x27;。

github · sarath-menon · Nov 14, 08:24

**「设计要点」** 运行判定逻辑由用户自有模型承担，判定时可访问运行trace、末次截图、最终页面（use\_vision=False时除外访问截图）；通过judge\_context参数传入自定义判定标准，支持judge=False关闭判定，同时兼容0.x版本的legacy评估参数。

**「改了什么」** \1. 新增结构化运行判定能力，每次运行自动生成包含6类字段的judgement结果；2. 恢复0.x版本use\_judge、ground\_truth参数兼容；3. 站点反制检测召回率从40%（6/15）提升至100%（15/15），干净运行误报率约8.3%（2/24），成功判定准确率无变化。

**「评论」** 暂无社区评论可用。

**Tags**: `#eval`, `#runtime`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [Antigravity /teamwork 多智能体功能更新](https://research.google/blog/advancing-science-engineering-with-antigravitys-teamwork-feature/) ⭐️ 7.0/10

2026年11月14日Google Research发布官方博客，展示Antigravity的/teamwork多智能体功能在数学、科学、编码、工程类任务上的应用案例，该功能此前已部分对外披露，当前更新已向外部用户推送。社区讨论提及多智能体团队存在上下文重复、token消耗过高的问题，同时关联了多智能体自适应harness的相关研究，Antigravity团队回应将持续迭代该功能并公开动态构建智能体团队的细节。

hackernews · acossta · Nov 14, 13:20 · [Discussion](https://news.ycombinator.com/item?id=50496811)

**「为什么重要」** 该功能是面向科研与工程场景的多智能体编排落地实践，社区讨论点出的多智能体上下文冗余、高token消耗是当前coding agent harness的普遍痛点，对相关工程师有直接参考价值。

**「可关注」** 可关注：多智能体团队场景下的上下文重复与token消耗问题，以及动态构建智能体团队的实现方案。

**「评论」** 社区用户反馈使用多智能体团队时出现上下文重复、周额度token在2天内耗尽的问题，同时分享了多智能体自适应harness的相关研究，也有用户对比了其与Claude动态工作流的差异。

**Tags**: `#orchestration`, `#coding-agent`, `#harness`, `#memory`

---

<a id="item-agent-engineer-2"></a>
### [datasette-llm 0.1a11 发布](https://simonwillison.net/2026/Nov/14/datasette-llm/) ⭐️ 6.0/10

datasette-llm 0.1a11 于 2026-11-14 发布，新增 OpenAI 兼容端点配置。该 alpha 版本允许 Datasette 插件通过 LM Studio、Ollama 或 llama.cpp 调用本地模型。配置支持在 \`default\_model\` 或 \`models\` 列表中使用含 \`api\_base\` 与 \`model\_name\` 的字典引用。版本要求 LLM 0.37.1+，并收紧模型查找、密钥校验与错误类型兼容性。

rss · Simon Willison · Nov 14, 23:59

**「为什么重要」** Datasette 生态首次原生支持 OpenAI 兼容协议，本地模型接入无需额外插件。对构建数据 Agent 的工程师可直接复用现有推理服务，但 alpha 阶段稳定性未经验证。

**「可关注」** 可关注：显式 \`key\` 不再回退到 provider 默认凭证，\`model\(\)\` / \`group\(\)\` 现在受 allowlist/blocklist 约束，且密钥缺失时提前抛出 \`NeedsKeyException\`，旧代码需检查隐式密钥依赖。

**Tags**: `#harness`

---

<a id="item-agent-engineer-3"></a>
### [HF趋势榜 Qwen3 DSpine草稿模型](https://huggingface.co/tencent/Qwen3.8-27B-DSpine-b16) ⭐️ 6.0/10

2026年11月15日，Hugging Face趋势榜新增tencent/Qwen3.8-27B-DSpine-b16模型，当前trendingScore为226，累计获得274个赞。该模型标注为兼容SGLang的Qwen3系列推测解码草稿模型，关联arXiv论文编号2609.36173。目前仅公开基础元数据，未披露技术细节、性能数据或架构说明，无法直接指导工程改进，对AI Agent推理优化存在潜在参考价值但信息不足。

rss · Hugging Face Trending Models · Nov 15, 02:53

**「为什么重要」** 该模型属于大模型推测解码的优化方向，若后续公开完整技术资料，可能为AI Agent推理延迟优化提供新的参考路径，但当前实际影响尚未得到证实。

**「可关注」** 可关注：该模型关联arXiv论文2609.36173，可后续跟进其公开的技术细节与性能基准数据。

**Tags**: `#speculative-decoding`, `#draft-model`, `#sglang`, `#inference-optimization`, `#text-generation`

---

## AI Deals

<a id="item-ai-deals-1"></a>
### [AI 语音面试陪练 领 90 分钟时长](https://www.v2ex.com/t/1257121#reply10) ⭐️ 8.0/10

独立开发者 cryptitalk 推出 AI 语音面试陪练工具，未登录用户可直接体验 10 分钟；使用 Google 账号登录并通过 5 分钟真人验证后，可获赠 90 分钟通话时长，前 20 位通过验证的用户还可获得 10 分钟一对一反馈邀约。

rss · V2EX Hot · Nov 14, 15:19

**「为什么重要」** 该工具采用全双工实时对话模式，支持用户随时打断 AI 发言，区别于传统分段回复的 AI 面试工具，当前提供技术面试、英语口语两类陪练角色，免费额度可满足轻度练习需求。

**「可关注」** 可关注：未登录可先体验 10 分钟，通过 5 分钟真人验证后可额外获得 90 分钟时长，时长按语音模型分钟计费。

**Tags**: `#limited-free`, `#promo`, `#api`

---

<a id="item-ai-deals-2"></a>
### [免费 Dictionary API 上线](https://api.suvankar.cc/docs/dictionary) ⭐️ 7.0/10

Hacker News 用户 suvankar\_m 在 Show HN 板块分享了一款基于 Wiktionary 数据的免费 Dictionary API，无需 API 密钥即可调用。目前可通过官方文档访问相关接口，公开信息未披露该 API 的速率限制、配额上限及服务可用时长。

rss · HN Free API / Credits · Nov 14, 06:30

**「可关注」** 可关注：该 API 无需 API 密钥即可调用，但尚未公开速率限制、配额上限等使用约束，适合轻量场景测试。

**Tags**: `#free-tier`, `#api`, `#limited-free`

---

<a id="item-ai-deals-3"></a>
### [免费 GitHub 仓库安全扫描工具](https://edgeiqlabs.com/free-repo-scanner/) ⭐️ 5.0/10

edgeiqlabs 在 Show HN 发布一款免费的 GitHub 仓库安全扫描工具，可检测泄露的密钥与暴露的配置，当前未公开具体使用限制、领取条件及截止时间。

rss · HN Free API / Credits · Nov 14, 12:09

**「为什么重要」** 该工具针对开发者常见的仓库密钥泄露、配置暴露风险提供免费检测能力，当前无公开使用门槛，适合有 GitHub 仓库安全巡检需求的开发者试用。

**「可关注」** 可关注：该工具暂未公开具体调用频率、扫描范围等限制，大规模使用前建议先小范围验证稳定性。

**Tags**: `#free-tier`, `#dev-tool`, `#security`, `#github`

---