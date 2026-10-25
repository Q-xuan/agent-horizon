---
layout: default
title: "Horizon Summary: 2026-10-25 (EN)"
date: 2026-10-25
lang: en
---

> From 145 items, 5 important content pieces were selected

---

**Agent Harness Architecture**
1. [MCP servers v2.1.0 安全修复发布](#item-harness-arch-1) ⭐️ 7.8/10
2. [pydantic-ai v2.61.0 发布](#item-harness-arch-2) ⭐️ 6.8/10
3. [security-audit-skill launch](#item-harness-arch-3) ⭐️ 6.0/10

**AI Agent Engineer**
1. [Sebastian Raschka 发布推理模型构建视频课程](#item-agent-engineer-1) ⭐️ 6.0/10

**AI Daily**
1. [谷歌开源TorchTPU TPU成PyTorch原生设备](#item-ai-daily-1) ⭐️ 5.5/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [MCP servers v2.1.0 安全修复发布](https://github.com/modelcontextprotocol/servers/releases/tag/v2.1.0) ⭐️ 7.8/10

Model Context Protocol 官方服务器仓库发布 v2.1.0，集中修复 8 个安全漏洞。\`@modelcontextprotocol/server-filesystem\` 升级至 2.0.1，堵住路径遍历、符号链接竞争条件、大小写绕过和目录列表信息泄露；\`@modelcontextprotocol/server-everything\` 同版本修复 HTTP/SSE 跨域请求风险；\`mcp-server-fetch\` 发布 2026.10.24，统一 IDNA 主机名校验、拒绝 NAT64 私有地址回绕、重定向后重新检查 robots.txt。TypeScript 服务器已切换语义版本，从日期版本升级需显式指定 2.0.1；Windows 平台 filesystem 写入边界仅部分修复，需参考 GHSA-53mr-w429-c597 配置规避。

github · cliffhall · Oct 25, 00:03

**「设计要点」** 三个服务器分别运行在 Node.js 和 Python 运行时，通过 MCP 协议向 agent harness 暴露工具接口。filesystem 服务器在 Linux/macOS 上将访问检查与写操作绑定防止符号链接竞争，everything 服务器在传输层强制 Origin 校验，fetch 服务器在地址分类层统一 IDNA 与 IPv4 映射检查。

**「改了什么」** TypeScript 服务器切换语义版本后，包管理器将 2.0.1 排于日期版本之后，需显式指定版本号安装。filesystem 服务器将路径检查与写操作绑定以消除竞争窗口，everything 服务器关闭跨域 wildcard，fetch 服务器统一主机名表示并扩展私有地址拒绝范围。

**Tags**: `#mcp`, `#tools`, `#permissions`, `#sandbox`

---

<a id="item-harness-arch-2"></a>
### [pydantic-ai v2.61.0 发布](https://github.com/pydantic/pydantic-ai/releases/tag/v2.61.0) ⭐️ 6.8/10

Official pydantic-ai v2.61.0 release ships runtime configuration tweaks, tool handling fixes, a breaking change for Cohere model tool returns, and google\_multi\_speaker deprecation. CohereModel tool returns containing files now raise NotImplementedError instead of being silently dropped, and provider-specific thinking settings that override broader thinking configs now emit warnings. The release adds async auth support to hosted MCP capabilities, structured citations to TextPart, and makes the durable engine extension surface public, while tightening InputGuardrail redaction and closing fail-open paths. Engineers using Cohere, Google Realtime, MCP, or citation features should review compatibility notes.

github · dsfaccini · Oct 24, 03:13

**「设计要点」** The release makes the durable engine extension API public, exposing operation types, ParameterTransports, and DurableRunContext for stateful agent run management. It also hardens capability authoring by sharing CapabilityStore locks per directory, allowing runs to cancel in-progress authoring, retaining the last valid authored capability on failed re-author, and making InputGuardrail redact user prompts while eliminating fail-open paths.

**「改了什么」** CohereModel tool returns with files now raise NotImplementedError instead of being silently dropped. The google\_multi\_speaker parameter on GoogleRealtimeModel is deprecated, provider-specific thinking overrides now trigger warnings, and hosted MCP capabilities accept async auth functions.

**Tags**: `#runtime`, `#tools`, `#subagents`

---

<a id="item-harness-arch-3"></a>
### [security-audit-skill launch](https://github.com/cloudflare/security-audit-skill) ⭐️ 6.0/10

Cloudflare open-sourced \`security-audit-skill\`, a coding-agent skill that turns agents into security auditors. It orchestrates isolated sub-agents through six phases: reconnaissance, coverage-led hunting, candidate validation, structured output, independent record verification, and target-neutral reporting. The skill outputs independently verified, machine-readable findings and seeded Cloudflare&\#x27;s internal vulnerability discovery harness described in &quot;Build your own vulnerability harness&quot;.

rss · GitHub Trending Daily · Oct 25, 00:44

**「Architecture Note」** The skill spawns sandboxed sub-agent proxies to execute distinct audit phases, isolating reconnaissance from validation to reduce false positives. It enforces structured output formats and independent record verification to maintain audit trail integrity across isolated execution contexts.

**「What Changed」** This initial open-source release exposes the multi-phase sub-agent orchestration pattern and sandbox integration that previously powered Cloudflare&\#x27;s internal vulnerability discovery harness.

**Tags**: `#tools`, `#subagents`, `#sandbox`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [Sebastian Raschka 发布推理模型构建视频课程](https://magazine.sebastianraschka.com/p/building-reasoning-models) ⭐️ 6.0/10

Sebastian Raschka 2026-10-24 发布 11 小时免费视频课程，配套同名书籍，用 PyTorch 从零实现推理模型。课程以 Qwen3 0.6B 为基座，覆盖评估、推理时缩放、强化学习、知识蒸馏与 KV 缓存。要求 Python 与 PyTorch 基础，后期实验需 GPU。内容聚焦底层 LLM 开发，不直接涉及 agent 工作流。

rss · Sebastian Raschka · Oct 24, 11:14

**「为什么重要」** 该课程提供从验证器到强化学习的全流程可运行代码，是理解推理模型内部机制的稀缺系统化资源。agent 工程师可通过掌握模型底层推理增强方式，优化 harness 层的上下文管理，但课程不覆盖工具链集成。

**「可关注」** 可关注：通过从零实现推理模型核心组件，可量化理解模型推理边界，进而更合理设定 agent 任务分解粒度与工具调用阈值。

**Tags**: `#coding-agent`, `#eval`, `#reasoning`

---

## AI Daily

<a id="item-ai-daily-1"></a>
### [谷歌开源TorchTPU TPU成PyTorch原生设备](https://mp.weixin.qq.com/s?__biz=MzA3MzI4MjgzMw==&amp;mid=2651069794&amp;idx=2&amp;sn=ae62dbad6234b3c4c7359543936974c7) ⭐️ 5.5/10

2026年PyTorch Conference上，科技媒体机器之心报道谷歌联合Meta开源TorchTPU完整软件栈，将TPU变为PyTorch原生设备，与GPU、CPU并列，并非PyTorch/XLA类的转接方案。报道称该栈已对齐4917个模型、97%的GPU算子，vLLM、SGLang、Hugging Face、Ray、TorchTitan等主流开源项目已完成接入，在Hugging Face Transformers v5中部署模型到TPU仅需传入device\_map=&quot;tpu&quot;参数。目前该声明暂无谷歌官方来源佐证，仅可作为行业信息记录。

rss · 机器之心 · Oct 24, 04:30

**「为什么重要」** PyTorch是全球使用最广泛的AI框架，此前长期与CUDA深度绑定，TPU此前仅能通过PyTorch/XLA等转接层支持PyTorch，用户需付出大量额外工程成本。过去一年Anthropic、Meta已签下大额TPU使用合约，硬件需求已验证，软件支持此前是TPU普及的最后短板，TorchTPU若落地将成为英伟达CUDA生态近十年来最正面的挑战。

**「可关注」** 可关注：TorchTPU基于PyTorch PrivateUse1接口注册为原生C++后端，项目已开源至google-pytorch/torch\_tpu仓库，配套23页技术报告发布在arXiv。

**Tags**: `#model`, `#lab`, `#open-source`, `#industry`

---