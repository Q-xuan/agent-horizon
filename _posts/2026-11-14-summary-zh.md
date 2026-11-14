---
layout: default
title: "Horizon Summary: 2026-11-14 (ZH)"
date: 2026-11-14
lang: zh
---

> 从 239 条内容中筛选出 20 条重要资讯。

<nav id="ah-toc" class="ah-toc" aria-label="目录"><span class="ah-toc-title">目录</span><ul><li><a href="#sec-harness-arch"><span class="ah-toc-name">Harness 架构</span><span class="ah-toc-count">4条</span></a></li><li><a href="#sec-agent-engineer"><span class="ah-toc-name">Agent 工程师日报</span><span class="ah-toc-count">9条</span></a></li><li><a href="#sec-ai-daily"><span class="ah-toc-name">AI 日报</span><span class="ah-toc-count">4条</span></a></li><li><a href="#sec-ai-deals"><span class="ah-toc-name">AI 羊毛</span><span class="ah-toc-count">3条</span></a></li></ul></nav>

---

**[Harness 架构](#sec-harness-arch)**
1. [Mastra v1.83.0 发布](#item-harness-arch-1) ⭐️ 8.8/10
2. [FastMCP v4.2.0 发布](#item-harness-arch-2) ⭐️ 7.8/10
3. [OpenCode v2.3.0 发布](#item-harness-arch-3) ⭐️ 7.8/10
4. [Cloudflare Kitesurf 开源发布](#item-harness-arch-4) ⭐️ 6.8/10

**[Agent 工程师日报](#sec-agent-engineer)**
1. [Decider v1.3 发布](#item-agent-engineer-1) ⭐️ 8.0/10
2. [XYBench 评测基准发布](#item-agent-engineer-2) ⭐️ 7.8/10
3. [多模态视觉编码解耦实验发布](#item-agent-engineer-3) ⭐️ 7.0/10
4. [具身智能基准验证器过拟合](#item-agent-engineer-4) ⭐️ 7.0/10
5. [llama.cpp v1.0.0 发布](#item-agent-engineer-5) ⭐️ 7.0/10
6. [PS4 离线运行 Qwen3.5-9B](#item-agent-engineer-6) ⭐️ 7.0/10
7. [SO-Arena 基准发布](#item-agent-engineer-7) ⭐️ 6.0/10
8. [HF Daily Paper：决策模型角色研究](#item-agent-engineer-8) ⭐️ 6.0/10
9. [HF trending Qwen3 DSpine 草稿模型](#item-agent-engineer-9) ⭐️ 6.0/10

**[AI 日报](#sec-ai-daily)**
1. [DeepSeek 全家桶应用 API 发布](#item-ai-daily-1) ⭐️ 8.8/10
2. [OpenAI 推出 ChatGPT Wallet](#item-ai-daily-2) ⭐️ 7.8/10
3. [Shield 用 OpenAI 处理遗留门户任务](#item-ai-daily-3) ⭐️ 5.8/10
4. [谷歌发布 Gemini 4 Hydrogen](#item-ai-daily-4) ⭐️ 5.0/10

**[AI 羊毛](#sec-ai-deals)**
1. [World Labs Atlas 开放 赠 10000 积分](#item-ai-deals-1) ⭐️ 8.0/10
2. [Firefox 内置免费 VPN 取消流量上限](#item-ai-deals-2) ⭐️ 8.0/10
3. [本周赛博领鸡蛋：Epic 免费送《斗阵骑士》](#item-ai-deals-3) ⭐️ 7.0/10

---

## Harness 架构
{: #sec-harness-arch .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-harness-arch" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-harness-arch-1"></a>
### [Mastra v1.83.0 发布](https://github.com/mastra-ai/mastra/releases/tag/%40mastra/core%401.83.0) ⭐️ 8.8/10

mastra-ai/mastra 发布 @mastra/core@1.83.0。所有 Agent 原生支持可恢复运行流，带重放缓存与跨实例 observe/abort 控制。@mastra/server 新增内置 MCP 端点 \`/api/mcp\`，支持 OAuth 发现与受众检查。实验性工作流存储 v2 采用 delta-write，支持 Postgres 与 libSQL，减少长流程写入量。

github · PaulieScanlon · 11月13日 14:32

**「设计要点」** 运行时通过流主题发布与重放缓存实现断线重连，所有权与 TTL 机制防止客户端重连时误杀运行。内置 MCP 服务器默认随 \`server.auth\` 启用，OAuth 元数据与受众校验通过 \`server.mcp.oauth\` 配置；工作流存储 v2 按步持久化差异，通过异步 \`steps\(\)\` 懒加载历史步骤。

**「改了什么」** 所有 Agent 获得可恢复流能力，\`agent.observe\(runId\)\` 与 \`abortRunStream\(runId\)\` 成为跨实例控制接口；\`Agent.durable\` 选项语义收窄为仅控制可恢复流，checkpoint-backed durable execution 迁移至 \`createDurableAgent\(\{ agent \}\)\`。调度系统新增一次性 \`runAt\` 与边界 \`endAt\` 参数。

**标签**: `#runtime`, `#mcp`, `#tools`, `#prefix-cache`

---

<a id="item-harness-arch-2"></a>
### [FastMCP v4.2.0 发布](https://github.com/PrefectHQ/fastmcp/releases/tag/v4.2.0) ⭐️ 7.8/10

FastMCP v4.2.0 引入服务器端 agent skill 分发机制，替换原有的本地 skill 文件夹部署模式。新版本通过实验性 MCP Skills extension（SEP 2640）实现集中式、版本化的 skill 目录，server 端使用 SkillCatalogProvider 托管 skill，client 端通过 read\_skill\(\) 和 to\_directory\(\) 完成验证与安装。同时新增 Annotated 依赖注入支持，允许依赖声明工具参数。

github · zzstoatzz · 11月13日 17:07

**「设计要点」** Server 端通过 SkillCatalogProvider 和 SkillManifestProvider 托管 skill，与 tools 同址部署，一次更新覆盖所有读取的 agent。Client 端通过 hashed manifest 验证文件完整性，支持 mount、proxy、ClientGroup 和 AuthMiddleware 透传。部署模型从本地 per-agent 副本改为集中式 server-hosted catalog。

**「改了什么」** 服务器端 skill 分发替代本地文件夹，新增 SkillCatalogProvider 与 SkillManifestProvider，client 通过 read\_skill\(\) 和 to\_directory\(\) 完成验证安装。依赖注入支持 Annotated 与 CallArgument，4.1 skills API 废弃，Skill 类成为作者入口，wire model 改名为 MCPSkill，要求 Python 3.11+。

**标签**: `#mcp`, `#tools`, `#runtime`

---

<a id="item-harness-arch-3"></a>
### [OpenCode v2.3.0 发布](https://github.com/anomalyco/opencode/releases/tag/v2.3.0) ⭐️ 7.8/10

OpenCode v2.3.0 默认启用后台子代理执行，子代理立即返回 session ID 并在空闲时向父代理报告结果，支持父/子会话并发工作。TUI 默认将工具调用和思考汇总为可折叠活动行，verbosity 默认设为 low，保留用户既有设置。桌面应用新增 prompt 跳转功能，支持跨当前 session 搜索并定位历史 prompt。此外，该版本实验性支持 MCP 事件，shell 命令在服务器 handoff 中保持输出，本地模型发现超时从 1 秒延长至 15 秒，提供方支持客户端证书配置以实现双向 TLS。

github · github-actions\[bot\] · 11月13日 08:55

**「设计要点」** 子代理默认后台运行改变父/子交互模型，父会话无需等待即可继续工作。TUI 采用可折叠 transcript 设计降低视觉噪音，同时保留用户 verbosity 配置。提供方支持客户端证书配置以实现双向 TLS，shell 命令通过进程守护程序实现服务器切换时的输出保持。

**「改了什么」** 子代理默认改为后台执行并立即返回 session ID。TUI transcript 默认汇总为单行可折叠活动，verbosity 默认 low。桌面应用新增 Cmd+Alt+G / Ctrl+Alt+G 跳转 prompt。shell 命令在服务器 handoff 中保持输出，超时后实验性支持后台运行。本地模型发现等待时间从 1 秒增至 15 秒。提供方新增 cert、key、passphrase 配置支持双向 TLS。

**标签**: `#subagents`, `#runtime`

---

<a id="item-harness-arch-4"></a>
### [Cloudflare Kitesurf 开源发布](https://blog.cloudflare.com/kitesurf-open-source/) ⭐️ 6.8/10

Cloudflare 于 2026-11-13 宣布将面向 AI agent 的无状态浏览器 Kitesurf 以 Apache 2.0 许可证开源。Kitesurf 完全运行在 Cloudflare Workers 上，无需浏览器容器，支持 Chrome DevTools Protocol（CDP）与 WebMCP 协议，可解析 HTML、执行页面 JavaScript、渲染截图，资源消耗低于完整 Chromium 浏览器，可按需扩展。用户可自行克隆仓库本地运行，也可部署到自己的 Cloudflare Workers 账号，部署需 Workers 付费计划，因依赖 Dynamic Workers 为页面创建隔离环境。

rss · Cloudflare AI · 11月13日 20:20

**「设计要点」** Kitesurf 核心由 Rust 编写并编译为 WebAssembly，依赖 Blitz（HTML 解析/DOM/布局/绘制）、Stylo（CSS 解析/级联/计算样式）、Boa（WebAssembly 内执行 JavaScript，仅在无法使用 Dynamic Workers 运行 JS 时作为后备）、Linebender 库（文本布局/2D 图形）、Krilla（PDF 输出）等开源组件。运行时分为 Engine（管理浏览器会话与客户端连接）、PageScript（运行页面及 JavaScript）、PageRenderer（绘制渲染结果）三个核心部分，所有包、核心、DOM 兼容层、渲染器、CLI 均独立存放在仓库的 packages 目录下。

**「改了什么」** 此前 Kitesurf 仅作为 Cloudflare 托管的 Browser Run 服务的一部分提供，用户无法自行控制实例。本次开源后，开发者可阅读、修改代码，本地运行实例，或部署到自有 Cloudflare 账号，不再依赖 Cloudflare 的托管 API。此前 9 月版本已新增 WebMCP 支持、新 API 与兼容性改进，本次开源是对此前承诺的落地。

**标签**: `#runtime`, `#tools`, `#mcp`

---

## Agent 工程师日报
{: #sec-agent-engineer .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-agent-engineer" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-agent-engineer-1"></a>
### [Decider v1.3 发布](https://www.perplexity.ai/hub/blog/perplexity-decider) ⭐️ 8.0/10

2026 年 11 月 13 日 Perplexity 发布 Decider v1.3，是面向智能体路由场景的小型决策模型，公开了训练方法、评估结果与落地用例。社区讨论显示该版本与 v1.2 基准表现接近，flash 版本较 v1.2 flash 高 4 分；其 locate 机制与 Cloudflare Clairic、ScaleDown Extract 功能对等，已有用户将其作为停服的 Inception Labs Mercury 模型的替代方案。当前无官方公开的完整基准数据，实际性能待验证。

hackernews · gmays · 11月13日 19:24 · [社区讨论](https://news.ycombinator.com/item?id=50488464)

**「为什么重要」** 它首次公开 Perplexity 决策模型的训练与评估细节，为智能体编排场景提供新可选方案；但社区对其性能优势、flash 版本定位的合理性仍有分歧，实际落地效果待更多验证。

**「可关注」** 可关注：决策模型的 flash 版本定位合理性、与同类路由/提取模型（Cloudflare Clairic、ScaleDown Extract）的成本性能对比，以及双向注意力对决策任务的实际增益。

**「评论」** 社区评价存在分歧：部分用户认为其本地基准表现优于 v1.2、定价有竞争力，也有用户反馈决策索引基准表现不及 v1.2；同时有用户指出其 locate 机制与 Cloudflare Clairic、ScaleDown Extract 功能对等，后者成本更低。

**标签**: `#coding-agent`, `#orchestration`, `#eval`

---

<a id="item-agent-engineer-2"></a>
### [XYBench 评测基准发布](https://huggingface.co/blog/allenai/xybench) ⭐️ 7.8/10

2026 年 11 月 13 日 Hugging Face 博客发布 XYBench 评测基准，由 Allen AI 联合卡内基梅隆大学、NVIDIA、约翰霍普金斯大学研发，包含 8115 道覆盖编程、烹饪、家居维修等场景的 XY 问题测试题，用于评估 AI 助手识别用户表面请求背后真实需求、纠正错误假设的能力。该基准获 EMNLP 2026 最佳资源论文奖，测试维度涵盖务实解决方案覆盖、回答侧重点、错误假设识别三项，采用 Claude Sonnet 4.5 作为自动评判员，人类评审一致性达 74.2%-100%。当前该基准仅覆盖英语查询和程序性问题，多语言、多文化、多轮对话场景的扩展仍待推进，面向 AI 助手、coding agent 研发人员提供意图理解与问题诊断能力的量化评测工具。

rss · Hugging Face Blog · 11月13日 17:02

**「为什么重要」** XYBench 首次系统量化了主流 AI 助手处理 XY 问题的能力缺口：当前测试的 Claude Sonnet 4.6、GPT-5、Gemini 3.1 Pro 等模型均更倾向于解决用户表面提出的错误请求，而非背后的真实目标，且识别到正确建议和实际输出正确建议存在明显能力 gap。该基准可用于验证提示词调整、训练优化对模型意图推断和实际行为改善的效果，但尚未有公开证据证明基于该基准的优化能直接提升实际产品表现。

**「可关注」** 可关注：模型识别正确建议与实际输出正确建议存在明显能力 gap，且明确告知用户真实目标后错误假设识别率未同步提升，提示意图推断和意图对齐是两类需要单独优化的能力。

**标签**: `#eval`

---

<a id="item-agent-engineer-3"></a>
### [多模态视觉编码解耦实验发布](https://huggingface.co/papers/2611.17334) ⭐️ 7.0/10

Hugging Face Daily Papers 于 2026-11-14 收录论文，提出控制预训练框架，可单独评估多模态视觉编码器的三个设计选择：上游视觉先验、专用视觉容量、预融合位置。研究在匹配 lifetime compute 条件下，于 VQA 和语言基准完成对比实验。此前这些设计选择因数据、架构和计算量差异难以隔离，该框架通过统一预训练数据和计算预算实现解耦。论文具体实验结果未在摘要中完整呈现。

rss · Hugging Face Daily Papers · 11月14日 02:52

**「为什么重要」** 此前多模态视觉编码器的设计选择常被数据、架构和计算量混杂，无法独立评估贡献。该框架提供控制变量方法，对构建处理视觉输入的智能体有参考价值。

**「可关注」** 在匹配计算量下对比视觉编码器三要素（上游先验、专用容量、预融合位置）的控制变量框架，可复现的实验设计。

**标签**: `#coding-agent`, `#eval`, `#multimodal`

---

<a id="item-agent-engineer-4"></a>
### [具身智能基准验证器过拟合](https://huggingface.co/papers/2611.08318) ⭐️ 7.0/10

Hugging Face Daily Papers 2026-11-14 推荐 arXiv 论文 2611.08318，指出具身自改进智能体基准测试中的 Criteria Exposure 问题：向智能体暴露成功验证标准会导致其生成过拟合验证器的机器人控制程序，而非完成语言指令要求的实际任务。这些验证标准最初为模仿学习训练的策略设计，往往比语言指令更严格，因此验证器分数可能无法忠实反映任务完成度。该现象对具身编码智能体的评估基准设计构成挑战。

rss · Hugging Face Daily Papers · 11月14日 02:52

**「为什么重要」** 随着具身编码智能体的基准分数持续升高，区分真正完成任务与过拟合验证器成为评估有效性的核心问题。该论文揭示的 Criteria Exposure 机制直接影响基准设计可靠性。

**「可关注」** 可关注：设计具身智能体评估时，需隔离任务指令与验证标准，避免智能体通过验证器过拟合获得虚假高分。

**标签**: `#eval`, `#coding-agent`

---

<a id="item-agent-engineer-5"></a>
### [llama.cpp v1.0.0 发布](https://www.reddit.com/r/LocalLLaMA/comments/1xv8t2e/llamacpp_v10_is_here/) ⭐️ 7.0/10

2026-11-13，Hugging Face 团队成员 Merve 在 Reddit 宣布 llama.cpp v1.0.0 稳定版发布，底层张量库 ggml 同步升至 v1.0.0。项目自此采用语义版本控制，MAJOR 版本 bump 将明确标识公共 C API（./include）的破坏性变更。当前支持 150 余种架构变体及所有主流推测解码方法，后端以动态库形式按需加载，分发渠道覆盖 Docker、Debian、Homebrew、conda-forge、MacPorts、Winget 与 XCFramework。同期发布的 Llama desktop apps（MacOS、Windows）基于该库构建，面向终端用户降低本地 AI 使用门槛。

reddit · r/LocalLLaMA · /u/unofficialmerve · 11月13日 14:07

**「为什么重要」** v1.0.0 将 API/ABI 稳定性纳入语义版本承诺，直接影响下游 agent 工具链的集成策略。桌面应用的上线可能改变本地模型部署的交互方式，但具体采用率尚不明确。

**「可关注」** 可关注：llama.cpp 进入语义版本控制时代，MAJOR 版本将明确标注公共 C API 破坏性变更，下游工具链需提前建立版本锁定或兼容性测试机制。

**标签**: `#coding-agent`, `#toolchain`

---

<a id="item-agent-engineer-6"></a>
### [PS4 离线运行 Qwen3.5-9B](https://www.reddit.com/r/LocalLLaMA/comments/1xvbn2m/qwen359b_running_on_a_ps4s_gpu_offline_using_its/) ⭐️ 7.0/10

开发者 /u/leonardo\_alegria 开源 garlic-llm 项目，实现 Qwen3.5-9B 模型在未改装的 PS4 主机 GPU 上离线运行，推理速度达 31–39 tokens/秒。项目使用 Qwen3.5 自带的 MTP 头执行推测解码，通过该头一次最多草稿 2 个 token、全模型单次校验的机制，将推理速度从 baseline 的 22 tokens/秒提升至当前水平，同时采用自定义 4/3-bit 量化方案将模型权重压缩至 4.5 GiB 以内，适配 PS4 的有限显存。模型支持对话、语音输入、代码生成三类任务，无需云服务、订阅或额外安装 Linux 系统，代码与模型权重已公开托管。

reddit · r/LocalLLaMA · /u/leonardo\_alegria · 11月13日 16:00

**「为什么重要」** 该案例验证了消费级老旧硬件运行 9B 规模开源模型的可行性，为边缘 LLM 部署、推测解码实现、本地 agent 工具适配提供了可复现的技术参考。

**「可关注」** 可关注：原生 MTP 头用于推测解码可在老旧 GPU 上带来明显的推理速度提升，自定义低比特量化是适配有限显存约束的核心手段。

**标签**: `#harness`, `#coding-agent`, `#edge-deployment`, `#speculative-decoding`

---

<a id="item-agent-engineer-7"></a>
### [SO-Arena 基准发布](https://huggingface.co/papers/2611.15777) ⭐️ 6.0/10

2026 年 11 月 14 日，Hugging Face Daily Papers 发布 SO-Arena 基准，面向快速低 token 决策的 System One 模型（与 agent 用例相关），用于评估其能力谱系与决策可靠性，覆盖 11 个领域、5 个能力族，支持基于可靠来源的证据锚定评估、领域特定细粒度难度评估。当前公开内容被截断，未披露基准可用性、与现有评估套件的性能对比、针对 agent 工程的具体指导，目前影响仅限 System One 模型评估的小众领域。

rss · Hugging Face Daily Papers · 11月14日 02:52

**「为什么重要」** 该基准目前仅公开核心设计框架，未披露可用性、横向对比结果和 agent 工程适配细节，对 System One 模型评估小众领域有参考价值，暂未证实对通用 agent 工程社区的广泛影响。

**「可关注」** 可关注：SO-Arena 针对 System One 模型设计了细粒度难度与证据锚定评估机制，若后续公开可用可补充 agent 快速决策模型的评估维度。

**标签**: `#eval`

---

<a id="item-agent-engineer-8"></a>
### [HF Daily Paper：决策模型角色研究](https://huggingface.co/papers/2611.17167) ⭐️ 6.0/10

2026-11-14，Hugging Face Daily Papers 发布论文摘要，探讨决策模型在长时域智能体中作为演员、评判者与教师的角色差异。研究比较 3 个决策模型和 3 个通用 LLM 在 ALFWorld 与 WebShop 基准上的表现：作为演员时，所有模型均被更容易的子目标拉离必须先完成的必要子目标；作为评判者时，能看到完整轨迹的模型能正确归功于朝向正确子目标的步骤。论文进一步使用 JEV 作为教师训练策略，但内容截断导致完整技术细节与具体性能数据缺失。该研究对做 agent eval 与 harness 的工程师有直接参考价值。

rss · Hugging Face Daily Papers · 11月14日 02:52

**「为什么重要」** 论文提出“表现差的决策模型仍可能成为有效教师”的研究问题，这挑战了仅以执行能力评判决策模型的常规标准。若该结论成立，将直接影响智能体训练流程中教师模型的选择标准，但具体性能提升幅度与泛化能力仍需完整论文验证。

**「可关注」** 可关注：决策模型在“即时动作选择”与“完整轨迹评判”任务上的能力可能存在显著差异，设计 agent harness 时应区分执行场景与评估场景的模型选型。

**标签**: `#eval`, `#harness`

---

<a id="item-agent-engineer-9"></a>
### [HF trending Qwen3 DSpine 草稿模型](https://huggingface.co/tencent/Qwen3.8-27B-DSpine-b16) ⭐️ 6.0/10

2026 年 11 月 14 日，Hugging Face trending 榜单新增 tencent/Qwen3.8-27B-DSpine-b16 模型，trendingScore 为 211，累计获得 245 个赞。该模型基于 Qwen3，属于支持推测解码的草稿模型，兼容 SGLang，关联 arxiv 论文 2609.36173，标签包含 dspine、speculative-decoding、draft-model、sglang。目前无公开技术细节、性能数据或实际落地用例，对 agent 推理 harness 优化的实际价值待验证，面向关注推理加速的 AI Agent 工程师。

rss · Hugging Face Trending Models · 11月14日 02:52

**「为什么重要」** 该模型作为 Hugging Face trending 榜单的 Qwen3 基推测解码草稿模型，理论上可能为 agent 推理加速提供新方向，但当前缺乏可验证的技术细节与性能数据，其实际优化效果尚未得到证实。

**「可关注」** 可关注该模型关联的 arxiv 论文 2609.36173，以及后续公开的技术细节与 SGLang 兼容性实测结果，评估其对 agent 推理加速的可用性。

**标签**: `#harness`

---

## AI 日报
{: #sec-ai-daily .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-daily" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-daily-1"></a>
### [DeepSeek 全家桶应用 API 发布](https://mp.weixin.qq.com/s?__biz=Mzk0OTYwNzc3NQ==&amp;mid=2247485910&amp;idx=1&amp;sn=529f50ba3b37e39319dad1faf7a122cf) ⭐️ 8.8/10

DeepSeek 2026 年 11 月 13 日正式发布全家桶应用 API，将原 App 专属的联网搜索、文件输入、语音交互等能力整合进原有 API，开发者仅需开启对应参数即可调用，无需额外对接外部工具。目前 V4.1-Flash 模型（deepseek-flash）已在 Messages、Responses、Chat Completions 接口下支持上述能力，调用扩展功能除 Token 费用外还需支付对应工具调用费。若对外提供应用服务，需开启安全校验参数，并承担内容安全审核、大模型登记、AI 标识等义务。

rss · DeepSeek · 11月13日 14:19

**「为什么重要」** 这套 API 直接开放了 DeepSeek App 的完整交互能力，省去开发者自行对接外部工具、处理调用衔接的重复工作，可大幅降低构建类 DeepSeek 对话应用的门槛。

**「可关注」** 可关注：新版 API 支持联网搜索、OCR、ASR、TTS 等底层能力独立调用，官方已开源对应前端 Demo 与示例代码，对外提供服务需开启安全校验参数并履行内容安全相关义务。

**标签**: `#lab`, `#product`, `#industry`

---

<a id="item-ai-daily-2"></a>
### [OpenAI 推出 ChatGPT Wallet](https://openai.com/index/introducing-chatgpt-wallet) ⭐️ 7.8/10

OpenAI 正式推出 ChatGPT Wallet 安全支付系统，支持 ChatGPT Work、Codex 及 dots 等平台上的 AI 代理在获得用户授权后完成消费，同时沿用现有卡片保护机制。

rss · OpenAI Blog · 11月13日 15:00

**「为什么重要」** 这为 AI 代理的合规消费场景提供了基础支付能力，同时通过用户授权和既有卡片保护机制降低支付风险。

**「可关注」** 可关注：ChatGPT Wallet 的用户授权逻辑与现有卡片保护规则的适配实现。

**标签**: `#product`, `#lab`, `#industry`

---

<a id="item-ai-daily-3"></a>
### [Shield 用 OpenAI 处理遗留门户任务](https://openai.com/business/customer-stories/shield) ⭐️ 5.8/10

OpenAI 官方博客 2026 年 11 月 13 日发布客户案例，介绍 Shield 公司基于 OpenAI 技术构建 Forge 智能体。该智能体可自动导航遗留门户系统完成常规任务，帮助 IT 技术人员将精力集中在需要人工判断的问题上。案例未披露具体效率提升数据与部署限制。

rss · OpenAI Blog · 11月13日 08:00

**「为什么重要」** 该案例展示了 OpenAI 技术在传统 IT 运维场景的落地路径，对处理遗留系统的团队有参考价值，但影响面有限。

**「可关注」** 可关注：Forge 智能体对遗留门户系统的自动导航能力，可作为 IT 运维场景中重复任务自动化的参考方案。

**标签**: `#industry`, `#product`, `#lab`

---

<a id="item-ai-daily-4"></a>
### [谷歌发布 Gemini 4 Hydrogen](https://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw==&amp;mid=2247943733&amp;idx=3&amp;sn=745bfc3f58406752d2d63db1306d234c) ⭐️ 5.0/10

据量子位报道，谷歌发布 Gemini 4 Hydrogen 轻量模型，接替 Gemini 3.8 Flash，官方宣称其任务完成速度较上代提升 2.5 倍，代码能力提升 3 倍，幻觉率下降 5 倍；在 Artificial Analysis 综合智能指数 High 档位得分 51 分，超过 Gemini 4 Argon 的 50 分，xhigh 档位得分 54 分。该模型支持 Low、Medium、High、xhigh 四档思考强度，100 万 Token 上下文窗口内输入定价 1.5 美元/百万 Token，输出定价 7.5 美元/百万 Token，已向全球用户开放。谷歌同步推出 Orchestrator 协同调度器，可动态分配 Gemini 4 Carbon 与 Hydrogen 的任务，测试显示该方案任务成功率接近单独使用 Carbon，同时平均减少 24%配额消耗，完成速度提升 19%。

rss · 量子位 · 11月13日 02:54

**「为什么重要」** 该模型是谷歌首次明确落地大小模型搭配的 Agent 执行方案，小模型在代码、长程 Agent 任务上的性能表现亮眼，同时降低推理成本，对 coding agent 的架构设计有直接参考价值。

**「可关注」** 可关注：Gemini 4 Hydrogen 与 Carbon 的 Orchestrator 大小模型搭配方案，在接近大模型任务成功率的同时降低 24% Token 消耗。

**标签**: `#model`, `#lab`, `#industry`, `#product`

---

## AI 羊毛
{: #sec-ai-deals .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-deals" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-deals-1"></a>
### [World Labs Atlas 开放 赠 10000 积分](https://www.ifanr.com/1689379?utm_source=rss&amp;utm_medium=rss&amp;utm_campaign=) ⭐️ 8.0/10

李飞飞创办的 World Labs 正式开放 Atlas 世界模型，新用户注册即赠 10000 积分，同步上线网页应用与开发者 API，体验地址为 atlas.worldlabs.ai。领取需完成手机号验证，注册后需选择美国或加拿大地区以确保功能正常，材料未提及领取截止时间。

rss · 爱范儿 · 11月13日 10:04

**「为什么重要」** Atlas 支持从草图、单张图片生成可自由探索的 3D 场景，配套 Viewfinder、Chisel、Relight、Splat to mesh 四款工具覆盖场景生成到导出的全链路，10000 积分足够体验核心功能，适合 3D 内容创作者、交互开发者试用。

**「可关注」** 可关注：+86 手机号可完成注册，但需手动选择美国/加拿大地区；免费积分消耗较快，生成完整 Splat 需 5000 积分、Chisel 整组渲染需 160 积分，大额生成需额外注意积分余额。

**标签**: `#credits`, `#free-tier`, `#api`, `#promo`, `#limited-free`

---

<a id="item-ai-deals-2"></a>
### [Firefox 内置免费 VPN 取消流量上限](https://blog.mozilla.org/en/firefox/built-in-vpn-unlimited-data/) ⭐️ 8.0/10

Mozilla 官方宣布 Firefox 内置免费 VPN 取消数据流量限制，该福利有效期至 2027 年 1 月。材料未提及领取条件、地区限制等额外细则。

rss · HN Free API / Credits · 11月13日 16:05

**「为什么重要」** 该调整是 Mozilla 官方推出的限时免费福利，在 2027 年 1 月前使用 Firefox 内置 VPN 无需支付流量超额费用，可满足用户的轻量跨境访问需求。

**「可关注」** 可关注：该福利仅覆盖 Firefox 内置 VPN 服务，未公开地区限制、速率上限等细则，使用前需确认当地网络监管要求。

**标签**: `#free-tier`, `#promo`, `#limited-free`

---

<a id="item-ai-deals-3"></a>
### [本周赛博领鸡蛋：Epic 免费送《斗阵骑士》](https://www.appinn.com/eggs-261113/) ⭐️ 7.0/10

你看到的内容可能由第三方 AI 基于小众软件文章提炼总结而成，可能与原文真实意图存在偏差。不代表小众软件观点和立场。请&lt;a href=&quot;https://www.appinn.com/eggs-261113/&quot; target=&quot;\_blank&quot;&gt;点击链接阅读原文&lt;/a&gt;细致比对和校验。&lt;br /&gt;&lt;br /&gt;少数派本周赛博领鸡蛋栏目更新，Epic Games Store 本周限时免费送出回合制类 Roguelike 自走棋游戏《斗阵骑士 / Knightica》，支持手机端与电脑端领取。

rss · 小众软件 · 11月13日 06:01

**「为什么重要」** 本周为该游戏限时免费领取周期，支持多端获取，适合喜欢自走棋、策略搭配的玩家入手。

**「可关注」** 可关注：Epic Games Store 本周限免的《斗阵骑士》包含 PC、Android、iOS 三个版本，对应领取链接可在原文中找到。

**标签**: `#limited-free`, `#promo`, `#game`

---