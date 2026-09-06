---
layout: default
title: "Horizon Summary: 2026-09-06 (EN)"
date: 2026-09-06
lang: en
---

> From 127 items, 3 important content pieces were selected

---

**Agent Harness Architecture**
1. [gemini-cli v0.60.0-nightly.20260905.g85aca163f released](#item-harness-arch-1) ⭐️ 5.8/10
2. [SGLang v0.5.19 Released](#item-harness-arch-2) ⭐️ 5.8/10

**AI Agent Engineer**
1. [Claude 3.5 Sonnet 形式化费马最后定理](#item-agent-engineer-1) ⭐️ 9.0/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [gemini-cli v0.60.0-nightly.20260905.g85aca163f released](https://github.com/google-gemini/gemini-cli/releases/tag/v0.60.0-nightly.20260905.g85aca163f) ⭐️ 5.8/10

gemini-cli v0.60.0-nightly.20260905.g85aca163f released with fixes for environment consent, workspace boundary checks, and config permission enforcement.

github · gemini-cli-robot · Sep 5, 01:26

**「What Changed」** Fixed prompt for consent on environment changes and sanitized runtime-altering environment variables. Enhanced workspace path boundary checks and symlink resolution in command safety and file discovery. Enforced strict permission and ownership checks on system-wide configuration paths.

**Tags**: `#permissions`, `#sandbox`, `#runtime`, `#tools`, `#config`

---

<a id="item-harness-arch-2"></a>
### [SGLang v0.5.19 Released](https://github.com/sgl-project/sglang/releases/tag/v0.5.19) ⭐️ 5.8/10

SGLang v0.5.19 adds support for new autoregressive models including Qwen3.8 \(2.4T-A95B\), Qwen3.8-27B, dots3.note, Ling-3.0-flash, Ling-3.0-tiny, Spark2.5, MiniCPM-SALA, and Granite 4.2, plus some diffusion models. It introduces beam search, DeepEP v2 for MoE, layer norm sequence parallelism, W4A8 MoE on Hopper, DCP on Blackwell MLA, and optimizations for speculative decoding and AMD hardware. The release includes 786 PRs from 214 contributors and dependency updates such as FlashInfer to 0.6.18.

github · Qiaolin-Yu · Sep 5, 02:27

**「Design Points」** The unified radix tree is now the default cache for every model. Layer norm sequence parallelism normalizes only local tensor shares in prefill to reduce overhead in high TP degrees.

**「What Changed」** This release adds support for multiple new models and features like beam search and DeepEP v2. It also enables DCP on the default Blackwell MLA backend and faster speculative kernels for KDA models.

**Tags**: `#runtime`, `#models`, `#release`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [Claude 3.5 Sonnet 形式化费马最后定理](https://www.anthropic.com/research/formalizing-fermats-last-theorem) ⭐️ 9.0/10

Anthropic 展示了 Claude 3.5 Sonnet 如何使用 Lean 形式化费马最后定理。研究博客和开源代码已发布。这项工作展示了 AI 在形式验证和数学证明代理方面的进步。影响对象是开发数学推理 AI 代理的工程师。

rss · Lobsters · Sep 5, 12:54

**「为什么重要」** 这一形式化工作突显了 Claude 3.5 Sonnet 在复杂数学任务中的能力。目前尚未证实其对实际 AI 代理构建的影响。

**「可关注」** 可关注：Claude 3.5 Sonnet 在 Lean 中形式化费马最后定理的实现细节。

**Tags**: `#coding-agent`, `#eval`, `#harness`, `#orchestration`

---