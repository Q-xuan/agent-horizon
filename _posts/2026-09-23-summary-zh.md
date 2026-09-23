---
layout: default
title: "Horizon Summary: 2026-09-23 (ZH)"
date: 2026-09-23
lang: zh
---

> 从 233 条内容中筛选出 22 条重要资讯。

---

**Harness 架构**
1. [cline/cline released sdk/sdk/v0.0.85](#item-harness-arch-1) ⭐️ 8.8/10
2. [Cline 桌面版 v0.0.33 发布](#item-harness-arch-2) ⭐️ 8.8/10
3. [vLLM v0.30.0 发布](#item-harness-arch-3) ⭐️ 8.8/10
4. [Cline SDK v0.0.84 发布](#item-harness-arch-4) ⭐️ 7.8/10
5. [2.1.280](#item-harness-arch-5) ⭐️ 7.8/10
6. [Cline v4.1.20 发布](#item-harness-arch-6) ⭐️ 6.8/10
7. [Cline CLI v3.0.64 发布](#item-harness-arch-7) ⭐️ 6.8/10
8. [GitHub trending: langchain-ai/agents-from-scratch](#item-harness-arch-8) ⭐️ 5.0/10

**Agent 工程师日报**
1. [GPT-6 Sol 与 Luna 发布](#item-agent-engineer-1) ⭐️ 8.0/10
2. [RRSI 约束 harness 递归自我改进](#item-agent-engineer-2) ⭐️ 7.5/10
3. [Claude Opus 5.5 发布，价格下调](#item-agent-engineer-3) ⭐️ 7.0/10
4. [llm 0.36 发布：插件可声明单轮模型](#item-agent-engineer-4) ⭐️ 6.8/10
5. [Claude Opus 5.5 与 GPT-6 掀价格战](#item-agent-engineer-5) ⭐️ 6.5/10
6. [RULER：SVG 生成 rubric 奖励](#item-agent-engineer-6) ⭐️ 6.0/10
7. [AIDE^2：AI agent 递归自我改进](#item-agent-engineer-7) ⭐️ 6.0/10
8. [D-RAC：PDF 归一化与多模态分块](#item-agent-engineer-8) ⭐️ 6.0/10
9. [llm 0.36 支持单轮模型插件](#item-agent-engineer-9) ⭐️ 5.5/10
10. [llm-anthropic 0.29 支持 Claude Opus 5.5](#item-agent-engineer-10) ⭐️ 5.5/10
11. [llm-typesafe 0.1a0 发布](#item-agent-engineer-11) ⭐️ 5.5/10

**AI 日报**
1. [Introducing GPT-6 Sol and Luna](#item-ai-daily-1) ⭐️ 9.8/10
2. [Parallel cut research time and cost in half with GPT‑6 Astra](#item-ai-daily-2) ⭐️ 8.3/10

**AI 羊毛**
1. [OpenRouter Batch 半价推理](#item-ai-deals-1) ⭐️ 7.0/10

---

## Harness 架构

<a id="item-harness-arch-1"></a>
### [cline/cline released sdk/sdk/v0.0.85](https://github.com/cline/cline/releases/tag/sdk/sdk/v0.0.85) ⭐️ 8.8/10

Cline SDK v0.0.85 improves runtime resilience by retrying turns that exhaust output tokens without tool calls and dynamically scaling default output allowances based on model limits.

github · github-actions\[bot\] · 9月22日 08:13

**标签**: `#runtime`, `#tools`, `#planning`

---

<a id="item-harness-arch-2"></a>
### [Cline 桌面版 v0.0.33 发布](https://github.com/cline/cline/releases/tag/desktop-v0.0.33) ⭐️ 8.8/10

Cline 桌面版 v0.0.33 发布。新任务可跑在独立 git worktree 中：欢迎屏的 Work in 开关选 Worktree 后，新线程首条 prompt 会从当前分支切出 cline/&lt;id&gt;，在 ~/.cline/worktrees/ 下建工作树并执行，仅新线程生效。长会话自动压缩修复：桌面 sidecar 过去只勾选 checkpoint、从未启用 compaction，90% 触发条件没装上，现补齐。另修 Windows 重复启动、登录早期失败、SSH 新会话启动等问题。

github · github-actions\[bot\] · 9月22日 09:07

**「设计要点」** 任务隔离靠 git worktree：分支命名 cline/&lt;id&gt;，工作树落在 ~/.cline/worktrees/，删除任务即清理分支与工作树，除非其他会话仍占用。压缩链路在 core 自四月起改为 opt-in，桌面 sidecar 漏配 compaction，导致长会话只 checkpoint 不压缩；本次同时让 summarizer 跟随会话当前凭证与模型，避免中途回退到截断。

**「改了什么」** 相对上一版，新增 worktree 任务隔离与长会话自动压缩；修复 Windows 多实例、登录竞态、SSH 新会话、删除当前会话视图、历史删除不生效等运行时问题。模型目录从 203 提供商、6,079 模型扩到 209、6,237，Kimi For Coding 拆成 kimi.com 与 kimi.ai。

**标签**: `#sandbox`, `#runtime`, `#memory`

---

<a id="item-harness-arch-3"></a>
### [vLLM v0.30.0 发布](https://github.com/vllm-project/vllm/releases/tag/v0.30.0) ⭐️ 8.8/10

vLLM v0.30.0 发布，合并 762 个提交。新增 DeepSeek-V4.1-Flash、GLM-5.3-Flash 等模型后端，DeepSeek-V4.1-Flash 在 SM100 上经 FlashMLA V4.1 将全部 KV 存为 MXFP8。引入 Fast Start：per-GPU 权重缓存守护进程持有量化、TP 分片后的权重，引擎重启时通过 CUDA IPC 映射，用 \`--load-format ipc\_cache\` 替代磁盘加载，覆盖 FP4 检查点和多节点 TP。新增 HiSparse 主机内存层，显存压力下将稀疏 MLA 解码的 KV 页溢出到 pinned host memory，经 \`HiSparseConnector\` 启用。

github · khluu · 9月22日 05:20

**「设计要点」** Fast Start 以 per-GPU 守护进程缓存量化、TP 分片权重，重启时经 CUDA IPC 映射，省去磁盘加载；HiSparse 为稀疏 MLA 解码增加 host-resident KV 层，显存不足时溢出到 pinned host memory，由 \`HiSparseConnector\` 控制。

**「改了什么」** 权重加载新增 \`--load-format ipc\_cache\` 持久化路径，稀疏 MLA 解码新增 HiSparse 主机内存层；Model Runner V2 在 H200 上把 CUDA graph 捕获从 12s 降到 2s、引擎初始化从 28.9s 降到 8.2s。Breaking changes 包括 scale-out 端点改为 \`--enable-scale-out\` 显式开启，移除 GPTQ \`g\_idx\`，弃用 \`all\` Mamba 缓存模式。

**标签**: `#runtime`, `#prefix-cache`, `#memory`

---

<a id="item-harness-arch-4"></a>
### [Cline SDK v0.0.84 发布](https://github.com/cline/cline/releases/tag/sdk/sdk/v0.0.84) ⭐️ 7.8/10

Cline SDK v0.0.84 修复 feature-flag 并发轮询竞争，新增 run-start hook 上下文注入。Compaction 改用 provider 上报的 input-token 数触发，summarizer 默认输出预算从 4096 提到 8192。Windows 下新增 \`disableCurrentDirectoryExecutableSearch\(\)\`，阻止工作区内被植入的程序顶替真实可执行文件。Subagent 工具调用默认并发执行，且不再继承父会话的审批策略。

github · github-actions\[bot\] · 9月22日 03:26

**「设计要点」** Run-start hook 通过 \`AgentRunStartResult\` 的 \`appendContext\` 通道注入上下文，运行时将其收敛为单条 \`&lt;hook\_context source=&quot;RunStart&quot;&gt;\` 消息置于输入消息之后；恢复会话中若尾部有未解析 \`tool\_use\`，则插入到该调用之前以保持配对相邻。Hook 文件与子进程层新增 \`blockingRunStartHooks\` 选项，默认仍为 fire-and-forget，开启后阻塞 hook 在子进程退出后的宽限期结束并丢弃 stdio 管道。

**「改了什么」** Feature-flag 轮询共享 in-flight 请求，失败可传播重试，切换账号不再等待前一账号请求。Compaction 触发条件加入 \`max\(estimate, actual\)\`，保留字符估算作为下限。配置型 subagent 的审批回调与父会话解耦，避免并发子代理争用同一终端审批。仅以磁盘 manifest 形式存在的会话现在可被真正删除。\`@cline/shared\` 导出 rules-path 解析器，覆盖 \`.clinerules\`、\`.cline/rules\` 及 OneDrive 重定向的 Documents 全局规则路径。

**标签**: `#runtime`, `#tools`, `#permissions`

---

<a id="item-harness-arch-5"></a>
### [2.1.280](https://code.claude.com/docs/en/changelog#2-1-280) ⭐️ 7.8/10

Claude Code 2.1.280 adds an MCP description length limit, fixes symlink write permission bypasses, and expands OpenTelemetry hook telemetry.

rss · Claude Code Changelog · 9月22日 16:48

**标签**: `#permissions`, `#sandbox`, `#tools`, `#mcp`, `#eval`

---

<a id="item-harness-arch-6"></a>
### [Cline v4.1.20 发布](https://github.com/cline/cline/releases/tag/v4.1.20) ⭐️ 6.8/10

Cline v4.1.20 调整子代理执行与输出预算。同一步内派生的子代理现在并行执行工具调用，有顺序依赖的工具仍串行，父代理等所有结果返回后再进入下一轮。默认输出预算改为模型声明输出上限的 30%，与固定 32,000 tokens 取大者；声明上限低于约 107k tokens 的模型不受影响。模型目录从 203 个提供商、6,079 个模型刷新到 209 个、6,237 个，36 个未固定模型的提供商默认模型发生变更。

github · github-actions\[bot\] · 9月22日 20:45

**「设计要点」** 同步子代理的工具调用并行调度，顺序依赖工具仍串行，父代理阻塞等待全部结果；默认输出预算按模型声明上限的 30% 与 32,000 tokens 取大。钩子注入的上下文以 \`&lt;hook\_context&gt;\` 块随首轮请求下发，不渲染到对话记录。

**「改了什么」** 子代理同一步内的工具调用从串行改为并行，默认输出预算从固定 32,000 tokens 改为按模型上限动态缩放。修复钩子上下文注入丢失、Retry 清空未发送输入、后台命令输出不流式、规则面板漏载、任务删除不生效、压缩回退截断、输出超限结束任务；自定义子代理在委派获批后不再逐条请求工具批准。

**标签**: `#runtime`, `#subagents`, `#tools`

---

<a id="item-harness-arch-7"></a>
### [Cline CLI v3.0.64 发布](https://github.com/cline/cline/releases/tag/cli-v3.0.64) ⭐️ 6.8/10

Cline CLI v3.0.64 修复模型回合在工具调用前耗尽输出 token 导致运行中断的问题，现在最多重试三次并提示拆分工作。大上下文模型的默认输出预算从固定 32,000 tokens 改为模型上限的 30%，取较大者，约 107k 以下模型不受影响。模型目录从 6,188 个增至 6,237 个，覆盖 209 个 provider，10 个 provider 的默认模型发生变更。

github · github-actions\[bot\] · 9月22日 08:25

**「设计要点」** 运行时在模型回合触及输出上限且未发起工具调用时插入重试层，通过提醒控制单回合输出长度。输出预算策略改为按模型上限比例分配，直接影响单回合成本与延迟。

**「改了什么」** 新增输出限制重试机制，大输出模型默认预算改为按上限比例分配，模型目录与 10 个 provider 默认模型刷新。

**标签**: `#runtime`, `#tools`, `#planning`

---

<a id="item-harness-arch-8"></a>
### [GitHub trending: langchain-ai/agents-from-scratch](https://github.com/langchain-ai/agents-from-scratch) ⭐️ 5.0/10

A LangChain educational repository that guides users through building an email assistant agent from scratch, covering evaluation, human-in-the-loop, and memory with accompanying code.

rss · GitHub Trending Daily · 9月23日 02:22

**标签**: `#memory`, `#eval`, `#tools`, `#permissions`

---

## Agent 工程师日报

<a id="item-agent-engineer-1"></a>
### [GPT-6 Sol 与 Luna 发布](https://openai.com/index/introducing-gpt-6-sol-and-luna/) ⭐️ 8.0/10

OpenAI 发布 GPT-6 Sol 与 Luna，发布日期为 2026-09-22。Hacker News 讨论集中在定价、agentic coding 体验与订阅用量限制。simonw 称 GPT-6 Luna 价格是 GPT-5.6 Luna 的一半；jeffnash 对比 Claude Code 20x 与 Codex Pro 20x，指出用量限制与计费窗口是选型决定因素，并认为 Codex 20x 计划下 ChatGPT 用量基本无限。官方公告细节未在材料中给出，具体能力与限制仍不确定。

hackernews · OfficialTurkey · 9月22日 18:00 · [社区讨论](https://news.ycombinator.com/item?id=49805509)

**「为什么重要」** 对 coding agent 工程师而言，模型迭代伴随价格与用量限制变化，关系 harness 选型与成本结构。已发生的是新模型发布与社区对价格、限流的反馈，尚未证实的是新模型在 agent 工作流中的实际表现。

**「可关注」** 可关注：GPT-6 Luna 降价与 20x 计划下 ChatGPT 用量宽松，可能改变 Codex 与 Claude Code 在 agent 场景中的成本与限流权衡。

**「评论」** 社区对 GPT-5.6 Sol 的 agent 交互体验有明确好感，认为其沟通方式与工程直觉契合；对新模型定价下降表示欢迎，但对订阅计划的用量限制与计费窗口复杂度仍有不满。

**标签**: `#coding-agent`, `#harness`, `#eval`, `#observability`

---

<a id="item-agent-engineer-2"></a>
### [RRSI 约束 harness 递归自我改进](https://huggingface.co/papers/2609.24972) ⭐️ 7.5/10

Hugging Face Daily Papers 在 2026-09-23 收录论文 RRSI，提出用正则化约束 agent harness 的递归自我改进。现有方法迭代提议并选择 harness 的组件级编辑，实现系统级递归自我改进，但容易记忆训练任务，在分布外基准上收益大幅缩水甚至消失。RRSI 将正则化原则引入 harness 自改进，约束演化候选的生成与选择，以缓解过拟合并提升 OOD 表现。论文具体正则化形式与实验数据在摘要中未完整给出。

rss · Hugging Face Daily Papers · 9月23日 02:22

**「为什么重要」** 对做 coding agent / harness 的工程师，这直接指向自动化 harness 演化的可靠性边界：当系统靠递归编辑自我改进时，如何避免只在训练任务上刷分。论文尚未给出完整实验细节，实际效果待验证。

**「可关注」** 可关注：在 harness 自动化演化流程中引入正则化约束，可能是缓解训练任务过拟合、保住 OOD 基准表现的一条路径。

**标签**: `#harness`, `#eval`, `#memory`, `#orchestration`

---

<a id="item-agent-engineer-3"></a>
### [Claude Opus 5.5 发布，价格下调](https://www.anthropic.com/claude-opus-5-5) ⭐️ 7.0/10

Anthropic 发布 Claude Opus 5.5。每百万 token 价格全线下调：缓存读取 $0.20（原 $0.50），输入 $4（原 $5），输出 $20（原 $25），缓存写入 $5（原 $6.25）。Hacker News 用户实测反映生成质量提升，3D 动画任务显著优于 Opus 5。Anthropic 称其沟通更自然，长会话更易协作。当前信息主要来自社区讨论，暂无第一方工程细节。

hackernews · km144 · 9月22日 16:29 · [社区讨论](https://news.ycombinator.com/item?id=49803892)

**「为什么重要」** 对 coding agent 与 harness 开发者，token 成本直接影响长会话与批量任务预算。缓存读取降价 60%，输出降价 20%，可能改变模型选型的经济性。社区观察到 Opus 5 是 OpenRouter 支出最高的模型，新价格或影响现有工作流成本结构。

**「可关注」** 若现有 agent 流程重度依赖 Opus 系列，可评估 Opus 5.5 在缓存密集型任务上的成本变化；社区实测的性能提升尚属个案，需自行验证。

**「评论」** Hacker News 用户指出 Anthropic 在呼吁“放缓前沿”后立即发布新模型并强调价格优势，存在反差。部分用户认可性能提升，也有用户更倾向 DeepSeek v4.1。

**标签**: `#coding-agent`, `#eval`, `#model-release`

---

<a id="item-agent-engineer-4"></a>
### [llm 0.36 发布：插件可声明单轮模型](https://github.com/simonw/llm/releases/tag/0.36) ⭐️ 6.8/10

simonw/llm 0.36 于 2026-09-22 发布。新增 OpenAI 模型别名 \`gpt-6-sol\` 与 \`gpt-6-luna\`；模型插件可声明 \`supports\_conversation = False\` 限定单轮提示，\`llm chat\` 启动前拒绝这类模型，库在收到助手或工具历史时抛出 \`llm.ConversationNotSupported\`。\`llm logs\` 的 Markdown 输出将推理轨迹包裹在 \`&lt;details&gt;&lt;summary&gt;\` 中。修复涵盖 \`llm logs -t\` 崩溃、\`AsyncResponse.log\_to\_db\(\)\` 报错、\`title\` 字段丢失、\`llm.Prompt\` 默认 \`Options\` 未初始化、异步流未关闭及 SQLite 连接未关闭等问题。

github · simonw · 9月22日 18:48

**「为什么重要」** 把单轮能力边界写进插件声明和 CLI 入口，能在会话开始前拦截不兼容的历史格式，而不是等运行时报错；日志折叠与连接、流关闭修复则直接降低调试与资源泄漏成本。目前材料未提供性能数据或更广泛的兼容性结论，影响主要集中在使用该插件机制与 OpenAI 新别名的场景。

**「可关注」** 可关注：\`supports\_conversation = False\` 为单轮模型提供了显式契约，开发 harness 或模型插件时可在入口处统一拦截多轮历史，避免依赖下游 provider 的偶发错误。

**标签**: `#harness`, `#observability`, `#coding-agent`

---

<a id="item-agent-engineer-5"></a>
### [Claude Opus 5.5 与 GPT-6 掀价格战](https://simonwillison.net/2026/Sep/22/opus-and-sol-and-luna/) ⭐️ 6.5/10

Anthropic 发布 Claude Opus 5.5，OpenAI 一小时后发布 GPT-6 Sol 与 GPT-6 Luna。GPT-6 Luna 定价 $0.10/$0.50（输入/输出，每百万 token），较 GPT-5.6 Luna 再降一半；GPT-6 Sol 定价 $2/$10，与 Grok 4.7 输入价持平。Claude Opus 5.5 从 $5/$25 降至 $4/$20，缓存读取价降 60%。GPT-5.6 已计划 11 月涨价 25%。Simon Willison 测试发现，Opus 5.5 在 max 思考档位下因过度推理耗尽 128,000 输出 token 上限，两次未能返回 SVG 结果，各耗资 $2.56、耗时近 20 分钟。

rss · Simon Willison · 9月22日 23:46

**「为什么重要」** token 单价与缓存价格直接决定 coding agent 的长对话和多轮工具调用成本。Opus 5.5 缓存读取降 60%，对 agentic 场景中 90% 以上输入走缓存的情况尤其关键。同时 max 档位在简单任务上即耗尽输出上限，提示高推理档位在长链路任务中存在不可用风险。

**「可关注」** 可关注：GPT-6 Luna 定价 $0.10/$0.50，是 OpenAI 最便宜的模型之一；Claude Opus 5.5 缓存读取降至 $0.20/M，长上下文 agent 的推理成本结构正在快速变化。但 Opus 5.5 max 档位在简单 SVG 任务上两次撞上 128K 输出上限，高投入推理档位的稳定性仍需实测。

**标签**: `#coding-agent`, `#harness`, `#eval`

---

<a id="item-agent-engineer-6"></a>
### [RULER：SVG 生成 rubric 奖励](https://huggingface.co/papers/2609.25270) ⭐️ 6.0/10

RULER 提出实例感知的 rubric 奖励，用于 SVG 代码生成的强化学习。论文实测，CLIP、Aesthetic 等标量指标从自然图像迁移到矢量内容时效果差，直接用作 RL 奖励会触发奖励黑客；改用多轴 rubric 提示视觉语言裁判后，与人类判断的相关性在跨样本和同指令内均显著更高。RULER 将每条指令转换为实例感知的 rubric 作为奖励信号。该方法给开放生成任务的评估设计提供了参考，但应用领域限于 SVG，且属于研究论文而非生产工程变更。

rss · Hugging Face Daily Papers · 9月23日 00:00

**「为什么重要」** 在缺乏绝对视觉 ground truth 的开放生成任务中，标量指标迁移失败和奖励黑客是通用风险。该论文实证多轴 rubric 与人类判断更相关，为 RL 奖励设计提供了可复用的评估思路。不过，其效果目前仅在 SVG 生成场景验证，尚未证明可推广到其他代码生成领域。

**「可关注」** 可关注：在开放生成任务的 RL 训练中，若标量奖励指标出现奖励黑客，可参考 RULER 用多轴 rubric 替代单一标量分数，并先验证其与人类判断的相关性。

**标签**: `#eval`, `#coding-agent`, `#rl`, `#reward-hacking`

---

<a id="item-agent-engineer-7"></a>
### [AIDE^2：AI agent 递归自我改进](https://huggingface.co/papers/2609.26457) ⭐️ 6.0/10

Hugging Face Daily Papers 于 2026-09-23 收录 AIDE^2 论文。该系统让前沿 AI research agent 修改自身代码，在 AI R&amp;D 任务套件上基准测试改写版本，保留通过的版本，形成递归自我改进循环。论文称这可对抗研发投入边际递减。目前 RSS 摘要仅给出高层概念，未提供可复核的代码、性能数据或架构细节，实际价值需读原文。

rss · Hugging Face Daily Papers · 9月23日 00:00

**「为什么重要」** 该论文触及 coding agent、评测与 harness 的交叉点：agent 自身代码成为优化对象时，评测体系与代码改写机制需共同支撑自我改进。对 agent 工程师而言，这是一手研究线索，但实际收益尚未证实。

**「可关注」** 可关注：AIDE^2 将 agent 自身代码作为优化对象，用基准测试筛选改写并保留通过版本，形成自我改进循环；但 RSS 摘要缺乏可复核的代码、性能数据或架构细节，落地效果需读原文验证。

**标签**: `#coding-agent`, `#eval`, `#harness`

---

<a id="item-agent-engineer-8"></a>
### [D-RAC：PDF 归一化与多模态分块](https://huggingface.co/papers/2609.24220) ⭐️ 6.0/10

Hugging Face 每日论文收录 D-RAC，面向企业 RAG 文档摄取提出新流程。该方法先把任意输入格式统一转为 PDF，再用单次多模态 LLM 调用完成检索感知分块。论文指出，规则抽取和 OCR 会破坏阅读顺序、压平表格、丢失标题层级；而基于纯文本的 agentic 分块则带来高 token 成本与幻觉风险。D-RAC 是 W-RAC 框架向任意文档格式的扩展。目前公开内容仅到摘要层面，缺少可复现基准或生产环境数据。

rss · Hugging Face Daily Papers · 9月23日 02:22

**「为什么重要」** 对企业知识库 RAG 和 agent 文档摄取工具链，D-RAC 提供了一条区别于规则 OCR 和纯文本 agentic 分块的中间路径。但论文尚未给出可复现基准或生产环境验证，实际收益仍待确认。

**「可关注」** 可关注：D-RAC 将文档格式归一化到 PDF 后，用单次多模态 LLM 调用替代多步文本抽取与分块，可能降低 agentic 分块的 token 成本与幻觉风险；不过目前仅停留在摘要描述，缺乏可复现的评测数据。

**标签**: `#harness`, `#eval`, `#rag`

---

<a id="item-agent-engineer-9"></a>
### [llm 0.36 支持单轮模型插件](https://simonwillison.net/2026/Sep/22/llm/) ⭐️ 5.5/10

llm 0.36 发布，新增 OpenAI 模型 \`gpt-6-sol\` 与 \`gpt-6-luna\`。模型插件可声明 \`supports\_conversation = False\`，用于仅接受单轮提示的模型；LLM 在收到助手或工具历史时抛出 \`llm.ConversationNotSupported\`，\`llm chat\` 也会在启动前拒绝。\`llm logs\` 的 Markdown 输出将推理轨迹包裹在 \`&lt;details&gt;&lt;summary&gt;\` 标签中。该版本还包含五位新贡献者的 bug 修复。

rss · Simon Willison · 9月22日 18:48

**「为什么重要」** 对 llm 插件作者和 CLI 用户，单轮模型现在有了明确的会话边界，\`llm chat\` 会在启动前拒绝不支持的会话。首个使用该功能的插件是 \`llm-typesafe\`。新模型 ID 让 GPT-6 Sol 和 GPT-6 Luna 可直接在 llm 中调用。

**「可关注」** 可关注：\`supports\_conversation = False\` 让插件在声明阶段标记单轮模型，\`llm chat\` 会在启动会话前拒绝，插件作者可据此在入口处拦截多轮请求。

**标签**: `#harness`, `#tooling`, `#plugins`, `#openai`

---

<a id="item-agent-engineer-10"></a>
### [llm-anthropic 0.29 支持 Claude Opus 5.5](https://simonwillison.net/2026/Sep/22/llm-anthropic/) ⭐️ 5.5/10

Simon Willison 发布 llm-anthropic 0.29。该插件为 llm CLI 新增 Claude Opus 5.5 支持。调用命令为 \`llm -m claude-opus-5.5 &quot;prompt goes here&quot;\`。发布说明未包含性能数据或架构调整。

rss · Simon Willison · 9月22日 17:14

**「为什么重要」** llm CLI 用户可直接调用 Claude Opus 5.5，无需更换工具链。

**「可关注」** 可关注：llm-anthropic 0.29 为 llm CLI 接入 Claude Opus 5.5，调用命令为 \`llm -m claude-opus-5.5\`。

**标签**: `#harness`, `#llm`, `#anthropic`

---

<a id="item-agent-engineer-11"></a>
### [llm-typesafe 0.1a0 发布](https://simonwillison.net/2026/Sep/22/llm-typesafe/) ⭐️ 5.5/10

Simon Willison 发布 LLM CLI 插件 llm-typesafe 0.1a0，接入 TypeSafe AI 的 Jev 模型。插件支持三类结构化输出：noul 二分类、choice 多选、score 评分。安装后需配置 TypeSafe API key，当前为 alpha 版本。

rss · Simon Willison · 9月22日 15:54

**「为什么重要」** LLM CLI 插件生态再添新模型，展示了 noul、choice、score 三类结构化输出的调用方式。当前为 alpha 版本，影响范围有限。

**「可关注」** 插件以 alpha 状态发布，但已完整覆盖 noul、choice、score 三类结构化输出，演示了 LLM CLI 接入新模型后的分类调用模式。

**标签**: `#harness`, `#eval`, `#coding-agent`

---

## AI 日报

<a id="item-ai-daily-1"></a>
### [Introducing GPT-6 Sol and Luna](https://openai.com/index/introducing-gpt-6-sol-and-luna) ⭐️ 9.8/10

OpenAI officially introduces GPT-6 Sol and Luna, two new models bringing frontier intelligence to everyday work with different balances of capability and cost.

rss · OpenAI Blog · 9月22日 18:00

**标签**: `#model`, `#lab`, `#product`

---

<a id="item-ai-daily-2"></a>
### [Parallel cut research time and cost in half with GPT‑6 Astra](https://openai.com/index/parallel-cuts-time-and-cost-with-astra) ⭐️ 8.3/10

OpenAI’s official blog shares a Parallel case study claiming GPT‑6 Astra cut agent research time and cost in half for labor-market data synthesis.

rss · OpenAI Blog · 9月22日 12:00

**标签**: `#model`, `#lab`, `#product`, `#eval`

---

## AI 羊毛

<a id="item-ai-deals-1"></a>
### [OpenRouter Batch 半价推理](https://openrouter.ai/blog/announcements/batch-api/) ⭐️ 7.0/10

OpenRouter 推出 Batch API，捆绑请求可享半价推理。该接口面向开发者，按批量计费，并非免费额度或积分赠送。材料未说明具体截止时间与使用上限。

rss · HN Free API / Credits · 9月22日 16:42

**「为什么重要」** 对可延迟的批量推理任务，半价直接降低调用成本。

**「可关注」** 可关注：OpenRouter Batch API 对捆绑请求提供半价推理，适合可延迟的批量任务，但材料未说明额度上限与截止时间。

**标签**: `#api`, `#promo`, `#batch`

---