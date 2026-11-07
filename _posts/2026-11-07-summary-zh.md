---
layout: default
title: "Horizon Summary: 2026-11-07 (ZH)"
date: 2026-11-07
lang: zh
---

> 从 180 条内容中筛选出 12 条重要资讯。

<nav id="ah-toc" class="ah-toc" aria-label="目录"><span class="ah-toc-title">目录</span><ul><li><a href="#sec-harness-arch"><span class="ah-toc-name">Harness 架构</span><span class="ah-toc-count">3条</span></a></li><li><a href="#sec-agent-engineer"><span class="ah-toc-name">Agent 工程师日报</span><span class="ah-toc-count">6条</span></a></li><li><a href="#sec-ai-daily"><span class="ah-toc-name">AI 日报</span><span class="ah-toc-count">2条</span></a></li><li><a href="#sec-ai-deals"><span class="ah-toc-name">AI 羊毛</span><span class="ah-toc-count">1条</span></a></li></ul></nav>

---

**[Harness 架构](#sec-harness-arch)**
1. [adk-python v2.14.0 发布](#item-harness-arch-1) ⭐️ 8.8/10
2. [OpenHands v1.37.0 发布](#item-harness-arch-2) ⭐️ 6.3/10
3. [Agent Framework 1.28.0](#item-harness-arch-3) ⭐️ 5.8/10

**[Agent 工程师日报](#sec-agent-engineer)**
1. [Harness-S 框架提出通用 Agent 训练方法](#item-agent-engineer-1) ⭐️ 7.0/10
2. [Drex 非自回归决策模型发布](#item-agent-engineer-2) ⭐️ 7.0/10
3. [ChatGPT 静默路由工具调用 赏金需 ID 验证](#item-agent-engineer-3) ⭐️ 6.0/10
4. [BestRand 缓解基准评估随机采样不稳定性](#item-agent-engineer-4) ⭐️ 6.0/10
5. [VisSearch-Bench 视觉搜索评估基准发布](#item-agent-engineer-5) ⭐️ 6.0/10
6. [NousResearch 发布 Arete-27B 微调模型](#item-agent-engineer-6) ⭐️ 6.0/10

**[AI 日报](#sec-ai-daily)**
1. [OpenAI 与 Hacktron 合作开展漏洞测试](#item-ai-daily-1) ⭐️ 7.8/10
2. [GitHub 发布智能体工程开发者指南](#item-ai-daily-2) ⭐️ 6.8/10

**[AI 羊毛](#sec-ai-deals)**
1. [本周 Epic 免费游戏 11.6~11.12](#item-ai-deals-1) ⭐️ 8.0/10

---

## Harness 架构
{: #sec-harness-arch .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-harness-arch" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-harness-arch-1"></a>
### [adk-python v2.14.0 发布](https://github.com/google/adk-python/releases/tag/v2.14.0) ⭐️ 8.8/10

google/adk-python v2.14.0 正式发布，将核心运行时、沙箱执行环境、A2A 协议支持和评估模块从实验状态转为稳定。新增分块文件流式传输（\`BaseEnvironment.read\_file\_stream\`）、多轮评估（\`MultiRunConfig\`）、语义工具参数匹配（\`ToolArgsMatcher\`），以及 Microsoft Teams 和 OpenAI Decisions 集成。长多轮工作流性能提升，30 节点 200 轮运行耗时降低 23%，峰值内存降低 9%。同时引入破坏性变更：Enum 工具参数现在以成员形式传递，\`VertexAiSessionService.create\_session\` 限制额外关键字参数，\`RunSkillScriptTool\` 在环境模式下不再接受 \`command\`。

github · haranrk · 11月7日 00:58

**「设计要点」** 运行时核心与沙箱环境稳定，通过 \`BaseEnvironment.read\_file\_stream\` 分块流式传输降低大文件内存占用。评测层支持 \`MultiRunConfig\` 并发多轮运行与 \`ToolArgsMatcher\` 语义匹配，记忆服务新增向量检索与 TTL；工具执行从自由格式 shell 命令转向验证路径参数（\`RunSkillScriptTool\`）。

**「改了什么」** 核心运行时、沙箱环境、A2A 和评估模块从实验状态转为稳定，新增分块文件流式读取、多轮并发评估、语义工具参数匹配及 Teams、OpenAI Decisions、MongoDB 向量记忆集成。工作流执行效率提升，30 节点 200 轮场景耗时降低 23%；破坏性变更包括 Enum 工具参数改为传递成员对象、\`VertexAiSessionService.create\_session\` 限制关键字参数、\`RunSkillScriptTool\` 移除 \`command\` 参数。

**标签**: `#runtime`, `#sandbox`, `#a2a`, `#eval`, `#tools`

---

<a id="item-harness-arch-2"></a>
### [OpenHands v1.37.0 发布](https://github.com/OpenHands/OpenHands/releases/tag/v1.37.0) ⭐️ 6.3/10

OpenHands v1.37.0 于 2026-11-06 发布。本次更新为自动化流程新增 Mermaid 图解释，优化聊天历史扫描性能，并修复会话恢复、首页路径等 bug。无架构变更或运行时重写，改动集中在 UI/UX 与稳定性。

github · openhands-release-bot\[bot\] · 11月6日 12:54

**「改了什么」** 自动化流程新增 Mermaid 图解释。聊天历史扫描性能优化，避免实时更新时重复扫描；会话恢复、首页路径等 bug 修复；依赖升级与代码清理。

**标签**: `#chat`, `#session-management`, `#performance`, `#automations`, `#memory`

---

<a id="item-harness-arch-3"></a>
### [Agent Framework 1.28.0](https://github.com/microsoft/agent-framework/releases/tag/dotnet-1.28.0) ⭐️ 5.8/10

Microsoft Agent Framework .NET 发布 dotnet-1.28.0。本次 minor 更新包含 .NET 运行时修复、Python 侧增量功能及跨语言维护修正。.NET 端修复声明式工作流公式解析的 InvariantCulture 问题，并引入 A2A 代理创建简化、HTTP 主机白名单、MCP 客户端调用级作用域等 \[BREAKING\] 变更。Python 端新增并发 MCP 调用支持、收窄未作用域 URL 会话批准规则，并修复 Python 3.15 的 Redis 集成。

github · dmytrostruk · 11月6日 22:00

**「设计要点」** 框架采用多语言 SDK 统一发版策略，.NET 与 Python 共享版本号但独立迭代。权限模型向最小特权收紧：MCP 会话、URL 批准、HTTP 主机及授权范围均从全局改为按调用或显式配置作用域。

**「改了什么」** .NET 端修复工作流公式解析的区域性依赖，简化 A2A 代理创建与负载处理，强制配置允许的 HTTP 主机，并将工作流 MCP 客户端范围限定到单次调用。Python 端支持并发 MCP 请求、收窄未作用域 URL 会话自动批准规则，并恢复 Python 3.15 的 Redis 集成支持。

**标签**: `#runtime`, `#mcp`, `#permissions`, `#memory`

---

## Agent 工程师日报
{: #sec-agent-engineer .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-agent-engineer" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-agent-engineer-1"></a>
### [Harness-S 框架提出通用 Agent 训练方法](https://huggingface.co/papers/2611.04277) ⭐️ 7.0/10

2026 年 11 月 7 日，Hugging Face Daily Papers 收录论文《Harness-S: Learning from Sibling Harnesses for Generalizable Agent Training》。该论文提出 Harness-S 训练框架，观察到从共同基础演化的 harness 具备 Locality、Complementarity 和 Nonstationarity 性质，据此构建固定 Sibling Harness Pool，并通过 Complementary Harness Rescue Training 在基础执行系统全部失败时调用 sibling harnesses rescue 失败，再将能力迁移回单一策略。框架通过 Directional Harness Evolution 沿不同修复方向生成 specialized harnesses，训练期间保持 pool 不变。论文未公开具体实验基准或性能数字，实际泛化效果待验证。

rss · Hugging Face Daily Papers · 11月7日 03:13

**「为什么重要」** 该工作直接针对 agent 训练中 harness 设计痛点，提出可复用的 sibling harness 池与 rescue 训练范式，可能减少对单一 harness 优化的依赖。但论文未提供跨环境泛化实验，实际效果待验证。

**「可关注」** 可关注：Harness-S 将 harness 演化性质（Locality、Complementarity、Nonstationarity）转化为固定 sibling pool 与按需 rescue 的训练流程，为多 harness 协作提供新思路。

**标签**: `#harness`

---

<a id="item-agent-engineer-2"></a>
### [Drex 非自回归决策模型发布](https://huggingface.co/papers/2611.07854) ⭐️ 7.0/10

2026 年 11 月 7 日 Hugging Face Daily Papers 发布开源非自回归决策模型家族 Drex，包含 8B（DLM）、9B（v1.5）、35B 含 3B 激活（v2.0）、27B（Max）四款参数规模的模型，原生支持智能体上下文作为输入，旨在替代自回归 LLM 用于智能体决策任务，解决输出不一致、强制解析、成本高、延迟高的生产痛点。当前公开内容被截断，暂未披露性能基准与详细架构拆解，主要面向 AI 智能体工程师群体。

rss · Hugging Face Daily Papers · 11月7日 03:13

**「为什么重要」** 该模型直接针对智能体决策环节中自回归 LLM 的普遍生产痛点，提供了开源的替代方案选项；但当前缺乏公开性能验证，实际落地效果尚未证实。

**「可关注」** 可关注：原生接受智能体上下文的非自回归决策模型 Drex，可作为智能体决策组件的潜在替代方案，减少输出解析开销与推理延迟。

**标签**: `#coding-agent`, `#harness`, `#eval`

---

<a id="item-agent-engineer-3"></a>
### [ChatGPT 静默路由工具调用 赏金需 ID 验证](https://community.openai.com/t/security-follow-up-tool-call-silently-routed-to-a-different-connector/1413053) ⭐️ 6.0/10

2026 年 11 月 6 日 Hacker News 讨论引用的 OpenAI 社区安全帖指出，ChatGPT 可静默将工具调用路由到不同连接器；评论者澄清该行为是 OpenAI 与 MCP 系统的预期表现，因二者未对独立工具调用设置作用域或绑定限制。同时 OpenAI 托管漏洞赏金计划（MBB）已要求所有提交报告的研究者完成身份验证（IDV），以减少低质量提交。该事件涉及 AI Agent 开发者、MCP 工具集成方及漏洞赏金提交者。

hackernews · Aldipower · 11月6日 22:50 · [社区讨论](https://news.ycombinator.com/item?id=50399569)

**「为什么重要」** 该路由行为揭示当前 OpenAI 与 MCP 工具调用无作用域绑定的设计特性，对 Agent 权限控制逻辑设计有直接参考价值；赏金计划 ID 验证要求则直接适用于所有计划提交 OpenAI 托管漏洞赏金的研究者。

**「可关注」** 可关注：OpenAI 与 MCP 当前未对独立工具调用设置作用域或绑定限制，设计 Agent 工具调用逻辑时需避免依赖未绑定的调用上下文做权限判断。

**「评论」** 社区评论普遍认为工具调用静默路由是 OpenAI 与 MCP 系统设计限制而非安全漏洞，同时有评论指出赏金计划 ID 验证要求源于 Bugcrowd 平台减少低质量提交的政策，与制裁合规无关。

**标签**: `#mcp`, `#orchestration`, `#permissions`

---

<a id="item-agent-engineer-4"></a>
### [BestRand 缓解基准评估随机采样不稳定性](https://huggingface.co/papers/2611.00883) ⭐️ 6.0/10

2026-11-07，Hugging Face Daily Papers 收录论文《Random Is Almost Enough? Stable and Low-Cost Benchmark Compression via BestRand》。该论文提出 BestRand 基准压缩方法，通过解析近似子集评估误差分布，缓解纯随机采样的长尾不稳定性。研究表明，随机采样在概率上能取得小误差，但少数子集会产生大误差，形成长尾分布；该不稳定性是现代基础模型固有特性，不会随评估模型数量增加而消失。当前摘要被截断，缺少具体性能对比数据与完整算法细节，需阅读原文获取完整信息。

rss · Hugging Face Daily Papers · 11月7日 03:13

**「为什么重要」** 基准评估成本高是 agent 工程中的常见痛点。BestRand 若验证有效，可在降低评估成本的同时提升结果稳定性，但当前仅为论文摘要，实际效果需阅读原文确认。

**「可关注」** 纯随机采样在基准压缩中概率上表现良好，但长尾大误差导致不稳定，BestRand 通过误差分布建模试图解决该问题。

**标签**: `#eval`

---

<a id="item-agent-engineer-5"></a>
### [VisSearch-Bench 视觉搜索评估基准发布](https://huggingface.co/papers/2611.04894) ⭐️ 6.0/10

2026 年 11 月 7 日 Hugging Face Daily Papers 公开了多模态智能体评估基准 VisSearch-Bench 的摘要信息，该基准包含 204 个人工编写的任务，覆盖 7 个主领域、25 个子领域，核心评估智能体的长程视觉搜索与跨模态视觉上下文管理能力。当前公开内容仅为不完整摘要，未披露技术细节、性能基线及明确的资源可用性信息，主要面向关注多模态智能体视觉搜索能力评估的工程师群体。

rss · Hugging Face Daily Papers · 11月7日 03:13

**「为什么重要」** 当前多数多模态智能体视觉搜索类评估仅测试单步实体识别后的文本检索能力，VisSearch-Bench 聚焦的长程跨模态视觉上下文管理是此前评估覆盖较少的维度，但具体任务设计、难度梯度及对现有模型的区分效果尚未公开。

**「可关注」** 现有视觉搜索类智能体评估多聚焦单步实体识别，VisSearch-Bench 针对长程跨模态视觉上下文管理能力设计测试集，可补充当前评估维度的不足。

**标签**: `#eval`, `#memory`

---

<a id="item-agent-engineer-6"></a>
### [NousResearch 发布 Arete-27B 微调模型](https://www.reddit.com/r/LocalLLaMA/comments/1xpmj33/nousresearcharete27b_hugging_face_qwen_finetune/) ⭐️ 6.0/10

2026 年 11 月 6 日 Reddit 用户转发 NousResearch 官方发布的 Arete-27B，该模型为基于阿里 Qwen3.8-27B 的监督微调（SFT）版本，未使用强化学习、偏好优化或架构修改，训练数据为纯文本，上下文长度 64k，针对言论自由、意识形态等 7 个价值类别调整价值取向。官方自评显示模型事实得分从 2.32 提升至 2.98（满分 5），含宣传内容的回答占比从 22%降至 0.9%，称通用能力与智能体基准无显著回退，已发布 GGUF 格式版本，官方博客的评估链接当前失效，暂无第三方验证相关声明。

reddit · r/LocalLLaMA · /u/jacek2023 · 11月6日 19:58

**「为什么重要」** 该模型面向通用辅助与智能体场景，若自评基准结果可复现，可为需要特定价值取向的编码智能体提供新的基座选择，但目前无第三方验证，相关性能结论需交叉官方材料确认。

**「可关注」** 可关注：该模型仅通过 SFT 完成价值对齐，未引入 RL 或架构修改，若基准结果可复现，可作为轻量价值对齐方案的参考样本。

**标签**: `#coding-agent`, `#eval`

---

## AI 日报
{: #sec-ai-daily .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-daily" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-daily-1"></a>
### [OpenAI 与 Hacktron 合作开展漏洞测试](https://openai.com/index/partnering-with-hacktron) ⭐️ 7.8/10

OpenAI 宣布与安全厂商 Hacktron 达成合作，核心任务包括排查自身系统安全漏洞、测试第三方服务连接链路、强化前沿 AI 系统的防御能力。

rss · OpenAI Blog · 11月6日 08:00

**「为什么重要」** 这是前沿 AI 实验室公开安全合作动作的典型案例，为行业 AI 系统安全运营提供了可参考的实践样本。

**「可关注」** 可关注：前沿 AI 系统的第三方服务连接安全与公开漏洞测试的合作模式。

**标签**: `#lab`, `#industry`, `#policy`

---

<a id="item-ai-daily-2"></a>
### [GitHub 发布智能体工程开发者指南](https://github.blog/ai-and-ml/github-copilot/beyond-code-generation-a-developers-guide-to-agentic-engineering/) ⭐️ 6.8/10

2026 年 11 月 6 日 GitHub 官方博客发布面向开发者的智能体工程指南，梳理覆盖规划、构建、验证、观测全流程的智能体工程工作流。关键数据：2026 年 10 月 GitHub 单周提交量达 12 亿次，同比提升 400%，超过 2025 年全年提交总量；Faros AI 研究显示团队 AI 采用率从低到高时，PR 平均审查时长增加 441%。该指南为指导性内容，并非模型发布、政策变更或正式产品公告。

rss · GitHub Blog · 11月6日 22:15

**「为什么重要」** 当前 AI 编码工具普及但开发者效率感知未同步提升，PR 审查耗时激增已成为行业普遍痛点，该指南回应了软件开发从纯代码生成向全流程智能体协作转型的实际需求。

**「可关注」** 可关注：GitHub Copilot 已落地跨设备会话 continuity、云沙箱任务运行、仓库级共享记忆、企业级托管配置等能力，覆盖规划到观测的全开发流程。

**标签**: `#lab`, `#industry`, `#product`

---

## AI 羊毛
{: #sec-ai-deals .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-deals" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-deals-1"></a>
### [本周 Epic 免费游戏 11.6~11.12](https://www.appinn.com/eggs-261106/) ⭐️ 8.0/10

你看到的内容可能由第三方 AI 基于小众软件文章提炼总结而成，可能与原文真实意图存在偏差。不代表小众软件观点和立场。请&lt;a href=&quot;https://www.appinn.com/eggs-261106/&quot; target=&quot;\_blank&quot;&gt;点击链接阅读原文&lt;/a&gt;细致比对和校验。&lt;br /&gt;&lt;br /&gt;本周（11.6~11.12）Epic 平台推出 3 款游戏相关福利：电脑端可免费领取《浮游世界/Flotsam》完整版，手机端可免费领取《巴别塔圣歌/Chants of Sennaar》的 Android 和 iOS 版本；《遗忘国度：放置勇士/Idle Champions of the Forgotten Realms》本体长期免费，本周登录 Epic 版本可领取限时 Morte’s Renown Pack 礼包，内含 5 名角色、每名角色 32 个白金宝箱及药水、专属魔宠。领取条件为登录对应平台 Epic 账号操作，《巴别塔圣歌》存在锁区限制，材料未明确具体截止时间。

rss · 小众软件 · 11月6日 08:21

**「为什么重要」** 本周福利覆盖 PC 与移动端，包含两款完整免费游戏及一款高口碑放置游戏的限时登录礼包，无需额外付费即可获取，适合不同平台的游戏玩家领取。

**「可关注」** 可关注：《巴别塔圣歌》手机版为 Epic 限免，锁区用户需确认自身地区是否可领取；《遗忘国度：放置勇士》的限时礼包需登录 Epic 版本游戏内领取，其他平台版本无法获取。

**标签**: `#limited-free`, `#promo`, `#game`

---