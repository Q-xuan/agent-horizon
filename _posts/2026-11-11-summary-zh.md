---
layout: default
title: "Horizon Summary: 2026-11-11 (ZH)"
date: 2026-11-11
lang: zh
---

> 从 233 条内容中筛选出 18 条重要资讯。

<nav id="ah-toc" class="ah-toc" aria-label="目录"><span class="ah-toc-title">目录</span><ul><li><a href="#sec-harness-arch"><span class="ah-toc-name">Harness 架构</span><span class="ah-toc-count">3条</span></a></li><li><a href="#sec-agent-engineer"><span class="ah-toc-name">Agent 工程师日报</span><span class="ah-toc-count">7条</span></a></li><li><a href="#sec-ai-daily"><span class="ah-toc-name">AI 日报</span><span class="ah-toc-count">7条</span></a></li><li><a href="#sec-ai-deals"><span class="ah-toc-name">AI 羊毛</span><span class="ah-toc-count">1条</span></a></li></ul></nav>

---

**[Harness 架构](#sec-harness-arch)**
1. [browser-use 1.0.0rc5 发布](#item-harness-arch-1) ⭐️ 9.3/10
2. [browser-use 1.0.0 发布](#item-harness-arch-2) ⭐️ 8.8/10
3. [Goose v1.59.0 发布](#item-harness-arch-3) ⭐️ 7.8/10

**[Agent 工程师日报](#sec-agent-engineer)**
1. [AlphaProof Code 正式发布](#item-agent-engineer-1) ⭐️ 8.0/10
2. [持久执行：长时程智能体容错](#item-agent-engineer-2) ⭐️ 8.0/10
3. [Claude 新增白板、表格、数据看板](#item-agent-engineer-3) ⭐️ 7.0/10
4. [Sage-Taiyi 科学发现元认知架构发布](#item-agent-engineer-4) ⭐️ 7.0/10
5. [ReproBridge 论文提出可复现 ML Artifacts 工作流](#item-agent-engineer-5) ⭐️ 7.0/10
6. [Longtail-SWE 覆盖 13 种小众语言](#item-agent-engineer-6) ⭐️ 7.0/10
7. [Bielik-11B-v3.1-Instruct 发布](#item-agent-engineer-7) ⭐️ 6.0/10

**[AI 日报](#sec-ai-daily)**
1. [Anthropic 启动 IPO 路演 拟发行 8.25 亿股](#item-ai-daily-1) ⭐️ 10.0/10
2. [Claude 发布 Whiteboards、Sheets 与 Data](#item-ai-daily-2) ⭐️ 8.8/10
3. [Claude 新增 Sheets 与 Whiteboards 功能](#item-ai-daily-3) ⭐️ 8.8/10
4. [Curative 用 Claude 代理提速合同谈判](#item-ai-daily-4) ⭐️ 8.3/10
5. [OpenAI 上线 ChatGPT 商家功能](#item-ai-daily-5) ⭐️ 7.8/10
6. [OpenAI 与 Upwork 发布自由职业 AI 研究](#item-ai-daily-6) ⭐️ 7.8/10
7. [Git 2.56.1 修复 6 个安全漏洞](#item-ai-daily-7) ⭐️ 7.8/10

**[AI 羊毛](#sec-ai-deals)**
1. [小渔排班宣布永久免费](#item-ai-deals-1) ⭐️ 8.0/10

---

## Harness 架构
{: #sec-harness-arch .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-harness-arch" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-harness-arch-1"></a>
### [browser-use 1.0.0rc5 发布](https://github.com/browser-use/browser-use/releases/tag/1.0.0rc5) ⭐️ 9.3/10

browser-use 1.0.0rc5 发布，核心 agent 运行时从基于 DOM dump 的步进式动作选择改为持久 Python REPL，结合 browser-harness helpers、raw CDP 与 Pydantic AI。Python 代码量从 68,815 行降至 13,154 行，同时保留 \`Agent\`、\`Browser\`、\`Tools\`、\`run\(\)\`、\`final\_result\(\)\` 等常用 0.x API 向后兼容。默认模型切换为 Browser Use 网关的 \`bu-fast\`，默认浏览器变为 Browser Use Cloud，需显式指定 \`Browser\(&\#x27;chromium&\#x27;\)\` 使用本地 Chromium。\`run\(\)\` 默认 \`max\_steps=100\`（原 500），\`timeout=1700\` 秒，Python 3.11+ 要求；当前需显式安装 \`browser-use==1.0.0rc5\`，默认 pip 仍安装 0.13.14。

github · gregpr07 · 11月9日 23:36

**「设计要点」** 1.0 运行时采用持久 Python REPL 替代之前的无状态步进循环，agent 直接在 REPL 中编写 Python 代码调用 browser-harness 和 CDP 控制浏览器，而非每步从 DOM 快照选择预定义动作。工具层通过 Pydantic AI 绑定，支持流式 Responses 与单次瞬态重试；会话状态由 REPL 进程和 Pydantic AI 上下文管理，不再依赖 DOM dump 步进式状态管理。

**「改了什么」** 核心引擎从 DOM dump 步进式选择器重写为持久 Python REPL + raw CDP 执行模型，代码量减少 75%。默认行为全面转向 Browser Use Cloud（模型、浏览器、API key 均默认托管），本地使用需显式配置；新增类型化结果、secrets、域名限制与 web search，移除多个 0.x 选项与 extras。

**标签**: `#runtime`, `#tools`

---

<a id="item-harness-arch-2"></a>
### [browser-use 1.0.0 发布](https://github.com/browser-use/browser-use/releases/tag/1.0.0) ⭐️ 8.8/10

browser-use 1.0.0 发布，这是一个完全重写的 web agent 框架。新版本用持久化 Python REPL 直接运行在 Chrome DevTools Protocol（CDP）上，彻底移除了 0.x 版本的 DOM 序列化和 action schema 中间层。接口上，默认使用 Browser Use Cloud 浏览器和 \`bu-fast\` 模型，需设置 \`BROWSER\_USE\_API\_KEY\`；\`max\_steps\` 默认降至 100，超时 1700 秒。项目声称 benchmark 分数提升最高 33 分，成本降低 2.7–5.2 倍，速度提升 2–3 倍，代码量减少 80%。

github · gregpr07 · 11月10日 02:04

**「设计要点」** 运行时改为模型直接写 Python 代码，经持久化 REPL 通过 CDP 执行，移除 DOM 序列化与 action schema 中间层。工具层简化为直接 CDP 调用，上下文支持流式响应与自动压缩；安全提供敏感数据脱敏与域名限制，但非沙箱。

**「改了什么」** 核心架构从 action-schema 驱动改为 REPL+CDP 直连，删除 136,866 行代码。默认行为全面转向云服务：浏览器默认走 Browser Use Cloud，模型默认走 \`bu-fast\` 网关；新增结构化输出、文件上传下载、web search 和 MCP 支持，大量 0.x 配置项被移除或改为报错。

**标签**: `#runtime`, `#tools`, `#sandbox`, `#eval`

---

<a id="item-harness-arch-3"></a>
### [Goose v1.59.0 发布](https://github.com/aaif-goose/goose/releases/tag/v1.59.0) ⭐️ 7.8/10

block/goose 发布 v1.59.0。本次更新在工具层引入延迟 MCP 工具执行，子代理支持恢复已完成委托，GDK 新增停止、审批与工具钩子，ACP 支持按客户端标签过滤会话列表。GPT-Live 实时语音可配置端点、模型与密钥，同时修复会话数据库初始化、Databricks OAuth 刷新、Gemini 参数传递等七项缺陷。

github · github-actions\[bot\] · 11月10日 17:17

**「设计要点」** 运行时层面，ToolExecutionOperation 支持延迟 MCP 工具调用，会话数据库初始化与应用池隔离。工具与权限层面，goose-agent \(GDK\) 新增停止、审批与工具钩子，ACP 协议支持按客户端标签过滤会话列表。

**「改了什么」** ToolExecutionOperation 新增延迟 MCP 工具执行路径，子代理支持恢复已完成委托，GDK 暴露停止、审批与工具钩子，ACP 支持按客户端标签过滤会话。GPT-Live 端点、模型与密钥可配置，实时语音支持每启动自定义指令。修复会话数据库初始化隔离、Databricks OAuth 过期刷新、Gemini 参数传递等七项缺陷。

**标签**: `#mcp`, `#subagents`, `#permissions`, `#runtime`, `#tools`

---

## Agent 工程师日报
{: #sec-agent-engineer .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-agent-engineer" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-agent-engineer-1"></a>
### [AlphaProof Code 正式发布](https://deepmind.google/blog/introducing-alphaproof-code/) ⭐️ 8.0/10

2026 年 11 月 10 日，DeepMind 发布 AI 证明代理 AlphaProof Code，可迭代遍历代码库，自动生成并执行 Lean 或 Rocq 语言的正式证明，用于验证软件实现正确性。社区已出现对其验证结果的质疑：有用户指出其对含历史 bug 的代码库验证后得出零 bug 结论，怀疑是证明定理错误或仅验证了窄范围属性。该工具面向软件可靠性、coding agent 正确性保证等场景，对 coding agent 评估、编排等验证工作流有潜在影响。

hackernews · Google DeepMind · 11月10日 12:11 · [社区讨论](https://news.ycombinator.com/item?id=50439193)

**「为什么重要」** 该工具是 AI 辅助形式化方法在代码验证领域的落地尝试，已发布的官方能力对 coding agent 可靠性、自动化验证工作流有直接参考价值。但其验证结果的完备性尚未得到社区验证，相关质疑是否成立仍需进一步观察。

**「可关注」** 可关注：AI 生成形式化证明的完备性风险，以及自动验证流程中“证明本身正确性”的校验缺口。

**「评论」** 社区对工具价值存在分歧：部分用户认可 AI 辅助形式化验证的前景，认为未来未验证软件会像明文 HTTP 一样被淘汰；但也有用户质疑其验证结果的可靠性，同时有实验者反馈 AI 生成的 Lean 代码存在逻辑错误或“证明作弊”问题，自动化流程中难以察觉这类缺陷。

**标签**: `#coding-agent`, `#eval`, `#orchestration`

---

<a id="item-agent-engineer-2"></a>
### [持久执行：长时程智能体容错](https://martinfowler.com/articles/durable-execution-agents.html) ⭐️ 8.0/10

2026 年 11 月 10 日，Martin Fowler 站点发布 Kiran Prakash 撰写的文章，介绍面向长时程智能体的持久执行（durable execution）编程模式。该模式针对任务周期可达数天到数周、涉及多轮人与外部系统交互的智能体场景，解决进程崩溃、网络故障、外部行为异常等导致的任务中断问题。核心机制是运行时记录所有与外部交互步骤的结果，故障后重跑程序时跳过已完成步骤，从记录重建程序状态继续执行，无需从头启动任务。该模式直接影响智能体编排框架与 harness 的设计思路。

rss · Martin Fowler · 11月10日 14:10

**「为什么重要」** 当前长时程智能体在真实运行中普遍面临任务中断后恢复成本高的问题，该模式提供了可落地的状态持久化与步骤跳过机制，为相关系统的容错设计提供了可直接参考的编程模型范式。

**「可关注」** 可关注：长时程智能体的容错设计可将外部交互步骤的结果持久化，故障后通过重跑跳过已完成步骤、重建状态恢复执行，无需从头启动任务。

**标签**: `#orchestration`, `#harness`, `#memory`

---

<a id="item-agent-engineer-3"></a>
### [Claude 新增白板、表格、数据看板](https://claude.com/resources/articles/sheets-whiteboards-data) ⭐️ 7.0/10

2026 年 11 月 10 日，Anthropic 在 Claude 平台原生上线白板、电子表格、数据看板三类协作工具，用户无需导出到第三方工具即可在平台内编辑项目产物、开展团队协作。该功能直接嵌入 Claude 对话工作流，覆盖此前需跨工具流转的项目文档、数据看板等场景。目前未公开具体版本号、灰度范围与功能限制。

hackernews · Yorothegoat · 11月10日 17:55 · [社区讨论](https://news.ycombinator.com/item?id=50443716)

**「为什么重要」** 这标志着 AI 模型厂商从提供模型能力向全栈 SaaS 工具层延伸，已明确覆盖项目协作场景。目前尚未证实该功能是否会替代第三方专业工具，但已对依赖 API 提供协作能力的客户形成潜在竞争信号。

**「可关注」** 可关注：AI 厂商推出的原生工具通常先作为跨工具流转的轻量 fallback，长期需观察其是否会覆盖专业工具的核心场景，进而影响 agent 工作流的工具选型。

**「评论」** 社区共识是新工具初期大概率仅作为快速查看编辑的 fallback，难以替代 Figma 等专业工具。分歧在于部分用户认为这是模型厂商侵蚀 API 客户业务空间的战略，也有开发者提出应推动轻量化文档格式适配 agent 工作流。

**标签**: `#coding-agent`, `#orchestration`, `#toolchain`

---

<a id="item-agent-engineer-4"></a>
### [Sage-Taiyi 科学发现元认知架构发布](https://huggingface.co/papers/2611.12762) ⭐️ 7.0/10

2026 年 11 月 10 日 Hugging Face 每日论文收录了 Sage-Taiyi 相关预印本，该研究提出面向科学发现智能体的元认知架构 Sage-Taiyi，以及跨学科科学构思评估基准 Taiyi-Bench。Taiyi-Bench 包含 265 个任务，覆盖 10 个学科，任务来源为 50 篇已发表论文，Sage-Taiyi 在该基准全部 8 项历史复现与开放构思指标上排名第一，总体得分 54.0，对比最强基线 AI Scientist-v2 的 47.9 有提升，同时在两个外部科学构思基准上表现良好。该研究聚焦科学发现窄场景，未提供通用生产工具，也未涉及主流智能体的突破性变更，原文末尾提及专家指导的合作相关内容但未完整展示。

rss · Hugging Face Daily Papers · 11月10日 00:00

**「为什么重要」** 该研究提供了元认知智能体编排、累积知识记忆设计的可参考思路，以及标准化的跨学科科学构思评估基准，对从事科研智能体、智能体评估的工程师有直接参考价值。目前相关结论仅验证于科学发现场景，尚未证实可迁移到通用智能体场景。

**「可关注」** 可关注 Sage-Taiyi 中“显式监控与调控证据、假设、未解问题，进而调整研究目标、选择可复用推理方法”的元认知设计，以及 Taiyi-Bench 的跨学科评估维度设计，可参考到科研类智能体的编排与评估工作中。

**标签**: `#eval`, `#orchestration`, `#memory`

---

<a id="item-agent-engineer-5"></a>
### [ReproBridge 论文提出可复现 ML Artifacts 工作流](https://huggingface.co/papers/2611.08452) ⭐️ 7.0/10

2026 年 11 月 10 日，Hugging Face Daily Papers 收录论文《ReproBridge: Building Reproducibility into ML Research Artifacts》。该工作提出 ReproBridge agent workflow，用于构建包含精炼代码库、环境配置、实验启动器和复现指南的标准化工件。配套的 ReproBridge-Bench 包含 1,029 个任务，覆盖 36 篇论文的 387 个实验，每个任务提供 5 个人工验证的参考分数，用于评估 coding agent 复现 ML 实验的能力。

rss · Hugging Face Daily Papers · 11月10日 00:00

**「为什么重要」** 该 benchmark 为 coding agent 在 ML 实验复现场景提供了可验证的评估标准。人工验证的参考分数为评估提供了可复现的基准，减少了自动化评分的不确定性。

**「可关注」** 可关注：ReproBridge-Bench 的 1,029 个任务及人工验证参考分数可作为 coding agent harness 的标准化测试集，用于量化 agent 在 ML 实验复现中的端到端能力。

**标签**: `#eval`, `#coding-agent`, `#orchestration`, `#harness`

---

<a id="item-agent-engineer-6"></a>
### [Longtail-SWE 覆盖 13 种小众语言](https://huggingface.co/papers/2611.10304) ⭐️ 7.0/10

Hugging Face Daily Papers 于 2026-11-10 发布 Longtail-SWE 基准。该基准包含 202 个仓库级 SWE 任务，覆盖 Clojure、Dart、Elixir、Erlang、F\#、Haskell、Julia、Kotlin、Lua、OCaml、R、Scala 和 Swift 共 13 种代表性不足的编程语言。任务通过 solver-judge-repairer 管道构建：solver 尝试解决候选任务，judge 审查任务描述、求解轨迹和测试结果，并指导修订测试和描述，以修正拒绝有效替代实现或接受错误解决方案的测试。

rss · Hugging Face Daily Papers · 11月10日 00:00

**「为什么重要」** 该基准填补了 13 种小众语言生态系统缺乏高质量仓库级 SWE 评估资源的空白，为 coding agent 开发和评估工具构建提供了可验证的任务集。

**「可关注」** 可关注：solver-judge-repairer 管道提供了一种可复用的任务构建流程，可用于其他小众语言生态系统的评估基准开发。

**标签**: `#eval`, `#coding-agent`

---

<a id="item-agent-engineer-7"></a>
### [Bielik-11B-v3.1-Instruct 发布](https://www.reddit.com/r/LocalLLaMA/comments/1xsrg0l/speakleashbielik11bv31instruct_hugging_face/) ⭐️ 6.0/10

2026 年 11 月 10 日，Reddit 用户/u/jacek2023 发帖官宣开源 11B 多语言大模型 Bielik-11B-v3.1-Instruct，该模型是 Bielik 11B v3 系列的更新版本，强化指令遵循、工具使用与推理能力，支持 56 种语言，侧重欧洲语言与波兰语优化。模型训练依托 PLGrid 环境下的计算资源（grant 号 PLG/2026/019559），在 Athena、Helios 超算及欧盟 EuroHPC Joint Undertaking 资助的 Gaia AI Factory 完成，训练流程为 500B token 预训练、26M 样本 SFT、14 个环境下的修改版 GRPO 强化学习，基于 SpeakLeash 自研 ALLaMo 框架实现，采用 Apache 2.0 协议开源，已提供 GGUF 格式权重与在线聊天入口，项目后续将发布决策模型与 dflash 系列模型。

reddit · r/LocalLLaMA · /u/jacek2023 · 11月10日 16:30

**「为什么重要」** 该模型针对 AI Agent 核心能力做定向优化且完全开源，覆盖多语言尤其是欧洲小语种场景，为本地化轻量级 Agent 开发提供了可复用的开源基座。

**「可关注」** 可关注：该模型采用三阶段训练流程（500B token 预训练+26M 样本 SFT+14 环境修改版 GRPO 强化学习），基于自研 ALLaMo 框架实现，训练数据覆盖 56 种语言，其轻量级多语言 Agent 模型的训练方案有参考价值。

**标签**: `#coding-agent`, `#tool-use`, `#open-source`

---

## AI 日报
{: #sec-ai-daily .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-daily" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-daily-1"></a>
### [Anthropic 启动 IPO 路演 拟发行 8.25 亿股](https://www.anthropic.com/news/roadshow-launch) ⭐️ 10.0/10

Anthropic 正式启动拟议的首次公开募股（IPO）路演，计划发行 8.25 亿股 A 类普通股，其中 8.013 亿股由 Anthropic 发行，2364.86 万股由现有股东出售，公司不会获得现有股东出售股份的收益。发行价预计为每股 70 至 78 美元，拟在纳斯达克全球精选市场上市，股票代码为“ANT”，同时将授予承销商 30 天期权，可额外购买最多 1.2375 亿股。该发行仅通过招股说明书进行，相关注册声明已提交美国证券交易委员会但尚未生效，在注册声明生效前不得出售证券或接受购买要约。

rss · Anthropic News · 11月10日 00:00

**「为什么重要」** 这是 Anthropic 公开上市进程的关键节点，明确的发行规模、价格区间和上市安排为后续公开市场交易提供了具体基准。

**「可关注」** 可关注：Anthropic 拟上市股票代码为 ANT，发行价区间 70-78 美元/股，后续可留意其注册声明生效及正式发行公告。

**标签**: `#lab`, `#industry`

---

<a id="item-ai-daily-2"></a>
### [Claude 发布 Whiteboards、Sheets 与 Data](https://claude.com/resources/articles/sheets-whiteboards-data) ⭐️ 8.8/10

Anthropic 于 2026 年 11 月 10 日发布 Claude Whiteboards 与 Claude Sheets beta 版，同时将原 Dashboards 正式上线为 Claude Data，所有付费计划可用。三个功能均支持网页、桌面、移动端：Whiteboards 是团队实时协作白板，支持 Claude 整理脑暴内容、转文档/幻灯片或导出至 Lucid、Miro 等工具；Sheets 是协作表格，支持 Claude 生成带公式、格式的表格，可导出 .xlsx/CSV 或对接 Airtable、Asana、monday.com、Smartsheet 等工具，当前功能较基础，后续将逐步扩展；Claude Data 支持数据故事、认证查询、实时共享，缓存与变更追踪已上线，认证查询和实时共享仍处 beta，合作伙伴包括 Amplitude、Mixpanel、Omni、PostHog、Sigma。此外，交互连接器现支持全屏或侧边打开，用户可在 Adobe、Atlassian、Box、Notion 等工具中直接操作，或要求 Claude 协助修改。Enterprise 计划下 Whiteboards 和 Sheets 默认关闭，Claude Data 默认于 2026 年 11 月 19 日开启，管理员可随时在组织设置的 Artifacts 项中调整开关。

rss · Claude Blog · 11月10日 00:00

**「为什么重要」** 此前用户在 Claude 完成项目输出后需切换到其他工具协作，Claude 无法实时跟进项目变更，此次更新将协作场景纳入 Claude 平台，减少了跨工具切换成本，也让 Claude 能够持续参与项目迭代。

**「可关注」** 可关注：Claude Data 已支持按仪表盘配置缓存刷新频率，可降低重复查询的加载耗时。

**标签**: `#product`, `#lab`, `#industry`

---

<a id="item-ai-daily-3"></a>
### [Claude 新增 Sheets 与 Whiteboards 功能](https://claude.com/resources/articles/more-ways-to-work-with-claude-sheets-whiteboards-and-interactive-connectors) ⭐️ 8.8/10

2026 年 11 月 10 日，Anthropic 宣布扩展 Claude 平台能力，新增 Claude Sheets、Claude Whiteboards、Claude Data 三种协作工件类型，同时升级基于 MCP 协议的交互连接器，支持合作伙伴将 Adobe、Atlassian 等应用直接内嵌至 Claude 内操作，Salesforce、NetSuite、Workday 插件已内置对应场景技能。目前 Claude Marketplace 已收录超 9000 个连接器与插件，Claude Data 的团队数据定义功能、上述两款插件及 Claude auto-connect 功能均处于 beta 阶段，仅对符合条件的 Team 及 Enterprise 计划开放，即将推出的 Claude Meetings 功能将支持通话中自动记录纪要并更新团队文档。

rss · Claude Blog · 11月10日 00:00

**「为什么重要」** 本次更新标志着 Claude 从开发者工具向全团队协作平台扩展，非技术团队可通过无代码方式将领域知识转化为自动化工具，同时企业级权限管控与合规能力的补齐，降低了大型组织接入使用的门槛。

**「可关注」** 可关注：基于 MCP 协议的交互连接器已支持应用内嵌操作，企业版新增单会话隔离虚拟机与合规 API，可对接超 100 种安全工具。

**标签**: `#lab`, `#product`, `#industry`, `#open-source`

---

<a id="item-ai-daily-4"></a>
### [Curative 用 Claude 代理提速合同谈判](https://claude.com/resources/articles/how-curative-is-building-a-national-provider-network-with-agents-on-claude) ⭐️ 8.3/10

Claude 官方博客公开健康险企业 Curative 的 AI 应用案例：Curative 基于 Claude 平台构建分层代理体系，核心代理 Gwen 覆盖医疗提供者合同从初步接洽到签署的全流程，谈判效率较 2025 年提升约 50 倍，每周可完成 2000 至 2400 份新合同签署，2025 年全年仅签署 2100 份。每份合同处理约消耗 2000 万 token，成本约为最初方案的十分之一，配套费率审校、沟通预检、资质校验等辅助代理，非标准定价转人工审批，其合同团队规模从 45 人增长至 55 人，人均效率提升 2.5 倍，人与代理共享考核目标。

rss · Claude Blog · 11月10日 00:00

**「为什么重要」** 该案例为 Claude 官方披露的垂直行业落地实践，展示了代理体系在复杂商业谈判、人机协作场景中的可落地效果，对 AI 应用场景选型与代理设计有参考价值。

**「可关注」** 可关注：Curative 按任务类型匹配不同 Claude 模型（Opus 负责核心谈判、Sonnet 负责费率审校、Haiku 负责沟通预检）、单次运行隔离避免跨 deal 记忆污染、用 Python 工具链处理合同红文修改的代理设计思路。

**标签**: `#lab`, `#industry`, `#product`, `#model`

---

<a id="item-ai-daily-5"></a>
### [OpenAI 上线 ChatGPT 商家功能](https://openai.com/index/introducing-businesses-chatgpt) ⭐️ 7.8/10

OpenAI 于 2026 年 11 月 10 日发布 ChatGPT 商家功能（Businesses in ChatGPT）。该功能支持商家在 ChatGPT 平台内管理自身公开信息、获取自身在平台中曝光情况的洞察数据，还可将用户对商家的兴趣转化为实际转化动作。目前官方未披露该功能的具体限制与覆盖范围。

rss · OpenAI Blog · 11月10日 10:00

**标签**: `#product`, `#lab`, `#industry`

---

<a id="item-ai-daily-6"></a>
### [OpenAI 与 Upwork 发布自由职业 AI 研究](https://openai.com/index/ai-effect-on-freelance-work) ⭐️ 7.8/10

2026 年 11 月 10 日，OpenAI 与 Upwork 联合发布新研究，显示 AI 正在重塑自由职业市场：需求结构发生转移，出现新的技能组合要求，AI 相关自由职业项目的预算和工时均有所提升。

rss · OpenAI Blog · 11月10日 07:00

**「为什么重要」** 该研究由头部 AI 实验室与头部自由职业平台联合开展，为评估 AI 对实际劳动力市场的影响提供了可参考的一手实证依据。

**「可关注」** 可关注：AI 相关自由职业项目的预算、工时增长趋势，以及新兴的技能组合要求。

**标签**: `#lab`, `#industry`, `#research`

---

<a id="item-ai-daily-7"></a>
### [Git 2.56.1 修复 6 个安全漏洞](https://github.blog/open-source/git/git-security-vulnerabilities-announced-7/) ⭐️ 7.8/10

Git 项目正式发布 Git 2.56.1 及 2.50.2 至 2.55.1 共 6 个维护版本的向后移植补丁，修复 6 个安全漏洞。漏洞涵盖递归克隆任意代码执行、协议 v2 路径遍历、GPG 签名剥离栈损坏、二进制补丁越界读取、大体积合并堆损坏、fast-import 流未授权文件系统访问 6 类问题。GitHub 已在其公有云、企业云服务中完成修复部署，GitHub Enterprise Server 需升级至 3.19.15、3.20.11、3.21.9、3.22.4 版本，同时 GitHub Desktop、Copilot 应用、Codespaces 及 Actions 也将同步更新带补丁的 Git 版本。

rss · GitHub Blog · 11月10日 18:00

**「为什么重要」** 这些漏洞覆盖递归克隆、合并、补丁应用、fast-import 等高频开发场景，可被利用触发代码执行、内存损坏或未授权文件访问，影响本地开发环境、代码托管平台及 CI/CD 流程，修复覆盖全系列维护版本，对开发工具链安全至关重要。

**「可关注」** 可关注：使用 2.50.2 至 2.55.1 维护版本的用户需升级至对应补丁版本；处理不可信 fast-import 流的场景默认已禁止相关不安全特性，需显式添加--allow-unsafe-features 参数才可启用。

**标签**: `#open-source`, `#industry`

---

## AI 羊毛
{: #sec-ai-deals .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-deals" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-deals-1"></a>
### [小渔排班宣布永久免费](https://www.appinn.com/xiaoyu-shift-calendar-free/) ⭐️ 8.0/10

你看到的内容可能由第三方 AI 基于小众软件文章提炼总结而成，可能与原文真实意图存在偏差。不代表小众软件观点和立场。请&lt;a href=&quot;https://www.appinn.com/xiaoyu-shift-calendar-free/&quot; target=&quot;\_blank&quot;&gt;点击链接阅读原文&lt;/a&gt;细致比对和校验。&lt;br /&gt;&lt;br /&gt;小渔排班是一款面向轮班、倒班工作者的 iOS 日历应用，自 2026 年 10 月起全功能永久免费，无广告、无订阅，仅保留自愿支持开发者的选项。该应用已开发 8 年，支持班次批量排班、班次闹钟、工时薪资统计、班表导出分享、iCloud 同步、多设备（iPhone/iPad/Apple Watch）支持及自定义主题等功能。

rss · 小众软件 · 11月10日 14:48

**「为什么重要」** 该应用此前为付费应用，曾登顶国区 App Store 效率付费榜第 2 名，如今永久免费可让倒班工作者零成本获取全功能排班工具，且开发者明确表示会继续长期维护更新。

**「可关注」** 可关注：该应用仅支持 iOS 生态，无安卓及跨平台版本，适合有倒班排班需求的 iOS 用户使用。

**标签**: `#free-tier`, `#promo`

---