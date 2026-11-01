---
layout: default
title: "Horizon Summary: 2026-11-01 (ZH)"
date: 2026-11-01
lang: zh
---

> 从 143 条内容中筛选出 4 条重要资讯。

<nav id="ah-toc" class="ah-toc" aria-label="目录"><span class="ah-toc-title">目录</span><ul><li><a href="#sec-harness-arch"><span class="ah-toc-name">Harness 架构</span><span class="ah-toc-count">1条</span></a></li><li><a href="#sec-agent-engineer"><span class="ah-toc-name">Agent 工程师日报</span><span class="ah-toc-count">3条</span></a></li></ul></nav>

---

**[Harness 架构](#sec-harness-arch)**
1. [LangChain Deep Agents 登 GitHub trending](#item-harness-arch-1) ⭐️ 5.5/10

**[Agent 工程师日报](#sec-agent-engineer)**
1. [ChatGPT HTML 预览沙箱逃逸漏洞披露](#item-agent-engineer-1) ⭐️ 8.0/10
2. [Betelgeuse 在 RTX 3060 跑 Qwen 3.8 Flash Next 22 tok/s](#item-agent-engineer-2) ⭐️ 6.0/10
3. [Betelgeuse 跑 Qwen3.8 Flash IQ4\_XS 实测](#item-agent-engineer-3) ⭐️ 6.0/10

---

## Harness 架构
{: #sec-harness-arch .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-harness-arch" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-harness-arch-1"></a>
### [LangChain Deep Agents 登 GitHub trending](https://github.com/langchain-ai/deepagents) ⭐️ 5.5/10

这是 GitHub trending 收录的 LangChain 新开源项目 Deep Agents，定位为开箱即用的带默认配置的 agent harness，官方文档地址为 https://docs.langchain.com/deepagents。技术上，它支持所有具备工具调用能力的 LLM，设计原则包括默认适配长周期多步任务、可扩展覆盖任意组件而无需 fork、模型无关、面向生产场景。

rss · GitHub Trending Daily · 11月1日 01:46

**标签**: `#agent-harness`, `#open-source`, `#langchain`, `#tools`

---

## Agent 工程师日报
{: #sec-agent-engineer .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-agent-engineer" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-agent-engineer-1"></a>
### [ChatGPT HTML 预览沙箱逃逸漏洞披露](https://simonwillison.net/2026/Oct/31/how-we-took-over-chatgpt-accounts/) ⭐️ 8.0/10

2026 年 10 月 31 日，Parameter Labs 披露针对 ChatGPT HTML 预览功能的复杂沙箱逃逸漏洞。攻击链利用 MathLive 库虚拟键盘的 postMessage\(\) 接口，从沙箱 iframe 向父页面发送消息；父页面接收代码使用 innerHTML 插入无沙箱限制的新 iframe，再结合 YouTube oEmbed 端点绕过 CSP，最终在 ChatGPT 页面执行 JavaScript 并窃取已登录用户私有数据。OpenAI 已修复该漏洞并支付 5000 美元漏洞赏金，作者认为赏金偏低。

rss · Simon Willison · 10月31日 23:15

**「为什么重要」** 该漏洞展示了第三方库 postMessage 接口与父页面 innerHTML 处理不当如何组合成沙箱逃逸链，对构建不可信代码执行环境的 agent 工程师有直接参考价值。

**「可关注」** 可关注：沙箱 iframe 内 postMessage 接口暴露与父页面 innerHTML 结合可能绕过同源策略与 CSP 限制。

**标签**: `#coding-agent`, `#permissions`, `#security`, `#sandbox`, `#artifacts`

---

<a id="item-agent-engineer-2"></a>
### [Betelgeuse 在 RTX 3060 跑 Qwen 3.8 Flash Next 22 tok/s](https://www.reddit.com/r/LocalLLaMA/comments/1xk8s6z/betelgeuse_running_qwen_38_flash_next_at_22_toks/) ⭐️ 6.0/10

Reddit 用户/u/zyxciss 分享其开发的 Betelgeuse 引擎（llama.cpp 分支）测试结果：在 RTX 3060 12GB + 16GB 单通道 DDR4 内存、系统内存限制 12G 的消费级 PC 上，可运行 68GB GSQ-RCO-IQ2\_XS 量化的 Qwen 3.8 Flash Next MoE 模型，实现 22 tok/s 持续解码、峰值 48 tok/s，输出 100%位精确，未做任何专家剪枝。该方案此前曾尝试通过门剪枝提速，但会 silently 降质输出，最终放弃该思路，转而通过 Arrival-Slack VRAM 专家槽池、流内 GPU 门铃+单 CUDA 图回放、RAM victim cache+io\_uring 分页器等机制实现提速，同时重构 GGUF 存储结构避免冗余专家张量占用。对比基线：同配置下 stock llama.cpp 因页错误解码仅 1.47 tok/s，Strata 低内存模式为 8.11 tok/s。注：该结果为用户自测，未获官方或第三方验证。

reddit · r/LocalLLaMA · /u/zyxciss · 10月31日 12:20

**「为什么重要」** 这是目前公开的首个消费级低配 PC 跑通大参数 MoE 模型且保持位精确、无专家剪枝的实践方案，打破了同配置下 MoE 推理要么速度极慢要么输出降质的瓶颈，为本地推理和 agent harness 的低成本部署提供了可参考的技术路径；但性能数据、模型有效性均未获第三方验证，上游 PR 也未合并，实际可用性待进一步确认。

**「可关注」** MoE 模型在低显存+小内存场景下，通过分离 VRAM 与 RAM 的专家缓存、消除逐层 CPU-GPU 调度同步开销，可在保持位精确的前提下大幅提升解码速度，但该方案的泛化性、不同硬件/模型下的表现仍需验证。

**标签**: `#harness`

---

<a id="item-agent-engineer-3"></a>
### [Betelgeuse 跑 Qwen3.8 Flash IQ4\_XS 实测](https://www.reddit.com/r/LocalLLaMA/comments/1xkh2ns/betelgeuse_running_qwen_38_flash_next_iq4_xs_at/) ⭐️ 6.0/10

2026 年 10 月 31 日，Reddit 用户/u/zyxciss 分享 Betelgeuse 推理工具（bel-cli / bel-server）的 IQ4\_XS 量化 Qwen 3.8 Flash Next 模型实测数据：搭载 RTX 3060 12GB 显卡、16GB 总系统内存的配置下，双通道 2x8GB DDR4 实现 24 tok/s 吞吐，单通道 1x16GB DDR4 为 14 tok/s，输出与 stock llama.cpp 100%字节级一致，显著高于同配置下 stock llama.cpp 的单通道~0.5 tok/s、双通道~0.6 tok/s 的 thrash 级表现。该测试为单用户未审计实测，无官方背书，对比基线为 stock llama.cpp；团队提及正在将同架构移植至 DeepSeek V4.1 Flash，早期测试同硬件约 25 tok/s，尚未公开验证。

reddit · r/LocalLLaMA · /u/zyxciss · 10月31日 18:06

**「为什么重要」** 已发生的部分为消费级硬件部署 4-bit 量化 MoE 模型提供了可参考的吞吐基准，同时验证了双通道内存配置对依赖主机内存带宽的推理场景的性能影响；尚未证实的影响是 Betelgeuse 团队提到的 DeepSeek V4.1 Flash 适配进展未经过公开验证，且单用户测试的普适性有限。

**「可关注」** 可关注：消费级硬件运行高比特量化 MoE 模型时，双通道内存配置对主机内存带宽敏感，victim cache 搭配异步硬件 DMA 的架构可显著提升推理吞吐。

**标签**: `#harness`

---