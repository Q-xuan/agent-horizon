---
layout: default
title: "Horizon Summary: 2026-11-15 (ZH)"
date: 2026-11-15
lang: zh
---

> 从 152 条内容中筛选出 9 条重要资讯。

<nav id="ah-toc" class="ah-toc" aria-label="目录"><span class="ah-toc-title">目录</span><ul><li><a href="#sec-harness-arch"><span class="ah-toc-name">Harness 架构</span><span class="ah-toc-count">2条</span></a></li><li><a href="#sec-agent-engineer"><span class="ah-toc-name">Agent 工程师日报</span><span class="ah-toc-count">6条</span></a></li><li><a href="#sec-ai-daily"><span class="ah-toc-name">AI 日报</span><span class="ah-toc-count">1条</span></a></li></ul></nav>

---

**[Harness 架构](#sec-harness-arch)**
1. [LangGraph 1.2.22 发布](#item-harness-arch-1) ⭐️ 5.3/10
2. [browser-use 1.0.5 发布](#item-harness-arch-2) ⭐️ 5.3/10

**[Agent 工程师日报](#sec-agent-engineer)**
1. [Antigravity /teamwork 功能更新](#item-agent-engineer-1) ⭐️ 7.0/10
2. [长周期智能体决策模型三角色研究](#item-agent-engineer-2) ⭐️ 7.0/10
3. [SO-Arena 基准测试发布](#item-agent-engineer-3) ⭐️ 6.0/10
4. [HF 每日论文：Duo 全双工世界模型](#item-agent-engineer-4) ⭐️ 6.0/10
5. [Open Vision Banana 方案](#item-agent-engineer-5) ⭐️ 6.0/10
6. [Qwen3 投机解码草稿模型 trending 上线](#item-agent-engineer-6) ⭐️ 6.0/10

**[AI 日报](#sec-ai-daily)**
1. [82 亿收购后 李飞飞苏姿丰 CoRL 首同台](#item-ai-daily-1) ⭐️ 5.5/10

---

## Harness 架构
{: #sec-harness-arch .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-harness-arch" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-harness-arch-1"></a>
### [LangGraph 1.2.22 发布](https://github.com/langchain-ai/langgraph/releases/tag/1.2.22) ⭐️ 5.3/10

langgraph 1.2.22 发布，同步更新 checkpoint-postgres 3.2.1、prebuilt 1.1.2 和 checkpoint 4.3.2。本次修复子图流式传输线程模型，并引入五项运行时性能优化。修复确保子图在独立线程上流式传输给调用方，避免阻塞。性能优化覆盖消息转换、待处理写入过滤、宽状态匹配、失败 futures 检查和通道跟踪，降低运行时开销。

github · github-actions\[bot\] · 11月14日 01:43

**「设计要点」** 子图执行改为独立线程流式传输，解耦调用方与子图运行。运行时通过跳过普通消息转换、按任务过滤待处理写入、集合匹配更新键、仅检查失败 futures、单次扫描未跟踪通道，减少状态管理和消息处理开销。

**「改了什么」** 修复子图流式传输线程模型，使子图在独立线程上向调用方流式传输。新增五项性能优化：跳过 add\_messages 中普通消息转换、过滤待处理写入、宽状态集合匹配、仅检查失败 futures、单次通道扫描。

**标签**: `#runtime`, `#subagents`

---

<a id="item-harness-arch-2"></a>
### [browser-use 1.0.5 发布](https://github.com/browser-use/browser-use/releases/tag/1.0.5) ⭐️ 5.3/10

browser-use 1.0.5 发布，新增可配置的基于模型的运行评判功能。每次浏览器 agent 任务运行后，用户指定的模型会检查 trace、最终页面和截图（除非 use\_vision=False），并将结果写入 result.judgement，字段包括 success、failure\_reason、description、prompt\_injection\_detected、bot\_block\_or\_captcha\_detected 和 gotchas。通过 judge\_context= 传入评判标准，judge=False 关闭该功能；同时恢复 0.x 版本的 use\_judge 和 ground\_truth 标志。该版本还改进了站点反制（pushback）场景的 gotcha 检测，在 13 次真实运行各评判 3 次的测试中，站点反制场景的 gotcha 检出率从 6/15 提升至 15/15，干净运行误报率为 2/24。

github · sarath-menon · 11月14日 08:24

**「改了什么」** 新增基于模型的运行评判，支持 judge\_context 和 judge=False 控制，恢复 use\_judge/ground\_truth 标志。改进站点反制 gotcha 检测，覆盖站点拒绝输入、报错、封锁、限流等场景，即使运行成功也会记录。

**标签**: `#tools`, `#eval`

---

## Agent 工程师日报
{: #sec-agent-engineer .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-agent-engineer" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-agent-engineer-1"></a>
### [Antigravity /teamwork 功能更新](https://research.google/blog/advancing-science-engineering-with-antigravitys-teamwork-feature/) ⭐️ 7.0/10

2026 年 11 月 14 日 Google Research 发布博客，介绍 Antigravity 的/teamwork 功能，支持科学与工程任务的多智能体动态协作。该功能已对外推送更新，Google Antigravity 团队成员回应称此前已公开过该功能的部分内容，本次更新包含更多可视化展示，将持续迭代并对外推送相关能力，后续会公开动态组建智能体团队的更多技术细节。当前社区有用户对比其与 Claude 动态工作流的差异，也有用户指出该功能缺少自动模式、公开使用说明不足。

hackernews · acossta · 11月14日 13:20 · [社区讨论](https://news.ycombinator.com/item?id=50496811)

**「为什么重要」** 该功能是面向科研与工程场景的多智能体协作编排能力，直接关联 AI Agent harness 的设计方向。社区已将其与自适应 harness 研究、Claude 动态工作流并列讨论，说明动态多智能体协作是当前行业关注的技术方向。

**「可关注」** 可关注：动态多智能体协作在科研工程场景的落地形态，以及不同 Agent harness 在自动模式、动态组队能力上的差异。

**「评论」** 社区认可多智能体团队协作在科研工程场景的潜力，有用户引用自适应 harness 研究佐证该方向的价值。同时存在分歧，部分用户认为/teamwork 与 Claude 动态工作流差异不明显，且当前缺少自动模式、使用说明不足，实用性待验证。

**标签**: `#harness`, `#orchestration`, `#coding-agent`, `#eval`

---

<a id="item-agent-engineer-2"></a>
### [长周期智能体决策模型三角色研究](https://huggingface.co/papers/2611.17167) ⭐️ 7.0/10

2026 年 11 月 14 日，Hugging Face Daily Papers 推送论文《Actor, Judge, or Teacher?》。研究在 ALFWorld 与 WebShop 基准对比三个决策模型和三个通用 LLM。所有模型作为 actor 时都会被更容易的子目标分散，偏离必须先完成的关键子目标。作为 judge 观察完整轨迹时，模型会认可朝向关键前置子目标的推进步骤。研究还验证动作表现较差的决策模型仍可作为有效教师，通过 JEV 在 ALFWorld 与 WebShop 上训练智能体策略。该结论对长周期智能体组件选型、评测体系构建和训练流程设计有直接参考价值。

rss · Hugging Face Daily Papers · 11月14日 23:00

**「为什么重要」** 该研究首次系统区分决策模型在长周期智能体中的 actor、judge、teacher 三种角色，并揭示动作能力与教学能力可能解耦。相关结论可指导智能体组件选型与流程设计，对架构设计、评测体系构建和训练流程优化有直接参考价值。

**「可关注」** 可关注：在长周期任务中，可尝试将动作表现一般但评估能力强的决策模型分离出来，专职担任 judge 或 teacher，而非强制要求同一模型承担所有角色。

**标签**: `#eval`, `#orchestration`

---

<a id="item-agent-engineer-3"></a>
### [SO-Arena 基准测试发布](https://huggingface.co/papers/2611.15777) ⭐️ 6.0/10

2026-11-14，Hugging Face Daily Papers 发布 SO-Arena 基准测试，用于评估 System One 模型。该基准覆盖 11 个领域与 5 个能力家族，提供基于可靠来源的评估、手动验证的参考标签，以及领域特定的细粒度难度标准。当前材料为截断公告，未披露完整技术细节、性能对比数据或实际采用案例，对工程师的即时可操作性有限。

rss · Hugging Face Daily Papers · 11月14日 23:00

**「为什么重要」** System One 模型以低 token、快速决策为卖点，但现有基准多关注聚合性能，难以刻画能力边界与决策可靠性。SO-Arena 试图填补这一空白，但其评估框架的实际区分度与工程可用性尚待完整论文验证。

**「可关注」** 可关注：SO-Arena 将 System One 模型评估拆分为能力谱系与决策可靠性两个维度，并引入细粒度难度标准，这与当前依赖聚合性能的基准形成对比。

**标签**: `#eval`, `#harness`, `#orchestration`

---

<a id="item-agent-engineer-4"></a>
### [HF 每日论文：Duo 全双工世界模型](https://huggingface.co/papers/2611.15131) ⭐️ 6.0/10

2026 年 11 月 14 日 Hugging Face 每日论文收录预印本 arXiv:2611.15131，该文提出互惠世界模型（RWM）及全双工模型 Duo v1，将认知意图与视听实现能力作为世界模型的同等基础组件，支持实时连续的多模态感知与交互响应。当前公开内容截断，未披露性能数据、开源代码，也无对现有智能体工具链或评测体系的直接改进说明，仅对全双工多模态智能体细分领域有较窄参考价值，需阅读全文获取可落地技术细节。

rss · Hugging Face Daily Papers · 11月14日 23:00

**「为什么重要」** 该预印本提出将认知意图纳入世界模型核心组件的思路，对全双工多模态智能体研发有参考价值；但目前公开内容不完整，尚未证实其对现有智能体工具链或通用评测体系有直接改进作用。

**「可关注」** 可关注全双工世界模型整合意图认知与视听实现的技术路径，但需等待全文公开与开源代码验证落地性。

**标签**: `#orchestration`, `#eval`, `#world-model`, `#multimodal-agent`

---

<a id="item-agent-engineer-5"></a>
### [Open Vision Banana 方案](https://huggingface.co/papers/2611.15844) ⭐️ 6.0/10

2026-11-14，Hugging Face Daily Papers 发布论文《Open Vision Banana: A Fully Open Recipe for Generative Visual Perception》，提出 Open Vision Banana \(OVB\) 这一将预训练图像生成器转换为统一多任务感知系统的完全开放、可复现配方，公开数据、权重、代码与实现细节。研究基于 4B 与 9B 参数开源权重基础模型，使用 210 万至 380 万条公共数据集训练对，分析颜色编码、提示设计、参数适配与任务平衡四类设计选择对泛化性能的影响，指出这些选择相互作用的特性：单独有益的选择组合后可能损害性能。该工作对开发视觉 agent 能力的工程师有参考价值，但在视觉感知以外的更广泛 agent 工程场景中相关性有限。

rss · Hugging Face Daily Papers · 11月14日 23:00

**「为什么重要」** 该论文提供了完全开放的生成式视觉感知系统构建配方，弥补了 Vision Banana 工作缺乏可复现实现的空白。对正在开发视觉能力的 coding agent 工程师而言，其关于设计选择相互作用的分析可直接参考；但论文未展示在真实 agent harness 中的部署效果，外部泛化能力尚未证实。

**「可关注」** 可关注设计选择之间的相互作用对泛化性能的非线性影响——单独有益的选择（如特定颜色编码或提示设计）组合后可能损害性能，提示多组件系统需整体评估而非孤立调优。

**标签**: `#perception`, `#generative-model`, `#open-recipe`, `#multi-task`

---

<a id="item-agent-engineer-6"></a>
### [Qwen3 投机解码草稿模型 trending 上线](https://huggingface.co/tencent/Qwen3.8-27B-DSpine-b16) ⭐️ 6.0/10

2026 年 11 月 14 日，Hugging Face trending 上线腾讯推出的 tencent/Qwen3.8-27B-DSpine-b16 模型，该模型为 Qwen3 系列优化的投机解码草稿模型，采用 safetensors 格式，trendingScore 为 231，获赞 272 次，标签包含 qwen3、dspine、speculative-decoding、draft-model、sglang、text-generation，附带关联 arxiv 论文（编号 2609.36173）。该模型兼容 SGLang 推理框架，可用于加速大模型文本生成推理，对 Agent 系统推理链路有潜在优化价值。当前公开材料仅包含模型 trending 元数据，无具体性能指标、使用指南或技术实现细节，实际收益需进一步查看模型仓库或关联论文评估。

rss · Hugging Face Trending Models · 11月14日 23:00

**「为什么重要」** 该模型针对 Qwen3 系列优化投机解码方案，若性能达标可降低大模型文本生成推理成本，对运行 Agent 系统的推理 harness 有潜在参考价值；但目前无公开性能数据，实际加速效果尚未证实。

**「可关注」** 可关注：该投机解码草稿模型兼容 SGLang 推理框架，后续可留意其公开的性能指标与使用文档，评估是否可用于现有 Agent 推理链路的加速验证。

**标签**: `#harness`, `#speculative-decoding`, `#inference-optimization`

---

## AI 日报
{: #sec-ai-daily .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-daily" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-daily-1"></a>
### [82 亿收购后 李飞飞苏姿丰 CoRL 首同台](https://mp.weixin.qq.com/s?__biz=MzA3MzI4MjgzMw==&amp;mid=2651074456&amp;idx=2&amp;sn=96fd9bd0e55a35b655b0a2dddd61264d) ⭐️ 5.5/10

2026 年 11 月 12 日，机器人学习顶会 CoRL 2026 在美国奥斯汀进入第三天，这是 AMD 宣布以约 82 亿美元全股票收购李飞飞创办的 World Labs 后，李飞飞与 AMD 董事长兼 CEO 苏姿丰首次公开同台对谈，对谈时长约半小时，覆盖物理 AI 市场机会、端到端基础模型边界、学界算力短缺、AI 时代读博选择等议题；苏姿丰判断物理 AI 尤其是机器人是未来几年数千亿美元量级的机会，李飞飞提出 AI 与计算已根本融合、多模态模型正走向融合。交易预计 2026 年底前完成交割，届时李飞飞将出任 AMD 执行副总裁兼首席科学家，直接向苏姿丰汇报。

rss · 机器之心 · 11月14日 03:34

**「为什么重要」** 这是收购完成后双方核心人物的首次公开对话，释放了 AMD 布局物理 AI 与机器人领域的方向信号，对谈内容涉及学界算力短缺、AI 研发路径等业界普遍关切的问题。

**「可关注」** 可关注：AMD 提出硬件、软件、系统协同优化的理念将延伸至机器人领域，未来 5 到 10 年该方向是重要投入方向。

**标签**: `#industry`, `#lab`

---