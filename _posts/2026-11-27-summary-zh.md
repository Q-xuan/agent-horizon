---
layout: default
title: "Horizon Summary: 2026-11-27 (ZH)"
date: 2026-11-27
lang: zh
---

> 从 203 条内容中筛选出 11 条重要资讯。

<nav id="ah-toc" class="ah-toc" aria-label="目录"><span class="ah-toc-title">目录</span><ul><li><a href="#sec-harness-arch"><span class="ah-toc-name">Harness 架构</span><span class="ah-toc-count">3条</span></a></li><li><a href="#sec-agent-engineer"><span class="ah-toc-name">Agent 工程师日报</span><span class="ah-toc-count">7条</span></a></li><li><a href="#sec-ai-daily"><span class="ah-toc-name">AI 日报</span><span class="ah-toc-count">1条</span></a></li></ul></nav>

---

**[Harness 架构](#sec-harness-arch)**
1. [pydantic-ai v2.76.0 发布](#item-harness-arch-1) ⭐️ 7.8/10
2. [E2B @e2b/acp 0.1.0 发布](#item-harness-arch-2) ⭐️ 7.8/10
3. [instructor v1.18.0 发布](#item-harness-arch-3) ⭐️ 5.8/10

**[Agent 工程师日报](#sec-agent-engineer)**
1. [Nemotron 3.5 Parse 开源微调与推理资源](#item-agent-engineer-1) ⭐️ 7.8/10
2. [编码智能体视觉推理超视频模型](#item-agent-engineer-2) ⭐️ 7.0/10
3. [llama.cpp AMD 基准测试看板上线](#item-agent-engineer-3) ⭐️ 6.8/10
4. [sqlite3\_rsync 无额外磁盘复制特性](#item-agent-engineer-4) ⭐️ 6.0/10
5. [Stable Gated DeltaNet-2 论文发布](#item-agent-engineer-5) ⭐️ 6.0/10
6. [OS-Omni 跨平台基准发布](#item-agent-engineer-6) ⭐️ 6.0/10
7. [DRBench Pro 评估深度研究代理](#item-agent-engineer-7) ⭐️ 6.0/10

**[AI 日报](#sec-ai-daily)**
1. [421 期周刊：Anthropic 造富](#item-ai-daily-1) ⭐️ 5.5/10

---

## Harness 架构
{: #sec-harness-arch .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-harness-arch" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-harness-arch-1"></a>
### [pydantic-ai v2.76.0 发布](https://github.com/pydantic/pydantic-ai/releases/tag/v2.76.0) ⭐️ 7.8/10

pydantic-ai v2.76.0 发布，核心新增实时会话中途动态揭示工具能力。通过\`UpdateTools\`类型与\`RealtimeModelProfile.supports\_tool\_updates\`标志控制，仅向支持工具更新的模型连接发送更新，\`DEFAULT\_REALTIME\_PROFILE\`默认关闭该能力。\`RealtimeInput\`联合类型扩展后，现有穷尽匹配（如\`assert\_never\`）会破坏类型检查，需显式处理\`UpdateTools\`分支。同时，\`gemini-2.5-pro\`与\`gemini-2.5-flash\`请求现在触发\`DeprecatedModelWarning\`，\`FileSystem.read\_file\`的\`offset\`参数改为 1-indexed 且\`offset=0\`抛出异常。

github · dsfaccini · 11月26日 23:49

**「设计要点」** 实时工具更新采用模型能力声明机制，\`supports\_tool\_updates\`为 False 的连接不会收到\`UpdateTools\`消息，避免向不支持的模型推送。历史修剪场景下，\`result.conversation\`保留运行期间添加的全部消息，若需传递压缩历史应改用\`result.all\_messages\(\)\`，这影响多轮运行间的状态传递设计。

**「改了什么」** 实时会话新增\`UpdateTools\`类型与\`RealtimeModelProfile.supports\_tool\_updates\`标志，支持中途动态揭示工具；\`FileSystem.read\_file\`的\`offset\`改为 1-indexed 且\`offset=0\`抛出异常。\`gemini-2.5-pro\`和\`gemini-2.5-flash\`请求触发\`DeprecatedModelWarning\`；新增\`GoogleInteractionsModel\`与\`CodeMode\(allow\_final\_output=True\)\`。

**标签**: `#runtime`, `#tools`

---

<a id="item-harness-arch-2"></a>
### [E2B @e2b/acp 0.1.0 发布](https://github.com/e2b-dev/E2B/releases/tag/%40e2b/acp%400.1.0) ⭐️ 7.8/10

E2B 发布 @e2b/acp 0.1.0，支持在 E2B sandbox 内运行 ACP 兼容 agent（goose、OpenCode、Claude Code 通过 ACP adapter）。通过 new ACPAgent\(sandbox, command, client\) 初始化，await agent.start\(\) 通过 stdin/stdout 启动 agent 并连接 ACP client。客户端文件系统与终端能力被强制关闭，agent 请求这些能力时直接拒绝，确保 agent 只能通过 sandbox 内自有工具执行文件编辑和命令运行。

github · github-actions\[bot\] · 11月26日 12:35

**「设计要点」** 运行时通过 stdin/stdout 桥接 agent 与 ACP client，权限模型在客户端侧禁用文件系统和终端能力，由 sandbox 侧统一拦截拒绝，实现工具调用边界隔离。

**「改了什么」** 新增 @e2b/acp 包，提供 ACPAgent 类用于在 E2B sandbox 中托管 ACP 兼容 agent。依赖升级至 e2b@2.65.0。

**「评论」** 无社区评论。

**标签**: `#sandbox`, `#tools`, `#permissions`

---

<a id="item-harness-arch-3"></a>
### [instructor v1.18.0 发布](https://github.com/567-labs/instructor/releases/tag/v1.18.0) ⭐️ 5.8/10

instructor 发布 v1.18.0。本次小版本以内部重构和修复为主，包括缓存键冲突修复、token-budget 策略与重试逻辑分离，以及 Bedrock、GenAI 等提供者模块结构调整。无新增 harness 级能力，仅作为依赖更新影响使用 instructor 的 agent 系统。

github · jxnl · 11月26日 21:02

**「改了什么」** 缓存层修复映射键冲突并强化覆盖契约；核心层将 token-budget 策略从重试执行中分离；Bedrock 与 GenAI 提供者各自收拢 SDK 构造与请求配置策略。流式传输修复 Unicode 控制字符保留与字段别名解析；安全层面将原始响应日志改为显式 opt-in 并忽略磁盘缓存。

**标签**: `#runtime`, `#prefix-cache`

---

## Agent 工程师日报
{: #sec-agent-engineer .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-agent-engineer" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-agent-engineer-1"></a>
### [Nemotron 3.5 Parse 开源微调与推理资源](https://huggingface.co/blog/nvidia/building-on-nemotron-35-parse-open-data-fine-tunin) ⭐️ 7.8/10

2026 年 11 月 26 日，NVIDIA 联合 Hugging Face 博客发布文档解析模型 Nemotron 3.5 Parse 的开源配套资源，包括 3 份合成训练数据集、端到端微调食谱、DFlash2 推理加速规范，以及 SFT+RLVR 训练流程说明。关键细节：3 份数据集分别为 990 万示例的 Synthetic Charts V1、100 万示例的 Synthetic Tables V1、790 万示例的 OCR Synthetic Multilingual v2，均含图像、标注与生成文档；模型架构上，Parse 3.5 采用 NaViT 动态矩形输入、压缩视觉 token 作为因果前缀、GQA-8 注意力降低缓存占用；DFlash2 在实测 32 token 配置下平均接受约 14 个草稿 token，单 H200 BF16 环境下，并发 1 时吞吐较关闭推测解码的 Parse 3.5 提升 7.62 倍，并发 512 时提升 1.52 倍，达到 20.44 页/秒，为 Parse 2.0 的 6.86 倍；SFT+RLVR 流程可将循环输出页数从 126 降至 29，9000 token 截断输出从 185 降至 35，整体评分从 66.24 升至 71.38。该资源面向构建 RAG、agent 文档处理工具链的工程师开放。

rss · Hugging Face Blog · 11月26日 05:05

**「为什么重要」** 本次发布首次公开了 Nemotron 3.5 Parse 的完整训练数据、可复现的微调与强化学习流程，以及可落地的推理加速方案，降低了文档解析模型在 RAG 和 agent 场景的定制门槛；目前尚未有公开证据验证这些资源在不同文档类型上的泛化效果，以及是否能完全复现官方公布的性能指标。

**「可关注」** 可关注：官方公开的 SFT+RLVR 微调食谱、三份开源训练数据集，以及 DFlash2 推理加速方案可直接用于文档解析模型的定制与部署优化；多轮重处理机制可在吞吐和复杂区域提取精度间做权衡。

**标签**: `#coding-agent`, `#fine-tuning`, `#inference-optimization`, `#rag`

---

<a id="item-agent-engineer-2"></a>
### [编码智能体视觉推理超视频模型](https://huggingface.co/papers/2611.34813) ⭐️ 7.0/10

2026-11-27 Hugging Face Daily Papers 收录论文报告，在 VBVR-Pro-Bench 基准上，编码智能体通过编写程序渲染答案视频，在相同输入、输出规范和评估条件下，表现优于原生视频生成模型。该研究首次在相同条件下对比符号路径（代码渲染）与原生视觉路径（视频生成）的视觉推理可靠性。论文未公开具体性能数值或统计显著性。

rss · Hugging Face Daily Papers · 11月27日 00:00

**「为什么重要」** 该研究挑战&quot;视觉推理应在像素空间原生进行&quot;的假设，为 agent 能力评估提供可复现的符号基准路径。对 coding agent 和 harness 开发者而言，代码生成可能比视频生成更适合作为视觉推理的可靠执行媒介。

**「可关注」** 可关注：当前视觉推理评估中，代码渲染路径与视频生成模型的对比基准尚未标准化，该研究仅提供概念验证。

**标签**: `#eval`, `#coding-agent`

---

<a id="item-agent-engineer-3"></a>
### [llama.cpp AMD 基准测试看板上线](https://huggingface.co/blog/ggml-org/llamacpp-amd-bench) ⭐️ 6.8/10

2026 年 11 月 26 日，Hugging Face 发布公开的 llama.cpp AMD Ryzen/Radeon 硬件基准测试看板，支持开发者对比不同构建、模型、量化方式的本地推理性能，基准工作流与底层结果完全公开。当前支持的硬件为 Radeon 8060S（gfx1151）和 Radeon AI Pro R9700S（gfx1201），测试指标包含 PP512（512 输入令牌处理吞吐，无生成）与 TG128（128 令牌生成吞吐，无预存上下文），均从上下文深度 0 开始测量。基准测试使用 llama-bench 工具运行，开启/关闭 Flash Attention，每个配置重复 10 次，每周自动执行，数据存储于公开的 ggml-org/install.sh-benches-data 存储桶，可直接下载复用。该工具面向使用 AMD 平台部署 llama.cpp 做本地推理的开发者，方便其追踪性能变化、评估方案效果。

rss · Hugging Face Blog · 11月26日 11:37

**「为什么重要」** 此前 AMD 平台 llama.cpp 本地推理性能缺乏公开可复现的跨构建、跨量化对比基准，该看板填补了这块空白，开发者无需自行搭建测试环境即可获取标准化的性能参考数据。

**「可关注」** 可关注：看板提供的 jsonl 格式原始数据完全公开，开发者可直接下载用于自行复现测试或对比本地运行结果。

**标签**: `#eval`

---

<a id="item-agent-engineer-4"></a>
### [sqlite3\_rsync 无额外磁盘复制特性](https://simonwillison.net/2026/Nov/26/sqlite3-rsync/) ⭐️ 6.0/10

2026 年 11 月 26 日从业者 Simon Willison 发布文章，重提 SQLite 官方工具 sqlite3\_rsync 的核心能力，他曾在 2024 年 10 月该工具首次发布时介绍过其基础用法。该工具 2024 年 10 月随 SQLite 3.47.0 以实验性功能上线，2025 年 5 月在 SQLite 3.50.0 中完成增强，支持通过 SSH 远程复制 SQLite 数据库快照，无需先创建完整本地副本，也支持类似 rsync 的增量同步，仅传输差异页内容。对比传统快照方法（backup API、VACUUM INTO）需要额外磁盘空间存储完整副本的限制，sqlite3\_rsync 解决了小磁盘环境下的快照复制痛点；若源端与副本初始差异极大，哈希交换 overhead 会导致总带宽略超数据库大小，最多多出百分之几，对使用 SQLite 存储 agent 状态或记忆的工程师有参考价值。

rss · Simon Willison · 11月26日 06:08

**「为什么重要」** 该工具填补了 SQLite 小磁盘环境下无额外本地存储完成远程快照同步的能力空白，是当前少有的官方提供的轻量 SQLite 复制方案。目前仅见个人实践提及，尚无公开性能对比数据或大规模应用案例验证其稳定性，影响面仍较窄。

**「可关注」** 可关注：磁盘资源受限的 SQLite 使用场景中，可优先验证 sqlite3\_rsync 替代传统 backup API 或 VACUUM INTO 的可行性。

**标签**: `#memory`

---

<a id="item-agent-engineer-5"></a>
### [Stable Gated DeltaNet-2 论文发布](https://huggingface.co/papers/2611.34051) ⭐️ 6.0/10

2026-11-27，Hugging Face Daily Papers 收录 arXiv 论文，提出 Stable Gated DeltaNet-2。该工作定位 Gated DeltaNet-2（GDN-2）长上下文训练不稳定的根因：擦除阶段的非对称读写方向产生非正规擦除算子，其方向增益跨 token 累积，即使无新写入也会触发循环状态指数增长。修复方案采用对称擦除保证非扩展状态传播，并引入衰减调节残差写入保持写入灵活性，附带理论稳定性保证。该研究对构建长上下文 agent 记忆系统的工程师有参考价值，但并非立即可用的工具、评估基准或协议更新。

rss · Hugging Face Daily Papers · 11月27日 00:00

**「为什么重要」** 论文首次从算子对称性角度解释 GDN-2 的长上下文训练崩溃机制，并给出理论可证的安全修复。对正在评估线性注意力方案的长上下文 agent 记忆系统而言，这提供了状态稳定性设计的参考基线，但实际工程收益仍需等待实现验证。

**「可关注」** 可关注：长上下文线性注意力模型的循环状态稳定性设计，特别是擦除算子对称性对状态传播的影响。

**标签**: `#memory`

---

<a id="item-agent-engineer-6"></a>
### [OS-Omni 跨平台基准发布](https://huggingface.co/papers/2611.34232) ⭐️ 6.0/10

Hugging Face Daily Papers 于 2026-11-27 介绍 OS-Omni，一个面向通用计算机使用智能体的跨平台长期工作流基准测试。该基准覆盖 Windows、Ubuntu、macOS、iOS、Android 与 Web 六类环境，首版 v1 包含每平台 48 个任务及 12 组桌面-Android 跨平台工作流。现有基准多隔离单一环境，OS-Omni 试图验证单一智能体跨操作系统与持久应用状态执行长期任务的能力。当前材料未披露具体性能数据或实现细节。

rss · Hugging Face Daily Papers · 11月27日 00:00

**「为什么重要」** 对 coding agent 工程师而言，OS-Omni 提供了首个标准化跨平台长期工作流评估框架，可直接检验智能体在真实多设备场景中的泛化能力与状态管理能力。当前仅发布 v1，后续波浪版本将扩展至 300 任务规模。

**「可关注」** 可关注：OS-Omni v1 的 12 组桌面-Android 跨平台工作流，可作为测试智能体状态保持与跨设备协同能力的首批标准化用例。

**标签**: `#eval`, `#coding-agent`

---

<a id="item-agent-engineer-7"></a>
### [DRBench Pro 评估深度研究代理](https://huggingface.co/papers/2611.34852) ⭐️ 6.0/10

Hugging Face Daily Papers 于 2026-11-27 发布论文摘要，介绍 DRBench Pro，一个面向深度研究代理的知识中心基准测试。该基准通过基于维基百科知识树的自动化流水线，构建本地知识树并采样子图生成研究查询和证据 grounded 评分标准，每个评分标准对应知识树中的一个关系以保持知识结构。现有基准测试评估报告质量多维度，但缺乏对结构化知识覆盖的专门评估。材料为截断摘要，缺少实现细节、性能比较和使用指导，仅建议相关团队快速浏览。

rss · Hugging Face Daily Papers · 11月27日 00:00

**「为什么重要」** 该基准填补了深度研究代理评估在结构化知识覆盖方面的空白，为相关团队提供了新的自动化评估工具。但截断摘要未提供性能数据或使用指南，实际可用性待验证。

**「可关注」** 可关注：该基准基于维基百科知识树子图采样的自动化流水线，为生成研究查询和证据 grounded 评分标准提供了可复现的结构化框架。

**标签**: `#eval`

---

## AI 日报
{: #sec-ai-daily .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-daily" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-daily-1"></a>
### [421 期周刊：Anthropic 造富](http://www.ruanyifeng.com/blog/2026/11/weekly-issue-421.html) ⭐️ 5.5/10

阮一峰《科技爱好者周刊》第 421 期发布，涵盖 AI 造富、人形机器人、网站流量、编程模型排名等科技动态。根据@AndrewBenson 的统计，Anthropic 成立于 2021 年，2023 年启动大规模招聘，截至 2026 年 9 月有约 5300 名可分配股票的员工，若市值达 1.4 万亿美元，2023 年入职员工股票获利中位数达 1.51 亿美元，上市一次性造就约 600 名亿万富翁，其中大部分仅二三十岁，数量超过洛杉矶全市现有亿万富翁人数；其 2024 年授予的期权每股 1.30 美元，上市后股价达每股 80 余美元，今年 4 月授予的期权每股 25.91 美元，持有半年后股价翻 3 倍。维基百科 2025 年以来真实人类访问量持续下滑创近年新低，综合 17 个编码基准的编程模型排名发布，前三为 Fable 5.2、Astra 6.2、Neon 4，国产模型最高为 Qwen 4 Max（第 10 位），此外小鹏展示人形机器人、Signal 推出防截图功能、Ladybird 浏览器发布 alpha 版等内容也在本期提及。

rss · 阮一峰 · 11月27日 00:10

**「为什么重要」** Anthropic 的造富案例直观呈现了 AI 行业高估值下的股权红利分配逻辑，同时维基百科访问量下滑、编程模型排名更新也为从业者提供了行业趋势参考。

**「可关注」** 可关注：综合 17 个编码基准的编程模型排名，其中国产模型 Qwen 4 Max、Kimi K3.1 Pro、Deepseek V.1 Flash 分别位列第 10、12、14 位，可作为编码场景的模型选型参考。

**标签**: `#model`, `#lab`, `#industry`, `#product`

---