---
layout: default
title: "Horizon Summary: 2026-09-30 (EN)"
date: 2026-09-30
lang: en
---

> From 210 items, 20 important content pieces were selected

---

**Agent Harness Architecture**
1. [openai/codex released rust-v0.159.0](#item-harness-arch-1) ⭐️ 8.3/10
2. [Cline SDK v0.0.87 发布](#item-harness-arch-2) ⭐️ 6.3/10
3. [google-gemini/gemini-cli released v0.63.0-preview.0](#item-harness-arch-3) ⭐️ 6.3/10
4. [2.1.285](#item-harness-arch-4) ⭐️ 6.3/10
5. [openai/codex released rust-v0.159.1](#item-harness-arch-5) ⭐️ 5.8/10
6. [google-gemini/gemini-cli released v0.62.0](#item-harness-arch-6) ⭐️ 5.8/10

**AI Agent Engineer**
1. [Getting the Source Right, Not Just the Fact: Source-Aware Verification for MCP Agents](#item-agent-engineer-1) ⭐️ 8.3/10
2. [Apple 提出表达式序列化往返评测协议](#item-agent-engineer-2) ⭐️ 8.3/10
3. [TraceDance Builds Behavior Benchmarks from Deployment Traces](#item-agent-engineer-3) ⭐️ 8.0/10
4. [HF daily paper: Knowing When Thinking Is Not Enough: Teaching Small Reasoning Models to Reason Beyond Their Parametric Knowledge](#item-agent-engineer-4) ⭐️ 8.0/10
5. [GLM-5.3 端到端漏洞利用能力扩散](#item-agent-engineer-5) ⭐️ 7.8/10
6. [GPT 6.1 Sol: Near-Astra intelligence for a fifth of the price](#item-agent-engineer-6) ⭐️ 6.0/10
7. [OpenAI DevDay 2026 引争议](#item-agent-engineer-7) ⭐️ 5.5/10
8. [GLM-5.3 实现二进制控制流劫持](#item-agent-engineer-8) ⭐️ 5.5/10
9. [Qwen3.8-Flash-Next 量化版发布](#item-agent-engineer-9) ⭐️ 5.5/10

**AI Daily**
1. [OpenAI DevDay 2026 回顾](#item-ai-daily-1) ⭐️ 10.0/10
2. [OpenAI 发布 GPT-6.1 Sol](#item-ai-daily-2) ⭐️ 8.8/10
3. [Asana 让 Claude 当 AI 队友](#item-ai-daily-3) ⭐️ 8.3/10
4. [OpenAI 发布主动助手 dots](#item-ai-daily-4) ⭐️ 6.8/10
5. [GitHub 更新开发者政策与透明度数据](#item-ai-daily-5) ⭐️ 6.8/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [openai/codex released rust-v0.159.0](https://github.com/openai/codex/releases/tag/rust-v0.159.0) ⭐️ 8.3/10

Codex Rust v0.159.0 introduces opt-in instant interrupt steering, app-server thread-history pagination, and Windows MCP/code-mode launch fixes.

github · github-actions\[bot\] · Sep 29, 08:05

**Tags**: `#runtime`, `#tools`, `#mcp`, `#sandbox`

---

<a id="item-harness-arch-2"></a>
### [Cline SDK v0.0.87 发布](https://github.com/cline/cline/releases/tag/sdk/sdk/v0.0.87) ⭐️ 6.3/10

Cline SDK v0.0.87 修复 Windows 下 hub 启动与 token 统计问题。Bun fetch 会把 loopback 请求送入 HTTP\(S\)\_PROXY，导致健康探测失败；新版在代理变量存在时向 NO\_PROXY 注入 loopback 地址，并识别 Windows \`B:\\~BUN\\\` 内嵌路径以正确派生 daemon。\`normalizeUsage\(\)\` 不再把 reasoning token 重复计入 outputTokens，成本仍按完整总量计算。Bedrock 路由、模型目录与 PHP 代码检索同步更新。

github · github-actions\[bot\] · Sep 29, 05:30

**「设计要点」** hub 客户端在每次探测、drain 和 shutdown 前调用 \`ensureLoopbackProxyBypass\(\)\`；daemon 逐条记录 socket 关闭码与原因，EADDRINUSE 时输出占用者 PID 与命令行。Gateway 模型保留 per-model \`apiProtocol\`，避免回退到 provider 默认 API。

**「改了什么」** 相对 v0.0.86，hub 在系统代理下可启动，reasoning token 不再双计，Bedrock 裸 OpenAI 模型 ID 走 inference profile，模型目录扩到 211 家 provider、6,447 个模型。

**Tags**: `#runtime`, `#tools`

---

<a id="item-harness-arch-3"></a>
### [google-gemini/gemini-cli released v0.63.0-preview.0](https://github.com/google-gemini/gemini-cli/releases/tag/v0.63.0-preview.0) ⭐️ 6.3/10

Gemini CLI v0.63.0-preview.0 ships bug fixes including bounded tool output and memory lifecycle optimizations for long-running agent loops.

github · gemini-cli-robot · Sep 29, 20:58

**Tags**: `#runtime`, `#memory`, `#mcp`, `#tools`

---

<a id="item-harness-arch-4"></a>
### [2.1.285](https://code.claude.com/docs/en/changelog#2-1-285) ⭐️ 6.3/10

Claude Code 2.1.285 introduces incremental tool, MCP, and permission conveniences including a WebFetch kill switch, desktop integration, plugin config commands, and a managed provider allowlist.

rss · Claude Code Changelog · Sep 29, 19:37

**Tags**: `#tools`, `#mcp`, `#permissions`, `#runtime`

---

<a id="item-harness-arch-5"></a>
### [openai/codex released rust-v0.159.1](https://github.com/openai/codex/releases/tag/rust-v0.159.1) ⭐️ 5.8/10

Codex Rust v0.159.1 backports GPT-6.1 Sol as the default model in bundled and Bedrock catalogs.

github · github-actions\[bot\] · Sep 29, 20:32

**Tags**: `#runtime`, `#models`, `#catalog`

---

<a id="item-harness-arch-6"></a>
### [google-gemini/gemini-cli released v0.62.0](https://github.com/google-gemini/gemini-cli/releases/tag/v0.62.0) ⭐️ 5.8/10

Routine gemini-cli v0.62.0 patch release with minor fixes to MCP tool title formatting, OAuth token retention, A2A server handling, and UI rendering.

github · gemini-cli-robot · Sep 29, 21:17

**Tags**: `#mcp`, `#tools`, `#runtime`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [Getting the Source Right, Not Just the Fact: Source-Aware Verification for MCP Agents](https://huggingface.co/blog/MultiverseComputingCAI/getting-the-source-right-not-just-the-fact-source) ⭐️ 8.3/10

Hugging Face introduces ProvenanceGuard, a source-aware verification approach for MCP agents designed to catch cross-source conflation where a fact exists in the evidence pool but is attributed to the wrong source.

rss · Hugging Face Blog · Sep 29, 13:07

**Tags**: `#eval`, `#mcp`, `#observability`, `#harness`

---

<a id="item-agent-engineer-2"></a>
### [Apple 提出表达式序列化往返评测协议](https://machinelearning.apple.com/research/communication-bottleneck-serialization) ⭐️ 8.3/10

2026 年 9 月 29 日，Apple Machine Learning Research 提出往返评测协议，以符号等价作精确 oracle，量化自然语言序列化中树结构组合信息的损失。协议将程序化生成的算术表达式转为文字题，再由独立提取器仅从文字题恢复表达式，并成对评测 16 个模型。材料未给出具体数值结果。

rss · Apple Machine Learning Research · Sep 29, 00:00

**「为什么重要」** 该协议把模型间自由文本交换的结构信息损失变成可复现度量，为依赖链式思考或中间文本传递的 agent 编排与 harness 设计提供新评估角度。

**「可关注」** 可关注：符号等价 oracle 让序列化损失可精确度量，可为 harness 中间表示与 agent 通信协议选型提供依据。

**Tags**: `#eval`, `#harness`, `#orchestration`

---

<a id="item-agent-engineer-3"></a>
### [TraceDance Builds Behavior Benchmarks from Deployment Traces](https://huggingface.co/papers/2609.33295) ⭐️ 8.0/10

Hugging Face Daily Papers featured TraceDance on 2026-09-29, garnering 60 upvotes. The system automatically constructs targeted benchmarks for user-specified undesirable agent behaviors from real-world deployment traces. Anchor-and-Confirm combines programmable retrieval with candidate-level confirmation by a Flash LLM, while the Anchor Synthesis Loop generates and revises specifications for custom behaviors. The benchmarks use decision-point continuation to evaluate an LLM&\#x27;s next turn at a recorded decision point with a behavior-specific rubric, requiring no reference answer or environment replay. Experiments span coding and general tasks.

rss · Hugging Face Daily Papers · Sep 29, 00:00

**「Why It Matters」** Agents can complete tasks while exhibiting undesirable behavior during execution. Fixed benchmark suites do not cover the specific behaviors developers encounter in deployment. TraceDance generates tests directly from production traces, closing the gap between task completion and execution quality.

**「Focus」** Decision-point continuation evaluates next-turn behavior at recorded trace points without environment replay, offering a lightweight path to test undesirable behaviors beyond fixed suites.

**Tags**: `#eval`, `#coding-agent`, `#observability`, `#harness`

---

<a id="item-agent-engineer-4"></a>
### [HF daily paper: Knowing When Thinking Is Not Enough: Teaching Small Reasoning Models to Reason Beyond Their Parametric Knowledge](https://huggingface.co/papers/2609.34327) ⭐️ 8.0/10

This paper identifies when small reasoning models should stop self-refining and instead query external knowledge, introducing a selective querying framework based on execution versus knowledge bottlenecks.

rss · Hugging Face Daily Papers · Sep 29, 00:00

**Tags**: `#orchestration`, `#eval`, `#coding-agent`, `#harness`

---

<a id="item-agent-engineer-5"></a>
### [GLM-5.3 端到端漏洞利用能力扩散](https://www.anthropic.com/research/glm-5-3-and-the-spread-of-advanced-cyber-capabilities) ⭐️ 7.8/10

Anthropic Frontier Red Team 评估 GLM-5.3，确认其可自主构建端到端网络漏洞利用，且安全限制能被简单技术绕过。在 ExploitBench 的 V8 引擎测试中，GLM-5.3 于 410 次尝试内成功 50 次，接近 Claude Mythos Preview 的 56 次；内部二进制利用基准上，完整控制流劫持成功率为 4%，低于 Claude Mythos Preview 的 6%，但已越过 Claude Opus 4.6 与 GLM-5.2 零成功的门槛。人类专家测试中，GLM-5.3 在一天内发现一款流行浏览器 Linux 构建的 JavaScript 引擎多个未知漏洞并链接成任意文件读取利用；GLM-5.3-Flash 用 20 分钟人工关注与 8 小时模型运行、约 20.40 美元成本，绕过 ARM64 PAC 硬化构建 Chrome CVE-2026-11645 利用链。GLM-5.3 以开放权重发布，简单技术可在 64% 到 100% 的模拟测试中绕过其安全限制；abliteration 可将拒答率从 90% 以上降至 3%（JailbreakBench、HarmBench）或 12%（StrongREJECT），且 GPQA-Diamond 得分不变。

rss · Anthropic Research · Sep 29, 00:00

**「为什么重要」** NIST CAISI 9 月 17 日评估称 GLM-5.3 是“迄今最具网络能力的开放权重模型”，聚合网络基准落后美国前沿约四个月。美国高能力模型多仅向受审核用户开放，而 GLM-5.3 任何人可下载，且安全限制可被 abliteration 移除，攻击者获取门槛显著降低。

**「可关注」** 可关注：开放权重已让高能力漏洞利用模型公开可得，防御方需将模型辅助红队纳入常态，同时重新评估针对开放模型的滥用缓解假设。

**Tags**: `#eval`, `#safety`, `#red-teaming`, `#model-capabilities`

---

<a id="item-agent-engineer-6"></a>
### [GPT 6.1 Sol: Near-Astra intelligence for a fifth of the price](https://openai.com/index/introducing-gpt-6-1-sol/) ⭐️ 6.0/10

Hacker News discussion of OpenAI&\#x27;s GPT 6.1 Sol release, highlighting significantly cheaper cached input pricing alongside mixed practitioner reports on coding model regression.

hackernews · crorella · Sep 29, 17:06 · [Discussion](https://news.ycombinator.com/item?id=49896586)

**Tags**: `#coding-agent`, `#eval`, `#pricing`

---

<a id="item-agent-engineer-7"></a>
### [OpenAI DevDay 2026 引争议](https://openai.com/index/devday-2026-recap/) ⭐️ 5.5/10

Hacker News 用户 polygot 提交 OpenAI DevDay 2026 官方回顾，但材料未包含可验证的一手技术细节。社区评论提到子账户登录、Codex 扩展与面向 Luna 的 Decisions API；CharlieDigital 称内部测试中 GPT 6 Luna 批量模式较 Jev 快约 1.6 倍、成本高 1.2 倍且准确率无损，但仅适用于离线处理。另有评论认为新功能缺乏日常可用性，现场反应冷淡。上述性能与功能描述均来自社区，尚未得到官方资料证实。

hackernews · polygot · Sep 29, 17:07 · [Discussion](https://news.ycombinator.com/item?id=49896600)

**「为什么重要」** 对 coding agent 与 harness 开发者而言，子账户、Codex 扩展和 Decisions API 若属实，可能影响权限模型与编排方式；但在官方技术文档缺位时，这些信号只能作为观察线索，不能作为集成依据。

**「可关注」** 可关注：在 OpenAI 公开 Decisions API 与子账户机制细节前，应避免基于社区传闻调整权限或编排架构，同时可跟踪官方后续对 Luna 批量推理成本与速度的披露。

**「评论」** 社区分歧明显：一部分开发者肯定子账户与 Codex 扩展的方向，认为供应商应更像操作系统；另一部分则批评 20 项新功能脱离日常场景，现场反应冷淡。

**Tags**: `#coding-agent`, `#permissions`, `#eval`, `#orchestration`

---

<a id="item-agent-engineer-8"></a>
### [GLM-5.3 实现二进制控制流劫持](https://simonwillison.net/2026/Sep/29/anthropic-frontier-red-team/) ⭐️ 5.5/10

Anthropic Frontier Red Team 从内部 Binary Exploitation 基准随机抽取 100 个任务，测得 GLM-5.3 在 4% 的试验中完成完整控制流劫持，Claude Mythos Preview 为 6%。Claude Opus 4.6 与 GLM-5.2 等早期模型成功率为零。报告称关键门槛已被跨过。

rss · Simon Willison · Sep 29, 22:20

**「为什么重要」** 在该内部基准上，早期模型成功率为零，当前两款模型取得非零控制流劫持结果，为评估模型底层安全能力提供了新数据点。但结果基于 100 个随机任务，且来自单一内部基准，尚不能推广为通用安全水位。

**「可关注」** GLM-5.3 与 Claude Mythos Preview 在内部二进制利用基准上取得 4%–6% 的控制流劫持成功率，早期模型为零，对手模型能力基线已不同，但整体成功率仍低。

**Tags**: `#eval`, `#coding-agent`, `#ai-security-research`

---

<a id="item-agent-engineer-9"></a>
### [Qwen3.8-Flash-Next 量化版发布](https://www.reddit.com/r/LocalLLaMA/comments/1wt4s88/release_gsqrco_ggufs_for_qwen38flashnext_plus_a/) ⭐️ 5.5/10

ISTA Deep Algorithms and Systems Lab 发布 Qwen3.8-Flash-Next 的 GSQ 与 RCO 量化 GGUF，以及一个移除半数路由专家的 Coder 构建。原模型为 176.9B 参数稀疏 MoE，48 层、每层 512 个路由专家，BF16 下占 354 GB。量化版提供 2.40–3.50 bpw 四档 GGUF（66.4–83.6 GB），其中 3.50 bpw 的 IQ3\_S 在 AIME25、GPQA-Diamond、LiveCodeBench v6 上与 BF16 基线持平或更优。Coder 版通过 RCO 按 KL 散度剪掉每层 256 个专家，保留权重仍为 3.5 bpw，整体等效约 1.89 bpw，常驻内存降至 29.6 GB。

reddit · r/LocalLLaMA · /u/Loginhe · Sep 29, 08:40

**「为什么重要」** 对本地部署而言，176.9B 模型的常驻内存降至 29.6 GB，可装入单张 32 GB 加速卡，同时 SWE-bench Verified 保留 BF16 91.3% 的能力。GSQ 与 RCO 分别针对低比特标量量化的精度损失和精确预算分配给出解法，且输出仍为标准 GGUF 类型。

**「可关注」** 可关注：RCO 在同一模型中同时执行逐张量比特分配与专家剪枝，并以精确预算约束输出；Coder 版为实验性构建，发布方提示校准集未覆盖的能力需额外验证。

**Tags**: `#quantization`, `#moe`, `#gguf`, `#local-llm`, `#model-release`

---

## AI Daily

<a id="item-ai-daily-1"></a>
### [OpenAI DevDay 2026 回顾](https://openai.com/index/devday-2026-recap) ⭐️ 10.0/10

OpenAI 官方发布 DevDay 2026 回顾，宣布推出 GPT-6 Astra，并汇总 ChatGPT、Codex、API、安全及开发者工具等超过 20 项更新。原文为第一方 recap，未提供技术细节与基准数据。

rss · OpenAI Blog · Sep 29, 10:00

**「为什么重要」** 此次 recap 覆盖模型、API 与开发工具多条线，与 coding agent 及 harness 生态直接相关。但具体能力、接口与限制仍需等待官方文档或实测确认。

**「可关注」** 可关注：Codex 与 API 的更新方向，当前仅有 recap 摘要，缺乏可集成的具体接口与版本信息。

**Tags**: `#model`, `#lab`, `#product`, `#industry`

---

<a id="item-ai-daily-2"></a>
### [OpenAI 发布 GPT-6.1 Sol](https://openai.com/index/introducing-gpt-6-1-sol) ⭐️ 8.8/10

OpenAI 发布 GPT-6.1 Sol，官方称其具备接近 Astra 的智能水平，适用于编程、计算机操作和专业工作。该模型标准 API 的输入与输出 token 价格均为 Astra 的五分之一。

rss · OpenAI Blog · Sep 29, 10:00

**「为什么重要」** GPT-6.1 Sol 将接近 Astra 能力的标准 API 输入与输出 token 价格定为 Astra 的五分之一，为编程与计算机操作任务提供了更低成本的候选方案。

**「可关注」** 可关注：GPT-6.1 Sol 的标准 API 输入与输出 token 价格均为 Astra 的五分之一，适用于编程、计算机操作和专业工作场景。

**Tags**: `#model`, `#lab`, `#product`, `#industry`

---

<a id="item-ai-daily-3"></a>
### [Asana 让 Claude 当 AI 队友](https://claude.com/blog/agents-you-can-coach-how-asana-builds-human-agent-teams-with-claude) ⭐️ 8.3/10

Asana 在 Anthropic 博客披露内部实践：把 Claude 驱动的 AI 代理作为队友嵌入 Work Graph，而非另建上下文结构。代理按角色划分，拥有独立凭证、共享记忆与显式访问控制；其有效权限被触发者权限封顶。仅管理员和编辑能提交、撤销或删除永久记忆，其他人的反馈只作用于当前任务。代理在任务中公开活动与步骤，人类可随时评论并修正指令。

rss · Claude Blog · Sep 29, 00:00

**「为什么重要」** 企业落地 AI 代理时，权限边界、记忆写入与工作可见性直接决定协作质量。Asana 的做法提供了可复用的设计参考。

**「可关注」** 可关注：Asana 将代理有效权限绑定到触发者，并用角色限制永久记忆写入，以此在开放共享与隐私安全间取得平衡。

**Tags**: `#product`, `#lab`, `#industry`

---

<a id="item-ai-daily-4"></a>
### [OpenAI 发布主动助手 dots](https://openai.com/index/introducing-dots) ⭐️ 6.8/10

OpenAI 发布主动助手 dots。官方描述称，dots 能在复杂项目与日常任务中持续工作，并帮助用户在任务推进时保持掌控。公告未披露具体能力、可用时间与差异化细节。

rss · OpenAI Blog · Sep 29, 00:00

**「为什么重要」** OpenAI 将主动助手定位为跨复杂项目与日常任务的协作者，但公告未给出可用时间与能力边界。

**「可关注」** dots 强调在任务持续向前推进时让用户保持掌控，但具体交互形态与技术实现尚未公开。

**Tags**: `#product`, `#lab`, `#industry`

---

<a id="item-ai-daily-5"></a>
### [GitHub 更新开发者政策与透明度数据](https://github.blog/news-insights/policy-news-and-insights/developer-policy-update-transparency-state-policy-and-whats-ahead/) ⭐️ 6.8/10

GitHub 官方博客发布开发者政策更新，覆盖透明度数据与州级政策，影响开发者与开源项目。文章由 Margaret Tucker 撰写，发布于 2026 年 9 月 29 日。当前材料仅为预告，未披露具体条款、数据明细与生效时间。

rss · GitHub Blog · Sep 29, 15:00

**「可关注」** 跟踪 GitHub 后续公布的透明度数据与州级政策细则，评估对开源项目合规要求的影响。

**Tags**: `#policy`, `#industry`, `#open-source`

---