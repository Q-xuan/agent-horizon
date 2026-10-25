---
layout: default
title: "Horizon Summary: 2026-10-25 (ZH)"
date: 2026-10-25
lang: zh
---

> 从 142 条内容中筛选出 7 条重要资讯。

<nav id="ah-toc" class="ah-toc" aria-label="目录"><span class="ah-toc-title">目录</span><ul><li><a href="#sec-harness-arch"><span class="ah-toc-name">Harness 架构</span><span class="ah-toc-count">3条</span></a></li><li><a href="#sec-agent-engineer"><span class="ah-toc-name">Agent 工程师日报</span><span class="ah-toc-count">3条</span></a></li><li><a href="#sec-ai-daily"><span class="ah-toc-name">AI 日报</span><span class="ah-toc-count">1条</span></a></li></ul></nav>

---

**[Harness 架构](#sec-harness-arch)**
1. [pydantic-ai v2.61.0 发布](#item-harness-arch-1) ⭐️ 7.8/10
2. [MCP Servers v2.1.0 安全补丁发布](#item-harness-arch-2) ⭐️ 6.8/10
3. [Cloudflare 安全审计技能登 GitHub Trending](#item-harness-arch-3) ⭐️ 5.0/10

**[Agent 工程师日报](#sec-agent-engineer)**
1. [battledrones v14 新增四人对战地图](#item-agent-engineer-1) ⭐️ 6.0/10
2. [Raschka 发布 11 小时推理模型视频课](#item-agent-engineer-2) ⭐️ 6.0/10
3. [Kimi 3.1 Pro 2.8T 模型上线](#item-agent-engineer-3) ⭐️ 5.5/10

**[AI 日报](#sec-ai-daily)**
1. [谷歌开源 TorchTPU TPU 成 PyTorch 原生设备](#item-ai-daily-1) ⭐️ 5.5/10

---

## Harness 架构
{: #sec-harness-arch .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-harness-arch" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-harness-arch-1"></a>
### [pydantic-ai v2.61.0 发布](https://github.com/pydantic/pydantic-ai/releases/tag/v2.61.0) ⭐️ 7.8/10

这是 pydantic 官方发布的 pydantic-ai v2.61.0 版本，核心覆盖运行时、工具、规划组件的修复与兼容性调整，涉及 thinking 配置作用域、Prefect 工作区并发运行、CohereModel 工具返回处理、pydantic\_graph 分支判断逻辑等问题，同时补充了 MCP 能力、输入 guardrail、沙箱运行等组件的改进，无重大架构创新。

github · dsfaccini · 10月24日 03:13

**「设计要点」** 本次更新公开了持久化引擎扩展的操作类型、ParameterTransports、DurableRunContext 及运行身份钩子；CapabilityStore 锁按目录共享，LocalStack 容器在 \`async with agent:\` 上下文内单例复用，降低资源冲突概率。

**「改了什么」** 修复 thinking 配置被上层作用域覆盖时的告警缺失、Prefect 工作区并发运行归属错误、pydantic\_graph 中 bool/int 类型 Literal 分支混淆、CohereModel 工具返回文件被静默丢弃等运行时问题；新增异步 auth 函数支持、结构化引用归一化、kimi-k3.1 系列模型支持、Realtime 能力增强等特性。

**「评论」** 暂无社区评论内容。

**标签**: `#runtime`, `#tools`, `#planning`

---

<a id="item-harness-arch-2"></a>
### [MCP Servers v2.1.0 安全补丁发布](https://github.com/modelcontextprotocol/servers/releases/tag/v2.1.0) ⭐️ 6.8/10

modelcontextprotocol/servers 发布 v2.1.0 安全补丁，修复 filesystem、everything、fetch 三个服务器的 8 个漏洞。filesystem 服务器在 Linux 和 macOS 上修复符号链接竞争条件，确保写操作留在已检查目录内；Windows 上仅部分修复。同时修复路径尾随引号/空白绕过、大小写不敏感卷上的符号链接检查回归，以及目录列表中的符号链接信息泄露。everything 服务器为 HTTP 和 SSE 传输增加 Origin 头检查，禁止跨域调用。fetch 服务器统一 IDNA 主机名检查与连接使用的名称，拒绝 NAT64 地址中的私有/回环 IPv4 映射，并在每次重定向后重新检查 robots.txt。TypeScript 服务器已迁移到语义版本，日期版本需显式安装 2.0.1。

github · cliffhall · 10月25日 00:03

**「设计要点」** filesystem 服务器在访问检查与写操作之间保持路径一致性，防止父目录被替换为符号链接导致的目录遍历。everything 服务器在传输层强制同源策略，fetch 服务器在网络层统一地址解析与连接验证。

**「改了什么」** 修复 filesystem 服务器的符号链接竞争条件、路径规范化绕过和目录列表信息泄露。修复 everything 服务器的跨域请求伪造漏洞。修复 fetch 服务器的 IDNA 主机名不一致、NAT64 私有地址绕过和 robots.txt 重定向绕过。

**标签**: `#security`, `#mcp`, `#sandbox`, `#tools`

---

<a id="item-harness-arch-3"></a>
### [Cloudflare 安全审计技能登 GitHub Trending](https://github.com/cloudflare/security-audit-skill) ⭐️ 5.0/10

这是 Cloudflare 开源的 coding-agent 安全审计技能，2026 年 10 月 25 日登上 GitHub Trending。该技能可将普通 agent 转化为安全审计员，通过多阶段流程编排隔离子代理，输出机器可读、经独立验证的安全发现，同时也是 Cloudflare 漏洞发现 harness 的初始基础，相关设计在《Build your own vulnerability harness》一文中有描述。当前公开源未披露具体技术实现细节。

rss · GitHub Trending Daily · 10月25日 01:21

**标签**: `#tools`, `#subagents`, `#sandbox`, `#eval`

---

## Agent 工程师日报
{: #sec-agent-engineer .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-agent-engineer" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-agent-engineer-1"></a>
### [battledrones v14 新增四人对战地图](https://simonwillison.net/2026/Oct/24/battledrones/) ⭐️ 6.0/10

2026 年 10 月 24 日，Simon Willison 发布 battledrones v14，新增名为 Compass Rose 的四人对战地图，此前版本地图仅支持双人对战。该地图由 Claude Opus 5.5 根据指定 prompt 生成，同时修改了 WebSocket 非音频多人模式代码，支持最多 4 名人类玩家加入，空位自动填充 AI。新增紫、绿两队机器人，加入原有蓝、红队伍，官方提供了四路 AI 对战回放链接。

rss · Simon Willison · 10月24日 03:59

**「为什么重要」** 这是公开可查的 coding agent 游戏开发实践案例，附带了实际使用的 prompt 与修改后的多人代码，可作为 coding agent 在游戏场景落地的参考；但目前无性能数据或架构层面的深度分析，无法评估其方案的通用性。

**「可关注」** 可关注：Claude Opus 5.5 已能直接生成游戏地图并修改 WebSocket 多人对战代码，支持扩展玩家数量。

**标签**: `#coding-agent`

---

<a id="item-agent-engineer-2"></a>
### [Raschka 发布 11 小时推理模型视频课](https://magazine.sebastianraschka.com/p/building-reasoning-models) ⭐️ 6.0/10

2026 年 10 月 24 日，AI 实践者 Sebastian Raschka 发布 11 小时免费视频课程，配套其《Build a Reasoning Model \(From Scratch\)》书籍，教授用 PyTorch 从预训练 Qwen3 0.6B 模型起步，从零实现推理模型的评估、推理缩放、强化学习、蒸馏全流程，包含数学答案验证器实现与 MATH-500 数据集评估。课程共 8 讲，为去年《Coding LLMs from the Ground Up》的续作，无需学习前作即可观看，仅需 Python 和 PyTorch 基础，早期文本生成与评估示例可在 CPU 运行，后续训练环节需 GPU 支持，配套书籍由 Manning 和 Amazon 发行，印刷版为全彩。另提供 90 分钟的 LinkedIn Learning 概念概览课，通过对应链接可免费访问 24 小时。该资源面向希望深入理解推理模型原理、构建 coding agent 的工程师，不属于新工具链更新或技术突破。

rss · Sebastian Raschka · 10月24日 11:14

**「为什么重要」** 该课程是目前少有的从代码层面完整拆解推理模型构建流程的免费实践资源，可帮助 coding agent 工程师厘清推理模型与 agent harness 的边界与协作关系。但课程属于教育类内容，并非新的技术突破或工具更新，对急需跟进最新研究进展的工程师优先级不高。

**「可关注」** 可关注：课程以预训练 Qwen3 0.6B 为基座，完整演示推理模型评估、推理缩放、强化学习与蒸馏的 PyTorch 实现，可作为理解推理模型内部机制的实践参考，无需提前掌握 LLM 从零训练知识。

**标签**: `#eval`, `#coding-agent`

---

<a id="item-agent-engineer-3"></a>
### [Kimi 3.1 Pro 2.8T 模型上线](https://latent.space/p/ainews-kimi-31/) ⭐️ 5.5/10

2026 年 10 月 24 日 Latent Space 的 AI 新闻汇总报道 Moonshot 发布 Kimi K3.1 Pro 模型：该模型为 2.8T 总参数、104B 激活参数的混合专家模型，上下文窗口 1M token，官方宣称支持全项目编码、Blender/CAD 工作、金融建模与长运行代理任务。第三方独立测试显示，其在 Artificial Analysis Intelligence Index 中排第四、得分 55，Arena Code Arena: WebDev 排第 8、得分 1692，Artificial Analysis Cyber Index 得分 64%为公开可访问结果最高。同期上线 Pro Highspeed API，官方称推理速度提升 2-3 倍、价格为标准版 2 倍，还推出 Kimi Hosted Agents 托管代理服务，支持 24/7 长任务执行与多代理协作。2.8T 开放权重版本承诺于 2026 年 11 月 4 日发布，本次报道为二手新闻汇总，未披露过多技术细节。

rss · Latent Space · 10月24日 07:18

**「为什么重要」** 若 11 月 4 日开放权重版本如期发布，Kimi 3.1 Pro 将成为首个达到 Fable 5.1 级性能的开放权重模型候选，可将闭源前沿模型的领先窗口缩小至约 1 个月；其代理、编码、网络安全类任务的第三方基准表现，以及高速 API、托管代理服务的推出，对 coding agent 与代理 harness 工程师有直接参考价值。需注意当前性能数据均为第三方测试结果，开放权重版本尚未正式发布。

**「可关注」** 可关注：Kimi 3.1 Pro 在代理、编码、网络安全类基准的第三方测试表现，以及 11 月 4 日开放权重版本的实际发布情况、高速 API 的实际吞吐与推理成本表现。

**标签**: `#coding-agent`, `#eval`, `#api`

---

## AI 日报
{: #sec-ai-daily .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-daily" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-daily-1"></a>
### [谷歌开源 TorchTPU TPU 成 PyTorch 原生设备](https://mp.weixin.qq.com/s?__biz=MzA3MzI4MjgzMw==&amp;mid=2651069794&amp;idx=2&amp;sn=ae62dbad6234b3c4c7359543936974c7) ⭐️ 5.5/10

2026 年 10 月 24 日 PyTorch Conference 2026 上，谷歌宣布开源 TorchTPU 完整软件栈，旨在让 TPU 成为 PyTorch 原生设备，与 GPU、CPU 并列。该转载内容提及 TorchTPU 已对齐 4917 个模型、97%的 GPU 算子，由谷歌与 Meta 联合开发，vLLM、SGLang、Hugging Face、Ray、TorchTitan 等主流开源项目已同步接入，配套 23 页技术报告发布在 arXiv。但该信息为机器之心的二手转载，未附谷歌官方发布链接，内容存在截断，相关细节无法核验。

rss · 机器之心 · 10月24日 04:30

**「为什么重要」** PyTorch 是全球使用最广泛的 AI 框架，自 2016 年诞生起长期与 CUDA 深度绑定，此前 TPU 接入 PyTorch 需经过 PyTorch/XLA 等转接层，付出大量额外工程成本。若 TorchTPU 落地，将首次让 TPU 成为 PyTorch 原生选项，打破 CUDA 的生态垄断，也补上谷歌 TPU 软件栈的短板。

**「可关注」** 可关注：TorchTPU 基于 PyTorch PrivateUse1 接口注册为 C++后端，开发者将设备从 GPU 迁移到 TPU 仅需修改设备指定参数，无需调整模型逻辑。

**标签**: `#model`, `#lab`, `#open-source`, `#industry`

---