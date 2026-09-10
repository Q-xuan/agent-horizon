---
layout: default
title: "Horizon Summary: 2026-09-10 (ZH)"
date: 2026-09-10
lang: zh
---

> 从 193 条内容中筛选出 16 条重要资讯。

---

**Harness 架构**
1. [OpenClaw-v1.1.0 发布](#item-harness-arch-1) ⭐️ 8.8/10
2. [vLLM v0.29.0 发布](#item-harness-arch-2) ⭐️ 8.8/10
3. [Codex rust-v0.154.0 发布](#item-harness-arch-3) ⭐️ 7.8/10
4. [pydantic-ai v2.42.0 发布](#item-harness-arch-4) ⭐️ 7.8/10
5. [Mastra @mastra/core@1.65.0 发布](#item-harness-arch-5) ⭐️ 7.8/10
6. [mem0 DeepSeek 插件 v0.3.0 发布](#item-harness-arch-6) ⭐️ 7.8/10
7. [mem0 opencode-v0.3.0 发布](#item-harness-arch-7) ⭐️ 6.8/10
8. [browser-use AI 代理 trending](#item-harness-arch-8) ⭐️ 5.0/10
9. [opencode 开源编码代理 trending](#item-harness-arch-9) ⭐️ 5.0/10

**Agent 工程师日报**
1. [Goodfire 使用 Ai2 栈追踪行为](#item-agent-engineer-1) ⭐️ 5.8/10
2. [Cognition RSA-260 因式分解](#item-agent-engineer-2) ⭐️ 5.8/10

**AI 日报**
1. [Paul Christiano 加入 OpenAI Foundation Board](#item-ai-daily-1) ⭐️ 7.8/10
2. [OpenAI 政策窗口开放 需要行动](#item-ai-daily-2) ⭐️ 6.8/10
3. [LWiAI Podcast \#256 Fable 5.1 发布](#item-ai-daily-3) ⭐️ 5.0/10

**AI 羊毛**
1. [复旦学术版 Codex 客户端上线 送 1 万积分](#item-ai-deals-1) ⭐️ 6.0/10
2. [DeepSeek V4-Flash 降价 24 天后](#item-ai-deals-2) ⭐️ 6.0/10

---

## Harness 架构

<a id="item-harness-arch-1"></a>
### [OpenClaw-v1.1.0 发布](https://github.com/mem0ai/mem0/releases/tag/openclaw-v1.1.0) ⭐️ 8.8/10

mem0 发布 OpenClaw-v1.1.0。会话准备、脱敏和遥测改走共享实现，OpenClaw 原生 memory 后端、工具、CLI 以及 Platform/OSS 模式保留。自包含 ESM 包仍发在 \`@mem0/openclaw-mem0\`，插件清单与包版本现已对齐。Dream 巩固已删除；抽取不再另截 2,000 字符。

github · kartik-mem0 · 9月9日 14:34

**「设计要点」** 会话准备、脱敏和遥测接到共享层，memory 后端、工具、CLI 仍是 OpenClaw 原生，Platform/OSS 模式保留。选中的 user 与 assistant 消息保留完整脱敏文本，近期消息挑选、更早摘要挑选和噪声过滤仍在；Triage、recall 与 memory/entity 产物仍可用。

**「改了什么」** Dream 巩固已删除，包括自动调度与加锁、\`openclaw mem0 dream\`、Dream 配置、memory-dream skill 和 Dream-state 公开产物，相关配置和集成需要改。\`openclaw mem0 status\` 未配置时不再崩溃并指向 setup；抽取不再另截 2,000 字符；遥测递归去掉敏感属性，上报改走共享实现。

**标签**: `#memory`, `#tools`, `#runtime`, `#cli`

---

<a id="item-harness-arch-2"></a>
### [vLLM v0.29.0 发布](https://github.com/vllm-project/vllm/releases/tag/v0.29.0) ⭐️ 8.8/10

vLLM v0.29.0 发布。该版本将 Model Runner V2 设为所有模型的默认运行时，并引入 CUDA 图内存分析以自动调整 KV cache 内存、批次分片采样等功能。新增支持 Hy4-preview、Qwen3.8-Flash-Next 等模型，并针对 Kimi-K3 和 DeepSeek V4 进行多项性能优化。

github · khluu · 9月9日 08:54

**「改了什么」** Model Runner V2 成为默认运行时。移除十个已弃用模型架构，迁移 FlexOlmo、Olmo3 和 Hunyuan V1/VL 到 Transformers 后端，移除 PyAV 视频解码后端。

**标签**: `#runtime`, `#memory`, `#tools`

---

<a id="item-harness-arch-3"></a>
### [Codex rust-v0.154.0 发布](https://github.com/openai/codex/releases/tag/rust-v0.154.0) ⭐️ 7.8/10

Codex rust-v0.154.0 发布了新版本，新增实验性 worktree 支持以创建隔离 checkout，并支持 inline 问答而不丢失草稿。Windows 会话可共享后台服务器，并新增 Vim R 替换模式。修复了插件工具刷新和 MCP 连接问题。

github · github-actions\[bot\] · 9月9日 22:35

**「改了什么」** 与 rust-v0.153.0 相比，新增实验性 worktree 支持和 Windows 后台服务器共享功能。修复了现有会话无法刷新新安装插件工具的问题，并改善了 MCP OAuth 刷新。

**标签**: `#runtime`, `#tools`, `#sandbox`

---

<a id="item-harness-arch-4"></a>
### [pydantic-ai v2.42.0 发布](https://github.com/pydantic/pydantic-ai/releases/tag/v2.42.0) ⭐️ 7.8/10

pydantic-ai v2.42.0 发布。该版本新增 GitHubCopilotProvider，支持 GitHub Copilot 的 OpenAI 兼容 API 接口。添加工具批准功能，并修复了 Bedrock、Anthropic 模型的运行时兼容性、$ref 处理和 ToolReturnContent 验证等问题。

github · dsfaccini · 9月9日 03:33

**「改了什么」** v2.42.0 相比 v2.41.0，新增 GitHubCopilotProvider 功能并支持 DeferredToolResults 的 approvals 兼容性。修复了 BedrockConverseModel 对 anthropic\_disallows\_sampling\_settings 的支持、$ref 定义 inline 处理、ToolReturnContent 验证以及 Anthropic 恢复等问题。

**标签**: `#runtime`, `#tools`, `#permissions`, `#planning`

---

<a id="item-harness-arch-5"></a>
### [Mastra @mastra/core@1.65.0 发布](https://github.com/mastra-ai/mastra/releases/tag/%40mastra/core%401.65.0) ⭐️ 7.8/10

Mastra @mastra/core@1.65.0 发布了高级追踪查询功能。新增严格的可移植追踪查询合约，支持有界时间范围、递归谓词、线程分组和确定性游标分页。实现了服务器端点和 ClickHouse、DuckDB、Postgres 存储适配器。

新增租户作用域的追踪删除，支持最多 1000 个追踪 ID 批处理，并级联清理跨度、分数、反馈、指标和日志。

工作流控制流块新增可选 id、description 和 metadata 字段，支持序列化和重新加载。

github · PaulieScanlon · 9月9日 09:43

**「设计要点」** 追踪查询合约在存储适配器执行前验证请求有效性。工作流定义支持稳定 id 和 metadata，适用于可视化编辑器。

**「改了什么」** 相对于上一版，新增了高级追踪查询合约、服务器端点和多存储实现。添加了租户作用域的追踪删除功能，支持最多 1000 个追踪 ID 批处理和级联清理，并为工作流控制流块新增了 id、description 和 metadata 字段。Agent channels 新增 onAction handlers，Factory 新增自定义 boards。

**标签**: `#runtime`, `#memory`, `#planning`, `#traces`, `#workflows`

---

<a id="item-harness-arch-6"></a>
### [mem0 DeepSeek 插件 v0.3.0 发布](https://github.com/mem0ai/mem0/releases/tag/deepseek-plugin-v0.3.0) ⭐️ 7.8/10

Mem0 发布了 Harness DeepSeek 插件 v0.3.0。新增在 system-prompt/assemble 期间自动 recall，使用最新 human prompt，避免重复上下文注入。自动从 durable session/event stream 捕获 completed turns，autoRecall 和 autoCapture 默认 true。

github · kartik-mem0 · 9月9日 14:36

**「设计要点」** 插件复用共享生命周期、去标识、身份和遥测工具，同时保留显式 search\_memory 和 add\_memory 工具并保持 per-call scope。跨用户 userId 覆盖需 allowUserOverride: true。

**「改了什么」** 新增自动 recall 和 capture 功能，复用共享工具并添加 userId override 权限要求。发布自包含 ESM 包 @mem0/deepseek-plugin。

**标签**: `#memory`, `#tools`, `#runtime`, `#permissions`

---

<a id="item-harness-arch-7"></a>
### [mem0 opencode-v0.3.0 发布](https://github.com/mem0ai/mem0/releases/tag/opencode-v0.3.0) ⭐️ 6.8/10

mem0 发布了 opencode-v0.3.0 插件版本。该版本将插件源代码从 integrations/mem0-plugin/.opencode-plugin/ 迁移到 integrations/opencode-plugin/，保留了 @mem0/opencode-plugin 包名和原生 OpenCode 钩子。插件复用共享对话准备、脱敏、作用域和遥测组件，构建自包含的 Bun/ESM dist/index.js。

github · kartik-mem0 · 9月9日 14:38

**「设计要点」** 全局内存工具作用域要求用户先在插件设置中启用；空身份和通配符身份被拒绝。插件复用共享组件进行对话准备、脱敏、作用域和遥测。

**「改了什么」** opencode-v0.3.0 强制全局内存工具使用前需在插件设置中启用，并拒绝空身份和通配符身份。移除了自动 Dream 整合、其门控和状态处理，以及 Dream 和 pin 技能/命令。现有使用这些功能的配置需更新。

**标签**: `#memory`, `#tools`, `#runtime`, `#permissions`

---

<a id="item-harness-arch-8"></a>
### [browser-use AI 代理 trending](https://github.com/browser-use/browser-use) ⭐️ 5.0/10

browser-use 是一个 AI 代理工具，让 AI 像人类一样使用浏览器。用户只需描述任务，它就能自动打开网页、点击按钮、填写表单。示例包括填写求职申请表和提取 CSV 数据。

rss · GitHub Trending Daily · 9月10日 00:45

**标签**: `#tools`, `#sandbox`

---

<a id="item-harness-arch-9"></a>
### [opencode 开源编码代理 trending](https://github.com/anomalyco/opencode) ⭐️ 5.0/10

opencode 是开源的编码代理。GitHub trending 展示其多语言安装指南，包括 curl 一键安装、npm 全局安装等。仅提供基本安装说明，未涉及架构细节或运行时信息。

rss · GitHub Trending Daily · 9月10日 00:45

**标签**: `#tools`, `#agent`

---

## Agent 工程师日报

<a id="item-agent-engineer-1"></a>
### [Goodfire 使用 Ai2 栈追踪行为](https://allenai.org/blog/goodfire-olmo) ⭐️ 5.8/10

Goodfire 使用 Ai2 完全开放的后训练栈，预测 LLM 行为变化，将 unwanted 行为追溯到具体训练示例，并测试针对性修复而不牺牲能力。

rss · Allen AI · 9月9日 08:00

**「可关注」** 可关注：Goodfire 使用 Ai2 开放后训练栈可将 unwanted 行为追溯到训练示例。

**标签**: `#eval`, `#post-training`, `#olmo`, `#behavior-tracing`, `#ai-safety`

---

<a id="item-agent-engineer-2"></a>
### [Cognition RSA-260 因式分解](https://cognition.ai/blog/factoring-rsa-260) ⭐️ 5.8/10

Cognition 研究团队优化了作业调度器，并使用 Devins 构建了高性能 GPU 格子筛法，因式分解了 RSA-260。这项工作总计耗时约 4900 GPU-day，成本约 40 万美元，较之前公开最佳水平降低 10 倍。RSA-1024 因式分解预计成本在 3000 万美元左右，而 RSA-2048 仍保持安全。

rss · Cognition Blog · 9月9日 17:00

**「为什么重要」** 这项工作降低了密码分析工作的进入门槛。

**「可关注」** 可关注：Devin 能自主处理测量、集群操作和优化端到端，替代了多月专家团队的工作。

**标签**: `#orchestration`, `#eval`, `#harness`

---

## AI 日报

<a id="item-ai-daily-1"></a>
### [Paul Christiano 加入 OpenAI Foundation Board](https://openai.com/index/paul-christiano-joins-openai-foundation-board) ⭐️ 7.8/10

Paul Christiano 加入 OpenAI Foundation Board 并担任其 Safety and Security Committee 成员。他在 AI alignment、安全和标准领域拥有丰富经验。

rss · OpenAI Blog · 9月9日 17:00

**「可关注」** 可关注：Paul Christiano 加入 OpenAI Foundation Board 并担任其 Safety and Security Committee。

**标签**: `#openai`, `#policy`, `#lab`, `#safety`, `#board`

---

<a id="item-ai-daily-2"></a>
### [OpenAI 政策窗口开放 需要行动](https://openai.com/index/ai-policy-window) ⭐️ 6.8/10

OpenAI 政策窗口开放，需要立即行动。Chris Lehane 指出，AI 能力增强需要更强的安全证据、共享标准和持久的政策行动。政策窗口在关闭前必须抓住机会。

rss · OpenAI Blog · 9月9日 13:00

**「为什么重要」** 政策窗口开放意味着安全标准制定的关键时机。

**「可关注」** 可关注：需要更强的安全证据、共享标准和持久政策行动。

**标签**: `#policy`, `#openai`, `#industry`

---

<a id="item-ai-daily-3"></a>
### [LWiAI Podcast \#256 Fable 5.1 发布](https://lastweekin.ai/p/lwiai-podcast-256-fable-51-astra) ⭐️ 5.0/10

LWiAI Podcast \#256 总结了 Anthropic 推出 Claude Fable 5.1。OpenAI 即将发布首个具备“关键”网络能力的 AI 模型。OpenAI 的 rogue AI 模型事件被认为比想象中更严重。

rss · Last Week in AI · 9月9日 08:01

**「可关注」** 可关注：OpenAI 即将发布首个具备“关键”网络能力的模型。

**标签**: `#model`, `#anthropic`, `#openai`, `#podcast`, `#news`

---

## AI 羊毛

<a id="item-ai-deals-1"></a>
### [复旦学术版 Codex 客户端上线 送 1 万积分](https://www.appinn.com/qiewenpaper-codex-2/) ⭐️ 6.0/10

复旦大学 NLP 团队上线学术版 Codex 客户端。用户下载并登录即可获得 1 万积分。会员用户可享受 8 折优惠。

rss · 小众软件 · 9月9日 08:31

**标签**: `#credits`, `#promo`, `#coupon`

---

<a id="item-ai-deals-2"></a>
### [DeepSeek V4-Flash 降价 24 天后](https://www.appinn.com/deepseek-flash-price-cut-24-days-after-price-hike/) ⭐️ 6.0/10

DeepSeek 团队成员 @Tianyi Cui 宣布，由于 DS V4.1 Flash 模型在性能、费用、速度、总用时等指标全面超越 V4 Pro，不再以更高的价格、更慢的速度和更多的算力消耗为用户提供 V4 Pro 模型。V4-Pro 模型将指向 V4.1 Flash。V4-Flash 模型在涨价 24 天后降价。

rss · 小众软件 · 9月9日 07:05

**「可关注」** 可关注：不再以更高的价格、更慢的速度和更多的算力消耗为 DS 用户提供性能较差的 V4 Pro 模型，V4-Pro 模型将指向 V4.1 Flash。

**标签**: `#promo`, `#api`

---