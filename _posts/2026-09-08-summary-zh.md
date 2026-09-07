---
layout: default
title: "Horizon Summary: 2026-09-08 (ZH)"
date: 2026-09-08
lang: zh
---

> 从 176 条内容中筛选出 10 条重要资讯。

---

**Harness 架构**
1. [MCP Python SDK v2.2.0 发布](#item-harness-arch-1) ⭐️ 7.8/10
2. [MCP Python SDK v1.30.0 发布](#item-harness-arch-2) ⭐️ 6.8/10
3. [browser-use GitHub trending](#item-harness-arch-3) ⭐️ 5.0/10

**Agent 工程师日报**
1. [OpenAI 研究加速：内部视图](#item-agent-engineer-1) ⭐️ 7.0/10
2. [Iris-mini Iris-pro 搜索代理发布](#item-agent-engineer-2) ⭐️ 7.0/10

**AI 日报**
1. [OpenAI 启动乌克兰新闻 AI 项目](#item-ai-daily-1) ⭐️ 6.8/10
2. [GPT-6 发布 OpenAI Agent Wiki](#item-ai-daily-2) ⭐️ 5.0/10

**AI 羊毛**
1. [免费 WhatsApp 购物车放弃通知 插件](#item-ai-deals-1) ⭐️ 5.0/10
2. [DepWarden 免费匿名依赖漏洞扫描](#item-ai-deals-2) ⭐️ 5.0/10
3. [PicFiddle 始终免费隐私图像编辑器](#item-ai-deals-3) ⭐️ 5.0/10

---

## Harness 架构

<a id="item-harness-arch-1"></a>
### [MCP Python SDK v2.2.0 发布](https://github.com/modelcontextprotocol/python-sdk/releases/tag/v2.2.0) ⭐️ 7.8/10

MCP Python SDK v2.2.0 发布。HTTP 客户端重定向仅限于端点同源。Streamable HTTP 会话空闲 30 分钟后默认过期。新增 issuer= 参数和会话管理选项。

github · maxisbey · 9月7日 15:53

**「改了什么」** HTTP 客户端重定向不再跟随跨域请求，空闲会话默认过期。新增 AuthSettings.validate\_token\_resource 和会话参数。

**标签**: `#mcp`, `#runtime`, `#protocol`, `#http-client`, `#breaking-changes`

---

<a id="item-harness-arch-2"></a>
### [MCP Python SDK v1.30.0 发布](https://github.com/modelcontextprotocol/python-sdk/releases/tag/v1.30.0) ⭐️ 6.8/10

MCP Python SDK 1.x 版本 v1.30.0 发布，更新了默认 HTTP 客户端重定向和空闲会话行为。streamable\_http\_client 和 sse\_client 仅在端点 origin 内跟随重定向，超出范围会失败。空闲 Streamable HTTP 会话在 30 分钟后过期，服务器同时持有的会话上限为 10000。新增了 session\_idle\_timeout 和 max\_sessions 参数，以及 OAuth issuer 检查。

github · maxisbey · 9月7日 14:03

**「改了什么」** HTTP 客户端重定向仅在 endpoint origin 内跟随，空闲 Streamable HTTP 会话在 30 分钟后过期。新增了 session\_idle\_timeout 和 max\_sessions 参数，以及 OAuth issuer 检查。

**标签**: `#mcp`, `#runtime`

---

<a id="item-harness-arch-3"></a>
### [browser-use GitHub trending](https://github.com/browser-use/browser-use) ⭐️ 5.0/10

browser-use 仓库进入 GitHub trending。该工具让 AI 代理能像人类一样操作网页浏览器：打开页面、点击按钮、输入文字、填写表单。你描述任务，它就能自动完成。例如填写表格任务：“用我的简历和信息填写这份求职申请。”

rss · GitHub Trending Daily · 9月7日 23:17

**标签**: `#tools`

---

## Agent 工程师日报

<a id="item-agent-engineer-1"></a>
### [OpenAI 研究加速：内部视图](https://simonwillison.net/2026/Sep/6/research-acceleration-the-view-inside-openai/) ⭐️ 7.0/10

OpenAI 分享内部研究团队使用 coding agents 加速研究的视图。2026 年 2 月至 8 月，研究者每日 AI 支出中位数从 0 增长至约 600 美元。2026 年 7 月底出现显著加速。影响 OpenAI 研究团队。

rss · Simon Willison · 9月6日 23:57

**「为什么重要」** OpenAI 研究团队每日 AI 支出中位数在 2026 年 7 月底显著上升。已发生的变化是研究工作流程的重塑，但具体原因尚未官方确认。

**「可关注」** 可关注：2026 年 7 月底研究者每日 AI 支出中位数显著上升。

**标签**: `#coding-agent`, `#harness`, `#eval`, `#orchestration`

---

<a id="item-agent-engineer-2"></a>
### [Iris-mini Iris-pro 搜索代理发布](https://huggingface.co/papers/2609.04304) ⭐️ 7.0/10

Iris-mini 和 Iris-pro 搜索代理分别在 35B-A3B 和 397B-A17B 规模下训练。任务从网页语料超链接实体图反向构建多跳轨迹。非答案实体重写为描述性参考，仅保留参考模型闭卷失败但证据提供后可解的问题。轨迹经轨道路径和轨迹级别过滤后 SFT，再通过 RL 针对 live search 优化，使用奖励判别器和观察总结器。该工作对代理训练、工具使用 harness 及评估系统产生影响。

rss · Hugging Face Daily Papers · 9月7日 00:00

**「为什么重要」** 已训练 Iris-mini 和 Iris-pro 搜索代理。实时搜索 RL 优化为工具使用 harness 提供新范式。

**「可关注」** 可关注：使用奖励判别器和观察总结器针对 live search 进行 RL 优化。

**标签**: `#eval`, `#orchestration`, `#coding-agent`, `#memory`, `#harness`

---

## AI 日报

<a id="item-ai-daily-1"></a>
### [OpenAI 启动乌克兰新闻 AI 项目](https://openai.com/index/supporting-independent-journalism-in-ukraine) ⭐️ 6.8/10

OpenAI、AIRPPU 和 WAN-IFRA 共同推出 AI 项目，帮助乌克兰新闻组织加强创新、韧性和独立新闻。该项目旨在提升乌克兰新闻业的创新能力和韧性。目前材料未提供具体实施细节或时间表。

rss · OpenAI Blog · 9月7日 00:00

**「可关注」** 可关注：OpenAI 与 AIRPPU、WAN-IFRA 合作推出 AI 项目支持乌克兰新闻组织。

**标签**: `#lab`, `#industry`, `#policy`

---

<a id="item-ai-daily-2"></a>
### [GPT-6 发布 OpenAI Agent Wiki](https://lastweekin.ai/p/last-week-in-ai-343-gpt-6-openais) ⭐️ 5.0/10

GPT-6 发布，OpenAI Agent 在 Wiki 上聊天讨论。Anthropic 推出 Claude Fable 5.1 并称其在 agentic 工作中成本可降低高达 45%。此外还有更多相关内容。

rss · Last Week in AI · 9月7日 13:02

**「为什么重要」** 本期报道了主要模型发布和 agentic 工作成本优化。

**「可关注」** 可关注：Claude Fable 5.1 在 agentic 工作中成本降低高达 45%

**标签**: `#model`, `#lab`, `#product`

---

## AI 羊毛

<a id="item-ai-deals-1"></a>
### [免费 WhatsApp 购物车放弃通知 插件](https://wordpress.org/plugins/6rsh-messaging-notifications/) ⭐️ 5.0/10

sixrsh 发布了免费 WhatsApp 购物车放弃通知 WordPress 插件。
该插件支持 WooCommerce 商店在购物车被放弃时发送 WhatsApp 通知。
免费使用，无额度限制，无到期时间。

rss · HN Free API / Credits · 9月7日 19:00

**「可关注」** 可关注：免费，无额度限制，无到期时间，适用于 WooCommerce 商店。

**标签**: `#free`, `#plugin`, `#woocommerce`, `#whatsapp`, `#abandoned-cart`

---

<a id="item-ai-deals-2"></a>
### [DepWarden 免费匿名依赖漏洞扫描](https://depwarden.in/blog/npm-pypi-typosquatting-2026-report) ⭐️ 5.0/10

DepWarden 是一个免费匿名依赖漏洞扫描器，支持 npm 和 PyPI 包。不需要账号或源代码上传，直接粘贴 manifest/lockfile，即可在隔离工作区中获得 OSV+KEV+EPSS 优先级的结果。作者还对 30 个最受欢迎的 npm/PyPI 包的单字符错别字同形词进行了研究，发现 32.7% 的 npm 注册同形词已被 OSV 恶意包数据库确认恶意。

rss · HN Free API / Credits · 9月7日 10:03

**「为什么重要」** 今天值得领取，因为它是完全免费且匿名的，不需要注册账号。

**「可关注」** 可关注：无需账号，直接粘贴 manifest/lockfile 即可获得优先级漏洞发现。

**标签**: `#free-tier`, `#promo`, `#api`

---

<a id="item-ai-deals-3"></a>
### [PicFiddle 始终免费隐私图像编辑器](https://picfiddle.com/) ⭐️ 5.0/10

PicFiddle 是一款始终免费的隐私优先图像编辑器。材料中未提及使用限额、注册要求或截止时间。

rss · HN Free API / Credits · 9月7日 01:09

**「可关注」** 始终免费隐私优先图像编辑器。

**标签**: `#free-tier`, `#promo`, `#image-editor`

---