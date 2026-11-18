---
layout: default
title: "Horizon Summary: 2026-11-18 (EN)"
date: 2026-11-18
lang: en
---

> From 193 items, 17 important content pieces were selected

---

**Agent Harness Architecture**
1. [Codex rust-v0.170.0 发布](#item-harness-arch-1) ⭐️ 7.8/10
2. [pydantic-ai v2.70.0 发布](#item-harness-arch-2) ⭐️ 7.8/10
3. [openai-agents v0.25 发布](#item-harness-arch-3) ⭐️ 7.8/10

**AI Agent Engineer**
1. [OpenAI 发布 GPT-6.2 双模型](#item-agent-engineer-1) ⭐️ 8.0/10
2. [llm CLI v0.38 发布](#item-agent-engineer-2) ⭐️ 7.8/10
3. [ONNX Runtime Repo Down](#item-agent-engineer-3) ⭐️ 7.0/10
4. [Prime Radiant 开源外部沙箱实现](#item-agent-engineer-4) ⭐️ 7.0/10
5. [Datasette Lite 浏览器完整重写](#item-agent-engineer-5) ⭐️ 7.0/10
6. [K2-Horizon 开源模型舰队发布](#item-agent-engineer-6) ⭐️ 7.0/10
7. [SWE-CoWork 编码代理组织基准发布](#item-agent-engineer-7) ⭐️ 7.0/10
8. [HF Daily Papers 权重空间编程无需 Transformer](#item-agent-engineer-8) ⭐️ 6.0/10
9. [ResWAM 世界动作模型论文发布](#item-agent-engineer-9) ⭐️ 6.0/10
10. [Edge0-145B-NVFP4 登顶趋势榜](#item-agent-engineer-10) ⭐️ 6.0/10

**AI Daily**
1. [OpenAI 发布 GPT-6.2 Astra 与 Sol](#item-ai-daily-1) ⭐️ 9.8/10
2. [ChatGPT Sales 插件上线](#item-ai-daily-2) ⭐️ 7.8/10
3. [GitHub 开源 Agent Host Protocol](#item-ai-daily-3) ⭐️ 7.8/10
4. [GitHub 微软试点 AI 辅助开源漏洞修复](#item-ai-daily-4) ⭐️ 6.8/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [Codex rust-v0.170.0 发布](https://github.com/openai/codex/releases/tag/rust-v0.170.0) ⭐️ 7.8/10

OpenAI Codex agent harness 发布 rust-v0.170.0。本次更新增加实验性跨环境同名 MCP 服务器支持（\#60905）、MCP OAuth 凭证竞态修复（\#60849, \#60981），以及 TUI 实时语音通话的 WebRTC 协商能力（\#61172）。沙箱机制修复了权限保留、子线程限制传递和 Windows 运行时注册恢复（\#60936, \#61134, \#60943, \#60944）。运行时稳定性改进包括 WebSocket 超大请求按广告限制立即回退 HTTP（\#60840, \#60841）、Cloud 会话重连及恢复轮次保留（\#60969, \#61014），以及 OpenTelemetry HTTP 导出器自动刷新认证头（\#61028）。

github · github-actions\[bot\] · Nov 18, 03:40

**「设计要点」** 沙箱权限管理转向 permission profile 标签体系，并在会话准入时统一规范化权限更新，确保子线程继承现有限制。MCP 服务器实现按环境隔离同名实例，运行时通过 WebSocket 消息大小限制回退 HTTP 并支持 Cloud 会话断线重连与恢复轮次保留。

**「改了什么」** 相对 rust-v0.169.0，本版本新增 TUI 实时语音通话实验支持、跨环境 MCP 服务器隔离和 OpenTelemetry 自动刷新认证头。修复覆盖 MCP OAuth 竞态、沙箱权限保留与 Windows 兼容性、WebSocket 超大请求回退、Cloud 会话重连及文件搜索去重。

**Tags**: `#mcp`, `#sandbox`, `#runtime`, `#permissions`, `#tools`

---

<a id="item-harness-arch-2"></a>
### [pydantic-ai v2.70.0 发布](https://github.com/pydantic/pydantic-ai/releases/tag/v2.70.0) ⭐️ 7.8/10

pydantic-ai v2.70.0 发布，同步修复 pydantic-ai-harness 0.70.0 中两个高危 ReDoS 漏洞。ToolOutputLimits 的 ANSI  stripping（strip\_ansi=True）与 JWT 密钥脱敏正则均存在二次时间复杂度回溯，攻击者可构造超长工具输出或含 JWT 的文本阻塞事件循环数秒至数分钟。本次更新还新增 StreamGuardrail、PruneToolResults、CapabilityPart 等运行时能力，并扩展 xAI、HuggingFace、Groq 及 OpenAI gpt-6.2 系列模型适配。

github · dsfaccini · Nov 17, 22:44

**「设计要点」** 安全修复位于 pydantic-ai-harness 层而非核心运行时，说明工具输出处理与密钥脱敏属于 harness 级职责。事件循环阻塞的影响路径表明，相关正则操作在异步运行时中同步执行且缺乏超时保护。

**「改了什么」** 修复 pydantic-ai-harness 0.70.0 中两个高危 ReDoS 漏洞：ToolOutputLimits 的 ANSI  stripping 正则与 JWT 脱敏正则。新增 StreamGuardrail 流式文本筛查、PruneToolResults 工具结果摘要、CapabilityPart 语音权限声明，以及 SpendLimits Budget 按作用域解析。模型层新增 xAI service\_tier 转发、HuggingFace logprobs、Groq JSON 输出修正与 OpenAI gpt-6.2 模型支持。

**「评论」** 暂无社区评论。

**Tags**: `#runtime`, `#tools`, `#permissions`

---

<a id="item-harness-arch-3"></a>
### [openai-agents v0.25 发布](https://github.com/openai/openai-agents-python/releases/tag/v0.25.0) ⭐️ 7.8/10

openai-agents v0.25.0 发布。移除 Runloop 沙箱提供方，构成破坏性变更。暴露第三方会话适配器工具，供 harness 实现者集成。修复内部沙箱操作误加载工作区启动文件。修复跨 resume 丢失嵌套 ToolContext 审批决策。避免已完成工具调用重复指纹。新增 handoff 错误恢复 opt-in。对齐隐式设置与提供方模型。对齐模型默认值与 TS SDK。MCP v2 支持并发 Streamable HTTP 请求。GPT-6 Chat Completions 工具请求默认关闭推理。依赖项升级：openai 3.29.0→3.48.0，mcp 2.0.0→2.3.0，websockets 15.0.1→16.1.1。

github · openai-sdks\[bot\] · Nov 18, 00:22

**「设计要点」** 沙箱层移除内置 Runloop 提供方，runtime 沙箱配置责任转移至外部集成。工具权限层修复 ToolContext 审批决策在 resume 间的持久化。新增会话适配器工具，供 harness 实现者接入自定义状态存储。

**「改了什么」** 破坏性变更：移除 Runloop 沙箱提供方。新增能力：暴露第三方会话适配器工具，handoff 错误恢复 opt-in。问题修复：内部沙箱操作不再加载工作区启动文件；嵌套 ToolContext 审批决策跨 resume 保留；已完成工具调用停止重复指纹；隐式设置与提供方模型对齐；模型默认值与 TS SDK 对齐；MCP v2 支持并发 Streamable HTTP 请求；GPT-6 Chat Completions 工具请求默认非推理。依赖升级：openai 3.29.0→3.48.0，mcp 2.0.0→2.3.0，websockets 15.0.1→16.1.1。

**Tags**: `#sandbox`, `#tools`, `#permissions`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [OpenAI 发布 GPT-6.2 双模型](https://openai.com/index/introducing-gpt-6-2-astra-sol/) ⭐️ 8.0/10

2026年11月17日OpenAI正式发布GPT-6.2 Astra与GPT-6.2 Sol，API标识为\`gpt-6.2-astra\`与\`gpt-6.2-sol\`，第三方库LLM已发布0.38版本适配两款新模型，前者定位前沿 hardest projects 模型，后者定位高效日常通用模型。Astra定价为输入$8/MTok、输出$40/MTok，是上一代6 Astra的80%，缓存输入价格降至$0.40/MTok，为上一代的1/4；Sol定价维持$2/$10，是GPT-5.6 Sol的一半。官方宣称两款模型在agent任务上可实现最高5倍成本降低、20% token 消耗减少，推理速度更快且所需工具调用更少，已在PacBench、数据分析考试等agent相关eval中验证性能。社区实测显示数据分析考试中Astra成本从V6的约20美元降至约4美元、Sol从约2.6美元降至约1.2美元，准确率与上一代接近，但存在偶尔提前终止未找到答案的情况；用Codex CLI跑复杂代码生成任务时，两款模型在3D动画生成任务中表现弱于Claude Fable 5.2与Gemini 4 Carbon。部分用户反馈Astra长任务中会随机询问无关内部实现细节，办公场景生成效果弱于旧模型，PacBench得分Astra为92、Sol为87，分别低于Kimi K3.1 Pro的93与Muse Wonder的87，但耗时更短。影响群体为使用OpenAI API开发agent、做coding agent harness的工程师。

hackernews · jasondavies · Nov 17, 17:46 · [Discussion](https://news.ycombinator.com/item?id=50535230)

**「为什么重要」** 已发生的agent场景定价下调与效率提升可直接降低coding agent的API成本，是当前值得跟进的变化；但成本下降、效率提升能否复现到所有自定义agent场景，以及长任务稳定性、办公场景生成质量的问题是否普遍，尚未得到充分验证。

**「可关注」** 长时agent任务可优先用小流量对比GPT-6.2双模型与上一代的token消耗、工具调用次数与实际成本，同时留意长任务中无关提问、提前终止的边界case。

**「评论」** 社区对成本下降共识明确，但模型表现存在分歧：办公场景生成质量、PacBench得分弱于部分竞品，长任务稳定性也收到较多负面反馈，也有用户认可其推理速度表现。

**Tags**: `#eval`, `#coding-agent`

---

<a id="item-agent-engineer-2"></a>
### [llm CLI v0.38 发布](https://github.com/simonw/llm/releases/tag/0.38) ⭐️ 7.8/10

2026-11-17，simonw 发布 llm CLI 正式版 v0.38。本次更新新增 OpenAI GPT-6.2 Astra、Sol 模型（gpt-6.2-astra、gpt-6.2-sol）的支持。修复6项问题：非OpenAI相关CLI命令（如llm --version、llm models list）启动慢的问题，原因是openai包改为首次需要时才导入；开启LLM\_OPENAI\_SHOW\_RESPONSES=1时异步OpenAI模型请求报Invalid \`http\_client\` argument错误的问题，现在异步请求/响应日志逻辑与同步一致；工具schema清理Pydantic title注解时误删default、const、enum、examples值内的title键的问题；模板、-f传入的片段文件、--functions传入的Python文件默认按UTF-8读取，非UTF-8文件回退到系统默认编码，避免Windows等系统出现UnicodeDecodeError；llm fragments list -q现在返回匹配片段的所有别名，而非仅匹配到的别名；Toolbox子类调用父类\_\_init\_\_时，现在会记录子类构造参数而非被父类参数覆盖。同时更新安装文档，提示uv tool upgrade llm、pipx upgrade llm、brew upgrade llm会移除llm install安装的插件，推荐用llm install -U llm升级保留插件。

github · simonw · Nov 17, 19:00

**「为什么重要」** 对使用llm CLI构建或调试AI Agent的开发者而言，本次更新直接覆盖了模型调用、启动性能、可观测性、函数调用schema准确性四个高频场景的问题。新增的GPT-6.2模型支持让用户可第一时间调用OpenAI最新发布的模型能力，异步日志修复解决了此前开启响应观测时异步请求完全不可用的阻塞性问题。

**「可关注」** 可关注：llm v0.38 修复了开启LLM\_OPENAI\_SHOW\_RESPONSES=1时异步OpenAI请求的报错问题，此前该配置会导致所有异步请求在发送前就失败，现在可正常观测异步调用的全链路日志。

**Tags**: `#observability`, `#openai`, `#bugfix`, `#tooling`

---

<a id="item-agent-engineer-3"></a>
### [ONNX Runtime Repo Down](https://github.com/microsoft/onnxruntime) ⭐️ 7.0/10

On November 17, 2026, an unconfirmed Hacker News post reported that Microsoft&\#x27;s official ONNX Runtime GitHub repository \(https://github.com/microsoft/onnxruntime\) is no longer accessible. The repository, which had roughly 22,000 stars, is a widely used inference runtime for agent and evaluation workflows. Users maintaining production eval pipelines reported unannounced breakage starting the morning of the incident, with no prior warning from Microsoft. The cause of the unavailability remains unconfirmed, and Microsoft has not issued any public statement as of the report timestamp.

hackernews · nvader · Nov 17, 23:18 · [Discussion](https://news.ycombinator.com/item?id=50539610)

**「Why It Matters」** ONNX Runtime is a core dependency for many agent and eval harnesses, so its sudden unavailability directly disrupts production pipelines with no advance notice. The lack of official communication or confirmed cause amplifies risk for teams relying on the runtime for critical workflows.

**「Engineer Takeaway」** Watch for: Maintain mirrored copies or alternative dependency sources for critical open-source components used in production eval and agent pipelines to mitigate single-point-of-failure risks from sudden repository unavailability.

**「Community Discussion」** Community comments include unsubstantiated speculation that the disappearance may be linked to compromised packages, default telemetry data exfiltration, or newly discovered backdoor exploit vectors. One user shared Intel&\#x27;s ONNX Runtime fork \(https://github.com/intel/onnxruntime\) as a temporary alternative, though no official explanation for the incident has been released.

**Tags**: `#eval`, `#harness`

---

<a id="item-agent-engineer-4"></a>
### [Prime Radiant 开源外部沙箱实现](https://simonwillison.net/2026/Nov/17/external-sandboxes-for-coding-agents/) ⭐️ 7.0/10

2026-11-17，Simon Willison 与 Prime Radiant 发布 coding agent 的「外部沙箱」模式：agent 代码在专用沙箱内执行，agent 本身驻留沙箱外。同日开源三套本地沙箱服务器实现，分别是基于 v86 与 WebAssembly 运行 Alpine Linux 的 \`external-sandbox-v86\`、基于 Apple Containers 的 \`external-sandbox-container\`，以及集成 Microsoft Quicksand 与 QEMU 的 \`external-sandbox-quicksand\`。三套实现均暴露 localhost API，支持配置 Pi、Claude Code 或 Codex 将代码执行请求转发至沙箱，并附带可热更新的 HTTP/HTTPS 允许列表代理与凭证替换机制。目前无社区评论。

rss · Simon Willison · Nov 17, 22:52

**「为什么重要」** 该模式将 agent 代码执行与 agent 本体分离，直接针对提示词注入或执行错误对宿主机的安全风险。三套开源实现分别基于 WebAssembly、Apple Containers 和 QEMU，为 harness 与权限工程提供了可运行的技术样本。

**「可关注」** 可关注：三套实现均通过 localhost API 暴露沙箱服务，harness 可在代理层配置网络白名单与凭证替换，在不改动 agent 的前提下实现执行环境隔离。

**Tags**: `#permissions`, `#harness`, `#coding-agent`

---

<a id="item-agent-engineer-5"></a>
### [Datasette Lite 浏览器完整重写](https://simonwillison.net/2026/Nov/17/datasette-lite/) ⭐️ 7.0/10

Simon Willison 于 2026-11-17 发布 Datasette Lite 完整重写版本。该版本通过 Pyodide 与 service workers 将完整服务端 Datasette Python 应用运行在浏览器中，替代了 2022 年首次发布时基于 web worker 与 innerHTML 注入的方案。用户可通过 lite.datasette.io 的 URL 参数加载 SQLite、JSON、CSV 或 SQL 脚本数据库，从 PyPI 选择 Datasette 版本，指定 GitHub commit/tag/branch，挑选 100 余种 SQLite 版本之一，并安装来自 PyPI 或 wheel URL 的插件。URL 支持 install、url、metadata、ref 等参数，可用于精确复现 bug 或演示工作进度，无需启动后端服务器；该机制已被用于 Datasette 自身 issue 中的 bug 对比演示。

rss · Simon Willison · Nov 17, 16:48

**「为什么重要」** 这改变了在浏览器中运行完整服务端 Python Web 应用的可行性判断。对构建 coding agent 或浏览器端 Python 工具链的工程师而言，service worker 方案解决了此前 JavaScript 插件无法执行、路由状态难以维持的关键限制。

**「可关注」** 可关注：service worker 介入后，Pyodide 应用可从“页面内脚本”升级为“完整网络应用栈”，路由、插件、静态资源加载均可被拦截和重写。

**Tags**: `#toolchain`, `#pyodide`, `#browser`

---

<a id="item-agent-engineer-6"></a>
### [K2-Horizon 开源模型舰队发布](https://huggingface.co/papers/2611.21003) ⭐️ 7.0/10

2026-11-18，Hugging Face Daily Papers 收录 K2-Horizon 开源模型舰队，包含 6 个模型规格，范围从 0.9B 稠密模型到 375B-A23B 混合专家模型，面向通用推理与智能体工作负载。论文提出 Mixture-of-Value Attention（MoVA）与 softplus 注意力门控，报告称 36B-A4B 模型以七分之一激活参数接近 32B 稠密模型性能；同时推出 Uno 无损扩散适配器，报告解码速度提升最高 2.2 倍。该舰队在智能体与编码基准上声称具备竞争力，目前完全开源，HF 日榜获 73 次点赞。

rss · Hugging Face Daily Papers · Nov 18, 03:59

**「为什么重要」** 这为智能体工程师提供了新的开源模型选项，且 MoVA 与 Uno 直接针对部署效率。但性能声明尚未经独立基准测试验证。

**「可关注」** MoVA 将 MoE 应用于注意力值投影，Uno 适配器报告无损提升解码速度 2.2 倍，两者均针对 agent 部署的激活参数与推理效率；36B-A4B 接近 32B 稠密模型的报告需独立验证。

**Tags**: `#coding-agent`, `#eval`, `#model-architecture`, `#efficiency`

---

<a id="item-agent-engineer-7"></a>
### [SWE-CoWork 编码代理组织基准发布](https://huggingface.co/papers/2611.20218) ⭐️ 7.0/10

SWE-CoWork 基准测试于 2026-11-18 由 Hugging Face Daily Papers 发布，面向 coding agent 与 harness 开发者。该基准包含 101 个跨真实仓库的开发任务，覆盖 11 种编程语言和 12 个应用领域。每个任务将编码代理置于含 26 名同事的模拟工程组织中，测试需求恢复、冲突调和与实现变更能力。研究团队评估了 11 个模型，观察到部分实现与完整任务之间存在显著差距，但具体性能数据未在摘要中提供。

rss · Hugging Face Daily Papers · Nov 18, 03:59

**「为什么重要」** 该基准首次将编码代理评估扩展到组织协作场景，为 coding agent 和 harness 开发提供了新的评测维度。不过具体模型性能排名和实际影响尚待完整论文验证。

**「可关注」** 可关注：编码代理在模拟组织中的需求恢复能力，或成为 harness 评估的新指标。

**Tags**: `#eval`, `#coding-agent`, `#harness`

---

<a id="item-agent-engineer-8"></a>
### [HF Daily Papers 权重空间编程无需 Transformer](https://huggingface.co/papers/2611.22055) ⭐️ 6.0/10

Hugging Face Daily Papers 于 2026-11-18 收录论文，展示三个前沿 LLM 在仅给 10 个标注样本与沙箱的条件下，为权重空间编程自主设计非 Transformer 稀疏架构。模型将纯文本事实编译为稀疏表，由固定程序查询，在多项选择 eval 任务上达到 54.4% 测试准确率，超过同期发布的最优 Transformer。该工作直接改进 AI agent、harness 或 eval 工具链的关联有限，因研究聚焦通用神经架构设计；论文内容被截断，具体架构细节与更广泛任务表现未披露。

rss · Hugging Face Daily Papers · Nov 18, 00:00

**「为什么重要」** 该工作以 54.4% 准确率证明 LLM 可在极少监督下设计有效计算结构，但当前任务与 agent 工程核心工作流脱节，尚未形成可直接复用的工具或方法论。

**「可关注」** 可关注：LLM 在极少样本下能自主设计稀疏架构并将文本编译为可查询表，显示权重空间编程无需 Transformer，但当前任务与 agent 工具链脱节。

**Tags**: `#eval`, `#architecture`, `#weight-space-programming`

---

<a id="item-agent-engineer-9"></a>
### [ResWAM 世界动作模型论文发布](https://huggingface.co/papers/2611.19559) ⭐️ 6.0/10

2026-11-18，Hugging Face Daily Papers 收录论文《ResWAM: Learning What Changes, Not What Stays, for World-Action Models》。该论文提出 ResWAM 世界动作模型，通过冻结 DINOv3 空间的视觉残差学习，仅监督当前帧到未来帧的特征变化，替代传统全未来观测监督。该方法降低视觉-语言-动作策略的计算成本，同时提升对任务相关运动的学习效果，对具身智能体开发有参考价值。目前仅提供摘要，无性能数据、代码发布或完整技术细节，可立即落地的 actionable 价值有限。

rss · Hugging Face Daily Papers · Nov 18, 00:00

**「为什么重要」** 该论文针对现有世界动作模型计算开销大、静态背景主导损失的问题，提出轻量替代方案。但因其仅发布摘要，尚未证实实际部署效果与性能增益。

**「可关注」** 可关注：冻结预训练视觉空间做残差监督，可能降低世界模型训练与推理成本。

**Tags**: `#coding-agent`

---

<a id="item-agent-engineer-10"></a>
### [Edge0-145B-NVFP4 登顶趋势榜](https://huggingface.co/Edge0/Edge0-145B-NVFP4) ⭐️ 6.0/10

Edge0/Edge0-145B-NVFP4 became a trending Hugging Face model on 2026-11-18 with a trendingScore of 123 and 496 likes. It is a 145B-parameter MoE text-generation model quantized to 4-bit NVFP4, tagged for coding-agent and edge-inference use cases. The provided material contains only basic metadata; no performance data, technical details, or usage guides are available, leaving deployment characteristics unverified.

rss · Hugging Face Trending Models · Nov 18, 03:59

**「为什么重要」** The NVFP4 quantization combined with MoE architecture could offer optimization potential for running coding agents on edge devices, but without benchmark data, the actual impact remains unconfirmed.

**「可关注」** Monitor the 145B MoE model&\#x27;s accuracy retention under 4-bit NVFP4 quantization and actual inference latency and memory footprint in coding-agent scenarios.

**Tags**: `#coding-agent`

---

## AI Daily

<a id="item-ai-daily-1"></a>
### [OpenAI 发布 GPT-6.2 Astra 与 Sol](https://openai.com/index/introducing-gpt-6-2-astra-sol) ⭐️ 9.8/10

OpenAI 正式发布 GPT-6.2 Astra 和 Sol 两个新模型。新模型在专业输出、编码和计算机使用能力上有所增强，同时效率更高、成本更低。此次更新覆盖 ChatGPT Work、Codex 及 API 产品线。

rss · OpenAI Blog · Nov 17, 17:45

**「为什么重要」** 对构建 coding agent 和 harness 的开发者而言，编码与计算机使用能力的提升可能直接改善工具调用稳定性；API 成本下降则可能降低批量测试与集成的开销。

**「可关注」** 可关注：GPT-6.2 Astra 与 Sol 在 Codex 和 API 产品线中的成本变化及计算机使用能力的改进。

**Tags**: `#model`, `#lab`, `#product`

---

<a id="item-ai-daily-2"></a>
### [ChatGPT Sales 插件上线](https://openai.com/index/introducing-chatgpt-for-sales) ⭐️ 7.8/10

OpenAI 推出 ChatGPT Sales 插件及 30 余个新增或扩展的合作伙伴插件，覆盖潜在客户研究、pitch 准备与 CRM 更新等销售工作流。该功能已在 ChatGPT 平台可用。

rss · OpenAI Blog · Nov 17, 08:00

**「可关注」** 可关注：ChatGPT 插件生态向垂直销售场景扩展，新增 CRM 数据写入与销售线索研究能力。

**Tags**: `#product`, `#lab`, `#industry`

---

<a id="item-ai-daily-3"></a>
### [GitHub 开源 Agent Host Protocol](https://github.blog/engineering/engineering-principles/building-the-agent-host-protocol-for-sessions-that-continue-across-devices/) ⭐️ 7.8/10

GitHub 开源 Agent Host Protocol（AHP）开放标准，用于实现 AI 智能体会话跨设备、跨应用的延续，目前已在 VS Code 的 GitHub Copilot 中落地，配套推出 5 个客户端与 2 个 agent host 实现。为适配 AHP，VS Code 侧新建的 agent host 约 36.9 万行 TypeScript，GitHub 侧 agent host 约 30.5 万行 Rust，原 Copilot Chat 扩展代码量超 41.5 万行 TypeScript。该协议围绕 URI 标识的 channel 设计，强制实现 root、session、chat 三个核心 channel，采用服务端仲裁的 reducer-based 状态模型，客户端通过发送 action 变更状态或触发副作用，支持弱网下的重连与操作重放。AHP 不约束 agent 行为逻辑，仅定义交互方式，核心协议保持最小化以便第三方集成。

rss · GitHub Blog · Nov 17, 18:20

**「为什么重要」** 此前各客户端需为 Copilot agent 做独立定制集成，且 agent 生命周期绑定单应用窗口，跨设备、跨应用会话延续难以实现。AHP 作为开放标准统一了交互规范，第三方开发者无需重复造轮子即可将 agent 接入自有工作流，同时支持会话在设备间无缝切换。

**「可关注」** 可关注：AHP 已发布官方规范文档，核心协议最小化，支持通过扩展 terminal、MCP、OTel 等可选 channel 适配自定义需求，reducer-based 状态模型可降低客户端与服务端的调试成本。

**Tags**: `#product`, `#open-source`, `#industry`

---

<a id="item-ai-daily-4"></a>
### [GitHub 微软试点 AI 辅助开源漏洞修复](https://github.blog/open-source/maintainers/maintainers-dont-need-more-ai-bug-reports-they-need-fixes/) ⭐️ 6.8/10

GitHub 与微软联合开展开源漏洞修复试点，使用微软 Codename MDASH 多模型代理扫描工具、GitHub 安全实验室 AI 分类代理及微软 FORGE 实验室人工验证，向 6 个开源项目维护者推送带修复建议的高质量漏洞报告，而非原始扫描结果。扫描共标记 9791 个潜在问题，经筛选验证后仅向维护者发送 99 份私有报告；截至 2026 年 11 月 15 日，55 份报告对应的漏洞已被修复，其中 14 份修复已进入正式发布。试点仅覆盖 6 个 GitHub 安全开源基金往期受资助项目，样本量有限，相关经验为早期探索结论。

rss · GitHub Blog · Nov 17, 18:29

**「为什么重要」** 当前 AI 生成的漏洞报告大量涌入开源社区，重复、无效报告已严重挤压维护者精力，该试点将 AI 能力从“生成漏洞发现”转向“辅助漏洞修复”，为缓解开源维护者负担、提升开源安全治理效率提供了可落地的实践参考。

**「可关注」** 可关注“多模型扫描 + AI 分类 + 人工验证 + 附带修复建议”的漏洞处理流程，该流程可将原始扫描结果压缩至约 1% 再推送至维护者，同时降低修复门槛。

**Tags**: `#open-source`, `#industry`, `#product`

---