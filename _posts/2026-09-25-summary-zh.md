---
layout: default
title: "Horizon Summary: 2026-09-25 (ZH)"
date: 2026-09-25
lang: zh
---

> 从 230 条内容中筛选出 14 条重要资讯。

---

**Harness 架构**
1. [Mastra 1.69.0 分类器与后台工具](#item-harness-arch-1) ⭐️ 8.8/10
2. [Cline SDK v0.0.86 发布](#item-harness-arch-2) ⭐️ 7.8/10
3. [Cline Desktop v0.0.35 更新](#item-harness-arch-3) ⭐️ 6.8/10
4. [pydantic/pydantic-ai released v2.49.0](#item-harness-arch-4) ⭐️ 6.8/10
5. [Claude Code v2.1.282 版](#item-harness-arch-5) ⭐️ 6.3/10
6. [cline/cline released cli-v3.0.65](#item-harness-arch-6) ⭐️ 6.3/10
7. [Claude Code 2.1.282 发布](#item-harness-arch-7) ⭐️ 6.3/10

**Agent 工程师日报**
1. [Liquid AI 发布 VLM 草稿模型](#item-agent-engineer-1) ⭐️ 8.8/10
2. [HF daily paper: Schrödinger&\#x27;s Code Repository: Have LLMs Learned SWE-bench or Memorized It?](#item-agent-engineer-2) ⭐️ 8.0/10
3. [HF daily paper: HappyWorld-Bench](#item-agent-engineer-3) ⭐️ 7.5/10
4. [即时记忆论文：查询时策展 Agent 轨迹](#item-agent-engineer-4) ⭐️ 7.0/10
5. [Gemini 3.8 Live 推出 Live Avatar](#item-agent-engineer-5) ⭐️ 6.3/10
6. [Strata 引擎 12GB 显存 65 tok/s](#item-agent-engineer-6) ⭐️ 5.5/10

**AI 日报**
1. [AI-powered fuzzing with the GitHub Security Lab Taskflow Agent](#item-ai-daily-1) ⭐️ 7.8/10

---

## Harness 架构

<a id="item-harness-arch-1"></a>
### [Mastra 1.69.0 分类器与后台工具](https://github.com/mastra-ai/mastra/releases/tag/%40mastra/core%401.69.0) ⭐️ 8.8/10

Mastra 1.69.0 将分类器（Classifier）提升为一等原语，支持在 \`new Mastra\(\{ classifiers \}\)\` 注册，并提供 \`getClassifier\`、\`listClassifiers\`、\`addClassifier\`、\`removeClassifier\` 等管理 API；未处于 trace 时会通过 observability provider 自动发起 \`CLASSIFIER\_EVALUATION\` 根 span。分类器可作为类型化工作流步骤（含 fluent 与 dynamic graph）驱动分支与条件控制流，并暴露完整答案与 token 用量。新增 \`ClassifierProcessor\` 对 agent 输入、输出与流式内容执行策略管控，默认 fail-closed（分类器失败即中止），可通过 \`errorStrategy: &\#x27;warn&\#x27;\` 退回 fail-open。工具层新增 \`context.background.adopt\(\)\`，允许 \`execute\(\)\` 立即返回确认，同时把长时原生后台操作交给 Mastra 跟踪完成与取消；但 adopted handle 仅存于内存，进程重启后无法恢复。

github · PaulieScanlon · 9月24日 06:58

**「设计要点」** 分类器从评测辅助变成运行时权限与路由的一等组件：既能作为工作流步骤参与控制流，又能通过 \`ClassifierProcessor\` 在 agent 输入/输出/流式链路上做 fail-closed 拦截。后台工具执行从“挂起 \`execute\(\)\` 等待结果”转为“立即确认 + 内存句柄跟踪”，改变了工具运行时的生命周期模型。

**「改了什么」** 相比旧版，分类器获得独立注册与管理 API、工作流步骤集成及自动追踪；\`ClassifierProcessor\` 引入默认中止的输入/输出/流式策略门；工具可通过 \`context.background.adopt\(\)\` 实现原生后台执行而不再阻塞 \`execute\(\)\`。Inngest durable runs 新增可配置 \`retries\`，并修复 \`resumeStream\(\)\` 等恢复方法在关键场景下因缺快照而失败的问题。

**标签**: `#runtime`, `#tools`, `#permissions`, `#eval`

---

<a id="item-harness-arch-2"></a>
### [Cline SDK v0.0.86 发布](https://github.com/cline/cline/releases/tag/sdk/sdk/v0.0.86) ⭐️ 7.8/10

Cline SDK v0.0.86 发布。本地 OpenAI 兼容服务（llama.cpp、Ollama、LM Studio）在输出 token 触顶时，现在会走一次 compact-and-retry 恢复，复用 \`prepareTurn\` 的强制压缩路径，并发出 \`task.max\_tokens\_recovery\` 生命周期事件。Hub 启动失败不再统一报“无兼容运行时”，而是附带真实原因和 \`cause\`。会话重命名、错误持久化、插件斜杠命令服务化等运行时问题同步修复。

github · github-actions\[bot\] · 9月24日 05:43

**「设计要点」** 运行时把输出截断视为上下文溢出的一种，接入同一套 forced-compaction 逻辑；压缩无内容可删或重试仍截断时，交回原有 nudge-and-retry，原始 max-tokens 错误与部分答案保留。插件命令发现、加载与执行收敛到 \`@cline/core\` 的 \`createPluginCommandService\`，CLI 与桌面 sidecar 共用，加载失败缓存空集合并 30 秒后重试。

**「改了什么」** 相对 v0.0.85，本地模型输出截断从直接失败变为一次压缩重试。Hub 启动错误从吞异常改为透传原因。\`HubRuntimeHost.updateSession\` 修复重命名回退。模型目录从 6,237 扩到 6,386，19 个未固定模型的供应商默认值变更。

**标签**: `#runtime`, `#memory`, `#planning`

---

<a id="item-harness-arch-3"></a>
### [Cline Desktop v0.0.35 更新](https://github.com/cline/cline/releases/tag/desktop-v0.0.35) ⭐️ 6.8/10

Cline Desktop v0.0.35 发布，桌面端新增 Linux 支持，每个版本随 macOS、Windows 一起提供 x64 .deb 与 .rpm 包，暂不提供 AppImage。插件斜杠命令不再作为纯文本发给模型，而是执行插件注册的 handler，按需开启回合；设置页新增诊断导出，将应用版本、系统、日志和会话清单写入 Downloads 并剥离敏感信息。

github · github-actions\[bot\] · 9月24日 08:34

**「设计要点」** 插件 slash 命令直接调用 handler 并展示返回，仅在命令要求时启动新回合；诊断导出会移除 API key、凭证形状的值、用户提示词和主目录路径，确保可安全附到 issue。

**「改了什么」** 新增 Linux 打包与 GTK 选择器、插件 slash 命令执行 handler、诊断导出脱敏；推理力度按 provider 记忆，本地模型长回复触顶时压缩会话并重试一次。

**标签**: `#runtime`, `#tools`, `#eval`, `#plugins`

---

<a id="item-harness-arch-4"></a>
### [pydantic/pydantic-ai released v2.49.0](https://github.com/pydantic/pydantic-ai/releases/tag/v2.49.0) ⭐️ 6.8/10

Pydantic-AI v2.49.0 adds GitHub Copilot OAuth device flow, TypeSafeModel structured output refinements, and RealtimeSession.wait\_for\_reply\(\), plus logprobs and model support fixes.

github · DouweM · 9月24日 03:09

**标签**: `#runtime`, `#tools`, `#permissions`

---

<a id="item-harness-arch-5"></a>
### [Claude Code v2.1.282 版](https://github.com/anthropics/claude-code/releases/tag/v2.1.282) ⭐️ 6.3/10

Claude Code v2.1.282 发布补丁。新增 \`allowClaudeInChromeWithManagedMcp\` 托管设置，允许 \`claude --chrome\` 与独占 \`managed-mcp.json\` 同时运行。Gateway 加入 \`store.readiness\_grace\_seconds\`，让 \`/readyz\` 在 Postgres 短暂故障期间保持就绪。修复 web search 结果无法解密导致的所有请求 400 错误，以及会话恢复时 extended thinking 丢失等问题。

github · ashwin-ant · 9月24日 18:38

**「设计要点」** 托管设置层新增 Chrome 与 MCP 互斥开关，并修复嵌套配置失效时的部分应用问题。Gateway 通过 readiness 宽限期容忍 Postgres 故障转移；会话层修复 resumed sessions 的 extended thinking 丢失与 redacted\_thinking 块错误。

**「改了什么」** 新增 \`maxProseWidth\` 设置，在宽终端中限制散文宽度。新增 \`allowClaudeInChromeWithManagedMcp\` 托管设置和 \`store.readiness\_grace\_seconds\` gateway 配置，并修复 web search 解密失败与会话恢复时 extended thinking 丢失。

**标签**: `#tools`, `#mcp`, `#permissions`

---

<a id="item-harness-arch-6"></a>
### [cline/cline released cli-v3.0.65](https://github.com/cline/cline/releases/tag/cli-v3.0.65) ⭐️ 6.3/10

Cline CLI v3.0.65 fixes local-model mid-answer failures with compaction/retry, improves hub startup error reporting and timeout, and preserves session error messages on resume.

github · github-actions\[bot\] · 9月24日 05:54

**标签**: `#runtime`, `#tools`, `#memory`

---

<a id="item-harness-arch-7"></a>
### [Claude Code 2.1.282 发布](https://code.claude.com/docs/en/changelog#2-1-282) ⭐️ 6.3/10

Claude Code 发布 2.1.282。新增 \`maxProseWidth\` 设置，宽终端下限制正文宽度，表格和代码块仍占满。新增托管设置 \`allowClaudeInChromeWithManagedMcp\`，允许 \`claude --chrome\` 与独占 \`managed-mcp.json\` 同时运行。Claude apps gateway 增加 \`store.readiness\_grace\_seconds\`，使 \`/readyz\` 在 Postgres 短暂故障（如数据库故障转移）期间保持就绪。启动提示以及 \`/status\`、\`claude doctor\` 会列出项目 settings 中被忽略或关闭 telemetry 的变量。

rss · Claude Code Changelog · 9月24日 18:46

**「设计要点」** 托管权限层新增 \`allowClaudeInChromeWithManagedMcp\`，将 Chrome 与 MCP 的互斥关系改为可配置；gateway 侧通过 \`store.readiness\_grace\_seconds\` 为 \`/readyz\` 设置宽限期，避免数据库主从切换时误报不健康。

**「改了什么」** 2.1.282 新增 Chrome 与托管 MCP 并行开关、gateway 就绪宽限和 telemetry 诊断入口；同时修复续会话丢失 extended thinking、\`redacted\_thinking\` 块报错、托管设置单个嵌套值无效导致整块被忽略等稳定性问题。

**标签**: `#tools`, `#mcp`, `#permissions`, `#runtime`

---

## Agent 工程师日报

<a id="item-agent-engineer-1"></a>
### [Liquid AI 发布 VLM 草稿模型](https://huggingface.co/blog/LiquidAI/lfm2-5-vl-dspark) ⭐️ 8.8/10

Liquid AI 发布 LFM2.5-VL-DSpark，为 LFM2.5-VL-3B 配套视觉语言投机解码草稿模型。草稿模型新增 280M 参数，占目标模型 8.9%；MLX 在 M5 Max 上解码提速 2.30x–3.13x、端到端最高 2.62x，H100 解码提速 2.04x–2.66x、端到端最高 2.27x。llama.cpp、MLX-VLM、SGLang 首日支持，推理算法与文本 DSpark 相同，且目标模型验证每个 token，贪婪输出与单独运行目标模型一致。该方案只加速解码，视觉编码与预填充仍占用大量端到端时间。

rss · Hugging Face Blog · 9月24日 14:08

**「为什么重要」** 对 coding agent 与 harness 开发者，VLM 推理瓶颈常在预填充与视觉编码，而非解码。LFM2.5-VL-DSpark 用 8.9% 参数增量换取最高 3.13x 解码提速，并首日支持 llama.cpp、MLX-VLM、SGLang，为端侧多模态部署提供了可复制的优化路径。

**「可关注」** 可关注：LFM2.5-VL-DSpark 用 280M 参数（+8.9%）在三大推理栈首日可用，但视觉编码与预填充未被加速，端侧 VLM 的端到端收益受非解码阶段限制。

**标签**: `#inference`, `#speculative-decoding`, `#vlm`, `#harness`, `#performance`

---

<a id="item-agent-engineer-2"></a>
### [HF daily paper: Schrödinger&\#x27;s Code Repository: Have LLMs Learned SWE-bench or Memorized It?](https://huggingface.co/papers/2609.27891) ⭐️ 8.0/10

论文提出 SchrodingerRepo，通过将测试仓库视为评估时动态实例化的潜变量，来应对仓库级 coding agent 基准中的数据泄漏与记忆化问题。

rss · Hugging Face Daily Papers · 9月25日 01:55

**标签**: `#eval`, `#coding-agent`, `#memory`, `#harness`

---

<a id="item-agent-engineer-3"></a>
### [HF daily paper: HappyWorld-Bench](https://huggingface.co/papers/2609.24308) ⭐️ 7.5/10

HappyWorld-Bench is a new hierarchical benchmark for evaluating world models across video, spatial, and embodied tracks using human A/B comparisons.

rss · Hugging Face Daily Papers · 9月25日 01:55

**标签**: `#eval`, `#world-model`, `#benchmark`, `#embodied-ai`

---

<a id="item-agent-engineer-4"></a>
### [即时记忆论文：查询时策展 Agent 轨迹](https://huggingface.co/papers/2609.27334) ⭐️ 7.0/10

Hugging Face Daily Papers 于 2026-09-25 收录一篇论文，提出 Just-in-Time Memory 架构。现有 agentic memory 系统多在写入时策展：任务结束后将轨迹蒸馏为反思、工作流或技能等固定工件，再按相似度检索。论文指出，该做法在查询未知时决定记忆内容，会不可逆丢弃信息，并带来长程信用分配难题；论文改为保留原始轨迹，把策展推迟到查询时。源内容未给出完整方法与实验数据。

rss · Hugging Face Daily Papers · 9月25日 01:55

**「为什么重要」** 对构建 agent memory 的工程师而言，这提供了一条与写入时蒸馏不同的路线：保留原始轨迹，把策展压力移到查询时。已发生变化的是论文提出了该架构；尚未证实的是其在实际长程任务中的收益。

**「可关注」** 可关注：若你的 agent 依赖写入时蒸馏记忆，需评估其是否因查询未知而丢失关键轨迹信息；该论文将原始轨迹保留与查询时策展作为对照方案，但具体效果仍待论文完整数据验证。

**标签**: `#memory`, `#orchestration`, `#eval`, `#coding-agent`

---

<a id="item-agent-engineer-5"></a>
### [Gemini 3.8 Live 推出 Live Avatar](https://deepmind.google/blog/introducing-gemini-38-live-with-live-avatar/) ⭐️ 6.3/10

Google DeepMind 在 2026 年 9 月 24 日发布 Gemini 3.8 Live，该版本新增 Live Avatar 功能。当前公开材料仅包含标题与链接，未提供技术细节、代码、基准测试或架构信息。因此，该更新对 coding agent / harness 工程工作流的实际影响尚无法确认。

rss · Google DeepMind · 9月24日 16:20

**「可关注」** 可关注：Gemini 3.8 Live 已推出 Live Avatar，但公开信息缺少技术细节与基准数据，工程侧暂无法评估其对 agent 工作流的实际价值。

**标签**: `#multimodal`, `#real-time`, `#gemini`, `#product-update`

---

<a id="item-agent-engineer-6"></a>
### [Strata 引擎 12GB 显存 65 tok/s](https://www.reddit.com/r/LocalLLaMA/comments/1wp7zyb/qwen38flashnext_on_12gb_vram_65_tokens_per_second/) ⭐️ 5.5/10

Reddit 用户 KnownAd4832 发布自研推理引擎 Strata，在 12GB RTX 5070、Ryzen 5 7600、64GB DDR5 的 Windows 主机上运行 Qwen3.8-Flash-Next。128K 上下文下，Q2\_0 输出 65.1 tok/s、提示处理 543 tok/s；IQ2\_XS 为 52.0/472；IQ3\_XXS 为 44.8/414。此前 llama.cpp 运行 IQ3\_XXS 仅 15 tok/s 输出、100-120 tok/s 提示处理。最低内存需求 Q2\_0 37.6GB、IQ2\_XS 39.2GB、IQ3\_XXS 47GB（RAM+VRAM），视觉编码器额外占 0.91GB。2-bit 量化采用 RCO-GSQ。引擎目前仅优化 CUDA，支持一键安装。数据均为作者自报，无独立验证。

reddit · r/LocalLLaMA · /u/KnownAd4832 · 9月24日 17:30

**「为什么重要」** 本地部署大模型的工程师可看到，在 12GB 显存消费级显卡上，通过自研引擎配合 2-3 bit 量化与 CPU 内存分担，有机会把推理吞吐做到 llama.cpp 的数倍。但该结果目前仅有单一来源，缺乏第三方复现和官方背书。

**「可关注」** 可关注：Strata 在 128K 上下文下把 Q2\_0 输出拉到 65.1 tok/s，代价是至少 37.6GB 系统内存；若显存只有 12GB，内存容量和 CUDA 优化是复现该吞吐的前提。

**标签**: `#toolchain`, `#inference`, `#coding-agent`

---

## AI 日报

<a id="item-ai-daily-1"></a>
### [AI-powered fuzzing with the GitHub Security Lab Taskflow Agent](https://github.blog/security/application-security/ai-powered-fuzzing-with-the-github-security-lab-taskflow-agent/) ⭐️ 7.8/10

GitHub Security Lab introduces an AI-powered fuzzing taskflow agent for automated vulnerability discovery.

rss · GitHub Blog · 9月24日 18:26

**标签**: `#product`, `#lab`, `#open-source`

---