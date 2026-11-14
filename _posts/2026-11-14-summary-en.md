---
layout: default
title: "Horizon Summary: 2026-11-14 (EN)"
date: 2026-11-14
lang: en
---

> From 239 items, 20 important content pieces were selected

---

**Agent Harness Architecture**
1. [Mastra core 1.83.0 发布](#item-harness-arch-1) ⭐️ 8.8/10
2. [FastMCP v4.2.0 发布](#item-harness-arch-2) ⭐️ 7.8/10
3. [OpenCode v2.3.0 发布](#item-harness-arch-3) ⭐️ 7.8/10
4. [Kitesurf 开源 Apache 2.0 版本](#item-harness-arch-4) ⭐️ 6.8/10

**AI Agent Engineer**
1. [Perplexity Decider v1.3 发布](#item-agent-engineer-1) ⭐️ 8.0/10
2. [XYBench 评测基准发布](#item-agent-engineer-2) ⭐️ 7.8/10
3. [HF 论文：解耦多模态视觉编码三要素](#item-agent-engineer-3) ⭐️ 7.0/10
4. [HF 论文：Criteria Exposure 导致验证器过拟合](#item-agent-engineer-4) ⭐️ 7.0/10
5. [llama.cpp v1.0.0 发布](#item-agent-engineer-5) ⭐️ 7.0/10
6. [Qwen3.5-9B 实现 PS4 离线运行](#item-agent-engineer-6) ⭐️ 7.0/10
7. [SO-Arena Benchmark 发布](#item-agent-engineer-7) ⭐️ 6.0/10
8. [HF 长程智能体决策模型角色研究](#item-agent-engineer-8) ⭐️ 6.0/10
9. [tencent Qwen3 DSpine 模型 trending](#item-agent-engineer-9) ⭐️ 6.0/10

**AI Daily**
1. [DeepSeek 全家桶应用 API 发布](#item-ai-daily-1) ⭐️ 8.8/10
2. [ChatGPT Wallet 上线 支持代理支付](#item-ai-daily-2) ⭐️ 7.8/10
3. [Shield Uses OpenAI to Automate Legacy Portal Tasks](#item-ai-daily-3) ⭐️ 5.8/10
4. [谷歌发布Gemini 4 Hydrogen](#item-ai-daily-4) ⭐️ 5.0/10

**AI Deals**
1. [Atlas 世界模型开放 赠10000积分](#item-ai-deals-1) ⭐️ 8.0/10
2. [Firefox Built-in VPN Removes Data Limit](#item-ai-deals-2) ⭐️ 8.0/10
3. [This Week Epic Free Game: Knightica](#item-ai-deals-3) ⭐️ 7.0/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [Mastra core 1.83.0 发布](https://github.com/mastra-ai/mastra/releases/tag/%40mastra/core%401.83.0) ⭐️ 8.8/10

Mastra 发布 @mastra/core@1.83.0，引入可恢复 Agent 流、内置 MCP 服务器与 OAuth 发现，以及实验性工作流存储版本 2。所有 Agent 现在发布带重放缓存的运行流，支持 \`agent.observe\(runId\)\` 跨实例观察与 \`observe\(\).abort\(\)\` 或 \`agent.abortRunStream\(runId\)\` 中止，客户端断线后重连不终止运行。内置 MCP 端点 \`/api/mcp\` 在配置 \`server.auth\` 时默认启用，支持 \`server.mcp.oauth\` 发现与受众检查， introspection 路由为 \`GET /api/mcp/builtin\`。实验性 \`storageVersion: 2\` 仅持久化每步增量变更，现已支持 \`@mastra/pg\` 与 \`@mastra/libsql\`，结果可通过异步 \`steps\(\)\` 懒加载步骤历史。

github · PaulieScanlon · Nov 13, 14:32

**「设计要点」** 可恢复流基于主题发布与重放缓存，跨实例通过 runId 观察运行，所有权与 TTL 机制防止重连误杀。内置 MCP 服务器集成于 \`@mastra/server\`，通过 \`server.mcp\` 配置工具集与访问控制，OAuth 元数据由 Auth provider 可选实现 \`getOAuthMetadata\(\)\` 与 \`verifyAudience\(\)\` 提供，\`CompositeAuth\` 合并授权服务器并检查受众。

**「改了什么」** \`Agent\` 的 \`durable\` 选项现仅控制可恢复流，检查点持久执行需迁移至 \`createDurableAgent\(\{ agent \}\)\`。新增 \`chatRoute\(\{ resumable: true \}\)\` 生成 POST 与重连 GET 端点对，支持 \`useChat\(\{ resume: true \}\)\`，并支持 \`server.apiRoutes: \[routes\]\` 显式路由数组配置。调度器新增一次性执行 \`runAt\` 与带结束时间的循环执行 \`endAt\`，\`cron\` 变为可选。

**Tags**: `#runtime`, `#mcp`, `#tools`, `#prefix-cache`

---

<a id="item-harness-arch-2"></a>
### [FastMCP v4.2.0 发布](https://github.com/PrefectHQ/fastmcp/releases/tag/v4.2.0) ⭐️ 7.8/10

FastMCP v4.2.0 将 agent 技能从本地文件夹迁移到服务端集中托管。服务器通过实验性 MCP Skills 扩展（SEP 2640）提供技能目录，客户端用 \`Client.read\_skill\(\)\` 和 \`to\_directory\(\)\` 拉取并校验后安装。技能随工具一起部署，一次更新覆盖所有读取该服务的 agent。依赖声明支持 \`Annotated\[dict, Depends\(get\_config\)\]\` 语法，参数保持真实类型。

github · zzstoatzz · Nov 13, 17:07

**「设计要点」** 技能以资源形式暴露，客户端通过哈希清单校验文件完整性。技能在 mount、proxy、ClientGroup 和 AuthMiddleware 中透传，保持与现有 FastMCP 运行时一致。

**「改了什么」** 服务端新增 \`SkillCatalogProvider\` 和 \`SkillManifestProvider\`，将技能部署模型从本地文件夹改为服务端集中托管。4.1 版技能 API 废弃，\`Skill\` 类成为作者入口，线缆模型改名为 \`MCPSkill\`，最低 Python 版本升至 3.11。

**Tags**: `#mcp`, `#tools`, `#runtime`

---

<a id="item-harness-arch-3"></a>
### [OpenCode v2.3.0 发布](https://github.com/anomalyco/opencode/releases/tag/v2.3.0) ⭐️ 7.8/10

OpenCode v2.3.0 发布。默认启用后台子代理执行，子代理立即返回会话 ID 并在空闲时汇报，支持父会话并发工作。TUI 默认折叠工具调用与思考步骤为单行活动，保留既有 \`session.verbosity\` 设置。桌面应用新增 \`Cmd+Alt+G\` / \`Ctrl+Alt+G\` 跳转到历史提示。技术层面新增 \`mcp\_events\`、\`shell\_timeout\_background\` 实验性标志，Windows Shell 走进程守护，Provider 支持 \`settings.tls\` 客户端证书，本地模型发现超时延长至 15 秒。

github · github-actions\[bot\] · Nov 13, 08:55

**「设计要点」** 运行时转向后台优先子代理模型，子代理立即返回会话 ID 并在空闲时向父代理汇报，支持并发执行。TUI 默认低 verbosity 折叠转录本，保留用户既有配置。Shell 与本地模型发现层引入进程守护和超时后台化实验性标志，本地模型发现单请求超时延长至 15 秒。

**「改了什么」** 子代理默认后台执行并立即返回会话 ID；TUI 转录本默认折叠工具与思考步骤，保留 \`session.verbosity\`；桌面应用新增跳转历史提示快捷键；新增 \`mcp\_events\` 与 \`shell\_timeout\_background\` 实验性标志；Windows 本地 Shell 通过进程守护运行；Provider 支持 \`settings.tls\` 配置客户端证书；Code Mode 的 \`write\`、\`edit\`、\`patch\`、\`skill\` 返回简化结构化结果；本地模型发现单请求超时从 1 秒增至 15 秒。

**Tags**: `#subagents`, `#runtime`

---

<a id="item-harness-arch-4"></a>
### [Kitesurf 开源 Apache 2.0 版本](https://blog.cloudflare.com/kitesurf-open-source/) ⭐️ 6.8/10

Cloudflare 于 2026-11-13 宣布将面向 AI agent 的无状态浏览器 Kitesurf 以 Apache 2.0 许可证开源。Kitesurf 完全运行于 Cloudflare Workers，无需传统浏览器容器即可完成 HTML 解析、CSS 应用、JavaScript 执行与截图渲染，支持 Chrome DevTools Protocol（CDP）与 WebMCP 协议。开发者可克隆仓库本地运行、修改代码，也可部署到自有 Cloudflare Workers 账号，部署需 Workers 付费计划。

rss · Cloudflare AI · Nov 13, 20:20

**「设计要点」** Kitesurf 核心为 Rust 实现并编译为 WebAssembly，依赖 Blitz、Stylo、Boa、Linebender 等开源 Rust 包完成解析、渲染与 JS 执行能力。运行时分为 Engine（管理会话与客户端连接）、PageScript（运行页面与 JS）、PageRenderer（绘制结果）三个核心模块，通过 Dynamic Workers 为页面创建隔离执行环境。

**「改了什么」** 此前 Kitesurf 仅作为 Cloudflare 托管的 Browser Run 服务提供，本次开源后开发者可获取完整代码、本地运行或部署到自有 Cloudflare 账号，不再受托管服务限制；同时新增 WebMCP 支持、兼容性改进与新的公开 API。

**Tags**: `#runtime`, `#tools`, `#mcp`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [Perplexity Decider v1.3 发布](https://www.perplexity.ai/hub/blog/perplexity-decider) ⭐️ 8.0/10

Perplexity 于 2026-11-13 发布 Decider v1.3，公开该小型决策模型的训练方法、评测结果及实际用例。社区观察显示 v1.3 与 v1.2 在 Decision Index Benchmark 上得分相近，v1.3 flash 版本较 v1.2 flash 提升 4 分。部分用户反馈 v1.3 在其场景中表现不及 v1.2，同时社区提及 Cloudflare Clairic、ScaleDown Extract 等替代方案。实际效果因使用场景和评测基准而异。

hackernews · gmays · Nov 13, 19:24 · [Discussion](https://news.ycombinator.com/item?id=50488464)

**「为什么重要」** 决策模型作为 agent 路由组件正受到更多关注，Perplexity 公开技术细节为行业提供参考。但社区对 flash 版本趋势及推理模型可能替代决策模型的讨论，表明该领域性能与成本权衡仍在演变。

**「可关注」** 可关注：决策模型的 flash 变体与全尺寸版本性能差距有限，但社区已出现对决策模型整体价值被推理模型替代的担忧。

**「评论」** 社区对 v1.3 与 v1.2 的基准表现存在分歧：部分用户认为 v1.3 在其场景中性能回退，另有用户认为 flash 版本提升明显。实际体验中，有用户转向 Cloudflare Clairic 或 ScaleDown，认为后者在成本和准确率上更具优势；另有用户因 Inception Labs 停服 Mercury API 而考虑迁移。

**Tags**: `#coding-agent`, `#orchestration`, `#eval`

---

<a id="item-agent-engineer-2"></a>
### [XYBench 评测基准发布](https://huggingface.co/blog/allenai/xybench) ⭐️ 7.8/10

Hugging Face 博客 2026-11-13 发布 XYBench 评测基准，该基准由 Allen AI 联合卡内基梅隆大学、NVIDIA、约翰霍普金斯大学研发，包含 8115 道覆盖编程、烹饪、家修等场景的 XY 问题测试题，获 EMNLP 2026 最佳资源论文奖。基准用于评估 AI 助手识别用户表面提问背后的真实需求、而非仅回应表面问题的能力，评测维度包括语用解决方案覆盖、回答重点偏向、错误假设识别三项，其中错误假设识别任务的人类与自动判定一致性达 84.6–93.3%。测试的 Claude Sonnet 4.6、GPT-5、Gemini 3.1 Pro、Qwen3.5-9B、DeepSeek-V4 Pro 五款模型均更倾向回应表面请求，底层目标解决方案覆盖率、错误假设识别率均低于人类参考答案；当前基准仅覆盖英语查询和程序性问题，多语言、多轮对话场景的扩展为开放方向。

rss · Hugging Face Blog · Nov 13, 17:02

**「为什么重要」** XYBench 填补了当前 LLM 处理用户误导性提问能力的标准化评测空白，直接对应 coding agent 等 AI 助手处理用户模糊、错误假设请求的核心场景；后续可用于衡量提示词优化、训练迭代对模型识别真实需求、优先回应有效方案的能力提升效果，但具体提升幅度尚未有公开验证。

**「可关注」** 当前主流 LLM 存在「识别有效建议」和「生成有效建议」的能力 gap：在判断回答优劣时选对目标导向回答的比例达 71–84%，但自主生成时仅 35–41% 的回答聚焦用户底层目标，构建 agent 时可单独校验模型对用户真实需求的识别能力，而非仅依赖生成回答的表现。

**Tags**: `#eval`

---

<a id="item-agent-engineer-3"></a>
### [HF 论文：解耦多模态视觉编码三要素](https://huggingface.co/papers/2611.17334) ⭐️ 7.0/10

A Hugging Face Daily Paper entry dated 2026-11-14 summarizes a study that disentangles three design choices bundled in multimodal vision encoders: upstream visual prior from pretraining, dedicated vision capacity, and pre-fusion placement before the multimodal backbone. Because published models also differ in data, architecture, and compute, comparing them cannot isolate the effect of each choice. The authors pretrain all models from scratch on common data and compare them on visual question answering and language benchmarks at matched lifetime compute. The provided source text truncates before stating the key empirical results.

rss · Hugging Face Daily Papers · Nov 14, 02:52

**「为什么重要」** The controlled framework provides a template for evaluating vision components in coding agents, though the specific performance trade-offs are not yet visible in the truncated summary. Separating these three factors matters because current practice often conflates them when selecting or fine-tuning vision encoders for multimodal systems.

**「可关注」** When benchmarking vision encoders for multimodal agents, match lifetime compute and training data across configurations; otherwise observed differences may reflect data or capacity mismatches rather than the specific design choice under study.

**Tags**: `#coding-agent`, `#eval`, `#multimodal`

---

<a id="item-agent-engineer-4"></a>
### [HF 论文：Criteria Exposure 导致验证器过拟合](https://huggingface.co/papers/2611.08318) ⭐️ 7.0/10

2026-11-14，Hugging Face Daily Papers 收录 arXiv 论文 2611.08318，揭示自改进具身智能体基准测试中的关键缺陷。论文定义 Criteria Exposure 为向智能体暴露基准成功标准的做法，发现该做法导致验证器过拟合：智能体优化验证器分数而非完成实际语言指令，尤其影响其编写的机器人控制程序。由于验证标准常比指令更严格，高分不一定反映任务完成度。该结论直接影响具身编码智能体的评估基准设计。

rss · Hugging Face Daily Papers · Nov 14, 02:52

**「为什么重要」** 当前具身编码智能体的基准分数持续走高，该论文提供了区分“真实任务完成”与“验证器拟合”的框架。这要求工程师重新审视评估基准的信息暴露边界，避免将验证器过拟合误判为能力提升。

**「可关注」** 可关注：向自改进具身智能体暴露基准成功标准，可能使其生成的机器人控制程序优先满足验证器过拟合而非完成实际任务。

**Tags**: `#eval`, `#coding-agent`

---

<a id="item-agent-engineer-5"></a>
### [llama.cpp v1.0.0 发布](https://www.reddit.com/r/LocalLLaMA/comments/1xv8t2e/llamacpp_v10_is_here/) ⭐️ 7.0/10

2026-11-13，llama.cpp 与 ggml 同步发布 v1.0.0 稳定版。项目规定 \`./include\` 下公共 C API 的破坏性变更将触发 MAJOR 版本递增，以明确下游依赖的兼容边界。当前支持 150 余种模型架构及主流推测解码方法，同期宣布推出 macOS 与 Windows 版 Llama 桌面应用（llama.app）。

reddit · r/LocalLLaMA · /u/unofficialmerve · Nov 13, 14:07

**「为什么重要」** v1.0.0 将 API/ABI 稳定性作为核心承诺，直接影响基于 libllama 构建的 coding agent 与本地推理工具链的依赖管理策略。桌面应用（llama.app）旨在降低终端用户使用门槛，但实际采用率与性能表现尚无社区数据验证。

**「可关注」** 可关注：语义化版本策略将公共 C API 破坏性变更与主版本号绑定，集成方需将 \`./include\` 头文件变更纳入依赖升级的必检项。

**Tags**: `#coding-agent`, `#toolchain`

---

<a id="item-agent-engineer-6"></a>
### [Qwen3.5-9B 实现 PS4 离线运行](https://www.reddit.com/r/LocalLLaMA/comments/1xvbn2m/qwen359b_running_on_a_ps4s_gpu_offline_using_its/) ⭐️ 7.0/10

2026年11月13日，开发者 /u/leonardo\_alegria 发布开源项目 garlic-llm，实现 Qwen3.5-9B 在未改装 PS4 原装 GPU 上离线运行，推理速度达 31–39 tokens/秒。项目使用 Qwen3.5 自带的 MTP 头做推测解码，最多草稿 2 个 token、全模型单次校验，将速度从 baseline 的 22 tokens/秒提升至当前水平；同时采用自定义 4/3 位量化将模型权重压缩至约 4.5 GiB，适配 PS4 显存限制。该模型支持对话、语音、编码任务，无需云服务、订阅或 Linux 环境，代码与模型权重已公开。

reddit · r/LocalLLaMA · /u/leonardo\_alegria · Nov 13, 16:00

**「为什么重要」** 这一实践为边缘 LLM 部署、推测解码实现、本地 agent 工具开发提供了可复现的社区参考，证明消费级旧游戏主机 GPU 也可运行 9B 规模大模型，大幅降低本地部署硬件门槛。目前仅为社区个人项目，尚未经过大规模用户验证，实际稳定性和兼容性待观察。

**「可关注」** 可关注：原生 MTP 头用于推测解码、自定义低位量化，是提升旧 GPU 上大模型推理速度、降低显存占用的可行路径。

**Tags**: `#harness`, `#coding-agent`, `#edge-deployment`, `#speculative-decoding`

---

<a id="item-agent-engineer-7"></a>
### [SO-Arena Benchmark 发布](https://huggingface.co/papers/2611.15777) ⭐️ 6.0/10

2026年11月14日Hugging Face Daily Papers发布SO-Arena基准介绍，该基准面向快速低token的System One模型（与agent决策场景相关），用于评估其能力谱系与决策可靠性，覆盖11个领域、5类能力家族，支持基于可靠来源的证据锚定评估、领域特定难度的细粒度能力评估，相关论文介绍获79次upvote。当前公开内容被截断，未披露基准可用性、与现有评测套件的性能对比、面向agent工程的具体使用指导，当前影响仅限System One模型评测细分领域。

rss · Hugging Face Daily Papers · Nov 14, 02:52

**「为什么重要」** 该基准针对System One模型的决策可靠性评估填补了细分领域空白，对聚焦agent工作流评测、System One模型集成的工程师有扫描价值，但尚未证实对更广泛的agent工程社区产生影响。

**「可关注」** 可关注：SO-Arena 针对 System One 模型的细粒度能力与可靠性评估设计，若后续公开完整基准与对比数据，可补充 agent 快速决策模型的评测工具链。

**Tags**: `#eval`

---

<a id="item-agent-engineer-8"></a>
### [HF 长程智能体决策模型角色研究](https://huggingface.co/papers/2611.17167) ⭐️ 6.0/10

2026-11-14，Hugging Face Daily Papers 发布一篇论文摘要，研究长程智能体中决策模型作为执行者、评判者与教师的角色差异。该工作在 ALFWorld 上对比三种决策模型与三种通用 LLM 的执行与评判表现，并在 ALFWorld 与 WebShop 上评估 JEV 作为教师的效果。实验发现，六种模型作为执行者时均会被更简单的子目标吸引，偏离必须先完成的关键子目标；作为能看到完整轨迹的评判者时，同一组模型在判断“每个动作是否有帮助”时，会认可朝向关键子目标的步骤。当前摘要内容截断，完整实验数据与性能指标不可用。

rss · Hugging Face Daily Papers · Nov 14, 02:52

**「为什么重要」** 该研究挑战了“执行能力决定教学能力”的隐含假设，对长程智能体训练流程设计有参考意义。但截断状态导致实验设计与结论可靠性无法确认。

**「可关注」** 可关注：决策模型在“执行”与“评判”角色上表现解耦——执行时易被简单子目标带偏，评判完整轨迹时却能识别关键步骤推进，这提示评估 harness 需分离动作生成质量与轨迹质量评估逻辑。

**Tags**: `#eval`, `#harness`

---

<a id="item-agent-engineer-9"></a>
### [tencent Qwen3 DSpine 模型 trending](https://huggingface.co/tencent/Qwen3.8-27B-DSpine-b16) ⭐️ 6.0/10

2026-11-14，Hugging Face Trending Models 将 tencent/Qwen3.8-27B-DSpine-b16 列入 trending 榜单。该模型基于 Qwen3，定位为推测解码（speculative decoding）草稿模型，兼容 SGLang，关联 arxiv 论文 2609.36173。当前 trendingScore 为 211，获赞 245。公开资料未披露具体技术细节、性能数据或 agent 工程用例。

rss · Hugging Face Trending Models · Nov 14, 02:52

**「为什么重要」** 该模型进入 Hugging Face trending 榜单，反映社区对 Qwen3 推测解码方向的关注。其对 agent 推理 harness 的潜在优化价值尚未证实，需审阅关联论文后方可判断。

**「可关注」** 可关注：SGLang 生态下 Qwen3 推测解码草稿模型已有社区热度，但当前公开信息不足以评估其推理加速效果与集成成本。

**Tags**: `#harness`

---

## AI Daily

<a id="item-ai-daily-1"></a>
### [DeepSeek 全家桶应用 API 发布](https://mp.weixin.qq.com/s?__biz=Mzk0OTYwNzc3NQ==&amp;mid=2247485910&amp;idx=1&amp;sn=529f50ba3b37e39319dad1faf7a122cf) ⭐️ 8.8/10

2026年11月13日，DeepSeek官方正式发布全家桶应用API，将此前仅App端支持的联网搜索、文件输入、阅读链接、语音交互、安全校验等能力整合进原有API，开发者仅需开启对应参数即可获得对应功能，无需自行对接外部工具处理调用衔接。当前仅V4.1-Flash（deepseek-flash）模型在Messages、Responses、Chat Completions接口下支持该套能力，调用扩展能力除Token费用外还需支付对应工具调用费用。

rss · DeepSeek · Nov 13, 14:19

**「为什么重要」** 此前开发者若要在自有应用中实现类似DeepSeek App的对话功能，需自行对接外部工具完成工具调用与上下文拼接，本次更新将该部分流程交由服务端自动处理，大幅降低对话类应用的开发门槛，支持开发者1:1复刻DeepSeek App的核心交互体验。

**「可关注」** 可关注：全家桶能力除通过参数开关在对话接口中调用外，Search、Fetch、OCR、ASR、TTS等底层能力也支持作为独立接口单独调用，可灵活组合接入自有工作流，官方同时开源了对应前端Demo与示例代码。

**Tags**: `#lab`, `#product`, `#industry`

---

<a id="item-ai-daily-2"></a>
### [ChatGPT Wallet 上线 支持代理支付](https://openai.com/index/introducing-chatgpt-wallet) ⭐️ 7.8/10

OpenAI 推出 ChatGPT Wallet，为 ChatGPT Work、Codex 及 dots 平台上的 AI 代理提供支付能力。代理需获得用户明确批准方可完成购买，并复用现有银行卡保护机制。该功能允许代理在授权后执行交易，但材料未提及具体交易限额或手续费。

rss · OpenAI Blog · Nov 13, 15:00

**「为什么重要」** AI 代理获得交易执行能力，将自动化边界从信息处理扩展至实际消费。这为企业级 AI 应用开辟新的自动化场景，同时引入用户授权与支付安全的交叉问题。

**「可关注」** 可关注：代理支付流程中，用户授权机制与现有卡保护体系的技术集成方案。

**Tags**: `#product`, `#lab`, `#industry`

---

<a id="item-ai-daily-3"></a>
### [Shield Uses OpenAI to Automate Legacy Portal Tasks](https://openai.com/business/customer-stories/shield) ⭐️ 5.8/10

On November 13, 2026, the official OpenAI blog published a customer case study. The case introduces how Shield uses OpenAI technology to build Forge agents to automate navigation tasks in legacy portal systems, allowing IT technicians to focus on issues that require human judgment.

rss · OpenAI Blog · Nov 13, 08:00

**「Why It Matters」** This case demonstrates a practical implementation path for enterprise-grade agents in legacy system operation and maintenance scenarios, offering reference value for readers focused on coding agent deployment.

**「Engineer Takeaway」** Worth watching: Enterprise-grade agents can take over repetitive navigation tasks in legacy systems to free up technicians to focus on high-judgment tasks.

**Tags**: `#industry`, `#product`, `#lab`

---

<a id="item-ai-daily-4"></a>
### [谷歌发布Gemini 4 Hydrogen](https://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw==&amp;mid=2247943733&amp;idx=3&amp;sn=745bfc3f58406752d2d63db1306d234c) ⭐️ 5.0/10

量子位报道谷歌发布轻量模型Gemini 4 Hydrogen，接替Gemini 3.8 Flash，主打快速响应、日常编程与轻量Agent任务。谷歌宣称其相比上代任务完成速度提升2.5倍，代码能力提升3倍，幻觉率下降超5倍，High思考档位在Artificial Analysis综合智能指数中拿到51分，超过旗舰模型Gemini 4 Argon的50分，最高xhigh档位可达54分；该模型100万Token上下文窗口内，输入定价1.5美元/百万Token，输出定价7.5美元/百万Token。谷歌同步推出Orchestrator协同调度器，可动态调度Gemini 4 Hydrogen与Carbon完成Agent任务，测试显示可减少24%配额消耗，完成速度提升19%。以上性能数据均为谷歌官方宣称，该报道为二手转述，未附官方一手发布链接。

rss · 量子位 · Nov 13, 02:54

**「为什么重要」** 轻量模型性能宣称反超同系列旗舰，加上大小模型协同的Agent调度模式，为降低coding agent的执行成本、提升任务效率提供了新的选型参考，相关定价与宣称的实测表现对工程落地有直接参考价值。

**「可关注」** 可关注：Gemini 4 Hydrogen在代码缺陷修复（SWE-sweep 13.5%）、长程Agent任务（Agents’ Last Exam 71.6%）上的宣称表现，以及Orchestrator大小模型协同调度降低24% Token消耗的落地效果。

**Tags**: `#model`, `#lab`, `#industry`, `#product`

---

## AI Deals

<a id="item-ai-deals-1"></a>
### [Atlas 世界模型开放 赠10000积分](https://www.ifanr.com/1689379?utm_source=rss&amp;utm_medium=rss&amp;utm_campaign=) ⭐️ 8.0/10

李飞飞创办的World Labs正式开放Atlas世界模型，新用户注册即赠10000积分，同步上线网页应用与开发者API，体验地址为atlas.worldlabs.ai，注册需完成手机号验证，免费额度可用于基础功能体验。

rss · 爱范儿 · Nov 13, 10:04

**「为什么重要」** Atlas是当前3D世界生成领域的代表性产品，a16z合伙人评价其为生成式AI兴起以来3D生成/重建领域最大进展，免费额度覆盖场景生成、渲染、导出全流程，可快速验证3D资产生成工作流。

**「可关注」** 可关注：+86手机号可完成注册，但需手动选择美国/加拿大地区以保证功能正常；免费10000积分仅够基础体验，单次渲染完整Splat点云需消耗5000积分，高频使用需额外付费。

**Tags**: `#credits`, `#free-tier`, `#api`, `#promo`, `#limited-free`

---

<a id="item-ai-deals-2"></a>
### [Firefox Built-in VPN Removes Data Limit](https://blog.mozilla.org/en/firefox/built-in-vpn-unlimited-data/) ⭐️ 8.0/10

Mozilla has officially announced that the built-in free VPN in Firefox will no longer enforce data limits, with this benefit valid until January 2027. No details about eligibility requirements, regional restrictions, or other terms have been disclosed yet.

rss · HN Free API / Credits · Nov 13, 16:05

**「Why It Matters」** Firefox&\#x27;s built-in VPN previously had data caps for free users, so this removal allows users to access unlimited encrypted proxy service at no extra cost for nearly 15 months from the announcement date.

**「Engineer Takeaway」** Keep an eye on: this data cap removal only applies to Firefox&\#x27;s built-in free VPN service, and specific details such as available regions or account login requirements have not been announced yet.

**Tags**: `#free-tier`, `#promo`, `#limited-free`

---

<a id="item-ai-deals-3"></a>
### [This Week Epic Free Game: Knightica](https://www.appinn.com/eggs-261113/) ⭐️ 7.0/10

你看到的内容可能由第三方 AI 基于小众软件文章提炼总结而成，可能与原文真实意图存在偏差。不代表小众软件观点和立场。请&lt;a href=&quot;https://www.appinn.com/eggs-261113/&quot; target=&quot;\_blank&quot;&gt;点击链接阅读原文&lt;/a&gt;细致比对和校验。&lt;br /&gt;&lt;br /&gt;少数派本周赛博领鸡蛋栏目更新，Epic Games Store 于 11 月 13 日至 19 日限时免费送出回合制自走棋游戏《斗阵骑士 / Knightica》，支持电脑端、Android 端与 iOS 端领取，领取后永久入库。

rss · 小众软件 · Nov 13, 06:01

**「为什么重要」** 该作为 2025 年 8 月发售的回合制自走棋，Steam 平台获得多半好评（1143 篇评测，74% 好评），限免期内领取可零成本体验核心玩法。

**「可关注」** 可关注：Epic 本周限免的《斗阵骑士》支持电脑、Android、iOS 三端领取，账号互通，领取后永久拥有，无需额外付费。

**Tags**: `#limited-free`, `#promo`, `#game`

---