---
layout: default
title: "Horizon Summary: 2026-08-27 (ZH)"
date: 2026-08-27
lang: zh
---

> 从 132 条内容中筛选出 11 条重要资讯。

---

**Harness 架构**
1. [Cline SDK v0.0.81 发布](#item-harness-arch-1) ⭐️ 7.5/10
2. [mastra/core 1.62.0 发布](#item-harness-arch-2) ⭐️ 7.5/10
3. [Codex rust-v0.150.0 发布](#item-harness-arch-3) ⭐️ 6.5/10
4. [Cline SDK v0.0.80 发布](#item-harness-arch-4) ⭐️ 6.5/10
5. [google/adk-python v2.8.0 发布](#item-harness-arch-5) ⭐️ 6.5/10
6. [Claude Code v2.1.247 发布](#item-harness-arch-6) ⭐️ 5.5/10
7. [Cline v4.1.16 发布](#item-harness-arch-7) ⭐️ 5.5/10

**Agent 工程师日报**
1. [Gemini 3.5 Transcribe 智能转录](#item-agent-engineer-1) ⭐️ 5.5/10
2. [Dolma 改编出泰语语料 Mangosteen](#item-agent-engineer-2) ⭐️ 5.5/10

**AI 日报**
1. [ChatGPT for Teachers 扩展至 55 学区](#item-ai-daily-1) ⭐️ 8.5/10
2. [OpenAI 报告：AI 让学习持续不断](#item-ai-daily-2) ⭐️ 6.5/10

---

## Harness 架构

<a id="item-harness-arch-1"></a>
### [Cline SDK v0.0.81 发布](https://github.com/cline/cline/releases/tag/sdk/sdk/v0.0.81) ⭐️ 7.5/10

Cline SDK v0.0.81 发布了。该版本优化了 session event payloads，将状态快照与对话转录分离。状态快照现在只包含状态、用量、模型、工作区和检查点，转录通过新的 session.messages 命令获取。这减少了大型任务的内存使用。

github · github-actions\[bot\] · 8月26日 09:38

**「改了什么」** 相对 v0.0.80 版，session.updated（以及 session.created / session.detached / run.started）事件不再嵌入完整的消息历史。每个事件现在是状态-only，减少了内存膨胀和事件日志问题。转录通过 session.messages 命令单独获取，检查点恢复回复不受影响。

**标签**: `#memory`, `#runtime`, `#protocol`

---

<a id="item-harness-arch-2"></a>
### [mastra/core 1.62.0 发布](https://github.com/mastra-ai/mastra/releases/tag/%40mastra/core%401.62.0) ⭐️ 7.5/10

mastra-ai/mastra 发布了 @mastra/core 1.62.0 版本。该版本新增了 ElasticsearchStore 和 Valkey/GLIDE 存储后端，支持从单个集群管理内存、工作流快照和语义召回。同时引入了 SandboxComputer 能力，支持截图、鼠标和键盘控制，以及 E2B/Daytona 桌面提供商。沙箱现在拥有自己的运行时环境，可通过 MastraSandbox\(\{ env \}\) 构造，并使用 getEnv\(\) 和 setEnv\(\) 方法在运行时管理环境。沙箱启动失败不再静默处理，并添加了可选的 find、connect 和 create 方法支持。

github · PaulieScanlon · 8月26日 13:40

**「改了什么」** 相对于上一版，@mastra/core 1.62.0 增加了可选集合行计数支持、分数查询元数据过滤以及 AgentController.generateThreadTitle 方法。这些变化提升了存储查询效率和会话管理能力。沙箱运行时环境管理允许在运行时更新环境变量，并提供 suspend/resume 沙箱的能力。

**标签**: `#sandbox`, `#memory`, `#runtime`, `#tools`

---

<a id="item-harness-arch-3"></a>
### [Codex rust-v0.150.0 发布](https://github.com/openai/codex/releases/tag/rust-v0.150.0) ⭐️ 6.5/10

Codex rust-v0.150.0 发布了新功能，包括 @-task 引用、权限快捷键、命令和 MCP 的中断钩子，以及针对不受信任项目的修复。支持在终端中引用其他 Codex 任务，/copy 提供响应选择器，自动为未命名终端任务生成标题，并添加中断钩子以在活动轮次中断时运行命令或 MCP 处理程序。修复了 Windows 沙盒设置、Unix 关闭挂起和 Bedrock 模型兼容性问题。

github · github-actions\[bot\] · 8月26日 19:37

**「设计要点」** 设计要点：新增中断钩子支持命令和 MCP 处理器的运行时中断，以及权限模式循环绑定和 deny-read 规则管理。

**「改了什么」** 相比 rust-v0.149.0，新增了 @-task 引用和权限模式循环支持，添加了中断钩子，并修复了不受信任项目 AGENTS.md 指令和 MCP 兼容性问题。

**标签**: `#permissions`, `#runtime`, `#mcp`, `#tools`, `#interrupt`

---

<a id="item-harness-arch-4"></a>
### [Cline SDK v0.0.80 发布](https://github.com/cline/cline/releases/tag/sdk/sdk/v0.0.80) ⭐️ 6.5/10

Cline SDK v0.0.80 发布，更新了运行时行为、工具配置和模型提供商支持。文件写入工具现在使用平台原生换行符，修复了 search\_codebase 在单行巨大文件上的崩溃。git remote URL 中的凭证被工作区信息中红 acted，Claude Code 被标记为订阅计费提供商。installMcpServer 不再将 -- 分隔符视为 stdio 命令一部分，tasks 工具可配置仅提供计划工作，模型目录刷新新增七个提供商并更新默认模型。

github · github-actions\[bot\] · 8月26日 08:45

**「改了什么」** 此版本修复了文件写入工具使用原生换行符、search\_codebase 在巨大文件上的崩溃、git remote URL 凭证红 action，以及 installMcpServer 参数处理问题。新增了 tasks 工具的调度配置选项，并刷新了模型目录，新增七个提供商并更新了默认模型。

**标签**: `#runtime`, `#tools`, `#mcp`, `#planning`, `#providers`

---

<a id="item-harness-arch-5"></a>
### [google/adk-python v2.8.0 发布](https://github.com/google/adk-python/releases/tag/v2.8.0) ⭐️ 6.5/10

Google ADK Python v2.8.0 发布。该版本为 RemoteA2aAgent 添加了原生任务模式支持，新增数据代理工具集，并添加 ADK\_MAX\_LLM\_CALLS 环境变量以配置最大 LLM 调用次数。同时集成 Model Armor 防护栏。

github · wukath · 8月26日 23:25

**「改了什么」** 相比 v2.7.1，新增原生任务模式支持到 RemoteA2aAgent，添加数据代理工具集，引入 ADK\_MAX\_LLM\_CALLS 环境变量配置最大 LLM 调用次数，并集成 Model Armor 防护栏。

**标签**: `#runtime`, `#tools`, `#guardrails`, `#task-mode`, `#data-agents`

---

<a id="item-harness-arch-6"></a>
### [Claude Code v2.1.247 发布](https://github.com/anthropics/claude-code/releases/tag/v2.1.247) ⭐️ 5.5/10

Claude Code v2.1.247 版本发布，新增 SendFeedback 工具，当会话出错时 Claude 可以草拟反馈报告供用户从 /feedback 查看和发送（可通过 feedbackDrafts 设置关闭）。添加了 /claude-api cost-optimize 命令，用于分析现有项目的 Claude API 花费并逐步优化缓存、令牌卫生、批量处理等。更新了 /claude-api 技能以覆盖管理员 API 功能，包括组织成员、邀请、工作区、API 密钥、速率限制报告等。

github · ashwin-ant · 8月26日 23:06

**「改了什么」** 此版本新增 SendFeedback 工具和 /claude-api cost-optimize 命令，以及 /claude-api 技能的管理员 API 支持。这些是小幅能力添加，而非架构级或重大运行时变化。

**标签**: `#tools`, `#permissions`

---

<a id="item-harness-arch-7"></a>
### [Cline v4.1.16 发布](https://github.com/cline/cline/releases/tag/v4.1.16) ⭐️ 5.5/10

Cline v4.1.16 发布了，该版本针对钩子工作区处理进行了修复，改为从活动的 VS Code 窗口解析工作区，而不是使用 ~/.cline 中的共享全局状态。在多窗口环境下，第二个窗口打开不同项目时，工作区的 .clinerules/hooks 脚本不会被发现，钩子 cwd 和传递的工作区路径也无法正确解析。

github · github-actions\[bot\] · 8月26日 08:42

**「改了什么」** v4.1.16 修复了钩子工作区解析问题，从活动的 VS Code 窗口解析工作区，而不是使用共享的全局状态。在多窗口场景下，这解决了第二个窗口打开另一个项目时钩子脚本无法发现的问题。

**标签**: `#runtime`, `#memory`, `#hooks`

---

## Agent 工程师日报

<a id="item-agent-engineer-1"></a>
### [Gemini 3.5 Transcribe 智能转录](https://deepmind.google/blog/intelligent-transcription-with-gemini-3-5-transcribe/) ⭐️ 5.5/10

Google DeepMind 宣布推出 Gemini 3.5 Transcribe，这是一款更智能的语音转录工具。
该工具提供更智能的 speech-to-text 转录功能。
这对需要处理音频输入的 AI Agent 工程师有潜在影响。

rss · Google DeepMind · 8月26日 17:01

**标签**: `#orchestration`, `#coding-agent`, `#eval`

---

<a id="item-agent-engineer-2"></a>
### [Dolma 改编出泰语语料 Mangosteen](https://allenai.org/blog/thai-llm-dolma) ⭐️ 5.5/10

Allen AI 官方博客称，泰国研究者改编了 Ai2 开源的 Dolma 工具包，做成名为 Mangosteen 的泰语语料，规模约 470 亿 token。材料的说法是：该语料会过滤低质量网页数据，同时维持或提升模型表现，并加强泰语文化知识。这段介绍没有给出评测集、对比基线、具体分数，也没有写清 Dolma 管线改了哪几步。

rss · Allen AI · 8月26日 08:00

**「为什么重要」** 这是 Dolma 被改成单一语种语料管线的官方记述。过滤网页质量和「表现不降、文化知识加强」是博客里的主张，材料里还没有可核对的评测数字。

**「可关注」** 可关注：Mangosteen 是把开源 Dolma 改成泰语过滤管线的实例；官方把「滤掉低质量网页」和「模型表现维持或提升」写在一起，但未提供可复核的评测设置。

**标签**: `#eval`, `#orchestration`, `#coding-agent`

---

## AI 日报

<a id="item-ai-daily-1"></a>
### [ChatGPT for Teachers 扩展至 55 学区](https://openai.com/index/bringing-chatgpt-for-teachers-to-more-us-school-districts) ⭐️ 8.5/10

OpenAI 将 ChatGPT for Teachers 扩展到 55 个美国学区系统。ChatGPT for Teachers 将安全 AI 工具、培训和支持带给超过 10 万名教育者和工作人员。

rss · OpenAI Blog · 8月26日 10:00

**「可关注」** 可关注：ChatGPT for Teachers 扩展到 55 个美国学区，向超过 10 万名教育者和工作人员提供安全 AI 工具、培训和支持。

**标签**: `#openai`, `#chatgpt`, `#education`, `#product`, `#policy`

---

<a id="item-ai-daily-2"></a>
### [OpenAI 报告：AI 让学习持续不断](https://openai.com/index/learning-never-stops) ⭐️ 6.5/10

OpenAI 发布了新报告，探索学生和教育工作者如何使用 ChatGPT 来支持持续学习。该报告强调学习支持超出课堂范围。

rss · OpenAI Blog · 8月26日 10:00

**标签**: `#openai`, `#chatgpt`, `#education`, `#industry`, `#product`

---