---
layout: default
title: "Horizon Summary: 2026-11-16 (ZH)"
date: 2026-11-16
lang: zh
---

> 从 142 条内容中筛选出 4 条重要资讯。

<nav id="ah-toc" class="ah-toc" aria-label="目录"><span class="ah-toc-title">目录</span><ul><li><a href="#sec-harness-arch"><span class="ah-toc-name">Harness 架构</span><span class="ah-toc-count">1条</span></a></li><li><a href="#sec-agent-engineer"><span class="ah-toc-name">Agent 工程师日报</span><span class="ah-toc-count">2条</span></a></li><li><a href="#sec-ai-daily"><span class="ah-toc-name">AI 日报</span><span class="ah-toc-count">1条</span></a></li></ul></nav>

---

**[Harness 架构](#sec-harness-arch)**
1. [Qwen Code 1.0 Preview 发布](#item-harness-arch-1) ⭐️ 5.0/10

**[Agent 工程师日报](#sec-agent-engineer)**
1. [Basalt 0.4.0 发布 支持多模型路由](#item-agent-engineer-1) ⭐️ 6.0/10
2. [datasette-llm 0.1a11 发布](#item-agent-engineer-2) ⭐️ 5.5/10

**[AI 日报](#sec-ai-daily)**
1. [OpenAI 上线科学博客](#item-ai-daily-1) ⭐️ 6.8/10

---

## Harness 架构
{: #sec-harness-arch .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-harness-arch" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-harness-arch-1"></a>
### [Qwen Code 1.0 Preview 发布](https://github.com/QwenLM/qwen-code) ⭐️ 5.0/10

Qwen Code 1.0 Preview 是通义千问开源的终端 AI 编程代理框架，该预览版整合了 Qoder 与 Qwen Code 的代理框架能力，支持终端、编辑器、桌面、浏览器、聊天等多端使用，当前未公开具体技术实现细节。

rss · GitHub Trending Daily · 11月15日 23:00

**标签**: `#runtime`, `#tools`

---

## Agent 工程师日报
{: #sec-agent-engineer .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-agent-engineer" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-agent-engineer-1"></a>
### [Basalt 0.4.0 发布 支持多模型路由](https://www.reddit.com/r/LocalLLaMA/comments/1xx1cu9/basalt_040_more_models_still_as_fast_qwen_27b_up/) ⭐️ 6.0/10

Basalt 项目维护者于 2026 年 11 月 15 日在 Reddit LocalLLaMA 社区发布 0.4.0 版本。本次更新新增首个稠密模型 Qwen 3.8 27B 的量化支持，在 5090 显卡上结构化输出最高达 776 tok/s，top-1 准确率 92.8%，对比 BF16 全精度模型的 KLD 为 0.0262；同时新增多模型路由、视频/文件上传、工具调用支持，上下文长度提升至 262K。该版本面向搭建本地 LLM 推理与 Agent 系统的工程师。

reddit · r/LocalLLaMA · /u/jesdga95 · 11月15日 17:30

**「为什么重要」** 该版本首次落地稠密模型量化推理方案，精度接近全精度 BF16，同时补全多模型路由、多模态输入等本地 Agent 常用能力，对搭建本地轻量推理与 Agent 系统的工程师有直接参考价值。

**「可关注」** 可关注：Basalt 0.4.0 的 Qwen 27B 量化方案在 5090 上实现了接近 BF16 精度的结构化输出吞吐，且已为 Qwen 4 的稠密内核做前期适配，可作为本地稠密模型推理的参考实现。

**标签**: `#orchestration`, `#coding-agent`

---

<a id="item-agent-engineer-2"></a>
### [datasette-llm 0.1a11 发布](https://simonwillison.net/2026/Nov/14/datasette-llm/) ⭐️ 5.5/10

2026 年 11 月 14 日，Datasette LLM 配置中间插件 datasette-llm 发布 0.1a11 alpha 版本，新增 OpenAI 兼容端点支持，支持 Datasette 对接 LM Studio、Ollama、llama.cpp 托管的本地 LLM。版本附带 uvx 运行示例，可快速启动集成本地模型的 Datasette Agent 实例。当前版本缺乏深度技术细节、性能数据与架构说明，实际兼容性待验证。

rss · Simon Willison · 11月14日 23:59

**「为什么重要」** 该版本让 Datasette 生态首次获得对接本地开源 LLM 服务的标准化接口，但当前为 alpha 版本，无公开性能基准与兼容性验证结果，实际工程落地价值尚不明确。

**「可关注」** 可关注：datasette-llm 0.1a11 的 OpenAI 兼容端点实现是否完整覆盖本地 LLM 服务的协议差异，以及 alpha 版本的接口稳定性。

**标签**: `#harness`, `#toolchain`

---

## AI 日报
{: #sec-ai-daily .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-daily" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-daily-1"></a>
### [OpenAI 上线科学博客](https://openai.com/index/our-new-blog-for-science) ⭐️ 6.8/10

OpenAI 正式上线全新科学博客。该博客用于发布研究团队利用 AI 推进科学发现的相关内容，包括新发现、实用方法以及研究者的 firsthand 经历。目前公开信息未披露该博客的更新频率、内容审核规则或具体首发内容安排。

rss · OpenAI Blog · 11月15日 22:00

**「为什么重要」** 这是 OpenAI 首次设立专门面向科学领域的博客渠道，后续其对外披露 AI for Science 相关研究成果的路径可能发生变化。

**「可关注」** 可关注：该博客后续发布的内容是否会同步公开配套的模型接口、数据集或复现指引。

**标签**: `#lab`, `#product`

---