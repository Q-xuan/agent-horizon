---
layout: default
title: "Horizon Summary: 2026-09-04 (EN)"
date: 2026-09-04
lang: en
---

> From 189 items, 21 important content pieces were selected

---

**Agent Harness Architecture**
1. [Cline Desktop v0.0.23 Released](#item-harness-arch-1) ⭐️ 7.8/10
2. [Microsoft Agent Framework python-1.17.0 发布](#item-harness-arch-2) ⭐️ 7.8/10
3. [Goose v1.49.0 发布](#item-harness-arch-3) ⭐️ 6.8/10
4. [Cline desktop-v0.0.23-beta.1 released](#item-harness-arch-4) ⭐️ 5.8/10
5. [Pydantic-ai v2.38.0 发布](#item-harness-arch-5) ⭐️ 5.8/10
6. [fastmcp v4.0.2 released](#item-harness-arch-6) ⭐️ 5.8/10
7. [LangChain 1.4.0 released](#item-harness-arch-7) ⭐️ 5.8/10

**AI Agent Engineer**
1. [350M 模型 GRPO 微调 结构化输出](#item-agent-engineer-1) ⭐️ 7.8/10
2. [GPT-6 Astra 发布](#item-agent-engineer-2) ⭐️ 7.0/10
3. [S3Gym: LLM Self-Improvement Benchmark](#item-agent-engineer-3) ⭐️ 7.0/10
4. [K2-Horizon-MoVA-36B-A4B GGUF 发布](#item-agent-engineer-4) ⭐️ 7.0/10
5. [GPT-6 Astra 发布](#item-agent-engineer-5) ⭐️ 6.0/10
6. [NeoMME: efficient multilingual multimodal encoder](#item-agent-engineer-6) ⭐️ 5.8/10
7. [WeatherNext 3 AI Model Announced](#item-agent-engineer-7) ⭐️ 5.8/10

**AI Daily**
1. [OpenAI Daybreak $1B Frontline Defenders](#item-ai-daily-1) ⭐️ 7.8/10
2. [Playco Cuts Manual Fixes 50% with GPT-6 Astra](#item-ai-daily-2) ⭐️ 7.8/10
3. [GPT-6 Astra Safety Overview](#item-ai-daily-3) ⭐️ 7.8/10
4. [GitHub Copilot app for Beginners: Run several agents at once](#item-ai-daily-4) ⭐️ 6.8/10
5. [ZGateway: Proxy for ZippyDB](#item-ai-daily-5) ⭐️ 6.8/10

**AI Deals**
1. [CloudCone SSD VPS Restock at 96 RMB/Year](#item-ai-deals-1) ⭐️ 7.0/10

**AI Creator Radar**
1. [Simon Willison retweets criticism of linking to LLM-generated articles](#item-ai-creator-1) ⭐️ 0.0/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [Cline Desktop v0.0.23 Released](https://github.com/cline/cline/releases/tag/desktop-v0.0.23) ⭐️ 7.8/10

Cline desktop v0.0.23 has been released. It adds shared Hub-managed Agent Plugin discovery and automatic MCP server initialization from ~/.agents/plugins. Agent Plugins are validated from plugin.json, making valid Agent Skills available to the agent, and stdio/Streamable HTTP/SSE MCP servers start automatically. Settings now list Agent Plugins separately from Cline Plugins.

github · github-actions\[bot\] · Sep 3, 18:33

**「What Changed」** This release adds shared Hub-managed Agent Plugin discovery and automatic MCP server initialization from ~/.agents/plugins. It also fixes the recurring &quot;Cline Hub was updated&quot; dialog on launch, shows device confirmation codes during sign-in, routes voice input failures to settings, and resolves vanishing scheduled-task reports and wedged MCP servers.

**Tags**: `#runtime`, `#tools`, `#mcp`

---

<a id="item-harness-arch-2"></a>
### [Microsoft Agent Framework python-1.17.0 发布](https://github.com/microsoft/agent-framework/releases/tag/python-1.17.0) ⭐️ 7.8/10

Microsoft Agent Framework Python 1.17.0 is released. The release restores sequence-only agent middleware inputs and removes the experimental agent-hooks core extra. It documents the same-event-loop concurrency contract for shared chat clients, supports OpenAI SDK 3.x, migrates Mistral clients to official SDK, and adds Foundry-hosted Telegram agent samples.

github · moonbox3 · Sep 3, 09:49

**「改了什么」** Restored sequence-only agent middleware inputs and removed the experimental agent-hooks core extra. Added support for OpenAI SDK 3.x and Foundry-hosted Telegram agent samples.

**Tags**: `#runtime`, `#tools`, `#memory`

---

<a id="item-harness-arch-3"></a>
### [Goose v1.49.0 发布](https://github.com/aaif-goose/goose/releases/tag/v1.49.0) ⭐️ 6.8/10

Goose v1.49.0 release adds auto-updater for the desktop application and Linux ARM64 packages. Background extension loading makes the CLI prompt immediately usable. New features include title sessions by subject, interactive git branch indicator, on\_failure PreToolUse hooks, web-search and browser skills, model-native audio transcription, and auto-focus chat input. New declarative providers such as Opper and Databricks Unity Catalog are added.

github · github-actions\[bot\] · Sep 3, 19:34

**「改了什么」** Relative to prior version, this release introduces auto-updater, Linux ARM64 desktop packages, background extension loading, and on\_failure PreToolUse hooks. New declarative providers and skills for web search, browser use, and audio transcription are also added.

**Tags**: `#runtime`, `#tools`

---

<a id="item-harness-arch-4"></a>
### [Cline desktop-v0.0.23-beta.1 released](https://github.com/cline/cline/releases/tag/desktop-v0.0.23-beta.1) ⭐️ 5.8/10

Cline desktop v0.0.23-beta.1 introduces image generation tool configuration and runtime-based scheduling grouping. Configure and opt in to image generation under Customize → Tools. Provider credentials stay server-side, and generated images remain available in session history. Scheduled runs are grouped within their runtime environment so similarly named local and SSH schedules stay separate. Includes all stable desktop improvements through 0.0.22.

github · github-actions\[bot\] · Sep 3, 01:46

**「设计要点」** Image generation is configured under Tools with server-side credential handling. Generated images persist in session history. Scheduled runs are grouped by runtime environment to keep local and SSH schedules separate. Media-generation settings apply only to the local runtime.

**「改了什么」** Adds image generation under Tools with server-side credential handling and session history persistence. Clarifies runtime environment grouping for schedules and local-only media settings.

**Tags**: `#runtime`, `#tools`, `#memory`

---

<a id="item-harness-arch-5"></a>
### [Pydantic-ai v2.38.0 发布](https://github.com/pydantic/pydantic-ai/releases/tag/v2.38.0) ⭐️ 5.8/10

Pydantic-ai v2.38.0 is released. It introduces typed event emission and subscription in run streams, context window support in profiles, new model integrations, and changes to capability handling. This release adds the @on\_event decorator to allow applications to emit and subscribe to typed CustomEvent and CapabilityEvent in the run event stream. It also adds context\_window to ModelProfile and context\_window\_used to RunContext, along with support for several new models and providers.

github · adtyavrdhn · Sep 3, 07:48

**「改了什么」** Pydantic-ai v2.38.0 adds typed event emission and subscription in run streams via the @on\_event decorator, context\_window to ModelProfile and RunContext, support for new models including gemini-3.8-flash, claude-fable-5-1, claude-mythos-5-1, and VLLMProvider, and a profile flag to reject streams without finish\_reason.

**Tags**: `#runtime`, `#memory`, `#subagents`, `#tools`, `#planning`

---

<a id="item-harness-arch-6"></a>
### [fastmcp v4.0.2 released](https://github.com/PrefectHQ/fastmcp/releases/tag/v4.0.2) ⭐️ 5.8/10

fastmcp v4.0.2 is released. ClientGroup is now importable from the package root with \`from fastmcp import ClientGroup\` for better integration flexibility. Accompanying documentation updates are included.

github · zzstoatzz · Sep 2, 23:27

**「What Changed」** ClientGroup is exposed from the package root to reduce internal module coupling in integrations. Minor documentation and changelog fixes were also applied.

**Tags**: `#mcp`, `#tools`, `#runtime`

---

<a id="item-harness-arch-7"></a>
### [LangChain 1.4.0 released](https://github.com/langchain-ai/langchain/releases/tag/langchain%3D%3D1.4.0) ⭐️ 5.8/10

LangChain 1.4.0 is released, introducing the langchain.mcp namespace and MCPAdapter. Agent tool routing improvements include model destination. Middleware trace inputs are omitted for Anthropic to improve performance. Runnable examples for langchain.mcp are documented.

github · github-actions\[bot\] · Sep 3, 16:59

**「What changed」** LangChain 1.4.0 adds the langchain.mcp namespace and MCPAdapter. It includes model destination in agent tool routing, omits middleware trace inputs for Anthropic, and updates documentation for runnable MCP examples.

**Tags**: `#mcp`, `#tools`, `#runtime`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [350M 模型 GRPO 微调 结构化输出](https://huggingface.co/blog/grpo-with-trl-ifstruct) ⭐️ 7.8/10

Hugging Face blog post details GRPO fine-tuning of LiquidAI/LFM2.5-350M with TRL in 100 steps for structured outputs. Base model scores 22.6% on IFStruct benchmark via llama.cpp server. Training uses 500 augmented samples from Nemotron data with LoRA targeting 6M parameters in q\_proj, k\_proj, v\_proj, out\_proj, in\_proj, w1, w2, w3. Three reward functions score json\_format, field\_count, and schema\_validation.

rss · Hugging Face Blog · Sep 3, 00:00

**「为什么重要」** Schema compliance decides whether an LLM integrates into downstream systems. This shows targeted GRPO fine-tuning of small models can improve structured output performance.

**「可关注」** 可关注：GRPO with 8 generations per prompt group and 100 steps trains LoRA adapters on hybrid architectures for schema compliance.

**Tags**: `#eval`, `#orchestration`, `#coding-agent`, `#harness`

---

<a id="item-agent-engineer-2"></a>
### [GPT-6 Astra 发布](https://www.latent.space/p/astra) ⭐️ 7.0/10

Latent Space 花费了 20B+ tokens 探索 GPT-6 Astra，这是一款每小时不到 6 美元的自动化 AI 工程师。他们分享了关于 AI Agent 工具、工作流以及成本/性能细节的见解，这些与 harness、orchestration 和 eval 相关。

rss · Latent Space · Sep 3, 21:09

**「为什么重要」** 文章分享了 GPT-6 Astra 的探索学习，但其对实际工作流的影响尚未证实。

**「可关注」** 可关注：20B+ tokens 的 GPT-6 Astra 探索。

**Tags**: `#coding-agent`, `#harness`, `#orchestration`, `#eval`

---

<a id="item-agent-engineer-3"></a>
### [S3Gym: LLM Self-Improvement Benchmark](https://huggingface.co/papers/2608.31100) ⭐️ 7.0/10

S³Gym is an interactive benchmark evaluating LLM self-improvement through three coupled capabilities: Self-Testing, Self-Judging, and Self-Improvement. It instantiates the protocol in seven text-based games with executable environment verifiers and separates permissive exploration from strict held-out evaluation. Three pathways for incorporating interaction experience are tested.

rss · Hugging Face Daily Papers · Sep 3, 00:00

**「Why it matters」** The benchmark directly tests self-improvement in LLMs interacting with environments, with relevance to agent evaluations and harnesses.

**「Key takeaway」** Observe: LLMs can potentially use self-testing and self-judging to improve future decisions via accumulated experience in text games.

**Tags**: `#eval`, `#harness`, `#coding-agent`, `#orchestration`

---

<a id="item-agent-engineer-4"></a>
### [K2-Horizon-MoVA-36B-A4B GGUF 发布](https://www.reddit.com/r/LocalLLaMA/comments/1w67wso/ifmk2horizonmova36ba4bgguf_hugging_face/) ⭐️ 7.0/10

IFM 官方发布了 K2-Horizon-MoVA-36B-A4B 模型。该模型为稀疏 MoE 架构，参数总量 36B，激活参数仅 4B，使用 MoVA 注意力机制。原生支持 524288 token 上下文。基准测试显示，在代理和推理任务上，该模型超越了约 30B 参数的稠密模型和高达 15 倍更大的 MoE 模型，并与闭源前沿模型相当。同时发布了多个 GGUF 量化版本，并将开源中间检查点、训练数据和训练代码。

reddit · r/LocalLLaMA · /u/jacek2023 · Sep 3, 13:47

**「为什么重要」** 低激活参数实现前沿性能，适合本地 agent 部署和 harness；512K 上下文原生支持，便于长上下文任务。

**「可关注」** 本地运行时优先使用 GGUF 量化文件；关注中间检查点的发布，以便研究训练过程中的能力变化。

**Tags**: `#eval`, `#memory`, `#harness`, `#coding-agent`, `#orchestration`

---

<a id="item-agent-engineer-5"></a>
### [GPT-6 Astra 发布](https://openai.com/index/gpt-6-astra/) ⭐️ 6.0/10

OpenAI 发布了 GPT-6 Astra 模型，在 ARC-AGI-3 基准测试中达到 99.9% 的高分，并在 Artificial Analysis Coding Agent Index 上取得显著进步。社区讨论指出，ARC-AGI-3 的分数是使用 Responses API harness 估算的，之前模型如 GPT-5.6 Sol 的分数可能被低估。影响包括对 AI 代理评估标准的重新评估。

hackernews · kibae · Sep 3, 18:41 · [Discussion](https://news.ycombinator.com/item?id=49554643)

**「为什么重要」** 该模型在代理基准上的表现为 AI 代理开发提供了新的参考点，尽管改进幅度适中。

**「可关注」** 可关注：ARC-AGI-3 评分依赖 Responses API harness，之前模型如 GPT-5.6 Sol 的分数可能被低估。

**「评论」** 社区讨论焦点在于 ARC-AGI-3 评分的可信度，指出其依赖特定 harness 实现，可能导致误导。部分用户认为其他基准改进属于点更新范畴，而非突破性进展。

**Tags**: `#eval`, `#harness`, `#coding-agent`

---

<a id="item-agent-engineer-6"></a>
### [NeoMME: efficient multilingual multimodal encoder](https://huggingface.co/blog/Hcompany/neomme) ⭐️ 5.8/10

Hugging Face Blog introduces NeoMME, a family of 260M and 800M multilingual multimodal encoders. A single bidirectional Transformer processes text tokens and raw image patches from scratch, trained with a masked discrete-diffusion objective. Fine-tuned for visual document retrieval, NeoMME-Retriever returns dense and late-interaction embeddings in one forward pass and reaches competitive nDCG@10 scores on ViDoRe v3 with higher throughput and 255× smaller index storage than prior models.

rss · Hugging Face Blog · Sep 3, 13:13

**「What to watch」** What to watch: NeoMME-260M encodes 51 pages per second at 2048×2048 resolution on an NVIDIA L40S GPU—twice ColModernVBERT—while hierarchical token pooling and asymmetric quantization reduce late-interaction index storage 255× to 6 kB per page with over 95% of baseline nDCG@10 retained.

**Tags**: `#eval`, `#harness`, `#orchestration`

---

<a id="item-agent-engineer-7"></a>
### [WeatherNext 3 AI Model Announced](https://deepmind.google/blog/introducing-weathernext-3-our-most-advanced-and-accurate-global-weather-ai-model/) ⭐️ 5.8/10

Google DeepMind announced WeatherNext 3 as their most advanced and accurate global weather AI model. The announcement is an official first-hand release with no accompanying technical details, code, architecture papers, or reproducible evaluation breakthroughs. No impacts on coding agents, harnesses, evals, memory, orchestration, permissions, or observability are mentioned.

rss · Google DeepMind · Sep 3, 15:02

**Tags**: `#eval`, `#harness`, `#orchestration`

---

## AI Daily

<a id="item-ai-daily-1"></a>
### [OpenAI Daybreak $1B Frontline Defenders](https://openai.com/index/daybreak-for-frontline-defenders) ⭐️ 7.8/10

OpenAI announced the Daybreak initiative. It commits $1 billion to provide frontier cyber AI tools, training, and support to frontline defenders. The focus is protecting essential services.

rss · OpenAI Blog · Sep 3, 13:15

**「Why It Matters」** The $1 billion commitment expands frontier cyber AI access to defenders of critical services.

**「Key Takeaway」** Key Takeaway: The $1 billion commitment expands access to frontier cyber AI tools, training, and support for essential services.

**Tags**: `#lab`, `#policy`, `#product`, `#industry`

---

<a id="item-ai-daily-2"></a>
### [Playco Cuts Manual Fixes 50% with GPT-6 Astra](https://openai.com/index/playco-game-prototyping-with-astra) ⭐️ 7.8/10

Using GPT-6 Astra, Playco built three themed game prototypes from one grey box foundation. The company reported 50% fewer manual fixes than with the previous model.

rss · OpenAI Blog · Sep 3, 12:00

**「Why it matters」** This real-world use case shows how GPT-6 Astra can streamline game prototyping and cut manual effort in half.

**「Engineer takeaway」** Key takeaway: 50% fewer manual fixes when prototyping games with GPT-6 Astra from a grey box foundation.

**Tags**: `#model`, `#lab`, `#industry`, `#product`

---

<a id="item-ai-daily-3"></a>
### [GPT-6 Astra Safety Overview](https://openai.com/index/safety-overview-gpt-6-astra) ⭐️ 7.8/10

OpenAI&\#x27;s blog posts a safety overview for GPT-6 Astra. GPT-6 Astra is their most capable broadly deployed model. It is the first to reach the Critical level of cybersecurity capability under the Preparedness Framework.

rss · OpenAI Blog · Sep 3, 00:00

**「Key Takeaway」** Key takeaway: GPT-6 Astra is the first model to reach the Critical level of cybersecurity capability under the Preparedness Framework.

**Tags**: `#model`, `#openai`, `#safety`, `#cybersecurity`, `#policy`

---

<a id="item-ai-daily-4"></a>
### [GitHub Copilot app for Beginners: Run several agents at once](https://github.blog/ai-and-ml/github-copilot/github-copilot-app-for-beginners-run-several-agents-at-once/) ⭐️ 6.8/10

The GitHub Copilot app now supports running parallel agents. This feature lets users run several agents at once, helping beginners move from feeling scared to feeling powerful. The tutorial appears on the official GitHub blog.

rss · GitHub Blog · Sep 3, 16:00

**「Why it matters」** Running parallel agents in the Copilot app makes the tool more efficient and accessible for beginners.

**「Takeaway」** Takeaway: Run several agents at once in the Copilot app.

**Tags**: `#github`, `#copilot`, `#product`, `#industry`

---

<a id="item-ai-daily-5"></a>
### [ZGateway: Proxy for ZippyDB](https://engineering.fb.com/2026/09/03/core-infra/zgateway-proxy-zippydb-meta/) ⭐️ 6.8/10

Meta introduced ZGateway, a proxy that unifies traffic for its most widely used key value store ZippyDB. ZippyDB backs product metadata, counters, and configuration and can serve billions of requests. The proxy adds admission control, load balancing, cross-region resilience, and richer operations.

rss · Engineering at Meta · Sep 3, 16:00

**「Why It Matters」** The proxy unifies traffic management for one of Meta&\#x27;s largest systems while adding resilience and control features.

**「Takeaway」** Takeaway: A proxy in front of a KV store enables admission control, load balancing, cross-region resilience, and richer operations.

**Tags**: `#lab`, `#infra`, `#product`

---

## AI Deals

<a id="item-ai-deals-1"></a>
### [CloudCone SSD VPS Restock at 96 RMB/Year](https://www.appinn.com/cloudcone-ssd-vps/) ⭐️ 7.0/10

CloudCone is restocking its SSD VPS during the Turns 9 Sale. The lowest tier costs 96 RMB per year \(14.24 USD\) with Alipay support. Recommended packages include 1 IPv4 and 3 IPv6 addresses.

rss · 小众软件 · Sep 3, 09:07

**Tags**: `#promo`, `#coupon`, `#vps`

---

## AI Creator Radar

<a id="item-ai-creator-1"></a>
### [Simon Willison retweets criticism of linking to LLM-generated articles](https://twitter.com/simonw/status/tweet-2095379448426320145) ⭐️ 0.0/10

Simon Willison retweeted a post from @bcantrill. The post states: &\#x27;To those linking to pieces that are obviously 100% LLM generated: do you... actually read them? I can&\#x27;t make it through the…&\#x27;. This commentary addresses concerns about linking to AI-generated content and questions its actual readership.

twitter · Simon Willison · Sep 3, 05:12

**「Content angle」** Content angle: Simon Willison questions whether links to obviously LLM-generated articles are actually read.

**Tags**: `#AI generated content`, `#LLM spam`, `#content quality`, `#Simon Willison`, `#Twitter commentary`

---