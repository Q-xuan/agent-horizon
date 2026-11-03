---
layout: default
title: "Horizon Summary: 2026-11-03 (ZH)"
date: 2026-11-03
lang: zh
---

> 从 183 条内容中筛选出 15 条重要资讯。

<nav id="ah-toc" class="ah-toc" aria-label="目录"><span class="ah-toc-title">目录</span><ul><li><a href="#sec-harness-arch"><span class="ah-toc-name">Harness 架构</span><span class="ah-toc-count">3条</span></a></li><li><a href="#sec-agent-engineer"><span class="ah-toc-name">Agent 工程师日报</span><span class="ah-toc-count">7条</span></a></li><li><a href="#sec-ai-daily"><span class="ah-toc-name">AI 日报</span><span class="ah-toc-count">5条</span></a></li></ul></nav>

---

**[Harness 架构](#sec-harness-arch)**
1. [Mastra v1.81.0 发布](#item-harness-arch-1) ⭐️ 8.8/10
2. [google/adk-go v2.7.0 发布](#item-harness-arch-2) ⭐️ 8.8/10
3. [pydantic-ai v2.65.0 发布](#item-harness-arch-3) ⭐️ 7.8/10

**[Agent 工程师日报](#sec-agent-engineer)**
1. [OpenAI 内部 Git 扩展实践公开](#item-agent-engineer-1) ⭐️ 8.0/10
2. [HF 论文：ProVe 提议者-验证器解码](#item-agent-engineer-2) ⭐️ 7.5/10
3. [TinyAstral 自演化 Harness 迁移蒸馏小模型](#item-agent-engineer-3) ⭐️ 7.0/10
4. [ReTrace 可扩展评估框架发布](#item-agent-engineer-4) ⭐️ 7.0/10
5. [UID-Conj. 辅助奖励提升小模型推理](#item-agent-engineer-5) ⭐️ 7.0/10
6. [LLM CLI 0.37 发布](#item-agent-engineer-6) ⭐️ 6.8/10
7. [Legora 法律 Agent 隐私构建实践](#item-agent-engineer-7) ⭐️ 5.5/10

**[AI 日报](#sec-ai-daily)**
1. [OpenAI 发布 Git 兼容后端 Pando](#item-ai-daily-1) ⭐️ 7.8/10
2. [OpenAI 上调 Security Bug Bounty 标准](#item-ai-daily-2) ⭐️ 7.8/10
3. [OpenAI LifeVal 基准测试发布](#item-ai-daily-3) ⭐️ 7.8/10
4. [OpenAI 启动电网守护者计划](#item-ai-daily-4) ⭐️ 6.8/10
5. [OpenAI 筹备下一轮内部安全冲刺](#item-ai-daily-5) ⭐️ 6.8/10

---

## Harness 架构
{: #sec-harness-arch .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-harness-arch" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-harness-arch-1"></a>
### [Mastra v1.81.0 发布](https://github.com/mastra-ai/mastra/releases/tag/%40mastra/core%401.81.0) ⭐️ 8.8/10

Mastra v1.81.0 发布，核心新增存储支持的 MCP 任务，实现可重启的长任务执行与跨实例轮询/取消。后台任务扩展至非 agent 所有者，支持 expiresAt/metadata 保留、per-owner 并发覆盖及队列恢复。可观测性增加执行 outcome、类型化 stopReason 及首 token 延迟（TTFT）测量，支持 ClickHouse、DuckDB、Postgres 等存储查询。

github · PaulieScanlon · 11月2日 12:33

**「设计要点」** MCP 任务通过共享存储适配器实现重启安全，后台任务状态（队列、保留、并发）持久化至存储层。可观测性统一 outcome/stopReason/stopReasonContext 字段，允许 null 值，TripWire 错误以独立类型跨 worker 序列化。

**「改了什么」** \- @mastra/mcp 新增实验性存储支持的 MCP 任务，长工具/代理/工作流立即返回 task ID，支持跨实例轮询、回答、取消及重启恢复
\- 后台任务支持非 agent 所有者（如 MCP 服务器），新增 expiresAt/metadata 保留、per-owner 并发覆盖、\{ onNoSlot: &\#x27;queue&\#x27; \} 队列恢复，存储适配器同步持久化新字段
\- 可观测性记录执行 outcome 与类型化 stopReason，新增 timeToFirstTokenMs，支持按 model/provider 分组，覆盖 ClickHouse/DuckDB/Postgres
\- 新增 savedViewStateSchema、savedViewStateEnvelopeSchema、filterNodeSchema，支持自定义仪表板和保存视图定义
\- 通道代理支持认证二进制附件下载至 channel-attachments/，默认 100 MiB 上限，可通过 maxAttachmentStorageBytes 调整
\- 破坏性变更：@mastra/playground-ui 移除 ChartCard description/summary、MetricsCard.\* 组件、fluid-hover 工具；@mastra/core 移除 network/vNext 和 telemetry/otel-vNext 子路径；@mastra/factory 弃用 defineBoard\(\) 及 boards/includeDefaultBoards 字段

**标签**: `#mcp`, `#runtime`, `#tools`, `#observability`

---

<a id="item-harness-arch-2"></a>
### [google/adk-go v2.7.0 发布](https://github.com/google/adk-go/releases/tag/v2.7.0) ⭐️ 8.8/10

google/adk-go v2.7.0 发布。本次更新引入 Anthropic Claude 作为一等公民模型（experimental），新增 search-gated tool discovery 机制管理大型 MCP 工具目录，并添加实验性 classifier API 支持工作流路由。模型调用默认限制为 500 次/invocation，遥测默认切换至 OpenTelemetry GenAI semantic conventions v2，后者对现有 trace 消费者构成 breaking change。此外修复 MCP 会话隔离、auth 凭证 mint 失败等问题，Go 版本要求提升至 1.26.10。

github · wolo-lab · 11月2日 10:37

**「设计要点」** 运行时基于 Go 1.26.10，工具层通过 \`tool/toolsearch\` 包装器将大型 MCP 目录从请求中解耦，模型检索后动态声明工具。记忆层 in-memory memory search 跳过 thought parts；权限与遥测层面，MCP 会话按用户凭证隔离，trace 默认采用 OpenTelemetry GenAI v2 语义约定。

**「改了什么」** 新增 Anthropic Claude 模型提供者（\`model/anthropicmodel\`）、search-gated 工具发现、实验性分类器 API 及每调用模型预算上限。遥测格式、模型调用上限行为、可选占位符错误传播及 Go 最低版本要求发生 breaking change。

**标签**: `#runtime`, `#tools`, `#mcp`, `#planning`

---

<a id="item-harness-arch-3"></a>
### [pydantic-ai v2.65.0 发布](https://github.com/pydantic/pydantic-ai/releases/tag/v2.65.0) ⭐️ 7.8/10

pydantic-ai v2.65.0 发布，包含工具与运行时增量改进、gh-aw 会话保护及多项破坏性变更。新增 OpenAI Responses WebSocket 传输、ConversationStore 对话存储、AskUserAnswer 多模态注释，以及 OpenRouter 与 Claude 模型的中途系统提示支持。调整 ModelFallback 拒绝回退逻辑，将 Z.ai 429 映射为 ModelQuotaExceededError，并在 V2 移除名称导入时提示替换名。默认禁止 Temporal 重试不可重试模型错误，同时修复 Bedrock 错误类型映射、Coder 工具错误返回及 BrowserUse 用量统计等问题，要求 daytona&gt;=0.226.1。

github · dsfaccini · 11月3日 01:25

**「设计要点」** 运行时层通过 non\_retryable\_model\_errors 默认禁止 Temporal 重试 ContentFilterError 等不可重试模型错误。工具层新增 ConversationStore 以消息日志形式存储对话并支持冲突修订，同时保护 gh-aw 规范会话捕获免受 agent 工具访问。

**「改了什么」** 新增 OpenAI Responses WebSocket 传输与 ConversationStore；调整 ModelFallback 拒绝回退及 Z.ai 429 错误类型为 ModelQuotaExceededError，V2 移除名称导入时提示替换名。保护 gh-aw 会话捕获并默认禁止 Temporal 重试不可重试模型错误；修复 Bedrock 错误映射、Coder 工具错误返回、BrowserUse 用量统计、FileSystem 事件前缀及 Anthropic 历史容器发送；要求 daytona&gt;=0.226.1。

**标签**: `#runtime`, `#tools`, `#permissions`, `#sandbox`

---

## Agent 工程师日报
{: #sec-agent-engineer .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-agent-engineer" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-agent-engineer-1"></a>
### [OpenAI 内部 Git 扩展实践公开](https://openai.com/index/scaling-git-at-openai/) ⭐️ 8.0/10

2026 年 11 月 2 日 OpenAI 官方工程博客发布《Scaling Git at OpenAI》，披露内部 Git 基础设施扩展方案，以及使用自研编码代理 Codex 在 10 周内构建生产级源码管理工具 Pando 的实践。Pando 由 1 名工程师设计核心、多组编码代理实现、少量工程师部署，2026 年 4 月起承担生产流量，是 OpenAI 内部源码管理工具体系的组成部分。社区评论指出该博客未披露每秒推送数、并发推送者数等性能基准数据。

hackernews · makeramen · 11月2日 23:47 · [社区讨论](https://news.ycombinator.com/item?id=50345924)

**「为什么重要」** 该博客是 OpenAI 首次公开大规模内部 Git 基础设施扩展的一手工程实践，同时提供了使用自研编码代理快速构建生产级代码管理工具的完整案例，对编码代理工具链设计、企业内部代码基础设施优化有直接参考价值。目前尚未有公开数据验证 Pando 的实际性能表现与大规模落地效果。

**「可关注」** 可关注：OpenAI 披露的编码代理参与生产级工具构建的实践细节，以及社区提出的全局 Git 缓存方案、性能基准数据缺失等讨论点。

**「评论」** 社区对该博客的评价整体偏正面，认可其无营销话术、细节详实且附带数据可视化的特点；同时存在分歧，部分用户指出博客未披露核心性能基准数据，另有用户提出可参考 pnpm 的全局缓存思路优化 Git 下载速度。

**标签**: `#coding-agent`

---

<a id="item-agent-engineer-2"></a>
### [HF 论文：ProVe 提议者-验证器解码](https://huggingface.co/papers/2610.27815) ⭐️ 7.5/10

2026 年 11 月 3 日 Hugging Face 每日论文收录 ProVe（提议者-验证器解码）技术，该技术反转传统推测解码中小模型草稿、大模型验证的角色，从标准自回归（AR）检查点微调大模型作为提议者，单次前向传播生成待验证的 token 块，再通过一次额外前向传播完成验证。验证器可使用小 AR 模型或提议者自身，后者为 ProVe-lossless 模式，可完全复现提议者的贪心 AR 解码输出。目前公开 6 个基准的实测数据，块大小为 16 时在 GSM8K 上平均匹配 6.6 个 AR token，该技术可直接用于优化 AI Agent 的 LLM 调用链路，降低推理延迟与成本。

rss · Hugging Face Daily Papers · 11月3日 00:00

**「为什么重要」** 该技术打破了传统推测解码的角色分工限制，lossless 模式可保证输出与标准自回归解码完全一致，同时提供可量化的推理加速收益，可直接作用于 AI Agent 的 LLM 调用链路优化。

**「可关注」** 可关注 ProVe-lossless 模式下大模型同时担任提议者与验证器的实现成本，以及块大小与不同基准的 token 匹配率 trade-off。

**标签**: `#harness`

---

<a id="item-agent-engineer-3"></a>
### [TinyAstral 自演化 Harness 迁移蒸馏小模型](https://huggingface.co/papers/2610.41216) ⭐️ 7.0/10

11 月 3 日发布的论文提出 TinyAstral 两阶段方法，将大模型教师 agent 的 harness 优化迁移至蒸馏小型 agent。第一阶段冻结开源教师模型，通过递归自我改进（RSI）演化 harness：前沿 LLM agent 读取教师轨迹并提出编辑，仅当通过配对统计检验时接受。第二阶段冻结最终 harness，收集含推理与失败恢复的教师轨迹，蒸馏小型学生 agent 并在相同 harness 中替换教师。该方法在 RoboTwin 基准上验证有效性，但原文截断未披露具体成功率提升数值。

rss · Hugging Face Daily Papers · 11月3日 00:00

**「为什么重要」** 该工作证明 harness 作为 agent 系统可优化组件，其改进可通过蒸馏跨模型规模迁移。对各类 agent 工具链设计有直接参考价值，但跨领域泛化效果尚未证实。

**「可关注」** 可关注：harness 的递归自我改进结合配对统计检验，可迁移至蒸馏小模型并保持性能。

**标签**: `#harness`, `#eval`, `#robotics`, `#distillation`

---

<a id="item-agent-engineer-4"></a>
### [ReTrace 可扩展评估框架发布](https://huggingface.co/papers/2610.27954) ⭐️ 7.0/10

2026-11-03，Hugging Face Daily Papers 聚合 arXiv 预印本论文《Lost in Recovery: Demystifying Recovery Behavior of Computer-Use Agents via Goal-Oriented Action Replay》，提出 ReTrace 可扩展评估框架。该框架形式化 Transition-Consistent 恢复机制，系统性研究长 horizon 计算机使用智能体在键盘鼠标操作中的故障恢复行为。现有恢复方案存在三类局限：环境重置在专有场景不可行、动作回放在长 horizon 下成本 prohibitive、API 回滚仅限 Web 环境。ReTrace 填补了模型恢复评估空白，但尚未经过生产级落地验证。

rss · Hugging Face Daily Papers · 11月3日 00:00

**「为什么重要」** 长 horizon 计算机使用智能体的错误累积与副作用问题日益突出，现有恢复手段覆盖不足。ReTrace 提供了首个系统化评估模型恢复行为的可扩展框架，对 coding agent 的评测体系设计和长流程自动化开发有直接参考价值。

**「可关注」** 可关注：长 horizon 场景下，环境重置、动作回放、API 回滚三类恢复方案均存在明确边界，模型驱动的恢复行为评估仍是空白，ReTrace 的形式化框架可作为评测基准参考。

**标签**: `#eval`, `#coding-agent`, `#orchestration`

---

<a id="item-agent-engineer-5"></a>
### [UID-Conj. 辅助奖励提升小模型推理](https://huggingface.co/papers/2610.41296) ⭐️ 7.0/10

2026-11-03，Hugging Face Daily Papers 收录论文提出 UID-Conj. 熵基辅助奖励指标，用于小语言模型自我改进与推理迁移。该指标结合全局熵变化与局部平滑度，在 Qwen3-1.7B 上通过在线奖励增强（30 道无参考答案 AIME 题）和离线加权 SFT（历史 AIME 题）实验，相比未修改 TTRL 基线，在适配基准与三个迁移基准的在线宏平均上提升 2.08 个百分点。论文最强证据部分内容截断，离线加权 SFT 的具体结果未完整呈现。

rss · Hugging Face Daily Papers · 11月3日 00:00

**「为什么重要」** 该工作提供了一种在有限监督下提升小模型推理能力的技术路径，其熵基辅助奖励设计对 agent 推理改进与评估有参考价值。不过当前证据主要来自 AIME 数学基准，迁移到其他任务域的效果尚未证实。

**「可关注」** 可关注：答案级奖励无法区分等正确推理轨迹，UID-Conj. 通过轨迹级熵基偏好信号在有限数据下提升小模型自我改进，这对构建低资源 agent 训练 harness 有直接参考。

**标签**: `#eval`, `#harness`

---

<a id="item-agent-engineer-6"></a>
### [LLM CLI 0.37 发布](https://github.com/simonw/llm/releases/tag/0.37) ⭐️ 6.8/10

simonw/llm 于 2026-11-02 发布 0.37 官方小版本，面向使用 LLM CLI 做模型调用、嵌入、工具链开发的工程师。本次更新新增 gpt-6.1-sol、gpt-6.1-terra、chat-latest 三个 OpenAI 模型支持，未自定义默认模型的用户默认模型从 GPT-5.6 Luna 切换为 GPT-6 Luna，同时新增 llm openai endpoint add/list/remove/path 四条命令用于管理 OpenAI 兼容模型端点。嵌入能力新增带 MIME 类型的附件支持，llm chat 新增 --usage 参数可在每轮对话后输出 token 用量，Python API 新增 chain.on\_response 回调方法。此外本次更新支持 Python 3.15、停止支持 Python 3.10，移除了 gpt-3.5-turbo、gpt-4、o1 等已停服的 OpenAI 模型及别名，同时修复了 llm chat 关闭日志仍写入、llm embed-multi 非 ASCII 文件乱码、多进程写日志 SQLITE\_BUSY、工具链 chain limit 误报等多项 bug。

github · simonw · 11月2日 23:49

**「为什么重要」** 本次更新覆盖了模型接入、嵌入处理、工具链稳定性三个 LLM CLI 高频使用场景的痛点，默认模型切换和旧模型移除会直接影响未自定义配置的用户使用成本，新增的端点管理命令降低了 OpenAI 兼容模型的接入门槛，bug 修复解决了并发日志、嵌入数据损坏等实际生产中的问题。

**「可关注」** 可关注：未自定义默认模型的用户升级后默认模型会切换为 GPT-6 Luna，可通过 llm models default gpt-5.6-luna 回退；使用 llm embed-multi --files 处理过非 ASCII 文件的用户需重新运行命令修复已损坏的集合。

**标签**: `#harness`

---

<a id="item-agent-engineer-7"></a>
### [Legora 法律 Agent 隐私构建实践](https://latent.space/p/building_legal_agents_when_you_can_t_see_the_data_-_jacob_lauritzen_cto_of_legora/) ⭐️ 5.5/10

2026 年 11 月 2 日 Latent Space 发布播客访谈，嘉宾为法律科技公司 Legora CTO Jacob Lauritzen。Legora 因客户数据归属合作律所，完全无法观测其法律 Agent 的运行轨迹，本次访谈分享了该团队在严格数据隐私约束下构建、测试 Agent 的工程实践。关键可验证细节包括：团队曾长期拒绝添加模型选择器后新增该功能；一次基础模型更新后 Agent 引用准确率从 70%升至 99%，未调整其他业务逻辑；测试环境仿照客户真实工作场景搭建，类似强化学习中的“世界”；核心产品包括可处理百万单元格的 Tabular Review 表格工具，产品整体运行在 Azure 平台且未使用 ElevenLabs。本次内容为播客访谈摘要，未披露具体实现代码、可复现评估基准或隐私合规的具体技术方案，相关实践对医疗、金融等同样受严格数据隐私约束的垂直领域 AI Agent 开发者有参考价值。

rss · Latent Space · 11月2日 22:54

**「为什么重要」** 这是少数公开讨论“完全不可观测 Agent 运行轨迹”场景的工程实践，填补了高隐私约束垂直领域 Agent 开发的公开经验空白。其测试环境设计、隐私下的可观测性替代方案是否可复用到其他垂直领域尚未验证。

**「可关注」** 可关注：完全不可观测 Agent 轨迹的场景下，可通过仿照真实业务场景搭建类强化学习测试环境、 paraphrase traces 缩小故障范围的方式补足可观测性，且基础模型能力提升可直接带来业务指标跃升，无需额外调整业务逻辑。

**标签**: `#observability`, `#permissions`, `#harness`, `#eval`, `#coding-agent`

---

## AI 日报
{: #sec-ai-daily .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-daily" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-daily-1"></a>
### [OpenAI 发布 Git 兼容后端 Pando](https://openai.com/index/scaling-git-at-openai) ⭐️ 7.8/10

OpenAI 官方博客 2026 年 11 月 2 日披露，其开发了 Git 兼容后端 Pando，专门适配 Codex 工具带来的大规模开发场景需求。该后端定位为支撑 Codex 相关开发流程的基础设施，目前未公开具体性能指标与开源计划。

rss · OpenAI Blog · 11月2日 15:30

**「为什么重要」** Pando 作为 Codex 的底层 Git 基础设施，直接决定大规模 AI 辅助开发场景的可用性与扩展上限，是 OpenAI 开发工具链的核心底层组件。

**「可关注」** 可关注：Pando 保持 Git 协议兼容，现有 Git 工作流理论上可平滑迁移对接。

**标签**: `#lab`, `#product`, `#industry`

---

<a id="item-ai-daily-2"></a>
### [OpenAI 上调 Security Bug Bounty 标准](https://openai.com/index/rewarding-defenders-with-bigger-bug-bounties) ⭐️ 7.8/10

OpenAI 宣布提高 Security Bug Bounty 的奖励额度，同时面向独立安全研究人员新增报告质量、忠诚度、优先活动三类奖金结构。该政策仅适用于通过官方渠道提交有效漏洞报告的研究人员，未披露各档奖励的具体金额。

rss · OpenAI Blog · 11月2日 18:00

**「为什么重要」** 更高的奖励预期与多维度奖金机制，能够激励更多独立安全研究人员参与 OpenAI 产品安全漏洞的挖掘与提交，缩短漏洞修复周期。

**「可关注」** 可关注 OpenAI 官方漏洞提交页面的规则更新，确认新增三类奖金的申报门槛与审核标准。

**标签**: `#policy`, `#lab`, `#industry`

---

<a id="item-ai-daily-3"></a>
### [OpenAI LifeVal 基准测试发布](https://openai.com/index/lifeval) ⭐️ 7.8/10

OpenAI 官方发布 LifeVal 基准测试，用于衡量 AI 协助完成日常现实任务的能力。测试覆盖托儿服务查找、财务管理、政府文书处理等场景。目前披露的细节较少，未公布具体测试维度与评分标准。

rss · OpenAI Blog · 11月2日 09:00

**「可关注」** 可关注：LifeVal 覆盖托儿服务、财务与政府文书等日常任务场景，后续评分标准与数据集值得跟踪。

**标签**: `#eval`, `#lab`

---

<a id="item-ai-daily-4"></a>
### [OpenAI 启动电网守护者计划](https://openai.com/index/grid-protectors-program) ⭐️ 6.8/10

OpenAI 正式推出电网守护者计划（Grid Protectors Program），将与电力企业合作，推动未来 AI 算力园区支撑电网可靠性、保护消费者用电成本。当前公开信息未披露具体合作方、落地细节与推进时间表。

rss · OpenAI Blog · 11月2日 15:00

**「为什么重要」** AI 算力规模持续扩张对电网承载能力提出更高要求，该计划是面向算力基础设施与电网协同的公开合作框架，对后续 AI 产业能源布局有参考价值。

**「可关注」** 可关注：该计划后续披露的电力合作方、算力园区电网接入标准与用电成本分摊规则。

**标签**: `#lab`, `#industry`, `#policy`

---

<a id="item-ai-daily-5"></a>
### [OpenAI 筹备下一轮内部安全冲刺](https://openai.com/index/preparing-our-next-security-sprint-to-harden-openai) ⭐️ 6.8/10

OpenAI 官方博客宣布，公司正与合作伙伴 Cathedral Systems 筹备下一轮内部安全冲刺，计划通过 AI 技术测试并强化自身防御能力。当前公告未披露具体落地细节、时间安排与影响范围。

rss · OpenAI Blog · 11月2日 18:00

**「为什么重要」** 这是 OpenAI 公开披露的 AI 系统安全强化新动作，反映行业对 AI 自身防御能力建设的关注持续升温。

**「可关注」** 可关注：OpenAI 后续是否会公开该安全冲刺的具体测试框架与防御优化成果。

**标签**: `#lab`, `#industry`

---