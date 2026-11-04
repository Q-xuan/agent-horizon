---
layout: default
title: "Horizon Summary: 2026-11-04 (EN)"
date: 2026-11-04
lang: en
---

> From 176 items, 15 important content pieces were selected

---

**Agent Harness Architecture**
1. [Agents 0.33.0 发布](#item-harness-arch-1) ⭐️ 8.8/10
2. [FastMCP v4.2.0a3 发布](#item-harness-arch-2) ⭐️ 6.8/10
3. [openai-agents-js v0.22.0-alpha.1 发布](#item-harness-arch-3) ⭐️ 6.8/10

**AI Agent Engineer**
1. [datasette-apps 0.3a0 发布](#item-agent-engineer-1) ⭐️ 7.8/10
2. [Datasette-agent 0.5a0 发布](#item-agent-engineer-2) ⭐️ 7.8/10
3. [StateBench 发布 长文档状态追踪基准](#item-agent-engineer-3) ⭐️ 7.8/10
4. [ParetoSaddler 提出联合质量成本优化方法](#item-agent-engineer-4) ⭐️ 7.0/10
5. [HF每日论文：Mage-VL-Cowork 混合CUA方案](#item-agent-engineer-5) ⭐️ 7.0/10
6. [HF 论文：近零词嵌入致门控模型训练静默停滞](#item-agent-engineer-6) ⭐️ 7.0/10
7. [Palette 小模型生成设计语言幻灯片](#item-agent-engineer-7) ⭐️ 5.8/10
8. [Cognition 发布 11 月安全指南](#item-agent-engineer-8) ⭐️ 5.8/10

**AI Daily**
1. [OpenAI 展示 Codex 工程应用案例](#item-ai-daily-1) ⭐️ 6.8/10
2. [Cisco 携手 OpenAI 强化企业安全](#item-ai-daily-2) ⭐️ 6.8/10
3. [Heimstaden 用 Codex 管物业](#item-ai-daily-3) ⭐️ 6.8/10

**AI Deals**
1. [Epic 13款小游戏限免 11.9截止](#item-ai-deals-1) ⭐️ 8.0/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [Agents 0.33.0 发布](https://github.com/cloudflare/agents/releases/tag/agents%400.33.0) ⭐️ 8.8/10

Cloudflare Agents 0.33.0 将 PiHarness 运行时升级至 Pi 1.5，流式输出存储改为批处理（最长 1 秒间隔），并优化调度器减少冗余检查。SQLite 存储事务减少约 27 倍，2,048 会话吞吐量从 88 提升至 459 runs/sec，但崩溃可能丢失约 1 秒数据。API 层面 \`session.watch\(\)\` 替代 \`session.events\(\)\`，新增 \`session.continue\(\)\` 与 \`defaults.maxTurns\`，移除 \`retry\(\)\` 和 \`parked\` 状态。Pi 1.4 不再受支持，升级后无法回滚。

github · github-actions\[bot\] · Nov 3, 13:14

**「设计要点」** Pi 1.5 运行时将流式文本追加改为增量写入，避免每次更新全量复制，500 KB 工具调用内存占用从 100 MB 大幅下降。调度器将并发提交合并为单次存储调用，常规运行零存储读取。浏览器工具层引入 \`browser.session\(\{ lock: true \}\)\` 与 \`BrowserSession\`，使 harness 外部代码可复用同一浏览器实例。

**「改了什么」** PiHarness 升级至 Pi 1.5，流式输出批处理存储，调度器并发性能提升约 5 倍。会话 API 替换为 \`session.watch\(\)\` 与 \`session.entries\(\)\`，新增 \`continue\(\)\` 和 \`maxTurns\` 限制，移除 \`retry\(\)\` 与 \`parked\` 状态，浏览器工具增加 \`functionDocs\(\)\`、作用域锁及外部调用支持。

**Tags**: `#runtime`, `#memory`, `#performance`

---

<a id="item-harness-arch-2"></a>
### [FastMCP v4.2.0a3 发布](https://github.com/PrefectHQ/fastmcp/releases/tag/v4.2.0a3) ⭐️ 6.8/10

FastMCP v4.2.0a3 发布，将 skills 子系统统一到 \`Skill\`、\`SkillCatalogProvider\` 和严格 \`SkillsDirectoryProvider\`。目录加载在发布前验证每个 skill，支持 YAML \`allowed-tools\` 列表。修复代理发现缓存、OpenAPI 引用保留和客户端连接恢复。skills 仍为实验性，仅用于集成测试。

github · zzstoatzz · Nov 3, 23:39

**「设计要点」** \`SkillsDirectoryProvider\` 在启动时验证 skill 目录，验证失败即抛出异常。legacy 4.1 skills providers 保留原有行为但输出弃用警告，计划 4.3 移除；\`experimental\_skills=True\` 重定向到新 provider 并拒绝子类以维持访问控制。

**「改了什么」** skills 加载从宽松变为启动时严格验证，引入 \`SkillsDirectoryProvider\` 和 \`SkillCatalogProvider\` 替代旧 provider。legacy 4.1 skills API 进入弃用倒计时，\`list\_skills\` 重命名为 \`list\_skill\_summaries\`，新增 \`Client.read\_skill\` 和 \`fastmcp list --skills\`。

**Tags**: `#tools`, `#permissions`, `#runtime`, `#mcp`

---

<a id="item-harness-arch-3"></a>
### [openai-agents-js v0.22.0-alpha.1 发布](https://github.com/openai/openai-agents-js/releases/tag/v0.22.0-alpha.1) ⭐️ 6.8/10

这是 OpenAI 官方发布的 JavaScript/TypeScript Agents SDK v0.22.0-alpha.1 预览版本，核心新增嵌入式 Codex 执行 harness。该版本要求使用 Node.js 24 及其自带 npm，提供 Linux x64、macOS Apple silicon、Windows x64 三平台 starter 压缩包及对应 SHA-256 校验和，部署流程为校验压缩包、解压后设置 OPENAI\_API\_KEY，执行 npm ci --ignore-scripts 后运行 node hello.mjs 即可调用示例模型接口，SDK 还支持将四个预构建包添加到现有应用中使用。

github · markstuart-oai · Nov 3, 15:36

**「改了什么」** 本次 alpha 相对前一版本明确披露的唯一能力变更为新增面向 JavaScript/TypeScript Agents SDK 的嵌入式 Codex harness，其余技术实现细节、架构调整未在发布内容中说明。

**Tags**: `#harness`, `#openai-agents-sdk`, `#alpha-release`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [datasette-apps 0.3a0 发布](https://github.com/datasette/datasette-apps/releases/tag/0.3a0) ⭐️ 7.8/10

2026年11月4日，simonw发布datasette-apps 0.3a0 alpha版本，核心优化Datasette Agent的应用创建与编辑能力。新增\#标签自动补全用户有权限查看的应用，新增app\_add\_stored\_queries、app\_remove\_stored\_queries两个工具管理应用可调用的存储查询，授予写查询需先获得用户审批；app\_create\(\)会校验请求的存储查询是否存在且用户有查看权限，创建前需用户审批写查询。工具结果新增应用相对路径，支持全屏打开应用，该版本要求Datasette≥1.0a41，支持Python 3.15并移除Python 3.10支持，主要影响使用Datasette Agent构建应用的开发者与agent工具权限设计工程师。

github · simonw · Nov 4, 00:29

**「为什么重要」** 该版本在Datasette生态内落地了agent工具的细粒度权限校验与写操作用户审批流，为其他agent harness设计工具安全模式提供了可参考的实现样本；目前这套模式在其他场景的适配效果尚未得到验证。

**「可关注」** 可关注：agent工具对写操作的权限前置校验与用户审批流的实现方式，以及工具结果返回相对路径替代自造URL的设计。

**Tags**: `#agent`, `#tools`, `#permissions`, `#harness`, `#datasette`

---

<a id="item-agent-engineer-2"></a>
### [Datasette-agent 0.5a0 发布](https://github.com/datasette/datasette-agent/releases/tag/0.5a0) ⭐️ 7.8/10

simonw 于 2026-11-03 发布 datasette-agent 0.5a0 正式 alpha 版本，面向数据场景的 AI agent 工具链迎来多项功能更新。核心变更包括：新建对话时可选择并锁定模型（模型列表来自 datasette-llm 的 agent 配置，可通过 \`/-/agent/api/models\` 获取）；新增 \`\#\` 引用标签，支持自动补全，可注入表结构、查询详情等上下文，权限跟随发送消息的用户；新增异步插件钩子 \`register\_agent\_reference\_types\(\)\`，支持插件扩展自定义 \`\#\` 引用类型；新增侧边栏面板，可通过 \`show\_in\_panel\` 工具渲染 Datasette 页面，窄屏支持 Chat \| Panel 切换。此外新增停止按钮、后台对话恢复、\`list\_tables\`/\`describe\_query\` 工具、\`sql\_query\` 命名参数与耗时统计，移除了“Explore with AI agent”功能及对应权限，最低依赖要求提升至 Python 3.11+、\`datasette&gt;=1.0a41\`、\`datasette-llm&gt;=0.1a9\`、\`llm&gt;=0.37.1\`，新增 Python 3.15 支持。该版本面向数据类 AI agent 开发者、插件架构工程师及工具调用模式研究者。

github · simonw · Nov 3, 23:13

**「为什么重要」** 该版本首次在数据类 agent 中落地按对话锁定模型、异步扩展引用类型、侧边栏渲染关联页面的交互模式，这些设计可直接复用于其他领域的 agent 工具链开发；目前尚未有公开案例验证这些模式在非数据场景下的适配效果。

**「可关注」** 可关注：\`register\_agent\_reference\_types\(\)\` 钩子支持异步函数扩展 \`\#\` 引用类型，为数据类 agent 的自定义上下文注入提供了低侵入的插件扩展路径。

**Tags**: `#harness`, `#permissions`, `#observability`, `#coding-agent`

---

<a id="item-agent-engineer-3"></a>
### [StateBench 发布 长文档状态追踪基准](https://allenai.org/blog/statebench) ⭐️ 7.8/10

Allen AI 于 2026-11-03 发布 StateBench 基准，评估语言模型在长文档中追踪实体状态变化的能力。基准设 4 个难度等级（R-trivial、Aperiodic、Soluble、General finite），对应从不可变赋值到引用赋值的状态更新操作。测试显示，预训练 Transformer 在 General finite 级别接近随机水平；循环与混合架构（如 Gated DeltaNet）经直接训练后可显著提升长序列表现。Gemini 3.8 Flash、Claude Opus 5.5、GPT-6 Sol 与 Luna 在输入增长时，Soluble 与 General finite 准确率骤降，最长 General finite 问题降至 13% 以下。所有预训练模型训练上下文不超过 64k token，测试输入远超该长度。基准附带技术报告、数据集与代码。

rss · Allen AI · Nov 3, 08:00

**「为什么重要」** 状态追踪是 AI Agent 处理代码、多步推理等长程任务的基础能力。StateBench 将理论难度分层并系统对比架构差异，为长上下文模型选型与记忆系统设计提供了可复现的评估框架。

**「可关注」** 可关注：任务表述格式显著影响模型得分，同一底层问题以 RULER 风格或电子表格编辑形式呈现时，混合模型与 Gated DeltaNet 表现差距明显，评估长上下文记忆能力需控制输入格式。

**Tags**: `#eval`, `#memory`

---

<a id="item-agent-engineer-4"></a>
### [ParetoSaddler 提出联合质量成本优化方法](https://huggingface.co/papers/2611.02079) ⭐️ 7.0/10

ParetoSaddler 是一种新提出的 LLM agent harness 优化方法，旨在同时优化响应质量与执行成本，对 harness 工程师有参考意义。该方法通过分离中间候选推广与最终部署选择，解决现有方法在联合优化时过早拒绝有价值候选的问题。每次迭代中，优化器更新父 harness 产生候选，通过多次执行比较两者，并使用 Bayesian bootstrap Pareto support 推广在质量或成本上显示可信进展的候选。该工作目前为 2026 年 11 月 4 日发布的 arXiv 预印本，来源内容截断，且无已确认的生产工具或版本号。

rss · Hugging Face Daily Papers · Nov 4, 00:00

**「为什么重要」** 现有 harness 优化主要关注响应质量，而实际部署需权衡质量与成本。ParetoSaddler 的分离机制为联合优化提供了新思路，可能影响后续 harness 工程实践。但该研究尚未正式发布，实际效果与可用性待验证。

**「可关注」** 联合质量-成本优化中，将中间候选推广与最终部署选择解耦，可能缓解过早拒绝问题。

**Tags**: `#harness`, `#eval`, `#coding-agent`

---

<a id="item-agent-engineer-5"></a>
### [HF每日论文：Mage-VL-Cowork 混合CUA方案](https://huggingface.co/papers/2610.40747) ⭐️ 7.0/10

2026年11月4日Hugging Face Daily Papers收录一篇预印本，介绍4B参数的混合计算机使用代理Mage-VL-Cowork：该代理从通用多模态对齐检查点出发，通过涵盖中训练、SFT、RL的5阶段渐进式课程端到端训练。配套工具Mage-CUA-Forge用可复用的技能条件生成工作流与应用专属准备器替代逐任务构建，合成293806个桌面及网页任务、覆盖6915个技能，单任务重复成本降低82.6%。研究团队还通过进化教师harness、部署专用CUA harness生成高质量训练轨迹。

rss · Hugging Face Daily Papers · Nov 4, 00:00

**「为什么重要」** 该预印本提供了混合CUA训练全流程的可落地技术细节，包括降本数据合成工具与进化harness方案，对从事代理训练、harness设计的工程师有直接参考价值；但内容为未同行评审的预印本，且摘要存在截断，相关结论尚未经社区验证。

**「可关注」** 可关注：技能条件化的可复用生成工作流可显著降低CUA训练数据的逐任务合成成本，渐进式5阶段课程是混合CUA端到端训练的可选路径。

**Tags**: `#coding-agent`, `#harness`, `#orchestration`

---

<a id="item-agent-engineer-6"></a>
### [HF 论文：近零词嵌入致门控模型训练静默停滞](https://huggingface.co/papers/2611.04449) ⭐️ 7.0/10

2026年11月4日Hugging Face每日论文收录一项实证研究，揭示非独立门控序列模型存在普遍近零输入词嵌入故障模式，可导致训练静默停滞。研究 surveyed 291个开源权重模型仓库（共280个独立嵌入表），52.6%的非独立门控/混合检查点（20/38个）存在范数低于10^-6的可达输入词嵌入，权重绑定模型的该比例为0%。故障根因为预训练中未见稀有/模板token获得零输入梯度，AdamW权重衰减持续缩小非独立嵌入；在Mamba、Gated DeltaNet、xLSTM等门控序列模型中，近零token可将输入嵌入梯度放大超30个数量级（最高达35），抑制历史状态读取，最终导致训练停滞。Transformer配置中非初始位置或BOS token可规避该故障，研究同时提供了根因分析与缓解策略，对训练/微调这类模型的工程师有直接参考价值。

rss · Hugging Face Daily Papers · Nov 4, 00:00

**「为什么重要」** 该故障模式在Mamba、xLSTM等agent常用高效门控序列模型中普遍存在，超半数 surveyed 非独立门控检查点受影响，是训练/微调这类模型时需提前排查的静默风险。目前未证实该故障在闭源或更大规模模型中的普遍程度。

**「可关注」** 可关注：训练或微调Mamba、xLSTM等非独立门控序列模型时，优先检查输入嵌入层的范数分布，排查是否存在近零行故障。

**Tags**: `#coding-agent`, `#sequence-model-training`, `#failure-mode-analysis`, `#embedding-stability`

---

<a id="item-agent-engineer-7"></a>
### [Palette 小模型生成设计语言幻灯片](https://huggingface.co/blog/ibm-research/palette-deck-building) ⭐️ 5.8/10

IBM Research 推出 Palette 项目，尝试训练可自托管的小开源模型按自定义设计语言生成幻灯片，解决大模型风格固化、生成内容无法对齐自有模板、数据不能出域的问题。项目采用 LoRA 微调 20B 基础模型，将任务拆分为设计师（输出结构化 JSON 简报）和编码器（生成 pptxgenjs 代码绘制单页）两个角色，训练数据为合成数据，包含设计决策的反事实推理，且每份合成数据都会经过 harness 检查重叠、溢出等问题并修复。训练中发现编码器示例长度约为设计师的5倍，未过采样设计师示例会导致其训练不足，且通过参考样例而非 prompt 规则可更有效解决生成内容与输入不一致的问题。该模型在 PresentBench 三个测量领域中的两个排名第一，支持用户通过 \[\[ \]\] 包裹的指令调整设计选择。

rss · Hugging Face Blog · Nov 3, 16:35

**「为什么重要」** 该项目验证了小模型在垂直生成场景下，通过合成数据构造、分角色任务拆分、检查修复链路可接近大模型效果，其中的合成数据逻辑、harness 设计对 coding agent 的垂直场景适配有参考价值，但当前仅覆盖幻灯片生成场景，通用性尚未得到验证。

**「可关注」** 可关注：小模型垂直生成任务可通过分角色拆分降低单步推理压力、用带反事实推理的合成数据提升决策质量、搭配检查修复 harness 过滤低级错误，LoRA 微调可大幅降低实验成本。

**Tags**: `#harness`, `#eval`

---

<a id="item-agent-engineer-8"></a>
### [Cognition 发布 11 月安全指南](https://cognition.ai/blog/practical-guide-to-security-november-2026) ⭐️ 5.8/10

2026 年 11 月 3 日，Cognition 发布安全指南，盘点近期多起安全事件，包括 10 月 29 日披露的 Claude Code Cursor 扩展被投毒（安装量低于 5,000，利用自动更新传播，发布版本与 Open VSX registry 不一致），以及 Binance 遭窃取 63.4 亿美元事件（攻击者通过虚假面试和篡改安装程序入侵工程师笔记本）。文章还提及 PHP2Shell、GitLab 未授权远程代码执行、eMudhra 证书机构私钥设为 4、KVM 虚拟机逃逸、Linux 多路径 TCP 栈 CVE-2026-98432（Go 1.24+ 默认启用）等漏洞。Cognition 建议企业立即启用防钓鱼多因素认证、审计公开攻击面、部署密码管理器和广告拦截器，30 天内完成设备管理/终端检测响应、扩展白名单、密钥扫描，并迁移至云端编码代理或远程开发环境。该博文未提供技术细节、评估数据或架构层面的深入分析。

rss · Cognition Blog · Nov 3, 17:00

**「为什么重要」** 该文出自 Devin 开发商 Cognition，直接点名编码代理生态中的扩展供应链风险（如 Claude Code Cursor 扩展投毒）及开发机失陷导致的生产环境入侵路径，对构建编码代理的工程师有直接参考价值。但博文停留在通用安全建议层面，未提供漏洞机理、复现步骤或代理权限模型的评估数据，因此其 actionable 程度有限。

**「可关注」** 可关注：扩展自动更新与注册表发布流程的下游信任链，Cursor 事件表明即使上游 Open VSX registry 未受污染，发布管道下游仍可能被篡改并推送恶意版本。

**Tags**: `#security`, `#coding-agent`, `#permissions`

---

## AI Daily

<a id="item-ai-daily-1"></a>
### [OpenAI 展示 Codex 工程应用案例](https://openai.com/index/accelerating-engineering-for-the-physical-world) ⭐️ 6.8/10

OpenAI 发布官方博客，介绍 ChatGPT 与 Codex 在 CAD、PCB 设计、仿真等物理工程工作流中的应用。分析指出该文主要定位为用例展示，未涉及新模型发布、政策变更或技术突破。文章未披露具体性能数字或限制条件。

rss · OpenAI Blog · Nov 3, 12:00

**「为什么重要」** 该文呈现了 AI 编码工具向物理工程领域渗透的具体场景，为相关自动化工作流构建提供参考。

**「可关注」** 可关注：Codex 在 CAD、PCB 设计及仿真等物理工程工作流中的实际应用案例。

**Tags**: `#lab`, `#product`, `#industry`

---

<a id="item-ai-daily-2"></a>
### [Cisco 携手 OpenAI 强化企业安全](https://openai.com/index/cisco-cyber) ⭐️ 6.8/10

OpenAI 官方博客发布的案例研究显示，思科正将网络智能与 OpenAI 模型结合，用于构建更自适应的企业安全防御体系。该案例不涉及新模型发布或重大政策调整，影响范围相对有限。材料未披露具体性能指标、部署规模或时间表。

rss · OpenAI Blog · Nov 3, 08:00

**「为什么重要」** 这是 OpenAI 企业级安全场景的又一落地案例，对关注 AI 安全应用的团队具有参考价值。

**「可关注」** 可关注：思科将网络智能与 OpenAI 模型结合，构建自适应企业安全防御解决方案的案例。

**Tags**: `#product`, `#industry`, `#lab`

---

<a id="item-ai-daily-3"></a>
### [Heimstaden 用 Codex 管物业](https://openai.com/index/heimstaden) ⭐️ 6.8/10

OpenAI 官方博客宣布，欧洲住宅房地产运营商 Heimstaden 正在其欧洲业务中部署 ChatGPT Enterprise 与 Codex，用于优化物业管理工作并降低成本。该案例展示了 OpenAI 企业级产品在房地产行业的应用，但未披露具体效率提升或成本节约数字，也未发布新模型或功能。

rss · OpenAI Blog · Nov 3, 08:00

**「为什么重要」** 这是 OpenAI 企业产品在传统房地产行业的实际应用案例，可作为企业级 AI 部署的参考。

**「可关注」** 可关注：ChatGPT Enterprise 与 Codex 在物业管理场景中的实际应用方式。

**Tags**: `#lab`, `#industry`, `#product`

---

## AI Deals

<a id="item-ai-deals-1"></a>
### [Epic 13款小游戏限免 11.9截止](https://www.appinn.com/eggs-261103/) ⭐️ 8.0/10

你看到的内容可能由第三方 AI 基于小众软件文章提炼总结而成，可能与原文真实意图存在偏差。不代表小众软件观点和立场。请&lt;a href=&quot;https://www.appinn.com/eggs-261103/&quot; target=&quot;\_blank&quot;&gt;点击链接阅读原文&lt;/a&gt;细致比对和校验。&lt;br /&gt;&lt;br /&gt;Epic商店当前发放13款Yash Future Tech Solutions出品的小游戏限免福利，涵盖赛车、平台跳跃、解谜、数学问答等品类，领取后永久入库无需立即下载。领取条件为登录Epic账户，在对应游戏页面点击「获取」并确认金额为0元即可添加到库，北京时间2026年11月9日凌晨2:30截止。

rss · 小众软件 · Nov 3, 13:13

**「为什么重要」** 这批限免均为轻量小游戏，品类覆盖休闲、竞速、解谜、教育等场景，永久入库规则无后续消费要求，适合想低成本扩充游戏库的玩家在截止前领取。

**「可关注」** 可关注：网页版领取时若弹出「与当前设备不兼容」提示，仍可继续完成入库操作，下载安装可延后处理。

**Tags**: `#promo`, `#limited-free`

---