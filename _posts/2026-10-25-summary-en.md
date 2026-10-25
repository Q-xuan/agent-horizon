---
layout: default
title: "Horizon Summary: 2026-10-25 (EN)"
date: 2026-10-25
lang: en
---

> From 142 items, 7 important content pieces were selected

---

**Agent Harness Architecture**
1. [pydantic-ai v2.61.0 发布](#item-harness-arch-1) ⭐️ 7.8/10
2. [MCP Servers v2.1.0 安全补丁](#item-harness-arch-2) ⭐️ 6.8/10
3. [Cloudflare security-audit-skill 发布](#item-harness-arch-3) ⭐️ 5.0/10

**AI Agent Engineer**
1. [Battledrones v14 四人地图](#item-agent-engineer-1) ⭐️ 6.0/10
2. [Raschka 发布推理模型从零构建视频课](#item-agent-engineer-2) ⭐️ 6.0/10
3. [Kimi K3.1 Pro 发布 2.8T 开源权重](#item-agent-engineer-3) ⭐️ 5.5/10

**AI Daily**
1. [谷歌开源TorchTPU TPU成PyTorch原生设备](#item-ai-daily-1) ⭐️ 5.5/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [pydantic-ai v2.61.0 发布](https://github.com/pydantic/pydantic-ai/releases/tag/v2.61.0) ⭐️ 7.8/10

pydantic-ai v2.61.0 发布，修复运行时 thinking 配置作用域覆盖警告、Prefect 工作区并发运行隔离、CohereModel 工具返回文件处理、pydantic\_graph 布尔/整数 Literal 分支决策等核心问题。新增结构化引用、持久化引擎扩展公开 API、Kimi k3.1-pro 模型支持、RealtimeModelProfile.supports\_audio\_output 等能力。同步调整 MCP 托管能力异步 auth、CapabilityStore 创作检查、InputGuardrail 脱敏与故障开放路径、LocalStack 容器共享等兼容性行为。

github · dsfaccini · Oct 24, 03:13

**「改了什么」** 修复 thinking 配置作用域覆盖、Prefect 并发运行隔离、CohereModel 工具返回文件显式报错、pydantic\_graph Literal 分支决策、OpenRouter 流式 reasoning 缺失 details 等运行时问题。新增结构化引用、持久化引擎公开 API、Kimi k3.1-pro 模型、Realtime 音频输出支持，并调整 MCP 异步 auth、CapabilityStore 创作检查、InputGuardrail 脱敏等兼容性行为。

**Tags**: `#runtime`, `#tools`, `#planning`

---

<a id="item-harness-arch-2"></a>
### [MCP Servers v2.1.0 安全补丁](https://github.com/modelcontextprotocol/servers/releases/tag/v2.1.0) ⭐️ 6.8/10

modelcontextprotocol/servers 发布 v2.1.0 安全补丁，修复 filesystem、everything 和 fetch 三个服务器的 8 个漏洞。filesystem 服务器修复符号链接竞争条件、路径尾部空白剥离绕过、大小写不敏感卷上的符号链接检查绕过，以及目录遍历泄露文件元数据等问题，Windows 上仅部分修复。everything 服务器强制 HTTP/SSE 传输检查 Origin 头并拒绝跨域请求。fetch 服务器统一 IDNA 主机名检查与连接使用的名称，拒绝 NAT64 封装的私有 IPv4 地址，并在每次重定向后重新检查 robots.txt。

github · cliffhall · Oct 25, 00:03

**「改了什么」** filesystem 服务器将写入限制在已检查目录内并修复路径检查绕过；everything 服务器关闭 HTTP/SSE 传输跨域访问。fetch 服务器统一地址校验与连接主机名，拒绝 NAT64 私有地址并在重定向链中逐跳检查 robots.txt，从日期版本升级需显式安装 2.0.1。

**Tags**: `#security`, `#mcp`, `#sandbox`, `#tools`

---

<a id="item-harness-arch-3"></a>
### [Cloudflare security-audit-skill 发布](https://github.com/cloudflare/security-audit-skill) ⭐️ 5.0/10

Cloudflare released security-audit-skill, an open-source coding-agent skill that transforms an agent into a security auditor. It orchestrates isolated subagents through a six-phase workflow: reconnaissance, coverage-led hunting, candidate validation, structured output, independent record verification, and target-neutral reporting. The skill produces independently verified, machine-readable findings and seeded Cloudflare&\#x27;s vulnerability discovery harness, described in Build your own vulnerability harness. The source provides no implementation details, API specifications, or performance data.

rss · GitHub Trending Daily · Oct 25, 01:21

**Tags**: `#tools`, `#subagents`, `#sandbox`, `#eval`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [Battledrones v14 四人地图](https://simonwillison.net/2026/Oct/24/battledrones/) ⭐️ 6.0/10

Simon Willison 于 2026-10-24 发布 Battledrones v14，新增四人对战地图 &quot;Compass Rose&quot;。他使用单条 prompt 调用 Claude Opus 5.5，要求生成四向旋转对称地图并修改 WebSocket 非音频多人代码，将玩家上限从 2 人提升至 4 人（空位由 AI 填充）。地图采用寒冰 biome，新增紫、绿两队配色，玩家可通过分享链接或 QR 码加入对局。

rss · Simon Willison · Oct 24, 03:59

**「为什么重要」** 这是 Claude Opus 5.5 生成游戏地图并修改 WebSocket 多人代码的完整一手案例，包含实际使用的 prompt。对 coding agent 工程师而言，它提供了 agent 在游戏开发场景中端到端交付可运行特性的具体样本，但未提供性能数据或架构层面的深入分析。

**「可关注」** 可关注：单条高层 prompt 同时驱动了地图资源生成与 WebSocket 多人代码修改，说明当前 coding agent 已具备跨资源类型与网络层的端到端实现能力。

**Tags**: `#coding-agent`

---

<a id="item-agent-engineer-2"></a>
### [Raschka 发布推理模型从零构建视频课](https://magazine.sebastianraschka.com/p/building-reasoning-models) ⭐️ 6.0/10

Sebastian Raschka 于 2026-10-24 发布 11 小时免费视频课程，演示如何用 PyTorch 从零构建推理模型。课程以预训练 Qwen3 0.6B 为基线，覆盖评估、推理时缩放、强化学习与蒸馏，共 8 讲，配套同名书籍已由 Manning 和 Amazon 发售。前置要求仅需 Python 与 PyTorch 基础，早期文本生成与评估示例可在 CPU 运行，后续训练环节建议使用 GPU。

rss · Sebastian Raschka · Oct 24, 11:14

**「为什么重要」** 对需要理解推理模型内部机制以编码或调试 agent 的工程师，这套材料提供了可验证的代码级学习路径。但课程不涉及新的技术突破或工具链更新，阅读优先级取决于个人是否需要深入原理。

**「可关注」** 可关注：课程前两讲已展示 Qwen3 0.6B 加载、流式文本生成、KV 缓存与 torch.compile 的性能对比，第三讲实现数学答案验证器并在 MATH-500 上评估基座模型。

**Tags**: `#eval`, `#coding-agent`

---

<a id="item-agent-engineer-3"></a>
### [Kimi K3.1 Pro 发布 2.8T 开源权重](https://latent.space/p/ainews-kimi-31/) ⭐️ 5.5/10

Moonshot 于 2026-10-24 发布 Kimi K3.1 Pro，2.8T 总参数、104B 激活参数、1M 上下文窗口的混合专家模型，Artificial Analysis Intelligence Index 得分 55 排名第四，官方声称超过 Fable 5.1。配套 Pro Highspeed API 速度提升 2–3 倍但价格翻倍，并推出 Kimi Hosted Agents 托管执行环境。开源权重承诺 2026-11-04 发布，当前技术细节有限，代理能力提升最显著，部分交互任务仍落后。

rss · Latent Space · Oct 24, 07:18

**「为什么重要」** 这是少数公开声称达到 Fable 5.1 级别性能的开源权重模型，可能扩大代理工程师的基座模型选择。但推理经济性、交互任务稳定性及评测呈现方式存在争议，实际影响尚未证实。

**「可关注」** 可关注：K3.1 Pro 代理能力提升最显著，但 Highspeed API 两倍定价与部分交互任务落后提示需在速度、成本与任务适配性之间做权衡。

**Tags**: `#coding-agent`, `#eval`, `#api`

---

## AI Daily

<a id="item-ai-daily-1"></a>
### [谷歌开源TorchTPU TPU成PyTorch原生设备](https://mp.weixin.qq.com/s?__biz=MzA3MzI4MjgzMw==&amp;mid=2651069794&amp;idx=2&amp;sn=ae62dbad6234b3c4c7359543936974c7) ⭐️ 5.5/10

据机器之心2026年10月24日转载，谷歌在PyTorch Conference 2026上宣布开源TorchTPU，这是一套让TPU成为PyTorch原生设备的完整软件栈，核心改动是支持通过&quot;device\_map=\\&quot;tpu\\&quot;&quot;参数直接将模型部署到TPU，由谷歌与Meta联合开发，vLLM、SGLang、Hugging Face、Ray、TorchTitan等主流开源项目已同步完成接入，配套23页技术报告已发布在arXiv。该报道未附谷歌官方发布链接，内容存在截断，仅提及TorchTPU基于PyTorch PrivateUse1接口实现C++后端，迁移代码改动类似将&quot;.to\(\\&quot;cuda\\&quot;\)&quot;改为&quot;.to\(\\&quot;tpu\\&quot;\)&quot;，还提到4917个模型、97%对齐GPU的相关表述，无更多可核对的官方细节。

rss · 机器之心 · Oct 24, 04:30

**「为什么重要」** PyTorch是全球使用最广泛的AI框架，此前长期与CUDA深度绑定，PyTorch用户使用TPU需经过PyTorch/XLA等转接层付出额外工程成本。TorchTPU让TPU与GPU、CPU并列成为PyTorch原生选项，是CUDA生态近十年来遭遇的最直接挑战之一；同时过去一年Anthropic、Meta已签署大额TPU租用协议，软件短板补齐后可能加速TPU在PyTorch生态的落地。

**「可关注」** 可关注：TorchTPU基于PyTorch PrivateUse1接口实现原生C++后端，PyTorch用户迁移模型到TPU的代码改动接近仅修改设备指定参数，无需侵入式修改源码，且返回普通PyTorch张量无额外包装。

**Tags**: `#model`, `#lab`, `#open-source`, `#industry`

---