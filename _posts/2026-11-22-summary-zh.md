---
layout: default
title: "Horizon Summary: 2026-11-22 (ZH)"
date: 2026-11-22
lang: zh
---

> 从 140 条内容中筛选出 10 条重要资讯。

<nav id="ah-toc" class="ah-toc" aria-label="目录"><span class="ah-toc-title">目录</span><ul><li><a href="#sec-harness-arch"><span class="ah-toc-name">Harness 架构</span><span class="ah-toc-count">2条</span></a></li><li><a href="#sec-agent-engineer"><span class="ah-toc-name">Agent 工程师日报</span><span class="ah-toc-count">4条</span></a></li><li><a href="#sec-ai-daily"><span class="ah-toc-name">AI 日报</span><span class="ah-toc-count">3条</span></a></li><li><a href="#sec-ai-deals"><span class="ah-toc-name">AI 羊毛</span><span class="ah-toc-count">1条</span></a></li></ul></nav>

---

**[Harness 架构](#sec-harness-arch)**
1. [Cline SDK v0.2.1 发布](#item-harness-arch-1) ⭐️ 5.5/10
2. [fastmcp v4.2.4 发布](#item-harness-arch-2) ⭐️ 5.3/10

**[Agent 工程师日报](#sec-agent-engineer)**
1. [AltRA-Test 论文发布](#item-agent-engineer-1) ⭐️ 6.0/10
2. [TuringSpace 交互式 CAPTCHA 基准发布](#item-agent-engineer-2) ⭐️ 6.0/10
3. [HF 每日论文：ZeroVLN 免微调导航框架](#item-agent-engineer-3) ⭐️ 6.0/10
4. [Mind2Act World 机器人操作诊断基准发布](#item-agent-engineer-4) ⭐️ 5.5/10

**[AI 日报](#sec-ai-daily)**
1. [腾讯元宝×KCL 发布群聊记忆基准](#item-ai-daily-1) ⭐️ 5.5/10
2. [Karpo 31B 开源 浏览器 Agent](#item-ai-daily-2) ⭐️ 5.5/10
3. [TML 开源 Inkling 2 Mini 端侧循环模型](#item-ai-daily-3) ⭐️ 5.5/10

**[AI 羊毛](#sec-ai-deals)**
1. [Google AI Pro 黑五五折](#item-ai-deals-1) ⭐️ 8.0/10

---

## Harness 架构
{: #sec-harness-arch .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-harness-arch" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-harness-arch-1"></a>
### [Cline SDK v0.2.1 发布](https://github.com/cline/cline/releases/tag/sdk/sdk/v0.2.1) ⭐️ 5.5/10

这是 cline/cline SDK v0.2.1 版本的正式发布，核心优化工具结果上限、推理占位处理、摘要器逻辑及默认模型配置，同时扩展工具链与 Hub 能力。read\_files 工具结果不再被截断至 8k，改用 50k 文件内容上限，其余工具结果保持 8k 上限。新增交错推理占位字段 reasoning\_content，修复 Reflection Beam 模型在会话压缩或模型切换后的参数缺失报错，同时修正摘要器推理偏好与自定义模型推理 seeding 逻辑，避免未编目模型、gpt-5.x 及 o 系列模型被传入拒绝的参数。

github · github-actions\[bot\] · 11月21日 05:19

**「设计要点」** 运行时层面，核心在启用工具与 spawn\_agent 能力时注册 ux\_verifier 子代理，通过 host 的 spawn\_agent 执行器分发检查清单；Hub 侧支持分块返回会话历史、归档云历史，云任务支持 initialMessage 一步创建发送、localGit 从 Git 快照启动，会话配置与 Hub RPC schema 支持 max 推理等级，云命令需账户验证，提供者管理需令牌认证。工具层新增 report\_ux\_verification、publish\_artifacts 两个可选工具，MCP 工具描述透传服务器工具提示，task.tool\_used 遥测新增 mode 字段；移除了 CLINE\_CAPTURE\_\*系列的请求磁盘写入功能，SDK 各包现在均包含许可证文件。

**「改了什么」** 工具链层面调整 read\_files 结果上限至 50k、其余工具保持 8k，修复交错推理占位缺失导致的 Reflection Beam 报错，修正摘要器推理偏好与自定义模型推理 seeding 逻辑，避免未编目模型被强制传入被拒绝的 reasoning\_effort: &quot;none&quot;参数。原生 OpenAI 适配器适配模型 effort 阶梯，不再将 max、Extra High 等推理等级原样发送给 GPT-5.x 及 o 系列模型；LiteLLM 适配器调整输入预算逻辑，设置 max\_output\_tokens 时不再使用 legacy max\_tokens 作为输入预算，空限制视为缺失。运行中的会话压缩任务现在支持停止，取消操作纳入遥测统计。默认模型变更为 anthropic/claude-sonnet-5.5，cline 提供者 bundled 默认改为首个免费模型。模型目录从 6457 个扩展至 7621 个，新增 94 个 providers.dev 提供者，调整多个提供者的默认模型与免费模型列表。新增 UX 验证、制品发布两个可选工具，Hub 支持会话历史分块返回、云任务快捷创建与无沙箱制品下载，session.resume 支持直接读取 Hub 历史启动已保存会话。

**「评论」** 暂无社区评论内容。

**标签**: `#runtime`, `#tools`, `#prefix-cache`

---

<a id="item-harness-arch-2"></a>
### [fastmcp v4.2.4 发布](https://github.com/PrefectHQ/fastmcp/releases/tag/v4.2.4) ⭐️ 5.3/10

fastmcp v4.2.4 是 PrefectHQ 发布的 MCP 框架补丁版本。修复 OAuth proxy 竞态条件安全漏洞（GHSA-78c8-3jhx-5mg7），防止并发请求重复兑换同一授权码或刷新令牌。撤销的 proxy access token 刷新后保持无效。同时修复挂载与版本化组件处理及 tool transform 行为，避免单个 transform 失败导致全部工具列表损坏。

github · zzstoatzz · 11月21日 05:24

**「改了什么」** 并发 token 请求不再重复兑换同一 OAuth proxy 授权码或刷新令牌；撤销的 access token 刷新后保持撤销状态。tool transform 无法应用时仅隐藏自身 tool，不再破坏整个工具列表。修复版本化组件重复列出、挂载组件响应及合并默认值破坏调用者对象等问题。

**标签**: `#mcp`, `#runtime`, `#tools`, `#permissions`

---

## Agent 工程师日报
{: #sec-agent-engineer .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-agent-engineer" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-agent-engineer-1"></a>
### [AltRA-Test 论文发布](https://huggingface.co/papers/2611.26073) ⭐️ 6.0/10

2026 年 11 月 21 日 Hugging Face Daily Papers 推送 AltRA-Test 相关论文，提出同名统计检验方法。相比要求所有标注项由同一批标注者完成的 Alt-Test，该方法适配大规模标注中不同标注员标注不同子集的稀疏场景，通过 bootstrap 重采样标注项、每项抽取 k 条人工标注并替换其中 1 条为 LLM 标注，生成成对的全人工与混合标注样本，用于验证 LLM 替代人工标注员的统计合理性。该方法适用场景聚焦标注验证、LLM 作为评测 judge 领域，无通用 agent 工程相关突破性更新。

rss · Hugging Face Daily Papers · 11月21日 23:00

**「为什么重要」** 该方法为稀疏标注场景下验证 LLM 替代人工标注的合理性提供了新工具，可支撑使用 LLM 作为评测 judge 的 agent 工程师做相关决策，但当前仅聚焦标注验证领域，未涉及通用 agent 工程的突破性更新。

**「可关注」** 可关注：稀疏标注场景下验证 LLM judge 替代人工标注合理性时，可参考 AltRA-Test 的 bootstrap 重采样配对设计。

**标签**: `#eval`, `#llm-judge`, `#annotation-validation`

---

<a id="item-agent-engineer-2"></a>
### [TuringSpace 交互式 CAPTCHA 基准发布](https://huggingface.co/papers/2611.25387) ⭐️ 6.0/10

2026 年 11 月 21 日，Hugging Face Daily Papers 收录 TuringSpace 相关研究论文，该研究提出包含 125 个交互式 CAPTCHA 的合成网页环境基准，覆盖 5 类空间能力，需通过点击、拖拽屏幕操作完成。每个任务均为可生成新实例的程序，内置检查器与参考解，可作为多模态大模型空间智能与交互动作能力的评估、训练 gym。当前该资源属于小众研究类工具，暂无对主流 agent 工具链的直接影响，也无已知 breaking changes。

rss · Hugging Face Daily Papers · 11月21日 23:00

**「为什么重要」** 该基准填补了现有 CAPTCHA 基准多已被破解、且极少覆盖空间能力，以及通用空间基准多不要求交互动作的空白，为评估多模态大模型的空间推理与交互能力提供了可复现、可扩展的测试场景。其对实际 agent 研发的影响尚未得到广泛验证。

**「可关注」** 可关注：若团队正在研发需要视觉-空间交互的 coding agent，可参考其程序化生成任务+内置检查器的设计，搭建同类型的可扩展交互评估环境。

**标签**: `#eval`

---

<a id="item-agent-engineer-3"></a>
### [HF 每日论文：ZeroVLN 免微调导航框架](https://huggingface.co/papers/2611.26414) ⭐️ 6.0/10

2026 年 11 月 21 日 Hugging Face Daily Papers 收录预印本论文《ZeroVLN: Learning to Navigate without Supervised Fine-Tuning of the VLM Brain》，提出视觉语言导航框架 ZeroVLN。该框架采用慢-快双模块设计，无需对 VLM 大脑做导航域有监督微调，通过语义工具调用接口将移动决策传递给专用动作专家，先完成动作专家对移动请求的适配，再联合优化大脑决策与动作专家协同。当前仅为预印本，未公开生产级实现细节与可泛化评估结果，相关标签为 orchestration、eval、mcp。

rss · Hugging Face Daily Papers · 11月21日 23:00

**「为什么重要」** 该框架将 VLM 的语义决策能力与专用动作执行模块解耦的思路，与当前 AI Agent 编排、MCP 工具集成的技术方向存在可参考的相似性，但相关结论尚未经过充分的实验验证。

**「可关注」** 可关注：通过语义工具调用接口分离大模型决策与动作执行，为减少领域微调对基础模型通用能力的破坏提供了可参考的技术路径。

**标签**: `#orchestration`, `#eval`, `#mcp`

---

<a id="item-agent-engineer-4"></a>
### [Mind2Act World 机器人操作诊断基准发布](https://huggingface.co/papers/2611.26444) ⭐️ 5.5/10

2026 年 11 月 21 日 Hugging Face Daily Papers curated arXiv preprint《Mind2Act World》，该 curation 获得 50 次 upvotes。这是一款机器人操作诊断基准，包含 30 个来自 5 个真实应用领域的模拟操作任务，设置 3 个难度等级、2 种场景（Clean/Random），共 180 个任务配置，核心设计是将智能体失败模式拆分为推理、执行、推理-执行组合三类分别评估，解决现有基准无法定位失败来源的问题。当前公开内容不完整，缺少完整评估指标、基线结果、工具链集成细节，且聚焦机器人操作领域，对多数 coding agent 工程师的直接参考价值有限。

rss · Hugging Face Daily Papers · 11月21日 23:00

**「为什么重要」** 该基准的“诊断式评估”设计模式可迁移至其他智能体评估场景，是当前少有的专门拆解推理-执行组合失效的评估框架；但当前内容为二手 curation，缺少一手官方发布渠道（如官方博客、GitHub 仓库、正式文档），且聚焦机器人操作，对 coding agent 领域的直接适用性尚未验证。

**「可关注」** 可关注：诊断式评估框架将推理、执行、组合三类失效解耦的设计思路，可参考用于 coding agent 的失败归因场景，但需注意当前基准未公开完整评估逻辑与工具链集成细节，无法直接复用。

**标签**: `#eval`, `#embodied-agent`

---

## AI 日报
{: #sec-ai-daily .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-daily" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-daily-1"></a>
### [腾讯元宝×KCL 发布群聊记忆基准](https://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw==&amp;mid=2247947677&amp;idx=3&amp;sn=0797fbd2116a405b44176c97577757d8) ⭐️ 5.5/10

腾讯元宝与伦敦国王学院 NLP 团队联合发布首个基于群聊构建的 Agent 记忆基准 GroupAssistBench。该基准基于 50 个真实群聊的 80299 条历史消息构建 2395 道评测题，用于检验 Agent 记忆从&quot;记得住&quot;到&quot;用得好&quot;的能力。研究团队对比了完整上下文、检索增强、外部记忆等 14 组配置，发现 EverMemOS 在 L1 记忆召回评测中得 0.621，高于使用相同任务模型的完整上下文配置的 0.570；但在 L2 开放式服务评测中仅得 0.247，低于完整上下文配置的 0.431。

rss · 量子位 · 11月21日 09:52

**「为什么重要」** 现有 Agent 记忆能力评测多聚焦单用户场景，该基准首次覆盖群聊多成员、多决策状态的复杂记忆使用需求，填补了对应领域的评测空白。

**「可关注」** 可关注：GroupAssistBench 的评测结果显示记忆召回得分与实际服务得分存在明显倒挂，提示 Agent 记忆优化不能仅聚焦召回准确率，还需提升记忆筛选与场景适配能力。

**标签**: `#lab`, `#industry`, `#eval`, `#product`

---

<a id="item-ai-daily-2"></a>
### [Karpo 31B 开源 浏览器 Agent](https://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw==&amp;mid=2247947677&amp;idx=1&amp;sn=ebf1f96b9afceacdfa0d407ecdb3ff2b) ⭐️ 5.5/10

量子位报道称，MachinePulse AI 开源决策模型 Karpo Decision 31B 及配套浏览器操作框架。该模型在《城市扫描仪》挑战中完成 36 场活动筛选任务（共 36 道题）耗时 2.6 秒，速度约为 Gemini 3.5 Flash（14.96 秒）的 6 倍，准确率 100%，成本仅为后者的十三分之一；在 300 个模型参与的 Decision Index 评测总榜中以 73.9 分位列第一，中位响应时间 94 毫秒，单题最多可同时判断 255 个候选选项，校准误差 2.3%。

rss · 量子位 · 11月21日 09:52

**「为什么重要」** 该模型专为 Agent 高频低延迟决策场景设计，配套浏览器操作框架同步开源，可降低浏览器 Agent 的开发与部署门槛，为相关场景提供轻量可选方案。

**「可关注」** 可关注：Karpo Decision 31B 单卡 RTX PRO 6000 即可部署，中位响应时间 94 毫秒，配套开源的 karpo-browser 框架与 KBB 评测集可参考用于浏览器 Agent 决策场景开发。

**标签**: `#model`, `#open-source`, `#industry`, `#agent`

---

<a id="item-ai-daily-3"></a>
### [TML 开源 Inkling 2 Mini 端侧循环模型](https://mp.weixin.qq.com/s?__biz=MzA3MzI4MjgzMw==&amp;mid=2651075624&amp;idx=2&amp;sn=b6e7e23d631dba7a952cbe5da8e77769) ⭐️ 5.5/10

本次信息来自机器之心的二手报道，未附官方一手发布链接。TML 开源 26B 参数循环 Transformer 多模态模型 Inkling 2 Mini，权重按 Apache 2.0 许可发布，支持文本、图像输入，最大上下文窗口 100 万 token，官方宣称可在笔记本运行，AA Index 得分 20.1。模型共 24 层，前、后各 6 层运行 1 次，中间 12 层运行 3 次，采用 MoE 架构，激活参数约 3.4B，计入循环重复计算后有效激活参数约 5.4B；开发者可下载部署，也可通过 Tinker 进行推理和微调。官方演示使用配备 48GB 内存的 M5 Pro MacBook Pro 离线完成推理，可写出可玩飞行模拟器、驱动 20 位村民的像素小镇，模型卡与官方博客已公开。

rss · 机器之心 · 11月21日 04:11

**「为什么重要」** 该模型将 26B 参数循环 Transformer 的部署门槛降到笔记本级别，结合社区已有的 harness 接入、游戏速通、动画生成等尝试，展示了端侧大模型在复杂任务执行上的可能性。

**「可关注」** 可关注：循环 Transformer 通过复用中间 12 层实现 24 层权重完成 48 次层计算，配合 MoE 将激活参数控制在 3.4B，是端侧大模型的一种架构探索方向。

**「评论」** 社区反馈热烈，已有开发者将其接入 DeepSeek Harness 获得较快推理速度，还有用户尝试让其通关电子游戏并实现速通、生成动画 MV 等。

**标签**: `#model`, `#open-source`, `#lab`, `#eval`

---

## AI 羊毛
{: #sec-ai-deals .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-deals" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-deals-1"></a>
### [Google AI Pro 黑五五折](https://www.appinn.com/google-ai-pro-black-friday-2026/) ⭐️ 8.0/10

你看到的内容可能由第三方 AI 基于小众软件文章提炼总结而成，可能与原文真实意图存在偏差。不代表小众软件观点和立场。请&lt;a href=&quot;https://www.appinn.com/google-ai-pro-black-friday-2026/&quot; target=&quot;\_blank&quot;&gt;点击链接阅读原文&lt;/a&gt;细致比对和校验。&lt;br /&gt;&lt;br /&gt;Google 在美区推出 AI Pro 及 AI Plus 年付黑五五折促销活动，美区原价 199.99 美元/年，优惠后年费约 99.99 美元，折合每月 8.33 美元。11 月 20 日至 26 日现有 Google One、Google AI 订阅老用户可提前参与，11 月 27 日起向符合条件的新用户开放，不同账户实际折扣可能不同，且首个优惠周期后后续费大概率恢复原价。

rss · 小众软件 · 11月21日 11:14

**「为什么重要」** 对于常使用 Gemini 高级模型、NotebookLM 增强功能，或是本就付费订阅 Google One 云存储的用户，此次五折是低成本获取 AI Pro 权益的窗口期，老用户无需等待新用户批次即可参与。

**「可关注」** 可关注：活动仅面向美区符合条件账户，折扣仅首个优惠周期有效，后续续费将恢复原价；已有 Google One 年费订阅的用户建议直接升级至 AI Pro，无需先取消原订阅，可按比例抵扣剩余费用或折算为额外使用时间。

**标签**: `#promo`, `#coupon`, `#limited-offer`, `#subscription`

---