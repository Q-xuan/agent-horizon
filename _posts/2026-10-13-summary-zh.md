---
layout: default
title: "Horizon Summary: 2026-10-13 (ZH)"
date: 2026-10-13
lang: zh
---

> 从 191 条内容中筛选出 12 条重要资讯。

<nav id="ah-toc" class="ah-toc" aria-label="目录"><span class="ah-toc-title">目录</span><ul><li><a href="#sec-harness-arch"><span class="ah-toc-name">Harness 架构</span><span class="ah-toc-count">4条</span></a></li><li><a href="#sec-agent-engineer"><span class="ah-toc-name">Agent 工程师日报</span><span class="ah-toc-count">7条</span></a></li><li><a href="#sec-ai-daily"><span class="ah-toc-name">AI 日报</span><span class="ah-toc-count">1条</span></a></li></ul></nav>

---

**[Harness 架构](#sec-harness-arch)**
1. [OpenHands v1.27.0 发布](#item-harness-arch-1) ⭐️ 7.8/10
2. [LangGraph checkpoint 4.3.0 发布](#item-harness-arch-2) ⭐️ 6.8/10
3. [DSPy 3.4.1 发布](#item-harness-arch-3) ⭐️ 5.5/10
4. [Anthropic 开源知识工作插件库](#item-harness-arch-4) ⭐️ 5.5/10

**[Agent 工程师日报](#sec-agent-engineer)**
1. [Anthropic 验证小模型 IoT 自主复制风险](#item-agent-engineer-1) ⭐️ 7.8/10
2. [SoftwareGym 自动化合成 GUI 训练环境](#item-agent-engineer-2) ⭐️ 6.8/10
3. [Codex CLI 默认运行后台常驻进程引争议](#item-agent-engineer-3) ⭐️ 6.0/10
4. [ProgramGym 发布：长程程序复现训练框架](#item-agent-engineer-4) ⭐️ 6.0/10
5. [Work2Skill：从人类演示归纳 GUI 技能](#item-agent-engineer-5) ⭐️ 5.8/10
6. [Anthropic 借 Unix 哲学协调多 Agent](#item-agent-engineer-6) ⭐️ 5.5/10
7. [Decision 3.0 开源多模态决策模型家族](#item-agent-engineer-7) ⭐️ 5.5/10

**[AI 日报](#sec-ai-daily)**
1. [GitHub 发布代码库上下文配置指南](#item-ai-daily-1) ⭐️ 5.3/10

---

## Harness 架构
{: #sec-harness-arch .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-harness-arch" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-harness-arch-1"></a>
### [OpenHands v1.27.0 发布](https://github.com/OpenHands/OpenHands/releases/tag/v1.27.0) ⭐️ 7.8/10

OpenHands 发布 v1.27.0。运行时层引入 OpenCode 和 Pi 作为本地内置 ACP agent，模型列表改由 agent 动态提供。端到端验证工具新增浏览器视频录制与复杂按键控制，同时上线自动化任务草稿管理与 DigitalOcean 托管 agent 连接。

github · openhands-release-bot\[bot\] · 10月12日 15:06

**「设计要点」** ACP 集成改为运行时由子 agent 动态拉取模型元数据，避免中央硬编码；测试框架打通 mock-LLM 轨迹保留与浏览器视频录制，提升无真实 LLM 消耗下的复现与调试能力。

**「改了什么」** 以 ACP 协议内置接入 OpenCode 和 Pi，解耦硬编码模型列表；验证套件支持 \`browser record\` 录屏、按键状态保持（down/up/release-all）以及基于 DeepSeek 的 mock-LLM 行为映射；补齐自动化设置分屏与草稿持久化面板。

**标签**: `#subagents`, `#runtime`, `#eval`, `#tools`

---

<a id="item-harness-arch-2"></a>
### [LangGraph checkpoint 4.3.0 发布](https://github.com/langchain-ai/langgraph/releases/tag/checkpoint%3D%3D4.3.0) ⭐️ 6.8/10

LangGraph 发布子模块 checkpoint 4.3.0。该版本集中修复状态持久化与状态机回放的顺序问题，修正 delta channel 的执行拓扑重放，并强化反序列化失败与命名空间校验的容错能力。

github · github-actions\[bot\] · 10月12日 22:26

**「设计要点」** 运行时回放将 delta channel 强绑定至 task path 拓扑顺序，避免分支恢复时写操作乱序；反序列化故障降级为保留原始 payload，防止局部节点解析失败破坏整条持久化历史。

**「改了什么」** 按 task path 排序 delta channel 回放，恢复 exit-mode 运行时代写 delta 时按原始发生顺序重放；InMemorySaver 默认将增量历史对齐至最新 checkpoint。对象重建失败时保留底层序列化数据，并在分发至 SQLite/Postgres 前校验 Store 命名空间标签，放宽 Store.put 参数类型至 Mapping\[str, Any\]。

**标签**: `#runtime`, `#memory`, `#eval`

---

<a id="item-harness-arch-3"></a>
### [DSPy 3.4.1 发布](https://github.com/stanfordnlp/dspy/releases/tag/3.4.1) ⭐️ 5.5/10

DSPy 3.4.1 正式发布，核心变更在于默认启用基于 JSONAdapter 的结构化 InstructionProposer，并支持 dspy.RLM 在 REPL 运行时直接编写代码构建子 Agent。版本新增 Python 3.15 支持并修复导入与流式问题，同时要求 GEPA 的反思模型必须为能返回 JSON 的 dspy.LM 实例。此外，ReActV2 签名禁止声明名为 history 或 tools 的输入字段。

github · isaacbmiller · 10月12日 23:12

**「设计要点」** RLM 的子 Agent 运行在宿主环境，仅通过 JSON 跨越解释器边界交互；max\_llm\_calls 预算统一覆盖主循环、llm\_query 及所有子 Agent 消耗。沙箱内代码禁止修改 model、api\_key 与 api\_base 等配置，仅允许调整 temperature 等生成参数。

**「改了什么」** GEPA 提示词提议器从自由文本提取改为结构化输入和 JSON 解析，相同种子下的优化结果不再与 3.4.0 保持一致。dspy.RLM 提示词默认追加子 Agent 描述，并在解释器初始化时自动注入 shim 适配层，保留了 dspy 及 \_dspy 命名前缀。

**标签**: `#subagents`, `#runtime`, `#tools`

---

<a id="item-harness-arch-4"></a>
### [Anthropic 开源知识工作插件库](https://github.com/anthropics/knowledge-work-plugins) ⭐️ 5.5/10

Anthropic 开源插件仓库 anthropics/knowledge-work-plugins。该项目主要面向 Claude Cowork 设计，同时兼容 Claude Code。用户可通过插件配置角色行为偏好、定义外部工具与数据接入方式，并绑定专用工作流与斜杠命令。

rss · GitHub Trending Daily · 10月12日 23:18

**「设计要点」** 插件作为应用层配置包，统一定义角色规则、工具调度策略与斜杠命令交互，打通桌面协作环境 Cowork 与终端工程环境 Claude Code 的执行规范。

**标签**: `#tools`, `#runtime`, `#permissions`

---

## Agent 工程师日报
{: #sec-agent-engineer .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-agent-engineer" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-agent-engineer-1"></a>
### [Anthropic 验证小模型 IoT 自主复制风险](https://www.anthropic.com/research/self-replicating-ai) ⭐️ 7.8/10

Anthropic 前沿红队发布实验，展示小参数模型脱离数据中心在商用 IoT 设备上运行与传播的可能。团队将 Gemma4-26B-A4B 切分至 15 台杂牌 Android 电视盒，以流水线并行跑出 0.39 tokens/s。在陌生硬件环境配置测试中，Qwen3.5-9B 成功适配 9 种硬件中的 8 种；在简化评测中，GLM-5.2 及以上模型已能跑通扫描、提权、传输权重与部署推理的完整链路，≤30B 模型当前在长链路串联时仍会出错。

rss · Anthropic Research · 10月12日 00:00

**「为什么重要」** 实验证实边缘端廉价弱算力可通过分布式切片承载 26B 级别模型，打破了自主蠕虫 Agent 必然依赖中心化 GPU 集群的防御假设。缺少集中关停节点的去中心化载荷，显著抬高了后续排查与阻断的难度。

**「可关注」** 可关注：红队 harness Memento 应对长程任务死磕错误假设的做法——定期重置 Agent 进程，仅继承工作区和试错记录摘要，强迫新实例切换排错路径。

**标签**: `#eval`, `#permissions`, `#harness`, `#orchestration`

---

<a id="item-agent-engineer-2"></a>
### [SoftwareGym 自动化合成 GUI 训练环境](https://huggingface.co/papers/2610.12611) ⭐️ 6.8/10

针对计算机使用 Agent（CUA）缺乏多样化执行环境的问题，SoftwareGym 提出了一套自动化 GUI 软件合成流水线。该方案先生成结构各异的设计规范，再实现为可运行应用，并通过 GUI 运行时评估与迭代修复保证功能可靠。目前研究已借助该流程合成了 182 个应用环境，缓解了原生环境接入成本高与浏览器环境交互深度不足的限制。

rss · Hugging Face Daily Papers · 10月12日 00:00

**「为什么重要」** 人工构建原生桌面测试环境成本高昂且容易导致 Agent 过拟合单一应用。自动合成并修复可执行软件，能以更低成本扩展 Agent 训练和基准评测的多样性。

**「可关注」** 可关注：流水线将结构化代码实现与基于 GUI 运行表现的迭代修复结合，为构建动态评测沙箱提供了可落地的闭环验证思路。

**标签**: `#harness`, `#eval`, `#coding-agent`

---

<a id="item-agent-engineer-3"></a>
### [Codex CLI 默认运行后台常驻进程引争议](https://github.com/openai/codex/issues/48195) ⭐️ 6.0/10

社区反馈 Codex CLI 默认在系统后台安装并运行自动更新的常驻守护进程。使用者指出该机制会堆积旧版本文件，个别环境下占用约 12 GB 磁盘空间，且更新期间可能破坏文件权限，导致 \`.git\` 目录变为只读并中断任务。目前官方未在文档中明示关闭方式，但可在 \`~/.codex/config.toml\` 中配置 \`daemon\_auto\_start = false\` 临时禁用。

hackernews · whimblepop · 10月12日 18:29 · [社区讨论](https://news.ycombinator.com/item?id=50060694)

**「可关注：本地或容器环境若遇 Codex 磁盘暴涨或 Git 写入受阻，可在 \`~/.codex/config.toml\` 的 \`\[features\]\` 段显式关闭 \`daemon\_auto\_start\`。」** 本地或容器环境若遇 Codex 磁盘暴涨或 Git 写入受阻，可在 \`~/.codex/config.toml\` 的 \`\[features\]\` 段显式关闭 \`daemon\_auto\_start\`。

**「评论」** 多位工程师抱怨后台守护进程稳定性较差，偶发权限故障导致长时间运行的任务中断；部分开发者倾向采用仅依赖基础 Bash 工具的轻量 harness，避开过度设计的常驻进程。

**标签**: `#coding-agent`, `#harness`, `#permissions`

---

<a id="item-agent-engineer-4"></a>
### [ProgramGym 发布：长程程序复现训练框架](https://huggingface.co/papers/2610.13395) ⭐️ 6.0/10

论文提出面向长程程序复现任务的训练框架 ProgramGym，包含 Program-Env 与 Program-Agent 两部分。该方案针对从零构建软件的场景，由 Program-Env 从代码库构建可验证训练环境，要求智能体在实现前先探索参考程序、自主理清需求并决定系统设计。受限公开摘要在环境构建细节处截断，具体评测指标与基线对比仍待论文完整公开。

rss · Hugging Face Daily Papers · 10月12日 00:00

**「为什么重要」** 现有代码评测多集中在单仓库修复 issue 或按预设文档生成，缺乏让智能体在长周期内自主摸索参考实现、完成系统级复现的可验证训练环境。

**「可关注」** 可关注：Program-Env 如何把已有代码仓库自动转化为可量化验证的探索型环境，以及实现前探索机制对长程任务执行深度的影响。

**标签**: `#coding-agent`, `#harness`, `#eval`, `#orchestration`

---

<a id="item-agent-engineer-5"></a>
### [Work2Skill：从人类演示归纳 GUI 技能](https://huggingface.co/papers/2610.12984) ⭐️ 5.8/10

Work2Skill 提出一套捕获人类桌面 GUI 操作并归纳可复用技能的框架。系统通过组件 WorkRecorder 对齐屏幕录像、鼠标键盘事件及无障碍树信息，并据此构建了同步多模态演示数据集 WorkDemo-350。该框架旨在理解上下文操作，将工作流通用规则与特定任务细节分离，为 Computer-use agent 提取可复用经验。

rss · Hugging Face Daily Papers · 10月12日 00:00

**「为什么重要」** Computer-use agent 面临陌生专业软件的流程认知壁垒。把真实人类操作转化为抽象技能，避开了让模型单靠盲目试错探索界面的低效问题。

**「可关注」** 可关注：WorkRecorder 同步对齐录屏、底层输入事件与无障碍树（Accessibility Tree）的多模态采集思路，能为构建桌面操作轨迹数据集提供工程参考。

**标签**: `#memory`, `#harness`, `#eval`

---

<a id="item-agent-engineer-6"></a>
### [Anthropic 借 Unix 哲学协调多 Agent](https://www.latent.space/p/claude-dynamic-workflows) ⭐️ 5.5/10

Latent Space 报道，Anthropic 在 AI Engineer New York 峰会介绍了动态工作流（Dynamic Workflows）设计思路。团队借鉴 Unix 与 Linux 哲学协调 Claude 多智能体协作，旨在让智能体接管更大规模项目的同时，避免给开发者带来过重负担。该内容目前为峰会演讲概述，尚未公开一手工程实现细节或白皮书。

rss · Latent Space · 10月12日 18:18

**「为什么重要」** 复杂工程任务容易导致智能体编排失控，Anthropic 将经典操作系统的模块化与协作思想引入多智能体架构，为规模化任务治理提供了参考方向。

**「可关注」** 可关注：Anthropic 后续是否会公布该动态工作流的具体 harness 实现或开源规范，当前阶段仅有设计思路可供借鉴。

**标签**: `#orchestration`, `#harness`, `#coding-agent`

---

<a id="item-agent-engineer-7"></a>
### [Decision 3.0 开源多模态决策模型家族](https://www.reddit.com/r/LocalLLaMA/comments/1x3th4p/decision_30_open_multimodal_decision_models_from/) ⭐️ 5.5/10

vLLM Semantic Router 团队发布 Decision 3.0 模型家族，覆盖 0.6B 到 27B 参数，采用 Apache-2.0 协议开源。模型支持文本、图像与视频输入，完全跳过自回归文本生成，直接输出单选、是非与打分题型的概率分布。单次调用可对同一输入执行独立前向计算，批量输出多个问题的判定结果。作者自测称 27B 版本在 Jev 0.3 评测中取得文本 64.7 与视觉 71.6 分，未做视频微调但在 Perception Test 上取得 77.4 分零样本成绩。

reddit · r/LocalLLaMA · /u/henzy123 · 10月12日 05:26

**「为什么重要」** Agent 编排流以往多用通用多模态模型生成文本做意图识别和安全守卫，时延高且依赖正则解析。这类专用判别模型将多模态路由转为单步概率输出，能显著压缩编排节点的推理耗时与解析失败率。

**「可关注」** 可关注：其架构支持对同一输入并发评估多个问题且免去文本生成，适合替代 Agent 路由层中开销偏大的轻量 Vision-LLM 提示词分类器。

**标签**: `#orchestration`, `#eval`, `#harness`

---

## AI 日报
{: #sec-ai-daily .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-daily" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-daily-1"></a>
### [GitHub 发布代码库上下文配置指南](https://github.blog/ai-and-ml/github-copilot/github-copilot-app-for-beginners-how-to-teach-copilot-about-your-codebase/) ⭐️ 5.3/10

GitHub 博客发布入门指南，介绍如何让 GitHub Copilot 理解特定代码库。内容涵盖为仓库添加自定义指令与技能、使用自定义 agent，以及接入 Playwright 等 MCP 服务器扩展工具链。

rss · GitHub Blog · 10月12日 17:43

**「可关注」** 可关注：代码库级别的 agent 辅助正逐渐整合为自定义指令与 MCP 工具调用两条路径，规范仓库上下文输入。

**标签**: `#product`, `#industry`, `#open-source`

---