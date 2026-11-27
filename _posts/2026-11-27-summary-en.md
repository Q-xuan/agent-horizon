---
layout: default
title: "Horizon Summary: 2026-11-27 (EN)"
date: 2026-11-27
lang: en
---

> From 177 items, 6 important content pieces were selected

---

**Agent Harness Architecture**
1. [pydantic-ai v2.76.0 发布](#item-harness-arch-1) ⭐️ 7.8/10
2. [@e2b/acp 0.1.0 发布](#item-harness-arch-2) ⭐️ 7.8/10
3. [Instructor v1.18.0 发布](#item-harness-arch-3) ⭐️ 5.8/10

**AI Agent Engineer**
1. [llama.cpp AMD 基准仪表盘上线](#item-agent-engineer-1) ⭐️ 6.8/10
2. [HF Daily Paper：编码智能体视觉推理研究](#item-agent-engineer-2) ⭐️ 6.0/10
3. [OS-Omni v1 跨平台智能体基准发布](#item-agent-engineer-3) ⭐️ 5.5/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [pydantic-ai v2.76.0 发布](https://github.com/pydantic/pydantic-ai/releases/tag/v2.76.0) ⭐️ 7.8/10

pydantic-ai v2.76.0 发布，新增实时会话中途工具更新能力，通过 \`UpdateTools\` 类型与 \`RealtimeModelProfile.supports\_tool\_updates\` 标志控制。对 \`RealtimeInput\` 的穷尽类型检查需显式处理 \`UpdateTools\` 分支，否则类型检查失败。\`gemini-2.5-pro\` 与 \`gemini-2.5-flash\` 请求现在触发 \`DeprecatedModelWarning\`。此外新增 \`GoogleInteractionsModel\`、\`CodeMode\(allow\_final\_output=True\)\` 及 per-tool \`ui\_visibility\` 等特性。

github · dsfaccini · Nov 26, 23:49

**「改了什么」** 相对 v2.75.0，新增实时会话中途工具更新能力，但破坏性调整了 \`RealtimeInput\` 的穷尽类型检查。\`gemini-2.5-pro\` 和 \`gemini-2.5-flash\` 请求现在触发 \`DeprecatedModelWarning\`，\`FileSystem.read\_file\` 的 \`offset\` 改为 1 索引且 \`offset=0\` 抛出异常。

**Tags**: `#tools`, `#runtime`

---

<a id="item-harness-arch-2"></a>
### [@e2b/acp 0.1.0 发布](https://github.com/e2b-dev/E2B/releases/tag/%40e2b/acp%400.1.0) ⭐️ 7.8/10

E2B 发布 @e2b/acp 0.1.0，支持在 E2B sandbox 内运行 ACP 兼容 agent（goose、OpenCode、Claude Code 通过 ACP adapter）。核心接口 \`new ACPAgent\(sandbox, command, client\)\` 加 \`await agent.start\(\)\` 通过 stdin/stdout 启动 agent。客户端文件系统与终端能力被关闭，agent 请求这些能力时直接拒绝，强制使用 sandbox 内建工具。依赖升级至 e2b@2.65.0。

github · github-actions\[bot\] · Nov 26, 12:35

**「设计要点」** 运行时通过 stdin/stdout 管道连接 agent 与 ACP client。客户端文件系统与终端能力被关闭，agent 请求这些能力时直接拒绝。

**「改了什么」** 新增 @e2b/acp 包，提供 ACPAgent API 在 sandbox 内托管 ACP 兼容 agent。强制关闭客户端文件系统与终端能力，拒绝 agent 对这些能力的请求。

**Tags**: `#sandbox`, `#runtime`, `#permissions`, `#mcp`

---

<a id="item-harness-arch-3"></a>
### [Instructor v1.18.0 发布](https://github.com/567-labs/instructor/releases/tag/v1.18.0) ⭐️ 5.8/10

Instructor v1.18.0 发布，修复缓存映射键冲突，并将 v2 令牌预算策略与重试执行分离。Bedrock、Gemini、Anthropic、OpenAI 等提供方获得工具调用保留、JSON 准备、thinking 默认值等修正，流式传输与批处理亦有修复。该版本未新增 agent harness 协议或架构能力，对基础设施工程师的直接参考价值有限。

github · jxnl · Nov 26, 21:02

**「设计要点」** 缓存层将运行时响应序列化与键生成分离，v2 重试路径将令牌预算策略从执行层解耦。两者均为内部重构，不改变公共接口或运行时模型。

**「改了什么」** 修复缓存键冲突，避免多模型缓存污染。v2 路径分离令牌预算策略与重试执行逻辑。各提供方修正工具调用传递、JSON 准备、thinking 默认值等边界行为。流式传输修复 Unicode 控制字符保留、字段别名解析及最后有效 JSON 选择。安全策略将原始响应日志改为显式 opt-in。

**Tags**: `#cache`, `#runtime`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [llama.cpp AMD 基准仪表盘上线](https://huggingface.co/blog/ggml-org/llamacpp-amd-bench) ⭐️ 6.8/10

2026年11月26日Hugging Face发布公开的llama.cpp基准测试仪表盘，面向AMD Ryzen和Radeon硬件用户，支持对比不同构建、模型、量化下的推理性能，基准工作流与原始结果完全公开。当前仪表盘支持的硬件为Radeon 8060S（gfx1151）和Radeon AI Pro R9700S（gfx1201），测试项包含PP512（512输入token处理，无生成）与TG128（128 token生成，无预存上下文），均从上下文深度0开始测量平均吞吐量（tokens/秒）。该工具主要服务于AMD平台的本地推理开发者，可公开复现所有测试结果。

rss · Hugging Face Blog · Nov 26, 11:37

**「为什么重要」** 该仪表盘首次公开了AMD平台上llama.cpp的标准化推理基准数据，解决了此前该场景下性能数据分散、难复现的问题，为评估本地推理栈提供了可对比的参考。目前其影响仅限AMD+llama.cpp的使用场景，未覆盖更广泛的硬件或推理框架。

**「可关注」** 可关注：仪表盘数据直接来自公开的ggml-org/install.sh-benches-data存储桶，基准使用llama-bench工具、每周自动运行、Flash Attention开/关各测10次，可直接复用数据做自定义对比或本地复现。

**Tags**: `#eval`

---

<a id="item-agent-engineer-2"></a>
### [HF Daily Paper：编码智能体视觉推理研究](https://huggingface.co/papers/2611.34813) ⭐️ 6.0/10

2026-11-27，Hugging Face Daily Papers 收录论文 2611.34813，提出用编码智能体替代视频生成模型做视觉推理。研究在相同输入、输出规范与规则式评估器下，对比两种范式：视频生成模型直接生成帧序列，编码智能体编写程序渲染答案视频。论文引入 VBVR-Pro-Bench 基准，声称编码智能体是更强视觉推理器，但当前摘要未披露具体性能数字或实现细节。

rss · Hugging Face Daily Papers · Nov 27, 00:00

**「为什么重要」** 该研究提出符号化（代码）替代原生像素生成的视觉推理路径，若结论成立，可能影响视觉推理系统的架构选型与评估标准设计。但需注意当前摘要未提供可验证的性能对比数据。

**「可关注」** VBVR-Pro-Bench 基准将代码生成输出与视频生成输出置于同一规则式评估器下比较，这种评估设计可复用于后续视觉推理系统的公平对比。

**Tags**: `#coding-agent`, `#eval`

---

<a id="item-agent-engineer-3"></a>
### [OS-Omni v1 跨平台智能体基准发布](https://huggingface.co/papers/2611.34232) ⭐️ 5.5/10

2026年11月27日Hugging Face Daily Papers公开OS-Omni跨平台计算机使用智能体基准介绍摘要。v1版本覆盖Windows、Ubuntu、macOS、iOS、Android、Web共6个平台，每个平台提供48个任务，另包含12组桌面与安卓手机配对的跨平台工作流。当前公开内容被截断，未披露完整技术细节、性能对比数据与可复现初始化设置，该基准面向计算机使用智能体评估需求，主要服务智能体研发与评测方向的工程师、研究者。

rss · Hugging Face Daily Papers · Nov 27, 00:00

**「为什么重要」** 现有计算机使用智能体基准多针对单一环境设计，无法验证智能体跨平台长时程工作流的通用能力，OS-Omni首次覆盖6类平台的统一评估场景，填补了该方向的基准空白。

**「可关注」** 可关注：OS-Omni v1 的跨平台工作流任务设计，以及后续公开的完整可复现评估配置。

**Tags**: `#eval`, `#coding-agent`, `#orchestration`

---