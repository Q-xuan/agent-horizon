---
layout: default
title: "Horizon Summary: 2026-09-23 (EN)"
date: 2026-09-23
lang: en
---

> From 233 items, 22 important content pieces were selected

---

**Agent Harness Architecture**
1. [cline/cline released sdk/sdk/v0.0.85](#item-harness-arch-1) ⭐️ 8.8/10
2. [Cline desktop v0.0.33 发布](#item-harness-arch-2) ⭐️ 8.8/10
3. [vLLM v0.30.0 发布](#item-harness-arch-3) ⭐️ 8.8/10
4. [Cline SDK v0.0.84 Released](#item-harness-arch-4) ⭐️ 7.8/10
5. [2.1.280](#item-harness-arch-5) ⭐️ 7.8/10
6. [Cline v4.1.20 Parallelizes Sub-Agent Tool Calls and Scales Output Budgets](#item-harness-arch-6) ⭐️ 6.8/10
7. [Cline CLI v3.0.64 发布](#item-harness-arch-7) ⭐️ 6.8/10
8. [GitHub trending: langchain-ai/agents-from-scratch](#item-harness-arch-8) ⭐️ 5.0/10

**AI Agent Engineer**
1. [OpenAI Launches GPT-6 Sol and Luna](#item-agent-engineer-1) ⭐️ 8.0/10
2. [RRSI 约束 harness 递归自我改进](#item-agent-engineer-2) ⭐️ 7.5/10
3. [Claude Opus 5.5 发布，价格下调](#item-agent-engineer-3) ⭐️ 7.0/10
4. [simonw/llm 0.36 发布](#item-agent-engineer-4) ⭐️ 6.8/10
5. [Opus 5.5、GPT-6 发布，价格战起](#item-agent-engineer-5) ⭐️ 6.5/10
6. [RULER：rubric 奖励优化 SVG 生成](#item-agent-engineer-6) ⭐️ 6.0/10
7. [AIDE^2：agent 递归自我改进](#item-agent-engineer-7) ⭐️ 6.0/10
8. [D-RAC 提出 PDF 归一化分块方法](#item-agent-engineer-8) ⭐️ 6.0/10
9. [llm 0.36 adds GPT-6 models and single-turn plugin flag](#item-agent-engineer-9) ⭐️ 5.5/10
10. [llm-anthropic 0.29 发布](#item-agent-engineer-10) ⭐️ 5.5/10
11. [llm-typesafe 0.1a0 发布](#item-agent-engineer-11) ⭐️ 5.5/10

**AI Daily**
1. [Introducing GPT-6 Sol and Luna](#item-ai-daily-1) ⭐️ 9.8/10
2. [Parallel cut research time and cost in half with GPT‑6 Astra](#item-ai-daily-2) ⭐️ 8.3/10

**AI Deals**
1. [OpenRouter Batch API 半价](#item-ai-deals-1) ⭐️ 7.0/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [cline/cline released sdk/sdk/v0.0.85](https://github.com/cline/cline/releases/tag/sdk/sdk/v0.0.85) ⭐️ 8.8/10

Cline SDK v0.0.85 improves runtime resilience by retrying turns that exhaust output tokens without tool calls and dynamically scaling default output allowances based on model limits.

github · github-actions\[bot\] · Sep 22, 08:13

**Tags**: `#runtime`, `#tools`, `#planning`

---

<a id="item-harness-arch-2"></a>
### [Cline desktop v0.0.33 发布](https://github.com/cline/cline/releases/tag/desktop-v0.0.33) ⭐️ 8.8/10

Cline desktop v0.0.33 发布，新增 git worktree 任务隔离，并修复桌面端长期未生效的自动压缩。新线程可在欢迎屏的 “Work in” 开关选择 Worktree，首个 prompt 会从当前分支切出 \`cline/&lt;id&gt;\`，在 \`~/.cline/worktrees/\` 下创建工作树并运行任务，删除任务时连带清理分支与工作树；仅新线程受影响，跟进与重开会话留在原地。自动压缩此前因 sidecar 只注册 checkpoint 未注册 compaction，90% 触发条件从未安装，本次修正后长会话可正常压缩。

github · github-actions\[bot\] · Sep 22, 09:07

**「设计要点」** 任务隔离通过 git worktree 实现，agent 在独立分支与工作树中执行，不触碰主工作区。记忆侧修正 sidecar 的 compaction 注册逻辑，并让 summarizer 跟随会话当前凭证与模型，避免凭证刷新后静默回退到截断。

**「改了什么」** 新增 git worktree 任务隔离，并修复桌面端从未真正运行的自动压缩。同时修补 Windows 多实例、SSH 新会话启动、登录早期点击失败等运行时缺陷；模型目录扩至 209 提供商、6,237 模型，36 家未固定模型的提供商默认模型发生变更。

**Tags**: `#sandbox`, `#runtime`, `#memory`

---

<a id="item-harness-arch-3"></a>
### [vLLM v0.30.0 发布](https://github.com/vllm-project/vllm/releases/tag/v0.30.0) ⭐️ 8.8/10

vLLM v0.30.0 发布，合并 315 位贡献者的 762 个提交。新增 DeepSeek-V4.1-Flash、GLM-5.3-Flash、K2-Horizon、Cohere Compass 等模型后端，以及基于 AVX512/AMX 稀疏 MLA 的 DeepSeek-V4 CPU 后端。运行时核心是 Fast Start：常驻每 GPU 的权重缓存守护进程保存后量化、TP 分片权重，引擎重启时通过 \`--load-format ipc\_cache\` 经 CUDA IPC 映射，跳过磁盘重载，已覆盖 FP4 检查点与多节点 TP。Model Runner V2 在 H200 上图捕获从 12s 降至 2s，引擎初始化从 28.9s 降至 8.2s。

github · khluu · Sep 22, 05:20

**「设计要点」** Fast Start 以持久化 per-GPU 守护进程持有后量化、TP 分片权重，重启时经 CUDA IPC 映射而非磁盘加载；HiSparse 为 sparse-MLA 解码引入主机常驻层，显存压力下将 KV 页溢出到 pinned host memory，并由 \`HiSparseConnector\` 统一控制与共享 TP rank 间主机缓存。

**「改了什么」** 新增 \`--load-format ipc\_cache\` 与权重缓存守护进程，支持 FP4 和多节点 TP 快速启动；Model Runner V2 支持 FULL CUDA 图微批次双批重叠、流水线并行下的 MTP/EAGLE3/DFlash/DSpark 投机解码，以及基于在线接受率估计的自适应验证。破坏性变更包括 scale-out 端点改为 \`--enable-scale-out\` 显式开启、移除 GPTQ \`g\_idx\`、弃用 \`all\` Mamba 缓存模式与 \`python -m vllm.entrypoints.grpc\_server\`。

**Tags**: `#runtime`, `#prefix-cache`, `#memory`

---

<a id="item-harness-arch-4"></a>
### [Cline SDK v0.0.84 Released](https://github.com/cline/cline/releases/tag/sdk/sdk/v0.0.84) ⭐️ 7.8/10

Cline SDK v0.0.84 fixes concurrent feature-flag polling races and adds run-start hook context injection. Polls for the same account now share one in-flight request, propagate failures for retry, and stop blocking on account switches. \`beforeRun\` returns \`AgentRunStartResult\` with an \`appendContext\` channel; the runtime injects collected context as a single \`&lt;hook\_context source=&quot;RunStart&quot;&gt;\` message after input messages. On Windows, \`disableCurrentDirectoryExecutableSearch\(\)\` in \`@cline/shared\` prevents workspace-planted executables from hijacking bare program names. Compaction now triggers on provider-reported input-token counts instead of only character estimates. Subagent tool calls run concurrently by default and no longer inherit parent approval policies. The release also covers manifest-backed session deletion, rules-path resolvers, atomic queue-head steering, client-typed model recommendations, gated Composio connectors, \`requestId\` in \`afterModel\` hooks, Langfuse attribution preservation, a 5-second login-shell PATH probe budget, and cloud-run state coherence.

github · github-actions\[bot\] · Sep 22, 03:26

**「Design Points」** The runtime records provider-reported input tokens per request and threads them to the prepare-turn pipeline as \`previousRequestInputTokens\`; compaction uses \`max\(estimate, actual\)\` with the estimate as a floor. Run-start hook injection stays backward-compatible because \`AgentStopControl\` remains assignable to \`AgentRunStartResult\`, and blocking hook behavior is opt-in via \`blockingRunStartHooks\` to avoid stalling hosts with lingering scripts. Windows executable search is disabled once at process startup across CLI, desktop sidecar, VS Code, and JetBrains hosts.

**「What Changed」** Feature-flag polling now shares in-flight requests and propagates failures. Run-start hooks inject context through a new result type with optional blocking. Windows startup disables current-directory executable search. Compaction uses actual token counts and raises the summarizer budget to 8192. Subagents execute tools concurrently without inheriting parent approvals. Session deletion handles on-disk manifests. Rules paths resolve across workspace and global layouts including OneDrive redirects. Queued prompts steer atomically to the queue head. Model recommendations carry client type. Composio connectors gate behind \`CLINE\_COMPOSIO\_BETA\`. \`afterModel\` hooks receive \`requestId\`. Langfuse spans preserve user and session attributes. Login-shell PATH probing allows 5 seconds. Cloud-run state rejects stale running metadata after settlement.

**Tags**: `#runtime`, `#tools`, `#permissions`

---

<a id="item-harness-arch-5"></a>
### [2.1.280](https://code.claude.com/docs/en/changelog#2-1-280) ⭐️ 7.8/10

Claude Code 2.1.280 adds an MCP description length limit, fixes symlink write permission bypasses, and expands OpenTelemetry hook telemetry.

rss · Claude Code Changelog · Sep 22, 16:48

**Tags**: `#permissions`, `#sandbox`, `#tools`, `#mcp`, `#eval`

---

<a id="item-harness-arch-6"></a>
### [Cline v4.1.20 Parallelizes Sub-Agent Tool Calls and Scales Output Budgets](https://github.com/cline/cline/releases/tag/v4.1.20) ⭐️ 6.8/10

Cline v4.1.20 parallelizes tool calls for sub-agents spawned in the same step and ties default output budgets to advertised model limits. Order-dependent tools still run sequentially, and the parent agent waits for every child result before its next turn. Models with large output limits now receive 30% of that limit or 32,000 tokens, whichever is larger; models under roughly 107k output tokens see no change. The release also restores hook context injection, preserves unsent composer text across retries, streams background command output live, and fixes rules discovery, task deletion, sub-agent approval, compaction credentials, and output-limit retries.

github · github-actions\[bot\] · Sep 22, 20:45

**「Architecture Note」** Same-step sub-agents execute tool calls concurrently, but the harness enforces ordering for dependent tools and blocks the parent turn until all results return. Default output budgets scale from advertised model limits instead of a fixed constant. Compaction now uses the task&\#x27;s current credentials and model rather than values captured at task start.

**「What Changed」** Sub-agent tool calls in the same step now run concurrently, and default output budgets become max\(32,000 tokens, 30% of the model&\#x27;s advertised output limit\). The model catalog grows to 209 providers and 6,237 models, with Kimi For Coding split into kimi.com and kimi.ai and six new providers added; 36 unpinned providers now default to different models, mostly DeepSeek V4.1 Flash, GLM 5.3 Flash, or MiMo V2.6 Flash.

**Tags**: `#runtime`, `#subagents`, `#tools`

---

<a id="item-harness-arch-7"></a>
### [Cline CLI v3.0.64 发布](https://github.com/cline/cline/releases/tag/cli-v3.0.64) ⭐️ 6.8/10

Cline CLI v3.0.64 修复了模型回合在工具调用前耗尽输出 token 导致运行中断的问题。现在这类回合会重试最多三次，并提示模型精简输出、拆分工作到多次工具调用，三次后仍失败才终止。同时，大输出上限模型的默认输出预算从固定 32,000 token 改为模型上限的 30%（取较大者），约 107k 以下模型不受影响。模型目录从 6,188 个刷新到 6,237 个，覆盖 209 个 provider，10 个 provider 的默认模型发生变更。

github · github-actions\[bot\] · Sep 22, 08:25

**「设计要点」** 运行时在工具调用前增加了输出限制重试与预算控制。重试策略针对 reasoning-heavy 或 oversized response，通过提醒拆分工作来避免单回合占满输出额度。默认输出预算按模型上限比例分配，直接影响单回合成本与时延。

**「改了什么」** 相对 cli-v3.0.63，输出限制失败不再直接终止运行，改为最多三次重试；大上下文模型的默认输出预算从固定 32,000 token 调整为模型上限的 30%；模型目录新增 49 个模型，10 个 provider 切换默认模型。

**Tags**: `#runtime`, `#tools`, `#planning`

---

<a id="item-harness-arch-8"></a>
### [GitHub trending: langchain-ai/agents-from-scratch](https://github.com/langchain-ai/agents-from-scratch) ⭐️ 5.0/10

A LangChain educational repository that guides users through building an email assistant agent from scratch, covering evaluation, human-in-the-loop, and memory with accompanying code.

rss · GitHub Trending Daily · Sep 23, 02:22

**Tags**: `#memory`, `#eval`, `#tools`, `#permissions`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [OpenAI Launches GPT-6 Sol and Luna](https://openai.com/index/introducing-gpt-6-sol-and-luna/) ⭐️ 8.0/10

OpenAI introduced GPT-6 Sol and Luna on September 22, 2026. Hacker News discussion focuses on pricing, agentic coding experience, and subscription usage limits. Simon Willison notes GPT-6 Luna is priced at half of GPT-5.6 Luna. Practitioners are comparing the new models against Claude Code and Codex plans, citing usage limits and reset windows as deciding factors.

hackernews · OfficialTurkey · Sep 22, 18:00 · [Discussion](https://news.ycombinator.com/item?id=49805509)

**「Why It Matters」** The reported price cut for Luna and the structure of 20x subscription tiers directly affect cost modeling for coding agents. Whether GPT-6 matches the agentic collaboration quality of 5.6 Sol remains unverified, but early practitioner sentiment treats that feel as a real selection criterion.

**「Worth Watching」** Worth watching: how GPT-6 Luna&\#x27;s lower price and Codex Pro 20x&\#x27;s effectively unmetered ChatGPT usage reshape the economics of long-running agent sessions relative to Claude Code 20x.

**「Community Discussion」** Commenters are divided between cost and collaboration quality. One practitioner praises 5.6 Sol&\#x27;s engineering instincts and worries the successor may feel less natural. Another argues Codex Pro 20x currently beats Claude Code 20x because ChatGPT usage is essentially unmetered on the 20x plan, despite confusing plan math.

**Tags**: `#coding-agent`, `#harness`, `#eval`, `#observability`

---

<a id="item-agent-engineer-2"></a>
### [RRSI 约束 harness 递归自我改进](https://huggingface.co/papers/2609.24972) ⭐️ 7.5/10

Hugging Face Daily Papers 收录 RRSI 论文，提出用正则化约束 agent harness 的递归自我改进。现有方法通过迭代提议和选择组件级编辑来自动优化 harness，在系统层面形成 RSI，但容易记忆训练任务，导致分布内增益在分布外基准上缩水或消失。RRSI 在候选生成与选择阶段引入正则化原则，抑制过拟合并提升 OOD 表现。该论文已获 156 次 upvote，具体实验设置与复现细节尚未在摘要中完整展开。

rss · Hugging Face Daily Papers · Sep 23, 02:22

**「为什么重要」** Agent harness 的自动化递归改进是提升冻结骨干模型能力的重要路径，但分布内收益难以迁移到 OOD 基准是该路线落地的核心风险。RRSI 将正则化引入 harness 演化流程，为缓解这一风险提供了可解释的技术方案。

**「可关注」** 可关注：RRSI 在候选生成与选择两端同时施加正则化约束，提示 harness 自动演化需要显式的泛化机制，而非仅依赖训练任务上的选择压力。

**Tags**: `#harness`, `#eval`, `#memory`, `#orchestration`

---

<a id="item-agent-engineer-3"></a>
### [Claude Opus 5.5 发布，价格下调](https://www.anthropic.com/claude-opus-5-5) ⭐️ 7.0/10

Anthropic 发布 Claude Opus 5.5。Hacker News 讨论中，用户整理出每百万 token 新定价：缓存读取 $0.20、输入 $4、输出 $20、缓存写入 $5，相比 Opus 5 的 $0.50、$5、$25、$6.25 全线下调。有用户复测 3D 动画生成任务，认为效果较 Opus 5 有可见提升。官方介绍强调其表达更自然、长会话更易协作。社区同时对「放缓前沿」的叙事与实际发布节奏提出质疑。

hackernews · km144 · Sep 22, 16:29 · [Discussion](https://news.ycombinator.com/item?id=49803892)

**「为什么重要」** 对 coding agent 与 harness 开发者，token 价格直接影响长任务与多轮交互成本。社区讨论提到 Opus 5 曾是 OpenRouter 上支出最高的模型，此次全线下调可能改变 agent 工作流的选型经济性。

**「可关注」** 可关注：若已在 Opus 5 上构建 agent，可对比 5.5 在同类任务上的输出质量与成本再决定是否切换；目前社区反馈的 3D 动画提升属于个案，尚不构成系统性基准。

**「评论」** 讨论集中在价格降幅与官方叙事的反差。有用户完整列出四项 token 新价，指出缓存读取从 $0.50 降至 $0.20 降幅最大；也有用户表示已转向 DeepSeek v4.1，并对「沟通更自然」的官方描述持保留态度。

**Tags**: `#coding-agent`, `#eval`, `#model-release`

---

<a id="item-agent-engineer-4"></a>
### [simonw/llm 0.36 发布](https://github.com/simonw/llm/releases/tag/0.36) ⭐️ 6.8/10

simonw/llm 0.36 发布。新增 OpenAI 模型别名 \`gpt-6-sol\` 与 \`gpt-6-luna\`。插件可声明 \`supports\_conversation = False\` 标记单轮模型，\`llm chat\` 启动前拒绝此类模型，库层收到助手或工具历史时抛出 \`llm.ConversationNotSupported\`。\`llm logs\` 的 Markdown 输出将推理轨迹包裹在 \`&lt;details&gt;&lt;summary&gt;\` 中。另修复 \`llm logs -t\` 崩溃、异步日志写入、\`title\` 字段保留等六类问题。

github · simonw · Sep 22, 18:48

**「为什么重要」** \`supports\_conversation = False\` 给单轮模型加了明确的架构约束，插件和使用方不能再把多轮历史传给不支持的模型。对维护模型插件和依赖 \`llm logs\` 调试的工程师，这次更新收窄了运行时错误面，并让推理轨迹更易读。

**「可关注」** 可关注：\`supports\_conversation = False\` 与 \`llm.ConversationNotSupported\` 形成声明与运行两层拦截，首个采用者为 llm-typesafe；自研单轮模型插件可评估接入该标志，把错误处理统一到库层。

**Tags**: `#harness`, `#observability`, `#coding-agent`

---

<a id="item-agent-engineer-5"></a>
### [Opus 5.5、GPT-6 发布，价格战起](https://simonwillison.net/2026/Sep/22/opus-and-sol-and-luna/) ⭐️ 6.5/10

Anthropic 发布 Claude Opus 5.5，OpenAI 约一小时后发布 GPT-6 Sol 与 GPT-6 Luna。GPT-6 Luna 定价 $0.10/M 输入、$0.01/M 缓存输入、$0.50/M 输出，价格约为 GPT-5.6 Luna 的一半；GPT-6 Sol 定价 $2/M 输入、$0.20/M 缓存输入、$10/M 输出，且 GPT-5.6 已计划 11 月涨价 25%。Claude Opus 5.5 定价 $4/M 输入、$0.20/M 缓存输入、$20/M 输出，较 Opus 5.0 输入输出各降 20%，缓存读取降 60%。Simon Willison 测试发现 Opus 5.5 在 max 思考等级下生成 SVG 时超出 128,000 输出 token 上限，两次均未返回响应，每次耗时近 20 分钟、花费 $2.56。

rss · Simon Willison · Sep 22, 23:46

**「为什么重要」** 模型单价与缓存价格直接影响 coding agent 长对话与多轮工具调用的成本。Opus 5.5 缓存读取降 60% 对 agentic 场景意义明显；Opus 5.5 max 档位在简单 SVG 任务上即耗尽 128,000 输出上限，高推理档位的稳定性存疑。

**「可关注」** 可关注：GPT-6 Luna 以 $0.10/$0.50 进入低价档，Claude Opus 5.5 缓存读取降至 $0.20/M，长上下文 agent 的 token 成本假设需要重算；同时 Opus 5.5 max 档位在轻量任务上出现过思考耗尽，高 effort 模式的稳定性待验证。

**Tags**: `#coding-agent`, `#harness`, `#eval`

---

<a id="item-agent-engineer-6"></a>
### [RULER：rubric 奖励优化 SVG 生成](https://huggingface.co/papers/2609.25270) ⭐️ 6.0/10

Hugging Face Daily Papers 于 2026-09-23 收录论文 RULER，提出面向 SVG 代码生成的实例感知 rubric 奖励方法，用于替代在风格化矢量内容上迁移性差的标量指标。论文指出，CLIP、Aesthetic 等在自然图像上校准的标量度量直接作为 RL 奖励会触发 reward hacking；实验表明，用视觉语言模型按多轴 rubric 打分与人类判断的相关性显著优于标量指标，且在样本间和指令内均成立。RULER 将每条指令转换为实例感知的 rubric 奖励，以提升人类对齐并缓解奖励黑客。该成果目前限于 SVG 生成领域，属于研究方法而非生产工程变更。

rss · Hugging Face Daily Papers · Sep 23, 00:00

**「为什么重要」** 对做 coding agent 与 harness 评估的人而言，该研究提供了一个可复用的信号：在开放式、无绝对视觉真值的生成任务中，标量指标作为奖励可能系统性失真，而多轴 rubric 评分更接近人类判断。不过其效果尚未在更广泛的代码生成或 agent 场景中得到验证。

**「可关注」** 可关注：为 RL 奖励或自动评估设计指标时，若任务缺乏绝对真值且域外分布明显，直接复用通用标量度量存在 reward hacking 风险，按实例构建多轴 rubric 是材料中给出的替代方向。

**Tags**: `#eval`, `#coding-agent`, `#rl`, `#reward-hacking`

---

<a id="item-agent-engineer-7"></a>
### [AIDE^2：agent 递归自我改进](https://huggingface.co/papers/2609.26457) ⭐️ 6.0/10

2026-09-23，Hugging Face Daily Papers 收录论文 AIDE^2，提出让 AI 研究 agent 修改自身代码，在 AI R&amp;D 任务套件上基准测试修改后的版本，并保留符合筛选条件的重写，形成递归自我改进循环。论文指出，AI agent 已开始自动参与训练效率与推理优化，持续自我改进可对冲研发投入边际递减。RSS 摘要仅提供高层概念，未包含代码、性能数据或架构细节。

rss · Hugging Face Daily Papers · Sep 23, 00:00

**「为什么重要」** 对 coding agent 与 harness 开发者而言，该论文把评测从外部基准移入 agent 自身迭代循环，基准测试与筛选规则直接决定哪些代码重写被保留。不过论文实际效果与可复现性仍待原文验证。

**「可关注」** 当 agent 自身代码成为优化对象时，基准测试套件与筛选逻辑会成为递归循环的核心组件，具体设计需查阅论文原文确认。

**Tags**: `#coding-agent`, `#eval`, `#harness`

---

<a id="item-agent-engineer-8"></a>
### [D-RAC 提出 PDF 归一化分块方法](https://huggingface.co/papers/2609.24220) ⭐️ 6.0/10

Hugging Face 每日论文发布 D-RAC。该方法面向企业 RAG 的异构文档摄取，先把任意输入格式归一化为 PDF，再通过单次多模态 LLM 调用完成检索感知分块。论文指出，规则抽取与 OCR 会破坏阅读顺序、压平表格、丢失标题层级；全 agentic 分块则 token 成本高且有幻觉风险。D-RAC 是 W-RAC 框架向任意文档格式的扩展。目前公开内容止于摘要，缺少可复现基准与生产数据。

rss · Hugging Face Daily Papers · Sep 23, 02:22

**「为什么重要」** 对做 RAG 摄取和 agent 文档工具链的人，这篇论文给出了一条具体路径：用确定性 PDF 渲染统一输入，再把视觉理解交给单次多模态调用，可能降低多格式解析的工程复杂度。但论文尚未提供可复现基准，实际收益仍待验证。

**「可关注」** 可关注：D-RAC 将格式归一化与检索感知分块拆为两步，先以 PDF 作为中间表示规避多格式解析难题，再用单次多模态 LLM 调用替代规则抽取。若后续放出基准，可对比其与现有 OCR 加规则分块方案在表格和标题层级上的保留效果。

**Tags**: `#harness`, `#eval`, `#rag`

---

<a id="item-agent-engineer-9"></a>
### [llm 0.36 adds GPT-6 models and single-turn plugin flag](https://simonwillison.net/2026/Sep/22/llm/) ⭐️ 5.5/10

llm 0.36 adds OpenAI model IDs gpt-6-sol and gpt-6-luna. Model plugins can now declare supports\_conversation = False for single-turn models; LLM raises llm.ConversationNotSupported when these models receive assistant or tool history, and llm chat rejects them before starting a session, with llm-typesafe as the first adopter. Reasoning traces in llm logs Markdown output are now wrapped in &lt;details&gt;&lt;summary&gt; tags, and the release includes bug fixes from five new contributors.

rss · Simon Willison · Sep 22, 18:48

**「Why it matters」** The supports\_conversation flag gives plugin authors a first-party way to model single-turn constraints, moving failure from silent misbehavior to explicit errors. The new GPT-6 model IDs keep the CLI aligned with current OpenAI releases.

**「Watch」** Watch: If you maintain an llm plugin for a single-turn model, set supports\_conversation = False so llm chat fails fast instead of sending invalid conversation history.

**Tags**: `#harness`, `#tooling`, `#plugins`, `#openai`

---

<a id="item-agent-engineer-10"></a>
### [llm-anthropic 0.29 发布](https://simonwillison.net/2026/Sep/22/llm-anthropic/) ⭐️ 5.5/10

Simon Willison 发布 llm-anthropic 0.29，为 llm CLI 新增 Claude Opus 5.5 支持。调用命令为 \`llm -m claude-opus-5.5 &quot;prompt goes here&quot;\`。该版本为插件例行更新，未提供性能数据或架构变化。

rss · Simon Willison · Sep 22, 17:14

**「为什么重要」** llm CLI 用户可直接在命令行调用 Claude Opus 5.5，模型选择范围扩大。

**「可关注」** llm-anthropic 0.29 将 Claude Opus 5.5 接入 llm CLI，可通过 \`-m claude-opus-5.5\` 直接调用。

**Tags**: `#harness`, `#llm`, `#anthropic`

---

<a id="item-agent-engineer-11"></a>
### [llm-typesafe 0.1a0 发布](https://simonwillison.net/2026/Sep/22/llm-typesafe/) ⭐️ 5.5/10

Simon Willison 发布 LLM CLI 插件 llm-typesafe 0.1a0，接入 TypeSafe AI 的 Jev 模型。安装并配置 API key 后，可通过 \`llm -m jev\` 调用。插件输出三类结构化结果：noul 二分类返回 0–1 数值，choice 按 criteria 映射到预设标签，score 按 criteria 数组分级。示例中，对退款请求的判定返回 \`\{&quot;type&quot;: &quot;noul&quot;, &quot;noul&quot;: 0.99\}\`。当前为 alpha 版本，仅覆盖 Jev 模型。

rss · Simon Willison · Sep 22, 15:54

**「为什么重要」** 对 coding agent 与 harness 开发者，这提供了一条轻量接入结构化判定模型的路径。Jev 模型侧重 noul、choice、score 等分类与打分任务，适合 eval 或自动分派。alpha 阶段仅支持单一模型，尚未验证大规模稳定性。

**「可关注」** 可关注：该插件用 \`-s\` 传问题、\`-o\` 传参数，直接在命令行产出 JSON 结构化结果，适合接入 eval 流程。

**Tags**: `#harness`, `#eval`, `#coding-agent`

---

## AI Daily

<a id="item-ai-daily-1"></a>
### [Introducing GPT-6 Sol and Luna](https://openai.com/index/introducing-gpt-6-sol-and-luna) ⭐️ 9.8/10

OpenAI officially introduces GPT-6 Sol and Luna, two new models bringing frontier intelligence to everyday work with different balances of capability and cost.

rss · OpenAI Blog · Sep 22, 18:00

**Tags**: `#model`, `#lab`, `#product`

---

<a id="item-ai-daily-2"></a>
### [Parallel cut research time and cost in half with GPT‑6 Astra](https://openai.com/index/parallel-cuts-time-and-cost-with-astra) ⭐️ 8.3/10

OpenAI’s official blog shares a Parallel case study claiming GPT‑6 Astra cut agent research time and cost in half for labor-market data synthesis.

rss · OpenAI Blog · Sep 22, 12:00

**Tags**: `#model`, `#lab`, `#product`, `#eval`

---

## AI Deals

<a id="item-ai-deals-1"></a>
### [OpenRouter Batch API 半价](https://openrouter.ai/blog/announcements/batch-api/) ⭐️ 7.0/10

OpenRouter 上线 Batch API，将批量捆绑的推理请求价格降为半价。官方公告称这是面向开发者的定价优惠，但未说明额度限制或截止时间。使用条件为通过 Batch API 提交请求。

rss · HN Free API / Credits · Sep 22, 16:42

**「为什么重要」** 对可延迟处理的批量推理任务，半价直接降低单位成本，且无需免费额度或赠金。

**「可关注」** 批量请求享半价，适合离线或异步任务；材料未提及限额与截止时间，需以官方文档为准。

**Tags**: `#api`, `#promo`, `#batch`

---