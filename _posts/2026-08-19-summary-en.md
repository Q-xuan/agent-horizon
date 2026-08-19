---
layout: default
title: "Horizon Summary: 2026-08-19 (EN)"
date: 2026-08-19
lang: en
---

> From 92 items, 4 important content pieces were selected

---

**Agent Harness Architecture**
1. [agent-framework dotnet-1.18.0 released](#item-harness-arch-1) ⭐️ 6.0/10

**AI Agent Engineer**
1. [Palomar: A registry of Lean verified mathematics](#item-agent-engineer-1) ⭐️ 7.0/10
2. [你的代理实际上需要多少内存？](#item-agent-engineer-2) ⭐️ 7.0/10
3. [Qwen3.8-27B 218 tok/s on 2x 3090 with vLLM + DFlash2](#item-agent-engineer-3) ⭐️ 7.0/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [agent-framework dotnet-1.18.0 released](https://github.com/microsoft/agent-framework/releases/tag/dotnet-1.18.0) ⭐️ 6.0/10

Microsoft agent-framework .NET SDK 1.18.0 is released. It adds concurrent tool execution support, Foundry session handling, and Cosmos chat history retrieval. The release provides opt-in concurrent tool invocation, hosted session and user identity pass-through, and Cosmos chat history API.

github · SergeyMenshykh · Aug 18, 14:30

**「What changed」** The .NET SDK 1.18.0 introduces opt-in concurrent tool invocation, hosted session/user identity pass-through for Foundry, and a Cosmos chat history retrieval API compared to the prior Python 1.14.0 version.

**Tags**: `#runtime`, `#tools`, `#memory`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [Palomar: A registry of Lean verified mathematics](https://terrytao.wordpress.com/2026/08/18/palomar-a-registry-of-lean-verified-mathematics/) ⭐️ 7.0/10

Terry Tao announces Palomar, a registry of Lean-verified mathematics as curated GitHub repo snapshots. These snapshots represent specific commits of repositories containing Lean code that adheres to current best practices for formalizations. The announcement includes submission details and discussion on Hacker News. This is directly relevant to AI agent harnesses, evaluation benchmarks, and memory for formal math retrieval and verification.

hackernews · matt\_d · Aug 19, 02:41 · [Discussion](https://news.ycombinator.com/item?id=49355968)

**「Why It Matters」** Palomar provides a centralized way to share and access Lean formalizations, which could influence how AI systems handle verified mathematics.

**「Takeaway」** Observable: The registry relies on GitHub snapshots of Lean repositories following best practices, creating a potential tension between centralization and dependency on external hosting.

**「Community Discussion」** Community members view Palomar as a preprint server analogue for Lean proofs and note the submission process is thorough but achievable even for non-experts. Some criticize the GitHub dependency and raise questions about recursively verifying the proofs.

**Tags**: `#eval`, `#harness`, `#coding-agent`, `#memory`, `#orchestration`

---

<a id="item-agent-engineer-2"></a>
### [你的代理实际上需要多少内存？](https://huggingface.co/blog/ibm-research/altk-evolve-hmm) ⭐️ 7.0/10

IBM Research&\#x27;s ALTK-Evolve lets agents distill lessons from past trajectories into reusable guidelines injected at inference time, with no weight updates or human annotation. Evaluation on AppWorld \(585 multi-step tasks\) across eight models from 30B dense to frontier proprietary systems showed model-specific optimal memory doses: strong models with headroom gain from the full guideline set \(DeepSeek-V3.2 +9.5pp TGC\), weaker models benefit from curated retrieval \(gpt-oss-120b +16.1pp TGC at +5% tokens\), and saturated models like GLM-5 show no gain. Gains appear on both TGC and stricter SGC metrics.

rss · Hugging Face Blog · Aug 18, 18:09

**「为什么重要」** This provides a portable, low-cost way to improve agent performance on complex multi-step tasks without retraining models or adding human effort.

**「可关注」** The right memory dose depends on model capability tier, with curated retrieval offering the best accuracy-cost tradeoff for models that benefit from selective guideline injection.

**Tags**: `#memory`, `#eval`, `#orchestration`, `#agent`

---

<a id="item-agent-engineer-3"></a>
### [Qwen3.8-27B 218 tok/s on 2x 3090 with vLLM + DFlash2](https://www.reddit.com/r/LocalLLaMA/comments/1vsccit/qwen3827b_on_2x_3090_vllm_dflash2_218_toks_single/) ⭐️ 7.0/10

Qwen3.8-27B achieved 218 tok/s decode throughput on 2x RTX 3090 using vLLM 0.26.1rc1 with DFlash2 speculative decoding. Prefill speeds reached 1342 tok/s at 10k context and 628 tok/s at 90k context. Spec-decode used 7 draft tokens with 3.35 acceptance length and 47.8% acceptance rate. Peak VRAM was 22.3 GB per card with a 131k context ceiling.

reddit · r/LocalLLaMA · /u/xjx546 · Aug 19, 04:39

**「Why it matters」** The benchmark provides a data point for running Qwen3.8-27B in coding agent orchestration and harness evaluations on dual consumer GPUs, though real-world impact depends on specific setups.

**「What to watch」** Watch for: Custom vLLM patches and DFlash2 speculative decoding enable 218 tok/s decode for Qwen3.8-27B on 2x RTX 3090 with 47.8% acceptance rate.

**Tags**: `#coding-agent`, `#orchestration`, `#harness`, `#eval`

---