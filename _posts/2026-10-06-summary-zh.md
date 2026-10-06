---
layout: default
title: "Horizon Summary: 2026-10-06 (ZH)"
date: 2026-10-06
lang: zh
---

> 从 187 条内容中筛选出 17 条重要资讯。

---

**Harness 架构**
1. [vllm-project/vllm released v0.31.0](#item-harness-arch-1) ⭐️ 8.8/10
2. [Mastra core 1.74.0 发布](#item-harness-arch-2) ⭐️ 8.3/10
3. [mastra-ai/mastra released @mastra/core@1.73.0](#item-harness-arch-3) ⭐️ 8.3/10
4. [Claude Code v2.1.290 发布](#item-harness-arch-4) ⭐️ 7.8/10
5. [openai/openai-agents-js released @openai/agents-core@0.19.0](#item-harness-arch-5) ⭐️ 7.3/10
6. [modelcontextprotocol/typescript-sdk released @modelcontextprotocol/server-legacy@2.3.1](#item-harness-arch-6) ⭐️ 7.3/10
7. [agents-realtime 0.19.0](#item-harness-arch-7) ⭐️ 6.8/10

**Agent 工程师日报**
1. [Cloudflare 修复容器跨租户数据暴露](#item-agent-engineer-1) ⭐️ 8.0/10
2. [Recursive Self-Rewrite 论文：多 harness 训练轨迹](#item-agent-engineer-2) ⭐️ 7.5/10
3. [HyperBrowseComp 用 423 题压测网页浏览 Agent](#item-agent-engineer-3) ⭐️ 7.5/10
4. [Cowork 从本地 VM 迁往云沙箱](#item-agent-engineer-4) ⭐️ 6.0/10
5. [Web Search API](#item-agent-engineer-5) ⭐️ 5.5/10
6. [RealCompanion 长对话基准发布](#item-agent-engineer-6) ⭐️ 5.5/10
7. [MotorMind：VLM 直驱机器人操作](#item-agent-engineer-7) ⭐️ 5.5/10

**AI 日报**
1. [Building advertising for the way people use AI](#item-ai-daily-1) ⭐️ 10.0/10
2. [OpenAI 应对欧盟文本溯源规则](#item-ai-daily-2) ⭐️ 8.8/10
3. [GitHub 发布 ReviewBench](#item-ai-daily-3) ⭐️ 8.8/10

---

## Harness 架构

<a id="item-harness-arch-1"></a>
### [vllm-project/vllm released v0.31.0](https://github.com/vllm-project/vllm/releases/tag/v0.31.0) ⭐️ 8.8/10

vLLM v0.31.0 is a major official release with substantial runtime performance optimizations, a new weight-cache daemon CLI, and prefix-cache mechanism changes.

github · khluu · 10月5日 06:44

**标签**: `#runtime`, `#prefix-cache`, `#memory`, `#tools`

---

<a id="item-harness-arch-2"></a>
### [Mastra core 1.74.0 发布](https://github.com/mastra-ai/mastra/releases/tag/%40mastra/core%401.74.0) ⭐️ 8.3/10

Mastra core 1.74.0 发布。工具执行上下文新增 \`context.agent.getMessages\(\)\`，可在标准与 durable agent loops 中读取当前完整对话，覆盖记忆消息与运行中响应，输入字段 \`messages\` 保持不变。观测记忆历史支持 \`groupId\` 过滤、\`sortDirection\` 排序与 \`recordId\` 直查，适配器通过 \`supportsObservationalMemoryHistorySearch\` 声明能力。记忆召回支持围绕命中 \`groupId\` 前后翻页，覆盖被 reflection 压缩的组与未激活缓冲组，现有记录无需重建索引。

github · PaulieScanlon · 10月5日 09:31

**「设计要点」** 工具层通过 \`context.agent.getMessages\(\)\` 暴露只读消息列表，反映消息移除，但不包含仅作用于 provider prompt 的瞬态转换。记忆层将观测组作为可翻页单元，适配器需显式声明历史搜索能力；Convex 适配器须重新部署 server functions 才能应用新过滤条件。

**「改了什么」** 工具从仅能访问输入 \`messages\` 扩展为可读取完整会话状态。观测记忆历史从基础查询升级为支持分组过滤、排序与单记录查找。召回从单次检索变为可前后翻页的观测组浏览。Playground UI 弃用 \`\*FieldBlock\`，改用基于 Base UI 的 \`Field\`/\`Fieldset\` 组件，并移除 \`ThreadTrace\` 的 \`anchorTraceId\` 与 \`LoadMoreSentinel\`，改用 \`pageSize\` 与 \`onLoadOlder\` 控制分页。

**标签**: `#tools`, `#memory`, `#runtime`, `#agents`

---

<a id="item-harness-arch-3"></a>
### [mastra-ai/mastra released @mastra/core@1.73.0](https://github.com/mastra-ai/mastra/releases/tag/%40mastra/core%401.73.0) ⭐️ 8.3/10

Mastra 1.73.0 introduces default agent error recovery processors, a new \`tool-call-resumed\` streaming chunk for tool-pause UX, and Google Workspace toolsets in \`@mastra/connect\`.

github · PaulieScanlon · 10月5日 09:30

**标签**: `#runtime`, `#tools`, `#streaming`

---

<a id="item-harness-arch-4"></a>
### [Claude Code v2.1.290 发布](https://github.com/anthropics/claude-code/releases/tag/v2.1.290) ⭐️ 7.8/10

Claude Code v2.1.290 扩展插件钩子与子代理权限检查。\`turn.step\` 钩子结果新增 \`serverToolUses\`，返回 API 自行执行的工具调用及其起止信息；\`tool.check\` 事件新增 \`agentId\` 和 \`ceiling\`，用于区分子代理与主会话的权限检查，并读取组织要求的审批上限。CLI 侧支持按会话名执行 \`claude attach\` 和 \`claude logs\`，不再强制使用会话 ID。同时修复代理转发、长会话图片堆积、计划任务恢复、权限规则匹配等多处运行时问题。

github · ashwin-ant · 10月5日 23:33

**「设计要点」** 插件钩子现在能拿到子代理身份与组织审批上限，权限判断从主会话单层扩展到子代理层级；\`serverToolUses\` 让顾问型工具调用在 \`turn.step\` 结果中可观测。

**「改了什么」** 新增 \`serverToolUses\`、\`agentId\`、\`ceiling\` 等钩子字段，以及按会话名操作的 CLI 命令；修复涵盖代理兼容性、子代理缓存、计划任务恢复、权限规则与 MCP 配置等大量边界问题。

**标签**: `#tools`, `#subagents`, `#permissions`, `#runtime`

---

<a id="item-harness-arch-5"></a>
### [openai/openai-agents-js released @openai/agents-core@0.19.0](https://github.com/openai/openai-agents-js/releases/tag/%40openai/agents-core%400.19.0) ⭐️ 7.3/10

openai/agents-core 0.19.0 tightens runtime correctness around tool streaming limits, checkpoint validation, MCP call recipient binding, conditional approval isolation, and error redaction.

github · github-actions\[bot\] · 10月5日 16:47

**标签**: `#runtime`, `#tools`, `#mcp`, `#permissions`

---

<a id="item-harness-arch-6"></a>
### [modelcontextprotocol/typescript-sdk released @modelcontextprotocol/server-legacy@2.3.1](https://github.com/modelcontextprotocol/typescript-sdk/releases/tag/%40modelcontextprotocol/server-legacy%402.3.1) ⭐️ 7.3/10

MCP TypeScript SDK legacy server patch adds optional \`expectedResource\` audience validation to \`requireBearerAuth\`, aligning legacy auth middleware with newer SDK versions.

github · github-actions\[bot\] · 10月5日 11:49

**标签**: `#mcp`, `#permissions`, `#auth`

---

<a id="item-harness-arch-7"></a>
### [agents-realtime 0.19.0](https://github.com/openai/openai-agents-js/releases/tag/%40openai/agents-realtime%400.19.0) ⭐️ 6.8/10

OpenAI Agents JS 发布 @openai/agents-realtime@0.19.0。本次 minor 版本集中修复工具审批与 Realtime 运行时缺陷。条件工具审批改为绑定隔离的标准化执行输入，持久审批恢复时重新评估当前策略，并拒绝不可复制的标准化值。同时修复大音频缓冲区编码栈溢出，以及 updateHistory 修正或插入项时的对话顺序错乱。

github · github-actions\[bot\] · 10月5日 16:47

**「设计要点」** 审批层将条件判断与执行输入隔离，恢复持久审批时重新读取策略而非沿用旧上下文。Realtime 侧在 updateHistory 覆盖或插入历史项时维持消息顺序，切换到无工具 agent 且无提示时清理陈旧工具配置。

**「改了什么」** 条件审批新增输入隔离与恢复重评，函数工具和 Realtime 审批解析失败默认脱敏，敏感错误追踪需显式调用策略。修复音频编码栈溢出、自动响应合并后等待任务释放、历史编辑顺序保持及无工具 agent 切换时的工具清理。

**标签**: `#tools`, `#permissions`, `#runtime`

---

## Agent 工程师日报

<a id="item-agent-engineer-1"></a>
### [Cloudflare 修复容器跨租户数据暴露](https://blog.cloudflare.com/containers-cross-tenant-vulnerability/) ⭐️ 8.0/10

Cloudflare 于 2026-10-05 发布工程博客，说明如何修复 Containers 中的跨租户数据暴露漏洞。文章提供了生产环境的隔离与多租户实现细节，涉及 agent 托管基础设施的沙箱边界。目前材料仅包含官方第一方博文，未见社区评论或外部验证。

rss · Lobsters · 10月5日 23:03

**「为什么重要」** 跨租户隔离是 agent 托管平台的底线问题，Cloudflare 这次公开了生产环境的漏洞机理与修复路径，给做 harness 和沙箱的人提供了一手参考。已发生的变化是漏洞被修复并披露，尚未证实的影响是其他多租户 agent 平台是否存在同类边界缺陷。

**「可关注」** 可关注：Cloudflare 在 Containers 中如何界定租户边界并处置数据暴露，这为自建多租户 agent 沙箱提供了隔离设计的对照基线。

**标签**: `#security`, `#permissions`, `#harness`

---

<a id="item-agent-engineer-2"></a>
### [Recursive Self-Rewrite 论文：多 harness 训练轨迹](https://huggingface.co/papers/2610.02826) ⭐️ 7.5/10

Hugging Face Daily Papers 收录论文，提出 Recursive Self-Rewrite（RSR）框架。它基于 Qwen-3.8-27B，先在多个专用 harness 下找成功解，再于通用 harness 下重建成训练轨迹。planner 抽 runbooks，critic 筛 verifier 与 solution leakage 并指导递归修订，executor 在新 sandbox 执行合格 runbooks。约 3K 个自选终端任务中，三个 harness 共解出 759 题，较记录池中最强单 harness 多 34.3%，扩展出 2,001 条成功源轨迹。

rss · Hugging Face Daily Papers · 10月6日 02:38

**「为什么重要」** 专用 harness 常引入部署时缺失的干预。RSR 把多 harness 的成功解重建成通用 harness 下的训练轨迹，直接回应训练数据与部署环境不一致的问题。

**「可关注」** 可关注：把专用 harness 的强表现沉淀为可移植 runbooks，再让通用 harness 复现，可能是缓解训练轨迹与部署环境割裂的一条路径。

**标签**: `#harness`, `#eval`, `#coding-agent`, `#orchestration`

---

<a id="item-agent-engineer-3"></a>
### [HyperBrowseComp 用 423 题压测网页浏览 Agent](https://huggingface.co/papers/2610.03574) ⭐️ 7.5/10

Hugging Face 每日论文页面介绍了新基准 HyperBrowseComp。它包含 423 道人工编写并经人工验证的多语言、多模态问题，覆盖 13 种语言，由母语者或高水平使用者撰写。题目要求定位冷门证据、跟随多步线索链，或检查视频、扫描文档、图像、地图等异构来源。为降低仅凭参数化知识作答的可能，研究者先用无互联网访问的模型过滤掉简单问题。评测时，多个模型在统一 Agent 协议下对比 provider-native search 与共享外部检索 harness。

rss · Hugging Face Daily Papers · 10月6日 02:38

**「为什么重要」** 对做 coding agent / harness 的读者，这个基准把检索与推理拆到统一协议下压测，提供了可复用的评测参考。它明确过滤参数化知识，直指当前 Agent 评测里“背答案”的问题。

**「可关注」** 可关注：HyperBrowseComp 用无网模型预过滤题目，再把 provider-native search 和外部 harness 放进同一 Agent 协议对比，这种“先防背题、再控变量”的评测设计可直接迁移到自有 harness 的回归测试。

**标签**: `#eval`, `#harness`, `#agent`

---

<a id="item-agent-engineer-4"></a>
### [Cowork 从本地 VM 迁往云沙箱](https://simonwillison.net/2026/Oct/5/felix-rieseberg/) ⭐️ 6.0/10

Anthropic 工程师 Felix Rieseberg 称，Cowork 旧版将模型推理放在云端，工具调用在本地 Anthropic VM 中执行；新版把推理和 VM 都迁到云端，每个会话获得独立沙箱，不共享状态。当沙箱需要访问用户设备文件时，由桌面应用负责该文件访问工具调用。旧方案因本地 VM 带来磁盘、电池与性能开销，且合盖即停；新方案声称支持手机使用、保持任务运行并省去本地 VM 耗电。目前仅有工程师引述，缺少实现细节与基准数据。

rss · Simon Willison · 10月5日 23:56

**「为什么重要」** 这是 agent harness 设计里一次具体的权限与执行位置迁移：工具调用从本地 VM 搬到云沙箱，文件访问通过桌面应用委托，直接影响会话隔离与权限边界。对做 coding agent 和 harness 的工程师有参考价值，但材料未提供性能或安全基准。

**「可关注」** 可关注：本地 VM 的磁盘、电池与合盖即停问题推动执行位置迁往云端，而文件访问仍需桌面应用中转，这一委托路径的工程代价材料未展开。

**标签**: `#harness`, `#orchestration`, `#permissions`, `#coding-agent`

---

<a id="item-agent-engineer-5"></a>
### [Web Search API](https://developers.cloudflare.com/changelog/post/2026-10-02-introducing-web-search-api/) ⭐️ 5.5/10

Cloudflare introduced a new Web Search API, but the announcement lacks technical depth and community discussion centers on licensing and alternatives.

hackernews · tosh · 10月5日 10:47 · [社区讨论](https://news.ycombinator.com/item?id=49963171)

**标签**: `#coding-agent`, `#tools`, `#api`

---

<a id="item-agent-engineer-6"></a>
### [RealCompanion 长对话基准发布](https://huggingface.co/papers/2610.01780) ⭐️ 5.5/10

RealCompanion 基准于 2026-10-06 在 Hugging Face Daily Papers 发布，收录 10 段真实 AI 伴侣长对话，共 27,218 条消息，跨度至多 120 天。除原始会话外，还提供 profile、persona、chat ground truth 和 question set 四个衍生文件，每个文件均标注所引用的消息。每条聊天标签附带推理轨迹，并逐阶段对照会话核验。论文提到三项发现，但摘要片段仅显示第一项，后续内容不完整。

rss · Hugging Face Daily Papers · 10月6日 02:38

**「为什么重要」** 该基准用真实纵向对话替代合成数据，直接考察记忆与长上下文理解。不过材料指出其影响面偏伴侣 AI，对通用 agent 工具链的工程价值仍待验证。

**「可关注」** 可关注：RealCompanion 要求每条聊天标签附带逐阶段核验的推理轨迹，且衍生文件必须回指所依据的消息，为长时程记忆评测提供了可溯源的标注范式。

**标签**: `#eval`, `#memory`

---

<a id="item-agent-engineer-7"></a>
### [MotorMind：VLM 直驱机器人操作](https://huggingface.co/papers/2609.38078) ⭐️ 5.5/10

2026 年 10 月 6 日，Hugging Face 每日论文上线 MotorMind。论文主张通用视觉语言模型（VLM）直接驱动机器人操作，摆脱外部动作专家与辅助工具链。现有 VLA 模型零样本泛化有限，专门训练又使其难以受益于通用 VLM 的快速进步。MotorMind 让 VLM 像人类遥操作员一样，从观察直接推理、发出动作、持续适应执行反馈。目前仅见摘要，无开源代码、架构细节与基准数据，可复现性待验证。

rss · Hugging Face Daily Papers · 10月6日 02:38

**「为什么重要」** 若通用 VLM 能独立承担机器人控制，具身 agent 的 harness 可省去外部动作专家与辅助模型，降低复杂度与成本。但论文未公开技术细节，该影响尚未证实。

**「可关注」** 可关注：MotorMind 把机器人控制从“VLM 推理 + 外部动作专家”推向“单一 VLM 端到端驱动”，但当前缺代码与基准，工程复现需等原文。

**标签**: `#harness`, `#eval`, `#orchestration`

---

## AI 日报

<a id="item-ai-daily-1"></a>
### [Building advertising for the way people use AI](https://openai.com/index/new-chatgpt-ads-format-and-measurement) ⭐️ 10.0/10

OpenAI introduces a new visual ad format in ChatGPT and expands measurement tools, attribution partnerships, and brand suitability for advertisers.

rss · OpenAI Blog · 10月5日 10:00

**标签**: `#product`, `#industry`, `#lab`, `#model`

---

<a id="item-ai-daily-2"></a>
### [OpenAI 应对欧盟文本溯源规则](https://openai.com/index/eu-text-provenance) ⭐️ 8.8/10

OpenAI 发布官方博客，说明其在欧盟文本溯源规则下的水印方案。文章介绍水印的适用范围、检测机制，以及访问权限为何先向研究人员开放。这是 OpenAI 对欧盟监管要求的官方技术说明。

rss · OpenAI Blog · 10月5日 15:00

**「为什么重要」** 欧盟对 AI 生成文本提出溯源要求，OpenAI 公开其水印与检测策略，为行业合规提供参考样本。

**「可关注」** 可关注：OpenAI 将水印与检测的访问权限首先开放给研究人员，而非直接面向公众。

**标签**: `#policy`, `#lab`, `#industry`, `#product`

---

<a id="item-ai-daily-3"></a>
### [GitHub 发布 ReviewBench](https://github.blog/ai-and-ml/github-copilot/reviewbench-an-open-benchmark-for-ai-code-review/) ⭐️ 8.8/10

GitHub 发布 ReviewBench，一个面向 AI 代码评审 agent 的开放基准。该基准基于具有代表性的 GitHub pull request 构建，采用多源 ground truth、校准评估和生产对齐的指标。官方尚未披露数据规模、参评模型或量化结果。

rss · GitHub Blog · 10月5日 15:59

**「为什么重要」** ReviewBench 为 AI 代码评审 agent 提供了基于代表性 PR 的开放评估框架。其多源 ground truth 与生产对齐指标，让不同 agent 的评审能力有了统一参照。

**「可关注」** 可关注：ReviewBench 采用多源 ground truth 与生产对齐指标，后续可用于横向对比不同代码评审 agent 在真实 PR 上的表现。

**标签**: `#eval`, `#open-source`, `#industry`, `#product`

---