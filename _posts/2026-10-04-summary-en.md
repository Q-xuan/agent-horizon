---
layout: default
title: "Horizon Summary: 2026-10-04 (EN)"
date: 2026-10-04
lang: en
---

> From 125 items, 3 important content pieces were selected

---

**Agent Harness Architecture**
1. [pydantic/pydantic-ai released v2.54.0](#item-harness-arch-1) ⭐️ 7.8/10

**AI Agent Engineer**
1. [The Agent Said It Was Done. The Database Disagreed.](#item-agent-engineer-1) ⭐️ 8.8/10
2. [Kyojin 让 128 GB 迷你主机跑 300B MoE](#item-agent-engineer-2) ⭐️ 7.5/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [pydantic/pydantic-ai released v2.54.0](https://github.com/pydantic/pydantic-ai/releases/tag/v2.54.0) ⭐️ 7.8/10

pydantic-ai v2.54.0 发布，包含持久化执行、wrap 钩子生命周期、Temporal 错误处理及 JSON Schema 兼容性等具体修复与行为变更。

github · dsfaccini · Oct 3, 03:21

**Tags**: `#runtime`, `#tools`, `#eval`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [The Agent Said It Was Done. The Database Disagreed.](https://huggingface.co/blog/microsoft/thinkingbox) ⭐️ 8.8/10

Microsoft and Hugging Face introduce ThinkingBox, a paper-backed evaluation framework that runs agents in isolated MCP tool sessions and grades the terminal backend state and side effects they leave behind.

rss · Hugging Face Blog · Oct 3, 22:56

**Tags**: `#eval`, `#mcp`, `#harness`, `#observability`

---

<a id="item-agent-engineer-2"></a>
### [Kyojin 让 128 GB 迷你主机跑 300B MoE](https://www.reddit.com/r/LocalLLaMA/comments/1wwocik/two_300b_moe_models_each_on_one_128_gb_mini_pc/) ⭐️ 7.5/10

Yamz-Labs 发布 Kyojin 引擎，基于 ExLlamaV3 与 ROCm，面向 AMD Strix Halo \(gfx1151\)，在单台 128 GB Ryzen AI Max+ 395 上打包运行两个 300B 级 MoE。GLM-5.3-Flash 占 99.7 GB，3.5K prefill 580 tok/s、64K 546 tok/s，MTP 解码 26–30 tok/s；MiMo-V2.6-Flash-MOPD 占 105 GB，4K prefill 约 650 tok/s，推测解码下 code 44、chat 35、prose 32 tok/s。以官方 FP8 为基线，GLM KLD 0.151、Top-1 89.3%，MiMo KLD 0.0713、Top-1 92.0%；GLM 包混合 turboderp 公开 2.05/3.05 bpw EXL3 张量，同 129 行对比 KLD 0.190 优于其 2.05 bpw 包 0.275，但体积 100 GB 对 85 GB 且解码慢约 10%。任务分数、128K 上下文与非 gfx1151 GPU 未测，转换管线不公开。

reddit · r/LocalLLaMA · /u/Yaniss916 · Oct 3, 14:16

**「为什么重要」** 这是把 300B 级 MoE 塞进单台 128 GB 消费级迷你主机并公开 prefill/decode 与量化指标的一手工程报告。对本地推理与 harness 工具链，它给出 gfx1151/ROCm 路径上可复现的吞吐和质量基线；但是否外推到其他 GPU 或 128K 长上下文尚未证实。

**「可关注」** 可关注：Kyojin 用 EXL3 混合量化加 MTP/推测解码，在 99.7–105 GB 占用下跑通 300B MoE；对比 turboderp 2.05 bpw 包，质量提升伴随体积增大与解码变慢，本地部署需按显存和时延取舍。

**Tags**: `#toolchain`, `#local-inference`, `#quantization`, `#rocm`, `#moe`

---