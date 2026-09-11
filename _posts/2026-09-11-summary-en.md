---
layout: default
title: "Horizon Summary: 2026-09-11 (EN)"
date: 2026-09-11
lang: en
---

> From 178 items, 18 important content pieces were selected

---

**Agent Harness Architecture**
1. [Codex python-v0.154.0 发布](#item-harness-arch-1) ⭐️ 7.8/10
2. [ADK Python v2.9.0 发布](#item-harness-arch-2) ⭐️ 7.8/10
3. [openai-agents-js v0.18.0 released](#item-harness-arch-3) ⭐️ 7.8/10
4. [Claude Code v2.1.268 发布](#item-harness-arch-4) ⭐️ 6.8/10
5. [Agent Framework python-1.18.0 发布](#item-harness-arch-5) ⭐️ 6.8/10
6. [E2B 2.49.1 lifecycle validation](#item-harness-arch-6) ⭐️ 6.8/10
7. [Cline desktop-v0.0.25 released](#item-harness-arch-7) ⭐️ 5.8/10

**AI Agent Engineer**
1. [OpenAI Agents API 发布](#item-agent-engineer-1) ⭐️ 8.0/10
2. [Datasette 1.0a39 security updates](#item-agent-engineer-2) ⭐️ 7.8/10
3. [SWE-2: Pushing the Pareto Frontier](#item-agent-engineer-3) ⭐️ 7.8/10
4. [Anthropic AI Misuse Report September 2026](#item-agent-engineer-4) ⭐️ 7.0/10
5. [Shopify 回归原生移动](#item-agent-engineer-5) ⭐️ 7.0/10

**AI Daily**
1. [Researcher Uses Codex and ChatGPT to Search for New Antimicrobial Molecules](#item-ai-daily-1) ⭐️ 6.8/10
2. [OpenAI Data agent ChatGPT Work](#item-ai-daily-2) ⭐️ 6.8/10
3. [Introducing ChatGPT for Financial Services](#item-ai-daily-3) ⭐️ 6.8/10
4. [OpenAI Expands AI Access and Cyber Defense for US Governments](#item-ai-daily-4) ⭐️ 6.8/10
5. [DeepSeek V4.1 Flash Released](#item-ai-daily-5) ⭐️ 6.8/10

**AI Deals**
1. [Modeinspect 99 Days Free AI Credits](#item-ai-deals-1) ⭐️ 7.0/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [Codex python-v0.154.0 发布](https://github.com/openai/codex/releases/tag/python-v0.154.0) ⭐️ 7.8/10

OpenAI Codex Python SDK v0.154.0 is released. New max and ultra reasoning-effort values added. ExternalMessage support in run/turn calls and history selection on resume/fork. Protocol models refreshed with backward compatibility.

github · aibrahim-oai · Sep 10, 19:51

**「改了什么」** This release adds max and ultra reasoning-effort values, ExternalMessage to run and turn calls, and new resume/fork options including include\_turns and turn\_service\_tier. Protocol models and notifications have been refreshed.

**Tags**: `#runtime`, `#tools`, `#memory`, `#planning`

---

<a id="item-harness-arch-2"></a>
### [ADK Python v2.9.0 发布](https://github.com/google/adk-python/releases/tag/v2.9.0) ⭐️ 7.8/10

Google ADK Python v2.9.0 is released. This release introduces automatic model failover for runtime resilience, LiveKit runner for voice and telephony agents, YAML-based graph workflows for ADK 2.0, and MCP SDK 2.x compatibility.

github · GWeale · Sep 10, 21:22

**「改了什么」** This release adds automatic model failover, LiveKit voice support, YAML-based graph workflows, and MCP 2.x compatibility compared to v2.8.0. Breaking changes include rerunning a failed node on resume instead of replaying it as complete, confining GCS tool local file paths to a configured root, and raising SessionNotFoundError when appending to an unknown session.

**Tags**: `#runtime`, `#mcp`, `#planning`

---

<a id="item-harness-arch-3"></a>
### [openai-agents-js v0.18.0 released](https://github.com/openai/openai-agents-js/releases/tag/v0.18.0) ⭐️ 7.8/10

openai-agents-js v0.18.0 migrates Docker file APIs to run inside containers and adds optional UnixLocalSandboxClient file I/O protection.

The Docker file APIs now run entirely inside a running container, requiring compatible images with /bin/sh and GNU utilities. Editor updates accept source files up to 10 MiB; use execCommand for larger edits. Newly added path grants require resume or recreation before file APIs can use them.

The UnixLocalSandboxClient adds fileIOProtection option with modes &\#x27;auto&\#x27; \| &\#x27;required&\#x27; \| &\#x27;off&\#x27;, defaulting to &\#x27;auto&\#x27;. imageGenerationTool\(\) accepts action &\#x27;generate&\#x27; \| &\#x27;edit&\#x27; \| &\#x27;auto&\#x27;.

github · seratch · Sep 10, 21:23

**「Architecture Note」** Docker file APIs now run entirely inside a running container. This changes compatibility for applications that relied on host-side file access and uses the container&\#x27;s default user or explicit runAs.

**「What Changed」** The Docker file API has been migrated to run inside containers, requiring compatible images and handling file permissions via runAs or default user. The UnixLocalSandboxClient now supports optional fileIOProtection with modes auto, required, or off, and imageGenerationTool\(\) accepts action options.

**Tags**: `#runtime`, `#sandbox`, `#tools`, `#permissions`

---

<a id="item-harness-arch-4"></a>
### [Claude Code v2.1.268 发布](https://github.com/anthropics/claude-code/releases/tag/v2.1.268) ⭐️ 6.8/10

Claude Code v2.1.268 is released. The update integrates gateway pricing with \`pricing:\` in \`gateway.yaml\` so clients receive matching rates for \`/cost\` and telemetry. It adds \`claude self-hosted-runner --remove-session-state\` to remove session state and \`gatewayInternalNetworks\` for allowlisting. Additional features include enhanced JSON output for plugins and auth status, along with numerous bug fixes for runtime, tools, and permissions.

github · ashwin-ant · Sep 10, 20:30

**「改了什么」** Relative to the previous version, this release adds gateway pricing alignment, self-hosted runner session state removal, enhanced plugin JSON output, auth config exposure, and internal network allowlisting. It also includes fixes for issues like HTTP 400 errors on third-party endpoints, WebFetch hanging, permission rules on symlinks, and various other runtime and tool bugs.

**Tags**: `#gateway`, `#runtime`, `#tools`, `#permissions`, `#auth`

---

<a id="item-harness-arch-5"></a>
### [Agent Framework python-1.18.0 发布](https://github.com/microsoft/agent-framework/releases/tag/python-1.18.0) ⭐️ 6.8/10

Microsoft released agent-framework Python 1.18.0. The update adds shared vector store support with abstractions, portable filters, and in-memory vector store implementations. It also improves the runtime tool invocation loop with a maximum duration bound and stop-reason signal. Additional changes include support for mixed workflow invocation and various backend integrations.

github · moonbox3 · Sep 10, 09:23

**「设计要点」** Shared vector store abstractions enable portable filters across multiple backends including Azure AI Search, Redis, Qdrant, and PostgreSQL. The tool invocation loop adds runtime bounds with stop-reason signals for improved control.

**「改了什么」** This release adds shared vector store support and tool loop improvements compared to the previous version. It includes breaking changes for dependency isolation and credential handling.

**Tags**: `#memory`, `#runtime`, `#tools`

---

<a id="item-harness-arch-6"></a>
### [E2B 2.49.1 lifecycle validation](https://github.com/e2b-dev/E2B/releases/tag/e2b%402.49.1) ⭐️ 6.8/10

E2B SDK \`e2b@2.49.1\` is a patch on sandbox lifecycle options and control-plane HTTP. Invalid \`Sandbox.create\` lifecycle options and \`Sandbox.connect\` \`onResume\` values are rejected before an API key is required, matching the Python SDK. Control-plane HTTP requests retry up to three times after \`429\` using the server&\#x27;s delta-seconds \`Retry-After\`. Envd requests, including filesystem operations, and volume-content requests are not retried.

github · github-actions\[bot\] · Sep 10, 17:37

**「设计要点」** \`onResume\` / \`on\_resume\` needs a control plane that knows the option: an older self-hosted or BYOC control plane drops the \`memory\` field, restores memory, and reports success instead of rejecting. Retries are configured or disabled with \`retries\`, and stop when waiting would exhaust the request timeout.

**「改了什么」** \`Sandbox.create\` lifecycle options and \`Sandbox.connect\` \`onResume\` are now rejected before the API-key check. Control-plane calls gained up to three timeout-bounded \`429\` retries via \`Retry-After\`; Envd, filesystem, and volume-content requests stay unretried. The older-control-plane silent \`memory\` restore is documented, not newly rejected.

**Tags**: `#sandbox`, `#memory`, `#runtime`

---

<a id="item-harness-arch-7"></a>
### [Cline desktop-v0.0.25 released](https://github.com/cline/cline/releases/tag/desktop-v0.0.25) ⭐️ 5.8/10

Cline desktop v0.0.25 is released. It fixes the ChatGPT model picker to only list models your actual subscription supports, avoiding context cap mismatches with the backend. Windows installer updates now stop the sidecar daemon first to prevent file write errors. Prompts are restored after failed sends before the turn starts, and local CLI providers can start sessions without an API key.

github · github-actions\[bot\] · Sep 10, 04:57

**「What&\#x27;s Changed」** Windows installer now stops the sidecar daemon to avoid &quot;Error opening file for writing&quot; errors during updates. Prompts lost on pre-turn send failures are recovered, and local CLI providers like Claude Code and Codex CLI can start sessions without an API key.

**Tags**: `#runtime`, `#tools`, `#permissions`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [OpenAI Agents API 发布](https://developers.openai.com/api/docs/guides/agents-api/overview) ⭐️ 8.0/10

OpenAI 发布了 Agents API，支持托管、集成工具的代理，并跨环境持久化状态。根据官方文档概述，Hacker News 讨论了代理抽象、harnesses 和托管计算服务。这影响了代理编排和工具集成开发者。

hackernews · aquir · Sep 10, 19:43 · [Discussion](https://news.ycombinator.com/item?id=49649213)

**「为什么重要」** OpenAI Agents API 的推出为代理提供了托管服务，这简化了构建复杂代理系统的过程。虽然影响尚未完全显现，但它可能减少自定义 harness 的工作量。

**「可关注」** 可关注：OpenAI 允许自托管沙箱，这提供了灵活性，避免供应商锁定。

**「评论」** 社区讨论中，用户强调代理抽象仍需探索，harnesses 仍需环境特定状态持久化。托管代理服务让用户能根据需要选择工具，并有人分享了自托管 VM 的成功经验。

**Tags**: `#harness`, `#orchestration`, `#agents`, `#API`, `#managed-services`

---

<a id="item-agent-engineer-2"></a>
### [Datasette 1.0a39 security updates](https://github.com/simonw/datasette/releases/tag/1.0a39) ⭐️ 7.8/10

Simon Willison released Datasette 1.0a39 alpha. It backports security fixes from 0.65.4. Permission checks now account for SQLite case-insensitive names. Full-text search index viewing requires table permissions. SQLite statistics tables are denied by default.

github · simonw · Sep 11, 00:05

**「Why it matters」** The permission modifications address access control vulnerabilities. They impact secure data toolchains using Datasette.

**「What to watch」** Watch for permission checks that now take SQLite&\#x27;s case-insensitive names into account.

**Tags**: `#permissions`, `#eval`, `#harness`, `#toolchain`, `#security`

---

<a id="item-agent-engineer-3"></a>
### [SWE-2: Pushing the Pareto Frontier](https://cognition.ai/blog/swe-2) ⭐️ 7.8/10

Cognition introduces SWE-2, its most advanced coding model. It reaches 50.0% on FrontierCode 1.1 Main, within one point of Fable 5.1 at 64% lower cost. SWE-2 scales RL to the multi-trillion-parameter regime for the first time, training all reasoning-effort levels in a single run. It is post-trained from Kimi K33 and is available in Devin Desktop, CLI, Web, and Fusion.

rss · Cognition Blog · Sep 10, 17:00

**「Why It Matters」** SWE-2 advances coding agent performance and cost tradeoffs. Its release provides a new baseline for agentic workflows, though real-world impacts on Devin usage remain untested.

**「Takeaway」** Takeaway: SWE-2 trains all effort levels in one RL run using linear cost penalties tuned to the base model&\#x27;s Pareto frontier.

**Tags**: `#coding-agent`, `#eval`, `#RL`, `#orchestration`

---

<a id="item-agent-engineer-4"></a>
### [Anthropic AI Misuse Report September 2026](https://www.anthropic.com/threat-intelligence-report-september-2026) ⭐️ 7.0/10

Anthropic released a September 2026 report on detecting and countering AI misuse. The report details proxying incidents where Moonshot AI silently forwarded customer requests to Claude and DeepSeek did the same without disclosure. It also covers biological weapons concerns, including the potential for millions of deaths. The findings offer insights for AI agent safety evaluations and orchestration.

hackernews · garo-pro · Sep 10, 17:23 · [Discussion](https://news.ycombinator.com/item?id=49647300)

**「Why it matters」** The report provides technical details on proxying risks and bioweapon threats that affect AI agent safety evaluations and model orchestration.

**「Engineer takeaway」** Attention: Proxying incidents by Moonshot AI and DeepSeek require verification of model usage in agent harnesses and orchestration.

**「Community discussion」** Community members highlighted a double standard in the report regarding biological weapons versus conventional weapons misuse. One commenter noted the report&\#x27;s restrictions on discussing topics like Emily Dickinson poems.

**Tags**: `#eval`, `#harness`, `#orchestration`

---

<a id="item-agent-engineer-5"></a>
### [Shopify 回归原生移动](https://simonwillison.net/2026/Sep/10/shopify-react-native/) ⭐️ 7.0/10

Shopify 决定从 React Native 切换回独立的 Swift 和 Kotlin 代码库，用于原生移动应用。自 2020 年起使用 React Native，旨在避免重复构建相同功能、让开发者跨栈工作、减少追赶特性平价的时间。现在，由于 AI 代理能够处理实现、翻译、测试和审查工作，维护双平台原生代码的成本不再是决定性因素。相关开源库 react-native-skia 和 flash-list 将迁移到新家园，restyle 将于 2026 年底归档。

rss · Simon Willison · Sep 10, 21:11

**「为什么重要」** AI 代理的成熟使得从 React Native 切换回原生不再成本高昂，这在 2020 年是决定性因素。已发生的是切换决策，尚未证实的是对行业移动开发范式的深远影响。

**「可关注」** 可关注：AI 代理能够处理实现、翻译、测试和审查工作。

**Tags**: `#coding-agent`, `#orchestration`, `#eval`, `#harness`

---

## AI Daily

<a id="item-ai-daily-1"></a>
### [Researcher Uses Codex and ChatGPT to Search for New Antimicrobial Molecules](https://openai.com/index/using-codex-chatgpt-to-search-for-new-antimicrobials) ⭐️ 6.8/10

César de la Fuente’s lab uses Codex and ChatGPT to search living and extinct genomes for new antimicrobial molecules.
The researchers target candidates to fight drug-resistant infections.
This applies the models to genomic data from living organisms and extinct species.

rss · OpenAI Blog · Sep 10, 16:00

**「What to watch」** What to watch: The lab uses Codex and ChatGPT to search living and extinct genomes for antimicrobial candidates to fight drug-resistant infections.

**Tags**: `#model`, `#lab`, `#industry`, `#product`

---

<a id="item-ai-daily-2"></a>
### [OpenAI Data agent ChatGPT Work](https://openai.com/index/put-data-to-work) ⭐️ 6.8/10

OpenAI has introduced the Data agent in ChatGPT Work. This feature lets users connect company data, uncover insights, and build interactive dashboards using natural language.

rss · OpenAI Blog · Sep 10, 15:00

**「可关注」** 可关注：Connect company data, uncover insights, and build interactive dashboards with AI using natural language.

**Tags**: `#lab`, `#product`, `#industry`

---

<a id="item-ai-daily-3"></a>
### [Introducing ChatGPT for Financial Services](https://openai.com/index/introducing-chatgpt-financial-services) ⭐️ 6.8/10

OpenAI introduces ChatGPT for Financial Services. It combines built-in financial data and GPT-6 Astra for research, modeling, and client-ready materials.

rss · OpenAI Blog · Sep 10, 07:00

**「Key Takeaway」** ChatGPT for Financial Services combines built-in financial data and GPT-6 Astra for research, modeling, and client-ready materials.

**Tags**: `#model`, `#lab`, `#industry`, `#product`

---

<a id="item-ai-daily-4"></a>
### [OpenAI Expands AI Access and Cyber Defense for US Governments](https://openai.com/index/expanding-ai-access-us-government) ⭐️ 6.8/10

OpenAI partners with GSA to offer eligible federal, state, local, and tribal governments $0 license fees, 50% off usage, and expanded cyber defense support. This initiative targets US government entities to expand access to OpenAI&\#x27;s AI models. The offer applies to qualifying public sector organizations.

rss · OpenAI Blog · Sep 10, 07:00

**「Key Takeaway」** Key takeaway: Eligible governments receive $0 license fees and 50% discounts on OpenAI usage.

**Tags**: `#openai`, `#policy`, `#government`, `#product`, `#industry`

---

<a id="item-ai-daily-5"></a>
### [DeepSeek V4.1 Flash Released](https://mp.weixin.qq.com/s?__biz=Mzk0OTYwNzc3NQ==&amp;mid=2247485817&amp;idx=1&amp;sn=627dd80114901f3fd8717e2c13feaf6a) ⭐️ 6.8/10

DeepSeek releases V4.1 Flash, a new native multimodal foundational model. It is described as stronger, faster, and more inclusive. Limited verifiable details are provided.

rss · DeepSeek · Sep 10, 05:44

**「Why It Matters」** This is an official announcement from DeepSeek lab about a new foundational model release.

**「Key Takeaway」** Key takeaway: Native multimodal, new foundational model.

**Tags**: `#model`, `#lab`, `#product`

---

## AI Deals

<a id="item-ai-deals-1"></a>
### [Modeinspect 99 Days Free AI Credits](https://www.producthunt.com/products/modeinspect-1-0) ⭐️ 7.0/10

Modeinspect offers 99 days of free AI credits for designing product UI in your codebase. This promotion is from a Product Hunt post. The credits are tied to using the tool for UI design in your codebase.

rss · Product Hunt · Sep 10, 03:31

**Tags**: `#credits`, `#promo`, `#free-tier`, `#api`

---