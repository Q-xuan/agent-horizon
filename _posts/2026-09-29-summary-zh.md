---
layout: default
title: "Horizon Summary: 2026-09-29 (ZH)"
date: 2026-09-29
lang: zh
---

> 从 210 条内容中筛选出 22 条重要资讯。

---

**Harness 架构**
1. [Codex rust-v0.158.0 发布](#item-harness-arch-1) ⭐️ 8.8/10
2. [MCP TypeScript SDK 1.31.0 发布](#item-harness-arch-2) ⭐️ 8.8/10
3. [MCP TS SDK v2.2.0 发布](#item-harness-arch-3) ⭐️ 8.3/10
4. [Kitesurf 更新：WebMCP 终端](#item-harness-arch-4) ⭐️ 8.3/10
5. [Claude Code v2.1.284 发布](#item-harness-arch-5) ⭐️ 6.8/10
6. [crewAI 1.15.23 发布](#item-harness-arch-6) ⭐️ 6.8/10
7. [langchain-fireworks 1.7.0 发布](#item-harness-arch-7) ⭐️ 6.3/10

**Agent 工程师日报**
1. [拆分 Prefill/Decode 的量化](#item-agent-engineer-1) ⭐️ 8.0/10
2. [AgentWorld 多智能体协作基准](#item-agent-engineer-2) ⭐️ 8.0/10
3. [Sonnet 5.5 发布：跑分差距源于回退率](#item-agent-engineer-3) ⭐️ 7.0/10
4. [Cloudflare agentic CLI](#item-agent-engineer-4) ⭐️ 7.0/10
5. [Holo4: powering generalist computer-use agents](#item-agent-engineer-5) ⭐️ 6.8/10
6. [Workers 原生运行 Rust 与 Tokio](#item-agent-engineer-6) ⭐️ 6.3/10
7. [SLCA-GRPO：修正工具调用信用误配](#item-agent-engineer-7) ⭐️ 6.0/10
8. [2026 LLM 年度 keynote](#item-agent-engineer-8) ⭐️ 5.5/10
9. [Swift 1.5 + HyperQwen 提速 37%](#item-agent-engineer-9) ⭐️ 5.5/10

**AI 日报**
1. [Anthropic 与 NVIDIA 管 Agent](#item-ai-daily-1) ⭐️ 9.8/10
2. [AI 发现 24 个 Android 漏洞](#item-ai-daily-2) ⭐️ 8.3/10
3. [OpenAI 扩展 Lenfest 计划](#item-ai-daily-3) ⭐️ 6.8/10
4. [Basis 用 GPT-6 Astra 处理税务工作簿快一倍](#item-ai-daily-4) ⭐️ 6.3/10
5. [Highlights from Git 2.56](#item-ai-daily-5) ⭐️ 6.3/10

**AI 羊毛**
1. [OpenCode、Command Code $10 套餐额度升至 $60](#item-ai-deals-1) ⭐️ 7.0/10

---

## Harness 架构

<a id="item-harness-arch-1"></a>
### [Codex rust-v0.158.0 发布](https://github.com/openai/codex/releases/tag/rust-v0.158.0) ⭐️ 8.8/10

Codex rust-v0.158.0 发布。MCP 服务器接入支持预注册 OAuth client secret，新增 \`codex mcp add --oauth-client-secret\` 参数。exec-server WebSocket 连接支持 bearer token 认证，app-server 配置路径同步覆盖。终端输入审批默认对提权命令开启，runtime-only grants 不再触发额外审查。沙盒修复涉及 Windows 10 路径、Linux 嵌套可写根及 macOS 路径别名。

github · github-actions\[bot\] · 9月28日 05:07

**「设计要点」** exec-server 将 WebSocket 认证抽离至 \`codex-websocket-auth\`，app-server 执行器连接同步支持 bearer token。审批策略默认收紧，提权命令强制终端输入确认，runtime-only grants 保留免审路径。

**「改了什么」** MCP 层新增 OAuth client-secret 配置入口；exec-server WebSocket 转为可选 bearer token 保护；终端审批默认覆盖提权命令；沙盒修复涉及 Windows 凭据、Linux 嵌套可写根和 macOS 路径别名识别。

**标签**: `#mcp`, `#permissions`, `#sandbox`, `#runtime`, `#tools`

---

<a id="item-harness-arch-2"></a>
### [MCP TypeScript SDK 1.31.0 发布](https://github.com/modelcontextprotocol/typescript-sdk/releases/tag/1.31.0) ⭐️ 8.8/10

MCP TypeScript SDK 发布 1.31.0，核心变更是把 OAuth 凭据绑定到颁发它的授权服务器。存储的令牌和客户端信息新增 \`issuer\` 字段，拒绝未知字段的存储后端需要放开该字段。构造 \`ClientCredentialsProvider\`、\`PrivateKeyJwtProvider\`、\`StaticPrivateKeyJwtProvider\` 时必须传入 \`expectedIssuer\`，否则标记为弃用。

github · felixweinberger · 9月28日 18:52

**「设计要点」** SDK 在 auth provider 层引入 issuer 绑定，防止跨授权服务器复用凭据。存储层需兼容新增的 \`issuer\` 字段，否则升级后会写入失败。

**「改了什么」** 1.30.1 到 1.31.0 之间，SDK 将 OAuth 凭据与颁发者绑定，并在三个 auth provider 中强制要求 \`expectedIssuer\` 参数。

**标签**: `#mcp`, `#permissions`, `#runtime`, `#tools`

---

<a id="item-harness-arch-3"></a>
### [MCP TS SDK v2.2.0 发布](https://github.com/modelcontextprotocol/typescript-sdk/releases/tag/v2.2.0) ⭐️ 8.3/10

MCP TypeScript SDK v2.2.0 发布，client、server、core、server-legacy、codemod 五个包同步升到 2.2.0。机器到机器 OAuth provider 构造时需传 \`expectedIssuer\`，否则弃用并告警；\`fetchToken\(\)\` 在发送前校验授权服务器绑定，不匹配抛 \`AuthorizationServerMismatchError\`。不带 cursor 的 \`listTools\(\)\`、\`listPrompts\(\)\`、\`listResources\(\)\`、\`listResourceTemplates\(\)\` 改为自动跟随 \`nextCursor\` 拉全量，\`listMaxPages\` 仍限制页数。

github · felixweinberger · 9月28日 19:24

**「设计要点」** OAuth 侧把授权服务器 issuer 绑定提前到 provider 构造与 \`fetchToken\(\)\` 调用前，避免把凭证发错服务器；列表调用默认全量翻页，harness 侧需按 \`listMaxPages\` 控制拉取规模。

**「改了什么」** 相对 2.1.0，OAuth provider 新增 \`expectedIssuer\` 绑定检查，列表 API 默认自动翻页到服务端停止下发 \`nextCursor\`。同时修复 CommonJS 项目类型检查、\`Client.listen\(\)\` 未处理拒绝与挂起、\`.localhost\` 回环判定等回归。

**标签**: `#mcp`, `#permissions`, `#tools`

---

<a id="item-harness-arch-4"></a>
### [Kitesurf 更新：WebMCP 终端](https://blog.cloudflare.com/kitesurf-update/) ⭐️ 8.3/10

Cloudflare 更新完全运行在 Workers 上的 agentic browser Kitesurf。本次加入 WebMCP 支持，网站可向 agent 直接暴露函数（如 searchFlights\(\)），取代模拟点击的脆弱交互。Kitesurf 同时补齐 Browser Run 全量 API，并新增终端渲染模式。WPT 子测试通过数达 730,000+，比发布时多 500,000。

rss · Cloudflare AI · 9月28日 13:00

**「设计要点」** Kitesurf 将 PageScript 与 PageRenderer 分离，前者在服务端 isolate 处理页面会话，后者负责生成像素。该设计允许把渲染逻辑外移到客户端或另一个 Worker，安全关键部分仍留在 Cloudflare 网络内。终端版即利用此分离，把 PageRenderer 移植到 Playground Worker，输出 Kitty 图形协议或纯 ANSI 文本。

**「改了什么」** 新增 WebMCP 支持，agent 可调用站点暴露的工具而非模拟点击；Browser Run 补齐 CDP、Playwright、Puppeteer、MCP 全量 API，Quick Actions 支持 Worker 内 env.BROWSER.quickAction\(\) 调用。引擎优化 Boa 与 Wasm DOM 边界，减少跨引擎往返并按需加载字体；同时发布终端版本，支持 Kitty 与 ANSI 渲染。

**标签**: `#runtime`, `#tools`, `#mcp`, `#sandbox`

---

<a id="item-harness-arch-5"></a>
### [Claude Code v2.1.284 发布](https://github.com/anthropics/claude-code/releases/tag/v2.1.284) ⭐️ 6.8/10

Claude Code v2.1.284 将 Claude Sonnet 5.5（\`claude-sonnet-5-5\`）设为默认 Sonnet 模型，提供 1M 上下文，输入 $2/Mtok、输出 $10/Mtok，缓存读 $0.20/Mtok。自动模式在读取工作目录之外文件前新增“Yes, but ask again next time”，允许单次读取并保留后续询问。交互终端加入 \`/mcp reconnect all\`，可一次性重连所有连接失败或待认证的 MCP server。Claude apps gateway 增加支出上限金额展示、Google OTLP 遥测转发和 \`private\_key\_jwt\` 证书认证，并在托管策略 \`availableModels\` 为空或缺失启动模型时给出启动警告。

github · ashwin-ant · 9月28日 18:02

**「设计要点」** auto mode 将越目录读取的授权拆成单次放行与后续重问，权限粒度更细；MCP 层新增 \`/mcp reconnect all\` 批量重连，gateway 支持 Google OTLP 遥测和 \`private\_key\_jwt\` 证书认证。

**「改了什么」** 默认模型切到 Sonnet 5.5；auto mode 越目录读取可单次放行；\`/mcp reconnect all\` 上线；gateway 支出上限显示金额并支持 Google OTLP 与证书认证；\`/effort\` 滑块键位可重绑定。

**标签**: `#permissions`, `#tools`, `#mcp`, `#runtime`

---

<a id="item-harness-arch-6"></a>
### [crewAI 1.15.23 发布](https://github.com/crewAIInc/crewAI/releases/tag/1.15.23) ⭐️ 6.8/10

crewAI 1.15.23 发布。新增 Gemini 3.8 Flash 原生支持。评测与追踪工作流调整：crewai eval 记录最后追踪运行并通过 AMP 评估，CLI 打印评估区域。修复 LLM 限流重试、Bedrock 同步回退、SQLite 连接关闭等运行时问题。

github · lorenzejay · 9月28日 21:14

**「设计要点」** 运行时侧重调用韧性与资源清理：LLM 限流自动重试，Bedrock acall 失败回退同步，SQLite 连接与 S3 响应体显式关闭。追踪层将 task span 扩展至输出格式与结果，TUI 接入 tracing 开关与 Evaluate 按钮。

**「改了什么」** 新增 Gemini 3.8 Flash 原生支持；eval 改为记录并评估最后追踪运行；修复 LLM 限流重试、Bedrock 同步回退、SQLite 连接泄漏等运行时缺陷。

**标签**: `#runtime`, `#tools`, `#eval`

---

<a id="item-harness-arch-7"></a>
### [langchain-fireworks 1.7.0 发布](https://github.com/langchain-ai/langchain/releases/tag/langchain-fireworks%3D%3D1.7.0) ⭐️ 6.3/10

langchain-fireworks 1.7.0 发布。相对 1.6.3，新增 prompt caching middleware，支持 prefix-cache；同时修复 mid-stream read timeout 的分类错误。发布还替换了不可用的集成测试模型，并刷新 model profile 数据。

github · github-actions\[bot\] · 9月28日 20:46

**「设计要点」** prompt caching middleware 提供 prefix-cache 能力；mid-stream read timeout 分类修复调整流式响应期的错误识别。

**「改了什么」** 新增 prompt caching middleware。修复 mid-stream read timeouts 分类。替换不可用的集成测试模型。刷新 model profile 数据。

**标签**: `#prefix-cache`, `#runtime`, `#tools`

---

## Agent 工程师日报

<a id="item-agent-engineer-1"></a>
### [拆分 Prefill/Decode 的量化](https://huggingface.co/papers/2609.26333) ⭐️ 8.0/10

一篇 HF 论文提出 disaggregated quantization（DQ），把 prefill 和 decode 的量化策略拆开：prefill 用低精度计算加速 prompt 处理，decode 用紧凑权重降低显存 traffic。在 Qwen 3 和 Gemma 3 上，decode 阶段移除 activation quantization，在不增加推理成本的情况下提升 decode-heavy 任务准确率。训练独立的 compute-native prefill 权重后，prompt 处理速度超过 weight-only inference，并在 2–3-bit decode 下持平或超过其准确率。作者发布了 Qwen3.8-27B GGUF decoder，称训练 NVFP4 prefiller 可将 1-bit 准确率提升 32.5 个百分点。

rss · Hugging Face Daily Papers · 9月28日 00:00

**「为什么重要」** 对做 coding agent 和 harness 的人来说，prefill 吃算力、decode 吃显存带宽，两者优化目标不同。DQ 提供了一种不换模型、只按阶段拆分量化配置的思路，可能影响长上下文 agent 的推理成本结构。

**「可关注」** 可关注：decode 阶段关闭 activation quantization 能在零成本下换取准确率，这为现有 GGUF/量化部署提供了一个低风险调优点；同时 prefill 与 decode 使用不同权重格式，意味着 serving 栈需要同时管理两套权重布局。

**标签**: `#inference`, `#quantization`, `#llm-serving`, `#performance`

---

<a id="item-agent-engineer-2"></a>
### [AgentWorld 多智能体协作基准](https://huggingface.co/papers/2609.31590) ⭐️ 8.0/10

2026-09-28，Hugging Face Daily Papers 发布 AgentWorld 基准，针对现有评测多在竞争环境、20 步以内短程交互或仅聚合个体表现的短板，转向长程多智能体协作。该基准含 100 个人工标注任务与 100 个增强变体，任务在 MMORPG 沙盒中跨越 50+ 轮交互，要求 3-20 个异构角色通过通信、联合规划和资源共享完成协调，且处于黑盒设置：每个智能体独立行动，无法访问其他智能体内部状态。论文提出在二元任务成功之外量化协作有效性的指标，但材料未展示具体指标定义。该基准面向 Agent 工程师的 eval 与 orchestration 工具体系。

rss · Hugging Face Daily Papers · 9月28日 00:00

**「为什么重要」** 现有基准难以分离 LLM 智能体的真实协作能力，AgentWorld 把长程交互、异构角色和黑盒通信纳入统一沙盒，为 eval 与 orchestration 工具提供了新的测量维度。该基准能否成为行业标准尚未证实，但其任务设计直接回应了多智能体协作评测的空白。

**「可关注」** 可关注：AgentWorld 在黑盒条件下要求 3-20 个异构智能体仅通过通信、联合规划和资源共享完成 50+ 轮协调，这对 orchestration 工具在无法访问智能体内部状态时的长程协同设计构成了直接压力。

**标签**: `#eval`, `#orchestration`, `#multi-agent`, `#benchmark`

---

<a id="item-agent-engineer-3"></a>
### [Sonnet 5.5 发布：跑分差距源于回退率](https://www.anthropic.com/claude-sonnet-5-5) ⭐️ 7.0/10

Anthropic 发布 Sonnet 5.5。HN 用户指出，该模型 Terminal-Bench 得 70.6 分，高于 Opus 5.5 的 66.4 分；但援引 Sonnet 5.5 System Card 第 8.5 节，Opus 5.5 有 10% 试验因安全防护回退到备用模型，Sonnet 5.5 回退率为 1.5%，跑分差距可能源于回退率差异。讨论中还提到，Sonnet 5.5 网络安全能力较 Sonnet 5 提升，因此采用与 Opus 5.5 相近的安全防护，高风险网络安全任务会回退到 Sonnet 5。

hackernews · D2OQZG8l5BI1S06 · 9月28日 17:58 · [社区讨论](https://news.ycombinator.com/item?id=49881850)

**「为什么重要」** 对 agent 工程师而言，模型跑分差异可能来自安全回退率而非纯能力差距，评估时需区分模型本身表现与安全策略影响。同时，安全防护导致的任务回退会直接影响 agent 在高风险场景的可用性。

**「可关注」** 可关注：对比模型 Terminal-Bench 成绩时，需核查 System Card 中的安全回退率，避免将策略差异误读为能力差异；生产环境中应预期高风险网络安全任务可能触发回退到旧版本模型。

**「评论」** 用户 simonw 反馈 Sonnet 5.5 在 max thinking effort 下耗尽 128,000 thinking tokens（耗时 15 分钟）仍未产出最终 SVG，与 Opus 5.5 表现一致。另有用户认为在 5x 订阅计划下 Opus 5.5 效率已足够日常使用，Sonnet 5.5 更适用于高并发或结果导向的 web/前端任务。

**标签**: `#coding-agent`, `#eval`, `#observability`, `#permissions`

---

<a id="item-agent-engineer-4"></a>
### [Cloudflare agentic CLI](https://blog.cloudflare.com/cloudflare-cf-cli-launch/) ⭐️ 7.0/10

2026 年 9 月 28 日，Cloudflare 发布 agentic CLI \`cf\`，用于操作 Cloudflare API。该工具以 TypeScript 编写，配置格式同样基于 TypeScript。官方工程博客放出这一消息，Hacker News 讨论集中在 CLI 架构与 agent 可发现性。

hackernews · macleos · 9月28日 15:28 · [社区讨论](https://news.ycombinator.com/item?id=49879577)

**「为什么重要」** 云厂商开始把 API 封装成 agent 友好的 CLI，并直接讨论配置格式与可发现性。对做 coding agent / harness 的人来说，这是工具链从“给人用的命令”转向“给 agent 用的接口”的一个实例。

**「可关注」** 可关注：Cloudflare 选择 TypeScript 作为实现和配置格式，社区出现分歧——slowin 认为应使用编译语言以避免用户管理依赖，bhouston 则建议支持 opencli 规范来提升 agent 可发现性。

**「评论」** 评论出现分歧：slowin 质疑 TypeScript 选型，认为应使用编译语言避免用户管理依赖；bhouston 建议支持 clidoc.dev 等 opencli 规范以提升可发现性；vamsiraju 对 TypeScript 配置格式感到困惑。

**标签**: `#coding-agent`, `#orchestration`, `#harness`

---

<a id="item-agent-engineer-5"></a>
### [Holo4: powering generalist computer-use agents](https://huggingface.co/blog/Hcompany/holo4) ⭐️ 6.8/10

Hugging Face blog announces Holo4, a new generalist computer-use agent model series \(27B dense and 35B-A3B MoE\) that supports GUIs, code, MCP, and APIs, with released trajectories and datasets.

rss · Hugging Face Blog · 9月28日 09:44

**标签**: `#coding-agent`, `#mcp`, `#eval`, `#observability`

---

<a id="item-agent-engineer-6"></a>
### [Workers 原生运行 Rust 与 Tokio](https://blog.cloudflare.com/rust-workers-emscripten-target/) ⭐️ 6.3/10

2026 年 9 月 28 日，Cloudflare 发布 wasm-bindgen 的 Emscripten 目标实验性预览，新增 wasm32-unknown-emscripten 编译器目标。Rust 代码与 Tokio 异步应用可在 Workers 上原生运行，借助 Node.js 兼容层虚拟化定时器、文件系统与套接字，库兼容性显著提升。官方示例中，Rust 版 Minecraft 服务器 Pumpkin 已在 Durable Object 内通过 Tokio 使用真实 TCP 套接字。该功能仍处预发布，libc、socket2、Mio 等底层库需打补丁，Tokio 支持补丁仅部分合入上游。

rss · Cloudflare Engineering · 9月28日 13:00

**「为什么重要」** 这降低了 Rust 生态向 Workers 迁移的门槛，尤其是依赖 Tokio 与系统级套接字的服务端应用。已发生的变化是工具链打通与示例验证；对通用 agent 工程的实际影响仍待更多采用数据。

**「可关注」** Emscripten 目标通过 Node.js 兼容层虚拟化原生平台能力，使 Tokio 阻塞语义得以在单线程 JS 事件循环中运行，但 JSPI 栈切换与线程本地运行时上下文存在冲突，完全可重入需要细致的线程本地处理。

**标签**: `#toolchain`, `#wasm`, `#cloudflare`

---

<a id="item-agent-engineer-7"></a>
### [SLCA-GRPO：修正工具调用信用误配](https://huggingface.co/papers/2609.29050) ⭐️ 6.0/10

Hugging Face 每日论文 2026-09-28 收录 SLCA-GRPO，针对工具调用智能体在 GRPO 训练中的跨段信用误配提出修正。论文指出，工具调用输出混合结构化调用与自然语言摘要，GRPO 将轨迹级标量优势无差别广播到所有 token，导致摘要生成的梯度噪声污染工具决策 token。SLCA-GRPO 引入 Segment-Locked Credit Assignment（SLCA），并构建 Schema-Guided LLM Simulator（SGLS）作为训练基础设施，以避免昂贵真实 API 调用。当前材料为截断摘要，缺少性能数据、代码与详细评估，实际效果待验证。

rss · Hugging Face Daily Papers · 9月28日 00:00

**「为什么重要」** 该工作指认了 GRPO 在工具调用场景下的具体结构缺陷，对做 agent 训练与工具编排的工程师有直接参考价值。但论文尚未提供可验证的性能数据或代码，实际收益仍不确定。

**「可关注」** 可关注：若你的工具调用 agent 采用 GRPO 类 on-policy RL，需检查轨迹级优势是否均匀分配到工具调用与摘要 token，避免梯度串扰；SLCA 与 SGLS 提供了一种分段锁定与模拟器解耦的思路，但落地前需等待完整评估。

**标签**: `#rl`, `#tool-calling`, `#agent-training`, `#orchestration`, `#coding-agent`

---

<a id="item-agent-engineer-8"></a>
### [2026 LLM 年度 keynote](https://simonwillison.net/2026/Sep/27/2026-in-llms-so-far/) ⭐️ 5.5/10

Simon Willison 于 9 月 25 日在 WeAreDevelopers World Congress North America 发表闭幕演讲，按时间线梳理 2026 年 LLM 关键事件，并公开 annotated slides。他将 2025 年 11 月 Claude Opus 4.5 与 GPT-5.1 的发布视为拐点：两者搭配 Claude Code 和 Codex 后，编码能力从“经常出错”提升到“可日常使用”。演讲还回顾了 2025 年 12 月假期开发者的实践热潮，以及 2026 年 1 月行业将编码 agent 投入使用的转向。他本人将 2026 年主题定为“更激进”，主张不断试探技术边界。

rss · Simon Willison · 9月27日 23:54

**「为什么重要」** 这份 keynote 把 2026 年至今的模型发布、harness 成熟度与开发者行为变化按时间线串联，为 coding agent 从业者提供了一份一线实践者视角的年度索引。它不包含可复现的 eval 数据或生产 trace，更适合作为回溯一手资料的目录，而非直接的技术决策依据。

**「可关注」** 可关注：2025 年 11 月的模型更新让编码 agent 跨过日常可用线，Simon Willison 据此把 2026 年主题定为“更激进”，主张持续试探技术边界。

**标签**: `#coding-agent`, `#eval`, `#orchestration`, `#memory`

---

<a id="item-agent-engineer-9"></a>
### [Swift 1.5 + HyperQwen 提速 37%](https://www.reddit.com/r/LocalLLaMA/comments/1wsqjku/swift_15_hyperqwen_37_less_task_completion_time/) ⭐️ 5.5/10

Reddit 用户 /u/KingGongzilla 将 Swift 1.0 与 Swift 1.5 适配到 HyperQwen，在单张 RTX 3090 24GB、FP8 KV cache、150k 上下文下用约 630 个任务测试。Swift 1.5 INT4-heads 平均耗时 68.2 秒，比 HyperQwen 原版 W4A16 AutoRound fast quant 的 108.1 秒低约 37%，解码 107.2 tok/s；Swift 1.0 耗时最短（66.2 秒），输出 token 从 8,985 降至 5,245。质量上 GSM8K、LiveCodeBench、工具调用与基线接近，IFBench 从 74.0% 降至 72.3%，困惑度从 6.551 升至 6.679。

reddit · r/LocalLLaMA · /u/KingGongzilla · 9月28日 20:52

**「为什么重要」** 本地部署 coding agent 时，任务总耗时由解码速度和输出 token 数共同决定。该测试显示 Swift 微调生成更少 token，在解码速度略低的情况下仍将任务时间缩短约 37%，为 RTX 3090 24GB 场景下的模型选型提供了具体数据。

**「可关注」** 在 24GB 显存下评估本地模型时，除解码 tok/s 外，平均输出 token 数会显著影响任务总耗时；Swift 1.5 INT4-heads 通过 GPTQ INT4 输出头与 65,536-token draft vocabulary 实现了约 37% 的任务提速。

**标签**: `#eval`, `#local-inference`, `#quantization`

---

## AI 日报

<a id="item-ai-daily-1"></a>
### [Anthropic 与 NVIDIA 管 Agent](https://claude.com/blog/giving-companies-more-control-over-their-ai-agents-with-nvidia) ⭐️ 9.8/10

NVIDIA 发布 Open Agent Safety Platform，Anthropic 参与合作，将 Claude Managed Agents 与开源的 NVIDIA OpenShell 整合。Managed Agents 把凭证放在独立保险库，agent 运行在隔离沙箱，接触不到密码和密钥。OpenShell 是开源安全运行时，默认阻止一切动作，只有规则放行才执行，并记录每次允许或拦截。平台分层设计，各层独立执行限制，企业可按需选用。

rss · Claude Blog · 9月28日 00:00

**「为什么重要」** 企业正从让 AI 答题转向部署 agent 处理跨部门复杂任务，agent 拿到的权限越多，公司越需要管住和审计它的行为。该平台把控制点放在模型之外，不依赖模型自身的安全对齐。

**「可关注」** 可关注：OpenShell 的 policy prover 用数学证明确认 agent 在既定规则下的可达范围，团队可从窄权限起步，依据日志逐步收紧到最小必要。

**标签**: `#lab`, `#industry`, `#product`, `#open-source`, `#policy`

---

<a id="item-ai-daily-2"></a>
### [AI 发现 24 个 Android 漏洞](https://github.blog/security/how-we-found-24-android-vulnerabilities-using-our-open-source-ai-security-agent/) ⭐️ 8.3/10

GitHub 发布博客，介绍其开源 AI 安全 agent 如何发现 24 个 Android 漏洞。文章拆解了背后的定向 AI 任务流，并说明如何在自有应用上复现同一套 agent。目前披露的细节集中在任务流设计与漏洞案例，尚未给出漏洞严重级别分布或修复状态。

rss · GitHub Blog · 9月28日 19:00

**「为什么重要」** 该 agent 开源且任务流公开，工程师可将其用于自有 Android 应用的安全自查。

**「可关注」** 可关注：GitHub 公开的定向 AI 任务流，以及复现到自有应用的具体步骤。

**标签**: `#open-source`, `#industry`, `#product`, `#security`

---

<a id="item-ai-daily-3"></a>
### [OpenAI 扩展 Lenfest 计划](https://openai.com/index/lenfest-ai-collaborative-expansion) ⭐️ 6.8/10

OpenAI 宣布扩展 Lenfest AI Collaborative 与 Fellowship Program。新增 500 万美元资金，以及最多 500 万美元的软件额度与工程支持。这是慈善项目扩容，不是模型发布或政策变更。

rss · OpenAI Blog · 9月28日 07:00

**「可关注」** Lenfest AI Collaborative 与 Fellowship Program 获得 OpenAI 的软件额度与工程支持，资金与额度合计最高 1000 万美元。

**标签**: `#lab`, `#industry`

---

<a id="item-ai-daily-4"></a>
### [Basis 用 GPT-6 Astra 处理税务工作簿快一倍](https://openai.com/index/basis-tax-workbook-with-astra) ⭐️ 6.3/10

OpenAI 发布客户案例，Basis 用 GPT-6 Astra 处理 50 个标签页的税务工作簿，速度比 GPT-5.6 Sol 快一倍。案例称 GPT-6 Astra 对用户意图理解更强，Basis 在实际使用中更有信心。目前仅公开单一场景对比，未披露测试环境与更多细节。

rss · OpenAI Blog · 9月28日 00:00

**「为什么重要」** 这是 GPT-6 Astra 在专业长文档场景的公开对比数据，可作为类似任务选型参考。但样本有限，不能推广到所有工作流。

**「可关注」** 可关注：GPT-6 Astra 在 50 个标签页税务工作簿上比 GPT-5.6 Sol 快一倍，且对用户意图理解更强。

**标签**: `#model`, `#product`, `#eval`, `#industry`

---

<a id="item-ai-daily-5"></a>
### [Highlights from Git 2.56](https://github.blog/open-source/git/highlights-from-git-2-56/) ⭐️ 6.3/10

GitHub 官方博客发布 Git 2.56 新特性亮点，介绍该版本的主要变化。

rss · GitHub Blog · 9月28日 17:23

**标签**: `#open-source`, `#product`, `#industry`

---

## AI 羊毛

<a id="item-ai-deals-1"></a>
### [OpenCode、Command Code $10 套餐额度升至 $60](https://www.appinn.com/opencode-vs-command-code-ai-coding-plans/) ⭐️ 7.0/10

OpenCode 与 Command Code 先后宣布，将 $10/月套餐中的 DeepSeek V4.1 Flash 使用额度永久提升至 $60/月。OpenCode 的 Go 套餐与 Command Code 的 GOAT 套餐均包含此项调整。材料未提及额外领取条件与截止时间。

rss · 小众软件 · 9月28日 08:17

**「为什么重要」** 同价位套餐的模型额度竞争加剧，$10 档位的 DeepSeek V4.1 Flash 配额被拉高至 $60/月。

**「可关注」** 可关注：OpenCode Go 与 Command Code GOAT 套餐的 DeepSeek V4.1 Flash 月度额度已提升至 $60/月；材料未说明详细使用限制。

**标签**: `#promo`, `#credits`, `#api`

---