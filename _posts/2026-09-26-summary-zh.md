---
layout: default
title: "Horizon Summary: 2026-09-26 (ZH)"
date: 2026-09-26
lang: zh
---

> 从 189 条内容中筛选出 11 条重要资讯。

---

**Harness 架构**
1. [Mastra 1.70.0 发布：模型路由](#item-harness-arch-1) ⭐️ 8.8/10
2. [Claude Code 2.1.283 发布](#item-harness-arch-2) ⭐️ 8.8/10
3. [anthropics/claude-code released v2.1.283](#item-harness-arch-3) ⭐️ 8.3/10
4. [Pydantic-AI v2.51.0 接入 GPT-Live](#item-harness-arch-4) ⭐️ 8.3/10
5. [pydantic-ai v2.50.0 发布](#item-harness-arch-5) ⭐️ 8.3/10
6. [DSPy 3.4.0 发布](#item-harness-arch-6) ⭐️ 8.3/10
7. [openai/codex released rust-v0.157.0](#item-harness-arch-7) ⭐️ 7.8/10

**Agent 工程师日报**
1. [Qwengram-0.8B 迁移 PLE 记忆，PPL 降 5.05%](#item-agent-engineer-1) ⭐️ 5.5/10
2. [Mica v0.1 4B got an iron pickaxe in real Minecraft without generating a single token](#item-agent-engineer-2) ⭐️ 5.5/10

**AI 日报**
1. [GitHub Copilot app for Beginners: How to build custom workflows with canvases](#item-ai-daily-1) ⭐️ 6.8/10

**科技博客**
1. [@simonw: RT @hillelogram: @simonw &quot;It doesn&\#x27;t get easier, y...](#item-tech-blog-1) ⭐️ 0.0/10

---

## Harness 架构

<a id="item-harness-arch-1"></a>
### [Mastra 1.70.0 发布：模型路由](https://github.com/mastra-ai/mastra/releases/tag/%40mastra/core%401.70.0) ⭐️ 8.8/10

Mastra 1.70.0 发布。ModelSelectionProcessor 通过分类器为每次请求动态选择模型，支持 scope: &\#x27;first-step&\#x27; 与 minProbability 控制路由范围。cancelQueuedMessages\(\{ signalIds \}\) 跨进程取消同一 runtime + memory 线程下所有 Agent 的待处理输入。观测查询引入可信 \{ organizationId, resourceId \} 租户作用域，由存储层强制并绑定到游标。

github · PaulieScanlon · 9月25日 10:06

**「设计要点」** ModelSelectionProcessor 挂在 inputProcessors 层，由分类器决定模型，失败时回落到 Agent 默认模型。cancelQueuedMessages 依赖共享 runtime + memory 线程实现跨 Agent 取消；观测查询的租户作用域由 store 强制执行，@mastra/server 从预留 organizationId 请求上下文键自动派生。

**「改了什么」** 新增 ModelSelectionProcessor 动态模型路由、cancelQueuedMessages 跨进程取消、可信租户作用域的 trace 查询，以及 closeOnSuspend durable stream\(\)/resume\(\) 选项。playground-ui 移除 ErrorState、PermissionDenied、SessionExpired 等组件，并去掉 Button outline 变体。

**标签**: `#runtime`, `#memory`, `#eval`, `#permissions`

---

<a id="item-harness-arch-2"></a>
### [Claude Code 2.1.283 发布](https://code.claude.com/docs/en/changelog#2-1-283) ⭐️ 8.8/10

Claude Code 2.1.283 发布。新增 \`x-claude-code-prompt-id\` 网关提示头，经 \`CLAUDE\_CODE\_GATEWAY\_HINT\_HEADERS=1\` 开启，供 LLM 网关聚合同一提示的请求。新增 \`availableModelsMatch\` 与 \`deniedModels\` 托管设置，收紧模型版本与黑名单管控。\`OTEL\_LOG\_TOOL\_CONTENT=1\` 下，MCP 工具、WebFetch、WebSearch 输出进入 \`tool.output\` OpenTelemetry span 事件。\`/doctor prompt-audit\` 与 \`/checkup prompt-audit\` 可审计 CLAUDE.md、skills、agents、commands 中面向旧模型的提示模式。

rss · Claude Code Changelog · 9月25日 22:00

**「设计要点」** 网关层新增请求分组提示头与 \`load\_test\_mode\` 压测块。模型权限通过托管设置精确到版本，工具输出可经 OTEL 落库，便于评测与审计。

**「改了什么」** 新增 \`availableModelsMatch\` 与 \`deniedModels\` 托管设置，模型权限支持版本级精确匹配与黑名单。网关侧加入 \`x-claude-code-prompt-id\` 请求分组与 \`load\_test\_mode\` 压测配置，OTEL 工具内容日志与 \`/doctor prompt-audit\` 诊断命令同步上线。

**标签**: `#runtime`, `#permissions`, `#eval`, `#tools`, `#mcp`

---

<a id="item-harness-arch-3"></a>
### [anthropics/claude-code released v2.1.283](https://github.com/anthropics/claude-code/releases/tag/v2.1.283) ⭐️ 8.3/10

Claude Code v2.1.283 adds managed model permission controls, gateway request-grouping headers, OTEL tool-content logging, and a prompt-audit diagnostic.

github · ashwin-ant · 9月25日 21:50

**标签**: `#runtime`, `#tools`, `#permissions`, `#eval`, `#mcp`

---

<a id="item-harness-arch-4"></a>
### [Pydantic-AI v2.51.0 接入 GPT-Live](https://github.com/pydantic/pydantic-ai/releases/tag/v2.51.0) ⭐️ 8.3/10

Pydantic-AI v2.51.0 发布，新增 \`OpenAILiveModel\` 接入 GPT-Live。realtime session 暴露 \`context\_window\_used\`，取 GPT-Live 上报的 ratio 或 response usage。OpenAI、Azure OpenAI、xAI 的 realtime \`tool\_choice\` 若强制工具调用，直接抛 \`UserError\`。Gemini Live 侧匹配 dated \`gemini-3.8-live\` id，连接时拒绝 \`google\_affective\_dialog\`，close code 转为 \`RealtimeError\`。

github · DouweM · 9月25日 23:19

**「设计要点」** realtime 工具校验前移到 connect 阶段，OpenAI/Azure/xAI 强制 tool\_choice 直接报错，Gemini 在连接时拒绝 affective dialog。\`context\_window\_used\` 把实时会话的上下文占用显式暴露给调用方。Agent graph 改为缓存复用，\`RunContext\` 在 capability hooks 中的复制开销下降。

**「改了什么」** 新增 \`OpenAILiveModel\` 接入 GPT-Live；realtime session 新增 \`context\_window\_used\` 字段；OpenAI/Azure/xAI 的强制 tool\_choice 从静默接受改为抛 \`UserError\`；Gemini Live 增加连接时 id 匹配与 close code 错误转换。性能侧缓存 agent graph，减少 \`RunContext\` 复制，单子节点不再起 task group。

**标签**: `#runtime`, `#tools`

---

<a id="item-harness-arch-5"></a>
### [pydantic-ai v2.50.0 发布](https://github.com/pydantic/pydantic-ai/releases/tag/v2.50.0) ⭐️ 8.3/10

pydantic-ai v2.50.0 发布，核心是给 Decisions 协议加了 DecisionModel 路由基类，并让 TypeSafeModel 继承它。新增 RunContext.in\_durable\_context，让 hook 能识别自己是否跑在 durable workflow 代码里。ModelSelectionContext 也做了破坏性调整：messages 以被路由的请求结尾，并新增 prompt 字段。决策模型的工具调用倾向改为 opt-in 的 decision\_route\_threshold。

github · DouweM · 9月25日 04:47

**「设计要点」** DecisionModel 作为路由基类统一了 Decisions 协议的模型抽象，TypeSafeModel 纳入同一体系；RunContext.in\_durable\_context 把 durable workflow 的执行状态暴露给 hook，便于运行时区分普通调用与持久化流程。

**「改了什么」** 相对 v2.49.0，v2.50.0 引入 DecisionModel 基类与 decide span，把路由决策从特例提升为可观测的协议层能力；同时用 decision\_route\_threshold 替换原先的工具调用倾向，并调整 ModelSelectionContext 的消息边界与 prompt 字段，属于破坏性变更。

**标签**: `#runtime`, `#planning`, `#tools`

---

<a id="item-harness-arch-6"></a>
### [DSPy 3.4.0 发布](https://github.com/stanfordnlp/dspy/releases/tag/3.4.0) ⭐️ 8.3/10

DSPy 3.4.0 通过 TypeSafe 客户端接入 Jev 决策后端，在普通签名中引入概率证据。新增实验类型 Noul、Choice、Score，分别输出布尔、多选与评分的决策值及概率、置信度。ReAnchor 依据程序指标校准阈值与权重，不修改指令或示例。LM 层切换为原生 lm15 引擎，支持注册自定义 HTTP provider。3.4 为 LM 过渡版本，3.5 是迁移死线。

github · isaacbmiller · 9月25日 04:06

**「设计要点」** DSPy 将 LM 请求抽象为 lm15 类型，默认 engine=&quot;auto&quot; 优先原生执行，仅在推理前选择 LiteLLM 兼容回退，认证失败与超时不触发切换。决策阈值、Score 切分和 Choice 权重在本地应用，相同请求可复用缓存证据。Jev 作为决策后端要求所有输出字段受支持，无生成式回退，嵌套决策输出不获得同等证据解码。

**「改了什么」** 3.3 引入的实验性 LM 类型被替换，旧版自定义 LM 与 OpenAI 风格 messages= 调用保留但标记弃用。RLM 解释器 API 改为关键字参数 interpreter\_factory=，不再接受实例或位置工厂。新增本地 CPython 解释器与异步 ReActV2。

**标签**: `#runtime`, `#tools`, `#eval`

---

<a id="item-harness-arch-7"></a>
### [openai/codex released rust-v0.157.0](https://github.com/openai/codex/releases/tag/rust-v0.157.0) ⭐️ 7.8/10

Codex Rust v0.157.0 adds background-server auto-start, conversation forking, and remote import support alongside GPT-6 model updates.

github · github-actions\[bot\] · 9月25日 02:31

**标签**: `#runtime`, `#tools`, `#planning`

---

## Agent 工程师日报

<a id="item-agent-engineer-1"></a>
### [Qwengram-0.8B 迁移 PLE 记忆，PPL 降 5.05%](https://www.reddit.com/r/LocalLLaMA/comments/1wpvep4/qwengram08b_i_transferred_qwen38_flashnexts_ngram/) ⭐️ 5.5/10

作者 Nicolodeva 将 Qwen3.8-Flash-Next 的 51B 参数 PLE n-gram 记忆迁移进 Qwen3.5-0.8B，主干与 PLE 均冻结，只在 decoder 第 3、9 层挂 R=1 reader，并用 token 级线性门控动态注入。冻结验证集上 PPL 从 18.2759 降至 17.3534，降幅 5.05%；作者说明这是语言模型验证结果，不是基准准确率提升。15M token 的 reader 是平衡检查点，20M 虽进一步降低聚合损失但数学回退。推理路径已在 llama.cpp 实现，GGUF 只含主干与 reader，PLE 作为外部量化 sidecar。

reddit · r/LocalLLaMA · /u/Nicolodeva · 9月25日 12:46

**「为什么重要」** 实验表明冻结大规模 PLE 记忆、仅训练轻量 reader 即可为小模型带来可测量的困惑度下降，且推理侧可在 llama.cpp 中以外部 sidecar 部署。对算力受限的实践者，这提供了一条不微调主干、用动态门控注入外部记忆的参考路径。

**「可关注」** PLE 记忆以外部量化 sidecar 形式与主干 GGUF 分离，Q8\_0 在独立 WikiText-2 运行时测试中保留 99.1% 的 BF16 reader NLL 增益。

**标签**: `#memory`, `#eval`, `#orchestration`

---

<a id="item-agent-engineer-2"></a>
### [Mica v0.1 4B got an iron pickaxe in real Minecraft without generating a single token](https://www.reddit.com/r/LocalLLaMA/comments/1wqahbz/mica_v01_4b_got_an_iron_pickaxe_in_real_minecraft/) ⭐️ 5.5/10

A 4B model plays Minecraft by scoring candidate commands with zero generated tokens in ~90–150 ms per step, but the Reddit-only source limits it to browse-level priority.

reddit · r/LocalLLaMA · /u/Top-Evidence174 · 9月25日 22:55

**标签**: `#coding-agent`, `#eval`, `#harness`, `#observability`

---

## AI 日报

<a id="item-ai-daily-1"></a>
### [GitHub Copilot app for Beginners: How to build custom workflows with canvases](https://github.blog/ai-and-ml/github-copilot/github-copilot-app-for-beginners-how-to-build-custom-workflows-with-canvases/) ⭐️ 6.8/10

GitHub&\#x27;s official blog offers a beginner guide to creating custom workflows with canvases in the GitHub Copilot app.

rss · GitHub Blog · 9月25日 18:00

**标签**: `#product`, `#lab`, `#model`

---

## 科技博客

<a id="item-tech-blog-1"></a>
### [@simonw: RT @hillelogram: @simonw &quot;It doesn&\#x27;t get easier, y...](https://twitter.com/simonw/status/tweet-2103495582048555120) ⭐️ 0.0/10

A retweeted quote about programming speed that lacks technical substance or transferable lessons.

twitter · Simon Willison · 9月25日 14:43

**标签**: `#software engineering`, `#productivity`, `#quotation`, `#social media`

---