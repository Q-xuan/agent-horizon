---
layout: default
title: "Horizon Summary: 2026-08-26 (ZH)"
date: 2026-08-26
lang: zh
---

> 从 159 条内容中筛选出 18 条重要资讯。

---

**Harness 架构**
1. [E2B SDK 2.46.0 发布](#item-harness-arch-1) ⭐️ 6.5/10
2. [Claude Code 2.1.243 发布](#item-harness-arch-2) ⭐️ 6.5/10
3. [Claude Code v2.1.246 发布](#item-harness-arch-3) ⭐️ 5.5/10
4. [Cline desktop-v0.0.17 发布](#item-harness-arch-4) ⭐️ 5.5/10
5. [pydantic-ai v2.34.0 发布](#item-harness-arch-5) ⭐️ 5.5/10
6. [Gemini CLI v0.58.0-preview.0 发布](#item-harness-arch-6) ⭐️ 5.5/10
7. [Gemini CLI v0.57.0 发布](#item-harness-arch-7) ⭐️ 5.5/10

**Agent 工程师日报**
1. [Granite 4.2 模型发布](#item-agent-engineer-1) ⭐️ 7.5/10

**AI 日报**
1. [OpenAI 封禁俄罗斯 AI 影响力账号](#item-ai-daily-1) ⭐️ 9.5/10
2. [Claude 内存功能上线](#item-ai-daily-2) ⭐️ 9.5/10
3. [Anthropic 推出 500 万 wellbeing 研究资助计划](#item-ai-daily-3) ⭐️ 8.5/10
4. [OpenAI Jalapeño 推理芯片首测](#item-ai-daily-4) ⭐️ 7.5/10
5. [Bain &amp; Company 加入 Claude 合作伙伴网络](#item-ai-daily-5) ⭐️ 7.5/10
6. [OpenAI 推出 ChatGPT Work Codex Admin 插件](#item-ai-daily-6) ⭐️ 6.5/10
7. [OpenAI：丰富智能背后的全栈](#item-ai-daily-7) ⭐️ 5.5/10

**AI 羊毛**
1. [Keenable AI 代理搜索 API 免费 100k 请求](#item-ai-deals-1) ⭐️ 8.0/10
2. [CanvasForMusic 免费 Spotify Canvas 制作工具](#item-ai-deals-2) ⭐️ 6.0/10
3. [社区速递 155 \| 适马千元人像神头与七月派友剁手清单](#item-ai-deals-3) ⭐️ 5.0/10

---

## Harness 架构

<a id="item-harness-arch-1"></a>
### [E2B SDK 2.46.0 发布](https://github.com/e2b-dev/E2B/releases/tag/e2b%402.46.0) ⭐️ 6.5/10

E2B SDK v2.46.0 发布了。该版本移除了客户端侧的 API key 格式验证逻辑，仅要求 key 存在。validateApiKey 选项已弃用，服务器现在是 key 有效性的唯一来源。同时更新了 tar 7.5.22 和 @bufbuild/protobuf 2.14.0 等依赖。

github · github-actions\[bot\] · 8月25日 11:21

**「改了什么」** SDK 移除了客户端侧的 API key 格式验证逻辑，服务器成为 key 有效性的唯一来源。同时更新了 tar 7.5.22 和 @bufbuild/protobuf 2.14.0 等依赖。

**标签**: `#runtime`, `#sandbox`, `#permissions`

---

<a id="item-harness-arch-2"></a>
### [Claude Code 2.1.243 发布](https://code.claude.com/docs/en/changelog#2-1-243) ⭐️ 6.5/10

Claude Code 2.1.243 版本发布。该版本新增子代理特定的提示缓存 TTL 控制功能，支持主对话保持较长缓存而子代理保持较短缓存。新增模型选择器自定义设置，可以通过有序列表来管理可用的模型。/usage 接口现在提供每循环运行次数、总令牌数和最后运行等详细指标。

rss · Claude Code Changelog · 8月25日 08:03

**「改了什么」** 新增 subagentPromptCacheTtl 和 promptCacheTtl 设置，让用户能为子代理单独控制缓存时间。添加 modelPicker 配置以定制模型选择器。/usage 现在显示按循环的运行计数和令牌使用量。

**标签**: `#subagents`, `#memory`, `#runtime`

---

<a id="item-harness-arch-3"></a>
### [Claude Code v2.1.246 发布](https://github.com/anthropics/claude-code/releases/tag/v2.1.246) ⭐️ 5.5/10

Claude Code v2.1.246 已发布，包含权限接口更新和运行时修复。新增 Auto 模式权限标签和 Bash 通配符启动警告。修复了转录慢、会话启动和插件安装等问题。

github · ashwin-ant · 8月25日 22:31

**「改了什么」** 新增了 Auto 模式权限标签和 Bash 启动警告。修复了多项运行时 bug，包括转录渲染、会话打开、MCP 工具调用和插件相关问题。

**标签**: `#permissions`, `#tools`, `#runtime`

---

<a id="item-harness-arch-4"></a>
### [Cline desktop-v0.0.17 发布](https://github.com/cline/cline/releases/tag/desktop-v0.0.17) ⭐️ 5.5/10

Cline desktop v0.0.17 发布了新版本。该版本将插件、MCP、技能、规则、钩子和工具合并到一个带标签的 Customize 中心，并显示实时计数。还重新设计了 Models 页面和 voice 页面，同时对侧边栏会话进行了分组。

github · github-actions\[bot\] · 8月25日 09:06

**「改了什么」** 相对于 v0.0.16，v0.0.17 整合了插件/MCP/技能/规则/钩子和工具到单一 Customize 中心，并重新设计了 Models 和 voice 页面。还移除了代理的 todo 工具和 Agenda 面板，并调整了会话搜索和通知等功能。

**标签**: `#mcp`, `#tools`, `#plugins`, `#models`, `#voice`

---

<a id="item-harness-arch-5"></a>
### [pydantic-ai v2.34.0 发布](https://github.com/pydantic/pydantic-ai/releases/tag/v2.34.0) ⭐️ 5.5/10

pydantic-ai v2.34.0 发布了 GLM-5.3 模型支持和 LangChain 迁移技能。新增了 ZaiModel 的 GLM-5.3 支持，并提供了 LangChain 迁移工具。同时修复了多个 bug，包括 TestModel 生成、UIEventStream 状态等。

github · dsfaccini · 8月25日 01:47

**「改了什么」** 相比 v2.33.0，新增了 GLM-5.3 模型支持和 LangChain 迁移技能，并修复了多个 bug。

**标签**: `#tools`, `#models`, `#integrations`

---

<a id="item-harness-arch-6"></a>
### [Gemini CLI v0.58.0-preview.0 发布](https://github.com/google-gemini/gemini-cli/releases/tag/v0.58.0-preview.0) ⭐️ 5.5/10

Google Gemini CLI v0.58.0-preview.0 已发布，包含核心和沙箱组件的 bug 修复以及重构。此版本修复了核心符号链接评估一致性、macOS Seatbelt 沙箱隔离 Docker 套接字和二进制文件、写入策略安全检查器，以及 A2A 服务器在新消息轮次上的 stale cancellation 错误。还优化了历史回滚和重试提示。没有新接口或限制。

github · gemini-cli-robot · 8月25日 18:22

**「改了什么」** 相对 v0.57.0-preview.0，此版本修复了核心符号链接处理一致性、macOS Seatbelt 沙箱隔离、写入策略安全检查器以及 A2A 服务器取消问题，并优化了历史回滚和重试提示。

**标签**: `#sandbox`, `#runtime`, `#permissions`, `#core`

---

<a id="item-harness-arch-7"></a>
### [Gemini CLI v0.57.0 发布](https://github.com/google-gemini/gemini-cli/releases/tag/v0.57.0) ⭐️ 5.5/10

Gemini CLI v0.57.0 发布了，主要修复了 OAuth 代理重定向 URI 解析、IDE 连接目录不匹配、取消请求回滚等核心问题，并新增了评估工具的工具调用格式化器和失败摘要集成功能。相比 v0.56.0，没有重大运行时重写或架构变化。

github · gemini-cli-robot · 8月25日 18:37

**「改了什么」** 相比上一版，修复了 OAuth 代理重定向 URI 解析、IDE 连接目录不匹配、取消时回滚多轮请求，以及 eval 工具的工具调用格式化器和失败摘要集成。

**标签**: `#eval`, `#runtime`, `#fix`, `#tools`

---

## Agent 工程师日报

<a id="item-agent-engineer-1"></a>
### [Granite 4.2 模型发布](https://huggingface.co/blog/ibm-granite/granite-4-2) ⭐️ 7.5/10

IBM 发布了 Granite 4.2 系列密集解码器-only 大语言模型，包含 3B、8B 和 30B 三个尺寸。这些模型从头在约 15 万亿 tokens 上预训练，上下文窗口扩展至 512K tokens，通过监督微调结合链式思考和代理轨迹数据，并进行多阶段强化学习，包括沙盒化代理 RL 以及思考和工具调用模式。所有模型在 Apache 2.0 许可下发布，可通过 OpenAI 兼容接口集成到代理系统中。

rss · Hugging Face Blog · 8月25日 15:14

**「为什么重要」** Granite 4.2 提供了沙盒环境中代理 RL 的详细训练方法，这对理解如何将工具调用和代码操作集成到 AI Agent 中具有参考价值。

**「可关注」** 可关注：8B 和 30B 模型在代理 RL 阶段学会在真实沙盒环境中调用工具、编辑代码、驱动终端并搜索网页。

**标签**: `#coding-agent`, `#orchestration`, `#eval`

---

## AI 日报

<a id="item-ai-daily-1"></a>
### [OpenAI 封禁俄罗斯 AI 影响力账号](https://openai.com/index/disrupting-malicious-uses-of-ai-influence-campaign-russia) ⭐️ 9.5/10

OpenAI 封禁了来自俄罗斯的账号。OpenAI 这些账号利用 AI 推广一个假的以色列智库。OpenAI 这些账号还发布了一个“主权”指数，该指数赞扬俄罗斯并批评西方。

rss · OpenAI Blog · 8月25日 00:00

**「可关注」** 可关注：OpenAI 封禁了使用 AI 推广假以色列智库和“主权”指数的俄罗斯账号。

**标签**: `#openai`, `#policy`, `#ai-safety`, `#influence-operations`, `#malicious-uses`

---

<a id="item-ai-daily-2"></a>
### [Claude 内存功能上线](https://claude.com/blog/claudes-memory-works-everywhere-and-you-decide-whats-in-it) ⭐️ 9.5/10

Claude 聊天和 Cowork 的内存已合并。从今天起，聊天中的记忆与 Cowork 共享。用户可按主题查看、编辑或删除记忆，默认不存储敏感主题，但可选择开启。

rss · Claude Blog · 8月25日 00:00

**「可关注」** 可关注：Claude 聊天中会自动添加记忆，无需事后总结。

**标签**: `#claude`, `#anthropic`, `#memory`, `#product`, `#feature`

---

<a id="item-ai-daily-3"></a>
### [Anthropic 推出 500 万 wellbeing 研究资助计划](https://www.anthropic.com/news/wellbeing-research-grants) ⭐️ 8.5/10

Anthropic 推出 500 万美元资助计划，资助独立开放源代码的 wellbeing 评估研究。计划提供直接资金、模型访问和技术支持，研究者将独立工作并开源项目。申请截止日期为 9 月 21 日，入选者提交完整提案时间为 10 月 5 日。

rss · Anthropic News · 8月25日 00:00

**「为什么重要」** wellbeing 评估对 AI 安全至关重要，因为 AI 已成为情感支持和问题解决工具，但评估需考虑多轮对话和上下文变化。

**「可关注」** 可关注：rigorous wellbeing 评估需明确测量标准、包含临床专家验证、测试过合规与过拒绝、反映多轮对话场景，并用真实专家验证 graders。

**标签**: `#lab`, `#eval`, `#open-source`, `#policy`, `#industry`

---

<a id="item-ai-daily-4"></a>
### [OpenAI Jalapeño 推理芯片首测](https://openai.com/index/jalapeno-first-results) ⭐️ 7.5/10

OpenAI 发布了 Jalapeño 自定义推理芯片的首测结果。该芯片在现代模型上实现了更高的吞吐量、更低的延迟和更好的功耗效率，比先前方案领先。

rss · OpenAI Blog · 8月25日 07:00

**「可关注」** 可关注：Jalapeño 芯片在推理吞吐量、延迟和功耗效率上优于先前方案。

**标签**: `#lab`, `#product`, `#industry`

---

<a id="item-ai-daily-5"></a>
### [Bain &amp; Company 加入 Claude 合作伙伴网络](https://claude.com/blog/bain-company-joins-the-claude-partner-network-as-a-global-premier-partner) ⭐️ 7.5/10

Anthropic 与 Bain &amp; Company 宣布合作，Bain 加入 Claude 合作伙伴网络作为全球顶级合作伙伴。Bain 已将 Claude 部署至其 19,000 名员工，在试点阶段超过 7,000 人积极使用，且超过三分之二的试点参与者采用 Claude for Excel。合作帮助企业将 AI 从实验转向可衡量的业务成果。

rss · Claude Blog · 8月25日 00:00

**「为什么重要」** 这个合作伙伴关系结合了 Anthropic 的前沿 AI 技术与 Bain 的企业部署经验，有助于企业实现 AI 部署。

**「可关注」** 可关注：Bain 采用 Claude 后，复杂代码库中生产力提升 30% 到 50%。

**标签**: `#lab`, `#industry`, `#product`

---

<a id="item-ai-daily-6"></a>
### [OpenAI 推出 ChatGPT Work Codex Admin 插件](https://openai.com/index/introducing-admin-plugin) ⭐️ 6.5/10

OpenAI 推出了 ChatGPT Work 和 Codex 的 Admin 插件。用户可以使用该插件来分析工作区使用情况、管理成员和权限、调整限制，并处理管理员请求。

rss · OpenAI Blog · 8月25日 00:00

**「为什么重要」** 该插件为企业用户提供了强大的管理工具，有助于更好地控制和管理他们的 ChatGPT 工作区。

**「可关注」** 可关注：使用 Admin 插件分析工作区使用、管理成员和权限、调整限制并处理管理员请求。

**标签**: `#openai`, `#product`, `#enterprise`

---

<a id="item-ai-daily-7"></a>
### [OpenAI：丰富智能背后的全栈](https://openai.com/index/the-full-stack-behind-abundant-intelligence) ⭐️ 5.5/10

OpenAI 首席财务官 Sarah Friar 解释了芯片、算力、模型和产品方面的进步如何共同作用。这些进步共同作用，以更大规模和更低成本提供更有用的智能。这篇文章介绍了公司全栈策略。

rss · OpenAI Blog · 8月25日 07:05

**标签**: `#openai`, `#lab`, `#product`, `#compute`, `#strategy`

---

## AI 羊毛

<a id="item-ai-deals-1"></a>
### [Keenable AI 代理搜索 API 免费 100k 请求](https://keenable.ai/) ⭐️ 8.0/10

Keenable 推出专为 AI 代理优化的网页搜索 API，基于自家 100B+ 页面索引。提供每月 100,000 次免费请求，低延迟（p95 &lt;250ms）。开源 NEEDLE 基准测试，并暴露 SQL-like 接口用于结构化提取和代理工作流。

rss · HN Free API / Credits · 8月25日 15:12

**「为什么重要」** 代理搜索模式不同于人类搜索，Keenable 直接针对代理需求优化，免费额度立即可用，适合构建 AI 代理的开发者。

**「可关注」** 可关注：Keenable 提供 100,000 次免费请求/月，适用于 AI 代理工作流；开源 NEEDLE 基准测试可自行验证。

**标签**: `#free-tier`, `#credits`, `#api`, `#search-api`, `#agent`

---

<a id="item-ai-deals-2"></a>
### [CanvasForMusic 免费 Spotify Canvas 制作工具](https://canvasformusic.com/) ⭐️ 6.0/10

CanvasForMusic 是一个免费的网页工具，用于为音乐艺术家制作自定义 Spotify Canvas。用户可以上传自己的 artwork，选择旋转预设或裁剪缩放预设，无需使用库存媒体。工具完全免费，无需注册即可使用。

rss · HN Free API / Credits · 8月25日 16:07

**「可关注」** 可关注：艺术家可使用现有资产制作自定义 Canvas，无需 After Effects 或视频编辑器，内置循环动画。

**标签**: `#free-tier`, `#promo`, `#tool`, `#spotify`, `#canvas`

---

<a id="item-ai-deals-3"></a>
### [社区速递 155 \| 适马千元人像神头与七月派友剁手清单](https://sspai.com/post/113828) ⭐️ 5.0/10

少数派社区周报第 155 期整理了适马千元人像神头与七月派友的剁手清单。除了首页时间流和侧栏的精选展位，少数派 Matrix 社区还有很多优秀内容因条件所限无法得到有效曝光，因此我们决定重启 Matrix 周报，并在此基础上添加更多社区内容、作者投稿新玩意呈现给大家。

rss · 少数派 · 8月25日 09:00

**标签**: `#promo`, `#community`, `#coupon`

---