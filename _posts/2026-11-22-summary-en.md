---
layout: default
title: "Horizon Summary: 2026-11-22 (EN)"
date: 2026-11-22
lang: en
---

> From 164 items, 8 important content pieces were selected

---

**Agent Harness Architecture**
1. [Cline CLI cli-v3.0.75 发布](#item-harness-arch-1) ⭐️ 5.5/10
2. [FastMCP v4.2.4 发布](#item-harness-arch-2) ⭐️ 5.5/10

**AI Daily**
1. [腾讯元宝×KCL 发群聊Agent记忆基准](#item-ai-daily-1) ⭐️ 5.5/10
2. [Karpo Decision 31B 开源 浏览器Agent框架释出](#item-ai-daily-2) ⭐️ 5.5/10
3. [TML 开源 Inkling 2 Mini 循环 Transformer 模型](#item-ai-daily-3) ⭐️ 5.5/10

**AI Deals**
1. [AIask Claude Opus 5.5 限时5折](#item-ai-deals-1) ⭐️ 8.0/10
2. [File Organizer 30枚兑换码发放](#item-ai-deals-2) ⭐️ 8.0/10
3. [Gemini 美区黑五 Pro 半价](#item-ai-deals-3) ⭐️ 8.0/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [Cline CLI cli-v3.0.75 发布](https://github.com/cline/cline/releases/tag/cli-v3.0.75) ⭐️ 5.5/10

Cline CLI cli-v3.0.75 调整 one-shot 运行默认行为、工具调用安全边界与文件读取上限。单次运行（stdin/prompt）默认切到 yolo mode，不再读取本地 .env 与 bunfig.toml，read\_files 输出上限从 8k 提升至约 48k 字符或 2000 行。首轮支持 timeout 与 Ctrl+C 中断，默认模型选择逻辑改为首个可用模型，Reflection Beam 在压缩或切换模型后的 400 错误已修复。同时移除 CLINE\_CAPTURE\_\* 调试变量，升级 undici 至 7.30.1 修复进程崩溃问题。

github · github-actions\[bot\] · Nov 21, 05:30

**「设计要点」** 运行时层：one-shot 模式默认切到 yolo，首轮支持异步中断；工具层：read\_files 取消 8k 截断，本地配置加载移除；权限层：.env/bunfig.toml 不再自动读取，降低密钥泄露风险。模型层：默认模型选择逻辑改为首个可用模型，reasoning 参数适配各 provider 能力，LiteLLM 预算字段修正。

**「改了什么」** one-shot 运行默认启用 yolo mode，首轮支持 timeout/Ctrl+C 中断；本地 .env 与 bunfig.toml 停止加载；read\_files 输出上限从 8k 提升至约 48k/2000 行。默认模型选择改为首个可用模型，Reflection Beam 在 compaction/model switch 后的 400 错误修复，移除 CLINE\_CAPTURE\_\* 调试变量。

**Tags**: `#runtime`, `#tools`, `#permissions`, `#configuration`

---

<a id="item-harness-arch-2"></a>
### [FastMCP v4.2.4 发布](https://github.com/PrefectHQ/fastmcp/releases/tag/v4.2.4) ⭐️ 5.5/10

FastMCP v4.2.4 修复 OAuth 代理授权码并发兑换竞态条件（GHSA-78c8-3jhx-5mg7），阻止同一授权码或刷新令牌被重复兑换。已撤销的代理访问令牌在刷新后保持撤销状态，防止复用。工具转换失败现在仅隐藏自身工具，不再破坏全部工具列表查询。挂载与版本化组件行为修正，包括共享版本去重、父级隐藏时子组件响应、合并默认值保留调用者对象。

github · zzstoatzz · Nov 21, 05:24

**「改了什么」** 修复 OAuth 代理授权码与刷新令牌的并发竞态（GHSA-78c8-3jhx-5mg7），防止重复兑换，并确保已撤销令牌刷新后保持撤销状态。工具转换失败仅隐藏自身工具，避免破坏工具列表；同时修正挂载组件版本重复列出、父级隐藏时子组件不可见、合并默认值破坏调用者对象等问题。

**Tags**: `#mcp`, `#tools`, `#permissions`

---

## AI Daily

<a id="item-ai-daily-1"></a>
### [腾讯元宝×KCL 发群聊Agent记忆基准](https://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw==&amp;mid=2247947677&amp;idx=3&amp;sn=0797fbd2116a405b44176c97577757d8) ⭐️ 5.5/10

腾讯元宝联合伦敦国王学院NLP团队发布首个群聊场景Agent记忆基准GroupAssistBench。该基准基于50个真实群聊的80299条历史消息构建2395道评测题，覆盖L1记忆召回、L2开放式服务两个层级，对比完整上下文、检索增强、外部记忆等14组配置。评测显示EverMemOS在L1召回得分0.621高于完整上下文的0.570，但L2服务得分0.247低于完整上下文的0.431，暴露出现有方案「记得住但用不好」的问题。

rss · 量子位 · Nov 21, 09:52

**「为什么重要」** 当前Agent记忆评测多聚焦召回准确率，缺乏面向群聊复杂场景的服务能力评估，该基准填补了群聊场景Agent记忆量化评测的空白，为相关产品迭代提供可参考的评估框架。

**「可关注」** 可关注：群聊场景Agent记忆评估需同时覆盖召回准确率与实际服务能力，避免仅以召回指标作为唯一优化目标。

**Tags**: `#eval`, `#lab`, `#product`, `#industry`

---

<a id="item-ai-daily-2"></a>
### [Karpo Decision 31B 开源 浏览器Agent框架释出](https://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw==&amp;mid=2247947677&amp;idx=1&amp;sn=ebf1f96b9afceacdfa0d407ecdb3ff2b) ⭐️ 5.5/10

MachinePulse AI 开源专为 Agent 设计的 Karpo Decision 31B 决策模型，量子位报道其在《城市扫描仪》挑战中耗时 2.6 秒，约为 Gemini 3.5 Flash（14.96 秒）的 6 倍，成本仅为后者的 1/13，36 道题准确率 100%；在 300 个模型参与的 Decision Index 评测总榜以 73.9 分登顶，单题最多可同时判断 255 个候选选项，校准误差 2.3%，单卡 RTX PRO 6000 中位响应时间 94 毫秒。同期 MachinePulse AI 还开源配套浏览器操作框架 karpo-browser，包含 System 1 + System 2 架构、Karpo Decision 27B Act 模型及配套评测集 KBB。以上数据均来自量子位二手报道，未附官方一手发布链接，无更多可核实的官方细节。

rss · 量子位 · Nov 21, 09:52

**「为什么重要」** 该方案同时覆盖 Agent 决策模型与浏览器操作全链路组件，且明确针对低延迟、低成本场景优化，为浏览器 Agent 的落地提供了可直接复用的开源技术路径。

**「可关注」** 可关注：Karpo Decision 31B 单卡 RTX PRO 6000 即可部署，中位响应时间 94 毫秒，适配对延迟敏感的 Agent 决策场景。

**Tags**: `#model`, `#open-source`, `#eval`, `#industry`

---

<a id="item-ai-daily-3"></a>
### [TML 开源 Inkling 2 Mini 循环 Transformer 模型](https://mp.weixin.qq.com/s?__biz=MzA3MzI4MjgzMw==&amp;mid=2651075624&amp;idx=2&amp;sn=b6e7e23d631dba7a952cbe5da8e77769) ⭐️ 5.5/10

Thinking Machines Lab（TML）开源26B参数循环Transformer多模态模型Inkling 2 Mini，采用looped transformer架构，总参数26B，激活参数约3.4B，计入循环重复计算后有效激活参数约5.4B，支持文本与图像输入，最大上下文窗口100万token，权重按Apache 2.0许可发布。官方宣称该模型可在笔记本运行，AA Index得分20.1，演示了在配备48GB内存的M5 Pro MacBook Pro离线环境下数分钟生成可玩飞行模拟器、驱动20位村民的像素小镇等场景。社区已出现接入DeepSeek Harness测试、通关电子游戏并实现速通、生成动画MV等用例。

rss · 机器之心 · Nov 21, 04:11

**「为什么重要」** 该模型以较低的有效激活参数实现了笔记本可运行的多模态智能体能力，展示了端侧大模型在复杂任务上的可行路径，为轻量级大模型架构设计提供了参考。

**「可关注」** 可关注：循环Transformer架构通过重复利用中间12层网络层，在仅存储24层权重的条件下为每个token提供48次层计算，兼顾了模型体积与连续推理任务的处理空间。

**「评论」** 社区反馈热烈，已有用户将其接入DeepSeek Harness获得较快运行速度，还有用户测试其通关电子游戏并学会速通、生成动画MV等能力。

**Tags**: `#model`, `#open-source`, `#lab`, `#eval`

---

## AI Deals

<a id="item-ai-deals-1"></a>
### [AIask Claude Opus 5.5 限时5折](https://www.v2ex.com/t/1258730#reply18) ⭐️ 8.0/10

AIask 于 2026-11-21 推出两项福利：一是周末老用户回复 V2EX 对应帖子内的个人 AIask 用户 ID 可领取鸡蛋，二是 Claude Opus 5.5 限时 5 天打一折，输入价格为 $0.4/M tokens，输出价格为 $2/M tokens。用户 ID 可在登录后平台面板左侧 LOGO 旁查看，新用户可通过 aiask.me 注册账号。

rss · V2EX Hot · Nov 21, 04:59

**「为什么重要」** 本次 Claude Opus 5.5 限时 5 天一折，过期无法享受该折扣，有模型调用需求的开发者可及时参与。

**「可关注」** 可关注：仅 AIask 老用户可回复 ID 领取鸡蛋福利并享受 Claude Opus 5.5 一折价，新用户需先注册平台账号；使用 Claude Opus 5.5 需创建 API 密钥并加入“组合”分组的“默认”分组，具体价格可在平台模型广场核对。

**Tags**: `#promo`, `#api`, `#limited-free`

---

<a id="item-ai-deals-2"></a>
### [File Organizer 30枚兑换码发放](https://www.v2ex.com/t/1258731#reply17) ⭐️ 8.0/10

开发者sakishum为回馈V2EX用户，放出30枚macOS文件整理工具File Organizer的App Store免费兑换码，黑五限时限量发放，先到先得，用户可直接在App Store兑换使用，无额外领取门槛。

rss · V2EX Hot · Nov 21, 05:03

**「为什么重要」** 该工具支持本地文件按规则归档、批量重命名，黑五限时免费兑换可满足有macOS文件整理需求的用户使用，数量有限先到先得。

**「可关注」** 可关注：兑换码无额外使用限制，仅适配macOS平台App Store版本，领完即止。

**Tags**: `#promo`, `#limited-free`, `#coupon`, `#macos`, `#app-store`

---

<a id="item-ai-deals-3"></a>
### [Gemini 美区黑五 Pro 半价](https://www.v2ex.com/t/1258834#reply8) ⭐️ 8.0/10

V2EX 用户 Msxx 分享谷歌 Gemini 美区黑五 Pro 年付半价活动，同时梳理当前主流订阅方案的差异与限制。学生身份订阅的美区 Pro 月费约 8.x 美元、日区约 30 元人民币，但学生版为受限版本，无法使用 Gemini 4，且近期 Google One 学生身份核验失败率较高。用户附带了个人订阅教程参考链接，并分享了自己搭配 DeepSeek Flash、Gemini 4 Neon 等工具的 AI 使用方案。

rss · V2EX Hot · Nov 21, 19:31

**「为什么重要」** 当前 Google One 学生身份核验收紧，大量用户验证失败，黑五半价年付是无需学生身份即可获得完整 Pro 权益的可行替代方案，且活动具有时效性。

**「可关注」** 可关注：美区黑五半价年付活动无学生身份限制，可完整使用 Gemini 4 等新模型，但需注意活动时效与美区账号支付要求。

**Tags**: `#promo`, `#student`, `#limited-free`, `#limited-region`, `#api`

---