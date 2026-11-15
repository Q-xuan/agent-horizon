---
layout: default
title: "Horizon Summary: 2026-11-15 (ZH)"
date: 2026-11-15
lang: zh
---

> 从 185 条内容中筛选出 7 条重要资讯。

<nav id="ah-toc" class="ah-toc" aria-label="目录"><span class="ah-toc-title">目录</span><ul><li><a href="#sec-harness-arch"><span class="ah-toc-name">Harness 架构</span><span class="ah-toc-count">1条</span></a></li><li><a href="#sec-agent-engineer"><span class="ah-toc-name">Agent 工程师日报</span><span class="ah-toc-count">3条</span></a></li><li><a href="#sec-ai-deals"><span class="ah-toc-name">AI 羊毛</span><span class="ah-toc-count">3条</span></a></li></ul></nav>

---

**[Harness 架构](#sec-harness-arch)**
1. [browser-use 1.0.5 发布](#item-harness-arch-1) ⭐️ 5.5/10

**[Agent 工程师日报](#sec-agent-engineer)**
1. [Antigravity 发布 /teamwork 多智能体特性](#item-agent-engineer-1) ⭐️ 7.0/10
2. [datasette-llm 0.1a11 支持 OpenAI 兼容端点](#item-agent-engineer-2) ⭐️ 6.0/10
3. [Qwen3 DSpine 草稿模型登 HF 趋势榜](#item-agent-engineer-3) ⭐️ 6.0/10

**[AI 羊毛](#sec-ai-deals)**
1. [AI 语音面试陪练 90 分钟时长可领](#item-ai-deals-1) ⭐️ 8.0/10
2. [免费 Wiktionary 词典 API](#item-ai-deals-2) ⭐️ 7.0/10
3. [edgeiqlabs 免费 GitHub 安全扫描工具](#item-ai-deals-3) ⭐️ 5.0/10

---

## Harness 架构
{: #sec-harness-arch .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-harness-arch" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-harness-arch-1"></a>
### [browser-use 1.0.5 发布](https://github.com/browser-use/browser-use/releases/tag/1.0.5) ⭐️ 5.5/10

browser-use 1.0.5 正式发布，可通过 pip install &\#x27;browser-use==1.0.5&\#x27;升级。本次新增可配置的结构化运行评判系统，仅需一次低开销模型请求即可完成运行判定，向 result.judgement 填充 success、failure\_reason、description、prompt\_injection\_detected、bot\_block\_or\_captcha\_detected、gotchas 等结构化字段，同时显著提升站点反制（封机器人、验证码、输入报错）检测准确率，并恢复 0.x 版本的旧评判参数支持。

github · sarath-menon · 11月14日 08:24

**「设计要点」** 评判模块为运行时可选组件，支持通过 judge\_context 传入自定义判定标准、judge=False 关闭，可访问运行全轨迹、末次截图与最终页面（use\_vision=False 时除外），同时兼容 0.x 版本的 use\_judge、ground\_truth 参数。

**「改了什么」** 新增可配置结构化运行评判能力，输出字段覆盖运行成功状态、失败原因、提示注入/机器人拦截检测、运行注意事项；站点反制场景检测准确率从 6/15 提升至 15/15，干净运行误报率 2/24，成功判定结果无回退；恢复 0.x 版本 use\_judge、ground\_truth 参数支持，相关实现对应 PR \#6398、\#6403、\#6404。

**标签**: `#eval`, `#runtime`

---

## Agent 工程师日报
{: #sec-agent-engineer .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-agent-engineer" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-agent-engineer-1"></a>
### [Antigravity 发布 /teamwork 多智能体特性](https://research.google/blog/advancing-science-engineering-with-antigravitys-teamwork-feature/) ⭐️ 7.0/10

2026 年 11 月 14 日 Google Research 发布官方博客，展示 Antigravity 的/teamwork 多智能体功能，面向科研、工程、编码类任务场景。Antigravity 团队成员表示该功能此前已部分公开，本次通过具体案例展示进展，将持续迭代并对外推送更新。社区反馈显示多智能体团队模式存在上下文重复、token 消耗过高的问题，也有用户指出该功能与 Claude 动态工作流的差异尚不清晰，且当前无自动模式、/goal 功能发布晚于同类工具。

hackernews · acossta · 11月14日 13:20 · [社区讨论](https://news.ycombinator.com/item?id=50496811)

**「为什么重要」** 该功能是官方公开的多智能体科研/工程编码实践案例，直接关联 agent 编排与编码 agent 工具链的工程落地。社区讨论点出了多智能体团队模式的上下文重复、高 token 消耗等实际痛点，并关联了多智能体自适应 harness 的前沿研究，为相关工程师提供可参考的实践与研究方向。

**「可关注」** 可关注：多智能体团队模式在提升任务效率的同时，存在上下文重复导致 token 消耗过高、存储占用大的工程权衡，需结合实际场景评估适配性。

**「评论」** 社区讨论呈现两类核心观点：一是实际使用中多智能体团队模式存在上下文重复、token 消耗过高的体验问题；二是对该功能与 Claude 动态工作流的差异、是否具备自动模式等能力提出疑问，同时有用户关联了多智能体自适应 harness 的前沿研究。

**标签**: `#orchestration`, `#coding-agent`, `#harness`, `#memory`

---

<a id="item-agent-engineer-2"></a>
### [datasette-llm 0.1a11 支持 OpenAI 兼容端点](https://simonwillison.net/2026/Nov/14/datasette-llm/) ⭐️ 6.0/10

datasette-llm 0.1a11 于 2026-11-14 发布，新增 OpenAI 兼容端点支持。该版本允许 Datasette 插件直接配置 LM Studio、Ollama 或 llama.cpp 等本地模型后端，无需额外 LLM 插件。配置通过新增的 endpoints 字段或 default\_model 字典实现，支持 Chat Completions 与 Responses 协议，工具调用与流式传输默认开启。此 alpha 版本要求 LLM 0.37.1 或更高版本，且模型查找逻辑与 allowlist/blocklist 行为发生兼容性变更。

rss · Simon Willison · 11月14日 23:59

**「为什么重要」** 本地 LLM 后端可直接接入 Datasette 插件生态，降低部署与测试门槛。但 0.1a11 仍属 alpha 阶段，allowlist 与 key 校验逻辑的变更可能影响现有配置，升级前需验证模型选择路径。

**「可关注」** 可关注：model\(\) 和 group\(\) 现在受 allowlists/blocklists 约束，且缺失 key 时提前抛出 NeedsKeyException，迁移时需检查现有模型选择逻辑。

**标签**: `#harness`

---

<a id="item-agent-engineer-3"></a>
### [Qwen3 DSpine 草稿模型登 HF 趋势榜](https://huggingface.co/tencent/Qwen3.8-27B-DSpine-b16) ⭐️ 6.0/10

2026 年 11 月 15 日，Hugging Face 趋势榜新增模型 tencent/Qwen3.8-27B-DSpine-b16，trendingScore 为 226，累计获 274 个赞。该模型被标注为兼容 SGLang 的 Qwen3 系列推测解码草稿模型，关联 arXiv 论文 2609.36173。当前仅公开基础元数据，无性能数据、技术细节或架构说明，对 AI Agent 推理优化的潜在参考价值尚未验证。

rss · Hugging Face Trending Models · 11月15日 02:53

**「为什么重要」** 推测解码是降低大模型推理延迟的主流方向之一，该模型若后续公开技术细节，可能为 AI Agent 推理优化提供新的可落地方案，但目前仅能确认其登上 HF 趋势榜、具备 SGLang 兼容标签，实际工程价值尚未得到验证。

**「可关注」** 可关注：该模型关联 arXiv 论文 2609.36173，可后续追踪论文或模型仓库更新，获取可用于工程改进的技术细节。

**标签**: `#speculative-decoding`, `#draft-model`, `#sglang`, `#inference-optimization`, `#text-generation`

---

## AI 羊毛
{: #sec-ai-deals .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-deals" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-deals-1"></a>
### [AI 语音面试陪练 90 分钟时长可领](https://www.v2ex.com/t/1257121#reply10) ⭐️ 8.0/10

独立开发者 cryptitalk 推出 AI 语音面试陪练工具，提供 10 分钟免登录免费体验。用户使用 Google 账号登录，与“小豆”完成 5 分钟真人验证后，可获赠 90 分钟通话时长。

rss · V2EX Hot · 11月14日 15:19

**「为什么重要」** 该工具采用全双工实时对话模式，支持用户随时打断 AI 回复，当前提供技术面试深挖、英语口语练习两类角色，测试阶段免费额度获取门槛较低。

**「可关注」** 可关注：免登录即可体验 10 分钟，Google 登录并通过 5 分钟真人验证后即可获得 90 分钟时长，前 20 位通过验证的用户可自愿获得开发者 1 对 1 反馈沟通机会。

**标签**: `#limited-free`, `#promo`, `#api`

---

<a id="item-ai-deals-2"></a>
### [免费 Wiktionary 词典 API](https://api.suvankar.cc/docs/dictionary) ⭐️ 7.0/10

Hacker News 用户 suvankar\_m 分享了一款基于 Wiktionary 数据的免费词典 API，无需 API 密钥即可调用，可通过官方文档访问使用；当前公开材料未披露该 API 的速率限制、配额上限及可用时长。

rss · HN Free API / Credits · 11月14日 06:30

**「为什么重要」** 面向需要轻量词义查询能力的开发者，该 API 无需密钥即可调用 Wiktionary 数据，可降低自建数据集与接入测试的成本。

**「可关注」** 可关注：该 API 未公开速率限制、配额上限与长期可用性承诺，生产环境使用前需自行验证稳定性。

**标签**: `#free-tier`, `#api`, `#limited-free`

---

<a id="item-ai-deals-3"></a>
### [edgeiqlabs 免费 GitHub 安全扫描工具](https://edgeiqlabs.com/free-repo-scanner/) ⭐️ 5.0/10

edgeiqlabs 在 Show HN 发布免费 GitHub 仓库安全扫描工具，可检测泄露密钥与暴露配置。目前未公开具体使用限制、领取条件及截止时间。

rss · HN Free API / Credits · 11月14日 12:09

**「为什么重要」** 该工具可覆盖仓库密钥泄露、配置暴露两类常见安全风险，适合个人开发者或小团队做基础仓库安全排查，但当前公开信息不足，社区互动量极低，属于优先级较低的羊毛条目，实用性待验证。

**「可关注」** 可关注：该工具未公开扫描频率、仓库数量限制等具体规则，使用前需确认是否符合自身需求。

**标签**: `#free-tier`, `#dev-tool`, `#security`, `#github`

---