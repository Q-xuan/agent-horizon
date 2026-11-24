---
layout: default
title: "Horizon Summary: 2026-11-25 (ZH)"
date: 2026-11-25
lang: zh
---

> 从 218 条内容中筛选出 16 条重要资讯。

<nav id="ah-toc" class="ah-toc" aria-label="目录"><span class="ah-toc-title">目录</span><ul><li><a href="#sec-harness-arch"><span class="ah-toc-name">Harness 架构</span><span class="ah-toc-count">3条</span></a></li><li><a href="#sec-agent-engineer"><span class="ah-toc-name">Agent 工程师日报</span><span class="ah-toc-count">5条</span></a></li><li><a href="#sec-ai-daily"><span class="ah-toc-name">AI 日报</span><span class="ah-toc-count">6条</span></a></li><li><a href="#sec-ai-deals"><span class="ah-toc-name">AI 羊毛</span><span class="ah-toc-count">2条</span></a></li></ul></nav>

---

**[Harness 架构](#sec-harness-arch)**
1. [Codex CLI rust-v0.172.0 发布](#item-harness-arch-1) ⭐️ 8.8/10
2. [pydantic-ai v2.73.0 发布](#item-harness-arch-2) ⭐️ 7.8/10
3. [gemini-cli v0.71.0-nightly 发布](#item-harness-arch-3) ⭐️ 6.8/10

**[Agent 工程师日报](#sec-agent-engineer)**
1. [Cognition 发布 SWE-2.1](#item-agent-engineer-1) ⭐️ 8.8/10
2. [Embo-Harness 研究 frontier-model-as-policy harness](#item-agent-engineer-2) ⭐️ 7.0/10
3. [AutoPILOT 解耦实时游戏 Agent 动作频率](#item-agent-engineer-3) ⭐️ 7.0/10
4. [HF 每日论文：CSPD 蒸馏 RL 专家](#item-agent-engineer-4) ⭐️ 7.0/10
5. [Microduck 避障 Sim2Real 教程发布](#item-agent-engineer-5) ⭐️ 6.8/10

**[AI 日报](#sec-ai-daily)**
1. [GPT-6 模型具备内在蛋白质设计能力](#item-ai-daily-1) ⭐️ 9.8/10
2. [MCP 新增 Skills 与任务能力](#item-ai-daily-2) ⭐️ 8.8/10
3. [Claude Artifacts 支持转 Mac/Windows 桌面应用](#item-ai-daily-3) ⭐️ 8.8/10
4. [Codex 与 Astra 辅助发现潜在系外行星](#item-ai-daily-4) ⭐️ 6.8/10
5. [iFood 大规模部署编码 agent](#item-ai-daily-5) ⭐️ 6.8/10
6. [OpenAI 发布 Intentful dot Aria 落地案例](#item-ai-daily-6) ⭐️ 5.8/10

**[AI 羊毛](#sec-ai-deals)**
1. [Koofr 1TB 终身 129.99 美元](#item-ai-deals-1) ⭐️ 8.0/10
2. [Upronix 免费 uptime 监控工具发布](#item-ai-deals-2) ⭐️ 5.0/10

---

## Harness 架构
{: #sec-harness-arch .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-harness-arch" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-harness-arch-1"></a>
### [Codex CLI rust-v0.172.0 发布](https://github.com/openai/codex/releases/tag/rust-v0.172.0) ⭐️ 8.8/10

OpenAI Codex CLI 发布 rust-v0.172.0，带来 MCP 服务器延迟加载、沙盒状态恢复、细粒度工具审批配置及嵌套代理线程导航。本次更新覆盖运行时行为、权限模型和远程会话一致性，包含 60 余项 PR。

github · github-actions\[bot\] · 11月24日 00:03

**「设计要点」** Code Mode 全面切换至 gRPC 主机连接，原 \`code\_mode\_host\_grpc\` 配置项弃用。MCP 工具审批状态持久化到配置层快照，支持跨重启保留。

**「改了什么」** 可选 stdio MCP 服务器默认改为首次工具调用时延迟启动并缓存工具列表（\#62366）。\`codex exec resume\` 恢复保存的沙盒权限、工作目录和工作区根目录（\#62194），并支持为单个 app 工具设置审批审查者（\#62360）；终端内可通过线程链接打开嵌套代理对话（\#62332），远程会话跨操作系统保持工作目录与可写路径（\#62375-62377）。

**标签**: `#mcp`, `#sandbox`, `#permissions`, `#subagents`, `#runtime`

---

<a id="item-harness-arch-2"></a>
### [pydantic-ai v2.73.0 发布](https://github.com/pydantic/pydantic-ai/releases/tag/v2.73.0) ⭐️ 7.8/10

pydantic-ai v2.73.0 发布。\`Agent.override\` 新增 \`capabilities\` 参数，同时导出 \`AgentInstructions\` 和 \`SourcedInstruction\` 类型。\`RealtimeSession.append\_voice\_instructions\` 支持 GPT-Live 语音模型。新增 \`DeprecatedModelWarning\`，在请求目标为 Anthropic 或 OpenAI 已废弃模型时发出警告。OpenAI Responses 的 \`input\_transformations\` 暴露在 \`provider\_details\` 和模型请求 span 中。\`openai\` 依赖底线从 3.31.0 提升至 3.50.0。私有 \`Agent.\_override\_root\_capability\` 上下文变量结构改为 \`\(capability, injected\)\` 元组，直接读取该变量的代码需要更新。

github · dsfaccini · 11月24日 03:53

**「设计要点」** agent 框架通过上下文变量管理能力注入，\`provider\_details\` 承载缓存与转换细节，\`RealtimeSession\` 扩展实时语音能力。

**「改了什么」** \`Agent.override\` 新增 \`capabilities\` 配置，导出 \`AgentInstructions\` 和 \`SourcedInstruction\`。\`RealtimeSession.append\_voice\_instructions\` 支持 GPT-Live 语音模型。废弃模型请求触发 \`DeprecatedModelWarning\`。OpenAI Responses 的 \`input\_transformations\` 暴露在 \`provider\_details\` 和模型请求 span。\`openai\` 依赖底线提升至 3.50.0。私有 \`Agent.\_override\_root\_capability\` 上下文变量结构改为 \`\(capability, injected\)\` 元组，属破坏性变更。

**标签**: `#runtime`, `#tools`, `#permissions`, `#prefix-cache`

---

<a id="item-harness-arch-3"></a>
### [gemini-cli v0.71.0-nightly 发布](https://github.com/google-gemini/gemini-cli/releases/tag/v0.71.0-nightly.20261124.gaafdfdfb5) ⭐️ 6.8/10

gemini-cli 官方 nightly 版本 v0.71.0.20261124 发布，单一修复 A2A server 组件，强制执行 bearer token 认证与请求输入验证。该变更面向 agent 互操作场景，非重大架构更新，对多数 harness 架构师优先级不高。

github · gemini-cli-robot · 11月24日 01:13

**「改了什么」** A2A server 组件新增 bearer token 认证强制与请求输入验证，关闭未认证访问与非法输入请求。

**标签**: `#a2a`, `#permissions`, `#runtime`

---

## Agent 工程师日报
{: #sec-agent-engineer .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-agent-engineer" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-agent-engineer-1"></a>
### [Cognition 发布 SWE-2.1](https://cognition.ai/blog/swe-2-1) ⭐️ 8.8/10

2026 年 11 月 24 日 Cognition 发布 SWE-2.1，是其编码智能体模型 SWE-2 的纯强化学习升级版本，基于 Kimi K3 训练，官方自报在 FrontierCode 2.0、Terminal-Bench 4.1 等编码基准，以及 ExploitBench（80%得分）、ExploitGym（27.3%旗标捕获率）等网络安全基准有显著提升。训练过程中通过扩展长短时程任务覆盖、优化训练后算法控制 rollout 长度震荡，实现稳定长周期训练，测试时计算扩展曲线斜率较基座模型明显提升。同步推出面向网络防御的 SWE-2.1 Cyber（已上线 Devin Security）和 10 倍推理加速的 SWE-2.1 Ultrafast；SWE-2.1 在 Devin Desktop 与 CLI 免费使用至 2026 年 12 月 8 日，全版本（含 Devin Desktop、Cloud、CLI）付费折扣持续至 2026 年 1 月 30 日。所有网络安全基准跑分均基于 Muse Wonder Full 版本，ExploitGym 测试关闭了缓解措施，编码基准跑分采用 Devin CLI harness，跑分结果未经过第三方独立验证。

rss · Cognition Blog · 11月24日 16:00

**「为什么重要」** 已发生的变化是 Cognition 首次将编码模型的强化学习训练收益明确延伸到网络安全攻防场景，同时通过长时程训练优化提升了复杂任务的自主完成能力；尚未证实的影响包括其宣称的测试时计算扩展收益是否能在其他编码场景复现，以及宽松防护的 Cyber 版本是否存在潜在滥用风险。

**「可关注」** 可关注：SWE-2.1 通过优化训练后算法减少 rollout 长度震荡，实现了从分钟级到小时级任务的稳定长周期训练，该训练方案对长时程编码智能体的研发有参考价值。

**标签**: `#coding-agent`, `#eval`

---

<a id="item-agent-engineer-2"></a>
### [Embo-Harness 研究 frontier-model-as-policy harness](https://huggingface.co/papers/2611.31201) ⭐️ 7.0/10

2026-11-24，Hugging Face Daily Papers 发布 Embo-Harness 框架研究摘要，获 90 个 upvote。该框架系统研究 frontier-model-as-policy 的机器人智能体 harness，调查 prompting、planning、action execution、tool use 四个核心组件，提炼六项实证发现。研究提出设计配方，优先利用模型原生视觉推理与工具使用能力，而非手工制作的计划、技能或动作先验。摘要文本被截断，完整论文内容未提供。该研究虽以机器人为场景，但作者声称其对更广泛的 agent 工程工作具有可推广性。

rss · Hugging Face Daily Papers · 11月24日 00:00

**「为什么重要」** 该研究提供了基于实证的 harness 设计原则，直接挑战依赖手工 agent 组件的传统做法。其主张优先调用模型原生能力而非外部编排，对优化 coding agent 与工具链工作流有潜在参考价值。

**「可关注」** 可关注：研究显示 harness 设计应优先利用模型原生视觉推理与工具使用能力，而非依赖手工制作的计划、技能或动作先验。

**标签**: `#harness`, `#orchestration`, `#tool-use`

---

<a id="item-agent-engineer-3"></a>
### [AutoPILOT 解耦实时游戏 Agent 动作频率](https://huggingface.co/papers/2611.28202) ⭐️ 7.0/10

Hugging Face Daily Papers 于 2026-11-24 介绍 AutoPILOT 研究论文。该论文提出面向实时游戏的视觉 agent harness，解耦 agent 动作频率与模型推理速度：每次模型调用可发送原始动作、启动开环宏，或编写无需额外模型调用的闭环控制器。配套 AFK-Bench 基准包含 120 款浏览器游戏，用于评估实时游戏 agent。该工作为研究预印本，非生产就绪工具。

rss · Hugging Face Daily Papers · 11月24日 00:00

**「为什么重要」** 实时游戏要求 agent 在环境持续运行时响应，现有 harness 将动作频率绑定模型推理速度。AutoPILOT 在 harness 层提供解耦方案，为实时交互设计提供参考，但生产落地效果尚未证实。

**「可关注」** 可关注：harness 对实时 agent 性能的影响，特别是动作调度与模型推理解耦的设计模式。

**标签**: `#harness`, `#eval`, `#orchestration`

---

<a id="item-agent-engineer-4"></a>
### [HF 每日论文：CSPD 蒸馏 RL 专家](https://huggingface.co/papers/2611.27376) ⭐️ 7.0/10

2026 年 11 月 24 日 Hugging Face 每日论文收录了一篇提出 Composable Soft-Prompt Distillation（CSPD）方法的论文，针对 RL 后训练产生的领域专家持续整合需求，该方案冻结预 RL 模型，将单个 RL 专家独立蒸馏为可训练的软提示，通过拼接即可组合多个专家能力，无需联合重训。在 23 个覆盖智能体、代码、数学的测试场景中，该方法在 22 个场景里至少恢复了教师模型 90%的性能增益。当前提供的论文内容存在截断，多专家场景的完整实验结果未披露。

rss · Hugging Face Daily Papers · 11月24日 00:00

**「为什么重要」** 该方法针对 RL 后训练专家持续整合的现有痛点——现有权重合并、多教师策略蒸馏（MOPD）方案每次新增专家都需重训整个模型，还可能损害域外能力——提供了无需重训整个模型即可组合多专家能力的可行路径，相关实验覆盖智能体、代码、数学场景，与 AI Agent 后训练工作流直接相关。但多专家场景的完整效果尚未披露，实际落地价值还需完整论文验证。

**「可关注」** 可关注：冻结基座+独立蒸馏软提示的组合方案，可在避免全模型重训的前提下保留 RL 后训练的大部分性能增益，但多专家场景下的实际效果与开销还需完整论文披露。

**标签**: `#coding-agent`, `#eval`

---

<a id="item-agent-engineer-5"></a>
### [Microduck 避障 Sim2Real 教程发布](https://huggingface.co/blog/nvidia/microduck-obstacle-avoidance) ⭐️ 6.8/10

2026 年 11 月 24 日 Hugging Face 发布 Microduck 机器人避障 Sim2Real 全流程教程，基于开源 Isaac Lab 完成避障控制器训练、Newton 完成物理与 ToF 传感建模，覆盖仿真训练、策略评估、ONNX 导出与真机部署全步骤。关键细节包括：复用固定权重的行走策略，单独训练 50Hz 运行的避障控制器调整游戏手柄的速度指令；仿真建模 VL53L5CX ToF 传感器（8×8 测距网格、15Hz 更新率、45°视场角、0.12-4m 量程），并加入噪声、延迟、缺失测量匹配真实硬件；训练默认使用 16384 个并行仿真环境跑 1500 次 PPO 迭代，也可在 NVIDIA DGX Spark 上用 4096 个并行环境跑 3000 次迭代完成。该教程面向小型机器人 Sim2Real 开发场景，通用性有限。

rss · Hugging Face Blog · 11月24日 16:34

**「为什么重要」** 该教程提供了 Microduck 避障场景的端到端可复现步骤，对小型机器人 Sim2Real 开发有直接参考价值，但场景聚焦特定硬件与细分任务，通用性有限，多数非机器人领域的 AI Agent 工程师无需跟进。

**「可关注」** 可关注：Sim2Real 流程中传感器建模加入噪声、延迟、缺失测量以匹配真实硬件特性，且并行训练环境数量可根据 GPU 内存灵活调整，低配环境需增加迭代次数。

**标签**: `#eval`, `#sim2real`, `#robotics`, `#training`, `#deployment`

---

## AI 日报
{: #sec-ai-daily .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-daily" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-daily-1"></a>
### [GPT-6 模型具备内在蛋白质设计能力](https://openai.com/index/gpt-6-models-demonstrate-intrinsic-protein-design-capabilities) ⭐️ 9.8/10

OpenAI 官方博客宣布 GPT-6 模型具备内在蛋白质设计能力，可通过推理与代码生成蛋白质结构与序列。实验室测试验证其在 5 个靶点上存在结合证据。当前公开信息未披露具体性能指标、设计成功率及后续落地规划。

rss · OpenAI Blog · 11月24日 13:00

**「为什么重要」** 这是 GPT 系列首次公开验证具备蛋白质设计这类专业科研能力，拓展了大模型在生物医药领域的应用边界。

**「可关注」** 可关注：GPT-6 通过推理与代码完成蛋白质设计的能力泛化路径，以及实验室验证的重复性与可复现性细节。

**标签**: `#model`, `#lab`, `#industry`, `#product`

---

<a id="item-ai-daily-2"></a>
### [MCP 新增 Skills 与任务能力](https://claude.com/resources/articles/skills-over-mcp-tasks-and-more) ⭐️ 8.8/10

Anthropic 宣布 Model Context Protocol（MCP）协议能力升级：Skills over MCP 进入公开测试版，Tasks 与 Elicitation 正式普遍可用，File Uploads 功能即将推出。当前 MCP 月 SDK 下载量超 7 亿，Claude 平台已有超 1 万个 MCP 连接器；规范还完成工具搜索按需加载、无状态化、企业级授权等优化，多服务器场景下工具上下文占用可降低超 85%。新能力默认面向 Claude Pro、Max、Ultra 套餐开放，Team 与 Enterprise 套餐正在逐步 rollout，所有更新均属于开放 MCP 规范扩展，兼容全生态支持该规范的客户端。

rss · Claude Blog · 11月24日 00:00

**「为什么重要」** MCP 是当前 AI agent 生态的核心连接标准，本次更新补齐了长任务执行、中途用户交互、文件传输等生产级所需能力，且开放规范特性可覆盖全生态客户端，能降低 agent 编排与系统对接的开发成本。

**「可关注」** 可关注：MCP 开放规范的 Skills over MCP、Tasks、Elicitation 已进入公测/GA 阶段，File Uploads 即将上线，可优先适配这些能力以支持更长流程的 agent 任务。

**标签**: `#model`, `#lab`, `#industry`, `#open-source`, `#product`

---

<a id="item-ai-daily-3"></a>
### [Claude Artifacts 支持转 Mac/Windows 桌面应用](https://claude.com/resources/articles/install-as-app) ⭐️ 8.8/10

Claude 官方宣布 artifacts 功能新增「Install as app」beta 特性，支持将 artifacts 转为 Mac 和 Windows 独立桌面应用。安装后的应用拥有独立图标与窗口，可分享给其他用户，需获得用户授权才能与电脑交互，且会随底层 artifacts 编辑自动更新，调用 Claude 的额度计入用户套餐用量限制。该 beta 功能全套餐可用，但 HIPAA 合规组织、混合部署场景无法使用，Claude Docs、Slides、Sheets 类 artifacts 不支持安装；Team 版默认开启该功能、全电脑访问权限默认关闭，Enterprise 版需所有者手动开启，打开应用需联网登录 Claude 账号。

rss · Claude Blog · 11月24日 00:00

**「为什么重要」** 该功能降低了自定义桌面工具的搭建门槛，用户无需打包、签名或配置 API 密钥即可快速将日常使用的 artifacts 转为独立应用，同时分级权限机制兼顾了使用便利性与系统安全。

**「可关注」** 可关注：安装应用提供三级权限管控，默认仅浏览器级权限，应用可申请置顶窗口、全局快捷键、通知等权限；全电脑访问权限仅允许授予本人或组织内成员开发的应用，Anthropic 不会预先审核上架应用，若应用包含第三方网站组件，该组件更新无需重新授权，其余更新均会重新触发授权请求。

**标签**: `#product`, `#lab`, `#industry`

---

<a id="item-ai-daily-4"></a>
### [Codex 与 Astra 辅助发现潜在系外行星](https://openai.com/index/searching-for-distant-planets-with-astra) ⭐️ 6.8/10

OpenAI 官方博客发布案例称，两名业余天文学家使用 Codex 与 Astra 工具，处理 NASA 开普勒、TESS 望远镜的公开数据，发现了潜在系外行星。

rss · OpenAI Blog · 11月24日 11:00

**「为什么重要」** 该案例展示了 Codex 与 Astra 在科研公开数据处理场景的可用性，拓展了工具的非专业领域应用边界。

**「可关注」** 可关注：Codex 与 Astra 可适配公开天文数据集的标准化处理流程，辅助非专业用户开展科研类数据挖掘。

**标签**: `#lab`, `#product`, `#industry`

---

<a id="item-ai-daily-5"></a>
### [iFood 大规模部署编码 agent](https://openai.com/business/customer-stories/ifood) ⭐️ 6.8/10

OpenAI 发布官方客户案例，披露餐饮平台 iFood 已在 15000 个代码仓库部署编码 agent，属于大规模企业级 AI 辅助开发落地实践。

rss · OpenAI Blog · 11月24日 00:00

**「为什么重要」** 该案例提供了编码 agent 企业级大规模落地的可验证样本，可参考其跨多仓库统一部署的实践路径。

**「可关注」** 可关注企业级场景下编码 agent 跨多仓库统一部署的落地模式。

**标签**: `#industry`, `#product`

---

<a id="item-ai-daily-6"></a>
### [OpenAI 发布 Intentful dot Aria 落地案例](https://openai.com/business/customer-stories/intentful-dots) ⭐️ 5.8/10

OpenAI 官方发布客户案例，介绍 Intentful 使用 dot Aria 代理自动化网站研究、提案搭建、消息标记与问题解决流程。该案例未披露具体效率提升数值，也未公开 dot Aria 的技术实现细节。

rss · OpenAI Blog · 11月24日 00:00

**「为什么重要」** 这是可验证的 AI 代理企业落地采用案例，可佐证该类工具在商业流程自动化场景的可行性。

**「可关注」** 可关注：dot Aria 已落地研究、提案、客服类企业流程自动化场景，可作为同类 coding agent 的落地参考。

**标签**: `#industry`, `#product`, `#lab`

---

## AI 羊毛
{: #sec-ai-deals .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-deals" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-deals-1"></a>
### [Koofr 1TB 终身 129.99 美元](https://www.appinn.com/koofr-1tb/) ⭐️ 8.0/10

你看到的内容可能由第三方 AI 基于小众软件文章提炼总结而成，可能与原文真实意图存在偏差。不代表小众软件观点和立场。请&lt;a href=&quot;https://www.appinn.com/koofr-1tb/&quot; target=&quot;\_blank&quot;&gt;点击链接阅读原文&lt;/a&gt;细致比对和校验。&lt;br /&gt;&lt;br /&gt;Koofr 云存储提供免费 10GB 基础存储空间，支持 WebDAV、Rclone。用户可通过 Stacksocial 平台使用优惠码 KOOFR 以 129.99 美元购入 1TB 终身订阅，该优惠 2026 年 11 月 24 日再次上线。

rss · 小众软件 · 11月24日 03:24

**「为什么重要」** 该服务原生支持 Rclone 与 WebDAV，适配服务器备份、跨云迁移等开发者常用场景，1TB 终身订阅价格低于官网年付档位，免费 10GB 额度可先试用再决策。

**「可关注」** 可关注：使用 Rclone 备份小文件场景时，Koofr 原生支持可直接对接，免费 10GB 额度可先测试同步稳定性。

**标签**: `#free-tier`, `#promo`, `#coupon`

---

<a id="item-ai-deals-2"></a>
### [Upronix 免费 uptime 监控工具发布](https://upronix.dev/) ⭐️ 5.0/10

Show HN 用户 slxca 发布免费 uptime 监控与可视化状态页构建工具 Upronix，当前公开内容未披露免费层的具体额度、使用限制、有效期等信息。

rss · HN Free API / Credits · 11月24日 18:28

**「为什么重要」** 目前公开信息未披露免费层具体规则，适合有轻量 uptime 监控与状态页搭建需求的开发者先做初步试用。

**「可关注」** 可关注：该工具暂无公开免费层细则，使用前建议先确认监控频率、状态页自定义能力、数据留存等限制条件。

**标签**: `#free-tier`, `#promo`

---