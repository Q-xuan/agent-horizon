---
layout: default
title: "Horizon Summary: 2026-11-27 (EN)"
date: 2026-11-27
lang: en
---

> From 203 items, 11 important content pieces were selected

---

**Agent Harness Architecture**
1. [pydantic-ai v2.76.0 发布](#item-harness-arch-1) ⭐️ 7.8/10
2. [E2B 发布 @e2b/acp 0.1.0](#item-harness-arch-2) ⭐️ 7.8/10
3. [instructor v1.18.0 发布](#item-harness-arch-3) ⭐️ 5.8/10

**AI Agent Engineer**
1. [Nemotron 3.5 Parse 开源](#item-agent-engineer-1) ⭐️ 7.8/10
2. [编码智能体视觉推理超越视频模型](#item-agent-engineer-2) ⭐️ 7.0/10
3. [llama.cpp AMD 基准仪表盘上线](#item-agent-engineer-3) ⭐️ 6.8/10
4. [sqlite3\_rsync 无额外磁盘复制数据库](#item-agent-engineer-4) ⭐️ 6.0/10
5. [Stable Gated DeltaNet-2 对称擦除修复长上下文不稳定](#item-agent-engineer-5) ⭐️ 6.0/10
6. [OS-Omni 跨平台代理基准发布](#item-agent-engineer-6) ⭐️ 6.0/10
7. [DRBench Pro 基准发布](#item-agent-engineer-7) ⭐️ 6.0/10

**AI Daily**
1. [科技爱好者周刊 421 期：AI 造富潮](#item-ai-daily-1) ⭐️ 5.5/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [pydantic-ai v2.76.0 发布](https://github.com/pydantic/pydantic-ai/releases/tag/v2.76.0) ⭐️ 7.8/10

pydantic-ai v2.76.0 发布，引入实时会话中途动态揭示工具的能力。新 \`UpdateTools\` 类型加入 \`RealtimeInput\` 联合，配合 \`RealtimeModelProfile.supports\_tool\_updates\` 标志控制发送。现有连接不会收到工具更新，但 exhaustive 类型检查（如 \`assert\_never\`）会因未处理新分支而失败。同时废弃 \`gemini-2.5-pro\` 和 \`gemini-2.5-flash\`，发出 \`DeprecatedModelWarning\`。

github · dsfaccini · Nov 26, 23:49

**「设计要点」** 实时工具更新按模型能力标志路由，仅向支持更新的连接发送，保持现有会话状态稳定。\`RealtimeInput\` 联合扩展破坏 exhaustive 模式匹配，要求调用方显式处理 \`UpdateTools\` 或主动抛出。

**「改了什么」** 新增 \`UpdateTools\` 实时输入类型及 \`supports\_tool\_updates\` 模型配置，支持实时会话中途推送工具定义。\`FileSystem.read\_file\` 的 \`offset\` 参数改为 1-indexed，\`offset=0\` 抛出异常。\`gemini-2.5-pro\` 和 \`gemini-2.5-flash\` 模型请求触发 \`DeprecatedModelWarning\`。

**Tags**: `#runtime`, `#tools`

---

<a id="item-harness-arch-2"></a>
### [E2B 发布 @e2b/acp 0.1.0](https://github.com/e2b-dev/E2B/releases/tag/%40e2b/acp%400.1.0) ⭐️ 7.8/10

E2B 发布 @e2b/acp 0.1.0，支持在 E2B 沙箱内运行 ACP 兼容 agent（goose、OpenCode、Claude Code 通过 ACP adapter）。新包提供 \`new ACPAgent\(sandbox, command, client\)\` 构造器，调用 \`await agent.start\(\)\` 后通过 stdin/stdout 启动 agent 并连接 ACP client 应用。客户端文件系统与终端能力被关闭，agent 请求这些能力时直接拒绝，确保文件编辑和命令执行仅通过 agent 自身工具在沙箱内完成。

github · github-actions\[bot\] · Nov 26, 12:35

**「设计要点」** 运行时禁用 client 的文件系统与终端能力，强制 agent 使用沙箱内工具执行操作，形成能力边界。Agent 与 client 通过 stdin/stdout 通信，由 \`ACPAgent\` 封装连接生命周期。

**「改了什么」** 新增 \`@e2b/acp\` 0.1.0 包，提供 ACP agent 沙箱运行能力。依赖升级至 e2b@2.65.0。

**Tags**: `#sandbox`, `#tools`, `#permissions`

---

<a id="item-harness-arch-3"></a>
### [instructor v1.18.0 发布](https://github.com/567-labs/instructor/releases/tag/v1.18.0) ⭐️ 5.8/10

567-labs/instructor v1.18.0 ships as a minor release centered on internal refactoring and reliability fixes. The release separates token-budget policy from retry execution, prevents cache mapping-key collisions, and makes raw response logging opt-in to address a security concern. Provider-specific SDK construction moves into dedicated modules for Bedrock and GenAI, while streaming, batch, and multimodal handling receive targeted fixes across OpenAI, Anthropic, Gemini, and Bedrock. No harness-level architecture changes or major new public capabilities appear in this release; it serves primarily as a dependency update for existing instructor users.

github · jxnl · Nov 26, 21:02

**「改了什么」** Separated token-budget policy from retry execution and fixed cache mapping-key collisions to strengthen coverage contracts. Made raw response logging opt-in, excluded disk caches from log scanning, and moved provider SDK construction into respective provider modules for Bedrock and GenAI.

**Tags**: `#runtime`, `#prefix-cache`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [Nemotron 3.5 Parse 开源](https://huggingface.co/blog/nvidia/building-on-nemotron-35-parse-open-data-fine-tunin) ⭐️ 7.8/10

2026年11月26日Hugging Face官方博客发布NVIDIA Nemotron 3.5 Parse的开源技术资源，包含3份合成训练数据集、端到端微调食谱、DFlash2推理加速规范，以及SFT+RLVR训练流程说明。开源数据集共约1938万条标注样本，覆盖图表、表格、多语言OCR场景，均附带生成文档和训练格式。训练流程先通过SFT建立基础文档理解能力，再使用GRPO算法的RLVR优化，开发检查点测试中循环输出占比降低77%，总分从66.24提升至71.38，表格和图表维度分别提升5.18和4.15分。推理优化方面，模型采用NaViT动态输入、GQA-8注意力、MTP+DFlash2推测解码，在单卡H200 BF16环境下，DFlash2在并发1时吞吐为关闭推测解码版本的7.62倍，并发512时为1.52倍，对比上一代Parse 2.0最高提升6.86倍；同时支持单/双/三遍解析机制，可在吞吐和难例提取精度间做权衡，双/三遍解析分别提升2.18、2.46 ParseBench分。上述训练效果为开发检查点结果，非最终发布模型表现。

rss · Hugging Face Blog · Nov 26, 05:05

**「为什么重要」** NVIDIA首次公开了Nemotron 3.5 Parse的完整训练数据、微调流程和推理优化实现，填补了此前文档解析模型技术细节闭源的空白，为RAG和agent场景的文档处理提供了可直接复用的技术参考。目前仅公开了H200环境下的推理性能数据，其他硬件平台的兼容性和性能表现尚未有公开验证。

**「可关注」** 可关注：NVIDIA公开的Parse 3.5技术链路中，SFT+GRPO的RLVR训练可将循环输出占比降低77%，DFlash2推测解码在单卡H200上最高可将文档解析吞吐提升7.62倍，且多遍解析机制支持在吞吐和难例提取精度间做灵活权衡。

**Tags**: `#coding-agent`, `#fine-tuning`, `#inference-optimization`, `#rag`

---

<a id="item-agent-engineer-2"></a>
### [编码智能体视觉推理超越视频模型](https://huggingface.co/papers/2611.34813) ⭐️ 7.0/10

2026 年 11 月 27 日，Hugging Face Daily Papers 收录论文《Solve Vision with Code》，报告在 VBVR-Pro-Bench 基准上，编码智能体通过编写程序渲染答案视频，在相同输入、输出规范与基于规则评估者条件下，优于原生视频生成模型的视觉推理表现。该研究提出符号式评估范式，将视觉推理任务从像素生成转为代码渲染，挑战“视觉原生推理更可靠”的假设。结果仅覆盖该基准，未提及其他任务域或模型规模。

rss · Hugging Face Daily Papers · Nov 27, 00:00

**「为什么重要」** 该研究引入的符号评估范式提供了一种可复现、可拆解的视觉推理评估路径，与当前依赖像素生成的评估方式形成对照。若后续验证成立，可能影响视觉推理系统的能力评估标准与工具链设计。

**「可关注」** 可关注：编码智能体在受控基准上以代码渲染替代像素生成，提示视觉推理评估可从“端到端视频生成”拆分为“程序化渲染+规则校验”的符号范式。

**Tags**: `#eval`, `#coding-agent`

---

<a id="item-agent-engineer-3"></a>
### [llama.cpp AMD 基准仪表盘上线](https://huggingface.co/blog/ggml-org/llamacpp-amd-bench) ⭐️ 6.8/10

2026年11月26日Hugging Face发布公开的llama.cpp基准测试仪表盘，面向AMD Ryzen与Radeon硬件，支持对比不同构建、模型、量化方式的本地推理性能，基准工作流与结果完全公开可查。当前仪表盘支持的硬件为Radeon 8060S（gfx1151）与Radeon AI Pro R9700S（gfx1201），测试指标包含PP512（512输入令牌处理吞吐）与TG128（128令牌生成吞吐），均从上下文深度0开始测量，每周自动运行基准测试，覆盖Inkling 2 Mini、Qwen、Gemma等模型，支持Q4\_K\_M、BF16等多种量化格式。该工具主要面向使用AMD硬件部署llama.cpp做本地推理的开发者，可辅助评估不同配置下的推理性能表现。

rss · Hugging Face Blog · Nov 26, 11:37

**「为什么重要」** 此前AMD硬件上llama.cpp本地推理的性能变化缺乏公开可复现的追踪渠道，该仪表盘填补了这一空白，为对应生态的开发者提供了统一的性能对比参考。

**「可关注」** 可关注公开基准数据存储桶ggml-org/install.sh-benches-data，支持复用结果做自定义分析或与本地运行结果交叉验证。

**Tags**: `#eval`

---

<a id="item-agent-engineer-4"></a>
### [sqlite3\_rsync 无额外磁盘复制数据库](https://simonwillison.net/2026/Nov/26/sqlite3-rsync/) ⭐️ 6.0/10

SQLite 官方工具 sqlite3\_rsync 支持通过 SSH 远程复制数据库快照，无需先创建本地完整副本。该工具于 2024 年 10 月随 SQLite 3.47.0 实验性引入，2025 年 5 月在 SQLite 3.50.0 中增强。Simon Willison 于 2026-11-26 发文指出，相比 backup API 和 VACUUM INTO 需要双倍磁盘空间的限制，sqlite3\_rsync 仅通过哈希比对传输差异页，实现增量同步。若源与副本差异极大，带宽可能略超数据库大小，但通常仅多出几个百分点。

rss · Simon Willison · Nov 26, 06:08

**「为什么重要」** 该工具解决了小磁盘实例上 SQLite 快照备份的空间痛点，对以 SQLite 存储 agent 状态或记忆的场景有直接参考价值。但影响面相对局限，未涉及性能基准或颠覆性架构变化。

**「可关注」** 可关注：在磁盘空间紧张且需跨机同步 SQLite 数据库时，sqlite3\_rsync 提供了一种无需预留双倍空间的替代方案。

**Tags**: `#memory`

---

<a id="item-agent-engineer-5"></a>
### [Stable Gated DeltaNet-2 对称擦除修复长上下文不稳定](https://huggingface.co/papers/2611.34051) ⭐️ 6.0/10

Hugging Face Daily Papers 于 2026-11-27 推介 arXiv 论文《Stable Gated DeltaNet-2: Understanding and Mitigating Recurrent State Instability》。该论文定位 Gated DeltaNet-2（GDN-2）长上下文训练不稳定的根因为擦除操作符不对称，产生非正规擦除算子，其方向增益跨 token 累积，导致循环状态指数增长（即使无新写入）。论文提出 Stable Gated DeltaNet-2，采用对称擦除确保非扩展状态传播，配合衰减调节残差写入保持写入灵活性，并提供理论保证。该工作目前仅为研究预印本，非立即可用的工具、评估基准或协议更新，对构建自定义长上下文 agent 记忆系统的工程师有参考价值。

rss · Hugging Face Daily Papers · Nov 27, 00:00

**「为什么重要」** 该论文从理论上厘清了线性注意力模型循环状态不稳定的机制，为长上下文 agent 记忆设计提供了可验证的修复路径。但实际工程落地效果尚未经大规模系统验证，目前仅具研究参考价值。

**「可关注」** 可关注：使用线性注意力或循环状态的长上下文 agent 记忆系统，若遇到训练中状态异常增长，可检查擦除操作符是否产生非正规算子及方向增益累积。

**Tags**: `#memory`

---

<a id="item-agent-engineer-6"></a>
### [OS-Omni 跨平台代理基准发布](https://huggingface.co/papers/2611.34232) ⭐️ 6.0/10

OS-Omni 是一个跨平台基准测试，用于评估通用计算机使用代理在长时程工作流上的表现，覆盖 Windows、Ubuntu、macOS、iOS、Android 和 Web 六个平台。v1 作为首波发布，包含每平台 48 个任务及 12 个桌面-Android 跨平台工作流，总计 300 个任务。该基准以每波 300 个任务的版本化波浪形式持续扩展，旨在解决现有基准按平台孤立的问题。目前公开材料未包含完整技术细节、性能对比或实现 specifics。

rss · Hugging Face Daily Papers · Nov 27, 00:00

**「为什么重要」** 对于正在构建跨平台代理的工程师，OS-Omni 提供了首个统一的长时程评估框架，可验证代理在真实多 OS 环境中的泛化能力。但 v1 任务规模有限，且跨平台工作流仅覆盖桌面-Android 组合，尚未证实其能否代表完整用户目标。

**「可关注」** 可关注：OS-Omni 采用每波 300 任务的版本化发布，后续波浪的任务分布可能影响代理训练的迭代策略。

**Tags**: `#eval`, `#coding-agent`

---

<a id="item-agent-engineer-7"></a>
### [DRBench Pro 基准发布](https://huggingface.co/papers/2611.34852) ⭐️ 6.0/10

2026-11-27，Hugging Face Daily Papers 发布论文 DRBench Pro，提出面向深度研究代理的知识中心评估基准。该基准将结构化知识覆盖设为主要评估目标。其自动化流程基于维基百科知识树构建本地知识树，采样子图生成研究查询与证据基础评分标准。评分标准对应知识树中的关系，保留被评估知识的层次结构，代理仅接收研究查询作为输入。当前材料为截断摘要，未包含实现细节、性能对比或使用指导，仅值得快速浏览。

rss · Hugging Face Daily Papers · Nov 27, 00:00

**「为什么重要」** 现有基准缺乏对研究报告覆盖哪些研究方向及探索深度的专门知识中心评估。DRBench Pro 试图填补该空白，为构建深度研究代理的团队提供新评估工具。但截断内容未证实其实际效用或与其他基准的对比表现。

**「可关注」** 可关注：该基准的自动化评估流程依赖维基百科知识树，可量化研究广度与深度。但当前材料未提供实现细节或性能数据，尚无法判断工程落地成本。

**Tags**: `#eval`

---

## AI Daily

<a id="item-ai-daily-1"></a>
### [科技爱好者周刊 421 期：AI 造富潮](http://www.ruanyifeng.com/blog/2026/11/weekly-issue-421.html) ⭐️ 5.5/10

阮一峰《科技爱好者周刊》第421期发布，核心话题为AI行业造富现象，同时涵盖小鹏人形机器人展示、维基百科访问量创新低、编程模型排名、防截图功能、重力通信等科技动态。其中Anthropic上市造富的具体数据为：该公司成立于2021年，2023年启动大规模招聘，截至2026年9月有约5300名可分配股票的员工，目前市值为1.17万亿美元，若市值达到1.4万亿美元，2023至2026年入职的员工股票获利中位数分别为1.51亿美元、7900万美元、2600万美元、500万美元，上市后一次性造就约600名亿万富翁，多为二三十岁的年轻员工。其造富核心来自期权，加入越早期权价格越低、份数越多，2024年授予的期权每股1.30美元，上市后价格涨至80美元以上，今年4月授予的期权每股25.91美元，持有半年后股价即翻3倍。

rss · 阮一峰 · Nov 27, 00:10

**「为什么重要」** 这期内容既呈现了AI行业造富的极端案例与底层逻辑，也反映了AI对互联网流量格局、开发工具链的实质性影响，对关注AI行业动态和开发实践的读者有参考价值。

**「可关注」** 可关注：国产模型在综合17个编码基准测试中已进入第一梯队，Qwen 4 Max、Kimi K3.1 Pro、Deepseek V.1 Flash分别位列第10、12、14名。

**Tags**: `#model`, `#lab`, `#industry`, `#product`

---