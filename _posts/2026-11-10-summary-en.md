---
layout: default
title: "Horizon Summary: 2026-11-10 (EN)"
date: 2026-11-10
lang: en
---

> From 195 items, 17 important content pieces were selected

---

**Agent Harness Architecture**
1. [browser-use 1.0.0rc2 发布](#item-harness-arch-1) ⭐️ 9.8/10
2. [browser-use 1.0.0 发布](#item-harness-arch-2) ⭐️ 7.8/10
3. [FastMCP v4.2.0a4 发布](#item-harness-arch-3) ⭐️ 7.8/10

**AI Agent Engineer**
1. [HOPE 高阶专家剪枝方法发布](#item-agent-engineer-1) ⭐️ 7.8/10
2. [Claude Fable 5.2 与 Mythos 5.2 发布](#item-agent-engineer-2) ⭐️ 7.0/10
3. [Google 发布 TPU 8tx 与 8i Max](#item-agent-engineer-3) ⭐️ 7.0/10
4. [ReproBridge 提出 ML 复现智能体工作流](#item-agent-engineer-4) ⭐️ 7.0/10
5. [Agent Harness 自演化：隐藏权衡](#item-agent-engineer-5) ⭐️ 7.0/10
6. [Nemotron-Personas-Finance-Japan 发布](#item-agent-engineer-6) ⭐️ 6.3/10
7. [llm-anthropic 0.31 支持 Fable 5.2 与 Mythos 5.2](#item-agent-engineer-7) ⭐️ 6.0/10
8. [Flide 提出决策推理精确分叉引擎](#item-agent-engineer-8) ⭐️ 6.0/10
9. [PCBRouteAgent 论文提出工具代理编排模式](#item-agent-engineer-9) ⭐️ 6.0/10

**AI Daily**
1. [ChatGPT Enterprise 上线 AWS Marketplace](#item-ai-daily-1) ⭐️ 7.8/10
2. [OpenAI Control Room 上线](#item-ai-daily-2) ⭐️ 7.8/10
3. [CodeRabbit 基于 Codex 交付量提升 20 倍](#item-ai-daily-3) ⭐️ 6.8/10
4. [OpenAI API 加速 Kuken 图纸检索](#item-ai-daily-4) ⭐️ 6.8/10
5. [Claude Fable 5.2 体验与 Jagged AGI 讨论](#item-ai-daily-5) ⭐️ 5.5/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [browser-use 1.0.0rc2 发布](https://github.com/browser-use/browser-use/releases/tag/1.0.0rc2) ⭐️ 9.8/10

browser-use 1.0.0rc2 将 agent 引擎从“DOM dump → 逐步选动作”改为持久化 Python REPL，基于 browser-harness 和 raw CDP 运行在 Pydantic AI 上。代码库从 68,815 行压缩至 13,154 行，削减约 80%，同时保留 0.x 的 Agent、Browser、Tools、run\(\)、final\_result\(\) 表面接口。默认行为变更：浏览器改为 Browser Use Cloud，默认模型为 bu-fast，模式为 ultrafast，run\(\) 默认 max\_steps=100（原 500）。需显式安装预发布版本，普通 pip install browser-use 仍安装 0.13.14。

github · gregpr07 · Nov 9, 16:52

**「设计要点」** agent 在持久化 REPL 中直接编写 Python 代码调用 browser-harness 助手和 CDP，替代原有每步从 DOM 快照选择动作的循环。运行时底层切换至 Pydantic AI，配置校验在浏览器启动和计费前完成，运行时错误统一通过 result.error 返回，不再静默忽略。

**「改了什么」** 默认浏览器切至云端，本地或 localhost 任务需显式指定 Browser\(&\#x27;chromium&\#x27;\)。新增结构化输出 output\_model\_schema、文件上传下载、sensitive\_data 密钥脱敏、域名黑白名单、联网搜索。CLI 入口统一为 browser-use，移除 bu/browser 脚本和 browser-use init。流式响应最长支持 930 秒，增加一次瞬态重试，上下文溢出时自动压缩一次。

**Tags**: `#runtime`, `#tools`, `#mcp`, `#planning`

---

<a id="item-harness-arch-2"></a>
### [browser-use 1.0.0 发布](https://github.com/browser-use/browser-use/releases/tag/1.0.0) ⭐️ 7.8/10

browser-use 发布 1.0.0。项目重写运行时，改为基于 Chrome DevTools Protocol 的持久化 Python REPL，删除 DOM 序列化、action schema 等中间抽象层，代码量减少 80%（136,866 行）。模型直接编写 Python 代码调用 \`bu\` 命名空间 API 操作浏览器，官方宣称得分高 33 点、成本降 2.7–5.2 倍、速度快 2–3 倍。默认切换为 Browser Use Cloud 托管浏览器与 \`bu-fast\` 模型，\`max\_steps\` 默认从 500 降至 100，超时 1700 秒。

github · gregpr07 · Nov 10, 02:04

**「设计要点」** 运行时简化为单层：模型输出 Python 代码，经持久化 REPL 直连 CDP 执行，结果回传模型。中间层全部移除，工具调用不再经过 DOM 序列化或 schema 校验。默认走 Browser Use Cloud 网关，本地浏览器需显式指定 \`Browser\(&\#x27;chromium&\#x27;\)\`。

**「改了什么」** 相对 0.x，运行时从多抽象层重写为 CDP + Python REPL 单层架构并删除 80% 代码，默认模型、浏览器、认证全部切换为 Browser Use Cloud 托管服务，原 0.x 配置项不兼容并直接报错。新增结构化输出、文件上传下载、敏感数据脱敏、域名限制、web search 与 Docker 镜像，\`max\_steps\` 默认从 500 降至 100。

**Tags**: `#runtime`, `#tools`

---

<a id="item-harness-arch-3"></a>
### [FastMCP v4.2.0a4 发布](https://github.com/PrefectHQ/fastmcp/releases/tag/v4.2.0a4) ⭐️ 7.8/10

FastMCP 4.2.0a4 是 PrefectHQ 发布的 MCP 服务器框架 alpha 预演版本，最低 Python 版本要求提升至 3.11。本次更新核心新增 Annotated 依赖注入支持，允许 Depends\(...\) 与 CurrentContext\(\) 等依赖以 Annotated 元数据形式声明，并统一作用于 tools、resources 和 prompts。修复了技能发现逻辑，避免将嵌套的 SKILL.md 误列为独立技能，同时补上了 OAuth 相关依赖（joserfc、Authlib）的安全漏洞，以及 OpenAPI 请求体、多选 elicitation 架构、文档字符串解析等核心缺陷。技能支持仍标记为实验性，仅建议用于集成测试。

github · zzstoatzz · Nov 10, 01:59

**「改了什么」** 相对上一 alpha，Skill 对象重构为存储中立，技能发现扩展至挂载服务器与代理链路，并新增 Client.read\_skill 与 fastmcp list --skills 接口；依赖系统原生支持 Annotated 元数据，Depends 与 CurrentContext 可直接标注在类型上。安全修复覆盖 Authlib/joserfc 版本下限、重定向 URI 浏览器级规范化、技能 frontmatter 校验及目录读取限额，同时修正 OpenAPI 请求体、多选 elicitation 架构、文档字符串解析等回归缺陷。

**Tags**: `#mcp`, `#tools`, `#permissions`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [HOPE 高阶专家剪枝方法发布](https://huggingface.co/blog/amazon/higher-order-pruning-experts) ⭐️ 7.8/10

2026年11月9日Hugging Face官方博客发布HOPE（高阶专家剪枝）方法，针对MoE模型推理时全部专家MLP驻留内存、多数专家闲置的问题，通过建模专家 pairwise 交互作用优化剪枝决策。该方法在Qwen3.5-122B、Qwen3.5-35B、GLM-4.5-Air三个模型、10%-50%剪枝率范围内测试，相比REAP、MAN等4种一阶基线方法取得最优平均排名（2.07/5），在agentic coding任务上比次优方法最高提升6.1%。当前验证仅覆盖代码类任务场景，对更大规模MoE模型、非代码类任务的适配效果尚未给出结论，主要面向MoE模型推理优化、Agent部署选型的工程师群体。

rss · Hugging Face Blog · Nov 9, 12:34

**「为什么重要」** 已发生的部分是HOPE突破了传统一阶专家剪枝忽略专家协作关系的瓶颈，在激进剪枝率下仍能保持模型性能；尚未证实的影响是该方法的通用性，目前仅验证了代码类agentic任务，其他场景的收益需要进一步实测。

**「可关注」** 可关注：HOPE的F矩阵对角线可完美复现REAP等一阶方法的专家重要性排序，其性能增益完全来自 off-diagonal 项捕获的专家 pairwise 交互，现有MoE推理优化流程可复用原有校准环节验证剪枝收益，额外开销仅为每层1-2秒的二次规划求解时间。

**Tags**: `#memory`, `#moe`, `#pruning`, `#optimization`, `#architecture`

---

<a id="item-agent-engineer-2"></a>
### [Claude Fable 5.2 与 Mythos 5.2 发布](https://www.anthropic.com/claude-fable-and-mythos-5-2) ⭐️ 7.0/10

Anthropic 于 2026-11-09 发布 Claude Fable 5.2 与 Mythos 5.2。Hacker News 帖子链接官方公告，社区用户报告 Fable 5.2 在 60 万行 Fortran 代码库上实现 36 倍加速，另有用户称其与 Opus 5.5 在普通编码任务上差异有限。当前无官方技术规格或完整基准数据可引用，社区对基准测试方法论亦存疑问。

hackernews · lairv · Nov 9, 18:01 · [Discussion](https://news.ycombinator.com/item?id=50429068)

**「为什么重要」** 对 coding agent 开发者，Fable 5.2 若在大型遗留代码库上保持强推理能力，可能影响模型选型。但社区报告未经官方验证，实际效果待观察。

**「可关注」** 可关注：Fable 5.2 在超大型代码库上的实际任务完成率，以及 5.2 与 5.5 的命名差异是否反映 Anthropic 的产品分层策略。

**「评论」** 社区报告呈现两极：有用户称 Fable 5.2 在 60 万行 Fortran 代码库上实现 36 倍加速，另有引用称其 agent 集群用 30 小时完成费马大定理形式化；但部分用户认为其与 Opus 5.5 在普通编码任务上差异有限。另有评论者对官方基准测试的模型对位选择提出质疑。

**Tags**: `#coding-agent`, `#eval`

---

<a id="item-agent-engineer-3"></a>
### [Google 发布 TPU 8tx 与 8i Max](https://blog.google/innovation-and-ai/infrastructure-and-cloud/global-network/tpu-8i-max-and-8tx/) ⭐️ 7.0/10

2026年11月9日Google官方发布专为智能体工作负载优化的TPU 8tx与8i Max两款新芯片，相关公告首发于Google博客，HackerNews社区同步讨论。社区反馈指出底层TPUSync技术已被开源智能体工具（如适配Qwen系列的Strata项目）采用，同时有用户提到Colab平台目前最高仅支持v6e-1 TPU，尚未上线新款型号，公告未披露具体性能、功耗、成本及与NVIDIA竞品的对比数据。

hackernews · \_benx\_ · Nov 9, 21:56 · [Discussion](https://news.ycombinator.com/item?id=50432831)

**「为什么重要」** 这是Google首次推出专为智能体场景优化的TPU产品线，其底层TPUSync技术已被开源智能体工具链采用，直接影响AI Agent工程师的基础设施与部署工具链选型。但当前公告未公开具体性能、成本及竞品对比数据，实际落地价值仍需后续参数披露验证。

**「可关注」** 可关注：TPUSync技术已被开源智能体工具链采用，新款TPU的Colab支持进度与公开性能/成本参数将直接影响工具链选型决策。

**「评论」** 社区讨论聚焦四个方向：一是确认TPUSync技术已被Strata等开源Qwen系列工具采用，推荐相关技术博客；二是呼吁Google Colab尽快上线新款TPU，现有v6e-1算力不足以支撑严肃开发；三是要求公开新款TPU的功耗、成本及与NVIDIA竞品的对比数据，目前官方尚未回应；四是有用户询问Google为何不直接销售新款TPU，暂无官方答复。

**Tags**: `#coding-agent`, `#inference`, `#cloud-infrastructure`, `#toolchain`

---

<a id="item-agent-engineer-4"></a>
### [ReproBridge 提出 ML 复现智能体工作流](https://huggingface.co/papers/2611.08452) ⭐️ 7.0/10

Hugging Face Daily Papers 于 2026 年 11 月 10 日介绍 ReproBridge，一种用于构建标准化可复现 ML 研究工件的智能体工作流，以及配套的 ReproBridge-Bench 基准。该基准包含 1,029 个任务，覆盖 36 篇论文的 387 个实验，每个任务提供 5 项人工验证的参考分数。ReproBridge 研究保留恢复的实验流程与决策是否有助于提升后续独立复现成功率。此成果面向构建智能体评测或研究型编码智能体工作流的团队，但属于研究输出，非生产工具变更。

rss · Hugging Face Daily Papers · Nov 10, 00:00

**「为什么重要」** 该基准提供大规模、人工验证的复现任务集，为评估智能体在真实 ML 实验复现中的能力提供了可量化参照。目前此类资源稀缺，尤其缺少带人类验证参考分数的规模化评测。

**「可关注」** 可关注：ReproBridge 将复现过程结构化为标准化工件（精炼代码库、环境配置、实验启动器、复现指南），其任务设计可参考用于构建编码智能体的评测场景。

**Tags**: `#eval`, `#orchestration`, `#coding-agent`

---

<a id="item-agent-engineer-5"></a>
### [Agent Harness 自演化：隐藏权衡](https://huggingface.co/papers/2611.07624) ⭐️ 7.0/10

该论文（2026-11-10，arXiv:2611.07624）实证检验无模型权重更新的 Agent Harness 递归自演化（RSI）。实验对 4 种方法、16 个演化后 Agent 在通用与编码任务上评估，发现所有 Agent 均获得新任务覆盖同时丢失原有覆盖任务；某通用任务案例可靠性提升 5.2 分，但丢失 10 个原有任务。多数可靠性增益伴随部署成本上升，且具体改动通常优于通用提醒，但组合效果会变化。最高分 Agent 未产生最大……（原文截断）。

rss · Hugging Face Daily Papers · Nov 10, 04:27

**「为什么重要」** 对 Agent 工程师而言，该研究提供了 benchmark 分数、任务覆盖、可靠性与部署成本之间的具体权衡数据，直接关联 Harness 开发与评估系统设计。研究指出高分不等于全面改进，提醒工程师在迭代时需同时监控任务覆盖变化与成本。

**「可关注」** 可关注：Harness 自演化存在任务覆盖丢失与部署成本上升的张力，评估时需同时监控覆盖度与成本。

**Tags**: `#harness`, `#eval`, `#coding-agent`

---

<a id="item-agent-engineer-6"></a>
### [Nemotron-Personas-Finance-Japan 发布](https://huggingface.co/blog/nvidia/nemotron-personas-finance-japan) ⭐️ 6.3/10

2026 年 11 月 9 日，NVIDIA、Elith 联合 Hugging Face 发布开源合成数据集 Nemotron-Personas-Finance-Japan，这是首个百万级日本金融领域合成人格数据集。数据集由日本多家头部金融机构与行业协会参与设计，采用 NVIDIA NeMo Data Designer 与 NeMo SDG-PGMs 框架生成，基于日本官方统计、家庭金融与金融素养数据构建，共 900 万条人格记录，每条含 50 个字段，覆盖人口属性、职业、资产分布、金融行为等维度，采用 CC BY 4.0 许可支持商用。所有记录均为合成数据，不涉及真实个人隐私，主要面向日本金融行业的 AI 开发与评估团队，也可用于日语 AI 项目的训练测试，原生兼容 NeMo User Sim 用户模拟框架，同天还发布了配套的合成日本商业文档 PII 数据集 Nemotron-PII-Japan，影响范围主要集中于日本金融领域 AI 开发者及日语 AI 项目团队。

rss · Hugging Face Blog · Nov 9, 15:05

**「为什么重要」** 该数据集填补了日本金融领域开源百万级合成人格数据的空白，解决了金融 AI 开发中真实数据隐私合规门槛高、本地化高质量数据不足的痛点，为相关团队提供了可商用的合规数据基础。

**「可关注」** 可关注：该数据集原生兼容 NeMo User Sim 用户模拟框架，配套同天发布的 Nemotron-PII-Japan 数据集可直接用于测试金融 Agent 对用户敏感信息的保护能力。

**Tags**: `#eval`, `#harness`, `#synthetic-data`

---

<a id="item-agent-engineer-7"></a>
### [llm-anthropic 0.31 支持 Fable 5.2 与 Mythos 5.2](https://simonwillison.net/2026/Nov/9/llm-anthropic/) ⭐️ 6.0/10

2026年11月9日，Simon Willison 发布 llm-anthropic 0.31，为 llm CLI 的 Anthropic 插件新增对 Anthropic 当日发布的 Fable 5.2、Mythos 5.2 模型的支持，可配置 low、medium、high、xhigh、max 五档推理强度。作者实测五档推理生成鹈鹕骑自行车 SVG，xhigh 档效果最佳，max 档因消耗 128000 token 思考后耗尽 token 未返回图像，该问题为 Fable 系列首次出现，此前 Fable 5、5.1 的 max 档可正常生成，故障是否普遍存在尚未证实。该更新面向 llm CLI 的 Anthropic 模型用户。

rss · Simon Willison · Nov 9, 23:58

**「为什么重要」** 该更新让 llm CLI 用户可直接调用 Anthropic 最新发布的两款模型，同时实测暴露了 Fable 5.2 max 推理档的 token 耗尽问题，该问题与 Opus 5.5 的过思考故障模式一致，目前尚未确认是否会影响其他使用场景。

**「可关注」** 可关注：Fable 5.2 的 max 推理档存在因过度思考耗尽 token 的已知问题，该故障模式与 Opus 5.5 一致，且为 Fable 系列首次出现。

**Tags**: `#harness`

---

<a id="item-agent-engineer-8"></a>
### [Flide 提出决策推理精确分叉引擎](https://huggingface.co/papers/2610.42148) ⭐️ 6.0/10

2026-11-10，Hugging Face Daily Papers 收录论文摘要，提出 Flide。该引擎面向 LLM agent 决策模型，将逻辑树结构与单层扁平 token 流的物理执行解耦。ForkAttention 用 GPU resident indices 导航请求依赖，覆盖标准注意力与 Gated DeltaNet 循环层，解决 prefix 重计算与概率失真问题。当前仅为截断摘要，缺少完整性能数据、评估结果和发布细节。

rss · Hugging Face Daily Papers · Nov 10, 00:00

**「为什么重要」** 决策模型（如 Jev）正成为 LLM agent 快速执行的新范式。现有生成式推理引擎对其支持不足。若 Flide 的 decoupled execution 与 exact arithmetic 在完整论文中验证，可能影响 agent harness 的推理后端设计。

**「可关注」** 可关注：ForkAttention 在单层扁平 token 流中通过 GPU resident indices 维护跨标准注意力与 Gated DeltaNet 层的请求依赖，这一设计为 agent 多分支决策推理的 prefix 重计算问题提供了新的实现路径。

**Tags**: `#harness`

---

<a id="item-agent-engineer-9"></a>
### [PCBRouteAgent 论文提出工具代理编排模式](https://huggingface.co/papers/2611.08175) ⭐️ 6.0/10

2026-11-10，Hugging Face Daily Papers 推送论文 PCBRouteAgent，提出一种多模态 PCB 路由代理。该代理采用全局-局部分层架构：Global Routing Planner 结合板图图像与电气几何信息制定连接拓扑、布线顺序、通道及层间过渡；Detailed Routing Executor 调用 KiCad 原生引擎执行布线，并在局部失败时进行有界恢复，未解决失败以结构化反馈返回以修正路由指南。当前公开材料仅提供截断摘要，未披露性能指标、评估数据集或完整实现细节，且问题域局限于 PCB 布线，其编排模式向其他领域的可迁移性尚未证实。

rss · Hugging Face Daily Papers · Nov 10, 04:27

**「为什么重要」** 该论文展示了全局规划与本地执行分离、原生工具集成及结构化失败反馈的代理编排模式，对工具使用 agent 设计有参考价值；但其狭窄领域和缺失的量化结果意味着该模式的有效性尚未得到广泛验证。

**「可关注」** 可关注：全局-局部分层编排与结构化失败反馈在工具使用代理中的复用潜力，但需等待完整论文验证其泛化能力。

**Tags**: `#orchestration`

---

## AI Daily

<a id="item-ai-daily-1"></a>
### [ChatGPT Enterprise 上线 AWS Marketplace](https://openai.com/index/chatgpt-enterprise-aws-marketplace) ⭐️ 7.8/10

OpenAI 于 2026 年 11 月 9 日宣布，ChatGPT Enterprise 正式上线 AWS Marketplace。企业用户可通过现有 AWS 采购与计费关系直接购买该服务，简化采购流程。目前未披露具体定价、区域限制等额外采购细则。

rss · OpenAI Blog · Nov 9, 19:00

**「为什么重要」** 企业无需额外开通独立采购通道，可直接复用现有 AWS 账单体系完成服务采购与结算，降低企业采购门槛。

**「可关注」** 可关注：企业用户现可通过 AWS Marketplace 复用现有采购与计费关系获取 ChatGPT Enterprise，采购流程进一步简化。

**Tags**: `#lab`, `#product`, `#industry`

---

<a id="item-ai-daily-2"></a>
### [OpenAI Control Room 上线](https://openai.com/index/control-room) ⭐️ 7.8/10

OpenAI 发布 Control Room 中央系统，用于跟踪研究基础设施中的模型 workload。该系统可在安全或安全问题出现时快速停止相关 workload。这是 OpenAI 内部研究基础设施的安全监控组件。

rss · OpenAI Blog · Nov 9, 13:00

**「为什么重要」** 这体现了 AI 实验室对模型安全监控的工程化投入，提供了从监控到紧急停止的完整响应链路。

**「可关注」** 可关注：内部安全监控系统的 workload 追踪与紧急停止机制设计。

**Tags**: `#lab`, `#industry`, `#policy`, `#product`

---

<a id="item-ai-daily-3"></a>
### [CodeRabbit 基于 Codex 交付量提升 20 倍](https://openai.com/index/coderabbit-codex-daybreak) ⭐️ 6.8/10

OpenAI 官方博客发布案例研究，披露代码开发工具 CodeRabbit 基于 OpenAI 模型实现 AI 生成代码的治理与信任校验，同时依托 Codex 帮助同规模工程团队提升软件交付量 20 倍。当前公开材料未披露该指标的计算方式、合作范围及落地时间，无法验证数据准确性。

rss · OpenAI Blog · Nov 9, 08:00

**「为什么重要」** 这是 OpenAI 官方公开的 Codex 与 OpenAI 模型产业落地案例，为 AI 编码工具的代码治理、交付提效效果提供了可参考的实证样本。

**「可关注」** 可关注：Codex 已在产业端出现同规模团队交付量提升 20 倍的落地案例。

**Tags**: `#lab`, `#industry`, `#product`

---

<a id="item-ai-daily-4"></a>
### [OpenAI API 加速 Kuken 图纸检索](https://openai.com/index/kuken) ⭐️ 6.8/10

Kuken Industries 使用 OpenAI API 检索 70 年历史冷却塔图纸。工程师单次检索耗时从近 1 小时降至 4.5 分钟。该案例来自 OpenAI 官方博客，无新模型或产品发布。

rss · OpenAI Blog · Nov 9, 08:00

**「为什么重要」** 该案例展示了 OpenAI API 在工业图纸检索中的具体效率提升，为类似场景提供可量化的参考。

**「可关注」** OpenAI API 将 70 年历史工程图纸的检索时延从近 1 小时压缩至 4.5 分钟。

**Tags**: `#industry`, `#lab`, `#product`

---

<a id="item-ai-daily-5"></a>
### [Claude Fable 5.2 体验与 Jagged AGI 讨论](https://www.oneusefulthing.org/p/fable-52-and-jagged-agi) ⭐️ 5.5/10

Ethan Mollick在其个人博客中分享了Claude Fable 5.2的早期非官方使用体验，该模型承接已发布的Opus 5.5的能力，他在单次提示下完成了视频创作、硬件破解、商业方案设计、人文课程重建、学术研究等跨领域任务。他认为该模型接近其定义的AGI标准但未达标，存在「锯齿状AGI（Jagged AGI）」的能力短板，包括自主发现审美与判断问题、持续运营复杂系统等。

rss · One Useful Thing · Nov 9, 19:04

**「为什么重要」** 这篇文章提供了当前大模型能力的多领域非官方实测样本，覆盖从创意生成到学术研究的多种场景，为评估大模型与AGI的边界提供了可参考的实测依据。

**「可关注」** 可关注：当前大模型可在单次提示下完成跨领域复杂任务，但在自主识别审美、判断类问题，以及长期稳定运行复杂多环节系统方面仍存在明显短板。

**Tags**: `#model`, `#industry`, `#eval`

---