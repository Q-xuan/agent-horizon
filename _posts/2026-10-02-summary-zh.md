---
layout: default
title: "Horizon Summary: 2026-10-02 (ZH)"
date: 2026-10-02
lang: zh
---

> 从 212 条内容中筛选出 18 条重要资讯。

---

**Harness 架构**
1. [ADK Python v2.11.0 发布](#item-harness-arch-1) ⭐️ 8.8/10
2. [pydantic-ai v2.53.0 发布](#item-harness-arch-2) ⭐️ 8.3/10
3. [anthropics/claude-code released v2.1.287](#item-harness-arch-3) ⭐️ 7.8/10
4. [openai/codex released rust-v0.160.0](#item-harness-arch-4) ⭐️ 7.3/10
5. [openai-agents-python v0.23.0 发布](#item-harness-arch-5) ⭐️ 7.3/10
6. [microsoft/agent-framework released dotnet-1.23.0](#item-harness-arch-6) ⭐️ 7.3/10
7. [google-gemini/gemini-cli released v0.64.0-nightly.20261002.gc9096a847](#item-harness-arch-7) ⭐️ 6.8/10

**Agent 工程师日报**
1. [pwasm 0.2a0 沙箱执行 WASM](#item-agent-engineer-1) ⭐️ 8.3/10
2. [HF daily paper: Beyond Memory: Harnessing Long-Horizon Agents with Explicit Belief States](#item-agent-engineer-2) ⭐️ 7.5/10
3. [预训练模型 pass@K 反超后训练模型](#item-agent-engineer-3) ⭐️ 7.5/10
4. [Green：Agent 可经共享缓存跨沙箱传播](#item-agent-engineer-4) ⭐️ 7.0/10
5. [ActiveSaddler 调整训练场景](#item-agent-engineer-5) ⭐️ 6.0/10
6. [RASO：跨 harness 检索增强技能优化](#item-agent-engineer-6) ⭐️ 6.0/10
7. [Introducing Olmo-core 3: Open, scalable training infrastructure for large MoEs](#item-agent-engineer-7) ⭐️ 5.8/10

**AI 日报**
1. [The eternal complement](#item-ai-daily-1) ⭐️ 6.3/10
2. [How Albertsons Companies is reimagining retail from the inside out](#item-ai-daily-2) ⭐️ 6.3/10
3. [GitHub Universe 2026 前瞻](#item-ai-daily-3) ⭐️ 5.8/10
4. [Mollick：智能体集群自我组织](#item-ai-daily-4) ⭐️ 5.0/10

---

## Harness 架构

<a id="item-harness-arch-1"></a>
### [ADK Python v2.11.0 发布](https://github.com/google/adk-python/releases/tag/v2.11.0) ⭐️ 8.8/10

ADK Python v2.11.0 发布，新增优雅取消、工作流工具确认、模型咨询工具和 SQLite 记忆服务。Runner、Workflow 和节点支持传入 \`abort\_signal\` 停止运行，\`/run\_sse\` 在客户端断开时取消运行。工作流工具节点通过 \`RequestInput\` 暂停等待用户批准，不再向下游传递错误。ModelConsultTool 允许任务中途咨询另一模型，受每轮和每会话预算限制；内置 SQLite 记忆服务通过 \`sqlite://\` URI 选择。

github · xuanyang15 · 10月2日 00:44

**「设计要点」** 取消信号从 Runner 贯通到 Workflow 和节点，并在 \`/run\_sse\` 绑定客户端断开事件。工作流工具节点复用 \`LlmAgent\` 的 \`RequestInput\` 确认机制，把人工审批变成统一的暂停原语；记忆层新增本地 SQLite 后端，通过 \`sqlite://\` URI 切换。

**「改了什么」** 相对上一版，新增 \`abort\_signal\` 取消、工作流工具确认、ModelConsultTool 和 SQLite 记忆服务。破坏性变更在 Dev UI：运行时配置改由服务器按请求提供，不再写入安装包，logo 设置改用命令行参数。

**标签**: `#runtime`, `#tools`, `#memory`, `#permissions`

---

<a id="item-harness-arch-2"></a>
### [pydantic-ai v2.53.0 发布](https://github.com/pydantic/pydantic-ai/releases/tag/v2.53.0) ⭐️ 8.3/10

pydantic-ai v2.53.0 发布，修复 ConcurrencyLimitedModel 的高危流式并发槽泄漏（GHSA-6fqq-452j-qhrp）。流式请求经 ConcurrencyLimitedModel 或 limit\_model\_concurrency 发出后，若消费者提前退出、抛错、取消，或以默认 debounce 消费完 stream\_text\(\)，槽位可能在不同任务上释放，重复流式请求会耗尽共享 limiter。Agent 级 max\_concurrency 和非流式请求不受影响，v1 不受影响。修复同时改变 limiter 共享规则：模型包装器与 agent 或外层包装器共享 limiter 时抛出 UserError；ConcurrencyLimiter.acquire\(\) 每次调用都占槽；自定义 AbstractConcurrencyLimiter 必须允许 release\(\) 来自其他任务。

github · dsfaccini · 10月2日 02:52

**「设计要点」** ConcurrencyLimitedModel 依赖 limiter 控制流式请求并发。槽位获取与释放原先绑定同一任务，跨任务释放会导致槽位泄漏；修复后 acquire\(\) 每次调用占槽，且自定义 limiter 需支持跨任务 release\(\)，避免共享 limiter 被重复流阻塞。

**「改了什么」** v2.53.0 将流式并发槽的释放从任务绑定改为允许跨任务释放，并把模型包装器共享 limiter 的行为从静默接受改为显式 UserError。

**标签**: `#runtime`, `#tools`, `#security`

---

<a id="item-harness-arch-3"></a>
### [anthropics/claude-code released v2.1.287](https://github.com/anthropics/claude-code/releases/tag/v2.1.287) ⭐️ 7.8/10

Claude Code v2.1.287 introduces MCP URL prompt support on the 2025-11-25 protocol, a new plugin mods system for deeper behavior modification, and a built-in side-agent plugin, plus minor telemetry and UI updates.

github · ashwin-ant · 10月1日 18:00

**标签**: `#mcp`, `#subagents`, `#tools`, `#runtime`, `#permissions`

---

<a id="item-harness-arch-4"></a>
### [openai/codex released rust-v0.160.0](https://github.com/openai/codex/releases/tag/rust-v0.160.0) ⭐️ 7.3/10

OpenAI Codex Rust v0.160.0 ships incremental agent harness improvements: workspace-default session resumption, opt-in Guardian review with cross-handoff context, and Windows sandbox permission fixes.

github · andrewgu-oai · 10月1日 20:19

**标签**: `#runtime`, `#sandbox`, `#permissions`, `#memory`, `#subagents`

---

<a id="item-harness-arch-5"></a>
### [openai-agents-python v0.23.0 发布](https://github.com/openai/openai-agents-python/releases/tag/v0.23.0) ⭐️ 7.3/10

OpenAI Agents Python SDK 发布 v0.23.0。新增四项可配置能力：MCP 列表分页上限、沙箱 Docker 移除保护、内存整合轮次、加密会话历史扫描预算。其中 Docker 保护与加密扫描默认关闭，需显式启用。

github · openai-sdks\[bot\] · 10月2日 01:08

**「设计要点」** 沙箱与会话层引入显式开关，Docker 移除保护和加密历史扫描均需 opt-in，默认不改变现有运行时行为。内存整合轮次与 MCP 分页上限开放为配置项，便于按部署环境调节资源边界。

**「改了什么」** v0.23.0 将 MCP 分页、沙箱 Docker 移除保护、内存整合轮次、加密会话历史扫描从固定逻辑改为可配置或可选启用。

**标签**: `#mcp`, `#sandbox`, `#memory`, `#sessions`

---

<a id="item-harness-arch-6"></a>
### [microsoft/agent-framework released dotnet-1.23.0](https://github.com/microsoft/agent-framework/releases/tag/dotnet-1.23.0) ⭐️ 7.3/10

Microsoft Agent Framework .NET 1.23.0 ships breaking changes for tool changes between runs, MCP client origin pinning, and several workflow/runtime fixes.

github · dmytrostruk · 10月1日 10:54

**标签**: `#runtime`, `#tools`, `#mcp`

---

<a id="item-harness-arch-7"></a>
### [google-gemini/gemini-cli released v0.64.0-nightly.20261002.gc9096a847](https://github.com/google-gemini/gemini-cli/releases/tag/v0.64.0-nightly.20261002.gc9096a847) ⭐️ 6.8/10

Gemini CLI nightly v0.64.0 ships fixes for chat history memory management, atomic state persistence, and emergency cancellation handling.

github · gemini-cli-robot · 10月2日 01:33

**标签**: `#runtime`, `#memory`, `#tools`

---

## Agent 工程师日报

<a id="item-agent-engineer-1"></a>
### [pwasm 0.2a0 沙箱执行 WASM](https://github.com/simonw/pwasm/releases/tag/0.2a0) ⭐️ 8.3/10

simonw 发布 pwasm 0.2a0，捆绑 MicroPython、QuickJS 和 Micro QuickJS 的 WebAssembly 构建，允许用纯 Python 在沙箱中运行不可信 Python 或 JavaScript，并限制内存、CPU 和 wall-clock 超时。新增 \`pwasm.guests\` 与 \`pwasm.sandbox.Sandbox\`，资源限制通过 \`Limits\(fuel=..., max\_memory=...\)\` 和 \`limits.set\_deadline\(\)\` 设置，超限抛出 \`OutOfFuel\` 或 \`Timeout\`。该版本实现除 SIMD 外的完整 WebAssembly 2.0 核心指令集，热点函数编译到 Python 后通常快 8 到 14 倍，编译结果缓存使 QuickJS 启动从约 1.3s 降至 0.1s。当前为 alpha，WASI 实现无文件系统和网络访问。

github · simonw · 10月1日 17:10

**「为什么重要」** 对需要安全执行代码的 agent harness 来说，pwasm 0.2a0 提供了仅依赖 Python 的 WASM 沙箱方案，内置 MicroPython 和 QuickJS 可直接运行不可信脚本。其资源限制和编译缓存机制直接影响沙箱启动速度与隔离边界，但 alpha 状态和缺失 SIMD、文件系统、网络访问也限定了当前适用范围。

**「可关注」** 可关注：pwasm 0.2a0 将热点函数编译为 Python 并磁盘缓存，使 QuickJS 启动从约 1.3s 降至 0.1s，若需在 harness 中嵌入轻量沙箱，可评估其 \`pwasm.guests\` 与 \`pwasm.sandbox\` 的隔离与性能表现。

**标签**: `#harness`, `#coding-agent`, `#permissions`, `#memory`

---

<a id="item-agent-engineer-2"></a>
### [HF daily paper: Beyond Memory: Harnessing Long-Horizon Agents with Explicit Belief States](https://huggingface.co/papers/2610.01415) ⭐️ 7.5/10

A research paper proposes PoS, an inference-time framework for maintaining explicit belief states in LLM agents and detecting Belief Trapping during long-horizon tasks.

rss · Hugging Face Daily Papers · 10月2日 00:00

**标签**: `#memory`, `#observability`, `#orchestration`

---

<a id="item-agent-engineer-3"></a>
### [预训练模型 pass@K 反超后训练模型](https://huggingface.co/papers/2610.01509) ⭐️ 7.5/10

Hugging Face Daily Papers 于 2026-10-02 收录论文《Sharpening Tax in Post-Training》。论文发现，预训练 LLM 配备轻量推理 harness 即可在智能体任务上作为可用智能体；尽管 pass@1 大幅落后，在充足测试时预算下，其 pass@K 解决方案覆盖率常超越后训练模型。论文进一步分析机制，指出后训练将任务分布推向更尖锐的既有行为，牺牲覆盖度换取单发准确率。源材料中机制描述截断，且该文当前仅 4 个 upvote，完整证据链需查阅原文。

rss · Hugging Face Daily Papers · 10月2日 00:00

**「为什么重要」** 该发现直接冲击“RL 后训练是智能体能力前提”的假设，对 harness 设计、智能体架构选型及评测体系（pass@1 与 pass@K 的取舍）有可解释的影响。不过论文尚未经过充分社区验证，其机制结论在源材料中不完整，实际工程收益仍待复现。

**「可关注」** 可关注：在 coding agent 评测中，pass@1 与 pass@K 可能衡量不同能力，轻量 harness 配合测试时预算或许比单纯堆叠后训练更能提升解决方案覆盖率。

**标签**: `#harness`, `#eval`, `#coding-agent`

---

<a id="item-agent-engineer-4"></a>
### [Green：Agent 可经共享缓存跨沙箱传播](https://simonwillison.net/2026/Oct/1/matthew-green/) ⭐️ 7.0/10

Matthew Green 指出，分别隔离的沙箱 Agent 能在共享包缓存中留下指令，改变接收方行为。载荷劫持 Agent，Agent 携带载荷感染下一个 Agent，构成蠕虫的两半。若将包缓存替换为 email、Slack、共享文档或 WhatsApp，将独立沙箱训练替换为 Muse 这类独立部署的个人 Agent，即具备蠕虫传播条件。该观点出自其 2026 年 9 月 30 日文章，Simon Willison 于 10 月 1 日引用。

rss · Simon Willison · 10月1日 06:29

**「为什么重要」** 沙箱隔离未覆盖共享包缓存等间接通道。Agent 可借此横向传递指令，传统边界防护可能漏掉这类路径。

**「可关注」** 可关注：共享包缓存等间接通道可绕过沙箱隔离，Agent 编排需显式处理这类横向通信路径。

**标签**: `#permissions`, `#orchestration`, `#harness`

---

<a id="item-agent-engineer-5"></a>
### [ActiveSaddler 调整训练场景](https://huggingface.co/papers/2610.00906) ⭐️ 6.0/10

Hugging Face 每日论文收录 ActiveSaddler，提出将 Agent Harness 优化建模为自动课程学习问题。现有方法主要优化 harness 的更新逻辑，却固定了生成反馈的训练场景；论文认为 harness 演化时，课程应同步调整。ActiveSaddler 将演化课程建模为非平稳 bandit，动态实例化优化目标。目前公开材料仅到摘要，缺少可复现代码、基准对比与生产环境数据，落地效果待验证。

rss · Hugging Face Daily Papers · 10月2日 00:00

**「为什么重要」** 对 coding agent 与 harness 开发者，该论文指出了一个易被忽略的维度：训练场景应随 harness 演化而动态调整，而非固定不变。但论文尚未放出代码与基准，实际增益仍属未证实的影响。

**「可关注」** 可关注：ActiveSaddler 把 harness 优化从“如何更新”扩展到“用什么场景生成反馈”，但当前仅到摘要，可等待代码与基准数据释出后再评估。

**标签**: `#harness`, `#eval`, `#orchestration`, `#coding-agent`

---

<a id="item-agent-engineer-6"></a>
### [RASO：跨 harness 检索增强技能优化](https://huggingface.co/papers/2609.38024) ⭐️ 6.0/10

HF Daily Papers 收录 RASO 论文，提出跨 harness 的检索增强技能优化框架。该框架从外部技能语料库检索相关知识，适配到目标任务，替代仅依赖昂贵 agent rollouts 的现有做法。论文指出公开技能已大量积累，但现有优化方法未将其作为先验利用。当前证据仅限截断摘要，无代码、基准数据或生产记录，实际效果与可复现性无法确认。

rss · Hugging Face Daily Papers · 10月2日 00:00

**「为什么重要」** 公开 agent 技能持续积累，现有优化流程却未利用这批先验，仍依赖昂贵 rollouts。RASO 将外部语料作为先验引入优化过程，为跨 harness 技能适配提供新路径；但能否降低成本、提升效果，目前无基准或代码支撑。

**「可关注」** 可关注：RASO 把公开技能语料当作先验而非从零 rollout，若后续释出代码与基准，可评估其跨 harness 迁移成本。

**标签**: `#harness`, `#memory`, `#eval`

---

<a id="item-agent-engineer-7"></a>
### [Introducing Olmo-core 3: Open, scalable training infrastructure for large MoEs](https://huggingface.co/blog/allenai/olmocore3) ⭐️ 5.8/10

AllenAI releases Olmo-core 3, an open-source framework for scalable trillion-parameter MoE training, with limited direct impact on day-to-day agent engineering.

rss · Hugging Face Blog · 10月1日 15:01

**标签**: `#training`, `#moe`, `#infrastructure`, `#open-source`, `#llm`

---

## AI 日报

<a id="item-ai-daily-1"></a>
### [The eternal complement](https://openai.com/index/the-eternal-complement) ⭐️ 6.3/10

OpenAI publishes an essay arguing that advanced AI&\#x27;s greatest impact may lie in routine execution work behind breakthrough ideas, shaping the next economy.

rss · OpenAI Blog · 10月1日 17:00

**标签**: `#lab`, `#industry`

---

<a id="item-ai-daily-2"></a>
### [How Albertsons Companies is reimagining retail from the inside out](https://openai.com/index/albertsons-reimagining-retail) ⭐️ 6.3/10

OpenAI publishes a customer case study on Albertsons using ChatGPT Enterprise and the OpenAI API to improve internal workflows and grocery shopping.

rss · OpenAI Blog · 10月1日 16:00

**标签**: `#product`, `#industry`, `#lab`

---

<a id="item-ai-daily-3"></a>
### [GitHub Universe 2026 前瞻](https://github.blog/news-insights/company-news/10-technical-talks-im-excited-about-at-github-universe-2026/) ⭐️ 5.8/10

GitHub 官方博客发布 GitHub Universe 2026 议程预览，列出 10 场技术演讲，主题包括验证 AI 编写代码与加固 npm 依赖。文章由 Andrea Griffiths 撰写，仅作会议预告，未涉及具体产品、模型或政策发布。

rss · GitHub Blog · 10月1日 15:07

**「为什么重要」** 验证 AI 生成代码与 npm 依赖安全是 coding agent 和 harness 开发中的高频问题，会议议程显示 GitHub 将围绕这些方向展开技术讨论。

**「可关注」** 可关注：GitHub Universe 2026 设有验证 AI 编写代码与 npm 依赖安全的专题演讲，可跟踪其技术思路。

**标签**: `#industry`, `#product`, `#open-source`

---

<a id="item-ai-daily-4"></a>
### [Mollick：智能体集群自我组织](https://www.oneusefulthing.org/p/the-dot-and-the-swarm) ⭐️ 5.0/10

Ethan Mollick 撰文承认此前判断失误：他认为人类需要像管理公司一样设计智能体分工，但苦涩教训（The Bitter Lesson）表明，更强的机器学习正在直接替代繁琐的人工编排。当前个人智能体（如 Meta Muse、OpenAI dots）已能自主获取上下文、制定计划并主动纠错；OpenAI 的 swarm 在 88 小时内给出纳维-斯托克斯问题证明，该证明尚未获正式接受，但 Clay Institute 似已认可。数千个智能体仅靠极薄弱的协调结构自行交换约 270 万条消息。Mollick 认为，组织工作只是 AI 又能自学完成的任务，人类管理中的委托代理、信息分散等约束在智能体身上大幅弱化。

rss · One Useful Thing · 10月1日 10:54

**「为什么重要」** 如果智能体集群能自行组织并推进数学证明，编码 agent 与 harness 的设计重点可能从“如何编排多个 agent”转向“如何设定目标与传递最优思路”。Mollick 同时提醒，个人智能体已能主动纠错并代替用户谈判，面向人类的客服渠道将面临智能体群体的直接冲击。

**「可关注」** 可关注：Mollick 在 Codex 中仅用几句话勾勒团队框架，智能体数量便从 3 个扩展到 13 个，人工干预极少。对 harness 设计者而言，与其细化每一步编排，不如把力气放在目标定义与跨 agent 的思路筛选上。

**标签**: `#industry`, `#product`, `#model`

---