---
layout: default
title: "Horizon Summary: 2026-11-01 (ZH)"
date: 2026-11-01
lang: zh
---

> 从 144 条内容中筛选出 2 条重要资讯。

<nav id="ah-toc" class="ah-toc" aria-label="目录"><span class="ah-toc-title">目录</span><ul><li><a href="#sec-agent-engineer"><span class="ah-toc-name">Agent 工程师日报</span><span class="ah-toc-count">2条</span></a></li></ul></nav>

---

**[Agent 工程师日报](#sec-agent-engineer)**
1. [ChatGPT HTML 预览沙箱漏洞修复](#item-agent-engineer-1) ⭐️ 7.0/10
2. [QwenPU 将 stories260k 编译进 Qwen 权重](#item-agent-engineer-2) ⭐️ 6.0/10

---

## Agent 工程师日报
{: #sec-agent-engineer .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-agent-engineer" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-agent-engineer-1"></a>
### [ChatGPT HTML 预览沙箱漏洞修复](https://simonwillison.net/2026/Oct/31/how-we-took-over-chatgpt-accounts/) ⭐️ 7.0/10

2026 年 10 月 31 日，Simon Willison 博客转述安全团队 Parameter Labs 的披露，ChatGPT 的 HTML 预览（曾称 Canvas）功能的沙箱 iframe 存在账户接管漏洞。攻击链利用 MathLive 库的 postMessage 接口：父页面通过 innerHTML 处理跨域消息，可插入无沙箱限制的 iframe，再结合 YouTube oEmbed 端点绕过 CSP 执行 JavaScript，最终窃取已登录用户的私有数据或代其发起操作。OpenAI 已修复该漏洞，支付 5000 美元 bug bounty，披露方认为该赏金金额偏低。

rss · Simon Willison · 10月31日 23:15

**「为什么重要」** 该漏洞是已公开验证的可利用沙箱逃逸链，直接冲击所有在 agent harness 中渲染不受信 HTML 内容的场景，证明主流 AI 平台的沙箱隔离仍可能存在跨域交互风险；目前尚未证实其他采用类似 postMessage 机制的 iframe 沙箱系统存在同类问题。

**「可关注」** 若 agent 系统需要渲染不受信 HTML 内容，需严格校验 postMessage 消息来源、禁止用 innerHTML 处理跨域消息、收紧 CSP 允许的脚本加载域名，避免出现同类沙箱逃逸风险。

**标签**: `#permissions`, `#coding-agent`, `#harness`, `#observability`

---

<a id="item-agent-engineer-2"></a>
### [QwenPU 将 stories260k 编译进 Qwen 权重](https://www.reddit.com/r/LocalLLaMA/comments/1xkiuut/an_llm_inside_an_llm_same_guy_who_put_a_riskv_cpu/) ⭐️ 6.0/10

2026 年 10 月 31 日，社区开源项目 QwenPU 公开代码仓库（GitHub: divagr18/QwenPU）与 HuggingFace 权重（divagr1925/QwenPU），其作者此前曾公开过将 RISC-V CPU 嵌入 Qwen 权重的实验，本次将 Karpathy 的 stories260k LLM 编译为支持 matmul、softmax、attention bit-exact 运算的 NPU，完整嵌入 Qwen 3.5-4B 的模型权重中，无需外部依赖即可运行。创作者表示完整技术说明仍在撰写，同时推进优化与体积缩减工作，目前无公开的生产用例验证。

reddit · r/LocalLLaMA · /u/LatentSpacer · 10月31日 19:18

**「为什么重要」** 该实验验证了模型权重内嵌自定义计算单元的极端打包思路，但完整技术细节未公开，也无已验证的生产场景价值，目前仅作为开源技术实验存在。

**「可关注」** 可关注：权重内嵌自定义计算单元的可行性已被社区实验验证，但完整实现细节、性能边界与压缩空间尚未公开。

**标签**: `#orchestration`, `#model-optimization`, `#open-source-model`

---