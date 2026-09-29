---
layout: default
title: "Horizon Summary: 2026-09-29 (EN)"
date: 2026-09-29
lang: en
---

> From 184 items, 21 important content pieces were selected

---

**Agent Harness Architecture**
1. [openai/codex released rust-v0.158.0](#item-harness-arch-1) ⭐️ 8.3/10
2. [MCP TypeScript SDK v2.2.0 Released](#item-harness-arch-2) ⭐️ 8.3/10
3. [modelcontextprotocol/typescript-sdk released 1.31.0](#item-harness-arch-3) ⭐️ 8.3/10
4. [Claude Code v2.1.284 发布](#item-harness-arch-4) ⭐️ 7.8/10
5. [Kitesurf 更新支持 WebMCP](#item-harness-arch-5) ⭐️ 7.3/10
6. [Fireworks 1.7.0 发布](#item-harness-arch-6) ⭐️ 6.8/10
7. [LangChain 1.4.3 Patch Released](#item-harness-arch-7) ⭐️ 5.8/10

**AI Agent Engineer**
1. [CIS 修正 RLVR 训练推理失配](#item-agent-engineer-1) ⭐️ 8.0/10
2. [llm-anthropic 0.30 发布](#item-agent-engineer-2) ⭐️ 7.8/10
3. [TraceDance 用部署轨迹构建行为基准](#item-agent-engineer-3) ⭐️ 7.5/10
4. [EMem-Bench：2,554 个具身 episode 测长程记忆](#item-agent-engineer-4) ⭐️ 7.5/10
5. [Supporting native Rust in Workers with the new Emscripten target for wasm-bindgen](#item-agent-engineer-5) ⭐️ 6.8/10
6. [Holo4 发布：27B 与 35B-A3B](#item-agent-engineer-6) ⭐️ 6.3/10
7. [Sonnet 5.5 发布](#item-agent-engineer-7) ⭐️ 6.0/10
8. [Claude Sonnet 5.5 发布](#item-agent-engineer-8) ⭐️ 6.0/10
9. [Claude Code’s Next Era — Thariq Shihipar, Anthropic](#item-agent-engineer-9) ⭐️ 6.0/10
10. [HF daily paper: AdaTutoRank: Learning to Rerank Document Sets via Adaptive Tutoring Optimization for RAG and Deep Research](#item-agent-engineer-10) ⭐️ 5.5/10

**AI Daily**
1. [OpenAI 就澳大利亚政府网站事件道歉](#item-ai-daily-1) ⭐️ 8.8/10
2. [GitHub AI Security Agent Finds 24 Android Bugs](#item-ai-daily-2) ⭐️ 7.3/10
3. [OpenAI 扩展 Lenfest 计划](#item-ai-daily-3) ⭐️ 6.8/10

**AI Deals**
1. [$10 套餐 6 倍 DeepSeek 额度](#item-ai-deals-1) ⭐️ 7.0/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [openai/codex released rust-v0.158.0](https://github.com/openai/codex/releases/tag/rust-v0.158.0) ⭐️ 8.3/10

Codex Rust v0.158.0 adds MCP OAuth client-secret support, bearer-token-secured exec-server WebSockets, sandbox fixes, and stricter default terminal approval for elevated commands.

github · github-actions\[bot\] · Sep 28, 05:07

**Tags**: `#mcp`, `#sandbox`, `#permissions`, `#tools`, `#runtime`

---

<a id="item-harness-arch-2"></a>
### [MCP TypeScript SDK v2.2.0 Released](https://github.com/modelcontextprotocol/typescript-sdk/releases/tag/v2.2.0) ⭐️ 8.3/10

The MCP TypeScript SDK v2.2.0 updates the client, server, core, server-legacy, and codemod packages. It tightens machine-to-machine OAuth by requiring \`expectedIssuer\` on \`ClientCredentialsProvider\`, \`PrivateKeyJwtProvider\`, \`StaticPrivateKeyJwtProvider\`, and \`CrossAppAccessProvider\`, and makes \`fetchToken\(\)\` throw \`AuthorizationServerMismatchError\` before sending anything when client information is bound to a different authorization server. List calls without a cursor now follow \`nextCursor\` until the server stops sending one, still capped by \`listMaxPages\`.

github · felixweinberger · Sep 28, 19:24

**「Design Notes」** OAuth providers now stamp and validate the authorization-server \`issuer\` on client information, rejecting mismatches pre-flight. Pagination is handled inside the SDK so \`listTools\(\)\`, \`listPrompts\(\)\`, \`listResources\(\)\`, and \`listResourceTemplates\(\)\` return complete lists by default.

**「What Changed」** \`expectedIssuer\` is deprecated-if-missing on four M2M OAuth providers; \`fetchToken\(\)\` adds an authorization-server mismatch guard; list methods auto-paginate; and fixes restore CommonJS type-checking, prevent \`Client.listen\(\)\` unhandled rejections and hangs, preserve \`\_meta\` on \`input\_required\`, treat \`.localhost\` as loopback, and stop \`createMcpHandler\` stack overflows.

**Tags**: `#mcp`, `#permissions`, `#tools`, `#runtime`

---

<a id="item-harness-arch-3"></a>
### [modelcontextprotocol/typescript-sdk released 1.31.0](https://github.com/modelcontextprotocol/typescript-sdk/releases/tag/1.31.0) ⭐️ 8.3/10

MCP TypeScript SDK 1.31.0 binds stored OAuth credentials to their issuing authorization server and deprecates provider construction without expectedIssuer.

github · felixweinberger · Sep 28, 18:52

**Tags**: `#mcp`, `#permissions`, `#auth`

---

<a id="item-harness-arch-4"></a>
### [Claude Code v2.1.284 发布](https://github.com/anthropics/claude-code/releases/tag/v2.1.284) ⭐️ 7.8/10

Anthropic released Claude Code v2.1.284. The release sets Claude Sonnet 5.5 \(\`claude-sonnet-5-5\`\) as the default Sonnet model with 1M context, priced at $2/$10 per Mtok and $0.20/Mtok for cache reads. Auto mode adds a &quot;Yes, but ask again next time&quot; option before reads outside working directories. The update also brings USD spend-limit tracking to \`/usage\` and the status line, rebindable effort-slider keybindings, and \`/mcp reconnect all\`.

github · ashwin-ant · Sep 28, 18:02

**「设计要点」** Auto mode now distinguishes one-off reads from recurring ones outside the working directory, so a single approval does not suppress future prompts. The Claude apps gateway adds certificate client authentication \(\`private\_key\_jwt\`\) and Google Cloud OTLP telemetry export, and warns when managed \`availableModels\` is empty or omits the startup model without setting \`model\` or \`enforceAvailableModels\`.

**「改了什么」** The default model shifts to Sonnet 5.5, and out-of-directory read permissions become granular. Spend limits now surface as USD amounts in \`/usage\` and the status line, while MCP recovery and effort-slider controls gain dedicated commands and keybindings.

**Tags**: `#runtime`, `#tools`, `#permissions`, `#mcp`

---

<a id="item-harness-arch-5"></a>
### [Kitesurf 更新支持 WebMCP](https://blog.cloudflare.com/kitesurf-update/) ⭐️ 7.3/10

Cloudflare 更新跑在 Workers 上的 agentic browser Kitesurf，加入 WebMCP 支持，网站可直接向 agent 暴露函数（如 searchFlights\(\)），不用再模拟点击。Cloudflare Radar 已提供 navigate-to、set-location 等 WebMCP 工具，可通过 chrome-devtools-mcp 经 wss 端点接入。Kitesurf 补齐 Browser Run 全量 API，支持 CDP、Playwright、Puppeteer、MCP，WPT 子测试通过数达 730,000+，比发布时多 500,000。官方称新增 Web 标准支持后，wall-clock 时间与 CPU 用量仍与发布基准大致持平。

rss · Cloudflare AI · Sep 28, 13:00

**「设计要点」** Kitesurf 把 PageScript（页面会话与代码执行）和 PageRenderer（像素生成）拆开，安全关键逻辑留在服务端，渲染可移到客户端或另一个 Worker。终端版将 PageRenderer 输出改为 Kitty 图形协议或 ANSI 文本，让开发者在终端里直接查看 agent 看到的页面。

**「改了什么」** 新增 WebMCP 支持与 Worker 内 env.BROWSER.quickAction\(\) 绑定；Boa 与 Wasm DOM 之间的 getAttribute、id、parentNode 等常见读取改为在 Wasm DOM 内直接应答，减少跨引擎往返；字体按需加载，跳过页面未使用的语言包。

**Tags**: `#runtime`, `#tools`, `#mcp`

---

<a id="item-harness-arch-6"></a>
### [Fireworks 1.7.0 发布](https://github.com/langchain-ai/langchain/releases/tag/langchain-fireworks%3D%3D1.7.0) ⭐️ 6.8/10

LangChain Fireworks 集成包 1.7.0 发布，上一版为 1.6.3。新增 prompt caching middleware，在 Fireworks 调用中启用前缀缓存；同时修复 mid-stream read timeout 的分类问题。版本还替换了不可用的集成测试模型，并刷新模型 profile 数据。

github · github-actions\[bot\] · Sep 28, 20:46

**「设计要点」** prompt caching middleware 位于 Fireworks 集成层，负责前缀缓存命中；mid-stream read timeout 被单独归类，与连接阶段超时区分。

**「改了什么」** 相对 1.6.3，1.7.0 引入 prompt caching middleware，支持前缀缓存；修复 mid-stream read timeout 分类；替换失效的集成测试模型，并刷新模型 profile 数据。

**Tags**: `#prefix-cache`, `#runtime`, `#tools`

---

<a id="item-harness-arch-7"></a>
### [LangChain 1.4.3 Patch Released](https://github.com/langchain-ai/langchain/releases/tag/langchain%3D%3D1.4.3) ⭐️ 5.8/10

LangChain 1.4.3 is a patch release that adds Bedrock Mantle chat model support to \`init\_chat\_model\` and fixes agent tool-call and cache-setting bugs. It also recognizes GPT-6 structured output without profiles. No breaking changes are introduced.

github · github-actions\[bot\] · Sep 28, 20:17

**「Design Notes」** The patch adjusts the model initialization path and agent tool layer. \`init\_chat\_model\` now routes Bedrock Mantle chat models, and \`create\_agent\` repairs invalid tool calls. Cache settings are sanitized for fallback models to prevent misconfiguration.

**「What Changed」** Relative to 1.4.2, \`init\_chat\_model\` supports Bedrock Mantle chat models, \`create\_agent\` fixes invalid tool calls, cache settings are sanitized for fallback models, and GPT-6 structured output is recognized without profiles.

**Tags**: `#runtime`, `#tools`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [CIS 修正 RLVR 训练推理失配](https://huggingface.co/papers/2609.32444) ⭐️ 8.0/10

Hugging Face Daily Papers 于 2026-09-29 收录论文，研究 RLVR 中推理引擎与训练引擎对同一 token 概率不一致的问题。论文提出校准重要性采样（CIS），将失配刻画为 log-odds 中的加性位移 ε\_t，其由 softmax 前的逐 logit 扰动决定，分布近似与 token 置信度无关。CIS 据此实施置信度感知截断，对较大正位移进行截断。原文未完整给出截断阈值，也未提供与既有方法的量化对比。

rss · Hugging Face Daily Papers · Sep 29, 00:00

**「为什么重要」** RLVR 是 coding agent 与 harness 训练的常见范式，训练与推理引擎的概率失配会直接影响策略更新。该论文给出可复现的失配刻画与修正方法，为 Agent 训练链路提供直接的技术参考。

**「可关注」** 可关注：CIS 把训练-推理失配归结为 logit 空间的加性位移，并据此做置信度感知截断，工程上可在 RLVR 训练框架中复现该修正逻辑。

**Tags**: `#eval`, `#harness`, `#coding-agent`

---

<a id="item-agent-engineer-2"></a>
### [llm-anthropic 0.30 发布](https://github.com/simonw/llm-anthropic/releases/tag/0.30) ⭐️ 7.8/10

simonw/llm-anthropic 发布 0.30，新增 Claude Sonnet 5.5 支持。插件加入 \`llm anthropic refresh\` 与 \`llm anthropic models\`，从 Anthropic models API 拉取可用模型并缓存至 \`anthropic\_models.json\`，未知模型按 API 回报的能力注册。新增 \`llm anthropic count\`，基于 token counting API 在不执行 prompt 的情况下统计输入 token，参数与 \`llm prompt\` 一致，Python 暴露 \`model.count\_tokens\(\)\`。修复对话遭遇拒绝后，后续 follow-up 因空 content 报 400 的错误。

github · simonw · Sep 28, 23:06

**「为什么重要」** 对 agent 工程师，\`count\` 提供了执行前的上下文与成本预估，\`refresh\`/\`models\` 减少跟进 Anthropic 新模型时的手工配置。拒绝后的 400 修复直接改善多轮对话稳定性。

**「可关注」** \`llm anthropic count\` 与 \`model.count\_tokens\(\)\` 可在不触发推理的前提下验证 prompt token 规模，适合嵌入 harness 预检；\`refresh\` 将模型能力发现从人工维护转为 API 驱动。

**Tags**: `#harness`, `#observability`, `#coding-agent`

---

<a id="item-agent-engineer-3"></a>
### [TraceDance 用部署轨迹构建行为基准](https://huggingface.co/papers/2609.33295) ⭐️ 7.5/10

TraceDance 从真实部署轨迹自动构建针对特定不良行为的 agent 基准。Anchor-and-Confirm 结合可编程检索与 Flash LLM 的候选确认，Anchor Synthesis Loop 生成并修订自定义行为规范。基准通过 decision-point continuation 评估 LLM 在记录决策点的下一轮输出，使用行为专属 rubric，不需要参考答案或环境回放。论文包含 coding 与通用任务的实验。

rss · Hugging Face Daily Papers · Sep 29, 00:00

**「为什么重要」** Agent 执行任务时可能出现不良行为，固定基准套件难以覆盖部署中遇到的具体问题。TraceDance 把部署轨迹直接转为行为测试，为 eval 与 observability 工作流提供了新路径。其架构尚未被证明是主流基准升级，但对 agent 工程师有直接参考价值。

**「可关注」** 可关注：TraceDance 用 decision-point continuation 在记录决策点评测 LLM 下一轮输出，替代环境回放，为 harness 中的 eval 环节提供了从部署轨迹构建测试的新思路。

**Tags**: `#eval`, `#observability`, `#coding-agent`, `#harness`

---

<a id="item-agent-engineer-4"></a>
### [EMem-Bench：2,554 个具身 episode 测长程记忆](https://huggingface.co/papers/2609.28236) ⭐️ 7.5/10

Hugging Face Daily Papers 收录 EmbodiedMemory-Bench（EMem-Bench）。该基准包含 2,554 个交互 episode，覆盖四类任务，要求智能体在长程具身交互中构建并更新记忆。论文将当前智能体的记忆瓶颈归结为四点：细粒度视觉记忆弱、动态世界状态跟踪不可靠、未记录交互结果揭示的世界状态、难以从先前经验泛化。作者认为现有基准未直接评测这些能力。

rss · Hugging Face Daily Papers · Sep 29, 00:00

**「为什么重要」** 对构建具身智能体或记忆系统的工程师，论文明确指出现有基准未覆盖长程交互中的四类记忆缺陷，EMem-Bench 提供了针对这些缺陷的交互式评测面。基准已发布，但是否能直接推动智能体记忆能力提升，尚未有外部验证。

**「可关注」** 可关注：EMem-Bench 把长程具身记忆拆成细粒度视觉、动态世界状态、交互结果记录、经验泛化四个可测维度，做记忆系统的工程师可以对照这四点检查自身设计是否被现有基准遗漏。

**Tags**: `#eval`, `#memory`, `#benchmark`, `#embodied-agent`

---

<a id="item-agent-engineer-5"></a>
### [Supporting native Rust in Workers with the new Emscripten target for wasm-bindgen](https://blog.cloudflare.com/rust-workers-emscripten-target/) ⭐️ 6.8/10

Cloudflare announces an experimental preview of the Emscripten wasm32-unknown-emscripten target for wasm-bindgen, allowing native Rust and Tokio-based applications to run on Workers.

rss · Cloudflare Engineering · Sep 28, 13:00

**Tags**: `#wasm`, `#rust`, `#toolchain`, `#cloudflare-workers`

---

<a id="item-agent-engineer-6"></a>
### [Holo4 发布：27B 与 35B-A3B](https://huggingface.co/blog/Hcompany/holo4) ⭐️ 6.3/10

H Company 发布 Holo4 系列 agentic 模型，提供 27B dense 与 35B-A3B MoE 两个尺寸，已在 H Models API 上线，同时发布 Holotron4 Nano。模型通过 GUI、代码、MCP 和 API 与软件交互，训练基于 Agentic Task Factory 生成的环境与任务。OSWorld 2.0 上，27B 得 61.7%，35B-A3B 得 30.9%，低于 Opus 5.5 的 81.8%，但参数量与成本显著更低。官方公开了基准测试的完整轨迹。

rss · Hugging Face Blog · Sep 28, 09:44

**「为什么重要」** 对 coding agent 与 harness 工程师，Holo4 的要点是同一模型跨 GUI、代码、MCP、API 四类接口通用，且公开 OSWorld 2.0 与 AutomationBench 的完整轨迹，可直接回放每一步。其 harness 改造经验——可靠记忆与桌面 shell——对长程 agent 设计有参考意义。

**「可关注」** Holo4 将 GUI 操作、代码执行、MCP 与 API 调用统一到同一模型，官方称无需按平台切换模型；同时公开全部基准轨迹，便于复现与对比 harness 差异。

**Tags**: `#coding-agent`, `#mcp`, `#eval`, `#harness`

---

<a id="item-agent-engineer-7"></a>
### [Sonnet 5.5 发布](https://www.anthropic.com/claude-sonnet-5-5) ⭐️ 6.0/10

Anthropic 上线 Sonnet 5.5，Hacker News 出现相关讨论。有用户指出 Sonnet 5.5 在 Terminal-Bench 得分 70.6，高于 Opus 5.5 的 66.4；但 Opus 5.5 约 10% 的试验因安全护栏触发回退模型，Sonnet 5.5 仅 1.5%，得分差距可能主要来自回退率差异而非模型能力。另有评论提到 Sonnet 5.5 对高风险网络安全任务会回退到 Sonnet 5。

hackernews · D2OQZG8l5BI1S06 · Sep 28, 17:58 · [Discussion](https://news.ycombinator.com/item?id=49881850)

**「为什么重要」** Terminal-Bench 等基准的裸分可能被安全护栏的回退率混淆，直接影响对模型编码能力的判断。对搭建 coding agent 评测流程的工程师来说，分差归因需要先剥离回退样本。

**「可关注」** 可关注：在对比 Terminal-Bench 分数时，先确认各模型的安全护栏回退率，避免把回退差异当成能力差距。

**「评论」** 评论分歧集中在性价比与使用场景。一方认为 Opus 5.5 的效率已足够日常 2–3 个并发会话，Sonnet 5.5 的额外并发不实用；另一方则强调 GLM、DeepSeek 等中国模型价格低得多，Anthropic 的定价缺乏竞争力。多数评论为闲聊，少数涉及评测归因与网络安全回退策略。

**Tags**: `#coding-agent`, `#eval`, `#observability`

---

<a id="item-agent-engineer-8"></a>
### [Claude Sonnet 5.5 发布](https://simonwillison.net/2026/Sep/28/claude-sonnet-5-5/) ⭐️ 6.0/10

Anthropic 发布 Claude Sonnet 5.5，官方称运行速度提升 30% 以上，多数任务成本最多降低 30%。定价与 Sonnet 5 持平，Simon Willison 实测认为其基准表现已全面超越前代，并作为 claude.ai 免费层模型上线。该模型在 max 思考档位复现了 Opus 5.5 的缺陷：单次请求思考 128,000 tokens（约 $1.28）后耗尽额度，未能生成 SVG；xhigh 档位耗时 41 秒、花费 5.74 美分，可正常输出。作者指出其在部分编码任务上接近 Opus 5.5，Haiku 5.5 将在未来数周内发布。

rss · Simon Willison · Sep 28, 22:07

**「为什么重要」** 免费层模型更替直接影响默认用户体验。Sonnet 5.5 进入 claude.ai 免费层后，与 ChatGPT 免费层使用的 Luna 5.6 形成对比，作者认为 Anthropic 当前免费档位能力更强。此外，max 档位的 token 失控缺陷提示高思考预算场景仍需成本护栏。

**「可关注」** 可关注：max 思考档位在 Sonnet 5.5 上仍可能耗尽 token 且无法产出结果，接入时需为思考预算和输出长度设置硬上限，避免单次请求成本失控。

**Tags**: `#coding-agent`, `#eval`, `#observability`

---

<a id="item-agent-engineer-9"></a>
### [Claude Code’s Next Era — Thariq Shihipar, Anthropic](https://www.latent.space/p/thariq) ⭐️ 6.0/10

Anthropic&\#x27;s Thariq Shihipar discusses Claude Code&\#x27;s next era, including shipping new models and features like Plugins and Projects.

rss · Latent Space · Sep 29, 01:48

**Tags**: `#coding-agent`, `#harness`, `#orchestration`

---

<a id="item-agent-engineer-10"></a>
### [HF daily paper: AdaTutoRank: Learning to Rerank Document Sets via Adaptive Tutoring Optimization for RAG and Deep Research](https://huggingface.co/papers/2609.32472) ⭐️ 5.5/10

AdaTutoRank proposes adaptive tutoring optimization for set-level document reranking in RAG and deep research, but only an abstract is available without results or code.

rss · Hugging Face Daily Papers · Sep 29, 00:00

**Tags**: `#rag`, `#eval`, `#retrieval`, `#deep-research`

---

## AI Daily

<a id="item-ai-daily-1"></a>
### [OpenAI 就澳大利亚政府网站事件道歉](https://openai.com/index/how-we-will-do-better-for-australia) ⭐️ 8.8/10

OpenAI 就涉及澳大利亚政府网站的事件公开道歉。官方称将加强安全防护措施，并提供支持以强化澳大利亚的网络防御能力。

rss · OpenAI Blog · Sep 28, 19:00

**「为什么重要」** 主要 AI 实验室公开为政府网站相关事件道歉，并承诺加强网络安全支持，显示其与政府数字基础设施交互时的责任边界正受到更严格审视。

**「可关注」** OpenAI 将加强安全防护措施，并为澳大利亚网络防御提供支持。

**Tags**: `#lab`, `#policy`, `#industry`

---

<a id="item-ai-daily-2"></a>
### [GitHub AI Security Agent Finds 24 Android Bugs](https://github.blog/security/how-we-found-24-android-vulnerabilities-using-our-open-source-ai-security-agent/) ⭐️ 7.3/10

GitHub&\#x27;s official blog reports that its open-source AI security agent uncovered 24 Android vulnerabilities using targeted taskflows. The post details the critical bugs and explains how to run the agent on your own app. The source is a first-party security tooling case study, not a major model release or policy change.

rss · GitHub Blog · Sep 28, 19:00

**「Why It Matters」** The case study shows that an open-source AI agent can surface critical Android vulnerabilities, and the published taskflows give teams a concrete method to reproduce the audit on their own codebases.

**「Takeaway」** Watch: GitHub&\#x27;s open-source AI security agent and the targeted taskflows behind the 24 findings, which the blog says can be run against your own Android app.

**Tags**: `#open-source`, `#product`, `#industry`

---

<a id="item-ai-daily-3"></a>
### [OpenAI 扩展 Lenfest 计划](https://openai.com/index/lenfest-ai-collaborative-expansion) ⭐️ 6.8/10

OpenAI 宣布扩展 Lenfest AI Collaborative and Fellowship Program。投入 500 万美元资金，并提供至多 500 万美元的软件额度与工程支持。此次属于公益项目扩展，不涉及模型发布或行业政策变化。

rss · OpenAI Blog · Sep 28, 07:00

**「为什么重要」** 关注 AI 行业生态的读者可注意，此举显示 OpenAI 正通过非产品渠道扩大影响力。但项目影响面相对有限，暂未触及 coding agent 或 harness 的核心技术演进。

**「可关注」** OpenAI 以资金、软件额度与工程支持结合的形式扩展公益项目，支持结构较为完整。

**Tags**: `#lab`, `#industry`

---

## AI Deals

<a id="item-ai-deals-1"></a>
### [$10 套餐 6 倍 DeepSeek 额度](https://www.appinn.com/opencode-vs-command-code-ai-coding-plans/) ⭐️ 7.0/10

OpenCode 与 Command Code 先后宣布，将 $10/月套餐中的 DeepSeek V4.1 Flash 使用额度永久提升至 $60/月等值。OpenCode 的 Go 套餐与 Command Code 的 GOAT 套餐均在此列，相当于 $10 换取 $60 额度，提升 6 倍。材料未提及领取条件、绑卡或地区限制，也未提供官方领取页面。

rss · 小众软件 · Sep 28, 08:17

**「为什么重要」** 额度为永久提升而非限时活动，$10/月套餐可用到 $60/月等值的 DeepSeek V4.1 Flash，直接影响订阅性价比。

**「可关注」** 可关注：这是 $10/月付费套餐的额度提升，不是免费额度；材料未说明绑卡、地区或领取入口等限制，订阅前需自行确认。

**Tags**: `#promo`, `#credits`, `#api`

---