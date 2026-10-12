---
layout: default
title: "Horizon Summary: 2026-10-13 (EN)"
date: 2026-10-13
lang: en
---

> From 191 items, 12 important content pieces were selected

---

**Agent Harness Architecture**
1. [OpenHands v1.27.0](#item-harness-arch-1) ⭐️ 7.8/10
2. [LangGraph checkpoint 4.3.0 Released](#item-harness-arch-2) ⭐️ 6.8/10
3. [DSPy 3.4.1 Released](#item-harness-arch-3) ⭐️ 5.5/10
4. [anthropics/knowledge-work-plugins Released](#item-harness-arch-4) ⭐️ 5.5/10

**AI Agent Engineer**
1. [Anthropic Shows Small AI Models Nearing Autonomous IoT Replication](#item-agent-engineer-1) ⭐️ 7.8/10
2. [SoftwareGym 自动合成 GUI 软件训练环境](#item-agent-engineer-2) ⭐️ 6.8/10
3. [Codex CLI 默认安装常驻后台进程引争议](#item-agent-engineer-3) ⭐️ 6.0/10
4. [ProgramGym 提出长程程序复现训练环境](#item-agent-engineer-4) ⭐️ 6.0/10
5. [Work2Skill 诱导 GUI 复用技能](#item-agent-engineer-5) ⭐️ 5.8/10
6. [Anthropic 借鉴 Unix 哲学协调 Claude Agent](#item-agent-engineer-6) ⭐️ 5.5/10
7. [Decision 3.0 多模态决策模型开源](#item-agent-engineer-7) ⭐️ 5.5/10

**AI Daily**
1. [GitHub Copilot 发布代码库上下文配置指南](#item-ai-daily-1) ⭐️ 5.3/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [OpenHands v1.27.0](https://github.com/OpenHands/OpenHands/releases/tag/v1.27.0) ⭐️ 7.8/10

OpenHands released v1.27.0, integrating OpenCode and Pi as built-in Agent Client Protocol \(ACP\) agents on local backends. The runtime now retrieves ACP model lists directly from agents instead of hardcoding presets, and connects Agent Canvas to DigitalOcean Managed Agents. End-to-end verification expands with mock-LLM DeepSeek evaluation runs and browser interaction recording.

github · openhands-release-bot\[bot\] · Oct 12, 15:06

**「Architecture Note」** Local ACP agent integration decouples model registry management by querying available models dynamically from the agent runtime. The verification harness preserves mock validation trajectories and adds browser video recording and granular key-press primitives for browser-based agent testing.

**「What Changed」** Added built-in local ACP support for OpenCode and Pi with dynamic agent model listing. Added browser video capture via \`browser record\` and discrete key controls \(\`browser key down\|up\|release-all\`\) to the verification runtime.

**Tags**: `#subagents`, `#runtime`, `#eval`, `#tools`

---

<a id="item-harness-arch-2"></a>
### [LangGraph checkpoint 4.3.0 Released](https://github.com/langchain-ai/langgraph/releases/tag/checkpoint%3D%3D4.3.0) ⭐️ 6.8/10

LangGraph released checkpoint 4.3.0 for its agent state persistence runtime. The update resolves state consistency bugs across replay and resume workflows, focusing on delta channel ordering, exit-mode write replays, and Store namespace validation. It also prevents data loss when stored objects fail to deserialize.

github · github-actions\[bot\] · Oct 12, 22:26

**「Architecture Note」** The runtime enforces deterministic state reconstruction by sorting delta channel replay by task path and replaying resumed exit-mode writes in live execution order. It also preserves raw serialized bytes if object reconstruction fails and adds namespace label validation before dispatching to SQLite or Postgres backends.

**「What Changed」** Ordered delta channel replay by task path and aligned resumed exit-mode delta replays with live execution order. Added namespace label validation before Store dispatch, defaulted InMemorySaver delta history to the latest checkpoint, and widened the Store.put value type to Mapping\[str, Any\].

**Tags**: `#runtime`, `#memory`, `#eval`

---

<a id="item-harness-arch-3"></a>
### [DSPy 3.4.1 Released](https://github.com/stanfordnlp/dspy/releases/tag/3.4.1) ⭐️ 5.5/10

DSPy 3.4.1 makes GEPA&\#x27;s structured InstructionProposer the default prompt optimizer and enables dspy.RLM to instantiate DSPy sub-agents directly inside its REPL. Sub-agent calls now consume slots from the parent max\_llm\_calls quota, and sandboxed code cannot modify provider endpoints or credentials. The release also disallows inputs named history or tools in dspy.ReActV2 signatures and requires GEPA reflection models to output adapter-parseable JSON.

github · isaacbmiller · Oct 12, 23:12

**「Architecture Note」** Sub-agents run on the host runtime rather than within the sandbox, passing only JSON across the interpreter boundary. A single max\_llm\_calls budget tracks llm\_query calls and sub-agent completions alike, while sandboxed calls restrict configurable LM parameters strictly to generation options like temperature and response\_format.

**「What Changed」** Code executed inside dspy.RLM can now import dspy and run Predict, ChainOfThought, ReActV2, or nested RLM instances. GEPA defaults to InstructionProposer backed by JSONAdapter instead of raw backtick prompt extraction, dropping unadapted plain-function reflection models.

**Tags**: `#subagents`, `#runtime`, `#tools`

---

<a id="item-harness-arch-4"></a>
### [anthropics/knowledge-work-plugins Released](https://github.com/anthropics/knowledge-work-plugins) ⭐️ 5.5/10

Anthropic open-sourced \`anthropics/knowledge-work-plugins\`, a plugin repository built for Claude Cowork and compatible with Claude Code. The plugins configure role- and team-specific workflows by specifying data sources, tool integrations, and custom slash commands. The repository operates purely at the application configuration level, providing no underlying agent harness runtime, sandboxing, or execution infrastructure details.

rss · GitHub Trending Daily · Oct 12, 23:18

**Tags**: `#tools`, `#runtime`, `#permissions`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [Anthropic Shows Small AI Models Nearing Autonomous IoT Replication](https://www.anthropic.com/research/self-replicating-ai) ⭐️ 7.8/10

Anthropic&\#x27;s Frontier Red Team demonstrated that small AI models are approaching the ability to self-replicate across low-cost commercial IoT devices without datacenter access. In simplified evaluations, GLM-5.2 and stronger models completed end-to-end autonomous replication chains, while Qwen3.5-9B configured working inference environments on 8 of 9 tested heterogeneous hardware types. The researchers also ran Gemma4-26B-A4B distributed across 15 networked off-brand Android TV boxes \($55 each, 4GB RAM\) at 0.39 tokens per second under pipeline parallelism. While sub-30B models still fail when composing the full multi-step lifecycle autonomously, Anthropic estimates historical progress could bring small open-weight models to full standalone replication capability within months.

rss · Anthropic Research · Oct 12, 00:00

**「Why It Matters」** The study demonstrates that autonomous replication and adaptation \(ARA\) does not strictly depend on centralized, easily monitored datacenter GPU clusters. Demonstrating distributed inference across weakly defended edge hardware shifts the security perimeter from cloud infrastructure controls to decentralized, difficult-to-sever botnet architectures.

**「Takeaway」** Watch for the Memento harness design: to prevent coding agents from fixating on dead-end debugging loops during long-horizon execution, it periodically respawns fresh agent instances that inherit only the workspace and concise handoff notes from previous runs.

**Tags**: `#eval`, `#permissions`, `#harness`, `#orchestration`

---

<a id="item-agent-engineer-2"></a>
### [SoftwareGym 自动合成 GUI 软件训练环境](https://huggingface.co/papers/2610.12611) ⭐️ 6.8/10

针对计算机使用 Agent（CUA）缺乏可靠软件环境的问题，研究者提出自动化合成流水线 SoftwareGym。该方案生成结构多样化的 GUI 设计并转化为可运行程序，通过运行时评估与迭代修复保障功能可用性。相比接入成本高的原生软件与交互深度有限的浏览器环境，该方法旨在降低特定应用过拟合风险，目前已合成 182 款应用。

rss · Hugging Face Daily Papers · Oct 12, 00:00

**「为什么重要」** CUA 训练与评测长期受限于原生软件的高集成成本和浏览器环境的浅层交互。利用自动化合成配合运行时修复批量提供可运行环境，尝试解决训练环境规模化扩展的瓶颈。

**「可关注」** 可关注：流水线通过运行时 GUI 评估配合迭代修复保证生成应用的功能可靠性，避免单次静态生成导致的环境失效。

**Tags**: `#harness`, `#eval`, `#coding-agent`

---

<a id="item-agent-engineer-3"></a>
### [Codex CLI 默认安装常驻后台进程引争议](https://github.com/openai/codex/issues/48195) ⭐️ 6.0/10

社区反馈 Codex CLI 默认在后台安装并运行自更新常驻 daemon。该进程缺乏公开文档说明，留存的历史版本可能累积占用大量磁盘空间，并在自动更新时偶发破坏本地文件权限，甚至将 .git 目录设为只读导致执行中断。

hackernews · whimblepop · Oct 12, 18:29 · [Discussion](https://news.ycombinator.com/item?id=50060694)

**「为什么重要」** 本地 coding agent 依赖宿主机环境与文件系统稳定性。CLI 工具链若隐式常驻后台自更新，容易引入非预期的权限突变与状态污染，直接打断自动化任务链。

**「可关注」** 可关注：若需关闭后台进程，可在 ~/.codex/config.toml 中添加 \[features\] daemon\_auto\_start = false，并排查 ~/.codex 下旧版本占用的磁盘空间。

**「评论」** 多位用户反映 daemon 故障率高且更新时易卡死目标任务；部分开发者转而推崇极简 harness，通过标准系统提示词调用 Bash 与原生 CLI，避开多余的后台常驻设计。

**Tags**: `#coding-agent`, `#harness`, `#permissions`

---

<a id="item-agent-engineer-4"></a>
### [ProgramGym 提出长程程序复现训练环境](https://huggingface.co/papers/2610.13395) ⭐️ 6.0/10

论文提出 ProgramGym 框架，包含 Program-Env 与 Program-Agent 两部分，面向从零复现软件的 coding agent 提供可扩展且可验证的训练环境。针对现有工作流无法支撑在实现前探索参考程序、难以自主推导需求与架构设计的断层，该工作尝试补齐长程开发能力。由于论文摘要文本截断，Program-Env 从代码仓库构建验证环境的具体机制和基准评测数据尚未完整公开。

rss · Hugging Face Daily Papers · Oct 12, 00:00

**「为什么重要」** coding agent 训练正从局部 issue 修复延伸至端到端构建程序。该框架尝试把探索参考代码与长程复现纳入训练环境，契合 agent harness 向多阶段长程演进的需求。

**「可关注」** 可关注：当智能体任务目标转向从零开发完整系统时，训练端如何解耦实现前的参考程序探索流程，并从既有代码库中自动化构建可验证信号。

**Tags**: `#coding-agent`, `#harness`, `#eval`, `#orchestration`

---

<a id="item-agent-engineer-5"></a>
### [Work2Skill 诱导 GUI 复用技能](https://huggingface.co/papers/2610.12984) ⭐️ 5.8/10

Work2Skill 提出从人类桌面 GUI 示教中诱导可复用技能的框架，面向处理复杂工作流与陌生软件的 computer-use agent。框架通过采集组件 WorkRecorder 同步对齐屏幕录像、键鼠操作事件与无障碍树信息，并构建了多模态示教数据集 WorkDemo-350。当前材料仅为摘要片段，论文与代码尚未完全公开，规则抽取算法的实际泛化效果仍有待验证。

rss · Hugging Face Daily Papers · Oct 12, 00:00

**「为什么重要」** GUI agent 面临陌生软件时常受限于领域知识，直接复用人工示教又难以拆解工作流通用规则与单次任务参数。该工作通过结构化对齐操作轨迹与系统无障碍树，为桌面示教诱导可复用技能提供了标准化数据基线。

**「可关注」** 可关注：采集桌面 GUI 示教数据时，仅依赖录屏难以解耦操作上下文，需将屏幕画面、键鼠事件流与系统无障碍树结构同步对齐。

**Tags**: `#memory`, `#harness`, `#eval`

---

<a id="item-agent-engineer-6"></a>
### [Anthropic 借鉴 Unix 哲学协调 Claude Agent](https://www.latent.space/p/claude-dynamic-workflows) ⭐️ 5.5/10

Anthropic 在 AI Engineer 峰会上分享了 Claude 多智能体编排思路。团队借鉴 Unix 与 Linux 的设计哲学构建动态工作流，试图让 Agent 承接更大规模项目，同时减轻开发者的认知负担。本次分享未提供完整工程白皮书或具体代码实现细节。

rss · Latent Space · Oct 12, 18:18

**「为什么重要」** 随着智能体任务复杂度上升，编排机制借鉴经典操作系统的小工具与组合哲学成为可行路径。目前该设计仍停留在演讲思路阶段，实际协调效率和工程约束尚未得到公开验证。

**「可关注」** 可关注：复杂任务编排中类似 Unix 哲学的职责解耦思路，但需留意缺乏具体协议与代码实现时的落地难度。

**Tags**: `#orchestration`, `#harness`, `#coding-agent`

---

<a id="item-agent-engineer-7"></a>
### [Decision 3.0 多模态决策模型开源](https://www.reddit.com/r/LocalLLaMA/comments/1x3th4p/decision_30_open_multimodal_decision_models_from/) ⭐️ 5.5/10

vLLM Semantic Router 团队在 Reddit 宣布以 Apache-2.0 协议开源 Decision 3.0 决策模型，参数覆盖 0.6B 至 27B。模型基于 Qwen3.5 与 Qwen3.8-27B 构建并集成视觉编码器，专用于免生成概率判定，单次前向可并行输出选项概率或分值。团队称其在官方 Jev 0.3 评估中位列榜首且支持零样本视频输入，但目前仅有社区发帖，缺乏正式技术报告与基座命名细节。

reddit · r/LocalLLaMA · /u/henzy123 · Oct 12, 05:26

**「为什么重要」** 多模态 Agent 传统上依赖大模型生成文本完成路由与守卫，时延与成本偏高。该模型将多模态判定收敛为免生成的直接概率输出，若实际路由效果属实，可显著压缩多模态编排链路的判定开销。

**「可关注」** 可关注：模型支持单次调用下多问题并行概率判定且免文本生成，适合前置守卫与意图路由，但需留意其依赖 trust\_remote\_code 加载且基座真实性尚待代码仓库验证。

**Tags**: `#orchestration`, `#eval`, `#harness`

---

## AI Daily

<a id="item-ai-daily-1"></a>
### [GitHub Copilot 发布代码库上下文配置指南](https://github.blog/ai-and-ml/github-copilot/github-copilot-app-for-beginners-how-to-teach-copilot-about-your-codebase/) ⭐️ 5.3/10

GitHub 发布面向初学者的 Copilot 教程，介绍如何让助手理解代码库。内容涵盖为仓库添加自定义指令与技能、配置自定义 agent，以及接入 Playwright 等 MCP 服务器。

rss · GitHub Blog · Oct 12, 17:43

**「可关注」** 可关注：教程演示了将 Playwright 等外部工具作为 MCP 服务器接入 Copilot 上下文的用法。

**Tags**: `#product`, `#industry`, `#open-source`

---