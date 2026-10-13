---
layout: default
title: "Horizon Summary: 2026-10-13 (EN)"
date: 2026-10-13
lang: en
---

> From 182 items, 12 important content pieces were selected

---

**Agent Harness Architecture**
1. [OpenHands v1.27.0 Released](#item-harness-arch-1) ⭐️ 7.8/10
2. [LangGraph checkpoint 4.3.0 发布](#item-harness-arch-2) ⭐️ 6.8/10
3. [DSPy 3.4.1 Released](#item-harness-arch-3) ⭐️ 5.5/10
4. [Anthropic Open-Sources knowledge-work-plugins](#item-harness-arch-4) ⭐️ 5.0/10

**AI Agent Engineer**
1. [Codex CLI 默认安装常驻后台守护进程](#item-agent-engineer-1) ⭐️ 6.0/10
2. [Anthropic Explores Unix Principles for Claude Agent Workflows](#item-agent-engineer-2) ⭐️ 5.5/10
3. [终端长程 Agent 轨迹数据扩展论文发布](#item-agent-engineer-3) ⭐️ 5.5/10
4. [论文评估大模型思考惯性与无思考指令遵从](#item-agent-engineer-4) ⭐️ 5.5/10
5. [ARCS: Structured Disambiguation for Text-to-SQL](#item-agent-engineer-5) ⭐️ 5.5/10
6. [GUI Agent 历史检索仅对开局有效](#item-agent-engineer-6) ⭐️ 5.5/10
7. [Decision 3.0 开源：多模态免生成决策模型](#item-agent-engineer-7) ⭐️ 5.5/10

**AI Daily**
1. [GitHub Guides Copilot Custom Instructions and MCP](#item-ai-daily-1) ⭐️ 5.3/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [OpenHands v1.27.0 Released](https://github.com/OpenHands/OpenHands/releases/tag/v1.27.0) ⭐️ 7.8/10

OpenHands v1.27.0 integrates OpenCode and Pi as built-in ACP \(Agent Client Protocol\) agents on local backends and queries ACP model lists dynamically from the agent rather than hardcoding them. The verify-openhands test suite adds DeepSeek mock-LLM driving, browser video capture via \`browser record\`, and key-holding actions \(\`browser key down\|up\|release-all\`\). The release also introduces persistent automation draft workflows, connects Agent Canvas to DigitalOcean Managed Agents, and bumps agent-server to 1.54.0.

github · openhands-release-bot\[bot\] · Oct 12, 15:06

**「Architecture Note」** The ACP runtime delegates model enumeration directly to connected agents instead of maintaining static registries, standardizing local execution across OpenCode and Pi. For harness evaluation, verify-openhands pairs mock validation trajectory preservation with browser-level video capture and low-level key state controls.

**「What Changed」** Enabled built-in local ACP agent execution for OpenCode and Pi with dynamic agent model querying. Added \`browser record\` video recording, key hold and release actions, and DeepSeek mock-LLM driving to the verify-openhands harness.

**Tags**: `#runtime`, `#subagents`, `#eval`, `#tools`

---

<a id="item-harness-arch-2"></a>
### [LangGraph checkpoint 4.3.0 发布](https://github.com/langchain-ai/langgraph/releases/tag/checkpoint%3D%3D4.3.0) ⭐️ 6.8/10

LangGraph 发布 checkpoint 4.3.0。核心修复了状态持久化中的通道重放与写入顺序，恢复执行模式下的 delta 写入现按实时顺序重放。反序列化增加容错机制，对象无法重建时保留原始序列化数据。

github · github-actions\[bot\] · Oct 12, 22:26

**「改了什么」** Delta 通道重放改为按任务路径排序，恢复运行时的写入对齐实时顺序。分发存储前增加命名空间标签校验，并将 Store put 值类型放宽至 Mapping\[str, Any\]。

**Tags**: `#runtime`, `#memory`, `#eval`

---

<a id="item-harness-arch-3"></a>
### [DSPy 3.4.1 Released](https://github.com/stanfordnlp/dspy/releases/tag/3.4.1) ⭐️ 5.5/10

DSPy 3.4.1 makes GEPA&\#x27;s structured InstructionProposer the default reflection engine and enables dspy.RLM to instantiate DSPy sub-agents directly from inside its REPL. The runtime pools all sub-agent and query invocations under a single max\_llm\_calls budget while restricting sandboxed LM options to generation parameters. Upgrade notices include required JSON outputs for GEPA reflection models, reserved history and tools input names in dspy.ReActV2, and modified RLM prompt templates that invalidate 3.4.0 prompt caches.

github · isaacbmiller · Oct 12, 23:12

**「Architecture Note」** RLM builds and executes sub-agents on the host process, passing only JSON across the interpreter boundary to isolate execution while strictly metering completion slots against max\_llm\_calls. GEPA switches reflection formatting from raw prompt interpolation to dspy.Predict with JSONAdapter, preserving typed history and multimodal objects without flattening them into string representations.

**「What Changed」** GEPA adopts InstructionProposer as the default proposer and requires reflection\_lm to be a dspy.LM returning valid JSON. RLM adds sub-agent construction inside sandboxed REPL code, disallows inputs or tools named dspy or prefixed with \_dspy, and dspy.ReActV2 bans inputs named history or tools.

**Tags**: `#subagents`, `#runtime`, `#planning`, `#eval`

---

<a id="item-harness-arch-4"></a>
### [Anthropic Open-Sources knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) ⭐️ 5.0/10

Anthropic open-sourced \`anthropics/knowledge-work-plugins\`, a repository of plugins built for Claude Cowork and compatible with Claude Code. The plugins configure Claude for specific roles and teams by specifying workflows, external tools, data sources, and slash commands. The current source contains only the project overview and omits underlying runtime or implementation details.

rss · GitHub Trending Daily · Oct 13, 03:18

**Tags**: `#tools`, `#runtime`, `#planning`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [Codex CLI 默认安装常驻后台守护进程](https://github.com/openai/codex/issues/48195) ⭐️ 6.0/10

社区反馈 Codex CLI 默认在后台运行常驻且自更新的守护进程。该进程未在公开文档中说明关闭方式，运行时会在本地堆积历史版本，且自动更新时存在破坏权限的缺陷，可能导致 \`.git\` 目录变只读并阻塞任务。用户目前可在 \`~/.codex/config.toml\` 中设置 \`\[features\] daemon\_auto\_start = false\` 禁用自动启动。

hackernews · whimblepop · Oct 12, 18:29 · [Discussion](https://news.ycombinator.com/item?id=50060694)

**「为什么重要」** 本地 coding agent 若静默引入自动更新与常驻后台服务，一旦发生权限锁死，会直接破坏持续执行环境的稳定性。

**「可关注」** 可关注：排查长任务异常中断或磁盘暴涨时，可检查 \`~/.codex/\` 目录，通过配置 feature flag 彻底关闭后台守护进程自启。

**「评论」** 多位用户反映该守护进程占用磁盘高达 12 GB 且更新易锁死文件；部分工程师对 npm 安装包默认常驻进程表示不解，并探讨转向极简 harness 架构。

**Tags**: `#coding-agent`, `#harness`, `#permissions`

---

<a id="item-agent-engineer-2"></a>
### [Anthropic Explores Unix Principles for Claude Agent Workflows](https://www.latent.space/p/claude-dynamic-workflows) ⭐️ 5.5/10

At AI Engineer New York, Anthropic presented dynamic workflows for coordinating Claude agents, drawing on architectural lessons from Unix and Linux to help agents tackle larger projects without overwhelming developers. The discussion comes from secondary coverage of the conference talk, while production implementation details, APIs, and public code remain undisclosed.

rss · Latent Space · Oct 12, 18:18

**「Why it matters」** Applying Unix-style modular decomposition reflects an architectural shift toward structured multi-agent orchestration, though its actual impact on developer cognitive load remains unverified in practice.

**「Key takeaway」** Worth watching: dynamic workflow orchestration that splits complex agent harnesses into modular, single-purpose components.

**Tags**: `#orchestration`, `#coding-agent`, `#harness`

---

<a id="item-agent-engineer-3"></a>
### [终端长程 Agent 轨迹数据扩展论文发布](https://huggingface.co/papers/2610.13166) ⭐️ 5.5/10

该论文探讨终端智能体（Terminal agent）处理现实长程任务时的数据构建问题。作者指出短轨迹仅能展示命令与工具调用，无法覆盖智能体探索取证、根据反馈调优以及持续推进交付的完整链路。当前环境合成方法常提前简化关键任务，削弱了智能体实际面对的探索与验证需求。因公开材料截断，论文提出的具体合成架构与实验评估细节尚未完整披露。

rss · Hugging Face Daily Papers · Oct 13, 00:00

**「为什么重要」** 长程终端智能体训练依赖高质量行为轨迹，若合成环境过度垫步，模型将无法学到真实的纠错与反馈调整能力。

**「可关注」** 可关注：构建长程任务合成环境时，需审查是否提前抹平了探索摩擦，避免将缺少试错反馈的顺推脚本作为训练数据。

**Tags**: `#coding-agent`, `#orchestration`, `#eval`

---

<a id="item-agent-engineer-4"></a>
### [论文评估大模型思考惯性与无思考指令遵从](https://huggingface.co/papers/2610.11765) ⭐️ 5.5/10

论文研究大模型在收到「不思考」指令时的思考惯性。研究指出仅靠关闭思考模式或检测推理长度并不准确，模型在关闭后仍可能生成推理，长输出也可能只是填充 Token。作者将模型响应统一拆解为答前追踪与最终答案，从纯答案遵从率（Empty-Thinking Rate）与问题相关度等维度量化无思考状态下的执行表现。

rss · Hugging Face Daily Papers · Oct 13, 00:00

**「为什么重要」** Agent harness 常尝试用提示词关闭思考以降低单步延迟与 Token 成本。该研究证实关闭指令不能确保模型直接输出答案，可能导致调用成本偏离预期。

**「可关注」** 可关注：在编排层压低推理开销时，需核验模型响应是否仍夹带隐藏的答前追踪或填充 Token，避免无效计费。

**Tags**: `#eval`, `#harness`, `#orchestration`

---

<a id="item-agent-engineer-5"></a>
### [ARCS: Structured Disambiguation for Text-to-SQL](https://huggingface.co/papers/2610.09396) ⭐️ 5.5/10

Paper ARCS introduces structured disambiguation for text-to-SQL systems, resolving user intent ambiguities through explicit, constrained interactions rather than free-form conversational dialogue. The authors release ARCS \(Ambiguity Resolution Corpus for SQL\), a benchmark containing naturally occurring ambiguities over real-world databases. Specific evaluation metrics and comparative performance baselines are omitted in the available excerpt.

rss · Hugging Face Daily Papers · Oct 13, 00:00

**「Why It Matters」** Free-form multi-turn dialogue creates cognitive friction and execution drift in deployed data agents. Constrained disambiguation shifts clarification into a structured interaction primitive, though its concrete accuracy gains remain unverified in the provided snippet.

**「Takeaway」** Note: In SQL agent harnesses, replacing open-ended conversational clarification with constrained, structured disambiguation forms reduces interaction ambiguity and token overhead.

**Tags**: `#eval`, `#orchestration`, `#harness`

---

<a id="item-agent-engineer-6"></a>
### [GUI Agent 历史检索仅对开局有效](https://huggingface.co/papers/2609.33304) ⭐️ 5.5/10

现有个人 GUI Agent 常检索任务相关历史并拼接至上下文，默认历史经验对全程决策均有效。研究发现该收益基本在第一步耗尽：检索记录显著改善了开局决策，但在后续 90% 的步骤中几乎无持续增益，也难以为主动建议提供有效依据。相关记录虽能指引任务起点，却无法判定具体动作是否匹配当前界面；目前原始摘要存在截断，完整方案与评测细节尚不明确。

rss · Hugging Face Daily Papers · Oct 13, 00:00

**「为什么重要」** 该结论指出了任务级经验与步骤级决策之间的脱节，打破了相关经验能持续指导执行的假设。这表明单纯把相关历史推入上下文，无法解决长序列 GUI 交互与主动调度问题。

**「可关注」** 可关注：任务相关性不等于单步动作适用性，历史经验在开局后增益极弱，设计 Agent Memory 时需解耦意图引导与单步界面动作匹配。

**Tags**: `#memory`, `#harness`, `#orchestration`

---

<a id="item-agent-engineer-7"></a>
### [Decision 3.0 开源：多模态免生成决策模型](https://www.reddit.com/r/LocalLLaMA/comments/1x3th4p/decision_30_open_multimodal_decision_models_from/) ⭐️ 5.5/10

vLLM Semantic Router 团队开源 Decision 3.0 决策模型家族（0.6B 至 27B，Apache-2.0），基于 Qwen3.5 与 Qwen3.8-27B 改造。模型支持多图与视频输入，覆盖选择题、判断题和评分三类决策，不走文本生成，在单次调用内通过独立前向传播直接输出各项答案概率。团队基于 Jev 0.3 套件自测显示，27B 模型在文本（64.7）与视觉（71.6）榜单均列第一，并在未专门做视频训练的情况下取得 Perception Test 验证集 77.4 分。模型提供 BF16 权重，加载需启用 trust\_remote\_code=True。

reddit · r/LocalLLaMA · /u/henzy123 · Oct 12, 05:26

**「为什么重要」** 传统 Agent 路由和守卫机制多依赖生成式模型输出 JSON 再解析，存在格式漂移与解码耗时问题。该方案将多模态语义决策收敛为单次请求下的判别前向计算，为流水线编排提供了无需解码的多模态路由选择。

**「可关注」** 可关注：该模型通过分类头前向计算跳过自回归解码，但自定义架构仍需 trust\_remote\_code=True 加载，且现有基准均来自发布者在 Reddit 公布的自测数据。

**Tags**: `#orchestration`, `#eval`, `#harness`

---

## AI Daily

<a id="item-ai-daily-1"></a>
### [GitHub Guides Copilot Custom Instructions and MCP](https://github.blog/ai-and-ml/github-copilot/github-copilot-app-for-beginners-how-to-teach-copilot-about-your-codebase/) ⭐️ 5.3/10

GitHub published a beginner&\#x27;s guide detailing how to tailor Copilot to a codebase. The tutorial covers adding custom instructions and skills to repositories, configuring custom agents, and connecting Model Context Protocol \(MCP\) servers such as Playwright.

rss · GitHub Blog · Oct 12, 17:43

**Tags**: `#product`, `#industry`

---