---
layout: default
title: "Horizon Summary: 2026-11-16 (ZH)"
date: 2026-11-16
lang: zh
---

> 从 143 条内容中筛选出 9 条重要资讯。

<nav id="ah-toc" class="ah-toc" aria-label="目录"><span class="ah-toc-title">目录</span><ul><li><a href="#sec-harness-arch"><span class="ah-toc-name">Harness 架构</span><span class="ah-toc-count">2条</span></a></li><li><a href="#sec-agent-engineer"><span class="ah-toc-name">Agent 工程师日报</span><span class="ah-toc-count">4条</span></a></li><li><a href="#sec-ai-daily"><span class="ah-toc-name">AI 日报</span><span class="ah-toc-count">2条</span></a></li><li><a href="#sec-ai-deals"><span class="ah-toc-name">AI 羊毛</span><span class="ah-toc-count">1条</span></a></li></ul></nav>

---

**[Harness 架构](#sec-harness-arch)**
1. [langchain-deepseek 1.2.0 发布](#item-harness-arch-1) ⭐️ 6.8/10
2. [browser-use 1.0.6 发布](#item-harness-arch-2) ⭐️ 5.5/10

**[Agent 工程师日报](#sec-agent-engineer)**
1. [现代 LLM 位置编码机制详解](#item-agent-engineer-1) ⭐️ 6.0/10
2. [datasette-apps 0.4a0 发布](#item-agent-engineer-2) ⭐️ 6.0/10
3. [Basalt 0.4.0 发布 新增多模型路由](#item-agent-engineer-3) ⭐️ 6.0/10
4. [Datasette 1.0a43 发布](#item-agent-engineer-4) ⭐️ 5.5/10

**[AI 日报](#sec-ai-daily)**
1. [OpenAI 发布格点标准模型候选定义](#item-ai-daily-1) ⭐️ 6.8/10
2. [OpenAI 科学博客正式上线](#item-ai-daily-2) ⭐️ 5.8/10

**[AI 羊毛](#sec-ai-deals)**
1. [离音 1.7.3 更新 送永久 Pro 码](#item-ai-deals-1) ⭐️ 7.0/10

---

## Harness 架构
{: #sec-harness-arch .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-harness-arch" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-harness-arch-1"></a>
### [langchain-deepseek 1.2.0 发布](https://github.com/langchain-ai/langchain/releases/tag/langchain-deepseek%3D%3D1.2.0) ⭐️ 6.8/10

langchain-ai/langchain 发布 langchain-deepseek 1.2.0。该版本将 ChatDeepSeek 路由至 LangSmith gateway，移除已终止支持的 Python 3.10，并刷新模型配置文件与依赖版本。这是 DeepSeek 集成包的行为变更，不影响核心 agent 架构。

github · github-actions\[bot\] · 11月15日 21:34

**「改了什么」** ChatDeepSeek 默认经 LangSmith gateway 转发请求；终止 Python 3.10 支持，需升级至 3.11+；同步更新 certifi、urllib3 等依赖及模型参数配置。

**标签**: `#runtime`, `#tools`

---

<a id="item-harness-arch-2"></a>
### [browser-use 1.0.6 发布](https://github.com/browser-use/browser-use/releases/tag/1.0.6) ⭐️ 5.5/10

browser-use 浏览器自动化库发布 1.0.6 版本。本次更新将默认模型从 bu-fast 切换为 BU 4.0，推理等级从 medium 提升为 high，默认调用成本上涨 15 倍，短测试任务成本从 $0.0014 升至 $0.022。Agent\(task\)、ChatBrowserUse\(\) 默认通过 Browser Use 网关调用 BU 4.0，用户可通过 llm 参数指定 bu-fast、bu-4.0-mini、bu-4.0-pro 等模型控制成本。此外更新了首次运行认证流程，无密钥时打开 Browser Use 登录页，审批后继续执行，云浏览器会输出实时预览链接；同时修复 Judge 组件输出脱离运行观测的 grounding 问题。

github · sarath-menon · 11月16日 00:51

**「设计要点」** 运行时默认通过 Browser Use 官方网关调用模型，Judge 组件的输出约束为当前运行观测到的内容，避免生成脱离实际执行过程的结论。

**「改了什么」** 默认模型从 bu-fast 切换为 BU 4.0，推理等级提升，默认调用成本上涨 15 倍；新增 llm 参数支持用户手动指定模型以控制成本。首次运行无密钥时改为走官方登录审批流程，云浏览器新增实时预览链接输出；修复 Judge 组件输出脱离运行观测的 grounding 问题。

**「评论」** 暂无社区评论可用。

**标签**: `#tools`, `#eval`

---

## Agent 工程师日报
{: #sec-agent-engineer .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-agent-engineer" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-agent-engineer-1"></a>
### [现代 LLM 位置编码机制详解](https://magazine.sebastianraschka.com/p/understanding-positional-embeddings) ⭐️ 6.0/10

2026 年 11 月 15 日，Sebastian Raschka 发布技术长文系统讲解 LLM 位置编码机制，覆盖从 GPT-2 绝对位置编码到 RoPE 等相对位置编码的原理、可视化、数学推导与 PyTorch 实现，同时整理 2026 年主流开源权重模型的位置编码选型。文章假设读者熟悉基础 LLM 架构，是作者后续 LLM 架构趋势分析的前置参考资料，对 agent 工程、工具链优化等近期工作流无直接可落地改进。

rss · Sebastian Raschka · 11月15日 12:10 · [社区讨论](https://news.ycombinator.com/item?id=50506376)

**「为什么重要」** 本文是当前少有的系统梳理位置编码全链路的技术材料，填补了作者此前未单独覆盖该模块的空白，可作为理解 2026 年 LLM 架构趋势的前置参考资料。

**「可关注」** 可关注：位置编码是 LLM 上下文窗口能力的核心基础组件，2026 年主流开源模型已普遍采用 RoPE 等相对位置编码方案，理解其机制有助于排查长上下文相关的模型行为问题。

**「评论」** 社区评论指出本文聚焦实现层面讲解，若要从理论层面彻底理解位置编码，需结合群表示论相关知识，如 RoPE 本质是平移群的表示。

**标签**: `#memory`, `#architecture`

---

<a id="item-agent-engineer-2"></a>
### [datasette-apps 0.4a0 发布](https://simonwillison.net/2026/Nov/15/datasette-apps/) ⭐️ 6.0/10

2026 年 11 月 15 日，datasette-apps 0.4a0 正式发布，新增 URL fragment 链接支持，沙盒应用可通过 URL fragment 实现相互引用。该版本同时将支持的 URL scheme 回传给 Datasette Agent，使其能够辅助生成可互链的沙盒 SQL 应用，例如支持搜索类应用跳转至详情类应用查看特定记录。该功能主要面向 Datasette 生态的工程师与沙盒 SQL 应用开发者。

rss · Simon Willison · 11月15日 04:02

**「为什么重要」** 该功能填补了 Datasette 沙盒应用此前无法原生互链的空白，开发者无需手动处理跨应用跳转逻辑，可直接构建关联应用场景，降低互链应用的开发门槛。

**「可关注」** 可关注：datasette-apps 的 URL fragment 机制为沙盒 SQL 应用提供了原生互链能力，配合 Datasette Agent 可降低互链应用的开发成本。

**标签**: `#coding-agent`, `#orchestration`, `#harness`

---

<a id="item-agent-engineer-3"></a>
### [Basalt 0.4.0 发布 新增多模型路由](https://www.reddit.com/r/LocalLLaMA/comments/1xx1cu9/basalt_040_more_models_still_as_fast_qwen_27b_up/) ⭐️ 6.0/10

Basalt 项目维护者 2026 年 11 月 15 日在 Reddit 宣布 v0.4.0 版本发布，新增多模型路由（首个支持 DeepSeek V4.1 Flash，IQ1\_M 量化版在 RTX 5090+5060 Ti 上对话速度 90 tok/s、结构化输出 246 tok/s）、视频/文件聊天功能，上线首款稠密模型 Qwen 3.8 27B NVFP4 量化版。该量化版在 RTX 5090 上结构化输出最高达 776 tok/s，对话速度 262 tok/s，prose 生成 194 tok/s，prefill 速度 12000 tok/s（4k 上下文，随上下文增长下降），top-1 准确率 92.8%匹配全 BF16 模型（KLD 0.0262），支持最高 262K 上下文，覆盖聊天、工具调用、思维链、图像视频能力。来源为社区帖子，非官方 Release Notes，工具社区采用度有限。

reddit · r/LocalLLaMA · /u/jesdga95 · 11月15日 17:30

**「为什么重要」** 该版本的多模型路由、多模态聊天能力及量化模型的性能精度数据有具体可验证指标，对搭建本地模型支撑的 agent 系统的工程师有参考价值，但来源为社区自发帖子、工具主流采用度不高，不属于高优先级阅读内容。

**「可关注」** 可关注：Basalt 0.4.0 的 Qwen 3.8 27B NVFP4 量化版在 RTX 5090 上的结构化输出吞吐、与 BF16 模型的精度匹配实测数据，以及多模型路由、多模态聊天的功能落地情况。

**标签**: `#harness`, `#orchestration`, `#eval`

---

<a id="item-agent-engineer-4"></a>
### [Datasette 1.0a43 发布](https://github.com/simonw/datasette/releases/tag/1.0a43) ⭐️ 5.5/10

simonw 于 2026-11-15 发布 Datasette 1.0a43 alpha 版本，修复两个安全漏洞：一是 1.0a31 至 1.0a42 版本中，\`/-/queries\` 等页面的 \`?owner\_id=\` 过滤可泄露任意用户的私有存储查询（含 SQL）；二是通过 \`add\_database\(db, name=..., route=...\)\` 注册的自定义 route 数据库存在下载权限绕过，对应修复已 backport 至稳定版 0.65.6 分支。该版本同时将 CSV/TSV 导出改为流式输出渲染器，调整单行 JSON 返回格式（添加 \`?\_shape=objects\` 参数可恢复旧格式），首页与数据库页的表格列表改为卡片展示，包含多项 breaking change：输出渲染器 \`render\` 函数须返回 \`Response\` 对象、SQL 查询页的 \`view\_name\` 变更为 \`query\`、流式导出失败时直接断开连接而非写入错误信息，\`allow\_csv\_stream\` 与 \`max\_csv\_mb\` 设置项也更名为 \`default\_allow\_stream\` 与 \`max\_stream\_mb\`，旧名称仍可兼容使用。

github · simonw · 11月15日 23:20

**「为什么重要」** 两个安全漏洞可导致未授权用户获取私有查询内容和受限数据库文件，影响使用 1.0a31 至 1.0a42 版本部署的 Datasette 实例；多项 breaking change 会直接影响自定义插件和接口调用方的兼容性，流式导出错误处理逻辑的调整也会改变工具对导出失败的感知方式。

**「可关注」** 可关注：若部署了 1.0a31 至 1.0a42 版本的 Datasette 实例需尽快升级修复安全漏洞；若自定义了输出渲染器、调用了单行 JSON 接口或编写了存储查询权限规则，需适配本次 breaking change；若插件复制过 1.0a20 升级指南的 \`permission\_resources\_sql\(\)\` 示例，需补充 \`if action == &quot;permissions-debug&quot;\` 检查避免权限泄露。

**标签**: `#permissions`, `#observability`

---

## AI 日报
{: #sec-ai-daily .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-daily" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-daily-1"></a>
### [OpenAI 发布格点标准模型候选定义](https://openai.com/index/step-toward-defining-the-standard-model) ⭐️ 6.8/10

OpenAI 声称的官方博客发布候选非微扰格点标准模型定义相关研究，称 GPT-6 Astra 模型辅助完成了该研究的详细证明。当前公开披露的信息极少，未说明该研究与过往工作的创新性差异、模型的具体贡献细节。

rss · OpenAI Blog · 11月15日 22:00

**「可关注」** 可关注：后续公开的完整研究内容与 GPT-6 Astra 参与证明的具体细节。

**标签**: `#lab`, `#model`

---

<a id="item-ai-daily-2"></a>
### [OpenAI 科学博客正式上线](https://openai.com/index/our-new-blog-for-science) ⭐️ 5.8/10

OpenAI 官方于 2026 年 11 月 15 日宣布正式上线全新科学博客。该博客定位为发布 AI 助力科学发现的新研究发现、实用方法及研究者的第一手经验。目前公开信息仅包含博客基础定位，无更多具体内容或更新计划披露。

rss · OpenAI Blog · 11月15日 22:00

**「为什么重要」** 这是 OpenAI 首次单独设立科学领域内容发布渠道，后续可观察其 AI for Science 方向的研究公开节奏与内容侧重。

**「可关注」** 可关注：该博客后续发布的 AI for Science 实用方法、研究复现相关公开内容。

**标签**: `#lab`, `#product`

---

## AI 羊毛
{: #sec-ai-deals .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-deals" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-deals-1"></a>
### [离音 1.7.3 更新 送永久 Pro 码](https://www.v2ex.com/t/1257232#reply8) ⭐️ 7.0/10

V2EX 开发者 andyiac 分享离线音乐播放器「离音」1.7.3 版本更新，同时发放 10 个该应用永久 Pro 版兑换码。应用支持 iPhone / iPad / Apple 芯片 Mac，无账号、无广告、不上传音频，免费下载，Pro 为一次性买断无订阅，支持 APE/FLAC/DSD 等音频格式、10 段均衡器、Wi-Fi 传歌等功能，兑换码可直接使用，无额外领取门槛说明。

rss · V2EX Hot · 11月15日 11:41

**「为什么重要」** 当前发放的兑换码可免费获取「离音」永久 Pro 权限，Pro 为一次性买断无订阅模式，无后续付费成本，且应用纯本地运行无数据上传。

**「可关注」** 可关注：离音 1.7.3 新增 WebDAV 单向导入（不做双向同步）、Apple 芯片 Mac 原生运行（Intel 机型不支持）、APE 实时解码（仅支持立体声，多声道 APE 直接拒绝播放）、睡眠定时独立成页等功能，Pro 权益包含 DSD/APE 播放、自定义 EQ 调音、全部主题与播放器样式等，兑换码可直接使用。

**标签**: `#promo`, `#limited-free`, `#coupon`, `#free-tier`

---