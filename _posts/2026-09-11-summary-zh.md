---
layout: default
title: "Horizon Summary: 2026-09-11 (ZH)"
date: 2026-09-11
lang: zh
---

> 从 207 条内容中筛选出 19 条重要资讯。

---

**Harness 架构**
1. [Claude Code v2.1.268 发布](#item-harness-arch-1) ⭐️ 7.8/10
2. [Codex python-v0.154.0 发布](#item-harness-arch-2) ⭐️ 7.8/10
3. [ADK Python v2.9.0 发布](#item-harness-arch-3) ⭐️ 7.8/10
4. [Cline desktop-v0.0.25 发布](#item-harness-arch-4) ⭐️ 6.8/10
5. [openai-agents-js v0.18.0 发布](#item-harness-arch-5) ⭐️ 6.8/10
6. [Agent Framework Python 1.18.0 发布](#item-harness-arch-6) ⭐️ 6.8/10
7. [e2b-dev/e2b e2b@2.49.1 发布](#item-harness-arch-7) ⭐️ 5.8/10

**Agent 工程师日报**
1. [Shopify 回归原生移动开发](#item-agent-engineer-1) ⭐️ 8.0/10
2. [SWE-2 发布：推向帕累托前沿](#item-agent-engineer-2) ⭐️ 7.8/10
3. [OpenAI Agents API 发布](#item-agent-engineer-3) ⭐️ 7.0/10

**AI 日报**
1. [OpenAI 政府 AI 访问扩展](#item-ai-daily-1) ⭐️ 9.8/10
2. [ChatGPT 金融服务版 发布](#item-ai-daily-2) ⭐️ 7.8/10
3. [Codex ChatGPT 搜索新型抗菌分子](#item-ai-daily-3) ⭐️ 6.8/10
4. [DeepSeek V4.1 Flash 发布](#item-ai-daily-4) ⭐️ 6.8/10
5. [ChatGPT Work Data agent 发布](#item-ai-daily-5) ⭐️ 5.8/10
6. [Copilot App 新手指南发布](#item-ai-daily-6) ⭐️ 5.8/10

**AI 羊毛**
1. [Mathathon Challenge 40 小时 $2M+ AI 积分](#item-ai-deals-1) ⭐️ 8.0/10
2. [geoSurge.ai 免费品牌可见性](#item-ai-deals-2) ⭐️ 6.0/10
3. [Modeinspect 99 天免费 AI 积分](#item-ai-deals-3) ⭐️ 5.0/10

---

## Harness 架构

<a id="item-harness-arch-1"></a>
### [Claude Code v2.1.268 发布](https://github.com/anthropics/claude-code/releases/tag/v2.1.268) ⭐️ 7.8/10

Claude Code v2.1.268 发布。新增网关定价同步功能，让 Claude apps gateway 的 pricing 配置生效。添加启动 CIDR 警告和自托管运行器会话清理选项。支持 configDirectory 输出和插件命令的 JSON 支持。

github · ashwin-ant · 9月10日 20:30

**「改了什么」** 相对于上一版，此次发布新增网关定价同步、启动 CIDR 警告、自托管运行器会话清理、configDirectory 输出，以及插件和认证的 JSON 支持。

**标签**: `#runtime`, `#tools`, `#gateway`, `#plugins`, `#json`

---

<a id="item-harness-arch-2"></a>
### [Codex python-v0.154.0 发布](https://github.com/openai/codex/releases/tag/python-v0.154.0) ⭐️ 7.8/10

OpenAI Codex Python v0.154.0 发布。新增 max 和 ultra 推理努力，支持 ExternalMessage 在同步异步 run/turn 调用中添加外部内容以启动或加入 turn。新增 include\_turns/turn\_service\_tier 在 resume/fork，并刷新协议模型。

github · aibrahim-oai · 9月10日 19:51

**「改了什么」** 新增 max/ultra 推理努力和 ExternalMessage 支持。新增 include\_turns/turn\_service\_tier 在 resume/fork，并刷新协议模型。

**标签**: `#runtime`, `#tools`, `#permissions`, `#planning`, `#memory`

---

<a id="item-harness-arch-3"></a>
### [ADK Python v2.9.0 发布](https://github.com/google/adk-python/releases/tag/v2.9.0) ⭐️ 7.8/10

ADK Python v2.9.0 发布。新增自动模型故障转移，提升代理弹性。添加 LiveKit runner，支持语音和电话代理开发。支持 YAML 加载 ADK 2.0 图工作流，并兼容 MCP SDK 2.x。

github · GWeale · 9月10日 21:22

**「改了什么」** 相比 v2.8.0，新增自动模型故障转移。添加 LiveKit runner 支持语音和电话集成。支持 YAML 加载 ADK 2.0 图工作流。MCP SDK 支持 2.x 版本。

**标签**: `#runtime`, `#mcp`, `#tools`, `#workflow`

---

<a id="item-harness-arch-4"></a>
### [Cline desktop-v0.0.25 发布](https://github.com/cline/cline/releases/tag/desktop-v0.0.25) ⭐️ 6.8/10

Cline desktop v0.0.25 发布。ChatGPT Codex 模型选择器现在仅列出计划可用的模型，并应用后端上下文容量限制。Windows 安装器停止守护进程后才杀死主二进制，本地 CLI 提供程序如 Claude Code、Codex CLI 和 OpenCode 现在无需 API 密钥即可启动会话。

github · github-actions\[bot\] · 9月10日 04:57

**「改了什么」** Cline desktop v0.0.25 修复了 Windows 安装器守护进程冲突，并使 ChatGPT Codex 模型选择器尊重订阅限制和上下文容量。提示发送失败时提示不再丢失，本地 CLI 提供程序无需 API 密钥即可启动会话。

**标签**: `#runtime`, `#tools`

---

<a id="item-harness-arch-5"></a>
### [openai-agents-js v0.18.0 发布](https://github.com/openai/openai-agents-js/releases/tag/v0.18.0) ⭐️ 6.8/10

openai-agents-js v0.18.0 发布了。该版本将 Docker 文件 API 迁移到容器内部运行，并为 UnixLocalSandboxClient 添加了可选的文件 I/O 保护。imageGenerationTool 现在支持 action 参数。

github · seratch · 9月10日 21:23

**「设计要点」** Docker 文件 API 现在完全在容器内运行，使用默认用户或 runAs。UnixLocalSandboxClient 的 fileIOProtection 默认 auto 模式下自动选择 Python 保护或保留 Node 行为。

**「改了什么」** 相比 v0.17.2，Docker 文件 API 迁移至容器内部，编辑器文件大小限制为 10MiB。新增 imageGenerationTool action 参数，并添加 fileIOProtection 配置选项。

**标签**: `#sandbox`, `#runtime`, `#permissions`, `#tools`

---

<a id="item-harness-arch-6"></a>
### [Agent Framework Python 1.18.0 发布](https://github.com/microsoft/agent-framework/releases/tag/python-1.18.0) ⭐️ 6.8/10

Microsoft Agent Framework Python 1.18.0 发布。新增共享向量存储抽象、便携过滤器和内存向量存储。添加工具调用循环最大时长限制和停止原因信号。支持混合工作流调用关键字参数和 UI 快照配置。

github · moonbox3 · 9月10日 09:23

**「设计要点」** 共享向量存储抽象用于内存持久化；工具调用循环添加最大时长和停止信号控制；工作流支持混合关键字参数。

**「改了什么」** 新增共享向量存储抽象和多种向量存储后端实现。引入工具调用循环时长限制和混合工作流参数支持。

**标签**: `#memory`, `#runtime`, `#tools`

---

<a id="item-harness-arch-7"></a>
### [e2b-dev/e2b e2b@2.49.1 发布](https://github.com/e2b-dev/E2B/releases/tag/e2b%402.49.1) ⭐️ 5.8/10

这是 e2b-dev/e2b 发布的 E2B SDK 2.49.1 版本。修复了无效 Sandbox.create/connect 选项的拒绝问题，记录了 onResume 内存字段处理方式，并为控制平面请求添加了最多 3 次 Retry-After HTTP 重试。

github · github-actions\[bot\] · 9月10日 17:37

**「改了什么」** 修复了无效 Sandbox.create/connect 选项的拒绝问题，记录了 onResume 内存字段处理方式，并添加了控制平面 HTTP 请求的重试功能。

**标签**: `#sandbox`, `#memory`, `#runtime`, `#control-plane`, `#retries`

---

## Agent 工程师日报

<a id="item-agent-engineer-1"></a>
### [Shopify 回归原生移动开发](https://simonwillison.net/2026/Sep/10/shopify-react-native/) ⭐️ 8.0/10

Shopify 决定从 React Native 切换回原生 Swift 和 Kotlin 代码库，重新构建各自的移动应用。

他们于 2020 年转向 React Native，是为了避免重复构建同一特性、让开发者跨栈工作，以及减少追逐特性平行的时间。

现在，AI 代理能够处理实现、翻译、测试和审查工作，使维护重复特性的成本不再是决定性因素。

这项变化影响 Shopify 的移动开发者。

rss · Simon Willison · 9月10日 21:11

**「为什么重要」** AI 代理使维护重复特性的成本不再是决定性因素。Shopify 的切换是已发生的变化，但其对移动开发工作流的长期影响尚未完全证实。

**「可关注」** 可关注：AI 代理处理跨平台实现、翻译、测试和审查工作，使维护重复特性的成本不再是决定性因素。

**标签**: `#coding-agent`, `#orchestration`, `#harness`, `#eval`

---

<a id="item-agent-engineer-2"></a>
### [SWE-2 发布：推向帕累托前沿](https://cognition.ai/blog/swe-2) ⭐️ 7.8/10

Cognition 发布 SWE-2 模型，基于 Kimi K33 后训练，在 FrontierCode 1.1 Main 达到 50.0% 分数，较 Fable 5.1 便宜 64%。通过扩展 RL 算法，在单次运行中训练所有推理努力级别。模型在 Devin Desktop、CLI、Web 和 Fusion 中可用。

rss · Cognition Blog · 9月10日 17:00

**「为什么重要」** SWE-2 发布后，在 FrontierCode 1.1 Main 达到 50.0% 分数，较 Fable 5.1 便宜 64%。这已发生的变化直接影响 coding-agent evals 的基准，但对 harness 的影响尚未证实。

**「可关注」** 可关注：SWE-2 medium 在 FrontierCode 1.1 Main 比 SWE-1.7 更高同时步数减少 58% 且成本降低 81%。

**标签**: `#coding-agent`, `#eval`

---

<a id="item-agent-engineer-3"></a>
### [OpenAI Agents API 发布](https://developers.openai.com/api/docs/guides/agents-api/overview) ⭐️ 7.0/10

OpenAI 发布 Agents API。作为构建可定制 AI 代理的服务，该 API 集成工具并提供环境无关状态管理。

官方文档概述引入代理编排抽象，支持状态和工具持久化。

该服务影响开发者构建代理 harness 的方式。

hackernews · aquir · 9月10日 19:43 · [社区讨论](https://news.ycombinator.com/item?id=49649213)

**「为什么重要」** OpenAI Agents API 发布提供代理编排抽象和状态工具持久化细节，影响 workflow 构建。

**「可关注」** 可关注：支持自托管沙箱，降低供应商锁定风险。

**「评论」** 社区评论指出，OpenAI Agents API 提供工具集成和状态管理，缓解 harness 环境耦合难题。部分用户担忧供应商锁定，并建议提供 reasoning tokens，自托管沙箱选项受欢迎。

**标签**: `#orchestration`, `#harness`, `#coding-agent`, `#agents-api`, `#memory`

---

## AI 日报

<a id="item-ai-daily-1"></a>
### [OpenAI 政府 AI 访问扩展](https://openai.com/index/expanding-ai-access-us-government) ⭐️ 9.8/10

OpenAI 与 GSA 合作，为符合条件的联邦、州、县、市和部落政府提供 AI 访问。他们将收取 $0 许可费，并提供 50% 使用折扣，并扩展网络安全防御支持。

rss · OpenAI Blog · 9月10日 07:00

**「为什么重要」** 政府机构可通过 GSA 获得 OpenAI AI 的 $0 许可费和 50% 使用折扣。

**「可关注」** 可关注：符合条件的政府机构可获得 $0 许可费和 50% 使用折扣，并获得扩展的网络安全防御支持。

**标签**: `#openai`, `#policy`, `#government`, `#product`

---

<a id="item-ai-daily-2"></a>
### [ChatGPT 金融服务版 发布](https://openai.com/index/introducing-chatgpt-financial-services) ⭐️ 7.8/10

OpenAI 推出 ChatGPT 金融服务版。
此版本结合内置金融数据和 GPT-6 Astra。
用户可使用该版本进行研究、建模和生成客户材料。

rss · OpenAI Blog · 9月10日 07:00

**「可关注」** 可关注：结合金融数据和 GPT-6 Astra 的研究建模能力。

**标签**: `#model`, `#lab`, `#industry`, `#product`

---

<a id="item-ai-daily-3"></a>
### [Codex ChatGPT 搜索新型抗菌分子](https://openai.com/index/using-codex-chatgpt-to-search-for-new-antimicrobials) ⭐️ 6.8/10

塞萨尔·德拉富恩特的实验室使用 Codex 和 ChatGPT 在活体和已灭绝基因组中搜索抗菌分子候选物。
该方法旨在开发新型抗菌药物以对抗耐药感染。
目前未披露具体搜索结果，方法依赖现有模型的生成能力。

rss · OpenAI Blog · 9月10日 16:00

**「可关注」** 「可关注：将 Codex 与 ChatGPT 结合用于基因组搜索以发现抗菌分子。」

**标签**: `#model`, `#lab`, `#industry`, `#product`

---

<a id="item-ai-daily-4"></a>
### [DeepSeek V4.1 Flash 发布](https://mp.weixin.qq.com/s?__biz=Mzk0OTYwNzc3NQ==&amp;mid=2247485817&amp;idx=1&amp;sn=627dd80114901f3fd8717e2c13feaf6a) ⭐️ 6.8/10

DeepSeek 发布了 V4.1 Flash。
这是更强、更快、更普惠的全新原生多模态基座模型。
官方公告中未提供具体性能数据或参数。

rss · DeepSeek · 9月10日 05:44

**「可关注」** 可关注：原生多模态，全新基座模型

**标签**: `#model`, `#DeepSeek`, `#multimodal`, `#product`

---

<a id="item-ai-daily-5"></a>
### [ChatGPT Work Data agent 发布](https://openai.com/index/put-data-to-work) ⭐️ 5.8/10

OpenAI 在 ChatGPT Work 中推出 Data agent。用户可以使用自然语言查询公司数据，挖掘洞见并构建交互式仪表盘。

rss · OpenAI Blog · 9月10日 15:00

**「为什么重要」** ChatGPT Work Data agent 发布，用户可通过自然语言连接公司数据。这有助于发现商业洞见。

**「可关注」** 可关注：自然语言查询公司数据。

**标签**: `#openai`, `#chatgpt`, `#product`, `#industry`

---

<a id="item-ai-daily-6"></a>
### [Copilot App 新手指南发布](https://github.blog/ai-and-ml/github-copilot/github-copilot-app-for-beginners-using-the-diff-terminal-and-browser/) ⭐️ 5.8/10

GitHub 发布了 Copilot App 的新手指南。用户可在侧边查看 AI 生成代码的 diffs、运行终端命令，并预览网页应用。开发者无需在多个标签页间切换，直接在 GitHub 界面上完成检查。

rss · GitHub Blog · 9月10日 21:31

**「为什么重要」** Copilot App 的侧边查看功能简化了 AI 生成代码的检查流程。

**「可关注」** 可关注：侧边查看 diffs、终端命令和浏览器预览。

**标签**: `#github`, `#copilot`, `#product`, `#app`

---

## AI 羊毛

<a id="item-ai-deals-1"></a>
### [Mathathon Challenge 40 小时 $2M+ AI 积分](https://mathathonchallenge.com/) ⭐️ 8.0/10

Mathathon Challenge 提供 40 小时和 $2M+ AI 积分给参与者。
参与者需解决开放问题才能领取。
这是发起的挑战。

rss · HN Free API / Credits · 9月10日 16:45

**标签**: `#credits`, `#free-tier`, `#promo`, `#challenge`

---

<a id="item-ai-deals-2"></a>
### [geoSurge.ai 免费品牌可见性](https://app.geosurge.ai/login) ⭐️ 6.0/10

geoSurge.ai 提供完全免费的品牌监控和 LLM 情感分析。用户连接现有 LLM 订阅，利用空闲 token，无需额外费用。数据通过仪表板查看或获取免费情感分析。

rss · HN Free API / Credits · 9月10日 13:16

**「为什么重要」** 无需额外成本即可监控品牌在 LLM 搜索中的表现。适合对品牌事实准确性有需求的个人或企业。

**「可关注」** 可关注：连接现有 LLM 订阅并使用空闲 token，无需额外支付。适用于有 LLM 订阅的用户。

**标签**: `#free-tier`, `#promo`, `#api`, `#sentiment-analysis`, `#brand-monitoring`

---

<a id="item-ai-deals-3"></a>
### [Modeinspect 99 天免费 AI 积分](https://www.producthunt.com/products/modeinspect-1-0) ⭐️ 5.0/10

Modeinspect 提供 99 天免费 AI 积分，用于在代码库中设计产品 UI。这是 Product Hunt 上的促销活动。

rss · Product Hunt · 9月10日 03:31

**标签**: `#promo`, `#credits`, `#free-tier`, `#limited-free`, `#producthunt`

---