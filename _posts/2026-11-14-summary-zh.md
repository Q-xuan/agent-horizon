---
layout: default
title: "Horizon Summary: 2026-11-14 (ZH)"
date: 2026-11-14
lang: zh
---

> 从 205 条内容中筛选出 18 条重要资讯。

<nav id="ah-toc" class="ah-toc" aria-label="目录"><span class="ah-toc-title">目录</span><ul><li><a href="#sec-harness-arch"><span class="ah-toc-name">Harness 架构</span><span class="ah-toc-count">4条</span></a></li><li><a href="#sec-agent-engineer"><span class="ah-toc-name">Agent 工程师日报</span><span class="ah-toc-count">8条</span></a></li><li><a href="#sec-ai-daily"><span class="ah-toc-name">AI 日报</span><span class="ah-toc-count">3条</span></a></li><li><a href="#sec-ai-deals"><span class="ah-toc-name">AI 羊毛</span><span class="ah-toc-count">3条</span></a></li></ul></nav>

---

**[Harness 架构](#sec-harness-arch)**
1. [Mastra core 1.83.0 发布](#item-harness-arch-1) ⭐️ 8.8/10
2. [FastMCP v4.2.0 发布](#item-harness-arch-2) ⭐️ 7.8/10
3. [OpenCode v2.3.0 发布](#item-harness-arch-3) ⭐️ 7.8/10
4. [Cloudflare Kitesurf 开源发布](#item-harness-arch-4) ⭐️ 7.8/10

**[Agent 工程师日报](#sec-agent-engineer)**
1. [XYBench 评测基准发布](#item-agent-engineer-1) ⭐️ 7.8/10
2. [llama.cpp v1.0.0 发布](#item-agent-engineer-2) ⭐️ 7.8/10
3. [HF 每日论文收录智能体决策模型研究](#item-agent-engineer-3) ⭐️ 7.0/10
4. [Anthropic 安全评估构建指南发布](#item-agent-engineer-4) ⭐️ 6.8/10
5. [Criteria Exposure 过拟合](#item-agent-engineer-5) ⭐️ 6.0/10
6. [腾讯 Qwen3-DSpine-b16 登 HF 趋势榜](#item-agent-engineer-6) ⭐️ 6.0/10
7. [SimReady 机器人拾放仿真教程上线](#item-agent-engineer-7) ⭐️ 5.8/10
8. [SO-Arena 基准评估 System One 模型](#item-agent-engineer-8) ⭐️ 5.5/10

**[AI 日报](#sec-ai-daily)**
1. [OpenAI 发布 ChatGPT Wallet](#item-ai-daily-1) ⭐️ 8.8/10
2. [DeepSeek 全家桶应用 API 发布](#item-ai-daily-2) ⭐️ 8.8/10
3. [Claude Tag 发布创业公司指南](#item-ai-daily-3) ⭐️ 5.8/10

**[AI 羊毛](#sec-ai-deals)**
1. [Epic 本周限免《斗阵骑士/Knightica》](#item-ai-deals-1) ⭐️ 8.0/10
2. [Atlas 世界模型开放 赠 1 万积分](#item-ai-deals-2) ⭐️ 8.0/10
3. [InstaBox 免费领 4 核 8GB 云电脑](#item-ai-deals-3) ⭐️ 7.0/10

---

## Harness 架构
{: #sec-harness-arch .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-harness-arch" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-harness-arch-1"></a>
### [Mastra core 1.83.0 发布](https://github.com/mastra-ai/mastra/releases/tag/%40mastra/core%401.83.0) ⭐️ 8.8/10

Mastra 发布 @mastra/core@1.83.0。每个 \`Agent\` 默认获得可恢复流能力，支持重放缓存、跨实例 \`observe\(\)\`/\`abort\(\)\` 控制及 ownership/TTL enforcement。\`@mastra/server\` 新增内置 MCP 端点 \`/api/mcp\`，默认在配置 \`server.auth\` 时启用，并支持 OAuth 发现与 audience 检查。实验性工作流存储 \`storageVersion: 2\` 扩展至 \`@mastra/pg\` 和 \`@mastra/libsql\`，以 delta write 降低长流程写入量。破坏性变更：\`Agent\` 的 \`durable\` 选项现仅控制可恢复流，checkpoint-backed 持久执行需迁移至 \`createDurableAgent\(\{ agent \}\)\`。

github · PaulieScanlon · 11月13日 14:32

**「设计要点」** 运行时层将 Agent 流发布到 stream topic 并维护重放缓存，允许客户端断线重连而不终止运行。权限层通过 \`server.mcp.oauth\` 配置 OAuth 发现与 token audience 校验，\`CompositeAuth\` 聚合多提供方授权服务器。存储层采用按步 delta write，仅持久化变更步骤，配合异步 \`steps\(\)\` 懒加载历史。

**「改了什么」** 所有 \`Agent\` 获得可恢复流（原仅 durable agents 支持），新增 \`agent.observe\(runId\)\`、\`observe\(\).abort\(\)\` 与 \`agent.abortRunStream\(runId\)\` 接口。内置 MCP 服务器替代手动 \`MCPServer\` 定义，支持 \`server.mcp\` 配置路径、工具集与访问控制。工作流存储 V2 支持 Postgres 与 libSQL 后端。\`durable\` 选项语义收窄，仅控制流可恢复性。

**标签**: `#runtime`, `#mcp`, `#tools`, `#storage`

---

<a id="item-harness-arch-2"></a>
### [FastMCP v4.2.0 发布](https://github.com/PrefectHQ/fastmcp/releases/tag/v4.2.0) ⭐️ 7.8/10

FastMCP v4.2.0 发布，将 Skill 升级为服务器可交付的一等公民。Skill 是带 name、description、instructions、files 的纯值对象，支持从目录或包加载，通过 SkillCatalogProvider、SkillsDirectoryProvider 或 SkillManifestProvider 作为资源提供，实验性 Skills 扩展暴露 skills/list 端点并附带哈希 manifest。客户端新增 read\_skill\(\) 验证文件摘要、to\_directory\(\) 安装 skill 到 agent 目录，且 skills 可随 mounts、proxies、ClientGroup 和 AuthMiddleware 组合。依赖注解升级支持 Annotated\[dict, Depends\(get\_config\)\] 与 CallArgument 拥有工具参数，但 Python 3.11+ 为硬性要求，4.1 版 skills API 已弃用并将于 4.3 移除，客户端对 Skills 扩展的支持仍不完整。

github · zzstoatzz · 11月13日 17:07

**「设计要点」** Skill 被设计为存储中立对象，通过 Provider 以资源形式挂载到服务器，客户端通过实验性 Skills 扩展的 skills/list 端点发现并校验哈希 manifest。该设计使 skills 能直接复用 FastMCP 的 mounts、proxies、ClientGroup 和 AuthMiddleware 组合模式，权限管控沿既有 AuthMiddleware 生效。

**「改了什么」** 相对 4.1，Skill 从辅助工具升级为服务器可交付的一等公民，提供纯值对象模型、目录与包加载，以及 SkillCatalogProvider、SkillsDirectoryProvider 和 SkillManifestProvider 三种挂载方式，实验性 Skills 扩展暴露 skills/list 发现端点；客户端新增 read\_skill\(\) 与 to\_directory\(\) 补齐验证与安装能力。依赖注解支持 Annotated 形式与 CallArgument 参数归属，Python 3.11+ 成为硬性要求，4.1 版 skills API 进入弃用倒计时，同步包含 OpenAPI、proxies、auth 与 telemetry 修复。

**标签**: `#mcp`, `#tools`, `#permissions`

---

<a id="item-harness-arch-3"></a>
### [OpenCode v2.3.0 发布](https://github.com/anomalyco/opencode/releases/tag/v2.3.0) ⭐️ 7.8/10

anomalyco/opencode v2.3.0 正式发布，核心变更包括子代理默认改为后台运行、TUI 转录默认折叠摘要、桌面应用新增提示跳转，以及 MCP 事件与 shell 后台化的实验性支持。子代理立即返回会话 ID 并在空闲时向父会话报告结果，支持父子会话并发工作。TUI 默认以 low verbosity 将工具调用和思考总结为单行可折叠活动记录。桌面应用新增 Jump to message 功能，支持通过 Cmd+Alt+G 或 Ctrl+Alt+G 跨会话搜索并跳转至历史提示。

github · github-actions\[bot\] · 11月13日 08:55

**「设计要点」** 运行时层将子代理改为立即返回会话 ID 的后台任务模型，父会话无需阻塞等待，通过空闲报告机制异步接收结果。工具层统一本地 shell 命令经进程守护程序调度，支持超时后自动转入后台，provider 层新增 mTLS 客户端证书配置；记忆层将 TUI 转录默认设为 low verbosity，将工具调用与思考流折叠为单行可展开活动记录。

**「改了什么」** 子代理默认改为后台运行，父会话可并发继续工作，子代理空闲时回传最终结果。TUI 转录默认折叠为单行活动摘要，桌面应用新增跨会话提示跳转；shell 命令在服务器切换后保持输出，超时后可自动转入后台，并新增 MCP 事件与 LM Studio 决策模型实验性支持。Code Mode 下 file 和 skill 工具返回更简化的结构化结果，本地模型发现请求超时从 1 秒延长至 15 秒。

**标签**: `#subagents`, `#runtime`, `#memory`

---

<a id="item-harness-arch-4"></a>
### [Cloudflare Kitesurf 开源发布](https://blog.cloudflare.com/kitesurf-open-source/) ⭐️ 7.8/10

Cloudflare 于 2026-11-13 将 Kitesurf 以 Apache 2.0 许可证开源。Kitesurf 是专为 AI agent 设计的无状态浏览器，运行在 Cloudflare Workers 上，支持 Chrome DevTools Protocol \(CDP\) 与 WebMCP 协议。其核心用 Rust 编写并编译为 WebAssembly，集成 Blitz（HTML 解析与 DOM）、Stylo（CSS 解析与级联）、Boa（JavaScript 执行）及 Linebender/Krilla（文本布局、2D 图形与 PDF）等开源库，无需浏览器容器即可解析页面、执行脚本并渲染截图。部署至个人 Cloudflare 账户需 Workers Paid 计划，因依赖 Dynamic Workers 提供页面级隔离。

rss · Cloudflare AI · 11月13日 20:20

**「设计要点」** Kitesurf 完全运行在 Cloudflare Workers 无容器环境中，Rust 核心编译为 WebAssembly 实现浏览器引擎。系统分为 Engine（会话与连接管理）、PageScript（页面与 JS 执行）和 PageRenderer（渲染输出）三层，通过 Dynamic Workers 为每个页面创建隔离执行环境，并在本地开发时通过 8787 端口提供 CDP 接口供 Puppeteer 或 AI harness 连接。

**「改了什么」** 此前 Kitesurf 仅通过 Browser Run 托管 API 提供，开发者无法修改代码或选择部署位置。开源后，开发者可克隆仓库、本地运行、自行修改并部署到 Cloudflare Workers，或直接集成到自有 AI agent 工具链中。

**标签**: `#tools`, `#runtime`, `#mcp`, `#sandbox`

---

## Agent 工程师日报
{: #sec-agent-engineer .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-agent-engineer" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-agent-engineer-1"></a>
### [XYBench 评测基准发布](https://huggingface.co/blog/allenai/xybench) ⭐️ 7.8/10

2026 年 11 月 13 日，Allen AI 联合 Carnegie Mellon、NVIDIA、Johns Hopkins 发布 XYBench 评测基准，该基准包含 8115 个跨编程、烹饪、家装等领域的真实问题，其中 1557 个来自 Stack Overflow、184 个来自 Stack Exchange、102 个为人工 curated、6272 个基于 WikiHow 指南生成，获 EMNLP 2026 最佳资源论文奖，用于评估 AI 助手识别用户基于误解的 XY 问题、优先解决真实目标而非表面请求的能力。基准测试了 Claude Sonnet 4.6、GPT-5、Gemini 3.1 Pro、Qwen3.5-9B、DeepSeek-V4 Pro 五个模型，所有模型在单轮设置下均更倾向提供表面请求的解决方案，底层目标解决方案占比仅 59%–71%，误解识别率远低于人类参考答案；基准采用 Claude Sonnet 4.5 作为自动裁判，其与人类标注者的解决方案识别一致性达 97.5%–100%，误解识别一致性为 84.6%–93.3%，语用强调一致性为 74.2%–79.8%。此外，oracle 实验中明确提供用户底层目标后，Sonnet 4.6 的底层目标解决方案占比从 59% 升至 67%，但误解识别率从 47% 降至 34%，仍落后于人类参考答案。当前 XYBench 仅覆盖英语查询，主要针对程序性与日常 procedural 问题，多语言、多文化、多轮对话场景的扩展仍待推进。

rss · Hugging Face Blog · 11月13日 17:02

**「为什么重要」** XYBench 填补了 AI 助手处理 XY 问题的专项评测空白，其拆分的「语用解决方案」「语用强调」「误解识别」三项指标，能区分模型「识别误解」和「按识别结果行动」的能力，避免多选测试掩盖生成端的实际短板。

**「可关注」** 可关注：模型在 XY 问题场景下存在「识别正确但执行偏差」的 gap，仅靠意图注入或多选评测无法完全衡量真实助手的纠错能力。

**标签**: `#eval`, `#benchmark`, `#xy-problem`, `#agent-evaluation`, `#huggingface`

---

<a id="item-agent-engineer-2"></a>
### [llama.cpp v1.0.0 发布](https://huggingface.co/blog/ggml-org/llama-cpp-v1) ⭐️ 7.8/10

llama.cpp v1.0.0 与 ggml v1.0.0 于 2026-11-13 正式发布。项目采用语义版本控制，MAJOR 版本 bump 对应公共 C API（./include）的破坏性变更并标记 ABI 不兼容。当前支持 150+ 模型架构变体及主流推测解码方法，分发渠道覆盖 Docker、Homebrew、conda-forge、MacPorts、Winget 及 XCFramework。Hugging Face 同步推出 Llama desktop apps for macOS/Windows。

rss · Hugging Face Blog · 11月13日 14:05

**「为什么重要」** v1.0.0 将 API 稳定性作为核心承诺，下游 harness 和 coding agent 可据此建立兼容性基线。语义版本规则明确区分 API/ABI breaking change 与功能更新，降低集成风险。但材料未提供具体性能基准或 breaking change 清单，实际迁移成本仍需对照 include/ 目录确认。

**「可关注」** 可关注：libllama 与 libggml 的公共头文件路径（llama.cpp/include/、ggml/include/）已锁定为版本边界，集成时应通过这些路径而非内部头文件做兼容性检查。

**标签**: `#harness`

---

<a id="item-agent-engineer-3"></a>
### [HF 每日论文收录智能体决策模型研究](https://huggingface.co/papers/2611.17167) ⭐️ 7.0/10

2026 年 11 月 13 日 Hugging Face 每日论文收录了一篇长程智能体决策模型角色研究论文，该论文当前获得 29 次 HF 每日论文点赞。该研究在 ALFWorld、WebShop 基准上对比 3 个决策模型与 3 个通用 LLM 的 Actor、Judge 表现，并测试 JEV 作为 Teacher 的效果。实验发现表现较差的 Actor 模型仍可有效教授智能体策略，动作级有用性判断优于轨迹级评估（原文该部分内容截断）；同时所有模型作为 Actor 时会被更简单的子目标干扰，偏离需优先完成的子目标，作为 Judge 查看完整轨迹时会认可该子目标的相关步骤。该研究为长程智能体的评估、设计及强化学习训练提供参考。

rss · Hugging Face Daily Papers · 11月13日 00:00

**「为什么重要」** 该研究针对长程智能体决策模型的核心角色分工问题，已通过 ALFWorld、WebShop 标准基准验证了 Actor 能力与教学能力解耦、动作级评估优于轨迹级评估的结论，为相关方案设计提供了可复用的实验依据。

**「可关注」** 可关注：决策模型的能力评估需按角色区分，Actor 性能不足的模型仍可能作为有效策略教师，Judge 评估优先采用动作级有用性判断可能比轨迹级评估更准确。

**标签**: `#eval`, `#orchestration`

---

<a id="item-agent-engineer-4"></a>
### [Anthropic 安全评估构建指南发布](https://www.anthropic.com/research/building-strong-safety-evaluations) ⭐️ 6.8/10

2026 年 11 月 13 日，Anthropic Research 发布安全评估构建指南，明确安全评估用于衡量模型造成或加剧伤害的倾向、响应对伤害发生概率与严重程度的影响，而非具体能力，是模型部署、配套 safeguards 选型、安全训练方向决策的核心依据。指南提出构建强安全评估需组建包含领域与方法专家的团队，在无互联网沙箱中运行评估并加实时监控，同时借鉴心理学领域的预注册、严格统计等改革提升可复现性，要求评估设计匹配目标（观察性或因果性），保证构念效度，避免用单一拒绝率作为所有风险场景的指标，双用领域需同步设计有害与良性请求评估过度拒绝。Anthropic 还提到近期因自身事件已加固评估环境，暂停多项给模型联网的评估并新增实时监控。

rss · Anthropic Research · 11月13日 00:00

**「为什么重要」** 当前 AI 安全评估普遍存在易被操纵、测量目标不符、可复现性差的问题，该指南是主流 AI 实验室公开的首个系统性安全评估构建建议，附带 Anthropic 自身实践案例，为相关团队提供了可直接参考的框架。但指南目前仅给出原则性要求，未公开具体 benchmark 或实现细节，其落地效果仍需后续实践验证。

**「可关注」** 可关注：安全评估需先明确目标是观察模型行为还是验证干预效果，对应选择观察性或因果性设计；同时需针对不同风险场景定制响应 rubric，避免用单一拒绝率作为所有场景的指标，双用领域需同步设计有害与良性请求评估过度拒绝问题。

**标签**: `#eval`

---

<a id="item-agent-engineer-5"></a>
### [Criteria Exposure 过拟合](https://huggingface.co/papers/2611.08318) ⭐️ 6.0/10

2026-11-13，Hugging Face Daily Papers 摘要了一篇研究（arXiv:2611.08318），指出自改进具身智能体在机器人模拟基准上存在 Criteria Exposure 问题：将基准成功标准暴露给学习智能体会导致验证器过拟合。智能体生成的代码能通过验证器却无法完成实际语言指令任务，使现有评估基准的分数失去可信度。该材料为截断摘要，未提供实验细节、具体修复建议或完整上下文，来源为二次策展 feed 而非原始论文。

rss · Hugging Face Daily Papers · 11月13日 00:00

**「为什么重要」** 该研究直接挑战了当前 embodied coding agent 评估体系的有效性。若验证器过拟合普遍存在，现有 benchmark 分数可能无法反映真实任务完成能力，影响工程师对 agent 性能的判断与选型。

**「可关注」** 可关注：当前 embodied agent 评估 harness 若直接暴露 verifier 标准给模型，可能产生过拟合代码，需验证 benchmark 分数与实际任务完成度的一致性。

**标签**: `#eval`, `#coding-agent`

---

<a id="item-agent-engineer-6"></a>
### [腾讯 Qwen3-DSpine-b16 登 HF 趋势榜](https://huggingface.co/tencent/Qwen3.8-27B-DSpine-b16) ⭐️ 6.0/10

2026 年 11 月 13 日，腾讯发布的 tencent/Qwen3.8-27B-DSpine-b16 模型登上 Hugging Face 趋势榜，该模型为 Qwen3 兼容的推测解码草稿模型，适配 SGLang 推理框架，标签覆盖推测解码、文本生成、推理优化方向，当前 trendingScore 为 203、获赞 235，暂未公开性能指标、技术实现细节及与现有草稿模型的对比数据。

rss · Hugging Face Trending Models · 11月13日 23:00

**「为什么重要」** 该模型面向推测解码场景设计，若性能达标可降低 LLM coding agent 的推理开销，但目前无公开基准测试数据，实际收益尚未得到证实。

**「可关注」** 可关注该模型关联的 arxiv 论文（编号 2609.36173）及后续公开的模型卡，重点查看其吞吐量、延迟对比数据，评估对 SGLang 推理管线的适配价值。

**标签**: `#coding-agent`, `#speculative-decoding`, `#sglang`, `#inference-optimization`

---

<a id="item-agent-engineer-7"></a>
### [SimReady 机器人拾放仿真教程上线](https://huggingface.co/blog/nvidia/simready-assets-robot-pick-and-place) ⭐️ 5.8/10

2026 年 11 月 13 日 Hugging Face 官方博客发布具身机器人仿真教程，讲解如何基于 SimReady Central 的 UR17G 机械臂、Robotiq 2F-140 夹爪、饮料罐资产，在 Isaac Sim 6.2 中搭建饮料罐拾放仿真场景，流程包含资产下载、SimReady profile 校验、机器人组装、控制代码运行与行为验证，还演示了用 GPT-6 Sol 生成任务代码的示例。教程明确生成代码结果会随 agent 与模型组合不同而变化，仅对具身机器人仿真研发工程师有直接参考价值，对通用 AI Agent 的 harness、评测、工具链改进无直接关联。

rss · Hugging Face Blog · 11月13日 18:00

**「为什么重要」** 该教程首次公开了 SimReady 资产在 Isaac Sim 中从校验到组装再到任务运行的全流程操作路径，降低了具身仿真场景的搭建成本；目前尚未看到公开数据验证该流程在不同机器人场景下的复用效果。

**「可关注」** 可关注：SimReady Central 资产自带仿真属性与 Robot-Body 4.0.0、Robot-Gripper 3.0.0 profile 校验报告，Isaac Sim 6.2 配套的 isaac-sim-remote、usd-articulation 等 agent 技能可支撑自动化组装与任务代码生成，但生成的控制代码需先校验关节限位、驱动设置、接触行为再适配，且结果会随模型与 agent 组合不同而变化。

**标签**: `#eval`, `#toolchain`, `#robotics`

---

<a id="item-agent-engineer-8"></a>
### [SO-Arena 基准评估 System One 模型](https://huggingface.co/papers/2611.15777) ⭐️ 5.5/10

Hugging Face Daily Papers 于 2026-11-13 介绍论文 SO-Arena: Benchmarking the Capability Spectrum and Reliability of System One Models。该基准针对快速、低 token 生成的 System One 模型，覆盖 11 个领域与 5 个能力家族，评估能力谱系与决策可靠性。评估方式包括基于可靠来源的证据 grounded 评估、领域特定难度标准的细粒度评估，以及现实场景测试。当前材料为截断版本，未披露与现有基准的对比、具体性能结果、可访问性信息或对 AI Agent 工程的具体用例。

rss · Hugging Face Daily Papers · 11月13日 00:00

**「为什么重要」** 现有基准多关注聚合性能，对 System One 模型决策可靠性的细粒度覆盖不足。SO-Arena 试图补全这一评估维度，但其实际可用性需阅读全文确认。

**「可关注」** 可关注：SO-Arena 将 System One 模型评估维度从聚合性能扩展到能力谱系与决策可靠性，但具体任务设计、评分标准及与现有 harness 的兼容性需查阅原文。

**标签**: `#eval`, `#harness`, `#coding-agent`

---

## AI 日报
{: #sec-ai-daily .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-daily" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-daily-1"></a>
### [OpenAI 发布 ChatGPT Wallet](https://openai.com/index/introducing-chatgpt-wallet) ⭐️ 8.8/10

OpenAI 正式推出 ChatGPT Wallet，这是一款面向 ChatGPT Work、Codex 及 dots 产品内 agent 的安全支付工具。该工具支持 agent 在获得用户授权后完成消费，同时沿用现有银行卡保护机制。目前未公开更多使用限制细节。

rss · OpenAI Blog · 11月13日 15:00

**「为什么重要」** 这是 AI 实验室首次为旗下多款 agent 产品提供官方配套支付工具，明确了 agent 消费场景的用户授权与资金安全规则，为行业 agent 支付能力建设提供了可参考的落地样本。

**「可关注」** 可关注：ChatGPT Wallet 与 Codex 等 agent 产品的集成规则，以及用户授权流程的具体实现方式。

**标签**: `#product`, `#lab`, `#industry`

---

<a id="item-ai-daily-2"></a>
### [DeepSeek 全家桶应用 API 发布](https://mp.weixin.qq.com/s?__biz=Mzk0OTYwNzc3NQ==&amp;mid=2247485910&amp;idx=1&amp;sn=529f50ba3b37e39319dad1faf7a122cf) ⭐️ 8.8/10

深度求索（DeepSeek）于 2026 年 11 月 13 日正式发布全家桶应用 API，将此前仅面向消费者的联网搜索、文件输入、阅读链接、语音交互等能力整合进原有 API，开发者仅需开启对应参数即可调用，无需额外对接外部工具。目前 V4.1-Flash（deepseek-flash）已在 Messages、Responses、Chat Completions 接口下支持上述能力，底层及语音能力还支持作为独立接口单独调用。调用相关能力除收取 Token 费用外，还需支付对应工具调用费用。

rss · DeepSeek · 11月13日 14:19

**「为什么重要」** 此前开发者若要在自有应用中实现类似 DeepSeek App 的交互功能，需自行对接外部工具处理调用衔接，本次开放后可直接复用官方能力，大幅降低对话类应用的开发成本。

**「可关注」** 可关注：原有 DeepSeek API 开启对应参数即可调用联网搜索、文件输入、阅读链接等能力，服务端自动完成工具调用与上下文拼接；OCR、ASR、TTS 等语音及底层能力还支持独立或组合调用。

**标签**: `#lab`, `#product`, `#industry`

---

<a id="item-ai-daily-3"></a>
### [Claude Tag 发布创业公司指南](https://claude.com/resources/articles/claude-tag-guide-for-startups) ⭐️ 5.8/10

Claude 官方博客发布面向创业公司的 Claude Tag（beta）使用指南，整理 8 家高增长创业公司的典型用法与实践案例，覆盖值班告警、Slack 线程转 PR 等场景。指南给出具体效率数据：NavigateAI 自 6 月通过该功能开出约 223 个 PR，其中 134 个已合并，中位合并耗时 2 小时；Campfire 曾 21 分钟开出 PR 并于当日合并。当前内容截断未展示完整信息，无新的模型、政策或重大产品发布。

rss · Claude Blog · 11月13日 00:00

**「为什么重要」** 指南汇总了不同规模高增长创业公司的落地实践与可复用配置模板，为 lean 团队快速落地 Claude Tag 提效提供了可直接参考的路径。

**「可关注」** 可关注：Claude Tag 在告警分诊、Slack 线程转 PR 等场景的落地配置，以及其将问题响应、需求落地周期从天级压缩到分钟级的实践效果。

**标签**: `#product`, `#lab`, `#industry`

---

## AI 羊毛
{: #sec-ai-deals .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-deals" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-deals-1"></a>
### [Epic 本周限免《斗阵骑士/Knightica》](https://www.appinn.com/eggs-261113/) ⭐️ 8.0/10

你看到的内容可能由第三方 AI 基于小众软件文章提炼总结而成，可能与原文真实意图存在偏差。不代表小众软件观点和立场。请&lt;a href=&quot;https://www.appinn.com/eggs-261113/&quot; target=&quot;\_blank&quot;&gt;点击链接阅读原文&lt;/a&gt;细致比对和校验。&lt;br /&gt;&lt;br /&gt;Epic 本周（11.13~11.19）限时免费开放回合制自走棋游戏《斗阵骑士/Knightica》的领取权限，支持手机端与电脑端，登录 Epic 账号即可永久入库。

rss · 小众软件 · 11月13日 06:01

**「为什么重要」** 该游戏在 Steam 平台获得多半好评，限免期内领取可永久入库，错过活动需付费购买。

**「可关注」** 可关注：仅需登录 Epic 账号即可领取，支持 Android、iOS 及电脑端，领取后永久入库。

**标签**: `#limited-free`, `#promo`, `#game`

---

<a id="item-ai-deals-2"></a>
### [Atlas 世界模型开放 赠 1 万积分](https://www.ifanr.com/1689379?utm_source=rss&amp;utm_medium=rss&amp;utm_campaign=) ⭐️ 8.0/10

李飞飞创办的 World Labs 正式开放 Atlas 世界模型，新用户注册即可获得 10000 积分。该模型同步上线网页应用与开发者 API，支持用户通过网页端体验 3D 场景生成、重建能力，也可通过 API 将能力集成到自有管线。注册需完成手机号验证，+86 手机号可正常接收验证码，后续需选择美国或加拿大区域以确保体验正常，体验地址为 atlas.worldlabs.ai。

rss · 爱范儿 · 11月13日 10:04

**「为什么重要」** Atlas 补齐了从单图/草图生成 3D 场景、调整布局、渲染导出到游戏引擎的全链路能力，是 3D 生成领域少有的公开可体验的成熟方案。新用户赠送的 10000 积分足够完成基础功能体验，无需付费即可上手。

**「可关注」** 可关注：Atlas 采用积分制，Viewfinder 渲染单帧消耗 50 积分，生成完整 Splat 需 5000 积分，Chisel 智能体按 Gemini 4 Argon 的输出 token 计费（每 1M 输出 token10000 积分），免费额度仅够基础功能体验，重度使用需额外充值。

**标签**: `#credits`, `#free-tier`, `#api`, `#promo`

---

<a id="item-ai-deals-3"></a>
### [InstaBox 免费领 4 核 8GB 云电脑](https://www.appinn.com/egg-instabox/) ⭐️ 7.0/10

你看到的内容可能由第三方 AI 基于小众软件文章提炼总结而成，可能与原文真实意图存在偏差。不代表小众软件观点和立场。请&lt;a href=&quot;https://www.appinn.com/egg-instabox/&quot; target=&quot;\_blank&quot;&gt;点击链接阅读原文&lt;/a&gt;细致比对和校验。InstaBox 当前提供免费 4 vCPU、8 GiB 内存、20 GiB 硬盘的云电脑额度，支持 Linux 桌面、安卓镜像，预装 Claude Code、OpenAI Codex 等 AI Agent 工具，可通过 Google 或 GitHub 账号注册领取，无需绑定信用卡。

rss · 小众软件 · 11月13日 06:42

**「为什么重要」** 该免费额度预置 AI Agent 运行环境与图形桌面，无需自行配置服务器环境，可快速用于 coding agent 测试或轻量开发场景。

**「可关注」** 可关注：免费实例 30 分钟无操作会自动关机，可通过 API 手动唤醒或保活，仅适合间歇性任务，无法作为常驻服务使用。

**标签**: `#promo`, `#free-tier`, `#limited-free`

---