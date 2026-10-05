---
layout: default
title: "Horizon Summary: 2026-10-05 (EN)"
date: 2026-10-05
lang: en
---

> From 137 items, 3 important content pieces were selected

---

**Agent Harness Architecture**
1. [fastmcp v3.4.8 Released](#item-harness-arch-1) ⭐️ 6.3/10
2. [OpenSRE v0.1 发布 Alpha](#item-harness-arch-2) ⭐️ 5.5/10

**AI Agent Engineer**
1. [Apex-2 3.87B MoE 从零训练](#item-agent-engineer-1) ⭐️ 5.5/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [fastmcp v3.4.8 Released](https://github.com/PrefectHQ/fastmcp/releases/tag/v3.4.8) ⭐️ 6.3/10

fastmcp v3.4.8 ships security and bug fixes for the FastMCP framework. The release extends Host/Origin protection to the SSE transport, strips Cookie from forwarded HTTP headers, and routes component manager requests through the server&\#x27;s auth provider. It also bounds CIMD cache growth and corrects schema inlining, tool lookup, and OpenAPI argument handling. The maintainers urge all users to upgrade.

github · jlowin · Oct 4, 16:55

**「Design Notes」** Component manager routes now inherit the server&\#x27;s auth provider, closing an authentication gap for internal management endpoints. CIMD cache growth is bounded to prevent unbounded memory consumption, and dev app previews require a startup-URL session.

**「What Changed」** SSE transport now enforces Host/Origin protection, forwarded headers drop Cookie, and component manager routes use the server&\#x27;s auth provider. CIMD cache growth is bounded, and hashed tool lookups respect transforms, enabled state, and auth.

**Tags**: `#permissions`, `#mcp`, `#runtime`, `#sandbox`

---

<a id="item-harness-arch-2"></a>
### [OpenSRE v0.1 发布 Alpha](https://github.com/Tracer-Cloud/opensre) ⭐️ 5.5/10

OpenSRE v0.1 发布 Alpha，定位为构建 AI SRE agent 的开源框架。项目提供工具集成与训练评估环境，宣称可连接 60+ 现有工具、自定义工作流，并在自有基础设施上回答生产问题。现有材料仅给出高层描述，未披露运行时、状态管理、权限或工具协议等实现细节。

rss · GitHub Trending Daily · Oct 5, 02:10

**Tags**: `#runtime`, `#tools`, `#eval`, `#planning`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [Apex-2 3.87B MoE 从零训练](https://www.reddit.com/r/LocalLLaMA/comments/1wxiy8y/i_trained_a_387b_moe_145b_active_from_scratch_on/) ⭐️ 5.5/10

开发者从零训练了 3.87B 参数的 MoE 模型 Apex-2，每 token 激活 1.45B。全 MoE 架构，32 层，d\_model 2048，GQA 16Q/4KV，16 专家 top-4，上下文 4096，使用 Qwen3 分词器。预训练仅用 86.5B token，在单张 GH200 上启动后扩展至两张并采用 DiLoCo；SFT 约 2.5B token，侧重代码与数学。DPO 实验失败后回退到 SFT 检查点。SFT 后 HumanEval 43.9、HumanEval+ 41.5、MBPP 56.3，但 MMLU 仅 28.6，数学与知识明显偏弱。作者指出模型几乎只支持英文，4k 上下文，LiveCodeBench 中高难度接近零分。

reddit · r/LocalLLaMA · /u/Prestigious-Taste-63 · Oct 4, 15:50

**「为什么重要」** 该报告给出一个可复现的小规模 MoE 训练案例：用约 0.087T 预训练 token 让基座 HumanEval+ 追平了用 18T token 训练的 Qwen2.5-1.5B。对资源受限的团队，这提供了在极低数据量下训练代码向 MoE 的实测参照，同时暴露了 DPO 在此规模下可能反噬代码与指令遵循能力。

**「可关注」** 可关注：在 3.87B/1.45B active 的 MoE 上，DPO（220k 对，长度归一化）显著拉长输出并损害 HumanEval、MATH-500 与 IFEval，作者最终保留 SFT 检查点；若做小规模代码模型后训练，需先验证偏好优化是否伤害指令遵循与代码正确性。

**Tags**: `#eval`, `#coding-agent`, `#model-training`

---