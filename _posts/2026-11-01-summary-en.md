---
layout: default
title: "Horizon Summary: 2026-11-01 (EN)"
date: 2026-11-01
lang: en
---

> From 144 items, 2 important content pieces were selected

---

**AI Agent Engineer**
1. [ChatGPT HTML 沙箱账户接管漏洞](#item-agent-engineer-1) ⭐️ 7.0/10
2. [QwenPU 将 LLM 嵌入 Qwen 权重](#item-agent-engineer-2) ⭐️ 6.0/10

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [ChatGPT HTML 沙箱账户接管漏洞](https://simonwillison.net/2026/Oct/31/how-we-took-over-chatgpt-accounts/) ⭐️ 7.0/10

Parameter Labs 于 2026-10-31 公开了针对 ChatGPT HTML 预览（原 Canvas）沙箱 iframe 的账户接管漏洞链。攻击利用 MathLive 库的 postMessage 接口，使父页面通过 innerHTML 注入无沙箱限制的 iframe，再借助 YouTube oEmbed 端点绕过内容安全策略（CSP）执行 JavaScript，最终窃取已登录用户的私有数据或代其执行操作。OpenAI 已修复漏洞并支付 5000 美元赏金，但该披露为第三方研究人员的二次转述，非 OpenAI 官方公告或同行评审论文，且未披露受影响的具体 ChatGPT 版本范围。

rss · Simon Willison · Oct 31, 23:15

**「为什么重要」** 该漏洞证明主流 AI 平台的 HTML 渲染沙箱仍存在跨 iframe 脚本注入风险，对构建渲染不可信内容的 coding agent 和 harness 具有直接参考价值。目前仅确认 OpenAI 已修复，尚未见其他平台或类似实现受影响范围的公开信息。

**「可关注」** 可关注：渲染不可信 HTML 时，父页面接收 postMessage 后使用 innerHTML 更新 DOM 且未校验消息来源，可能成为沙箱逃逸的跳板；内容安全策略白名单中的 oEmbed 端点若存在反射型 XSS，可进一步突破脚本执行限制。

**Tags**: `#permissions`, `#coding-agent`, `#harness`, `#observability`

---

<a id="item-agent-engineer-2"></a>
### [QwenPU 将 LLM 嵌入 Qwen 权重](https://www.reddit.com/r/LocalLLaMA/comments/1xkiuut/an_llm_inside_an_llm_same_guy_who_put_a_riskv_cpu/) ⭐️ 6.0/10

2026年10月31日，开源项目QwenPU公开代码与HuggingFace权重，将Karpathy的stories260k LLM以位精确方式编译进Qwen 3.5-4B的模型权重中，内嵌NPU可独立完成矩阵乘法、softmax与注意力运算，无需外部工具依赖。公开代码托管于GitHub仓库divagr18/QwenPU，权重发布在HuggingFace的divagr1925/QwenPU下。目前创作者尚未发布完整技术说明，仍在推进性能优化与体积缩减，该技术仅处于早期实验阶段，无已证实的生产用例与agent工程相关落地场景。

reddit · r/LocalLLaMA · /u/LatentSpacer · Oct 31, 19:18

**「为什么重要」** 该实验首次公开演示了将完整可运行LLM与NPU运算逻辑打包进现有大模型权重的可行性，突破了传统大模型权重仅存储参数的边界，为端侧轻量化部署提供了全新的实验思路。但目前仅处于概念验证阶段，无已证实的实际应用价值与工程落地路径。

**「可关注」** 可关注：该实验的位精确NPU权重打包思路若后续公开完整实现，或为端侧大模型轻量化、无外部依赖运行提供新的技术参考。

**Tags**: `#orchestration`, `#model-optimization`, `#open-source-model`

---