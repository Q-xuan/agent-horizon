---
layout: default
title: "Horizon Summary: 2026-09-09 (EN)"
date: 2026-09-09
lang: en
---

> From 178 items, 13 important content pieces were selected

---

**Agent Harness Architecture**
1. [Claude Code v2.1.265 发布](#item-harness-arch-1) ⭐️ 7.8/10
2. [pydantic-ai v2.41.0 发布](#item-harness-arch-2) ⭐️ 7.8/10
3. [openai-agents-python v0.22.1 发布](#item-harness-arch-3) ⭐️ 7.8/10
4. [openai-agents-js v0.17.1 发布](#item-harness-arch-4) ⭐️ 7.8/10
5. [Goose v1.50.0 发布](#item-harness-arch-5) ⭐️ 6.8/10
6. [Gemini CLI v0.60.0-preview.0 Released](#item-harness-arch-6) ⭐️ 5.8/10
7. [gemini-cli v0.59.0 released](#item-harness-arch-7) ⭐️ 5.8/10

**AI Agent Engineer**
1. [Safety for Whom? Refusing the Right Subset of a Topic](#item-agent-engineer-1) ⭐️ 7.8/10

**AI Daily**
1. [OpenAI Shares AI Navier-Stokes Solution](#item-ai-daily-1) ⭐️ 7.8/10
2. [OpenAI $5M Grant for Teen AI Research](#item-ai-daily-2) ⭐️ 7.8/10
3. [OpenAI Blog: The Work Now Within Reach](#item-ai-daily-3) ⭐️ 6.8/10
4. [ChatGPT Images 2.5 Released](#item-ai-daily-4) ⭐️ 6.8/10
5. [GPT-5.6 Sol Runs Quantum Experiments](#item-ai-daily-5) ⭐️ 5.8/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [Claude Code v2.1.265 发布](https://github.com/anthropics/claude-code/releases/tag/v2.1.265) ⭐️ 7.8/10

Anthropic released Claude Code v2.1.265. The update adds support for --plugin-dir pointing to a folder of plugins, loading each child folder with a manifest dynamically, and picking up added or removed children while running. It introduces a 1 GB cap on tool results saved to disk, with previews in the conversation indicating when a saved file was truncated. Stability fixes address subagent resumption after tool list or system prompt prefix changes that broke prompt-cache reuse, along with other runtime and compatibility improvements.

github · ashwin-ant · Sep 8, 20:37

**「改了什么」** The key changes are dynamic plugin folder support via --plugin-dir and a 1GB limit on tool result disk storage with truncation previews. Fixes improve subagent and resumed teammate stability for prompt-cache reuse when tool lists or prompts change, plus various other bug fixes for sessions, plugins, and workflows.

**Tags**: `#runtime`, `#subagents`, `#prefix-cache`, `#tools`, `#sandbox`

---

<a id="item-harness-arch-2"></a>
### [pydantic-ai v2.41.0 发布](https://github.com/pydantic/pydantic-ai/releases/tag/v2.41.0) ⭐️ 7.8/10

pydantic-ai v2.41.0 adds a direct \`ImageGenerator\` API and an \`openai-codex\` provider for ChatGPT/Codex subscription authentication. \`ImageGeneration\` and \`XSearch\` deprecate \`fallback\_model\` in favor of \`fallback\_subagent\_model\`. Anthropic native web searches now appear in \`RequestUsage.details\` and are priced in \`cost\`. \`BedrockConverseModel\` wraps botocore transport errors in \`ModelAPIError\`, and Gemini thinking levels snap to the nearest supported level.

github · dsfaccini · Sep 8, 04:15

**「设计要点」** On \`ImageGeneration\` and \`XSearch\`, \`fallback\_model\` is deprecated for \`fallback\_subagent\_model\`. Image generation is also exposed as a direct \`ImageGenerator\` API.

**「改了什么」** Versus v2.40.0, \`ImageGeneration\` and \`XSearch\` deprecate \`fallback\_model\` for \`fallback\_subagent\_model\`, and image generation is callable via \`ImageGenerator\`. Also new: \`openai-codex\` auth, Anthropic web-search usage and cost, Bedrock \`ModelAPIError\` wrapping, and Gemini thinking-level snapping.

**Tags**: `#subagents`, `#tools`, `#runtime`

---

<a id="item-harness-arch-3"></a>
### [openai-agents-python v0.22.1 发布](https://github.com/openai/openai-agents-python/releases/tag/v0.22.1) ⭐️ 7.8/10

OpenAI released openai-agents-python v0.22.1. This version adds support for image results in web search tools, server-wide guardrails for MCP tools, customizable output guardrails, configurable Unix-local sandbox isolation, Docker container labels, and streamed transcription options. It also includes fixes for core usage and tool argument issues.

github · seratch · Sep 8, 09:18

**「改了什么」** Added image results support for web search tools, server-wide guardrails for MCP tools, customizable output guardrails, configurable Unix-local sandbox isolation, Docker container labels, and streamed transcription options. Multiple fixes were applied to core components, sandbox, sessions, and voice features.

**Tags**: `#mcp`, `#sandbox`, `#tools`, `#runtime`, `#guardrails`

---

<a id="item-harness-arch-4"></a>
### [openai-agents-js v0.17.1 发布](https://github.com/openai/openai-agents-js/releases/tag/v0.17.1) ⭐️ 7.8/10

openai-agents-js v0.17.1 is a JavaScript SDK for building AI agents with OpenAI. This release delivers server-wide MCP tool guardrails, Docker sandbox label support, enhanced web search tools, and runtime improvements for approval sessions and replay.

github · seratch · Sep 8, 10:04

**「改了什么」** This release introduces server-wide MCP tool guardrails and Docker sandbox container label support. It adds image results to web search tools and runtime improvements for approval session resumption and replay.

**Tags**: `#mcp`, `#sandbox`, `#runtime`, `#tools`, `#permissions`

---

<a id="item-harness-arch-5"></a>
### [Goose v1.50.0 发布](https://github.com/aaif-goose/goose/releases/tag/v1.50.0) ⭐️ 6.8/10

Goose v1.50.0 adds support for GPT-6 Astra models and tool calling for goose-agent. Subagent platform enforcement is introduced with permission management fixes. Kotlin callers can configure the Databricks AI Gateway path and the latest MCP version is preferred.

github · github-actions\[bot\] · Sep 8, 19:32

**「改了什么」** Goose v1.50.0 adds GPT-6 model support and tool calling for goose-agent. It enforces subagent platform guards and preserves permission revocations across managers.

**Tags**: `#subagents`, `#permissions`, `#tools`, `#runtime`

---

<a id="item-harness-arch-6"></a>
### [Gemini CLI v0.60.0-preview.0 Released](https://github.com/google-gemini/gemini-cli/releases/tag/v0.60.0-preview.0) ⭐️ 5.8/10

Google Gemini CLI v0.60.0-preview.0 is released as a minor preview. This update includes sandbox and MCP OAuth improvements such as web fetch routing fixes, RFC 9207 issuer enforcement in MCP OAuth, macOS Seatbelt sandbox isolation for temp and settings directories, extension loader path validation, NTFS 8.3 short name mitigation, and workspace boundary checks. It references changelogs from v0.58.0 and v0.59.0-preview.0.

github · gemini-cli-robot · Sep 8, 21:04

**「What Changed」** Relative to v0.59.0-preview.0, this release adds destination validation and routing improvements in web fetch utilities, RFC 9207 issuer identification enforcement in MCP OAuth, macOS Seatbelt sandbox isolation for temporary directories, hardened extension loader path resolution, NTFS 8.3 path mitigation, and enhanced workspace safety checks.

**Tags**: `#sandbox`, `#mcp`, `#runtime`, `#extensions`, `#tools`

---

<a id="item-harness-arch-7"></a>
### [gemini-cli v0.59.0 released](https://github.com/google-gemini/gemini-cli/releases/tag/v0.59.0) ⭐️ 5.8/10

gemini-cli v0.59.0 is a patch release of the Gemini CLI tool. It includes security fixes for MCP authentication and restricted-mode workspace trust. The changes prevent SSRF in MCP OAuth metadata discovery and authentication, and enforce fail-closed workspace trust with filtering of mcpServers in restricted mode.

github · gemini-cli-robot · Sep 8, 21:13

**「Design notes」** Security fixes target MCP OAuth SSRF prevention and workspace trust enforcement for mcpServers in restricted mode.

**「What changed」** This release fixes SSRF in MCP OAuth metadata discovery and authentication, and enforces fail-closed workspace trust filtering mcpServers in restricted mode compared to v0.58.0.

**Tags**: `#mcp`, `#permissions`, `#sandbox`, `#runtime`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [Safety for Whom? Refusing the Right Subset of a Topic](https://huggingface.co/blog/MultiverseComputingCAI/safety-for-whom) ⭐️ 7.8/10

The Hugging Face blog post argues that real LLM deployments require tailored safety refusals within the same topic for different settings like educational vs enterprise use. It introduces a paper studying this via boundary-aware self-distillation. The paper uses political persuasion as testbed, showing that standard self-generated safety tuning creates coverage gaps and over-refusal, which boundary-aware training with held-out pairs controls, reducing over-refusal from 32.94% to 4.16% while maintaining high harmful refusal rates.

rss · Hugging Face Blog · Sep 8, 14:23

**「Why it matters」** This matters for agent safety harnesses and evaluations because it shows that harmful-refusal rate alone can hide over-refusal on benign prompts, requiring measurement of both sides of the boundary for deployment-specific safety.

**「What to watch」** Data composition decides the trade-off between safety and over-refusal; evaluate both sides of the intended boundary.

**Tags**: `#harness`, `#eval`, `#permissions`, `#orchestration`, `#coding-agent`

---

## AI Daily

<a id="item-ai-daily-1"></a>
### [OpenAI Shares AI Navier-Stokes Solution](https://openai.com/index/navier-stokes-solution) ⭐️ 7.8/10

OpenAI shares an AI-generated solution to the Navier–Stokes Millennium Prize Problem. The solution includes a writeup and a formal proof in Lean.

rss · OpenAI Blog · Sep 8, 10:00

**「Why It Matters」** This shows AI capability on unsolved math problems.

**「Engineer Takeaway」** AI can generate formal proofs in Lean for complex math.

**「Community Discussion」** No community comments available.

**Tags**: `#model`, `#lab`, `#open-source`, `#math`

---

<a id="item-ai-daily-2"></a>
### [OpenAI $5M Grant for Teen AI Research](https://openai.com/index/teen-development-research-grants) ⭐️ 7.8/10

OpenAI is offering $5 million in grants to fund independent research examining how generative AI impacts teen development, well-being, and safety. The program targets studies on effects of generative AI on adolescents. Applications are open now for independent researchers.

rss · OpenAI Blog · Sep 8, 09:00

**「Engineer Takeaway」** Focus on: independent research into generative AI effects on teen development, well-being, and safety.

**Tags**: `#openai`, `#policy`, `#ai-safety`, `#teen-development`, `#grant`

---

<a id="item-ai-daily-3"></a>
### [OpenAI Blog: The Work Now Within Reach](https://openai.com/index/the-work-now-within-reach) ⭐️ 6.8/10

OpenAI&\#x27;s blog post explores how more capable and affordable AI can expand the work people and businesses can accomplish and make growth more economical. The post provides a general statement on AI capabilities expanding work and growth without specific new facts, model details, benchmarks, or comparisons to prior work.

rss · OpenAI Blog · Sep 8, 13:00

**「Why It Matters」** This post highlights the potential for advancing AI to increase productivity and make business growth more economical.

**「Takeaway」** More capable and affordable AI can expand the work people and businesses can accomplish and make growth more economical.

**「Community Discussion」** No community comments available.

**Tags**: `#openai`, `#industry`, `#product`

---

<a id="item-ai-daily-4"></a>
### [ChatGPT Images 2.5 Released](https://openai.com/index/introducing-chatgpt-images-2-5) ⭐️ 6.8/10

OpenAI introduces ChatGPT Images 2.5. The feature turns user ideas, sketches, and reference photos into more personalized and polished images. These images better reflect the original ideas.

rss · OpenAI Blog · Sep 8, 11:30

**「Pay attention to」** Pay attention to: generating more personalized images from ideas, sketches, and reference photos.

**Tags**: `#openai`, `#chatgpt`, `#product`, `#model`

---

<a id="item-ai-daily-5"></a>
### [GPT-5.6 Sol Runs Quantum Experiments](https://openai.com/index/codex-quantum-computing-experiments) ⭐️ 5.8/10

MIT researcher employs GPT-5.6 Sol and Codex for quantum computing experiments. The system autonomously runs the experiments. It then analyzes the results and calibrates the qubits.

rss · OpenAI Blog · Sep 8, 17:00

**「Takeaway」** Takeaway: GPT-5.6 Sol with Codex enables autonomous quantum computing experiments, result analysis, and qubit calibration.

**Tags**: `#model`, `#lab`, `#industry`, `#product`

---