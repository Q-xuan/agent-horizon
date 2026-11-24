---
layout: default
title: "Horizon Summary: 2026-11-25 (EN)"
date: 2026-11-25
lang: en
---

> From 218 items, 16 important content pieces were selected

---

**Agent Harness Architecture**
1. [Codex CLI rust-v0.172.0 发布](#item-harness-arch-1) ⭐️ 8.8/10
2. [pydantic-ai v2.73.0 发布](#item-harness-arch-2) ⭐️ 7.8/10
3. [gemini-cli v0.71.0-nightly 发布](#item-harness-arch-3) ⭐️ 6.8/10

**AI Agent Engineer**
1. [Cognition 发布 SWE-2.1 模型](#item-agent-engineer-1) ⭐️ 8.8/10
2. [Embo-Harness 前沿模型策略 harness 研究](#item-agent-engineer-2) ⭐️ 7.0/10
3. [HF 每日论文：AutoPILOT 实时游戏智能体 harness](#item-agent-engineer-3) ⭐️ 7.0/10
4. [HF 每日论文：CSPD 可组合软提示蒸馏](#item-agent-engineer-4) ⭐️ 7.0/10
5. [Microduck 避障 Sim2Real 教程发布](#item-agent-engineer-5) ⭐️ 6.8/10

**AI Daily**
1. [GPT-6 展示蛋白质设计能力](#item-ai-daily-1) ⭐️ 9.8/10
2. [MCP 协议更新 扩展 Claude 交互能力](#item-ai-daily-2) ⭐️ 8.8/10
3. [Claude Artifacts 上线 Install as app 测试功能](#item-ai-daily-3) ⭐️ 8.8/10
4. [Codex与Astra辅助发现潜在系外行星](#item-ai-daily-4) ⭐️ 6.8/10
5. [iFood 在 15,000 仓库部署编码代理](#item-ai-daily-5) ⭐️ 6.8/10
6. [Intentful dot Aria 自动化](#item-ai-daily-6) ⭐️ 5.8/10

**AI Deals**
1. [Koofr 1TB 终身订阅 129.9美元 再开](#item-ai-deals-1) ⭐️ 8.0/10
2. [Show HN: Upronix 免费 uptime 监控工具](#item-ai-deals-2) ⭐️ 5.0/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [Codex CLI rust-v0.172.0 发布](https://github.com/openai/codex/releases/tag/rust-v0.172.0) ⭐️ 8.8/10

OpenAI Codex CLI rust-v0.172.0 releases MCP server lazy-loading, sandbox permission restoration, per-tool approval configuration, and nested agent thread navigation. Optional stdio MCP servers with cached tool lists now start on their first tool call by default. The \`codex exec resume\` command restores saved sandbox permissions, working directory, and workspace roots unless explicitly overridden. Users can set an approval reviewer for individual connected app tools via \`config.toml\`.

github · github-actions\[bot\] · Nov 24, 00:03

**「设计要点」** The release moves sandbox preparation into platform backends and introduces a shared sandbox launcher for Linux and macOS. Code Mode switches entirely to gRPC for host connections, deprecating the \`code\_mode\_host\_grpc\` setting. MCP tool approvals now use persistent Guardian V3 board evidence and attached reviewers for synchronous flows.

**「改了什么」** Relative to rust-v0.171.0, stdio MCP servers with cached tool lists now lazy-start on first invocation, and \`codex exec resume\` preserves sandbox permissions and workspace roots. The release adds per-tool approval reviewers in \`config.toml\`, TUI thread link navigation for nested agents, slash command Tab completion, and Shift+Up/Down task group navigation.

**Tags**: `#mcp`, `#sandbox`, `#permissions`, `#subagents`, `#runtime`

---

<a id="item-harness-arch-2"></a>
### [pydantic-ai v2.73.0 发布](https://github.com/pydantic/pydantic-ai/releases/tag/v2.73.0) ⭐️ 7.8/10

pydantic-ai v2.73.0 正式发布。本次更新扩展 agent 能力配置接口：\`Agent.override\` 新增 \`capabilities\` 参数，同时导出 \`AgentInstructions\` 与 \`SourcedInstruction\` 类型；\`RealtimeSession\` 新增 \`append\_voice\_instructions\` 支持 GPT-Live 语音模型；对 Anthropic 与 OpenAI 已弃用模型触发 \`DeprecatedModelWarning\`。OpenAI Responses 的 \`input\_transformations\`  surfaced 到 \`provider\_details\` 与模型请求 span。版本将 \`openai\` 依赖地板提升至 3.50.0，并变更私有上下文变量 \`Agent.\_override\_root\_capability\` 为 \`\(capability, injected\)\` 元组结构，直接读取该变量的代码需同步修改。

github · dsfaccini · Nov 24, 03:53

**「设计要点」** 运行时通过上下文变量注入 agent 覆盖能力，工具层支持嵌套参数模型的别名序列化以适配 Render 与 Azure Durable Task。记忆模块修复 \`Dataset\` 文件生成中 \`init=False\` 字段与 \`ClassVar\` 注解的处理，评测模块统一 Logfire 5 与 6 的在线评估事件emit。沙箱层新增 \`E2BSandbox\(idle\_timeout=...\)\` 与 \`boxd&gt;=0.3.3\` 支持，SSRF 保护在下载与 PowerShell 执行路径上加固。

**「改了什么」** \`Agent.override\` 新增 \`capabilities\` 配置入口，\`RealtimeSession\` 支持 GPT-Live 语音指令追加，对 Anthropic 与 OpenAI 已弃用模型触发 \`DeprecatedModelWarning\`。OpenAI Responses 缓存转换元数据 surfaced 到 provider 详情与 span。私有上下文变量 \`Agent.\_override\_root\_capability\` 改为 \`\(capability, injected\)\` 元组结构，\`openai\` 依赖地板升至 3.50.0，\`boxd\` 依赖升至 0.3.3。

**Tags**: `#runtime`, `#tools`, `#permissions`, `#prefix-cache`

---

<a id="item-harness-arch-3"></a>
### [gemini-cli v0.71.0-nightly 发布](https://github.com/google-gemini/gemini-cli/releases/tag/v0.71.0-nightly.20261124.gaafdfdfb5) ⭐️ 6.8/10

gemini-cli 发布官方 nightly 版本 v0.71.0-nightly.20261124.gaafdfdfb5。本次更新仅针对 A2A server 组件，强制实施 bearer token 认证并新增请求输入验证。该版本未包含重大架构或功能变更，仅做安全加固。

github · gemini-cli-robot · Nov 24, 01:13

**「改了什么」** A2A server 现强制验证 bearer token，未携带有效令牌的请求将被拒绝。服务端新增请求输入校验，拦截非法输入格式。变更来自 PR \#30420。

**Tags**: `#a2a`, `#permissions`, `#runtime`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [Cognition 发布 SWE-2.1 模型](https://cognition.ai/blog/swe-2-1) ⭐️ 8.8/10

Cognition 2026年11月24日发布SWE-2.1，作为SWE-2的纯强化学习升级版，基于Kimi K3训练，官方宣称其在FrontierCode 2.0、Terminal-Bench 4.1等编码基准，以及ExploitBench（80%）、ExploitGym（27.3%旗标捕获，针对Muse Wonder Full）等网络安全基准有大幅提升。模型支持长时自主工作，性能随rollout时间延长对数线性提升，同时推出面向Devin Security的SWE-2.1 Cyber版本，以及与Cerebras合作的10倍速SWE-2.1 Ultrafast版本。SWE-2.1免费至2026年12月8日，SWE-2.1 Ultrafast折扣价至2026年1月30日。

rss · Cognition Blog · Nov 24, 16:00

**「为什么重要」** 该升级是Cognition coding agent模型的最新重大迭代，其长时自主工作能力、网络安全能力提升及推理加速方案，对coding agent、网络安全方向的工程师有直接参考价值。

**「可关注」** 可关注：SWE-2.1通过降低训练时长度振荡实现了长时任务稳定训练，且测试时计算投入越多性能持续提升，其长时自主工作训练范式可参考。

**Tags**: `#coding-agent`, `#eval`

---

<a id="item-agent-engineer-2"></a>
### [Embo-Harness 前沿模型策略 harness 研究](https://huggingface.co/papers/2611.31201) ⭐️ 7.0/10

2026年11月24日Hugging Face Daily Papers发布论文《Embo-Harness: Towards Understanding Frontier-Model-as-Policy Harness》的截断摘要，提出Embo-Harness框架，用于系统研究将前沿多模态模型直接作为策略的机器人agent harness。研究拆解机器人agent循环的4个核心组件（提示工程、规划、动作执行、工具使用），提炼6项实证发现，总结出优先利用模型原生视觉推理与工具使用能力、而非手工制作的计划、技能或动作先验的harness设计方法。当前公开内容为截断摘要，完整论文未披露，研究直接用例为机器人领域，设计思路可泛化至更广泛的agent工程场景。

rss · Hugging Face Daily Papers · Nov 24, 00:00

**「为什么重要」** 该研究首次系统拆解前沿模型作为策略的harness核心组件，提炼了可验证的设计原则，对优化agent harness、工具链与agentic工作流的工程师有直接参考价值；但非机器人场景下该设计思路的实际效果尚未得到验证。

**「可关注」** 可关注：前沿模型作为策略的harness设计可优先复用模型原生视觉推理、工具使用能力，减少手工制作的计划、技能等组件投入。

**Tags**: `#harness`, `#orchestration`, `#tool-use`

---

<a id="item-agent-engineer-3"></a>
### [HF 每日论文：AutoPILOT 实时游戏智能体 harness](https://huggingface.co/papers/2611.28202) ⭐️ 7.0/10

2026年11月24日 Hugging Face 每日论文收录视觉智能体 harness 研究 AutoPILOT，该方案解耦智能体动作频率与模型推理速度，支持单次模型调用输出原始动作、启动开环宏或写入闭环控制器，无需额外模型调用即可持续执行操作。研究同时发布 AFK-Bench 基准，包含120款按特性分组的浏览器游戏，用于实时游戏智能体评估。该成果为研究预印本，非生产级可用工具。

rss · Hugging Face Daily Papers · Nov 24, 00:00

**「为什么重要」** 该研究直指实时游戏智能体 harness 的核心瓶颈——动作频率受模型推理速度限制，提出的三类动作输出模式为后续 agent  harness 设计提供了可参考的技术路径，AFK-Bench 也补充了实时场景下的评估缺口。目前仅为研究预印本，相关方案的实际落地效果尚未得到大规模验证。

**「可关注」** 可关注：现有视觉智能体 harness 普遍将单次模型调用限制为单次动作，AutoPILOT 提出的原始动作、开环宏、闭环控制器三类输出模式，是解耦动作频率与推理速度的可行技术方向。

**Tags**: `#harness`, `#eval`, `#orchestration`

---

<a id="item-agent-engineer-4"></a>
### [HF 每日论文：CSPD 可组合软提示蒸馏](https://huggingface.co/papers/2611.27376) ⭐️ 7.0/10

2026年11月24日Hugging Face每日论文收录了《Composable Soft-Prompt Distillation of RL Experts: Toward Continual Post-Training》一文，提出可组合软提示蒸馏（CSPD）方法，用于解决强化学习后训练领域专家的持续整合问题。该方法冻结预RL基座模型，将单个RL专家独立蒸馏为可训练的软提示，通过拼接即可组合多个专家，无需联合重训；在23个测试的智能体、代码、数学场景中，22个场景至少恢复教师模型90%的性能增益。当前公开内容截断，缺少多专家场景下的完整结果细节，相关结论的普适性待进一步验证。

rss · Hugging Face Daily Papers · Nov 24, 00:00

**「为什么重要」** 已公开的论文实证结果表明CSPD可规避传统权重合并、多教师策略蒸馏方法在新增专家时需全模型重训、易丢失非目标域能力的问题，对智能体后训练工作流有参考价值；但多专家场景的完整效果尚未公开，实际工程落地的兼容性仍需验证。

**「可关注」** 可关注：冻结基座模型、独立蒸馏软提示后拼接的组合范式，可降低RL专家持续整合时的重训开销与能力退化风险。

**Tags**: `#coding-agent`, `#eval`

---

<a id="item-agent-engineer-5"></a>
### [Microduck 避障 Sim2Real 教程发布](https://huggingface.co/blog/nvidia/microduck-obstacle-avoidance) ⭐️ 6.8/10

2026年11月24日Hugging Face官方博客发布Microduck机器人避障Sim2Real全流程教程，覆盖Isaac Lab控制器训练、Newton ToF传感建模、策略评估与真机部署全步骤。关键细节包括：复用已训练好的固定行走策略，单独训练避障控制器调整游戏手柄的速度指令；用SimReady资产生成随机障碍场地，ToF传感器建模匹配VL53L5CX参数并加入噪声、延迟、丢测量模拟真实传感误差；训练支持最多16384个并行仿真环境，也可在NVIDIA DGX Spark上用4096环境完成3000次PPO迭代。该教程面向Microduck机器人开发者与Sim2Real仿真从业者，提供可复现的分步操作指引。

rss · Hugging Face Blog · Nov 24, 16:34

**「为什么重要」** 这是目前公开的首份Microduck避障Sim2Real完整可复现教程，补齐了该细分场景的公开资料空白；目前尚未有公开证据证明该流程可直接复用到其他小型机器人平台。

**「可关注」** 可关注：教程提供了可调节并行度的Sim2Real训练配置，以及带噪声/丢包模拟的ToF传感器建模方案，可直接复用到同类型小型机器人仿真训练中。

**Tags**: `#eval`, `#sim2real`, `#robotics`, `#training`, `#deployment`

---

## AI Daily

<a id="item-ai-daily-1"></a>
### [GPT-6 展示蛋白质设计能力](https://openai.com/index/gpt-6-models-demonstrate-intrinsic-protein-design-capabilities) ⭐️ 9.8/10

OpenAI 官方博客宣布 GPT-6 模型具备蛋白质设计能力。模型通过推理和代码生成蛋白质结构与序列，实验室测试在五个靶点上观测到结合证据。

rss · OpenAI Blog · Nov 24, 13:00

**「为什么重要」** 这是 OpenAI 首次展示 GPT-6 在蛋白质设计方面的能力，实验室验证结果为大语言模型参与生物科学研究提供了实证基础。

**「可关注」** 可关注：模型通过推理与代码生成蛋白质结构及序列的设计路径，以及实验室对五个靶点结合活性的验证结果。

**Tags**: `#model`, `#lab`, `#industry`, `#product`

---

<a id="item-ai-daily-2"></a>
### [MCP 协议更新 扩展 Claude 交互能力](https://claude.com/resources/articles/skills-over-mcp-tasks-and-more) ⭐️ 8.8/10

Anthropic 宣布 MCP 协议多项更新，Claude 现已支持 Skills over MCP 公测版、Tasks 与 Elicitation 正式版，File Uploads 功能即将上线。当前 MCP 月 SDK 下载量超 7 亿次，Claude 平台已有超 1 万个 MCP 连接器，多服务器场景下工具搜索可降低超 85% 的上下文占用。功能限制方面：Skills over MCP 默认对 Pro、Max、Ultra 套餐开启，Team 套餐需管理员启用，Enterprise 支持即将上线；Tasks 与 Elicitation 目前仅面向 Pro、Max、Ultra 套餐及部分 Team、Enterprise 组织；File Uploads 即将面向符合条件的各套餐推出。

rss · Claude Blog · Nov 24, 00:00

**「为什么重要」** 这些更新让 Claude 与 MCP 服务器的交互更接近 agent 间协作，支持更长、更复杂的多步骤生产任务，同时通过工具搜索优化降低多服务器场景下的上下文开销，推动 MCP 标准在 agent 编排领域的落地。

**「可关注」** 可关注：开放 MCP 规范扩展的兼容性，支持 Skills over MCP、Tasks 等特性的服务器可在所有兼容客户端运行，无需绑定 Claude 生态。

**Tags**: `#model`, `#lab`, `#industry`, `#open-source`, `#product`

---

<a id="item-ai-daily-3"></a>
### [Claude Artifacts 上线 Install as app 测试功能](https://claude.com/resources/articles/install-as-app) ⭐️ 8.8/10

Claude官方宣布Artifacts功能新增“Install as app”beta特性，支持将Artifacts转为Mac和Windows独立桌面应用，应用拥有独立图标与窗口，可发送通知、添加菜单栏或系统托盘项，提供默认、应用权限、完全计算机访问三级权限管控，且随底层Artifacts编辑自动更新。该beta阶段全套餐可用，但HIPAA就绪组织、混合部署无法使用，Claude Docs、Slides、Sheets类Artifacts不支持安装；应用运行需保持在线登录Claude，向Claude发起的请求计入用户套餐用量限额，Team与Enterprise管理员可管控组织内应用权限开关。

rss · Claude Blog · Nov 24, 00:00

**「为什么重要」** 它将原本用于分享静态产出的Artifacts升级为可独立运行的日常工具，降低了知识工作者和开发者构建、维护轻量桌面应用的门槛。

**「可关注」** 可关注：安装的应用需保持在线登录Claude才可运行，每次应用更新后需重新申请权限，且仅支持对自制或组织内应用授予完全计算机访问权限，Anthropic不会预先审核第三方应用。

**Tags**: `#product`, `#lab`, `#industry`

---

<a id="item-ai-daily-4"></a>
### [Codex与Astra辅助发现潜在系外行星](https://openai.com/index/searching-for-distant-planets-with-astra) ⭐️ 6.8/10

OpenAI官方博客公开案例称，两名业余天文学家使用Codex与Astra工具，处理NASA开普勒与TESS望远镜的公开观测数据，发现了潜在系外行星。该案例未披露具体发现数量、行星参数及后续验证进展等细节。

rss · OpenAI Blog · Nov 24, 11:00

**「为什么重要」** 该案例是OpenAI官方公开的科研场景落地用例，验证了Codex与Astra在公开科研数据集处理上的可行性，拓展了工具的应用边界。

**「可关注」** 可关注Codex与Astra对公开天文观测数据集的适配能力，其已能支撑非专业群体开展相关数据分析任务。

**Tags**: `#lab`, `#product`, `#industry`

---

<a id="item-ai-daily-5"></a>
### [iFood 在 15,000 仓库部署编码代理](https://openai.com/business/customer-stories/ifood) ⭐️ 6.8/10

OpenAI 发布客户案例，披露 iFood 在 15,000 个代码仓库中部署编码代理。案例未公开具体技术架构、性能指标或成本数据，仅描述规模化应用场景。该材料属于营销案例，非技术发布或政策变更。

rss · OpenAI Blog · Nov 24, 00:00

**「为什么重要」** 这是目前公开的最大规模编码代理企业部署案例之一，为评估 AI 辅助开发的工业级落地提供了可量化的参考基准。

**「可关注」** 可关注：15,000 仓库规模下的编码代理部署模式，可作为企业内部推广 AI 编程工具的规模参考。

**Tags**: `#industry`, `#product`

---

<a id="item-ai-daily-6"></a>
### [Intentful dot Aria 自动化](https://openai.com/business/customer-stories/intentful-dots) ⭐️ 5.8/10

OpenAI 于 2026-11-24 发布客户案例，介绍 Intentful 使用 dot Aria 代理自动化网站研究与提案构建。该工具由 Marina Petrova 使用，可主动标记消息并自动解决问题。案例未披露技术架构、性能指标或部署规模。

rss · OpenAI Blog · Nov 24, 00:00

**「为什么重要」** 该案例提供 AI 代理在商业工作流中落地的行业参考，但技术细节有限，仅能作为行业采用观察。

**「可关注」** 可关注：AI 代理在研究与提案自动化场景中的实际应用，但需注意官方未提供实现细节。

**Tags**: `#industry`, `#product`, `#lab`

---

## AI Deals

<a id="item-ai-deals-1"></a>
### [Koofr 1TB 终身订阅 129.9美元 再开](https://www.appinn.com/koofr-1tb/) ⭐️ 8.0/10

你看到的内容可能由第三方 AI 基于小众软件文章提炼总结而成，可能与原文真实意图存在偏差。不代表小众软件观点和立场。请点击链接阅读原文细致比对和校验。Koofr云存储提供免费10GB基础存储空间，原生支持WebDAV与Rclone。2026年11月24日再次在Stacksocial平台上线1TB终身订阅促销，使用优惠码KOOFR可129.9美元购入，该渠道可享返利。

rss · 小众软件 · Nov 24, 03:24

**「为什么重要」** 该优惠为多次限时回归的促销，Koofr原生支持Rclone与WebDAV，适配服务器备份、跨平台文件同步需求，免费10GB额度可先试用再决定是否购买终身版。

**「可关注」** 可关注：使用Rclone可直接对接Koofr，适合需要低成本备份服务器小文件的场景，免费版文件分享功能有10次限制。

**Tags**: `#free-tier`, `#promo`, `#coupon`

---

<a id="item-ai-deals-2"></a>
### [Show HN: Upronix 免费 uptime 监控工具](https://upronix.dev/) ⭐️ 5.0/10

Hacker News user slxca announced Upronix, a free uptime monitoring and visual status page builder, in a Show HN post. The provided source content does not disclose specific free tier details including quota, usage limits, or expiration date.

rss · HN Free API / Credits · Nov 24, 18:28

**「为什么重要」** No concrete free tier terms are public yet, making it a low-detail but valid lead for developers with uptime monitoring or self-hosted status page needs to track for future official quota announcements.

**「可关注」** 可关注：Upronix&\#x27;s upcoming free tier quota and usage limits, which are not yet confirmed to meet production monitoring needs.

**Tags**: `#free-tier`, `#promo`

---