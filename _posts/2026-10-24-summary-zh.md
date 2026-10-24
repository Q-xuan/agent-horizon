---
layout: default
title: "Horizon Summary: 2026-10-24 (ZH)"
date: 2026-10-24
lang: zh
---

> 从 189 条内容中筛选出 15 条重要资讯。

<nav id="ah-toc" class="ah-toc" aria-label="目录"><span class="ah-toc-title">目录</span><ul><li><a href="#sec-harness-arch"><span class="ah-toc-name">Harness 架构</span><span class="ah-toc-count">4条</span></a></li><li><a href="#sec-agent-engineer"><span class="ah-toc-name">Agent 工程师日报</span><span class="ah-toc-count">6条</span></a></li><li><a href="#sec-ai-daily"><span class="ah-toc-name">AI 日报</span><span class="ah-toc-count">2条</span></a></li><li><a href="#sec-ai-deals"><span class="ah-toc-name">AI 羊毛</span><span class="ah-toc-count">3条</span></a></li></ul></nav>

---

**[Harness 架构](#sec-harness-arch)**
1. [Goose v1.56.0 发布](#item-harness-arch-1) ⭐️ 7.8/10
2. [google/adk-python v2.13.0 发布](#item-harness-arch-2) ⭐️ 7.8/10
3. [MCP TypeScript SDK v2.4.0 发布](#item-harness-arch-3) ⭐️ 7.8/10
4. [Cloudflare 开源 security-audit-skill](#item-harness-arch-4) ⭐️ 5.0/10

**[Agent 工程师日报](#sec-agent-engineer)**
1. [Kimi K3.1 Pro 发布](#item-agent-engineer-1) ⭐️ 7.0/10
2. [IQuest-Q1 CLI 智能体模型发布](#item-agent-engineer-2) ⭐️ 7.0/10
3. [DFM 分块参数记忆架构论文发布](#item-agent-engineer-3) ⭐️ 7.0/10
4. [NVIDIA Nemotron-3.5-Bolt-E4B-4GB 发布](#item-agent-engineer-4) ⭐️ 6.5/10
5. [OpenDS 基准评估开放网络深度搜索](#item-agent-engineer-5) ⭐️ 6.0/10
6. [LitPivot 发布：文献语境研究辅助工具](#item-agent-engineer-6) ⭐️ 5.8/10

**[AI 日报](#sec-ai-daily)**
1. [OpenAI Habitat 扩容服务 10 亿 ChatGPT 用户](#item-ai-daily-1) ⭐️ 7.8/10
2. [OpenAI 升级 frontier 安全](#item-ai-daily-2) ⭐️ 7.8/10

**[AI 羊毛](#sec-ai-deals)**
1. [智谱 ZCode 1024 程序员节发额度](#item-ai-deals-1) ⭐️ 8.0/10
2. [Epic 本周免费游戏 10.23~10.29](#item-ai-deals-2) ⭐️ 8.0/10
3. [Show HN 免费无限制 AI 文本检测器发布](#item-ai-deals-3) ⭐️ 6.0/10

---

## Harness 架构
{: #sec-harness-arch .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-harness-arch" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-harness-arch-1"></a>
### [Goose v1.56.0 发布](https://github.com/aaif-goose/goose/releases/tag/v1.56.0) ⭐️ 7.8/10

Goose v1.56.0 正式发布，补齐 subagent 生命周期管控：支持恢复失败或取消的委托任务、通过 \`GOOSE\_MAX\_CONCURRENT\_SUBAGENTS\` 限制并发数，并在 UI 提供只读子代理会话。运行时引入自动 thinking level 以改善模型推理，同时用 Boa JavaScript runtime 替换原有 PCTX code mode。新增 IO Intelligence provider 与 provider-defined cache pricing 支持，CLI 通过 OSC 7501 上报 session 状态。该版本还加入危险的 include history 选项与 Windows NSIS 桌面安装器。

github · github-actions\[bot\] · 10月23日 15:49

**「设计要点」** Subagent 管控链覆盖创建、恢复、并发限制与只读审计，形成完整生命周期管理。MCP 工具层统一 provider-safe public names，GDK 下沉 skills discovery 与 foreground subagent 运行，权限与工具边界收紧。

**「改了什么」** 相对上一版，subagent 支持失败/取消任务恢复与并发上限控制，代码执行模式从 PCTX 切换至 Boa JavaScript。provider 层新增缓存定价与 IO Intelligence 接入，CLI 增加 OSC 7501 状态上报。

**标签**: `#subagents`, `#runtime`, `#permissions`, `#tools`, `#prefix-cache`

---

<a id="item-harness-arch-2"></a>
### [google/adk-python v2.13.0 发布](https://github.com/google/adk-python/releases/tag/v2.13.0) ⭐️ 7.8/10

google/adk-python v2.13.0 正式发布。本次升级将 12 项实验特性转稳定，新增基于 TypeSafe Jev 模型的非 LLM 工作流分类器 \`TypesafeClassifier\` 与 \`ClassifierNode\`，单次前向传播返回校准概率，路由速度快于 LLM。同时引入实时音频交互（支持 barge-in，集成 Gemini 语音转文字与文字转语音）、MongoDB 会话与记忆服务（\`MongoDbSessionService\`、\`MongoDbMemoryService\`），以及执行性能优化（字符串模型 agent 执行轮次提速最高 8 倍）。破坏性变更：遥测默认切换至 OpenTelemetry GenAI v2 \(\`otel\_semconv\_1\_44\`\) 并移除 \`call\_llm\` span，需设置 \`ADK\_TELEMETRY\_SCHEMA\_VERSION\_OPT\_IN=otel\_semconv\_1\_36\` 回退至 v1 schema。

github · Jacksunwei · 10月23日 18:08

**「设计要点」** 运行时优化事件加载开销，字符串模型 agent 执行轮次提速最高 8 倍；工具层 \`MongoDbToolset\` 支持序列化并直接部署至 Agent Engine，连接字符串无需打包进镜像。记忆层 \`MongoDbMemoryService\` 基于关键词匹配召回，无需向量索引或 embedding 模型；评测层将 invocation duration 拆分为 model、tool 和 framework 时间。

**「改了什么」** 新增非 LLM 工作流分类器 \`TypesafeClassifier\` 与 \`ClassifierNode\`，支持基于 Jev 模型的单次前向传播路由。12 项实验特性转稳定，新增实时音频交互、MongoDB 会话/记忆/工具集集成、\`delete\_memory\` API 与 OpenSandbox 环境，执行性能提升最高 8 倍；遥测默认升级至 OpenTelemetry GenAI v2 并移除 \`call\_llm\` span。

**标签**: `#planning`, `#runtime`

---

<a id="item-harness-arch-3"></a>
### [MCP TypeScript SDK v2.4.0 发布](https://github.com/modelcontextprotocol/typescript-sdk/releases/tag/v2.4.0) ⭐️ 7.8/10

MCP TypeScript SDK v2.4.0 发布，包含与 2026-07-28 及 2025-11-25 规范对齐的破坏性变更。工具参数验证现在拒绝 \`number\` 类型上的 \`x-mcp-header\` 注解，客户端不再列出此类工具，服务器返回 \`-32020\`；\`outputSchema\` 结果不再包装在 \`\{ result \}\` 中，需直接读取 \`structuredContent\`。新增 Skills over MCP \(SEP-2640\) 支持，服务器可通过 \`loadSkills\(folder\)\` 和 \`skills.attach\(server\)\` 发布技能文件夹，客户端使用 \`SkillsClient\` 列出、读取和验证。OAuth 刷新令牌支持 opt-in \`scope\` 参数，\`ServerEvent\` 新增可选 \`params\` 字段以支持网关转发变更通知的 \`\_meta\`。

github · felixweinberger · 10月23日 18:32

**「改了什么」** 破坏性变更包括：\`number\` 参数上的 \`x-mcp-header\` 被客户端过滤、服务器返回 \`-32020\`；2025-11-25 连接的 \`outputSchema\` 结果去掉了 \`\{ result \}\` 包装；Ajv 验证器升级至 fast-uri 3.1.8，拒绝无效 URI 方案的 \`$id\`/\`$ref\`。新增 Skills over MCP、OAuth refresh scope 配置、ServerEvent params 支持，以及 v1 到 v2 升级指南作为可安装 skill。修复了资源更新列表显示、每请求传输绑定、HTTP 405 响应头及 \`@hono/node-server\` 兼容性问题。

**标签**: `#mcp`, `#tools`, `#breaking-changes`, `#spec-compliance`

---

<a id="item-harness-arch-4"></a>
### [Cloudflare 开源 security-audit-skill](https://github.com/cloudflare/security-audit-skill) ⭐️ 5.0/10

这是 Cloudflare 开源的 coding agent 工具 security-audit-skill，用于多阶段自动化安全审计。该工具通过编排隔离子 agent 完成侦察、覆盖引导的漏洞狩猎、候选验证、结构化输出、独立记录校验、目标中立报告全流程，输出机器可读、经独立验证的安全发现结果。它是 Cloudflare 漏洞发现工具链的基础组件，相关实践出自官方文章《Build your own vulnerability harness》。

rss · GitHub Trending Daily · 10月24日 01:57

**标签**: `#tools`, `#subagents`, `#sandbox`

---

## Agent 工程师日报
{: #sec-agent-engineer .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-agent-engineer" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-agent-engineer-1"></a>
### [Kimi K3.1 Pro 发布](https://www.kimi.ai/blog/kimi-k3-1-pro) ⭐️ 7.0/10

2026 年 10 月 23 日 Kimi K3.1 Pro 正式上线 Kimi API，当前未开源，Moonshot 承诺 2026 年 11 月 4 日前发布完整模型权重；同步推出 Highspeed 版本，推理速度为普通版 2-3 倍，价格翻倍，输入缓存命中场景定价不变。该模型输入定价为 2 美元/百万 token，输出为 10 美元/百万 token，与 GPT-6.1 Sol 持平，仅为 Claude Opus 5.5 的一半。Moonshot 自研基准显示其性能与 Opus 5.5、GPT-6 Astra 相当，Artificial Analysis 评分为 55，高于 Claude Fable 5.1、GPT-6 Astra、Gemini 4 Argon（均为 53），低于 Claude Opus 5.5（58），是首个达到该评分的即将开源模型。社区 Pac-Man 基准测试显示其与 Claude Sonnet 5.5 得分均为 93，成本 0.68 美元、耗时 11 分钟，低于 Sonnet 5.5 的 1.61 美元成本和 14 分钟耗时。社区反馈显示其订阅配额限制严苛，99 美元/月套餐单会话 47 分钟即触发 5 小时用量上限。

hackernews · Jowsey · 10月23日 16:59 · [社区讨论](https://news.ycombinator.com/item?id=50212065)

**「为什么重要」** 这是首个评分接近主流 frontier 闭源编码模型的即将开源选项，定价低于同类竞品，且提供更高速度的付费版本，为编码 agent 的模型选型提供了新的可选方案；但其开源后的实际性能、安全策略落地效果尚未得到验证。

**「可关注」** K3.1 Pro API 兼容 OpenAI 格式，可直接接入现有 OpenAI 兼容的 agent harness，其定价与 Highspeed 版本的性价比选项可纳入编码场景的模型选型对比。

**「评论」** 社区反馈存在两类典型问题：一是模型回复风格偏直接，偶发身份混淆（自称 Kimi 或 ChatGPT）、引用模糊系统指令的情况；二是订阅配额限制严苛，高等级套餐短时间内即可触发用量上限。另有用户注意到 Moonshot 的开源策略声明，称会控制开源权重的网络攻击能力上限，后续逐步提升该能力。

**标签**: `#coding-agent`, `#permissions`, `#harness`, `#eval`

---

<a id="item-agent-engineer-2"></a>
### [IQuest-Q1 CLI 智能体模型发布](https://huggingface.co/papers/2610.30949) ⭐️ 7.0/10

2026 年 10 月 24 日 Hugging Face Daily Papers 收录编号为 2610.30949 的 IQuest-Q1 相关研究论文，提出面向 CLI 系统的稀疏 MoE 智能体基础模型，总参数 320B、激活参数 15B，该论文当日获得 54 次点赞。论文公开了三阶段训练流程的具体技术方案：预训练结合 Stable SplitNorm、Muon、muP，采用两阶段课程设计，第二阶段提升编码数据占比，同时保持安全与最优学习率的大稳定裕度；中训练扩展多领域、多格式数据混合、逐步延长上下文；后训练采用多脚手架、多版本方案，结合 SFT、领域专用 RL、MOPD 整合互补训练信号强化编码能力，末尾提及模型合并采用 diff 方案但内容截断。该研究为 CLI 智能体、编码智能体训练方向的工程师提供了可参考的训练框架设计。

rss · Hugging Face Daily Papers · 10月24日 01:57

**「为什么重要」** 该研究公开了面向 CLI 智能体的稀疏 MoE 模型可落地的三阶段训练框架，包含多项具体训练技术方案，对正在设计编码智能体训练流程的工程师有直接参考价值；但论文内容截断，模型完整技术细节、性能表现、开源情况等尚未公开。

**「可关注」** 可关注：其预训练阶段两阶段课程设计中编码数据占比的动态调整策略、后训练阶段多脚手架多版本整合互补训练信号的方案，为智能体编码能力训练提供了可复用的设计参考。

**标签**: `#coding-agent`

---

<a id="item-agent-engineer-3"></a>
### [DFM 分块参数记忆架构论文发布](https://huggingface.co/papers/2610.25100) ⭐️ 7.0/10

2026 年 10 月 24 日 Hugging Face Daily Papers 收录的论文提出 Deep Fusion Memory（DFM）分块级参数记忆架构，针对现有外部参数记忆训练数据构建工作量大、输出级融合浅的问题，通过因果记忆预测器结合语料块嵌入监督生成记忆，并将预测记忆融入中间隐状态，减少训练数据构建工作量，实现更深层记忆融合，该论文当前获得 39 次 upvote。当前公开内容未包含性能验证或实现细节。

rss · Hugging Face Daily Papers · 10月24日 01:57

**「为什么重要」** 该架构针对 LLM 外部知识使用中在线检索开销高、持续预训练易灾难性遗忘的痛点，其记忆融合思路可参考用于 Agent 记忆系统设计，但当前无公开实证效果，影响尚未证实。

**「可关注」** 可关注分块级参数记忆将记忆注入中间隐状态而非仅输出层融合的设计思路，以及因果预测器结合检索嵌入监督降低训练数据构建成本的技术路径。

**标签**: `#memory`

---

<a id="item-agent-engineer-4"></a>
### [NVIDIA Nemotron-3.5-Bolt-E4B-4GB 发布](https://www.reddit.com/r/LocalLLaMA/comments/1xdiecx/nvidianvidianemotron35bolte4b4gb_hugging_face/) ⭐️ 6.5/10

2026 年 10 月 23 日 Reddit r/LocalLLaMA 板块用户 jacek2023 发帖分享 NVIDIA 推出的小语言模型 NVIDIA-Nemotron-3.5-Bolt-E4B-4GB，该模型基于 Gemma-4-E4B-it 进一步后训练，优化多轮工具调用、指令遵循与输入接地能力，面向低延迟、低内存、低 TTFT 的边缘/设备 Agent 部署场景。帖子同时提供了配套用于推测解码的 DFlash 草稿模型、BF16 全精度版本链接，以及 Hugging Face 模型仓库与技术报告地址，模型支持商用与非商用用途。该内容为社区二手分享，非 NVIDIA 官方首发公告，主要面向端侧 Agent、低 TTFT 系统开发者。

reddit · r/LocalLLaMA · /u/jacek2023 · 10月23日 16:13

**「为什么重要」** 该模型专门针对端侧 Agent 的低 TTFT、多轮工具调用需求做优化，配套推测解码方案与多格式端侧版本；但实际运行性能、不同硬件下的适配效果尚未有公开第三方验证。

**「可关注」** 可关注：该模型针对低 TTFT、多轮工具调用场景优化，配套 DFlash 推测解码草稿模型，已提供 GGUF 等端侧部署格式。

**标签**: `#coding-agent`

---

<a id="item-agent-engineer-5"></a>
### [OpenDS 基准评估开放网络深度搜索](https://huggingface.co/papers/2610.30181) ⭐️ 6.0/10

2026-10-24，Hugging Face Daily Papers 发布论文《Deep Search in Real-World Web Environments》，提出 OpenDS 基准。该基准评估智能体在真实动态开放网络环境中执行多步深度搜索的能力，要求智能体通过网络搜索、浏览器交互自主探索并整合多源证据。当前源内容被截断，未披露基准规模、任务设计、评估指标及基线性能等具体技术细节。

rss · Hugging Face Daily Papers · 10月24日 01:57

**「为什么重要」** 现有智能体评估多依赖静态检索场景，OpenDS 试图填补实时开放网络环境下的评估空白。但完整论文未公开前，其任务设计合理性、可复现性及实际使用价值仍不确定。

**「可关注」** 可关注：OpenDS 要求智能体在无预设数据分布的真实网络中完成多步搜索与证据整合，与静态检索基准的评估范式存在本质差异。

**标签**: `#eval`, `#web-agent`, `#agent-benchmark`

---

<a id="item-agent-engineer-6"></a>
### [LitPivot 发布：文献语境研究辅助工具](https://allenai.org/blog/litpivot) ⭐️ 5.8/10

2026 年 10 月 23 日，Allen AI 发布 LitPivot 工具，该工具旨在帮助研究者打磨早期研究想法，通过文献支持的批判与修订，随研究提案演变动态提供文献语境化支持。当前公开信息仅包含官方博客的高层介绍，未披露技术架构、性能数据，也未提及与 AI Agent 工程工作流（如 harness 设计、eval 方法、工具链集成）相关的具体细节，对 AI Agent 工程师的直接可操作性有限。

rss · Allen AI · 10月23日 08:00

**「为什么重要」** LitPivot 的定位涉及文献检索、工具链编排方向，若后续公开技术实现细节，可能为研究类 AI Agent 的工作流设计提供参考。

**「可关注」** 可关注 LitPivot 后续公开的技术架构与工具链集成方案，评估其对研究类 Agent 工作流的参考价值。

**标签**: `#orchestration`, `#toolchain`, `#retrieval`

---

## AI 日报
{: #sec-ai-daily .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-daily" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-daily-1"></a>
### [OpenAI Habitat 扩容服务 10 亿 ChatGPT 用户](https://openai.com/index/scaling-storage-one-billion-users-part-two) ⭐️ 7.8/10

OpenAI 发布 Habitat 存储系统扩容技术深挖（Part II），披露其通过可靠多租户架构、全局缓存与 Azure Cosmos DB 组合方案，将 ChatGPT 读性能提升 12 倍，支撑超过 10 亿用户使用。

rss · OpenAI Blog · 10月23日 17:00

**「为什么重要」** 该文是 OpenAI 首次公开超 10 亿用户规模下的存储系统扩容具体技术细节，为同量级互联网服务的存储架构设计提供了可参考的官方落地案例。

**「可关注」** 可关注：超大规模用户场景下，多租户架构搭配全局缓存与 Azure Cosmos DB 的存储组合方案对读性能的提升效果。

**标签**: `#lab`, `#industry`, `#product`

---

<a id="item-ai-daily-2"></a>
### [OpenAI 升级 frontier 安全](https://openai.com/index/securing-our-frontier-model-training-environment) ⭐️ 7.8/10

OpenAI 官方博客介绍 frontier model 训练与评估环境的 containment 强化措施，包括离线环境与高算力红队测试。材料未披露具体技术实现细节与覆盖范围。

rss · OpenAI Blog · 10月23日 10:00

**「为什么重要」** 这属于实验室安全政策更新，对 AI 行业前沿模型的安全治理实践具有参考意义。

**「可关注」** 可关注：离线环境与高算力红队测试在 frontier model 安全评估中的具体应用方式。

**标签**: `#lab`, `#policy`, `#eval`, `#industry`

---

## AI 羊毛
{: #sec-ai-deals .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-deals" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-deals-1"></a>
### [智谱 ZCode 1024 程序员节发额度](https://www.appinn.com/zcode-1024-free-500-million-tokens/) ⭐️ 8.0/10

你看到的内容可能由第三方 AI 基于小众软件文章提炼总结而成，可能与原文真实意图存在偏差。不代表小众软件观点和立场。请&lt;a href=&quot;https://www.appinn.com/zcode-1024-free-500-million-tokens/&quot; target=&quot;\_blank&quot;&gt;点击链接阅读原文&lt;/a&gt;细致比对和校验。智谱 ZCode 推出 1024 程序员节活动，可免费领取 5 亿 Tokens 额度，支持 GLM-5.3 与 GLM-5.3-Flash 模型，未说明两款模型的额度分配方式，不可理解为每款模型各送 5 亿 Tokens。新老用户均可参与，需下载 ZCode 客户端登录后点击活动入口领取。额度 2026 年 10 月 23 日 23:00 生效，2026 年 10 月 26 日 09:00 到期，仅本周末有效。

rss · 小众软件 · 10月23日 15:17

**「为什么重要」** 当前处于可领取状态，额度有效期仅覆盖本周末，适合有短期模型调用需求的开发者测试小工具或旧项目。

**「可关注」** 可关注：领取后需到「模型设置 → Start Plan」查看 ZCode 1024 Dev Day 活动套餐，注意区分其与日常 Start Plan 的每日 300 万/500 万 Tokens 额度，避免混淆。

**标签**: `#credits`, `#free-tier`, `#promo`, `#limited-free`, `#api`

---

<a id="item-ai-deals-2"></a>
### [Epic 本周免费游戏 10.23~10.29](https://www.appinn.com/eggs-261023/) ⭐️ 8.0/10

你看到的内容可能由第三方 AI 基于小众软件文章提炼总结而成，可能与原文真实意图存在偏差。不代表小众软件观点和立场。请&lt;a href=&quot;https://www.appinn.com/eggs-261023/&quot; target=&quot;\_blank&quot;&gt;点击链接阅读原文&lt;/a&gt;细致比对和校验。&lt;br /&gt;&lt;br /&gt;Epic Games 于 10 月 23 日至 29 日开展每周免费游戏赠送活动。PC 端可领取《斯盖尔仪式 / Sker Ritual》《归家 / Home – A Unique Horror Adventure》2 款游戏，移动端可领取《归家》1 款游戏，领取需前往对应 Epic 商店页面，活动截止时间为 10 月 29 日。

rss · 小众软件 · 10月23日 07:34

**「为什么重要」** 本次免费领取为限时活动，活动结束后游戏将恢复收费，两款可领游戏均支持中文，适合恐怖题材玩家收藏。

**「可关注」** 可关注：《归家》的 PC、Android、iOS 三个平台版本需分别领取，均可在浏览器端完成操作。

**标签**: `#promo`, `#limited-free`, `#free-games`

---

<a id="item-ai-deals-3"></a>
### [Show HN 免费无限制 AI 文本检测器发布](https://kouh.me/ai-text-detector) ⭐️ 6.0/10

Show HN 用户 mrkn1 于 2026-10-23 发布一款宣称免费、无限制、私有的 AI 文本检测工具，链接为 https://kouh.me/ai-text-detector。目前无公开的使用限制、服务方背景及可信度验证信息，发布时仅获 1 个赞、0 条评论。

rss · HN Free API / Credits · 10月23日 21:06

**「为什么重要」** 该工具未公开服务条款、隐私政策及实际运行规则，可靠性与数据安全风险均未得到验证，暂不适合作为正式检测方案使用。

**「可关注」** 可关注：该工具宣称无使用限制，但无任何公开合规与安全说明，若尝试使用需自行承担数据泄露风险。

**标签**: `#free-tier`

---