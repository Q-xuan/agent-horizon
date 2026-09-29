---
layout: default
title: "Horizon Summary: 2026-09-29 (ZH)"
date: 2026-09-29
lang: zh
---

> 从 202 条内容中筛选出 20 条重要资讯。

---

**Harness 架构**
1. [MCP TypeScript SDK 1.31.0 发布](#item-harness-arch-1) ⭐️ 8.8/10
2. [modelcontextprotocol/typescript-sdk released @modelcontextprotocol/core@2.2.0](#item-harness-arch-2) ⭐️ 8.3/10
3. [Codex rust-v0.158.0 发布](#item-harness-arch-3) ⭐️ 7.8/10
4. [crewAIInc/crewAI released 1.15.23](#item-harness-arch-4) ⭐️ 6.8/10
5. [2.1.284](#item-harness-arch-5) ⭐️ 6.8/10
6. [LangChain 1.4.3 发布](#item-harness-arch-6) ⭐️ 6.3/10
7. [langchain-ai/langchain released langchain-fireworks==1.7.0](#item-harness-arch-7) ⭐️ 6.3/10

**Agent 工程师日报**
1. [Claude Sonnet 5.5 发布](#item-agent-engineer-1) ⭐️ 8.0/10
2. [拆分 Prefill 与 Decode 量化](#item-agent-engineer-2) ⭐️ 8.0/10
3. [Holo4: powering generalist computer-use agents](#item-agent-engineer-3) ⭐️ 6.8/10
4. [llm-anthropic 0.30 发布](#item-agent-engineer-4) ⭐️ 6.3/10
5. [Supporting native Rust in Workers with the new Emscripten target for wasm-bindgen](#item-agent-engineer-5) ⭐️ 6.3/10
6. [Sonnet 5.5 发布](#item-agent-engineer-6) ⭐️ 6.0/10
7. [Cloudflare 推 agentic CLI](#item-agent-engineer-7) ⭐️ 5.5/10
8. [EMem-Bench 提出具身记忆基准](#item-agent-engineer-8) ⭐️ 5.5/10
9. [AdaTutoRank 优化文档集合重排](#item-agent-engineer-9) ⭐️ 5.5/10

**AI 日报**
1. [OpenAI 为澳大利亚政府网站事件致歉](#item-ai-daily-1) ⭐️ 8.8/10
2. [How we found 24 Android vulnerabilities using our open source AI security agent](#item-ai-daily-2) ⭐️ 8.3/10
3. [OpenAI 扩展 Lenfest 协作项目](#item-ai-daily-3) ⭐️ 6.8/10

**AI 羊毛**
1. [OpenCode、Command Code 送 6 倍 DeepSeek 额度](#item-ai-deals-1) ⭐️ 8.0/10

---

## Harness 架构

<a id="item-harness-arch-1"></a>
### [MCP TypeScript SDK 1.31.0 发布](https://github.com/modelcontextprotocol/typescript-sdk/releases/tag/1.31.0) ⭐️ 8.8/10

MCP TypeScript SDK 1.31.0 发布，核心变更是 OAuth 凭据与签发授权服务器绑定。存储的 token 和 client information 新增 \`issuer\` 字段，构造 \`ClientCredentialsProvider\`、\`PrivateKeyJwtProvider\`、\`StaticPrivateKeyJwtProvider\` 时必须传入 \`expectedIssuer\`，否则触发弃用警告。拒绝未知字段的存储实现需同步放开该字段。

github · felixweinberger · 9月28日 18:52

**「设计要点」** SDK 在 OAuth 凭据持久化层引入 issuer 绑定，防止跨授权服务器凭据混用。构造 provider 时显式声明 \`expectedIssuer\`，将签发方校验前移到客户端初始化阶段。

**「改了什么」** 存储的 OAuth tokens 与 client information 增加 \`issuer\` 字段。\`ClientCredentialsProvider\`、\`PrivateKeyJwtProvider\`、\`StaticPrivateKeyJwtProvider\` 的构造参数新增 \`expectedIssuer\`，缺失时标记为弃用。

**标签**: `#mcp`, `#permissions`, `#runtime`

---

<a id="item-harness-arch-2"></a>
### [modelcontextprotocol/typescript-sdk released @modelcontextprotocol/core@2.2.0](https://github.com/modelcontextprotocol/typescript-sdk/releases/tag/%40modelcontextprotocol/core%402.2.0) ⭐️ 8.3/10

MCP TypeScript SDK v2.2.0 deprecates OAuth provider construction without expectedIssuer and adds AuthorizationServerMismatchError validation in fetchToken\(\).

github · github-actions\[bot\] · 9月28日 19:07

**标签**: `#mcp`, `#tools`, `#permissions`, `#runtime`

---

<a id="item-harness-arch-3"></a>
### [Codex rust-v0.158.0 发布](https://github.com/openai/codex/releases/tag/rust-v0.158.0) ⭐️ 7.8/10

Codex rust-v0.158.0 发布。MCP 服务器支持预注册 OAuth client secret，通过 \`codex mcp add --oauth-client-secret\` 配置。exec-server WebSocket 直连启用 bearer token 认证，app-server 连接同样覆盖。提权命令默认开启终端输入审批，runtime-only 授权不再触发审查。修复 Windows、Linux、macOS 沙箱缺陷，涉及 Win10 路径、嵌套可写根、Git 元数据保护与系统路径别名。

github · github-actions\[bot\] · 9月28日 05:07

**「设计要点」** WebSocket 认证提取至 \`codex-websocket-auth\`，exec-server 与 app-server 统一 bearer token 校验。会话代理操作经 \`AgentControl\` 路由，V2 上下文与子代理加载收敛到同一控制器。沙箱层修复跨平台路径解析与元数据保护，审批逻辑区分提权命令与 runtime-only 授权。

**「改了什么」** 新增 MCP OAuth client-secret 配置、WebSocket bearer token 认证、提权命令默认终端审批。沙箱修复覆盖 Windows 10 路径、Linux 嵌套可写根与 macOS 路径别名。

**标签**: `#mcp`, `#permissions`, `#sandbox`, `#runtime`, `#tools`

---

<a id="item-harness-arch-4"></a>
### [crewAIInc/crewAI released 1.15.23](https://github.com/crewAIInc/crewAI/releases/tag/1.15.23) ⭐️ 6.8/10

crewAI 1.15.23 adds native Gemini 3.8 Flash support, improves evaluation tracing and platform integration UX, and includes multiple bug fixes.

github · lorenzejay · 9月28日 21:14

**标签**: `#eval`, `#runtime`, `#tools`

---

<a id="item-harness-arch-5"></a>
### [2.1.284](https://code.claude.com/docs/en/changelog#2-1-284) ⭐️ 6.8/10

Claude Code 2.1.284 adds Sonnet 5.5 as the default model, refines auto-mode read permissions with a &\#x27;ask again next time&\#x27; option, and introduces spend-limit display and effort-slider keybindings.

rss · Claude Code Changelog · 9月28日 18:15

**标签**: `#permissions`, `#tools`, `#sandbox`

---

<a id="item-harness-arch-6"></a>
### [LangChain 1.4.3 发布](https://github.com/langchain-ai/langchain/releases/tag/langchain%3D%3D1.4.3) ⭐️ 6.3/10

LangChain 1.4.3 补丁发布。init\_chat\_model 新增 Bedrock Mantle 聊天模型支持。修复 create\_agent 中无效工具调用的问题，并清理 fallback 模型的缓存设置。同时让 GPT-6 结构化输出在无 profiles 时也能被识别。

github · github-actions\[bot\] · 9月28日 20:17

**「改了什么」** init\_chat\_model 新增 Bedrock Mantle 聊天模型支持。create\_agent 修复无效工具调用，fallback 模型缓存设置得到清理，GPT-6 结构化输出在无 profiles 时可被识别。anyio 从 4.11.0 升级到 4.14.2。

**标签**: `#runtime`, `#tools`, `#prefix-cache`

---

<a id="item-harness-arch-7"></a>
### [langchain-ai/langchain released langchain-fireworks==1.7.0](https://github.com/langchain-ai/langchain/releases/tag/langchain-fireworks%3D%3D1.7.0) ⭐️ 6.3/10

Minor 1.7.0 release of langchain-fireworks adds a prompt caching middleware and fixes mid-stream timeout classification, with no detailed technical notes.

github · github-actions\[bot\] · 9月28日 20:46

**标签**: `#prefix-cache`, `#runtime`, `#eval`

---

## Agent 工程师日报

<a id="item-agent-engineer-1"></a>
### [Claude Sonnet 5.5 发布](https://simonwillison.net/2026/Sep/28/claude-sonnet-5-5/) ⭐️ 8.0/10

Anthropic 发布 Claude Sonnet 5.5，官方称比 Sonnet 5 快 30% 以上、多数任务成本最多降低 30%，定价与 Sonnet 5 持平。Simon Willison 实测发现，该模型在 max 思考档位下复现 Opus 5.5 缺陷：思考 128,000 tokens、花费 1.28 美元后耗尽 token，未产出 SVG；同一任务改用 xhigh 档位后，耗时 41 秒、花费 5.74 美分并成功生成。Sonnet 5.5 已上线 claude.ai 免费档，部分编码任务表现接近 Opus 5.5。

rss · Simon Willison · 9月28日 22:07

**「为什么重要」** 对 coding agent 与 harness 开发者而言，Sonnet 5.5 的定价与速度变化直接影响推理成本模型；max 思考档位的高成本无产出失败也提示，在 agent 循环中需要为高思考预算设置超时与 token 上限。

**「可关注」** 可关注：接入 Sonnet 5.5 时，max 思考档位存在 128,000 tokens 无产出风险，可先用 xhigh 档位验证成本与成功率，再决定是否提升思考预算。

**标签**: `#coding-agent`, `#eval`, `#observability`, `#harness`

---

<a id="item-agent-engineer-2"></a>
### [拆分 Prefill 与 Decode 量化](https://huggingface.co/papers/2609.26333) ⭐️ 8.0/10

HF 论文提出 disaggregated quantization（DQ），把 prefill 与 decode 的量化策略拆开：prefill 用低精度计算加速 prompt 处理，decode 用紧凑权重降低显存带宽。在 Qwen 3 和 Gemma 3 上，decode 阶段去掉激活量化即可提升 decode 密集任务的准确率，且不增加推理成本。训练独立的 compute-native prefill 权重后，prompt 处理速度超过 weight-only 推理，并在 2–3-bit decode 下匹配或超过其准确率。作者发布 Qwen3.8-27B GGUF 解码器，配合 NVFP4 prefiller 将 1-bit 准确率提高 32.5 个百分点。

rss · Hugging Face Daily Papers · 9月29日 02:27

**「为什么重要」** Prefill 与 decode 的瓶颈不同，统一量化精度往往只优化一侧。该论文给出拆分方案与可直接使用的 GGUF 工件，为 coding agent 在长上下文与多轮生成场景下的显存、延迟取舍提供新选项。

**「可关注」** DQ 把 prefill 与 decode 的计算格式、权重和存储位置分开优化。论文报告在 Qwen 3 与 Gemma 3 上，decode 去激活量化不增推理成本即提升准确率；2–3-bit decode 下，compute-native prefill 权重加速 prompt 处理且准确率匹配或超过 weight-only 推理。

**标签**: `#memory`, `#eval`, `#harness`

---

<a id="item-agent-engineer-3"></a>
### [Holo4: powering generalist computer-use agents](https://huggingface.co/blog/Hcompany/holo4) ⭐️ 6.8/10

Hugging Face announces Holo4, a new series of generalist computer-use agent models available in 27B dense and 35B-A3B MoE sizes with open trajectories and an API.

rss · Hugging Face Blog · 9月28日 09:44

**标签**: `#coding-agent`, `#mcp`, `#eval`, `#harness`

---

<a id="item-agent-engineer-4"></a>
### [llm-anthropic 0.30 发布](https://github.com/simonw/llm-anthropic/releases/tag/0.30) ⭐️ 6.3/10

llm-anthropic 0.30 于 2026-09-28 发布，新增 Claude Sonnet 5.5 支持，并加入 \`llm anthropic refresh\`、\`llm anthropic models\` 和 \`llm anthropic count\` 三个命令。refresh 从 Anthropic models API 拉取可用模型并缓存到 \`anthropic\_models.json\`，未知模型按 API 回报的能力注册；models 命令列出当前 API key 可用的模型，\`--json\` 可查看完整能力；count 命令调用 token counting API 统计输入 token 而不执行 prompt，参数与 \`llm prompt\` 一致，Python 侧对应 \`model.count\_tokens\(\)\`。同时修复了对话中拒绝后续 prompt 报 400 错误的问题。

github · simonw · 9月28日 23:06

**「为什么重要」** 对使用 LLM CLI 管理 Anthropic 模型的工程师，token 计数和模型列表缓存减少了盲试和手动查文档的成本；拒绝后的对话修复则移除了一个会中断多轮流程的硬错误。

**「可关注」** 可关注：\`llm anthropic count\` 与 \`model.count\_tokens\(\)\` 提供了不触发推理的 token 预估路径，适合在 harness 中做上下文预算和成本控制。

**标签**: `#harness`, `#observability`, `#coding-agent`

---

<a id="item-agent-engineer-5"></a>
### [Supporting native Rust in Workers with the new Emscripten target for wasm-bindgen](https://blog.cloudflare.com/rust-workers-emscripten-target/) ⭐️ 6.3/10

Cloudflare announces experimental first-class support for the Emscripten wasm32-unknown-emscripten target in wasm-bindgen, allowing native Rust and Tokio-based applications to run on Workers.

rss · Cloudflare Engineering · 9月28日 13:00

**标签**: `#toolchain`, `#rust`, `#wasm`, `#cloudflare-workers`

---

<a id="item-agent-engineer-6"></a>
### [Sonnet 5.5 发布](https://www.anthropic.com/claude-sonnet-5-5) ⭐️ 6.0/10

Anthropic 发布 Sonnet 5.5。Hacker News 讨论指出，该模型在 Terminal-Bench 上得分 70.6，高于 Opus 5.5 的 66.4；但 Opus 5.5 有 10% 的试验因安全防护回退到备用模型，Sonnet 5.5 仅 1.5%，分差可能主要由回退率差异造成。系统卡第 8.5 节显示，Sonnet 5.5 网络安全能力较 Sonnet 5 显著提升，因此部署了与 Opus 5.5 类似的防护，高风险网络安全任务会回退到 Sonnet 5。社区同时讨论其定价远高于 GLM、DeepSeek 等中国模型，以及 Opus 5.5 在 5x 计划下已足够日常使用。

hackernews · D2OQZG8l5BI1S06 · 9月28日 17:58 · [社区讨论](https://news.ycombinator.com/item?id=49881850)

**「为什么重要」** Terminal-Bench 分数差距可能由安全回退率差异解释，提示 benchmark 结果未必直接等价于模型能力。Sonnet 5.5 对高风险网络安全任务回退到 Sonnet 5，也改变了 coding agent 在安全敏感场景下的使用范围。

**「可关注」** 可关注：在对比 Terminal-Bench 等 agent 评测时，需核查系统卡中的安全回退比例，避免将策略干预误读为模型性能差异。

**「评论」** 社区对 Sonnet 5.5 的性价比和定位有分歧：有用户认为 Opus 5.5 在 5x 计划下已足够支撑 2-3 个并发会话，Sonnet 5.5 的额外并发不实用。另有用户指出 GLM、DeepSeek 等中国模型价格仅为 Anthropic 的 1/20，在非前沿场景下更具成本优势。

**标签**: `#coding-agent`, `#eval`, `#llm`, `#benchmark`, `#anthropic`

---

<a id="item-agent-engineer-7"></a>
### [Cloudflare 推 agentic CLI](https://blog.cloudflare.com/cloudflare-cf-cli-launch/) ⭐️ 5.5/10

Cloudflare 发布面向其 API 的 agentic CLI \`cf\`。材料未提供官方技术公告细节，以下信息来自 Hacker News 讨论。社区指出该 CLI 用 TypeScript 编写，可能给用户带来依赖管理负担；权限 token 的创建仍需手动在网站查找，且入口位置经常变动。另有开发者认为代理直接调用 Cloudflare REST API 并无障碍，质疑 CLI 是否为 REST 的子集。材料未包含架构细节、调用链路或评测数据。

hackernews · macleos · 9月28日 15:28 · [社区讨论](https://news.ycombinator.com/item?id=49879577)

**「为什么重要」** coding agent 与 harness 开发者可从中观察一线云厂商如何设计 agent 接口。社区对语言选型、token 获取摩擦以及 CLI 与 REST 的边界提出质疑，但材料未提供足够证据评估其实际收益或风险。

**「可关注」** 可关注：\`cf\` 目前无法自动创建权限 token，用户仍需在 Cloudflare 网站手动操作，且该入口位置频繁变动；同时有开发者表示直接 REST 调用已能满足代理需求，CLI 的能力覆盖范围尚不明确。

**「评论」** 评论分歧显著。有用户反对用随机词生成器配置生产基础设施，认为 Cloudflare 应限制此类使用；也有用户称赞 CLI 是当前较好的产品发布形态。实现层面，有评论指出 TypeScript 带来依赖管理问题，认为应使用编译型语言。实际体验上，token 配置流程被反复吐槽，REST 调用则被部分开发者视为更可靠的替代方案。

**标签**: `#coding-agent`, `#harness`, `#permissions`

---

<a id="item-agent-engineer-8"></a>
### [EMem-Bench 提出具身记忆基准](https://huggingface.co/papers/2609.28236) ⭐️ 5.5/10

Hugging Face Daily Papers 收录论文，提出具身记忆基准 EMem-Bench。该基准包含 2,554 个交互 episode，覆盖四个任务家族，评估长时程具身交互中的记忆构建与更新。论文指出现有智能体存在四项记忆缺陷：细粒度视觉记忆弱、动态世界状态跟踪不可靠、未记录交互结果揭示的世界状态、从先前经验泛化有限。当前仅公开摘要，缺少代码、实验结果与架构细节；对一般 Agent 工程师而言，影响范围较窄，需完整论文才能评估。

rss · Hugging Face Daily Papers · 9月29日 00:00

**「为什么重要」** 现有基准未直接评估长时程具身交互中的记忆能力，该论文试图填补这一空白。但摘要未提供实验数据或代码，基准的实际区分度与可用性仍待全文验证。

**「可关注」** 可关注：论文归纳的四项记忆缺陷为长时程任务提供了评估维度，但摘要未含代码与实验结果，工程落地需等待全文与开源实现。

**标签**: `#eval`, `#memory`, `#benchmark`

---

<a id="item-agent-engineer-9"></a>
### [AdaTutoRank 优化文档集合重排](https://huggingface.co/papers/2609.32472) ⭐️ 5.5/10

2026-09-29，Hugging Face Daily Papers 收录论文 AdaTutoRank，针对 RAG 与深度研究中的文档集合重排。现有重排器按相关性匹配选文档，难以构成复杂信息需求所需的完整、互补、非冗余集合；先前工作以集合级聚合分数为目标，但该标量由集合中所有文档共享，信用分配稀疏——冗余文档可能搭便车，关键文档可能被连带惩罚。AdaTutoRank 提出自适应辅导优化应对该问题，材料未展示完整方法细节与实验数据。

rss · Hugging Face Daily Papers · 9月29日 00:00

**「为什么重要」** 对做 RAG 与深度研究的工程师，重排器直接决定下游模型看到什么证据；集合级奖励的信用分配缺陷可能让检索结果包含冗余或遗漏关键文档。该方法尚未验证对端到端效果的影响，但指出了一个具体的监督信号设计问题。

**「可关注」** 可关注：AdaTutoRank 将重排目标从单文档相关性转向集合组合，并试图用自适应辅导优化解决共享标量奖励中的搭便车问题；材料未给出实验数据，实际效果待验证。

**标签**: `#rag`, `#deep-research`, `#eval`, `#optimization`

---

## AI 日报

<a id="item-ai-daily-1"></a>
### [OpenAI 为澳大利亚政府网站事件致歉](https://openai.com/index/how-we-will-do-better-for-australia) ⭐️ 8.8/10

OpenAI 官方博客发文，就涉及澳大利亚政府网站的事件致歉。文章称将强化安全防护措施，并为澳大利亚网络安全防御提供更多支持。该政策调整目前限于澳大利亚区域，未提及全球性变更。

rss · OpenAI Blog · 9月29日 01:00

**「为什么重要」** OpenAI 公开致歉并宣布区域化安全支持，显示主要实验室开始针对具体国家调整防护策略。关注服务边界与合规风险的工程师，可将此区域政策纳入观察。

**「可关注」** 可关注：OpenAI 为澳大利亚列出的具体防护与支持措施，及其区域化执行方式。

**标签**: `#policy`, `#industry`, `#lab`

---

<a id="item-ai-daily-2"></a>
### [How we found 24 Android vulnerabilities using our open source AI security agent](https://github.blog/security/how-we-found-24-android-vulnerabilities-using-our-open-source-ai-security-agent/) ⭐️ 8.3/10

GitHub 官方博客介绍其开源 AI 安全代理通过定向任务流发现 24 个 Android 漏洞，并开放该工具供用户自行运行。

rss · GitHub Blog · 9月28日 19:00

**标签**: `#open-source`, `#industry`, `#product`, `#lab`

---

<a id="item-ai-daily-3"></a>
### [OpenAI 扩展 Lenfest 协作项目](https://openai.com/index/lenfest-ai-collaborative-expansion) ⭐️ 6.8/10

OpenAI 宣布扩展 Lenfest AI Collaborative 与 Fellowship Program。新增 500 万美元资金，并配套至多 500 万美元软件额度与工程支持。该项目为慈善性质扩展，不涉及核心模型或产品更新。

rss · OpenAI Blog · 9月28日 07:00

**「为什么重要」** 此次扩展体现 OpenAI 在核心产品之外的资源投放，但属于慈善项目，对模型能力与开发工具链无直接技术影响。

**「可关注」** 可关注：至多 500 万美元软件额度与工程支持的兑现形式，材料未披露具体细节。

**标签**: `#lab`, `#industry`, `#product`

---

## AI 羊毛

<a id="item-ai-deals-1"></a>
### [OpenCode、Command Code 送 6 倍 DeepSeek 额度](https://www.appinn.com/opencode-vs-command-code-ai-coding-plans/) ⭐️ 8.0/10

OpenCode 与 Command Code 先后宣布，$10/月 套餐中 DeepSeek V4.1 Flash 使用额度永久提升至 $60/月。OpenCode 调整 Go 套餐，Command Code 调整 GOAT 套餐。$10 换 $60，额度放大 6 倍。材料未提及领取门槛与截止时间。

rss · 小众软件 · 9月28日 08:17

**「为什么重要」** 两家工具在 $10/月 价位上把 DeepSeek V4.1 Flash 额度拉到 $60/月，做 coding agent 的开发者可以按套餐差异比价。

**「可关注」** 可关注：OpenCode Go 套餐与 Command Code GOAT 套餐均将 DeepSeek V4.1 Flash 额度永久提至 $60/月，月费 $10；材料未说明是否限新用户或存在其他调用限制。

**标签**: `#promo`, `#credits`, `#api`

---