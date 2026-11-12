---
layout: default
title: "Horizon Summary: 2026-11-12 (ZH)"
date: 2026-11-12
lang: zh
---

> 从 206 条内容中筛选出 18 条重要资讯。

<nav id="ah-toc" class="ah-toc" aria-label="目录"><span class="ah-toc-title">目录</span><ul><li><a href="#sec-harness-arch"><span class="ah-toc-name">Harness 架构</span><span class="ah-toc-count">3条</span></a></li><li><a href="#sec-agent-engineer"><span class="ah-toc-name">Agent 工程师日报</span><span class="ah-toc-count">13条</span></a></li><li><a href="#sec-ai-daily"><span class="ah-toc-name">AI 日报</span><span class="ah-toc-count">1条</span></a></li><li><a href="#sec-ai-deals"><span class="ah-toc-name">AI 羊毛</span><span class="ah-toc-count">1条</span></a></li></ul></nav>

---

**[Harness 架构](#sec-harness-arch)**
1. [pydantic-ai v2.68.0 发布](#item-harness-arch-1) ⭐️ 8.8/10
2. [MCP servers v2.4.0 安全修复发布](#item-harness-arch-2) ⭐️ 8.3/10
3. [LangChain 1.5.0 发布](#item-harness-arch-3) ⭐️ 5.8/10

**[Agent 工程师日报](#sec-agent-engineer)**
1. [Gemini Decisions API 发布](#item-agent-engineer-1) ⭐️ 8.0/10
2. [Apple 更快 RAG 检索研究引讨论](#item-agent-engineer-2) ⭐️ 7.0/10
3. [AWS 官方 aws-emulator 发布](#item-agent-engineer-3) ⭐️ 7.0/10
4. [llm 0.37.2 安全补丁发布](#item-agent-engineer-4) ⭐️ 7.0/10
5. [Embodied First Exam 发布](#item-agent-engineer-5) ⭐️ 7.0/10
6. [Tests as Data 保护人机契约](#item-agent-engineer-6) ⭐️ 7.0/10
7. [Anthropic IPO 路演 多芯片训练细节披露](#item-agent-engineer-7) ⭐️ 6.0/10
8. [GTAGym 预印本发布](#item-agent-engineer-8) ⭐️ 6.0/10
9. [HF 每日论文：Tree-Ising 修复 LLM 权重](#item-agent-engineer-9) ⭐️ 6.0/10
10. [HF 每日论文：WICL 机器人操控新范式](#item-agent-engineer-10) ⭐️ 6.0/10
11. [HF trending：Qwen3 SGLang 推测解码模型](#item-agent-engineer-11) ⭐️ 6.0/10
12. [BotPsy 0.8B 端侧智能体模型开源](#item-agent-engineer-12) ⭐️ 5.8/10
13. [Simon Willison 工具站加标签云](#item-agent-engineer-13) ⭐️ 5.5/10

**[AI 日报](#sec-ai-daily)**
1. [OpenAI 退伍军人 ChatGPT Plus 计划落地](#item-ai-daily-1) ⭐️ 7.8/10

**[AI 羊毛](#sec-ai-deals)**
1. [Mu3ic 1.8.0 更新 送码+双 11 优惠](#item-ai-deals-1) ⭐️ 6.0/10

---

## Harness 架构
{: #sec-harness-arch .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-harness-arch" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-harness-arch-1"></a>
### [pydantic-ai v2.68.0 发布](https://github.com/pydantic/pydantic-ai/releases/tag/v2.68.0) ⭐️ 8.8/10

这是 pydantic-ai v2.68.0 官方发布，面向 agent 框架使用者与 harness 开发者。核心更新包括输出 token 超限时的模型回退逻辑、委托任务 API 扩展、运行内审批流改造、工作区后端行为约束，新增 Gemini Decisions API 后端与持久化子工作流委托支持，同时包含多项 harness API 重命名与兼容性调整。

github · dsfaccini · 11月12日 01:56

**「设计要点」** 运行时适配 Temporal 等持久化执行场景，要求工作区后端保持分离进程存活，权限记忆与提示注入防护均支持持久化运行，子代理任务控制事件新增 Event 后缀与 agent\_name、parent\_task\_id 字段，harness 层多项标识符与事件结构重命名并保留废弃别名。

**「改了什么」** 相对 v2.67.0，新增 OutputTokenLimitExceeded 异常与 ModelFallback 超限回退能力，新增 DelegationTasks.discover\(\)方法并修复损坏任务阻塞任务列表的问题，新增 RequestInput 支持运行内审批与用户询问，工作区后端强制要求保持分离进程存活，支持 SubAgents 委托到 Temporal/DBOS 持久化子工作流，新增 GoogleDecisionsModel 后端，新增支持通过工作流信号触发的 CancellationToken 取消 Temporal 持久化运行，新增 Workspace.run 的 per-command cwd 参数，新增 ConversationStore 支持 UI 适配器对话的加载与保存，新增 GoogleModel 与 BedrockConverseModel 流式请求的 AI Gateway 流式成本统计，升级 genai-prices 依赖至 0.2.3，修复用户与工具内容中类应用框架文本的转义逻辑，修复 Vercel AI 与 AG-UI 事件流未传递 ModelResponse.canonical\_system 的问题，修复 Claude 模型 max\_tokens 超过上限时自动截断的问题，修复 OpenAICompatibleProvider 等供应商的 vendor/model id 大小写不敏感解析问题，harness 层重命名多项字段与标识符、新增 RefineOutput 能力，所有重命名均保留废弃别名。

**标签**: `#runtime`, `#subagents`, `#permissions`, `#sandbox`

---

<a id="item-harness-arch-2"></a>
### [MCP servers v2.4.0 安全修复发布](https://github.com/modelcontextprotocol/servers/releases/tag/v2.4.0) ⭐️ 8.3/10

modelcontextprotocol/servers 发布 v2.4.0，修复三个 MCP 服务器共六个安全漏洞。filesystem 服务器修复 Linux/macOS 符号链接竞争条件，防止读取允许目录外文件，Windows 上缩小竞争窗口；git 服务器阻止仓库配置触发服务器权限执行程序；fetch 服务器修正 IPv6 站点本地地址误判及 robots.txt 绕过。受影响包需升级至 @modelcontextprotocol/server-filesystem 2.3.0 及 mcp-server-git、mcp-server-fetch 2026.11.11。

github · cliffhall · 11月11日 07:07

**「设计要点」** filesystem 服务器采用检查后锁定语义，读写操作均相对于已检查目录打开文件，避免检查与打开之间的目录替换攻击。git 服务器强制覆盖仓库本地配置（core.fsmonitor、diff.external、hooks 等），并拒绝 Git &lt; 2.31 版本。所有服务器 Docker 镜像默认以非 root 用户运行。

**「改了什么」** filesystem 新增 --read-only-dir 参数支持 per-directory 只读访问，拒绝 NTFS 备用数据流路径及 Windows 设备名路径。server-everything 默认将 HTTP 传输绑定到 loopback 接口。TypeScript 服务器从日期版本迁移到语义版本，npm 需显式指定 2.3.0 安装。

**标签**: `#mcp`, `#sandbox`, `#tools`, `#permissions`

---

<a id="item-harness-arch-3"></a>
### [LangChain 1.5.0 发布](https://github.com/langchain-ai/langchain/releases/tag/langchain%3D%3D1.5.0) ⭐️ 5.8/10

LangChain 1.5.0 发布。该版本移除已终止生命周期的 Python 3.10 支持，最低运行环境升至 Python 3.11，langchain-core 最低版本要求同步提升至 1.8.0。技术新增方面，本次引入 ModelRouterMiddleware（beta）与 auto-mode middleware 两项中间件。当前 release notes 未提供实现细节或架构上下文。

github · github-actions\[bot\] · 11月11日 15:47

**「改了什么」** langchain 1.5.0 相对 1.4.10 停止支持 Python 3.10，最低版本改为 Python 3.11；langchain-core 最低依赖提升至 1.8.0。新增 model router 与 auto mode 中间件，其中 ModelRouterMiddleware 标记为 beta。

**标签**: `#runtime`, `#tools`

---

## Agent 工程师日报
{: #sec-agent-engineer .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-agent-engineer" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-agent-engineer-1"></a>
### [Gemini Decisions API 发布](https://blog.google/innovation-and-ai/technology/developers-tools/gemini-decisions-api/) ⭐️ 8.0/10

2026 年 11 月 11 日，Google 发布 Gemini Decision 1 决策模型 API，加入 Jev、OpenAI 的决策模型赛道。该 API 支持 yes/no、选择、rubric 评分三类问题，复用 Jev 对 yes/no 问题的术语&quot;Noul&quot;；定价与 GPT-6 Luna 决策模型一致，为每百万输入 token 10 美分、输出免费，高于最便宜的 Jev（每百万输入 token 4.2 美分）。输入模态上，Gemini Decision 1 支持文本、图片、音频、视频、PDF，覆盖范围广于仅支持文本/JSON 的 Jev 和支持文本、图片的 OpenAI；实测其对视频的 yes/no 问题返回 0 到 1 之间的概率值，而非 Jev 与 OpenAI 的 0.0/1.0 绝对判断。该 API 面向需要结构化决策能力的 Agent 编排、Coding Harness 集成、多模态场景开发者。

hackernews · iamdelirium · 11月11日 18:32 · [社区讨论](https://news.ycombinator.com/item?id=50456791)

**「为什么重要」** 该 API 首次提供全模态输入的决策模型选项，可覆盖音视频、PDF 等非文本场景的结构化决策需求，对多模态 Agent 工具链建设有直接参考价值；但其实际精度、在 coding harness 中的落地效果尚未得到大规模验证。

**「可关注」** 可关注：Gemini Decision 1 的全模态输入能力是否适配音视频代码审查、多模态 Agent 决策等场景，同时需权衡其高于 Jev 的定价成本。

**「评论」** 社区讨论围绕三类决策模型的差异展开：有用户指出决策模型此前因无法输出概率未受重视，也有用户提到当前决策模型成本极低，10 万 token 上下文加数百个 100token 问题的成本约等于单次谷歌搜索 API 调用；另有用户肯定其多模态能力对特定场景的价值，同时有用户提到该 API 定价高于 Jev，另有用户推荐基于 Gemma4 微调的 span-02 模型作为更优替代。

**标签**: `#orchestration`, `#harness`, `#coding-agent`, `#eval`

---

<a id="item-agent-engineer-2"></a>
### [Apple 更快 RAG 检索研究引讨论](https://machinelearning.apple.com/research/faster-retrieval) ⭐️ 7.0/10

2026-11-11 Hacker News 线程分享了 Apple 官方 ML Research 关于更快 RAG 检索的研究，该研究面向 RAG 场景的检索效率优化；社区讨论围绕 learned retrieval 方法在 agent 知识管线中的实际权衡展开，从业者对比了 Spotify 的 Parallel Fusion Router 等同类方案，也有从业者提出 embedding/BERT 类检索在代码库场景下效果未必优于 grep，另有从业者认为检索机制会向 LLM 引入启发式偏差，无偏探索往往能获得更优输出质量；目前 Apple 研究的完整技术细节与基准数据未公开。

hackernews · zerop · 11月11日 16:57 · [社区讨论](https://news.ycombinator.com/item?id=50455633)

**「为什么重要」** RAG 是 coding agent 常用的外部知识组件，Apple 作为平台厂商布局该方向研究，加上社区对 learned retrieval 落地权衡的讨论，对构建 RAG 型 agent 系统的工程师有参考价值；但 Apple 研究的完整效果与落地路径尚未公开，实际影响还未证实。

**「可关注」** 可关注：learned retrieval 方法在 agent 知识管线中的实际效果存在分歧，需结合自身场景规模与知识类型验证适用性。

**「评论」** 社区对更快 RAG 检索的 learned 范式存在明显分歧，部分从业者认为该方法仅适合亿级以上超大规模检索场景，也有从业者基于代码库 RAG 落地经验认为现有 embedding/BERT 类检索效果有限，未必能胜过 grep 等传统方法；另有从业者提出检索机制会向 LLM 引入启发式系统的偏差，速度与质量权衡下无偏探索往往能获得更优最终输出质量；另有讨论提及 Apple 在个人助理 AI 领域的长期布局。

**标签**: `#memory`, `#eval`, `#harness`

---

<a id="item-agent-engineer-3"></a>
### [AWS 官方 aws-emulator 发布](https://simonwillison.net/2026/Nov/11/aws-emulator/) ⭐️ 7.0/10

2026 年 11 月 11 日 AWS 发布官方本地模拟器 aws-emulator，支持开发者在本地克隆 AWS 多项服务进行测试，无需付费 API 密钥。该项目用 Rust 编写，上线前三周累计产生 29684 次提交，由大量 AI agent 协作完成。当前工具在 macOS 与 Windows 平台运行需依赖 Docker，暂不支持单二进制直接部署。该工具主要面向需要本地测试 AWS 服务、构建 agent 测试 harness 与 eval 环境的开发者。

rss · Simon Willison · 11月11日 21:18

**「为什么重要」** 该工具首次提供 AWS 官方支持的本地服务测试环境，可避免测试阶段产生真实云服务调用费用，对构建 coding agent 测试框架与 eval 流水线的工程师有直接实用价值。

**「可关注」** 可关注：aws-emulator 由大量 AI agent 协作完成开发，其迭代模式与测试 harness 的适配性可后续跟踪。

**标签**: `#harness`, `#eval`, `#tools`

---

<a id="item-agent-engineer-4"></a>
### [llm 0.37.2 安全补丁发布](https://simonwillison.net/2026/Nov/11/llm/) ⭐️ 7.0/10

llm 0.37.2 于 2026 年 11 月 11 日发布，修复两个安全漏洞（GHSA-v9h7-jj4g-f862、GHSA-r639-rr7r-x72w）：通过 extra-openai-models.yaml 配置 OpenAI 兼容端点时，若 api\_key\_name 对应的密钥未存储，或 responses 为 true 的模型使用 -o chat\_completions 1 运行，可能意外将 OpenAI API 密钥发送至第三方提供商。此外该版本还修复了管道附件支持、空附件报错优化、extra-openai-models.yaml 解析兼容性、llm openai endpoint list --json 兼容未加引号日期、Python API 嵌入集合模型一致性等问题。

rss · Simon Willison · 11月11日 17:19

**「为什么重要」** 该补丁直接修复 API 密钥泄露风险，对使用 llm CLI 或基于其构建 agent 工具、处理 OpenAI 兼容接口凭证的工程师有直接影响，需及时升级避免密钥泄露。

**「可关注」** 可关注：使用 extra-openai-models.yaml 配置 OpenAI 兼容端点、或运行 responses 模型时携带 -o chat\_completions 1 参数的场景，升级前需确认密钥未因漏洞泄露。

**标签**: `#security`, `#permissions`, `#harness`

---

<a id="item-agent-engineer-5"></a>
### [Embodied First Exam 发布](https://huggingface.co/papers/2611.12177) ⭐️ 7.0/10

2026 年 11 月 12 日，Hugging Face Daily Papers 分享新论文提出的 Embodied First Exam 框架，这是面向编码智能体的原生机器人控制评估框架，该论文当日获得 23 次点赞。框架包含 35 个套件、1156 项多样化任务，覆盖 47 台机器人，支持编码智能体自主选择直接控制、代码控制或训练策略控制三种控制方式。该框架填补了现有机器人基准仅适配视觉运动策略、不适用于编码智能体的空白，其中 9 个新套件已拓展至空间谜题、灵巧操作、多机器人交互等非抓放场景，部分内容因原文截断未完整披露。该框架为编码智能体与机器人控制领域的评测体系构建提供了可参考的基准。

rss · Hugging Face Daily Papers · 11月12日 04:13

**「为什么重要」** 该框架首次为编码智能体提供了适配其控制特性的机器人评测基准，解决了现有评测体系不匹配的痛点。其能否成为行业通用评测标准、对编码智能体实际控制能力的提升是否有明确指导作用，尚待后续验证。

**「可关注」** 可关注：框架支持编码智能体自主选择控制方式，且任务覆盖灵巧操作、多机器人交互等非抓放场景，可参考其任务设计思路适配自身评测需求。

**标签**: `#eval`, `#coding-agent`

---

<a id="item-agent-engineer-6"></a>
### [Tests as Data 保护人机契约](https://martinfowler.com/articles/tests-as-data.html) ⭐️ 7.0/10

2026-11-11，Martin Fowler 发布文章介绍 Matteo Vaccari 提出的 tests as data 模式。该模式主张将客户测试作为人与 AI 编码代理之间的主要契约，并将其置于测试数据而非可修改的测试代码中，以防止 AI 在同时生成生产代码和测试代码时意外破坏测试覆盖。文章指出，过去 DSL 解析器和自定义测试运行器成本高昂，而 AI 现在使这些方案变得廉价。这是一篇概念性文章，未提供基准数据或生产环境验证。

rss · Martin Fowler · 11月11日 15:17

**「为什么重要」** 该模式直接针对 coding agent 同时生成生产代码与测试代码时的核心风险：人类失去对功能错误的保护。将测试视为不可变数据而非可修改代码，为 harness 设计提供了新的契约保护思路。

**「可关注」** 当 coding agent 同时生成生产代码与测试代码时，可考虑将核心契约测试设计为不可变数据而非可修改代码，以降低 agent 意外破坏覆盖的风险；AI 现在使自定义 DSL 解析器和测试运行器的维护成本显著降低。

**标签**: `#eval`, `#coding-agent`, `#harness`

---

<a id="item-agent-engineer-7"></a>
### [Anthropic IPO 路演 多芯片训练细节披露](https://simonwillison.net/2026/Nov/11/anthropic-ipo-roadshow/) ⭐️ 6.0/10

2026 年 11 月 11 日，Simon Willison 公开了 Anthropic IPO 路演视频的提取文字稿，披露了 Claude 的多芯片训练与服务策略。路演显示 Anthropic 当前在 AWS Trainium、Google TPU、NVIDIA GPU、AMD GPU 四类芯片上运行 Claude，其早期押注的多芯片栈适配已投入数年。Anthropic 提到内部工具 Mythos 可将新芯片平台适配周期从过去的数十人月缩短至 3 天，且近 100%的内核由 Claude 编写。路演还提及 Anthropic 的“计算乘数”策略，以及未来递归自我改进阶段 Claude 可自主发现计算乘数的预期。

rss · Simon Willison · 11月11日 15:11

**「为什么重要」** 这是 Anthropic 官方首次在公开路演中详细披露多芯片适配的技术路径与成本优势，为行业评估大模型基础设施跨芯片方案提供了可参考的一手信息。但路演中关于递归自我改进阶段计算乘数自动增长的表述仍属预期，尚未有实际落地证据。

**「可关注」** 可关注：跨芯片适配的工程成本是大模型多芯片策略的核心门槛，Anthropic 通过多年栈适配积累与内部工具自动化，将新芯片接入周期压缩至 3 天，该路径的工程投入与收益比值得基础设施团队参考。

**标签**: `#observability`

---

<a id="item-agent-engineer-8"></a>
### [GTAGym 预印本发布](https://huggingface.co/papers/2611.13028) ⭐️ 6.0/10

2026 年 11 月 12 日 Hugging Face Daily Papers 分享了 GTAGym 预印本（arXiv:2611.13028），该工作面向 GTA V 推出智能体评估与强化学习环境，配套 GTAVBench 基准包含 103 个跨 9 类任务族的在线任务、47 个基于 GTA V 图像的射击/狙击任务，支持自动任务验证，解决此前游戏智能体评估依赖人工标注的痛点；当前仅公开摘要级信息，无深度技术细节与性能数据，影响面局限于游戏/交互式智能体评估相关方向的工程师。

rss · Hugging Face Daily Papers · 11月12日 00:00

**「为什么重要」** 它首次覆盖 AAA 游戏场景提供可自动验证的智能体评估与 RL 训练框架，填补了该领域的工具空白；但当前仅公开预印本摘要，无开源细节与性能数据，实际可用性尚未得到验证。

**「可关注」** 可关注：GTAGym 通过截图与键鼠操作实现任务自动验证，并行测试能力可降低游戏智能体评估的人工标注成本。

**标签**: `#eval`

---

<a id="item-agent-engineer-9"></a>
### [HF 每日论文：Tree-Ising 修复 LLM 权重](https://huggingface.co/papers/2611.14210) ⭐️ 6.0/10

2026 年 11 月 12 日 HF 每日论文收录 arXiv 预印本论文《Tree-Ising: Repairing Language Models with Bit-Level Ising Edits》，该论文当前获得 77 次点赞，研究提出无梯度位级离散优化方法 Tree-Ising，用于修复 LLM 权重以解决推理循环等问题。对比此前 MIT Takehi 等人提出的权重空间编程工作——后者由 GPT-6 Astra agent 修复 Qwen3.5-0.8B 推理循环时消耗 158 轮 agent 交互、8970 万 token、50 次前向请求——Tree-Ising 将修复问题建模为模型自身 BF16 权重上的稀疏离散优化，通过前向统计定义目标：削弱循环方向、强化结论方向、保留生产 token 上的层输出，在状态树表示下允许的编辑为符号翻转和指数偏移，且保留所有共享组指数和尾数。当前该研究仍处于早期阶段，无已落地的生产级工具或协议变更，完整技术细节需参考原论文。

rss · Hugging Face Daily Papers · 11月12日 04:13

**「为什么重要」** 当前仅为早期研究阶段，无已落地的生产级工具或协议变更，对现有 coding agent 工程工作流的直接影响有限，需等待后续验证。

**「可关注」** 可关注：无梯度位级权重修复路径对 LLM 推理异常问题的解决思路。

**标签**: `#coding-agent`

---

<a id="item-agent-engineer-10"></a>
### [HF 每日论文：WICL 机器人操控新范式](https://huggingface.co/papers/2611.12885) ⭐️ 6.0/10

2026 年 11 月 12 日 Hugging Face 每日论文收录 arXiv 预印本 2611.12885，该论文当前获得 65 次 HF 每日论文点赞，提出 World In-Context Learning（WICL） agent 学习范式。该范式让冻结模型从演示出发，在仿真器等环境中执行任务时将交互反馈写入上下文而非权重，既避免训练策略的分布耦合，也补全了标准上下文学习缺少的当前环境反馈问题。配套实现 RoboScript 模块化框架，目前仅在机器人操控场景验证，未公开性能指标与实现细节，通用性待验证。

rss · Hugging Face Daily Papers · 11月12日 04:13

**「为什么重要」** 该工作提出了一种不依赖权重更新的 agent 学习思路，可能为降低策略训练成本、提升跨环境迁移能力提供新方向；但目前仅展示于机器人操控场景，缺乏性能与实现细节，对通用 agent 工程的参考价值尚未得到验证。

**「可关注」** 可关注：将环境交互反馈写入上下文而非模型权重的设计，可能为解耦策略与训练环境分布、降低训练成本提供新思路。

**标签**: `#memory`, `#in-context-learning`, `#agent-learning`, `#robotic-manipulation`

---

<a id="item-agent-engineer-11"></a>
### [HF trending：Qwen3 SGLang 推测解码模型](https://huggingface.co/tencent/Qwen3.8-27B-DSpine-b16) ⭐️ 6.0/10

2026 年 11 月 12 日 Hugging Face trending 出现基于 Qwen3 的推测解码草稿模型 tencent/Qwen3.8-27B-DSpine-b16，标签包含 sglang、speculative-decoding、draft-model，trendingScore 为 186，获 197 次点赞，采用 safetensors 格式，关联论文 arXiv:2609.36173。该模型面向 SGLang 文本生成场景，当前公开条目未提供技术细节、性能基准或架构 specifics，具体推理优化效果与兼容性尚未确认，主要影响做 agent 推理优化、SGLang 相关开发的工程师。

rss · Hugging Face Trending Models · 11月12日 04:13

**「为什么重要」** 该模型属于 Qwen3 生态的推测解码草稿方案，若技术细节验证通过，有望降低 SGLang 文本生成的推理开销，对 agent harness 的推理效率优化有潜在价值。但目前公开信息不足，具体性能增益与落地可行性尚未证实。

**「可关注」** 可关注：该模型关联论文 arXiv:2609.36173，可优先查阅论文获取架构与性能细节，再评估是否接入 SGLang 推理流程。

**标签**: `#harness`

---

<a id="item-agent-engineer-12"></a>
### [BotPsy 0.8B 端侧智能体模型开源](https://huggingface.co/blog/qvac/botpsy) ⭐️ 5.8/10

2026 年 11 月 11 日 Hugging Face 官方博客发布 Tether AI Research 研发的 BotPsy 0.8B 参数端侧智能体语言模型，专为函数调用与智能体工作流优化，基于 Qwen3.5-0.8B 构建，支持设备端本地部署。模型采用 SFT、多教师策略蒸馏、两轮强化学习的四阶段后训练，核心基准测试中较基座 Qwen3.5-0.8B-Think 能力近乎翻倍：BFCL v4 从 23.4 升至 44.0，ACEBench 从 30.1 升至 58.7，τ-bench 从 23.2 升至 51.5；在六项工具调用与智能体基准测试中均超过同参数量级（≤1.2B）的竞品模型，同时在五项测试中超过 2.5 倍参数量级的 Qwen3.5-2B-Think。该模型以 Apache 2.0 协议开源，提供 safetensors 与 GGUF（bf16、Q8、Q4）格式，适配 QVAC SDK 与 llama.cpp，官方明确其仅适合低到中等难度任务，不适合高风险使用场景，仍存在出错可能。

rss · Hugging Face Blog · 11月11日 05:01

**「为什么重要」** 它首次将≤1.2B 参数模型的工具调用与智能体能力提升到接近更大参数量模型的水平，为需要数据隐私、低部署成本的本地智能体工作流提供了可选项，减少了云端大模型的依赖与成本波动风险。目前其性能数据为官方发布，尚未有第三方独立复现验证，实际端侧部署的稳定性与硬件适配表现仍待观察。

**「可关注」** 可关注：BotPsy 在工具调用场景下推理 token 消耗仅为基座 Qwen3.5-0.8B-Think 的约 1/3，多轮对话工具调用能力较基座近乎提升 6 倍，推理循环率从 22.9%降至 1.4%，适合对端侧推理成本与稳定性有要求的轻量智能体场景。

**标签**: `#coding-agent`

---

<a id="item-agent-engineer-13"></a>
### [Simon Willison 工具站加标签云](https://simonwillison.net/2026/Nov/11/tools-tags/) ⭐️ 5.5/10

2026 年 11 月 11 日，Simon Willison 为其个人工具站 tools.simonwillison.net 新增按标签浏览功能，该站目前收录 244 个 vibe 编码工具。他使用 tree-sitter 对工具代码做静态分析，提取各工具依赖的 JavaScript 库、浏览器 API、Web API 宿主信息，生成对应三类标签的标签云，标签大小对应使用该标签的工具数量。该分析工作基于他剩余的 Fable 5.2 额度完成，主要面向关注其工具集的开发者、vibe coding 实践者开放使用。

rss · Simon Willison · 11月11日 18:42

**「为什么重要」** 该实践展示了一种无需执行代码即可提取代码库依赖标签的轻量方案，适合个人工具集、小型项目的依赖归类场景。目前仅为个人项目验证，尚未证实可复用到更大规模的代码分析工作流。

**「可关注」** 可关注：用 tree-sitter 做静态分析提取代码依赖标签，可在不执行代码的前提下完成轻量级代码库的依赖梳理。

**标签**: `#coding-agent`

---

## AI 日报
{: #sec-ai-daily .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-daily" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-daily-1"></a>
### [OpenAI 退伍军人 ChatGPT Plus 计划落地](https://openai.com/index/chatgpt-plus-for-veterans) ⭐️ 7.8/10

OpenAI 官方宣布，其面向美国退伍军人及退役过渡军人推出的 ChatGPT Plus 免费一年计划，已有超 2 万人报名，该计划用途为辅助参与者准备平民职业生涯。

rss · OpenAI Blog · 11月11日 08:00

**「为什么重要」** 这是 OpenAI 针对特定垂直人群的定向产品推广动作，有明确报名数据和用途指向，可观察其面向特定群体的产品落地策略。

**「可关注」** 可关注：OpenAI 退伍军人群体 ChatGPT Plus 免费计划的后续落地数据与使用反馈。

**标签**: `#lab`, `#product`, `#policy`

---

## AI 羊毛
{: #sec-ai-deals .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-deals" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-deals-1"></a>
### [Mu3ic 1.8.0 更新 送码+双 11 优惠](https://www.v2ex.com/t/1256202#reply49) ⭐️ 6.0/10

V2EX 用户 aslehx 分享 Mu3ic 1.8.0 稳定版更新，该版本新增播客、听书功能，优化大曲库同步、浏览、搜索与加载体验，同时推出福利活动：前 50 名可领激活码，后续用户留邮箱可领 6 元优惠券，叠加持续 1 个月的双 11 优惠后售价 26 元（原价 48 元），进群可获取 iOS 端内测资格。

rss · V2EX Hot · 11月11日 08:16

**「为什么重要」** 本次更新补齐播客、听书能力，同时针对大曲库场景优化使用体验，叠加双 11 优惠后入手成本较低，适合有音频内容消费需求的用户。

**「可关注」** 前 50 名发放的激活码不包含 1 年 2 次换机权益，其余权益与常规激活码一致；双 11 优惠持续 1 个月，叠加 6 元券后到手价 26 元。

**标签**: `#promo`, `#coupon`, `#limited-free`

---