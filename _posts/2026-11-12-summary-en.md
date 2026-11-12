---
layout: default
title: "Horizon Summary: 2026-11-12 (EN)"
date: 2026-11-12
lang: en
---

> From 211 items, 17 important content pieces were selected

---

**Agent Harness Architecture**
1. [Model Context Protocol servers v2.4.0 发布](#item-harness-arch-1) ⭐️ 7.8/10
2. [pydantic-ai v2.68.0 发布](#item-harness-arch-2) ⭐️ 6.8/10
3. [OpenAI Codex rust-v0.167.2 发布](#item-harness-arch-3) ⭐️ 5.3/10

**AI Agent Engineer**
1. [llm 0.37.2 修复密钥泄漏漏洞](#item-agent-engineer-1) ⭐️ 8.0/10
2. [Gemini Decisions API 发布](#item-agent-engineer-2) ⭐️ 7.0/10
3. [AWS 官方本地模拟器 aws-emulator 发布](#item-agent-engineer-3) ⭐️ 7.0/10
4. [HF Daily Paper: WikiTrace 缓解记忆退化](#item-agent-engineer-4) ⭐️ 7.0/10
5. [Embodied First Exam 框架](#item-agent-engineer-5) ⭐️ 7.0/10
6. [HF 每日论文：BioAgent-DF 审计框架](#item-agent-engineer-6) ⭐️ 7.0/10
7. [Tests as Data 测试策略提出](#item-agent-engineer-7) ⭐️ 7.0/10
8. [Apple 高效 RAG 检索研究引讨论](#item-agent-engineer-8) ⭐️ 6.0/10
9. [Anthropic IPO路演披露多芯片训练策略](#item-agent-engineer-9) ⭐️ 6.0/10
10. [FINCOSMOS 金融智能体开放评估范式](#item-agent-engineer-10) ⭐️ 6.0/10
11. [BotPsy 0.8B 端侧 Agent 模型开源](#item-agent-engineer-11) ⭐️ 5.8/10
12. [Inflect v3 本地 TTS 发布](#item-agent-engineer-12) ⭐️ 5.5/10

**AI Daily**
1. [OpenAI 退伍军人免费 ChatGPT Plus 申领破 2 万](#item-ai-daily-1) ⭐️ 5.8/10

**AI Deals**
1. [Mu3ic 1.8.0 送码 双11优惠](#item-ai-deals-1) ⭐️ 7.0/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [Model Context Protocol servers v2.4.0 发布](https://github.com/modelcontextprotocol/servers/releases/tag/v2.4.0) ⭐️ 7.8/10

Model Context Protocol servers v2.4.0 发布，修复 filesystem、git、fetch 三个 MCP 服务器的 6 个关键安全漏洞。filesystem 服务器将读操作绑定到已检查目录，消除符号链接竞争条件，并拒绝 FIFO、socket 和 device 文件；Windows 平台仅缩小竞争窗口而未完全关闭。git 服务器覆盖仓库本地配置（core.fsmonitor、diff.external、hooks、filter 和 merge drivers、signing），防止任意程序执行，并拒绝 Git 低于 2.31 的仓库。fetch 服务器将 IPv6 站点本地地址视为私有，修复 robots.txt 路径绕过。升级目标：@modelcontextprotocol/server-filesystem 2.3.0、mcp-server-git 2026.11.11、mcp-server-fetch 2026.11.11。

github · cliffhall · Nov 11, 07:07

**「设计要点」** filesystem 服务器读工具和文件资源现在相对于已检查目录打开文件，与写入行为一致。git 服务器强制覆盖仓库配置并拒绝旧版 Git。fetch 服务器私有地址检查扩展至 IPv6 站点本地地址，robots.txt 匹配同时检查站点解析路径和原始路径。

**「改了什么」** 修复 6 个 CVE：filesystem 符号链接竞争条件（GHSA-p9cv-8g75-4xcg）、move\_file 路径穿越（GHSA-7m4x-rv66-mxhh）、git 仓库配置命令注入（GHSA-6hqx-gqrx-c5r2）、git 仓库隔离绕过（GHSA-q74p-4wrc-q7w6）、fetch IPv6 私有地址误判（GHSA-3rxj-6jhw-qfv7）、fetch robots.txt 绕过（GHSA-f9hh-cmx9-2f23）。filesystem 新增 --read-only-dir 参数，拒绝 NTFS 备用数据流及 Windows 设备名路径。server-everything 默认将 HTTP 传输绑定到回环地址，Docker 镜像以非 root 用户运行。server-memory 更新至 2.1.1。

**Tags**: `#mcp`, `#tools`, `#permissions`, `#sandbox`

---

<a id="item-harness-arch-2"></a>
### [pydantic-ai v2.68.0 发布](https://github.com/pydantic/pydantic-ai/releases/tag/v2.68.0) ⭐️ 6.8/10

pydantic-ai v2.68.0 发布，新增输出 token 超限时的模型回退机制、延迟用户输入管道、委托任务发现与修复，以及工作区后端进程存活要求。运行时层面支持 Temporal 和 DBOS 持久化子工作流，并将提示注入防御器语义分类改为持久化操作。Harness 侧新增 \`RefineOutput\` 能力、对话存储接口，并重命名多个事件与字段以统一命名规范。

github · dsfaccini · Nov 12, 01:56

**「设计要点」** 工作区后端必须保持分离进程存活，测试套件会校验重连能力。委托任务与用户交互均支持持久化执行，子代理事件统一加 \`Event\` 后缀并携带 \`agent\_name\` 与 \`parent\_task\_id\`。

**「改了什么」** 新增 \`OutputTokenLimitExceeded\` 异常，\`ModelFallback\` 在 \`max\_tokens\` 截断时自动切换模型。\`AskUser\` 移至延迟管道，新增 \`RequestInput\` 支持运行内审批与问答。\`DelegationTasks\` 增加 \`discover\(\)\` 方法，单条损坏任务不再阻塞 \`opened\(\)\`。工作区后端强制要求分离进程持续运行，harness 字段与事件命名规范化并新增 \`RefineOutput\` 能力。

**Tags**: `#runtime`, `#tools`, `#subagents`, `#sandbox`

---

<a id="item-harness-arch-3"></a>
### [OpenAI Codex rust-v0.167.2 发布](https://github.com/openai/codex/releases/tag/rust-v0.167.2) ⭐️ 5.3/10

OpenAI Codex agent harness发布patch版本rust-v0.167.2。本次更新将Google Cloud Vertex AI部署的工具更新默认行为改为增量发送，替代旧版非增量模式。用户可在\`config.toml\`的\`\[features\]\`段设置\`incremental\_tools\_legacy\_gcp = false\` opting out，回退到旧版行为。变更仅针对GCP Vertex AI，不影响其他provider。

github · github-actions\[bot\] · Nov 11, 22:44

**「改了什么」** 相对上一版，本版本在Google Cloud Vertex AI上默认启用增量工具更新。新增配置项\`incremental\_tools\_legacy\_gcp\`（位于\`config.toml\`的\`\[features\]\`段），设为\`false\`可恢复非增量更新。相关实现见PR \#60617与\#60848。

**Tags**: `#tools`, `#runtime`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [llm 0.37.2 修复密钥泄漏漏洞](https://simonwillison.net/2026/Nov/11/llm/) ⭐️ 8.0/10

llm 0.37.2 于 2026-11-11 发布，修复两个安全漏洞（GHSA-v9h7-jj4g-f862、GHSA-r639-rr7r-x72w）。通过 extra-openai-models.yaml 配置 OpenAI 兼容端点时，若 api\_key\_name 未存储，或对 responses: true 模型使用 -o chat\_completions 1，OPENAI\_API\_KEY 环境变量或已存储的 openai 密钥可能泄漏至第三方。修复后上述场景返回 No key found 错误而非发送密钥。影响所有使用 llm openai endpoint add 或手动编辑 extra-openai-models.yaml 的用户。

rss · Simon Willison · Nov 11, 17:19

**「为什么重要」** 这值得今天看，因为 llm 常作为 coding agent 的底层工具链组件，密钥泄漏风险直接影响代理执行环境的安全边界。已发生的修复明确了第三方端点调用时的密钥发送逻辑，但尚未证实实际泄漏事件或下游代理框架的受影响范围。

**「可关注」** 可关注：llm 0.37.2 收紧了 OpenAI 兼容端点的密钥发送逻辑，api\_key\_name 缺失或 responses: true 模型强制切换格式时，工具链不再隐式传递环境变量中的密钥，而是显式报错。

**Tags**: `#permissions`, `#security`, `#toolchain`, `#release`

---

<a id="item-agent-engineer-2"></a>
### [Gemini Decisions API 发布](https://blog.google/innovation-and-ai/technology/developers-tools/gemini-decisions-api/) ⭐️ 7.0/10

2026年11月11日Google发布Gemini Decisions API，配套模型Gemini Decision 1正式进入决策模型赛道，与Jev、OpenAI决策模型形成竞争。该模型支持是/否、多选、rubric评分三类问题，复用Jev的“Noul”术语指代是/否问题；定价为每百万输入token 10美分、输出免费，高于Jev的4.2美分/百万输入token，与OpenAI同档位决策模型定价一致。Gemini Decision 1支持文本、图片、音频、视频、PDF输入，覆盖模态多于仅支持文本的Jev、支持文本和图片的OpenAI。测试显示其对视频的yes/no问题返回连续概率值而非0/1二元结果，例如识别视频中机器人的概率为0.9234。该API主要面向需要结构化决策输出的agent编排、coding harness、评估场景的开发者。

hackernews · iamdelirium · Nov 11, 18:32 · [Discussion](https://news.ycombinator.com/item?id=50456791)

**「为什么重要」** 当前决策模型赛道刚兴起，Gemini Decision 1的全模态输入是现有同类产品没有的能力，可能覆盖视频、音频相关的agent校验场景；但其实际效果、成本收益比尚未有大规模验证，是否能在coding harness等场景替代现有方案仍不明确。

**「可关注」** 可关注：Gemini Decision 1的多模态输入能力是否能在音视频相关的agent校验、评估场景中提供比多步推理更高效的方案，同时需权衡其比Jev高出一倍多的输入成本。

**「评论」** 社区普遍认可决策模型是刚被验证有用的赛道，Gemini的全模态输入是核心差异点；但对其高于Jev的定价存在争议，部分用户认为多模态场景下成本可接受，也有用户提到基于Gemma微调的span-02决策模型表现不错，对Gemini的实际效果持观望态度。

**Tags**: `#orchestration`, `#coding-agent`, `#harness`, `#eval`

---

<a id="item-agent-engineer-3"></a>
### [AWS 官方本地模拟器 aws-emulator 发布](https://simonwillison.net/2026/Nov/11/aws-emulator/) ⭐️ 7.0/10

AWS 发布官方 aws-emulator，支持本地克隆 AWS 服务进行测试，无需付费 API 密钥。项目主要由 AI agents 构建，三周内累计 29,684 次提交，使用 Rust 编写。当前版本要求 macOS 或 Windows 环境运行 Docker，尚未提供单二进制分发。

rss · Simon Willison · Nov 11, 21:18

**「为什么重要」** 本地模拟器可直接替代付费 API 密钥进行 AWS 服务测试。AI agents 在三周内完成近三万次提交的工程实践，提供了大规模自动化编码的实证样本。

**「可关注」** 可关注：Docker 依赖与单二进制需求的矛盾，以及 Rust 实现是否扩展至其他平台。

**Tags**: `#harness`, `#eval`, `#coding-agent`, `#permissions`

---

<a id="item-agent-engineer-4"></a>
### [HF Daily Paper: WikiTrace 缓解记忆退化](https://huggingface.co/papers/2611.14320) ⭐️ 7.0/10

2026-11-12，Hugging Face Daily Papers 推送论文《Don&\#x27;t Just Trust Your Memory》，提出 WikiTrace 证据链接记忆系统。该系统让 LLM agent 在应用 lessons 前可回溯核对原始轨迹，减少因错误或误用记忆导致的性能退化。论文指出，现有记忆系统仅以任务成败标注轨迹，却不附带轨迹来源，导致 agent 无法验证记忆正确性。该研究为 agent 记忆工程提供设计思路，但具体实现与实验规模未完全披露。

rss · Hugging Face Daily Papers · Nov 12, 03:33

**「为什么重要」** 该论文直接针对 agent 记忆系统的一个常见失效模式给出可验证的缓解方案，而非仅停留在问题描述。对构建依赖外部记忆的 coding agent 而言，证据链接机制可能改变记忆检索与验证的工程边界，但实际收益仍需复现实验确认。

**「可关注」** 可关注：记忆系统若仅提供 lessons 而不保留轨迹来源，agent 将无法识别错误记忆，WikiTrace 的交叉验证设计提示记忆模块需同步存储证据链路。

**Tags**: `#memory`, `#llm-agent`, `#agent-architecture`

---

<a id="item-agent-engineer-5"></a>
### [Embodied First Exam 框架](https://huggingface.co/papers/2611.12177) ⭐️ 7.0/10

Hugging Face Daily Papers 于 2026-11-12 发布论文 arXiv:2611.12177，提出 Embodied First Exam 评估框架。该框架面向 coding agents 控制物理机器人，覆盖 47 个机器人、35 个套件、1,156 个任务，支持直接控制、code-to-control 与训练策略控制三种范式，并包含 9 个新任务套件。现有 robotics 基准多围绕 visuomotor policy learning 构建，本框架首次提供 agent-native 替代方案，供 coding agents 在进入物理世界前接受统一考核。源内容截断，未披露完整动态任务细节，社区采纳情况尚不确定。

rss · Hugging Face Daily Papers · Nov 12, 03:33

**「为什么重要」** 该框架首次将 coding agents 的评估范围从软件任务延伸到物理机器人控制，填补了 agent-native 具身评估空白。是否成为社区标准、实际接入 harness 的成本与任务难度，仍需后续验证。

**「可关注」** 可关注：其直接控制、code-to-control 与训练策略控制三种范式与现有 visuomotor 基准的接口差异，评估接入 harness 的额外成本。

**Tags**: `#eval`, `#coding-agent`

---

<a id="item-agent-engineer-6"></a>
### [HF 每日论文：BioAgent-DF 审计框架](https://huggingface.co/papers/2611.01527) ⭐️ 7.0/10

2026年11月12日HF每日论文收录BioAgent-DF审计框架相关研究，该框架针对生物医学研究智能体的决策溯源问题，通过在相同科学计算位点保存配对参考与候选值、恢复或移植后运行智能体，测试证据与输出的分离性。实验覆盖8个SciFact批次，Qwen3.5-4B在3组捕获-声明组合出现可重复引用变化，Gemma 3 4B IT在4组组合出现可重复读取与引用变化，共覆盖2个声明；完全恢复参考证据集时判决结果不变，基线提示词下的判决变化在显式示例提示词下未复现，另有补充工具与优化器实验但内容被截断。该研究目前仅针对生物医学研究智能体，可推广性未验证。

rss · Hugging Face Daily Papers · Nov 12, 03:33

**「为什么重要」** 该研究提供了可操作的智能体决策鲁棒性审计方法，验证了工具状态证据摆放位置对输出的影响，以及显式示例提示词的缓解作用，对智能体harness设计与工具链开发有参考价值；但领域限定在生物医学研究场景，通用性尚未验证。

**「可关注」** 可关注工具状态证据的摆放位置对智能体输出的影响，显式示例提示词可缓解非预期的判决变化，可用于智能体鲁棒性测试与工具链设计参考。

**Tags**: `#eval`, `#harness`

---

<a id="item-agent-engineer-7"></a>
### [Tests as Data 测试策略提出](https://martinfowler.com/articles/tests-as-data.html) ⭐️ 7.0/10

2026-11-11，Martin Fowler 网站发布 Matteo Vaccari 文章《Tests as data: ensuring AI-generated code does what we want》。文章提出：AI 编码助手同时生成生产代码与测试代码时，开发者应将测试视为人类可读的数据契约，而非开发者编写的测试代码，以保留测试对意外 AI 修改的防护价值。文章提出三项主张：AI 写代码时开发者成为其客户；客户测试而非开发者测试成为人机间主要契约；将该契约置于测试数据而非测试代码中，更易保护其不被编码代理意外修改。文章指出过去 DSL 解析器与自定义测试运行器成本高昂，而 AI 使其变得廉价，但当前摘录为概念性阐述，未提供实证基准、代码示例或突破性技术变更。

rss · Martin Fowler · Nov 11, 15:17

**「为什么重要」** 该文直接关联 AI agent 的 eval 与 harness 设计，提出将测试从“代码”重新定义为“数据契约”的概念框架，可能影响未来 coding agent 的验证策略。但当前材料仅为概念摘录，未提供可复现实验或对比基线，实际影响尚未证实。

**「可关注」** 可关注：当 AI 同时生成生产代码与测试代码时，传统测试代码的防护假设失效，需考虑将测试规范表达为人类可读的数据契约而非可执行代码。

**Tags**: `#eval`, `#harness`, `#coding-agent`

---

<a id="item-agent-engineer-8"></a>
### [Apple 高效 RAG 检索研究引讨论](https://machinelearning.apple.com/research/faster-retrieval) ⭐️ 6.0/10

2026-11-11，HackerNews 用户 zerop 分享 Apple 官方机器学习研究《Faster Retrieval for Better, More Efficient RAG》。原帖未附论文核心技术细节，仅提供外部链接。社区评论提及 Spotify 的 Parallel Fusion Router 等 learned retrieval 方案，并讨论检索速度与输出质量的权衡。该研究关联 agent 记忆与知识系统构建，但完整技术价值需查阅原文确认。

hackernews · zerop · Nov 11, 16:57 · [Discussion](https://news.ycombinator.com/item?id=50455633)

**「为什么重要」** RAG 检索效率决定 agent 响应速度与成本。Apple 以平台厂商身份布局该领域，可能推动端侧推理与本地知识检索整合，但具体技术方案与性能数据尚未公开。

**「可关注」** 可关注：社区反馈显示 embedding 模型在代码库检索场景下效果有限，传统搜索（如 grep）在该场景仍具竞争力。

**「评论」** 社区对 learned retrieval 与传统检索的适用边界存在分歧。部分开发者基于代码库经验质疑 embedding 模型效果，另有观点指出此类方法更适用于超大规模索引场景。

**Tags**: `#memory`, `#harness`, `#coding-agent`

---

<a id="item-agent-engineer-9"></a>
### [Anthropic IPO路演披露多芯片训练策略](https://simonwillison.net/2026/Nov/11/anthropic-ipo-roadshow/) ⭐️ 6.0/10

2026年11月11日，Simon Willison发布对Anthropic IPO路演视频的非官方转录总结，披露Anthropic联合创始人Tom Brown介绍Claude已实现跨AWS Trainium、Google TPU、NVIDIA GPU、AMD GPU四类芯片的训练与推理，源于其早期押注的多芯片策略。关键细节包括：此前接入新芯片平台需数十名工程师耗时数月，2026年首次接入AMD GPU时，内部工具Mythos仅用3天、几乎无人工干预即完成Claude的AMD适配，近100%的内核由Claude自行编写或移植。路演还提及Anthropic通过发现“计算倍率”提升总有效算力，并预期接近递归自我改进阶段时，Claude可自行发现计算倍率。当前信息来自非官方转录，无官方完整文本，内容存在截断，主要影响AI基础设施、大模型训练推理工程团队及关注Anthropic技术路线的从业者。

rss · Simon Willison · Nov 11, 15:11

**「为什么重要」** 已发生的部分是公开了Anthropic跨多芯片适配的多年工程成果，以及用AI辅助完成新芯片平台迁移的实际实践；尚未证实的是其提出的计算倍率叠加效应、递归自我改进加速算力增长的论断暂无公开验证，对行业的具体影响仍需观察。

**「可关注」** 可关注：大模型跨多芯片架构适配的工程化沉淀，以及用模型自身完成底层内核移植的实践路径。

**Tags**: `#observability`

---

<a id="item-agent-engineer-10"></a>
### [FINCOSMOS 金融智能体开放评估范式](https://huggingface.co/papers/2611.07464) ⭐️ 6.0/10

2026年11月12日Hugging Face Daily Papers推送FINCOSMOS相关论文（获22次upvote），该研究提出面向金融领域智能体的开放世界评估范式，旨在解决现有封闭式基准无法测量智能体静默失败的痛点。核心设计为：隐藏的用户策略由组合语法采样生成，仅在被询问时透露，智能体需自行从网络获取数据并匹配该策略，现有基准通过固定任务、数据或时间线规避了相关失败场景。该范式主要面向金融智能体研发与评估方向的工程师。

rss · Hugging Face Daily Papers · Nov 12, 03:33

**「为什么重要」** 现有金融智能体评估基准普遍封闭化，无法覆盖开放网络环境下的静默失败场景，FINCOSMOS的范式设计为相关评估工作提供了新的思路。但该研究的完整技术细节、性能验证结果尚未公开，实际落地价值还需进一步确认。

**「可关注」** 可关注：现有封闭式金融智能体基准会掩盖执行错误策略、使用未验证数据、回测数据泄露等静默失败，若需设计开放环境下的智能体评估用例，可参考FINCOSMOS对数据来源、策略对齐的要求。

**Tags**: `#eval`

---

<a id="item-agent-engineer-11"></a>
### [BotPsy 0.8B 端侧 Agent 模型开源](https://huggingface.co/blog/qvac/botpsy) ⭐️ 5.8/10

Hugging Face Blog 于 2026-11-11 发布 BotPsy，一款 0.8B 参数端侧 Agentic LLM，基于 Qwen3.5-0.8B 并专攻 function calling。模型以 Apache 2.0 开源，提供 bf16、Q8、Q4 三种精度权重，面向低至中等难度任务。Tether AI Research 声称其在 BFCL v4、ACEBench、τ-bench 等六个 tool-use 与 agentic 基准上达到 ≤1.2B 参数级别 SOTA，并在五项测试中超过 2.5 倍大的 Qwen3.5-2B-Think。文章同时指出模型仍会犯错，不适合高风险场景，且未提供完整技术规格、训练数据细节或独立基准验证。

rss · Hugging Face Blog · Nov 11, 05:01

**「为什么重要」** 端侧小模型持续逼近更大模型的 tool-use 能力，可能降低自托管 Agent 的算力成本与数据隐私风险。但当前信息仅来自官方博客，缺少独立复现、真实延迟数据和硬件适配细节，实际影响尚未证实。

**「可关注」** 可关注：BotPsy 的四阶段训练流程（SFT → MOPD → 两轮 RL）及其声称的推理 token 压缩（GPQA Diamond 约为基座模型的 1/3）可作为轻量级 Agent 模型设计的参考基线，但需等待权重发布与独立验证。

**Tags**: `#coding-agent`, `#on-device`, `#function-calling`

---

<a id="item-agent-engineer-12"></a>
### [Inflect v3 本地 TTS 发布](https://www.reddit.com/r/LocalLLaMA/comments/1xtzwxf/i_released_inflect_v3_lightweight_local_tts_in/) ⭐️ 5.5/10

Inflect v3 发布，包含 Mini（34.31M 参数，6 种音色）、Micro（11.79M 参数）、Atom（157K 参数）三款本地 TTS 模型。Mini 支持参考音色调优、8 种声学事件标签（\[laugh\]、\[sigh\] 等），可在 CPU 与 CUDA 上运行，权重与推理代码采用 Apache 2.0 许可。公告未提供延迟、RTF 或主观听感对比数据。

reddit · r/LocalLLaMA · /u/b111ue · Nov 12, 01:36

**「为什么重要」** 该模型系列为 agent 工具链提供本地语音输出选项，34M 参数规模与 CPU 运行能力降低了部署门槛，但缺乏公开性能基准，实际效果待验证。

**「可关注」** 可关注：声学事件标签与参考音色调优可作为 agent 语音交互的差异化能力，但需在目标硬件上实测 RTF 与音质是否满足产品要求。

**Tags**: `#toolchain`

---

## AI Daily

<a id="item-ai-daily-1"></a>
### [OpenAI 退伍军人免费 ChatGPT Plus 申领破 2 万](https://openai.com/index/chatgpt-plus-for-veterans) ⭐️ 5.8/10

OpenAI 官方博客宣布，已有超过 2 万名退伍军人及正在过渡的服役人员申领了为期一年的免费 ChatGPT Plus，用于辅助准备平民职业。该里程碑属于现有公益项目，未伴随新模型发布、功能更新或政策调整。

rss · OpenAI Blog · Nov 11, 08:00

**「为什么重要」** 该项目是 OpenAI 面向特定群体的 AI 工具福利计划，覆盖超 2 万目标用户，为 AI 在职业过渡、公共服务等场景的落地提供了可参考的实践案例。

**「可关注」** 可关注：AI 工具在职业过渡、技能提升等公共服务场景的落地进展与用户反馈。

**Tags**: `#product`, `#lab`

---

## AI Deals

<a id="item-ai-deals-1"></a>
### [Mu3ic 1.8.0 送码 双11优惠](https://www.v2ex.com/t/1256202#reply46) ⭐️ 7.0/10

V2EX用户aslehx分享称Mu3ic迎来1.8.0史诗级更新，定位最强音频内容消费终端，支持音乐、电台、播客、听书全场景，深度优化第三方大体量音乐服的曲库同步、浏览、搜索与加载体验，同时升级横屏唱机皮肤与智能标签检索。福利方面：前50名用户可免费领取激活码，该激活码不支持1年2次换机权益，其余权益不变；后续用户留邮箱可获6元优惠券，叠加持续1个月的双11优惠后，软件售价为26元（原价48元）；进官方Telegram群可获取iOS端内测资格。

rss · V2EX Hot · Nov 11, 08:16

**「为什么重要」** 当前双11优惠持续1个月，前50名送激活码活动仍在进行，现在参与可享受免费权益或26元的优惠价格，同时可进群获取iOS端内测资格。

**「可关注」** Mu3ic 1.8.0支持对接Navidrome、Jellyfin、Emby、Audiobookshelf等第三方音频服务，新增拼音模糊搜索能力，针对数十万首级别的大曲库做了性能优化，横屏唱机皮肤支持随应用明暗模式自动切换木色与彩胶纹理。

**Tags**: `#promo`, `#coupon`, `#limited-free`

---