---
layout: default
title: "Horizon Summary: 2026-11-05 (EN)"
date: 2026-11-05
lang: en
---

> From 213 items, 16 important content pieces were selected

---

**Agent Harness Architecture**
1. [@mastra/core 1.82.0 发布](#item-harness-arch-1) ⭐️ 8.8/10
2. [pydantic-ai v2.66.0 安全修复发布](#item-harness-arch-2) ⭐️ 7.8/10
3. [Gemini CLI v0.67.0 发布](#item-harness-arch-3) ⭐️ 7.8/10

**AI Agent Engineer**
1. [Anthropic 可证明推理研究更新](#item-agent-engineer-1) ⭐️ 8.0/10
2. [Cognition 发布 SWE-2 Flash 模型](#item-agent-engineer-2) ⭐️ 7.8/10
3. [Axion 1.0 开源智能体基础模型发布](#item-agent-engineer-3) ⭐️ 7.0/10
4. [ToolSpace 提出工具中心框架](#item-agent-engineer-4) ⭐️ 7.0/10
5. [WebHarbor 153 Docker化Web环境发布](#item-agent-engineer-5) ⭐️ 7.0/10
6. [datasette-apps 0.3a0 发布](#item-agent-engineer-6) ⭐️ 6.8/10
7. [Dharma Field Extractor 2B 参数模型发布](#item-agent-engineer-7) ⭐️ 6.3/10
8. [Kimi K3.1 Pro 开源权重发布](#item-agent-engineer-8) ⭐️ 6.0/10
9. [datasette-agent 0.5a0 发布](#item-agent-engineer-9) ⭐️ 6.0/10
10. [RoboColosseum 论文提出具身智能评估框架](#item-agent-engineer-10) ⭐️ 6.0/10

**AI Daily**
1. [OpenAI 管道在 Linux 内核发现 948 个提权漏洞](#item-ai-daily-1) ⭐️ 8.8/10
2. [OpenAI 将收购 Pierre Computer Company](#item-ai-daily-2) ⭐️ 7.8/10
3. [Claude Marketplace 合作方突破25家](#item-ai-daily-3) ⭐️ 7.8/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [@mastra/core 1.82.0 发布](https://github.com/mastra-ai/mastra/releases/tag/%40mastra/core%401.82.0) ⭐️ 8.8/10

Mastra 发布 @mastra/core@1.82.0，核心升级 Knowledge v2。新 page-tree 内存模型把知识组织成 pages/notes/pins，配套 \`knowledge\_list\`、\`knowledge\_read\` 行/段/grep 读取、列表钉选和 \`\[\[links\]\]\` 链接索引；服务端新增 \`knowledge.upsertPage\(\)\`、\`removePage\(\)\` 同步接口，支持向量/混合检索和长页分块嵌入。只读 Knowledge HTTP/JS 客户端 API 通过 SSE 流暴露树/页/图/搜索/活动端点，且带 FGA 作用域门控。Evented durable agent 修复 API 关闭时 worker 停止问题，需配合 \`PostgresStore\` 等支持 fencing 的共享存储实现跨进程连续性；后台任务支持挂起后重载恢复，MCP 增加从聊天接收任务输入的行为。

github · PaulieScanlon · Nov 4, 10:59

**「设计要点」** Knowledge v2 采用 page-tree 作为内存子系统主结构，服务端通过 FGA 作用域门控的只读路由暴露数据，客户端用 SSE 流同步变更。Durable agent 跨进程连续性依赖 fencing 共享存储（如 \`@mastra/pg\` 的 \`PostgresStore\`）和共享 pubsub，单进程部署不受影响。

**「改了什么」** Knowledge 从旧内存模型迁移到 page-tree 结构，\`knowledge.reindex\(\)\` 移除，改用 \`upsertPage\`/note 写入和 \`reindexLinks\(\)\`。\`@mastra/temporal@0.5.0\` 开始校验步骤 \`inputSchema\` 和 \`requestContextSchema\`，\`@mastra/factory@0.27.0\` 移除 work-item claiming API。Evented durable agent 在 API 关闭时保持 worker 运行，后台任务增加重载后恢复能力。

**Tags**: `#memory`, `#tools`, `#permissions`

---

<a id="item-harness-arch-2"></a>
### [pydantic-ai v2.66.0 安全修复发布](https://github.com/pydantic/pydantic-ai/releases/tag/v2.66.0) ⭐️ 7.8/10

pydantic-ai v2.66.0 修复 2 个高危安全漏洞：web\_fetch\_tool 本地回退在处理深度嵌套 JSON 时因重缩进导致内存耗尽（GHSA-m5vj-8mcw-82qx）；harness secret redaction 的 private\_key 模式存在正则指数回溯（GHSA-mfx5-pc32-32m8）。同步修复 5 个中危和 1 个低危漏洞，涉及云元数据访问、OpenTelemetry 凭据泄露、tool schema 展开攻击面等。新增 OpenSandbox、RenderSandbox、Azure Durable Tasks 及 Pixeltable 集成。

github · adtyavrdhn · Nov 4, 11:51

**「设计要点」** 事件循环上多个路径存在资源耗尽风险：web\_fetch\_tool 在限制检查前重缩进 JSON、tool schema 的 $defs/$ref 内联展开、decision model 重复解析 $ref、Vercel AI/AG-UI 适配器加载消息的平方级复杂度。secret redaction 使用易受攻击的正则表达式，OpenTelemetry embedding spans 记录敏感头信息。

**「改了什么」** 修复 web\_fetch\_tool 本地回退的内存耗尽漏洞，将 JSON 重缩进移至下载大小限制之后。修复 harness secret redaction 中 private\_key 模式的正则指数回溯。Anthropic 20260209 web tools 直接调用 API 支持引用；FunctionToolset\(requires\_approval=True\) 可应用于 Tool 实例；realtime session instructions 每轮重新解析并以追加形式交付；SummarizingCompaction\(keep\_user\_messages=True\) 仅通过文本标记识别副本。新增 OpenSandbox、RenderSandbox 自托管工作空间，pydantic\_ai\_harness 支持 Azure Durable Tasks 和 Pixeltable 工具/内存存储。MCP 能力新增 include\_instructions 参数。

**「评论」** 无可用社区评论。

**Tags**: `#tools`, `#permissions`, `#runtime`

---

<a id="item-harness-arch-3"></a>
### [Gemini CLI v0.67.0 发布](https://github.com/google-gemini/gemini-cli/releases/tag/v0.67.0) ⭐️ 7.8/10

Gemini CLI v0.67.0 发布。核心新增 IDE companion 通过 exec stdio 桥接容器沙箱（PR \#29858）。权限修复将不可信 flag 检查限定于外部输出，并记忆用户已批准 flag（PR \#29833）。同期修复 agent 重复加载、IDE 上下文过滤、A2A 路由顺序、原子写入遵守只读文件与硬链接、token 元数据保留、thought signatures 传递、非交互模式取消处理、模型发现命令等十余项问题。

github · gemini-cli-robot · Nov 4, 20:27

**「设计要点」** IDE companion 通过 exec stdio 直连容器沙箱，改变工具执行边界。权限系统将不可信 flag 检查收缩至外部输出，并持久化用户批准记录，降低重复授权成本。

**「改了什么」** 相对 v0.66.0，新增 IDE companion 容器沙箱 exec stdio 桥接及 models 模型发现命令。修复覆盖不可信 flag 权限范围、工作区为主目录时的重复 agent 加载、IDE 设置文件上下文排除、A2A 路由注册顺序、RFC 9110 token 分割、只读文件原子写入、扩展 token 元数据保留、thought signatures 传递、非交互模式终止信号处理等。

**Tags**: `#sandbox`, `#permissions`, `#runtime`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [Anthropic 可证明推理研究更新](https://www.anthropic.com/research/provable-inference) ⭐️ 8.0/10

Anthropic 于 2026-11-04 发布可证明推理研究，提出基于零知识证明的方案，使客户端可密码学验证特定 LLM 生成给定输出。方案当前指标为 90-100 倍计算开销、17 秒证明验证、6.5MB 承诺大小，每份承诺覆盖约 1600 万次请求。高计算开销目前限制生产部署可行性。社区出现归属争议，指该工作基于 VerInf 项目且署名不足。

hackernews · ltononro · Nov 4, 17:17 · [Discussion](https://news.ycombinator.com/item?id=50368626)

**「为什么重要」** 该技术为 agent harness 中的模型输出可验证性提供密码学路径，但 90-100x 开销与归属争议使当前更接近研究原型而非生产工具。

**「可关注」** 可关注：闭源模型提供者的可证明推理需承受 90-100x 计算开销，而开源模型可通过确定性重跑以更低成本实现类似验证，两种路径成本差异显著。

**「评论」** 社区出现归属争议，VerInf 原作者指控 Anthropic 未充分署名。技术讨论认为闭源模型可证明推理成本高于开源模型重跑，且 90-100x 开销高于四家独立提供者概率证明成本；另有用户指出该技术可检测 OpenRouter 等路由的模型替换。

**Tags**: `#observability`, `#eval`, `#permissions`, `#harness`

---

<a id="item-agent-engineer-2"></a>
### [Cognition 发布 SWE-2 Flash 模型](https://cognition.ai/blog/swe-2-flash) ⭐️ 7.8/10

2026年11月4日，Cognition官方发布全美产编码模型SWE-2 Flash。该模型基于Inkling-Small（276B总参数/12B激活参数）训练，首次在强化学习前新增中间训练阶段，Terminal-Bench 4.0得分从基线的0.9%提升至20.0%，FrontierCode 2.0从3.2%提升至24.0%，网络安全相关评测ExploitBench得分从11.3%提升至34.8%，性能超过所有美国开源权重编码模型，包括体积大3倍的模型。模型现已上线Devin Desktop与CLI，价格为更大同系列模型SWE-2的五分之一，速度为3倍；权重暂不公开，计划未来几周内向行业伙伴与研究机构推出受控共享计划。

rss · Cognition Blog · Nov 4, 18:00

**「为什么重要」** 该模型首次验证了强化学习前中间训练阶段对编码模型性能的提升效果，且小参数模型在成本、速度与能力上已具备替代更大模型处理软件代理日常工作的潜力；其后续受控权重共享计划对行业开源生态与敏感场景部署的影响尚未明确。

**「可关注」** 可关注：编码模型训练中，强化学习前中间训练的数据混合策略、以及强化学习任务的多样性与质量，对小参数模型的评测增益有显著影响。

**Tags**: `#coding-agent`, `#eval`

---

<a id="item-agent-engineer-3"></a>
### [Axion 1.0 开源智能体基础模型发布](https://huggingface.co/papers/2611.03233) ⭐️ 7.0/10

Hugging Face Daily Papers 2026年11月4日收录arXiv预印本，介绍Axion 1.0，一款完全开源的智能体基础模型，具备较强的智能体能力，当前在HF日报获得39次点赞。其训练采用简化3阶段流程：两个轻量监督微调阶段加强化学习，未使用中间训练、直接偏好优化（DPO）或在线策略蒸馏（OPD）等技术。第一阶段通过模型感知数据构造，合成挑战性问题并根据基座模型自身的成功解题策略进行对抗增强，培养自包含推理能力；第二阶段通过可扩展流水线构造多样、自动可验证的真实世界工具依赖任务，扩展工具推理能力。当前公开内容缺少性能评估结果与完整技术规格，标签为coding-agent。

rss · Hugging Face Daily Papers · Nov 4, 00:00

**「为什么重要」** 它提出了无需DPO/OPD的简化智能体训练范式，创新的模型感知数据构造与自动可验证工具任务生成方法可降低智能体模型训练开发门槛，但当前仅为预印本，性能评估结果尚未公开，实际效果待验证。

**「可关注」** 可关注其无DPO/OPD的3阶段训练流程，以及模型感知的数据构造方法、自动可验证工具依赖任务生成流水线的具体实现细节。

**Tags**: `#coding-agent`

---

<a id="item-agent-engineer-4"></a>
### [ToolSpace 提出工具中心框架](https://huggingface.co/papers/2611.05036) ⭐️ 7.0/10

2026-11-04，Hugging Face Daily Papers 收录论文《ToolSpace: Scaling Tool-Centric Environment Synthesis for Long-Horizon Agents》。该论文提出工具中心框架 ToolSpace，逆转现有数据为中心的环境缩放流程。ToolSpace 从真实 MCP 服务执行迹和开放代理语料中，用确定性规则挖掘工具组合依赖，构建加权工具组合图并聚类为环境。该方法解决现有方法中工具接口不匹配真实服务、组合缺乏执行 grounding、任务跨环境能力弱等痛点，对 MCP 代理评测环境构建和 Harness 开发有直接参考价值。

rss · Hugging Face Daily Papers · Nov 4, 00:00

**「为什么重要」** 现有 MCP 环境缩放方法普遍存在工具接口失真和组合缺乏执行 grounding 的问题，ToolSpace 提供了一种可验证的替代路径。对构建长周期代理评测基准的工程师而言，其确定性规则挖掘和跨环境任务生成思路可直接复用。

**「可关注」** 可关注：ToolSpace 用确定性规则替代 LLM 判断来挖掘工具依赖，可能降低环境合成的不确定性。

**Tags**: `#mcp`, `#eval`, `#harness`

---

<a id="item-agent-engineer-5"></a>
### [WebHarbor 153 Docker化Web环境发布](https://huggingface.co/papers/2611.03634) ⭐️ 7.0/10

On November 4, 2026, a paper indexed by Hugging Face Daily Papers proposes WebHarbor, a suite of 153 deterministic dockerized real-world web environments for GUI web agent training and evaluation. The suite is built via task-driven human-agent collaboration, faithfully reconstructing visual interfaces, content, and functional workflows of real web services under deterministic control. It addresses pain points of live website evaluation such as changing content, access restrictions, and limited coverage of authenticated workflows, as well as low functional depth and visual fidelity of existing synthetic environments.

rss · Hugging Face Daily Papers · Nov 4, 00:00

**「为什么重要」** Current GUI web agent training and evaluation lack stable, high-fidelity unified environment benchmarks. WebHarbor&\#x27;s reproducibility can reduce evaluation result volatility, providing a controlled benchmark for cross-agent capability comparison.

**「可关注」** 可关注：WebHarbor&\#x27;s deterministic containerized implementation can be directly integrated into existing GUI agent evaluation harnesses, replacing volatile live websites or low-fidelity synthetic environments to reduce evaluation noise.

**Tags**: `#eval`, `#coding-agent`, `#harness`

---

<a id="item-agent-engineer-6"></a>
### [datasette-apps 0.3a0 发布](https://github.com/datasette/datasette-apps/releases/tag/0.3a0) ⭐️ 6.8/10

2026年11月4日，simonw发布datasette-apps 0.3a0 alpha版本，核心优化Datasette Agent创建与编辑自定义HTML应用的集成体验。本次更新新增\`app\_add\_stored\_queries\(\)\`、\`app\_remove\_stored\_queries\(\)\`两个agent工具，用于管理应用可调用的存储查询，授予写查询需用户提前审批；\`app\_create\(\)\`新增前置校验，确认请求的存储查询存在且用户有查看权限，创建前也会要求用户批准写查询。此外，Datasette Agent内支持通过\`\#\`自动补全有权限的应用，应用工具结果新增相对路径字段，应用查看按钮与\`\#\`引用链接现在会在Agent面板全屏打开。该版本最低要求Datasette 1.0a41及以上，支持Python 3.15，已移除Python 3.10支持，影响使用Datasette Agent构建datasette-apps的用户及关注agent权限设计的工程师。

github · simonw · Nov 4, 00:29

**「为什么重要」** 该版本将agent权限校验、用户审批流程嵌入应用管理的具体工具链，为同类agent工具的权限设计提供了窄场景参考，但当前仍处于alpha阶段，仅适用于Datasette生态内的使用场景，适用范围有限。

**「可关注」** 可关注：agent工具对写操作采用前置权限校验+用户审批的流程设计，以及通过返回相对路径替代自生成URL的链接可靠性做法。

**Tags**: `#agent`, `#permissions`, `#datasette`

---

<a id="item-agent-engineer-7"></a>
### [Dharma Field Extractor 2B 参数模型发布](https://huggingface.co/blog/Dharma-AI/dharma-field-extractor) ⭐️ 6.3/10

Hugging Face 官方博客 2026-11-04 发布 Dharma Field Extractor，这是一个 20 亿参数的文档字段提取模型，基座为 DharmaOCR-LITE v1.1，经 LoRA 适配器微调后支持开放提取、schema 定向两种模式，输出结构化 JSON。博客给出的自研 benchmark（覆盖 546 份文档、三类场景共 1638 个提取案例）显示，该模型字段级 F1 得分为 0.834，高于测试的四个前沿 LLM 配置（最高为 Claude Opus 5 的 0.816）；博客测算其单 L40S 自托管成本比对比的 frontier API 低 6 至 147 倍。该模型主要面向需要批量处理发票、表单、ID 等文档结构化字段提取的 agent 工具链开发者。

rss · Hugging Face Blog · Nov 4, 17:50

**「为什么重要」** 该模型针对文档字段提取垂直场景专项优化，为 agent 工具链提供了比通用 frontier API 成本更低的潜在替代选项，但目前仅公开博客与试用入口，未开放论文、模型权重或第三方评测结果，影响面局限于文档处理相关场景，未涉及通用 agent 架构或评测框架的突破。

**「可关注」** 可关注：若你的 agent 工具链存在高并发的结构化文档字段提取需求，可后续跟进该模型的权重公开情况、跨场景泛化能力及实际部署适配成本。

**Tags**: `#toolchain`, `#eval`, `#orchestration`

---

<a id="item-agent-engineer-8"></a>
### [Kimi K3.1 Pro 开源权重发布](https://huggingface.co/moonshotai/Kimi-K3.1-Pro) ⭐️ 6.0/10

2026-11-04，Moonshot AI 在 Hugging Face 发布 Kimi K3.1 Pro 开源模型权重（moonshotai/Kimi-K3.1-Pro）。该 image-text-to-text 模型发布当日 trendingScore 达 453、获赞 461 次，社区反馈存在分歧：有用户认为其跑分未显著超越 DeepSeekV4.1-Flash 且疑似 benchmaxxed，也有实测者评价其为略低于前沿但足够实用的强开源模型。硬件门槛：社区估算全精度运行需约 8 台 B300 节点；OpenRouter、Together、Modal 等第三方推理服务已开始托管，据观察 Together 吞吐量约为官方端点的两倍，Modal 约为四倍。官方技术规格未在材料中披露。

hackernews · Hugging Face Trending Models · Nov 4, 15:30 · [Discussion](https://news.ycombinator.com/item?id=50366999)

**「为什么重要」** 该模型为 coding-agent 评估提供了新的开源选项，但其实际采用取决于推理成本优化进展及在代理任务中的真实表现验证。

**「可关注」** 可关注：第三方推理服务商已提供显著高于官方端点的吞吐量，暗示该模型在推理优化层面仍有压缩空间。

**「评论」** 社区对 K3.1 Pro 的性能定位存在分歧：部分用户认为其跑分表现一般、存在 benchmaxxed 嫌疑，另一些实测者则认为其作为开源模型已足够强劲；同时普遍指出全精度运行硬件门槛极高（约 8 台 B300），而量化部署方案仍在探索中。

**Tags**: `#coding-agent`, `#eval`, `#harness`

---

<a id="item-agent-engineer-9"></a>
### [datasette-agent 0.5a0 发布](https://simonwillison.net/2026/Nov/3/datasette-agent/) ⭐️ 6.0/10

Simon Willison于2026年11月3日发布datasette-agent 0.5a0，核心新增panel功能，支持agent聊天窗口与Datasette数据库页面（如数据表、查询页）并排显示。结合datasette-apps可通过对话创建、修改数据库驱动的应用，当前可通过GitHub账号登录agent.datasette.io试用该功能。

rss · Simon Willison · Nov 3, 23:13

**「为什么重要」** 该发布为数据库场景的agent交互提供了并排工作流的新范式，对数据库类agent工具、数据应用生成方向的工程师有参考价值，但并非所有agent工程师的必读内容；当前工具定位小众，尚未对主流agent框架生态产生明确影响。

**「可关注」** 可关注：数据库-backed应用的agent交互可采用页面与聊天侧边并排的布局，减少页面切换操作。

**Tags**: `#coding-agent`, `#harness`, `#orchestration`, `#observability`

---

<a id="item-agent-engineer-10"></a>
### [RoboColosseum 论文提出具身智能评估框架](https://huggingface.co/papers/2611.02497) ⭐️ 6.0/10

Hugging Face Daily Papers 于 2026-11-04 介绍 RoboColosseum 研究论文。该框架提供分布式评估基础设施，通过统一策略服务与标准化协议，在四种机器人 embodiment（SO-101、Franka、Bimanual-YAM、G1 Humanoid）上评估视觉-语言-动作（VLA）策略与前沿 AI 智能体。研究测试五个 VLA 策略与三个 frontier AI agents，设置 Open Track（无任务特定适应的盲法 pairwise 对比）与 Fine-tune Track（跨 20 个任务与四种 embodiment 的适应能力测量）。影响范围限于具身智能研究社区，具体性能数据未在提供材料中披露。

rss · Hugging Face Daily Papers · Nov 4, 00:00

**「为什么重要」** 该框架试图解决物理试验可复现性差的痛点，通过标准化协议与跨机器人统一接口降低评估门槛。对构建 coding agent 与 harness 的工程师而言，其 orchestration 设计（本地机器人网络 + 统一策略服务）提供了可参考的分布式评估模式，但实际效果与易用性仍需后续实证。

**「可关注」** 可关注：RoboColosseum 将策略 serving 与评估协议解耦，并在异构机器人网络上运行，这种架构对设计多环境、多 embodiment 的 agent 评估 harness 有参考价值。

**Tags**: `#eval`, `#harness`, `#orchestration`

---

## AI Daily

<a id="item-ai-daily-1"></a>
### [OpenAI 管道在 Linux 内核发现 948 个提权漏洞](https://openai.com/index/a-thousand-fewer-paths-to-root) ⭐️ 8.8/10

OpenAI 发布自主漏洞修复管道，在 Linux 内核中发现 948 个本地权限提升漏洞。该管道自动完成漏洞发现、验证及补丁生成全流程。目前未披露补丁是否已合并至主线内核或实际部署。

rss · OpenAI Blog · Nov 4, 08:00

**「为什么重要」** 这是 OpenAI 首次公开披露其自主漏洞修复管道在真实大型代码库中的运行结果。948 个漏洞的规模显示该流程已具备处理复杂系统级代码的能力。

**「可关注」** 可关注：自主漏洞修复管道在 Linux 内核这一大型 C 代码库中完成从发现到补丁生成的端到端自动化。

**Tags**: `#lab`, `#industry`, `#product`

---

<a id="item-ai-daily-2"></a>
### [OpenAI 将收购 Pierre Computer Company](https://openai.com/index/openai-to-acquire-pierre) ⭐️ 7.8/10

OpenAI 官方宣布将收购 Pierre Computer Company，核心目标是扩展 Codex 产品的代码构建、理解与审查相关工具能力。当前公告未披露收购金额、交割时间等具体细节。

rss · OpenAI Blog · Nov 4, 14:30

**「为什么重要」** Codex 是 OpenAI 面向代码开发场景的核心产品，此次收购直接补强其代码工具链能力，可能影响后续 coding agent 与代码审查工具的功能边界。

**「可关注」** 可关注：Codex 后续在代码构建、理解、审查维度的工具迭代与整合进展。

**Tags**: `#lab`, `#industry`, `#product`

---

<a id="item-ai-daily-3"></a>
### [Claude Marketplace 合作方突破25家](https://claude.com/resources/articles/new-agents-and-products-claude-marketplace) ⭐️ 7.8/10

Anthropic 向 Claude Marketplace 新增覆盖安全、开发基础设施、创意、生产力场景的代理与产品，合作方总数超过 25 家。符合条件的企业客户可将部分已承诺的 Anthropic 消费额度用于购买这些第三方工具，实现同一笔承诺消费覆盖 Claude 及合作产品。新增工具包括 Chainguard、Checkmarx、Datadog、Runway、Asana 等，分别对应代码漏洞修复、代理可观测性、音视频生成、项目管理等具体能力。

rss · Claude Blog · Nov 4, 00:00

**「为什么重要」** 这降低了企业采购 Claude 生态相关工具的决策与预算成本，同时通过承诺消费的灵活使用提升了预算效率，也标志着 Anthropic 在 Claude 生态上的合作布局进一步扩大。

**「可关注」** 可关注：企业用户可将已承诺的 Anthropic 消费额度用于 Claude Marketplace 内的第三方合作工具，无需单独申请采购预算。

**Tags**: `#lab`, `#product`, `#industry`

---