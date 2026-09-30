---
layout: default
title: "Horizon Summary: 2026-09-30 (ZH)"
date: 2026-09-30
lang: zh
---

> 从 210 条内容中筛选出 20 条重要资讯。

---

**Harness 架构**
1. [openai/codex released rust-v0.159.0](#item-harness-arch-1) ⭐️ 8.3/10
2. [Cline SDK v0.0.87 修复 Windows 启动与计费](#item-harness-arch-2) ⭐️ 6.3/10
3. [google-gemini/gemini-cli released v0.63.0-preview.0](#item-harness-arch-3) ⭐️ 6.3/10
4. [2.1.285](#item-harness-arch-4) ⭐️ 6.3/10
5. [openai/codex released rust-v0.159.1](#item-harness-arch-5) ⭐️ 5.8/10
6. [google-gemini/gemini-cli released v0.62.0](#item-harness-arch-6) ⭐️ 5.8/10

**Agent 工程师日报**
1. [Getting the Source Right, Not Just the Fact: Source-Aware Verification for MCP Agents](#item-agent-engineer-1) ⭐️ 8.3/10
2. [Apple 往返协议量化序列化损失](#item-agent-engineer-2) ⭐️ 8.3/10
3. [TraceDance 从部署轨迹生成行为基准](#item-agent-engineer-3) ⭐️ 8.0/10
4. [HF daily paper: Knowing When Thinking Is Not Enough: Teaching Small Reasoning Models to Reason Beyond Their Parametric Knowledge](#item-agent-engineer-4) ⭐️ 8.0/10
5. [GLM-5.3 端到端漏洞利用能力评估](#item-agent-engineer-5) ⭐️ 7.8/10
6. [GPT 6.1 Sol: Near-Astra intelligence for a fifth of the price](#item-agent-engineer-6) ⭐️ 6.0/10
7. [OpenAI DevDay 2026 回顾](#item-agent-engineer-7) ⭐️ 5.5/10
8. [GLM-5.3 控制流劫持成功率 4%](#item-agent-engineer-8) ⭐️ 5.5/10
9. [Qwen3.8-Flash-Next 推出 GSQ-RCO 量化与专家剪枝版](#item-agent-engineer-9) ⭐️ 5.5/10

**AI 日报**
1. [OpenAI DevDay 2026 回顾](#item-ai-daily-1) ⭐️ 10.0/10
2. [OpenAI 发布 GPT-6.1 Sol](#item-ai-daily-2) ⭐️ 8.8/10
3. [Asana 训练 Claude 代理当队友](#item-ai-daily-3) ⭐️ 8.3/10
4. [OpenAI 发布 dots 主动助手](#item-ai-daily-4) ⭐️ 6.8/10
5. [GitHub 更新开发者政策与透明度数据](#item-ai-daily-5) ⭐️ 6.8/10

---

## Harness 架构

<a id="item-harness-arch-1"></a>
### [openai/codex released rust-v0.159.0](https://github.com/openai/codex/releases/tag/rust-v0.159.0) ⭐️ 8.3/10

Codex Rust v0.159.0 introduces opt-in instant interrupt steering, app-server thread-history pagination, and Windows MCP/code-mode launch fixes.

github · github-actions\[bot\] · 9月29日 08:05

**标签**: `#runtime`, `#tools`, `#mcp`, `#sandbox`

---

<a id="item-harness-arch-2"></a>
### [Cline SDK v0.0.87 修复 Windows 启动与计费](https://github.com/cline/cline/releases/tag/sdk/sdk/v0.0.87) ⭐️ 6.3/10

Cline SDK v0.0.87 发布，修复 Windows 下 hub 因系统代理无法启动的问题，新增 loopback 代理绕过。修正 reasoning token 重复计费，Bedrock 推理路由与模型目录同步更新。补全 PHP 代码搜索、UTF-8 BOM 解析及云会话交接能力。

github · github-actions\[bot\] · 9月29日 05:30

**「设计要点」** 运行时层面，hub client 在探测、排水和关闭前调用 ensureLoopbackProxyBypass\(\)，将 loopback 地址写入 NO\_PROXY/no\_proxy，避免 Bun fetch 把本地请求送入 HTTP\(S\)\_PROXY。计费层调整 normalizeUsage\(\)，使 outputTokens 排除 reasoning tokens，成本仍按完整输出计费。

**「改了什么」** 相对 v0.0.86，hub 在 Windows 系统代理环境下可正常启动，daemon 日志新增 socket 关闭原因与端口占用诊断。token 统计不再双计 reasoning，Bedrock 裸 OpenAI 模型 id 改走 inference profile，模型目录扩至 211 家 provider、6,447 个模型。

**标签**: `#runtime`, `#tools`

---

<a id="item-harness-arch-3"></a>
### [google-gemini/gemini-cli released v0.63.0-preview.0](https://github.com/google-gemini/gemini-cli/releases/tag/v0.63.0-preview.0) ⭐️ 6.3/10

Gemini CLI v0.63.0-preview.0 ships bug fixes including bounded tool output and memory lifecycle optimizations for long-running agent loops.

github · gemini-cli-robot · 9月29日 20:58

**标签**: `#runtime`, `#memory`, `#mcp`, `#tools`

---

<a id="item-harness-arch-4"></a>
### [2.1.285](https://code.claude.com/docs/en/changelog#2-1-285) ⭐️ 6.3/10

Claude Code 2.1.285 introduces incremental tool, MCP, and permission conveniences including a WebFetch kill switch, desktop integration, plugin config commands, and a managed provider allowlist.

rss · Claude Code Changelog · 9月29日 19:37

**标签**: `#tools`, `#mcp`, `#permissions`, `#runtime`

---

<a id="item-harness-arch-5"></a>
### [openai/codex released rust-v0.159.1](https://github.com/openai/codex/releases/tag/rust-v0.159.1) ⭐️ 5.8/10

Codex Rust v0.159.1 backports GPT-6.1 Sol as the default model in bundled and Bedrock catalogs.

github · github-actions\[bot\] · 9月29日 20:32

**标签**: `#runtime`, `#models`, `#catalog`

---

<a id="item-harness-arch-6"></a>
### [google-gemini/gemini-cli released v0.62.0](https://github.com/google-gemini/gemini-cli/releases/tag/v0.62.0) ⭐️ 5.8/10

Routine gemini-cli v0.62.0 patch release with minor fixes to MCP tool title formatting, OAuth token retention, A2A server handling, and UI rendering.

github · gemini-cli-robot · 9月29日 21:17

**标签**: `#mcp`, `#tools`, `#runtime`

---

## Agent 工程师日报

<a id="item-agent-engineer-1"></a>
### [Getting the Source Right, Not Just the Fact: Source-Aware Verification for MCP Agents](https://huggingface.co/blog/MultiverseComputingCAI/getting-the-source-right-not-just-the-fact-source) ⭐️ 8.3/10

Hugging Face introduces ProvenanceGuard, a source-aware verification approach for MCP agents designed to catch cross-source conflation where a fact exists in the evidence pool but is attributed to the wrong source.

rss · Hugging Face Blog · 9月29日 13:07

**标签**: `#eval`, `#mcp`, `#observability`, `#harness`

---

<a id="item-agent-engineer-2"></a>
### [Apple 往返协议量化序列化损失](https://machinelearning.apple.com/research/communication-bottleneck-serialization) ⭐️ 8.3/10

Apple Machine Learning Research 提出往返评测协议，测量树状结构化内容经自然语言序列化后的损失。生成器把程序化生成的算术表达式转成文字题，提取器仅从文字题还原表达式，符号等价提供精确判定。研究覆盖 16 个模型的两两组合。该协议把结构化信息在自由文本交换中的幸存程度变成可复现的量化问题。

rss · Apple Machine Learning Research · 9月29日 00:00

**「为什么重要」** 做 coding agent 与 harness 的工程师常让模型以自然语言交换中间结果，该协议提供了用符号等价 oracle 精确量化这种瓶颈的方法。已发生的变化是协议设计与 16 模型评测，对特定 harness 的实际影响仍待验证。

**「可关注」** 可关注：当 harness 依赖模型以自然语言交换中间结果时，可用符号等价构造往返测试，直接测量结构化信息的幸存比例，而非依赖人工抽查。

**标签**: `#eval`, `#harness`, `#orchestration`

---

<a id="item-agent-engineer-3"></a>
### [TraceDance 从部署轨迹生成行为基准](https://huggingface.co/papers/2609.33295) ⭐️ 8.0/10

2026-09-29，TraceDance 论文提出从真实部署轨迹自动构建针对性行为基准的系统，用于评估用户指定的不良行为。系统用 Anchor-and-Confirm 机制，结合可编程检索与 Flash LLM 的候选确认，并通过 Anchor Synthesis Loop 生成和修订自定义行为规范。基准采用决策点延续，在录制的决策点上评估 LLM 的下一轮输出，使用行为特定评分规则，无需参考答案或环境重放。论文报告了在编程与通用任务上的实验。

rss · Hugging Face Daily Papers · 9月29日 00:00

**「为什么重要」** 固定基准套件难以覆盖部署中遇到的具体不良行为，该工作直接针对这一评估缺口。其决策点延续方法无需环境重放即可评估 LLM 在决策点的下一轮输出，为行为基准提供了不依赖完整环境复现的验证路径。

**「可关注」** 可关注：在评估 Agent 时，除了任务完成率，还可以利用部署轨迹中的决策点，针对特定不良行为设计评分规则，无需重放环境即可检验模型的下一轮选择。

**标签**: `#eval`, `#coding-agent`, `#observability`, `#harness`

---

<a id="item-agent-engineer-4"></a>
### [HF daily paper: Knowing When Thinking Is Not Enough: Teaching Small Reasoning Models to Reason Beyond Their Parametric Knowledge](https://huggingface.co/papers/2609.34327) ⭐️ 8.0/10

This paper identifies when small reasoning models should stop self-refining and instead query external knowledge, introducing a selective querying framework based on execution versus knowledge bottlenecks.

rss · Hugging Face Daily Papers · 9月29日 00:00

**标签**: `#orchestration`, `#eval`, `#coding-agent`, `#harness`

---

<a id="item-agent-engineer-5"></a>
### [GLM-5.3 端到端漏洞利用能力评估](https://www.anthropic.com/research/glm-5-3-and-the-spread-of-advanced-cyber-capabilities) ⭐️ 7.8/10

Anthropic Frontier Red Team 评估 GLM-5.3，发现其具备与 Claude Mythos Preview 相当的端到端漏洞利用能力，但缺乏有效安全限制；模拟测试中，简单技术绕过防护的成功率为 64%–100%。ExploitBench 上，GLM-5.3 在 410 次尝试中成功构建 50 次端到端漏洞利用；内部二进制利用基准中，完整控制流劫持比例为 4%。人类专家一天内用 GLM-5.3 发现浏览器 JavaScript 引擎多个未知漏洞并串联成可利用网页；GLM-5.3-Flash 以 8 小时、20 分钟人工投入构建绕过 PAC 的 ARM64 漏洞利用链，API 成本 20.40 美元。开源权重使 abliteration 可在约 2,200 GPU 小时、4,400 美元内将拒绝率从 90% 以上降至 2%–12%，能力未见显著下降。

rss · Anthropic Research · 9月29日 00:00

**「为什么重要」** GLM-5.3 作为开放权重模型，任何人可下载，且防护可被低成本移除，这降低了恶意行为者获取高级网络攻击能力的门槛。Anthropic 指出这些能力同样可帮助防御者，但对整体网络安全态势的净影响尚未证实。

**「可关注」** 可关注：开放权重模型的前沿网络安全能力可被 abliteration 快速释放，防御方需将模型滥用视为可复现工程问题，而非仅依赖发布方的安全声明。

**标签**: `#eval`, `#safety`, `#red-teaming`, `#model-capabilities`

---

<a id="item-agent-engineer-6"></a>
### [GPT 6.1 Sol: Near-Astra intelligence for a fifth of the price](https://openai.com/index/introducing-gpt-6-1-sol/) ⭐️ 6.0/10

Hacker News discussion of OpenAI&\#x27;s GPT 6.1 Sol release, highlighting significantly cheaper cached input pricing alongside mixed practitioner reports on coding model regression.

hackernews · crorella · 9月29日 17:06 · [社区讨论](https://news.ycombinator.com/item?id=49896586)

**标签**: `#coding-agent`, `#eval`, `#pricing`

---

<a id="item-agent-engineer-7"></a>
### [OpenAI DevDay 2026 回顾](https://openai.com/index/devday-2026-recap/) ⭐️ 5.5/10

Hacker News 提交了 OpenAI DevDay 2026 官方回顾链接，但现有材料仅含社区评论，未见第一方技术细节、代码或基准数据。评论提到的 Decisions API、子账户登录、Codex 扩展及 Ultrafast 基础设施均未在提供的文本中得到证实。部分评论者认为发布反响平淡，新功能难以融入日常工作流；也有评论者提到决策模型 API 与批量推理速度，但相关数据来自个人未公开测试，无法核实。

hackernews · polygot · 9月29日 17:07 · [社区讨论](https://news.ycombinator.com/item?id=49896600)

**「为什么重要」** 对 coding agent 与 harness 开发者而言，社区讨论中出现的 Codex 扩展、子账户权限和 Decisions API 暗示了供应商可能在身份、编排与推理接口上推进，但在缺乏第一方资料前，这些仍属未证实信号，不宜直接纳入技术规划。

**「可关注」** 可关注：Decisions API、子账户与 Codex 扩展若经第一方确认，将直接影响 agent 的权限边界与编排方式；目前所有相关描述均来自社区评论，不能作为架构决策依据。

**「评论」** 评论普遍认为此次发布缺乏日常可用功能，对 ultrafast 能力仅限 Pro 500 用户表示不满；分歧在于 Decisions API 与子账户是否具有实际价值，有评论者视其为重要更新，也有评论者质疑整体产品方向。

**标签**: `#coding-agent`, `#permissions`, `#eval`, `#orchestration`

---

<a id="item-agent-engineer-8"></a>
### [GLM-5.3 控制流劫持成功率 4%](https://simonwillison.net/2026/Sep/29/anthropic-frontier-red-team/) ⭐️ 5.5/10

Anthropic Frontier Red Team 从内部 Binary Exploitation 基准随机抽取 100 个任务。GLM-5.3 完整控制流劫持成功率 4%，Claude Mythos Preview 6%。Claude Opus 4.6 和 GLM-5.2 等早期模型均未成功。报告称阈值已被跨越。

rss · Simon Willison · 9月29日 22:20

**「为什么重要」** 官方第一方基准给出具体指标：GLM-5.3 与 Claude Mythos Preview 在二进制利用上已越过早期模型未达到的阈值。这是模型能力边界的实测数据，对安全评测与红队测试有参考价值。

**「可关注」** 内部 Binary Exploitation 基准上，GLM-5.3 与 Claude Mythos Preview 的控制流劫持成功率分别为 4% 和 6%，早期模型为零。模型能力边界的这一变化，为安全评测与红队测试提供了新的对比基线。

**标签**: `#eval`, `#coding-agent`, `#ai-security-research`

---

<a id="item-agent-engineer-9"></a>
### [Qwen3.8-Flash-Next 推出 GSQ-RCO 量化与专家剪枝版](https://www.reddit.com/r/LocalLLaMA/comments/1wt4s88/release_gsqrco_ggufs_for_qwen38flashnext_plus_a/) ⭐️ 5.5/10

ISTA-DASLab 发布 Qwen3.8-Flash-Next 的 GSQ/RCO 量化 GGUFs 与专家剪枝 Coder 构建。原模型为 48 层稀疏 MoE，每层 512 个路由专家，176.9B 参数，BF16 下 354 GB。量化版覆盖 2.40–3.50 bpw（66.4–83.6 GB），IQ3\_S 在 3.50 bpw 下任务均分 93.26，略高于 BF16 的 93.12。Coder 版每层剪除 256 个专家，保留权重仍为 3.5 bpw，按原始参数量折算等效 1.89 bpw，常驻内存 29.6 GB；SWE-bench Verified 75.60，为 BF16 的 91.3%，属实验性发布。

reddit · r/LocalLLaMA · /u/Loginhe · 9月29日 08:40

**「为什么重要」** 该版本把 176.9B 稀疏 MoE 的常驻显存压到 29.6 GB，可装入单张 32 GB 加速卡；同时用 RCO 统一处理量化类型分配与专家保留，为 MoE 模型本地部署提供一条剪枝加量化的组合路径。

**「可关注」** 可关注：RCO 以任务损失梯度下降同时满足每层精确预算，无需逐约束调参，并在该版本中统一负责量化类型分配与专家保留。

**标签**: `#quantization`, `#moe`, `#gguf`, `#local-llm`, `#model-release`

---

## AI 日报

<a id="item-ai-daily-1"></a>
### [OpenAI DevDay 2026 回顾](https://openai.com/index/devday-2026-recap) ⭐️ 10.0/10

OpenAI 发布 DevDay 2026 回顾，宣布推出 GPT-6 Astra，并汇总超过 20 项更新，覆盖 ChatGPT、Codex、API、安全及面向开发者的新工具。官方 recap 仅列出发布范围，未提供模型基准、API 定价或工具具体变更等技术细节。所有信息均来自 OpenAI 第一方博客，尚无独立验证。

rss · OpenAI Blog · 9月29日 10:00

**「为什么重要」** 作为主要实验室的年度开发者大会，OpenAI 此次集中更新模型与开发者工具，影响 ChatGPT 与 Codex 的现有用户及 API 接入方。

**「可关注」** GPT-6 Astra 与 Codex、API、安全工具同步亮相，开发者可对照官方发布说明检查自身工作流是否受影响。

**标签**: `#model`, `#lab`, `#product`, `#industry`

---

<a id="item-ai-daily-2"></a>
### [OpenAI 发布 GPT-6.1 Sol](https://openai.com/index/introducing-gpt-6-1-sol) ⭐️ 8.8/10

OpenAI 发布 GPT-6.1 Sol。官方称其具备接近 Astra 的智能水平，覆盖编程、计算机操作及专业工作场景。API 输入与输出 token 价格定为 Astra 标准价的五分之一。

rss · OpenAI Blog · 9月29日 10:00

**「为什么重要」** OpenAI 将接近 Astra 的智能水平开放给 coding、computer use 及专业工作场景，输入与输出 token 价格均为 Astra 标准价的五分之一。对做 coding agent 与 computer use 集成的团队，单位调用成本随之降低。

**「可关注」** GPT-6.1 Sol 的 API 输入与输出 token 价格均为 Astra 标准价的五分之一，做 coding agent 或 computer use 集成时可重新评估模型选型。

**标签**: `#model`, `#lab`, `#product`, `#industry`

---

<a id="item-ai-daily-3"></a>
### [Asana 训练 Claude 代理当队友](https://claude.com/blog/agents-you-can-coach-how-asana-builds-human-agent-teams-with-claude) ⭐️ 8.3/10

Anthropic 官方博客披露，Asana 将 Claude 驱动的 AI 代理作为团队成员运行，依托 Work Graph 模型赋予代理明确角色、任务与权限。代理具备持久记忆、独立凭证和共享上下文，可在活动流中与人类同事协同工作。Asana 称代理的有效访问权限受触发者权限约束，且仅管理员和编辑可将反馈写入永久记忆。该案例覆盖内容写作、洞察分析、项目管理等岗位，但属于客户实践，非模型发布或政策变更。

rss · Claude Blog · 9月29日 00:00

**「为什么重要」** 该案例展示了企业如何通过权限继承、角色化配置和透明活动流，将 AI 代理嵌入既有工作模型，而非另建上下文结构。对构建 coding agent / harness 的读者而言，其「触发者权限上界」和「共享记忆分级写入」机制提供了可参考的访问控制与记忆治理设计。

**「可关注」** 可关注：Asana 将代理的有效访问权限绑定到触发者权限，并限制仅管理员和编辑可提交永久记忆，以此在开放协作与权限收敛之间取得平衡。

**标签**: `#product`, `#lab`, `#industry`

---

<a id="item-ai-daily-4"></a>
### [OpenAI 发布 dots 主动助手](https://openai.com/index/introducing-dots) ⭐️ 6.8/10

OpenAI 发布 dots，一款主动助手，可在复杂项目和日常任务中持续工作。官方称其能在工作推进时让用户保持掌控。当前公告仅有一句简介，未披露具体能力、可用时间及与现有产品的差异。

rss · OpenAI Blog · 9月29日 00:00

**「可关注」** 可关注：dots 主打跨复杂项目与日常任务的持续工作，并强调用户掌控，但技术形态、接入方式与可用范围均未公布。

**标签**: `#product`, `#lab`, `#industry`

---

<a id="item-ai-daily-5"></a>
### [GitHub 更新开发者政策与透明度数据](https://github.blog/news-insights/policy-news-and-insights/developer-policy-update-transparency-state-policy-and-whats-ahead/) ⭐️ 6.8/10

GitHub 发布开发者政策更新，涉及透明度数据以及影响开发者和开源项目的州政策。官方博客文章由 Margaret Tucker 撰写，但当前材料仅为简短预告，未披露具体政策条款或数据细节。

rss · GitHub Blog · 9月29日 15:00

**「可关注」** 可关注：GitHub 官方博客将发布影响开发者和开源项目的政策更新，需等待完整内容以确认透明度数据与州政策的具体范围。

**标签**: `#policy`, `#industry`, `#open-source`

---