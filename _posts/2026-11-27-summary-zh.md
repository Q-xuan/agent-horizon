---
layout: default
title: "Horizon Summary: 2026-11-27 (ZH)"
date: 2026-11-27
lang: zh
---

> 从 177 条内容中筛选出 6 条重要资讯。

<nav id="ah-toc" class="ah-toc" aria-label="目录"><span class="ah-toc-title">目录</span><ul><li><a href="#sec-harness-arch"><span class="ah-toc-name">Harness 架构</span><span class="ah-toc-count">3条</span></a></li><li><a href="#sec-agent-engineer"><span class="ah-toc-name">Agent 工程师日报</span><span class="ah-toc-count">3条</span></a></li></ul></nav>

---

**[Harness 架构](#sec-harness-arch)**
1. [pydantic-ai v2.76.0 发布](#item-harness-arch-1) ⭐️ 7.8/10
2. [E2B 发布 @e2b/acp 0.1.0](#item-harness-arch-2) ⭐️ 7.8/10
3. [Instructor v1.18.0 发布](#item-harness-arch-3) ⭐️ 5.8/10

**[Agent 工程师日报](#sec-agent-engineer)**
1. [llama.cpp AMD 基准面板上线](#item-agent-engineer-1) ⭐️ 6.8/10
2. [Coding Agents 视觉推理能力对比研究](#item-agent-engineer-2) ⭐️ 6.0/10
3. [OS-Omni v1 跨平台智能体基准发布](#item-agent-engineer-3) ⭐️ 5.5/10

---

## Harness 架构
{: #sec-harness-arch .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-harness-arch" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-harness-arch-1"></a>
### [pydantic-ai v2.76.0 发布](https://github.com/pydantic/pydantic-ai/releases/tag/v2.76.0) ⭐️ 7.8/10

pydantic-ai v2.76.0 发布。该版本为支持工具更新的实时模型引入中途会话工具更新能力，通过新增 \`UpdateTools\` 类型和 \`RealtimeModelProfile.supports\_tool\_updates\` 标志控制。同时调整 \`RealtimeInput\` 联合类型，导致穷尽性类型检查（如 \`assert\_never\`）失效，需显式处理 \`UpdateTools\`。此外，对 \`gemini-2.5-pro\` 和 \`gemini-2.5-flash\` 模型发出弃用警告，开启 \`filterwarnings = error\` 的代码将因此失败。

github · dsfaccini · 11月26日 23:49

**「设计要点」** 框架通过 \`RealtimeModelProfile\` 为不同模型声明能力边界，实时会话的工具更新仅在模型支持时下发。运行时尚有 \`result.conversation\` 与压缩能力（\`SummarizingCompaction\`、\`RelevanceCompaction\`）协作管理对话历史，UI 层通过 Pax 适配器与状态段（\`StatusLink\`）暴露交互。

**「改了什么」** 新增 \`UpdateTools\` 类型与 \`RealtimeModelProfile.supports\_tool\_updates\` 标志，支持实时会话中途更新工具；\`RealtimeInput\` 联合类型扩展导致穷尽性类型检查失效，需补全处理分支。\`gemini-2.5-pro\` 与 \`gemini-2.5-flash\` 触发 \`DeprecatedModelWarning\`，\`FileSystem.read\_file\` 的 \`offset\` 改为 1 起始，Pax 新增 \`/computer-use\` 桌面沙箱与双击选词交互。

**标签**: `#tools`, `#runtime`

---

<a id="item-harness-arch-2"></a>
### [E2B 发布 @e2b/acp 0.1.0](https://github.com/e2b-dev/E2B/releases/tag/%40e2b/acp%400.1.0) ⭐️ 7.8/10

E2B 发布 @e2b/acp 0.1.0，支持在 E2B 沙箱内运行符合 Agent Client Protocol 的 agent。新包提供 \`ACPAgent\` API，通过 \`new ACPAgent\(sandbox, command, client\)\` 构造实例，调用 \`await agent.start\(\)\` 后通过 stdin/stdout 启动 agent 并连接 ACP client。运行时强制禁用客户端文件系统与终端能力，拒绝 agent 对这两项能力的请求，确保 agent 仅使用沙箱原生工具执行文件编辑与命令运行。该版本同步将核心依赖 e2b 升级至 2.65.0。

github · github-actions\[bot\] · 11月26日 12:35

**「设计要点」** 运行时通过能力隔离实现安全边界：客户端侧文件系统与终端能力被关闭，agent 请求被显式拒绝，所有操作必须走沙箱原生工具层。通信采用 stdin/stdout 进程管道，避免网络端口暴露。

**「改了什么」** 新增 @e2b/acp 包，提供 ACPAgent API 以在 E2B 沙箱中托管 goose、OpenCode、Claude Code（通过 ACP adapter）等 ACP 兼容 agent。引入强制能力隔离机制，禁用客户端文件系统与终端访问。

**标签**: `#sandbox`, `#runtime`, `#permissions`, `#mcp`

---

<a id="item-harness-arch-3"></a>
### [Instructor v1.18.0 发布](https://github.com/567-labs/instructor/releases/tag/v1.18.0) ⭐️ 5.8/10

Instructor v1.18.0 正式发布，主要包含内部重构与缺陷修复。本次更新修复了缓存键映射冲突，将 v2 token 预算策略与重试执行分离，并重构了 Bedrock、GenAI 等提供者的 SDK 构造与请求配置策略。流式传输、批处理、多模态及安全方面也有多项修复，如保护请求日志、将原始响应日志改为 opt-in。该版本未引入重大 harness 能力或协议变更，对 agent 基础设施工程师的直接影响有限。

github · jxnl · 11月26日 21:02

**「设计要点」** v2 引擎将 token 预算策略与重试执行分离，提供者层各自独立管理 SDK 构造与请求配置策略，缓存层分离运行时响应序列化逻辑。这些重构细化了模块边界，但未改变对外接口或运行时模型。

**「改了什么」** 修复缓存键冲突与遗留响应兼容性；v2 分离 token 预算与重试逻辑，提供者层独立管理 SDK 与请求配置；流式传输增强 Unicode 与别名解析；安全修复默认禁用原始响应日志；新增 typed Jev decision models；同时修正批处理、多模态及并行工具调用的边界行为。

**标签**: `#cache`, `#runtime`

---

## Agent 工程师日报
{: #sec-agent-engineer .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-agent-engineer" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-agent-engineer-1"></a>
### [llama.cpp AMD 基准面板上线](https://huggingface.co/blog/ggml-org/llamacpp-amd-bench) ⭐️ 6.8/10

2026 年 11 月 26 日，Hugging Face 发布公开的 llama.cpp × AMD 基准测试面板，面向 AMD Ryzen 和 Radeon 硬件开发者提供本地推理性能对比与跟踪能力。面板支持按硬件、模型、llama.cpp 构建筛选，当前可选硬件为 Radeon 8060S（gfx1151）和 Radeon AI Pro R9700S（gfx1201），覆盖 Inkling 2 Mini、Qwen、Gemma 等模型，支持 Q4\_K\_M、Q8\_0、BF16 等量化格式；基准测试包含 PP512（512 输入 token 处理吞吐）和 TG128（128 token 生成吞吐）两项，均从上下文深度零开始测量，使用 llama-bench 工具运行，包含 Flash Attention 开启和关闭两种配置，每次配置重复 10 次，每周自动运行，完整结果公开存储在 Hugging Face 的 ggml-org/install.sh-benches-data 存储桶中，开发者可直接复用数据做自定义分析或本地复现。

rss · Hugging Face Blog · 11月26日 11:37

**「为什么重要」** 这是 Hugging Face 推出的首个面向 AMD Ryzen/Radeon 硬件的公开 llama.cpp 推理性能基准面板，解决了此前 AMD 平台本地推理性能数据分散、可复现性差的问题。目前仅覆盖两款 AMD 硬件，后续模型与硬件扩展范围尚未公布。

**「可关注」** 可关注面板公开的 ggml-org/install.sh-benches-data 存储桶数据，可直接用于复现基准或对比本地运行结果。

**标签**: `#eval`

---

<a id="item-agent-engineer-2"></a>
### [Coding Agents 视觉推理能力对比研究](https://huggingface.co/papers/2611.34813) ⭐️ 6.0/10

2026-11-27 Hugging Face Daily Papers 收录论文《Solve Vision with Code》，在相同输入、输出规范与评估器条件下，对比 coding agents 与视频生成模型的视觉推理能力。Coding agents 通过编写程序渲染答案视频，视频生成模型直接生成视频完成任务。论文引入 VBVR-Pro-Bench 评估基准，声称 coding agents 是更强的视觉推理器，但未披露具体性能数据或技术实现细节。

rss · Hugging Face Daily Papers · 11月27日 00:00

**「为什么重要」** 该研究首次在严格对照条件下测试符号化代码路径与原生视觉生成路径的可靠性差异。若结论可复现，将影响视觉推理任务的评估范式与 coding agent 应用边界。

**「可关注」** 可关注：VBVR-Pro-Bench 基准的评估维度设计，以及 coding agent 通过代码渲染视频完成视觉推理的具体工作流实现。

**标签**: `#coding-agent`, `#eval`

---

<a id="item-agent-engineer-3"></a>
### [OS-Omni v1 跨平台智能体基准发布](https://huggingface.co/papers/2611.34232) ⭐️ 5.5/10

2026 年 11 月 27 日 Hugging Face Daily Papers 发布研究简报，介绍跨平台计算机使用智能体基准 OS-Omni。v1 覆盖 Windows、Ubuntu、macOS、iOS、Android、Web 共 6 个平台，每平台 48 个任务，另含 12 组桌面与安卓手机配对的跨平台工作流。当前公开内容为二手摘要，缺少完整技术细节、性能对比及可复现设置说明，面向智能体评估领域的研究者与工程师。

rss · Hugging Face Daily Papers · 11月27日 00:00

**「为什么重要」** 它首次提供覆盖 6 类操作系统、支持长时程跨平台工作流的智能体评估框架，填补了现有基准仅覆盖单一环境的空白。当前未披露具体任务难度、对主流智能体的区分度等关键指标，实际评估价值待完整论文发布后验证。

**「可关注」** 可关注：现有智能体评估基准多隔离单一环境，OS-Omni 的跨平台长时程任务设计可能对现有 coding agent 的跨环境能力提出新测试维度。

**标签**: `#eval`, `#coding-agent`, `#orchestration`

---