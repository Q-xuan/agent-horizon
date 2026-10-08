---
layout: default
title: "Horizon Summary: 2026-10-08 (EN)"
date: 2026-10-08
lang: en
---

> From 212 items, 24 important content pieces were selected

---

**Agent Harness Architecture**
1. [cloudflare/agents released agents@0.27.0](#item-harness-arch-1) ⭐️ 8.3/10
2. [mastra-ai/mastra released @mastra/core@1.75.0](#item-harness-arch-2) ⭐️ 8.3/10
3. [Claude Code 2.1.293 发布](#item-harness-arch-3) ⭐️ 8.3/10
4. [openai/codex released rust-v0.161.0](#item-harness-arch-4) ⭐️ 7.8/10
5. [cline/cline released desktop-v0.0.44](#item-harness-arch-5) ⭐️ 7.8/10
6. [Agent Framework 1.24.0](#item-harness-arch-6) ⭐️ 7.3/10
7. [Cline SDK v0.0.91 发布](#item-harness-arch-7) ⭐️ 6.8/10

**AI Agent Engineer**
1. [HF daily paper: From Evidence to Action: How Tool-Using Agents Fail](#item-agent-engineer-1) ⭐️ 7.5/10
2. [Claude Haiku 5.5](#item-agent-engineer-2) ⭐️ 7.0/10
3. [Claude Haiku 5.5 发布](#item-agent-engineer-3) ⭐️ 7.0/10
4. [UNREAL 统一检索与长上下文](#item-agent-engineer-4) ⭐️ 7.0/10
5. [Liquid AI 开源 d1 边缘决策模型](#item-agent-engineer-5) ⭐️ 6.3/10
6. [Bolmo 字节级技术登 Nature](#item-agent-engineer-6) ⭐️ 6.3/10
7. [SSR：多模态智能体改用选择式推理](#item-agent-engineer-7) ⭐️ 6.0/10
8. [GPT-6 发布，智能界面面向大众](#item-agent-engineer-8) ⭐️ 5.5/10

**AI Daily**
1. [GPT-6 全球上线 ChatGPT](#item-ai-daily-1) ⭐️ 9.8/10
2. [Claude Haiku 5.5 发布并调价](#item-ai-daily-2) ⭐️ 9.8/10
3. [Claude 新增 eval 构建与调优命令](#item-ai-daily-3) ⭐️ 8.8/10
4. [Helping teens learn, plan, and shape the future of AI](#item-ai-daily-4) ⭐️ 7.8/10
5. [Google 开发者知识 API 发布](#item-ai-daily-5) ⭐️ 7.8/10
6. [丽笙推出 ChatGPT 酒店插件](#item-ai-daily-6) ⭐️ 6.8/10

**AI Deals**
1. [Claude: Monthly API credits for Max and Team plans](#item-ai-deals-1) ⭐️ 7.0/10
2. [Claude Agents SDK will no longer use subscription; API credits included in plans](#item-ai-deals-2) ⭐️ 6.0/10
3. [Claude Max and Teams plans now forced to API \(Oct 7th update\)](#item-ai-deals-3) ⭐️ 5.0/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [cloudflare/agents released agents@0.27.0](https://github.com/cloudflare/agents/releases/tag/agents%400.27.0) ⭐️ 8.3/10

Cloudflare Agents v0.27.0 adds four experimental harnesses, a web\_search tool, and a breaking rebuild of the Channels API around conversations and turns.

github · github-actions\[bot\] · Oct 7, 13:25

**Tags**: `#runtime`, `#tools`, `#mcp`, `#sandbox`, `#subagents`

---

<a id="item-harness-arch-2"></a>
### [mastra-ai/mastra released @mastra/core@1.75.0](https://github.com/mastra-ai/mastra/releases/tag/%40mastra/core%401.75.0) ⭐️ 8.3/10

Mastra core 1.75.0 adds span-level observability queries, cross-store token/cost trace aggregation, and self-embedding vector stores for semantic recall.

github · Patrycja-J · Oct 7, 16:17

**Tags**: `#eval`, `#memory`, `#runtime`

---

<a id="item-harness-arch-3"></a>
### [Claude Code 2.1.293 发布](https://code.claude.com/docs/en/changelog#2-1-293) ⭐️ 8.3/10

Claude Code 2.1.293 发布，新增默认 Haiku 模型 \`claude-haiku-5-5\`，1M 上下文，输入 $0.10/Mtok、输出 $0.50/Mtok，超过 100K 的 prompt 按 $0.50/$2.50 计费。工具层加入 \`isDeferred\` 参数，mod 可将工具 schema 从启动即放入 prompt，而非藏在 tool search 后；\`subagentStatusLine\` 增加 \`agentType\`，脚本可区分自定义 subagent 类型。修复上下文压缩后 Claude 把压缩前动作当作已完成而重做或撤回的问题，以及 HTTP MCP 连接在关闭前持续持有全部请求的内存泄漏。

rss · Claude Code Changelog · Oct 7, 18:26

**「设计要点」** Deferred tool registration 让 harness 控制工具 schema 的暴露时机，\`isDeferred=false\` 直接进 prompt；subagent 状态通过 \`agentType\` 暴露类型，配合 \`SendMessage\` 与权限规则修复，影响 subagent 的工具可见性与消息路由。

**「改了什么」** 2.1.293 回滚了 2.1.290 对云会话容器重启后保持休眠的修复，以及 2.1.281 的自动模式拒绝消息调整。claude.ai 技能同步在无会话时从每 10 分钟改为约每 40 分钟，OpenTelemetry \`claude\_code.at\_mention\` 每次读取 prompt 的 agent 与 MCP 资源事件上限各降为 100。

**Tags**: `#runtime`, `#tools`, `#mcp`, `#subagents`, `#memory`

---

<a id="item-harness-arch-4"></a>
### [openai/codex released rust-v0.161.0](https://github.com/openai/codex/releases/tag/rust-v0.161.0) ⭐️ 7.8/10

Codex Rust v0.161.0 adds terminal MCP login, Bedrock multi-agent V2 support, and opt-in Daybreak/Cyber routing controls.

github · github-actions\[bot\] · Oct 7, 15:58

**Tags**: `#runtime`, `#tools`, `#mcp`, `#subagents`, `#planning`

---

<a id="item-harness-arch-5"></a>
### [cline/cline released desktop-v0.0.44](https://github.com/cline/cline/releases/tag/desktop-v0.0.44) ⭐️ 7.8/10

Cline desktop v0.0.44 fixes MCP Windows startup timeouts, adds session auto-reconnect, and resolves API key and custom base URL failures for local and enterprise providers.

github · github-actions\[bot\] · Oct 7, 07:17

**Tags**: `#runtime`, `#tools`, `#mcp`

---

<a id="item-harness-arch-6"></a>
### [Agent Framework 1.24.0](https://github.com/microsoft/agent-framework/releases/tag/dotnet-1.24.0) ⭐️ 7.3/10

microsoft/agent-framework 发布 dotnet-1.24.0，针对 .NET agent harness 的运行时状态、记忆与安全做增量加固。会话状态往返保留显式 null，可禁用近期搜索记忆，惰性请求消息能穿过 agent invocation 保留。LocalCodeAct 能力校验收紧，敏感声明式标识符会被拒绝，Anthropic agent 包转为稳定。

github · dmytrostruk · Oct 7, 13:26

**「设计要点」** 运行时细化会话状态序列化与后台任务元数据同步；工具层校验 LocalCodeAct 能力声明并绑定 MCP 审批头；记忆侧修正 Foundry 空上下文消息、Valkey 零消息限制及近期搜索记忆开关。

**「改了什么」** 新增显式 null 会话状态保留、惰性请求消息传递和后台任务延迟发布；安全面拒绝敏感声明式标识符、越界 MaxBatchSize 及未授权 MCP 调用；Anthropic 包标记稳定。

**Tags**: `#runtime`, `#memory`, `#sandbox`, `#permissions`, `#tools`

---

<a id="item-harness-arch-7"></a>
### [Cline SDK v0.0.91 发布](https://github.com/cline/cline/releases/tag/sdk/sdk/v0.0.91) ⭐️ 6.8/10

Cline SDK v0.0.91 发布，收紧运行时结束原因处理，stdio MCP 初始化超时从 3s 提升到 10s，并限制 Anthropic 回退仅发往官方端点。缺失或未识别的 finish reason 不再视为成功，\`AgentModelFinishReason\` 新增 \`unknown\`；无工具活动时保留部分响应并以隐藏用户消息续跑一次，第二次 unknown 才失败。排队用户消息现在在每次请求边界被消费，包括首次迭代。

github · github-actions\[bot\] · Oct 7, 06:00

**「设计要点」** 运行时把 finish reason 状态机显式建模为 \`unknown\`，配合隐藏消息重试与请求边界消费队列，避免静默截断。MCP 层给 stdio 服务器 10s 初始化预算，显式 \`timeout\` 仍可覆盖。

**「改了什么」** 相对 v0.0.90，SDK 把未识别结束原因从成功改为可重试的中间态，修复 Windows 下 npx/uvx 启动超时导致的 MCP 服务器静默丢弃，并用 \`isOfficialAnthropicEndpoint\` 把服务端 refusal \`fallbacks\` 限制在 \`api.anthropic.com\`，避免自定义端点返回 400。

**Tags**: `#runtime`, `#tools`, `#mcp`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [HF daily paper: From Evidence to Action: How Tool-Using Agents Fail](https://huggingface.co/papers/2610.07753) ⭐️ 7.5/10

A new paper introduces SafeActBench to study how tool-using agents fail to connect evidence to action, finding that failures often occur before execution and in multi-action workflows.

rss · Hugging Face Daily Papers · Oct 7, 00:00

**Tags**: `#eval`, `#harness`, `#coding-agent`, `#orchestration`

---

<a id="item-agent-engineer-2"></a>
### [Claude Haiku 5.5](https://www.anthropic.com/claude-haiku-5-5) ⭐️ 7.0/10

Community discussion of Claude Haiku 5.5, covering pricing tiers, a 100k context cutoff, and cost/latency tradeoffs across thinking levels.

hackernews · sfkgtbor · Oct 7, 18:01 · [Discussion](https://news.ycombinator.com/item?id=49996437)

**Tags**: `#coding-agent`, `#eval`, `#observability`

---

<a id="item-agent-engineer-3"></a>
### [Claude Haiku 5.5 发布](https://simonwillison.net/2026/Oct/7/claude-haiku-5-5/) ⭐️ 7.0/10

Anthropic 发布 Claude Haiku 5.5。每百万 token 输入/输出定价 $0.10/$0.50，与 GPT-6 Luna 持平；超过 100,000 token 后上调 5 倍至 $0.50/$2.50。新 tokenizer 更紧缩，同一长提示较 Haiku 4.5 多耗约 1.25 倍 token。100,000 token 以内，Haiku 5.5 与 Luna 同价且自报基准分更高；超出后 Luna 更划算。模型强制开启推理，默认 medium；Anthropic 同步为 Max 与 Team 订阅者提供与订阅费等额的每月 API 额度，并将 Sonnet 5.5 缓存读取价格减半。

rss · Simon Willison · Oct 7, 20:56

**「为什么重要」** 100,000 token 成为新的成本分水岭，直接影响长上下文 agent 的选型。tokenizer 变更带来隐性涨价，标价对比可能失真。API 额度与订阅费对齐，改变订阅用户的边际调用成本。

**「可关注」** 可关注：若 agent 上下文稳定低于 100,000 token，Haiku 5.5 具备成本竞争力；一旦接近或超过该阈值，需按 $0.50/$2.50 重新核算，并与 Luna 的 272,000 token 阈值对比。建议用真实提示实测 tokenizer 膨胀率，再决定是否切换。

**Tags**: `#coding-agent`, `#eval`, `#orchestration`

---

<a id="item-agent-engineer-4"></a>
### [UNREAL 统一检索与长上下文](https://huggingface.co/papers/2610.08463) ⭐️ 7.0/10

UNREAL 提出模型原生的证据选择框架，用同一个冻结 LLM 同时处理语料检索与长上下文推理。它从冻结模型的内部表示中编码 chunk 并派生检索 query，新增可训练参数少于 500K，骨干网络不变。在 3B token、21M chunk 的 Wikipedia 索引上，四种 dense 与 hybrid UNREAL 骨干均超过 SOTA retriever-reranker 系统。

rss · Hugging Face Daily Papers · Oct 7, 00:00

**「为什么重要」** 对做 agent memory / retrieval 架构的工程师，这提供了一条不替换 backbone、不引入独立检索器的替代路径。已发生的变化是该方法在 Wikipedia 基准上超过现有 retriever-reranker 组合；尚未证实的是其在生产环境多跳、动态语料下的稳定性。

**「可关注」** 可关注：UNREAL 把检索与长上下文的证据选择收敛到模型内部表示，新增参数少于 500K，适合评估冻结 LLM 上的统一记忆层，而非直接替换现有 RAG 栈。

**Tags**: `#memory`, `#eval`, `#retrieval`, `#long-context`

---

<a id="item-agent-engineer-5"></a>
### [Liquid AI 开源 d1 边缘决策模型](https://huggingface.co/blog/LiquidAI/open-d1) ⭐️ 6.3/10

Liquid AI 开源 d1-3B 与 d1-omni-600M 两款多模态决策模型，面向边缘设备。d1-3B 在 Decision Index 0.2.1 得 48.57，为 10B 以下最高分，超过 Decider 35B-A3B 的 47.11。模型不生成 token，单次前向传播直接输出决策。d1-3B 基于 LFM2.5-VL-3B，支持文本与图像；d1-omni-600M 基于 LFM2.5-Encoder-350M，支持文本+图像或文本+音频，仍处早期研究阶段。在 NVIDIA Jetson AGX Thor 上单问延迟 16 ms，Jetson Orin Nano 上 50 ms；RTX 4090 上低于 10 ms。

rss · Hugging Face Blog · Oct 7, 16:54

**「为什么重要」** d1 不做 token 生成，单次前向传播直接输出决策，边缘延迟压到 50 ms 以内。对做 coding agent / harness 的人，这是本地分类、路由或工具选择的前置层形态，而非通用对话模型。

**「可关注」** 可关注：d1-3B 在 3B 参数量下达到 48.57 的 Decision Index 分数，边缘延迟稳定在 50 ms 以内；加载需 transformers&gt;=5.14 并设 trust\_remote\_code=True。d1-omni-600M 仍处早期研究阶段，未发布速度数据，且视觉与音频决策基准缺公开评测。

**Tags**: `#edge`, `#multimodal`, `#benchmark`, `#model-release`

---

<a id="item-agent-engineer-6"></a>
### [Bolmo 字节级技术登 Nature](https://allenai.org/blog/bolmo-nature) ⭐️ 6.3/10

10 月 7 日，Allen AI 宣布 Bolmo 字节级语言模型技术正式发表于 Nature。新检查点显示，该方法已从 Olmo 泛化到其他模型家族。Bolmo 是 Ai2 的完全开源字节级语言模型。

rss · Allen AI · Oct 7, 08:00

**「为什么重要」** 字节级模型直接处理原始字节，不依赖预定义词表。该技术进入 Nature 并泛化到 Olmo 之外，为开源社区提供了 tokenization 之外的可行路径。

**「可关注」** Bolmo 新检查点已泛化至 Olmo 以外的模型家族，做输入表示实验时可对比字节级与传统 tokenization 方案。

**Tags**: `#llm`, `#tokenization`, `#research`

---

<a id="item-agent-engineer-7"></a>
### [SSR：多模态智能体改用选择式推理](https://huggingface.co/papers/2610.01892) ⭐️ 6.0/10

Hugging Face 每日论文上线一篇多模态智能体推理框架论文，提出 Selection-based Structured Reasoning（SSR）。SSR 将动作生成前的自由形式推理改为选择：把反复出现的高层推理预先写成可复用的自然语言候选，每轮根据当前上下文计算候选似然并选一个，无需辅助任务头。论文针对小模型容量有限、开放生成长推理对动作指导弱且推理成本高的问题，指出预指定推理轨迹支持并行评分，通过 teacher-forced prefilling 计算 token 似然。论文发布于 2026-10-07，当前获得 14 个 upvotes。

rss · Hugging Face Daily Papers · Oct 7, 00:00

**「为什么重要」** 多模态 agent 通常在每步动作前生成自由形式推理，小模型上这段推理冗长且对动作帮助有限，却带来可观推理开销。SSR 把推理压缩为受控选择，直接对着成本与指导性两个痛点；能否在实际任务中降低时延并提升动作质量，仍需完整论文和实验验证。

**「可关注」** 可关注：若多模态 agent 的推理步骤可被枚举为有限候选，SSR 的并行评分与免任务头设计提供了一种降低推理开销的替代路径；采用前需评估候选集对实际任务推理分布的覆盖度。

**Tags**: `#agents`, `#reasoning`, `#multimodal`, `#efficiency`

---

<a id="item-agent-engineer-8"></a>
### [GPT-6 发布，智能界面面向大众](https://openai.com/index/gpt-6-for-everyone/) ⭐️ 5.5/10

OpenAI 发布 GPT-6，主打面向大众的智能界面。官方系统卡显示，相比 GPT-5.6，GPT-6 Sol（10 月）在标准自残评测上出现统计显著回退，GPT-6 Luna（10 月）在自残、血腥和性内容上均出现统计显著回退。本次发布重点在消费端体验，未提供面向 coding agent、harness 或工具链的明确破坏性变更。

hackernews · joshuawright11 · Oct 7, 18:00 · [Discussion](https://news.ycombinator.com/item?id=49996425)

**「为什么重要」** 系统卡明确记录安全评测回退，为关注模型安全与评估的工程师提供了具体信号；但本次发布未触及 agent 工程链路，消费端变化与工具端影响需分开看待。

**「可关注」** 可关注：GPT-6 的安全评测回退已被官方系统卡记录，若后续将其用于 agent 或工具链，需重新验证相关安全边界；当前材料未给出面向工程集成的技术细节。

**「评论」** HN 用户对 5.6 与 6 的对比反应不一，有用户批评新界面过于简化，也有用户借系统卡链接指出安全评测回退；另有用户担忧工作与聊天合并会波及 Codex 等工具。讨论重心在消费体验，未形成对 agent 工程影响的共识。

**Tags**: `#eval`, `#coding-agent`, `#ui`

---

## AI Daily

<a id="item-ai-daily-1"></a>
### [GPT-6 全球上线 ChatGPT](https://openai.com/index/gpt-6-for-everyone) ⭐️ 9.8/10

OpenAI 宣布 GPT-6 正在全球范围内向 ChatGPT 推送，并引入 Intelligent UI。官方称新界面将提供更快的响应，支持可视化与交互式体验，用户可直接探索和使用。目前公告信息有限，未披露具体模型参数、基准测试或分阶段推送细节。

rss · OpenAI Blog · Oct 7, 00:00

**「为什么重要」** 作为 OpenAI 的重大模型发布，GPT-6 的全球上线将直接影响所有 ChatGPT 用户，并可能重塑人机交互方式。

**「可关注」** 可关注：Intelligent UI 把视觉与交互能力直接嵌入模型响应，用户可在 ChatGPT 内直接探索和使用这些内容。

**Tags**: `#model`, `#lab`, `#product`, `#industry`

---

<a id="item-ai-daily-2"></a>
### [Claude Haiku 5.5 发布并调价](https://www.anthropic.com/claude-haiku-5-5) ⭐️ 9.8/10

Anthropic 发布 Claude Haiku 5.5，定位高并发、成本敏感任务。官方称其为迄今最便宜、最快的小模型，平均运行成本较 Haiku 4.5 低约 75%；10 万 token 以内请求降价 90%，超出部分降价 50%。同步将 Sonnet 5.5 缓存读取价格减半至 $0.10 / 百万 token，多数智能体任务成本降低约 20%。模型已上线 AWS、Google Cloud、Azure 及 Claude Platform，并首次配备可调节 effort 设置。

rss · Claude Blog · Oct 7, 00:00

**「为什么重要」** Haiku 5.5 在 OSWorld 2.1 取得 72.4%，较 Haiku 4.5 的 15.7% 大幅提升；Terminal-Bench 4.0 从 0.0% 升至 39.2%。价格下调叠加 Max/Team 月度 API 额度，直接压低智能体与子代理的调用成本。

**「可关注」** 可关注：Haiku 5.5 适合压缩、摘要、子代理等窄域任务，复杂智能体编码仍应选 Sonnet 5.5 或 Opus 5.5；Python 与 TypeScript SDK 已新增 computer use 与 browser use beta 支持。

**Tags**: `#model`, `#lab`, `#product`, `#industry`

---

<a id="item-ai-daily-3"></a>
### [Claude 新增 eval 构建与调优命令](https://claude.dev/blog/automating-eval-design-and-hillclimbing/) ⭐️ 8.8/10

Claude 官方博客为 claude-api skill 新增 /claude-api build-eval 与 /claude-api hillclimb 命令，把评估构建与爬山调优流程内置到 Claude Code。build-eval 通过访谈引导用户在代码库内生成评估，优先采样生产流量，并挑选最简可用评分器；hillclimb 每次只做一个补丁级改动，随机拆分训练/测试集，若训练集提升而测试集持平即回滚以防过拟合。官方示例中，44 张客服工单基准从 Opus 4.8 默认高努力度的 74.4% 准确率、每单 4.6 美分，经提示词审计与模型降档至 Sonnet 5 低努力度后达到 88.9% 准确率、每单约 1 美分。若最终增益在评估噪声内，hillclimb 会建议不要合并。

rss · Claude Blog · Oct 7, 00:00

**「为什么重要」** 这两个命令将评估设计与爬山调优从经验原则落为可执行工作流，对做 coding agent 与 harness 的工程师有直接参考价值。它同时给出了成本-性能权衡的具体路径：先审提示词，再降模型档位，并用留出集兜底。

**「可关注」** 可关注：hillclimb 在每轮改动前会检查评估噪声是否小于最小可行动增益，不足时建议增加重复次数或案例数，而不是盲目迭代。

**Tags**: `#eval`, `#product`, `#lab`, `#model`

---

<a id="item-ai-daily-4"></a>
### [Helping teens learn, plan, and shape the future of AI](https://openai.com/index/teens-learn-and-plan) ⭐️ 7.8/10

OpenAI announced College Planner and new learning tools for ChatGPT Teens.

rss · OpenAI Blog · Oct 7, 12:00

**Tags**: `#product`, `#lab`, `#industry`

---

<a id="item-ai-daily-5"></a>
### [Google 开发者知识 API 发布](https://developers.googleblog.com/supercharge-your-development-with-the-google-developer-knowledge-api-ecosystem/) ⭐️ 7.8/10

Google 发布 Developer Knowledge API 生态，为 AI agent 与开发工具提供官方结构化文档源。接口覆盖 Google Cloud、Firebase、Android，返回 Markdown 格式的最新文档，替代脆弱的网页抓取。核心能力包括语义与关键词搜索、智能文档分块、grounded Q&amp;A。gcloud CLI 已内置该接口，提供 answer-query、documents search-chunks、documents describe 命令。官方同时提供 agent skill、多语言客户端库与 API Explorer。

rss · Google Developers AI · Oct 7, 00:00

**「为什么重要」** AI agent 与开发工具长期依赖网页抓取或受限于训练数据截止。该 API 提供官方、可编程、频繁索引的文档源，直接改善信息获取的准确性与新鲜度。

**「可关注」** 可关注：gcloud developer-knowledge answer-query 支持直接读取错误日志文件并返回 grounded 答案，且 CLI 已预装在 Cloud Shell，跨 Linux、macOS、Windows 无需额外配置。

**Tags**: `#product`, `#lab`, `#industry`

---

<a id="item-ai-daily-6"></a>
### [丽笙推出 ChatGPT 酒店插件](https://openai.com/index/radisson) ⭐️ 6.8/10

丽笙酒店集团与 Accenture 合作，基于 OpenAI 技术开发了一款 ChatGPT 插件。旅客可在规划行程时查找、比较并预订酒店。该消息来自 OpenAI 官方博客，属于企业产品集成，并非模型或政策更新。

rss · OpenAI Blog · Oct 7, 07:00

**「为什么重要」** 该合作展示了传统酒店集团通过 Accenture 集成 OpenAI 技术，将酒店查找、比较与预订流程嵌入 ChatGPT 的路径。对关注企业级 AI 应用的从业者，提供了一个可参考的集成样本。

**「可关注」** 可关注：丽笙酒店集团与 Accenture 合作开发 ChatGPT 插件，将酒店查找、比较与预订流程嵌入对话界面。这种由外部合作方主导的集成方式，为传统企业接入 OpenAI 技术提供了一种实施路径。

**Tags**: `#product`, `#industry`, `#lab`

---

## AI Deals

<a id="item-ai-deals-1"></a>
### [Claude: Monthly API credits for Max and Team plans](https://support.claude.com/en/articles/17154008-monthly-api-credits-for-max-and-team-plans) ⭐️ 7.0/10

Claude 官方页面宣布 Max 和 Team 订阅用户可获得每月 API credits。

rss · HN Free API / Credits · Oct 7, 18:52

**Tags**: `#credits`, `#api`, `#promo`

---

<a id="item-ai-deals-2"></a>
### [Claude Agents SDK will no longer use subscription; API credits included in plans](https://news.ycombinator.com/item?id=49997654) ⭐️ 6.0/10

Claude Max and Team plans now include monthly API credits covering the Agent SDK, Claude API, and Managed Agents, claimable into a Claude Console organization.

rss · HN Free API / Credits · Oct 7, 19:28

**Tags**: `#credits`, `#api`, `#promo`

---

<a id="item-ai-deals-3"></a>
### [Claude Max and Teams plans now forced to API \(Oct 7th update\)](https://news.ycombinator.com/item?id=49999508) ⭐️ 5.0/10

Claude Max与Team套餐用户现可在Console组织中领取月度API credits，用于Agent SDK、Claude API及Managed Agents。

rss · HN Free API / Credits · Oct 7, 22:15

**Tags**: `#credits`, `#api`, `#promo`

---