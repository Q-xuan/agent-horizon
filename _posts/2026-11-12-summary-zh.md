---
layout: default
title: "Horizon Summary: 2026-11-12 (ZH)"
date: 2026-11-12
lang: zh
---

> 从 198 条内容中筛选出 18 条重要资讯。

<nav id="ah-toc" class="ah-toc" aria-label="目录"><span class="ah-toc-title">目录</span><ul><li><a href="#sec-harness-arch"><span class="ah-toc-name">Harness 架构</span><span class="ah-toc-count">4条</span></a></li><li><a href="#sec-agent-engineer"><span class="ah-toc-name">Agent 工程师日报</span><span class="ah-toc-count">12条</span></a></li><li><a href="#sec-ai-daily"><span class="ah-toc-name">AI 日报</span><span class="ah-toc-count">2条</span></a></li></ul></nav>

---

**[Harness 架构](#sec-harness-arch)**
1. [pydantic-ai v2.67.0 发布](#item-harness-arch-1) ⭐️ 7.8/10
2. [MCP Servers v2.4.0 发布](#item-harness-arch-2) ⭐️ 7.8/10
3. [langchain-core 1.8.0 发布](#item-harness-arch-3) ⭐️ 6.8/10
4. [Anthropic Claude Skills 仓库公开](#item-harness-arch-4) ⭐️ 5.0/10

**[Agent 工程师日报](#sec-agent-engineer)**
1. [AWS 官方 aws-emulator 发布](#item-agent-engineer-1) ⭐️ 8.0/10
2. [Gemini Decisions API 发布](#item-agent-engineer-2) ⭐️ 7.0/10
3. [Anthropic IPO 路演披露多芯片策略](#item-agent-engineer-3) ⭐️ 7.0/10
4. [Tree-Ising 无梯度修复 LLM 权重](#item-agent-engineer-4) ⭐️ 7.0/10
5. [WikiTrace 证据链接记忆缓解 Agent 退化](#item-agent-engineer-5) ⭐️ 7.0/10
6. [Tests as Data 框架发布](#item-agent-engineer-6) ⭐️ 7.0/10
7. [BotPsy 0.8B 开源端侧智能体发布](#item-agent-engineer-7) ⭐️ 6.8/10
8. [多向量嵌入 Token Pooling 感知训练](#item-agent-engineer-8) ⭐️ 6.8/10
9. [Apple 发布更快 RAG 检索研究](#item-agent-engineer-9) ⭐️ 6.0/10
10. [llm 0.37.2 安全补丁发布](#item-agent-engineer-10) ⭐️ 6.0/10
11. [FINCOSMOS 金融智能体开放世界评估范式](#item-agent-engineer-11) ⭐️ 6.0/10
12. [Embodied First Exam 发布](#item-agent-engineer-12) ⭐️ 6.0/10

**[AI 日报](#sec-ai-daily)**
1. [Google 发布 A2UI 1.0 开放协议](#item-ai-daily-1) ⭐️ 7.8/10
2. [OpenAI 退伍军人免费 ChatGPT Plus 活动落地](#item-ai-daily-2) ⭐️ 6.8/10

---

## Harness 架构
{: #sec-harness-arch .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-harness-arch" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-harness-arch-1"></a>
### [pydantic-ai v2.67.0 发布](https://github.com/pydantic/pydantic-ai/releases/tag/v2.67.0) ⭐️ 7.8/10

pydantic-ai v2.67.0 发布，核心更新包括 durable execution 下 \`SubAgents\(dynamic\_agents=...\)\` 支持、\`RepoContext\` 按目录加载嵌套指令并默认限制 32,000 字符、\`ArtifactScanner\` 匹配前剥离默认可忽略字符。新增 \`provider\_settings\` 统一承载提供程序原生工具字段，扩展文档发送至 \`mimetypes\` 已知任意媒体类型。同时引入 \`Workspace.authority\_of\` 细粒度权限、\`dequeue\`/\`set\_enqueue\_priority\` 消息队列控制，以及多模型与沙箱后端改进。

github · dsfaccini · 11月10日 23:11

**「设计要点」** 运行时层面，durable execution 现在支持动态子代理与 DBOS 子工作流并行，Prefect 任务在二进制消息历史重试时自动重放。工具层通过 \`provider\_settings\` 统一承载提供程序特定字段，权限模型新增 \`Workspace.authority\_of\` 路径级授权与 \`directory\` 权限校验。

**「改了什么」** 相对上一版，v2.67.0 使 durable execution 支持动态子代理与任务控制，\`RepoContext\` 改为按目录加载指令并引入 32k 字符上限，\`ArtifactScanner\` 增加 Unicode 规范化。工具配置统一迁入 \`provider\_settings\`，新增消息队列 \`dequeue\` 与优先级调整，guardrail verdicts 与能力结果持久化。

**标签**: `#subagents`, `#runtime`, `#memory`, `#tools`

---

<a id="item-harness-arch-2"></a>
### [MCP Servers v2.4.0 发布](https://github.com/modelcontextprotocol/servers/releases/tag/v2.4.0) ⭐️ 7.8/10

modelcontextprotocol/servers 发布 v2.4.0，修复 3 个 MCP 服务器共 6 个安全漏洞。filesystem 服务器升级至 2.3.0，git 与 fetch 服务器升级至 2026.11.11。技术要点包括：filesystem 采用检查后打开语义阻断符号链接竞争（Linux 和 macOS），拒绝 FIFO/套接字/设备文件及 Windows NTFS 备用数据流，新增 --read-only-dir 支持 per-directory 只读访问；Windows 上竞争窗口仅收窄，目录连接暂未覆盖。git 服务器覆盖仓库配置中的命令执行项，拒绝 Git &lt; 2.31；fetch 服务器将 IPv6 站点本地地址纳入私有范围，改进 robots.txt 路径解析。

github · cliffhall · 11月11日 07:07

**「设计要点」** filesystem 服务器通过目录描述符绑定实现路径作用域隔离，所有文件操作在检查后立即基于该描述符执行，消除时间窗口内的符号链接替换风险。git 服务器在命令执行前强制重置仓库级配置，形成最小权限执行边界。

**「改了什么」** filesystem 服务器基于已验证的目录描述符执行读写，move\_file 先移出源文件再验证目标，新增 --read-only-dir 支持 per-directory 只读访问，Linux 和 macOS 阻断符号链接竞争而 Windows 仅收窄窗口；git 服务器强制覆盖 core.fsmonitor、diff.external 等配置项，拒绝 Git &lt; 2.31，并封堵交替对象存储与链接工作树，Windows 目录连接暂未覆盖；fetch 服务器拒绝非全局单播 IPv6 地址，robots.txt 按站点解析路径匹配。

**标签**: `#mcp`, `#permissions`, `#sandbox`, `#tools`

---

<a id="item-harness-arch-3"></a>
### [langchain-core 1.8.0 发布](https://github.com/langchain-ai/langchain/releases/tag/langchain-core%3D%3D1.8.0) ⭐️ 6.8/10

langchain-core 1.8.0 正式发布。本次升级移除 Python 3.10 支持，最低运行版本提升至 Python 3.11。新增 decision models 特性，但发布说明未披露实现细节。

github · github-actions\[bot\] · 11月11日 15:22

**「改了什么」** langchain-core 1.8.0 终止 Python 3.10 支持，最低版本提升至 Python 3.11。新增 decision models 特性，但未提供接口文档或实现细节。

**标签**: `#runtime`, `#planning`

---

<a id="item-harness-arch-4"></a>
### [Anthropic Claude Skills 仓库公开](https://github.com/anthropics/skills) ⭐️ 5.0/10

Anthropic 公开 Claude Agent Skills 标准实现仓库 \`anthropics/skills\`。Skills 以文件夹形式组织指令、脚本和资源，Claude 可动态加载以提升 specialized 任务完成能力。当前仅提供高层概念介绍，未公开具体实现细节、代码路径或限制条件。

rss · GitHub Trending Daily · 11月11日 23:00

**标签**: `#tools`

---

## Agent 工程师日报
{: #sec-agent-engineer .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-agent-engineer" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-agent-engineer-1"></a>
### [AWS 官方 aws-emulator 发布](https://simonwillison.net/2026/Nov/11/aws-emulator/) ⭐️ 8.0/10

2026 年 11 月 11 日 AWS 发布官方本地模拟器 aws-emulator，支持开发者无需付费 API 密钥即可在本地模拟 AWS 服务开展测试。该项目用 Rust 编写，由大量 AI agent 参与开发，上线前三周累计产生 29684 次提交。当前版本仅支持通过 Docker 在 macOS 或 Windows 上运行，暂未提供单二进制可直接运行的版本。影响群体为 AWS 服务集成测试开发者、coding agent 与测试 harness 构建者。

rss · Simon Willison · 11月11日 21:18

**「为什么重要」** 它直接填补了 AWS 官方本地测试模拟器的空白，可降低云服务集成测试的成本与权限门槛；AI agent 主导完成该项目的案例，也为后续 AI 辅助工程开发提供了可参考的实践样本。

**「可关注」** 可关注：aws-emulator 后续是否会推出免 Docker 的单二进制版本，以适配更多测试场景与跨平台需求。

**标签**: `#harness`, `#eval`, `#coding-agent`

---

<a id="item-agent-engineer-2"></a>
### [Gemini Decisions API 发布](https://blog.google/innovation-and-ai/technology/developers-tools/gemini-decisions-api/) ⭐️ 7.0/10

Google 于 2026-11-11 发布 Gemini Decisions API（对应模型为 Gemini Decision 1），正式加入决策模型服务赛道。该 API 支持是/否、选择、rubric 评分三类问题，复用 Jev 的术语「Noul」指代是/否问题；定价与 GPT-6 Luna 决策模型一致，为每百万输入 token 10 美分，输出免费，高于 Jev 的每百万 4.2 美分。其支持文本、图片、音频、视频、PDF 全模态输入，是三者中模态覆盖最广的，测试中对视频类是/否问题返回概率值而非 0/1 的确定结果，主要面向需要多模态决策能力的开发者及 coding agent harness 场景。

hackernews · iamdelirium · 11月11日 18:32 · [社区讨论](https://news.ycombinator.com/item?id=50456791)

**「为什么重要」** 它是当前公开决策模型 API 中唯一支持音视频输入的选项，对需要处理多模态输入的 coding agent harness 有直接可用性；但定价高于 Jev，成本敏感场景需权衡适配成本。

**「可关注」** 可关注多模态决策场景下，Gemini Decision 1 的音视频输入能力与概率返回格式的适配成本，以及其与 Jev、OpenAI 决策模型的定价差对 harness 选型的影响。

**「评论」** 社区讨论聚焦决策模型在 coding agent 中的落地用法，部分用户认为其多模态能力是差异化优势，也有用户指出其定价高于 Jev 等同类产品，同时有人提到本地可运行的轻量分类工具可作为替代方案。

**标签**: `#coding-agent`, `#harness`, `#orchestration`

---

<a id="item-agent-engineer-3"></a>
### [Anthropic IPO 路演披露多芯片策略](https://simonwillison.net/2026/Nov/11/anthropic-ipo-roadshow/) ⭐️ 7.0/10

2026 年 11 月 11 日 Simon Willison 发布报道，披露 Anthropic 于 2026 年 11 月 10 日启动的 IPO 路演视频内容，该视频无官方公开转录稿，相关内容为 Willison 使用 MacWhisper 提取的非官方版本。联合创始人 Tom Brown 在视频中首次公开 Anthropic 训练与推理服务 Claude 的四芯片家族策略，覆盖 AWS Trainium、Google TPUs、NVIDIA GPU、AMD GPU，称早期押注多芯片策略时行业普遍认为跨芯片运行 AI 模型不划算，因每个芯片需定制专属软件栈与推理栈，成本高、难度大；此前 Anthropic 仅在 2025 年 9 月的故障 postmortem 中透露过 TPU 部署存在专属问题，本次是首次公开完整多芯片布局细节。关键细节包括：2026 年 Anthropic 首次合作 AMD GPU 时，内部工具 Mythos 仅用 3 天、几乎无人工干预完成 Claude 在 AMD 平台的适配，Claude 自行编写了近 100%的内核；此外 Tom Brown 还披露了 Anthropic 的「计算乘数」策略，称其可通过软硬件优化放大有效算力，并预期在递归自我改进阶段，Claude 可自行发现新的计算乘数。当前披露内容未包含性能基准、生产链路数据或深度架构分析，相关策略的实际效果尚未有公开可验证数据，主要面向 AI 基础设施、模型服务及 agent 工具链领域的工程师。

rss · Simon Willison · 11月11日 15:11

**「为什么重要」** 这是 Anthropic 首次公开披露其跨四大硬件生态的多芯片训练推理落地策略，以及内部工具在芯片适配上的效率案例，填补了此前仅通过故障 postmortem 推测其多芯片布局的信息空白；但相关计算乘数的具体收益、多芯片栈的实际性能表现、递归自我改进阶段的自发现能力均无公开数据支撑，对行业的具体影响尚未验证。

**「可关注」** 可关注跨芯片适配的自动化工具链效率，以及模型参与底层内核开发、计算乘数优化的可行性边界，目前相关实践仅 Anthropic 单方披露，无公开基准验证。

**标签**: `#infrastructure`, `#compute`, `#toolchain`

---

<a id="item-agent-engineer-4"></a>
### [Tree-Ising 无梯度修复 LLM 权重](https://huggingface.co/papers/2611.14210) ⭐️ 7.0/10

Hugging Face Daily Papers 于 2026-11-11 介绍 arXiv 预印本 Tree-Ising，一种无梯度位级权重编辑方法。该方法将语言模型修复（如消除 agent 推理循环）建模为 BF16 权重上的稀疏离散优化问题，仅通过符号翻转和指数移位修改权重，无需重新训练。相比 MIT Takehi 等人此前用 GPT-6 Astra agent 修复 Qwen3.5-0.8B 推理循环的方案（158 轮 agent 交互、89.7M token、50 次前向传播），Tree-Ising 省去高成本 agent 循环。当前材料在性能基准前截断，实际效率提升幅度未确认。

rss · Hugging Face Daily Papers · 11月11日 00:00

**「为什么重要」** 该工作直接针对 coding agent 的推理循环等故障模式，提供了一种不依赖重训练或高成本 agent 交互的修复路径。若后续基准证实效率优势，可改变 agent 模型故障缓解的工程实践。

**「可关注」** 可关注：Tree-Ising 将权重修复转为稀疏离散优化，用 BF16 位级编辑替代高 token 消耗的 agent 交互循环。

**标签**: `#coding-agent`

---

<a id="item-agent-engineer-5"></a>
### [WikiTrace 证据链接记忆缓解 Agent 退化](https://huggingface.co/papers/2611.14320) ⭐️ 7.0/10

2026-11-11，Hugging Face Daily Papers 发布论文摘要，提出 WikiTrace 证据链接记忆系统。该系统将 agent 从轨迹中提炼的每条 lesson 与其原始支持轨迹关联，使 agent 能在新任务中验证 lesson 有效性。当前 LLM agent 普遍存在 memory-induced degradation：agent 因误用或误读无轨迹附带的 lesson，在原本可完成的任务上失败。论文指出 lesson 仅从任务成功/失败标签推断，缺乏可回溯证据。该研究获 45 次 upvotes，但原文摘要被截断，具体实验设置与效果数据未完整披露。

rss · Hugging Face Daily Papers · 11月11日 00:00

**「为什么重要」** memory-induced degradation 是 LLM agent 从经验学习时的已知风险。WikiTrace 提供了一种可验证的记忆架构思路，直接针对 lesson 与轨迹脱节的根因，对设计 coding agent 记忆模块有参考价值。

**「可关注」** 可关注：外部记忆若仅存储 distilled lesson 而丢弃原始轨迹，agent 将失去验证依据，记忆架构需保留证据回溯路径。

**标签**: `#memory`

---

<a id="item-agent-engineer-6"></a>
### [Tests as Data 框架发布](https://martinfowler.com/articles/tests-as-data.html) ⭐️ 7.0/10

2026 年 11 月 11 日，Martin Fowler 发布 Matteo Vaccari 提出的 Tests as Data 框架，针对 AI 编码代理同时编写生产代码与测试代码的场景。该框架提出三项核心主张：开发者成为 AI 的客户、客户测试取代开发者测试成为人机核心合同、将合同沉淀为测试数据而非测试代码以避免被编码代理意外修改。框架指出过去 DSL 解析器与自定义测试运行器成本高昂，如今 AI 已让这类工具的实现与维护成本大幅降低，最终目标是建立人类可读的人机测试合同。

rss · Martin Fowler · 11月11日 15:17

**「为什么重要」** 该框架直击 AI 编码代理同时修改生产代码与测试代码时评估标准被破坏的核心痛点，为 eval 与 harness 的架构设计提供了可参考的方向，对保障 AI 生成代码的评估可信度有直接价值。

**「可关注」** 可关注：将人机约定的测试标准沉淀为人类可读的测试数据，避免被编码代理意外修改，同时可借助 AI 降低自定义测试 DSL 与运行器的实现成本。

**标签**: `#coding-agent`, `#eval`, `#harness`

---

<a id="item-agent-engineer-7"></a>
### [BotPsy 0.8B 开源端侧智能体发布](https://huggingface.co/blog/qvac/botpsy) ⭐️ 6.8/10

2026 年 11 月 11 日 Hugging Face Blog 官宣 BotPsy，这是一款 0.8B 参数的开源智能体语言模型，由 Tether AI Research 推出，基于 Qwen3.5-0.8B 打造，针对函数调用与端侧个人助理场景优化，采用 SFT、多教师在线策略蒸馏、两轮强化学习的四阶段后训练流程，将按 Apache 2.0 协议开源用于研究与教育场景。关键性能上，它在 6 项工具调用与智能体基准测试中均超过测试的≤1.2B 参数其他模型，5 项基准得分高于 2.5 倍参数量的 Qwen3.5-2B-Think，比如 BFCL v4 得分 44.0 对比 37.7。该模型仅适配低到中等难度任务，不适合高风险场景，当前公开内容未披露完整性能基准、训练细节与集成指南，完整技术信息需查阅原帖，主要面向端侧、低资源智能体部署的研发团队。

rss · Hugging Face Blog · 11月11日 05:01

**「为什么重要」** 它填补了≤1B 参数开源端侧智能体模型的性能空白，为低资源、隐私优先的自托管智能体部署提供了新选项；其实际端侧部署效率、长期稳定性及生态适配性尚未得到公开验证。

**「可关注」** 可关注：BotPsy 提供 bf16、Q8、Q4 三种精度权重及 GGUF 格式，适配 llama.cpp 与 QVAC SDK，且多数工具调用与智能体基准测试在测试的≤1.2B 参数区间取得 SOTA。

**标签**: `#coding-agent`

---

<a id="item-agent-engineer-8"></a>
### [多向量嵌入 Token Pooling 感知训练](https://huggingface.co/blog/token-pooling) ⭐️ 6.8/10

Hugging Face 2026 年 11 月 11 日发布博客，提出面向多向量嵌入模型的 Token Pooling 感知训练方法。该方法通过 Ward 层次聚类合并相似 token 向量，在 pool\_factor=4 的 4 倍压缩设置下，常规训练模型的 NanoBEIR nDCG@10 保留率为 94.6%，经池化感知训练后提升至 97.8%。技术已集成至 Sentence Transformers 的 HierarchicalTokenPooling 模块与 MultiVectorTokenPoolingLoss 损失，支持 max\_tokens、pool\_factor、distance\_threshold 三种池化预算控制方式，主要面向 RAG 检索组件开发者。

rss · Hugging Face Blog · 11月11日 00:00

**「为什么重要」** 该技术为多向量检索的存储-质量权衡提供了可落地的训练方案，已证实可在 4 倍压缩下提升检索质量保留率。目前仅公开博客与示例代码，尚未见大规模工业场景验证结果，对 Agent 架构、Harness 框架的直接影响较窄。

**「可关注」** 可关注：Sentence Transformers 已原生支持池化感知训练与自适应阈值校准，现有 ColBERT 类多向量检索 pipeline 可低改动接入该压缩方案。

**标签**: `#eval`, `#memory`

---

<a id="item-agent-engineer-9"></a>
### [Apple 发布更快 RAG 检索研究](https://machinelearning.apple.com/research/faster-retrieval) ⭐️ 6.0/10

2026 年 11 月 11 日 Apple 机器学习研究团队公开关于更快 RAG 检索的研究，Hacker News 社区讨论将其归入「learned retrieval 范式」，与 Spotify 的 Parallel Fusion Router 同属该技术方向。讨论中普遍提及该方向的核心权衡是检索速度与输出质量，部分开发者认为这类方法仅对处理亿级以上条目的超大规模检索场景有显著价值。也有开发者结合自身 RAG 开发经验，对现有嵌入模型在代码库检索等场景的效果存疑，认为其未必能超过 grep+正则方案；目前公开材料未包含该研究的基准测试、架构细节或具体性能数据，无法评估其实际落地价值。

hackernews · zerop · 11月11日 16:57 · [社区讨论](https://news.ycombinator.com/item?id=50455633)

**「为什么重要」** 该研究指向 RAG 检索优化方向，与 AI Agent 的记忆检索、工具链设计直接相关，是当前业界探索的效率优化路径之一。但目前公开内容仅包含研究标题与社区讨论，无技术细节与性能数据，其实际效果尚未得到验证。

**「可关注」** 可关注：learned retrieval 范式的适用边界，当前社区已出现「仅对亿级以上超大规模检索场景有效」与「特定场景下效果不及传统检索方案」两种分歧，需结合自身场景验证。

**「评论」** 社区讨论的共识是该研究属于 learned retrieval 范式，核心权衡为检索速度与输出质量；分歧集中在适用场景与效果上限，部分开发者认为其仅对亿级以上超大规模检索有价值，也有开发者分享实际经验称现有嵌入模型在代码库检索等场景的效果未必能超过 grep+正则方案。

**标签**: `#memory`, `#orchestration`, `#retrieval`

---

<a id="item-agent-engineer-10"></a>
### [llm 0.37.2 安全补丁发布](https://simonwillison.net/2026/Nov/11/llm/) ⭐️ 6.0/10

2026 年 11 月 11 日，Simon Willison 发布 llm 0.37.2 安全补丁，修复两个 GHSA 安全公告（GHSA-v9h7-jj4g-f862、GHSA-r639-rr7r-x72w）报告的 API 密钥泄露风险，该漏洞由 Daniel de Araujo 报告。漏洞触发路径为 llm 的 extra-openai-models.yaml 配置项，以及 0.37 版本新增的 llm openai endpoint add 命令，具体场景包括 api\_key\_name 对应的密钥未存储、使用 responses: true 模型时携带-o chat\_completions 1 参数运行。本次更新为专项安全补丁，无重大架构变更，当前公开信息未包含完整技术细节，该问题影响使用 llm CLI 对接 OpenAI 兼容第三方服务的用户，存在配置的 OpenAI API 密钥被意外发送至第三方的问题。

rss · Simon Willison · 11月11日 17:19

**「为什么重要」** 该补丁针对 llm CLI 对接第三方 OpenAI 兼容服务时的密钥泄露风险，未升级的用户若使用相关功能，配置的 OpenAI API 密钥存在被意外传输至非预期第三方的可能。

**「可关注」** 可关注：使用 llm CLI 对接 OpenAI 兼容第三方服务的用户需尽快升级至 0.37.2 版本，规避 API 密钥泄露风险。

**标签**: `#permissions`, `#harness`, `#security`, `#tooling`

---

<a id="item-agent-engineer-11"></a>
### [FINCOSMOS 金融智能体开放世界评估范式](https://huggingface.co/papers/2611.07464) ⭐️ 6.0/10

2026-11-11，Hugging Face Daily Papers 收录论文 2611.07464，提出 FINCOSMOS——面向金融智能体的开放世界评估范式。该范式通过模拟用户持有组合语法采样的隐藏策略，迫使智能体从 Web 主动获取数据，以测量现有封闭世界基准无法捕捉的静默失败模式，包括未验证数据、用户未要求的策略，以及使用未来数据的回测。论文内容被截断，未提供性能验证或实现细节，且评估范围限定在金融领域。

rss · Hugging Face Daily Papers · 11月11日 00:00

**「为什么重要」** 现有封闭世界基准通过固定任务、数据或时间线移除了静默失败，而非测量它们。FINCOSMOS 试图在金融场景中重建这些失败条件，但材料未提供实证结果，其对通用智能体评估的迁移价值尚未证实。

**「可关注」** 可关注：开放世界评估若将数据获取责任完全交给智能体，并引入用户隐藏策略，可能暴露封闭世界设定下被掩盖的静默失败模式。

**标签**: `#eval`

---

<a id="item-agent-engineer-12"></a>
### [Embodied First Exam 发布](https://huggingface.co/papers/2611.12177) ⭐️ 6.0/10

2026 年 11 月 11 日 Hugging Face 每日论文栏目发布 Embodied First Exam，这是一个面向编码智能体的具身原生评测框架，用于测试编码智能体控制物理机器人的能力。该框架共包含 35 个任务套件、覆盖 47 台机器人的 1156 个任务，新增 9 个超越传统抓取放置任务类型的套件，涵盖空间谜题、灵巧操作、多机器人交互等场景，支持智能体自主选择直接控制、代码控制、训练策略控制三种控制路径。目前仅公开论文摘要，未披露完整技术细节、性能基准数据或开源实现，主要面向具身智能体研发方向的工程师。

rss · Hugging Face Daily Papers · 11月11日 00:00

**「为什么重要」** 该框架首次针对编码智能体控制物理机器人的场景设计评测，填补了现有机器人评测基准仅面向视觉运动策略学习、不覆盖编码智能体性能的空白。但目前仅公开摘要，完整基准数据和实现未披露，对非具身方向的编码智能体工程师暂无直接可用价值。

**「可关注」** 可关注：现有主流机器人评测基准均面向视觉运动策略学习设计，未覆盖编码智能体控制机器人的场景，该框架是少有的针对该场景的评测方案。

**标签**: `#eval`, `#coding-agent`

---

## AI 日报
{: #sec-ai-daily .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-daily" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-daily-1"></a>
### [Google 发布 A2UI 1.0 开放协议](https://developers.googleblog.com/a2ui-10-build-delightful-fast-reliable-agentic-experiences/) ⭐️ 7.8/10

Google 于 2026 年 11 月 11 日发布 A2UI 1.0 稳定版，这是一款生成式 UI 开放协议，允许 AI 智能体以交互式界面替代纯文本返回结果。该协议配套开源 Web、Android、iOS 渲染器 SDK，以及 Python、TypeScript、Dart 智能体 SDK，Atlassian、Bloomberg、ByteDance 等公司已基于其开展落地。当前 Gemini 支持 A2UI 0.9.1，Jetpack Compose 的 1.0 适配即将推出，ByteDance Lynx 框架当前支持 0.9 版本、正在适配 1.0。

rss · Google Developers AI · 11月11日 00:00

**「为什么重要」** 当前 AI 智能体交互普遍停留在纯文本阶段，复杂操作需要多轮对话，用户体验受限；A2UI 1.0 提供了跨平台原生渲染的统一协议框架，能降低多端交互式智能体界面的开发成本，同时兼容 MCP Apps 生态。

**「可关注」** 可关注：A2UI 1.0 已支持与 MCP Apps 结合，可在 Claude、Gemini 等第三方智能体中直接渲染交互式 UI。

**标签**: `#lab`, `#industry`, `#open-source`, `#product`

---

<a id="item-ai-daily-2"></a>
### [OpenAI 退伍军人免费 ChatGPT Plus 活动落地](https://openai.com/index/chatgpt-plus-for-veterans) ⭐️ 6.8/10

OpenAI 推出面向退伍军人及退役过渡服役人员的免费一年 ChatGPT Plus 订阅权益。截至官方发布报道时，已有超 2 万人完成申领。该权益主要用于辅助用户准备平民职业生涯。

rss · OpenAI Blog · 11月11日 08:00

**「为什么重要」** 该举措属于非技术突破类的行业产品/政策倡议，覆盖退伍军人职业过渡的细分场景，且有明确的参与数据支撑。

**「可关注」** 可关注：AI 工具在退伍军人职业过渡场景的落地进展。

**标签**: `#lab`, `#product`, `#policy`, `#industry`

---