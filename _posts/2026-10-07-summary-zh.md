---
layout: default
title: "Horizon Summary: 2026-10-07 (ZH)"
date: 2026-10-07
lang: zh
---

> 从 186 条内容中筛选出 23 条重要资讯。

---

**Harness 架构**
1. [Claude Code v2.1.292](#item-harness-arch-1) ⭐️ 8.3/10
2. [gemini-cli v0.64.0-preview.0 发布](#item-harness-arch-2) ⭐️ 7.8/10
3. [Claude Code v2.1.291 修复会话回归](#item-harness-arch-3) ⭐️ 6.8/10
4. [gemini-cli v0.65.0-nightly 修复会话与权限](#item-harness-arch-4) ⭐️ 6.3/10
5. [Gemini CLI v0.63.0 发布](#item-harness-arch-5) ⭐️ 6.3/10
6. [microsoft/semantic-kernel released python-1.45.0](#item-harness-arch-6) ⭐️ 6.3/10
7. [microsoft/semantic-kernel released dotnet-1.81.0](#item-harness-arch-7) ⭐️ 6.3/10

**Agent 工程师日报**
1. [自生成反馈破坏 TTT 长时程适应](#item-agent-engineer-1) ⭐️ 8.0/10
2. [OpenAI Decisions API 进入公测](#item-agent-engineer-2) ⭐️ 7.5/10
3. [Introducing Mistral Large 4: Le chonk](#item-agent-engineer-3) ⭐️ 7.5/10
4. [HF daily paper: Harness Engineering for Software Engineering via Modular Executable Dev-Primitives](#item-agent-engineer-4) ⭐️ 7.5/10
5. [OSWorld-Pro 过程化评估 CUAs](#item-agent-engineer-5) ⭐️ 7.5/10
6. [EmbeddingGemma 2: An open, lightweight multimodal embedding model](#item-agent-engineer-6) ⭐️ 7.0/10
7. [llm-mistral 0.16 发布](#item-agent-engineer-7) ⭐️ 6.8/10
8. [LMBuild 测 Agent 3D 建造](#item-agent-engineer-8) ⭐️ 6.0/10
9. [EmbeddingGemma 2 开源](#item-agent-engineer-9) ⭐️ 6.0/10
10. [I gave a 21M model a 6.4B-parameter lookup table. It matches a 114M dense model and runs with the table on an SSD \(RX 9070\)](#item-agent-engineer-10) ⭐️ 5.5/10

**AI 日报**
1. [OpenAI 公开数学 AI 新结果](#item-ai-daily-1) ⭐️ 10.0/10
2. [OpenAI 与 Ironclad 训练合同 agent](#item-ai-daily-2) ⭐️ 8.3/10
3. [Building Git infrastructure for agent-scale development](#item-ai-daily-3) ⭐️ 7.8/10
4. [Jump Trading 扩展量化研究](#item-ai-daily-4) ⭐️ 6.8/10
5. [OpenAI 扩展 Atlassian 合作](#item-ai-daily-5) ⭐️ 6.8/10
6. [Meta nts.meta.com 支持 NTS](#item-ai-daily-6) ⭐️ 6.8/10

---

## Harness 架构

<a id="item-harness-arch-1"></a>
### [Claude Code v2.1.292](https://github.com/anthropics/claude-code/releases/tag/v2.1.292) ⭐️ 8.3/10

Claude Code v2.1.292 发布。\`claude plugin install\` 新增 \`--marketplace &lt;source&gt;\`，可在同一套策略检查下自动补全 marketplace 再安装插件。Agent 工具加入 \`effort\` 参数，按指定力度运行子代理；新增 \`CLAUDE\_CODE\_OVERLOADED\_RETRY\_BASE\_DELAY\_MS\` 调整 529 重试的基础退避时长。mod 侧新增 \`prompt.autocomplete\` 事件、\`agent.spawn\` 工作流代理拒绝能力，以及 \`$.model.complete\` 的 prompt 缓存。

github · ashwin-ant · 10月6日 18:59

**「设计要点」** 工具层与 mod 钩子继续扩展：插件安装复用 marketplace 策略检查，子代理支持 effort 分级，\`$.model.complete\` 支持按块前缀缓存。权限与沙箱收紧，覆盖 UNC 路径、自动模式绕过、托管设置缓存篡改及 MCP 工具名超长导致的全局失败。

**「改了什么」** 新增能力集中在插件安装链路、子代理力度控制、mod 钩子与模型请求缓存。其余大量条目为安全与稳定性修复，包括沙箱越权读取、计划模式恢复、云会话与插件加载缺陷，不构成接口变化。

**标签**: `#runtime`, `#tools`, `#subagents`, `#permissions`, `#prefix-cache`

---

<a id="item-harness-arch-2"></a>
### [gemini-cli v0.64.0-preview.0 发布](https://github.com/google-gemini/gemini-cli/releases/tag/v0.64.0-preview.0) ⭐️ 7.8/10

gemini-cli v0.64.0-preview.0 发布。协议层接入 a2a V1→V2 设置迁移，acp 桥接 PromptResponse.usage 并发出 usage\_update 通知。运行时将文件工具序列化并改为原子写入，headless 模式开始传播解析后的文件夹信任状态。另修复 CPU 挂起、状态损坏恢复、Ctrl+C 取消传递等稳定性问题。

github · gemini-cli-robot · 10月6日 20:26

**「设计要点」** 文件工具操作被序列化，写入原子化，规避并发冲突。headless 模式向下传递解析后的文件夹信任状态，收紧权限边界。ChatRecordingService 改用仅追加增量补丁与有界历史窗口，限制内存增长。

**「改了什么」** 相对 v0.63.0-preview.0，新增 a2a V1→V2 设置迁移与 acp usage 桥接。文件工具从并行执行改为串行原子写入。headless 信任传播、状态原子持久化、Ctrl+C 紧急中止链路均得到修复。

**标签**: `#runtime`, `#tools`, `#permissions`

---

<a id="item-harness-arch-3"></a>
### [Claude Code v2.1.291 修复会话回归](https://github.com/anthropics/claude-code/releases/tag/v2.1.291) ⭐️ 6.8/10

Claude Code v2.1.291 发布补丁，修复两处回归。2.1.290 引入的云会话可能丢弃权限提示答案的问题得到修复；2.1.288 引入的退出时丢失会话末尾消息的问题也一并解决。此版本不引入新功能或架构调整。

github · ashwin-ant · 10月6日 03:55

**「设计要点」** 权限提示的应答回传依赖云会话链路，退出时的消息持久化则关系运行时状态落盘。两处回归分别触及权限交互与会话记忆的完整性。

**「改了什么」** 修复 2.1.290 中云会话丢弃权限提示答案的回归；修复 2.1.288 中退出时丢失会话最后消息的回归。

**标签**: `#permissions`, `#runtime`, `#memory`

---

<a id="item-harness-arch-4"></a>
### [gemini-cli v0.65.0-nightly 修复会话与权限](https://github.com/google-gemini/gemini-cli/releases/tag/v0.65.0-nightly.20261007.gef59c532f) ⭐️ 6.3/10

google-gemini/gemini-cli 发布 v0.65.0-nightly.20261007.gef59c532f。本次为 nightly 修订版，聚焦安全与会话恢复。CLI 在不可信文件夹中强制只读工作区设置；核心层修复恢复会话时的重复工具响应轮次，并阻止快速退出删除已恢复会话历史。OAuth 回调 iss 参数验证对齐 RFC 9207。

github · gemini-cli-robot · 10月7日 01:31

**「设计要点」** 权限层将不可信文件夹的工作区锁定为只读，限制工具写入路径。会话恢复机制调整了历史与工具响应的重放逻辑，避免状态错乱。

**「改了什么」** 相对 v0.64.0-nightly，新增不可信文件夹只读强制；修复恢复会话时的重复工具响应与历史误删；OAuth 回调验证对齐 RFC 9207；Ctrl+O 展开不再触发终端清屏与滚动重置。

**标签**: `#runtime`, `#permissions`, `#sandbox`, `#tools`

---

<a id="item-harness-arch-5"></a>
### [Gemini CLI v0.63.0 发布](https://github.com/google-gemini/gemini-cli/releases/tag/v0.63.0) ⭐️ 6.3/10

Gemini CLI v0.63.0 发布，为补丁版本。核心修复是限制长时运行 agent 循环中的工具输出大小，并优化内存生命周期。同时修复 MCP 配置错误提示、stdin 恢复、临时目录清理、认证死循环及非交互模式下自主计划执行等问题。无破坏性变更，未新增能力或调整架构。

github · gemini-cli-robot · 10月6日 20:38

**「设计要点」** 工具输出边界与内存生命周期优化针对长时运行 agent 循环，属于运行时资源管理层面的修复。

**「改了什么」** 相对 v0.62.0，v0.63.0 限制了长时运行 agent 循环中的工具输出大小并优化内存生命周期，同时修复 MCP 配置错误提示、stdin 恢复及认证死循环等稳定性问题。

**标签**: `#runtime`, `#memory`, `#tools`, `#mcp`

---

<a id="item-harness-arch-6"></a>
### [microsoft/semantic-kernel released python-1.45.0](https://github.com/microsoft/semantic-kernel/releases/tag/python-1.45.0) ⭐️ 6.3/10

Semantic Kernel 1.45.0 is a routine maintenance release with minor breaking changes and dependency updates, lacking significant architectural innovations.

github · eavanvalkenburg · 10月6日 12:54

**标签**: `#runtime`, `#tools`, `#permissions`

---

<a id="item-harness-arch-7"></a>
### [microsoft/semantic-kernel released dotnet-1.81.0](https://github.com/microsoft/semantic-kernel/releases/tag/dotnet-1.81.0) ⭐️ 6.3/10

Semantic Kernel .NET 1.81.0 is a routine minor release with incremental plugin, file handling, and vector store filtering improvements.

github · dmytrostruk · 10月6日 16:34

**标签**: `#runtime`, `#tools`, `#permissions`, `#memory`

---

## Agent 工程师日报

<a id="item-agent-engineer-1"></a>
### [自生成反馈破坏 TTT 长时程适应](https://huggingface.co/papers/2610.05076) ⭐️ 8.0/10

Hugging Face Daily Papers 收录论文，验证自生成反馈会破坏 TTT 的长时程适应。论文在 128K-token 流上运行三个 TTT-E2E 配置（125M、760M、3B）。保留生成文本更新后，模型对独立人类文本的预测变差。Adam 更新 Qwen3-4B 现有权重时复现同样失败。相同更新机制读真实文本可改进，排除写作本身问题。三个匹配比较显示，Fixed Generation 用冻结模型生成训练块，在 125M 和 760M 上消除超过 98% 的损害。

rss · Hugging Face Daily Papers · 10月7日 01:58

**「为什么重要」** 做 agent memory 与 self-improvement loop 的工程师可拿到量化基线：自生成反馈在 128K-token 流上足以让 TTT 退化。Fixed Generation 的 98% 消除率目前仅在 125M 和 760M 上报告，3B 与 Qwen3-4B 的对应数据未给出。

**「可关注」** 可关注：设计长时程 self-improvement loop 时，若用 TTT 更新权重，需把生成端与学习端解耦——用冻结模型产训练块，避免模型被自身退化输出污染。

**标签**: `#memory`, `#eval`, `#harness`, `#observability`

---

<a id="item-agent-engineer-2"></a>
### [OpenAI Decisions API 进入公测](https://developers.openai.com/api/docs/guides/decisions) ⭐️ 7.5/10

OpenAI 的 Decisions API 进入公开测试，官方开发者文档已发布，接口端点为 \`https://api.openai.com/v1/decisions\`，示例请求调用 \`gpt-6-luna\` 模型。社区开发者对比了该 API 与手写 prompt 分类方案：成本持平（每百万 token 0.10 美元），速度比 responses API 快约 10 倍，质量与 luna 基本相当。另有开发者通过 OpenRouter 对 Jev 和 Mercury Decide 发起少于 600 次调用的初步评估，结果尚未收敛。

hackernews · chiefstorm · 10月6日 20:57 · [社区讨论](https://news.ycombinator.com/item?id=49984025)

**「为什么重要」** 对 coding agent 与 harness 工程师而言，这提供了一个可能替代 prompt 分类的原生决策接口，在延迟敏感的编排环节有直接用处。但当前对比数据多来自个人测试，尚缺公开基准。

**「可关注」** 可关注：Decisions API 在相同 token 成本下将决策延迟压低约一个数量级，适合对响应速度敏感的 agent 编排环节，但需自行验证在具体任务上的质量与成本表现。

**「评论」** HN 讨论中，开发者通过 OpenRouter 对比了 Jev 与 Mercury Decide，认为 Jev 胜在性价比，Mercury Decide 则因 dLLM 路线具备吸引力。也有观点指出，快速的 yes/no/confidence 输出正是当前市场所需，大厂正围绕低价决策模型展开竞争。

**标签**: `#eval`, `#harness`, `#orchestration`, `#coding-agent`

---

<a id="item-agent-engineer-3"></a>
### [Introducing Mistral Large 4: Le chonk](https://simonwillison.net/2026/Oct/6/le-chonk/) ⭐️ 7.5/10

Mistral Large 4 preview released: 1T parameter / 49B active model with only &\#x27;none&\#x27; and &\#x27;high&\#x27; reasoning levels, open weights promised by end of month.

rss · Simon Willison · 10月6日 20:18

**标签**: `#coding-agent`, `#eval`, `#harness`, `#observability`

---

<a id="item-agent-engineer-4"></a>
### [HF daily paper: Harness Engineering for Software Engineering via Modular Executable Dev-Primitives](https://huggingface.co/papers/2610.07832) ⭐️ 7.5/10

该论文提出 Dev-Primitives，一种将仓库组件转化为可执行抽象以缓解长程软件工程任务中上下文爆炸和语义漂移的模块化方案。

rss · Hugging Face Daily Papers · 10月7日 00:00

**标签**: `#coding-agent`, `#harness`, `#memory`, `#orchestration`

---

<a id="item-agent-engineer-5"></a>
### [OSWorld-Pro 过程化评估 CUAs](https://huggingface.co/papers/2609.24890) ⭐️ 7.5/10

Hugging Face Daily Papers 于 2026-10-07 收录 OSWorld-Pro，当前 20 upvotes。该基准含 300+ 任务、2800+ 子目标，基于 67,000+ 条人工标注，面向 Computer-Use Agents \(CUAs\) 做过程化评估。它用与人类对齐的 LLM-Judges 判定子目标完成度，取代 OSWorld 只验最终交付物的功能验证。论文未公布跨模型跑分，子目标判定与人工标注的一致性仍待第三方复核。

rss · Hugging Face Daily Papers · 10月7日 01:58

**「为什么重要」** CUAs 在数百步后只交最终答卷，失败原因常被端到端验证抹平。OSWorld-Pro 把评估下沉到子目标，让键盘输入错误与图形界面点击错误可分别归因，直接影响调试与改进路径。

**「可关注」** 可关注：接入 OSWorld-Pro 后，CUA 评估需从功能验证器切换为子目标级 LLM-Judges，并准备对齐 67,000 条人工标注的判定标准。

**标签**: `#eval`, `#coding-agent`, `#observability`

---

<a id="item-agent-engineer-6"></a>
### [EmbeddingGemma 2: An open, lightweight multimodal embedding model](https://blog.google/innovation-and-ai/technology/developers-tools/embeddinggemma-2/) ⭐️ 7.0/10

Google releases EmbeddingGemma 2, an open-source multimodal embedding model that agent engineers can use for local RAG and memory systems.

hackernews · ilreb · 10月6日 16:03 · [社区讨论](https://news.ycombinator.com/item?id=49980487)

**标签**: `#memory`, `#toolchain`, `#multimodal`

---

<a id="item-agent-engineer-7"></a>
### [llm-mistral 0.16 发布](https://github.com/simonw/llm-mistral/releases/tag/0.16) ⭐️ 6.8/10

simonw 发布 llm-mistral 0.16。插件支持推理模型，覆盖 Mistral Large 4。用 \`-o reasoning\_effort\` 调节推理级别，可选 \`none\`、\`minimal\`、\`low\`、\`medium\`、\`high\`、\`xhigh\`，具体取决于模型。底层改用官方 \`mistralai\` Python 库。破坏性变更：\`safe\_mode\` 已移除，请改用 \`-o safe\_prompt 1\`，与 Mistral API 命名对齐。Voxtral 音频模型新增本地 MP3 附件支持，此前仅支持 URL。

github · simonw · 10月6日 21:32

**「为什么重要」** 调用 Mistral 的 llm 用户需更新参数写法。推理力度可调和本地音频附件直接改变调用方式。

**「可关注」** 可关注：升级到 0.16 必须替换 \`safe\_mode\`；调用推理模型时需按模型支持选择 \`reasoning\_effort\` 档位。

**标签**: `#harness`, `#coding-agent`, `#tools`

---

<a id="item-agent-engineer-8"></a>
### [LMBuild 测 Agent 3D 建造](https://huggingface.co/papers/2610.04292) ⭐️ 6.0/10

Hugging Face Daily Papers 于 2026-10-07 收录 LMBuild 论文。该基准评估 LLM Agent 生成物理可建造且功能性 3D 结构的能力，针对现有评测重几何质量、轻物理可实现性的缺口。LMBuild 将生成对象表示为包含部件分解、关节、材料与装配顺序的组装结构，并提供含交互式环境的统一框架，Agent 可在其中调用工具完成检索。论文页显示 27 次 upvotes；目前仅公开摘要，缺少可复现的性能对比数据，影响面集中于 3D 与具身生成场景。

rss · Hugging Face Daily Papers · 10月7日 01:58

**「为什么重要」** 对做 3D 与具身生成的 Agent 工程师，LMBuild 提供了把物理可实现性纳入评测的参考框架。其实际区分度与跨场景通用性尚未经可复现数据验证。

**「可关注」** 可关注：LMBuild 用部件分解、关节、材料与装配顺序刻画 3D 对象，把评测从几何质量推进到物理可实现性；若做具身或 3D 生成 Agent，可对照其框架检查自身评测是否覆盖建造约束。

**标签**: `#eval`, `#harness`

---

<a id="item-agent-engineer-9"></a>
### [EmbeddingGemma 2 开源](https://www.reddit.com/r/LocalLLaMA/comments/1wz7faa/introducing_embeddinggemma_2_a_bestinclass_open/) ⭐️ 6.0/10

Google DeepMind 开源 EmbeddingGemma 2。总参数 740M，由 270M 文本、170M 视觉和 300M 音频编码器组成。模型把文本（含代码）、图像、视频和音频映射进同一个 768 维向量空间。面向手机和笔记本等消费级硬件，提供低延迟语义表示，支持端侧搜索、RAG、分类和聚类。官方称其 &quot;best-in-class&quot;，但未给出基准数据。

reddit · r/LocalLLaMA · /u/Recoil42 · 10月6日 16:42

**「为什么重要」** 对做 agent RAG、记忆和检索工具链的工程师，这是一个可直接部署到端侧的组件模型。它把多模态输入统一到同一向量空间，可能简化本地检索管线的数据预处理。但材料未证实其相对现有嵌入模型的实际增益，且它不改变 coding agent、协议或 harness 本身。

**「可关注」** 可关注：EmbeddingGemma 2 采用模块化编码器（文本/视觉/音频分离）并输出 768 维统一向量，为端侧多模态检索提供了新选项；但在缺乏公开基准的情况下，不宜直接替换现有嵌入方案。

**标签**: `#memory`, `#rag`, `#coding-agent`, `#eval`

---

<a id="item-agent-engineer-10"></a>
### [I gave a 21M model a 6.4B-parameter lookup table. It matches a 114M dense model and runs with the table on an SSD \(RX 9070\)](https://www.reddit.com/r/LocalLLaMA/comments/1wz7tvs/i_gave_a_21m_model_a_64bparameter_lookup_table_it/) ⭐️ 5.5/10

A hobbyist reports that a 21M model with a 6.4B-parameter SSD-resident lookup table matches a 114M dense model on a small Wikipedia corpus, running at ~140 tok/s on a consumer AMD GPU with minimal VRAM.

reddit · r/LocalLLaMA · /u/fechyyy · 10月6日 16:57

**标签**: `#memory`, `#eval`, `#toolchain`

---

## AI 日报

<a id="item-ai-daily-1"></a>
### [OpenAI 公开数学 AI 新结果](https://openai.com/index/sharing-ai-progress-in-mathematics) ⭐️ 10.0/10

OpenAI 发布内部前沿模型在数学开放问题上的新结果，并在 GitHub 公开 Lean 证明形式化与研究细节。材料未说明具体问题、模型版本或量化指标。该发布来自官方博客，属第一方研究披露。

rss · OpenAI Blog · 10月6日 12:00

**「为什么重要」** 公开 Lean 证明形式化与研究细节，使外部研究者可独立复核其数学结论，提升结果可验证性。

**「可关注」** 可关注：OpenAI 在 GitHub 公开的 Lean 证明形式化与研究细节，可用于独立验证数学结果。

**标签**: `#model`, `#lab`, `#open-source`, `#eval`

---

<a id="item-ai-daily-2"></a>
### [OpenAI 与 Ironclad 训练合同 agent](https://openai.com/index/advancing-computer-use-with-ironclad) ⭐️ 8.3/10

OpenAI 与 Ironclad 合作，在复杂合同工作流上训练并评估 AI agent，推进 computer use 在专业工作中的应用。官方博客称此为应用更新，未发布新模型或政策。公开材料未给出具体基准数字或技术细节。

rss · OpenAI Blog · 10月6日 10:00

**「为什么重要」** 专业工作流是 computer use 的高价值场景。该合作为 agent 在复杂合同任务中的训练与评估提供了公开案例。

**「可关注」** 可关注：双方如何针对复杂合同工作流设定训练目标与评估方案。

**标签**: `#lab`, `#product`, `#eval`, `#industry`

---

<a id="item-ai-daily-3"></a>
### [Building Git infrastructure for agent-scale development](https://github.blog/engineering/architecture-optimization/building-git-infrastructure-for-agent-scale-development/) ⭐️ 7.8/10

GitHub is rebuilding its Git infrastructure to create a foundation for agent-scale software development.

rss · GitHub Blog · 10月6日 20:57

**标签**: `#industry`, `#product`, `#open-source`

---

<a id="item-ai-daily-4"></a>
### [Jump Trading 扩展量化研究](https://openai.com/index/jump-trading) ⭐️ 6.8/10

OpenAI 官方博客发布客户案例，Jump Trading 用 ChatGPT 扩展量化研究。文章称其部署更长周期的 AI 工作流，融合多个数据源，并保留人工复核。这是单一企业用例，未给出具体指标，也不涉及模型或政策更新。

rss · OpenAI Blog · 10月6日 12:00

**「为什么重要」** 案例展示了长周期 AI 工作流在高风险领域的用法：多源数据输入，人工复核留在环路里。对设计 coding agent 的人来说，这种人机协作形态值得参考。

**「可关注」** 可关注：Jump Trading 将 ChatGPT 嵌入更长周期的研究工作流，串联多个数据源，关键步骤保留人工复核。

**标签**: `#model`, `#industry`, `#product`

---

<a id="item-ai-daily-5"></a>
### [OpenAI 扩展 Atlassian 合作](https://openai.com/index/atlassian-partnership) ⭐️ 6.8/10

OpenAI 与 Atlassian 宣布扩大合作伙伴关系，目标是将前沿模型与企业知识连接，帮助团队规划、构建和交付工作。官方公告未披露具体模型名称、产品功能或上线时间。目前仅确认合作方向，缺乏可验证的技术细节。

rss · OpenAI Blog · 10月6日 16:00

**「可关注」** 双方合作聚焦企业知识连接，目前无模型名称、功能或时间表可查。

**标签**: `#lab`, `#industry`, `#model`, `#product`

---

<a id="item-ai-daily-6"></a>
### [Meta nts.meta.com 支持 NTS](https://engineering.fb.com/2026/10/06/production-engineering/nts-authenticated-time-at-meta/) ⭐️ 6.8/10

Meta 公共时间服务 nts.meta.com 现已支持 NTS（Network Time Security，RFC 8915）。数据包经过认证，设备可验证时间来源并检测传输篡改。服务器不保存每客户端状态，Cookie 密钥派生而不存储、不复制。实现已开源。

rss · Engineering at Meta · 10月6日 16:00

**「为什么重要」** 认证时间同步可防止传输篡改，是基础设施的安全基础。Meta 开源了无状态 NTS 实现，Cookie 密钥派生而不存储，工程师可直接参考。

**「可关注」** nts.meta.com 的 NTS 服务器无每客户端状态，Cookie 密钥派生而不存储、不复制，且实现已开源，可作为认证时间同步的参考设计。

**标签**: `#industry`, `#lab`, `#open-source`, `#product`

---