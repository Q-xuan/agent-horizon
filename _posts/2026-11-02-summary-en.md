---
layout: default
title: "Horizon Summary: 2026-11-02 (EN)"
date: 2026-11-02
lang: en
---

> From 148 items, 5 important content pieces were selected

---

**Agent Harness Architecture**
1. [fastmcp v4.2.0a2 发布](#item-harness-arch-1) ⭐️ 6.8/10
2. [crewAI v1.15.34 发布](#item-harness-arch-2) ⭐️ 5.3/10

**AI Agent Engineer**
1. [单RTX 3090 Ti 本地LLM解码优化](#item-agent-engineer-1) ⭐️ 6.0/10

**AI Daily**
1. [Fysiverse-UniWAM 24项真机评测双第一](#item-ai-daily-1) ⭐️ 5.5/10

**AI Deals**
1. [HikerApi 100次免费抓取额度分享](#item-ai-deals-1) ⭐️ 6.0/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [fastmcp v4.2.0a2 发布](https://github.com/PrefectHQ/fastmcp/releases/tag/v4.2.0a2) ⭐️ 6.8/10

fastmcp v4.2.0a2 是 PrefectHQ 发布的第二个 4.2 版本 alpha，包含 4.1.5 全部修复及 4.2 专属变更，含一项破坏性更新。技术上新包括：JSON Schema \`const\`/\`enum\` 改为 JSON 等价比较（\`true\` 不再匹配 \`1\`）；\`prompts/get\` 缺参数时返回 \`-32602\` invalid params；OpenAPI 上游错误截断至 1 KB 并丢弃 HTML body；严格输入校验拒绝未声明 OpenAPI 参数。大型工具目录 schema 展开速度提升，kept-alive stdio 传输按客户端 timeout 管理子进程生命周期。Skills 发现支持代理穿透，Prefab 后端地址支持重绑定，Skills 功能仍标记为实验性。

github · zzstoatzz · Nov 1, 22:58

**「设计要点」** 运行时层采用 kept-alive stdio 子进程模型，不同 timeout 的客户端可共享会话，超时变更会重启空闲子进程。工具层通过严格 JSON Schema 校验和 OpenAPI 上游错误截断收紧输入边界，Skills 目录通过代理后端分页和 Prefab 渲染器资源共享提升大规模目录扩展效率。

**「改了什么」** 相对 v4.2.0a1，本版本将 Skill 改为存储中立对象（以文件夹作为加载器之一），JSON Schema \`const\`/\`enum\` 校验改为 JSON 等价比较，\`prompts/get\` 缺参数错误码改为 \`-32602\`。OpenAPI 上游错误体限制为 1 KB 并拒绝未声明参数，kept-alive stdio 子进程支持按客户端 timeout 独立管理，Skills 发现可穿透代理且 Prefab 后端地址支持 4.2 代理重绑定。

**Tags**: `#mcp`, `#tools`, `#runtime`

---

<a id="item-harness-arch-2"></a>
### [crewAI v1.15.34 发布](https://github.com/crewAIInc/crewAI/releases/tag/1.15.34) ⭐️ 5.3/10

crewAIInc/crewAI 发布 1.15.34 版本。本次更新新增 LiteLLM 目录集成、组织级 skill 搜索、\`crewai deploy create --zip\` 及 \`crewai run --inputs\` 支持。修复涵盖工具调用停止计数、OpenAI 兼容提供商 API 密钥校验、上下文窗口回退警告、LiteLLM 流式错误保留原始异常等。版本号 1.15.34 为官方小版本迭代。

github · joaomdmoura · Nov 1, 21:21

**「改了什么」** 新增 LiteLLM 独立目录集成、组织 skill 搜索、部署 zip 构建与提交哈希输出、\`crewai run --inputs\` 透传至 Python flow。修复包括 Gemini 已停用模型过滤、重复工具调用警告、结构化输出请求、JSON 输出模型不匹配时重构而非报错、AMP 登录重试、Python 3.12 深层 JSON TUI 显示等。移除 1.15.29 版 agent executor 并提供迁移文档。

**Tags**: `#tools`, `#runtime`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [单RTX 3090 Ti 本地LLM解码优化](https://www.reddit.com/r/LocalLLaMA/comments/1xlec67/getting_incredible_results_with_a_single_rtx/) ⭐️ 6.0/10

2026年11月1日Reddit用户/u/uniVocity分享其使用6年历史硬件的本地LLM推理优化实践，硬件为单RTX 3090 Ti（24GB GDDR6X显存）、128GB DDR4内存、AMD Ryzen Threadripper 3990X处理器，通过gpu-unlock解除消费级Ampere显卡FP16/BF16矩阵指令固件 throttles、Xolotl推理引擎、XQ/GSQ V2量化、FP4 KV缓存、Engram NVMe表、DSpark投机解码等配置，实现DeepSeek-V4.1-Flash-1017（552B MoE，约39B激活参数）约35 tok/s解码速度，Qwen3.8-Flash-Next（125B MoE+51B n-gram，约3.5B激活参数）约138-140 tok/s解码速度。该方案为个人自测结果，无官方验证，仅覆盖本地推理场景，部分步骤基于Gentoo Linux系统，其他环境需自行调整。

reddit · r/LocalLLaMA · /u/uniVocity · Nov 1, 21:01

**「为什么重要」** 消费级Ampere显卡存在官方未公开的FP16/BF16矩阵指令 throttles，该实践提供了可复现的解除方案，同时针对大MoE模型的单卡本地推理给出了量化、KV缓存、投机解码的组合优化路径，对资源有限的本地LLM部署有参考价值，但数据仅为单用户自测，未覆盖agent场景的端到端效果验证，通用性尚未得到广泛验证。

**「可关注」** 消费级Ampere显卡存在未公开的FP16/BF16矩阵指令 throttles，开源gpu-unlock模块可解除该限制，结合Xolotl引擎的多级内存管理、NVMe Engram流式传输与DSpark投机解码，可在单张24GB显存消费级显卡上运行大MoE模型并达到百级tok/s解码速度。

**Tags**: `#inference-optimization`, `#local-llm`, `#quantization`

---

## AI Daily

<a id="item-ai-daily-1"></a>
### [Fysiverse-UniWAM 24项真机评测双第一](https://mp.weixin.qq.com/s?__biz=MzA3MzI4MjgzMw==&amp;mid=2651071440&amp;idx=1&amp;sn=913d398a504d3e029db48cde218437a2) ⭐️ 5.5/10

机器之心二手报道称，飞捷科思（Fysics AI）联合复旦大学认知与智能技术实验室（CITLab）提出的统一世界动作模型Fysiverse-UniWAM，无需大规模机器人预训练，在24项真机评测中包揽自主导航、移动操作项目的第一名。其中13项导航任务的位置误差全部领先，4项移动操作任务成功率全部第一，平均成功率达80.0%，领先当前最强机器人预训练基线π₀.5达17.5个百分点；MAP-Bench基准测试中该模型平均位置误差9.85厘米、平均朝向误差2.30°，较最强外部基线分别降低30.1%和44.0%。该报道未附官方一手链接且正文严重截断，仅能确认上述评测成绩，无更多可核对的官方发布细节。

rss · 机器之心 · Nov 1, 04:00

**「为什么重要」** 当前主流具身智能模型多依赖大规模机器人预训练作为技术起点，Fysiverse-UniWAM走预训练视频世界模型+共享骨干联合学习的路线，在无需大规模机器人预训练的条件下取得真机评测领先成绩，为行业提供了不同的技术路径参考。

**「可关注」** 可关注：Fysiverse-UniWAM 以预训练视频世界模型为起点，通过共享骨干网络实现导航与操作的联合学习，搭配操作锚定位姿（MAP）与超150万条轨迹、累计约7500小时的MAP-Data数据集，在无需大规模机器人预训练的条件下取得了真机评测领先成绩。

**Tags**: `#model`, `#eval`, `#industry`

---

## AI Deals

<a id="item-ai-deals-1"></a>
### [HikerApi 100次免费抓取额度分享](https://news.ycombinator.com/item?id=50327394) ⭐️ 6.0/10

Hacker News用户aziktazik 2026年11月1日分享称，使用HikerApi获取Instagram公开数据时获得100次免费测试API请求，付费请求单价为0.001美元。该用户表示该服务无使用限制、响应速度快，推荐给有Instagram抓取需求的开发者。当前无官方信息确认该免费额度是否公开开放、有效期及地区限制。

rss · HN Free API / Credits · Nov 1, 17:00

**「为什么重要」** 该信息仅为个人使用分享，无官方渠道验证免费额度的可领性、有效期及相关限制，参考价值有限，可留意HikerApi官方后续的公开活动。

**「可关注」** 可关注：HikerApi的Instagram抓取API付费单价为0.001美元/次，有测试需求的开发者可留意其免费测试额度的公开领取渠道。

**Tags**: `#credits`, `#api`, `#promo`

---