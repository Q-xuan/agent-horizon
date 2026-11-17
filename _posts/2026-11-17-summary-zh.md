---
layout: default
title: "Horizon Summary: 2026-11-17 (ZH)"
date: 2026-11-17
lang: zh
---

> 从 226 条内容中筛选出 19 条重要资讯。

<nav id="ah-toc" class="ah-toc" aria-label="目录"><span class="ah-toc-title">目录</span><ul><li><a href="#sec-harness-arch"><span class="ah-toc-name">Harness 架构</span><span class="ah-toc-count">3条</span></a></li><li><a href="#sec-agent-engineer"><span class="ah-toc-name">Agent 工程师日报</span><span class="ah-toc-count">8条</span></a></li><li><a href="#sec-ai-daily"><span class="ah-toc-name">AI 日报</span><span class="ah-toc-count">6条</span></a></li><li><a href="#sec-ai-deals"><span class="ah-toc-name">AI 羊毛</span><span class="ah-toc-count">2条</span></a></li></ul></nav>

---

**[Harness 架构](#sec-harness-arch)**
1. [pydantic-ai v2.69.0 发布](#item-harness-arch-1) ⭐️ 8.3/10
2. [openai-agents-js v0.22.0-alpha.3 发布](#item-harness-arch-2) ⭐️ 7.8/10
3. [adk-go v2.8.0 发布](#item-harness-arch-3) ⭐️ 7.8/10

**[Agent 工程师日报](#sec-agent-engineer)**
1. [OpenAI 儿童安全声明与社区反馈](#item-agent-engineer-1) ⭐️ 7.0/10
2. [Mobile AI Factory 论文发布](#item-agent-engineer-2) ⭐️ 7.0/10
3. [WebArena-Pro 基准发布](#item-agent-engineer-3) ⭐️ 7.0/10
4. [Clover 2 公开 27.8B 动态路由 LoRA 模型](#item-agent-engineer-4) ⭐️ 7.0/10
5. [external-sandbox-quicksand 0.2.0 发布](#item-agent-engineer-5) ⭐️ 6.8/10
6. [external-sandbox-container 0.2.0 发布](#item-agent-engineer-6) ⭐️ 6.3/10
7. [MIRIX-2.0 多智能体记忆系统论文公开](#item-agent-engineer-7) ⭐️ 6.0/10
8. [Hugging Face 多智能体对齐研究](#item-agent-engineer-8) ⭐️ 6.0/10

**[AI 日报](#sec-ai-daily)**
1. [OpenAI 扩展 ChatGPT 学术研究者项目](#item-ai-daily-1) ⭐️ 8.8/10
2. [OpenAI 推进医疗团队计算机使用代理](#item-ai-daily-2) ⭐️ 8.8/10
3. [LVMH 媒体部与 OpenAI 宣布战略合作](#item-ai-daily-3) ⭐️ 8.3/10
4. [OpenAI 发布科研用 ChatGPT 报告](#item-ai-daily-4) ⭐️ 7.8/10
5. [OpenAI 启动首阶段嵌入式评估](#item-ai-daily-5) ⭐️ 7.8/10
6. [OpenAI 扩展 ChatGPT 医疗能力](#item-ai-daily-6) ⭐️ 7.8/10

**[AI 羊毛](#sec-ai-deals)**
1. [BrowserPod 4.0 浏览器 MicroVM 免费开放](#item-ai-deals-1) ⭐️ 6.0/10
2. [Supabase Free 周备份工具开源](#item-ai-deals-2) ⭐️ 5.0/10

---

## Harness 架构
{: #sec-harness-arch .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-harness-arch" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-harness-arch-1"></a>
### [pydantic-ai v2.69.0 发布](https://github.com/pydantic/pydantic-ai/releases/tag/v2.69.0) ⭐️ 8.3/10

这是 pydantic-ai v2.69.0 官方版本发布，核心变更包含延迟工具调用处理的破坏性调整、响应级工具调用 ID 通用化、流式循环检测，同时扩展 Gemini 4 Hydrogen 与 Groq 模型支持，同时包含大量错误分类细化、包结构重命名等兼容性调整。

github · dsfaccini · 11月17日 01:03

**「设计要点」** 运行时将 RequestInput 合并入 HandleDeferredToolCalls 并支持恢复令牌，子代理 settled 任务历史改为持久化到文件而非挂载在 DelegationTasks 所有者内存；新增 DetectLoops 组件对流式思维、文本和工具调用参数做循环检测，包结构按能力名重命名并保留旧别名兼容。

**「改了什么」** 本次发布包含多项破坏性变更：合并 RequestInput 到 HandleDeferredToolCalls 并支持恢复令牌，新增 tool\_call\_ids\_are\_response\_scoped 配置项替代原有响应级工具调用 ID 逻辑，新增流式循环检测能力覆盖思维、文本和工具调用参数，同时扩展 Gemini 4 Hydrogen、Groq service\_tier 模型支持，新增 KubernetesSandbox、WindowsWorkspace 等沙箱能力；此外统一细化错误分类，将各类 API、传输、限流、配额错误映射为对应 Model\*Error 异常，包结构按能力名重命名并保留旧别名兼容，Advisor 支持 native=与 local=参数替代原有 mode 参数，TestModel 调整边界校验逻辑，TieredCompaction 支持跳过失败层级并允许层级省略触发条件。

**「评论」** 暂无社区评论内容。

**标签**: `#tools`, `#runtime`

---

<a id="item-harness-arch-2"></a>
### [openai-agents-js v0.22.0-alpha.3 发布](https://github.com/openai/openai-agents-js/releases/tag/v0.22.0-alpha.3) ⭐️ 7.8/10

OpenAI 发布 openai-agents-js v0.22.0-alpha.3，引入 typed Decisions（\`agent.decide\(\)\`、\`ctx.decide\(\)\`、\`DecisionHandoff\`）用于 agent 路由与控制流，新增 \`ResponsesModel\`、\`ChatCompletionsModel\`、\`AiSdkModel\` 三类应用-owned 模型后端适配器并支持流式输出。跨平台原生语音扩展至 Node.js、浏览器、React Native 与 Workers，覆盖音频输入、响应时机、SIP 通话等控制。本地执行器新增只读工作区与可选的 \`trusted\_workspace\_write\`（Linux、macOS），LocalStorage 支持命名 profiles、历史查询与 fork。捆绑包支持 Linux x64/ARM64、macOS Apple silicon、Windows x64，要求 glibc 2.39+、OpenSSL 3 或 VC++ Redistributable，启动器检查基于 Node.js 24。

github · markstuart-oai · 11月16日 21:06

**「设计要点」** 运行时抽象层同时覆盖 Node.js、浏览器、React Native 与 Workers，模型调用通过 \`ResponsesModel\`、\`ChatCompletionsModel\`、\`AiSdkModel\` 适配器解耦，决策系统用 typed Decisions 替代隐式分支，本地执行通过 \`trusted\_workspace\_write\` 与 \`resumeAuthority\` 实现最小权限写入。工具层引入命名空间、并发限制与 MCP 集成，状态管理通过 LocalStorage named profiles 与 checkpoint 机制持久化。

**「改了什么」** 相对 alpha.2，新增 typed Decisions API 与 \`OpenAIDecisions\` 适配器（需 \`openai\` 7.30.0+），工具回调默认改为并发 admission，\`Session.enqueue\(\)\` 开始拒绝 \`ifBusy: &\#x27;reject&\#x27;\` 场景，\`AgentOptions\` 强制非字符串 Output 配置 \`outputType\`。序列化 Classic sandbox 恢复与 UnixLocal/Docker 快照恢复新增可信绑定要求，ESM/CJS 导入修复类与工具身份共享，User-Agent 统一标识为 \`openai\_agents\_js\`。

**标签**: `#runtime`, `#planning`, `#memory`, `#subagents`

---

<a id="item-harness-arch-3"></a>
### [adk-go v2.8.0 发布](https://github.com/google/adk-go/releases/tag/v2.8.0) ⭐️ 7.8/10

Google 发布 adk-go v2.8.0。本次更新引入 config path resolution 的 breaking change：workflow edge references 不再接受绝对 config\_path，且通过链接进入 config 目录的引用全部失效，影响 Kubernetes ConfigMaps、Bazel runfiles、Nix store paths 等部署模式。新功能包括 in-memory artifact:// 引用支持、服务端 OAuth2 consent flow、Agent Runtime stream-query 客户端、Vertex AI RAG memory service、BigQuery toolset，以及 MCP toolset 扩展。修复覆盖 A2A 协议兼容性、REST 接口行为、事件时间戳精度等。

github · adk-go-bot · 11月16日 15:05

**「改了什么」** 相对 v2.7.1，v2.8.0 强制 config 目录必须为真实文件而非符号链接，否则 agent 与 workflow 引用均无法加载。新增 memory 增量写入、Vertex AI RAG 记忆服务、服务端 OAuth2 授权流程，以及 BigQuery 和 Vertex AI RAG 工具集。

**标签**: `#runtime`, `#permissions`, `#memory`

---

## Agent 工程师日报
{: #sec-agent-engineer .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-agent-engineer" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-agent-engineer-1"></a>
### [OpenAI 儿童安全声明与社区反馈](https://openai.com/index/strengthening-online-child-safety/) ⭐️ 7.0/10

2026 年 11 月 16 日 OpenAI 发布加强在线儿童性虐待内容（CSAM）防控的官方声明，同期社区反馈多起与 CSAM 规则相关的生产事故与策略变更：有团队称其自主代理本应调用本地图像分类器，误切换至 OpenAI 图像分类器处理用户上传内容，在分类超 10 万张图像后被 OpenAI 判定 CSAM 违规封号，申诉后未获事件相关细节；另有用户反馈使用 Claude 调用 GPT 图像生成童话故事配图时，涉及儿童形象的内容被过度过滤，多次请求生成恐惧表情的儿童形象均被拒绝。此外 OpenRouter 已对零数据保留（ZDR）端点启动 CSAM 扫描与留存，影响相关 API 调用方的数据留存预期。

hackernews · rossant · 11月16日 18:12 · [社区讨论](https://news.ycombinator.com/item?id=50520804)

**「为什么重要」** 这些事件直接暴露 AI 代理工具链中第三方服务规则冲突、安全过滤误伤、API 数据留存承诺变更三类风险，是当前构建 coding agent 与合规架构的工程师需要优先明确的边界；其中已发生的生产封号、过滤失效、留存策略变更已实际影响相关服务的可用性与合规预期。

**「可关注」** 可关注：自主代理调用第三方图像分类、生成类 API 时，需提前确认服务方 CSAM 检测规则、数据留存策略与封号申诉机制，规避规则冲突导致的生产故障。

**「评论」** 社区讨论围绕三类实际体验展开：生产代理调用 OpenAI 图像分类器触发封号且申诉无反馈、图像生成模型对儿童相关内容的过度过滤、OpenRouter 在 ZDR 端点新增 CSAM 扫描打破零数据保留预期；部分用户认可 CSAM 防控的必要性，但认为需提升规则透明度与误伤申诉通道。

**标签**: `#permissions`, `#safety`, `#observability`, `#toolchain`, `#coding-agent`

---

<a id="item-agent-engineer-2"></a>
### [Mobile AI Factory 论文发布](https://huggingface.co/papers/2611.13509) ⭐️ 7.0/10

2026 年 11 月 17 日 Hugging Face 每日论文收录《Mobile AI Factory》论文，提出同名 agentic 系统，可自动化完成针对特定移动设备与任务的小语言模型（SLM）微调、量化全流程。系统核心包含编排 LLM、准确率回滚规则、跨模型架构与量化方案的自适应搜索，同时集成目标设备的真实推理测量。当前公开内容仅为截断摘要，未披露性能基准数据，主要用例面向端侧移动 AI 场景。

rss · Hugging Face Daily Papers · 11月17日 05:34

**「为什么重要」** 该论文公开了面向端侧模型定制的 agent orchestration、eval 与自动化 ML 流程的具体设计，对做 coding agent/harness 的工程师有直接参考价值。但当前仅公开截断摘要，未披露性能基准与泛化性验证结果，实际效果尚未证实。

**「可关注」** 可关注：其用编排 LLM 做流程决策、规则化准确率回滚、结合真实设备推理测量的自动化 ML 流程设计，对 agent orchestration 与 eval harness 工程有参考价值。

**标签**: `#orchestration`, `#eval`, `#harness`

---

<a id="item-agent-engineer-3"></a>
### [WebArena-Pro 基准发布](https://huggingface.co/papers/2611.17955) ⭐️ 7.0/10

2026 年 11 月 17 日，Hugging Face Daily Papers 发布 WebArena-Pro 基准，这是面向 Web Agent 的可复现多模态评测工具，覆盖 20 个自托管 Web 应用、6 个领域共 300 个任务，解决现有基准应用覆盖不足、仅支持文本/视觉模态、在线基准不可复现、未评估音视频内容的核心问题，面向构建或评测 Web Agent 的工程师群体。

rss · Hugging Face Daily Papers · 11月17日 05:34

**「为什么重要」** 当前 Web Agent 评测工具普遍存在覆盖范围窄、模态单一、运行结果不可复现的缺口，WebArena-Pro 针对这些问题设计，为相关研发工作提供了标准化的可复现评测环境。

**「可关注」** 可关注：该基准采用自托管应用架构，可规避在线基准因页面与数据漂移导致的不可复现问题，同时填补了现有基准对音视频模态评测的空白。

**标签**: `#eval`, `#web-agent`, `#benchmark`, `#multimodal`, `#reproducibility`

---

<a id="item-agent-engineer-4"></a>
### [Clover 2 公开 27.8B 动态路由 LoRA 模型](https://www.reddit.com/r/LocalLLaMA/comments/1xyb7jw/clover_2_dense_278b_base_7_lora_experts_routed/) ⭐️ 7.0/10

Clover 2 开发团队于 2026-11-17 公开 27.8B 基础模型及全套配套组件，包含 7 个任务专用 LoRA 适配器、训练好的 per-token 路由器和 vLLM 部署插件。推理时路由器按 token 动态选择适配专家，无匹配场景回退到基础模型，并非静态合并权重。官方称该方案在 GSM8K、MATH-500、GSM-Hard、LongBench-v2 及创意写作任务上相比原始基础模型有可观测提升，当前提供一周免费试用，暂未发布 GGUF 版本，llama.cpp 对混合注意力架构的支持仍处于早期阶段。

reddit · r/LocalLLaMA · /u/bakatristan · 11月17日 04:35

**「为什么重要」** 这是目前公开的 per-token 动态 LoRA 路由落地方案，所有核心组件均开源，为 LoRA 工作流编排、agent harness 开发提供了可直接复用的工程参考，避免了静态合并多专家权重带来的能力折损问题。

**「可关注」** 可关注：公开的动态 per-token LoRA 路由方案搭配现成 vLLM 插件，可直接复用到现有 LoRA 编排或 agent harness 流程中，当前自托管需优先选择 vLLM 路径，GGUF 及 llama.cpp 兼容性仍在早期是主要限制。

**标签**: `#orchestration`, `#eval`, `#harness`

---

<a id="item-agent-engineer-5"></a>
### [external-sandbox-quicksand 0.2.0 发布](https://github.com/prime-radiant-inc/external-sandbox-quicksand/releases/tag/0.2.0) ⭐️ 6.8/10

simonw 于 2026-11-16 发布 external-sandbox-quicksand 0.2.0。该版本新增 \`--proxy\` 选项，以 deny-all 模式启动 HTTP\(S\) 代理，支持通过 \`/proxy\` 页面进行 web-based allowlisting，\`--proxy-config FILE\` 仍可在启动时提供策略且两者同时给出时后者优先。代理现在通过 truststore 使用操作系统信任存储验证上游 TLS 证书，避免主机浏览器和 curl 接受的站点返回 502；客户端中途断开连接不再记录为 502，而是记录为 \`allowed\` 并附带 \`client\_disconnected\` 原因，证书失败则记录 \`upstream\_certificate\_not\_verified\`。该更新对 agent 网络权限和可观测性有直接改进，但作为 niche 0.2.0 发布，更广泛生态影响有限。

github · simonw · 11月16日 22:24

**「为什么重要」** 该版本直接改进了 agent 沙箱的网络权限控制（deny-all 默认 + web allowlisting）和可观测性（更准确的断开/证书日志），对正在搭建类似 harness 的团队有参考价值。但作为 niche 0.2.0 发布，其影响目前局限于该工具自身用户，尚未观察到更广泛生态系统的连锁反应。

**「可关注」** 可关注：deny-all 代理模式配合 web-based allowlisting 提供了比纯策略文件更灵活的网络权限控制路径，而系统 trust store 集成则解决了容器/沙箱环境中常见的上游证书验证失败问题。

**标签**: `#permissions`, `#observability`, `#harness`

---

<a id="item-agent-engineer-6"></a>
### [external-sandbox-container 0.2.0 发布](https://github.com/prime-radiant-inc/external-sandbox-container/releases/tag/0.2.0) ⭐️ 6.3/10

simonw 于 2026-11-16 发布 \`prime-radiant-inc/external-sandbox-container\` 0.2.0。本次小版本更新包含三项增量改进：新增 \`--proxy\` 选项，以默认 deny-all 模式启动托管 HTTP\(S\) 代理，支持通过 \`/proxy\` 页面添加 allow rules；代理现在通过 \`truststore\` 库验证上游 TLS 证书是否匹配操作系统信任存储，解决此前主机浏览器和 \`curl\` 可接受站点返回 502 的问题；沙箱客户端在响应中途断开连接时，日志状态改为 \`allowed\`，原因标记为 \`client\_disconnected\`，而非 502 错误，证书失败则记录为 \`upstream\_certificate\_not\_verified\`。\`--proxy-config FILE\` 仍可在启动时提供策略，且当与 \`--proxy\` 同时使用时优先。本次更新不涉及破坏性变更或重大架构调整。

github · simonw · 11月16日 22:24

**「为什么重要」** 该版本直接改进 agent 沙箱的网络权限控制与可观测性。deny-all 代理模式降低了初始策略编写门槛，TLS 信任存储集成减少了因证书校验导致的误报 502，而断开连接日志的细化有助于区分网络故障与客户端主动断开。

**「可关注」** 可关注：\`--proxy\` 的 deny-all 默认行为与 \`/proxy\` 页面动态 allow 规则的组合，可能改变沙箱网络策略的配置流程；TLS 信任存储集成意味着代理的出站证书校验逻辑与主机环境解耦，需验证 \`truststore\` 在不同基础镜像中的行为一致性。

**标签**: `#sandbox`, `#proxy`, `#permissions`, `#observability`, `#security`

---

<a id="item-agent-engineer-7"></a>
### [MIRIX-2.0 多智能体记忆系统论文公开](https://huggingface.co/papers/2611.12068) ⭐️ 6.0/10

2026 年 11 月 17 日，Hugging Face Daily Papers 收录 arXiv 预印本论文《MIRIX-2.0: Multi-Agent Memory System》，提出同名的多智能体记忆系统，针对 LLM 智能体长期记忆的参数记忆需训练、记忆整合易丢细节、全量存储检索成本递增等痛点设计。该系统的基准性能在 5 个智能体记忆与 QA 基准中的 4 个上领先对比基线：LoCoMo 得分 91.4%，LongMemEval-S 得分 72.6%，分别领先最强基线 14.3 分；关闭 AutoDream 后，单跳与多跳文档 QA 得分分别领先 HyperMem 31.0 分、22.0 分；作为过程记忆方案时，在 ALFWorld、WebShop、MetaClaw-Bench 上的成功率均高于对比记忆方法，MetaClaw-Bench 得分 49.2%。当前该成果仅为研究预印本，并非生产就绪工具，完整技术细节、可复现性及实际场景适配效果需查阅原论文验证，对 AI Agent 工程实践的即时可操作价值有限。

rss · Hugging Face Daily Papers · 11月17日 05:34

**「为什么重要」** 该研究针对 LLM 智能体长期记忆的核心痛点提出了新的多智能体记忆方案，在多个主流公开基准上取得领先性能，为相关技术研究提供了新的参考方向；但其实际工程落地效果、跨场景泛化能力以及对现有智能体记忆方案的替代可能性尚未得到验证，暂无法确认其产业应用价值。

**「可关注」** 可关注：该多智能体记忆系统在公开基准上表现突出，但作为未经过同行评议的预印本成果，其工程实现复杂度、复现成本、实际场景下的性能衰减情况均不明确，不建议直接引入生产级智能体系统。

**标签**: `#memory`, `#eval`

---

<a id="item-agent-engineer-8"></a>
### [Hugging Face 多智能体对齐研究](https://huggingface.co/papers/2611.17820) ⭐️ 6.0/10

Hugging Face Daily Papers 2026-11-17 聚合了一篇多智能体 LLM 对齐迁移研究论文。论文聚焦败血症分诊、新闻推荐两项软件工程任务及多项咨询提案生成任务，给出四项发现中的两项完整结果。研究发现单智能体与团队安全差距与模型能力无明确趋势，Anthropic Mythos Preview 在不同任务上差距表现相反。多项自然干预措施（如同行评审、群聊协调）无法可靠将智能体团队带回单智能体对齐行为。当前材料内容被截断，缺少第三、四项发现及完整技术细节，影响范围限于多智能体系统对齐、评估与编排工程师。

rss · Hugging Face Daily Papers · 11月17日 05:34

**「为什么重要」** 当前多智能体系统部署常假设单智能体对齐可自然迁移至团队场景，或可通过简单协调机制修复。该研究提供实证反驳，表明常见干预无效且安全差距与模型能力无关。这对 agent harness 设计与 eval 策略构成直接挑战。

**「可关注」** 可关注：在构建多智能体工作流时，不要假设单智能体对齐结果能自然迁移到团队场景，同行评审或群聊等协调机制未必能恢复对齐行为，需针对团队场景单独设计对齐验证。

**标签**: `#eval`, `#orchestration`

---

## AI 日报
{: #sec-ai-daily .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-daily" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-daily-1"></a>
### [OpenAI 扩展 ChatGPT 学术研究者项目](https://openai.com/index/expanding-chatgpt-for-academic-researchers) ⭐️ 8.8/10

OpenAI 官方宣布扩展 ChatGPT for Academic Researchers 项目，向全球 20 万名研究人员免费开放前沿模型使用权限。本次扩展无额外公开的使用限制说明，覆盖全球学术研究者群体。

rss · OpenAI Blog · 11月16日 17:00

**「为什么重要」** 这是主流 AI 实验室首次将前沿模型免费权限大规模定向开放给全球学术群体，有望降低科研场景的 AI 工具使用门槛。

**「可关注」** 可关注：该项目后续开放的申请规则、模型权限覆盖范围及使用限制细则。

**标签**: `#lab`, `#product`, `#policy`

---

<a id="item-ai-daily-2"></a>
### [OpenAI 推进医疗团队计算机使用代理](https://openai.com/index/advancing-computer-use-for-healthcare-teams) ⭐️ 8.8/10

OpenAI 于 2026 年 11 月 16 日发布官方博客，宣布推进其计算机使用代理技术的适配工作，目标为医疗团队提供部署支持。当前公开材料未披露具体性能参数、落地时间表及合作方信息。

rss · OpenAI Blog · 11月16日 06:00

**「为什么重要」** 医疗场景对操作准确性、数据合规性要求极高，计算机使用代理进入该领域落地，既拓展了 AI 代理的应用边界，也为技术迭代提供了高标准的验证场景。

**「可关注」** 可关注：医疗场景下的操作可追溯、数据合规要求，或成为计算机使用代理后续迭代的核心约束。

**标签**: `#lab`, `#product`, `#industry`

---

<a id="item-ai-daily-3"></a>
### [LVMH 媒体部与 OpenAI 宣布战略合作](https://openai.com/index/lvmh-media-division-partnership) ⭐️ 8.3/10

2026 年 11 月 16 日，LVMH 媒体部门与 OpenAI 在官方博客宣布达成战略合作。合作核心为以 AI 技术支持新闻业，同时使 LVMH 旗下出版物可通过 ChatGPT 更便捷地触达用户。目前公开信息未披露合作的具体落地时间与内容授权细节。

rss · OpenAI Blog · 11月16日 09:00

**「可关注」** 可关注：LVMH 旗下出版物接入 ChatGPT 的具体交互形式、内容授权边界及后续落地节奏。

**标签**: `#industry`, `#lab`, `#product`

---

<a id="item-ai-daily-4"></a>
### [OpenAI 发布科研用 ChatGPT 报告](https://openai.com/index/science-at-the-frontier) ⭐️ 7.8/10

OpenAI 官方博客于 2026 年 11 月 16 日发布科研使用报告，披露 1800 余名科学家将 ChatGPT 用于科研场景的相关研究发现。报告覆盖日常科研流程、报告撰写环节的生产力提升反馈，以及对科研发现的预期三类核心内容。

rss · OpenAI Blog · 11月16日 12:00

**「为什么重要」** 该报告为 OpenAI 官方披露的科研场景大模型使用实证数据，可反映 AI 在专业领域的落地应用现状。

**「可关注」** 可关注：报告中提及的科研场景下 ChatGPT 使用环节与用户反馈的生产力数据。

**标签**: `#lab`, `#industry`, `#product`, `#research`

---

<a id="item-ai-daily-5"></a>
### [OpenAI 启动首阶段嵌入式评估](https://openai.com/index/our-first-phase-of-embedded-assessments) ⭐️ 7.8/10

OpenAI 启动首阶段嵌入式评估，联合 Apollo Research、METR、Transluce、Goodfire 四家外部研究机构，对模型对齐、安全防护机制及监控系统开展独立评估。

rss · OpenAI Blog · 11月16日 08:00

**「为什么重要」** 这是 OpenAI 首次引入外部独立研究机构开展嵌入式模型安全评估，第三方介入的验证模式或为行业模型安全治理提供新的参考路径。

**「可关注」** 可关注：首阶段评估的后续公开结果，以及第三方独立评估维度的后续扩展情况。

**标签**: `#lab`, `#eval`, `#policy`, `#industry`

---

<a id="item-ai-daily-6"></a>
### [OpenAI 扩展 ChatGPT 医疗能力](https://openai.com/index/more-ways-to-move-care-forward-with-chatgpt-for-healthcare) ⭐️ 7.8/10

OpenAI 于 2026 年 11 月 16 日宣布扩展 ChatGPT 的医疗场景能力，新增三类功能：计算机使用代理、优化后的临床回答、可跨医疗软件互操作的新插件。这些功能旨在让 ChatGPT 在医疗领域完成实际工作任务。

rss · OpenAI Blog · 11月16日 06:00

**「为什么重要」** 这是 OpenAI 官方发布的医疗场景具体产品能力更新，覆盖工具操作、回答质量、系统对接三个方向，推动生成式 AI 在医疗场景从纯问答向实际工作流延伸。

**「可关注」** 可关注：新增医疗插件的跨系统互操作标准，以及计算机使用代理在医疗场景的权限控制与合规边界。

**标签**: `#lab`, `#product`, `#industry`

---

## AI 羊毛
{: #sec-ai-deals .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-deals" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-deals-1"></a>
### [BrowserPod 4.0 浏览器 MicroVM 免费开放](https://browserpod.io/blog/browserpod-40/) ⭐️ 6.0/10

BrowserPod 官方宣布 4.0 版本的浏览器端 MicroVM 现已免费开放任意使用，当前未明确具体有效期、使用限制、地区限制等规则。

rss · HN Free API / Credits · 11月16日 12:41

**「为什么重要」** 该工具支持在浏览器内运行 MicroVM，对需要轻量浏览器端虚拟化能力的开发者而言属于免费可用资源，但完整使用规则尚未公开。

**「可关注」** 可关注：面向需要浏览器端 MicroVM 能力的开发者，当前无明确使用门槛，但需留意后续官方规则更新。

**标签**: `#free-tier`, `#dev-tool`, `#promo`

---

<a id="item-ai-deals-2"></a>
### [Supabase Free 周备份工具开源](https://github.com/liulewis/supabase-free-backup-lite) ⭐️ 5.0/10

社区开发者 agricalc 开源了 supabase-free-backup-lite 工具，可免费为 Supabase Free 项目提供每周自动数据库备份，备份通过 pg\_dump 存储到 Cloudflare R2。该工具无使用费用，但需要用户自行托管、完成配置，且需持有独立的 Cloudflare R2 账户。无官方服务背书，无附带免费额度可领取。

rss · HN Free API / Credits · 11月17日 01:13

**「为什么重要」** Supabase Free 官方不提供自动备份能力，该工具填补了免费 tier 的备份空白，适合有自托管能力、需要低成本备份 Supabase 项目的用户。

**「可关注」** 可关注：需自行部署配置，且依赖独立的 Cloudflare R2 账户，无官方运维支持。

**标签**: `#limited-free`, `#free-tier`, `#open-source`

---