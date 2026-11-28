---
layout: default
title: "Horizon Summary: 2026-11-28 (EN)"
date: 2026-11-28
lang: en
---

> From 190 items, 10 important content pieces were selected

---

**Agent Harness Architecture**
1. [pydantic-ai v2.77.0 发布](#item-harness-arch-1) ⭐️ 7.8/10
2. [MCP servers v2.6.0 安全发布](#item-harness-arch-2) ⭐️ 7.8/10

**AI Agent Engineer**
1. [DeepCrossAttention 层间注意力提速 3x](#item-agent-engineer-1) ⭐️ 7.0/10
2. [OS-Omni 跨平台 Agent 基准 v1 发布](#item-agent-engineer-2) ⭐️ 7.0/10
3. [HF论文：编码智能体视觉推理更强](#item-agent-engineer-3) ⭐️ 7.0/10
4. [HF 每日论文：AI 代理数据库错误归因](#item-agent-engineer-4) ⭐️ 7.0/10
5. [Gated DeltaNet-2 长上下文训练稳定性修复](#item-agent-engineer-5) ⭐️ 6.0/10

**AI Deals**
1. [NodeWarden 免费密码库更新](#item-ai-deals-1) ⭐️ 7.0/10
2. [SonoJS Mock 免费前端工具](#item-ai-deals-2) ⭐️ 7.0/10
3. [Show HN 免费数学发现有声书上线](#item-ai-deals-3) ⭐️ 7.0/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [pydantic-ai v2.77.0 发布](https://github.com/pydantic/pydantic-ai/releases/tag/v2.77.0) ⭐️ 7.8/10

pydantic-ai v2.77.0 发布，新增 SQLite、Postgres、MongoDB 三种 ConversationStore 后端，Pax 会话存储重命名为 SqliteSessionStore（旧名称 SqliteConversationStore 触发 HarnessDeprecationWarning）。Skills\(...\) 默认跳过缺失或不可读路径并给出警告，可通过 missing\_directories=&\#x27;error&\#x27; 恢复报错。新增 compact\_history 钩子、CompactionStartEvent/CompactionEndEvent 流式事件，以及 thinking\_summary 跨 provider 摘要能力。SubAgents 权限模型调整，低于 operator 权限的磁盘子代理定义文件会被跳过。

github · dsfaccini · Nov 27, 23:32

**「设计要点」** Harness 采用可插拔 ConversationStore 抽象层，支持 SQLite/Postgres/MongoDB 后端。技能目录通过 SkipReason 枚举实现类型安全的降级处理；SubAgents 基于 authority 模型控制磁盘访问，working\_directory 委托继承父级最低权限。

**「改了什么」** 新增 SQLite/Postgres/MongoDB 三种 ConversationStore 后端，Pax 会话存储重命名为 SqliteSessionStore。Skills\(...\) 默认跳过缺失或不可读路径，stream\_response\(\) 提前结束时标记 state=&\#x27;incomplete&\#x27;，回退子代理请求计入 UsageLimits。Memory 和 Planning 启动上下文通过 enqueue\(placement=&\#x27;before\_prompt&\#x27;\) 移至用户提示之前，SubAgents 拒绝加载低于 operator 权限的磁盘定义文件。

**Tags**: `#memory`, `#tools`, `#compatibility`

---

<a id="item-harness-arch-2"></a>
### [MCP servers v2.6.0 安全发布](https://github.com/modelcontextprotocol/servers/releases/tag/v2.6.0) ⭐️ 7.8/10

modelcontextprotocol/servers v2.6.0 patches eight security vulnerabilities across git, memory, fetch, and filesystem servers. The git server fix prevents arbitrary code execution by blocking Git LFS from running programs named in repository configuration. Teams must upgrade mcp-server-git to 2026.11.27, @modelcontextprotocol/server-memory to 2.2.2, mcp-server-fetch to 2026.11.27, and @modelcontextprotocol/server-filesystem to 2.4.1 on Windows. Date-versioned npm packages require explicit version specification during upgrade.

github · cliffhall · Nov 27, 09:51

**「设计要点」** The git server records repository Git directories at startup and after write operations to enforce boundary checks, and runs Git in a private object directory to block alternates file reads. The memory server creates temporary files through exclusive handles to prevent symlink-based permission changes, while the filesystem server on Windows validates directory paths before and after reads to detect junction swaps.

**「改了什么」** mcp-server-git 2026.11.27 hardens repository isolation, blocks Git LFS program execution, redacts credentials, literalizes paths, and checks boundaries after writes. @modelcontextprotocol/server-memory 2.2.2, mcp-server-fetch 2026.11.27, and @modelcontextprotocol/server-filesystem 2.4.1 fix symlink attacks, robots.txt bypasses, and Windows directory swaps respectively.

**Tags**: `#mcp`, `#tools`, `#sandbox`, `#memory`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [DeepCrossAttention 层间注意力提速 3x](https://research.google/blog/supercharging-transformer-residual-connections/) ⭐️ 7.0/10

Google Research 发布 DeepCrossAttention \(DCA\)，一种 transformer 架构修改。DCA 在层深度维度执行 cross-attention，而非标准 token 间注意力。官方博客称该机制保持模型质量相当，同时实现最高 3 倍推理加速，并改善历史上下文访问。HN 用户 amluto 解释其原理为每个 token 查询所有先前层嵌入的动态加权混合，绕过扩展标准注意力的计算开销。该技术可能影响 AI agent 推理延迟与长程记忆，但目前仅见博客单方声明，无独立验证数据。

hackernews · ComputedCamp995 · Nov 27, 23:06 · [Discussion](https://news.ycombinator.com/item?id=50672565)

**「为什么重要」** Google Research 发布 DCA 博客并引发 HN 讨论，该技术声称通过层间注意力实现 3 倍推理加速。对 AI agent 工程师而言，这属于 transformer 效率优化的新线索，但 3 倍加速与质量相当的说法尚未见独立验证，实际 agent 收益仍不确定。

**「可关注」** 可关注：DCA 将注意力从 token 维度转向层深度维度，通过查询全深度历史嵌入绕过标准注意力的计算扩展，该机制若成立可降低长上下文推理成本。

**「评论」** HN 讨论中，用户 spankalee 猜测 Gemini Neon 的高性价比可能源于类似优化；amluto 认为层间注意力或可解决 LLM 字符计数难题；pollorollo 批评博客图表误用折线图；ipunchghosts 以 Densenet anyone? 联想到密集连接思路。

**Tags**: `#memory`, `#transformer-architecture`, `#inference-optimization`, `#long-context-reasoning`

---

<a id="item-agent-engineer-2"></a>
### [OS-Omni 跨平台 Agent 基准 v1 发布](https://huggingface.co/papers/2611.34232) ⭐️ 7.0/10

Hugging Face Daily Papers 于 2026-11-28 发布 OS-Omni 基准论文。OS-Omni 是首个覆盖六类操作系统的通用计算机使用 Agent 跨平台实时评测环境，包含 Windows、Ubuntu、macOS、iOS、Android 和 Web。v1 版本每平台含 48 个任务，共 12 条跨平台工作流，均采用桌面端配 Android 手机的形式。后续以每波 300 个任务的形式迭代，并提供可复现的初始化设置。

rss · Hugging Face Daily Papers · Nov 28, 05:07

**「为什么重要」** 现有 Agent 评测多局限于单一环境，无法验证同一 Agent 在跨操作系统长流程中的稳定性。OS-Omni 填补了跨平台通用 Agent 的系统化评测空白，为工程师提供了可复现的对照基准。

**「可关注」** v1 仅覆盖桌面与 Android 手机的跨平台配对，且采用版本化分批发布，说明该领域评测仍处早期，当前结果不宜直接外推至全场景跨平台能力。

**Tags**: `#eval`, `#coding-agent`

---

<a id="item-agent-engineer-3"></a>
### [HF论文：编码智能体视觉推理更强](https://huggingface.co/papers/2611.34813) ⭐️ 7.0/10

2026年11月28日Hugging Face Daily Papers发布论文摘要，该研究在完全一致的输入、输出规范与评测器条件下，对比编码智能体与视频生成模型的视觉推理能力：编码智能体通过编写代码渲染答案视频，表现优于原生视频生成模型；研究同时推出新的视觉推理评测基准VBVR-Pro-Bench。当前摘要内容截断，未披露具体性能数据与完整技术细节，为二手摘要非原始研究全文。

rss · Hugging Face Daily Papers · Nov 28, 05:07

**「为什么重要」** 该研究首次在统一测试条件下对比了“原生视觉推理”与“代码符号推理”两条路径的效果，对编码智能体能力边界拓展、视觉推理评测体系设计有参考价值；但目前仅能获取二手摘要，未验证原始研究的实验细节与结论可靠性。

**「可关注」** 可关注VBVR-Pro-Bench的评测设计，以及编码智能体通过代码生成替代像素生成完成视觉推理任务的路径可行性。

**Tags**: `#eval`, `#coding-agent`

---

<a id="item-agent-engineer-4"></a>
### [HF 每日论文：AI 代理数据库错误归因](https://huggingface.co/papers/2611.30483) ⭐️ 7.0/10

2026年11月28日Hugging Face每日论文发布一项预注册实证研究，聚焦AI代理操作生产数据库出错时的损害归因问题，核心对比模型能力、数据库前置防护层、数据库引擎三者对损害的影响权重。研究分两层实验设计：Layer A通过脚本向4种关系型数据库引擎施加22个典型错误，覆盖5种权限配置、2种恢复配置，共完成792个实验单元、874次恢复演练（含10分钟重复测试）；Layer B使用6个4B至12B参数的开源工具调用模型，以及1个35B参数混合专家模型驱动最小代理执行错误操作。当前公开的材料为截断版本，未披露研究结果与最终结论，该研究主要面向开发数据库交互类AI代理、设计相关权限与评估框架的工程师群体。

rss · Hugging Face Daily Papers · Nov 28, 05:07

**「为什么重要」** 该研究直接针对AI代理操作生产数据库的高优先级安全问题，实验设计覆盖了代理工具链、权限配置、评估设计的关键变量，对相关工程实践有参考价值；但目前公开材料为截断版本，尚未披露具体结论，暂无法确认其对实际落地的直接影响。

**「可关注」** 可关注：后续公开的研究结果中，模型、前置防护层、数据库引擎三者的损害贡献度排序，以及不同权限、恢复配置下的实际防护效果差异。

**Tags**: `#eval`, `#permissions`, `#coding-agent`

---

<a id="item-agent-engineer-5"></a>
### [Gated DeltaNet-2 长上下文训练稳定性修复](https://huggingface.co/papers/2611.34051) ⭐️ 6.0/10

Hugging Face Daily Papers 2026-11-28 收录 Gated DeltaNet-2 稳定性修复论文。该论文定位 GDN-2 长上下文训练失败根因。擦除操作读写方向不对称产生非正规算子，方向增益跨 token 累积引发状态指数增长。修复采用对称擦除确保状态传播非扩张。配合衰减调节残差写入保留灵活性，附带理论证明。论文未公开完整证明、性能基准及生产就绪细节。

rss · Hugging Face Daily Papers · Nov 28, 05:07

**「为什么重要」** 线性注意力固定大小循环状态是长上下文 agent 记忆的候选方案。GDN-2 此次提出的对称擦除与衰减写入机制，为同类架构的状态稳定性提供了可验证的理论修复路径。但论文缺少性能基准与生产就绪评估，实际工程可用性尚未证实。

**「可关注」** 可关注：非正规擦除算子导致状态指数增长的根因，可对照现有线性注意力实现检查擦除方向对称性；对称擦除与衰减调节残差写入的修复方案目前仅具理论证明，尚无公开基准验证。

**Tags**: `#memory`

---

## AI Deals

<a id="item-ai-deals-1"></a>
### [NodeWarden 免费密码库更新](https://www.appinn.com/nodewarden-update-1/) ⭐️ 7.0/10

你看到的内容可能由第三方 AI 基于小众软件文章提炼总结而成，可能与原文真实意图存在偏差。不代表小众软件观点和立场。请&lt;a href=&quot;https://www.appinn.com/nodewarden-update-1/&quot; target=&quot;\_blank&quot;&gt;点击链接阅读原文&lt;/a&gt;细致比对和校验。&lt;br /&gt;&lt;br /&gt;NodeWarden 是开源 Bitwarden 兼容密码管理器，可直接部署在 Cloudflare Workers 上，依托 Cloudflare 免费额度即可零成本自托管私人密码库。本次更新新增离线使用、自动云备份、多用户管理、密码安全检测等功能，兼容 Bitwarden 全平台客户端，还免费提供原 Bitwarden 付费的 TOTP 动态验证码功能，无明确失效时间，仅需自行部署且受 Cloudflare 免费额度限制。

rss · 小众软件 · Nov 27, 09:13

**「为什么重要」** 自托管模式可让用户完全掌控密码数据，新增的离线使用、自动云备份解决了自建密码库的核心痛点，且无需承担服务器成本，适合有私有密码管理需求的用户。

**「可关注」** 可关注：升级前必须完整备份，保留原有 JWT\_SECRET、数据库及 Durable Objects 绑定，老版本需检查 Cloudflare 的 NODE\_VERSION 是否为 Node.js 24.22.1。

**Tags**: `#free-tier`, `#limited-free`, `#promo`

---

<a id="item-ai-deals-2"></a>
### [SonoJS Mock 免费前端工具](https://api.sonojs.com/) ⭐️ 7.0/10

Hacker News 用户 winbetacom 在 Show HN 分享了面向前端开发者的免费工具套件 SonoJS Mock。该工具提供 JSONPlaceholder 风格的 Mock REST API 资源、支持 GET/POST/PATCH/DELETE 的临时一次性 REST 端点、真实感 JSON 假数据生成、占位图片生成、JSON 格式化/对比/搜索/转换工作台功能，所有临时 API 无需账号即可使用。

rss · HN Free API / Credits · Nov 27, 23:36

**「为什么重要」** 前端开发者在原型开发、接口联调阶段无需注册账号即可快速获取 Mock 接口与测试数据，可降低开发门槛、提升迭代效率。

**「可关注」** 可关注：临时 API 支持 GET、POST、PATCH、DELETE 四种请求方法，无需账号即可创建 disposable 端点。

**Tags**: `#free-tier`, `#api`, `#developer-tool`, `#mock-api`

---

<a id="item-ai-deals-3"></a>
### [Show HN 免费数学发现有声书上线](https://labs.opentangle.com/after-proof/) ⭐️ 7.0/10

用户zzzmarcus发布Show HN帖子，分享由Claude负责研究、Gemini Neon负责写作、ChatGPT负责配图与旁白制作的约8小时有声书及配套电子书，内容覆盖近期数学发现、相关数学解释与领域发展的人类故事与历史背景；电子书包含完整脚注与参考文献，内容更新至2026年11月27日，帖子称可免费通过给定链接获取，未提及访问限制、有效期或地区限制。

rss · HN Free API / Credits · Nov 27, 19:44

**「为什么重要」** 近期数学领域进展密集，该资源将专业学术发现转化为大众可消费的音频与文本内容，配套的脚注与参考文献也便于读者追溯原始研究来源，对想快速了解领域动态的开发者或爱好者有参考价值。

**「可关注」** 可关注：多模型协作产出垂直领域科普内容的路径已跑通，Gemini Neon的写作质量在该场景下接近人类优秀水平，但内容未经专业数学领域审校，引用时需自行核验。

**Tags**: `#limited-free`

---