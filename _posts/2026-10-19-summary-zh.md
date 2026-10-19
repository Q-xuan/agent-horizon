---
layout: default
title: "Horizon Summary: 2026-10-19 (ZH)"
date: 2026-10-19
lang: zh
---

> 从 160 条内容中筛选出 6 条重要资讯。

<nav id="ah-toc" class="ah-toc" aria-label="目录"><span class="ah-toc-title">目录</span><ul><li><a href="#sec-harness-arch"><span class="ah-toc-name">Harness 架构</span><span class="ah-toc-count">3条</span></a></li><li><a href="#sec-agent-engineer"><span class="ah-toc-name">Agent 工程师日报</span><span class="ah-toc-count">2条</span></a></li><li><a href="#sec-ai-deals"><span class="ah-toc-name">AI 羊毛</span><span class="ah-toc-count">1条</span></a></li></ul></nav>

---

**[Harness 架构](#sec-harness-arch)**
1. [vLLM v0.32.0 发布](#item-harness-arch-1) ⭐️ 7.8/10
2. [FastMCP v4.1.1 发布](#item-harness-arch-2) ⭐️ 5.3/10
3. [Claude Code 官方插件目录上 GitHub Trending](#item-harness-arch-3) ⭐️ 5.0/10

**[Agent 工程师日报](#sec-agent-engineer)**
1. [llm-echo 0.5 发布](#item-agent-engineer-1) ⭐️ 6.3/10
2. [DeepSeek 搜索抓取 API 定价 $0.75/千次](#item-agent-engineer-2) ⭐️ 6.0/10

**[AI 羊毛](#sec-ai-deals)**
1. [Show HN：WhatsApp MCP 免费跑 Cloudflare](#item-ai-deals-1) ⭐️ 5.0/10

---

## Harness 架构
{: #sec-harness-arch .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-harness-arch" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-harness-arch-1"></a>
### [vLLM v0.32.0 发布](https://github.com/vllm-project/vllm/releases/tag/v0.32.0) ⭐️ 7.8/10

vLLM v0.32.0 正式发布，新增结构化输出端点与通用解析器，扩展低精度 KV 缓存支持。POST /v1/systemone 端点支持 choice、noul、score 结构化决策，hf 工具与推理解析器通过读取 checkpoint 的 response\_template 消除模型特定集成。NVFP4 KV 缓存扩展至 SM8x、SM12x、SM90 及 SM100，GLM-5.x 在 SM100 默认启用 FP8 KV 缓存，KV 内存减半，吞吐提升 2.3-5.5%，TTFT 增加 7-11%。Model Runner V2 成为 ROCm 默认，Python 3.10 支持移除。

github · khluu · 10月18日 06:50

**「设计要点」** 运行时默认采用 Model Runner V2，支持 GPU n-gram 推测、弹性专家并行和流水线并行。工具层新增 hf 解析器，通过模型 checkpoint 的 response\_template 实现零集成工具调用与推理解析。KV 缓存层支持 NVFP4、FP8 及 ROCm 4-bit ultraquant\_4bit 格式，跨 SM8x 至 SM100 及 MiniMax-M3 稀疏注意力架构。

**「改了什么」** 新增 POST /v1/systemone 端点，提供 choice、noul、score 结构化决策能力。引入 --tool-call-parser hf 与 --reasoning-parser hf，模型自带 response\_template 时无需额外解析器。NVFP4 KV 缓存支持扩展至 SM8x、SM12x、SM90 及 MiniMax-M3 稀疏注意力，ROCm 新增 4-bit ultraquant\_4bit KV 缓存。Model Runner V2 成为 ROCm 默认并移除 MRV1 例外。Python 3.10 支持终止，默认 CORS 来源受限，torch.compile 序列并行与 AsyncTP 传递移除，cascade attention 与 mamba\_cache\_mode=&quot;all&quot; 移除。

**标签**: `#runtime`, `#tools`, `#memory`, `#planning`

---

<a id="item-harness-arch-2"></a>
### [FastMCP v4.1.1 发布](https://github.com/PrefectHQ/fastmcp/releases/tag/v4.1.1) ⭐️ 5.3/10

FastMCP v4.1.1 发布。该补丁版本修复正则工具搜索的拒绝服务漏洞，限制模式长度不超过 1,000 字符并设置约 1 秒超时；恢复 SkillsDirectoryProvider 对符号链接技能文件夹的发现能力，包括指向技能根目录外部的链接，但技能自身的文件仍须在其链接到的文件夹内解析；同时修复不可解析代理设置导致更新检查中断的问题，以及 JWKS 刷新锁被子类属性污染的问题。

github · zzstoatzz · 10月18日 02:12

**「改了什么」** 正则工具搜索增加长度与时间边界防止 DoS；SkillsDirectoryProvider 恢复符号链接技能文件夹发现并支持外部链接，但技能文件仍须在链接文件夹内解析；代理设置解析失败不再中止更新检查，JWKS 刷新锁清除子类属性。

**标签**: `#tools`, `#security`, `#mcp`

---

<a id="item-harness-arch-3"></a>
### [Claude Code 官方插件目录上 GitHub Trending](https://github.com/anthropics/claude-plugins-official) ⭐️ 5.0/10

这是 Anthropic 官方维护的 Claude Code 高质量插件目录，收录支持 MCP 等能力的插件；当前公开内容仅说明目录定位与安装安全提示，明确 Anthropic 不控制插件内包含的 MCP 服务器、文件或其他软件，也无法验证其功能与变更风险，未披露具体技术实现或 harness 变更细节。

rss · GitHub Trending Daily · 10月19日 01:26

**标签**: `#tools`, `#mcp`

---

## Agent 工程师日报
{: #sec-agent-engineer .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-agent-engineer" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-agent-engineer-1"></a>
### [llm-echo 0.5 发布](https://github.com/simonw/llm-echo/releases/tag/0.5) ⭐️ 6.3/10

2026 年 10 月 18 日，simonw 发布 llm-echo 0.5。该版本依赖 LLM&gt;=0.36，新增对 reasoning tokens 的支持，同时将模拟 token 用量统计的范围扩大到工具调用、推理文本与系统提示。llm-echo 是 LLM 生态的调试插件，可重复回传输入的 prompt，本次更新无架构变更，影响范围限于使用该工具做 agent 可观测性与成本跟踪调试的开发者。

github · simonw · 10月18日 23:16

**「为什么重要」** 该更新补全了带工具调用、推理 token 场景下的模拟 token 统计能力，方便开发者在无真实 LLM 调用时做成本与可观测性调试。目前未公开该统计规则的精度对比数据，实际效果需开发者自行验证。

**「可关注」** 可关注：llm-echo 0.5 的模拟 token 统计已覆盖工具调用、推理文本与系统提示，适配带 reasoning tokens 的 LLM 调试场景，需配合 LLM&gt;=0.36 使用。

**标签**: `#observability`, `#eval`, `#tooling`

---

<a id="item-agent-engineer-2"></a>
### [DeepSeek 搜索抓取 API 定价 $0.75/千次](https://api-docs.deepseek.com/guides/search/) ⭐️ 6.0/10

DeepSeek 于 2026-10-18 正式上线托管搜索与抓取 API，定价为每 1000 次成功请求 0.75 美元。该定价低于 Brave Search API 的 5 美元/千次、Kagi API 的 12 美元/千次，面向需为 AI agent 工具链集成搜索能力的工程师。目前公开材料未披露该 API 的限流规则、数据覆盖范围、可用区域等细节。

hackernews · fagnerbrack · 10月18日 06:50 · [社区讨论](https://news.ycombinator.com/item?id=50138531)

**「为什么重要」** 该 API 为 AI agent 工具链的搜索能力集成提供了新的低成本选项，可降低相关场景的调用成本。但当前公开信息未披露技术实现细节，也未证实会对现有搜索 API 市场或现有 agent 系统造成显著冲击。

**「可关注」** 可关注该 API 的限流规则、数据覆盖范围与区域可用性，这些是集成到 agent 工具链前的必要验证项。

**「评论」** 社区讨论中存在不同观点：部分用户认为自托管搜索工具（如 searxng-ai-kit）可免费替代付费搜索 API；也有用户推测搜索 API 价格未来可能走低甚至出现厂商付费提供的情况；另有用户指出当前付费搜索 API 存在的背景是谷歌未开放付费搜索接口。

**标签**: `#coding-agent`

---

## AI 羊毛
{: #sec-ai-deals .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-deals" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-deals-1"></a>
### [Show HN：WhatsApp MCP 免费跑 Cloudflare](https://github.com/finereli/whatsapp-mcp) ⭐️ 5.0/10

HN 社区用户 zoozla 分享开源 WhatsApp MCP 工具，可免费部署在 Cloudflare 免费层，支持个人 WhatsApp 账号接入 Claude，需关联 Google 账号获取联系人姓名，仅支持单用户部署，无官方设定的截止时间。

rss · HN Free API / Credits · 10月18日 21:36

**「为什么重要」** 此前个人用户将 WhatsApp 接入 Claude 需使用 WhatsApp Business 或自建服务器，该项目提供轻量免费部署方案，解决了个人用户的轻量接入需求。

**「可关注」** 可关注：单用户部署设计规避 WhatsApp 服务条款风险，需自行完成 Cloudflare 与 Google 账号的授权配置。

**标签**: `#api`, `#free-tier`

---