---
layout: default
title: "Horizon Summary: 2026-11-12 (EN)"
date: 2026-11-12
lang: en
---

> From 206 items, 18 important content pieces were selected

---

**Agent Harness Architecture**
1. [pydantic-ai v2.68.0 发布](#item-harness-arch-1) ⭐️ 8.8/10
2. [MCP Servers v2.4.0 安全修复发布](#item-harness-arch-2) ⭐️ 8.3/10
3. [LangChain 1.5.0 发布](#item-harness-arch-3) ⭐️ 5.8/10

**AI Agent Engineer**
1. [Gemini Decisions API 发布](#item-agent-engineer-1) ⭐️ 8.0/10
2. [Apple 快速 RAG 检索研究引讨论](#item-agent-engineer-2) ⭐️ 7.0/10
3. [AWS 官方 aws-emulator 发布](#item-agent-engineer-3) ⭐️ 7.0/10
4. [llm 0.37.2 修复密钥泄漏漏洞](#item-agent-engineer-4) ⭐️ 7.0/10
5. [HF Daily Papers 发布 Embodied First Exam](#item-agent-engineer-5) ⭐️ 7.0/10
6. [Tests as Data 模式提出](#item-agent-engineer-6) ⭐️ 7.0/10
7. [Anthropic IPO路演披露多芯片策略](#item-agent-engineer-7) ⭐️ 6.0/10
8. [HF 每日论文：GTAGym 发布](#item-agent-engineer-8) ⭐️ 6.0/10
9. [Tree-Ising BF16 离散优化修复 LLM](#item-agent-engineer-9) ⭐️ 6.0/10
10. [HF 每日论文：WICL 机器人操作](#item-agent-engineer-10) ⭐️ 6.0/10
11. [Qwen3-DSpine 推测解码模型上榜 HF Trending](#item-agent-engineer-11) ⭐️ 6.0/10
12. [BotPsy 0.8B 端侧智能体模型发布](#item-agent-engineer-12) ⭐️ 5.8/10
13. [Simon Willison 标签云上线](#item-agent-engineer-13) ⭐️ 5.5/10

**AI Daily**
1. [OpenAI 退伍军人免费 ChatGPT Plus 计划](#item-ai-daily-1) ⭐️ 7.8/10

**AI Deals**
1. [Mu3ic 1.8.0 更新 送码+双11优惠](#item-ai-deals-1) ⭐️ 6.0/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [pydantic-ai v2.68.0 发布](https://github.com/pydantic/pydantic-ai/releases/tag/v2.68.0) ⭐️ 8.8/10

pydantic-ai v2.68.0 于 2026-11-12 发布。本次更新引入 \`OutputTokenLimitExceeded\` 异常与 \`ModelFallback\` 自动降级机制，当响应在 \`max\_tokens\` 处被截断时自动切换模型。新增 \`RequestInput\` 支持运行内审批与用户输入，\`AskUser\` 移至延迟管线，并标记延迟调用的 \`kind\` 与 \`answered\_by\`。\`DelegationTasks\` 新增 \`discover\(\)\` 方法，且单个损坏的已保存任务不再阻塞 \`opened\(\)\`。工作区后端现需保持分离进程持续运行，并由 \`WorkspaceBackendSuite\` 强制执行检查。

github · dsfaccini · Nov 12, 01:56

**「设计要点」** 运行时支持 Temporal 与 DBOS 作为持久化委托子工作流，\`PromptInjectionDefender\` 语义分类改造为持久化操作以兼容 Temporal。权限系统在持久化执行中保留记忆审批，事件流通过 Vercel AI 与 AG-UI 协议携带 \`canonical\_system\`。

**「改了什么」** 模型回退链新增输出令牌超限触发点，\`ModelFallback\` 在 \`max\_tokens\` 截断时自动切换。子代理任务控制事件重命名并添加 \`agent\_name\` 与 \`parent\_task\_id\` 字段，Harness 层重命名缩写标识符与事件字段，新增 \`RefineOutput\` 能力与 \`GoogleDecisionsModel\` 后端。

**Tags**: `#runtime`, `#subagents`, `#permissions`, `#sandbox`

---

<a id="item-harness-arch-2"></a>
### [MCP Servers v2.4.0 安全修复发布](https://github.com/modelcontextprotocol/servers/releases/tag/v2.4.0) ⭐️ 8.3/10

MCP servers v2.4.0 patches six vulnerabilities across three packages. \`@modelcontextprotocol/server-filesystem\` upgrades to 2.3.0; \`mcp-server-git\` and \`mcp-server-fetch\` both release 2026.11.11. The filesystem server closes a symlink race condition for reads on Linux and macOS by opening files relative to the checked directory, refuses FIFOs/sockets/devices, and narrows the Windows race without resolving it. The Git server blocks repository configuration from executing programs and refuses Git older than 2.31. The fetch server treats IPv6 site-local addresses as private and normalizes paths before robots.txt matching. Date-versioned npm users must explicitly install 2.3.0.

github · cliffhall · Nov 11, 07:07

**「设计要点」** The filesystem server aligns read path resolution with write behavior, opening files relative to the access-checked directory, and introduces \`--read-only-dir\` for per-directory read-only confinement. The Git server injects configuration overrides into every Git command to prevent program execution, rejecting Git versions that ignore these overrides.

**「改了什么」** The filesystem server now validates \`move\_file\` sources before moving and refuses NTFS alternate-data-stream paths, Windows device names, and trailing dots or spaces. The Git server extends \`--repository\` confinement to alternate object stores, linked worktrees, and Git directory symlinks. The fetch server closes path-normalization bypasses in robots.txt handling.

**Tags**: `#mcp`, `#sandbox`, `#tools`, `#permissions`

---

<a id="item-harness-arch-3"></a>
### [LangChain 1.5.0 发布](https://github.com/langchain-ai/langchain/releases/tag/langchain%3D%3D1.5.0) ⭐️ 5.8/10

LangChain 1.5.0 正式发布，最低 Python 版本升至 3.11，langchain-core 最低版本要求同步提升至 1.8.0。本次更新引入 ModelRouterMiddleware（beta）与 auto-mode middleware 两个新中间件。发布说明未提供实现细节、代码路径或架构上下文，无法评估对 agent harness 的具体影响。

github · github-actions\[bot\] · Nov 11, 15:47

**「改了什么」** 移除 Python 3.10 支持，最低依赖升至 langchain-core 1.8.0。新增模型路由中间件与自动模式中间件，前者标记为 beta。

**Tags**: `#runtime`, `#tools`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [Gemini Decisions API 发布](https://blog.google/innovation-and-ai/technology/developers-tools/gemini-decisions-api/) ⭐️ 8.0/10

Google 2026-11-11发布Gemini Decision 1决策模型API，加入Jev、OpenAI的决策模型赛道。该API支持是/否、选择、rubric评分三类问题，复用Jev的术语“Noul”指代是/否问题；定价为每百万输入token 10美分，输出免费，与OpenAI GPT-6 Luna决策模型同价，高于Jev的4.2美分每百万。输入模态覆盖文本、图片、音频、视频、PDF，比仅支持文本的Jev、支持文本和图片的OpenAI覆盖更广；测试显示其对视频的yes/no问题返回0到1之间的概率值，而非另外两款产品的0.0/1.0绝对判断。该API面向需要结构化决策能力的Agent编排、Coding Harness、多模态场景开发者。

hackernews · iamdelirium · Nov 11, 18:32 · [Discussion](https://news.ycombinator.com/item?id=50456791)

**「为什么重要」** 该API首次提供全模态的结构化决策能力，对处理音视频、PDF输入的Agent工具链与评测体系有直接参考价值；但当前定价高于Jev，成本敏感场景需结合实际输入模态需求权衡。

**「可关注」** 可关注多模态决策模型的概率输出粒度与纯文本/图像决策模型的差异，以及不同决策模型API的定价与模态覆盖的trade-off。

**「评论」** 社区讨论聚焦决策模型的落地场景、成本与多模态能力的平衡，有用户指出此前通过语法约束输出获取结构化结果的方案无法得到概率值，也有用户认为当前定价偏高但多模态输入场景实用性强。

**Tags**: `#orchestration`, `#harness`, `#coding-agent`, `#eval`

---

<a id="item-agent-engineer-2"></a>
### [Apple 快速 RAG 检索研究引讨论](https://machinelearning.apple.com/research/faster-retrieval) ⭐️ 7.0/10

2026-11-11，Apple ML Research 发布 &quot;Faster Retrieval for Better, More Efficient RAG&quot; 研究，Hacker News 社区讨论 learned retrieval 方法在 agent 知识管线中的实际权衡。从业者对比了该方法与 grep、embedding 模型及传统 BERT 实现的优劣，讨论集中在速度与质量的取舍、大规模场景适用性，以及检索偏差对 LLM 输出的影响。当前材料未包含该研究的完整技术细节或基准数据。

hackernews · zerop · Nov 11, 16:57 · [Discussion](https://news.ycombinator.com/item?id=50455633)

**「为什么重要」** RAG 是 coding agent 常用的外部知识组件，Apple 作为平台厂商的布局可能影响本地推理与检索管线的设计方向。社区对 learned retrieval 的适用边界存在明显分歧，其实际效果尚未在 agent 工程场景中得到充分验证。

**「可关注」** 可关注：learned retrieval 方法在亿级条目规模下可能具备优势，但在中小规模代码库中，embedding 模型与 grep 的对比结果仍不确定，需结合实际数据验证其是否优于传统检索。

**「评论」** 评论呈现明显分歧：armcat 指出 Spotify 的 Parallel Fusion Router 采用类似范式，但仅适用于超大规模场景；comandillos 认为检索方法会引入 heuristics 偏差，可能降低最终输出质量；mickeyp 对 embedding/BERT 模型在代码库检索中能否超越 grep 表示怀疑，认为过度简化搜索条件会退化为 grep + regex。

**Tags**: `#memory`, `#eval`, `#harness`

---

<a id="item-agent-engineer-3"></a>
### [AWS 官方 aws-emulator 发布](https://simonwillison.net/2026/Nov/11/aws-emulator/) ⭐️ 7.0/10

AWS has released the official local emulator aws-emulator, enabling developers to clone AWS services locally for testing without paid API keys. The tool is written in Rust, with 29,684 commits in its first three weeks, built by a large swarm of agents. AWS executive Swaminathan Sivasubramanian detailed its development process in a guest post on Werner Vogels&\#x27; blog. The emulator was publicly introduced by Simon Willison on November 11, 2026. The current version requires Docker to run on macOS and Windows, serving developers who need to test AWS services locally, as well as teams building agent test harnesses and eval environments.

rss · Simon Willison · Nov 11, 21:18

**「为什么重要」** It is the first officially supported local AWS service emulation solution, eliminating the need for paid API keys and cloud dependencies for AWS service testing, with direct practical value for agent test harness and eval scenarios. The current version only supports Docker-based operation, and a cross-platform standalone binary version has not been released yet, though the author has publicly expressed hope for this improvement.

**「可关注」** Watch for: The current version relies on Docker to run; if a dependency-free standalone binary is released later, it can be more easily integrated into multi-language test suites.

**Tags**: `#harness`, `#eval`, `#tools`

---

<a id="item-agent-engineer-4"></a>
### [llm 0.37.2 修复密钥泄漏漏洞](https://simonwillison.net/2026/Nov/11/llm/) ⭐️ 7.0/10

llm 0.37.2于2026年11月11日发布，核心修复两个安全漏洞（编号GHSA-v9h7-jj4g-f862、GHSA-r639-rr7r-x72w）。漏洞源于extra-openai-models.yaml配置机制缺陷：当配置的api\_key\_name对应密钥从未存储时，工具仍会发送OPENAI\_API\_KEY环境变量到第三方OpenAI兼容端点；此外responses为true的模型通过-o chat\_completions 1参数运行时，也会将存储的openai密钥或环境变量发送至对应第三方端点。该漏洞影响所有使用llm CLI配置OpenAI兼容第三方服务、尤其是处理API凭证的agent工程师。

rss · Simon Willison · Nov 11, 17:19

**「为什么重要」** 这两个漏洞已确认可导致OpenAI API密钥泄露给不受信的第三方服务商，对使用llm构建凭证处理流程的coding agent团队构成直接安全风险，修复版本已公开可立即升级。

**「可关注」** 可关注：使用llm配置OpenAI兼容第三方端点时，需立即升级到0.37.2版本，避免未存储的api\_key\_name配置或responses模型搭配chat\_completions参数的使用组合触发密钥外泄。

**Tags**: `#security`, `#permissions`, `#harness`

---

<a id="item-agent-engineer-5"></a>
### [HF Daily Papers 发布 Embodied First Exam](https://huggingface.co/papers/2611.12177) ⭐️ 7.0/10

2026年11月12日，Hugging Face Daily Papers 分享新论文提出的 Embodied First Exam 评估框架。该框架是面向编码智能体的原生机器人控制评估工具，包含 35 个套件、1156 项多样化任务，覆盖 47 台机器人，支持编码智能体自主选择直接控制、代码控制或训练策略控制的方式。它填补了现有机器人基准仅适配视觉运动策略、不适用于编码智能体的空白，面向需要验证编码智能体物理世界控制能力的工程师群体。

rss · Hugging Face Daily Papers · Nov 12, 04:13

**「为什么重要」** 该框架首次针对编码智能体设计原生机器人控制评估标准，提供了可落地的具体评估规模，为编码智能体进入物理世界前的能力验证提供参考。目前尚无公开证据证明其实际评测效果已被广泛验证。

**「可关注」** 可关注：Embodied First Exam 已公开 1156 项任务、47 台机器人的评估规模，支持编码智能体自主选择控制方式，可作为现有编码智能体物理控制能力的适配验证参考。

**Tags**: `#eval`, `#coding-agent`

---

<a id="item-agent-engineer-6"></a>
### [Tests as Data 模式提出](https://martinfowler.com/articles/tests-as-data.html) ⭐️ 7.0/10

2026-11-11 Martin Fowler 发文提出「tests as data」模式。Matteo Vaccari 主张：AI 写代码时开发者变为其客户，客户测试应成为人机主要契约。该契约应置于测试数据而非测试代码中，以防编码代理意外修改。文章指出过去 DSL 解析器与自定义测试运行器成本高昂，如今 AI 使其廉价，从而优化人类可读的测试契约。此为概念性文章，未提供基准数据或生产环境实证。

rss · Martin Fowler · Nov 11, 15:17

**「为什么重要」** 该模式直接关联 coding agent 与 harness 的 eval 设计，提出将测试视为不可变数据以维护人机契约。但文章未提供生产环境基准或实证数据，影响尚未证实。

**「可关注」** 可关注：当 AI 同时生成生产与测试代码时，将测试视为不可变数据而非可修改代码，可降低代理意外破坏测试覆盖的风险。

**Tags**: `#eval`, `#coding-agent`, `#harness`

---

<a id="item-agent-engineer-7"></a>
### [Anthropic IPO路演披露多芯片策略](https://simonwillison.net/2026/Nov/11/anthropic-ipo-roadshow/) ⭐️ 6.0/10

On November 11, 2026, Simon Willison published a third-party extracted transcript of Anthropic&\#x27;s IPO roadshow video, revealing details from the &quot;Approach to compute&quot; section presented by co-founder Tom Brown that Claude is trained and served across four major chip families: AWS Trainium, Google TPUs, NVIDIA GPUs, and AMD GPUs. The roadshow noted that Anthropic pioneered a multi-chip strategy early on when many considered it not worth the effort, as each chip requires a tailored software and inference stack. This year, when first working with AMD GPUs, Anthropic&\#x27;s internal tool Mythos completed Claude&\#x27;s AMD adaptation in just 3 days with almost no human intervention, and Claude ported or wrote nearly 100% of the kernels. The transcript is a third-party extraction via MacWhisper, not an official Anthropic release, and the roadshow&\#x27;s mention of recursive self-improvement accelerating compute multiplier discovery remains an unverified future expectation. The information is primarily relevant to practitioners in large model infrastructure selection and AI engineering toolchain development.

rss · Simon Willison · Nov 11, 15:11

**「为什么重要」** This roadshow marks Anthropic&\#x27;s first official public disclosure of its multi-chip infrastructure strategy, supplementing earlier fragmented insights such as TPU-specific bugs mentioned in its September last year postmortem. The deployment case of AI tools autonomously completing new chip adaptation provides a reference sample for the efficiency boundaries of AI engineering toolchains, while the claim about recursive self-improvement accelerating compute multiplier discovery remains an unsubstantiated future expectation.

**「可关注」** Pay attention to: the progress of automation in large model cross-chip adaptation, and the engineering feasibility of AI-assisted low-level kernel porting.

**Tags**: `#observability`

---

<a id="item-agent-engineer-8"></a>
### [HF 每日论文：GTAGym 发布](https://huggingface.co/papers/2611.13028) ⭐️ 6.0/10

2026年11月12日，Hugging Face Daily Papers 分享了一篇预印本，介绍面向 GTA V 的智能体评估与强化学习环境 GTAGym，以及配套支持自动任务验证的基准 GTAVBench。GTAVBench 从 GTA V 主线任务衍生，包含 9 类任务族共 150 项任务，其中 103 项为在线任务、47 项为基于图像的射击/狙击任务，配套 Web 服务器提供在线环境与评估接口访问，支持通过截图与键鼠操作开展并行测试，自动完成结果验证。当前仅公开摘要级信息，无深度技术细节与性能数据，应用场景局限于游戏/交互式智能体评估领域，仅对相关方向工程师有参考价值。

rss · Hugging Face Daily Papers · Nov 12, 00:00

**「为什么重要」** GTAGym 解决了游戏智能体评估长期依赖人工标注任务结果的痛点，提供了可自动验证的标准化评估框架。当前仅公开摘要，实际可用性、泛化能力以及对非游戏场景的参考价值尚未得到验证。

**「可关注」** 可关注：GTAGym 的自动任务验证与并行测试能力，或可复用到其他交互式智能体评估场景的基准设计中。

**Tags**: `#eval`

---

<a id="item-agent-engineer-9"></a>
### [Tree-Ising BF16 离散优化修复 LLM](https://huggingface.co/papers/2611.14210) ⭐️ 6.0/10

On 2026-11-12, Hugging Face Daily Papers featured arXiv preprint 2611.14210 presenting Tree-Ising, a gradient-free bit-level discrete optimization method for repairing LLM weights to address issues like reasoning loops. The method casts repair as sparse optimization over a model&\#x27;s BF16 weights, where admissible edits are sign flips and exponent shifts that preserve all shared group exponents and mantissas, with lossless BF16 storage as a special case within a state-tree representation. It extends prior MIT weight-space programming work in which a GPT-6 Astra agent corrected Qwen3.5-0.8B reasoning loops without gradients, using 158 agent turns, 89.7 million tokens, and 50 forward-pass requests. The current summary is truncated, and the approach remains early-stage research with no immediate production-ready tooling or protocol changes for agent engineering workflows.

rss · Hugging Face Daily Papers · Nov 12, 04:13

**「为什么重要」** This work provides a concrete gradient-free formulation for bit-level weight editing, which could offer a new avenue for efficient agent-driven model customization. However, the practical impact is unconfirmed; as an early-stage preprint without validated production implementations or reported performance gains, it currently serves as a research direction rather than an actionable engineering change.

**「可关注」** 可关注：Tree-Ising frames weight repair as sign flips and exponent shifts on BF16 weights that preserve shared group exponents and mantissas within a state-tree representation, offering a formal perspective on sparse, lossless model weight editing.

**Tags**: `#coding-agent`

---

<a id="item-agent-engineer-10"></a>
### [HF 每日论文：WICL 机器人操作](https://huggingface.co/papers/2611.12885) ⭐️ 6.0/10

2026年11月12日Hugging Face每日论文收录arXiv预印本，提出World In-Context Learning（WICL）新型智能体学习范式，该论文当日获65次社区点赞。该范式将环境/仿真器交互反馈写入冻结模型的上下文而非权重，避免训练策略的分布耦合，同时补全标准上下文学习缺失的环境反馈。配套实现RoboScript为模块化上下文脚本框架，但当前摘录内容截断，未公开性能数据与实现细节，验证场景仅限机器人操作，通用智能体工程场景的适用性未证实。

rss · Hugging Face Daily Papers · Nov 12, 04:13

**「为什么重要」** 该工作从机制层面绕开了训练策略的分布耦合问题，为智能体上下文学习提供了新的架构思路，但当前仅展示机器人操作场景，尚未证实对通用智能体工程的适用性。

**「可关注」** 可关注：WICL将环境反馈写入上下文而非权重的设计，绕开了训练策略的分布耦合，但当前仅公开机器人操作场景的验证，无完整实现与性能数据。

**Tags**: `#memory`, `#in-context-learning`, `#agent-learning`, `#robotic-manipulation`

---

<a id="item-agent-engineer-11"></a>
### [Qwen3-DSpine 推测解码模型上榜 HF Trending](https://huggingface.co/tencent/Qwen3.8-27B-DSpine-b16) ⭐️ 6.0/10

Hugging Face Trending Models 于 2026-11-12 列出 tencent/Qwen3.8-27B-DSpine-b16，这是一个基于 Qwen3 的推测解码 draft model，兼容 SGLang 文本生成。该模型标签包含 safetensors、dspine、speculative-decoding、draft-model、sglang、text-generation，trendingScore=186，获 197 个 likes。当前 listing 未提供性能基准、架构细节或技术说明。

rss · Hugging Face Trending Models · Nov 12, 04:13

**「为什么重要」** 该模型针对 agent 推理优化设计，可能对 coding agent 的推理效率有潜在价值。但缺乏具体性能数据，实际收益尚不明确。

**「可关注」** 可关注：SGLang 生态中基于 Qwen3 的 draft model 新选项出现，但需查看模型页或关联论文（arxiv:2609.36173）确认吞吐量、延迟及兼容性细节。

**Tags**: `#harness`

---

<a id="item-agent-engineer-12"></a>
### [BotPsy 0.8B 端侧智能体模型发布](https://huggingface.co/blog/qvac/botpsy) ⭐️ 5.8/10

Hugging Face官方博客2026年11月11日发布BotPsy，为Tether AI Research推出的0.8B参数端侧智能体语言模型，基于Qwen3.5-0.8B构建，针对函数调用与智能体工作流优化，采用SFT、多教师策略蒸馏、两轮强化学习的四阶段后训练流程，提供bf16、Q8、Q4三种精度格式，以Apache 2.0开源协议发布，支持Hugging Face safetensors与GGUF两种文件格式。官方测试显示，BotPsy在BFCL v4、ACEBench、τ-bench等6项工具调用与智能体基准中均优于测试过的所有≤1.2B参数模型，且在5项基准中超过2.5倍参数的Qwen3.5-2B-Think；但模型仅适配低到中等难度任务，不适合高风险场景，当前公开内容未包含完整技术细节、部署指南与第三方复现结果。

rss · Hugging Face Blog · Nov 11, 05:01

**「为什么重要」** 该模型验证了亚十亿参数端侧智能体在工具调用场景的可行性，为需要低延迟、隐私保护、规避云LLM成本的coding agent场景提供了新的轻量选项；但其实际端侧部署表现、复杂任务泛化能力与长期稳定性尚未有公开验证，影响仍待观察。

**「可关注」** 可关注：BotPsy针对工具调用优化的亚十亿参数训练方案，以及多精度开源格式对本地轻量agent部署的潜在价值，但需等待完整技术文档与第三方评测确认实际落地表现。

**Tags**: `#coding-agent`

---

<a id="item-agent-engineer-13"></a>
### [Simon Willison 标签云上线](https://simonwillison.net/2026/Nov/11/tools-tags/) ⭐️ 5.5/10

Simon Willison 于 2026-11-11 为其个人工具集 tools.simonwillison.net 新增标签云浏览功能，该集目前收录 244 个 vibe-coding 工具。他使用 tree-sitter 静态分析每个工具的 JavaScript 代码，提取所用库（如 Marked 12 次、Pyodide 11 次）、浏览器 API（如 ES modules 92 次、Clipboard API 69 次）及 Web API 宿主依赖，生成可点击的标签云。该分析通过 Fable 5.2 完成，此前工具集仅支持列表或搜索浏览。此更新仅影响该个人项目的浏览体验，未涉及通用框架变更，对 agent 工程工作流的直接适用性有限。

rss · Simon Willison · Nov 11, 18:42

**「可关注」** 可关注：tree-sitter 可用于静态分析小型工具代码库中的 JavaScript 依赖，提取库与 API 使用模式，无需运行代码。

**Tags**: `#coding-agent`

---

## AI Daily

<a id="item-ai-daily-1"></a>
### [OpenAI 退伍军人免费 ChatGPT Plus 计划](https://openai.com/index/chatgpt-plus-for-veterans) ⭐️ 7.8/10

OpenAI 官方公告显示，已有超过 2 万名美国退伍军人及正在过渡的服役人员注册其定向提供的免费一年 ChatGPT Plus 权益，该权益旨在支持相关人群准备平民职业。

rss · OpenAI Blog · Nov 11, 08:00

**「为什么重要」** 该计划是 OpenAI 针对特定群体的用户触达动作，公开了 AI 工具在职业过渡场景落地的具体用户覆盖数据，属于可验证的产品落地事实。

**「可关注」** 可关注：针对特定人群的 AI 工具定向权益投放可形成可量化的用户增长路径。

**Tags**: `#lab`, `#product`, `#policy`

---

## AI Deals

<a id="item-ai-deals-1"></a>
### [Mu3ic 1.8.0 更新 送码+双11优惠](https://www.v2ex.com/t/1256202#reply49) ⭐️ 6.0/10

V2EX 用户 aslehx 分享 Mu3ic 1.8.0 稳定版更新，该版本新增播客、听书功能，深度优化第三方大体量音乐服的曲库同步、搜索、加载体验，升级支持自适应彩胶纹理的横屏唱机皮肤。福利规则：前 50 名可领激活码（无 1 年 2 次换机权益，其余权益不变），后续用户留邮箱可获 6 元优惠券，叠加持续 1 个月的双 11 优惠后售价 26 元（原价 48 元），iOS 内测资格需进群获取。

rss · V2EX Hot · Nov 11, 08:16

**「为什么重要」** 该版本将 Mu3ic 从音乐播放器扩展为支持音乐、电台、播客、听书的音频内容消费终端，当前叠加限量激活码和双 11 优惠，是低成本体验的窗口期。

**「可关注」** 可关注：Mu3ic 1.8.0 支持 Navidrome、Jellyfin、Emby、Audiobookshelf 等第三方媒体服务，新增拼音模糊搜索、RSS/OPML 导入播客订阅功能，针对数十万级曲库的检索、加载性能做了专项优化。

**Tags**: `#promo`, `#coupon`, `#limited-free`

---