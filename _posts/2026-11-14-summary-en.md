---
layout: default
title: "Horizon Summary: 2026-11-14 (EN)"
date: 2026-11-14
lang: en
---

> From 221 items, 19 important content pieces were selected

---

**Agent Harness Architecture**
1. [Mastra @mastra/core@1.83.0 发布](#item-harness-arch-1) ⭐️ 8.8/10
2. [Agent Framework Python 1.26.0 发布](#item-harness-arch-2) ⭐️ 8.8/10
3. [FastMCP v4.2.0 发布](#item-harness-arch-3) ⭐️ 7.8/10
4. [Kitesurf 开源，Workers 无容器 Agent 浏览器](#item-harness-arch-4) ⭐️ 7.8/10

**AI Agent Engineer**
1. [具身智能体验证器标准暴露风险](#item-agent-engineer-1) ⭐️ 7.0/10
2. [XYBench XY 问题评测基准发布](#item-agent-engineer-2) ⭐️ 6.8/10
3. [llama.cpp v1.0.0 正式发布](#item-agent-engineer-3) ⭐️ 6.8/10
4. [Perplexity Decider v1.3 发布](#item-agent-engineer-4) ⭐️ 6.0/10
5. [Open Vision Banana 开放配方发布](#item-agent-engineer-5) ⭐️ 6.0/10
6. [长程 Agent 决策模型角色研究](#item-agent-engineer-6) ⭐️ 6.0/10
7. [WorldDraft 视频渲染基准发布](#item-agent-engineer-7) ⭐️ 6.0/10
8. [Qwen3 DSpine 草稿模型上架 Hugging Face](#item-agent-engineer-8) ⭐️ 6.0/10
9. [PS4 跑 Qwen3.5-9B 离线推理](#item-agent-engineer-9) ⭐️ 5.5/10

**AI Daily**
1. [DeepSeek 全家桶应用 API 发布](#item-ai-daily-1) ⭐️ 9.8/10
2. [OpenAI 推出 ChatGPT Wallet](#item-ai-daily-2) ⭐️ 7.8/10
3. [Shield 用 Forge agents 简化遗留门户交接](#item-ai-daily-3) ⭐️ 6.3/10

**AI Deals**
1. [World Labs Atlas 开放 注册赠积分](#item-ai-deals-1) ⭐️ 9.0/10
2. [Epic 本周限免《斗阵骑士》](#item-ai-deals-2) ⭐️ 8.0/10
3. [Firefox 免费内置 VPN 无限流量至 2027.1](#item-ai-deals-3) ⭐️ 8.0/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [Mastra @mastra/core@1.83.0 发布](https://github.com/mastra-ai/mastra/releases/tag/%40mastra/core%401.83.0) ⭐️ 8.8/10

Mastra 发布 @mastra/core@1.83.0，带来三项核心架构增强：全局可恢复 Agent 流（支持 cross-instance observe/abort、replay cache、TTL/ownership enforcement）、内置 MCP 服务器（/api/mcp + OAuth discovery/audience 检查）、以及实验性 Workflow Storage V2（Postgres/libSQL delta writes）。同步上线可恢复 AI SDK chat 路由、一次性与 bounded schedules，并调整 \`durable\` 选项语义。

github · PaulieScanlon · Nov 13, 14:32

**「设计要点」** 可恢复流通过 replay cache 与跨实例 observe/abort 实现断线重连，TTL 与 ownership 机制防止孤儿运行；内置 MCP 服务器默认随 \`server.auth\` 启用，通过 \`server.mcp.oauth\` 做 OAuth discovery 与 audience 检查，工具集白名单控制暴露范围；Workflow Storage V2 采用 delta writes 仅持久化每步变更，配合异步 \`steps\(\)\` 懒加载历史，降低长工作流存储压力。

**「改了什么」** 所有 Agent 默认获得可恢复流能力（此前仅 durable agents 支持）；\`@mastra/server\` 新增 \`/api/mcp\` 内置端点及 \`server.mcp.oauth\` 配置；\`@mastra/pg\` 与 \`@mastra/libsql\` 支持实验性 \`storageVersion: 2\`；\`durable\` 选项语义收窄为仅控制可恢复流，durable execution 需迁移至 \`createDurableAgent\`。

**Tags**: `#runtime`, `#mcp`, `#tools`, `#permissions`

---

<a id="item-harness-arch-2"></a>
### [Agent Framework Python 1.26.0 发布](https://github.com/microsoft/agent-framework/releases/tag/python-1.26.0) ⭐️ 8.8/10

微软开源 Agent Framework 发布 Python 1.26.0 版本。本次更新新增 harness 运行时控制、实验性消息标记、结构化输出支持，同时包含 Copilot 集成与 Hyperlight 沙箱的两项破坏性变更，以及多项依赖范围调整与安全修复。

github · eavanvalkenburg · Nov 13, 08:28

**「设计要点」** 运行时层面新增 harness 的 loop\_return\_final\_only 参数控制非流式返回结果，Hyperlight 沙箱默认启用 30 秒有限执行预算并支持中断取消；安全与权限层面新增 FIDES 重放溯源钩子、任务范围授权中间件，以及上下文提供者消息的实验性分类回调。

**「改了什么」** \1. 核心新增 create\_harness\_agent\(\) 的 loop\_return\_final\_only 参数、实验性 SecureAgentConfig.message\_labeler 消息分类回调；2. GitHub Copilot 集成支持 Pydantic 模型与 JSON Schema 的结构化输出，但要求 Copilot CLI 不低于 1.0.85；3. Hyperlight 沙箱默认启用 30 秒执行预算，取消执行可触发中断；4. 旧版 Memory 系列 API 标记为 2026 年 12 月 31 日后移除，多项依赖上下界同步调整。

**「评论」** 暂无社区公开评论。

**Tags**: `#runtime`, `#permissions`, `#tools`

---

<a id="item-harness-arch-3"></a>
### [FastMCP v4.2.0 发布](https://github.com/PrefectHQ/fastmcp/releases/tag/v4.2.0) ⭐️ 7.8/10

FastMCP v4.2.0 将 agent 技能分发从本地文件夹迁移到服务器端，通过实验性 MCP Skills 扩展（SEP 2640）实现集中部署与更新。新增 \`SkillCatalogProvider\`、\`SkillManifestProvider\` 及客户端 \`Client.read\_skill\(\)\`、\`to\_directory\(\)\` 方法，支持通过资源接口和哈希清单读取技能。依赖注入新增 \`Annotated\` 声明与 \`CallArgument\` 参数归属。该版本要求 Python 3.11+，4.1 版技能 API 已弃用并将在 4.3 移除。

github · zzstoatzz · Nov 13, 17:07

**「设计要点」** 技能作为普通资源通过 MCP 协议暴露，客户端通过文件大小与摘要校验实现安装，无需宿主原生支持 Skills 扩展。技能在挂载、代理、\`ClientGroup\` 中保持命名空间隔离，并受 \`AuthMiddleware\` 控制。

**「改了什么」** 技能存储从本地文件夹改为服务器端提供，新增 \`SkillCatalogProvider\` 和客户端 \`read\_skill\(\)\`/\`to\_directory\(\)\` 方法。\`Skill\` 类变为存储中性对象，线模型重命名为 \`MCPSkill\`，依赖注入支持 \`Annotated\` 与 \`CallArgument\`。

**Tags**: `#mcp`, `#tools`, `#runtime`

---

<a id="item-harness-arch-4"></a>
### [Kitesurf 开源，Workers 无容器 Agent 浏览器](https://blog.cloudflare.com/kitesurf-open-source/) ⭐️ 7.8/10

Cloudflare 于 2026-11-13 将 Kitesurf 以 Apache 2.0 许可证开源。Kitesurf 是专为 AI agents 设计的无状态浏览器，完全运行在 Cloudflare Workers 上，无需浏览器容器。它支持 Chrome DevTools Protocol \(CDP\) 与 WebMCP，可解析 HTML、应用 CSS、执行 JavaScript 并渲染截图。核心用 Rust 编写并编译为 WebAssembly，依赖 Blitz、Stylo、Boa、Linebender 及 Krilla 等开源包。

rss · Cloudflare AI · Nov 13, 20:20

**「设计要点」** Kitesurf 采用三层架构：Engine 管理浏览器会话与客户端连接，PageScript 在 WebAssembly 中运行页面及 JavaScript，PageRenderer 负责绘制结果。它通过 Dynamic Workers 为每个页面创建隔离 Worker 实例，实现无容器浏览器环境。本地开发通过 wrangler 在 127.0.0.1:8787 启动，生产环境需 Workers Paid 计划。

**「改了什么」** Kitesurf 从 Cloudflare 托管的 Browser Run API 转为开源项目。开发者现在可以克隆仓库、本地修改并部署到自有 Cloudflare Workers 实例。部署需 Workers Paid 计划，因 Kitesurf 使用 Dynamic Workers 为页面创建隔离环境。此前仅能通过托管 API 使用，现在获得完整代码控制权。

**Tags**: `#tools`, `#mcp`, `#sandbox`, `#runtime`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [具身智能体验证器标准暴露风险](https://huggingface.co/papers/2611.08318) ⭐️ 7.0/10

Hugging Face Daily Papers 于 2026-11-14 推介论文 2611.08318。该论文批评具身自我改进智能体开发中的 Criteria Exposure \(CE\) 做法，即把机器人模拟基准的验证器成功标准直接暴露给学习智能体。论文发现，这些标准通常比自然语言指令更严格，导致智能体生成过拟合于验证器的代码，而非完成实际任务。该结果对具身编码智能体评估设计有直接影响，但具体实验数据需查阅原文。

rss · Hugging Face Daily Papers · Nov 14, 03:38

**「为什么重要」** 随着具身编码智能体报告的基准分数持续升高，验证器过拟合可能导致评估指标失真，使开发者无法区分真实任务完成能力与针对验证器的投机取巧。

**「可关注」** 设计具身智能体评估时，应分离验证器标准与任务指令，防止智能体针对验证器逻辑优化而非完成实际任务。

**Tags**: `#eval`, `#coding-agent`

---

<a id="item-agent-engineer-2"></a>
### [XYBench XY 问题评测基准发布](https://huggingface.co/blog/allenai/xybench) ⭐️ 6.8/10

2026 年 11 月 13 日，Hugging Face 博客联合卡内基梅隆大学、NVIDIA、约翰霍普金斯大学发布 XYBench 评测基准，该基准获 EMNLP 2026 最佳资源论文奖，包含 8115 道面向 AI 助手的 XY 问题测试题，用于评估模型识别用户隐含误解、优先解决真实需求的能力。数据集来自 Stack Overflow、Stack Exchange、人工 curated 示例和 WikiHow 生成的 procedural 问题，评估维度包括语用解决方案覆盖、语用重点偏向、误解识别三个指标，测试模型为 Claude Sonnet 4.6、GPT-5、Gemini 3.1 Pro、Qwen3.5-9B、DeepSeek-V4 Pro，以人类参考答案为对照，当前仅覆盖英语查询。实验显示所有模型均更倾向解决用户表面提出的错误请求，仅 35%–41% 的回复重点落在用户隐含的真实需求上；oracle 实验中显式提供真实需求后，模型对底层目标的方案覆盖率上升但误解识别率下降，仍落后人类；模型在选择题中挑选正确方案的比例（71%–84%）远高于自主生成正确方案的比例。该基准主要面向 AI 助手、coding agent 领域的研究者与工程师，可用于量化模型处理用户错误提问的能力改进，未来将拓展至其他语言、文化及多轮对话场景。

rss · Hugging Face Blog · Nov 13, 17:02

**「为什么重要」** XYBench 填补了 XY 问题场景下标准化评测的空白，量化了当前主流 LLM 在识别用户隐含误解、优先解决真实需求上的普遍性能缺口；该基准对生产环境 agent 的实际优化效果、跨语言及多轮场景的适配效果尚未得到验证。

**「可关注」** 可关注：XYBench 揭示主流模型存在「识别正确方案」与「输出正确方案」的能力 gap，且显式提供用户真实意图反而会降低误解识别率，可针对性验证现有 agent 的提示词或微调策略能否缓解该问题。

**Tags**: `#eval`

---

<a id="item-agent-engineer-3"></a>
### [llama.cpp v1.0.0 正式发布](https://huggingface.co/blog/ggml-org/llama-cpp-v1) ⭐️ 6.8/10

2026年11月13日，ggml-org 发布 llama.cpp v1.0.0 及配套 ggml v1.0.0，定位为本地与多模态AI推理的稳定基础库。项目同步启用语义化版本规则，明确大版本 bump 对应 \`./include\` 下公共 C API 的破坏性变更，小版本对应向后兼容的特性、后端或模型支持更新，补丁版本仅做无接口变更的 bug 修复。后续 llama.cpp 与 ggml 将通过大版本号明确标注 API/ABI 不兼容，面向所有依赖该库构建跨平台本地AI产品的下游开发者。当前公开材料未包含具体破坏性变更列表、迁移指南或性能基准数据，无法直接评估升级成本。

rss · Hugging Face Blog · Nov 13, 14:05

**「为什么重要」** 该版本是 llama.cpp 首个正式稳定版，明确了公共接口的长期兼容性承诺与变更边界，对依赖该库构建本地推理、隐私优先AI产品的开发者而言，接口稳定性直接影响迭代规划与维护成本。不过具体升级需等待后续公开的完整变更说明。

**「可关注」** 可关注：后续 llama.cpp 大版本更新将明确标注公共 C API 的 ABI/API 不兼容，集成前需核对 \`include\` 目录下的公共头文件变更。

**Tags**: `#harness`, `#inference`

---

<a id="item-agent-engineer-4"></a>
### [Perplexity Decider v1.3 发布](https://www.perplexity.ai/hub/blog/perplexity-decider) ⭐️ 6.0/10

On November 13, 2026, Perplexity released the Decider v1.3 decision model for Agent orchestration routing scenarios. Community feedback shows the flash variant scores 4 points higher than the v1.2 flash on benchmarks, but some users report overall benchmark performance regression, and mention competing alternatives including Cloudflare Clairic and ScaleDown Extract. Current discussions do not disclose the original training and evaluation technical details of this version, and it mainly affects engineers focusing on Agent decision layer selection.

hackernews · gmays · Nov 13, 19:24 · [Discussion](https://news.ycombinator.com/item?id=50488464)

**「为什么重要」** Decision models are core components of Agent orchestration. The performance and cost performance of Decider v1.3 can serve as a reference for similar selection, but community feedback shows limited overall improvement and the existence of cheaper alternatives, and it has not been proven to become a mainstream solution.

**「可关注」** 可关注：Decider v1.3 flash variant scores 4 points higher than v1.2 on benchmarks, but overall decision model performance improvement is limited, and there are competing solutions such as Cloudflare Clairic and ScaleDown Extract with lower costs.

**「评论」** Community discussions show some users believe Decider v1.3 has overall benchmark performance below expectations, while other users report competitive pricing in actual use. Some users also point out that alternatives such as Cloudflare Clairic and ScaleDown Extract have advantages in cost and accuracy.

**Tags**: `#orchestration`, `#eval`

---

<a id="item-agent-engineer-5"></a>
### [Open Vision Banana 开放配方发布](https://huggingface.co/papers/2611.15844) ⭐️ 6.0/10

Open Vision Banana（OVB）于 2026-11-14 发布，是一套将预训练图像生成器转换为统一多任务感知系统的完全开放可复现配方。该方案基于 4B 与 9B 参数开源基座模型，使用 2.1M-3.8M 训练对，重点分析了颜色编码、提示设计、参数适配与任务平衡对泛化能力的影响。论文指出这些设计选择存在交互作用，单独有益的配置组合后可能损害性能。当前公开摘要被截断，未披露完整性能指标或下游任务对比基线。

rss · Hugging Face Daily Papers · Nov 14, 03:38

**「为什么重要」** 该工作提供了生成式视觉感知领域的全开源可复现参考，但其对 AI Agent 工程（agent 改进、harness、eval、toolchain）的直接适用性较窄。目前仅见论文摘要与 30 个 upvotes，尚无社区实测数据或完整性能基准验证其实际效果。

**「可关注」** 设计选择之间存在交互作用，单独有益的配置组合后可能损害泛化，这提示在多任务感知系统调优时需采用系统性组合评估而非单因素 ablation。

**Tags**: `#multi-modal-perception`, `#open-reproducibility`, `#generative-models`

---

<a id="item-agent-engineer-6"></a>
### [长程 Agent 决策模型角色研究](https://huggingface.co/papers/2611.17167) ⭐️ 6.0/10

2026-11-14，Hugging Face Daily Papers 整理论文 arXiv:2611.17167，研究长程 Agent 中决策模型作为执行者、评判者与教师的角色。实验在 ALFWorld 与 WebShop 上对比三种决策模型与三种通用 LLM，发现执行表现差的模型仍可胜任评判与教学。该摘要为二次来源，未附具体指标，原文实验细节缺失。

rss · Hugging Face Daily Papers · Nov 14, 03:38

**「为什么重要」** 该论文针对 Agent 角色编排与评估，提供‘弱执行者仍可胜任评判与教学’的初步实验证据，对 coding-agent 的 harness 设计有参考价值。但摘要未附具体指标，结论需以原文为准，尚未形成可复用的工程方案。

**「可关注」** 可关注：Agent 系统中执行、评判、教学角色可能需解耦，执行能力弱的模型未必不适合担任评判者或教师。

**Tags**: `#coding-agent`, `#eval`, `#orchestration`

---

<a id="item-agent-engineer-7"></a>
### [WorldDraft 视频渲染基准发布](https://huggingface.co/papers/2611.16217) ⭐️ 6.0/10

2026年11月14日Hugging Face每日论文收录arXiv预印本，提出WorldDraft基准，用于评估多模态编码代理中作为生成式渲染器的视频模型能力，这类代理将4D世界构建与视觉生成解耦，核心问题是视频模型能否仅承担渲染角色。基准包含432个严格配对的测试用例，覆盖48个可执行的4D世界家族，横跨6个动态挑战类别，采用3×3因子设计，正交交叉草稿粒度与两类核心渲染能力（世界保持、视觉实现）。当前公开内容仅为截断摘要，无完整结果、实现细节或性能数据，主要面向多模态编码代理方向的工程师。

rss · Hugging Face Daily Papers · Nov 14, 03:38

**「为什么重要」** WorldDraft填补了多模态编码代理中视频模型渲染能力评估的结构化资源空白，其因子设计为相关能力拆解提供了可参考框架；但完整评估结果未公开，暂无法判断该基准的实际落地价值。

**「可关注」** 可关注：WorldDraft的3×3正交因子设计可参考用于搭建4D世界构建与渲染能力解耦场景的评估框架。

**Tags**: `#eval`, `#coding-agent`

---

<a id="item-agent-engineer-8"></a>
### [Qwen3 DSpine 草稿模型上架 Hugging Face](https://huggingface.co/tencent/Qwen3.8-27B-DSpine-b16) ⭐️ 6.0/10

2026-11-14，Hugging Face trending 列表新增 tencent/Qwen3.8-27B-DSpine-b16，这是一个基于 Qwen3 的推测解码草稿模型，标签显示兼容 SGLang。该模型 trendingScore 为 214，获 248 个 likes，关联 arxiv:2609.36173。当前公开信息仅含基础元数据，未提供技术细节、性能基准或架构说明，因此具体推理加速效果与兼容性细节尚不明确。该模型可能对使用 SGLang 做 agent 推理优化的工程师有用。

rss · Hugging Face Trending Models · Nov 14, 03:38

**「为什么重要」** 推测解码草稿模型有潜力降低 LLM 推理延迟，对 agent 工作流有潜在价值。但该模型目前仅有 trending 元数据，无实测性能数据，因此实际收益尚未证实。

**「可关注」** 可关注：该模型标注兼容 SGLang，若你正在做 agent 推理加速，可查阅 arxiv:2609.36173 或模型页面确认 draft model 的 token 接受率与延迟收益。

**Tags**: `#harness`

---

<a id="item-agent-engineer-9"></a>
### [PS4 跑 Qwen3.5-9B 离线推理](https://www.reddit.com/r/LocalLLaMA/comments/1xvbn2m/qwen359b_running_on_a_ps4s_gpu_offline_using_its/) ⭐️ 5.5/10

2026年11月13日，开源项目garlic-llm的开发者发布工具，支持在未改装的PS4主机GPU上离线运行Qwen3.5-9B模型，自报推理速度达31-39 tok/s。项目使用Qwen3.5自带的MTP头做推测解码，最多生成2个草稿token后由全模型一次性校验，相比优化前22 tok/s的速度有提升；同时采用自定义4/3-bit权重量化打包方案，将模型体积压缩至约4.5 GiB以适配PS4显存限制。该实现无需云服务、订阅或Linux环境，但性能声明尚未经独立验证，PS4硬件场景非常小众，对主流编码代理工作流的直接参考价值有限。

reddit · r/LocalLLaMA · /u/leonardo\_alegria · Nov 13, 16:00

**「为什么重要」** 该实践验证了未改装消费级旧游戏主机GPU运行9B级开源模型的可行性，拓展了边缘部署的硬件边界。但相关性能声明尚未经独立验证，量化与推测解码方案能否复用到其他边缘硬件场景仍待观察。

**「可关注」** 可关注：针对显存极受限的边缘硬件，结合模型原生MTP头做推测解码、搭配自定义低比特量化打包的优化路径，但相关性能声明需独立验证后再评估复用价值。

**Tags**: `#coding-agent`, `#inference-optimization`, `#quantization`, `#speculative-decoding`, `#edge-deployment`

---

## AI Daily

<a id="item-ai-daily-1"></a>
### [DeepSeek 全家桶应用 API 发布](https://mp.weixin.qq.com/s?__biz=Mzk0OTYwNzc3NQ==&amp;mid=2247485910&amp;idx=1&amp;sn=529f50ba3b37e39319dad1faf7a122cf) ⭐️ 9.8/10

DeepSeek 官方于 2026 年 11 月 13 日正式发布全家桶应用 API，将原有 App 的联网搜索、文件输入、语音交互、深度思考搜索等能力整合进原有 API 体系。开发者仅需开启对应参数即可获得相关功能，无需额外对接外部工具处理调用衔接。目前 deepseek-flash（V4.1-Flash）模型已在 Messages、Responses、Chat Completions 接口支持上述能力，底层能力还支持 Search、Fetch、OCR、ASR、TTS 独立接口调用，调用扩展能力除 Token 费用外还需支付对应工具调用费用。

rss · DeepSeek · Nov 13, 14:19

**「为什么重要」** 过去开发者需自行对接外部工具才能实现类似 DeepSeek App 的交互能力，本次更新直接降低了对话类应用的开发成本，让开发者能更专注于业务逻辑构建。

**「可关注」** 可关注：官方已开源对应前端 Demo 与示例代码，同时提示对外提供应用服务的开发者需开启安全校验参数，并承担内容安全审核、大模型登记、AI 标识等合规义务。

**Tags**: `#model`, `#lab`, `#product`, `#industry`

---

<a id="item-ai-daily-2"></a>
### [OpenAI 推出 ChatGPT Wallet](https://openai.com/index/introducing-chatgpt-wallet) ⭐️ 7.8/10

OpenAI 发布 ChatGPT Wallet，面向 ChatGPT Work、Codex 及 dots 等产品内的 agent 提供支付能力。该工具要求用户审批购买操作，并兼容现有卡保护机制。目前未披露具体费率、覆盖地区或接入流程细节。

rss · OpenAI Blog · Nov 13, 15:00

**「可关注」** 可关注：ChatGPT Wallet 要求用户审批购买操作，并兼容现有卡保护机制，agent 开发需适配这一审批流程。

**Tags**: `#lab`, `#product`, `#industry`

---

<a id="item-ai-daily-3"></a>
### [Shield 用 Forge agents 简化遗留门户交接](https://openai.com/business/customer-stories/shield) ⭐️ 6.3/10

Shield 公司使用 OpenAI 的 Forge agents 帮助 IT 技术人员交接遗留门户系统的工作。这些 agents 负责导航系统，使技术人员能专注于需要人类判断的问题。该客户故事发布于 2026 年 11 月 13 日的 OpenAI 官方博客，展示了 AI 在遗留系统维护中的企业应用，但未提供技术规格或性能数据。

rss · OpenAI Blog · Nov 13, 08:00

**「为什么重要」** 该案例展示 AI 在 IT 遗留系统领域的行业应用，但未提供与先前能力的差异化或具体实施细节。

**「可关注」** 可关注：这是一篇营销客户故事而非技术发布，未提供 API、模型或基准测试细节。

**Tags**: `#industry`, `#lab`, `#product`

---

## AI Deals

<a id="item-ai-deals-1"></a>
### [World Labs Atlas 开放 注册赠积分](https://www.ifanr.com/1689379?utm_source=rss&amp;utm_medium=rss&amp;utm_campaign=) ⭐️ 9.0/10

李飞飞创办的 World Labs 正式开放 Atlas 世界模型，新用户注册即赠 10000 积分，支持网页端体验及开发者 API 调用，体验地址为 atlas.worldlabs.ai，注册即可领取，官方未公布截止时间。

rss · 爱范儿 · Nov 13, 10:04

**「为什么重要」** Atlas 支持从草图、单张图片生成可自由探索的 3D 场景，还可导出为 Blender、游戏引擎可用的资产格式，填补了 3D 场景快速生成到生产管线的工具链空白。

**「可关注」** 可关注：+86 手机号可正常完成注册，但后续需选择美国/加拿大区域以确保功能正常；免费 10000 积分仅够基础体验，完整 Splat 生成、整组渲染等操作积分消耗较高。

**Tags**: `#credits`, `#free-tier`, `#api`, `#promo`

---

<a id="item-ai-deals-2"></a>
### [Epic 本周限免《斗阵骑士》](https://www.appinn.com/eggs-261113/) ⭐️ 8.0/10

你看到的内容可能由第三方 AI 基于小众软件文章提炼总结而成，可能与原文真实意图存在偏差。不代表小众软件观点和立场。请&lt;a href=&quot;https://www.appinn.com/eggs-261113/&quot; target=&quot;\_blank&quot;&gt;点击链接阅读原文&lt;/a&gt;细致比对和校验。&lt;br /&gt;&lt;br /&gt;Epic Games Store 于 2026 年 11 月 13 日至 11 月 19 日限时免费送出回合制类 Roguelike 自走棋游戏《斗阵骑士 / Knightica》，支持 PC、Android、iOS 三端领取。该游戏 Steam 平台总体评价为多半好评（1143 篇评测，74% 好评），发行于 2025 年 8 月 21 日。

rss · 小众软件 · Nov 13, 06:01

**「为什么重要」** 本次限免为本周专属福利，11 月 19 日截止，且支持多端适配，可覆盖不同设备的玩家需求。

**「可关注」** 可关注：Epic 本周限免的《斗阵骑士 / Knightica》支持全平台领取，截止时间为 11 月 19 日，对回合制自走棋玩法感兴趣的玩家可及时领取。

**Tags**: `#limited-free`, `#promo`

---

<a id="item-ai-deals-3"></a>
### [Firefox 免费内置 VPN 无限流量至 2027.1](https://blog.mozilla.org/en/firefox/built-in-vpn-unlimited-data/) ⭐️ 8.0/10

Mozilla 官方宣布 Firefox 浏览器内置的免费 VPN 服务取消流量上限，提供无限流量额度，无需额外付费。该优惠有效期截至 2027 年 1 月。目前官方未公布额外领取限制，Firefox 用户可直接使用该服务。

rss · HN Free API / Credits · Nov 13, 16:05

**「为什么重要」** 该福利由 Mozilla 官方博客正式公告确认，有效期明确，是当前少有的免费无流量限制的浏览器内置 VPN 服务，可满足用户的轻量 VPN 使用需求。

**「可关注」** 可关注：该无限流量优惠仅适用于 Firefox 内置 VPN 服务，有效期至 2027 年 1 月，后续是否续期及具体 eligibility 限制官方暂未披露。

**Tags**: `#free-tier`, `#limited-free`, `#promo`

---