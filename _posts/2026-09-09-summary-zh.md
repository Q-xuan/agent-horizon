---
layout: default
title: "Horizon Summary: 2026-09-09 (ZH)"
date: 2026-09-09
lang: zh
---

> 从 211 条内容中筛选出 23 条重要资讯。

---

**Harness 架构**
1. [Claude Code v2.1.265 发布](#item-harness-arch-1) ⭐️ 7.8/10
2. [openai-agents-python v0.22.1 发布](#item-harness-arch-2) ⭐️ 7.8/10
3. [openai-agents-js v0.17.1 发布](#item-harness-arch-3) ⭐️ 6.8/10
4. [Goose v1.50.0 发布](#item-harness-arch-4) ⭐️ 5.8/10
5. [pydantic-ai v2.41.0 发布](#item-harness-arch-5) ⭐️ 5.8/10
6. [gemini-cli v0.60.0-preview.0 发布](#item-harness-arch-6) ⭐️ 5.8/10
7. [Gemini CLI v0.59.0 发布](#item-harness-arch-7) ⭐️ 5.8/10
8. [EveryInc compound-engineering-plugin trending](#item-harness-arch-8) ⭐️ 5.0/10

**Agent 工程师日报**
1. [HF 博客：话题级安全拒绝不足](#item-agent-engineer-1) ⭐️ 7.8/10
2. [FlowBalance：基于验证器的自改进](#item-agent-engineer-2) ⭐️ 7.0/10
3. [OpenAI 声称解决 Navier-Stokes 千年大奖问题](#item-agent-engineer-3) ⭐️ 6.0/10
4. [ChatGPT Images 2.5 发布](#item-agent-engineer-4) ⭐️ 6.0/10
5. [EmbodiedSkills VLA 代理统一框架](#item-agent-engineer-5) ⭐️ 6.0/10
6. [AlphaGenome Atlas 发布](#item-agent-engineer-6) ⭐️ 5.8/10

**AI 日报**
1. [OpenAI Navier-Stokes 解法发布](#item-ai-daily-1) ⭐️ 9.8/10
2. [GPT-5.6 Sol 助力量子计算实验](#item-ai-daily-2) ⭐️ 8.3/10
3. [OpenAI 开放 500 万美元研究资助](#item-ai-daily-3) ⭐️ 7.8/10
4. [Claude Platform 成本优化指南](#item-ai-daily-4) ⭐️ 7.8/10
5. [1Password Codex 工程生产力提升 21%](#item-ai-daily-5) ⭐️ 6.8/10
6. [OpenAI 《The Work Now Within Reach》 发布](#item-ai-daily-6) ⭐️ 5.8/10

**AI 羊毛**
1. [Posterlet 免费无限 AI 海报生成器](#item-ai-deals-1) ⭐️ 7.0/10
2. [AI 商业计划生成器 免费试用](#item-ai-deals-2) ⭐️ 5.0/10
3. [unfetch AI 插件 免费](#item-ai-deals-3) ⭐️ 5.0/10

---

## Harness 架构

<a id="item-harness-arch-1"></a>
### [Claude Code v2.1.265 发布](https://github.com/anthropics/claude-code/releases/tag/v2.1.265) ⭐️ 7.8/10

Claude Code v2.1.265 发布。新增遥测增强，包括 user.email 和 user.groups 到 Claude Desktop 和 Cowork 会话。支持 --plugin-dir 参数指向插件文件夹，实现子文件夹动态加载。添加 1GB 工具结果保存上限，并修复子代理提示缓存重用和进程恢复等问题。

github · ashwin-ant · 9月8日 20:37

**「改了什么」** v2.1.265 发布后，新增动态插件加载支持和 1GB 工具结果保存上限。修复了子代理提示缓存重用和进程恢复等多个运行时问题。

**标签**: `#runtime`, `#subagents`, `#prefix-cache`, `#tools`, `#memory`

---

<a id="item-harness-arch-2"></a>
### [openai-agents-python v0.22.1 发布](https://github.com/openai/openai-agents-python/releases/tag/v0.22.1) ⭐️ 7.8/10

openai-agents-python v0.22.1 发布了沙箱环境隔离、MCP 服务器级守卫、网页搜索工具图像支持等新特性。该版本新增了 configurable Unix-local 沙箱隔离、MCP 工具服务器级守卫、图像结果支持以及语音流式转录选项的暴露。多个 fix PR 修复了核心、会话、沙箱和语音处理中的 bug。

github · seratch · 9月8日 09:18

**「改了什么」** 相比上一版，v0.22.1 新增了网页搜索工具图像结果的支持、MCP 工具服务器级守卫、Unix-local 沙箱环境隔离配置以及语音流式转录选项的暴露。

**标签**: `#sandbox`, `#mcp`, `#tools`, `#runtime`, `#guardrails`

---

<a id="item-harness-arch-3"></a>
### [openai-agents-js v0.17.1 发布](https://github.com/openai/openai-agents-js/releases/tag/v0.17.1) ⭐️ 6.8/10

OpenAI 发布了 openai-agents-js v0.17.1。新增服务器范围 MCP 工具 guardrails、自定义输出 guardrails、Docker 容器标签支持以及 Web 搜索工具图像结果支持。修复了类型契约、批准恢复、会话写入和聊天补全回放等问题。

github · seratch · 9月8日 10:04

**「改了什么」** 相比 v0.17.0，新增了服务器范围 MCP 工具 guardrails 和 Docker 容器标签支持，修复了类型契约、会话写入和聊天补全回放等问题。

**标签**: `#mcp`, `#sandbox`, `#tools`, `#runtime`, `#guardrails`

---

<a id="item-harness-arch-4"></a>
### [Goose v1.50.0 发布](https://github.com/aaif-goose/goose/releases/tag/v1.50.0) ⭐️ 5.8/10

Goose v1.50.0 发布了工具调用增强和子代理平台强制执行。支持 GPT-6 Astra 模型、工具调用以及 Kotlin 调用器配置 Databricks AI Gateway 路径。修复了 Snowflake 连接 HTTPS 要求、子代理守卫、权限撤销等问题。

github · github-actions\[bot\] · 9月8日 19:32

**「设计要点」** 运行时强制子代理平台守卫。保留权限撤销状态。

**「改了什么」** 新增工具调用支持和 GPT-6 模型集成。强制执行子代理平台守卫并保留权限撤销。

**标签**: `#subagents`, `#permissions`, `#tools`, `#runtime`

---

<a id="item-harness-arch-5"></a>
### [pydantic-ai v2.41.0 发布](https://github.com/pydantic/pydantic-ai/releases/tag/v2.41.0) ⭐️ 5.8/10

pydantic-ai v2.41.0 发布。新增 ImageGenerator 直接图像生成 API 和 openai-codex 提供程序支持。弃用 fallback\_model，转为 fallback\_subagent\_model。修复 Anthropic 原生搜索报告、Bedrock 错误包装和 Gemini thinking levels 处理。

github · dsfaccini · 9月8日 04:15

**「改了什么」** pydantic-ai v2.41.0 引入 ImageGenerator 直接图像生成 API 和 openai-codex 提供程序。弃用 fallback\_model 并添加 fallback\_subagent\_model。修复 Anthropic 原生 web searches 报告、BedrockConverseModel 错误包装和 Gemini thinking levels 快照。

**标签**: `#subagents`, `#tools`, `#runtime`

---

<a id="item-harness-arch-6"></a>
### [gemini-cli v0.60.0-preview.0 发布](https://github.com/google-gemini/gemini-cli/releases/tag/v0.60.0-preview.0) ⭐️ 5.8/10

gemini-cli v0.60.0-preview.0 发布。针对沙盒隔离、MCP OAuth RFC enforcement、扩展加载器边界校验和 Web Fetch 路由进行修复。版本从 0.59.0-preview.0 提升至 0.60.0-preview.0。多项安全和权限检查增强。

github · gemini-cli-robot · 9月8日 21:04

**「改了什么」** 相对 v0.59.0-preview.0，修复 macOS Seatbelt 沙盒临时目录隔离、MCP OAuth issuer 识别、扩展路径解析边界和核心 Web Fetch 连接路由。版本号提升并包含多项安全增强。

**标签**: `#sandbox`, `#mcp`, `#extensions`, `#cli`, `#fix`

---

<a id="item-harness-arch-7"></a>
### [Gemini CLI v0.59.0 发布](https://github.com/google-gemini/gemini-cli/releases/tag/v0.59.0) ⭐️ 5.8/10

Gemini CLI v0.59.0 发布。修复了 MCP OAuth 元数据发现和认证中的 SSRF 漏洞。强制执行受限模式下的工作区信任检查并过滤 mcpServers。

github · gemini-cli-robot · 9月8日 21:13

**「改了什么」** 修复了 MCP OAuth 元数据发现和认证中的 SSRF 漏洞。强制执行 fail-closed 工作区信任检查并过滤受限模式下的 mcpServers。

**标签**: `#mcp`, `#sandbox`, `#permissions`

---

<a id="item-harness-arch-8"></a>
### [EveryInc compound-engineering-plugin trending](https://github.com/EveryInc/compound-engineering-plugin) ⭐️ 5.0/10

GitHub trending repo EveryInc/compound-engineering-plugin 是一个 Compound Engineering 插件，为 AI coding agents 提供 33 种技能。该插件采用 brainstorm、plan、build、review、capture 的循环结构组织工作，确保知识从每次变更中被写入，以便下次变更读取。插件运行在 14 个 agent hosts 上，支持 Claude Code、Codex、Cursor 等。

rss · GitHub Trending Daily · 9月8日 23:28

**「设计要点」** 插件使用 loop-based 结构将 brainstorm、plan、build、review、capture 步骤串联，确保知识从变更中被写入内存供下次使用。运行时支持多个 agent hosts，包括 Claude Code、Codex 和 Cursor。

**标签**: `#runtime`, `#planning`, `#memory`, `#tools`

---

## Agent 工程师日报

<a id="item-agent-engineer-1"></a>
### [HF 博客：话题级安全拒绝不足](https://huggingface.co/blog/MultiverseComputingCAI/safety-for-whom) ⭐️ 7.8/10

Hugging Face 博客和论文指出，话题级安全拒绝在真实部署中不足，例如公民导师和公共助理在政治话题上需要不同边界。提出边界感知自蒸馏方法，通过政治说服测试训练模型仅拒绝有害子集。标准自生成安全调优存在覆盖差距和过度拒绝问题，需同时评估边界两侧以平衡。

rss · Hugging Face Blog · 9月8日 14:23

**「为什么重要」** 该研究强调在真实部署中需根据上下文定义安全边界，而非广义话题类别。

**「可关注」** 可关注：安全调优不应仅通过有害拒绝率评估，需同时报告边界两侧的拒绝率以避免过度拒绝。

**标签**: `#harness`, `#eval`, `#orchestration`, `#permissions`

---

<a id="item-agent-engineer-2"></a>
### [FlowBalance：基于验证器的自改进](https://huggingface.co/papers/2609.03241) ⭐️ 7.0/10

FlowBalance 是一种基于验证器的自改进方法。它使推理模型能够从自身的策略内经验中自我提升，通过校准 token 级指导分数与稀疏验证器优势在正负轨迹上。对于每个策略内轨迹，使用同一策略的 frozen 训练时视图利用特权上下文产生 token 级 log-probability gains，这些 gains 聚合为轨迹级自指导分数。FlowBalance 用验证器导出的组优势校准此分数：正优势轨迹保留指导，负优势轨迹反转指导。

rss · Hugging Face Daily Papers · 9月8日 00:00

**「为什么重要」** FlowBalance 解决了推理模型内部循环脆弱的问题，使其能从策略内经验自改进。这对 agent harnesses、evals 和 reasoning loops 相关，但具体性能提升尚未证实。

**「可关注」** 可关注：dense same-model guidance 易强化 false confidence 或在窄解模式上过度集中学习，而 FlowBalance 用验证器导出的组优势校准 token 级指导分数。

**标签**: `#harness`, `#eval`, `#coding-agent`, `#orchestration`

---

<a id="item-agent-engineer-3"></a>
### [OpenAI 声称解决 Navier-Stokes 千年大奖问题](https://openai.com/index/navier-stokes-solution/) ⭐️ 6.0/10

OpenAI 官方博客宣布其内部模型已解决 Navier-Stokes 存在与光滑性问题，这是千年大奖问题之一。该模型证明流体运动方程的动力学在有限时间内可产生奇点。模型是最近训练的，较 Astra 在数学能力上提升超过两倍。这对 AI Agent 的推理评估具有参考价值。

hackernews · tedsanders · 9月8日 17:13 · [社区讨论](https://news.ycombinator.com/item?id=49613262)

**「为什么重要」** 这项声明展示了 AI 模型在数学问题上的前沿能力提升，对 AI Agent 的推理评估具有参考意义。

**「可关注」** 可关注：OpenAI 内部模型较 Astra 在数学能力上提升超过两倍，但存在基于他人工作和提示的争议。

**「评论」** HN 评论中，Terence Tao 指出 AI 努力可能抢占研究先机，激励不再分享研究方向。部分用户质疑该解决方案是否基于他人实际工作与提示。

**标签**: `#coding-agent`, `#eval`, `#orchestration`

---

<a id="item-agent-engineer-4"></a>
### [ChatGPT Images 2.5 发布](https://simonwillison.net/2026/Sep/8/introducing-chatgpt-images-25/) ⭐️ 6.0/10

OpenAI 发布了 ChatGPT Images 2.5 模型，提升了多轮指令遵循能力、响应速度，并更好地保留参考照片中的主体。API 新增了 gpt-image-2.5-sunburst 和 gpt-image-2.5-flare 两个模型 ID。Simon Willison 升级了 openai\_image.py 工具，支持传入参考图片。

rss · Simon Willison · 9月8日 22:46

**「为什么重要」** OpenAI 发布了 ChatGPT Images 2.5 模型，API 新增了 gpt-image-2.5-sunburst 和 gpt-image-2.5-flare 两个模型 ID。这些模型在多轮指令遵循、响应速度和主体保留方面有改进。

**「可关注」** Sunburst 适合需要精度的编辑工作流，Flare 适合日常快速高质量图像生成。

**标签**: `#coding-agent`, `#harness`, `#orchestration`, `#image-generation`

---

<a id="item-agent-engineer-5"></a>
### [EmbodiedSkills VLA 代理统一框架](https://huggingface.co/papers/2609.01281) ⭐️ 6.0/10

EmbodiedSkills 框架将 VLA 技能决策视为可执行提案，运行时检查前提条件并验证执行结果，以协调具身代理中的感知、规划和执行。共享的可执行技能接口连接高层次技能选择、有限低层次 VLA 执行和后动作验证。该框架针对长时序任务中的 VLA 模型，强调动作预测本身不足以保证操作有效性或结果验证。

rss · Hugging Face Daily Papers · 9月8日 00:00

**「为什么重要」** 该框架针对 VLA 代理在长时序任务中协调感知规划执行的问题提供统一方法。

**「可关注」** 可关注：将 VLA 技能决策作为执行提案进行运行时验证。

**标签**: `#orchestration`, `#coding-agent`, `#harness`

---

<a id="item-agent-engineer-6"></a>
### [AlphaGenome Atlas 发布](https://deepmind.google/blog/alphagenome-atlas-a-predictive-map-of-every-possible-dna-letter-change-in-the-human-genome/) ⭐️ 5.8/10

Google DeepMind 发布了 AlphaGenome Atlas，这是一个预测人类基因组中每种可能单字母 DNA 变体的分子效应的图谱。AlphaGenome Atlas 映射了人类基因组中 90 亿个单字母 DNA 变体的分子效应。此发布为基因组学研究提供了新的预测工具。

rss · Google DeepMind · 9月8日 14:00

**标签**: `#eval`, `#harness`, `#orchestration`

---

## AI 日报

<a id="item-ai-daily-1"></a>
### [OpenAI Navier-Stokes 解法发布](https://openai.com/index/navier-stokes-solution) ⭐️ 9.8/10

OpenAI 分享了 Navier–Stokes 千年大奖问题的人工智能生成解法。
解法包含详细的写上。
证明使用 Lean 语言形式化。

rss · OpenAI Blog · 9月8日 10:00

**「可关注」** 可关注：AI 生成的 Navier–Stokes 解法包含 Lean 形式化证明。

**标签**: `#lab`, `#model`, `#industry`, `#product`

---

<a id="item-ai-daily-2"></a>
### [GPT-5.6 Sol 助力量子计算实验](https://openai.com/index/codex-quantum-computing-experiments) ⭐️ 8.3/10

MIT 研究者使用 GPT-5.6 Sol 搭配 Codex 自主运行量子计算实验，分析结果并校准量子比特。OpenAI 官方博客介绍了这一过程。

rss · OpenAI Blog · 9月8日 17:00

**「可关注」** 可关注：MIT 研究者使用 GPT-5.6 Sol 搭配 Codex 自主运行量子计算实验。

**标签**: `#model`, `#lab`, `#product`, `#industry`

---

<a id="item-ai-daily-3"></a>
### [OpenAI 开放 500 万美元研究资助](https://openai.com/index/teen-development-research-grants) ⭐️ 7.8/10

OpenAI 开放了 500 万美元的独立研究资助计划。计划支持独立研究生成式 AI 如何影响青少年发展、福祉和安全。申请现在即可。

rss · OpenAI Blog · 9月8日 09:00

**标签**: `#lab`, `#policy`, `#industry`, `#product`

---

<a id="item-ai-daily-4"></a>
### [Claude Platform 成本优化指南](https://claude.com/blog/reducing-cost-and-improving-performance-with-claude-platform) ⭐️ 7.8/10

Claude Platform 通过最大化提示缓存命中率、移除提示反模式和校准模型努力，可在不牺牲性能的情况下降低成本。已更新 claude-api skill，提供 prompt-audit 命令移除反模式，hillclimb 校准努力，cost-optimize 全面优化。示例中，移除反模式后成本降低 14.6% 且准确率提升 5.3%；另一优化使成本降低 73% 且通过率不变。

rss · Claude Blog · 9月8日 00:00

**「为什么重要」** 这些方法实用且直接可应用于现有应用，帮助开发者在 Claude Platform 上控制成本并提升性能。

**「可关注」** 可关注：运行 /claude-api prompt-audit 移除提示中的反模式。

**标签**: `#model`, `#lab`, `#product`, `#industry`

---

<a id="item-ai-daily-5"></a>
### [1Password Codex 工程生产力提升 21%](https://openai.com/index/1password) ⭐️ 6.8/10

1Password 工程师使用 OpenAI Codex 快速构建新功能和内部工具，工程生产力提升 21%。这些工具在生产就绪状态下运行，同时维持严格的安全策略。

rss · OpenAI Blog · 9月8日 00:00

**「为什么重要」** 1Password 的案例显示，Codex 在安全政策约束下能显著提升工程生产力。这为安全敏感团队提供了实际参考。

**「可关注」** 可关注：1Password 工程师使用 Codex 快速构建新功能和内部工具，并在生产就绪状态下维持严格的安全策略。

**标签**: `#openai`, `#codex`, `#1password`, `#productivity`, `#security`

---

<a id="item-ai-daily-6"></a>
### [OpenAI 《The Work Now Within Reach》 发布](https://openai.com/index/the-work-now-within-reach) ⭐️ 5.8/10

OpenAI 博客发布《The Work Now Within Reach》。该帖子探讨更强大、更经济的 AI 如何扩展人们和企业可完成的工作。并使增长更加经济。这是通用探索性陈述，没有具体模型细节或可验证主张。

rss · OpenAI Blog · 9月8日 13:00

**「为什么重要」** OpenAI 的探索性帖子有助于把握 AI 进步对工作扩展和经济增长的影响。在当前 AI 快速发展背景下，了解这些变化具有现实意义。

**「可关注」** 可关注：更强大、更经济的 AI 将扩展人们和企业的可完成工作，并使增长更具经济性。

**标签**: `#openai`, `#ai`, `#industry`, `#blog`, `#future-of-work`

---

## AI 羊毛

<a id="item-ai-deals-1"></a>
### [Posterlet 免费无限 AI 海报生成器](https://posterlet.com/) ⭐️ 7.0/10

Show HN 发布 Posterlet 免费无限 AI 海报生成器。用户可免费无限使用该工具。

rss · HN Free API / Credits · 9月8日 16:16

**标签**: `#promo`, `#free-tier`, `#api`

---

<a id="item-ai-deals-2"></a>
### [AI 商业计划生成器 免费试用](https://news.ycombinator.com/item?id=49610069) ⭐️ 5.0/10

一位开发者分享了免费的 AI 商业计划生成器工具。该工具支持根据资源、想法和利基市场等进行 100% 定制的商业计划评估和开发。用户可通过提供的链接进行一次试用。

rss · HN Free API / Credits · 9月8日 13:27

**「为什么重要」** 该工具免费且支持定制化服务，适合有具体资源、想法和利基市场的用户。

**「可关注」** 可关注：该工具仅限一次试用，适合有具体资源、想法和利基市场的用户。

**标签**: `#free-tier`, `#promo`, `#limited-free`, `#ai-tool`

---

<a id="item-ai-deals-3"></a>
### [unfetch AI 插件 免费](https://unfetch.com/plugin) ⭐️ 5.0/10

unfetch 发布免费 AI 插件，支持 Google Ads、Console 和 Analytics。
该插件无额度限制、模型价格或截止时间。
通过 Show HN 推广。

rss · HN Free API / Credits · 9月8日 11:55

**「为什么重要」** 该插件免费且无截止时间，适合 Google Ads 用户。

**「可关注」** 可关注：免费无额度限制，适用于 Google Ads、Console 和 Analytics 用户。

**标签**: `#free-tier`, `#promo`, `#plugin`, `#google-ads`, `#ai`

---