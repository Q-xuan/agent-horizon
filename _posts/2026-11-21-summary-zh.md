---
layout: default
title: "Horizon Summary: 2026-11-21 (ZH)"
date: 2026-11-21
lang: zh
---

> 从 170 条内容中筛选出 14 条重要资讯。

<nav id="ah-toc" class="ah-toc" aria-label="目录"><span class="ah-toc-title">目录</span><ul><li><a href="#sec-harness-arch"><span class="ah-toc-name">Harness 架构</span><span class="ah-toc-count">3条</span></a></li><li><a href="#sec-agent-engineer"><span class="ah-toc-name">Agent 工程师日报</span><span class="ah-toc-count">7条</span></a></li><li><a href="#sec-ai-daily"><span class="ah-toc-name">AI 日报</span><span class="ah-toc-count">1条</span></a></li><li><a href="#sec-ai-deals"><span class="ah-toc-name">AI 羊毛</span><span class="ah-toc-count">3条</span></a></li></ul></nav>

---

**[Harness 架构](#sec-harness-arch)**
1. [cloudflare/agents 0.34.0 发布](#item-harness-arch-1) ⭐️ 8.8/10
2. [Agents SDK v1.0.0a1 发布](#item-harness-arch-2) ⭐️ 7.8/10
3. [Claude Code v2.1.330 发布](#item-harness-arch-3) ⭐️ 5.5/10

**[Agent 工程师日报](#sec-agent-engineer)**
1. [Inkling 2 Mini 循环 Transformer 开源](#item-agent-engineer-1) ⭐️ 8.0/10
2. [AltRA-Test 提出稀疏标注场景 LLM 替代检验方法](#item-agent-engineer-2) ⭐️ 7.0/10
3. [arXiv 预印本称模型可自改权重](#item-agent-engineer-3) ⭐️ 6.0/10
4. [TuringSpace 空间智能基准发布](#item-agent-engineer-4) ⭐️ 6.0/10
5. [HF 每日论文 扩散 Transformer 激活转向替代 RL 后训练](#item-agent-engineer-5) ⭐️ 6.0/10
6. [Fragments 11·20：AI 审查成本差](#item-agent-engineer-6) ⭐️ 6.0/10
7. [ZeroVLN 免 SFT 的 VLM 导航框架](#item-agent-engineer-7) ⭐️ 5.5/10

**[AI 日报](#sec-ai-daily)**
1. [OpenAI 公布对抗性蒸馏防御方案](#item-ai-daily-1) ⭐️ 6.8/10

**[AI 羊毛](#sec-ai-deals)**
1. [Epic 11.20~26 限免两款游戏](#item-ai-deals-1) ⭐️ 8.0/10
2. [波波小红书获客助手 30 天版送码](#item-ai-deals-2) ⭐️ 8.0/10
3. [Ferry 免费 iOS Mac 远程桌面](#item-ai-deals-3) ⭐️ 8.0/10

---

## Harness 架构
{: #sec-harness-arch .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-harness-arch" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-harness-arch-1"></a>
### [cloudflare/agents 0.34.0 发布](https://github.com/cloudflare/agents/releases/tag/agents%400.34.0) ⭐️ 8.8/10

cloudflare/agents 0.34.0 发布，核心升级至 Pi 1.6 运行时。Pi 工具现在支持 \`harness.signal\(\)\` 信号唤醒、\`notify\` 跨 session 等待及 \`onAbort: &quot;keep&quot;\` 保留输入，agent 可在工具等待时睡眠。MCP 客户端新增 \`MCPAuthorizationRequiredError\` 重新授权信号，失败服务器需调用 \`reconnectMcpServer\(id\)\` 恢复。失败请求不再向客户端泄露错误详情，改为通用 500 或 WebSocket 1011 关闭，并提供 \`onFetchError\(\)\` 回调。

github · github-actions\[bot\] · 11月20日 15:56

**「设计要点」** Pi 1.6 运行时引入工具级 park/wait 原语，agent 主循环可在工具等待信号或截止时间时释放执行权。MCP 客户端增加显式授权失效状态机，失败服务器停止自动重试，需前端调用 \`reconnectMcpServer\(id\)\` 恢复；错误处理层在服务端截断异常栈，客户端仅收到通用状态码。

**「改了什么」** Pi 工具获得等待原语，支持信号唤醒、跨 session 通知及中止后保留输入。MCP 客户端增加重新授权错误类型和手动重连接口，服务端默认隐藏失败请求的错误详情。

**标签**: `#runtime`, `#tools`, `#mcp`, `#subagents`, `#permissions`

---

<a id="item-harness-arch-2"></a>
### [Agents SDK v1.0.0a1 发布](https://github.com/openai/openai-agents-python/releases/tag/v1.0.0-alpha.1) ⭐️ 7.8/10

openai-agents-python 发布 v1.0.0-alpha.1，将 Codex 作为可选模型提供商嵌入 Python SDK。通过 PyO3 直接集成未修改的 Codex Core rust-v0.166.0，消除独立的 app-server 与 JSON-RPC 中间层。支持 per-run 选择 CodexProvider，复用 ThreadManager，并通过 SDK session 管理对话历史。预构建 wheel 仅通过 GitHub Releases 分发，支持 CPython 3.10–3.14 及四大平台。

github · markstuart-oai · 11月20日 20:51

**「设计要点」** 运行时通过 PyO3 将 Rust 版 Codex Core 直接嵌入 Python 进程，移除外部 app-server 与 JSON-RPC 调用链。Provider 复用同一 ThreadManager，每次调用获得独立线程；SDK session 负责历史记录与自动压缩。原生工具与审批逻辑直接遵循 Codex 的沙盒策略，审批暂停会终止当前模型调用。

**「改了什么」** 相对 v0.24.0-alpha.8，执行入口从 Agent.run\(\)/Session.submit\(\) 迁移到 Runner.run\(\)/Runner.run\_streamed\(\)，需在 RunConfig 中显式选择 CodexProvider；agents.classic 导入路径同步变更。SessionState 与 Runner 的 RunState 检查点格式不兼容，建议新建 SDK session；同时修复 session 压缩对 Codex 本地历史的支持及沙盒清单内联二进制文件保留。

**标签**: `#runtime`, `#models`

---

<a id="item-harness-arch-3"></a>
### [Claude Code v2.1.330 发布](https://github.com/anthropics/claude-code/releases/tag/v2.1.330) ⭐️ 5.5/10

这是 Anthropic 官方发布的 Claude Code v2.1.330 版本，新增企业组织登录、内置 easel 图表绘制工具、自托管运行器启动目录配置、插件系统错误提示优化四项核心能力；同时修复了 40 余个涉及会话稳定性、工具调用、MCP 集成、跨平台兼容性等模块的问题，整体提升企业级使用体验与运行稳定性。

github · claude-code-publisher\[bot\] · 11月20日 22:32

**「设计要点」** 自托管运行器新增两项调度耗时指标，分别统计从工作订单下发到运行器注册、到首会话交接的时长，方便排查编排调度瓶颈；内置 easel 图表工具作为独立 mod 运行，支持 MCP 指标结果自动生成图表，用户可在\`/config\`中关闭自动出图功能。

**「改了什么」** \#\#\# 新增能力
\1. 企业组织登录：支持登录 Anthropic Enterprise Admin Console 管控的组织，自动应用组织策略并使用对应云服务商或网关；新增\`CLAUDE\_CODE\_FULL\_SIGN\_IN\_LINK=1\`环境变量，可在短链接报错或脚本读取链接时输出完整登录地址。
\2. 内置 easel 图表绘制 mod：Pro、Max、Team、Enterprise 用户可在 macOS、Linux 上使用，支持根据需求或 MCP 指标结果自动生成图表，可在\`/config\`中关闭自动出图。
\3. 自托管运行器配置：新增\`--start-dir\` / \`SELF\_HOSTED\_RUNNER\_START\_DIR\`参数，可配置工作启动目录，设置与 hooks 仍正常加载；\`/metrics\`新增两项调度耗时指标，分别统计编排器派生运行器从工作订单下发到注册、到首会话交接的时长。
\4. 插件系统优化：\`claude plugin install --json\`输出新增\`commandPrinted\`、\`commandFailed\`字段，标识插件安装命令的输出与执行状态；插件市场拉取失败、Anthropic 管控 git 拒绝插件仓库时新增明确提示，命名插件并给出操作建议。
\#\#\# 问题修复
共修复 40 余个问题，覆盖会话稳定性、工具调用、MCP 集成、跨平台兼容性、权限管理、远程控制、文件操作、插件系统等模块，包括：长会话压缩后冻结、WebFetch 卡顿/返回空结果、多进程同时保存设置丢失、\`--continue\`/\`--resume\`打开空会话、Linux/WSL 休眠后连接等待超时、MCP 工具 schema 异常导致会话文件膨胀、慢仓库 Bash 命令无差异输出、Git Bash 启动慢导致后续 Bash 变慢、\`/rewind\`恢复错版本文件、权限批准后输入丢失、MCP 资源@提及不生效、MCP 服务器被过早关闭、Chrome 连接状态异常、Bedrock 会话模型选择错误、全屏模式输入丢失、同名 MCP 连接器被覆盖、多插件命令并发时插件丢失、任务并发时元数据丢失、磁盘满时备份文件异常、Code Mode 多项异常、LSP 工具调用卡顿/失败、\`/mcp\`列表分类错误、企业策略拦截 easel 的重复警告、\`/stats\`时区统计错误、\`/ultrareview\`跨仓库评审错误、Grep 多行模式匹配异常、带 BOM 的 Jupyter 被判定为无效 JSON、CLAUDE.md/记忆文件链接定义被注释删除、Monitor 会话记忆残留、第三方 Claude Desktop 长会话+PDF 报错、同名 agent 文件选择错误、daemon 日志无文件时卡住、Markdown 加粗/斜体后字符丢失、Edit 拒绝合法 hook 命令、Read 分页显示重复等。

**「评论」** 暂无社区评论可用。

**标签**: `#permissions`, `#tools`, `#mcp`, `#runtime`

---

## Agent 工程师日报
{: #sec-agent-engineer .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-agent-engineer" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-agent-engineer-1"></a>
### [Inkling 2 Mini 循环 Transformer 开源](https://thinkingmachines.ai/news/inkling-2-mini/) ⭐️ 8.0/10

2026 年 11 月 20 日，Thinking Machines AI 发布开源权重循环 Transformer 模型 Inkling 2 Mini，模型参数量级参考了社区对轻量本地模型的需求设计。官方称其性能对标 Qwen3 8B-27B 级别，训练全程采用 nvfp4 精度，本地解码在 Ryzen 平台通过 llama.cpp Vulkan 后端可达 27 tok/s，M1 Pro 32GB MacBook 跑 q4\_xl 量化版约 10 tok/s。社区已有用户实测其基础编码任务表现达标，相关 llama.cpp 优化 PR（32694、32657、32429、32704）及社区补丁可额外提升约 30%解码速度，目前研究访问权限尚未完全开放。

hackernews · jasondavies · 11月20日 20:12 · [社区讨论](https://news.ycombinator.com/item?id=50581260)

**「为什么重要」** 这是目前首个公开权重的循环 Transformer 模型，打破了此前循环架构仅处于传闻的状态，其本地解码效率匹配社区对轻量编码模型的长期需求。目前其复杂场景下的真实编码表现、对模型安全可解释性的影响尚未有充分验证。

**「可关注」** 可关注：循环架构开源模型的推理优化路径，以及 llama.cpp 未合并 PR 和社区补丁对 Inkling 2 Mini 解码速度的提升效果。

**「评论」** 社区共识认为该模型基础编码表现达标、本地部署效率符合预期，部分用户关注循环架构对模型安全可解释性的影响，也有用户希望获得研究权限开展更高量级的 harness 测试。

**标签**: `#coding-agent`, `#eval`, `#harness`, `#memory`

---

<a id="item-agent-engineer-2"></a>
### [AltRA-Test 提出稀疏标注场景 LLM 替代检验方法](https://huggingface.co/papers/2611.26073) ⭐️ 7.0/10

Hugging Face Daily Papers 于 2026-11-21 推介论文《AltRA-Test: An Alternative Annotator Test for LLM Judges Without Shared Annotators》。该论文提出 AltRA-Test 统计检验方法。该方法解决现有替代标注者测试（Alt-Test）仅适用于密集标注场景的局限。AltRA-Test 通过 bootstrap 重采样项目，为每个项目抽取 k 条人类标注并替换其中一条为 LLM 标注，生成配对数据。这验证了大规模稀疏标注场景下 LLM 替代人类标注的统计合理性。该方法对采用 LLM 作为评分或标注工具的 Agent 评测体系有直接参考价值，但未涉及 Agent 工程其他核心模块改进。

rss · Hugging Face Daily Papers · 11月21日 04:28

**「为什么重要」** 现有 LLM 替代人类标注的统计检验仅支持密集标注场景。大规模标注实践中常出现不同项目由不同标注者标注的稀疏情况。AltRA-Test 填补了这一空白，为 Agent 评测中 LLM 标注的可靠性提供了可验证框架。

**「可关注」** 可关注：AltRA-Test 的 bootstrap 重采样设计允许在标注者不完全重叠的场景下进行统计检验。这对构建大规模 Agent 评测数据集时的标注质量控制有直接参考价值。

**标签**: `#eval`, `#llm-judge`, `#statistical-validation`

---

<a id="item-agent-engineer-3"></a>
### [arXiv 预印本称模型可自改权重](https://arxiv.org/abs/2611.21885) ⭐️ 6.0/10

2026 年 11 月 20 日公开的 arXiv 预印本（编号 2611.21885）声称语言模型无需梯度训练即可通过自我推理改写自身权重提升性能，但 Hacker News 社区讨论指出观测到的“性能提升”仅为缩短推理轨迹以避免触达 token 上限，且该方向已有 Google“sleep”框架、权重空间编程等相关先例，同时讨论也提及自主大模型自我改权可能带来的安全风险。

hackernews · lwhsiao · 11月20日 16:29 · [社区讨论](https://news.ycombinator.com/item?id=50577265)

**「为什么重要」** 该预印本的核心主张已被社区指出存在明显瑕疵，且相关方向已有公开先例，其 novelty 存疑；同时社区讨论点出了自主运行大模型自我改权的安全风险，对智能体权限管控设计有参考价值。

**「可关注」** 可关注自主智能体的权重修改权限边界设计，避免模型未经受控的自我改权引发安全或对齐问题。

**「评论」** 社区讨论普遍质疑该研究的“无训练”表述，认为观测到的“性能提升”实为缩短推理轨迹规避 token 限制的 trivial 结果，同时援引 Google“sleep”框架、权重空间编程等 prior 工作质疑其 novelty，另有评论指出该方向可能带来自主智能体消解安全对齐的风险。

**标签**: `#eval`, `#permissions`, `#harness`

---

<a id="item-agent-engineer-4"></a>
### [TuringSpace 空间智能基准发布](https://huggingface.co/papers/2611.25387) ⭐️ 6.0/10

Hugging Face Daily Papers 于 2026-11-21 介绍论文《TuringSpace: Grounding Spatial Intelligence in Action with Interactive CAPTCHAs》。该工作提出包含 125 个交互式 CAPTCHA 的合成网络环境，覆盖五种空间能力，要求模型通过屏幕点击与拖拽完成任务；每个任务以程序形式实现，支持实例生成、检查器与预言机，构成可扩展训练 gym。现有 CAPTCHA 基准多已被解决且极少涉及空间推理，空间基准也罕有动作要求。该工具主要面向交互式多模态智能体评估，对通用 agent 工程用例较窄。

rss · Hugging Face Daily Papers · 11月21日 04:28

**「为什么重要」** TuringSpace 填补了交互式空间推理评估的空白，为多模态模型提供了可复现的动作式测试床。但其用例聚焦 CAPTCHA 场景，尚未证实对通用 agent 工程有广泛迁移价值。

**「可关注」** 可关注：TuringSpace 的程序化任务生成与检查器/预言机设计，为交互式多模态智能体提供了可复现的评估与训练框架。

**标签**: `#eval`

---

<a id="item-agent-engineer-5"></a>
### [HF 每日论文 扩散 Transformer 激活转向替代 RL 后训练](https://huggingface.co/papers/2611.26627) ⭐️ 6.0/10

2026 年 11 月 21 日 Hugging Face 每日论文收录编号 2611.26627 的论文显示，扩散 Transformer 的强化学习（RL）后训练增益可通过添加至冻结基座模型块输出的固定激活转向向量复现，在 SD3.5-M 上该向量参数量仅为 RL 微调 LoRA 的 1/65（0.29M 对比 18.8M），且拟合过程无需奖励信号，仅需匹配公开 RL 微调检查点的速度预测。现有公开内容存在截断，部分实验细节未完整披露。当前结论仅基于扩散 Transformer 验证，未证明对 LLM 智能体系统的直接适用性，相关发现为多模态及 LLM 智能体调优提供了潜在可参考的低成本调优思路。

rss · Hugging Face Daily Papers · 11月21日 04:28

**「为什么重要」** 该研究提出 RL 后训练增益可能主要源于简单输入无关激活偏移的假设，若该结论可迁移至 LLM 智能体调优场景，将大幅降低后训练成本；但目前该假设仅在扩散 Transformer 上得到验证，尚未证实对 LLM 智能体的适用性。

**「可关注」** 可关注：当前仅验证于扩散 Transformer 的结论显示 RL 后训练增益可由参数量仅为 LoRA 1/65 的输入无关激活转向向量复现，且拟合无需奖励信号，但该思路对 LLM 智能体调优的适用性尚未得到证实。

**标签**: `#activation-steering`, `#rl-post-training`, `#parameter-efficient-tuning`, `#diffusion-transformers`

---

<a id="item-agent-engineer-6"></a>
### [Fragments 11·20：AI 审查成本差](https://martinfowler.com/fragments/2026-11-20.html) ⭐️ 6.0/10

2026 年 11 月 20 日，Martin Fowler 发布的 Fragments 片段引用了 CodeScene 开展的一项实验。该实验覆盖 3 个 LLM、246 个开源仓库的 465 个 PR，每个 PR 经 5 个代理组成的审查修复流水线处理，对比 CodeScene 健康度评分 2.8（低健康度）与 9.7（高健康度）的 PR，发现 AI 审查代理处理低质量 PR 的 token 成本比高质量 PR 高 22%至 35%，其中 Complex Method 与 Complex Conditional 是推高成本的主要代码坏味道。当前公开内容仅为高层摘要，完整实验方法、可复现设置需查看原 CodeScene 博客。

rss · Martin Fowler · 11月20日 18:38

**「为什么重要」** 该实验首次量化了代码质量对 AI 审查流水线 token 成本的直接影响，22%-35%的成本差对大规模代码审查场景的成本控制与代码质量治理有直接参考价值。但当前仅公开高层摘要，完整实验细节与可复现性尚未公开。

**「可关注」** 可关注：AI 代码审查场景中，低质量 PR 会直接推高 22%-35%的 token 成本，Complex Method 与 Complex Conditional 是主要成本诱因；同时需控制代理运行速度在人类可治理阈值内避免失控，且当前 agentic 工程中验证已取代代码生成成为核心瓶颈。

**标签**: `#coding-agent`, `#eval`

---

<a id="item-agent-engineer-7"></a>
### [ZeroVLN 免 SFT 的 VLM 导航框架](https://huggingface.co/papers/2611.26414) ⭐️ 5.5/10

2026 年 11 月 21 日 Hugging Face 每日论文发布 ZeroVLN 视觉语言导航框架摘要，该框架采用慢-快导航架构，无需对 VLM 主干做导航域有监督微调，通过语义工具调用接口将动作决策委托给独立动作专家，避免改动基础 VLM 权重导致的通用视觉能力退化。当前公开材料仅为论文聚合站摘要，缺少性能基准、完整实现细节，可立即落地的实践价值有限，为视觉语言导航、VLM Agent 方向的工程师提供了免微调适配领域的架构参考。

rss · Hugging Face Daily Papers · 11月21日 04:28

**「为什么重要」** 该框架为 VLM Agent 设计提供了保留核心模型能力的通用架构思路，通过解耦 VLM 主干与动作决策模块，可规避微调带来的通用能力退化风险，目前尚未有公开的性能验证与落地案例。

**「可关注」** VLM Agent 可通过语义工具调用接口解耦动作决策模块，在不微调 VLM 主干的前提下适配领域任务。

**标签**: `#orchestration`, `#tool-calling`, `#vlm-agent`, `#fine-tuning-avoidance`, `#embodied-navigation`

---

## AI 日报
{: #sec-ai-daily .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-daily" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-daily-1"></a>
### [OpenAI 公布对抗性蒸馏防御方案](https://openai.com/index/combatting-adversarial-distillation) ⭐️ 6.8/10

OpenAI 发布官方博客，提出对抗对抗性蒸馏的分层防御方案，整合模型训练、安全防护、检测与执法四类措施，防范模型能力提取攻击，未披露具体技术细节与落地安排。

rss · OpenAI Blog · 11月20日 10:00

**「为什么重要」** 对抗性蒸馏是大模型能力泄露的高风险攻击路径，该方案是 OpenAI 首次系统公开的对应防御框架，为行业防护提供参考方向。

**「可关注」** 可关注：OpenAI 将对抗性蒸馏防御拆分为训练、防护、检测、执法四层，后续可跟踪各层的具体实现与落地进展。

**标签**: `#model`, `#lab`, `#industry`, `#security`

---

## AI 羊毛
{: #sec-ai-deals .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-deals" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-deals-1"></a>
### [Epic 11.20~26 限免两款游戏](https://www.appinn.com/eggs-261120/) ⭐️ 8.0/10

你看到的内容可能由第三方 AI 基于小众软件文章提炼总结而成，可能与原文真实意图存在偏差。不代表小众软件观点和立场。请&lt;a href=&quot;https://www.appinn.com/eggs-261120/&quot; target=&quot;\_blank&quot;&gt;点击链接阅读原文&lt;/a&gt;细致比对和校验。&lt;br /&gt;&lt;br /&gt;Epic 于 2026 年 11 月 20 日至 26 日开展限时免费赠送活动，电脑端可领取海盗题材单人动作冒险游戏《深渊之印 / Mark of the Deep》，手机端可领取无战斗解谜生活模拟游戏《Lonesome Village》，两款游戏均支持中文，可通过 Epic 官方商店对应页面领取。

rss · 小众软件 · 11月20日 07:21

**「为什么重要」** 两款游戏均为付费发行内容，本次限免周期仅 7 天，活动结束后需付费购买才能获取。

**「可关注」** 可关注：《深渊之印》融合类银河战士恶魔城探索与类魂战斗，偏好动作冒险的玩家可优先领取；《Lonesome Village》无战斗设计，适合偏好休闲解谜、生活模拟的玩家。

**标签**: `#promo`, `#limited-free`, `#game`, `#epic`

---

<a id="item-ai-deals-2"></a>
### [波波小红书获客助手 30 天版送码](https://www.v2ex.com/t/1258559#reply40) ⭐️ 8.0/10

V2EX 用户 gybin02 赠送自研波波小红书获客助手 30 天版激活码，前 50 条符合要求的回帖可领取。领取需在回帖中留 Base64 编码的邮箱，并回答“找小红书意向客户、回评论最烦哪一步”，一人仅首条回帖有效。激活码需在获取后 30 天内激活，首次激活绑定设备，到期后可 19.9 元终身买断，无自动扣费。

rss · V2EX Hot · 11月20日 07:04

**「为什么重要」** 该工具覆盖小红书运营的养号、线索挖掘、评论私信自动回复等高频重复场景，前 50 名即可免费获得 30 天全功能使用权，适合有小红书获客需求的用户参与。

**「可关注」** 可关注：该工具 AI 评论基于笔记内容现写，非群发灌水，间隔、上限、关键词过滤等参数可自行调整，首次激活绑定设备，支持多账号独立人设配置。

**标签**: `#promo`, `#limited-free`, `#coupon`

---

<a id="item-ai-deals-3"></a>
### [Ferry 免费 iOS Mac 远程桌面](https://www.v2ex.com/t/1258592#reply27) ⭐️ 8.0/10

开发者 reallinzc1 推出免费 iOS 端 Mac 远程桌面应用 Ferry，无广告、无内购、无需注册，可通过国区 App Store 及 TestFlight 下载。该应用逆向实现了 macOS 14 及以上系统屏幕共享的高性能模式，支持 HEVC 视频流与 AAC-ELD 音频传输，低延迟高帧率。使用高性能模式需满足 Mac 为 Apple 芯片、系统版本 macOS 14 以上、开启屏幕共享且用 Mac 账户密码登录的条件，中继网络下会自动退回传统 VNC 模式。

rss · V2EX Hot · 11月20日 08:10

**「为什么重要」** 当前主流 iOS 端 Mac 远程工具免费版普遍存在画质、帧率或功能限制，Ferry 完全免费且提供高性能模式，可替代同类受限的免费方案。

**「可关注」** 可关注：Ferry 高性能模式仅支持 Apple 芯片 Mac、macOS 14 及以上系统，且需 UDP 直连，中继网络、SSH 隧道或代理环境下会自动退回无声音的传统 VNC 模式，连接期间 Mac 会熄灭自身屏幕，断开后恢复。

**标签**: `#free-tier`, `#promo`, `#limited-free`

---