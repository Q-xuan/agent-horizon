---
layout: default
title: "Horizon Summary: 2026-11-17 (ZH)"
date: 2026-11-17
lang: zh
---

> 从 201 条内容中筛选出 15 条重要资讯。

<nav id="ah-toc" class="ah-toc" aria-label="目录"><span class="ah-toc-title">目录</span><ul><li><a href="#sec-harness-arch"><span class="ah-toc-name">Harness 架构</span><span class="ah-toc-count">3条</span></a></li><li><a href="#sec-agent-engineer"><span class="ah-toc-name">Agent 工程师日报</span><span class="ah-toc-count">4条</span></a></li><li><a href="#sec-ai-daily"><span class="ah-toc-name">AI 日报</span><span class="ah-toc-count">8条</span></a></li></ul></nav>

---

**[Harness 架构](#sec-harness-arch)**
1. [openai-agents-python v0.24.0-alpha.8 发布](#item-harness-arch-1) ⭐️ 7.8/10
2. [openai-agents-js v0.22.0-alpha.3 发布](#item-harness-arch-2) ⭐️ 7.8/10
3. [adk-go v2.8.0 发布](#item-harness-arch-3) ⭐️ 7.8/10

**[Agent 工程师日报](#sec-agent-engineer)**
1. [HF 每日论文 MIRIX-2.0 多智能体记忆系统](#item-agent-engineer-1) ⭐️ 7.0/10
2. [GH-AWTrace 数据集发布](#item-agent-engineer-2) ⭐️ 7.0/10
3. [HF 日报：MEM-SQL HARE 基准](#item-agent-engineer-3) ⭐️ 6.0/10
4. [HF Daily Papers：多智能体对齐](#item-agent-engineer-4) ⭐️ 6.0/10

**[AI 日报](#sec-ai-daily)**
1. [ChatGPT 医疗版新增计算机代理与跨软件插件](#item-ai-daily-1) ⭐️ 8.8/10
2. [OpenAI 扩展学术研究者免费 ChatGPT 计划](#item-ai-daily-2) ⭐️ 7.8/10
3. [OpenAI 上线儿童网络安全工具](#item-ai-daily-3) ⭐️ 7.8/10
4. [OpenAI 与 LVMH 媒体部门合作](#item-ai-daily-4) ⭐️ 7.8/10
5. [OpenAI 嵌入式评估首阶段启动](#item-ai-daily-5) ⭐️ 7.8/10
6. [OpenAI 推进医疗团队计算机使用代理](#item-ai-daily-6) ⭐️ 7.8/10
7. [OpenAI 与 The King’s Trust 启动百万英镑合作](#item-ai-daily-7) ⭐️ 7.8/10
8. [TPU 同策略 RL 实现零数值差异方案](#item-ai-daily-8) ⭐️ 7.8/10

---

## Harness 架构
{: #sec-harness-arch .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-harness-arch" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-harness-arch-1"></a>
### [openai-agents-python v0.24.0-alpha.8 发布](https://github.com/openai/openai-agents-python/releases/tag/v0.24.0-alpha.8) ⭐️ 7.8/10

OpenAI 官方发布 Python Agents SDK v0.24.0-alpha.8。本次 alpha 版本新增工具调用执行前审批（支持会话级决策记忆）、自定义模型客户端（兼容异步 Responses、Chat Completions、LiteLLM、AnyLLM 及自定义适配器）、Realtime 语音会话（支持服务器 WebSocket、浏览器 WebRTC 和 SIP 接入）三项核心能力。同时扩展检查点恢复机制，支持保存待处理工具请求与审批状态，并新增 ARM64 Linux wheel。

github · markstuart-oai · 11月16日 04:39

**「设计要点」** 运行时采用原生工具循环，模型客户端与应用层解耦，支持应用自有适配器。存储层通过 CustomStorage 抽象对接 Redis、MongoDB、SQLAlchemy 和 Dapr Redis 等后端，权限控制由应用回调执行，工具审批状态可在会话内记忆。

**「改了什么」** 新增 FunctionToolApprovalRequest/Decision 实现工具审批，agents.realtime.native 提供原生语音 API，Application-owned model client 扩展模型接入，SQLAlchemySQLiteSessionStore 提供同步 SQLite 存储，TraceOptions.group\_id 支持提示词缓存路由分组，Agent.as\_tool\(\) 与 Agent.decide\(\) 补充代理协作能力。Linux 包新增 ARM64 wheel，要求 glibc 2.28+。

**标签**: `#tools`, `#permissions`, `#runtime`, `#memory`

---

<a id="item-harness-arch-2"></a>
### [openai-agents-js v0.22.0-alpha.3 发布](https://github.com/openai/openai-agents-js/releases/tag/v0.22.0-alpha.3) ⭐️ 7.8/10

openai-agents-js v0.22.0-alpha.3 是 OpenAI 官方 Agent SDK 的预发布版本。本次发布引入类型化决策（Typed Decisions）用于 agent 控制流与 handoff，新增 \`ResponsesModel\`、\`ChatCompletionsModel\`、\`AiSdkModel\` 三种应用自有模型后端适配器，并将 Native Realtime/Voice 扩展至 Node.js、浏览器、React Native 和 Workers 运行时。LocalStorage 历史管理新增命名配置文件、查询、编辑与分叉能力，本地执行器则新增只读工作区与可选的 \`trusted\_workspace\_write\` 权限。Linux 捆绑包要求 glibc 2.39 与 OpenSSL 3，Windows x64 捆绑包要求 VC++ Redistributable，Starter 检查使用 Node.js 24。

github · markstuart-oai · 11月16日 21:06

**「设计要点」** 运行时层覆盖 Node.js、浏览器、React Native 与 Workers。工具层通过原生工具命名空间和 MCP 集成实现细粒度权限控制，记忆层采用 LocalStorage 配置文件管理对话历史与检查点，权限模型通过 \`trusted\_workspace\_write\` 和沙盒恢复的 \`resumeAuthority\` 约束写入范围。

**「改了什么」** 相对上一版，agent 控制流新增类型化决策与 handoff 路由；模型层支持应用自有后端适配器及流式输出；语音能力跨平台扩展并新增音频输入、响应时序与 SIP 控制；历史管理支持命名配置、查询、编辑与分叉；工具回调默认并发执行，需通过 \`maxFunctionConcurrency: 1\` 控制竞态；Session 的 \`ifBusy\` 选项从忽略变为显式拒绝；序列化沙盒恢复需额外声明受信任绑定；新增 \`beforeComplete\` 钩子与 \`turn.acceptedText\(\)\` 输出检查。

**标签**: `#runtime`, `#memory`, `#subagents`, `#planning`

---

<a id="item-harness-arch-3"></a>
### [adk-go v2.8.0 发布](https://github.com/google/adk-go/releases/tag/v2.8.0) ⭐️ 7.8/10

Google 官方发布 adk-go v2.8.0。本次更新包含配置加载的破坏性变更：agent 与 workflow 的配置引用不再接受绝对路径，且配置目录内任何符号链接都会阻止引用加载，影响 Kubernetes ConfigMaps、Bazel runfiles、Nix store 等部署场景，需将挂载复制为真实文件目录（如 cp -rL）。同时新增内存服务 artifact:// 引用支持、服务端 OAuth2 用户同意流、工具请求终端用户登录、Agent Runtime 流式查询客户端、Vertex AI RAG 内存服务、OTLP 与 Google Cloud 遥测导出、BigQuery 工具集及 MCP 工具转换能力。

github · adk-go-bot · 11月16日 15:05

**「设计要点」** adk-go 作为 Go 语言 agent harness，在 v2.8.0 中收紧配置加载规则，统一拒绝 agent 与 workflow 引用中的绝对路径及配置目录内符号链接，以降低路径遍历风险。运行时新增 OAuth2 同意流与工具级认证请求机制，内存服务支持 artifact 引用与 Vertex AI RAG 集成，遥测层接入 OTLP 标准协议，工具层扩展 MCP 与 BigQuery 集成。

**「改了什么」** 配置加载逻辑收紧：workflow edge references 与 agent references 统一拒绝绝对路径及配置目录内符号链接，需提前将挂载复制为真实文件。新增内存服务 artifact:// 引用、服务端 OAuth2 同意流、工具请求用户登录、Agent Runtime 流式查询、Vertex AI RAG 内存服务、OTLP/Google Cloud MeterProvider、BigQuery 工具集及 ToMCPTool 转换器。

**标签**: `#runtime`, `#permissions`, `#config`

---

## Agent 工程师日报
{: #sec-agent-engineer .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-agent-engineer" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-agent-engineer-1"></a>
### [HF 每日论文 MIRIX-2.0 多智能体记忆系统](https://huggingface.co/papers/2611.12068) ⭐️ 7.0/10

2026 年 11 月 16 日，Hugging Face 每日论文栏目发布 MIRIX-2.0 多智能体 LLM 智能体记忆系统，针对长期记忆需训练、整合易丢细节、全量存储检索成本高的痛点设计。该系统在 5 个 QA 与智能体任务基准中的 4 个取得最优表现：LoCoMo 准确率达 91.4%，LongMemEval-S 达 72.6%，领先最强基线 14.3 分；关闭 AutoDream 组件时，单跳与多跳文档 QA 较 HyperMem 分别提升 31.0、22.0 分；作为过程记忆在 ALFWorld、WebShop 上平均成功率最高，MetaClaw-Bench 达 49.2%。当前公开内容截断，完整技术实现细节未披露，相关结果供从事智能体记忆、评估组件开发的工程师参考。

rss · Hugging Face Daily Papers · 11月16日 00:00

**「为什么重要」** 已发生的部分是 MIRIX-2.0 在主流记忆与智能体任务基准上给出了可量化的性能增益，覆盖了 QA 检索与过程记忆两类核心场景；尚未证实的是其性能能否泛化到更多真实复杂智能体场景，以及完整实现公开前结果无法独立复现。

**「可关注」** 可关注：当前公开的性能报告未披露 AutoDream 等核心组件的作用机制与落地成本，可待完整技术细节公开后评估其可复现性与实际部署价值。

**标签**: `#memory`, `#eval`, `#multi-agent`

---

<a id="item-agent-engineer-2"></a>
### [GH-AWTrace 数据集发布](https://huggingface.co/papers/2611.06866) ⭐️ 7.0/10

2026 年 11 月 16 日 Hugging Face 每日论文聚合介绍了一篇 arXiv 预印本，发布 GH-AWTrace 大规模 GitHub 智能体工作流执行日志数据集。该数据集包含 25014 条已验证工作流、4112526 条运行记录、562877 份非空执行日志，覆盖 5051 个仓库，链接工作流定义、运行记录与运行时日志，数据留存受 GitHub 日志保留策略限制。它填补了现有研究仅关注工作流定义与输出、缺乏运行时执行证据的空白，为智能体执行故障、工具使用、代理委托等研究提供真实生产 Trace 数据，可用于智能体评测、可观测性、工作流编排优化方向，但原文末尾截断，未披露性能对比或深度技术排查细节。

rss · Hugging Face Daily Papers · 11月16日 00:00

**「为什么重要」** 该数据集首次公开大规模 GitHub 智能体工作流的真实运行时执行证据，解决了此前研究缺乏生产环境 Trace 数据的痛点；但目前仅公开数据集说明，无配套性能对比或技术排查结论，实际研究价值待后续验证。

**「可关注」** 可关注：该数据集包含工具拒绝、代理委托、执行失败的真实生产日志，可直接用于智能体执行故障排查与工具使用行为分析。

**标签**: `#eval`, `#observability`, `#orchestration`

---

<a id="item-agent-engineer-3"></a>
### [HF 日报：MEM-SQL HARE 基准](https://huggingface.co/papers/2611.18338) ⭐️ 6.0/10

2026 年 11 月 16 日，Hugging Face Daily Papers 分享了一篇 Text-to-SQL 领域新论文，提出面向历史查询复用评估的基准 HARE 与内存增强方法 MEM-SQL。HARE 包含 1600 个请求，源自 4 个数据集共 823 个已验证查询，标注了请求保留的 SQL 组件与所需编辑，可区分全查询适配与部分复用场景。当前公开的论文摘录未披露 MEM-SQL 的完整技术细节、性能结果与可复现资源，相关内容仅对数据库交互类 Agent 的内存系统设计有窄范围参考价值。

rss · Hugging Face Daily Papers · 11月16日 00:00

**「为什么重要」** 该工作首次系统提出面向历史 SQL 查询复用的评估基准，为数据库交互类 Agent 的序列化工具调用效果评估提供了新的度量维度。但当前公开内容仅为论文摘要，完整技术路径与性能表现尚未得到验证，实际工程参考价值待后续完整论文发布后确认。

**「可关注」** 可关注：现有数据库交互类 Agent 的评估基准普遍忽略历史查询复用场景，若相关场景与业务匹配，可跟踪 HARE 基准的完整评估体系与 MEM-SQL 的内存复用设计。

**标签**: `#eval`, `#memory`

---

<a id="item-agent-engineer-4"></a>
### [HF Daily Papers：多智能体对齐](https://huggingface.co/papers/2611.17820) ⭐️ 6.0/10

2026 年 11 月 16 日 Hugging Face Daily Papers 收录一篇多智能体 LLM 对齐迁移预印本，研究单智能体对齐训练无法迁移到多智能体团队的问题，聚焦 2 个软件工程任务（脓毒症分诊、新闻推荐）和 10 个咨询提案生成任务，当前获 HF Daily Papers 12 次点赞。目前披露 3 项部分发现：单/团队安全差距与模型能力无明确正相关，Anthropic Mythos Preview 在不同任务上差距表现相反；互评、群聊协调等自然干预无法稳定让团队对齐到单智能体行为；第三项发现内容被截断。该预印本仅公开部分内容，无完整结论、可落地方案或性能数据。

rss · Hugging Face Daily Papers · 11月16日 00:00

**「为什么重要」** 该研究针对多智能体对齐迁移这一 agent 工程师关注的核心问题，已披露的实证结果提示模型能力相关安全差距、常见自然干预的有效性存在不确定性，但完整研究结论尚未公开，暂只能作为待跟进的研究方向。

**「可关注」** 可关注：当前多智能体场景下，单智能体对齐训练的迁移效果不稳定，互评、群聊协调等常见干预手段未在实证中表现出稳定的对齐修复效果，需警惕直接复用单智能体对齐方案到多智能体团队。

**标签**: `#orchestration`, `#eval`, `#coding-agent`

---

## AI 日报
{: #sec-ai-daily .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-daily" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-daily-1"></a>
### [ChatGPT 医疗版新增计算机代理与跨软件插件](https://openai.com/index/more-ways-to-move-care-forward-with-chatgpt-for-healthcare) ⭐️ 8.8/10

OpenAI 发布 ChatGPT 医疗健康版新功能。新增计算机使用代理、改进临床答案，以及可跨医疗软件运行的新插件。这些功能旨在让 AI 直接在医疗系统中执行实际操作，而非仅提供文本回复。

rss · OpenAI Blog · 11月16日 06:00

**「为什么重要」** 医疗健康是 AI 落地的核心垂直场景。跨软件插件与计算机代理的引入，可能改变临床工作流中系统切换与手动操作的成本结构。

**「可关注」** 可关注：医疗垂直 agent 的跨系统集成与操作自动化趋势。

**标签**: `#lab`, `#product`, `#industry`

---

<a id="item-ai-daily-2"></a>
### [OpenAI 扩展学术研究者免费 ChatGPT 计划](https://openai.com/index/expanding-chatgpt-for-academic-researchers) ⭐️ 7.8/10

OpenAI 官方宣布扩展 ChatGPT for Academic Researchers 计划，向全球 20 万名学术研究者免费提供前沿模型访问权限。本次扩展大幅提升了学术群体的免费前沿模型覆盖规模，是 OpenAI 学术访问政策的重大调整。

rss · OpenAI Blog · 11月16日 17:00

**「为什么重要」** 这是头部 AI 实验室首次面向全球学术研究者大规模免费开放前沿模型，显著降低了学术场景使用前沿模型的成本与访问门槛。

**「可关注」** 可关注：面向学术场景的 AI 模型免费开放政策正从有限试点转向规模化覆盖，这类政策调整可能影响学术场景的 AI 工具选型。

**标签**: `#openai`, `#product`, `#policy`, `#industry`

---

<a id="item-ai-daily-3"></a>
### [OpenAI 上线儿童网络安全工具](https://openai.com/index/strengthening-online-child-safety) ⭐️ 7.8/10

OpenAI 于 2026 年 11 月 16 日发布官方公告，推出新工具、实用指南及跨领域合作伙伴关系，用于防范、检测和响应网络儿童性剥削与虐待。相关举措覆盖事前防范、事中检测、事后响应全流程，具体工具细节暂未公开。

rss · OpenAI Blog · 11月16日 17:00

**「为什么重要」** 该举措是 OpenAI 针对儿童网络性剥削防护的明确布局，为 AI 行业内容安全合规提供了可参考的落地框架，也回应了当前全球对儿童网络安全的监管要求，对 AI 企业的内容安全策略设计有参考价值。

**「可关注」** 可关注：OpenAI 推出的相关工具及实用指南可作为 AI 内容安全合规的参考范本，适配儿童内容防护场景的落地需求。

**标签**: `#lab`, `#policy`, `#industry`, `#product`

---

<a id="item-ai-daily-4"></a>
### [OpenAI 与 LVMH 媒体部门合作](https://openai.com/index/lvmh-media-division-partnership) ⭐️ 7.8/10

OpenAI 与 LVMH 媒体部门宣布达成战略合作，双方将探索用 AI 支持新闻采编工作，同时把 LVMH 旗下出版物接入 ChatGPT 以提升内容可及性。目前公告未披露具体合作规模、落地时间表及技术方案细节。

rss · OpenAI Blog · 11月16日 09:00

**「为什么重要」** 这是头部 AI 实验室与全球媒体集团达成的公开战略合作，为 AI 在新闻业的应用提供了可观察的行业落地样本。

**「可关注」** 可关注后续 LVMH 出版物接入 ChatGPT 的具体产品形态，以及 AI 在新闻采编场景的落地技术方案。

**标签**: `#industry`, `#lab`, `#product`

---

<a id="item-ai-daily-5"></a>
### [OpenAI 嵌入式评估首阶段启动](https://openai.com/index/our-first-phase-of-embedded-assessments) ⭐️ 7.8/10

OpenAI 官方博客宣布启动嵌入式评估首阶段计划，与 Apollo Research、METR、Transluce、Goodfire 四家研究机构开展合作。合作方将独立评估模型的对齐性、安全措施及监控系统。目前公开信息未详述该评估体系与既有评估框架的具体差异。

rss · OpenAI Blog · 11月16日 08:00

**「为什么重要」** 这是 OpenAI 首次公开推进嵌入式第三方评估合作，为行业模型安全治理的独立验证机制提供了新的实践样本。

**「可关注」** 可关注：后续评估框架的具体细则及四家机构的独立评估报告公开节奏。

**标签**: `#lab`, `#eval`, `#policy`, `#industry`

---

<a id="item-ai-daily-6"></a>
### [OpenAI 推进医疗团队计算机使用代理](https://openai.com/index/advancing-computer-use-for-healthcare-teams) ⭐️ 7.8/10

OpenAI 官方博客发布公告，宣布推进面向医疗团队的计算机使用代理（computer-use agents）的研发与应用。当前公开材料未披露具体技术改进内容、性能数据或落地场景范围。

rss · OpenAI Blog · 11月16日 06:00

**「可关注」** 可关注：OpenAI 后续公开的医疗场景计算机使用代理技术细节与落地范围。

**标签**: `#lab`, `#industry`, `#product`

---

<a id="item-ai-daily-7"></a>
### [OpenAI 与 The King’s Trust 启动百万英镑合作](https://openai.com/index/the-kings-trust-and-openai) ⭐️ 7.8/10

OpenAI 官方博客于 2026 年 11 月 16 日宣布，与英国慈善机构 The King’s Trust 启动总额 £1m 的合作项目，计划为英国境内最多 2.5 万名年轻人提供面向工作的实用 AI 技能培训。

rss · OpenAI Blog · 11月16日 00:00

**「为什么重要」** 该合作是 OpenAI 面向英国青年就业场景的 AI 技能普及动作，属于其海外公益合作布局的一部分。

**「可关注」** 可关注：面向非技术青年群体的 AI 技能培训项目的落地模式与后续覆盖效果。

**标签**: `#lab`, `#industry`

---

<a id="item-ai-daily-8"></a>
### [TPU 同策略 RL 实现零数值差异方案](https://developers.googleblog.com/unlocking-stable-on-policy-rl-on-tpu-with-bitwise-zero-traininference-mismatch/) ⭐️ 7.8/10

Google 开发者博客发布基于 Tunix 实现的 Zero-TIM 技术方案，解决大语言模型同策略强化学习训练中 rollout 生成与梯度更新执行路径不同导致的数值不稳定问题，实现 TPU 上训练与推理的位级零数值差异。该方案在 64 块 TPU v5p（DP8×TP8）多主机规模上完成验证，要求采样解码、服务预填充、训练前向三条路径在相同权重、上下文与采样设置下输出位级一致的 logprobs。

rss · Google Developers AI · 11月16日 00:00

**「为什么重要」** 该方案解决了同策略 RL 训练长期存在的数值不稳定痛点，其开源的模块化 JAX/XLA 与 Pallas 实现，为分布式 TPU 栈的位级精确同策略 RL 提供了可复用的参考范式，符合当前大规模 RL 收敛的行业要求。

**「可关注」** 可关注：该方案通过固定分片内核累加顺序、显式跨分片规约顺序、统一 logprob 评分尾部和自定义服务核微分规则四部分方法，实现 TPU 上采样、预填充、训练三条路径的位级 logprobs 对齐。

**标签**: `#lab`, `#industry`, `#product`

---