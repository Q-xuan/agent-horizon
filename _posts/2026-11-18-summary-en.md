---
layout: default
title: "Horizon Summary: 2026-11-18 (EN)"
date: 2026-11-18
lang: en
---

> From 177 items, 16 important content pieces were selected

---

**Agent Harness Architecture**
1. [vLLM v0.34.0 发布](#item-harness-arch-1) ⭐️ 8.8/10
2. [pydantic-ai v2.69.0 发布](#item-harness-arch-2) ⭐️ 7.8/10
3. [OpenCode v1.19.6 Released](#item-harness-arch-3) ⭐️ 5.3/10

**AI Agent Engineer**
1. [GPT-6.2 Astra/Sol 发布](#item-agent-engineer-1) ⭐️ 8.0/10
2. [External sandbox 模式发布](#item-agent-engineer-2) ⭐️ 8.0/10
3. [K2-Horizon 开源模型舰队发布](#item-agent-engineer-3) ⭐️ 7.0/10
4. [SPILLWAY ：工具准入与消毒分离](#item-agent-engineer-4) ⭐️ 7.0/10
5. [SWE-CoWork 基准发布](#item-agent-engineer-5) ⭐️ 7.0/10
6. [Accelerate Bench 程序优化基准发布](#item-agent-engineer-6) ⭐️ 7.0/10

**AI Daily**
1. [OpenAI 与北约合作开发 AI 网络防御工具](#item-ai-daily-1) ⭐️ 8.8/10
2. [Claude Platform 关联计费 Beta 上线](#item-ai-daily-2) ⭐️ 8.8/10
3. [Gemini 4 Hydrogen 发布 机器人插件同步上线](#item-ai-daily-3) ⭐️ 8.8/10
4. [ChatGPT 新增 Sales 插件与 30+ 合作插件](#item-ai-daily-4) ⭐️ 7.8/10
5. [Astra for Law 24 法律领域评测第一](#item-ai-daily-5) ⭐️ 7.8/10
6. [OpenAI 与智利政府达成合作](#item-ai-daily-6) ⭐️ 7.8/10
7. [GitHub 开源 AHP 跨设备协议](#item-ai-daily-7) ⭐️ 7.8/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [vLLM v0.34.0 发布](https://github.com/vllm-project/vllm/releases/tag/v0.34.0) ⭐️ 8.8/10

vLLM v0.34.0 发布，移除 Model Runner V1，仅保留 Model Runner V2 作为 GPU 执行路径；默认启用可扩展 KV cache，按 warmup 后实际空闲内存分配缓存。该版本带来 Blackwell/MI355X 显著加速（Step5 解码最高 1.95×），并实施多项破坏性变更：默认 block size 改为 64、ROCm 7.2 镜像停更、强制 huggingface\_hub &gt;= 2.0.0。新增 10 个模型支持，包括 Mistral Large 4 与 MiniMax-M3.1-Flash。

github · khluu · Nov 16, 23:22

**「设计要点」** KV cache 分配机制从估算改为基于 CUDA graph capture 与 warmup 后的实际空闲内存，默认开启可扩展 KV cache。Model Runner V2 承载全部 GPU 推理负载，包括双批重叠、推测解码与 DCP；Rust 前端新增无状态 Responses API 与 n&gt;1 支持，服务层通过 /checkpoint/prepare、/checkpoint/status、/checkpoint/restore 提供 CRIU + cuda-checkpoint 的 checkpoint/restore 能力。

**「改了什么」** 移除 Model Runner V1 及其 logits processor 接口，默认 block size 从 16 改为 64，ROCm 7.2 构建产物停更，huggingface\_hub 最低版本要求提升至 2.0.0。可扩展 KV cache 默认启用，gpu\_memory\_utilization 默认值变为 1.0；同时移除 QuTLASS/fp\_quant、Marlin W4A8 量化支持及 Keye-VL/Keye-VL-1.5 模型支持，新增 suffix decoding、自定义 speculator 插件 API 及多种硬件加速内核。

**Tags**: `#runtime`, `#prefix-cache`, `#breaking-changes`

---

<a id="item-harness-arch-2"></a>
### [pydantic-ai v2.69.0 发布](https://github.com/pydantic/pydantic-ai/releases/tag/v2.69.0) ⭐️ 7.8/10

pydantic-ai v2.69.0 发布，核心变更包括延迟工具调用处理的破坏性调整、流式输出循环检测，以及工具调用 ID 作用域配置。\`HandleDeferredToolCalls\` 合并 \`RequestInput\` 并支持 resume token，\`DetectLoops\` 新增流式 thinking、text 和 tool call arguments 的循环检测。Harness 层重命名 \`subagents\`、\`filesystem\`、\`spend\` 等包为能力名，\`DockerSandbox\` 改为 \`DockerContainer\`，\`BubblewrapSandbox\` 改为 \`BubblewrappedWorkspace\`。

github · dsfaccini · Nov 17, 01:03

**「设计要点」** 延迟工具调用处理统一到 \`HandleDeferredToolCalls\` 并支持 resume token，改变 agent 中断恢复的接口契约。流式循环检测下沉到 \`DetectLoops\`，在 thinking、text 和 tool call arguments 层面对流式增量做重复检测，Harness 包重命名将能力名与包名对齐，\`DockerSandbox\` 保留废弃别名。

**「改了什么」** \`RequestInput\` 并入 \`HandleDeferredToolCalls\` 并支持 resume token，\`DetectLoops\` 新增流式循环检测，\`tool\_call\_ids\_are\_response\_scoped\` profile 标志配置工具调用 ID 作用域。Harness 的 \`subagents\`、\`filesystem\`、\`spend\` 包重命名为能力名，\`DockerSandbox\` 改名为 \`DockerContainer\`，\`BubblewrapSandbox\` 改名为 \`BubblewrappedWorkspace\`，\`Advisor\` 接受 \`native=\` 和 \`local=\` 并废弃 \`mode\`。

**Tags**: `#runtime`, `#tools`

---

<a id="item-harness-arch-3"></a>
### [OpenCode v1.19.6 Released](https://github.com/anomalyco/opencode/releases/tag/v1.19.6) ⭐️ 5.3/10

anomalyco/opencode v1.19.6 is a patch release focused on runtime stability. It introduces context overflow handling for session images, replacing the oldest entries with a placeholder when history exceeds 25 MiB. The release also adds compaction-based retry for oversized provider request bodies, preventing hard failures on size-limit errors.

github · github-actions\[bot\] · Nov 17, 07:21

**「What Changed」** Session image history now enforces a 25 MiB cap, substituting placeholders for the oldest images upon overflow. Provider request bodies exceeding size limits now undergo compaction and automatic retry instead of failing the turn.

**Tags**: `#runtime`, `#memory`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [GPT-6.2 Astra/Sol 发布](https://openai.com/index/introducing-gpt-6-2-astra-sol/) ⭐️ 8.0/10

2026年11月17日OpenAI正式发布GPT-6.2 Astra与GPT-6.2 Sol，API标识分别为\`gpt-6.2-astra\`与\`gpt-6.2-sol\`，第三方工具LLM 0.38已率先支持。Astra定价为输入$8/MTok、输出$40/MTok，是上一代6 Astra价格的80%，缓存输入定价$0.40/MTok；Sol定价维持$2/$10，为GPT-5.6 Sol的一半。社区实测显示两款模型在数据分析和PacBench等agent场景下成本、速度均有提升，Astra在数据分析考试中成本较6代降低约80%，token效率提升约20%，但存在长任务随机询问无关细节、偶尔提前终止漏答、特定生成任务效果弱于竞品的问题，部分办公场景生成效果也弱于旧版模型及竞品。

hackernews · jasondavies · Nov 17, 17:46 · [Discussion](https://news.ycombinator.com/item?id=50535230)

**「为什么重要」** 两款模型的定价与效率表现直接关联agentic工作流的边际成本，社区公开的对比基准和实测成本数据可减少选型时的信息差，但长任务的异常交互和特定场景的性能短板需要纳入评估范围。

**「可关注」** 可关注：两款模型的缓存输入定价折扣和工具调用次数减少，可优先在长上下文agent会话和工具链密集场景做成本验证，同时需处理长任务中无关提问的异常交互。

**「评论」** 社区共识认可两款模型的成本与速度优势，但普遍反馈Astra长任务会随机询问无关内部细节、办公及特定生成场景效果弱于竞品，也有用户指出发布相关讨论中竞品话题占比过高。

**Tags**: `#coding-agent`, `#eval`, `#harness`

---

<a id="item-agent-engineer-2"></a>
### [External sandbox 模式发布](https://simonwillison.net/2026/Nov/17/external-sandboxes-for-coding-agents/) ⭐️ 8.0/10

Simon Willison 与 Prime Radiant 发布 external sandbox 模式，将 coding agent 的代码执行隔离到专用沙箱，agent 本身运行于沙箱外，以降低本地模型试用时的误操作或 prompt injection 风险。同步开源三个服务器实现：\`external-sandbox-v86\`（Node.js + v86 在 WebAssembly 中运行 Alpine Linux）、\`external-sandbox-container\`（Python + Apple Containers 运行 Alpine Linux）、\`external-sandbox-quicksand\`（Python + Microsoft Quicksand 捆绑 QEMU 与 Alpine Linux）。三者提供统一 localhost API，可配置 Pi、Claude Code、Codex 发送代码执行请求；沙箱还支持可选的 HTTP/HTTPS 白名单代理与凭据替换机制，用于控制网络访问并避免向 agent 泄露密钥。

rss · Simon Willison · Nov 17, 22:52

**「为什么重要」** 该模式提供了一套可立即使用的 agent 代码隔离方案，直接回应安全与权限边界工程痛点。对正在评估本地模型或 agent 执行环境的团队，三个实现构成可对比、可验证的参考基线。

**「可关注」** 可关注：三个实现底层技术栈不同（WebAssembly、Apple Containers、QEMU），但对外提供统一 localhost API，并内置网络白名单代理与凭据替换，可直接接入 Pi、Claude Code、Codex 等现有工具链。

**Tags**: `#sandbox`, `#coding-agent`, `#security`, `#permissions`, `#toolchain`

---

<a id="item-agent-engineer-3"></a>
### [K2-Horizon 开源模型舰队发布](https://huggingface.co/papers/2611.21003) ⭐️ 7.0/10

2026年11月17日HF每日论文收录的预印本发布K2-Horizon全开源语言模型舰队，规模覆盖0.9B稠密模型到375B-A23B MoE模型，面向通用推理、智能体工作及软件工程等场景。该工作提出Mixture-of-Value Attention（MoVA）、softplus注意力门控、Uno无损扩散适配器三项技术改进，作者报告其智能体与编码基准表现领先或匹敌同尺寸开源模型，其中36B-A4B模型通过前两项技术几乎匹配同数据训练的32B稠密模型，活跃参数仅为后者的1/7，解码速度最高提升2.2x。目前仅公开预印本，完整可复现细节需查阅全文。

rss · Hugging Face Daily Papers · Nov 17, 00:00

**「为什么重要」** 该舰队全开源且覆盖多尺寸档位，为智能体、编码场景的模型选型与架构优化提供了新的参考基准；但当前仅公开预印本，作者报告的benchmark结果尚未经社区独立复现验证。

**「可关注」** 可关注：MoVA与softplus注意力门控的组合在36B-A4B模型上实现了接近32B稠密模型的性能，同时将活跃参数规模降至后者的1/7，为小尺寸高效模型设计提供了可参考的技术路径。

**Tags**: `#coding-agent`, `#eval`, `#harness`

---

<a id="item-agent-engineer-4"></a>
### [SPILLWAY ：工具准入与消毒分离](https://huggingface.co/papers/2611.07222) ⭐️ 7.0/10

2026年11月17日Hugging Face每日论文收录SPILLWAY相关研究，该论文当前获得49次HF每日论文点赞，针对工具调用型agent的提示注入攻击问题，提出将工具调用准入决策与内容消毒分离的确定性防御方案：不再依赖LLM对每次工具调用做准入检查，而是基于工具返回的typed字段判断调用是否放行，无需逐任务规划，降低调用开销与攻击面。当前公开材料为截断版本，缺少完整技术细节与性能验证数据，相关方案直接面向做agent harness、工具链安全设计的工程师群体。

rss · Hugging Face Daily Papers · Nov 17, 00:00

**「为什么重要」** 当前工具调用型agent的运行时防御普遍依赖LLM做逐次调用准入或前置任务规划，存在额外调用开销与攻击面。SPILLWAY提出的基于typed字段的确定性准入思路跳出了对LLM决策的依赖，为agent工具链安全设计提供了可参考的架构方向，但具体性能收益、兼容性等尚未有公开验证数据。

**「可关注」** 可关注：工具返回的typed字段可作为确定性准入判断的依据，减少工具调用链中对LLM决策的依赖，降低调用开销与提示注入攻击面。

**Tags**: `#harness`, `#permissions`

---

<a id="item-agent-engineer-5"></a>
### [SWE-CoWork 基准发布](https://huggingface.co/papers/2611.20218) ⭐️ 7.0/10

SWE-CoWork 基准于 2026-11-17 发布，包含 101 个跨真实仓库的开发任务，覆盖 11 种编程语言与 12 个应用领域。基准将编码 Agent 置于含 26 个职责不同同事的模拟组织场景，要求其从简短交接中恢复分散需求、协调冲突证据并实现代码变更，最终通过私有可执行测试评估。研究团队评估了 11 个模型，发现部分实现与完整任务完成之间存在显著差距，但性能结果展示不完整。该基准为编码 Agent 在多源需求收集、冲突协调与代码实现全流程能力提供了评测框架。

rss · Hugging Face Daily Papers · Nov 17, 00:00

**「为什么重要」** 该基准首次将编码 Agent 置于模拟组织协作场景，而非传统单一仓库修复任务，对评估 Agent 在实际工程环境中的综合能力有直接参考价值。材料未展示具体性能数字，因此尚未证实各模型在真实组织场景中的表现排序。

**「可关注」** 可关注：SWE-CoWork 的 26 同事模拟机制与私有测试评估方式，可能影响后续编码 Agent 评测基准的设计方向。

**Tags**: `#coding-agent`, `#eval`, `#orchestration`

---

<a id="item-agent-engineer-6"></a>
### [Accelerate Bench 程序优化基准发布](https://huggingface.co/papers/2611.20882) ⭐️ 7.0/10

2026-11-17，Hugging Face Daily Papers 发布 Accelerate Bench 基准测试，包含 32 个来自科学应用与超级计算竞赛的 CPU 优化任务。每个任务提供可运行程序，明确工作负载、正确性要求、时间边界及允许编辑范围，要求 agent 自主选择优化位置与策略。基准支持公开测试迭代与独立验证器评分，版本 1.1 下评估 16 组模型-harness 配对，Score@1 介于 25.5% 至 67.4% 之间。当前范围仅覆盖程序优化用例，且多数提交程序正确但加速幅度差异显著。

rss · Hugging Face Daily Papers · Nov 17, 00:00

**「为什么重要」** 该基准为 coding agent 与 harness 的优化能力提供了可复现的对比框架，但当前仅覆盖程序优化单一场景，尚未证实对通用代码生成任务的迁移价值。

**「可关注」** Score@1 在 16 个 harness 间跨度达 41.9 个百分点，提示程序优化任务对模型-harness 配对选择高度敏感。

**Tags**: `#eval`, `#coding-agent`, `#harness`

---

## AI Daily

<a id="item-ai-daily-1"></a>
### [OpenAI 与北约合作开发 AI 网络防御工具](https://openai.com/index/strengthening-nato-allied-cyber-defences-ai) ⭐️ 8.8/10

OpenAI 宣布与北约及盟国网络机构合作，开发 AI 工具协助可信防御者发现系统漏洞、测试修复方案并保护关键基础设施。项目聚焦防御性应用场景。目前公开信息未披露具体合作规模、技术细节或部署时间表。

rss · OpenAI Blog · Nov 17, 00:00

**「为什么重要」** 该合作将 AI 模型直接对接北约及盟国网络防御机构，属于 AI 实验室与国防联盟的直接技术合作。此类合作通常伴随严格的使用范围限制与合规要求。

**「可关注」** 可关注：AI 在漏洞发现与修复验证环节的自动化能力演进，以及面向可信防御者的工具访问控制设计。

**Tags**: `#lab`, `#policy`, `#industry`

---

<a id="item-ai-daily-2"></a>
### [Claude Platform 关联计费 Beta 上线](https://claude.com/resources/articles/linked-billing-on-claude-platform) ⭐️ 8.8/10

Anthropic 在 Claude Platform 上线关联计费（linked billing）Beta 版。包括 Asana、ClickHouse、Linear、Warp 等在内的第三方平台可让终端客户直接支付 Claude API 用量，无需共享 API 密钥。客户保留现有 Anthropic 计费关系，可设置月度消费上限并随时解绑，但请求在平台的组织中运行，客户组织的 IP 白名单、加密密钥及数据保留策略不适用。

rss · Claude Blog · Nov 17, 00:00

**「为什么重要」** 对构建 coding agent 或工作流工具的团队而言，关联计费消除了托管客户 API 密钥的安全负担，同时让终端用户保留对支出和 Anthropic 组织策略的控制权。平台无需自建计量与开票系统即可直接向客户转嫁 Claude API 成本。

**「可关注」** 可关注：平台可通过 Console 或 Usage and Cost Analytics API（Beta）查看每个关联客户的请求数、Token 用量及模型使用情况，并在单请求级别决定由平台还是终端客户承担费用。

**Tags**: `#lab`, `#product`, `#industry`

---

<a id="item-ai-daily-3"></a>
### [Gemini 4 Hydrogen 发布 机器人插件同步上线](https://developers.googleblog.com/gemini-hydrogen-for-robotics/) ⭐️ 8.8/10

Google官方发布通用机器人模型Gemini 4 Hydrogen，速度与效率较前代Gemini 4 Argon显著提升，保留直接由相机图像控制机械臂的能力，空间与具身推理能力更强。配套上线Google Antigravity平台的Robotics插件，集成硬件接入、仿真、控制等全流程技能，降低端到端机器人开发门槛。关键性能与效率数据：在Artificial Analysis Robotics 0.1基准上，Hydrogen控制6轴机械臂完成8项日常桌面任务得分为58，单token成本低于Argon；在公开ERQA基准上，其空间推理任务表现优于Gemini Robotics ER 2；插件支持I2RT YAM、SO-ARM101、FR3 Duo等机械臂的快速校准，其中I2RT YAM臂校准耗时约10分钟。使用限制：Antigravity Robotics插件仅面向付费Google AI Pro或Ultra订阅用户开放，需在Antigravity的Customizations中搜索Robotics安装。

rss · Google Developers AI · Nov 17, 00:00

**「为什么重要」** 该模型与插件组合将高物理推理能力与低成本、快速开发流程结合，开发者可从零开始在数小时内完成可落地的机器人应用，大幅降低通用机器人开发门槛。

**「可关注」** 可关注：Gemini 4 Hydrogen在ERQA等基准上全面超越Gemini Robotics ER 2，现有ER 2用户可迁移相关 workloads；Antigravity Robotics插件支持MuJoCo直接在平台内运行，可通过自然语言迭代调整机器人控制策略。

**Tags**: `#model`, `#lab`, `#product`

---

<a id="item-ai-daily-4"></a>
### [ChatGPT 新增 Sales 插件与 30+ 合作插件](https://openai.com/index/introducing-chatgpt-for-sales) ⭐️ 7.8/10

OpenAI 发布 ChatGPT Sales 插件。同步上线 30 余款新的和扩展的合作插件。这些工具覆盖潜在客户研究、销售话术准备及 CRM 更新。用户可在 ChatGPT 内直接推进交易流程。

rss · OpenAI Blog · Nov 17, 08:00

**「为什么重要」** 这是 ChatGPT 首次进入销售垂直场景。对构建 coding agent 的团队而言，插件生态展示了 LLM 与外部工作流的集成范式。

**「可关注」** 可关注：ChatGPT 销售插件覆盖潜在客户研究、话术准备与 CRM 更新场景。

**Tags**: `#product`, `#industry`, `#lab`

---

<a id="item-ai-daily-5"></a>
### [Astra for Law 24 法律领域评测第一](https://openai.com/index/astra-law-6-2) ⭐️ 7.8/10

OpenAI 宣布 Astra for Law 在覆盖 24 个法律领域的启动评测中获得第一名。该产品现已面向所有 ChatGPT Enterprise 客户开放，需提交申请获取访问权限。

rss · OpenAI Blog · Nov 17, 00:00

**「为什么重要」** 这标志着 OpenAI 在垂直领域法律智能上的首次公开评测亮相，并直接向企业客户交付。对正在评估法律 AI 工具的团队而言，这是一个可量化的性能参考点。

**「可关注」** 可关注：Astra for Law 的评测基准覆盖 24 个法律领域，可作为法律 AI 能力对比的参考框架。

**Tags**: `#product`, `#eval`

---

<a id="item-ai-daily-6"></a>
### [OpenAI 与智利政府达成合作](https://openai.com/index/introducing-openai-for-chile) ⭐️ 7.8/10

2026年11月17日，OpenAI 官方宣布与智利政府达成合作，双方将围绕三个方向推进相关工作：支持负责任的 AI 落地、建设公共部门 AI 技能、帮助当地初创企业开发 AI 应用。目前公开信息未披露合作的具体资金规模、落地时间表等细节。

rss · OpenAI Blog · Nov 17, 00:00

**「为什么重要」** 这是 OpenAI 国际政府合作版图向拉美地区的实质性延伸，为当地 AI 生态发展提供了直接的产业与政策支持。

**「可关注」** 可关注：OpenAI 拉美政府合作的具体落地规则，以及其对当地 AI 初创企业的技术资源倾斜方向。

**Tags**: `#policy`, `#industry`, `#lab`

---

<a id="item-ai-daily-7"></a>
### [GitHub 开源 AHP 跨设备协议](https://github.blog/engineering/engineering-principles/building-the-agent-host-protocol-for-sessions-that-continue-across-devices/) ⭐️ 7.8/10

GitHub 发布开放标准 Agent Host Protocol \(AHP\)，实现 AI agent 会话跨设备、跨应用无缝续接。该协议最初在 VS Code 和 GitHub Copilot 中落地，现已开放供第三方集成，并已交付五个客户端与两个宿主实现。协议以 URI 标识的 channel 为核心，服务端仲裁 reducer 状态，客户端发送 action 驱动状态变更或触发副作用。未披露协议具体版本号及完整 channel 规范细节。

rss · GitHub Blog · Nov 17, 18:20

**「为什么重要」** 此前每个客户端需独立集成，agent 生命周期绑定单窗口，关闭窗口或切换设备即丢失会话。AHP 提供统一协议，使多客户端共享同一 agent 历史与状态，开发者无需为每个宿主重复造轮子。

**「可关注」** 可关注：协议采用 reducer 状态模型，服务端仲裁状态，客户端仅发送 action，便于断线重连、重放及调试，且与 React 等 UI 框架兼容。

**Tags**: `#open-source`, `#industry`, `#product`

---