---
layout: default
title: "Horizon Summary: 2026-10-13 (EN)"
date: 2026-10-13
lang: en
---

> From 200 items, 10 important content pieces were selected

---

**Agent Harness Architecture**
1. [OpenHands v1.27.0](#item-harness-arch-1) ⭐️ 7.8/10
2. [LangGraph checkpoint==4.3.0 Released](#item-harness-arch-2) ⭐️ 6.8/10
3. [DSPy 3.4.1 发布](#item-harness-arch-3) ⭐️ 5.5/10
4. [Anthropic Open-Sources knowledge-work-plugins](#item-harness-arch-4) ⭐️ 5.5/10

**AI Agent Engineer**
1. [Codex CLI 默认常驻后台守护进程引争议](#item-agent-engineer-1) ⭐️ 6.5/10
2. [长程终端智能体数据扩展研究公布](#item-agent-engineer-2) ⭐️ 6.0/10
3. [论文评估 LLM 禁思指令下的思考惯性](#item-agent-engineer-3) ⭐️ 5.8/10
4. [ARCS 提出结构化交互 Text-to-SQL 消歧](#item-agent-engineer-4) ⭐️ 5.5/10
5. [GUI Agent 经验检索被指仅首步有效](#item-agent-engineer-5) ⭐️ 5.5/10

**AI Daily**
1. [GitHub 推出 Copilot 代码库配置指南](#item-ai-daily-1) ⭐️ 5.3/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [OpenHands v1.27.0](https://github.com/OpenHands/OpenHands/releases/tag/v1.27.0) ⭐️ 7.8/10

OpenHands released v1.27.0, introducing OpenCode and Pi as built-in Agent Client Protocol \(ACP\) agents on local backends. The release expands the evaluation toolchain with DeepSeek mock-LLM end-to-end verification, browser video recording, and key-holding actions. It connects Agent Canvas to DigitalOcean Managed Agents and bumps agent-server to 1.54.0.

github · openhands-release-bot\[bot\] · Oct 12, 15:06

**「Architecture Note」** Shifts ACP model discovery from static runtime registries to dynamic inspection queried directly from agent instances. Extends the evaluation harness to preserve mock validation trajectories during end-to-end model gap mapping and capture browser video streams during task runs.

**「What Changed」** Integrates OpenCode and Pi as built-in local ACP agents and queries ACP model lists dynamically from agents instead of hardcoding them. Adds browser video capture via \`browser record\`, discrete key holding with \`browser key down\|up\|release-all\`, and preserved mock-LLM validation trajectories on DeepSeek.

**Tags**: `#eval`, `#subagents`, `#runtime`, `#tools`

---

<a id="item-harness-arch-2"></a>
### [LangGraph checkpoint==4.3.0 Released](https://github.com/langchain-ai/langgraph/releases/tag/checkpoint%3D%3D4.3.0) ⭐️ 6.8/10

LangGraph released checkpoint==4.3.0, focusing on state restoration consistency and persistence reliability. The patch fixes delta write replay ordering on resumed runs, prevents state loss when object deserialization fails, and enforces namespace label validation before dispatching to backing stores. It also defaults InMemorySaver delta history to the latest checkpoint and expands Store.put value typing to Mapping\[str, Any\].

github · github-actions\[bot\] · Oct 12, 22:26

**「Architecture Note」** Enforces namespace label validation across checkpoint-postgres, checkpoint-sqlite, and base checkpoint implementations before store dispatch. Task path-ordered delta channel replay ensures deterministic state reconstruction across distributed execution steps.

**「What Changed」** Replays resumed exit-mode runs&\#x27; delta writes in live execution order and sorts delta channel replay strictly by task path. Preserves raw serialized payloads when an object fails reconstruction rather than failing catastrophically, and widens Store.put accepted value types to Mapping\[str, Any\].

**Tags**: `#runtime`, `#memory`

---

<a id="item-harness-arch-3"></a>
### [DSPy 3.4.1 发布](https://github.com/stanfordnlp/dspy/releases/tag/3.4.1) ⭐️ 5.5/10

DSPy 3.4.1 发布。\`dspy.RLM\` 允许在 REPL 内导入并构建子 Agent，调用与父级共用 \`max\_llm\_calls\` 配额。GEPA 默认改用基于 \`JSONAdapter\` 的结构化 \`InstructionProposer\`，要求反射模型必须支持 JSON 输出。\`dspy.ReActV2\` 禁止输入字段命名为 \`history\` 或 \`tools\`。

github · isaacbmiller · Oct 12, 23:12

**「设计要点」** 子 Agent 由宿主机构建并执行，跨解释器边界仅传递 JSON；沙箱代码仅能调整温度和缓存等生成参数，无法修改模型与请求头。GEPA 反射保留 \`dspy.History\` 与图像等对象的结构化语义，直接通过 \`dspy.Predict\` 交付反射模型。

**「改了什么」** RLM 提示词默认追加子 Agent 引导段落，子 Agent 与 \`llm\_query\` 统一计入同一调用预算。GEPA 调整默认反射请求结构，导致同种子优化结果与 3.4.0 不一致，且不再兼容纯函数式反射模型。

**Tags**: `#subagents`, `#runtime`, `#tools`

---

<a id="item-harness-arch-4"></a>
### [Anthropic Open-Sources knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) ⭐️ 5.5/10

Anthropic open-sourced \`anthropics/knowledge-work-plugins\`, a repository of role- and team-specific workflow plugins built for Claude Cowork and compatible with Claude Code. The plugins configure how Claude executes tasks by defining tool and data integrations, workflow steps, and slash commands for knowledge work. The repository provides application-layer role configurations rather than core agent harness runtime modifications.

rss · GitHub Trending Daily · Oct 13, 03:42

**Tags**: `#tools`, `#planning`, `#subagents`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [Codex CLI 默认常驻后台守护进程引争议](https://github.com/openai/codex/issues/48195) ⭐️ 6.5/10

GitHub 与 Hacker News 讨论指出，Codex CLI 默认在后台安装并常驻自更新守护进程。用户反馈该机制累积旧版本占用高达 12 GB 磁盘空间，且自动更新时曾出现改动文件权限、致使 \`.git\` 变为只读并中断任务的情况。该功能未见官方文档公开说明，目前可通过在 \`~/.codex/config.toml\` 中添加 \`\[features\] daemon\_auto\_start = false\` 关闭自启。

hackernews · whimblepop · Oct 12, 18:29 · [Discussion](https://news.ycombinator.com/item?id=50060694)

**「可关注」** 可关注：若在受控开发机或 CI 环境中使用 Codex CLI，可在 \`~/.codex/config.toml\` 中显式设置 \`daemon\_auto\_start = false\`，规避后台自动更新引发的磁盘膨胀与 \`.git\` 权限漂移。

**「评论」** 有开发者吐槽守护进程频发 bug 阻断工作流，不得不软链接 PID 文件至 \`/dev/null\` 并锁定；也有用户指出 Claude Code 同样存在多版本二进制留存及后台常驻进程的设计。

**Tags**: `#coding-agent`, `#harness`, `#permissions`

---

<a id="item-agent-engineer-2"></a>
### [长程终端智能体数据扩展研究公布](https://huggingface.co/papers/2610.13166) ⭐️ 6.0/10

论文《Scaling Agentic Data for Long-Horizon Terminal Intelligence》探讨如何为终端智能体构建长程任务轨迹数据。作者指出短轨迹仅展示命令与工具调用，无法体现智能体通过探索累积证据并动态调优策略的完整链条；同时现有环境合成机制常预先简化关键步骤，变相消除了智能体探索与验证的必要。因公开摘要在解决方案处截断，具体方法与实验基准仍待原文确认。

rss · Hugging Face Daily Papers · Oct 13, 00:00

**「为什么重要」** 终端智能体正从单步执行走向复杂专业交付，厘清环境合成与真实探索之间的断层，是合成有效长程训练数据的关键前置问题。

**「可关注」** 可关注：构建长程任务合成环境时，需防止环境初始化脚本过早消解中间验证工作，避免训练轨迹丧失试错与策略调整的信息密度。

**Tags**: `#coding-agent`, `#orchestration`, `#eval`, `#harness`

---

<a id="item-agent-engineer-3"></a>
### [论文评估 LLM 禁思指令下的思考惯性](https://huggingface.co/papers/2610.11765) ⭐️ 5.8/10

论文《Thinking Inertia》提出了评估大语言模型在被要求禁止思考时遵从度的测试框架。研究指出，直接禁用思考模式或依据文本长度判断并不准确，模型常在关闭思考模式后仍生成推理内容。该框架将响应拆分为答前轨迹与最终答案，从纯答案遵从率（Empty-Thinking Rate）以及问题与答前轨迹的相关度等维度量化模型的禁思表现。

rss · Hugging Face Daily Papers · Oct 13, 00:00

**「为什么重要」** 构建 Agent harness 时，工程师常试图在简单任务中关闭推理模式以削减延迟和 Token 成本。该研究指出模型存在不听指令的推理惯性，提示词层面的关停要求未必能切实减少隐藏开销。

**「可关注」** 可关注：评估 Agent 的非思考路径时，不能仅依赖调用参数中的关闭开关，需检查模型输出最终答案前是否仍夹带答前推理轨迹。

**Tags**: `#eval`, `#harness`, `#orchestration`

---

<a id="item-agent-engineer-4"></a>
### [ARCS 提出结构化交互 Text-to-SQL 消歧](https://huggingface.co/papers/2610.09396) ⭐️ 5.5/10

论文针对真实场景中 Text-to-SQL 的隐蔽歧义问题，提出结构化消歧（structured disambiguation）范式与对应评测基准 ARCS。该方案放弃高认知成本且低效的多轮自由对话澄清，改用显式、受限的交互机制确认用户意图。ARCS 覆盖真实数据库中自然产生的无约束歧义，具体交互协议与工程工具链细节仍待论文完整公开。

rss · Hugging Face Daily Papers · Oct 13, 00:00

**「为什么重要」** 自然语言意图歧义是 Text-to-SQL 离线准确率高但上线频繁翻车的主因。将澄清过程从发散的开放式追问收敛为结构化交互，有望系统性降低交互轮次与解析漂移风险。

**「可关注」** 可关注：构建数据查询 Agent 时，尝试用带约束的表单或枚举选项代替自由文本反问，降低澄清环节的 token 消耗与状态解析不确定性。

**Tags**: `#eval`, `#orchestration`, `#coding-agent`

---

<a id="item-agent-engineer-5"></a>
### [GUI Agent 经验检索被指仅首步有效](https://huggingface.co/papers/2609.33304) ⭐️ 5.5/10

论文《Relevance Does Not Imply Applicability》指出，个人 GUI Agent 将任务相关交互历史拼入上下文的做法存在明显局限。检索经验能显著提升单轮任务的首步决策，但在后续 90% 的步骤中增益极微，且难以有效指导何时发起主动建议。相关历史仅能提示任务起点，无法判定过往动作是否适用于当前屏幕，原始材料在核心机理阐述处截断。

rss · Hugging Face Daily Papers · Oct 13, 00:00

**「为什么重要」** 研究揭示了记忆检索机制的常见盲区：任务级相关性不代表步骤级适用性。盲目向多步决策注入全局历史，不仅无法提升长尾步骤的执行质量，还可能引入冗余上下文噪声。

**「可关注」** 可关注：GUI Agent 的经验激活需从任务级静态检索转向屏幕状态级动态判定，避免将整段历史无差别塞入后续步骤的决策上下文。

**Tags**: `#memory`, `#harness`, `#orchestration`

---

## AI Daily

<a id="item-ai-daily-1"></a>
### [GitHub 推出 Copilot 代码库配置指南](https://github.blog/ai-and-ml/github-copilot/github-copilot-app-for-beginners-how-to-teach-copilot-about-your-codebase/) ⭐️ 5.3/10

GitHub 官方发布面向初学者的指南，介绍如何帮助 GitHub Copilot 适配具体代码库。内容涵盖为仓库添加自定义指令与技能、使用自定义 Agent，以及连接 Playwright 等 MCP 服务器。文章主要梳理基础用法，未包含新功能发布。

rss · GitHub Blog · Oct 12, 17:43

**「可关注」** 可关注：GitHub 推荐通过仓库级自定义指令、技能定义及 MCP 服务器接入 Playwright 等外部工具，统一补齐 Copilot 的项目上下文。

**Tags**: `#product`, `#industry`

---