---
layout: default
title: "Horizon Summary: 2026-10-24 (EN)"
date: 2026-10-24
lang: en
---

> From 189 items, 15 important content pieces were selected

---

**Agent Harness Architecture**
1. [Goose v1.56.0 发布](#item-harness-arch-1) ⭐️ 7.8/10
2. [adk-python v2.13.0 发布](#item-harness-arch-2) ⭐️ 7.8/10
3. [MCP TypeScript SDK v2.4.0 发布](#item-harness-arch-3) ⭐️ 7.8/10
4. [Cloudflare 安全审计 skill 开源](#item-harness-arch-4) ⭐️ 5.0/10

**AI Agent Engineer**
1. [Kimi K3.1 Pro 上线 API](#item-agent-engineer-1) ⭐️ 7.0/10
2. [IQuest-Q1 发布 320B CLI Agent MoE 模型](#item-agent-engineer-2) ⭐️ 7.0/10
3. [Deep Fusion Memory 提出 LLM 参数化记忆架构](#item-agent-engineer-3) ⭐️ 7.0/10
4. [Nemotron-3.5-Bolt 4GB 发布](#item-agent-engineer-4) ⭐️ 6.5/10
5. [OpenDS 基准提出 评估 Web 智能体深度搜索](#item-agent-engineer-5) ⭐️ 6.0/10
6. [LitPivot 发布：文献动态情境化研究构思](#item-agent-engineer-6) ⭐️ 5.8/10

**AI Daily**
1. [OpenAI Habitat 扩容至 10 亿 ChatGPT 用户](#item-ai-daily-1) ⭐️ 7.8/10
2. [OpenAI 加强 frontier model 训练环境管控](#item-ai-daily-2) ⭐️ 7.8/10

**AI Deals**
1. [智谱 ZCode 1024 送 5 亿 Tokens](#item-ai-deals-1) ⭐️ 8.0/10
2. [Epic 本周免费游戏 10.23~10.29](#item-ai-deals-2) ⭐️ 8.0/10
3. [Show HN 免费无限制AI文本检测器发布](#item-ai-deals-3) ⭐️ 6.0/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [Goose v1.56.0 发布](https://github.com/aaif-goose/goose/releases/tag/v1.56.0) ⭐️ 7.8/10

Goose v1.56.0 发布。本次更新强化子代理生命周期管理与运行时推理，新增失败或取消委托子代理的恢复机制、GOOSE\_MAX\_CONCURRENT\_SUBAGENTS 并发上限、自动 thinking level 操作。代码执行后端由 PCTX 切换为 Boa JavaScript 运行时，Provider 层新增 IO Intelligence 与缓存价格支持。桌面端引入 Windows NSIS 安装器与只读子代理会话视图。

github · github-actions\[bot\] · Oct 23, 15:49

**「设计要点」** 子代理调度层引入恢复队列与 GOOSE\_MAX\_CONCURRENT\_SUBAGENTS 并发门控，失败任务可重入执行。权限与 UI 层分别新增危险历史包含选项与只读子代理会话链接，分离操作风险与观察权限。

**「改了什么」** 子代理从一次性委托执行改为支持失败恢复与并发控制。运行时推理增加自动 thinking level 调节，代码执行后端由 PCTX 迁移至 Boa JavaScript，Provider 层新增 IO Intelligence 与缓存价格感知。

**Tags**: `#subagents`, `#runtime`, `#permissions`, `#tools`, `#prefix-cache`

---

<a id="item-harness-arch-2"></a>
### [adk-python v2.13.0 发布](https://github.com/google/adk-python/releases/tag/v2.13.0) ⭐️ 7.8/10

google/adk-python v2.13.0 于 2026-10-22 发布。新增 TypeSafe Jev 模型工作流分类器（TypesafeClassifier、ClassifierNode），以单次前向传播返回校准概率，绕过 LLM 路由；12 项实验特性转稳定；接入实时音频（CascadeLive、barge-in、Gemini STT/TTS）与 MongoDB 集成（MongoDbSessionService、MongoDbMemoryService、MongoDbToolset）。string-model agents 的 turn 执行提速最高 8 倍，事件加载开销降低。遥测默认切换至 OpenTelemetry GenAI v2（otel\_semconv\_1\_44），移除 call\_llm span，可通过 ADK\_TELEMETRY\_SCHEMA\_VERSION\_OPT\_IN=otel\_semconv\_1\_36 回退至 v1。

github · Jacksunwei · Oct 23, 18:08

**「设计要点」** 分类器层引入 BaseClassifier 与 ClassifierNode，支持 LLM 与非 LLM（Jev）路由解耦；MongoDbMemoryService 以关键词匹配实现长期记忆，无需向量索引；MongoDbSessionService 支持 runner 副本间会话共享；MongoDbToolset 支持序列化以便部署至 Agent Engine。遥测层切换至 OpenTelemetry GenAI v2，eval 模块将调用耗时拆分为 model、tool、framework 三部分。

**「改了什么」** 相对 v2.12.0，v2.13.0 新增非 LLM 的 TypeSafe Jev 分类器与 ClassifierNode 工作流路由节点；12 项实验特性转稳定；新增 CascadeLive 实时音频（含 barge-in 与 Gemini STT/TTS）；新增 MongoDB 会话服务、记忆服务（关键词检索，无需 embedding）与工具集（支持 Atlas Automated Embedding）；string-model agents 执行 turn 提速最高 8 倍；遥测默认启用 OpenTelemetry GenAI v2 并移除 call\_llm span。

**Tags**: `#planning`, `#runtime`

---

<a id="item-harness-arch-3"></a>
### [MCP TypeScript SDK v2.4.0 发布](https://github.com/modelcontextprotocol/typescript-sdk/releases/tag/v2.4.0) ⭐️ 7.8/10

modelcontextprotocol/typescript-sdk v2.4.0 正式发布，\`@modelcontextprotocol/client\`、\`server\`、\`core\`、\`server-legacy\`、\`codemod\` 同步升至 2.4.0，\`@modelcontextprotocol/node\` 升至 2.1.2。本次更新按 2026-07-28 规范收紧工具参数校验与输出 schema 处理，包含破坏性变更。新增 Skills over MCP（SEP-2640）和 OAuth 刷新可选 \`scope\` 参数。

github · felixweinberger · Oct 23, 18:32

**「设计要点」** 工具输出 schema 通过 \`z.object\(...\).meta\(\{ id \}\)\` 声明，客户端需读取 \`structuredContent\` 而非旧版 \`structuredContent.result\`。内嵌 Ajv 验证器升级至 fast-uri 3.1.8，拒绝 \`$id\` 或 \`$ref\` 中使用非法 URI scheme（如 \`my\_tool:output\`）。

**「改了什么」** \`number\` 类型参数上的 \`x-mcp-header\` 注解被 2026-07-28 规范拒绝，客户端不再列出此类工具且服务端返回 \`-32020\`；\`outputSchema\` 结果取消 \`\{ result \}\` 包装，调用方需直接读取 \`structuredContent\`；内嵌 Ajv 验证器升级至 fast-uri 3.1.8，拒绝 \`$id\` 或 \`$ref\` 中使用非法 URI scheme。新增 \`loadSkills\(folder\)\` 与 \`SkillsClient\` 支持技能文件夹发布、列表与验证，\`server.attach\` 为实验性接口。

**Tags**: `#mcp`, `#tools`, `#breaking-changes`, `#spec-compliance`

---

<a id="item-harness-arch-4"></a>
### [Cloudflare 安全审计 skill 开源](https://github.com/cloudflare/security-audit-skill) ⭐️ 5.0/10

Cloudflare 开源 security-audit-skill，一个将 coding agent 转变为安全审计器的技能。该技能编排隔离子代理，执行多阶段审计流程，涵盖侦察、覆盖引导狩猎、候选验证、结构化输出、独立记录验证和目标中性报告。输出为独立验证的机器可读发现。该技能曾作为 Cloudflare 漏洞发现 harness 的基础。

rss · GitHub Trending Daily · Oct 24, 01:57

**Tags**: `#tools`, `#subagents`, `#sandbox`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [Kimi K3.1 Pro 上线 API](https://www.kimi.ai/blog/kimi-k3-1-pro) ⭐️ 7.0/10

2026年10月23日，Moonshot 推出的 coding 专属模型 Kimi K3.1 Pro 正式上线 Kimi API，当前未开源完整权重，Moonshot 承诺 2026年11月4日前发布全量权重。同步推出的 Highspeed 版本推理速度是普通版的 2-3 倍，价格为普通版的 2 倍，仅输入 token 缓存命中场景定价不变。该模型输入定价为 $2/百万 token、输出定价为 $10/百万 token，与 GPT-6.1 Sol 持平，仅为 Claude Opus 5.5 的一半。Moonshot 自研基准显示其性能与 Claude Opus 5.5、GPT-6 Astra 相当，Artificial Analysis 评分 55，高于 Claude Fable 5.1、GPT-6 Astra、Gemini 4 Argon 的 53 分，低于 Claude Opus 5.5 的 58 分，是首个达到该评分的即将开源权重模型。

hackernews · Jowsey · Oct 23, 16:59 · [Discussion](https://news.ycombinator.com/item?id=50212065)

**「为什么重要」** 这是目前首个接近闭源 frontier 模型性能的即将开源权重 coding 模型，为需要低成本自部署 coding agent 的团队提供了新的候选选项。但当前完整权重尚未发布，实际开源后的性能、安全策略表现还需验证。

**「可关注」** 可关注：Kimi K3.1 Pro 输出定价仅为 Claude Opus 5.5 的一半，Highspeed 版本输入 token 缓存命中价格不变，若 coding 场景缓存命中率高可有效降低推理成本。

**「评论」** 社区实测显示模型回复风格偏直接，存在身份认知不一致的问题；有用户反馈 $99/月订阅套餐在 47 分钟内即触发 5 小时配额限制，另有用户关注其承诺开源权重网络能力低于闭源 frontier 模型的策略。

**Tags**: `#coding-agent`, `#permissions`, `#harness`, `#eval`

---

<a id="item-agent-engineer-2"></a>
### [IQuest-Q1 发布 320B CLI Agent MoE 模型](https://huggingface.co/papers/2610.30949) ⭐️ 7.0/10

Hugging Face Daily Papers published IQuest-Q1 on October 24, 2026: a sparse Mixture-of-Experts \(MoE\) agentic foundation model tailored for CLI systems, with 320B total parameters and 15B activated parameters. Its training follows a three-stage pipeline: \(1\) pre-training combines Stable SplitNorm, Muon, and muP, uses a two-stage curriculum where the second stage raises the coding data share, and maintains a wide stability margin between safe and optimal learning rates; \(2\) mid-training expands the data mixture across domains and formats, and progressively extends context length; \(3\) post-training adopts a multi-scaffold, multi-version setup that combines SFT, domain-specialized RL, and MOPD to integrate complementary training signals and strengthen agentic coding capabilities. The public content mentions model merging via diff but is truncated at the end. The work targets engineers working on coding agent development and agent training workflows.

rss · Hugging Face Daily Papers · Oct 24, 01:57

**「为什么重要」** The work discloses a full training pipeline for sparse MoE models targeting CLI agent scenarios, with actionable technical choices and signal integration designs that offer direct reference for coding agent training engineering. However, the currently public content is truncated, and complete technical details and performance data remain to be supplemented.

**「可关注」** Engineers can focus on its progressive coding data share strategy in the three-stage training, the engineering design of integrating complementary signals via multi-scaffold post-training, and the activated parameter efficiency of sparse MoE in CLI agent scenarios.

**Tags**: `#coding-agent`

---

<a id="item-agent-engineer-3"></a>
### [Deep Fusion Memory 提出 LLM 参数化记忆架构](https://huggingface.co/papers/2610.25100) ⭐️ 7.0/10

Hugging Face Daily Papers 于 2026-10-24 收录论文《Deep Fusion Memory: A Chunk-Level Parametric Memory for Large Language Models》。该论文提出 Deep Fusion Memory（DFM）架构，通过上下文感知因果预测器生成记忆，以检索到的 chunk embedding 为监督，将预测记忆整合到中间隐状态而非仅输出层插值，从而降低训练数据构建工作量并实现更深层记忆融合。当前材料为论文摘要片段，未提供性能验证数据或实现细节。

rss · Hugging Face Daily Papers · Oct 24, 01:57

**「为什么重要」** 该工作直接针对 agent 记忆系统设计中的关键瓶颈——外部参数化记忆的训练数据开销与融合深度。若后续验证有效，可能为 coding agent 的长期记忆机制提供新思路，但目前缺乏实验数据支撑。

**「可关注」** DFM 将记忆预测监督从输出层移至隐状态层，可能影响 agent 记忆模块接入方式，但需等待完整论文的基准测试与实现细节。

**Tags**: `#memory`

---

<a id="item-agent-engineer-4"></a>
### [Nemotron-3.5-Bolt 4GB 发布](https://www.reddit.com/r/LocalLLaMA/comments/1xdiecx/nvidianvidianemotron35bolte4b4gb_hugging_face/) ⭐️ 6.5/10

2026年10月23日，Reddit社区用户/u/jacek2023转发分享NVIDIA推出的小语言模型Nemotron-3.5-Bolt-E4B-4GB，该模型基于Gemma-4-E4B-it进一步后训练，优化多轮工具调用、指令遵循与输入接地能力，面向低内存、低TTFT的边缘/设备agent部署场景。配套提供用于推测解码的DFlash drafter模型，另有BF16全精度版本，模型支持商用与非商用用途，官方已发布技术报告及Hugging Face仓库链接。当前内容为社区二次传播，非NVIDIA官方首发公告。

reddit · r/LocalLLaMA · /u/jacek2023 · Oct 23, 16:13

**「为什么重要」** 该模型针对低延迟多轮工具调用、端侧agent部署场景优化，可为低TTFT设备端agent、轻量化coding agent系统提供新的候选模型参考；但当前信息为社区二手转发，尚未有官方一手发布信息佐证，实际性能与落地情况需进一步验证。

**「可关注」** 可关注：该模型针对低TTFT、多轮工具调用场景优化，配套DFlash drafter支持推测解码，适合端侧agent轻量化部署的初步验证。

**Tags**: `#coding-agent`

---

<a id="item-agent-engineer-5"></a>
### [OpenDS 基准提出 评估 Web 智能体深度搜索](https://huggingface.co/papers/2610.30181) ⭐️ 6.0/10

2026-10-24，Hugging Face Daily Papers 收录论文 arXiv:2610.30181，提出 OpenDS 基准。该基准面向真实动态开放网络环境，评估智能体执行多步深度搜索的能力，旨在弥补当前静态检索式评估的不足。现有材料未披露基准规模、任务设计、评估指标及基线性能，实际使用价值需参考完整论文确认。该工作主要影响 web-agent 与 agent-benchmark 方向的研究者与工程师。

rss · Hugging Face Daily Papers · Oct 24, 01:57

**「为什么重要」** OpenDS 首次将智能体评估场景从静态检索扩展至实时开放 Web，填补了现有基准空白。但具体任务规模、指标设计与基线性能尚未披露，其实际落地价值仍需完整论文验证。

**「可关注」** OpenDS 将 web-agent 评估从静态检索推向真实动态环境，但规模、指标与基线尚未公开，暂不宜直接纳入自动化评测流水线。

**Tags**: `#eval`, `#web-agent`, `#agent-benchmark`

---

<a id="item-agent-engineer-6"></a>
### [LitPivot 发布：文献动态情境化研究构思](https://allenai.org/blog/litpivot) ⭐️ 5.8/10

Allen AI 于 2026-10-23 发布 LitPivot，一个帮助研究人员通过文献支持的批评与修订来动态完善早期研究构想的系统。该系统随提案演变提供文献情境化，但公开资料仅提供高层描述，未披露技术架构、性能数据或 agent 工程细节（如 harness 设计、eval 方法或工具链集成）。标签显示其涉及 orchestration、toolchain 与 retrieval，但具体实现未知。

rss · Allen AI · Oct 23, 08:00

**「可关注」** 可关注：当前公开信息仅含高层概念，缺乏技术架构、性能基准及与 agent harness、eval 流程的集成细节，尚无法判断其工具链或检索机制对现有 coding agent 工作流的可复用性。

**Tags**: `#orchestration`, `#toolchain`, `#retrieval`

---

## AI Daily

<a id="item-ai-daily-1"></a>
### [OpenAI Habitat 扩容至 10 亿 ChatGPT 用户](https://openai.com/index/scaling-storage-one-billion-users-part-two) ⭐️ 7.8/10

OpenAI 官方博客公开了其 Habitat 存储系统的扩容技术细节，该系统用于服务超过 10 亿 ChatGPT 用户，通过可靠多租户、全局缓存与 Azure Cosmos DB 实现读性能提升 12 倍。

rss · OpenAI Blog · Oct 23, 17:00

**「为什么重要」** 该内容为官方公开的大规模存储系统扩容实践，为高并发产品的基础设施设计提供了可参考的技术路径。

**「可关注」** 可关注：Habitat 通过可靠多租户、全局缓存搭配 Azure Cosmos DB 实现读性能 12 倍提升的具体落地细节。

**Tags**: `#lab`, `#industry`, `#product`

---

<a id="item-ai-daily-2"></a>
### [OpenAI 加强 frontier model 训练环境管控](https://openai.com/index/securing-our-frontier-model-training-environment) ⭐️ 7.8/10

OpenAI 官方博客发文介绍 frontier model 训练与评估环境的 containment 强化措施。措施包括离线环境与高算力红队测试。

rss · OpenAI Blog · Oct 23, 10:00

**「可关注」** 可关注：离线环境与高算力红队测试在 frontier model 训练 containment 中的具体实施方案。

**Tags**: `#lab`, `#policy`, `#eval`, `#industry`

---

## AI Deals

<a id="item-ai-deals-1"></a>
### [智谱 ZCode 1024 送 5 亿 Tokens](https://www.appinn.com/zcode-1024-free-500-million-tokens/) ⭐️ 8.0/10

你看到的内容可能由第三方 AI 基于小众软件文章提炼总结而成，可能与原文真实意图存在偏差。不代表小众软件观点和立场。请点击链接阅读原文细致比对和校验。智谱 ZCode 推出 1024 程序员节活动，新老用户均可免费领取共 5 亿 Tokens 额度，该额度仅支持 GLM-5.3 与 GLM-5.3-Flash 模型，2026 年 10 月 23 日 23:00 生效、10 月 26 日 09:00 到期，需下载 ZCode 客户端登录后点击活动入口领取，领取成功后生效前客户端会显示「待生效」。

rss · 小众软件 · Oct 23, 15:17

**「为什么重要」** 当前可正常领取，额度仅本周末有效，适合临时跑小工具、调试旧项目使用，过期自动作废无法延续。

**「可关注」** 可关注：新用户无门槛可参与领取，注意区分活动 5 亿 Tokens 额度与 ZCode Start Plan 的每日免费额度，两者相互独立，不可叠加。

**Tags**: `#credits`, `#free-tier`, `#promo`, `#limited-free`, `#api`

---

<a id="item-ai-deals-2"></a>
### [Epic 本周免费游戏 10.23~10.29](https://www.appinn.com/eggs-261023/) ⭐️ 8.0/10

你看到的内容可能由第三方 AI 基于小众软件文章提炼总结而成，可能与原文真实意图存在偏差。不代表小众软件观点和立场。请&lt;a href=&quot;https://www.appinn.com/eggs-261023/&quot; target=&quot;\_blank&quot;&gt;点击链接阅读原文&lt;/a&gt;细致比对和校验。&lt;br /&gt;&lt;br /&gt;Epic Games 于10月23日至29日开展每周免费游戏活动，PC端可领取《斯盖尔仪式 / Sker Ritual》《归家 / Home – A Unique Horror Adventure》2款游戏，移动端可领取《归家》1款游戏，领取截止时间为10月29日。

rss · 小众软件 · Oct 23, 07:34

**「为什么重要」** 本周限免为固定周期福利，两款可领取游戏均为支持中文的付费作品，当前免费领取可节省购买成本。

**「可关注」** 可关注：《归家》的PC、Android、iOS三个平台版本需分别领取，均支持浏览器端完成领取操作。

**Tags**: `#promo`, `#limited-free`, `#free-games`

---

<a id="item-ai-deals-3"></a>
### [Show HN 免费无限制AI文本检测器发布](https://kouh.me/ai-text-detector) ⭐️ 6.0/10

Show HN 用户 mrkn1 分享了一款宣称免费、无限制、私有的 AI 文本检测工具，链接为 https://kouh.me/ai-text-detector，截至发帖时该帖仅获 1 个赞、0 条评论，工具的实际使用限制、服务条款及可信度均未得到公开验证。

rss · HN Free API / Credits · Oct 23, 21:06

**「为什么重要」** 当前公开可验证的 AI 文本检测工具中，宣称完全免费、无限制且保障隐私的产品较少，该工具若属实可填补相关需求空白，但当前缺乏足够的验证信息。

**「可关注」** 可关注：该工具目前无公开的使用限制、服务条款及运营方背景信息，实际可用性与隐私承诺需进一步验证后再使用。

**Tags**: `#free-tier`

---