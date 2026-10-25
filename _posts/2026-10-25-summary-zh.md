---
layout: default
title: "Horizon Summary: 2026-10-25 (ZH)"
date: 2026-10-25
lang: zh
---

> 从 145 条内容中筛选出 5 条重要资讯。

<nav id="ah-toc" class="ah-toc" aria-label="目录"><span class="ah-toc-title">目录</span><ul><li><a href="#sec-harness-arch"><span class="ah-toc-name">Harness 架构</span><span class="ah-toc-count">3条</span></a></li><li><a href="#sec-agent-engineer"><span class="ah-toc-name">Agent 工程师日报</span><span class="ah-toc-count">1条</span></a></li><li><a href="#sec-ai-daily"><span class="ah-toc-name">AI 日报</span><span class="ah-toc-count">1条</span></a></li></ul></nav>

---

**[Harness 架构](#sec-harness-arch)**
1. [MCP servers v2.1.0 安全修复发布](#item-harness-arch-1) ⭐️ 7.8/10
2. [pydantic-ai v2.61.0 发布](#item-harness-arch-2) ⭐️ 6.8/10
3. [Cloudflare 安全审计技能开源](#item-harness-arch-3) ⭐️ 6.0/10

**[Agent 工程师日报](#sec-agent-engineer)**
1. [Raschka 发布推理模型从零视频课](#item-agent-engineer-1) ⭐️ 6.0/10

**[AI 日报](#sec-ai-daily)**
1. [谷歌开源 TorchTPU 一行代码跑 TPU](#item-ai-daily-1) ⭐️ 5.5/10

---

## Harness 架构
{: #sec-harness-arch .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-harness-arch" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-harness-arch-1"></a>
### [MCP servers v2.1.0 安全修复发布](https://github.com/modelcontextprotocol/servers/releases/tag/v2.1.0) ⭐️ 7.8/10

modelcontextprotocol/servers 发布 v2.1.0 安全更新，修复 filesystem、everything、fetch 三个核心 MCP 服务器的 8 个漏洞。filesystem 修复符号链接竞争条件、路径尾随引号/空白绕过、大小写符号链接绕过及目录列表信息泄露；everything 在 HTTP/SSE 传输层强制 Origin 检查并移除通配符 CORS；fetch 统一 IDNA 主机名检查、拒绝 NAT64 私有地址回连、重定向后重新校验 robots.txt。升级目标：@modelcontextprotocol/server-filesystem@2.0.1、@modelcontextprotocol/server-everything@2.0.1、mcp-server-fetch@2026.10.24。注意 TypeScript 包已切至语义版本，日期版本用户需显式指定版本号安装。

github · cliffhall · 10月25日 00:03

**「设计要点」** filesystem 在 Linux 和 macOS 上将写入操作锚定在已检查目录内缓解 TOCTOU，但 Windows 仅部分修复。everything 在传输层拒绝非预期 Origin 的跨域请求。fetch 在地址分类与连接阶段使用同一主机名形式，防止 IDNA 编码不一致导致的 SSRF。

**「改了什么」** filesystem 修复路径遍历与符号链接竞争条件，写入操作严格限制在允许目录边界内。everything 修复跨域请求漏洞，禁止外部 web 源调用服务器工具。fetch 修复 SSRF 相关漏洞，统一主机名校验逻辑并拒绝 NAT64 封装的私有 IPv4 地址。

**标签**: `#mcp`, `#tools`, `#permissions`, `#sandbox`

---

<a id="item-harness-arch-2"></a>
### [pydantic-ai v2.61.0 发布](https://github.com/pydantic/pydantic-ai/releases/tag/v2.61.0) ⭐️ 6.8/10

pydantic-ai v2.61.0 发布，调整运行时配置与工具行为。CohereModel 工具返回文件改为抛出 NotImplementedError，属破坏性变更；google\_multi\_speaker 在 GoogleRealtimeModel 上弃用。新增 MCP 托管 async auth、TextPart 结构化引用、kimi-k3.1-pro 等模型名，修复 InputGuardrail 提示词泄露，公开 durable engine 扩展接口。完整变更范围因 notes 截断不全。

github · dsfaccini · 10月24日 03:13

**「设计要点」** 将 durable engine 扩展接口公开，包括 operation types、ParameterTransports 与 DurableRunContext。CapabilityStore 按目录共享锁，支持运行中断授权流程；LocalStack 容器在 agent 上下文内单例共享，限制 aws configure 写入路径。

**「改了什么」** CohereModel 工具返回文件改为抛出 NotImplementedError，属破坏性变更；google\_multi\_speaker 在 GoogleRealtimeModel 上弃用。MCP 托管能力支持 async auth 函数，TextPart 新增结构化引用，新增 kimi-k3.1-pro 等模型名，InputGuardrail 修复提示词泄露与 fail-open 路径，durable engine 扩展接口公开。

**标签**: `#runtime`, `#tools`, `#subagents`

---

<a id="item-harness-arch-3"></a>
### [Cloudflare 安全审计技能开源](https://github.com/cloudflare/security-audit-skill) ⭐️ 6.0/10

Cloudflare 开源 security-audit-skill，这是一款编码代理安全审计技能。它编排隔离子代理执行侦察、覆盖引导搜索、候选验证、结构化输出、独立记录验证和目标中性报告，输出机器可读、独立验证的审计结果。该技能是 Cloudflare 漏洞发现 harness 的种子实现，对代理 harness 工程师有子代理工作流与沙箱集成的参考价值，但属于垂直领域工具，缺少深度技术实现细节。

rss · GitHub Trending Daily · 10月25日 00:44

**「设计要点」** 运行时通过编排隔离子代理实现多阶段安全审计，涵盖侦察、覆盖引导搜索、候选验证与结构化输出，并引入独立记录验证机制确保结果可验证。

**标签**: `#tools`, `#subagents`, `#sandbox`

---

## Agent 工程师日报
{: #sec-agent-engineer .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-agent-engineer" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-agent-engineer-1"></a>
### [Raschka 发布推理模型从零视频课](https://magazine.sebastianraschka.com/p/building-reasoning-models) ⭐️ 6.0/10

2026 年 10 月 24 日，Sebastian Raschka 发布免费的 11 小时《Build Reasoning Models from the Ground Up》视频课程，配套同名书籍，内容基于预训练 Qwen3 0.6B 模型，用 PyTorch 从零实现推理缩放、强化学习、蒸馏等核心推理模型技术。该课程是其 2025 年《Coding LLMs from the Ground Up》的续作，无需前置学习前作也可独立观看，前置要求为熟悉 Python 与 PyTorch，早期文本生成与评估示例可在 CPU 运行，后续训练环节需 GPU。课程聚焦底层 LLM 开发而非直接提供 agent harness、工具链或工作流的改进方案，对 coding agent 工程师的参考价值取决于是否需要从模型层优化 agent 推理能力。

rss · Sebastian Raschka · 10月24日 11:14

**「为什么重要」** 当前主流大语言模型多已支持推理模式，理解推理模型的底层实现是提升 agent 推理能力的基础路径；该课程提供可直接运行的 PyTorch 实现参考，但内容不涉及 agent 工具链与工作流优化，对 coding agent 工程师的实际价值需结合自身优化方向判断。

**「可关注」** 可关注：课程配套代码与书籍可对照学习，基于 Qwen3 0.6B 的推理模型实现全流程覆盖，早期评估环节无需 GPU 即可运行验证。

**标签**: `#coding-agent`, `#eval`, `#reasoning`

---

## AI 日报
{: #sec-ai-daily .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-daily" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-daily-1"></a>
### [谷歌开源 TorchTPU 一行代码跑 TPU](https://mp.weixin.qq.com/s?__biz=MzA3MzI4MjgzMw==&amp;mid=2651069794&amp;idx=2&amp;sn=ae62dbad6234b3c4c7359543936974c7) ⭐️ 5.5/10

2026 年 10 月 24 日，科技媒体机器之心报道谷歌在 PyTorch Conference 2026 上开源 TorchTPU，这是一套让 PyTorch 原生运行在 TPU 上的完整软件栈。报道称该栈已覆盖 4917 个模型、与 GPU 实现 97%算子对齐，由谷歌与 Meta 联合开发，vLLM、SGLang、Hugging Face 等主流开源项目已同步完成接入，相关 23 页技术报告已发布在 arXiv。需注意该声明暂无谷歌官方来源直接佐证，仅可作为行业信息记录。

rss · 机器之心 · 10月24日 04:30

**「为什么重要」** 这是 PyTorch 自 2016 年诞生以来首次将 TPU 列为与 GPU、CPU 并列的原生设备，打破了此前 PyTorch 跑 TPU 必须依赖 PyTorch/XLA、TorchAX 等转接层的局面，也是英伟达 CUDA 生态近十年遭遇的最直接挑战。过去一年 TPU 硬件已获得 Anthropic 最多 100 万颗、Meta 数十亿美元的订单，软件栈补齐将直接影响后续 AI 框架与芯片的生态选择。

**「可关注」** 可关注：TorchTPU 基于 PyTorch PrivateUse1 接口实现为原生 C++后端，模型迁移至 TPU 仅需修改设备指定参数，无需侵入式修改源码，且默认提供 Strict 等三档即时执行模式。

**标签**: `#model`, `#lab`, `#open-source`, `#industry`

---