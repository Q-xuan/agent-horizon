---
layout: default
title: "Horizon Summary: 2026-10-06 (EN)"
date: 2026-10-06
lang: en
---

> From 198 items, 16 important content pieces were selected

---

**Agent Harness Architecture**
1. [vLLM v0.31.0 发布](#item-harness-arch-1) ⭐️ 8.8/10
2. [Claude Code v2.1.290 Released](#item-harness-arch-2) ⭐️ 8.3/10
3. [Mastra 1.74.0 发布](#item-harness-arch-3) ⭐️ 8.3/10
4. [Mastra 1.73.0 Adds Default Error Recovery and Tool-Pause UX](#item-harness-arch-4) ⭐️ 8.3/10
5. [OpenAI Agents JS Realtime 0.19.0 Released](#item-harness-arch-5) ⭐️ 7.8/10
6. [OpenAI Agents Core 0.19.0](#item-harness-arch-6) ⭐️ 7.3/10
7. [E2B 2.52.1 修正构建与重试语义](#item-harness-arch-7) ⭐️ 6.8/10

**AI Agent Engineer**
1. [OSWorld-Pro：CUA 过程化评测](#item-agent-engineer-1) ⭐️ 7.5/10
2. [PluginRSI Evolves Agent Harnesses with Reusable Plugins](#item-agent-engineer-2) ⭐️ 7.5/10
3. [Cowork 从本地 VM 迁至云端沙箱](#item-agent-engineer-3) ⭐️ 6.0/10
4. [HF daily paper: ASCENT: Online Test-Time Training of Long-Horizon Agents via Self-Distillation of Verified Experience](#item-agent-engineer-4) ⭐️ 5.5/10
5. [HF daily paper: CANOPY: Adaptive-Granularity Evidence Compression for Multimodal RAG](#item-agent-engineer-5) ⭐️ 5.5/10

**AI Daily**
1. [OpenAI 推 ChatGPT 视觉广告](#item-ai-daily-1) ⭐️ 9.8/10
2. [OpenAI 阐述欧盟文本溯源方案](#item-ai-daily-2) ⭐️ 9.3/10
3. [ReviewBench: An open benchmark for AI code review](#item-ai-daily-3) ⭐️ 8.8/10

**AI Deals**
1. [Show HN: Free Public API Lab](#item-ai-deals-1) ⭐️ 5.0/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [vLLM v0.31.0 发布](https://github.com/vllm-project/vllm/releases/tag/v0.31.0) ⭐️ 8.8/10

vLLM v0.31.0 发布，合入 717 个提交、307 位贡献者。新增权重缓存守护进程 \`vllm preload\`，把量化后权重常驻 GPU 内存，支持引擎重启、数据并行、MTP 草稿模型与 \`/health\` 探活。前缀缓存引入 SWA bounded replay，滑动窗口 KV 不再进入前缀缓存。Model Runner V2 支持草稿模型投机解码与自定义 logits 处理器，调度层新增 \`--max-num-active-seqs\` 与自适应 \`--long-prefill-token-threshold\`。

github · khluu · Oct 5, 06:44

**「设计要点」** 权重缓存守护进程通过独立 CLI 与引擎解耦，重启时复用 GPU 中的量化权重；SWA bounded replay 在块哈希层区分滑动窗口 KV，避免污染前缀缓存。多模态请求参数默认拒绝，需显式 \`--trust-request-mm-kwargs\`；前缀缓存额外键按来源打标，LoRA 名与 \`cache\_salt\` 不再冲突。

**「改了什么」** 新增 \`vllm preload\` 守护进程与实验性 CRIU 快照 \`vllm snapshot create/restore\`；调度支持 \`--max-num-active-seqs\` 独立限流 RUNNING，\`--long-prefill-token-threshold\` 按等待 prefill 数量自适应。破坏性变更包括移除 \`tokenizer\_mode=&quot;slow&quot;\`、\`quantization=&quot;fp8&quot;\` 改为 \`fp8\_per\_tensor\` 简写、AllSpark INT8 后端移除，\`--enforce-eager\` 同时关闭 JIT kernel warmup。

**Tags**: `#runtime`, `#prefix-cache`, `#tools`

---

<a id="item-harness-arch-2"></a>
### [Claude Code v2.1.290 Released](https://github.com/anthropics/claude-code/releases/tag/v2.1.290) ⭐️ 8.3/10

Claude Code v2.1.290 adds subagent-aware permission checks, server tool use visibility in mod hooks, and partial-name session attach/log commands. The release exposes \`serverToolUses\` in \`turn.step\` hook results, \`agentId\` in \`tool.check\` events, and \`ceiling\` in approval verdicts. It also fixes proxy beta-header handling, long-session image limits, and scheduled task resumption after compaction.

github · ashwin-ant · Oct 5, 23:33

**「Design Notes」** Plugin hooks can now tell a subagent&\#x27;s permission check from the main session&\#x27;s via \`agentId\`, and read the organization-required approval \`ceiling\` directly from the \`tool.check\` verdict. \`claude plugin validate\` lists gating hooks and whether they have \`.catch\` handlers.

**「What Changed」** Added \`serverToolUses\` to \`turn.step\` results, \`agentId\` to \`tool.check\`, and \`ceiling\` to approval verdicts, plus partial-name \`claude attach\` and \`claude logs\`. Fixed proxy beta-header rejections, long-session image errors, scheduled tasks after compaction, and subagent thinking cache loss.

**Tags**: `#tools`, `#permissions`, `#subagents`, `#runtime`

---

<a id="item-harness-arch-3"></a>
### [Mastra 1.74.0 发布](https://github.com/mastra-ai/mastra/releases/tag/%40mastra/core%401.74.0) ⭐️ 8.3/10

Mastra 1.74.0 发布。工具执行上下文新增 \`context.agent.getMessages\(\)\`，标准与 durable agent loop 均可读取当前会话全量消息，含记忆消息与运行中响应，原有仅含输入的 \`messages\` 字段保持不变。observational memory 历史搜索支持 \`groupId\` 过滤、\`sortDirection\` 排序与 \`recordId\` 直查，适配器通过 \`supportsObservationalMemoryHistorySearch\` 声明能力。Convex 需重新部署服务端函数才能启用新过滤条件。

github · PaulieScanlon · Oct 5, 09:31

**「设计要点」** 工具层从仅读输入 \`messages\` 扩展为可读完整会话状态；记忆层通过分组分页与反射压缩后的组回溯，把 observational memory 检索从单条命中扩展为上下文窗口式的连续翻阅。

**「改了什么」** 相对旧版，工具可直接访问会话历史而非仅限当前输入；记忆召回新增按 \`groupId\` 前后分页，无需重建索引即可读取被反射压缩或尚未激活的缓冲组。

**Tags**: `#runtime`, `#tools`, `#memory`

---

<a id="item-harness-arch-4"></a>
### [Mastra 1.73.0 Adds Default Error Recovery and Tool-Pause UX](https://github.com/mastra-ai/mastra/releases/tag/%40mastra/core%401.73.0) ⭐️ 8.3/10

Mastra 1.73.0 enables three default error processors—ProviderHistoryCompat, PrefillErrorHandler, and StreamErrorRetryProcessor—so agents automatically repair provider history and prompt issues before retrying transient failures. The release adds a tool-call-resumed stream chunk, wired through @mastra/ai-sdk and @mastra/react useChat, letting clients mark suspended or approval-gated tool calls as answered before the tool-result arrives. @mastra/connect introduces Google Docs, Drive, and Sheets toolsets plus binary proxy responses via responseType: &\#x27;arraybuffer&\#x27;. Durable and evented execution also gains correctness fixes, including linear thread-history loading and heartbeat/lease fencing to prevent double-runs.

github · PaulieScanlon · Oct 5, 09:30

**「Design Notes」** The default error-processor chain is repair-first: ProviderHistoryCompat rewrites outbound prompts and history before StreamErrorRetryProcessor replays only transient failures, bounded by a safety cap of 3 retries per turn unless maxProcessorRetries is raised. Observational memory now exposes viewAttachment in the recall tool, returning native media parts for images and PDFs instead of text-only descriptions.

**「What Changed」** Agents now self-heal transient provider failures, assistant-prefill rejections, and history incompatibilities out of the box. Streaming clients gain a tool-call-resumed chunk to clear pending UI states, while durable and evented execution fixes linear-time thread loading and stop long-running steps from double-running.

**Tags**: `#runtime`, `#tools`, `#permissions`

---

<a id="item-harness-arch-5"></a>
### [OpenAI Agents JS Realtime 0.19.0 Released](https://github.com/openai/openai-agents-js/releases/tag/%40openai/agents-realtime%400.19.0) ⭐️ 7.8/10

OpenAI released @openai/agents-realtime@0.19.0. The release fixes conditional tool approval normalization by binding approvals to isolated normalized execution input in core and Realtime, re-evaluating current policies on durable approval resumes, and rejecting uncopyable normalized values before approval. It also prevents stack overflow when encoding large realtime audio buffers, preserves conversation order when updateHistory corrects or inserts overlapping items, and clears stale tools when switching to a tool-less Realtime agent without a prompt. Default function-tool and Realtime approval parse failures are now redacted, requiring explicit invocation policy for sensitive error traces.

github · github-actions\[bot\] · Oct 5, 16:47

**「设计要点」** Conditional tool approvals now run against isolated normalized input, and durable approval resumes re-evaluate live policies instead of trusting cached state. Realtime audio encoding and conversation history updates received targeted correctness fixes.

**「改了什么」** 0.19.0 binds conditional tool approvals to isolated normalized execution input, re-evaluates policies on durable approval resumes, and redacts approval parse failures. It also fixes realtime audio buffer stack overflow, conversation ordering under overlapping edits, and stale tool cleanup on agent switches.

**Tags**: `#runtime`, `#tools`, `#permissions`

---

<a id="item-harness-arch-6"></a>
### [OpenAI Agents Core 0.19.0](https://github.com/openai/openai-agents-js/releases/tag/%40openai/agents-core%400.19.0) ⭐️ 7.3/10

OpenAI released @openai/agents-core@0.19.0 for the Agents JS runtime. The minor update bounds agent tool streaming callbacks to 1024 pending events by default, configurable via onStreamMaxPendingEvents or restored to unlimited with null. It rejects started checkpoints that lack completed initial input validation, including older snapshots without completion evidence. Conditional tool approvals now evaluate against isolated normalized execution input in core and Realtime, re-evaluate current policies on durable resumes, and reject uncopyable values before approval.

github · github-actions\[bot\] · Oct 5, 16:47

**「Architecture Note」** The tool and permission layer is tightened: streaming backpressure is capped, MCP call provenance is enforced across resumes, and conditional approvals are decoupled from ambient run state. Default function-tool and Realtime approval parse failures are redacted unless an explicit invocation policy permits sensitive error traces.

**「What Changed」** The runtime caps streaming callback buffering at 1024 pending events by default and validates checkpoint completion evidence before resume. MCP calls now enforce recipient binding on resume, while conditional tool approvals isolate normalized execution input and re-evaluate policies on durable resumes.

**Tags**: `#runtime`, `#tools`, `#mcp`, `#permissions`

---

<a id="item-harness-arch-7"></a>
### [E2B 2.52.1 修正构建与重试语义](https://github.com/e2b-dev/E2B/releases/tag/e2b%402.52.1) ⭐️ 6.8/10

E2B 发布 2.52.1 补丁。模板构建的 \`.dockerignore\` 过滤对齐 BuildKit：前导 \`\*\*\` 加字面量（如 \`\*\*.txt\`）现在匹配任意深度；仅命中父目录的否定模式不再重新包含路径；JS SDK 中 \`?\` 和方括号表达式把 BMP 外字符（如 emoji）当作单个字符。502 重试收紧：沙箱创建、fork、快照等资源创建类 POST 遇到 502 直接返回，不再重试，避免重复创建；503 仍对所有操作重试。密钥更新 \`POST /secrets/\{id\}\` 在 502 或连接中断后不再重放，因为每次更新都会追加新版本。

github · github-actions\[bot\] · Oct 5, 12:41

**「设计要点」** 重试策略按幂等性分级：资源创建类 POST 不重试，503 仍全量重试；密钥更新因追加语义被排除在重放之外。

**「改了什么」** 相对上一版，\`.dockerignore\` 匹配规则向 BuildKit 看齐，502 重试从全量重试改为仅安全操作重试，并修复 JS SDK \`WatchHandle.stop\(\)\` 的退出错误。

**Tags**: `#sandbox`, `#runtime`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [OSWorld-Pro：CUA 过程化评测](https://huggingface.co/papers/2609.24890) ⭐️ 7.5/10

Hugging Face Daily Papers 于 2026-10-06 收录 OSWorld-Pro 论文摘要。该基准面向 Computer-Use Agent（CUA），包含 300+ 任务、2,800+ 子目标，基于 67,000 条人工标注构建。评测使用与人类对齐的 LLM-Judge 判定子目标完成度，将评估粒度从 OSWorld 的最终交付物下沉到过程步骤。材料仅提供摘要，完整实验结果与代码发布状态未确认。

rss · Hugging Face Daily Papers · Oct 6, 00:00

**「为什么重要」** 现有 CUA 评测多在数百步后检查最终结果，无法区分失败源于键盘输入误差还是 GUI 点击精度不足。OSWorld-Pro 提供子目标级中间信号，让失败定位有据可循。对构建 coding agent 与 harness 的工程师，这类过程化评测数据可作为调试与观测工具的设计输入。

**「可关注」** 可关注：OSWorld-Pro 的子目标划分与人工标注规模可为自建 CUA 评测提供参照；接入前建议等待完整论文与代码，确认 LLM-Judge 的误判率及任务覆盖范围。

**Tags**: `#eval`, `#coding-agent`, `#observability`

---

<a id="item-agent-engineer-2"></a>
### [PluginRSI Evolves Agent Harnesses with Reusable Plugins](https://huggingface.co/papers/2609.32423) ⭐️ 7.5/10

Published 2026-10-06, PluginRSI represents an agent harness as a composition of atomized plugins. It improves individual plugins independently, accumulates them in a shared library, and recombines them into new harnesses each iteration. The paper claims gains over existing harness optimization methods across software engineering, command-line interaction, and question-answering tasks. Resulting harnesses reportedly retain their advantage when transferred to other solver models without further optimization. The source text is truncated, leaving the full scope of the plugin library&\#x27;s acceleration claims unclear.

rss · Hugging Face Daily Papers · Oct 6, 00:00

**「Why It Matters」** Unlike methods that search over complete harness programs, PluginRSI isolates individual mechanisms into reusable plugins. This offers a concrete architectural pattern for engineers building harnesses, evaluation pipelines, and toolchains that need to transfer improvements across models and task domains.

**「Engineer Takeaway」** Watch: PluginRSI&\#x27;s shared plugin library and recombination loop provide a template for isolating harness mechanisms and reusing them across solver models without re-optimization.

**Tags**: `#harness`, `#eval`, `#orchestration`, `#coding-agent`

---

<a id="item-agent-engineer-3"></a>
### [Cowork 从本地 VM 迁至云端沙箱](https://simonwillison.net/2026/Oct/5/felix-rieseberg/) ⭐️ 6.0/10

Felix Rieseberg 说明 Cowork 架构调整：旧版推理在云端，工具调用在本地 Anthropic VM 执行，用户抱怨磁盘、电池、性能开销，且合盖后任务停止；新版将推理与 VM 均置于云端，每会话独立沙箱，不共享状态，VM 需要用户设备文件时由桌面应用代理该文件访问工具调用。Rieseberg 称这能支持手机使用、保持任务运行、避免本地 VM 耗电。该信息来自社交媒体引述，非官方工程博客，细节有限。

rss · Simon Willison · Oct 5, 23:56

**「为什么重要」** 这呈现了 agent 工具执行从本地 VM 迁往云端沙箱的一条路径：桌面应用转为本地文件访问的代理，会话级沙箱替代共享本地环境。本地 VM 的磁盘、电池与中断代价，是本地执行方案的常见瓶颈。

**「可关注」** 可关注：工具执行迁移到云端后，本地文件访问需要显式代理层，桌面应用成为文件工具调用的 broker；每会话独立沙箱也改变了状态隔离方式。

**Tags**: `#harness`, `#coding-agent`, `#permissions`, `#orchestration`

---

<a id="item-agent-engineer-4"></a>
### [HF daily paper: ASCENT: Online Test-Time Training of Long-Horizon Agents via Self-Distillation of Verified Experience](https://huggingface.co/papers/2610.05303) ⭐️ 5.5/10

A paper proposes ASCENT, an online test-time training method that updates LLM agent weights via self-distillation of verified execution trajectories during deployment.

rss · Hugging Face Daily Papers · Oct 6, 00:00

**Tags**: `#harness`, `#eval`, `#memory`

---

<a id="item-agent-engineer-5"></a>
### [HF daily paper: CANOPY: Adaptive-Granularity Evidence Compression for Multimodal RAG](https://huggingface.co/papers/2610.00923) ⭐️ 5.5/10

Proposes CANOPY, a hierarchical framework that adaptively compresses retrieved multimodal evidence by scoring regions against the query to balance context retention and granularity.

rss · Hugging Face Daily Papers · Oct 6, 00:00

**Tags**: `#rag`, `#multimodal`, `#context-compression`

---

## AI Daily

<a id="item-ai-daily-1"></a>
### [OpenAI 推 ChatGPT 视觉广告](https://openai.com/index/new-chatgpt-ads-format-and-measurement) ⭐️ 9.8/10

OpenAI 于 2026 年 10 月 5 日宣布在 ChatGPT 中推出新的视觉广告格式，并扩展面向广告主的测量工具、归因合作伙伴与品牌适配能力。更新覆盖广告呈现、效果衡量与品牌安全环节。目前仅见官方说明，缺乏社区讨论与第三方验证。

rss · OpenAI Blog · Oct 5, 10:00

**「为什么重要」** 作为主流实验室在 ChatGPT 内广告产品与测量体系的实质更新，此次变化为广告主提供了新的投放与评估选项。

**「可关注」** 可关注：视觉广告格式与测量、归因能力同步扩展，OpenAI 正在补齐 ChatGPT 广告闭环的基础设施。

**Tags**: `#product`, `#lab`, `#industry`, `#policy`

---

<a id="item-ai-daily-2"></a>
### [OpenAI 阐述欧盟文本溯源方案](https://openai.com/index/eu-text-provenance) ⭐️ 9.3/10

OpenAI 发布博文，阐述在欧盟文本溯源规则下的水印方案。内容涵盖水印适用范围、检测机制，以及访问权限为何优先面向研究人员。

rss · OpenAI Blog · Oct 5, 15:00

**「为什么重要」** 欧盟对 AI 生成文本提出溯源要求，OpenAI 作为主要实验室给出官方回应。水印与检测机制是文本溯源规则的核心工程实现。

**「可关注」** 可关注：水印访问权限从研究人员开始，OpenAI 同步说明适用范围与检测机制。

**Tags**: `#policy`, `#lab`, `#industry`

---

<a id="item-ai-daily-3"></a>
### [ReviewBench: An open benchmark for AI code review](https://github.blog/ai-and-ml/github-copilot/reviewbench-an-open-benchmark-for-ai-code-review/) ⭐️ 8.8/10

GitHub launches ReviewBench, an open benchmark for evaluating AI code review agents built on representative pull requests with multi-source ground truth and production-aligned metrics.

rss · GitHub Blog · Oct 5, 15:59

**Tags**: `#eval`, `#open-source`, `#product`, `#lab`

---

## AI Deals

<a id="item-ai-deals-1"></a>
### [Show HN: Free Public API Lab](https://sondahub.com/) ⭐️ 5.0/10

Free no-account public API playground supporting REST, OData, MCP, FHIR, SOAP, and Socket.IO, available now on sondahub.com and GitHub.

rss · HN Free API / Credits · Oct 5, 20:58

**Tags**: `#api`, `#free-tier`, `#limited-free`

---