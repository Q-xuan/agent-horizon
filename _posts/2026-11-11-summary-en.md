---
layout: default
title: "Horizon Summary: 2026-11-11 (EN)"
date: 2026-11-11
lang: en
---

> From 207 items, 18 important content pieces were selected

---

**Agent Harness Architecture**
1. [Goose v1.59.0 发布](#item-harness-arch-1) ⭐️ 7.8/10
2. [pydantic-ai v2.67.0 发布](#item-harness-arch-2) ⭐️ 7.8/10
3. [DSPy 3.5.0 发布](#item-harness-arch-3) ⭐️ 7.8/10
4. [Anthropic Agent Skills 实现公开](#item-harness-arch-4) ⭐️ 6.0/10
5. [Cursor Projects 多人协作上线](#item-harness-arch-5) ⭐️ 5.8/10

**AI Agent Engineer**
1. [Gemini 4 Carbon 正式发布可用](#item-agent-engineer-1) ⭐️ 7.8/10
2. [AlphaProof Code 发布](#item-agent-engineer-2) ⭐️ 7.0/10
3. [Meta Muse Ember 1.0 发布](#item-agent-engineer-3) ⭐️ 7.0/10
4. [ReproBridge 可复现 ML 工作流](#item-agent-engineer-4) ⭐️ 7.0/10
5. [llm-gemini 0.36 发布 支持 Gemini 4 Carbon](#item-agent-engineer-5) ⭐️ 6.0/10
6. [Sage-Taiyi 元认知架构发布](#item-agent-engineer-6) ⭐️ 6.0/10

**AI Daily**
1. [OpenAI 推出 Businesses in ChatGPT](#item-ai-daily-1) ⭐️ 7.8/10
2. [OpenAI ThinkYoung 研究聚焦教育指导](#item-ai-daily-2) ⭐️ 7.8/10
3. [OpenAI Upwork 研究：AI 改变自由职业市场](#item-ai-daily-3) ⭐️ 7.8/10
4. [OpenAI 博客发布 Gilbert + Tobin AI 转型访谈](#item-ai-daily-4) ⭐️ 6.8/10
5. [OpenAI 推出护理人员免费 ChatGPT 培训](#item-ai-daily-5) ⭐️ 6.8/10
6. [Git 2.56.1 修复6个安全漏洞](#item-ai-daily-6) ⭐️ 6.8/10

**AI Deals**
1. [小渔排班永久免费](#item-ai-deals-1) ⭐️ 8.0/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [Goose v1.59.0 发布](https://github.com/aaif-goose/goose/releases/tag/v1.59.0) ⭐️ 7.8/10

Goose v1.59.0 发布，新增延迟 MCP 工具执行、子代理恢复、Agent 钩子控制及会话管理改进。ToolExecutionOperation 支持最小化延迟 MCP 工具，goose-agent \(GDK\) 新增 stop、approval 和 tool 钩子操作。子代理可通过 follow-up 恢复已完成的 delegate，会话列表支持按 client tags 过滤（ACP）。同时修复 Databricks OAuth 令牌刷新、Gemini thinking level 发送及 cargo-deny advisory 等问题。

github · github-actions\[bot\] · Nov 10, 17:17

**「设计要点」** ToolExecutionOperation 引入延迟 MCP 工具执行路径，goose-agent \(GDK\) 扩展 stop、approval、tool 钩子接口。会话层增加 client tag 过滤（ACP）并将数据库初始化与应用程序池隔离。

**「改了什么」** 新增延迟 MCP 工具执行、子代理 follow-up 恢复、Agent 控制钩子及会话 client tag 过滤。修复 Databricks OAuth 令牌过期刷新、Gemini 参数修正及 cargo-deny zip8 advisory。

**「评论」** 无社区评论。

**Tags**: `#MCP`, `#subagent`, `#tool-execution`, `#session-management`, `#release`

---

<a id="item-harness-arch-2"></a>
### [pydantic-ai v2.67.0 发布](https://github.com/pydantic/pydantic-ai/releases/tag/v2.67.0) ⭐️ 7.8/10

pydantic-ai v2.67.0 正式发布。持久执行层新增动态子代理支持（\`SubAgents\(dynamic\_agents=...\)\`），\`RepoContext\` 默认递归加载目录内嵌套指令文件并新增 \`walk\_up\` 参数，内联指令上限设为每对话 32,000 字符。\`ArtifactScanner\` 在匹配前剥离默认可忽略字符并标记隐藏变体选择器。文档工具支持标准库 \`mimetypes\` 全部已知类型，格式由库自动推断。

github · dsfaccini · Nov 10, 23:11

**「设计要点」** 持久执行层新增动态子代理与 DBOS 子工作流并行执行能力，guardrail 判定作为持久操作记录。\`CodeMode\` 远程沙箱通过 gRPC 运行，\`Workspace.authority\_of\` 提供按路径权限控制，\`RepoContext\` 嵌套指令加载机制改变上下文构建策略。

**「改了什么」** 相对上一版，v2.67.0 在 durable execution 与 Temporal/DBOS 中支持动态子代理与任务控制，\`RepoContext\` 改为默认递归加载目录指令并增加 32,000 字符上限，\`ArtifactScanner\` 调整文本归一化逻辑，provider 原生工具配置迁移至 \`provider\_settings\` 且文档工具支持全部 mimetype。

**「评论」** 无社区评论可用。

**Tags**: `#runtime`, `#subagents`, `#memory`, `#tools`, `#sandbox`

---

<a id="item-harness-arch-3"></a>
### [DSPy 3.5.0 发布](https://github.com/stanfordnlp/dspy/releases/tag/3.5.0) ⭐️ 7.8/10

DSPy 3.5.0 发布，核心变更包括 ReActV2 取代 ReAct、RLM/Flex/GEPA 毕业、富工具结果与 RLM 历史持久化。底层 LM 层替换为轻量级 lm15 引擎，LiteLLM 与 OpenAI 库变为可选依赖，默认安装体积从 206.7 MiB 降至 30.9 MiB，依赖数从 65 减至 25。XMLAdapter 成为默认适配器，model\_type=&quot;auto&quot; 成为默认路由，磁盘缓存默认受限加载且禁用 pickle，仅存储纯 NumPy 数组。该版本变更提示、默认值与 API，存在破坏性更新。

github · isaacbmiller · Nov 10, 16:25

**「设计要点」** RLM 与 Flex 解释器内嵌真实 DSPy 运行时，通过 InterpreterPool 预热解释器，缓存 Deno 启动快照，使首次执行延迟从 1.59 s 降至 0.45 s，池化转发延迟低至 0.10 s。工具接口支持返回图片、文件等 DSPy 内容部件，历史记录结构化保存工具调用 ID 与错误状态。

**「改了什么」** ReActV2 成为默认 dspy.ReAct，提供结构化 History 与类型化 submit 工具，旧名称在 3.6 前弃用。RLM 新增 History 持久化（不恢复实时解释器变量）、图像裁剪与混合文本/图像子查询能力，Flex 与 RLM 解释器支持 InterpreterPool 预热。

**Tags**: `#runtime`, `#tools`, `#memory`, `#planning`

---

<a id="item-harness-arch-4"></a>
### [Anthropic Agent Skills 实现公开](https://github.com/anthropics/skills) ⭐️ 6.0/10

Anthropic has publicly released its implementation of the Agent Skills standard via the \`anthropics/skills\` repository. The system provides dynamic loading of reusable task-specific resource packages—folders containing instructions, scripts, and tools—to improve Claude&\#x27;s performance on specialized tasks. Skills enable repeatable workflows such as generating brand-compliant documents or analyzing data with organizational tools. The Agent Skills standard is separately documented at agentskills.io.

rss · GitHub Trending Daily · Nov 11, 03:12

**Tags**: `#tools`, `#runtime`

---

<a id="item-harness-arch-5"></a>
### [Cursor Projects 多人协作上线](https://cursor.com/blog/projects-multiplayer) ⭐️ 5.8/10

Cursor 于 2026-11-10 将 Projects 多智能体工作区升级为多人协作模式，向所有用户开放 beta。团队可在同一 workspace 中与智能体 fleet 共享上下文、记忆、文档和任务面板，共同规划与交付。每个成员仍保留与 coordinator 及 worker agents 的一对一本地上下文，同时叠加共享层存储需求文档、图表和规格。跨成员智能体通过 coordinator 实时同步任务顺序，避免后期冲突。

rss · Cursor Blog · Nov 10, 12:00

**「改了什么」** Projects 从支持单人多智能体调度扩展为团队 multiplayer workspace，新增共享上下文层、共享任务面板、跨成员智能体通信与协调能力。新成员加入时自动继承项目上下文，无需重复搭建。

**Tags**: `#memory`, `#subagents`, `#planning`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [Gemini 4 Carbon 正式发布可用](https://deepmind.google/blog/gemini-4-carbon-is-now-available/) ⭐️ 7.8/10

2026年11月10日，Google DeepMind 官方宣布 Gemini 4 Carbon 模型正式可用，这是该领先AI实验室发布的新版本。该模型面向AI agent工程师，可用于编码智能体、harness 及评估工作流的底层模型选型。当前官方公告未包含该模型的具体技术性能指标、能力细节，也未提供与先前Gemini版本的对比基准。

rss · Google DeepMind · Nov 10, 16:03

**「为什么重要」** 作为领先AI实验室发布的新模型，其前序Gemini系列已被广泛用于智能体开发，此次发布为工程师提供了新的底层模型评估候选。目前官方材料尚未证实该模型相比现有Gemini版本的实际性能与能力提升。

**「可关注」** 可关注：官方当前未披露 Gemini 4 Carbon 与先前Gemini版本的性能对比基准及具体能力细节，相关评估工作需等待更多技术信息公布。

**Tags**: `#harness`, `#coding-agent`, `#eval`

---

<a id="item-agent-engineer-2"></a>
### [AlphaProof Code 发布](https://deepmind.google/blog/introducing-alphaproof-code/) ⭐️ 7.0/10

DeepMind 于 2026-11-10 发布 AlphaProof Code，一个面向形式化代码验证的 AI proof agent。该工具在代码库上迭代，编写并运行 Lean 或 Rocq 证明，操作模式与经典 coding agent 相似。社区指出其可能仅验证狭窄定理，且 AI 生成的证明存在错误风险；当前材料缺少原始博客中的完整技术规格、性能基准与详细架构。

hackernews · Google DeepMind · Nov 10, 12:11 · [Discussion](https://news.ycombinator.com/item?id=50439193)

**「为什么重要」** 形式化验证正从学术走向工程实践，但 AI 生成证明的可信度仍需独立审计。若该工具仅证明实现而非规范，则对代码正确性的提升范围有限。

**「可关注」** 可关注：AI 生成证明代码的可信度与人工审查成本。

**「评论」** 社区对“零 bug”结论持怀疑态度，认为可能仅验证了狭窄属性或定理定义有误。部分用户指出其工作流与现有 coding agent 高度相似，并提醒 AI 生成的 Lean 代码可能“作弊”，需对抗性审查。

**Tags**: `#coding-agent`, `#eval`

---

<a id="item-agent-engineer-3"></a>
### [Meta Muse Ember 1.0 发布](https://simonwillison.net/2026/Nov/10/muse-ember/) ⭐️ 7.0/10

据Simon Willison 2026年11月10日发布的博客，Meta AI正式推出Muse Ember 1.0小型高效模型，定位面向智能体高频重复工作，支持工具调用、编码子任务、路由、信息提取、长文档解析等场景，上下文长度支持1M token，提供minimal、low、medium、high、xhigh、max共6档推理等级。短提示（≤200k输入token）场景下，输入定价$0.10/百万token、缓存输入$0.004/百万token、输出$0.50/百万token，与GPT-6 Luna、Claude Haiku 5.5持平；超过200k输入token后，输入涨至$0.30/百万token、缓存输入$0.012/百万token、输出$1.50/百万token，长上下文下定价介于前两者之间。Artificial Analysis的效率前沿（Pareto线）数据显示，Muse Ember的xhigh、max推理等级处于该线，同 Intelligence Index 下每任务成本低于Claude Haiku 5.5 xhigh版本。实测其6档推理等级的输出质量无严格线性对应，high推理等级未返回完整SVG。

rss · Simon Willison · Nov 10, 07:28

**「为什么重要」** 当前coding agent及 orchestration 场景对低成本、强工具调用能力的模型需求明确，Muse Ember在短上下文下定价与同级别模型持平，长上下文下成本优势更突出，且处于效率前沿，为成本敏感型的agent场景提供了新的选型参考。

**「可关注」** 可关注Muse Ember在工具调用、编码子任务等agent高频场景的实际推理质量与成本表现，以及长上下文（&gt;200k token）下的真实性价比，对比现有选型的适配性。

**Tags**: `#coding-agent`, `#orchestration`

---

<a id="item-agent-engineer-4"></a>
### [ReproBridge 可复现 ML 工作流](https://huggingface.co/papers/2611.08452) ⭐️ 7.0/10

Hugging Face Daily Papers 于 2026-11-11 介绍 ReproBridge，一个将精炼代码库、环境配置、实验启动器和复现指南打包为标准化 artifacts 的 agent workflow。配套的 ReproBridge-Bench 包含 1,029 个任务，覆盖 36 篇论文的 387 个实验，每个任务附带 5 个人工验证的参考分数。该基准用于评估 coding agent 独立复现 ML 实验的能力，但当前材料内容截断，未披露具体 agent 性能对比数据。

rss · Hugging Face Daily Papers · Nov 11, 03:12

**「为什么重要」** ML 实验复现长期依赖人工填补论文与代码间的细节缺口，ReproBridge 试图通过标准化 artifacts 降低这一摩擦。Benchmark 的发布为 coding agent 评估提供了可复用的任务集与验证基线，但尚未有公开性能数据证明其区分度。

**「可关注」** 可关注：ReproBridge-Bench 的 1,029 个任务及人工验证参考分数可作为 coding agent 复现能力的评估基线，但需等待具体 agent 性能数据以确认任务区分度。

**Tags**: `#eval`, `#coding-agent`, `#harness`

---

<a id="item-agent-engineer-5"></a>
### [llm-gemini 0.36 发布 支持 Gemini 4 Carbon](https://simonwillison.net/2026/Nov/10/llm-gemini/) ⭐️ 6.0/10

2026年11月10日，Simon Willison 发布 llm-gemini 0.36，该版本为窄插件更新，无架构变更、性能基准或 eval 突破。新增对两周前宣布、刚全量开放的 Gemini 4 Carbon 的支持，该模型 launch 定价为每百万输入 token 2 美元、输出 10 美元，与 GPT-6.1 Sol、Claude Sonnet 5.5 同价，12 月 1 日将翻倍至 4/20 美元，与 Opus 5.5 同价。同时新增可配置的思维努力（thinking effort）参数，默认中等。该更新影响使用 llm-gemini 调用 Gemini 系列模型的开发者。

rss · Simon Willison · Nov 10, 20:09

**「为什么重要」** 该版本让 llm-gemini 用户可立即接入刚全量开放的 Gemini 4 Carbon，可配置的思维努力参数也提供了输出精细度控制选项。但该模型的临时定价意味着 12 月 1 日后的调用成本存在明确变化预期，实际影响尚未完全显现。

**「可关注」** 可关注 llm-gemini 0.36 对 Gemini 4 Carbon 的接入情况，若计划长期使用该模型，可提前评估 12 月 1 日定价调整后的调用成本。

**Tags**: `#coding-agent`, `#harness`

---

<a id="item-agent-engineer-6"></a>
### [Sage-Taiyi 元认知架构发布](https://huggingface.co/papers/2611.12762) ⭐️ 6.0/10

Sage-Taiyi 采用元认知架构，2026-11-11 出现在 Hugging Face Daily Papers。该架构通过显式监控与调控，动态修订对证据、假设和未解问题的理解，并据此调整研究目标与推理方法选择。在 Taiyi-Bench（265 个跨 10 学科任务）上，Sage-Taiyi 在全部八项历史复现与开放 ideation 指标上排名第一，Overall 得分 54.0，对比 AI Scientist-v2 基线的 47.9。当前材料为截断摘要，未披露实现细节、外部基准具体得分或复现步骤。

rss · Hugging Face Daily Papers · Nov 11, 03:12

**「为什么重要」** 该工作展示了元认知监控在 Agent orchestration 与记忆设计中的潜在应用，但领域局限于科学发现，且材料不完整，对通用 Agent 工程的直接适用性尚未证实。

**「可关注」** 可关注：显式监控证据与假设修订机制，对需要长期规划与自我修正的 Agent 系统有设计参考价值。

**Tags**: `#eval`, `#orchestration`, `#memory`

---

## AI Daily

<a id="item-ai-daily-1"></a>
### [OpenAI 推出 Businesses in ChatGPT](https://openai.com/index/introducing-businesses-chatgpt) ⭐️ 7.8/10

OpenAI 于 2026 年 11 月 10 日推出 Businesses in ChatGPT 功能。该功能允许企业在 ChatGPT 中管理业务信息、查看业务展示数据，并将用户兴趣转化为行动。目前官方未披露具体技术实现细节与上线范围。

rss · OpenAI Blog · Nov 10, 10:00

**「为什么重要」** 这是 OpenAI 首次为企业提供在 ChatGPT 对话界面中管理信息、查看展示数据并转化用户兴趣的官方功能，标志着平台向商业生态扩展。

**「可关注」** 可关注：Businesses in ChatGPT 目前仅开放信息管理与展示数据查看功能，转化链路的具体实现方式尚未公开。

**Tags**: `#product`, `#industry`, `#lab`

---

<a id="item-ai-daily-2"></a>
### [OpenAI ThinkYoung 研究聚焦教育指导](https://openai.com/index/closing-ai-guidance-gap-education) ⭐️ 7.8/10

OpenAI 发布博客文章，介绍 ThinkYoung 最新研究及 EMEA 教育合作项目经验。文章聚焦教师支持、AI 素养提升与独立学习三个方向。未披露具体合作规模或量化数据。

rss · OpenAI Blog · Nov 10, 09:00

**「可关注」** 可关注：ThinkYoung 研究及 EMEA 合作聚焦教师支持、AI 素养与独立学习。

**Tags**: `#lab`, `#industry`, `#policy`

---

<a id="item-ai-daily-3"></a>
### [OpenAI Upwork 研究：AI 改变自由职业市场](https://openai.com/index/ai-effect-on-freelance-work) ⭐️ 7.8/10

OpenAI 与 Upwork 联合发布最新研究，显示 AI 正在推动自由职业市场需求转移与新技能组合涌现。AI 相关项目的预算和工时均呈现增长，但研究未披露具体统计数字或样本量。该结果基于双方平台数据，反映了 AI 对自由职业市场的实际影响。

rss · OpenAI Blog · Nov 10, 07:00

**「为什么重要」** 这项联合研究提供了 AI 影响自由职业市场的实证数据，有助于理解 AI 时代技能需求的演变方向。

**「可关注」** AI 相关自由职业项目预算与工时同步增长，新技能组合正在形成。

**Tags**: `#lab`, `#industry`, `#research`

---

<a id="item-ai-daily-4"></a>
### [OpenAI 博客发布 Gilbert + Tobin AI 转型访谈](https://openai.com/index/gilbert-tobin-sam-nickless) ⭐️ 6.8/10

OpenAI 官方博客于 2026 年 11 月 12 日发布对 Gilbert + Tobin 律师事务所 CEO Sam Nickless 的访谈，讨论该律所通过 AI 进行业务转型的实践。这是一则客户成功案例，未发布新模型、政策或产品。报道未披露具体技术指标、性能数据或实施细节。

rss · OpenAI Blog · Nov 12, 00:00

**Tags**: `#industry`, `#lab`, `#product`

---

<a id="item-ai-daily-5"></a>
### [OpenAI 推出护理人员免费 ChatGPT 培训](https://openai.com/index/helping-caregivers-use-ai-in-everyday-life) ⭐️ 6.8/10

OpenAI 通过 OpenAI Academy 项目，正在美国 5 个城市面向护理人员推出免费 ChatGPT 实操培训，帮助其掌握日常实用的 AI 技能。

rss · OpenAI Blog · Nov 10, 12:00

**「为什么重要」** 这是 OpenAI 将 AI 工具普及向非技术垂直人群的尝试，把 AI 能力落地到日常照护场景，有望降低护理人员群体的 AI 使用门槛。

**「可关注」** 可关注：面向特定垂直人群的 AI 工具落地培训模式，可积累细分场景下的真实使用需求反馈。

**Tags**: `#lab`, `#product`, `#industry`

---

<a id="item-ai-daily-6"></a>
### [Git 2.56.1 修复6个安全漏洞](https://github.blog/open-source/git/git-security-vulnerabilities-announced-7/) ⭐️ 6.8/10

Git项目官方发布Git 2.56.1及2.55.1、2.54.1、2.53.1、2.52.1、2.51.3、2.50.2共7个版本的安全补丁，修复6个安全漏洞。漏洞覆盖递归克隆任意代码执行、路径遍历、内存损坏等高危风险，涉及CVE-2026-111760等6个编号。官方建议所有用户及捆绑Git的应用尽快升级至修复版本。

rss · GitHub Blog · Nov 10, 18:00

**「为什么重要」** 所有使用Git进行代码克隆、合并、托管操作的AI开发场景均可能受这些漏洞影响，GitHub已在其云服务、Codespaces、Actions等平台完成修复部署，升级可规避远程代码执行等高风险威胁。

**「可关注」** 可关注：升级至Git 2.56.1或对应维护分支的补丁版本，同时更新捆绑Git的第三方应用；处理不可信git fast-import流时不要开启--allow-unsafe-features选项。

**Tags**: `#open-source`, `#security`, `#dev-tools`

---

## AI Deals

<a id="item-ai-deals-1"></a>
### [小渔排班永久免费](https://www.appinn.com/xiaoyu-shift-calendar-free/) ⭐️ 8.0/10

你看到的内容可能由第三方 AI 基于小众软件文章提炼总结而成，可能与原文真实意图存在偏差。不代表小众软件观点和立场。请&lt;a href=&quot;https://www.appinn.com/xiaoyu-shift-calendar-free/&quot; target=&quot;\_blank&quot;&gt;点击链接阅读原文&lt;/a&gt;细致比对和校验。&lt;br /&gt;&lt;br /&gt;小渔排班开发者宣布这款开发了8年的轮班日历应用自2026年10月起全功能永久免费，无广告、无订阅，仅保留自愿支持开发者的选项，此前为付费应用。该应用专为轮班、倒班工作者设计，支持班次批量排布、班次闹钟自动调整、工时与薪资统计、班表导出（PDF/图片/CSV）、iCloud同步，以及iPhone、iPad、Apple Watch多端支持与小组件功能，用户可直接前往App Store下载使用，无截止时间。

rss · 小众软件 · Nov 10, 14:48

**「为什么重要」** 该应用此前为付费工具，曾进入国区App Store效率付费榜第2名，现在永久免费且无广告，对轮班工作者是零成本实用工具，开发者明确会继续长期维护更新。

**「可关注」** 可关注：小渔排班当前仅支持iOS生态，无安卓版本，垂直轮班场景的日历工具在移动端仍有稳定用户需求。

**Tags**: `#free-tier`, `#promo`

---