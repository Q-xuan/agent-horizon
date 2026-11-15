---
layout: default
title: "Horizon Summary: 2026-11-16 (EN)"
date: 2026-11-16
lang: en
---

> From 142 items, 4 important content pieces were selected

---

**Agent Harness Architecture**
1. [Qwen Code 1.0 Preview 发布](#item-harness-arch-1) ⭐️ 5.0/10

**AI Agent Engineer**
1. [Basalt 0.4.0 发布](#item-agent-engineer-1) ⭐️ 6.0/10
2. [datasette-llm 本地模型支持](#item-agent-engineer-2) ⭐️ 5.5/10

**AI Daily**
1. [OpenAI 上线科学博客](#item-ai-daily-1) ⭐️ 6.8/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [Qwen Code 1.0 Preview 发布](https://github.com/QwenLM/qwen-code) ⭐️ 5.0/10

Qwen Code 1.0 Preview is an open-source AI coding agent harness announced on GitHub Trending. It merges the agent harness capabilities of Qoder and Qwen Code into one open-source release. The agent runs in terminals, editors, desktops, browsers, and chat interfaces. The source material provides no technical implementation details, architecture specifics, or changelog information.

rss · GitHub Trending Daily · Nov 15, 23:00

**Tags**: `#runtime`, `#tools`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [Basalt 0.4.0 发布](https://www.reddit.com/r/LocalLLaMA/comments/1xx1cu9/basalt_040_more_models_still_as_fast_qwen_27b_up/) ⭐️ 6.0/10

Basalt 0.4.0 于 2026-11-15 发布，新增首个 dense 模型 Qwen 3.8 27B 支持。在 5090 单流环境下，结构化输出最高 776 tok/s，对话 262 tok/s，prose 194 tok/s；prefill 在 4k 上下文时达 12,000 tok/s，随上下文增长而下降。该模型 top-1 准确率 92.8%，相对 BF16 基线的 KLD 为 0.0262。本次更新同时加入多模型路由、视频/文件支持、工具调用与图像输入，上下文长度上限扩至 262K。

reddit · r/LocalLLaMA · /u/jesdga95 · Nov 15, 17:30

**「为什么重要」** 对构建本地 agent 系统的工程师而言，Basalt 0.4.0 提供了 dense 模型在消费级显卡上的吞吐量参考基线（776 tok/s 结构化输出），可用于评估本地推理组件的性能预算。但该项目定位 niche，尚未形成广泛行业影响，多数团队仅需快速扫描。

**「可关注」** 可关注：Basalt 对 Qwen 3.8 27B 的量化实现达到 92.8% top-1 准确率（相对 BF16 KLD 0.0262），说明该 dense kernel 路线在精度与速度间取得了可验证的平衡，可作为本地 agent 推理模块的参考实现。

**Tags**: `#orchestration`, `#coding-agent`

---

<a id="item-agent-engineer-2"></a>
### [datasette-llm 本地模型支持](https://simonwillison.net/2026/Nov/14/datasette-llm/) ⭐️ 5.5/10

2026-11-14，Simon Willison 发布 datasette-llm 0.1a11。该插件作为 Datasette 的 LLM 配置中间层，供其他 Datasette 插件调用，本次更新新增 OpenAI 兼容端点支持。用户可配置 \`api\_base\` 接入 LM Studio、Ollama 或 llama.cpp 托管的本地模型。文章提供通过 \`uvx --with datasette-agent\` 启动 Datasette Agent 的命令示例，截图显示 agent 执行 \`sql\_query\` 工具查询数据库，返回 200 个 repos 和 1,889 个 releases。当前为 0.1a11 alpha 版本，未披露性能数据或架构细节。

rss · Simon Willison · Nov 14, 23:59

**「为什么重要」** 该更新使 Datasette Agent 能直接对接本地模型服务，降低本地部署 LLM 应用的门槛。但作为 alpha 版本，接口稳定性和生产可用性尚未验证。

**「可关注」** 可关注：datasette-llm 通过 OpenAI 兼容端点抽象 LLM 后端，使 Datasette 插件无需修改即可接入 LM Studio、Ollama 或 llama.cpp，但 0.1a11 为 alpha 版本，接口稳定性未经验证。

**Tags**: `#harness`, `#toolchain`

---

## AI Daily

<a id="item-ai-daily-1"></a>
### [OpenAI 上线科学博客](https://openai.com/index/our-new-blog-for-science) ⭐️ 6.8/10

OpenAI launched a new science blog on November 15, 2026, to publish new findings, practical methods, and firsthand accounts from researchers using AI to advance scientific discovery. The announcement does not include specific technical research results or policy adjustments.

rss · OpenAI Blog · Nov 15, 22:00

**「为什么重要」** This is OpenAI&\#x27;s first dedicated publishing channel for AI-driven scientific discovery research, making it easier for relevant researchers to access first-hand information in this field.

**「可关注」** 可关注：OpenAI has added an official dedicated channel for publishing content related to AI scientific discovery.

**Tags**: `#lab`, `#product`

---