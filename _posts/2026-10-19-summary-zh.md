---
layout: default
title: "Horizon Summary: 2026-10-19 (ZH)"
date: 2026-10-19
lang: zh
---

> 从 159 条内容中筛选出 4 条重要资讯。

<nav id="ah-toc" class="ah-toc" aria-label="目录"><span class="ah-toc-title">目录</span><ul><li><a href="#sec-harness-arch"><span class="ah-toc-name">Harness 架构</span><span class="ah-toc-count">2条</span></a></li><li><a href="#sec-agent-engineer"><span class="ah-toc-name">Agent 工程师日报</span><span class="ah-toc-count">2条</span></a></li></ul></nav>

---

**[Harness 架构](#sec-harness-arch)**
1. [vLLM v0.32.0 发布](#item-harness-arch-1) ⭐️ 7.8/10
2. [fastmcp v4.1.1 发布](#item-harness-arch-2) ⭐️ 5.3/10

**[Agent 工程师日报](#sec-agent-engineer)**
1. [DeepSeek Search and Fetch API 定价公布](#item-agent-engineer-1) ⭐️ 7.0/10
2. [llm-echo 0.5 发布](#item-agent-engineer-2) ⭐️ 6.3/10

---

## Harness 架构
{: #sec-harness-arch .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-harness-arch" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-harness-arch-1"></a>
### [vLLM v0.32.0 发布](https://github.com/vllm-project/vllm/releases/tag/v0.32.0) ⭐️ 7.8/10

vLLM v0.32.0 正式发布，新增 \`POST /v1/systemone\` 结构化输出端点与 \`--tool-call-parser hf\` / \`--reasoning-parser hf\` 通用解析器，模型无需特定配置即可接入。NVFP4 与 FP8 KV cache 扩展至更多 GPU 架构，ROCm 新增 4-bit \`ultraquant\_4bit\` KV cache。Model Runner V2 成为 ROCm 默认，引入 GPU n-gram 推测与 Elastic EP。该版本移除 Python 3.10 支持、cascade attention 及 \`mamba\_cache\_mode=&quot;all&quot;\`，并收紧默认 CORS 策略。

github · khluu · 10月18日 06:50

**「设计要点」** 运行时默认切换至 Model Runner V2，支持 GPU n-gram 推测、Elastic EP 及 MLA 模型的 prefill context parallelism。工具层通过 \`vllm download-kernels\` 与 \`vllm preload --preload-autotune\` 预热 FlashInfer 内核与自动调优表，多模态张量通过共享内存一次广播至 workers。

**「改了什么」** 新增结构化输出端点与通用解析器，NVFP4/FP8 KV cache 覆盖更多 GPU 架构，Model Runner V2 成为 ROCm 默认。移除 Python 3.10 支持、cascade attention、\`mamba\_cache\_mode=&quot;all&quot;\`，默认 CORS 策略收紧，\`max\_tokens\` 不再预留上下文窗口空间。

**标签**: `#runtime`, `#tools`, `#prefix-cache`

---

<a id="item-harness-arch-2"></a>
### [fastmcp v4.1.1 发布](https://github.com/PrefectHQ/fastmcp/releases/tag/v4.1.1) ⭐️ 5.3/10

PrefectHQ 的 fastmcp 发布 v4.1.1 补丁版本，核心包含两项安全加固与两项 bug 修复：正则工具搜索新增 1000 字符长度上限与约 1 秒执行超时，防止正则表达式拒绝服务攻击；SkillsDirectoryProvider 恢复对链接技能文件夹的发现能力，支持指向技能根目录外部的链接，要求技能自身文件仍在其链接的文件夹内可解析。同时修复不可解析代理配置阻断更新检查、JWKS 刷新锁混入子类属性的问题，另有示例代码路由修复，所有 4.x 用户建议升级，本次发布有 4 位贡献者，其中 1 位为首次贡献者。

github · zzstoatzz · 10月18日 02:12

**「改了什么」** 相对 v4.1.0，新增正则工具搜索的长度与耗时边界防止 DoS，恢复链接技能文件夹发现能力并保留路径约束；修复不可解析代理配置中断更新检查、JWKS 刷新锁携带子类属性的问题，同时修正组件管理路由中版本查询参数到 VersionSpec 的转换逻辑。

**标签**: `#tools`, `#permissions`, `#mcp`

---

## Agent 工程师日报
{: #sec-agent-engineer .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-agent-engineer" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-agent-engineer-1"></a>
### [DeepSeek Search and Fetch API 定价公布](https://api-docs.deepseek.com/guides/search/) ⭐️ 7.0/10

DeepSeek 2026 年 10 月 18 日发布 Search and Fetch API 官方文档，定价为每 1000 次成功请求$0.75，面向 AI agent 提供低成本网页搜索能力。该定价显著低于 Brave Search API 的每千次$5、Kagi API 的每千次$12，为 coding agent 工具链开发者提供了新的付费搜索选项。

hackernews · fagnerbrack · 10月18日 06:50 · [社区讨论](https://news.ycombinator.com/item?id=50138531)

**「为什么重要」** 当前 AI agent 工具链可选的付费网页搜索服务普遍成本较高，DeepSeek 该 API 的定价显著低于现有主流方案，可能降低 agent 搜索功能的落地成本。

**「可关注」** 可关注：DeepSeek Search and Fetch API 每千次$0.75 的定价低于 Brave、Kagi 同类服务，可纳入 agent 搜索工具链的成本对比范围。

**「评论」** 社区讨论中，有用户推荐自建 searxng-ai-kit 等免费方案替代付费搜索 API，也有用户推测搜索 API 价格未来可能因流量竞争进一步走低，另有用户指出 Google 未提供付费搜索 API 是这类第三方服务存在的原因。

**标签**: `#coding-agent`, `#orchestration`, `#permissions`

---

<a id="item-agent-engineer-2"></a>
### [llm-echo 0.5 发布](https://github.com/simonw/llm-echo/releases/tag/0.5) ⭐️ 6.3/10

2026 年 10 月 18 日，simonw 发布 llm-echo 0.5 版本。该工具是 LLM 生态的调试插件，依赖 LLM&gt;=0.36，核心功能是模拟回显输入给模型的 prompt，无需真实调用 LLM。本次更新新增对 reasoning tokens 的支持，同时调整模拟 token 统计逻辑，将 tool calls、推理文本、系统提示词纳入统计范围。该工具面向使用 LLM 构建 agent、开展可观测性与成本跟踪的开发者。

github · simonw · 10月18日 23:16

**「为什么重要」** 该更新完善了无真实 LLM 调用场景下的 token 统计维度，对 agent 调试、成本预估场景有直接参考价值，目前暂无更广泛的生态影响报道。

**「可关注」** 可关注：无真实 LLM 调用的调试、测试场景中，token 统计需同步覆盖 tool calls、推理文本、系统提示词等新增维度，避免成本预估出现偏差。

**标签**: `#observability`, `#eval`, `#coding-agent`

---