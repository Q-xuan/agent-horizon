---
layout: default
title: "Horizon Summary: 2026-11-05 (ZH)"
date: 2026-11-05
lang: zh
---

> 从 219 条内容中筛选出 17 条重要资讯。

<nav id="ah-toc" class="ah-toc" aria-label="目录"><span class="ah-toc-title">目录</span><ul><li><a href="#sec-harness-arch"><span class="ah-toc-name">Harness 架构</span><span class="ah-toc-count">3条</span></a></li><li><a href="#sec-agent-engineer"><span class="ah-toc-name">Agent 工程师日报</span><span class="ah-toc-count">8条</span></a></li><li><a href="#sec-ai-daily"><span class="ah-toc-name">AI 日报</span><span class="ah-toc-count">5条</span></a></li><li><a href="#sec-ai-deals"><span class="ah-toc-name">AI 羊毛</span><span class="ah-toc-count">1条</span></a></li></ul></nav>

---

**[Harness 架构](#sec-harness-arch)**
1. [Mastra Core 1.82.0 发布](#item-harness-arch-1) ⭐️ 8.8/10
2. [pydantic-ai v2.66.0 发布](#item-harness-arch-2) ⭐️ 6.8/10
3. [gemini-cli v0.67.0 发布](#item-harness-arch-3) ⭐️ 6.8/10

**[Agent 工程师日报](#sec-agent-engineer)**
1. [Cognition 发布 SWE-2 Flash 模型](#item-agent-engineer-1) ⭐️ 8.8/10
2. [Anthropic 发布可证明 LLM 推理进展](#item-agent-engineer-2) ⭐️ 8.0/10
3. [Kimi K3.1 Pro 权重开源](#item-agent-engineer-3) ⭐️ 7.0/10
4. [OpenAI 协调修复 948 个 Linux 内核提权漏洞](#item-agent-engineer-4) ⭐️ 7.0/10
5. [LoCo 推理压缩方法提出](#item-agent-engineer-5) ⭐️ 7.0/10
6. [Dharma Field Extractor 2B 模型发布](#item-agent-engineer-6) ⭐️ 6.8/10
7. [OpenAI Images 2.6 发布](#item-agent-engineer-7) ⭐️ 6.0/10
8. [Route Anything 论文：通用 AI 路由框架](#item-agent-engineer-8) ⭐️ 6.0/10

**[AI 日报](#sec-ai-daily)**
1. [OpenAI 拟收购 Pierre Computer Company](#item-ai-daily-1) ⭐️ 7.8/10
2. [Daybreak Red 上线 AWS GovCloud 美东区](#item-ai-daily-2) ⭐️ 7.8/10
3. [OpenAI 自主流水线修复 948 个提权漏洞](#item-ai-daily-3) ⭐️ 7.8/10
4. [Lion-ER-35B-A3B 具身推理模型发布](#item-ai-daily-4) ⭐️ 5.5/10
5. [Seq-Drifting 实现扩散语言模型一步生成](#item-ai-daily-5) ⭐️ 5.5/10

**[AI 羊毛](#sec-ai-deals)**
1. [Samewindow 免费备份 ChatGPT Claude 对话](#item-ai-deals-1) ⭐️ 7.0/10

---

## Harness 架构
{: #sec-harness-arch .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-harness-arch" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-harness-arch-1"></a>
### [Mastra Core 1.82.0 发布](https://github.com/mastra-ai/mastra/releases/tag/%40mastra/core%401.82.0) ⭐️ 8.8/10

Mastra Core 1.82.0 发布，Knowledge 子系统升级至 v2，采用 page-tree 数据模型（pages/notes/pins），新增 \`knowledge\_list\`、\`knowledge\_read\`（支持行/节/grep 式读取）、列表固定及链接索引工具，服务端同步 API \`knowledge.upsertPage\(\)\`/\`removePage\(\)\` 支持外部内容同步与向量/混合搜索。配套只读 Knowledge HTTP/JS 客户端 API 与 SSE 变更流，采用 FGA 感知范围门控。持久化 evented agent 跨 API 重启连续性需 fencing 能力共享存储（如 \`@mastra/pg\` 的 \`PostgresStore\`）。后台任务与 MCP 新增可恢复的 &quot;input required&quot; 流程。

github · PaulieScanlon · 11月4日 10:59

**「设计要点」** Knowledge v2 采用 page-tree 架构分离页面、笔记与固定项，服务端同步与只读客户端 API 分层解耦。持久化 agent 连续性依赖 fencing 共享存储与共享 pubsub，运行时空闲线程回收与运行所有权隔离防止跨 run 干扰，范围门控与 FGA 集成在服务端路由层实现。

**「改了什么」** Knowledge 从平面结构重构为 page-tree，工具链升级支持精细读取与链接索引，服务端 upsert/remove API 替代原有 reindex。持久化 evented agent 修复 API 关闭时 worker 停止问题，但跨进程连续性需显式配置 fencing 存储。后台任务与 MCP 支持重载后恢复的挂起流程，Temporal 步骤增加输入验证，实验性 subconscious 与 knowledge 内存选项移除。

**标签**: `#memory`, `#tools`, `#api`, `#permissions`, `#runtime`

---

<a id="item-harness-arch-2"></a>
### [pydantic-ai v2.66.0 发布](https://github.com/pydantic/pydantic-ai/releases/tag/v2.66.0) ⭐️ 6.8/10

pydantic-ai v2.66.0 发布，集中修复 harness 层 9 个安全漏洞。web\_fetch\_tool 本地回退在事件循环重排 JSON 后超限返回，深度嵌套文档可膨胀数百倍引发内存耗尽；private\_key 脱敏正则遭 crafted text 触发指数回退，数百字符可卡死事件循环数分钟。中危漏洞覆盖腾讯云元数据地址未入阻止列表、OpenTelemetry 追踪泄露 extra\_headers/extra\_body 凭证、AG-UI 工具 schema 互引展开爆炸、DecisionModel 重复解析 $ref、Vercel AI/AG-UI 适配器消息加载平方复杂度、工具结果反序列化误重建文件类型、MCP URL 路径凭证泄露至前端。低危漏洞为 allowed\_domains 先解析 DNS 后校验。版本同步修复 pydantic-ai-slim v1.107.10 与 pydantic-ai-harness 0.66.0，并新增 OpenSandbox、RenderSandbox、Azure Durable Task、Pixeltable 及 MCP include\_instructions。

github · adtyavrdhn · 11月4日 11:51

**「设计要点」** 安全修复集中在事件循环的正则/JSON 展开攻击面与适配器层输入边界。工具运行时通过返回内容截断、正则回溯修复、域名预检、$ref 去重解析降低阻塞风险。序列化层增加工具结果类型校验，防止反序列化时误触发文件下载。

**「改了什么」** web\_fetch\_tool 本地回退改为先截断返回内容再重排 JSON，消除内存膨胀。private\_key 脱敏正则重写，消除指数回退。allowed\_domains 与 PlaywrightBrowser 出站策略改为先校验域名后解析 DNS。DecisionModel 与 AG-UI 适配器修复 $ref 重复展开与消息加载平方复杂度。新增 OpenSandbox、RenderSandbox 沙箱，Azure Durable Task、Pixeltable 持久化后端，MCP capability 支持 include\_instructions。

**标签**: `#tools`, `#runtime`, `#permissions`

---

<a id="item-harness-arch-3"></a>
### [gemini-cli v0.67.0 发布](https://github.com/google-gemini/gemini-cli/releases/tag/v0.67.0) ⭐️ 6.8/10

gemini-cli v0.67.0 发布。新增 IDE companion 经 exec stdio 桥接容器沙箱，修复 agent 重复加载、上下文过滤、不可信标志检查等核心问题。无重大架构变更。

github · gemini-cli-robot · 11月4日 20:27

**「设计要点」** 无架构层变更。沙箱通信、上下文过滤、权限检查均属增量修复，运行时与工具层保持稳定。

**「改了什么」** \- 新增 IDE companion 通过 exec stdio 桥接容器沙箱
\- 修复工作区为主目录时 agent 重复加载（\#27692）
\- 排除 IDE 设置和 GEMINI.md 自打开文件上下文
\- 限制不可信标志检查范围并记忆已批准标志
\- 新增 models 命令与 --list-models 标志
\- 修复 A2A server 路由注册顺序、RFC 9110 头分割、原子写入硬链接处理、token 元数据对齐、thought signatures 传递、信号取消后工具执行、CRLF diff 等 15 项问题

**标签**: `#sandbox`, `#runtime`, `#permissions`

---

## Agent 工程师日报
{: #sec-agent-engineer .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-agent-engineer" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-agent-engineer-1"></a>
### [Cognition 发布 SWE-2 Flash 模型](https://cognition.ai/blog/swe-2-flash) ⭐️ 8.8/10

Cognition 于 2026 年 11 月 4 日发布美国本土编码模型 SWE-2 Flash，针对软件工程 Agent 的自动化、代码审查、功能开发等核心任务优化。该模型首次在训练流程中新增强化学习前的中间训练阶段，对比基座 Inkling-Small，Terminal-Bench 4.0 得分从 0.9% 升至 20.0%，FrontierCode 2.0 得分从 3.2% 升至 24.0%，性能超过所有美国开源权重模型（含 3 倍尺寸的模型）。SWE-2 Flash 目前已上线 Devin Desktop 与 CLI，价格为同系列更大模型 SWE-2 的 1/5，推理速度为其 3 倍；权重暂不公开，Cognition 计划数周内推出面向行业伙伴与研究机构的受信权重共享计划，该模型 ExploitBench 得分从 11.3% 升至 34.8%。

rss · Cognition Blog · 11月4日 18:00

**「为什么重要」** SWE-2 Flash 是首个公开披露新增预 RL 中间训练阶段并取得可验证编码基准大幅提升的商用编码模型，为编码 Agent 工程师提供了低成本、高响应的新选型；但其权重共享计划尚未落地，具体可及性与安全规则仍不明确。

**「可关注」** 可关注：SWE-2 Flash 通过新增预 RL 中间训练阶段，在 12B 激活参数的 Inkling-Small 基座上实现了编码任务性能的大幅跃升，且成本仅为更大同系列模型的 1/5、推理速度 3 倍，适合对成本与响应速度敏感的编码 Agent 场景，但权重暂未公开，需关注后续受信共享计划的具体规则。

**标签**: `#coding-agent`, `#eval`

---

<a id="item-agent-engineer-2"></a>
### [Anthropic 发布可证明 LLM 推理进展](https://www.anthropic.com/research/provable-inference) ⭐️ 8.0/10

2026 年 11 月 4 日 Anthropic 发布官方研究，公开零知识可证明大模型推理的进展，给出可验证关键指标：承诺大小约 6.5MB，单次承诺支持约 1600 万次请求，24 线程下证明验证耗时 17 秒，计算开销约为 90-100 倍。该成果面向需要可验证模型执行的 LLM Agent 系统构建者，同时社区出现对前期工作归属的争议。

hackernews · ltononro · 11月4日 17:17 · [社区讨论](https://news.ycombinator.com/item?id=50368626)

**「为什么重要」** 已落地的量化性能指标首次为零知识可证明 LLM 推理提供工程参考基准，尚未证实的是该方案在真实 Agent 负载下的成本与延迟是否满足生产要求。

**「可关注」** 可关注：闭源模型提供方的可证明推理计算开销达 90-100 倍，远高于开放权重模型直接重算的方案，需根据模型开放属性选型验证方案。

**「评论」** 社区共识认为这是零知识可证明 LLM 推理的显著进展，同时存在对前期工作 VerInf 引用不足的争议；讨论中明确开放权重模型可通过重算实现更低成本的可证明推理，闭源模型提供方则需面对更高的实现成本，另有用户提及该方案可检测模型路由篡改但相关场景未证实。

**标签**: `#observability`, `#eval`, `#harness`

---

<a id="item-agent-engineer-3"></a>
### [Kimi K3.1 Pro 权重开源](https://huggingface.co/moonshotai/Kimi-K3.1-Pro) ⭐️ 7.0/10

2026 年 11 月 4 日，Moonshot AI 在 HuggingFace 正式发布 Kimi K3.1 Pro 大模型的开源权重，仓库地址为 https://huggingface.co/moonshotai/Kimi-K3.1-Pro，该模型在 HuggingFace  trending 榜单中 trendingScore 达 556，获赞 568 次。社区讨论覆盖第三方推理提供商的吞吐优化空间、与 DeepSeekV4.1-Flash 等竞品开源模型的基准表现差异、本地部署算力门槛，以及该模型在 coding agent、eval 场景的适用性。目前社区对模型基准表现存在分歧，部分用户认为存在刷榜倾向，也有实际测试反馈称其日常用例表现足够优秀。

hackernews · Hugging Face Trending Models · 11月4日 15:30 · [社区讨论](https://news.ycombinator.com/item?id=50366999)

**「为什么重要」** 这是 Moonshot AI 首次公开 K3.1 系列 Pro 版本的官方权重，为 AI agent 团队提供了新的模型选型选项。目前第三方推理提供商已开始接入该模型，后续推理成本与性能的优化空间值得关注，但模型本地部署的高算力门槛尚未有官方明确说明。

**「可关注」** 可关注：第三方推理提供商（如 Together、Modal）对 Kimi K3.1 Pro 的吞吐优化效果，以及该模型在 coding agent 实际任务中的表现与成本 tradeoff。

**「评论」** 社区对模型基准表现与开放程度存在分歧：部分用户认为其 benchmark 成绩未明显超过 DeepSeekV4.1-Flash，存在刷榜嫌疑；也有实际测试者反馈其在多数日常用例中表现优秀，足够满足通用需求。另有用户质疑其“开源权重”的宣传表述，认为与实际开放程度存在差异，同时有社区用户提到本地部署该模型可能需要 8 台 B300 级别节点的算力门槛。

**标签**: `#coding-agent`, `#eval`, `#harness`

---

<a id="item-agent-engineer-4"></a>
### [OpenAI 协调修复 948 个 Linux 内核提权漏洞](https://openai.com/index/a-thousand-fewer-paths-to-root/) ⭐️ 7.0/10

2026 年 11 月 4 日 OpenAI 安全团队公开宣布，已发现并协调完成 948 个 Linux 内核权限提升漏洞的修复工作。这些漏洞作用于 AI Agent 及其运行框架依赖的底层计算基础设施，修复后降低了关键权限相关的攻击面。目前未披露受影响的具体内核版本范围及漏洞利用场景细节。

hackernews · dangelosaurus · 11月4日 23:33 · [社区讨论](https://news.ycombinator.com/item?id=50372929)

**「为什么重要」** 该事件直接加固了 AI Agent 及其运行框架的底层运行环境安全基线，减少了权限类攻击的入口。社区围绕 AI 驱动漏洞发现对 Agent 工具链安全的影响仍在讨论，暂无官方进一步结论。

**「可关注」** 可关注：AI Agent 运行所依赖的底层内核权限类漏洞的修复进度，以及 AI 驱动漏洞发现能力对自身工具链安全的影响。

**「评论」** 社区讨论呈现多个方向：部分用户对 Linux 内核存在大量提权漏洞的根源提出质疑，另一部分用户关注 AI 驱动漏洞发现的效率与投入产出关系，还有用户对现有系统在大量潜在漏洞下的稳定性表示疑惑。

**标签**: `#permissions`, `#harness`, `#eval`

---

<a id="item-agent-engineer-5"></a>
### [LoCo 推理压缩方法提出](https://huggingface.co/papers/2611.04814) ⭐️ 7.0/10

Hugging Face Daily Papers 于 2026-11-05 推荐论文《Think Less, Locally: Local Preference Learning for Reasoning Compression》，提出 LoCo 推理压缩方法。该方法从模型自身推理轨迹中检测过度思考状态，冻结对应推理前缀，从相同状态重新生成更短的验证延续，再以状态条件偏好对进行 DPO 训练。材料显示论文内容被截断，缺乏完整性能验证数据，但标签指向 coding-agent 场景。

rss · Hugging Face Daily Papers · 11月5日 04:00

**「为什么重要」** 推理模型过度思考导致的成本问题是 coding agent 等应用的实际痛点。LoCo 提供了技术上具体、可复现的压缩路径，但完整效果尚待完整论文验证。

**「可关注」** 可关注：LoCo 利用模型自身轨迹检测过度思考状态，通过状态条件 DPO 训练实现推理压缩，为降低 coding agent 推理开销提供了可复现的技术路径。

**标签**: `#coding-agent`

---

<a id="item-agent-engineer-6"></a>
### [Dharma Field Extractor 2B 模型发布](https://huggingface.co/blog/Dharma-AI/dharma-field-extractor) ⭐️ 6.8/10

2026 年 11 月 4 日，Hugging Face 官方博客发布 Dharma Field Extractor 2B 参数文档字段提取模型，可将任意文档图像转为结构化 JSON 输出。该模型基于 DharmaOCR-LITE v1.1 微调 LoRA 适配器得到，支持开放提取、Schema 定向两种请求模式，覆盖发票、表单、身份证等多类文档，无需 per-type 微调。官方称其在 546 份文档、1638 个用例的 benchmark 上取得 0.834 的字段级 F1 分数，高于测试的所有前沿 LLM 配置，自托管单 L40S 成本比 frontier API 低 6 至 147 倍。当前公开材料未披露完整技术规格与详细 benchmark 数据，仅面向需要文档结构化处理的 agent 工具链、企业文档处理场景开放试用。

rss · Hugging Face Blog · 11月4日 17:50

**「为什么重要」** 该模型首次在文档字段提取任务上实现专用小模型性能超过前沿 LLM 且成本大幅降低，为高吞吐量文档处理的 agent 工具链提供了新的可选方案。但当前公开材料未披露完整技术细节与多语言场景下的实际表现，大规模部署效果尚未证实。

**「可关注」** 可关注：基于领域专用 OCR 基座加 LoRA 适配器实现的文档字段提取模型，可在无 per-type 微调的情况下支持多类文档的开放/Schema 定向提取，且自托管成本显著低于按 token 计费的前沿 LLM API。

**标签**: `#toolchain`, `#eval`

---

<a id="item-agent-engineer-7"></a>
### [OpenAI Images 2.6 发布](https://openai.com/index/introducing-images-2-6/) ⭐️ 6.0/10

OpenAI 2026 年 11 月 4 日正式发布 Images 2.6 图像生成模型，新增网格提示词生成一致动画帧、原生 SVG 输出两项能力，社区对生成质量反馈褒贬不一，该更新仅对将图像生成集成到 Agent 工具链或评估相关 Agent 能力的工程师有直接参考价值。

hackernews · davidbarker · 11月4日 23:35 · [社区讨论](https://news.ycombinator.com/item?id=50372945)

**「为什么重要」** 该更新提供了 Agent 可调用的新图像生成能力，但社区已指出动画帧一致性存疑、SVG 输出实现逻辑异常，实际落地效果尚未验证，仅对相关集成开发者有短期参考意义。

**「可关注」** 可关注：Images 2.6 新增的网格提示词动画帧生成、原生 SVG 输出能力，可纳入 Agent 图像生成工具链的候选能力清单，但需先验证帧一致性、SVG 可用性是否满足业务要求。

**「评论」** 社区反馈两极，部分用户认为生成质量倒退、动画帧间噪声明显，也有用户指出网格提示词生成动画帧并非新技巧，对 SVG 输出的实现方式存疑，整体认为图像生成领域进步有限。

**标签**: `#eval`, `#toolchain`, `#image-generation`

---

<a id="item-agent-engineer-8"></a>
### [Route Anything 论文：通用 AI 路由框架](https://huggingface.co/papers/2611.05275) ⭐️ 6.0/10

Hugging Face Daily Papers 于 2026-11-05 分享论文《Route Anything: A Study of Model and Policy Routing for General-Purpose AI Systems》。该论文提出统一框架研究通用 AI 系统的模型与策略路由，开发刻画最优路由的统一理论基础，方向与 Agent 编排核心需求直接相关。当前内容截断，未提供完整技术细节、性能数据或可复现实现，需查阅原文进一步评估实际价值。

rss · Hugging Face Daily Papers · 11月5日 04:00

**「为什么重要」** 该方向直接关联 Agent 编排与任务路由核心需求，但当前摘要截断，未提供可验证的性能数据或实现细节，实际价值需待原文评估。

**「可关注」** 模型与策略路由统一框架与 Agent 编排需求的契合度，但当前摘要截断，缺技术细节与性能数据，需待原文评估。

**标签**: `#orchestration`, `#eval`

---

## AI 日报
{: #sec-ai-daily .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-daily" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-daily-1"></a>
### [OpenAI 拟收购 Pierre Computer Company](https://openai.com/index/openai-to-acquire-pierre) ⭐️ 7.8/10

OpenAI 官方宣布计划收购 Pierre Computer Company, Inc.，核心目的是扩展 Codex 在代码构建、理解与审查场景的工具能力。目前公开细节有限。

rss · OpenAI Blog · 11月4日 14:30

**「为什么重要」** Codex 是 OpenAI 面向代码智能场景的核心产品，此次收购将直接补充其代码构建、理解与审查的工具能力，是代码智能工具领域的最新动态。

**「可关注」** 可关注：Codex 后续在代码构建、理解、审查场景的工具更新与整合进展。

**标签**: `#lab`, `#industry`, `#product`

---

<a id="item-ai-daily-2"></a>
### [Daybreak Red 上线 AWS GovCloud 美东区](https://openai.com/index/daybreak-red-aws-govcloud) ⭐️ 7.8/10

OpenAI 已将 Daybreak Red（即 GPT-5.6 Cyber）模型上线至 AWS GovCloud（US-East）区域的 Amazon Bedrock 平台。该服务仅对获批客户开放，用途限定为授权网络安全工作。

rss · OpenAI Blog · 11月4日 07:00

**「为什么重要」** 该部署为 AWS GovCloud（US-East）的授权网络安全场景新增了官方模型访问渠道，服务仅面向批准客户开放。

**「可关注」** 可关注：AWS GovCloud（US-East）的批准客户可通过 Amazon Bedrock 接入 Daybreak Red 开展授权网络安全工作。

**标签**: `#model`, `#lab`, `#product`

---

<a id="item-ai-daily-3"></a>
### [OpenAI 自主流水线修复 948 个提权漏洞](https://openai.com/index/a-thousand-fewer-paths-to-root) ⭐️ 7.8/10

OpenAI 官方博客 2026 年 11 月 4 日宣布，其研发的自主流水线已完成 948 个 Linux 内核本地权限提升漏洞的发现、验证与补丁生成。该流水线实现了漏洞处理全链路的自动化，覆盖从漏洞识别到补丁输出的完整步骤，无需人工介入核心流程。

rss · OpenAI Blog · 11月4日 08:00

**「为什么重要」** Linux 内核本地权限提升漏洞属于系统高危风险，攻击者利用后可直接获取系统 root 权限，广泛影响服务器、嵌入式设备等场景。该自主流水线实现全流程自动化，可大幅压缩漏洞修复周期，降低人工排查成本。

**「可关注」** 可关注：该自主流水线的漏洞发现、验证、补丁生成全流程自动化方案的可复用性与跨场景适配能力。

**标签**: `#lab`, `#industry`

---

<a id="item-ai-daily-4"></a>
### [Lion-ER-35B-A3B 具身推理模型发布](https://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw==&amp;mid=2247939340&amp;idx=2&amp;sn=25a664251ec6cb5820f1268911de9141) ⭐️ 5.5/10

据量子位报道，招商局先进技术研究院下属狮子山人工智能实验室发布具身推理视觉语言模型「驭物™ Lion-ER-35B-A3B」。该模型采用 MoE 混合专家架构，总参数约 35B，单 Token 激活参数约 3B，宣称在十项主流具身相关基准上实现全部指标上涨，技术路线为能力牵引的具身数据引擎闭环迭代，而非堆砌训练数据。

rss · 量子位 · 11月4日 05:33

**「为什么重要」** 该模型尝试跳出具身领域“堆数据提性能”的常见训练惯性，通过能力牵引的数据闭环针对性补全机器人对三维空间关系、物体状态变化、任务进度的感知与推理能力，为低开销具身模型落地提供了新思路。

**「可关注」** 可关注：MoE 架构在具身推理场景下以低激活参数实现多基准性能提升的技术路径是否可复现。

**标签**: `#model`, `#lab`, `#industry`

---

<a id="item-ai-daily-5"></a>
### [Seq-Drifting 实现扩散语言模型一步生成](https://mp.weixin.qq.com/s?__biz=MzIwMTc4ODE0Mw==&amp;mid=2247723829&amp;idx=2&amp;sn=50729365492d766992fa8bf441dac962) ⭐️ 5.5/10

香港城市大学、深圳大学、中国科学技术大学、牛津大学研究团队提出 Seq-Drifting 方法，尝试将扩散语言模型的多轮去噪生成过程压缩为单步完成，核心是通过依赖当前生成上下文的漂移场，训练模型协调不同位置的词元选择。在无条件 128-token 生成任务中，该方法生成困惑度（Gen-PPL）达 36.01，相较四步蒸馏基线 FMLM 实现 11.2 倍实际运行时间加速。不过该内容为科技媒体二手转述，未附官方一手可核对来源，缺乏更多可验证的官方细节。

rss · PaperWeekly · 11月4日 04:05

**「为什么重要」** 当前扩散语言模型虽支持并行生成词元，但仍需多轮去噪保障文本质量，主流自回归模型又存在串行依赖、长输出耗时久的问题，Seq-Drifting 的一步生成框架为提升文本生成效率提供了新路径，且已在条件续写、机器翻译、摘要生成、推理任务上完成初步验证。

**「可关注」** 可关注：Seq-Drifting 的论文、代码及模型权重已公开，可通过 arXiv 链接、GitHub 仓库 \`jyliu-ai/Seq-Drifting\` 及 Hugging Face 仓库 \`jyliuAI/Seq-Drifting\` 获取。

**标签**: `#model`, `#research`, `#paper`

---

## AI 羊毛
{: #sec-ai-deals .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-deals" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-deals-1"></a>
### [Samewindow 免费备份 ChatGPT Claude 对话](https://www.samewindow.com/) ⭐️ 7.0/10

HN 用户 gsngsn 分享免费的 Samewindow Chrome 扩展，提供分别适配 ChatGPT、Claude 的两个独立版本，支持备份对应平台的 AI 对话、在平台内创建文件夹，可直接通过 Chrome 商店安装，无显性付费限制。

rss · HN Free API / Credits · 11月4日 13:04

**「为什么重要」** 当前无显性付费限制，Chrome 商店可直接安装，适合需要备份 AI 对话的用户立即使用。

**「可关注」** 可关注：该扩展提供适配 ChatGPT 与 Claude 的独立版本，需分别在对应 Chrome 商店页面安装。

**标签**: `#free-tier`, `#chrome-extension`, `#ai-tool`, `#promo`

---