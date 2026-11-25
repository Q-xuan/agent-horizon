---
layout: default
title: "Horizon Summary: 2026-11-26 (EN)"
date: 2026-11-26
lang: en
---

> From 183 items, 13 important content pieces were selected

---

**Agent Harness Architecture**
1. [Mastra Core 1.86.0 发布](#item-harness-arch-1) ⭐️ 8.8/10
2. [pydantic-ai v2.75.0 发布](#item-harness-arch-2) ⭐️ 7.8/10
3. [Cloudflare Search for Agents 上线](#item-harness-arch-3) ⭐️ 5.8/10

**AI Agent Engineer**
1. [Inkling 2 Mini 单卡推理优化](#item-agent-engineer-1) ⭐️ 8.8/10
2. [RLVB 训练 Agent 避免过早作答](#item-agent-engineer-2) ⭐️ 7.0/10
3. [HF 每日论文：NightWatch 框架](#item-agent-engineer-3) ⭐️ 7.0/10
4. [HF 每日论文：具身智能镜像基准发布](#item-agent-engineer-4) ⭐️ 7.0/10
5. [ICLWorld 跨域智能体 ICL 基准发布](#item-agent-engineer-5) ⭐️ 7.0/10
6. [Ai2 发布科研 AI Agent 边界报告](#item-agent-engineer-6) ⭐️ 6.8/10
7. [IBM 开源 CUGA 语音代理案例](#item-agent-engineer-7) ⭐️ 6.8/10
8. [Simon Willison 总结 LLM 三阶段跃迁](#item-agent-engineer-8) ⭐️ 6.0/10

**AI Daily**
1. [GitHub 发布应用现代化证据指南](#item-ai-daily-1) ⭐️ 6.3/10
2. [Gemini 4 Neon 登顶 LiveBench 长流程榜](#item-ai-daily-2) ⭐️ 5.5/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [Mastra Core 1.86.0 发布](https://github.com/mastra-ai/mastra/releases/tag/%40mastra/core%401.86.0) ⭐️ 8.8/10

Mastra Core 1.86.0 发布，引入持久化事件工作流、实验性 Knowledge 导入器基础设施、原生 durable Agent 执行引擎和频道优先聊天集成。\`startExperimentAsync\(\)\` 支持 \`durable: true\`，实验变为事件化工作流，worker 崩溃或重新部署后，pubsub 重投递未确认项，另一 worker 继续处理；新增 \`interrupted\` 线程运行状态，durable agent 被 \`mastra.shutdown\(\)\` 中断时不再显示 \`failed\`。Knowledge 导入器提供端到端契约、执行入口和持久化记账，支持 in-memory、LibSQL 和 Postgres，具备租约、重放保护和结算/修复语义；\`createChannelTools\(\)\` 和 \`@mastra/slack\` 的 \`createSlackTools\(\)\` 提供频道读写能力。\`durable.executionEngine\` 现为默认值，旧版 \`executionEngine: &\#x27;durable&\#x27;\` 重命名为 \`executionEngine: &\#x27;default&\#x27;\`。

github · PaulieScanlon · Nov 25, 10:00

**「设计要点」** Durable 实验和 Agent 执行基于事件化工作流，worker 崩溃或重新部署后，pubsub 重投递未确认项，另一 worker 继续处理。Knowledge 导入器在同一数据库和命名空间下维护绑定、节点映射、游标状态和运行记录，与页面写入共享事务；\`knowledge.storage.transaction\(\)\` 支持 \`deadlineAt\` 选项，Postgres 适配器会统计连接等待、语句执行和锁等待时间。

**「改了什么」** 核心新增 durable 实验、Knowledge 导入器基础设施和 durable Agent 执行引擎默认值。\`get\_process\_output\` 移除 \`wait: true\`，\`@mastra/connect\` 替换为 \`ConnectEvents\` 迭代器 API，\`@mastra/mcp-apps-components\` 将 \`projectId\` 重命名为 \`project\`，\`@mastra/playground-ui\` traces 组件发生重大破坏性 API 变更。

**Tags**: `#runtime`, `#memory`

---

<a id="item-harness-arch-2"></a>
### [pydantic-ai v2.75.0 发布](https://github.com/pydantic/pydantic-ai/releases/tag/v2.75.0) ⭐️ 7.8/10

pydantic-ai v2.75.0 发布，重构工作区文件权限处理并调整持久化运行行为。低于 \`operator\` 权限的文件不再注入 \`RepoContext\`、\`Skills\` 和 \`Memory\` 指令，新增 \`lowest\_authority\_under\` 参数。持久化运行启动时记录额外 \`realpath\` 调用，需完成在途运行或使用工作器版本化。Gemini 思维令牌现计入 \`OpenAIChatModel\` 输出统计，\`UsageLimits\` 阈值提前触发。

github · dsfaccini · Nov 25, 18:21

**「设计要点」** 工作区权限通过 \`lowest\_authority\_under\` 参数控制核心上下文组件的指令注入，低于阈值文件转为框架数据或工具暴露。持久化运行在启动时记录 \`realpath\` 工作区调用，跨引擎（Temporal、DBOS、Prefect）存在在途运行兼容性风险。能力指令随 \`authority\` 属性下放，从系统提示移至用户通道框架数据。

**「改了什么」** \`RepoContext\`、\`Skills\` 和 \`Memory\` 停止将低于 \`operator\` 权限的工作区文件内容注入指令，改为通过工具或框架数据提供。\`FallbackModel\` 和 \`ModelFallback\` 现默认对空响应和不合法 OpenAI 响应执行回退，而非抛出 \`UnexpectedModelBehavior\`。持久化运行启动时记录额外 \`realpath\` 工作区调用，跨版本升级需完成在途运行或使用工作器版本化。

**Tags**: `#permissions`, `#memory`, `#tools`, `#runtime`

---

<a id="item-harness-arch-3"></a>
### [Cloudflare Search for Agents 上线](https://blog.cloudflare.com/search-for-agents/) ⭐️ 5.8/10

Cloudflare launched Search for Agents, a dashboard toggle that automatically provisions AI Search instances for user zones. The service crawls and indexes website content, then exposes a search API at \`/.well-known/search\` under the user&\#x27;s domain. Agents discover the endpoint via HTML \`&lt;meta&gt;\` tags or YAML front matter, and query it using GET or the new HTTP QUERY method \(RFC 10008\). Results return as Markdown rather than generated answers. The feature is available to all customers including Free tier with limits.

rss · Cloudflare AI · Nov 25, 14:00

**「设计要点」** The feature operates at Cloudflare&\#x27;s network level, automatically provisioning AI Search instances and injecting discoverability metadata into HTML responses or Markdown front matter. Search behavior is subject to existing zone-level controls including bot management, AI Crawl Control, and WAF configurations.

**「改了什么」** Previously, users manually created AI Search instances and integrated search endpoints. Search for Agents automates instance creation, indexing, and endpoint advertisement via standard web mechanisms, eliminating manual infrastructure setup.

**Tags**: `#tools`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [Inkling 2 Mini 单卡推理优化](https://huggingface.co/blog/inkling-2-mini-inference-hillclimb) ⭐️ 8.8/10

Hugging Face 2026年11月25日发布博客，公布 Inkling 2 Mini 在单张 NVIDIA RTX PRO 6000 96GB 上的推理优化结果。该模型为 26B 总参数、3B 激活的循环 MoE 架构，含 24 物理层（中间 12 层循环 3 次，单 token 经过 48 层），采用混合 NVFP4/MXFP8 量化，内置 DSpark 草稿器支持推测解码；官方现有服务配方针对 sm100 架构的 B200、GB300 GPU，未覆盖 sm120 架构的 RTX PRO 6000。经 coding agent 自动调优，单用户解码速度从基线 136 tok/s 提升至 190.6 tok/s（+40%），8 用户聚合吞吐从 ~570 tok/s 提升至 716 tok/s（+26%），贪婪输出与无推测场景字节级一致，长上下文 needle 检索通过 250K token 测试，最优配置已部署为 Hugging Face 推理端点，所有实验日志、脚本与原始测量数据公开于 NielsRogge/inkling-2-mini-hillclimb 仓库。

rss · Hugging Face Blog · Nov 25, 00:00

**「为什么重要」** Inkling 2 Mini 在 Artificial Analysis Intelligence Index v5 及 32/48 个基准测试中优于 Gemma 4 31B、Qwen3.8-27B 等同参数量级开源模型，适配编码、工具调用与推理任务；本次优化验证了单张 sm120 架构的 RTX PRO 6000 即可跑出接近内存带宽天花板的推理吞吐，为本地 coding agent 部署提供了可复现的配置与实验范式。

**「可关注」** 可关注：Inkling 2 Mini 的 DSpark 推测解码需固定 7 个草稿 token（匹配模型块大小限制），温度 1.0 下概率采样比贪婪采样快 11%，sm120 架构卡的 kernel 兼容性需优先于调参验证。

**Tags**: `#coding-agent`, `#eval`, `#harness`

---

<a id="item-agent-engineer-2"></a>
### [RLVB 训练 Agent 避免过早作答](https://huggingface.co/papers/2611.32884) ⭐️ 7.0/10

一篇 arXiv 预印本提出强化学习可验证信念（RLVB）方法，解决长任务 Agent 过早锁定答案的“懒惰”问题。评估显示，Agent 常在仍列出多个可能答案时即提交结论，而仅用结局奖励无法区分幸运猜测与有证据支撑的答案。训练阶段，模拟器计算每一步的精确后验分布，在答案仍不确定时奖励继续取证，在证据充分时奖励最终提交。该方法面向长时程任务的行为改进。

rss · Hugging Face Daily Papers · Nov 25, 00:00

**「为什么重要」** 该研究直接针对长任务 Agent 的常见失效模式，提供了可量化的训练信号替代方案。目前仅见预印本，尚未有生产环境验证或官方发布。

**「可关注」** 训练阶段可用模拟器计算精确后验，在证据不足时奖励继续取证、证据充分时奖励提交，以替代仅靠结局奖励导致的过早作答。

**Tags**: `#coding-agent`, `#eval`

---

<a id="item-agent-engineer-3"></a>
### [HF 每日论文：NightWatch 框架](https://huggingface.co/papers/2611.28947) ⭐️ 7.0/10

2026年11月25日Hugging Face每日论文收录论文《Don&\#x27;t Sleep, Keep Watch: Proactive Perception for Computer-Use Agents》，提出即插即用框架NightWatch，可为基于视觉语言模型（VLM）的计算机使用代理（CUA）提供连续、时间锚定的感知能力，无需修改代理的模型、提示词或动作空间。该框架针对现有CUA依赖离散环境快照、VLM推理延迟导致的感知-动作间隙问题设计，配套轻量模型NightWatch-0.8B。当前公开内容为论文摘要截断版，来源为二次聚合器，非原始论文全文，该论文在Hugging Face平台获得84次点赞。影响群体为构建CUA及代理harness的工程师。

rss · Hugging Face Daily Papers · Nov 25, 00:00

**「为什么重要」** 已发生的变化是：动态环境下的感知-动作间隙是CUA的明确工程痛点，NightWatch的即插即用设计无需改动代理核心组件，对相关工程师有直接参考价值。尚未证实的影响包括：论文完整实验数据、实际落地成本、跨场景适配效果均未公开。

**「可关注」** 可关注：现有CUA的感知-动作间隙由离散快照和VLM延迟共同导致，NightWatch的即插即用方案无需改动代理核心组件，但完整实验细节与落地成本尚未公开。

**Tags**: `#coding-agent`, `#harness`

---

<a id="item-agent-engineer-4"></a>
### [HF 每日论文：具身智能镜像基准发布](https://huggingface.co/papers/2611.33010) ⭐️ 7.0/10

2026年11月25日Hugging Face每日论文收录研究《Embodied AI Fails the Mirror Test: How a Simple Mirror Breaks Robot Policies》，该研究推出基于RoboDojo构建的可复现RoboDojo-Mirror基准，保留原任务目标、成功判定标准与策略检查点，设置无镜子基线、单镜、双镜、镜像桌面共4种测试场景，覆盖VLA、世界动作模型、智能体策略共5类机器人操作策略。测试结果显示所有镜像场景下策略聚合成功率均下降，平均降幅10.8至56.7个百分点，最高降幅达62.5个百分点，该基准为具身智能体鲁棒性评估提供新的标准化测试用例，当前影响限于具身AI子领域，该论文当前获得27次Hugging Face每日论文点赞。

rss · Hugging Face Daily Papers · Nov 25, 00:00

**「为什么重要」** 该研究首次系统量化了镜子反射场景对主流机器人操作策略的鲁棒性影响，填补了具身智能体非理想视觉场景测试的空白，为相关策略的鲁棒性优化提供了可复现的评估标尺，不过当前影响仍局限于具身AI子领域，尚未延伸至通用编码智能体评估。

**「可关注」** 可关注：RoboDojo-Mirror基准已公开可复现，若团队涉及具身智能体策略评估，可将其纳入视觉干扰场景的鲁棒性测试集。

**Tags**: `#eval`

---

<a id="item-agent-engineer-5"></a>
### [ICLWorld 跨域智能体 ICL 基准发布](https://huggingface.co/papers/2611.32649) ⭐️ 7.0/10

2026 年 11 月 25 日，Hugging Face Daily Papers 发布 preprint ICLWorld，提出跨数字与物理世界的在线智能体上下文学习（ICL）基准。该基准覆盖计算机使用与机器人使用两类场景，配套 UIverse 统一评估工具包，将各类环境统一转化为用户界面接口。研究团队构建 30 个环境、录制 630 段演示视频（累计 10 小时以上），并设计 160 个含定制化、常反直觉规则的任务。现有智能体评估多为离线、依赖文本或静态图像，存在训练数据污染风险，且机器人评估常限于方法级消融，ICLWorld 试图填补这一空白。

rss · Hugging Face Daily Papers · Nov 25, 00:00

**「为什么重要」** 现有智能体评估工具普遍存在离线、易受训练数据污染、仅覆盖数字或仅覆盖物理世界的问题。ICLWorld 提供在线、跨域、含标准化接口的评估资源，直接针对 coding agent 与机器人智能体的 ICL 能力测试缺口。

**「可关注」** 可关注：UIverse 将异构环境统一为 UI 接口的设计，可能简化跨数字/物理智能体评估的 harness 接入成本。

**Tags**: `#eval`, `#harness`, `#coding-agent`

---

<a id="item-agent-engineer-6"></a>
### [Ai2 发布科研 AI Agent 边界报告](https://huggingface.co/blog/allenai/where-scientists-draw-the-line-on-ai-agents) ⭐️ 6.8/10

Ai2 发布基于 17 位科学家访谈的科研 AI Agent 责任边界报告。报告提出科学信任五维度——验证、隐私、客观性、问责、透明——并强调科学家应参与决定 Agent 承担的研究任务与评估标准。受访者对 AI 辅助科研划出不同红线：有人拒绝 AI 生成研究创意，有人担忧自动化削弱专业能力学习。报告建议构建参与式基准，让科学家定义 Agent 应遵守的研究规范，但相关评估框架仍处于提案阶段。

rss · Hugging Face Blog · Nov 25, 18:52

**「为什么重要」** 报告首次将科研伦理规范转化为对 AI Agent 的具体技术要求，为高 stakes 科研场景的权限控制、过程可追溯性和结果可复现性设计提供参照。其提出的五维度信任框架直接影响 Agent 工程师在可观测性、文件访问边界和任务授权方面的设计决策。

**「可关注」** 可关注：科研 Agent 的评估需超越任务完成率，纳入文件访问范围、方法透明度及对矛盾证据的处理能力，这些维度正成为高 stakes 科研场景的核心约束条件。

**Tags**: `#permissions`, `#observability`, `#eval`

---

<a id="item-agent-engineer-7"></a>
### [IBM 开源 CUGA 语音代理案例](https://huggingface.co/blog/ibm-research/an-indic-voice-agent-with-cuga) ⭐️ 6.8/10

2026 年 11 月 25 日，Hugging Face Blog 发布 IBM Research 的 CUGA（Configurable Generalist Agent）开源 agent harness 案例，展示其用于印度区域语言（如印地语、泰米尔语）农业知识语音代理。该架构将语音转文本后送入 CUGA 文本大脑处理，再转回语音，CUGA 负责模型接线、工具管理、状态与 guardrails。文章指出默认英文嵌入模型在跨语言检索中静默失效，替换为 \`intfloat/multilingual-e5-large\` 后，单一英文文档即可服务多语言查询。CUGA 同时也是 AppWorld Benchmark 领先者，并与 IBM Bharat Core 关联以支持数据主权场景。

rss · Hugging Face Blog · Nov 25, 10:22

**「为什么重要」** 该案例将多语言语音代理的构建拆解为可审计、可替换的文本层与语音层，并把跨语言检索问题明确指向嵌入模型而非提示词工程。这为类似数字服务的快速原型与合规部署提供了可复现的工程路径。

**「可关注」** 可关注：CUGA 将语音代理解耦为文本大脑加 STT/TTS 薄层，开发者可先以纯文本完成 agent 逻辑与检索验证，再独立替换语音提供商；但需在调优任何提示词前验证嵌入模型是否覆盖目标语言，否则跨语言检索会静默返回错误结果。

**Tags**: `#harness`, `#eval`, `#orchestration`

---

<a id="item-agent-engineer-8"></a>
### [Simon Willison 总结 LLM 三阶段跃迁](https://simonwillison.net/2026/Nov/24/llm-inflection-points/) ⭐️ 6.0/10

Simon Willison 于 2026-11-24 发表 retrospective。他把过去 12 个月 LLM 与 coding agent 的能力跃迁归纳为三个节点。第一节点是 2025-11-24 Claude Opus 4.5 发布。作者称该模型让 Claude Code 的默认输出首次达到可用阈值。Claude Code 于 2025-02-24 随 Claude 3.7 Sonnet 发布，此时已运行 9 个月。同期 OpenAI 发布 GPT-5.1 Instant/Thinking/Codex/Codex-Max，Codex agent 可靠性随之提升。第二节点是 2026 年 6-7 月 Claude Fable 5 发布。该模型随后受美国出口管制有效封禁，直至 2026-07-01 才恢复可用。作者定义 &quot;Fable class models&quot; 为给定目标与工具即可蛮力求解的模型。当前他将其归类为 Claude Fable 5/5.1/5.2、Claude Opus 5.5、GPT-6 Astra 及 Gemini 4 Neon。第三节点是 2026 年 9-10 月。Opus 5.5 于 2026-09-22 发布。frontier LLMs 在 3D 建模与游戏开发上取得进展。作者记录 Opus 5.5 通过 12 小时 playtesting 重平衡 RTS 游戏并提升娱乐性的案例。文章未附可复现基准或代码级改进细节。

rss · Simon Willison · Nov 24, 23:02

**「为什么重要」** 该 retrospective 以一线使用者视角，将抽象能力跃迁锚定到具体产品发布时间与可观察行为变化。对 agent 工程师而言，这三个节点对应着从&quot;需要频繁修正&quot;到&quot;默认可用&quot;、从&quot;单轮求解&quot;到&quot;主动调用工具链&quot;、从&quot;生成内容&quot;到&quot;评估并优化体验&quot;的阈值跨越，可作为评估当前工具成熟度的参照系。

**「可关注」** 可关注：作者将 &quot;Fable class&quot; 定义为给定目标与工具即可蛮力求解的模型类别，这一分类标准可用来校准 agent 对 frontier model 的能力预期与工具设计边界。

**Tags**: `#coding-agent`, `#eval`, `#orchestration`

---

## AI Daily

<a id="item-ai-daily-1"></a>
### [GitHub 发布应用现代化证据指南](https://github.blog/ai-and-ml/github-copilot/how-to-choose-the-next-safe-step-in-application-modernization/) ⭐️ 6.3/10

GitHub 官方博客发布应用现代化实践指南，提出证据优先的可复用改造流程，并展示如何将该流程编码为 GitHub Copilot agent skill。作者在 4 个公开应用（涵盖小型 Node.js 游戏到大型 Java ERP 系统）上验证了该方法的可行性。改造决策按 disruptive 程度从低到高分为保留、升级、替换、包装、重写五级，同时配套 L0-L4 四级回归保护强度评级。流程要求先完成包含依赖清单、运行时 pin、外部契约等内容的证据盘点，再选择最小 disruptive 的改造方案，未验证的假设不得作为决策依据。

rss · GitHub Blog · Nov 25, 15:00

**「为什么重要」** 该指南将应用现代化的方案选择流程标准化，降低了团队决策的主观偏差，配套的 GitHub Copilot agent skill 可直接复用，减少了流程落地的重复成本。

**「可关注」** 可关注：改造方案优先选择 disruptive 程度最低的可行选项，仅当存在已证实的安全漏洞、依赖不兼容、架构无法满足需求等明确证据时，才升级到重写等更 disruptive 的方案。

**Tags**: `#product`, `#industry`

---

<a id="item-ai-daily-2"></a>
### [Gemini 4 Neon 登顶 LiveBench 长流程榜](https://mp.weixin.qq.com/s?__biz=MzI3MTA0MTk1MA==&amp;mid=2652745183&amp;idx=2&amp;sn=9e2398515e5d4f23adafd26dd399519e) ⭐️ 5.5/10

新智元11月25日报道称Gemini 4 Neon以87.4分登顶LiveBench 2.0长流程总榜，领先Claude Fable 5.2、GPT-6.2 Astra 2.5分，该榜单为10月重构的长流程评测，包含7个子项、471道题，Neon在浏览器操作、研究、编程、推理子项得分领先。该说法无官方一手来源佐证，且Neon在Artificial Analysis智力指数v5.0.1总榜仅排第三，单任务成本2.654美元，高于Astra的1.941美元。

rss · 新智元 · Nov 25, 09:40

**「为什么重要」** LiveBench 2.0聚焦长流程、重工具调用的智能体任务，Neon在该细分场景的领先表现，体现了不同模型在复杂智能体工作流上的能力分化，可为相关场景的模型选型提供参考。

**「可关注」** 可关注：长流程智能体场景的模型选型需结合具体评测维度与单任务成本综合评估，单一榜单的排名结果不具备全场景泛化性。

**Tags**: `#model`, `#eval`, `#industry`

---