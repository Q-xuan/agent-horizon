---
layout: default
title: "Horizon Summary: 2026-09-29 (ZH)"
date: 2026-09-29
lang: zh
---

> 从 184 条内容中筛选出 21 条重要资讯。

---

**Harness 架构**
1. [openai/codex released rust-v0.158.0](#item-harness-arch-1) ⭐️ 8.3/10
2. [MCP TS SDK v2.2.0 发布](#item-harness-arch-2) ⭐️ 8.3/10
3. [modelcontextprotocol/typescript-sdk released 1.31.0](#item-harness-arch-3) ⭐️ 8.3/10
4. [Claude Code v2.1.284 发布](#item-harness-arch-4) ⭐️ 7.8/10
5. [Kitesurf 支持 WebMCP](#item-harness-arch-5) ⭐️ 7.3/10
6. [Fireworks 集成 1.7.0 发布](#item-harness-arch-6) ⭐️ 6.8/10
7. [LangChain 1.4.3 发布](#item-harness-arch-7) ⭐️ 5.8/10

**Agent 工程师日报**
1. [CIS 修正 RLVR 训练推理失配](#item-agent-engineer-1) ⭐️ 8.0/10
2. [llm-anthropic 0.30 发布](#item-agent-engineer-2) ⭐️ 7.8/10
3. [TraceDance 用部署轨迹构建行为基准](#item-agent-engineer-3) ⭐️ 7.5/10
4. [EMem-Bench 发布具身记忆基准](#item-agent-engineer-4) ⭐️ 7.5/10
5. [Supporting native Rust in Workers with the new Emscripten target for wasm-bindgen](#item-agent-engineer-5) ⭐️ 6.8/10
6. [Holo4 发布：27B 与 35B-A3B](#item-agent-engineer-6) ⭐️ 6.3/10
7. [Sonnet 5.5 分数受回退率干扰](#item-agent-engineer-7) ⭐️ 6.0/10
8. [Claude Sonnet 5.5 发布](#item-agent-engineer-8) ⭐️ 6.0/10
9. [Claude Code’s Next Era — Thariq Shihipar, Anthropic](#item-agent-engineer-9) ⭐️ 6.0/10
10. [HF daily paper: AdaTutoRank: Learning to Rerank Document Sets via Adaptive Tutoring Optimization for RAG and Deep Research](#item-agent-engineer-10) ⭐️ 5.5/10

**AI 日报**
1. [OpenAI 就澳政府网站事件致歉](#item-ai-daily-1) ⭐️ 8.8/10
2. [GitHub 开源 AI 安全代理发现 24 个 Android 漏洞](#item-ai-daily-2) ⭐️ 7.3/10
3. [OpenAI 扩展 Lenfest 项目](#item-ai-daily-3) ⭐️ 6.8/10

**AI 羊毛**
1. [OpenCode、Command Code 送 6 倍 DeepSeek 额度](#item-ai-deals-1) ⭐️ 7.0/10

---

## Harness 架构

<a id="item-harness-arch-1"></a>
### [openai/codex released rust-v0.158.0](https://github.com/openai/codex/releases/tag/rust-v0.158.0) ⭐️ 8.3/10

Codex Rust v0.158.0 adds MCP OAuth client-secret support, bearer-token-secured exec-server WebSockets, sandbox fixes, and stricter default terminal approval for elevated commands.

github · github-actions\[bot\] · 9月28日 05:07

**标签**: `#mcp`, `#sandbox`, `#permissions`, `#tools`, `#runtime`

---

<a id="item-harness-arch-2"></a>
### [MCP TS SDK v2.2.0 发布](https://github.com/modelcontextprotocol/typescript-sdk/releases/tag/v2.2.0) ⭐️ 8.3/10

MCP TypeScript SDK v2.2.0 发布。OAuth 机器对机器提供商强制传入 expectedIssuer，fetchToken\(\) 在发送请求前校验授权服务器归属，不匹配即抛 AuthorizationServerMismatchError。无 cursor 的 listTools\(\)、listPrompts\(\)、listResources\(\)、listResourceTemplates\(\) 自动跟随 nextCursor 拉全量列表，listMaxPages 仍限制页数。同时修复 CommonJS 项目类型检查、Client.listen\(\) 未处理拒绝与挂起、input\_required 结果丢失 \_meta 等问题。

github · felixweinberger · 9月28日 19:24

**「设计要点」** OAuth 层引入 issuer 绑定校验，阻止跨授权服务器误用凭证；列表调用将分页循环下沉到 SDK，隐藏 cursor 细节但保留 listMaxPages 上限。

**「改了什么」** OAuth 提供商构造参数收紧，新增授权服务器不匹配错误；四个 list 方法默认行为从单次请求改为自动翻页；修复 2.1.0 引入的 CommonJS 类型检查回归。

**标签**: `#mcp`, `#permissions`, `#tools`, `#runtime`

---

<a id="item-harness-arch-3"></a>
### [modelcontextprotocol/typescript-sdk released 1.31.0](https://github.com/modelcontextprotocol/typescript-sdk/releases/tag/1.31.0) ⭐️ 8.3/10

MCP TypeScript SDK 1.31.0 binds stored OAuth credentials to their issuing authorization server and deprecates provider construction without expectedIssuer.

github · felixweinberger · 9月28日 18:52

**标签**: `#mcp`, `#permissions`, `#auth`

---

<a id="item-harness-arch-4"></a>
### [Claude Code v2.1.284 发布](https://github.com/anthropics/claude-code/releases/tag/v2.1.284) ⭐️ 7.8/10

Claude Code v2.1.284 将默认 Sonnet 模型切换为 \`claude-sonnet-5-5\`，提供 1M 上下文与 $2/$10 per Mtok 定价。自动模式在工作目录外读取前新增 &quot;Yes, but ask again next time&quot; 选项，细化单次授权与持续询问的边界。\`/usage\` 与状态行新增美元金额追踪，\`rate\_limits.spend\_limit\` 扩展 \`used\_usd\`、\`limit\_usd\` 和 \`period\` 字段。MCP 层加入 \`/mcp reconnect all\`，可一次性重试所有连接失败或待认证的服务器。

github · ashwin-ant · 9月28日 18:02

**「设计要点」** 权限层在 auto mode 中引入可复用的单次读授权，避免全量放开工作目录外访问。工具层为 MCP 增加批量重连入口，Gateway 侧支持 \`private\_key\_jwt\` 证书认证与 Google Cloud OTLP 遥测导出，分别减少会话恢复失败并扩展企业接入。

**「改了什么」** 默认模型切换为 Sonnet 5.5，auto mode 读权限支持单次授权，\`/usage\` 与状态行展示美元额度，MCP 增加批量重连，Gateway 支持证书认证与 Google OTLP 导出。

**标签**: `#runtime`, `#tools`, `#permissions`, `#mcp`

---

<a id="item-harness-arch-5"></a>
### [Kitesurf 支持 WebMCP](https://blog.cloudflare.com/kitesurf-update/) ⭐️ 7.3/10

Cloudflare 更新全 Workers 运行的 agentic browser Kitesurf，新增 WebMCP 支持，网站可向 agent 直接暴露 searchFlights\(\) 等函数工具，替代模拟点击。Kitesurf 现已完整覆盖 Browser Run API，支持 CDP、Playwright、Puppeteer、MCP，并可在 Worker 内通过 env.BROWSER.quickAction\(\) 调用 Quick Actions。团队将 PageRenderer 迁至 Playground Worker，支持 Kitty 终端图形协议与 ANSI 文本模式，可通过 brew install 在终端渲染页面。WPT 子测试通过量达 730,000+，较发布时增加 500,000。

rss · Cloudflare AI · 9月28日 13:00

**「设计要点」** Kitesurf 将 PageScript 与 PageRenderer 分离：PageScript 在服务端 isolate 处理页面会话与代码，PageRenderer 负责生成像素，可移到客户端或另一个 Worker。安全关键部分留在 Cloudflare 网络内，渲染数据外流，类似 Browser Isolation 的边缘隔离模型。

**「改了什么」** 相比 8 月首发，Kitesurf 新增 WebMCP、URL 模块解析、JSON 模块与 import map 支持，iframe 加载与隔离更稳定；Boa 与 Wasm DOM 之间的边界减少跨引擎往返，getAttribute、id、parentNode 等常见读取直接在 Wasm DOM 内完成。Quick Actions 从仅 REST API 扩展到 Worker 绑定，PageRenderer 外移后新增终端渲染能力。

**标签**: `#runtime`, `#tools`, `#mcp`

---

<a id="item-harness-arch-6"></a>
### [Fireworks 集成 1.7.0 发布](https://github.com/langchain-ai/langchain/releases/tag/langchain-fireworks%3D%3D1.7.0) ⭐️ 6.8/10

langchain-fireworks 1.7.0 发布，相对 1.6.3 新增 prompt caching middleware，并修正 mid-stream read timeout 的分类错误。同时替换了不可用的集成测试模型，刷新 model profile 数据。该更新属于合作方集成包范围，未改动核心 harness 架构。

github · github-actions\[bot\] · 9月28日 20:46

**「设计要点」** prompt caching middleware 直接介入前缀缓存命中路径，影响 agent 运行时中重复 prompt 的 token 成本。mid-stream read timeout 分类修正区分流式响应中的网络中断与模型端超时，便于上层做重试或降级决策。

**「改了什么」** 新增 prompt caching middleware，支持在 Fireworks 模型调用中启用提示缓存。修复流式读取超时被误分类的问题，提升错误可观测性。另替换失效的集成测试模型并刷新模型档案数据。

**标签**: `#prefix-cache`, `#runtime`, `#tools`

---

<a id="item-harness-arch-7"></a>
### [LangChain 1.4.3 发布](https://github.com/langchain-ai/langchain/releases/tag/langchain%3D%3D1.4.3) ⭐️ 5.8/10

LangChain 发布 1.4.3 补丁。\`init\_chat\_model\` 新增 Bedrock Mantle 聊天模型支持。修复 \`create\_agent\` 无效工具调用与 fallback 模型缓存设置错误。GPT-6 结构化输出可在无 profile 时识别。anyio 升级至 4.14.2。

github · github-actions\[bot\] · 9月28日 20:17

**「设计要点」** 模型接入层扩展至 Bedrock Mantle，Agent 工具调用链路修复，fallback 路径增加缓存设置清理。

**「改了什么」** \`init\_chat\_model\` 支持 Bedrock Mantle 聊天模型。\`create\_agent\` 修复无效工具调用。fallback 模型缓存设置得到清理。GPT-6 结构化输出无需 profile 识别。anyio 从 4.11.0 升至 4.14.2。

**标签**: `#runtime`, `#tools`

---

## Agent 工程师日报

<a id="item-agent-engineer-1"></a>
### [CIS 修正 RLVR 训练推理失配](https://huggingface.co/papers/2609.32444) ⭐️ 8.0/10

2026 年 9 月 29 日，Hugging Face Daily Papers 收录一篇论文，研究 RLVR 中训练引擎与推理引擎对同一 token 赋予不同概率造成的失配。论文提出校准重要性采样（CIS），依据是一项经验支持的 logit 位移刻画：失配可表示为 softmax 前逐 logit 扰动在 log-odds 上的加性位移 ε\_t，且该位移分布近似不随 token 置信度变化。由此作者设计置信度感知截断，对较大正位移进行截断；具体截断阈值在提供的材料中未完整给出。该方法面向 Agent 训练链路，提供可复现的方法论改进。

rss · Hugging Face Daily Papers · 9月29日 00:00

**「为什么重要」** RLVR 的 rollout 由推理引擎采样、梯度由训练引擎计算，两者概率不一致会直接影响策略更新。论文用可解释的 logit 位移刻画这一差异，并给出对应修正，对从事 Agent 训练、评测与基础设施工程的读者具有直接技术参考价值。

**「可关注」** 可关注：在自建或对比 RLVR 训练栈时，可将训练引擎与推理引擎的 token 概率差异作为独立排查项，并参考 CIS 的 logit 位移与置信度感知截断思路，而非仅调整奖励或超参数。

**标签**: `#eval`, `#harness`, `#coding-agent`

---

<a id="item-agent-engineer-2"></a>
### [llm-anthropic 0.30 发布](https://github.com/simonw/llm-anthropic/releases/tag/0.30) ⭐️ 7.8/10

2026-09-28，simonw/llm-anthropic 发布 0.30 版本，新增 Claude Sonnet 5.5 支持。插件加入 \`llm anthropic refresh\` 与 \`llm anthropic models\` 命令，从 Anthropic models API 拉取可用模型并缓存到 \`anthropic\_models.json\`，对未知模型按 API 回报的能力注册，包括图像与 PDF 输入、\`thinking\`、\`effort\`、结构化输出和最大输出 token。新增 \`llm anthropic count\` 命令，通过 token counting API 在不执行 prompt 的情况下统计输入 token，接受与 \`llm prompt\` 相同的参数，Python 侧提供 \`model.count\_tokens\(\)\`。修复了对话中遇到拒绝后，后续 prompt 报 400 错误的问题。

github · simonw · 9月28日 23:06

**「为什么重要」** Token 计数和模型发现为调用前估算输入 token 提供了直接手段，有助于控制上下文预算与成本；模型缓存让 harness 能及时识别新模型及其能力边界。

**「可关注」** 可关注：\`llm anthropic count\` 支持 \`-c\` 统计会话中后续 prompt 的 token，可在多轮 agent 流程中做预检。

**标签**: `#harness`, `#observability`, `#coding-agent`

---

<a id="item-agent-engineer-3"></a>
### [TraceDance 用部署轨迹构建行为基准](https://huggingface.co/papers/2609.33295) ⭐️ 7.5/10

TraceDance 是一个自动化系统，从真实部署轨迹构建针对特定不良行为的 agent 基准。Anchor-and-Confirm 结合可编程检索与 Flash LLM 的候选确认，Anchor Synthesis Loop 生成并修订自定义行为规范。基准采用决策点延续，在记录的决策点用行为特定评分标准评估 LLM 下一轮输出，无需参考答案或环境重放。论文包含编码与通用场景实验，但摘要未给出具体结果。

rss · Hugging Face Daily Papers · 9月29日 00:00

**「为什么重要」** Agent 完成任务时可能伴随执行不良行为，固定基准难以覆盖部署中遇到的具体问题。TraceDance 直接从真实轨迹生成针对性测试，为 eval 与 observability 工作流提供新路径。它目前仍是研究系统，尚未成为主流基准方案。

**「可关注」** 可关注：TraceDance 的决策点延续不依赖环境重放或参考答案，只评估 LLM 在记录决策点的下一轮输出，这可能改变 harness 中行为回归测试的构建方式。

**标签**: `#eval`, `#observability`, `#coding-agent`, `#harness`

---

<a id="item-agent-engineer-4"></a>
### [EMem-Bench 发布具身记忆基准](https://huggingface.co/papers/2609.28236) ⭐️ 7.5/10

2026 年 9 月 29 日，Hugging Face 每日论文发布 EmbodiedMemory-Bench（EMem-Bench）。基准包含 2,554 个交互式 episode，覆盖四类任务家族，要求智能体在观察、行动和遭遇变化时建立并更新记忆。论文将当前智能体的记忆缺陷归纳为四点：细粒度视觉记忆弱、动态世界状态跟踪不可靠、未记录交互结果揭示的世界状态、难以从先前经验泛化。现有基准未直接评估这些长时程具身交互中的记忆能力。

rss · Hugging Face Daily Papers · 9月29日 00:00

**「为什么重要」** 对需要长时程记忆的 agent 系统而言，这套基准把记忆评估从静态问答推向交互式环境，直接对应维持并更新世界模型的工程难点。论文尚未给出具体智能体跑分或横向对比，实际区分度仍待验证。

**「可关注」** 可关注：论文将长时程记忆缺陷拆成细粒度视觉、动态世界状态、交互结果记录、经验泛化四项，设计记忆系统评测时可对照这些维度分别建立指标，而非只测端到端任务完成率。

**标签**: `#eval`, `#memory`, `#benchmark`, `#embodied-agent`

---

<a id="item-agent-engineer-5"></a>
### [Supporting native Rust in Workers with the new Emscripten target for wasm-bindgen](https://blog.cloudflare.com/rust-workers-emscripten-target/) ⭐️ 6.8/10

Cloudflare announces an experimental preview of the Emscripten wasm32-unknown-emscripten target for wasm-bindgen, allowing native Rust and Tokio-based applications to run on Workers.

rss · Cloudflare Engineering · 9月28日 13:00

**标签**: `#wasm`, `#rust`, `#toolchain`, `#cloudflare-workers`

---

<a id="item-agent-engineer-6"></a>
### [Holo4 发布：27B 与 35B-A3B](https://huggingface.co/blog/Hcompany/holo4) ⭐️ 6.3/10

H Company 发布 Holo4 agentic 模型系列，提供 27B dense 与 35B-A3B MoE 两个尺寸，同步上线 H Models API，并推出 Holotron4 Nano。模型通过 GUI、代码、MCP 和 API 与软件交互，训练基于 Agentic Task Factory 生成的约 10,000 个任务。OSWorld 2.0 上，Holo4 27B 得 61.7%，35B-A3B 得 30.9%，低于 Opus 5.5 的 81.8%；官方称其参数量与成本远低于前沿闭源模型。公开基准的完整轨迹已开源。

rss · Hugging Face Blog · 9月28日 09:44

**「为什么重要」** Holo4 同时覆盖桌面 GUI、代码沙盒、MCP 与业务 API，并公开 OSWorld 2.0 等基准的逐步轨迹。做 coding agent 与 harness 的工程师可直接复现轨迹，对照自建 loop 的长程任务表现。

**「可关注」** 可关注：Holo4 将 GUI、代码、MCP 与 API 统一到同一模型与同一调用方式，并开源基准轨迹，可直接用于对比自建 harness 在长程任务上的记忆与工具调用策略。

**标签**: `#coding-agent`, `#mcp`, `#eval`, `#harness`

---

<a id="item-agent-engineer-7"></a>
### [Sonnet 5.5 分数受回退率干扰](https://www.anthropic.com/claude-sonnet-5-5) ⭐️ 6.0/10

2026-09-28 的 Hacker News 讨论串围绕 Anthropic 的 Sonnet 5.5 页面展开，被引用最多的一条技术质疑是 Terminal-Bench 分差可能被安全回退率混淆。有评论称，Sonnet 5.5 得分 70.6，高于 Opus 5.5 的 66.4，但 Opus 5.5 有 10% 的试次因安全护栏由回退模型回答，Sonnet 5.5 只有 1.5%。材料没有提供 Anthropic 页面正文，评论将细节指向 Sonnet 5.5 System Card 第 8.5 节。

hackernews · D2OQZG8l5BI1S06 · 9月28日 17:58 · [社区讨论](https://news.ycombinator.com/item?id=49881850)

**「为什么重要」** 对做 coding agent 与评测的人来说，榜单分差不能直接当作模型能力差。已发生的是有评论给出回退率数据并指出混淆可能；尚未证实的是这些回退是否完全解释 70.6 与 66.4 的差距。

**「可关注」** 可关注：Sonnet 5.5 与 Opus 5.5 的 Terminal-Bench 分差可能被 10% 对 1.5% 的安全回退率干扰，解读前需先核对回退样本。

**「评论」** 评论分歧明显：有用户认为 Opus 5.5 的效率已够日常 2–3 个会话，质疑 Sonnet 5.5 的并发价值；也有用户强调 GLM、DeepSeek 等中国模型价格更低。技术向评论则聚焦回退率与安全护栏对网络安全任务的影响。

**标签**: `#coding-agent`, `#eval`, `#observability`

---

<a id="item-agent-engineer-8"></a>
### [Claude Sonnet 5.5 发布](https://simonwillison.net/2026/Sep/28/claude-sonnet-5-5/) ⭐️ 6.0/10

Anthropic 发布 Claude Sonnet 5.5，官方称比 Sonnet 5 快 30% 以上，多数任务成本最多低 30%，定价与 Sonnet 5 持平。Simon Willison 实测发现，该模型在部分编码任务上接近 Opus 5.5，基准表现超过 Sonnet 5；但 &quot;max&quot; 思考档位复现了 Opus 5.5 的缺陷，思考 128,000 tokens（花费 $1.28）后耗尽 token，未能生成 SVG。使用 &quot;xhigh&quot; 档位生成 SVG 耗时 41 秒，成本 5.74 美分。Sonnet 5.5 已上线 claude.ai 免费档。

rss · Simon Willison · 9月28日 22:07

**「为什么重要」** 免费档模型更替直接影响开发者默认可用能力。Sonnet 5.5 进入 claude.ai 免费档后，Anthropic 免费产品的能力可能超过使用 Luna 5.6 的 ChatGPT 免费档。同时，&quot;max&quot; 档位出现 128,000 tokens 高消耗后失败，提示高投入思考模式仍需显式成本控制。

**「可关注」** 可关注：Sonnet 5.5 维持 Sonnet 5 定价但基准表现更好，然而 &quot;max&quot; 思考档位存在与 Opus 5.5 相同的缺陷，接入时需限制思考预算或评估 &quot;xhigh&quot; 档位的成本表现。

**标签**: `#coding-agent`, `#eval`, `#observability`

---

<a id="item-agent-engineer-9"></a>
### [Claude Code’s Next Era — Thariq Shihipar, Anthropic](https://www.latent.space/p/thariq) ⭐️ 6.0/10

Anthropic&\#x27;s Thariq Shihipar discusses Claude Code&\#x27;s next era, including shipping new models and features like Plugins and Projects.

rss · Latent Space · 9月29日 01:48

**标签**: `#coding-agent`, `#harness`, `#orchestration`

---

<a id="item-agent-engineer-10"></a>
### [HF daily paper: AdaTutoRank: Learning to Rerank Document Sets via Adaptive Tutoring Optimization for RAG and Deep Research](https://huggingface.co/papers/2609.32472) ⭐️ 5.5/10

AdaTutoRank proposes adaptive tutoring optimization for set-level document reranking in RAG and deep research, but only an abstract is available without results or code.

rss · Hugging Face Daily Papers · 9月29日 00:00

**标签**: `#rag`, `#eval`, `#retrieval`, `#deep-research`

---

## AI 日报

<a id="item-ai-daily-1"></a>
### [OpenAI 就澳政府网站事件致歉](https://openai.com/index/how-we-will-do-better-for-australia) ⭐️ 8.8/10

OpenAI 官方博客发文，就涉及澳大利亚政府网站的事件致歉，并称将加强保护措施、支持澳大利亚网络防御。文章未披露事件细节、影响范围或技术根因，目前仅见 OpenAI 单方说明。

rss · OpenAI Blog · 9月28日 19:00

**标签**: `#lab`, `#policy`, `#industry`

---

<a id="item-ai-daily-2"></a>
### [GitHub 开源 AI 安全代理发现 24 个 Android 漏洞](https://github.blog/security/how-we-found-24-android-vulnerabilities-using-our-open-source-ai-security-agent/) ⭐️ 7.3/10

GitHub 官方博客披露，其开源 AI 安全代理通过定向任务流发现 24 个 Android 漏洞。文章说明了关键 Android 漏洞的挖掘过程，并给出在自有应用上运行同一开源代理的步骤。该内容为第一方安全工具案例，非模型发布或政策变更。

rss · GitHub Blog · 9月28日 19:00

**「为什么重要」** 这是 GitHub 第一方公开的 AI 安全代理实战结果，漏洞数量与任务流方法具体可查，且代理开源，可直接复现到自有 Android 应用。

**「可关注」** 可关注：GitHub 开源了该 AI 安全代理，并公开了发现 24 个 Android 漏洞所用的定向任务流，可参照文章在自有应用上运行同一代理。

**标签**: `#open-source`, `#product`, `#industry`

---

<a id="item-ai-daily-3"></a>
### [OpenAI 扩展 Lenfest 项目](https://openai.com/index/lenfest-ai-collaborative-expansion) ⭐️ 6.8/10

OpenAI 宣布扩展 Lenfest AI Collaborative and Fellowship Program。投入包括 500 万美元资金，以及至多 500 万美元的软件额度与工程支持。该项目由 Lenfest Institute 主导。官方未披露具体受助机构与时间表。

rss · OpenAI Blog · 9月28日 07:00

**「可关注」** 可关注：OpenAI 为 Lenfest AI Collaborative and Fellowship Program 提供至多 500 万美元软件额度与工程支持，项目细节与受助方名单尚未公布。

**标签**: `#lab`, `#industry`

---

## AI 羊毛

<a id="item-ai-deals-1"></a>
### [OpenCode、Command Code 送 6 倍 DeepSeek 额度](https://www.appinn.com/opencode-vs-command-code-ai-coding-plans/) ⭐️ 7.0/10

OpenCode 与 Command Code 先后宣布，$10/月套餐中 DeepSeek V4.1 Flash 使用额度永久提升至 $60/月等值。OpenCode 调整 Go 套餐，Command Code 调整 GOAT 套餐。两者均为付费套餐增值，非免费额度。材料未提及官方领取页、绑卡或地区限制。

rss · 小众软件 · 9月28日 08:17

**「为什么重要」** 对 $10 档付费用户，同等月费对应的 DeepSeek V4.1 Flash 额度提升至 6 倍，且为永久调整。

**「可关注」** 可关注：该提升为付费套餐内额度永久调整，非免费领取；适用已订阅或准备订阅 OpenCode Go、Command Code GOAT 套餐的用户。材料未提供绑卡、地区等限制信息。

**标签**: `#promo`, `#credits`, `#api`

---