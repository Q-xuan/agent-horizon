---
layout: default
title: "Horizon Summary: 2026-11-17 (EN)"
date: 2026-11-17
lang: en
---

> From 201 items, 15 important content pieces were selected

---

**Agent Harness Architecture**
1. [Agents SDK v0.24.0 发布](#item-harness-arch-1) ⭐️ 7.8/10
2. [openai-agents-js v0.22.0-alpha.3 发布](#item-harness-arch-2) ⭐️ 7.8/10
3. [google/adk-go v2.8.0 发布](#item-harness-arch-3) ⭐️ 7.8/10

**AI Agent Engineer**
1. [HF 论文：MIRIX-2.0 多智能体记忆系统](#item-agent-engineer-1) ⭐️ 7.0/10
2. [GH-AWTrace 数据集发布](#item-agent-engineer-2) ⭐️ 7.0/10
3. [HF 每日论文：MEM-SQL 与 HARE 基准](#item-agent-engineer-3) ⭐️ 6.0/10
4. [多智能体对齐迁移研究 Aligning AI Teams](#item-agent-engineer-4) ⭐️ 6.0/10

**AI Daily**
1. [OpenAI 发布医疗版 ChatGPT 新功能](#item-ai-daily-1) ⭐️ 8.8/10
2. [ChatGPT 学术研究计划扩至 20 万人](#item-ai-daily-2) ⭐️ 7.8/10
3. [OpenAI 发布儿童网络安全防护工具](#item-ai-daily-3) ⭐️ 7.8/10
4. [LVMH Media 与 OpenAI 达成合作](#item-ai-daily-4) ⭐️ 7.8/10
5. [OpenAI 嵌入式评估首阶段启动](#item-ai-daily-5) ⭐️ 7.8/10
6. [OpenAI 推进医疗团队计算机代理](#item-ai-daily-6) ⭐️ 7.8/10
7. [OpenAI 启动百万英镑青年 AI 培训](#item-ai-daily-7) ⭐️ 7.8/10
8. [TPU 同策略 RL 实现零训练推理差异](#item-ai-daily-8) ⭐️ 7.8/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [Agents SDK v0.24.0 发布](https://github.com/openai/openai-agents-python/releases/tag/v0.24.0-alpha.8) ⭐️ 7.8/10

OpenAI 官方发布 Python Agents SDK v0.24.0-alpha.8。本次 alpha 版本新增三项核心能力：工具调用执行前审批（支持会话级决策记忆，覆盖权限与工具模块）、自定义模型客户端支持（扩展运行时模型集成能力，兼容 async Responses、Chat Completions、LiteLLM、AnyLLM 及自定义适配器）、Realtime 语音会话支持（提供服务器 WebSocket、浏览器 WebRTC、SIP 通话三种连接方案）。此外支持带预算保留的断点恢复、ARM64 Linux wheel 安装，以及 \`ModelOutputItemCompleted\` 工具观察、\`FunctionToolApprovalRequest\` 审批接口、\`SQLAlchemySQLiteSessionStore\` 存储后端等 API 扩展。alpha 版本稳定性待验证。

github · markstuart-oai · Nov 16, 04:39

**「设计要点」** 运行时层通过 application-owned model client 解耦原生工具循环与 OpenAI 后端，支持 LiteLLM、AnyLLM 及自定义适配器。权限与记忆层引入 managed approval 机制，在审批谓词前执行 input policy，并将决策持久化至会话级。存储层通过 CustomStorage 扩展至 SQLAlchemy SQLite、Redis、MongoDB、Dapr，同时支持预算感知的 checkpoint 恢复。

**「改了什么」** 新增工具调用执行前审批能力，支持会话级决策记忆与 \`run\_input\_policy\_before\_approval\` 配置。新增自定义模型客户端支持，原生工具循环兼容 async Responses、Chat Completions、LiteLLM、AnyLLM 及自定义适配器。新增原生 Realtime 语音会话 API，支持 WebSocket、WebRTC、SIP 连接。新增带预算保留的断点恢复能力。新增 ARM64 Linux wheel 支持。新增 \`FunctionToolApprovalRequest\`、\`FunctionToolApprovalDecision\`、\`SQLAlchemySQLiteSessionStore\`、\`ResponsesSocketFactoryOptions\`、\`Session.replace\_history\_suffix\`、\`SessionState.with\_appended\_pending\_input\` 等接口。

**Tags**: `#tools`, `#permissions`, `#runtime`, `#memory`

---

<a id="item-harness-arch-2"></a>
### [openai-agents-js v0.22.0-alpha.3 发布](https://github.com/openai/openai-agents-js/releases/tag/v0.22.0-alpha.3) ⭐️ 7.8/10

这是OpenAI开源的openai-agents-js SDK v0.22.0-alpha.3预发布版本，新增类型化Decision机制（含agent.decide\(\)、ctx.decide\(\)、OpenAIDecisions适配器）实现agent控制流与handoff的类型安全路由，支持应用自主配置的ResponsesModel/ChatCompletionsModel/AiSdkModel模型后端（均支持流式输出），扩展Native Realtime/Voice至Node.js、浏览器、React Native、Workers，新增LocalStorage命名配置文件及历史查询、编辑、分叉能力，配套沙箱工作流的内存、工件、UI辅助能力；同时新增原生工具的命名空间、并发限制、调用方限制、托管审批、客户端搜索、可配置错误格式，MCP的发现过滤器、缓存控制、每工具审批、借用别名，provider的作用域头/查询参数、显式WebSocket路由、托管历史、缓冲Responses JSON、托管提示、重试控制，文本会话的Sign in with ChatGPT与Codex CLI登录路由，beforeComplete输出检查钩子与turn.acceptedText\(\)精确文本前缀暴露；升级要求工具回调默认并发需手动设置maxFunctionConcurrency:1避免竞态，Session.enqueue支持ifBusy: &\#x27;reject&\#x27;拒绝逻辑，AgentOptions要求非字符串Output类型匹配outputType，沙箱快照恢复需单独配置可信resumeAuthority声明，捆绑包需五个同版本SDK包对齐，checkpoint恢复需匹配原生Codex修订与执行器策略；修复User-Agent标识、ESM/CJS模块身份一致性、恢复流程的终端工具所有权与MCP回调错误问题；捆绑包新增Linux x64/ARM64、macOS Apple silicon、Windows x64平台支持，要求Linux glibc 2.39+、OpenSSL 3，Windows x64需VC++运行库，Node.js 24用于捆绑包校验。

github · markstuart-oai · Nov 16, 21:06

**「设计要点」** 运行时层通过三种模型后端抽象解耦SDK与具体模型提供方，支持流式输出；控制流层引入类型化Decision实现agent路由与handoff的类型安全；记忆层新增本地命名配置文件，支持历史查询、编辑、分叉，配套沙箱工作流的内存、工件、UI辅助能力。

**「改了什么」** 相对v0.22.0-alpha.2，新增类型化Decision与OpenAIDecisions适配器、三种应用级模型后端、跨平台实时语音控制、LocalStorage历史管理能力；工具回调默认允许并发，需手动设置maxFunctionConcurrency:1避免竞态；Session.enqueue新增ifBusy: &\#x27;reject&\#x27;拒绝逻辑；AgentOptions要求非字符串Output类型匹配outputType；沙箱快照恢复需单独配置可信resumeAuthority声明，捆绑包需五个同版本SDK包对齐，checkpoint恢复需匹配原生Codex修订与执行器策略；修复User-Agent标识、ESM/CJS模块身份一致性、恢复流程的终端工具所有权与MCP回调错误问题；新增多平台捆绑包安装支持。

**Tags**: `#runtime`, `#memory`, `#subagents`, `#planning`

---

<a id="item-harness-arch-3"></a>
### [google/adk-go v2.8.0 发布](https://github.com/google/adk-go/releases/tag/v2.8.0) ⭐️ 7.8/10

Google 官方发布 adk-go v2.8.0。版本引入配置加载的破坏性变更：workflow edge 引用拒绝绝对 config\_path，且配置目录内任意符号链接均阻断 agent/workflow 引用加载，覆盖 Kubernetes ConfigMap、Bazel runfiles、Nix store 路径等场景，需将挂载复制为真实文件目录（如 cp -rL）后使用。新功能包括内存服务 artifact:// 引用支持、服务端 OAuth2 用户同意流、工具请求终端用户登录、Agent Runtime 流式查询客户端、MCP 工具集转换器、Vertex AI RAG 记忆服务及 BigQuery 工具集。

github · adk-go-bot · Nov 16, 15:05

**「改了什么」** 相对 v2.7.1，v2.8.0 收紧配置解析器对符号链接的接受策略，agent 与 workflow 引用均受影响。内存服务新增 artifact:// 引用解析与服务端 OAuth2 同意流，工具可请求终端用户登录；CLI、Agent Engine 客户端、记忆层及工具层分别新增部署环境配置、流式查询、Vertex AI RAG 服务、增量写入、BigQuery 工具集及 MCP 转换器。

**Tags**: `#runtime`, `#permissions`, `#config`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [HF 论文：MIRIX-2.0 多智能体记忆系统](https://huggingface.co/papers/2611.12068) ⭐️ 7.0/10

2026年11月16日Hugging Face每日论文发布MIRIX-2.0多智能体LLM智能体记忆系统，该论文当前获社区45次赞同。该系统在5个QA与智能体任务基准中的4个达到对比系统最高准确率：LoCoMo得分91.4%，LongMemEval-S得分72.6%，领先最强基线14.3分；关闭AutoDream后，单跳与多跳文档QA得分分别比HyperMem高31.0、22.0分；作为过程记忆，其在ALFWorld、WebShop上的成功率高于对比记忆方法，MetaClaw-Bench得分49.2%，对比基线为44%（原文内容截断，完整技术实现细节与剩余对比数据未披露）。该成果面向从事LLM智能体记忆模块开发、智能体任务评估的工程师。

rss · Hugging Face Daily Papers · Nov 16, 00:00

**「为什么重要」** 当前LLM智能体长期记忆存在参数记忆需训练、记忆整合易丢细节、全量存储检索成本高的普遍痛点，MIRIX-2.0在多个主流记忆与智能体任务基准上取得明确性能提升，为相关模块设计提供了可参考的评估参照，目前尚未有实际落地效果的公开验证。

**「可关注」** 可关注：多智能体记忆系统在QA、过程记忆类基准上的性能增益，以及AutoDream组件对文档QA结果的显著影响。

**Tags**: `#memory`, `#eval`, `#multi-agent`

---

<a id="item-agent-engineer-2"></a>
### [GH-AWTrace 数据集发布](https://huggingface.co/papers/2611.06866) ⭐️ 7.0/10

2026年11月16日，Hugging Face每日论文聚合介绍了一篇arXiv预印本，发布大规模GitHub智能体工作流执行日志数据集GH-AWTrace。该数据集包含25014条已验证智能体工作流，覆盖5051个仓库，关联4112526条运行记录与562877份非空执行日志归档，数据受GitHub日志保留限制保存，同时关联仓库元数据与生成的工作流配置。它填补了现有研究仅关注工作流定义与输出、缺乏运行时执行证据的空白，可用于分析智能体执行失败、工具拒绝、代理委托等场景，对智能体评测、可观测性、工作流编排优化有参考价值；目前公开内容未包含性能对比或深度技术排查细节。

rss · Hugging Face Daily Papers · Nov 16, 00:00

**「为什么重要」** 该数据集首次公开了大规模带真实运行时执行证据的GitHub智能体工作流数据，解决了该领域缺乏生产级Trace数据的研究痛点；其对智能体故障分析、工具使用研究的实际增益还需后续研究进一步验证。

**「可关注」** 可关注：GH-AWTrace 提供的真实生产执行日志可用于验证智能体工作流的故障定位与工具调用行为分析。

**Tags**: `#eval`, `#observability`, `#orchestration`

---

<a id="item-agent-engineer-3"></a>
### [HF 每日论文：MEM-SQL 与 HARE 基准](https://huggingface.co/papers/2611.18338) ⭐️ 6.0/10

2026年11月16日，Hugging Face Daily Papers分享了一篇新论文，提出面向历史查询复用的Text-to-SQL基准HARE与内存增强方法MEM-SQL。HARE包含1600条请求，源自4个数据集的823条已验证查询，标注了各请求保留的组件与需编辑的部分，可区分全查询适配与部分复用场景。MEM-SQL通过存储全查询模板、可复用SQL块及领域概念映射实现内存增强。当前公开摘录未披露完整技术细节、性能数据与可复现资源，需参考原论文获取全量信息，该成果在Hugging Face Daily Papers获得17次赞同，主要对数据库交互类Agent的序列化工具调用、记忆系统设计场景有参考价值。

rss · Hugging Face Daily Papers · Nov 16, 00:00

**「为什么重要」** 它首次系统覆盖了Text-to-SQL场景下的历史查询复用评估空白，为数据库交互Agent的序列化工具调用效果测试提供了新的基准思路；但该方法对通用Agent记忆系统的迁移价值尚未得到验证，仅对数据库交互类场景有直接参考意义。

**「可关注」** 可关注：现有Text-to-SQL基准多仅独立评估单条查询生成效果，HARE对历史查询复用的评估维度可补充数据库交互Agent的序列化工具调用测试框架。

**Tags**: `#eval`, `#memory`

---

<a id="item-agent-engineer-4"></a>
### [多智能体对齐迁移研究 Aligning AI Teams](https://huggingface.co/papers/2611.17820) ⭐️ 6.0/10

Hugging Face Daily Papers 于 2026-11-16 推荐一篇预印本，研究单智能体 LLM 对齐训练向多智能体团队的迁移失败机制。该研究在败血症分诊、新闻推荐器及十个咨询提案生成任务上开展实证，发现单-团队安全差距与模型能力无清晰正相关：Anthropic Mythos Preview 在一个任务上差距最大，在另一个任务上最小。研究还测试了互相批评、群聊协调等自然干预，但这些方法无法可靠将团队行为拉回单智能体对齐水平。当前材料仅呈现部分发现，全文尚未发布，缺乏完整结论、可操作解决方案或量化性能数据。

rss · Hugging Face Daily Papers · Nov 16, 00:00

**「为什么重要」** 多智能体系统对齐是 coding agent 工程的核心难题。该预印本提供初步实证证据，表明常见自然干预可能无法解决能力相关安全差距，值得在全文发布前浏览。

**「可关注」** 可关注：单智能体对齐结果不能直接外推多智能体团队，现有自然协调机制（互评、群聊）可能无法弥补安全差距。

**Tags**: `#orchestration`, `#eval`, `#coding-agent`

---

## AI Daily

<a id="item-ai-daily-1"></a>
### [OpenAI 发布医疗版 ChatGPT 新功能](https://openai.com/index/more-ways-to-move-care-forward-with-chatgpt-for-healthcare) ⭐️ 8.8/10

OpenAI 宣布为医疗场景的 ChatGPT 增加三项新功能：computer-use agents、改进的临床问答，以及可在不同医疗软件间工作的插件。这些功能的目标是让 ChatGPT 在医疗软件中完成实际工作。公告未披露具体发布时间、支持地区或临床验证细节。

rss · OpenAI Blog · Nov 16, 06:00

**「为什么重要」** 医疗是 AI 落地的关键垂直领域，OpenAI 此次为医疗场景扩展 ChatGPT 功能，显示其对垂直行业的持续投入。新功能同时涉及 agent 执行与跨系统整合，扩展了 ChatGPT 在医疗场景的应用方向。

**「可关注」** 可关注：医疗场景中 computer-use agent 与跨医疗软件插件的实际落地形式。

**Tags**: `#lab`, `#product`, `#industry`

---

<a id="item-ai-daily-2"></a>
### [ChatGPT 学术研究计划扩至 20 万人](https://openai.com/index/expanding-chatgpt-for-academic-researchers) ⭐️ 7.8/10

OpenAI 宣布扩展 ChatGPT for Academic Researchers 计划，向全球 20 万名研究人员免费提供前沿模型访问权限。此次扩展将免费覆盖规模扩大至 20 万人，但材料未说明具体模型范围、访问形式或申请条件。

rss · OpenAI Blog · Nov 16, 17:00

**「为什么重要」** 该扩展是 OpenAI 在学术可及性方面的政策调整，将免费前沿模型覆盖扩大至 20 万研究者规模。材料未评估具体影响，仅记录这一规模变化本身。

**「可关注」** 可关注：免费访问的具体形式与模型限制尚未披露，材料未说明相关约束条件。

**Tags**: `#openai`, `#product`, `#policy`, `#industry`

---

<a id="item-ai-daily-3"></a>
### [OpenAI 发布儿童网络安全防护工具](https://openai.com/index/strengthening-online-child-safety) ⭐️ 7.8/10

2026年11月16日，OpenAI 官方博客发布公告，推出用于防范、检测和应对网络儿童性剥削与虐待的新工具、实用指南，同时公布相关合作伙伴关系，覆盖该领域的全流程防护工作。

rss · OpenAI Blog · Nov 16, 17:00

**「为什么重要」** 该举措为AI平台应对网络儿童性剥削问题提供了可参考的工具与规范框架，有助于推动行业建立统一的防护标准。

**「可关注」** 可关注：OpenAI 配套发布的儿童网络性剥削防护实用指南的具体技术落地规则与工具调用方式。

**Tags**: `#lab`, `#policy`, `#industry`, `#product`

---

<a id="item-ai-daily-4"></a>
### [LVMH Media 与 OpenAI 达成合作](https://openai.com/index/lvmh-media-division-partnership) ⭐️ 7.8/10

LVMH Media Division 与 OpenAI 宣布建立战略合作伙伴关系，旨在用 AI 支持新闻业，并通过 ChatGPT 让 LVMH 旗下出版物更易访问。公告未披露具体合作规模、投入资金或覆盖的出版物数量。

rss · OpenAI Blog · Nov 16, 09:00

**「为什么重要」** LVMH 作为全球奢侈品媒体集团与 OpenAI 达成合作，是新闻业 AI 应用的一个新案例。该合作如何落地，可观察新闻业与 AI 的协作边界。

**「可关注」** 可关注：LVMH 旗下出版物接入 ChatGPT 的内容授权范围与交互形式。

**Tags**: `#industry`, `#lab`, `#product`

---

<a id="item-ai-daily-5"></a>
### [OpenAI 嵌入式评估首阶段启动](https://openai.com/index/our-first-phase-of-embedded-assessments) ⭐️ 7.8/10

2026年11月16日OpenAI官方宣布，与Apollo Research、METR、Transluce、Goodfire四家研究机构启动嵌入式评估首阶段计划，由上述独立机构评估模型对齐性、安全措施及监控系统。

rss · OpenAI Blog · Nov 16, 08:00

**「为什么重要」** 这是OpenAI首次推进嵌入式第三方评估机制，独立机构的介入可提升模型对齐、安全相关评估的客观性，为行业评估范式提供参考。

**「可关注」** 可关注：后续可跟踪四家机构的评估方法论与公开结论，了解第三方嵌入式评估的落地实践。

**Tags**: `#lab`, `#eval`, `#policy`, `#industry`

---

<a id="item-ai-daily-6"></a>
### [OpenAI 推进医疗团队计算机代理](https://openai.com/index/advancing-computer-use-for-healthcare-teams) ⭐️ 7.8/10

OpenAI 于 2026 年 11 月 16 日发布官方博客，宣布推进面向医疗团队的计算机使用代理能力。该公告未披露具体技术改进细节、性能指标或适用范围。目前可确认的信息仅限发布主体、发布时间及目标应用领域。

rss · OpenAI Blog · Nov 16, 06:00

**Tags**: `#lab`, `#industry`, `#product`

---

<a id="item-ai-daily-7"></a>
### [OpenAI 启动百万英镑青年 AI 培训](https://openai.com/index/the-kings-trust-and-openai) ⭐️ 7.8/10

OpenAI 宣布与英国慈善机构 The King&\#x27;s Trust 启动 £1m 合作，计划为英国最多 2.5 万名年轻人提供实用 AI 技能培训。该项目聚焦工作场景所需的 AI 应用能力，目前未披露具体课程内容、实施周期或参与门槛。

rss · OpenAI Blog · Nov 16, 00:00

**「可关注」** 关注 OpenAI 通过 The King&\#x27;s Trust 落地英国青年 AI 技能培训的后续课程设计。

**Tags**: `#lab`, `#industry`

---

<a id="item-ai-daily-8"></a>
### [TPU 同策略 RL 实现零训练推理差异](https://developers.googleblog.com/unlocking-stable-on-policy-rl-on-tpu-with-bitwise-zero-traininference-mismatch/) ⭐️ 7.8/10

Google 开发者博客发布 Zero-TIM（零训练-推理不匹配）技术方案，落地于 Tunix 框架，解决大语言模型同策略强化学习训练中 rollout 生成与梯度更新执行路径不同导致的数值不稳定问题。该方案在 64 块 TPU v5p 组成的 DP8×TP8 多主机网格上完成验证，实现采样解码、服务预填充、训练前向三条路径的 logprob 位级完全一致，当前验证基于 Qwen3-8B  checkpoint 在 FrozenLake 环境的 200 步数值测试，实现已在 Tunix 开源。

rss · Google Developers AI · Nov 16, 00:00

**「为什么重要」** 消除训练-推理数值不匹配已成为大规模 RL 收敛的行业标配要求，该方案提供了可复用的分布式 JAX/TPU 栈位精确同策略 RL 实现蓝图，解决了同策略 RL 训练易因数值差异退化为异策略的行业痛点。

**「可关注」** 可关注：Tunix 的 Zero-TIM 提供四部分可复用配方，通过锁存分片内核累加、显式规约顺序、统一 logprob 评分尾、自定义服务内核微分规则，实现 TPU 上采样/预填充/训练三条路径的位级 logprob 对齐；同时提供采样解码-预填充、预填充-训练前向的两步诊断方法，可快速定位数值对齐问题，并通过 XLA\_FLAGS 传递 --xla\_allow\_excess\_precision=false 约束编译器中间精度。

**Tags**: `#lab`, `#industry`, `#product`

---