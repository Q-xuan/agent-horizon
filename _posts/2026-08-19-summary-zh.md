---
layout: default
title: "Horizon Summary: 2026-08-19 (ZH)"
date: 2026-08-19
lang: zh
---

> 从 92 条内容中筛选出 4 条重要资讯。

---

**Harness 架构**
1. [agent-framework dotnet-1.18.0 发布](#item-harness-arch-1) ⭐️ 6.0/10

**Agent 工程师日报**
1. [Palomar Lean 验证数学仓库](#item-agent-engineer-1) ⭐️ 7.0/10
2. [ALTK-Evolve 内存剂量校准实验](#item-agent-engineer-2) ⭐️ 7.0/10
3. [Qwen3.8-27B 2x3090 vLLM DFlash2 218 tok/s](#item-agent-engineer-3) ⭐️ 7.0/10

---

## Harness 架构

<a id="item-harness-arch-1"></a>
### [agent-framework dotnet-1.18.0 发布](https://github.com/microsoft/agent-framework/releases/tag/dotnet-1.18.0) ⭐️ 6.0/10

Microsoft agent-framework .NET SDK 1.18.0 版本发布。此版本新增了并发工具执行支持、Foundry 会话处理以及 Cosmos 聊天历史检索功能。

github · SergeyMenshykh · 8月18日 14:30

**「改了什么」** 此版本相比上一版主要增加了 .NET 代理并发工具调用的 opt-in 支持，以及 Foundry 托管会话和用户身份透传功能，以及 Cosmos 聊天历史检索 API。

**标签**: `#runtime`, `#tools`, `#memory`

---

## Agent 工程师日报

<a id="item-agent-engineer-1"></a>
### [Palomar Lean 验证数学仓库](https://terrytao.wordpress.com/2026/08/18/palomar-a-registry-of-lean-verified-mathematics/) ⭐️ 7.0/10

Terry Tao 宣布推出 Palomar，这是一个 Lean 验证数学的注册表。它由 GitHub 仓库的快照组成，具体到特定提交，包含遵循当前最佳实践的 Lean 代码。Palomar 类似于预印本服务器，为形式化数学提供集中管理。这一举措直接相关于评估基准、代理 harness 和记忆系统，用于形式化数学的检索和验证。

hackernews · matt\_d · 8月19日 02:41 · [社区讨论](https://news.ycombinator.com/item?id=49355968)

**「为什么重要」** Palomar 的推出为 Lean 形式化数学提供了一个集中注册表，这在评估基准和代理 harness 中可能有用。

**「可关注」** 可关注：Palomar 要求提交者提供详细的仓库快照和提交信息，这对 harness 系统的内存管理和版本控制有直接影响。

**「评论」** 社区成员对 Palomar 表示认可，认为它类似于预印本服务器，但也指出验证证明的过程可能存在递归问题。一些用户分享了提交经验，并将它与 Isabelle 和 Metamath 社区进行了比较。

**标签**: `#eval`, `#harness`, `#coding-agent`, `#memory`, `#orchestration`

---

<a id="item-agent-engineer-2"></a>
### [ALTK-Evolve 内存剂量校准实验](https://huggingface.co/blog/ibm-research/altk-evolve-hmm) ⭐️ 7.0/10

ALTK-Evolve 让代理从自身轨迹中提取可重用指导原则，并在推理时注入，无需更新模型权重或人工标注。在 AppWorld 基准（585 多步任务）上评估 8 个模型后发现，代理内存剂量需根据模型能力校准。强模型（如 DeepSeek-V3.2）使用完整指南集提升任务完成率 +9.5pp，弱模型（如 gpt-oss-120b）使用精选检索提升 +16.1pp（仅 +5% tokens），饱和模型（如 GLM-5）无增益。

rss · Hugging Face Blog · 8月18日 18:09

**「为什么重要」** 这一发现揭示了代理内存并非通用功能，而是需针对模型能力校准的剂量。实验在 8 个模型上验证了三种模式，并提供了可验证的性能提升数据，影响代理系统在不同能力模型上的内存注入策略。

**「可关注」** 可关注：弱模型的最佳内存策略是精选检索，在 gpt-oss-120b 上实现 +16.1pp 任务完成率提升，仅增加 5% tokens。

**标签**: `#memory`, `#eval`, `#orchestration`, `#agent`

---

<a id="item-agent-engineer-3"></a>
### [Qwen3.8-27B 2x3090 vLLM DFlash2 218 tok/s](https://www.reddit.com/r/LocalLLaMA/comments/1vsccit/qwen3827b_on_2x_3090_vllm_dflash2_218_toks_single/) ⭐️ 7.0/10

Qwen3.8-27B 在 2× RTX 3090 上使用 vLLM + DFlash2 实现了单请求解码 218 tok/s。使用 Club-3090 基准套件测量，prefill 速度分别为 1342 tok/s（10k 上下文）和 628 tok/s（90k 上下文），spec-decode 使用 7 个草稿 token，接受长度 3.35，接受率 47.8%。峰值显存占用 22.3 GB/卡，上下文上限 131k，堆栈为 vLLM v0.26.1rc1 + AutoRound INT4（group 128） + DFlash2。

reddit · r/LocalLLaMA · /u/xjx546 · 8月19日 04:39

**「为什么重要」** 此基准报告展示了消费级双 3090 硬件上通过 vLLM 和 DFlash2 实现高吞吐量的可行性，对本地大模型推理和 coding agent 部署有参考价值。

**「可关注」** 可关注：DFlash2 搭配 vLLM 在双 RTX 3090 上可实现 Qwen3.8-27B 218 tok/s 的单请求解码。

**标签**: `#coding-agent`, `#orchestration`, `#harness`, `#eval`

---