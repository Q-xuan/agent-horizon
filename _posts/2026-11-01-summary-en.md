---
layout: default
title: "Horizon Summary: 2026-11-01 (EN)"
date: 2026-11-01
lang: en
---

> From 152 items, 11 important content pieces were selected

---

**Agent Harness Architecture**
1. [pydantic-ai v2.64.0 发布](#item-harness-arch-1) ⭐️ 7.8/10
2. [Claude Code v2.1.316 发布](#item-harness-arch-2) ⭐️ 5.5/10
3. [Qwen Code 登 GitHub Trending](#item-harness-arch-3) ⭐️ 5.0/10

**AI Agent Engineer**
1. [HF 每日论文：Youtu-Parsing-Omni 跨模态解析](#item-agent-engineer-1) ⭐️ 7.0/10
2. [WorkFactory 可扩展智能体训练框架](#item-agent-engineer-2) ⭐️ 7.0/10
3. [Co-Design Bench 多模态编码基准发布](#item-agent-engineer-3) ⭐️ 7.0/10
4. [VibeGame 提示词转2D游戏框架公开](#item-agent-engineer-4) ⭐️ 6.0/10
5. [QwenPU 在 Qwen 权重内编译 NPU](#item-agent-engineer-5) ⭐️ 6.0/10
6. [inspect\_ai 0.3.287 发布](#item-agent-engineer-6) ⭐️ 5.5/10
7. [Betelgeuse 实现 RTX 3060 跑 68B MoE 22 tok/s](#item-agent-engineer-7) ⭐️ 5.5/10
8. [Betelgeuse 跑通 Qwen 3.8 Flash Next IQ4\_XS 24 tok/s](#item-agent-engineer-8) ⭐️ 5.5/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [pydantic-ai v2.64.0 发布](https://github.com/pydantic/pydantic-ai/releases/tag/v2.64.0) ⭐️ 7.8/10

pydantic-ai v2.64.0 发布，调整兼容性与工具默认行为。重试传输放弃后抛出 ModelHTTPError，服务端状态 ID 仅回传给创建端点。Coder 工具默认关闭严格 schema，需 Coder\(strict=True\) 显式启用。json-repair 变为可选依赖，仅 Coder 与 RepairToolArguments 需要。新增 ModelFallback 能力、first\_event\_timeout 模型设置与 BoxdSandbox 工作区。

github · dsfaccini · Oct 30, 23:27

**「设计要点」** 能力系统扩展 RunContext.load\_capability 支持按需加载，ModelFallback 提供 per-attempt prepare\_model\_request 钩子与 RetryModelRequest。ArtifactScanner 为 Memory 与 Skills 增加制品安全扫描。BoxdSandbox 将 Coder、Shell、FileSystem 等能力运行在隔离机器中。服务端状态通过引用计数管理实时会话生命周期。

**「改了什么」** Coder 工具默认关闭严格工具 schema，json-repair 改为可选依赖。新增 ModelFallback 能力、first\_event\_timeout 设置与 BoxdSandbox 工作区；服务端状态 ID 限制为创建端点，重试传输放弃后抛出 ModelHTTPError。

**Tags**: `#runtime`, `#tools`, `#context`

---

<a id="item-harness-arch-2"></a>
### [Claude Code v2.1.316 发布](https://github.com/anthropics/claude-code/releases/tag/v2.1.316) ⭐️ 5.5/10

Claude Code v2.1.316 官方发布。新增 \`CLAUDE\_CODE\_SUBAGENT\_EFFORT\` 子代理 effort 控制、apps gateway 分层策略合并与共享群组预算、Bedrock guardrail 输入标签；修复 Bash 工具别名与脚本执行、auto mode 安全判定、云会话同步、VS Code 集成等 20 余项缺陷。Opus 4.8 fast mode 已标记弃用，2026-11-30 停止服务。

github · ashwin-ant · Oct 31, 01:01

**「设计要点」** apps gateway 引入 \`managed.policy\_mode: layered\` 实现多策略分层合并，替代原有单策略匹配；\`pooled\_budget\` 为群组提供共享月度预算；子代理 effort 通过环境变量独立配置，解耦父子会话级联。

**「改了什么」** 新增子代理 effort 环境变量、apps gateway 分层策略与群组共享预算、Bedrock guardrail 输入标签；Opus 4.8 fast mode 进入弃用期。修复涵盖 shell 命令未随进程退出、Bash 别名乱码、auto mode 无安全判定时未标记失败、云会话文件搜索路径错误、模型不可用时未降级等运行时问题。

**Tags**: `#subagents`, `#permissions`, `#runtime`, `#sandbox`

---

<a id="item-harness-arch-3"></a>
### [Qwen Code 登 GitHub Trending](https://github.com/QwenLM/qwen-code) ⭐️ 5.0/10

QwenLM/qwen-code 是一个开源终端 AI coding agent，近期登上 GitHub Trending。该项目宣传支持 Auto-Memory、Auto-Skills、SubAgents、Agent Teams 及 MCP，主打动态工作流与零配置。目前仅见高层功能列表，无官方版本号、接口定义或架构实现细节。

rss · GitHub Trending Daily · Oct 31, 23:00

**Tags**: `#mcp`, `#memory`, `#subagents`, `#open-source-agent`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [HF 每日论文：Youtu-Parsing-Omni 跨模态解析](https://huggingface.co/papers/2610.39301) ⭐️ 7.0/10

2026年10月31日HF每日论文收录Youtu-Parsing-Omni跨模态解析器，该论文在HF每日论文板块获得68次赞同。其核心设计为单编码器适配所有模态、单Schema覆盖所有任务，可将文档、图像、音频、视频转为时空对齐的结构化记录，为Agent提供跨模态感知与跨模态证据定位能力。技术细节包括Youtu-Omni-Encoder基于预训练语言模型初始化，所有模态在共享权重的统一时空坐标系下编码，少量融合层实现视频帧与并发音频的跨模态注意力；OmniSchema统一10类解析任务的输出格式，支持单次自进化后训练流程。当前仅公开论文摘要，无性能基准、实现代码及生产环境验证信息，主要面向多模态Agent感知层建设的工程师。

rss · Hugging Face Daily Papers · Oct 31, 23:00

**「为什么重要」** 该论文提出的统一编码器+统一Schema设计，为多模态Agent感知层建设提供了可参考的技术路径；但目前仅公开摘要，无性能基准与实现代码，实际工程价值尚未得到验证。

**「可关注」** 可关注：统一模态编码器搭配共享时空坐标系、统一任务Schema的跨模态感知层设计，以及单次后训练覆盖多任务的实现思路。

**Tags**: `#harness`, `#multi-modal`, `#agent`, `#perception`, `#encoder-architecture`

---

<a id="item-agent-engineer-2"></a>
### [WorkFactory 可扩展智能体训练框架](https://huggingface.co/papers/2610.37161) ⭐️ 7.0/10

2026年10月31日，Hugging Face Daily Papers收录WorkFactory相关论文，提出可扩展的智能体训练任务构建框架。该框架从专业意图出发，通过信息级规划构建信息支持图指导任务实例化，再通过探针执行识别支持故障并修复，解决专业任务信息缺失/不一致导致教师模型执行失败、监督信号弱的问题。研究团队已构建覆盖612个职业的112686条可执行任务数据集，用于语言模型微调，面向AI Agent训练场景。

rss · Hugging Face Daily Papers · Oct 31, 23:00

**「为什么重要」** 该框架提供了可复用的规模化专业任务构建方案，直接填补了智能体监督训练中高质量专业任务数据不足的缺口，对AI Agent工程师的训练工具链有明确参考价值。目前尚未公开该数据集的具体使用效果与开源计划。

**「可关注」** 可关注：WorkFactory的信息支持图构建与探针执行修复机制，可作为专业场景智能体训练任务生成的参考实现。

**Tags**: `#orchestration`

---

<a id="item-agent-engineer-3"></a>
### [Co-Design Bench 多模态编码基准发布](https://huggingface.co/papers/2610.35138) ⭐️ 7.0/10

2026年10月31日Hugging Face Daily Papers发布多模态协同编码评估基准Co-Design Bench。该基准为免参考设计，从26314个真实用户编码会话的37463条去重查询中整理构建273个任务，包含多模态编辑（ME）、仓库编辑（RE）两个赛道，覆盖Grounded Understanding、UI Transformation、Functional Implementation三个能力维度，任务对配备标准化请求与可运行编辑前应用，配套2331条隐藏专家编写的接受标准，采用judge-then-refute评分协议，基于源码与浏览器证据完成评分。该基准面向多模态编码agent的评估与开发场景。

rss · Hugging Face Daily Papers · Oct 31, 23:00

**「为什么重要」** 当前多模态编码agent评估多依赖人工参考或窄场景测试，该基准直接使用真实用户编码会话数据构建，覆盖协同编码核心场景，可填补高真实感多模态编码评估的空白，为agent能力迭代提供可复用的量化参考。

**「可关注」** 可关注：该基准免参考设计降低评估成本，两类赛道覆盖多模态局部编辑与仓库级协同编辑场景，judge-then-refute评分协议结合源码与浏览器证据，可直接接入现有coding agent评估流程。

**Tags**: `#eval`, `#coding-agent`

---

<a id="item-agent-engineer-4"></a>
### [VibeGame 提示词转2D游戏框架公开](https://huggingface.co/papers/2610.33106) ⭐️ 6.0/10

2026年10月31日Hugging Face Daily Papers公开推介VibeGame研究框架，支持从自然语言提示词（可搭配参考图）端到端生成完整2D游戏项目。其AI原生游戏引擎将项目状态表示为schema校验的结构化文本，提供帧同步运行时控制，允许智能体按需检查游戏状态、执行动作、验证行为；框架配套设计了自进化对抗式LLM智能体团队协调开发流程。目前仅公开论文摘要，完整实现与效果未披露，相关设计对多智能体编排、状态交互式环境harness的工程师有参考价值。

rss · Hugging Face Daily Papers · Oct 31, 23:00

**「为什么重要」** 该框架尝试将LLM智能体的自然语言交互能力拓展到需协调代码、场景、资源、物理等多模块的2D游戏开发场景，其结构化状态接口、帧同步控制的设计为交互式环境的agent交互提供了可参考的范式。但目前仅公开摘要，框架的实际开发效率、游戏可玩性、多智能体对抗机制的效果均未得到公开验证，对通用编码智能体工作流的参考价值仍需进一步评估。

**「可关注」** 可关注：VibeGame 采用的 schema 校验结构化状态接口、帧同步运行时控制机制，以及自进化对抗式多智能体团队的编排方式，对状态交互式环境的 agent harness 设计有参考价值。

**Tags**: `#harness`, `#orchestration`, `#coding-agent`

---

<a id="item-agent-engineer-5"></a>
### [QwenPU 在 Qwen 权重内编译 NPU](https://www.reddit.com/r/LocalLLaMA/comments/1xkiuut/an_llm_inside_an_llm_same_guy_who_put_a_riskv_cpu/) ⭐️ 6.0/10

一位开发者发布 QwenPU 项目，将 NPU 编译进 Qwen 3.5-4B 的权重中，使 Karpathy 的 stories260k LLM 能在原模型参数内以 bit-exact 方式运行 matmul、softmax 和 attention，无需外部工具。代码与权重已公开于 GitHub（divagr18/QwenPU）与 HuggingFace（divagr1925/QwenPU），但完整技术文档、性能基准和优化细节仍在撰写中，作者表示正在优化体积与速度。

reddit · r/LocalLLaMA · /u/LatentSpacer · Oct 31, 19:18

**「为什么重要」** 这展示了在模型权重空间内嵌入可计算单元并运行完整 LLM 的可行性，突破了传统推理依赖外部算力的模式。但目前缺乏可验证的性能数据和详细技术说明，其实际效率、稳定性及对 coding agent 的潜在影响仍需等待完整技术文章发布后评估。

**「可关注」** 可关注：权重内嵌 NPU 的完整技术文档与性能基准仍在撰写中，可验证其 bit-exact 实现是否能在无外部工具条件下达到可用推理速度。

**Tags**: `#coding-agent`, `#model-architecture`, `#weight-manipulation`

---

<a id="item-agent-engineer-6"></a>
### [inspect\_ai 0.3.287 发布](https://github.com/UKGovernmentBEIS/inspect_ai/releases/tag/0.3.287) ⭐️ 5.5/10

\`inspect\_ai\` 0.3.287 于 2026-10-31 发布。运行时可在 \`react\(\)\` 回合边界持有并重写对话，compaction handler 新增 \`reset\(\)\`；\`range\_goal\` 注册表类型预留给 \`inspect\_ranges\`。sentinel host 开始上报 monitor model 的输入预算与 token 计数。缺陷修复包括：sandbox-bridged agent 达限时终止 Agent 而非样本、Anthropic 工具变更导致 unrecognised 模型签名错误、Gemini 长解码响应不再受 per-request 输出上限截断，以及 Docker Engine 28 未知用户报告为不支持。

github · github-actions\[bot\] · Oct 31, 16:33

**「为什么重要」** \`react\(\)\` 的回合级重写与 sentinel 的 token 预算可见性，会改变现有 harness 对长任务内存管理与监控指标的假设；沙箱桥接 Agent 的终止逻辑修正，将故障域从样本缩小到单个 Agent，可能影响现有容错脚本的预期。

**「可关注」** 可关注：若现有流程依赖 sandbox-bridged agent 的样本级重试，需适配 0.3.287 将“Agent 达限”改为终止 Agent 而非样本的语义变更；同时 \`react\(\)\` 的回合边界重写与 sentinel 的 token 预算上报，可能要求下游日志解析与内存策略同步调整。

**Tags**: `#eval`, `#orchestration`, `#observability`, `#memory`, `#permissions`

---

<a id="item-agent-engineer-7"></a>
### [Betelgeuse 实现 RTX 3060 跑 68B MoE 22 tok/s](https://www.reddit.com/r/LocalLLaMA/comments/1xk8s6z/betelgeuse_running_qwen_38_flash_next_at_22_toks/) ⭐️ 5.5/10

2026年10月31日，Reddit用户/u/zyxciss分享其开发的llama.cpp分支Betelgeuse（bel-cli/bel-server，已提交上游llama.cpp PR \#31469）的 anecdotal 测试结果：在受MemoryMax=12G cgroup限制的RTX 3060 12GB + 16GB单通道DDR4消费级PC上，可100% bit-exact运行68B参数的Qwen 3.8 Flash Next MoE模型（GSQ-RCO-IQ2\_XS量化），经28,080条路由器记录和576个生成token的字节级对比，输出与stock llama.cpp完全一致（0差异），持续解码速度达22 tok/s，峰值 bursts 可达48 tok/s，无任何专家丢弃。同配置下stock llama.cpp因mmap颠簸仅跑1.47 tok/s，单token物理SSD读取达208–312 MiB；同场景优化工具Strata在强制--low-ram mmap模式下仅8.11 tok/s，单token SSD读取约105 MiB；Betelgeuse则将单token物理SSD读取降至12.43 MiB。即使是对更大参数的Q8\_K\_XL量化版本（总大小约190GB），Betelgeuse也能跑出8 tok/s冷启动、12 tok/s warm的速度，峰值 bursts 达21 tok/s，而stock llama.cpp直接OOM或低于0.1 tok/s。该结果未提供可复现的测试脚本、硬件环境细节有限，属于个人分享的未验证 anecdotal 数据，仅对本地消费级硬件跑MoE模型的场景有参考价值。

reddit · r/LocalLLaMA · /u/zyxciss · Oct 31, 12:20

**「为什么重要」** 该结果绕开了此前MoE推理为提速普遍采用的专家丢弃/门控剪枝方案，展示了在极低内存消费级硬件上运行大参数MoE模型且不损失输出精度的可行性。但该架构的通用性、长期稳定性以及对其他MoE模型的适配效果尚未得到社区独立验证，实际落地价值仍待观察。

**「可关注」** 可关注：MoE推理在低内存消费级硬件上的提速可通过「VRAM专家槽池+RAM victim cache+io\_uring预读+单CUDA Graph回放」的组合实现，且无需牺牲输出精度，但该方案目前仅来自个人项目的 anecdotal 数据，尚未经过社区复现验证。

**Tags**: `#coding-agent`, `#local-llm`, `#inference-optimization`, `#moe`

---

<a id="item-agent-engineer-8"></a>
### [Betelgeuse 跑通 Qwen 3.8 Flash Next IQ4\_XS 24 tok/s](https://www.reddit.com/r/LocalLLaMA/comments/1xkh2ns/betelgeuse_running_qwen_38_flash_next_iq4_xs_at/) ⭐️ 5.5/10

2026年10月31日，Reddit社区用户/u/zyxciss分享Betelgeuse（bel-cli / bel-server）推理工具的社区自测 benchmark：在RTX 3060 12GB + 16GB总系统RAM的配置下，运行IQ4\_XS量化的Qwen 3.8 Flash Next模型时，双通道2x8GB DDR4配置下吞吐达24 tok/s，单通道1x16GB DDR4配置下为14 tok/s，两次测试均实现0 dropped experts、100%字节级输出对齐。对比基线为同配置下stock llama.cpp跑IQ4\_XS双通道仅~0.6 tok/s（出现内存颠簸），Strata（--low-ram）双通道仅5-6 tok/s。该数据无官方第一方验证，仅对使用Betelgeuse工具栈开展低RAM本地Agent部署的工程师有参考价值。

reddit · r/LocalLLaMA · /u/zyxciss · Oct 31, 18:06

**「为什么重要」** 这回应了社区此前对低比特量化MoE推理实用性的质疑，首次给出IQ4\_XS这一常用4-bit量化档位下Betelgeuse相对主流本地推理工具的实机性能差距，同时验证了双通道系统RAM对MoE专家调度的实际影响。

**「可关注」** 可关注：消费级低RAM环境下，MoE推理性能受系统RAM通道数影响显著，Betelgeuse的Exclusive Host RAM Victim Cache + 异步硬件DMA架构可在保持100%输出对齐的前提下，实现相对stock llama.cpp的数倍吞吐提升。

**Tags**: `#toolchain`, `#quantization`, `#local-inference`, `#moe`

---