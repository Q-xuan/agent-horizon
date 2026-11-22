---
layout: default
title: "Horizon Summary: 2026-11-22 (EN)"
date: 2026-11-22
lang: en
---

> From 161 items, 7 important content pieces were selected

---

**Agent Harness Architecture**
1. [Cline CLI v3.0.75 发布](#item-harness-arch-1) ⭐️ 5.5/10

**AI Daily**
1. [腾讯元宝×KCL 发群聊Agent记忆基准](#item-ai-daily-1) ⭐️ 5.5/10
2. [Karpo Decision 31B 开源 浏览器Agent框架释出](#item-ai-daily-2) ⭐️ 5.5/10
3. [TML 开源 Inkling 2 Mini](#item-ai-daily-3) ⭐️ 5.5/10

**AI Deals**
1. [Google AI Pro 黑五 年付五折](#item-ai-deals-1) ⭐️ 8.0/10
2. [AIask Claude Opus 5.5 限时5天1折](#item-ai-deals-2) ⭐️ 8.0/10
3. [File Organizer 30枚兑换码限免](#item-ai-deals-3) ⭐️ 8.0/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [Cline CLI v3.0.75 发布](https://github.com/cline/cline/releases/tag/cli-v3.0.75) ⭐️ 5.5/10

Cline CLI v3.0.75 将一次性运行（one-shot）默认模式从 act 改为 yolo，并修复 \`--timeout\` 与 Ctrl+C 无法中断首轮执行的问题。\`read\_files\` 结果不再截断至 8k 字符，上限改为 2000 行或约 48k 字符。CLI 停止读取启动目录下的 \`.env\` 与 \`bunfig.toml\`，无保存模型时默认选择第一个免费模型而非 Claude Sonnet 5.5。yolo 模式不含 team 工具，需要时需传 \`--act\`。

github · github-actions\[bot\] · Nov 21, 05:30

**「设计要点」** 运行时控制层将 one-shot 默认确认策略从 act 改为 yolo，工具层结果传输上限从固定 8k 字符改为按行数/字符数双重限制，配置加载范围从启动目录收缩。提供商适配层修正了推理参数与模型目录匹配逻辑，并移除 \`CLINE\_CAPTURE\_\*\` 调试变量以避免请求体写入磁盘。

**「改了什么」** One-shot 运行默认进入 yolo 模式；\`--timeout\` 与 Ctrl+C 可中断首轮执行。\`read\_files\` 结果上限从 8k 字符提升至约 48k 字符或 2000 行。CLI 不再读取启动目录的 \`.env\` 与 \`bunfig.toml\`，无保存模型时默认选择第一个免费模型。

**Tags**: `#runtime`, `#tools`, `#permissions`

---

## AI Daily

<a id="item-ai-daily-1"></a>
### [腾讯元宝×KCL 发群聊Agent记忆基准](https://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw==&amp;mid=2247947677&amp;idx=3&amp;sn=0797fbd2116a405b44176c97577757d8) ⭐️ 5.5/10

腾讯元宝联合伦敦国王学院NLP团队发布首个基于群聊构建的Agent记忆基准GroupAssistBench。该基准基于50个真实群聊的80299条历史消息构建2395道评测题，用于检验Agent记忆能否从“记得住”走向“用得好”。研究团队对比了完整上下文、检索增强、外部记忆等14组配置，其中EverMemOS在L1记忆召回得分0.621高于完整上下文的0.570，但在L2开放式服务得分0.247低于完整上下文的0.431。本次信息来自二手科技媒体量子位的报道，无官方一手发布链接。

rss · 量子位 · Nov 21, 09:52

**「为什么重要」** 当前Agent记忆评测多聚焦单场景信息召回，该基准首次覆盖多人群聊的复杂记忆使用场景，为评估Agent在真实群聊中的记忆应用能力提供了可复用的测试集。

**「可关注」** 可关注：GroupAssistBench设置L1记忆召回、L2开放式服务双评测维度，可用来区分Agent记忆“记得住”和“用得好”的能力差异。

**Tags**: `#agent`, `#lab`, `#industry`, `#eval`

---

<a id="item-ai-daily-2"></a>
### [Karpo Decision 31B 开源 浏览器Agent框架释出](https://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw==&amp;mid=2247947677&amp;idx=1&amp;sn=ebf1f96b9afceacdfa0d407ecdb3ff2b) ⭐️ 5.5/10

MachinePulse AI 开源 Karpo Decision 31B 决策模型及配套浏览器 Agent 框架。该模型在《城市扫描仪》挑战中完成筛选任务耗时 2.6 秒，为 Gemini 3.5 Flash 的 1/6，成本仅为后者的 1/13，36 道题准确率 100%；在 300 个模型参与的 Decision Index 评测总榜中以 73.9 分登顶，单题最多可同时判断 255 个候选选项，校准误差 2.3%，中位响应时间 94 毫秒，单张 RTX PRO 6000 即可运行。开源方案包含 karpo-browser 框架、Karpo Decision 27B Act 模型及配套评测集 KBB，采用 System 1 + System 2 架构，面向网页动作决策场景优化。

rss · 量子位 · Nov 21, 09:52

**「为什么重要」** 该成果针对 Agent 场景的高频决策效率痛点，在速度、成本、准确率上均展现显著优势，配套开源的浏览器操作框架可直接服务于开发者构建低延迟浏览器 Agent。

**「可关注」** 可关注：Karpo Decision 31B 单卡 RTX PRO 6000 即可运行，中位响应时间 94 毫秒，适合对决策时延要求高的 Agent 场景集成。

**Tags**: `#model`, `#open-source`, `#industry`, `#eval`, `#agent`

---

<a id="item-ai-daily-3"></a>
### [TML 开源 Inkling 2 Mini](https://mp.weixin.qq.com/s?__biz=MzA3MzI4MjgzMw==&amp;mid=2651075624&amp;idx=2&amp;sn=b6e7e23d631dba7a952cbe5da8e77769) ⭐️ 5.5/10

Thinking Machines Lab（TML）开源了26B参数的循环Transformer模型Inkling 2 Mini，权重按Apache 2.0许可发布，支持文本和图像输入，最大上下文窗口100万token。该模型激活参数约3.4B，计入循环重复计算后有效参数激活量约5.4B，官方宣称可在笔记本运行，AA Index得分20.1，可胜任智能体任务；官方演示使用配备48GB内存的M5 Pro MacBook Pro离线完成推理。

rss · 机器之心 · Nov 21, 04:11

**「为什么重要」** 该模型验证了小参数循环架构在端侧部署的可行性，为智能体任务的轻量化落地提供了新参考，发布后社区已出现多类落地尝试。

**「可关注」** 可关注循环Transformer通过重复利用中间12层，以24层权重实现48次层计算，在控制权重体积的同时提升连续任务处理能力。

**「评论」** 社区已尝试将其接入DeepSeek Harness获得较快推理速度，还有用户用它通关电子游戏、生成动画MV，甚至实现游戏速通。

**Tags**: `#open-source`, `#model`, `#lab`, `#eval`

---

## AI Deals

<a id="item-ai-deals-1"></a>
### [Google AI Pro 黑五 年付五折](https://www.appinn.com/google-ai-pro-black-friday-2026/) ⭐️ 8.0/10

你看到的内容可能由第三方 AI 基于小众软件文章提炼总结而成，可能与原文真实意图存在偏差。不代表小众软件观点和立场。请&lt;a href=&quot;https://www.appinn.com/google-ai-pro-black-friday-2026/&quot; target=&quot;\_blank&quot;&gt;点击链接阅读原文&lt;/a&gt;细致比对和校验。&lt;br /&gt;&lt;br /&gt;Google 推出 AI Pro/Plus 黑五限时年付五折优惠，美区原价 199.99 美元/年，折后约 99.99 美元/年，折合每月 8.33 美元，活动覆盖 Google AI Plus 和 Google AI Pro 年付套餐，最高优惠 50%。11 月 20 至 26 日现有 Google One、Google AI 订阅用户可提前参与，11 月 27 日起向新用户开放，不同账户显示的折扣可能不同，最终以 Google 结算页面为准，目前该活动主要面向符合条件的美区账户开放。

rss · 小众软件 · Nov 21, 11:14

**「为什么重要」** 该优惠允许已有 Google One 订阅的老用户提前参与，且 AI Pro 套餐包含 5TB Google One 云存储、Gemini 高级模型及 NotebookLM 增强功能，相比不稳定的学生版 Pro、日区学生订阅等替代方案无使用限制，适合经常使用 Gemini、NotebookLM 或已在付费购买 Google One 存储空间的用户。

**「可关注」** 可关注：已订阅 Google One 的用户建议直接走升级路径，不要先取消原有订阅，旧套餐剩余费用按比例退款或折算使用时长的规则以 Google 结算页为准；本次黑五折扣仅首个年付周期有效，后续续费大概率恢复 199.99 美元/年的原价。

**「评论」** 有长期使用谷歌学生 Pro 的用户分享转投该优惠的决策，原因是学生身份验证不稳定、学生版 Pro 无法使用 Gemini 4，同时对比了日区学生订阅身份不稳定、小米合作优惠频繁掉车等方案的不足，还分享了该用户搭配 DeepSeek Flash、Gemini 4 Neon、ChatGPT Images 2.6 的工具链使用经验。

**Tags**: `#promo`, `#coupon`, `#limited-offer`, `#subscription`

---

<a id="item-ai-deals-2"></a>
### [AIask Claude Opus 5.5 限时5天1折](https://www.v2ex.com/t/1258730#reply18) ⭐️ 8.0/10

AIask平台推出限时促销活动，Claude Opus 5.5模型限时5天打1折，输入价格为$0.4/M tokens，输出价格为$2/M tokens。老用户需在V2EX本帖下回复个人面板的用户ID即可领取对应福利，活动自2026年11月21日起生效，为期5天。

rss · V2EX Hot · Nov 21, 04:59

**「为什么重要」** Claude Opus 5.5的公开API调用成本普遍较高，该活动提供的1折输入输出价格对比常规定价有显著优势，限时窗口适合有相关模型调用需求的开发者参与。

**「可关注」** 可关注：老用户需在V2EX本帖下回复个人面板ID领取福利，Claude Opus 5.5需创建API密钥后加入“组合”分组的“默认”分组使用，具体价格以模型广场公示为准。

**Tags**: `#promo`, `#api`, `#credits`, `#limited-free`

---

<a id="item-ai-deals-3"></a>
### [File Organizer 30枚兑换码限免](https://www.v2ex.com/t/1258731#reply17) ⭐️ 8.0/10

V2EX developer sakishum is offering 30 limited free redemption codes for their self-made macOS file organization tool File Organizer on the App Store. V2EX users can redeem the codes on a first-come, first-served basis to get the app for free. The tool supports organizing files by type or date rules with preview before execution, automatic archiving of new files in selected folders when the app is running, batch renaming \(including prefix, suffix, replacement, and serial number modes\) with undo function, and all processing is done locally on the device.

rss · V2EX Hot · Nov 21, 05:03

**「为什么重要」** This is a Black Friday giveaway from the developer, and the tool processes all files locally without uploading data, which meets the needs of macOS users for file organization and batch renaming. The redemption codes are limited and available on a first-come, first-served basis, so it is still worth claiming today.

**「可关注」** The tool is only compatible with macOS, all file processing is performed locally, and the redemption codes have no extra usage restrictions, available on a first-come, first-served basis.

**Tags**: `#promo`, `#limited-free`, `#coupon`

---