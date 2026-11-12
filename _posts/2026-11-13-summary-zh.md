---
layout: default
title: "Horizon Summary: 2026-11-13 (ZH)"
date: 2026-11-13
lang: zh
---

> 从 197 条内容中筛选出 18 条重要资讯。

<nav id="ah-toc" class="ah-toc" aria-label="目录"><span class="ah-toc-title">目录</span><ul><li><a href="#sec-harness-arch"><span class="ah-toc-name">Harness 架构</span><span class="ah-toc-count">5条</span></a></li><li><a href="#sec-agent-engineer"><span class="ah-toc-name">Agent 工程师日报</span><span class="ah-toc-count">5条</span></a></li><li><a href="#sec-ai-daily"><span class="ah-toc-name">AI 日报</span><span class="ah-toc-count">8条</span></a></li></ul></nav>

---

**[Harness 架构](#sec-harness-arch)**
1. [pydantic-ai v2.68.0 发布](#item-harness-arch-1) ⭐️ 7.8/10
2. [OpenClaw 持久化代理安全架构](#item-harness-arch-2) ⭐️ 5.8/10
3. [Claude Code v2.1.323 发布](#item-harness-arch-3) ⭐️ 5.5/10
4. [browser-use 1.0.3rc1 发布候选版](#item-harness-arch-4) ⭐️ 5.3/10
5. [browser-use 登上 GitHub Trending](#item-harness-arch-5) ⭐️ 5.0/10

**[Agent 工程师日报](#sec-agent-engineer)**
1. [Gemini 4 Hydrogen 发布](#item-agent-engineer-1) ⭐️ 7.8/10
2. [smolmaxxing 实现 16B 模型跑 1GB 以下设备](#item-agent-engineer-2) ⭐️ 7.0/10
3. [SteerDistill 闭环蒸馏降低 Agent 推理成本](#item-agent-engineer-3) ⭐️ 7.0/10
4. [PISA 与 PISA-E 路由方法发布](#item-agent-engineer-4) ⭐️ 7.0/10
5. [HF 日报：RL 激励 LLM 自学习研究](#item-agent-engineer-5) ⭐️ 6.0/10

**[AI 日报](#sec-ai-daily)**
1. [Opus 5.5 设为全付费层默认](#item-ai-daily-1) ⭐️ 8.8/10
2. [Claude Managed Agents 推出自托管私有测试](#item-ai-daily-2) ⭐️ 8.8/10
3. [Claude Meetings Beta 上线](#item-ai-daily-3) ⭐️ 8.8/10
4. [Claude 发布制造业专用插件](#item-ai-daily-4) ⭐️ 8.8/10
5. [OpenAI 200 万美元资助儿童 AI 安全研究](#item-ai-daily-5) ⭐️ 7.8/10
6. [GitHub 发布 Agent Skills 实践指南](#item-ai-daily-6) ⭐️ 7.8/10
7. [J.Crew 上线 Claude 造型顾问](#item-ai-daily-7) ⭐️ 7.8/10
8. [Claude Tag 发布创业公司使用指南](#item-ai-daily-8) ⭐️ 7.8/10

---

## Harness 架构
{: #sec-harness-arch .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-harness-arch" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-harness-arch-1"></a>
### [pydantic-ai v2.68.0 发布](https://github.com/pydantic/pydantic-ai/releases/tag/v2.68.0) ⭐️ 7.8/10

pydantic-ai v2.68.0 于 2026-11-12 发布。本次新增 \`OutputTokenLimitExceeded\` 异常，\`ModelFallback\` 在响应因 \`max\_tokens\` 截断时自动切换模型；\`AskUser\` 迁至 deferred pipeline，由 \`RequestInput\` 在 run 内处理审批与回答，并标记 \`kind\` 与 \`answered\_by\`。新增 \`DelegationTasks.discover\(\)\`，修复损坏的 saved task 阻塞 \`opened\(\)\` 的问题。workspace backends 须保持 detached processes 存活，\`WorkspaceBackendSuite\` 增加检查。

github · dsfaccini · 11月12日 01:56

**「设计要点」** 运行时将 \`PromptInjectionDefender\` 语义分类改为 durable operations，支持 Temporal；子代理委托可降级为 Temporal 与 DBOS child workflows，\`Permissions\` remembered approvals 在 durable execution 中持久化。工具层将 \`AskUser\` 后移至 deferred pipeline，由 \`RequestInput\` 在 run 内处理；沙箱层要求 workspace backends 保证 detached processes 存活，并在 \`WorkspaceBackendSuite\` 中校验重连。

**「改了什么」** 模型层新增 \`OutputTokenLimitExceeded\` 与 \`ModelFallback\` 自动切换，用户交互改为 deferred pipeline 内的 \`RequestInput\`。子代理新增 \`DelegationTasks.discover\(\)\` 并修复 saved task 阻塞，harness 层展开缩写、重命名事件字段并新增 \`RefineOutput\` capability、\`GoogleDecisionsModel\` backend 与 \`ConversationStore\` 支持。

**标签**: `#runtime`, `#tools`, `#subagents`, `#sandbox`, `#permissions`

---

<a id="item-harness-arch-2"></a>
### [OpenClaw 持久化代理安全架构](https://developers.openai.com/blog/securing-persistent-agents-like-openclaw-at-openai) ⭐️ 5.8/10

OpenAI 开发者博客发布 OpenClaw 持久化代理安全架构。OpenClaw 作为 24/7 运行的代理，能主动采取行动且可自行修改配置与代码，威胁模型从外部攻击转向内部错位。安全架构核心是将可信静态逻辑（网关、网络、身份、沙箱控制）与不可信 LLM 执行（代理工作负载）分离，通过远程 Harness 实现容器级隔离。部署控制包括：网络 allowlist 与显式 deny 列表、工作区写入限制、codex linux sandbox 进程隔离、凭证代理隐藏密钥、基于 LLM 的 Auto-review 自动审批、独立代理身份关联 ChatGPT Service Account，以及全量审计日志。文章附 codex harness 的 requirements.toml 与 config.toml 配置示例，明确移除 danger-full-access 模式、限制网络域名、禁用 SOCKS5 与本地代理监听。

rss · OpenAI Developer · 11月12日 00:00

**「设计要点」** 运行时采用 OpenClaw Gateway 与 Agent Harness 分离部署，网关作为可信静态代码运行在独立容器/集群，负责代理配置；代理工作负载作为不可信代码运行在沙箱内。权限模型通过 codex linux sandbox 实现网络 allowlist、工作区写入限制、进程隔离和凭证代理，密钥对代理透明。额外增加基于 LLM 的 Auto-review 层作为动态防护，所有控制平面配置变更与代理回合均被记录审计。

**「改了什么」** 这篇文章首次公开 OpenAI 内部 OpenClaw 部署的安全控制清单，将此前未公开的沙箱配置、网络限制、身份分离和 Auto-review 机制标准化为可复用的配置示例。持久化代理引入内部威胁模型，要求从架构上分离可信控制面与不可信执行面，这与传统一次性代码执行的安全假设不同。

**标签**: `#runtime`, `#permissions`, `#sandbox`, `#persistent-agents`

---

<a id="item-harness-arch-3"></a>
### [Claude Code v2.1.323 发布](https://github.com/anthropics/claude-code/releases/tag/v2.1.323) ⭐️ 5.5/10

Claude Code v2.1.323 引入实验性 Code Mode，允许 Claude 编写 JavaScript 调用工具。插件系统新增 \`engines\[&quot;claude-code&quot;\]\` 版本约束，超出范围插件禁止安装、更新或加载。\`claude plugin validate\` 增强 TypeScript hooks 类型检查与 \`$\` nouns 验证。同时修复 sign-in 状态漂移、内存峰值、Bash 权限检查及 worktree 会话路径错误等多项问题。

github · claude-code-publisher\[bot\] · 11月12日 22:12

**「设计要点」** Code Mode 将工具调用从声明式 schema 转为 JavaScript 运行时生成，改变 agent 执行层的工具绑定机制。插件引擎通过版本范围约束实现运行时兼容性门控，\`claude plugin validate\` 承担静态检查职责；sign-in 与后台会话状态统一为 per-session 绑定，消除跨 profile 凭证残留风险。

**「改了什么」** 新增实验性 Code Mode（JavaScript 工具调用）、插件版本兼容性门控、插件验证的 TypeScript 类型检查与 \`$\` nouns 检查。修复后台会话 sign-in 状态漂移、大文件编辑内存峰值、Bash 权限检查绕过、worktree 退出后路径错误及非流式请求错误恢复等问题，新增环境变量控制项。

**标签**: `#runtime`, `#tools`, `#plugins`

---

<a id="item-harness-arch-4"></a>
### [browser-use 1.0.3rc1 发布候选版](https://github.com/browser-use/browser-use/releases/tag/1.0.3rc1) ⭐️ 5.3/10

browser-use 发布 1.0.3rc1 官方候选版本，需显式执行 \`pip install &\#x27;browser-use==1.0.3rc1&\#x27;\` 安装，默认 pip 安装仍会获取 1.0.2 版本。本次更新无新增功能，聚焦 6 项 bug 修复，覆盖 MCP 集成、多环境浏览器运行、配置校验、云任务超时等场景。

github · gregpr07 · 11月12日 02:11

**「设计要点」** 运行时层新增跨 pid 命名空间 Chrome 实例识别逻辑，通过 DevToolsActivePort 适配容器、云沙箱等隔离环境；MCP CLI 管道处理增加客户端提前关闭的异常退出兜底，避免进程 hanging；同时优化云运行取消任务的下载复制超时机制，将最长阻塞时长从 300 秒缩短至 10 秒。

**「改了什么」** 相对 1.0.2 版本，本次候选版共修复 6 项问题：修复 \`--cli-mcp\` 在客户端提前关闭管道时无法正常退出的 bug；无远程调试浏览器或无显示环境时 CLI 可自动启动本地 Chromium；无效 \`BU\_CDP\_URL\` 配置会在 3 秒内输出明确错误后退出；支持识别其他 pid 命名空间的 Chrome 实例；取消的云运行任务下载复制超时从最长 300 秒缩短至 10 秒；修复 \`ActionResult\` 仅对首个被忽略的 0.x 字段告警的问题，现会提示所有被忽略的 0.x 字段，相关修复见 PR \#6383。

**标签**: `#mcp`, `#runtime`, `#sandbox`

---

<a id="item-harness-arch-5"></a>
### [browser-use 登上 GitHub Trending](https://github.com/browser-use/browser-use) ⭐️ 5.0/10

这是开源 Python 浏览器 agent 工具库 browser-use，同时提供 Browser Use Cloud 托管服务，核心能力是通过持久 REPL 结合 Chrome DevTools Protocol（CDP）让 LLM 驱动真实浏览器完成任务，支持任意本地或云端 LLM，采用 MIT 协议。

rss · GitHub Trending Daily · 11月12日 23:00

**「设计要点」** 运行时采用持久 REPL 承载模型生成的 Python 代码，直接调用内置浏览器 harness 辅助函数与原生 CDP 操控浏览器，未提及额外沙箱隔离机制。

**标签**: `#runtime`, `#tools`, `#sandbox`

---

## Agent 工程师日报
{: #sec-agent-engineer .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-agent-engineer" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-agent-engineer-1"></a>
### [Gemini 4 Hydrogen 发布](https://deepmind.google/blog/introducing-gemini-4-hydrogen/) ⭐️ 7.8/10

Google DeepMind 2026 年 11 月 12 日通过官方博客宣布推出 Gemini 4 Hydrogen 基础模型，该模型为 Gemini 系列新变体，与 AI agent 开发、评测存在潜在关联，当前未公开具体技术参数、能力细节与定价策略。已有用户反馈该模型已在 Gemini 服务中替代 3.8 Flash 上线，主要影响使用 Gemini 系列模型开发 AI agent 的工程师群体。

rss · Google DeepMind · 11月12日 18:00

**「为什么重要」** 这是 Gemini 系列官方基础模型更新，该系列是 AI agent 开发常用的底层模型之一，命名规则变化可能影响工程师模型选型。但具体能力提升、性价比及对现有 agent 工作流的影响尚未得到官方证实，需等待后续详细披露。

**「可关注」** 可关注两点：一是当前公开信息未披露该模型技术指标、定价与能力边界，选型前需等待官方详细说明；二是已有用户反馈该模型在 Gemini 服务中替代 3.8 Flash 上线，可留意后续灰度范围扩展情况。

**「评论」** HackerNews 用户反馈该模型上线速度较快，对元素命名体系表示困惑，认为氢的命名易让人误判模型定位。有用户推测其定位为替代 3.5 Flash Lite 的高性能入门模型，但对其定价高于现有 3.8 Flash 折扣价的合理性提出疑问。另有用户反馈使用 Gemini 命令行工具时遭遇账号封禁，支持流程体验不佳。

**标签**: `#coding-agent`, `#eval`

---

<a id="item-agent-engineer-2"></a>
### [smolmaxxing 实现 16B 模型跑 1GB 以下设备](https://github.com/hyperionaidev/smolmaxxing/) ⭐️ 7.0/10

2026 年 11 月 12 日，开源项目 smolmaxxing（仓库：github.com/hyperionaidev/smolmaxxing，作者 mrashad74）宣布实现 16B 参数大语言模型在可用内存低于 1GB 的边缘消费级设备（初代 iPad Air、小米电视盒子）上运行，已开源对应优化内核、修改后的模型及复现结果，模型托管于 Hugging Face 的 hyperionaidev 账号，未公开具体推理速度等性能指标。该成果面向需要本地无云推理的端侧/边缘 AI Agent 开发者。

hackernews · mrashad74 · 11月12日 15:23 · [社区讨论](https://news.ycombinator.com/item?id=50468888)

**「为什么重要」** 当前端侧 AI Agent 多依赖云端推理，该开源方案提供了可复现的低资源 LLM 部署路径，降低了边缘设备本地运行大模型的门槛。

**「可关注」** 可关注：项目已开源优化内核、修改后的模型及复现步骤，可直接验证低资源环境下的 LLM 部署效果。

**「评论」** 社区普遍认可低资源模型优化的技术进展，有用户分享已跑通 6.5M 参数推理模型，也有用户讨论小模型在实际任务中的实用性边界，另有用户调侃相关技术的潜在滥用风险。

**标签**: `#inference-optimization`, `#edge-deployment`, `#open-source-tooling`, `#low-resource-llm`

---

<a id="item-agent-engineer-3"></a>
### [SteerDistill 闭环蒸馏降低 Agent 推理成本](https://huggingface.co/papers/2611.13410) ⭐️ 7.0/10

2026-11-12，Hugging Face Daily Papers 收录论文《SteerDistill: Quantizing LLM Agents via Closed-Loop Teacher Steering》。该方法针对低比特量化 LLM Agent 任务成功率下降问题，提出闭环量化感知蒸馏框架。全精度教师模型指导学生修正失败响应，并基于学生执行反馈迭代优化指导，从而修正行为偏差。该方法旨在降低 Agent 推理成本，同时维持任务成功率。

rss · Hugging Face Daily Papers · 11月12日 00:00

**「为什么重要」** 量化是降低 LLM Agent 推理成本的关键路径，但离线数据难以覆盖学生失败场景，导致行为偏差修正困难。SteerDistill 的闭环机制提供了一种实用蒸馏思路，可能影响轻量级 Agent 的训练流程设计。

**「可关注」** 可关注：量化 Agent 的行为偏差可通过教师-学生闭环执行反馈进行迭代修正，而非依赖静态离线数据集。

**标签**: `#coding-agent`, `#quantization`, `#distillation`

---

<a id="item-agent-engineer-4"></a>
### [PISA 与 PISA-E 路由方法发布](https://huggingface.co/papers/2611.10193) ⭐️ 7.0/10

Hugging Face Daily Papers 于 2026-11-12 介绍了 arXiv 论文 2611.10193，提出 PISA 与 PISA-E 两种提示自适应、成本感知的 LLM 推理路由框架。PISA 通过软聚类成员度与模型特定预测器估计单模型能力，PISA-E 进一步支持集成路由，可在推理时调整成本-质量权衡而无需重新训练。该方法针对需要在异构请求上平衡响应质量与推理成本的 Web 服务场景，相比传统单模型路由和固定集成路由，支持动态调整集成组成与基数。材料未提供完整评估指标或生产部署上下文。

rss · Hugging Face Daily Papers · 11月12日 00:00

**「为什么重要」** 该论文提供了无需重新训练即可在推理时调整成本-质量权衡的具体技术路径，对 agent 推理优化有参考价值。但材料未披露实际性能数据或大规模部署验证，其效果尚未在生产环境得到证实。

**「可关注」** 可关注：PISA 的软聚类成员度与模型特定预测器组合，以及 PISA-E 在推理时动态调整集成组成的机制，可作为 agent 推理路由的工具链优化参考。

**标签**: `#orchestration`

---

<a id="item-agent-engineer-5"></a>
### [HF 日报：RL 激励 LLM 自学习研究](https://huggingface.co/papers/2610.39671) ⭐️ 6.0/10

2026-11-12，Hugging Face Daily Papers 收录 arXiv 预印本 2610.39671，提出一种基于强化学习的 LLM 自学习框架。该框架引入 BookNavigator 接口，使模型能自主检索、学习并应用长格式参考材料中的知识，同时配套基于教科书的数学问题求解基准，用于评估即时知识获取与推理能力。当前仅为研究预印本，内容被截断，尚无生产就绪工具或框架变更，对 agent 工程的影响尚未证实。

rss · Hugging Face Daily Papers · 11月12日 00:00

**「为什么重要」** 该研究将自学习、长上下文交互与知识推理评估结合，指向 agent 在陌生领域减少对预训练知识依赖的潜在路径。但论文尚未经过同行评审，且无可用代码或工具发布，实际工程价值待验证。

**「可关注」** 可关注：BookNavigator 接口将“导航-学习-应用”耦合为单一交互流程，可能影响未来 agent 长文档处理与知识检索的设计范式，但当前仅停留在论文阶段。

**标签**: `#eval`, `#memory`, `#harness`

---

## AI 日报
{: #sec-ai-daily .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-daily" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-daily-1"></a>
### [Opus 5.5 设为全付费层默认](https://claude.com/resources/articles/using-claude-opus-5-5-as-your-daily-driver-for-knowledge-work) ⭐️ 8.8/10

Anthropic 宣布将 Claude Opus 5.5 设为 Pro、Max、Ultra、Team 所有付费 Claude 套餐的默认模型，官方推荐其作为研究、分析、写作等知识工作的日常主力模型。官方同步给出全系模型的定价、速度与适用场景对比：Opus 5.5 输入/输出 token 价格为每百万$4/$20，速度为中等；Haiku 5.5 定价最低（$0.10/$0.50）、速度最快，适合短平快任务；Sonnet 5.5 速度更快（$2/$10），适合有明确 brief 的轻量任务；Fable 5.2 定价最高（$8/$40），适合最复杂的开放技术任务。存在使用限制：Pro 套餐、Team 标准席位及按席位计费的 Enterprise 套餐默认额度不包含 Fable 5.2，仅限时推广活动可享，超出额度需按使用量扣费；更高定价的模型会更快消耗套餐额度；Haiku 5.5 处理超过 100k token 的长提示词时，价格会上涨至每百万$0.50/$2.50。

rss · Claude Blog · 11月12日 00:00

**「为什么重要」** 此次默认模型调整覆盖所有付费 Claude 用户，官方同步给出全系模型的选型参考，同时公开的内部测试显示 Opus 5.5 在财报分析、文档生成、图表识别等场景的输出质量与成本效率较上一代有明显提升，帮助用户根据任务复杂度平衡成本与输出质量，避免不必要的模型升级开销。

**「可关注」** 可关注：使用 Opus 5.5 时无需添加&quot;think hard&quot;&quot;think carefully&quot;类提示词，删除这类提示可加快回复速度，且无明显质量损失。

**标签**: `#model`, `#lab`, `#product`, `#policy`

---

<a id="item-ai-daily-2"></a>
### [Claude Managed Agents 推出自托管私有测试](https://claude.com/resources/articles/self-hosted-claude-managed-agents) ⭐️ 8.8/10

Anthropic 发布自托管 Claude Managed Agents 私有测试版，允许企业在自有云或本地环境运行自主构建的 agent，可完全控制凭证、会话历史存储及模型请求路由。该版本将原托管服务的全部组件（agent 控制平面、数据库、运行工具的工作节点）均部署在企业侧，当前仅开放私有测试，需联系 Anthropic 账户团队申请访问。

rss · Claude Blog · 11月12日 00:00

**「为什么重要」** 此前企业若需全栈自托管 agent 服务只能自行搭建平台，此次更新填补了该空白，满足对数据驻留、内部系统访问权限有严格要求的团队的合规需求，无需额外投入平台开发成本。

**「可关注」** 可关注：自托管版本支持将模型请求路由至 Amazon Bedrock、Google Agent Platform、Microsoft Foundry 或自有网关，会话历史可通过 OpenTelemetry 导出至现有监控工具。

**标签**: `#product`, `#lab`, `#industry`

---

<a id="item-ai-daily-3"></a>
### [Claude Meetings Beta 上线](https://claude.com/resources/articles/claude-meetings) ⭐️ 8.8/10

Anthropic 官方发布 Claude Meetings Beta 功能，Claude 可作为可见参会者加入视频会议，实时跟进对话并协助完成纪要撰写、协作文档/白板创建、会议问答等任务。目前该功能仅支持 Google Meet，优先向 Team 和 Enterprise 套餐用户开放，零数据保留（ZDR）、HIPAA 就绪配置、客户管理加密密钥（CMEK）的组织暂不适用。Beta 期间，会议笔记、转录、通话内回答免费，使用关联工具计入套餐用量，生成的文档、白板等制品免费至 2027 年 2 月 10 日。

rss · Claude Blog · 11月12日 00:00

**「为什么重要」** 该功能将 AI 助手的协作场景从会后延伸至会议实时环节，可自动完成记录、即时问答、共创制品等任务，减少参会者的手动操作负担，目前仅面向付费企业用户开放，后续将适配更多视频会议平台。

**「可关注」** 可关注：Claude Meetings 目前仅支持 Google Meet，其他会议平台适配即将上线；beta 期间生成的文档、白板等制品免费至 2027 年 2 月 10 日。

**标签**: `#lab`, `#product`

---

<a id="item-ai-daily-4"></a>
### [Claude 发布制造业专用插件](https://claude.com/resources/articles/claude-for-manufacturing) ⭐️ 8.8/10

Anthropic 官方发布面向制造业的 Claude 专用插件 Claude for Manufacturing，内置 17 项技能与 4 款工业/办公系统连接器，可辅助完成报价、质量报告、供应商请求等流程。该插件仅读取企业自有系统数据，所有输出需人工审核后才能对外发出，且不直接操控生产设备。此外 Infor 同步发布配套插件，支持通过 Claude 直接修改 Infor 系统内的采购订单、生产排程等记录，操作权限跟随用户原有 Infor 权限。

rss · Claude Blog · 11月12日 00:00

**「为什么重要」** 2025 年制造业领导委员会调查显示 79% 的制造商存在手动录入数据的行业痛点，该插件可将流程推进到人工审核节点，减少重复数据录入工作。

**「可关注」** 可关注：无对应连接器的系统可将定期导出文件存入 Microsoft 365，由 Claude 基于文件完成流程处理，且技能支持企业自定义扩展。

**标签**: `#product`, `#lab`, `#industry`

---

<a id="item-ai-daily-5"></a>
### [OpenAI 200 万美元资助儿童 AI 安全研究](https://openai.com/index/children-first-declaration) ⭐️ 7.8/10

OpenAI 官方宣布投入 200 万美元，资助 AI 与儿童安全相关研究，支持开发用于评估青少年 AI 接触风险与机会的共享工具。该投入为公开政策类资助，暂无更多技术落地细节披露。

rss · OpenAI Blog · 11月12日 00:00

**「为什么重要」** 该资助明确了 OpenAI 在青少年 AI 安全领域的布局方向，为相关风险评估工具开发提供了资金支持，是 AI 伦理与儿童保护政策领域的可核实进展，但当前仅为政策类投入，影响面有限。

**「可关注」** 可关注：OpenAI 后续推出的青少年 AI 风险与机会评估工具的技术规范与开源情况。

**标签**: `#lab`, `#policy`, `#industry`

---

<a id="item-ai-daily-6"></a>
### [GitHub 发布 Agent Skills 实践指南](https://github.blog/ai-and-ml/github-copilot/build-once-run-on-any-agent-a-practical-guide-to-agent-skills/) ⭐️ 7.8/10

GitHub 发布 Agent skills 实践指南，定义其为中心为 SKILL.md 文件的版本化可共享指令集。Agent skills 可在不同 agent 间复用，但执行依赖目标环境提供的工具、凭证与权限。指南通过 Proof Agent 与 Data Forge 两个示例，说明技能拆分、协调及项目配置外置的实践方式。

rss · GitHub Blog · 11月12日 22:54

**「为什么重要」** 该指南首次由 GitHub 官方明确 Agent skills 的结构与使用规则，为团队沉淀可复用 agent 知识提供可操作范式。对构建 coding agent 或 harness 的读者，这直接关联到如何设计可跨环境复用的 agent 能力模块。

**「可关注」** 可关注：将项目配置（如数据库、命名规范）外置到 manifest，避免硬编码到技能指令中，提升技能跨项目复用性。

**标签**: `#product`, `#industry`, `#open-source`, `#agent`

---

<a id="item-ai-daily-7"></a>
### [J.Crew 上线 Claude 造型顾问](https://claude.com/resources/articles/j-crew-style-advisor-with-claude) ⭐️ 7.8/10

J.Crew 正式上线 AI 造型工具 Style Advisor，基于 Claude Code 及多款 Claude 模型（Fable 5.1、Opus 5.5、Sonnet 5.5、Haiku 5.5）开发，目前仅在美国市场提供男女款穿搭推荐服务。该工具基于 J.Crew 自有造型师拍摄的官方造型库生成完整穿搭方案，用户可通过描述场景（如海滩婚礼、求职面试）或单件商品获取推荐，还可持续调整需求优化结果。

rss · Claude Blog · 11月12日 00:00

**「为什么重要」** 这是 Anthropic 官方披露的 Claude 企业级落地案例，展示了不同参数规模 Claude 模型按任务特性分工（复杂推理用 Fable/Opus、轻量响应用 Sonnet/Haiku）的落地路径，也为零售行业 AI 化提供了可参考的实践样本。

**「可关注」** 可关注：多模型按任务特性分工（复杂推理用大参数模型、轻量响应用小参数模型）的落地模式，可参考用于自身业务的 AI 工具开发。

**标签**: `#product`, `#industry`, `#model`

---

<a id="item-ai-daily-8"></a>
### [Claude Tag 发布创业公司使用指南](https://claude.com/resources/articles/claude-tag-guide-for-startups) ⭐️ 7.8/10

官方 Claude 博客发布 beta 版 Claude Tag 的创业公司使用指南，汇总 8 家高增长创业公司的落地实践，覆盖告警分诊、线程转 PR 等 5 类高频场景，附带可直接复用的配置与 prompt 示例。关键数据包括：NavigateAI 自 6 月已通过该功能开出 223 个 PR，其中 134 个已合并，中位合并耗时 2 小时；Kikoff 旗下 Campfire 团队曾 21 分钟完成 PR 提交并于当日合并；Orderful 借助该功能 2 天就上线了此前积压的 753 文档支持能力。

rss · Claude Blog · 11月12日 00:00

**「为什么重要」** 该指南由 Claude 官方发布，提供可落地的真实创业公司用例，能帮助资源有限的 lean 团队快速找到适配自身场景的 Claude Tag 用法，降低 beta 功能的试错成本。

**「可关注」** 可关注：优先将 Claude Tag 接入 Slack 的 on-call、告警、快速需求类频道，参考指南中提供的 prompt 模板与 8 家创业公司的场景配置快速落地。

**标签**: `#lab`, `#product`, `#industry`

---