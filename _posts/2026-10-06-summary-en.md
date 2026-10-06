---
layout: default
title: "Horizon Summary: 2026-10-06 (EN)"
date: 2026-10-06
lang: en
---

> From 187 items, 17 important content pieces were selected

---

**Agent Harness Architecture**
1. [vllm-project/vllm released v0.31.0](#item-harness-arch-1) ⭐️ 8.8/10
2. [Mastra Core 1.74.0 Released](#item-harness-arch-2) ⭐️ 8.3/10
3. [mastra-ai/mastra released @mastra/core@1.73.0](#item-harness-arch-3) ⭐️ 8.3/10
4. [Claude Code v2.1.290 发布](#item-harness-arch-4) ⭐️ 7.8/10
5. [openai/openai-agents-js released @openai/agents-core@0.19.0](#item-harness-arch-5) ⭐️ 7.3/10
6. [modelcontextprotocol/typescript-sdk released @modelcontextprotocol/server-legacy@2.3.1](#item-harness-arch-6) ⭐️ 7.3/10
7. [OpenAI Agents Realtime 0.19.0 Released](#item-harness-arch-7) ⭐️ 6.8/10

**AI Agent Engineer**
1. [Cloudflare 修复容器跨租户数据暴露](#item-agent-engineer-1) ⭐️ 8.0/10
2. [RSR 框架：递归自改写扩展终端任务轨迹](#item-agent-engineer-2) ⭐️ 7.5/10
3. [HyperBrowseComp：多语言多模态浏览 Agent 基准](#item-agent-engineer-3) ⭐️ 7.5/10
4. [Cowork 转向每会话云沙箱](#item-agent-engineer-4) ⭐️ 6.0/10
5. [Web Search API](#item-agent-engineer-5) ⭐️ 5.5/10
6. [RealCompanion 发布长对话理解基准](#item-agent-engineer-6) ⭐️ 5.5/10
7. [MotorMind 论文：VLM 操作机器人](#item-agent-engineer-7) ⭐️ 5.5/10

**AI Daily**
1. [Building advertising for the way people use AI](#item-ai-daily-1) ⭐️ 10.0/10
2. [OpenAI 说明欧盟文本溯源规则应对方案](#item-ai-daily-2) ⭐️ 8.8/10
3. [GitHub 推出 ReviewBench](#item-ai-daily-3) ⭐️ 8.8/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [vllm-project/vllm released v0.31.0](https://github.com/vllm-project/vllm/releases/tag/v0.31.0) ⭐️ 8.8/10

vLLM v0.31.0 is a major official release with substantial runtime performance optimizations, a new weight-cache daemon CLI, and prefix-cache mechanism changes.

github · khluu · Oct 5, 06:44

**Tags**: `#runtime`, `#prefix-cache`, `#memory`, `#tools`

---

<a id="item-harness-arch-2"></a>
### [Mastra Core 1.74.0 Released](https://github.com/mastra-ai/mastra/releases/tag/%40mastra/core%401.74.0) ⭐️ 8.3/10

Mastra core 1.74.0 gives tools read access to the full conversation via \`context.agent.getMessages\(\)\` in standard and durable agent loops, covering remembered messages and in-run responses without changing the input-only \`messages\` field. Observational memory history adds \`groupId\` filtering, \`sortDirection\` ordering, and \`recordId\` lookup, with adapters signaling support through \`supportsObservationalMemoryHistorySearch\`. Memory recall can now page before or after a matched \`groupId\`, including groups condensed by reflection or still buffered, with no re-indexing required. The release also introduces accessible form primitives in Playground UI and removes \`anchorTraceId\` in favor of \`pageSize\` and \`onLoadOlder\`.

github · PaulieScanlon · Oct 5, 09:31

**「Design Notes」** Tools receive a read-only view of the conversation that reflects message-list removals but not transient provider-prompt transforms. Memory adapters advertise observational history search support via a capability flag, so unsupported backends can degrade gracefully; Convex requires a server function redeploy for the new filters. Recall paging reads original observation groups directly from storage around search hits, avoiding re-indexing.

**「What Changed」** Tools can now read the full conversation via \`context.agent.getMessages\(\)\` in standard and durable loops. Observational memory history adds \`groupId\` filtering, \`sortDirection\`, and \`recordId\` lookup with adapter capability signaling, while recall supports paging before/after observation groups around search hits without re-indexing.

**Tags**: `#tools`, `#memory`, `#runtime`, `#agents`

---

<a id="item-harness-arch-3"></a>
### [mastra-ai/mastra released @mastra/core@1.73.0](https://github.com/mastra-ai/mastra/releases/tag/%40mastra/core%401.73.0) ⭐️ 8.3/10

Mastra 1.73.0 introduces default agent error recovery processors, a new \`tool-call-resumed\` streaming chunk for tool-pause UX, and Google Workspace toolsets in \`@mastra/connect\`.

github · PaulieScanlon · Oct 5, 09:30

**Tags**: `#runtime`, `#tools`, `#streaming`

---

<a id="item-harness-arch-4"></a>
### [Claude Code v2.1.290 发布](https://github.com/anthropics/claude-code/releases/tag/v2.1.290) ⭐️ 7.8/10

Claude Code v2.1.290 扩展插件钩子与子代理权限检查。\`turn.step\` 钩子结果新增 \`serverToolUses\`，返回 API 自行执行的工具调用；\`tool.check\` 事件新增 \`agentId\` 和 \`ceiling\`，用于区分子代理与主会话的权限判定，并读取组织要求的审批上限。CLI 支持按会话名执行 \`claude attach\` 和 \`claude logs\`。版本还修复了权限规则、计划任务恢复、WebFetch 截断及插件加载等大量问题。

github · ashwin-ant · Oct 5, 23:33

**「设计要点」** 插件钩子层新增 \`serverToolUses\`、\`agentId\`、\`ceiling\` 字段，直接暴露服务端工具调用与子代理权限边界。\`claude plugin validate\` 开始检查门控钩子的 \`.catch\` 注册，插件加载与卸载逻辑收紧，避免用户安装的插件覆盖组织插件。

**「改了什么」** \`turn.step\` 钩子可读取 API 侧工具调用明细；\`tool.check\` 能识别子代理与主会话，并获取组织审批上限。CLI 会话管理从 ID 扩展到名称匹配。新增 \`/claude-api managed-agents-onboard\` 命令，支持 \`ant apply\` 文件与 Console 快速启动模板。

**Tags**: `#tools`, `#subagents`, `#permissions`, `#runtime`

---

<a id="item-harness-arch-5"></a>
### [openai/openai-agents-js released @openai/agents-core@0.19.0](https://github.com/openai/openai-agents-js/releases/tag/%40openai/agents-core%400.19.0) ⭐️ 7.3/10

openai/agents-core 0.19.0 tightens runtime correctness around tool streaming limits, checkpoint validation, MCP call recipient binding, conditional approval isolation, and error redaction.

github · github-actions\[bot\] · Oct 5, 16:47

**Tags**: `#runtime`, `#tools`, `#mcp`, `#permissions`

---

<a id="item-harness-arch-6"></a>
### [modelcontextprotocol/typescript-sdk released @modelcontextprotocol/server-legacy@2.3.1](https://github.com/modelcontextprotocol/typescript-sdk/releases/tag/%40modelcontextprotocol/server-legacy%402.3.1) ⭐️ 7.3/10

MCP TypeScript SDK legacy server patch adds optional \`expectedResource\` audience validation to \`requireBearerAuth\`, aligning legacy auth middleware with newer SDK versions.

github · github-actions\[bot\] · Oct 5, 11:49

**Tags**: `#mcp`, `#permissions`, `#auth`

---

<a id="item-harness-arch-7"></a>
### [OpenAI Agents Realtime 0.19.0 Released](https://github.com/openai/openai-agents-js/releases/tag/%40openai/agents-realtime%400.19.0) ⭐️ 6.8/10

OpenAI released @openai/agents-realtime@0.19.0 for the Agents JS SDK. The minor release fixes conditional tool approvals, error redaction, and realtime conversation ordering. Conditional approvals now bind to isolated normalized execution input in core and Realtime, and durable approval resumes re-evaluate current policies. It also rejects uncopyable normalized values before approval and preserves invalid-input handling.

github · github-actions\[bot\] · Oct 5, 16:47

**「Design Notes」** Approval checks run against isolated normalized input rather than shared mutable state, and durable resumes re-evaluate policies instead of reusing cached decisions. Default function-tool and Realtime approval parse failures redact error traces unless an explicit invocation policy is set.

**「What Changed」** Tool approval logic now evaluates policies on isolated normalized input and re-checks on durable resumes. Realtime fixes prevent stack overflows when encoding large audio buffers, keep conversation order when updateHistory corrects or inserts items, and clear stale tools when switching to a tool-less agent without a prompt.

**Tags**: `#tools`, `#permissions`, `#runtime`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [Cloudflare 修复容器跨租户数据暴露](https://blog.cloudflare.com/containers-cross-tenant-vulnerability/) ⭐️ 8.0/10

Cloudflare 工程博客披露其 Containers 产品存在跨租户数据暴露漏洞，并公布了修复方案与技术细节。该漏洞直接关涉多租户 agent 托管基础设施的隔离边界，官方文章深入分析了隔离与多租户实现。博客发布于 2026 年 10 月 5 日，目前未见社区讨论或第三方复现。

rss · Lobsters · Oct 5, 23:03

**「为什么重要」** 该漏洞涉及多租户环境下的数据隔离，对依赖云容器服务托管 agent 的团队有直接参考意义。Cloudflare 公开的修复细节可作为评估自身沙箱边界时的对照案例。

**「可关注」** 多租户容器隔离存在被绕过导致数据暴露的风险，Cloudflare 的修复细节可作为审计自身 agent 沙箱租户边界的参考。

**Tags**: `#security`, `#permissions`, `#harness`

---

<a id="item-agent-engineer-2"></a>
### [RSR 框架：递归自改写扩展终端任务轨迹](https://huggingface.co/papers/2610.02826) ⭐️ 7.5/10

2026 年 10 月 6 日，Hugging Face Daily Papers 收录论文《Scaling Trajectories for Complex Tasks through Recursive Self-Rewrite》，提出 Recursive Self-Rewrite（RSR）框架。该框架用单一基础模型 Qwen-3.8-27B 在多种 harness 下发现成功解，再通过 planner-critic-executor 架构在通用 harness 下重构为训练轨迹：planner 抽取流程为 runbook，critic 筛查 verifier 与 solution 泄漏并指导递归修订，executor 在全新 sandbox 中执行合格 runbook。在约 3K 自建终端任务上，三种 harness 联合解决 759 题，比记录池中最强单 harness 多 34.3%。论文当日获得 83 赞。

rss · Hugging Face Daily Papers · Oct 6, 02:38

**「为什么重要」** 对 coding agent 与 harness 设计者，该文给出可复核的轨迹构建路径：用多 harness 发现成功解，再以通用 harness 重构，直接回应专用 harness 干预在部署时不可用的问题。已发生的变化是框架与实验数字；尚未证实的影响是该方法在更大规模或真实环境中的泛化表现。

**「可关注」** 可关注：planner-critic-executor 与多 harness 协同在终端任务上比最强单 harness 提升 34.3%，构建训练轨迹时可评估是否引入 critic 筛查泄漏与递归修订，以降低专用 harness 干预带来的分布偏移。

**Tags**: `#harness`, `#eval`, `#coding-agent`, `#orchestration`

---

<a id="item-agent-engineer-3"></a>
### [HyperBrowseComp：多语言多模态浏览 Agent 基准](https://huggingface.co/papers/2610.03574) ⭐️ 7.5/10

HyperBrowseComp 发布，包含 423 道由母语或高水平使用者人工编写并验证的多语言、多模态网页浏览题目，覆盖 13 种语言。题目答案简短且可公开验证，需定位冷门证据、跟随多步线索链，或检查视频、扫描文档、图像、地图等异构来源。为减少仅凭参数化知识作答的可能，较易题目已被无网络模型过滤。评测在统一 Agent 协议下对比 provider-native search 与共享外部检索 harness。

rss · Hugging Face Daily Papers · Oct 6, 02:38

**「为什么重要」** 对做 coding agent / harness 的人，它提供了可直接复用的检索与推理评测设计：用无网络模型预过滤抗参数化知识，并在统一协议下对比不同检索后端。

**「可关注」** 可关注：HyperBrowseComp 将视频、扫描文档、图像、地图等异构来源纳入浏览 Agent 评测，并显式区分 provider-native search 与外部 harness，可作为自建检索评测的参考基线。

**Tags**: `#eval`, `#harness`, `#agent`

---

<a id="item-agent-engineer-4"></a>
### [Cowork 转向每会话云沙箱](https://simonwillison.net/2026/Oct/5/felix-rieseberg/) ⭐️ 6.0/10

On October 5, 2026, Felix Rieseberg described Anthropic&\#x27;s Cowork moving from a local VM to per-session cloud sandboxes. The previous version ran model inference in the cloud while executing tool calls inside an Anthropic-provided VM shipped with the desktop app; users valued the capabilities but disliked the local disk, battery, and performance costs, and disliked that closing the laptop stopped work. The new version runs both inference and the VM in the cloud, giving each session its own sandbox with no shared state; when the VM needs a file on the user&\#x27;s device, the desktop app handles that file-access tool call. Rieseberg said this addresses phone use, persistent work, and battery drain, but the description lacks implementation details or benchmarks.

rss · Simon Willison · Oct 5, 23:56

**「为什么重要」** For harness and orchestration engineers, this marks a shift from locally managed VMs to cloud-isolated sandboxes with delegated local file access. The architectural change is confirmed, but whether it fully removes local overhead and preserves security boundaries remains unverified.

**「可关注」** 可关注: When agent execution moves to cloud sandboxes, local file-access tool calls require explicit cross-device delegation, and the design of permission and state isolation directly affects session security and resumability.

**Tags**: `#harness`, `#orchestration`, `#permissions`, `#coding-agent`

---

<a id="item-agent-engineer-5"></a>
### [Web Search API](https://developers.cloudflare.com/changelog/post/2026-10-02-introducing-web-search-api/) ⭐️ 5.5/10

Cloudflare introduced a new Web Search API, but the announcement lacks technical depth and community discussion centers on licensing and alternatives.

hackernews · tosh · Oct 5, 10:47 · [Discussion](https://news.ycombinator.com/item?id=49963171)

**Tags**: `#coding-agent`, `#tools`, `#api`

---

<a id="item-agent-engineer-6"></a>
### [RealCompanion 发布长对话理解基准](https://huggingface.co/papers/2610.01780) ⭐️ 5.5/10

RealCompanion 发布长对话理解基准，包含 10 段真实人机陪伴关系、27,218 条跨最多 120 天的消息。基准除原始对话外，提供 profile、persona、chat ground truth 和 question set 四个衍生文件，每个标签都引用其依据的消息，并附带逐阶段核对的推理轨迹。论文提出三个发现，但公开摘要仅显示第一点：历史上下文很少被需要且距离远。该基准针对陪伴式 AI 的长期人类理解，不直接覆盖通用 agent 工具链。

rss · Hugging Face Daily Papers · Oct 6, 02:38

**「为什么重要」** 现有长期记忆与长上下文评测多依赖合成数据，RealCompanion 提供真实纵向对话及可溯源的推理轨迹，为记忆检索和上下文依赖判断给出新基线。但其场景限于陪伴式 AI，对通用 coding agent 工具链的直接迁移价值尚未证实。

**「可关注」** 该基准用真实纵向对话替代合成人物，并给每个标签附上可溯源的推理轨迹，为长期记忆评测提供新基线；但其场景限于陪伴式 AI，尚未覆盖通用 agent 工具链。

**Tags**: `#eval`, `#memory`

---

<a id="item-agent-engineer-7"></a>
### [MotorMind 论文：VLM 操作机器人](https://huggingface.co/papers/2609.38078) ⭐️ 5.5/10

Hugging Face 每日论文收录 MotorMind，提出让通用视觉语言模型（VLM）直接推理观测、输出动作并依据执行反馈持续调整，从而摆脱对外部动作专家或大量专用工具的依赖。论文指出，现有 VLA 模型零样本泛化受限且依赖专门训练，而基于 VLM 的智能体系统虽用于高层推理或编码控制，却常引入复杂的外部模型与成本。目前公开信息仅限摘要，未提供开源代码、架构细节或基准数据，可复现性待验证。

rss · Hugging Face Daily Papers · Oct 6, 02:38

**「为什么重要」** 若通用 VLM 能直接承担机器人操作中的观测推理与动作生成，具身 agent 的 harness 可能减少对外部动作专家和工具链的依赖。但该影响尚未经论文细节或第三方验证，目前仅停留在问题提出阶段。

**「可关注」** MotorMind 试图用单一通用 VLM 替代“高层推理 + 外部动作专家”的分层方案，这对做 coding agent / harness 的人是一个信号——控制回路可能进一步向通用模型收敛，但在缺少代码与基准前，不宜作为工程选型依据。

**Tags**: `#harness`, `#eval`, `#orchestration`

---

## AI Daily

<a id="item-ai-daily-1"></a>
### [Building advertising for the way people use AI](https://openai.com/index/new-chatgpt-ads-format-and-measurement) ⭐️ 10.0/10

OpenAI introduces a new visual ad format in ChatGPT and expands measurement tools, attribution partnerships, and brand suitability for advertisers.

rss · OpenAI Blog · Oct 5, 10:00

**Tags**: `#product`, `#industry`, `#lab`, `#model`

---

<a id="item-ai-daily-2"></a>
### [OpenAI 说明欧盟文本溯源规则应对方案](https://openai.com/index/eu-text-provenance) ⭐️ 8.8/10

OpenAI 发布博客，说明其在欧盟文本溯源规则下的水印方案。文章介绍水印的适用范围、检测方式，以及访问权限为何先向研究人员开放。这是 OpenAI 对欧盟监管要求的第一方技术说明。

rss · OpenAI Blog · Oct 5, 15:00

**「为什么重要」** 欧盟对 AI 生成文本提出溯源要求，OpenAI 公开其水印与检测策略，展示主要实验室的合规技术路径。研究人员优先获得访问权限，也影响后续检测工具的验证节奏。

**「可关注」** OpenAI 明确水印访问从研究人员起步，并披露检测机制与适用范围，这是其应对欧盟溯源规则的具体技术路径。

**Tags**: `#policy`, `#lab`, `#industry`, `#product`

---

<a id="item-ai-daily-3"></a>
### [GitHub 推出 ReviewBench](https://github.blog/ai-and-ml/github-copilot/reviewbench-an-open-benchmark-for-ai-code-review/) ⭐️ 8.8/10

GitHub 推出 ReviewBench，面向 AI 代码审查 agent 的开放基准。该基准基于 GitHub 代表性 pull request，采用多源 ground truth、校准评估与生产对齐指标。

rss · GitHub Blog · Oct 5, 15:59

**「为什么重要」** GitHub 将代码审查 agent 的评测建立在代表性 pull request 与多源 ground truth 之上，并引入生产对齐指标，为该领域提供开放基准。

**「可关注」** 可关注：ReviewBench 采用多源 ground truth 与生产对齐指标，评估代码审查 agent 时可作为方法论参考。

**Tags**: `#eval`, `#open-source`, `#industry`, `#product`

---