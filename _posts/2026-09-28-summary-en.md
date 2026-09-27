---
layout: default
title: "Horizon Summary: 2026-09-28 (EN)"
date: 2026-09-28
lang: en
---

> From 147 items, 1 important content pieces were selected

---

**AI Agent Engineer**
1. [Qwen 加 logit 惩罚提升准确率](#item-agent-engineer-1) ⭐️ 6.0/10

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [Qwen 加 logit 惩罚提升准确率](https://www.reddit.com/r/LocalLLaMA/comments/1wromzr/adding_logit_penalty_for_wait_maybe_and_perhaps/) ⭐️ 6.0/10

Reddit 用户 /u/am17an 在 50 道随机 MATH-500 题目上测试 Qwen3.5-4B 的多个 GGUF 量化版本，对 49 个 hedging token 施加 -2 logit bias。各量化版本准确率均上升：BF16 从 74% 升至 84%，Q8\_0 从 76% 升至 80%，Q4\_K\_M 从 60% 升至 66%，Q3\_K\_M 从 52% 升至 66%，Q2\_K 从 12% 升至 24%。推理 token 数量同步下降 11.0%–19.4%，BF16 亦出现提升。token 列表取自 Meta 论文的 overthinking markers，但作者明确此为单模型单次测试。

reddit · r/LocalLLaMA · /u/am17an · Sep 27, 16:29

**「为什么重要」** 该做法把论文中的 overthinking markers 转化为 llama.cpp 可直接执行的 --logit-bias 参数，为抑制过度推理提供了一条低成本的干预路径。但 50 题样本和单一模型限制了结论强度，跨模型、跨任务的普适性尚未验证。

**「可关注」** 可关注：该干预只需在 llama.cpp 启动参数中加入 --logit-bias，实现成本低；但当前证据仅来自 50 题单模型测试，跨模型、跨任务的普适性尚未确认。

**Tags**: `#eval`, `#harness`, `#coding-agent`

---