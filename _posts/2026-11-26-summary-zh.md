---
layout: default
title: "Horizon Summary: 2026-11-26 (ZH)"
date: 2026-11-26
lang: zh
---

> 从 187 条内容中筛选出 11 条重要资讯。

<nav id="ah-toc" class="ah-toc" aria-label="目录"><span class="ah-toc-title">目录</span><ul><li><a href="#sec-harness-arch"><span class="ah-toc-name">Harness 架构</span><span class="ah-toc-count">2条</span></a></li><li><a href="#sec-agent-engineer"><span class="ah-toc-name">Agent 工程师日报</span><span class="ah-toc-count">5条</span></a></li><li><a href="#sec-ai-daily"><span class="ah-toc-name">AI 日报</span><span class="ah-toc-count">2条</span></a></li><li><a href="#sec-ai-deals"><span class="ah-toc-name">AI 羊毛</span><span class="ah-toc-count">2条</span></a></li></ul></nav>

---

**[Harness 架构](#sec-harness-arch)**
1. [Mastra Core 1.86.0 发布](#item-harness-arch-1) ⭐️ 8.8/10
2. [FastMCP v4.2.7a1 发布](#item-harness-arch-2) ⭐️ 5.5/10

**[Agent 工程师日报](#sec-agent-engineer)**
1. [NVIDIA Nemotron 3.5 Parse 更新](#item-agent-engineer-1) ⭐️ 7.8/10
2. [科学家划定 AI 研究助手边界](#item-agent-engineer-2) ⭐️ 7.8/10
3. [CUGA 印地语语音代理案例发布](#item-agent-engineer-3) ⭐️ 6.3/10
4. [VibeVideoAgent 框架：代码生成视频的感知闭环](#item-agent-engineer-4) ⭐️ 6.0/10
5. [SlidesWeaver 多智能体编排方案提出](#item-agent-engineer-5) ⭐️ 6.0/10

**[AI 日报](#sec-ai-daily)**
1. [GitHub 公布应用现代化安全步骤方法](#item-ai-daily-1) ⭐️ 6.8/10
2. [Gemini 4 Neon 登顶长流程榜](#item-ai-daily-2) ⭐️ 5.0/10

**[AI 羊毛](#sec-ai-deals)**
1. [Google AI 会员订阅避坑指南](#item-ai-deals-1) ⭐️ 8.0/10
2. [林易 API 回帖加群送 $18 额度](#item-ai-deals-2) ⭐️ 7.0/10

---

## Harness 架构
{: #sec-harness-arch .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-harness-arch" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-harness-arch-1"></a>
### [Mastra Core 1.86.0 发布](https://github.com/mastra-ai/mastra/releases/tag/%40mastra/core%401.86.0) ⭐️ 8.8/10

Mastra Core 1.86.0 发布，核心新增 durable evented workflows 与原生 durable Agent 执行引擎，支持崩溃安全的任务续跑。引入实验性 Knowledge importer 基础设施，提供批量同步、租约、重放保护与 settle/repair 语义，支持 in-memory、LibSQL 和 Postgres 存储。新增 knowledge\_activity 工具与 host-run principals/author 机制，允许在 agent 运行外安全调用 Knowledge 工具。包含多项 breaking changes，如 \`get\_process\_output\` 的 \`wait: true\` 移除、\`@mastra/connect\` 事件 API 迭代器化、MCP 字段重命名等。

github · PaulieScanlon · 11月25日 10:00

**「设计要点」** 运行时层新增 durable execution engine 作为默认选项，通过事件化工作流实现崩溃恢复，要求 worker 基于 pubsub（如 Redis Streams）运行以重投递未确认事件。Knowledge 存储层统一纳入 importer bookkeeping（bindings、cursor state、runs、flush receipts），并在同一事务中完成页面写入与 importer 状态更新；Postgres 适配器支持事务级 deadline 强制回滚。

**「改了什么」** 实验任务可通过 \`durable: true\` 运行为事件化工作流，worker 崩溃或 redeploy 后可由其他 worker 接续未确认项，避免状态卡在 running。Agent 原生支持 durable 执行引擎，配置项从 \`executionEngine: &\#x27;durable&\#x27;\` 变更为 \`executionEngine: &\#x27;default&\#x27;\`，保留现有流式与模型输出 API。新增实验性 Knowledge importer 端到端契约与运行器，支持外部源同步到 Knowledge，包含 unsettled 标记、listNodes、listLinkingNodes 及 retireBinding 生命周期管理。

**标签**: `#runtime`, `#durable-execution`, `#memory`, `#tools`

---

<a id="item-harness-arch-2"></a>
### [FastMCP v4.2.7a1 发布](https://github.com/PrefectHQ/fastmcp/releases/tag/v4.2.7a1) ⭐️ 5.5/10

FastMCP v4.2.7a1 是 PrefectHQ 发布的 MCP 协议兼容性 alpha 补丁版本，核心调整围绕 skills 代理的发现与寻址逻辑展开。本次更新让 skills 代理自动跳过使用旧版 MCP 协议的后端，同时过滤后端返回的畸形技能条目，避免无效数据污染技能列表。此外新增对技能 URI 前缀中百分号编码斜杠的解析支持，修复对应路径下已发布技能无法被客户端发现的问题，同时清理了代理验证环节的冗余警告输出。

github · github-actions\[bot\] · 11月26日 01:00

**「设计要点」** skills 代理层新增后端协议版本校验与畸形条目过滤逻辑，运行时自动跳过对旧版 MCP 后端的发现请求，避免无效数据流入技能列表；URI 解析层新增百分号编码斜杠的兼容处理，扩展技能路径的寻址范围。

**「改了什么」** 本次更新包含三项修复：skills 代理跳过使用旧版 MCP 协议的后端的发现请求，同时过滤后端返回的畸形技能条目；新增对技能 URI 前缀中百分号编码斜杠的解析支持，修复对应路径下已发布技能无法被客户端发现的问题；清理代理验证环节的冗余警告输出。

**标签**: `#mcp`, `#runtime`, `#tools`

---

## Agent 工程师日报
{: #sec-agent-engineer .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-agent-engineer" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-agent-engineer-1"></a>
### [NVIDIA Nemotron 3.5 Parse 更新](https://huggingface.co/blog/nvidia/building-on-nemotron-35-parse-open-data-fine-tunin) ⭐️ 7.8/10

2026 年 11 月 26 日，Hugging Face 官方博客发布 NVIDIA Nemotron 3.5 Parse 的配套技术资源，包括 3 份开源合成训练数据集、公开微调配方、DFlash2 推理加速方案，以及 SFT+RLVR 两阶段训练方法论。关键细节：开源数据集分别为 Synthetic Charts V1（998 万条）、Synthetic Tables V1（100 万条）、OCR Synthetic Multilingual v2（790 万条），均含图像、标注与生成文档；DFlash2 在单张 H200 BF16 环境下，并发 1 时吞吐量较关闭推测解码的 Parse 3.5 提升 7.62 倍，并发 512 时提升 1.52 倍；SFT+RLVR 训练后，循环输出 flagged 页面从 126 页降至 29 页，达 9000 token 限制的输出从 185 页降至 35 页，整体评分从 66.24 升至 71.38。该资源面向 RAG、agent 工作流的文档解析开发者，可基于开源内容微调适配自身场景。

rss · Hugging Face Blog · 11月26日 05:05

**「为什么重要」** 该更新首次公开了 Nemotron 3.5 Parse 的全套训练资源、微调路径与推理加速实现，降低了文档解析模型的自研门槛；目前尚未有公开证据证明这些资源可直接复用到非文档解析类模型场景。

**「可关注」** 可关注：开源合成数据集和 SFT+RLVR 微调配方可直接用于文档解析模型的领域适配，DFlash2 speculative decoding 方案可复用到其他基于自回归解码的文本生成模型推理加速场景。

**标签**: `#rag`, `#fine-tuning`, `#inference`, `#agent-workflow`, `#document-model`

---

<a id="item-agent-engineer-2"></a>
### [科学家划定 AI 研究助手边界](https://huggingface.co/blog/allenai/where-scientists-draw-the-line-on-ai-agents) ⭐️ 7.8/10

2026 年 11 月 25 日，Hugging Face 博客发布 Ai2 团队研究，基于对 17 名跨领域（自然、应用、社会科学）科学家的访谈，提出科研场景 AI agent 需满足可验证性、隐私、客观性、问责制、透明度五维信任要求，同时明确科研人员需保留研究任务选择、agent 运行规则、评估标准制定的决策权。当前提出的参与式基准等评估方案仍处于待和科研群体共同验证的阶段，尚未落地，影响科研 AI agent 开发者、评估工具工程师及科研 AI 治理相关方。

rss · Hugging Face Blog · 11月25日 18:52

**「为什么重要」** 这是目前少有的基于一线科研人员实际使用需求提出的 AI agent 行为边界，直接对应科研场景对结果可复现、行为可审计、数据合规的核心诉求；其提出的五维信任要求与评估方向，为科研 AI agent 的工程设计与合规评估提供了可参考的框架，具体方案仍需和科研群体共同验证。

**「可关注」** 可关注：科研场景 AI agent 的评估需覆盖授权文件访问范围、矛盾证据遗漏率、方法可复现性等维度，而非仅任务完成率。

**标签**: `#permissions`, `#observability`, `#eval`, `#harness`

---

<a id="item-agent-engineer-3"></a>
### [CUGA 印地语语音代理案例发布](https://huggingface.co/blog/ibm-research/an-indic-voice-agent-with-cuga) ⭐️ 6.3/10

2026 年 11 月 25 日 Hugging Face 博客发布 IBM Research 使用开源 CUGA （ConfigUrable Generalist Agent）agent harness 构建印地语等印度区域语言语音代理的案例，该 harness 为 AppWorld Benchmark 领先方案。案例以农业问答为核心场景，核心设计为 CUGA 仅处理文本输入输出，语音层为薄封装，支持 Sarvam AI 云 API 与开源 SraVaani/Svara 两种语音服务切换；解决了跨语言检索问题，将默认英文嵌入模型替换为 intfloat/multilingual-e5-large 后，单份英文文档即可服务所有目标语言，无需翻译副本；同时内置 OFF\_TOPIC guardrail 实现无额外 LLM 调用的农业话题重定向。该方案不限于农业场景，替换知识库即可适配政务、健康等本土语言服务场景，用户可直接在 Hugging Face Spaces 的 CUGA Apps 中体验该代理，案例未公开具体性能指标与可复现评估数据。

rss · Hugging Face Blog · 11月25日 10:22

**「为什么重要」** 该案例首次公开了用开源 agent harness 构建多语言语音代理的端到端实践，验证了文本核心+薄语音封装的架构可行性，以及多语言嵌入模型解决跨语言检索的轻量化路径，可作为 agent harness 用法的参考。目前未公开具体性能指标与大规模落地数据，其工程价值尚待实际项目验证，并非能直接指导工程优化的必读内容。

**「可关注」** 构建多语言语音 agent 时，优先用非英语语种验证检索层准确性，再调整 prompt；同时将语音服务与 agent 核心解耦，可无侵入切换部署模型。

**标签**: `#harness`, `#eval`, `#permissions`

---

<a id="item-agent-engineer-4"></a>
### [VibeVideoAgent 框架：代码生成视频的感知闭环](https://huggingface.co/papers/2611.34237) ⭐️ 6.0/10

2026-11-26，Hugging Face Daily Papers 分享 arXiv 预印本，提出 VibeVideoAgent。这是一个 training-free 框架，让 coding agent 在代码驱动视频生成过程中检查草稿，捕获非运行时渲染错误（如重叠标签、相机偏离、对象交互 broken、 narration 不同步），这些错误不会触发 runtime error。该机制旨在减少中间输出导致的上下文膨胀，避免昂贵的后期重写。当前材料仅为截断摘要，缺乏完整技术细节、性能基准及代码/工件可用性信息，核心用例相对小众，对通用 AI agent 工程的直接价值有限。

rss · Hugging Face Daily Papers · 11月26日 00:00

**「为什么重要」** 该框架针对 coding agent 中一个普遍痛点：非运行时错误检测与中间输出上下文管理。但完整论文未公开，实际效果与可用性尚未证实。

**「可关注」** 可关注：代码生成类任务中，非运行时错误（如渲染逻辑、时序同步）的中间检查机制，可能减少后期重写成本。

**标签**: `#coding-agent`, `#orchestration`, `#observability`

---

<a id="item-agent-engineer-5"></a>
### [SlidesWeaver 多智能体编排方案提出](https://huggingface.co/papers/2611.28010) ⭐️ 6.0/10

Hugging Face Daily Papers 于 2026-11-26 收录论文 SlidesWeaver。该系统为混合多智能体架构，通过共享 deck 级与 slide 级状态协调语言与视觉智能体，采用分阶段多模态承诺、扩散模型构图规划及两种生成调度生成可编辑演示文稿，主要面向对多智能体编排感兴趣的工程师。摘要内容截断，技术细节不完整。

rss · Hugging Face Daily Papers · 11月26日 00:00

**「为什么重要」** 该工作提供了多智能体编排在结构化多模态生成任务中的具体设计参考，尤其适合关注 agent 协作的工程师快速浏览。但应用场景较窄，且摘要信息截断，实际效果需阅读全文验证。

**「可关注」** 可关注：共享状态与分阶段多模态承诺机制在多智能体协作中的设计，以及扩散模型用于构图规划的具体实现。

**标签**: `#orchestration`

---

## AI 日报
{: #sec-ai-daily .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-daily" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-daily-1"></a>
### [GitHub 公布应用现代化安全步骤方法](https://github.blog/ai-and-ml/github-copilot/how-to-choose-the-next-safe-step-in-application-modernization/) ⭐️ 6.8/10

GitHub 发布官方博客，提出证据优先的应用现代化步骤选择方法，同时演示了将该流程编码为 GitHub Copilot agent skill 的实现方式。作者在 4 个公开应用（从小型 Node.js 游戏到大型 Java ERP 系统）上验证了该方法的可复现性，给出从保留到重写的 5 级处理优先级，以及 L0 到 L4 的 4 级回归保护等级。该内容属于实践指导类文章，并非重大模型发布或行业政策变动，影响范围有限。

rss · GitHub Blog · 11月25日 15:00

**「为什么重要」** 该方法提供了可复现的落地路径，既降低了应用现代化过程中盲目变更的风险，也展示了将工程流程编码为 AI 代理能力的实践方式。

**「可关注」** 可关注：优先构建包含运行时 pin、外部契约、废弃依赖的证据清单，按保留到重写的优先级选择最小侵入的处理方案，同时明确当前可达到的回归保护等级。

**标签**: `#product`, `#lab`

---

<a id="item-ai-daily-2"></a>
### [Gemini 4 Neon 登顶长流程榜](https://mp.weixin.qq.com/s?__biz=MzI3MTA0MTk1MA==&amp;mid=2652745183&amp;idx=2&amp;sn=9e2398515e5d4f23adafd26dd399519e) ⭐️ 5.0/10

11 月 25 日新智元发布二手报道，称博主@AI\_Screening 晒出 LiveBench 2.0（10 月重构的长流程评测，含 7 个子项 471 道题）截图，Gemini 4 Neon 以 87.4 分登顶总榜，领先并列 84.9 分的 Claude Fable 5.2、GPT-6.2 Astra 2.5 分；但该排名无官方来源核实。此外 Neon 在 Artificial Analysis 智力指数 v5.0.1 中总榜排第三，仅在其 Coding Agent Index 以 58.6 分排名第一，单任务成本为 2.654 美元，高于 Astra 的 1.941 美元，仅为 Fable 5.2 的约 27%。

rss · 新智元 · 11月25日 09:40

**「为什么重要」** LiveBench 2.0 是面向长流程场景的重构评测，Neon 的领先表现与其官方定位的长流程、重工具调用智能体工作流匹配，相关得分和成本数据可作为 Coding Agent 场景选型的参考依据。

**「可关注」** 可关注：Gemini 4 Neon 在浏览器操作、研究、编程、推理等长流程子项得分突出，Coding Agent Index 排名第一，适合多轮工具调用的智能体场景，但单任务成本仍高于 GPT-6.2 Astra，需结合实际需求权衡。

**标签**: `#model`, `#eval`, `#industry`

---

## AI 羊毛
{: #sec-ai-deals .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-deals" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-deals-1"></a>
### [Google AI 会员订阅避坑指南](https://www.v2ex.com/t/1259690#reply20) ⭐️ 8.0/10

V2EX 用户 FringJX 分享 Google AI 会员订阅的实操避坑经验，涵盖地区归属设置、支付方式限制、年费五折优惠获取三个核心要点。账号关联地区不能为中国或香港，否则反重力功能不可用；Play 商店地区需切换为日本、美国或新加坡，且需添加支付方式，香港支付方式无法使用反重力高级模型。支付卡需为单币 Visa 或万事达，招行双币卡会被识别为银联不支持。年费五折优惠需先开通低价 Plus 订阅再覆盖升级，Plus 退款会扣手续费，首月订阅成本越低损失越小。

rss · V2EX Hot · 11月25日 05:38

**「为什么重要」** 这些经验覆盖了订阅过程中最常见的地区限制、支付卡不兼容、优惠获取三个痛点，可帮助用户避免订阅失败或额外损失。

**「可关注」** 可关注：订阅前需分别完成账号关联地区与 Play 商店地区的设置，且必须使用单币 Visa 或万事达卡，招行双币卡无法完成支付。

**标签**: `#promo`, `#coupon`, `#api`

---

<a id="item-ai-deals-2"></a>
### [林易 API 回帖加群送 $18 额度](https://www.v2ex.com/t/1259773#reply53) ⭐️ 7.0/10

林易 API（第三方 AI 大模型 API 中转平台，非模型厂商官方渠道）推出推广活动，回帖可领 $8 额度、加群可再领 $10 额度，合计最高 $18。平台支持 Claude、GPT、Gemini 等多家模型，兼容 OpenAI、Anthropic 接口，Claude Code、Codex CLI 等客户端改 Base URL 和 Key 即可使用。领取条件为先在 linyiapi.ai 注册账号，回帖发送注册邮箱前缀（或注册后修改用户名），加指定 QQ 群发送「注册账号 + 领额度」即可，每份福利每个 V2EX 账号、每个林易账号各限领 1 次。额度无有效期，仅可用于按量付费，不可购买套餐、不可退款，活动在帖子持续有效期间均可参与。

rss · V2EX Hot · 11月25日 09:12

**「为什么重要」** 额度无有效期，叠加平台按量最低至 GPT 官方价 1.35 折、Claude 官方价 1.8 折的优惠，且仅需修改配置即可接入常用 AI coding 客户端，适合需要低成本试用多家大模型 API 的开发者。

**「可关注」** 可关注：每份额度每个 V2EX 账号、每个林易账号仅可领取 1 次，批量注册小号领额度的额度会被扣除；赠送额度仅可用于按量付费，不可购买套餐或退款；创建 API Key 时选择的分组直接决定可用模型范围与计费倍率。

**标签**: `#promo`, `#credits`, `#api`, `#limited-free`

---