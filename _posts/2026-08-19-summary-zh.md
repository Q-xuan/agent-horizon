---
layout: default
title: "Horizon Summary: 2026-08-19 (ZH)"
date: 2026-08-19
lang: zh
---

> 从 105 条内容中筛选出 19 条重要资讯。

---

**Harness 架构**
1. [pydantic-ai v2.32.0 发布](#item-harness-arch-1) ⭐️ 7.0/10
2. [Agent Framework dotnet-1.18.0 发布](#item-harness-arch-2) ⭐️ 7.0/10
3. [Codex rust-v0.148.0 发布](#item-harness-arch-3) ⭐️ 6.0/10
4. [Cline desktop-v0.0.14 发布](#item-harness-arch-4) ⭐️ 6.0/10
5. [Gemini CLI v0.56.0-nightly.20260819.g571851b10 发布](#item-harness-arch-5) ⭐️ 5.0/10
6. [langchain-openai 1.5.2 发布](#item-harness-arch-6) ⭐️ 5.0/10
7. [Claude Code 2.1.235 发布](#item-harness-arch-7) ⭐️ 5.0/10

**Agent 工程师日报**
1. [Qwen3.8-27B 2x 3090 vLLM DFlash2 218 tok/s](#item-agent-engineer-1) ⭐️ 8.0/10
2. [DeepSeek V4 Flash Q4\_K\_XL 4× RTX 3060 ~100 tok/s 提示处理](#item-agent-engineer-2) ⭐️ 7.0/10
3. [Palomar：Lean 验证数学注册表](#item-agent-engineer-3) ⭐️ 6.0/10
4. [Turbovec：Rust TurboQuant 向量搜索](#item-agent-engineer-4) ⭐️ 6.0/10
5. [ALTK-Evolve：Agent 内存剂量因模型能力而异](#item-agent-engineer-5) ⭐️ 6.0/10
6. [XuanTie C950 运行 Qwen-3.8 27B 模型](#item-agent-engineer-6) ⭐️ 6.0/10

**AI 日报**
1. [OpenAI 加强国家安全民主监督](#item-ai-daily-1) ⭐️ 8.0/10
2. [ChatGPT Ads 扩展至欧洲 31 个市场](#item-ai-daily-2) ⭐️ 7.0/10
3. [OpenAI 加强前沿模型监控 指导开发节奏](#item-ai-daily-3) ⭐️ 7.0/10
4. [OpenAI 推出 ChatGPT for Teens](#item-ai-daily-4) ⭐️ 7.0/10
5. [哈工大开源自进化 GUI Agent，用过一次学会](#item-ai-daily-5) ⭐️ 6.0/10
6. [Claude 加速蛋白设计与分析化学](#item-ai-daily-6) ⭐️ 6.0/10

---

## Harness 架构

<a id="item-harness-arch-1"></a>
### [pydantic-ai v2.32.0 发布](https://github.com/pydantic/pydantic-ai/releases/tag/v2.32.0) ⭐️ 7.0/10

pydantic-ai v2.32.0 发布了。该版本更新了 instrumentation 协议至版本 6，tool results 现在以 role: &\#x27;tool&\#x27; 格式发出。同时，同步 hooks 和工具在线程池中运行，并强制执行 timeout。还支持了 xAI 附件搜索和 OpenRouter web-search 来源。

github · dsfaccini · 8月19日 03:51

**「设计要点」** 运行时 instrumentation 版本更新为 6，tool results 现在在 role: &\#x27;tool&\#x27; 下发出。同步工具和 hooks 使用线程池处理，并强制 timeout。

**「改了什么」** 相比 v2.31.1，新增 instrumentation 版本 6 和 sync hooks 线程池支持。添加了 xAI 提供商集成和 OpenRouter 来源。

**标签**: `#runtime`, `#tools`, `#instrumentation`, `#hooks`

---

<a id="item-harness-arch-2"></a>
### [Agent Framework dotnet-1.18.0 发布](https://github.com/microsoft/agent-framework/releases/tag/dotnet-1.18.0) ⭐️ 7.0/10

Microsoft Agent Framework .NET 1.18.0 版本已发布。该版本更新了运行时、工具、内存和权限方面的内容，涉及多个 PR。版本号更新为 1.18.0，包含任务存储隔离键作用域、工具批准循环边界、文件技能发现硬化、对话历史聚合以及 Cosmos NoSQL 向量内存样本等改进，并有重命名 AgentIsolationKeyProvider 的 breaking change。

github · SergeyMenshykh · 8月18日 14:30

**「改了什么」** 相比 1.17.0，此次发布真正增加了任务存储隔离键作用域支持、工具批准循环边界、文件技能发现硬化、托管代理对话历史单一来源以及函数调用存储。还包括 Cosmos 向量内存样本和重命名 AgentIsolationKeyProvider 的 breaking change。

**标签**: `#runtime`, `#tools`, `#memory`, `#permissions`, `#subagents`

---

<a id="item-harness-arch-3"></a>
### [Codex rust-v0.148.0 发布](https://github.com/openai/codex/releases/tag/rust-v0.148.0) ⭐️ 6.0/10

OpenAI Codex TUI 发布了 rust-v0.148.0 版本。该版本新增了会话管理功能，包括使用 codex exec fork 进行会话 fork，以及从 TUI 恢复选择器中归档和恢复会话。还添加了对 Amazon Bedrock Runtime 提供商的支持，支持 AWS 配置文件、区域和 GPT-5.6 路由。新增了 MCP 工具钩子和异步命令钩子支持，以及 /export 命令将对话导出为 Markdown。

github · github-actions\[bot\] · 8月18日 22:26

**「改了什么」** 相比上一版 rust-v0.147.0，主要新增了会话 fork、归档恢复功能，支持 Amazon Bedrock 提供商，添加了异步命令钩子和 MCP 工具调用支持，以及 Markdown 对话导出功能。修复了模型切换导致的 stale instructions 问题和会话恢复时的 cwd 持久化以及 approval policy 恢复等 bug。

**标签**: `#runtime`, `#tools`, `#mcp`, `#memory`, `#permissions`

---

<a id="item-harness-arch-4"></a>
### [Cline desktop-v0.0.14 发布](https://github.com/cline/cline/releases/tag/desktop-v0.0.14) ⭐️ 6.0/10

Cline 桌面版 v0.0.14 发布了。它添加了 macOS 通知、实时命令流式输出（支持颜色和后台选项）、语音输入、内联图像生成，以及可折叠的运行总结。

github · github-actions\[bot\] · 8月19日 06:18

**「改了什么」** 相比 v0.0.13，主要新增了实时命令流式输出、后台执行、内联图像渲染和语音输入等功能。修复了会话流式输出、命令执行和 Gemini base URL 的问题。

**标签**: `#runtime`, `#tools`, `#planning`

---

<a id="item-harness-arch-5"></a>
### [Gemini CLI v0.56.0-nightly.20260819.g571851b10 发布](https://github.com/google-gemini/gemini-cli/releases/tag/v0.56.0-nightly.20260819.g571851b10) ⭐️ 5.0/10

Gemini CLI 的 nightly 版本 v0.56.0-nightly.20260819.g571851b10 发布。针对 SSR Agent 修复了子代理行为和相关 UI 问题，包括子代理运行控制、handoff token 修复以及终端 rerender 等。

github · gemini-cli-robot · 8月19日 01:07

**「改了什么」** 相比上一版，修复了 SSR Agent 的子代理行为和 UI 问题。包括防止代理模式禁用时子代理运行、修复启动时的 sub-agent handoff token 回归、终端退出外部编辑器后强制 rerender 缓冲区以及自动补全建议添加空格等。

**标签**: `#subagents`, `#runtime`

---

<a id="item-harness-arch-6"></a>
### [langchain-openai 1.5.2 发布](https://github.com/langchain-ai/langchain/releases/tag/langchain-openai%3D%3D1.5.2) ⭐️ 5.0/10

langchain-openai 1.5.2 发布了 OpenAI 集成的小版本更新。修复了 o-series 模型在 get\_num\_tokens\_from\_messages 中的 token counting 支持，并保留了 reasoning item boundaries。增加了从响应头提取 gateway metadata 的功能。

github · github-actions\[bot\] · 8月18日 17:38

**「改了什么」** 相对上一版 1.5.1，1.5.2 修复了 reasoning item boundaries 的保留问题，并支持了 o-series 模型在 get\_num\_tokens\_from\_messages 中的 token 计算。

**标签**: `#runtime`, `#eval`, `#planning`

---

<a id="item-harness-arch-7"></a>
### [Claude Code 2.1.235 发布](https://code.claude.com/docs/en/changelog#2-1-235) ⭐️ 5.0/10

Claude Code 2.1.235 给提示输入加了可选 \`spellcheck\`，用本机已装的 aspell、hunspell 或 ispell 给拼错的词加下划线。语言服务器中途断开或重连时，不再整段失效 prompt cache。Agent 工具在当前会话没有 general-purpose agent 时，省略 \`subagent\_type\` 会报错并列出可用 agent，而不是广告一个不可用的默认。权限对话框的文案和「don&\#x27;t ask again」与实际授权范围对齐；Shift+Tab 在权限提示的 comment 字段里不再误批编辑并授予整场 session 的编辑权限。

rss · Claude Code Changelog · 8月18日 22:28

**「设计要点」** Agent 工具省略 \`subagent\_type\` 时，若当前会话没有 general-purpose agent，会报错并列出可用 agent，不再走不可用的默认。权限对话框的展示范围与「don&\#x27;t ask again」和实际授权对齐，内容显示不全时不提供「don&\#x27;t ask again」；语言服务器断连不再整段失效 prompt cache，云端会话（如 \`/ultrareview\`、\`/autofix-pr\`）的事件流也不再每次更新都重扫重渲染。

**「改了什么」** 相对上一版，唯一新增能力是可选 \`spellcheck\` 设置。其余是 prompt cache、权限提示、Agent 默认、终端 UI、嵌入式 grep、跨会话 \`SendMessage\` 体积检查和 \`claude rc\` enterprise-gateway 校验的针对性修复。

**标签**: `#permissions`, `#subagents`, `#runtime`, `#tools`

---

## Agent 工程师日报

<a id="item-agent-engineer-1"></a>
### [Qwen3.8-27B 2x 3090 vLLM DFlash2 218 tok/s](https://www.reddit.com/r/LocalLLaMA/comments/1vsccit/qwen3827b_on_2x_3090_vllm_dflash2_218_toks_single/) ⭐️ 8.0/10

Qwen3.8-27B 在 2× RTX 3090 上使用 vLLM + DFlash2 实现了单请求吞吐量 218 tok/s。使用 Club-3090 基准测试套件测试，prefill 速度 1342 tok/s（10k 上下文）和 628 tok/s（90k 上下文），spec-decode 7 draft tokens 接受长度 3.35 接受率 47.8%。峰值 VRAM 22.3 GB/卡，支持上下文上限 131k（DFlash2 drafter 约占 13.5 GB）。堆栈为 2× RTX 3090（PCIe Gen4 x16/x16，无 NVLink），vLLM v0.26.1rc1 + AutoRound INT4（group 128）+ DFlash2，并进行了自定义 vLLM 补丁。这对本地推理 harness、内存管理和 coding-agent 编排有直接影响。

reddit · r/LocalLLaMA · /u/xjx546 · 8月19日 04:39

**「为什么重要」** 材料展示了 Qwen3.8-27B 在消费级 2x 3090 硬件上通过 vLLM + DFlash2 实现 218 tok/s 单请求吞吐的 benchmark，已发生的变化是具体测试数据。尚未证实的影响是是否能在多请求或不同硬件上验证。

**「可关注」** 可关注：Qwen3.8-27B 在 2x 3090 上通过 vLLM + DFlash2 实现了 218 tok/s 单请求吞吐，支持 131k 上下文。

**标签**: `#harness`, `#memory`, `#orchestration`, `#coding-agent`, `#eval`

---

<a id="item-agent-engineer-2"></a>
### [DeepSeek V4 Flash Q4\_K\_XL 4× RTX 3060 ~100 tok/s 提示处理](https://www.reddit.com/r/LocalLLaMA/comments/1vrqf4f/running_deepseek_v4_flash_q4_k_xl_at_100_toks/) ⭐️ 7.0/10

用户在 4× RTX 3060 12GB 上运行 DeepSeek-V4-Flash-0731 UD-Q4\_K\_XL GGUF 模型，上下文窗口 368640 tokens，使用 llama.cpp 实现 99.4 tok/s 提示处理和 10.1 tok/s 生成。配置使用 -ncmoe 34 专家层放置和 -ot 显式张量分割，-ub 2048 微批大小是关键性能提升。模型约 144 GiB，KV cache Q8\_0，未完全填充上下文窗口，速度为配置容量。

reddit · r/LocalLLaMA · /u/syscomua · 8月18日 14:15

**「为什么重要」** 此配置在消费级多 GPU 硬件上实现了大 MoE 模型长上下文高效推理，对于 coding agent harness 处理超长提示有实际参考意义。相比 -ub 1024 配置的 63.4 tok/s，速度有显著提升。

**「可关注」** 可关注：通过 -ncmoe 34 和 -ot 张量放置策略，可在 4× RTX 3060 上管理大模型 VRAM 余量，并使用 -ub 2048 提升提示处理至约 100 tok/s。

**标签**: `#harness`, `#orchestration`, `#memory`, `#coding-agent`

---

<a id="item-agent-engineer-3"></a>
### [Palomar：Lean 验证数学注册表](https://terrytao.wordpress.com/2026/08/18/palomar-a-registry-of-lean-verified-mathematics/) ⭐️ 6.0/10

Terry Tao 在博客上发布了 Palomar，这是一个 Lean 验证数学的注册表，由 GitHub 快照组成。Palomar 注册了符合当前最佳实践的 Lean 代码的 GitHub 仓库或特定提交快照。2026 年 8 月 18 日的公告影响了形式化数学社区，特别是数学代理评估和 harness 的开发者。

hackernews · matt\_d · 8月19日 02:41 · [社区讨论](https://news.ycombinator.com/item?id=49355968)

**「为什么重要」** Palomar 的发布为 Lean 数学形式化提供了集中注册，这在数学代理评估和 harness 开发中可能相关。已发生的是 Terry Tao 的公告，尚未证实其对整个领域的广泛影响。

**「可关注」** 可关注：提交 Palomar 注册的过程是彻底但可实现的。

**「评论」** 社区将 Palomar 视为 Lean 证明的 preprint server 类似物。有人指出 Lean 重新发明了 Isabelle 的 AFP，且验证证明本身存在递归问题。

**标签**: `#eval`, `#harness`, `#coding-agent`, `#memory`, `#orchestration`

---

<a id="item-agent-engineer-4"></a>
### [Turbovec：Rust TurboQuant 向量搜索](https://github.com/RyanCodrai/turbovec) ⭐️ 6.0/10

Turbovec 是 Google TurboQuant 的 Rust 向量搜索实现。Hacker News 帖子宣布了该库的发布，社区讨论了其内存效率、基准测试和潜在 SQLite 集成。用户提到 4GB 可存储 1000 万文档。

hackernews · fittingopposite · 8月18日 18:07 · [社区讨论](https://news.ycombinator.com/item?id=49349898)

**「为什么重要」** 该库的内存效率使其在向量搜索领域更具竞争力。SQLite 绑定计划将使其集成到现有系统中更加容易。

**「可关注」** 可关注：4GB 存储 1000 万文档的内存效率。

**「评论」** 社区讨论中，用户高度赞扬了 Turbovec 的内存效率，并期待 SQLite 绑定。有人指出 FAISS 不再是 SoTA，并分享了向量压缩的实验。

**标签**: `#memory`, `#eval`, `#orchestration`, `#coding-agent`

---

<a id="item-agent-engineer-5"></a>
### [ALTK-Evolve：Agent 内存剂量因模型能力而异](https://huggingface.co/blog/ibm-research/altk-evolve-hmm) ⭐️ 6.0/10

ALTK-Evolve 方法从代理轨迹中提炼行为指南，并在推理时注入，无需权重更新。评估八个模型在 AppWorld 基准发现，代理内存剂量需根据模型能力模式校准：强模型（如 DeepSeek-V3.2）全指南集提升任务完成率 9.5pp，弱模型（如 gpt-oss-120b）精选检索提升 16.1pp，饱和模型（如 GLM-5）无增益。影响代理工作流，强调内存校准而非一刀切。

rss · Hugging Face Blog · 8月18日 18:09

**「为什么重要」** 研究已观察到代理内存剂量需按模型能力模式校准，但其在生产环境中的实际影响尚未证实。

**「可关注」** 可关注：弱模型采用 curated retrieval 策略可实现 16.1pp 任务完成率提升且仅增加 5% tokens。

**标签**: `#memory`, `#eval`, `#orchestration`, `#coding-agent`

---

<a id="item-agent-engineer-6"></a>
### [XuanTie C950 运行 Qwen-3.8 27B 模型](https://www.reddit.com/r/LocalLLaMA/comments/1vs0wsl/alibabas_riscv_cpu_xuantie_c950_runs_qwen38_27b/) ⭐️ 6.0/10

Alibaba 的 XuanTie C950 RISC-V CPU 运行 Qwen-3.8 27B 模型达到 30 tokens per second。

reddit · r/LocalLLaMA · /u/DeltaSqueezer · 8月18日 20:24

**「为什么重要」** 这一 CPU 基准值得今天阅读，因为它提供了 RISC-V 架构在 LLM 推理上的新数据。

**「可关注」** 可关注：XuanTie C950 在运行 27B 模型时达到 30 tps。

**标签**: `#coding-agent`, `#harness`, `#eval`, `#orchestration`

---

## AI 日报

<a id="item-ai-daily-1"></a>
### [OpenAI 加强国家安全民主监督](https://openai.com/index/strengthening-democratic-oversight-in-national-security) ⭐️ 8.0/10

OpenAI 推出了加强国家安全领域 AI 民主监督的倡议。该倡议支持政府机构使用工具、培训和专业知识。

rss · OpenAI Blog · 8月18日 19:00

**「可关注」** 可关注：OpenAI 支持政府机构使用工具、培训和专业知识来加强 AI 在国家安全领域的民主监督。

**标签**: `#lab`, `#policy`, `#product`

---

<a id="item-ai-daily-2"></a>
### [ChatGPT Ads 扩展至欧洲 31 个市场](https://openai.com/index/chatgpt-ads-expands-across-europe) ⭐️ 7.0/10

OpenAI 将 ChatGPT Ads 扩展到 31 个欧洲市场。广告商可以接触到人们探索、比较选项和做出决策时的人。官方博客发布了这一公告。

rss · OpenAI Blog · 8月18日 22:00

**「为什么重要」** ChatGPT Ads 扩展至欧洲 31 个市场，让广告商有机会触达更多潜在客户。

**「可关注」** 可关注：ChatGPT Ads 扩展至 31 个欧洲市场，广告商可接触探索、比较和决策的用户。

**标签**: `#model`, `#lab`, `#product`, `#industry`

---

<a id="item-ai-daily-3"></a>
### [OpenAI 加强前沿模型监控 指导开发节奏](https://openai.com/index/pacing-model-development-cyber-capabilities) ⭐️ 7.0/10

OpenAI 正在加强前沿 AI 模型的监控、对齐和安全。新安全措施将指导模型开发的速度。这是在网络关键能力背景下提出的。

rss · OpenAI Blog · 8月18日 11:00

**「可关注」** 可关注：OpenAI 加强前沿模型的监控、对齐和安全，以指导模型开发的速度。

**标签**: `#lab`, `#policy`, `#model`, `#industry`

---

<a id="item-ai-daily-4"></a>
### [OpenAI 推出 ChatGPT for Teens](https://openai.com/index/chatgpt-for-teens) ⭐️ 7.0/10

OpenAI 推出了 ChatGPT for Teens。该版本帮助青少年学习、批判性思考，并自信地使用 AI。它内置了更强的保护措施、健康使用功能，并为家长提供了额外控制。

rss · OpenAI Blog · 8月18日 11:00

**「可关注」** 可关注：ChatGPT for Teens 内置了更强的保护措施、健康使用功能和家长控制。

**标签**: `#model`, `#lab`, `#product`, `#policy`

---

<a id="item-ai-daily-5"></a>
### [哈工大开源自进化 GUI Agent，用过一次学会](https://mp.weixin.qq.com/s?__biz=MzIwMTc4ODE0Mw==&amp;mid=2247722251&amp;idx=2&amp;sn=4974c06bb8a5a6187b274963d94b38ba) ⭐️ 6.0/10

哈尔滨工业大学开源了一款自进化 GUI Agent。该 Agent 只需使用一次就能学会执行跨多个应用的连续任务。文章称其为 AI 助手终于会“长记性”了。

rss · PaperWeekly · 8月18日 14:06

**「为什么重要」** 该自进化 GUI Agent 的开源为 AI 助手在多应用场景下实现连续工作提供了新思路。

**「可关注」** 可关注：用过一次就能学会的 GUI Agent

**标签**: `#open-source`, `#lab`, `#industry`, `#product`, `#eval`

---

<a id="item-ai-daily-6"></a>
### [Claude 加速蛋白设计与分析化学](https://news.google.com/rss/articles/CBMid0FVX3lxTFBZSUlFZ25ZeUpwR2FqLUh5WlJpQVRfM3RPaVg5dlo5NWMzbldIOW1WZDR2MklDNWdidlJIN2JKbUV1VU52aDk0YmlpdVJIVmRVTzRfanM5ZmU5MnlWVTZLSHZhTE0wVC1iRzNwUzRKRTk3MC1DMWZR?oc=5) ⭐️ 6.0/10

Anthropic 发布文章，介绍 Claude 如何加速蛋白设计和分析化学。文章提供了模型在生物技术和化学领域的应用案例。文章是来自实验室的原始来源。

google\_news · Anthropic · 8月18日 22:14

**「为什么重要」** 蛋白设计和分析化学是前沿领域，这项应用展示了 AI 模型在科学发现中的作用。

**「可关注」** 可关注：Claude 在蛋白设计和分析化学领域的应用案例。

**标签**: `#lab`, `#model`, `#industry`, `#product`

---