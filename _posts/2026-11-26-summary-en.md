---
layout: default
title: "Horizon Summary: 2026-11-26 (EN)"
date: 2026-11-26
lang: en
---

> From 187 items, 11 important content pieces were selected

---

**Agent Harness Architecture**
1. [Mastra Core 1.86.0 发布](#item-harness-arch-1) ⭐️ 8.8/10
2. [FastMCP v4.2.7a1 发布](#item-harness-arch-2) ⭐️ 5.5/10

**AI Agent Engineer**
1. [Nemotron 3.5 Parse 更新](#item-agent-engineer-1) ⭐️ 7.8/10
2. [科学家划定科研 AI Agent 红线](#item-agent-engineer-2) ⭐️ 7.8/10
3. [CUGA Indic 语音代理案例](#item-agent-engineer-3) ⭐️ 6.3/10
4. [VibeVideoAgent 训练免费框架发布](#item-agent-engineer-4) ⭐️ 6.0/10
5. [SlidesWeaver 论文提出多智能体编排方案](#item-agent-engineer-5) ⭐️ 6.0/10

**AI Daily**
1. [GitHub 应用现代化安全步骤选择指南](#item-ai-daily-1) ⭐️ 6.8/10
2. [Gemini 4 Neon 登顶 LiveBench](#item-ai-daily-2) ⭐️ 5.0/10

**AI Deals**
1. [Google AI 会员订阅避坑实操](#item-ai-deals-1) ⭐️ 8.0/10
2. [林易 API 回帖加群送 $18 额度](#item-ai-deals-2) ⭐️ 7.0/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [Mastra Core 1.86.0 发布](https://github.com/mastra-ai/mastra/releases/tag/%40mastra/core%401.86.0) ⭐️ 8.8/10

Mastra Core 1.86.0 发布 durable evented workflows 与 native durable Agent execution engine，\`startExperimentAsync\(\)\` 支持 \`durable: true\` 实现 crash-safe 实验。Knowledge importer 基础设施（实验性）提供 lease-based sync、batching、replay protection 与 settle/repair semantics。同时新增 \`createChannelTools\(\)\`、\`createSlackTools\(\)\`、\`knowledge\_activity\`、host-run \`principals\`/\`author\`，并将 \`executionEngine: &\#x27;durable&\#x27;\` 重命名为 \`&\#x27;default&\#x27;\`，\`get\_process\_output\` 的 \`wait: true\` 改为 \`waitSeconds\`（1–300）。

github · PaulieScanlon · Nov 25, 10:00

**「设计要点」** Durable execution 基于 evented workflow 与 pubsub 重投递实现 crash-safe 恢复，Agent durable 模式保留 streaming API。Knowledge importer 通过 \`KnowledgeStorage.importers\` 在数据库同一事务中维护 binding、cursor、run 与 writer guard，支持 in-memory、LibSQL、Postgres；host 可通过固定 \`principals\` 与 \`author\` 在 agent run 外执行 Knowledge 工具。

**「改了什么」** 实验支持 durable evented workflow，redeploy 或 crash 后不遗留 \`running\` 状态。Knowledge 增加实验性 importer 端到端契约与 runner，支持批量同步、租约与重放保护，新增 \`interrupted\` run status、\`knowledge\_activity\` 工具及 host-run \`principals\`/\`author\`。

**「评论」** 暂无社区评论。

**Tags**: `#runtime`, `#durable-execution`, `#memory`, `#tools`

---

<a id="item-harness-arch-2"></a>
### [FastMCP v4.2.7a1 发布](https://github.com/PrefectHQ/fastmcp/releases/tag/v4.2.7a1) ⭐️ 5.5/10

FastMCP v4.2.7a1 patches the skills proxy in the PrefectHQ MCP runtime. It skips legacy MCP backends during discovery, filters malformed entries from proxied skill lists, and accepts percent-encoded slashes in skill URI prefixes. These changes improve discovery reliability and URI handling for MCP clients.

github · github-actions\[bot\] · Nov 26, 01:00

**「改了什么」** The skills proxy now ignores legacy MCP backends and drops malformed entries from skills/list responses \(PR \#6828\). It also decodes percent-encoded slashes in skill path prefixes \(PR \#6827\) and sanitizes proxy validation warnings \(PR \#6830\).

**Tags**: `#mcp`, `#runtime`, `#tools`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [Nemotron 3.5 Parse 更新](https://huggingface.co/blog/nvidia/building-on-nemotron-35-parse-open-data-fine-tunin) ⭐️ 7.8/10

NVIDIA 于 2026-11-26 在 Hugging Face Blog 发布 Nemotron 3.5 Parse 文档模型更新。该模型将页面图像转为结构化数据，面向 RAG 与 agent 工作流。本次更新开源三份合成训练数据集（Synthetic Charts V1 9.98M 条、Synthetic Tables V1 1M 条、OCR Synthetic Multilingual v2 7.9M 条），并公开基于 NeMo 的微调 recipe 与 DFlash2 推测解码加速方案。模型采用 SFT 接 RLVR（GRPO）的两阶段训练；在匹配评估的开发检查点上，循环标记输出从 126 页降至 29 页（降幅约 77%），整体得分从 66.24 提升至 71.38。在单张 H200、BF16 精度、2,078 页基准测试中，DFlash2 将并发 1 时吞吐提升 7.62 倍，并发 512 时提升 1.52 倍；Parse 3.5 还支持单次、双次、三次重处理流程以处理复杂区域，其中双次与三次流程在参考评估中分别提升 2.18 与 2.46 ParseBench 分。

rss · Hugging Face Blog · Nov 26, 05:05

**「为什么重要」** 本次更新公开了 Nemotron Parse 的完整训练数据、微调脚本与 DFlash2 推理加速实现，为文档解析模型在 RAG/agent 场景中的定制提供了可复用的基础资源。SFT+RLVR 的两阶段训练流程配合可验证奖励，展示了在结构化输出任务上提升一致性的可行路径，但文中未提供该 pipeline 在用户自有数据上的迁移效果。

**「可关注」** 可关注：DFlash2 在 H200 BF16 上并发 1 时吞吐提升 7.62 倍，但并发 512 时增益降至 1.52 倍，说明 speculative decoding 的收益与并发度存在明显权衡，需按实际部署场景验证。

**Tags**: `#rag`, `#fine-tuning`, `#inference`, `#agent-workflow`, `#document-model`

---

<a id="item-agent-engineer-2"></a>
### [科学家划定科研 AI Agent 红线](https://huggingface.co/blog/allenai/where-scientists-draw-the-line-on-ai-agents) ⭐️ 7.8/10

这篇 Hugging Face 博客文章整理了 Ai2 对 17 位科学家的访谈。文章提出科研 AI Agent 的五项信任维度：验证、隐私、客观性、问责与透明。科学家要求掌控任务分配、运行逻辑与评估标准，并强调可复现性、文件访问边界与物理安全约束。文章建议构建由科学家参与定义的基准测试，但相关方案仍处于提案阶段，尚未形成标准。

rss · Hugging Face Blog · Nov 25, 18:52

**「为什么重要」** 科研场景对 AI Agent 的约束涉及可复现性、隐私保护与物理安全等硬性要求，远高于通用任务。这些发现直接影响科研垂直领域 coding agent 与 harness 的权限设计、审计机制与验证流程。

**「可关注」** 可关注：科研 Agent 的评估应覆盖文件访问越界检测、方法可复现性与矛盾证据识别，而非仅看任务完成率。

**Tags**: `#permissions`, `#observability`, `#eval`, `#harness`

---

<a id="item-agent-engineer-3"></a>
### [CUGA Indic 语音代理案例](https://huggingface.co/blog/ibm-research/an-indic-voice-agent-with-cuga) ⭐️ 6.3/10

IBM Research 于 2026-11-25 在 Hugging Face Blog 发布案例。该案例介绍开源 CUGA \(Configurable Generalist Agent\) 代理框架，该框架为 AppWorld Benchmark 领先方案。研究团队用其构建印度语言语音代理，面向农民等用户，支持 Hindi、Tamil、Telugu 等 Indic 语言语音提问。流程为：语音经 speech-to-text 转文本，通过 CUGA 的 knowledge.search 检索知识库，生成 grounded answer 后经 text-to-speech 返回语音。关键工程决策包括：采用 multilingual-e5-large 嵌入模型解决跨语言检索问题。默认英文嵌入模型对 Hindi 等语言向量无意义。通过 OFF\_TOPIC 标签实现无二次 LLM 调用的离题重定向。支持 Sarvam AI 云端 API 与 SraVaani、Svara 开源模型两种语音方案。代理仅处理文本，语音层可独立替换。用户可在 Hugging Face Spaces 的 CUGA Apps 直接试用。配套教程从空文件夹逐层搭建。

rss · Hugging Face Blog · Nov 25, 10:22

**「为什么重要」** 该案例展示 agent harness 在 multilingual、voice-first 场景下的工程权衡。文本代理与语音层解耦设计降低切换成本。嵌入模型选择直接决定跨语言检索有效性。对构建区域语言数字服务的工程师有参考价值。

**「可关注」** 可关注：在非英语场景下，先验证嵌入模型的跨语言检索质量，再调整提示词或代理逻辑。

**Tags**: `#harness`, `#eval`, `#permissions`

---

<a id="item-agent-engineer-4"></a>
### [VibeVideoAgent 训练免费框架发布](https://huggingface.co/papers/2611.34237) ⭐️ 6.0/10

2026年11月26日，Hugging Face Daily Papers 分享 arXiv 预印本，介绍 VibeVideoAgent 训练免费框架。该框架让编码代理在视频生成生产过程中检查中间草稿，捕获非运行时渲染错误（如重叠标签、相机偏离、物体交互断裂、旁白不同步），减少中间输出导致的上下文膨胀，避免昂贵的后期重写。当前材料为截断摘要，缺少完整技术细节、性能基准及代码可用性信息，且代码驱动视频生成用例相对小众，对通用 AI 代理工程的价值尚未完全证实。

rss · Hugging Face Daily Papers · Nov 26, 00:00

**「为什么重要」** 它触及编码代理处理非运行时错误与中间上下文管理的共性痛点，但当前仅提供截断摘要，完整技术细节和性能数据缺失，实际影响范围尚未明确。

**「可关注」** 可关注：非运行时错误检测和中间上下文膨胀是编码代理的已知痛点，但需等待完整论文验证该训练免费方案的实际效果与开销。

**Tags**: `#coding-agent`, `#orchestration`, `#observability`

---

<a id="item-agent-engineer-5"></a>
### [SlidesWeaver 论文提出多智能体编排方案](https://huggingface.co/papers/2611.28010) ⭐️ 6.0/10

2026-11-26，Hugging Face Daily Papers 收录论文 2611.28010，提出多智能体系统 SlidesWeaver，用于生成可编辑且视觉丰富的 PPTX 演示文稿。该系统通过共享 deck 级与 slide 级状态、分阶段多模态承诺、扩散模型构图规划，协调语言与视觉智能体，结合程序化方法的可编辑性与图像方法的视觉丰富度。摘要内容截断，来源为二手 curated 信息，技术细节不完整，仅适合对多智能体编排感兴趣的工程师快速浏览后按需阅读全文。

rss · Hugging Face Daily Papers · Nov 26, 00:00

**「为什么重要」** 该论文展示了多智能体系统通过共享状态与分阶段承诺协调异构智能体的具体机制，对设计 coding agent 中的多步骤协作流程有参考价值。但应用场景局限于演示文稿生成，且摘要截断，其编排方案的通用性尚未证实。

**「可关注」** 可关注 SlidesWeaver 的 deck/slide 级共享状态与分阶段多模态承诺机制，用于协调语言与视觉智能体在内容、布局和外观上的相互依赖。

**Tags**: `#orchestration`

---

## AI Daily

<a id="item-ai-daily-1"></a>
### [GitHub 应用现代化安全步骤选择指南](https://github.blog/ai-and-ml/github-copilot/how-to-choose-the-next-safe-step-in-application-modernization/) ⭐️ 6.8/10

GitHub 发布博客介绍应用现代化的证据优先方法论，通过四个公开应用案例演示可重复的决策流程。该方法要求先建立包含依赖、运行时 pin、外部契约等证据清单，并按保留、升级、替换、封装、重写的优先级选择最小侵入性方案。文章同时展示如何将该流程编码为 GitHub Copilot agent skill，同时保留架构判断权在系统负责人手中。文中定义 L0 到 L4 四级回归保护强度，并以 PiggyMetrics 为例说明旧系统可能比标签显示更具可维护性。

rss · GitHub Blog · Nov 25, 15:00

**「为什么重要」** 这篇文章将架构决策从经验判断转为可重复的证据收集流程，并直接落地到 Copilot 技能，对正在评估遗留系统改造的团队有直接参考价值。

**「可关注」** 可关注：先做 time-boxed 可行性检查，再决定走捕获行为后升级还是先建现代切片路径，避免在不可运行的系统上要求完整测试套件。

**Tags**: `#product`, `#lab`

---

<a id="item-ai-daily-2"></a>
### [Gemini 4 Neon 登顶 LiveBench](https://mp.weixin.qq.com/s?__biz=MzI3MTA0MTk1MA==&amp;mid=2652745183&amp;idx=2&amp;sn=9e2398515e5d4f23adafd26dd399519e) ⭐️ 5.0/10

新智元 11 月 25 日发布的二手报道称 Gemini 4 Neon 在重构后的 LiveBench 2.0（长流程版，含 7 个子项 471 道题）中以 87.4 分登顶总榜，领先并列第二的 Claude Fable 5.2、GPT-6.2 Astra 2.5 分；但该消息无官方来源核实，且该模型在 Artificial Analysis 智力指数 v5.0.1 中仅排第三，单成功任务成本为 2.654 美元，高于 GPT-6.2 Astra 的 1.941 美元。

rss · 新智元 · Nov 25, 09:40

**「为什么重要」** 单一长流程榜单的头部排名容易掩盖模型在通用能力、成本上的差异，跨榜单对比能更准确判断模型适配场景。

**「可关注」** 可关注：Gemini 4 Neon 在长流程工具调用类任务上表现突出，但单任务成本高于 GPT-6.2 Astra，需按实际场景权衡选型。

**Tags**: `#model`, `#eval`, `#industry`

---

## AI Deals

<a id="item-ai-deals-1"></a>
### [Google AI 会员订阅避坑实操](https://www.v2ex.com/t/1259690#reply20) ⭐️ 8.0/10

FringJX 在 V2EX 分享谷歌 AI 会员订阅的实操避坑经验。账号关联地区需通过 policies.google.com/country-association-form 设置，不能为中国或香港，否则无法使用反重力功能；Play 商店地区控制谷歌 AI 权益、家庭组及付款，切换需添加支付方式，且不能直接用香港地区支付方式购买，需将商店地区切换为日本、美国或新加坡。支付需使用单币 Visa 或万事达，招行双币信用卡会被识别为银联不支持。年费五折优惠需先开通低价 Plus 订阅再覆盖，跳板订阅成本越低越好。

rss · V2EX Hot · Nov 25, 05:38

**「为什么重要」** 当前谷歌 AI 会员订阅存在地区归属、支付方式、优惠获取三重限制，该经验汇总了已验证的避坑路径，可降低用户订阅失败的概率与成本。

**「可关注」** 可关注：订阅前需先完成账号关联地区与 Play 商店地区的双重设置，支付优先选单币 Visa/万事达避开招行双币卡限制，年费五折可通过先开低价 Plus 再覆盖的方式获取。

**Tags**: `#promo`, `#coupon`, `#api`

---

<a id="item-ai-deals-2"></a>
### [林易 API 回帖加群送 $18 额度](https://www.v2ex.com/t/1259773#reply53) ⭐️ 7.0/10

林易 API（第三方AI大模型API中转平台）发起推广活动，回帖可领$8 API额度，加指定QQ群可再领$10，合计最高$18。领取需先在linyiapi.ai注册账号，回帖提交注册邮箱前缀（或注册后修改用户名），进群发送指定信息，两份额度可叠加，每个V2EX账号、每个林易账号每份福利各限领1次，批量注册小号领额度的额度会被扣除。额度无有效期，仅可用于按量付费，不可购买套餐、不可退款，活动长期有效（帖子持续存在即可参与）。

rss · V2EX Hot · Nov 25, 09:12

**「为什么重要」** 额度无有效期，平台标注GPT按量最低为官方价1.35折，且支持Claude Code、Codex CLI等常用编码工具，仅需修改Base URL和Key即可接入，适合想低成本试用多家主流模型的开发者。

**「可关注」** 可关注：赠送额度仅支持按量付费，不可购买套餐；创建Key时选择的分组决定可调用模型范围与计费倍率，当前按量分组倍率在×0.52到×2.8之间。

**Tags**: `#promo`, `#credits`, `#api`, `#limited-free`

---