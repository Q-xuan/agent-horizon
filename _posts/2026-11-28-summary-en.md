---
layout: default
title: "Horizon Summary: 2026-11-28 (EN)"
date: 2026-11-28
lang: en
---

> From 161 items, 9 important content pieces were selected

---

**Agent Harness Architecture**
1. [MCP servers v2.6.0 安全修复发布](#item-harness-arch-1) ⭐️ 7.8/10
2. [pydantic-ai v2.76.0 发布](#item-harness-arch-2) ⭐️ 6.8/10

**AI Agent Engineer**
1. [OS-Omni 跨平台智能体基准发布](#item-agent-engineer-1) ⭐️ 7.0/10
2. [AI 编码智能体视觉推理击败视频模型](#item-agent-engineer-2) ⭐️ 7.0/10
3. [DRBench Pro 知识覆盖基准发布](#item-agent-engineer-3) ⭐️ 7.0/10
4. [HF 每日论文：AI 代理数据库错误损害研究](#item-agent-engineer-4) ⭐️ 7.0/10

**AI Daily**
1. [Rosetta 开源 终结基模学新忘旧](#item-ai-daily-1) ⭐️ 5.5/10
2. [科技爱好者周刊 Issue 421：盘点AI造富与科技新动态](#item-ai-daily-2) ⭐️ 5.0/10

**AI Deals**
1. [NodeWarden 更新：Cloudflare 免费密码管理器](#item-ai-deals-1) ⭐️ 8.0/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [MCP servers v2.6.0 安全修复发布](https://github.com/modelcontextprotocol/servers/releases/tag/v2.6.0) ⭐️ 7.8/10

modelcontextprotocol/servers 发布 v2.6.0，修复 4 个常用 MCP 服务器中的 8 个安全漏洞，并完成 v2.5.0 遗留的 2 项修复。mcp-server-git 修复 Git LFS 远程代码执行、仓库路径遍历、凭据泄露等 6 项漏洞，补全写操作后仓库边界重校验。@modelcontextprotocol/server-memory 修复符号链接权限提升，mcp-server-fetch 补全 robots.txt 绕过。需升级 mcp-server-git 至 2026.11.27、@modelcontextprotocol/server-memory 至 2.2.2、mcp-server-fetch 至 2026.11.27，Windows 用户还需升级 @modelcontextprotocol/server-filesystem 至 2.4.1。

github · cliffhall · Nov 27, 09:51

**「设计要点」** mcp-server-git 在启动时记录根仓库的 Git 目录，拒绝指向外部仓库的 --repository 路径，并在每次写操作后重复校验仓库边界。memory 服务器改用独占临时文件句柄写入，防止符号链接交换导致的权限提升。

**「改了什么」** 相对 v2.5.0，v2.6.0 完成两项遗留修复：mcp-server-git 写操作后仓库边界重校验，以及 mcp-server-fetch 的 robots.txt 反斜杠与路径参数绕过。同时修复 mcp-server-git 的 Git LFS 远程代码执行、仓库路径遍历等 6 项漏洞，@modelcontextprotocol/server-memory 的符号链接权限提升漏洞，以及 @modelcontextprotocol/server-filesystem 在 Windows 上的目录遍历漏洞。

**Tags**: `#mcp`, `#tools`, `#permissions`, `#memory`

---

<a id="item-harness-arch-2"></a>
### [pydantic-ai v2.76.0 发布](https://github.com/pydantic/pydantic-ai/releases/tag/v2.76.0) ⭐️ 6.8/10

pydantic-ai v2.76.0 is released, focusing on realtime session tool dynamic update capability. It introduces \`UpdateTools\` message type and \`RealtimeModelProfile.supports\_tool\_updates\` capability flag, allowing new tool definitions to be pushed mid-session to models that support tool updates. The \`RealtimeInput\` union type gains \`UpdateTools\` member, causing existing exhaustive match code \(e.g., \`assert\_never\`\) to fail type checking; the maintainers suggest handling the branch explicitly or raising for it. Meanwhile, \`gemini-2.5-pro\` and \`gemini-2.5-flash\` start emitting \`DeprecatedModelWarning\` \(a \`UserWarning\` subclass\), breaking code that converts warnings to errors via \`filterwarnings=error\`.

github · dsfaccini · Nov 26, 23:49

**「设计要点」** The realtime tool update mechanism controls message sending per-connection via the model profile flag \`supports\_tool\_updates\`, with \`DEFAULT\_REALTIME\_PROFILE\` defaulting to \`False\` to prevent existing connections from unexpectedly receiving \`UpdateTools\`. \`GoogleInteractionsModel\` introduces a stateless Google interaction layer complementary to the stateful \`GoogleModel\`; \`pydantic-ai-pax\` is split into a standalone package with per-provider extras.

**「改了什么」** Relative to v2.75.0, v2.76.0 introduces two breaking changes: the \`RealtimeInput\` union gains \`UpdateTools\`, breaking existing \`assert\_never\` exhaustive matches; \`FileSystem.read\_file\` \`offset\` shifts from 0-indexed to 1-indexed, with \`offset=0\` now raising an error. New capabilities include mid-session tool updates in realtime \(\`UpdateTools\`\), stateless Google interactions \(\`GoogleInteractionsModel\`\), and sandboxed code output submission \(\`CodeMode\(allow\_final\_output=True\)\`\).

**Tags**: `#tools`, `#runtime`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [OS-Omni 跨平台智能体基准发布](https://huggingface.co/papers/2611.34232) ⭐️ 7.0/10

2026年11月27日Hugging Face每日论文发布OS-Omni基准介绍。该基准是实时跨平台计算机使用智能体评估环境与执行框架，针对现有基准多隔离单一环境的限制，覆盖Windows、Ubuntu、macOS、iOS、Android、Web六类平台，支持桌面与安卓手机的跨设备长时程工作流评估。v1版本每平台包含48个任务，共12组跨平台工作流，整体以每波300个任务的形式版本化发布，任务集可复现，面向通用计算机使用智能体、coding agent的研发与评估人员。

rss · Hugging Face Daily Papers · Nov 27, 00:00

**「为什么重要」** 现有计算机使用智能体基准多隔离Web、移动或桌面单一环境，无法验证智能体跨平台长时程工作流能力，OS-Omni填补了该评估空白，为通用智能体的真实场景能力验证提供了可复现的新工具。

**「可关注」** 可关注：OS-Omni 采用版本化批次发布可复现任务集，支持跨平台长时程工作流评估，可作为通用计算机使用智能体的标准化测试工具。

**Tags**: `#eval`, `#coding-agent`

---

<a id="item-agent-engineer-2"></a>
### [AI 编码智能体视觉推理击败视频模型](https://huggingface.co/papers/2611.34813) ⭐️ 7.0/10

2026-11-27，Hugging Face Daily Papers 收录论文《Solve Vision with Code》。该文提出 VBVR-Pro-Bench 视觉推理基准，在相同输入、输出规格和评估器条件下，对比 coding agent 编写程序渲染答案视频与视频生成模型直接生成视频两种路径。实验发现 coding agent 的符号推理路径表现更强，且评估使用未修改的规则基础评估器。目前仅提供摘要片段，未披露完整技术细节、性能指标或可复现信息。结果对构建或评估推理型 coding agent 的工程师有参考价值。

rss · Hugging Face Daily Papers · Nov 27, 00:00

**「为什么重要」** 该研究首次在相同条件下直接对比符号推理与原生视觉推理两条路径，挑战了“视觉原生更优”的默认假设。对正在选择视觉推理技术栈的工程师而言，这提供了一个新的评估维度。

**「可关注」** 可关注：在视觉推理任务中，代码渲染加规则评估的符号路径可能比端到端视频生成更可靠，但当前结论仅基于论文摘要，缺乏完整指标与复现细节，不宜直接作为架构选型依据。

**Tags**: `#eval`, `#coding-agent`, `#reasoning`

---

<a id="item-agent-engineer-3"></a>
### [DRBench Pro 知识覆盖基准发布](https://huggingface.co/papers/2611.34852) ⭐️ 7.0/10

2026 年 11 月 27 日，Hugging Face Daily Papers 收录一篇 arXiv 预印本，提出 DRBench Pro 知识覆盖基准，获 17 次赞同。该基准以结构化知识覆盖为首要评测目标，通过自动化管道从 Wikipedia 构建局部知识树，采样子图生成研究查询与基于证据的评分细则，每条细则对应知识树中的一条关系。智能体仅接收研究查询，评测据此衡量研究方向的广度与深度。当前材料截断，且该基准尚未正式发布、缺乏广泛生产验证，可信度中等。

rss · Hugging Face Daily Papers · Nov 27, 00:00

**「为什么重要」** 对构建或评测深度研究智能体及其评估 harness 的工程师而言，该基准首次将结构化知识覆盖作为核心评测维度，填补了现有评测的空白。但预印本状态意味着其评分体系与子图采样策略尚未经社区大规模复现验证。

**「可关注」** 可关注：其基于 Wikipedia 知识树子图采样生成关系绑定评分细则的自动化管道，可作为现有深度研究智能体评估 harness 的结构化知识覆盖度量的参考实现。

**Tags**: `#eval`, `#deep-research-agent`, `#benchmark`

---

<a id="item-agent-engineer-4"></a>
### [HF 每日论文：AI 代理数据库错误损害研究](https://huggingface.co/papers/2611.30483) ⭐️ 7.0/10

2026年11月27日Hugging Face Daily Papers推送一篇预注册研究论文，实验探究AI代理操作生产数据库出错时损害的决定因素，测试变量覆盖模型类型、数据库前置防护层、数据库引擎、权限设置、恢复机制，直接关联AI代理安全、工具开发与评估设计领域。研究分两层开展：Layer A无模型参与，通过脚本施加22个标准化错误，测试4种关系型引擎在5种权限配置、2种恢复配置下的表现，共覆盖792个测试单元、874次恢复演练（含10分钟重复测试）；Layer B使用6个小开源权重模型（4B至12B参数，另加1个35B混合专家模型）驱动极简工具调用代理开展测试。当前公开的论文摘要被截断，完整研究结论尚未披露。

rss · Hugging Face Daily Papers · Nov 27, 00:00

**「为什么重要」** 该研究针对AI代理操作生产数据库出错的高优先级安全问题，通过结构化实验测试了多个与代理安全、工具设计直接相关的变量，是目前少有的针对该场景的预注册实证研究。目前完整结论未披露，其实证结果后续可支撑代理数据库工具的风险评估与防护设计。

**「可关注」** 可关注：该研究的预注册实验设计覆盖了无模型脚本错误、小模型驱动代理两类测试场景，以及引擎、权限、恢复等多类变量，完整结果披露后可对照自身代理数据库工具的设计缺口。

**Tags**: `#eval`, `#permissions`, `#coding-agent`, `#harness`

---

## AI Daily

<a id="item-ai-daily-1"></a>
### [Rosetta 开源 终结基模学新忘旧](https://mp.weixin.qq.com/s?__biz=MzA3MzI4MjgzMw==&amp;mid=2651076720&amp;idx=2&amp;sn=d375259d0dfaea462ea23093a9ae08bd) ⭐️ 5.5/10

港科大与腾讯混元联合提出的原生多模态预训练方案Rosetta已被NeurIPS 2026接收，目前已全面开源全套预训练、推理、评测代码及模型权重，支持单卡至千卡集群部署。该方案针对基模迭代新能力时需从头重训、联合训练引发灾难性遗忘的痛点，提出组合式架构设计，在总参数与标准MoE一致的前提下，避免加入新任务时原有能力退化。实验显示，标准MoE与MoT在加入生图任务后，语言与代码能力评测分数直接跌至0分，而Rosetta可稳定保留基模能力并生成高质量图像。

rss · 机器之心 · Nov 27, 09:00

**「为什么重要」** 当前多模态基模迭代普遍面临“学新忘旧”的资源浪费问题，Rosetta提供了无需重训即可扩展新能力的通解，同时解决了原生多模态预训练中长期存在的模态协同与能力保留两难。

**「可关注」** 可关注：Rosetta 采用统一注意力层搭配组合式FFN的架构，通过梯度动量对齐机制，在不增加总参数预算的前提下避免联合训练时的路由坍缩与能力退化。

**Tags**: `#model`, `#open-source`, `#lab`, `#industry`

---

<a id="item-ai-daily-2"></a>
### [科技爱好者周刊 Issue 421：盘点AI造富与科技新动态](http://www.ruanyifeng.com/blog/2026/11/weekly-issue-421.html) ⭐️ 5.0/10

阮一峰科技爱好者周刊第421期围绕AI行业造富展开，提及Anthropic上市带来的员工财富效应，据第三方统计其约5300名可分股票员工中，2023年入职者获利中位数达1.51亿美元，2024年入职者为7900万美元，上市一次性造就约600名亿万富翁。同期内容还提及小鹏公司展示人形机器人、维基百科真人访问量创历史新低、综合17个编码基准的编程模型排名等科技动态。该内容为第三方周刊转载，无官方一手信源支持，可核验的实质性新事实有限。

rss · 阮一峰 · Nov 27, 00:10

**「为什么重要」** 本期内容呈现了AI行业造富的极端案例，同时披露了维基百科真人访问量持续下滑、主流系统拟自动截图训练模型等行业趋势，对关注AI产业影响与个人隐私风险的读者有参考价值。

**「可关注」** 可关注：综合17个编码基准的编程模型排名中，国产模型Qwen 4 Max、Kimi K3.1 Pro、Deepseek V.1 Flash分别位列第10、12、14位，可作为编码场景选型参考。

**Tags**: `#model`, `#lab`, `#industry`

---

## AI Deals

<a id="item-ai-deals-1"></a>
### [NodeWarden 更新：Cloudflare 免费密码管理器](https://www.appinn.com/nodewarden-update-1/) ⭐️ 8.0/10

你看到的内容可能由第三方 AI 基于小众软件文章提炼总结而成，可能与原文真实意图存在偏差。不代表小众软件观点和立场。请&lt;a href=&quot;https://www.appinn.com/nodewarden-update-1/&quot; target=&quot;\_blank&quot;&gt;点击链接阅读原文&lt;/a&gt;细致比对和校验。&lt;br /&gt;&lt;br /&gt;NodeWarden 是开源自托管密码管理器，可直接部署在 Cloudflare Workers 上，无需自有服务器，依托 Cloudflare 免费额度即可运行，兼容 Bitwarden 官方全系列客户端。本次更新新增离线 PWA 使用、自动云备份、多用户管理、密码安全检测、更多双因素认证方式等功能，原 Bitwarden 付费的 TOTP 动态验证码生成功能也可免费使用。

rss · 小众软件 · Nov 27, 09:13

**「为什么重要」** 本次更新补齐了自托管密码管理器常见的离线访问、自动备份等核心能力，且仍无需自有服务器、可在 Cloudflare 免费额度内运行，对希望低成本自建密码库的用户仍有实用价值。

**「可关注」** 可关注：升级旧版本时需保留原有 JWT\_SECRET、数据库及 Durable Objects 绑定，升级前必须完整备份，同时确认 Cloudflare 环境设置的 NODE\_VERSION 为 24.22.1。

**Tags**: `#free-tier`, `#self-hosted`, `#password-manager`, `#api`

---