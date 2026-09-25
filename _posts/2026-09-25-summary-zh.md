---
layout: default
title: "Horizon Summary: 2026-09-25 (ZH)"
date: 2026-09-25
lang: zh
---

> 从 211 条内容中筛选出 14 条重要资讯。

---

**Harness 架构**
1. [Mastra 1.69.0 发布](#item-harness-arch-1) ⭐️ 8.8/10
2. [cline/cline released sdk/sdk/v0.0.86](#item-harness-arch-2) ⭐️ 8.3/10
3. [Cline Desktop v0.0.35 支持 Linux](#item-harness-arch-3) ⭐️ 6.8/10
4. [pydantic-ai v2.49.0 发布](#item-harness-arch-4) ⭐️ 6.8/10
5. [anthropics/claude-code released v2.1.282](#item-harness-arch-5) ⭐️ 6.3/10
6. [Cline v4.1.21 发布](#item-harness-arch-6) ⭐️ 6.3/10
7. [Cline CLI v3.0.65 发布](#item-harness-arch-7) ⭐️ 6.3/10
8. [video-use 用 Claude 剪视频](#item-harness-arch-8) ⭐️ 5.0/10

**Agent 工程师日报**
1. [LFM2.5-VL-DSpark 发布](#item-agent-engineer-1) ⭐️ 8.3/10
2. [Introducing Gemini 3.8 Live with Live Avatar](#item-agent-engineer-2) ⭐️ 7.8/10
3. [Qwen3.8-Flash-Next on 12GB VRAM - 65 tokens per second](#item-agent-engineer-3) ⭐️ 6.0/10

**AI 日报**
1. [AI-powered fuzzing with the GitHub Security Lab Taskflow Agent](#item-ai-daily-1) ⭐️ 8.3/10
2. [When chat is the wrong UI](#item-ai-daily-2) ⭐️ 5.8/10

**科技新闻**
1. [Simon Willison 转发鹈鹕独轮车讲解 shell 命令的 AI 视频提示词](#item-tech-news-1) ⭐️ 0.0/10

---

## Harness 架构

<a id="item-harness-arch-1"></a>
### [Mastra 1.69.0 发布](https://github.com/mastra-ai/mastra/releases/tag/%40mastra/core%401.69.0) ⭐️ 8.8/10

Mastra 1.69.0 将 classifier 提升为 core 与 workflow 的一等原语，支持在 \`new Mastra\(\{ classifiers \}\)\` 注册、管理，并作为带类型的分支步骤驱动控制流。新增 \`ClassifierProcessor\` 对 agent 输入、输出与流式内容执行策略，默认 fail-closed，可用 \`errorStrategy: &\#x27;warn&\#x27;\` 恢复 fail-open。工具层加入 \`context.background.adopt\(\)\`，允许立即返回确认并将长任务交给后台跟踪 completion/cancel，但句柄仅存内存，重启后不恢复。

github · PaulieScanlon · 9月24日 06:58

**「设计要点」** Classifier 评估通过 root \`CLASSIFIER\_EVALUATION\` span 接入可观测性；工作流中的 classifier 步骤暴露完整类型化答案与 token 用量。后台工具执行把 \`execute\(\)\` 从长阻塞中解耦，运行时需自行维护 adopted handle 的生命周期。

**「改了什么」** classifier 从零散调用变为可注册、可追踪、可编排的原语；\`ClassifierProcessor\` 把安全/路由策略下沉到 agent 输入输出与流式管道，并默认拒绝分类失败；后台工具改用 \`adopt\(\)\` 交接 completion 与 cancel，不再挂起 \`execute\(\)\`。

**标签**: `#runtime`, `#tools`, `#permissions`, `#planning`

---

<a id="item-harness-arch-2"></a>
### [cline/cline released sdk/sdk/v0.0.86](https://github.com/cline/cline/releases/tag/sdk/sdk/v0.0.86) ⭐️ 8.3/10

Cline SDK v0.0.86 adds output-token-limit recovery through forced compaction and improves local hub startup error reporting.

github · github-actions\[bot\] · 9月24日 05:43

**标签**: `#runtime`, `#tools`, `#planning`, `#eval`

---

<a id="item-harness-arch-3"></a>
### [Cline Desktop v0.0.35 支持 Linux](https://github.com/cline/cline/releases/tag/desktop-v0.0.35) ⭐️ 6.8/10

Cline Desktop v0.0.35 发布，新增 Linux x64 \`.deb\` 和 \`.rpm\` 包，使用 GTK 原生选择器，暂不提供 AppImage。插件 slash 命令改为直接执行 handler，不再作为纯文本发给模型；skills 和 workflows 菜单项来自当前会话工作区。设置新增 Diagnostics 导出，写入单个文本文件并剥离 API keys、凭证、提示和主目录路径。语音输入支持 provider 实时转录，网络中断时回退浏览器 recognizer。

github · github-actions\[bot\] · 9月24日 08:34

**「设计要点」** 桌面端通过 sidecar 和 hub 与后端协作，hub 启动失败时等待延长至 15 秒；插件 slash 命令从模型文本输入转为本地 handler 执行，诊断导出按会话 manifest 聚合日志并脱敏。

**「改了什么」** 相对 v0.0.34，新增 Linux 构建与 GTK 集成；插件 slash 命令执行路径改变，直接调用 handler；推理 effort 按 provider 持久化；模型目录扩至 6,386 个，19 个 provider 默认模型变更。

**标签**: `#runtime`, `#tools`, `#plugins`

---

<a id="item-harness-arch-4"></a>
### [pydantic-ai v2.49.0 发布](https://github.com/pydantic/pydantic-ai/releases/tag/v2.49.0) ⭐️ 6.8/10

pydantic-ai v2.49.0 发布，新增 GitHubCopilotOAuthFlow 设备授权流程，并扩展 TypeSafeModel 的结构化输出控制。BoolCriteria 可为 bool 字段指定 yes/no 语义，True/False Enum 亦可；用户对 None 的描述会作为“以上皆非”选项，非评分整数可作 Choice，可选字段与嵌套模型在该选项下回落默认值。RealtimeSession 新增 wait\_for\_reply\(\)；同时修复 OpenAI 流式 logprobs 丢失、Bedrock Converse 上 gpt-6 系列模型名与参数报错、OpenAICodexModel 延迟工具 400 等问题。

github · DouweM · 9月24日 03:09

**「设计要点」** 运行时接入 GitHub Copilot 账号改用设备授权；TypeSafeModel 用 BoolCriteria 和“以上皆非”选项收紧结构化输出边界，实时会话新增 wait\_for\_reply\(\) 同步点。

**「改了什么」** 相对 v2.48.0，能力变化集中在三点：Copilot 设备授权登录、TypeSafeModel 对 bool/None/整数/默认值的结构化输出控制、RealtimeSession 同步等待。其余为跨 provider 的兼容性修复，包括 Bedrock 模型名与采样参数、OpenAI logprobs 与延迟工具、Vertex AI 图像 fileData 传递。

**标签**: `#runtime`, `#tools`, `#permissions`

---

<a id="item-harness-arch-5"></a>
### [anthropics/claude-code released v2.1.282](https://github.com/anthropics/claude-code/releases/tag/v2.1.282) ⭐️ 6.3/10

Routine Claude Code release adding minor managed settings, telemetry diagnostics, UI polish, and a web search decryption bug fix.

github · ashwin-ant · 9月24日 18:38

**标签**: `#tools`, `#mcp`, `#permissions`, `#runtime`

---

<a id="item-harness-arch-6"></a>
### [Cline v4.1.21 发布](https://github.com/cline/cline/releases/tag/v4.1.21) ⭐️ 6.3/10

Cline v4.1.21 发布。新增日本 OpenAI 兼容 provider ai&amp;，模型目录刷新至 6,386 个模型、209 个 provider；19 个未固定模型的 provider 默认值变更，其中 11 个改为 Claude Opus 5.5。本地模型（llama.cpp、Ollama、LM Studio）触发输出上限时，Cline 会压缩对话并重试一次，压缩无效再走 concise-retry 兜底并保留部分回答。另修复 Windows @-mention 文件名、空命令输出、取消重试延迟等问题。

github · github-actions\[bot\] · 9月24日 16:16

**「设计要点」** 本地模型输出上限的处理链路：llama.cpp、Ollama、LM Studio 按剩余上下文截断生成，与用户设置的 output budget 无关。Cline 现在在任务结束前插入一次对话压缩和重试，失败后再走 concise-retry 兜底。

**「改了什么」** 相对 v4.1.20，本地模型撞到输出上限后不再直接结束任务，而是先压缩对话重试一次；失败任务重开会显示错误和重试选项，而非标记为完成。

**标签**: `#runtime`, `#memory`, `#tools`

---

<a id="item-harness-arch-7"></a>
### [Cline CLI v3.0.65 发布](https://github.com/cline/cline/releases/tag/cli-v3.0.65) ⭐️ 6.3/10

Cline CLI v3.0.65 发布，修复本地模型长会话在输出上限中断、hub 启动报错不清、会话恢复后错误信息丢失等问题。本地模型（llama.cpp、Ollama、LM Studio）在剩余上下文内截断生成，CLI 现在会压缩对话并重试一次，失败再退回简洁重试，并保留部分回答。hub 启动失败会给出具体原因，等待时间从 8 秒放宽到 15 秒，适配 Windows 安装或更新后首次启动 8–13 秒的情况。会话中的错误信息在恢复后重新出现在转录里，不再发给模型或计入压缩。

github · github-actions\[bot\] · 9月24日 05:54

**「设计要点」** 运行时上，CLI 在本地模型输出受限时先压缩再重试，hub 启动等待延长到 15 秒；插件加载失败不再每次提示都拉起沙箱，而是等 30 秒后重试。会话恢复时错误信息只进转录，不进入模型上下文，也不参与压缩计数。

**「改了什么」** 本地模型输出上限从直接失败改为压缩重试，hub 启动诊断和等待时间调整，会话错误信息与 \`cline history update --title/--prompt\` 在 hub 托管会话中改为持久化。Yolo 模式收紧输出规则，模型目录从 6,237 扩到 6,386，19 个 provider 默认模型变更，并新增 ai&amp; provider。

**标签**: `#runtime`, `#tools`

---

<a id="item-harness-arch-8"></a>
### [video-use 用 Claude 剪视频](https://github.com/browser-use/video-use) ⭐️ 5.0/10

video-use 是 browser-use 团队推出的开源视频剪辑工具，基于 Claude Code 运行。用户将原始素材放入文件夹，通过自然语言对话指示剪辑，最终得到 final.mp4。工具自动移除填充词、口误和 take 间空档，并逐段自动调色，不依赖预设或菜单，覆盖口播、混剪、教程、旅行、访谈等场景。目前可在 Browser Use Cloud 中试用。

rss · GitHub Trending Daily · 9月25日 01:06

**标签**: `#tools`, `#planning`, `#runtime`

---

## Agent 工程师日报

<a id="item-agent-engineer-1"></a>
### [LFM2.5-VL-DSpark 发布](https://huggingface.co/blog/LiquidAI/lfm2-5-vl-dspark) ⭐️ 8.3/10

LiquidAI 发布 LFM2.5-VL-DSpark，为 LFM2.5-VL-3B 提供视觉语言投机解码草稿器。草稿器增加 280M 参数，仅占目标模型 3B 参数量的 8.9%；在 M5 Max 上解码提速 2.30x–3.13x，H100 上为 2.04x–2.66x，端到端延迟分别改善 1.56x–2.62x 和 1.64x–2.27x。其沿用文本 DSpark 架构，将图像块与文本投影到共享表征后抽取隐藏状态，推理算法不变，且目标模型逐字验证草稿，贪心输出与原始模型一致。llama.cpp、MLX-VLM 和 SGLang 已首日支持，但需合入指定 PR。

rss · Hugging Face Blog · 9月24日 14:08

**「为什么重要」** 对构建 VLM Agent 的工程师，这提供了一条不改变输出分布的加速路径。同时它暴露了 VLM 推理的瓶颈转移：视觉编码与 prefill 未被加速，端到端收益受 Amdahl 定律限制，边缘设备上该约束更明显。

**「可关注」** 可关注：VLM 端到端加速比远低于解码加速比，边缘设备上 prefill 占比更高；引入草稿器前应先测量视觉编码与 prefill 耗时，再评估 8.9% 参数增长是否值得。

**标签**: `#inference`, `#vlm`, `#speculative-decoding`, `#toolchain`

---

<a id="item-agent-engineer-2"></a>
### [Introducing Gemini 3.8 Live with Live Avatar](https://deepmind.google/blog/introducing-gemini-38-live-with-live-avatar/) ⭐️ 7.8/10

Google DeepMind introduces Gemini 3.8 Live with Live Avatar, a new real-time multimodal model release.

rss · Google DeepMind · 9月24日 16:20

**标签**: `#coding-agent`, `#multimodal`, `#model-release`

---

<a id="item-agent-engineer-3"></a>
### [Qwen3.8-Flash-Next on 12GB VRAM - 65 tokens per second](https://www.reddit.com/r/LocalLLaMA/comments/1wp7zyb/qwen38flashnext_on_12gb_vram_65_tokens_per_second/) ⭐️ 6.0/10

A custom inference engine claims 65 tok/s output on 12GB VRAM for Qwen3.8-Flash-Next with specific quantization and memory trade-offs.

reddit · r/LocalLLaMA · /u/KnownAd4832 · 9月24日 17:30

**标签**: `#harness`, `#eval`, `#local-inference`

---

## AI 日报

<a id="item-ai-daily-1"></a>
### [AI-powered fuzzing with the GitHub Security Lab Taskflow Agent](https://github.blog/security/application-security/ai-powered-fuzzing-with-the-github-security-lab-taskflow-agent/) ⭐️ 8.3/10

GitHub Security Lab launches an AI-powered fuzzing taskflow via its Taskflow Agent framework, adding automated security testing capabilities.

rss · GitHub Blog · 9月24日 18:26

**标签**: `#product`, `#open-source`, `#lab`, `#industry`

---

<a id="item-ai-daily-2"></a>
### [When chat is the wrong UI](https://github.blog/ai-and-ml/github-copilot/when-chat-is-the-wrong-ui/) ⭐️ 5.8/10

GitHub Blog post argues that canvases offer a more tangible UI than chat boxes for developers, in the context of GitHub Copilot.

rss · GitHub Blog · 9月24日 20:00

**标签**: `#product`, `#lab`

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [Simon Willison 转发鹈鹕独轮车讲解 shell 命令的 AI 视频提示词](https://twitter.com/simonw/status/tweet-2103264194158338480) ⭐️ 0.0/10

Simon Willison 转发了一条推文，其中 @goodside 分享了一段提示词，要求生成一段 30 秒动画视频，让一只骑独轮车的鹈鹕用合成语音解释 shell 命令 \`w \| t...\`。该内容展示了文本到视频与语音合成技术在创意演示中的结合，但缺乏技术细节、详细分析或行业影响证据。目前它仅作为社交媒体上的创意示例流传，属于社区层面的低影响力内容。

twitter · Simon Willison · 9月24日 23:23

**「背景」** 文本到视频生成与语音合成是当前生成式 AI 的常见应用方向，该推文以趣味提示词的形式展示了二者的结合。

**标签**: `#AI video generation`, `#shell scripting`, `#Simon Willison`, `#social media`, `#text-to-video`

---