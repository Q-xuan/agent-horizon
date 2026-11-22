---
layout: default
title: "Horizon Summary: 2026-11-22 (ZH)"
date: 2026-11-22
lang: zh
---

> 从 164 条内容中筛选出 8 条重要资讯。

<nav id="ah-toc" class="ah-toc" aria-label="目录"><span class="ah-toc-title">目录</span><ul><li><a href="#sec-harness-arch"><span class="ah-toc-name">Harness 架构</span><span class="ah-toc-count">2条</span></a></li><li><a href="#sec-ai-daily"><span class="ah-toc-name">AI 日报</span><span class="ah-toc-count">3条</span></a></li><li><a href="#sec-ai-deals"><span class="ah-toc-name">AI 羊毛</span><span class="ah-toc-count">3条</span></a></li></ul></nav>

---

**[Harness 架构](#sec-harness-arch)**
1. [Cline CLI v3.0.75 发布](#item-harness-arch-1) ⭐️ 5.5/10
2. [FastMCP v4.2.4 发布](#item-harness-arch-2) ⭐️ 5.5/10

**[AI 日报](#sec-ai-daily)**
1. [腾讯元宝×KCL 发群聊 Agent 记忆基准](#item-ai-daily-1) ⭐️ 5.5/10
2. [Karpo Decision 31B 开源 速度超 Gemini 6 倍](#item-ai-daily-2) ⭐️ 5.5/10
3. [TML 开源 26B Inkling 2 Mini 循环 Transformer](#item-ai-daily-3) ⭐️ 5.5/10

**[AI 羊毛](#sec-ai-deals)**
1. [AIask Claude Opus 5.5 限时一折](#item-ai-deals-1) ⭐️ 8.0/10
2. [File Organizer 黑五免费兑换码](#item-ai-deals-2) ⭐️ 8.0/10
3. [Gemini 黑五 Pro 半价 转正攻略](#item-ai-deals-3) ⭐️ 8.0/10

---

## Harness 架构
{: #sec-harness-arch .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-harness-arch" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-harness-arch-1"></a>
### [Cline CLI v3.0.75 发布](https://github.com/cline/cline/releases/tag/cli-v3.0.75) ⭐️ 5.5/10

Cline CLI v3.0.75 于 2026-11-21 发布，调整 one-shot run 默认行为、工具输出上限与本地配置加载策略。无交互场景下 one-shot 默认启用 yolo mode，\`read\_files\` 输出上限从 8k 字符提升至约 48k 字符/2000 行。CLI 停止读取启动目录的 \`.env\` 和 \`bunfig.toml\`，并移除 \`CLINE\_CAPTURE\_\*\` 调试变量。模型选择逻辑、reasoning 参数适配及 compaction 行为也有多项修复。

github · github-actions\[bot\] · 11月21日 05:30

**「设计要点」** one-shot run 的 yolo 默认化与本地 .env 加载移除，体现了无交互场景下自动执行与敏感信息隔离的架构收紧。\`read\_files\` 输出上限提升和 reasoning 参数适配修复，反映了工具层与模型层接口的兼容性调整。

**「改了什么」** one-shot run 默认切换至 yolo mode，支持 \`--timeout\` 和 Ctrl+C 中断首轮执行。停止加载本地 \`.env\` 与 \`bunfig.toml\`，\`read\_files\` 输出限制提升至约 48k 字符/2000 行。修复 Reflection Beam 在 compaction 或模型切换后的 400 错误，调整 LiteLLM 的 \`max\_tokens\` 预算逻辑，并刷新模型目录。

**标签**: `#runtime`, `#tools`, `#permissions`, `#configuration`

---

<a id="item-harness-arch-2"></a>
### [FastMCP v4.2.4 发布](https://github.com/PrefectHQ/fastmcp/releases/tag/v4.2.4) ⭐️ 5.5/10

这是 PrefectHQ 开发的 FastMCP 发布的 v4.2.4 补丁版本，核心修复了编号为 GHSA-78c8-3jhx-5mg7 的 OAuth 代理竞争条件漏洞，同时解决了已撤销令牌复用、工具转换失败影响全量列表、挂载/版本化组件行为异常等问题。

github · zzstoatzz · 11月21日 05:24

**「设计要点」** OAuth 代理层对授权码和刷新令牌的兑换逻辑加了并发互斥控制，避免同一凭证被多次兑换；工具转换层实现故障隔离，单工具转换失败仅隐藏对应工具，不再破坏全量工具列表；挂载组件的版本化逻辑修正了重复版本展示、父级 twin 隐藏时的响应逻辑等边界行为。

**「改了什么」** 相对 v4.2.3，本次修复了 OAuth 代理授权码/刷新令牌的并发兑换竞争条件，阻止已撤销的代理访问令牌刷新后重新生效；工具转换失败时仅隐藏对应工具，不再影响全量工具列表；修正了挂载/版本化组件的重复版本展示、隐藏父级 twin 时的响应、合并默认配置破坏调用方对象等行为。

**标签**: `#mcp`, `#tools`, `#permissions`

---

## AI 日报
{: #sec-ai-daily .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-daily" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-daily-1"></a>
### [腾讯元宝×KCL 发群聊 Agent 记忆基准](https://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw==&amp;mid=2247947677&amp;idx=3&amp;sn=0797fbd2116a405b44176c97577757d8) ⭐️ 5.5/10

腾讯元宝联合伦敦国王学院 NLP 团队发布首个群聊场景 Agent 记忆基准 GroupAssistBench。基准基于 50 个真实群聊的 80299 条历史消息构建 2395 道评测题，覆盖 L1 记忆召回、L2 开放式服务两类任务。研究对比完整上下文、检索增强、外部记忆等 14 组配置，发现 EverMemOS 的 L1 召回得分 0.621 高于完整上下文的 0.570，但 L2 服务得分 0.247 低于完整上下文的 0.431，验证了 Agent“记得住”不等于“用得好”的问题。

rss · 量子位 · 11月21日 09:52

**「为什么重要」** 当前 Agent 记忆评测多聚焦单用户场景，该基准首次针对群聊多用户记忆的实用性问题设计量化测试，填补了该场景的评估空白，为群聊 Agent 记忆研发提供了可复用的评测框架。

**「可关注」** 可关注：群聊场景 Agent 记忆的评测需同时覆盖记忆召回准确性和实际服务能力，仅提升召回得分不必然带来服务效果提升。

**标签**: `#eval`, `#lab`, `#product`, `#industry`

---

<a id="item-ai-daily-2"></a>
### [Karpo Decision 31B 开源 速度超 Gemini 6 倍](https://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw==&amp;mid=2247947677&amp;idx=1&amp;sn=ebf1f96b9afceacdfa0d407ecdb3ff2b) ⭐️ 5.5/10

据量子位 2026 年 11 月 21 日二手报道，MachinePulse AI 开源专为 Agent 设计的 Karpo Decision 31B 决策模型，同时开源采用 System 1 + System 2 架构的配套浏览器操作框架，该框架包含 karpo-browser 框架、网页动作决策模型 Karpo Decision 27B Act 及配套评测集 KBB。该模型在《城市扫描仪》挑战中处理任务耗时 2.6 秒，约为 Gemini 3.5 Flash（14.96 秒）的 1/6，成本仅为后者的 1/13，36 道题准确率达 100%；在 300 个模型参评的 Decision Index 评测总榜中以 73.9 分位列第一，中位响应时间 94 毫秒，单题最多可同时判断 255 个候选选项，校准误差 2.3%。本次报道未附官方一手发布链接，相关细节暂无法独立核实。

rss · 量子位 · 11月21日 09:52

**「为什么重要」** 面向 Agent 场景的决策模型在速度、成本维度实现对主流商用模型的反超，且配套浏览器操作框架同步开源，可降低浏览器 Agent 的落地门槛。

**「可关注」** 可关注：Karpo Decision 31B 单题最多可同时判断 255 个候选选项，中位响应时间 94 毫秒，适合对低延迟、多选项决策有要求的 Agent 场景。

**标签**: `#model`, `#open-source`, `#eval`, `#industry`

---

<a id="item-ai-daily-3"></a>
### [TML 开源 26B Inkling 2 Mini 循环 Transformer](https://mp.weixin.qq.com/s?__biz=MzA3MzI4MjgzMw==&amp;mid=2651075624&amp;idx=2&amp;sn=b6e7e23d631dba7a952cbe5da8e77769) ⭐️ 5.5/10

Thinking Machines Lab（TML）开源了总参数 26B 的循环 Transformer 多模态模型 Inkling 2 Mini，权重按 Apache 2.0 许可发布，支持文本与图像输入，最大上下文窗口为 100 万 token，在 AA Index 上得分 20.1，官方宣称其可在笔记本运行并胜任智能体任务，开发者可下载部署，也能通过 Tinker 进行推理和微调。该模型采用循环 Transformer 与混合专家（MoE）架构，总层数 24 层，前 6 层与后 6 层各运行 1 次，中间 12 层运行 3 次，每个 token 完成 48 次层计算，激活参数约 3.4B，计入循环重复计算后有效激活参数约 5.4B。官方演示中使用配备 48GB 内存的 M5 Pro MacBook Pro 离线运行，该模型在几分钟内生成可玩飞行模拟器，还可驱动包含 20 位村民的微型像素小镇 Thinkyville。

rss · 机器之心 · 11月21日 04:11

**「为什么重要」** 该模型通过循环 Transformer 架构重复利用中间层权重，搭配混合专家（MoE）设计将激活参数控制在较低水平，在消费级笔记本上实现了智能体任务、游戏通关、动画生成等复杂能力，验证了端侧大模型在有限硬件下处理复杂任务的可行性，为轻量级多模态模型部署提供了新思路。

**「可关注」** 可关注：循环 Transformer 通过重复利用中间 12 层权重，以 26B 总参数量、约 3.4B 激活参数实现每 token 48 次层计算，在控制端侧部署开销的同时提升了连续推导类任务的处理空间。

**「评论」** 模型发布后社区反馈热烈，有开发者将其接入 DeepSeek Harness 获得较快推理速度，还有用户测试其可玩通关电子游戏并学会速通、生成动画 MV。

**标签**: `#model`, `#open-source`, `#lab`, `#eval`

---

## AI 羊毛
{: #sec-ai-deals .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-deals" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-deals-1"></a>
### [AIask Claude Opus 5.5 限时一折](https://www.v2ex.com/t/1258730#reply18) ⭐️ 8.0/10

AIask 平台推出限时 5 天的 Claude Opus 5.5 折扣活动，该模型输入价格降至 0.4 美元/百万 tokens，输出价格降至 2 美元/百万 tokens；老用户需在对应 V2EX 帖子下回复个人 ID（ID 位于登录后平台面板左侧 LOGO 旁）领取福利，新用户可通过 aiask.me 注册参与，活动自 2026 年 11 月 21 日起生效。

rss · V2EX Hot · 11月21日 04:59

**「为什么重要」** 该活动为 Claude Opus 5.5 提供一折优惠，价格远低于常规 API 定价，活动限时 5 天，当前仍在有效期内，对需要调用该模型的开发者可降低使用成本。

**「可关注」** 可关注：该折扣仅适用于 Claude Opus 5.5 模型，需在平台“组合”分组的“默认”分组下创建 API 密钥使用，具体价格以模型广场展示为准。

**标签**: `#promo`, `#api`, `#limited-free`

---

<a id="item-ai-deals-2"></a>
### [File Organizer 黑五免费兑换码](https://www.v2ex.com/t/1258731#reply17) ⭐️ 8.0/10

开发者 sakishum 为回馈 V2EX 用户，在 App Store 上架的付费 macOS 文件整理工具 File Organizer 放出 30 个免费兑换码，黑五限时限量领取、先到先得，兑换码直接附在帖子正文中，无其他额外领取限制。

rss · V2EX Hot · 11月21日 05:03

**「为什么重要」** 当前兑换码仍为先到先得状态，黑五活动期内可免费获取这款付费工具，无需支付 App Store 售价。

**「可关注」** 可关注：该工具完全在本地运行，支持按类型/日期规则预览整理文件、新文件自动归档、可撤销批量重命名（含前缀/后缀/替换/序列号），适配 macOS 本地文件整理需求。

**标签**: `#promo`, `#limited-free`, `#coupon`, `#macos`, `#app-store`

---

<a id="item-ai-deals-3"></a>
### [Gemini 黑五 Pro 半价 转正攻略](https://www.v2ex.com/t/1258834#reply8) ⭐️ 8.0/10

V2EX 用户 Msxx 分享谷歌 Gemini 美区黑五 Pro 年付半价活动，说明学生身份订阅的核验风险、功能限制，同时分享个人 AI 工具使用经验，附订阅教程参考。当前主流 Gemini Pro 订阅方案包括美区学生身份月付 8.x 美元、日区学生身份月付约 30 元人民币、小米合作 3 个月 Pro 优惠，其中学生身份订阅存在 SheerID 核验失败风险，且激活的 Pro 为受限版无法使用 Gemini 4，小米优惠稳定性不足。

rss · V2EX Hot · 11月21日 19:31

**「为什么重要」** 当前谷歌对学生身份 Gemini Pro 的核验门槛提升，大量用户核验失败，黑五半价年付 Pro 是无需学生身份、可正常使用 Gemini 4 的稳定替代方案，年付成本低于美区学生月付价格。

**「可关注」** 可关注：无学生身份或学生核验失败的用户可考虑美区黑五半价年付 Gemini Pro，该方案无功能限制且支持 Gemini 4，年付成本低于美区学生月付价格；日常 AI 使用可按需搭配 DeepSeek Flash 做代码、Gemini 4 Neon 做文字、ChatGPT Images 2.6 Flare 档做生图。

**标签**: `#promo`, `#student`, `#limited-free`, `#limited-region`, `#api`

---