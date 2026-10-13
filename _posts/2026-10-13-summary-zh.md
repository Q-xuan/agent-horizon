---
layout: default
title: "Horizon Summary: 2026-10-13 (ZH)"
date: 2026-10-13
lang: zh
---

> 从 182 条内容中筛选出 12 条重要资讯。

<nav id="ah-toc" class="ah-toc" aria-label="目录"><span class="ah-toc-title">目录</span><ul><li><a href="#sec-harness-arch"><span class="ah-toc-name">Harness 架构</span><span class="ah-toc-count">4条</span></a></li><li><a href="#sec-agent-engineer"><span class="ah-toc-name">Agent 工程师日报</span><span class="ah-toc-count">7条</span></a></li><li><a href="#sec-ai-daily"><span class="ah-toc-name">AI 日报</span><span class="ah-toc-count">1条</span></a></li></ul></nav>

---

**[Harness 架构](#sec-harness-arch)**
1. [OpenHands v1.27.0 发布](#item-harness-arch-1) ⭐️ 7.8/10
2. [LangGraph checkpoint 4.3.0 发布](#item-harness-arch-2) ⭐️ 6.8/10
3. [DSPy 3.4.1 发布](#item-harness-arch-3) ⭐️ 5.5/10
4. [Anthropic 开源 knowledge-work-plugins](#item-harness-arch-4) ⭐️ 5.0/10

**[Agent 工程师日报](#sec-agent-engineer)**
1. [Codex CLI 默认常驻守护进程引争议](#item-agent-engineer-1) ⭐️ 6.0/10
2. [Anthropic 借鉴 Unix 哲学编排 Claude Agent](#item-agent-engineer-2) ⭐️ 5.5/10
3. [论文探讨长程终端 Agent 轨迹数据扩展](#item-agent-engineer-3) ⭐️ 5.5/10
4. [研究揭示大模型禁思指令下的思考惯性](#item-agent-engineer-4) ⭐️ 5.5/10
5. [Text-to-SQL 意图消歧基准 ARCS 提出](#item-agent-engineer-5) ⭐️ 5.5/10
6. [GUI Agent 经验检索仅在初始步骤有效](#item-agent-engineer-6) ⭐️ 5.5/10
7. [Decision 3.0 多模态决策模型开源](#item-agent-engineer-7) ⭐️ 5.5/10

**[AI 日报](#sec-ai-daily)**
1. [GitHub 发布 Copilot 代码库配置指南](#item-ai-daily-1) ⭐️ 5.3/10

---

## Harness 架构
{: #sec-harness-arch .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-harness-arch" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-harness-arch-1"></a>
### [OpenHands v1.27.0 发布](https://github.com/OpenHands/OpenHands/releases/tag/v1.27.0) ⭐️ 7.8/10

OpenHands 发布 v1.27.0。本地后端新增 OpenCode 与 Pi 作为内置 ACP（Agent Client Protocol）代理，ACP 模型列表由代理端动态提供而不再硬编码。端到端验证工具 verify-openhands 接入基于 DeepSeek 的 mock-LLM 行为对齐，并为浏览器环境补充了录屏和按键状态控制能力。

github · openhands-release-bot\[bot\] · 10月12日 15:06

**「设计要点」** 协议层解耦 ACP 代理与宿主，可用模型目录改由下游代理自行声明上报，无需平台端硬编码维护；评测框架通过 mock-LLM 驱动端到端行为映射，配合无头浏览器底层按键与录屏接口固化复现轨迹。

**「改了什么」** 本地后端内置 OpenCode 与 Pi 两种 ACP 代理并支持动态拉取模型列表；verify-openhands 增加 \`browser record\` 录屏与 \`browser key down\|up\|release-all\` 按键控制；自动化流程新增草稿持久化管理与分屏配置面板；agent-server 升级至 1.54.0。

**标签**: `#runtime`, `#subagents`, `#eval`, `#tools`

---

<a id="item-harness-arch-2"></a>
### [LangGraph checkpoint 4.3.0 发布](https://github.com/langchain-ai/langgraph/releases/tag/checkpoint%3D%3D4.3.0) ⭐️ 6.8/10

LangGraph 发布状态持久化子包 checkpoint 4.3.0，修复增量通道重放与反序列化容错。新版本规范了 delta 写入重放顺序，并在对象无法重建时保留原始序列化数据。同时放宽 Store 存储值类型至 Mapping\[str, Any\]，增强多存储后端的一致性校验。

github · github-actions\[bot\] · 10月12日 22:26

**「设计要点」** 增量通道重放改为按任务路径（task path）排序，恢复 exit 模式执行时按实时写入顺序重放 delta。状态分发前在 Postgres 与 SQLite 等后端统一校验命名空间标签。

**「改了什么」** InMemorySaver 增量历史默认对齐最新检查点，并在 CI 中补齐 delta 一致性套件。对象反序列化失败时不再丢弃原始数据，避免状态持久化静默损坏。

**标签**: `#runtime`, `#memory`, `#eval`

---

<a id="item-harness-arch-3"></a>
### [DSPy 3.4.1 发布](https://github.com/stanfordnlp/dspy/releases/tag/3.4.1) ⭐️ 5.5/10

DSPy 发布 3.4.1 版本，将 GEPA 优化器的默认指令提议器切换为结构化的 \`InstructionProposer\`，并允许 \`dspy.RLM\` 在 REPL 环境内通过 \`import dspy\` 构建子 Agent。新版本支持 Python 3.15，修复了 3.4.0 的导入崩溃与解释器问题。受反思请求结构调整和提示词变更影响，GEPA 优化结果可能与 3.4.0 不同，旧缓存也会失效。

github · isaacbmiller · 10月12日 23:12

**「设计要点」** RLM 的子 Agent 实际运行在宿主环境，仅通过 JSON 跨越解释器边界传输数据。\`max\_llm\_calls\` 统一统计主模型、批处理查询与所有子 Agent 的调用次数；沙盒代码无法修改 \`model\`、\`api\_base\` 等连接配置，只能传参温度等推理项。

**「改了什么」** GEPA 反思模型现强制要求为能够输出 JSON 的 \`dspy.LM\` 实例，非结构化文本输出会导致优化失败并保留原选方案。RLM 会为每条提示词追加子 Agent 说明段落，且保留 \`dspy\` 作为输入与工具命名关键字；\`dspy.ReActV2\` 签名不再允许声明名为 \`history\` 或 \`tools\` 的输入。

**标签**: `#subagents`, `#runtime`, `#planning`, `#eval`

---

<a id="item-harness-arch-4"></a>
### [Anthropic 开源 knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) ⭐️ 5.0/10

Anthropic 开源 knowledge-work-plugins 仓库。该项目主要面向 Claude Cowork 构建，同时兼容 Claude Code 运行时。插件用于定义岗位专属的工作流、指定工具与数据源接入规则，并通过斜杠命令扩展交互能力，将通用模型转变为特定岗位的专用 agent。

rss · GitHub Trending Daily · 10月13日 03:18

**「设计要点」** 插件打包封装数据调用路径、关键工作流规则与斜杠命令，向 Claude Cowork 和 Claude Code 暴露标准化的角色上下文与工具层定义。

**标签**: `#tools`, `#runtime`, `#planning`

---

## Agent 工程师日报
{: #sec-agent-engineer .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-agent-engineer" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-agent-engineer-1"></a>
### [Codex CLI 默认常驻守护进程引争议](https://github.com/openai/codex/issues/48195) ⭐️ 6.0/10

社区反馈 Codex CLI 默认在后台运行自更新守护进程，且文档未提供对应关闭说明。该进程在启动时向 \`~/.codex\` 写入 PID 与锁文件，有开发者反映其残留旧版本导致磁盘占用达 12 GB，且自动更新时会异常修改文件权限，甚至导致 \`.git\` 变为只读从而阻断任务执行。目前可通过在 \`~/.codex/config.toml\` 中配置 \`\[features\] daemon\_auto\_start = false\` 禁用自启。

hackernews · whimblepop · 10月12日 18:29 · [社区讨论](https://news.ycombinator.com/item?id=50060694)

**「为什么重要」** coding agent CLI 若隐式拉起常驻后台进程，可能在无人值守时擅自变更环境状态与仓库权限，直接威胁 harness 运行环境的确定性与执行稳定性。

**「可关注」** 可关注：检查本地及容器内的 Codex CLI 配置文件，按需关闭守护进程自启动，并排查 \`~/.codex\` 目录避免历史更新版本积压占用空间。

**「评论」** 开发者普遍对通过包管理器安装的 CLI 默认运行常驻自更新后台表示警惕，指责其权限问题频繁中断任务；部分用户转向依赖基础 Bash 的极简 harness 方案以降低外部依赖复杂度。

**标签**: `#coding-agent`, `#harness`, `#permissions`

---

<a id="item-agent-engineer-2"></a>
### [Anthropic 借鉴 Unix 哲学编排 Claude Agent](https://www.latent.space/p/claude-dynamic-workflows) ⭐️ 5.5/10

Anthropic 在 AI Engineer New York 峰会上介绍了动态工作流（Dynamic Workflows）设计。该思路借鉴 Unix 和 Linux 的系统哲学，试图通过多 Claude Agent 协同完成更复杂的工程项目，同时降低开发者的管理负担。目前公开信息集中在架构理念，尚未披露具体的实现代码与接口细节。

rss · Latent Space · 10月12日 18:18

**「可关注」** 可关注：编排框架转向类 Unix 的单一职责与组合管道模式，核心挑战仍在多 Agent 间上下文传递与状态边界的收敛。

**标签**: `#orchestration`, `#coding-agent`, `#harness`

---

<a id="item-agent-engineer-3"></a>
### [论文探讨长程终端 Agent 轨迹数据扩展](https://huggingface.co/papers/2610.13166) ⭐️ 5.5/10

Hugging Face Daily Papers 收录长程终端智能体数据扩展论文。论文指出短轨迹仅能展示命令与工具调用，难以覆盖探索积累证据、反馈调优及生成最终交付物的完整流程；同时指出现有环境合成容易预先简化关键操作，削弱了智能体的实际探索与验证需求。受限于公开摘要截断，具体合成方案与评测基线尚未披露完整细节。

rss · Hugging Face Daily Papers · 10月13日 00:00

**「为什么重要」** 长程终端任务依赖试错与反馈链条。若合成环境提前抹平复杂交互，训练出的模型难以应对真实终端环境下的不确定性与长链路排错。

**「可关注」** 可关注：构建终端训练数据时，评估环境初始化是否过度简化了探索与排错过程，防止削弱模型在多轮交互中的验证能力。

**标签**: `#coding-agent`, `#orchestration`, `#eval`

---

<a id="item-agent-engineer-4"></a>
### [研究揭示大模型禁思指令下的思考惯性](https://huggingface.co/papers/2610.11765) ⭐️ 5.5/10

论文研究大模型在被要求“不思考”时的行为表现。以往通过关闭思考模式或统计长轨迹来判定非思考状态的方法并不准，模型关闭思考模式后仍可能输出隐式推理，长轨迹也常混入填充 Token。作者将输出拆分为前置轨迹与最终答案，提出纯答案依从率（Empty-Thinking Rate）及问题与前置轨迹相关度等指标，定量评测模型对禁思指令的依从缺陷。

rss · Hugging Face Daily Papers · 10月13日 00:00

**「为什么重要」** 构建低延迟或低成本的 Agent harness 时，工程师常试图切断模型的长思考。这项研究表明仅靠配置或指令关停思考，未必能阻止模型产生额外的推理开销。

**「可关注」** 可关注：构建轻量分支路由或高频调用时，需在 harness 层直接校验模型是否产生非预期的前置轨迹 Token，不能单纯假设禁用思考配置即等于零额外开销。

**标签**: `#eval`, `#harness`, `#orchestration`

---

<a id="item-agent-engineer-5"></a>
### [Text-to-SQL 意图消歧基准 ARCS 提出](https://huggingface.co/papers/2610.09396) ⭐️ 5.5/10

论文针对 Text-to-SQL 落地中的用户意图歧义问题，提出结构化消歧（Structured Disambiguation）范式。该方法放弃低效的多轮自由对话澄清，转用显式、受限的交互消除模糊性，避免查询结果静默偏离真实目标。团队同步开源了基于真实数据库的意图消歧评测基准 ARCS（Ambiguity Resolution Corpus for SQL）。

rss · Hugging Face Daily Papers · 10月13日 00:00

**「为什么重要」** 开放式追问会打断用户工作流且交互成本高。用结构化交互代替自由文本澄清，为数据分析 Agent 的确认机制提供了更具可控性的实现路径。

**「可关注」** 可关注：构建 SQL 查询 Agent 时，将歧义澄清收拢为有限的结构化选项，比依赖模型自由发起追问更利于状态机收敛。

**标签**: `#eval`, `#orchestration`, `#harness`

---

<a id="item-agent-engineer-6"></a>
### [GUI Agent 经验检索仅在初始步骤有效](https://huggingface.co/papers/2609.33304) ⭐️ 5.5/10

论文《Relevance Does Not Imply Applicability》指出，现有个人 GUI Agent 将任务相关历史直接拼入上下文的做法存在局限。检索到的经验主要在首个决策步骤起效，后续 90% 的执行步骤收益极弱，也难以指导 Agent 何时应当给出主动建议。相关记录能标明起步位置，却无法映射到当前屏幕的具体动作。目前公开摘要在此截断，具体机制与完整方案仍待披露。

rss · Hugging Face Daily Papers · 10月13日 00:00

**「为什么重要」** 常见 Memory 方案默认「任务相关即全程可用」。该研究揭示了经验相关性与单步适用性之间的断层，直接挑战了把整条历史轨迹全量塞入上下文的 Harness 习惯。

**「可关注」** 可关注：构建 GUI Agent 记忆体系时，需解耦任务级检索与屏幕状态级的动作激活，单靠开局检索无法支撑连续的多步决策。

**标签**: `#memory`, `#harness`, `#orchestration`

---

<a id="item-agent-engineer-7"></a>
### [Decision 3.0 多模态决策模型开源](https://www.reddit.com/r/LocalLLaMA/comments/1x3th4p/decision_30_open_multimodal_decision_models_from/) ⭐️ 5.5/10

vLLM Semantic Router 团队发布 Decision 3.0 模型家族（涵盖 0.6B 至 27B，采用 Apache-2.0 协议），基于 Qwen 架构构建并内置视觉编码器，支持文本、多图与视频输入。该系列完全跳过文本自回归生成，直接输出单选、是非与打分类型的概率分布，支持单次调用内针对同一输入并行判定多个问题。团队使用 Jev 0.3 评测套件测试，称 27B 版本在文本与视觉榜单均位列第一，且视频任务在未参与训练的情况下以 zero-shot 运行。

reddit · r/LocalLLaMA · /u/henzy123 · 10月12日 05:26

**「为什么重要」** 面向 Agent 路由与多模态分发场景，免生成、直接出分类概率的设计消除了文本后处理与解析出错的风险，显式压缩了决策延迟。

**「可关注」** 可关注：利用此类免生成概率模型替换 Agent 流程中的前置语义路由、内容审核与轻量级分支判断节点。

**标签**: `#orchestration`, `#eval`, `#harness`

---

## AI 日报
{: #sec-ai-daily .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-daily" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-daily-1"></a>
### [GitHub 发布 Copilot 代码库配置指南](https://github.blog/ai-and-ml/github-copilot/github-copilot-app-for-beginners-how-to-teach-copilot-about-your-codebase/) ⭐️ 5.3/10

GitHub 博客发布 Copilot 初学者指南。文章介绍如何向代码仓库添加自定义指令与技能，配置自定义 Agent。开发者也可以接入 Playwright 等 MCP 服务，让 Copilot 获取具体项目的上下文与交互能力。

rss · GitHub Blog · 10月12日 17:43

**「为什么重要」** 通过自定义指令和 MCP 协议扩展上下文，正在成为主流代码助手对齐项目环境的标准配置路径。

**「可关注」** 可关注：通过接入 Playwright 等 MCP 服务，可直接扩展 Copilot 对本地代码库的测试与执行能力。

**标签**: `#product`, `#industry`

---