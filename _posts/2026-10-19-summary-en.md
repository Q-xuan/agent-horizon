---
layout: default
title: "Horizon Summary: 2026-10-19 (EN)"
date: 2026-10-19
lang: en
---

> From 134 items, 3 important content pieces were selected

---

**Agent Harness Architecture**
1. [vLLM v0.32.0 发布](#item-harness-arch-1) ⭐️ 7.8/10

**AI Agent Engineer**
1. [DeepSeek 搜索抓取 API 上线 定价 0.75 美元/千次](#item-agent-engineer-1) ⭐️ 7.0/10

**AI Daily**
1. [Anthropic 公共福利基金启动](#item-ai-daily-1) ⭐️ 8.8/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [vLLM v0.32.0 发布](https://github.com/vllm-project/vllm/releases/tag/v0.32.0) ⭐️ 7.8/10

vLLM v0.32.0 发布，新增 \`POST /v1/systemone\` 结构化决策端点与通用 \`hf\` 工具/推理解析器，后者通过读取 checkpoint 的 \`response\_template\` 消除模型特定解析器配置。低精度 KV 缓存扩展至 NVFP4 在 SM8x/SM12x/SM90/SM100 及 MiniMax-M3 稀疏注意力 SM100 的支持，GLM-5.x 在 SM100 默认启用 FP8 KV 缓存。Model Runner V2 成为 ROCm 默认运行时，移除模型特定 MRV1 例外。安全修复涵盖 CVE GHSA-4hhp-h66f-j5j7 等三项，默认 CORS 来源受限，Python 3.10 支持终止。

github · khluu · Oct 18, 06:50

**「设计要点」** Model Runner V2 成为 ROCm 默认运行时并移除模型特定例外，共享内存张量 arena 将大多模态张量一次性广播给 worker，\`--api-server-count\` 负载均衡将连接分发至最轻量 API worker。低精度 KV 缓存（NVFP4/FP8）覆盖 SM8x/SM12x/SM90/SM100 多架构，通用解析器在 Python 与 Rust 前端统一工具调用与推理格式。

**「改了什么」** 新增 \`POST /v1/systemone\` 结构化决策端点与通用 \`hf\` 解析器（读取 \`response\_template\` 免模型特定配置），NVFP4 KV 缓存扩展至 SM8x/SM12x/SM90/SM100 及 MiniMax-M3 稀疏注意力 SM100，Model Runner V2 成为 ROCm 默认运行时。新增 \`vllm download-kernels\` 与 \`vllm preload --preload-autotune\` 加速启动；破坏性变更包括终止 Python 3.10、默认 CORS 来源受限、\`max\_tokens\` 不再从上下文窗口预留。

**Tags**: `#runtime`, `#tools`, `#prefix-cache`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [DeepSeek 搜索抓取 API 上线 定价 0.75 美元/千次](https://api-docs.deepseek.com/guides/search/) ⭐️ 7.0/10

2026年10月18日，DeepSeek官方上线托管搜索与抓取API，定价为每1000次成功请求0.75美元。该定价显著低于Brave Search API的5美元/千次、Kagi API的12美元/千次，定位为AI agent开发的低成本搜索工具替代选项。目前公开信息仅包含定价，未披露调用限制、返回格式、可用区域等其他细节。

hackernews · fagnerbrack · Oct 18, 06:50 · [Discussion](https://news.ycombinator.com/item?id=50138531)

**「为什么重要」** 对于构建AI agent工具链的开发者而言，该API提供了新的低成本搜索能力选项，有望降低agent开发中的搜索相关成本。但目前仅公开定价，实际可用性、稳定性等细节尚未披露，影响尚未完全明确。

**「可关注」** 可关注：该API的调用频率限制、返回结果质量、区域可用性等尚未公开的细节，以及其与自建搜索方案（如searxng-ai-kit）的成本、稳定性对比。

**「评论」** 社区讨论中，有开发者指出自建搜索工具（如searxng-ai-kit）可免费替代托管搜索服务；也有用户讨论搜索API未来可能因流量控制权竞争出现负定价；还有观点认为这类托管搜索服务存在的原因是谷歌未提供付费搜索API。

**Tags**: `#coding-agent`, `#harness`

---

## AI Daily

<a id="item-ai-daily-1"></a>
### [Anthropic 公共福利基金启动](https://www.anthropic.com/news/public-benefit-fund) ⭐️ 8.8/10

Anthropic 宣布设立 Anthropic Public Benefit Fund。公司拟注入 5% 股份（须股东批准），并设定动态追加机制：估值较基准每上涨 50%，董事会可追加 2% 股份。基金采用全资 LLC 架构，排除政治用途。叠加创始人 80% 股权捐赠承诺及员工匹配计划后，约 20% 股份将用于公益。

rss · Anthropic News · Oct 18, 00:00

**「为什么重要」** 该基金将公益股权与公司估值增长直接挂钩，并明确排除政治献金。其规模随公司成长自动扩大，为 Anthropic 已承诺的 2 亿美元劳动力市场研究提供了潜在补充路径。

**「可关注」** 可关注：基金采用 LLC 而非 501\(c\)\(3\) 架构，以换取捐赠形式灵活性；后续公布的估值里程碑与治理细节将决定实际公益规模。

**Tags**: `#policy`, `#lab`, `#industry`

---