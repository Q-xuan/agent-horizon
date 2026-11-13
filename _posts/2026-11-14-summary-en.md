---
layout: default
title: "Horizon Summary: 2026-11-14 (EN)"
date: 2026-11-14
lang: en
---

> From 205 items, 18 important content pieces were selected

---

**Agent Harness Architecture**
1. [Mastra core 1.83.0 发布](#item-harness-arch-1) ⭐️ 8.8/10
2. [FastMCP v4.2.0 发布](#item-harness-arch-2) ⭐️ 7.8/10
3. [OpenCode v2.3.0 发布](#item-harness-arch-3) ⭐️ 7.8/10
4. [Cloudflare Kitesurf 开源发布](#item-harness-arch-4) ⭐️ 7.8/10

**AI Agent Engineer**
1. [XYBench 评测基准发布](#item-agent-engineer-1) ⭐️ 7.8/10
2. [llama.cpp v1.0.0 发布](#item-agent-engineer-2) ⭐️ 7.8/10
3. [长程智能体决策模型角色研究](#item-agent-engineer-3) ⭐️ 7.0/10
4. [Anthropic 发布安全评估构建指南](#item-agent-engineer-4) ⭐️ 6.8/10
5. [具身智能体评估存在验证器过拟合风险](#item-agent-engineer-5) ⭐️ 6.0/10
6. [Qwen3 DSpine 模型登 HF 榜](#item-agent-engineer-6) ⭐️ 6.0/10
7. [SimReady 资产构建机器人拾放模拟](#item-agent-engineer-7) ⭐️ 5.8/10
8. [SO-Arena 基准测试发布](#item-agent-engineer-8) ⭐️ 5.5/10

**AI Daily**
1. [ChatGPT Wallet 正式上线](#item-ai-daily-1) ⭐️ 8.8/10
2. [DeepSeek 全家桶应用 API 发布](#item-ai-daily-2) ⭐️ 8.8/10
3. [Claude Tag 创业公司使用指南发布](#item-ai-daily-3) ⭐️ 5.8/10

**AI Deals**
1. [Epic 11.13-19 免费领《斗阵骑士》](#item-ai-deals-1) ⭐️ 8.0/10
2. [World Labs Atlas开放 注册赠10000积分](#item-ai-deals-2) ⭐️ 8.0/10
3. [InstaBox 免费 4核8GB 云电脑](#item-ai-deals-3) ⭐️ 7.0/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [Mastra core 1.83.0 发布](https://github.com/mastra-ai/mastra/releases/tag/%40mastra/core%401.83.0) ⭐️ 8.8/10

Mastra 发布 @mastra/core@1.83.0，核心新增三项架构能力：全量 Agent 可恢复运行流（带重放缓存与跨实例 observe/abort 控制）、内置 MCP 服务器端点（/api/mcp，支持 OAuth 发现）、以及实验性工作流存储 V2（delta 写入，支持 Postgres 与 libSQL）。此外，AI SDK 聊天路由支持断点续传，调度器新增一次性与 bounded 周期执行。破坏性变更：Agent 的 durable 选项现仅控制可恢复流，不再提供 checkpoint 支持的持久执行，需迁移至 createDurableAgent。

github · PaulieScanlon · Nov 13, 14:32

**「设计要点」** 可恢复流通过 replay cache 与 ownership/TTL 实现跨实例 observe/abort，断线重连不终止运行。内置 MCP 服务器通过 server.mcp.oauth 配置 OAuth 发现与 audience 校验，CompositeAuth 聚合多提供方授权服务器；工作流存储 V2 采用 per-step delta 写入与异步 steps\(\) 延迟加载，降低长循环 I/O。

**「改了什么」** 全量 Agent 获得可恢复流能力（此前仅 durable Agent 支持），Agent.durable 语义收窄为仅控制可恢复流，checkpoint 持久执行迁移至 createDurableAgent。新增 /api/mcp 内置端点与 OAuth 发现、工作流存储 V2 支持 Postgres/libSQL、chatRoute\(\{ resumable: true \}\) 及 runAt/endAt 调度。

**Tags**: `#runtime`, `#mcp`, `#tools`, `#storage`

---

<a id="item-harness-arch-2"></a>
### [FastMCP v4.2.0 发布](https://github.com/PrefectHQ/fastmcp/releases/tag/v4.2.0) ⭐️ 7.8/10

FastMCP v4.2.0 发布，将 Skill 实现为 MCP 服务器可提供的一等公民。Skill 是包含 name、description、instructions 和 files 的纯值对象，支持从目录、包加载或代码构建，通过 SkillCatalogProvider 或 SkillsDirectoryProvider 提供，客户端通过实验性 Skills 扩展的 skills/list 端点获取带哈希清单的技能列表。FastMCP 客户端新增 Client.read\_skill\(\) 验证文件摘要、to\_directory\(\) 安装技能到任意 agent 的 skills 目录，且 Skills 已接入 mounts、proxies、ClientGroup 和 AuthMiddleware 等组合模式。依赖注解升级支持 Annotated\[dict, Depends\(get\_config\)\] 及 CallArgument 拥有工具参数。该版本要求 Python 3.11+，4.1 Skills API 已弃用并将于 4.3 移除。

github · zzstoatzz · Nov 13, 17:07

**「设计要点」** Skills 以资源形式通过 SkillCatalogProvider 和 SkillsDirectoryProvider 提供，客户端依赖实验性 Skills 扩展的 skills/list 端点发现技能。FastMCP 客户端通过 Client.read\_skill\(\) 与 to\_directory\(\) 补足第三方客户端支持缺口，Skills 同时接入 mounts、proxies、ClientGroup 和 AuthMiddleware 等组合模式。

**「改了什么」** Skill 成为服务器可提供的一等对象，新增 Skill 纯值模型、SkillsDirectoryProvider、Client.read\_skill\(\) 与 to\_directory\(\)，旧版 4.1 skills API 已弃用并将于 4.3 移除，作者类 Skill 对应的传输模型更名为 MCPSkill。依赖注解支持 Annotated 注入和 CallArgument 参数归属，同时要求 Python 3.11+ 并完成大量 OpenAPI、代理、认证、遥测修复。

**Tags**: `#mcp`, `#tools`, `#permissions`

---

<a id="item-harness-arch-3"></a>
### [OpenCode v2.3.0 发布](https://github.com/anomalyco/opencode/releases/tag/v2.3.0) ⭐️ 7.8/10

OpenCode v2.3.0 将后台子代理设为默认运行时行为：子代理立即返回会话 ID 并在后台继续执行，空闲时向父会话报告结果，支持父会话与多个子代理并发工作。TUI 默认启用低详细度模式，将工具调用和思考过程折叠为单行可折叠活动记录，用户可通过 \`session.verbosity\` 配置调整。桌面端新增 \`Cmd+Alt+G\` / \`Ctrl+Alt+G\` 跳转功能，支持跨当前会话搜索并跳转到历史提示。此外，该版本实验性支持 \`mcp\_events\` 和 \`shell\_timeout\_background\` 标志，以及 LM Studio 决策模型和客户端证书双向 TLS 配置。

github · github-actions\[bot\] · Nov 13, 08:55

**「设计要点」** 子代理运行时从同步阻塞改为默认异步后台执行，立即返回会话 ID 并通过空闲报告向父会话传递结果，改变父会话与子代理的并发交互模型。TUI 采用折叠活动行渲染转录内容，Shell 命令执行层引入进程守护进程并支持超时后台迁移，同时实验性支持 MCP 事件和客户端证书双向 TLS。

**「改了什么」** 默认后台子代理替代同步子代理执行，支持父会话与子代理并发工作。TUI 转录详细度默认降为低，采用可折叠活动行；桌面端新增消息跳转导航。实验性标志 \`mcp\_events\` 与 \`shell\_timeout\_background\` 分别启用 MCP 事件流和 shell 超时后台迁移，同时新增 LM Studio 决策模型支持和客户端证书双向 TLS 配置。

**Tags**: `#subagents`, `#runtime`, `#memory`

---

<a id="item-harness-arch-4"></a>
### [Cloudflare Kitesurf 开源发布](https://blog.cloudflare.com/kitesurf-open-source/) ⭐️ 7.8/10

Cloudflare 正式开源专为 AI agent 设计的无状态浏览器 Kitesurf，该工具完全运行在 Cloudflare Workers 上，支持 Chrome DevTools Protocol（CDP）与 WebMCP 协议，无需浏览器容器即可完成 HTML 解析、CSS 应用、JavaScript 执行与截图渲染，采用 Apache 2.0 许可，开发者可本地运行或部署到自有 Cloudflare 账户，部署需使用 Workers 付费计划。

rss · Cloudflare AI · Nov 13, 20:20

**「设计要点」** 运行时完全基于 Cloudflare Workers，核心逻辑用 Rust 编写并编译为 WebAssembly，依赖 Blitz、Stylo、Boa 等开源组件分别承担 HTML 解析与渲染、CSS 处理、JavaScript 执行能力，通过 Dynamic Workers 为每个页面创建隔离运行环境，对外提供 CDP 接口兼容 Puppeteer 等客户端。

**「改了什么」** 本次正式开源，开发者可克隆仓库本地运行、修改代码，也可部署到自有 Cloudflare 账户使用，此前仅提供 Browser Run 托管 API 调用。

**Tags**: `#tools`, `#runtime`, `#mcp`, `#sandbox`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [XYBench 评测基准发布](https://huggingface.co/blog/allenai/xybench) ⭐️ 7.8/10

2026年11月13日，Allen AI 联合 CMU、NVIDIA、JHU 发布 XYBench 评测基准，包含 8115 个跨编程、烹饪、家装等场景的真实问题，用于评估 AI 助手识别用户基于误解的 XY 问题、优先解决底层真实诉求的能力，该基准获 EMNLP 2026 最佳资源论文奖。测试的 Claude Sonnet 4.6、GPT-5、Gemini 3.1 Pro、Qwen3.5-9B、DeepSeek-V4 Pro 五个模型均更倾向解决用户表面提出的错误请求，而非底层真实目标；人类参考答案在误解识别维度表现优于所有模型。当前 XYBench 仅覆盖英语查询，且问题以程序性场景为主。

rss · Hugging Face Blog · Nov 13, 17:02

**「为什么重要」** XYBench 首次标准化评测 LLM 处理 XY 问题的能力，填补了该方向的空白，已发布的评测结果可直接用于对比不同模型的意图识别与纠错表现。目前尚未有公开证据证明基于该基准优化的训练或提示词方法能真正提升模型将推断出的用户真实意图落地为回复重点的能力。

**「可关注」** 可关注：XYBench 将 XY 问题处理拆解为「误解识别」和「真实诉求优先」两个独立评测维度，当前模型存在「能判断正确方案但生成回复时仍聚焦错误请求」的明显 gap，且显式提供用户真实意图反而会降低模型的误解识别率。

**Tags**: `#eval`, `#benchmark`, `#xy-problem`, `#agent-evaluation`, `#huggingface`

---

<a id="item-agent-engineer-2"></a>
### [llama.cpp v1.0.0 发布](https://huggingface.co/blog/ggml-org/llama-cpp-v1) ⭐️ 7.8/10

2026年11月13日，Hugging Face发布llama.cpp v1.0.0与配套ggml v1.0.0，前者为C/C++实现的多模态本地LLM推理库，后者为机器学习张量库。项目明确采用语义版本控制规则：公开C API的破坏性变更触发主版本号 bump，向后兼容的功能、后端更新、模型支持或API新增触发次版本号 bump，仅bug修复触发修订版本号 bump。当前llama.cpp已支持150+架构变体与所有主流推测解码方法，分发渠道覆盖Linux、macOS、Windows、Android、iOS等平台的预发布制品、Docker、Debian、Homebrew、conda-forge、MacPorts、Winget、XCFramework，同时上线Llama桌面应用降低本地AI使用门槛。

rss · Hugging Face Blog · Nov 13, 14:05

**「为什么重要」** 这是llama.cpp项目启动3.5年来的首个稳定大版本，首次明确公开API与ABI的兼容性边界规则，对依赖该库构建本地AI应用、agent工具链的下游开发者有直接约束意义；配套桌面应用进一步降低了本地AI的部署门槛。

**「可关注」** 可关注：llama.cpp v1.0.0 起公开C API的破坏性变更会触发主版本号 bump，下游集成需适配新的版本边界规则。

**Tags**: `#harness`

---

<a id="item-agent-engineer-3"></a>
### [长程智能体决策模型角色研究](https://huggingface.co/papers/2611.17167) ⭐️ 7.0/10

这篇 2026-11-13 发布的论文（arXiv:2611.17167）研究长程智能体中决策模型的演员、裁判与教师角色。实验在 ALFWorld 上对比三种决策模型与三种通用 LLM 的执行与评判表现，并在 ALFWorld 与 WebShop 上验证 JEV 作为教师的效果。结果显示，执行能力较差的模型仍能有效训练策略；对单步动作的有用性判断优于对完整轨迹的评估。所有模型在执行时均会被更易的子目标干扰，偏离必须优先完成的子目标。

rss · Hugging Face Daily Papers · Nov 13, 00:00

**「为什么重要」** 该研究证明决策模型的评判与教学能力可独立于执行能力，为智能体评估与训练流程设计提供新维度。实验在标准基准上的对比结果可直接指导 judge 模块与教师模型的选择。

**「可关注」** 可关注：动作级有用性判断在智能体评判中优于轨迹级评估，且执行能力弱的决策模型仍可作为有效的策略教师。

**Tags**: `#eval`, `#orchestration`

---

<a id="item-agent-engineer-4"></a>
### [Anthropic 发布安全评估构建指南](https://www.anthropic.com/research/building-strong-safety-evaluations) ⭐️ 6.8/10

2026年11月13日，Anthropic Research 发布安全评估构建指南，明确安全评估用于衡量模型造成或加剧伤害的倾向、响应是否降低伤害概率及伤害严重程度，是模型部署、配套 safeguards 制定及后续安全训练方向决策的核心依据。指南提出三类核心构建要求：组建包含领域专家与方法专家的跨职能团队、在无互联网沙箱中运行并实时监控评估过程、匹配评估设计与待回答的问题类型，同时强调需同时测量有害请求的合规响应率与良性请求的拒绝率，避免单一拒绝率指标失真。当前指南仅给出概念框架与 Anthropic 内部实践示例，未公开具体 benchmark 或实现细节。

rss · Anthropic Research · Nov 13, 00:00

**「为什么重要」** 当前AI安全评估普遍存在易被操纵、测量效度不足、可复现性差的问题，该指南借鉴心理学领域的可复现性改革经验，给出了可直接落地的评估构建框架，对依赖评估做模型安全判断的团队有直接参考价值。

**「可关注」** 可关注：安全评估需同时测量“对有害请求的合规响应”和“对良性请求的过度拒绝”，避免单一拒绝率指标失真。

**Tags**: `#eval`

---

<a id="item-agent-engineer-5"></a>
### [具身智能体评估存在验证器过拟合风险](https://huggingface.co/papers/2611.08318) ⭐️ 6.0/10

Hugging Face Daily Papers 2026-11-13 摘要了一篇研究论文，指出具身自我改进智能体接触基准测试成功标准（Criteria Exposure）会导致验证器过拟合。论文发现，此类智能体生成的代码能通过验证器检查，但无法完成对应的语言指令任务。该问题源于验证器最初为模仿学习训练的策略设计，现被用于评估智能体生成的代码，标准与任务存在错位。当前材料为截断摘要，源自二次策展Feed而非原始论文，缺少实验细节、具体建议及完整上下文。

rss · Hugging Face Daily Papers · Nov 13, 00:00

**「为什么重要」** 现有具身智能体基准普遍采用Criteria Exposure设计。若验证器过拟合现象成立，当前基准分数可能无法真实反映智能体完成任务的能力，直接影响agent eval harness的可靠性评估。

**「可关注」** 可关注：在评估具身编码智能体时，应同时测量验证器通过率与实际任务完成率，警惕仅依赖单一验证器分数的基准设计可能掩盖真实能力缺陷。

**Tags**: `#eval`, `#coding-agent`

---

<a id="item-agent-engineer-6"></a>
### [Qwen3 DSpine 模型登 HF 榜](https://huggingface.co/tencent/Qwen3.8-27B-DSpine-b16) ⭐️ 6.0/10

2026-11-13，腾讯发布 Qwen3 兼容的 speculative decoding 草稿模型 tencent/Qwen3.8-27B-DSpine-b16，托管于 Hugging Face 并进入趋势榜（trendingScore=203，likes=235）。该模型针对 SGLang 优化，标签显示支持 text-generation 与 draft-model 推理加速。目前公开资料未提供性能指标、技术实现细节或与现有草稿模型的对比数据，需查阅 arxiv:2609.36173 或完整 model card 评估实际收益。潜在受益群体为基于 SGLang 构建 coding agent 的工程师。

rss · Hugging Face Trending Models · Nov 13, 23:00

**「为什么重要」** speculative decoding 是降低 LLM 推理延迟的关键技术之一，该模型若验证有效，可直接影响 coding agent 的响应速度。但当前缺乏基准测试数据，实际加速效果与兼容性仍待确认。

**「可关注」** 可关注：SGLang 用户可先查阅 arxiv:2609.36173 与 model card，确认该 draft model 的 token 接受率与延迟数据，再评估是否接入现有推理管线。

**Tags**: `#coding-agent`, `#speculative-decoding`, `#sglang`, `#inference-optimization`

---

<a id="item-agent-engineer-7"></a>
### [SimReady 资产构建机器人拾放模拟](https://huggingface.co/blog/nvidia/simready-assets-robot-pick-and-place) ⭐️ 5.8/10

Hugging Face 官方博客于 2026-11-13 发布教程，演示如何在 Isaac Sim 6.2 中使用 SimReady Central 的 UR17G 机械臂、Robotiq 2F-140 夹爪与饮料罐资产构建拾放场景。教程说明 SimReady 资产预置碰撞、质量、关节驱动等 OpenUSD 仿真属性，并通过 Robot-Body 4.0.0 与 Robot-Gripper 3.0.0 profile 验证。用户需自行下载资产、组装机器人、检查关节限位与接触行为，并可选择使用 GPT-6 Sol 等 agent 生成控制代码，但生成结果可能因 agent 与模型组合不同而变化。该内容仅对具身智能机器人研发工程师有直接参考价值，对通用 AI Agent 的 harness 或评测无直接关联。

rss · Hugging Face Blog · Nov 13, 18:00

**「为什么重要」** 该教程公开 Isaac Sim 与 SimReady Central 的端到端组装流程，并展示 frontier AI model 辅助生成仿真控制代码的路径。但材料未提供该自动化流程的成功率或性能对比基线，实际效果取决于 agent 与 Isaac Sim skills 的兼容性，且生成代码与结果可能因模型组合不同而变化。

**「可关注」** 可关注：SimReady profile 验证为机器人资产复用提供共享基线，但组装后的场景控制器与接触行为仍需在 Isaac Sim 中独立测试，不能仅凭 profile 通过即认为任务可行。

**Tags**: `#eval`, `#toolchain`, `#robotics`

---

<a id="item-agent-engineer-8"></a>
### [SO-Arena 基准测试发布](https://huggingface.co/papers/2611.15777) ⭐️ 5.5/10

Hugging Face Daily Papers 于 2026-11-13 发布 SO-Arena 基准测试，用于评估 System One 模型的能力谱与决策可靠性。该基准覆盖 11 个领域和 5 个能力家族，提供基于证据的评估、细粒度能力评估和真实场景测试。但当前公告内容被截断，未披露性能结果、可访问性、与现有评估的对比等关键细节。

rss · Hugging Face Daily Papers · Nov 13, 00:00

**「为什么重要」** SO-Arena 针对 System One 模型的细粒度能力评估与决策可靠性，对 AI Agent 工程中的模型选型与 harness 设计有潜在参考价值。但公告信息不完整，其实际效用需等待完整论文发布后验证。

**「可关注」** 可关注：System One 模型评估正从聚合性能转向细粒度能力谱与决策可靠性分析，但 SO-Arena 的具体方法论、难度标准和可复现性需待完整论文确认。

**Tags**: `#eval`, `#harness`, `#coding-agent`

---

## AI Daily

<a id="item-ai-daily-1"></a>
### [ChatGPT Wallet 正式上线](https://openai.com/index/introducing-chatgpt-wallet) ⭐️ 8.8/10

OpenAI 于 2026 年 11 月 13 日正式发布 ChatGPT Wallet。该工具为 ChatGPT Work、Codex 及 dots 产品中的智能体提供安全支付能力，允许其在用户批准前提下完成购买，并沿用现有卡片保护机制。

rss · OpenAI Blog · Nov 13, 15:00

**「为什么重要」** 该工具为 AI 智能体提供交易执行能力，是 OpenAI 产品生态向支付场景的延伸。

**「可关注」** 可关注：ChatGPT Wallet 的交易执行需用户批准，并沿用现有卡片保护机制。

**Tags**: `#product`, `#lab`, `#industry`

---

<a id="item-ai-daily-2"></a>
### [DeepSeek 全家桶应用 API 发布](https://mp.weixin.qq.com/s?__biz=Mzk0OTYwNzc3NQ==&amp;mid=2247485910&amp;idx=1&amp;sn=529f50ba3b37e39319dad1faf7a122cf) ⭐️ 8.8/10

深度求索（DeepSeek）2026年11月13日正式发布全家桶应用API，将此前仅面向App/网页端用户的联网搜索、文件输入、阅读链接、语音交互等能力整合进原有API。开发者仅需开启对应参数即可调用相关能力，无需额外对接外部工具，服务端会自动完成工具调用与上下文拼接。目前V4.1-Flash模型（deepseek-flash）已在Messages、Responses、Chat Completions接口下支持上述能力，底层能力还支持作为Search、Fetch、OCR、ASR、TTS等独立接口单独调用，调用除Token费用外还需支付对应工具调用费用。

rss · DeepSeek · Nov 13, 14:19

**「为什么重要」** 此前开发者若要在自有应用中实现类似DeepSeek App的交互功能，需耗费大量精力对接外部工具，新版API直接开放端侧能力，可大幅降低对话类应用的开发成本。

**「可关注」** 可关注：DeepSeek已开源对应前端Demo与示例代码，支持直接导入DeepSeek历史对话，开发者可基于新版API快速验证功能。

**Tags**: `#lab`, `#product`, `#industry`

---

<a id="item-ai-daily-3"></a>
### [Claude Tag 创业公司使用指南发布](https://claude.com/resources/articles/claude-tag-guide-for-startups) ⭐️ 5.8/10

Claude官方博客发布面向创业公司的Claude Tag（beta）使用指南，访谈8家高增长创业公司，梳理出Slack场景下的典型用法，包括值班告警分诊、Slack线程转PR、团队知识库搭建等场景。其中NavigateAI自6月以来已通过该流程生成223个PR，134个已合并，中位合并耗时2小时，Kikoff曾用21分钟完成故障排查PR的提出与合并。

rss · Claude Blog · Nov 13, 00:00

**「为什么重要」** 该指南汇总了高增长创业公司的真实落地经验，为初创团队配置Claude Tag的场景与规则提供了可直接复用的参考，减少了AI工具适配的摸索成本。

**「可关注」** 可关注：Claude Tag在告警分诊、轻量需求转PR等场景的落地效果，其跨工具关联排查、自动生成草稿PR的能力可有效压缩故障处理与需求交付的周期。

**Tags**: `#product`, `#lab`, `#industry`

---

## AI Deals

<a id="item-ai-deals-1"></a>
### [Epic 11.13-19 免费领《斗阵骑士》](https://www.appinn.com/eggs-261113/) ⭐️ 8.0/10

你看到的内容可能由第三方 AI 基于小众软件文章提炼总结而成，可能与原文真实意图存在偏差。不代表小众软件观点和立场。请&lt;a href=&quot;https://www.appinn.com/eggs-261113/&quot; target=&quot;\_blank&quot;&gt;点击链接阅读原文&lt;/a&gt;细致比对和校验。&lt;br /&gt;&lt;br /&gt;Epic本周（11月13日至11月19日）限时免费开放回合制自走棋游戏《斗阵骑士/Knightica》的领取权限，支持手机端与电脑端，登录Epic账号即可永久入库，领取截止时间为11月19日。

rss · 小众软件 · Nov 13, 06:01

**「为什么重要」** 该游戏在Steam平台获得多半好评（1143篇评价，74%好评），2025年8月发行，本次限免是获取正版的低成本机会，适合喜欢自走棋、站位搭配玩法的玩家。

**「可关注」** 可关注：本次限免覆盖Android、iOS与PC端，跨平台玩家可统一入库管理。

**Tags**: `#limited-free`, `#promo`, `#game`

---

<a id="item-ai-deals-2"></a>
### [World Labs Atlas开放 注册赠10000积分](https://www.ifanr.com/1689379?utm_source=rss&amp;utm_medium=rss&amp;utm_campaign=) ⭐️ 8.0/10

李飞飞创办的World Labs正式开放Atlas世界模型，同步上线网页应用与开发者API，新用户完成手机号验证注册即可获得10000积分。平台提供Viewfinder、Chisel等工具，支持从图片/草图生成可探索的3D场景，生成结果可导出至Blender或游戏引擎。

rss · 爱范儿 · Nov 13, 10:04

**「为什么重要」** Atlas此前仅以演示视频形式曝光，本次开放后普通用户可直接体验从单张图片/草图生成完整可交互3D场景的能力，10000免费积分覆盖基础功能试用。

**「可关注」** 可关注：免费10000积分可覆盖Viewfinder单帧渲染、Chisel单次整组渲染的基础试用；+86手机号可完成注册，需将使用地区选为美国或加拿大以确保功能正常；生成结果支持导出GLB格式对接游戏引擎。

**Tags**: `#credits`, `#free-tier`, `#api`, `#promo`

---

<a id="item-ai-deals-3"></a>
### [InstaBox 免费 4核8GB 云电脑](https://www.appinn.com/egg-instabox/) ⭐️ 7.0/10

你看到的内容可能由第三方 AI 基于小众软件文章提炼总结而成，可能与原文真实意图存在偏差。不代表小众软件观点和立场。请&lt;a href=&quot;https://www.appinn.com/egg-instabox/&quot; target=&quot;\_blank&quot;&gt;点击链接阅读原文&lt;/a&gt;细致比对和校验。&lt;br /&gt;&lt;br /&gt;InstaBox 当前提供免费 4 vCPU、8 GiB 内存、20 GiB 硬盘的云电脑额度，支持 Linux 桌面、安卓镜像，预装 Claude Code、OpenAI Codex 等 AI Agent 工具，可通过 Google 或 GitHub 账号注册领取，无需绑定信用卡；免费版 30 分钟空闲后自动关机，支持手动或 API 唤醒。

rss · 小众软件 · Nov 13, 06:42

**「为什么重要」** 当前同类免费云电脑福利中该额度配置较高，且预置 AI Agent 与图形桌面环境，用户无需自行配置即可直接试用 AI 编程相关工具。

**「可关注」** 可关注：免费版 30 分钟无操作自动关机，支持 API 保活，20 GiB 硬盘空间较小，适合轻量临时测试场景。

**Tags**: `#promo`, `#free-tier`, `#limited-free`

---