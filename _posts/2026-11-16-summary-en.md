---
layout: default
title: "Horizon Summary: 2026-11-16 (EN)"
date: 2026-11-16
lang: en
---

> From 143 items, 9 important content pieces were selected

---

**Agent Harness Architecture**
1. [langchain-deepseek 1.2.0 发布](#item-harness-arch-1) ⭐️ 6.8/10
2. [browser-use 1.0.6 发布](#item-harness-arch-2) ⭐️ 5.5/10

**AI Agent Engineer**
1. [Raschka 详解 LLM 位置编码](#item-agent-engineer-1) ⭐️ 6.0/10
2. [datasette-apps 0.4a0 发布](#item-agent-engineer-2) ⭐️ 6.0/10
3. [Basalt 0.4.0 发布 支持多模型路由](#item-agent-engineer-3) ⭐️ 6.0/10
4. [Datasette 1.0a43 发布：修复权限漏洞](#item-agent-engineer-4) ⭐️ 5.5/10

**AI Daily**
1. [OpenAI 博客：晶格标准模型候选定义](#item-ai-daily-1) ⭐️ 6.8/10
2. [OpenAI 上线科学博客](#item-ai-daily-2) ⭐️ 5.8/10

**AI Deals**
1. [离音 1.7.3 更新 送永久 Pro 码](#item-ai-deals-1) ⭐️ 7.0/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [langchain-deepseek 1.2.0 发布](https://github.com/langchain-ai/langchain/releases/tag/langchain-deepseek%3D%3D1.2.0) ⭐️ 6.8/10

langchain-ai/langchain 发布 partner 包 langchain-deepseek 1.2.0。本次将 ChatDeepSeek 路由切换至 LangSmith gateway。同时移除已 EOL 的 Python 3.10 支持，并更新 certifi、urllib3 等依赖及模型配置。

github · github-actions\[bot\] · Nov 15, 21:34

**「改了什么」** ChatDeepSeek 改经 LangSmith gateway 路由。移除 Python 3.10 支持（破坏性变更）。依赖项 certifi、urllib3 升级，模型 profile 刷新。

**Tags**: `#runtime`, `#tools`

---

<a id="item-harness-arch-2"></a>
### [browser-use 1.0.6 发布](https://github.com/browser-use/browser-use/releases/tag/1.0.6) ⭐️ 5.5/10

browser-use 1.0.6 将 \`Agent\(task\)\` 与 \`ChatBrowserUse\(\)\` 的默认模型从 \`bu-fast\` 切换至 Browser Use 网关的 \`bu-4.0\`，推理等级从 medium 升到 high，默认调用成本上涨约 15 倍。用户传 \`llm=&\#x27;bu-fast&\#x27;\` 可保留旧模型与价格，或选 \`llm=&\#x27;bu-4.0-mini&\#x27;\`、\`llm=&\#x27;bu-4.0-pro&\#x27;\` 按任务难度分级。首跑认证流程改为打开 Browser Use 登录页，审批后继续，云浏览器输出实时预览链接。Judge 组件的 grounding 行为修复，确保判断仅基于运行观测。

github · sarath-menon · Nov 16, 00:51

**「改了什么」** 默认模型从 \`bu-fast\` 切换为 \`bu-4.0\`，输入输出 token 价格分别从 $0.12 / $0.60 涨至 $1.80 / $9.00 每百万。首跑认证改为浏览器登录审批，Judge grounding 收紧至运行观测。

**Tags**: `#tools`, `#eval`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [Raschka 详解 LLM 位置编码](https://magazine.sebastianraschka.com/p/understanding-positional-embeddings) ⭐️ 6.0/10

Sebastian Raschka 于 2026-11-15 发布技术长文，系统梳理 LLM 位置编码机制，包括 RoPE、GPT-2 学习式绝对位置嵌入及 2026 年开源模型的实际选型。文章通过可视化、数学公式和 PyTorch 代码实现，解释位置信息如何注入 Transformer 架构。内容聚焦基础架构原理，对 agent 工程、harness 设计或工具链改进无直接可执行动作。

rss · Sebastian Raschka · Nov 15, 12:10 · [Discussion](https://news.ycombinator.com/item?id=50506376)

**「为什么重要」** 文章为理解上下文窗口机制提供基础，适合需要阅读模型架构文档的工程师。但材料未表明该知识会在短期内改变现有 agent 系统的行为或性能。

**「可关注」** 可关注：位置编码方案（如 RoPE）决定上下文窗口的扩展与泛化方式，评估新模型时需核对其位置策略与现有 harness 的兼容性。

**「评论」** 社区评论指出，真正理解位置编码需从群表示论出发，RoPE 本质是平移群的表示，这为参数化与可微学习提供理论框架。

**Tags**: `#memory`, `#architecture`

---

<a id="item-agent-engineer-2"></a>
### [datasette-apps 0.4a0 发布](https://simonwillison.net/2026/Nov/15/datasette-apps/) ⭐️ 6.0/10

2026年11月15日，datasette-apps 0.4a0正式发布，新增URL fragment链接支持：沙盒应用可识别并使用URL中的fragment参数，同时支持的URL scheme会回传给Datasette Agent，使其能够辅助生成可相互引用的沙盒SQL应用。该功能支持例如独立的应用A展示特定记录详情、独立的应用B搜索记录并链接到应用A对应页面的场景，主要影响Datasette生态的工程师与沙盒SQL应用开发者。

rss · Simon Willison · Nov 15, 04:02

**「为什么重要」** 已发生的变更填补了Datasette沙盒应用间的原生互链能力空白，让Agent辅助生成关联应用的场景成为可能；尚未证实的是该机制是否会成为Datasette工具链的标准互连模式，或推动其他SQL沙盒工具跟进类似设计。

**「可关注」** Datasette沙盒应用可通过URL fragment实现轻量互链，无需额外后端路由配置。

**Tags**: `#coding-agent`, `#orchestration`, `#harness`

---

<a id="item-agent-engineer-3"></a>
### [Basalt 0.4.0 发布 支持多模型路由](https://www.reddit.com/r/LocalLLaMA/comments/1xx1cu9/basalt_040_more_models_still_as_fast_qwen_27b_up/) ⭐️ 6.0/10

Basalt 0.4.0 于 2026-11-15 由维护者 /u/jesdga95 在 Reddit 发布，新增多模型路由（首发 DeepSeek V4.1 Flash，IQ1\_M 量化在 5090+5060 Ti 上对话 90 tok/s、结构化 246 tok/s）、视频与文件聊天，并引入首个 dense 模型 Qwen 3 27B NVFP4。在 RTX 5090 单流下，该模型结构化输出最高 776 tok/s，对话 262 tok/s，prose 194 tok/s，4k 上下文预填充约 12,000 tok/s。精度方面，top-1 准确率 92.8%，对比全 BF16 基线的 KLD 为 0.0262，支持最高 262K 上下文。信息来源于社区 Reddit 帖子，非官方发布说明，且工具主流采用度有限。

reddit · r/LocalLLaMA · /u/jesdga95 · Nov 15, 17:30

**「为什么重要」** 该更新展示了社区驱动的本地推理 harness 在 dense kernel 优化上的具体进展，量化精度接近全 BF16 基线。但因其来源为单一维护者帖子且工具采用度有限，实际影响与可复现性仍需独立验证。

**「可关注」** 可关注：Basalt 在 RTX 5090 上对 Qwen 3 27B NVFP4 跑出 776 tok/s 结构化输出，同时保持 92.8% BF16 级 top-1 准确率，提示 dense 量化 kernel 可能已接近实用，但数据来自单一社区帖子，复现前应谨慎评估。

**Tags**: `#harness`, `#orchestration`, `#eval`

---

<a id="item-agent-engineer-4"></a>
### [Datasette 1.0a43 发布：修复权限漏洞](https://github.com/simonw/datasette/releases/tag/1.0a43) ⭐️ 5.5/10

Datasette 1.0a43 于 2026-11-15 发布，修复两个安全漏洞：\`/-/queries\` 页面的 \`?owner\_id=\` 过滤泄露私有存储查询（含 SQL），影响 1.0a31–1.0a42；以及数据库下载权限绕过，当 \`add\_database\` 的 route 与 name 不一致时发生。本次更新将 CSV/TSV 导出改为流式渲染器，单行 JSON 格式改为 \`\{&quot;row&quot;: \{...\}\}\`，并调整渲染器返回值和插件钩子参数。运行受影响版本或自定义输出渲染器的开发者需验证兼容性；数据库下载修复已反向移植至 0.65.6。

github · simonw · Nov 15, 23:20

**「为什么重要」** 两个权限漏洞直接扩大未授权数据访问范围，运行 1.0a31–1.0a42 的实例需立即升级。单行 JSON 与渲染器接口的破坏性变更可能中断 agent 对 Datasette 数据格式的依赖，需核对 \`?\_shape=objects\` 兼容方案。

**「可关注」** 可关注：若插件复制了升级指南中缺失 \`permissions-debug\` 检查的 \`permission\_resources\_sql\(\)\` 示例，将导致匿名用户获得全部写操作权限，需立即审计自定义权限插件。

**Tags**: `#permissions`, `#observability`

---

## AI Daily

<a id="item-ai-daily-1"></a>
### [OpenAI 博客：晶格标准模型候选定义](https://openai.com/index/step-toward-defining-the-standard-model) ⭐️ 6.8/10

OpenAI 博客 RSS 源分享一篇候选非微扰晶格标准模型定义。文章称 GPT-6 Astra 模型协助将想法转化为详细证明。目前公开内容仅此一句描述，未披露具体数学构造、与先前工作的对比或模型介入细节。

rss · OpenAI Blog · Nov 15, 22:00

**「可关注」** 可关注：公开内容未披露模型具体介入方式与证明细节。

**Tags**: `#lab`, `#model`

---

<a id="item-ai-daily-2"></a>
### [OpenAI 上线科学博客](https://openai.com/index/our-new-blog-for-science) ⭐️ 5.8/10

OpenAI 于 2026 年 11 月 15 日正式上线全新科学博客，该博客用于发布 AI 助力科学发现的新研究成果、实用方法，以及相关研究者的第一手经验。目前公开披露的信息仅明确博客定位，无更多具体内容细节。

rss · OpenAI Blog · Nov 15, 22:00

**「为什么重要」** 该博客是 OpenAI 集中输出 AI 科研领域内容的官方渠道，方便相关研究者与从业者获取一手研究与实践信息。

**「可关注」** 可关注：OpenAI 官方科学博客已上线，可定期查看 AI 辅助科研相关的研究成果与实践方法。

**Tags**: `#lab`, `#product`

---

## AI Deals

<a id="item-ai-deals-1"></a>
### [离音 1.7.3 更新 送永久 Pro 码](https://www.v2ex.com/t/1257232#reply8) ⭐️ 7.0/10

V2EX 开发者 andyiac 分享支持 iPhone / iPad / Apple 芯片 Mac 的离线音乐播放器「离音」1.7.3 版本更新，同时发放 10 个该应用永久 Pro 版兑换码。应用免费下载，Pro 为一次性买断制（无订阅），包含 DSD/APE 播放、10 段均衡器、睡眠定时等权益。材料未说明具体领取规则与截止时间。

rss · V2EX Hot · Nov 15, 11:41

**「为什么重要」** 该播放器无账号、无广告、不上传音频，纯本地运行，支持 19 种音频格式及内嵌 CUE 解析，本次发放的永久 Pro 兑换码可无期限解锁全部付费权益。

**「可关注」** 可关注：离音播放 APE 文件时采用边读边解码方案，不做缓存转码，仅支持立体声输出，多声道 APE 会直接拒绝播放。

**Tags**: `#promo`, `#limited-free`, `#coupon`, `#free-tier`

---