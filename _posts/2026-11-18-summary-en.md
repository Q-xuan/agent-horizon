---
layout: default
title: "Horizon Summary: 2026-11-18 (EN)"
date: 2026-11-18
lang: en
---

> From 186 items, 15 important content pieces were selected

---

**Agent Harness Architecture**
1. [Codex rust-v0.170.0 发布](#item-harness-arch-1) ⭐️ 7.8/10
2. [Goose v1.60.0 发布](#item-harness-arch-2) ⭐️ 7.8/10
3. [pydantic-ai v2.70.0 发布](#item-harness-arch-3) ⭐️ 7.8/10

**AI Agent Engineer**
1. [GPT-6.2 Astra/Sol 发布](#item-agent-engineer-1) ⭐️ 8.0/10
2. [llm 0.38 发布 新增GPT-6.2模型支持](#item-agent-engineer-2) ⭐️ 7.8/10
3. [External Sandbox 模式 三套开源实现发布](#item-agent-engineer-3) ⭐️ 7.0/10
4. [HF 论文：OPD 重塑 LLM ReAct](#item-agent-engineer-4) ⭐️ 7.0/10
5. [Self-Improvement Memory 提出 CRSI 机制](#item-agent-engineer-5) ⭐️ 7.0/10
6. [HF日报：权重空间编程无需Transformer](#item-agent-engineer-6) ⭐️ 6.0/10
7. [Edge0-145B-NVFP4 登 HF 趋势榜](#item-agent-engineer-7) ⭐️ 6.0/10
8. [Martin Fowler 确定性模拟测试介绍](#item-agent-engineer-8) ⭐️ 6.0/10

**AI Daily**
1. [GitHub 发布开源 AHP 跨设备会话协议](#item-ai-daily-1) ⭐️ 8.8/10
2. [GPT-6.2 Astra Sol 发布](#item-ai-daily-2) ⭐️ 7.8/10
3. [OpenAI 发布 ChatGPT Sales 插件](#item-ai-daily-3) ⭐️ 7.8/10
4. [GitHub 微软试点 AI 漏洞修复直报](#item-ai-daily-4) ⭐️ 7.8/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [Codex rust-v0.170.0 发布](https://github.com/openai/codex/releases/tag/rust-v0.170.0) ⭐️ 7.8/10

openai/codex 发布 rust-v0.170.0。本次新增 TUI 实时语音通话的 WebRTC 协商能力，以及 OpenTelemetry HTTP 导出器的自动刷新认证头。实验性支持跨环境同名 MCP 服务器相互隔离。错误修复涵盖 WebSocket 超大请求降级、MCP OAuth 凭证竞态、Cloud 会话重连与恢复轮次保留、Windows 文件替换与运行时注册恢复，以及沙箱权限继承和搜索去重。文档同步更新沙箱权限配置说明。

github · github-actions\[bot\] · Nov 18, 03:40

**「设计要点」** 实验性 MCP 服务器环境隔离通过独立命名空间实现，避免跨环境配置冲突。沙箱权限在会话设置准入时统一规范化，并在线程和子进程中继承保留。运行时重连逻辑在 Cloud 流式传输中断后恢复活跃恢复轮次。Windows 平台修复原子写入和特权错误后的运行时注册对账。

**「改了什么」** 新增 TUI 实时语音通话的 WebRTC 协商能力。MCP 服务器现在支持跨环境独立实例。OAuth 凭证刷新在取消和登出时具备竞态安全。Cloud 对话在临时流中断后自动重连并保留恢复轮次。Windows 沙箱修复文件替换、权限保留和运行时注册恢复问题。

**Tags**: `#mcp`, `#sandbox`, `#runtime`, `#permissions`, `#tools`

---

<a id="item-harness-arch-2"></a>
### [Goose v1.60.0 发布](https://github.com/aaif-goose/goose/releases/tag/v1.60.0) ⭐️ 7.8/10

Goose agent harness 发布 v1.60.0。核心运行时新增 SkillOperation、SlashCommandOperation、Bang command 和 Steering 四种操作类型，同时移除遗留 Skills 扩展（破坏性变更）。新增 Cortecs 与 Onysoft 声明式 provider 支持，GDK 引入可复用轮次限制。此外包含 MCP 运行时与平台扩展分离、移除 chat 模式、MSRV 提升至 1.95.0 等改进，以及大量针对 Ollama、OpenAI、Databricks、Bedrock 等后端的 bug 修复。

github · github-actions\[bot\] · Nov 17, 23:08

**「设计要点」** 本版将平台扩展与 MCP 运行时分离，并把 hook 触发从 GDK API 移入 Goose 自身运行循环，收紧了核心与扩展的边界。新增的四种操作类型均通过状态机注册，使运行时更偏向声明式。

**「改了什么」** 相对上一版，核心运行时新增四种操作类型并移除 Skills 扩展（破坏性变更），新增两个声明式 provider，GDK 支持可复用轮次限制。同时移除 chat 模式与 GDK hook API，MSRV 提升至 1.95.0，并修复多项 provider 适配与安全隐私问题。

**Tags**: `#runtime`, `#tools`

---

<a id="item-harness-arch-3"></a>
### [pydantic-ai v2.70.0 发布](https://github.com/pydantic/pydantic-ai/releases/tag/v2.70.0) ⭐️ 7.8/10

pydantic-ai v2.70.0 发布，包含 harness 两个高危 ReDoS 安全修复。\`strip\_ansi=True\` 时 \`ToolOutputLimits\` 的 ANSI 转义序列正则存在二次方耗时，攻击者可构造含大量未终止转义序列的工具输出阻塞事件循环数十秒至分钟级。默认 \`jwt\` 密钥脱敏正则同样存在二次方回溯，攻击者可 craft 数百 KB 文本触发长时间占用。版本同时新增 \`StreamGuardrail\`、\`PruneToolResults\`、\`ToolSearch\` 等运行时能力，以及 xAI \`service\_tier\` 转发、HuggingFace logprobs 返回等模型层特性。

github · dsfaccini · Nov 17, 22:44

**「设计要点」** harness 在工具输出处理和密钥脱敏环节对不可信输入使用正则表达式，本次修复将 ANSI 与 JWT 匹配改为线性复杂度模式。新引入的 \`StreamGuardrail\` 在流式输出返回调用方前逐段筛查，\`PruneToolResults\` 允许模型用摘要替换工具结果以减少上下文占用。

**「改了什么」** 修复两个高危 ReDoS：\`strip\_ansi=True\` 下的 ANSI 转义序列处理与默认 \`jwt\` 密钥脱敏模式。新增 \`StreamGuardrail\` 流式筛查、\`PruneToolResults\` 工具结果裁剪、\`ToolSearch\` 预搜索延迟、\`SubAgent\(on\_model\_error=\)\` 独立重试、\`ToolDefinition.durable\` 持久化执行，以及 xAI \`service\_tier\` 与 HuggingFace logprobs 支持。

**Tags**: `#runtime`, `#tools`, `#permissions`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [GPT-6.2 Astra/Sol 发布](https://openai.com/index/introducing-gpt-6-2-astra-sol/) ⭐️ 8.0/10

OpenAI发布GPT-6.2 Astra和GPT-6.2 Sol，API标识为gpt-6.2-astra和gpt-6.2-sol，LLM 0.38已率先支持。Astra输入定价$8/MTok、输出$40/MTok，为上一代GPT-6 Astra的80%，缓存输入价格降至$0.40/MTok；Sol维持$2/$10定价，为GPT-5.6 Sol的一半。社区实测显示Astra成本较V6下降约80%（从~$20到~$4），Sol下降约54%（从$2.6到$1.2），token用量减少约20%，工具调用次数也更少。PacBench测试中，Astra得分92、耗时6.6分钟、花费$2.04；Sol得分87、耗时6.3分钟、花费$0.49。也有用户反馈Astra长任务中会提出与当前目标无关的内部实现细节问题，部分办公场景生成质量不及旧模型。

hackernews · jasondavies · Nov 17, 17:46 · [Discussion](https://news.ycombinator.com/item?id=50535230)

**「为什么重要」** 对coding agent和harness团队而言，新模型的价格与token效率优化可直接降低长会话运行成本，公开的PacBench数据也为agent能力选型提供了可对比的参考；但模型在长任务中的异常提问和部分场景的质量波动，需要团队在接入前做针对性验证。

**「可关注」** 可关注：长会话agent场景可优先验证GPT-6.2 Astra的缓存折扣与token效率带来的成本收益，同时测试其长任务中的无关提问是否会影响实际工作流稳定性。

**「评论」** 社区普遍确认了成本与token效率的提升，但存在明显分歧：部分用户认为办公场景生成质量不如旧模型，也有用户反馈Astra在长任务中会出现与当前目标无关的内部细节提问，影响使用体验。

**Tags**: `#coding-agent`, `#eval`, `#orchestration`, `#harness`

---

<a id="item-agent-engineer-2"></a>
### [llm 0.38 发布 新增GPT-6.2模型支持](https://github.com/simonw/llm/releases/tag/0.38) ⭐️ 7.8/10

2026年11月17日，simonw/llm 发布官方 0.38 版本，新增 OpenAI GPT-6.2 Astra、Sol 对应模型 \`gpt-6.2-astra\`、\`gpt-6.2-sol\` 的支持。本次更新修复多项问题：非 OpenAI 相关命令（如 \`llm --version\`、\`llm models list\`）通过延迟导入 \`openai\` 包提升启动速度；修复 \`LLM\_OPENAI\_SHOW\_RESPONSES=1\` 环境下异步 OpenAI 模型调用报 \`Invalid http\_client\` 参数错误的问题，异步请求/响应现已正常记录；修复工具 schema 中因 Pydantic \`title\` 注解清理误删 \`default\`、\`const\`、\`enum\`、\`examples\` 值内 \`title\` 键的问题；模板、片段、函数文件读取优先使用 UTF-8 编码，避免非 ASCII 字符在非 UTF-8 默认编码系统触发 \`UnicodeDecodeError\`；同时修正 \`llm fragments list -q\` 别名匹配逻辑、\`Toolbox\` 子类构造参数记录逻辑；文档同步更新升级说明，提示使用 \`uv tool upgrade llm\`、\`pipx upgrade llm\` 或 \`brew upgrade llm\` 升级会移除通过 \`llm install\` 安装的插件，推荐使用 \`llm install -U llm\` 升级保留插件。变更影响使用 llm CLI 进行 LLM 开发、工具调用、本地模型管理的开发者。

github · simonw · Nov 17, 19:00

**「为什么重要」** 本次更新的多项修复直接作用于 LLM agent 工具调用准确率、异步工作流可观测性、跨平台使用稳定性。其中工具 schema 的 \`title\` 键保留问题修复，可避免模型因缺失参数描述信息产生工具调用偏差；异步日志修复则让异步 agent 工作流的调试能力恢复正常。

**「可关注」** 可关注：若你的工作流依赖 llm 的异步 OpenAI 模型调用或工具 schema 传递，0.38 版本的对应修复可直接消除已知报错和参数描述偏差。

**Tags**: `#harness`, `#coding-agent`, `#observability`

---

<a id="item-agent-engineer-3"></a>
### [External Sandbox 模式 三套开源实现发布](https://simonwillison.net/2026/Nov/17/external-sandboxes-for-coding-agents/) ⭐️ 7.0/10

2026年11月17日，Simon Willison与AI研究实验室Prime Radiant联合推出面向coding agent的外部沙箱模式，核心规则为agent执行的代码在独立沙箱内运行，agent本身驻留在沙箱外，解决prompt注入或操作失误导致主机受损的核心安全痛点。为演示该模式，双方同步发布三套开源沙箱服务器实现：external-sandbox-v86基于v86在WebAssembly中运行Alpine Linux，external-sandbox-container基于Apple Containers运行Alpine Linux，external-sandbox-quicksand基于微软Quicksand库打包QEMU与Alpine Linux。三套实现均提供统一localhost API，可配置Pi、Claude Code、Codex等agent将代码执行请求转发至沙箱，同时支持可选的HTTP/HTTPS白名单代理与凭证替换机制，用于控制agent代码的通信目标、避免向agent泄露密钥。该方案主要面向coding agent的harness开发者、工具链开发者及本地模型使用者。

rss · Simon Willison · Nov 17, 22:52

**「为什么重要」** 该模式直接针对coding agent代码执行环节的安全核心痛点，此前缺乏公开的标准化外部沙箱实现，三套开源方案降低了agent harness与工具链开发者的安全集成门槛。

**「可关注」** 可关注：三套实现均提供统一localhost API，可低改动接入现有Pi、Claude Code、Codex等agent的代码执行链路。

**Tags**: `#coding-agent`, `#harness`, `#permissions`

---

<a id="item-agent-engineer-4"></a>
### [HF 论文：OPD 重塑 LLM ReAct](https://huggingface.co/papers/2611.19244) ⭐️ 7.0/10

2026年11月18日 Hugging Face Daily Papers 收录一篇预印本研究，探究同策略蒸馏（OPD）对 LLM 智能体 ReAct 交互模式的影响，实验覆盖数学、ALFWorld、τ²-bench 三个领域。通用推理监督下，数学领域不必要工具调用占比从 70.4% 降至 14.4%，准确率从 16.7% 提升至 38.0%；代码解释器监督可改善家庭动作与零售查询表现。但 ALFWorld 领域监督会导致 τ²-bench 准确率从 41.5% 跌至 6.6%，同时出现违反用户信息依赖的频繁工具调用。该研究为预印本，相关结论待同行评审验证。

rss · Hugging Face Daily Papers · Nov 18, 00:00

**「为什么重要」** 该研究提供了同策略蒸馏影响 LLM 智能体交互模式的可量化实验证据，正负迁移的具体数值可直接指导智能体训练监督信号选择与跨域评估设计，避免未预期的性能退化。

**「可关注」** 可关注：跨域应用同策略蒸馏时需验证目标域性能，避免严重负迁移；不同监督信号对智能体工具调用模式的改变差异显著，训练时需针对性选择监督来源。

**Tags**: `#eval`, `#coding-agent`, `#orchestration`

---

<a id="item-agent-engineer-5"></a>
### [Self-Improvement Memory 提出 CRSI 机制](https://huggingface.co/papers/2611.18856) ⭐️ 7.0/10

2026-11-18，Hugging Face Daily Papers 收录论文 proposing Self-Improvement Memory \(SIM\)。该机制面向 harness optimizer，按 recurring harness problem 分组编辑历史，记录 rationale、预测与观察结果及评估上下文，以支持 Continual Recursive Self-Improvement \(CRSI\)。实验覆盖四个领域，但原文结果描述截断（仅显示 &quot;achieves hig&quot;），具体性能数字与对比基线未完整提供。该工作针对 benchmark 或 policy model 演化时，harness 优化器难以复用历史编辑决策的问题。

rss · Hugging Face Daily Papers · Nov 18, 00:00

**「为什么重要」** 当前 harness 优化研究多假设固定 benchmark 与 policy model，实际部署中二者常随迭代变化。SIM 提供显式记忆结构，使优化过程可跨兼容环境延续，减少重复试错。

**「可关注」** 可关注：harness 优化器可引入按问题分组的编辑历史记忆，记录 rationale 与评估上下文，以支持跨 benchmark 或 policy model 的持续优化。

**Tags**: `#harness`, `#eval`, `#memory`

---

<a id="item-agent-engineer-6"></a>
### [HF日报：权重空间编程无需Transformer](https://huggingface.co/papers/2611.22055) ⭐️ 6.0/10

2026年11月18日Hugging Face Daily Papers收录的论文显示，3个前沿大模型在极简指导、10个标注样本、沙箱环境的条件下，可手写设计稀疏表架构替代标准Transformer，在多项选择题任务上最高达到54.4%的测试准确率，超过同任务下公开的最优Transformer模型表现，该研究对agent工程工具链的直接影响较窄。

rss · Hugging Face Daily Papers · Nov 18, 00:00

**「为什么重要」** 该研究验证了大模型无需梯度训练即可手写可运行神经架构的可行性，但当前验证场景局限于低样本多项选择题，对coding agent相关架构设计的直接参考价值尚未得到证实。

**「可关注」** 可关注前沿大模型在极低样本下手写可运行架构的能力边界，以及稀疏表结构在轻量eval场景的潜在适配性。

**Tags**: `#eval`, `#architecture`, `#coding-agent`

---

<a id="item-agent-engineer-7"></a>
### [Edge0-145B-NVFP4 登 HF 趋势榜](https://huggingface.co/Edge0/Edge0-145B-NVFP4) ⭐️ 6.0/10

2026-11-18，Hugging Face 趋势榜出现 Edge0/Edge0-145B-NVFP4 模型。该模型为 145B 参数 MoE 架构，采用 4-bit NVFP4 量化并以 GGUF 格式发布，标签指向 coding 与 agent 场景。当前公开信息仅包含 trendingScore=123、likes=496 等基础元数据，未披露技术规格、性能基准或部署细节。对边缘/本地 coding agent 部署有潜在参考价值，但具体能力与限制尚不明确。

rss · Hugging Face Trending Models · Nov 18, 04:37

**「为什么重要」** 该模型以 145B 规模 MoE 搭配 4-bit NVFP4 量化，若技术细节公开，可能为边缘设备运行大型 coding agent 提供新选项。但目前缺乏可验证的性能数据与实现细节，实际影响仍不确定。

**「可关注」** 可关注：GGUF 格式与 NVFP4 量化组合在 145B MoE 模型上的实际内存占用与推理延迟表现，待官方发布技术报告后评估是否纳入边缘 agent 部署候选。

**Tags**: `#coding-agent`, `#moe`, `#edge-inference`, `#gguf`

---

<a id="item-agent-engineer-8"></a>
### [Martin Fowler 确定性模拟测试介绍](https://martinfowler.com/articles/deterministic-simulation-testing.html) ⭐️ 6.0/10

2026年11月17日Martin Fowler发布文章，介绍Unmesh Joshi提出的确定性模拟测试方法，用于解决分布式系统测试中部分故障与实时流量叠加、同故障多次运行产生不同执行轨迹的问题。该方法用单线程执行循环驱动的模拟时钟、网络、存储组件替换真实依赖，支持注入硬故障与模拟网络/磁盘延迟尖峰，且每次执行可完全复现。文章以Tickloom Java实现的quorum键值存储为运行示例，未提供性能数据或生产环境落地验证。

rss · Martin Fowler · Nov 17, 14:33

**「为什么重要」** 该技术为分布式系统测试提供了可复现的故障注入与延迟模拟方案，对提升AI agent评估（eval）的可复现性和测试 harness 的可靠性有参考价值，但文章未提供性能数据或生产环境落地验证。

**「可关注」** 可关注：用单线程驱动的模拟组件替换真实时钟、网络、存储依赖，可提升分布式系统与agent测试场景的执行复现性。

**Tags**: `#eval`, `#harness`, `#orchestration`, `#distributed-systems`

---

## AI Daily

<a id="item-ai-daily-1"></a>
### [GitHub 发布开源 AHP 跨设备会话协议](https://github.blog/engineering/engineering-principles/building-the-agent-host-protocol-for-sessions-that-continue-across-devices/) ⭐️ 8.8/10

GitHub正式发布开源的Agent Host Protocol（AHP）开放标准，用于实现智能体会话跨设备、跨应用的连续性，目前已落地VS Code Copilot及GitHub全产品线，同时向第三方开发者开放集成。该协议不规定智能体具体行为，仅聚焦交互逻辑，核心设计保持最小化，以URI标识的channel为功能单元，要求所有服务端实现root、session、chat三个基础channel，可扩展terminal、MCP、OTel等可选channel。其采用服务端仲裁的reducer式状态模型，客户端通过发送action序列变更状态或触发副作用，天然支持弱网环境下的重连重放，且与React等主流UI框架适配良好。GitHub在适配AHP时基于Copilot SDK新建独立agent host进程，其中VS Code agent host约36.9万行TypeScript，GitHub agent host约30.5万行Rust，替代了原先绑定VS Code窗口生命周期、超40万行TypeScript的Copilot Chat扩展代码。

rss · GitHub Blog · Nov 17, 18:20

**「为什么重要」** 此前各客户端需独立开发智能体集成，无法实现会话跨端延续，AHP作为统一开放标准，降低了第三方将智能体接入自有编辑器、终端、自研工具等场景的门槛，有助于减少智能体生态的碎片化。

**「可关注」** 可关注：AHP的服务端仲裁reducer状态模型，支持弱网下重连重放，且与React等主流UI框架适配，可简化多端智能体应用的开发。

**Tags**: `#open-source`, `#product`, `#industry`

---

<a id="item-ai-daily-2"></a>
### [GPT-6.2 Astra Sol 发布](https://openai.com/index/introducing-gpt-6-2-astra-sol) ⭐️ 7.8/10

OpenAI 官方博客宣布推出 GPT-6.2 Astra 和 Sol 模型。公告称两款模型提升专业输出、编码、计算机使用能力，并改善成本效率，覆盖 ChatGPT Work、Codex 及 API。目前未公开具体基准测试数据、定价细节或正式上线时间。

rss · OpenAI Blog · Nov 17, 17:45

**「为什么重要」** 该公告同时覆盖 ChatGPT Work、Codex 和 API 三条产品线，显示 OpenAI 推进多端能力对齐。对工程团队而言，成本效率声称改善需等待第三方基准验证。

**「可关注」** 可关注：GPT-6.2 Astra 与 Sol 在 Codex 和 API 的成本效率声称改进，但具体幅度未披露。

**Tags**: `#model`, `#lab`, `#product`

---

<a id="item-ai-daily-3"></a>
### [OpenAI 发布 ChatGPT Sales 插件](https://openai.com/index/introducing-chatgpt-for-sales) ⭐️ 7.8/10

OpenAI 发布 ChatGPT Sales 插件，同步推出 30 余款新增及扩展的合作伙伴集成。这些集成覆盖潜在客户研究、销售话术准备和 CRM 数据更新等场景。用户可通过 ChatGPT 直接推进销售流程，无需切换工具。

rss · OpenAI Blog · Nov 17, 08:00

**「为什么重要」** OpenAI 将 ChatGPT 扩展至销售工作流，标志其从通用助手向垂直场景渗透。官方博客发布且来源可信，代表产品战略的实质性转向。

**「可关注」** 可关注：Sales 插件与 30+ 合作伙伴集成在潜在客户研究、话术准备和 CRM 更新场景中的实际表现。

**Tags**: `#product`, `#lab`, `#industry`

---

<a id="item-ai-daily-4"></a>
### [GitHub 微软试点 AI 漏洞修复直报](https://github.blog/open-source/maintainers/maintainers-dont-need-more-ai-bug-reports-they-need-fixes/) ⭐️ 7.8/10

GitHub 与微软联合开展开源 AI 漏洞修复试点，针对 AI 生成的重复、无效漏洞报告淹没开源维护者工作量的痛点，尝试让 AI 直接提供带修复建议的已验证漏洞报告而非仅提交原始发现。试点使用微软 Codename MDASH 多模型代理扫描系统扫描 6 个 GitHub Secure Open Source Fund 支持的开源项目，初始标记 9791 个潜在问题，经 GitHub 安全实验室 AI 分诊代理去重、有效性校验，再由 7 名微软 FORGE 实验室研究员人工复核后，仅向维护者发送 99 份私有报告。截至 2026 年 11 月 15 日，维护者已完成 55 份漏洞修复，其中 14 份已进入正式发布版本。试点样本量较小，相关经验仍属早期探索。

rss · GitHub Blog · Nov 17, 18:29

**「为什么重要」** 当前 AI 漏洞扫描成本极低但修复仍需人工判断，大量未经筛选的 AI 漏洞报告已造成维护者负担过载，该试点将“找漏洞”和“修漏洞”的链路打通，直接提交带修复建议的高质量报告，为缓解开源维护者压力、提升开源安全修复效率提供了可参考的实践路径。

**「可关注」** 可关注：试点将 AI 扫描的原始漏洞结果经 AI 分诊、人工复核后压缩至约 1% 再提交维护者，且每份报告附带可审查的修复建议，将维护者的工作重心从筛选报告转移到实际修复。

**Tags**: `#open-source`, `#industry`, `#product`

---