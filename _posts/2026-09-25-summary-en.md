---
layout: default
title: "Horizon Summary: 2026-09-25 (EN)"
date: 2026-09-25
lang: en
---

> From 211 items, 14 important content pieces were selected

---

**Agent Harness Architecture**
1. [Mastra 1.69.0 发布](#item-harness-arch-1) ⭐️ 8.8/10
2. [cline/cline released sdk/sdk/v0.0.86](#item-harness-arch-2) ⭐️ 8.3/10
3. [Cline 桌面版 v0.0.35 发布](#item-harness-arch-3) ⭐️ 6.8/10
4. [pydantic-ai v2.49.0 发布](#item-harness-arch-4) ⭐️ 6.8/10
5. [anthropics/claude-code released v2.1.282](#item-harness-arch-5) ⭐️ 6.3/10
6. [Cline v4.1.21 发布](#item-harness-arch-6) ⭐️ 6.3/10
7. [Cline CLI v3.0.65 发布](#item-harness-arch-7) ⭐️ 6.3/10
8. [video-use 开源：对话剪视频](#item-harness-arch-8) ⭐️ 5.0/10

**AI Agent Engineer**
1. [LFM2.5-VL-DSpark 正式发布](#item-agent-engineer-1) ⭐️ 8.3/10
2. [Introducing Gemini 3.8 Live with Live Avatar](#item-agent-engineer-2) ⭐️ 7.8/10
3. [Qwen3.8-Flash-Next on 12GB VRAM - 65 tokens per second](#item-agent-engineer-3) ⭐️ 6.0/10

**AI Daily**
1. [AI-powered fuzzing with the GitHub Security Lab Taskflow Agent](#item-ai-daily-1) ⭐️ 8.3/10
2. [When chat is the wrong UI](#item-ai-daily-2) ⭐️ 5.8/10

**Technology News**
1. [Simon Willison retweets AI video prompt featuring pelican explaining shell command](#item-tech-news-1) ⭐️ 0.0/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [Mastra 1.69.0 发布](https://github.com/mastra-ai/mastra/releases/tag/%40mastra/core%401.69.0) ⭐️ 8.8/10

Mastra 1.69.0 把分类器提升为 core 与 workflow 的一等原语：可在 \`new Mastra\(\{ classifiers \}\)\` 注册，用 \`getClassifier\`、\`listClassifiers\`、\`addClassifier\`、\`removeClassifier\` 管理，无活跃 trace 的评估会自动起根 \`CLASSIFIER\_EVALUATION\` span。新增 \`ClassifierProcessor\` 对 agent 输入、输出和流式内容施加分类策略，默认 fail-closed，分类器失败即 abort；设 \`errorStrategy: &\#x27;warn&\#x27;\` 才回到旧 fail-open。工具层新增 \`context.background.adopt\(\)\`，\`execute\(\)\` 可立即返回确认，把长时操作的完成与取消交给原生后台跟踪，但句柄只在内存，进程重启后不恢复。

github · PaulieScanlon · Sep 24, 06:58

**「设计要点」** 分类器既是运行时原语也是工作流步骤，能在 fluent/dynamic graph 里做类型化分支，并给出完整答案与 token 用量。\`ClassifierProcessor\` 把安全/路由门控前移到 agent 输入输出与流式管道，用显式 abort 收口权限。

**「改了什么」** 分类器从零变成可注册、可追踪、可嵌入工作流的核心能力。后台工具从必须挂起 \`execute\(\)\` 等结果，改为 adopt 句柄后立即返回。Inngest durable run 新增 \`retries\`，并修复 resume 时缺快照失败的问题。

**Tags**: `#runtime`, `#tools`, `#permissions`, `#planning`

---

<a id="item-harness-arch-2"></a>
### [cline/cline released sdk/sdk/v0.0.86](https://github.com/cline/cline/releases/tag/sdk/sdk/v0.0.86) ⭐️ 8.3/10

Cline SDK v0.0.86 adds output-token-limit recovery through forced compaction and improves local hub startup error reporting.

github · github-actions\[bot\] · Sep 24, 05:43

**Tags**: `#runtime`, `#tools`, `#planning`, `#eval`

---

<a id="item-harness-arch-3"></a>
### [Cline 桌面版 v0.0.35 发布](https://github.com/cline/cline/releases/tag/desktop-v0.0.35) ⭐️ 6.8/10

Cline Desktop v0.0.35 发布，桌面端首次支持 Linux，每个版本提供 x64 \`.deb\` 和 \`.rpm\` 包，暂不提供 AppImage。插件斜杠命令改为直接执行插件注册的 handler，不再把命令当纯文本发给模型；斜杠菜单中的技能和工作流改为从当前会话的工作区（含 worktree）读取。设置页新增 Diagnostics 导出，会把应用版本、系统、设置、sidecar 与 hub 日志及所选会话 manifest 写入 Downloads 下的单个文本文件，并剥离 API key、凭证样式值、提示词和 home 目录路径。

github · github-actions\[bot\] · Sep 24, 08:34

**「设计要点」** 工具层上，插件 slash command 从“文本透传”变为“本地 handler 执行”，仅在命令需要时才开启模型回合；单个插件损坏不再导致所有 slash 提示失败。诊断导出在权限与隐私上做了字段级 redaction，明确排除密钥、凭证、提示词和用户 home 路径，可直接附到 GitHub issue。

**「改了什么」** 相比 desktop-v0.0.34，这一版补齐了 Linux 桌面运行时、修复了插件斜杠命令的执行路径，并新增了可安全外发的诊断导出。推理强度选择改为按 provider 持久化，切换 provider 时应用上次所选 effort；本地模型在触达 output-token 上限时会压缩对话并重试一次，不再直接失败。

**Tags**: `#runtime`, `#tools`, `#plugins`

---

<a id="item-harness-arch-4"></a>
### [pydantic-ai v2.49.0 发布](https://github.com/pydantic/pydantic-ai/releases/tag/v2.49.0) ⭐️ 6.8/10

pydantic-ai v2.49.0 adds GitHub Copilot device OAuth via \`GitHubCopilotOAuthFlow\`, extends \`TypeSafeModel\` with \`BoolCriteria\` and improved \`None\`/numeric choice handling, and introduces \`RealtimeSession.wait\_for\_reply\(\)\`. The release also fixes OpenAI logprob streaming, Bedrock model-name and parameter handling, and realtime error propagation. Changes are incremental, targeting structured-output reliability and provider compatibility rather than core architecture.

github · DouweM · Sep 24, 03:09

**「设计要点」** The OAuth flow and realtime session method touch the tool and runtime layers: device authorization is added as a first-class flow, while \`wait\_for\_reply\(\)\` gives realtime consumers a synchronous handle on asynchronous audio streams. \`TypeSafeModel\` changes refine how structured outputs map optional and numeric fields to model choices.

**「改了什么」** Versus v2.48.0, the release adds Copilot device OAuth, \`BoolCriteria\`, \`RealtimeSession.wait\_for\_reply\(\)\`, and several \`TypeSafeModel\` structured-output improvements. It also fixes Bedrock Converse compatibility for GPT-5.6/GPT-6 and new \`gpt-6-\*\` models, preserves streamed OpenAI logprobs, and surfaces realtime receive-side failures to all consumer shapes.

**Tags**: `#runtime`, `#tools`, `#permissions`

---

<a id="item-harness-arch-5"></a>
### [anthropics/claude-code released v2.1.282](https://github.com/anthropics/claude-code/releases/tag/v2.1.282) ⭐️ 6.3/10

Routine Claude Code release adding minor managed settings, telemetry diagnostics, UI polish, and a web search decryption bug fix.

github · ashwin-ant · Sep 24, 18:38

**Tags**: `#tools`, `#mcp`, `#permissions`, `#runtime`

---

<a id="item-harness-arch-6"></a>
### [Cline v4.1.21 发布](https://github.com/cline/cline/releases/tag/v4.1.21) ⭐️ 6.3/10

Cline v4.1.21 发布，新增日本区 OpenAI 兼容 provider ai&amp;，模型目录刷新至 6,386 个模型、209 个 provider。未固定默认模型的 19 个 provider 中有 11 个切到 Claude Opus 5.5，包括 GitHub Copilot 和 Vertex。本地模型（llama.cpp、Ollama、LM Studio）触发输出上限时，harness 会压缩对话并重试一次，不再直接结束任务。另外修复了失败任务重开、空命令输出、Windows @-mention 文件名和取消重试等待等问题。

github · github-actions\[bot\] · Sep 24, 16:16

**「设计要点」** 本地模型服务端按剩余上下文截断生成，与 output budget 无关；Cline 的恢复路径是先 compact 再 concise-retry，并保留部分答案。

**「改了什么」** 相对 v4.1.20，本地模型长回复触顶后新增压缩并重试的恢复路径，模型默认值批量刷新；其余为 provider 新增、js-yaml 安全版本提升和交互修复。

**Tags**: `#runtime`, `#memory`, `#tools`

---

<a id="item-harness-arch-7"></a>
### [Cline CLI v3.0.65 发布](https://github.com/cline/cline/releases/tag/cli-v3.0.65) ⭐️ 6.3/10

Cline CLI v3.0.65 发布，修复本地模型长会话在输出上限中断、hub 启动报错不清、会话恢复后错误丢失等问题。llama.cpp、Ollama、LM Studio 会在剩余上下文内截断生成，CLI 现在压缩对话并重试一次，失败再退回简洁重试，保留部分回答。hub 启动失败会给出具体原因，等待时间从 8 秒放宽到 15 秒，覆盖 Windows 安装或更新后首次启动 8–13 秒的情况。会话中的错误信息在恢复后重新出现在 transcript，不再发给模型或计入 compaction。

github · github-actions\[bot\] · Sep 24, 05:54

**「设计要点」** 运行时上，本地模型输出受限时先压缩再重试；hub 启动失败输出原因并延长等待；插件加载失败不再每次 prompt 都拉起 sandbox，而是 30 秒后重试。错误消息只进 transcript，不进入模型上下文，也不参与 compaction 计数。

**「改了什么」** 相对 cli-v3.0.64，本地模型输出上限从直接失败改为压缩重试；hub 启动诊断和等待时间调整；错误消息与 \`cline history update\` 的 title/prompt 在 hub 托管会话中跨恢复持久化；Yolo 模式收紧输出规则；新增 ai&amp; provider；模型目录从 6,237 扩到 6,386，19 个 provider 默认模型变更。

**Tags**: `#runtime`, `#tools`

---

<a id="item-harness-arch-8"></a>
### [video-use 开源：对话剪视频](https://github.com/browser-use/video-use) ⭐️ 5.0/10

browser-use 开源 video-use，把视频剪辑搬进 Claude Code。原始素材丢进文件夹，对话下达指令，Claude Code 自动切掉 filler words、false starts 和 take 间死区，逐段自动调色，输出 final.mp4。不设预设和菜单，talking heads、montages、tutorials、travel、interviews 都能直接处理。可在 Browser Use Cloud 试用。

rss · GitHub Trending Daily · Sep 25, 01:06

**Tags**: `#tools`, `#planning`, `#runtime`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [LFM2.5-VL-DSpark 正式发布](https://huggingface.co/blog/LiquidAI/lfm2-5-vl-dspark) ⭐️ 8.3/10

LiquidAI 发布 LFM2.5-VL-DSpark，为 LFM2.5-VL-3B 提供投机解码 drafter，增加 280M 参数（8.9%）。在 M5 Max 上解码提速 2.30x 到 3.13x，H100 上为 2.04x 到 2.66x；端到端延迟分别改善 1.56x 到 2.62x 与 1.64x 到 2.27x。该 drafter 沿用文本 DSpark 架构，在固定 tapped layers 捕获隐状态，将图像 patch 与文本 token 投影到同一表示后生成候选块，推理算法不变；llama.cpp、MLX-VLM 和 SGLang 已首日支持，模型提供 Safetensors 与 GGUF 格式。投机解码仅加速 decode，视觉编码与 prefill 不在范围内，端到端收益受 Amdahl 定律限制。

rss · Hugging Face Blog · Sep 24, 14:08

**「为什么重要」** 对构建 VLM agent 的工程师而言，这提供了即插即用的推理优化路径：drafter 仅增加 8.9% 参数，主流框架已首日集成，可在边缘设备与数据中心 GPU 上获得 2–3 倍解码加速。文章同时明确划定加速边界——视觉编码与 prefill 未被加速，端到端增益受非解码阶段制约，为评估真实部署收益提供依据。

**「可关注」** 可关注：LFM2.5-VL-DSpark 的推理算法与文本 DSpark 一致，图像与文本在 tapped layers 之前已投影到同一隐状态空间，现有文本投机解码工具链可低成本迁移到 VLM；目标模型会验证每个候选 token，贪心输出与单独运行目标模型一致，但需按硬件选择 block size 8 或 9，并预期端到端提速会显著低于纯解码提速。

**Tags**: `#inference`, `#vlm`, `#speculative-decoding`, `#toolchain`

---

<a id="item-agent-engineer-2"></a>
### [Introducing Gemini 3.8 Live with Live Avatar](https://deepmind.google/blog/introducing-gemini-38-live-with-live-avatar/) ⭐️ 7.8/10

Google DeepMind introduces Gemini 3.8 Live with Live Avatar, a new real-time multimodal model release.

rss · Google DeepMind · Sep 24, 16:20

**Tags**: `#coding-agent`, `#multimodal`, `#model-release`

---

<a id="item-agent-engineer-3"></a>
### [Qwen3.8-Flash-Next on 12GB VRAM - 65 tokens per second](https://www.reddit.com/r/LocalLLaMA/comments/1wp7zyb/qwen38flashnext_on_12gb_vram_65_tokens_per_second/) ⭐️ 6.0/10

A custom inference engine claims 65 tok/s output on 12GB VRAM for Qwen3.8-Flash-Next with specific quantization and memory trade-offs.

reddit · r/LocalLLaMA · /u/KnownAd4832 · Sep 24, 17:30

**Tags**: `#harness`, `#eval`, `#local-inference`

---

## AI Daily

<a id="item-ai-daily-1"></a>
### [AI-powered fuzzing with the GitHub Security Lab Taskflow Agent](https://github.blog/security/application-security/ai-powered-fuzzing-with-the-github-security-lab-taskflow-agent/) ⭐️ 8.3/10

GitHub Security Lab launches an AI-powered fuzzing taskflow via its Taskflow Agent framework, adding automated security testing capabilities.

rss · GitHub Blog · Sep 24, 18:26

**Tags**: `#product`, `#open-source`, `#lab`, `#industry`

---

<a id="item-ai-daily-2"></a>
### [When chat is the wrong UI](https://github.blog/ai-and-ml/github-copilot/when-chat-is-the-wrong-ui/) ⭐️ 5.8/10

GitHub Blog post argues that canvases offer a more tangible UI than chat boxes for developers, in the context of GitHub Copilot.

rss · GitHub Blog · Sep 24, 20:00

**Tags**: `#product`, `#lab`

---

## Technology News

<a id="item-tech-news-1"></a>
### [Simon Willison retweets AI video prompt featuring pelican explaining shell command](https://twitter.com/simonw/status/tweet-2103264194158338480) ⭐️ 0.0/10

Simon Willison retweeted a prompt from @goodside asking for a 30-second animated video with synthesized voice, featuring an animated pelican on a unicycle that explains a shell command beginning with \`w \| t\`. The retweeted text is truncated, so the full command and any resulting video are not visible. The item is a social media share of a creative text-to-video prompt rather than a product release or technical analysis.

twitter · Simon Willison · Sep 24, 23:23

**「Background」** Text-to-video AI tools are frequently demonstrated through whimsical or educational prompts shared on social media, and such posts often circulate without the full prompt, output, or technical context needed for independent evaluation.

**Tags**: `#AI video generation`, `#shell scripting`, `#Simon Willison`, `#social media`, `#text-to-video`

---