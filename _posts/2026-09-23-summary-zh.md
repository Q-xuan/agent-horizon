---
layout: default
title: "Horizon Summary: 2026-09-23 (ZH)"
date: 2026-09-23
lang: zh
---

> 从 222 条内容中筛选出 20 条重要资讯。

---

**Harness 架构**
1. [vllm-project/vllm released v0.30.0](#item-harness-arch-1) ⭐️ 8.8/10
2. [2.1.280](#item-harness-arch-2) ⭐️ 8.8/10
3. [cline/cline released v4.1.20](#item-harness-arch-3) ⭐️ 8.3/10
4. [Cline SDK v0.0.85 发布](#item-harness-arch-4) ⭐️ 8.3/10
5. [Cline desktop v0.0.33 发布](#item-harness-arch-5) ⭐️ 8.3/10
6. [Cline CLI v3.0.64 发布](#item-harness-arch-6) ⭐️ 8.3/10
7. [openai/codex released rust-v0.156.0](#item-harness-arch-7) ⭐️ 7.8/10
8. [LangChain 从零构建 agent](#item-harness-arch-8) ⭐️ 5.5/10

**Agent 工程师日报**
1. [Transformers 支持 GGUF](#item-agent-engineer-1) ⭐️ 8.3/10
2. [HF daily paper: RRSI: Regularized Recursive Self-Improvement of Agent Harnesses](#item-agent-engineer-2) ⭐️ 7.5/10
3. [GameHorizon Suite 发布](#item-agent-engineer-3) ⭐️ 7.5/10
4. [AISI 与 EvalEval 推进评测结果可复现](#item-agent-engineer-4) ⭐️ 6.3/10
5. [GPT-6 Sol 与 Luna 发布](#item-agent-engineer-5) ⭐️ 6.0/10
6. [onPanda 用 token 级校正标注对齐数据](#item-agent-engineer-6) ⭐️ 6.0/10
7. [Claude Opus 5.5 缓存读取降价](#item-agent-engineer-7) ⭐️ 5.5/10
8. [HF daily paper: Transferring the Intelligence of VLMs to Robotic Control](#item-agent-engineer-8) ⭐️ 5.5/10

**AI 日报**
1. [Introducing GPT-6 Sol and Luna](#item-ai-daily-1) ⭐️ 9.8/10
2. [GPT-6 优化 prompt 缓存](#item-ai-daily-2) ⭐️ 8.8/10
3. [OpenAI 发布第三方安全评估原则](#item-ai-daily-3) ⭐️ 8.3/10
4. [Opus 5.5 降价：任务成本怎么算](#item-ai-daily-4) ⭐️ 6.8/10

---

## Harness 架构

<a id="item-harness-arch-1"></a>
### [vllm-project/vllm released v0.30.0](https://github.com/vllm-project/vllm/releases/tag/v0.30.0) ⭐️ 8.8/10

vLLM v0.30.0 is a major official release adding new models, a persistent GPU weight-cache daemon for faster restarts via CUDA IPC, and a CPU backend with sparse MLA kernels.

github · khluu · 9月22日 05:20

**标签**: `#runtime`, `#models`, `#prefix-cache`

---

<a id="item-harness-arch-2"></a>
### [2.1.280](https://code.claude.com/docs/en/changelog#2-1-280) ⭐️ 8.8/10

Claude Code 2.1.280 ships Opus 5.5 as the default model, adds an MCP description length cap env var and OpenTelemetry hook output metrics, and fixes symlinked-write permission checks and auto-mode retry loops.

rss · Claude Code Changelog · 9月22日 16:48

**标签**: `#runtime`, `#tools`, `#mcp`, `#permissions`, `#sandbox`

---

<a id="item-harness-arch-3"></a>
### [cline/cline released v4.1.20](https://github.com/cline/cline/releases/tag/v4.1.20) ⭐️ 8.3/10

Cline v4.1.20 parallelizes sub-agent tool calls within a step and scales default output budgets to model limits.

github · github-actions\[bot\] · 9月22日 20:45

**标签**: `#runtime`, `#subagents`, `#tools`

---

<a id="item-harness-arch-4"></a>
### [Cline SDK v0.0.85 发布](https://github.com/cline/cline/releases/tag/sdk/sdk/v0.0.85) ⭐️ 8.3/10

Cline SDK v0.0.85 调整运行时与网关默认值。模型达到输出 token 限制但未产出可用工具调用时，运行时会重试至多三次，附加简洁响应提醒，并在工具调用进度或每次运行开始时重置计数器；空 max-tokens 响应走同一恢复路径，\`turn-finished\` 事件在每次恢复迭代前发出以保持配对。默认输出配额改为按模型能力缩放，未显式指定时取 \`max\(32000, floor\(maxOutputTokens \* 0.3\)\)\`，仅抬升不下调，约 106,667 token 以下模型不受影响，128,000 token 模型从 32,000 升至 38,400。模型目录同步更新，209 个提供商下模型数增至 6,237，10 个未固定模型的提供商默认模型发生变更。

github · github-actions\[bot\] · 9月22日 08:13

**「设计要点」** 运行时在输出配额耗尽且无工具调用时插入恢复循环，通过提醒模型拆分任务来避免单轮 \`max-tokens\` 直接终止会话。网关的默认输出计算引入模型能力感知，在保留模型输出、剩余上下文钳制与推理预算下限的前提下，仅抬升不下调，让大输出模型获得更高配额。

**「改了什么」** 新增输出 token 耗尽后的自动重试与事件配对逻辑。默认输出配额从固定 32,000 改为基于模型输出上限的缩放计算。模型目录刷新，Cline Pass 新增 MiMo V2.6 系列，10 个提供商的默认模型切换。

**标签**: `#runtime`, `#tools`, `#planning`

---

<a id="item-harness-arch-5"></a>
### [Cline desktop v0.0.33 发布](https://github.com/cline/cline/releases/tag/desktop-v0.0.33) ⭐️ 8.3/10

Cline desktop v0.0.33 上线 per-task git worktree 隔离。新任务从当前分支切出 \`cline/&lt;id&gt;\`，在 \`~/.cline/worktrees/\` 下独立运行，不触碰用户工作树。修复 desktop 端 auto-compaction 从未启用问题：sidecar 只勾选 checkpoints，漏掉 compaction，90% 触发条件始终未安装。Windows 改为单实例，重复启动聚焦已有窗口，关闭驻留托盘。登录、SSH 新会话、更新入口、会话删除等缺陷一并修复。

github · github-actions\[bot\] · 9月22日 09:07

**「设计要点」** 任务隔离基于 git worktree：新线程创建 \`cline/&lt;id&gt;\` 分支与 \`~/.cline/worktrees/\` 工作树，删除任务时清理分支与工作树，除非其他会话仍占用。记忆侧，sidecar 管理压缩策略，此前遗漏 compaction opt-in，本次修正后压缩请求跟随会话当前凭证与模型，不再静默截断。

**「改了什么」** 新增 worktree 任务隔离与 desktop 自动压缩。Windows 单实例与托盘驻留。登录重试、SSH 首条消息、更新菜单、会话删除、macOS 全屏退出、Cloud 开关过滤、旧 Linux 兼容、\`.cline/rules\` 加载、单选题提交、输出超限重试、压缩凭证刷新、历史删除、子代理审批等缺陷修复。模型目录从 203 提供商、6,079 模型扩至 209 提供商、6,237 模型。

**标签**: `#runtime`, `#sandbox`, `#memory`

---

<a id="item-harness-arch-6"></a>
### [Cline CLI v3.0.64 发布](https://github.com/cline/cline/releases/tag/cli-v3.0.64) ⭐️ 8.3/10

Cline CLI v3.0.64 修复了模型轮次在工具调用前耗尽输出 token 导致运行中断的问题，改为最多重试三次并提示模型拆分任务。默认输出预算从固定 32,000 tokens 调整为模型上限的 30%（取较大者），仅影响输出上限约 107k tokens 以上的模型。模型目录同步更新，总量从 6,188 增至 6,237，覆盖 209 个提供商。

github · github-actions\[bot\] · 9月22日 08:25

**「设计要点」** 运行时在工具调用前增加了输出 token 超限的重试屏障，通过提醒模型控制输出长度并拆分工作来避免单轮响应占满预算。默认输出预算改为按模型上限动态计算，而非全局固定值。

**「改了什么」** 新增输出 token 超限重试逻辑，最多三次；默认输出预算改为模型上限的 30% 与 32,000 tokens 的较大值。模型目录新增 49 个模型，10 个提供商默认模型发生变更。

**标签**: `#runtime`, `#tools`, `#planning`

---

<a id="item-harness-arch-7"></a>
### [openai/codex released rust-v0.156.0](https://github.com/openai/codex/releases/tag/rust-v0.156.0) ⭐️ 7.8/10

Codex Rust v0.156.0 enables worktree sessions by default, adds daemon management and voice support, and ships a fullscreen TUI, marking a significant runtime feature update.

github · github-actions\[bot\] · 9月22日 19:51

**标签**: `#runtime`, `#tools`, `#subagents`, `#sandbox`

---

<a id="item-harness-arch-8"></a>
### [LangChain 从零构建 agent](https://github.com/langchain-ai/agents-from-scratch) ⭐️ 5.5/10

LangChain 开源教程仓库 \`langchain-ai/agents-from-scratch\`，演示如何从零构建连接 Gmail API 的 ambient 邮件助手。仓库分 4 节，每节配 notebook 与 \`src/email\_assistant\` 代码，依次覆盖 agent 基础、评估、human-in-the-loop 与 memory。这是教学材料，不是运行时发布或架构重写。

rss · GitHub Trending Daily · 9月22日 23:29

**「设计要点」** 教程按能力递进组织：从基础 agent 循环，到引入评估与 human-in-the-loop，最终叠加 memory。代码与 notebook 分离，\`src/email\_assistant\` 目录承载可复用实现，Gmail API 作为外部工具层接入。

**标签**: `#memory`, `#eval`, `#tools`

---

## Agent 工程师日报

<a id="item-agent-engineer-1"></a>
### [Transformers 支持 GGUF](https://huggingface.co/blog/transformers-llama-cpp-quants) ⭐️ 8.3/10

Hugging Face 宣布 Transformers 库新增对 llama.cpp GGUF 量化模型的原生支持。调用 \`from\_pretrained\` 时传入 \`gguf\_file\` 即可加载，无需额外配置。底层复用 ggml 内核，初始面向 Apple Silicon，首个支持架构为 Qwen3.5。官方在 MacBook Pro M2 Max（32 GB，macOS 26.6，PyTorch 2.12.1，kernels 0.17.0）上对比 llama-bench，称 Transformers 生成速度已接近 llama.cpp；但基准条件不同，Transformers 测量包含 prefill，llama-bench 仅统计 decode 吞吐。

rss · Hugging Face Blog · 9月22日 00:00

**「为什么重要」** 本地推理与 coding agent 部署多了一条路径：工程师可用标准 Transformers API 运行 GGUF 模型，不必切换到 llama.cpp 或 Ollama 等独立工具链。\`transformers serve\` 同时提供 OpenAI 兼容接口，可直接接入 Jan、Pi 等客户端。

**「可关注」** 可关注：当前支持仅限 Apple Silicon 与 Qwen3.5 架构，且依赖 \`kernels\` 库及特定 PyTorch 版本；若量化内核无法获取，模型会回退到反量化并占用更多内存，注意力实现也会退至 \`sdpa\`。

**标签**: `#coding-agent`, `#harness`

---

<a id="item-agent-engineer-2"></a>
### [HF daily paper: RRSI: Regularized Recursive Self-Improvement of Agent Harnesses](https://huggingface.co/papers/2609.24972) ⭐️ 7.5/10

论文提出 RRSI，通过正则化约束 agent harness 的递归自我改进过程，以缓解过拟合并提升分布外泛化能力。

rss · Hugging Face Daily Papers · 9月22日 00:00

**标签**: `#harness`, `#eval`, `#memory`, `#orchestration`

---

<a id="item-agent-engineer-3"></a>
### [GameHorizon Suite 发布](https://huggingface.co/papers/2609.25001) ⭐️ 7.5/10

2026-09-22，Hugging Face 每日论文收录 GameHorizon Suite。该工作推出大规模 AAA 游戏数据集与多 horizon 评测基准，包含自动标注管线 GameHorizon-Annotator、数据集 GameHorizon-Data 及配套评测。论文指出现有基准覆盖游戏少、缺少语言指令、依赖高方差在线 rollout。目前范围限于 gameplay，未扩展至通用 coding agent；论文获 110 次 upvote。

rss · Hugging Face Daily Papers · 9月22日 00:00

**「为什么重要」** 做 coding agent / harness 的工程师可以留意，它提供了可复现的多 horizon 规划与评测基线，自动标注管线也降低了构建同类基准的门槛。但其有效性尚未在通用编程任务中得到验证。

**「可关注」** 可关注：GameHorizon-Annotator 的自动标注思路能否迁移到代码任务的多 horizon 指令构建，以及现有 gameplay 基准与 coding agent 评测之间的方法论差距。

**标签**: `#eval`, `#agent`, `#benchmark`, `#dataset`, `#planning`

---

<a id="item-agent-engineer-4"></a>
### [AISI 与 EvalEval 推进评测结果可复现](https://huggingface.co/blog/evaleval-aisi) ⭐️ 6.3/10

UK AISI 与 EvalEval 将 Every Eval Ever（EEE）模式和 Evaluation Cards 平台投入实践，合作始于 NeurIPS 2025 期间的联合研讨会。AISI 在适当范围内公开了论文《How Inference Compute Shapes Frontier LLM Evaluation》的配套数据，包含 HealthBench、FrontierMath、Humanity&\#x27;s Last Exam、SWE-Bench Pro、Terminal-Bench 2.0 五个基准的验证结果、上下文和配置信息，覆盖 Claude Opus 4/4.5/4.6 与 GPT-5/5.2/5.4 六个模型，并附带 Cyber CTFs 和 The Last Ones 两个网络安全评测。数据显示 Humanity&\#x27;s Last Exam 的表现随评测协议和推理算力变化；模型在每次尝试后获得 oracle 正确性反馈时，会随 token 使用增加继续解决更多任务。

rss · Hugging Face Blog · 9月22日 00:00

**「为什么重要」** 评测结果常因格式、平台和细节缺失而难以复现，重新运行成本高昂。AISI 此次公开配置和 transcript 级信息，为跨生态比较提供了可验证的参考点。

**「可关注」** 可关注：Humanity&\#x27;s Last Exam 的分数随推理算力和评测协议变化，且 oracle 反馈会改变任务解决曲线，做 agent 评测时需固定并披露这些设置。

**标签**: `#eval`, `#benchmark`, `#reproducibility`, `#infrastructure`

---

<a id="item-agent-engineer-5"></a>
### [GPT-6 Sol 与 Luna 发布](https://openai.com/index/introducing-gpt-6-sol-and-luna/) ⭐️ 6.0/10

OpenAI 发布 GPT-6 Sol 与 Luna。HN 讨论中，simonw 称 GPT-6 Luna 价格是 GPT-5.6 Luna 的一半。jeffnash 对比 Claude Code 20x 与 Codex Pro 20x，认为 Codex 用量限制更宽松，ChatGPT 20x 套餐下用量几乎无上限。leokennis 表示 ChatGPT Plus 自 5.6 起可满足日常聊天、搜索、轻量编码与文档审阅。官方技术细节、架构与基准数据未在材料中提供。

hackernews · OfficialTurkey · 9月22日 18:00 · [社区讨论](https://news.ycombinator.com/item?id=49805509)

**「为什么重要」** 模型定价与订阅用量直接影响 coding agent 的工具选型与运行成本。Luna 降价可能改变 API 与订阅的性价比，但套餐换算复杂，实际限制仍需官方文档确认。

**「可关注」** 可关注：GPT-6 Luna 半价与 Codex Pro 20x 的宽松用量限制，可能降低长任务 agent 的边际成本；但 20x 与 5x 套餐并非简单倍数关系，需实测验证。

**「评论」** simonw 强调 Luna 半价是重大变化。jeffnash 认为 Codex 在用量限制上明显优于 Claude Code，且套餐换算存在不直观的数学关系。m\_fayer 对 5.6 Sol 的交互体验有留恋，担心继任者不如以往顺手。leokennis 认为 ChatGPT Plus 对普通用户已接近无限额度。

**标签**: `#coding-agent`, `#eval`, `#harness`

---

<a id="item-agent-engineer-6"></a>
### [onPanda 用 token 级校正标注对齐数据](https://huggingface.co/papers/2609.24983) ⭐️ 6.0/10

onPanda 是面向 LLM 对齐数据和 agent 轨迹的交互式标注工具。核心交互为 token 级校正：标注者定位首个不当 token，从候选 token 中选取替换或自由输入，系统截断后续内容并从修正前缀继续生成，循环「定位-校正-继续」直至满意。论文报告在一项小规模对照研究中，相比人工后编辑，中位标注时间减少 52%。目前公开材料仅到摘要层级，研究规模有限。

rss · Hugging Face Daily Papers · 9月22日 00:00

**「为什么重要」** 对 coding agent 与 harness 团队，agent 轨迹的对齐标注成本直接影响训练与评估迭代。onPanda 将标注动作从整段后编辑压缩为 token 级干预，可能改变对齐数据生产交互。但 52% 降幅来自小样本对照，尚未在大规模生产环境验证。

**「可关注」** 可关注：若自建 agent 轨迹标注或对齐数据管线，可评估 token 级截断-继续交互相比人工后编辑的省力程度，并验证长轨迹场景下该收益是否依然成立。

**标签**: `#eval`, `#coding-agent`, `#toolchain`

---

<a id="item-agent-engineer-7"></a>
### [Claude Opus 5.5 缓存读取降价](https://www.anthropic.com/claude-opus-5-5) ⭐️ 5.5/10

Anthropic 发布 Claude Opus 5.5。每百万 token 定价下调：缓存读取从 $0.50 降至 $0.20，输入从 $5 降至 $4，输出从 $25 降至 $20，缓存写入从 $6.25 降至 $5。Hacker News 讨论引用的发布说明称，模型沟通更自然，关键信息前置，长会话中更易跟进与检查；并称这是其上周呼吁“放缓前沿”后的首次发布。

hackernews · km144 · 9月22日 16:29 · [社区讨论](https://news.ycombinator.com/item?id=49803892)

**「为什么重要」** 缓存读取价格降至原价五分之一，直接影响高频复用上下文的 agent 成本结构。沟通风格改进可能降低长会话审查负担，但材料未提供基准测试或技术细节。

**「可关注」** 缓存读取单价从 $0.50 降到 $0.20/1M tokens，若 coding agent 工作流大量命中缓存，单次任务成本模型需要重算。

**「评论」** GodelNumbering 列出完整价格对比，并指出 Opus 5 是 OpenRouter 上支出最高的模型。sailingparrot 认为官方在呼吁“放缓前沿”后立即以具体数字展示并未放缓。wg0 表示更倾向 DeepSeek v4.1，称其能自主编写 TypeScript Chrome 驱动协议服务器并生成原型。mcintyre1994 引用官方描述，认为沟通更清晰也带来安全收益。

**标签**: `#coding-agent`, `#eval`, `#harness`

---

<a id="item-agent-engineer-8"></a>
### [HF daily paper: Transferring the Intelligence of VLMs to Robotic Control](https://huggingface.co/papers/2609.22966) ⭐️ 5.5/10

一篇关于将 VLM 智能迁移到机器人控制的论文摘要，通过离散指令接口实现闭环控制，但信息有限且与主流 Agent 工程实践关联度不高。

rss · Hugging Face Daily Papers · 9月22日 00:00

**标签**: `#agent`, `#robotics`, `#vlm`

---

## AI 日报

<a id="item-ai-daily-1"></a>
### [Introducing GPT-6 Sol and Luna](https://openai.com/index/introducing-gpt-6-sol-and-luna) ⭐️ 9.8/10

OpenAI officially introduced GPT-6 Sol and Luna, two models bringing frontier intelligence to everyday work with different balances of capability and cost.

rss · OpenAI Blog · 9月22日 18:00

**标签**: `#model`, `#lab`, `#product`

---

<a id="item-ai-daily-2"></a>
### [GPT-6 优化 prompt 缓存](https://openai.com/index/better-prompt-caching-for-gpt-6) ⭐️ 8.8/10

OpenAI 发布 GPT-6 的 prompt caching 改进，包含更高缓存命中率、新诊断工具、显式断点，以及延迟与成本调控。官方称这些能力可减少调用开销，但未给出具体命中率数值或对比基线。目前信息仅来自官方博客，尚无第三方实测验证。

rss · OpenAI Blog · 9月22日 21:00

**「为什么重要」** 对运行 coding agent 与 harness 的工程场景，长上下文的缓存命中率与断点控制直接影响成本与时延。GPT-6 的显式断点与诊断工具为调控缓存行为提供了新入口。

**「可关注」** GPT-6 引入显式断点与诊断工具，允许开发者在长会话中主动划定缓存边界，而非仅依赖自动命中。

**标签**: `#model`, `#lab`, `#product`, `#industry`

---

<a id="item-ai-daily-3"></a>
### [OpenAI 发布第三方安全评估原则](https://openai.com/index/priorities-principles-third-party-assessments) ⭐️ 8.3/10

OpenAI 发布第三方安全评估的优先级与原则，覆盖前沿模型及其安全措施。该文提出严格、安全、独立的评估框架，但属于政策框架而非模型发布。材料未披露具体评估指标或实施时间表。

rss · OpenAI Blog · 9月22日 00:00

**「为什么重要」** 作为主要实验室的官方政策文件，该框架为第三方评估前沿模型安全提供了可验证的参考依据。

**「可关注」** 可关注：OpenAI 将第三方评估聚焦于前沿模型与安全措施，并强调评估过程的严格性、安全性与独立性。

**标签**: `#policy`, `#eval`, `#lab`, `#industry`

---

<a id="item-ai-daily-4"></a>
### [Opus 5.5 降价：任务成本怎么算](https://claude.com/blog/what-a-task-costs-on-opus-5-5) ⭐️ 6.8/10

Claude 官方博客拆解 Opus 5.5 的任务成本。API 目录价中，输入与输出 token 比 Opus 5 便宜 20%，缓存读取便宜 60%，缓存读取价从输入价的 1/10 降到 1/20。文章指出四因素决定开销：轮次、缓存命中、输出 token 类型、模型选择。示例任务上下文从 20K 涨到 120K，40 轮共处理约 2.8M 输入 token，90% 缓存命中下输入成本约 $1.62；25 轮约 $1.02。同等 token 无缓存需 $11.20，96% 命中约 $0.99。官方提醒 Opus 5.5 默认思考更多，实际任务成本需按 /usage 实测。

rss · Claude Blog · 9月22日 00:00

**「为什么重要」** 对 coding agent 使用者，单价下降不直接等于账单下降。长会话的输入大头是缓存读取，Opus 5.5 把这部分价格压到输入价的 1/20，缓存密集的会话输入最多可省 60%；但模型总是先思考再回复，输出 token 可能增加，最终账单取决于任务形态。

**「可关注」** 可关注：缓存命中率比模型单价更影响输入成本，96% 命中比 90% 再省近四成；用 /usage 拉取真实会话的输入、输出、缓存三项，再按任务形态调 effort 档位，比只比较单价更可靠。

**标签**: `#model`, `#lab`, `#product`, `#industry`

---