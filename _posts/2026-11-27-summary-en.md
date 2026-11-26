---
layout: default
title: "Horizon Summary: 2026-11-27 (EN)"
date: 2026-11-27
lang: en
---

> From 200 items, 10 important content pieces were selected

---

**Agent Harness Architecture**
1. [@e2b/acp 0.1.0 发布](#item-harness-arch-1) ⭐️ 7.8/10
2. [Instructor v1.18.0 发布](#item-harness-arch-2) ⭐️ 6.8/10
3. [browser-use 1.0.9 发布](#item-harness-arch-3) ⭐️ 5.5/10

**AI Agent Engineer**
1. [Nemotron 3.5 Parse 开源数据与推理优化](#item-agent-engineer-1) ⭐️ 7.8/10
2. [Hugging Face 多智能体 swarm 训练指南 Part 1 发布](#item-agent-engineer-2) ⭐️ 7.8/10
3. [llama.cpp AMD 基准看板发布](#item-agent-engineer-3) ⭐️ 6.3/10
4. [Google MCP 权限收紧](#item-agent-engineer-4) ⭐️ 6.0/10
5. [sqlite3\_rsync 远程快照复制](#item-agent-engineer-5) ⭐️ 6.0/10
6. [Play2Evolve 游戏框架论文预览发布](#item-agent-engineer-6) ⭐️ 6.0/10
7. [AIRIS 社会具身智能基准发布](#item-agent-engineer-7) ⭐️ 5.5/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [@e2b/acp 0.1.0 发布](https://github.com/e2b-dev/E2B/releases/tag/%40e2b/acp%400.1.0) ⭐️ 7.8/10

E2B 发布 \`@e2b/acp\` 0.1.0，首次支持在 E2B 沙箱内运行 ACP 兼容 agent（Goose、OpenCode、Claude Code 通过 ACP adapter）。调用 \`new ACPAgent\(sandbox, command, client\)\` 创建实例，\`await agent.start\(\)\` 通过 stdin/stdout 启动 agent 并连接客户端。该版本关闭客户端文件系统与终端能力，拒绝 agent 对这两项能力的请求，强制 agent 使用沙箱原生工具执行文件操作和命令。

github · github-actions\[bot\] · Nov 26, 12:35

**「设计要点」** Agent 在 E2B 沙箱内运行，通过 stdin/stdout 与外部 ACP client 通信。权限模型显式禁用客户端文件系统与终端能力，agent 请求这两项能力时直接被拒绝，确保所有文件编辑和命令执行都在沙箱原生工具层完成。

**「改了什么」** 新增 \`@e2b/acp\` 0.1.0 包，引入 \`ACPAgent\` 类支持在沙箱内运行 ACP 兼容 agent。内置能力限制拒绝 agent 对客户端文件系统与终端能力的请求。依赖更新至 \`e2b@2.65.0\`。

**Tags**: `#sandbox`, `#tools`, `#runtime`, `#permissions`

---

<a id="item-harness-arch-2"></a>
### [Instructor v1.18.0 发布](https://github.com/567-labs/instructor/releases/tag/v1.18.0) ⭐️ 6.8/10

Instructor v1.18.0 发布，修复缓存键冲突、重试终端钩子与多 provider 流式传输问题。核心层将 token-budget 策略与重试执行分离，Bedrock、GenAI 等 provider 模块接管 SDK 构造与请求配置。安全层面将原始响应日志改为 opt-in 并扫描提交，同时新增 typed Jev 决策模型。

github · jxnl · Nov 26, 21:02

**「设计要点」** 核心层拆分运行时响应序列化与缓存策略，provider 模块独立封装 SDK 构造与请求配置策略，形成更清晰的职责边界。

**「改了什么」** 修复缓存映射键冲突，恢复带 envelope 字段名的旧响应格式；拆分 token-budget 策略与重试执行，分离运行时响应序列化；Bedrock、GenAI provider 模块接管 SDK 构造与请求配置。流式传输支持请求本地路由、Unicode 控制字符保留、字段别名解析；批处理保留输出文件、拒绝截断结果、标准化 provider 任务状态；安全修复包括请求日志保护、原始响应日志 opt-in 与提交扫描；新增 typed Jev 决策模型，修复 Anthropic thinking 与工具使用默认值。

**Tags**: `#cache`, `#runtime`, `#providers`

---

<a id="item-harness-arch-3"></a>
### [browser-use 1.0.9 发布](https://github.com/browser-use/browser-use/releases/tag/1.0.9) ⭐️ 5.5/10

这是browser-use官方1.0.9补丁版本发布，新增云浏览器IP轮换能力缓解站点IP封禁问题，修复Claude提示词缓存跨路由失效导致的重复计费问题。新增的\`rotate\_proxy\`接口支持按站点国家指定出口IP，仅在站点因IP封禁时触发，单站点最多触发一次，11个常用封禁站点通过率从48%提升至62%；修复覆盖OpenRouter、Bedrock及OpenRouter后置ChatOpenAI三类Claude路由。

github · gregpr07 · Nov 26, 22:45

**「改了什么」** \1. 新增\`rotate\_proxy\(country=None\)\`接口，云浏览器优先通过自身连接切换出口IP，无需API密钥，API仅作为降级方案；切换时保留标签页、Cookie与登录态，仅在页面触发IP封禁时触发，单站点最多触发一次，支持按站点顶级域指定对应国家出口，11个封禁站点通过率从48%提升至62%；\`rotate\_proxy\`在云服务无可用新出口IP时会明确报错，指向browser-use.com主机的\`Browser\(cdp\_url=...\)\`实例均视为云浏览器。2. 修复Claude提示词缓存失效问题，覆盖\`openrouter:anthropic/...\`、\`bedrock:\` Claude模型、\`ChatOpenAI\(..., base\_url=&\#x27;https://openrouter.ai/api/v1&\#x27;\)\`三类路由，消除此前每步全量提示词重复计费、缓存读取值始终为0的问题；Bedrock路由仅通过单元测试验证，未做实机测试。相关实现见PR \#6540、\#6546。

**Tags**: `#sandbox`, `#tools`, `#runtime`, `#prefix-cache`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [Nemotron 3.5 Parse 开源数据与推理优化](https://huggingface.co/blog/nvidia/building-on-nemotron-35-parse-open-data-fine-tunin) ⭐️ 7.8/10

2026年11月26日NVIDIA与Hugging Face联合发布Nemotron 3.5 Parse文档模型的配套开源资源，包括3份合计约1890万条示例的合成训练数据集、端到端微调指南，以及DFlash2推测解码推理优化方案，同时公开了该模型的SFT+RLVR两阶段训练流程。关键细节：3份数据集分别为Synthetic Charts V1（998万条）、Synthetic Tables V1（100万条）、OCR Synthetic Multilingual v2（790万条），均含图像、标注与生成文档；架构层面将固定尺寸预处理改为NaViT动态矩形输入，用压缩视觉token因果前缀替代编码器-解码器交叉注意力，解码器采用GQA-8注意力降低缓存内存占用；DFlash2在单H200、BF16精度、并发1时吞吐较Parse 3.5禁用推测解码提升7.62倍，并发512时提升1.52倍；两阶段训练后循环输出页面数从126降至29（降幅77%），达到9000 token限制的输出从185降至35，整体评分从66.24升至71.38，表格和图表维度分别提升5.18和4.15分。上述资源面向构建RAG、agent系统中文档处理能力的工程师开放；此外官方还提供了单次/两次/三次解析的级联方案，两次和三次解析较单次分别提升2.18和2.46个ParseBench点，支持在吞吐和提取精度间做权衡。

rss · Hugging Face Blog · Nov 26, 05:05

**「为什么重要」** 官方首次公开Nemotron 3.5 Parse的完整训练数据、微调流程和推理优化实现，为文档解析能力的定制化开发提供了可复现的基础；目前尚未有公开证据证明这些方案在其他硬件栈、其他文档类型上的效果与官方基准一致。

**「可关注」** 可关注：DFlash2推测解码在单H200高并发场景下的吞吐提升表现，以及SFT+RLVR训练流程对降低循环输出、提升表格/图表提取准确率的可复现效果。

**Tags**: `#coding-agent`, `#harness`, `#memory`

---

<a id="item-agent-engineer-2"></a>
### [Hugging Face 多智能体 swarm 训练指南 Part 1 发布](https://huggingface.co/blog/training-swarms) ⭐️ 7.8/10

Hugging Face 发布多智能体 swarm 技术博客系列第一部分，提供可复现的小模型训练与评估示例。首篇实验配置为 4 个智能体共享一个 Qwen3-0.6B 策略，在信息聚合任务上测试通信收益，运行于 2 张 H200 约 5 小时，成本约 50 美元。实验采用集中式训练与去中心化执行，团队奖励按 36,864 token 预算扣减，每轮 8 次尝试。系列核心问题为：智能体间通信是否真正提升性能，还是仅增加计算消耗。

rss · Hugging Face Blog · Nov 26, 00:00

**「为什么重要」** 博客系列提供可复现示例与具体 runtime、费用数据，填补多智能体 swarm 实践中的可复现性空白。对 coding agent 工程师而言，这是从小模型、小团队规模直接测量通信收益的实践材料。

**「可关注」** 可关注：多智能体系统的性能对比必须在固定 token 预算下进行，否则无法区分通信增益与单纯增加尝试次数的效果。

**Tags**: `#eval`, `#orchestration`, `#multi-agent-system`, `#training`

---

<a id="item-agent-engineer-3"></a>
### [llama.cpp AMD 基准看板发布](https://huggingface.co/blog/ggml-org/llamacpp-amd-bench) ⭐️ 6.3/10

On November 26, 2026, Hugging Face officially launched the llama.cpp × AMD benchmark dashboard, a public tool for tracking local inference performance on AMD Ryzen and Radeon hardware. The dashboard currently supports two GPU models: Radeon 8060S \(gfx1151\) and Radeon AI Pro R9700S \(gfx1201\), and offers three tabs: Overview for cross-quantization comparison, Build history for tracking performance across builds, and Context scaling for observing throughput changes as context length grows. It allows comparison of PP512 \(512 input token processing throughput\) and TG128 \(128 token generation throughput\) metrics across different llama.cpp builds, models, and quantization formats. Benchmark runs use the llama-bench tool with Flash Attention toggled on and off, 10 repetitions per configuration, and are scheduled weekly; results are stored publicly in the ggml-org/install.sh-benches-data Hugging Face storage bucket. Supported models include Inkling 2 Mini, Qwen, Gemma, gpt-oss, and LFM, with quantization options covering Q4\_K\_M, Q8\_0, BF16, F16 and other formats.

rss · Hugging Face Blog · Nov 26, 11:37

**「为什么重要」** The dashboard fills the gap of publicly available llama.cpp inference benchmarks for AMD hardware, allowing developers to compare performance across quantizations and builds without setting up their own benchmark pipeline. However, its audience is limited to AMD local inference developers, making it a routine addition to the evaluation toolchain rather than a breakthrough for the broader AI community.

**「可关注」** 可关注：Public benchmark data can be directly downloaded and reused, or compared with local llama-bench run results to verify the performance of your own hardware and configurations.

**Tags**: `#eval`, `#observability`, `#harness`

---

<a id="item-agent-engineer-4"></a>
### [Google MCP 权限收紧](https://techstackups.com/articles/google-workspace-ai-agents-mcp/) ⭐️ 6.0/10

2026-11-26 的一篇二手报道及 Hacker News 讨论称，Google 要求 AI agent 必须使用其官方 Workspace MCP 服务器。报道指出 Gmail MCP 服务器无法发送邮件，而社区评论指出 MCP 本身已有 elicitation 原语可用于工具调用前的人工确认，因此该限制更可能是商业决策而非安全措施。目前材料中未包含 Google 官方直接公告，技术细节仅涉及政策限制与社区讨论。受影响方包括依赖 Google Workspace 的 agent 开发者及使用第三方 agent 的企业用户。

hackernews · ritzaco · Nov 26, 09:44 · [Discussion](https://news.ycombinator.com/item?id=50653477)

**「为什么重要」** 此事值得关注，因为它直接涉及 MCP 服务器权限设计、agent 工具链选型，以及云服务商通过按使用量计费抬高 agent 集成成本的可能趋势。目前报道为二手来源，商业动机与官方政策细节尚未经 Google 直接证实。

**「可关注」** 可关注：MCP 协议已提供 elicitation 原语支持调用前确认，但平台仍可能以安全为名实施功能限制，设计 agent 工具链时需区分协议能力与平台政策。

**「评论」** 社区评论普遍认为 Gmail MCP 禁发邮件是商业决策而非安全措施，并担忧供应商锁定与按使用量计费成本上升。部分用户提到浏览器自动化等规避方案，但认为其冗余且可能违反服务条款。

**Tags**: `#mcp`, `#permissions`, `#orchestration`

---

<a id="item-agent-engineer-5"></a>
### [sqlite3\_rsync 远程快照复制](https://simonwillison.net/2026/Nov/26/sqlite3-rsync/) ⭐️ 6.0/10

Simon Willison 2026 年 11 月 26 日的博客介绍了 SQLite 官方工具 sqlite3\_rsync 的磁盘高效快照能力。该工具 2024 年 10 月随 SQLite 3.47.0 以实验性功能加入，2025 年 5 月 SQLite 3.50.0 增强。与备份 API 或 VACUUM INTO 需要完整本地副本不同，sqlite3\_rsync 可通过 SSH 直接复制快照，无需预留等量磁盘空间；同步机制类似 rsync，通过页级哈希比对仅传输差异内容，但副本与源差异极大时哈希交换开销可能导致带宽略超数据库大小（百分之几以内）。该工具对使用 SQLite 存储状态、记忆或评估数据的 agent 工程师有实用价值，但对更广泛的 agent 工程社区影响较窄。

rss · Simon Willison · Nov 26, 06:08

**「为什么重要」** 当 agent 运行在磁盘空间不足一半的小型实例上时，传统 SQLite 备份方法会因空间限制失效，sqlite3\_rsync 提供了不依赖完整本地副本的替代路径。

**「可关注」** 可关注：若 agent 使用 SQLite 存储状态或评估数据，且运行环境磁盘空间有限，sqlite3\_rsync 提供了无需完整本地副本的快照复制方案。

**Tags**: `#eval`, `#memory`, `#tooling`

---

<a id="item-agent-engineer-6"></a>
### [Play2Evolve 游戏框架论文预览发布](https://huggingface.co/papers/2611.33457) ⭐️ 6.0/10

2026 年11 月26 日Hugging Face Daily Papers发布论文预览，介绍面向游戏开发的递归3 阶段agent框架Play2Evolve。该框架分为初始化、优化、进化三个阶段，通过agent playtesting获取的playfulness反馈，指导修复功能问题、优化视觉资产、拓展玩法内容，目标是让agent生成的游戏超越基础可运行性。该研究目前仅覆盖游戏开发窄场景，未公开性能基准与更广泛适用性证据，对做agentic coding、agent编排、eval设计的工程师有参考价值。

rss · Hugging Face Daily Papers · Nov 26, 00:00

**「为什么重要」** 该研究提出的“用agent自测结果作为反馈驱动迭代”的思路，可迁移至通用agentic coding工作流与eval设计场景；但目前仅针对游戏开发窄场景，无公开性能基准与更广泛适用性验证，实际落地价值尚未证实。

**「可关注」** 可关注：agent自测反馈作为迭代优化信号，在特定场景下可突破“仅保证产物可运行”的agent输出上限。

**Tags**: `#coding-agent`, `#orchestration`, `#eval`

---

<a id="item-agent-engineer-7"></a>
### [AIRIS 社会具身智能基准发布](https://huggingface.co/papers/2611.34347) ⭐️ 5.5/10

AIRIS 是一个于 2026-11-26 发布的因果流式基准，用于评估自我中心视频中的社会具身智能。它包含 8,000 个专家问题，基于 357 个视频片段，覆盖 11 个上下文类别和 36 个能力维度，将智能建模为 Attention-Intention-Reaction-Interaction \(A-I-R-I\) 时间链。模型在每个查询点仅接收当时可用的观察前缀，但决策感知指标的具体计算方式在摘要中被截断。该工作与主流 agent 工程的相关性目前有限，主要面向具身社会交互 agent 的细分领域。

rss · Hugging Face Daily Papers · Nov 26, 00:00

**「为什么重要」** 现有社会智能基准通常使用完整视频或评估孤立能力，AIRIS 的流式因果设置能更准确暴露在线决策失败点。但该基准的实际采用度与工程可用性尚不明确，目前仅凭摘要无法评估其对现有 agent 工作流的实际影响。

**「可关注」** 可关注：流式因果评估要求模型在信息不完整时做出社会决策，这对延迟约束下的置信度校准提出新挑战，但当前缺乏实现细节与性能基线，难以直接迁移到现有系统。

**Tags**: `#eval`

---