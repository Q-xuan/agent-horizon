---
layout: default
title: "Horizon Summary: 2026-11-18 (ZH)"
date: 2026-11-18
lang: zh
---

> 从 193 条内容中筛选出 17 条重要资讯。

<nav id="ah-toc" class="ah-toc" aria-label="目录"><span class="ah-toc-title">目录</span><ul><li><a href="#sec-harness-arch"><span class="ah-toc-name">Harness 架构</span><span class="ah-toc-count">3条</span></a></li><li><a href="#sec-agent-engineer"><span class="ah-toc-name">Agent 工程师日报</span><span class="ah-toc-count">10条</span></a></li><li><a href="#sec-ai-daily"><span class="ah-toc-name">AI 日报</span><span class="ah-toc-count">4条</span></a></li></ul></nav>

---

**[Harness 架构](#sec-harness-arch)**
1. [Codex rust-v0.170.0 发布](#item-harness-arch-1) ⭐️ 7.8/10
2. [pydantic-ai v2.70.0 发布](#item-harness-arch-2) ⭐️ 7.8/10
3. [openai-agents-python v0.25.0 发布](#item-harness-arch-3) ⭐️ 7.8/10

**[Agent 工程师日报](#sec-agent-engineer)**
1. [GPT-6.2 Astra 与 Sol 发布](#item-agent-engineer-1) ⭐️ 8.0/10
2. [llm CLI v0.38 发布](#item-agent-engineer-2) ⭐️ 7.8/10
3. [ONNX Runtime 官方仓库突然不可用](#item-agent-engineer-3) ⭐️ 7.0/10
4. [coding agent 外部沙箱模式发布](#item-agent-engineer-4) ⭐️ 7.0/10
5. [Datasette Lite 完整重写发布](#item-agent-engineer-5) ⭐️ 7.0/10
6. [K2-Horizon 开源模型舰队发布](#item-agent-engineer-6) ⭐️ 7.0/10
7. [SWE-CoWork 编码代理基准](#item-agent-engineer-7) ⭐️ 7.0/10
8. [权重空间编程可脱离 Transformer](#item-agent-engineer-8) ⭐️ 6.0/10
9. [ResWAM 改世界动作模型监督范式](#item-agent-engineer-9) ⭐️ 6.0/10
10. [HF 趋势榜：Edge0-145B-NVFP4](#item-agent-engineer-10) ⭐️ 6.0/10

**[AI 日报](#sec-ai-daily)**
1. [GPT-6.2 Astra 与 Sol 发布](#item-ai-daily-1) ⭐️ 9.8/10
2. [ChatGPT 推出 Sales 销售插件](#item-ai-daily-2) ⭐️ 7.8/10
3. [GitHub 开源 AHP 跨设备会话协议](#item-ai-daily-3) ⭐️ 7.8/10
4. [GitHub 微软试点 AI 辅助开源漏洞修复](#item-ai-daily-4) ⭐️ 6.8/10

---

## Harness 架构
{: #sec-harness-arch .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-harness-arch" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-harness-arch-1"></a>
### [Codex rust-v0.170.0 发布](https://github.com/openai/codex/releases/tag/rust-v0.170.0) ⭐️ 7.8/10

OpenAI Codex agent harness 发布 rust-v0.170.0。本次更新引入实验性跨环境同名称 MCP 服务器支持、MCP OAuth 凭证竞争修复，以及 TUI 实时语音通话（WebRTC）能力。沙盒层修复了权限保留、子线程限制传递和 Windows 平台兼容性问题，运行时改进了 WebSocket 超大请求回退、Cloud 对话重连和 Windows 注册恢复。

github · github-actions\[bot\] · 11月18日 03:40

**「设计要点」** 该版本在工具层扩展 MCP 协议支持，允许跨环境隔离同名称服务器实例；运行时通过 WebSocket 消息大小限制感知和 HTTP 回退优化长请求传输；沙盒权限模型新增 permission profile 机制，统一处理会话准入和恢复时的权限继承。

**「改了什么」** 相对 rust-v0.169.0，新增实验性 TUI 实时语音通话与跨环境 MCP 服务器隔离，修复 MCP OAuth 凭证竞争、沙盒权限及子线程限制失效问题，并改进 Cloud 对话重连恢复和 Windows 运行时兼容性。

**标签**: `#mcp`, `#sandbox`, `#runtime`, `#permissions`, `#tools`

---

<a id="item-harness-arch-2"></a>
### [pydantic-ai v2.70.0 发布](https://github.com/pydantic/pydantic-ai/releases/tag/v2.70.0) ⭐️ 7.8/10

pydantic-ai v2.70.0 发布，修复 pydantic-ai-harness 两个高危 ReDoS 漏洞。ToolOutputLimits 在 strip\_ansi=True 时，ANSI 转义序列正则存在二次时间复杂度；JWT 密钥脱敏正则回溯同样导致事件循环阻塞。攻击者可通过恶意工具输出或含 JWT 文本触发数十秒至数分钟的事件循环占用。修复版本为 pydantic-ai-harness 0.70.0。本次还包含 xAI service\_tier 转发、HuggingFace logprobs 支持、Skills 文件读取等兼容性变更与新功能。

github · dsfaccini · 11月17日 22:44

**「改了什么」** 修复 ToolOutputLimits ANSI stripping 正则（GHSA-m4cr-m4qc-9hh3）与 JWT secret redaction 正则（GHSA-5m5q-5qj4-gx9h）两个高危 ReDoS 漏洞，消除事件循环二次时间阻塞风险。新增 StreamGuardrail、PruneToolResults、ToolSearch 等运行时能力。HuggingFaceModelSettings 增加 huggingface\_logprobs 与 huggingface\_top\_logprobs 参数。修复 OpenAIChatModel、AnthropicModel、GroqModel 等模型适配问题。

**标签**: `#runtime`, `#tools`, `#permissions`

---

<a id="item-harness-arch-3"></a>
### [openai-agents-python v0.25.0 发布](https://github.com/openai/openai-agents-python/releases/tag/v0.25.0) ⭐️ 7.8/10

openai-agents-python v0.25.0 发布。本次更新移除 Runloop sandbox provider，构成破坏性变更。新增第三方 session adapter 实用工具，修复 sandbox 内部操作误加载 workspace 启动文件、resume 时丢失嵌套 ToolContext 审批决策、已完成工具调用重复指纹等问题。模型默认值与 TypeScript SDK 对齐，GPT-6 Chat Completions 工具请求默认关闭 reasoning，MCP v2 支持并发 Streamable HTTP 请求。

github · openai-sdks\[bot\] · 11月18日 00:22

**「改了什么」** 破坏性变更：移除 Runloop sandbox provider。新增第三方 session adapter 接入工具。修复 sandbox 启动文件加载、ToolContext 嵌套审批决策恢复、工具调用重复指纹三个问题。新增 opt-in handoff error recovery，模型默认值与 TS SDK 对齐，MCP v2 支持并发 Streamable HTTP 请求。

**标签**: `#sandbox`, `#tools`, `#permissions`

---

## Agent 工程师日报
{: #sec-agent-engineer .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-agent-engineer" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-agent-engineer-1"></a>
### [GPT-6.2 Astra 与 Sol 发布](https://openai.com/index/introducing-gpt-6-2-astra-sol/) ⭐️ 8.0/10

2026 年 11 月 17 日 OpenAI 官方发布 GPT-6.2 Astra 与 GPT-6.2 Sol，API 标识为 gpt-6.2-astra 与 gpt-6.2-sol。Astra 定价为输入$8/MTok、输出$40/MTok，与 Claude Fable 5.2 定价一致，均为上一代 6 Astra 价格的 80%，缓存输入价格降至$0.40/MTok，为上一代的 40%；Sol 维持$2/$10 的定价，是 GPT-5.6 Sol 价格的一半。官方称 GPT-6.2 Astra 为前沿模型，GPT-6.2 Sol 为高效通用模型，两款模型针对 agent 工作负载实现最高 5 倍成本下降、20% token 消耗减少、更少工具调用需求、更快推理速度，已在 PacBench、数据分析考试等 agent 相关评测中验证性能。社区实测显示 Astra 在 PacBench 得 92 分（耗时 6.6 分钟、花费$2.04），Sol 得 87 分（耗时 6.3 分钟、花费$0.49），但也有用户反馈 Astra 长任务中会随机询问无关内部实现细节，偶尔提前终止未找到答案。

hackernews · jasondavies · 11月17日 17:46 · [社区讨论](https://news.ycombinator.com/item?id=50535230)

**「为什么重要」** 两款模型针对 agent 场景做了显式的成本、速度与效率优化，定价下调对长运行 agent 会话的成本影响直接；但社区实测显示其部分生成质量仍存在争议，尚未形成一致的全场景性能优势共识。

**「可关注」** 可关注：gpt-6.2-astra 的缓存输入价格降至$0.40/MTok，长 agent 会话场景的成本下降空间明确，但需验证长任务中随机询问无关细节、提前终止未返回结果的问题是否影响实际业务流。

**「评论」** 社区共识认为两款模型成本与速度优势明显，agent 场景工具调用次数减少；分歧集中在生成质量上，Astra 部分 benchmark 得分低于竞品，办公类内容生成表现被指弱于更早的模型，长任务中随机询问无关细节的问题也引发不满。

**标签**: `#eval`, `#coding-agent`

---

<a id="item-agent-engineer-2"></a>
### [llm CLI v0.38 发布](https://github.com/simonw/llm/releases/tag/0.38) ⭐️ 7.8/10

2026 年 11 月 17 日，simonw 发布 llm CLI v0.38 官方版本。本次更新新增支持 OpenAI gpt-6.2-astra、gpt-6.2-sol 两个模型，同时修复 6 项缺陷：非 OpenAI 相关 CLI 命令（如 llm --version、llm models list）启动速度提升、开启 LLM\_OPENAI\_SHOW\_RESPONSES=1 时异步 OpenAI 模型请求报错修复、工具 schema 中 title 键保留、跨平台文件编码兼容、片段查询逻辑修正、Toolbox 子类参数记录修正。此外更新了升级文档，提示使用 llm install -U llm 升级可保留已安装插件，避免 uv tool upgrade llm、pipx upgrade llm、brew upgrade llm 移除插件。

github · simonw · 11月17日 19:00

**「为什么重要」** 对 coding agent / harness 开发者而言，异步模型日志修复和工具 schema 标题保留直接解决 function calling 场景的可观测性与参数传递正确性问题；非 OpenAI 命令启动加速降低了 CLI 工具的日常调用开销。目前暂无公开基准数据验证启动加速的具体幅度。

**「可关注」** 可关注：llm CLI 升级时若需保留已安装插件，应使用 llm install -U llm 而非 uv tool upgrade llm、pipx upgrade llm 或 brew upgrade llm。

**标签**: `#observability`, `#openai`, `#bugfix`, `#tooling`

---

<a id="item-agent-engineer-3"></a>
### [ONNX Runtime 官方仓库突然不可用](https://github.com/microsoft/onnxruntime) ⭐️ 7.0/10

2026 年 11 月 17 日有未确认的 Hacker News 帖子称，微软官方 ONNX Runtime GitHub 仓库（https://github.com/microsoft/onnxruntime）已突然无法访问，该仓库此前拥有 2.2 万星标，是 agent 与 eval 工作流广泛使用的推理运行时。已有用户反馈当日 eval 流水线因此中断，未发现任何提前通知。目前事件原因未获官方证实，社区猜测涉及包泄露、遥测问题或安全后门风险，均无实锤。

hackernews · nvader · 11月17日 23:18 · [社区讨论](https://news.ycombinator.com/item?id=50539610)

**「为什么重要」** 该仓库是 agent 与 eval 工具链的常用核心依赖，其突然不可用已造成实际生产流水线中断；社区提及的安全、遥测相关问题暂无官方证实，不构成已确认影响。

**「可关注」** 可关注：依赖 ONNX Runtime 的流水线可临时验证 intel/onnxruntime fork 的兼容性，同时检查自身依赖链对单一官方仓库的容错能力。

**「评论」** 社区实际体验显示多用户当日 eval 流水线首先发现故障，未找到任何提前通知；用户猜测原因包括 PyPI 包泄露、默认遥测数据外泄、模型后门新攻击向量，同时有人提供了 Intel 维护的带 OpenVINO 修改的 fork 作为临时替代，但所有猜测均无官方证实。

**标签**: `#eval`, `#harness`

---

<a id="item-agent-engineer-4"></a>
### [coding agent 外部沙箱模式发布](https://simonwillison.net/2026/Nov/17/external-sandboxes-for-coding-agents/) ⭐️ 7.0/10

2026 年 11 月 17 日，Simon Willison 与 AI 研究实验室 Prime Radiant 联合推出面向 coding agent 的「外部沙箱」执行模式，将 agent 执行的代码与 agent 本身隔离运行，降低误操作或提示词注入的破坏风险。目前开源三个具体实现：external-sandbox-v86 基于 v86 在 WebAssembly 中运行 Alpine Linux，external-sandbox-container 基于 Apple Containers 运行 Alpine Linux，external-sandbox-quicksand 基于微软 Quicksand 库打包 QEMU 与 Alpine Linux。所有实现提供统一 localhost API，支持 Pi、Claude Code、Codex 等 agent 配置调用，附带可动态调整的 HTTP/HTTPS 白名单代理与凭证替换机制，用于限制 agent 代码出站访问、避免向 agent 泄露密钥。目前未公开这些实现的大规模生产环境验证数据。

rss · Simon Willison · 11月17日 22:52

**「为什么重要」** 该模式直接针对 coding agent 的核心安全痛点，给出了可落地的开源实现，为轻量本地沙箱集成提供了新的可选方案；但各实现的性能损耗、生产稳定性及跨框架兼容性尚未有公开验证结果。

**「可关注」** 可关注：三个开源实现均提供统一 localhost API，配套网络白名单代理与凭证替换机制，可低成本接入现有 coding agent harness 做隔离验证。

**标签**: `#permissions`, `#harness`, `#coding-agent`

---

<a id="item-agent-engineer-5"></a>
### [Datasette Lite 完整重写发布](https://simonwillison.net/2026/Nov/17/datasette-lite/) ⭐️ 7.0/10

Simon Willison 于 2026-11-17 发布 Datasette Lite 完整重写版本，基于 Pyodide 与 service workers 在浏览器中运行完整服务端 Datasette Python 应用。用户可通过 URL 参数加载 SQLite/JSON/CSV 数据库、选择 Datasette 版本（PyPI 或 GitHub 引用）、挑选 100 余种 SQLite 版本，并安装 PyPI 或 wheel 插件；目标资源需支持 open CORS headers。相比 2022 年初始版本的 web worker + innerHTML hack（导致 JavaScript 功能失效），新版本功能已接近真实服务端应用。该工具面向需快速分享数据库 demo、bug 复现或 work-in-progress 功能的开发者，无需启动后端服务。

rss · Simon Willison · 11月17日 16:48

**「为什么重要」** 已发生的变化是浏览器端 Python Web 应用首次通过 service workers 实现接近原生的插件与 JS 混合执行。尚未证实的影响包括这是否会推动更多服务器端 Python 框架采用类似浏览器端分发模式，目前仅见作者将其用于自身开发流程。

**「可关注」** 可关注：service workers 将 Pyodide 应用从 innerHTML 注入 hack 升级为可执行完整 JS 插件的运行时，这对浏览器端 Python Web 框架的架构设计有参考价值。

**标签**: `#toolchain`, `#pyodide`, `#browser`

---

<a id="item-agent-engineer-6"></a>
### [K2-Horizon 开源模型舰队发布](https://huggingface.co/papers/2611.21003) ⭐️ 7.0/10

2026 年 11 月 18 日，Hugging Face Daily Papers 发布 K2-Horizon 开源语言模型舰队，共包含 6 款完全开源模型，参数量覆盖 0.9B 稠密模型到 375B-A23B 混合专家（MoE）模型，针对通用推理、智能体工作（数学、科学、软件工程、深度研究、办公自动化等场景）优化。该舰队引入混合值注意力（MoVA）与 Uno 无损扩散适配器两项技术，其中 36B-A4B 模型在相同训练数据下接近 32B 稠密模型性能，激活参数仅为后者的七分之一，解码速度最高提升 2.2 倍。官方称其在智能体与编码基准测试中与同尺寸主流开源模型性能相当或领先，该论文当日获 Hugging Face 社区 73 次点赞。

rss · Hugging Face Daily Papers · 11月18日 03:59

**「为什么重要」** 该模型舰队针对智能体与编码场景优化，提出的 MoVA 与 Uno 无损扩散适配器为小参数模型实现接近大参数稠密模型性能提供了可参考的技术路径，相关基准测试结果可供做 coding agent 的工程师评估模型选型。

**「可关注」** 可关注：MoVA 将混合专家机制应用于注意力值投影、搭配 softplus 注意力门控的方案，可在降低激活参数量的同时维持接近更大稠密模型的性能，Uno 无损扩散适配器可进一步提升解码速度。

**标签**: `#coding-agent`, `#eval`, `#model-architecture`, `#efficiency`

---

<a id="item-agent-engineer-7"></a>
### [SWE-CoWork 编码代理基准](https://huggingface.co/papers/2611.20218) ⭐️ 7.0/10

SWE-CoWork 基准测试于 2026-11-18 在 Hugging Face Daily Papers 发布。该基准包含 101 个开发任务，覆盖 101 个真实仓库、11 种编程语言和 12 个应用领域，面向编码代理与 harness 开发者提供新评估维度。每个任务将代理置于模拟工程组织，要求其从简短交接中恢复分散在 26 位同事和工作记录中的需求，协调冲突证据，并实施由私有可执行测试评估的更改。评估涉及 11 个模型，结果显示部分实现与完整任务完成之间存在显著差距，但完整性能结果细节未在提供内容中披露。

rss · Hugging Face Daily Papers · 11月18日 03:59

**「为什么重要」** 该基准首次将编码代理评估置于模拟组织协作场景，补充了现有单任务仓库级评估的空白。不过完整性能结果尚未披露，实际对 harness 选型的指导作用待后续数据验证。

**「可关注」** 可关注：基准引入 26 位具有限知识和受控协作行为的模拟同事，以及私有可执行测试，对编码代理的需求恢复和冲突协调能力提出新约束。

**标签**: `#eval`, `#coding-agent`, `#harness`

---

<a id="item-agent-engineer-8"></a>
### [权重空间编程可脱离 Transformer](https://huggingface.co/papers/2611.22055) ⭐️ 6.0/10

2026 年 11 月 18 日 Hugging Face Daily Papers 收录相关研究，给定最少指导、10 个标注样本与沙箱环境，3 个前沿 LLM 在多项选择题任务中可自主设计非 Transformer 的稀疏架构用于权重空间编程，最高测试准确率达 54.4%，且 LLM 设计的模型准确率高于同任务下公开的最优 Transformer 模型。当前研究聚焦通用神经架构设计，对 AI 代理工程、评估工具链等领域的直接关联有限，公开内容存在截断。

rss · Hugging Face Daily Papers · 11月18日 00:00

**「为什么重要」** 该研究验证了 LLM 在极低样本与沙箱约束下自主设计有效神经架构的可行性，但当前成果仅覆盖多项选择题任务，尚未证实对 AI 代理相关工程场景的直接价值，需后续研究拓展验证。

**「可关注」** 可关注：权重空间编程场景下，LLM 自主设计的稀疏架构已能在特定任务上超越公开最优 Transformer，可留意该范式对轻量评估架构设计的潜在参考价值。

**标签**: `#eval`, `#architecture`, `#weight-space-programming`

---

<a id="item-agent-engineer-9"></a>
### [ResWAM 改世界动作模型监督范式](https://huggingface.co/papers/2611.19559) ⭐️ 6.0/10

2026 年 11 月 18 日 HF Daily Papers 收录的论文提出 ResWAM 世界动作模型，针对现有世界动作模型（WAM）监督完整未来观测时损失被静态背景主导、难以学习任务相关运动，且依赖大视频生成模型或独立世界模型导致训练推理开销大的问题，提出在冻结 DINOv3 空间开展视觉残差学习，仅监督当前帧到未来帧的特征变化，替代全未来观测监督，可在降低视觉-语言-动作（VLA）策略计算成本的同时提升任务相关运动学习效果。目前仅公开论文摘要，无性能数据、代码发布或完整技术细节，可立即落地的 actionable 价值有限。

rss · Hugging Face Daily Papers · 11月18日 00:00

**「为什么重要」** 该思路跳出了全帧未来预测的监督范式，针对 WAM 的静态背景冗余和计算开销问题给出轻量替代方向，对视觉-语言-动作策略的轻量化落地有参考意义。但需注意目前仅公开摘要，无实证性能数据支撑，效果尚未证实。

**「可关注」** 可关注：冻结预训练视觉空间做残差监督的范式，是否能在降低 VLA 策略世界模型计算开销的同时，避免静态背景对任务相关运动学习的干扰。

**标签**: `#coding-agent`

---

<a id="item-agent-engineer-10"></a>
### [HF 趋势榜：Edge0-145B-NVFP4](https://huggingface.co/Edge0/Edge0-145B-NVFP4) ⭐️ 6.0/10

2026 年 11 月 18 日，Hugging Face 趋势榜新增 Edge0/Edge0-145B-NVFP4 模型，当前 trendingScore 为 123，累计获 496 个点赞。该模型为 145B 参数的 MoE 架构文本生成模型，采用 4-bit NVFP4 量化，标签覆盖 coding-agent、edge-inference，适配编码智能体与边缘推理场景。目前公开信息仅包含基础元数据，无深入技术细节、性能数据或使用指南。

rss · Hugging Face Trending Models · 11月18日 03:59

**「为什么重要」** 该模型作为大参数 MoE 模型完成 4-bit NVFP4 量化，同时标注编码智能体与边缘推理适用标签，对智能体部署优化有潜在参考价值。但目前无公开性能、推理延迟等关键数据，实际部署效果尚未验证。

**「可关注」** 可关注：该模型同时覆盖 coding-agent 与 edge-inference 标签，但未公开量化后的性能、推理延迟等关键指标，可留意其后续发布的部署基准数据。

**标签**: `#coding-agent`

---

## AI 日报
{: #sec-ai-daily .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-daily" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-daily-1"></a>
### [GPT-6.2 Astra 与 Sol 发布](https://openai.com/index/introducing-gpt-6-2-astra-sol) ⭐️ 9.8/10

OpenAI 正式发布 GPT-6.2 Astra 与 Sol 两款模型。新模型专业输出、编码、计算机使用及效率提升，同时成本降低。该更新覆盖 ChatGPT Work、Codex 及 API 产品线。

rss · OpenAI Blog · 11月17日 17:45

**「为什么重要」** 此次更新由 OpenAI 官方发布，同时覆盖 ChatGPT Work、Codex 及 API 三条产品线，涉及能力提升与成本降低两个维度。

**「可关注」** 可关注：ChatGPT Work、Codex 及 API 用户可评估新模型编码、计算机使用及效率提升与成本降低情况。

**标签**: `#model`, `#lab`, `#product`

---

<a id="item-ai-daily-2"></a>
### [ChatGPT 推出 Sales 销售插件](https://openai.com/index/introducing-chatgpt-for-sales) ⭐️ 7.8/10

OpenAI 官方发布 ChatGPT Sales 插件，同步上线 30 余款新增或扩展的合作伙伴插件，覆盖销售工作流场景。该系列插件支持潜在客户研究、销售话术准备、CRM 数据更新等具体功能，可辅助销售团队推进交易流程。

rss · OpenAI Blog · 11月17日 08:00

**「为什么重要」** 这是 OpenAI 首次布局垂直销售场景的 ChatGPT 插件，标志着其企业级产品线从通用工具向行业业务流延伸，为销售团队的现有工具链提供了大模型整合选项。

**「可关注」** 可关注：ChatGPT 垂直场景插件生态的扩展节奏，以及销售类插件对 CRM 等现有企业系统的对接兼容性。

**标签**: `#product`, `#lab`, `#industry`

---

<a id="item-ai-daily-3"></a>
### [GitHub 开源 AHP 跨设备会话协议](https://github.blog/engineering/engineering-principles/building-the-agent-host-protocol-for-sessions-that-continue-across-devices/) ⭐️ 7.8/10

GitHub 官方开源 Agent Host Protocol（AHP）开放标准，用于实现 AI 智能体会话跨设备、跨应用的延续，目前已在 VS Code 的 GitHub Copilot 中完成首次落地。此前各客户端需单独定制集成才能实现会话连续，AHP 通过统一协议让多客户端共享同一套代理、历史与状态，无需 bespoke 集成；AHP 不限定代理具体行为，仅聚焦用户与代理的交互方式，核心围绕 URI 标识的 channel 设计，必选实现 root、session、chat 三个 channel，状态采用服务端仲裁的 reducer 模型，客户端通过发送 action 修改状态或触发副作用，支持弱网下的重连与 action 重放。落地层面，GitHub 为适配 AHP 重构了原有 Copilot Chat 扩展的 harness，原扩展超 40 万行 TypeScript（不含测试），新 VS Code agent host 约 36.9 万行 TypeScript，GitHub agent host 约 30.5 万行 Rust，目前已支持 5 个客户端与 2 个 host 运行。

rss · GitHub Blog · 11月17日 18:20

**「为什么重要」** AHP 作为开放标准，解决了此前各客户端需单独定制集成才能实现会话连续的问题，第三方开发者可基于该协议快速将 AI 代理接入自有应用与工作流，无需重复开发适配逻辑。

**「可关注」** 可关注：AHP 采用服务端仲裁的 reducer 式状态模型，弱网下可通过 action 重放实现会话重连，核心协议设计保持最小化，便于第三方客户端实现。

**标签**: `#product`, `#open-source`, `#industry`

---

<a id="item-ai-daily-4"></a>
### [GitHub 微软试点 AI 辅助开源漏洞修复](https://github.blog/open-source/maintainers/maintainers-dont-need-more-ai-bug-reports-they-need-fixes/) ⭐️ 6.8/10

GitHub 与微软联合开展开源安全试点，使用微软 Codename MDASH 多模型代理扫描系统、GitHub 安全实验室 AI 分诊代理及微软 FORGE Lab 研究员人工核验，向 6 个开源项目维护者推送附带修复建议的私有漏洞报告，而非仅发送原始扫描结果。扫描共标记 9791 个潜在问题，经筛选和人工核验后仅发出 99 份报告；截至 2026 年 11 月 15 日，维护者已修复其中 55 个，14 个修复已进入正式版本。试点仅覆盖 6 个 GitHub Secure Open Source Fund alumni 项目，属于早期探索，样本量有限。

rss · GitHub Blog · 11月17日 18:29

**「为什么重要」** 当前开源维护者普遍被大量 AI 生成的重复、无效漏洞报告淹没，修复能力才是开源安全的瓶颈，该试点直接针对这一痛点，验证了 AI 从“输出问题”转向“辅助修复”的可行性，为开源安全工具的设计提供了新思路。

**「可关注」** 可关注：开源安全场景下，AI 扫描结果经分诊+人工核验后附带修复建议的流程，能大幅降低维护者的筛选成本，提升漏洞修复效率。

**标签**: `#open-source`, `#industry`, `#product`

---