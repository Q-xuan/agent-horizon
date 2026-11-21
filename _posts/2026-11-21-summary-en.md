---
layout: default
title: "Horizon Summary: 2026-11-21 (EN)"
date: 2026-11-21
lang: en
---

> From 181 items, 14 important content pieces were selected

---

**Agent Harness Architecture**
1. [CF Agents 0.34.0 发布](#item-harness-arch-1) ⭐️ 8.8/10
2. [openai-agents-python v1.0.0a1 发布](#item-harness-arch-2) ⭐️ 7.8/10
3. [browser-use 1.0.8rc1 发布](#item-harness-arch-3) ⭐️ 5.5/10

**AI Agent Engineer**
1. [arXiv：语言模型可自重写权重](#item-agent-engineer-1) ⭐️ 7.0/10
2. [Inkling 2 Mini 开源发布](#item-agent-engineer-2) ⭐️ 7.0/10
3. [TuringSpace 交互式 CAPTCHA 基准发布](#item-agent-engineer-3) ⭐️ 7.0/10
4. [CodeScene：代码质量影响 Agent 审查成本](#item-agent-engineer-4) ⭐️ 7.0/10
5. [AltRA-Test 统计测试发布](#item-agent-engineer-5) ⭐️ 6.0/10
6. [ZeroVLN 免微调VLM导航框架发布](#item-agent-engineer-6) ⭐️ 5.5/10

**AI Daily**
1. [OpenAI 公布对抗性蒸馏分层防御方案](#item-ai-daily-1) ⭐️ 6.8/10
2. [Sage S2.1 Flash技术报告开源](#item-ai-daily-2) ⭐️ 5.5/10

**AI Deals**
1. [Epic 11.20~11.26 限免游戏汇总](#item-ai-deals-1) ⭐️ 8.0/10
2. [波波小红书获客助手 送30天激活码](#item-ai-deals-2) ⭐️ 8.0/10
3. [Ferry 免费 iOS 远程桌面发布](#item-ai-deals-3) ⭐️ 7.0/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [CF Agents 0.34.0 发布](https://github.com/cloudflare/agents/releases/tag/agents%400.34.0) ⭐️ 8.8/10

Cloudflare 发布 agents@0.34.0，核心升级是 Pi 1.6 运行时支持，带来非阻塞工具等待与子 agent 协调能力。Pi 工具可挂起等待信号或截止时间，agent 期间休眠，通过 \`harness.signal\(\)\` 交付信号；\`submit\(\)\` 和 \`continue\(\)\` 的 \`notify\` 参数支持跨 session 唤醒。MCP 客户端新增 \`MCPAuthorizationRequiredError\` 处理重新授权，失败请求不再泄露错误详情，改为通用 500 或 WebSocket 1011 关闭，并提供 \`onFetchError\(\)\` 自定义响应。注意：Pi 1.6 上线后无法回滚至 Pi 1.5。

github · github-actions\[bot\] · Nov 20, 15:56

**「设计要点」** Pi 1.6 运行时引入 park/unpark 状态管理，实现工具非阻塞等待与 agent 休眠，降低资源占用。MCP 客户端错误处理层增加授权状态机，失败服务器保持 failed 状态直到显式 \`reconnectMcpServer\(id\)\`，避免无效重试。

**「改了什么」** Pi 1.6 替换 Pi 1.5，支持工具 park/unpark、\`notify\` 跨 session 协调、\`onAbort: &quot;keep&quot;\` 保留队列输入，以及 Anthropic 线程过期自动重建。MCP 客户端增加 \`MCPAuthorizationRequiredError\` 与 \`reconnectMcpServer\(id\)\`，失败请求默认隐藏错误详情；PiHarness 延迟创建 root session 并支持 \`init\` 历史初始化。

**Tags**: `#runtime`, `#tools`, `#mcp`, `#subagents`

---

<a id="item-harness-arch-2"></a>
### [openai-agents-python v1.0.0a1 发布](https://github.com/openai/openai-agents-python/releases/tag/v1.0.0-alpha.1) ⭐️ 7.8/10

openai-agents-python发布v1.0.0-alpha.1预览版，将Codex作为可选嵌入式模型提供商。通过PyO3直接嵌入未修改的Codex Core rust-v0.166.0，消除JSON-RPC app-server层开销。支持CPython 3.10-3.14，提供Linux x86-64、Linux ARM64、macOS ARM64和Windows x64四个平台的wheel包。开发者可通过CodexProvider和RunConfig在Runner中切换模型提供商，支持工具调用、审批流程和流式输出。

github · markstuart-oai · Nov 20, 20:51

**「设计要点」** 运行时通过PyO3将Rust版Codex Core直接嵌入Python进程，避免app-server启动和JSON-RPC序列化开销。Provider复用ThreadManager但每次调用获取新线程，SDK session管理对话历史。

**「改了什么」** 相对v0.24.0-alpha.8，Execution模型从Agent.run\(\)和Session.submit\(\)迁移到Runner.run\(\)/run\_streamed\(\)，CodexProvider成为一等模型提供商。自动session compaction现在使用本地对话历史，sandbox manifest修复内联二进制文件保留。

**Tags**: `#runtime`, `#tools`

---

<a id="item-harness-arch-3"></a>
### [browser-use 1.0.8rc1 发布](https://github.com/browser-use/browser-use/releases/tag/1.0.8rc1) ⭐️ 5.5/10

browser-use 1.0.8rc1 是浏览器自动化 agent 系统的发布候选版本，包含 6 项具体实现改进。运行时优化方面，judge 复用缓存中的 run 避免重复计费，thinking 模型在步数限制时不再强制最终调用，gateway 将输出 token 预留从 32,768 降至 16,384 防止小额余额中途失败。工具层修复了 \`bu.type\` 密码字段脱红、\`Browser\(cdp\_url=...\)\` 正确附加已打开页面而非新建空白标签页。安全方面新增无 API key 时通过 SSH 或无头机器的链接+代码审批流程。

github · gregpr07 · Nov 20, 22:48

**「设计要点」** 本次发布调整了运行时计费缓存、模型步数限制回退、信用额度预留阈值、CDP 页面附加逻辑以及 SSH/无头机器审批流程。未提及核心 agent 记忆或评测 harness 的变更。

**「改了什么」** 相对上一版本，本次发布候选新增 judge 缓存复用避免重复计费、thinking 模型步数限制非强制回退、gateway 输出 token 预留减半、\`bu.type\` 密码字段脱红、CDP URL 附加已有页面、SSH/无头机器链接审批六项具体修复。

**Tags**: `#runtime`, `#tools`, `#permissions`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [arXiv：语言模型可自重写权重](https://arxiv.org/abs/2611.21885) ⭐️ 7.0/10

2026年11月20日，arXiv发布编号2611.21885的论文，提出语言模型可通过自主推理重写自身权重实现性能提升，宣称该过程无需梯度、无需训练。社区反馈的关键细节显示，模型实际做出的修改仅为缩短推理轨迹以规避token限制，该结论与近期weight-space programming研究、Google sleep框架的发现相似。该研究直接影响关注AI Agent自改进能力、模型安全对齐的工程师群体，但实际改进幅度与技术细节需结合原文验证。

hackernews · lwhsiao · Nov 20, 16:29 · [Discussion](https://news.ycombinator.com/item?id=50577265)

**「为什么重要」** 该研究直接关联AI Agent自主性改进的核心方向，同时引发了自主模型安全对齐风险的讨论，对关注agent自改进与安全性的工程师有参考价值。但论文宣称的无训练自改进与实际仅缩短推理轨迹的结论存在张力，其真实技术价值与安全影响尚未得到充分验证。

**「可关注」** 可关注：论文宣称的无梯度自改进与实际仅缩短推理轨迹的结论存在明显张力，需结合原文验证其技术细节与真实改进幅度。

**「评论」** 社区对该研究的实际改进幅度普遍持怀疑态度，认为其效果与weight-space programming研究、Google sleep框架的结论一致，仅能通过缩短推理轨迹规避token限制；同时有讨论指出该研究存在AI安全风险，担忧自主运行的LLM可能通过修改权重规避安全对齐机制。

**Tags**: `#orchestration`, `#eval`, `#harness`

---

<a id="item-agent-engineer-2"></a>
### [Inkling 2 Mini 开源发布](https://thinkingmachines.ai/news/inkling-2-mini/) ⭐️ 7.0/10

Thinking Machines 于 2026-11-20 开源发布 Inkling 2 Mini，采用 looped transformer 架构，面向本地推理优化。官方宣称其性能对标 Qwen3.8-27B 级别，训练全程使用 nvfp4。社区实测显示 llama.cpp Vulkan 在 Ryzen 395 上解码速度约 27 tokens/s，M1 Pro 32GB 上约 10 t/s（q4 xl 量化）。实际任务表现存在差异：代码生成任务通过，但钱币识别等多轮推理任务出现 12k token 的无效输出。

hackernews · jasondavies · Nov 20, 20:12 · [Discussion](https://news.ycombinator.com/item?id=50581260)

**「为什么重要」** 这是首个以 looped transformer 架构开源且明确面向本地部署的模型，若性能声明属实，可能改变小参数量 coding agent 的选型格局。但社区实测显示任务泛化能力不稳定，实际 agent 收益仍需更多验证。

**「可关注」** 可关注：社区已提供针对 llama.cpp 的约 30% 速度提升补丁（涉及 PR 32694、32657、32429、32704 及 llama-graph.cpp 修改），但尚未合并，本地部署需自行 patch。

**「评论」** 社区对 looped 架构开源表示兴奋，认为可能引发后续模型跟进；实测中代码任务表现良好，但复杂推理任务出现长输出幻觉，速度优化补丁仍处于未合并状态。

**Tags**: `#coding-agent`, `#eval`, `#orchestration`

---

<a id="item-agent-engineer-3"></a>
### [TuringSpace 交互式 CAPTCHA 基准发布](https://huggingface.co/papers/2611.25387) ⭐️ 7.0/10

2026年11月21日Hugging Face Daily Papers发布论文，提出TuringSpace：一个包含125个交互式CAPTCHA的合成网页环境，覆盖5类空间能力，需通过点击、拖拽屏幕操作完成。每个任务均为可生成新实例的程序，自带校验器与真值oracle，因此也可作为可扩展的训练gym。现有CAPTCHA基准大多已被破解且极少涉及空间任务，空间基准也极少要求动作执行，TuringSpace填补了该空白，适用于多模态大语言模型的空间推理与动作能力评估，对应eval、spatial-reasoning、agent-evaluation三类标签。

rss · Hugging Face Daily Papers · Nov 21, 03:42

**「为什么重要」** 它首次提供了同时覆盖空间推理与动作执行要求的可扩展评估工具，解决了现有CAPTCHA与空间两类基准的痛点，对开发空间动作类AI Agent的工程师有直接参考价值。

**「可关注」** 可关注：TuringSpace 的所有任务均为程序化生成，自带实例校验与真值 oracle，可直接用于空间动作类Agent的能力评估，也可作为训练 gym 生成训练样本。

**Tags**: `#eval`, `#spatial-reasoning`, `#agent-evaluation`

---

<a id="item-agent-engineer-4"></a>
### [CodeScene：代码质量影响 Agent 审查成本](https://martinfowler.com/fragments/2026-11-20.html) ⭐️ 7.0/10

Martin Fowler 2026-11-20 Fragments 转述 CodeScene 实验。实验处理 246 个开源仓库的 465 个 PR，调用 3 个 LLM 与 5 个 Agent 的审查/修复流水线。结果：CodeHealth 2.8（不健康）对比 9.7（健康），token 成本高 22-35%。Complex Method 与 Complex Conditional 代码异味是关键成本驱动。该数据对构建 coding agent、评估系统及智能体工程流程的工程师有直接影响。

rss · Martin Fowler · Nov 20, 18:38

**「为什么重要」** 这是可量化的实证，首次把代码健康度与多 Agent 流水线的 token 成本直接挂钩。对设计审查流水线、控制 AI 支出、构建代码质量门禁的团队有直接参考价值。

**「可关注」** 可关注：多 Agent 审查流水线的 token 成本随代码健康度下降而上升 22-35%，Complex Method 与 Complex Conditional 是主要驱动因素，评估基准应纳入代码质量维度。

**Tags**: `#coding-agent`, `#eval`, `#orchestration`

---

<a id="item-agent-engineer-5"></a>
### [AltRA-Test 统计测试发布](https://huggingface.co/papers/2611.26073) ⭐️ 6.0/10

2026年11月21日Hugging Face Daily Papers收录了AltRA-Test相关研究，该研究提出Alternative Annotator Test with Resampled Annotations统计测试方法，解决大规模稀疏标注场景下LLM judge性能验证的痛点。此前Alt-Test仅支持所有标注条目由相同标注者完成的密集场景，AltRA-Test无需统一标注者覆盖，通过bootstrap重采样条目、为每个条目抽取k个人类标注并替换其中1个为LLM标注，生成配对的全人类与LLM标注数据。该方法适用于依赖LLM-as-judge工作流的AI agent评估管线构建，当前公开内容未包含实验性能数据，该论文目前获得20次社区点赞。

rss · Hugging Face Daily Papers · Nov 21, 03:42

**「为什么重要」** 现有LLM judge验证方法普遍要求标注者覆盖一致，难以适配大规模标注中常见的稀疏标注场景，AltRA-Test为相关评估场景提供了可落地的统计验证框架。

**「可关注」** 可关注AltRA-Test的验证逻辑，若你的AI agent评估管线采用LLM-as-judge且存在标注者覆盖不均的问题，可参考该方法的框架设计评估环节。

**Tags**: `#eval`

---

<a id="item-agent-engineer-6"></a>
### [ZeroVLN 免微调VLM导航框架发布](https://huggingface.co/papers/2611.26414) ⭐️ 5.5/10

HF 2026年11月21日发布的每日论文摘要介绍ZeroVLN慢-快导航框架，该框架无需对视觉语言模型（VLM）主干做导航领域监督微调，通过语义工具调用接口将移动决策传递给独立动作专家执行，替代传统方案微调VLM预测几何目标的路径；该摘要在HF Daily Papers获得21次点赞，公开内容未披露完整技术细节与性能数据，对低成本视觉语言导航Agent设计有参考价值。

rss · Hugging Face Daily Papers · Nov 21, 03:42

**「为什么重要」** 当前主流视觉语言导航方案需微调VLM主干，可能损害模型通用视觉能力，ZeroVLN提出的免微调主干+动作委托思路为降低领域适配成本提供了新方向；但公开信息未包含完整性能验证结果，实际效果尚未证实。

**「可关注」** 免微调VLM主干、通过语义工具调用将动作执行委托给独立专家的 orchestration 模式，可减少大模型领域适配的算力与数据成本。

**Tags**: `#orchestration`, `#vlm-agent`, `#tool-calling`

---

## AI Daily

<a id="item-ai-daily-1"></a>
### [OpenAI 公布对抗性蒸馏分层防御方案](https://openai.com/index/combatting-adversarial-distillation) ⭐️ 6.8/10

On November 20, 2026, OpenAI published an official blog post outlining a layered defense approach to combat adversarial distillation and capability extraction. The framework integrates four core components: model training, safeguards, detection, and enforcement. No specific technical details, performance metrics, or deployment timelines are disclosed in the public release.

rss · OpenAI Blog · Nov 20, 10:00

**「为什么重要」** Adversarial distillation poses a potential risk of AI model capability leakage, and this publicly released layered defense framework is relevant to AI security practice.

**「可关注」** Note: OpenAI has consolidated model training, safeguards, detection, and enforcement into a unified layered defense framework against adversarial distillation.

**Tags**: `#model`, `#lab`, `#industry`, `#policy`

---

<a id="item-ai-daily-2"></a>
### [Sage S2.1 Flash技术报告开源](https://mp.weixin.qq.com/s?__biz=MzA3MzI4MjgzMw==&amp;mid=2651075493&amp;idx=3&amp;sn=63643451e794a6d8ac3dbb423d7f460d) ⭐️ 5.5/10

上海AI Lab联合复旦大学、中国科学院软件研究所等多家科研机构与高校，正式发布Sage S2.1 Flash技术报告，披露总参数量达320B的混合专家（MoE）模型的完整训练流程与技术细节。该模型在四项智能体基准上达到SOTA，采用统一架构处理文本、图像与科学数据，支持工具调用、专业软件操作等复杂任务。示例显示模型可仅凭指令从12487张CT图像中筛选切片，调用3D Slicer重建三维骨骼模型。

rss · 机器之心 · Nov 20, 03:58

**「为什么重要」** 该报告公开了大参数MoE智能体模型的完整训练细节，同时探索了科学多模态能力融入通用智能体架构的实践路径，对多模态智能体研发有直接参考价值。

**「可关注」** 可关注：Sage S2.1 Flash采用统一多模态主干，通过动态专家路由控制推理计算量，结合稀疏注意力与线性注意力支持长上下文处理，可直接接入科学专用模态。

**Tags**: `#model`, `#lab`, `#open-source`, `#eval`

---

## AI Deals

<a id="item-ai-deals-1"></a>
### [Epic 11.20~11.26 限免游戏汇总](https://www.appinn.com/eggs-261120/) ⭐️ 8.0/10

你看到的内容可能由第三方 AI 基于小众软件文章提炼总结而成，可能与原文真实意图存在偏差。不代表小众软件观点和立场。请&lt;a href=&quot;https://www.appinn.com/eggs-261120/&quot; target=&quot;\_blank&quot;&gt;点击链接阅读原文&lt;/a&gt;细致比对和校验。&lt;br /&gt;&lt;br /&gt;Epic 本周（11.20~11.26）开启限时免费领取福利，PC 端可领海盗题材动作冒险游戏《深渊之印 / Mark of the Deep》，移动端可领无战斗解谜生活模拟游戏《Lonesome Village》。两款游戏均支持中文，Steam 评价均为多半好评。领取需登录对应平台的 Epic 账号，在官方商店页完成领取操作，限免周期截至 11 月 26 日。

rss · 小众软件 · Nov 20, 07:21

**「为什么重要」** 两款游戏均为支持中文的 Steam 多半好评作品，限免周期仅一周，错过后续需付费获取，适合对应平台玩家领取。

**「可关注」** 可关注：PC 端《深渊之印》融合类银河战士恶魔城探索与类魂战斗，移动端《Lonesome Village》主打解谜与村庄生活模拟，需对应平台 Epic 账号领取，无额外领取门槛。

**Tags**: `#limited-free`, `#promo`

---

<a id="item-ai-deals-2"></a>
### [波波小红书获客助手 送30天激活码](https://www.v2ex.com/t/1258559#reply40) ⭐️ 8.0/10

V2EX 用户 gybin02 发起波波小红书获客助手送码活动，前 50 条有效回帖可领取 30 天版激活码。领取需在回帖中提供邮箱（支持 Base64 编码防爬）并回答‘你现在怎么找小红书上的意向客户、回评论，最烦的是哪一步’，一人仅首条回帖有效。激活码将发送至预留邮箱，激活后绑定设备，30 天内可使用全量功能，到期后可选择 19.9 元买断永久版，无自动扣费。

rss · V2EX Hot · Nov 20, 07:04

**「为什么重要」** 小红书运营的养号、评论回复、线索挖掘均为高频重复环节，该工具可自动化处理上述流程，30 天免费版足够验证是否匹配自身获客 workflow。

**「可关注」** 可关注：该工具为 Chrome/Edge 插件，AI 评论、私信自动回复等参数可自行调整，建议先用保守节奏测试，避免触发平台风控。

**Tags**: `#promo`, `#limited-free`, `#coupon`

---

<a id="item-ai-deals-3"></a>
### [Ferry 免费 iOS 远程桌面发布](https://www.v2ex.com/t/1258592#reply25) ⭐️ 7.0/10

开发者 reallinzc1 推出完全免费、无广告无内购的 iOS/iPadOS 远程桌面应用 Ferry，可用于连接 Mac，目前可在 App Store 和 TestFlight 下载，无需注册。其逆向了 macOS 14 的高性能屏幕共享协议，支持 HEVC 视频流与 AAC-ELD 音频传输，同局域网实测帧率约 57 帧，远高于传统 VNC 模式。使用条件为 Apple 芯片 Mac、macOS 14 及以上，需在系统设置的通用-共享中开启屏幕共享，使用 Mac 账户密码登录，Mac 端无需安装额外软件，连接期间 Mac 屏幕会熄灭，断开后恢复。

rss · V2EX Hot · Nov 20, 08:10

**「为什么重要」** 现有免费远程桌面工具 UU 远程将于 12 月起限制免费版为 1080p 30 帧，虚拟屏功能需会员，Ferry 作为无广告无内购的替代方案，可满足高频远程操控 Mac 的需求。

**「可关注」** 可关注：高性能模式仅支持 UDP 直连，经中继/隧道/代理会退回无声音的普通 VNC 模式；仅适配 Apple 芯片 Mac 且需 macOS 14 以上，必须用 Mac 账户密码登录，仅设 VNC 密码无法使用高性能模式。

**Tags**: `#free-tier`, `#apple-app`, `#testflight`, `#remote-desktop`, `#no-registration`

---