---
layout: default
title: "Horizon Summary: 2026-11-15 (EN)"
date: 2026-11-15
lang: en
---

> From 152 items, 9 important content pieces were selected

---

**Agent Harness Architecture**
1. [LangGraph 1.2.22 发布](#item-harness-arch-1) ⭐️ 5.3/10
2. [browser-use 1.0.5 发布](#item-harness-arch-2) ⭐️ 5.3/10

**AI Agent Engineer**
1. [Google Research 发布 Antigravity /teamwork 功能](#item-agent-engineer-1) ⭐️ 7.0/10
2. [长周期智能体决策模型多角色研究发布](#item-agent-engineer-2) ⭐️ 7.0/10
3. [SO-Arena 基准发布](#item-agent-engineer-3) ⭐️ 6.0/10
4. [HF每日论文：Duo 全双工世界模型发布](#item-agent-engineer-4) ⭐️ 6.0/10
5. [Open Vision Banana 全开放视觉感知配方](#item-agent-engineer-5) ⭐️ 6.0/10
6. [腾讯Qwen3投机解码模型登HF Trending](#item-agent-engineer-6) ⭐️ 6.0/10

**AI Daily**
1. [CoRL 2026 李飞飞苏姿丰收购后首同台](#item-ai-daily-1) ⭐️ 5.5/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [LangGraph 1.2.22 发布](https://github.com/langchain-ai/langgraph/releases/tag/1.2.22) ⭐️ 5.3/10

LangGraph 1.2.22 为补丁版本，修复子图流式传输的线程调度问题，并引入五项运行时性能优化。修复确保调用方流式消费子图时，子图在独立线程上运行。性能优化包括跳过纯消息的 add\_messages 转换、按任务过滤待处理写入、宽状态下的键集合匹配、仅检查失败 futures 的 runner 停止条件，以及每次运行仅执行一次未追踪和增量通道查找。配套发布 checkpoint-postgres 3.2.1、prebuilt 1.1.2 与 checkpoint 4.3.2。

github · github-actions\[bot\] · Nov 14, 01:43

**「设计要点」** 子图执行采用独立线程模型，调用方流式消费时不会阻塞子图运行。运行时通过减少消息转换、过滤写入状态、集合化键匹配和延迟通道追踪降低开销。

**「改了什么」** 修复子图流式传输的线程模型，确保调用方流式消费子图时子图在独立线程运行。新增五项性能优化：纯消息跳过 add\_messages 转换、按任务过滤待处理写入、宽状态键集合匹配、仅检查失败 futures、每次运行单次通道追踪。

**Tags**: `#runtime`, `#subagents`

---

<a id="item-harness-arch-2"></a>
### [browser-use 1.0.5 发布](https://github.com/browser-use/browser-use/releases/tag/1.0.5) ⭐️ 5.3/10

browser-use 1.0.5 正式发布。本次更新引入可配置的基于模型的运行评判功能，每次浏览器代理任务运行均由用户自有模型进行评判，结果填充 \`result.judgement\` 字段，包含成功状态、失败原因、描述、提示注入检测、机器人拦截检测及站点反制细节。可通过 \`judge\_context=\` 传入评判标准，或 \`judge=False\` 关闭；同时恢复 0.x 版本的 \`use\_judge\` 与 \`ground\_truth\` 标志。评判器默认查看运行 trace、最后截图及最终页面（\`use\_vision=False\` 时除外），并在站点拒绝输入、报错、拦截或限速时写入 gotchas，即使运行成功也不例外。

github · sarath-menon · Nov 14, 08:24

**「改了什么」** 新增基于模型的运行评判机制，每次运行自动生成结构化 \`result.judgement\`；恢复旧版 \`use\_judge\` 与 \`ground\_truth\` 标志；改进站点反制 gotcha 检测，使站点拒绝输入、报错、拦截或限速场景的检出率从 6/15 提升至 15/15，同时保持成功 verdict 不变。

**Tags**: `#tools`, `#eval`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [Google Research 发布 Antigravity /teamwork 功能](https://research.google/blog/advancing-science-engineering-with-antigravitys-teamwork-feature/) ⭐️ 7.0/10

2026年11月14日Google Research发布博客，介绍Antigravity的/teamwork功能，支持科学与工程任务下的动态多智能体协作。社区反馈显示该功能此前已在Antigravity官方博客部分披露，当前仍在持续迭代，同时有用户将其与Claude动态工作流对比，质疑功能差异与成熟度，博客全文技术细节未完全公开。

hackernews · acossta · Nov 14, 13:20 · [Discussion](https://news.ycombinator.com/item?id=50496811)

**「为什么重要」** 该功能直接对应多智能体编排与coding agent harness设计的行业热点方向，官方披露引发社区对动态团队协作落地的讨论；社区同时关联了自适应多智能体harness的相关研究，说明该方向的技术探索正在加速。

**「可关注」** 可关注动态多智能体harness的角色分配与非同质任务流适配方案，以及不同平台动态工作流能力的实际落地差异。

**「评论」** 社区共识是团队式多智能体工作流在减少质量损耗、提升自主性上有应用潜力，同时有用户指出Antigravity /teamwork与Claude动态工作流差异不明确，且当前缺乏自动模式与使用指引。

**Tags**: `#harness`, `#orchestration`, `#coding-agent`, `#eval`

---

<a id="item-agent-engineer-2"></a>
### [长周期智能体决策模型多角色研究发布](https://huggingface.co/papers/2611.17167) ⭐️ 7.0/10

Hugging Face Daily Papers 于 2026-11-14 推荐论文《Actor, Judge, or Teacher? Understanding Decision Models in Long-Horizon Agents》。该研究在 ALFWorld 与 WebShop 基准上，对比三个决策模型与三个通用 LLM 作为动作执行者（actor）、轨迹评估者（judge）和策略教师（teacher）的表现。实验发现，作为 actor 时，六种模型均会被更易子目标干扰而偏离关键前置子目标；作为 judge 时，它们会认可朝向该子目标的推进步骤；即使动作表现较差的决策模型，仍可作为有效教师（JEV）。结论对智能体组件选型与流程设计有参考价值。

rss · Hugging Face Daily Papers · Nov 14, 23:00

**「为什么重要」** 该研究首次系统揭示长周期智能体中决策模型的多角色能力可解耦：动作执行能力弱并不妨碍其承担评估或教学角色。这一结论对当前智能体架构中普遍采用的单一模型多角色复用模式提出反思，为组件解耦与专业化选型提供了实证依据。

**「可关注」** 可关注：在长周期智能体设计中，可尝试将 actor、judge、teacher 角色拆分给不同模型或配置，利用评估者对关键前置子目标推进步骤的认可特性，优化轨迹筛选与策略蒸馏流程。

**Tags**: `#eval`, `#orchestration`

---

<a id="item-agent-engineer-3"></a>
### [SO-Arena 基准发布](https://huggingface.co/papers/2611.15777) ⭐️ 6.0/10

2026 年 11 月 14 日，Hugging Face Daily Papers 发布 SO-Arena 基准测试，用于评估 System One 模型的能力谱系与决策可靠性。该基准覆盖 11 个领域和 5 个能力家族，提供基于可靠来源的证据锚定评估、细粒度领域难度分级，以及面向真实场景的验证机制。当前公告为 truncated 版本，未披露完整技术细节、性能对比数据或实际落地案例，对工程师的直接影响有限。

rss · Hugging Face Daily Papers · Nov 14, 23:00

**「为什么重要」** SO-Arena 针对快速低 token 的 System One 模型设计评估框架，填补了当前基准仅关注聚合性能、忽视决策可靠性的空白。但公告未提供可复现的实验设置或模型对比基线，其评估方法论的实际区分度尚未经社区验证。

**「可关注」** 可关注：SO-Arena 的证据锚定与细粒度评估设计，可能为低延迟 agent 的可靠性测试提供新范式，但需等待完整技术报告确认其难度分级与标注一致性。

**Tags**: `#eval`, `#harness`, `#orchestration`

---

<a id="item-agent-engineer-4"></a>
### [HF每日论文：Duo 全双工世界模型发布](https://huggingface.co/papers/2611.15131) ⭐️ 6.0/10

2026年11月14日Hugging Face每日论文收录预印本arXiv:2611.15131，提出互惠世界模型（RWM）及全双工模型Duo v1。RWM将认知意图、视听实现能力与物理现实并列为世界的核心构成要素，改变现有世界模型仅模拟物理现实、将推理决策作为外部控制的思路。Duo v1计划通过自回归建模等三项关键技术实现实时连续的视听感知与用户交互响应，但目前仅公开摘要，无性能数据、开源代码，也未说明对现有智能体工具链或评测体系的直接改进，仅对全双工多模态智能体细分领域有参考价值。

rss · Hugging Face Daily Papers · Nov 14, 23:00

**「为什么重要」** 该工作首次将认知意图纳入世界模型的核心构成框架，为全双工多模态智能体的感知-决策-响应一体化设计提供了新思路；但目前仅公开摘要，无落地技术细节与性能验证，实际工程价值尚未证实。

**「可关注」** 可关注该预印本全文发布后的技术细节公开情况，以及其设计是否对现有全双工多模态智能体的感知-响应链路有可复用的改进。

**Tags**: `#orchestration`, `#eval`, `#world-model`, `#multimodal-agent`

---

<a id="item-agent-engineer-5"></a>
### [Open Vision Banana 全开放视觉感知配方](https://huggingface.co/papers/2611.15844) ⭐️ 6.0/10

Hugging Face Daily Papers 于 2026-11-14 介绍 Open Vision Banana \(OVB\) 论文。该工作提出将预训练图像生成器转换为统一多任务感知系统的完全开放、可复现方案，基于 4B 与 9B 参数开源基模型，使用 210 万至 380 万训练数据对。论文分析了颜色编码、提示设计、参数适配和任务平衡等设计选择，指出这些因素会相互影响，单独有益的决策组合后可能损害性能。该方案对开发视觉感知能力的 agent 工程师有参考价值，但对 broader agent engineering 的适用性有限。当前材料中论文结论部分被截断。

rss · Hugging Face Daily Papers · Nov 14, 23:00

**「为什么重要」** OVB 首次公开了 Vision Banana 框架的完整数据、权重、代码与实现细节，填补了此前完全闭源的空白。其对设计选择相互作用的实证分析，为构建生成式视觉感知系统提供了可复现的基准。

**「可关注」** 可关注：将图像生成器迁移为感知系统时，颜色编码、提示设计、参数适配与任务平衡等设计选择存在交互效应，需联合调优而非孤立评估单个组件。

**Tags**: `#perception`, `#generative-model`, `#open-recipe`, `#multi-task`

---

<a id="item-agent-engineer-6"></a>
### [腾讯Qwen3投机解码模型登HF Trending](https://huggingface.co/tencent/Qwen3.8-27B-DSpine-b16) ⭐️ 6.0/10

2026年11月14日，Hugging Face Trending上线腾讯针对Qwen3系列优化的投机解码草稿模型tencent/Qwen3.8-27B-DSpine-b16，该模型采用safetensors格式，标签包含qwen3、dspine、speculative-decoding、draft-model、sglang，兼容SGLang推理框架，关联arxiv论文编号2609.36173，可用于加速包括Agent系统在内的大模型文本生成推理，当前trendingScore为231，获赞272次；目前仅公开trending元数据，无具体性能指标、使用指南或技术实现细节，实际收益需进一步查看模型仓库或关联论文评估。

rss · Hugging Face Trending Models · Nov 14, 23:00

**「为什么重要」** 投机解码是当前大模型推理加速的热门技术方向，该模型针对Qwen3系列优化且兼容主流推理框架SGLang，若实际性能达标可降低Agent等场景的推理成本，但目前仅公开元数据，实际落地价值尚未验证。

**「可关注」** 可关注该模型关联的arxiv论文2609.36173与模型仓库后续公开的技术细节，评估其投机解码方案对自身推理链路的适配性。

**Tags**: `#harness`, `#speculative-decoding`, `#inference-optimization`

---

## AI Daily

<a id="item-ai-daily-1"></a>
### [CoRL 2026 李飞飞苏姿丰收购后首同台](https://mp.weixin.qq.com/s?__biz=MzA3MzI4MjgzMw==&amp;mid=2651074456&amp;idx=2&amp;sn=96fd9bd0e55a35b655b0a2dddd61264d) ⭐️ 5.5/10

2026年11月12日，机器人学习顶会CoRL 2026在美国奥斯汀进入第三天，AMD此前宣布以82亿美元全股票交易收购李飞飞创办的World Labs、预计年底前完成交割，李飞飞将出任AMD执行副总裁兼首席科学家向苏姿丰汇报，二人当日完成收购后首次公开同台对谈，对谈时长约半小时，内容覆盖物理AI机会、端到端基础模型边界、学术界算力短缺等话题。苏姿丰称物理AI尤其是机器人是未来几年数千亿美元量级的机会，收购逻辑是加深对工作负载的理解以落地软硬协同优化；李飞飞提出「AI就是计算，计算就是AI」，认为多模态模型正走向融合，需硬件与软件协同演化。该内容为机器之心的二手整理报道，无对应官方一手信源。

rss · 机器之心 · Nov 14, 03:34

**「为什么重要」** 这是82亿美元收购案后双方核心人物的首次公开对谈，释放了AMD加码物理AI与机器人领域的明确信号，同时覆盖了当前机器人学习领域最关注的算力、模型架构走向等核心议题，对从业者判断行业趋势有参考价值。

**「可关注」** 可关注：物理AI领域软硬协同优化成为行业共识，学术界算力短缺是当前机器人学习落地的普遍瓶颈。

**Tags**: `#industry`, `#lab`

---