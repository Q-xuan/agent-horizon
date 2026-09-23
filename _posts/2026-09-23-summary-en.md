---
layout: default
title: "Horizon Summary: 2026-09-23 (EN)"
date: 2026-09-23
lang: en
---

> From 222 items, 20 important content pieces were selected

---

**Agent Harness Architecture**
1. [vllm-project/vllm released v0.30.0](#item-harness-arch-1) ⭐️ 8.8/10
2. [2.1.280](#item-harness-arch-2) ⭐️ 8.8/10
3. [cline/cline released v4.1.20](#item-harness-arch-3) ⭐️ 8.3/10
4. [Cline SDK v0.0.85 Adds Retry and Model-Aware Output Scaling](#item-harness-arch-4) ⭐️ 8.3/10
5. [Cline desktop v0.0.33](#item-harness-arch-5) ⭐️ 8.3/10
6. [Cline CLI v3.0.64 Released](#item-harness-arch-6) ⭐️ 8.3/10
7. [openai/codex released rust-v0.156.0](#item-harness-arch-7) ⭐️ 7.8/10
8. [LangChain agents-from-scratch Trends on GitHub](#item-harness-arch-8) ⭐️ 5.5/10

**AI Agent Engineer**
1. [Transformers 支持 GGUF](#item-agent-engineer-1) ⭐️ 8.3/10
2. [HF daily paper: RRSI: Regularized Recursive Self-Improvement of Agent Harnesses](#item-agent-engineer-2) ⭐️ 7.5/10
3. [GameHorizon Suite 发布](#item-agent-engineer-3) ⭐️ 7.5/10
4. [AISI and EvalEval Release Shared Infrastructure for Reproducible Evaluation Reporting](#item-agent-engineer-4) ⭐️ 6.3/10
5. [GPT-6 Sol 与 Luna 发布](#item-agent-engineer-5) ⭐️ 6.0/10
6. [onPanda：token 级校正标注工具](#item-agent-engineer-6) ⭐️ 6.0/10
7. [Claude Opus 5.5 发布并降价](#item-agent-engineer-7) ⭐️ 5.5/10
8. [HF daily paper: Transferring the Intelligence of VLMs to Robotic Control](#item-agent-engineer-8) ⭐️ 5.5/10

**AI Daily**
1. [Introducing GPT-6 Sol and Luna](#item-ai-daily-1) ⭐️ 9.8/10
2. [OpenAI 改进 GPT-6 提示缓存](#item-ai-daily-2) ⭐️ 8.8/10
3. [OpenAI 发布第三方评估原则](#item-ai-daily-3) ⭐️ 8.3/10
4. [Opus 5.5 降价：缓存读取降 60%](#item-ai-daily-4) ⭐️ 6.8/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [vllm-project/vllm released v0.30.0](https://github.com/vllm-project/vllm/releases/tag/v0.30.0) ⭐️ 8.8/10

vLLM v0.30.0 is a major official release adding new models, a persistent GPU weight-cache daemon for faster restarts via CUDA IPC, and a CPU backend with sparse MLA kernels.

github · khluu · Sep 22, 05:20

**Tags**: `#runtime`, `#models`, `#prefix-cache`

---

<a id="item-harness-arch-2"></a>
### [2.1.280](https://code.claude.com/docs/en/changelog#2-1-280) ⭐️ 8.8/10

Claude Code 2.1.280 ships Opus 5.5 as the default model, adds an MCP description length cap env var and OpenTelemetry hook output metrics, and fixes symlinked-write permission checks and auto-mode retry loops.

rss · Claude Code Changelog · Sep 22, 16:48

**Tags**: `#runtime`, `#tools`, `#mcp`, `#permissions`, `#sandbox`

---

<a id="item-harness-arch-3"></a>
### [cline/cline released v4.1.20](https://github.com/cline/cline/releases/tag/v4.1.20) ⭐️ 8.3/10

Cline v4.1.20 parallelizes sub-agent tool calls within a step and scales default output budgets to model limits.

github · github-actions\[bot\] · Sep 22, 20:45

**Tags**: `#runtime`, `#subagents`, `#tools`

---

<a id="item-harness-arch-4"></a>
### [Cline SDK v0.0.85 Adds Retry and Model-Aware Output Scaling](https://github.com/cline/cline/releases/tag/sdk/sdk/v0.0.85) ⭐️ 8.3/10

Cline SDK v0.0.85 adds runtime retries for output-token limit exhaustion and scales default output allowances by model capability. Turns that hit the output-token limit without a usable tool call now retry up to three consecutive times with a reminder to respond concisely and split work across tool calls; the counter resets on tool-call progress and at run start, and exhaustion still fails with the existing error. When no request limit or caller default is supplied and the model advertises an output limit, the gateway uses \`max\(32000, floor\(maxOutputTokens \* 0.3\)\)\` instead of a flat 32,000, raising defaults only for models above roughly 106,667 tokens. The model catalog refreshes to 6,237 models across 209 providers, and 10 providers that do not pin a default in \`builtins.ts\` resolve to new models.

github · github-actions\[bot\] · Sep 22, 08:13

**「Design Notes」** The runtime emits \`turn-finished\` before each recovery iteration to keep iteration events paired, and empty max-tokens responses follow the same recovery path as exhausted turns. Model-output and remaining-context clamps and the reasoning-budget floor still apply after the new default scaling.

**「What Changed」** Output-token limit exhaustion now triggers up to three retries with concise-response reminders instead of failing the run immediately. Default output allowances scale with model capabilities via \`max\(32000, floor\(maxOutputTokens \* 0.3\)\)\`, affecting only models above roughly 106,667 tokens while leaving explicit limits and caller defaults unchanged.

**Tags**: `#runtime`, `#tools`, `#planning`

---

<a id="item-harness-arch-5"></a>
### [Cline desktop v0.0.33](https://github.com/cline/cline/releases/tag/desktop-v0.0.33) ⭐️ 8.3/10

Cline desktop v0.0.33 adds per-task git worktree isolation and fixes auto-compaction for long sessions. Picking Worktree on the welcome screen cuts a fresh \`cline/&lt;id&gt;\` branch, creates a worktree under \`~/.cline/worktrees/\`, and runs the task there so the agent never touches the main working tree. Auto-compaction had never run on desktop because the sidecar opted sessions into checkpoints but never into compaction; the 90% trigger is now installed. Deleting a task removes its worktree and branch, discarding uncommitted changes, unless another session still lives there.

github · github-actions\[bot\] · Sep 22, 09:07

**「Design Notes」** Task isolation uses git worktrees as a lightweight sandbox: each new thread gets its own branch and directory, with cleanup tied to task deletion. The memory layer now follows the session&\#x27;s current credentials and model during compaction, and output-limit retries use a bigger default budget for models with large advertised limits.

**「What Changed」** New threads can run in isolated git worktrees, and long sessions now compact automatically. Windows relaunch focuses the existing window and hides to the tray, SSH hosts support brand-new chats, and the model catalog refreshed to 209 providers and 6,237 models.

**Tags**: `#runtime`, `#sandbox`, `#memory`

---

<a id="item-harness-arch-6"></a>
### [Cline CLI v3.0.64 Released](https://github.com/cline/cline/releases/tag/cli-v3.0.64) ⭐️ 8.3/10

Cline CLI v3.0.64 stops runs from dying when a model turn hits its output-token limit before a tool call. The turn retries up to three times with a conciseness reminder, splitting work across tool calls. Default output budgets now use 30% of a model&\#x27;s advertised output limit or 32,000 tokens, whichever is larger, leaving models under roughly 107k output tokens unchanged. The model catalog refreshes from 6,188 to 6,237 entries across 209 providers, with new defaults for 10 providers.

github · github-actions\[bot\] · Sep 22, 08:25

**「Design Notes」** Retry logic intercepts output-token-limit failures before tool execution and prompts the model to redistribute work across calls. Output budgets derive from model metadata rather than fixed constants.

**「What Changed」** Runs survive output-token-limit errors before tool calls via up to three retries, and large-output models default to 30% of their advertised limit instead of 32,000 tokens. The catalog adds 49 models and updates defaults for 10 providers.

**Tags**: `#runtime`, `#tools`, `#planning`

---

<a id="item-harness-arch-7"></a>
### [openai/codex released rust-v0.156.0](https://github.com/openai/codex/releases/tag/rust-v0.156.0) ⭐️ 7.8/10

Codex Rust v0.156.0 enables worktree sessions by default, adds daemon management and voice support, and ships a fullscreen TUI, marking a significant runtime feature update.

github · github-actions\[bot\] · Sep 22, 19:51

**Tags**: `#runtime`, `#tools`, `#subagents`, `#sandbox`

---

<a id="item-harness-arch-8"></a>
### [LangChain agents-from-scratch Trends on GitHub](https://github.com/langchain-ai/agents-from-scratch) ⭐️ 5.5/10

LangChain&\#x27;s agents-from-scratch repository is an official tutorial trending on GitHub. It builds an ambient email assistant with Gmail API access across four sections, each pairing a notebook with code in src/email\_assistant. The progression covers agent basics, evaluation, human-in-the-loop, and memory. It is an educational guide rather than a runtime release or architectural redesign.

rss · GitHub Trending Daily · Sep 22, 23:29

**「设计要点」** Code is organized into four progressive modules under src/email\_assistant, covering agent basics, evaluation, human-in-the-loop, and memory. The end goal is an ambient assistant that manages email through the Gmail API.

**Tags**: `#memory`, `#eval`, `#tools`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [Transformers 支持 GGUF](https://huggingface.co/blog/transformers-llama-cpp-quants) ⭐️ 8.3/10

Transformers 库新增 GGUF 量化模型加载支持。通过 kernels 库复用 ggml/Metal 内核，在 Apple Silicon 上直接运行量化权重，无需反量化。初始支持 Qwen3.5 架构，覆盖 Q4\_K\_M、Q5\_K\_M、Q6\_K 等量化等级。在 M2 Max 上对比 llama.cpp，三个检查点（小型稠密、更大稠密、MoE）的生成速度接近 llama.cpp；但 Transformers 测量包含 prefill，llama-bench 仅测 decode，条件不完全一致。

rss · Hugging Face Blog · Sep 22, 00:00

**「为什么重要」** 本地推理与 coding agent 部署多了一条路径：同一份 GGUF 检查点可直接接入 transformers 生态，并通过 transformers serve 暴露 OpenAI 兼容接口，供 Jan、Pi 等客户端调用。对已在 transformers 上构建工具链的工程师，减少了在 llama.cpp 与 transformers 之间切换的成本。

**「可关注」** 可关注：GGUF 加载路径依赖 kernels 库与特定 PyTorch 版本，且当前仅支持 Apple Silicon 与 Qwen3.5 架构；若内核获取失败会回退到 sdpa 或反量化，显存与速度表现会变化，接入前需在目标硬件上验证。

**Tags**: `#coding-agent`, `#harness`

---

<a id="item-agent-engineer-2"></a>
### [HF daily paper: RRSI: Regularized Recursive Self-Improvement of Agent Harnesses](https://huggingface.co/papers/2609.24972) ⭐️ 7.5/10

论文提出 RRSI，通过正则化约束 agent harness 的递归自我改进过程，以缓解过拟合并提升分布外泛化能力。

rss · Hugging Face Daily Papers · Sep 22, 00:00

**Tags**: `#harness`, `#eval`, `#memory`, `#orchestration`

---

<a id="item-agent-engineer-3"></a>
### [GameHorizon Suite 发布](https://huggingface.co/papers/2609.25001) ⭐️ 7.5/10

Hugging Face 每日论文收录 GameHorizon Suite，面向 gameplay 发布大规模 AAA 数据集与多 horizon 评测基准，覆盖多样模型家族。套件含三部分：自动多 horizon 指令标注 pipeline GameHorizon-Annotator、大规模 AAA 数据集 GameHorizon-Data，以及配套评测基准。现有工作或游戏覆盖窄、或缺语言指令、或依赖高方差在线 rollout，该套件针对这些缺口提供统一数据与评测方案。论文 2026-09-22 上线，获 110 次 upvote；当前范围限于 gameplay，未覆盖通用 coding agent。

rss · Hugging Face Daily Papers · Sep 22, 00:00

**「为什么重要」** 对 coding agent 工程师而言，多 horizon 规划与评测是跨域共同能力；GameHorizon 将视觉理解、指令分解、目标规划和精确动作控制纳入同一基准，方法可参考，但目前仅在 gameplay 域验证，尚未证明对通用编码任务有效。

**「可关注」** 可关注：GameHorizon-Annotator 的自动多 horizon 指令标注 pipeline，以及用离线 AAA 数据集替代高方差在线 rollout 的评测设计。

**Tags**: `#eval`, `#agent`, `#benchmark`, `#dataset`, `#planning`

---

<a id="item-agent-engineer-4"></a>
### [AISI and EvalEval Release Shared Infrastructure for Reproducible Evaluation Reporting](https://huggingface.co/blog/evaleval-aisi) ⭐️ 6.3/10

UK AISI and EvalEval have moved their collaboration into implementation, releasing verified evaluation results through the Every Eval Ever schema and the Evaluation Cards platform. AISI published results, context, and configuration for five benchmarks—HealthBench, FrontierMath, Humanity&\#x27;s Last Exam, SWE-Bench Pro, and Terminal-Bench 2.0—covering six frontier models: Claude Opus 4, Claude Opus 4.5, Claude Opus 4.6, GPT-5, GPT-5.2, and GPT-5.4. The release includes two related cyber evaluations, Cyber CTFs and The Last Ones, with a partially overlapping model set. It accompanies AISI&\#x27;s paper on how inference compute and evaluation protocol shape frontier LLM benchmark performance.

rss · Hugging Face Blog · Sep 22, 00:00

**「Why It Matters」** Evaluation results are often reported without enough detail to reproduce, and re-running evaluations can be prohibitively expensive. This release provides verified reference points with setup information, allowing researchers to examine how protocol and inference compute choices influence reported performance—for example, on Humanity&\#x27;s Last Exam, where scores shift with evaluation protocol and token budget.

**「Worth Watching」** Worth watching: whether broader adoption of the Every Eval Ever schema by other evaluators enables reliable comparison of scores produced under meaningfully different conditions, and how transcript-level transparency in Evaluation Cards supports diagnosis beyond simple reproducibility.

**Tags**: `#eval`, `#benchmark`, `#reproducibility`, `#infrastructure`

---

<a id="item-agent-engineer-5"></a>
### [GPT-6 Sol 与 Luna 发布](https://openai.com/index/introducing-gpt-6-sol-and-luna/) ⭐️ 6.0/10

OpenAI 发布 GPT-6 Sol 与 Luna。HN 讨论中，simonw 指出 GPT-6 Luna 价格降至 GPT-5.6 Luna 的一半，称影响重大；jeffnash 对比 Claude Code 20x 与 Codex Pro 20x，认为当前 Codex 在用量限制上优势明显，ChatGPT 20x 套餐下用量几乎无上限，且 20x 与 5x 套餐的用量并非简单 4 倍关系。m\_fayer 称 GPT-5.6 Sol 曾是个人工作流中的甜点，担心继任模型在交互手感上不及前代。材料仅包含社区评论，缺少官方技术细节、架构说明与基准数据。

hackernews · OfficialTurkey · Sep 22, 18:00 · [Discussion](https://news.ycombinator.com/item?id=49805509)

**「为什么重要」** 对 coding agent 工程师而言，模型价格与订阅用量限制直接影响工具选型与成本结构。GPT-6 Luna 降价与 Codex 当前用量策略，可能改变 Claude Code 与 Codex 之间的实际使用成本对比，但官方规格与长期计费规则尚未明确。

**「可关注」** 可关注：GPT-6 Luna 价格减半与 Codex 20x 套餐下「几乎无上限」的用量描述，提示在评估 coding agent 订阅时，需把模型单价、套餐用量窗口与重置规则一并纳入计算，而非仅看标称倍数。

**「评论」** HN 评论共识是 GPT-6 Luna 降价显著，且 Codex 当前在用量限制上比 Claude Code 更宽松。分歧或顾虑在于模型「手感」：m\_fayer 对 GPT-5.6 Sol 的交互体验被替代表示担忧，leokennis 则从普通用户视角认为 ChatGPT Plus 自 5.6 起已基本够用。

**Tags**: `#coding-agent`, `#eval`, `#harness`

---

<a id="item-agent-engineer-6"></a>
### [onPanda：token 级校正标注工具](https://huggingface.co/papers/2609.24983) ⭐️ 6.0/10

onPanda 是一个交互式标注工具，用于高效标注 LLM 对齐数据与 agent 轨迹。其核心交互是 token 级校正：标注者定位首个不当 token，从模型候选 token 中选择替换或自由输入正确文本，系统截断后续内容并从修正后的前缀继续生成，循环「定位-修正-继续」直至得到满意回复。一项小规模对照研究显示，相比人工后编辑，onPanda 将中位标注时间减少 52%。论文提到最终回复中绝大多数 token 得以复用，但摘要在此处截断，完整比例未给出。

rss · Hugging Face Daily Papers · Sep 22, 00:00

**「为什么重要」** 对 coding agent 与 harness 团队而言，对齐数据与轨迹标注是成本瓶颈。onPanda 把标注粒度从整段后编辑压缩到 token 级干预，可能改变数据生产流程。不过目前证据仅来自小规模对照研究，在复杂 agent 轨迹上的效果尚未验证。

**「可关注」** 可关注：该工具依赖模型自身候选 token 与截断重生成，若在自有 harness 中复现 locate-correct-continue 循环，需评估其对 agent 轨迹一致性的影响；52% 的耗时下降来自小规模研究，外推需谨慎。

**Tags**: `#eval`, `#coding-agent`, `#toolchain`

---

<a id="item-agent-engineer-7"></a>
### [Claude Opus 5.5 发布并降价](https://www.anthropic.com/claude-opus-5-5) ⭐️ 5.5/10

Anthropic 于 2026-09-22 发布 Claude Opus 5.5。Hacker News 讨论确认每百万 token 价格下调：缓存读取 $0.20（Opus 5 为 $0.50），输入 $4（$5），输出 $20（$25），缓存写入 $5（$6.25）。官方称沟通更自然、重点前置，但未提供基准测试、上下文窗口或工具调用变化。材料缺乏 Agent 工程可验证细节。

hackernews · km144 · Sep 22, 16:29 · [Discussion](https://news.ycombinator.com/item?id=49803892)

**「为什么重要」** 缓存读取成本下降 60%，对依赖长上下文复用的 coding agent 与 harness 是直接成本变化；Opus 5 此前是 OpenRouter 支出最高的模型，调价可能影响选型。沟通改进是否提升任务成功率，尚无数据支撑。

**「可关注」** 若框架大量复用系统提示或历史对话，缓存读取单价减半可降低单位任务成本；但官方未公布延迟、上下文窗口及工具调用行为变化，升级前需自行验证。

**「评论」** 评论确认降价并对比 OpenRouter 支出排名，同时质疑其“放缓前沿”表态；也有用户表示更倾向 DeepSeek v4.1，并提到其能自主编写 Chrome 驱动协议服务器完成复杂任务。

**Tags**: `#coding-agent`, `#eval`, `#harness`

---

<a id="item-agent-engineer-8"></a>
### [HF daily paper: Transferring the Intelligence of VLMs to Robotic Control](https://huggingface.co/papers/2609.22966) ⭐️ 5.5/10

一篇关于将 VLM 智能迁移到机器人控制的论文摘要，通过离散指令接口实现闭环控制，但信息有限且与主流 Agent 工程实践关联度不高。

rss · Hugging Face Daily Papers · Sep 22, 00:00

**Tags**: `#agent`, `#robotics`, `#vlm`

---

## AI Daily

<a id="item-ai-daily-1"></a>
### [Introducing GPT-6 Sol and Luna](https://openai.com/index/introducing-gpt-6-sol-and-luna) ⭐️ 9.8/10

OpenAI officially introduced GPT-6 Sol and Luna, two models bringing frontier intelligence to everyday work with different balances of capability and cost.

rss · OpenAI Blog · Sep 22, 18:00

**Tags**: `#model`, `#lab`, `#product`

---

<a id="item-ai-daily-2"></a>
### [OpenAI 改进 GPT-6 提示缓存](https://openai.com/index/better-prompt-caching-for-gpt-6) ⭐️ 8.8/10

OpenAI 官方博客宣布 GPT-6 提示缓存改进，称可提高缓存命中率，并新增诊断、显式断点以及延迟与成本控制。材料未给出具体命中率数值或对比基线。此次为功能更新，非新模型发布。

rss · OpenAI Blog · Sep 22, 21:00

**「为什么重要」** 提示缓存直接影响 coding agent 与 harness 的推理延迟和调用成本。GPT-6 提供的显式断点和诊断，让缓存行为更可观测、可控制。

**「可关注」** GPT-6 的显式断点与缓存诊断，可在 harness 中更精细地划定缓存边界并排查未命中问题。

**Tags**: `#model`, `#lab`, `#product`, `#industry`

---

<a id="item-ai-daily-3"></a>
### [OpenAI 发布第三方评估原则](https://openai.com/index/priorities-principles-third-party-assessments) ⭐️ 8.3/10

OpenAI 发布第三方安全评估的优先级与原则，覆盖前沿模型与安全防护机制。文件要求评估严谨、安全且独立。目前仅公布框架，未披露具体执行细节。

rss · OpenAI Blog · Sep 22, 00:00

**「可关注」** 可关注：OpenAI 将第三方评估定位为严谨、安全且独立的流程，具体执行标准仍待披露。

**Tags**: `#policy`, `#eval`, `#lab`, `#industry`

---

<a id="item-ai-daily-4"></a>
### [Opus 5.5 降价：缓存读取降 60%](https://claude.com/blog/what-a-task-costs-on-opus-5-5) ⭐️ 6.8/10

Claude 官方博客说明 Opus 5.5 每 token 成本低于 Opus 5。API 目录价中，输入与输出 token 比 Opus 5 便宜 20%，缓存读取便宜 60%，缓存读取价从输入价的 1/10 降至 1/20。文章用交互计算器拆解任务级成本：轮次、缓存命中、输出 token 类型和模型选择共同决定账单，同一 token 数下示例会话约便宜 31%。

rss · Claude Blog · Sep 22, 00:00

**「为什么重要」** 对跑 coding agent 的工程师来说，长会话的输入账单大部分来自缓存读取，这次降价直接压低 Claude Code 的长任务成本；同时 Opus 5.5 默认思考更多，省下的钱可能被更多输出 token 抵消，需要按自己的任务实测。

**「可关注」** 用 /usage 拉取真实会话的 input、output 和 cache 数据，再按 0% 工作量变化估算纯降价收益；长会话优先保缓存命中率，短问答则更受输出价格影响。

**Tags**: `#model`, `#lab`, `#product`, `#industry`

---