---
layout: default
title: "Horizon Summary: 2026-10-06 (ZH)"
date: 2026-10-06
lang: zh
---

> 从 190 条内容中筛选出 17 条重要资讯。

---

**Harness 架构**
1. [Mastra 1.73.0 默认错误恢复](#item-harness-arch-1) ⭐️ 8.8/10
2. [mastra-ai/mastra released @mastra/core@1.74.0](#item-harness-arch-2) ⭐️ 7.3/10
3. [openai/openai-agents-js released @openai/agents-realtime@0.19.0](#item-harness-arch-3) ⭐️ 7.3/10
4. [agents-core 0.19.0 发布](#item-harness-arch-4) ⭐️ 7.3/10
5. [langchain-ai/langgraph released 1.2.13](#item-harness-arch-5) ⭐️ 6.3/10
6. [extensions 0.19.0 追踪修复](#item-harness-arch-6) ⭐️ 6.3/10
7. [MCP server-legacy 2.3.1 发布](#item-harness-arch-7) ⭐️ 6.3/10

**Agent 工程师日报**
1. [HF daily paper: HyperBrowseComp: A Multilingual and Multimodal Stress Test for Web-Browsing Agents](#item-agent-engineer-1) ⭐️ 7.5/10
2. [RealCompanion 基准：27k 消息测伴侣记忆](#item-agent-engineer-2) ⭐️ 7.0/10
3. [RSR 递归自改写扩展复杂任务轨迹](#item-agent-engineer-3) ⭐️ 7.0/10
4. [HF daily paper: SimuVerity: Benchmarking Agents for Engineering-Grade Simulink Model Generation](#item-agent-engineer-4) ⭐️ 6.0/10
5. [Cloudflare Web Search API](#item-agent-engineer-5) ⭐️ 5.5/10
6. [Kyojin 开源，125B MoE 上机](#item-agent-engineer-6) ⭐️ 5.5/10

**AI 日报**
1. [Building advertising for the way people use AI](#item-ai-daily-1) ⭐️ 9.3/10
2. [Our approach to EU text provenance rules](#item-ai-daily-2) ⭐️ 8.8/10
3. [ReviewBench: An open benchmark for AI code review](#item-ai-daily-3) ⭐️ 8.8/10
4. [Cresta 基于 Claude Agent SDK 构建 Conductor](#item-ai-daily-4) ⭐️ 7.3/10

---

## Harness 架构

<a id="item-harness-arch-1"></a>
### [Mastra 1.73.0 默认错误恢复](https://github.com/mastra-ai/mastra/releases/tag/%40mastra/core%401.73.0) ⭐️ 8.8/10

Mastra 1.73.0 为 Agent 默认启用三个错误处理器 \`ProviderHistoryCompat\`、\`PrefillErrorHandler\`、\`StreamErrorRetryProcessor\`，在重试前先修复 provider 历史与 prompt。流式输出新增 \`tool-call-resumed\` chunk，在暂停或审批门控的工具调用恢复时、\`tool-result\` 之前发出，\`@mastra/ai-sdk\` 与 \`@mastra/react\` 的 \`useChat\` 已接入。\`@mastra/connect\` 增加 Google Docs/Drive/Sheets 工具集，平台代理支持 \`responseType: &\#x27;arraybuffer&\#x27;\` 返回二进制响应。\`@mastra/memory\` 的观测记忆 \`recall\` 工具加入 \`viewAttachment\`，模型可直接查看图片/PDF 原生媒体分片。

github · PaulieScanlon · 10月5日 09:30

**「设计要点」** 错误处理器按“先修复、再重试”排序，默认只重试瞬时故障，确定性错误立即抛出；\`errorProcessorDefaults: false\` 是唯一关闭默认项的方式，空 \`errorProcessors\` 列表仍会合并默认处理器。Durable 流不再单独发送 \`tripwire\` chunk，改用 \`finishReason === &\#x27;tripwire&\#x27;\` 与 \`output.tripwire\`。

**「改了什么」** 相比上一版，Agent 无需配置即可从 provider 瞬时失败、assistant prefill 拒绝和历史不兼容中恢复；工具暂停/审批恢复有了明确的流式信号，客户端能可靠清除待处理状态。Durable 与 evented 执行修复了输出处理器重试、并行恢复、事件步骤重复执行，大线程历史加载从平方级降为线性。

**标签**: `#runtime`, `#tools`, `#streaming`

---

<a id="item-harness-arch-2"></a>
### [mastra-ai/mastra released @mastra/core@1.74.0](https://github.com/mastra-ai/mastra/releases/tag/%40mastra/core%401.74.0) ⭐️ 7.3/10

Mastra 1.74.0 expands tool context to include full conversation history and adds filtering, ordering, and paging to observational memory search.

github · PaulieScanlon · 10月5日 09:31

**标签**: `#tools`, `#memory`, `#runtime`

---

<a id="item-harness-arch-3"></a>
### [openai/openai-agents-js released @openai/agents-realtime@0.19.0](https://github.com/openai/openai-agents-js/releases/tag/%40openai/agents-realtime%400.19.0) ⭐️ 7.3/10

OpenAI Agents JS Realtime 0.19.0 ships fixes for conditional tool approvals, durable approval resumes, realtime audio encoding, and conversation ordering.

github · github-actions\[bot\] · 10月5日 16:47

**标签**: `#runtime`, `#tools`, `#permissions`

---

<a id="item-harness-arch-4"></a>
### [agents-core 0.19.0 发布](https://github.com/openai/openai-agents-js/releases/tag/%40openai/agents-core%400.19.0) ⭐️ 7.3/10

OpenAI 发布 agents-core 0.19.0，修复 harness 的流式回调、检查点校验、MCP 调用绑定与条件审批问题。默认将 agent 工具流式回调限制为 1024 个待处理事件，可通过 \`onStreamMaxPendingEvents\` 调整或传 \`null\` 恢复无限制。拒绝缺少初始输入验证完成证据的已启动检查点，恢复的 MCP 调用绑定回原始接收者，条件工具审批在 core 与 Realtime 中绑定到隔离的规范化执行输入。

github · github-actions\[bot\] · 10月5日 16:47

**「设计要点」** 运行时在流式回调、检查点恢复与 MCP 调用上加强边界与来源校验。工具层对条件审批引入规范化输入隔离和策略重评估。权限侧默认脱敏函数工具与 Realtime 审批解析失败，敏感错误追踪需显式调用策略。

**「改了什么」** 相比此前版本，0.19.0 将流式回调默认限流至 1024 并开放配置，检查点恢复要求完整的初始输入验证证据，MCP 历史待处理调用需重新运行以补全接收者来源，条件审批在持久化恢复时重新评估当前策略。

**标签**: `#runtime`, `#mcp`, `#tools`, `#permissions`

---

<a id="item-harness-arch-5"></a>
### [langchain-ai/langgraph released 1.2.13](https://github.com/langchain-ai/langgraph/releases/tag/1.2.13) ⭐️ 6.3/10

LangGraph 1.2.13 patch release fixes checkpoint replay, DeltaChannel, and subgraph state bugs.

github · github-actions\[bot\] · 10月5日 17:51

**标签**: `#runtime`, `#memory`, `#subagents`

---

<a id="item-harness-arch-6"></a>
### [extensions 0.19.0 追踪修复](https://github.com/openai/openai-agents-js/releases/tag/%40openai/agents-extensions%400.19.0) ⭐️ 6.3/10

OpenAI 发布 agents-extensions 0.19.0，聚焦追踪策略、MCP 信息编辑与沙箱依赖修复。核心变更是 Codex spans 遵循调用 Runner 的敏感数据策略，MCP 认证与头部从 AI SDK UI 输出中移除，Daytona SDK 升至 ^0.201.0 以修补 OpenTelemetry 依赖。空白 CODEX\_API\_KEY 现视为未配置，回落到 OPENAI\_API\_KEY。包元数据改用原生 Node.js TypeScript 支持生成。

github · github-actions\[bot\] · 10月5日 16:47

**「设计要点」** 运行时覆盖混合 CommonJS 与 ESM 应用，追踪层通过 Runner 策略统一管控敏感数据导出。沙箱侧保留 Daytona 轮询生命周期，同时修复 Blaxel 前缀修剪与文件并发。构建侧移除未使用依赖，共享日志收敛到 agents-core。

**「改了什么」** 相对上一版，此版本无新架构能力，主要是补丁级修复。追踪策略收紧：默认 OpenAI trace 省略生成推理，错误追踪移除原始响应体与头部。沙箱依赖升级，Daytona SDK 锁定 ^0.201.0 以获取修补的 OpenTelemetry 传递依赖。

**标签**: `#runtime`, `#tools`, `#mcp`, `#sandbox`, `#permissions`

---

<a id="item-harness-arch-7"></a>
### [MCP server-legacy 2.3.1 发布](https://github.com/modelcontextprotocol/typescript-sdk/releases/tag/%40modelcontextprotocol/server-legacy%402.3.1) ⭐️ 6.3/10

modelcontextprotocol/typescript-sdk 发布 @modelcontextprotocol/server-legacy@2.3.1。补丁为 requireBearerAuth 增加可选参数 expectedResource，校验 bearer token 的 audience。该包保持冻结，仅同步 1.x 中间件能力。

github · github-actions\[bot\] · 10月5日 11:49

**「设计要点」** requireBearerAuth 设置 expectedResource 后，要求 verifier 在 AuthInfo.resource 中报告匹配值。字符串比较忽略 fragment 和一个尾部斜杠。不匹配或缺失时返回 401 invalid\_token，附带 WWW-Authenticate challenge。

**「改了什么」** requireBearerAuth 新增可选 expectedResource 参数，与 @modelcontextprotocol/server 2.3.0 和 @modelcontextprotocol/sdk 1.32.0 对齐。未设置时行为不变。@modelcontextprotocol/core 依赖升级至 2.3.1。

**标签**: `#mcp`, `#tools`, `#permissions`

---

## Agent 工程师日报

<a id="item-agent-engineer-1"></a>
### [HF daily paper: HyperBrowseComp: A Multilingual and Multimodal Stress Test for Web-Browsing Agents](https://huggingface.co/papers/2610.03574) ⭐️ 7.5/10

HyperBrowseComp is a new multilingual and multimodal benchmark of 423 challenging questions for evaluating web-browsing agents, using a shared retrieval harness and common agent protocol.

rss · Hugging Face Daily Papers · 10月5日 00:00

**标签**: `#eval`, `#harness`, `#coding-agent`

---

<a id="item-agent-engineer-2"></a>
### [RealCompanion 基准：27k 消息测伴侣记忆](https://huggingface.co/papers/2610.01780) ⭐️ 7.0/10

Hugging Face Daily Papers 于 2026-10-05 收录 RealCompanion 基准论文。该基准包含 10 段与 AI 伴侣的真实关系，共 27,218 条消息，时间跨度最多 120 天；除原始对话外，还发布 profile、persona、chat ground truth、question set 四个派生文件，每个文件均标注所引用的消息。每条聊天标签附带产生它的推理轨迹，并逐阶段对照对话验证。论文报告三个发现，但公开摘要仅显示第一个——过去很少被需要且距离很远（原文此处截断），其余发现未展示。

rss · Hugging Face Daily Papers · 10月5日 00:00

**「为什么重要」** AI 伴侣的长期记忆与人类理解缺少公开可复现的纵向评估数据；RealCompanion 提供带引用和推理轨迹的真实对话基准，可直接用于 agent memory 与评测基础设施的验证。

**「可关注」** 可关注：RealCompanion 的每个聊天标签都附带可逐阶段核对的推理轨迹，且首个发现指出“过去很少被需要”，为 agent memory 评测提供了具体张力。

**标签**: `#eval`, `#memory`

---

<a id="item-agent-engineer-3"></a>
### [RSR 递归自改写扩展复杂任务轨迹](https://huggingface.co/papers/2610.02826) ⭐️ 7.0/10

论文提出 Recursive Self-Rewrite（RSR），用同一基础模型 Qwen-3.8-27B 在多种专用 harness 下找成功解，再重构为通用 harness 的训练轨迹。planner 抽取流程成 runbook，critic 筛查 verifier 与 solution 泄漏并递归修正，executor 在新沙箱执行合格 runbook。约 3K 条自建终端任务上，三个 harness 共解出 759 个任务，较记录池中最强单一 harness 提升 34.3%。

rss · Hugging Face Daily Papers · 10月5日 00:00

**「为什么重要」** 专用 harness 的干预在部署时常不可得，RSR 把跨 harness 成功轨迹转成通用 harness 可复现的训练数据，直接服务于 agent 训练数据生成与 eval 设计。

**「可关注」** 可关注：若训练数据来自特定 harness，需排查其中是否包含部署时无法复现的干预；RSR 的 planner-critic-executor 拆分给出了用通用 harness 重建轨迹的参考架构。

**标签**: `#harness`, `#eval`, `#coding-agent`, `#orchestration`

---

<a id="item-agent-engineer-4"></a>
### [HF daily paper: SimuVerity: Benchmarking Agents for Engineering-Grade Simulink Model Generation](https://huggingface.co/papers/2610.02304) ⭐️ 6.0/10

SimuVerity 推出包含 101 项任务的基准，通过分层评估器从六个维度系统评测 agent 生成工程级 Simulink 模型的能力。

rss · Hugging Face Daily Papers · 10月5日 00:00

**标签**: `#eval`, `#coding-agent`, `#benchmark`

---

<a id="item-agent-engineer-5"></a>
### [Cloudflare Web Search API](https://developers.cloudflare.com/changelog/post/2026-10-02-introducing-web-search-api/) ⭐️ 5.5/10

Cloudflare 于 2026-10-02 发布 Web Search API。HN 讨论聚焦两个问题：服务条款是否允许存储和二次分发搜索结果，以及与 Gemini 等现有搜索服务的成本差异。社区发现该 API 文档声称三家提供商均支持零数据保留，但提供商页面显示 Exa 的零数据保留为「否」，存在信息不一致。目前公开材料未包含该 API 的架构细节或生产环境基准。

hackernews · tosh · 10月5日 10:47 · [社区讨论](https://news.ycombinator.com/item?id=49963171)

**「为什么重要」** 对 coding agent 开发者而言，搜索 API 的结果存储权限和零数据保留政策直接影响 agent 的会话记录与合规设计。成本差异也会改变工具选型，但具体影响尚未在材料中证实。

**「可关注」** 可关注：在把 Web Search API 接入 agent 前，需先核实服务条款对结果存储和二次分发的限制，并核对各提供商的零数据保留声明是否与实际页面一致。

**「评论」** 社区对是否值得通过 Cloudflare 中间层存在分歧：一方认为直接调用 Gemini Flash Lite 2.5 等提供商更便宜，另一方则分享本地索引与浏览器插件缓存来规避反爬限制的实践。

**标签**: `#coding-agent`, `#tools`, `#permissions`, `#api`

---

<a id="item-agent-engineer-6"></a>
### [Kyojin 开源，125B MoE 上机](https://www.reddit.com/r/LocalLLaMA/comments/1wybesy/qwen38flashnext_125b_on_a_single_strix_halo_mini/) ⭐️ 5.5/10

开发者发布 Qwen3.8-Flash-Next（125B MoE，6B 激活）的 95 GB EXL3 权重与基于 ExLlamaV3 的 Kyojin 引擎，在单台 AMD Strix Halo 迷你机（Ryzen AI Max+ 395，128 GB）完成部署。实测开启投机解码时解码速度 44-59 tok/s（聊天约 47、代码约 58），不带为 32.7 tok/s；预填充在 4K/32K/128K 下约 1,412/1,486/1,367 tok/s，128K needle 测试 10/10 且保持 32 tok/s，与原始 FP8 模型的 top-1 一致率为 94.1%。作者给出对比基线：Halogen 0.16.2 在纯解码（39.8 vs 32.7 tok/s）和预填充（4K 约 1,460 vs 1,306 tok/s）上更快，但 Kyojin 保真度更高（94.1% vs 92.3%，KL 散度低 41%）；llama.cpp 在同机的对比数据来自第三方，未经作者复测。引擎附带默认关闭的 uncensor 预设，作者建议依赖工具调用的 agent 不要开启。

reddit · r/LocalLLaMA · /u/Yaniss916 · 10月5日 15:25

**「为什么重要」** 在 128 GB 单机上跑起 125B MoE 并公开引擎与权重，给本地 agent 部署提供了可复现基线。材料同时呈现速度与保真度的取舍：Kyojin 在解码和预填充上落后于 Halogen，但以更高 top-1 一致率和更低 KL 散度贴近原版 FP8 模型。

**「可关注」** Kyojin 在解码与预填充上均落后于 Halogen 0.16.2，但以 94.1% top-1 一致率和低 41% 的 KL 散度更贴近原版 FP8 模型；对输出忠实度敏感的本地 agent，可跟踪其引擎核心重做后的速度变化。

**标签**: `#inference`, `#local-llm`, `#performance`, `#eval`

---

## AI 日报

<a id="item-ai-daily-1"></a>
### [Building advertising for the way people use AI](https://openai.com/index/new-chatgpt-ads-format-and-measurement) ⭐️ 9.3/10

OpenAI introduces a new visual ad format in ChatGPT and expands measurement tools, attribution partnerships, and brand suitability for advertisers.

rss · OpenAI Blog · 10月5日 10:00

**标签**: `#product`, `#industry`, `#lab`, `#policy`

---

<a id="item-ai-daily-2"></a>
### [Our approach to EU text provenance rules](https://openai.com/index/eu-text-provenance) ⭐️ 8.8/10

OpenAI outlines its approach to EU text provenance rules, detailing where watermarks apply, how detection works, and why access starts with researchers.

rss · OpenAI Blog · 10月5日 15:00

**标签**: `#policy`, `#lab`, `#industry`, `#model`

---

<a id="item-ai-daily-3"></a>
### [ReviewBench: An open benchmark for AI code review](https://github.blog/ai-and-ml/github-copilot/reviewbench-an-open-benchmark-for-ai-code-review/) ⭐️ 8.8/10

GitHub launched ReviewBench, an open benchmark for evaluating AI code review agents using representative pull requests, multi-source ground truth, and production-aligned metrics.

rss · GitHub Blog · 10月5日 15:59

**标签**: `#lab`, `#eval`, `#open-source`, `#product`, `#industry`

---

<a id="item-ai-daily-4"></a>
### [Cresta 基于 Claude Agent SDK 构建 Conductor](https://claude.com/blog/how-cresta-turned-cx-expertise-into-an-agent-builder-on-the-claude-agent-sdk) ⭐️ 7.3/10

Cresta 把客户经验做成 Conductor，一个跑在 Claude Agent SDK 上的智能体构建器。用户用自然语言描述需求，Conductor 引导从蓝图到实现、评估、优化的全流程。Claude Agent SDK 负责通用执行：收集上下文、调用工具、写代码、跑代码；Conductor 在其上叠加 Cresta 的对话数据、CX 工作流和领域上下文。Cresta 称早期用例初始部署时间约缩短一半。

rss · Claude Blog · 10月5日 00:00

**「为什么重要」** 对做 agent harness 的人来说，这是「元智能体」的一个落地样本：通用执行层用 Claude Agent SDK，领域控制面自己写。评估方法也可参考——Cresta 用固定任务集衡量 Conductor 的构建能力，模型或框架更新后重跑同一套题，对比前后差异。

**「可关注」** Cresta 选型时重点评估了 Claude Agent SDK 的数据隐私、租户架构、组织级密钥分发、控制与可观测性；把通用执行交给 SDK，自己专注 CX 工作流与反馈闭环。评估覆盖构建新智能体、写测试、改旧智能体、根因分析四类固定任务，新模型或框架更新后重跑对比。

**标签**: `#lab`, `#product`, `#industry`, `#model`

---