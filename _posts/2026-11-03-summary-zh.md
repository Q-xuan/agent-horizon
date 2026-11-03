---
layout: default
title: "Horizon Summary: 2026-11-03 (ZH)"
date: 2026-11-03
lang: zh
---

> 从 181 条内容中筛选出 16 条重要资讯。

<nav id="ah-toc" class="ah-toc" aria-label="目录"><span class="ah-toc-title">目录</span><ul><li><a href="#sec-harness-arch"><span class="ah-toc-name">Harness 架构</span><span class="ah-toc-count">4条</span></a></li><li><a href="#sec-agent-engineer"><span class="ah-toc-name">Agent 工程师日报</span><span class="ah-toc-count">7条</span></a></li><li><a href="#sec-ai-daily"><span class="ah-toc-name">AI 日报</span><span class="ah-toc-count">5条</span></a></li></ul></nav>

---

**[Harness 架构](#sec-harness-arch)**
1. [google/adk-go v2.7.0 发布](#item-harness-arch-1) ⭐️ 8.8/10
2. [@mastra/core@1.81.0 发布](#item-harness-arch-2) ⭐️ 7.8/10
3. [pydantic-ai v2.65.0 发布](#item-harness-arch-3) ⭐️ 6.8/10
4. [微软开源 MCP 初学者入门课程](#item-harness-arch-4) ⭐️ 5.0/10

**[Agent 工程师日报](#sec-agent-engineer)**
1. [TinyAstral 自进化 Harness 迁移](#item-agent-engineer-1) ⭐️ 7.0/10
2. [ReTrace 框架：智能体恢复行为评估](#item-agent-engineer-2) ⭐️ 7.0/10
3. [ProVe 推测解码论文发布](#item-agent-engineer-3) ⭐️ 7.0/10
4. [OpenAI Git 扩展策略发布](#item-agent-engineer-4) ⭐️ 7.0/10
5. [llm 0.37 发布 支持多模态嵌入](#item-agent-engineer-5) ⭐️ 6.0/10
6. [HF 每日论文：ReGap-Bench 基准发布](#item-agent-engineer-6) ⭐️ 6.0/10
7. [DeepSeek-V4.1-Flash-1017 1bit Coder 发布](#item-agent-engineer-7) ⭐️ 5.5/10

**[AI 日报](#sec-ai-daily)**
1. [OpenAI 安全漏洞赏金计划升级](#item-ai-daily-1) ⭐️ 8.8/10
2. [OpenAI 发布 LifeVal 日常基准](#item-ai-daily-2) ⭐️ 8.8/10
3. [OpenAI 发布 Pando Git 兼容后端](#item-ai-daily-3) ⭐️ 7.8/10
4. [OpenAI 推出 Grid Protectors Program](#item-ai-daily-4) ⭐️ 7.8/10
5. [OpenAI 筹备内部安全冲刺](#item-ai-daily-5) ⭐️ 6.8/10

---

## Harness 架构
{: #sec-harness-arch .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-harness-arch" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-harness-arch-1"></a>
### [google/adk-go v2.7.0 发布](https://github.com/google/adk-go/releases/tag/v2.7.0) ⭐️ 8.8/10

Google ADK Go v2.7.0 正式发布。新增 Anthropic Claude 模型支持（实验性）、搜索门控工具发现、实验性分类器 API 及单次调用模型预算上限。默认切换至 OpenTelemetry GenAI 语义约定 v2，构成遥测消费方的破坏性变更。同步修复 MCP 会话认证、工作流连接恢复、LoopAgent 取消行为及 Go 版本要求至 1.26.10。

github · wolo-lab · 11月2日 10:37

**「设计要点」** 运行时通过 \`RunConfig.MaxLLMCalls\` 在单次 invocation 上硬截断模型调用链，默认 500 次并返回 \`agent.ErrLLMCallsLimitExceeded\`。工具层与遥测层分别引入 \`tool/toolsearch\` 包装器（按需声明大型 MCP 目录工具）和 OpenTelemetry GenAI semantic conventions v2（消息内容以结构化值写入 span）。

**「改了什么」** 新增 \`model/anthropicmodel\`、\`tool/toolsearch\` 与 \`exp/classifier\`，分别提供 Anthropic Claude 模型支持（实验性）、大型 MCP 目录搜索门控发现及类型化工作流路由。默认启用 OpenTelemetry GenAI v2 遥测格式，旧版可通过 \`ADK\_TELEMETRY\_SCHEMA\_VERSION\_OPT\_IN=otel\_semconv\_1\_36\` 回退至 2027-03-31，同时单次 invocation 模型调用默认上限 500 次，可通过 \`RunConfig.MaxLLMCalls\` 或 \`ADK\_MAX\_LLM\_CALLS\` 调整，\`-1\` 表示无限制。

**标签**: `#tools`, `#runtime`, `#mcp`, `#planning`

---

<a id="item-harness-arch-2"></a>
### [@mastra/core@1.81.0 发布](https://github.com/mastra-ai/mastra/releases/tag/%40mastra/core%401.81.0) ⭐️ 7.8/10

@mastra/core@1.81.0 发布实验性存储支持的 MCP 任务，实现重启安全的长运行执行。背景任务扩展至非 agent 所有者，支持保留期、并发控制和排队恢复。可观测性增加执行结果、停止原因、模型/提供商导出及首 token 延迟（TTFT）测量。同时引入认证通道附件下载和工厂作用域沙箱环境。

github · PaulieScanlon · 11月2日 12:33

**「设计要点」** MCP 任务通过共享存储实现跨实例轮询、应答和取消，确保重启安全；背景任务采用 per-owner 并发覆盖与 onNoSlot 队列，存储适配器持久化 expiresAt 和 metadata；可观测性层统一记录 outcome、stopReason 及 TTFT，支持 ClickHouse、DuckDB 和 Postgres 查询分组。

**「改了什么」** 新增实验性 storage-backed MCP tasks 实现重启安全长运行执行；背景任务开放非 agent 所有者并增加保留、并发与排队恢复；可观测性增加 outcome、stopReason、model/provider 导出及 TTFT 测量；同时引入认证附件下载、factory 作用域沙箱和 setCookies\(\)。Breaking changes 包括 playground-ui API 清理、移除 @mastra/core/network/vNext 与 @mastra/core/telemetry/otel-vendor 子路径，以及 defineBoard\(\) 和 MastraFactory boards 废弃。

**标签**: `#mcp`, `#runtime`, `#tools`, `#subagents`, `#eval`

---

<a id="item-harness-arch-3"></a>
### [pydantic-ai v2.65.0 发布](https://github.com/pydantic/pydantic-ai/releases/tag/v2.65.0) ⭐️ 6.8/10

pydantic-ai v2.65.0 正式发布，带来运行时行为调整与工具功能增量。新增 BrowserUse 调用量统计、AskUserAnswer 多模态支持、OpenAI Responses WebSocket 传输及 12h 提示缓存。调整 ModelFallback 在模型拒绝时的回退逻辑，并将 Z.ai 的 429 错误映射为 ModelQuotaExceededError。本次更新无核心架构改动，但包含若干破坏性行为变更。

github · dsfaccini · 11月3日 01:25

**「改了什么」** 相对 v2.64.0，v2.65.0 新增 BrowserUse 调用量统计、AskUserAnswer 多模态支持、OpenAI Responses WebSocket 传输及 ConversationStore 会话存储。破坏性变更包括 ModelFallback 在模型拒绝时触发回退、Z.ai 429 错误改为 ModelQuotaExceededError，以及 Temporal 默认停止重试不可重试的模型错误。

**标签**: `#runtime`, `#tools`

---

<a id="item-harness-arch-4"></a>
### [微软开源 MCP 初学者入门课程](https://github.com/microsoft/mcp-for-beginners) ⭐️ 5.0/10

这是微软官方开源的面向开发者的 Model Context Protocol（MCP）入门学习资源，2026 年 11 月 3 日登上 GitHub Trending。课程提供.NET、Java、TypeScript、JavaScript、Rust、Python 六种语言的实际案例，覆盖从会话配置到服务编排的模块化、可扩展、安全 AI 工作流构建方法，未公开版本号、接口规范或使用限制。

rss · GitHub Trending Daily · 11月3日 03:48

**标签**: `#mcp`, `#tools`

---

## Agent 工程师日报
{: #sec-agent-engineer .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-agent-engineer" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-agent-engineer-1"></a>
### [TinyAstral 自进化 Harness 迁移](https://huggingface.co/papers/2610.41216) ⭐️ 7.0/10

2026 年 11 月 3 日，Hugging Face Daily Papers 收录论文 TinyAstral，提出两阶段方法将自我进化的 agent harness 迁移至紧凑操作 agent。第一阶段冻结开源教师模型，通过递归自我改进\(RSI\)优化 harness：前沿 LLM agents 读取教师轨迹提出编辑，仅通过配对统计测试的编辑被接受。第二阶段冻结最终 harness，收集含推理与失败恢复的教师轨迹，蒸馏小模型学生并在相同 harness 中替换教师。论文在 RoboTwin 基准评估，harness 进化提升教师成功率，但具体数值及学生模型性能数据在提供片段中缺失。

rss · Hugging Face Daily Papers · 11月3日 00:00

**「为什么重要」** 该工作验证 harness 可独立于模型权重进化并跨规模迁移，为降低 agent 推理成本提供路径。但 RoboTwin 为物理操作任务基准，其结论向 coding agent 场景的迁移仍需验证。

**「可关注」** Harness 可视为独立迭代组件，通过 LLM 生成编辑并辅以统计验证，再蒸馏小模型复用优化后的工具链与恢复逻辑。

**标签**: `#harness`, `#eval`, `#orchestration`

---

<a id="item-agent-engineer-2"></a>
### [ReTrace 框架：智能体恢复行为评估](https://huggingface.co/papers/2610.27954) ⭐️ 7.0/10

2026 年 11 月 3 日 Hugging Face Daily Papers 收录一篇研究论文，提出 ReTrace 可扩展评估框架，用于系统研究长时序计算机使用智能体的故障恢复行为。当前该领域现有恢复方案存在明确空白：专有场景环境重置不可行、长时序动作回放成本极高、API 回滚仅适用于 Web 环境，ReTrace 填补了该研究缺口。公开摘要内容截断，未包含完整技术细节、实验验证数据与框架使用方法，该研究对智能体评测、工具链及计算机使用智能体开发从业者有直接参考价值。

rss · Hugging Face Daily Papers · 11月3日 00:00

**「为什么重要」** 长时序计算机使用智能体的恢复能力是当前落地关键瓶颈，ReTrace 框架为相关能力评估提供了新的研究路径，不过完整技术细节与实验验证结果尚未公开，实际可用性待进一步确认。

**「可关注」** 可关注：当前长时序计算机使用智能体的恢复能力缺乏通用评估方案，现有环境重置、动作回放、API 回滚三类恢复手段均存在明确的适用边界限制。

**标签**: `#eval`, `#coding-agent`, `#harness`

---

<a id="item-agent-engineer-3"></a>
### [ProVe 推测解码论文发布](https://huggingface.co/papers/2610.27815) ⭐️ 7.0/10

Hugging Face Daily Papers 于 2026-11-03 收录论文 ProVe: Proposer-Verifier Decoding。该工作反转传统推测解码角色：将大模型微调为提议者，单前向传播预测未来 token 块，再由验证者用一次额外前向传播校验。论文提供无损变体 ProVe-lossless，以提议者自身作验证者复现贪婪自回归解码。初步基准显示 block size 16 时 GSM8K 平均 AR-matching prefix 达 6.6 tokens。当前材料截断于 32B 模型描述，完整基准对比与加速比数据未完全展示。该方向对做 LLM 推理加速与 agent 推理优化的工程师有参考价值。

rss · Hugging Face Daily Papers · 11月3日 00:00

**「为什么重要」** 论文提出的大模型块提议者范式，与现有小模型草稿、大模型验证的推测解码路径形成对比。初步基准和无损变体提供了可验证的起点，但实际加速收益、微调成本及在 agent 长链路推理中的稳定性尚未证实。

**「可关注」** 可关注：大模型微调为块提议者后，单前向传播输出多 token 的匹配长度分布，以及无损模式下验证者与提议者合一对输出一致性的保证机制。

**标签**: `#eval`, `#llm-inference`, `#speculative-decoding`

---

<a id="item-agent-engineer-4"></a>
### [OpenAI Git 扩展策略发布](https://openai.com/index/scaling-git-at-openai/) ⭐️ 7.0/10

OpenAI 于 2026-11-03 发布工程博客《Scaling Git at OpenAI》，分享 Git 扩展策略。文章面向 coding agent 与 harness 开发者，据分析提供大规模代码库下 Git 操作优化的生产级参考。具体技术实现、性能基准与适用限制未在提供材料中披露，需查阅原文获取细节。

rss · Lobsters · 11月3日 02:18

**「为什么重要」** 该文章据分析为 OpenAI 工程团队一手实践，提供优化 agent 系统中 Git 相关工作的可操作生产级上下文。但具体可复用方案需阅读原文确认。

**「可关注」** 可关注：OpenAI 官方分享的 Git 扩展策略对 coding agent 的 Git 操作 harness 设计有参考意义，但具体实现需查阅原文确认。

**标签**: `#coding-agent`, `#harness`

---

<a id="item-agent-engineer-5"></a>
### [llm 0.37 发布 支持多模态嵌入](https://simonwillison.net/2026/Nov/2/llm/) ⭐️ 6.0/10

llm 0.37 是 Simon Willison 开发的 LLM CLI 工具与 Python 库版本，2026-11-02 发布，累计约两个月的新功能与修复。本次更新新增 \`gpt-6.1-sol\`、\`gpt-6.1-terra\`、\`chat-latest\` 模型，新增 \`llm openai endpoint add\`、\`list\`、\`remove\`、\`path\` 命令用于管理 OpenAI 兼容端点配置；未设置默认模型的用户，默认模型从 \`gpt-5.6-luna\` 更换为价格更低的 \`gpt-6-luna\`。嵌入功能新增多模态附件支持，可处理文本、音频、图像、视频内容，适配 Gemini Embedding 2 等模型。此外新增 Python 3.15 支持、移除 Python 3.10 支持，下线多个已停用的 OpenAI 模型，同时修复了日志配置不生效、多进程日志冲突、工具链链限制误触发、非 ASCII 文件嵌入乱码等多项问题。

rss · Simon Willison · 11月2日 23:49

**「为什么重要」** 对 coding agent 与 harness 开发者而言，新增的 OpenAI 兼容端点管理命令降低了自定义模型接入成本，多模态嵌入支持扩展了 agent 处理非文本数据的能力，默认模型降价也直接影响日常调用开销。这些变更均为已落地的功能，无需额外适配即可使用。

**「可关注」** 可关注：llm 0.37 新增的 OpenAI 兼容端点管理命令与多模态嵌入能力，可直接复用到 agent 工具链的自定义模型接入与多模态数据处理场景中。

**标签**: `#harness`, `#memory`

---

<a id="item-agent-engineer-6"></a>
### [HF 每日论文：ReGap-Bench 基准发布](https://huggingface.co/papers/2610.39419) ⭐️ 6.0/10

2026 年 11 月 3 日 Hugging Face Daily Papers 收录 arXiv 编号 2610.39419 的多模态推理论文，该研究提出成对多模态推理基准 ReGap-Bench，包含 5 项视觉推理任务，固定场景、问题与答案，仅变化视觉参考类型。实验显示任务匹配的视觉参考（如编号）可将模型准确率提升最高 25%，不匹配的参考几乎无增益甚至拉低表现。该基准主要面向多模态推理场景的模型评估与优化，当前未覆盖主流编码智能体或工具链相关能力。

rss · Hugging Face Daily Papers · 11月3日 00:00

**「为什么重要」** 该研究提供了可复用的多模态推理评估基准，也验证了视觉参考对齐对推理准确率的正向作用，对构建或评估多模态智能体的工程师有参考价值；但当前结论仅适用于多模态推理场景，未覆盖编码智能体或工具链相关能力。

**「可关注」** 可关注：为多模态推理任务设计视觉参考时，需优先匹配任务类型，不匹配的参考可能无收益甚至损害表现；ReGap-Bench 可作为该类场景的标准化评估工具。

**标签**: `#eval`

---

<a id="item-agent-engineer-7"></a>
### [DeepSeek-V4.1-Flash-1017 1bit Coder 发布](https://www.reddit.com/r/LocalLLaMA/comments/1xlys6k/release_ista_deepseekv41flash1017_gsqrco_coder_a/) ⭐️ 5.5/10

2026 年 11 月 2 日，ISTA DASLab 在 Reddit 发布 DeepSeek-V4.1-Flash-1017 的 Coder 实验版模型。该模型为总参数量 763.2B 的稀疏混合专家架构，其中 transformer 部分 551.9B 参数，经每层保留 192/384 个 routed experts 的专家剪枝、GSQ 与 RCO 量化后，transformer 权重体积为 72.1GB，按原始 transformer 参数计算有效比特率为 1.05 bits/parameter，移除的专家不计入比特存储。该模型标注为实验版本，公开的初步基准测试结果为 LiveCodeBench v6 88.57 分、SWE-bench Verified 77.00 分，分别对应基底模型 98.7%、94.8%的得分。模型可在 llama.cpp b11870 及以上版本、Strata 运行，无官方性能基准验证数据，面向本地编码代理构建者。

reddit · r/LocalLLaMA · /u/Loginhe · 11月2日 14:33

**「为什么重要」** 这是目前公开的 DeepSeek-V4.1-Flash-1017 系列中压缩率最高的本地可部署 Coder 变体，1.05 bits/parameter 的有效比特率大幅降低了本地运行该规模 MoE 模型的内存门槛；但当前仅提供两项非官方基准的初步结果，且标注为实验版本，能力覆盖范围未经验证。

**「可关注」** 可关注：该模型通过 RCO 对每层专家保留数设置硬约束，避免了 GGUF 格式下因层间专家数差异产生的填充开销，同时共享未剪枝版本的 Engram 文件与视觉投影器文件，减少了重复下载体积。

**标签**: `#coding-agent`

---

## AI 日报
{: #sec-ai-daily .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-daily" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-daily-1"></a>
### [OpenAI 安全漏洞赏金计划升级](https://openai.com/index/rewarding-defenders-with-bigger-bug-bounties) ⭐️ 8.8/10

OpenAI 官方博客 2026 年 11 月 2 日宣布更新安全漏洞赏金计划，提高基础赏金金额。本次更新同时为独立安全研究人员新增报告质量、忠诚度、优先活动三类奖金。

rss · OpenAI Blog · 11月2日 18:00

**「为什么重要」** 该调整是头部 AI 实验室首次明确细化漏洞赏金的激励维度，为 AI 安全研究者的贡献回报机制提供了可参考的范式。

**「可关注」** 可关注：OpenAI 新增的三类漏洞赏金奖金覆盖报告质量、研究者忠诚度与优先活动场景，后续其他 AI 实验室或跟进类似激励设计。

**标签**: `#lab`, `#policy`, `#industry`

---

<a id="item-ai-daily-2"></a>
### [OpenAI 发布 LifeVal 日常基准](https://openai.com/index/lifeval) ⭐️ 8.8/10

OpenAI 于 2026 年 11 月 2 日发布 LifeVal 评估基准。该基准用于衡量 AI 系统辅助用户完成日常事务的能力，覆盖找托儿服务、财务管理、处理政府文书等典型场景。

rss · OpenAI Blog · 11月2日 09:00

**「为什么重要」** 当前多数 AI 评估基准聚焦专业或学术场景，LifeVal 填补了日常实用场景评估的空白，可更直接反映 AI 对普通用户的实际帮助价值。

**「可关注」** 可关注：LifeVal 的评估维度可参考作为 coding agent 日常辅助能力的设计参考。

**标签**: `#eval`, `#lab`

---

<a id="item-ai-daily-3"></a>
### [OpenAI 发布 Pando Git 兼容后端](https://openai.com/index/scaling-git-at-openai) ⭐️ 7.8/10

OpenAI 官方博客发布技术文章，介绍其开发的 Git 兼容后端 Pando。该后端专为支撑 Codex 带来的大规模开发场景设计。当前公开材料未披露 Pando 的具体性能指标、落地范围等细节。

rss · OpenAI Blog · 11月2日 15:30

**「为什么重要」** 这是 OpenAI 面向 AI 辅助编程场景推出的底层基础设施，直接关联 Codex 的规模化落地能力。其设计思路可能为同类 Git 后端优化提供参考。

**「可关注」** 可关注 Pando 作为 Git 兼容后端的架构设计，以及其与 Codex 的适配细节。

**标签**: `#product`, `#lab`

---

<a id="item-ai-daily-4"></a>
### [OpenAI 推出 Grid Protectors Program](https://openai.com/index/grid-protectors-program) ⭐️ 7.8/10

OpenAI 于 2026 年 11 月 2 日宣布推出 Grid Protectors Program。该计划将与电力公司合作，旨在支持未来 AI 计算园区的电网可靠性，同时保护消费者用电成本。目前公开信息未披露具体合作规模、落地时间表及成本测算细节。

rss · OpenAI Blog · 11月2日 15:00

**「可关注」** 可关注：该计划后续披露的电力合作细则与 AI 计算园区的电网接入标准。

**标签**: `#policy`, `#industry`, `#lab`

---

<a id="item-ai-daily-5"></a>
### [OpenAI 筹备内部安全冲刺](https://openai.com/index/preparing-our-next-security-sprint-to-harden-openai) ⭐️ 6.8/10

OpenAI 宣布正与安全公司 Cathedral Systems 合作筹备下一次内部安全冲刺，计划用 AI 测试并强化自身防御能力。目前未披露该冲刺的具体时间、覆盖范围，也未说明与过往安全工作相比的差异化细节。

rss · OpenAI Blog · 11月2日 18:00

**「为什么重要」** 头部 AI 实验室公开的安全强化动作，其用 AI 测试防御能力的实践方向对行业有参考意义。

**「可关注」** 可关注：AI 实验室用 AI 测试自身防御能力的落地实践进展。

**标签**: `#lab`, `#security`, `#industry`

---