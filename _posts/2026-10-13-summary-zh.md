---
layout: default
title: "Horizon Summary: 2026-10-13 (ZH)"
date: 2026-10-13
lang: zh
---

> 从 200 条内容中筛选出 10 条重要资讯。

<nav id="ah-toc" class="ah-toc" aria-label="目录"><span class="ah-toc-title">目录</span><ul><li><a href="#sec-harness-arch"><span class="ah-toc-name">Harness 架构</span><span class="ah-toc-count">4条</span></a></li><li><a href="#sec-agent-engineer"><span class="ah-toc-name">Agent 工程师日报</span><span class="ah-toc-count">5条</span></a></li><li><a href="#sec-ai-daily"><span class="ah-toc-name">AI 日报</span><span class="ah-toc-count">1条</span></a></li></ul></nav>

---

**[Harness 架构](#sec-harness-arch)**
1. [OpenHands v1.27.0 发布](#item-harness-arch-1) ⭐️ 7.8/10
2. [LangGraph checkpoint 4.3.0 发布](#item-harness-arch-2) ⭐️ 6.8/10
3. [DSPy 3.4.1 发布](#item-harness-arch-3) ⭐️ 5.5/10
4. [Anthropic 开源知识工作插件集](#item-harness-arch-4) ⭐️ 5.5/10

**[Agent 工程师日报](#sec-agent-engineer)**
1. [Codex CLI 默认常驻后台自更新进程](#item-agent-engineer-1) ⭐️ 6.5/10
2. [面向长程终端智能体的数据缩放研究](#item-agent-engineer-2) ⭐️ 6.0/10
3. [论文揭示 LLM 禁用思考时的思考惯性](#item-agent-engineer-3) ⭐️ 5.8/10
4. [ARCS 提出结构化澄清 Text-to-SQL 歧义](#item-agent-engineer-4) ⭐️ 5.5/10
5. [GUI Agent 经验检索面临首步后失效问题](#item-agent-engineer-5) ⭐️ 5.5/10

**[AI 日报](#sec-ai-daily)**
1. [GitHub 发布 Copilot 代码库适配入门指南](#item-ai-daily-1) ⭐️ 5.3/10

---

## Harness 架构
{: #sec-harness-arch .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-harness-arch" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-harness-arch-1"></a>
### [OpenHands v1.27.0 发布](https://github.com/OpenHands/OpenHands/releases/tag/v1.27.0) ⭐️ 7.8/10

OpenHands 发布 v1.27.0。本地后端新增 OpenCode 与 Pi 作为内置 ACP 智能体，并将 ACP 模型列表调整为由 agent 端动态提供。测试框架补充 DeepSeek 场景的 mock-LLM 端到端校验，同时为浏览器工具链增加了视频录制与按键状态控制命令。

github · openhands-release-bot\[bot\] · 10月12日 15:06

**「设计要点」** ACP 协议层废除硬编码模型列表，改为直接向智能体查询可用模型；端到端测试链路完善 mock-LLM 轨迹持久化，降低多模型适配回归成本。

**「改了什么」** 本地后端直接集成 OpenCode 与 Pi 智能体；测试工具链引入 browser record 录屏与 browser key 组合按键控制；Agent Canvas 接入 DigitalOcean Managed Agents。

**标签**: `#eval`, `#subagents`, `#runtime`, `#tools`

---

<a id="item-harness-arch-2"></a>
### [LangGraph checkpoint 4.3.0 发布](https://github.com/langchain-ai/langgraph/releases/tag/checkpoint%3D%3D4.3.0) ⭐️ 6.8/10

LangGraph 发布 checkpoint 4.3.0 版本。本次更新修正断点恢复时的增量（delta）写入与回放顺序，完善存储命名空间校验，并增强反序列化失败时的容错机制。

github · github-actions\[bot\] · 10月12日 22:26

**「设计要点」** 恢复 exit-mode 运行时代入 live 顺序回放增量写入，通道回放依据 task path 严格排序。反序列化遇阻时保留原始序列化数据，防止状态损毁。

**「改了什么」** InMemorySaver 增量历史默认指向最新检查点并在 CI 接入一致性测试。Postgres 与 SQLite 模块在分发前校验 namespace 标签，同时将 Store.put 值类型放宽至 Mapping\[str, Any\]。

**标签**: `#runtime`, `#memory`

---

<a id="item-harness-arch-3"></a>
### [DSPy 3.4.1 发布](https://github.com/stanfordnlp/dspy/releases/tag/3.4.1) ⭐️ 5.5/10

DSPy 发布 3.4.1 版本，允许 dspy.RLM 在 REPL 运行的代码中构建子 Agent，并将子调用统一计入总预算。优化器 GEPA 将结构化 InstructionProposer 设为默认提案器，并支持 Python 3.15。新版本引入了破坏性变更：ReActV2 禁止输入字段命名为 history 或 tools，GEPA 优化结果不再与 3.4.0 保持一致。

github · isaacbmiller · 10月12日 23:12

**「设计要点」** RLM 沙箱内的子 Agent（包括 Predict、ChainOfThought、ReActV2 及嵌套 RLM）实际在宿主环境构建并运行，跨解释器边界仅传递 JSON。沙箱代码禁止篡改 model、api\_key 与 headers，且 max\_llm\_calls 预算强制跨主从 Agent 统一扣减。

**「改了什么」** GEPA 默认通过 JSONAdapter 配合 dspy.Predict 提议指令，反射 LM 必须返回标准 JSON，否则优化直接失败；dspy.ReActV2 签名明确封禁 history 与 tools 变量名；在 3.4.0 中以 null Score 保存的模型文件在新版不再支持加载。

**标签**: `#subagents`, `#runtime`, `#tools`

---

<a id="item-harness-arch-4"></a>
### [Anthropic 开源知识工作插件集](https://github.com/anthropics/knowledge-work-plugins) ⭐️ 5.5/10

Anthropic 开源知识工作插件仓库 anthropics/knowledge-work-plugins。项目针对特定角色与团队定制工具链及业务流，原生适配 Claude Cowork，并兼容 Claude Code。

rss · GitHub Trending Daily · 10月13日 03:42

**「设计要点」** 插件包封装了外部工具接入、数据源拉取规则与斜杠命令规范，约束 agent 在垂直业务场景中的执行动作与输出规格。

**标签**: `#tools`, `#planning`, `#subagents`

---

## Agent 工程师日报
{: #sec-agent-engineer .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-agent-engineer" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-agent-engineer-1"></a>
### [Codex CLI 默认常驻后台自更新进程](https://github.com/openai/codex/issues/48195) ⭐️ 6.5/10

社区反馈 Codex CLI 默认启动常驻且自更新的后台守护进程，且未提供正式的停用文档。用户排查发现该进程会堆积旧版本二进制文件，导致磁盘占用达到 12 GB，并在自更新时偶发损坏本地文件权限，致使 \`.git\` 目录变成只读并中断任务。目前可通过在 \`~/.codex/config.toml\` 中添加 \`daemon\_auto\_start = false\` 禁用自动启动。

hackernews · whimblepop · 10月12日 18:29 · [社区讨论](https://news.ycombinator.com/item?id=50060694)

**「为什么重要」** CLI harness 引入隐蔽的常驻自更新机制会打破本地环境的确定性。守护进程在运行期修改文件系统与权限，会直接造成长期运行的 agent 任务意外中断。

**「可关注」** 可关注：检查运行环境中的常驻进程与磁盘占用，在 \`~/.codex/config.toml\` 中显式配置 \`daemon\_auto\_start = false\`，防止后台自动更新损坏 \`.git\` 权限。

**「评论」** 开发者对 harness 过度设计与偶发 bug 表示不满，有人选择转向仅依赖 Bash 的轻量化方案。也有用户指出 Claude Code 同样存在后台运行常驻进程并在本地保留历史版本的行为。

**标签**: `#coding-agent`, `#harness`, `#permissions`

---

<a id="item-agent-engineer-2"></a>
### [面向长程终端智能体的数据缩放研究](https://huggingface.co/papers/2610.13166) ⭐️ 6.0/10

论文探讨长程终端智能体的数据构建难题。短轨迹仅能演示命令与工具调用，无法体现多轮探索积累证据、基于反馈调整策略的长程行为。现有环境合成往往预先代劳或简化关键步骤，削弱了智能体实际需要的探索与验证过程；当前公开摘要在具体技术方案处截断，未包含基准测试细节。

rss · Hugging Face Daily Papers · 10月13日 00:00

**「为什么重要」** 终端智能体走向长程任务，核心在于自纠错与策略调整。若合成环境提前替模型抹平探索与验证难度，生成的长轨迹将失去训练价值。

**「可关注」** 可关注：合成长程任务轨迹时，需警惕环境预置逻辑过度简化排错与验证链路，避免产出缺乏真实探索密度的无效数据。

**标签**: `#coding-agent`, `#orchestration`, `#eval`, `#harness`

---

<a id="item-agent-engineer-3"></a>
### [论文揭示 LLM 禁用思考时的思考惯性](https://huggingface.co/papers/2610.11765) ⭐️ 5.8/10

论文研究了大模型在收到禁止思考指令时的遵从表现。研究指出，仅看是否关闭思考模式或输出是否包含长轨迹并不可靠，模型在关闭思考模式后仍常生成隐藏推理痕迹。作者将模型回答标准化为前置轨迹与最终答案，提出严格不思考率（Empty-Thinking Rate）及问题与前置轨迹相关度等多维度指标，量化评估模型的思考惯性。

rss · Hugging Face Daily Papers · 10月13日 00:00

**「为什么重要」** 部分 Agent 调度框架依赖动态切换思考模式来压缩 Token 成本与响应延迟。该研究表明关闭开关不等于停止推理，为工程端评估无思考模式的真实执行开销提供了量化指标。

**「可关注」** 可关注：构建动态思考的 Agent harness 时，检验模型是否真正跳过推理需核查前置轨迹与问题相关度，不能单看接口返回的思考开关状态或输出长度。

**标签**: `#eval`, `#harness`, `#orchestration`

---

<a id="item-agent-engineer-4"></a>
### [ARCS 提出结构化澄清 Text-to-SQL 歧义](https://huggingface.co/papers/2610.09396) ⭐️ 5.5/10

论文提出结构化消歧（Structured Disambiguation）机制，用受约束的显式交互代替多轮自由对话，解决 Text-to-SQL 场景中隐蔽的数据与领域歧义。团队同步构建了评测基准 ARCS（Ambiguity Resolution Corpus for SQL），覆盖真实数据库中自然发生的用户意图模糊问题。目前公开材料仅披露了基准构建理念，具体交互协议与工程实现细节尚未完整公开。

rss · Hugging Face Daily Papers · 10月13日 00:00

**「为什么重要」** 自由多轮对话消歧常增加用户的认知负担且容易引入新歧义。将消歧动作约束为结构化表单或离散选项，为数据库查询 Agent 提供了更可控的人机交互路径。

**「可关注」** 设计 SQL 生成或工具调用 Agent 时，可关注将意图澄清收敛为固定 Schema 的选择题或表单，替代无边界的自然语言多轮追问。

**标签**: `#eval`, `#orchestration`, `#coding-agent`

---

<a id="item-agent-engineer-5"></a>
### [GUI Agent 经验检索面临首步后失效问题](https://huggingface.co/papers/2609.33304) ⭐️ 5.5/10

论文《Relevance Does Not Imply Applicability》指出，个人 GUI Agent 依赖任务相关历史经验时存在明显衰减。检索到的交互历史能显著改善开局第一步决策，但在剩余 90% 的执行步骤中几乎没有持续收益，且难以辅助判断是否应当触发主动建议。相关记录能指示任务从何开始，却无法有效指导当前屏幕状态下的具体操作动作。

rss · Hugging Face Daily Papers · 10月13日 00:00

**「为什么重要」** 主流 Agent 记忆设计通常默认“检索相关即可全局套用”。该研究揭示了把任务级相关经验直接拼入长上下文的缺陷，表明记忆检索机制需要从静态任务相关转向按步骤动态判断适用性。

**「可关注」** 可关注：构建多步 GUI 任务 harness 时，避免仅在入口处一次性追加检索历史，需测试按当前界面状态动态激活具体动作经验的分步调度方案。

**标签**: `#memory`, `#harness`, `#orchestration`

---

## AI 日报
{: #sec-ai-daily .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-daily" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-daily-1"></a>
### [GitHub 发布 Copilot 代码库适配入门指南](https://github.blog/ai-and-ml/github-copilot/github-copilot-app-for-beginners-how-to-teach-copilot-about-your-codebase/) ⭐️ 5.3/10

GitHub 官方博客发布面向初学者的指南，讲解如何让 Copilot 理解特定代码库。内容涵盖为仓库添加自定义指令与技能、使用自定义 Agent，以及接入 Playwright 等 MCP 服务器。

rss · GitHub Blog · 10月12日 17:43

**「可关注」** 可关注：官方示例将 MCP 服务器（如 Playwright）与代码库级自定义指令结合，用于为 Agent 补全上下文与执行环境。

**标签**: `#product`, `#industry`

---