---
layout: default
title: "Horizon Summary: 2026-09-09 (ZH)"
date: 2026-09-09
lang: zh
---

> 从 178 条内容中筛选出 13 条重要资讯。

---

**Harness 架构**
1. [Claude Code v2.1.265 发布](#item-harness-arch-1) ⭐️ 7.8/10
2. [pydantic-ai v2.41.0 发布](#item-harness-arch-2) ⭐️ 7.8/10
3. [openai-agents-python v0.22.1 发布](#item-harness-arch-3) ⭐️ 7.8/10
4. [openai-agents-js v0.17.1 发布](#item-harness-arch-4) ⭐️ 7.8/10
5. [Goose v1.50.0 发布](#item-harness-arch-5) ⭐️ 6.8/10
6. [Gemini CLI v0.60.0-preview.0 发布](#item-harness-arch-6) ⭐️ 5.8/10
7. [gemini-cli v0.59.0 发布](#item-harness-arch-7) ⭐️ 5.8/10

**Agent 工程师日报**
1. [LlamaGuard-3 政治边界安全](#item-agent-engineer-1) ⭐️ 7.8/10

**AI 日报**
1. [OpenAI 分享 Navier-Stokes 解](#item-ai-daily-1) ⭐️ 7.8/10
2. [OpenAI $5M 青少年研究拨款](#item-ai-daily-2) ⭐️ 7.8/10
3. [OpenAI 发文谈 AI 扩大可完成工作](#item-ai-daily-3) ⭐️ 6.8/10
4. [ChatGPT Images 2.5 发布](#item-ai-daily-4) ⭐️ 6.8/10
5. [GPT-5.6 Sol 助力量子计算实验](#item-ai-daily-5) ⭐️ 5.8/10

---

## Harness 架构

<a id="item-harness-arch-1"></a>
### [Claude Code v2.1.265 发布](https://github.com/anthropics/claude-code/releases/tag/v2.1.265) ⭐️ 7.8/10

Claude Code v2.1.265 发布。新增指向插件文件夹的 --plugin-dir 参数，支持动态加载子文件夹中的插件。修复了子代理重启时工具列表和系统提示前缀变化导致的提示缓存复用失败问题，并限制了工具结果保存到磁盘的 1GB 大小。

github · ashwin-ant · 9月8日 20:37

**「改了什么」** v2.1.265 增加了指向插件文件夹的 --plugin-dir 支持，并限制了工具结果保存到磁盘的 1GB 大小。修复了子代理和代理队友在重启或切换时提示缓存复用失败的问题，并改进了远程控制、VSCode 集成和多个其他 bug。

**标签**: `#runtime`, `#subagents`, `#prefix-cache`, `#tools`, `#sandbox`

---

<a id="item-harness-arch-2"></a>
### [pydantic-ai v2.41.0 发布](https://github.com/pydantic/pydantic-ai/releases/tag/v2.41.0) ⭐️ 7.8/10

pydantic-ai v2.41.0 发布。ImageGeneration 和 XSearch 工具上废弃 fallback\_model，改为 fallback\_subagent\_model，同时新增 ImageGenerator 直接图像生成 API。添加 openai-codex 提供商支持，并修复 Anthropic 原生搜索报告和 Bedrock 错误。

github · dsfaccini · 9月8日 04:15

**「改了什么」** 废弃 fallback\_model 引入 fallback\_subagent\_model 到 ImageGeneration 和 XSearch。新增 ImageGenerator API 和 openai-codex 提供商。修复 Anthropic 搜索报告和 Bedrock 错误。

**标签**: `#subagents`, `#tools`, `#runtime`

---

<a id="item-harness-arch-3"></a>
### [openai-agents-python v0.22.1 发布](https://github.com/openai/openai-agents-python/releases/tag/v0.22.1) ⭐️ 7.8/10

openai-agents-python v0.22.1 发布。该版本新增了网页搜索工具的图像结果支持、MCP 工具的服务器级防护栏以及 Unix 本地沙箱隔离配置等功能。同时支持 Docker 容器标签和流式转录选项，并修复了核心使用和工具参数的多个问题。

github · seratch · 9月8日 09:18

**「改了什么」** 相比上一版，v0.22.1 增加了网页搜索工具的图像结果支持、MCP 工具的服务器级防护栏以及 Unix 本地沙箱隔离配置等新能力，并修复了多个核心使用和工具参数问题。

**标签**: `#mcp`, `#sandbox`, `#tools`, `#runtime`, `#guardrails`

---

<a id="item-harness-arch-4"></a>
### [openai-agents-js v0.17.1 发布](https://github.com/openai/openai-agents-js/releases/tag/v0.17.1) ⭐️ 7.8/10

openai-agents-js v0.17.1 发布了服务器范围的 MCP 工具防护功能、Docker 沙箱容器的标签支持以及网页搜索工具的图片结果增强。此外，修复了审批会话恢复、会话写入和 Chat Completions 工具回放等多个运行时问题。

github · seratch · 9月8日 10:04

**「改了什么」** 相比 v0.17.0，v0.17.1 增加了服务器范围的 MCP 工具防护功能和 Docker 沙箱容器的标签支持。还支持了网页搜索工具的图片结果。

**标签**: `#mcp`, `#sandbox`, `#runtime`, `#tools`, `#permissions`

---

<a id="item-harness-arch-5"></a>
### [Goose v1.50.0 发布](https://github.com/aaif-goose/goose/releases/tag/v1.50.0) ⭐️ 6.8/10

Goose v1.50.0 发布。新增 GPT-6 Astra 模型支持和 goose-agent 工具调用功能。子代理平台强制执行和权限管理修复。Kotlin 调用者可配置 Databricks AI Gateway 路径。

github · github-actions\[bot\] · 9月8日 19:32

**「改了什么」** v1.50.0 相比上一版真正增加了 GPT-6 模型支持和工具调用能力。子代理平台守卫和权限管理得到强化。

**标签**: `#subagents`, `#permissions`, `#tools`, `#runtime`

---

<a id="item-harness-arch-6"></a>
### [Gemini CLI v0.60.0-preview.0 发布](https://github.com/google-gemini/gemini-cli/releases/tag/v0.60.0-preview.0) ⭐️ 5.8/10

Google Gemini CLI v0.60.0-preview.0 发布。该预览版本对 sandbox 和 MCP OAuth 进行了更新，包括 web fetch 工具的连接路由改进、MCP OAuth 的 RFC 9207 发行者识别强制执行，以及 macOS Seatbelt sandbox 的隔离。

github · gemini-cli-robot · 9月8日 21:04

**「设计要点」** macOS Seatbelt sandbox 隔离临时目录和设置目录，提升运行时安全边界检查。

**「改了什么」** 相比 v0.59.0-preview.0，修复了 web fetch 路由验证和 MCP OAuth 的 RFC 9207 合规，同时强化了扩展加载器的路径边界验证。

**标签**: `#sandbox`, `#mcp`, `#runtime`, `#extensions`, `#tools`

---

<a id="item-harness-arch-7"></a>
### [gemini-cli v0.59.0 发布](https://github.com/google-gemini/gemini-cli/releases/tag/v0.59.0) ⭐️ 5.8/10

gemini-cli v0.59.0 发布了补丁版本，修复了 MCP 认证的安全漏洞和受限模式下工作空间信任的问题。主要更新包括防止 MCP OAuth 中的 SSRF 攻击，以及在受限模式下过滤 mcpServers。

github · gemini-cli-robot · 9月8日 21:13

**「改了什么」** 相对于 v0.58.0，修复了 MCP OAuth 元数据发现和认证中的 SSRF 漏洞，并强制实施受限模式下的工作空间信任和 mcpServers 过滤。

**标签**: `#mcp`, `#permissions`, `#sandbox`, `#runtime`

---

## Agent 工程师日报

<a id="item-agent-engineer-1"></a>
### [LlamaGuard-3 政治边界安全](https://huggingface.co/blog/MultiverseComputingCAI/safety-for-whom) ⭐️ 7.8/10

Hugging Face 博客发布论文《Safety for Whom? Boundary-Aware Self-Distillation for Controlled LLM Safety Refusal》，指出真实部署需在同一话题内拒绝特定子集，而非整个话题。LlamaGuard-3 无法区分政治操纵请求与事实信息。Qwen3-8B 模型在政治拒绝率从 9.47% 提升至 84.75%，但 XSTest 过拒率从 2% 升至 74%。通过边界对数据，过拒率降至 4.16%，几乎不损失安全增益。

rss · Hugging Face Blog · 9月8日 14:23

**「为什么重要」** 该研究对真实部署至关重要，因为同一话题下不同设置需要不同边界。论文已展示通过边界数据可精确控制权衡，已验证可降低过拒率。

**「可关注」** 可关注：仅评估有害拒绝率无法反映边界形状，需同时测量合规侧的过拒率。

**标签**: `#harness`, `#eval`, `#permissions`, `#orchestration`, `#coding-agent`

---

## AI 日报

<a id="item-ai-daily-1"></a>
### [OpenAI 分享 Navier-Stokes 解](https://openai.com/index/navier-stokes-solution) ⭐️ 7.8/10

OpenAI 分享了 Navier–Stokes 千年大奖问题的 AI 生成解决方案。

解决方案包含写上和 Lean 形式证明。

目前未提供更多信息。

rss · OpenAI Blog · 9月8日 10:00

**标签**: `#model`, `#lab`, `#open-source`, `#math`

---

<a id="item-ai-daily-2"></a>
### [OpenAI $5M 青少年研究拨款](https://openai.com/index/teen-development-research-grants) ⭐️ 7.8/10

OpenAI 推出 500 万美元拨款，支持独立研究生成式 AI 对青少年发展、福祉和安全的影响。
申请者可提交提案。

rss · OpenAI Blog · 9月8日 09:00

**「可关注」** 可关注：OpenAI 提供 500 万美元拨款支持独立研究生成式 AI 对青少年发展、福祉和安全的影响。

**标签**: `#openai`, `#policy`, `#ai-safety`, `#teen-development`, `#grant`

---

<a id="item-ai-daily-3"></a>
### [OpenAI 发文谈 AI 扩大可完成工作](https://openai.com/index/the-work-now-within-reach) ⭐️ 6.8/10

OpenAI 发布博客 The Work Now Within Reach。导语称，更强、更便宜的 AI 能扩大个人和企业可完成的工作，并让增长更经济。可见材料没有新模型、数字、基准或产品细节。

rss · OpenAI Blog · 9月8日 13:00

**标签**: `#openai`, `#industry`, `#product`

---

<a id="item-ai-daily-4"></a>
### [ChatGPT Images 2.5 发布](https://openai.com/index/introducing-chatgpt-images-2-5) ⭐️ 6.8/10

OpenAI 发布了 ChatGPT Images 2.5。ChatGPT Images 2.5 帮助用户将想法、草图和参考照片转化为更个性化的、精致的图像。这些图像能更好地反映用户的想法。

rss · OpenAI Blog · 9月8日 11:30

**「为什么重要」** ChatGPT Images 2.5 的发布让用户能更轻松地创建个性化图像。

**「可关注」** 可关注：ChatGPT Images 2.5 支持从用户想法、草图和参考照片生成更个性化的图像。

**标签**: `#openai`, `#chatgpt`, `#product`, `#model`

---

<a id="item-ai-daily-5"></a>
### [GPT-5.6 Sol 助力量子计算实验](https://openai.com/index/codex-quantum-computing-experiments) ⭐️ 5.8/10

MIT 研究员使用 GPT-5.6 Sol 与 Codex 自主运行量子计算实验，分析结果并校准量子比特。该过程由 OpenAI 官方博客介绍，属于高层次 teaser，未提供具体技术细节、指标或对比基线。

rss · OpenAI Blog · 9月8日 17:00

**「为什么重要」** 量子计算实验自动化有助于加速科研进程。材料为官方博客 teaser。

**「可关注」** 可关注：MIT 研究员使用 GPT-5.6 Sol 与 Codex 自主运行量子计算实验。

**标签**: `#model`, `#lab`, `#industry`, `#product`

---