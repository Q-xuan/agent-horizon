---
layout: default
title: "Horizon Summary: 2026-09-29 (EN)"
date: 2026-09-29
lang: en
---

> From 210 items, 22 important content pieces were selected

---

**Agent Harness Architecture**
1. [Codex rust-v0.158.0 发布](#item-harness-arch-1) ⭐️ 8.8/10
2. [MCP TypeScript SDK 1.31.0 Released](#item-harness-arch-2) ⭐️ 8.8/10
3. [MCP TypeScript SDK v2.2.0 Released](#item-harness-arch-3) ⭐️ 8.3/10
4. [Kitesurf 更新支持 WebMCP](#item-harness-arch-4) ⭐️ 8.3/10
5. [Claude Code v2.1.284 发布](#item-harness-arch-5) ⭐️ 6.8/10
6. [crewAI 1.15.23 发布](#item-harness-arch-6) ⭐️ 6.8/10
7. [langchain-fireworks 1.7.0 Adds Prompt Caching Middleware](#item-harness-arch-7) ⭐️ 6.3/10

**AI Agent Engineer**
1. [DQ 论文：拆分预填充与解码量化](#item-agent-engineer-1) ⭐️ 8.0/10
2. [AgentWorld：多智能体长程协作基准](#item-agent-engineer-2) ⭐️ 8.0/10
3. [Sonnet 5.5 发布，安全回退影响评测](#item-agent-engineer-3) ⭐️ 7.0/10
4. [Cloudflare 发布 CLI \`cf\`](#item-agent-engineer-4) ⭐️ 7.0/10
5. [Holo4: powering generalist computer-use agents](#item-agent-engineer-5) ⭐️ 6.8/10
6. [Workers 原生运行 Rust 预览](#item-agent-engineer-6) ⭐️ 6.3/10
7. [SLCA-GRPO：解决工具调用信用误配](#item-agent-engineer-7) ⭐️ 6.0/10
8. [2026 LLM 年度 keynote 回顾](#item-agent-engineer-8) ⭐️ 5.5/10
9. [Swift 1.5 + HyperQwen 提速 37%](#item-agent-engineer-9) ⭐️ 5.5/10

**AI Daily**
1. [Anthropic 联手 NVIDIA 管 Agent](#item-ai-daily-1) ⭐️ 9.8/10
2. [AI 发现 24 个 Android 漏洞](#item-ai-daily-2) ⭐️ 8.3/10
3. [OpenAI 500 万美元扩 Lenfest 计划](#item-ai-daily-3) ⭐️ 6.8/10
4. [GPT-6 Astra 税务工作簿快 1 倍](#item-ai-daily-4) ⭐️ 6.3/10
5. [Highlights from Git 2.56](#item-ai-daily-5) ⭐️ 6.3/10

**AI Deals**
1. [OpenCode 与 Command Code $10 套餐额度翻 6 倍](#item-ai-deals-1) ⭐️ 7.0/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [Codex rust-v0.158.0 发布](https://github.com/openai/codex/releases/tag/rust-v0.158.0) ⭐️ 8.8/10

Codex rust-v0.158.0 ships MCP OAuth client-secret support, bearer-token-secured exec-server WebSockets, and default terminal input approval for elevated commands. Sandbox fixes address Windows 10 paths, nested writable roots on Linux, and Git metadata protections. The fullscreen TUI gains copy-on-select and right-click paste, while image generation supports explicit transparent backgrounds.

github · github-actions\[bot\] · Sep 28, 05:07

**「设计要点」** WebSocket authentication is extracted into a dedicated \`codex-websocket-auth\` crate and applied opt-in to exec-server and app-server executor connections. Guardian authorization reviews now bind to the action&\#x27;s target environment, with thread-owned context capture made unconditional and legacy evidence paths removed.

**「改了什么」** Adds \`codex mcp add --oauth-client-secret\` for pre-registered OAuth clients and bearer-token auth for direct exec-server WebSockets. Enables terminal input approval by default for elevated commands, while runtime-only grants skip unnecessary reviews.

**Tags**: `#mcp`, `#permissions`, `#sandbox`, `#runtime`, `#tools`

---

<a id="item-harness-arch-2"></a>
### [MCP TypeScript SDK 1.31.0 Released](https://github.com/modelcontextprotocol/typescript-sdk/releases/tag/1.31.0) ⭐️ 8.8/10

The MCP TypeScript SDK 1.31.0 release hardens OAuth credential storage by binding stored tokens and client information to the authorization server that issued them. Stored credentials now include an \`issuer\` field, and \`ClientCredentialsProvider\`, \`PrivateKeyJwtProvider\`, and \`StaticPrivateKeyJwtProvider\` must be constructed with \`expectedIssuer\`; omitting it is deprecated. Storage implementations that reject unknown fields must allow the new field.

github · felixweinberger · Sep 28, 18:52

**「Design Notes」** OAuth credentials are bound to their issuing authorization server via the new \`issuer\` field, and providers validate \`expectedIssuer\` at construction time. This shifts issuer verification earlier in the auth flow and prevents cross-issuer token reuse at the storage layer.

**「What Changed」** Stored OAuth tokens and client information now include an \`issuer\` field. \`ClientCredentialsProvider\`, \`PrivateKeyJwtProvider\`, and \`StaticPrivateKeyJwtProvider\` require \`expectedIssuer\`; constructing them without it is deprecated. Storage backends that reject unknown fields need to allow \`issuer\`.

**Tags**: `#mcp`, `#permissions`, `#runtime`, `#tools`

---

<a id="item-harness-arch-3"></a>
### [MCP TypeScript SDK v2.2.0 Released](https://github.com/modelcontextprotocol/typescript-sdk/releases/tag/v2.2.0) ⭐️ 8.3/10

The MCP TypeScript SDK v2.2.0 updates the client, server, core, server-legacy, and codemod packages. Machine-to-machine OAuth providers now expect an expectedIssuer; constructing ClientCredentialsProvider, PrivateKeyJwtProvider, StaticPrivateKeyJwtProvider, or CrossAppAccessProvider without it logs a deprecation warning. fetchToken\(\) validates authorization server binding and throws AuthorizationServerMismatchError before sending anything when client information belongs to a different issuer. List calls without a cursor now follow nextCursor until the server stops returning one, with listMaxPages still capping the walk.

github · felixweinberger · Sep 28, 19:24

**「Design Notes」** OAuth providers bind expectedIssuer at construction and enforce it inside fetchToken\(\), moving issuer validation ahead of token requests. Pagination for listTools\(\), listPrompts\(\), listResources\(\), and listResourceTemplates\(\) is now transparent to callers unless listMaxPages caps the walk.

**「What Changed」** OAuth machine-to-machine flows gain issuer binding checks and a new AuthorizationServerMismatchError; list methods auto-paginate via nextCursor. The release also fixes CommonJS type-checking, unhandled rejections in Client.listen\(\), and stack overflows in createMcpHandler.

**Tags**: `#mcp`, `#permissions`, `#tools`

---

<a id="item-harness-arch-4"></a>
### [Kitesurf 更新支持 WebMCP](https://blog.cloudflare.com/kitesurf-update/) ⭐️ 8.3/10

Cloudflare 更新其 agentic browser Kitesurf，核心新增 WebMCP 支持，网站可向 agent 直接暴露 searchFlights\(\) 等函数，不再依赖像素点击。浏览器标准覆盖继续扩大，WPT 子测试通过数达 730,000+，较发布时增加 500,000；URL 模块解析、JSON modules、import map 与 iframe 行为均有改进。渲染层 PageRenderer 可外移到客户端或 Worker，官方还推出终端版本，通过 Kitty 图形协议或纯 ANSI 文本在终端渲染页面。

rss · Cloudflare AI · Sep 28, 13:00

**「设计要点」** Kitesurf 保持 PageScript 与 PageRenderer 分离，安全关键部分留在服务端 isolate，渲染逻辑可移至客户端或独立 Worker。引擎减少 Boa 与 Wasm DOM 的跨边界调用，getAttribute、id、parentNode 等读取直接在 Wasm DOM 内响应；计时器与脚本加载的重复工作减少，内存回收更及时。

**「改了什么」** 新增 WebMCP 支持，Cloudflare Radar 已暴露 navigate-to、set-location 等工具，可通过 chrome-devtools-mcp 连接。Kitesurf 获得完整 Browser Run API 覆盖，支持 CDP、Playwright、Puppeteer、MCP，并在 Worker 脚本中提供 env.BROWSER.quickAction\(\) 绑定。新增终端版本，支持 Kitty 与 ANSI 输出。

**Tags**: `#runtime`, `#tools`, `#mcp`, `#sandbox`

---

<a id="item-harness-arch-5"></a>
### [Claude Code v2.1.284 发布](https://github.com/anthropics/claude-code/releases/tag/v2.1.284) ⭐️ 6.8/10

Claude Code v2.1.284 将 Claude Sonnet 5.5（\`claude-sonnet-5-5\`）设为默认 Sonnet 模型，提供 1M 上下文，定价 $2/$10 per Mtok，缓存读取 $0.20/Mtok。自动模式在工作目录外读取前新增“Yes, but ask again next time”，支持单次放行且保留后续询问。\`/usage\` 与状态行展示 Claude apps gateway 消费上限美元金额，\`rate\_limits.spend\_limit\` 增加 \`used\_usd\`、\`limit\_usd\`、\`period\`。修复恢复会话中 MCP 工具调用因服务器未就绪而失败的问题，现最多等待 10 秒。

github · ashwin-ant · Sep 28, 18:02

**「设计要点」** 权限模型细化：auto mode 对目录外读取提供一次性授权；\`allowManagedPermissionRulesOnly\` 下仅官方或受管来源的插件可保留 \`allowed-tools\` 预批准；\`.claude/rules\` 外部符号链接需显式审批。MCP 工具层新增 \`/mcp reconnect all\` 批量重连，恢复会话中的调用会等待服务器连接完成。

**「改了什么」** 默认模型切换至 Sonnet 5.5；auto mode 读取权限从全量允许/拒绝细化为单次允许并保留后续提示；新增 \`/mcp reconnect all\`、effort slider 键位绑定及 gateway 消费上限与遥测导出（Google OTLP、\`private\_key\_jwt\`）可见性。修复集中在 MCP 工具可用性、权限预批准边界、终端渲染与输入交互。

**Tags**: `#permissions`, `#tools`, `#mcp`, `#runtime`

---

<a id="item-harness-arch-6"></a>
### [crewAI 1.15.23 发布](https://github.com/crewAIInc/crewAI/releases/tag/1.15.23) ⭐️ 6.8/10

crewAI 1.15.23 发布，新增原生 Gemini 3.8 Flash 支持，并调整 eval 与 tracing 流程。crewai eval 现在通过 AMP 记录最近一次被追踪的运行，而非直接打印；tracing task span 也会带上声明的输出格式与结果。平台集成设置流程得到简化，常用集成被优先展示。此外修复了 LLM 限流重试、Bedrock acall 同步回退、SQLite 连接关闭、S3 响应体关闭、Selenium driver 复用等问题。

github · lorenzejay · Sep 28, 21:14

**「设计要点」** 运行时层面，LLM 对限流提供商调用增加重试，Bedrock 的 acall 在必要时回退到同步调用；tracing 与 eval 的耦合更紧，task span 直接携带输出格式和结果，供 CLI 与 TUI 消费。资源管理上，修复了 SQLite 连接未关闭、S3 响应体未关闭、Selenium driver 不可复用等泄漏问题。

**「改了什么」** 相比此前版本，模型层新增 Gemini 3.8 Flash 原生支持；eval 工作流从打印最近追踪运行改为通过 AMP 记录；TUI 修复 tracing 开关并加入 Evaluate 按钮；LLM 与 Bedrock 调用路径分别补上限流重试和同步回退；同时清理 SQLite、S3、Selenium 相关资源泄漏。

**Tags**: `#runtime`, `#tools`, `#eval`

---

<a id="item-harness-arch-7"></a>
### [langchain-fireworks 1.7.0 Adds Prompt Caching Middleware](https://github.com/langchain-ai/langchain/releases/tag/langchain-fireworks%3D%3D1.7.0) ⭐️ 6.3/10

langchain-fireworks 1.7.0 is a minor provider integration update for LangChain. It adds a prompt caching middleware and fixes classification of mid-stream read timeouts. The release also refreshes model profile data and replaces an unavailable integration test model. No breaking changes are documented.

github · github-actions\[bot\] · Sep 28, 20:46

**「Architecture Note」** The prompt caching middleware is added to the Fireworks provider integration. The timeout fix adjusts how streaming responses classify mid-stream read timeouts.

**「What Changed」** Adds a prompt caching middleware and fixes mid-stream read timeout classification. Also replaces an unavailable integration test model and refreshes model profile data.

**Tags**: `#prefix-cache`, `#runtime`, `#tools`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [DQ 论文：拆分预填充与解码量化](https://huggingface.co/papers/2609.26333) ⭐️ 8.0/10

论文提出 disaggregated quantization（DQ），为预填充和解码阶段分别定制计算格式、权重与存储位置。在 Qwen 3 和 Gemma 3 上，解码阶段移除激活量化可在不增加推理成本的前提下提升解码密集型任务的准确率。训练独立的计算原生预填充权重，相比纯权重推理加速提示处理，并在 2-3-bit 解码下匹配或超过其准确率。论文发布 Qwen3.8-27B GGUF 解码器；训练 NVFP4 预填充器使 1-bit 准确率提升 32.5 个百分点。

rss · Hugging Face Daily Papers · Sep 28, 00:00

**「为什么重要」** 长上下文预填充与逐 token 解码对量化策略的需求相反，该工作给出可分别优化的实证路径，直接影响服务成本与精度权衡。

**「可关注」** 可关注：为预填充与解码配置不同量化格式（如解码侧保留激活量化、预填充侧用 NVFP4）可能成为 LLM 服务的新默认选项，需在自有工作负载上验证 2-3-bit 解码的精度边界。

**Tags**: `#inference`, `#quantization`, `#llm-serving`, `#performance`

---

<a id="item-agent-engineer-2"></a>
### [AgentWorld：多智能体长程协作基准](https://huggingface.co/papers/2609.31590) ⭐️ 8.0/10

AgentWorld 是一个评测多智能体 LLM 长程协作的新基准，包含 100 个人工标注任务和 100 个增强变体。任务在 MMORPG 沙盒中展开，要求 3–20 个非对称角色在 50+ 轮交互里通过通信、联合规划和资源共享完成目标。所有智能体处于黑盒设置，独立行动且无法访问彼此内部状态。论文提出量化协作有效性的指标，而非仅看二元任务成败。

rss · Hugging Face Daily Papers · Sep 28, 00:00

**「为什么重要」** 现有基准多聚焦竞争场景、20 步以内的短程交互，或仅聚合个体表现，难以分离真正的协作能力。AgentWorld 把评测重心移到长程、非对称、黑盒协作，为多智能体系统的评测与编排提供更贴近真实约束的测试床。

**「可关注」** 可关注：AgentWorld 在二元任务成败之外引入协作有效性指标，设计多智能体评测时需把通信、联合规划与资源共享的协作质量单独度量。

**Tags**: `#eval`, `#orchestration`, `#multi-agent`, `#benchmark`

---

<a id="item-agent-engineer-3"></a>
### [Sonnet 5.5 发布，安全回退影响评测](https://www.anthropic.com/claude-sonnet-5-5) ⭐️ 7.0/10

Anthropic 发布 Sonnet 5.5。HN 讨论聚焦 Terminal-Bench 分数：Sonnet 5.5 得 70.6，高于 Opus 5.5 的 66.4。用户 abejora 分析称，Opus 5.5 有 10% 试验因安全防护回退到备用模型，Sonnet 5.5 仅 1.5%，分数差距可能主要来自回退率差异，并引用 Sonnet 5.5 System Card 第 8.5 节。用户 wongarsu 转引官方说明，Sonnet 5.5 网络安全能力较 Sonnet 5 大幅提升，因此部署与 Opus 5.5 同级防护，高风险网络安全任务会回退到 Sonnet 5。用户 simonw 实测，在 max thinking effort 下，Sonnet 5.5 与 Opus 5.5 同样在 15 分钟内耗尽 128,000 thinking tokens，未产出最终 SVG。

hackernews · D2OQZG8l5BI1S06 · Sep 28, 17:58 · [Discussion](https://news.ycombinator.com/item?id=49881850)

**「为什么重要」** 模型选型不能只看榜单分数。安全回退率直接改变 Terminal-Bench 等终端任务表现，生产环境需把回退当作可观测指标。同时，max thinking effort 下的 token 预算与超时风险在 Sonnet 5.5 上仍未解决。

**「可关注」** 接入 Sonnet 5.5 时，将安全回退率和 thinking token 消耗纳入监控，避免用单一评测分数替代生产行为评估。

**「评论」** 社区对 Sonnet 5.5 的实用性存在分歧。Sol- 认为 Opus 5.5 效率已足够，5x 限额下日常 2–3 个并发会话够用，不确定何时需要 Sonnet 5.5。abejora 和 wongarsu 从安全回退角度解释评测差异，认为不应高估 Sonnet 5.5 的 Terminal-Bench 优势。simonw 实测确认 max thinking effort 下存在 128k thinking token 耗尽问题。

**Tags**: `#coding-agent`, `#eval`, `#observability`, `#permissions`

---

<a id="item-agent-engineer-4"></a>
### [Cloudflare 发布 CLI \`cf\`](https://blog.cloudflare.com/cloudflare-cf-cli-launch/) ⭐️ 7.0/10

Cloudflare 推出 agentic CLI \`cf\`，用于操作其 API。该工具以 TypeScript 编写，配置格式同样基于 TypeScript。社区讨论聚焦于技术选型与 agent 可发现性。

hackernews · macleos · Sep 28, 15:28 · [Discussion](https://news.ycombinator.com/item?id=49879577)

**「为什么重要」** 云厂商开始为 agent 场景定制 CLI，并引入 TypeScript 配置格式。对 coding agent 与 harness 开发者而言，这关系到工具发现方式、依赖管理和运行时开销等实际工程选择。

**「可关注」** agentic CLI 采用 TypeScript 配置虽增强灵活性，但社区质疑其依赖负担与编译语言缺失，设计 harness 时需在 agent 可发现性与部署简洁性之间取舍。

**「评论」** 评论分歧明显。slowin 认为不应强迫用户管理 CLI 依赖，应使用编译语言；bhouston 建议支持 opencli 规范以提升可发现性；vamsiraju 觉得 TypeScript 配置格式&quot;最令人困惑但有趣&quot;；emadabdulrahim 感叹当下最出色的产品发布之一是 CLI。

**Tags**: `#coding-agent`, `#orchestration`, `#harness`

---

<a id="item-agent-engineer-5"></a>
### [Holo4: powering generalist computer-use agents](https://huggingface.co/blog/Hcompany/holo4) ⭐️ 6.8/10

Hugging Face blog announces Holo4, a new generalist computer-use agent model series \(27B dense and 35B-A3B MoE\) that supports GUIs, code, MCP, and APIs, with released trajectories and datasets.

rss · Hugging Face Blog · Sep 28, 09:44

**Tags**: `#coding-agent`, `#mcp`, `#eval`, `#observability`

---

<a id="item-agent-engineer-6"></a>
### [Workers 原生运行 Rust 预览](https://blog.cloudflare.com/rust-workers-emscripten-target/) ⭐️ 6.3/10

Cloudflare 宣布 wasm-bindgen 新增 Emscripten 目标的首个公开实验性预览，支持在 Workers 上原生运行 Rust 及 Tokio 应用。该目标由 Google 一年前发起，Cloudflare 工程师继续推进并合入 wasm-bindgen。官方测试显示库兼容性明显改善，并在 Durable Object 中通过 Tokio 真实 TCP socket 跑通了 Rust 版 Minecraft 服务器 Pumpkin。目前实验补丁集已提供示例，Tokio 的 wasm32-unknown-emscripten 目标支持补丁已先行合入上游，但在 Rust Workers Tokio 示例中仍需直接引入相关补丁。

rss · Cloudflare Engineering · Sep 28, 13:00

**「为什么重要」** Workers 是单线程 JS 事件循环环境，与 Tokio 依赖的阻塞式 parking 语义存在根本冲突。此次借 Emscripten 虚拟化 timer、文件系统和 socket，并配合 JSPI 与 Tokio 补丁，把原生 Rust 异步生态接入 Workers，但功能仍处实验预览，尚未成为稳定生产路径。

**「可关注」** 可关注：Emscripten 目标在 Workers 上通过 Node.js 编译标志虚拟化原生平台特性，使 Tokio 阻塞调用可借助 JSPI 挂起并交还事件循环；但 JSPI 栈切换不切换线程，Tokio 线程局部运行时上下文会被新进入的 Wasm 调用共享并触发 panic，完全可重入的 JSPI 支持仍需仔细处理线程局部状态。

**Tags**: `#toolchain`, `#wasm`, `#cloudflare`

---

<a id="item-agent-engineer-7"></a>
### [SLCA-GRPO：解决工具调用信用误配](https://huggingface.co/papers/2609.29050) ⭐️ 6.0/10

Hugging Face 每日论文提出 SLCA-GRPO，针对工具调用智能体在标准 GRPO 训练中的跨段信用误配问题。工具调用输出混合结构化调用与自然语言摘要，GRPO 将轨迹级标量优势无差别广播到所有 token，摘要生成的梯度噪声由此污染工具决策 token。SLCA-GRPO 引入 Segment-Locked Credit Assignment（SLCA）锁定分段信用，并构建 Schema-Guided LLM Simulator（SGLS）替代真实 API 以支撑可扩展探索。论文摘要被截断，尚无性能数据、代码或详细评估。

rss · Hugging Face Daily Papers · Sep 28, 00:00

**「为什么重要」** 工具调用智能体的 RL 训练长期面临输出异构带来的优化脆弱性，该论文将问题定位到 token 级的信用误配，为调试 GRPO 提供了具体切口。实际训练收益尚待论文完整数据验证。

**「可关注」** 可关注：若正在用 GRPO 训练工具调用智能体，需检查轨迹级优势是否将摘要生成的梯度噪声带入工具决策 token。

**Tags**: `#rl`, `#tool-calling`, `#agent-training`, `#orchestration`, `#coding-agent`

---

<a id="item-agent-engineer-8"></a>
### [2026 LLM 年度 keynote 回顾](https://simonwillison.net/2026/Sep/27/2026-in-llms-so-far/) ⭐️ 5.5/10

Simon Willison 在 WeAreDevelopers World Congress North America 闭幕 keynote 中，按时间线梳理 2026 年 LLM 关键事件。他将 2025 年 11 月 Claude Opus 4.5 与 GPT-5.1 的发布视为拐点：两者搭配 Claude Code、Codex 后，编码 agent 从“经常出错”变为“可日常可靠使用”。演讲还回顾 2025 年 11 月 24 日 steipete/Warelay 首次提交、12 月假期开发者的集中实践，以及他本人 2026 年“更激进”的年度目标。annotated slides 与视频已上线，内容以趋势索引为主，未提供可复现的评测数据。

rss · Simon Willison · Sep 27, 23:54

**「为什么重要」** 对 coding agent 与 harness 开发者，这场演讲给出 2026 年迄今的事件索引，可快速定位 Claude Code、Codex 等工具的关键节点。但材料是 keynote 综述，尚未包含生产环境 trace 或可复现 eval，实际影响需回到一手来源验证。

**「可关注」** 可关注：Willison 将 Claude Opus 4.5 与 GPT-5.1 视为编码 agent 日常可用的拐点，可作为 harness 对比基线；但他同时预测 2026 年 coding agent 安全可能出现“Challenger disaster”，且 sandboxing 尚未解决，落地时需区分能力提升与安全就绪。

**Tags**: `#coding-agent`, `#eval`, `#orchestration`, `#memory`

---

<a id="item-agent-engineer-9"></a>
### [Swift 1.5 + HyperQwen 提速 37%](https://www.reddit.com/r/LocalLLaMA/comments/1wsqjku/swift_15_hyperqwen_37_less_task_completion_time/) ⭐️ 5.5/10

Reddit 用户 KingGongzilla 将 Swift 1.0 与 Swift 1.5 适配到 HyperQwen，在单张 RTX 3090 24GB、FP8 KV cache、150k 上下文配置下，基于约 630 个任务对比了 HyperQwen 原版 W4A16 fast quant。Swift 1.5 INT4-heads 平均任务耗时 68.2 s，比原版 108.1 s 低约 37%；Swift 1.0 耗时 66.2 s，输出 token 最少。解码速度上，Swift 1.5 INT4-heads 为 107.2 tok/s，略低于原版 112.1 tok/s。耗时下降主要来自输出 token 数从 8,985 降至 5,669，而非吞吐提升。质量上，GSM8K、LiveCodeBench、工具调用等指标与原版基本持平，IFBench 略有下降。

reddit · r/LocalLLaMA · /u/KingGongzilla · Sep 28, 20:52

**「为什么重要」** 对在 24GB 显存上本地运行 coding agent 的工程师，这组数据说明端到端任务时间不只由解码吞吐决定，输出 token 数同样是关键变量。作者公开了适配后的 HuggingFace 模型集合与量化配置，可直接复现对比。

**「可关注」** 可关注：在单卡 RTX 3090 上做 agent 推理选型，除了比较 tok/s，还应比较平均输出 token 数；Swift 1.5 INT4-heads 以略低的解码速度换取了更短的任务完成时间。

**Tags**: `#eval`, `#local-inference`, `#quantization`

---

## AI Daily

<a id="item-ai-daily-1"></a>
### [Anthropic 联手 NVIDIA 管 Agent](https://claude.com/blog/giving-companies-more-control-over-their-ai-agents-with-nvidia) ⭐️ 9.8/10

NVIDIA 发布 Open Agent Safety Platform，Anthropic 参与合作。Claude Managed Agents 将凭证存入保险库，Agent 全程不可见。开源 NVIDIA OpenShell 负责约束执行范围，默认拒绝所有未授权操作。平台已上线，OpenShell 以 Apache 2.0 协议开源。

rss · Claude Blog · Sep 28, 00:00

**「为什么重要」** Agent 从答题转向执行业务动作，权限越大，外部约束越关键。该平台把模型内防护与模型外执行控制分层解耦，企业可逐层采纳。

**「可关注」** Managed Agents 的 Agent 循环与沙箱分离运行，凭证独立保险库托管；OpenShell 默认拒绝并记录每次工具调用，团队可从最小权限起步，用策略证明器数学校验可达范围。

**Tags**: `#lab`, `#industry`, `#product`, `#open-source`, `#policy`

---

<a id="item-ai-daily-2"></a>
### [AI 发现 24 个 Android 漏洞](https://github.blog/security/how-we-found-24-android-vulnerabilities-using-our-open-source-ai-security-agent/) ⭐️ 8.3/10

GitHub 博客介绍其开源 AI 安全 agent 发现 24 个 Android 漏洞。文章梳理了背后的定向 AI 任务流、发现的关键 Android 漏洞，以及如何在自己的 app 上运行同一开源 agent。目前仅公开摘要，具体漏洞细节、agent 名称与任务流实现尚未在材料中给出。

rss · GitHub Blog · Sep 28, 19:00

**「为什么重要」** 对做 coding agent 的人而言，这是一个可参考的 agent 任务流设计案例，展示了如何用定向任务流驱动 agent 完成真实漏洞挖掘。

**「可关注」** 可关注：文章公开的定向 AI 任务流，可直接用于在自己的 app 上运行同一开源 agent。

**Tags**: `#open-source`, `#industry`, `#product`, `#security`

---

<a id="item-ai-daily-3"></a>
### [OpenAI 500 万美元扩 Lenfest 计划](https://openai.com/index/lenfest-ai-collaborative-expansion) ⭐️ 6.8/10

OpenAI 宣布扩展 Lenfest AI Collaborative and Fellowship Program，新增 500 万美元资金，并提供至多 500 万美元的软件额度与工程支持。该公告来自 OpenAI 官方博客，属于慈善项目扩容，未涉及模型发布或 API 政策变化。软件额度与工程支持将如何分配、面向哪些机构，原文未进一步说明。

rss · OpenAI Blog · Sep 28, 07:00

**「可关注」** Lenfest 项目包含至多 500 万美元的 OpenAI 软件额度与工程支持，具体支持形式与覆盖范围尚未公开。

**Tags**: `#lab`, `#industry`

---

<a id="item-ai-daily-4"></a>
### [GPT-6 Astra 税务工作簿快 1 倍](https://openai.com/index/basis-tax-workbook-with-astra) ⭐️ 6.3/10

OpenAI 发布客户案例：Basis 用 GPT-6 Astra 处理 50 标签税务工作簿，耗时较 GPT-5.6 Sol 减半。官方称新模型对用户意图理解更强，Basis 在实际使用中信心更足。该案例为单一场景分享，未附独立测试数据。

rss · OpenAI Blog · Sep 28, 00:00

**「为什么重要」** 该案例给出 GPT-6 Astra 在 50 标签复杂工作簿上的具体提速数据，为评估长文档、多标签结构化任务提供了参考基线。

**「可关注」** 可关注：GPT-6 Astra 处理 50 标签税务工作簿的耗时较 GPT-5.6 Sol 减半，官方同时强调其用户意图理解增强；若你的场景涉及长文档表格解析，可纳入对比测试。

**Tags**: `#model`, `#product`, `#eval`, `#industry`

---

<a id="item-ai-daily-5"></a>
### [Highlights from Git 2.56](https://github.blog/open-source/git/highlights-from-git-2-56/) ⭐️ 6.3/10

GitHub 官方博客发布 Git 2.56 新特性亮点，介绍该版本的主要变化。

rss · GitHub Blog · Sep 28, 17:23

**Tags**: `#open-source`, `#product`, `#industry`

---

## AI Deals

<a id="item-ai-deals-1"></a>
### [OpenCode 与 Command Code $10 套餐额度翻 6 倍](https://www.appinn.com/opencode-vs-command-code-ai-coding-plans/) ⭐️ 7.0/10

OpenCode 与 Command Code 先后宣布，将 $10/月 套餐中的 DeepSeek V4.1 Flash 使用额度永久提升至 $60/月。OpenCode 对应 Go 套餐，Command Code 对应 GOAT 套餐，均为付费订阅加量，非免费额度。材料未提供官方领取页与详细限制说明。

rss · 小众软件 · Sep 28, 08:17

**「为什么重要」** $10 月费对应 $60 模型额度，额度为套餐价格的 6 倍。该提升为永久性，但仅限 OpenCode Go 与 Command Code GOAT 两个付费套餐，不构成免费额度。

**「可关注」** 可关注：若已在 OpenCode Go 或 Command Code GOAT 套餐内，DeepSeek V4.1 Flash 的月度可用额度已永久提升至 $60/月；未订阅者需先购买 $10/月 套餐，且材料未说明超额后的计费方式或速率限制。

**Tags**: `#promo`, `#credits`, `#api`

---