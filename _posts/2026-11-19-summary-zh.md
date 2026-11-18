---
layout: default
title: "Horizon Summary: 2026-11-19 (ZH)"
date: 2026-11-19
lang: zh
---

> 从 213 条内容中筛选出 17 条重要资讯。

<nav id="ah-toc" class="ah-toc" aria-label="目录"><span class="ah-toc-title">目录</span><ul><li><a href="#sec-harness-arch"><span class="ah-toc-name">Harness 架构</span><span class="ah-toc-count">3条</span></a></li><li><a href="#sec-agent-engineer"><span class="ah-toc-name">Agent 工程师日报</span><span class="ah-toc-count">9条</span></a></li><li><a href="#sec-ai-daily"><span class="ah-toc-name">AI 日报</span><span class="ah-toc-count">4条</span></a></li><li><a href="#sec-ai-deals"><span class="ah-toc-name">AI 羊毛</span><span class="ah-toc-count">1条</span></a></li></ul></nav>

---

**[Harness 架构](#sec-harness-arch)**
1. [mastra-ai/mastra @mastra/core@1.84.0 发布](#item-harness-arch-1) ⭐️ 8.8/10
2. [Codex rust-v0.170.0 发布](#item-harness-arch-2) ⭐️ 7.8/10
3. [openai-agents-python v0.25.0 发布](#item-harness-arch-3) ⭐️ 7.8/10

**[Agent 工程师日报](#sec-agent-engineer)**
1. [Gemini 4 Neon 发布](#item-agent-engineer-1) ⭐️ 8.8/10
2. [DaisyRose-27B 开源 强化学习 Agent 后训练模型](#item-agent-engineer-2) ⭐️ 8.3/10
3. [180B MoE 模型 32GB 内存运行方案](#item-agent-engineer-3) ⭐️ 7.8/10
4. [Genie 4 正式发布](#item-agent-engineer-4) ⭐️ 7.8/10
5. [OpenAI 芯片设计模型案例发布](#item-agent-engineer-5) ⭐️ 7.0/10
6. [curl AI 重写未跟上人类修复](#item-agent-engineer-6) ⭐️ 7.0/10
7. [GPT-6.2 Astra/Sol 发布](#item-agent-engineer-7) ⭐️ 7.0/10
8. [Xing 4 系列模型架构报告发布](#item-agent-engineer-8) ⭐️ 7.0/10
9. [Self-Improvement Memory 论文发布](#item-agent-engineer-9) ⭐️ 7.0/10

**[AI 日报](#sec-ai-daily)**
1. [Codex 沙箱功能发布](#item-ai-daily-1) ⭐️ 7.8/10
2. [OpenAI 披露前沿 AI 风险管理实践](#item-ai-daily-2) ⭐️ 7.8/10
3. [OpenAI 模型实现芯片设计优化](#item-ai-daily-3) ⭐️ 7.8/10
4. [OpenAI 与费加罗报集团达成合作](#item-ai-daily-4) ⭐️ 6.8/10

**[AI 羊毛](#sec-ai-deals)**
1. [Gemini Tasks 个人助理功能免费开放](#item-ai-deals-1) ⭐️ 7.0/10

---

## Harness 架构
{: #sec-harness-arch .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-harness-arch" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-harness-arch-1"></a>
### [mastra-ai/mastra @mastra/core@1.84.0 发布](https://github.com/mastra-ai/mastra/releases/tag/%40mastra/core%401.84.0) ⭐️ 8.8/10

mastra-ai/mastra 发布 @mastra/core@1.84.0。本次更新引入实验性 Storage Version 2，将 agent 与 evented workflow 的持久化格式改为 header + per-step rows 的增量写入模式，发布消息体积从 98 MB 降至 11 MB，写入量从 75 MB 降至 3.1 MB。同时新增自动工作流崩溃恢复循环，通过 leader election lease 实现多实例协调，并支持 Redis/Valkey Streams 与 Google Cloud Pub/Sub 的 broker-aware 消息重投递，避免重复执行。

github · PaulieScanlon · 11月18日 10:36

**「设计要点」** 运行时采用 durable agent 与 evented workflow 双模式，Storage Version 2 以 delta-based 行格式替换全量快照，仅传输步骤间状态变更。分布式恢复依赖存储适配器上的 leader election lease，仅 leader 实例执行恢复扫描；broker 通过 pubsub.redeliversUnacked 标记决定是否由自身重投递未确认消息。

**「改了什么」** Storage Version 2 覆盖 agents 与 evented workflows，result.steps\(\) 与 getState\(\) 改为异步；工作流恢复循环由 startWorkers\(\) 启动，leader 实例扫描并重启默认引擎崩溃运行，broker 通过 redeliversUnacked 标记避免 evented 运行重复执行。此外新增 @mastra/platform 托管客户端、Knowledge movePage/reembed 操作及 MCP Apps 可观测性嵌入。

**标签**: `#runtime`, `#memory`, `#subagents`

---

<a id="item-harness-arch-2"></a>
### [Codex rust-v0.170.0 发布](https://github.com/openai/codex/releases/tag/rust-v0.170.0) ⭐️ 7.8/10

OpenAI Codex 发布 rust-v0.170.0，更新 MCP、sandbox、runtime 与 TUI 等核心 agent harness 组件。新增 WebRTC 实时语音通话协商、OpenTelemetry HTTP 导出器自动刷新认证头，以及实验性跨环境同名 MCP 服务器支持。修复 MCP OAuth 竞态、Cloud 对话自动重连与恢复轮次保持、Windows 文件替换与 sandbox 权限保留，以及 oversized WebSocket 请求立即回退 HTTP。

github · github-actions\[bot\] · 11月18日 03:40

**「设计要点」** 运行时层增加 Cloud 对话空闲重连与恢复轮次保持机制，降低流式传输中断后的状态丢失。Sandbox 权限模型引入 permission profiles 与 filesystem rules，统一 Windows 与 TUI 的权限转换逻辑。MCP 服务器按环境隔离命名，OAuth 凭证写入增加取消安全保护。

**「改了什么」** 相对 rust-v0.169.0，TUI 新增 WebRTC 实时语音通话协商。MCP 修复 OAuth 凭证竞态，支持跨环境独立命名同名称服务器。Sandbox 修复 Windows 文件权限保留、子线程权限继承及运行时注册恢复。Cloud 对话在流中断后自动重连并保留活跃恢复轮次。

**标签**: `#mcp`, `#sandbox`, `#runtime`, `#permissions`, `#tools`

---

<a id="item-harness-arch-3"></a>
### [openai-agents-python v0.25.0 发布](https://github.com/openai/openai-agents-python/releases/tag/v0.25.0) ⭐️ 7.8/10

openai-agents-python v0.25.0 移除 beta Runloop sandbox provider，并修改 Pydantic run context checkpoint 行为。RunState schema 升至 1.22，支持嵌套 agent-tool 审批恢复。OpenAIResponsesCompactionSession 默认模型改为 gpt-6-luna，MCP v2 Streamable HTTP 支持并发请求。

github · openai-sdks\[bot\] · 11月18日 00:22

**「设计要点」** 跨 worker 共享 checkpoint 的应用需先升级 reader。Pydantic checkpoint 保留默认值与原地编辑，process-local 资源需自定义序列化器，第三方 session adapter 工具已暴露。

**「改了什么」** 移除 Runloop sandbox provider，用户需迁移至 Modal 或其他支持 provider 或停留在 0.24.0。Pydantic run context checkpoint 保留默认值与原地编辑，RunState schema 1.22 支持嵌套 agent-tool 审批恢复。OpenAIResponsesCompactionSession 默认模型从 gpt-4.1 改为 gpt-6-luna，Agent model 设置更贴合所选模型。MCP v2 Streamable HTTP 支持并发请求，失败或不完整的 Responses 调用保留 provider-reported token usage。Runner handoffs 新增 failure\_error\_function 恢复选项，演示 REPL 可单独批准或拒绝工具调用。

**标签**: `#sandbox`, `#memory`, `#runtime`

---

## Agent 工程师日报
{: #sec-agent-engineer .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-agent-engineer" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-agent-engineer-1"></a>
### [Gemini 4 Neon 发布](https://deepmind.google/blog/introducing-gemini-4-neon/) ⭐️ 8.8/10

Google DeepMind 于 2026-11-18 官方发布 Gemini 4 Neon，是当前主流 AI agent 骨干模型的大版本升级，直接影响 agent 工程、工具链配置与评估流程。社区观察显示，Neon 整体智能评分高于 Gemini 4 Carbon，但在 CritPt 等研究级推理评估中得分更低；OpenRouter 实测其吞吐达 127 tokens/秒（https://openrouter.ai/google/gemini-4-neon），约为 Carbon 的 2.7 倍（https://openrouter.ai/google/gemini-4-carbon）。

rss · Google DeepMind · 11月18日 21:35

**「为什么重要」** 作为广泛用于 AI agent 场景的骨干模型新版本，其能力、API 与评估规则调整会直接传导至 agent 架构、harness 配置与工具链选型。目前仅看到社区初步观察，具体官方调整细节需以正式文档为准。

**「可关注」** 可关注：Gemini 4 Neon 与 Carbon 的定位差异及实测吞吐差异，后续需核对官方文档确认 API 兼容性与适用场景边界。

**「评论」** 社区对 Gemini 系列频繁推出的新命名表示疲惫，同时围绕 Neon 与 Carbon 的定位差异、实测速度差异展开讨论，关注模型能力与场景的匹配逻辑。

**标签**: `#coding-agent`, `#eval`, `#harness`

---

<a id="item-agent-engineer-2"></a>
### [DaisyRose-27B 开源 强化学习 Agent 后训练模型](https://huggingface.co/blog/RadixArk/daisyrose-27b-pushing-the-frontier-of-post-trainin) ⭐️ 8.3/10

RadixArk 于 2026 年 11 月 18 日发布首款模型 DaisyRose-27B，基座为 Qwen3.8-27B，采用 Apache 2.0 协议开源。模型通过 RadixArk 自研的 Miles 框架做强化学习后训练，训练集为 1200 个精心筛选的长时序 Agent 任务，在 144 张 H200 GPU 上训练 18 天，支持最长 1M token 的会话，单次训练尝试最长运行 1.5 小时，支持 100 次以上工具调用、256K 以上输出 token，保留基座的架构、分词器、对话模板、图像理解能力与 256K token 上下文窗口，训练过程使用 harness summarization 折叠多轨迹。Terminal-Bench 4.1 pass@1 从基线的 5.6%提升至 12.0%，其余推理、指令遵循、编程基准均有提升，官方推荐使用 SGLang 搭配 DSpark 推测解码部署。

rss · Hugging Face Blog · 11月18日 19:54

**「为什么重要」** 已发生的变化是 DaisyRose-27B 验证了小规模 curated 任务集配合高效异步训练框架，即可在 Agent 后训练场景拿到 Terminal-Bench 4.1 翻倍的性能提升，且模型、训练框架 Miles 均开源。尚未证实的影响是该效率优势能否复现到其他基座模型、任务场景，以及社区实际测试后的泛化表现。

**「可关注」** RadixArk 自研异步训练后端在 Agent 长轨迹训练上的 MFU 达 37%，较同配置开源 Megatron 方案降低 57% GPU 耗时；其基于 AgentENV 的弹性内存沙箱服务，云基础设施成本较主流云沙箱提供商低 80%，且训练全程沙箱创建成功率维持在 99.95%以上。

**「评论」** 社区讨论主要围绕三点：一是对仅用 1200 个任务就拿到大幅基准提升的泛化性存疑，有用户认为可能存在 benchmaxxing；二是用户期待出现 GGUF 格式量化版本以便本地测试；三是已有用户指出同类基于 Qwen3.8 的竞品模型 Sabi-noema 已发布，可作对比参考。

**标签**: `#coding-agent`, `#eval`, `#harness`

---

<a id="item-agent-engineer-3"></a>
### [180B MoE 模型 32GB 内存运行方案](https://huggingface.co/blog/moe-expert-streaming) ⭐️ 7.8/10

2026 年 11 月 18 日 Hugging Face 官方博客发布 MoE 推理优化技术，支持 180B 参数 MoE 模型在 32GB 内存设备上通过 SSD 流式传输专家运行，token 生成性能比 Strata 基线低 6%。该方案基于 huggingface/transformers\#50717 拉取请求实现，核心改进是将逐专家 Python 循环替换为预分配设备槽池的 LRU 缓存，复用原生 grouped\_mm 内核，无需自定义专家矩阵乘法。对比测试显示，该方案在 24GB 显存的 A10G 上运行 Qwen3.6-35B-A3B 时，decode 速度达 82-88 tok/s，高于 llama.cpp Q8\_0 的 63-64 tok/s、vLLM FP8 专家 offload 的 20.1 tok/s，远高于 Transformers 原生 Accelerate offload 的 0.16 tok/s。实测 Qwen3.8-Flash-Next（含 121GB FP8 专家权重、51GB n-gram 嵌入表）在 32GB 内存设备上加载后占用约 18GiB，6K 长度提示词峰值内存占用 25.4GiB，专家经 3 比特量化后磁盘存储占用 49GB、设备缓存占用 12GiB。当前方案 API 仍在与 Transformers 维护者讨论阶段，量化专家配置可能后续调整为走 per-layer 量化计划而非当前自定义选项。

rss · Hugging Face Blog · 11月18日 00:00

**「为什么重要」** 该方案填补了 Transformers 原生对超大参数 MoE 模型低内存推理的能力空白，实测性能接近专用推理引擎 Strata，显著优于现有主流开源引擎的 MoE offload 表现；但当前代码尚未合并到 Transformers 主分支，量产工具链适配仍需等待。

**「可关注」** 可关注 huggingface/transformers\#50717 的 PR 进展，该方案通过槽池缓存复用原生内核的设计，避免了逐专家循环的性能损耗和自定义内核的开发成本，若合并将直接降低本地 MoE 模型的部署硬件门槛。

**标签**: `#memory`, `#harness`, `#inference`, `#model-optimization`

---

<a id="item-agent-engineer-4"></a>
### [Genie 4 正式发布](https://deepmind.google/blog/genie-4-is-now-available/) ⭐️ 7.8/10

Google DeepMind 于 2026-11-18 正式发布 Genie 4。这是其交互式环境生成平台的最新主要版本，面向 AI agent 开发、训练与评估工作流。当前官方公告未披露具体技术改进细节、性能数据或 API 变更。

rss · Google DeepMind · 11月18日 18:13

**「为什么重要」** 这是 agent 领域领先实验室的核心工具更新，直接影响 AI Agent 工程师的评估与训练基础设施选型。但具体能力边界、性能提升及与现有 harness 的兼容性尚未证实，需等待后续技术文档。

**「可关注」** 官方未公布具体技术细节与性能基准，现有基于 Genie 的 eval harness 需等待兼容性说明后再评估迁移成本。

**标签**: `#eval`, `#harness`

---

<a id="item-agent-engineer-5"></a>
### [OpenAI 芯片设计模型案例发布](https://openai.com/index/advancing-chip-design-with-our-models/) ⭐️ 7.0/10

2026 年 11 月 18 日 OpenAI 官方博客发布芯片设计相关案例，展示其模型在该领域的应用；HN 讨论中用户分享用 agent 将芯片设计视为软件设计问题，编写电路生成软件、自动化 EDA 流程，还可监控多轮数小时仿真，仅小部分设计为 RTL、主体为模拟电路；另有用户质疑未公开相关 RISC-V 设计，当前公开材料缺少深度技术实现、基准测试与可复现产物。

hackernews · vighneshiyer · 11月18日 17:45 · [社区讨论](https://news.ycombinator.com/item?id=50549493)

**「为什么重要」** 该案例是模型落地芯片设计这类高复杂度工程场景的公开参考，HN 讨论披露的 agent 自动化 EDA、长任务监控的实践模式，对 coding agent/ harness 工程师有直接参考价值；但当前公开内容未包含可复现的技术细节与性能数据，实际落地效果尚未证实。

**「可关注」** 可关注：agent 在长周期工程任务（如多小时 EDA 仿真）中的监控与调度模式，以及将硬件设计问题转化为软件生成任务的工程思路。

**「评论」** HN 讨论中用户认可 agent 辅助芯片设计的实践价值，同时存在两类争议：一是 AI 公司向客户所在行业扩张可能形成竞争关系，二是本次案例未公开 RISC-V 设计等可复现内容，另有用户调侃芯片命名 Jalapeño 的巧思。

**标签**: `#coding-agent`, `#orchestration`

---

<a id="item-agent-engineer-6"></a>
### [curl AI 重写未跟上人类修复](https://simonwillison.net/2026/Nov/18/daniel-stenberg/) ⭐️ 7.0/10

curl 项目负责人 Daniel Stenberg 2026 年 11 月 17 日在官方博客披露，AI 代理耗时约 3 周将 18.5 万行 curl C 代码重写为 34 万行 Rust 代码，同期人类 curl 团队合并 300+提交、修复 200+缺陷与多个安全漏洞，AI 重写版本未包含这些同期修复。该案例直接影响代码迁移工具选型、AI 编码代理能力评估与活跃开源项目的重写决策。

rss · Simon Willison · 11月18日 15:58

**「为什么重要」** 该案例是公开生产环境实证，已证实当前 AI 代码重写工具无法同步跟踪活跃维护代码库的持续迭代；尚未证实其对代码迁移工作流设计、代理评测体系的具体影响范围。

**「可关注」** 可关注：AI 代码迁移工具在活跃维护项目上的迭代同步能力仍是核心短板，重写结果需额外校验同期人类修复的缺陷与安全漏洞。

**标签**: `#coding-agent`, `#eval`, `#security`

---

<a id="item-agent-engineer-7"></a>
### [GPT-6.2 Astra/Sol 发布](https://latent.space/p/ainews-gpt-6-2-astra-the-2-frontier-model-is-better-and-20-600-cheaper-but-has-mixed-reviews-6-2-sol/) ⭐️ 7.0/10

2026 年 11 月 18 日 OpenAI 发布 GPT-6.2 Astra 与 Sol 两款前沿模型，已向 ChatGPT Work、Codex 的 Plus、Pro、Enterprise、Edu 用户及 API 开发者推送，API 标识为 gpt-6.2-astra 和 gpt-6.2-sol。两款模型均支持 1M 上下文、128K 输出上限，Astra API 价格为每百万 token 输入 8 美元、缓存输入 0.4 美元、输出 40 美元，Sol 定价为每百万 token 输入 2 美元、缓存输入 0.1 美元、输出 10 美元；企业版 Astra 额外配备法律搜索索引，在 Harvey LAB-AA 测试中得分 20.8%，高于基础版 Astra 的 15.0%；OpenAI 给 Astra 的 AI 自我改进能力评级为 High，为外部发布模型中首次，Vals 的 RSI-Index 从 27.07%升至 29.01%，50%为人类参考值。Artificial Analysis 的 Intelligence Index 测试显示 Astra 得 62 分，位列全球第二，仅次于 Fable 5.2 的 65 分；Epoch 验证其在 FrontierMath Erdős 测试中解出 7 道 Lean 格式题目，此前最佳为 3 道；Sol 的单任务成本约为 9 月版 Astra 的 15%，Astra 单任务成本较前代降低 20%至 600%。该发布为第三方实践者博客总结，非 OpenAI 官方完整内容，部分早期测试者反馈模型存在强化学习痕迹、子代理工作兼容性问题，评价两极。

rss · Latent Space · 11月18日 10:19

**「为什么重要」** 当前 Astra 是全球智能第二的前沿模型，且单位智能成本最优，对 AI agent 工程师的模型选型有直接参考价值；其两极的市场反馈是否会影响企业级 adoption，以及 Anthropic 即将 IPO 背景下的前沿模型竞争格局变化，尚未得到证实。

**「可关注」** 可关注：GPT-6.2 Sol 单任务成本仅为前代 Astra 的 15%，长工程任务、多轮编码场景可优先做对比测试，同时需验证其子代理输出与现有 agent harness 的兼容性。

**标签**: `#coding-agent`, `#eval`

---

<a id="item-agent-engineer-8"></a>
### [Xing 4 系列模型架构报告发布](https://huggingface.co/papers/2611.22115) ⭐️ 7.0/10

2026-11-18，Hugging Face Daily Papers 收录一篇关于 Xing 4 系列大语言模型的预印本技术报告。该模型基于 TeleChat 谱系，在 Ascend 芯片与 MindSpore 框架上针对智能体任务优化架构与训练流程。报告详述稀疏激活、注意力设计、模型深度与宽度权衡及推测解码对计算、内存访问和执行开销的影响，并介绍基于 MindSpore HyperParallel 的预训练基础设施，涵盖拓扑感知混合分片、分布式优化器执行及长序列工作负载与激活内存的协调管理。该工作面向 AI Agent 工程师，提供模型架构设计与训练工具链的具体技术细节。

rss · Hugging Face Daily Papers · 11月18日 00:00

**「为什么重要」** 该报告系统性公开了在国产芯片与框架上训练前沿智能体模型的工程实现细节，包括架构权衡与基础设施设计。对在 Ascend/MindSpore 栈上开展模型训练或 agent 能力优化的团队具有直接参考价值。

**「可关注」** 可关注：MindSpore HyperParallel 在拓扑感知混合分片与长序列激活内存管理上的具体实现，以及稀疏激活与推测解码在 agent 任务上的实际 trade-off 数据。

**标签**: `#coding-agent`, `#eval`, `#architecture`

---

<a id="item-agent-engineer-9"></a>
### [Self-Improvement Memory 论文发布](https://huggingface.co/papers/2611.18856) ⭐️ 7.0/10

2026-11-18，Hugging Face Daily Papers 收录论文《Self-Improvement Memory Enables Continual Recursive Self-Improvement》，提出 Self-Improvement Memory（SIM）机制。SIM 面向 harness optimizer 而非任务求解策略，通过按 recurring harness problem 分组记录历史编辑、修改理由、预测与观测结果及评估上下文，支持在策略模型或基准变化时继续执行 harness 优化（Continual Recursive Self-Improvement）。论文在四个领域完成实验验证，但具体性能数字未完全披露。

rss · Hugging Face Daily Papers · 11月18日 00:00

**「为什么重要」** SIM 针对 harness 优化中模型或基准迭代时历史经验丢失的缺口，将编辑 rationale 与 outcome 结构化存储，使优化器能在策略模型或基准变化后延续工作。对维护长期运行的 agent 与 eval 系统有直接参考价值。

**「可关注」** harness 优化器的记忆机制开始从无状态走向带上下文的历史追踪，记录编辑理由和评估上下文可能比单纯记录最终分数更有助于跨版本迁移。

**标签**: `#harness`, `#memory`, `#eval`

---

## AI 日报
{: #sec-ai-daily .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-daily" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-daily-1"></a>
### [Codex 沙箱功能发布](https://openai.com/index/inside-the-codex-sandbox) ⭐️ 7.8/10

OpenAI 官方博客发文介绍 Codex 沙箱功能，该功能支持在 macOS、Linux、Windows 系统上运行用户机器指令，同时可执行用户自定义控制的文件系统与网络访问限制。

rss · OpenAI Blog · 11月18日 08:00

**「为什么重要」** 该功能明确了 Codex 本地运行的跨平台支持范围与权限管控规则，为开发者在本地使用 AI 执行指令提供了可自主配置的安全边界。

**「可关注」** 可关注：Codex 本地运行时可自主配置文件系统与网络访问限制，覆盖 macOS、Linux、Windows 三端。

**标签**: `#lab`, `#product`

---

<a id="item-ai-daily-2"></a>
### [OpenAI 披露前沿 AI 风险管理实践](https://openai.com/index/managing-frontier-ai-risk) ⭐️ 7.8/10

OpenAI 于 2026 年 11 月 18 日发布官方博客，披露其从 AI 训练到部署全生命周期管理前沿 AI 风险的具体实践。核心措施涵盖模型对齐、沙箱隔离、阻断式 safeguards 及全流程监控。文章未披露具体技术参数或风险事件应对细节。

rss · OpenAI Blog · 11月18日 06:00

**「为什么重要」** 该内容来自 OpenAI 官方一手来源，清晰呈现头部 AI 实验室前沿 AI 风险管理的落地框架，对行业合规与风险防控实践有参考价值。

**「可关注」** 可关注：OpenAI 公开的前沿 AI 全周期风险管理框架中，阻断式 safeguards 与沙箱隔离的具体落地设计。

**标签**: `#lab`, `#policy`, `#industry`

---

<a id="item-ai-daily-3"></a>
### [OpenAI 模型实现芯片设计优化](https://openai.com/index/advancing-chip-design-with-our-models) ⭐️ 7.8/10

OpenAI 官方博客发布案例研究，披露其旗下模型（包括 GPT-6 Astra）已完成 Jalapeño 硅的电路优化，以及 RISC-V 核心设计的改进，展示了 AI 辅助芯片设计领域的最新进展。

rss · OpenAI Blog · 11月18日 00:00

**「为什么重要」** 该案例是 OpenAI 模型在芯片设计场景的公开落地实践，为 AI 辅助硬件设计领域提供了可参考的验证样本。

**「可关注」** 可关注：GPT-6 Astra 在电路优化、RISC-V 核心设计等硬件场景的落地效果与后续技术公开计划。

**标签**: `#model`, `#lab`, `#industry`

---

<a id="item-ai-daily-4"></a>
### [OpenAI 与费加罗报集团达成合作](https://openai.com/index/le-groupe-figaro-and-openai-announce-partnership) ⭐️ 6.8/10

OpenAI 与法国媒体集团 Le Groupe Figaro 达成内容合作，将把《费加罗报》的新闻内容接入 ChatGPT。接入形式为 AI 生成的新闻摘要、摘录，同时附上指向原始报道的链接。目前双方未披露合作的具体付费条款、覆盖内容范围等细节。

rss · OpenAI Blog · 11月18日 00:00

**「为什么重要」** 这是 OpenAI 与欧洲主流媒体集团的又一项内容合作，体现了 AI 公司与传统媒体在内容分发上的合作路径正在逐步落地。

**「可关注」** 可关注：AI 公司与传统媒体的内容合作正形成「摘要引流+原文链接」的标准化接入范式。

**标签**: `#lab`, `#industry`, `#product`

---

## AI 羊毛
{: #sec-ai-deals .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-deals" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-deals-1"></a>
### [Gemini Tasks 个人助理功能免费开放](https://blog.google/innovation-and-ai/products/gemini-app/tasks-in-gemini-free-new-features/) ⭐️ 7.0/10

Google 官方宣布将 Gemini 应用内的 Tasks 个人助理功能免费开放给用户。目前未公开该功能的具体使用额度、区域限制、领取条件及生效截止时间。

rss · HN Free API / Credits · 11月18日 20:20

**「可关注」** 可关注：该功能暂未公布具体使用限制、区域适配范围及免费有效期，使用前建议先确认账号所在区域是否可用。

**标签**: `#free-tier`, `#promo`

---