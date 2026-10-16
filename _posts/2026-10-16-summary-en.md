---
layout: default
title: "Horizon Summary: 2026-10-16 (EN)"
date: 2026-10-16
lang: en
---

> From 208 items, 11 important content pieces were selected

---

**Agent Harness Architecture**
1. [openai-agents-python v0.24.0 发布](#item-harness-arch-1) ⭐️ 7.8/10
2. [agent-framework 1.22.0](#item-harness-arch-2) ⭐️ 7.8/10
3. [Codex rust-v0.163.0 发布](#item-harness-arch-3) ⭐️ 6.8/10

**AI Agent Engineer**
1. [IBM Granite Switch 4.1 发布](#item-agent-engineer-1) ⭐️ 7.8/10
2. [NVIDIA Nemotron 3.5 Bolt 74B-A9B 发布](#item-agent-engineer-2) ⭐️ 6.0/10
3. [affinity 4卡R9700跑通DeepSeek-V4-Flash](#item-agent-engineer-3) ⭐️ 6.0/10
4. [Muse Spark Open 开源模型发布](#item-agent-engineer-4) ⭐️ 5.5/10

**AI Daily**
1. [OpenAI Rosalind 学术计划](#item-ai-daily-1) ⭐️ 7.8/10
2. [OpenAI 教育产品支持巴西葡语](#item-ai-daily-2) ⭐️ 6.3/10
3. [GitHub：开发者接口将演进为环境智能](#item-ai-daily-3) ⭐️ 5.8/10

**AI Deals**
1. [OpenCode 免费提供 DeepSeek V4.1 Flash](#item-ai-deals-1) ⭐️ 7.0/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [openai-agents-python v0.24.0 发布](https://github.com/openai/openai-agents-python/releases/tag/v0.24.0) ⭐️ 7.8/10

openai-agents-python v0.24.0 正式发布。本次更新在工具层新增 MCP 注解透出与 run-wide 工具异常格式化能力；修复了会话写入批处理、待审批状态下自动压缩延迟、Redis 历史替换原子性等问题。依赖侧同步升级 fastapi 0.141.1、grpcio 1.84.0、redis 8.1.0、temporalio 1.34.0 等版本。

github · openai-sdks\[bot\] · Oct 15, 02:20

**「设计要点」** SDK 在工具转换层新增 MCP 注解透出，支持 run-wide 异常格式化；记忆层将 Redis 压缩历史替换改为原子操作，并在待审批场景下延迟自动压缩。

**「改了什么」** 新增 MCP 注解透出与 run-wide 工具异常格式化；修复会话写入超 API 限制批处理、待审批时自动压缩提前触发、Redis 历史替换非原子、Runner 追踪 opt-out 未生效、未可序列化 dataclass run context 写入、沙箱脱敏丢失调用者异常等问题；依赖升级。

**Tags**: `#mcp`, `#tools`, `#runtime`, `#memory`, `#permissions`

---

<a id="item-harness-arch-2"></a>
### [agent-framework 1.22.0](https://github.com/microsoft/agent-framework/releases/tag/python-1.22.0) ⭐️ 7.8/10

Microsoft agent-framework Python 1.22.0 releases with core Python 3.15 runtime support and a breaking persisted-state compatibility change for serialized Agent Framework Content and streamed response-update records. The state change affects chat histories, session stores, and workflow checkpoints that embed these records, while plain session metadata and checkpoints without such content remain unaffected. The 1.22 runtime maintains backward read compatibility with earlier record formats, but pre-1.22 runtimes cannot parse new records containing \`hosted\` or \`merge\_mode\` fields.

github · eavanvalkenburg · Oct 15, 09:53

**「设计要点」** The core framework and root \`agent-framework\` package target Python 3.15, while optional extras and features remain gated by upstream dependency constraints documented per package. Persisted state containing serialized Content or streamed response updates evolves to include \`hosted\` and \`merge\_mode\` fields, creating an asymmetric compatibility window where 1.22 reads legacy records but older runtimes reject new ones, necessitating store isolation or migration during version transitions.

**「改了什么」** Core runtime gains Python 3.15 support with per-package limitation documentation, while a breaking persisted-state schema change adds \`hosted\` and \`merge\_mode\` fields to serialized Content and streamed response-update records, requiring store isolation or migration during rolling deployments. Additional breaking changes consolidate content identity and stream-merge semantics across providers, enforce AG-UI fail-closed trust boundaries with thread-bound continuations, isolate tool-approval state from client snapshots, bound HTTP response bodies and decoding stages, and refresh development UI dependencies, alongside provider-specific additions for Cosmos, OAuth, Ollama/OpenAI service URLs, and Oracle connection pools.

**Tags**: `#runtime`, `#memory`

---

<a id="item-harness-arch-3"></a>
### [Codex rust-v0.163.0 发布](https://github.com/openai/codex/releases/tag/rust-v0.163.0) ⭐️ 6.8/10

OpenAI Codex 发布 rust-v0.163.0。本次版本新增并行只读工具执行、响应中断与转向，以及 \`/config\`、\`/keymap\`、\`/daemon\` 等界面功能。技术层面，独立只读工具（skill、memory、conversation-history）现可并行调用，中断响应同时停止 Code Mode 单元及其嵌套工具调用。Daybreak 模型对符合条件账户默认启用，\`codex exec\` 也可通过 OpenAI API key 选择。

github · github-actions\[bot\] · Oct 15, 21:30

**「设计要点」** 工具执行层新增独立只读工具并行调度，中断机制会级联取消 Code Mode 嵌套调用。网络代理层在 DNS 查询前强制权限检查并拒绝重复 Host 头，权限边界从执行时扩展到连接建立阶段。

**「改了什么」** 相对 rust-v0.162.0，本版本新增并行只读工具执行、默认启用的响应中断与 Code Mode 中断，以及 \`/config\` 搜索、\`/keymap\` 快捷键配置和 \`/daemon\` 后台服务重启。运行时弃用 bundled patched \`zsh\`，改用标准 shell executor，Linux 与 macOS 发布包通过剥离符号减小体积。

**Tags**: `#runtime`, `#tools`, `#memory`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [IBM Granite Switch 4.1 发布](https://huggingface.co/blog/ibm-granite/granite-switch-4-1) ⭐️ 7.8/10

On October 15, 2026, IBM released the Granite Switch 4.1 model series, available in 8B and 30B parameter versions. The model combines a base model, a general-purpose Decision aLoRA, a safety-focused Guardian aLoRA that on average outperforms Jev 1.13, Microsoft-Decision-1, GPT-Luna-Decisions, and Clef-Flash on safety-related decision tasks, and the Granite-Speech-5.0-Turbo-CTC speech encoder \(the fastest ASR model on the OpenASR Leaderboard\) via Activated LoRAs, delivering chat, decision-making, and speech transcription capabilities. Its VRAM footprint is roughly equivalent to that of the base model alone, enabling multi-task inference on a single GPU. Task switching relies on KV cache reuse and vLLM optimizations for low-rank adapter inference, delivering fast switching speeds for use cases requiring multi-capability single endpoints, such as agent and inference harness deployments. IBM also plans to release an Adapter SDK to support user-built custom adapters for extending model capabilities.

rss · Hugging Face Blog · Oct 15, 20:34

**「为什么重要」** The architecture validates the feasibility of composing multiple capabilities into a single model, with its low VRAM overhead and KV cache reuse scheme directly applicable to multi-task agent inference harness design. The planned Adapter SDK and Granite Libraries adapter ecosystem also provide a reference path for building custom multi-capability model compositions.

**「可关注」** Watch for: The KV cache reuse mechanism of Activated LoRAs, and vLLM&\#x27;s optimizations for low-rank adapter inference, which together enable low-latency, low-VRAM multi-task switching.

**Tags**: `#coding-agent`, `#orchestration`, `#eval`, `#harness`

---

<a id="item-agent-engineer-2"></a>
### [NVIDIA Nemotron 3.5 Bolt 74B-A9B 发布](https://www.reddit.com/r/LocalLLaMA/comments/1x6o31q/nvidianvidianemotron35bolt74ba9b24gb_hugging_face/) ⭐️ 6.0/10

2026年10月15日，Reddit社区转发NVIDIA官方在Hugging Face上线的Nemotron 3.5 Bolt 74B-A9B 24GB视觉语言模型，该模型专为本地agent任务优化，训练数据截止2026年5月。核心规格为总参数74B、激活参数9B，采用Mamba-2-Transformer混合LatentMoE架构，原生2-bit量化后可适配24GB显存，支持最高256K上下文、文本/图像/视频多模态输入，可在NVIDIA Ampere、Hopper、Blackwell架构GPU上通过vLLM部署，配套LiLiCorr草稿模型的推测解码支持，可用于商业或非商业场景。当前未公开具体性能基准与agent任务评测结果，需结合官方模型卡进一步评估实际实用性。

reddit · r/LocalLLaMA · /u/jacek2023 · Oct 15, 15:04

**「为什么重要」** 该模型原生2-bit量化后仅需24GB显存即可运行，大幅降低了本地部署多模态agent的硬件门槛，同时支持256K长上下文，对需要本地运行agent任务的开发者有直接参考价值。

**「可关注」** 可关注：该模型采用Mamba-2-Transformer混合LatentMoE架构，原生2-bit量化适配24GB显存，配套vLLM部署方案与LiLiCorr推测解码支持，可降低本地多模态agent的部署硬件成本。

**Tags**: `#coding-agent`

---

<a id="item-agent-engineer-3"></a>
### [affinity 4卡R9700跑通DeepSeek-V4-Flash](https://www.reddit.com/r/LocalLLaMA/comments/1x70e5r/deepseekv4flash0731_on_4x_radeon_ai_pro_r9700/) ⭐️ 6.0/10

Reddit用户/u/brainchillzZ实测证实，affinity本地LLM推理框架此前因作者仅用2卡模拟4卡测试时出现无法解释的重复token异常，拒绝启动4卡AMD Radeon AI PRO R9700配置；使用affinity稳定性修复分支（neuromaniacMD/affinity v4-fixes）及预量化2.875bpw DeepSeek-V4-Flash-0731模型，该4卡配置可正常运行，greedy解码达约79 tok/s，采样temp 1.0时约63 tok/s，全部11008个专家常驻显存，无退化输出，跨卡一致性校验全部通过。该结果仅对使用该特定硬件、模型和affinity框架构建本地推理工具链的用户有直接参考价值。

reddit · r/LocalLLaMA · /u/brainchillzZ · Oct 15, 23:06

**「为什么重要」** 已确认此前4卡配置无法启动的根因是2卡模拟场景的bug，而非affinity框架本身不支持4卡AMD Radeon AI PRO R9700执行，为同环境用户提供了可复现的配置路径；该修复的普适性尚未验证，目前仅见此单点实测报告。

**「可关注」** 可关注：affinity的集合通信逻辑原本就支持N卡（已测3/4/8卡场景），此前4卡启动限制完全来自2卡模拟的重复token bug；4卡全量专家常驻显存时，需加--placement-strategy static参数规避默认热放置策略的报错。

**Tags**: `#harness`

---

<a id="item-agent-engineer-4"></a>
### [Muse Spark Open 开源模型发布](https://www.reddit.com/r/LocalLLaMA/comments/1x6r9pz/introducing_muse_spark_open_the_most_capable_us/) ⭐️ 5.5/10

2026年10月15日Reddit社区发布Meta旗下Muse Spark Open开源模型公告，面向编码与智能体任务设计。该模型总参数816B、激活参数42B，完成基于Meta Superintelligence Scaling Framework的安全后训练，支持1M tokens上下文窗口，覆盖文本、图像、视频、音频多模态；配套SGLang自定义Helion GPU内核，在NVIDIA、AMD GPU上实现1.03–3.95倍内核加速，AMD MI350端端到端性能提升3%，支持SGLang、vLLM、TensorRT-LLM、Apple MLX、llama.cpp等主流推理引擎，可运行于双Apple M5 Ultra Mac Studio。权重已在Hugging Face、Amazon SageMaker AI、Google Cloud Model Garden、Microsoft Foundry Models等平台开放下载，同时可通过Baseten、Fireworks AI、Groq等平台调用API，采用带有限商业条款的Muse Model License，多数开发者可免费使用。当前信息仅来自Reddit社区帖子，无官方一手来源验证，内容存在截断，相关技术声明真实性待确认。

reddit · r/LocalLLaMA · /u/AIatMeta · Oct 15, 17:03

**「为什么重要」** 若该模型技术声明属实，其针对编码与智能体任务的优化、超长上下文与多硬件适配特性，将为相关开发者提供新的开源选择；但当前无官方来源验证性能声明，实际效果待权重公开后检验。

**「可关注」** 可关注：该模型宣称适配Apple M5 Ultra及主流推理框架，若权重公开后可验证其在本地编码、智能体任务中的实际性能与硬件占用情况。

**Tags**: `#coding-agent`, `#inference`, `#model-optimization`, `#multimodal`

---

## AI Daily

<a id="item-ai-daily-1"></a>
### [OpenAI Rosalind 学术计划](https://openai.com/index/introducing-the-rosalind-academic-plan) ⭐️ 7.8/10

OpenAI 发布 Rosalind Academic Plan，为符合条件的学术实验室提供 GPT-Rosalind 及相关工具的赞助访问权限。该计划旨在支持生命科学研究。目前未公开具体配额、申请条件及覆盖地区等细节。

rss · OpenAI Blog · Oct 15, 19:00

**Tags**: `#model`, `#lab`, `#industry`, `#policy`

---

<a id="item-ai-daily-2"></a>
### [OpenAI 教育产品支持巴西葡语](https://openai.com/index/teaching-students-to-think-and-learn-through-questions) ⭐️ 6.3/10

OpenAI 发布博客文章庆祝教师节，宣布 AI for Educators 产品新增巴西葡萄牙语支持，并介绍 Study Mode 功能。Study Mode 可以帮助教师支持学生进行主动的、循序渐进的学习。此次更新属于产品迭代，并非重大模型发布或政策变更，广泛影响有限。

rss · OpenAI Blog · Oct 15, 13:00

**「为什么重要」** 该更新显示 OpenAI 教育产品线的本地化动作，但属于有限范围的产品迭代。

**「可关注」** 可关注：OpenAI 教育产品线的本地化与功能迭代节奏。

**Tags**: `#product`, `#industry`, `#lab`

---

<a id="item-ai-daily-3"></a>
### [GitHub：开发者接口将演进为环境智能](https://github.blog/news-insights/company-news/the-next-developer-interface-is-ambient-intelligence/) ⭐️ 5.8/10

GitHub官方博客发文称，AI、智能体、语音及物理控制正推动开发者接口从操作工具转向表达意图，助力开发者更专注于构建工作。

rss · GitHub Blog · Oct 15, 19:39

**「为什么重要」** 该文是GitHub作为主流开发者平台对工具演进方向的公开判断，可作为行业趋势的参考信号。

**「可关注」** 可关注：GitHub将环境智能视为开发者接口的演进方向，后续相关工具迭代可留意其落地路径。

**Tags**: `#industry`, `#AI`, `#agent`

---

## AI Deals

<a id="item-ai-deals-1"></a>
### [OpenCode 免费提供 DeepSeek V4.1 Flash](https://www.appinn.com/opencode-free-deepseek-v4-1-flash/) ⭐️ 7.0/10

OpenCode officially offers free access to the DeepSeek V4.1 Flash model. Users can switch to this model via the /model command after updating their OpenCode client. The model currently only supports a 200KB context window, and no expiration date for this offer is mentioned.

rss · 小众软件 · Oct 15, 09:48

**「为什么重要」** This offer has no stated expiration date, and the switch path is straightforward with no extra application required, making it suitable for users who need lightweight DeepSeek model access for simple tasks.

**「可关注」** 可关注：The DeepSeek V4.1 Flash model only supports a 200KB context window, making it suitable only for short-text processing scenarios, while users with long-context needs should opt for other models.

**Tags**: `#free-tier`, `#api`, `#limited-free`

---