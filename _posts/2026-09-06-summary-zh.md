---
layout: default
title: "Horizon Summary: 2026-09-06 (ZH)"
date: 2026-09-06
lang: zh
---

> 从 127 条内容中筛选出 3 条重要资讯。

---

**Harness 架构**
1. [gemini-cli v0.60.0-nightly.20260905.g85aca163f 发布](#item-harness-arch-1) ⭐️ 5.8/10
2. [sglang v0.5.19 发布](#item-harness-arch-2) ⭐️ 5.8/10

**Agent 工程师日报**
1. [Anthropic 形式化费马大定理](#item-agent-engineer-1) ⭐️ 9.0/10

---

## Harness 架构

<a id="item-harness-arch-1"></a>
### [gemini-cli v0.60.0-nightly.20260905.g85aca163f 发布](https://github.com/google-gemini/gemini-cli/releases/tag/v0.60.0-nightly.20260905.g85aca163f) ⭐️ 5.8/10

gemini-cli v0.60.0-nightly.20260905.g85aca163f 发布。修复了环境变化同意提示和运行时环境变量清理。增强了 workspace 路径边界检查和符号链接解析。加强了系统配置路径的权限和所有权检查。

github · gemini-cli-robot · 9月5日 01:26

**「改了什么」** 修复了环境变化同意提示和运行时环境变量清理，增强了 workspace 路径边界检查和符号链接解析，并加强了系统配置路径的权限和所有权检查。

**标签**: `#permissions`, `#sandbox`, `#runtime`, `#tools`, `#config`

---

<a id="item-harness-arch-2"></a>
### [sglang v0.5.19 发布](https://github.com/sgl-project/sglang/releases/tag/v0.5.19) ⭐️ 5.8/10

sglang v0.5.19 发布，786 个 PR 来自 214 位贡献者。新支持 Qwen3.8 \(2.4T-A95B\)、Qwen3.8-27B、dots3.note、Ling-3.0-flash、Ling-3.0-tiny、Spark2.5、MiniCPM-SALA、Granite 4.2 以及 LongCat-Image-Edit &amp; Edit-Turbo 等模型。新增 beam search 功能，支持 DeepEP v2 后端，并将 unified radix tree 设为默认 cache。更新 cookbook 指南和多个依赖包。

github · Qiaolin-Yu · 9月5日 02:27

**「改了什么」** v0.5.19 引入 beam search 支持和 DeepEP v2 引擎，将 unified radix tree 设为默认 cache。新增 LayerNorm sequence parallelism 优化和多个模型支持。

**标签**: `#runtime`, `#models`, `#release`

---

## Agent 工程师日报

<a id="item-agent-engineer-1"></a>
### [Anthropic 形式化费马大定理](https://www.anthropic.com/research/formalizing-fermats-last-theorem) ⭐️ 9.0/10

Anthropic 发布研究博文 Formalizing Fermat&\#x27;s Last Theorem。该条由 Lobsters RSS 转出，材料只有标题和链接，没有正文。分析摘要称 Claude 3.5 Sonnet 用 Lean 形式化费马大定理，并开源代码。模型版本、形式化范围和开源内容均未对照原文核实。

rss · Lobsters · 9月5日 12:54

**「为什么重要」** 长证明形式化是数学推理 agent 的硬任务。分析把它标成评测方向，材料没有任务集、基线和分数。

**「可关注」** 可关注：先核对 Lean 证明复盖了哪些引理、用了哪个 Claude 版本、代码能否复现。这些点材料都没给出。

**标签**: `#coding-agent`, `#eval`, `#harness`, `#orchestration`

---