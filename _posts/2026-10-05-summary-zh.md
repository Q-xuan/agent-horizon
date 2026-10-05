---
layout: default
title: "Horizon Summary: 2026-10-05 (ZH)"
date: 2026-10-05
lang: zh
---

> 从 136 条内容中筛选出 2 条重要资讯。

---

**Harness 架构**
1. [FastMCP v3.4.8 发布](#item-harness-arch-1) ⭐️ 6.8/10

**Agent 工程师日报**
1. [Apex-2：3.87B MoE 从零训练](#item-agent-engineer-1) ⭐️ 5.5/10

---

## Harness 架构

<a id="item-harness-arch-1"></a>
### [FastMCP v3.4.8 发布](https://github.com/PrefectHQ/fastmcp/releases/tag/v3.4.8) ⭐️ 6.8/10

FastMCP v3.4.8 发布安全补丁。SSE 传输接入 Host/Origin 保护，转发 HTTP 头剔除 Cookie。组件管理器路由改用服务器 auth provider 认证，CIMD 缓存增长受限。哈希工具查找同步应用 transforms、enabled 状态与 auth。

github · jlowin · 10月4日 16:55

**「设计要点」** 传输层与工具查找统一收敛到服务器 auth provider 与 Host/Origin 策略，压缩未授权访问面。客户端 schema 构建引入 create\_model 与 bounded cache，控制内存与生成体积。

**「改了什么」** SSE 补齐 Host/Origin 防护并剔除转发 Cookie，组件管理器路由切换至服务器 auth provider。客户端 schema 构建改用 create\_model 与 bounded cache，超大 schema 保留 $ref 指针，CIMD 缓存设上限。

**标签**: `#mcp`, `#permissions`, `#runtime`

---

## Agent 工程师日报

<a id="item-agent-engineer-1"></a>
### [Apex-2：3.87B MoE 从零训练](https://www.reddit.com/r/LocalLLaMA/comments/1wxiy8y/i_trained_a_387b_moe_145b_active_from_scratch_on/) ⭐️ 5.5/10

/u/Prestigious-Taste-63 从零训练了 3.87B 总参数、1.45B 激活的 MoE 模型 Apex-2，未使用外部基础权重，权重与架构细节已公开。模型全 MoE 层、32 层、d\_model 2048、GQA 16Q/4KV、16 专家 top-4，上下文 4096，使用 Qwen3 151k 分词器，可通过 transformers / vLLM 以 Qwen3MoeForCausalLM 加载。预训练消耗 86.5B tokens（GH200 单卡扩至双卡，DiLoCo），SFT 约 2.5B tokens；SFT 后 HumanEval 43.9、HumanEval+ 41.5、MBPP 56.3、GSM8K 32.4、MATH-500 21.0、MMLU 28.6。作者称基座 HumanEval+ 以约 0.087T tokens 追平使用 18T tokens 的 Qwen2.5-1.5B，但知识与数学仍落后；DPO 在 220k 长度归一化数据上使回答变长并损害代码、数学与 IFEval，已弃用，模型局限为英文中心、知识薄弱、LiveCodeBench 中高难度接近零、4k 上下文。

reddit · r/LocalLLaMA · /u/Prestigious-Taste-63 · 10月4日 15:50

**「为什么重要」** 该帖公开了小规模从零训练 MoE 的完整配置、基准与 DPO 失败记录，为 coding agent 与 harness 开发者提供了可复现参考；作者报告的 token 效率对比（0.087T vs 18T）若成立，说明代码能力对小数据量更敏感，而知识任务仍受数据差距限制。

**「可关注」** 可关注：在 4k 上下文、英文中心的小 MoE 上，DPO 的长度归一化策略可能反向损害代码与指令遵循，SFT 检查点比继续偏好优化更稳。

**标签**: `#eval`, `#coding-agent`, `#moe`

---