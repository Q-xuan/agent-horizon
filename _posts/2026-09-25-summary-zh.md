---
layout: default
title: "Horizon Summary: 2026-09-25 (ZH)"
date: 2026-09-25
lang: zh
---

> 从 226 条内容中筛选出 17 条重要资讯。

---

**Harness 架构**
1. [Mastra 1.69.0：分类器与后台工具](#item-harness-arch-1) ⭐️ 8.8/10
2. [cline/cline released sdk/sdk/v0.0.86](#item-harness-arch-2) ⭐️ 8.3/10
3. [pydantic/pydantic-ai released v2.49.0](#item-harness-arch-3) ⭐️ 8.3/10
4. [Cline Desktop v0.0.35 发布](#item-harness-arch-4) ⭐️ 7.3/10
5. [Cline CLI v3.0.65 发布](#item-harness-arch-5) ⭐️ 6.3/10
6. [Gemini CLI v0.61.0 发布](#item-harness-arch-6) ⭐️ 6.3/10
7. [2.1.282](#item-harness-arch-7) ⭐️ 6.3/10
8. [Anthropic 开源金融 agents 参考实现](#item-harness-arch-8) ⭐️ 5.5/10

**Agent 工程师日报**
1. [HF daily paper: Schrödinger&\#x27;s Code Repository: Have LLMs Learned SWE-bench or Memorized It?](#item-agent-engineer-1) ⭐️ 8.0/10
2. [Just-in-Time Memory 论文](#item-agent-engineer-2) ⭐️ 7.0/10
3. [HF 论文：提取前沿模型隐藏思维链](#item-agent-engineer-3) ⭐️ 7.0/10
4. [VHD-Play 先解模型再造 RL 环境](#item-agent-engineer-4) ⭐️ 7.0/10
5. [LFM2.5-VL-DSpark 发布](#item-agent-engineer-5) ⭐️ 6.8/10

**AI 日报**
1. [Claude Opus 5.5 长会话降本 40%](#item-ai-daily-1) ⭐️ 9.8/10
2. [Meta AI Glasses 引入隐私处理](#item-ai-daily-2) ⭐️ 8.8/10
3. [AI-powered fuzzing with the GitHub Security Lab Taskflow Agent](#item-ai-daily-3) ⭐️ 7.8/10
4. [Claude Tag 频道支持个人连接器](#item-ai-daily-4) ⭐️ 7.8/10

---

## Harness 架构

<a id="item-harness-arch-1"></a>
### [Mastra 1.69.0：分类器与后台工具](https://github.com/mastra-ai/mastra/releases/tag/%40mastra/core%401.69.0) ⭐️ 8.8/10

Mastra 1.69.0 将分类器提升为核心原语，支持在 \`new Mastra\(\{ classifiers \}\)\` 注册并通过管理 API 增删查改，同时可作为类型化工作流步骤驱动分支控制。新增 \`ClassifierProcessor\` 在 agent 输入、输出与流式内容上执行策略，默认 fail-closed，显式中止违规请求。工具层引入 \`context.background.adopt\(\)\`，允许立即返回确认并将长任务交由后台跟踪完成与取消，但句柄仅存于内存，进程重启后不恢复。

github · PaulieScanlon · 9月24日 06:58

**「设计要点」** 分类器评估自动生成 root \`CLASSIFIER\_EVALUATION\` span，工作流步骤暴露完整类型化答案与 token 用量。后台工具通过 \`adopt\(\{ completion, cancel \}\)\` 解耦 \`execute\(\)\` 与长时操作，取消信号经 \`context.abortSignal\` 传递。

**「改了什么」** 新增分类器注册、管理 API 与工作流步骤集成；\`ClassifierProcessor\` 支持输入/输出/流式策略门控并默认 fail-closed；\`context.background.adopt\(\)\` 落地原生后台工具执行。Inngest durable runs 增加可配置 \`retries\` 并修复 resume 快照缺失。

**标签**: `#runtime`, `#tools`, `#permissions`, `#planning`, `#eval`

---

<a id="item-harness-arch-2"></a>
### [cline/cline released sdk/sdk/v0.0.86](https://github.com/cline/cline/releases/tag/sdk/sdk/v0.0.86) ⭐️ 8.3/10

Cline SDK v0.0.86 adds a compact-and-retry recovery path for output-token truncation on local model servers and improves hub startup error reporting.

github · github-actions\[bot\] · 9月24日 05:43

**标签**: `#runtime`, `#memory`

---

<a id="item-harness-arch-3"></a>
### [pydantic/pydantic-ai released v2.49.0](https://github.com/pydantic/pydantic-ai/releases/tag/v2.49.0) ⭐️ 8.3/10

pydantic-ai v2.49.0 adds GitHub Copilot OAuth device flow, TypeSafeModel structured-output refinements, and a RealtimeSession reply-wait API, plus logprobs and model-support fixes.

github · DouweM · 9月24日 03:09

**标签**: `#runtime`, `#permissions`, `#eval`

---

<a id="item-harness-arch-4"></a>
### [Cline Desktop v0.0.35 发布](https://github.com/cline/cline/releases/tag/desktop-v0.0.35) ⭐️ 7.3/10

Cline Desktop v0.0.35 发布。新增 Linux x64 \`.deb\` 与 \`.rpm\` 包，Open folder 调用 GTK 选择器，更新后台下载，无 AppImage。插件 slash 命令不再作为纯文本发给模型，而是执行注册的 handler，按需开启 turn；菜单项取自当前工作区（含 worktrees）。设置页新增 Diagnostics 导出，写入单个文本文件，含版本、OS、设置、sidecar 与 hub 日志、所选会话 manifest，并剥离 API key、凭证、提示与 home 路径。语音输入恢复 provider-backed 实时转写，支持 OpenAI、Vercel AI Gateway、ElevenLabs，断网时回退浏览器 recognizer。Reasoning effort 按 provider 记忆。模型目录更新至 6,386 个，19 个 provider 默认模型变更，其中 11 个改为 Claude Opus 5.5。

github · github-actions\[bot\] · 9月24日 08:34

**「设计要点」** 插件 slash 命令的执行路径从“文本透传给模型”改为“调用插件 handler 并展示回复”，仅当命令要求时才启动新 turn；单个插件损坏不再导致所有 slash 命令失败。诊断导出在本地生成脱敏文本，显式移除 API key、凭证形态值、用户提示与 home 目录路径，可直接附于 GitHub issue。本地模型（llama.cpp、Ollama、LM Studio）触发输出 token 上限时，自动压缩对话并重试一次，不再直接中断运行。应用信任操作系统证书存储，企业 CA 签发的端点不再报 &quot;unable to get local issuer certificate&quot;。

**「改了什么」** 相对 desktop-v0.0.34，新增 Linux 打包与 GTK 文件夹选择器；插件 slash 命令改为执行 handler 而非发送纯文本；设置页加入 Diagnostics 导出；hub 启动失败提示具体原因，等待时间从 8 秒延长到 15 秒；Windows 首次启动因二进制扫描需 8–13 秒。

**标签**: `#runtime`, `#tools`, `#plugins`

---

<a id="item-harness-arch-5"></a>
### [Cline CLI v3.0.65 发布](https://github.com/cline/cline/releases/tag/cli-v3.0.65) ⭐️ 6.3/10

Cline CLI v3.0.65 发布。本地模型长会话触及输出 token 上限时，CLI 压缩对话并重试一次，失败则保留部分答案；Hub 启动失败时给出具体原因，等待时间从 8 秒延长到 15 秒。会话错误与 \`cline history update\` 元数据在恢复后保留，插件加载失败改为 30 秒后重试。Yolo 模式收紧输出规则，新增 ai&amp; 提供商，模型目录扩至 6,386 个。

github · github-actions\[bot\] · 9月24日 05:54

**「设计要点」** 本地模型运行时通过对话压缩与单次重试吸收输出 token 上限；hub 与沙箱作为外部工具层，启动超时与插件加载失败被隔离为重试逻辑，不阻塞主循环。会话状态在恢复路径上持久化，但不进入模型上下文或压缩计数。

**「改了什么」** 相对 v3.0.64，本地模型在输出 token 限制时先压缩重试再保留部分答案；hub 启动等待从 8 秒增至 15 秒并补充诊断；会话错误与 \`history update\` 元数据跨恢复持久化；插件加载失败改为 30 秒后重试而非每次 spawn 沙箱；Yolo 模式提示词收紧；新增 ai&amp; 提供商并刷新模型目录。

**标签**: `#runtime`, `#memory`, `#tools`

---

<a id="item-harness-arch-6"></a>
### [Gemini CLI v0.61.0 发布](https://github.com/google-gemini/gemini-cli/releases/tag/v0.61.0) ⭐️ 6.3/10

Gemini CLI v0.61.0 为维护版本，主攻安全加固与运行时修复。新增间接提示注入防护，阻断通过构建文件修改和不可信标志注入的指令。沙箱侧加固文件系统边界，隔离运行时状态。同时修复显式版本化 Flash 模型 ID 被覆盖、AgentLoopContext 属性在对象展开时丢失的问题。

github · gemini-cli-robot · 9月23日 23:59

**「设计要点」** 沙箱收紧文件系统边界，将运行时状态与宿主隔离。核心循环保留 AgentLoopContext 属性，防止上下文在对象展开时丢失。

**「改了什么」** 新增间接提示注入防护，覆盖构建文件与不可信标志。加固沙箱文件系统边界并隔离运行时状态。修复 Flash 模型 ID 显式版本保留及 AgentLoopContext 属性展开丢失。

**标签**: `#sandbox`, `#permissions`, `#runtime`

---

<a id="item-harness-arch-7"></a>
### [2.1.282](https://code.claude.com/docs/en/changelog#2-1-282) ⭐️ 6.3/10

Claude Code 2.1.282 adds minor terminal, telemetry, MCP, and gateway settings plus a web-history 400 error fix.

rss · Claude Code Changelog · 9月24日 18:46

**标签**: `#runtime`, `#mcp`, `#permissions`, `#sandbox`, `#tools`

---

<a id="item-harness-arch-8"></a>
### [Anthropic 开源金融 agents 参考实现](https://github.com/anthropics/financial-services) ⭐️ 5.5/10

Anthropic 开源金融 agents 参考实现，含 skills 与 data connectors。覆盖投行、股票研究、私募与财富管理工作流。同一份 system prompt 和 skills 支持两种部署：安装为 Claude Cowork 插件，或经 Claude Managed Agents API 接入自有工作流引擎。该仓库是领域参考材料，非 harness 架构或协议更新。

rss · GitHub Trending Daily · 9月24日 23:19

**「设计要点」** 同一份 system prompt 与 skills 可在两种位置运行：本地作为 Claude Cowork 插件，或通过 Claude Managed Agents API 置于自有工作流引擎之后。工具层以 skills 和 data connectors 形式暴露。

**标签**: `#agents`, `#tools`, `#runtime`

---

## Agent 工程师日报

<a id="item-agent-engineer-1"></a>
### [HF daily paper: Schrödinger&\#x27;s Code Repository: Have LLMs Learned SWE-bench or Memorized It?](https://huggingface.co/papers/2609.27891) ⭐️ 8.0/10

A new paper introduces SchrodingerRepo, an evaluation framework that dynamically instantiates repository representations to combat data leakage and memorization in coding agent benchmarks like SWE-bench.

rss · Hugging Face Daily Papers · 9月24日 00:00

**标签**: `#eval`, `#coding-agent`, `#memory`

---

<a id="item-agent-engineer-2"></a>
### [Just-in-Time Memory 论文](https://huggingface.co/papers/2609.27334) ⭐️ 7.0/10

Hugging Face Daily Papers 在 2026-09-24 推荐的论文提出，现有 agent memory 系统多在 write time 策展：任务结束后把轨迹压成反思、工作流、技能或推理策略等固定产物，之后按相似度检索。这要求在未知未来查询前决定记什么，不可逆丢弃信息，且产出与查询无关的摘要。学习 write-time 策展器还面临长程信用分配，存储决策的价值可能要到很多任务之后、相关查询出现时才显现。该论文保留原始轨迹，把策展推迟到查询时，学习任务自适应的 memory。

rss · Hugging Face Daily Papers · 9月24日 00:00

**「为什么重要」** 对做 coding agent 与 harness 的工程师，memory 策展时机直接影响信息保留与长程任务表现。该论文把策展从 write time 移到查询时，为缓解信息损失和信用分配提供了可解释的技术路径；但摘要未展示基准突破或生产数据，实际收益仍待验证。

**「可关注」** 可关注：若现有 agent 依赖 write-time 摘要做 memory，可评估保留原始轨迹、在查询时学习策展是否更能支撑长程 coding 任务。

**标签**: `#memory`, `#eval`, `#coding-agent`

---

<a id="item-agent-engineer-3"></a>
### [HF 论文：提取前沿模型隐藏思维链](https://huggingface.co/papers/2609.26637) ⭐️ 7.0/10

2026 年 9 月 24 日，Hugging Face Daily Papers 收录论文《Capable yet Parsimonious》。研究通过标准 API 注册自定义工具，诱导闭源前沿模型外部化中间推理。作者先在开源模型上对比原生 CoT，再扩展至 GPT-6 Astra 等闭源前沿模型；提取的推理性能与原生 CoT 持平，并在竞赛数学、科学和代码生成上显著优于无推理基线。论文同时提醒，这些轨迹可能反映事后合理化而非真实推理。

rss · Hugging Face Daily Papers · 9月24日 00:00

**「为什么重要」** 该论文提供了一条可复现的路径，把闭源模型的隐藏推理转为可见文本，直接服务 agent 评测与可观测性。目前证据限于研究实验，尚未证明对主流 coding agent 工作流产生实际影响。

**「可关注」** 可关注：通过标准 API 注册自定义工具即可诱导闭源模型输出中间推理，可在评测中与原生 CoT 及无推理基线三方对比，但需区分真实推理与事后合理化。

**标签**: `#eval`, `#observability`, `#coding-agent`, `#harness`

---

<a id="item-agent-engineer-4"></a>
### [VHD-Play 先解模型再造 RL 环境](https://huggingface.co/papers/2609.27321) ⭐️ 7.0/10

VHD-Play 反转环境生成顺序：先采样并求解数学模型，再由语料库支撑的 setter 将决策过程渲染为有状态工具。可执行动力学与轨迹评分参考继承自同一已解模型。流水线产出 3,300 个多样化智能体环境，单个成本数美分。现有方法通常先搭环境、后补结果规则或标注轨迹，动力学与评估只能事后对齐。

rss · Hugging Face Daily Papers · 9月24日 00:00

**「为什么重要」** 长程任务的状态演化、决策依赖与延迟结果，让环境多样性和结果信号成为训练瓶颈。VHD-Play 将可执行动力学与评分参考绑定在同一已解模型上，避免事后对齐。对构建 agent 训练与评估工具链的工程师，这提供了一条低成本、可验证的环境扩展路径。

**「可关注」** 可关注：VHD-Play 把「先有可执行模型，再生成环境」作为默认顺序，若需批量构造带状态、带延迟反馈的 RL 环境，可评估其已解模型到有状态工具的渲染成本与评分一致性。

**标签**: `#eval`, `#orchestration`, `#harness`

---

<a id="item-agent-engineer-5"></a>
### [LFM2.5-VL-DSpark 发布](https://huggingface.co/blog/LiquidAI/lfm2-5-vl-dspark) ⭐️ 6.8/10

2026 年 9 月 24 日，Liquid AI 发布 LFM2.5-VL-DSpark，为 LFM2.5-VL-3B 配备视觉草稿模型，用投机解码加速 VLM 推理。草稿模型约 280M 参数，在 3B 目标模型上增加 8.9% 参数，采用 4 层简化注意力结构，推荐块大小 8 或 9。官方基准显示，设备端解码最高加速 3.13x，H100 上最高 2.66x；端到端提升分别达 2.62x 和 2.27x。llama.cpp、MLX-VLM 与 SGLang 已首日支持，但需合入对应 PR。

rss · Hugging Face Blog · 9月24日 14:08

**「为什么重要」** 对多模态 Agent 与边缘部署场景，这提供了一条不改变输出质量的推理加速路径：投机解码是精确的，目标模型验证每个草稿 token，贪心输出与单独运行目标模型一致。但视觉编码与预填充不在加速范围内，端到端收益受 Amdahl 定律限制。

**「可关注」** 可关注：视觉草稿模型与文本 DSpark 架构同构，图像块与文本 token 在 tapped layers 前投影到同一隐藏状态空间，推理算法与文本模型完全一致；若已在 LFM2.5 文本栈中接入 DSpark，迁移到 VLM 的改动成本较低。

**标签**: `#toolchain`, `#inference`, `#vlm`

---

## AI 日报

<a id="item-ai-daily-1"></a>
### [Claude Opus 5.5 长会话降本 40%](https://claude.com/blog/claude-opus-5-5-built-for-coding-sessions-that-use-more-context) ⭐️ 9.8/10

Claude 发布 Opus 5.5，官方估算在 token 计费的典型负载下，运行成本比 Opus 5 低约 40%。输入与输出 token 降价 20%，缓存读取降价 60%；Claude Code 单次请求上下文六个月增长约 2.6 倍，缓存未命中率下降超 50%。Zeta Labs 反馈最难任务完成量翻倍，单任务成本接近减半；输出速度比 Opus 5 快 30% 以上。

rss · Claude Blog · 9月24日 00:00

**「为什么重要」** 开发者正把 agent 用于更长、更开放的任务，上下文工程的经济影响被放大。缓存读取占 agentic 与编程工作成本的大头，本次降价直接作用于主要开销；长任务下减少轮次比缓存 token 更省。

**「可关注」** 可关注：运行 /usage 查看 Claude Code 缓存读取占比，把 Opus 5.5 用于开放、上下文重的任务；短而机械的任务收益有限，需自行测量。

**标签**: `#model`, `#lab`, `#product`, `#industry`

---

<a id="item-ai-daily-2"></a>
### [Meta AI Glasses 引入隐私处理](https://engineering.fb.com/2026/09/23/security/private-processing-meta-ai-glasses/) ⭐️ 8.8/10

Meta 工程博客宣布为 Meta AI Glasses 引入隐私处理能力。官方称眼镜是让 AI 全天候辅助用户的理想形态，能理解个人情境并让用户保持专注。目前公开摘要未披露具体技术方案、数据处理范围或上线时间。

rss · Engineering at Meta · 9月24日 00:00

**标签**: `#product`, `#industry`, `#policy`

---

<a id="item-ai-daily-3"></a>
### [AI-powered fuzzing with the GitHub Security Lab Taskflow Agent](https://github.blog/security/application-security/ai-powered-fuzzing-with-the-github-security-lab-taskflow-agent/) ⭐️ 7.8/10

GitHub Security Lab announced an AI-powered fuzzing taskflow agent in an official blog post.

rss · GitHub Blog · 9月24日 18:26

**标签**: `#product`, `#open-source`, `#lab`, `#industry`

---

<a id="item-ai-daily-4"></a>
### [Claude Tag 频道支持个人连接器](https://claude.com/blog/claude-tag-now-supports-personal-connectors-in-channels) ⭐️ 7.8/10

Claude Tag \(beta\) 在 Slack 频道支持个人连接器，用户可调用自己账号下的日历、Google Drive、CRM 等服务，他人无法使用。输出可逐条预览或开启自动模式，企业版管理员可强制全员预览。该功能先在 Team 计划推出，Enterprise 随后；个人连接器不执行无人值守任务，定时与自主操作仍使用管理员挂载的共享连接器。

rss · Claude Blog · 9月24日 00:00

**「为什么重要」** 频道协作长期受限于管理员统一挂载的连接器，个人数据难以在群组场景调用。此次更新把访问权限从频道维度下沉到用户维度，同时保留日志隔离与人工预览控制。

**「可关注」** 可关注：个人连接器的操作日志记在用户名下，频道自身操作仍走服务账号，安全团队可分别审计；但定时任务与自主行为不会使用个人连接器，需依赖共享连接器。

**标签**: `#product`, `#lab`, `#model`

---