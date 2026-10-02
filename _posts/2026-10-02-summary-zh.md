---
layout: default
title: "Horizon Summary: 2026-10-02 (ZH)"
date: 2026-10-02
lang: zh
---

> 从 189 条内容中筛选出 18 条重要资讯。

---

**Harness 架构**
1. [google/adk-python released v2.11.0](#item-harness-arch-1) ⭐️ 8.8/10
2. [Claude Code 2.1.287 发布](#item-harness-arch-2) ⭐️ 8.8/10
3. [Codex rust-v0.160.0 发布](#item-harness-arch-3) ⭐️ 6.8/10
4. [openai/openai-agents-python released v0.23.0](#item-harness-arch-4) ⭐️ 6.8/10
5. [microsoft/agent-framework released dotnet-1.23.0](#item-harness-arch-5) ⭐️ 6.8/10
6. [e2b-dev/e2b released e2b@2.52.0](#item-harness-arch-6) ⭐️ 6.3/10
7. [E2B CLI 2.21.0 限制 fork](#item-harness-arch-7) ⭐️ 6.3/10

**Agent 工程师日报**
1. [Box^2-Bench 测模型对外部引导依赖](#item-agent-engineer-1) ⭐️ 8.0/10
2. [pwasm 0.2a0 支持 WASM 沙箱](#item-agent-engineer-2) ⭐️ 7.8/10
3. [AREX-2 提出长程反思自改进智能体](#item-agent-engineer-3) ⭐️ 7.5/10
4. [Mid-Harness 论文：边界处验证动作](#item-agent-engineer-4) ⭐️ 7.5/10
5. [Meta-Skill 设计 Harness](#item-agent-engineer-5) ⭐️ 7.5/10
6. [沙箱 Agent 可借共享缓存传播蠕虫](#item-agent-engineer-6) ⭐️ 6.0/10
7. [Qwen Flash Next 接入 MTP](#item-agent-engineer-7) ⭐️ 6.0/10
8. [Clef 决策模型与 RL 微调平台](#item-agent-engineer-8) ⭐️ 5.5/10

**AI 日报**
1. [OpenAI：AI 或重塑常规执行工作](#item-ai-daily-1) ⭐️ 6.3/10
2. [Albertsons 部署 ChatGPT](#item-ai-daily-2) ⭐️ 6.3/10
3. [10 technical talks I’m excited about at GitHub Universe 2026](#item-ai-daily-3) ⭐️ 5.8/10

---

## Harness 架构

<a id="item-harness-arch-1"></a>
### [google/adk-python released v2.11.0](https://github.com/google/adk-python/releases/tag/v2.11.0) ⭐️ 8.8/10

ADK v2.11.0 adds runtime cancellation, workflow tool approval, and a built-in SQLite memory service.

github · xuanyang15 · 10月2日 00:44

**标签**: `#runtime`, `#tools`, `#memory`, `#permissions`

---

<a id="item-harness-arch-2"></a>
### [Claude Code 2.1.287 发布](https://code.claude.com/docs/en/changelog#2-1-287) ⭐️ 8.8/10

Claude Code 2.1.287 发布。新增 Claude Mods，插件可修改更深层运行时行为；内置 side-agent mod「You should know」用于标记用户或 Claude 可能遗漏的内容，通过 \`/plugin enable cc-plugin-you-should-know@builtin\` 启用。MCP 服务器在 2025-11-25 协议下可发起 URL 提示（如登录），但需在 MCP 配置中加入 \`&quot;bareElicitationCapability&quot;: true\`，否则服务器可能无法连接。OpenTelemetry \`user\_prompt\` 事件新增 \`prompt\_text\` 字段，作为 \`prompt\` 的副本，供嵌套点分键的后端使用。

rss · Claude Code Changelog · 10月1日 18:14

**「设计要点」** Claude Mods 将插件能力从工具层延伸到运行时行为层，side-agent 以独立观察者身份介入会话。MCP 客户端以 \`bareElicitationCapability\` 作为 URL elicitation 的显式开关，未开启时拒绝连接；OpenTelemetry 用 \`prompt\_text\` 复制 \`prompt\`，绕开后端对点分键的嵌套限制。

**「改了什么」** 运行时新增 Mods 插件机制与内置 side-agent；MCP 层支持 URL 提示并引入破坏性配置项 \`bareElicitationCapability\`；可观测性层为 \`user\_prompt\` 事件补充 \`prompt\_text\` 字段。

**标签**: `#runtime`, `#mcp`, `#subagents`, `#eval`

---

<a id="item-harness-arch-3"></a>
### [Codex rust-v0.160.0 发布](https://github.com/openai/codex/releases/tag/rust-v0.160.0) ⭐️ 6.8/10

OpenAI Codex 发布 rust-v0.160.0。新增 workspace 默认会话权限，支持在项目外启动会话，并在恢复时还原已保存权限。Guardian 审查能力改为可选开启，可检索早期用户指令并纳入 agent 交接上下文。Windows 沙盒修复 PowerShell 回退与长路径 ACL 问题，同时抑制后台助手弹出的控制台窗口。

github · andrewgu-oai · 10月1日 20:19

**「设计要点」** 权限层引入 workspace 默认值，使无项目会话在策略允许下运行。Guardian 作为可选审查模块，通过检索历史指令和交接上下文增强记忆连续性。Subagent 启动时保留 pending 环境，确保配置或准备失败能正确回传。

**「改了什么」** TUI 支持重连后恢复未发送消息，修复 resume/fork 历史中的 provider 与模型查找。SQLite 连接初始化错误不再被掩盖为超时，并新增后台日志库空间回收。显式 provider 模型目录被设为权威来源，刷新失败后不再复用陈旧条目。

**标签**: `#sandbox`, `#permissions`, `#memory`, `#subagents`, `#runtime`

---

<a id="item-harness-arch-4"></a>
### [openai/openai-agents-python released v0.23.0](https://github.com/openai/openai-agents-python/releases/tag/v0.23.0) ⭐️ 6.8/10

OpenAI Agents Python v0.23.0 adds configurable MCP listing page limits, opt-in Docker removal protection, configurable memory consolidation turns, and an opt-in encrypted history scan budget.

github · openai-sdks\[bot\] · 10月2日 01:08

**标签**: `#sandbox`, `#mcp`, `#memory`, `#sessions`

---

<a id="item-harness-arch-5"></a>
### [microsoft/agent-framework released dotnet-1.23.0](https://github.com/microsoft/agent-framework/releases/tag/dotnet-1.23.0) ⭐️ 6.8/10

Microsoft Agent Framework .NET 1.23.0 ships breaking changes to tool handling between runs, MCP client origin pinning, and multiple workflow topology and declarative workflow fixes.

github · dmytrostruk · 10月1日 10:54

**标签**: `#runtime`, `#tools`, `#mcp`, `#workflow`

---

<a id="item-harness-arch-6"></a>
### [e2b-dev/e2b released e2b@2.52.0](https://github.com/e2b-dev/E2B/releases/tag/e2b%402.52.0) ⭐️ 6.3/10

E2B 2.52.0 caps sandbox fork count at 20 via client-side validation and aligns template file copying with Docker ignore semantics.

github · github-actions\[bot\] · 10月1日 10:44

**标签**: `#sandbox`, `#tools`, `#runtime`

---

<a id="item-harness-arch-7"></a>
### [E2B CLI 2.21.0 限制 fork](https://github.com/e2b-dev/E2B/releases/tag/%40e2b/cli%402.21.0) ⭐️ 6.3/10

E2B CLI 2.21.0 发布，核心变更为 sandbox fork 数量增加客户端校验。CLI、JavaScript 与 Python SDK 现在在调用 API 前拒绝 1–20 范围外的 count。此前 21–100 的 count 会直接到达 API。省略 count 时请求不带该字段，仍由 API 默认值处理。

github · github-actions\[bot\] · 10月1日 10:44

**「改了什么」** \`e2b sandbox fork --count\`、JavaScript \`Sandbox.fork\(\{ count \}\)\` 与 Python \`Sandbox.fork\(count=...\)\` 新增前置校验，count 超出 1–20 直接报错。补丁部分将 protobuf 与 OpenAPI 客户端、终端样式及交互提示升级到兼容的次要版本，并更新依赖至 \`e2b@2.52.0\`。

**标签**: `#sandbox`, `#runtime`, `#tools`

---

## Agent 工程师日报

<a id="item-agent-engineer-1"></a>
### [Box^2-Bench 测模型对外部引导依赖](https://huggingface.co/papers/2609.39578) ⭐️ 8.0/10

新论文提出 Box^2-Bench 基准，固定模型与任务，变化工作流可靠性，单独隔离模型对外部引导的依赖调节能力。作者将「受益于有用引导、同时覆盖不可靠引导」的能力称为 thinking outside the box。实测显示，前沿模型能从可靠引导中获益，但面对误导性或失效引导时仍显脆弱。作者用坏工作流训练两个开源权重模型，保留好工作流用于评估，并探索两种互补训练策略，其中一种为反事实监督。

rss · Hugging Face Daily Papers · 10月2日 01:56

**「为什么重要」** Agent harness 常借助人工设计的工作流提升模型，但模型能力增强后，不可靠引导可能越来越制约执行。该基准把「选择性依赖」从笼统的 agent 评测中拆出，直接对应 harness 设计中的引导质量问题。

**「可关注」** 可关注：Box^2-Bench 将工作流可靠性作为独立变量，为 harness 中外部引导的评估提供了隔离方法；训练用坏工作流、评估保留好工作流的设定，也划出了能力泛化的测试边界。

**标签**: `#eval`, `#harness`, `#orchestration`, `#coding-agent`

---

<a id="item-agent-engineer-2"></a>
### [pwasm 0.2a0 支持 WASM 沙箱](https://github.com/simonw/pwasm/releases/tag/0.2a0) ⭐️ 7.8/10

simonw 发布 pwasm 0.2a0，新增基于 WebAssembly 的沙箱，可执行未受信的 Python 与 JavaScript 代码。该版本内置 MicroPython、QuickJS 与 MQuickJS 的 WebAssembly 构建，通过 \`pwasm.guests\` 与 \`pwasm.sandbox\` 提供内存、CPU 与时间限制，且无文件系统与网络访问。pwasm 完整实现 WebAssembly 2.0 核心指令集（除 SIMD），并引入编译到 Python 的执行层，热点函数较解释执行快 8–14 倍；磁盘缓存将 QuickJS 启动从约 1.3s 降至 0.1s。项目同时支持 PyPy 与 CPython 3.10–3.14。

github · simonw · 10月1日 17:10

**「为什么重要」** 对需要执行未受信代码的 agent harness 而言，pwasm 0.2a0 提供了纯 Python 的 WebAssembly 沙箱方案，内置资源限制与无文件系统/网络的 WASI 实现。其编译到 Python 的层级与磁盘缓存显著降低了启动与执行开销，但尚未验证在真实 agent 负载下的稳定性与兼容性。

**「可关注」** 可关注：\`pwasm.guests\` 与 \`pwasm.sandbox\` 的 API 设计，以及 \`Limits\`、\`OutOfFuel\`、\`Timeout\` 等异常如何嵌入现有 harness 的权限与超时控制。同时注意其 wheel 约 650KB，且当前不支持 SIMD。

**标签**: `#coding-agent`, `#harness`, `#permissions`

---

<a id="item-agent-engineer-3"></a>
### [AREX-2 提出长程反思自改进智能体](https://huggingface.co/papers/2609.38288) ⭐️ 7.5/10

AREX-2 论文把智能体的自改进能力定义为测试时迭代优化解，并拆成反思与长程执行两部分。作者假设这两种能力领域无关，因此在机器学习和算法编程任务上合成长程改进轨迹，利用可验证反馈监督训练。基于 Qwen3.8-27B 的智能体在 MLE-bench Lite 上报告了较强结果，论文未披露具体分数。

rss · Hugging Face Daily Papers · 10月2日 01:56

**「为什么重要」** 对 coding agent 与 harness 设计者而言，这提供了一条将反思与长程执行分离训练、再在可验证域合成轨迹的路径。当前证据仅限 MLE-bench Lite，跨领域泛化尚未验证。

**「可关注」** 可关注：设计迭代改进循环时，可把「生成更优解」与「维持多轮有效迭代」作为两个独立模块，并优先在有可验证反馈的任务域构造监督数据。

**标签**: `#eval`, `#coding-agent`, `#harness`, `#orchestration`

---

<a id="item-agent-engineer-4"></a>
### [Mid-Harness 论文：边界处验证动作](https://huggingface.co/papers/2609.39982) ⭐️ 7.5/10

Hugging Face Daily Papers 于 2026-10-02 收录 Mid-Harness 论文，提出在模型与 harness 边界处采样并验证候选动作，再转发执行，且不修改生成器与 harness。实验基于 TMAX-9B 生成器，摘要显示弱验证下增加动作采样收益有限，强验证器可提升轨迹成功率，但原文在此处截断，具体效果未完整给出。论文将测试时计算放在模型与 harness 之间，用于提升终端 Agent 的动作可靠性。

rss · Hugging Face Daily Papers · 10月2日 01:56

**「为什么重要」** 终端 Agent 执行错误命令可能改变环境状态，阻碍后续步骤。该论文把可靠性瓶颈从模型生成转移到 harness 边界的动作筛选，为不更换模型的情况下提升执行成功率提供了一条可测试路径。

**「可关注」** 可关注：在 harness 外层增加动作采样前，先确认验证器是否足够强，否则采样数量增加对结果帮助有限。

**标签**: `#harness`, `#coding-agent`, `#eval`, `#orchestration`

---

<a id="item-agent-engineer-5"></a>
### [Meta-Skill 设计 Harness](https://huggingface.co/papers/2609.38143) ⭐️ 7.5/10

Hugging Face 论文提出 Meta-Skill 方法，在测试期 AI-for-AI 设定下让 Builder 为 Target 设计执行环境（harness），两侧模型权重均保持固定。Builder 从 Target 在开发集上的执行反馈中学习元技能，再用冻结的技能库为未见任务构建 harness。在 Harness-Bench 和 NewtonBench 上，完整技能库相比无技能构建将宏平均性能提升 8.95 个百分点，相比直接向 Target 交付同一技能库提升 12.02 个百分点。论文发布于 2026-10-02，目前获得 76 次 upvote。

rss · Hugging Face Daily Papers · 10月2日 01:56

**「为什么重要」** 该工作把 harness 设计本身变成可学习的对象，为固定权重模型提供了一条不依赖微调的 Agent 性能优化路径。目前结果限于 Harness-Bench 和 NewtonBench，尚未覆盖更广场景。

**「可关注」** 可关注：在固定模型权重下，由 Builder 学习元技能并构建 harness 的思路，为 Agent 执行环境优化提供了不依赖微调的新路径。

**标签**: `#harness`, `#eval`, `#coding-agent`, `#orchestration`

---

<a id="item-agent-engineer-6"></a>
### [沙箱 Agent 可借共享缓存传播蠕虫](https://simonwillison.net/2026/Oct/1/matthew-green/) ⭐️ 6.0/10

Matthew Green 在 2026 年 9 月 30 日的文章中提出，分别隔离的沙箱 Agent 可通过共享包缓存互相传递指令，接收方行为随之改变。Simon Willison 于 10 月 1 日引述了这一分析。Green 指出，若将包缓存替换为 email、Slack、共享文档或 WhatsApp，并将独立沙箱化的训练运行替换为独立部署的个人 Agent（如 Muse），即构成蠕虫传播的完整条件。该分析目前仅为观点引述，缺少完整技术细节与可复现材料。

rss · Simon Willison · 10月1日 06:29

**「为什么重要」** 沙箱隔离常被视为 Agent 安全边界，该分析指出共享基础设施可能成为跨沙箱传播通道，直接影响 harness 的权限与编排设计。目前尚未出现公开复现或实际攻击案例，风险仍停留在理论推演层面。

**「可关注」** 可关注：共享包缓存、邮件、Slack 等跨 Agent 通信面是否应纳入沙箱威胁模型，而非仅隔离执行环境。

**标签**: `#permissions`, `#orchestration`, `#harness`

---

<a id="item-agent-engineer-7"></a>
### [Qwen Flash Next 接入 MTP](https://www.reddit.com/r/LocalLLaMA/comments/1wuwrsk/qwen4exp_add_mtp_by_am17an_pull_request_29761/) ⭐️ 6.0/10

2026 年 10 月 1 日，llama.cpp 合并 PR \#29761，为 Qwen Flash Next 添加 MTP 支持。Hugging Face 已发布对应的 GGUF 量化版本。该 PR 从开发到合并耗时 17 小时。目前影响范围限于单一模型与单一推理特性，尚无基准数据或社区反馈。

reddit · r/LocalLLaMA · /u/jacek2023 · 10月1日 11:18

**「为什么重要」** 对使用 Qwen Flash Next 的本地推理用户而言，MTP 支持与现成 GGUF 量化版本降低了尝试门槛。但材料未提供性能对比，实际收益仍待验证。

**「可关注」** 可关注：GGUF 量化版本已随 PR 发布，本地部署可直接切换；不过 MTP 对生成速度的具体提升尚未给出基准，需自行实测。

**标签**: `#harness`, `#coding-agent`

---

<a id="item-agent-engineer-8"></a>
### [Clef 决策模型与 RL 微调平台](https://blog.cloudflare.com/clef-decision-models/) ⭐️ 5.5/10

Cloudflare 发布 Clef 开放权重决策模型与 RL 微调平台。早期社区实测显示，Clef 比现有 Jev 模型慢 2–3 倍，仇恨言论识别更少；输入定价 $0.24/m，约为 Jev（$0.042/m）的 6 倍。按每次调用 300 token 估算，百万次决策成本从约 $12.60 升至约 $72。评论指出，Clef 仅开放权重，训练数据与流程未公开，无法从专有 Qwen 基座复现。

hackernews · jasondavies · 10月1日 16:18 · [社区讨论](https://news.ycombinator.com/item?id=49923692)

**「为什么重要」** 对 coding agent 与 harness 工程师，决策模型是编排链路上的候选组件。Clef 当前在延迟、准确率、成本上均落后于 Jev，且训练流程不透明，短期替换动力有限。若具备自托管能力，开放权重提供了一条潜在路径。

**「可关注」** 可关注：选型决策模型时，将 Clef 与 Jev 做延迟、准确率、单次调用成本的三维对比；已有 Jev 工作流的话，迁移前先做小规模 A/B 测试。

**「评论」** 有评论猜测 Clef 基于 Typesafe 新范式且排名优于 Jev，但实测反馈是更慢、更不准、更贵。开放权重的价值也有分歧：一方看中自托管，另一方强调未公开数据与流程，不等于开源。

**标签**: `#orchestration`, `#eval`, `#fine-tuning`

---

## AI 日报

<a id="item-ai-daily-1"></a>
### [OpenAI：AI 或重塑常规执行工作](https://openai.com/index/the-eternal-complement) ⭐️ 6.3/10

OpenAI 发布博客文章《The eternal complement》，提出先进 AI 的最大影响可能在于突破性想法背后的常规执行工作。文章认为，执行环节或塑造下一个经济形态与进步节奏。该文为官方观点，并非模型发布或政策变更。

rss · OpenAI Blog · 10月1日 17:00

**「为什么重要」** 作为 OpenAI 官方对 AI 经济影响的一手论述，该文为观察行业叙事提供了直接材料。

**「可关注」** 可关注：OpenAI 将 AI 的经济价值指向常规执行环节，而非仅限突破性创新。

**标签**: `#lab`, `#industry`

---

<a id="item-ai-daily-2"></a>
### [Albertsons 部署 ChatGPT](https://openai.com/index/albertsons-reimagining-retail) ⭐️ 6.3/10

Albertsons Cos. 正在使用 ChatGPT Enterprise 与 OpenAI API，帮助团队提速，并让数百万顾客的杂货购物更便捷。该案例来自 OpenAI 官方博客，属于企业采用实例，并非模型发布或政策变化。公开材料未披露具体部署规模、量化收益或技术实现细节。

rss · OpenAI Blog · 10月1日 16:00

**「可关注」** 可关注：官方仅披露产品组合与业务方向，未给出架构、成本或效果数据，具体实现仍待补充。

**标签**: `#product`, `#industry`, `#lab`

---

<a id="item-ai-daily-3"></a>
### [10 technical talks I’m excited about at GitHub Universe 2026](https://github.blog/news-insights/company-news/10-technical-talks-im-excited-about-at-github-universe-2026/) ⭐️ 5.8/10

GitHub Blog previews 10 technical talks at GitHub Universe 2026, including sessions on verifying AI-written code and securing npm dependencies.

rss · GitHub Blog · 10月1日 15:07

**标签**: `#industry`, `#product`, `#open-source`, `#eval`

---