---
layout: default
title: "Horizon Summary: 2026-11-28 (ZH)"
date: 2026-11-28
lang: zh
---

> 从 190 条内容中筛选出 10 条重要资讯。

<nav id="ah-toc" class="ah-toc" aria-label="目录"><span class="ah-toc-title">目录</span><ul><li><a href="#sec-harness-arch"><span class="ah-toc-name">Harness 架构</span><span class="ah-toc-count">2条</span></a></li><li><a href="#sec-agent-engineer"><span class="ah-toc-name">Agent 工程师日报</span><span class="ah-toc-count">5条</span></a></li><li><a href="#sec-ai-deals"><span class="ah-toc-name">AI 羊毛</span><span class="ah-toc-count">3条</span></a></li></ul></nav>

---

**[Harness 架构](#sec-harness-arch)**
1. [pydantic-ai v2.77.0 发布](#item-harness-arch-1) ⭐️ 7.8/10
2. [MCP servers v2.6.0 发布](#item-harness-arch-2) ⭐️ 7.8/10

**[Agent 工程师日报](#sec-agent-engineer)**
1. [DeepCrossAttention 实现最高 3 倍推理加速](#item-agent-engineer-1) ⭐️ 7.0/10
2. [OS-Omni v1 跨平台 Agent 基准发布](#item-agent-engineer-2) ⭐️ 7.0/10
3. [HF 论文：编码智能体视觉推理更强](#item-agent-engineer-3) ⭐️ 7.0/10
4. [HF 每日论文：AI agent 数据库错误归因](#item-agent-engineer-4) ⭐️ 7.0/10
5. [Gated DeltaNet-2 长上下文训练稳定性修复](#item-agent-engineer-5) ⭐️ 6.0/10

**[AI 羊毛](#sec-ai-deals)**
1. [NodeWarden 支持离线云备份功能](#item-ai-deals-1) ⭐️ 7.0/10
2. [SonoJS Mock 免费前端 Mock 工具发布](#item-ai-deals-2) ⭐️ 7.0/10
3. [Show HN 免费数学科普有声书+电子书](#item-ai-deals-3) ⭐️ 7.0/10

---

## Harness 架构
{: #sec-harness-arch .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-harness-arch" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-harness-arch-1"></a>
### [pydantic-ai v2.77.0 发布](https://github.com/pydantic/pydantic-ai/releases/tag/v2.77.0) ⭐️ 7.8/10

pydantic-ai v2.77.0 正式发布。本次新增 SQLite、Postgres、MongoDB 三种 \`ConversationStore\` 后端，Pax session store 重命名为 \`SqliteSessionStore\`，旧名称保留但触发 \`HarnessDeprecationWarning\`。技能加载逻辑改为默认跳过缺失或不可读路径并给出警告，不再中断运行；同时引入 \`thinking\_summary\`、\`compact\_history\(\)\` 钩子、流式 \`incomplete\` 状态、子代理权限收紧（低于 \`&\#x27;operator&\#x27;\` 的磁盘定义被跳过）以及回退子代理请求计入 \`UsageLimits\`。此外调整了 \`Memory\`/\`Planning\` 上下文插入位置、压缩收据类型、Claude on Foundry 的 system message 格式，并提前对 GPT-5.4/5.6 的工具请求做前置校验。

github · dsfaccini · 11月27日 23:32

**「设计要点」** 运行时层新增 \`CompactionStartEvent\`/\`CompactionEndEvent\` 流式事件和 \`request\_compaction\(\)\` 钩子，改变历史压缩的触发与观测方式。权限模型收紧：\`SubAgents\` 拒绝加载低于 \`&\#x27;operator&\#x27;\` 权限的磁盘定义文件，\`working\_directory\` 委托继承父级最低目录权限，\`/permissions\` 模式进入 Pax 页脚；记忆层调整 \`Memory\` 和 \`Planning\` 启动快照插入位置，压缩收据改为 \`CompactionReceiptPart\`。

**「改了什么」** 新增 SQLite、Postgres、MongoDB 三种 \`ConversationStore\` 后端，会话存储类重命名并触发弃用警告；技能加载默认容错，跳过缺失/不可读路径，\`pax\` 技能搜索优先最近目录。新增跨提供商的 \`thinking\_summary\`、\`compact\_history\(\)\` 钩子与 compaction 流式事件；子代理权限收紧，回退子代理请求计入 \`UsageLimits\`，流式响应增加 \`incomplete\` 终态，GPT-5.4/5.6 工具请求前置校验提前抛出 \`ModelRequestRejectedError\`。

**标签**: `#memory`, `#tools`, `#compatibility`

---

<a id="item-harness-arch-2"></a>
### [MCP servers v2.6.0 发布](https://github.com/modelcontextprotocol/servers/releases/tag/v2.6.0) ⭐️ 7.8/10

modelcontextprotocol/servers v2.6.0 发布，修复 git、memory、fetch、filesystem 四个服务器的 8 个安全漏洞。git 服务器阻断 Git LFS 配置触发的任意代码执行，修复 \`--repository\` 逃逸、凭据泄露、环境变量读取、alternates 注入、忽略文件覆盖，并补全 v2.5.0 遗留的写入后 repository 检查；memory 服务器阻止临时文件符号链接权限变更；fetch 服务器补全 robots.txt 对反斜杠和路径参数的匹配；filesystem 服务器在 Windows 上增加目录读取前后检查。TypeScript 包已迁至语义版本，需显式安装 \`@modelcontextprotocol/server-memory@2.2.2\` 和 \`@modelcontextprotocol/server-filesystem@2.4.1\`。

github · cliffhall · 11月27日 09:51

**「设计要点」** git 服务器在启动时记录 \`--repository\` 的 Git 目录并拒绝外部重定向，每次 Git 调用使用私有对象目录隔离 alternates。memory 服务器改为独占创建临时文件并通过句柄完成写入与权限设置，阻断符号链接交换。

**「改了什么」** 修复 git 服务器 6 个漏洞，包括 Git LFS 任意代码执行、\`--repository\` 逃逸、凭据泄露、环境变量读取、alternates 注入及忽略文件覆盖，并补全 v2.5.0 遗留的写入后 repository 检查。memory 服务器阻断临时文件符号链接权限提升，fetch 服务器补全 robots.txt 反斜杠与路径参数匹配，Windows 平台 filesystem 服务器增加目录读取前后检查。

**标签**: `#mcp`, `#tools`, `#sandbox`, `#memory`

---

## Agent 工程师日报
{: #sec-agent-engineer .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-agent-engineer" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-agent-engineer-1"></a>
### [DeepCrossAttention 实现最高 3 倍推理加速](https://research.google/blog/supercharging-transformer-residual-connections/) ⭐️ 7.0/10

2026 年 11 月 27 日 Hacker News 讨论分享了 Google Research 提出的 DeepCrossAttention（DCA）transformer 修改方案。DCA 采用层间深度交叉注意力（而非标准 token 间注意力），让每个 token 查询所有先前层嵌入的动态加权组合，无需承担传统注意力扩展的计算开销。官方称该方案可实现最高 3 倍推理加速，模型质量与基线相当，同时提升历史上下文访问能力。目前仅能看到 HN 讨论内容，未获取官方博客全文及独立验证结果，相关方为 AI agent 工程师及 transformer 优化从业者。

hackernews · ComputedCamp995 · 11月27日 23:06 · [社区讨论](https://news.ycombinator.com/item?id=50672565)

**「为什么重要」** 该方案直接针对 transformer 推理效率优化，若声明属实，可降低 AI agent 的推理延迟与运行成本，同时改进的历史上下文处理能力或对长程推理、agent 记忆模块有增益。但目前仅来自 HN 讨论的二手信息，尚未有官方全文或独立验证，相关影响尚未证实。该内容并非优先级最高的必读材料，但提供了有价值的 transformer 优化技术背景。

**「可关注」** 可关注：层间交叉注意力的设计绕开了传统 token 级注意力扩展的计算瓶颈，为 transformer 效率优化提供了不同于常规 token 压缩、注意力稀疏化的新思路。

**「评论」** 社区讨论中，有用户猜测该技术可能与 Gemini Neon 的高性价比、低延迟表现相关；有用户认为该设计或能解决经典的&quot;草莓问题&quot;（数词、字符计数类推理难题）；另有用户指出博客配图使用折线图展示不同方法性能不符合规范，还有用户联想到 DenseNet 的跨层连接设计。

**标签**: `#memory`, `#transformer-architecture`, `#inference-optimization`, `#long-context-reasoning`

---

<a id="item-agent-engineer-2"></a>
### [OS-Omni v1 跨平台 Agent 基准发布](https://huggingface.co/papers/2611.34232) ⭐️ 7.0/10

OS-Omni 是一个面向通用计算机使用代理的跨平台实时基准测试与执行环境，覆盖 Windows、Ubuntu、macOS、iOS、Android 和 Web 六类操作系统。v1 版本包含每平台 48 个任务，以及 12 个跨平台工作流，每个工作流配对一台桌面设备与一部 Android 手机。该基准以版本化波次发布，每波 300 个任务，并提供可重现的初始化设置。它针对现有基准测试通常隔离 Web、移动或桌面环境的局限，评估代理在长期跨平台工作流中的表现。

rss · Hugging Face Daily Papers · 11月28日 05:07

**「为什么重要」** 现有基准测试通常将 Web、移动或桌面环境隔离，无法验证单一通用代理能否执行跨操作系统且依赖持久应用状态的长期工作流。OS-Omni 填补了这一空白，为评估跨平台计算机使用与编码代理能力提供了可重现的实践资源。

**「可关注」** 可关注：v1 的跨平台工作流仅覆盖桌面与 Android 手机配对，iOS 与 Web 的跨平台组合尚未在首波发布中体现。

**标签**: `#eval`, `#coding-agent`

---

<a id="item-agent-engineer-3"></a>
### [HF 论文：编码智能体视觉推理更强](https://huggingface.co/papers/2611.34813) ⭐️ 7.0/10

2026 年 11 月 28 日，Hugging Face Daily Papers 发布论文摘要，该研究在完全一致的输入、输出规范与评测器条件下，对比编码智能体与原生视频生成模型的视觉推理能力，结果是编写代码渲染答案视频的编码智能体表现优于视频生成模型，同时研究推出新视觉推理评测基准 VBVR-Pro-Bench。当前摘要内容截断，未披露具体性能数据与完整技术细节，且为二手论文摘要，非原始研究全文。

rss · Hugging Face Daily Papers · 11月28日 05:07

**「为什么重要」** 该研究首次在统一测试条件下验证了编码智能体在视觉推理任务上的潜力，为视觉推理技术路线选择提供了新的对比参考；但摘要未披露完整实验细节与具体性能数据，核心结论尚未经原始研究全文证实。

**「可关注」** 可关注：编码智能体通过编写程序渲染答案视频完成视觉推理的范式，以及新基准 VBVR-Pro-Bench 的评测维度设计。

**标签**: `#eval`, `#coding-agent`

---

<a id="item-agent-engineer-4"></a>
### [HF 每日论文：AI agent 数据库错误归因](https://huggingface.co/papers/2611.30483) ⭐️ 7.0/10

2026 年 11 月 28 日 HF 每日论文收录一项预注册实证研究，聚焦 AI agent 操作生产数据库出错后的损害归因问题，研究模型能力、前置防护层、数据库引擎三者对损害的影响权重，该论文当前获 HF 每日论文 4 次点赞。实验分两层：Layer A 无模型参与，通过脚本施加 22 个典型错误，测试 4 种关系型引擎在 5 种权限配置、2 种恢复配置下的损害情况，共覆盖 792 个测试单元、874 次恢复演练（含 10 分钟重复测试）；Layer B 使用 6 个开源小模型（4B 至 12B 参数，加 1 个 35B 混合专家模型）驱动最小工具调用 agent 开展测试，但当前公开摘要截断，未披露 Layer B 的具体设计与研究结果。该研究直接影响数据库交互类 agent 的权限设计、安全防护与评估框架构建。

rss · Hugging Face Daily Papers · 11月28日 05:07

**「为什么重要」** 该研究针对 AI agent 操作生产数据库的高优先级安全风险，其实验设计覆盖的模型选择、前置防护层、数据库引擎、权限与恢复配置等变量，与数据库交互类 agent 的工具链、权限设计和安全评估高度相关，是当前少有的针对该场景的预注册实证研究。

**「可关注」** 可关注：该研究将无模型脚本错误测试与模型驱动 agent 测试分层设计，后续披露的 Layer B 结果可对比模型能力与防护层、引擎配置对损害的实际影响权重。

**标签**: `#eval`, `#permissions`, `#coding-agent`

---

<a id="item-agent-engineer-5"></a>
### [Gated DeltaNet-2 长上下文训练稳定性修复](https://huggingface.co/papers/2611.34051) ⭐️ 6.0/10

2026 年 11 月 28 日，Hugging Face Daily Papers 收录论文《Stable Gated DeltaNet-2: Understanding and Mitigating Recurrent State Instability》，提出针对 Gated DeltaNet-2 线性注意力架构长上下文训练不稳定性的根因修复方案。该工作定位到擦除过程中读取与修改方向的不对称性产生非正规擦除算子，其方向增益跨 token 累积，导致即使无新写入也会触发指数状态增长。修复方案采用对称擦除确保状态传播非扩展，并引入衰减调节残差写入保持写入灵活性，附带理论保证。论文内容截断，缺失方法全称、完整证明、性能基准及生产就绪细节。

rss · Hugging Face Daily Papers · 11月28日 05:07

**「为什么重要」** 稳定的循环状态模型与长上下文 agent 记忆相关，但该论文目前仅提供理论分析，缺少实证基准与工程落地细节，对大多数 agent 工程工作流的直接影响有限。

**「可关注」** 可关注：线性注意力模型的循环状态稳定性问题可能源于擦除算子的非正规性，对称擦除设计或可借鉴。

**标签**: `#memory`

---

## AI 羊毛
{: #sec-ai-deals .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-deals" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-deals-1"></a>
### [NodeWarden 支持离线云备份功能](https://www.appinn.com/nodewarden-update-1/) ⭐️ 7.0/10

你看到的内容可能由第三方 AI 基于小众软件文章提炼总结而成，可能与原文真实意图存在偏差。不代表小众软件观点和立场。请&lt;a href=&quot;https://www.appinn.com/nodewarden-update-1/&quot; target=&quot;\_blank&quot;&gt;点击链接阅读原文&lt;/a&gt;细致比对和校验。&lt;br /&gt;&lt;br /&gt;开源密码管理器 NodeWarden 可直接部署于 Cloudflare Workers，依托 Cloudflare 免费额度即可零成本自建兼容 Bitwarden 的私人密码库，本次更新新增离线使用、自动云备份、多用户管理、密码安全检测、免费 TOTP 等功能，升级时需保留原有 JWT\_SECRET 与数据库、附件存储、Durable Objects 绑定，升级前需完成完整备份，官方提供 DEMO 可直接体验。

rss · 小众软件 · 11月27日 09:13

**「为什么重要」** 自托管密码库无需维护服务器，新增离线使用能力可无网络查看密码，免费提供 Bitwarden 官方付费的 TOTP 功能，适合有零成本自建密码库需求的用户。

**「可关注」** 可关注：若为今年 2 月部署的老版本，升级前需确认 Cloudflare 的 NODE\_VERSION 为 24.22.1，禁止重新生成原有 JWT\_SECRET，且必须保留原有数据库与存储绑定。

**标签**: `#free-tier`, `#limited-free`, `#promo`

---

<a id="item-ai-deals-2"></a>
### [SonoJS Mock 免费前端 Mock 工具发布](https://api.sonojs.com/) ⭐️ 7.0/10

Hacker News 用户 winbetacom 分享了 SonoJS Mock 这套面向前端开发者的免费工具套件，提供 JSONPlaceholder 风格的 Mock REST API、支持 GET/POST/PATCH/DELETE 的临时一次性 REST 端点、真实感 JSON 假数据生成、占位图片生成、JSON 格式化/对比/搜索/转换工作台功能，使用临时 API 无需注册账号。

rss · HN Free API / Credits · 11月27日 23:36

**「为什么重要」** 前端开发者无需搭建后端服务即可快速生成接口与测试数据，降低原型开发与界面联调成本。

**「可关注」** 可关注：临时 API 无需注册即可创建，支持 GET、POST、PATCH、DELETE 四种请求方法，用完即弃。

**标签**: `#free-tier`, `#api`, `#developer-tool`, `#mock-api`

---

<a id="item-ai-deals-3"></a>
### [Show HN 免费数学科普有声书+电子书](https://labs.opentangle.com/after-proof/) ⭐️ 7.0/10

zzzmarcus 在 Show HN 分享了一部约 8 小时的免费数学科普有声书与电子书，内容覆盖近数月数学新发现、相关推导解释及人文故事与历史背景，制作过程中用 Claude 做研究、Gemini Neon 撰写文本、ChatGPT 生成配图与旁白，目前通过给定链接可获取，未标注收费、地区限制与截止时间。

rss · HN Free API / Credits · 11月27日 19:44

**「为什么重要」** 该书电子版附完整脚注与参考文献，内容更新至发布当日，且无标注获取门槛，适合想低成本了解近期数学进展的读者。

**「可关注」** 可关注：该书为多模型协作产出的长内容样本，可作为评估 Gemini Neon 长文写作能力的参考。

**标签**: `#limited-free`

---