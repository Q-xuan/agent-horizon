---
layout: default
title: "Horizon Summary: 2026-11-11 (ZH)"
date: 2026-11-11
lang: zh
---

> 从 207 条内容中筛选出 18 条重要资讯。

<nav id="ah-toc" class="ah-toc" aria-label="目录"><span class="ah-toc-title">目录</span><ul><li><a href="#sec-harness-arch"><span class="ah-toc-name">Harness 架构</span><span class="ah-toc-count">5条</span></a></li><li><a href="#sec-agent-engineer"><span class="ah-toc-name">Agent 工程师日报</span><span class="ah-toc-count">6条</span></a></li><li><a href="#sec-ai-daily"><span class="ah-toc-name">AI 日报</span><span class="ah-toc-count">6条</span></a></li><li><a href="#sec-ai-deals"><span class="ah-toc-name">AI 羊毛</span><span class="ah-toc-count">1条</span></a></li></ul></nav>

---

**[Harness 架构](#sec-harness-arch)**
1. [Goose v1.59.0 发布](#item-harness-arch-1) ⭐️ 7.8/10
2. [pydantic-ai v2.67.0 发布](#item-harness-arch-2) ⭐️ 7.8/10
3. [stanfordnlp/dspy 3.5.0 发布](#item-harness-arch-3) ⭐️ 7.8/10
4. [Anthropic Agent Skills 实现公开](#item-harness-arch-4) ⭐️ 6.0/10
5. [Cursor Projects 升级多玩家协作](#item-harness-arch-5) ⭐️ 5.8/10

**[Agent 工程师日报](#sec-agent-engineer)**
1. [Gemini 4 Carbon 正式上线](#item-agent-engineer-1) ⭐️ 7.8/10
2. [DeepMind 发布 AlphaProof Code](#item-agent-engineer-2) ⭐️ 7.0/10
3. [Meta Muse Ember 1.0 发布](#item-agent-engineer-3) ⭐️ 7.0/10
4. [ReproBridge 发布 1029 任务基准](#item-agent-engineer-4) ⭐️ 7.0/10
5. [llm-gemini 0.36 发布 支持 Gemini 4 Carbon](#item-agent-engineer-5) ⭐️ 6.0/10
6. [Sage-Taiyi 科学发现架构发布](#item-agent-engineer-6) ⭐️ 6.0/10

**[AI 日报](#sec-ai-daily)**
1. [OpenAI 上线 ChatGPT 企业功能](#item-ai-daily-1) ⭐️ 7.8/10
2. [OpenAI 发布教育 AI 指导研究](#item-ai-daily-2) ⭐️ 7.8/10
3. [OpenAI Upwork 自由职业研究发布](#item-ai-daily-3) ⭐️ 7.8/10
4. [Gilbert + Tobin 律所 AI 转型访谈](#item-ai-daily-4) ⭐️ 6.8/10
5. [OpenAI 为护理人员推出免费 ChatGPT 培训](#item-ai-daily-5) ⭐️ 6.8/10
6. [Git 2.56.1 修复 6 个安全漏洞](#item-ai-daily-6) ⭐️ 6.8/10

**[AI 羊毛](#sec-ai-deals)**
1. [小渔排班 宣布永久免费](#item-ai-deals-1) ⭐️ 8.0/10

---

## Harness 架构
{: #sec-harness-arch .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-harness-arch" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-harness-arch-1"></a>
### [Goose v1.59.0 发布](https://github.com/aaif-goose/goose/releases/tag/v1.59.0) ⭐️ 7.8/10

Goose v1.59.0 发布，新增延迟 MCP 工具执行、子代理恢复、Agent 钩子控制及会话管理改进。ToolExecutionOperation 支持最小化延迟 MCP 工具；goose-agent \(GDK\) 新增 stop、approval 和 tool hook 操作；已完成委托支持后续跟进恢复。同时修复会话数据库与应用池隔离、Databricks OAuth 令牌自动刷新、Gemini thinking level 传递及 cargo-deny advisory 等问题。

github · github-actions\[bot\] · 11月10日 17:17

**「设计要点」** 会话数据库与应用池隔离初始化。goose-agent \(GDK\) 暴露 stop、approval、tool hook 控制面，ToolExecutionOperation 承载延迟 MCP 工具执行。

**「改了什么」** 新增延迟 MCP 工具执行、子代理恢复、Agent 钩子控制、实时语音指令配置、GPT-Live 端点配置及按客户端标签过滤会话。修复会话数据库初始化隔离、Databricks OAuth 令牌刷新、Gemini 参数传递、Opus 5.5 压缩提示词适配及 cargo-deny advisory 等问题。

**标签**: `#MCP`, `#subagent`, `#tool-execution`, `#session-management`, `#release`

---

<a id="item-harness-arch-2"></a>
### [pydantic-ai v2.67.0 发布](https://github.com/pydantic/pydantic-ai/releases/tag/v2.67.0) ⭐️ 7.8/10

pydantic-ai 正式发布 v2.67.0 版本，核心更新覆盖持久化执行、上下文加载、工具链、权限控制四大方向。本次版本新增持久化执行下动态子代理支持，优化 RepoContext 默认递归加载每目录嵌套指令文件并设置 32000 字符上限，调整 ArtifactScanner 匹配逻辑以支持隐藏变体选择器，扩展文档工具支持标准库 mimetypes 识别的全部媒体类型。同时完成多项兼容性调整，包括原生工具字段迁移至 provider\_settings、CodeMode 禁止使用 Python 内置名作为工具名、OpenAI 响应无 history\_digest 时停止续传等。

github · dsfaccini · 11月10日 23:11

**「设计要点」** 本次更新围绕 agent 运行时的持久化、上下文管理、工具调用、权限控制四个核心维度展开：运行时层覆盖子代理、guardrail、judge、Prefect 重试的 durable 记录与 gRPC 远程沙箱支持；上下文层优化仓库指令的递归加载与字符上限控制；工具层扩展文档媒体类型支持并重构原生工具配置结构；权限层新增路径级工作区权限与 operator 权限校验。

**「改了什么」** 相对上一版本，本次新增持久化执行下动态子代理、DBOS 子工作流并行执行能力，支持 guardrail 与 judge 结果 durable 记录、Prefect 流重试时重放含二进制内容的历史消息，CodeMode 远程沙箱可通过 gRPC 运行（依赖 pydantic-monty 1.5.0）；RepoContext 默认递归加载每目录嵌套指令文件，新增 walk\_up 参数与 32000 字符上限配置，Coder 基于嵌套指令构建，模型写入/编辑目录时自动 surfaced 嵌套指令；ArtifactScanner 匹配前剥离默认可忽略字符并标记隐藏变体选择器，文档工具支持标准库 mimetypes 识别的全部媒体类型，原生工具字段迁移至 provider\_settings，新增消息队列 dequeue 与优先级调整能力，CodeMode 禁止使用 Python 内置名作为工具名；新增路径级工作区权限、operator 权限校验，禁止低于 operator 权限创建 CapabilityCreation 运行，OpenAI 响应无 history\_digest 时停止通过 openai\_previous\_response\_id 续传，聊天模板特殊 token 在内容中拆分、输出中恢复，流式运行结束时 StreamedRunResult.result 抛出 UserError。

**标签**: `#runtime`, `#subagents`, `#memory`, `#tools`, `#sandbox`

---

<a id="item-harness-arch-3"></a>
### [stanfordnlp/dspy 3.5.0 发布](https://github.com/stanfordnlp/dspy/releases/tag/3.5.0) ⭐️ 7.8/10

DSPy 3.5.0 发布，核心模块 RLM、Flex、GEPA 脱离实验阶段。ReAct 被 ReActV2 替换，引入结构化 History 与类型化 submit 工具；工具结果支持图片、文件等富媒体。RLM 新增对话历史持久化与图像能力，优先使用原生推理并支持显式计划；lm15 引擎使 LiteLLM 与 OpenAI 库变为可选依赖，默认安装体积从 206.7 MiB 降至 30.9 MiB。本版本变更 prompts、默认值与 API，存在破坏性变更，需参照升级指南迁移。

github · isaacbmiller · 11月10日 16:25

**「设计要点」** 运行时基于 Deno，通过预编译标准库、缓存启动快照与 InterpreterPool 预热降低冷启动开销；工具层采用结构化 History 与类型化 submit，支持富媒体结果，RLM History 提供对话持久化但不恢复实时变量。LM 层改用轻量 lm15 引擎，默认自动路由 API 族，磁盘缓存默认禁用 pickle 并限制加载。

**「改了什么」** ReActV2 替换 ReAct，提供结构化 History 与类型化 submit 工具；RLM、Flex、GEPA 脱离实验阶段，工具结果支持富媒体且 RLM 新增对话历史持久化与图像能力。LiteLLM 与 OpenAI 库变为可选，XMLAdapter 与 model\_type=&quot;auto&quot; 成为默认，磁盘缓存禁用 pickle 并限制加载；本版本变更 prompts、默认值与 API。

**标签**: `#runtime`, `#tools`, `#memory`, `#planning`

---

<a id="item-harness-arch-4"></a>
### [Anthropic Agent Skills 实现公开](https://github.com/anthropics/skills) ⭐️ 6.0/10

这是 Anthropic 公开的 Agent Skills 标准实现仓库\`anthropics/skills\`，对应\`agentskills.io\`定义的通用标准，用于扩展 Claude 的能力边界。技术上新点在于支持动态加载包含指令、脚本、资源的技能文件夹，以可复现的方式提升 Claude 完成特定专业任务的表现，适用场景包括按企业品牌规范生成文档、使用组织内部工具分析数据等。

rss · GitHub Trending Daily · 11月11日 03:12

**标签**: `#tools`, `#runtime`

---

<a id="item-harness-arch-5"></a>
### [Cursor Projects 升级多玩家协作](https://cursor.com/blog/projects-multiplayer) ⭐️ 5.8/10

Cursor Projects 在 2026-11-10 宣布升级为多玩家（multiplayer）协作工作区。此前 Projects 仅支持单人多 agent 协调，现在团队可邀请成员加入同一 Project，与 agent fleet 共享上下文、记忆和任务看板。新增跨团队成员 agent 实时通信，使不同工程师的 agent 能提前协调工作顺序、避免合并冲突。该功能目前以 beta 形式向所有 Cursor 用户推出。

rss · Cursor Blog · 11月10日 12:00

**「改了什么」** Projects 从单人多 agent 工作区升级为团队级多玩家工作区，新增共享上下文层、共享任务板、跨 teammate agent 实时通信，以及新成员加入时的上下文预配置。beta 阶段已向所有 Cursor 用户开放。

**标签**: `#memory`, `#subagents`, `#planning`

---

## Agent 工程师日报
{: #sec-agent-engineer .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-agent-engineer" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-agent-engineer-1"></a>
### [Gemini 4 Carbon 正式上线](https://deepmind.google/blog/gemini-4-carbon-is-now-available/) ⭐️ 7.8/10

Google DeepMind 于 2026-11-10 发布官方公告，确认 Gemini 4 Carbon 模型即日起正式上线（general availability）。该模型面向 AI agent 工程师、harness 开发者及 eval 工作流提供新的底层模型选项。当前公告未披露具体技术性能指标、能力细节或与前一版本的对比基准。

rss · Google DeepMind · 11月10日 16:03

**「为什么重要」** Gemini 4 Carbon 来自主流 AI 实验室，其可用性扩展了 agent 系统的底层模型选型空间。但具体能力提升、成本结构及 API 兼容性尚未公开，实际影响需等待进一步技术文档。

**「可关注」** 可关注：Gemini 4 Carbon 已进入 GA 阶段，但技术细节与定价尚未公开，建议暂缓接入生产 harness，待官方发布基准测试与 API 文档后再评估迁移成本。

**标签**: `#harness`, `#coding-agent`, `#eval`

---

<a id="item-agent-engineer-2"></a>
### [DeepMind 发布 AlphaProof Code](https://deepmind.google/blog/introducing-alphaproof-code/) ⭐️ 7.0/10

据 Hacker News 讨论，DeepMind 于 2026 年 11 月 10 日发布 AlphaProof Code 形式化代码验证证明代理，核心机制为迭代遍历代码库编写并运行 Lean/Rocq 证明，工作模式与经典编码代理高度相似。社区讨论提到该代理此前验证过存在历史 bug 的人类编写代码库时未发现缺陷，引发对证明范围是否过窄、AI 生成证明本身是否存在错误的质疑，目前无公开完整技术规格、性能基准与详细架构信息。

hackernews · Google DeepMind · 11月10日 12:11 · [社区讨论](https://news.ycombinator.com/item?id=50439193)

**「为什么重要」** 这是面向代码场景的形式化验证 AI 证明代理首次进入公众讨论，其与现有编码代理高度相似的工作模式，以及社区提出的 AI 证明可靠性、验证范围过窄等实际风险，对 coding agent 设计、代码正确性 eval 工具链开发有直接参考价值。

**「可关注」** 可关注 AI 生成形式化证明本身的可靠性风险，以及当前验证代理可能仅覆盖窄代码属性而非全量正确性的限制，避免在 eval 场景中过度信任其验证结果。

**「评论」** 社区普遍认可该代理与经典编码代理的工作模式相似性，均通过迭代代码库生成并运行证明代码；同时存在分歧，有用户质疑其此前验证零 bug 的结果可能源于证明范围过窄，或 AI 生成的证明本身存在未被发现的错误，也有用户看好其长期改变软件验证范式的潜力。

**标签**: `#coding-agent`, `#eval`

---

<a id="item-agent-engineer-3"></a>
### [Meta Muse Ember 1.0 发布](https://simonwillison.net/2026/Nov/10/muse-ember/) ⭐️ 7.0/10

2026 年 11 月 10 日，Meta AI 发布 Muse Ember 1.0，定位为面向 agent 工作流的小型高效模型，主打 tool calls、编码子任务、路由、信息提取、长文档解析等重复性推理场景。该模型提供 minimal、low、medium、high、xhigh、max 共 6 个推理等级，支持 1M token 上下文；短提示词（≤200k 输入 token）定价为$0.10/百万输入 token、$0.50/百万输出 token，与 GPT-6 Luna、Claude Haiku 5.5 持平；超过 200k 输入 token 后输入价涨至$0.30/百万，输出价涨至$1.50/百万。Artificial Analysis 的 Intelligence Index vs Cost per Task 图表显示，Muse Ember 的 xhigh、max 推理等级位于效率帕累托前沿，同 Intelligence Index 下成本比 Claude Haiku 5.5 xhigh 低约一半。公开测试显示其 high 推理等级生成 SVG 时未返回完整结果，推理等级与输出质量无明确线性映射关系。目前公开材料未提供该模型的性能基准或生产环境实测数据，主要影响做 coding agent 选型、成本优化的工程师。

rss · Simon Willison · 11月10日 07:28

**「为什么重要」** 当前 agent 工作流对低推理成本、高执行效率的小模型需求明确，Muse Ember 的帕累托前沿定位为工具调用、编码子任务等场景的模型选型提供了新的成本优化选项。

**「可关注」** 可关注：若 agent 工作流以 tool calls、编码子任务、长文档解析为核心场景，可对比测试 Muse Ember xhigh/max 等级与现有同价位模型的单任务成本、延迟及输出稳定性表现。

**标签**: `#coding-agent`, `#orchestration`

---

<a id="item-agent-engineer-4"></a>
### [ReproBridge 发布 1029 任务基准](https://huggingface.co/papers/2611.08452) ⭐️ 7.0/10

2026-11-11 ，Hugging Face Daily Papers 介绍 ReproBridge，一个用于构建可复现机器学习研究工件的标准化代理工作流，配套 ReproBridge-Bench 基准。该基准包含 1,029 个任务，覆盖 387 个实验、36 篇论文，每个任务提供 5 个人工验证的参考分数。材料未包含代理性能对比数据。

rss · Hugging Face Daily Papers · 11月11日 03:12

**「为什么重要」** 它为 coding agent 评估与 harness 开发提供了标准化资源，直接针对 ML 实验复现这一具体场景。目前材料未披露代理在该基准上的实际表现数据。

**「可关注」** 可关注：ReproBridge-Bench 的 1,029 个任务及人工验证参考分数可作为 coding agent 复现能力的评估素材。

**标签**: `#eval`, `#coding-agent`, `#harness`

---

<a id="item-agent-engineer-5"></a>
### [llm-gemini 0.36 发布 支持 Gemini 4 Carbon](https://simonwillison.net/2026/Nov/10/llm-gemini/) ⭐️ 6.0/10

llm-gemini 0.36 于 2026-11-10 发布，新增对 Gemini 4 Carbon 的支持。该模型初始定价为输入 $2/百万 token、输出 $10/百万 token，12 月 1 日将翻倍至 $4/$20。本次更新新增可配置的 thinking effort 参数，默认值为 medium。作者实测该模型可生成基于 OpenStreetMap 数据的 Three.js 动画，并可通过追加提示转为无外部依赖的独立 HTML 文件。

rss · Simon Willison · 11月10日 20:09

**「为什么重要」** 这是 llm-gemini 插件对最新公开可用 Gemini 模型的适配，临时定价窗口与可配置思考强度为 coding agent 的成本调控与输出质量调整提供了新选项，12 月 1 日模型涨价后相关成本结构将发生变化。

**「可关注」** 可关注：llm-gemini 0.36 新增的 thinking effort 参数可针对 coding agent 场景调整模型思考强度，Gemini 4 Carbon 当前临时定价窗口（12 月 1 日涨价前）可评估成本收益。

**标签**: `#coding-agent`, `#harness`

---

<a id="item-agent-engineer-6"></a>
### [Sage-Taiyi 科学发现架构发布](https://huggingface.co/papers/2611.12762) ⭐️ 6.0/10

2026 年 11 月 11 日 HF 每日论文收录 Sage-Taiyi 元认知科学发现架构，该架构通过显式监控与调控机制，基于积累的科学认知调整研究目标与推理方法。配套的 Taiyi-Bench 是覆盖 10 个学科、265 个任务的 AI 协同科学创想基准，Sage-Taiyi 在该基准全部 8 项历史复现与开放创想指标上排名第一，总体得分 54.0，高于最强基线 AI Scientist-v2 的 47.9。当前公开材料为截断版本，未披露实现细节，领域适配性有限。

rss · Hugging Face Daily Papers · 11月11日 03:12

**「为什么重要」** 该工作提出的显式元认知监控、可复用推理方法选择机制，对智能体编排与记忆设计有可迁移参考价值；但当前公开内容截断、领域聚焦科学发现，尚未证实对通用 AI Agent 工程的实际落地价值。

**「可关注」** 可关注：元认知驱动的显式监控与调控机制、配套的 Taiyi-Bench 评估框架，对智能体记忆设计与效果验证有参考价值。

**标签**: `#eval`, `#orchestration`, `#memory`

---

## AI 日报
{: #sec-ai-daily .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-daily" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-daily-1"></a>
### [OpenAI 上线 ChatGPT 企业功能](https://openai.com/index/introducing-businesses-chatgpt) ⭐️ 7.8/10

2026 年 11 月 10 日，OpenAI 发布 ChatGPT 面向企业的「Businesses in ChatGPT」功能。该功能支持企业方管理自身在 ChatGPT 内的业务信息、获取自身业务在 ChatGPT 中的展示相关洞察，还可将用户对企业的兴趣转化为实际转化动作。本次更新为产品功能扩展，未涉及底层模型调整。

rss · OpenAI Blog · 11月10日 10:00

**「为什么重要」** 该功能为企业在 ChatGPT 生态内提供了官方运营与转化通道，是 OpenAI 面向 B 端场景的产品能力补充。

**「可关注」** 可关注：企业可通过该功能直接管理在 ChatGPT 中展示的业务信息。

**标签**: `#product`, `#industry`, `#lab`

---

<a id="item-ai-daily-2"></a>
### [OpenAI 发布教育 AI 指导研究](https://openai.com/index/closing-ai-guidance-gap-education) ⭐️ 7.8/10

2026 年 11 月 10 日，OpenAI 官方博客发布新内容，公布 ThinkYoung 相关研究与 EMEA 地区教育合作项目的经验总结，聚焦教师支持、AI 素养提升与自主学习三个核心方向。

rss · OpenAI Blog · 11月10日 09:00

**「为什么重要」** 当前教育场景的 AI 应用规范仍处于探索阶段，该研究成果与合作经验可为教育从业者提供可参考的落地方向。

**「可关注」** 可关注：教育场景下 AI 素养培育与教师支持工具的设计方向。

**标签**: `#lab`, `#industry`, `#policy`

---

<a id="item-ai-daily-3"></a>
### [OpenAI Upwork 自由职业研究发布](https://openai.com/index/ai-effect-on-freelance-work) ⭐️ 7.8/10

OpenAI 与 Upwork 联合发布新研究，披露 AI 对自由职业市场的影响。研究发现 AI 推动自由职业需求发生转移，新的技能组合不断涌现，AI 相关自由职业项目的预算与工时均呈增长态势，未披露具体增幅数值。

rss · OpenAI Blog · 11月10日 07:00

**「为什么重要」** 该研究为自由职业从业者、相关企业提供了 AI 冲击下自由职业市场变化的直接参考依据，有助于把握技能需求与项目机会的变化方向。

**「可关注」** 可关注：AI 相关自由职业项目的技能需求与预算投入均呈增长趋势，可针对性储备对应技能组合。

**标签**: `#lab`, `#industry`, `#research`

---

<a id="item-ai-daily-4"></a>
### [Gilbert + Tobin 律所 AI 转型访谈](https://openai.com/index/gilbert-tobin-sam-nickless) ⭐️ 6.8/10

OpenAI 博客发布对 Gilbert + Tobin CEO Sam Nickless 的采访，讨论该律所如何通过 AI 进行业务转型。这是一篇客户成功案例，未涉及具体技术模型发布或产品更新。

rss · OpenAI Blog · 11月12日 00:00

**标签**: `#industry`, `#lab`, `#product`

---

<a id="item-ai-daily-5"></a>
### [OpenAI 为护理人员推出免费 ChatGPT 培训](https://openai.com/index/helping-caregivers-use-ai-in-everyday-life) ⭐️ 6.8/10

OpenAI 宣布其 OpenAI Academy 项目正在美国 5 个城市面向护理人员推出免费 ChatGPT 实操培训，帮助其掌握日常实用的 AI 技能。该项目暂无进一步扩展规模的公开信息。

rss · OpenAI Blog · 11月10日 12:00

**「为什么重要」** 这是 OpenAI 拓展 AI 普惠覆盖群体的新动作，护理人员此前较少成为 AI 技能培训的目标受众，该项目的落地可观察垂直场景的 AI 工具适配路径。

**「可关注」** 可关注：护理等垂直场景的 AI 实操培训项目的用户反馈，为同类场景的 AI 工具设计提供参考。

**标签**: `#lab`, `#product`, `#industry`

---

<a id="item-ai-daily-6"></a>
### [Git 2.56.1 修复 6 个安全漏洞](https://github.blog/open-source/git/git-security-vulnerabilities-announced-7/) ⭐️ 6.8/10

Git 项目今日发布 Git 2.56.1 及 2.50.2 至 2.55.1 共 6 个旧维护版本的向后移植补丁，修复 6 个安全漏洞。漏洞涵盖递归克隆任意代码执行、路径遍历、内存损坏等风险，其中 CVE-2026-111760 可通过恶意仓库的递归克隆触发代码执行。项目方建议用户升级至 Git 2.56.1 或对应维护系列的补丁版本，同时更新所有捆绑 Git 的应用程序。

rss · GitHub Blog · 11月10日 18:00

**「为什么重要」** 该安全公告覆盖所有使用 Git 的 AI 开发场景，恶意构造的仓库可在递归克隆时触发任意代码执行，对代码托管、自动化流水线等环节的代码安全构成直接威胁。

**「可关注」** 可关注：升级至 Git 2.56.1 或对应维护系列的补丁版本，同步更新捆绑 Git 的应用程序，处理不可信仓库时避免使用存在漏洞的旧版本。

**标签**: `#open-source`, `#security`, `#dev-tools`

---

## AI 羊毛
{: #sec-ai-deals .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-deals" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-deals-1"></a>
### [小渔排班 宣布永久免费](https://www.appinn.com/xiaoyu-shift-calendar-free/) ⭐️ 8.0/10

你看到的内容可能由第三方 AI 基于小众软件文章提炼总结而成，可能与原文真实意图存在偏差。不代表小众软件观点和立场。请&lt;a href=&quot;https://www.appinn.com/xiaoyu-shift-calendar-free/&quot; target=&quot;\_blank&quot;&gt;点击链接阅读原文&lt;/a&gt;细致比对和校验。&lt;br /&gt;&lt;br /&gt;小渔排班是面向轮班、倒班工作者（如医护、制造业从业者）的日历应用，2018 年为开发者家人初衷开发，已迭代 8 年，2026 年 10 月起全功能永久免费，无广告、无订阅，仅保留自愿支持开发者的选项，用户可直接前往 App Store 下载使用。该应用支持班次闹钟、工时薪资统计、班表导出（PDF/图片/CSV）、iCloud 同步备份，适配 iPhone、iPad、Apple Watch 等多设备，开发者承诺长期维护更新。

rss · 小众软件 · 11月10日 14:48

**「为什么重要」** 该应用此前为付费工具，曾登上国区 App Store 效率付费榜第 2 名，如今全功能无广告无订阅永久免费，对轮班、倒班人群是零成本的排班管理工具福利，且开发者明确会持续更新维护。

**「可关注」** 可关注：小渔排班全功能永久免费，无广告无订阅，支持 iCloud 同步、多格式班表导出，适配苹果全系设备，适合有轮班排班需求的用户使用。

**标签**: `#free-tier`, `#promo`

---