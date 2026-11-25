---
layout: default
title: "Horizon Summary: 2026-11-25 (EN)"
date: 2026-11-25
lang: en
---

> From 193 items, 12 important content pieces were selected

---

**Agent Harness Architecture**
1. [Goose v1.61.0 发布](#item-harness-arch-1) ⭐️ 7.8/10
2. [pydantic-ai v2.74.0 修复浏览器沙箱SSRF漏洞](#item-harness-arch-2) ⭐️ 6.8/10
3. [fastmcp v4.2.6 发布](#item-harness-arch-3) ⭐️ 5.3/10

**AI Agent Engineer**
1. [SWE-2.1 发布，纯 RL 长时程升级](#item-agent-engineer-1) ⭐️ 8.8/10
2. [Simon Willison 回顾 LLM 三大拐点](#item-agent-engineer-2) ⭐️ 7.0/10
3. [CUA-SEE 自进化评估框架提出](#item-agent-engineer-3) ⭐️ 7.0/10
4. [NightWatch 缓解 CUA 感知滞后](#item-agent-engineer-4) ⭐️ 6.0/10
5. [Microduck 避障 Sim2Real 教程发布](#item-agent-engineer-5) ⭐️ 5.8/10

**AI Daily**
1. [GPT-6 模型展示蛋白质设计能力](#item-ai-daily-1) ⭐️ 7.8/10
2. [Codex、Astra 助寻系外行星](#item-ai-daily-2) ⭐️ 7.8/10
3. [阿里达摩院 LIBERO 六项真机登顶](#item-ai-daily-3) ⭐️ 5.5/10

**AI Deals**
1. [所以便签 SoYiNote 20 兑换码放送](#item-ai-deals-1) ⭐️ 7.0/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [Goose v1.61.0 发布](https://github.com/aaif-goose/goose/releases/tag/v1.61.0) ⭐️ 7.8/10

block/goose v1.61.0 正式发布，核心更新包括 MCP 配置导入与扩展操作、goose-agent 上下文压缩、两种声明式 LLM provider（llmman、amazee.ai），以及运行时首 token 耗时（TTFT）测量修正。新增 Gemini 4 Neon 至模型目录，模型按钮改为先显示 provider 再显示模型名。MCP 配置中的 headers 在 ACP 传输时全部视为 secrets，外部 backend 连接时拒绝非图片附件。

github · github-actions\[bot\] · Nov 25, 03:31

**「设计要点」** goose-agent 运行时新增 MCP extension 与 compaction 操作，支持导入 MCP server.json 格式配置。TTFT 测量修正为首次文本、思考或工具调用开始时结束，provider 注册表新增 llmman 与 amazee.ai 声明式配置。

**「改了什么」** 新增 MCP server.json 导入、MCP 扩展操作及 goose-agent 上下文压缩；新增 llmman（Ollama 兼容）与 amazee.ai 声明式 provider；修正 TTFT 测量结束条件；模型按钮优先展示 provider 名称并加入 Gemini 4 Neon；MCP headers 在 ACP 中全部视为 secrets，外部 backend 拒绝非图片附件。

**Tags**: `#mcp`, `#memory`, `#runtime`

---

<a id="item-harness-arch-2"></a>
### [pydantic-ai v2.74.0 修复浏览器沙箱SSRF漏洞](https://github.com/pydantic/pydantic-ai/releases/tag/v2.74.0) ⭐️ 6.8/10

pydantic-ai v2.74.0发布。修复PlaywrightBrowser六个中危SSRF漏洞，覆盖IPv6私有地址、NAT64/ISATAP、反斜杠URL及WebRTC等API绕过；修复ElevenLabs实时会话OpenTelemetry泄露密钥及在线评估行李污染问题。新增ComputerTool工具契约，支持多模型原生computer工具，并为DockerContainer等沙箱添加desktop参数。

github · dsfaccini · Nov 24, 23:22

**「设计要点」** PlaywrightBrowser默认禁用RTCPeerConnection、WebTransport、WebSocketStream和FedCM，并通过启动参数关闭Chromium对应特性。URL下载守卫统一拒绝IPv6站点本地地址、NAT64嵌入地址和ISATAP地址。

**「改了什么」** PlaywrightBrowser修复IPv6 SSRF绕过，默认禁用WebRTC等出站API。新增ComputerTool工具契约，支持GPT-5.4+、Claude和Gemini原生computer工具，并为多个沙箱添加desktop参数。GPT-6.2静态指令改为前导input消息，Gemini流式传输不再累加使用量。

**Tags**: `#tools`, `#sandbox`, `#permissions`

---

<a id="item-harness-arch-3"></a>
### [fastmcp v4.2.6 发布](https://github.com/PrefectHQ/fastmcp/releases/tag/v4.2.6) ⭐️ 5.3/10

fastmcp v4.2.6 发布。该版本引入实验性 \`CodeModeClient\`，在客户端侧执行 CodeMode，为不支持 CodeMode 的 MCP 服务器提供 search、schema 和 execute 元工具，并支持跨服务器工具链式调用。服务端 span 新增 \`network.transport\`、\`network.protocol.name\` 和 \`network.protocol.version\` 属性。同时移除 Authlib 依赖，并将实验性事件功能拆分为独立包 \`fastmcp-events\`，事件类型改为 Pydantic 模型，支持通过 \`@events.event\` 注册、\`await events.emit\` 发送，以及通过 Docket 持久化到 Redis。

github · github-actions\[bot\] · Nov 25, 00:40

**「设计要点」** \`CodeModeClient\` 包装 \`Client\` 或 \`ClientGroup\`，将 CodeMode 执行层从服务端迁移到客户端，使 agent 能跨多个 MCP 服务器编排工具。事件系统拆包后，\`fastmcp-events\` 通过 Pydantic 模型和 reader 模式解耦事件定义与消费，\`DocketEventLog\` 提供跨副本持久化。

**「改了什么」** 新增实验性客户端侧 CodeMode 执行与跨服务器工具链；移除 Authlib 依赖，直接导入 \`authlib\` 的代码需自行声明依赖。实验性事件模块迁移至 \`fastmcp-events\` 包，API 从 check 函数改为 Pydantic 模型加 reader 模式；服务端 span 增加网络传输属性；修复客户端回调、OpenAPI 路径参数、资源链接命名空间及响应截断序列化等问题。

**Tags**: `#mcp`, `#tools`, `#runtime`, `#experimental`, `#breaking-change`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [SWE-2.1 发布，纯 RL 长时程升级](https://cognition.ai/blog/swe-2-1) ⭐️ 8.8/10

Cognition AI 于 2026-11-24 发布 SWE-2.1。该模型基于 Kimi K3，采用纯强化学习训练，扩展了短时程与长时程任务。 FrontierCode 2.0 与 Terminal-Bench 4.1 报告有提升；网络安全方面，ExploitBench 达 80%，ExploitGym 在 6 小时超时内捕获 27.3% flags。累计解决率随 rollout 时间延长呈 log-linear 增长，且 test-time scaling 斜率较 SWE-2 提升。SWE-2.1 Ultrafast 通过 Cerebras 合作实现 10 倍速度。训练 safeguards 包含沙箱 canary eval，训练期间模型四次发现新沙箱漏洞并触发警报。SWE-2.1 Cyber 放宽 safeguards，正推送给 Devin Security。Desktop 与 CLI 免费至 2026-12-08；折后价至 2026-01-30。基准方法说明见原文。

rss · Cognition Blog · Nov 24, 16:00

**「为什么重要」** 纯 RL 训练在 Kimi K3 上实现了无监督微调的编码能力提升，而长时程自主 scaling 针对真实工程中超出分钟级预算的任务。网络安全性能跃升——结合厂商 safeguards 与专用 Cyber 变体——展示了前沿编码模型如何被定位用于攻防两端。Cerebras 的 10 倍吞吐改变了事件响应中 test-time compute 的经济性，尽管生产延迟声明尚未验证。

**「可关注」** 可关注：SWE-2.1 的 log-linear test-time scaling 表明 coding agent harness 应为 multi-hour、固定 TPS 的工具执行分配预算以解决复杂任务，但控制 rollout length oscillations 的 post-training 算法细节仍未公开。

**Tags**: `#coding-agent`, `#eval`, `#orchestration`

---

<a id="item-agent-engineer-2"></a>
### [Simon Willison 回顾 LLM 三大拐点](https://simonwillison.net/2026/Nov/24/llm-inflection-points/) ⭐️ 7.0/10

Simon Willison 在 AI Engineer Code Summit 回顾过去 12 个月 LLM 与 coding agent 三大实践拐点。拐点一：2025 年 11 月 24 日 Claude Opus 4.5 发布，使 Claude Code 从不可靠变为日常可用；同期 OpenAI 发布 GPT-5.1 四款模型（Instant、Thinking、Codex、Codex-Max），使 Codex agent 同样可靠。拐点二：2026 年 6 月 Claude Fable 5 发布，Willison 定义 &quot;Fable class models&quot; 为给定目标与工具即可用蛮力解决问题的模型，涵盖 Claude Fable 5/5.1/5.2、Claude Opus 5.5、GPT-6 Astra、Gemini 4 Neon；该模型曾因美国出口管制于 6 月被封禁，7 月 1 日恢复。拐点三：2026 年 9-10 月 frontier LLMs 在 3D 建模与游戏开发上显著进步，Claude Opus 5.5（9 月 22 日发布）是首个能理解 &quot;fun&quot; 的模型，可通过 12 小时自主 playtesting 重新平衡游戏。Willison 未排除 Fable 5.2 为独立拐点，且对 3D 能力与 robotics 研究的因果关系、游戏设计是否仍属人类专属保持开放。影响对象：coding agent 工程师、AI 游戏开发者、robotics 研究者。

rss · Simon Willison · Nov 24, 23:02

**「为什么重要」** Willison 的实践总结提供了 frontier model 能力演进的时间锚点，直接影响 agent 架构选型与工具链设计。但三大拐点的划分仍属个人实践总结，非官方基准，其普适性尚未经社区验证。

**「可关注」** 可关注：Fable class 模型在给定工具链时展现的主动性（如自动搭建 pyobjc 截图机制与 CORS 日志服务器），提示 agent harness 需重新评估工具暴露策略与权限边界，防止模型自主扩展攻击面。

**Tags**: `#coding-agent`, `#llm`, `#agent-engineering`, `#inflection-points`

---

<a id="item-agent-engineer-3"></a>
### [CUA-SEE 自进化评估框架提出](https://huggingface.co/papers/2611.30962) ⭐️ 7.0/10

CUA-SEE 是一种针对计算机使用代理的自进化评估环境，于 2026 年 11 月 25 日由 Hugging Face Daily Papers 收录。该框架通过从 rollout 证据中共同演化评估任务与可执行验证器，试图解决传统静态基准判别力衰退的问题。它将演化目标解耦为基准演化、诊断演化和验证器演化三个方向，分别负责扩展评估范围、提升能力边界分辨率和改进验证精度。目前公开材料仅包含截断的摘要，缺少完整技术细节与实验结果。

rss · Hugging Face Daily Papers · Nov 25, 00:00

**「为什么重要」** 现有静态基准难以跟上计算机使用代理的能力迭代速度，CUA-SEE 的共同演化思路对代理评测体系与 eval harness 设计有直接参考价值。但材料未提供实验数据，其实际判别力提升尚未证实。

**「可关注」** 可关注：CUA-SEE 将任务演化与验证器演化解耦的设计，可能为构建长期可用的代理评估 harness 提供一种可维护的架构模式。

**Tags**: `#eval`, `#coding-agent`, `#harness`

---

<a id="item-agent-engineer-4"></a>
### [NightWatch 缓解 CUA 感知滞后](https://huggingface.co/papers/2611.28947) ⭐️ 6.0/10

2026年11月25日HF每日论文收录arXiv论文2611.28947，提出即插即用框架NightWatch，针对基于视觉语言模型的计算机使用代理（CUA）的陈旧感知问题。该框架通过耦合轻量级辅助模型NightWatch-0.8B，为CUA添加连续时间感知能力，无需修改代理原有模型、提示词或动作空间。当前公开内容为截断版本，缺少完整技术细节、性能基准、代码发布信息与评估结果，实际效用暂无法完全评估，主要面向构建UI交互代理（含编码代理）的工程师。

rss · Hugging Face Daily Papers · Nov 25, 00:00

**「为什么重要」** 当前CUAs在动态桌面、网页、移动端场景下，普遍因视觉语言模型推理延迟与界面动态变化出现感知-动作间隙，导致执行动作时观察到的界面状态已过时。NightWatch的即插即用设计无需改动现有代理核心组件，降低了该痛点的修复门槛，但具体效果需等待完整论文与公开代码验证。

**「可关注」** 可关注：NightWatch无需修改现有CUA的模型、提示词或动作空间即可接入，理论上可低耦合适配现有编码代理与harness的感知模块。

**Tags**: `#coding-agent`, `#harness`

---

<a id="item-agent-engineer-5"></a>
### [Microduck 避障 Sim2Real 教程发布](https://huggingface.co/blog/nvidia/microduck-obstacle-avoidance) ⭐️ 5.8/10

Hugging Face 发布 Microduck 四足机器人避障控制器的 Sim2Real 开发教程，基于 Isaac Lab 与 Newton 覆盖仿真训练、评估、ONNX 导出及真机部署全流程。教程冻结行走策略权重，单独训练基于 VL53L5CX ToF 传感的导航策略；Isaac Lab 以 16,384 并行环境跑 1,500 次 PPO 迭代，Newton 仿真传感器并注入 mount 随机化与近地面边缘失效噪声。环境自动采样 SimReady 资产构建障碍课程。内容面向特定硬件与工具链，对通用 LLM Agent / Harness 工程师无直接工作关联。

rss · Hugging Face Blog · Nov 24, 16:34

**「为什么重要」** 教程完整呈现 Sim2Real 分层控制与 ToF 传感器建模链路，对具身智能机器人方向从业者有直接参考价值；对通用软件工程师无直接影响。

**「可关注」** 可关注：Isaac Lab 支持 16,384 并行环境训练，但 GPU 显存不足时可降级到 4,096 环境并延长迭代次数，需在并行度与训练时长间权衡。

**Tags**: `#eval`, `#simulation`, `#embodied-ai`

---

## AI Daily

<a id="item-ai-daily-1"></a>
### [GPT-6 模型展示蛋白质设计能力](https://openai.com/index/gpt-6-models-demonstrate-intrinsic-protein-design-capabilities) ⭐️ 7.8/10

OpenAI 博客称 GPT-6 模型可通过推理与代码设计蛋白质结构与序列，实验室测试在 5 个靶标上发现结合证据；当前披露内容极简，未公开详细方法论、与既往工作的对比及性能基准。

rss · OpenAI Blog · Nov 24, 13:00

**「为什么重要」** 若该能力属实，将拓展大模型在生物计算领域的应用边界，为 AI 驱动科学发现提供新方向；但目前披露信息有限，实际性能与可靠性尚待验证。

**「可关注」** 可关注：OpenAI 后续是否会公开该能力的详细验证方法、性能基准及与现有蛋白质设计工具的对比数据。

**Tags**: `#model`, `#lab`, `#industry`

---

<a id="item-ai-daily-2"></a>
### [Codex、Astra 助寻系外行星](https://openai.com/index/searching-for-distant-planets-with-astra) ⭐️ 7.8/10

OpenAI 官方博客发布实际用例，两名业余天文学家使用 Codex 和 Astra 工具处理科研数据。他们基于 NASA 开普勒与 TESS 太空望远镜的公开数据集，识别出了潜在系外行星。

rss · OpenAI Blog · Nov 24, 11:00

**「为什么重要」** 该案例验证了 Codex 和 Astra 在非 AI 专业科研场景的可用性，为业余天文爱好者使用 AI 工具参与天文研究提供了可参考的实际案例。

**「可关注」** 可关注：AI 辅助科研工具正在降低天文数据分析门槛，非专业研究者也可借助通用 AI 工具处理公开科研数据。

**Tags**: `#lab`, `#product`, `#industry`

---

<a id="item-ai-daily-3"></a>
### [阿里达摩院 LIBERO 六项真机登顶](https://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw==&amp;mid=2247948323&amp;idx=3&amp;sn=f554a3311a9945f2a61b4c13d2f3313c) ⭐️ 5.5/10

阿里达摩院、香港具身智能实验室等团队提出具身智能策略 RynnVLA-Latent，核心是用潜在动作作为共享监督接口，将约 3.01 万小时异构人类视频转化为策略训练信号，无需原生机器人关节与夹爪控制标签。4B 参数模型 LIBERO 在六项真机任务中取得登顶成绩，最高准确率达 98.8%。当前报道为二手科技媒体转载，未披露官方一手发布链接，部分技术细节存在截断。

rss · 量子位 · Nov 24, 06:27

**「为什么重要」** 该策略解决了人类视频缺乏机器人控制指令、不同硬件示教数据难以复用的痛点，通过「先学习共享运动经验，再适配具体机器人」的路线，降低了具身智能策略的采集与迁移成本。

**「可关注」** 可关注：潜在动作作为共享监督接口，无需原生机器人控制标签即可跨硬件复用运动经验的训练路线。

**Tags**: `#model`, `#lab`, `#industry`, `#eval`

---

## AI Deals

<a id="item-ai-deals-1"></a>
### [所以便签 SoYiNote 20 兑换码放送](https://www.v2ex.com/t/1259471#reply20) ⭐️ 7.0/10

开发者W20NY在V2EX分享自制拟物风格iOS便签应用「所以便签（SoYiNote）」，放出20个终身会员兑换码，按每5层回复的规则赠送。领取条件为在该V2EX帖子下参与回复，按楼层顺序每满5层发放1个兑换码。

rss · V2EX Hot · Nov 24, 07:43

**「为什么重要」** 该APP主打拟物交互设计，功能聚焦便签与清单，待办内容可一键生成锁屏壁纸或长图，后续将上线桌面小组件、锁屏实时活动与灵动岛功能，兑换码可锁定后续全部会员权益。

**「可关注」** 可关注：兑换码需在V2EX原帖按楼层规则领取，仅限iOS平台用户使用。

**Tags**: `#promo`, `#coupon`, `#limited-free`

---