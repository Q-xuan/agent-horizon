---
layout: default
title: "Horizon Summary: 2026-11-28 (ZH)"
date: 2026-11-28
lang: zh
---

> 从 161 条内容中筛选出 9 条重要资讯。

<nav id="ah-toc" class="ah-toc" aria-label="目录"><span class="ah-toc-title">目录</span><ul><li><a href="#sec-harness-arch"><span class="ah-toc-name">Harness 架构</span><span class="ah-toc-count">2条</span></a></li><li><a href="#sec-agent-engineer"><span class="ah-toc-name">Agent 工程师日报</span><span class="ah-toc-count">4条</span></a></li><li><a href="#sec-ai-daily"><span class="ah-toc-name">AI 日报</span><span class="ah-toc-count">2条</span></a></li><li><a href="#sec-ai-deals"><span class="ah-toc-name">AI 羊毛</span><span class="ah-toc-count">1条</span></a></li></ul></nav>

---

**[Harness 架构](#sec-harness-arch)**
1. [MCP Servers v2.6.0 安全补丁发布](#item-harness-arch-1) ⭐️ 7.8/10
2. [pydantic-ai v2.76.0 发布](#item-harness-arch-2) ⭐️ 6.8/10

**[Agent 工程师日报](#sec-agent-engineer)**
1. [OS-Omni v1 跨平台智能体基准上线](#item-agent-engineer-1) ⭐️ 7.0/10
2. [VBVR-Pro-Bench：编码智能体视觉推理胜出](#item-agent-engineer-2) ⭐️ 7.0/10
3. [DRBench Pro 基准发布](#item-agent-engineer-3) ⭐️ 7.0/10
4. [HF Daily Paper：AI 代理数据库错误损害研究](#item-agent-engineer-4) ⭐️ 7.0/10

**[AI 日报](#sec-ai-daily)**
1. [港科大混元 Rosetta 开源 解决基模遗忘](#item-ai-daily-1) ⭐️ 5.5/10
2. [Anthropic 上市造富与小鹏机器人展示](#item-ai-daily-2) ⭐️ 5.0/10

**[AI 羊毛](#sec-ai-deals)**
1. [NodeWarden 新增离线与自动备份功能](#item-ai-deals-1) ⭐️ 8.0/10

---

## Harness 架构
{: #sec-harness-arch .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-harness-arch" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-harness-arch-1"></a>
### [MCP Servers v2.6.0 安全补丁发布](https://github.com/modelcontextprotocol/servers/releases/tag/v2.6.0) ⭐️ 7.8/10

modelcontextprotocol/servers 发布 v2.6.0 安全补丁，修复 4 个 MCP 服务器共 8 个安全漏洞。mcp-server-git 修复 Git LFS 远程代码执行、仓库路径遍历、凭据泄露等关键问题；@modelcontextprotocol/server-memory 修复文件权限绕过；mcp-server-fetch 补全 robots.txt 绕过；@modelcontextprotocol/server-filesystem 修复 Windows 目录遍历。需升级至：mcp-server-git 2026.11.27、@modelcontextprotocol/server-memory 2.2.2、mcp-server-fetch 2026.11.27、@modelcontextprotocol/server-filesystem 2.4.1（仅 Windows）。TypeScript 包已从日期版本迁移至语义版本，需显式指定版本号安装。

github · cliffhall · 11月27日 09:51

**「改了什么」** 完成 v2.5.0 遗留的两项修复：mcp-server-git 的 \`--repository\` 写入后重校验，以及 server-fetch 的 robots.txt 反斜杠与路径参数匹配。新增 6 个漏洞修复，Git 服务器禁用 LFS 过滤器程序执行、禁止跨仓库根路径、隐藏远程凭据、禁止 repo\_path 环境变量展开、隔离对象存储、拒绝覆盖忽略文件的合并。TypeScript 服务器包版本号从日期格式迁移至语义化版本。

**标签**: `#mcp`, `#tools`, `#permissions`, `#memory`

---

<a id="item-harness-arch-2"></a>
### [pydantic-ai v2.76.0 发布](https://github.com/pydantic/pydantic-ai/releases/tag/v2.76.0) ⭐️ 6.8/10

pydantic-ai 发布 v2.76.0，实时会话场景新增中途动态更新工具能力，通过 \`RealtimeModelProfile.supports\_tool\_updates\` 与 \`UpdateTools\` 类型实现。\`RealtimeInput\` 联合类型新增 \`UpdateTools\` 成员，导致原有 exhaustive match（如 \`assert\_never\`）代码类型检查失败。同时开始对 \`gemini-2.5-pro\` 与 \`gemini-2.5-flash\` 发出 \`DeprecatedModelWarning\` 弃用警告。

github · dsfaccini · 11月26日 23:49

**「设计要点」** 实时会话工具更新通过模型能力标记 \`supports\_tool\_updates\` 控制推送时机，仅向支持该能力的连接发送 \`UpdateTools\`，避免向旧连接发送不兼容消息。\`FileSystemToolset.read\_file\` 的 \`offset\` 参数从 0-indexed 改为 1-indexed，\`offset=0\` 将直接触发异常。

**「改了什么」** \- 实时会话支持中途动态更新工具，新增 \`UpdateTools\` 消息类型与 \`RealtimeModelProfile.supports\_tool\_updates\` 能力标记
\- \`RealtimeInput\` 联合类型扩展，原有 exhaustive match 需显式处理 \`UpdateTools\` 分支
\- \`gemini-2.5-pro\` 与 \`gemini-2.5-flash\` 触发 \`DeprecatedModelWarning\` 弃用警告
\- \`FileSystemToolset.read\_file\` 的 \`offset\` 改为 1-indexed
\- 新增 \`GoogleInteractionsModel\` 支持无状态 Google Interactions
\- Pax 新增 \`/computer-use\` 桌面沙箱与双击/三击选择交互改进

**标签**: `#tools`, `#runtime`

---

## Agent 工程师日报
{: #sec-agent-engineer .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-agent-engineer" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-agent-engineer-1"></a>
### [OS-Omni v1 跨平台智能体基准上线](https://huggingface.co/papers/2611.34232) ⭐️ 7.0/10

2026 年 11 月 27 日 Hugging Face Daily Papers 发布 OS-Omni v1 跨平台计算机使用智能体基准。该基准为实时可执行评测环境，覆盖 Windows、Ubuntu、macOS、iOS、Android、Web 共 6 个平台，首波发布包含每平台 48 个任务、12 组桌面与安卓手机跨设备长时序工作流，解决现有基准隔离不同环境、无法评估跨平台长时序任务的问题，面向智能体评测与开发工程师。

rss · Hugging Face Daily Papers · 11月27日 00:00

**「为什么重要」** 当前计算机使用智能体基准多隔离 Web、移动端或桌面环境，无法验证单一通用智能体跨多操作系统、跨设备完成长时序任务的能力，OS-Omni v1 提供的可复现版本化任务集填补了该场景的评测工具空白。

**「可关注」** 可关注：OS-Omni 采用版本化任务集发布模式，后续每波 300 个任务的更新可支撑跨平台智能体能力的长期对比评测。

**标签**: `#eval`, `#coding-agent`

---

<a id="item-agent-engineer-2"></a>
### [VBVR-Pro-Bench：编码智能体视觉推理胜出](https://huggingface.co/papers/2611.34813) ⭐️ 7.0/10

2026 年 11 月 27 日，Hugging Face Daily Papers 收录论文《Solve Vision with Code: Coding Agents Are Stronger Visual Reasoners Than Video Models》。该论文提出 VBVR-Pro-Bench 视觉推理基准，在相同输入、输出规范与基于规则的评估器条件下，对比编码智能体与视频生成模型。编码智能体通过编写程序渲染答案视频，而非直接生成像素视频。实验结果显示编码智能体是更强的视觉推理器。目前仅公开摘要片段，未披露完整技术细节、具体性能指标与可复现信息。该结果对构建或评估面向推理任务的编码智能体的工程师有参考价值。

rss · Hugging Face Daily Papers · 11月27日 00:00

**「为什么重要」** 该研究首次在严格控制的相同条件下，将“原生视觉推理”（视频生成）与“符号推理”（编码智能体）进行直接对比，挑战了视频生成模型在视觉推理任务上的固有优势假设。若结论可复现，意味着编码智能体在视觉推理场景中可能具备更可靠的推理路径。

**「可关注」** 可关注：在视觉推理任务中，编码智能体通过代码生成中间表示再渲染视频的路径，可能比端到端视频生成模型更易获得可验证、可调试的推理过程。

**标签**: `#eval`, `#coding-agent`, `#reasoning`

---

<a id="item-agent-engineer-3"></a>
### [DRBench Pro 基准发布](https://huggingface.co/papers/2611.34852) ⭐️ 7.0/10

2026 年 11 月 27 日，Hugging Face Daily Papers 介绍 arXiv 预印本 DRBench Pro。该基准面向深度研究代理，以结构化知识覆盖为首要评估目标。其自动化管道从 Wikipedia 构建本地知识树，通过采样子图生成研究查询及关系绑定的证据评分标准。代理仅接收研究查询，评估系统据此测量研究输出的知识覆盖广度与深度。该工作目前仅为预印本，未公开完整评估 harness，缺乏生产环境验证。

rss · Hugging Face Daily Papers · 11月27日 00:00

**「为什么重要」** 现有深度研究代理基准多关注报告质量多维度，但缺乏对知识覆盖结构的专门度量。DRBench Pro 试图填补这一空白，为构建或评估深度研究代理的工程师提供新的 eval 维度。但需注意，该基准尚未正式发布，其实践价值需等待后续验证。

**「可关注」** 可关注：该基准将知识覆盖结构化为关系绑定的评分标准，但当前仅为预印本，尚无公开的评估 harness 或生产验证数据。

**标签**: `#eval`, `#deep-research-agent`, `#benchmark`

---

<a id="item-agent-engineer-4"></a>
### [HF Daily Paper：AI 代理数据库错误损害研究](https://huggingface.co/papers/2611.30483) ⭐️ 7.0/10

2026 年 11 月 27 日 Hugging Face Daily Papers 发布预印本研究，聚焦 AI 代理执行生产数据库语句出错时的损害严重程度影响因素，覆盖模型类型、数据库防护层、引擎选择、权限设置、恢复机制 5 类变量，关联 AI 代理安全、工具链与评估设计领域。研究采用两层预注册实验设计：Layer A 通过脚本注入 22 个标准化错误，无模型参与，覆盖 4 种关系型引擎、5 种权限配置、2 种恢复配置，共完成 792 个测试单元、874 次恢复演练（含 10 分钟重复测试）；Layer B 使用 6 个 4B 至 12B 参数的开源模型及 1 个 35B 混合专家模型驱动最小工具调用代理测试，但材料中该部分描述截断，完整实验参数未披露。当前提供的材料仅披露研究设计与部分实验参数，完整研究结论未公开。

rss · Hugging Face Daily Papers · 11月27日 00:00

**「为什么重要」** 该研究针对 AI 代理操作生产数据库出错的高优先级安全风险，采用预注册对照实验设计，系统测试模型能力、防护层、引擎、权限、恢复机制等核心变量的影响，为相关领域的可复现评估提供基准框架。

**「可关注」** 可关注：研究将无模型标准化错误注入与多规模模型驱动的代理错误测试分层开展，可对照评估现有数据库防护配置对不同错误来源的拦截效果。

**标签**: `#eval`, `#permissions`, `#coding-agent`, `#harness`

---

## AI 日报
{: #sec-ai-daily .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-daily" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-daily-1"></a>
### [港科大混元 Rosetta 开源 解决基模遗忘](https://mp.weixin.qq.com/s?__biz=MzA3MzI4MjgzMw==&amp;mid=2651076720&amp;idx=2&amp;sn=d375259d0dfaea462ea23093a9ae08bd) ⭐️ 5.5/10

港科大与腾讯混元联合提出的原生多模态预训练方案 Rosetta（组合式原生多模态预训练）已被 NeurIPS 2026 接收，目前已全面开源预训练、推理、评测代码及模型权重，支持单卡至千卡集群部署。该方案针对基模增量学习新能力时的灾难性遗忘痛点，试图解决现有 MoE 路由坍缩、MoT 结构隔离导致原有能力退化的问题——对比实验显示，全量联合预训练加入文生图任务后，MoE 与 MoT 在 MMLU、BBH、MBPP 等语言能力评测上出现断崖式遗忘，后两者得分直接跌至 0 分，且 MoT 总参数膨胀近 20%，而 Rosetta 与标准 MoE 保持完全一致的总参数预算；Rosetta 通过统一注意力层、组合式 FFN 架构配合动量梯度对齐机制，宣称可在扩展新能力时保持原有基模能力不退化。本则为机器之心的二手转述，未获取发布方官方一手公告，具体技术细节需以公开论文及开源仓库为准。

rss · 机器之心 · 11月27日 09:00

**「为什么重要」** 当前基模迭代新能力普遍需从头重训，或联合训练导致原有能力退化，Rosetta 的方案为原生多模态模型的增量能力扩展提供了可参考的工程思路，有望降低多模态基模的迭代成本。

**「可关注」** 可关注：Rosetta 已全面开源预训练、推理、评测代码及模型权重，支持单卡至千卡集群部署，其统一注意力+组合式 FFN 的架构设计可参考用于多模态模型的增量能力扩展场景。

**标签**: `#model`, `#open-source`, `#lab`, `#industry`

---

<a id="item-ai-daily-2"></a>
### [Anthropic 上市造富与小鹏机器人展示](http://www.ruanyifeng.com/blog/2026/11/weekly-issue-421.html) ⭐️ 5.0/10

Anthropic 上周上市，约 5300 名员工可分股票。若市值达 1.4 万亿美元（当前 1.17 万亿），2023 年入职的 290 人获利中位数 1.51 亿美元，2024 年入职的 640 人获利中位数 7900 万美元，2025 年入职的 1360 人获利中位数 2600 万美元，2026 年入职的 3000 人获利中位数 500 万美元。上市一次性造就 600 个亿万富翁。2024 年授予的期权每股 1.30 美元，上市后价格 80 几美元；2026 年 4 月授予的期权每股 25.91 美元。小鹏公司本周展示人形机器人。维基百科 2025 年开始真实人类访问量一路向下，创历史新低。综合 17 个编码基准测试的排名前三为 Fable 5.2、Astra 6.2、Neon 4，国产模型最高为 Qwen 4 Max（第 10 位）。

rss · 阮一峰 · 11月27日 00:10

**「为什么重要」** 这期周刊集中呈现 AI 行业造富规模与速度，同时提示维基百科访问量持续下滑，可作为观察行业周期与流量结构变化的参考切片。

**「可关注」** 可关注：Anthropic 上市后不同入职年份员工的期权获利中位数差异显著，入职时间窗口对财富效应影响直接。

**标签**: `#model`, `#lab`, `#industry`

---

## AI 羊毛
{: #sec-ai-deals .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-deals" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-deals-1"></a>
### [NodeWarden 新增离线与自动备份功能](https://www.appinn.com/nodewarden-update-1/) ⭐️ 8.0/10

你看到的内容可能由第三方 AI 基于小众软件文章提炼总结而成，可能与原文真实意图存在偏差。不代表小众软件观点和立场。请点击链接阅读原文细致比对和校验。NodeWarden 是可直接部署在 Cloudflare Workers 上的开源自托管密码管理器，无需自有服务器，可在 Cloudflare 免费额度内使用，兼容 Bitwarden 全系列客户端。本次更新新增离线使用、自动云备份、多用户管理、密码安全检测等功能，原 Bitwarden 付费的 TOTP 动态验证码生成、Send 分享等功能也可免费使用。

rss · 小众软件 · 11月27日 09:13

**「为什么重要」** 对于想自托管密码库又不想维护服务器的用户，NodeWarden 可直接复用 Cloudflare 免费额度，无需承担服务器成本；新增的离线访问、自动云备份、密码安全检测等功能补齐了此前自建密码管理器的核心短板，且原 Bitwarden 付费的 TOTP 功能也可免费使用。

**「可关注」** 可关注：升级前需保留原有 JWT\_SECRET、数据库及 Durable Objects 绑定，完成完整备份后再操作；今年 2 月部署的老版本需检查 Cloudflare 的 NODE\_VERSION 是否为 Node.js 24.22.1。

**标签**: `#free-tier`, `#self-hosted`, `#password-manager`, `#api`

---