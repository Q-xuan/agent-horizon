---
layout: default
title: "Horizon Summary: 2026-11-22 (EN)"
date: 2026-11-22
lang: en
---

> From 140 items, 10 important content pieces were selected

---

**Agent Harness Architecture**
1. [Cline SDK v0.2.1 发布](#item-harness-arch-1) ⭐️ 5.5/10
2. [fastmcp v4.2.4 安全补丁发布](#item-harness-arch-2) ⭐️ 5.3/10

**AI Agent Engineer**
1. [AltRA-Test 提出稀疏标注 LLM Judge 验证方法](#item-agent-engineer-1) ⭐️ 6.0/10
2. [TuringSpace 空间智能基准发布](#item-agent-engineer-2) ⭐️ 6.0/10
3. [HF 每日论文：ZeroVLN 免微调导航框架](#item-agent-engineer-3) ⭐️ 6.0/10
4. [Mind2Act World 机器人操作诊断基准](#item-agent-engineer-4) ⭐️ 5.5/10

**AI Daily**
1. [腾讯元宝×KCL 发布 Agent 记忆基准](#item-ai-daily-1) ⭐️ 5.5/10
2. [Karpo Decision 31B 开源](#item-ai-daily-2) ⭐️ 5.5/10
3. [TML开源Inkling 2 Mini模型](#item-ai-daily-3) ⭐️ 5.5/10

**AI Deals**
1. [Google AI Pro 黑五五折 老用户可提前领](#item-ai-deals-1) ⭐️ 8.0/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [Cline SDK v0.2.1 发布](https://github.com/cline/cline/releases/tag/sdk/sdk/v0.2.1) ⭐️ 5.5/10

这是 Cline 项目的 SDK v0.2.1 版本发布，核心围绕工具结果处理、推理逻辑兼容性、Hub 云能力与工具集展开优化，新增多项面向 harness 工程师的可选工具与接口，同步刷新模型目录与默认模型配置。

github · github-actions\[bot\] · Nov 21, 05:19

**「设计要点」** 运行时支持可中断的会话压缩流程，工具层新增 MCP 工具注解透传、自定义模型能力自动 seeding 机制，Hub 云服务新增分块历史返回、沙箱外工件下载能力，权限层要求 provider 管理类 Hub 命令必须使用 token 鉴权。

**「改了什么」** 工具结果上限调整，read\_files 结果取消 8k 截断改用 50k 上限，其余工具维持 8k 上限；新增 interleaved reasoning 占位字段修复模型压缩/切换后的参数缺失错误，调整摘要器推理偏好、自定义模型能力 seeding 与 OpenAI/LiteLLM 适配逻辑避免端点拒绝；新增 ux\_verifier、publish\_artifacts 可选工具，Hub 云会话支持分块历史返回与沙箱外工件下载，同步刷新模型目录与默认模型配置。

**Tags**: `#runtime`, `#tools`, `#prefix-cache`

---

<a id="item-harness-arch-2"></a>
### [fastmcp v4.2.4 安全补丁发布](https://github.com/PrefectHQ/fastmcp/releases/tag/v4.2.4) ⭐️ 5.3/10

fastmcp v4.2.4 修复 OAuth proxy 授权码与刷新令牌并发兑换 race condition（GHSA-78c8-3jhx-5mg7），并阻止已撤销的 proxy access token 在刷新后重新生效。工具转换失败时仅隐藏自身工具，不再破坏整个工具列表。挂载与版本化组件修复重复版本列出、父级 twin 隐藏时子组件响应异常，以及合并默认值破坏调用者对象的问题，新增混合版本化/非版本化组件挂载警告。

github · zzstoatzz · Nov 21, 05:24

**「改了什么」** 修复 OAuth proxy 并发兑换 race condition 与已撤销 token 刷新后重新生效的安全问题。工具转换失败仅隐藏自身工具，不再破坏整个列表；挂载混合版本化/非版本化组件时发出警告，并修正版本化组件重复列出、父级 twin 隐藏时子组件响应及合并默认值保留调用者对象。

**Tags**: `#mcp`, `#runtime`, `#tools`, `#permissions`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [AltRA-Test 提出稀疏标注 LLM Judge 验证方法](https://huggingface.co/papers/2611.26073) ⭐️ 6.0/10

2026-11-21，Hugging Face Daily Papers 介绍 AltRA-Test 统计检验方法。该方法针对稀疏标注场景设计，无需所有标注项由同一批标注者完成，弥补了此前 Alt-Test 仅适用于密集标注场景的局限。其通过 bootstrap 重采样 items，对每个 item 抽取 k 个人工标注并替换其中一个为 LLM 标注，为验证 LLM 替代人工标注员的统计合理性提供新工具。该方法对使用 LLM 作为评测 judge 的 agent 工程师有参考价值，但适用场景聚焦于标注验证领域，无通用 agent 工程相关的突破性更新。

rss · Hugging Face Daily Papers · Nov 21, 23:00

**「为什么重要」** AltRA-Test 针对稀疏标注场景设计，无需共享标注者即可验证 LLM 替代人工的统计合理性，扩展了现有检验方法的适用范围。但当前研究仅聚焦标注验证领域，尚未证实对通用 agent 工程或 LLM 评测工作流的直接影响。

**「可关注」** 在稀疏标注场景下评估 LLM judge 时，可参考 AltRA-Test 的 bootstrap 设计，通过重采样 items 并替换单个人工标注为 LLM 标注的方式验证替代统计合理性。

**Tags**: `#eval`, `#llm-judge`, `#annotation-validation`

---

<a id="item-agent-engineer-2"></a>
### [TuringSpace 空间智能基准发布](https://huggingface.co/papers/2611.25387) ⭐️ 6.0/10

2026-11-21，Hugging Face Daily Papers 发布论文《TuringSpace: Grounding Spatial Intelligence in Action with Interactive CAPTCHAs》。该研究提出可扩展交互式 CAPTCHA 基准 TuringSpace，包含 125 个程序生成任务，覆盖五种空间能力，要求模型通过屏幕点击与拖拽解决。每项任务内置检查器与预言机，兼作训练环境。该资源面向多模态 LLM 的空间推理与交互行动评估，对构建视觉-空间交互 agent 的工程师有参考价值，但属小众研究资源，未直接影响主流 agent 工具链或引发重大变更。

rss · Hugging Face Daily Papers · Nov 21, 23:00

**「为什么重要」** 当前主流 agent 评估多聚焦文本或静态视觉，该基准提供可交互空间任务，填补了空间推理与物理行动结合评估的空白。但尚未见到实际集成到主流框架的报道，影响范围待观察。

**「可关注」** 程序生成任务配合内置检查器的设计模式，可复用于构建可扩展的 agent 交互式评估环境。

**Tags**: `#eval`

---

<a id="item-agent-engineer-3"></a>
### [HF 每日论文：ZeroVLN 免微调导航框架](https://huggingface.co/papers/2611.26414) ⭐️ 6.0/10

2026年11月21日Hugging Face每日论文推荐了一篇视觉语言导航（VLN）预印本，提出名为ZeroVLN的慢-快导航框架。该框架无需对VLM大脑做导航域有监督微调，而是通过语义工具调用接口以自然语言传递移动决策给专用动作专家，先完成动作专家对移动请求的适配，再联合优化VLM大脑的决策质量与动作专家的协同能力。当前仅公开预印本内容，未提供生产级实现细节或可泛化的评估结果，该条目获得22次upvote。

rss · Hugging Face Daily Papers · Nov 21, 23:00

**「为什么重要」** 该工作提出的「免微调VLM大脑+语义工具调用对接动作专家」的范式，与当前AI Agent的工具编排、MCP对齐集成及评估设计方向存在关联。但目前仅为预印本，未公开可复现的评估结果，相关范式对通用场景的适用性尚未证实。

**「可关注」** 可关注：将VLM的领域决策能力通过语义工具调用接口卸载给专用专家模块，或可降低大模型微调对通用能力的损耗，同时适配Agent工具编排场景。

**Tags**: `#orchestration`, `#eval`, `#mcp`

---

<a id="item-agent-engineer-4"></a>
### [Mind2Act World 机器人操作诊断基准](https://huggingface.co/papers/2611.26444) ⭐️ 5.5/10

On November 21, 2026, Hugging Face Daily Papers curated an arXiv preprint introducing Mind2Act World, a diagnostic benchmark for embodied robotic manipulation. The benchmark includes 30 simulated manipulation tasks across 5 real-world application domains, with each task set to 3 difficulty levels and 2 scene settings \(Clean and Random\), totaling 180 task configurations. Its core design decouples agent failure modes into reasoning, execution, and reasoning-execution composition, addressing the limitation of existing benchmarks that either evaluate reasoning and execution in the same tasks or assess them separately without covering their composition. Currently, the public content lacks full evaluation metrics, baseline results, and toolchain integration details. It has reference value for evaluation work in embodied intelligence and robotic manipulation fields, but has limited direct relevance to most coding agent engineers. This curation received 50 upvotes on Hugging Face Daily Papers. This is a second-hand curation without an official first-hand release \(official blog, GitHub repository, or official documentation\), with an analysis score capped at 5.5.

rss · Hugging Face Daily Papers · Nov 21, 23:00

**「为什么重要」** The decoupled diagnostic evaluation design that splits failure modes into reasoning, execution, and composition can be migrated to other agent evaluation scenarios. However, the current benchmark only covers robotic manipulation, has limited direct reference value for most coding agent engineers, and does not disclose production-level practices that can be directly reused.

**「可关注」** Pay attention to the decoupled design of diagnostic evaluation that separates reasoning, execution, and composition failure modes, which can be reused in fault localization scenarios for other coding agents.

**Tags**: `#eval`, `#embodied-agent`

---

## AI Daily

<a id="item-ai-daily-1"></a>
### [腾讯元宝×KCL 发布 Agent 记忆基准](https://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw==&amp;mid=2247947677&amp;idx=3&amp;sn=0797fbd2116a405b44176c97577757d8) ⭐️ 5.5/10

腾讯元宝与伦敦国王学院 NLP 团队联合发布首个基于群聊构建的 Agent 记忆基准 GroupAssistBench。基准基于 50 个真实群聊、80,299 条历史消息构建 2,395 道评测题，检查 Agent 记忆能否从“记得住”走向“用得好”。研究比较完整上下文、检索增强和外部记忆等 14 组配置，EverMemOS 在 L1 记忆召回中得分 0.621，高于完整上下文得分 0.570，但在 L2 开放式服务中得分 0.247，低于完整上下文得分 0.431。

rss · 量子位 · Nov 21, 09:52

**「为什么重要」** 群聊场景要求 Agent 不仅召回历史，更要在正确时刻判断该使用谁的哪条记忆。该基准首次量化了多人群聊中“记得住”与“用得好”之间的落差。

**「可关注」** 可关注：EverMemOS 在 L1 记忆召回中得分 0.621，高于完整上下文得分 0.570，但在 L2 开放式服务中得分 0.247，低于完整上下文得分 0.431，显示记忆召回与服务使用存在显著反差。

**Tags**: `#lab`, `#industry`, `#eval`, `#product`

---

<a id="item-ai-daily-2"></a>
### [Karpo Decision 31B 开源](https://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw==&amp;mid=2247947677&amp;idx=1&amp;sn=ebf1f96b9afceacdfa0d407ecdb3ff2b) ⭐️ 5.5/10

MachinePulse AI开源的Karpo Decision 31B决策模型，在《城市扫描仪》挑战中耗时2.6秒，约为Gemini 3.5 Flash（14.96秒）的6倍，成本仅为后者的十三分之一，36题准确率100%。单张RTX PRO 6000即可部署，中位响应时间94毫秒，在Decision Index评测总榜（300个模型）中以Full分73.9位列第一，校准误差2.3%，单题最多可同时判断255个候选选项。同时MachinePulse AI还开源了配套浏览器操作框架，包含karpo-browser框架、Karpo Decision 27B Act模型与KBB评测集，采用System 1 + System 2架构，在Browserbase Benchmark v2 102道核心任务上有对应表现。

rss · 量子位 · Nov 21, 09:52

**「为什么重要」** 该模型专为Agent高频低延迟决策设计，开源后可为浏览器Agent等场景提供更快的决策能力，降低部署成本。

**「可关注」** 可关注：Karpo Decision 31B单RTX PRO 6000即可部署，中位响应时间94毫秒，适合对时延敏感的Agent决策场景。

**Tags**: `#model`, `#open-source`, `#industry`, `#agent`

---

<a id="item-ai-daily-3"></a>
### [TML开源Inkling 2 Mini模型](https://mp.weixin.qq.com/s?__biz=MzA3MzI4MjgzMw==&amp;mid=2651075624&amp;idx=2&amp;sn=b6e7e23d631dba7a952cbe5da8e77769) ⭐️ 5.5/10

Thinking Machines Lab（TML）开源26B参数循环Transformer多模态模型Inkling 2 Mini，权重按Apache 2.0许可发布，支持文本、图像输入，最大上下文窗口100万token。该模型总参数26B，激活参数约3.4B，循环计算后有效激活参数约5.4B，官方宣称可在笔记本运行，公开演示基于配备48GB内存的M5 Pro MacBook Pro离线完成写可玩飞行模拟器、驱动20位像素小镇村民日常交互等任务，AA Index得分20.1。

rss · 机器之心 · Nov 21, 04:11

**「为什么重要」** 它验证了循环Transformer架构在端侧部署多模态智能体任务的可行性，为低算力场景下的复杂模型应用提供了新参考。

**「可关注」** 可关注：循环Transformer通过重复利用中间12层网络（前6层、后6层各运行1次，中间12层运行3次），让24层权重实现每token 48次层计算，在控制权重大小的同时提升任务处理能力。

**「评论」** 社区已尝试将其接入DeepSeek Harness获得较快推理速度，还实现了游戏速通、生成动画MV等落地玩法。

**Tags**: `#model`, `#open-source`, `#lab`, `#eval`

---

## AI Deals

<a id="item-ai-deals-1"></a>
### [Google AI Pro 黑五五折 老用户可提前领](https://www.appinn.com/google-ai-pro-black-friday-2026/) ⭐️ 8.0/10

你看到的内容可能由第三方 AI 基于小众软件文章提炼总结而成，可能与原文真实意图存在偏差。不代表小众软件观点和立场。请&lt;a href=&quot;https://www.appinn.com/google-ai-pro-black-friday-2026/&quot; target=&quot;\_blank&quot;&gt;点击链接阅读原文&lt;/a&gt;细致比对和校验。&lt;br /&gt;&lt;br /&gt;Google 在美区推出 AI Pro 及 AI Plus 年付套餐黑五五折活动，优惠后年费约 99.99 美元，折合每月 8.33 美元。11 月 20 日至 26 日现有 Google One、Google AI 订阅老用户可提前参与，11 月 27 日起向符合条件的新用户开放。部分账户参与限制未完整披露，最终以 Google 结算页面为准。

rss · 小众软件 · Nov 21, 11:14

**「为什么重要」** 活动当前对美区老用户已开放，优惠后年费包含 5TB Google One 存储与 Gemini 高级功能，对已有 Google One 订阅的用户性价比高于单独购买对应服务。

**「可关注」** 可关注：仅美区符合条件账户可参与，老用户可直接在 Google One 设置尝试升级，首个优惠周期后续费将恢复原价。

**Tags**: `#promo`, `#coupon`, `#limited-offer`, `#subscription`

---