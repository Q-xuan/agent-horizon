---
layout: default
title: "Horizon Summary: 2026-09-11 (ZH)"
date: 2026-09-11
lang: zh
---

> 从 178 条内容中筛选出 18 条重要资讯。

---

**Harness 架构**
1. [Codex python-v0.154.0 发布](#item-harness-arch-1) ⭐️ 7.8/10
2. [ADK Python v2.9.0 发布](#item-harness-arch-2) ⭐️ 7.8/10
3. [openai/openai-agents-js v0.18.0 发布](#item-harness-arch-3) ⭐️ 7.8/10
4. [Claude Code v2.1.268 发布](#item-harness-arch-4) ⭐️ 6.8/10
5. [agent-framework python-1.18.0 发布](#item-harness-arch-5) ⭐️ 6.8/10
6. [E2B e2b@2.49.1 发布](#item-harness-arch-6) ⭐️ 6.8/10
7. [Cline desktop-v0.0.25 发布](#item-harness-arch-7) ⭐️ 5.8/10

**Agent 工程师日报**
1. [OpenAI Agents API 发布](#item-agent-engineer-1) ⭐️ 8.0/10
2. [Datasette 1.0a39 发布](#item-agent-engineer-2) ⭐️ 7.8/10
3. [SWE-2 发布：推 Pareto 前沿](#item-agent-engineer-3) ⭐️ 7.8/10
4. [Anthropic 2026 9 月滥用报告](#item-agent-engineer-4) ⭐️ 7.0/10
5. [Shopify 回归原生移动开发](#item-agent-engineer-5) ⭐️ 7.0/10

**AI 日报**
1. [Codex ChatGPT 搜索新型抗菌分子](#item-ai-daily-1) ⭐️ 6.8/10
2. [OpenAI Data agent 发布](#item-ai-daily-2) ⭐️ 6.8/10
3. [ChatGPT 金融服务 发布](#item-ai-daily-3) ⭐️ 6.8/10
4. [OpenAI GSA 合作 政府 AI 访问](#item-ai-daily-4) ⭐️ 6.8/10
5. [DeepSeek V4.1 Flash 发布](#item-ai-daily-5) ⭐️ 6.8/10

**AI 羊毛**
1. [Modeinspect 99 天免费 AI 积分](#item-ai-deals-1) ⭐️ 7.0/10

---

## Harness 架构

<a id="item-harness-arch-1"></a>
### [Codex python-v0.154.0 发布](https://github.com/openai/codex/releases/tag/python-v0.154.0) ⭐️ 7.8/10

OpenAI Codex Python SDK v0.154.0 发布。新增 max 和 ultra 推理努力值。支持在同步和异步 run\(\) 和 turn\(\) 调用中添加 ExternalMessage。新增 resume/fork 的 include\_turns、turn\_service\_tier 和 source 元数据，并刷新生成协议模型。

github · aibrahim-oai · 9月10日 19:51

**「改了什么」** 新增 max 和 ultra 推理努力值，并在 run\(\) 和 turn\(\) 调用中添加 ExternalMessage 支持。新增 resume/fork 的 include\_turns、turn\_service\_tier 和 source 元数据，并刷新协议模型。

**标签**: `#runtime`, `#tools`, `#memory`, `#planning`

---

<a id="item-harness-arch-2"></a>
### [ADK Python v2.9.0 发布](https://github.com/google/adk-python/releases/tag/v2.9.0) ⭐️ 7.8/10

Google ADK Python v2.9.0 发布。该版本通过自动模型故障转移提升代理可用性，支持 LiveKit 语音和电话代理。同时允许从 YAML 配置加载 ADK 2.0 图工作流，并兼容 MCP SDK 2.x。

github · GWeale · 9月10日 21:22

**「改了什么」** 新增 FallbackModel 实现自动模型故障转移。添加 LiveKit runner 支持语音和电话代理。允许从 YAML 配置加载 ADK 2.0 图工作流。同时兼容 MCP SDK 2.x。

**标签**: `#runtime`, `#mcp`, `#planning`

---

<a id="item-harness-arch-3"></a>
### [openai/openai-agents-js v0.18.0 发布](https://github.com/openai/openai-agents-js/releases/tag/v0.18.0) ⭐️ 7.8/10

openai/openai-agents-js v0.18.0 发布。Docker 文件 API 迁移至容器内运行，应用需兼容容器镜像、GNU 工具和文件权限。编辑器文件大小限制为 10 MiB。新增可选 UnixLocalSandboxClient 文件 I/O 保护。

github · seratch · 9月10日 21:23

**「设计要点」** Docker 文件 API 运行于容器内，需兼容容器镜像和文件权限。fileIOProtection 模式决定文件 I/O 后端。

**「改了什么」** Docker 文件 API 迁移至容器运行，新增 fileIOProtection 参数。

**标签**: `#runtime`, `#sandbox`, `#tools`, `#permissions`

---

<a id="item-harness-arch-4"></a>
### [Claude Code v2.1.268 发布](https://github.com/anthropics/claude-code/releases/tag/v2.1.268) ⭐️ 6.8/10

Claude Code v2.1.268 发布。系统添加了网关定价对齐功能，通过 gateway.yaml 中的 pricing 设置让已签名的 Claude Code 客户端获得相同费率。还添加了自托管运行器会话状态移除命令、插件 JSON 输出支持，以及内部网络允许列表。

github · ashwin-ant · 9月10日 20:30

**「改了什么」** Claude Code v2.1.268 相比上一版，添加了网关定价对齐、自托管运行器会话状态移除、插件 JSON 输出增强、认证配置暴露和内部网络允许列表。

**标签**: `#gateway`, `#runtime`, `#tools`, `#permissions`, `#auth`

---

<a id="item-harness-arch-5"></a>
### [agent-framework python-1.18.0 发布](https://github.com/microsoft/agent-framework/releases/tag/python-1.18.0) ⭐️ 6.8/10

agent-framework Python 1.18.0 发布。该版本新增了共享向量存储支持，包括向量存储抽象、便携过滤器和多种向量存储实现。运行时工具调用循环添加了最大持续时间限制和停止原因信号。还支持混合工作流调用关键字参数。

github · moonbox3 · 9月10日 09:23

**「设计要点」** 新增共享向量存储抽象，支持便携过滤器和多种向量存储后端实现。工具调用循环添加了最大持续时间界限和停止原因信号。

**「改了什么」** agent-framework Python 1.18.0 引入了共享向量存储抽象和工具调用循环的最大持续时间限制。

**标签**: `#memory`, `#runtime`, `#tools`

---

<a id="item-harness-arch-6"></a>
### [E2B e2b@2.49.1 发布](https://github.com/e2b-dev/E2B/releases/tag/e2b%402.49.1) ⭐️ 6.8/10

E2B 发布 \`e2b@2.49.1\`。\`Sandbox.create\` 生命周期选项与 \`Sandbox.connect\` 的 \`onResume\` 在要求 API key 前拒绝非法值，对齐 Python SDK。\`onResume\` / \`on\_resume\` 依赖认识该选项的控制面：旧版自托管或 BYOC 会丢掉 \`memory\` 字段，仍恢复内存并报成功，而不是拒绝请求。控制面 HTTP 遇 429 最多重试 3 次，按服务端 \`Retry-After\` 的 delta-seconds 等待，可用 \`retries\` 配置或关闭；等待将耗尽请求超时时停止，Envd（含文件系统）和 volume-content 请求不重试。

github · github-actions\[bot\] · 9月10日 17:37

**「设计要点」** \`onResume\` 的 \`memory\` 由控制面解释：旧版自托管或 BYOC 不认识该选项时会丢掉字段，照常恢复内存并返回成功。429 重试只打控制面 HTTP，Envd（含文件系统）和 volume-content 不重试。

**「改了什么」** 创建与连接选项改为在要求 API key 前拒绝非法值。控制面 HTTP 遇 429 最多重试 3 次，按 \`Retry-After\` 等待，可用 \`retries\` 配置或关闭。

**标签**: `#sandbox`, `#memory`, `#runtime`

---

<a id="item-harness-arch-7"></a>
### [Cline desktop-v0.0.25 发布](https://github.com/cline/cline/releases/tag/desktop-v0.0.25) ⭐️ 5.8/10

Cline desktop v0.0.25 发布。ChatGPT Codex 模型选择器现在只列出你的计划实际可用的模型，修复了上下文限制。Windows 安装程序修复了 sidecar 守护进程冲突问题。提示在发送失败前不再丢失。

github · github-actions\[bot\] · 9月10日 04:57

**「改了什么」** 相比上一版，ChatGPT Codex 模型选择器限制匹配 backend 实际可用模型。Windows 安装程序停止 sidecar 守护进程以避免冲突。

**标签**: `#runtime`, `#tools`, `#permissions`

---

## Agent 工程师日报

<a id="item-agent-engineer-1"></a>
### [OpenAI Agents API 发布](https://developers.openai.com/api/docs/guides/agents-api/overview) ⭐️ 8.0/10

OpenAI 发布了 Agents API，用于托管、集成工具的代理，并在不同环境中保持状态。该 API 允许开发者构建和管理代理，集成各种工具并跨环境持久化状态。这影响了代理编排和工具集成领域的开发者。

hackernews · aquir · 9月10日 19:43 · [社区讨论](https://news.ycombinator.com/item?id=49649213)

**「为什么重要」** OpenAI Agents API 的发布是已发生的变化，为代理提供了托管服务。HN 讨论了 agent abstractions、harnesses 和 managed compute services，这对 orchestration 和工具集成领域有潜在价值，但影响尚未证实。

**「可关注」** 可关注：支持自托管沙箱。

**「评论」** 社区认为该 API 解决了构建 harness 的难题，支持跨环境状态持久化，但仍需探索最佳抽象。有人提到自托管沙箱选项可降低锁定风险。

**标签**: `#harness`, `#orchestration`, `#agents`, `#API`, `#managed-services`

---

<a id="item-agent-engineer-2"></a>
### [Datasette 1.0a39 发布](https://github.com/simonw/datasette/releases/tag/1.0a39) ⭐️ 7.8/10

Simon Willison 在 simonw/datasette 发布了 Datasette 1.0a39 alpha 版本，包含安全更新。这些更新修改了表和视图的权限检查，并从 0.65.4 版本回溯修复。关键细节包括权限解析考虑 SQLite 不区分大小写名称、默认拒绝 sqlite\_stat\* 表、视图表权限检查、外键 API 尊重 view-table 权限，以及行端点在解析主键前检查权限。此版本影响使用 Datasette 的数据工具链和安全配置的用户。

github · simonw · 9月11日 00:05

**「为什么重要」** 此安全更新修改了权限检查逻辑，已发生的变化影响依赖 Datasette 进行数据访问控制的用户。

**「可关注」** 可关注：表和视图权限检查现在考虑 SQLite 不区分大小写名称。

**标签**: `#permissions`, `#eval`, `#harness`, `#toolchain`, `#security`

---

<a id="item-agent-engineer-3"></a>
### [SWE-2 发布：推 Pareto 前沿](https://cognition.ai/blog/swe-2) ⭐️ 7.8/10

Cognition 推出 SWE-2 编码模型，在 FrontierCode 1.1 Main 达到 50.0% 分数，接近 Fable 5.1 的 50.9%，成本降低 64%。该模型首次将 RL 扩展到多万亿参数规模，通过单次运行训练所有 reasoning-effort 级别。SWE-2 基于 Kimi K33 2.8T 参数模型 post-training 而来，已在 Devin Desktop、CLI、Web 和 Fusion 中可用。

rss · Cognition Blog · 9月10日 17:00

**「为什么重要」** SWE-2 接近 frontier 性能且成本大幅降低，这对 coding agent 的 eval 和工作流有直接影响。尚未证实其在实际部署中的长期影响。

**「可关注」** 可关注：SWE-2 使用 Pareto-informed cost penalties 在单次 RL run 中训练所有 reasoning-effort 级别，优化了 cost–performance tradeoffs。

**标签**: `#coding-agent`, `#eval`, `#RL`, `#orchestration`

---

<a id="item-agent-engineer-4"></a>
### [Anthropic 2026 9 月滥用报告](https://www.anthropic.com/threat-intelligence-report-september-2026) ⭐️ 7.0/10

Anthropic 发布了 2026 年 9 月的 AI 滥用检测报告。该报告披露了 Moonshot AI 公司将 Kimi 模型用户请求转发给 Claude 的情况，DeepSeek 也同样将用户交换转发至 Claude，MiniMax 通过壳公司构建了代理网络服务。报告还讨论了生物武器滥用的潜在风险。

hackernews · garo-pro · 9月10日 17:23 · [社区讨论](https://news.ycombinator.com/item?id=49647300)

**「为什么重要」** 该报告为 AI 代理安全评估提供了具体案例和技术细节，对模型编排的安全性有参考价值。报告中披露的代理转发机制可能影响模型使用安全，但生物武器滥用等影响尚未得到证实。

**「可关注」** 可关注：Moonshot AI 和 DeepSeek 未经用户同意转发请求至 Claude 的行为暴露了代理机制的潜在安全漏洞。

**「评论」** 社区讨论焦点集中在代理转发和生物武器滥用的严重性上。部分用户指出在威胁行为者识别上存在双标现象。

**标签**: `#eval`, `#harness`, `#orchestration`

---

<a id="item-agent-engineer-5"></a>
### [Shopify 回归原生移动开发](https://simonwillison.net/2026/Sep/10/shopify-react-native/) ⭐️ 7.0/10

Shopify 决定从 React Native 切换回独立的 Swift 和 Kotlin 原生代码库。
这一变化源于 AI 代理已能完成大部分实现、翻译、测试和审查工作，使双平台维护不再是主要成本。
Shopify 维护的 react-native-skia 和 flash-list 库将寻找新归宿，restyle 将于 2026 年底归档。

rss · Simon Willison · 9月10日 21:11

**「为什么重要」** 这一转变凸显了 AI 代理在弥合跨平台差距方面的成熟度。它将影响 Shopify 的移动开发流程，但具体影响仍待观察。

**「可关注」** 可关注：AI 代理能处理实现、翻译、测试和审查工作

**标签**: `#coding-agent`, `#orchestration`, `#eval`, `#harness`

---

## AI 日报

<a id="item-ai-daily-1"></a>
### [Codex ChatGPT 搜索新型抗菌分子](https://openai.com/index/using-codex-chatgpt-to-search-for-new-antimicrobials) ⭐️ 6.8/10

César de la Fuente 的实验室使用 Codex 和 ChatGPT 在活体和 extinct genomes 中搜索新型抗菌分子。这些分子针对药物耐药感染。研究者将 AI 工具应用于基因组搜索，以发现新的抗菌候选药物。

rss · OpenAI Blog · 9月10日 16:00

**「可关注」** 可关注：将 Codex 与 ChatGPT 应用于活体和 extinct genomes 的基因组搜索以发现抗菌分子。

**标签**: `#model`, `#lab`, `#industry`, `#product`

---

<a id="item-ai-daily-2"></a>
### [OpenAI Data agent 发布](https://openai.com/index/put-data-to-work) ⭐️ 6.8/10

OpenAI 在 ChatGPT Work 中推出 Data agent。用户可以通过自然语言连接公司数据，发现洞见，并构建交互式仪表盘。

rss · OpenAI Blog · 9月10日 15:00

**「可关注」** 可关注：使用自然语言连接公司数据并构建交互式仪表盘。

**标签**: `#lab`, `#product`, `#industry`

---

<a id="item-ai-daily-3"></a>
### [ChatGPT 金融服务 发布](https://openai.com/index/introducing-chatgpt-financial-services) ⭐️ 6.8/10

OpenAI 发布 ChatGPT 金融服务版，结合内置金融数据和 GPT-6 Astra，支持研究、建模和生成客户就绪材料。该版本针对金融行业优化数据整合。公告简短，未提供详细实现细节。

rss · OpenAI Blog · 9月10日 07:00

**「为什么重要」** 金融服务领域对数据准确性和合规材料生成要求严格，此版本整合内置数据支持相关工作。

**「可关注」** 可关注：GPT-6 Astra 整合研究建模和客户就绪材料生成。

**标签**: `#model`, `#lab`, `#industry`, `#product`

---

<a id="item-ai-daily-4"></a>
### [OpenAI GSA 合作 政府 AI 访问](https://openai.com/index/expanding-ai-access-us-government) ⭐️ 6.8/10

OpenAI 与 GSA 合作，为符合条件的联邦、州、县、市和部落政府提供 AI 访问。这些政府可获得 0 元授权费、50% 使用费折扣，并获得扩展的网络安全防御支持。此举旨在扩大 AI 在政府领域的应用。

rss · OpenAI Blog · 9月10日 07:00

**「可关注」** 可关注：政府可获得 0 元授权费和 50% 使用费折扣。

**标签**: `#openai`, `#policy`, `#government`, `#product`, `#industry`

---

<a id="item-ai-daily-5"></a>
### [DeepSeek V4.1 Flash 发布](https://mp.weixin.qq.com/s?__biz=Mzk0OTYwNzc3NQ==&amp;mid=2247485817&amp;idx=1&amp;sn=627dd80114901f3fd8717e2c13feaf6a) ⭐️ 6.8/10

DeepSeek 发布 V4.1 Flash，原生多模态全新基座模型。模型被描述为更强、更快、更普惠。官方微信公告未提供具体参数或性能数据。

rss · DeepSeek · 9月10日 05:44

**「可关注」** 可关注：原生多模态，全新基座模型。

**标签**: `#model`, `#lab`, `#product`

---

## AI 羊毛

<a id="item-ai-deals-1"></a>
### [Modeinspect 99 天免费 AI 积分](https://www.producthunt.com/products/modeinspect-1-0) ⭐️ 7.0/10

Modeinspect 提供 99 天免费 AI 积分，用于在代码库中设计产品 UI。
用户通过其工具设计 UI 来领取这些积分。
领取条件是设计产品 UI 在代码库中，截止时间未在材料中提及。

rss · Product Hunt · 9月10日 03:31

**标签**: `#credits`, `#promo`, `#free-tier`, `#api`

---