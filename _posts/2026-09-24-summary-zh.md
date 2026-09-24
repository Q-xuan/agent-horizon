---
layout: default
title: "Horizon Summary: 2026-09-24 (ZH)"
date: 2026-09-24
lang: zh
---

> 从 220 条内容中筛选出 17 条重要资讯。

---

**Harness 架构**
1. [Claude Code v2.1.281 发布](#item-harness-arch-1) ⭐️ 8.8/10
2. [Mastra 1.68.0 发布：MCP v2 与向量库扩展](#item-harness-arch-2) ⭐️ 8.8/10
3. [modelcontextprotocol/typescript-sdk released @modelcontextprotocol/node@2.1.0](#item-harness-arch-3) ⭐️ 8.8/10
4. [block/goose released v1.52.0](#item-harness-arch-4) ⭐️ 7.8/10
5. [mem0 v2.2.0 发布：新增用户画像记忆](#item-harness-arch-5) ⭐️ 7.3/10
6. [Improved token efficiency for longer agent runs](#item-harness-arch-6) ⭐️ 7.3/10
7. [fastmcp v4.0.6 修复会话泄漏与资源匹配](#item-harness-arch-7) ⭐️ 6.8/10

**Agent 工程师日报**
1. [Advancing Private AI Compute with secure, server-side memory](#item-agent-engineer-1) ⭐️ 6.3/10

**AI 日报**
1. [OpenAI 扩展 Daybreak 至乌克兰](#item-ai-daily-1) ⭐️ 8.8/10
2. [OpenAI 发布心理健康评测基准](#item-ai-daily-2) ⭐️ 8.8/10
3. [GitHub Copilot 渲染百万行 PR](#item-ai-daily-3) ⭐️ 7.8/10
4. [Sam Altman’s remarks at the United Nations Security Council](#item-ai-daily-4) ⭐️ 6.8/10
5. [Ringg 基于 GPT-5.6 解决 65% 客服来电](#item-ai-daily-5) ⭐️ 6.8/10
6. [GitHub 调研：开发者呼吁减少算力浪费](#item-ai-daily-6) ⭐️ 6.8/10
7. [Bringing Private Processing to Meta AI Glasses](#item-ai-daily-7) ⭐️ 6.8/10
8. [OpenAI Academy 成立两周年](#item-ai-daily-8) ⭐️ 6.3/10

**AI 创作者雷达**
1. [Simon Willison 提及 Gemini 3.8 TTS 支持多声音对话与克隆](#item-ai-creator-1) ⭐️ 0.0/10

---

## Harness 架构

<a id="item-harness-arch-1"></a>
### [Claude Code v2.1.281 发布](https://github.com/anthropics/claude-code/releases/tag/v2.1.281) ⭐️ 8.8/10

Claude Code v2.1.281 发布，扩展 Claude apps gateway 的策略与上游控制。新增 desktop 策略块与 Bedrock upstreams 的 assume\_role、guardrail 配置，支持跨 AWS 账户调用、应用 Amazon Bedrock guardrail 及按开发者隔离会话；settings.json 增加 &quot;attribution&quot;: false 隐藏 commit 和 PR 归属。MCP 侧支持 2026-07-28 协议的 URL-mode elicitation，服务器可请求打开浏览器流程。另修复会话恢复、提示缓存、代理流截断及沙箱匹配等大量问题。

github · ashwin-ant · 9月23日 19:19

**「设计要点」** gateway 通过 STS 承担 IAM 角色访问 Bedrock，支持跨账户与按开发者隔离会话；telemetry.resource\_attributes 为 Claude Desktop 和 /login 会话注入固定标签。权限模型收紧：命令替换产生的 recursive rm 即使匹配 Bash allow rule 也会提示，需显式设置 CLAUDE\_CODE\_DISABLE\_SUBSTITUTION\_RM\_PROMPT=1 才能跳过。

**「改了什么」** 新增 gateway desktop 策略块、Bedrock assume\_role 与 guardrail、MCP URL-mode elicitation、plugin validate 的 MCP 检查及 settings.json 的 attribution 开关；修复恢复会话历史错乱、代理丢流导致的内容块缺失、沙箱 excludedCommands 匹配失败等问题。

**标签**: `#runtime`, `#mcp`, `#permissions`, `#sandbox`

---

<a id="item-harness-arch-2"></a>
### [Mastra 1.68.0 发布：MCP v2 与向量库扩展](https://github.com/mastra-ai/mastra/releases/tag/%40mastra/core%401.68.0) ⭐️ 8.8/10

Mastra 1.68.0 发布，核心包 @mastra/core 升级至 1.68.0。最大变化是 @mastra/mcp@2.0.0 基于 MCP 2026-07-28 协议重写，移除 initialize 握手与会话头，工具需要输入时改用 context.suspend\(\)/context.resumeData 挂起与恢复，服务端路由显式返回 \{ status: &\#x27;suspended&\#x27;, suspendPayload, resumeSchema \} 或 \{ status: &\#x27;completed&\#x27;, output \}。同时新增 Azure AI Search 与 Weaviate 两个 MastraVector 后端，可观测性查询支持分页、字段发现与增量轮询。

github · Patrycja-J · 9月23日 08:40

**「设计要点」** MCP v2 用签名且自包含的 requestState 承载续跑状态，替代旧 elicitation 接口；durable agent 默认不再持久化 running 检查点，仅在 recovery.durableAgents: &\#x27;auto&\#x27; 或自定义 shouldPersistSnapshot 时写入，减少常规运行的存储写入。Memory 新增 messageHistory: \{ maxTokens, atMaxRemoveTokens? \}，按 token 预算丢弃最旧消息并持久化裁剪边界。

**「改了什么」** 相对旧版，Agent Controller 流消息改为一次完整 message\_start 后按 ID 发送 message\_update 增量，message\_end 仅含消息 ID；@mastra/mcp@2.0.0 为破坏性重写，仅支持 MCP 2026-07-28，移除部分传输与协议表面。Trace 查询新增 page 分页与 root-span 摘要字段，数据集与实验列表支持 orderBy 服务端排序。

**标签**: `#mcp`, `#runtime`, `#tools`, `#memory`, `#eval`

---

<a id="item-harness-arch-3"></a>
### [modelcontextprotocol/typescript-sdk released @modelcontextprotocol/node@2.1.0](https://github.com/modelcontextprotocol/typescript-sdk/releases/tag/%40modelcontextprotocol/node%402.1.0) ⭐️ 8.8/10

MCP TypeScript SDK v2.1.0 introduces request-time OAuth scope challenges for tools, resources, and prompts, enforcing insufficient\_scope via HTTP 403 preflight.

github · github-actions\[bot\] · 9月23日 15:43

**标签**: `#mcp`, `#permissions`, `#tools`

---

<a id="item-harness-arch-4"></a>
### [block/goose released v1.52.0](https://github.com/aaif-goose/goose/releases/tag/v1.52.0) ⭐️ 7.8/10

Goose v1.52.0 adds live voice conversations, new provider implementations, recipe parameter limits, and support for additional models.

github · github-actions\[bot\] · 9月23日 14:59

**标签**: `#runtime`, `#tools`, `#planning`, `#permissions`

---

<a id="item-harness-arch-5"></a>
### [mem0 v2.2.0 发布：新增用户画像记忆](https://github.com/mem0ai/mem0/releases/tag/v2.2.0) ⭐️ 7.3/10

mem0 v2.2.0 发布。MemoryClient 与 AsyncMemoryClient 新增 User Profiles，按项目配置 JSON Schema，由 LLM 从用户记忆生成结构化、始终最新的 JSON 摘要。生成异步执行，每个 job POST 携带 Idempotency-Key；重试时传入相同 idempotency\_key 可避免启动第二个任务。另修复 Valkey vector store 中 None 时间戳触发的 TypeError。

github · kartik-mem0 · 9月23日 19:03

**「设计要点」** 记忆层引入 schema 驱动的用户画像抽象，LLM 填充、异步生成，通过幂等键保证任务重试安全。向量存储侧统一 None 时间戳处理，与 Redis provider 行为对齐。

**「改了什么」** 新增 get\_profile、generate\_profile、get\_profile\_settings、update\_profile\_settings、sample\_profiles、get\_profile\_job 六个接口。异步任务支持 Idempotency-Key 重试保护。Valkey vector store 的 insert 与 update 路径改用 .get\(\) 加真值检查，None 时间戳回落默认值。

**标签**: `#memory`, `#runtime`, `#tools`

---

<a id="item-harness-arch-6"></a>
### [Improved token efficiency for longer agent runs](https://cursor.com/blog/improved-token-efficiency) ⭐️ 7.3/10

Cursor details harness optimizations that cut token costs by 7% via improved context assembly, system prompt trimming, and agent work division.

rss · Cursor Blog · 9月23日 12:00

**标签**: `#runtime`, `#memory`, `#tools`, `#mcp`, `#subagents`

---

<a id="item-harness-arch-7"></a>
### [fastmcp v4.0.6 修复会话泄漏与资源匹配](https://github.com/PrefectHQ/fastmcp/releases/tag/v4.0.6) ⭐️ 6.8/10

fastmcp v4.0.6 发布，修补 Client 退出取消时的 session 泄漏，并让资源模板匹配客户端实际发送的 raw 或 percent-encoded 字面量，以及 exploded 或 comma-joined 列表查询参数。completion 不再返回调用者不可见的 prompt 与 template。JSON schema 遇到 float 或超大 length 限制时正常加载。auth 侧缓存 OIDC discovery，并将 Google access token 移出 request URL。

github · zzstoatzz · 9月23日 18:54

**「设计要点」** Client 在 context 退出、任何 await 之前释放 session hold；未共享的 stdio subprocess 在 session 因取消退出时终止。资源模板按 RFC 6570 §3.1 处理 percent-encoding，completion 可见性与 list 接口对齐。

**「改了什么」** 相对 v4.0.5，修复 session 泄漏、资源模板匹配、completion 可见性、JSON schema 加载及 OIDC/Google auth token 处理；新增实验性 JevSearchTransform、CodeMode 嵌套 schema 字段命名，并暴露 FileSystemProvider 发现失败。

**标签**: `#runtime`, `#tools`, `#mcp`, `#permissions`

---

## Agent 工程师日报

<a id="item-agent-engineer-1"></a>
### [Advancing Private AI Compute with secure, server-side memory](https://deepmind.google/blog/advancing-private-ai-compute-with-secure-server-side-memory/) ⭐️ 6.3/10

Google DeepMind announces private, server-side memory for its Private AI Compute platform.

rss · Google DeepMind · 9月23日 16:00

**标签**: `#memory`, `#security`, `#infrastructure`

---

## AI 日报

<a id="item-ai-daily-1"></a>
### [OpenAI 扩展 Daybreak 至乌克兰](https://openai.com/index/openai-extends-cyber-access-to-ukraine-for-civilian-defense) ⭐️ 8.8/10

OpenAI 宣布将 Daybreak 项目的访问权限扩展至乌克兰政府，用于支持民用基础设施的网络防御。该公告由 OpenAI 官方发布，属于政策层面的具体行动，而非模型发布。材料未披露技术细节、覆盖范围或时间表。

rss · OpenAI Blog · 9月23日 13:00

**「可关注」** 可关注：OpenAI 的 Daybreak 项目现已覆盖乌克兰政府的民用基础设施网络防御场景，但具体技术接口与部署方式尚未公开。

**标签**: `#policy`, `#lab`, `#industry`

---

<a id="item-ai-daily-2"></a>
### [OpenAI 发布心理健康评测基准](https://openai.com/index/introducing-mentalhealthbench) ⭐️ 8.8/10

OpenAI 发布 MentalHealthBench。该基准由专家参与构建，评估 AI 在真实心理健康对话中的有用性与安全性。官方暂未披露更多技术细节。

rss · OpenAI Blog · 9月23日 10:00

**「为什么重要」** 心理健康对话对模型安全边界要求极高。该基准提供专家参与的评估框架，用于衡量有用性与安全性。

**「可关注」** 可关注：专家如何参与界定心理健康场景中的安全与有用边界。

**标签**: `#lab`, `#eval`, `#product`

---

<a id="item-ai-daily-3"></a>
### [GitHub Copilot 渲染百万行 PR](https://github.blog/engineering/user-experience/rendering-huge-pull-requests-in-the-github-copilot-app/) ⭐️ 7.8/10

GitHub 工程博客介绍，Copilot app 重构 diff 渲染层，以打开百万行 pull request，并显示数百条内联评审评论。作者 Alberto Gimeno 撰文说明重建思路。原文未给出具体性能指标或实现细节。

rss · GitHub Blog · 9月23日 18:29

**「可关注」** 可关注：GitHub 将 diff 表面重建为可承载百万行变更与数百条内联评论的渲染层，具体优化手段待原文细节披露。

**标签**: `#product`, `#engineering`, `#industry`

---

<a id="item-ai-daily-4"></a>
### [Sam Altman’s remarks at the United Nations Security Council](https://openai.com/index/sam-altman-un-security-council-remarks) ⭐️ 6.8/10

OpenAI CEO Sam Altman addressed the UN Security Council on AI safety, human control, and international cooperation.

rss · OpenAI Blog · 9月23日 12:00

**标签**: `#lab`, `#policy`, `#industry`

---

<a id="item-ai-daily-5"></a>
### [Ringg 基于 GPT-5.6 解决 65% 客服来电](https://openai.com/index/ringg) ⭐️ 6.8/10

OpenAI 官方博客披露，Ringg 使用 GPT-5.6 驱动多语言客服智能体，覆盖语音、聊天、WhatsApp 和网页，可解决至多 65% 的客户来电，成本较 GPT-4.1 降低 90%。该数据来自第一方案例研究，非模型发布或政策变更。

rss · OpenAI Blog · 9月23日 12:00

**「为什么重要」** 这是 GPT-5.6 在真实生产环境的量化案例：多语言、多渠道并行，同时实现高自动解决率与大幅降本，显示模型已能支撑复杂客服流程的端到端自动化。

**「可关注」** 可关注：在客服场景中，GPT-5.6 相比 GPT-4.1 将成本压低 90%，并保持至多 65% 的来电自动解决率，可作为构建高并发自动化 Agent 的成本与能力参考基线。

**标签**: `#model`, `#product`, `#industry`, `#eval`

---

<a id="item-ai-daily-6"></a>
### [GitHub 调研：开发者呼吁减少算力浪费](https://github.blog/news-insights/research/developers-want-more-efficient-software-heres-what-over-1000-github-users-told-us-they-need/) ⭐️ 6.8/10

GitHub 联合 Yale Program on Climate Change Communication 发布调研，覆盖超过 1000 名 GitHub 用户。核心发现是：开发者对减少浪费算力的工具、测量方法和实践指导有强烈需求。该内容属于研究报告，不是产品或模型更新。

rss · GitHub Blog · 9月23日 13:00

**「为什么重要」** 超过 1000 名 GitHub 用户表达了对效率工具、测量和实践指导的需求，说明减少浪费算力已是开发者关心的具体问题。

**「可关注」** 可关注：调研指出，开发者需要「减少浪费算力」的工具、测量和实践指导，这是来自 1000 多名 GitHub 用户的直接反馈。

**标签**: `#industry`, `#research`, `#product`

---

<a id="item-ai-daily-7"></a>
### [Bringing Private Processing to Meta AI Glasses](https://engineering.fb.com/2026/09/23/security/private-processing-meta-ai-glasses/) ⭐️ 6.8/10

Meta Engineering announces private processing for AI glasses, but the provided excerpt is too truncated to evaluate concrete technical details or impact.

rss · Engineering at Meta · 9月24日 00:00

**标签**: `#product`, `#industry`, `#lab`

---

<a id="item-ai-daily-8"></a>
### [OpenAI Academy 成立两周年](https://openai.com/index/two-years-of-openai-academy) ⭐️ 6.3/10

OpenAI 官方博客发文纪念 OpenAI Academy 成立两周年，并称将继续把 AI 技能推广到更多社区。该更新为教育/社区项目里程碑，非模型发布或政策调整。

rss · OpenAI Blog · 9月23日 16:00

**「可关注」** 可关注：OpenAI Academy 成立两周年，官方称将把 AI 技能带到更多社区。

**标签**: `#lab`, `#industry`, `#product`

---

## AI 创作者雷达

<a id="item-ai-creator-1"></a>
### [Simon Willison 提及 Gemini 3.8 TTS 支持多声音对话与克隆](https://twitter.com/simonw/status/tweet-2102861892549279922) ⭐️ 0.0/10

2026 年 9 月 23 日，Simon Willison 在 Twitter 上提到新的 Gemini 3.8 TTS 模型，称其价格低廉，并支持在多个声音之间生成对话。据其描述，该模型提供 2000 多种预置声音，也支持用户克隆自己的声音。他表示为该模型搭建了一个简单界面，并用 Claude 生成了一段由两只鹈鹕争论是否迁往 Pacifica Pier 的脚本来测试。目前这一信息仅来自单一社交媒体帖子，缺乏官方文档、具体定价和版本细节确认。

twitter · Simon Willison · 9月23日 20:45

**「为何现在值得注意」** Simon Willison 以开发者身份分享了实际搭建界面和生成对话的体验，显示多声音对话与声音克隆可能正在成为 TTS 工具的新功能方向；但这些能力、成本及“Gemini 3.8”这一版本号目前均未得到官方确认，其行业影响仍有待验证。

**「内容切入角度」** 可做角度：以“一条推文能告诉我们多少关于 TTS 的未来”为线索，拆解 Simon Willison 提到的多声音对话、2000+ 预置声音和声音克隆功能，讨论若这些能力被官方证实且价格低廉，可能为播客、有声内容和短视频配音带来哪些变化，同时明确标注当前信息仅来自个人分享、尚待核实。

**标签**: `#Gemini TTS`, `#Text-to-Speech`, `#Voice Cloning`, `#Multi-voice Dialogue`, `#AI Content Creation`

---