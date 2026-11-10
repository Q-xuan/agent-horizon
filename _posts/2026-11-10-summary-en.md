---
layout: default
title: "Horizon Summary: 2026-11-10 (EN)"
date: 2026-11-10
lang: en
---

> From 212 items, 18 important content pieces were selected

---

**Agent Harness Architecture**
1. [browser-use 1.0.0rc5 发布](#item-harness-arch-1) ⭐️ 8.8/10
2. [browser-use 1.0.0 发布](#item-harness-arch-2) ⭐️ 7.8/10
3. [FastMCP v4.2.0a4 发布](#item-harness-arch-3) ⭐️ 7.8/10
4. [Anthropic Skills 仓库发布](#item-harness-arch-4) ⭐️ 6.0/10

**AI Agent Engineer**
1. [Fable 5.2 与 Mythos 发布](#item-agent-engineer-1) ⭐️ 8.0/10
2. [Google 发布 8tx 与 8i Max TPU](#item-agent-engineer-2) ⭐️ 7.0/10
3. [HF 每日论文：ReproBridge 基准发布](#item-agent-engineer-3) ⭐️ 7.0/10
4. [HF 每日论文：A2-MEAS 具身框架](#item-agent-engineer-4) ⭐️ 7.0/10
5. [Agent Harness Evolution 研究摘要](#item-agent-engineer-5) ⭐️ 7.0/10
6. [HF Daily Papers：AutoVend 基准发布](#item-agent-engineer-6) ⭐️ 6.0/10
7. [simonw/llm-anthropic 0.31 发布](#item-agent-engineer-7) ⭐️ 5.8/10
8. [Nemotron 日本金融合成数据集发布](#item-agent-engineer-8) ⭐️ 5.8/10
9. [HOPE 二阶剪枝降低 MoE 内存](#item-agent-engineer-9) ⭐️ 5.8/10

**AI Daily**
1. [ChatGPT Enterprise 登陆 AWS Marketplace](#item-ai-daily-1) ⭐️ 7.8/10
2. [OpenAI 发布 Control Room 工作负载管控系统](#item-ai-daily-2) ⭐️ 7.8/10
3. [CodeRabbit 用 Codex 实现 20x 软件交付](#item-ai-daily-3) ⭐️ 6.8/10
4. [Kuken Industries 用 OpenAI API 检索 70 年图纸](#item-ai-daily-4) ⭐️ 6.8/10
5. [Touch-R1 入选 NeurIPS 2026](#item-ai-daily-5) ⭐️ 5.5/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [browser-use 1.0.0rc5 发布](https://github.com/browser-use/browser-use/releases/tag/1.0.0rc5) ⭐️ 8.8/10

browser-use 1.0.0rc5 发布，agent 引擎从逐步 DOM 动作选择改为基于 Pydantic AI 的持久 Python REPL，调用 browser-harness 与原始 CDP。代码库从 68,815 行压缩至 13,154 行，保留 0.x 常用接口。默认切换至 Browser Use Cloud 浏览器、\`bu-fast\` 模型、\`max\_steps=100\` 与 \`timeout=1700\` 秒，新增结构化输出、上传下载、密钥脱敏、域名限制与网页搜索。

github · gregpr07 · Nov 9, 23:36

**「设计要点」** 运行时采用持久 Python REPL 替代逐步 DOM 解析，通过 browser-harness 与原始 CDP 操控浏览器。工具结果全部保留在对话中，密钥通过 \`type\_secret\(\)\` 脱敏但非沙箱隔离，本地浏览器需显式指定 \`Browser\(&\#x27;chromium&\#x27;\)\`。

**「改了什么」** 引擎替换为基于 Pydantic AI 的持久 Python REPL，代码行数从约 69k 降至 13k。默认浏览器改为 Browser Use Cloud，模型改为 \`bu-fast\`，\`max\_steps\` 默认 100，新增结构化输出、上传下载、密钥脱敏、域名限制与网页搜索。

**Tags**: `#runtime`, `#tools`, `#planning`

---

<a id="item-harness-arch-2"></a>
### [browser-use 1.0.0 发布](https://github.com/browser-use/browser-use/releases/tag/1.0.0) ⭐️ 7.8/10

browser-use 1.0.0 完成底层重写，删除 80% 代码，以持久化 Python REPL 直连 Chrome DevTools Protocol 取代原有 action schema 与 DOM 序列化层。默认模型切换至 Browser Use 网关的 \`bu-fast\`，默认浏览器变为云端实例，\`max\_steps\` 从 500 降至 100，单步超时上限 1700 秒。官方基准测试宣称同模型下得分提升最高 33 分，成本降低 2.7–5.2 倍，速度提升 2–3 倍。

github · gregpr07 · Nov 10, 02:04

**「设计要点」** 运行时从“模型-动作 schema-DOM-浏览器”多层翻译栈坍缩为“模型-Python 代码-CDP”直连模型，消除序列化开销。发布说明未展开工具层、记忆与权限的具体实现，仅提及 secrets 脱敏与域名限制，未声明沙箱边界。

**「改了什么」** 删除全部 0.x 模块路径、action schema 与 DOM serializer，默认接入云端浏览器与 \`bu-fast\` 模型，\`run\(\)\` 步数上限改为 100。新增结构化输出、上传下载、web search、CLI/MCP 服务及 Docker 镜像，错误处理从抛出异常改为返回 \`status=&\#x27;error&\#x27;\`，未 honored 的 0.x 配置项直接报 \`TypeError\`。

**Tags**: `#runtime`, `#tools`, `#sandbox`, `#eval`

---

<a id="item-harness-arch-3"></a>
### [FastMCP v4.2.0a4 发布](https://github.com/PrefectHQ/fastmcp/releases/tag/v4.2.0a4) ⭐️ 7.8/10

FastMCP 发布 v4.2.0a4 alpha 预发行版本。该版本将最低 Python 要求提升至 3.11，构成破坏性变更。新增 \`Annotated\` 依赖注入支持，允许在工具、资源和提示中声明 \`Depends\(...\)\` 与 \`CurrentContext\(\)\` 元数据。技能功能仍处于实验阶段，仅面向集成测试。同时修复认证、OpenAPI 请求体、多选 elicitation 等核心缺陷。

github · zzstoatzz · Nov 10, 01:59

**「设计要点」** 技能对象重构为存储中立结构，引入严格 \`SkillsDirectoryProvider\`，并通过挂载服务器实现发现传播。实验性技能支持限制在集成测试场景。

**「改了什么」** 最低 Python 版本提升至 3.11。工具、资源和提示支持 \`Annotated\` 依赖声明。技能发现改为通过挂载服务器传播，4.1 版技能 API 标记废弃。修复 OpenAPI 请求体、CIMD 重定向 URI、多选 elicitation 模式等问题，并调整技能 URI 编码与发现逻辑。

**Tags**: `#mcp`, `#runtime`, `#tools`

---

<a id="item-harness-arch-4"></a>
### [Anthropic Skills 仓库发布](https://github.com/anthropics/skills) ⭐️ 6.0/10

Anthropic released an official Agent Skills implementation for Claude in the \`anthropics/skills\` repository. Skills are folders containing instructions, scripts, and resources that Claude loads dynamically to handle specialized repetitive tasks, such as generating documents with brand guidelines or analyzing organizational data. The implementation follows the Agent Skills standard described at agentskills.io. The repository currently provides only high-level conceptual documentation without versioned releases, API specifications, or architecture details.

rss · GitHub Trending Daily · Nov 10, 05:12

**Tags**: `#tools`, `#runtime`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [Fable 5.2 与 Mythos 发布](https://www.anthropic.com/claude-fable-and-mythos-5-2) ⭐️ 8.0/10

Anthropic 于 2026-11-09 发布 Claude Fable 5.2 与 Mythos 5.2。早期社区报告称 Fable 5.2 编码与代码审查能力接近 Opus 5.5，官方同步更新多领域基准对比。用户反馈显示模型 lineup 平衡性改善，普通编码任务下 Fable 5.2 与 Opus 5.5 差异缩小。一名用户报告在 60 万行 Fortran 计算材料科学代码库上实现 36 倍加速，耗时 2 天，并开源结果。社区对基准对比中 Carbon、Argon 及 robodojo 的选择提出疑问。

hackernews · lairv · Nov 9, 18:01 · [Discussion](https://news.ycombinator.com/item?id=50429068)

**「为什么重要」** Fable 5.2 的发布改变了 Anthropic 模型 lineup 的层级关系，使中档模型首次接近旗舰模型性能。这改变 coding agent 的模型选型成本与路由策略考量。36 倍加速案例若可复现，将改变遗留代码库优化的工作流，但单点案例尚未形成统计显著性。

**「可关注」** Fable 5.2 与 Opus 5.5 性能接近使模型路由策略需重新校准，同时社区对官方基准对比（Carbon、Argon、robodojo）的质疑提示内部 eval 应优先于公开 benchmark。

**「评论」** 社区共识认为 Anthropic 模型 lineup 平衡性显著改善，Fable 5.2 普通编码能力接近 Opus 5.5。分歧集中在官方基准对比的可信度：用户指出 Carbon 模型在特定基准的缺失及 robodojo 对比对象切换，认为对比曲线异常。实际体验包括 60 万行 Fortran 代码库 36 倍加速及代码审查发现 7 个严重 bug 的案例。另有用户推测 Fable 5.2 的命名与 OpenAI 的 Astra 模型竞争有关，但该观点未获证实。

**Tags**: `#coding-agent`, `#eval`

---

<a id="item-agent-engineer-2"></a>
### [Google 发布 8tx 与 8i Max TPU](https://blog.google/innovation-and-ai/infrastructure-and-cloud/global-network/tpu-8i-max-and-8tx/) ⭐️ 7.0/10

On November 9, 2026, Google officially announced the 8tx and 8i Max TPUs, explicitly designed for agentic workloads. The accompanying TPUSync distributed inference technology has already been adopted by open-source agent tooling such as Strata for Qwen series models. The publicly released content does not include key metrics such as performance, cost per token, or hardware comparisons against NVIDIA GPUs.

hackernews · \_benx\_ · Nov 9, 21:56 · [Discussion](https://news.ycombinator.com/item?id=50432831)

**「为什么重要」** This is Google&\#x27;s first explicit launch of TPUs purpose-built for agentic scenarios, with the supporting distributed inference technology already having open-source adoption precedents. However, specific performance and cost advantages have not been publicly disclosed, and the actual impact on agentic inference deployment still requires verification.

**「可关注」** Monitor the open-source adoption progress of the TPUSync distributed inference solution, as well as the timeline for the new TPUs to be available on Colab and for cost/performance metrics to be publicly released.

**「评论」** Community discussions focus on four points: users hope the new TPUs will be rolled out to Colab soon to lower access barriers; some users recommend TPUSync technical documentation and note existing open-source project adoptions; other users question why Google does not sell these TPUs directly, and some users also question the lack of publicly disclosed per-token power consumption, cost, and comparisons with NVIDIA competing products.

**Tags**: `#orchestration`, `#coding-agent`

---

<a id="item-agent-engineer-3"></a>
### [HF 每日论文：ReproBridge 基准发布](https://huggingface.co/papers/2611.08452) ⭐️ 7.0/10

2026年11月10日Hugging Face每日论文推送了编号为2611.08452的论文，介绍ReproBridge：一个用于构建标准化可复现机器学习研究制品的代理工作流，以及配套的ReproBridge-Bench评估基准。该基准包含1029个任务，覆盖36篇论文的387个实验，每个任务附带5个人工验证的参考分数，用于测试编码代理在ML实验复现任务上的能力。当前公开的论文内容存在截断，暂无社区讨论。

rss · Hugging Face Daily Papers · Nov 10, 00:00

**「为什么重要」** 该基准填补了编码代理在ML实验复现场景的大规模量化评估空白，可支撑相关代理的能力对比与迭代；目前尚未有社区公开的采纳或扩展信息，其实际应用效果仍待验证。

**「可关注」** 可关注：ReproBridge-Bench 的 1029 个带人工验证参考分数的复现任务，以及其公开的完整任务集与评分规则，可补充现有编码代理评估在 ML 实验复现场景的覆盖缺口。

**Tags**: `#eval`, `#coding-agent`, `#orchestration`

---

<a id="item-agent-engineer-4"></a>
### [HF 每日论文：A2-MEAS 具身框架](https://huggingface.co/papers/2611.09124) ⭐️ 7.0/10

2026年11月10日，Hugging Face Daily Papers收录介绍具身多智能体框架A2-MEAS的论文。该框架以代码作为可扩展校正接口，整合校正语言、空间证据、执行历史与动作提案，配套MetaBrain提供训练监督与运行时引导，动作模型A2-WLA新增运动感知历史与隐式世界模型。该框架在50任务的BEHAVIOR 20基准上取得0.5755 Q-score，当前无社区公开讨论，且具身智能的定位使其对通用编码智能体、主流工具链工程师的直接参考价值有限。

rss · Hugging Face Daily Papers · Nov 10, 05:12

**「为什么重要」** 该论文提出的代码校正接口、多智能体监督机制与动作模型设计，为具身智能体的架构设计与评估方案提供了可参考的具体实现，但尚未有公开复现或跨场景验证结果，其对通用编码智能体的适用性仍待验证。

**「可关注」** 可关注 A2-MEAS将代码作为校正与行为适配的统一接口，训练阶段通过校正编码器与适配器将知识吸收到策略权重，部署阶段可冻结权重仅通过新代码调整行为，这种解耦设计或可参考到需要热更新的智能体场景。

**Tags**: `#eval`, `#orchestration`, `#memory`

---

<a id="item-agent-engineer-5"></a>
### [Agent Harness Evolution 研究摘要](https://huggingface.co/papers/2611.07624) ⭐️ 7.0/10

Hugging Face Daily Papers 于 2026-11-10 摘要了一篇研究，探讨在不更新模型权重的前提下，通过 agent harness evolution 实现递归自我改进（RSI）的效果。研究评估四种方法，发现全部 16 个演化后的代理均获得此前未覆盖的任务，同时丢失部分已覆盖任务；在一个通用任务案例中，可靠性提升 5.2 分，但丢失 10 个已覆盖任务。多数可靠性增益伴随部署成本上升，且特定组件干预通常优于通用提醒，但组合后收益可能变化。该摘要为二次来源，原文被截断，未提供完整实验细节。

rss · Hugging Face Daily Papers · Nov 10, 05:12

**「为什么重要」** 这提供了 harness 演化的首批系统性实证对比，直接关联 coding agent 的可靠性、成本与任务覆盖权衡。研究已发表，但具体收益是否适用于特定 harness 设计仍需工程师自行验证。

**「可关注」** 可关注：harness 演化会同时改变任务覆盖边界，需建立新获得与丢失任务的监控指标；特定干预策略通常优于通用提醒，但组合效果存在不确定性，建议小范围 A/B 验证。

**Tags**: `#harness`, `#eval`, `#coding-agent`

---

<a id="item-agent-engineer-6"></a>
### [HF Daily Papers：AutoVend 基准发布](https://huggingface.co/papers/2610.36980) ⭐️ 6.0/10

2026年11月10日，Hugging Face Daily Papers 推介了提出 AutoVend 基准的论文，该基准用于评估 LLM 智能体在长期自主售货运营任务中的表现，配套模拟器包含共享仓库、采购提前期、付费补货、库存过期、recurring 运营成本等真实运营约束。测试设定为 1 个 LLM 智能体通过网页操作界面管理 20 台售货机，覆盖 5 种站点类型，运行 180 个模拟天。当前推介内容未披露完整评测结果、对比数据及可复现技术细节，主要面向 LLM 智能体商业运营评测方向的研究者。

rss · Hugging Face Daily Papers · Nov 10, 00:00

**「为什么重要」** 它将线下 O2O 售货场景的长期运营约束纳入 LLM 智能体评测框架，填补了相关场景的评测空白。完整评测结果尚未公开，其对不同智能体能力的区分度、约束设计的合理性还有待完整论文验证。

**「可关注」** 可关注：AutoVend 模拟器纳入的库存过期、补货周期、recurring 运营成本等真实约束，可作为长期自主运营类智能体评测的参考设计。

**Tags**: `#eval`

---

<a id="item-agent-engineer-7"></a>
### [simonw/llm-anthropic 0.31 发布](https://github.com/simonw/llm-anthropic/releases/tag/0.31) ⭐️ 5.8/10

2026年11月9日，simonw 发布 llm-anthropic 0.31 版本，本次更新仅新增 \`claude-fable-5.2\` 和 \`claude-mythos-5.2\` 两个 Claude 5.2 模型别名，无其他 documented 变更，影响范围为使用该库且需调用对应 Claude 5.2 模型的开发者。

github · simonw · Nov 9, 23:58

**「为什么重要」** 本次更新未涉及库的功能逻辑或 agent 工作流相关变更，仅对使用 llm-anthropic 调用 Claude 5.2 系列模型的用户有直接别名支持价值，无更广泛的行业影响。

**「可关注」** 可关注：若你使用 llm-anthropic 库调用 Claude 5.2 系列模型，可更新至 0.31 版本使用新增的 \`claude-fable-5.2\`、\`claude-mythos-5.2\` 别名，无需其他配置变更。

**Tags**: `#model-support`

---

<a id="item-agent-engineer-8"></a>
### [Nemotron 日本金融合成数据集发布](https://huggingface.co/blog/nvidia/nemotron-personas-finance-japan) ⭐️ 5.8/10

2026年11月9日，Hugging Face与NVIDIA联合发布开源合成数据集Nemotron-Personas-Finance-Japan，专为日本金融领域AI开发设计。该数据集基于日本官方人口、家庭财务及金融素养统计数据生成，共包含900万条合成人物记录（100万条核心记录衍生出9个变体人物），每条记录含50个字段，总token数约15亿，采用CC BY 4.0许可支持商用。数据集由NVIDIA NeMo Data Designer与NeMo SDG-PGMs框架生成，已纳入日本多家金融机构及行业协会的反馈，所有人物均为合成生成，面向日本金融AI开发、用户模拟、模型评估等场景开放。

rss · Hugging Face Blog · Nov 9, 15:05

**「为什么重要」** 这是首个百万级规模的日本金融领域开源合成人物数据集，填补了日本金融AI开发中合规可用高质量数据的空白，降低了使用真实用户数据的隐私合规风险。其对训练偏差的改善效果、对金融场景AI性能的实际提升作用尚未经过大规模验证，需结合具体使用场景观察。

**「可关注」** 可关注：该数据集已适配NeMo User Sim用户模拟框架，且可与同天发布的Nemotron-PII-Japan配套使用，前者用于生成金融场景模拟用户，后者用于测试PII检测与脱敏 pipeline 的效果。

**Tags**: `#eval`

---

<a id="item-agent-engineer-9"></a>
### [HOPE 二阶剪枝降低 MoE 内存](https://huggingface.co/blog/amazon/higher-order-pruning-experts) ⭐️ 5.8/10

Hugging Face 于 2026-11-09 发布 HOPE（Higher-Order Pruning of Experts），一种无需训练的 MoE 模型专家剪枝方法，通过二阶交互项建模专家间合作关系。在 Qwen3.5-122B（每层 256 专家、每 token 仅激活 8 个、95% 内存来自专家 MLP）上，50% 剪枝率时比最优一阶基线（REAP、MAN、EAN、Frequency）在 agentic coding 任务上平均排名最优，最高提升 +6.1%。该方法需一次校准数据集前向传播，外加每层 1–2 秒二次规划求解，总开销可忽略。当前评估覆盖 Qwen3.5-122B、Qwen3.5-35B 与 GLM-4.5-Air 三个模型。

rss · Hugging Face Blog · Nov 9, 12:34

**「为什么重要」** 对需部署 MoE 模型的 agent 工程师，HOPE 在 aggressive pruning 下仍能保持 agentic coding 性能，且无需重训练或动态加载。其有效性已在 SWE-Bench Pro 等编码基准上验证，但模型覆盖范围仍有限。

**「可关注」** 可关注：HOPE 的 F 矩阵对角线几乎完美恢复 REAP 的一阶专家排序（Spearman ρ），表明性能增益主要来自专家 pairwise 交互项，而非独立重要性评分差异。

**Tags**: `#memory`

---

## AI Daily

<a id="item-ai-daily-1"></a>
### [ChatGPT Enterprise 登陆 AWS Marketplace](https://openai.com/index/chatgpt-enterprise-aws-marketplace) ⭐️ 7.8/10

OpenAI 官方宣布 ChatGPT Enterprise 现已登陆 AWS Marketplace。企业用户可通过现有 AWS 账户完成采购与计费，复用既有采购关系简化流程。目前未披露具体定价、区域限制或功能差异。

rss · OpenAI Blog · Nov 9, 19:00

**「为什么重要」** 这是 OpenAI 企业级产品与云厂商市场的直接集成，可降低企业采购门槛。AWS 企业客户无需单独签约，即可在现有采购框架内获取 ChatGPT Enterprise。

**「可关注」** 可关注：ChatGPT Enterprise 已支持通过 AWS Marketplace 采购，企业可复用现有 AWS 计费关系。

**Tags**: `#product`, `#lab`, `#industry`

---

<a id="item-ai-daily-2"></a>
### [OpenAI 发布 Control Room 工作负载管控系统](https://openai.com/index/control-room) ⭐️ 7.8/10

OpenAI 发布内部系统 Control Room，用于跟踪研究基础设施中的模型工作负载。当安全或安全问题出现时，该系统可快速停止相关模型工作负载。

rss · OpenAI Blog · Nov 9, 13:00

**「为什么重要」** 这显示大型 AI 实验室正在建立具体的模型工作负载安全管控机制。

**「可关注」** 可关注：跨研究基础设施的模型工作负载跟踪与快速停止机制设计。

**Tags**: `#lab`, `#policy`, `#safety`

---

<a id="item-ai-daily-3"></a>
### [CodeRabbit 用 Codex 实现 20x 软件交付](https://openai.com/index/coderabbit-codex-daybreak) ⭐️ 6.8/10

OpenAI 官方博客发布客户案例，报告 CodeRabbit 基于 OpenAI Codex 与模型，使工程团队在相同人力下软件交付量提升 20 倍。CodeRabbit 同时使用 OpenAI 模型治理并信任 AI 生成的代码。该案例属于客户应用展示，并非 OpenAI 发布新模型、政策或核心产品。

rss · OpenAI Blog · Nov 9, 08:00

**「为什么重要」** 该案例展示了 AI 编码工具在工程团队中的规模化应用效果，20 倍交付提升的声称值得关注，但需注意这是单一客户案例，非独立第三方验证。

**「可关注」** 可关注：CodeRabbit 将 OpenAI 模型用于代码信任治理，同时使用 Codex 提升交付量，显示 AI 工具在代码生成与代码治理上的双重应用。

**Tags**: `#lab`, `#industry`, `#product`

---

<a id="item-ai-daily-4"></a>
### [Kuken Industries 用 OpenAI API 检索 70 年图纸](https://openai.com/index/kuken) ⭐️ 6.8/10

OpenAI 官方博客发布客户案例，Kuken Industries 采用 OpenAI API 检索 70 年历史的冷却塔图纸。工程师查找维修所需图纸的平均时长从近 1 小时降至 4.5 分钟。该案例展示了生成式 AI 在传统工业文档检索场景的落地效果。

rss · OpenAI Blog · Nov 9, 08:00

**「为什么重要」** 该案例为工业领域非结构化历史文档的 AI 检索提供了可验证的效率提升样本，降低了同类场景的落地参考门槛。

**「可关注」** 可关注：针对历史工业图纸这类非结构化文档，通过 OpenAI API 实现语义检索可将平均查找时长从近 1 小时压缩至 4.5 分钟。

**Tags**: `#industry`, `#product`

---

<a id="item-ai-daily-5"></a>
### [Touch-R1 入选 NeurIPS 2026](https://mp.weixin.qq.com/s?__biz=MzA3MzI4MjgzMw==&amp;mid=2651073140&amp;idx=3&amp;sn=788754bcaa053557f9c8ccd807058410) ⭐️ 5.5/10

戴盟机器人团队联合厦门大学、南京大学、大湾区大学、复旦大学提出首个触觉推理模型Touch-R1，相关论文已被NeurIPS 2026接收。该模型针对视觉与触觉冲突场景下多模态大模型易误判物体物理属性的问题，通过强化学习实现跨传感器触觉推理，可依据触觉证据修正视觉误判。配套开源的TouchReason-1M数据集覆盖1000余个日常物体、9大类材料，包含14700条有效触觉序列与132.3万个同步数据对，支持4种视触觉传感器的标准化采集与评测。以上信息来自科技媒体机器之心的公开报道，未附官方一手发布链接。

rss · 机器之心 · Nov 9, 08:45

**「为什么重要」** 当前多模态大模型在视觉与触觉信息冲突时往往优先采信视觉，易导致机器人抓取失败、物品损伤等安全风险。Touch-R1首次将强化学习系统性引入触觉推理领域，为具身智能建立更可靠的触觉物理认知能力提供了新路径。

**「可关注」** 可关注：Touch-R1的论文、代码、模型、TouchReason-1M数据集及TouchReason-Bench评测基准均已开源，支持跨传感器触觉推理模型的训练与效果验证。

**Tags**: `#model`, `#eval`, `#industry`

---