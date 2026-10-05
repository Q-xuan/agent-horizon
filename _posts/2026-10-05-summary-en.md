---
layout: default
title: "Horizon Summary: 2026-10-05 (EN)"
date: 2026-10-05
lang: en
---

> From 136 items, 2 important content pieces were selected

---

**Agent Harness Architecture**
1. [FastMCP v3.4.8 Patches SSE, Header, and Auth Security](#item-harness-arch-1) ⭐️ 6.8/10

**AI Agent Engineer**
1. [Apex-2：3.87B MoE 从零训练](#item-agent-engineer-1) ⭐️ 5.5/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [FastMCP v3.4.8 Patches SSE, Header, and Auth Security](https://github.com/PrefectHQ/fastmcp/releases/tag/v3.4.8) ⭐️ 6.8/10

FastMCP v3.4.8 is a security-focused patch for the MCP server framework. It applies Host/Origin protections to SSE transport, strips Cookie from forwarded HTTP headers, and enforces the server auth provider on component manager routes. The release also bounds CIMD cache growth and fixes schema inlining, tool lookup, and Windows argument passing.

github · jlowin · Oct 4, 16:55

**「Design Points」** The patch hardens transport and auth boundaries. SSE now runs the same Host/Origin checks as other transports, forwarded headers drop cookies to prevent credential leakage, and component manager routes respect the configured auth provider. Tool lookups apply transforms, enabled state, and auth consistently across hashed and injected paths.

**「What Changed」** SSE gains Host/Origin protection, forwarded HTTP headers exclude Cookie, and component manager routes use the server auth provider. The release also bounds CIMD cache growth, fixes hashed and injected tool lookups to respect transforms and auth, and corrects Windows .cmd argument passing and OpenAPI header handling.

**Tags**: `#mcp`, `#permissions`, `#runtime`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [Apex-2：3.87B MoE 从零训练](https://www.reddit.com/r/LocalLLaMA/comments/1wxiy8y/i_trained_a_387b_moe_145b_active_from_scratch_on/) ⭐️ 5.5/10

2026-10-04，/u/Prestigious-Taste-63 开源 Apex-2，一个从零训练的 3.87B MoE，每 token 激活 1.45B 参数；32 层全 MoE，d\_model 2048，GQA 16Q/4KV，16 专家 top-4，上下文 4096，Qwen3 tokenizer（151k）。预训练 86.5B tokens（GH200 ×1 → ×2，DiLoCo），SFT 约 2.5B tokens，HumanEval+ 41.5，MBPP+ 48.9，MMLU 28.6。作者称基座以约 0.087T tokens 在 HumanEval+ 上追平 18T tokens 的 Qwen2.5-1.5B，但知识与数学仍落后；DPO 导致答案变长且代码/数学/IFEval 下降，已弃用。模型英语为主、知识薄弱、LiveCodeBench 中高难度接近零分、仅 4k 上下文，权重已公开，可通过 transformers / vLLM 经 Qwen3MoeForCausalLM 加载。

reddit · r/LocalLLaMA · /u/Prestigious-Taste-63 · Oct 4, 15:50

**「为什么重要」** 小团队用单卡到双卡 GH200 完成 3.87B MoE 从零训练，验证了 86.5B tokens 规模下 MoE 架构与 DiLoCo 分布式训练的可行性。HumanEval+ 与 18T tokens 密集模型的对比，为超小数据预算下的代码能力提供了参考基线。

**「可关注」** 可关注：86.5B tokens 预训练下，全 MoE 架构的 HumanEval+ 追平 18T tokens 的 1.5B 密集模型；但同规模 DPO 出现答案变长与代码/数学/IFEval 下降。

**Tags**: `#eval`, `#coding-agent`, `#moe`

---