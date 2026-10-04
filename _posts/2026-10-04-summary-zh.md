---
layout: default
title: "Horizon Summary: 2026-10-04 (ZH)"
date: 2026-10-04
lang: zh
---

> 从 125 条内容中筛选出 3 条重要资讯。

---

**Harness 架构**
1. [pydantic/pydantic-ai released v2.54.0](#item-harness-arch-1) ⭐️ 7.8/10

**Agent 工程师日报**
1. [The Agent Said It Was Done. The Database Disagreed.](#item-agent-engineer-1) ⭐️ 8.8/10
2. [Kyojin 让 300B MoE 模型跑上 128 GB 迷你电脑](#item-agent-engineer-2) ⭐️ 7.5/10

---

## Harness 架构

<a id="item-harness-arch-1"></a>
### [pydantic/pydantic-ai released v2.54.0](https://github.com/pydantic/pydantic-ai/releases/tag/v2.54.0) ⭐️ 7.8/10

pydantic-ai v2.54.0 发布，包含持久化执行、wrap 钩子生命周期、Temporal 错误处理及 JSON Schema 兼容性等具体修复与行为变更。

github · dsfaccini · 10月3日 03:21

**标签**: `#runtime`, `#tools`, `#eval`

---

## Agent 工程师日报

<a id="item-agent-engineer-1"></a>
### [The Agent Said It Was Done. The Database Disagreed.](https://huggingface.co/blog/microsoft/thinkingbox) ⭐️ 8.8/10

Microsoft and Hugging Face introduce ThinkingBox, a paper-backed evaluation framework that runs agents in isolated MCP tool sessions and grades the terminal backend state and side effects they leave behind.

rss · Hugging Face Blog · 10月3日 22:56

**标签**: `#eval`, `#mcp`, `#harness`, `#observability`

---

<a id="item-agent-engineer-2"></a>
### [Kyojin 让 300B MoE 模型跑上 128 GB 迷你电脑](https://www.reddit.com/r/LocalLLaMA/comments/1wwocik/two_300b_moe_models_each_on_one_128_gb_mini_pc/) ⭐️ 7.5/10

Yamz-Labs 发布 Kyojin 推理引擎，基于 ExLlamaV3 与 ROCm，面向 AMD Strix Halo \(gfx1151\)，首次将两个 300B 级 MoE 模型各自压入单台 128 GB 迷你电脑（Ryzen AI Max+ 395）。GLM-5.3-Flash 权重 99.7 GB，3.5K prefill 580 tok/s，64K 时 546 tok/s，MTP 解码 26–30 tok/s；MiMo-V2.6-Flash-MOPD 权重 105 GB，4K prefill 约 650 tok/s，推测解码最高 44 tok/s。以官方 FP8 为基线，GLM KLD 0.151、Top-1 一致率 89.3%，MiMo KLD 0.0713、一致率 92.0%；GLM pack 混合 turboderp 的 2.05 与 3.05 bpw EXL3 tensors 并自研层混合与调优，同 129 行测试下 KLD 0.190，优于 turboderp 2.05 bpw 的 0.275，但体积 100 GB 对 85 GB，解码慢约 10%。首次发布，未测 128K 上下文任务得分、gfx1151 以外 GPU 及 Uncensored 变体，转换管线私有。

reddit · r/LocalLLaMA · /u/Yaniss916 · 10月3日 14:16

**「为什么重要」** 300B 级 MoE 模型现在可在单台 128 GB 迷你电脑本地运行，Kyojin 引擎与 EXL3 权重公开。任务得分、长上下文及非 gfx1151 硬件表现仍待验证。

**「可关注」** 可关注：同 129 行测试下，GLM pack 100 GB KLD 0.190，turboderp 2.05 bpw 85 GB KLD 0.275，后者解码快约 10%，体积、质量与速度构成直接权衡。

**标签**: `#toolchain`, `#local-inference`, `#quantization`, `#rocm`, `#moe`

---