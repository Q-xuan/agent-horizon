---
layout: default
title: "Horizon Summary: 2026-09-29 (EN)"
date: 2026-09-29
lang: en
---

> From 202 items, 20 important content pieces were selected

---

**Agent Harness Architecture**
1. [MCP TypeScript SDK 1.31.0](#item-harness-arch-1) ⭐️ 8.8/10
2. [modelcontextprotocol/typescript-sdk released @modelcontextprotocol/core@2.2.0](#item-harness-arch-2) ⭐️ 8.3/10
3. [Codex rust-v0.158.0 发布](#item-harness-arch-3) ⭐️ 7.8/10
4. [crewAIInc/crewAI released 1.15.23](#item-harness-arch-4) ⭐️ 6.8/10
5. [2.1.284](#item-harness-arch-5) ⭐️ 6.8/10
6. [LangChain 1.4.3 Patch Release](#item-harness-arch-6) ⭐️ 6.3/10
7. [langchain-ai/langchain released langchain-fireworks==1.7.0](#item-harness-arch-7) ⭐️ 6.3/10

**AI Agent Engineer**
1. [Claude Sonnet 5.5 发布](#item-agent-engineer-1) ⭐️ 8.0/10
2. [分离 Prefill 与 Decode 量化](#item-agent-engineer-2) ⭐️ 8.0/10
3. [Holo4: powering generalist computer-use agents](#item-agent-engineer-3) ⭐️ 6.8/10
4. [llm-anthropic 0.30 发布](#item-agent-engineer-4) ⭐️ 6.3/10
5. [Supporting native Rust in Workers with the new Emscripten target for wasm-bindgen](#item-agent-engineer-5) ⭐️ 6.3/10
6. [Sonnet 5.5 发布，安全回退影响评测](#item-agent-engineer-6) ⭐️ 6.0/10
7. [Cloudflare \`cf\` CLI 发布](#item-agent-engineer-7) ⭐️ 5.5/10
8. [EMem-Bench：具身记忆评测基准](#item-agent-engineer-8) ⭐️ 5.5/10
9. [AdaTutoRank：自适应辅导优化重排](#item-agent-engineer-9) ⭐️ 5.5/10

**AI Daily**
1. [OpenAI 就澳洲政府网站事件道歉](#item-ai-daily-1) ⭐️ 8.8/10
2. [How we found 24 Android vulnerabilities using our open source AI security agent](#item-ai-daily-2) ⭐️ 8.3/10
3. [OpenAI Expands Lenfest Program with Up to $10M Support](#item-ai-daily-3) ⭐️ 6.8/10

**AI Deals**
1. [OpenCode 与 Command Code $10 套餐 DeepSeek 额度升至 $60](#item-ai-deals-1) ⭐️ 8.0/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [MCP TypeScript SDK 1.31.0](https://github.com/modelcontextprotocol/typescript-sdk/releases/tag/1.31.0) ⭐️ 8.8/10

The Model Context Protocol \(MCP\) TypeScript SDK version 1.31.0 introduces issuer binding for stored OAuth credentials. Stored OAuth tokens and client information now include an \`issuer\` field, and storage implementations that reject unknown fields must allow it. Constructing \`ClientCredentialsProvider\`, \`PrivateKeyJwtProvider\`, or \`StaticPrivateKeyJwtProvider\` without \`expectedIssuer\` is deprecated.

github · felixweinberger · Sep 28, 18:52

**「Design Points」** The change tightens OAuth credential storage by binding each token and client record to the authorization server that issued it, reducing the risk of credential replay across issuers. Providers now require an explicit \`expectedIssuer\` parameter to validate the issuer at construction time.

**「What Changed」** Stored OAuth tokens and client information now persist an \`issuer\` field. Auth provider constructors deprecate omission of \`expectedIssuer\`, making issuer validation explicit for \`ClientCredentialsProvider\`, \`PrivateKeyJwtProvider\`, and \`StaticPrivateKeyJwtProvider\`.

**Tags**: `#mcp`, `#permissions`, `#runtime`

---

<a id="item-harness-arch-2"></a>
### [modelcontextprotocol/typescript-sdk released @modelcontextprotocol/core@2.2.0](https://github.com/modelcontextprotocol/typescript-sdk/releases/tag/%40modelcontextprotocol/core%402.2.0) ⭐️ 8.3/10

MCP TypeScript SDK v2.2.0 deprecates OAuth provider construction without expectedIssuer and adds AuthorizationServerMismatchError validation in fetchToken\(\).

github · github-actions\[bot\] · Sep 28, 19:07

**Tags**: `#mcp`, `#tools`, `#permissions`, `#runtime`

---

<a id="item-harness-arch-3"></a>
### [Codex rust-v0.158.0 发布](https://github.com/openai/codex/releases/tag/rust-v0.158.0) ⭐️ 7.8/10

Codex rust-v0.158.0 ships MCP OAuth client-secret support, bearer-token security for direct exec-server WebSocket connections, and default terminal-input approval for elevated commands. It fixes Windows sandbox failures involving ordinary Windows 10 paths, rejected stored credentials, and large permission policies. Linux sandbox startup with nested writable roots is repaired, and Git metadata protections are preserved across writable roots on Linux and macOS.

github · github-actions\[bot\] · Sep 28, 05:07

**「设计要点」** WebSocket authentication is extracted into a dedicated \`codex-websocket-auth\` crate, and app-server executor connections support bearer tokens. Sandbox fixes reorder read-only metadata mounts for nested writable roots and preserve Git metadata protections across writable roots on Linux and macOS.

**「改了什么」** MCP servers can authenticate with pre-registered OAuth client secrets via \`codex mcp add --oauth-client-secret\`. Direct exec-server WebSocket connections now support bearer tokens, including through app-server, and elevated commands trigger terminal-input approval by default.

**Tags**: `#mcp`, `#permissions`, `#sandbox`, `#runtime`, `#tools`

---

<a id="item-harness-arch-4"></a>
### [crewAIInc/crewAI released 1.15.23](https://github.com/crewAIInc/crewAI/releases/tag/1.15.23) ⭐️ 6.8/10

crewAI 1.15.23 adds native Gemini 3.8 Flash support, improves evaluation tracing and platform integration UX, and includes multiple bug fixes.

github · lorenzejay · Sep 28, 21:14

**Tags**: `#eval`, `#runtime`, `#tools`

---

<a id="item-harness-arch-5"></a>
### [2.1.284](https://code.claude.com/docs/en/changelog#2-1-284) ⭐️ 6.8/10

Claude Code 2.1.284 adds Sonnet 5.5 as the default model, refines auto-mode read permissions with a &\#x27;ask again next time&\#x27; option, and introduces spend-limit display and effort-slider keybindings.

rss · Claude Code Changelog · Sep 28, 18:15

**Tags**: `#permissions`, `#tools`, `#sandbox`

---

<a id="item-harness-arch-6"></a>
### [LangChain 1.4.3 Patch Release](https://github.com/langchain-ai/langchain/releases/tag/langchain%3D%3D1.4.3) ⭐️ 6.3/10

LangChain 1.4.3 is a patch release over 1.4.2. It adds Bedrock Mantle chat model support to \`init\_chat\_model\`, fixes GPT-6 structured output recognition without profiles, repairs invalid tool calls in \`create\_agent\`, and sanitizes cache settings for fallback models. The anyio dependency is bumped to 4.14.2.

github · github-actions\[bot\] · Sep 28, 20:17

**「Design Points」** The changes concentrate in three runtime paths: chat model initialization via \`init\_chat\_model\`, agent tool-call validation inside \`create\_agent\`, and cache-setting propagation for fallback models. No interface or protocol breaks.

**「What Changed」** Bedrock Mantle chat models are now selectable through \`init\_chat\_model\`. GPT-6 structured output no longer requires profiles. \`create\_agent\` rejects invalid tool calls. Fallback models receive sanitized cache settings. anyio moves from 4.11.0 to 4.14.2.

**Tags**: `#runtime`, `#tools`, `#prefix-cache`

---

<a id="item-harness-arch-7"></a>
### [langchain-ai/langchain released langchain-fireworks==1.7.0](https://github.com/langchain-ai/langchain/releases/tag/langchain-fireworks%3D%3D1.7.0) ⭐️ 6.3/10

Minor 1.7.0 release of langchain-fireworks adds a prompt caching middleware and fixes mid-stream timeout classification, with no detailed technical notes.

github · github-actions\[bot\] · Sep 28, 20:46

**Tags**: `#prefix-cache`, `#runtime`, `#eval`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [Claude Sonnet 5.5 发布](https://simonwillison.net/2026/Sep/28/claude-sonnet-5-5/) ⭐️ 8.0/10

Anthropic 发布 Claude Sonnet 5.5，定价与 Sonnet 5 持平，官方称速度提升 30% 以上，多数任务成本最多降低 30%，基准测试全面超越前代。Simon Willison 实测：xhigh 思考档位生成 SVG 耗时 41 秒，花费 5.74 美分；max 档位复现 Opus 5.5 缺陷，思考 128,000 tokens、花费 1.28 美元后耗尽 token 且未输出。该模型已成为 claude.ai 免费层模型，实测可生成 WebGL 三维动画页面，部分编码任务表现接近 Opus 5.5。Haiku 5.5 将在未来数周内推出。

rss · Simon Willison · Sep 28, 22:07

**「为什么重要」** 对 coding agent 与 harness 开发者而言，Sonnet 5.5 在保持价格的同时提升速度并降低成本，直接影响推理预算与延迟设计。但 max 思考档位的 token 耗尽缺陷提示，需设置输出上限与失败重试，否则单次调用可能产生 1.28 美元无结果开销。

**「可关注」** 可关注：Sonnet 5.5 的 xhigh 档位在 41 秒内完成 SVG 生成且成本可控，但 max 档位存在 128,000 tokens 无输出缺陷，生产环境应避免直接使用 max 档位或增加 token 预算熔断。

**Tags**: `#coding-agent`, `#eval`, `#observability`, `#harness`

---

<a id="item-agent-engineer-2"></a>
### [分离 Prefill 与 Decode 量化](https://huggingface.co/papers/2609.26333) ⭐️ 8.0/10

2026-09-29，Hugging Face Daily Papers 收录论文《Disaggregated Quantization: Specializing LLM Prefill and Decode》，提出 disaggregated quantization（DQ），针对 prefill 与 decode 分别特化计算格式、权重与存储位置。在 Qwen 3 和 Gemma 3 上，decode 阶段移除激活量化可在不增加推理成本的前提下提升 decode-heavy 任务精度；训练独立的 compute-native prefill 权重能在 2–3-bit decode 下匹配或超过 weight-only 推理精度，同时加速 prompt 处理。论文释出 Qwen3.8-27B GGUF decoders，并报告 NVFP4 prefiller 将 1-bit 精度提升 32.5 点（原文数据在此处截断），当前获得 44 个 upvotes。

rss · Hugging Face Daily Papers · Sep 29, 02:27

**「为什么重要」** 主流推理常对 prefill 与 decode 使用同一套低比特权重，该论文用实验指出两阶段对量化策略的诉求相反：prefill 受益于低精度计算，decode 受益于紧凑权重以降低显存带宽。对 coding agent 与推理 harness 工程师而言，这直接影响内存占用、吞吐与精度的权衡假设。

**「可关注」** 可关注：若现有推理栈对 prefill 与 decode 强制统一量化格式，可能同时牺牲 prompt 处理速度与生成精度；可评估分阶段特化权重与已释出的 GGUF 解码器在实际负载下的收益。

**Tags**: `#memory`, `#eval`, `#harness`

---

<a id="item-agent-engineer-3"></a>
### [Holo4: powering generalist computer-use agents](https://huggingface.co/blog/Hcompany/holo4) ⭐️ 6.8/10

Hugging Face announces Holo4, a new series of generalist computer-use agent models available in 27B dense and 35B-A3B MoE sizes with open trajectories and an API.

rss · Hugging Face Blog · Sep 28, 09:44

**Tags**: `#coding-agent`, `#mcp`, `#eval`, `#harness`

---

<a id="item-agent-engineer-4"></a>
### [llm-anthropic 0.30 发布](https://github.com/simonw/llm-anthropic/releases/tag/0.30) ⭐️ 6.3/10

simonw/llm-anthropic 0.30 发布，新增 Claude Sonnet 5.5 支持，并加入 \`llm anthropic refresh\`、\`llm anthropic models\`、\`llm anthropic count\` 三个命令。\`refresh\` 从 Anthropic models API 拉取可用模型并缓存到用户目录 \`anthropic\_models.json\`，未收录模型按 API 回报的能力注册，包括图像与 PDF 输入、thinking、effort、结构化输出和最大输出 token。\`count\` 调用 token counting API 统计输入 token 而不运行模型，Python 侧对应 \`model.count\_tokens\(\)\`。同时修复了对话中遭拒后，后续 prompt 因空 content 报 400 错误的问题。

github · simonw · Sep 28, 23:06

**「为什么重要」** 对用 LLM CLI 管理 Anthropic 模型的工程师，模型枚举和 token 预检从查文档变为本地命令，可减少上下文超限的反复试错。目前材料仅展示工具链增量更新，未提供对 agent 架构或生产环境的影响数据。

**「可关注」** 可关注：\`llm anthropic count\` 与 \`model.count\_tokens\(\)\` 能在不触发推理的前提下统计输入 token，适合在 harness 中作为上下文预算的前置校验；\`refresh\` 依赖本地 \`anthropic\_models.json\` 缓存，新模型能力需主动拉取后才会注册。

**Tags**: `#harness`, `#observability`, `#coding-agent`

---

<a id="item-agent-engineer-5"></a>
### [Supporting native Rust in Workers with the new Emscripten target for wasm-bindgen](https://blog.cloudflare.com/rust-workers-emscripten-target/) ⭐️ 6.3/10

Cloudflare announces experimental first-class support for the Emscripten wasm32-unknown-emscripten target in wasm-bindgen, allowing native Rust and Tokio-based applications to run on Workers.

rss · Cloudflare Engineering · Sep 28, 13:00

**Tags**: `#toolchain`, `#rust`, `#wasm`, `#cloudflare-workers`

---

<a id="item-agent-engineer-6"></a>
### [Sonnet 5.5 发布，安全回退影响评测](https://www.anthropic.com/claude-sonnet-5-5) ⭐️ 6.0/10

2026 年 9 月 28 日，Anthropic 发布 Sonnet 5.5，Hacker News 讨论集中在 Terminal-Bench 得分。Sonnet 5.5 取得 70.6 分，高于 Opus 5.5 的 66.4 分。用户 abejora 指出，Opus 5.5 有 10% 的试验因安全护栏回退到其他模型，Sonnet 5.5 仅 1.5%，分差可能主要来自回退率差异。该数据出自 Sonnet 5.5 System Card 第 8.5 节，目前为社区解读，尚无独立基准复现。

hackernews · D2OQZG8l5BI1S06 · Sep 28, 17:58 · [Discussion](https://news.ycombinator.com/item?id=49881850)

**「为什么重要」** 对 coding agent 工程师而言，这提醒在对比模型终端任务基准时，安全回退率会直接扭曲结果。若忽略回退机制，容易把工程约束误读为模型能力差异。

**「可关注」** 可关注：解读 Terminal-Bench 等终端基准时，需同步核查模型的安全回退率与 System Card 中的降级策略，避免将护栏触发误判为能力差距。

**「评论」** 社区对 Sonnet 5.5 的定位和性价比分歧明显：Sol- 认为 Opus 5.5 在 5x 套餐下已够用，难以看到 Sonnet 5.5 的日常场景；azuanrb 和 MisterMunchkin 则强调 GLM、DeepSeek 等中国模型价格优势显著。wongarsu 注意到 Sonnet 5.5 网络安全能力提升后配备了接近 Opus 5.5 的护栏，高风险任务会回退到 Sonnet 5。

**Tags**: `#coding-agent`, `#eval`, `#llm`, `#benchmark`, `#anthropic`

---

<a id="item-agent-engineer-7"></a>
### [Cloudflare \`cf\` CLI 发布](https://blog.cloudflare.com/cloudflare-cf-cli-launch/) ⭐️ 5.5/10

Cloudflare 发布了 agentic CLI \`cf\`，用于操作其 API。当前材料仅包含 HN 社区讨论，未提供官方架构说明、trace 或 eval 数据。评论集中在 TypeScript 选型、token 创建与权限管理的摩擦，以及 CLI 相对直接调用 REST 的必要性。该产品对 agent 工具链的实际影响尚无法从现有材料评估。

hackernews · macleos · Sep 28, 15:28 · [Discussion](https://news.ycombinator.com/item?id=49879577)

**「为什么重要」** Cloudflare 推出 agentic CLI \`cf\` 作为其 API 的操作入口，但 HN 讨论显示，token 权限管理和与 REST 的边界仍是 agent 自动化的实际断点。已发生的是产品发布，未证实的是它是否比现有 REST 方案更适合 agent 工作流。

**「可关注」** 可关注：\`cf\` 与 Cloudflare REST API 的能力边界。有评论者指出 agent 依据 REST 文档已可执行全部操作，若 CLI 是子集，harness 需评估是否值得引入额外抽象；同时 CLI 不负责生成带权限的 token，用户仍需手动在网站查找，且入口经常变动。

**「评论」** HN 评论分歧较大。有评论者质疑 TypeScript 选型，认为应使用编译型语言避免依赖地狱；也有评论者将 agentic CLI 称为“随机词生成器”，质疑其用于生产基础设施配置的安全性。另有开发者表示从未遇到 agent 通过 REST 调用 Cloudflare 的障碍，认为 CLI 价值待验证。共识是 token 管理体验差，网站入口经常变动。

**Tags**: `#coding-agent`, `#harness`, `#permissions`

---

<a id="item-agent-engineer-8"></a>
### [EMem-Bench：具身记忆评测基准](https://huggingface.co/papers/2609.28236) ⭐️ 5.5/10

Hugging Face 每日论文收录 EmbodiedMemory-Bench（EMem-Bench），针对长程具身交互中的记忆能力提出基准。该基准包含 2,554 个交互 episode，覆盖四类任务家族，要求 agent 在观察、行动与遭遇环境变化时持续建立并更新记忆。论文将当前 agent 的记忆缺陷归纳为四点：细粒度视觉记忆弱、动态世界状态跟踪不可靠、未记录交互结果揭示的世界状态、难以从先前经验泛化。目前 RSS 仅提供摘要，尚无代码、实验结果或架构细节，对一般 coding agent 工程师的即时可操作性有限。

rss · Hugging Face Daily Papers · Sep 29, 00:00

**「为什么重要」** 长程具身任务要求 agent 跨时间维持环境状态，而现有基准缺少对记忆能力的直接评估；EMem-Bench 的出现为这一空白提供了可量化的测试面。不过摘要未给出实验数据，其区分度与实用性仍待全文验证。

**「可关注」** 可关注：EMem-Bench 把长程具身记忆拆成细粒度视觉、动态世界状态、交互结果记录与经验泛化四个维度，但摘要未提供代码与实验数据，暂无法评估其基线表现。

**Tags**: `#eval`, `#memory`, `#benchmark`

---

<a id="item-agent-engineer-9"></a>
### [AdaTutoRank：自适应辅导优化重排](https://huggingface.co/papers/2609.32472) ⭐️ 5.5/10

AdaTutoRank 面向 RAG 与深度研究的文档集合重排，提出自适应辅导优化。主流重排器按相关性匹配挑选文档，但复杂信息需求要的是互补、无冗余的集合。先前工作以集合级 rubric 总分作奖励，把目标从排序文档转向组合集合；但该分数是集合内所有文档共享的单一标量，监督稀疏——集合得分高时，冗余文档跟着受奖；集合得分低时，关键文档跟着受罚。信用分配分不清贡献者与搭便车者。该论文 2026-09-29 收录于 Hugging Face Daily Papers，获 7 次 upvote。

rss · Hugging Face Daily Papers · Sep 29, 00:00

**「为什么重要」** 重排器决定哪些证据进入下游模型。集合级奖励若让监督稀疏，重排器就难以区分关键文档与冗余文档，直接影响 RAG 与深度研究的证据质量。

**「可关注」** 可关注：集合级奖励导致文档重排信用分配稀疏，AdaTutoRank 用自适应辅导优化应对；但原文对 on-policy 蒸馏现有方法缺陷的描述在截断处中断，具体改进需查论文全文。

**Tags**: `#rag`, `#deep-research`, `#eval`, `#optimization`

---

## AI Daily

<a id="item-ai-daily-1"></a>
### [OpenAI 就澳洲政府网站事件道歉](https://openai.com/index/how-we-will-do-better-for-australia) ⭐️ 8.8/10

OpenAI 官方博客致歉，称事件涉及澳大利亚政府网站。同时宣布强化安全防护与支持，加强澳大利亚网络防御。此次为区域性政策更新，未提及全球调整。

rss · OpenAI Blog · Sep 29, 01:00

**「为什么重要」** 主要 AI 实验室正式回应政府网站相关事件，并给出安全防护与支持承诺，属区域合规与网络防御层面的政策动作。

**Tags**: `#policy`, `#industry`, `#lab`

---

<a id="item-ai-daily-2"></a>
### [How we found 24 Android vulnerabilities using our open source AI security agent](https://github.blog/security/how-we-found-24-android-vulnerabilities-using-our-open-source-ai-security-agent/) ⭐️ 8.3/10

GitHub 官方博客介绍其开源 AI 安全代理通过定向任务流发现 24 个 Android 漏洞，并开放该工具供用户自行运行。

rss · GitHub Blog · Sep 28, 19:00

**Tags**: `#open-source`, `#industry`, `#product`, `#lab`

---

<a id="item-ai-daily-3"></a>
### [OpenAI Expands Lenfest Program with Up to $10M Support](https://openai.com/index/lenfest-ai-collaborative-expansion) ⭐️ 6.8/10

OpenAI announced an expansion of the Lenfest AI Collaborative and Fellowship Program on September 28, 2026. The commitment includes $5 million in funding and up to $5 million in software credits and engineering support. The source is an official OpenAI blog post; no further technical or product details were provided.

rss · OpenAI Blog · Sep 28, 07:00

**「Why It Matters」** The expansion concerns a philanthropic program rather than a core model or product release, limiting its broader industry impact.

**Tags**: `#lab`, `#industry`, `#product`

---

## AI Deals

<a id="item-ai-deals-1"></a>
### [OpenCode 与 Command Code $10 套餐 DeepSeek 额度升至 $60](https://www.appinn.com/opencode-vs-command-code-ai-coding-plans/) ⭐️ 8.0/10

OpenCode 将 $10/月 Go 套餐中的 DeepSeek V4.1 Flash 额度永久提升至 $60/月。Command Code 随后在 $10/月 GOAT 套餐中做出相同调整，同款模型额度也永久提升至 $60/月。用户以 $10 月费可获得价值 $60 的模型用量，额度放大 6 倍。材料未提及具体领取条件或截止时间。

rss · 小众软件 · Sep 28, 08:17

**「为什么重要」** 两家在 $10 套餐中同时将 DeepSeek V4.1 Flash 额度提升至 $60/月，$10 月费可用到 $60 模型用量，对依赖该模型做编程辅助的用户是直接的额度放大。

**「可关注」** 可关注：OpenCode Go 与 Command Code GOAT 的 $10/月套餐均永久提供 $60/月 DeepSeek V4.1 Flash 额度；适合已订阅这两家、且主力使用 DeepSeek V4.1 Flash 的用户，材料未说明超额计费或额度结转规则。

**Tags**: `#promo`, `#credits`, `#api`

---