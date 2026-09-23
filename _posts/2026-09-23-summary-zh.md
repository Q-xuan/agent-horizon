---
layout: default
title: "Horizon Summary: 2026-09-23 (ZH)"
date: 2026-09-23
lang: zh
---

> 从 220 条内容中筛选出 18 条重要资讯。

---

**Harness 架构**
1. [Cline desktop v0.0.34 发布](#item-harness-arch-1) ⭐️ 8.8/10
2. [vllm-project/vllm released v0.30.0](#item-harness-arch-2) ⭐️ 8.8/10
3. [Claude Code v2.1.280 发布](#item-harness-arch-3) ⭐️ 8.3/10
4. [openai/codex released rust-v0.156.0](#item-harness-arch-4) ⭐️ 8.3/10
5. [Cline 桌面版 v0.0.33 发布](#item-harness-arch-5) ⭐️ 8.3/10
6. [2.1.280](#item-harness-arch-6) ⭐️ 8.3/10
7. [Cline SDK v0.0.85 改进运行时韧性](#item-harness-arch-7) ⭐️ 7.8/10

**Agent 工程师日报**
1. [Claude Opus 5.5 发布并降价](#item-agent-engineer-1) ⭐️ 9.0/10
2. [simonw released 0.36 in simonw/llm](#item-agent-engineer-2) ⭐️ 8.3/10
3. [llm 0.36 支持单轮模型约束](#item-agent-engineer-3) ⭐️ 7.5/10
4. [Opus 5.5 与 GPT-6 同日发布](#item-agent-engineer-4) ⭐️ 6.5/10
5. [simonw released 0.29 in simonw/llm-anthropic](#item-agent-engineer-5) ⭐️ 6.3/10
6. [GPT-6 Sol and Luna](#item-agent-engineer-6) ⭐️ 5.5/10

**AI 日报**
1. [GPT-6 Sol 和 Luna 发布](#item-ai-daily-1) ⭐️ 9.8/10
2. [GPT-6 优化提示缓存](#item-ai-daily-2) ⭐️ 9.3/10
3. [Parallel 用 GPT-6 Astra 减半](#item-ai-daily-3) ⭐️ 5.8/10

**AI 羊毛**
1. [OpenRouter Batch API：批量请求半价](#item-ai-deals-1) ⭐️ 8.0/10
2. [产品评论分析 API 注册送 $1 额度](#item-ai-deals-2) ⭐️ 5.0/10

---

## Harness 架构

<a id="item-harness-arch-1"></a>
### [Cline desktop v0.0.34 发布](https://github.com/cline/cline/releases/tag/desktop-v0.0.34) ⭐️ 8.8/10

Cline desktop v0.0.34 发布。Composio 连接器修复工具加载不全，完整拉取列表并刷新缓存。新增 Mac 到 Mac 的 SSH 远程连接，应用在 Apple Silicon 和 Intel 主机上使用自签名后端作为 helper。会话错误跨客户端持久保留。停止运行在重试等待期间立即生效。

github · github-actions\[bot\] · 9月22日 21:10

**「设计要点」** 工具层上，Composio 此前只加载前 20 个工具且缓存不过期，v0.0.34 改为拉取完整列表并主动刷新。远程连接层引入自签名后端 helper 处理 darwin/arm64 目标，替代系统 SSH 路径；Windows 和 Linux 桌面仍无法直接连接 Mac。状态层将失败运行和重试耗尽的错误写入转录，仅含错误的条目不参与 compaction。

**「改了什么」** Composio 工具从最多 20 个扩展到全量加载，Installed 视图计数修正。Mac 主机 SSH 远程从报错不可用变为可用，依赖签名后端 helper。错误条目从一次性提示变为持久化转录内容，并跳过压缩。停止操作从等待 backoff 结束变为立即中断。

**标签**: `#tools`, `#runtime`, `#sandbox`, `#memory`

---

<a id="item-harness-arch-2"></a>
### [vllm-project/vllm released v0.30.0](https://github.com/vllm-project/vllm/releases/tag/v0.30.0) ⭐️ 8.8/10

vLLM v0.30.0 ships a persistent GPU weight-cache daemon with CUDA IPC fast-start, broad new model/kernel support, and multi-node TP capabilities.

github · khluu · 9月22日 05:20

**标签**: `#runtime`, `#memory`, `#prefix-cache`

---

<a id="item-harness-arch-3"></a>
### [Claude Code v2.1.280 发布](https://github.com/anthropics/claude-code/releases/tag/v2.1.280) ⭐️ 8.3/10

Claude Code v2.1.280 将默认 Opus 模型切换为 Opus 5.5（\`claude-opus-5-5\`），支持 1M 上下文，输入/输出价格 $4/$20 per Mtok，缓存读取 $0.20/Mtok。新增 \`CLAUDE\_CODE\_MAX\_MCP\_DESCRIPTION\_LENGTH\` 环境变量，可调整 MCP 工具描述和服务器指令的 2,048 字符上限。\`hook\_execution\_complete\` OpenTelemetry 事件新增 hook 输出大小与超大输出落盘数量指标。权限层修复符号链接写入判定：提示明确写入落点，\`acceptEdits\`、允许规则和自动模式不再批准树外落地。

github · ashwin-ant · 9月22日 16:38

**「设计要点」** 自动模式重试逻辑收紧：安全检查拒绝审查时直接拒绝并提示重试无效；无答案时引入退避，连续十次后终止轮次。Write 工具参数校验放宽，兼容 \`path\`、\`file\_text\`、\`file\_content\` 等非标准字段；后台子代理与 fork 恢复机制修复，避免工具列表重建导致的 prompt cache 失效。

**「改了什么」** 默认模型切到 Opus 5.5，MCP 描述长度开放配置，OpenTelemetry 增加 hook 输出体积指标，符号链接写入与自动模式重试的权限判定收紧。

**标签**: `#runtime`, `#tools`, `#mcp`, `#permissions`, `#eval`

---

<a id="item-harness-arch-4"></a>
### [openai/codex released rust-v0.156.0](https://github.com/openai/codex/releases/tag/rust-v0.156.0) ⭐️ 8.3/10

OpenAI Codex rust-v0.156.0 ships default-enabled worktree sessions, daemon management, fullscreen TUI, voice conversations, and a usage dashboard.

github · github-actions\[bot\] · 9月22日 19:51

**标签**: `#runtime`, `#tools`, `#planning`

---

<a id="item-harness-arch-5"></a>
### [Cline 桌面版 v0.0.33 发布](https://github.com/cline/cline/releases/tag/desktop-v0.0.33) ⭐️ 8.3/10

Cline 桌面版 v0.0.33 发布，新增 git worktree 任务隔离，并修复桌面端 auto-compaction 长期未触发的问题。新线程可在欢迎屏把 “Work in” 切到 Worktree，首个 prompt 即从当前分支切出 \`cline/&lt;id&gt;\`，在 \`~/.cline/worktrees/\` 下建 worktree 执行，agent 不碰工作区；删除任务会清掉对应 worktree 和分支，除非仍有其他会话占用，且只影响新线程。auto-compaction 此前因 sidecar 只勾选 checkpoint 未勾选 compaction，90% 阈值从未安装，长会话直接爆上下文；该缺口可追溯到 4 月 core 将 compaction 改为 opt-in。

github · github-actions\[bot\] · 9月22日 09:07

**「设计要点」** worktree 隔离在 sidecar 层为每个新线程切出独立 git worktree，执行路径固定为 \`~/.cline/worktrees/\`，删除任务即回收分支与工作树。compaction 修复同时改了两处：sidecar 为会话装上 90% 触发，summarizer 改为跟随会话当前凭证与模型，避免凭证刷新后静默回退到截断。

**「改了什么」** 相对上一版，真正变了的能力是把任务执行搬进独立 git worktree，以及让桌面端长会话首次真正触发 auto-compaction。其余改动集中在 Windows 单实例、启动期登录、SSH 新会话、更新入口和模型目录刷新等稳定性与目录问题。

**标签**: `#runtime`, `#sandbox`, `#memory`

---

<a id="item-harness-arch-6"></a>
### [2.1.280](https://code.claude.com/docs/en/changelog#2-1-280) ⭐️ 8.3/10

Claude Code 2.1.280 ships Opus 5.5 as default, adds MCP description length config and hook telemetry, and patches a symlink write-approval bypass.

rss · Claude Code Changelog · 9月22日 16:48

**标签**: `#runtime`, `#tools`, `#mcp`, `#permissions`

---

<a id="item-harness-arch-7"></a>
### [Cline SDK v0.0.85 改进运行时韧性](https://github.com/cline/cline/releases/tag/sdk/sdk/v0.0.85) ⭐️ 7.8/10

Cline SDK v0.0.85 发布，改动集中在运行时韧性与默认输出分配。达到模型输出 token 上限但未产出工具调用的 turn 现在会重试，最多连续三次，附加简洁回复与拆分工具调用的提醒；计数器在工具调用进展和每次运行开始时重置，耗尽后仍以现有错误失败。默认输出 token 改为随模型扩展，请求限制与调用者默认值均缺失时取 \`max\(32000, floor\(maxOutputTokens \* 0.3\)\)\`，只升不降。模型目录同步更新，209 个 provider 下模型数从 6,188 增至 6,237。

github · github-actions\[bot\] · 9月22日 08:13

**「设计要点」** 网关在请求限制与调用者默认值均缺失时，按模型广告的输出上限计算默认 token 配额，保留模型输出、剩余上下文钳制与推理预算下限。重试路径通过 \`turn-finished\` 事件保持迭代配对，空的 max-tokens 响应与超限响应共用同一恢复逻辑。

**「改了什么」** 新增输出 token 超限重试，默认输出 token 从固定 32,000 改为模型感知扩展。模型目录刷新，10 个未固定模型的 provider 默认模型发生变更。

**标签**: `#runtime`, `#tools`

---

## Agent 工程师日报

<a id="item-agent-engineer-1"></a>
### [Claude Opus 5.5 发布并降价](https://www.anthropic.com/claude-opus-5-5) ⭐️ 9.0/10

Anthropic 于 2026-09-22 发布 Claude Opus 5.5。相比 Opus 5，每 1M tokens 输入价格由 $5 降至 $4，输出由 $25 降至 $20，缓存读取由 $0.50 降至 $0.20，缓存写入由 $6.25 降至 $5。官方称新模型通信更自然，长会话中更易跟随与检查。

hackernews · km144 · 9月22日 16:29 · [社区讨论](https://news.ycombinator.com/item?id=49803892)

**「为什么重要」** 缓存读取降价幅度最大，对依赖长会话与高频调用的 coding agent 成本结构影响直接。官方所称的通信改进则关系 harness 的输出解析与人工检查流程。

**「可关注」** Opus 5.5 缓存读取价格降至原来的 40%，依赖 prompt caching 的 coding agent 可重新测算长会话成本。

**「评论」** 社区讨论集中在价格与 Anthropic 的 frontier pacing 立场上。有用户质疑其上周呼吁放缓前沿发展，本周即发布大幅升级模型；也有用户表示已转向 DeepSeek v4.1 等低成本方案。

**标签**: `#coding-agent`, `#eval`, `#harness`, `#observability`

---

<a id="item-agent-engineer-2"></a>
### [simonw released 0.36 in simonw/llm](https://github.com/simonw/llm/releases/tag/0.36) ⭐️ 8.3/10

simonw/llm 0.36 introduces a plugin API for declaring single-turn models and improves reasoning-trace formatting in logs.

github · simonw · 9月22日 18:48

**标签**: `#harness`, `#observability`, `#tooling`

---

<a id="item-agent-engineer-3"></a>
### [llm 0.36 支持单轮模型约束](https://simonwillison.net/2026/Sep/22/llm/) ⭐️ 7.5/10

2026 年 9 月 22 日，Simon Willison 发布 llm 0.36。新增 gpt-6-sol 与 gpt-6-luna 两个 OpenAI 模型。模型插件可声明 supports\_conversation = False，标记只接受单轮提示的模型；LLM 在收到助手或工具历史时抛出 llm.ConversationNotSupported，llm chat 也会在启动前拒绝这类模型。llm logs 的 Markdown 输出将推理轨迹包裹在 &lt;details&gt;&lt;summary&gt; 标签中，版本另含五位新贡献者的 bug 修复。

rss · Simon Willison · 9月22日 18:48

**「为什么重要」** 该标志把单轮模型的限制前移到插件声明与 llm chat 启动阶段，而非调用后抛错。对需要动态管理对话与工具历史的 harness 和插件集成，这提供了明确的失败边界。

**「可关注」** 可关注：为自研模型插件声明 supports\_conversation = False，可在 llm chat 启动前阻断单轮模型接收历史，减少运行时错误。

**标签**: `#harness`, `#coding-agent`, `#tooling`

---

<a id="item-agent-engineer-4"></a>
### [Opus 5.5 与 GPT-6 同日发布](https://simonwillison.net/2026/Sep/22/opus-and-sol-and-luna/) ⭐️ 6.5/10

Anthropic 发布 Claude Opus 5.5，OpenAI 约一小时后推出 GPT-6 Sol 与 GPT-6 Luna。GPT-6 两个型号价格较 GPT-5.6 现行促销价减半（GPT-5.6 已计划 11 月涨价 25%）：Luna 为 $0.10/M 输入、$0.50/M 输出，Sol 为 $2/M 输入、$10/M 输出。Claude Opus 5.5 相比 Opus 5.0 输入与输出降价 20% 至 $4/M 与 $20/M，缓存读取价格下降 60%。Simon Willison 测试发现 Opus 5.5 在 max 思考等级下因过度推理触及 128,000 输出 token 上限而无法完成响应，两次均失败，每次花费 $2.56、耗时近 20 分钟。

rss · Simon Willison · 9月22日 23:46

**「为什么重要」** GPT-6 与 Opus 5.5 的降价直接压缩 coding agent 与长对话场景的推理成本，Opus 5.5 缓存读取降 60% 对 agentic 对话尤其关键。同时 Opus 5.5 的 max 等级在简单任务上即可能耗尽 128K 输出预算，提示高 effort 设置未必稳定，选型时需重新验证成本与可靠性。

**「可关注」** 可关注：GPT-6 Luna 以 $0.10/$0.50 成为 OpenAI 最便宜的模型之一，而 Opus 5.5 的 max 等级在简单 SVG 任务上即触发 128K 输出上限；工程上需把 effort 当作成本与稳定性风险来管理，而非默认拉满。

**标签**: `#coding-agent`, `#eval`

---

<a id="item-agent-engineer-5"></a>
### [simonw released 0.29 in simonw/llm-anthropic](https://github.com/simonw/llm-anthropic/releases/tag/0.29) ⭐️ 6.3/10

simonw/llm-anthropic 0.29 adds support for the Claude Opus 5.5 model via \`llm -m claude-opus-5.5\`.

github · simonw · 9月22日 17:14

**标签**: `#harness`, `#coding-agent`

---

<a id="item-agent-engineer-6"></a>
### [GPT-6 Sol and Luna](https://openai.com/index/introducing-gpt-6-sol-and-luna/) ⭐️ 5.5/10

HN thread reacting to the GPT-6 Sol and Luna announcement, focusing on pricing, subjective coding-agent experience, and usage-limit math.

hackernews · OfficialTurkey · 9月22日 18:00 · [社区讨论](https://news.ycombinator.com/item?id=49805509)

**标签**: `#coding-agent`, `#observability`, `#harness`

---

## AI 日报

<a id="item-ai-daily-1"></a>
### [GPT-6 Sol 和 Luna 发布](https://openai.com/index/introducing-gpt-6-sol-and-luna) ⭐️ 9.8/10

OpenAI 于 2026 年 9 月 22 日发布 GPT-6 Sol 和 Luna 两款模型。官方称其将前沿智能带入日常工作，并在能力与成本之间提供不同平衡。目前公开信息有限，未披露具体参数、基准测试或定价细节。

rss · OpenAI Blog · 9月22日 18:00

**「可关注」** 可关注：两款模型在能力与成本上给出不同取舍，可按实际场景选择。

**标签**: `#model`, `#lab`, `#product`

---

<a id="item-ai-daily-2"></a>
### [GPT-6 优化提示缓存](https://openai.com/index/better-prompt-caching-for-gpt-6) ⭐️ 9.3/10

OpenAI 发布 GPT-6 提示缓存改进，包含更高缓存命中率、新诊断工具、显式断点，以及降低延迟与成本的控件。官方称这些改动可减少重复请求开销。目前未公布具体命中率数字或延迟降幅。

rss · OpenAI Blog · 9月22日 21:00

**「为什么重要」** 对 coding agent 与 harness 场景，提示缓存直接影响长上下文任务的延迟与调用成本。

**「可关注」** 可关注：GPT-6 新增显式断点与诊断工具，可在长会话中更精细地控制缓存行为。

**标签**: `#model`, `#lab`, `#product`

---

<a id="item-ai-daily-3"></a>
### [Parallel 用 GPT-6 Astra 减半](https://openai.com/index/parallel-cuts-time-and-cost-with-astra) ⭐️ 5.8/10

OpenAI 官方博客发布客户案例。Parallel 的智能体使用 GPT-6 Astra 研究和合成劳动力市场数据，耗时与成本较此前模型均减半。官方未披露对比基线、任务规模及测试条件。该案例来自 OpenAI 一手材料，但属于客户宣传，尚无独立验证。

rss · OpenAI Blog · 9月22日 12:00

**「为什么重要」** 对 coding agent 与 harness 开发者而言，该案例显示 GPT-6 Astra 可能降低多步检索与合成任务的延迟和 token 成本。若效果成立，智能体执行长流程数据研究时，单位任务开销有望减半。但目前仅有一个客户案例，不足以推断普遍性能。

**「可关注」** GPT-6 Astra 在劳动力市场数据研究中将耗时与成本减半，但需等待独立基准测试验证。

**标签**: `#model`, `#lab`, `#industry`

---

## AI 羊毛

<a id="item-ai-deals-1"></a>
### [OpenRouter Batch API：批量请求半价](https://openrouter.ai/blog/announcements/batch-api/) ⭐️ 8.0/10

OpenRouter 推出 Batch API，将请求捆绑成批量任务后按半价计费。开发者可通过打包请求降低推理成本。官方公告未提及适用模型、额度上限或截止时间。

rss · HN Free API / Credits · 9月22日 16:42

**「为什么重要」** 对可排队、非实时的批量推理任务，这能直接减少一半 API 支出。

**「可关注」** OpenRouter Batch API 适合可排队、非交互式的批量推理场景；材料未披露具体模型覆盖与速率限制，接入前需查阅官方文档确认适用范围。

**标签**: `#promo`, `#api`, `#discount`

---

<a id="item-ai-deals-2"></a>
### [产品评论分析 API 注册送 $1 额度](https://bb-product-api-docs.web.app/) ⭐️ 5.0/10

aditya314159 在 Show HN 发布产品评论分析 API，输入品牌与产品名后，抓取 Amazon、TikTok、Reddit、YouTube、Instagram、Walmart 等平台的评论，提取跨评论重复出现的正面情绪并附原文引用与链接。单次分析收费 $0.99，注册创建 API key 赠送 $1 额度，首次分析免费。目前仅支持消费品，单产品分析耗时数分钟。

rss · HN Free API / Credits · 9月22日 15:45

**「为什么重要」** 对需要零成本验证产品口碑的开发者，$1 注册额度可直接覆盖首次分析，快速拿到跨平台评论证据。

**「可关注」** 可关注：该 API 仅支持消费品且按次计费 $0.99，适合小规模口碑验证；非消费品或高频调用场景需先评估成本与覆盖范围。

**标签**: `#credits`, `#promo`, `#api`, `#free-tier`

---