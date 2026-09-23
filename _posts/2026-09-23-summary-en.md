---
layout: default
title: "Horizon Summary: 2026-09-23 (EN)"
date: 2026-09-23
lang: en
---

> From 220 items, 18 important content pieces were selected

---

**Agent Harness Architecture**
1. [Cline desktop v0.0.34 发布](#item-harness-arch-1) ⭐️ 8.8/10
2. [vllm-project/vllm released v0.30.0](#item-harness-arch-2) ⭐️ 8.8/10
3. [Claude Code v2.1.280 发布](#item-harness-arch-3) ⭐️ 8.3/10
4. [openai/codex released rust-v0.156.0](#item-harness-arch-4) ⭐️ 8.3/10
5. [Cline 桌面 v0.0.33 发布](#item-harness-arch-5) ⭐️ 8.3/10
6. [2.1.280](#item-harness-arch-6) ⭐️ 8.3/10
7. [Cline SDK v0.0.85 发布](#item-harness-arch-7) ⭐️ 7.8/10

**AI Agent Engineer**
1. [Claude Opus 5.5 发布，降价](#item-agent-engineer-1) ⭐️ 9.0/10
2. [simonw released 0.36 in simonw/llm](#item-agent-engineer-2) ⭐️ 8.3/10
3. [llm 0.36 新增单轮模型插件标志](#item-agent-engineer-3) ⭐️ 7.5/10
4. [Opus 5.5 与 GPT-6 发布，价格战升级](#item-agent-engineer-4) ⭐️ 6.5/10
5. [simonw released 0.29 in simonw/llm-anthropic](#item-agent-engineer-5) ⭐️ 6.3/10
6. [GPT-6 Sol and Luna](#item-agent-engineer-6) ⭐️ 5.5/10

**AI Daily**
1. [GPT-6 Sol 与 Luna 发布](#item-ai-daily-1) ⭐️ 9.8/10
2. [GPT-6 改进 prompt 缓存](#item-ai-daily-2) ⭐️ 9.3/10
3. [Parallel 用 GPT‑6 Astra 减半研究耗时与成本](#item-ai-daily-3) ⭐️ 5.8/10

**AI Deals**
1. [OpenRouter Batch 半价推理](#item-ai-deals-1) ⭐️ 8.0/10
2. [产品评论分析 API 注册送 $1 额度](#item-ai-deals-2) ⭐️ 5.0/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [Cline desktop v0.0.34 发布](https://github.com/cline/cline/releases/tag/desktop-v0.0.34) ⭐️ 8.8/10

Cline desktop v0.0.34 修复 Composio 工具加载、Mac SSH 远程和会话错误持久化。Composio 连接器拉取全部工具并刷新缓存，不再停留在前 20 个。Mac 到 Mac 的 SSH 远程改用签名后端 helper，Apple Silicon 和 Intel 均支持，Windows 和 Linux 桌面端仍无法直连。会话错误跨客户端保留，重试耗尽后的失败也记录，且不参与 compaction；停止等待重试的运行立即生效。

github · github-actions\[bot\] · Sep 22, 21:10

**「设计要点」** Composio 连接器改为全量拉取并刷新缓存，避免陈旧数据。Mac 主机统一使用应用自签名后端作为 SSH helper。错误条目写入转录但不参与 compaction。

**「改了什么」** Composio 工具从只读前 20 个变为全量拉取并刷新；Mac SSH 远程从提示不支持变为通过签名后端 helper 支持；会话错误从离开即失变为跨客户端和 compaction 持久化；停止运行从等待 backoff 结束变为立即生效。

**Tags**: `#tools`, `#runtime`, `#sandbox`, `#memory`

---

<a id="item-harness-arch-2"></a>
### [vllm-project/vllm released v0.30.0](https://github.com/vllm-project/vllm/releases/tag/v0.30.0) ⭐️ 8.8/10

vLLM v0.30.0 ships a persistent GPU weight-cache daemon with CUDA IPC fast-start, broad new model/kernel support, and multi-node TP capabilities.

github · khluu · Sep 22, 05:20

**Tags**: `#runtime`, `#memory`, `#prefix-cache`

---

<a id="item-harness-arch-3"></a>
### [Claude Code v2.1.280 发布](https://github.com/anthropics/claude-code/releases/tag/v2.1.280) ⭐️ 8.3/10

Claude Code v2.1.280 将 Claude Opus 5.5（claude-opus-5-5）设为默认 Opus 模型，提供 1M 上下文，输入 $4/Mtok、输出 $20/Mtok，缓存读取 $0.20/Mtok。新增环境变量 CLAUDE\_CODE\_MAX\_MCP\_DESCRIPTION\_LENGTH，可调整此前固定的 2,048 字符 MCP 工具描述与服务器指令上限。hook\_execution\_complete OpenTelemetry 事件加入 hook 输出大小及超限输出落盘数量。修复符号链接写入判定：提示词指明落点后，acceptEdits、允许规则和 auto mode 不再批准落到目录外的写入；auto mode 在安全校验拒审时改为一次拒绝，在安全校验无结果时退避并在连续十次后停止回合。

github · ashwin-ant · Sep 22, 16:38

**「设计要点」** 权限层按解析后的真实落点判断写入，不再依赖树内路径拼写；auto mode 用一次拒绝和退避替代无限重试。可观测性通过 OpenTelemetry 暴露 hook 输出体积与落盘数量，便于评估工具层开销。

**「改了什么」** 相对旧版，默认 Opus 模型切换到 Opus 5.5；MCP 描述长度从硬编码 2,048 字符变为可配置；hook 执行事件新增输出大小与超限落盘指标；修复符号链接写入判定和 auto mode 重试循环。

**Tags**: `#runtime`, `#tools`, `#mcp`, `#permissions`, `#eval`

---

<a id="item-harness-arch-4"></a>
### [openai/codex released rust-v0.156.0](https://github.com/openai/codex/releases/tag/rust-v0.156.0) ⭐️ 8.3/10

OpenAI Codex rust-v0.156.0 ships default-enabled worktree sessions, daemon management, fullscreen TUI, voice conversations, and a usage dashboard.

github · github-actions\[bot\] · Sep 22, 19:51

**Tags**: `#runtime`, `#tools`, `#planning`

---

<a id="item-harness-arch-5"></a>
### [Cline 桌面 v0.0.33 发布](https://github.com/cline/cline/releases/tag/desktop-v0.0.33) ⭐️ 8.3/10

Cline 桌面 v0.0.33 发布，新增 git worktree 任务隔离，并修复桌面端长会话自动压缩从未运行的问题。新任务可在欢迎界面选择 Worktree，在 \`~/.cline/worktrees/\` 下创建 \`cline/&lt;id&gt;\` 分支与工作树执行，不触碰主工作区。此前 sidecar 只把会话加入检查点而未加入压缩，90% 触发条件从未安装，长对话直接耗尽空间。版本同时修正 Windows 单实例、SSH 新会话启动、更新入口及模型目录。

github · github-actions\[bot\] · Sep 22, 09:07

**「设计要点」** 运行时隔离上，新线程可切到独立 git worktree，任务删除即清理对应分支与工作树，除非仍有其他会话占用。记忆管理上，压缩器此前固定使用会话启动时的凭证，刷新后请求失败并静默回退到截断，现改为跟随会话当前凭证与模型。

**「改了什么」** 新增 Worktree 隔离，仅影响新线程；修复桌面端自动压缩失效；Windows 重复启动改为唤起已有窗口，关闭隐藏到托盘；SSH 主机新建会话不再因缺失 transcript 中断；更新检查入口加入 macOS 应用菜单与各平台托盘；删除当前会话返回新任务视图；Linux x64 恢复 pre-AVX2 CPU 支持；\`.cline/rules\` 下的规则、技能与 MCP 服务器被一致加载；单选项问题点击即提交；模型回合触及输出上限时最多重试三次；压缩不再中途静默截断；历史记录删除后不再复现；子代理在委派获批后不再逐条请求工具审批；模型目录从 203 提供商、6,079 模型更新至 209 提供商、6,237 模型。

**Tags**: `#runtime`, `#sandbox`, `#memory`

---

<a id="item-harness-arch-6"></a>
### [2.1.280](https://code.claude.com/docs/en/changelog#2-1-280) ⭐️ 8.3/10

Claude Code 2.1.280 ships Opus 5.5 as default, adds MCP description length config and hook telemetry, and patches a symlink write-approval bypass.

rss · Claude Code Changelog · Sep 22, 16:48

**Tags**: `#runtime`, `#tools`, `#mcp`, `#permissions`

---

<a id="item-harness-arch-7"></a>
### [Cline SDK v0.0.85 发布](https://github.com/cline/cline/releases/tag/sdk/sdk/v0.0.85) ⭐️ 7.8/10

Cline SDK v0.0.85 发布，改动集中在运行时恢复与默认输出额度。模型回合耗尽输出 token 却未产出可用工具调用时，不再直接以 output-token-limit 失败，而是重试至多三次。默认输出额度从固定 32,000 改为按模型上限缩放，公式为 max\(32000, floor\(maxOutputTokens \* 0.3\)\)，只升不降。模型目录同步更新，provider 数仍为 209，模型总数从 6,188 增至 6,237。

github · github-actions\[bot\] · Sep 22, 08:13

**「设计要点」** 运行时新增回合级重试恢复：三次重试之间追加“简洁回复、拆分工具调用”提示，工具调用有进展或每次运行开始时重置计数，耗尽后仍以原错误失败。空 max-tokens 响应走同一路径，且每次恢复迭代前先发 turn-finished，保证迭代事件成对。

**「改了什么」** 相对 v0.0.84，新增输出 token 耗尽后的自动重试；默认输出额度从固定 32,000 改为模型感知缩放；刷新模型目录，10 个未在 builtins.ts 固定模型的 provider 默认解析结果发生变化。

**Tags**: `#runtime`, `#tools`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [Claude Opus 5.5 发布，降价](https://www.anthropic.com/claude-opus-5-5) ⭐️ 9.0/10

2026 年 9 月 22 日，Anthropic 发布 Claude Opus 5.5。每 1M tokens 价格下调：输入 $4、输出 $20、缓存读取 $0.20、缓存写入 $5，较 Opus 5 分别降 20%、20%、60%、20%。官方称其输出更自然，长会话中更易读、易检查。这是 Anthropic 呼吁放缓前沿后的首次模型发布。

hackernews · km144 · Sep 22, 16:29 · [Discussion](https://news.ycombinator.com/item?id=49803892)

**「为什么重要」** 缓存读取成本降 60%，直接改变长会话与多轮工具调用的经济模型。输出与输入价格同步下调，降低 eval 与大规模并行任务的预算压力。

**「可关注」** 可关注：缓存读取单价降至 $0.20/1M tokens，harness 可重新评估长上下文的缓存保留策略与重复读取开销。

**「评论」** HN 讨论集中在价格与措辞。GodelNumbering 列出完整价格对比，指出 Opus 5 已是 OpenRouter 上支出最高的模型。sailingparrot 讽刺官方开头重申“放缓前沿”，随后用具体数字证明并未放缓。mcintyre1994 引用官方沟通改进描述，认为更清晰的输出有助于人工检查。wg0 表示继续使用 DeepSeek v4.1 high。

**Tags**: `#coding-agent`, `#eval`, `#harness`, `#observability`

---

<a id="item-agent-engineer-2"></a>
### [simonw released 0.36 in simonw/llm](https://github.com/simonw/llm/releases/tag/0.36) ⭐️ 8.3/10

simonw/llm 0.36 introduces a plugin API for declaring single-turn models and improves reasoning-trace formatting in logs.

github · simonw · Sep 22, 18:48

**Tags**: `#harness`, `#observability`, `#tooling`

---

<a id="item-agent-engineer-3"></a>
### [llm 0.36 新增单轮模型插件标志](https://simonwillison.net/2026/Sep/22/llm/) ⭐️ 7.5/10

Simon Willison 发布 llm 0.36，新增 gpt-6-sol 与 gpt-6-luna 两个 OpenAI 模型。插件可通过 \`supports\_conversation = False\` 声明模型仅接受单轮提示；收到 assistant 或 tool 历史时，LLM 抛出 \`llm.ConversationNotSupported\`，\`llm chat\` 启动前即拒绝。\`llm logs\` 的 Markdown 输出将推理轨迹包裹在 \`&lt;details&gt;&lt;summary&gt;\` 标签内。首个使用该标志的插件是 llm-typesafe，版本另含五位新贡献者的 bug 修复。

rss · Simon Willison · Sep 22, 18:48

**「为什么重要」** 该标志直接影响 agent harness 与工具集成管理对话和工具历史的方式，为单轮模型提供显式约束。已发生的变化是新增插件 API 与错误类型，尚未证实的影响是各 harness 的适配进度。

**「可关注」** 可关注：\`supports\_conversation = False\` 与 \`ConversationNotSupported\` 构成单轮模型的显式契约，harness 需预判该异常并调整历史传递策略。

**Tags**: `#harness`, `#coding-agent`, `#tooling`

---

<a id="item-agent-engineer-4"></a>
### [Opus 5.5 与 GPT-6 发布，价格战升级](https://simonwillison.net/2026/Sep/22/opus-and-sol-and-luna/) ⭐️ 6.5/10

Anthropic 发布 Claude Opus 5.5。OpenAI 随后发布 GPT-6 Sol 与 GPT-6 Luna。GPT-6 定价为 GPT-5.6 促销价的一半；GPT-5.6 已计划 11 月涨价 25%。GPT-6 Luna 输入/输出降至 $0.10/$0.50 每百万 token。Opus 5.5 输入/输出降至 $4/$20，缓存读取降 60%。Simon Willison 测试发现，Opus 5.5 在 max 档位下过度推理，撞上 128,000 输出上限未返回结果。两次各耗时近 20 分钟、花费 $2.56。Anthropic 预告 Sonnet 5.5 与 Haiku 5.5 即将推出。

rss · Simon Willison · Sep 22, 23:46

**「为什么重要」** GPT-6 Luna 以 $0.10/$0.50 成为 OpenAI 最便宜的可用模型之一。Opus 5.5 缓存读取降 60%，对长程 agent 对话尤其关键。Opus 5.5 max 档位在简单 SVG 任务上耗尽输出限制，高推理档位需重新评估。

**「可关注」** 可关注：GPT-6 Luna 与 Opus 5.5 定价已变，agent 成本结构需重算。但 Opus 5.5 max 档位在 128k 输出上限前失效，长任务需测试思考档位与输出预算的匹配。

**Tags**: `#coding-agent`, `#eval`

---

<a id="item-agent-engineer-5"></a>
### [simonw released 0.29 in simonw/llm-anthropic](https://github.com/simonw/llm-anthropic/releases/tag/0.29) ⭐️ 6.3/10

simonw/llm-anthropic 0.29 adds support for the Claude Opus 5.5 model via \`llm -m claude-opus-5.5\`.

github · simonw · Sep 22, 17:14

**Tags**: `#harness`, `#coding-agent`

---

<a id="item-agent-engineer-6"></a>
### [GPT-6 Sol and Luna](https://openai.com/index/introducing-gpt-6-sol-and-luna/) ⭐️ 5.5/10

HN thread reacting to the GPT-6 Sol and Luna announcement, focusing on pricing, subjective coding-agent experience, and usage-limit math.

hackernews · OfficialTurkey · Sep 22, 18:00 · [Discussion](https://news.ycombinator.com/item?id=49805509)

**Tags**: `#coding-agent`, `#observability`, `#harness`

---

## AI Daily

<a id="item-ai-daily-1"></a>
### [GPT-6 Sol 与 Luna 发布](https://openai.com/index/introducing-gpt-6-sol-and-luna) ⭐️ 9.8/10

OpenAI 官方博客发布 GPT-6 Sol 与 Luna 两款模型，称其将前沿智能带入日常工作，并在能力与成本之间提供不同平衡。官方未透露具体参数、基准成绩或定价。现阶段信息仅来自 OpenAI 一方，尚无独立评测或社区反馈。

rss · OpenAI Blog · Sep 22, 18:00

**「可关注」** OpenAI 将 GPT-6 系列拆为 Sol 与 Luna 两条产品线，后续选型需按任务复杂度匹配不同成本档位。

**Tags**: `#model`, `#lab`, `#product`

---

<a id="item-ai-daily-2"></a>
### [GPT-6 改进 prompt 缓存](https://openai.com/index/better-prompt-caching-for-gpt-6) ⭐️ 9.3/10

OpenAI 宣布 GPT-6 改进 prompt caching，带来更高缓存命中率、新诊断工具、显式断点，以及降低延迟和成本的控制选项。目前仅见官方说明，尚无第三方实测数据。

rss · OpenAI Blog · Sep 22, 21:00

**「为什么重要」** 对 coding agent 与 harness 开发者而言，prompt caching 直接影响长上下文任务的延迟与 API 成本。GPT-6 的显式断点与诊断能力，可能让缓存行为更可预测、更易调试。

**「可关注」** 可关注：GPT-6 提供显式断点与缓存诊断，用于降低延迟和成本。

**Tags**: `#model`, `#lab`, `#product`

---

<a id="item-ai-daily-3"></a>
### [Parallel 用 GPT‑6 Astra 减半研究耗时与成本](https://openai.com/index/parallel-cuts-time-and-cost-with-astra) ⭐️ 5.8/10

OpenAI 官方博客发布客户案例，称 Parallel 使用 GPT‑6 Astra 后，智能体研究与合成劳动力市场数据的耗时和成本较此前模型减半。案例仅给出单一效果声明，未披露基线模型、测试规模与任务细节。材料属一手客户宣传，证据厚度有限。

rss · OpenAI Blog · Sep 22, 12:00

**「为什么重要」** 若该效果在同类数据合成任务中可复现，GPT‑6 Astra 或能降低长周期研究型智能体的运行成本。目前仅有一家客户的一面之词，尚不能作为通用结论。

**「可关注」** 可关注：GPT‑6 Astra 在劳动力市场数据的研究与合成任务上，被客户声称可将耗时和成本减半；但官方未给出任务定义、基线模型与测试规模，暂无法作为选型依据。

**Tags**: `#model`, `#lab`, `#industry`

---

## AI Deals

<a id="item-ai-deals-1"></a>
### [OpenRouter Batch 半价推理](https://openrouter.ai/blog/announcements/batch-api/) ⭐️ 8.0/10

OpenRouter 上线 Batch API，捆绑请求可享半价推理。官方公告面向开发者，称通过批量提交降低调用成本。材料未披露具体模型范围、额度上限及截止时间。

rss · HN Free API / Credits · Sep 22, 16:42

**「为什么重要」** 对可延迟的批量任务，半价推理能直接压缩 token 支出。若业务不要求实时响应，该 API 提供了一条不改造现有链路的降本路径。

**「可关注」** 可关注：OpenRouter Batch API 适用于可排队、非交互式的推理负载；采用前需评估任务时延容忍度，并留意官方后续公布的模型覆盖与限额规则。

**Tags**: `#promo`, `#api`, `#discount`

---

<a id="item-ai-deals-2"></a>
### [产品评论分析 API 注册送 $1 额度](https://bb-product-api-docs.web.app/) ⭐️ 5.0/10

aditya314159 在 Show HN 发布产品评论分析 API，输入品牌与产品名，抓取 Amazon、TikTok、Reddit、YouTube、Instagram、Walmart 等平台的评论，提取反复出现的正面评价并附原文链接。单次分析 $0.99，注册创建 API key 赠送 $1 额度，首个产品分析免费。目前仅支持消费品，单个产品分析需数分钟。

rss · HN Free API / Credits · Sep 22, 15:45

**「可关注」** 可关注：该 API 目前仅覆盖消费品，按次计费 $0.99，可先领取 $1 额度完成一次免费分析，验证输出质量后再考虑付费。

**Tags**: `#credits`, `#promo`, `#api`, `#free-tier`

---