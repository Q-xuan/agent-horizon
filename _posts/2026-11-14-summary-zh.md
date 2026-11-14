---
layout: default
title: "Horizon Summary: 2026-11-14 (ZH)"
date: 2026-11-14
lang: zh
---

> 从 221 条内容中筛选出 19 条重要资讯。

<nav id="ah-toc" class="ah-toc" aria-label="目录"><span class="ah-toc-title">目录</span><ul><li><a href="#sec-harness-arch"><span class="ah-toc-name">Harness 架构</span><span class="ah-toc-count">4条</span></a></li><li><a href="#sec-agent-engineer"><span class="ah-toc-name">Agent 工程师日报</span><span class="ah-toc-count">9条</span></a></li><li><a href="#sec-ai-daily"><span class="ah-toc-name">AI 日报</span><span class="ah-toc-count">3条</span></a></li><li><a href="#sec-ai-deals"><span class="ah-toc-name">AI 羊毛</span><span class="ah-toc-count">3条</span></a></li></ul></nav>

---

**[Harness 架构](#sec-harness-arch)**
1. [Mastra core 1.83.0 发布](#item-harness-arch-1) ⭐️ 8.8/10
2. [microsoft/agent-framework python-1.26.0 发布](#item-harness-arch-2) ⭐️ 8.8/10
3. [FastMCP v4.2.0 发布](#item-harness-arch-3) ⭐️ 7.8/10
4. [Cloudflare Kitesurf 开源发布](#item-harness-arch-4) ⭐️ 7.8/10

**[Agent 工程师日报](#sec-agent-engineer)**
1. [具身智能体验证器过拟合研究发布](#item-agent-engineer-1) ⭐️ 7.0/10
2. [XYBench 发布 评估 XY 问题处理能力](#item-agent-engineer-2) ⭐️ 6.8/10
3. [llama.cpp v1.0.0 发布](#item-agent-engineer-3) ⭐️ 6.8/10
4. [Perplexity Decider v1.3 更新](#item-agent-engineer-4) ⭐️ 6.0/10
5. [Open Vision Banana 开源配方发布](#item-agent-engineer-5) ⭐️ 6.0/10
6. [HF Paper：长期智能体角色研究](#item-agent-engineer-6) ⭐️ 6.0/10
7. [WorldDraft 基准发布 评估视频渲染能力](#item-agent-engineer-7) ⭐️ 6.0/10
8. [Qwen3 DSpine 草稿模型上 HF 榜](#item-agent-engineer-8) ⭐️ 6.0/10
9. [Qwen3.5-9B 在 PS4 离线运行](#item-agent-engineer-9) ⭐️ 5.5/10

**[AI 日报](#sec-ai-daily)**
1. [DeepSeek 全家桶应用 API 发布](#item-ai-daily-1) ⭐️ 9.8/10
2. [OpenAI 推出 ChatGPT Wallet](#item-ai-daily-2) ⭐️ 7.8/10
3. [Shield 用 Forge 代理简化遗留门户交接](#item-ai-daily-3) ⭐️ 6.3/10

**[AI 羊毛](#sec-ai-deals)**
1. [World Labs Atlas 开放 注册赠 10000 积分](#item-ai-deals-1) ⭐️ 9.0/10
2. [Epic 本周免费送《斗阵骑士/Knightica》](#item-ai-deals-2) ⭐️ 8.0/10
3. [Firefox 内置 VPN 无限流量至 2027 年 1 月](#item-ai-deals-3) ⭐️ 8.0/10

---

## Harness 架构
{: #sec-harness-arch .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-harness-arch" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-harness-arch-1"></a>
### [Mastra core 1.83.0 发布](https://github.com/mastra-ai/mastra/releases/tag/%40mastra/core%401.83.0) ⭐️ 8.8/10

Mastra 发布 @mastra/core@1.83.0，核心更新三项：所有 Agent 原生支持可恢复运行流，提供跨实例 observe/abort、replay cache 与 TTL enforcement；@mastra/server 内置 MCP 端点 \`/api/mcp\`，支持 OAuth discovery 与 audience 校验；实验性 Workflow Storage V2 采用 delta writes，降低 Postgres 与 libSQL 的写入量。AI SDK chat 路由新增 \`useChat\(\{ resume: true \}\)\` 支持，调度器增加一次性 \`runAt\` 与 bounded \`endAt\` 执行。Breaking change：\`Agent.durable\` 现在仅控制 resumable streams，checkpoint-backed durable execution 需迁移至 \`createDurableAgent\(\{ agent \}\)\`。

github · PaulieScanlon · 11月13日 14:32

**「设计要点」** 运行时层通过 stream topic 与 replay cache 实现断线重连，observe/abort 跨实例生效；存储层以 per-step delta 替换全量 run 重写；协议层内置 MCP server 并集成 OAuth discovery。

**「改了什么」** 所有 Agent 默认获得可恢复流能力，不再局限于 durable agents；内置 MCP server 替代手动 MCPServer 定义；工作流存储引入 delta writes 实验选项，\`durable\` 选项语义收窄。

**「评论」** 无社区评论。

**标签**: `#runtime`, `#mcp`, `#tools`, `#permissions`

---

<a id="item-harness-arch-2"></a>
### [microsoft/agent-framework python-1.26.0 发布](https://github.com/microsoft/agent-framework/releases/tag/python-1.26.0) ⭐️ 8.8/10

microsoft/agent-framework python-1.26.0 发布。核心新增 harness 运行时参数 \`loop\_return\_final\_only\`，允许非流式调用仅获取最终循环响应；引入实验性 \`SecureAgentConfig.message\_labeler\` 回调用于上下文消息分类。Copilot 集成通过 \`response\_format\` 支持 Pydantic 模型与 JSON Schema 结构化输出。Hyperlight 执行层引入默认 30 秒预算与中断机制，旧版 Memory API 标记为弃用。

github · eavanvalkenburg · 11月13日 08:28

**「设计要点」** 运行时层通过 \`loop\_return\_final\_only\` 分离流式与非流式返回语义，Hyperlight 沙箱采用硬中断加执行预算双控。权限与审计侧，FIDES replay-provenance 绑定服务历史 continuation，approval 状态在 agent-as-tool 场景下做 run-level 隔离。记忆层弃用旧 MemoryContextProvider 体系，转向 FileMemoryProvider 与 AgentFileStore 的文件存储布局。

**「改了什么」** 非流式 harness 调用新增 \`loop\_return\_final\_only\` 参数；实验性消息标签器上线；Copilot 集成支持 Pydantic/JSON Schema 结构化输出；Hyperlight 默认 30 秒执行预算并支持中断取消；旧 Memory API 宣布弃用；Copilot CLI 最低版本要求提升至 1.0.85。

**标签**: `#runtime`, `#permissions`, `#tools`

---

<a id="item-harness-arch-3"></a>
### [FastMCP v4.2.0 发布](https://github.com/PrefectHQ/fastmcp/releases/tag/v4.2.0) ⭐️ 7.8/10

FastMCP v4.2.0 将 agent 技能分发从本地文件夹迁移到服务器端，通过实验性 MCP Skills extension（SEP 2640）实现集中部署。新增 SkillCatalogProvider 在服务器注册技能，客户端通过 Client.read\_skill\(\) 和 to\_directory\(\) 读取并安装技能。技能作为普通资源提供，支持挂载、代理、ClientGroup 和 AuthMiddleware。Python 3.11 成为最低要求，4.1 版 skills API 已废弃并将于 4.3 移除。

github · zzstoatzz · 11月13日 17:07

**「设计要点」** 技能以资源形式挂载在 MCP 服务器，与工具同域部署。客户端通过资源接口读取文件清单和内容，实验性 skills/list 提供带哈希清单的发现能力。依赖注入支持 Annotated\[dict, Depends\(get\_config\)\] 语法，CallArgument 允许依赖拥有工具参数。

**「改了什么」** 服务器端技能分发替代本地文件夹部署，SkillCatalogProvider 和 SkillManifestProvider 提供技能目录。客户端新增 read\_skill\(\) 和 to\_directory\(\) 方法。依赖注入支持 Annotated 类型和 CallArgument 参数归属。4.1 skills API 进入废弃流程。

**标签**: `#mcp`, `#tools`, `#runtime`

---

<a id="item-harness-arch-4"></a>
### [Cloudflare Kitesurf 开源发布](https://blog.cloudflare.com/kitesurf-open-source/) ⭐️ 7.8/10

Cloudflare 专为 AI agent 设计的无状态浏览器 Kitesurf 正式开源，采用 Apache 2.0 协议托管于 GitHub。该浏览器完全运行在 Cloudflare Workers 上，无需浏览器容器，支持 Chrome DevTools Protocol（CDP）与 WebMCP 协议，底层基于 Rust 编译为 WebAssembly 的 Blitz、Stylo、Boa、Linebender、Krilla 等开源组件实现 HTML 解析、CSS 渲染、JavaScript 执行、文本布局与 PDF 输出，相比 Chromium 更省 CPU 与内存，可基于全球 Workers 网络按需扩展。部署到个人 Cloudflare 账号需使用 Workers 付费计划，因依赖 Dynamic Workers 实现页面隔离。

rss · Cloudflare AI · 11月13日 20:20

**「设计要点」** Kitesurf 是无状态服务器 less 浏览器，核心逻辑用 Rust 编写并编译为 WebAssembly 运行在 Cloudflare Workers 上，无需浏览器容器。内部分为管理会话与客户端连接的 Engine、执行页面脚本的 PageScript、负责渲染输出的 PageRenderer 三个核心模块，通过 Dynamic Workers 为每个页面提供隔离环境。

**「改了什么」** 此前 Kitesurf 仅以 Cloudflare 托管的 Browser Run 服务形式提供，本次开源后开发者可自行克隆仓库本地运行，或修改代码后部署到个人 Cloudflare 账号，无需再依赖官方托管 API。

**标签**: `#tools`, `#mcp`, `#sandbox`, `#runtime`

---

## Agent 工程师日报
{: #sec-agent-engineer .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-agent-engineer" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-agent-engineer-1"></a>
### [具身智能体验证器过拟合研究发布](https://huggingface.co/papers/2611.08318) ⭐️ 7.0/10

Hugging Face Daily Papers 于 2026-11-14 推荐了一篇研究具身自我改进智能体的论文。该论文批评将机器人模拟基准测试的成功验证标准暴露给学习智能体的常见做法，指出这会导致代码过拟合到验证器而非完成实际语言指令任务。论文发现验证器标准通常比语言指令要求更严格，因此基准分数可能无法忠实反映任务完成情况。这一发现对设计可靠智能体评估和具身编码智能体开发有直接影响。

rss · Hugging Face Daily Papers · 11月14日 03:38

**「为什么重要」** 随着具身编码智能体报告越来越高的基准分数，该研究揭示了一个关键且未被充分认识的评估缺陷：高分可能来自对验证器的过拟合而非真实任务完成能力。这对当前智能体评估设计构成直接挑战，因为验证器标准暴露可能系统性扭曲智能体行为。

**「可关注」** 可关注：在具身智能体评估中，将验证器成功标准暴露给学习智能体可能导致代码过拟合到验证逻辑而非任务本身，需重新审视评估设计中的标准暴露策略。

**标签**: `#eval`, `#coding-agent`

---

<a id="item-agent-engineer-2"></a>
### [XYBench 发布 评估 XY 问题处理能力](https://huggingface.co/blog/allenai/xybench) ⭐️ 6.8/10

2026 年 11 月 13 日，Hugging Face 博客联合卡内基梅隆大学、NVIDIA、约翰霍普金斯大学发布 XYBench 基准，该基准包含 8115 道跨编程、烹饪、家装等领域的真实问题，由 1557 道 Stack Overflow 问题、184 道 Stack Exchange 问题、102 道人工 curated 问题、6272 道基于 WikiHow 指南生成的问题构成，用于评估 AI 助手识别用户隐含误解（即 XY 问题：用户真实目标为 X，却误以为方案 Y 可行而请求帮助 Y）并优先导向真实目标的能力，成果获 EMNLP 2026 最佳资源论文奖。基准通过实用解决方案、实用侧重、误解识别三个维度评估模型表现，人类评审与自动化判分的一致性达 74.2%-100%。测试的 Claude Sonnet 4.6、GPT-5、Gemini 3.1 Pro、Qwen3.5-9B、DeepSeek-V4 Pro 五款模型均在单轮设置下接受评估，均更倾向提供表面请求的解决方案，底层目标解决方案占比、误解识别率均低于人类参考答案。当前基准仅覆盖英语查询，主要针对单轮程序性问题，多语言、多文化、多轮对话场景的扩展是后续开放方向。

rss · Hugging Face Blog · 11月13日 17:02

**「为什么重要」** XYBench 首次系统量化了 LLM 处理 XY 问题的能力缺口，为评估提示工程或训练方法对「识别隐含意图并优先解决真实目标」的效果提供了可复现的测试集，直接服务于需要处理用户模糊/错误请求的 coding agent 等场景。

**「可关注」** 当前模型存在「能识别正确建议但自身生成时仍优先回应表面请求」的落差，且显式提供用户真实目标反而可能降低模型对错误思路的规避率，提示针对 XY 问题的训练需同时强化意图推断与行为对齐。

**标签**: `#eval`

---

<a id="item-agent-engineer-3"></a>
### [llama.cpp v1.0.0 发布](https://huggingface.co/blog/ggml-org/llama-cpp-v1) ⭐️ 6.8/10

2026-11-13，llama.cpp 与 ggml 同步发布 v1.0.0。项目定位为本地及多模态 AI 推理的轻量级 C/C++ 基础库，支持 150+ 架构变体。核心变化是公开语义化版本规则：major 版本 bump 将标记 \`./include\` 下 public C API 的 breaking change，ABI 不兼容亦同。公告内容截断，未提供具体 breaking changes 列表、迁移指南或性能基准数据，升级成本待评估。

rss · Hugging Face Blog · 11月13日 14:05

**「为什么重要」** v1.0.0 是首个明确承诺长期 API 稳定性的里程碑，下游 harness 和集成方可将其视为可靠依赖。语义化版本规则的公开，使接口兼容性风险可通过版本号预判。

**「可关注」** 可关注：ggml-org 项目已明确 public C API 位于 \`./include\` 目录，semantic versioning 规则将 major 版本与 breaking change 绑定，集成或 fork 时应锁定头文件路径并建立版本变更监控。

**标签**: `#harness`, `#inference`

---

<a id="item-agent-engineer-4"></a>
### [Perplexity Decider v1.3 更新](https://www.perplexity.ai/hub/blog/perplexity-decider) ⭐️ 6.0/10

2026 年 11 月 13 日 Perplexity 发布 Decider v1.3 决策模型，对比 v1.2 基线，其 flash 变体在 AA Decision Index 上得分高 4 分，但部分社区用户反馈整体基准测试表现退步。当前公开材料未披露该版本的具体训练与评估技术细节，社区同时提及 Cloudflare Clairic、ScaleDown Extract 等潜在竞品替代方案。该更新对关注 Agent 路由与决策层的工程师有参考价值。

hackernews · gmays · 11月13日 19:24 · [社区讨论](https://news.ycombinator.com/item?id=50488464)

**「为什么重要」** 该版本是 Perplexity 决策模型线的最新公开迭代，社区已围绕其性能与性价比展开讨论；但其对 Agent orchestration 落地的实际影响尚未有明确验证，目前仅具备方向性参考意义。

**「可关注」** 可关注：Decider v1.3 flash 变体相对前代有小幅基准提升，但社区已出现定价更低的竞品选项，可结合自身 Agent 决策场景的成本与精度需求评估选型。

**「评论」** 社区对 Decider 系列的认可度较高，但就 v1.3 的性能表现存在分歧：部分用户反馈其本地基准表现良好且定价有竞争力，也有用户认为其整体表现不及前代，性价比弱于 ScaleDown Extract 等竞品。

**标签**: `#orchestration`, `#eval`

---

<a id="item-agent-engineer-5"></a>
### [Open Vision Banana 开源配方发布](https://huggingface.co/papers/2611.15844) ⭐️ 6.0/10

Hugging Face Daily Papers 于 2026-11-14 介绍 Open Vision Banana \(OVB\)，一个将预训练图像生成器转换为统一多任务感知系统的完全开源可复现配方。该配方基于 4B 与 9B 参数的开源基础模型，使用 210 万至 380 万对公开数据集训练。论文分析了颜色编码、提示设计、参数适配与任务平衡四类关键设计选择，指出这些选择相互影响，单独有益的组合可能相互损害。当前摘要截断，未提供完整性能数据，且该工作与 AI Agent 工程的相关性较窄。

rss · Hugging Face Daily Papers · 11月14日 03:38

**「为什么重要」** OVB 填补了生成式视觉感知领域完全开源可复现配方的空白，其设计选择交互分析为多任务系统调优提供了可验证基线。但需注意，摘要未披露具体性能指标，且与当前 coding agent 与 harness 场景的直接关联有限。

**「可关注」** 可关注：设计选择间的交互作用意味着复现时需系统化消融，而非孤立验证单因素增益。

**标签**: `#multi-modal-perception`, `#open-reproducibility`, `#generative-models`

---

<a id="item-agent-engineer-6"></a>
### [HF Paper：长期智能体角色研究](https://huggingface.co/papers/2611.17167) ⭐️ 6.0/10

2026-11-14，Hugging Face Daily Papers 发布论文摘要（arXiv 2611.17167），研究决策模型在长期智能体中作为 actor、judge、teacher 的角色差异。实验在 ALFWorld 与 WebShop 基准上对比三个决策模型与三个通用 LLM，发现执行表现差的模型仍可作为有效评判者与教师。作为 actor 时，六种模型均被更易的子目标拉离必须先完成的关键子目标；作为 judge 时，同一模型能正确归功于关键步骤并判断动作是否有帮助。该摘要为二次策展来源，未提供具体性能指标与原始论文全文，结论需以原论文验证。

rss · Hugging Face Daily Papers · 11月14日 03:38

**「为什么重要」** 该研究提示智能体系统设计可将执行、评估、训练角色分离，避免单一模型能力瓶颈。但当前仅为摘要，具体指标与实验细节缺失，实际工程价值需待原论文确认。

**「可关注」** 可关注：评判者与教师角色对模型能力的要求可能与 actor 不同，评估智能体组件时需按角色分别设计基准。

**标签**: `#coding-agent`, `#eval`, `#orchestration`

---

<a id="item-agent-engineer-7"></a>
### [WorldDraft 基准发布 评估视频渲染能力](https://huggingface.co/papers/2611.16217) ⭐️ 6.0/10

2026 年 11 月 14 日，Hugging Face Daily Papers 收录了一篇 arXiv 预印本，该预印本提出 WorldDraft 基准，专门评估多模态编码代理中作为生成渲染器的视频模型能力——这类代理将 4D 世界构建与视觉生成解耦，使视频模型从世界生成器转向渲染器角色。该基准采用 3×3 因子设计，覆盖 48 个可执行 4D 世界家族、6 类动态挑战类别，共 432 组严格配对的测试用例，从「世界保持」（保留预设 4D 运动学与相机路径）和「视觉实现」（持续绑定文本指定的目标属性）两个维度评估渲染器性能。目前仅公开截断摘要，无完整结果、实现细节或性能数据，适用场景局限于多模态编码代理的渲染器评估子领域。

rss · Hugging Face Daily Papers · 11月14日 03:38

**「为什么重要」** 该基准填补了「代码构建 4D 世界、视频模型负责渲染」这一分工范式的结构化评测空白，是首个针对该细分场景的评估资源。但当前仅公开摘要，实际可用性、性能基准等核心信息尚未披露，暂无法验证其对工程实践的落地价值。

**「可关注」** 可关注：WorldDraft 是首个针对多模态编码代理中视频模型渲染能力的结构化基准，若后续公开完整测试集与基线结果，可作为该细分场景的评测工具。

**标签**: `#eval`, `#coding-agent`

---

<a id="item-agent-engineer-8"></a>
### [Qwen3 DSpine 草稿模型上 HF 榜](https://huggingface.co/tencent/Qwen3.8-27B-DSpine-b16) ⭐️ 6.0/10

2026 年 11 月 14 日，Hugging Face Trending 榜单新增 tencent/Qwen3.8-27B-DSpine-b16 模型，当前 trendingScore 为 214，获 248 个赞，标签包含 safetensors、qwen3、dspine、speculative-decoding、draft-model、sglang、text-generation、harness，关联 arXiv 论文 2609.36173。该模型为 Qwen3 系列的推测解码草稿模型，兼容 SGLang 推理框架，目前公开信息仅为基础元数据，无具体性能基准、架构细节或使用限制说明，潜在受众为 LLM 推理优化、agent 推理工作流相关的工程师。

rss · Hugging Face Trending Models · 11月14日 03:38

**「为什么重要」** 推测解码草稿模型是 LLM 推理加速的潜在技术方向，该模型兼容主流推理框架 SGLang，若后续公开有效性能数据，可能为 agent 推理提速提供可选方案，但目前无实证效果信息，尚未证实实际收益。

**「可关注」** 可关注：该模型关联的 arXiv 论文 2609.36173 已公开，可后续跟进论文中的架构与性能细节，评估是否适配自身推理优化需求。

**标签**: `#harness`

---

<a id="item-agent-engineer-9"></a>
### [Qwen3.5-9B 在 PS4 离线运行](https://www.reddit.com/r/LocalLLaMA/comments/1xvbn2m/qwen359b_running_on_a_ps4s_gpu_offline_using_its/) ⭐️ 5.5/10

2026 年 11 月 13 日，开发者/u/leonardo\_alegria 开源 garlic-llm 项目，实现 Qwen3.5-9B 在未改装的 PS4 GPU 上离线运行，开发者自报速度达 31-39 tok/s。项目使用 Qwen3.5 自带的 MTP 头做推测解码，最多草稿 2 个 token，全模型单次 pass 验证，这是提速核心，将速度从之前的 22 tok/s 提升到当前水平。同时采用自定义 4/3-bit 权重量化打包，将模型压缩到约 4.5 GiB，适配 PS4 内存限制。当前性能数据为开发者单方面披露，未经过独立验证，且 PS4 硬件场景极为小众，对主流 coding agent 工作流的直接适用性有限。

reddit · r/LocalLLaMA · /u/leonardo\_alegria · 11月13日 16:00

**「为什么重要」** 该项目已落地验证消费级旧游戏主机 GPU 运行 9B 级开源模型的可行性，同时验证了模型自带 MTP 头、自定义低比特量化打包在极受限边缘设备上的实用价值。但这些技术向主流 coding agent 场景迁移的实际收益尚未得到验证，暂不具备普适参考性。

**「可关注」** 可关注：模型自带 MTP 头用于推测解码、自定义低比特权重量化打包，是适配极受限边缘设备的可行技术路径。

**标签**: `#coding-agent`, `#inference-optimization`, `#quantization`, `#speculative-decoding`, `#edge-deployment`

---

## AI 日报
{: #sec-ai-daily .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-daily" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-daily-1"></a>
### [DeepSeek 全家桶应用 API 发布](https://mp.weixin.qq.com/s?__biz=Mzk0OTYwNzc3NQ==&amp;mid=2247485910&amp;idx=1&amp;sn=529f50ba3b37e39319dad1faf7a122cf) ⭐️ 9.8/10

DeepSeek 官方于 2026 年 11 月 13 日正式发布全家桶应用 API，将 App 内的联网搜索、文件输入、语音交互、深度思考搜索等能力整合进原有 API，开发者仅需开启对应参数即可获得相关功能，无需额外对接外部工具处理调用衔接。目前 V4.1-Flash 模型（deepseek-flash）已在 Messages、Responses、Chat Completions 接口下支持上述能力，相关底层及语音能力还支持 Search、Fetch、OCR、ASR、TTS 等独立接口调用，调用除收取 Token 费用外还会收取对应工具调用费用。

rss · DeepSeek · 11月13日 14:19

**「为什么重要」** 开发者无需自行对接外部工具、处理上下文拼接与工具调用衔接，可直接在自有应用中复刻 DeepSeek App 的完整对话功能，大幅降低复杂对话应用的开发成本。

**「可关注」** 可关注：原有 DeepSeek API 开启对应参数即可调用联网搜索、文件解析、语音交互等能力，无需额外对接外部工具。

**标签**: `#model`, `#lab`, `#product`, `#industry`

---

<a id="item-ai-daily-2"></a>
### [OpenAI 推出 ChatGPT Wallet](https://openai.com/index/introducing-chatgpt-wallet) ⭐️ 7.8/10

OpenAI 官方发布 ChatGPT Wallet，是面向 ChatGPT Work、Codex 等产品内 agent 的支付工具。该工具支持带用户审批的购买功能，同时兼容现有卡保护机制。

rss · OpenAI Blog · 11月13日 15:00

**「为什么重要」** 该工具补齐了 OpenAI 生态内 agent 完成消费场景的支付能力，同时通过用户审批和现有卡保护机制明确了安全使用边界。

**「可关注」** 可关注：ChatGPT Wallet 的 agent 支付需经用户审批，且兼容现有卡保护机制。

**标签**: `#lab`, `#product`, `#industry`

---

<a id="item-ai-daily-3"></a>
### [Shield 用 Forge 代理简化遗留门户交接](https://openai.com/business/customer-stories/shield) ⭐️ 6.3/10

OpenAI 官方博客发布客户案例，安全服务商 Shield 使用 OpenAI 的 Forge 代理，帮助 IT 技术人员自动化操作遗留门户系统完成工作交接。Forge 代理可自主导航遗留门户，让技术人员将精力集中在需要人工判断的问题上。

rss · OpenAI Blog · 11月13日 08:00

**「为什么重要」** 该案例展示了 AI 在 IT 遗留系统运维场景的落地尝试，但未披露技术细节与能力迭代信息，参考价值有限。

**「可关注」** 可关注：Forge 代理在遗留门户系统自动化导航场景的落地表现，后续可追踪其技术细节公开情况。

**标签**: `#industry`, `#lab`, `#product`

---

## AI 羊毛
{: #sec-ai-deals .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-deals" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-deals-1"></a>
### [World Labs Atlas 开放 注册赠 10000 积分](https://www.ifanr.com/1689379?utm_source=rss&amp;utm_medium=rss&amp;utm_campaign=) ⭐️ 9.0/10

李飞飞创办的 World Labs 今日正式开放 Atlas 世界模型，新用户注册即赠 10000 积分，支持网页端体验及开发者 API 调用，体验地址为 atlas.worldlabs.ai。用户可通过网页工具将草图、图片转化为可自由探索的 3D 场景，还可导出至 Blender 或游戏引擎继续加工。领取条件为完成新用户注册，材料未提及有效期。

rss · 爱范儿 · 11月13日 10:04

**「为什么重要」** Atlas 同步上线 Viewfinder、Chisel 等网页工具，10000 免费积分可覆盖单帧渲染、整组渲染等基础操作，无需额外成本即可体验 3D 场景生成全流程，适合快速验证相关能力。

**「可关注」** 可关注：+86 手机号可正常接收注册验证码，但需选择美国/加拿大区域才能正常使用；免费 10000 积分仅够基础体验，生成完整 Splat 需 5000 积分，Chisel API 按 Gemini 4 Argon 每 1M 输出 token 收取 10000 积分。

**标签**: `#credits`, `#free-tier`, `#api`, `#promo`

---

<a id="item-ai-deals-2"></a>
### [Epic 本周免费送《斗阵骑士/Knightica》](https://www.appinn.com/eggs-261113/) ⭐️ 8.0/10

你看到的内容可能由第三方 AI 基于小众软件文章提炼总结而成，可能与原文真实意图存在偏差。不代表小众软件观点和立场。请&lt;a href=&quot;https://www.appinn.com/eggs-261113/&quot; target=&quot;\_blank&quot;&gt;点击链接阅读原文&lt;/a&gt;细致比对和校验。&lt;br /&gt;&lt;br /&gt;2025 年 8 月 21 日发行的回合制类 Roguelike 自走棋游戏《斗阵骑士/Knightica》，本周（11 月 13 日至 11 月 19 日）在 Epic Games Store 限时免费送出，支持电脑端、Android 端、iOS 端领取，领取后永久入库。

rss · 小众软件 · 11月13日 06:01

**「为什么重要」** 本周限时福利，11 月 19 日截止，过期后无法再免费领取，该作 Steam 平台获多半好评，适合喜欢自走棋、兵种站位搭配玩法的玩家入库。

**「可关注」** 可关注：Epic 账号跨平台通用，领取后电脑、Android、iOS 端均可下载游玩。

**标签**: `#limited-free`, `#promo`

---

<a id="item-ai-deals-3"></a>
### [Firefox 内置 VPN 无限流量至 2027 年 1 月](https://blog.mozilla.org/en/firefox/built-in-vpn-unlimited-data/) ⭐️ 8.0/10

Mozilla 官方公告，Firefox 内置免费 VPN 取消流量上限，提供无限流量额度，该优惠有效期至 2027 年 1 月，未提及额外领取限制条件。

rss · HN Free API / Credits · 11月13日 16:05

**「为什么重要」** 该福利为官方明确公示的长期免费额度，有效期清晰可验证，是当前 Firefox 用户可获取的确定性强 VPN 优惠。

**「可关注」** 可关注：当前仅确认无限流量优惠有效期至 2027 年 1 月，后续收费规则、适用设备范围暂未公布。

**标签**: `#free-tier`, `#limited-free`, `#promo`

---