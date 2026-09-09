---
layout: default
title: "Horizon Summary: 2026-09-09 (ZH)"
date: 2026-09-09
lang: zh
---

> 从 182 条内容中筛选出 17 条重要资讯。

---

**Harness 架构**
1. [Claude Code v2.1.265 发布](#item-harness-arch-1) ⭐️ 7.8/10
2. [agents-js v0.17.1 发布](#item-harness-arch-2) ⭐️ 7.8/10
3. [Goose v1.50.0 发布](#item-harness-arch-3) ⭐️ 6.8/10
4. [openai/openai-agents-python v0.22.1 发布](#item-harness-arch-4) ⭐️ 6.8/10
5. [gemini-cli v0.59.0 发布](#item-harness-arch-5) ⭐️ 6.8/10
6. [pydantic-ai v2.41.0 发布](#item-harness-arch-6) ⭐️ 5.8/10
7. [Gemini CLI v0.60.0-preview.0 发布](#item-harness-arch-7) ⭐️ 5.8/10
8. [browser-use/browser-use 进入 GitHub trending](#item-harness-arch-8) ⭐️ 5.0/10
9. [EveryInc Compound Engineering Plugin 登 GitHub Trending](#item-harness-arch-9) ⭐️ 5.0/10

**Agent 工程师日报**
1. [OpenAI 内部模型解决 Navier-Stokes 千年大奖难题](#item-agent-engineer-1) ⭐️ 7.0/10
2. [HF 博客：边界感知自蒸馏安全](#item-agent-engineer-2) ⭐️ 5.8/10

**AI 日报**
1. [OpenAI：工作触手可及](#item-ai-daily-1) ⭐️ 8.8/10
2. [OpenAI 分享 Navier-Stokes 解](#item-ai-daily-2) ⭐️ 8.8/10
3. [OpenAI 推出 $5M 青少年研究拨款](#item-ai-daily-3) ⭐️ 7.8/10
4. [GPT-5.6 Sol 助力量子计算实验](#item-ai-daily-4) ⭐️ 5.8/10
5. [ChatGPT Images 2.5 发布](#item-ai-daily-5) ⭐️ 5.8/10

**科技新闻**
1. [Simon Willison 谈 OpenAI Navier-Stokes 千年难题与数据使用](#item-tech-news-1) ⭐️ 0.0/10

---

## Harness 架构

<a id="item-harness-arch-1"></a>
### [Claude Code v2.1.265 发布](https://github.com/anthropics/claude-code/releases/tag/v2.1.265) ⭐️ 7.8/10

Claude Code v2.1.265 发布。新增支持指向插件文件夹的 --plugin-dir 参数，每个子文件夹有清单时加载，运行时添加或移除子文件夹也能被拾取。添加了 1GB 工具结果保存到磁盘的上限，预览中会提示保存的文件被截断。修复了子代理恢复后工具列表和系统提示前缀变化导致提示缓存复用失败等问题。

github · ashwin-ant · 9月8日 20:37

**「设计要点」** 运行时状态机、提示缓存内存管理、工具沙箱和权限控制。

**「改了什么」** 新增动态插件文件夹加载支持和 1GB 工具结果磁盘上限。修复了子代理恢复提示缓存复用失败、远程控制会话信号发送等问题。

**标签**: `#runtime`, `#tools`, `#sandbox`, `#memory`, `#subagents`, `#prefix-cache`

---

<a id="item-harness-arch-2"></a>
### [agents-js v0.17.1 发布](https://github.com/openai/openai-agents-js/releases/tag/v0.17.1) ⭐️ 7.8/10

openai-agents-js 发布 v0.17.1。MCP 工具可配覆盖整个 server 的 guardrail，输出拦截文案可自定义。Docker sandbox 容器可加 labels，web search 工具支持图片结果。运行时修了 Session 写入恢复、approval 归属和 Chat Completions 工具回合回放。

github · seratch · 9月8日 10:04

**「设计要点」** MCP 工具可在整个 server 上统一加 guardrail，输出拦截文案可自定义。Docker sandbox 容器允许加 labels。

**「改了什么」** 相对 v0.17.0，加上 server 范围 MCP 工具 guardrail、自定义输出拦截文案、sandbox 容器 labels 和 web search 图片结果。同时修了 sandbox Git 参数注入，以及回放、handoff 与并发 Session 写入。

**标签**: `#mcp`, `#sandbox`, `#tools`, `#runtime`, `#guardrails`

---

<a id="item-harness-arch-3"></a>
### [Goose v1.50.0 发布](https://github.com/aaif-goose/goose/releases/tag/v1.50.0) ⭐️ 6.8/10

Goose v1.50.0 发布。该版本新增对 GPT-6 Astra 模型的支持，并增强了代理的工具调用功能。Kotlin 调用者现在可以配置 Databricks AI Gateway 路径。修复了 Snowflake HTTPS 要求、子代理平台守卫、权限撤销等多个问题。

github · github-actions\[bot\] · 9月8日 19:32

**标签**: `#tools`, `#subagents`, `#permissions`, `#runtime`

---

<a id="item-harness-arch-4"></a>
### [openai/openai-agents-python v0.22.1 发布](https://github.com/openai/openai-agents-python/releases/tag/v0.22.1) ⭐️ 6.8/10

openai/openai-agents-python v0.22.1 发布。该版本新增可配置 Unix-local sandbox 隔离，支持 MCP 工具服务器级 guardrails，并使 web search 工具返回图片结果。同时修复了核心运行时和语音相关问题。

github · seratch · 9月8日 09:18

**「设计要点」** sandbox 隔离配置为运行时提供 Unix-local 沙箱支持，MCP guardrails 在工具层实现服务器级保护。

**「改了什么」** 新增可配置 Unix-local sandbox 隔离和 MCP 服务器级 guardrails，web search 工具返回图片结果，并修复多项核心和语音问题。

**标签**: `#sandbox`, `#mcp`, `#runtime`, `#tools`

---

<a id="item-harness-arch-5"></a>
### [gemini-cli v0.59.0 发布](https://github.com/google-gemini/gemini-cli/releases/tag/v0.59.0) ⭐️ 6.8/10

google-gemini/gemini-cli v0.59.0 正式发布。修复了 MCP OAuth 元数据发现和认证中的 SSRF 漏洞。强制执行受限模式下工作空间信任并过滤 mcpServers。

github · gemini-cli-robot · 9月8日 21:13

**「改了什么」** 相比 v0.58.0，修复 MCP OAuth SSRF 问题。强制执行受限模式下工作空间信任并过滤 mcpServers。

**标签**: `#mcp`, `#permissions`, `#tools`, `#sandbox`, `#runtime`

---

<a id="item-harness-arch-6"></a>
### [pydantic-ai v2.41.0 发布](https://github.com/pydantic/pydantic-ai/releases/tag/v2.41.0) ⭐️ 5.8/10

pydantic-ai v2.41.0 发布。新增 ImageGenerator 直接图像生成 API，支持 openai-codex provider，并弃用 fallback\_model 改为 fallback\_subagent\_model。修复 Anthropic 原生 web searches 在 RequestUsage.details 的报告和 cost 计算、BedrockConverseModel 包装 botocore 传输错误、Gemini thinking levels 快照到支持级别等 bug。

github · dsfaccini · 9月8日 04:15

**「改了什么」** 新增 ImageGenerator API 和 openai-codex provider，弃用 fallback\_model 并引入 fallback\_subagent\_model，修复多个 bug。

**标签**: `#subagents`, `#tools`, `#image-generation`, `#providers`

---

<a id="item-harness-arch-7"></a>
### [Gemini CLI v0.60.0-preview.0 发布](https://github.com/google-gemini/gemini-cli/releases/tag/v0.60.0-preview.0) ⭐️ 5.8/10

Google Gemini CLI v0.60.0-preview.0 发布。核心/MCP/sandbox/extension 模块进行小幅更新。修复了 Web fetch 工具的目的地验证和连接路由、MCP OAuth 流中的 RFC 9207 发行者识别、macOS Seatbelt sandbox 的临时目录隔离，以及扩展加载器的路径解析和边界验证。

github · gemini-cli-robot · 9月8日 21:04

**「改了什么」** 相比 v0.59.0-preview.0，主要变化是强化 MCP OAuth 流以符合 RFC 9207，隔离 macOS Seatbelt sandbox 的临时目录，并通过环境变化同意提示和运行时变量清理提升扩展安全性。

**标签**: `#mcp`, `#sandbox`, `#runtime`, `#extensions`

---

<a id="item-harness-arch-8"></a>
### [browser-use/browser-use 进入 GitHub trending](https://github.com/browser-use/browser-use) ⭐️ 5.0/10

browser-use/browser-use repo 进入 GitHub trending，推广 AI 代理使用网页浏览器的自动化能力。浏览器 Use 允许 AI 代理像人类一样操作网页浏览器，打开页面、点击按钮、输入信息并填写表单。用户只需描述任务，它就能自动完成。例如填充表单或提取结构化数据。

rss · GitHub Trending Daily · 9月9日 01:20

**标签**: `#tools`, `#sandbox`, `#runtime`

---

<a id="item-harness-arch-9"></a>
### [EveryInc Compound Engineering Plugin 登 GitHub Trending](https://github.com/EveryInc/compound-engineering-plugin) ⭐️ 5.0/10

EveryInc Compound Engineering Plugin 登 GitHub Trending。该插件为 Claude Code、Codex、Cursor 等 AI 编码代理提供 33 种技能。它采用 brainstorm-plan-build-review-capture 循环组织工程工作流程，并通过持久知识捕获在更改间保留知识。它在 14 个代理主机上运行。

rss · GitHub Trending Daily · 9月9日 01:20

**「设计要点」** 插件围绕 brainstorm-plan-build-review-capture 循环组织工程工作流程，并通过持久知识捕获在更改间保留知识。它在 14 个代理主机上运行。

**标签**: `#planning`, `#memory`, `#tools`

---

## Agent 工程师日报

<a id="item-agent-engineer-1"></a>
### [OpenAI 内部模型解决 Navier-Stokes 千年大奖难题](https://openai.com/index/navier-stokes-solution/) ⭐️ 7.0/10

OpenAI 宣布其内部系统生成的证明解决了 Navier-Stokes 存在与光滑性问题。该证明显示 Navier-Stokes 方程的动力学在有限时间内可能出现奇点。OpenAI 分享了这一解决方案和相关材料。这一结果由内部 AI 模型产生，引发了数学界和 AI 研究者的广泛讨论。

hackernews · tedsanders · 9月8日 17:13 · [社区讨论](https://news.ycombinator.com/item?id=49613262)

**「为什么重要」** 这一结果显示了 AI 在数学能力上的快速进步。它已发生，但对研究动态的具体影响尚未完全证实。

**「可关注」** 可关注：内部模型在数学能力上的快速提升。

**「评论」** 社区对 OpenAI 模型快速数学能力提升的讨论展开。Terence Tao 指出谣言可能触发大量 AI 努力，有人质疑其基于他人工作。

**标签**: `#eval`, `#coding-agent`, `#orchestration`

---

<a id="item-agent-engineer-2"></a>
### [HF 博客：边界感知自蒸馏安全](https://huggingface.co/blog/MultiverseComputingCAI/safety-for-whom) ⭐️ 5.8/10

HF 博客批判话题级 LLM 安全防护的局限性，指出同一模型在不同部署中需不同边界，LlamaGuard-3 无法区分政治操纵与事实信息。最新论文研究边界感知自蒸馏，采用政治提示作为测试用例，使用自我生成数据修复覆盖缺口并引入边界对。覆盖修复后残余失败降至 0.20%。训练后有害拒绝率提升至 84.75%，XSTest 过拒绝对升至 74.00%。影响评估 harness 和代理权限的细粒度控制。

rss · Hugging Face Blog · 9月8日 14:23

**「为什么重要」** HF 博客强调真实部署需针对话题子集精细边界，而非全拒。论文方法提供细粒度安全训练框架，已发生的变化是边界感知训练降低过拒绝对，但对 harness 工具的影响尚未证实。

**「可关注」** 可关注：安全训练需同时测量有害拒绝率与过拒绝对，否则提升拒绝率会使模型在合规提示上失效。

**标签**: `#eval`, `#harness`, `#permissions`

---

## AI 日报

<a id="item-ai-daily-1"></a>
### [OpenAI：工作触手可及](https://openai.com/index/the-work-now-within-reach) ⭐️ 8.8/10

OpenAI 博客发布了题为《The Work Now Within Reach》的文章。
文章探讨了更具能力且更经济的 AI 如何扩展人们和企业能完成的工作，并使增长更经济。

rss · OpenAI Blog · 9月8日 13:00

**标签**: `#openai`, `#model`, `#industry`

---

<a id="item-ai-daily-2"></a>
### [OpenAI 分享 Navier-Stokes 解](https://openai.com/index/navier-stokes-solution) ⭐️ 8.8/10

OpenAI 分享了 AI 生成的 Navier-Stokes 千年大奖问题解决方案。

rss · OpenAI Blog · 9月8日 10:00

**「可关注」** 可关注：AI 生成的 Navier-Stokes 解包含 Lean 形式化证明。

**标签**: `#OpenAI`, `#model`, `#industry`, `#eval`, `#open-source`

---

<a id="item-ai-daily-3"></a>
### [OpenAI 推出 $5M 青少年研究拨款](https://openai.com/index/teen-development-research-grants) ⭐️ 7.8/10

OpenAI 推出 500 万美元拨款计划。
该计划支持独立研究生成式 AI 对青少年发展、福祉和安全的影响。
申请现在开放。

rss · OpenAI Blog · 9月8日 09:00

**「可关注」** 可关注：申请 OpenAI $5M 拨款研究生成式 AI 对青少年发展、福祉和安全的影响

**标签**: `#lab`, `#policy`, `#industry`

---

<a id="item-ai-daily-4"></a>
### [GPT-5.6 Sol 助力量子计算实验](https://openai.com/index/codex-quantum-computing-experiments) ⭐️ 5.8/10

MIT 研究者使用 GPT-5.6 Sol 集成 Codex，自主运行量子计算实验，分析结果并校准量子比特。
该过程实现了实验的完全自动化。
材料未披露具体实验细节或量化指标。

rss · OpenAI Blog · 9月8日 17:00

**「可关注」** 可关注：MIT 研究者利用 GPT-5.6 Sol 与 Codex 自主运行量子计算实验并校准量子比特。

**标签**: `#openai`, `#quantum-computing`, `#gpt`, `#ai-application`, `#industry`

---

<a id="item-ai-daily-5"></a>
### [ChatGPT Images 2.5 发布](https://openai.com/index/introducing-chatgpt-images-2-5) ⭐️ 5.8/10

OpenAI 发布了 ChatGPT Images 2.5。
ChatGPT Images 2.5 帮助将你的想法、草图和参考照片转化为更个性化、精致的图像。
这些图像能更好地反映你的想法。

rss · OpenAI Blog · 9月8日 11:30

**标签**: `#openai`, `#product`, `#chatgpt`, `#image-generation`

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [Simon Willison 谈 OpenAI Navier-Stokes 千年难题与数据使用](https://twitter.com/simonw/status/tweet-2097474703380365698) ⭐️ 0.0/10

Simon Willison 分享了他对 OpenAI Navier-Stokes 千年难题故事的思考。这件事突显了使用数据来改进 AI 模型性能的含义仍然存在困惑。OpenAI 作为人工智能领域的领先公司，其相关故事引发了对数据使用方式的广泛讨论。使用数据“to improve model performance”的概念在技术界仍未明确，这对 AI 行业的发展具有重要意义。

twitter · Simon Willison · 9月8日 23:58

**「纳维-斯托克斯千年难题」** 纳维-斯托克斯方程是描述粘性流体运动的基本偏微分方程，由英国数学家克劳德·朗德尔在 1845 年提出。克莱数学研究所于 2000 年将该方程的存在性和光滑性问题列为七大千禧年难题之一，悬赏 100 万美元。OpenAI 声称其内部 AI 系统已找到该问题的解决方案，证明流体运动的动力学在有限时间内可能出现奇点，并提供了证明的书面形式和在 Lean 定理证明器中的形式化。Simon Willison 认为，此类 AI 生成解决方案突显了“使用数据来改进模型性能”这一概念的模糊性，因为 AI 如何利用数据生成新知识仍缺乏清晰定义。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/navier-stokes-solution/">On the Navier-Stokes Millennium Prize Problem | OpenAI</a></li>
<li><a href="https://www.newscientist.com/article/2588063-openai-has-solved-the-navier-stokes-millennium-problem-using-15m-of-ai-effort/">OpenAI has solved the Navier-Stokes Millennium problem using $15m of AI ...</a></li>
<li><a href="https://www.nature.com/articles/d41586-026-02842-5">OpenAI claims huge maths breakthrough on a famed &#x27;Millennium Problem ...</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#Navier-Stokes`, `#Millennium Prize Problem`, `#AI Data Usage`, `#Tech Analysis`

---