---
layout: default
title: "Horizon Summary: 2026-11-21 (ZH)"
date: 2026-11-21
lang: zh
---

> 从 183 条内容中筛选出 17 条重要资讯。

<nav id="ah-toc" class="ah-toc" aria-label="目录"><span class="ah-toc-title">目录</span><ul><li><a href="#sec-harness-arch"><span class="ah-toc-name">Harness 架构</span><span class="ah-toc-count">4条</span></a></li><li><a href="#sec-agent-engineer"><span class="ah-toc-name">Agent 工程师日报</span><span class="ah-toc-count">6条</span></a></li><li><a href="#sec-ai-daily"><span class="ah-toc-name">AI 日报</span><span class="ah-toc-count">5条</span></a></li><li><a href="#sec-ai-deals"><span class="ah-toc-name">AI 羊毛</span><span class="ah-toc-count">2条</span></a></li></ul></nav>

---

**[Harness 架构](#sec-harness-arch)**
1. [Codex rust-v0.171.0 发布](#item-harness-arch-1) ⭐️ 7.8/10
2. [openai-agents-python v1.0.0-alpha.1 发布](#item-harness-arch-2) ⭐️ 7.8/10
3. [cloudflare/agents v0.34.0 发布](#item-harness-arch-3) ⭐️ 7.8/10
4. [OpenAI Agents API 时间感知与异步输入发布](#item-harness-arch-4) ⭐️ 6.8/10

**[Agent 工程师日报](#sec-agent-engineer)**
1. [Hugging Face 发布 harness 适配方案](#item-agent-engineer-1) ⭐️ 8.8/10
2. [Inkling 2 Mini 开源发布](#item-agent-engineer-2) ⭐️ 7.0/10
3. [TuringSpace 交互式 CAPTCHA 基准发布](#item-agent-engineer-3) ⭐️ 6.0/10
4. [AltRA-Test 提出无共享标注员检验](#item-agent-engineer-4) ⭐️ 6.0/10
5. [代码质量降多智能体审查成本 22-35%](#item-agent-engineer-5) ⭐️ 6.0/10
6. [WeVisForensics 自演化视频检测](#item-agent-engineer-6) ⭐️ 5.5/10

**[AI 日报](#sec-ai-daily)**
1. [Anthropic 完成 IPO 登陆纳斯达克](#item-ai-daily-1) ⭐️ 9.8/10
2. [OpenAI 推出对抗性蒸馏分层防护方案](#item-ai-daily-2) ⭐️ 8.8/10
3. [OpenAI 发布 MedChemBench 基准](#item-ai-daily-3) ⭐️ 7.8/10
4. [Agent Anomaly Detection 开放跨云监控私有预览](#item-ai-daily-4) ⭐️ 7.8/10
5. [上海 AI Lab 发布 Sage S2.1 Flash](#item-ai-daily-5) ⭐️ 5.0/10

**[AI 羊毛](#sec-ai-deals)**
1. [Epic 本周限免两款游戏](#item-ai-deals-1) ⭐️ 8.0/10
2. [greatai 开源非营利可领免费审查](#item-ai-deals-2) ⭐️ 5.0/10

---

## Harness 架构
{: #sec-harness-arch .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-harness-arch" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-harness-arch-1"></a>
### [Codex rust-v0.171.0 发布](https://github.com/openai/codex/releases/tag/rust-v0.171.0) ⭐️ 7.8/10

openai/codex 正式发布 rust-v0.171.0。默认启用带子代理转录的 TUI 工作区，新增 \`codex exec --remote\` 非交互式远程会话执行，以及通过 \`/statusline\` 自定义 MCP 状态行。修复会话切换时草稿和线程状态丢失、权限配置跨工作目录保留等问题。模型目录新增 GPT-6.2 Sol 和 Astra，Sol 设为默认。

github · github-actions\[bot\] · 11月20日 00:44

**「设计要点」** TUI 工作区默认启用，主对话旁并排显示可搜索文档预览、图片预览和子代理转录。新增 \`codex exec --remote\` 支持在现有应用服务器上启动或恢复非交互式会话，自定义 MCP 状态行需启用 \`tui\_extensions\_statusline\`，会话状态保留修复覆盖草稿、排队跟进、中断输入和权限配置，提升多线程切换可靠性。

**「改了什么」** 默认启用带子代理转录的 TUI 工作区，新增 \`codex exec --remote\` 远程非交互式会话执行命令。新增 \`/statusline\` 自定义 MCP 状态行，修复会话切换时草稿、排队跟进和中断输入丢失，以及权限配置跨工作目录丢失问题。

**标签**: `#runtime`, `#subagents`, `#mcp`, `#memory`, `#tools`

---

<a id="item-harness-arch-2"></a>
### [openai-agents-python v1.0.0-alpha.1 发布](https://github.com/openai/openai-agents-python/releases/tag/v1.0.0-alpha.1) ⭐️ 7.8/10

这是 OpenAI 官方发布的 Python Agents SDK v1.0.0 首个 alpha 预览版，核心变化是新增可选的 Codex 模型提供方，预编译 wheel 包（版本 1.0.0a1）仅通过 GitHub Releases 分发，支持 CPython 3.10 至 3.14 环境。该版本通过 PyO3 嵌入未修改的 Codex Core rust-v0.166.0 运行时，直接调用 Core 能力，移除了此前需要的独立 codex app-server 和 JSON-RPC 通信层。

github · markstuart-oai · 11月20日 20:51

**「设计要点」** 运行时将未修改的 Codex Core rust-v0.166.0 通过 PyO3 直接嵌入 Python wheel，无需启动独立 app-server 和 JSON-RPC 中间层；CodexProvider 可复用同一个 ThreadManager，每次调用分配独立线程，支持通过 SDK session 保留对话历史，使用完毕后需调用 await provider.aclose\(\)释放资源。

**「改了什么」** 相对此前 harness 预览版 v0.24.0-alpha.8，新增 CodexProvider 可选模型提供方，支持通过 RunConfig 传入 Runner 选择 Codex 模型；执行入口从 Agent.run\(\)、Session.submit\(\)迁移到 Runner.run\(\)/Runner.run\_streamed\(\)，agents.classic 的导入路径统一为从 agents 包导入 Agent、Runner、RunConfig；同时修复了 Codex 会话压缩依赖本地历史、沙箱清单保存内联二进制文件的问题。

**标签**: `#runtime`, `#model-provider`

---

<a id="item-harness-arch-3"></a>
### [cloudflare/agents v0.34.0 发布](https://github.com/cloudflare/agents/releases/tag/agents%400.34.0) ⭐️ 7.8/10

cloudflare/agents 发布 v0.34.0，核心升级至 Pi 1.6 运行时。Pi harness 新增非阻塞等待工具，支持工具挂起后由信号或截止时间唤醒，agent 可休眠；\`submit\(\)\` 与 \`continue\(\)\` 接受 \`notify\` 实现子代理等待协调。MCP 客户端引入 \`MCPAuthorizationRequiredError\` 重新授权信号，失败请求改为通用 500 或 WebSocket 1011 关闭，并提供 \`onFetchError\(\)\` 钩子。升级需将 Pi 相关包更新至 \`~1.6.0\`，且一旦运行在 Pi 1.6 上无法回滚至 1.5。

github · github-actions\[bot\] · 11月20日 15:56

**「设计要点」** Pi harness 采用信号驱动的挂起-唤醒机制，工具通过 \`harness.signal\(\)\` 交付信号而非直接操作 pi 实例，确保调度顺序正确。会话层支持通过 \`init\` 参数从现有历史初始化，根会话需通过 \`harness.root\(\)\` 显式创建以避免遗漏默认配置；MCP 客户端将授权状态与服务器连接状态解耦，失败服务器保持失败态直至显式重连。

**「改了什么」** Pi 1.6 支持非阻塞等待与子 agent 协调，\`submit\(\)\` 新增 \`onAbort: &quot;keep&quot;\` 保留中断时的排队输入，\`PiHarness.dispose\(\)\` 释放 per-session 状态。MCP 客户端增加 \`MCPAuthorizationRequiredError\` 与 \`reconnectMcpServer\(id\)\` 接口，失败请求错误详情被脱敏；Anthropic 消息线程过期后自动恢复，聊天操作跨标签页竞争条件得到修复。

**标签**: `#runtime`, `#tools`, `#mcp`, `#subagents`

---

<a id="item-harness-arch-4"></a>
### [OpenAI Agents API 时间感知与异步输入发布](https://developers.openai.com/blog/time-awareness-and-async-input-for-personal-agents) ⭐️ 6.8/10

这是 OpenAI 官方开发者博客发布的个人助理类 agent 构建指南，核心介绍 Agents API 的两项新 runtime 能力：实验性时间感知（time\_awareness）与异步函数工具。开启 time\_awareness 后，模型会定期收到当前时间提醒，可依据用户设定的截止时间自主调整工作优先级，比如临近会议时优先整理调研结果而非开启新研究方向。异步函数工具允许 agent 在等待用户输入时继续执行其他任务，即使未收到用户回复也能在截止时间前交付可用结果。示例使用模型为 gpt-6.2-astra，配置时需使用具备 Agents API 访问权限的项目的 API key，开启 experimental.time\_awareness=true，异步工具需设置 async: true，必填参数为 question，可选 choices 为建议回复选项。

rss · OpenAI Developer · 11月20日 00:00

**「设计要点」** Agents API 的时间感知能力由服务端定期向模型注入当前时间戳实现，无需 agent 侧自行维护计时逻辑。异步工具的执行模型为：agent 发起异步工具调用后不阻塞，应用层负责收集用户回复并回传结果，模型可依据剩余时间自主决策是继续深挖调研还是优先产出结果。

**「改了什么」** 相对此前版本，Agents API 新增实验性 time\_awareness 开关，以及函数工具的 async 执行模式，打破同步阻塞限制，允许 agent 在等待用户输入时保持工作流推进。

**标签**: `#runtime`, `#planning`

---

## Agent 工程师日报
{: #sec-agent-engineer .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-agent-engineer" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-agent-engineer-1"></a>
### [Hugging Face 发布 harness 适配方案](https://huggingface.co/blog/harness-adapters-at-scale) ⭐️ 8.8/10

Hugging Face 2026 年 11 月 20 日发布官方博客，提出通过强化学习为不同 agent harness 训练定制 LoRA 适配器的方案。该方案针对 Qwen3.8-27B 在 Pi 1.5.2、OpenCode 2.2.7、Hermes Agent v0.22.6 三个 harness 上的测试显示，Terminal-Bench 2.1 pass@1 从基线的 39% 提升至 55%，单任务平均 token 消耗从 2.9K 降至 1.5K；同时可将三个 harness 的适配器合并为单一 super adapter，所有适配器、训练任务等产物均已公开在 Hugging Face Hub 对应集合中。

rss · Hugging Face Blog · 11月20日 00:00

**「为什么重要」** 该方案首次公开了在真实 agent harness 内部完成 agentic RL 训练的全流程可复用 recipe，证明针对特定 harness 与任务分布优化模型可同时提升准确率与 token 效率；目前该方案在其他模型、其他类型 harness 上的泛化效果尚未公开验证。

**「可关注」** 可关注：官方方案直接在目标 harness 内开展 agentic RL 训练，无需重写 agent 循环，同时公开了配套的任务生成、验证与训练工具链。

**标签**: `#harness`, `#eval`, `#coding-agent`, `#orchestration`

---

<a id="item-agent-engineer-2"></a>
### [Inkling 2 Mini 开源发布](https://thinkingmachines.ai/news/inkling-2-mini/) ⭐️ 7.0/10

2026 年 11 月 20 日，Thinking Machines Lab 开源发布 Inkling 2 Mini，这是一款采用循环 Transformer 架构的多模态混合专家模型，物理总参数量约 26B，每 token 激活参数量仅 3B。模型通过复用 12 层中间层权重实现 3 次循环，等效 48 层逻辑解码器，支持 1M token 上下文、图文输入，以端到端 NVFP4 训练、NVFP4 与 MXFP8 混合精度格式发布，同时提供 transformers、llama.cpp（GGUF）、MLX、SGLang 推理支持，附带 DSpark drafter 以提升推理速度，另有可自定义循环次数的研究版 checkpoint。官方称其推理性能至少 comparable 到 Qwen3.8-27B，在 Artificial Analysis Intelligence Index v5 的 48 项基准中 32 项领先，覆盖编码、知识工作、视觉理解等场景，但社区提示其事实性得分与同参数量模型一致，循环次数增加不提升知识存储能力，真实场景表现仍需验证。该模型为基础模型发布，非直接 harness/工具链更新，主要面向需要本地推理能力的 coding agent、本地助理类应用的工程师。

hackernews · jasondavies · 11月20日 20:12 · [社区讨论](https://news.ycombinator.com/item?id=50581260)

**「为什么重要」** 这是目前少数开源落地的循环 Transformer 架构模型，为本地轻量 agent 提供了新的基础模型选项；但其推理性能对标更大模型的声明尚未在真实 agent 工作流中得到充分验证，循环架构对安全性与可解释性的影响也暂无公开结论。

**「可关注」** 可关注：Inkling 2 Mini 通过循环复用中间层权重实现更高逻辑层深度，其 GGUF 版本已支持 Ollama/llama.cpp 本地部署，可测试其在轻量本地 coding agent 场景中的推理速度与效果表现。

**「评论」** 社区普遍认可该模型开源循环架构的创新性，认为若基准表现稳定将是优秀的本地模型；同时有用户指出其事实性得分与同参数量模型一致，循环次数增加仅提升推理不提升知识存储，还有用户正准备在 AMD 7900XTX 显卡上测试其解码速度表现。

**标签**: `#eval`, `#orchestration`

---

<a id="item-agent-engineer-3"></a>
### [TuringSpace 交互式 CAPTCHA 基准发布](https://huggingface.co/papers/2611.25387) ⭐️ 6.0/10

2026 年 11 月 20 日 Hugging Face 每日论文发布 TuringSpace 基准，这是一个可扩展的交互式 CAPTCHA 基准，用于评估多模态大模型（MLLMs）的空间智能与交互动作能力。该基准包含 125 个任务，覆盖 5 类空间能力，每个任务均为可生成新实例的程序，内置检查器与预言机，同时可作为可扩展的训练 gym。它面向从事多模态大模型空间推理、agent 评估系统开发的团队，当前公开内容未包含基准性能测试结果，应用场景目前聚焦于空间交互推理。

rss · Hugging Face Daily Papers · 11月20日 00:00

**「为什么重要」** 它填补了现有 CAPTCHA 基准基本已被解决且少涉及空间能力、现有空间基准极少要求交互动作的空白，为相关评估提供了可复用的框架。但当前未公开基准性能测试结果，其对模型能力提升的实际验证效果尚未明确。

**「可关注」** 可关注：TuringSpace 的任务均为带检查器与预言机的可编程实例，支持自动生成新样本与评估，适合作为空间交互推理能力的可扩展训练与评测工具。

**标签**: `#eval`

---

<a id="item-agent-engineer-4"></a>
### [AltRA-Test 提出无共享标注员检验](https://huggingface.co/papers/2611.26073) ⭐️ 6.0/10

2026-11-20，Hugging Face Daily Papers 介绍 AltRA-Test 论文。该论文提出一种基于 bootstrap 的统计检验方法，用于在大规模标注场景中验证用 LLM 法官替代人类标注员的统计合理性。相比此前 Alt-Test 要求所有标注项由相同标注员标注的密集场景限制，AltRA-Test 支持不同标注项由不同标注员子集标注的非重叠场景。该方法通过重采样标注项、为每项抽取 k 条人类标注并替换其中一条为 LLM 标注，生成配对数据以进行统计推断；目前材料未提供该检验的具体功效、计算开销或实际应用案例。

rss · Hugging Face Daily Papers · 11月20日 00:00

**「为什么重要」** 该工作填补了 LLM 法官评估方法论中的空白，为构建基于 LLM 法官的 agent 评估流水线提供了统计验证工具。不过目前仅见论文提出，尚未有大样本实证或工业界部署报告证实其实际表现。

**「可关注」** 可关注：AltRA-Test 的非重叠标注员假设更贴合大规模众包标注的常见实践。

**标签**: `#eval`

---

<a id="item-agent-engineer-5"></a>
### [代码质量降多智能体审查成本 22-35%](https://martinfowler.com/fragments/2026-11-20.html) ⭐️ 6.0/10

2026 年 11 月 20 日，Martin Fowler 在其 Fragments 专栏引用了 CodeScene 的实证研究，验证代码质量对多智能体代码审查流水线 token 成本的影响。研究覆盖 246 个开源仓库的 465 个 PR，采用 3 个 LLM 搭配 5 个智能体的审查修复流水线，对比 CodeHealth 评分 2.8（低质量）与 9.7（高质量）的 PR，token 成本降幅为 22% 至 35%，其中 Complex Method、Complex Conditional 被识别为推高成本的核心代码坏味道。该 Fragments 为二次摘要，完整方法论、原始数据与可复现细节仅存于原博客，未在本次引用中公开。

rss · Martin Fowler · 11月20日 18:38

**「为什么重要」** 该研究为 coding agent 与代码审查流水线的成本优化提供了可量化的实证锚点，证明代码质量是控制智能体工作流 token 消耗的有效变量；但当前测试仅基于公开开源 PR，内部业务场景的成本降幅尚未得到验证。

**「可关注」** 可关注：多智能体代码审查场景下，优先治理 Complex Method、Complex Conditional 两类代码坏味道，可降低 token 消耗。

**标签**: `#coding-agent`

---

<a id="item-agent-engineer-6"></a>
### [WeVisForensics 自演化视频检测](https://huggingface.co/papers/2611.21373) ⭐️ 5.5/10

2026 年 11 月 20 日 Hugging Face 每日论文收录 WeVisForensics 相关研究，该框架是面向 AI 生成视频检测的自演化多智能体系统，由主调查智能体协调覆盖视觉、音频线索的自演化子智能体库，可自主决定检查的伪影类型、时间窗口与终止时机。当前公开摘要在中途截断，未披露性能指标、可操作技术细节，且领域适用性较窄。

rss · Hugging Face Daily Papers · 11月20日 00:00

**「为什么重要」** 该研究提出了自适应主智能体协调专业子智能体的编排模式，以及子智能体库自演化机制，对多智能体任务编排、AI 生成内容检测方向的工程师有参考价值；但当前公开内容截断，实际性能与泛化能力尚未证实。

**「可关注」** 可关注：自适应主智能体协调子智能体库的编排设计，以及&quot;策略优化不直接提升固定专家能力&quot;这一多智能体系统设计张力。

**标签**: `#orchestration`

---

## AI 日报
{: #sec-ai-daily .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-daily" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-daily-1"></a>
### [Anthropic 完成 IPO 登陆纳斯达克](https://www.anthropic.com/news/ipo-close) ⭐️ 9.8/10

Anthropic 官方宣布首次公开募股完成，共发行 11.27 亿股 A 类普通股，发行价每股 83 美元，含承销商全额行权的 1.47 亿股额外购股权，总募资约 935 亿美元，其中 Anthropic 获约 916 亿美元。其 A 类普通股于 2026 年 11 月 19 日在纳斯达克全球精选市场挂牌交易，股票代码为 ANT，本次发行由高盛、摩根士丹利担任联席账簿管理人。同步完成的 N 类普通股私募未依据《1933 年证券法》注册，向 AMD、博通、谷歌、美光、微软、英伟达、台积电等 7 家厂商发行 3.13 亿股，募资约 260 亿美元，整体募资约 1195 亿美元。

rss · Anthropic News · 11月20日 00:00

**「为什么重要」** 这是 AI 主流实验室迄今规模最大的资本动作之一，募资规模与参与方覆盖核心算力与云服务厂商，将直接影响其后续研发与算力投入节奏。

**「可关注」** 可关注：Anthropic 上市后公开披露的研发投入与算力采购计划，以及 N 类股股东的技术合作动向。

**标签**: `#lab`, `#industry`

---

<a id="item-ai-daily-2"></a>
### [OpenAI 推出对抗性蒸馏分层防护方案](https://openai.com/index/combatting-adversarial-distillation) ⭐️ 8.8/10

2026 年 11 月 20 日 OpenAI 发布官方公告，推出对抗对抗性蒸馏的分层防护方案。该方案覆盖模型训练、防护机制、攻击检测、执法处置四个核心环节，旨在防止模型能力被未经授权的提取。

rss · OpenAI Blog · 11月20日 10:00

**「为什么重要」** 对抗性蒸馏是当前大模型能力泄露的主流攻击路径之一，该方案首次明确覆盖从训练到执法的全链路防护逻辑，为行业模型安全防护提供了可参考的框架。

**「可关注」** 可关注：OpenAI 将模型训练、防护、检测、执法纳入同一防护体系，覆盖对抗性蒸馏全链路。

**标签**: `#lab`, `#model`, `#policy`

---

<a id="item-ai-daily-3"></a>
### [OpenAI 发布 MedChemBench 基准](https://openai.com/index/introducing-medchembench) ⭐️ 7.8/10

2026 年 11 月 20 日，OpenAI 官方发布新基准 MedChemBench，用于评估 AI 模型在早期药物发现场景下的核心能力。该基准覆盖分子结构解读、实验证据推理、化合物筛选三项任务。目前未公开该基准与现有同类工具的差异及具体测试规则。

rss · OpenAI Blog · 11月20日 00:00

**「为什么重要」** 早期药物发现是 AI 制药的核心落地场景，该基准为相关模型的能力评估提供了统一的测试框架，便于行业对比不同模型的实际表现。

**「可关注」** 可关注：MedChemBench 针对分子结构解读、实验证据推理、化合物筛选三项核心能力的评估维度设计。

**标签**: `#eval`, `#lab`, `#industry`

---

<a id="item-ai-daily-4"></a>
### [Agent Anomaly Detection 开放跨云监控私有预览](https://developers.googleblog.com/agent-anomaly-detection-safeguarding-agents-across-other-clouds/) ⭐️ 7.8/10

Google 宣布 Agent Anomaly Detection 进入私有预览，新增对运行在 AWS、Microsoft Foundry 及本地基础设施的非 Google Cloud agent 的监控能力。该功能基于 agent 的追踪与日志分析，无需访问 agent 运行时，仅需将 telemetry 上报至用户的 Google Cloud 项目即可生效。当前仅支持使用 ADK for Python 2.12.0 及以上版本构建的 agent，需配置对应环境变量与 GCP 凭据完成上报，agent 被发现后 30 分钟内即可启用分析，测试中已成功识别跨云场景下的目录爬取、异常超额退款等风险行为。

rss · Google Developers AI · 11月20日 00:00

**「为什么重要」** 此前 Agent Anomaly Detection 仅覆盖 Google Cloud 环境内的 agent，此次扩展补齐了主流非 GCP 部署场景的行为风险监控空白。其无需 runtime 访问、基于现有 telemetry 分析的方案，降低了跨云 agent 监控的接入成本。

**「可关注」** 可关注：ADK for Python 2.12.0 及以上版本已支持跨云 telemetry 上报，仅需配置对应环境变量与 GCP 凭据即可接入 Agent Anomaly Detection，分析过程独立运行不占用 agent 自身资源。

**标签**: `#product`, `#industry`, `#Google`, `#monitoring`

---

<a id="item-ai-daily-5"></a>
### [上海 AI Lab 发布 Sage S2.1 Flash](https://mp.weixin.qq.com/s?__biz=MzA3MzI4MjgzMw==&amp;mid=2651075493&amp;idx=3&amp;sn=63643451e794a6d8ac3dbb423d7f460d) ⭐️ 5.0/10

上海 AI Lab 联合复旦大学、中科院软件所等多家机构发布 Sage S2.1 Flash 技术报告，开源总参数量 320B 的混合专家模型，在四项智能体基准上达到 SOTA，探索科学多模态感知融入通用智能体的方向。报告披露了该模型的完整训练流程与技术细节，相关论文、代码与模型已同步开源，其支持长上下文处理、工具调用、专业软件操作，具备读懂分子和光谱等科学数据的能力，可完成从 12487 张 CT 图像中筛选切片并重建 3D 骨骼模型的任务。上线首周用户反馈其工具调用流畅、任务执行完整，生成画面也在鹈鹕测试中获得积极评价。目前公开信息仅包含报道披露的内容，无更多可核对的原始技术细节。

rss · 机器之心 · 11月20日 03:58

**「为什么重要」** 该模型首次将科学多模态感知能力融入通用智能体框架，同时覆盖工具调用、专业软件操作等贴近实际开发与科研的场景，为相关领域的智能体应用提供了新的开源基座。

**「可关注」** 可关注：其统一科学多模态架构通过动态 MoE 路由与混合注意力机制，同时支持长上下文处理与多类型数据输入，为科学场景智能体提供了统一的推理基座。

**标签**: `#model`, `#lab`, `#open-source`, `#eval`

---

## AI 羊毛
{: #sec-ai-deals .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-deals" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-deals-1"></a>
### [Epic 本周限免两款游戏](https://www.appinn.com/eggs-261120/) ⭐️ 8.0/10

你看到的内容可能由第三方 AI 基于小众软件文章提炼总结而成，可能与原文真实意图存在偏差。不代表小众软件观点和立场。请点击链接阅读原文细致比对和校验。
Epic 平台本周（11.20~11.26）限时免费送出两款游戏：电脑端可领《深渊之印 / Mark of the Deep》，手机端可领《Lonesome Village》，两款游戏均可通过对应 Epic 商店页面免费领取，其中《深渊之印》支持中文。

rss · 小众软件 · 11月20日 07:21

**「为什么重要」** 两款游戏在 Steam 均获得多半好评，且本周限免期间无需付费即可领取，适合对应题材与平台偏好的玩家获取。

**「可关注」** 可关注：两款游戏分属不同平台与品类，《深渊之印》适配 PC 端，主打类魂战斗与银河城探索；《Lonesome Village》适配移动端，无战斗侧重解谜与生活模拟，可按需选择对应平台领取。

**标签**: `#limited-free`, `#promo`, `#game`

---

<a id="item-ai-deals-2"></a>
### [greatai 开源非营利可领免费审查](https://www.producthunt.com/products/greatai-review) ⭐️ 5.0/10

greatai Review 已在 Product Hunt 上线，面向开源项目与非营利组织提供免费的 AI 加人工代码审查服务，目前未公开具体领取规则、服务有效期、额度限制等关键信息，也无明确截止时间。

rss · Product Hunt · 11月20日 04:56

**「为什么重要」** 该服务当前仅对开源项目与非营利组织开放，若相关项目有代码审查需求，可后续关注官方规则更新，暂无其他已知限制。

**「可关注」** 可关注：仅开源项目与非营利组织符合申请资格，具体领取方式、服务有效期等规则尚未公开，需等待官方补充说明。

**标签**: `#free-tier`, `#promo`, `#limited-free`

---