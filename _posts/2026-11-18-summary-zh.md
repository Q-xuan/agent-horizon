---
layout: default
title: "Horizon Summary: 2026-11-18 (ZH)"
date: 2026-11-18
lang: zh
---

> 从 177 条内容中筛选出 16 条重要资讯。

<nav id="ah-toc" class="ah-toc" aria-label="目录"><span class="ah-toc-title">目录</span><ul><li><a href="#sec-harness-arch"><span class="ah-toc-name">Harness 架构</span><span class="ah-toc-count">3条</span></a></li><li><a href="#sec-agent-engineer"><span class="ah-toc-name">Agent 工程师日报</span><span class="ah-toc-count">6条</span></a></li><li><a href="#sec-ai-daily"><span class="ah-toc-name">AI 日报</span><span class="ah-toc-count">7条</span></a></li></ul></nav>

---

**[Harness 架构](#sec-harness-arch)**
1. [vLLM v0.34.0 发布](#item-harness-arch-1) ⭐️ 8.8/10
2. [pydantic-ai v2.69.0 发布](#item-harness-arch-2) ⭐️ 7.8/10
3. [OpenCode v1.19.6 发布](#item-harness-arch-3) ⭐️ 5.3/10

**[Agent 工程师日报](#sec-agent-engineer)**
1. [GPT-6.2 Astra/Sol 发布](#item-agent-engineer-1) ⭐️ 8.0/10
2. [coding agent 外部沙箱模式发布](#item-agent-engineer-2) ⭐️ 8.0/10
3. [K2-Horizon 开源模型系列公开](#item-agent-engineer-3) ⭐️ 7.0/10
4. [SPILLWAY 防御工具调用 Agent 提示注入](#item-agent-engineer-4) ⭐️ 7.0/10
5. [SWE-CoWork 编码 Agent 基准](#item-agent-engineer-5) ⭐️ 7.0/10
6. [Accelerate Bench：程序优化](#item-agent-engineer-6) ⭐️ 7.0/10

**[AI 日报](#sec-ai-daily)**
1. [OpenAI 联合北约开发 AI 网络防御工具](#item-ai-daily-1) ⭐️ 8.8/10
2. [Claude Platform 关联计费 beta 上线](#item-ai-daily-2) ⭐️ 8.8/10
3. [Gemini 4 Hydrogen 发布 机器人插件上线](#item-ai-daily-3) ⭐️ 8.8/10
4. [OpenAI 推出 ChatGPT Sales 插件](#item-ai-daily-4) ⭐️ 7.8/10
5. [Astra for Law 24 法律领域评测第一](#item-ai-daily-5) ⭐️ 7.8/10
6. [OpenAI 与智利政府达成合作](#item-ai-daily-6) ⭐️ 7.8/10
7. [GitHub 发布开源 AHP 协议](#item-ai-daily-7) ⭐️ 7.8/10

---

## Harness 架构
{: #sec-harness-arch .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-harness-arch" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-harness-arch-1"></a>
### [vLLM v0.34.0 发布](https://github.com/vllm-project/vllm/releases/tag/v0.34.0) ⭐️ 8.8/10

vLLM v0.34.0 发布，包含 1,061 次提交与 10 个新模型。运行时移除 Model Runner V1，Extensible KV cache 默认开启，默认 block size 从 16 改为 64。新增 Blackwell/MI355X 硬件加速，Step5 解码最高提升 1.95 倍。多项破坏性变更：ROCm 7.2 镜像移除，要求 huggingface\_hub &gt;= 2.0.0，移除 fp\_quant 与 Marlin W4A8 量化路径。

github · khluu · 11月16日 23:22

**「设计要点」** Model Runner V2 成为唯一 GPU 运行时，Dual-batch overlap 与 speculative decoding 均迁移至 MRV2；Extensible KV cache 改为基于 warmup 后实际空闲内存动态 sizing，替代原有估算机制。新增 \`/checkpoint/prepare\`、\`/checkpoint/status\`、\`/checkpoint/restore\` 接口支持 CRIU + cuda-checkpoint，Rust frontend 同步支持无状态 Responses API 与 n &gt; 1。

**「改了什么」** 移除 Model Runner V1，MRV2 成为唯一 GPU 运行时。Extensible KV cache 默认开启，block size 默认值从 16 调整为 64。终止 ROCm 7.2 支持，强制 huggingface\_hub &gt;= 2.0.0，移除 fp\_quant 与 Marlin W4A8 量化路径。

**标签**: `#runtime`, `#prefix-cache`, `#breaking-changes`

---

<a id="item-harness-arch-2"></a>
### [pydantic-ai v2.69.0 发布](https://github.com/pydantic/pydantic-ai/releases/tag/v2.69.0) ⭐️ 7.8/10

pydantic-ai v2.69.0 发布，对 deferred tool call 处理、工具调用 ID 作用域及 harness 命名空间做 breaking 调整。\`RequestInput\` 并入 \`HandleDeferredToolCalls\` 并支持 resume token；\`tool\_call\_ids\_are\_response\_scoped\` profile flag 统一工具调用 ID 生命周期。harness 包 \`subagents\`、\`filesystem\`、\`spend\` 改名为能力名，\`DockerSandbox\` 改名为 \`DockerContainer\`，\`BubblewrapSandbox\` 改名为 \`BubblewrappedWorkspace\`。运行时新增流式 thinking、text 与 tool call arguments 的 \`DetectLoops\` 循环检测，settled sub-agent 任务历史改为文件持久化，同时新增 \`WindowsWorkspace\`、\`KubernetesSandbox\` 与 harness 内 \`Peers\` 消息能力。

github · dsfaccini · 11月17日 01:03

**「设计要点」** 工具层通过 resume token 重构 deferred tool call 恢复路径；运行时在流式 thinking、text 与 tool call arguments 中插入 \`DetectLoops\` 循环检测。settled sub-agent 任务历史从 owner 内存迁出，改为文件持久化，降低内存占用。

**「改了什么」** 本版对工具调用与 harness 命名空间做 breaking 调整：\`RequestInput\` 并入 \`HandleDeferredToolCalls\` 并支持 resume token；\`tool\_call\_ids\_are\_response\_scoped\` profile flag 统一工具调用 ID 作用域；harness 包 \`subagents\`、\`filesystem\`、\`spend\` 改名为能力名，\`DockerSandbox\` 改名为 \`DockerContainer\`，\`BubblewrapSandbox\` 改名为 \`BubblewrappedWorkspace\`。运行时新增流式 thinking、text 与 tool call arguments 的循环检测，settled sub-agent 任务历史改为文件持久化，同时新增 \`WindowsWorkspace\`、\`KubernetesSandbox\`、harness 内 \`Peers\` 消息及 \`Coder\(autonomy=...\)\` 配置。

**标签**: `#runtime`, `#tools`

---

<a id="item-harness-arch-3"></a>
### [OpenCode v1.19.6 发布](https://github.com/anomalyco/opencode/releases/tag/v1.19.6) ⭐️ 5.3/10

OpenCode v1.19.6 发布。核心修复两项运行时行为：会话图片历史超过 25 MiB 时自动替换最旧图片为占位符，防止请求体膨胀；提供者返回请求体过大错误时，系统执行压缩并重试，而非直接失败该轮对话。桌面端新增 OpenCode 2.0 后台下载与可选升级路径。

github · github-actions\[bot\] · 11月17日 07:21

**「设计要点」** 运行时引入两层保护机制：图片上下文按 25 MiB 阈值做 oldest-first 裁剪并替换占位符；提供者请求失败时触发 compaction 重试链路，将失败 turn 转为可恢复错误。

**「改了什么」** 会话图片历史超 25 MiB 时自动裁剪最旧图片并替换占位符。提供者请求体过大错误触发压缩与重试，替代直接失败。

**标签**: `#runtime`, `#memory`

---

## Agent 工程师日报
{: #sec-agent-engineer .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-agent-engineer" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-agent-engineer-1"></a>
### [GPT-6.2 Astra/Sol 发布](https://openai.com/index/introducing-gpt-6-2-astra-sol/) ⭐️ 8.0/10

OpenAI 于 2026 年 11 月 17 日正式发布 GPT-6.2 Astra 与 GPT-6.2 Sol，API 标识分别为\`gpt-6.2-astra\`和\`gpt-6.2-sol\`。Astra 输入定价$8/MTok、输出$40/MTok，为上一代 6 Astra 定价的 80%，缓存输入价降至$0.40/MTok，为上一代的 1/4；Sol 维持$2/$10 定价，为 GPT-5.6 Sol 的一半。社区实测显示，Astra 在数据分析考试中成本从约$20 降至约$4，Sol 从$2.6 降至$1.2，同时 token 效率提升约 20%、所需工具调用次数减少、推理速度更快；PacBench 测试中 Astra 得分 92、耗时 6.6 分钟、花费$2.04，Sol 得分 87、耗时 6.3 分钟、花费$0.49。已知问题包括 Astra 长任务执行中偶尔提前终止未找到目标答案，部分用户反馈其沟通风格存在困惑、会提出无意义的内部实现细节问题。

hackernews · jasondavies · 11月17日 17:46 · [社区讨论](https://news.ycombinator.com/item?id=50535230)

**「为什么重要」** 本次发布直接降低了 agent 工作流的 API 调用成本，缓存折扣对长运行会话场景利好，实测的 token 效率、工具调用减少、速度提升对 coding agent 与评估 harness 的设计有直接参考价值；但 Astra 的长任务稳定性、沟通风格问题对实际落地的具体影响仍需更多场景验证。

**「可关注」** 可关注：GPT-6.2 Astra 的缓存输入价折扣与 token 效率提升，对长运行 agent 会话的成本优化有直接参考价值；同时需验证其长任务提前终止问题对自身工作流的影响。

**「评论」** 社区反馈两极：部分用户实测确认成本、速度优势明显，也有用户指出 Astra 在创意、办公类场景表现弱于竞品，长任务中偶发的无意义提问、提前终止问题影响实际使用体验。

**标签**: `#coding-agent`, `#eval`, `#harness`

---

<a id="item-agent-engineer-2"></a>
### [coding agent 外部沙箱模式发布](https://simonwillison.net/2026/Nov/17/external-sandboxes-for-coding-agents/) ⭐️ 8.0/10

2026 年 11 月 17 日，Simon Willison 与 AI 研究实验室 Prime Radiant 联合推出面向 coding agent 的「外部沙箱」架构模式，同步发布三个本地服务器实现，用于隔离 agent 执行的代码与宿主机环境，降低 prompt injection 等攻击带来的风险。三个实现分别托管于 \`prime-radiant-inc/external-sandbox-v86\`、\`prime-radiant-inc/external-sandbox-container\`、\`prime-radiant-inc/external-sandbox-quicksand\` 仓库：前者基于 v86 在 WebAssembly 中运行 Alpine Linux，中间者基于 Apple Containers 运行 Alpine Linux，后者基于 Microsoft Quicksand 库捆绑 QEMU 与 Alpine Linux。所有实现均提供统一的 localhost API，可配置 Pi、Claude Code、Codex 等工具将代码执行请求发送至沙箱。沙箱还支持可选 HTTP/HTTPS 白名单代理与凭证替换机制，可在不向 agent 泄露密钥的前提下完成需要认证的 API 调用。

rss · Simon Willison · 11月17日 22:52

**「为什么重要」** 该模式直接针对 coding agent 本地部署时的代码执行安全痛点，尤其适合希望试用本地模型又担心 prompt injection 造成宿主机损害的开发者，三个开箱即用的实现降低了相关安全隔离方案的落地门槛。

**「可关注」** 可关注：三个实现均提供统一 localhost API，可低成本接入现有 coding agent 工具链，无需修改 agent 核心逻辑即可获得代码执行隔离能力。

**标签**: `#sandbox`, `#coding-agent`, `#security`, `#permissions`, `#toolchain`

---

<a id="item-agent-engineer-3"></a>
### [K2-Horizon 开源模型系列公开](https://huggingface.co/papers/2611.21003) ⭐️ 7.0/10

2026 年 11 月 17 日，Hugging Face Daily Papers 公开 K2-Horizon 预印本，该系列包含 6 款全开源语言模型，规模覆盖 0.9B 稠密模型到 375B-A23B 混合专家（MoE）模型，面向通用推理、智能体任务（数学、科学、软件工程、深度研究、办公自动化等场景）。作者提出混合值注意力（MoVA）、softplus 注意力门控、Uno 无损扩散适配器三项技术，其中 36B-A4B 模型采用前两项技术，在相同训练数据下接近 32B 稠密模型效果，激活参数仅为后者的 1/7，解码速度最高提升 2.2 倍。作者报告的智能体与编码基准测试结果与同尺寸强开源模型相当，完整复现细节需查阅完整论文。

rss · Hugging Face Daily Papers · 11月17日 00:00

**「为什么重要」** 该系列首次公开覆盖 0.9B 至 375B 的全开源模型矩阵，同时披露的 MoVA、Uno 适配器等技术方案为低激活参数模型设计、解码加速提供了可参考的实现路径；其 benchmark 结果经社区复现验证后，可补充当前开源智能体模型的选型参考。

**「可关注」** 可关注：MoVA 与 softplus 注意力门控的组合可在激活参数仅为 1/7 的情况下接近更大稠密模型效果，Uno 无损扩散适配器的 2.2 倍解码加速方案可纳入低延迟场景的优化候选。

**标签**: `#coding-agent`, `#eval`, `#harness`

---

<a id="item-agent-engineer-4"></a>
### [SPILLWAY 防御工具调用 Agent 提示注入](https://huggingface.co/papers/2611.07222) ⭐️ 7.0/10

2026 年 11 月 17 日 Hugging Face Daily Papers 发布论文介绍 SPILLWAY，这是一款面向工具调用 Agent 的提示注入确定性防御方案。该方案将动作准入与内容消毒分离，通过工具返回的结构化 typed 字段做动作准入判断，替代原有每步工具调用都需 LLM 检查的机制，无需为每个任务单独做规划，降低调用开销与攻击面。当前公开材料为截断版本，缺少完整技术细节与性能验证数据，该研究主要面向 Agent harness、安全工具链设计方向的工程师。

rss · Hugging Face Daily Papers · 11月17日 00:00

**「为什么重要」** 该研究针对工具调用 Agent 提示注入这一高影响安全问题，提出了区别于现有 LLM 逐步检查、溯源类防御的架构思路，将准入逻辑下沉到工具结构化返回字段，从设计上绕开了 LLM 被注入文本干扰的风险。目前仅公开截断版论文，具体性能提升幅度、落地兼容性等影响尚未得到公开验证。

**「可关注」** 可关注：工具返回的结构化字段可作为动作准入的确定性依据，替代部分场景下的 LLM 逐步检查逻辑，在降低调用开销的同时缩小提示注入攻击面。

**标签**: `#harness`, `#permissions`

---

<a id="item-agent-engineer-5"></a>
### [SWE-CoWork 编码 Agent 基准](https://huggingface.co/papers/2611.20218) ⭐️ 7.0/10

2026 年 11 月 17 日，Hugging Face Daily Papers 发布编码 Agent 协作基准 SWE-CoWork，用于评估 Agent 在模拟组织场景中作为数字员工的综合能力。该基准包含 101 个跨真实仓库的开发任务，覆盖 11 种编程语言、12 个应用领域，每个任务设置 26 个职责不同、知识边界受限、协作行为受控的同事，要求 Agent 从简短交接信息出发，完成跨角色需求收集、冲突证据协调、代码实现全流程，最终结果由私有可执行测试评估。目前公开内容仅提及评估了 11 个模型，发现部分实现与完整任务完成存在显著差距，未披露完整性能结果，对编码 Agent 评测体系设计与 harness 开发有直接参考价值。

rss · Hugging Face Daily Papers · 11月17日 00:00

**「为什么重要」** 该基准将编码 Agent 评测场景延伸到组织协作维度，填补了多源需求收集、跨角色冲突协调能力评测的空白；但目前公开的性能结果不完整，尚无法直接对比主流编码 Agent 在该场景下的实际表现差异。

**「可关注」** 可关注：当前编码 Agent 评测 harness 可参考其多角色、多源信息冲突的场景设计，补充组织协作维度的自动化评测用例。

**标签**: `#coding-agent`, `#eval`, `#orchestration`

---

<a id="item-agent-engineer-6"></a>
### [Accelerate Bench：程序优化](https://huggingface.co/papers/2611.20882) ⭐️ 7.0/10

2026-11-17，Hugging Face Daily Papers 发布 Accelerate Bench v1.1，一个包含 32 个 CPU 优化任务的基准测试，任务改编自科学应用与超算竞赛。基准提供公开测试接口与独立验证器，支持迭代开发。研究团队评估了 16 个编码智能体（模型与 harness 组合），Score@1 范围为 25.5% 至 67.4%。该基准仅覆盖程序优化用例，不评估其他编码任务。

rss · Hugging Face Daily Papers · 11月17日 00:00

**「为什么重要」** Accelerate Bench 提供了可复现的评估基础设施，便于比较不同 harness 在真实优化任务上的表现。但其范围狭窄，仅针对程序优化，结果不能直接推广到通用编码任务。

**「可关注」** 可关注：Score@1 在 25.5%–67.4% 区间分布，不同 harness 表现差异大。

**标签**: `#eval`, `#coding-agent`, `#harness`

---

## AI 日报
{: #sec-ai-daily .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-daily" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-daily-1"></a>
### [OpenAI 联合北约开发 AI 网络防御工具](https://openai.com/index/strengthening-nato-allied-cyber-defences-ai) ⭐️ 8.8/10

2026 年 11 月 17 日，OpenAI 在官方博客宣布与北约及盟国网络机构开展合作，共同开发面向可信防御方的 AI 工具，覆盖漏洞发现、修复方案测试、关键系统防护三大场景。目前双方未披露工具的具体落地时间与性能参数。

rss · OpenAI Blog · 11月17日 00:00

**「为什么重要」** 这是头部 AI 实验室与北约层面网络机构的首次公开合作，为 AI 技术应用于关键基础设施防御领域提供了官方合作范本，也推动 AI 网络防御从技术探索走向政策协同阶段。

**「可关注」** 可关注：后续公开的 AI 防御工具的技术边界、测试标准，以及漏洞发现环节的准确率与误报率相关指标。

**标签**: `#lab`, `#policy`, `#industry`

---

<a id="item-ai-daily-2"></a>
### [Claude Platform 关联计费 beta 上线](https://claude.com/resources/articles/linked-billing-on-claude-platform) ⭐️ 8.8/10

Anthropic 今日在 Claude Platform 上线关联计费 beta 功能，第三方平台（含 coding agent、工作流自动化工具等）可支持终端用户无需共享 API key 即可支付 Claude API 使用费用。终端用户保留原有 Anthropic 计费关系，可自主设置单平台月度消费限额，也可随时解绑关联；平台可自主决定单次请求由自身还是终端用户承担费用。目前已有 Asana、ClickHouse、Linear 等 19 家第三方平台支持该功能，当前为 beta 阶段，请求运行在平台所属组织，终端用户组织的 IP 白名单、加密密钥、数据保留规则不适用。

rss · Claude Blog · 11月17日 00:00

**「为什么重要」** 该功能解决了第三方平台集成 Claude API 时共享 API key 带来的密钥泄露风险，同时省去平台自建计量、计费系统的成本，平衡了平台接入效率与终端用户的计费控制权。

**「可关注」** 可关注：平台可通过 Console 或 Usage and Cost Analytics API（beta）获取各关联客户的请求量、Token 消耗及模型使用数据，无需自行搭建计量系统。

**标签**: `#lab`, `#product`, `#industry`

---

<a id="item-ai-daily-3"></a>
### [Gemini 4 Hydrogen 发布 机器人插件上线](https://developers.googleblog.com/gemini-hydrogen-for-robotics/) ⭐️ 8.8/10

Google 官方发布通用机器人模型 Gemini 4 Hydrogen，其速度、效率较前代 Gemini 4 机器人模型显著提升，同时具备更强的空间与具身推理能力。同日上线 Google Antigravity 平台的 Robotics 插件，提供硬件接入、仿真、机器人控制等预置技能，降低端到端机器人开发门槛。在 Artificial Analysis Robotics 0.1 基准测试中，Gemini 4 Hydrogen 控制 6 轴机械臂完成 8 项日常桌面任务得分为 58，与 Gemini 4 Argon 相当，单 token 成本更低；公开 ERQA 基准测试中，其多视角对应、3D 轨迹推理等空间推理任务表现优于 Gemini Robotics ER 2。使用该插件校准机械臂仅需约 10 分钟，从零搭建分拣应用全流程约 1 小时即可完成。该模型已在 Google Interactions API 上线，google-genai SDKs 首日提供支持。Antigravity 平台仅面向付费 Google AI Pro 或 Ultra 订阅用户开放。

rss · Google Developers AI · 11月17日 00:00

**「为什么重要」** Gemini 4 Hydrogen 将专有具身推理模型能力融入核心 Gemini 4 系列，性能全面超越前代专用模型，配合低代码插件大幅降低机器人应用开发门槛，让开发者可在数小时内完成从硬件接入到可落地应用的开发流程。

**「可关注」** 可关注：正在使用 Gemini Robotics ER 2 的开发者可迁移至 Gemini 4 Hydrogen 处理具身推理相关负载，Antigravity Robotics 插件支持通过自然语言调整 MuJoCo 仿真参数，验证抓取策略后可直接部署到实体硬件。

**标签**: `#model`, `#lab`, `#product`

---

<a id="item-ai-daily-4"></a>
### [OpenAI 推出 ChatGPT Sales 插件](https://openai.com/index/introducing-chatgpt-for-sales) ⭐️ 7.8/10

OpenAI 于 2026 年 11 月 17 日发布 ChatGPT Sales 插件，同步上线超 30 款新增及扩展的合作伙伴插件，覆盖潜在客户调研、销售话术准备、CRM 更新等销售工作流环节，可辅助推进交易流程。

rss · OpenAI Blog · 11月17日 08:00

**「为什么重要」** 该产品拓展了 ChatGPT 在企业销售场景的应用覆盖，将 AI 能力接入销售核心工作流。

**「可关注」** 可关注：ChatGPT 插件生态向垂直行业工作流延伸的落地路径。

**标签**: `#product`, `#industry`, `#lab`

---

<a id="item-ai-daily-5"></a>
### [Astra for Law 24 法律领域评测第一](https://openai.com/index/astra-law-6-2) ⭐️ 7.8/10

OpenAI 宣布 Astra for Law 在覆盖 24 个法律领域的启动评测中排名第一，该产品现已面向所有 ChatGPT Enterprise 客户开放申请访问。

rss · OpenAI Blog · 11月17日 00:00

**「为什么重要」** 这反映了 OpenAI 在法律智能垂直场景的 AI 能力落地进展，为法律行业企业用户提供了可申请的 AI 工具选项。

**「可关注」** 可关注：Astra for Law 在 24 个法律领域的评测细节，以及后续的访问权限扩展计划。

**标签**: `#product`, `#eval`

---

<a id="item-ai-daily-6"></a>
### [OpenAI 与智利政府达成合作](https://openai.com/index/introducing-openai-for-chile) ⭐️ 7.8/10

OpenAI 宣布与智利政府达成合作，双方将围绕负责任的 AI 采用、公共部门 AI 技能建设、支持当地初创企业开发 AI 应用三个方向推进落地。目前合作暂无公开的具体落地时间表与投入规模。

rss · OpenAI Blog · 11月17日 00:00

**「为什么重要」** 这是 OpenAI 国际政府协作的实质性拓展，有望推动智利公共部门 AI 能力建设与本地 AI 创业生态发展。

**「可关注」** 可关注：OpenAI 与智利政府合作覆盖公共部门技能建设与本地初创企业支持两大方向。

**标签**: `#policy`, `#industry`, `#lab`

---

<a id="item-ai-daily-7"></a>
### [GitHub 发布开源 AHP 协议](https://github.blog/engineering/engineering-principles/building-the-agent-host-protocol-for-sessions-that-continue-across-devices/) ⭐️ 7.8/10

GitHub 发布开源的 Agent Host Protocol（AHP），该协议最初为 VS Code 和 GitHub Copilot 构建，支持 agent 会话跨设备、跨应用无缝延续，现已开放供第三方集成到自定义工作流。此前 VS Code 内置的 Copilot Chat 扩展非测试代码超 41.5 万行 TypeScript，迁移到 AHP 架构后，VS Code agent host 约 36.9 万行 TypeScript，GitHub agent host 约 30.5 万行 Rust。AHP 不规定 agent 行为逻辑，仅聚焦交互方式，核心协议保持最小化，服务端必须实现 root、session、chat 三个通道，可选支持终端、MCP、遥测等扩展通道。

rss · GitHub Blog · 11月17日 18:20

**「为什么重要」** 此前各客户端需单独开发 agent 定制化集成，无法复用会话状态，AHP 作为统一开放标准，可让编辑器、终端、移动端、自定义工具等不同客户端共享同一套 agent 会话、历史与状态，解决跨设备会话延续的碎片化问题，降低第三方集成成本。

**「可关注」** 可关注：AHP 采用服务端仲裁的 reducer 式状态模型，客户端仅需发送 action 序列，天然支持弱网环境下的重连重放，且适配 React 等主流 UI 框架。

**标签**: `#open-source`, `#industry`, `#product`

---