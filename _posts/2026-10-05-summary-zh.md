---
layout: default
title: "Horizon Summary: 2026-10-05 (ZH)"
date: 2026-10-05
lang: zh
---

> 从 137 条内容中筛选出 3 条重要资讯。

---

**Harness 架构**
1. [fastmcp v3.4.8 发布](#item-harness-arch-1) ⭐️ 6.3/10
2. [OpenSRE v0.1 发布](#item-harness-arch-2) ⭐️ 5.5/10

**Agent 工程师日报**
1. [3.87B MoE Apex-2 从零训练](#item-agent-engineer-1) ⭐️ 5.5/10

---

## Harness 架构

<a id="item-harness-arch-1"></a>
### [fastmcp v3.4.8 发布](https://github.com/PrefectHQ/fastmcp/releases/tag/v3.4.8) ⭐️ 6.3/10

fastmcp v3.4.8 发布，以安全修复为主。SSE 传输接入 Host/Origin 保护，转发 HTTP 头时剔除 Cookie。组件管理器路由改用服务器 auth provider 鉴权，CIMD 缓存增长受限。哈希工具查找纳入 transforms、enabled 状态与 auth 检查。

github · jlowin · 10月4日 16:55

**「设计要点」** SSE 传输层补齐 Host/Origin 校验，与既有 HTTP 传输对齐。工具查找链路统一走服务器端 lookup，注入工具与哈希查找均受 transforms、enabled 状态和 auth 约束。客户端 schema 构建改用 create\_model 并加 bounded cache，防止无界增长。

**「改了什么」** SSE 传输获得 Host/Origin 防护；HTTP 头转发排除 Cookie；组件管理器路由鉴权切换到服务器 auth provider；CIMD 缓存设置上限；哈希工具查找应用 transforms、enabled 与 auth；客户端 schema 类型构建引入 create\_model 与 bounded caches；OpenAPI 组件仅发送声明参数并保留配置头。

**标签**: `#permissions`, `#mcp`, `#runtime`, `#sandbox`

---

<a id="item-harness-arch-2"></a>
### [OpenSRE v0.1 发布](https://github.com/Tracer-Cloud/opensre) ⭐️ 5.5/10

OpenSRE v0.1 以公共 alpha 发布，定位为构建 AI SRE 代理的开源框架。宣称可连接 60+ 现有工具、自定义工作流，并在自有基础设施上回答生产问题。同时提供代理改进所需的训练与评估环境。目前核心工作流可用于早期探索，但尚未完整。

rss · GitHub Trending Daily · 10月5日 02:10

**标签**: `#runtime`, `#tools`, `#eval`, `#planning`

---

## Agent 工程师日报

<a id="item-agent-engineer-1"></a>
### [3.87B MoE Apex-2 从零训练](https://www.reddit.com/r/LocalLLaMA/comments/1wxiy8y/i_trained_a_387b_moe_145b_active_from_scratch_on/) ⭐️ 5.5/10

开发者从零训练 3.87B MoE 模型 Apex-2，每 token 激活 1.45B 参数；全 MoE 层，32 层，d\_model 2048，GQA 16Q/4KV，16 专家 top-4，上下文 4096，Qwen3 tokenizer。预训练 86.5B token，GH200 单卡扩双卡，用 DiLoCo；SFT 约 2.5B token，偏代码和数学；DPO 220k 对试过，答案变长，代码、数学、IFEval 分数下降，弃用。SFT 后 HumanEval 43.9，HumanEval+ 41.5，MBPP 56.3，GSM8K 32.4，MATH-500 21.0，IFEval 44.7，MMLU 28.6；作者对比：0.087T 预训练 token 下，base 模型 HumanEval+ 追平用 18T token 的 Qwen2.5-1.5B。模型已上 Hugging Face，可通过 Qwen3MoeForCausalLM 用 transformers / vLLM 加载；限制：英语为主，知识弱，LiveCodeBench 中高难近零，4k 上下文。

reddit · r/LocalLLaMA · /u/Prestigious-Taste-63 · 10月4日 15:50

**「为什么重要」** 小数据量下全 MoE 架构在代码基准上展现效率，但 MMLU 和数学仍受数据量限制。DPO 在该规模反效果，对做小规模代码模型的人有直接参考。

**「可关注」** 可关注：86.5B token 预训练 + 偏代码 SFT 可让 3.87B MoE 的 HumanEval+ 到 41.5，但长度归一化 DPO 反而损害代码与指令遵循；小规模对齐阶段需重新评估。

**标签**: `#eval`, `#coding-agent`, `#model-training`

---