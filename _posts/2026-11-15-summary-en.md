---
layout: default
title: "Horizon Summary: 2026-11-15 (EN)"
date: 2026-11-15
lang: en
---

> From 186 items, 8 important content pieces were selected

---

**Agent Harness Architecture**
1. [browser-use 1.0.5 发布](#item-harness-arch-1) ⭐️ 5.5/10

**AI Agent Engineer**
1. [Antigravity /teamwork 多代理协作更新](#item-agent-engineer-1) ⭐️ 7.0/10
2. [datasette-llm 0.1a11 支持OpenAI兼容端点](#item-agent-engineer-2) ⭐️ 5.8/10
3. [inspect\_ai 0.3.290 发布](#item-agent-engineer-3) ⭐️ 5.5/10

**AI Daily**
1. [李飞飞苏姿丰CoRL 2026首次同台对谈](#item-ai-daily-1) ⭐️ 5.0/10

**AI Deals**
1. [AI 语音面试陪练 100 分钟免费额度](#item-ai-deals-1) ⭐️ 7.0/10
2. [x6o4 RSS Cloud 送 Kindle 7 天试用码](#item-ai-deals-2) ⭐️ 7.0/10
3. [免费词典 API 上线 无需密钥](#item-ai-deals-3) ⭐️ 7.0/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [browser-use 1.0.5 发布](https://github.com/browser-use/browser-use/releases/tag/1.0.5) ⭐️ 5.5/10

这是browser-use 1.0.5版本的正式发布，核心新增内置模型驱动的浏览器代理运行评判机制，支持配置化评判规则，站点反制边缘场景识别能力显著提升。安装命令为\`pip install &\#x27;browser-use==1.0.5&\#x27;\`，每次运行后会自动填充\`result.judgement\`字段，包含成功状态、失败原因、提示词注入检测、机器人拦截/验证码检测、问题记录等维度，旧版0.x的\`use\_judge\`/\`ground\_truth\`参数已恢复兼容。经13次真实运行各评判3次验证，站点反制场景的问题识别率从6/15提升至15/15，干净运行场景误报率为2/24，成功判定结果无变化。

github · sarath-menon · Nov 14, 08:24

**「设计要点」** 评判模块作为低侵入旁路能力接入运行链路，默认可访问运行轨迹、末帧截图与最终页面（\`use\_vision=False\`时除外），支持通过\`judge\_context\`传入自定义评判标准，也可通过\`judge=False\`关闭该能力；模块会在站点拒绝输入、报错、拦截、限流时生成问题记录，哪怕运行最终成功也会记录，例如表单要求特定格式的电话号码这类问题。

**「改了什么」** 相对上一版本，新增内置模型驱动的运行自动评判能力，恢复0.x版本\`use\_judge\`/\`ground\_truth\`参数的兼容性，站点反制边缘场景的问题识别率从6/15提升至15/15，干净运行场景误报率控制在2/24，成功判定结果无变化，相关实现对应PR \#6398、\#6403、\#6404。

**Tags**: `#eval`, `#tools`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [Antigravity /teamwork 多代理协作更新](https://research.google/blog/advancing-science-engineering-with-antigravitys-teamwork-feature/) ⭐️ 7.0/10

Google Research 2026-11-14 博客更新了 Antigravity /teamwork 多代理功能在科学计算与工程任务中的用例。该功能目前处于持续迭代阶段，团队确认正在推送给外部用户，后续将公布动态构建代理团队的实现细节。公开材料未包含深层技术实现说明或性能基准数据。

hackernews · acossta · Nov 14, 13:20 · [Discussion](https://news.ycombinator.com/item?id=50496811)

**「为什么重要」** 这是 Google 首次系统展示 /teamwork 在复杂技术任务中的实际应用场景，而非仅发布概念公告。对正在设计 agent orchestration 与 harness 的工程师而言，这提供了评估多代理协作落地路径的新参考，但具体技术差异仍需更多披露才能判断。

**「可关注」** 可关注：/teamwork 与 Claude dynamic workflows、Codex 等工具的 orchestration 模型差异尚未有公开技术对比，社区对其“自动模式”缺失的批评值得在选型时纳入评估。

**「评论」** 社区讨论引用 Adaptive Auto-Harness 与 team-solve 等证据，支持多代理团队工作流能提升自主性并控制质量衰减。Antigravity 团队成员确认 /teamwork 正在持续改进并将推送给外部用户，但部分用户认为其功能落后于 Claude dynamic workflows 且缺乏自动模式。

**Tags**: `#harness`, `#coding-agent`, `#orchestration`

---

<a id="item-agent-engineer-2"></a>
### [datasette-llm 0.1a11 支持OpenAI兼容端点](https://github.com/datasette/datasette-llm/releases/tag/0.1a11) ⭐️ 5.8/10

2026年11月14日，simonw发布datasette-llm 0.1a11，新增OpenAI兼容端点直接配置能力，支持Chat Completions与Responses API，相比此前版本无需额外LLM插件即可接入本地或第三方模型。配置项支持在YAML中通过endpoints字段注册模型，可指定api\_base、model\_name、key等参数，端点模型默认支持工具调用与流式输出。该版本调整了模型查找、密钥校验、黑白名单的生效逻辑，要求依赖LLM 0.37.1及以上版本，目前仍处于早期alpha阶段，主要面向Datasette数据探索生态用户。

github · simonw · Nov 14, 23:59

**「为什么重要」** 该更新降低了Datasette对接OpenAI兼容模型的门槛，减少了插件依赖成本；但目前该插件仍处早期alpha阶段，且主要面向Datasette数据探索场景，对主流agent工程框架的影响尚未明确。

**「可关注」** 可关注：配置OpenAI兼容端点时需将凭证写入key字段，避免额外headers在Datasette的/-/config.json中泄露。

**Tags**: `#harness`

---

<a id="item-agent-engineer-3"></a>
### [inspect\_ai 0.3.290 发布](https://github.com/UKGovernmentBEIS/inspect_ai/releases/tag/0.3.290) ⭐️ 5.5/10

inspect\_ai 0.3.290 于 2026-11-13 发布。本次更新增强 agent 可观测性，包括 in-flight 模型调用事件 ID、跨 agent bridge 的持久消息 ID 及工具事件来源记录；评估准确性方面，excluded epoch 不再参与 epoch reduction，score reason 新增 excluded 和 zeroed 标记。新增 Gemini 4 Carbon、Gemini 4 Hydrogen、Mistral Large 4、Meta Muse 系列及 Moonshot Kimi K3 支持，并修复 bridged agent 限流后无响应、sandbox 身份作用域隔离、ACP 请求卡住、异步 fsspec 读取阻塞事件循环等缺陷。

github · github-actions\[bot\] · Nov 14, 21:14

**「为什么重要」** 可观测性增强直接改善 agent 轨迹调试效率；模型支持扩展与多项关键缺陷修复（限流、权限、事件循环）降低了生产 harness 的运行风险。

**「可关注」** 可关注：excluded epoch 已从 epoch reduction 中移除，且 score reason 新增 excluded 和 zeroed 状态，评估脚本若依赖旧聚合逻辑需核对结果。

**Tags**: `#harness`, `#eval`, `#observability`, `#orchestration`

---

## AI Daily

<a id="item-ai-daily-1"></a>
### [李飞飞苏姿丰CoRL 2026首次同台对谈](https://mp.weixin.qq.com/s?__biz=MzA3MzI4MjgzMw==&amp;mid=2651074456&amp;idx=2&amp;sn=96fd9bd0e55a35b655b0a2dddd61264d) ⭐️ 5.0/10

2026年11月12日，机器人学习顶会CoRL 2026进入第三天，AMD此前宣布以约82亿美元全股票交易收购的李飞飞创办的World Labs尚未完成交割，李飞飞与AMD董事长兼CEO苏姿丰在该会议首次同台开展约半小时对谈，话题覆盖物理AI市场机会、端到端基础模型边界、学界算力短缺、AI时代读博选择等；苏姿丰称物理AI尤其是机器人是未来几年数千亿美元量级的机会，李飞飞称AI与计算已根本融合、多模态模型正走向融合，对谈未披露具体未公开的新交易或技术细节。

rss · 机器之心 · Nov 14, 03:34

**「为什么重要」** 这是该笔收购宣布后双方核心人物的首次公开同台，释放了AMD加码物理AI、World Labs融入其技术体系的信号，对关注机器人AI领域的从业者有参考价值。

**「可关注」** 可关注：AMD将硬件、软件、系统协同优化的思路延伸至机器人领域，World Labs与AMD的结合被双方视为团队科学在AI时代的实践。

**Tags**: `#industry`, `#event`, `#lab`

---

## AI Deals

<a id="item-ai-deals-1"></a>
### [AI 语音面试陪练 100 分钟免费额度](https://www.v2ex.com/t/1257121#reply10) ⭐️ 7.0/10

独立开发者 cryptitalk 推出 AI 语音面试陪练工具 aidou.studio，提供最高 100 分钟免费通话额度。无登录状态下可直接体验 10 分钟，使用 Google 账号登录并完成与小豆的 5 分钟真人验证后，可额外获得 90 分钟时长。材料未提及额度有效期及截止时间。

rss · V2EX Hot · Nov 14, 15:19

**「为什么重要」** 该工具采用全双工实时对话模式，支持用户随时打断回复，提供技术面试官 Alex、英语口语私教 Emma 两类角色，区别于传统分段回复的AI面试工具，适合有面试练手需求的用户先试用。

**「可关注」** 可关注：无登录可直接体验10分钟，完成Google账号真人验证（与小豆聊5分钟）后可额外获得90分钟通话时长，总时长最高100分钟。

**Tags**: `#free-tier`, `#promo`, `#limited-free`

---

<a id="item-ai-deals-2"></a>
### [x6o4 RSS Cloud 送 Kindle 7 天试用码](https://www.v2ex.com/t/1257010#reply6) ⭐️ 7.0/10

V2EX个人开发者VeeSong发放x6o4 RSS Cloud共100个7天免费试用码，该工具支持将RSS内容推送至Kindle阅读，也可对接AI agent实现语音一键推送，需微信扫码领取；另放出20个x6o4 Reader去广告会员兑换码，可直接使用。

rss · V2EX Hot · Nov 14, 03:18

**「为什么重要」** 该工具专门针对Kindle电纸书优化RSS阅读体验，解决miniflux、FreshRSS等自部署方案不适配Kindle的问题，支持AI agent一键推送未读文章，适合有Kindle阅读RSS需求的用户；当前100个试用码为限时福利，未抢到名额的用户后续可等待官方释放名额或直接付费。

**「可关注」** 可关注：x6o4 RSS Cloud配套skill已开源至GitHub，可fork后对接自建RSS服务器，也支持调整适配其他电纸书设备；100个7天试用码需微信扫码领取，若未抢到可等待后续释放名额或直接付费。

**Tags**: `#limited-free`, `#promo`

---

<a id="item-ai-deals-3"></a>
### [免费词典 API 上线 无需密钥](https://api.suvankar.cc/docs/dictionary) ⭐️ 7.0/10

suvankar\_m 在 Hacker News 分享了一款基于 Wiktionary 数据的免费词典 API，访问地址为 https://api.suvankar.cc/docs/dictionary。该 API 无需 API 密钥即可调用，目前未公开调用额度、速率限制及服务有效期。

rss · HN Free API / Credits · Nov 14, 06:30

**「为什么重要」** 对于需要轻量词典能力的开发场景，该 API 省去了密钥申请流程，可快速接入验证原型。

**「可关注」** 可关注：该 API 未公开速率限制、配额及服务有效期，生产环境接入前需自行验证稳定性。

**Tags**: `#free-tier`, `#api`

---