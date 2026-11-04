---
layout: default
title: "Horizon Summary: 2026-11-04 (ZH)"
date: 2026-11-04
lang: zh
---

> 从 176 条内容中筛选出 15 条重要资讯。

<nav id="ah-toc" class="ah-toc" aria-label="目录"><span class="ah-toc-title">目录</span><ul><li><a href="#sec-harness-arch"><span class="ah-toc-name">Harness 架构</span><span class="ah-toc-count">3条</span></a></li><li><a href="#sec-agent-engineer"><span class="ah-toc-name">Agent 工程师日报</span><span class="ah-toc-count">8条</span></a></li><li><a href="#sec-ai-daily"><span class="ah-toc-name">AI 日报</span><span class="ah-toc-count">3条</span></a></li><li><a href="#sec-ai-deals"><span class="ah-toc-name">AI 羊毛</span><span class="ah-toc-count">1条</span></a></li></ul></nav>

---

**[Harness 架构](#sec-harness-arch)**
1. [Cloudflare Agents 0.33.0 发布](#item-harness-arch-1) ⭐️ 8.8/10
2. [FastMCP v4.2.0a3 发布](#item-harness-arch-2) ⭐️ 6.8/10
3. [openai-agents-js v0.22.0-alpha.1 发布](#item-harness-arch-3) ⭐️ 6.8/10

**[Agent 工程师日报](#sec-agent-engineer)**
1. [datasette-apps 0.3a0 发布](#item-agent-engineer-1) ⭐️ 7.8/10
2. [Datasette-agent 0.5a0 发布](#item-agent-engineer-2) ⭐️ 7.8/10
3. [StateBench 长文档状态跟踪基准发布](#item-agent-engineer-3) ⭐️ 7.8/10
4. [ParetoSaddler 优化 Harness 质量-成本权衡](#item-agent-engineer-4) ⭐️ 7.0/10
5. [Mage-VL-Cowork 混合 CUA 方案](#item-agent-engineer-5) ⭐️ 7.0/10
6. [HF 论文：近零词嵌入致门控模型训练停滞](#item-agent-engineer-6) ⭐️ 7.0/10
7. [Palette 小模型适配设计语言幻灯片](#item-agent-engineer-7) ⭐️ 5.8/10
8. [Cognition 2026 年 11 月安全实践指南发布](#item-agent-engineer-8) ⭐️ 5.8/10

**[AI 日报](#sec-ai-daily)**
1. [OpenAI：Codex 加速实体工程工作流](#item-ai-daily-1) ⭐️ 6.8/10
2. [思科整合 OpenAI 模型强化企业安全](#item-ai-daily-2) ⭐️ 6.8/10
3. [Heimstaden 用 OpenAI 工具改欧洲物业](#item-ai-daily-3) ⭐️ 6.8/10

**[AI 羊毛](#sec-ai-deals)**
1. [Epic 免费领 13 款小游戏](#item-ai-deals-1) ⭐️ 8.0/10

---

## Harness 架构
{: #sec-harness-arch .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-harness-arch" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-harness-arch-1"></a>
### [Cloudflare Agents 0.33.0 发布](https://github.com/cloudflare/agents/releases/tag/agents%400.33.0) ⭐️ 8.8/10

Cloudflare Agents 0.33.0 发布，核心升级 PiHarness 至 Pi 1.5 运行时。存储层改为批量写入流式答案与工具输出，SQLite 上长答案存储事务减少约 27 倍，CPU 占用降低约四分之一，但崩溃最多丢失约 1 秒数据。调度器优化使 2,048 会话并发下吞吐量从 88 提升至 459 runs/sec。Pi 1.5 对话无法被 1.4 读取，部署不可回滚。新增 \`session.watch\(\)\`、\`session.continue\(\)\` 及 \`defaults.maxTurns\` 接口，同时移除 \`session.events\(\)\`、\`retry\(\)\` 和 \`parked\` 状态。

github · github-actions\[bot\] · 11月3日 13:14

**「设计要点」** PiHarness 采用事件驱动批处理架构，流式输出按秒批量持久化而非逐更新写入，大幅降低存储事务开销。调度器改为按提交聚合检查与会话状态窗口化，避免全量轮询，同时内存管理从复制改为追加，消除大负载堆膨胀。

**「改了什么」** Pi 运行时升级至 1.5，存储写入改为批量持久化，调度器取消逐提交全量会话检查。会话 API 替换为 \`session.watch\(\)\` 与 \`session.entries\(\)\`，新增 \`session.continue\(\)\` 和 \`defaults.maxTurns\`，移除 \`session.events\(\)\`、\`retry\(\)\` 及 \`parked\` 状态；工具模式构建改为依赖 \`@earendil-works/pi-schema\`，浏览器工具新增作用域锁与外部调用支持。

**标签**: `#runtime`, `#memory`, `#performance`

---

<a id="item-harness-arch-2"></a>
### [FastMCP v4.2.0a3 发布](https://github.com/PrefectHQ/fastmcp/releases/tag/v4.2.0a3) ⭐️ 6.8/10

这是 PrefectHQ 发布的 FastMCP v4.2.0a3 alpha 预发布版本，核心重构 skills 子系统，新增严格的 SkillsDirectoryProvider 启动验证、YAML allowed-tools 支持，同时为 4.1 版 skills 提供者添加弃用警告并预告 4.3 版本移除，还修复了代理发现缓存过期、OpenAPI schema 引用丢失、客户端连接恢复失败等 bug；skills 功能仍标记为实验性，本版本仅用于集成测试，非生产可用。

github · zzstoatzz · 11月3日 23:39

**「设计要点」** skills 子系统围绕 Skill、SkillCatalogProvider 与新增的 SkillsDirectoryProvider 重构，目录加载会在发布前校验每个 skill，旧 experimental\_skills 路径重定向到新提供者并拒绝子类以保留访问控制；ClientGroup 退出上下文后仍保留已知工具路由。

**「改了什么」** 相对上一版本，新增严格 SkillsDirectoryProvider 启动验证、YAML allowed-tools 支持，弃用 4.1 版 skills 提供者并预告 4.3 移除；修复代理发现缓存过期、OpenAPI schema 引用与显式 null 值保留、客户端连接恢复等 bug，skills 功能仍为实验性。

**标签**: `#tools`, `#permissions`, `#runtime`, `#mcp`

---

<a id="item-harness-arch-3"></a>
### [openai-agents-js v0.22.0-alpha.1 发布](https://github.com/openai/openai-agents-js/releases/tag/v0.22.0-alpha.1) ⭐️ 6.8/10

OpenAI 官方发布 JavaScript/TypeScript Agents SDK 的 alpha 版本 v0.22.0-alpha.1，核心新增内嵌 Codex harness 能力。该版本要求使用 Node.js 24 及其自带 npm 运行，提供 Linux x64、macOS Apple silicon、Windows x64 三平台的 starter 压缩包与对应 SHA-256 校验和，配置 OPENAI\_API\_KEY 后执行指定命令即可跑通示例。

github · markstuart-oai · 11月3日 15:36

**「改了什么」** 新增内嵌 Codex harness，同步发布三大主流平台的 starter 压缩包及校验文件，降低接入与验证门槛。

**标签**: `#harness`, `#openai-agents-sdk`, `#alpha-release`

---

## Agent 工程师日报
{: #sec-agent-engineer .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-agent-engineer" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-agent-engineer-1"></a>
### [datasette-apps 0.3a0 发布](https://github.com/datasette/datasette-apps/releases/tag/0.3a0) ⭐️ 7.8/10

2026 年 11 月 4 日，simonw 发布 datasette-apps 0.3a0 alpha 版本，主要优化 Datasette Agent 的应用创建与编辑能力。新增 app\_add\_stored\_queries、app\_remove\_stored\_queries 两个 agent 工具，用于管理应用可调用的存储查询，授予写查询前需用户审批；app\_create\(\)新增校验逻辑，会检查请求的存储查询是否存在且用户有查看权限，创建应用前也会要求用户审批写查询。同时支持在聊天消息中输入\#自动补全有权限的应用，应用工具结果新增相对路径字段，相关视图按钮与链接现在会在 Datasette Agent 面板中全屏打开应用。该版本最低依赖 Datasette 1.0a41，支持 Python 3.15，已移除 Python 3.10 支持。

github · simonw · 11月4日 00:29

**「为什么重要」** 该版本落地了 agent 工具的权限校验与写操作用户审批流程，为设计同类工具接口与 harness 安全模式提供了可参考的实现，但当前仅覆盖 Datasette 生态且为 alpha 版本，稳定性尚未得到广泛验证。

**「可关注」** 可关注：agent 工具对写操作的权限前置校验与用户审批流程的设计，以及工具结果返回相对路径供 agent 直接引用的实现方式。

**标签**: `#agent`, `#tools`, `#permissions`, `#harness`, `#datasette`

---

<a id="item-agent-engineer-2"></a>
### [Datasette-agent 0.5a0 发布](https://github.com/datasette/datasette-agent/releases/tag/0.5a0) ⭐️ 7.8/10

2026 年 11 月 3 日，simonw 发布 datasette-agent 0.5a0 alpha 版本，面向数据智能体开发、插件架构相关的工程师。本次更新新增会话级模型锁定、\#引用自动补全（带表 schema/存储查询上下文注入）、异步插件钩子扩展自定义引用类型、侧边栏渲染 Datasette 页面、停止按钮、会话后台运行等特性，同时修复系统提示未送达部分模型的 bug，移除\`datasette-agent-explore\`权限及相关页面。版本最低要求提升至 Python 3.11+，依赖\`datasette&gt;=1.0a41\`、\`datasette-llm&gt;=0.1a9\`、\`llm&gt;=0.37.1\`。

github · simonw · 11月3日 23:13

**「为什么重要」** 该版本针对数据场景 agent 的核心交互与扩展能力做了关键补全，会话级模型选择、引用上下文注入、异步插件钩子等特性对同类数据 agent 开发有直接参考价值，alpha 版本可提前验证兼容性。

**「可关注」** 可关注：该版本新增的\`register\_agent\_reference\_types\(\)\`异步插件钩子支持自定义\#引用类型的搜索、上下文注入逻辑，为扩展数据类 agent 的领域引用能力提供了官方插件入口。

**标签**: `#harness`, `#permissions`, `#observability`, `#coding-agent`

---

<a id="item-agent-engineer-3"></a>
### [StateBench 长文档状态跟踪基准发布](https://allenai.org/blog/statebench) ⭐️ 7.8/10

Allen AI 于 2026 年 11 月 3 日发布 StateBench 长文档状态跟踪基准，同步公开技术报告、数据集与代码，基准包含 4 个递进难度等级，覆盖从不可变赋值到带变量引用的有限状态更新问题。该基准测试了开源预训练模型、前沿大模型以及直接任务训练的模型在长序列状态跟踪上的表现，所有测试的开源预训练模型训练时未接触超过 64000 token 的上下文，测试输入长度远超该阈值，验证了循环与混合架构在长序列状态跟踪任务上的泛化优势。前沿模型 Gemini 3.8 Flash、Claude Opus 5.5、GPT-6 Sol 与 Luna 在更长输入下的高难度状态跟踪任务上准确率跌至 13%及以下。

rss · Allen AI · 11月3日 08:00

**「为什么重要」** 该基准填补了长上下文状态跟踪多难度等级测试的空白，此前同类测试多聚焦最高难度场景，无法区分不同架构在普通场景下的性能差异。相关结论可参考用于 Agent 记忆系统设计与长上下文模型选型，但尚未验证跨任务泛化效果。

**「可关注」** 可关注：循环与混合架构经直接任务训练后，在长序列状态跟踪任务上的泛化距离显著优于 Transformer；前沿大模型在长输入高难度状态更新场景下仍存在准确率骤降的问题。

**标签**: `#eval`, `#memory`

---

<a id="item-agent-engineer-4"></a>
### [ParetoSaddler 优化 Harness 质量-成本权衡](https://huggingface.co/papers/2611.02079) ⭐️ 7.0/10

2026-11-04，Hugging Face Daily Papers 报道 arXiv 预印本 2611.02079，提出 ParetoSaddler 方法。该方法将中间候选提升与最终部署选择解耦，解决现有 harness 优化在联合质量-成本优化时过早拒绝候选的问题。技术核心是：每轮迭代中，优化器更新父 harness 生成候选，通过重复执行比较两者，并使用 Bayesian bootstrap Pareto support 提升在质量或成本上显示可信进展的候选。该工作目前仅为预印本，内容被截断，无确认的生产工具，主要影响 harness 工程师与 coding-agent 开发者。

rss · Hugging Face Daily Papers · 11月4日 00:00

**「为什么重要」** ParetoSaddler 针对现有 harness 优化仅关注响应质量、难以处理质量-成本联合优化的痛点，提供了明确的技术框架。但该研究尚未发布正式版本，其实际效果与工程可用性仍需后续验证。

**「可关注」** 可关注：ParetoSaddler 通过分离中间提升与最终选择，用 Bayesian bootstrap Pareto support 处理多目标权衡，这为 harness 优化提供了新的技术路径，但当前仅为预印本，尚无生产工具。

**标签**: `#harness`, `#eval`, `#coding-agent`

---

<a id="item-agent-engineer-5"></a>
### [Mage-VL-Cowork 混合 CUA 方案](https://huggingface.co/papers/2610.40747) ⭐️ 7.0/10

2026 年 11 月 4 日 Hugging Face 每日论文收录一篇未同行评审预印本，提出 4B 参数混合计算机使用代理 Mage-VL-Cowork，通过涵盖 midtrain、SFT、RL 的渐进式 5 阶段课程，从通用多模态对齐检查点端到端训练。配套工具 Mage-CUA-Forge 用可复用的技能条件生成工作流和应用专属准备器替代逐任务代理构建，合成了 293806 个桌面与网页任务，覆盖 6915 个技能，将单任务重复支出降低 82.6%。研究未直接蒸馏默认教师模型，而是进化教师 harness 并实例化专用 CUA harness 以生成高质量代理轨迹。

rss · Hugging Face Daily Papers · 11月4日 00:00

**「为什么重要」** 这篇预印本提供了混合 CUA 端到端训练、大规模训练数据合成降本、harness 进化的具体可操作工程细节，对从事计算机使用代理开发、训练管线搭建、agent harness 优化的工程师有直接参考价值。需注意该内容为未同行评审预印本，相关结论尚未经社区复现验证。

**「可关注」** 可关注：技能条件化的可复用生成工作流可将单任务训练数据合成成本降低 82.6%，同时支撑 29 万级以上任务规模的合成。

**标签**: `#coding-agent`, `#harness`, `#orchestration`

---

<a id="item-agent-engineer-6"></a>
### [HF 论文：近零词嵌入致门控模型训练停滞](https://huggingface.co/papers/2611.04449) ⭐️ 7.0/10

2026 年 11 月 4 日 Hugging Face 每日论文收录一项实证研究，调研 291 个开源权重语言模型仓库的 280 个独立词嵌入表发现，52.6%的非独立门控及混合架构检查点（20/38 个）存在范数低于 10^-6 的可达输入词嵌入，权重绑定模型该比例为 0%。该故障可在预训练阶段因罕见/模板词元未获得输入梯度，配合 AdamW 权重衰减收缩非独立嵌入时触发，在 Mamba、Gated DeltaNet、xLSTM 等门控序列模型中会放大输入词嵌入梯度超 30 个数量级（最高达 35），导致训练静默停滞；Transformer 架构中非初始位置或 BOS 词元可规避该问题。该发现对训练或微调上述门控序列模型的工程师有直接参考价值。

rss · Hugging Face Daily Papers · 11月4日 00:00

**「为什么重要」** 该研究揭示了门控序列模型训练中此前未被充分记录的普遍静默故障模式，已证实会影响 Mamba、xLSTM 等 agent 领域常用高效架构的训练稳定性，尚未证实该模式对闭源商业模型的影响范围。

**「可关注」** 可关注：使用非独立门控/混合架构（如 Mamba、xLSTM）训练时，需排查输入词嵌入是否存在近零行，避免罕见/模板词元梯度为零叠加 AdamW 权重衰减触发训练停滞。

**标签**: `#coding-agent`, `#sequence-model-training`, `#failure-mode-analysis`, `#embedding-stability`

---

<a id="item-agent-engineer-7"></a>
### [Palette 小模型适配设计语言幻灯片](https://huggingface.co/blog/ibm-research/palette-deck-building) ⭐️ 5.8/10

2026 年 11 月 3 日 Hugging Face 博客发布 IBM Research 的 Palette 项目，尝试通过 LoRA 微调 20B 参数开源小模型，在用户自有设计语言下生成幻灯片，解决前沿模型风格固化、小模型生成质量差的问题。项目将生成流程拆分为设计师（输出结构化 JSON brief）和编码器（生成 pptxgenjs 代码）两个角色，用合成设计语言数据训练，编码器可并行处理单页代码生成使编码阶段速度提升 6–7 倍，搭配 harness 检查修复重叠、溢出等错误，在 PresentBench 的三个测试领域中两个排名第一。当前成果仅覆盖幻灯片生成场景，技术细节有限，对通用 coding agent 或工具链的参考价值待验证，适合需要私有化部署、定制设计语言幻灯片生成的团队。

rss · Hugging Face Blog · 11月3日 16:35

**「为什么重要」** 它验证了小模型在特定结构化生成任务上，通过合成数据+角色拆分+harness 检查修复的范式，可接近前沿模型输出质量，同时保留数据所有权，适配数据隐私和定制化需求；但当前仅验证幻灯片生成领域，通用性尚未证实。

**「可关注」** 可关注：布局类结构化生成任务可尝试拆分编辑判断与几何计算为独立角色并行处理，配合合成数据生成与检查修复 harness 提升小模型输出质量，LoRA 微调可降低实验成本。

**标签**: `#harness`, `#eval`

---

<a id="item-agent-engineer-8"></a>
### [Cognition 2026 年 11 月安全实践指南发布](https://cognition.ai/blog/practical-guide-to-security-november-2026) ⭐️ 5.8/10

2026 年 11 月 3 日，Devin 开发商 Cognition 发布安全实践指南，梳理了 2026 年 10 月下旬至 11 月初的多起安全事件，包括 10 月 29 日 Cursor 披露的恶意 Claude Code Cursor 扩展后门事件：该扩展通过自动更新传播，安装量低于 5000，其版本与 Open VSX 开放扩展 registry 的官方版本不一致，攻击者可能篡改了 Open VSX 下游的扩展发布流程。指南同时提及 Binance 63.4 亿美元被盗、PHP2Shell、GitLab 未授权远程代码执行等关键漏洞，给出企业分阶段的安全加固行动项，面向使用 AI 编码工具、云服务的开发团队。

rss · Cognition Blog · 11月3日 17:00

**「为什么重要」** 该指南由编码代理产品 Devin 的开发商 Cognition 发布，梳理的恶意 Claude Code Cursor 扩展后门事件属于直接面向开发者的编码工具供应链攻击，给出的开发环境加固建议覆盖了编码代理、编辑器扩展、MCP 服务器等常见攻击面，对使用 AI 编码工具的工程团队有直接参考价值。

**「可关注」** 可关注 编码工具扩展的供应链安全存在发布流程下游被篡改的风险，需对编辑器、AI 编码工具的扩展及 MCP 服务器做准入管控与自动更新延迟配置。

**标签**: `#security`, `#coding-agent`, `#permissions`

---

## AI 日报
{: #sec-ai-daily .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-daily" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-daily-1"></a>
### [OpenAI：Codex 加速实体工程工作流](https://openai.com/index/accelerating-engineering-for-the-physical-world) ⭐️ 6.8/10

2026 年 11 月 3 日，OpenAI 官方博客发布内容，展示 ChatGPT 与 Codex 在 CAD、PCB 设计、仿真等实体工程工作流中的应用，用于加速相关流程。该内容属于用例展示类发布，未提及新模型发布、政策调整或技术突破相关信息。

rss · OpenAI Blog · 11月3日 12:00

**「为什么重要」** 该博客是 OpenAI 官方公开的 Codex 非纯软件工程领域落地用例，为 coding agent 在实体工程等垂直场景的适配提供可参考的实践方向。

**「可关注」** 可关注：Codex 在 CAD、PCB 设计、仿真等实体工程工作流的落地用例与适配思路。

**标签**: `#lab`, `#product`, `#industry`

---

<a id="item-ai-daily-2"></a>
### [思科整合 OpenAI 模型强化企业安全](https://openai.com/index/cisco-cyber) ⭐️ 6.8/10

OpenAI 官方博客 2026 年 11 月 3 日发布案例研究，显示思科将自身网络智能与 OpenAI 模型结合，打造自适应企业安全防御方案。该方案旨在提升企业安全防护的响应效率与场景适配能力。

rss · OpenAI Blog · 11月3日 08:00

**「为什么重要」** 这是生成式 AI 在企业安全领域的可验证落地用例，为同类企业安全方案的开发提供参考路径。

**「可关注」** 可关注：思科网络智能与 OpenAI 模型结合的安全防御方案落地细节。

**标签**: `#product`, `#industry`, `#lab`

---

<a id="item-ai-daily-3"></a>
### [Heimstaden 用 OpenAI 工具改欧洲物业](https://openai.com/index/heimstaden) ⭐️ 6.8/10

OpenAI 官方博客宣布，欧洲住宅地产运营商 Heimstaden 已将 ChatGPT Enterprise 和 Codex 工具应用于其欧洲范围内的物业管理业务，目标是降低运营成本、提升员工工作能力。本次更新无新模型、政策或产品发布，属于行业应用案例。

rss · OpenAI Blog · 11月3日 08:00

**「为什么重要」** 这是 OpenAI 官方披露的其企业级产品在欧洲传统地产运营场景的应用实践，可参考 To B AI 工具在实体行业的应用路径。

**「可关注」** 可关注：企业级 AI 工具在传统地产运营场景的降本与员工能力提升应用方向。

**标签**: `#lab`, `#industry`, `#product`

---

## AI 羊毛
{: #sec-ai-deals .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-deals" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-deals-1"></a>
### [Epic 免费领 13 款小游戏](https://www.appinn.com/eggs-261103/) ⭐️ 8.0/10

你看到的内容可能由第三方 AI 基于小众软件文章提炼总结而成，可能与原文真实意图存在偏差。不代表小众软件观点和立场。请&lt;a href=&quot;https://www.appinn.com/eggs-261103/&quot; target=&quot;\_blank&quot;&gt;点击链接阅读原文&lt;/a&gt;细致比对和校验。&lt;br /&gt;&lt;br /&gt;Epic 商店正在限时免费发放 13 款 Yash Future Tech Solutions 出品的小游戏，类型涵盖射气球、横版闯关、赛车、解谜、数学问答等，领取后永久入库，无需立即下载。来源方已实际完成 13 款游戏的领取，合计花费 0 元。截止时间为北京时间 2026 年 11 月 9 日凌晨 2:30，登录 Epic 账户进入对应游戏页面点击获取即可领取；注意部分页面同时列有 Demo，需选择标注「免费」的游戏本体。

rss · 小众软件 · 11月3日 13:13

**「为什么重要」** 这批免费游戏均为永久入库，无需占用即时存储空间，适合想扩充休闲游戏库的用户；当前距截止时间不足一周，错过即无法再免费领取。

**「可关注」** 可关注：网页版领取时若遇到「与当前设备不兼容」提示仍可完成入库，下载安装可后续再进行。

**标签**: `#promo`, `#limited-free`

---