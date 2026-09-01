---
layout: default
title: "Horizon Summary: 2026-09-02 (ZH)"
date: 2026-09-02
lang: zh
---

> 从 210 条内容中筛选出 19 条重要资讯。

---

**Harness 架构**
1. [LangChain 1.4.0a3 发布](#item-harness-arch-1) ⭐️ 7.8/10
2. [Graphiti mcp-v1.1.0 发布](#item-harness-arch-2) ⭐️ 7.8/10
3. [Claude Code 2.1.257 发布](#item-harness-arch-3) ⭐️ 7.8/10
4. [Codex rust-v0.152.0 发布](#item-harness-arch-4) ⭐️ 6.8/10
5. [Pydantic AI v2.37.0 发布](#item-harness-arch-5) ⭐️ 6.8/10
6. [Gemini CLI v0.59.0-preview.0 发布](#item-harness-arch-6) ⭐️ 6.8/10
7. [Cline desktop-v0.0.22-beta.1 发布](#item-harness-arch-7) ⭐️ 5.8/10
8. [video-use Claude Code 视频编辑工具](#item-harness-arch-8) ⭐️ 5.0/10

**Agent 工程师日报**
1. [BenchMIRT：LLM 基准实际测量什么](#item-agent-engineer-1) ⭐️ 7.8/10
2. [@huggingface/kernels 发布](#item-agent-engineer-2) ⭐️ 7.8/10
3. [Claude Fable 5.1 &amp; Mythos 5.1 发布](#item-agent-engineer-3) ⭐️ 7.0/10
4. [CogEvol 高效可靠学习环境生成](#item-agent-engineer-4) ⭐️ 7.0/10
5. [MineAmongUs 3D sandbox 与 ARIA harness 发布](#item-agent-engineer-5) ⭐️ 7.0/10
6. [Super Library Agent 问题提出](#item-agent-engineer-6) ⭐️ 6.0/10
7. [Gemini agentic video 发布](#item-agent-engineer-7) ⭐️ 5.8/10

**AI 日报**
1. [Anthropic EFS 发布](#item-ai-daily-1) ⭐️ 8.8/10
2. [Astra 首达临界网络安全能力阈值](#item-ai-daily-2) ⭐️ 7.8/10
3. [ChatGPT 连接 EHR 与医疗数据](#item-ai-daily-3) ⭐️ 7.8/10
4. [OpenAI 博客：AI 原生公司工作流转运营](#item-ai-daily-4) ⭐️ 6.8/10

---

## Harness 架构

<a id="item-harness-arch-1"></a>
### [LangChain 1.4.0a3 发布](https://github.com/langchain-ai/langchain/releases/tag/langchain%3D%3D1.4.0a3) ⭐️ 7.8/10

LangChain 发布 1.4.0a3，这是 1.4.0 线的第三个 alpha。本版加入 \`langchain.mcp\`，把 MCP 服务器适配成 LangChain 工具。安装需 \`pip install --pre &quot;langchain==1.4.0a3&quot;\`，并加 \`langchain\[mcp\]\` extra，依赖 \`fastmcp&gt;=4.0.0\`。

github · github-actions\[bot\] · 9月1日 17:19

**「设计要点」** \`MCPAdapter\` 适配 URL、本地脚本、进程内服务器、可点名多台服务器的 \`MCPConfig\`、现成 client，以及 FastMCP \`ClientGroup\`。\`list\_tools\` 按 SEP-2549 做客户端缓存（默认 \`use\`，在服务器 TTL 提示内复用；\`refresh\` 重拉，\`bypass\` 跳过）；单工具可用 \`as\_langchain\_tool\`；annotations（snake\_case）和 \`\_meta\` 放在 \`metadata\[&quot;mcp&quot;\]\[&quot;tool&quot;\]\`，服务器身份放在 \`metadata\[&quot;mcp&quot;\]\[&quot;server&quot;\]\`；\`elicitation=&quot;interrupt&quot;\` 把服务端中途提问变成 LangGraph interrupt，人答完再续跑。

**「改了什么」** 本版新增 \`langchain.mcp\` 命名空间。\`MCPAdapter\` 把 MCP 服务器适配成工具，自管 client 可用 \`as\_langchain\_tool\`。

**标签**: `#mcp`, `#tools`, `#runtime`

---

<a id="item-harness-arch-2"></a>
### [Graphiti mcp-v1.1.0 发布](https://github.com/getzep/graphiti/releases/tag/mcp-v1.1.0) ⭐️ 7.8/10

Graphiti mcp-v1.1.0 发布。针对自托管 Neo4j 部署，MCP 服务器现在一致使用配置的 NEO4J\_DATABASE。之前自定义设置可能导致数据分散在 home 数据库和配置数据库之间。核心依赖更新为 graphiti-core 0.30.1，并修复了 CI 发布元数据问题。

github · mehulp93 · 9月1日 23:09

**「设计要点」** MCP 服务器修复了 Neo4j 数据库路由问题，确保所有操作严格遵循 NEO4J\_DATABASE 配置。之前可能导致 add\_memory 和 search 操作数据分散在不同数据库。

**「改了什么」** 相比 v0.30.0，mcp-v1.1.0 修复了 Neo4j 数据库路由并一致使用配置数据库。还更新了 graphiti-core 至 0.30.1，并修复了 CI 相关依赖。

**标签**: `#mcp`, `#runtime`, `#memory`

---

<a id="item-harness-arch-3"></a>
### [Claude Code 2.1.257 发布](https://code.claude.com/docs/en/changelog#2-1-257) ⭐️ 7.8/10

Claude Code 2.1.257 发布了。新增子代理模型强制功能，使用 CLAUDE\_CODE\_SUBAGENT\_MODEL\_FORCE 环境变量强制子代理模型。添加自动模式下的包含逃逸规则以处理云元数据凭证获取等操作。新增/doctor 警告用于过时的沙盒掩码文件，并新增 timeFormat 和 timeZone 设置选项用于转录时间戳。

rss · Claude Code Changelog · 9月1日 18:00

**「改了什么」** Claude Code 2.1.257 相对上一版新增了子代理模型强制、自动模式包含逃逸规则、沙盒掩码警告以及时间戳配置选项。

**标签**: `#subagents`, `#sandbox`, `#permissions`, `#runtime`

---

<a id="item-harness-arch-4"></a>
### [Codex rust-v0.152.0 发布](https://github.com/openai/codex/releases/tag/rust-v0.152.0) ⭐️ 6.8/10

Codex rust-v0.152.0 发布。新增 Vim 模式支持 / 和 ? 搜索草稿，并支持高亮匹配和 n、N 重复导航。MCP 服务器名支持冒号、@、/、. 等字符，并新增 per-tool output\_token\_limit 配置。App-server 客户端可配置 thread/shellCommand 超时，支持超过一小时的 deadline。

github · github-actions\[bot\] · 9月1日 01:58

**「改了什么」** rust-v0.152.0 相比上一版，新增 Vim 搜索和 rate-limit 行动栏。MCP 支持增强，新增 per-tool 输出限额和超时配置。

**标签**: `#mcp`, `#runtime`, `#tools`

---

<a id="item-harness-arch-5"></a>
### [Pydantic AI v2.37.0 发布](https://github.com/pydantic/pydantic-ai/releases/tag/v2.37.0) ⭐️ 6.8/10

Pydantic AI v2.37.0 发布。新增 glm-5.3-flash 模型支持并重构 Z.AI 测试套件。修复了代理追踪、工具调用和模型路由等多个 bug。

github · dsfaccini · 9月1日 01:48

**「改了什么」** 相比 v2.36.0，新增 glm-5.3-flash 模型支持并重构 Z.AI 测试套件。修复了代理追踪、工具调用和 UI 相关的多个 bug。

**标签**: `#runtime`, `#tools`, `#fix`

---

<a id="item-harness-arch-6"></a>
### [Gemini CLI v0.59.0-preview.0 发布](https://github.com/google-gemini/gemini-cli/releases/tag/v0.59.0-preview.0) ⭐️ 6.8/10

Gemini CLI v0.59.0-preview.0 发布。修复了 MCP OAuth 元数据发现和认证的 SSRF 漏洞，并强制执行受限模式下工作区信任的 fail-closed 策略。相比 v0.58.0-preview.0，主要技术改进是 MCP 安全修复和权限控制增强。

github · gemini-cli-robot · 9月1日 20:19

**「改了什么」** Gemini CLI v0.59.0-preview.0 相比 v0.58.0-preview.0，新增 MCP OAuth 认证的 SSRF 防护，以及受限模式下工作区信任的 fail-closed 策略和 mcpServers 过滤。

**标签**: `#mcp`, `#sandbox`, `#permissions`, `#runtime`, `#fix`

---

<a id="item-harness-arch-7"></a>
### [Cline desktop-v0.0.22-beta.1 发布](https://github.com/cline/cline/releases/tag/desktop-v0.0.22-beta.1) ⭐️ 5.8/10

Cline desktop v0.0.22-beta.1 发布。该版本支持 Composio 连接器在打包桌面运行时直接注册工具，适用于符合条件的账号，并默认启用网页搜索。包含 0.0.21 版所有稳定改进。

github · github-actions\[bot\] · 9月1日 22:39

**「改了什么」** Composio 连接器在桌面打包运行时直接注册工具，支持更安全的 OAuth 撤销和更可靠的连接断开调和行为。网页搜索默认启用。

**标签**: `#runtime`, `#tools`, `#subagents`, `#permissions`

---

<a id="item-harness-arch-8"></a>
### [video-use Claude Code 视频编辑工具](https://github.com/browser-use/video-use) ⭐️ 5.0/10

video-use 是一个开源工具，允许通过 Claude Code 编辑视频。用户将原始视频文件放入文件夹，与 Claude Code 聊天，即可生成 final.mp4。支持任何内容类型，包括谈话头、蒙太奇、教程、旅行和访谈，无需预设或菜单。功能包括去除填充词和死区，并自动为每个片段进行色彩分级。

rss · GitHub Trending Daily · 9月1日 23:24

**标签**: `#tools`, `#subagents`, `#sandbox`

---

## Agent 工程师日报

<a id="item-agent-engineer-1"></a>
### [BenchMIRT：LLM 基准实际测量什么](https://huggingface.co/blog/allenai/benchmirt) ⭐️ 7.8/10

AllenAI 推出 BenchMIRT，这是一种针对 LLM 基准提示级的审计方法。它基于多维项目反应理论，分析 100 个 LLM 在 16 个基准（34K 问题）上的表现，独立发现安全和通用推理两个维度。结果显示 BBQ 更关联通用推理，WMDP 得分与推理负相关，HarmBench 不同问题组信号不同。训练数据使用 2025 年 3 月前发布的模型。

rss · Hugging Face Blog · 9月1日 21:39

**「为什么重要」** BenchMIRT 发布，能帮助研究者分离基准信号，使分数更容易解释。尚未证实其对未来模型评估的影响。

**「可关注」** 可关注：BenchMIRT 可用 10% 问题保留能力测量，并预测未观察问题正确率 79%（对比 70%）。

**标签**: `#eval`, `#harness`, `#benchmark`, `#llm`, `#auditing`

---

<a id="item-agent-engineer-2"></a>
### [@huggingface/kernels 发布](https://huggingface.co/blog/webgpu-kernels) ⭐️ 7.8/10

Hugging Face 发布了 @huggingface/kernels 库，包含 207 个 WebGPU 内核，用于本地 AI 推理。该库提供 JavaScript loader，可从 Hugging Face Hub 下载并运行内核，并附带 Fleet 浏览器 GPU 基准测试套件。

每个内核作为独立仓库发布，包含 manifest.json、test.json、bench.json 和 \*.wgsl.jinja 文件，Apache-2.0 许可。

在 Apple M4 GPU 上，与 ORT WebGPU 1.30.0-dev.20260826-b1f76d586a 相比，这些内核在 809 个匹配测试用例中几何平均快 2.57 倍，中位数快 1.90 倍。

rss · Hugging Face Blog · 9月1日 00:00

**「为什么重要」** 该发布为浏览器端本地 AI 提供了可发现、可测试、可基准化的内核基础层。

**「可关注」** 可关注：内核应为不同形状和设备提供变体，以匹配性能需求。

**标签**: `#eval`, `#orchestration`, `#harness`

---

<a id="item-agent-engineer-3"></a>
### [Claude Fable 5.1 &amp; Mythos 5.1 发布](https://www.anthropic.com/claude-fable-and-mythos-5-1) ⭐️ 7.0/10

Anthropic 发布了 Claude Fable 5.1 和 Claude Mythos 5.1。Fable 5.1 写作风格更自然，响应风格指令更可靠。缓存读取定价从 $1/M 降至 $0.25/M，Fable 5.1 缓存读取成本降至 Opus 的一半。发布了记录和可视化 LLM thinking effort 水平的开发者工具。

hackernews · denysvitali · 9月1日 17:53 · [社区讨论](https://news.ycombinator.com/item?id=49525378)

**「为什么重要」** 缓存成本降低已发生，影响 coding agent harness 的 eval 成本。Fable 5.1 写作风格改进已发生，但对 agent 性能的具体影响尚未证实。

**「可关注」** 可关注：Pelican 可视化工具可记录和可视化 thinking effort 低、中、高、xhigh 水平的 reasoning traces。

**「评论」** Felix Rieseberg 指出 Fable 5.1 写作风格更自然，响应指令更可靠。Simon Willison 分享 Pelican 工具并修复 bug，生成 max effort 耗时近 14 分钟。部分用户认为 Fable 被 nerfed，Mythos 是营销策略。

**标签**: `#coding-agent`, `#harness`, `#observability`, `#eval`, `#orchestration`

---

<a id="item-agent-engineer-4"></a>
### [CogEvol 高效可靠学习环境生成](https://huggingface.co/papers/2608.30968) ⭐️ 7.0/10

CogEvol 模型家族使用生产接地 SFT 和 RL，从课程简报一次性生成学习环境，包括结构化 JSON 幻灯片或自包含交互式 HTML 页面。在 220k 生产请求中，幻灯片生成中位耗时 17 秒，交互页面 59 秒，取代了多轮代理脚手架。可靠性通过 53,687 验证 SFT 样本和修复的奖励劫持 GRPO RL 实现，CogEvol-27B 在幻灯片质量和 500 案例交互 HTML 基准上分别得分 83.7 和 63.7。这直接影响代理编排和内容生成评估 harness。

rss · Hugging Face Daily Papers · 9月1日 00:00

**「为什么重要」** 这一单次生成方法将学习环境生成从多轮代理脚手架替换为 17 秒和 59 秒中位耗时，显著提升效率。生产数据验证和奖励机制改进为代理编排提供了可靠替代方案。

**「可关注」** 可关注：220k 生产请求驱动的 53,687 验证 SFT 样本和奖励劫持修复后的 GRPO RL。

**标签**: `#harness`, `#eval`, `#orchestration`

---

<a id="item-agent-engineer-5"></a>
### [MineAmongUs 3D sandbox 与 ARIA harness 发布](https://huggingface.co/papers/2608.30428) ⭐️ 7.0/10

HF daily paper 介绍了 MineAmongUs 3D 多模态 Among Us 沙盒和 ARIA 可配置 VLM 代理 harness。 MineAmongUs 中 imposter 代理需通过联合言语和非言语行动欺骗 crewmates。 ARIA harness 暴露代理在多代理社会演绎中的联合欺骗认知能力。 这些工具直接相关于代理评估和 harness 架构。

rss · Hugging Face Daily Papers · 9月1日 00:00

**「为什么重要」** MineAmongUs 3D 多模态沙盒和 ARIA harness 的发布填补了现有文本-only 测试基板在非言语传感器运动通道的空白。 这些工具直接相关于代理评估和 harness 架构。

**「可关注」** 可关注：现有测试基板仅为文本模式且固定配置，忽略非言语传感器运动通道，导致观察到的行为是否反映底层模型还是 harness 存在歧义。

**标签**: `#harness`, `#eval`, `#orchestration`, `#coding-agent`

---

<a id="item-agent-engineer-6"></a>
### [Super Library Agent 问题提出](https://huggingface.co/papers/2608.29310) ⭐️ 6.0/10

组织常开发维护相关应用的组合：独立部署的代码库，共享大量领域逻辑、接口模式或操作惯例。LLM coding agents 生成维护此类软件时，逐个应用工作流会重复共享逻辑，导致维护中冗余、死代码和结构侵蚀积累。提出 Super Library Agent 问题：代理顺序生成 N 个相关应用，同时维护共享的 Super Library 可重用跨应用组件。最小顺序脚手架可提取共享代码并迁移应用到演化库中。这对 coding-agent 的 orchestration 和 memory 具有架构相关性。

rss · Hugging Face Daily Papers · 9月1日 00:00

**「为什么重要」** 该工作提出多应用组合维护的 Super Library Agent 问题，并给出最小顺序脚手架。这对 LLM coding agents 的 orchestration 和 memory 管理有架构相关性，但论文未提供实验验证或基准测试。

**「可关注」** 可关注：代理顺序生成相关应用组合时维护共享 Super Library 的最小顺序脚手架。

**标签**: `#coding-agent`, `#orchestration`, `#memory`

---

<a id="item-agent-engineer-7"></a>
### [Gemini agentic video 发布](https://deepmind.google/blog/introducing-agentic-video-in-gemini/) ⭐️ 5.8/10

Google DeepMind 发布了 Gemini agentic video understanding 能力的介绍。官方博客介绍了这一新功能。相关于 coding-agent 和 orchestration 领域。

rss · Google DeepMind · 9月1日 17:08

**「为什么重要」** 这一能力已发布。相关于 coding-agent 和 orchestration 领域。

**「可关注」** 可关注：Gemini agentic video understanding 能力。

**标签**: `#coding-agent`, `#orchestration`

---

## AI 日报

<a id="item-ai-daily-1"></a>
### [Anthropic EFS 发布](https://www.anthropic.com/news/enterprise-frontier-safeguards) ⭐️ 8.8/10

Anthropic 推出 Enterprise Frontier Safeguards \(EFS\)，结合零数据留存隐私与误用检测保障。EFS 由 100 余客户及 AWS、Google Cloud、Microsoft Azure 共同开发。数据存储在客户控制的云基础设施中，无 Anthropic 人工审核。分阶段推出，秋季后期开始。

rss · Anthropic News · 9月1日 00:00

**「为什么重要」** EFS 解决了企业对前沿模型安全与隐私的困境。

**「可关注」** 可关注：客户可控制数据存储在自身云基础设施，使用加密密钥和审计日志。

**标签**: `#lab`, `#product`, `#industry`, `#policy`

---

<a id="item-ai-daily-2"></a>
### [Astra 首达临界网络安全能力阈值](https://openai.com/index/path-to-astra) ⭐️ 7.8/10

OpenAI 宣布 Astra 是首个达到 Preparedness Framework 临界网络安全能力阈值的模型。模型发布时增加了更强的保障措施。

rss · OpenAI Blog · 9月1日 13:00

**「为什么重要」** OpenAI 宣布 Astra 达到 Preparedness Framework 临界网络安全能力阈值。模型发布时增加了更强的保障措施。

**「可关注」** 可关注：Astra 是 OpenAI 首个达到 Preparedness Framework 临界网络安全能力阈值的模型，并增加了更强的发布保障措施。

**标签**: `#model`, `#lab`, `#policy`, `#product`

---

<a id="item-ai-daily-3"></a>
### [ChatGPT 连接 EHR 与医疗数据](https://openai.com/index/chatgpt-connects-health-records-and-healthcare-sources) ⭐️ 7.8/10

ChatGPT 现已连接可信医疗数据。
帮助临床医生安全访问患者背景、医学研究等更多信息。

rss · OpenAI Blog · 9月1日 12:00

**「为什么重要」** 此集成帮助临床医生安全访问患者上下文和医学研究等信息。

**「可关注」** 可关注：ChatGPT 连接 EHR 与医疗数据

**标签**: `#lab`, `#industry`, `#product`

---

<a id="item-ai-daily-4"></a>
### [OpenAI 博客：AI 原生公司工作流转运营](https://openai.com/index/ai-native-company-workflows) ⭐️ 6.8/10

OpenAI 博客分享 AI 原生公司如何将工作流转化为运营能力。Basis、Clay 和 Exa Labs 使用 AI 代理分别改善入职、账户管理和开发者集成。这些案例为企业领导者提供了实际应用参考。

rss · OpenAI Blog · 9月1日 17:00

**「为什么重要」** 这些案例表明 AI 代理可将工作流转化为持续运营能力，对 AI 原生公司有指导价值。

**「可关注」** 可关注：企业可通过 AI 代理提升入职、账户管理和开发者集成。

**标签**: `#lab`, `#industry`, `#product`

---