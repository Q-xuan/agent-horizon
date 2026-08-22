---
layout: default
title: "Horizon Summary: 2026-08-22 (ZH)"
date: 2026-08-22
lang: zh
---

> 从 145 条内容中筛选出 24 条重要资讯。

---

**Harness 架构**
1. [DSPy 3.3.1 发布](#item-harness-arch-1) ⭐️ 8.0/10
2. [e2b@2.45.0 发布](#item-harness-arch-2) ⭐️ 6.0/10
3. [Cline v4.1.12 发布](#item-harness-arch-3) ⭐️ 5.0/10
4. [Cline v4.1.11 发布](#item-harness-arch-4) ⭐️ 5.0/10
5. [Cline desktop-v0.0.16-beta.1 发布](#item-harness-arch-5) ⭐️ 5.0/10
6. [Goose v1.47.0 发布](#item-harness-arch-6) ⭐️ 5.0/10
7. [gemini-cli v0.56.0-nightly.20260822.g5411f113c 发布](#item-harness-arch-7) ⭐️ 5.0/10

**Agent 工程师日报**
1. [NVIDIA AVO 100% 完成 ARC-AGI-3](#item-agent-engineer-1) ⭐️ 9.0/10
2. [Felony Bench 聚合 AI 代理法律案例](#item-agent-engineer-2) ⭐️ 7.0/10
3. [Claudette: 让 Claude 停止 BuzzFeed 风格输出](#item-agent-engineer-3) ⭐️ 7.0/10
4. [自托管沙箱代理软件工厂构建](#item-agent-engineer-4) ⭐️ 7.0/10
5. [DeepSeek Harness v0.1.1 发布](#item-agent-engineer-5) ⭐️ 7.0/10
6. [Simile AI：模拟成新 Scaling Law](#item-agent-engineer-6) ⭐️ 6.0/10

**AI 日报**
1. [Anthropic IPO 文件显示 AI 反弹风险](#item-ai-daily-1) ⭐️ 6.0/10
2. [OpenAI 呼吁加州加强 AI 法律](#item-ai-daily-2) ⭐️ 6.0/10
3. [康涅狄格 SB5 法案：AI 州监管趋势](#item-ai-daily-3) ⭐️ 6.0/10
4. [浙大 BEACON 按里程碑分配信用](#item-ai-daily-4) ⭐️ 5.0/10
5. [英国转向蓬勃发展的芯片新贵 支持主权 AI 策略](#item-ai-daily-5) ⭐️ 5.0/10
6. [WSJ：中国 AI 飞跃的幕后人物](#item-ai-daily-6) ⭐️ 5.0/10
7. [在线主播起诉 Twitch 和 Amazon 生成式 AI 训练](#item-ai-daily-7) ⭐️ 5.0/10
8. [犹他大学 SCI 获 2400 万美元 NSF 资助](#item-ai-daily-8) ⭐️ 5.0/10

**AI 羊毛**
1. [OpenAI 宣布 GPT-5.6 Sol API 定价降超 20%](#item-ai-deals-1) ⭐️ 7.0/10
2. [Ox Alpha 免费领取一周](#item-ai-deals-2) ⭐️ 6.0/10
3. [ChillyCapy 离线 AI 文本检测器](#item-ai-deals-3) ⭐️ 6.0/10

---

## Harness 架构

<a id="item-harness-arch-1"></a>
### [DSPy 3.3.1 发布](https://github.com/stanfordnlp/dspy/releases/tag/3.3.1) ⭐️ 8.0/10

DSPy 3.3.1 发布了 PythonInterpreter 的托管运行时安装选项。通过 \`pip install &quot;dspy\[deno\]&quot;\` 可以获得托管二进制文件，优先使用它并继续支持系统 Deno 2.x 和自定义命令。这加强了沙箱隔离和请求处理，关闭了几个执行完整性和隔离漏洞。还添加了端到端的解释器执行可见性，包括回调 API，并改进了优化器吞吐量和适配器正确性。此外，GEPA 优化器支持多提案采样，适配器在缺失可选字段时应用默认值，MCP 兼容性增强。

github · isaacbmiller · 8月21日 23:07

**「设计要点」** PythonInterpreter 提供了托管运行时选项，通过 \`pip install &quot;dspy\[deno\]&quot;\` 安装托管二进制文件。沙箱隔离得到加强，执行完整性和隔离漏洞被关闭。

**「改了什么」** 此版本增加了 PythonInterpreter 的托管运行时安装选项，并加强了沙箱隔离和请求处理。GEPA 优化器支持多提案采样，适配器在缺失可选字段时应用默认值，MCP 兼容性增强，CodeAct 和 ProgramOfThought 已弃用。

**标签**: `#runtime`, `#sandbox`, `#mcp`, `#tools`, `#interpreter`

---

<a id="item-harness-arch-2"></a>
### [e2b@2.45.0 发布](https://github.com/e2b-dev/E2B/releases/tag/e2b%402.45.0) ⭐️ 6.0/10

e2b-dev/e2b 发布了 e2b@2.45.0 版本。主要技术更新是 Sandbox.list 接口新增了排序和过滤功能。支持按开始时间排序（order 选项，&\#x27;asc&\#x27;/&\#x27;desc&\#x27;，默认 &\#x27;desc&\#x27;），以及 startedAfter/started\_after 和 template 过滤器，这些过滤器在服务器端应用于整个分页数据集。

github · github-actions\[bot\] · 8月21日 12:42

**「改了什么」** 相比上一版，e2b@2.45.0 向 Sandbox.list 添加了按开始时间排序和 startedAfter/template 过滤器。这些更改在服务器端应用在分页前。

**标签**: `#sandbox`, `#api`, `#runtime`

---

<a id="item-harness-arch-3"></a>
### [Cline v4.1.12 发布](https://github.com/cline/cline/releases/tag/v4.1.12) ⭐️ 5.0/10

Cline v4.1.12 发布了。这个版本通过 SDK bundle 应用到 Windows 运行时。Cline 强制执行企业 MCP 控制，包括在 Customize 市场隐藏远程禁用市场的条目，并限制到 allowedMCPServers。当自定义 OpenAI-Compatible 模型的存储能力列表为空时，恢复了工具调用功能。

github · github-actions\[bot\] · 8月21日 22:39

**「改了什么」** v4.1.12 相比 v4.1.11，强制实施了 Customize 市场的企业 MCP 控制，包括根据远程配置隐藏 MCP 条目和应用 allowlist 限制。同时恢复了自定义 OpenAI-Compatible 模型的工具调用，这些模型之前因空能力列表而无法调用工具。

**标签**: `#mcp`, `#tools`, `#permissions`, `#runtime`

---

<a id="item-harness-arch-4"></a>
### [Cline v4.1.11 发布](https://github.com/cline/cline/releases/tag/v4.1.11) ⭐️ 5.0/10

Cline v4.1.11 发布了新版本，新增了在任务期间生成图像的功能。支持支持图像生成的模型，并在对话中内联显示生成的图像。这是通过 SDK bundle 发布的补丁版本，适用于 Windows 等平台。同时修复了代码操作在 VS Code 1.134 上失败、包含空格的文件路径、CRLF 行尾编辑、会话恢复、遗留任务迁移、令牌限制等多个问题。

github · github-actions\[bot\] · 8月21日 05:30

**「改了什么」** Cline v4.1.11 相对于上一版 v4.1.10，真正新增的能力是在任务期间生成图像，并在对话中内联显示。同时修复了多个具体技术问题。

**标签**: `#tools`, `#runtime`, `#memory`

---

<a id="item-harness-arch-5"></a>
### [Cline desktop-v0.0.16-beta.1 发布](https://github.com/cline/cline/releases/tag/desktop-v0.0.16-beta.1) ⭐️ 5.0/10

Cline desktop v0.0.16-beta.1 发布了。该版本修复了云端切换时提示丢失的问题，并修复了模型选择器弹窗阻塞点击的问题。视觉上清理了提供商设置、通知和头像叠加的回归。包含重新设计的首次运行引导、集中化工具可用性、PostToolUse 钩子修复以及检查点恢复改进。

github · github-actions\[bot\] · 8月21日 20:06

**「设计要点」** PostToolUse 钩子输出和上下文变化现在能传递到模型，工具可用性已集中化，检查点恢复在队列轮次后不再锁定。

**「改了什么」** 相比 v0.0.15-beta.1，修复了云端切换时提示丢失的问题，并修复了模型选择器弹窗的点击阻塞。视觉回归也已清理。

**标签**: `#runtime`, `#tools`, `#memory`

---

<a id="item-harness-arch-6"></a>
### [Goose v1.47.0 发布](https://github.com/aaif-goose/goose/releases/tag/v1.47.0) ⭐️ 5.0/10

Goose v1.47.0 发布了。该版本添加了交互式 git 分支指示器，支持预注册 OAuth 客户端用于 streamable\_http 扩展，并在聊天底部模型选择器中显示最近使用的模型。同时修复了子代理并发通知隔离、配方参数验证等多个问题。

github · github-actions\[bot\] · 8月21日 18:14

**「改了什么」** 相比上一版，Goose v1.47.0 增加了交互式 git UI 和预注册 OAuth 支持，并优化了模型选择器显示最近模型。修复了 subagent 并发和 recipe 验证等 bug。

**标签**: `#subagents`, `#tools`, `#runtime`

---

<a id="item-harness-arch-7"></a>
### [gemini-cli v0.56.0-nightly.20260822.g5411f113c 发布](https://github.com/google-gemini/gemini-cli/releases/tag/v0.56.0-nightly.20260822.g5411f113c) ⭐️ 5.0/10

gemini-cli v0.56.0-nightly.20260822.g5411f113c 发布。该版本更新了 macOS Seatbelt sandbox 以隔离 Docker 和容器运行时套接字及二进制文件。这是针对运行时权限的特定沙盒修复，属于 nightly 构建的次要 bugfix。

github · gemini-cli-robot · 8月22日 01:10

**「设计要点」** macOS Seatbelt sandbox 已更新以隔离 Docker 和容器运行时套接字及二进制文件。这涉及运行时权限管理。

**「改了什么」** 本次发布修复了 macOS Seatbelt sandbox 以隔离 Docker 和容器运行时套接字和二进制文件。相比上一版 v0.56.0-nightly.20260821.g30573d2e4，这是针对沙盒隔离的变更。

**标签**: `#sandbox`, `#runtime`, `#permissions`

---

## Agent 工程师日报

<a id="item-agent-engineer-1"></a>
### [NVIDIA AVO 100% 完成 ARC-AGI-3](https://www.reddit.com/r/LocalLLaMA/comments/1vuh7to/nvidia_avo_got_100_on_arcagi3_it_completed_all/) ⭐️ 9.0/10

NVIDIA AVO 在 ARC-AGI-3 上取得了 100% 的分数。它在所有 25 个公开环境中独立完成了 183 个关卡，没有任何指令、明确规则或目标陈述。这对 AI 代理的推理、评估和开发工作流程产生了重大影响。

reddit · r/LocalLLaMA · /u/theologi · 8月21日 14:01

**「为什么重要」** 这一自主完成所有关卡的结果突显了代理在无指导下解决复杂任务的能力，对代理评估和开发具有重要意义。

**「可关注」** 可关注：NVIDIA AVO 在无指令、无明确规则、无目标陈述的情况下完成 ARC-AGI-3 所有 183 关。

**标签**: `#eval`, `#coding-agent`, `#orchestration`, `#memory`, `#harness`

---

<a id="item-agent-engineer-2"></a>
### [Felony Bench 聚合 AI 代理法律案例](https://www.felonybench.com/) ⭐️ 7.0/10

Felony Bench 聚合了 AI 代理造成第三方法律或安全伤害的真实案例，突出了责任问题和更好的代理护栏需求。它跟踪了第三方妥协的真实世界 AI 代理事件，例如 CFAA 违反。这直接影响 harness 设计、权限控制、评估基准和编排安全保障。

hackernews · colinprince · 8月21日 15:17 · [社区讨论](https://news.ycombinator.com/item?id=49389430)

**「为什么重要」** Felony Bench 提供了 AI 代理引发第三方损害的实际案例，这对 harness 设计和安全保障具有参考价值。目前这些案例主要用于评估代理行为，但尚未证实其对实际部署的影响。

**「可关注」** 可关注：AI 代理在运行时可能导致 CFAA 等法律问题，需要关注权限控制和编排安全。

**「评论」** 社区讨论中，有人质疑 Felony Bench 名称的准确性，认为“无意中”损害难以证明恶意意图。另有讨论焦点在责任归属上，如用户、模型主机还是开发者。

**标签**: `#harness`, `#permissions`, `#eval`, `#orchestration`, `#coding-agent`

---

<a id="item-agent-engineer-3"></a>
### [Claudette: 让 Claude 停止 BuzzFeed 风格输出](https://github.com/adnanakil/nobuzz/blob/main/README.md) ⭐️ 7.0/10

Claudette 是一个 GitHub 工具，使用针对性指令让 Claude 生成简洁、非 BuzzFeed 风格的响应。它通过提示词工程清理 Claude 的冗长输出，直接适用于代理 harness 和评估。影响对象包括 coding agent 和 harness 开发者。目前是社区工具，尚未有官方 Anthropic 回应具体风格问题。

hackernews · aakil · 8月21日 14:31 · [社区讨论](https://news.ycombinator.com/item?id=49388752)

**「为什么重要」** Claudette 工具的发布反映了用户对 Claude 输出风格的普遍不满，这在代理 harness 开发中尤为重要。已发生的是工具的开发，尚未证实其对实际交互的影响。

**「可关注」** 可关注：限制输出词数是清理 Claude 输出最强的因素。

**「评论」** 社区用户反馈使用 Claudette 指令后输出更清晰明确。有人认为这是 Claude 产品风格问题的表现，也有人认为用户已适应。相关工作包括 Vomit 工具。

**标签**: `#harness`, `#eval`, `#coding-agent`, `#orchestration`

---

<a id="item-agent-engineer-4"></a>
### [自托管沙箱代理软件工厂构建](https://blog.jakesaunders.dev/building-an-almost-fully-self-hosted-sandboxed-agentic-software-factory/) ⭐️ 7.0/10

Hacker News 发布了博客文章，标题为“Building an \(almost\) fully self-hosted, sandboxed, agentic software factory”，作者是 jakelsaunders94。该文章描述了构建一个几乎完全自托管、沙箱化的代理软件工厂的过程，涉及编排、验证循环和自托管挑战。该系统对 coding-agent 架构、harnesses 和 evals 具有相关性，但具体细节仅限于标题和元数据。

hackernews · jakelsaunders94 · 8月21日 16:27 · [社区讨论](https://news.ycombinator.com/item?id=49390463)

**「为什么重要」** 该博客文章的发布为自托管沙箱代理软件工厂提供了参考，但其在实际生产环境中的影响尚未证实。

**「可关注」** 可关注：自托管沙箱代理软件工厂在验证循环和编排方面的工程挑战。

**「评论」** 社区讨论中，用户指出验证是生产系统的关键难点，代理验证自身假设可能不足。有人提到自托管 GPU 运行 coding 模型的结果不佳，并分享了类似自建工厂的经历。

**标签**: `#coding-agent`, `#orchestration`, `#harness`, `#permissions`, `#eval`

---

<a id="item-agent-engineer-5"></a>
### [DeepSeek Harness v0.1.1 发布](https://www.reddit.com/r/LocalLLaMA/comments/1vugyfe/deepseek_harness_v011_released/) ⭐️ 7.0/10

DeepSeek Harness v0.1.1 发布，增强了适配器的多模态能力和图像处理功能。该版本新增了多模态视觉理解模型 DeepSeek-V4-Flash-Vision-Exp，并支持原生图像请求配置。/goal 和 /plan 等命令可接受文本和图像输入，@菜单可引用文件和会话，MCP/ACP 支持持久图像附件，PTC 模式支持嵌套图像转发。

reddit · r/LocalLLaMA · /u/Fun-Doctor6855 · 8月21日 13:51

**「为什么重要」** 此版本发布为多模态代理 Harness 提供了图像处理支持，已发生的功能增强值得关注。

**「可关注」** 可关注：PTC 模式支持嵌套图像转发和 MCP/ACP 的持久图像附件。

**标签**: `#harness`, `#mcp`, `#orchestration`, `#coding-agent`, `#vision`

---

<a id="item-agent-engineer-6"></a>
### [Simile AI：模拟成新 Scaling Law](https://www.latent.space/p/simile) ⭐️ 6.0/10

Latent Space 对 Simile AI CEO Joon Sung Park 进行了采访。他从病毒式传播的生成代理转向创建每个活生人类的 80 亿个数字孪生，并将模拟视为新的 Scaling Law。这标志着该公司从有趣的探索转向严肃的商业领域。这将影响从事生成代理、内存和编排的 AI Agent 工程师。

rss · Latent Space · 8月21日 23:37

**「为什么重要」** 采访强调模拟作为生成代理的新 Scaling Law，可能影响代理的内存和编排设计，但目前缺乏技术细节和基准测试，实际影响尚未证实。

**「可关注」** 可关注：Simile AI CEO 表示模拟将成为生成代理的新 Scaling Law，这标志着从病毒式探索到严肃业务的转变。

**标签**: `#orchestration`, `#memory`, `#eval`, `#simulation`, `#coding-agent`

---

## AI 日报

<a id="item-ai-daily-1"></a>
### [Anthropic IPO 文件显示 AI 反弹风险](https://news.google.com/rss/articles/CBMiogFBVV95cUxNeXdwbzNJcERVMTFvY2JtSkNBMUVaWGpSNlRqYXM1MndRT0lFOWw0NFpURjU4aVFZeTZvdjNRRWs0VWNaWXhzTXQ1QlJ4eUEwR2FXdl9Ca2xIQzVwQmgteVVLRkZneTlHMUt1dXJWNGk3UWladzNVQWZRc3ZpRFlQR2xTbGZLdGlRZzF2RWRvTk5CcVJQM19ZZlA1U2tCN1lkRkHSAacBQVVfeXFMTXQtbkxtMGJVQ0lSUjgwcG1EUFZkb1pWRjY4czE4M3NlQ1RsVWtWOVBESjM2SllMby1jN2haVy1wMWYxR2FnSFpwOUhKT180bVpRTzlETERmYjVQdE1SYjBiYXc0VzRRQnVSUC10Z2lpc0FqZlJibF8waTdOSndRa091YXZwUkRSWnlxbEI3NTYyeW55a1NkZ2NGVTc4YUM3UHZtQ056aGM?oc=5) ⭐️ 6.0/10

Anthropic 即将提交的 IPO 文件（S-1）将把 AI 反弹列为风险因素。CNBC 援引来源报道称，这一披露将反映公众对 AI 技术的担忧。

google\_news · CNBC · 8月21日 21:44

**「为什么重要」** 这一披露有助于了解 AI 行业面临的公众反弹压力。

**「可关注」** 可关注：Anthropic IPO 文件将 AI 反弹列为风险因素。

**标签**: `#lab`, `#industry`, `#policy`

---

<a id="item-ai-daily-2"></a>
### [OpenAI 呼吁加州加强 AI 法律](https://news.google.com/rss/articles/CBMingFBVV95cUxQT2JQdDFETkdMaENPNG1fVmE3WnpKbnlLLXVSZmo4dXBEZWVsM1pZNXpBWWJmVmNISzlrS01PREF1dDBXYUEtNkZ5MExXX3hHbzBYTzJYVFlxNGtuV2pIMnJ2V1hMdnp5YTd0amt5aktKNFNZNmp6c3VVUEs5V3dwNWlOMldQNGVJbGFJZEFlMlE0SDlZSHpVM2F6VEwzdw?oc=5) ⭐️ 6.0/10

OpenAI 呼吁在加州加强人工智能法律。根据 Politico 报道。这份政策立场来自主要实验室，但未提供原始声明的具体细节。

google\_news · Politico · 8月21日 22:29

**「可关注」** 可关注：OpenAI 呼吁在加州加强人工智能法律

**标签**: `#openai`, `#policy`, `#california`, `#ai\_laws`, `#industry`

---

<a id="item-ai-daily-3"></a>
### [康涅狄格 SB5 法案：AI 州监管趋势](https://news.google.com/rss/articles/CBMiyAFBVV95cUxOU1VlZV9tT3pLWm9KaEZySmxvb2picjkwbGt1UnZrNEdkNkxUaTV1QkNBb0U5bXRRWFFRRUlwVmhUWnFDOUlKSm9QVkdveFp1UWRITXliWGN4dzhJYnU1bFJTNV9JNlkyVUdHRzdlUC13MHJ0U0xyUl9kNnlDUGVGSHpXQ0Jad0FSYlhDU211Y0tMQTdnVTNiTzhqWmdlWDFYQ2VFMHJqSktPa3M5bzdrYU1ETzlaaU5reXhxcHgyNU5mTHBOWFpVTw?oc=5) ⭐️ 6.0/10

Sidley Austin 分析了康涅狄格州的 SB5 法案，作为州 AI 监管趋势的案例研究。该法案是综合 AI 法律。文章提供了政策概述，但没有可验证的新事实或重大模型或实验室发布。

google\_news · Sidley Austin · 8月21日 19:03

**「为什么重要」** 了解康涅狄格州 SB5 法案有助于把握州 AI 监管的最新趋势。

**「可关注」** 可关注：康涅狄格州 SB5 法案作为州 AI 监管趋势的案例研究。

**标签**: `#policy`, `#regulation`, `#industry`

---

<a id="item-ai-daily-4"></a>
### [浙大 BEACON 按里程碑分配信用](https://mp.weixin.qq.com/s?__biz=MzIwMTc4ODE0Mw==&amp;mid=2247722361&amp;idx=2&amp;sn=5a006b50943113b0c6017e795dbada36) ⭐️ 5.0/10

PaperWeekly 发文介绍浙江大学的 Agent 系统 BEACON，标题将其与 ICML 2026 并列，并称长程任务成功率接近翻倍。给定材料里几乎没有实验设置，能核对的方法信息只有「按里程碑分配信用」。翻倍幅度、对比基线和「一步错不再全盘输」都只出现在标题里，这里不当成已核实结果。

rss · PaperWeekly · 8月21日 14:31

**「为什么重要」** 文章把长程失败写成「一步错就全盘输」，对应做法是按里程碑分配信用。这和长程 agent 里中间步骤怎么计分是同一类问题，但材料没有给出可核对的实验数字。

**「可关注」** 可关注：长程轨迹是否按里程碑切分后再分配信用，而不是整条成败一刀切。

**标签**: `#model`, `#lab`, `#industry`

---

<a id="item-ai-daily-5"></a>
### [英国转向蓬勃发展的芯片新贵 支持主权 AI 策略](https://news.google.com/rss/articles/CBMilwFBVV95cUxPbTJaRUhiSVhXZGpxd0lxTGhUdThiWFFfQ1BqRWJLeXl5Z3FmQXJTWURKTDFaQU5OM0N0M1ptcGpleU1KVnVvdFpOYUtjVFUzdV9DSWVnVHcwU0w2b3dBSktkNmhpVVlNS0hDY0hhUmRFRlZvN0phYzZMQ0tKN2tDaFNyN2dfQU81WTJldm9vN0ZvYUh2SXhZ?oc=5) ⭐️ 5.0/10

英国转向小型芯片公司来支持其主权 AI 策略。这些新兴芯片公司正在蓬勃发展。

google\_news · Bloomberg.com · 8月22日 03:32

**「可关注」** 可关注：转向小型芯片公司支持主权 AI 策略。

**标签**: `#policy`, `#industry`, `#ai`

---

<a id="item-ai-daily-6"></a>
### [WSJ：中国 AI 飞跃的幕后人物](https://news.google.com/rss/articles/CBMickFVX3lxTFBjWE5CYjA1SjdibGl2UXJ5cmJkRm43NHZkU29wSTM3Rm9faUFqbTUzdmplcWwwcDFTbE80M3dSNzdXRDJnZVVCc2N6Tlh6M0hwNy1HRXJ6eGJYMDk0ZFN6T3FvRU1ybXhGRFl4bXl4dDRPZw?oc=5) ⭐️ 5.0/10

WSJ 发表文章《The Brains Who Powered China’s Surprising AI Leap》，探讨了中国 AI 进步背后的关键人物和努力。该文章提供了中国 AI 发展的行业叙事，但没有提供直接的模型发布、实验室公告或可验证的政策变化。

google\_news · WSJ · 8月21日 20:21

**标签**: `#industry`, `#china`, `#lab`

---

<a id="item-ai-daily-7"></a>
### [在线主播起诉 Twitch 和 Amazon 生成式 AI 训练](https://news.google.com/rss/articles/CBMimgFBVV95cUxOMzh6dHF3NWtpWktuZkJnNEhRZm5nTnUzMkhMWVcwTzB1NC1RQkZfTERpUXFLcTFMc0FMN3B0aEFsZHpmRHBfWlMwaHFLRHN4NjZfQmNxMWxyQVY0X2Z6Ulowbk9zLS1lRm1yeWl1UUtEaC1uSko0NEZPWlNiN1kySS1IR2pEejE1eVFBeHhPLThib2R2NjNJRmVB?oc=5) ⭐️ 5.0/10

在线主播已起诉 Twitch 和 Amazon，针对生成式 AI 训练。Courthouse News 报道了这一事件。目前尚未提供更多信息。

google\_news · Courthouse News · 8月21日 19:47

**标签**: `#industry`, `#policy`

---

<a id="item-ai-daily-8"></a>
### [犹他大学 SCI 获 2400 万美元 NSF 资助](https://news.google.com/rss/articles/CBMitAFBVV95cUxOYUczbHV3RDhUQXg1dU54NWFYb1pvVEtFRThBOG1MZmlPVUtUU1pBanBGWkVPNGQ0NXM0RDZTZ3FSeGI3QlNyVkNESTNsUVZlTDBnelZRSzM2azVyMkFTSFJPS2pGZkhjUlZFb2JZZ05Kd0JQeU1UVExBclhQbG11ckVOWkt0MnM3ZGo4OUZ5cWdSdEM5RFVsVm8zaDlqYTgtemxQYUVNMWJSR1RobnR2MHFBLTA?oc=5) ⭐️ 5.0/10

犹他大学计算与信息学院（SCI）是美国国家科学基金（NSF）一项 2400 万美元资助项目的参与者。该项目旨在扩展 AI 就绪数据基础设施。

google\_news · The University of Utah · 8月21日 22:32

**「可关注」** 可关注：NSF 资助将扩展 AI 就绪数据基础设施

**标签**: `#lab`, `#policy`, `#industry`, `#infrastructure`

---

## AI 羊毛

<a id="item-ai-deals-1"></a>
### [OpenAI 宣布 GPT-5.6 Sol API 定价降超 20%](https://twitter.com/OpenAI/status/2090885187634905500) ⭐️ 7.0/10

OpenAI 宣布降低 GPT-5.6 Sol 的 API 使用和积分定价，降幅超过 20%。这是官方 Twitter 公告。材料中未提供具体额度、领取条件或截止时间。

rss · HN Free API / Credits · 8月21日 19:39

**「可关注」** 可关注：降低 GPT-5.6 Sol API 和积分定价超过 20%。

**标签**: `#credits`, `#promo`, `#api`

---

<a id="item-ai-deals-2"></a>
### [Ox Alpha 免费领取一周](https://twitter.com/opencode/status/2090544355824038300) ⭐️ 6.0/10

OpenCode 平台上，Ox Alpha 隐形模型本周免费提供。无需配额或注册限制。领取截止到下周。

rss · HN Free API / Credits · 8月21日 15:30

**「可关注」** 可关注：OpenCode 平台上的 Ox Alpha 隐形模型，本周免费领取，无需额外配额或注册限制。

**标签**: `#free-tier`, `#promo`, `#limited-free`, `#api`

---

<a id="item-ai-deals-3"></a>
### [ChillyCapy 离线 AI 文本检测器](https://capytoolkit.com/tools/text/offline-private-ai-text-detector/) ⭐️ 6.0/10

ChillyCapy 发布了离线免费私有的 AI 文本检测器工具。
该工具无需注册或支付墙。

rss · HN Free API / Credits · 8月21日 14:22

**「可关注」** 可关注：离线运行，无需注册或支付墙。

**标签**: `#free-tier`, `#offline`, `#private`, `#ai-tool`, `#no-signup`

---