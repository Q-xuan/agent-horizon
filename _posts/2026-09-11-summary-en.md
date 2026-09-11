---
layout: default
title: "Horizon Summary: 2026-09-11 (EN)"
date: 2026-09-11
lang: en
---

> From 207 items, 19 important content pieces were selected

---

**Agent Harness Architecture**
1. [Claude Code v2.1.268 发布](#item-harness-arch-1) ⭐️ 7.8/10
2. [Codex python-v0.154.0 发布](#item-harness-arch-2) ⭐️ 7.8/10
3. [google/adk-python v2.9.0 released](#item-harness-arch-3) ⭐️ 7.8/10
4. [Cline desktop-v0.0.25 发布](#item-harness-arch-4) ⭐️ 6.8/10
5. [openai-agents-js v0.18.0 发布](#item-harness-arch-5) ⭐️ 6.8/10
6. [Agent Framework python-1.18.0 发布](#item-harness-arch-6) ⭐️ 6.8/10
7. [E2B 2.49.1 发布](#item-harness-arch-7) ⭐️ 5.8/10

**AI Agent Engineer**
1. [Shopify Reverts to Native Mobile with AI Agents](#item-agent-engineer-1) ⭐️ 8.0/10
2. [SWE-2 Pushing the Pareto Frontier](#item-agent-engineer-2) ⭐️ 7.8/10
3. [OpenAI Agents API 发布](#item-agent-engineer-3) ⭐️ 7.0/10

**AI Daily**
1. [OpenAI Expands AI Access to Governments](#item-ai-daily-1) ⭐️ 9.8/10
2. [ChatGPT for Financial Services](#item-ai-daily-2) ⭐️ 7.8/10
3. [Codex and ChatGPT Search for New Antimicrobial Molecules](#item-ai-daily-3) ⭐️ 6.8/10
4. [DeepSeek V4.1 Flash Released](#item-ai-daily-4) ⭐️ 6.8/10
5. [OpenAI Data Agent in ChatGPT Work](#item-ai-daily-5) ⭐️ 5.8/10
6. [GitHub Copilot 应用 for Beginners 指南](#item-ai-daily-6) ⭐️ 5.8/10

**AI Deals**
1. [Mathathon Challenge 40 Hours $2M+ AI Credits](#item-ai-deals-1) ⭐️ 8.0/10
2. [geoSurge.ai 免费品牌可见性](#item-ai-deals-2) ⭐️ 6.0/10
3. [Modeinspect 99天免费AI积分上线](#item-ai-deals-3) ⭐️ 5.0/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [Claude Code v2.1.268 发布](https://github.com/anthropics/claude-code/releases/tag/v2.1.268) ⭐️ 7.8/10

Claude Code v2.1.268 is released. The update adds gateway pricing synchronization with pricing set in gateway.yaml for matching client costs and telemetry. It introduces startup CIDR warnings when access\_control.allow\_cidrs is empty, the gatewayInternalNetworks setting, self-hosted runner session cleanup with --remove-session-state, configDirectory in auth status --json, and JSON support for plugin commands and list.

github · ashwin-ant · Sep 10, 20:30

**「改了什么」** This release changes the gateway to support pricing sync via gateway.yaml configuration, adds the --remove-session-state flag for self-hosted runners, and includes JSON output for auth status and plugin management.

**Tags**: `#runtime`, `#tools`, `#gateway`, `#plugins`, `#json`

---

<a id="item-harness-arch-2"></a>
### [Codex python-v0.154.0 发布](https://github.com/openai/codex/releases/tag/python-v0.154.0) ⭐️ 7.8/10

OpenAI codex Python v0.154.0 is released. It adds max and ultra reasoning-effort values. It adds ExternalMessage support for turns with tool authority. It includes include\_turns/turn\_service\_tier on resume/fork and protocol refreshes.

github · aibrahim-oai · Sep 10, 19:51

**「设计要点」** ExternalMessage supports starting turns or joining active turns with tool-level authority. The resume and fork operations now support include\_turns and turn\_service\_tier options.

**「改了什么」** Added max and ultra reasoning-effort values. Added ExternalMessage to synchronous and asynchronous run and turn calls. Added include\_turns on resume/fork, turn\_service\_tier, and source metadata. Refreshed generated protocol models and notifications.

**Tags**: `#runtime`, `#tools`, `#permissions`, `#planning`, `#memory`

---

<a id="item-harness-arch-3"></a>
### [google/adk-python v2.9.0 released](https://github.com/google/adk-python/releases/tag/v2.9.0) ⭐️ 7.8/10

Google ADK Python v2.9.0 is released. It introduces automatic model failover with FallbackModel, LiveKit runner for voice and telephony, YAML-based ADK 2.0 graph workflows, and MCP SDK 2.x support. Breaking changes include workflow node resumption behavior, GCS tool path restrictions, and in-memory session handling.

github · GWeale · Sep 10, 21:22

**「Design notes」** Design notes: FallbackModel enables automatic failover to backup models for resilience. YAML configuration and LiveKit runner support declarative workflows and voice/telephony integrations. In-memory sessions now raise SessionNotFoundError on mismatched appends.

**「What changed」** v2.9.0 adds FallbackModel for automatic model failover, LiveKit runner for voice and telephony, YAML support for ADK 2.0 graphs, and MCP SDK 2.x compatibility. Breaking changes: nodes now rerun on resume, GCS tools confined to local\_file\_root, in-memory sessions raise SessionNotFoundError.

**Tags**: `#runtime`, `#mcp`, `#tools`, `#workflow`

---

<a id="item-harness-arch-4"></a>
### [Cline desktop-v0.0.25 发布](https://github.com/cline/cline/releases/tag/desktop-v0.0.25) ⭐️ 6.8/10

Cline desktop v0.0.25 is released. Windows installer now stops the Cline Hub daemon first to avoid file write errors. ChatGPT model picker respects subscription limits and retired models are removed. Prompt handling is improved to recover lost prompts on send failures.

github · github-actions\[bot\] · Sep 10, 04:57

**「设计要点」** The Cline Hub daemon runs detached and outlives the main application. The installer stops the daemon before updating the binary to prevent conflicts.

**「改了什么」** Model picker now respects ChatGPT subscription limits by filtering models and removing retired ones. Windows installer daemon conflicts are fixed by stopping the sidecar process first, and prompt recovery on send failures is improved. Local CLI providers support session start without API keys. Model catalog is refreshed with new defaults for several providers.

**Tags**: `#runtime`, `#tools`

---

<a id="item-harness-arch-5"></a>
### [openai-agents-js v0.18.0 发布](https://github.com/openai/openai-agents-js/releases/tag/v0.18.0) ⭐️ 6.8/10

openai-agents-js v0.18.0 migrates Docker file APIs inside containers and adds optional file I/O protection to UnixLocalSandboxClient. Docker file APIs now run entirely within the container, requiring /bin/sh and GNU utils, with a 10MiB editor limit and path grant resumption. The fileIOProtection option defaults to &\#x27;auto&\#x27; for Python-based protection on file and editor operations.

github · seratch · Sep 10, 21:23

**「设计要点」** Docker file APIs execute inside the running container using default user or explicit runAs. UnixLocalSandboxClient adds fileIOProtection \(&\#x27;auto&\#x27;\|&\#x27;required&\#x27;\|&\#x27;off&\#x27;\) for file/editor ops without affecting shell commands.

**「改了什么」** Docker file APIs are now container-internal, breaking host file access compatibility. Added fileIOProtection option to UnixLocalSandboxClient and image generation tool action selection.

**Tags**: `#sandbox`, `#runtime`, `#permissions`, `#tools`

---

<a id="item-harness-arch-6"></a>
### [Agent Framework python-1.18.0 发布](https://github.com/microsoft/agent-framework/releases/tag/python-1.18.0) ⭐️ 6.8/10

Microsoft released Agent Framework Python 1.18.0. It adds shared vector-store abstractions, portable filters, and an in-memory vector store. The tool invocation loop now supports maximum duration bounds and stop-reason signals. Mixed workflow invocation keyword arguments are supported, and UI snapshot configuration was added to suppress terminal message snapshots.

github · moonbox3 · Sep 10, 09:23

**「设计要点」** The framework uses shared vector-store abstractions for memory handling, allowing portable filters and multiple backend implementations.

**「改了什么」** The release changes the vector store abstraction to be shared and portable. Tool loops gain duration bounds and support for mixed workflow keyword arguments. Breaking changes include dependency isolation for Lab and SecretString as a masked wrapper.

**Tags**: `#memory`, `#runtime`, `#tools`

---

<a id="item-harness-arch-7"></a>
### [E2B 2.49.1 发布](https://github.com/e2b-dev/E2B/releases/tag/e2b%402.49.1) ⭐️ 5.8/10

E2B SDK 2.49.1 is a patch release. It rejects invalid Sandbox.create lifecycle options and Sandbox.connect onResume values before requiring an API key, matching the Python SDK. It documents that onResume needs a control plane that knows the option, as older self-hosted or BYOC control planes drop the memory field. It adds up to three retries for control-plane HTTP requests using the server&\#x27;s delta-seconds Retry-After delay, configurable via the retries parameter.

github · github-actions\[bot\] · Sep 10, 17:37

**「改了什么」** E2B 2.49.1 rejects invalid Sandbox.create lifecycle options and Sandbox.connect onResume values before requiring an API key. It documents onResume behavior with older control planes and adds up to 3x Retry-After HTTP retries for control-plane requests.

**Tags**: `#sandbox`, `#memory`, `#runtime`, `#control-plane`, `#retries`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [Shopify Reverts to Native Mobile with AI Agents](https://simonwillison.net/2026/Sep/10/shopify-react-native/) ⭐️ 8.0/10

Shopify is reverting from React Native to separate Swift and Kotlin codebases for its native mobile apps. The decision follows six years of using React Native since 2020, when the goals were to stop building the same features twice, allow developers to work across the stack, and spend less time on feature parity. AI agents now handle implementation, translation, testing, and review work, making the cost of maintaining duplicated features no longer the deciding factor.

rss · Simon Willison · Sep 10, 21:11

**「Why it matters」** This change demonstrates how AI agents are shifting the economics of mobile development by bridging cross-platform duplication costs.

**「What to watch」** Watch: AI agents now handling enough of the implementation, translation, testing, and review work that maintaining duplicated features across platforms is no longer prohibitive.

**Tags**: `#coding-agent`, `#orchestration`, `#harness`, `#eval`

---

<a id="item-agent-engineer-2"></a>
### [SWE-2 Pushing the Pareto Frontier](https://cognition.ai/blog/swe-2) ⭐️ 7.8/10

Cognition released SWE-2, post-trained from Kimi K33 \(2.8T parameters\). It reaches 50.0% on FrontierCode 1.1 Main1, within one point of Fable 5.1 while being 64% cheaper. SWE-2 scaled RL to the multi-trillion-parameter regime using a new algorithm that trains all reasoning-effort levels in a single run. It is available in Devin Desktop, CLI, Web, and Fusion.

rss · Cognition Blog · Sep 10, 17:00

**「Why it matters」** The release advances cost-performance tradeoffs for coding agents by optimizing the full Pareto frontier in one RL run, with concrete benchmark improvements over prior models like SWE-1.7 at lower cost.

**「Takeaway」** A new single-run RL algorithm trains all reasoning-effort levels by applying linear cost penalties tuned to the base model&\#x27;s Pareto frontier.

**Tags**: `#coding-agent`, `#eval`

---

<a id="item-agent-engineer-3"></a>
### [OpenAI Agents API 发布](https://developers.openai.com/api/docs/guides/agents-api/overview) ⭐️ 7.0/10

OpenAI released the Agents API, a hosted service for building customizable AI agents that includes integrated tools and environment-agnostic state management. The API introduces a new orchestration abstraction with explicit details on state and tool persistence. This affects developers building agent harnesses by offering a platform that abstracts environment-specific complexities.

hackernews · aquir · Sep 10, 19:43 · [Discussion](https://news.ycombinator.com/item?id=49649213)

**「为什么重要」** The Agents API provides a standardized abstraction for agent state and tools that does not tie to specific runtimes or environments.

**「可关注」** 可关注：Self-hosting the sandbox option reduces vendor lock-in and eases transitions between providers.

**「评论」** Community discussion centers on the difficulty of defining agent abstractions and state persistence across environments. Opinions split between concerns over vendor lock-in and appreciation for self-hosting flexibility.

**Tags**: `#orchestration`, `#harness`, `#coding-agent`, `#agents-api`, `#memory`

---

## AI Daily

<a id="item-ai-daily-1"></a>
### [OpenAI Expands AI Access to Governments](https://openai.com/index/expanding-ai-access-us-government) ⭐️ 9.8/10

OpenAI is expanding AI access to federal, state, local, and tribal governments through a partnership with the GSA. Eligible governments will receive $0 license fees, 50% off usage, and enhanced cyber defense support.

rss · OpenAI Blog · Sep 10, 07:00

**「Why It Matters」** The program provides governments with $0 license fees, 50% off usage, and enhanced cyber defense support.

**「Engineer Takeaway」** Key Takeaway: Eligible governments receive $0 license fees, 50% off usage, and expanded cyber defense support.

**Tags**: `#openai`, `#policy`, `#government`, `#product`

---

<a id="item-ai-daily-2"></a>
### [ChatGPT for Financial Services](https://openai.com/index/introducing-chatgpt-financial-services) ⭐️ 7.8/10

OpenAI launches ChatGPT for Financial Services. The service combines built-in financial data with GPT-6 Astra. GPT-6 Astra supports research, modeling, and client-ready materials.

rss · OpenAI Blog · Sep 10, 07:00

**「Why It Matters」** This provides financial services with a specialized AI tool integrating financial data and advanced capabilities for research and modeling.

**「Pay Attention」** Attention: Built-in financial data and GPT-6 Astra are now available for research, modeling, and client-ready materials.

**Tags**: `#model`, `#lab`, `#industry`, `#product`

---

<a id="item-ai-daily-3"></a>
### [Codex and ChatGPT Search for New Antimicrobial Molecules](https://openai.com/index/using-codex-chatgpt-to-search-for-new-antimicrobials) ⭐️ 6.8/10

OpenAI blog post reports that César de la Fuente’s lab uses Codex and ChatGPT to search living and extinct genomes for antimicrobial candidates. The goal is to fight drug-resistant infections. This applies existing models to genomic data for new molecule discovery.

rss · OpenAI Blog · Sep 10, 16:00

**「Why It Matters」** This case shows Codex and ChatGPT being used in a real lab for scientific discovery of antimicrobials against resistant infections.

**「Takeaway」** Takeaway: Researchers apply Codex and ChatGPT to search living and extinct genomes for antimicrobial candidates.

**Tags**: `#model`, `#lab`, `#industry`, `#product`

---

<a id="item-ai-daily-4"></a>
### [DeepSeek V4.1 Flash Released](https://mp.weixin.qq.com/s?__biz=Mzk0OTYwNzc3NQ==&amp;mid=2247485817&amp;idx=1&amp;sn=627dd80114901f3fd8717e2c13feaf6a) ⭐️ 6.8/10

DeepSeek released V4.1 Flash, a native multimodal base model. It is described as stronger, faster, and more inclusive. The official announcement provides minimal details.

rss · DeepSeek · Sep 10, 05:44

**「Why It Matters」** The release of V4.1 Flash as a native multimodal model is relevant for AI developers.

**「Key Takeaway」** Key takeaway: V4.1 Flash is a native multimodal base model.

**Tags**: `#model`, `#DeepSeek`, `#multimodal`, `#product`

---

<a id="item-ai-daily-5"></a>
### [OpenAI Data Agent in ChatGPT Work](https://openai.com/index/put-data-to-work) ⭐️ 5.8/10

OpenAI has launched the Data agent in ChatGPT Work. Users can connect company data and use natural language to uncover insights and build interactive dashboards. The announcement provides limited technical details or comparisons.

rss · OpenAI Blog · Sep 10, 15:00

**「Why it matters」** This enables natural language interaction with company data, allowing users to uncover insights and build dashboards more easily.

**「Takeaway」** Connect company data, uncover insights, and build interactive dashboards with AI using natural language.

**Tags**: `#openai`, `#chatgpt`, `#product`, `#industry`

---

<a id="item-ai-daily-6"></a>
### [GitHub Copilot 应用 for Beginners 指南](https://github.blog/ai-and-ml/github-copilot/github-copilot-app-for-beginners-using-the-diff-terminal-and-browser/) ⭐️ 5.8/10

GitHub 发布了 Copilot 应用 for Beginners 指南。教用户在侧边查看 diff、运行终端命令和预览网页应用。检查代理生成的代码通常需要切换标签页。

rss · GitHub Blog · Sep 10, 21:31

**「为什么重要」** GitHub 发布了 Copilot 应用 for Beginners 指南。指南提供了使用 Copilot 应用时侧边查看 diff、运行终端命令和预览网页应用的方法。

**「可关注」** 可关注：并排查看 diff、运行终端命令和预览网页应用。

**Tags**: `#github`, `#copilot`, `#product`, `#app`

---

## AI Deals

<a id="item-ai-deals-1"></a>
### [Mathathon Challenge 40 Hours $2M+ AI Credits](https://mathathonchallenge.com/) ⭐️ 8.0/10

Mathathon Challenge offers 40 hours and $2M+ AI credits to participants who solve an open problem. The condition to claim these rewards is solving an open problem.

rss · HN Free API / Credits · Sep 10, 16:45

**「What to Watch」** Solve an open problem to claim the 40 hours and $2M+ AI credits.

**Tags**: `#credits`, `#free-tier`, `#promo`, `#challenge`

---

<a id="item-ai-deals-2"></a>
### [geoSurge.ai 免费品牌可见性](https://app.geosurge.ai/login) ⭐️ 6.0/10

jonsmostovojs shared on Hacker News about geoSurge.ai, a completely free brand monitoring and LLM sentiment analysis tool. It connects existing LLM subscriptions and uses spare tokens for analysis with no extra costs. Users get free sentiment analysis and beautiful dashboards after connecting subscriptions.

rss · HN Free API / Credits · Sep 10, 13:16

**「为什么重要」** This provides free brand visibility and sentiment analysis for users who make purchase decisions based on LLM outputs, helping reduce hallucinations without additional spending.

**「可关注」** Connect your existing LLM subscriptions and use spare tokens for free brand monitoring and sentiment analysis.

**Tags**: `#free-tier`, `#promo`, `#api`, `#sentiment-analysis`, `#brand-monitoring`

---

<a id="item-ai-deals-3"></a>
### [Modeinspect 99天免费AI积分上线](https://www.producthunt.com/products/modeinspect-1-0) ⭐️ 5.0/10

Modeinspect 提供99天免费AI积分，用于在代码库中设计产品UI。这是Product Hunt的推广活动。

rss · Product Hunt · Sep 10, 03:31

**「可关注」** 可关注：Modeinspect支持在代码库中设计产品UI。

**Tags**: `#promo`, `#credits`, `#free-tier`, `#limited-free`, `#producthunt`

---