---
layout: default
title: "Horizon Summary: 2026-10-09 (EN)"
date: 2026-10-09
lang: en
---

> From 192 items, 17 important content pieces were selected

---

**Agent Harness Architecture**
1. [@openai/agents-core 0.20.0 Released](#item-harness-arch-1) ⭐️ 8.1/10
2. [Codex rust-v0.162.0 Released](#item-harness-arch-2) ⭐️ 8.0/10
3. [FastMCP v4.1.0 发布](#item-harness-arch-3) ⭐️ 7.8/10
4. [Claude Code 2.1.281](#item-harness-arch-4) ⭐️ 7.8/10
5. [Claude Code v2.1.295 发布](#item-harness-arch-5) ⭐️ 7.6/10
6. [OpenHands v1.26.0 Released](#item-harness-arch-6) ⭐️ 6.8/10
7. [Microsoft Agent Framework python-1.21.0 Released](#item-harness-arch-7) ⭐️ 6.8/10
8. [Anthropic open-sources knowledge-work-plugins](#item-harness-arch-8) ⭐️ 5.2/10

**AI Agent Engineer**
1. [Agent 监管基准 AgentMonBench 与 EBG 发布](#item-agent-engineer-1) ⭐️ 7.2/10
2. [TestPrism 提出多实现测试评测基准](#item-agent-engineer-2) ⭐️ 7.0/10
3. [Trace2Env：基于 Trace 仿真 Agent 交互环境](#item-agent-engineer-3) ⭐️ 6.0/10
4. [ttok 1.0 默认切换至 o200k\_base](#item-agent-engineer-4) ⭐️ 5.8/10
5. [ttok 0.4 发布，支持截断特殊 Token](#item-agent-engineer-5) ⭐️ 5.8/10
6. [Learn2Play Bench 评测基准发布](#item-agent-engineer-6) ⭐️ 5.8/10

**AI Daily**
1. [LegalOn 降低 Codex 成本 65%](#item-ai-daily-1) ⭐️ 5.8/10
2. [Oracle 用 Codex 构建工作流](#item-ai-daily-2) ⭐️ 5.3/10
3. [Last Week in AI 第 346 期发布](#item-ai-daily-3) ⭐️ 5.0/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [@openai/agents-core 0.20.0 Released](https://github.com/openai/openai-agents-js/releases/tag/%40openai/agents-core%400.20.0) ⭐️ 8.1/10

OpenAI released @openai/agents-core@0.20.0 in openai/openai-agents-js, tightening runtime turn enforcement, local tool sandboxing, and MCP tool discovery. Post-approval model calls now count toward maxTurns, requiring callers at the limit to raise thresholds for subsequent responses. The update caps automatic MCP tool listing to 64 pages by default, enforces runAs and trusted Python 3 for UnixLocal file tools, and redacts unchecked terminal output in cancelled session checkpoints.

github · github-actions\[bot\] · Oct 8, 23:04

**「Design Notes」** Human-in-the-loop approvals no longer bypass execution budgets, strictly binding resumed model calls to the session maxTurns limit. For local file tools, edits replace files without mutating existing hardlinks, require writable parent directories, and preserve sticky bits and ownership across manifest materialization and Docker snapshots.

**「What Changed」** MCP tool discovery defaults to 64 pages via maxListPages and preserves hosted discovery provenance across identity collisions. Checkpoints redact uninspected terminal output upon cancellation while retaining completion history, and overlapping agent runs now serialize resolved computer tool instances.

**Tags**: `#runtime`, `#tools`, `#mcp`, `#permissions`, `#sandbox`

---

<a id="item-harness-arch-2"></a>
### [Codex rust-v0.162.0 Released](https://github.com/openai/codex/releases/tag/rust-v0.162.0) ⭐️ 8.0/10

Codex released rust-v0.162.0, adding managed Git worktree creation and listing tools for trusted local projects when the feature is enabled. The release introduces opt-in ranked tool search and promise-streaming helpers in Code Mode, alongside remote compaction and live web access configuration for custom Responses-compatible providers. It also hardens Linux sandbox execution and restores Windows 10 drive-letter file access.

github · github-actions\[bot\] · Oct 8, 18:55

**「Design Highlights」** Worktree tools introduce native repository isolation scoped strictly to trusted local projects for parallel task workflows. On context and execution layers, custom model providers can delegate context compaction remotely, while Code Mode adds dynamic ranked tool discovery.

**「What Changed」** Codex adds managed Git worktrees, opt-in ranked tool search in Code Mode, and remote compaction toggles for custom Responses providers. The Linux sandbox now rejects writable construction executables and preserves deny-glob masks against ripgrep configuration.

**Tags**: `#runtime`, `#tools`, `#sandbox`, `#mcp`

---

<a id="item-harness-arch-3"></a>
### [FastMCP v4.1.0 发布](https://github.com/PrefectHQ/fastmcp/releases/tag/v4.1.0) ⭐️ 7.8/10

FastMCP 发布 v4.1.0 维护版本，集中修复 OpenAPI、代理与鉴权逻辑，恢复支持 Python 3.15。该版本收紧了多处安全输入边界，引入 MultiAuth 凭证隔离与 HTTP 会话超时等破坏性变更。官方建议在升级前执行完现有挂起任务。

github · jlowin · Oct 8, 22:56

**「设计要点」** MultiAuth 改为按来源限定客户端 ID 并重划所有权作用域；技能文件解析与 OpenAPI 路径参数强制施加目录边界校验，拦截路径遍历。

**「改了什么」** HTTP 会话恢复 MCP SDK 默认的 30 分钟空闲超时；工具搜索正则引擎换用 Pydantic 且不再支持环视与反向引用；CodeMode 要求 Monty 1.1 并将参数更名为 max\_feed\_duration\_secs。

**Tags**: `#mcp`, `#tools`, `#permissions`, `#runtime`

---

<a id="item-harness-arch-4"></a>
### [Claude Code 2.1.281](https://code.claude.com/docs/en/changelog#2-1-281) ⭐️ 7.8/10

Claude Code 2.1.281 adds enterprise gateway policies and runtime execution controls. The Claude apps gateway introduces desktop policy keys to block reads outside working directories and disable bypass permission mode, alongside Amazon Bedrock upstream STS role assumption \(\`assume\_role\`\) and mandatory guardrail enforcement. Command and HTTP hooks add \`onFailure: &quot;block&quot;\` to fail closed on timeouts or crashes, while self-hosted runners move system prompts from CLI flags to files.

rss · Claude Code Changelog · Oct 8, 19:00

**「Architecture Note」** The apps gateway adds STS role assumption on Bedrock upstreams with optional per-developer sessions and cross-account access, paired with uniform Bedrock guardrail evaluation across requests. Command and HTTP lifecycle hooks support fail-closed semantics \(\`onFailure: &quot;block&quot;\`\), blocking execution if hook processes fail to start, time out, or exit unexpectedly.

**「What Changed」** Self-hosted runners now pass system prompts via \`--system-prompt-file\` instead of command-line text to avoid launch failures with large prompts. Auto mode server-side reviews now block flagged read-only and sandboxed shell commands, and dangerous \`rm\` prompts in unattended sessions auto-deny with rewrite hints after two minutes.

**Tags**: `#permissions`, `#sandbox`, `#runtime`

---

<a id="item-harness-arch-5"></a>
### [Claude Code v2.1.295 发布](https://github.com/anthropics/claude-code/releases/tag/v2.1.295) ⭐️ 7.6/10

Claude Code 发布 v2.1.295 版本。命令与 HTTP hook 增加 onFailure: &quot;block&quot; 策略，执行失败、超时或异常退出时直接阻断后续操作。Claude apps gateway 增加 timeouts.upstream\_ttfb\_ms 配置以控制云端上游首包超时与故障切换，同时终端支持 OSC 7501 状态协议并修复多项子 agent 调度问题。

github · ashwin-ant · Oct 8, 19:48

**「设计要点」** Hook 运行时补齐阻断语义，避免防护钩子崩溃时默认放行；网关层将上游首字节时延（TTFB）纳入超时判定与路由故障切换，增强 Bedrock、Vertex 等多云 upstream 容灾能力。

**「改了什么」** Hook 增加 onFailure: &quot;block&quot; 选项；网关新增 timeouts.upstream\_ttfb\_ms 与 models 模型通配过滤；支持终端 OSC 7501 状态协议；修复远程 MCP 断开重连缺少指数退避，以及工作树子 agent 串扰父级 git 状态的缺陷。

**Tags**: `#runtime`, `#permissions`, `#tools`

---

<a id="item-harness-arch-6"></a>
### [OpenHands v1.26.0 Released](https://github.com/OpenHands/OpenHands/releases/tag/v1.26.0) ⭐️ 6.8/10

OpenHands released v1.26.0, focusing on agent behavioral verification and workspace management improvements. The update introduces the verify-openhands verification skill and control-openhands CLI with recipe mappings, converts empty-response corrective nudges into informational chat notes, and adds explanation and switching flows for suspended workspaces.

github · openhands-release-bot\[bot\] · Oct 8, 20:36

**「Architecture Note」** Evaluation harnesses now integrate the verify-openhands skill alongside the control-openhands CLI to drive live behavioral recipes and capture reproducible defects. At the runtime layer, automations now extract local run logs directly from server-level bash events, and MCP preserves catalog identity across repeated STDIO installations.

**「What Changed」** Added the verify-openhands skill, control-openhands CLI, and behavioral recipe mappings with daily pass support. Handled suspended workspaces with explicit explanations and switch prompts, rendered empty-response nudges as informational notes in chat, and minimized Canvas Docker runtime packages.

**Tags**: `#runtime`, `#tools`, `#eval`

---

<a id="item-harness-arch-7"></a>
### [Microsoft Agent Framework python-1.21.0 Released](https://github.com/microsoft/agent-framework/releases/tag/python-1.21.0) ⭐️ 6.8/10

Microsoft released agent-framework python-1.21.0. The update adds standing guidance for tool results, exposes rewritten variable-expansion arguments, and supports full-buffer Purview policy evaluation on streamed responses. It also introduces an alpha Oracle native vector-store connector and configurable maximum reasoning effort for OpenAI models.

github · jpalvarezl · Oct 8, 10:27

**「Architecture Note」** The runtime now isolates provider-owned service session state when subagents are invoked as tools across core, Foundry, and GitHub Copilot packages. Additionally, core execution serializes shared file modifications and runs local sibling tools in declaration-only mixed batches.

**「What Changed」** Added reasoning-effort configuration for OpenAI, an alpha Oracle vector connector, and SDK updates for Anthropic \(1.11\) and GitHub Copilot \(1.0.16\). Fixed resource leaks by properly closing delegated streams on early consumer termination across Gemini and Ollama integrations.

**Tags**: `#runtime`, `#tools`, `#memory`, `#subagents`

---

<a id="item-harness-arch-8"></a>
### [Anthropic open-sources knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) ⭐️ 5.2/10

Anthropic open-sourced \`anthropics/knowledge-work-plugins\`, a repository of role-specific plugins built for Claude Cowork and compatible with Claude Code. The plugins configure task execution procedures, tool and data source integrations, critical workflow handling, and custom slash commands for specialized roles. The repository provides workflow, tool, and prompt templates rather than core harness runtime or sandbox architecture modifications.

rss · GitHub Trending Daily · Oct 9, 05:59

**Tags**: `#tools`, `#subagents`, `#planning`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [Agent 监管基准 AgentMonBench 与 EBG 发布](https://huggingface.co/papers/2610.06406) ⭐️ 7.2/10

针对长程任务中 Agent 行为海量且证据分散导致人工核查困难的问题，该论文提出面向软件工程 Agent 监管的评测基准 AgentMonBench。该基准包含三个子集，覆盖需求与行为的一致性，以及对需人工介入的重大自主决策的识别能力。研究同时提出无需训练的行为图方案 EBG（Evidence-Grounded Behavior Graph），通过将关联源码的证据聚合为行为结构，辅助监督器定位关键决策。

rss · Hugging Face Daily Papers · Oct 9, 00:00

**「为什么重要」** 当长程 coding agent 逐步接管端到端开发，工程师的核心工作正从编写单步指令转向审查自主执行过程。该研究将评估重点从任务成功率推进到行为可解释性与关键决策识别，为自动化监管工具建立了标准化测试集。

**「可关注」** 可关注：构建 long-horizon agent 的 harness 时，直接平铺原始执行日志难以支持有效的人工介入，可参考 EBG 将零散执行记录组织为与源码绑定的行为图结构。

**Tags**: `#observability`, `#eval`, `#coding-agent`, `#harness`

---

<a id="item-agent-engineer-2"></a>
### [TestPrism 提出多实现测试评测基准](https://huggingface.co/papers/2610.12289) ⭐️ 7.0/10

研究团队提出测试生成评测基准 TestPrism，指出依赖单一参考解评测会显著虚高测试用例质量。该基准包含来自 17 个来源的 300 个测试任务与 3000 个候选实现，其中有效与无效实现各占一半。核心指标联合成功函数（Joint Success Function）要求生成的测试在初始状态失败、通过所有有效实现并拦截所有无效实现。在 14 种基线 coding agent 配置下，该指标达标率仅为 28.00%，远低于单参考解评测测出的 59.67%。

rss · Hugging Face Daily Papers · Oct 9, 00:00

**「为什么重要」** 单参考解评测无法识别过度拟合特定实现的脆弱断言。引入正反候选实现能反映测试集对替代有效代码的兼容度以及对故障的真实捕捉能力。

**「可关注」** 可关注：构建 coding agent 评测 harness 时，引入反例实现与多实现交叉校验，能过滤虚假测试通过率并暴露漏测问题。

**Tags**: `#eval`, `#coding-agent`, `#harness`

---

<a id="item-agent-engineer-3"></a>
### [Trace2Env：基于 Trace 仿真 Agent 交互环境](https://huggingface.co/papers/2610.06100) ⭐️ 6.0/10

针对真实运行系统难以访问或复刻的问题，论文提出免训练框架 Trace2Env。该方法将历史交互 Trace 重构成包含环境 Schema、支撑证据与行为知识的 Worldbook，并在运行时由 World Model Agent 结合持久化状态模拟交互环境，为 Task Agent 提供有状态仿真支持。

rss · Hugging Face Daily Papers · Oct 9, 00:00

**「为什么重要」** 它探索了无需重构可执行系统、仅靠历史交互日志搭建仿真环境的路径，为复杂沙盒的低成本复现提供了思路。不过，这类模拟环境的保真度仍取决于历史日志覆盖面与知识归纳质量。

**「可关注」** 可关注：在搭建 Agent 评测 Harness 且缺失外部环境接口时，利用历史调用链路提取规则并由 Agent 维护持久化状态的 Mock 方案。

**Tags**: `#eval`, `#harness`, `#orchestration`

---

<a id="item-agent-engineer-4"></a>
### [ttok 1.0 默认切换至 o200k\_base](https://github.com/simonw/ttok/releases/tag/1.0) ⭐️ 5.8/10

Simon Willison 发布 CLI Token 计数工具 ttok 1.0。该版本将默认 tokenizer 切换为 GPT-5 与 GPT-6 系列使用的 o200k\_base。此外，ttok --list-models 命令现可展示底层 tiktoken 库对 gpt-5\* 等模型前缀的具体映射逻辑。

github · simonw · Oct 9, 00:34

**「为什么重要」** 本地脚本与 harness 中依赖 ttok 快速估算输入开销的环节，其默认的分词基准已正式对齐新一代模型。

**「可关注」** 可关注：若测试脚本依赖未指定编码器的默认 ttok 命令统计旧模型上下文，需检查计费与截断预算是否因编码规则变化产生偏差，必要时显式传入模型参数。

**Tags**: `#harness`, `#observability`, `#eval`

---

<a id="item-agent-engineer-5"></a>
### [ttok 0.4 发布，支持截断特殊 Token](https://github.com/simonw/ttok/releases/tag/0.4) ⭐️ 5.8/10

CLI 分词工具 ttok 发布 0.4 版本。新版允许在计数与截断 Token 时使用 \`--allow-special\`，并修复了新版 Click 导致的 \`--tokens\` 重复警告。新版本还提供 \`--list-models\` 查看已安装 tiktoken 支持的模型，文档补全了 \`gpt-4o\` 与 \`o1\` 等 \`o200k\_base\` 模型，并将运行环境提升至 Python 3.10+。

github · simonw · Oct 8, 23:34

**「为什么重要」** 此前在截断或统计含特殊 Token 的输入时会直接报错。放开 \`--allow-special\` 后，工程师可直接通过管道将 \`files-to-prompt\` 的代码输出交给 ttok 进行上下文截断与预算控制。

**「可关注」** 可关注：ttok 已将打包方式迁移至 \`pyproject.toml\` 并要求 Python 3.10 及以上环境，在低版本运行环境中调用 CLI 需要注意环境兼容性。

**Tags**: `#harness`, `#coding-agent`, `#observability`

---

<a id="item-agent-engineer-6"></a>
### [Learn2Play Bench 评测基准发布](https://huggingface.co/papers/2610.08215) ⭐️ 5.8/10

研究者发布文本游戏基准 Learn2Play Bench，用于评估 LLM Agent 从交互经验中学习新知识的能力。现有评测基准多在指令中直接提供规则，或任务已被预训练模型熟知，难以区分交互学习与先验推理。该基准构建了规则全新且反直觉的文本游戏，要求 Agent 脱离预训练先验，纯靠环境交互反馈获取知识。

rss · Hugging Face Daily Papers · Oct 9, 00:00

**「为什么重要」** 现有评测容易把预训练记忆混淆为交互适应能力。该基准通过反直觉规则隔离模型先验，为检验 Agent 动态探索与记忆机制提供了对照环境。

**「可关注」** \*\*可关注\*\* 评测 Agent 交互学习与记忆更新机制时，可引入反直觉或人工构造的新规则，隔离预训练先验对评测结果的干扰。

**Tags**: `#eval`, `#memory`, `#orchestration`

---

## AI Daily

<a id="item-ai-daily-1"></a>
### [LegalOn 降低 Codex 成本 65%](https://openai.com/index/legalon-halves-codex-costs) ⭐️ 5.8/10

LegalOn 将日常 Codex 预估成本降低 65%，同时保持开发速度。团队将 Astra、Sol 和 Luna 分流至不同任务，并执行预算管理。

rss · OpenAI Blog · Oct 8, 12:00

**「可关注」** 可关注：按任务匹配模型并管控预算，可压缩 Codex 日常预估成本。

**Tags**: `#product`, `#industry`, `#lab`

---

<a id="item-ai-daily-2"></a>
### [Oracle 用 Codex 构建工作流](https://openai.com/index/oracle) ⭐️ 5.3/10

OpenAI 博客发布 Oracle 应用案例。Oracle 涵盖招聘、工程与运营业务，使用 ChatGPT Work 和 Codex 搭建工作流。材料未公开具体技术架构、量化数据与工程限制，属企业宣传。

rss · OpenAI Blog · Oct 8, 16:00

**Tags**: `#product`, `#industry`, `#lab`

---

<a id="item-ai-daily-3"></a>
### [Last Week in AI 第 346 期发布](https://lastweekin.ai/p/last-week-in-ai-346-719-math-manuscripts) ⭐️ 5.0/10

Last Week in AI 发布第 346 期周报。OpenAI 公布了未发布前沿模型产出的 719 份数学证明手稿。此外，Mistral 与 Reflection AI 推出开源权重模型，周报亦提及安全团队的人事变动。

rss · Last Week in AI · Oct 9, 05:06

**「可关注」** 可关注：OpenAI 前沿模型的数学证明手稿及 Mistral 开源权重模型进展。

**Tags**: `#model`, `#open-source`, `#lab`, `#industry`

---