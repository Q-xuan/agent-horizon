---
layout: default
title: "Horizon Summary: 2026-09-25 (EN)"
date: 2026-09-25
lang: en
---

> From 230 items, 14 important content pieces were selected

---

**Agent Harness Architecture**
1. [Mastra 1.69.0 发布](#item-harness-arch-1) ⭐️ 8.8/10
2. [Cline SDK v0.0.86 发布](#item-harness-arch-2) ⭐️ 7.8/10
3. [Cline Desktop v0.0.35 发布](#item-harness-arch-3) ⭐️ 6.8/10
4. [pydantic/pydantic-ai released v2.49.0](#item-harness-arch-4) ⭐️ 6.8/10
5. [Claude Code v2.1.282 发布](#item-harness-arch-5) ⭐️ 6.3/10
6. [cline/cline released cli-v3.0.65](#item-harness-arch-6) ⭐️ 6.3/10
7. [Claude Code 2.1.282 发布](#item-harness-arch-7) ⭐️ 6.3/10

**AI Agent Engineer**
1. [LFM2.5-VL-DSpark 发布](#item-agent-engineer-1) ⭐️ 8.8/10
2. [HF daily paper: Schrödinger&\#x27;s Code Repository: Have LLMs Learned SWE-bench or Memorized It?](#item-agent-engineer-2) ⭐️ 8.0/10
3. [HF daily paper: HappyWorld-Bench](#item-agent-engineer-3) ⭐️ 7.5/10
4. [Just-in-Time Memory 论文：查询时策展 Agent 记忆](#item-agent-engineer-4) ⭐️ 7.0/10
5. [Gemini 3.8 Live Avatar](#item-agent-engineer-5) ⭐️ 6.3/10
6. [Strata 引擎 Qwen3.8 推理 65 tok/s](#item-agent-engineer-6) ⭐️ 5.5/10

**AI Daily**
1. [AI-powered fuzzing with the GitHub Security Lab Taskflow Agent](#item-ai-daily-1) ⭐️ 7.8/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [Mastra 1.69.0 发布](https://github.com/mastra-ai/mastra/releases/tag/%40mastra/core%401.69.0) ⭐️ 8.8/10

Mastra 1.69.0 将分类器（Classifier）提升为一等原语，支持在 \`new Mastra\(\{ classifiers \}\)\` 注册，并提供 \`getClassifier\`、\`listClassifiers\`、\`addClassifier\`、\`removeClassifier\` 管理 API。分类器可直接作为工作流步骤（含 fluent 与 dynamic graph）驱动分支控制，并自动生成 \`CLASSIFIER\_EVALUATION\` 根追踪。新增 \`ClassifierProcessor\` 对 agent 输入、输出与流式内容执行策略管控，默认 fail-closed（分类器失败即中止），可通过 \`errorStrategy: &\#x27;warn&\#x27;\` 退回 fail-open。工具层新增 \`context.background.adopt\(\)\`，允许 \`execute\(\)\` 立即返回确认，由原生后台任务接管完成与取消；句柄仅存内存，进程重启后不恢复。

github · PaulieScanlon · Sep 24, 06:58

**「设计要点」** 分类器同时进入运行时注册表、工作流步骤与处理器链，形成从评估到策略阻断的统一路径。后台工具通过 adopt 将长任务从 \`execute\(\)\` 生命周期中解耦，但牺牲了跨重启的持久性。

**「改了什么」** 相比此前版本，分类器从独立评估工具变为可注册、可追踪、可阻断的工作流与 agent 原语；后台工具不再需要挂起 \`execute\(\)\` 等待完成。

**Tags**: `#runtime`, `#tools`, `#permissions`, `#eval`

---

<a id="item-harness-arch-2"></a>
### [Cline SDK v0.0.86 发布](https://github.com/cline/cline/releases/tag/sdk/sdk/v0.0.86) ⭐️ 7.8/10

Cline SDK v0.0.86 发布，新增本地模型输出截断的 compact-and-retry 恢复。文本轮次触达 output-token 上限时，运行时走一次强制压缩再重试；压缩无可删内容或重试再次截断，才退回 nudge-and-retry，原始 max-tokens 错误仍带部分回答抛出。产生工具调用的轮次不重放。新增 \`task.max\_tokens\_recovery\` 事件（\`started\`/\`retried\`/\`failed\`）观测恢复频率。

github · github-actions\[bot\] · Sep 24, 05:43

**「设计要点」** 恢复路径复用 \`prepareTurn\` 处理上下文溢出的同一套强制压缩逻辑。插件斜杠命令收敛为 \`@cline/core\` 的 \`createPluginCommandService\`，CLI 与桌面 sidecar 共用；插件加载失败不再拒绝服务，而是记录日志、缓存空命令集，30 秒后重试，handler 异常仍向上抛。

**「改了什么」** Hub 启动失败透出真实原因并放宽新 hub 等待至 15 秒。会话重命名经 \`session.update\` 显式传 \`title\` 不再被 metadata 替换覆盖；终端错误持久化为只显示历史条目；模型列表在主机不可达或密钥错误时上报错误；退避期间可中止请求；流式转录覆盖 OpenAI、Vercel AI Gateway 和 ElevenLabs。

**Tags**: `#runtime`, `#memory`, `#planning`

---

<a id="item-harness-arch-3"></a>
### [Cline Desktop v0.0.35 发布](https://github.com/cline/cline/releases/tag/desktop-v0.0.35) ⭐️ 6.8/10

Cline Desktop v0.0.35 adds Linux support with x64 .deb and .rpm packages. Plugin slash commands now execute handlers instead of passing as plain text to the model. A new Diagnostics export writes sanitized logs to Downloads. Voice input streams via provider-backed transcription with browser fallback, and reasoning effort persists per provider.

github · github-actions\[bot\] · Sep 24, 08:34

**「设计要点」** Plugin slash commands invoke registered handlers directly and start a turn only when requested. Slash menus, skills, and workflows resolve from the active conversation workspace, including worktrees. Diagnostics export strips API keys, credential-shaped values, prompts, and home paths before writing a single text file.

**「改了什么」** Linux packaging \(.deb/.rpm\) joins macOS and Windows with native GTK picker and background updates. Plugin slash commands moved from plain-text passthrough to handler execution. Settings adds a Diagnostics row for sanitized log export. Reasoning effort is remembered per provider, and unreachable endpoints surface real errors instead of empty lists.

**Tags**: `#runtime`, `#tools`, `#eval`, `#plugins`

---

<a id="item-harness-arch-4"></a>
### [pydantic/pydantic-ai released v2.49.0](https://github.com/pydantic/pydantic-ai/releases/tag/v2.49.0) ⭐️ 6.8/10

Pydantic-AI v2.49.0 adds GitHub Copilot OAuth device flow, TypeSafeModel structured output refinements, and RealtimeSession.wait\_for\_reply\(\), plus logprobs and model support fixes.

github · DouweM · Sep 24, 03:09

**Tags**: `#runtime`, `#tools`, `#permissions`

---

<a id="item-harness-arch-5"></a>
### [Claude Code v2.1.282 发布](https://github.com/anthropics/claude-code/releases/tag/v2.1.282) ⭐️ 6.3/10

Claude Code v2.1.282 发布，补丁级更新。新增 \`maxProseWidth\` 设置，在宽终端中限制正文宽度，表格与代码块仍保持全宽；新增 \`allowClaudeInChromeWithManagedMcp\` 托管设置，允许 \`claude --chrome\` 与独占 \`managed-mcp.json\` 同时运行。网关新增 \`store.readiness\_grace\_seconds\`，让 \`/readyz\` 在 Postgres 短暂故障（如数据库切换）期间保持就绪。修复 web search 历史无法解密导致的所有请求 400 错误，以及会话恢复时重发消息、丢失 extended thinking 等问题。

github · ashwin-ant · Sep 24, 18:38

**「设计要点」** 托管设置层增强布尔锁校验与嵌套容错：单个无效值不再导致整个 \`permissions\`、\`autoMode\`、\`worktree\`、\`attribution\` 块被忽略。Bash 权限规则中的 \`:\*\` 中间模式现从所有来源生效，启动时给出匹配警告。

**「改了什么」** 相对上一版，权限与托管配置健壮性提升：Chrome 与 managed MCP 可共存，布尔锁键拼写错误现在会锁定并提示，嵌套无效值不再阻断其余设置。网关侧新增 Postgres 故障宽限，减少误报未就绪。

**Tags**: `#tools`, `#mcp`, `#permissions`

---

<a id="item-harness-arch-6"></a>
### [cline/cline released cli-v3.0.65](https://github.com/cline/cline/releases/tag/cli-v3.0.65) ⭐️ 6.3/10

Cline CLI v3.0.65 fixes local-model mid-answer failures with compaction/retry, improves hub startup error reporting and timeout, and preserves session error messages on resume.

github · github-actions\[bot\] · Sep 24, 05:54

**Tags**: `#runtime`, `#tools`, `#memory`

---

<a id="item-harness-arch-7"></a>
### [Claude Code 2.1.282 发布](https://code.claude.com/docs/en/changelog#2-1-282) ⭐️ 6.3/10

Claude Code 发布 2.1.282，以修复为主，新增少量配置。新增 \`maxProseWidth\` 限制宽终端中 prose 宽度，表格与代码块仍占满；新增托管设置 \`allowClaudeInChromeWithManagedMcp\`，允许 \`claude --chrome\` 与独占 \`managed-mcp.json\` 共存。Claude apps gateway 新增 \`store.readiness\_grace\_seconds\`，让 \`/readyz\` 在 Postgres 短时中断（如数据库故障转移）期间保持就绪。启动提示、\`/status\` 和 \`claude doctor\` 会列出项目中 ignored 或关闭遥测的 settings 变量。

rss · Claude Code Changelog · Sep 24, 18:46

**「设计要点」** 托管设置层细化了 MCP 与 Chrome 的权限边界，\`allowClaudeInChromeWithManagedMcp\` 让浏览器自动化在受管 MCP 环境下可运行。Gateway 通过 \`readiness\_grace\_seconds\` 把数据库故障纳入就绪检查容忍窗口，避免瞬时切换引发服务不可用。

**「改了什么」** 新增 \`allowClaudeInChromeWithManagedMcp\` 托管设置，允许 \`claude --chrome\` 与独占 \`managed-mcp.json\` 同时运行；gateway 新增 \`store.readiness\_grace\_seconds\`，使 \`/readyz\` 可容忍短时 Postgres 故障；Bash 权限规则中的 \`:\*\` 中间模式现从所有 settings 来源生效，不再仅限于 \`--allowedTools\`。

**Tags**: `#tools`, `#mcp`, `#permissions`, `#runtime`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [LFM2.5-VL-DSpark 发布](https://huggingface.co/blog/LiquidAI/lfm2-5-vl-dspark) ⭐️ 8.8/10

Liquid AI 发布 LFM2.5-VL-DSpark，为 LFM2.5-VL-3B 配备视觉语言投机解码 drafter。该 drafter 增加约 280M 参数，仅占目标模型 3B 参数的 8.9%；在 M5 Max 上解码最高加速 3.13x，H100 上最高 2.66x，端到端延迟最高分别改善 2.62x 与 2.27x。llama.cpp、MLX-VLM 与 SGLang 首日支持。drafter 沿用文本 LFM2.5-DSpark 架构，在固定 tapped layers 捕获目标模型隐藏状态并生成候选 token 块；图像 patch 与文本 token 在进入这些层前投影到同一表示空间，推理算法与文本模型一致。

rss · Hugging Face Blog · Sep 24, 14:08

**「为什么重要」** VLM 的端到端延迟由视觉编码、prefill 与 decode 共同决定，而投机解码只作用于 decode。LFM2.5-VL-DSpark 以 8.9% 的参数增量在边缘设备上把 decode 最高提升 3.13x，端到端最高提升 2.62x，表明轻量 drafter 在视觉负载中仍有实际收益。但未加速的视觉编码与 prefill 会按 Amdahl 定律稀释整体增益，这也是 H100 与 Apple silicon 上端到端提升低于 decode 提升的原因。

**「可关注」** 可关注：图像 patch 与文本 token 在 tapped layers 之前已投影到同一隐藏状态空间，drafter 对模态无感知，因此 llama.cpp、MLX-VLM 与 SGLang 可以复用文本 DSpark 的同一套投机解码流程，只需挂载 draft 模型并配置 block size。

**Tags**: `#inference`, `#speculative-decoding`, `#vlm`, `#harness`, `#performance`

---

<a id="item-agent-engineer-2"></a>
### [HF daily paper: Schrödinger&\#x27;s Code Repository: Have LLMs Learned SWE-bench or Memorized It?](https://huggingface.co/papers/2609.27891) ⭐️ 8.0/10

论文提出 SchrodingerRepo，通过将测试仓库视为评估时动态实例化的潜变量，来应对仓库级 coding agent 基准中的数据泄漏与记忆化问题。

rss · Hugging Face Daily Papers · Sep 25, 01:55

**Tags**: `#eval`, `#coding-agent`, `#memory`, `#harness`

---

<a id="item-agent-engineer-3"></a>
### [HF daily paper: HappyWorld-Bench](https://huggingface.co/papers/2609.24308) ⭐️ 7.5/10

HappyWorld-Bench is a new hierarchical benchmark for evaluating world models across video, spatial, and embodied tracks using human A/B comparisons.

rss · Hugging Face Daily Papers · Sep 25, 01:55

**Tags**: `#eval`, `#world-model`, `#benchmark`, `#embodied-ai`

---

<a id="item-agent-engineer-4"></a>
### [Just-in-Time Memory 论文：查询时策展 Agent 记忆](https://huggingface.co/papers/2609.27334) ⭐️ 7.0/10

Hugging Face Daily Papers 于 2026-09-25 收录论文 Just-in-Time Memory，主张保留原始 Agent 轨迹，把记忆策展推迟到查询时执行，以避开写入时蒸馏带来的信息丢失与长程信用分配问题。现有设计在任务结束后将轨迹固化为反思、工作流或技能等工件，未来查询未知，只能生成查询无关的摘要。该论文目前停留在提出架构层面，未给出具体工具或协议变更，也未提供生产环境验证数据。

rss · Hugging Face Daily Papers · Sep 25, 01:55

**「为什么重要」** 对 coding agent 与 harness 设计者，这暴露了记忆模块的核心张力：写入时策展实现简单但会不可逆地丢弃信息，查询时策展保留原始上下文却可能增加检索与计算开销。论文尚未公布实测基准，实际收益与成本仍待社区验证。

**「可关注」** 可关注：若现有 Agent 记忆依赖写入时蒸馏，可评估保留原始轨迹、在查询时再做筛选的方案，尤其观察长程任务中信用分配与信息保真的差异。

**Tags**: `#memory`, `#orchestration`, `#eval`, `#coding-agent`

---

<a id="item-agent-engineer-5"></a>
### [Gemini 3.8 Live Avatar](https://deepmind.google/blog/introducing-gemini-38-live-with-live-avatar/) ⭐️ 6.3/10

Google DeepMind 发布 Gemini 3.8 Live，新增 Live Avatar 功能。官方公告已上线，但现有材料仅包含标题与链接，未提供技术细节、代码、基准测试或架构信息。该功能定位实时多模态场景，具体能力与限制尚不明确。

rss · Google DeepMind · Sep 24, 16:20

**「为什么重要」** 这是 Google DeepMind 在实时多模态方向的官方产品更新，但材料中缺乏技术细节，暂无法确认对 coding agent 或 harness 工作流的直接影响。

**「可关注」** 可关注：Gemini 3.8 Live 引入 Live Avatar，但当前未见技术文档与基准数据，工程侧可等待更多细节再评估接入价值。

**Tags**: `#multimodal`, `#real-time`, `#gemini`, `#product-update`

---

<a id="item-agent-engineer-6"></a>
### [Strata 引擎 Qwen3.8 推理 65 tok/s](https://www.reddit.com/r/LocalLLaMA/comments/1wp7zyb/qwen38flashnext_on_12gb_vram_65_tokens_per_second/) ⭐️ 5.5/10

Reddit 用户 KnownAd4832 发布自研推理引擎 Strata，针对 Qwen3.8-Flash-Next 与 12GB 显存 PC 优化。同一 IQ3\_XXS 量化下，输出从 llama.cpp 的 15 tok/s 提升到约 65 tok/s，提示处理从 100–120 tok/s 提升到约 430 tok/s。在 128K 上下文、64GB DDR5（5600）+ RTX 5070 12GB + Ryzen 5 7600 + Windows 环境下，Q2\_0 输出 65.1 tok/s、提示处理 543 tok/s；IQ3\_XXS 输出 44.8 tok/s、提示处理 414 tok/s。最低内存+显存需求从 Q2\_0 的 37.6GB 到 IQ3\_XXS 的 47GB 不等，视觉编码器另占 0.91GB；引擎目前仅优化 CUDA，提供一键安装，所有性能数字为作者自报，暂无独立验证。

reddit · r/LocalLLaMA · /u/KnownAd4832 · Sep 24, 17:30

**「为什么重要」** 对持有 12GB 显卡和 64GB 内存的本地部署者，这给出了在 128K 上下文下运行 Qwen3.8-Flash-Next 的一条路径，但性能数字来自单一自报测试，尚未经第三方复现。

**「可关注」** 可关注：Strata 在 2-bit 量化（Q2\_0）下同时给出最高输出与提示处理速度，且内存+显存门槛比 IQ3\_XXS 低约 9.4GB，低比特量化配合专用引擎可能是 12GB 显存跑长上下文的一个权衡点。

**Tags**: `#toolchain`, `#inference`, `#coding-agent`

---

## AI Daily

<a id="item-ai-daily-1"></a>
### [AI-powered fuzzing with the GitHub Security Lab Taskflow Agent](https://github.blog/security/application-security/ai-powered-fuzzing-with-the-github-security-lab-taskflow-agent/) ⭐️ 7.8/10

GitHub Security Lab introduces an AI-powered fuzzing taskflow agent for automated vulnerability discovery.

rss · GitHub Blog · Sep 24, 18:26

**Tags**: `#product`, `#lab`, `#open-source`

---