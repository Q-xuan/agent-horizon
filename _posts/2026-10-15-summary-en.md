---
layout: default
title: "Horizon Summary: 2026-10-15 (EN)"
date: 2026-10-15
lang: en
---

> From 197 items, 10 important content pieces were selected

---

**Agent Harness Architecture**
1. [Mastra core 1.77.0 发布](#item-harness-arch-1) ⭐️ 8.8/10
2. [Agent Framework 1.25.0](#item-harness-arch-2) ⭐️ 7.8/10
3. [langgraph checkpointpostgres 3.2.0 adds prune](#item-harness-arch-3) ⭐️ 6.8/10

**AI Agent Engineer**
1. [Zellige AI 开源 Tessera-27B-B-CJK](#item-agent-engineer-1) ⭐️ 6.0/10

**AI Daily**
1. [GitHub 发布新版星标历史 API](#item-ai-daily-1) ⭐️ 6.8/10
2. [SentinelOne 借助 OpenAI Daybreak 压缩恶意软件分析时间](#item-ai-daily-2) ⭐️ 6.3/10
3. [Block 借助 OpenAI 构建 AI 安全运营](#item-ai-daily-3) ⭐️ 6.3/10

**AI Deals**
1. [Free Voronoi 拼图生成器可用](#item-ai-deals-1) ⭐️ 6.0/10
2. [免费Remote Jobs API 无认证](#item-ai-deals-2) ⭐️ 6.0/10
3. [Petal 开源免费屏幕共享工具上线](#item-ai-deals-3) ⭐️ 5.0/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [Mastra core 1.77.0 发布](https://github.com/mastra-ai/mastra/releases/tag/%40mastra/core%401.77.0) ⭐️ 8.8/10

Mastra agent harness 发布 @mastra/core@1.77.0。本次引入 FactorySandbox 一等契约，内置 Docker、E2B、Mastra Platform 三种实现，支持可调设置、仓库模板和预构建环境。Factory 现支持多仓库会话与跨仓库源码控制工具，durable agent run fencing 扩展至 Cloudflare DO/D1、Convex、DynamoDB 等十多种存储后端。观测记忆新增并发冲突感知写入与跨系统链路追踪。

github · PaulieScanlon · Oct 14, 08:29

**「设计要点」** Factory 沙箱层抽象为 provider 实例契约，支持设置、模板、构建全生命周期管理，脱离回调式单会话创建。Durable agent 在存储适配器层实现 run fencing，通过所有权标记防止崩溃恢复后的状态覆写；观测记忆引入 generation 保护与块级写入 API，解决多进程重叠缓冲的竞态。

**「改了什么」** 相对上一版，核心新增 FactorySandbox 契约及 Docker、E2B、Mastra Platform 三种内置实现、环境预构建与多仓库会话、跨存储后端的 durable run fencing，以及观测记忆的冲突感知写入。AgentController 的 steer 与 followUp 接口支持文件附件，工作流 HTTP 路由收紧为仅通过 agent 路由启动。

**Tags**: `#sandbox`, `#tools`, `#runtime`, `#memory`

---

<a id="item-harness-arch-2"></a>
### [Agent Framework 1.25.0](https://github.com/microsoft/agent-framework/releases/tag/dotnet-1.25.0) ⭐️ 7.8/10

Microsoft 发布 Agent Framework .NET 1.25.0。A2A 协议升级至 1.0.0-preview3，运行时修复 SSE 流未正确终止、agent handoff 回弹及 reasoning 状态残留问题。新增 closed-list workflow question 支持，tool approval 增加无响应自动拒绝机制，purview 检查扩展至引用与错误详情。Cosmos chat 元数据与 partition-key 策略解耦，Foundry toolbox 响应缓存隔离，并回滚 Harness progress 简洁化 breaking change，同时修复 OpenTelemetry 包装下 continuation token 丢失。

github · dmytrostruk · Oct 14, 19:10

**「设计要点」** Runtime 层修复 SSE 终止符与 agent 状态机残留，A2A 协议升级影响跨系统互操作。工具层引入 approval 复用与无响应超时拒绝，工作流层支持 closed-list 问题约束；存储层解耦 Cosmos partition-key，观测层修正 OpenTelemetry 包装下 continuation token 保持。

**「改了什么」** A2A 协议升级至 1.0.0-preview3，SSE 流终止符修复为 data: \[DONE\]，handoff 回弹与 reasoning 残留问题得到修正。新增 closed-list workflow question、tool approval 无响应自动拒绝、purview 检查扩展引用与错误详情；Cosmos chat 元数据与 partition-key 解耦，Foundry 缓存隔离，并回滚 Harness progress 简洁化 breaking change，同时修复 OpenTelemetry 包装下 continuation token 丢失。

**Tags**: `#dotnet-agent-framework`, `#A2A-protocol`, `#agent-runtime`, `#tool-approval`, `#agent-workflow`

---

<a id="item-harness-arch-3"></a>
### [langgraph checkpointpostgres 3.2.0 adds prune](https://github.com/langchain-ai/langgraph/releases/tag/checkpointpostgres%3D%3D3.2.0) ⭐️ 6.8/10

langchain-ai/langgraph released checkpointpostgres 3.2.0 on October 14, 2026. The update adds a prune capability to PostgresSaver and AsyncPostgresSaver for managing checkpoint lifecycle. This enables production deployments to remove outdated checkpoints. No interface changes or operational limits are documented in the release notes.

github · github-actions\[bot\] · Oct 14, 19:54

**「What Changed」** checkpointpostgres 3.2.0 introduces prune functionality for PostgresSaver and AsyncPostgresSaver. This is the sole feature addition since version 3.1.3.

**Tags**: `#memory`, `#runtime`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [Zellige AI 开源 Tessera-27B-B-CJK](https://www.reddit.com/r/LocalLLaMA/comments/1x5xm28/tessera27bbcjk_zellige_ais_new_finetune_of_qwen/) ⭐️ 6.0/10

2026年10月14日，Zellige AI发布开源Apache-2.0权重的Tessera-27B-B-CJK模型，该模型基于Qwen3.8-27B微调，面向编码智能体场景优化，内部思考采用混合英文、中文与符号的压缩CJK速记，输出保持英文/代码格式，兼容现有智能体harness。在11个held-out编码智能体任务、xhigh effort设置下，该模型每轮思考token为基座模型的0.50-0.64倍，典型轮次为0.496倍（90% CI 0.385-0.624），88轮匹配测试中工具调用有效率和基座一致，无重复循环，101K-131K输入长度下6/6工具调用有效。该模型在数学竞赛、硬算法编码场景表现弱于基座，GGUF与NVFP4量化版本尚未完成测试。

reddit · r/LocalLLaMA · /u/ghgi\_ · Oct 14, 17:35

**「为什么重要」** 该模型针对编码智能体循环的token消耗问题，提出了可复现的压缩CJK内部思考微调方案，且开源权重与训练流程，为智能体效率优化提供了新的参考方向。

**「可关注」** 可关注：针对编码智能体场景，可通过将内部思考替换为压缩CJK速记、同时保持输出兼容现有harness的微调思路降低token消耗，但需注意该方案在数学竞赛、硬算法编码场景表现弱于基座，且量化版本尚未验证。

**Tags**: `#coding-agent`, `#harness`

---

## AI Daily

<a id="item-ai-daily-1"></a>
### [GitHub 发布新版星标历史 API](https://github.blog/engineering/architecture-optimization/from-2500-requests-to-24-rebuilding-star-history-without-the-stargazers/) ⭐️ 6.8/10

GitHub has officially launched a new repository star history API. This API provides star trend data without returning individual user identities, cuts request volume from 2,500 to 24, avoids unbounded database operations, and the official team has disclosed corresponding engineering tradeoffs.

rss · GitHub Blog · Oct 14, 19:11

**「为什么重要」** GitHub serves as the core hosting platform for AI open-source projects. The privacy protection and performance optimization of this API will directly impact the efficiency and compliance of obtaining star trend data for AI open-source projects.

**「可关注」** Watch for: The new star history API achieves a significant reduction in request volume and eliminates unbounded database operations by opting not to return individual user identities.

**Tags**: `#industry`, `#product`, `#open-source`

---

<a id="item-ai-daily-2"></a>
### [SentinelOne 借助 OpenAI Daybreak 压缩恶意软件分析时间](https://openai.com/index/sentinelone) ⭐️ 6.3/10

OpenAI 官方博客发布短讯称，SentinelOne 借助 OpenAI Daybreak 将恶意软件分析时间从数周缩短至小时级。公告未披露具体技术实现或量化性能指标。效率提升使其有能力调查更多威胁。

rss · OpenAI Blog · Oct 14, 12:00

**「为什么重要」** 这显示生成式 AI 在安全运营分析环节的落地案例。若小时级分析可复现，安全团队可将人力重新分配至高优先级威胁。

**「可关注」** 可关注：AI 辅助恶意软件分析的具体工作流集成与效果验证。

**Tags**: `#industry`, `#product`

---

<a id="item-ai-daily-3"></a>
### [Block 借助 OpenAI 构建 AI 安全运营](https://openai.com/index/block-ai-powered-security) ⭐️ 6.3/10

Block Inc. 正在使用 OpenAI 技术构建 AI 驱动的安全运营系统。其安全团队将威胁调查和补丁提案时间缩短至分钟级。该信息来自 OpenAI 官方博客 2026 年 10 月 14 日发布的客户案例，目前公开的技术细节有限。

rss · OpenAI Blog · Oct 14, 07:00

**「可关注」** 可关注：AI 辅助将安全威胁调查与补丁提案压缩到分钟级。

**Tags**: `#lab`, `#industry`, `#product`

---

## AI Deals

<a id="item-ai-deals-1"></a>
### [Free Voronoi 拼图生成器可用](https://gopuzzlego.com/generator) ⭐️ 6.0/10

gopuzzlego.com provides a free, no-signup jigsaw puzzle generator that outputs SVG, PDF, and STL files with Voronoi-shaped pieces. It charges no fees, requires no account, and has no stated usage limits or expiration dates as of its 2026-10-14 launch.

rss · HN Free API / Credits · Oct 14, 11:02

**「为什么重要」** No public paid tiers or usage restrictions are announced, so it works for immediate free use. But its Hacker News post has only 1 point and 0 comments, with no details on long-term maintenance, so availability may shift without warning.

**「可关注」** 可关注：The tool needs no account and supports SVG, PDF, STL exports, fitting users who need quick custom puzzle assets, but its long-term maintenance status is unannounced and availability may change.

**Tags**: `#free-tier`, `#no-account`, `#tool`

---

<a id="item-ai-deals-2"></a>
### [免费Remote Jobs API 无认证](https://remote-jobs-api.tten.no/) ⭐️ 6.0/10

HN用户earnnovadev发布免费远程工作API，提供63万条跨16个招聘板的实时职位数据。该API无需认证即可调用，未公开速率限制、有效期等使用规则，相关Show HN帖子仅获1赞0评论。

rss · HN Free API / Credits · Oct 14, 08:04

**「为什么重要」** 若开发者有轻量级远程职位数据抓取需求，可免认证直接调用，但未披露使用限制，稳定性待验证，对多数AI/开发者场景价值有限。

**「可关注」** 可关注：该API无需认证即可访问，但未公开速率限制与有效期，仅适合轻量测试，生产环境使用需自行验证稳定性。

**Tags**: `#api`, `#free-tier`

---

<a id="item-ai-deals-3"></a>
### [Petal 开源免费屏幕共享工具上线](https://petal.live/) ⭐️ 5.0/10

前 CoScreen 创始团队发布开源免费协作屏幕共享工具 Petal，替代已停服的 CoScreen，完全免费且不商业化，支持 macOS、Windows 及网页端，核心功能包括多人共享可交互桌面窗口、持久化房间，可直接使用官方托管实例，或通过 docker-compose 自托管，无使用费用，无截止时间限制。

rss · HN Free API / Credits · Oct 14, 18:23

**「为什么重要」** CoScreen 已于 2025 年 7 月 31 日停服，Petal 作为开源替代品不会被厂商单方面关停，适合有 pair programming 需求的开发者团队使用。

**「可关注」** 可关注：Petal 首版开发仅用 8 周，使用了 Fable、Astra 等前沿模型辅助编写实时音视频与窗口捕获代码，支持对接自有 LiveKit 服务器将媒体流量保留在内网，Linux 版本正在开发中可参与贡献。

**Tags**: `#open-source`, `#free-tier`, `#developer-tools`, `#screen-sharing`, `#collaboration`

---