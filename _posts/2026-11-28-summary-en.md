---
layout: default
title: "Horizon Summary: 2026-11-28 (EN)"
date: 2026-11-28
lang: en
---

> From 172 items, 10 important content pieces were selected

---

**Agent Harness Architecture**
1. [pydantic-ai v2.77.0 发布](#item-harness-arch-1) ⭐️ 7.8/10
2. [MCP 服务器 v2.6.0 安全修复](#item-harness-arch-2) ⭐️ 6.8/10

**AI Agent Engineer**
1. [DeepCrossAttention 推理提速 3x](#item-agent-engineer-1) ⭐️ 7.0/10
2. [OS-Omni 跨平台智能体基准发布](#item-agent-engineer-2) ⭐️ 7.0/10
3. [DRBench Pro 深度研究 Agent 基准发布](#item-agent-engineer-3) ⭐️ 7.0/10
4. [HF 每日论文：AI 代理数据库损害归因研究](#item-agent-engineer-4) ⭐️ 7.0/10
5. [HF 每日论文：编码智能体视觉推理优于视频模型](#item-agent-engineer-5) ⭐️ 6.0/10

**AI Daily**
1. [港科大混元开源Rosetta 解决基模遗忘](#item-ai-daily-1) ⭐️ 5.0/10

**AI Deals**
1. [NodeWarden 更新：Cloudflare 免费密码库](#item-ai-deals-1) ⭐️ 7.0/10
2. [Google AI Pro 黑五新用户优惠](#item-ai-deals-2) ⭐️ 7.0/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [pydantic-ai v2.77.0 发布](https://github.com/pydantic/pydantic-ai/releases/tag/v2.77.0) ⭐️ 7.8/10

pydantic-ai v2.77.0 发布，新增 SQLite、Postgres、MongoDB 作为 ConversationStore 持久化后端，原 Pax 会话存储类重命名为 SqliteSessionStore 并触发 HarnessDeprecationWarning。技能加载默认跳过缺失或不可读路径，SkillCatalog 新增 advice 字段，pax 按最近目录优先搜索同名技能。流式响应在提供者终端事件前结束时标记 state=&\#x27;incomplete&\#x27;，压缩事件以 CompactionReceiptPart 替代 UserPromptPart 发送。新增 compact\_history\(\) 能力钩子与 CompactionStartEvent/CompactionEndEvent，SubAgents 跳过低于 &\#x27;operator&\#x27; 权限的磁盘子代理定义。

github · dsfaccini · Nov 27, 23:32

**「设计要点」** 框架以 ConversationStore 抽象层实现多后端持久化，通过 HarnessDeprecationWarning 兼容旧会话存储命名。权限系统通过 authority 字段控制子代理与工作目录的访问范围，SubAgents 在加载时过滤低于 &\#x27;operator&\#x27; 权限的定义文件。流式事件与压缩机制通过新增事件类型扩展 AgentStreamEvent 联合体，保持现有运行流不变。

**「改了什么」** 相对上一版本，ConversationStore 新增 SQLite、Postgres、MongoDB 后端，Pax 会话存储类重命名为 SqliteSessionStore 并保留旧导入但触发弃权警告。Skills\(\) 默认跳过缺失或不可读路径，SkillCatalog 新增 advice 字段。流式响应在终端事件前结束时标记 incomplete，压缩事件以 CompactionReceiptPart 发送。SubAgents 跳过低于 &\#x27;operator&\#x27; 权限的磁盘定义文件，fallback 子代理请求计入 UsageLimits。

**Tags**: `#memory`, `#tools`, `#compatibility`

---

<a id="item-harness-arch-2"></a>
### [MCP 服务器 v2.6.0 安全修复](https://github.com/modelcontextprotocol/servers/releases/tag/v2.6.0) ⭐️ 6.8/10

modelcontextprotocol/servers v2.6.0 是一个安全修复版本，修复了 git、memory、fetch 和 filesystem 四个服务器中的 8 个漏洞，并完成了 v2.5.0 遗留的两项修复。关键修复包括：阻止 Git LFS 过滤器执行仓库配置中命名的程序、禁止 \`--repository\` 指向其他仓库、修复 \`git\_remote\` 通过 crafted remote name/URL 泄露凭据、禁止 \`repo\_path\` 环境变量展开、隔离 objects 目录防止 alternates 文件竞争、拒绝会覆盖忽略文件的合并提交，以及 Windows 下目录 junction/symlink 检查。fetch 服务器还补全了 robots.txt 对反斜杠和路径参数的匹配。需升级 \`mcp-server-git\` 至 2026.11.27、\`@modelcontextprotocol/server-memory\` 至 2.2.2、\`mcp-server-fetch\` 至 2026.11.27，Windows 用户还需升级 \`@modelcontextprotocol/server-filesystem\` 至 2.4.1。

github · cliffhall · Nov 27, 09:51

**「改了什么」** 相对 v2.5.0，本次发布修复了 4 个 MCP 服务器中的 8 个安全漏洞，并完成了上一版本遗留的 2 项修复。git 服务器强化了仓库根目录校验、隔离了 LFS 过滤器执行、修复了凭据泄露与路径展开问题，并新增合并提交保护；memory 服务器修复了临时文件符号链接攻击；fetch 服务器补全了 robots.txt 对特殊路径的匹配；filesystem 服务器在 Windows 上增加了目录变更检测。

**Tags**: `#security`, `#mcp`, `#tools`, `#sandbox`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [DeepCrossAttention 推理提速 3x](https://research.google/blog/supercharging-transformer-residual-connections/) ⭐️ 7.0/10

Google Research 发布 DeepCrossAttention，一种针对 transformer 残差连接的优化方案。根据 Hacker News 上分享的官方博客，该技术声称在保持模型质量无显著下降的前提下，可将推理速度提升至 3 倍。该优化直接针对 LLM 推理效率，对 AI agent 系统的响应时间与运营成本有潜在影响。实际加速比受模型架构、硬件与部署配置影响，材料未提供独立基准测试数据。

hackernews · ComputedCamp995 · Nov 27, 23:06 · [Discussion](https://news.ycombinator.com/item?id=50672565)

**「为什么重要」** LLM 推理延迟是 AI agent 系统的核心约束，针对 transformer 基础结构的加速可能直接降低 agent 响应时延并减少 token 消耗。社区评论中已出现将其与 MTP、DFlash 等现有推理优化叠加讨论，表明该技术正进入实际部署栈的评估视野。

**「可关注」** 可关注：DeepCrossAttention 的残差连接修改与现有推理优化（如 MTP、DFlash）的兼容性，以及其在 agent 工作流中的实际延迟收益是否可复现。

**「评论」** 社区评论中，用户 yieldcrv 询问将 MTP 与 DFlash 与此项优化结合是否能实现更高加速比；pollorollo 指出博客图表类型使用不当；ipunchghosts 提及 DenseNet 架构对比；spankalee 猜测 Gemini Neon 的高性价比可能与此项技术相关，但未证实技术关联。

**Tags**: `#inference-optimization`, `#llm-architecture`, `#harness`

---

<a id="item-agent-engineer-2"></a>
### [OS-Omni 跨平台智能体基准发布](https://huggingface.co/papers/2611.34232) ⭐️ 7.0/10

2026年11月28日Hugging Face Daily Papers发布论文介绍OS-Omni基准，这是首个面向通用计算机使用智能体的跨平台长时程评估基准，覆盖Windows、Ubuntu、macOS、iOS、Android、Web共6个平台，解决现有智能体基准的平台孤岛问题。v1版本每个平台包含48个任务，同时提供12组跨桌面与安卓手机的长时程工作流，面向AI智能体评估系统构建者、coding agent工程师开放。

rss · Hugging Face Daily Papers · Nov 28, 04:28

**「为什么重要」** 现有计算机使用智能体基准普遍按单一平台隔离设计，无法验证智能体跨系统、跨持久应用状态的长时程工作流执行能力，OS-Omni填补了该领域的基准空白，其明确的技术规格可直接用于跨平台智能体评估体系搭建。

**「可关注」** 可关注：OS-Omni采用版本化任务发布节奏，每波新增300个任务，当前v1已提供6平台共288个单平台任务与12组跨桌面-安卓工作流，且支持可复现初始化环境，可直接集成到现有跨平台智能体评估流程中。

**Tags**: `#eval`, `#coding-agent`

---

<a id="item-agent-engineer-3"></a>
### [DRBench Pro 深度研究 Agent 基准发布](https://huggingface.co/papers/2611.34852) ⭐️ 7.0/10

Hugging Face Daily Papers 于 2026-11-28 收录论文，提出面向专业深度研究 Agent 的评测基准 DRBench Pro。该基准以结构化知识覆盖与探索深度为主要评估维度，通过 Wikipedia 本地知识树与子图采样生成研究查询及证据 grounded 评分标准，实现自动化评测。现有基准多关注报告质量，缺乏知识中心视角，DRBench Pro 填补了该空白。其流水线可复现，但当前仅基于 Wikipedia，未覆盖通用 Agent 或 coding Agent 场景。

rss · Hugging Face Daily Papers · Nov 28, 04:28

**「为什么重要」** 该基准首次将结构化知识覆盖作为主要评估目标，提供了基于 Wikipedia 的可复现自动化评测流水线，对深度研究 Agent 的评测与工具链设计有直接参考价值。但其适用场景相对垂直，尚未证实对通用 Agent 或 coding Agent 的通用改进价值。

**「可关注」** 可关注：基于 Wikipedia 知识树与子图采样的自动化评测流水线设计，以及如何将知识图谱关系映射为证据 grounded 评分标准，这对构建领域特定 Agent 评测体系有参考价值。

**Tags**: `#eval`, `#deep-research-agent`

---

<a id="item-agent-engineer-4"></a>
### [HF 每日论文：AI 代理数据库损害归因研究](https://huggingface.co/papers/2611.30483) ⭐️ 7.0/10

2026年11月28日Hugging Face每日论文收录一篇预注册实证研究，量化AI代理执行错误数据库语句时损害严重度的决定因素，对比模型选择、数据库前置防护层、数据库引擎属性三类变量的影响。研究分两层开展：Layer A用22个标准化错误脚本（无模型参与）在4种关系型引擎、5种权限方案、2种恢复方案下测试，共覆盖792个实验单元、874次恢复演练（含10分钟重复测试）；Layer B用6个开源小模型（4B至12B参数，加1个35B混合专家模型）驱动极简工具调用代理复现错误。当前研究仅覆盖小尺寸开源模型与关系型数据库场景，未验证商用大模型及非关系型数据库的表现。

rss · Hugging Face Daily Papers · Nov 28, 04:28

**「为什么重要」** 该研究针对AI代理误操作生产数据库的高影响运营风险，提供了结构化、可复现的实验范式与量化归因结果，可为数据库访问代理的防护层设计、权限配置、评估套件开发提供直接参考依据。

**「可关注」** 可关注：该研究将无模型的标准错误脚本测试与模型驱动代理测试分层设计，可参考其分层框架拆分数据库代理风险的归因变量，降低实验混淆。

**Tags**: `#permissions`, `#eval`, `#coding-agent`, `#harness`

---

<a id="item-agent-engineer-5"></a>
### [HF 每日论文：编码智能体视觉推理优于视频模型](https://huggingface.co/papers/2611.34813) ⭐️ 6.0/10

2026年11月28日Hugging Face每日论文收录了一篇视觉推理研究，该条目当前获得60次upvote。该研究提出新基准VBVR-Pro-Bench，在完全相同的任务输入、输出规格与评估规则下，对比了通过代码生成答案视频的编码智能体与视频生成模型的视觉推理能力，结果显示编码智能体可靠性更高。当前公开内容仅包含摘要片段，无详细性能指标、技术实现细节与具体量化对比结果。

rss · Hugging Face Daily Papers · Nov 28, 04:28

**「为什么重要」** 该研究首次在完全一致的条件下对比了代码生成视频的符号推理路径与视频生成模型的原生视觉推理路径，为视觉推理智能体评估提供了新的基准框架。目前仅公开摘要，具体性能差距、泛化能力等实际影响尚未证实。

**「可关注」** 可关注：相同视觉推理任务下，通过代码生成答案视频的编码智能体路径，在统一评估规则中表现出比视频生成模型更高的可靠性，或可纳入视觉推理智能体评估方案的参考范围。

**Tags**: `#eval`, `#coding-agent`

---

## AI Daily

<a id="item-ai-daily-1"></a>
### [港科大混元开源Rosetta 解决基模遗忘](https://mp.weixin.qq.com/s?__biz=MzA3MzI4MjgzMw==&amp;mid=2651076720&amp;idx=2&amp;sn=d375259d0dfaea462ea23093a9ae08bd) ⭐️ 5.0/10

港科大与腾讯混元联合提出的组合式原生多模态预训练方案Rosetta已被NeurIPS 2026接收，全套预训练、推理、评测代码及模型权重已全面开源，支持单卡至千卡集群运行。该方案用于解决基模增量学习新能力时的灾难性遗忘问题，无需从头重训基模。对比实验中，加入文生图任务后，MoE与MoT的语言能力（BBH、MBPP）跌至0分，而Rosetta在保持原有能力的同时可生成高质量图像，总参数量与标准MoE保持一致。

rss · 机器之心 · Nov 27, 09:00

**「为什么重要」** 该方案解决了原生多模态预训练长期存在的「遗忘-协同」两难困境：此前主流方案要么出现灾难性遗忘，要么结构硬隔离导致总参数量膨胀近20%且跨模态能力无法互通，Rosetta为基模低成本扩展新能力提供了可落地的工程路径。

**「可关注」** 可关注：Rosetta核心采用统一注意力层+组合式FFN的架构设计，通过动量对齐梯度缓解模态间冲突，总参数量与标准MoE对齐，已开源支持单卡至千卡集群的全流程代码与模型权重。

**Tags**: `#model`, `#open-source`, `#lab`, `#industry`

---

## AI Deals

<a id="item-ai-deals-1"></a>
### [NodeWarden 更新：Cloudflare 免费密码库](https://www.appinn.com/nodewarden-update-1/) ⭐️ 7.0/10

你看到的内容可能由第三方 AI 基于小众软件文章提炼总结而成，可能与原文真实意图存在偏差。不代表小众软件观点和立场。请&lt;a href=&quot;https://www.appinn.com/nodewarden-update-1/&quot; target=&quot;\_blank&quot;&gt;点击链接阅读原文&lt;/a&gt;细致比对和校验。开源密码管理器NodeWarden支持部署至Cloudflare Workers，无需自备服务器，可借助Cloudflare公开免费额度零成本自建兼容Bitwarden的私人密码库。本次更新新增离线PWA访问、自动云备份、多用户邀请注册、密码安全检测、免费TOTP生成等功能，老版本升级需保留原有JWT\_SECRET与数据库绑定，升级前必须完成完整备份。

rss · 小众软件 · Nov 27, 09:13

**「为什么重要」** 自建密码库的核心痛点如离线访问、自动备份、多用户管理本次更新均已补齐，且无需承担服务器成本，免费提供Bitwarden付费版专属的TOTP功能，对自托管密码库需求用户性价比极高。

**「可关注」** 可关注：升级老实例时需核对Cloudflare环境的NODE\_VERSION是否为24.22.1，且严禁重新生成原有JWT\_SECRET，否则会导致已有数据无法解密。

**Tags**: `#free-tier`, `#promo`, `#open-source`, `#self-hosted`

---

<a id="item-ai-deals-2"></a>
### [Google AI Pro 黑五新用户优惠](https://www.v2ex.com/t/1260358#reply54) ⭐️ 7.0/10

V2EX 用户分享 Google AI Pro 黑五新用户优惠，新用户订阅价格为 120 美元，较同期老用户优惠高 20 美元。材料未提及该优惠的适用地区、有效期及领取限制。

rss · V2EX Hot · Nov 27, 08:13

**「可关注」** 可关注：该优惠仅面向新用户，订阅价格 120 美元，较同期老用户优惠高 20 美元，订阅前需确认自身是否符合新用户资格。

**Tags**: `#promo`, `#api`, `#limited-offer`

---