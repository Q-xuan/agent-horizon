---
layout: default
title: "Horizon Summary: 2026-11-03 (ZH)"
date: 2026-11-03
lang: zh
---

> 从 197 条内容中筛选出 13 条重要资讯。

<nav id="ah-toc" class="ah-toc" aria-label="目录"><span class="ah-toc-title">目录</span><ul><li><a href="#sec-harness-arch"><span class="ah-toc-name">Harness 架构</span><span class="ah-toc-count">4条</span></a></li><li><a href="#sec-agent-engineer"><span class="ah-toc-name">Agent 工程师日报</span><span class="ah-toc-count">5条</span></a></li><li><a href="#sec-ai-daily"><span class="ah-toc-name">AI 日报</span><span class="ah-toc-count">4条</span></a></li></ul></nav>

---

**[Harness 架构](#sec-harness-arch)**
1. [Mastra v1.81.0 发布](#item-harness-arch-1) ⭐️ 8.8/10
2. [adk-go v2.7.0 发布](#item-harness-arch-2) ⭐️ 8.8/10
3. [vLLM v0.33.0rc3 发布候选](#item-harness-arch-3) ⭐️ 6.8/10
4. [Anthropic Agent Skills 公开发布](#item-harness-arch-4) ⭐️ 6.0/10

**[Agent 工程师日报](#sec-agent-engineer)**
1. [Legora 无观测法律 Agent 实践](#item-agent-engineer-1) ⭐️ 7.0/10
2. [SimpleLoRIF 识别微调安全退化数据](#item-agent-engineer-2) ⭐️ 7.0/10
3. [R²Orch 提出递归自博弈编排方案](#item-agent-engineer-3) ⭐️ 6.0/10
4. [HF 每日论文：CEPO 多智能体提示优化框架](#item-agent-engineer-4) ⭐️ 6.0/10
5. [CaPtain 开源后训练流水线发布](#item-agent-engineer-5) ⭐️ 6.0/10

**[AI 日报](#sec-ai-daily)**
1. [OpenAI 发布 LifeVal 基准](#item-ai-daily-1) ⭐️ 7.8/10
2. [Qodo 推出 Codex 官方审查插件](#item-ai-daily-2) ⭐️ 7.8/10
3. [Claude API Message Threads 公测上线](#item-ai-daily-3) ⭐️ 7.8/10
4. [OpenAI 推出 Grid Protectors Program](#item-ai-daily-4) ⭐️ 6.8/10

---

## Harness 架构
{: #sec-harness-arch .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-harness-arch" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-harness-arch-1"></a>
### [Mastra v1.81.0 发布](https://github.com/mastra-ai/mastra/releases/tag/%40mastra/core%401.81.0) ⭐️ 8.8/10

Mastra v1.81.0 发布，核心新增实验性存储支持的 MCP 任务，长运行工具/Agent/工作流可立即返回 task ID，跨实例轮询/应答/取消并重启恢复。后台任务扩展至非 Agent 所有者（如 MCP 服务器），支持 expiresAt/metadata 保留、per-owner 并发覆盖、onNoSlot: &\#x27;queue&\#x27; 排队恢复，存储适配器已更新持久化新字段。可观测性新增 outcome/stopReason 类型化字段、model/provider 导出及 TTFT 测量，支持 ClickHouse/DuckDB/Postgres 查询。认证附件下载限制 10 MiB 内写入 channel-attachments/（上限 100 MiB），工厂级沙箱按 factoryId 隔离凭证。

github · PaulieScanlon · 11月2日 12:33

**「设计要点」** 存储层统一支撑 MCP 任务持久化和后台任务状态保存，实现跨实例重启安全。可观测性字段贯穿全链路，沙箱环境按 factoryId 隔离凭证。

**「改了什么」** 新增 storage-backed MCP tasks 实验能力与后台任务非 Agent 所有者支持，新增 expiresAt/metadata 保留、per-owner 并发控制、onNoSlot: &\#x27;queue&\#x27; 排队恢复及 outcome/stopReason/TTFT 可观测性字段。同时移除 @mastra/core/network/vNext 等子路径、playground-ui 图表 API 及 factory boards 相关接口。

**标签**: `#mcp`, `#runtime`, `#tools`, `#memory`, `#observability`

---

<a id="item-harness-arch-2"></a>
### [adk-go v2.7.0 发布](https://github.com/google/adk-go/releases/tag/v2.7.0) ⭐️ 8.8/10

Google 发布 adk-go v2.7.0。该版本将 Anthropic Claude 作为一等公民模型加入（实验性），通过 \`model/anthropicmodel\` 支持流式、工具调用与 prompt caching；新增 \`tool/toolsearch\` 实现搜索门控工具发现，避免大型 MCP 目录污染每次请求上下文；引入实验性分类器 API \`exp/classifier\` 用于工作流路由。运行时默认开启 OpenTelemetry GenAI semantic conventions v2 遥测（breaking change），并将单次 invocation 模型调用预算默认设为 500 次，可通过 \`RunConfig.MaxLLMCalls\` 或 \`ADK\_MAX\_LLM\_CALLS\` 调整，\`-1\` 表示无限制。

github · wolo-lab · 11月2日 10:37

**「设计要点」** 运行时通过 \`RunConfig.MaxLLMCalls\` 在 invocation 层硬编码模型调用预算，默认 500 次。工具层新增 \`tool/toolsearch\` 包装器，将大型 MCP 目录的发现延迟到模型首步 \`search\_tools\` 调用之后，避免全量工具声明挤占上下文；MCP 会话在开启 \`Config.Auth\` 后按用户 credential 隔离，防止跨用户 403。

**「改了什么」** 相对上一版，v2.7.0 新增 Anthropic Claude 模型支持、搜索门控工具发现、实验性分类器 API 与模型调用预算。遥测默认迁移至 OpenTelemetry GenAI semantic conventions v2，可选指令占位符从缺失时渲染空字符串改为传播基础设施错误，且 Go 版本要求升至 1.26.10。

**标签**: `#runtime`, `#tools`, `#mcp`, `#planning`, `#prefix-cache`

---

<a id="item-harness-arch-3"></a>
### [vLLM v0.33.0rc3 发布候选](https://github.com/vllm-project/vllm/releases/tag/v0.33.0rc3) ⭐️ 6.8/10

vLLM v0.33.0rc3 发布候选，包含 927 个提交。该版本将依赖升级至 PyTorch 2.14.0 与 Triton 3.8.0，停止发布 CUDA 12.9 wheel 与镜像，仅提供 CUDA 13.0 制品。CUDA wheel 现与 libtorch ABI 稳定，新增 AWS EFA 镜像与 vllm/vllm 短名称镜像别名。API 层面新增/v1/decisions 端点，Rust frontend 修复长对话 HTTP 500 问题。

github · khluu · 11月2日 10:10

**「设计要点」** CUDA wheel 与 libtorch ABI 稳定，降低自定义集成兼容成本。Rust frontend 修复长对话 HTTP 500 并在启动时校验不支持的标志；新增 watchdog 转储卡死引擎与 worker 的栈轨迹；Mooncake transfer engine 的 EFA build 支持多节点 KV 传输。

**「改了什么」** 依赖升级至 PyTorch 2.14 与 Triton 3.8，停止 CUDA 12.9 支持，CUDA wheel 与 libtorch ABI 稳定。新增/v1/decisions 端点、output\_mode=&quot;derender&quot;及 token embeddings late chunking；Rust frontend 修复长对话稳定性；移除 Medusa、MLP speculator 及 legacy Ray compiled-graph executor，弃用--mamba-cache-mode、LM Format Enforcer 及--ir-op-priority，NIXL connector 需 NIXL 1.5+，暂停生成时请求返回 HTTP 503。

**标签**: `#runtime`

---

<a id="item-harness-arch-4"></a>
### [Anthropic Agent Skills 公开发布](https://github.com/anthropics/skills) ⭐️ 6.0/10

Anthropic 公开发布官方 Agent Skills 实现，位于 \`anthropics/skills\` 仓库。该机制动态加载包含指令、脚本与资源的文件夹，使 Claude 能以可重复方式完成专门任务，并参考 \`agentskills.io\` 标准。当前公开内容仅含概念描述，未披露具体代码路径或实现细节。

rss · GitHub Trending Daily · 11月2日 23:00

**标签**: `#tools`, `#runtime`

---

## Agent 工程师日报
{: #sec-agent-engineer .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-agent-engineer" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-agent-engineer-1"></a>
### [Legora 无观测法律 Agent 实践](https://latent.space/p/building_legal_agents_when_you_can_t_see_the_data_-_jacob_lauritzen_cto_of_legora/) ⭐️ 7.0/10

2026 年 11 月 2 日 Latent Space 发布播客，Legora CTO Jacob Lauritzen 分享客户数据隐私约束下无法观测 Agent 执行 trace 的法律 Agent 生产实践。因数据属于律所客户，Legora 完全无法读取 Agent 的任何执行记录，团队通过模拟客户工作场景的仿真环境（类似强化学习“worlds”）完成测试，曾上线模型选择器，当前评估现有模型可完成约 60%法律工作，剩余部分需要更强模型；一次无改动的发布曾让引用准确率从 70%升至 99%。该实践面向在严格隐私限制下开发 Agent、设计 eval 与 harness 的工程团队。

rss · Latent Space · 11月2日 22:54

**「为什么重要」** 这是少有的面向严格隐私约束下法律 Agent 生产实践的公开分享，直接覆盖无 trace 可观测场景下的测试环境设计、模型选型与效果验证逻辑，对开发合规敏感领域 Agent 的工程师有直接参考价值。目前分享内容为访谈记录，未附带可复现的基准测试数据。

**「可关注」** 可关注：在无法获取原始执行 trace 的场景下，可通过 paraphrase 执行摘要将故障类型收敛到 10-20 类，同时用模拟客户工作流的仿真环境替代真实 trace 完成测试与 eval。

**标签**: `#observability`, `#eval`, `#harness`, `#permissions`, `#orchestration`

---

<a id="item-agent-engineer-2"></a>
### [SimpleLoRIF 识别微调安全退化数据](https://huggingface.co/papers/2610.37481) ⭐️ 7.0/10

2026 年 11 月 2 日发布的论文提出 SimpleLoRIF 可扩展梯度嵌入方法，仅对 Transformer 最后 4 个块做反向传播，即可处理百万级 规模的微调数据集，识别出看似无害但会导致大模型安全退化的训练样本；此前同类梯度归因方法仅适用于小规模分析场景，该方法实际落地效果尚未有公开验证。

rss · Hugging Face Daily Papers · 11月2日 00:00

**「为什么重要」** 该方法将梯度归因从小规模分析工具升级为可落地的全量后训练数据集过滤方案，为 Agent 模型的微调数据安全审计、训练数据筛选提供了可验证的技术路径，但目前仅公开论文摘要，实际工程适配效果尚未证实。

**「可关注」** 可关注 SimpleLoRIF 仅针对最后 4 层 Transformer 做反向传播的轻量化实现思路，以及其百万级 数据集的梯度嵌入效率表现，后续可验证是否适配自身微调流程的安全审计需求。

**标签**: `#eval`, `#harness`

---

<a id="item-agent-engineer-3"></a>
### [R²Orch 提出递归自博弈编排方案](https://huggingface.co/papers/2610.22740) ⭐️ 6.0/10

Hugging Face Daily Papers 于 2026-11-02 发布截断摘要，介绍 R²Orch 递归自博弈编排范式。该方案以内循环自博弈改进编排器、外循环优化内循环改进方式为核心，并引入 Recursive Learnability 训练目标，奖励 Proposer 选择在技能撤回时 rollout 仍产生不同结果的任务，以解决手工设计课程、优势崩溃及嘈杂技能评估问题。当前摘要未提供完整技术细节、实验验证与可复现性信息，实际工程效用尚不确定。

rss · Hugging Face Daily Papers · 11月2日 00:00

**「为什么重要」** 该研究针对智能体编排学习中的课程设计、评估信号等痛点提出新范式，但当前仅提供概念框架，尚未有实验数据支撑其有效性。

**「可关注」** 可关注：Recursive Learnability 目标通过奖励&\#x27;技能撤回后 rollout 结果分化&\#x27;的任务选择，可能为编排器评估提供更稳定的训练信号，但需等待完整论文验证其在实际 harness 中的效果。

**标签**: `#orchestration`, `#eval`

---

<a id="item-agent-engineer-4"></a>
### [HF 每日论文：CEPO 多智能体提示优化框架](https://huggingface.co/papers/2610.34722) ⭐️ 6.0/10

2026 年 11 月 2 日 Hugging Face 每日论文收录 CEPO（协调器-执行器提示优化）框架，该框架面向多智能体系统提示优化场景，将提示拆分为共享协调器提示与智能体专属执行器提示，分别按角色对齐规则独立更新，底层搜索可由现有提示优化器承接。当前公开内容仅包含论文摘要，无性能评估数据、实现细节或已确认的开源发布信息，主要面向多智能体编排与 harness 设计的工程师群体。

rss · Hugging Face Daily Papers · 11月2日 00:00

**「为什么重要」** 该框架首次明确拆分多智能体系统中协调与执行的提示角色，为提示优化提供了可复用的结构范式，但实际效果与落地可行性需等待完整论文验证。

**「可关注」** 可关注：CEPO 的协调/执行提示分离结构是否可适配现有多智能体 harness 的提示管理流程。

**标签**: `#orchestration`, `#harness`, `#multi-agent`

---

<a id="item-agent-engineer-5"></a>
### [CaPtain 开源后训练流水线发布](https://huggingface.co/papers/2610.40799) ⭐️ 6.0/10

2026 年 11 月 2 日 Hugging Face Daily Papers 收录 CaPtain 相关论文，这是一款开源后训练流水线，可将小型开源视觉语言模型（VLM）转化为可用的 Code-as-Policy 机器人智能体，测试阶段无需依赖视觉语言动作模型（VLA）、闭源前沿模型或特权状态信息。当前仅公开论文摘要，无技术实现细节、性能指标与评估结果，适用场景相对狭窄。

rss · Hugging Face Daily Papers · 11月2日 00:00

**「为什么重要」** 它将大模型智能体通用的「监督微调+多轮强化学习」训练范式延伸到机器人操控的 Code-as-Policy 场景，但当前仅公开摘要级信息，无实证数据支撑效果，暂无法判断实际落地价值。

**「可关注」** 可关注：Code-as-Policy 范式尝试复用通用大模型智能体的后训练流程，但当前公开信息不足，暂无法评估其对现有机器人智能体训练栈的替代空间。

**标签**: `#coding-agent`

---

## AI 日报
{: #sec-ai-daily .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-daily" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-daily-1"></a>
### [OpenAI 发布 LifeVal 基准](https://openai.com/index/lifeval) ⭐️ 7.8/10

OpenAI 正式发布 LifeVal 基准测试，用于衡量 AI 系统在育儿、财务管理、处理政府文书等日常任务中的辅助表现，填补了现有评测多侧重专业场景、少覆盖生活实用场景的空白。

rss · OpenAI Blog · 11月2日 09:00

**「为什么重要」** 当前多数 AI 评测聚焦专业场景，LifeVal 首次系统覆盖日常实用任务评估维度，为衡量 AI 生活辅助能力提供了统一标尺。

**「可关注」** 可关注 LifeVal 的任务分类与评测设计，可参考其思路完善 coding agent 的生活类任务评估体系。

**标签**: `#eval`, `#lab`, `#product`

---

<a id="item-ai-daily-2"></a>
### [Qodo 推出 Codex 官方审查插件](https://openai.com/index/qodo-codex-plugin) ⭐️ 7.8/10

代码工具厂商 Qodo 发布 OpenAI Codex 官方插件，可将企业编码标准与代码库上下文嵌入 AI 代码审查流程。该插件支持开发者在提交拉取请求前，跨代码仓库捕获 P0 级严重问题。

rss · OpenAI Blog · 11月2日 00:00

**「为什么重要」** 该插件将企业私有编码规范与代码库上下文接入 Codex 审查链路，解决了 AI 代码审查难以适配企业自定义规则的问题，对关注代码审查工具落地的开发者有参考价值。

**「可关注」** 可关注：Qodo Codex 插件将企业编码规范与代码库上下文嵌入 PR 前审查流程，可降低 P0 级问题流入后续环节的概率。

**标签**: `#product`, `#industry`

---

<a id="item-ai-daily-3"></a>
### [Claude API Message Threads 公测上线](https://claude.com/resources/articles/message-threads) ⭐️ 7.8/10

Anthropic 面向 Claude Messages API 上线 Message Threads 公开测试版，代理每轮仅需发送新增消息而非完整对话历史。500k 至 1M token 的请求中位首字延迟（TTFT）降低约 35%。线程在内存中加密存储、不写入磁盘，5 分钟无请求后过期，需重新发送完整对话开启新线程，且 token 消耗保持不变。

rss · Claude Blog · 11月2日 00:00

**「为什么重要」** 长运行编码代理、计算机使用代理等场景的会话延迟随上下文增长快速上升，该功能提供可量化的优化路径，且已在多数 Claude Code 用户中默认启用，落地成本低。

**「可关注」** 可关注：Claude Messages API 新增 thread 参数，长会话场景下仅需每轮发送新增消息与上一轮响应 ID 即可降低首字延迟，线程过期后需重新发送完整对话开启新会话。

**标签**: `#product`, `#lab`, `#api`, `#performance`

---

<a id="item-ai-daily-4"></a>
### [OpenAI 推出 Grid Protectors Program](https://openai.com/index/grid-protectors-program) ⭐️ 6.8/10

OpenAI 于 2026 年 11 月 2 日宣布推出 Grid Protectors Program。该计划将与电力公司合作，保障未来 AI 计算园区的电网可靠性，同时保护消费者用电成本。当前公开信息未披露具体合作方、落地时间表及实施细节。

rss · OpenAI Blog · 11月2日 15:00

**「为什么重要」** AI 算力规模扩张对电网负荷的压力是行业普遍关注的问题，该计划是头部 AI 实验室主动对接电网侧的早期布局，可能影响后续 AI 基础设施的落地规则。

**「可关注」** 可关注：该计划后续披露的具体合作模式、电网适配技术标准，以及是否会对 AI 计算园区的电力采购规则产生影响。

**标签**: `#lab`, `#industry`, `#policy`

---