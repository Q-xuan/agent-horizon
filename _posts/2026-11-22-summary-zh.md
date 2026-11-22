---
layout: default
title: "Horizon Summary: 2026-11-22 (ZH)"
date: 2026-11-22
lang: zh
---

> 从 161 条内容中筛选出 7 条重要资讯。

<nav id="ah-toc" class="ah-toc" aria-label="目录"><span class="ah-toc-title">目录</span><ul><li><a href="#sec-harness-arch"><span class="ah-toc-name">Harness 架构</span><span class="ah-toc-count">1条</span></a></li><li><a href="#sec-ai-daily"><span class="ah-toc-name">AI 日报</span><span class="ah-toc-count">3条</span></a></li><li><a href="#sec-ai-deals"><span class="ah-toc-name">AI 羊毛</span><span class="ah-toc-count">3条</span></a></li></ul></nav>

---

**[Harness 架构](#sec-harness-arch)**
1. [Cline CLI v3.0.75 发布](#item-harness-arch-1) ⭐️ 5.5/10

**[AI 日报](#sec-ai-daily)**
1. [腾讯元宝×KCL 发布群聊 Agent 记忆基准](#item-ai-daily-1) ⭐️ 5.5/10
2. [Karpo Decision 31B 开源 浏览器 Agent 双赢](#item-ai-daily-2) ⭐️ 5.5/10
3. [TML 开源 Inkling 2 Mini 循环 Transformer](#item-ai-daily-3) ⭐️ 5.5/10

**[AI 羊毛](#sec-ai-deals)**
1. [Google AI Pro 黑五五折 老用户可提前领](#item-ai-deals-1) ⭐️ 8.0/10
2. [AIask Opus 5.5 限时一折](#item-ai-deals-2) ⭐️ 8.0/10
3. [File Organizer 兑换码限量发放](#item-ai-deals-3) ⭐️ 8.0/10

---

## Harness 架构
{: #sec-harness-arch .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-harness-arch" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-harness-arch-1"></a>
### [Cline CLI v3.0.75 发布](https://github.com/cline/cline/releases/tag/cli-v3.0.75) ⭐️ 5.5/10

Cline CLI v3.0.75 将 one-shot run 默认模式从 act 切至 yolo，无人值守时自动批准工具；\`--timeout\` 与 Ctrl+C 现可中断首轮执行。无保存模型时 Cline provider 从第一个可用模型启动，而非默认 Claude Sonnet 5.5；\`read\_files\` 结果上限从 8k 字符提升至 2000 行或约 48k 字符。CLI 不再读取启动目录的 \`.env\` 与 \`bunfig.toml\`，移除 \`CLINE\_CAPTURE\_\*\` 调试变量，并将 undici 升级至 7.30.1。模型层修复 Reflection Beam 在 compaction 后的 400 错误，调整 reasoning effort 传递逻辑，使高 reasoning level 能正确到达 GPT-5.x/o-series 与自定义模型。

github · github-actions\[bot\] · 11月21日 05:30

**「设计要点」** 运行时通过区分 one-shot 与交互模式控制工具批准策略，yolo mode 下无 team tools。工具层将 \`read\_files\` 截断逻辑上移至模型上下文，保留 2000 行硬上限；模型适配层修复 \`reasoning\_effort: &quot;none&quot;\` 的拒绝问题，并在原生 OpenAI provider 按模型能力映射 reasoning level。

**「改了什么」** One-shot run 默认行为从 act mode 切至 yolo mode，除非显式指定 \`--act\` 或满足保留条件。\`read\_files\` 不再截断至 8k 字符，上限为 2000 行或约 48k 字符；Compaction 与模型切换后 Reflection Beam 的 400 错误消除，LiteLLM 停止使用遗留 \`max\_tokens\` 作为输入预算。

**标签**: `#runtime`, `#tools`, `#permissions`

---

## AI 日报
{: #sec-ai-daily .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-daily" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-daily-1"></a>
### [腾讯元宝×KCL 发布群聊 Agent 记忆基准](https://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw==&amp;mid=2247947677&amp;idx=3&amp;sn=0797fbd2116a405b44176c97577757d8) ⭐️ 5.5/10

据二手科技媒体量子位报道，腾讯元宝联合伦敦国王学院 NLP 团队发布首个基于群聊构建的 Agent 记忆基准 GroupAssistBench。该基准基于 50 个真实群聊的 80299 条历史消息构建 2395 道评测题，对比测试了 14 组配置。测试显示 EverMemOS 在 L1 记忆召回评测中得 0.621，高于同模型完整上下文配置的 0.570；但在 L2 开放式服务评测中仅得 0.247，低于完整上下文配置的 0.431。

rss · 量子位 · 11月21日 09:52

**「为什么重要」** 当前 Agent 记忆评测多聚焦单聊或通用场景，该基准首次以真实群聊为载体区分记忆召回与实际服务能力，可更准确衡量 Agent 在多人交互场景下的记忆应用水平。

**「可关注」** 可关注：Agent 记忆召回得分高不代表实际服务能力达标，需结合场景化任务综合评估。

**标签**: `#agent`, `#lab`, `#industry`, `#eval`

---

<a id="item-ai-daily-2"></a>
### [Karpo Decision 31B 开源 浏览器 Agent 双赢](https://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw==&amp;mid=2247947677&amp;idx=1&amp;sn=ebf1f96b9afceacdfa0d407ecdb3ff2b) ⭐️ 5.5/10

量子位报道 MachinePulse AI 开源的 Karpo Decision 31B 决策模型在《城市扫描仪》挑战中，完成指定筛选任务的速度达 Gemini 3.5 Flash 的 6 倍，成本仅为后者的 1/13，36 道题准确率为 100%；该模型在 Decision Index 评测总榜以 73.9 分位列第一，单题最多可同时判断 255 个候选选项，校准误差 2.3%，单张 RTX PRO 6000 部署时中位响应时间 94 毫秒。同时 MachinePulse AI 还将采用 System 1 + System 2 架构的 karpo-browser 浏览器操作框架、网页动作决策模型 Karpo Decision 27B Act 及评测集 KBB 一并开源。

rss · 量子位 · 11月21日 09:52

**「为什么重要」** 该模型及配套框架专为 Agent 高频决策场景设计，可支撑浏览器操作、工具调用等 Agent 核心环节的快速判断，开源后降低了相关场景的部署使用门槛。

**「可关注」** 可关注：Karpo Decision 31B 单张 RTX PRO 6000 即可部署，中位响应时间 94 毫秒，适配对延迟敏感的 Agent 决策场景。

**标签**: `#model`, `#open-source`, `#industry`, `#eval`, `#agent`

---

<a id="item-ai-daily-3"></a>
### [TML 开源 Inkling 2 Mini 循环 Transformer](https://mp.weixin.qq.com/s?__biz=MzA3MzI4MjgzMw==&amp;mid=2651075624&amp;idx=2&amp;sn=b6e7e23d631dba7a952cbe5da8e77769) ⭐️ 5.5/10

Thinking Machines Lab（TML）发布并开源 26B 参数循环 Transformer 多模态模型 Inkling 2 Mini，支持文本与图像输入，最大上下文窗口 100 万 token，权重按 Apache 2.0 许可发布，已上线 HuggingFace 与官方博客。模型总参数 26B，激活参数约 3.4B，计入循环重复计算后有效激活参数约 5.4B，AA Index 得分 20.1。官方宣称其可在笔记本运行，演示使用配备 48GB 内存的 M5 Pro MacBook Pro 离线完成推理，可胜任智能体任务，包括数分钟内写出可玩飞行模拟器、驱动 20 位村民的微型像素小镇 Thinkyville 等。

rss · 机器之心 · 11月21日 04:11

**「为什么重要」** 该模型验证了循环 Transformer 架构在端侧部署的可行性，其开源权重与宽松许可降低了开发者本地部署多模态智能体模型的门槛，配套的智能体任务演示也为端侧模型能力边界提供了新的参考。

**「可关注」** 可关注：Inkling 2 Mini 的循环 Transformer 架构将 24 层中最前、最后 6 层各运行 1 次，中间 12 层运行 3 次，使每个 token 完成 48 次层计算，搭配 MoE 将激活参数压至 3.4B，在控制权重体积的同时提升了连续任务的处理能力，为端侧大模型部署提供了新的架构思路。

**「评论」** 社区反馈较为积极，已有开发者将其接入 DeepSeek Harness 获得较快推理速度，还有用户测试其可玩通关电子游戏并学会速通，也能完成动画 MV 生成任务。

**标签**: `#open-source`, `#model`, `#lab`, `#eval`

---

## AI 羊毛
{: #sec-ai-deals .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-deals" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-deals-1"></a>
### [Google AI Pro 黑五五折 老用户可提前领](https://www.appinn.com/google-ai-pro-black-friday-2026/) ⭐️ 8.0/10

你看到的内容可能由第三方 AI 基于小众软件文章提炼总结而成，可能与原文真实意图存在偏差。不代表小众软件观点和立场。请&lt;a href=&quot;https://www.appinn.com/google-ai-pro-black-friday-2026/&quot; target=&quot;\_blank&quot;&gt;点击链接阅读原文&lt;/a&gt;细致比对和校验。&lt;br /&gt;&lt;br /&gt;Google AI Pro/Plus 开启黑五促销，美区年付原价 199.99 美元/年，最高五折后约 99.99 美元/年，折合每月 8.33 美元。11 月 20～26 日现有 Google One、Google AI 订阅用户可提前参与，11 月 27 日起向新用户开放。不同账户显示的折扣可能不同，后续续费可能恢复正常价格，优惠仅适用于首个优惠周期。

rss · 小众软件 · 11月21日 11:14

**「为什么重要」** 对于常使用 Gemini、NotebookLM 或已付费购买 Google One 存储的用户，本次五折优惠包含 5TB 云存储与相关增强功能，且老用户无需等待新用户开放窗口即可参与，性价比高于学生版或第三方合作优惠。

**「可关注」** 可关注：美区符合条件用户可在 11 月 20～26 日优先查看优惠，已订阅 Google One 的用户建议通过官方「更改会员方案」路径升级，无需先取消原订阅。

**「评论」** 有参与用户分享称学生身份 Google One Pro 验证流程不稳定，且受限版 Pro 无法使用 Gemini 4，小米合作优惠也出现掉车情况，因此选择参与本次黑五美区年付优惠。

**标签**: `#promo`, `#coupon`, `#limited-offer`, `#subscription`

---

<a id="item-ai-deals-2"></a>
### [AIask Opus 5.5 限时一折](https://www.v2ex.com/t/1258730#reply18) ⭐️ 8.0/10

AIask 平台推出 Claude Opus 5.5 限时 5 天一折促销活动，输入价格为$0.4/M tokens，输出价格为$2/M tokens。老用户在对应 V2EX 帖子下回复个人 ID 即可领取对应福利，平台注册地址为 https://aiask.me。

rss · V2EX Hot · 11月21日 04:59

**「为什么重要」** 该活动为 Claude Opus 5.5 提供一折优惠，属于短期限时促销，对于有该模型 API 调用需求的用户而言是难得的低成本获取渠道。

**「可关注」** 可关注：老用户需在对应 V2EX 帖子下回复个人 ID 领取福利；调用 Claude Opus 5.5 需创建 API 密钥并配置至“组合”分组的“默认”分组，具体价格可在平台模型广场查看。

**标签**: `#promo`, `#api`, `#credits`, `#limited-free`

---

<a id="item-ai-deals-3"></a>
### [File Organizer 兑换码限量发放](https://www.v2ex.com/t/1258731#reply17) ⭐️ 8.0/10

V2EX 开发者 sakishum 放出 30 枚 macOS 文件整理工具 File Organizer 的 App Store 限量免费兑换码，V2EX 用户可先到先得兑换。兑换后即可免费下载安装该应用，支持按类型/日期规则整理文件、自动归档、批量重命名等功能，所有处理均在本地完成。

rss · V2EX Hot · 11月21日 05:03

**「为什么重要」** 本次兑换码为黑五回馈限量发放，先到先得，领完即无免费获取该应用的渠道。

**「可关注」** 可关注：该工具完全在本地处理文件，无需上传数据，适合对文件隐私敏感的用户。

**标签**: `#promo`, `#limited-free`, `#coupon`

---