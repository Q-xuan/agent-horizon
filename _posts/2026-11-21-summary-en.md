---
layout: default
title: "Horizon Summary: 2026-11-21 (EN)"
date: 2026-11-21
lang: en
---

> From 183 items, 17 important content pieces were selected

---

**Agent Harness Architecture**
1. [Codex rust-v0.171.0 发布](#item-harness-arch-1) ⭐️ 7.8/10
2. [Agents SDK v1.0.0a1 发布](#item-harness-arch-2) ⭐️ 7.8/10
3. [Agents v0.34.0 发布](#item-harness-arch-3) ⭐️ 7.8/10
4. [OpenAI Agents API 时间感知模式](#item-harness-arch-4) ⭐️ 6.8/10

**AI Agent Engineer**
1. [Hugging Face 发布 Harness Adapters 方案](#item-agent-engineer-1) ⭐️ 8.8/10
2. [Inkling 2 Mini 开源发布](#item-agent-engineer-2) ⭐️ 7.0/10
3. [TuringSpace 交互式 CAPTCHA 基准发布](#item-agent-engineer-3) ⭐️ 6.0/10
4. [AltRA-Test 支持 LLM 裁判替代人类标注](#item-agent-engineer-4) ⭐️ 6.0/10
5. [Fragments：代码质量降多智能体审查成本](#item-agent-engineer-5) ⭐️ 6.0/10
6. [WeVisForensics 自演化多智能体检测框架](#item-agent-engineer-6) ⭐️ 5.5/10

**AI Daily**
1. [Anthropic IPO 完成 总募资约1195亿美元](#item-ai-daily-1) ⭐️ 9.8/10
2. [OpenAI 推出对抗性蒸馏分层防护](#item-ai-daily-2) ⭐️ 8.8/10
3. [OpenAI 发布 MedChemBench](#item-ai-daily-3) ⭐️ 7.8/10
4. [Agent Anomaly Detection 支持跨云监控](#item-ai-daily-4) ⭐️ 7.8/10
5. [上海AI Lab开源Sage S2.1](#item-ai-daily-5) ⭐️ 5.0/10

**AI Deals**
1. [Epic 本周限免两款游戏](#item-ai-deals-1) ⭐️ 8.0/10
2. [greatai Review 上线 开源非营利可领免费审查](#item-ai-deals-2) ⭐️ 5.0/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [Codex rust-v0.171.0 发布](https://github.com/openai/codex/releases/tag/rust-v0.171.0) ⭐️ 7.8/10

openai/codex 正式发布 rust-v0.171.0。模型目录新增 GPT-6.2 Sol 与 Astra，Sol 设为默认选择。本次更新默认启用带子代理转录的 TUI 工作区，支持可搜索文档预览、图像预览及主对话并排显示。新增 \`codex exec --remote &lt;ADDR&gt;\` 命令在现有应用服务器上启动或恢复非交互式会话，以及通过 \`/statusline\` 配置自定义 MCP 状态行。修复会话切换时草稿、排队跟进和中断输入随原始线程保留的问题，以及变更工作目录时权限配置文件丢失的问题。

github · github-actions\[bot\] · Nov 20, 00:44

**「设计要点」** TUI 状态行采用本地配置加持久化的提供者架构，支持 MCP 状态行发现与线程作用域资源读取。会话层引入 session-scoped stores 稳定模型侧 ID，并保留 MCP 注册作用域跨客户端操作。

**「改了什么」** 默认启用 TUI 工作区并展示子代理转录，新增 \`codex exec --remote\` 远程非交互式会话执行及 \`/statusline\` 自定义 MCP 状态行。修复会话切换时草稿与排队跟进丢失、工作目录变更时权限配置文件失效，以及企业 MCP 无刷新令牌 ID 令牌的登录问题。

**Tags**: `#runtime`, `#subagents`, `#mcp`, `#memory`, `#tools`

---

<a id="item-harness-arch-2"></a>
### [Agents SDK v1.0.0a1 发布](https://github.com/openai/openai-agents-python/releases/tag/v1.0.0-alpha.1) ⭐️ 7.8/10

OpenAI Python Agents SDK 发布 v1.0.0-alpha.1 首个预览版，基于 feat/simple-codex 分支合并。本次将 Codex 作为 opt-in 模型提供商引入，通过 PyO3 嵌入未修改的 Codex Core rust-v0.166.0，直接调用 Core 以消除 codex app-server 启动及 JSON-RPC 通信层。开发者通过 \`CodexProvider\` 与 \`RunConfig\(model\_provider=provider\)\` 选择 Codex，支持 API key 或已保存登录态。预构建 wheel 仅通过 GitHub Releases 分发，支持 CPython 3.10–3.14 及 Linux x86-64、Linux ARM64、macOS 11+ Apple silicon、Windows x64 四平台。

github · markstuart-oai · Nov 20, 20:51

**「设计要点」** 运行时通过 PyO3 将 Codex Core Rust 核心直接嵌入 Python 进程，移除独立 app-server 与 JSON-RPC 中间层。provider 复用单一 \`ThreadManager\`，每次调用获取新线程，需通过 \`await provider.aclose\(\)\` 显式关闭以释放资源。

**「改了什么」** 相对 v0.24.0-alpha.8，执行入口从 \`Agent.run\(\)\` / \`Session.submit\(\)\` 迁移至 \`Runner.run\(\)\` / \`Runner.run\_streamed\(\)\`，并在 run config 中通过 \`CodexProvider\` 选择模型。会话压缩改用本地对话历史（含审批暂停后），保存的沙箱清单开始保留内联二进制文件。

**Tags**: `#runtime`, `#model-provider`

---

<a id="item-harness-arch-3"></a>
### [Agents v0.34.0 发布](https://github.com/cloudflare/agents/releases/tag/agents%400.34.0) ⭐️ 7.8/10

Cloudflare 发布 agents v0.34.0。本次升级支持 Pi 1.6，引入非阻塞等待工具、子代理等待协调、MCP 重新授权信号及失败请求错误脱敏。Pi 工具可通过 \`harness.signal\(\)\` park 等待信号或截止时间，agent 同时睡眠；\`submit\(\)\` 与 \`continue\(\)\` 接受 \`notify\` 参数，支持跨会话唤醒；\`submit\(input, \{ onAbort: &quot;keep&quot; \}\)\` 保留中止时的排队输入。MCP 客户端在需要重新授权时抛出 \`MCPAuthorizationRequiredError\`，失败服务器保持失败状态直到调用 \`reconnectMcpServer\(id\)\`。失败请求默认返回通用 500 或 WebSocket 1011 关闭码，不再泄露错误详情，可通过 \`onFetchError\(\)\` 自定义响应。

github · github-actions\[bot\] · Nov 20, 15:56

**「设计要点」** Pi 1.6 将工具等待从阻塞改为 park/signal 模型，agent 在工具等待期间可睡眠，降低资源占用。MCP 客户端引入显式重新授权状态机，失败服务器不再自动重试，需手动调用 \`reconnectMcpServer\(id\)\` 恢复。错误处理层统一拦截失败请求并脱敏，\`onFetchError\` 提供自定义响应扩展点。

**「改了什么」** Pi harness 升级至 Pi 1.6，1.5 不再支持且无法回滚。新增 \`harness.signal\(\)\`、\`submit\(\)\`/\`continue\(\)\` 的 \`notify\` 与 \`onAbort: &quot;keep&quot;\`、\`harness.root\(\)\`/\`sessions.create\(\)\`/\`sessions.fork\(\)\` 的 \`init\` 参数。MCP 客户端增加 \`MCPAuthorizationRequiredError\` 与 \`reconnectMcpServer\(id\)\`。Lifecycle 增加 \`onFetchError\` 钩子，默认隐藏失败请求错误详情。修复跨标签页聊天竞态条件，\`PiHarness.dispose\(\)\` 释放 pi-ai 会话状态，更多 provider 连接断开后自动重试。Anthropic 消息线程过期后自动重建，FLUX.2 图像模型接入，\`claudeCode\(\)\` 默认模型改为 \`claude-sonnet-5-5\`，示例代码迁移出已停用的 Workers AI 模型，已取消的 schedule、queue 和 Task 不再重跑。

**Tags**: `#runtime`, `#tools`, `#mcp`, `#subagents`

---

<a id="item-harness-arch-4"></a>
### [OpenAI Agents API 时间感知模式](https://developers.openai.com/blog/time-awareness-and-async-input-for-personal-agents) ⭐️ 6.8/10

OpenAI 官方博客发布个人 Agent 的时间感知与异步输入设计模式。Agents API 新增 time awareness 能力，向模型周期性推送当前时间，使其能根据截止时间调整工作优先级。同步引入 async function tools，允许 Agent 在等待用户回复时继续执行其他任务。文章以会议准备 Agent 为例，展示使用 \`gpt-6.2-astra\` 模型、开启 \`experimental.time\_awareness: true\` 并配置 \`request\_user\_input\_async\` 异步工具的完整代码，覆盖 JavaScript、Python、Go、Java、Ruby 五种 SDK。

rss · OpenAI Developer · Nov 20, 00:00

**「设计要点」** 运行时通过实验性 time awareness 将时间上下文注入模型循环，驱动 Agent 按剩余时间重新排优先级。异步工具层以 \`async: true\` 标记函数工具，Agent 循环在等待用户输入时可继续执行搜索等独立任务，工具返回用户回复或超时状态。

**「改了什么」** Agents API 新增实验性 time awareness 配置项与异步函数工具类型。开发者开启 \`experimental.time\_awareness: true\` 即可让模型感知时间流逝，定义 \`async: true\` 的函数工具后，Agent 能在等待用户输入期间保持工作进度。

**Tags**: `#runtime`, `#planning`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [Hugging Face 发布 Harness Adapters 方案](https://huggingface.co/blog/harness-adapters-at-scale) ⭐️ 8.8/10

Hugging Face 2026-11-20 发布博客，提出通过 RL 训练定制 LoRA adapter 适配特定 agent harness 与任务分布。以 Qwen3.8-27B 为例，在 pi harness 下 Terminal-Bench 2.1 pass@1 从 39% 提升至 55%，单任务平均 token 从 2.9K 降至 1.5K。团队针对 pi 1.5.2、OpenCode 2.2.7、Hermes Agent v0.22.6 分别训练 adapter，并合并为可在三者 unchanged 运行的 super adapter。训练使用 TRL AsyncGRPOTrainer、OpenEnv 与 Harbor，任务集经 openenv validate 及基础模型难度筛选后公开于 Hub。

rss · Hugging Face Blog · Nov 20, 00:00

**「为什么重要」** 该方案证明在真实 harness 内部做 RL 训练可同时提升准确率与 token 效率，且提供可复用的端到端 recipe。这为 coding agent 优化提供了针对特定工具链做微调的具体路径。

**「可关注」** 可关注：在 harness 内部做 RL 训练可直接利用生产 token 分布，但需锁定 harness 版本并验证合并 adapter 的跨 harness 行为一致性。

**Tags**: `#harness`, `#eval`, `#coding-agent`, `#orchestration`

---

<a id="item-agent-engineer-2"></a>
### [Inkling 2 Mini 开源发布](https://thinkingmachines.ai/news/inkling-2-mini/) ⭐️ 7.0/10

Thinking Machines Lab released Inkling 2 Mini, an open-weight looped transformer with ~26B total parameters and 3B active parameters per token that repeats its middle 12 layers three times to execute 48 visits per token via cross-pass gating. It supports 1M-token multimodal context, ships in NVFP4 and MXFP8 with a DSpark drafter, and works with Ollama, Llama.cpp, and SGLang. A variable-loop research variant is also available. The lab reports it matches or exceeds Qwen3.8-27B on 32 of 48 AA Index v5 benchmarks, leading in FrontierCode v2.0 and tying Terminal-Bench 4.0, though trailing on AutomationBench-AA v1.0.6.

hackernews · jasondavies · Nov 20, 20:12 · [Discussion](https://news.ycombinator.com/item?id=50581260)

**「为什么重要」** The release matters because it packages a parameter-efficient looped architecture into a locally deployable form factor, giving engineers a tunable compute-accuracy knob via the variable-pass research variant. However, the claimed reasoning gains do not extend to factuality: AA-Omniscience scores scale with total parameter count rather than loop depth, so knowledge-intensive tasks may not improve with extra passes. Independent validation of the benchmark claims is still pending.

**「可关注」** The architecture reuses core weights across passes while maintaining separate KV caches and short-convolution states for each of the 48 layer visits, reducing checkpoint size but preserving per-visit context. For agent harnesses, the 1M context window and per-token expert routing \(8 of 128 experts\) will pressure existing KV cache management and MoE scheduling; the DSpark drafter may offset latency but adds memory overhead. The variable-pass research checkpoint lets teams benchmark speed-accuracy trade-offs on their own hardware before committing to the fixed 3-pass configuration.

**「评论」** Commenters express strong interest in local testing, particularly on AMD RDNA 3 hardware, and note the unsloth/Inkling-2-Mini-GGUF release for Ollama. Some view the open-weight looped architecture as a potential industry shift, while others caution that reasoning gains do not increase fact storage, citing the model&\#x27;s AA-Omniscience score as consistent with its parameter count. The community awaits independent benchmark validation.

**Tags**: `#eval`, `#orchestration`

---

<a id="item-agent-engineer-3"></a>
### [TuringSpace 交互式 CAPTCHA 基准发布](https://huggingface.co/papers/2611.25387) ⭐️ 6.0/10

2026年11月20日Hugging Face每日论文发布TuringSpace基准，这是一个用于评估多模态大语言模型空间智能与交互动作能力的可扩展交互式CAPTCHA合成网页环境。该基准包含125个覆盖5类空间能力的任务，所有任务均配套实例生成器、检查器与预言机，支持自动生成评估实例与结果校验，同时可作为可扩展的训练 gym 使用。目前该基准未公开具体任务的模型性能表现数据，面向需要评估模型空间交互推理能力的多模态大模型、智能体评估系统研发团队。

rss · Hugging Face Daily Papers · Nov 20, 00:00

**「为什么重要」** 该基准填补了现有CAPTCHA测试多已被破解、少涉及空间能力，以及现有空间推理基准极少要求交互动作的空白，为相关领域提供了可自动生成实例、同时支持评估与训练的标准化工具。但其实际评估效果、对模型空间能力的提升作用尚未有公开性能数据验证，也未成为行业通用标准。

**「可关注」** 可关注：该基准的程序化任务生成、内置检查器与预言机设计，为构建可扩展的交互式智能体评估与训练环境提供了可参考的实现范式。

**Tags**: `#eval`

---

<a id="item-agent-engineer-4"></a>
### [AltRA-Test 支持 LLM 裁判替代人类标注](https://huggingface.co/papers/2611.26073) ⭐️ 6.0/10

2026-11-20，Hugging Face Daily Papers 收录论文《AltRA-Test: An Alternative Annotator Test for LLM Judges Without Shared Annotators》。该论文提出 AltRA-Test，一种基于 bootstrap 的统计检验方法，用于在大型标注场景中判断用 LLM 裁判替代人类标注者是否统计上合理。相比此前 Alt-Test 要求所有项目由相同标注者标注，AltRA-Test 允许项目由不同标注者子集标注：通过重采样项目、为每个项目抽取 k 个人类标注并替换其中一个为 LLM 标注，生成配对的全人类与混合标注进行比较。该方法针对 eval 场景，目前无社区评论。

rss · Hugging Face Daily Papers · Nov 20, 00:00

**「为什么重要」** 该工作填补了 LLM 裁判评估方法论中的一项空白：在非重叠标注者的大规模标注场景中，提供了统计上合理的替代验证框架。对于构建基于 LLM 裁判的 agent 评估流水线的工程师，这提供了一种可量化的决策依据，但论文影响范围相对有限，尚未有社区验证。

**「可关注」** 可关注：当标注流水线中不同项目由不同标注者处理时，AltRA-Test 的 bootstrap 重采样策略提供了一种统计检验替代 LLM 裁判可行性的思路，但需注意其假设条件与实现复杂度。

**Tags**: `#eval`

---

<a id="item-agent-engineer-5"></a>
### [Fragments：代码质量降多智能体审查成本](https://martinfowler.com/fragments/2026-11-20.html) ⭐️ 6.0/10

2026年11月20日Martin Fowler发布的Fragments摘要了CodeScene的一项实验：Marcus Borg在246个开源仓库的465个PR上测试了3个LLM参与的5智能体审查修复流水线，发现CodeHealth评分2.8的典型不健康PR相比评分9.7的典型健康PR，token成本高22%-35%；其中Complex Method、Complex Conditional是推高审查成本的核心代码异味。

rss · Martin Fowler · Nov 20, 18:38

**「为什么重要」** 该实验为多智能体代码审查场景的token成本优化提供了可量化的基线，明确的高成本代码异味类型可直接指导PR治理和审查流水线的输入优化，对控制coding agent的运营成本有直接参考价值。

**「可关注」** 可关注：CodeScene标记的Complex Method、Complex Conditional两类代码异味会显著增加多智能体代码审查的token消耗，针对性优化可降低22%-35%的审查成本。

**Tags**: `#coding-agent`

---

<a id="item-agent-engineer-6"></a>
### [WeVisForensics 自演化多智能体检测框架](https://huggingface.co/papers/2611.21373) ⭐️ 5.5/10

2026年11月20日Hugging Face Daily Papers收录论文《WeVisForensics: Self-Evolving Agent for Omni AI-Generated Video Detection》，提出自演化多智能体框架WeVisForensics：主调查智能体协调覆盖视觉、音频线索的取证检查子智能体库，可自主选择检查的伪影类型、时间窗口与终止时机。当前公开摘录内容不完整，未提供性能指标、具体实现细节等可验证信息，也未明确适用范围是否具备通用性。

rss · Hugging Face Daily Papers · Nov 20, 00:00

**「为什么重要」** 该工作提出的自适应主智能体协调专业子智能体、子智能体库自演化的编排模式，与现有固定多智能体流程、单次链式推理的AI生成视频检测方案形成差异，对智能体编排设计有参考价值。但当前摘录内容截断，实际检测效果、适用场景等关键信息尚未公开，实际影响待验证。

**「可关注」** 可关注：主智能体自主决策检查维度、时间窗口与终止时机的自适应编排设计，以及子智能体库随交互自演化的机制，但需等待完整论文公开验证实际落地效果。

**Tags**: `#orchestration`

---

## AI Daily

<a id="item-ai-daily-1"></a>
### [Anthropic IPO 完成 总募资约1195亿美元](https://www.anthropic.com/news/ipo-close) ⭐️ 9.8/10

Anthropic 官方宣布首次公开募股（IPO）完成，共发行 11.27 亿股 A 类普通股，发行价每股 83 美元，包含承销商全额行权的 1.47 亿股额外购股权；IPO 总募资约 935 亿美元，其中 Anthropic 获得约 916 亿美元，剩余为售股股东所得。同步完成向 AMD、Broadcom、Google、Micron、Microsoft、NVIDIA、TSMC Partners 的 3.13 亿股 Class N 普通股私募，募资约 260 亿美元，该部分股份未依据《1933 年证券法》注册。A 类普通股于 2026 年 11 月 19 日在纳斯达克全球精选市场挂牌，交易代码为 ANT。

rss · Anthropic News · Nov 20, 00:00

**「为什么重要」** 这是 AI 主流实验室迄今规模最大的资本动作，战略投资者覆盖核心算力、芯片厂商，反映行业对 AI 基础设施的持续重投入。

**「可关注」** 可关注：Anthropic 上市后股权结构包含多家算力巨头战略持股，后续算力合作优先级可能变化。

**Tags**: `#lab`, `#industry`

---

<a id="item-ai-daily-2"></a>
### [OpenAI 推出对抗性蒸馏分层防护](https://openai.com/index/combatting-adversarial-distillation) ⭐️ 8.8/10

OpenAI 于 2026 年 11 月 20 日发布对抗对抗性蒸馏的分层防护方案。该方案整合模型训练、安全防护、攻击检测与执法处置四层能力，目标为阻止未授权方通过对抗性蒸馏提取模型核心能力。官方暂未披露方案的具体技术细节与落地效果。

rss · OpenAI Blog · Nov 20, 10:00

**「为什么重要」** 对抗性蒸馏是当前大模型能力泄露的高风险攻击路径，该方案是头部实验室首次公开的系统性分层防护框架，为行业模型安全防护提供了可参考的官方思路。

**「可关注」** 可关注：OpenAI 将模型防护拆分为训练、安全防护、检测、执法四层的设计思路，后续可对照自身模型安全体系做能力缺口梳理。

**Tags**: `#lab`, `#model`, `#policy`

---

<a id="item-ai-daily-3"></a>
### [OpenAI 发布 MedChemBench](https://openai.com/index/introducing-medchembench) ⭐️ 7.8/10

OpenAI 官方发布新基准 MedChemBench，用于评估 AI 模型在早期药物发现中的三项核心能力，涵盖分子结构解读、实验证据推理、化合物筛选。目前未公开该基准与现有同类工具的差异。

rss · OpenAI Blog · Nov 20, 00:00

**「为什么重要」** 该基准为行业衡量 AI 在早期药物发现场景的实用能力提供了统一评估框架，填补了相关细分维度的评估空白。

**「可关注」** 可关注：可对照 MedChemBench 的评估维度，排查自身模型在药物发现相关任务上的能力短板。

**Tags**: `#eval`, `#lab`, `#industry`

---

<a id="item-ai-daily-4"></a>
### [Agent Anomaly Detection 支持跨云监控](https://developers.googleblog.com/agent-anomaly-detection-safeguarding-agents-across-other-clouds/) ⭐️ 7.8/10

Google于2026年11月20日宣布将Agent Anomaly Detection扩展至私有预览阶段，新增对运行在AWS、Microsoft Foundry及本地基础设施的Agent的监控能力。该功能基于Agent的追踪和日志运行，无需访问Agent运行时，仅需遥测数据流入用户指定的Google Cloud项目即可完成分析，分析过程独立运行不会拖慢Agent性能。当前仅支持ADK for Python 2.12.0及以上版本构建的Agent接入，需配置指定环境变量开启遥测发送，Agent被发现后30分钟内即可出现在监控列表，支持手动或自动启用异常检测，检测结果仅会在Agent Anomaly Detection控制台展示。

rss · Google Developers AI · Nov 20, 00:00

**「为什么重要」** 此前Agent Anomaly Detection仅支持监控Google Cloud环境内的Agent，此次扩展填补了跨云、本地部署Agent的行为异常检测空白，无需改造Agent运行时即可接入，降低了多环境部署的监控成本。

**「可关注」** 可关注：ADK for Python 2.12.0及以上版本构建的Agent，仅需配置4项指定环境变量并开启ADK的Google Cloud导出器，即可将遥测发送至Google Cloud项目接入该监控能力，分析过程独立运行不影响Agent性能。

**Tags**: `#product`, `#industry`, `#Google`, `#monitoring`

---

<a id="item-ai-daily-5"></a>
### [上海AI Lab开源Sage S2.1](https://mp.weixin.qq.com/s?__biz=MzA3MzI4MjgzMw==&amp;mid=2651075493&amp;idx=3&amp;sn=63643451e794a6d8ac3dbb423d7f460d) ⭐️ 5.0/10

上海AI Lab联合复旦大学、中国科学院软件研究所等多家机构发布Sage S2.1 Flash技术报告，开源总参数量320B的混合专家模型，披露完整训练流程与技术细节。该模型在四项智能体基准上达到SOTA，探索科学多模态感知融入通用智能体的方向，支持文本、图像、科学数据统一处理，可完成分子与光谱读懂、工具调用、专业软件操作等任务，示例中能从12487张CT图像重建三维骨骼模型。需注意，该内容为机器之心的二手科技媒体报道，未附上海AI Lab官方发布的一手链接，相关技术细节仅来自该报道。

rss · 机器之心 · Nov 20, 03:58

**「为什么重要」** 该报告首次系统披露320B参数MoE通用智能体的完整训练流程，同时探索科学多模态能力融入通用智能体的路径，为相关领域研究提供了可参考的开源技术方案。

**「可关注」** 可关注：其320B MoE架构通过动态专家路由控制推理计算量，结合稀疏注意力与线性注意力支持长上下文处理，模型主干可在共享上下文中处理文本、图像和科学数据表示，为复杂推理与多步骤任务执行提供基础，也为进一步接入科学专用模态奠定了架构基础。

**Tags**: `#model`, `#lab`, `#open-source`, `#eval`

---

## AI Deals

<a id="item-ai-deals-1"></a>
### [Epic 本周限免两款游戏](https://www.appinn.com/eggs-261120/) ⭐️ 8.0/10

你看到的内容可能由第三方 AI 基于小众软件文章提炼总结而成，可能与原文真实意图存在偏差。不代表小众软件观点和立场。请点击链接阅读原文细致比对和校验。Epic平台本周（11月20日至11月26日）限时免费送出两款游戏：电脑端可领《深渊之印 / Mark of the Deep》，手机端可领《Lonesome Village》，两款游戏均支持中文，需前往Epic对应商店页面领取。

rss · 小众软件 · Nov 20, 07:21

**「可关注」** 可关注：本次Epic限免游戏按平台区分发放，PC端与移动端需分别进入对应商店页面领取。

**Tags**: `#limited-free`, `#promo`, `#game`

---

<a id="item-ai-deals-2"></a>
### [greatai Review 上线 开源非营利可领免费审查](https://www.producthunt.com/products/greatai-review) ⭐️ 5.0/10

Product Hunt 上线的 greatai 面向开源项目与非营利组织提供免费的 AI 加人工代码审查服务，目前未明确服务有效期、领取方式、额度限制等关键规则，也未公布截止时间。

rss · Product Hunt · Nov 20, 04:56

**「为什么重要」** 当前该服务仅面向开源项目与非营利组织开放，若符合资质可留意后续规则更新，暂无需额外成本。

**「可关注」** 可关注：该服务仅面向开源项目与非营利组织开放，具体领取规则尚未明确，需等待官方补充细节。

**Tags**: `#free-tier`, `#promo`, `#limited-free`

---