---
layout: default
title: "Horizon Summary: 2026-09-21 (EN)"
date: 2026-09-21
lang: en
---

> From 165 items, 10 important content pieces were selected

---

**Agent Harness Architecture**
1. [Cloudflare audit skill](#item-harness-arch-1) ⭐️ 7.5/10
2. [typesafe 0.0.1a3 发布](#item-harness-arch-2) ⭐️ 6.8/10
3. [Mem0 持久记忆层](#item-harness-arch-3) ⭐️ 5.5/10
4. [Claude 知识工作插件](#item-harness-arch-4) ⭐️ 5.0/10

**AI Agent Engineer**
1. [Code2Skill 合成 Agent 技能](#item-agent-engineer-1) ⭐️ 6.5/10
2. [MintAct 统一视觉 Agent](#item-agent-engineer-2) ⭐️ 6.2/10
3. [llm-keys-ui 0.1 配置密钥](#item-agent-engineer-3) ⭐️ 6.0/10
4. [RecreationWorld Eval](#item-agent-engineer-4) ⭐️ 6.0/10
5. [GraphSkillEvo 优化 Agent 技能](#item-agent-engineer-5) ⭐️ 5.5/10
6. [Qwen 3.8 27B 单卡 21 天](#item-agent-engineer-6) ⭐️ 5.5/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [Cloudflare audit skill](https://github.com/cloudflare/security-audit-skill) ⭐️ 7.5/10

Cloudflare open-sourced \`security-audit-skill\`, a coding-agent skill for multi-phase security audits. It coordinates isolated agents across reconnaissance, coverage-led hunting, candidate validation, structured output, independent record verification, and target-neutral reporting. The source describes it as the skill that seeded Cloudflare&\#x27;s vulnerability discovery harness.

rss · GitHub Trending Daily · Sep 21, 02:29

**「设计要点」** The harness separates audit phases across isolated agents and adds independent verification for both candidate findings and recorded results. It produces machine-readable findings and uses coverage-led search to guide the hunting phase.

**Tags**: `#runtime`, `#subagents`, `#tools`, `#eval`

---

<a id="item-harness-arch-2"></a>
### [typesafe 0.0.1a3 发布](https://github.com/langchain-ai/langchain/releases/tag/langchain-typesafe%3D%3D0.0.1a3) ⭐️ 6.8/10

LangChain released the experimental \`langchain-typesafe==0.0.1a3\` package. This alpha includes \`TypeSafeClassifier\`, experimental \`AutoModeMiddleware\`, and \`ModelRouterMiddleware\`; classifier questions are now scoped to each invocation. The changelog also records a trace usage metadata fix, but provides no architecture diagram, documented constraints, or breaking-change notes.

github · github-actions\[bot\] · Sep 20, 18:54

**「设计要点」** The package places classification and model selection in middleware, with \`AutoModeMiddleware\` and \`ModelRouterMiddleware\` representing experimental routing paths. Classifier questions are invocation-scoped, while the release notes do not specify the runtime contract, permission model, or evaluation behavior.

**「改了什么」** This release packages the initial \`TypeSafeClassifier\`, experimental auto-mode and model-router middleware, invocation-scoped classifier questions, and a trace usage metadata fix under version \`0.0.1a3\`.

**Tags**: `#runtime`, `#planning`, `#tools`

---

<a id="item-harness-arch-3"></a>
### [Mem0 持久记忆层](https://github.com/mem0ai/mem0) ⭐️ 5.5/10

Mem0 is presented as drop-in persistent memory infrastructure for AI agents and applications. Its page highlights a “New Memory Algorithm \(April 2026\)”: LoCoMo rises from 71.4 to 92.5, and LongMemEval from 67.8 to 94.4, with 7.0K and 6.8K tokens and p50 latency of 0.88s and 1.09s respectively. BEAM is reported at 64.1 for 1M and 48.6 for 10M, using 6.7K–6.9K tokens and 1.00–1.05s latency. The page says all benchmarks used the same production-representative model stack.

rss · GitHub Trending Daily · Sep 21, 02:29

**「设计要点」** The source describes Mem0 as a memory layer that persists agent context and can be integrated as drop-in infrastructure. It does not provide enough detail to identify its storage, retrieval, permission, or runtime boundaries.

**Tags**: `#memory`, `#eval`, `#runtime`

---

<a id="item-harness-arch-4"></a>
### [Claude 知识工作插件](https://github.com/anthropics/knowledge-work-plugins) ⭐️ 5.0/10

anthropics/knowledge-work-plugins is an open-source plugin collection for Claude Cowork, with compatibility for Claude Code. It turns Claude into role-, team-, or company-specific specialists by defining preferred work practices, tool and data access, critical workflows, and slash commands. The available description does not establish runtime, permission, sandbox, or state-management designs, so its impact on harness architecture remains unclear.

rss · GitHub Trending Daily · Sep 21, 02:29

**「设计要点」** The repository presents a plugin layer above Claude Cowork and Claude Code that packages role-specific instructions, workflow handling, tool and data inputs, and slash-command configuration. The supplied material does not describe the underlying runtime, isolation model, authorization flow, or persistent state.

**Tags**: `#tools`, `#planning`, `#runtime`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [Code2Skill 合成 Agent 技能](https://huggingface.co/papers/2609.05571) ⭐️ 6.5/10

Code2Skill proposes a fully automated pipeline that converts selected code units into implementation-anchored records covering atomic operations, composite workflows, and recurring patterns. It verifies each record through source-body-blind reconstruction and source-aware comparison. The paper was listed by Hugging Face Daily Papers on 2026-09-21; the supplied abstract is truncated after an application count of 19,769, and reports no concrete benchmark results, reproducibility artifacts, or comparison data.

rss · Hugging Face Daily Papers · Sep 21, 00:00

**「为什么重要」** The approach could provide a code-grounded input for coding-agent skill libraries and evaluation design because it does not require prior agent-environment interactions and retains executable evidence. Its practical advantage remains unconfirmed because the supplied material includes no benchmark or comparison results.

**「可关注」** 可关注：The central tension is between executable grounding and verified transfer; Code2Skill addresses grounding with source code and verification with source-body-blind reconstruction, but the supplied evidence does not show how well the synthesized skills transfer.

**Tags**: `#coding-agent`, `#harness`, `#eval`, `#memory`

---

<a id="item-agent-engineer-2"></a>
### [MintAct 统一视觉 Agent](https://huggingface.co/papers/2609.22083) ⭐️ 6.2/10

Published on 2026-09-21, MintAct presents 2B, 4B, and 8B vision-language models for UI grounding, multi-step navigation, and visual tool use across mobile, desktop, and web environments. The paper reports that the unified models match per-domain specialists across these capabilities. Its infrastructure runs hundreds of concurrent instances on heterogeneous backends for trajectory collection and online RL, while an asynchronous framework controls cross-domain training distribution; the supplied abstract is truncated and provides no benchmark values, reproducibility details, or code link.

rss · Hugging Face Daily Papers · Sep 21, 00:00

**「为什么重要」** MintAct treats heterogeneous environment orchestration and online RL as first-class parts of a unified visual-agent system, which is relevant to agent harness and evaluation infrastructure. The practical effect beyond the paper&\#x27;s reported results remains unverified because detailed benchmarks and implementation materials are unavailable here.

**「可关注」** 可关注：whether explicit control of cross-domain training distribution and asynchronous execution can maintain stable data collection when environments differ in latency, reliability, and interaction protocol.

**Tags**: `#visual-agent`, `#orchestration`, `#eval`, `#harness`, `#coding-agent`

---

<a id="item-agent-engineer-3"></a>
### [llm-keys-ui 0.1 配置密钥](https://simonwillison.net/2026/Sep/20/llm-keys-ui/) ⭐️ 6.0/10

On September 20, 2026, Simon Willison released llm-keys-ui 0.1 for a narrow Codex Remote workflow. Running \`uvx --with llm-keys-ui llm keys-ui --all\` starts a web interface reachable through local-network or Tailscale device IPs, where users can save additional LLM API keys. Later shell commands can retrieve named keys such as \`anthropic\`; the release includes no performance data, evaluation results, or broader architecture changes.

rss · Simon Willison · Sep 20, 19:22

**「为什么重要」** The workflow keeps key entry out of the ChatGPT app and agent session, matching the author&\#x27;s stated motivation. Its impact is limited to this specific key-configuration path, and the source does not provide a security audit or evidence of broader effects.

**「可关注」** 可关注：The key-handling boundary is explicit: Codex starts the local or Tailscale web server, while later shell commands retrieve keys by name.

**Tags**: `#coding-agent`, `#permissions`, `#harness`

---

<a id="item-agent-engineer-4"></a>
### [RecreationWorld Eval](https://huggingface.co/papers/2609.22000) ⭐️ 6.0/10

Published on 2026-09-21, the RecreationWorld paper proposes a five-platform benchmark for hybrid computer-use agents that alternate between GUI exploration, coding, execution, and visual verification. Agents must recreate a running reference without a prescribed workflow, using reproducible environments on Ubuntu, macOS, Windows, Android, and the Web, plus a unified harness with native GUI and coding tools. The supplied excerpt says the reference serves as an oracle for hidden behavioral checks, but provides no experimental results, baseline comparisons, implementation details, or open-source status; the excerpt is also truncated.

rss · Hugging Face Daily Papers · Sep 21, 00:00

**「为什么重要」** The paper targets a gap in current computer-use evaluation: real digital work combines interface interaction and software development rather than treating them as separate stages. Its practical value for agent evaluation and harness design remains unverified because the supplied material contains no results or baseline comparison.

**Tags**: `#eval`, `#harness`, `#coding-agent`, `#orchestration`, `#computer-use`

---

<a id="item-agent-engineer-5"></a>
### [GraphSkillEvo 优化 Agent 技能](https://huggingface.co/papers/2609.21749) ⭐️ 5.5/10

Hugging Face Daily Papers listed GraphSkillEvo on 2026-09-21. The paper proposes representing skills as graph-structured natural-language artifacts and applying evolutionary optimization to improve LLM-agent execution. The supplied excerpt identifies weak workflow guidance, redundancy, and an unconstrained search space as problems with unstructured skills, but provides no full method, code, reproducible experiments, or performance comparison.

rss · Hugging Face Daily Papers · Sep 21, 00:00

**「为什么重要」** The work targets skill representation and optimization, both relevant to agent orchestration and harness design. Its engineering benefit remains unverified because the available material does not establish how the graph representation performs against unstructured skills.

**「可关注」** 可关注：Graph structure may act as an explicit constraint for agent-skill search, but the supplied material does not show whether it improves coding-agent outcomes.

**Tags**: `#harness`, `#orchestration`, `#eval`, `#coding-agent`

---

<a id="item-agent-engineer-6"></a>
### [Qwen 3.8 27B 单卡 21 天](https://www.reddit.com/r/LocalLLaMA/comments/1wloora/the_bear_can_dance_qwen_38_27b_on_one_3090_for_3/) ⭐️ 5.5/10

On September 20, 2026, a Reddit author reported running a local agent loop for about 21 days with Qwen 3.8 27B Q4 on one RTX 3090, using Q8 KV and a 200k context. The task was to build a CUDA inference engine for that GPU, with roughly 12 human interventions; the run produced working kernels, benchmarks, notes, and a long Git history, but did not beat llama.cpp. Prefill reached about 250 tokens per second versus roughly 700 on the same card, while 699 compactions consumed about 83 hours, or 17% of the calendar time; the report has no independent validation or complete benchmark.

reddit · r/LocalLLaMA · /u/skeole · Sep 20, 18:26

**「为什么重要」** The report shows that a quantized 27B model maintained a real engineering goal for weeks on consumer hardware, with most stops attributed to protocol escalation rather than aimless wandering. It also exposes the cost of long-running local orchestration: 180 subagents, about 230 million input and output tokens, and GPU contention between vLLM and the engine under test.

**「可关注」** 可关注：The repeated failure came from unclear ownership of the script controlling vLLM, allowing a worker to shut down the orchestrator&\#x27;s own model host; the fixed handoff protocol helped define when to stop vLLM, run a benchmark, restart it, poll health, and write state.

**Tags**: `#harness`, `#orchestration`, `#coding-agent`, `#memory`

---