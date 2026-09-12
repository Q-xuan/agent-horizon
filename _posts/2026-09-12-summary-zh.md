---
layout: default
title: "Horizon Summary: 2026-09-12 (ZH)"
date: 2026-09-12
lang: zh
---

> 从 189 条内容中筛选出 14 条重要资讯。

---

**Harness 架构**
1. [Cloudflare Agents agents@0.23.0 发布](#item-harness-arch-1) ⭐️ 8.8/10
2. [agents @think@0.18.0 发布](#item-harness-arch-2) ⭐️ 7.8/10
3. [cloudflare/agents @cloudflare/ai-chat@0.12.0 发布](#item-harness-arch-3) ⭐️ 7.8/10
4. [Mastra @mastra/core@1.66.0 发布](#item-harness-arch-4) ⭐️ 7.8/10
5. [DSPy 3.4.0b1 发布](#item-harness-arch-5) ⭐️ 7.8/10
6. [Claude Code v2.1.269 发布](#item-harness-arch-6) ⭐️ 6.8/10
7. [Cline desktop-v0.0.26 发布](#item-harness-arch-7) ⭐️ 6.8/10
8. [Letta Code GitHub trending](#item-harness-arch-8) ⭐️ 5.0/10

**Agent 工程师日报**
1. [Devin Fusion harness 发布](#item-agent-engineer-1) ⭐️ 7.8/10
2. [OpenRouter provider.only 避免行为差异](#item-agent-engineer-2) ⭐️ 7.0/10

**AI 日报**
1. [OpenAI Habitat 存储平台服务 10 亿用户](#item-ai-daily-1) ⭐️ 8.8/10
2. [Perplexity 使用 Astra 内部系统](#item-ai-daily-2) ⭐️ 5.8/10
3. [GitHub 博客：营销 ops 代码化](#item-ai-daily-3) ⭐️ 5.8/10

**AI 羊毛**
1. [Epic Games 免费游戏 9.11-9.17](#item-ai-deals-1) ⭐️ 6.0/10

---

## Harness 架构

<a id="item-harness-arch-1"></a>
### [Cloudflare Agents agents@0.23.0 发布](https://github.com/cloudflare/agents/releases/tag/agents%400.23.0) ⭐️ 8.8/10

Cloudflare Agents agents@0.23.0 发布。提取 facet 子代理路由和 WebSocket 转发机制到 dynamic-agents 生命周期能力，新增 this.dynamicAgents 公共 facade。facet 定位为隔离原语而非推荐的聊天会话建模方式。新增 RoutedAgents 能力，支持用户中心与每个聊天一个 Durable Object 的拓扑。

github · github-actions\[bot\] · 9月11日 10:42

**「设计要点」** 将 facet 路由、WebSocket 转发、虚拟连接和注册表提取到 dedicated dynamic-agents 模块，注册为 Lifecycle capability。热路径保持 composition-root wiring。新增 this.dynamicAgents 能力 facade。facet 作为隔离原语定位。

**「改了什么」** 提取 facet 子代理路由和 WebSocket 转发机制到 dynamic-agents 能力，新增 this.dynamicAgents facade。新增 RoutedAgents 能力，支持用户中心与每个聊天一个 Durable Object 拓扑。

**标签**: `#subagents`, `#runtime`, `#dynamic-agents`, `#capabilities`

---

<a id="item-harness-arch-2"></a>
### [agents @think@0.18.0 发布](https://github.com/cloudflare/agents/releases/tag/%40cloudflare/think%400.18.0) ⭐️ 7.8/10

Cloudflare agents 框架发布 @cloudflare/think@0.18.0 版本。存储从旧表迁移到 agents/sessions，提示上下文迁移到 agents/context。原有子类保持编译和运行兼容，但上下文方法已废弃。存储迁移在首次唤醒时进行，无法回滚。

github · github-actions\[bot\] · 9月11日 10:42

**「设计要点」** 设计要点：Lifecycle 拥有持久化作业队列，由告警事件循环驱动。作业包含可序列化回调地址，调度通过 scoped jobs surface。

**「改了什么」** 相对上一版，存储重构是主要变更。会话存储迁移到 agents/sessions，上下文迁移到 agents/context，移除部分旧 API。调度机制从 alarm 改为 durable job queue。

**标签**: `#runtime`, `#memory`

---

<a id="item-harness-arch-3"></a>
### [cloudflare/agents @cloudflare/ai-chat@0.12.0 发布](https://github.com/cloudflare/agents/releases/tag/%40cloudflare/ai-chat%400.12.0) ⭐️ 7.8/10

Cloudflare agents 0.12.0 发布，更新 AIChatAgent 消息处理。消息通过 agents/sessions 表存储，同时保留可变 messages 数组、破坏性再生、保留、广播和 v4 消息转换。首次唤醒时迁移，无回滚。this.messages 空直到 onStart，hydrationByteBudget 为 32 MiB。

github · github-actions\[bot\] · 9月11日 10:42

**「设计要点」** 消息通过 agents/sessions 表持久化，首次唤醒迁移。Streams 使用 durable chunk log。this.messages 延迟到 onStart 加载。

**「改了什么」** AIChatAgent 消息从 cf\_ai\_chat\_agent\_messages 迁移到 agents/sessions 表。Streams 能力重构为 resumable streams。恢复尝试改为 chained Tasks。

**标签**: `#memory`, `#runtime`

---

<a id="item-harness-arch-4"></a>
### [Mastra @mastra/core@1.66.0 发布](https://github.com/mastra-ai/mastra/releases/tag/%40mastra/core%401.66.0) ⭐️ 7.8/10

Mastra @mastra/core@1.66.0 发布。@mastra/deployer 静态生成 workers.json 清单，Cloud 部署专用 orchestration worker。Trace 查询支持多 DB，新增 span predicates、metadata.\* 和 feedback/scores 过滤。Observability 存储添加 deleteFeedback\(\) 和 deleteScores\(\)。

github · PaulieScanlon · 9月11日 09:37

**「设计要点」** @mastra/memory 添加 beforeObservation、afterObservation、beforeReflection、afterReflection 等 async transform hooks，允许在模型调用前或持久化前过滤或重塑消息和观测。Mastra.getWorkerConfig\(\) 暴露 worker topology 和 instance-level settings，便于部署工具比对 runtime 和 build-time 配置。

**「改了什么」** 相比上一版，@mastra/core@1.66.0 新增 span name、model provider、timing、outcome、identity 和 version lineage 的 trace filters。添加 deleteFeedback\(\) 和 deleteScores\(\) 到 observability storage。

**标签**: `#runtime`, `#deployment`, `#observability`, `#traces`, `#queries`

---

<a id="item-harness-arch-5"></a>
### [DSPy 3.4.0b1 发布](https://github.com/stanfordnlp/dspy/releases/tag/3.4.0b1) ⭐️ 7.8/10

DSPy 3.4.0b1 是 3.4 版的首个 beta 版本。它将语言模型执行迁移到共享引擎接口，并添加了本地 CPython 解释器用于受信任代码，同时为 ReActV2 引入异步执行。还新增了 GEPA 的自定义 Flex 代码提案，并修复了评估、流式传输和演示采样等 bug。此为 prerelease，API 可能在稳定版前变更。安装命令为 pip install --upgrade &quot;dspy==3.4.0b1&quot;。

github · isaacbmiller · 9月11日 22:24

**「设计要点」** DSPy 3.4 采用共享 LM 引擎接口，支持 native lm15 和 LiteLLM 后端。LocalInterpreter 提供持久本地 CPython 执行环境，但非安全沙箱，保留主机文件系统和凭证访问。

**「改了什么」** 3.4.0b1 取代了 3.3 实验 LM 类型，引入共享引擎和本地解释器。ReActV2 支持异步调用，并修复了 GEPA 评估对崩溃示例的处理。

**标签**: `#runtime`, `#sandbox`, `#tools`, `#eval`, `#planning`

---

<a id="item-harness-arch-6"></a>
### [Claude Code v2.1.269 发布](https://github.com/anthropics/claude-code/releases/tag/v2.1.269) ⭐️ 6.8/10

Claude Code v2.1.269 发布。新增了可复现插件评估功能，支持运行插件评估套件并生成 JSON 和 HTML 报告。添加了 /output-style 支持、Bash 工具文件变更差异、OTEL 仓库指标标签，以及 Workflow 工具并发代理限制。

github · ashwin-ant · 9月11日 19:17

**「改了什么」** 新增了可复现的插件评估套件，支持在远程控制和云端会话中切换输出样式，并为 Bash 工具添加了文件编辑变更差异。还添加了 OTEL 仓库指标标签和 Workflow 工具的并发代理限制。

**标签**: `#eval`, `#tools`, `#subagents`, `#runtime`

---

<a id="item-harness-arch-7"></a>
### [Cline desktop-v0.0.26 发布](https://github.com/cline/cline/releases/tag/desktop-v0.0.26) ⭐️ 6.8/10

Cline desktop v0.0.26 发布。Composer 集成当前分支 GitHub PR 显示，包括 PR 编号、合并状态、变更行数和 CI 检查。支持点击打开浏览器或展开 CI 日志，状态每 30 秒刷新。Customize 视图合并 Tools、Skills、Rules 标签为一个列表，并添加搜索栏和切换功能。

github · github-actions\[bot\] · 9月11日 07:46

**「改了什么」** 相比 v0.0.25，Composer 集成 GitHub PR 显示和 CI 检查。Customize 视图合并 Tools、Skills、Rules 标签为一个列表，并添加搜索栏和切换功能。

**标签**: `#runtime`, `#tools`

---

<a id="item-harness-arch-8"></a>
### [Letta Code GitHub trending](https://github.com/letta-ai/letta-code) ⭐️ 5.0/10

GitHub trending 展示 letta-ai/letta-code 仓库。Letta Code 是一个 stateful agent harness。Letta Code 创建 memory-equipped identity-driven agents。Agents 通过 self-rewriting memory、skills、prompts 和 even the harness itself（through mods）学习和进化。

rss · GitHub Trending Daily · 9月12日 01:18

**标签**: `#memory`, `#runtime`, `#tools`

---

## Agent 工程师日报

<a id="item-agent-engineer-1"></a>
### [Devin Fusion harness 发布](https://cognition.ai/blog/local-fusion) ⭐️ 7.8/10

Fusion harness 现已集成到 Devin Desktop 和 CLI 中。Fusion 通过并行运行 lead 和 sidekick 代理实现高效性，lead 负责规划和审查，sidekick 负责执行。推荐搭配 Fable 5.1 与 SWE-2。在多个 coding benchmarks 上，Fusion 效率提升高达 39%，同时降低显著成本。例如 DeepSWE 1.1 基准中 Fusion \(Fable 5.1 + SWE-2\) 成本降低 46%。

rss · Cognition Blog · 9月11日 17:00

**「为什么重要」** Fusion harness 已集成到 Devin Desktop 和 CLI 中。开发者可直接在本地使用该 harness 验证其在 coding benchmarks 上的效率提升。

**「可关注」** 可关注：更强的 sidekick 模型可降低整体系统成本，尽管其 token 价格更高。

**标签**: `#harness`, `#coding-agent`, `#eval`, `#orchestration`

---

<a id="item-agent-engineer-2"></a>
### [OpenRouter provider.only 避免行为差异](https://simonwillison.net/2026/Sep/11/so-you-want-to-use-openrouter/) ⭐️ 7.0/10

OpenRouter 自动 fallback 和成本路由是其卖点，但 Mohamed Moustafa 指出这可能导致问题。不同提供程序运行不同服务软件，优化和设置不同，导致同一 OpenRouter 端点上的模型请求行为不同。部分提供程序缺乏视觉模型支持，reasoning effort 选项处理方式也不同。使用 provider.only 选项可控制路由到特定提供程序，/endpoints 方法可获取可用提供程序列表。

rss · Simon Willison · 9月11日 22:49

**「为什么重要」** OpenRouter 自动 fallback 的行为差异已发生，但对代理工具链一致性的影响尚未证实。使用 provider.only 可避免潜在的不一致行为。

**「可关注」** 可关注：使用 provider.only 选项控制路由到特定提供程序，并通过 /endpoints 方法获取可用列表。

**标签**: `#orchestration`, `#coding-agent`

---

## AI 日报

<a id="item-ai-daily-1"></a>
### [OpenAI Habitat 存储平台服务 10 亿用户](https://openai.com/index/scaling-storage-one-billion-users-part-one) ⭐️ 8.8/10

OpenAI 将 Habitat Python 库演进为全球分布式存储平台，服务 10 亿 ChatGPT 用户。平台支持 2200 万请求每秒。演进过程从 Python 库扩展到全球规模。

rss · OpenAI Blog · 9月11日 10:00

**「为什么重要」** OpenAI 存储扩展展示了大规模在线存储系统的实现路径。

**「可关注」** 可关注：从 Python 库演进到全球分布式存储平台

**标签**: `#lab`, `#industry`, `#product`

---

<a id="item-ai-daily-2"></a>
### [Perplexity 使用 Astra 内部系统](https://openai.com/index/perplexity-improving-accuracy-with-astra) ⭐️ 5.8/10

Perplexity 使用 Astra 系统撰写沟通、修改软件并监控生产系统。检查频率比使用早期模型时低很多。

rss · OpenAI Blog · 9月14日 00:00

**「可关注」** 可关注：Perplexity 使用 Astra 撰写沟通、修改软件并监控生产系统，且检查频率比早期模型时低很多。

**标签**: `#openai`, `#perplexity`, `#astra`, `#product`, `#industry`

---

<a id="item-ai-daily-3"></a>
### [GitHub 博客：营销 ops 代码化](https://github.blog/ai-and-ml/github-copilot/marketing-ops-as-code-automating-events-from-planning-to-follow-up-on-github/) ⭐️ 5.8/10

GitHub 博客发布文章，Tomoko Tanaka 记录了如何使用代码支持 APAC 营销团队的事件自动化。她将营销运营工作写成代码，实现从规划到跟进的自动化。文章出现在 GitHub 官方博客。

rss · GitHub Blog · 9月11日 18:26

**「可关注」** 可关注：将工作写成代码即可自动化。

**标签**: `#product`, `#industry`, `#github`

---

## AI 羊毛

<a id="item-ai-deals-1"></a>
### [Epic Games 免费游戏 9.11-9.17](https://www.appinn.com/eggs-26911/) ⭐️ 6.0/10

Epic Games 9.11-9.17 期间免费送出三款游戏，电脑游戏为《天空奇兵 / LUFTRAUSERS》和《星界战士 / Astral Ascent》，手机游戏为《Alone With You》。这些游戏可通过 Epic Launcher 领取，领取条件是在活动期间内完成。截止时间为 9.17。

rss · 小众软件 · 9月11日 07:48

**「可关注」** 可关注：领取需在 Epic Launcher 完成，截止 9.17。

**标签**: `#promo`, `#limited-free`, `#games`

---