---
layout: default
title: "Horizon Summary: 2026-09-03 (ZH)"
date: 2026-09-03
lang: zh
---

> 从 207 条内容中筛选出 23 条重要资讯。

---

**Harness 架构**
1. [Claude Code v2.1.259 发布](#item-harness-arch-1) ⭐️ 7.8/10
2. [LangChain 1.4.0a4 发布](#item-harness-arch-2) ⭐️ 7.8/10
3. [Cline v4.1.17 发布](#item-harness-arch-3) ⭐️ 6.8/10
4. [Codex rust-v0.153.0 发布](#item-harness-arch-4) ⭐️ 5.8/10
5. [Cline SDK v0.0.82 发布](#item-harness-arch-5) ⭐️ 5.8/10
6. [Cline desktop-v0.0.22 发布](#item-harness-arch-6) ⭐️ 5.8/10
7. [Cline CLI v3.0.61 发布](#item-harness-arch-7) ⭐️ 5.8/10
8. [browser-use/video-use GitHub trending](#item-harness-arch-8) ⭐️ 5.0/10

**Agent 工程师日报**
1. [llm-gemini 0.34 发布](#item-agent-engineer-1) ⭐️ 7.0/10
2. [HF daily paper: 自托管 LLM GRPO 合并](#item-agent-engineer-2) ⭐️ 7.0/10
3. [Harness-of-Harness 多日自主开发框架](#item-agent-engineer-3) ⭐️ 7.0/10
4. [llm 0.34 日志加耗时并修缓存](#item-agent-engineer-4) ⭐️ 6.8/10
5. [Gemini 3.8 Flash 发布](#item-agent-engineer-5) ⭐️ 6.0/10
6. [H3-World：语言理解转向世界控制](#item-agent-engineer-6) ⭐️ 6.0/10
7. [llm-openrouter 0.7.1 发布](#item-agent-engineer-7) ⭐️ 5.8/10
8. [IBM TSFM Confluent 实时智能](#item-agent-engineer-8) ⭐️ 5.8/10

**AI 日报**
1. [GitHub Copilot 成本优化 发布](#item-ai-daily-1) ⭐️ 7.8/10
2. [Meta 组织第二大脑 AI 专家](#item-ai-daily-2) ⭐️ 7.8/10
3. [GitHub Blog 解码 AI 流行语](#item-ai-daily-3) ⭐️ 6.8/10
4. [ATV Big Air Tour 用 ChatGPT 节省 3 天工作](#item-ai-daily-4) ⭐️ 5.8/10

**AI 羊毛**
1. [LongCat-2.0 免费试用 Cline](#item-ai-deals-1) ⭐️ 6.0/10
2. [Éclat Blue One-Click Auth 公测](#item-ai-deals-2) ⭐️ 5.0/10
3. [translatemycall.com 免费电话服务](#item-ai-deals-3) ⭐️ 5.0/10

---

## Harness 架构

<a id="item-harness-arch-1"></a>
### [Claude Code v2.1.259 发布](https://github.com/anthropics/claude-code/releases/tag/v2.1.259) ⭐️ 7.8/10

Claude Code v2.1.259 由 Anthropic 发布，新增 managedMcpServers 托管设置，允许组织向所有用户提供 HTTP/SSE MCP 服务器。添加 --permission-prompts none 选项用于无头主机，并支持 GitLab MR 操作以在工具摘要中显示 MR \!N。修复了并发会话中状态丢失等问题。

github · ashwin-ant · 9月2日 22:33

**「改了什么」** 相比上一版，v2.1.259 增加了 managedMcpServers 设置和 GitLab MR 支持，修复了并发会话中 ~/.claude.json 状态丢失的问题。

**标签**: `#mcp`, `#permissions`, `#tools`, `#runtime`, `#memory`

---

<a id="item-harness-arch-2"></a>
### [LangChain 1.4.0a4 发布](https://github.com/langchain-ai/langchain/releases/tag/langchain%3D%3D1.4.0a4) ⭐️ 7.8/10

LangChain 1.4.0a4 alpha 版本正式发布。该版本针对 MCP 客户端处理、打断路由和可重入组进行了更新，以支持 fastmcp 兼容性。
核心改动包括将 MCP 客户端 arming 操作内联至 \_\_init\_\_ 方法，使用 arm marker 替代闭包内省，基于协商协议 era 门控打断路由，移除 elicitation 标志，并新增 \_ReentrantClientGroup。
这是 LangChain 框架在 MCP 适配器上的迭代，针对 fastmcp 4.0.1 的兼容性优化。

github · github-actions\[bot\] · 9月2日 05:35

**「改了什么」** 相比 1.4.0a3，该版本重构了 MCPAdapter，重点是客户端 arming 内联、arm marker 打标、基于协议 era 的打断路由门控，以及新增可重入组以支持 fastmcp 兼容性。

**标签**: `#mcp`, `#runtime`, `#tools`

---

<a id="item-harness-arch-3"></a>
### [Cline v4.1.17 发布](https://github.com/cline/cline/releases/tag/v4.1.17) ⭐️ 6.8/10

Cline v4.1.17 发布了。新增 ClinePass 界面元素，包括账户页面卡片、提供商设置提示和首页横幅。修复了长会话中后台 Hub 进程内存膨胀问题，通过快照替代全量转录广播。修复了钩子脚本失败导致的核心进程崩溃，以及聊天渲染、成本估算、API 密钥等多个 bug。

github · github-actions\[bot\] · 9月2日 05:40

**「改了什么」** 上线 ClinePass 界面元素和模型目录刷新。模型目录更新后，默认模型对 57 个提供商生效。

**标签**: `#runtime`, `#memory`, `#tools`

---

<a id="item-harness-arch-4"></a>
### [Codex rust-v0.153.0 发布](https://github.com/openai/codex/releases/tag/rust-v0.153.0) ⭐️ 5.8/10

openai/codex rust-v0.153.0 发布。新增 Vim 模式支持撤销（u）和重做（Ctrl+R），插件 CLI 支持列出安装移除插件，TUI 自动 recap 禁用选项，TUI 历史记录显示完整补丁和命令。TUI 会话在 app-server 连接断开后自动重连，保留草稿和转录。

github · github-actions\[bot\] · 9月3日 01:37

**「改了什么」** Vim 模式新增撤销和重做支持。TUI 会话在 app-server 断开后自动重连，保留草稿和转录。

**标签**: `#tools`, `#runtime`

---

<a id="item-harness-arch-5"></a>
### [Cline SDK v0.0.82 发布](https://github.com/cline/cline/releases/tag/sdk/sdk/v0.0.82) ⭐️ 5.8/10

Cline SDK v0.0.82 发布了。修复了网关模型工具调用被静默禁用的问题，以及空能力列表导致图像输入被剥离。Langfuse 追踪现在支持 minified release builds。新增加了 SessionImportService，支持从 Claude Code、Codex 和 opencode 导入会话历史。

github · github-actions\[bot\] · 9月2日 04:40

**「设计要点」** hub 管理在活动检查前建立 drain barrier，避免在运行工作下被退休。SessionImportService 实现事务性、幂等性导入会话历史。

**「改了什么」** 此版本修复了工具调用和图像输入处理问题，添加了会话历史导入功能，改进了 hub 管理逻辑，并刷新了模型目录。

**标签**: `#tools`, `#runtime`

---

<a id="item-harness-arch-6"></a>
### [Cline desktop-v0.0.22 发布](https://github.com/cline/cline/releases/tag/desktop-v0.0.22) ⭐️ 5.8/10

Cline desktop v0.0.22 发布。新增从 Claude Code、Codex 和 opencode 导入历史记录到会话的功能。在 Sessions 头部提供导入按钮，并在设置中添加选项。macOS 上启用语音输入，并将调度运行折叠到单个侧边栏一行。

github · github-actions\[bot\] · 9月2日 05:20

**「改了什么」** Cline desktop v0.0.22 相对上一版新增历史记录导入功能，将调度运行折叠到单个侧边栏行，并启用 macOS 语音输入。

**标签**: `#tools`, `#runtime`, `#memory`

---

<a id="item-harness-arch-7"></a>
### [Cline CLI v3.0.61 发布](https://github.com/cline/cline/releases/tag/cli-v3.0.61) ⭐️ 5.8/10

Cline CLI v3.0.61 发布，修复了 Hub 替换流中较旧版本的兼容问题。CLI 不再因不可达的远程 MCP 服务器而崩溃，并为特定模型重新启用了工具调用。Windows 二进制现已通过 Azure Trusted Signing 签名，并改进了 Langfuse 追踪和检查点恢复等功能。

github · github-actions\[bot\] · 9月2日 04:49

**「改了什么」** v3.0.61 修复了 Hub 替换流、远程 MCP 服务器不可达导致的崩溃，以及特定模型工具调用被禁用的问题，并改进了 Windows 二进制签名、检查点恢复和 Langfuse 追踪支持。

**标签**: `#mcp`, `#runtime`, `#tools`

---

<a id="item-harness-arch-8"></a>
### [browser-use/video-use GitHub trending](https://github.com/browser-use/video-use) ⭐️ 5.0/10

browser-use/video-use 工具在 GitHub trending，推出开源视频编辑工具 video-use。100% 开源，用户将原始视频素材放入文件夹，与 Claude Code 聊天，即可生成 final.mp4。支持任何内容类型，无需预设或菜单。在 Browser Use Cloud 中可尝试。

rss · GitHub Trending Daily · 9月3日 01:41

**标签**: `#tools`, `#subagents`, `#planning`

---

## Agent 工程师日报

<a id="item-agent-engineer-1"></a>
### [llm-gemini 0.34 发布](https://simonwillison.net/2026/Sep/2/llm-gemini/) ⭐️ 7.0/10

llm-gemini 0.34 发布了。2026 年 9 月 2 日新增 gemini-3.8-flash 模型支持，支持低、中、高三种 thinking levels。修复了异步响应未能记录解析模型版本的 bug。

rss · Simon Willison · 9月2日 16:39

**「为什么重要」** Gemini 3.8 Flash 模型支持为 coding-agent harness 提供了新模型选项。异步响应修复确保了工具链的准确性。

**「可关注」** 可关注：Gemini 3.8 Flash 支持三种 thinking levels。

**标签**: `#coding-agent`, `#harness`, `#orchestration`, `#model-integration`

---

<a id="item-agent-engineer-2"></a>
### [HF daily paper: 自托管 LLM GRPO 合并](https://huggingface.co/papers/2609.01572) ⭐️ 7.0/10

数据主权限制迫使企业自托管 LLM。持续采用新模型而不停用旧模型，导致服务舰队扩张，碎片化有限 GPU 池。我们将 200+内部应用的流量整合到单个模型，通过生产错误分析沿指令遵循、函数调用、内部任务分布三个轴，训练各轴 GRPO 专家并用两阶段 SLERP 合并。质量通过生产流量分层离线基准测试，用确定性验证器或校准 LLM judges 打分。

rss · Hugging Face Daily Papers · 9月3日 01:41

**「为什么重要」** 数据主权约束下，自托管 LLM 需覆盖企业请求混合。GRPO 专家和 SLERP 合并方案可整合 200+应用流量到单一模型，缓解 GPU 池碎片化。

**「可关注」** 可关注：沿三个轴训练 GRPO 专家并用 SLERP 合并，避免联合优化引入的跨域奖励干扰。

**标签**: `#eval`, `#orchestration`, `#harness`, `#coding-agent`

---

<a id="item-agent-engineer-3"></a>
### [Harness-of-Harness 多日自主开发框架](https://huggingface.co/papers/2609.01481) ⭐️ 7.0/10

Harness-of-Harness \(HoH\) 框架将 coding-agent 执行组织成迭代 planning-coding-testing 循环。HoH 在现有 harness 上运行，实现多日自主软件开发中的持续改进。HoH 平衡 repair 与 capability growth，划分 small verifiable increments，分离 implementation-time testing 与 independent evaluation，并约束 verifiable outputs 而非 workflow。

rss · Hugging Face Daily Papers · 9月3日 01:41

**「为什么重要」** HoH 框架已提供迭代循环和 repair-growth 平衡等具体技术，支持 coding-agent 的持续改进。尚未证实其在实际多日开发中的效果。

**「可关注」** 可关注：HoH 平衡 repair 与 capability growth，划分 small verifiable increments，分离 implementation-time testing 与 independent evaluation。

**标签**: `#harness`, `#coding-agent`, `#eval`, `#orchestration`

---

<a id="item-agent-engineer-4"></a>
### [llm 0.34 日志加耗时并修缓存](https://github.com/simonw/llm/releases/tag/0.34) ⭐️ 6.8/10

simonw 发布 llm 0.34。\`llm logs --usage\` 的 Markdown 输出现含响应耗时，毫秒数与可读时长一并写出；\`llm logs --short\` 新增 \`duration\_ms\` 字段。长对话下 \`llm logs\` 缓存重复的 message 与 model 查找；动态生成的 OpenAI options 类也做缓存，避免 \`llm-openrouter\` 等插件反复构造 Pydantic 类。非法 schema DSL 传给 \`llm prompt --schema\` 时改为干净命令行报错，不再出 Python traceback；\`llm --extract\` 能识别 CRLF 换行的围栏代码块；\`monotonic\_ulid\(\)\` 在系统时钟回拨或并发时间戳乱序时仍保持单调；\`typing-extensions\` 列为直接依赖，并补测试防止漏依赖。

github · simonw · 9月2日 19:23

**「为什么重要」** 用 llm 记调用日志的人，现在能在 \`--usage\` / \`--short\` 里直接看到单次响应耗时。长会话 logs 与 OpenAI 兼容插件反复建 Pydantic 类，是这次点名修掉的开销；材料没有给出加速数字。

**「可关注」** 可关注：长对话 logs 上的重复 message / model 查找，以及插件动态构造 OpenAI options（Pydantic 类），是 0.34 写明的两条热路径。

**标签**: `#coding-agent`, `#orchestration`, `#observability`

---

<a id="item-agent-engineer-5"></a>
### [Gemini 3.8 Flash 发布](https://blog.google/innovation-and-ai/models-and-research/gemini-models/3-8-flash-and-3-8-flash-cyber/) ⭐️ 6.0/10

Google 发布了 Gemini 3.8 Flash 模型。该模型速度快，在基准测试中与更大模型竞争，在 HTML 生成等任务中表现良好。模型智能分数为 59，与 Opus 5 中等版本相当。适用于编码代理、评估和 harness。

hackernews · bratao · 9月2日 15:12 · [社区讨论](https://news.ycombinator.com/item?id=49537553)

**「为什么重要」** Gemini 3.8 Flash 的发布展示了快速模型在基准测试中的竞争力。社区成员分享了其在 HTML 生成和多模态支持方面的实际体验。

**「可关注」** 可关注：Gemini 3.8 Flash 在 HTML/JS 生成任务中表现突出，成本低至 1.8 美分。

**「评论」** 社区成员分享了使用体验。Simon Willison 指出速度与 HTML/JS 生成能力结合令人兴奋，并提供了示例代码。Matt London 表示其在 deepswe.datacurve.ai 上排名第一，超越 Opus 5。

**标签**: `#coding-agent`, `#eval`, `#harness`

---

<a id="item-agent-engineer-6"></a>
### [H3-World：语言理解转向世界控制](https://www.reddit.com/r/LocalLLaMA/comments/1w5akpy/h3world_turning_language_understanding_into_world/) ⭐️ 6.0/10

H3-World 论文将语言指令转换为视频和游戏场景中的角色和相机动作。通过 MiniMax-H3 的预训练文本路径实现语言原生控制。为每个视频潜在间隔分配动作提示，实现时间上接地的精确控制。仅使用 8000 个游戏样本、10000 个 LoRA 步骤和 0.199%可训练参数，即可实现包括未见动作组合和视觉场景在内的可控角色和相机运动。

reddit · r/LocalLLaMA · /u/sachasayan · 9月2日 13:35

**「可关注」** 可关注：仅使用 0.199%可训练参数和 8000 个游戏样本，即可实现包括未见动作组合在内的可控角色和相机运动。

**标签**: `#orchestration`, `#coding-agent`, `#harness`, `#eval`

---

<a id="item-agent-engineer-7"></a>
### [llm-openrouter 0.7.1 发布](https://github.com/simonw/llm-openrouter/releases/tag/0.7.1) ⭐️ 5.8/10

Simonw 发布了 llm-openrouter 0.7.1 版本，修复了加载 OpenRouter 模型的性能问题。感谢 waveplate 贡献的 \#59。这是一个小版本更新，没有破坏性变更。

github · simonw · 9月2日 20:23

**「可关注」** 可关注：修复了加载 OpenRouter 模型的性能问题。

**标签**: `#orchestration`, `#coding-agent`

---

<a id="item-agent-engineer-8"></a>
### [IBM TSFM Confluent 实时智能](https://huggingface.co/blog/ibm-research/real-time-intelligence) ⭐️ 5.8/10

IBM TSFM 集成 Confluent，支持实时智能。模型训练一次泛化到未见系列，通过 Flink SQL 函数 AI\_FORECAST 和 AI\_DETECT\_ANOMALIES 在流数据上直接运行预测和异常检测。Confluent Cloud 提供新鲜上下文、治理和成本效率，无需专用 ML 栈。

rss · Hugging Face Blog · 9月2日 13:49

**「为什么重要」** 该集成将实时业务事件转化为可行动的智能，桥接操作和分析领域。

**「可关注」** 可关注：使用 AI\_FORECAST Flink SQL 函数调用 IBM TSFM 模型实现实时预测和异常检测。

**标签**: `#orchestration`, `#observability`, `#real-time`, `#time-series`, `#foundation-model`

---

## AI 日报

<a id="item-ai-daily-1"></a>
### [GitHub Copilot 成本优化 发布](https://github.blog/ai-and-ml/github-copilot/how-we-make-ai-coding-more-cost-efficient-without-sacrificing-task-quality/) ⭐️ 7.8/10

GitHub 博客文章解释如何通过 GitHub Copilot 使 AI 编码更具成本效率，而不牺牲任务质量。较短的输出可能导致更高成本，但 GitHub Copilot 通过减少完整编码任务中的浪费工作来实现优化。

rss · GitHub Blog · 9月2日 18:00

**「为什么重要」** 这一方法帮助开发者在 AI 编码中节省成本，提高工作效率。

**「可关注」** 可关注：较短输出可能成本更高，GitHub Copilot 通过减少完整任务浪费来优化 AI 编码成本。

**标签**: `#lab`, `#product`, `#industry`

---

<a id="item-ai-daily-2"></a>
### [Meta 组织第二大脑 AI 专家](https://engineering.fb.com/2026/09/02/ml-applications/organizational-second-brain-ai-learns-from-experts/) ⭐️ 7.8/10

Meta 构建了 AI 代理，作为给定领域的次级专家。它使深层专业知识易于获取并保留，供组织内任何人访问、分享并构建。该系统非典型领域特定代理，其创新在于整合两层：结构化可审计知识架构。

rss · Engineering at Meta · 9月2日 09:00

**「为什么重要」** 这个系统帮助组织保留专业知识，防止知识流失。

**「可关注」** 可关注：结构化可审计知识架构

**标签**: `#lab`, `#product`, `#industry`

---

<a id="item-ai-daily-3"></a>
### [GitHub Blog 解码 AI 流行语](https://github.blog/ai-and-ml/decoding-the-new-ai-lingo-loops-harnesses-squads-hill-climbing-oh-my/) ⭐️ 6.8/10

GitHub Blog 发布文章，解码 AI 新流行语。这些术语包括 Loops、harnesses、squads 和 hill climbing 等，均来自 GitHub Podcast。

文章指出，从 loop engineering 到 harnesses、squads 和 open weights，GitHub Podcast 拆解开发者对话中的 AI 术语。

rss · GitHub Blog · 9月2日 21:00

**「可关注」** 可关注：GitHub Podcast 拆解 AI 术语 Loops、harnesses、squads 和 hill climbing。

**标签**: `#github`, `#industry`, `#ai-terms`

---

<a id="item-ai-daily-4"></a>
### [ATV Big Air Tour 用 ChatGPT 节省 3 天工作](https://openai.com/index/atv-big-air-tour) ⭐️ 5.8/10

ATV Big Air Tour 使用 ChatGPT 加速营销和商品管理。将三天的营销工作缩短至三小时。15 分钟内将商品照片生成库存网站。

rss · OpenAI Blog · 9月2日 12:00

**「为什么重要」** ATV Big Air Tour 的案例展示了 ChatGPT 在营销和商品管理中的效率提升。

**「可关注」** 可关注：15 分钟将商品照片生成库存网站。

**标签**: `#industry`, `#product`, `#ChatGPT`

---

## AI 羊毛

<a id="item-ai-deals-1"></a>
### [LongCat-2.0 免费试用 Cline](https://twitter.com/Meituan_LongCat/status/2094996391387111865) ⭐️ 6.0/10

美团官方发布 LongCat-2.0 免费试用 Cline。该模型无具体额度或时长限制。领取条件为在 Cline 平台访问，截止时间未提供。

rss · HN Free API / Credits · 9月2日 09:58

**标签**: `#free-tier`, `#promo`, `#model`

---

<a id="item-ai-deals-2"></a>
### [Éclat Blue One-Click Auth 公测](https://news.ycombinator.com/item?id=49543502) ⭐️ 5.0/10

Éclat Blue One-Click Auth 推出小规模公测。作为轻量级 OIDC 身份提供商，支持前端通过浏览器原生 API 认证，无需导入外部 SDK。严格执行授权码流和 PKCE 协议，可直接通过浏览器 API 安全前端应用。无需注册即可在首页 Try Me 链接查看集成流程和端点。

rss · HN Free API / Credits · 9月2日 22:32

**「可关注」** 可关注：适用于前端应用认证，无需暴露客户端密钥。

**标签**: `#free-tier`, `#promo`, `#api`, `#beta`, `#limited-free`

---

<a id="item-ai-deals-3"></a>
### [translatemycall.com 免费电话服务](https://translatemycall.com/) ⭐️ 5.0/10

translatemycall.com 提供免费电话号码，支持 47 种语言的实时通话翻译。该服务声称无需注册即可使用，但未披露具体领取条件和使用限制。目前未提供截止时间或额度信息。

rss · HN Free API / Credits · 9月2日 17:24

**「可关注」** 可关注：服务未提供注册详情、使用限制、截止时间或使用限制。

**标签**: `#free-tier`, `#promo`

---