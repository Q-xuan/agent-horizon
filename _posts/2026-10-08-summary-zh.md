---
layout: default
title: "Horizon Summary: 2026-10-08 (ZH)"
date: 2026-10-08
lang: zh
---

> 从 212 条内容中筛选出 24 条重要资讯。

---

**Harness 架构**
1. [cloudflare/agents released agents@0.27.0](#item-harness-arch-1) ⭐️ 8.3/10
2. [mastra-ai/mastra released @mastra/core@1.75.0](#item-harness-arch-2) ⭐️ 8.3/10
3. [Claude Code 2.1.293 发布](#item-harness-arch-3) ⭐️ 8.3/10
4. [openai/codex released rust-v0.161.0](#item-harness-arch-4) ⭐️ 7.8/10
5. [cline/cline released desktop-v0.0.44](#item-harness-arch-5) ⭐️ 7.8/10
6. [Agent Framework 1.24.0](#item-harness-arch-6) ⭐️ 7.3/10
7. [Cline SDK v0.0.91 发布](#item-harness-arch-7) ⭐️ 6.8/10

**Agent 工程师日报**
1. [HF daily paper: From Evidence to Action: How Tool-Using Agents Fail](#item-agent-engineer-1) ⭐️ 7.5/10
2. [Claude Haiku 5.5](#item-agent-engineer-2) ⭐️ 7.0/10
3. [Claude Haiku 5.5 发布](#item-agent-engineer-3) ⭐️ 7.0/10
4. [UNREAL：单模型统一检索与长上下文](#item-agent-engineer-4) ⭐️ 7.0/10
5. [Liquid AI 开源 d1 边缘决策模型](#item-agent-engineer-5) ⭐️ 6.3/10
6. [Bolmo 字节级语言模型登 Nature](#item-agent-engineer-6) ⭐️ 6.3/10
7. [SSR：多模态智能体推理改为候选选择](#item-agent-engineer-7) ⭐️ 6.0/10
8. [GPT-6 发布，推出全民智能界面](#item-agent-engineer-8) ⭐️ 5.5/10

**AI 日报**
1. [GPT-6 全球上线 ChatGPT](#item-ai-daily-1) ⭐️ 9.8/10
2. [Claude Haiku 5.5 发布](#item-ai-daily-2) ⭐️ 9.8/10
3. [Claude API 新增 eval 命令](#item-ai-daily-3) ⭐️ 8.8/10
4. [Helping teens learn, plan, and shape the future of AI](#item-ai-daily-4) ⭐️ 7.8/10
5. [Google 推出开发者知识 API](#item-ai-daily-5) ⭐️ 7.8/10
6. [Radisson 推出 ChatGPT 插件](#item-ai-daily-6) ⭐️ 6.8/10

**AI 羊毛**
1. [Claude: Monthly API credits for Max and Team plans](#item-ai-deals-1) ⭐️ 7.0/10
2. [Claude Agents SDK will no longer use subscription; API credits included in plans](#item-ai-deals-2) ⭐️ 6.0/10
3. [Claude Max and Teams plans now forced to API \(Oct 7th update\)](#item-ai-deals-3) ⭐️ 5.0/10

---

## Harness 架构

<a id="item-harness-arch-1"></a>
### [cloudflare/agents released agents@0.27.0](https://github.com/cloudflare/agents/releases/tag/agents%400.27.0) ⭐️ 8.3/10

Cloudflare Agents v0.27.0 adds four experimental harnesses, a web\_search tool, and a breaking rebuild of the Channels API around conversations and turns.

github · github-actions\[bot\] · 10月7日 13:25

**标签**: `#runtime`, `#tools`, `#mcp`, `#sandbox`, `#subagents`

---

<a id="item-harness-arch-2"></a>
### [mastra-ai/mastra released @mastra/core@1.75.0](https://github.com/mastra-ai/mastra/releases/tag/%40mastra/core%401.75.0) ⭐️ 8.3/10

Mastra core 1.75.0 adds span-level observability queries, cross-store token/cost trace aggregation, and self-embedding vector stores for semantic recall.

github · Patrycja-J · 10月7日 16:17

**标签**: `#eval`, `#memory`, `#runtime`

---

<a id="item-harness-arch-3"></a>
### [Claude Code 2.1.293 发布](https://code.claude.com/docs/en/changelog#2-1-293) ⭐️ 8.3/10

Claude Code 2.1.293 发布，新增默认 Haiku 模型 \`claude-haiku-5-5\`，支持 1M 上下文，价格为 $0.10/$0.50 per Mtok，超过 100K 的 prompt 为 $0.50/$2.50。工具层新增 \`agentType\` 到 \`subagentStatusLine\`，脚本可区分自定义 subagent 类型；\`$.tool.register\` 新增 \`isDeferred\`，设为 \`false\` 时工具 schema 从初始 prompt 可见，而非藏在工具搜索后。运行时修复上下文压缩后 Claude 重做或撤回已完成工作的问题，以及 HTTP MCP 连接持有所有请求导致的内存泄漏。

rss · Claude Code Changelog · 10月7日 18:26

**「设计要点」** 工具注册、subagent 状态与 MCP 连接生命周期通过新字段和修复暴露给 harness；后台化会话的消息队列和权限工具缺失场景也得到修正。

**「改了什么」** 相对上一版，mod 可控制工具 schema 是否延迟注册，subagent 状态行可识别类型；上下文压缩、MCP 内存泄漏、后台消息丢失和 \`/model\` effort 回绕等问题被修复。

**标签**: `#runtime`, `#tools`, `#mcp`, `#subagents`, `#memory`

---

<a id="item-harness-arch-4"></a>
### [openai/codex released rust-v0.161.0](https://github.com/openai/codex/releases/tag/rust-v0.161.0) ⭐️ 7.8/10

Codex Rust v0.161.0 adds terminal MCP login, Bedrock multi-agent V2 support, and opt-in Daybreak/Cyber routing controls.

github · github-actions\[bot\] · 10月7日 15:58

**标签**: `#runtime`, `#tools`, `#mcp`, `#subagents`, `#planning`

---

<a id="item-harness-arch-5"></a>
### [cline/cline released desktop-v0.0.44](https://github.com/cline/cline/releases/tag/desktop-v0.0.44) ⭐️ 7.8/10

Cline desktop v0.0.44 fixes MCP Windows startup timeouts, adds session auto-reconnect, and resolves API key and custom base URL failures for local and enterprise providers.

github · github-actions\[bot\] · 10月7日 07:17

**标签**: `#runtime`, `#tools`, `#mcp`

---

<a id="item-harness-arch-6"></a>
### [Agent Framework 1.24.0](https://github.com/microsoft/agent-framework/releases/tag/dotnet-1.24.0) ⭐️ 7.3/10

microsoft/agent-framework 发布 dotnet-1.24.0，聚焦 .NET agent harness 的运行时状态、记忆与安全加固。核心变更包括跨 roundtrip 保留显式 null 会话状态、遵循禁用的近期搜索记忆、加固 LocalCodeAct 能力校验，以及拒绝敏感声明式标识符。Anthropic agent 包转入稳定版，同时修复 MCP 审批重放 ID、A2A 运行错误保存、HTTP 头分隔符校验等问题。

github · dmytrostruk · 10月7日 13:26

**「设计要点」** 会话状态序列化保留显式 null，避免 roundtrip 后语义丢失。记忆层支持关闭近期搜索，工具与权限层收紧 LocalCodeAct 能力校验和声明式 MCP 调用的受保护值拒绝。

**「改了什么」** 相对旧版，新增对显式 null 会话状态的 roundtrip 保留、禁用近期搜索记忆的遵循、LocalCodeAct 能力校验加固，以及 Anthropic agent 包的稳定化。安全侧加入敏感声明式标识符拒绝、HTTP 头分隔符校验和 MCP 审批头绑定。

**标签**: `#runtime`, `#memory`, `#sandbox`, `#permissions`, `#tools`

---

<a id="item-harness-arch-7"></a>
### [Cline SDK v0.0.91 发布](https://github.com/cline/cline/releases/tag/sdk/sdk/v0.0.91) ⭐️ 6.8/10

Cline SDK v0.0.91 收紧运行时结束原因处理，缺失或未识别的 finish reason 不再视为成功完成。\`AgentModelFinishReason\` 新增 \`unknown\`，AI SDK adapter 将统一 \`other\` 和缺失原因映射到它而非 \`stop\`；无工具活动时保留部分响应并以隐藏 user message 续跑一次，第二次 unknown 直接失败。Stdio MCP 默认 initialize 预算从 3s 提到 10s，修复 Windows 下 npx/uvx 启动被静默丢弃的问题。Anthropic provider 的 fallbacks 选项仅发送到 \`api.anthropic.com\`，自定义端点不再收到导致 400 的字段。

github · github-actions\[bot\] · 10月7日 06:00

**「设计要点」** 运行时把结束原因当作显式状态机管理，未知原因不再默认落到 \`stop\`；MCP 初始化超时和 provider 端点门控都在工具与模型接入层做了硬限制。

**「改了什么」** 相对 v0.0.90，SDK 把 finish reason 未知态纳入失败路径，MCP stdio 初始化超时从 3s 提高到 10s，Anthropic fallbacks 增加官方端点判断，并新增 \`apiKeyOptional\` provider 事实与 Langfuse BYOK 追踪开关。

**标签**: `#runtime`, `#tools`, `#mcp`

---

## Agent 工程师日报

<a id="item-agent-engineer-1"></a>
### [HF daily paper: From Evidence to Action: How Tool-Using Agents Fail](https://huggingface.co/papers/2610.07753) ⭐️ 7.5/10

A new paper introduces SafeActBench to study how tool-using agents fail to connect evidence to action, finding that failures often occur before execution and in multi-action workflows.

rss · Hugging Face Daily Papers · 10月7日 00:00

**标签**: `#eval`, `#harness`, `#coding-agent`, `#orchestration`

---

<a id="item-agent-engineer-2"></a>
### [Claude Haiku 5.5](https://www.anthropic.com/claude-haiku-5-5) ⭐️ 7.0/10

Community discussion of Claude Haiku 5.5, covering pricing tiers, a 100k context cutoff, and cost/latency tradeoffs across thinking levels.

hackernews · sfkgtbor · 10月7日 18:01 · [社区讨论](https://news.ycombinator.com/item?id=49996437)

**标签**: `#coding-agent`, `#eval`, `#observability`

---

<a id="item-agent-engineer-3"></a>
### [Claude Haiku 5.5 发布](https://simonwillison.net/2026/Oct/7/claude-haiku-5-5/) ⭐️ 7.0/10

Anthropic 发布 Claude Haiku 5.5，每百万 token 输入/输出定价 $0.10/$0.50，10 万 token 以内与 GPT-6 Luna 同价；超过 10 万 token 后涨至 $0.50/$2.50，Luna 则到 27.2 万 token 后才提价至 $0.20/$0.75。Haiku 5.5 换用新 tokenizer，同样长 prompt 比 Haiku 4.5 多耗约 1.25 倍 token，存在隐性涨价，且不支持关闭推理，默认 medium 档。Anthropic 同步将 Sonnet 5.5 缓存读取价格减半，并向 Max 5x、Max 20x、Team 订阅者发放每月 $100、$200、最高 $500 的 API 额度，当月有效、不结转。

rss · Simon Willison · 10月7日 20:56

**「为什么重要」** 10 万 token 成为成本分水岭。以内 Haiku 5.5 与 Luna 同价且基准更高，以外 Luna 更划算。tokenizer 变更直接影响按 token 计费的预算模型。

**「可关注」** 可关注：若 agent 上下文稳定低于 10 万 token，Haiku 5.5 可作低成本档位；超出后需对比 Luna，并用 Claude Token Counter 重新校准 token 预算。

**标签**: `#coding-agent`, `#eval`, `#orchestration`

---

<a id="item-agent-engineer-4"></a>
### [UNREAL：单模型统一检索与长上下文](https://huggingface.co/papers/2610.08463) ⭐️ 7.0/10

UNREAL 提出模型原生的证据选择框架，在冻结 LLM 的内部表示上直接编码文本块并派生检索查询，新增可训练参数少于 500K，骨干网络保持不变。在 3B token、21M 文本块的 Wikipedia 索引上，四种 dense 与 hybrid UNREAL 骨干均超过 SOTA retriever-reranker 系统；最佳模型将 recall 从 49.1% 的基线进一步提升，但原文此处数据截断，完整数值未给出。该论文发表于 2026-10-07，属于研究贡献，尚未成为生产环境的即时变更。

rss · Hugging Face Daily Papers · 10月7日 00:00

**「为什么重要」** 对 coding agent 与 harness 开发者而言，这条路径不替换骨干模型，仅用极少参数统一检索与长上下文证据选择，可能降低记忆模块的独立维护成本。但论文未提供生产环境验证，实际收益仍待社区复现。

**「可关注」** 可关注：UNREAL 在冻结 LLM 上加装少于 500K 参数即超越 retriever-reranker 管线，若后续开源实现稳定，或可减少记忆与检索模块的分离维护。

**标签**: `#memory`, `#eval`, `#retrieval`, `#long-context`

---

<a id="item-agent-engineer-5"></a>
### [Liquid AI 开源 d1 边缘决策模型](https://huggingface.co/blog/LiquidAI/open-d1) ⭐️ 6.3/10

Liquid AI 开源 d1-3B 与 d1-omni-600M 两个多模态决策模型，面向边缘设备。官方称 d1-3B 在 Decision Index 0.2.1 得 48.57，超过所有 4B、9B 模型及 Decider 35B-A3B（47.11）。模型不做 token 生成，单次前向传播直接输出决策；d1-3B 支持文本和图像，d1-omni-600M 支持文本+图像或文本+音频，后者仍为早期研究版本。边缘延迟：Jetson AGX Thor 16 ms，Jetson AGX Orin 64 GB 26 ms，Jetson Orin Nano 50 ms；三个问题耗时仅为一个问题的 1.3 倍。

rss · Hugging Face Blog · 10月7日 16:54

**「为什么重要」** 对 coding agent / harness 工程师，这类单次前向、毫秒级延迟的决策模型适合嵌入 agent 循环做路由、分类、结构化判断，替代逐 token 生成的等待。但材料仅覆盖边缘决策场景，未验证通用 agent 任务或工具调用表现。

**「可关注」** 可关注：d1-3B 在 3B 参数量下给出 16–50 ms 边缘延迟，且三个问题批量推理仅 1.3 倍单问题耗时，适合高频结构化决策；但需 transformers&gt;=5.14，且依赖 trust\_remote\_code=True 加载。

**标签**: `#edge`, `#multimodal`, `#benchmark`, `#model-release`

---

<a id="item-agent-engineer-6"></a>
### [Bolmo 字节级语言模型登 Nature](https://allenai.org/blog/bolmo-nature) ⭐️ 6.3/10

Allen AI 宣布 Bolmo 字节级语言模型技术正式发表于 Nature。官方称新开源检查点显示该方法已从 Olmo 泛化到其他模型家族。当前公告仅为简短预告，未包含技术细节、基准数据或对 agent 工程工作流的直接影响。

rss · Allen AI · 10月7日 08:00

**「为什么重要」** 字节级语言模型已获 Nature 收录并出现跨家族泛化证据，但公告未提供基准或工程影响数据，实际价值仍待验证。

**「可关注」** 可关注：官方仅发布简短预告，技术细节、基准测试及对 agent 工具链的影响仍待论文全文与开源检查点披露。

**标签**: `#llm`, `#tokenization`, `#research`

---

<a id="item-agent-engineer-7"></a>
### [SSR：多模态智能体推理改为候选选择](https://huggingface.co/papers/2610.01892) ⭐️ 6.0/10

多模态智能体通常在动作前生成自由形式的推理。小模型容量有限，长推理对动作生成帮助有限，却带来高推理成本。SSR 把推理重构为从预置、可复用的自然语言候选中选择，每轮根据当前上下文按概率挑选候选，无需辅助任务头。预置推理轨迹支持并行评分，通过 teacher-forced prefilling 计算 token 似然。该论文 2026 年 10 月 7 日收录于 Hugging Face Daily Papers，获 14 赞。

rss · Hugging Face Daily Papers · 10月7日 00:00

**「为什么重要」** 小模型跑多模态智能体时，推理长度和成本是实际瓶颈。SSR 用选择代替生成以降低推理开销，但论文尚未给出完整实验对比，效果待验证。

**「可关注」** 可关注：SSR 将推理候选预置并复用，配合 teacher-forced prefilling 做并行评分，为小模型多模态智能体的推理降本提供了明确的技术路径。

**标签**: `#agents`, `#reasoning`, `#multimodal`, `#efficiency`

---

<a id="item-agent-engineer-8"></a>
### [GPT-6 发布，推出全民智能界面](https://openai.com/index/gpt-6-for-everyone/) ⭐️ 5.5/10

OpenAI 发布 GPT-6，主推全民智能界面。系统卡披露，GPT-6 Sol（10 月）在标准自残评估上出现统计显著回退；GPT-6 Luna（10 月）在自残、血腥、性内容评估上均出现统计显著回退，extremism vision 评估也有回退。此次发布侧重消费级体验，未提及面向 coding agent、harness 或工具链的破坏性变更。

hackernews · joshuawright11 · 10月7日 18:00 · [社区讨论](https://news.ycombinator.com/item?id=49996425)

**「为什么重要」** 系统卡披露的安全回退是具体、可验证的模型行为变化，为评估该模型能否进入生产环境提供了直接依据；不过官方发布重心在消费端，未给出 agent 相关的技术变更。

**「可关注」** 可关注：GPT-6 Sol 与 Luna 在系统卡中披露的安全评估回退（自残、血腥、性内容），以及官方将本次发布定位为消费级界面而非 agent 工具链更新，在集成前需以系统卡数据为准。

**「评论」** HN 讨论聚焦界面与交互：有用户批评 GPT-6 界面多余留白和清单显得居高临下，也有用户认为短句来回比长文更有效，并提到重复输出同一和弦图的问题；另有评论担心工作场景与聊天合并会影响 Codex，但属社区观点。

**标签**: `#eval`, `#coding-agent`, `#ui`

---

## AI 日报

<a id="item-ai-daily-1"></a>
### [GPT-6 全球上线 ChatGPT](https://openai.com/index/gpt-6-for-everyone) ⭐️ 9.8/10

OpenAI 宣布 GPT-6 在 ChatGPT 中全球上线，同步推出 Intelligent UI。官方称新界面响应更快，支持视觉内容与交互体验，用户可直接探索使用。目前披露信息有限，具体能力与限制尚未说明。

rss · OpenAI Blog · 10月7日 00:00

**「为什么重要」** OpenAI 官方全球发布 GPT-6，属于头部实验室的重要模型更新。对关注模型能力与交互界面变化的开发者，这是今天的核心动态。

**「可关注」** 可关注：GPT-6 在 ChatGPT 中引入 Intelligent UI，官方称响应更快，并支持视觉与交互内容直接使用。

**标签**: `#model`, `#lab`, `#product`, `#industry`

---

<a id="item-ai-daily-2"></a>
### [Claude Haiku 5.5 发布](https://www.anthropic.com/claude-haiku-5-5) ⭐️ 9.8/10

Anthropic 发布 Claude Haiku 5.5，面向高并发、成本敏感任务。官方称平均运行成本较 Haiku 4.5 降低约 75%，10 万 token 以内请求降价 90%，超过 10 万 token 降价 50%。Sonnet 5.5 缓存读取同步减半至每百万 token 0.10 美元，多数 agentic 任务成本下降约 20%。该模型为首个支持可调节 effort 的 Haiku 级模型，已在 AWS、Google Cloud、Azure 及 Claude Platform 上线；Max 与 Team 订阅者本周起将获得每月 API 额度。

rss · Claude Blog · 10月7日 00:00

**「为什么重要」** Haiku 5.5 在 Terminal-Bench 4.0 取得 39.2%，Haiku 4.5 为 0.0%，Sonnet 5.5 为 70.6%。官方建议将其用于压缩、摘要、子代理等窄范围任务，复杂 agentic 编码仍推荐 Sonnet 5.5 或 Opus 5.5。

**「可关注」** 可关注：Haiku 5.5 采用与 Sonnet 5.5、Opus 5.5 相近的新 tokenizer，单任务 token 消耗略增；10 万 token 以内输入价 0.10 美元/百万、输出 0.50 美元/百万，此前 90% 的 Haiku 请求在此区间，适合替代压缩、摘要、子代理等高频调用。

**标签**: `#model`, `#lab`, `#product`, `#industry`

---

<a id="item-ai-daily-3"></a>
### [Claude API 新增 eval 命令](https://claude.dev/blog/automating-eval-design-and-hillclimbing/) ⭐️ 8.8/10

Claude 官方博客为 claude-api skill 新增 \`/claude-api build-eval\` 与 \`/claude-api hillclimb\` 两条命令，用于在代码库内构建评估并逐轮改进应用。build-eval 引导用户确定输入与最简评分器，运行基线并输出带置信区间的分数；hillclimb 随机切分训练/测试集，每轮只提交一个补丁，若训练集提升而测试集持平即回滚以防过拟合。官方示例中，内部客服基准从 Opus 4.8 默认高努力档的 74.4% 决策准确率、每工单 4.6 美分 token 成本出发，经提示词审计与模型降档，Sonnet 5 低努力档达到 88.9% 准确率、每工单约 1 美分；后续提示词加入路由规则与退款上限交叉引用，结果在原文截断处未完整给出。

rss · Claude Blog · 10月7日 00:00

**「为什么重要」** 这两条命令把评估设计与防过拟合流程固化为 skill 内的引导式工作流，降低搭建可靠评估的门槛。对做 coding agent / harness 的读者而言，其训练/测试切分、噪声检查与补丁回滚机制提供了可复用的参考。

**「可关注」** 可关注：hillclimb 在每轮改动前检查评估噪声是否小于最小可感知提升，若训练集涨而测试集持平即回滚补丁，这套防过拟合检查可直接迁移到自建 harness 的调优流程中。

**标签**: `#eval`, `#product`, `#lab`, `#model`

---

<a id="item-ai-daily-4"></a>
### [Helping teens learn, plan, and shape the future of AI](https://openai.com/index/teens-learn-and-plan) ⭐️ 7.8/10

OpenAI announced College Planner and new learning tools for ChatGPT Teens.

rss · OpenAI Blog · 10月7日 12:00

**标签**: `#product`, `#lab`, `#industry`

---

<a id="item-ai-daily-5"></a>
### [Google 推出开发者知识 API](https://developers.googleblog.com/supercharge-your-development-with-the-google-developer-knowledge-api-ecosystem/) ⭐️ 7.8/10

Google 推出 Developer Knowledge API 生态，为 AI agent 与开发工具提供官方结构化文档接口。覆盖 Google Cloud、Firebase、Android 等产品，输出 Markdown 文档。提供 gcloud CLI、agent skill、API Explorer 与多语言客户端库。支持语义与关键词搜索、文档分块、grounded Q&amp;A。API 频繁索引，保证文档新鲜，替代网页抓取。

rss · Google Developers AI · 10月7日 00:00

**「为什么重要」** AI agent 常受训练数据截止与网页抓取失败困扰。该 API 提供官方实时文档源，降低幻觉风险，提升检索 token 效率。

**「可关注」** gcloud CLI 内置 \`developer-knowledge\` 命令，含 \`answer-query\`、\`documents search-chunks\`、\`documents describe\`。agent skill 通过 \`npx skills add google/skills --skill retrieving-developer-knowledge\` 安装，可对接 MCP server。客户端库支持 \`BatchGetDocuments\` 单次最多取 20 篇文档。

**标签**: `#product`, `#lab`, `#industry`

---

<a id="item-ai-daily-6"></a>
### [Radisson 推出 ChatGPT 插件](https://openai.com/index/radisson) ⭐️ 6.8/10

Radisson Hotel Group 与 Accenture 合作，基于 OpenAI 技术构建 ChatGPT 插件。该插件帮助旅客在规划行程时查找、比较并预订酒店。OpenAI 官方博客发布了这一合作，属于产品集成，不涉及模型或政策变化。

rss · OpenAI Blog · 10月7日 07:00

**「为什么重要」** 酒店预订进入 ChatGPT 插件场景，显示对话式入口开始承接具体行业交易流程。

**「可关注」** 该插件覆盖查找、比较到预订的完整链路，由 Accenture 与 Radisson 联合交付。

**标签**: `#product`, `#industry`, `#lab`

---

## AI 羊毛

<a id="item-ai-deals-1"></a>
### [Claude: Monthly API credits for Max and Team plans](https://support.claude.com/en/articles/17154008-monthly-api-credits-for-max-and-team-plans) ⭐️ 7.0/10

Claude 官方页面宣布 Max 和 Team 订阅用户可获得每月 API credits。

rss · HN Free API / Credits · 10月7日 18:52

**标签**: `#credits`, `#api`, `#promo`

---

<a id="item-ai-deals-2"></a>
### [Claude Agents SDK will no longer use subscription; API credits included in plans](https://news.ycombinator.com/item?id=49997654) ⭐️ 6.0/10

Claude Max and Team plans now include monthly API credits covering the Agent SDK, Claude API, and Managed Agents, claimable into a Claude Console organization.

rss · HN Free API / Credits · 10月7日 19:28

**标签**: `#credits`, `#api`, `#promo`

---

<a id="item-ai-deals-3"></a>
### [Claude Max and Teams plans now forced to API \(Oct 7th update\)](https://news.ycombinator.com/item?id=49999508) ⭐️ 5.0/10

Claude Max 与 Team 套餐用户现可在 Console 组织中领取月度 API credits，用于 Agent SDK、Claude API 及 Managed Agents。

rss · HN Free API / Credits · 10月7日 22:15

**标签**: `#credits`, `#api`, `#promo`

---