---
layout: default
title: "Horizon Summary: 2026-10-16 (ZH)"
date: 2026-10-16
lang: zh
---

> 从 208 条内容中筛选出 11 条重要资讯。

<nav id="ah-toc" class="ah-toc" aria-label="目录"><span class="ah-toc-title">目录</span><ul><li><a href="#sec-harness-arch"><span class="ah-toc-name">Harness 架构</span><span class="ah-toc-count">3条</span></a></li><li><a href="#sec-agent-engineer"><span class="ah-toc-name">Agent 工程师日报</span><span class="ah-toc-count">4条</span></a></li><li><a href="#sec-ai-daily"><span class="ah-toc-name">AI 日报</span><span class="ah-toc-count">3条</span></a></li><li><a href="#sec-ai-deals"><span class="ah-toc-name">AI 羊毛</span><span class="ah-toc-count">1条</span></a></li></ul></nav>

---

**[Harness 架构](#sec-harness-arch)**
1. [openai-agents-sdk v0.24.0](#item-harness-arch-1) ⭐️ 7.8/10
2. [agent-framework python-1.22.0 发布](#item-harness-arch-2) ⭐️ 7.8/10
3. [Codex rust-v0.163.0 发布](#item-harness-arch-3) ⭐️ 6.8/10

**[Agent 工程师日报](#sec-agent-engineer)**
1. [Granite Switch 4.1 发布](#item-agent-engineer-1) ⭐️ 7.8/10
2. [Nemotron 3.5 Bolt 74B-A9B 发布](#item-agent-engineer-2) ⭐️ 6.0/10
3. [affinity 4 卡 R9700 跑通 DeepSeek-V4-Flash-0731](#item-agent-engineer-3) ⭐️ 6.0/10
4. [Muse Spark Open 开源发布](#item-agent-engineer-4) ⭐️ 5.5/10

**[AI 日报](#sec-ai-daily)**
1. [OpenAI 推出 Rosalind 学术计划](#item-ai-daily-1) ⭐️ 7.8/10
2. [OpenAI 上线 AI for Educators 葡语版及 Study Mode](#item-ai-daily-2) ⭐️ 6.3/10
3. [GitHub ：开发者接口趋向环境智能](#item-ai-daily-3) ⭐️ 5.8/10

**[AI 羊毛](#sec-ai-deals)**
1. [OpenCode 免费开放 DeepSeek V4.1 Flash](#item-ai-deals-1) ⭐️ 7.0/10

---

## Harness 架构
{: #sec-harness-arch .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-harness-arch" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-harness-arch-1"></a>
### [openai-agents-sdk v0.24.0](https://github.com/openai/openai-agents-python/releases/tag/v0.24.0) ⭐️ 7.8/10

OpenAI 官方 Python agent SDK 发布 v0.24.0。新增转换后工具暴露 MCP 注解、run-wide 工具异常格式化两项能力。修复会话写入未达批量阈值、待审批时自动压缩提前触发、Redis 压缩历史非原子替换、不可序列化 dataclass 运行上下文等问题，同步升级 fastapi、redis、temporalio 等依赖。

github · openai-sdks\[bot\] · 10月15日 02:20

**「设计要点」** 运行时批量提交会话写入以适配 API 限额，内存管理在待审批时延迟压缩，Redis 压缩历史采用原子替换。工具层暴露 MCP 注解，调用链保留异常所有权并遵守 Runner 跟踪选择退出。

**「改了什么」** 相对 v0.23.1，新增 MCP 注解暴露与 run-wide 工具异常格式化。修复会话写入未批量导致的 API 限流、待审批状态下自动压缩提前触发、Redis 压缩历史非原子替换、不可序列化 dataclass 运行上下文序列化失败、调用者跟踪未遵守 Runner 选择退出、沙盒编辑丢失调用者异常等问题。升级 fastapi 至 0.141.1、redis 至 8.1.0、temporalio 至 1.34.0 等依赖。

**标签**: `#mcp`, `#tools`, `#runtime`, `#memory`, `#permissions`

---

<a id="item-harness-arch-2"></a>
### [agent-framework python-1.22.0 发布](https://github.com/microsoft/agent-framework/releases/tag/python-1.22.0) ⭐️ 7.8/10

Microsoft agent-framework Python 1.22.0 正式发布，核心框架与根包新增 Python 3.15 运行时支持，但部分可选包与功能仍受上游依赖限制。本次发布引入持久化状态兼容性破坏变更：序列化 Content 与流式响应更新记录新增 \`hosted\` 与 \`merge\_mode\` 字段，导致聊天历史、会话存储、协议快照及包含这些记录的工作流检查点无法被 1.22 前运行时读取。多个适配器统一内容身份、托管执行、协议元数据、重放与流合并语义，AG-UI 进一步收紧请求信任边界与线程状态隔离。

github · eavanvalkenburg · 10月15日 09:53

**「设计要点」** 框架采用多包分层架构，核心 \`agent-framework\` 与各 provider/adapter 包（如 \`agent-framework-openai\`、\`agent-framework-ag-ui\`）独立发布但同步版本。持久化层通过序列化格式演进实现状态兼容性管理，流式响应与内容记录的结构化字段（\`hosted\`、\`merge\_mode\`）成为跨版本互操作的关键边界。

**「改了什么」** 新增 Cosmos memory provider 的 User-Agent token、Foundry 非流式 OAuth 同意请求暴露、Ollama/OpenAI chat client 可配置服务 URL、Oracle 连接池配置转发。修复 continuation token 跨转换保留、A2A 空附件支持、MCP 提示目录刷新、敏感遥测脱敏等多项核心问题，并统一内容身份与流合并语义。

**标签**: `#runtime`, `#memory`

---

<a id="item-harness-arch-3"></a>
### [Codex rust-v0.163.0 发布](https://github.com/openai/codex/releases/tag/rust-v0.163.0) ⭐️ 6.8/10

OpenAI Codex 发布 rust-v0.163.0 版本，新增并行只读工具执行、响应中断与即时转向、全局配置搜索、自定义快捷键、后台服务重启等核心能力，Daybreak 功能默认对符合条件账号启用，\`codex exec\` 支持通过 OpenAI API 密钥选择 Daybreak。版本同时修复网络代理权限校验、线程恢复、跨平台粘贴、命令输出处理等多项问题，优化了沙箱安全与发布包体积。

github · github-actions\[bot\] · 10月15日 21:30

**「设计要点」** 运行时默认开启并行只读工具执行，覆盖 skill、memory、会话历史查询场景；响应中断机制默认启用，可终止 Code Mode 单元格及嵌套工具调用。沙箱新增 bubblewrap、Seatbelt 后端做文件系统隔离与 syscall 过滤完整性校验，网络代理增加权限前置校验、拒绝重复 Host 头、阻止凭证别名绕过校验的逻辑。

**「改了什么」** 相对上一版本，新增并行只读工具执行、响应中断/转向、\`/config\` 全局搜索配置、\`/keymap\` 自定义快捷键、\`/daemon\` 重启后台服务能力，Daybreak 默认启用且 \`codex exec\` 支持选择。修复网络代理权限、线程权限恢复、跨平台粘贴、命令输出处理等多项问题，移除 bundled patched zsh，Linux 与 macOS 发布包通过剥离符号缩小体积。

**「评论」** 暂无社区评论可用。

**标签**: `#runtime`, `#tools`, `#memory`

---

## Agent 工程师日报
{: #sec-agent-engineer .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-agent-engineer" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-agent-engineer-1"></a>
### [Granite Switch 4.1 发布](https://huggingface.co/blog/ibm-granite/granite-switch-4-1) ⭐️ 7.8/10

2026 年 10 月 15 日 IBM 在 Hugging Face 博客发布 Granite Switch 4.1，推出 8B 与 30B 两个版本，通过 Activated LoRAs 搭配 KV 缓存复用，将聊天、决策（含通用 Decision aLoRA 与安全场景 Guardian aLoRA）、语音转录（Granite-Speech-5.0-Turbo-CTC，OpenASR 最快 ASR 模型）三类能力组合进单一模型，占用 VRAM 与基座模型基本一致，可单 GPU 运行多任务。Guardian aLoRA 在安全相关决策任务上平均优于 Jev 1.13、Microsoft-Decision-1 等竞品，搭载 4 个专用 aLoRA 的 30B 版本在真实 5 步 RAG 工作流测试中比 Jev-27B 完成速度更快。官方已上线 Speech-to-Decisions 演示空间实现单端点实时全流程处理，同时开放自定义组合 Granite Libraries 适配器的能力，后续将发布适配 Mellea 的 Adapter SDK，更多技术细节与性能数据将在数周内补充。

rss · Hugging Face Blog · 10月15日 20:34

**「为什么重要」** 它首次将聊天、决策、语音三类能力整合进单一开源模型，且多任务切换的 VRAM 开销与基座模型基本持平，同时公开了 Activated LoRAs+KV 缓存复用的实现路径，对设计多能力推理 harness 的工程师有直接参考价值。目前更多生产环境性能基准、稳定性数据尚未公开，实际效果待验证。

**「可关注」** 可关注：Activated LoRAs 的 KV 缓存复用机制可实现基座与多适配器的缓存共享，搭配 vLLM 低秩适配器推理优化，能在几乎不增加额外 VRAM 开销的前提下组合多类任务能力。

**标签**: `#coding-agent`, `#orchestration`, `#eval`, `#harness`

---

<a id="item-agent-engineer-2"></a>
### [Nemotron 3.5 Bolt 74B-A9B 发布](https://www.reddit.com/r/LocalLLaMA/comments/1x6o31q/nvidianvidianemotron35bolt74ba9b24gb_hugging_face/) ⭐️ 6.0/10

NVIDIA 发布专为本地 agent 任务优化的 Nemotron 3.5 Bolt 74B-A9B 24GB 视觉语言模型，已在 Hugging Face 上线，提供官方 GGUF 权重与 LiLiCorr 优化版本。该模型总参数 74B、激活参数 9B，采用 Mamba-2-Transformer 混合 LatentMoE 架构，原生 2-bit IQ2 量化后可适配 24GB 显存，支持最高 256K 上下文长度，输入支持文本、图像、视频，输出为文本，采用 OpenMDW-1.1 许可，可用于商业或非商业用途。模型训练周期为 2025 年 12 月至 2026 年 5 月，后训练数据截止 2026 年 5 月。官方还提供配套 vLLM 部署配方，支持通过 LiLiCorr drafter 实现 7 个 speculative token 的 speculative decoding，推理模式可通过 chat-template 控制。

reddit · r/LocalLLaMA · /u/jacek2023 · 10月15日 15:04

**「为什么重要」** 该模型原生 2-bit 量化后仅需 24GB 显存即可运行，降低了本地部署多模态 agent 的门槛，目前官方未公开 agent 任务实测性能与精度损失数据。

**「可关注」** 可关注：该模型提供原生 2-bit 量化权重与适配 NVIDIA Ampere、Hopper、Blackwell 架构的 vLLM 部署配方，可直接在 24GB 显存设备上部署多模态 agent 场景，后续可结合官方模型卡评估实际任务表现。

**标签**: `#coding-agent`

---

<a id="item-agent-engineer-3"></a>
### [affinity 4 卡 R9700 跑通 DeepSeek-V4-Flash-0731](https://www.reddit.com/r/LocalLLaMA/comments/1x70e5r/deepseekv4flash0731_on_4x_radeon_ai_pro_r9700/) ⭐️ 6.0/10

Reddit 用户/u/brainchillzZ 于 2026 年 10 月 15 日实测证实，此前因作者仅用 2 卡模拟 4 rank 出现重复 token 异常而拒绝启动 4 卡配置的 affinity 本地推理框架，在带稳定性修复的 v4-fixes 分支下可于 4 块 AMD Radeon AI PRO R9700 上正常运行 DeepSeek-V4-Flash-0731 模型。实测硬件为 Threadripper PRO 9955WX、128GB RAM，4 卡全接 CPU 通道且 pairwise 支持 P2P，搭配预构建的 2.875bpw 量化模型，无需下载 149GB 原始模型或进行 2.5 小时量化，启动需添加环境变量 AFF\_ALLOW\_NRANK=1 与参数--gpus 4，同时需添加--placement-strategy static 规避默认热放置策略因提示&quot;needs the registered host pool&quot;触发的报错。4 卡贪心解码速度约 79 tok/s，温度 1.0 时约 63 tok/s，开启思考的聊天场景约 90 tok/s，2 卡同场景仅 36 tok/s；4 卡配置下全部 11008 个专家常驻 VRAM，无需分配主机内存池，5 轮贪心/采样测试及聊天服务器测试无退化输出，框架自带的跨卡校验全部通过，模型加载总耗时约 1 分钟（其中 42 秒用于推送 96GB 专家参数至显存）；框架的 collective 通信实现原生支持 N rank，已在 3、4、8 卡场景下通过测试，此前 4 卡启动限制完全源于 2 卡模拟 4 rank 的异常，真实 4 卡硬件不会复现该问题。该结果仅对使用该特定硬件、模型与 affinity 框架构建本地推理或 agent 工具链的用户有直接参考价值。

reddit · r/LocalLLaMA · /u/brainchillzZ · 10月15日 23:06

**「为什么重要」** 此前 affinity 框架对 4 卡 R9700 的启动限制被怀疑是硬件或框架 collective 实现的固有问题，本次实测证实该限制源于 2 卡模拟 4 rank 的异常，并非真实 4 卡执行的缺陷，为同配置用户提供了可验证的运行方案；但其他硬件、模型或框架版本的兼容性尚未得到验证。

**「可关注」** 可关注：affinity 框架的 4 卡 R9700 启动限制是 2 卡模拟测试的假问题，对应稳定性修复分支（neuromaniacMD/affinity v4-fixes）已公开，同配置用户可按文中参数直接部署。

**标签**: `#harness`

---

<a id="item-agent-engineer-4"></a>
### [Muse Spark Open 开源发布](https://www.reddit.com/r/LocalLLaMA/comments/1x6r9pz/introducing_muse_spark_open_the_most_capable_us/) ⭐️ 5.5/10

2026 年 10 月 15 日 Reddit 社区发布 Meta 旗下 Muse Spark Open 开源模型相关信息，称其为迄今能力最强的美国开源权重模型，面向编码与智能体任务，总参数 816B、激活参数 42B，支持 1M tokens 上下文窗口，覆盖文本、图像、视频、音频多模态，额外开展基于 Meta 超级智能扩展框架的安全后训练与评估。配套自定义 Helion 内核可在 SGLang 中实现 NVIDIA、AMD GPU 1.03–3.95 倍内核加速，AMD MI350 端端到端推理提升 3%。模型兼容 SGLang、vLLM、TensorRT-LLM、MLX、llama.cpp 等主流推理引擎，适配 AMD、Apple、Intel、NVIDIA 硬件，优化支持双 Apple M5 Ultra Mac Studio 运行。权重可在 Hugging Face、Google Cloud Model Garden 等渠道下载，采用带有限商业条款的 Muse Model License，多数开发者可免费使用。以上信息来自 Reddit 社区帖子，无官方来源验证，内容存在截断。

reddit · r/LocalLLaMA · /u/AIatMeta · 10月15日 17:03

**「为什么重要」** 该模型提供了面向编码/智能体任务的高参数开源模型新选项，支持超长上下文、多模态及多硬件平台推理优化，还宣称开展了专项安全后训练；但其实际性能、安全后训练效果及商业条款适用范围尚未得到官方验证。

**「可关注」** 可关注：该模型宣称支持 1M tokens 上下文、多硬件平台推理优化及多引擎兼容，可评估其在实际编码/智能体任务中的延迟、吞吐与适配成本。

**标签**: `#coding-agent`, `#inference`, `#model-optimization`, `#multimodal`

---

## AI 日报
{: #sec-ai-daily .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-daily" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-daily-1"></a>
### [OpenAI 推出 Rosalind 学术计划](https://openai.com/index/introducing-the-rosalind-academic-plan) ⭐️ 7.8/10

OpenAI 正式发布 Rosalind 学术计划，为符合条件的高校生命科学研究实验室提供赞助访问权限。该计划覆盖 GPT-Rosalind 模型及相关配套工具，面向学术端生命科学研究场景开放申请。

rss · OpenAI Blog · 10月15日 19:00

**「为什么重要」** 该计划降低了高校实验室使用前沿 AI 生命科学工具的成本门槛，可支持学术端生命科学研究的效率提升。

**「可关注」** 可关注：符合条件的高校生命科学实验室可申请该计划获取 GPT-Rosalind 的赞助访问权限。

**标签**: `#model`, `#lab`, `#industry`, `#policy`

---

<a id="item-ai-daily-2"></a>
### [OpenAI 上线 AI for Educators 葡语版及 Study Mode](https://openai.com/index/teaching-students-to-think-and-learn-through-questions) ⭐️ 6.3/10

OpenAI 发布教师节主题博客，宣布 AI for Educators 完成巴西葡萄牙语本地化，同时上线 Study Mode 功能。该功能可辅助教师引导学生开展主动的、循序渐进的学习。

rss · OpenAI Blog · 10月15日 13:00

**「为什么重要」** 这是 OpenAI 教育场景工具的定向产品更新，为巴西地区教育从业者提供了本地化支持，同时补充了学习过程引导类功能，整体影响范围有限。

**「可关注」** 可关注：AI for Educators 巴西葡萄牙语版本已发布，Study Mode 功能同步上线。

**标签**: `#product`, `#industry`, `#lab`

---

<a id="item-ai-daily-3"></a>
### [GitHub ：开发者接口趋向环境智能](https://github.blog/news-insights/company-news/the-next-developer-interface-is-ambient-intelligence/) ⭐️ 5.8/10

GitHub 官方博客 2026 年 10 月 15 日发文指出，AI、智能体、语音及物理控制技术正推动软件开发的交互模式从操作工具转向表达意图，开发者接口将向环境智能方向演进，该方向旨在帮助开发者更专注于构建工作。

rss · GitHub Blog · 10月15日 19:39

**「为什么重要」** 这是主流开发者平台方对行业交互演进方向的公开趋势判断，可参考其视角下的技术发展预期。

**「可关注」** 可关注：开发者交互从工具操作向意图表达的演进方向，以及环境智能相关的技术落地进展。

**标签**: `#industry`, `#AI`, `#agent`

---

## AI 羊毛
{: #sec-ai-deals .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-deals" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-deals-1"></a>
### [OpenCode 免费开放 DeepSeek V4.1 Flash](https://www.appinn.com/opencode-free-deepseek-v4-1-flash/) ⭐️ 7.0/10

OpenCode 官方在 X 平台宣布免费开放 DeepSeek V4.1 Flash 模型，用户更新 OpenCode 程序后输入 /model 指令即可切换使用，该模型仅支持 200KB 上下文，未提及领取有效期。

rss · 小众软件 · 10月15日 09:48

**「可关注」** 可关注：更新 OpenCode 后通过输入 /model 指令切换至 DeepSeek V4.1 Flash，该模型仅支持 200KB 上下文。

**标签**: `#free-tier`, `#api`, `#limited-free`

---