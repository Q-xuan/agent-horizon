---
layout: default
title: "Horizon Summary: 2026-10-29 (ZH)"
date: 2026-10-29
lang: zh
---

> 从 209 条内容中筛选出 17 条重要资讯。

<nav id="ah-toc" class="ah-toc" aria-label="目录"><span class="ah-toc-title">目录</span><ul><li><a href="#sec-harness-arch"><span class="ah-toc-name">Harness 架构</span><span class="ah-toc-count">3条</span></a></li><li><a href="#sec-agent-engineer"><span class="ah-toc-name">Agent 工程师日报</span><span class="ah-toc-count">6条</span></a></li><li><a href="#sec-ai-daily"><span class="ah-toc-name">AI 日报</span><span class="ah-toc-count">6条</span></a></li><li><a href="#sec-ai-deals"><span class="ah-toc-name">AI 羊毛</span><span class="ah-toc-count">2条</span></a></li></ul></nav>

---

**[Harness 架构](#sec-harness-arch)**
1. [Mastra Core 1.80.0 发布](#item-harness-arch-1) ⭐️ 7.8/10
2. [E2B SDK 2.62.0 发布](#item-harness-arch-2) ⭐️ 7.8/10
3. [MCP servers v2.2.0 安全更新发布](#item-harness-arch-3) ⭐️ 7.8/10

**[Agent 工程师日报](#sec-agent-engineer)**
1. [NVIDIA Nemotron 3.5 Transcribe 开源](#item-agent-engineer-1) ⭐️ 7.8/10
2. [Gemini 4 Carbon 官宣](#item-agent-engineer-2) ⭐️ 7.8/10
3. [MPO 优化 long-horizon LLM agents](#item-agent-engineer-3) ⭐️ 7.0/10
4. [VibeVideoBench 基准发布](#item-agent-engineer-4) ⭐️ 7.0/10
5. [HF 论文：Agent 记忆税研究](#item-agent-engineer-5) ⭐️ 7.0/10
6. [GitHub Octoverse 2026 数据发布](#item-agent-engineer-6) ⭐️ 6.0/10

**[AI 日报](#sec-ai-daily)**
1. [GitHub Octoverse 2026：代码活动量创历史新高](#item-ai-daily-1) ⭐️ 8.8/10
2. [OpenAI ServiceNow 合作扩围](#item-ai-daily-2) ⭐️ 7.8/10
3. [OpenAI 谈 AI 融入企业组织架构](#item-ai-daily-3) ⭐️ 7.8/10
4. [GitHub Universe 2026 发布 AI 交付产品矩阵](#item-ai-daily-4) ⭐️ 7.8/10
5. [Legora 构建法律工作智能体 OS](#item-ai-daily-5) ⭐️ 6.8/10
6. [Genie 4 发布：首个原生音频实时世界模型](#item-ai-daily-6) ⭐️ 5.5/10

**[AI 羊毛](#sec-ai-deals)**
1. [ChatGPT Pro API 额度福利](#item-ai-deals-1) ⭐️ 6.0/10
2. [IFTTT 免费计划取消无限运行权益](#item-ai-deals-2) ⭐️ 5.0/10

---

## Harness 架构
{: #sec-harness-arch .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-harness-arch" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-harness-arch-1"></a>
### [Mastra Core 1.80.0 发布](https://github.com/mastra-ai/mastra/releases/tag/%40mastra/core%401.80.0) ⭐️ 7.8/10

这是 Mastra Core 1.80.0 的官方发布。引入用户级 OAuth 连接隔离（@mastra/connect 的 tools\(\{ resourceId \}\) 与 userConnectRoutes\(\)），内置 request\_connection 工具供聊天界面渲染连接卡片。新增 Span 聚合 API（POST /observability/spans/aggregate）及 ClickHouse/Postgres/DuckDB 存储后端，支持按 agent run、tool、workflow 分组统计延迟、错误率、token 和成本。同时统一 provider 错误分类（classifyProviderError）、支持 durable run 取消（agent.abortRun），新增 renderOnly 工具与线程运行状态订阅，并调整 trace 查询接口。

github · PaulieScanlon · 10月28日 15:23

**「设计要点」** 连接层采用 resourceId 硬隔离，确保用户 OAuth 凭证不可跨用户复用；可观测层通过 span 聚合 API 将运行时指标外置到列式/关系型存储，降低 agent 运行时的查询耦合。错误处理统一到 provider 错误分类器，流式响应携带 provider 元数据，支持客户端持久化后复现一致错误语义。

**「改了什么」** 新增用户级 OAuth 连接隔离与内置 request\_connection 工具，Span 聚合 API 支持 ClickHouse/Postgres/DuckDB 后端提供分组指标查询，统一 provider 错误分类与持久化，retry 逻辑对齐分类结果，并新增 durable run 取消（agent.abortRun）、线程运行状态订阅（withRunStatus: true）、按调用指定 agentModel 的实验能力及 renderOnly 工具。Breaking changes 包括：queryTraceThreads\(\) 移除 model/provider 字段且 page.limit 上限 100，connect-session 返回 launchUrl，code-sdk 不再默认注册内置子代理，playground-ui TracesExplorer 排序 API 改为 \{ field, direction \} 对象。

**标签**: `#permissions`, `#tools`, `#eval`, `#observability`

---

<a id="item-harness-arch-2"></a>
### [E2B SDK 2.62.0 发布](https://github.com/e2b-dev/E2B/releases/tag/e2b%402.62.0) ⭐️ 7.8/10

E2B SDK 2.62.0 针对沙箱内命令执行与文件操作引入内存优化。新增 \`retainOutput\`/\`retain\_output\` 选项（默认 true），设为 false 时 stdout/stderr 不再缓冲在内存。\`files.write\` 支持流式写入字节块，JS 接受 \`AsyncIterable&lt;Uint8Array&gt;\` 与 \`ReadableStream\`，Python 接受 \`Iterable\[bytes\]\` 与 \`AsyncIterable\[bytes\]\`。

github · github-actions\[bot\] · 10月28日 20:24

**「设计要点」** 运行时通过输出回调（\`onStdout\`/\`onStderr\` 等）继续传递数据，但结果对象与句柄上的 \`stdout\`/\`stderr\` 字段在关闭缓冲时置为 undefined/None。流式上传强制使用 octet-stream，浏览器不支持流式请求体时抛出 \`InvalidArgumentError\`。

**「改了什么」** \`commands.run\` 与 \`commands.connect\` 新增 \`retainOutput\`/\`retain\_output\` 参数（默认 true），设为 false 时停止内存缓冲 stdout/stderr，结果对象与句柄上的输出字段置为 undefined/None。\`files.write\` 改为流式传输字节块，JS 与 Python 分别接受同步/异步可迭代对象，不再全量缓冲。\`gzip: true\` 与 \`useOctetStream: false\` 的组合现在被显式拒绝。

**标签**: `#sandbox`, `#tools`, `#memory`, `#runtime`

---

<a id="item-harness-arch-3"></a>
### [MCP servers v2.2.0 安全更新发布](https://github.com/modelcontextprotocol/servers/releases/tag/v2.2.0) ⭐️ 7.8/10

modelcontextprotocol/servers 发布 v2.2.0，核心内容是应对 2026 年 10 月 eMudhra CA 私钥泄露事件的安全更新。TypeScript 服务器依赖 Node.js 24.22.1+ 或 26.12.1+ 运行时的 CA 证书 bundle，Python 服务器 mcp-server-fetch 升级 certifi 至 2026.10.23 以移除受影响的 eMudhra 根证书。本次发布同时包含 server-everything、server-filesystem、server-memory 的功能修复与 mcp-server-fetch 的网络行为加固。

github · cliffhall · 10月28日 20:57

**「设计要点」** TypeScript 服务器不内置 CA 证书，完全委托 Node.js 运行时做 TLS 验证；Python 服务器通过 httpx 依赖 certifi 包。网络边界按服务器隔离：server-everything 是唯一发起出站 HTTPS 请求的 TypeScript 服务器，server-filesystem、server-memory、server-sequential-thinking、mcp-server-git、mcp-server-time 无网络连接。

**「改了什么」** 安全层面：TypeScript 服务器要求 Node.js 24.22.1+ 或 26.12.1+，mcp-server-fetch 的 Dockerfile 锁定 certifi 2026.10.23。功能修复：server-everything 修复 gzip-file-as-resource 对 HTTP 错误的处理、环境变量掩码、非公网地址拒绝；server-filesystem 修复跨文件系统移动、路径大小写处理、realpath 超时；server-memory 修复未建模字段丢失与迁移失败处理；mcp-server-fetch 增加 --no-readability-js 选项、拒绝 IPv4 兼容 IPv6 地址、修复 HTML 解码与 robots.txt 5xx 拒绝。

**标签**: `#mcp`, `#runtime`, `#tools`

---

## Agent 工程师日报
{: #sec-agent-engineer .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-agent-engineer" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-agent-engineer-1"></a>
### [NVIDIA Nemotron 3.5 Transcribe 开源](https://huggingface.co/blog/nvidia/nemotron-transcribe-granary) ⭐️ 7.8/10

2026 年 10 月 28 日，Hugging Face 官方博客发布 NVIDIA 开源的 Nemotron 3.5 Transcribe 语音模型与 Granary v2 数据管道。该模型为单 checkpoint 集成转录、说话人分离、翻译、音频问答能力，支持 40 种语言转录、31 种语言与英语互译、13 种语言说话人标注，最长处理 1 小时音频、最多标注 8 位说话人，支持自然语言提示控制输出，仅支持录播音频处理，配套微调食谱与 Granary v2 多语言数据管道，已上线 Hugging Face 与 ModelScope，量化版本即将支持 RTX Spark、DGX Spark 等设备本地运行。该模型面向需要音频处理能力的 Agent 工具链、多语言转录场景开发者开放。

rss · Hugging Face Blog · 10月28日 14:58 · [社区讨论](https://news.ycombinator.com/item?id=50275128)

**「为什么重要」** 该模型已在多个公开基准验证领先性：英语转录为首个登顶 Hugging Face Open ASR Leaderboard 的开源权重模型，说话人分离指标在 David AI、VoiceArena 基准排名第一，仅约 4B 活跃参数即达到开源权重模型准确率-活跃参数帕累托前沿。配套开放的数据管道与微调方案降低了特定场景适配门槛，但实际落地效果仍需开发者根据自身场景验证。

**「可关注」** 可关注：该模型音频问答能力仅支持英语训练，词级时间戳、说话人分离等能力支持的语言范围与转录、翻译不同，使用时需对照模型卡的任务-语言矩阵确认支持情况。

**「评论」** 社区讨论集中在部署限制与实际体验：有用户指出模型仅支持录播音频不支持实时流，且需 NVIDIA GPU 运行；另有用户提到该模型是目前唯一开源支持近场说话人转录的语音 LLM，但日常使用仍有每几句出错的概率。

**标签**: `#harness`, `#toolchain`, `#speech-model`, `#fine-tuning`, `#multimodal`

---

<a id="item-agent-engineer-2"></a>
### [Gemini 4 Carbon 官宣](https://deepmind.google/blog/gemini-4-carbon-our-next-frontier-model/) ⭐️ 7.8/10

Google DeepMind 于 2026-10-28 在官方博客宣布即将推出 Gemini 4 Carbon 前沿模型。该公告面向 AI agent 开发者群体，涉及 coding-agent、eval 与 harness 方向。目前公开材料未披露具体技术规格、性能基准或正式发布时间。这是该系列模型的下一代 frontier 版本，但细节待官方后续补充。

rss · Google DeepMind · 10月28日 17:00

**「为什么重要」** frontier 模型更新通常意味着底层能力边界可能移动，对依赖模型能力的 agent harness 有潜在影响。但具体影响范围取决于后续披露的技术细节，目前尚无法验证。

**「可关注」** 可关注：官方已确认下一代 frontier 模型存在，但当前无技术细节可做集成或适配规划，建议等待正式技术文档。

**标签**: `#coding-agent`, `#eval`, `#harness`

---

<a id="item-agent-engineer-3"></a>
### [MPO 优化 long-horizon LLM agents](https://huggingface.co/papers/2610.35013) ⭐️ 7.0/10

2026-10-29 ， HF daily papers 收录预印本，提出 Multiscale Policy Optimization \(MPO\)。MPO 结合 Multiscale Advantage Estimation \(MAE\) 与 turn-level importance sampling，将 credit assignment 与 policy updates 对齐到 turn scale。在 search 、 tool-use 与 automation 任务上，4B 与 30B-A3B 模型均取得 consistent gains over strong RL baselines。该工作针对 long-horizon LLM agents 的 RL 训练，影响做 agent 性能优化的工程师。预印本尚未经 peer review 。

rss · Hugging Face Daily Papers · 10月29日 03:35

**「为什么重要」** 该工作直接针对 long-horizon LLM agents 的 credit assignment 难题，提供可复现的 RL 优化方案。实验覆盖 search 、 tool-use 与 automation 三类 agent 任务，对做 RL-based agent 训练的工程师有参考价值。尚未证实的影响：预印本结论需经 peer review 与更广泛复现。

**「可关注」** turn-level credit assignment 与 policy update scale 对齐，在 search 、 tool-use 与 automation 任务上带来 consistent gains over strong RL baselines。

**标签**: `#coding-agent`

---

<a id="item-agent-engineer-4"></a>
### [VibeVideoBench 基准发布](https://huggingface.co/papers/2610.35864) ⭐️ 7.0/10

VibeVideoBench 是评估多模态代理代码驱动视频生成能力的新基准。基准包含 239 个英语和汉语自包含任务，覆盖 12 个类别。任务要求代理在原生沙盒 harness 内运行，不使用图像或视频生成模型，在一小时内交付带声音的 MP4 文件。评估采用分层且基于证据的规则，检查程序规范与输出证据。Hugging Face Daily Papers 于 2026-10-29 整理发布该基准。

rss · Hugging Face Daily Papers · 10月29日 03:35

**「为什么重要」** 该基准直接针对代码渲染视频的代理评估场景，为 agent 工程师提供标准化测试 harness 与任务集。材料显示其要求代理在无生成模型支持下完成视频交付，这区别于当前扩散视频模型路线，对 coding agent 与 multimodal agent 评估有直接参考价值。

**「可关注」** 可关注：基准强制要求原生沙盒 harness 且禁用图像视频生成模型，这为评估纯代码渲染代理提供了可复现的对比基线。

**标签**: `#eval`, `#coding-agent`, `#harness`

---

<a id="item-agent-engineer-5"></a>
### [HF 论文：Agent 记忆税研究](https://huggingface.co/papers/2610.34073) ⭐️ 7.0/10

2026 年 10 月 29 日 Hugging Face 每日论文发布论文《Memory Tax: Dissecting the Net Value of Agent Memory》的截断摘要，该论文在 HF 每日论文站获得 146 次点赞。该研究开展大规模多基准、多模型后端的 Agent 记忆系统评估，提出将记忆相对朴素 RAG 的净价值拆分为记忆收益与记忆税，实证发现多数专用记忆系统在多项基准上表现不及朴素 RAG，净价值为负。当前材料为聚合站摘要，缺少完整实验细节与原始论文全文。

rss · Hugging Face Daily Papers · 10月29日 03:35

**「为什么重要」** 该研究首次系统拆解 Agent 记忆的净价值构成，为 Agent 记忆组件设计、记忆系统评测体系构建提供了可量化的参考框架，但完整实验结论尚未公开。

**「可关注」** 可关注：当前多数专用 Agent 记忆系统在多基准评估中表现弱于朴素 RAG，记忆系统选型前需先验证其在目标任务上的净收益。

**标签**: `#memory`, `#eval`

---

<a id="item-agent-engineer-6"></a>
### [GitHub Octoverse 2026 数据发布](https://simonwillison.net/2026/Oct/28/github-octoverse-2026/) ⭐️ 6.0/10

2026 年 10 月 28 日 GitHub Universe 大会上，GitHub 发布年度 Octoverse 2026 报告，现场公布核心指标：月合并 PR 达 2.2 亿，同比不到一年增长三倍；月提交数达 73.8 亿，同比超三倍，其中大部分增长来自 2026 年下半年；月新建仓库达 3030 万，同比翻倍。报告新增按行业分类的统计，以及涉及互操作性、逆向工程的仓库专项统计，其统计方法包括用 LLM 分类修正 VPN 导致的用户位置偏差、用多语言嵌入模型按 NAICS 标准对仓库做行业分类。现场分享将上述增长归因于代理工程（agentic engineering）的普及，相关数据可为开发者、编码 agent 工程师及生态分析人员提供参考。

rss · Simon Willison · 10月28日 16:45

**「为什么重要」** 这份报告提供了 2026 年 GitHub 生态的量化活动基准，其中提交、合并 PR 的集中增长趋势，可辅助编码 agent 工程师判断自身工具对开发者产出的实际影响，但增长与代理普及的因果关联尚未经独立验证。

**「可关注」** 可关注：2026 年下半年提交量、合并 PR 量的集中增长幅度，可作为校验编码 agent 实际效率贡献的参考基准。

**标签**: `#coding-agent`

---

## AI 日报
{: #sec-ai-daily .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-daily" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-daily-1"></a>
### [GitHub Octoverse 2026：代码活动量创历史新高](https://github.blog/news-insights/octoverse/octoverse-commits-pushes-reach-new-highs-in-2026-as-developers-build-with-agents/) ⭐️ 8.8/10

GitHub 发布 Octoverse 2026 报告，披露过去 12 个月（截至 2026 年 9 月 30 日，含公开及私有仓库）平台代码推送量达 179 亿次，超过 2024 与 2025 年总和；提交量达 343 亿次，为两年前的 3 倍以上；合并 PR 达 13 亿次，日均 350 万次。报告同时显示，含 agent 配置的新仓库平均提交量是无配置新仓库的 8 倍，9 月超过 40% 的 PR 由 agent 发起，该比例 3 月为 17%。过去 12 个月 GitHub Actions 每秒运行 1440 个任务，日均 1.24 亿次，为去年的 3 倍以上；开发者合并超 3000 万个 Dependabot PR 更新依赖，速度约为 2025 年的 2 倍。

rss · GitHub Blog · 10月28日 16:07

**「为什么重要」** 报告显示 agent 已从开发者试玩工具转为日常开发协同工具，直接推动年中后 GitHub 活动量陡增，同时开发者跨医疗、农业等新领域、多模型使用 agent 的态势正在形成。

**「可关注」** 可关注：含 agent 配置的新仓库平均提交量是无配置新仓库的 8 倍，agent 已深度嵌入日常开发流程。

**标签**: `#industry`, `#open-source`, `#product`

---

<a id="item-ai-daily-2"></a>
### [OpenAI ServiceNow 合作扩围](https://openai.com/index/openai-servicenow-partnership-expansion) ⭐️ 7.8/10

2026 年 10 月 28 日，OpenAI 与 ServiceNow 宣布扩大合作，实现双向集成：OpenAI 的模型与 agent 将接入 ServiceNow 平台，同时 ServiceNow 的工作流将嵌入 ChatGPT 与 Codex 产品中。

rss · OpenAI Blog · 10月28日 13:15

**「为什么重要」** 本次合作将 AI 能力与企业级 IT 服务流程打通，为双方企业用户提供更集成的自动化工作流支持，降低跨平台操作成本。

**「可关注」** 可关注：ServiceNow 工作流在 ChatGPT、Codex 中的具体集成方式与后续落地节奏。

**标签**: `#lab`, `#industry`, `#product`, `#model`

---

<a id="item-ai-daily-3"></a>
### [OpenAI 谈 AI 融入企业组织架构](https://openai.com/index/the-future-of-the-firm) ⭐️ 7.8/10

OpenAI 官方博客发布文章，分析 AI 整合进企业组织架构的潜在模式。文章提出 AI 可能以三种方式进入企业组织架构：低于现有岗位层级、并行于现有岗位、填补现有岗位之间的空白，阐述 AI 在未来企业中的角色定位。

rss · OpenAI Blog · 10月28日 10:00

**「为什么重要」** 作为头部 AI 实验室的官方视角，其对企业 AI 组织整合路径的分析可为行业 AI 落地提供可参考的行业洞察。

**「可关注」** 可关注：AI 融入企业组织架构的三种潜在路径（低于、并行、介于现有岗位）的实际落地可行性。

**标签**: `#lab`, `#industry`

---

<a id="item-ai-daily-4"></a>
### [GitHub Universe 2026 发布 AI 交付产品矩阵](https://github.blog/news-insights/company-news/github-universe-2026-evolving-every-layer-of-the-stack/) ⭐️ 7.8/10

GitHub 于 2026 年 10 月 28 日在 Universe 大会发布 AI 辅助软件交付体系及多款配套产品。核心更新包括支持跨项目 agent 编排的 GitHub Copilot app、多模型编排工具 Copilot Fusion、多仓库并行会话的 Copilot projects、跨端持续会话能力、可自学习的 Copilot automations 以及高危问题检出率最高的 Copilot code review Max。Copilot Fusion 在 Artificial Analysis Coding Agent Index 中得分接近 Opus 5.5 Max，成本降低 50%、单任务耗时减少 40%。GitHub Enterprise 客户无需单独订阅即可使用全部 Copilot 功能，按实际 AI 用量付费。

rss · GitHub Blog · 10月28日 16:09

**「为什么重要」** 这是全球主流开发者工具平台首次公开完整 agentic 软件交付产品矩阵，覆盖从需求提出到代码合并的全链路 AI 能力，同时通过多模型编排降低了企业使用 AI 编码工具的成本门槛，是行业 AI 软件交付路径的重要更新。

**「可关注」** 可关注：GitHub Enterprise 客户现已无需单独订阅即可使用全量 Copilot 功能，按实际 AI 用量付费，可简化企业工具采购及使用流程。

**标签**: `#lab`, `#industry`, `#product`

---

<a id="item-ai-daily-5"></a>
### [Legora 构建法律工作智能体 OS](https://openai.com/index/legora) ⭐️ 6.8/10

OpenAI 官方博客发布行业案例，介绍法律科技公司 Legora 正基于 OpenAI 模型、ChatGPT 及 Codex 构建面向法律工作的智能体操作系统，用于加速法律流程、拓展合同分析能力，释放律师精力聚焦更高价值工作。

rss · OpenAI Blog · 10月28日 09:30

**「为什么重要」** 该案例是 OpenAI 官方披露的垂直行业落地动态，可参考其产品栈在法律科技场景的适配路径。

**「可关注」** 可关注：垂直行业智能体操作系统对通用模型、交互工具、编码工具的集成范式。

**标签**: `#lab`, `#industry`, `#product`

---

<a id="item-ai-daily-6"></a>
### [Genie 4 发布：首个原生音频实时世界模型](https://mp.weixin.qq.com/s?__biz=MzIwNzc2NTk0NQ==&amp;mid=2247622879&amp;idx=1&amp;sn=aed85a9a679302016c4300873ec91f32) ⭐️ 5.5/10

Google DeepMind 于 2026-10-28 发布 Genie 4 世界模型，官方定位为迄今最具交互性的世界模型。这是 DeepMind 首个原生生成音频的实时世界模型，支持通过文本输入实时生成带环境声的交互场景，并提升了物理运动与人物动作的自然度。

rss · 夕小瑶科技说 · 10月28日 10:11

**「为什么重要」** Genie 4 首次将音频生成集成到实时世界模型中，实现了文本驱动的多模态交互，使世界模型从纯视觉生成迈向音频-视觉联合生成。

**「可关注」** 可关注：实时世界模型中音频与视觉的联合生成能力，以及文本指令对场景元素的实时控制能力。

**标签**: `#model`, `#lab`, `#industry`

---

## AI 羊毛
{: #sec-ai-deals .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-deals" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-deals-1"></a>
### [ChatGPT Pro API 额度福利](https://help.openai.com/en/articles/20001626-api-credits-benefit-for-eligible-chatgpt-subscriptions#credit-amounts) ⭐️ 6.0/10

OpenAI 官方帮助文档显示，符合条件的 ChatGPT Pro 订阅用户可获 100/200/500 美元额度的 API credits，当前未披露具体领取条件、额度有效期及截止时间，无额外可操作信息。

rss · HN Free API / Credits · 10月29日 02:36

**「可关注」** 可关注：该 API 额度福利仅面向符合条件的 ChatGPT Pro 订阅用户，额度分 100/200/500 美元三档，具体领取规则与有效期暂未公开。

**标签**: `#credits`, `#api`, `#promo`

---

<a id="item-ai-deals-2"></a>
### [IFTTT 免费计划取消无限运行权益](https://ifttt.com/explore/put-ai-to-work-for-you) ⭐️ 5.0/10

IFTTT 官方宣布终止其免费计划的无限运行权益，具体调整后的免费额度、限制规则、生效时间等细则未在给定内容中披露。

rss · HN Free API / Credits · 10月28日 18:39

**「为什么重要」** 该权益收缩会影响依赖免费方案使用 IFTTT 自动化流程的用户，后续需关注官方公布的具体规则。

**「可关注」** 可关注：IFTTT 后续发布的免费计划细则，评估现有自动化流程的适配或成本调整。

**标签**: `#free-tier`, `#promo`, `#limited-free`

---