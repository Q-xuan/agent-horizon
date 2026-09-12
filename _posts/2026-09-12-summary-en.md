---
layout: default
title: "Horizon Summary: 2026-09-12 (EN)"
date: 2026-09-12
lang: en
---

> From 189 items, 14 important content pieces were selected

---

**Agent Harness Architecture**
1. [Cloudflare Agents 0.23.0 Released](#item-harness-arch-1) ⭐️ 8.8/10
2. [Cloudflare Agents @cloudflare/think@0.18.0 发布](#item-harness-arch-2) ⭐️ 7.8/10
3. [Cloudflare agents @0.12.0 released](#item-harness-arch-3) ⭐️ 7.8/10
4. [@mastra/core@1.66.0 发布](#item-harness-arch-4) ⭐️ 7.8/10
5. [DSPy 3.4.0b1 Released](#item-harness-arch-5) ⭐️ 7.8/10
6. [Claude Code v2.1.269 Released](#item-harness-arch-6) ⭐️ 6.8/10
7. [Cline desktop v0.0.26 released](#item-harness-arch-7) ⭐️ 6.8/10
8. [GitHub Trending: letta-ai/letta-code](#item-harness-arch-8) ⭐️ 5.0/10

**AI Agent Engineer**
1. [Devin Desktop &amp; CLI 引入 Fusion](#item-agent-engineer-1) ⭐️ 7.8/10
2. [OpenRouter fallback inconsistencies](#item-agent-engineer-2) ⭐️ 7.0/10

**AI Daily**
1. [OpenAI Evolves Habitat for 1B ChatGPT Users](#item-ai-daily-1) ⭐️ 8.8/10
2. [Perplexity Adopts Astra for Communications and Monitoring](#item-ai-daily-2) ⭐️ 5.8/10
3. [Marketing Ops as Code: Automating GitHub Events](#item-ai-daily-3) ⭐️ 5.8/10

**AI Deals**
1. [Epic Games Free Games \(9.11-9.17\): LUFTRAUSERS, ASTRAL ASCENT &amp; Alone With You](#item-ai-deals-1) ⭐️ 6.0/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [Cloudflare Agents 0.23.0 Released](https://github.com/cloudflare/agents/releases/tag/agents%400.23.0) ⭐️ 8.8/10

Cloudflare Agents 0.23.0 is released. It extracts sub-agent \(facet\) routing and WebSocket machinery into the dynamic-agents lifecycle capability with a new public facade. A RoutedAgents capability is added to support the user hub with one Durable Object per chat topology. The Lifecycle now owns a durable job queue driven by an alarm event loop.

github · github-actions\[bot\] · Sep 11, 10:42

**「Design points」** Dynamic-agents is registered as a Lifecycle capability \(capabilityId: &quot;dynamic-agents&quot;\) handling facet routing, WebSocket forwarding, and virtual connections. RoutedAgents codifies the recommended many-chats pattern using a durable catalog of independent top-level Agents. The job queue is owned by Lifecycle with serializable callback jobs driven in timestamp order.

**「What changed」** Sub-agent machinery is extracted into the dynamic-agents module with this.dynamicAgents facade added. Lifecycle now owns a durable job queue instead of alarms. RoutedAgents capability is introduced for catalog-based routing of multiple top-level Agents.

**Tags**: `#subagents`, `#runtime`, `#dynamic-agents`, `#capabilities`

---

<a id="item-harness-arch-2"></a>
### [Cloudflare Agents @cloudflare/think@0.18.0 发布](https://github.com/cloudflare/agents/releases/tag/%40cloudflare/think%400.18.0) ⭐️ 7.8/10

Cloudflare Agents framework releases @cloudflare/think@0.18.0. It migrates Think conversation storage onto agents/sessions and prompt context onto agents/context with backward-compatible deprecations. Existing subclasses keep compiling and running via deprecated forwards to the new context API. Storage migrates on first wake and cannot be rolled back.

github · github-actions\[bot\] · Sep 11, 10:42

**「设计要点」** Conversation storage uses agents/sessions Durable Object tables. Prompt context is in agents/context. Lifecycle owns a durable job queue for alarms and scheduling. Media eviction is a context-window technique separate from storage.

**「改了什么」** Storage migrates on first wake and cannot be rolled back. hydrationByteBudget defaults to 32 MiB. Removed sessionAttachments, getRecentHistory, and compactAfter tokenCounter option. Alarm system changes: jobs queue replaces pull-based alarms. Scheduler API unchanged.

**Tags**: `#runtime`, `#memory`

---

<a id="item-harness-arch-3"></a>
### [Cloudflare agents @0.12.0 released](https://github.com/cloudflare/agents/releases/tag/%40cloudflare/ai-chat%400.12.0) ⭐️ 7.8/10

Cloudflare agents 0.12.0 minor release updates AIChatAgent message handling via sessions table with first-wake migration and rollback safety. Existing cf\_ai\_chat\_agent\_messages rows are imported once into a linear Sessions chain. Boot no longer loads the transcript synchronously in the constructor; messages are empty until onStart. Hydration is bounded by 32 MiB.

github · github-actions\[bot\] · Sep 11, 10:42

**「设计要点」** Messages are empty until onStart. Streams chunk log uses mutable rollover blocks. Recovery continuations run as chained Tasks.

**「改了什么」** Migrated AIChatAgent messages to agents/sessions on first wake. Rolled over stream chunks to mutable blocks with atomic cutover. Replatform resumable streams onto agents/streams. Recovery continuations as chained Tasks instead of schedule rows.

**Tags**: `#memory`, `#runtime`

---

<a id="item-harness-arch-4"></a>
### [@mastra/core@1.66.0 发布](https://github.com/mastra-ai/mastra/releases/tag/%40mastra/core%401.66.0) ⭐️ 7.8/10

Mastra core 1.66.0 adds deploy-scoped worker provisioning for Mastra Cloud, enabling dedicated orchestration and background workers via a versioned workers.json manifest and authenticated endpoints. It enhances trace querying with advanced predicates for spans, metadata, feedback, and scores across multiple databases. Observability signal deletion for feedback and scores is introduced, along with memory transform hooks and streaming reliability improvements.

github · PaulieScanlon · Sep 11, 09:37

**「改了什么」** Mastra core 1.66.0 adds deploy-scoped worker provisioning for Cloud, richer trace querying predicates across multiple DBs, and observability signal deletion. It also introduces memory transform hooks and first-chunk timeout for streaming models.

**Tags**: `#runtime`, `#deployment`, `#observability`, `#traces`, `#queries`

---

<a id="item-harness-arch-5"></a>
### [DSPy 3.4.0b1 Released](https://github.com/stanfordnlp/dspy/releases/tag/3.4.0b1) ⭐️ 7.8/10

DSPy 3.4.0b1 beta release introduces shared engine for LM execution, local interpreter, async execution, and related tool/eval improvements. It moves language-model execution to a shared engine interface, adds a local CPython interpreter for trusted code, and brings async execution to ReActV2. This is a prerelease, not the stable 3.4.0 release. APIs and behavior may change before stable. Install explicitly with \`pip install --upgrade &quot;dspy==3.4.0b1&quot;\`.

github · isaacbmiller · Sep 11, 22:24

**「Architecture Note」** DSPy&\#x27;s LM layer uses the lm15 request, response, and streaming types from dspy.lm15. The default engine=&quot;auto&quot; prefers native lm15 execution. Custom backends implement complete\(Request\) -&gt; Response. LocalInterpreter runs generated Python in a persistent local CPython subprocess.

**「What Changed」** The experimental 3.3 LM types are replaced with lm15 equivalents. Async ReActV2 now supports await calls. LocalInterpreter provides persistent CPython for trusted code. GEPA accepts custom code proposers and fixes evaluation alignment.

**Tags**: `#runtime`, `#sandbox`, `#tools`, `#eval`, `#planning`

---

<a id="item-harness-arch-6"></a>
### [Claude Code v2.1.269 Released](https://github.com/anthropics/claude-code/releases/tag/v2.1.269) ⭐️ 6.8/10

Claude Code v2.1.269 from Anthropic adds reproducible plugin evals via \`claude plugin eval\`, /output-style support to list and switch output styles, Bash tool change diffs, OTEL repository metrics tagging, and CLAUDE\_CODE\_WORKFLOW\_MAX\_CONCURRENT\_AGENTS \(1–256\) for Workflow tool concurrent agents.

It adds CLAUDE\_CODE\_GATEWAY\_MODEL\_DISCOVERY\_TIMEOUT\_MS and fixes prompt cache invalidation after cutoffs, terminal input regressions in kitty-protocol and others, permission rule scoping, and session resumption problems.

github · ashwin-ant · Sep 11, 19:17

**「What changed」** v2.1.269 adds reproducible plugin evals, /output-style switching, Bash edit diffs, and OTEL vcs tagging.

It also raises the Workflow tool&\#x27;s concurrent agent limit and resolves terminal, caching, and permission issues.

**Tags**: `#eval`, `#tools`, `#subagents`, `#runtime`

---

<a id="item-harness-arch-7"></a>
### [Cline desktop v0.0.26 released](https://github.com/cline/cline/releases/tag/desktop-v0.0.26) ⭐️ 6.8/10

Cline desktop v0.0.26 adds live GitHub PR display and CI inspection in the composer, with status refreshing every 30 seconds while visible. It merges the Tools, Skills, and Rules tabs into a single consistent list with search functionality and enable/disable toggles. Additional changes include fixes for session states, image handling, authentication, and more.

github · github-actions\[bot\] · Sep 11, 07:46

**「What changed」** Cline desktop v0.0.26 introduces GitHub PR integration in the composer and tab unification in the customize view. It also resolves issues with queued prompts, session restoration, image handling, sign-out persistence, and scheduled tasks.

**Tags**: `#runtime`, `#tools`

---

<a id="item-harness-arch-8"></a>
### [GitHub Trending: letta-ai/letta-code](https://github.com/letta-ai/letta-code) ⭐️ 5.0/10

Letta Code is a stateful agent harness for creating agents that are more like people than tools. Letta Code agents have memory, identity, and a sense of experience over time. They learn and evolve over long horizons through rewriting their own memory, skills, prompts, and even the harness itself \(through mods\). It can be used interactively, or to power applications.

rss · GitHub Trending Daily · Sep 12, 01:18

**Tags**: `#memory`, `#runtime`, `#tools`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [Devin Desktop &amp; CLI 引入 Fusion](https://cognition.ai/blog/local-fusion) ⭐️ 7.8/10

Cognition 在 Devin Desktop 和 CLI 中引入 Fusion harness。它采用 lead frontier model 负责规划和 review，sidekick cost-effective model 负责执行的架构。推荐 Fable 5.1 搭配 SWE-2。Fusion 在多个 coding benchmarks 上实现最高 39% 效率提升，同时成本降低 20% 至 46%。

rss · Cognition Blog · Sep 11, 17:00

**「为什么重要」** Fusion 已集成到 Devin Desktop 和 CLI，用户可直接使用。材料显示其在基准测试中成本节省，但其在真实任务中的长期性能影响尚未证实。

**「可关注」** 可关注：使用更强的 sidekick 模型可能降低整体系统成本，因为其 token 效率更高且减少 review 轮次。

**Tags**: `#harness`, `#coding-agent`, `#eval`, `#orchestration`

---

<a id="item-agent-engineer-2"></a>
### [OpenRouter fallback inconsistencies](https://simonwillison.net/2026/Sep/11/so-you-want-to-use-openrouter/) ⭐️ 7.0/10

OpenRouter automatically handles fallbacks and picks the most cost-effective option for each request. However, this can cause problems because different providers run different serving software with different optimizations and settings, meaning the same endpoint can serve model requests that behave differently. Some providers even lack vision capability for vision models, and the way the reasoning effort option is processed can differ as well. To ensure reliable usage, control which provider is routed to using the provider.only option.

rss · Simon Willison · Sep 11, 22:49

**「Why it matters」** Variable model behavior across providers can disrupt consistent LLM orchestration in agent toolchains. Explicit provider selection provides a way to mitigate these inconsistencies.

**「What to watch」** What to watch: Use the provider.only option to ensure consistent model behavior when using OpenRouter.

**Tags**: `#orchestration`, `#coding-agent`

---

## AI Daily

<a id="item-ai-daily-1"></a>
### [OpenAI Evolves Habitat for 1B ChatGPT Users](https://openai.com/index/scaling-storage-one-billion-users-part-one) ⭐️ 8.8/10

OpenAI evolved the Habitat Python library into a globally distributed storage platform. This platform serves 1 billion ChatGPT users and processes 22 million requests per second. The transformation supports the storage infrastructure needs of massive AI services at scale.

rss · OpenAI Blog · Sep 11, 10:00

**「Why It Matters」** Serving 1 billion users at 22M requests per second requires advanced distributed storage systems to maintain performance and reliability.

**「Engineer Takeaway」** Key takeaway: Habitat evolved from a Python library to a globally distributed storage platform serving 1 billion ChatGPT users at 22M requests per second.

**Tags**: `#lab`, `#industry`, `#product`

---

<a id="item-ai-daily-2"></a>
### [Perplexity Adopts Astra for Communications and Monitoring](https://openai.com/index/perplexity-improving-accuracy-with-astra) ⭐️ 5.8/10

Perplexity uses Astra to write communications, change software, and monitor production systems. It checks in much less frequently than with earlier models.

rss · OpenAI Blog · Sep 14, 00:00

**Tags**: `#openai`, `#perplexity`, `#astra`, `#product`, `#industry`

---

<a id="item-ai-daily-3"></a>
### [Marketing Ops as Code: Automating GitHub Events](https://github.blog/ai-and-ml/github-copilot/marketing-ops-as-code-automating-events-from-planning-to-follow-up-on-github/) ⭐️ 5.8/10

Tomoko Tanaka documents automating GitHub&\#x27;s APAC marketing events from planning to follow-up via code on GitHub. The process covers event planning, execution, and follow-up. By writing down workflows, she enabled automation using GitHub tools.

rss · GitHub Blog · Sep 11, 18:26

**「Why It Matters」** This case study shows how code can streamline internal marketing operations at GitHub.

**「Key Takeaway」** Key takeaway: If you can write down how you do your work, you can automate it.

**Tags**: `#product`, `#industry`, `#github`

---

## AI Deals

<a id="item-ai-deals-1"></a>
### [Epic Games Free Games \(9.11-9.17\): LUFTRAUSERS, ASTRAL ASCENT &amp; Alone With You](https://www.appinn.com/eggs-26911/) ⭐️ 6.0/10

Epic Games is offering three free games this week: LUFTRAUSERS and ASTRAL ASCENT for PC, and Alone With You for mobile. These games can be claimed on the Epic Games Launcher from September 11 to 17. The giveaway is available during this limited period.

rss · 小众软件 · Sep 11, 07:48

**「Note」** Note: Claim the games on the Epic Games Launcher before the deadline on September 17.

**Tags**: `#promo`, `#limited-free`, `#games`

---