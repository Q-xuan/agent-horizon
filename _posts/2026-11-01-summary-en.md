---
layout: default
title: "Horizon Summary: 2026-11-01 (EN)"
date: 2026-11-01
lang: en
---

> From 143 items, 4 important content pieces were selected

---

**Agent Harness Architecture**
1. [LangChain Deep Agents 开源](#item-harness-arch-1) ⭐️ 5.5/10

**AI Agent Engineer**
1. [ChatGPT HTML 预览沙箱漏洞](#item-agent-engineer-1) ⭐️ 8.0/10
2. [Betelgeuse 实现 RTX 3060 跑 Qwen 3.8 Flash Next 高 bit 推理](#item-agent-engineer-2) ⭐️ 6.0/10
3. [Betelgeuse 跑 Qwen 3.8 Flash Next IQ4\_XS 基准](#item-agent-engineer-3) ⭐️ 6.0/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [LangChain Deep Agents 开源](https://github.com/langchain-ai/deepagents) ⭐️ 5.5/10

LangChain 开源 Deep Agents，一个开箱即用的 agent harness。该工具针对长期多步骤任务提供默认调优，支持任意具备 tool calling 能力的 LLM，并允许覆盖或替换任意组件而不必 fork。目前仅公开高层设计原则，无官方发布说明、变更日志或具体实现路径。

rss · GitHub Trending Daily · Nov 1, 01:46

**Tags**: `#agent-harness`, `#open-source`, `#langchain`, `#tools`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [ChatGPT HTML 预览沙箱漏洞](https://simonwillison.net/2026/Oct/31/how-we-took-over-chatgpt-accounts/) ⭐️ 8.0/10

Parameter Labs 于 2026-10-31 披露 ChatGPT HTML 预览功能（曾称 Canvas）的沙箱逃逸漏洞。攻击链利用 MathLive 虚拟键盘的 postMessage\(\) 接口，在父页面通过 innerHTML 注入无沙箱限制的 iframe，再借助 YouTube oEmbed 端点绕过内容安全策略执行 JavaScript，最终通过分享链接窃取已登录用户私密数据或代其执行操作。OpenAI 已修复漏洞并支付 5000 美元赏金，披露者认为该金额对如此严重的漏洞偏低。

rss · Simon Willison · Oct 31, 23:15

**「为什么重要」** 该漏洞揭示沙箱 iframe 中运行不可信代码时，第三方库的 postMessage 接口与父页面 innerHTML 组合可突破隔离边界。即使内容安全策略限制内联脚本，信任域的反射漏洞仍可被利用执行任意代码。对实现 coding agent 的工程师而言，这直接关系到 untrusted code 执行环境的安全设计。

**「可关注」** 可关注：沙箱 iframe 内第三方库的 postMessage 接收端若使用 innerHTML 且未校验消息来源，可能被利用注入无沙箱限制的 iframe；同时需审查内容安全策略允许的信任域是否存在反射型漏洞。

**Tags**: `#coding-agent`, `#permissions`, `#security`, `#sandbox`, `#artifacts`

---

<a id="item-agent-engineer-2"></a>
### [Betelgeuse 实现 RTX 3060 跑 Qwen 3.8 Flash Next 高 bit 推理](https://www.reddit.com/r/LocalLLaMA/comments/1xk8s6z/betelgeuse_running_qwen_38_flash_next_at_22_toks/) ⭐️ 6.0/10

Reddit 用户 /u/zyxciss 分享其开发的 llama.cpp 分支 Betelgeuse 的测试结果：在 RTX 3060 12GB + 16GB DDR4 单通道内存的消费级硬件上，Qwen 3.8 Flash Next MoE 模型可实现 22 tok/s 持续推理速度，峰值 48 tok/s，且未做任何专家剪枝，输出 100% 位精确。测试对比 stock llama.cpp 同配置冷启动仅 1.47 tok/s，Strata 同配置强制低内存模式仅 8.11 tok/s；Betelgeuse 通过 Arrival-Slack VRAM 槽池、流内 GPU 门铃调度、RAM 受害者缓存等优化实现提速，同时将单 token 物理 NVMe 读取量从 ~71 MB 降至 12.43 MB。该结果未获官方验证，仅为个人实践分享，作者还提到正在将相关架构移植到 DeepSeek V4.1 Flash 模型，早期测试同硬件已达 ~25 tok/s。

reddit · r/LocalLLaMA · /u/zyxciss · Oct 31, 12:20

**「为什么重要」** 消费级硬件运行 MoE 大模型普遍受限于显存容量与调度开销，该分享提供了无专家剪枝前提下提升本地推理速度的可参考实践路径，对本地部署 MoE 模型的工程师有参考价值，但结果尚未经官方或第三方复现验证。

**「可关注」** 可关注 Betelgeuse 针对 MoE 模型的显存槽池非均匀分配、流内门铃替代跨流调度同步、RAM 与 VRAM 专属缓存隔离这三项优化设计，以及其放弃牺牲输出质量的专家剪枝方案的实践思路。

**Tags**: `#harness`

---

<a id="item-agent-engineer-3"></a>
### [Betelgeuse 跑 Qwen 3.8 Flash Next IQ4\_XS 基准](https://www.reddit.com/r/LocalLLaMA/comments/1xkh2ns/betelgeuse_running_qwen_38_flash_next_iq4_xs_at/) ⭐️ 6.0/10

Reddit 用户 /u/zyxciss 分享 Betelgeuse 推理工具（bel-cli / bel-server）在 RTX 3060 12GB 上运行 IQ4\_XS 量化版 Qwen 3.8 Flash Next 的实测基准数据。16GB 总系统内存下，单通道 1x16GB DDR4 配置吞吐 14 tok/s，双通道 2x8GB DDR4 配置吞吐 24 tok/s；对比 stock llama.cpp，单通道仅 ~0.5 tok/s（抖动）、双通道仅 ~0.6 tok/s（抖动），且 Betelgeuse 输出与 stock llama.cpp 100% 字节级一致。此外测试还显示 IQ2\_XS 量化下单通道配置吞吐 22.03 tok/s（48 tok/s 突发），Q8\_K\_XL 量化下 stock llama.cpp 出现 OOM，而 Betelgeuse 单通道配置可跑 8 tok/s（冷启动）/12 tok/s（热启动）。该测试为未审计的单用户实测，无官方背书，作者提及的 DeepSeek V4.1 Flash 适配仍处于开发阶段，相关性能数据尚未落地。

reddit · r/LocalLLaMA · /u/zyxciss · Oct 31, 18:06

**「为什么重要」** 该测试提供了消费级硬件运行高比特 MoE 量化模型的真实可参考吞吐数据，明确验证了内存带宽对 MoE 推理性能的关键影响，对本地 agent 部署的硬件选型有参考意义；作者提及的 DeepSeek V4.1 Flash 适配仍处于开发阶段，相关性能声明尚未得到验证。

**「可关注」** 消费级平台部署高比特 MoE 量化模型时，同容量双通道内存配置对吞吐的提升远高于单通道，Betelgeuse 采用的主机内存受害者缓存 + 异步硬件 DMA 路径可有效缓解 MoE 专家换入换出的带宽瓶颈，相关架构思路可参考。

**Tags**: `#harness`

---