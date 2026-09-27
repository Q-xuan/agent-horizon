---
layout: default
title: "Horizon Summary: 2026-09-28 (ZH)"
date: 2026-09-28
lang: zh
---

> 从 147 条内容中筛选出 1 条重要资讯。

---

**Agent 工程师日报**
1. [Qwen 抑制犹豫 token 提升数学准确率](#item-agent-engineer-1) ⭐️ 6.0/10

---

## Agent 工程师日报

<a id="item-agent-engineer-1"></a>
### [Qwen 抑制犹豫 token 提升数学准确率](https://www.reddit.com/r/LocalLLaMA/comments/1wromzr/adding_logit_penalty_for_wait_maybe_and_perhaps/) ⭐️ 6.0/10

Reddit 用户 am17an 报告，对 Qwen3.5-4B GGUF 量化模型施加 logit 惩罚，抑制 &quot;wait&quot;、&quot;maybe&quot; 等犹豫 token，MATH-500 准确率提升。测试基于 50 道随机题目，覆盖 BF16 到 Q2\_K 五种量化。结果显示 BF16 从 74% 升至 84%，Q2\_K 从 12% 升至 24%，推理 token 普遍减少 11%–19%。作者声明这是单模型单次测试，结果待复现。

reddit · r/LocalLLaMA · /u/am17an · 9月27日 16:29

**「为什么重要」** 这是 harness 层面的具体干预，可直接用 llama.cpp 的 --logit-bias 复现。在低量化模型上提升幅度最大，Q2\_K 准确率从 12% 升至 24%。

**「可关注」** 可关注：该实验仅覆盖 50 题和一个模型，准确率提升是否稳定需更多样本验证；惩罚 token 列表来自 Meta 论文的 overthinking markers，直接套用到 Qwen 上有效但机制未明。

**标签**: `#eval`, `#harness`, `#coding-agent`

---