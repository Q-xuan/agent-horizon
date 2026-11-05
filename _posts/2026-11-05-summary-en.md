---
layout: default
title: "Horizon Summary: 2026-11-05 (EN)"
date: 2026-11-05
lang: en
---

> From 219 items, 17 important content pieces were selected

---

**Agent Harness Architecture**
1. [Mastra Core 1.82.0 发布](#item-harness-arch-1) ⭐️ 8.8/10
2. [pydantic-ai v2.66.0 发布](#item-harness-arch-2) ⭐️ 6.8/10
3. [Gemini CLI v0.67.0 发布](#item-harness-arch-3) ⭐️ 6.8/10

**AI Agent Engineer**
1. [Cognition 推出 SWE-2 Flash](#item-agent-engineer-1) ⭐️ 8.8/10
2. [Anthropic ZK 可证明推理进展](#item-agent-engineer-2) ⭐️ 8.0/10
3. [Kimi K3.1 Pro 开源权重发布](#item-agent-engineer-3) ⭐️ 7.0/10
4. [OpenAI 修复 948 个 Linux 内核提权漏洞](#item-agent-engineer-4) ⭐️ 7.0/10
5. [LoCo 本地偏好学习压缩推理链](#item-agent-engineer-5) ⭐️ 7.0/10
6. [Dharma Field Extractor 2B 发布](#item-agent-engineer-6) ⭐️ 6.8/10
7. [OpenAI Images 2.6 发布](#item-agent-engineer-7) ⭐️ 6.0/10
8. [Route Anything 框架论文发布](#item-agent-engineer-8) ⭐️ 6.0/10

**AI Daily**
1. [OpenAI 收购 Pierre](#item-ai-daily-1) ⭐️ 7.8/10
2. [Daybreak Red 上线 AWS GovCloud](#item-ai-daily-2) ⭐️ 7.8/10
3. [OpenAI 自主流水线修复 948 个内核漏洞](#item-ai-daily-3) ⭐️ 7.8/10
4. [Lion-ER-35B-A3B 具身模型发布](#item-ai-daily-4) ⭐️ 5.5/10
5. [Seq-Drifting 实现扩散语言模型单步生成](#item-ai-daily-5) ⭐️ 5.5/10

**AI Deals**
1. [Samewindow 免费备份 AI 对话](#item-ai-deals-1) ⭐️ 7.0/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [Mastra Core 1.82.0 发布](https://github.com/mastra-ai/mastra/releases/tag/%40mastra/core%401.82.0) ⭐️ 8.8/10

Mastra Core 1.82.0 发布，Knowledge 子系统重构为 v2 page-tree 模型（pages/notes/pins）。新增服务器端同步 API（knowledge.upsertPage/removePage）、向量/混合搜索与分块嵌入，配套只读 HTTP/JS 客户端 API 及 SSE 变更流。Evented durable agents 获得跨 API 重启连续性，需配合 fencing 共享存储（如 @mastra/pg 的 PostgresStore）。后台任务支持可恢复的 &quot;input required&quot; 流程，MCP 工具结果扩展支持图片/音频/文件。

github · PaulieScanlon · Nov 4, 10:59

**「设计要点」** Knowledge v2 采用 page-tree 架构分离服务器端写入与客户端只读访问，SSE 流推送变更。Durable agent 连续性依赖 fencing 共享存储与共享 pubsub，worker 进程独立于 API 进程。权限控制通过 Agent scopes 函数动态 narrowing，FGA-aware 范围门控保护只读 Knowledge 路由。

**「改了什么」** Knowledge 从内存结构升级为 page-tree 模型，新增 knowledge\_list、knowledge\_read（行/节/grep 读取）、列表固定（kind: &\#x27;list&\#x27;）与链接索引。Evented durable agents 在 API 关闭后 worker 继续运行完成清理，需 fencing 存储实现跨进程连续性。工作流新增 getStepResultAsync 替代 getStepResult，为按需加载 step 结果做准备。@mastra/temporal 0.5.0 开始验证 inputSchema 与 requestContextSchema。

**Tags**: `#memory`, `#tools`, `#api`, `#permissions`, `#runtime`

---

<a id="item-harness-arch-2"></a>
### [pydantic-ai v2.66.0 发布](https://github.com/pydantic/pydantic-ai/releases/tag/v2.66.0) ⭐️ 6.8/10

pydantic-ai v2.66.0 正式发布，集中修复 2 个高危与 6 个中危安全漏洞。\`web\_fetch\_tool\` 本地回退在事件循环中重新缩进 JSON 后再应用返回内容限制，深度嵌套文档可膨胀数百倍，导致内存耗尽或事件循环延迟。\`private\_key\` 密钥脱敏正则存在指数级回溯，数百字符即可阻塞事件循环数分钟，该修复位于 \`pydantic-ai-harness\` 0.66.0。中危修复包括腾讯云元数据地址漏blocklist、OpenTelemetry 嵌入向量跨度泄露凭据、工具 schema 内联爆炸、DecisionModel \`$ref\` 重复解析、Vercel AI/AG-UI 适配器消息加载 O\(n²\)、反序列化工具结果文件类型混淆、MCP URL 路径凭据泄露、DNS 白名单先解析后检查。同步新增 OpenSandbox、Azure Durable Task、Pixeltable 工具与记忆存储、RenderSandbox 等功能。

github · adtyavrdhn · Nov 4, 11:51

**「设计要点」** 所有高危与中危修复均指向事件循环阻塞或内存耗尽：\`web\_fetch\_tool\` 在事件循环中重新缩进 JSON 后才截断；密钥脱敏正则直接运行于事件循环；AG-UI 适配器在事件循环中处理客户端提交的 schema 与消息。 Harness 对不可信输入缺乏前置大小校验与复杂度保护。

**「改了什么」** \`web\_fetch\_tool\` 修复本地回退在事件循环中重缩进 JSON 的漏洞，改为先截断或避免重缩进。\`private\_key\` 脱敏正则指数回溯已在 \`pydantic-ai-harness\` 0.66.0 修复。腾讯云元数据地址 \`169.254.0.23\` 加入 cloud-metadata blocklist。OpenTelemetry 嵌入向量跨度不再记录 \`extra\_headers\` 与 \`extra\_body\`。工具 schema 内联与 DecisionModel \`$ref\` 解析增加防膨胀保护。Vercel AI/AG-UI 适配器消息加载从 O\(n²\) 改为线性。消息历史反序列化增加文件类型形状校验。MCP 能力标识符不再从 URL 路径派生。\`allowed\_domains\` 与 PlaywrightBrowser 在 DNS 解析前检查域名列表。

**Tags**: `#tools`, `#runtime`, `#permissions`

---

<a id="item-harness-arch-3"></a>
### [Gemini CLI v0.67.0 发布](https://github.com/google-gemini/gemini-cli/releases/tag/v0.67.0) ⭐️ 6.8/10

Google Gemini CLI v0.67.0 adds container sandbox support for the IDE companion via exec stdio bridging. The release fixes duplicate agent loading when the workspace is the home directory, excludes IDE settings and GEMINI.md from open file context, and scopes untrusted flag checks to external output with approval memory. Additional fixes cover A2A server route registration, RFC 9110 token rules for custom headers, atomic writeTextFile respecting read-only files and hard links, and introduces a \`models\` command with \`--list-models\` flag for model discovery. No major architectural overhauls or breaking changes appear in the truncated changelog.

github · gemini-cli-robot · Nov 4, 20:27

**「设计要点」** Container sandbox integration runs the IDE companion over exec stdio, avoiding a new transport layer. Untrusted flag checks now scope to external output and persist approval state, reducing permission prompts without altering the core permission model.

**「改了什么」** IDE companion bridges into container sandboxes via exec stdio. Core fixes prevent duplicate agent loading in home-directory workspaces, filter context to exclude IDE settings and GEMINI.md, scope untrusted flag checks with approval memory, and add \`models\` command and \`--list-models\` flag.

**Tags**: `#sandbox`, `#runtime`, `#permissions`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [Cognition 推出 SWE-2 Flash](https://cognition.ai/blog/swe-2-flash) ⭐️ 8.8/10

Cognition 于 2026-11-04 发布 SWE-2 Flash 编码模型。模型基于 Inkling-Small，总参数 276B，激活参数 12B。训练流程新增预强化学习阶段的 mid-training。Terminal-Bench 4.0 从 0.9% 升至 20.0%。FrontierCode 2.0 从 3.2% 升至 24.0%。ExploitBench 从 11.3% 升至 34.8%。在主流评估中，SWE-2 Flash 超越所有美国开源权重模型。该模型甚至超过规模大三倍的模型。模型已在 Devin Desktop 和 CLI 上线。价格为 SWE-2 的五分之一，速度三倍。权重暂不公开，计划向行业伙伴与研究机构安全共享。免费试用至 2026-11-30。

rss · Cognition Blog · Nov 4, 18:00

**「为什么重要」** SWE-2 Flash 展示新增 mid-training 阶段对编码基准的显著提升。该模型已可直接在 Devin 平台使用。这为构建编码智能体提供新选项。权重共享计划尚未落地，实际安全性与可复现性待验证。

**「可关注」** SWE-2 Flash 采用预 RL mid-training，编码基准提升显著。已可在 Devin 平台试用，权重暂不公开。

**Tags**: `#coding-agent`, `#eval`

---

<a id="item-agent-engineer-2"></a>
### [Anthropic ZK 可证明推理进展](https://www.anthropic.com/research/provable-inference) ⭐️ 8.0/10

Anthropic 于 2026-11-04 发布官方研究，展示零知识可证明 LLM 推理的进展。实测指标包括：承诺大小约 6.5 MB，24 线程下验证耗时 17 秒，计算开销约 90–100 倍。该成果相比此前 ZK 方案有显著改进，面向需要验证模型执行的可靠 LLM 代理系统工程师。当前细节仅来自分析摘要，原文内容未直接提供。

hackernews · ltononro · Nov 4, 17:17 · [Discussion](https://news.ycombinator.com/item?id=50368626)

**「为什么重要」** 该研究首次给出可证明推理的实测性能边界，让工程师能评估在 agent harness 中引入验证层的实际成本。但 90–100 倍开销与 17 秒验证时延表明，当前方案更适合对可验证性要求极高且能承受计算成本的场景，尚未成为通用基础设施。

**「可关注」** 可关注：闭源模型提供者的零知识可证明推理需承受 90–100 倍计算开销，而开源模型可通过确定性重跑以更低成本实现类似验证，工程选型时需优先权衡模型开放性与验证需求。

**「评论」** 社区对工作归属存在争议，有评论指其基于 VerInf 但署名不足；技术讨论聚焦闭源模型可证明推理的 90–100 倍开销与 17 秒验证时延，相比开源模型确定性重跑方案成本更高。

**Tags**: `#observability`, `#eval`, `#harness`

---

<a id="item-agent-engineer-3"></a>
### [Kimi K3.1 Pro 开源权重发布](https://huggingface.co/moonshotai/Kimi-K3.1-Pro) ⭐️ 7.0/10

2026年11月4日Moonshot AI在HuggingFace平台正式发布Kimi K3.1 Pro大模型开源权重，该模型为多模态（图像-文本-文本）类型，支持文本生成、对话任务。社区反馈显示第三方推理服务商已开始托管该模型，同时围绕其本地部署算力需求、与DeepSeek V4.1-Flash等竞品的基准表现、以及agent工作负载的实际适用性展开讨论，部分观点认为其存在基准刷分倾向，也有实测者反馈其通用表现优秀，适配多数使用场景。

hackernews · Hugging Face Trending Models · Nov 4, 15:30 · [Discussion](https://news.ycombinator.com/item?id=50366999)

**「为什么重要」** 这是Moonshot AI首次公开Kimi K3.1 Pro的模型权重，为AI agent团队、eval套件开发者新增了可选基座模型；同时社区已出现不同推理服务商的性能与成本差异，可帮助团队评估部署与调优方向。

**「可关注」** 可关注第三方推理服务商对Kimi K3.1 Pro的吞吐优化空间，以及该模型在coding agent、eval场景下的实际任务表现与算力消耗比。

**「评论」** 社区对该模型评价存在分歧：部分用户认为其基准表现未明显超过DeepSeek V4.1-Flash，存在&quot;benchmaxxed&quot;倾向；也有实测者反馈其通用表现优秀，适配多数场景；另有用户指出本地部署该模型需要约8xB300节点级别的算力门槛。

**Tags**: `#coding-agent`, `#eval`, `#harness`

---

<a id="item-agent-engineer-4"></a>
### [OpenAI 修复 948 个 Linux 内核提权漏洞](https://openai.com/index/a-thousand-fewer-paths-to-root/) ⭐️ 7.0/10

OpenAI 安全团队 2026-11-04 宣布发现并协调修复 948 个 Linux 内核权限提升漏洞。这些漏洞加固 AI agent 与 harness 依赖的底层基础设施权限边界。具体漏洞编号、受影响版本及修复方式未在材料中披露。

hackernews · dangelosaurus · Nov 4, 23:33 · [Discussion](https://news.ycombinator.com/item?id=50372929)

**「为什么重要」** 底层内核权限边界收紧，直接缩小 agent 运行环境的提权攻击面。社区讨论转向 AI 驱动漏洞发现的规模与成本，但尚未形成定论。

**「可关注」** 可关注：AI 辅助漏洞挖掘已产出可观的 Linux 内核提权漏洞批量修复，但社区对这是否代表安全研究范式转移或仅是资金与意愿问题仍有分歧。

**「评论」** 社区对 948 个漏洞的数量感到震惊，讨论 Linux 内核安全模型复杂性、现实世界缓解因素及 AI 漏洞发现的成本效益。原帖作者确认团队工作并开放答疑，同时发布招聘信息。

**Tags**: `#permissions`, `#harness`, `#eval`

---

<a id="item-agent-engineer-5"></a>
### [LoCo 本地偏好学习压缩推理链](https://huggingface.co/papers/2611.04814) ⭐️ 7.0/10

2026-11-05，Hugging Face Daily Papers 推荐了 LoCo（Local Preference Learning for Reasoning Compression）论文。LoCo 从模型自身推理轨迹中检测过思考状态，冻结对应推理前缀，从同一状态重新生成更短且经过验证的续写，并用 DPO 训练状态条件偏好对，以教会模型判断何时应停止推理。该方法针对推理模型过长的思维链导致的高推理成本问题，对 coding agent 效率优化有潜在价值。当前来源内容截断，缺少完整性能验证数据与对比基线。

rss · Hugging Face Daily Papers · Nov 5, 04:00

**「为什么重要」** 推理模型的长思维链带来显著推理开销，LoCo 提供了一种状态级别而非轨迹级别的推理压缩新思路，可能降低 coding agent 的推理成本。但完整效果与泛化能力尚需论文全文验证。

**「可关注」** 可关注：LoCo 通过冻结前缀、对检测到的过思考状态生成短续写并用 DPO 训练状态条件偏好对，提供了一种降低推理链长度的工程路径，但需验证其压缩率与准确率在不同任务上的权衡。

**Tags**: `#coding-agent`

---

<a id="item-agent-engineer-6"></a>
### [Dharma Field Extractor 2B 发布](https://huggingface.co/blog/Dharma-AI/dharma-field-extractor) ⭐️ 6.8/10

2026年11月4日Hugging Face官方博客发布Dharma Field Extractor，一款20亿参数的文档字段提取模型，输入任意文档可输出符合要求的结构化JSON字段，支持开放提取、schema定向两种请求模式。该模型基于DharmaOCR-LITE v1.1 checkpoint训练LoRA适配器，训练数据覆盖英、巴西葡语等多语言多领域文档，包含发票、表单、身份证件等类型。官方benchmark覆盖546份文档共1638个用例，字段级F1得分0.834，高于测试的Claude Opus 5（0.816）、GPT-5.6 Luna（0.741）等四个前沿LLM配置；单L40S GPU自托管成本比 frontier API 低6至147倍，对比基于单L40S每小时2.24美元的GPU定价，实际成本随硬件、吞吐量、延迟需求变化。该模型面向高吞吐量文档结构化处理场景，如发票录入、医疗调度、合规合同字段提取。

rss · Hugging Face Blog · Nov 4, 17:50

**「为什么重要」** 该发布验证了小参数领域专用模型在文档结构化任务上可实现质量、成本双优于前沿API的路径，为高吞吐量文档处理场景提供了可自托管的替代选项；目前尚无第三方公开复现结果，长尾文档类型的适配效果也未得到验证。

**「可关注」** 可关注：该模型基于 DharmaOCR-LITE v1.1 加LoRA适配器的训练方案，在文档字段提取任务上实现了比测试的四个前沿LLM配置更高的字段级F1，同时自托管成本仅为 frontier API 的1/6到1/147，可参考其任务拆解思路评估自有文档处理管线的模型选型。

**Tags**: `#toolchain`, `#eval`

---

<a id="item-agent-engineer-7"></a>
### [OpenAI Images 2.6 发布](https://openai.com/index/introducing-images-2-6/) ⭐️ 6.0/10

OpenAI 2026年11月4日正式发布Images 2.6图像生成模型，新增网格提示生成一致动画帧、原生SVG输出两项官方能力。社区对生成质量反馈不一，有用户指出近期生成效果退化、帧间一致性仍存问题。该更新仅对将图像生成集成到Agent工具链、或评估含图像生成能力Agent的工程师有直接影响。

hackernews · davidbarker · Nov 4, 23:35 · [Discussion](https://news.ycombinator.com/item?id=50372945)

**「为什么重要」** 已发生的变化是OpenAI首次将动画帧网格提示、原生SVG输出作为官方能力明确提供；尚未证实的是这些能力能否解决社区反馈的生成质量、帧间一致性差的问题，对更广泛受众的参考价值有限。

**「可关注」** 可关注：集成图像生成能力的Agent工具链需先验证Images 2.6的帧间一致性、SVG输出合规性及生成质量稳定性，再评估是否接入。

**「评论」** 社区对图像生成质量普遍持负面态度，认为该领域近年进步有限甚至出现退化，对新增的动画帧、SVG功能也持怀疑态度，有用户反馈近期生成效果明显下降。

**Tags**: `#eval`, `#toolchain`, `#image-generation`

---

<a id="item-agent-engineer-8"></a>
### [Route Anything 框架论文发布](https://huggingface.co/papers/2611.05275) ⭐️ 6.0/10

2026年11月5日Hugging Face Daily Papers分享通用AI系统路由框架Route Anything相关论文，该框架聚焦动态选择模型、工具与策略候选以平衡性能与计算成本，当前公开内容截断，未包含完整技术细节、评测结果与可复现实现，需查阅原文评估落地价值。

rss · Hugging Face Daily Papers · Nov 5, 04:00

**「为什么重要」** 该研究方向直接关联Agent编排与任务路由的核心需求，若框架完整落地，有望为异构模型、工具协同的AI系统提供动态调度基础，但当前缺乏完整技术细节与性能数据，实际价值尚未证实。

**「可关注」** 可关注：该框架的理论基础与路由策略设计，若公开完整实现与评测数据，可评估其对现有Agent编排系统调度逻辑的优化空间。

**Tags**: `#orchestration`, `#eval`

---

## AI Daily

<a id="item-ai-daily-1"></a>
### [OpenAI 收购 Pierre](https://openai.com/index/openai-to-acquire-pierre) ⭐️ 7.8/10

OpenAI 宣布计划收购 Pierre Computer Company, Inc.。此次收购旨在扩展 Codex 的代码构建、理解与审查工具。目前公告未披露交易金额、具体时间表及后续整合计划。

rss · OpenAI Blog · Nov 4, 14:30

**「为什么重要」** Codex 是 OpenAI 面向开发者的核心代码工具，此次收购直接指向其代码理解与审查能力的增强。

**「可关注」** 可关注：Codex 后续代码理解与审查功能的整合进展。

**Tags**: `#lab`, `#industry`, `#product`

---

<a id="item-ai-daily-2"></a>
### [Daybreak Red 上线 AWS GovCloud](https://openai.com/index/daybreak-red-aws-govcloud) ⭐️ 7.8/10

Daybreak Red（GPT-5.6 Cyber）模型现已在 AWS GovCloud（US-East）的 Amazon Bedrock 平台上线。该服务仅对批准客户开放，且限定用于授权网络安全工作。OpenAI 官方博客发布了这一产品可用性更新。

rss · OpenAI Blog · Nov 4, 07:00

**「可关注」** 可关注：AWS GovCloud 上的 Amazon Bedrock 新增 Daybreak Red 模型访问渠道，需注意其批准客户与授权用途限制。

**Tags**: `#model`, `#lab`, `#product`

---

<a id="item-ai-daily-3"></a>
### [OpenAI 自主流水线修复 948 个内核漏洞](https://openai.com/index/a-thousand-fewer-paths-to-root) ⭐️ 7.8/10

OpenAI 官方宣布其研发的自主流水线已完成 948 个 Linux 内核本地权限提升漏洞的发现、验证与补丁生成。该成果属于 AI 在网络安全领域的实质性应用进展，无公开的后续落地限制说明。

rss · OpenAI Blog · Nov 4, 08:00

**「为什么重要」** 这是 AI 自动化在网络安全领域落地的实质性进展，为大规模内核漏洞的快速响应提供了可复用的技术路径。

**「可关注」** 可关注：自主流水线在 Linux 内核漏洞全链路处理（发现、验证、补丁生成）的落地实践与效果。

**Tags**: `#lab`, `#industry`

---

<a id="item-ai-daily-4"></a>
### [Lion-ER-35B-A3B 具身模型发布](https://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw==&amp;mid=2247939340&amp;idx=2&amp;sn=25a664251ec6cb5820f1268911de9141) ⭐️ 5.5/10

量子位报道称招商局先进技术研究院下属狮子山人工智能实验室发布具身推理视觉语言模型「驭物™ Lion-ER-35B-A3B」。该模型采用MoE混合专家架构，总参数约35B，每Token仅激活约3B参数。报道称其在十项主流具身相关基准上实现全部指标上涨，技术路线区别于大规模堆砌训练数据的传统做法，通过能力牵引的具身数据引擎，围绕模型所需能力正向设计数据，经评测发现短板后闭环迭代优化。

rss · 量子位 · Nov 4, 05:33

**「为什么重要」** 该模型提出的能力牵引数据闭环迭代思路，为低参数开销下提升机器人三维空间理解、状态捕捉等具身推理能力提供了不同于堆砌数据的可行路径，有助于解决视角变化混淆物体身份、误判相机运动等机器人执行难题。

**「可关注」** 可关注：该MoE架构模型以约3B的激活参数实现十项具身基准全提升，其围绕能力正向设计数据、评测闭环迭代的思路可参考。

**Tags**: `#model`, `#lab`, `#industry`

---

<a id="item-ai-daily-5"></a>
### [Seq-Drifting 实现扩散语言模型单步生成](https://mp.weixin.qq.com/s?__biz=MzIwMTc4ODE0Mw==&amp;mid=2247723829&amp;idx=2&amp;sn=50729365492d766992fa8bf441dac962) ⭐️ 5.5/10

香港城市大学、深圳大学、中国科学技术大学、牛津大学联合团队提出Seq-Drifting方法，将扩散语言模型的多轮去噪生成过程压缩为单步完成，核心是引入依赖当前生成上下文的漂移场，训练时根据已生成内容为每个位置构造候选词元作为优化目标，协调不同位置的词元选择。在无条件128-token生成任务中，该方法生成困惑度（Gen-PPL）达36.01，相较四步蒸馏基线FMLM实现11.2倍实际运行时间加速。目前该方法已在条件续写、机器翻译、摘要生成及推理任务完成验证，论文、代码与模型权重已公开。以上信息来自科技媒体PaperWeekly的报道，暂未找到可公开核对的一手官方来源。

rss · PaperWeekly · Nov 4, 04:05

**「为什么重要」** 扩散语言模型长期受多轮去噪导致的生成效率低问题限制，Seq-Drifting提出的一步生成框架若验证成立，有望突破该瓶颈，为文本生成场景提供新的效率优化路径。

**「可关注」** 可关注：Seq-Drifting的论文、代码与模型权重已公开，可复现其一步生成框架在条件续写、机器翻译等任务的表现。

**Tags**: `#model`, `#research`, `#paper`

---

## AI Deals

<a id="item-ai-deals-1"></a>
### [Samewindow 免费备份 AI 对话](https://www.samewindow.com/) ⭐️ 7.0/10

HN用户gsngsn分享免费的Samewindow Chrome扩展，分别适配ChatGPT、Claude平台，支持备份对应AI对话、创建文件夹，可直接通过Chrome商店安装，无显性付费限制。

rss · HN Free API / Credits · Nov 4, 13:04

**「为什么重要」** 当前无额外使用成本，用户可立即安装使用，满足AI对话数据备份与整理的实用需求。

**「可关注」** 可关注：该扩展目前仅支持Chrome浏览器，需通过Chrome商店对应链接安装，未提及其他浏览器适配计划。

**Tags**: `#free-tier`, `#chrome-extension`, `#ai-tool`, `#promo`

---