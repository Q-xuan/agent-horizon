---
layout: default
title: "Horizon Summary: 2026-10-06 (ZH)"
date: 2026-10-06
lang: zh
---

> 从 198 条内容中筛选出 16 条重要资讯。

---

**Harness 架构**
1. [vLLM v0.31.0 发布](#item-harness-arch-1) ⭐️ 8.8/10
2. [Claude Code v2.1.290 发布](#item-harness-arch-2) ⭐️ 8.3/10
3. [Mastra 1.74.0 发布：工具可读完整对话](#item-harness-arch-3) ⭐️ 8.3/10
4. [Mastra 1.73.0 默认错误恢复](#item-harness-arch-4) ⭐️ 8.3/10
5. [Agents Realtime 0.19.0](#item-harness-arch-5) ⭐️ 7.8/10
6. [agents-core 0.19.0 发布](#item-harness-arch-6) ⭐️ 7.3/10
7. [E2B 2.52.1 收紧 502 重试语义](#item-harness-arch-7) ⭐️ 6.8/10

**Agent 工程师日报**
1. [OSWorld-Pro 推出过程化评测](#item-agent-engineer-1) ⭐️ 7.5/10
2. [PluginRSI：递归改进 Agent Harness](#item-agent-engineer-2) ⭐️ 7.5/10
3. [Cowork 转向云端沙箱架构](#item-agent-engineer-3) ⭐️ 6.0/10
4. [HF daily paper: ASCENT: Online Test-Time Training of Long-Horizon Agents via Self-Distillation of Verified Experience](#item-agent-engineer-4) ⭐️ 5.5/10
5. [HF daily paper: CANOPY: Adaptive-Granularity Evidence Compression for Multimodal RAG](#item-agent-engineer-5) ⭐️ 5.5/10

**AI 日报**
1. [ChatGPT 上线新视觉广告格式](#item-ai-daily-1) ⭐️ 9.8/10
2. [OpenAI 说明欧盟文本溯源规则](#item-ai-daily-2) ⭐️ 9.3/10
3. [ReviewBench: An open benchmark for AI code review](#item-ai-daily-3) ⭐️ 8.8/10

**AI 羊毛**
1. [Show HN: Free Public API Lab](#item-ai-deals-1) ⭐️ 5.0/10

---

## Harness 架构

<a id="item-harness-arch-1"></a>
### [vLLM v0.31.0 发布](https://github.com/vllm-project/vllm/releases/tag/v0.31.0) ⭐️ 8.8/10

vLLM v0.31.0 发布，包含 717 个提交、307 位贡献者。核心变更是推理运行时与前缀缓存机制：新增 \`vllm preload\` 权重缓存守护进程，量化后权重在 GPU 显存中跨引擎重启常驻；SWA bounded replay 将滑动窗口 KV 排除在前缀缓存之外。调度层新增 \`--max-num-active-seqs\` 独立限制 RUNNING 准入，等待队列优先调度已持有 KV block 的请求。安全侧默认拒绝 per-request \`mm\_processor\_kwargs\`，需显式 \`--trust-request-mm-kwargs\`。

github · khluu · 10月5日 06:44

**「设计要点」** 权重缓存守护进程通过独立 CLI 管理 GPU 显存中的量化权重，配合 CRIU 快照可恢复已初始化的 TP1 引擎。SWA bounded replay 在块哈希与缓存键中区分滑动窗口 KV，避免其污染前缀缓存。

**「改了什么」** 新增 \`vllm preload\` 守护进程与 \`vllm snapshot create/restore\` 实验性快照；\`--max-num-active-seqs\` 与重排后的等待队列改变 RUNNING 准入逻辑；\`tokenizer\_mode=&quot;slow&quot;\`、AllSpark INT8 W8A16 后端及 \`quantization=&quot;fp8&quot;\` 在线量化被移除，\`--enforce-eager\` 现在同时禁用 JIT kernel warmup。

**标签**: `#runtime`, `#prefix-cache`, `#tools`

---

<a id="item-harness-arch-2"></a>
### [Claude Code v2.1.290 发布](https://github.com/anthropics/claude-code/releases/tag/v2.1.290) ⭐️ 8.3/10

Claude Code v2.1.290 发布，扩展插件钩子与权限模型。mod 的 \`turn.step\` 钩子新增 \`serverToolUses\`，可读取 API 自行执行的工具调用；\`tool.check\` 事件新增 \`agentId\` 与 \`ceiling\`，用于区分子代理权限检查并获取组织要求的审批级别。CLI 增加 \`claude attach &lt;name&gt;\` 和 \`claude logs &lt;name&gt;\`，支持用会话名片段代替 ID。同时修复代理 beta 头、长会话图片卡死、计划任务恢复失效等大量问题。

github · ashwin-ant · 10月5日 23:33

**「设计要点」** 权限层现在能区分主会话与子代理的检查，并通过 \`ceiling\` 暴露组织级审批上限；插件钩子可观测 API 侧服务端工具调用，扩展了 harness 对工具执行面的可见性。

**「改了什么」** 相比前版，v2.1.290 把权限检查细化到子代理维度，插件钩子可读取服务端工具调用与组织审批上限；CLI 会话管理支持名称片段匹配，并新增 Managed Agents 模板引导命令。

**标签**: `#tools`, `#permissions`, `#subagents`, `#runtime`

---

<a id="item-harness-arch-3"></a>
### [Mastra 1.74.0 发布：工具可读完整对话](https://github.com/mastra-ai/mastra/releases/tag/%40mastra/core%401.74.0) ⭐️ 8.3/10

Mastra 1.74.0 发布。工具执行上下文新增 \`context.agent.getMessages\(\)\`，标准与 durable agent loop 均可读取当前对话，包括记忆消息和本轮回复，原输入字段 \`messages\` 保持不变。observational memory 历史搜索支持 \`groupId\` 过滤、\`sortDirection\` 排序和 \`recordId\` 直查，适配器通过 \`supportsObservationalMemoryHistorySearch\` 声明能力。Convex 需重新部署 server functions 才能启用新过滤。

github · PaulieScanlon · 10月5日 09:31

**「设计要点」** 工具层通过 getter 暴露消息列表，反映删除操作，但不包含仅用于 provider prompt 的瞬时变换，返回值只读。记忆检索支持围绕命中 \`groupId\` 前后分页，覆盖被 reflection 压缩的组和尚未激活的缓冲组，无需重建索引。

**「改了什么」** 工具上下文从只读输入 \`messages\` 扩展为可调用 \`agent.getMessages\(\)\` 获取完整会话；observational memory 历史搜索新增分组过滤、排序和记录直查，并支持围绕命中分组前后分页。

**标签**: `#runtime`, `#tools`, `#memory`

---

<a id="item-harness-arch-4"></a>
### [Mastra 1.73.0 默认错误恢复](https://github.com/mastra-ai/mastra/releases/tag/%40mastra/core%401.73.0) ⭐️ 8.3/10

Mastra 1.73.0 默认启用三个错误处理器（\`ProviderHistoryCompat\`、\`PrefillErrorHandler\`、\`StreamErrorRetryProcessor\`），在重试前修复历史与提示词。新增 \`tool-call-resumed\` 流式块，客户端可在 \`tool-result\` 前标记暂停或审批门控的工具调用已恢复。\`@mastra/connect\` 加入 Google Docs/Drive/Sheets 工具集，平台代理支持 \`responseType: &\#x27;arraybuffer&\#x27;\` 返回二进制响应。破坏性变更：durable stream 不再单独发送 \`tripwire\` 块，改用 \`finishReason === &\#x27;tripwire&\#x27;\` 与 \`output.tripwire\`。

github · PaulieScanlon · 10月5日 09:30

**「设计要点」** 错误处理器按“先修复再重试”排序，默认只重试瞬时故障，确定性错误立即抛出；\`errorProcessorDefaults: false\` 是唯一关闭默认的开关。\`tool-call-resumed\` 经 \`@mastra/ai-sdk\` 与 \`@mastra/react\` 的 \`useChat\` 贯通，子代理经委派暂停时也能正确清理待处理状态。

**「改了什么」** Agent 无需配置即可从瞬时 provider 故障、assistant-prefill 拒绝与 provider 历史不兼容中恢复；\`ProviderHistoryCompat\` 现在也会在出站前修复提示词。Durable/evented 执行修复了输出处理器重试、恢复工具并行执行、事件步骤重复运行（心跳+租约防护）等问题，大线程历史加载从平方级降为线性。

**标签**: `#runtime`, `#tools`, `#permissions`

---

<a id="item-harness-arch-5"></a>
### [Agents Realtime 0.19.0](https://github.com/openai/openai-agents-js/releases/tag/%40openai/agents-realtime%400.19.0) ⭐️ 7.8/10

OpenAI Agents JS 发布 Realtime 0.19.0。核心修复条件工具审批：将审批绑定到隔离的规范化执行输入，持久审批恢复时重新评估当前策略，并拒绝不可复制的规范化值。同时修复 Realtime 音频缓冲区编码栈溢出、updateHistory 场景下的对话顺序错乱，以及切换到无工具 agent 时的陈旧工具清理。包元数据生成切换到原生 Node.js TypeScript 支持。

github · github-actions\[bot\] · 10月5日 16:47

**「设计要点」** 工具权限层引入规范化执行输入隔离，策略在 durable approval 恢复时重新求值，避免过期审批状态。Realtime 运行时调整音频缓冲区编码路径，防止大缓冲区触发栈溢出；对话状态在 updateHistory 插入或更正项目时保持顺序。

**「改了什么」** 条件工具审批改为绑定隔离的规范化执行输入，持久审批恢复时重新评估策略；默认函数工具和 Realtime 审批解析失败默认脱敏，敏感错误追踪需显式调用策略。Realtime 侧修复音频缓冲区栈溢出、updateHistory 对话顺序、无工具 agent 切换时的工具清理，以及自动响应请求合并后的任务释放。

**标签**: `#runtime`, `#tools`, `#permissions`

---

<a id="item-harness-arch-6"></a>
### [agents-core 0.19.0 发布](https://github.com/openai/openai-agents-js/releases/tag/%40openai/agents-core%400.19.0) ⭐️ 7.3/10

OpenAI Agents JS 核心包发布 0.19.0，聚焦流式回调背压、检查点校验、MCP 调用归属与条件工具审批隔离。默认将 agent 工具流式待处理事件限制为 1024，可通过 onStreamMaxPendingEvents 调整或传 null 恢复无限制。启动的检查点若缺少初始输入验证完成证据会被拒绝，需带原始输入与上下文重启。恢复的 MCP 调用绑定到原始接收者，无接收者来源的历史挂起函数调用要求重新运行。条件工具审批绑定到隔离的规范化执行输入，并在持久审批恢复时重新评估当前策略。

github · github-actions\[bot\] · 10月5日 16:47

**「设计要点」** 运行时为流式工具回调引入 1024 条待处理事件上限，防止无界缓冲。检查点与 MCP 恢复路径加强来源校验，审批恢复时重新执行策略而非沿用旧决策。

**「改了什么」** 新增 onStreamMaxPendingEvents 控制流式缓冲上限；检查点恢复强制校验初始输入完成证据；MCP 恢复调用绑定原始接收者；条件审批在 core 与 Realtime 中隔离规范化输入并重评策略；默认脱敏函数工具与 Realtime 审批解析失败的错误追踪。

**标签**: `#runtime`, `#tools`, `#mcp`, `#permissions`

---

<a id="item-harness-arch-7"></a>
### [E2B 2.52.1 收紧 502 重试语义](https://github.com/e2b-dev/E2B/releases/tag/e2b%402.52.1) ⭐️ 6.8/10

E2B 2.52.1 补丁发布。核心修正是 \`.dockerignore\` 过滤对齐 BuildKit，以及 502 重试语义收紧：sandbox 创建、fork、snapshot 等资源创建型 POST 在收到 502 后直接返回，不再自动重试，防止网关已处理请求却响应超时造成的重复创建。503 仍照常重试。Secret 更新接口在 502 或连接中断后不再重放。

github · github-actions\[bot\] · 10月5日 12:41

**「设计要点」** 资源创建型操作不可盲目重放。网关 502 可能掩盖 API 已成功执行的事实，重试会复制沙箱或快照。Secret 更新为追加写，重放即产生额外版本，因此也排除在重试之外。

**「改了什么」** \`.dockerignore\` 匹配规则调整：\`\*\*\` 后接字面量可在任意深度命中；仅匹配父目录的否定模式不再重新包含文件；JS SDK 的 \`?\` 和括号表达式可匹配 BMP 外字符。502 重试范围收缩至可安全重放的操作。JS SDK 将 \`WatchHandle.stop\(\)\` 视为干净结束，\`onExit\` 不再抛 \`TimeoutError\`。

**标签**: `#sandbox`, `#runtime`

---

## Agent 工程师日报

<a id="item-agent-engineer-1"></a>
### [OSWorld-Pro 推出过程化评测](https://huggingface.co/papers/2609.24890) ⭐️ 7.5/10

Hugging Face Daily Papers 收录 OSWorld-Pro。该基准面向 Computer-Use Agents（CUAs），包含 300 余个任务、2,800 余个子目标，并基于 67,000 条人工标注，用与人类对齐的 LLM-Judges 评估子目标完成度。相比 OSWorld 只验终态交付物，OSWorld-Pro 把评测下沉到执行过程。目前仅见摘要，完整结果与代码发布情况未确认。

rss · Hugging Face Daily Papers · 10月6日 00:00

**「为什么重要」** CUAs 过去常用功能验证器检查最终产物，分不清键盘输入出错和图形界面点击出错，改进方向也就不同。OSWorld-Pro 将失败定位到子目标层，给 eval 工具链更细的观测粒度。已发生的是基准提出，尚未证实的是对实际调试或训练的收益。

**「可关注」** 可关注：为 CUAs 搭过程化 eval 时，OSWorld-Pro 的子目标切分与 67,000 条人工标注规模可作参照；但代码与完整结果未出，暂不宜接入生产链路。

**标签**: `#eval`, `#coding-agent`, `#observability`

---

<a id="item-agent-engineer-2"></a>
### [PluginRSI：递归改进 Agent Harness](https://huggingface.co/papers/2609.32423) ⭐️ 7.5/10

PluginRSI 把 Agent Harness 拆成原子化插件，围绕插件组织演化。单个插件独立改进，汇入共享库，每次迭代再重组成新 Harness。论文称其在软件工程、命令行交互和问答任务上优于现有 Harness 优化方法，且迁移到其他求解模型时无需重新优化仍保持优势。该论文 2026-10-06 见于 Hugging Face Daily Papers，目前仅 1 个 upvote，属研究贡献而非主流产品变更。

rss · Hugging Face Daily Papers · 10月6日 00:00

**「为什么重要」** 对做 Harness、评测和工具链设计的工程师，它给出了一条把机制隔离、复用并跨模型迁移的具体路径。论文结论尚未在更大范围复现，实际收益仍待验证。

**「可关注」** 可关注：将 Harness 机制原子化为可独立改进、共享和重组的插件，可能降低跨任务与跨模型迁移的优化成本。

**标签**: `#harness`, `#eval`, `#orchestration`, `#coding-agent`

---

<a id="item-agent-engineer-3"></a>
### [Cowork 转向云端沙箱架构](https://simonwillison.net/2026/Oct/5/felix-rieseberg/) ⭐️ 6.0/10

Felix Rieseberg 称 Cowork 正把工具执行从本地 Anthropic VM 迁往每会话独立的云端沙箱。旧方案在本地运行 VM，占用磁盘与电量，拖慢性能，且合上笔记本会中断工作。新方案将模型推理与 VM 均置于云端，会话间不共享状态；VM 需要访问用户设备文件时，由桌面应用代理该文件访问工具调用。该描述来自 Simon Willison 转载的社交媒体引述，并非官方工程博客，细节有限。

rss · Simon Willison · 10月5日 23:56

**「为什么重要」** 对 agent harness 设计者而言，这呈现了工具执行从本地虚拟机上云的一种具体路径，以及桌面端如何转为文件访问代理。手机使用、任务续跑、省电等收益仍是产品方说法，尚无第三方验证。

**「可关注」** 可关注：执行环境整体迁往云端沙箱后，本地客户端收缩为受控的文件访问代理，工具调用路由与权限边界需要重新设计。

**标签**: `#harness`, `#coding-agent`, `#permissions`, `#orchestration`

---

<a id="item-agent-engineer-4"></a>
### [HF daily paper: ASCENT: Online Test-Time Training of Long-Horizon Agents via Self-Distillation of Verified Experience](https://huggingface.co/papers/2610.05303) ⭐️ 5.5/10

A paper proposes ASCENT, an online test-time training method that updates LLM agent weights via self-distillation of verified execution trajectories during deployment.

rss · Hugging Face Daily Papers · 10月6日 00:00

**标签**: `#harness`, `#eval`, `#memory`

---

<a id="item-agent-engineer-5"></a>
### [HF daily paper: CANOPY: Adaptive-Granularity Evidence Compression for Multimodal RAG](https://huggingface.co/papers/2610.00923) ⭐️ 5.5/10

Proposes CANOPY, a hierarchical framework that adaptively compresses retrieved multimodal evidence by scoring regions against the query to balance context retention and granularity.

rss · Hugging Face Daily Papers · 10月6日 00:00

**标签**: `#rag`, `#multimodal`, `#context-compression`

---

## AI 日报

<a id="item-ai-daily-1"></a>
### [ChatGPT 上线新视觉广告格式](https://openai.com/index/new-chatgpt-ads-format-and-measurement) ⭐️ 9.8/10

OpenAI 在 ChatGPT 中引入视觉广告格式，并扩展测量工具、归因合作伙伴和品牌适配能力。该更新来自 OpenAI 官方博客，面向广告主。材料未提供具体上线范围、计费方式或早期效果数据。

rss · OpenAI Blog · 10月5日 10:00

**「为什么重要」** OpenAI 将广告产品扩展到 ChatGPT 对话界面，并同步完善测量与归因体系，这是主流 AI 应用商业化路径的实质更新。

**「可关注」** 可关注：新广告格式配套扩展了测量工具、归因合作伙伴和品牌适配能力，广告效果评估链条有所延长。

**标签**: `#product`, `#lab`, `#industry`, `#policy`

---

<a id="item-ai-daily-2"></a>
### [OpenAI 说明欧盟文本溯源规则](https://openai.com/index/eu-text-provenance) ⭐️ 9.3/10

OpenAI 发布说明，阐述在欧盟文本溯源规则下的水印方案。官方介绍了水印的适用范围、检测机制，并说明访问权限将优先向研究人员开放。目前仅披露框架性信息，未给出具体技术细节或上线时间。

rss · OpenAI Blog · 10月5日 15:00

**「为什么重要」** 欧盟对 AI 生成文本提出溯源要求，OpenAI 作为主要实验室给出官方应对方案，为行业合规提供参考。水印与检测机制的具体设计，关系着文本溯源规则的落地路径。

**「可关注」** OpenAI 说明访问权限将优先向研究人员开放，后续技术细节与开放范围值得跟踪。

**标签**: `#policy`, `#lab`, `#industry`

---

<a id="item-ai-daily-3"></a>
### [ReviewBench: An open benchmark for AI code review](https://github.blog/ai-and-ml/github-copilot/reviewbench-an-open-benchmark-for-ai-code-review/) ⭐️ 8.8/10

GitHub launches ReviewBench, an open benchmark for evaluating AI code review agents built on representative pull requests with multi-source ground truth and production-aligned metrics.

rss · GitHub Blog · 10月5日 15:59

**标签**: `#eval`, `#open-source`, `#product`, `#lab`

---

## AI 羊毛

<a id="item-ai-deals-1"></a>
### [Show HN: Free Public API Lab](https://sondahub.com/) ⭐️ 5.0/10

Free no-account public API playground supporting REST, OData, MCP, FHIR, SOAP, and Socket.IO, available now on sondahub.com and GitHub.

rss · HN Free API / Credits · 10月5日 20:58

**标签**: `#api`, `#free-tier`, `#limited-free`

---