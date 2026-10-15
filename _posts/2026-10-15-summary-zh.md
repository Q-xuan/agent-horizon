---
layout: default
title: "Horizon Summary: 2026-10-15 (ZH)"
date: 2026-10-15
lang: zh
---

> 从 197 条内容中筛选出 10 条重要资讯。

<nav id="ah-toc" class="ah-toc" aria-label="目录"><span class="ah-toc-title">目录</span><ul><li><a href="#sec-harness-arch"><span class="ah-toc-name">Harness 架构</span><span class="ah-toc-count">3条</span></a></li><li><a href="#sec-agent-engineer"><span class="ah-toc-name">Agent 工程师日报</span><span class="ah-toc-count">1条</span></a></li><li><a href="#sec-ai-daily"><span class="ah-toc-name">AI 日报</span><span class="ah-toc-count">3条</span></a></li><li><a href="#sec-ai-deals"><span class="ah-toc-name">AI 羊毛</span><span class="ah-toc-count">3条</span></a></li></ul></nav>

---

**[Harness 架构](#sec-harness-arch)**
1. [Mastra core 1.77.0 发布](#item-harness-arch-1) ⭐️ 8.8/10
2. [Agent Framework dotnet-1.25.0 发布](#item-harness-arch-2) ⭐️ 7.8/10
3. [langgraph checkpointpostgres 3.2.0 发布](#item-harness-arch-3) ⭐️ 6.8/10

**[Agent 工程师日报](#sec-agent-engineer)**
1. [Tessera-27B-B-CJK 开源发布](#item-agent-engineer-1) ⭐️ 6.0/10

**[AI 日报](#sec-ai-daily)**
1. [GitHub 新 Star 历史 API 发布](#item-ai-daily-1) ⭐️ 6.8/10
2. [SentinelOne 用 Daybreak 加速恶意软件分析](#item-ai-daily-2) ⭐️ 6.3/10
3. [Block 用 OpenAI 技术构建 AI 安全](#item-ai-daily-3) ⭐️ 6.3/10

**[AI 羊毛](#sec-ai-deals)**
1. [GoPuzzleGo 免费无账号拼图生成器](#item-ai-deals-1) ⭐️ 6.0/10
2. [免费远程工作 API 发布 无需认证](#item-ai-deals-2) ⭐️ 6.0/10
3. [Petal 开源替代 CoScreen](#item-ai-deals-3) ⭐️ 5.0/10

---

## Harness 架构
{: #sec-harness-arch .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-harness-arch" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-harness-arch-1"></a>
### [Mastra core 1.77.0 发布](https://github.com/mastra-ai/mastra/releases/tag/%40mastra/core%401.77.0) ⭐️ 8.8/10

Mastra core 1.77.0 发布。引入 FactorySandbox 一等契约，内置 Docker、E2B、Mastra Platform 三个提供者；支持预构建环境模板与多仓库会话；storage adapters 新增 durable agent run fencing；Observational Memory 增加并发冲突保护与 generation 机制；Span 支持跨追踪链接。含多项 breaking changes。

github · PaulieScanlon · 10月14日 08:29

**「设计要点」** FactorySandbox 契约将沙箱生命周期拆为 settings、template、builds 三阶段，提供者通过单实例接入。Run fencing 在 Cloudflare DO/D1、Convex、DynamoDB 等 11 种存储后端实现，防止崩溃恢复后线程/消息/工作流状态被覆写。Observational Memory 通过 supersededBy 与 blockAfter 机制解决多进程重叠缓冲冲突。

**「改了什么」** 新增 FactorySandbox 接口及三个内置实现；会话支持预构建环境与多仓库 source\_control 工具；storage adapters 统一支持 run fencing；Observational Memory 新增 commitActiveObservations、appendBufferedObservations API；Span 增加 links 字段与 W3C traceparent 解析。Breaking changes：Factory 沙箱配置迁移至 provider-instance 模式；工作流 HTTP 路由禁止启动/恢复内部工作流；AgentController 会话 API 调整；playground-ui Dialog 组件改为受控模式。

**标签**: `#sandbox`, `#tools`, `#runtime`, `#memory`

---

<a id="item-harness-arch-2"></a>
### [Agent Framework dotnet-1.25.0 发布](https://github.com/microsoft/agent-framework/releases/tag/dotnet-1.25.0) ⭐️ 7.8/10

Microsoft .NET Agent Framework 1.25.0 正式发布。A2A 协议包升级至 1.0.0-preview3，SSE 流终止补充 data: \[DONE\] 标记，修复 agent handoff 时的 reasoning 残留与 bounce-back 问题。工具审批新增超时自动拒绝与复用评估，工作流支持 closed-list 问题。Purview 检查纳入引用和错误详情，Cosmos chat metadata 与 partition-key 策略解耦（breaking change）。

github · dmytrostruk · 10月14日 19:10

**「设计要点」** 运行时修复 SSE 流终止符与 agent 状态传递缺陷，工具层增加超时自动拒绝与复用评估，工作流层新增 closed-list 问题支持。无显式架构重构。

**「改了什么」** A2A 协议升级至 1.0.0-preview3；SSE 流终止符合规范；修复 handoff reasoning 残留；工具审批增加超时拒绝和复用评估；支持 closed-list workflow questions；Purview 检查包含引用和错误详情；Cosmos chat metadata 与 partition-key 解耦。

**标签**: `#dotnet-agent-framework`, `#A2A-protocol`, `#agent-runtime`, `#tool-approval`, `#agent-workflow`

---

<a id="item-harness-arch-3"></a>
### [langgraph checkpointpostgres 3.2.0 发布](https://github.com/langchain-ai/langgraph/releases/tag/checkpointpostgres%3D%3D3.2.0) ⭐️ 6.8/10

langchain-ai/langgraph 发布 checkpointpostgres==3.2.0。本次更新为 PostgresSaver 与 AsyncPostgresSaver 新增 prune 能力，用于清理过期 checkpoint。该功能面向生产环境 checkpoint 生命周期管理，属于运维层面增强。版本自 3.1.3 升级，变更范围窄，未触及核心架构。

github · github-actions\[bot\] · 10月14日 19:54

**「改了什么」** PostgresSaver 与 AsyncPostgresSaver 新增 prune 方法，支持清理历史 checkpoint。无其他接口或行为变更。

**标签**: `#memory`, `#runtime`

---

## Agent 工程师日报
{: #sec-agent-engineer .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-agent-engineer" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-agent-engineer-1"></a>
### [Tessera-27B-B-CJK 开源发布](https://www.reddit.com/r/LocalLLaMA/comments/1x5xm28/tessera27bbcjk_zellige_ais_new_finetune_of_qwen/) ⭐️ 6.0/10

2026 年 10 月 14 日，Zellige AI 发布 Apache-2.0 开源编码智能体模型 Tessera-27B-B-CJK，基于 Qwen3.8-27B 微调，通过压缩中英混合 CJK 速记做内部思考降低智能体循环的思考 token 消耗，同时保持输出为普通英文/代码，兼容现有智能体 harness。
对比未微调基座 Qwen3.8-27B，在 11 个 held-out 编码智能体任务、xhigh effort 设置下，该模型单轮思考 token 为基线的 0.50-0.64 倍（典型轮次 0.496 倍，90% 置信区间 0.385-0.624，按 token 加权 0.644 倍）；88 轮匹配测试中有效工具调用 100%、无重复循环，101K-131K token 长度提示词下 6/6 有效工具调用。
当前仅验证 bf16 版本，GGUF、NVFP4 量化版本未测试；该模型在竞赛数学、硬算法编码任务上表现弱于基座且更易循环，所有性能数据为团队自测，无第三方独立基准验证，实际效果需进一步确认。
该模型面向编码智能体、agent harness 开发者，可降低智能体循环的 token 成本。

reddit · r/LocalLLaMA · /u/ghgi\_ · 10月14日 17:35

**「为什么重要」** 这是目前少数公开探索用内部思考压缩降低编码智能体 token 消耗的开源方案，且保持输出兼容现有 harness 生态，若验证有效可为 agent 循环成本优化提供新思路。
但当前性能数据仅为团队自测，未经过第三方复现，量化版本效果未知，实际落地效果仍有不确定性。

**「可关注」** 可关注该模型「内部思考压缩、输出格式兼容」的 token 优化思路，以及其仅用 4 步短 LoRA 在基座自有输出上完成微调的训练流程，但需注意其未覆盖竞赛数学等场景、量化版本未验证的局限性。

**标签**: `#coding-agent`, `#harness`

---

## AI 日报
{: #sec-ai-daily .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-daily" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-daily-1"></a>
### [GitHub 新 Star 历史 API 发布](https://github.blog/engineering/architecture-optimization/from-2500-requests-to-24-rebuilding-star-history-without-the-stargazers/) ⭐️ 6.8/10

GitHub 发布新版仓库 Star 历史 API，不再返回单个用户身份信息，同时避免无界数据库操作。该 API 将获取 Star 趋势数据的请求量从 2500 次降至 24 次，同时公开了对应的工程权衡选择。

rss · GitHub Blog · 10月14日 19:11

**「为什么重要」** GitHub 是 AI 开源项目的核心托管平台，该 API 既保护用户隐私，又大幅降低获取 Star 趋势的请求成本，对依赖此类数据的 AI 工具、项目统计场景有直接价值。

**「可关注」** 可关注：新版 Star 历史 API 通过放弃返回个体用户身份，换取了请求量下降 99% 和无界数据库操作的消除。

**标签**: `#industry`, `#product`, `#open-source`

---

<a id="item-ai-daily-2"></a>
### [SentinelOne 用 Daybreak 加速恶意软件分析](https://openai.com/index/sentinelone) ⭐️ 6.3/10

OpenAI 官方博客发布短讯称，SentinelOne 借助 OpenAI Daybreak 将恶意软件分析时长从数周缩短至小时级，可提升威胁调查容量，未披露具体技术细节与量化性能指标。

rss · OpenAI Blog · 10月14日 12:00

**「为什么重要」** 这展示了大模型在网络安全分析场景的落地可能性，为同类威胁处理效率提升提供了参考方向。

**「可关注」** 可关注：OpenAI Daybreak 在恶意软件分析场景的落地应用进展。

**标签**: `#industry`, `#product`

---

<a id="item-ai-daily-3"></a>
### [Block 用 OpenAI 技术构建 AI 安全](https://openai.com/index/block-ai-powered-security) ⭐️ 6.3/10

OpenAI 官方博客发布客户案例，称 Block Inc. 正使用 OpenAI 技术构建 AI 驱动的安全能力，其安全团队可将威胁调查与补丁方案提出的耗时缩短至分钟级。该内容为商业客户案例，未披露具体技术实现细节与量化性能数据。

rss · OpenAI Blog · 10月14日 07:00

**「为什么重要」** 该案例是 OpenAI 官方披露的 To B 场景落地样本，可参考企业将大模型能力接入安全运维流程的实践方向。

**「可关注」** 可关注：大模型在安全运维场景的落地实践进展，尤其是威胁调查、补丁生成等细分环节的效率提升情况。

**标签**: `#lab`, `#industry`, `#product`

---

## AI 羊毛
{: #sec-ai-deals .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-deals" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-deals-1"></a>
### [GoPuzzleGo 免费无账号拼图生成器](https://gopuzzlego.com/generator) ⭐️ 6.0/10

GoPuzzleGo 上线免费在线拼图生成器，支持 SVG、PDF、STL 三种输出格式，拼图碎片基于 Voronoi 算法生成，无需注册账号即可直接使用，未提及使用期限或额度限制。

rss · HN Free API / Credits · 10月14日 11:02

**「为什么重要」** 该工具当前无使用门槛，但相关 Hacker News 帖子互动量极低，无长期可用性的公开信息，适合临时需求试用。

**「可关注」** 可关注：该工具无需注册即可直接导出多格式 Voronoi 拼图，但无公开维护方信息，长期稳定性未验证。

**标签**: `#free-tier`, `#no-account`, `#tool`

---

<a id="item-ai-deals-2"></a>
### [免费远程工作 API 发布 无需认证](https://remote-jobs-api.tten.no/) ⭐️ 6.0/10

HN 用户 earnnovadev 在 Show HN 帖子中发布免费远程工作 API，提供 63 万条跨 16 个招聘板的实时职位数据，无需认证即可调用，未公开速率限制与有效期等信息。

rss · HN Free API / Credits · 10月14日 08:04

**「为什么重要」** 该 API 社区关注度极低（仅 1 赞 0 评论），且未披露核心使用限制，对主流 AI/开发者场景的实用价值有限。

**「可关注」** 可关注：该 API 无需认证即可调用，但未公开速率限制与有效期，长期稳定性待验证。

**标签**: `#api`, `#free-tier`

---

<a id="item-ai-deals-3"></a>
### [Petal 开源替代 CoScreen](https://petal.live/) ⭐️ 5.0/10

原 CoScreen 四位联合创始人发布开源免费屏幕共享与结对编程工具 Petal，替代 2025 年 7 月 31 日停服的 CoScreen 服务。Petal 完全免费且无商业化计划，支持 macOS、Windows 及网页端，Linux 版本后续推出。用户可直接使用官方托管实例，也可通过 docker-compose 自托管，无使用额度与时间限制。

rss · HN Free API / Credits · 10月14日 18:23

**「为什么重要」** 此前 Screenhero、CoScreen、Around 等多款受开发者喜爱的同类工具均因收购后停服，Petal 以开源、免费、支持自托管的模式，试图打破“工具被收购即停服”的行业怪圈，为开发者提供可长期使用的替代方案。

**「可关注」** 可关注：Petal 媒体流基于 LiveKit，支持自托管 LiveKit 服务器或替换为其他视频后端；共享窗口以系统真实窗口形式呈现而非网格平铺，支持多用户同时共享、带标签光标及直接操作共享窗口。

**标签**: `#open-source`, `#free-tier`, `#developer-tools`, `#screen-sharing`, `#collaboration`

---