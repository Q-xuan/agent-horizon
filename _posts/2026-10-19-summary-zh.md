---
layout: default
title: "Horizon Summary: 2026-10-19 (ZH)"
date: 2026-10-19
lang: zh
---

> 从 134 条内容中筛选出 3 条重要资讯。

<nav id="ah-toc" class="ah-toc" aria-label="目录"><span class="ah-toc-title">目录</span><ul><li><a href="#sec-harness-arch"><span class="ah-toc-name">Harness 架构</span><span class="ah-toc-count">1条</span></a></li><li><a href="#sec-agent-engineer"><span class="ah-toc-name">Agent 工程师日报</span><span class="ah-toc-count">1条</span></a></li><li><a href="#sec-ai-daily"><span class="ah-toc-name">AI 日报</span><span class="ah-toc-count">1条</span></a></li></ul></nav>

---

**[Harness 架构](#sec-harness-arch)**
1. [vLLM v0.32.0 发布](#item-harness-arch-1) ⭐️ 7.8/10

**[Agent 工程师日报](#sec-agent-engineer)**
1. [DeepSeek 搜索抓取 API 定价发布](#item-agent-engineer-1) ⭐️ 7.0/10

**[AI 日报](#sec-ai-daily)**
1. [Anthropic 成立公共福利基金](#item-ai-daily-1) ⭐️ 8.8/10

---

## Harness 架构
{: #sec-harness-arch .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-harness-arch" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-harness-arch-1"></a>
### [vLLM v0.32.0 发布](https://github.com/vllm-project/vllm/releases/tag/v0.32.0) ⭐️ 7.8/10

vLLM v0.32.0 发布，引入结构化决策端点 \`POST /v1/systemone\` 与通用 \`hf\` 工具/推理解析器，降低模型特定配置需求。NVFP4 与 FP8 KV 缓存扩展至 SM8x、SM12x、SM90、SM100 架构，GLM-5.x 在 SM100 默认启用 FP8 KV 缓存。Model Runner V2 成为 ROCm 默认，移除多项旧特性。Python 3.10 支持终止，默认 CORS 策略收紧。

github · khluu · 10月18日 06:50

**「设计要点」** Model Runner V2 引入 GPU n-gram 推测器与 Elastic EP，MLA 模型支持流水线并行与 prefill 上下文并行，ROCm 上成为默认运行时。共享内存张量 arena 广播多模态张量，\`--api-server-count\` 启用 API worker 负载均衡。

**「改了什么」** 新增 \`POST /v1/systemone\` 端点与 \`hf\` 通用解析器，NVFP4/FP8 KV 缓存扩展至 SM8x/SM12x/SM90/SM100，Model Runner V2 成为 ROCm 默认。启动流程引入 FlashInfer 预编译内核与自动调优表持久化，API worker 负载均衡提升短请求吞吐；Python 3.10 支持终止，默认 CORS 策略收紧，移除 cascade attention 与 \`mamba\_cache\_mode=&quot;all&quot;\`。

**标签**: `#runtime`, `#tools`, `#prefix-cache`

---

## Agent 工程师日报
{: #sec-agent-engineer .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-agent-engineer" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-agent-engineer-1"></a>
### [DeepSeek 搜索抓取 API 定价发布](https://api-docs.deepseek.com/guides/search/) ⭐️ 7.0/10

2026 年 10 月 18 日，DeepSeek 官方上线托管搜索与抓取 API，定价为每 1000 次成功请求 0.75 美元，低于 Brave Search API 的 5 美元/千次、Kagi API 的 12 美元/千次，为 AI agent 工具链构建提供了新的低成本付费搜索选项。

hackernews · fagnerbrack · 10月18日 06:50 · [社区讨论](https://news.ycombinator.com/item?id=50138531)

**「为什么重要」** 该 API 以显著低于主流竞品的定价切入搜索市场，可能降低 AI agent 的搜索工具使用成本；但其实际结果覆盖范围、稳定性、请求成功率统计口径等尚未有公开验证，成本优势能否落地到实际工程场景仍不确定。

**「可关注」** 可关注：DeepSeek 该搜索抓取 API 的请求成功率定义、结果覆盖范围与 Brave、Kagi 的差异，以及集成到 coding agent 工具链时的实际延迟表现。

**「评论」** 社区讨论中，有开发者指出自建 searxng 等免费搜索方案成本更低；也有用户认为搜索 API 未来可能因流量控制权竞争出现负定价；另有评论确认了 Brave、Kagi API 的定价高于 DeepSeek 新服务。

**标签**: `#coding-agent`, `#harness`

---

## AI 日报
{: #sec-ai-daily .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-daily" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-daily-1"></a>
### [Anthropic 成立公共福利基金](https://www.anthropic.com/news/public-benefit-fund) ⭐️ 8.8/10

Anthropic 宣布成立 Anthropic Public Benefit Fund，需股东批准后先划转 5%的公司股份。后续公司估值较预设基线每上涨 50%，董事会可酌情追加 2%股份。该基金为全资 LLC，所持股份不得用于任何政治献金或游说。目前联合创始人及员工的股权捐赠承诺叠加本次划转，已覆盖约 20%的公司股份，后续将公布具体估值里程碑与基金治理细则。

rss · Anthropic News · 10月18日 00:00

**「为什么重要」** 这是 Anthropic 作为公益公司首次将股权激励逻辑转向公共福利，把公司增长红利直接绑定公益投入的自动扩容，而非仅依赖内部项目或一次性捐赠。

**「可关注」** 可关注：Anthropic 后续将公开该基金的估值里程碑、治理细则，以及 METR 等独立机构参与模型安全验证的机制。

**标签**: `#policy`, `#lab`, `#industry`

---