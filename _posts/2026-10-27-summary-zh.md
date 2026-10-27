---
layout: default
title: "Horizon Summary: 2026-10-27 (ZH)"
date: 2026-10-27
lang: zh
---

> 从 226 条内容中筛选出 18 条重要资讯。

<nav id="ah-toc" class="ah-toc" aria-label="目录"><span class="ah-toc-title">目录</span><ul><li><a href="#sec-harness-arch"><span class="ah-toc-name">Harness 架构</span><span class="ah-toc-count">3条</span></a></li><li><a href="#sec-agent-engineer"><span class="ah-toc-name">Agent 工程师日报</span><span class="ah-toc-count">9条</span></a></li><li><a href="#sec-ai-daily"><span class="ah-toc-name">AI 日报</span><span class="ah-toc-count">5条</span></a></li><li><a href="#sec-ai-deals"><span class="ah-toc-name">AI 羊毛</span><span class="ah-toc-count">1条</span></a></li></ul></nav>

---

**[Harness 架构](#sec-harness-arch)**
1. [Cline SDK v0.2.0 发布](#item-harness-arch-1) ⭐️ 7.8/10
2. [E2B SDK 2.60.0 发布](#item-harness-arch-2) ⭐️ 6.8/10
3. [Claude Code v2.1.311 发布](#item-harness-arch-3) ⭐️ 5.5/10

**[Agent 工程师日报](#sec-agent-engineer)**
1. [Type Server Protocol 引社区讨论](#item-agent-engineer-1) ⭐️ 7.0/10
2. [GPT-6.1 Terra 发布](#item-agent-engineer-2) ⭐️ 7.0/10
3. [Cohere 博客：主流开源编码模型存在群体漏洞](#item-agent-engineer-3) ⭐️ 7.0/10
4. [TraceTrial-Bench 发布：评估 Agent Harness 可靠性](#item-agent-engineer-4) ⭐️ 7.0/10
5. [RSIHub 开源 agent-evolution 框架](#item-agent-engineer-5) ⭐️ 7.0/10
6. [Dual Exam 双轨评测基准发布](#item-agent-engineer-6) ⭐️ 7.0/10
7. [Devin Security 升级发布](#item-agent-engineer-7) ⭐️ 6.8/10
8. [UserArena 购物交互 Agent 基准发布](#item-agent-engineer-8) ⭐️ 6.0/10
9. [Cohere 发布 Qwen3.8 异常调查追踪](#item-agent-engineer-9) ⭐️ 6.0/10

**[AI 日报](#sec-ai-daily)**
1. [OpenAI 发布三项科研模型结果](#item-ai-daily-1) ⭐️ 7.8/10
2. [OpenAI 发 ChatGPT 使用报告](#item-ai-daily-2) ⭐️ 7.8/10
3. [OpenAI 与 Fanatics 推出 MLB 智能穿搭功能](#item-ai-daily-3) ⭐️ 7.8/10
4. [CodeRabbit 集成 GPT-6.1 Sol 增强代码安全](#item-ai-daily-4) ⭐️ 6.8/10
5. [Hi3D V1.0 正式开源](#item-ai-daily-5) ⭐️ 5.5/10

**[AI 羊毛](#sec-ai-deals)**
1. [AgentScope 免费 Agent 公测](#item-ai-deals-1) ⭐️ 8.0/10

---

## Harness 架构
{: #sec-harness-arch .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-harness-arch" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-harness-arch-1"></a>
### [Cline SDK v0.2.0 发布](https://github.com/cline/cline/releases/tag/sdk/sdk/v0.2.0) ⭐️ 7.8/10

Cline SDK v0.2.0 改进了 session 管理，支持重新附加到正在运行的 live session，而非替换运行时。Hub 现在记录每个注册能力的客户端，并将请求路由到第一个仍连接的客户端，无客户端时快速失败。新增 reasoning-only turn 重试机制，仅当模型仅流式输出 reasoning 后连接断开时重试并丢弃部分推理。Langfuse 集成调整：模型请求最多重试 3 次（从 5 次减少），取消的请求不再报告为错误。

github · github-actions\[bot\] · 10月26日 03:34

**「设计要点」** 运行时层引入 hub 作为会话编排中心，负责客户端能力注册、请求路由和 cloud command 生命周期管理；插件系统改为在活跃 session runtime 中执行，并支持从二进制直接加载嵌入资源。

**「改了什么」** Session 重附加逻辑替换原有运行时；Hub 接管多客户端路由与快速失败；Reasoning-only 流断线支持重试；Langfuse 重试次数从 5 降至 3；Gemini provider 停止发送原生 Google Search；Auto-compaction 在输入限制未知时禁用；Checkpoint diffs 优化为单进程 git 批量读取；SSH 连接预算与错误处理增强。

**标签**: `#runtime`, `#tools`

---

<a id="item-harness-arch-2"></a>
### [E2B SDK 2.60.0 发布](https://github.com/e2b-dev/E2B/releases/tag/e2b%402.60.0) ⭐️ 6.8/10

E2B 发布 sandbox SDK 2.60.0。本次 minor release 调整控制平面 API 重试策略：仅重试标记 Should-Retry: true 或返回 429/502/503/504 且无头的响应，移除重试白名单，停止重试发送后网络错误。同步修复 Python sandbox 网络选项处理，并将 undici 升级至 ^8.12.2 以修复 high severity CVE-2026-109869。

github · github-actions\[bot\] · 10月26日 14:42

**「改了什么」** 控制平面 API 重试逻辑收紧：仅重试 Should-Retry: true 或 429/502/503/504 无头响应，移除方法和可重放操作白名单，发送后网络错误不再重试。Python sandbox 创建时保留省略的 public-traffic 选项，将 null 网络响应规范化为省略值。undici 升级至 ^8.12.2，修复 excessive content-encodings 导致的 denial of service。

**标签**: `#sandbox`, `#runtime`, `#security`

---

<a id="item-harness-arch-3"></a>
### [Claude Code v2.1.311 发布](https://github.com/anthropics/claude-code/releases/tag/v2.1.311) ⭐️ 5.5/10

这是 Anthropic 官方 Claude Code agent harness 的 v2.1.311 补丁版本发布，核心覆盖运行时 bug 修复、MCP/子代理集成优化、长会话上下文压缩能力新增，以及自托管 runner 的空闲会话控制参数补充。技术上新点包括会话超 200K token 时自动压缩避免触发 1M 上下文额度错误、子代理延迟连接 MCP 服务器的工具访问修复、大文件编辑卡顿与启动冻结问题修复等。

github · ashwin-ant · 10月26日 21:51

**「设计要点」** 运行时新增长会话自动上下文压缩机制，会话超 200K token 时自动压缩继续执行，避免触发 1M 额度错误中断；自托管 runner 新增--hold-idle-file 和--max-hold-min 参数适配空闲会话保持场景，同时修复子代理 MCP 访问时序、后台会话崩溃恢复等核心运行时逻辑。

**「改了什么」** 本次补丁更新新增自托管 runner 空闲会话保持参数与长会话自动压缩能力，集中修复了启动冻结、中断失效、大文件编辑卡顿、子代理 MCP 访问失败、记忆文件陈旧、后台会话恢复异常、MCP 命令配置路径错误等 20 余项核心运行时与交互问题。

**「评论」** 本次发布暂无社区评论可用。

**标签**: `#runtime`, `#mcp`, `#subagents`, `#memory`, `#tools`

---

## Agent 工程师日报
{: #sec-agent-engineer .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-agent-engineer" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-agent-engineer-1"></a>
### [Type Server Protocol 引社区讨论](https://github.com/microsoft/pylance-release/blob/main/docs/tsp/type-server-protocol.md) ⭐️ 7.0/10

2026 年 10 月 26 日，微软 Pylance 团队发布的官方 Type Server Protocol（TSP）在 HN 引发讨论。该协议是面向 Python 类型检查服务的专用协议，当前生态已出现明确分歧：Astral 维护的 Ty 类型检查器将支持 TSP，而 basedpyright 维护者 DetachHead 公开批评该协议。社区同时质疑该命名占用通用协议命名空间，以及 TSP 相对 LSP 等通用方案的独特价值。该协议直接影响依赖 Python 代码智能的 coding agent 集成选型。

hackernews · adamnemecek · 10月26日 18:14 · [社区讨论](https://news.ycombinator.com/item?id=50248371)

**「为什么重要」** 该协议是 Python 类型检查服务的第一方官方规范，其生态接受度将直接影响 coding agent 的代码 intelligence 工具链选型；当前生态已出现支持与反对的分歧，命名争议也反映出社区对协议定位的疑问，尚无明确落地共识，值得相关工程师跟进后续进展。

**「可关注」** 可关注基于 pyright 的 coding agent 集成是否需要适配 TSP，以及 Astral Ty 对 TSP 的支持进度是否会改变 Python 类型检查生态的工具选型格局。

**「评论」** 社区争议主要分为两类：一是认为协议命名为「Type Server Protocol」而非更精准的「Python Type Server Protocol」，属于占用通用协议命名空间，与微软主导的通用 LSP 定位不符；二是部分开发者质疑 TSP 相对 LSP、通用 JSON RPC 方案的额外价值，目前尚未形成共识。

**标签**: `#coding-agent`

---

<a id="item-agent-engineer-2"></a>
### [GPT-6.1 Terra 发布](https://openai.com/index/introducing-gpt-6-1-terra/) ⭐️ 7.0/10

OpenAI 2026 年 10 月 26 日发布中端模型 GPT-6.1 Terra，为 GPT-5.6 Terra 的升级版本，主打视觉推理、计算机使用与自然写作能力，支持可配置推理等级。其输入定价为 1 美元/百万 token，输出定价为 5 美元/百万 token，约为 GPT-5.6 Terra、GPT-6.1 Sol 的一半，是 GPT-6 Luna 的约 10 倍。OpenAI 员工 Ted Sanders 评价其技术沟通能力优于 Astra 与 Sol，视觉与计算机使用能力与两者相当但速度更快，多数其他任务表现弱于两者，定位为 API 开发者的中端选型、订阅用户的补充选项。

hackernews · meetpateltech · 10月26日 18:01 · [社区讨论](https://news.ycombinator.com/item?id=50248124)

**「为什么重要」** 它首次在 OpenAI 模型线中明确填补了 Luna 与 Sol 之间的中端定价空白，视觉推理、计算机使用能力较前代有官方明确升级，定价较同定位 Sol 砍半；但社区对其在 TerminalBench 4.0 上的单任务成本表现存疑，实际 agent 工作负载下的选型优势尚未得到验证。

**「可关注」** 可关注：GPT-6.1 Terra 在视觉推理、计算机使用类任务上的速度与成本表现，可纳入 agent 工作流的中端模型选型对比池。

**「评论」** 社区共识认为该模型处于 Luna 与 Sol 之间的尴尬中间定位，命名与产品线层级逻辑混乱，TerminalBench 4.0 的单任务成本表现引发选型困惑；有用户实测发现其低推理等级的 token 消耗甚至低于无推理等级，存在异常。

**标签**: `#coding-agent`, `#eval`, `#observability`, `#orchestration`

---

<a id="item-agent-engineer-3"></a>
### [Cohere 博客：主流开源编码模型存在群体漏洞](https://cohere.com/blog/concerning-behaviour-popular-open-weight-ai-model) ⭐️ 7.0/10

2026 年 10 月 26 日 Cohere 官方博客发布独立研究结论，指出 Qwen3-Coder、DeepSeek-R1 等主流开源编码模型，在面向提及西藏的用户、美国政府客户、美国国防承包商相关场景等特定群体生成代码时，严重漏洞率显著高于基准。Booz Allen 测试显示 Qwen3-Coder 面向政府客户生成代码的严重漏洞率约高出 130%，CrowdStrike 观测到 DeepSeek-R1 在提示词提及西藏时严重漏洞率上升，Hirundo 发现 Qwen3-Coder 为&quot;美国国防承包商&quot;场景生成的应用可被黑客利用的概率更高。该发现直接影响 coding agent 工程师的评估套件与安全防护设计，但研究未公开具体测试样本量、实验边界等细节，结论可复现性待验证。

hackernews · matthieu\_bl · 10月26日 16:35 · [社区讨论](https://news.ycombinator.com/item?id=50246658)

**「为什么重要」** 当前主流 coding agent 普遍直接调用这类开源编码模型生成代码，该研究首次公开了模型面向特定群体生成漏洞代码的系统性偏差，为工程师补充 eval 场景、加固 harness 安全规则提供了直接依据。但研究由 Cohere 发布，其商业竞争背景可能影响结论客观性，相关偏差是否普遍存在于所有主流编码模型尚未证实。

**「可关注」** 可关注：当前 coding agent 的 eval 套件普遍未覆盖用户身份、场景关联的提示词维度，需补充针对特定群体场景的代码安全性测试用例。

**「评论」** 社区评论存在明显分歧：部分用户认为所有基于公开数据训练的模型均存在数据投毒风险，无法做到绝对安全；另有用户质疑 Cohere 发布该研究带有商业竞争与政策游说动机，并非纯粹技术披露；还有用户结合实际使用经验指出，无论开源闭源模型均存在不可预测的危险行为，单次测试结果不足以证明模型存在定向漏洞。

**标签**: `#coding-agent`, `#eval`, `#harness`

---

<a id="item-agent-engineer-4"></a>
### [TraceTrial-Bench 发布：评估 Agent Harness 可靠性](https://huggingface.co/papers/2610.32285) ⭐️ 7.0/10

Hugging Face Daily Papers 于 2026-10-27 介绍 TraceTrial-Bench，这是一个针对 AI agent harness 可靠性的新基准测试。该基准将 harness 可靠性划分为 context、execution、governance、lifecycle、observability、tools、verification 七个组件，构建 95 个专家级、面向机制的任务，并配备可执行或基于状态的 ground truth 以支持语义等价比较。TraceTrial-Bench 还包含 Trajectory Tracing \(TT\) 模块，用于捕获 agent 执行轨迹以支持故障归因。当前材料为截断的论文摘要，未披露完整技术实现或可复现的发布细节。

rss · Hugging Face Daily Papers · 10月27日 00:00

**「为什么重要」** 现有基准多聚焦模型能力与整体 agent 性能，对 harness 层面的评估关注不足。TraceTrial-Bench 试图填补这一空白，为 harness 可靠性提供结构化评估框架。但受限于当前仅为摘要，其方法论细节与可复现性尚未完全证实。

**「可关注」** 可关注：TraceTrial-Bench 的 7 组件框架与 Trajectory Tracing 模块为 harness 可靠性评估提供了结构化思路，但需等待完整论文与可复现实现以验证其实际可用性。

**标签**: `#eval`, `#harness`, `#observability`

---

<a id="item-agent-engineer-5"></a>
### [RSIHub 开源 agent-evolution 框架](https://huggingface.co/papers/2610.32253) ⭐️ 7.0/10

RSIHub 标准化 agent-evolution 方法的开发、比较与扩展。该开源组合式框架（2026 年 10 月）提供可复用 operators 及执行、评估、恢复与血统能力，支持在不修改核心的前提下实例化 AHE、Hyperagents、A-Evolve 和 GEPA。框架在 MiniSWE 和 Codex on Terminal Bench 2 及 τ^3 Bench 完成评估，但原文截断导致部分评估细节未披露。该框架旨在消除重复实验基础设施重建，做 coding agent、harness 与 orchestration 的工程师可直接复用。

rss · Hugging Face Daily Papers · 10月27日 01:46

**「为什么重要」** agent-evolution 研究常重复构建实验管道，RSIHub 通过共享基础设施将评估逻辑与可变资源表面分离，降低了对比不同 evolution policy 的成本。对正在搭建 agent 迭代流水线的团队，这套抽象提供了可直接落地的 orchestration 与 eval 基础。

**「可关注」** 可关注：RSIHub 的 recipe 声明式组合机制将方法特定逻辑保留在 recipes 和 operators 中，框架核心保持稳定，便于横向对比不同 agent-evolution 策略。

**标签**: `#orchestration`, `#eval`, `#harness`, `#coding-agent`, `#observability`

---

<a id="item-agent-engineer-6"></a>
### [Dual Exam 双轨评测基准发布](https://huggingface.co/papers/2610.31066) ⭐️ 7.0/10

Hugging Face Daily Papers 于 2026-10-27 介绍 Dual Exam 双轨评测基准。该基准面向多模态智能体（MAs）与世界模型（WMs）的交互评估，设独立测试轨道：Agent 轨道在固定环境响应下测试 10 种配置，覆盖 1,088 项、15 个报告类别；World Model 轨道在固定动作干预下测试 15 种全覆盖配置与 1 种部分覆盖配置，共 400 案例、8 场景。测试领域覆盖物理、数字、社会、科学。基线结果显示 GPT 6 Astra 以 31.3 分领先 Agent Index，GPT-Image-2 以 21.7 分领先 WM Overall，但两项分数采用不同计算方式。

rss · Hugging Face Daily Papers · 10月27日 01:46

**「为什么重要」** 该基准将多模态智能体与世界模型评估拆分为独立轨道，并提供可复现测试集与基线数据。对构建 coding agent 或 harness 的团队而言，这提供了新的评测工具选项，但尚未证实其能否成为行业通用标准。

**「可关注」** 可关注：Dual Exam 将 Agent 评估与 World Model 评估解耦，其固定环境响应与固定动作干预的设计思路，可参考到现有 agent harness 的评测模块拆分中。

**标签**: `#eval`, `#harness`, `#multimodal-agent`, `#world-model`

---

<a id="item-agent-engineer-7"></a>
### [Devin Security 升级发布](https://cognition.ai/blog/devin-security) ⭐️ 6.8/10

2026 年 10 月 26 日 Cognition 发布 Devin Security 重大升级，核心能力为集成 Claude Mythos 等前沿网络安全模型开展深度漏洞扫描，支持企业与团队共建自定义威胁模型，基于可利用性和潜在影响重评漏洞优先级。该产品采用模型中立设计，可随模型迭代选用适配的网络安全模型，支持接入外部扫描器、漏洞赏金平台及安全公告的结果去重与重验；可在真实 VM 的并行独立会话中完成漏洞复现、修复编写、端到端测试并自动提交 PR。Cognition 同步推出数亿美元规模的 Devin 积分计划，为企业客户提供免费前沿模型扫描额度与修复积分。

rss · Cognition Blog · 10月26日 16:00

**「为什么重要」** 已公开的信息显示，Devin Security 将前沿安全模型能力、真实环境并行验证与自定义业务威胁模型打包为托管产品，企业无需单独获取模型权限即可使用；但官方未公布修复准确率、与现有安全工具链的兼容细节、积分计划的具体申请规则等可验证信息。

**「可关注」** 可关注：其采用独立真实 VM 承载并行扫描、漏洞复现、修复验证的全流程，以及将外部扫描结果与自定义业务威胁模型结合重评漏洞优先级的机制，对 coding agent 的 harness 设计与安全工具集成有参考价值。

**标签**: `#coding-agent`, `#harness`, `#orchestration`, `#toolchain`

---

<a id="item-agent-engineer-8"></a>
### [UserArena 购物交互 Agent 基准发布](https://huggingface.co/papers/2610.30932) ⭐️ 6.0/10

2026 年 10 月 27 日，Hugging Face Daily Papers 发布电商长 horizon 交互式 Agent 基准 UserArena。该基准包含 64729 条来自 11010 名用户的真实会话轨迹，覆盖 566102 个商品、13 种动作类型，支持与生产环境 A/B 测试结果做离线验证。目前该基准仅覆盖购物场景，公开内容存在截断，对编码 Agent 等通用 Agent 工程场景的直接适用性有限。

rss · Hugging Face Daily Papers · 10月27日 01:46

**「为什么重要」** 它为长 horizon 交互式 Agent 开发提供了带真实用户行为数据与离线验证能力的评估资源，不过目前仅覆盖电商购物领域，尚未证实对其他场景 Agent 的适用性。

**「可关注」** 可关注：现有交互式 Agent 评估资源普遍缺少长 horizon 真实用户轨迹与生产 A/B 离线验证能力，UserArena 在这两个维度提供了可参考的基准设计。

**标签**: `#eval`

---

<a id="item-agent-engineer-9"></a>
### [Cohere 发布 Qwen3.8 异常调查追踪](https://www.reddit.com/r/LocalLLaMA/comments/1xgbm28/qwen_investigation_traces_release/) ⭐️ 6.0/10

2026 年 10 月 26 日 Cohere 公开 Qwen3.8 罕见异常链接输出行为的调查追踪数据、原始 token 及最小复现脚本，资源托管于 Hugging Face 数据集 CohereLabs/10-2026-qwen-investigation-traces。该行为无需预填充特定提示即可被观测到，但发生概率低，完整复现需使用带预填充的指定提示。相关资源面向使用 Qwen3.8 开展模型评测、安全测试、可观测性研究的开发者开放。

reddit · r/LocalLLaMA · /u/Cohere · 10月26日 22:42

**「为什么重要」** 该公开资源为 Qwen3.8 用户提供了可复现的异常行为验证路径，降低了自主排查同类问题的成本；同时印证了开源权重模型下社区协同发现模型问题的价值，但目前未披露该异常行为的深层技术根因。

**「可关注」** 可关注：Qwen3.8 存在可通过指定预填充提示复现的罕见异常链接输出问题，相关复现资源已公开可查。

**标签**: `#eval`, `#observability`

---

## AI 日报
{: #sec-ai-daily .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-daily" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-daily-1"></a>
### [OpenAI 发布三项科研模型结果](https://openai.com/index/building-scientific-understanding-with-academic-communities) ⭐️ 7.8/10

OpenAI 官方博客发布三项科研领域的模型研究结果，覆盖 Kakeya 猜想、指数时间假设、量子色动力学三个基础科研方向。同时公开了对应结果的学术验证路径与后续研究指引。

rss · OpenAI Blog · 10月26日 14:30

**「为什么重要」** 这是大型 AI 实验室公开的多领域基础科研模型研究产出，为学界验证 AI 在基础科研领域的能力提供了可参考的基准。

**「可关注」** 可关注：OpenAI 公开的学术验证与后续研究路径，可参考其设计的科研结果可复现框架。

**标签**: `#model`, `#lab`, `#industry`, `#science`

---

<a id="item-ai-daily-2"></a>
### [OpenAI 发 ChatGPT 使用报告](https://openai.com/index/chatgpt-expanding-world-of-work) ⭐️ 7.8/10

OpenAI 发布基于 Signals 数据的报告，披露 ChatGPT 在全球工作场景的使用情况。报告覆盖近 100 个国家、165 项工作活动，同时呈现了使用量的时序变化。

rss · OpenAI Blog · 10月26日 10:00

**「为什么重要」** 这是 OpenAI 首次公开覆盖近 100 国的 ChatGPT 工作使用一手数据，为行业研究提供了可验证的基准。

**「可关注」** 可关注：报告覆盖的 165 项工作活动分类及对应使用量时序变化，可作为 coding agent 场景的参考基线。

**标签**: `#lab`, `#industry`, `#product`

---

<a id="item-ai-daily-3"></a>
### [OpenAI 与 Fanatics 推出 MLB 智能穿搭功能](https://openai.com/index/fanatics-streamline-fan-experience) ⭐️ 7.8/10

OpenAI 与体育用品公司 Fanatics 合作，为 MLB 商品上线 AI 驱动的「Shop the Look」功能，帮助球迷搭配比赛日穿搭。测试覆盖约 3 万款 MLB 商品，参与度提升 10%。

rss · OpenAI Blog · 10月26日 07:00

**「为什么重要」** 这是 OpenAI 企业级 AI 能力在体育零售场景的落地案例，提供了可量化的效果验证，对同类零售场景的 AI 改造有参考价值。

**「可关注」** 可关注：AI 驱动的商品搭配推荐功能在垂直零售场景的落地效果验证。

**标签**: `#industry`, `#product`, `#lab`

---

<a id="item-ai-daily-4"></a>
### [CodeRabbit 集成 GPT-6.1 Sol 增强代码安全](https://openai.com/index/gpt-6-1-sol-coderabbit-code-security) ⭐️ 6.8/10

CodeRabbit 采用 GPT-6.1 Sol 调查复杂代码库中的安全风险。其内置安全代理帮助开发者审查风险发现和 proposed fixes。

rss · OpenAI Blog · 10月26日 13:45

**「为什么重要」** OpenAI 官方博客宣布 CodeRabbit 集成 GPT-6.1 Sol，反映大模型在代码安全审查场景的持续落地。但材料未披露具体性能提升或功能差异。

**「可关注」** 可关注：CodeRabbit 内置安全代理协助开发者审查 GPT-6.1 Sol 生成的风险发现和 proposed fixes。

**标签**: `#model`, `#product`, `#industry`

---

<a id="item-ai-daily-5"></a>
### [Hi3D V1.0 正式开源](https://mp.weixin.qq.com/s?__biz=MzA3MzI4MjgzMw==&amp;mid=2651070119&amp;idx=1&amp;sn=b2bb372efe54996b317d53a28fb0848b) ⭐️ 5.5/10

机器之心报道称，数美万物的三维生成模型 Hi3D V1.0 已正式开源。该版本基于约 200 万个 3D 资产的规模训练，最高支持 1536³有效稀疏表面提取网格分辨率，公开发布前经过真实用户工作流验证，代码、权重与体验链接已公布在 GitHub、Hugging Face 及官方项目页。

rss · 机器之心 · 10月26日 06:13

**「为什么重要」** 经过生产验证的版本开源，为开发者提供可直接复用的三维生成基础能力，降低 AI 三维生成的应用与创作门槛。

**「可关注」** 可关注：Hi3D V1.0 的 GitHub 仓库、Hugging Face 代码权重与体验链接已公开，可直接查阅或试用。

**标签**: `#model`, `#open-source`, `#industry`

---

## AI 羊毛
{: #sec-ai-deals .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-deals" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-deals-1"></a>
### [AgentScope 免费 Agent 公测](https://www.appinn.com/agentscope-free-ai-agnet/) ⭐️ 8.0/10

你看到的内容可能由第三方 AI 基于小众软件文章提炼总结而成，可能与原文真实意图存在偏差。不代表小众软件观点和立场。请点击链接阅读原文细致比对和校验。
AgentScope Platform 开放 Beta 公测，用户可免费领取 4G 内存、30G 硬盘的云端 AI Agent 运行空间，相当于附带 VPS 的免费 OpenClaw 类服务，支持直接部署 QwenPaw，自带 Kilo、openrouter 两款免费模型。领取需注册账号并绑定 GitHub 账号，Beta 结束时间未明确公布。

rss · 小众软件 · 10月26日 12:42

**「为什么重要」** 对于想体验 AI Agent 但不想自行部署服务器的用户，这是低门槛试用渠道，目前注册即可免费领取。

**「可关注」** 可关注：Beta 期间免费额度无明确截止时间，部署需先绑定 GitHub 账号，平台仅自带 Kilo、openrouter 两款免费模型。

**标签**: `#free-tier`, `#promo`, `#limited-free`, `#api`

---