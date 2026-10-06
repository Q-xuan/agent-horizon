---
layout: default
title: "Horizon Summary: 2026-10-06 (EN)"
date: 2026-10-06
lang: en
---

> From 190 items, 17 important content pieces were selected

---

**Agent Harness Architecture**
1. [Mastra 1.73.0 默认错误恢复](#item-harness-arch-1) ⭐️ 8.8/10
2. [mastra-ai/mastra released @mastra/core@1.74.0](#item-harness-arch-2) ⭐️ 7.3/10
3. [openai/openai-agents-js released @openai/agents-realtime@0.19.0](#item-harness-arch-3) ⭐️ 7.3/10
4. [agents-core 0.19.0](#item-harness-arch-4) ⭐️ 7.3/10
5. [langchain-ai/langgraph released 1.2.13](#item-harness-arch-5) ⭐️ 6.3/10
6. [agents-extensions 0.19.0](#item-harness-arch-6) ⭐️ 6.3/10
7. [server-legacy 2.3.1 发布](#item-harness-arch-7) ⭐️ 6.3/10

**AI Agent Engineer**
1. [HF daily paper: HyperBrowseComp: A Multilingual and Multimodal Stress Test for Web-Browsing Agents](#item-agent-engineer-1) ⭐️ 7.5/10
2. [RealCompanion 发布纵向对话基准](#item-agent-engineer-2) ⭐️ 7.0/10
3. [RSR：递归自改写扩展复杂任务轨迹](#item-agent-engineer-3) ⭐️ 7.0/10
4. [HF daily paper: SimuVerity: Benchmarking Agents for Engineering-Grade Simulink Model Generation](#item-agent-engineer-4) ⭐️ 6.0/10
5. [Cloudflare Web 搜索 API](#item-agent-engineer-5) ⭐️ 5.5/10
6. [Strix Halo 跑通 125B MoE](#item-agent-engineer-6) ⭐️ 5.5/10

**AI Daily**
1. [Building advertising for the way people use AI](#item-ai-daily-1) ⭐️ 9.3/10
2. [Our approach to EU text provenance rules](#item-ai-daily-2) ⭐️ 8.8/10
3. [ReviewBench: An open benchmark for AI code review](#item-ai-daily-3) ⭐️ 8.8/10
4. [Cresta Builds Conductor on Claude Agent SDK](#item-ai-daily-4) ⭐️ 7.3/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [Mastra 1.73.0 默认错误恢复](https://github.com/mastra-ai/mastra/releases/tag/%40mastra/core%401.73.0) ⭐️ 8.8/10

Mastra 1.73.0 默认启用三个错误处理器 \`ProviderHistoryCompat\`、\`PrefillErrorHandler\`、\`StreamErrorRetryProcessor\`，在重试前修复历史与提示词。流新增 \`tool-call-resumed\` 分片，在挂起或审批门控的工具调用恢复后、\`tool-result\` 前发出，客户端可据此清理待处理工具状态。\`@mastra/connect\` 增加 Google Docs/Drive/Sheets 工具集，平台代理支持 \`responseType: &\#x27;arraybuffer&\#x27;\` 返回二进制响应。\`@mastra/memory\` 的观测记忆 \`recall\` 工具加入 \`viewAttachment\`，模型可直接读取图片/PDF 原生媒体分片。

github · PaulieScanlon · Oct 5, 09:30

**「设计要点」** 错误恢复按修复优先排序：\`ProviderHistoryCompat\` 在出站前重写提示词，\`StreamErrorRetryProcessor\` 只重试瞬时故障，默认每轮上限 3 次，确定性错误立即抛出。工具恢复通过 \`tool-call-resumed\` 在 \`tool-result\` 前标记已回答，覆盖子代理委派后结果替换的场景。观测记忆将附件作为原生媒体分片注入 \`recall\` 结果，修复附件引用以便代理复用。

**「改了什么」** Agent 无需配置即可从 provider 瞬时故障、prefill 拒绝和历史不兼容中恢复；durable 与 evented 执行修复输出处理器重试、恢复后工具并行、事件步骤重复执行，大线程历史加载从平方级降为线性。破坏性变更：durable 流不再单独发送 \`tripwire\` 分片，改用 \`finishReason === &\#x27;tripwire&\#x27;\` 与 \`output.tripwire\`。

**Tags**: `#runtime`, `#tools`, `#streaming`

---

<a id="item-harness-arch-2"></a>
### [mastra-ai/mastra released @mastra/core@1.74.0](https://github.com/mastra-ai/mastra/releases/tag/%40mastra/core%401.74.0) ⭐️ 7.3/10

Mastra 1.74.0 expands tool context to include full conversation history and adds filtering, ordering, and paging to observational memory search.

github · PaulieScanlon · Oct 5, 09:31

**Tags**: `#tools`, `#memory`, `#runtime`

---

<a id="item-harness-arch-3"></a>
### [openai/openai-agents-js released @openai/agents-realtime@0.19.0](https://github.com/openai/openai-agents-js/releases/tag/%40openai/agents-realtime%400.19.0) ⭐️ 7.3/10

OpenAI Agents JS Realtime 0.19.0 ships fixes for conditional tool approvals, durable approval resumes, realtime audio encoding, and conversation ordering.

github · github-actions\[bot\] · Oct 5, 16:47

**Tags**: `#runtime`, `#tools`, `#permissions`

---

<a id="item-harness-arch-4"></a>
### [agents-core 0.19.0](https://github.com/openai/openai-agents-js/releases/tag/%40openai/agents-core%400.19.0) ⭐️ 7.3/10

OpenAI shipped @openai/agents-core 0.19.0, tightening runtime and security behavior across the agent harness. Streaming callbacks are now bounded to 1024 pending events by default, checkpoint restarts reject incomplete initial input validation, and resumed MCP calls must bind to their original recipients. Conditional tool approvals re-evaluate policies on durable resumes and reject uncopyable normalized values, while default approval parse failures redact sensitive error traces.

github · github-actions\[bot\] · Oct 5, 16:47

**「Design Notes」** The release enforces bounded buffering in tool streaming, validates checkpoint completion before restart, and carries recipient provenance through MCP call resumption. Conditional approvals isolate normalized execution input and re-check active policies when restoring from durable state.

**「What Changed」** Streaming callbacks gained a default 1024-event pending limit with onStreamMaxPendingEvents to adjust or disable it. Checkpoint validation now rejects started snapshots without completed initial input evidence, and MCP resumption requires original recipient binding or a fresh run for legacy pending calls.

**Tags**: `#runtime`, `#mcp`, `#tools`, `#permissions`

---

<a id="item-harness-arch-5"></a>
### [langchain-ai/langgraph released 1.2.13](https://github.com/langchain-ai/langgraph/releases/tag/1.2.13) ⭐️ 6.3/10

LangGraph 1.2.13 patch release fixes checkpoint replay, DeltaChannel, and subgraph state bugs.

github · github-actions\[bot\] · Oct 5, 17:51

**Tags**: `#runtime`, `#memory`, `#subagents`

---

<a id="item-harness-arch-6"></a>
### [agents-extensions 0.19.0](https://github.com/openai/openai-agents-js/releases/tag/%40openai/agents-extensions%400.19.0) ⭐️ 6.3/10

openai/agents-extensions 0.19.0 随 agents-core 0.19.0 发布，以补丁修复为主，无重大架构变更。核心改动是让 Codex span 遵循调用方 Runner 的敏感数据追踪策略，覆盖混合 CommonJS 与 ESM 应用；同时脱敏 MCP 认证与头部信息，默认函数工具和 Realtime 审批的解析失败也不再进入错误追踪。沙箱侧要求 Daytona SDK ^0.201.0 以引入修补版 OpenTelemetry 依赖，保留轮询生命周期，并修复远程会话归档上限、Blaxel 前缀线性裁剪与递归拷贝并发问题。

github · github-actions\[bot\] · Oct 5, 16:47

**「设计要点」** 追踪策略由 Runner 统一控制，Codex span 与 AI SDK 错误追踪遵循同一敏感数据策略；MCP 与函数工具脱敏在服务端保留重放配置的前提下，于 UI 输出层完成。

**「改了什么」** 追踪策略扩展到 Codex span 与混合模块应用；MCP 认证信息、AI SDK 原始响应体与头部从追踪及 UI 输出中脱敏；沙箱创建遵守归档上限，递归拷贝尊重本地文件并发。

**Tags**: `#runtime`, `#tools`, `#mcp`, `#sandbox`, `#permissions`

---

<a id="item-harness-arch-7"></a>
### [server-legacy 2.3.1 发布](https://github.com/modelcontextprotocol/typescript-sdk/releases/tag/%40modelcontextprotocol/server-legacy%402.3.1) ⭐️ 6.3/10

@modelcontextprotocol/server-legacy 发布 2.3.1，requireBearerAuth 新增可选参数 expectedResource，用于校验 bearer token 的 audience。该参数对齐 @modelcontextprotocol/server 2.3.0 与 @modelcontextprotocol/sdk 1.32.0。设置后，仅当 verifier 在 AuthInfo.resource 报告相同值才接受 token，字符串比较时忽略 fragment 和一个末尾斜杠；不匹配或缺失则返回 401 invalid\_token 并附带 WWW-Authenticate 挑战。未设置时行为不变，包体其余部分保持冻结，仅同步此项以匹配其所复制的 1.x 中间件。

github · github-actions\[bot\] · Oct 5, 11:49

**「设计要点」** Bearer 鉴权通过 expectedResource 把 token audience 绑定到服务端 URL，校验逻辑读取 verifier 返回的 AuthInfo.resource，以字符串比对并忽略 fragment 和单个末尾斜杠。失败路径统一回 401 invalid\_token，与主包 1.x 中间件保持一致。

**「改了什么」** requireBearerAuth 多了一个可选的 audience 校验入口；包体其余部分冻结，@modelcontextprotocol/core 依赖升至 2.3.1。

**Tags**: `#mcp`, `#tools`, `#permissions`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [HF daily paper: HyperBrowseComp: A Multilingual and Multimodal Stress Test for Web-Browsing Agents](https://huggingface.co/papers/2610.03574) ⭐️ 7.5/10

HyperBrowseComp is a new multilingual and multimodal benchmark of 423 challenging questions for evaluating web-browsing agents, using a shared retrieval harness and common agent protocol.

rss · Hugging Face Daily Papers · Oct 5, 00:00

**Tags**: `#eval`, `#harness`, `#coding-agent`

---

<a id="item-agent-engineer-2"></a>
### [RealCompanion 发布纵向对话基准](https://huggingface.co/papers/2610.01780) ⭐️ 7.0/10

RealCompanion 发布纵向真实对话基准，覆盖 10 段人与 AI 陪伴的长期关系，共 27,218 条消息，跨度最长 120 天。除原始对话外，还释出四个衍生文件：profile、persona、chat ground truth 和 question set，每个文件均标注所引用的消息。每条 chat 标签附带推理轨迹，并按阶段对照对话校验。论文提到三个发现，但提供的摘要仅显示第一个发现的开头——过去很少被需要，且距离遥远；其余发现在当前材料中不完整。

rss · Hugging Face Daily Papers · Oct 5, 00:00

**「为什么重要」** 该基准把长期对话中的记忆与人类理解变成可度量任务，提供带引用的可复现工件。对构建 agent 记忆与评估基础设施的工程师而言，它给出了一个基于真实纵向数据的测试场，而非纯合成场景。

**「可关注」** 可关注：RealCompanion 用引用消息加分阶段校验推理轨迹的方式构造标签，这种可溯源设计可直接用于 agent 记忆系统的评估集构建。

**Tags**: `#eval`, `#memory`

---

<a id="item-agent-engineer-3"></a>
### [RSR：递归自改写扩展复杂任务轨迹](https://huggingface.co/papers/2610.02826) ⭐️ 7.0/10

论文提出 Recursive Self-Rewrite（RSR）框架，用单一基座模型 Qwen-3.8-27B 在多种专用 harness 下发现成功解，再重构为通用 harness 下的训练轨迹。planner 提取流程为 runbook，critic 筛查 verifier 与 solution 泄漏并指导递归修订，executor 在全新沙箱中执行合格 runbook。约 3K 自建终端任务上，三种 harness 联合解决 759 个任务，比记录池中最强单一 harness 多 34.3%。RSR 扩展 2,001 条成功源轨迹。

rss · Hugging Face Daily Papers · Oct 5, 00:00

**「为什么重要」** 专用 harness 干预在部署时常不可用，该工作给出把多 harness 成功解转为通用训练轨迹的完整架构与量化结果。做 agent 训练数据生成、harness 设计与 eval 策划的工程师可直接参考。

**「可关注」** 可关注：RSR 用 planner-critic-executor 将专用 harness 成功解重构为通用 harness 训练轨迹，759 任务、34.3% 增益与 2,001 条源轨迹扩展可作为数据合成与 eval 设计的参照基线。

**Tags**: `#harness`, `#eval`, `#coding-agent`, `#orchestration`

---

<a id="item-agent-engineer-4"></a>
### [HF daily paper: SimuVerity: Benchmarking Agents for Engineering-Grade Simulink Model Generation](https://huggingface.co/papers/2610.02304) ⭐️ 6.0/10

SimuVerity 推出包含 101 项任务的基准，通过分层评估器从六个维度系统评测 agent 生成工程级 Simulink 模型的能力。

rss · Hugging Face Daily Papers · Oct 5, 00:00

**Tags**: `#eval`, `#coding-agent`, `#benchmark`

---

<a id="item-agent-engineer-5"></a>
### [Cloudflare Web 搜索 API](https://developers.cloudflare.com/changelog/post/2026-10-02-introducing-web-search-api/) ⭐️ 5.5/10

Cloudflare 推出 Web Search API，changelog 日期为 2026-10-02。HN 讨论聚焦服务条款对存储和二次分发结果的限制，以及与 Gemini、Exa 等现有提供商的成本对比。目前材料未提供该 API 的架构细节、延迟数据或生产环境基准。

hackernews · tosh · Oct 5, 10:47 · [Discussion](https://news.ycombinator.com/item?id=49963171)

**「为什么重要」** 对 coding agent 和 harness 开发者而言，搜索 API 的条款限制和计费模式直接影响工具链设计。社区已指出存储限制和 Zero Data Retention 声明与提供商页面存在矛盾，但实际影响尚待验证。

**「可关注」** 可关注：在把 Web Search API 接入 agent 前，需先确认条款是否允许缓存响应和提供“分享 transcript”功能，并核对提供商的 Zero Data Retention 状态。

**「评论」** HN 讨论显示，开发者最关心搜索结果能否存储与二次分发，以及 Cloudflare 中转后的成本与数据保留政策；jasonjmcghee 发现 Cloudflare 宣称的 Zero Data Retention 与 Exa 提供商页面标注“否”存在矛盾。

**Tags**: `#coding-agent`, `#tools`, `#permissions`, `#api`

---

<a id="item-agent-engineer-6"></a>
### [Strix Halo 跑通 125B MoE](https://www.reddit.com/r/LocalLLaMA/comments/1wybesy/qwen38flashnext_125b_on_a_single_strix_halo_mini/) ⭐️ 5.5/10

Yamz Labs 开源 Qwen3.8-Flash-Next（125B MoE，6B 激活）的 95 GB EXL3 权重与 Kyojin 引擎新版本，在单台 AMD Strix Halo 迷你主机（Ryzen AI Max+ 395，128 GB）上跑通。开启投机解码后解码 44–59 tok/s（对话约 47、代码约 58），关闭为 32.7 tok/s；预填充 4K/32K/128K 分别 1,412/1,486/1,367 tok/s，近乎平稳。128K 针检索 10/10，速度仍 32 tok/s；与原始 FP8 模型 top-1 一致率 94.1%，KL 散度低 41%。团队称投机解码返回与普通解码完全一致的 token。

reddit · r/LocalLLaMA · /u/Yaniss916 · Oct 5, 15:25

**「为什么重要」** 单台 128 GB 迷你主机即可运行 125B MoE 并保持长上下文吞吐，降低本地部署门槛。同时公开与 Halogen 0.16.2 的对比数据，显示其在保真度上占优、速度上仍落后，为本地推理引擎选型提供可验证基准。

**「可关注」** 可关注：Kyojin 以 94.1% top-1 一致率和更低 KL 散度换取速度，若 agent 场景重视输出稳定性可评估；但团队明示速度仍落后 Halogen，核心重写尚未完成，采用前建议等待后续版本。

**Tags**: `#inference`, `#local-llm`, `#performance`, `#eval`

---

## AI Daily

<a id="item-ai-daily-1"></a>
### [Building advertising for the way people use AI](https://openai.com/index/new-chatgpt-ads-format-and-measurement) ⭐️ 9.3/10

OpenAI introduces a new visual ad format in ChatGPT and expands measurement tools, attribution partnerships, and brand suitability for advertisers.

rss · OpenAI Blog · Oct 5, 10:00

**Tags**: `#product`, `#industry`, `#lab`, `#policy`

---

<a id="item-ai-daily-2"></a>
### [Our approach to EU text provenance rules](https://openai.com/index/eu-text-provenance) ⭐️ 8.8/10

OpenAI outlines its approach to EU text provenance rules, detailing where watermarks apply, how detection works, and why access starts with researchers.

rss · OpenAI Blog · Oct 5, 15:00

**Tags**: `#policy`, `#lab`, `#industry`, `#model`

---

<a id="item-ai-daily-3"></a>
### [ReviewBench: An open benchmark for AI code review](https://github.blog/ai-and-ml/github-copilot/reviewbench-an-open-benchmark-for-ai-code-review/) ⭐️ 8.8/10

GitHub launched ReviewBench, an open benchmark for evaluating AI code review agents using representative pull requests, multi-source ground truth, and production-aligned metrics.

rss · GitHub Blog · Oct 5, 15:59

**Tags**: `#lab`, `#eval`, `#open-source`, `#product`, `#industry`

---

<a id="item-ai-daily-4"></a>
### [Cresta Builds Conductor on Claude Agent SDK](https://claude.com/blog/how-cresta-turned-cx-expertise-into-an-agent-builder-on-the-claude-agent-sdk) ⭐️ 7.3/10

Cresta launched Conductor, a natural language agent builder for customer experience teams, built on the Claude Agent SDK. The SDK acts as a general-purpose execution harness that gathers context, calls tools, and writes and runs code, while Conductor layers Cresta&\#x27;s conversation intelligence, evaluations, and runtime on top. Cresta reports that early use cases across its own and partner deployments cut initial deployment time roughly in half. The company originally prototyped Conductor internally with Claude Sonnet and Claude Opus before productizing it.

rss · Claude Blog · Oct 5, 00:00

**「Why it matters」** Conductor illustrates a split between general-purpose agent execution and domain-specific control planes: the Claude Agent SDK handles open-ended development work, while Cresta&\#x27;s platform supplies CX context, policy, and observability. Cresta also reruns a fixed set of build tasks—building a new agent, writing a test case, modifying an existing agent, and performing root cause analysis—whenever a new Claude model or framework update ships, using identical scoring to detect regressions before committing.

**「Takeaway」** Worth watching: Cresta separates deterministic business rules from flexible model behavior, then converts proven build patterns into reusable memory artifacts that teams can share as skills.

**Tags**: `#lab`, `#product`, `#industry`, `#model`

---