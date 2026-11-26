---
layout: default
title: "Horizon Summary: 2026-11-27 (ZH)"
date: 2026-11-27
lang: zh
---

> 从 200 条内容中筛选出 10 条重要资讯。

<nav id="ah-toc" class="ah-toc" aria-label="目录"><span class="ah-toc-title">目录</span><ul><li><a href="#sec-harness-arch"><span class="ah-toc-name">Harness 架构</span><span class="ah-toc-count">3条</span></a></li><li><a href="#sec-agent-engineer"><span class="ah-toc-name">Agent 工程师日报</span><span class="ah-toc-count">7条</span></a></li></ul></nav>

---

**[Harness 架构](#sec-harness-arch)**
1. [E2B @e2b/acp 0.1.0 发布](#item-harness-arch-1) ⭐️ 7.8/10
2. [Instructor v1.18.0 发布](#item-harness-arch-2) ⭐️ 6.8/10
3. [browser-use 1.0.9 发布](#item-harness-arch-3) ⭐️ 5.5/10

**[Agent 工程师日报](#sec-agent-engineer)**
1. [Nemotron 3.5 Parse 开源优化](#item-agent-engineer-1) ⭐️ 7.8/10
2. [Hugging Face 开源多智能体 swarm 训练教程](#item-agent-engineer-2) ⭐️ 7.8/10
3. [llama.cpp AMD 基准看板上线](#item-agent-engineer-3) ⭐️ 6.3/10
4. [Google 强制 Workspace MCP 使用引争议](#item-agent-engineer-4) ⭐️ 6.0/10
5. [sqlite3\_rsync 轻量快照同步](#item-agent-engineer-5) ⭐️ 6.0/10
6. [Play2Evolve 递归框架优化游戏生成](#item-agent-engineer-6) ⭐️ 6.0/10
7. [AIRIS 社会具身智能基准发布](#item-agent-engineer-7) ⭐️ 5.5/10

---

## Harness 架构
{: #sec-harness-arch .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-harness-arch" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-harness-arch-1"></a>
### [E2B @e2b/acp 0.1.0 发布](https://github.com/e2b-dev/E2B/releases/tag/%40e2b/acp%400.1.0) ⭐️ 7.8/10

E2B 发布 \`@e2b/acp\` 0.1.0，首次支持在 E2B sandbox 内运行 ACP 兼容 agent。该包通过 \`new ACPAgent\(sandbox, command, client\)\` 与 \`await agent.start\(\)\` 启动 agent，基于 stdin/stdout 通信并连接 ACP client。客户端文件系统与终端能力被显式关闭，agent 请求这些能力时直接拒绝，强制其使用 sandbox 原生工具执行文件操作和命令。依赖同步更新至 \`e2b@2.65.0\`。

github · github-actions\[bot\] · 11月26日 12:35

**「设计要点」** 运行时通过 stdin/stdout 与 agent 进程通信，能力层在 client 侧禁用文件系统和终端能力，由 sandbox 原生工具接管文件操作与命令执行，形成能力边界隔离。

**「改了什么」** 新增 \`@e2b/acp\` 包，支持 Goose、OpenCode、Claude Code（通过 ACP adapter）等 ACP 兼容 agent 在 E2B sandbox 中运行。客户端文件系统和终端能力默认关闭并拒绝请求，强制 agent 使用 sandbox 原生工具。

**「评论」** 无社区评论。

**标签**: `#sandbox`, `#tools`, `#runtime`, `#permissions`

---

<a id="item-harness-arch-2"></a>
### [Instructor v1.18.0 发布](https://github.com/567-labs/instructor/releases/tag/v1.18.0) ⭐️ 6.8/10

这是结构化 LLM 输出库 Instructor 的官方 v1.18.0 版本发布，该库是 agent harness 生态的常用依赖。本次更新包含缓存键冲突修复、运行时与 provider 职责分离的核心重构，以及覆盖 Bedrock、OpenAI、Anthropic、Gemini 等多 provider 的兼容性、流式传输、批处理、安全相关修复，同时新增 typed Jev 决策模型与可复现离线性能基线。

github · jxnl · 11月26日 21:02

**「设计要点」** 本次重构将 token 预算策略、重试执行逻辑、缓存响应序列化等运行时能力与 provider 实现解耦，各 provider 模块独立负责自身 SDK 构造、请求配置策略与兼容性适配；安全层面默认关闭原始响应日志、忽略磁盘缓存，减少敏感信息暴露面。

**「改了什么」** 相对上一版本，修复了缓存键映射冲突、流式传输 Unicode 控制字符丢失、多 provider 工具调用与批处理结果保留等问题；重构核心模块与 provider 的职责边界，新增 typed Jev 决策模型，补充可复现离线性能基线，同时收紧请求日志与依赖提交的安全策略。

**标签**: `#cache`, `#runtime`, `#providers`

---

<a id="item-harness-arch-3"></a>
### [browser-use 1.0.9 发布](https://github.com/browser-use/browser-use/releases/tag/1.0.9) ⭐️ 5.5/10

browser-use 1.0.9 发布云浏览器 IP 轮换与 Claude 缓存修复。新增 rotate\_proxy 接口，在页面因 IP 被拦截时切换出口 IP，标签页、cookie 与登录状态保留，每个站点最多触发一次；云报告无新出口 IP 时接口明确失败。针对 .ru、.de、.co.uk、.kr 等国家域名可指定对应国家出口，在 11 个常见拦截站点上通过率从 48% 提升至 62%。同步修复 Claude prompt caching 在 OpenRouter、Bedrock 及 ChatOpenAI 路由上的失效问题，消除全量 prompt 重复计费。

github · gregpr07 · 11月26日 22:45

**「设计要点」** 云浏览器通过 browser-use.com 主机上的 CDP 连接识别，IP 轮换走浏览器自有连接，API key 仅作后备。Claude 缓存修复覆盖三层 provider 路由，但 Bedrock 仅经单测验证未做实机测试。

**「改了什么」** 新增 rotate\_proxy 接口支持云浏览器出口 IP 轮换，拦截时自动触发，无可用出口时明确失败。修复 Claude prompt caching 在 OpenRouter、Bedrock 及 ChatOpenAI 路由上的缓存失效问题。

**「评论」** 无社区评论。

**标签**: `#sandbox`, `#tools`, `#runtime`, `#prefix-cache`

---

## Agent 工程师日报
{: #sec-agent-engineer .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-agent-engineer" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-agent-engineer-1"></a>
### [Nemotron 3.5 Parse 开源优化](https://huggingface.co/blog/nvidia/building-on-nemotron-35-parse-open-data-fine-tunin) ⭐️ 7.8/10

2026 年 11 月 26 日 NVIDIA 与 Hugging Face 联合发布 Nemotron 3.5 Parse 文档模型的开源配套资源，包括 3 份合成训练数据集、微调指南、DFlash2 推测解码优化方案，以及 SFT+RLVR 训练流程说明，面向 RAG 与 agent 系统的文档处理场景。关键细节：3 份数据集共约 1890 万样本，分别为 Synthetic Charts V1（998 万）、Synthetic Tables V1（100 万）、OCR Synthetic Multilingual v2（790 万），均包含图像、标注、生成文档与训练格式；架构上 Parse 3.5 采用 NaViT 动态矩形输入、压缩视觉 token 作为因果前缀、GQA-8 注意力降低解码器缓存占用；DFlash2 在单张 H200 BF16 环境下，并发 1 时吞吐较 Parse 3.5 禁用推测解码提升 7.62 倍，并发 512 时提升 1.52 倍，32-token 配置下平均接受 14 个草稿 token；SFT+RLVR 流程可将循环输出页数从 126 降至 29，整体评分从 66.24 提升至 71.38。这些资源可供工程师直接用于定制文档解析能力。

rss · Hugging Face Blog · 11月26日 05:05

**「为什么重要」** 这些资源首次公开了 Nemotron 3.5 Parse 的可复现训练与优化全链路，降低了 RAG 和 agent 系统集成高精度文档解析能力的门槛；具体性能收益会随部署硬件、文档类型变化，需结合实际场景验证。

**「可关注」** 可关注：DFlash2 推测解码在低并发场景吞吐提升更显著，高并发场景可结合多轮重处理策略平衡速度与提取精度。

**标签**: `#coding-agent`, `#harness`, `#memory`

---

<a id="item-agent-engineer-2"></a>
### [Hugging Face 开源多智能体 swarm 训练教程](https://huggingface.co/blog/training-swarms) ⭐️ 7.8/10

2026 年 11 月 26 日，Hugging Face 官方博客发布多智能体 swarm 训练系列技术文章第一部分，提供可在 Hugging Face Jobs 上运行的复现示例，指导开发者构建、训练、评估小模型驱动的多智能体系统。首个示例采用 4 个共享 Qwen3-0.6B 策略的智能体，完成信息共享排序任务，单次运行约 5 小时、占用 2 张 H200、成本约 50 美元，采用集中训练分散执行模式，团队共享奖励、单个智能体有独立上下文和私有输入。当前示例仅验证小团队基础通信的可行性，尚未开展与单智能体同预算的性能对比，通信是否真的提升系统效能而非仅增加算力消耗仍是系列待验证的核心问题。

rss · Hugging Face Blog · 11月26日 00:00

**「为什么重要」** 该系列是官方发布的首个面向小模型、低成本多智能体 swarm 的可复现实践指南，填补了此前缺少落地级训练参考的空白。系列明确将“多智能体通信是否带来实际性能增益而非仅增加算力消耗”作为核心验证问题，为从业者提供了可对照的基准实验框架。

**「可关注」** 可关注：该系列采用共享单个小模型策略、集中训练分散执行的模式降低多智能体训练成本，当前首示例仅验证基础通信可行性，同预算下的性能对比结果需等待后续文章验证。

**标签**: `#eval`, `#orchestration`, `#multi-agent-system`, `#training`

---

<a id="item-agent-engineer-3"></a>
### [llama.cpp AMD 基准看板上线](https://huggingface.co/blog/ggml-org/llamacpp-amd-bench) ⭐️ 6.3/10

2026 年 11 月 26 日，Hugging Face 发布 llama.cpp 针对 AMD Ryzen 与 Radeon 硬件的公开基准测试看板，支持按硬件、模型、构建版本对比不同量化的推理性能。当前支持的硬件为 Radeon 8060S（gfx1151）与 Radeon AI Pro R9700S（gfx1201），核心指标为 PP512（512 输入 token 无生成吞吐）与 TG128（128 生成 token 吞吐），均以 tokens per second 为计量单位，同时提供构建历史、上下文扩展两个分析标签页。基准测试使用 llama-bench 工具，开启/关闭 Flash Attention，每个配置重复 10 次取均值，模型集当前覆盖 Inkling 2 Mini、Qwen、Gemma、gpt-oss、LFM 等 dense 与 mixture-of-experts 架构模型，支持 Q4\_K\_M、Q8\_0、BF16、F16 等量化格式。基准流程与原始结果完全公开，面向 AMD 平台本地推理开发者开放，数据存储于 Hugging Face 公共存储桶，支持复现与自定义分析。

rss · Hugging Face Blog · 11月26日 11:37

**「为什么重要」** 已发生的变化是填补了 AMD 平台 llama.cpp 本地推理性能的公开可对比基准工具空白，开发者无需自行搭建测试流程即可跟踪不同量化、构建版本的性能变化。尚未证实的影响是当前仅支持两款 AMD 硬件与有限模型集，后续覆盖范围扩展情况暂未明确。

**「可关注」** 可关注：公开基准数据以 .jsonl 格式存储在 Hugging Face 公共存储桶，路径按构建、硬件、模型、量化分层，可直接拉取做自定义对比或复现本地测试。

**标签**: `#eval`, `#observability`, `#harness`

---

<a id="item-agent-engineer-4"></a>
### [Google 强制 Workspace MCP 使用引争议](https://techstackups.com/articles/google-workspace-ai-agents-mcp/) ⭐️ 6.0/10

2026 年 11 月 26 日二手科技媒体报道称，谷歌要求 AI agent 必须使用其官方 Workspace MCP 服务器，其中 Gmail MCP 服务器不支持发送邮件功能。该信息目前无谷歌官方直接公告佐证，仅来自二手报道与 Hacker News 社区讨论，影响使用谷歌 Workspace 服务的 AI agent 开发者及终端用户。

hackernews · ritzaco · 11月26日 09:44 · [社区讨论](https://news.ycombinator.com/item?id=50653477)

**「为什么重要」** 若该限制落地，将直接改变 AI agent 接入 Workspace 服务的工具链设计逻辑，同时暴露 MCP 生态中厂商通过权限限制实现商业绑定的潜在风险。目前限制的真实动机尚未得到谷歌官方确认，社区普遍认为其更偏向商业决策而非安全考量。

**「可关注」** 可关注：MCP 协议已内置 elicitation 原语支持工具调用前的用户确认，厂商以安全为由限制工具权限时需额外验证其真实动机。

**「评论」** 社区普遍认为该限制是商业决策而非安全措施，同时存在两类实际担忧：一是厂商锁定与用量计费成本上升，二是限制可能迫使开发者采用浏览器操作等低效绕行方案，也有用户开始寻求谷歌 Workspace 的替代服务。

**标签**: `#mcp`, `#permissions`, `#orchestration`

---

<a id="item-agent-engineer-5"></a>
### [sqlite3\_rsync 轻量快照同步](https://simonwillison.net/2026/Nov/26/sqlite3-rsync/) ⭐️ 6.0/10

SQLite 官方工具 sqlite3\_rsync 于 2024 年 10 月在 SQLite 3.47.0 中作为实验性功能发布，2025 年 5 月随 3.50.0 版本得到增强。2026 年 11 月 26 日 Simon Willison 的博客介绍了其核心特性：无需本地预留完整数据库副本的磁盘空间，即可通过 SSH 将 SQLite 快照复制到远程机器，也支持类似 rsync 的增量同步，仅传输差异页内容，仅当副本与源差异极大时带宽开销最多增加几个百分点。该工具对使用 SQLite 存储 Agent 状态、记忆或评估数据的工程师有实用价值。

rss · Simon Willison · 11月26日 06:08

**「为什么重要」** 该工具解决了小磁盘环境下 SQLite 快照备份的空间瓶颈，是依赖 SQLite 做存储的 Agent 工具链的可选备份方案；目前暂无公开数据证明其在 Agent 场景的落地效果，整体影响范围相对较窄。

**「可关注」** 可关注：使用 SQLite 作为 Agent 状态、评估存储时，sqlite3\_rsync 可替代需要完整本地副本的备份 API 或 VACUUM INTO，解决小实例磁盘空间不足的备份问题。

**标签**: `#eval`, `#memory`, `#tooling`

---

<a id="item-agent-engineer-6"></a>
### [Play2Evolve 递归框架优化游戏生成](https://huggingface.co/papers/2611.33457) ⭐️ 6.0/10

2026 年 11 月 26 日，Hugging Face Daily Papers 预览了一篇研究论文，提出 Play2Evolve 递归 3 阶段智能体框架（Initialization、Refinement、Evolution），用于从自然语言描述生成游戏。该框架让智能体通过试玩自身生成的游戏，将 playfulness 作为反馈，诊断功能、视觉呈现和游戏玩法问题，并据此迭代改进。当前材料仅提供论文摘要片段，未包含性能基准、对比基线或更广泛适用性的证据，且社区暂无评论。

rss · Hugging Face Daily Papers · 11月26日 00:00

**「为什么重要」** 该工作把试玩反馈引入智能体迭代循环，为 coding agent 的自我改进和 eval 设计提供了可迁移的思路，但仅针对游戏开发场景，尚未证实通用性。

**「可关注」** 可关注：递归 3 阶段框架（初始化-细化-演化）结合智能体自反馈的机制，可迁移到其他需要多轮迭代优化的 coding agent 工作流，但需注意当前证据仅限游戏领域。

**标签**: `#coding-agent`, `#orchestration`, `#eval`

---

<a id="item-agent-engineer-7"></a>
### [AIRIS 社会具身智能基准发布](https://huggingface.co/papers/2611.34347) ⭐️ 5.5/10

2026 年 11 月 26 日 Hugging Face Daily Papers 发布社会具身智能评估基准 AIRIS，该基准为因果流式设计，将社会具身智能建模为时间锚定的注意、意图、反应、交互（A-I-R-I）链，包含 8000 个专家 curated 问题，覆盖 357 个第一人称视频剪辑、11 个上下文类别与 36 个能力维度。查询时模型仅能获得当前时间点可用的观测前缀，配套决策感知指标。当前公开内容仅为截断摘要，无技术实现细节、性能对比数据，对主流编码智能体与 harness 工程工作的相关性有限，主要面向具身社交交互智能体方向的研究者。

rss · Hugging Face Daily Papers · 11月26日 00:00

**「为什么重要」** 它首次将社会具身智能评估锚定在流式第一人称视频的在线决策场景，但当前公开信息不足，对多数智能体工程师的实际参考价值尚未明确。

**「可关注」** 可关注：现有社会具身智能评估多基于完整视频或单能力维度，AIRIS 的因果流式评估范式可对照参考在线决策场景的基准设计思路。

**标签**: `#eval`

---