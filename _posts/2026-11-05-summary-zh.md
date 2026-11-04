---
layout: default
title: "Horizon Summary: 2026-11-05 (ZH)"
date: 2026-11-05
lang: zh
---

> 从 213 条内容中筛选出 16 条重要资讯。

<nav id="ah-toc" class="ah-toc" aria-label="目录"><span class="ah-toc-title">目录</span><ul><li><a href="#sec-harness-arch"><span class="ah-toc-name">Harness 架构</span><span class="ah-toc-count">3条</span></a></li><li><a href="#sec-agent-engineer"><span class="ah-toc-name">Agent 工程师日报</span><span class="ah-toc-count">10条</span></a></li><li><a href="#sec-ai-daily"><span class="ah-toc-name">AI 日报</span><span class="ah-toc-count">3条</span></a></li></ul></nav>

---

**[Harness 架构](#sec-harness-arch)**
1. [Mastra Core 1.82.0 发布](#item-harness-arch-1) ⭐️ 8.8/10
2. [pydantic-ai v2.66.0 发布](#item-harness-arch-2) ⭐️ 7.8/10
3. [Gemini CLI v0.67.0 发布](#item-harness-arch-3) ⭐️ 7.8/10

**[Agent 工程师日报](#sec-agent-engineer)**
1. [Anthropic 发布可证明推理研究](#item-agent-engineer-1) ⭐️ 8.0/10
2. [Cognition 发布 SWE-2 Flash 模型](#item-agent-engineer-2) ⭐️ 7.8/10
3. [Axion 1.0 开源智能体基础模型发布](#item-agent-engineer-3) ⭐️ 7.0/10
4. [ToolSpace 框架反置 MCP 环境合成流程](#item-agent-engineer-4) ⭐️ 7.0/10
5. [WebHarbor 论文：153 个 Docker 化网站环境](#item-agent-engineer-5) ⭐️ 7.0/10
6. [datasette-apps 0.3a0 发布](#item-agent-engineer-6) ⭐️ 6.8/10
7. [Dharma Field Extractor 文档提取模型发布](#item-agent-engineer-7) ⭐️ 6.3/10
8. [Kimi K3.1 Pro 权重开源](#item-agent-engineer-8) ⭐️ 6.0/10
9. [datasette-agent 0.5a0 发布](#item-agent-engineer-9) ⭐️ 6.0/10
10. [RoboColosseum 具身智能评估框架发布](#item-agent-engineer-10) ⭐️ 6.0/10

**[AI 日报](#sec-ai-daily)**
1. [OpenAI 修复 948 个 Linux 内核本地提权漏洞](#item-ai-daily-1) ⭐️ 8.8/10
2. [OpenAI 将收购 Pierre Computer Company](#item-ai-daily-2) ⭐️ 7.8/10
3. [Claude Marketplace 新增 25+ 合作伙伴工具](#item-ai-daily-3) ⭐️ 7.8/10

---

## Harness 架构
{: #sec-harness-arch .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-harness-arch" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-harness-arch-1"></a>
### [Mastra Core 1.82.0 发布](https://github.com/mastra-ai/mastra/releases/tag/%40mastra/core%401.82.0) ⭐️ 8.8/10

Mastra 发布 @mastra/core@1.82.0，核心更新为 Knowledge v2 记忆子系统。新 page-tree 数据模型将知识组织为 pages/notes/pins，配套增强的 knowledge\_list、knowledge\_read（支持行/节/grep 风格读取）及列表固定能力。新增服务器端同步 API（knowledge.upsertPage/removePage）与只读 HTTP/JS 客户端 API（含 SSE 变更流），后者经 scope 门控与 FGA 检查。持久化 agent 现支持 API 重启后的 worker 连续性，但需 fencing-capable 共享存储（如 @mastra/pg 的 PostgresStore）与共享 pubsub。

github · PaulieScanlon · 11月4日 10:59

**「设计要点」** 事件化持久化 agent 的跨进程连续性依赖 fencing-capable 共享存储与共享 pubsub/lease 基础设施，每个 run 保持独立所有权，避免嵌套 durable agent 间的所有权冲突。只读 Knowledge 路由采用 scope 门控与 FGA 感知，支持通过 SSE 推送变更事件。

**「改了什么」** Knowledge v2 以 page-tree 模型替代旧记忆结构，移除 experimental\_subconscious、Memory knowledge 选项与 knowledge.reindex\(\)，知识必须直接挂载到 Agent；新增服务器端 upsertPage/removePage 同步接口及只读客户端 API（listKnowledge/getKnowledge）与 SSE 流。持久化 agent 在 API 关闭后由 worker 继续执行，需配合 PostgresStore 等 fencing 存储实现跨进程连续性；@mastra/temporal@0.5.0 开始验证 step 输入 schema，@mastra/factory@0.27.0 移除 work-item claiming APIs。

**标签**: `#memory`, `#tools`, `#permissions`

---

<a id="item-harness-arch-2"></a>
### [pydantic-ai v2.66.0 发布](https://github.com/pydantic/pydantic-ai/releases/tag/v2.66.0) ⭐️ 7.8/10

pydantic-ai 发布 v2.66.0，同步修复 v1.107.10。本次修复两个高危安全漏洞：web\_fetch\_tool 本地回退在处理深度嵌套 JSON 时发生内存耗尽，private\_key 密钥脱敏正则存在指数级回溯。新增 OpenSandbox、RenderSandbox 自托管工作空间，以及 Azure Durable Task、Pixeltable 工具与记忆存储。MCP 能力新增 include\_instructions 参数，可排除服务器指令。

github · adtyavrdhn · 11月4日 11:51

**「设计要点」** 事件循环上执行 JSON 重缩进与密钥脱敏，导致内存和 CPU 消耗不受控。工具层和适配器（AG-UI、Vercel AI）对客户端提交的 schema 和消息做内联展开，触发指数级复杂度。

**「改了什么」** 修复 web\_fetch\_tool 本地回退内存耗尽与 private\_key 脱敏正则回溯两个高危漏洞，新增 OpenSandbox、RenderSandbox 自托管沙箱及 Azure Durable Task、Pixeltable 集成，MCP 能力增加 include\_instructions 参数。

**标签**: `#tools`, `#permissions`, `#runtime`

---

<a id="item-harness-arch-3"></a>
### [Gemini CLI v0.67.0 发布](https://github.com/google-gemini/gemini-cli/releases/tag/v0.67.0) ⭐️ 7.8/10

这是 Google 官方 Gemini CLI v0.67.0 正式发布，新增 IDE companion 通过 exec stdio 桥接到容器沙箱的能力，同时修复非受信标志权限检查范围、重复加载 agent、A2A 服务路由顺序等多个核心问题，还新增 models 命令与--list-models 参数用于模型发现。

github · gemini-cli-robot · 11月4日 20:27

**「改了什么」** 新增 IDE companion 通过 exec stdio 接入容器沙箱的能力；新增 models 命令与--list-models 参数用于模型发现；修复非受信标志检查仅作用于外部输出且持久化用户已批准标志的问题；修复重复加载 agent、A2A 服务路由顺序、请求取消后仍执行工具等多个核心缺陷。

**标签**: `#sandbox`, `#permissions`, `#runtime`

---

## Agent 工程师日报
{: #sec-agent-engineer .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-agent-engineer" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-agent-engineer-1"></a>
### [Anthropic 发布可证明推理研究](https://www.anthropic.com/research/provable-inference) ⭐️ 8.0/10

2026 年 11 月 4 日，Anthropic 发布可证明推理研究，通过零知识证明确保客户端可密码学验证指定 LLM 是否生成给定输出。关键性能指标为：计算开销 90-100 倍，证明验证耗时 17 秒（24 线程），承诺大小约 6.5MB，单个承诺可覆盖约 1600 万次请求。当前高计算成本限制该方案的生产可用性，主要影响需要 LLM 输出可验证性的 agent 工程、工具链设计场景。

hackernews · ltononro · 11月4日 17:17 · [社区讨论](https://news.ycombinator.com/item?id=50368626)

**「为什么重要」** 这是零知识证明在 LLM 推理验证领域的首次公开量化落地方案，性能指标显著优于过往相关 zk 结果。但 90-100 倍的计算开销尚未验证生产环境可行性，对强验证需求的 agent 场景的价值仍待落地验证。

**「可关注」** 可关注：闭源模型提供方的可证明推理成本远高于开源模型的重跑验证方案，当前 90-100 倍计算开销是生产落地的核心瓶颈。

**「评论」** 社区存在两点主要讨论：一是该方案被指基于 VerInf 工作但引用标注不足；二是开源模型可通过重跑 deterministic 推理低成本实现可证明推理，当前高开销的零知识证明方案更适合闭源模型场景。

**标签**: `#observability`, `#eval`, `#permissions`, `#harness`

---

<a id="item-agent-engineer-2"></a>
### [Cognition 发布 SWE-2 Flash 模型](https://cognition.ai/blog/swe-2-flash) ⭐️ 7.8/10

2026 年 11 月 4 日，Cognition 官方发布全美产编码模型 SWE-2 Flash，核心创新为在强化学习阶段前新增中间训练阶段。该模型基于 276B 总参数、12B 激活参数的 Inkling-Small 基座，Terminal-Bench 4.0 得分从基座的 0.9% 提升至 20.0%，FrontierCode 2.0 从 3.2% 提升至 24.0%，性能超过所有美国开源权重编码模型，包括参数量大 3 倍的模型。SWE-2 Flash 已上线 Devin Desktop 与 CLI，价格为同系列更大模型 SWE-2 的 1/5，速度为 3 倍，目前暂不公开权重，计划后续向可信行业伙伴与研究机构安全共享，其针对网络安全场景优化训练，ExploitBench 得分从 11.3% 提升至 34.8%。

rss · Cognition Blog · 11月4日 18:00

**「为什么重要」** 该模型首次在编码模型训练中验证了强化学习前中间训练阶段的有效性，以较小参数量实现了远超基座、甚至超过更大开源模型的编码性能，为编码模型训练流程提供了新的参考方向。其权重共享计划若落地，或为行业提供兼顾透明度与安全性的模型访问方案，但具体落地节奏与影响尚未明确。

**「可关注」** 可关注：SWE-2 Flash 通过强化学习前的中间训练阶段、分阶段安排稀缺高质量数据、优化 RL 任务质量与多样性，实现了小参数量编码性能的大幅提升，其训练数据配比与 RL 任务设计的思路可参考。

**标签**: `#coding-agent`, `#eval`

---

<a id="item-agent-engineer-3"></a>
### [Axion 1.0 开源智能体基础模型发布](https://huggingface.co/papers/2611.03233) ⭐️ 7.0/10

2026 年 11 月 4 日 Hugging Face Daily Papers 介绍 arXiv 预印本提出的 Axion 1.0，这是一款完全开源的智能体基础模型。该模型采用简化 3 阶段训练流程：两个轻量监督微调阶段后接强化学习，未使用 DPO、OPD 或中间训练；第一阶段通过模型感知数据构建实现强自包含推理，合成挑战性问题并基于基础模型自身的成功解题策略对抗性强化问题，第二阶段通过可扩展流水线构建真实世界工具依赖的自动可验证任务。当前公开内容被截断，缺少性能评估结果与完整技术规格。

rss · Hugging Face Daily Papers · 11月4日 00:00

**「为什么重要」** 已公开的简化训练流程与两类数据构建方法，为开源智能体模型训练提供了可参考的实现路径。具体性能表现、泛化能力等影响尚未公开，需等待完整论文验证。

**「可关注」** 可关注：其无 DPO/OPD 的 3 阶段训练流程、基于基础模型解题策略的推理数据构建方法，以及工具任务自动生成流水线的可复现性。

**标签**: `#coding-agent`

---

<a id="item-agent-engineer-4"></a>
### [ToolSpace 框架反置 MCP 环境合成流程](https://huggingface.co/papers/2611.05036) ⭐️ 7.0/10

2026 年 11 月 4 日，Hugging Face Daily Papers 收录论文《ToolSpace: Scaling Tool-Centric Environment Synthesis for Long-Horizon Agents》。该论文提出工具中心框架 ToolSpace，反置现有数据为中心的环境缩放流程：先从真实 MCP 服务执行迹和开放代理语料中，用确定性规则挖掘相邻调用间的数据、状态与重试依赖，构建加权工具组合图并聚类为环境，最后合成数据库。现有方法存在工具接口不匹配真实服务、组合未基于执行验证、任务跨环境能力弱等缺陷。该框架对 MCP 代理评测环境构建与 Harness 开发有直接参考价值。

rss · Hugging Face Daily Papers · 11月4日 00:00

**「为什么重要」** 论文已发布，其工具优先的合成顺序与确定性规则挖掘方法，为 MCP 代理评测环境提供了一种可复现的构建路径。实际效果与适用范围尚需后续实验验证。

**「可关注」** 可关注：ToolSpace 用确定性规则替代 LLM 判断挖掘执行迹中的工具依赖，将环境构建反转为工具优先，可能降低合成环境与真实 MCP 服务的接口偏差。

**标签**: `#mcp`, `#eval`, `#harness`

---

<a id="item-agent-engineer-5"></a>
### [WebHarbor 论文：153 个 Docker 化网站环境](https://huggingface.co/papers/2611.03634) ⭐️ 7.0/10

2026 年 11 月 4 日，Hugging Face Daily Papers 收录 WebHarbor 论文（获 19 次点赞）。该论文提出 153 个 Docker 化真实网站环境的确定性套件，用于 GUI web agent 训练与评估。相比实时网站评估的内容变动、访问限制和认证工作流覆盖不足，以及现有合成环境的功能深度与视觉保真度缺陷，WebHarbor 在确定性控制下重建真实网络服务的界面、内容与工作流。环境通过任务驱动的人机协作构建，coding agents 实现功能扩展，人类贡献者审计视觉保真度与功能，但具体审计标准与任务分布未在摘要中披露。

rss · Hugging Face Daily Papers · 11月4日 00:00

**「为什么重要」** GUI agent 评估长期受实时网站不稳定与合成环境保真度不足困扰。WebHarbor 提供可复现的 Docker 化真实环境套件，直接服务于评估 harness 与 GUI agent 训练 pipeline 的稳定性需求。论文已公开，但实际环境覆盖范围与任务难度分布仍需查阅原文确认。

**「可关注」** 可关注：WebHarbor 的确定性 Docker 化重建模式，或可降低 GUI agent 评估中实时网站波动带来的方差。

**标签**: `#eval`, `#coding-agent`, `#harness`

---

<a id="item-agent-engineer-6"></a>
### [datasette-apps 0.3a0 发布](https://github.com/datasette/datasette-apps/releases/tag/0.3a0) ⭐️ 6.8/10

simonw 于 2026 年 11 月 4 日发布 datasette-apps 0.3a0，该版本为 alpha 阶段，核心优化 Datasette Agent 创建和编辑应用的能力。新增 app\_add\_stored\_queries、app\_remove\_stored\_queries 两个 agent 工具（对应\#43），用于管理应用可调用的存储查询，授予写查询需用户提前审批；app\_create\(\)（对应\#43）现在会校验请求的存储查询是否存在、用户是否具备查看权限，创建应用前需用户批准写查询。此外，Datasette Agent 聊天支持输入\#自动补全有权限的应用，应用工具结果新增相对路径，应用链接与查看按钮现可在 Datasette Agent 面板全屏打开。该版本要求 Datasette 1.0a41 及以上，新增 Python 3.15 支持，移除 Python 3.10 支持。

github · simonw · 11月4日 00:29

**「为什么重要」** 该版本在 agent 工具链中落地了写操作的权限校验与用户审批流程，为同类 agent 工具的权限设计提供了可参考的实现样本；目前功能范围限定在 Datasette 应用管理场景，仍处于 alpha 阶段，功能稳定性尚未验证。

**「可关注」** 可关注：agent 工具对写操作采用前置权限校验+用户审批的流程设计，以及通过返回相对路径替代自行拼接 URL 的链接处理方式。

**标签**: `#agent`, `#permissions`, `#datasette`

---

<a id="item-agent-engineer-7"></a>
### [Dharma Field Extractor 文档提取模型发布](https://huggingface.co/blog/Dharma-AI/dharma-field-extractor) ⭐️ 6.3/10

Hugging Face 2026 年 11 月 4 日发布 Dharma Field Extractor，这是一个 20 亿参数的文档字段提取模型，基础模型为 DharmaOCR-LITE v1.1，额外训练 LoRA 适配器，支持开放提取、schema 定向提取两种模式，可输出结构化 JSON，覆盖收据、发票、身份证、表单等多类文档，支持英语、葡萄牙语等多语言。博客声称其在自建 546 份文档、1638 个测试用例的基准上，字段级 F1 得分 0.834，高于测试的所有前沿 LLM 配置（Claude Opus 5 为 0.816，GPT-5.6 Luna 为 0.741），单 L40S GPU 自托管成本比所测 API 低 6 至 147 倍。该模型主要面向需要高吞吐量文档结构化提取的 toB 工具链、表单处理、合规录入等场景的开发者。

rss · Hugging Face Blog · 11月4日 17:50

**「为什么重要」** 该模型为文档字段提取这一垂直场景提供了小模型替代通用 LLM API 的潜在方案，但当前性能与成本优势均来自发布方自建基准，尚未得到独立验证，且未涉及 agent 架构、通用评测框架等通用领域的突破，影响面较窄。

**「可关注」** 可关注：垂直领域小模型通过任务专用训练，在特定结构化提取场景上可能同时实现质量与成本优势，但需优先验证发布方基准的泛化性与实际生产环境的稳定性。

**标签**: `#toolchain`, `#eval`, `#orchestration`

---

<a id="item-agent-engineer-8"></a>
### [Kimi K3.1 Pro 权重开源](https://huggingface.co/moonshotai/Kimi-K3.1-Pro) ⭐️ 6.0/10

2026 年 11 月 4 日，Hacker News 社区分享 Kimi K3.1 Pro 模型权重已在 Hugging Face 公开，仓库地址为 moonshotai/Kimi-K3.1-Pro，该模型为图像-文本-文本多模态类型，Hugging Face trendingScore 达 453，获 461 个赞。社区反馈的关键信息包括：有用户指出全精度运行需约 8 台 B300 节点的高硬件成本；性能存在争议，部分用户认为其未明显超过 DeepSeekV4.1-Flash，存在“刷榜”嫌疑，也有实测用户称其是强开源模型，多数场景可用；已有 OpenRouter、Together、Modal 等第三方推理服务商托管该模型，其中 Together 吞吐量为 Moonshot 官方端点的 2 倍，Modal 吞吐量为官方端点的 4 倍。该模型为 coding agent、模型选型、推理优化方向的工程师提供了新的可选方案。

hackernews · Hugging Face Trending Models · 11月4日 15:30 · [社区讨论](https://news.ycombinator.com/item?id=50366999)

**「为什么重要」** 该模型是近期公开的高关注度开源多模态模型，第三方推理托管已快速落地，为工程师提供了新的模型选型选项；但其实际性能在 coding agent 场景的适配性、不同推理渠道的成本差异等仍需进一步验证。

**「可关注」** 可关注：第三方推理服务商已快速跟进托管该模型，且存在明显的吞吐量差异，后续可对比其在不同 coding agent 任务中的实际表现与成本。

**「评论」** 社区对模型性能存在明显分歧：部分用户认为其 benchmarks 存在“刷榜”嫌疑，未明显超越 DeepSeekV4.1-Flash；也有实测用户反馈其实际表现强劲，多数场景可用。同时社区普遍关注其高硬件运行成本与第三方推理优化的空间。

**标签**: `#coding-agent`, `#eval`, `#harness`

---

<a id="item-agent-engineer-9"></a>
### [datasette-agent 0.5a0 发布](https://simonwillison.net/2026/Nov/3/datasette-agent/) ⭐️ 6.0/10

2026 年 11 月 3 日，Simon Willison 发布 datasette-agent 0.5a0。本次更新核心新增 panel UI，支持 agent 聊天窗口与 Datasette 数据库页面（如表、查询页）并排显示；结合 datasette-apps 可通过相邻聊天界面提示生成、修改数据库支撑的应用，当前需 GitHub 账号登录 agent.datasette.io 体验。

rss · Simon Willison · 11月3日 23:13

**「为什么重要」** 该发布验证了数据库页面旁置聊天界面的 agent 交互范式，但工具本身受众较窄，对通用 agent harness 设计的参考价值有限。

**「可关注」** 可关注数据库支撑应用通过侧边聊天界面迭代的交互模式，以及 panel 式 UI 在 agent 工具链中的适配可能性。

**标签**: `#coding-agent`, `#harness`, `#orchestration`, `#observability`

---

<a id="item-agent-engineer-10"></a>
### [RoboColosseum 具身智能评估框架发布](https://huggingface.co/papers/2611.02497) ⭐️ 6.0/10

2026-11-04，Hugging Face Daily Papers 发布论文，提出 RoboColosseum 分布式评估框架，提供统一策略服务与标准化协议，用于在本地运营的机器人网络上评估视觉-语言-动作（VLA）策略与前沿 AI 智能体。初始研究覆盖 SO-101、Franka、Bimanual-YAM、G1 Humanoid 四种形态，测试 5 个 VLA 策略与 3 个前沿 AI 智能体。Open Track 在匹配本地条件下进行无任务特定适配的盲法 pairwise 试验；Fine-tune Track 测量策略在全部四种形态上对 20 个任务的适配能力。材料未提供具体性能数字或完整复现细节。

rss · Hugging Face Daily Papers · 11月4日 00:00

**「为什么重要」** 该框架针对物理试验可复现性差的问题，提出统一策略服务与标准化协议，对具身智能系统的评估与 harness 设计具有参考价值。但影响目前局限于具身 AI 领域，材料未提供跨领域迁移证据。

**「可关注」** 可关注：框架通过统一策略服务与标准化协议尝试解决物理试验可复现性差的问题，其 Open Track 盲法 pairwise 设计与 Fine-tune Track 跨 20 任务适配度量，为具身智能评估提供了可复用的 harness 模式。

**标签**: `#eval`, `#harness`, `#orchestration`

---

## AI 日报
{: #sec-ai-daily .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-daily" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-daily-1"></a>
### [OpenAI 修复 948 个 Linux 内核本地提权漏洞](https://openai.com/index/a-thousand-fewer-paths-to-root) ⭐️ 8.8/10

OpenAI 官方披露其构建的自主漏洞修复管道，已在 Linux 内核中发现、验证并生成 948 个本地权限提升漏洞的补丁，这是该自动化漏洞修复技术首次在核心系统级基础设施上完成大规模漏洞全流程处理。

rss · OpenAI Blog · 11月4日 08:00

**「为什么重要」** 该成果是自动化安全工具从实验室走向真实高复杂度生产环境的实质性落地案例，为后续系统级漏洞自动化治理提供了可参考的实践路径。

**「可关注」** 可关注：自主漏洞修复管道完成了 Linux 内核这一高复杂度场景下 948 个本地提权漏洞的发现、验证与补丁生成全流程，验证了自动化安全工具在核心基础设施场景的落地可行性。

**标签**: `#lab`, `#industry`, `#product`

---

<a id="item-ai-daily-2"></a>
### [OpenAI 将收购 Pierre Computer Company](https://openai.com/index/openai-to-acquire-pierre) ⭐️ 7.8/10

OpenAI 官方宣布将收购 Pierre Computer Company，核心目标是扩展 Codex 产品的代码构建、理解与审查相关工具能力。本次公告仅披露核心方向，未公开收购金额、交割时间等细节。

rss · OpenAI Blog · 11月4日 14:30

**「为什么重要」** 该收购是 OpenAI 布局代码工具链的直接动作，明确指向 Codex 产品的能力迭代方向，对关注 coding agent 工具生态的从业者有参考价值。

**「可关注」** 可关注：Codex 后续在代码构建、理解、审查维度的工具更新，以及收购完成后相关能力的集成节奏。

**标签**: `#lab`, `#industry`, `#product`

---

<a id="item-ai-daily-3"></a>
### [Claude Marketplace 新增 25+ 合作伙伴工具](https://claude.com/resources/articles/new-agents-and-products-claude-marketplace) ⭐️ 7.8/10

Anthropic 向 Claude Marketplace 新增覆盖安全、开发基础设施、创意、生产力场景的代理与产品，目前合作伙伴总数超过 25 家。符合条件的企业客户可将部分已承诺的 Anthropic 支出用于抵扣这些第三方工具的购买费用，无需额外新增预算即可扩展 Claude 生态内的工具使用范围。

rss · Claude Blog · 11月4日 00:00

**「为什么重要」** 这降低了企业客户在 Claude 生态内采购第三方工具的决策成本，同时通过承诺支出的跨产品抵扣规则，提升了 Anthropic 企业客户的预算使用灵活性。

**「可关注」** 可关注：Claude Marketplace 已覆盖安全审计、开发部署、创意生产、项目管理等场景的第三方工具，企业客户可通过已承诺的 Anthropic 支出直接采购。

**标签**: `#lab`, `#product`, `#industry`

---