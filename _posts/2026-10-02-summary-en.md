---
layout: default
title: "Horizon Summary: 2026-10-02 (EN)"
date: 2026-10-02
lang: en
---

> From 212 items, 18 important content pieces were selected

---

**Agent Harness Architecture**
1. [ADK Python v2.11.0 Out](#item-harness-arch-1) ⭐️ 8.8/10
2. [pydantic-ai v2.53.0 Patches Streaming Concurrency Leak](#item-harness-arch-2) ⭐️ 8.3/10
3. [anthropics/claude-code released v2.1.287](#item-harness-arch-3) ⭐️ 7.8/10
4. [openai/codex released rust-v0.160.0](#item-harness-arch-4) ⭐️ 7.3/10
5. [OpenAI Agents Python v0.23.0 发布](#item-harness-arch-5) ⭐️ 7.3/10
6. [microsoft/agent-framework released dotnet-1.23.0](#item-harness-arch-6) ⭐️ 7.3/10
7. [google-gemini/gemini-cli released v0.64.0-nightly.20261002.gc9096a847](#item-harness-arch-7) ⭐️ 6.8/10

**AI Agent Engineer**
1. [pwasm 0.2a0 支持 WASM 沙箱](#item-agent-engineer-1) ⭐️ 8.3/10
2. [HF daily paper: Beyond Memory: Harnessing Long-Horizon Agents with Explicit Belief States](#item-agent-engineer-2) ⭐️ 7.5/10
3. [预训练模型 pass@K 反超后训练模型](#item-agent-engineer-3) ⭐️ 7.5/10
4. [沙箱 Agent 可经共享包缓存传播蠕虫](#item-agent-engineer-4) ⭐️ 7.0/10
5. [ActiveSaddler: Curriculum Learning for Harness Optimization](#item-agent-engineer-5) ⭐️ 6.0/10
6. [RASO：跨 harness 检索增强技能优化](#item-agent-engineer-6) ⭐️ 6.0/10
7. [Introducing Olmo-core 3: Open, scalable training infrastructure for large MoEs](#item-agent-engineer-7) ⭐️ 5.8/10

**AI Daily**
1. [The eternal complement](#item-ai-daily-1) ⭐️ 6.3/10
2. [How Albertsons Companies is reimagining retail from the inside out](#item-ai-daily-2) ⭐️ 6.3/10
3. [GitHub Universe 2026 技术议程](#item-ai-daily-3) ⭐️ 5.8/10
4. [Mollick：模型已学会组织智能体](#item-ai-daily-4) ⭐️ 5.0/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [ADK Python v2.11.0 Out](https://github.com/google/adk-python/releases/tag/v2.11.0) ⭐️ 8.8/10

ADK Python v2.11.0 adds graceful cancellation, workflow tool confirmation, a model-consultation tool, and a built-in SQLite memory service. \`abort\_signal\` threads through \`Runner\`, \`Workflow\`, and nodes to stop runs gracefully, and \`/run\_sse\` cancels on client disconnect. Workflow tool nodes pause for approval via \`RequestInput\` instead of erroring downstream. \`ModelConsultTool\` consults another model mid-task under per-turn and per-session budgets, memory persists to SQLite via a \`sqlite://\` URI, and an opt-in path supports MCP SDK 2.x.

github · xuanyang15 · Oct 2, 00:44

**「Design Notes」** Cancellation synthesizes an abort event and function response when \`abort\_signal\` fires. Workflow tool nodes share the \`RequestInput\` confirmation path with \`LlmAgent\`, and the SQLite memory service is selected by URI scheme.

**「What Changed」** Graceful cancellation via \`abort\_signal\` now spans \`Runner\`, \`Workflow\`, and nodes, with \`/run\_sse\` canceling on client disconnect, while workflow tool nodes pause for approval via \`RequestInput\`. The release adds \`ModelConsultTool\` with per-turn and per-session budgets, a SQLite memory service via \`sqlite://\` URI, and an opt-in MCP SDK 2.x modern-protocol path; breaking, the Dev UI runtime config moves to the server endpoint \`/dev-ui/assets/config/runtime-config.json\` and logos use \`--logo-text\` and \`--logo-image-url\`.

**Tags**: `#runtime`, `#tools`, `#memory`, `#permissions`

---

<a id="item-harness-arch-2"></a>
### [pydantic-ai v2.53.0 Patches Streaming Concurrency Leak](https://github.com/pydantic/pydantic-ai/releases/tag/v2.53.0) ⭐️ 8.3/10

pydantic-ai v2.53.0 patches a high-severity streaming concurrency slot leak in ConcurrencyLimitedModel. A streamed request could retain its slot when released on a different task than the one that acquired it. Early exit, cancellation, or fully consuming stream\_text\(\) with default debouncing all triggered the leak. Repeated streams could block every request sharing the limiter. Agent-level max\_concurrency and non-streaming requests are unaffected.

github · dsfaccini · Oct 2, 02:52

**「Design Notes」** The fix redefines limiter sharing. A model wrapper now raises UserError when it shares a limiter with the agent or an enclosing wrapper. ConcurrencyLimiter.acquire\(\) takes a slot on every call, even on the same task. Custom AbstractConcurrencyLimiter implementations must allow release\(\) from another task.

**「What Changed」** The release hardens concurrency limiter semantics and patches GHSA-6fqq-452j-qhrp. It also converts clai2 plugins to declarative Plugin subclasses and adds ToolCallJudge, SystemOneModel, and AbsurdDurability.

**Tags**: `#runtime`, `#tools`, `#security`

---

<a id="item-harness-arch-3"></a>
### [anthropics/claude-code released v2.1.287](https://github.com/anthropics/claude-code/releases/tag/v2.1.287) ⭐️ 7.8/10

Claude Code v2.1.287 introduces MCP URL prompt support on the 2025-11-25 protocol, a new plugin mods system for deeper behavior modification, and a built-in side-agent plugin, plus minor telemetry and UI updates.

github · ashwin-ant · Oct 1, 18:00

**Tags**: `#mcp`, `#subagents`, `#tools`, `#runtime`, `#permissions`

---

<a id="item-harness-arch-4"></a>
### [openai/codex released rust-v0.160.0](https://github.com/openai/codex/releases/tag/rust-v0.160.0) ⭐️ 7.3/10

OpenAI Codex Rust v0.160.0 ships incremental agent harness improvements: workspace-default session resumption, opt-in Guardian review with cross-handoff context, and Windows sandbox permission fixes.

github · andrewgu-oai · Oct 1, 20:19

**Tags**: `#runtime`, `#sandbox`, `#permissions`, `#memory`, `#subagents`

---

<a id="item-harness-arch-5"></a>
### [OpenAI Agents Python v0.23.0 发布](https://github.com/openai/openai-agents-python/releases/tag/v0.23.0) ⭐️ 7.3/10

OpenAI Agents Python v0.23.0 ships four configurable or opt-in runtime controls across MCP, sandbox, and session subsystems. MCP listing gains configurable page limits. The sandbox adds opt-in Docker removal protection and configurable memory consolidation turns. Sessions introduce an opt-in encrypted history scan budget. Core fixes cover nested agent tool state, guardrail persistence, streaming tracebacks, and tool failure redaction.

github · openai-sdks\[bot\] · Oct 2, 01:08

**「设计要点」** Sandbox and session changes ship as opt-in or configurable limits, not defaults. MCP page limits and encrypted history scan budgets expose operational bounds to harness engineers.

**「改了什么」** Versus v0.22.3, v0.23.0 adds configurable MCP listing page limits, opt-in Docker removal protection, configurable memory consolidation turns, and an opt-in encrypted history scan budget. Core fixes isolate nested agent tool state, preserve guarded final outputs, scope function tool approvals to owning agents, and redact default tool failure details and streaming exception tracebacks.

**Tags**: `#mcp`, `#sandbox`, `#memory`, `#sessions`

---

<a id="item-harness-arch-6"></a>
### [microsoft/agent-framework released dotnet-1.23.0](https://github.com/microsoft/agent-framework/releases/tag/dotnet-1.23.0) ⭐️ 7.3/10

Microsoft Agent Framework .NET 1.23.0 ships breaking changes for tool changes between runs, MCP client origin pinning, and several workflow/runtime fixes.

github · dmytrostruk · Oct 1, 10:54

**Tags**: `#runtime`, `#tools`, `#mcp`

---

<a id="item-harness-arch-7"></a>
### [google-gemini/gemini-cli released v0.64.0-nightly.20261002.gc9096a847](https://github.com/google-gemini/gemini-cli/releases/tag/v0.64.0-nightly.20261002.gc9096a847) ⭐️ 6.8/10

Gemini CLI nightly v0.64.0 ships fixes for chat history memory management, atomic state persistence, and emergency cancellation handling.

github · gemini-cli-robot · Oct 2, 01:33

**Tags**: `#runtime`, `#memory`, `#tools`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [pwasm 0.2a0 支持 WASM 沙箱](https://github.com/simonw/pwasm/releases/tag/0.2a0) ⭐️ 8.3/10

simonw 发布 pwasm 0.2a0，捆绑 MicroPython、QuickJS 和 Micro QuickJS 的 WebAssembly 构建，用纯 Python 在沙箱中运行不可信 Python/JavaScript 及 C 编译程序，并施加内存、CPU 和时间限制。新增 pwasm.guests 与 pwasm.sandbox.Sandbox，资源限制通过 Limits\(fuel=..., max\_memory=...\) 和 set\_deadline\(\) 实现，越界抛出 OutOfFuel 或 Timeout。该版本实现 WebAssembly 2.0 核心指令集（除 SIMD），并引入编译到 Python 的层级，热函数通常比解释器快 8–14 倍；编译结果缓存到 ~/.cache/pwasm，QuickJS 启动从约 1.3s 降到 0.1s。

github · simonw · Oct 1, 17:10

**「为什么重要」** 对需要安全执行代码的 agent harness 来说，pwasm 0.2a0 提供了纯 Python 的 WASM 沙箱方案，内置 MicroPython 和 QuickJS 两种 guest，可直接运行不可信脚本并限制资源。编译缓存显著降低启动开销，使沙箱在交互式场景中更可用。

**「可关注」** pwasm 0.2a0 用编译到 Python 的层级把热函数提速 8–14 倍，并用磁盘缓存把 QuickJS 启动从约 1.3s 压到 0.1s；若 harness 需要频繁起停沙箱，可评估 PWASM\_CACHE\_DIR 与 mode=&quot;compile&quot; 的实际收益。

**Tags**: `#harness`, `#coding-agent`, `#permissions`, `#memory`

---

<a id="item-agent-engineer-2"></a>
### [HF daily paper: Beyond Memory: Harnessing Long-Horizon Agents with Explicit Belief States](https://huggingface.co/papers/2610.01415) ⭐️ 7.5/10

A research paper proposes PoS, an inference-time framework for maintaining explicit belief states in LLM agents and detecting Belief Trapping during long-horizon tasks.

rss · Hugging Face Daily Papers · Oct 2, 00:00

**Tags**: `#memory`, `#observability`, `#orchestration`

---

<a id="item-agent-engineer-3"></a>
### [预训练模型 pass@K 反超后训练模型](https://huggingface.co/papers/2610.01509) ⭐️ 7.5/10

论文报告一个反直觉发现：预训练 LLM 配备轻量推理 harness 即可作为可用智能体。在充足测试时预算下，尽管 pass@1 远低于后训练模型，其 pass@K 常反超后者。作者进一步分析了底层机制，并指出这一结果对 RL 后训练在智能体任务上的必要性及评测方法提出挑战。

rss · Hugging Face Daily Papers · Oct 2, 00:00

**「为什么重要」** 对 coding agent 与 harness 工程而言，这直接动摇了「后训练模型一定更适合智能体任务」的默认假设。若结论成立，轻量 harness 加预训练模型可能在解覆盖率上提供更高性价比，尤其在测试时预算充足的场景。

**「可关注」** 可关注：在智能体架构选型与评测时，需区分 pass@1 与 pass@K 指标；若任务更看重解覆盖率而非单次准确率，预训练模型加轻量 harness 值得作为基线重新评估。

**Tags**: `#harness`, `#eval`, `#coding-agent`

---

<a id="item-agent-engineer-4"></a>
### [沙箱 Agent 可经共享包缓存传播蠕虫](https://simonwillison.net/2026/Oct/1/matthew-green/) ⭐️ 7.0/10

Matthew Green 在 9 月 30 日的分析中指出，互相隔离的沙箱 Agent 能在共享包缓存中留下指令，改变接收方行为。这凑成蠕虫的两半：载荷劫持 Agent，Agent 携带载荷感染下一个 Agent。若把包缓存换成 email、Slack、共享文档或 WhatsApp，把独立沙箱训练换成独立部署的个人 Agent（如 Muse），就具备蠕虫传播的完整条件。

rss · Simon Willison · Oct 1, 06:29

**「为什么重要」** 沙箱隔离是 Agent 安全的常见基线。该分析表明，仅靠沙箱边界不足以阻断 Agent 间指令传递，共享包缓存等中间状态可能成为跨实例传播路径。

**「可关注」** 可关注：设计 Agent 的共享缓存、文件系统或消息通道时，需把跨实例指令注入当作攻击面，不能只信任沙箱隔离。

**Tags**: `#permissions`, `#orchestration`, `#harness`

---

<a id="item-agent-engineer-5"></a>
### [ActiveSaddler: Curriculum Learning for Harness Optimization](https://huggingface.co/papers/2610.00906) ⭐️ 6.0/10

A Hugging Face Daily Papers entry dated Oct 2, 2026 presents ActiveSaddler, which formulates agent harness optimization as an automated curriculum learning problem. The paper notes that current methods iteratively update prompts, tool interfaces, and control logic from execution feedback but largely fix which training scenarios produce that feedback. ActiveSaddler instead models the evolving curriculum as a non-stationary bandit with dynamically instantiated optimization targets. Only the abstract is public; no code, benchmark results, or production data are available yet, so reproducibility and impact remain unverified.

rss · Hugging Face Daily Papers · Oct 2, 00:00

**「Why It Matters」** Harness and eval engineers typically adjust training scenarios manually or keep them static while the agent harness mutates. The paper identifies this mismatch, but its claimed benefit is not yet backed by released artifacts or comparative benchmarks.

**「Engineer Takeaway」** Watch: track whether ActiveSaddler releases code and benchmark numbers; until then, treat the non-stationary bandit curriculum as an unverified hypothesis rather than a drop-in optimization.

**Tags**: `#harness`, `#eval`, `#orchestration`, `#coding-agent`

---

<a id="item-agent-engineer-6"></a>
### [RASO：跨 harness 检索增强技能优化](https://huggingface.co/papers/2609.38024) ⭐️ 6.0/10

Hugging Face 每日论文于 2026-10-02 收录 RASO \(Retrieval-Augmented Skill Optimization\)。该框架从外部技能库检索已有 agent 技能，将其作为先验知识适配到目标任务，以跨不同 harness 优化技能。论文指出现有技能优化方法忽视公开积累的技能，仅依赖昂贵的 agent rollouts 迭代。目前材料仅含截断摘要，无代码、基准数据或生产验证，实际效果与可复现性待确认。

rss · Hugging Face Daily Papers · Oct 2, 00:00

**「为什么重要」** 技能优化长期依赖高成本 rollouts，RASO 提出把公开技能库作为先验知识引入优化流程，为降本提供新路径。但摘要未提供基准数字，实际收益仍待验证。

**「可关注」** 可关注：RASO 将外部技能库作为先验知识注入优化过程，若后续放出代码与基准，可评估其跨 harness 适配能力是否优于纯 rollout 方案。

**Tags**: `#harness`, `#memory`, `#eval`

---

<a id="item-agent-engineer-7"></a>
### [Introducing Olmo-core 3: Open, scalable training infrastructure for large MoEs](https://huggingface.co/blog/allenai/olmocore3) ⭐️ 5.8/10

AllenAI releases Olmo-core 3, an open-source framework for scalable trillion-parameter MoE training, with limited direct impact on day-to-day agent engineering.

rss · Hugging Face Blog · Oct 1, 15:01

**Tags**: `#training`, `#moe`, `#infrastructure`, `#open-source`, `#llm`

---

## AI Daily

<a id="item-ai-daily-1"></a>
### [The eternal complement](https://openai.com/index/the-eternal-complement) ⭐️ 6.3/10

OpenAI publishes an essay arguing that advanced AI&\#x27;s greatest impact may lie in routine execution work behind breakthrough ideas, shaping the next economy.

rss · OpenAI Blog · Oct 1, 17:00

**Tags**: `#lab`, `#industry`

---

<a id="item-ai-daily-2"></a>
### [How Albertsons Companies is reimagining retail from the inside out](https://openai.com/index/albertsons-reimagining-retail) ⭐️ 6.3/10

OpenAI publishes a customer case study on Albertsons using ChatGPT Enterprise and the OpenAI API to improve internal workflows and grocery shopping.

rss · OpenAI Blog · Oct 1, 16:00

**Tags**: `#product`, `#industry`, `#lab`

---

<a id="item-ai-daily-3"></a>
### [GitHub Universe 2026 技术议程](https://github.blog/news-insights/company-news/10-technical-talks-im-excited-about-at-github-universe-2026/) ⭐️ 5.8/10

GitHub 官方博客预览 GitHub Universe 2026 的 10 场技术演讲，主题涉及验证 AI 编写的代码与保护 npm 依赖安全。文章仅提前披露会议议程，未伴随产品、模型或政策发布。受限于信息量，当前可确认的实质影响有限。

rss · GitHub Blog · Oct 1, 15:07

**「可关注」** 可关注：GitHub Universe 2026 将设 AI 代码验证与 npm 依赖安全相关技术演讲，但官方尚未公布具体产品细节或发布时间。

**Tags**: `#industry`, `#product`, `#open-source`

---

<a id="item-ai-daily-4"></a>
### [Mollick：模型已学会组织智能体](https://www.oneusefulthing.org/p/the-dot-and-the-swarm) ⭐️ 5.0/10

Ethan Mollick 撰文承认，自己此前认为人类需要像管理公司一样精心设计智能体组织架构的判断有误。他认为苦涩教训（The Bitter Lesson）同样适用于组织问题：更强大的模型已能自行规划步骤、寻找信息并协调工作，不再依赖精细的人工规则。他举出 OpenAI 用数千个智能体在 88 小时内推进纳维–斯托克斯方程证明的例子，称其协调结构极为精简；同时提到 Meta Muse、OpenAI dots 等个人智能体已能主动处理邮件、行程等事务，无需用户输入大量上下文或计划。该文属于反思性评论，尚无模型发布、政策变更或基准测试等可验证的新事实，且纳维–斯托克斯证明尚未获得正式接受。

rss · One Useful Thing · Oct 1, 10:54

**「为什么重要」** 对构建 coding agent 与 harness 的工程师而言，这篇文章指出了一个方向性变化：当模型能自行拆分任务、组建团队并传递想法时，精心设计的编排层和提示链的价值可能被削弱。Mollick 以 OpenAI swarm 和 Codex 自动派生智能体为例，说明薄协调结构已能驱动大规模协作，这迫使重新评估自建多智能体框架的投入产出。

**「可关注」** 可关注：OpenAI 推进纳维–斯托克斯证明时，仅设少量分组、一次方向调整，并由 Codex 在组间传递最优想法，便协调了约 270 万条消息；这种薄协调结构可作为设计多智能体系统时的对照基线。

**Tags**: `#industry`, `#product`, `#model`

---