---
layout: default
title: "Horizon Summary: 2026-11-28 (ZH)"
date: 2026-11-28
lang: zh
---

> 从 172 条内容中筛选出 10 条重要资讯。

<nav id="ah-toc" class="ah-toc" aria-label="目录"><span class="ah-toc-title">目录</span><ul><li><a href="#sec-harness-arch"><span class="ah-toc-name">Harness 架构</span><span class="ah-toc-count">2条</span></a></li><li><a href="#sec-agent-engineer"><span class="ah-toc-name">Agent 工程师日报</span><span class="ah-toc-count">5条</span></a></li><li><a href="#sec-ai-daily"><span class="ah-toc-name">AI 日报</span><span class="ah-toc-count">1条</span></a></li><li><a href="#sec-ai-deals"><span class="ah-toc-name">AI 羊毛</span><span class="ah-toc-count">2条</span></a></li></ul></nav>

---

**[Harness 架构](#sec-harness-arch)**
1. [pydantic-ai v2.77.0 发布](#item-harness-arch-1) ⭐️ 7.8/10
2. [MCP servers v2.6.0 发布](#item-harness-arch-2) ⭐️ 6.8/10

**[Agent 工程师日报](#sec-agent-engineer)**
1. [Google DeepCrossAttention 发布 推理快 3x](#item-agent-engineer-1) ⭐️ 7.0/10
2. [OS-Omni 跨平台智能体基准发布](#item-agent-engineer-2) ⭐️ 7.0/10
3. [DRBench Pro 专业深度研究基准发布](#item-agent-engineer-3) ⭐️ 7.0/10
4. [HF 每日论文：AI 代理数据库损害归因](#item-agent-engineer-4) ⭐️ 7.0/10
5. [Coding Agents 视觉推理优于视频模型](#item-agent-engineer-5) ⭐️ 6.0/10

**[AI 日报](#sec-ai-daily)**
1. [港科大混元开源 Rosetta 解决基模学新忘旧](#item-ai-daily-1) ⭐️ 5.0/10

**[AI 羊毛](#sec-ai-deals)**
1. [NodeWarden 更新：Cloudflare 免费自建密码库](#item-ai-deals-1) ⭐️ 7.0/10
2. [Google AI Pro 黑五开放新用户优惠](#item-ai-deals-2) ⭐️ 7.0/10

---

## Harness 架构
{: #sec-harness-arch .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-harness-arch" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-harness-arch-1"></a>
### [pydantic-ai v2.77.0 发布](https://github.com/pydantic/pydantic-ai/releases/tag/v2.77.0) ⭐️ 7.8/10

这是 pydantic-ai v2.77.0 的官方发布。新增 SQLite、Postgres、MongoDB 三后端支持 \`ConversationStore\` 持久化，同时将 Pax session store 重命名为 \`SqliteSessionStore\`（旧名称保留但触发 \`HarnessDeprecationWarning\`）。技能系统默认跳过缺失或不可读路径，新增 \`SkillCatalog.advice\` 和就近搜索 \`pax\` 技能文件夹。新增跨提供商 \`thinking\_summary\`、\`compact\_history\(\)\` 压缩钩子、子代理权限收紧、流式不完整状态标记等运行时行为调整。

github · dsfaccini · 11月27日 23:32

**「设计要点」** 运行时通过 \`AgentStreamEvent\` 扩展压缩事件，并引入 \`CompactionReceiptPart\` 替代 \`UserPromptPart\` 传递回执。权限模型新增 \`&\#x27;operator&\#x27;\` 阈值，磁盘子代理定义文件低于该权限即被跳过，\`working\_directory\` 委托的 workspace 权限降至父代理授予的最低级别。

**「改了什么」** \`ConversationStore\` 新增 SQLite、Postgres、MongoDB 三后端，Pax session store 重命名为 \`SqliteSessionStore\` 并触发 \`HarnessDeprecationWarning\`。技能系统默认跳过缺失/不可读路径，新增 \`SkillCatalog.advice\` 和就近搜索 \`pax\` 技能文件夹。运行时新增 \`thinking\_summary\`、\`compact\_history\(\)\` 压缩钩子、\`CompactionReceiptPart\`，收紧子代理权限至 \`&\#x27;operator&\#x27;\` 阈值，流式响应标记 \`state=&\#x27;incomplete&\#x27;\`，回退子代理请求计入 \`UsageLimits\`，并提前拒绝 GPT-5.4/5.6 工具请求及 OpenAI/Azure 图像输出。

**标签**: `#memory`, `#tools`, `#compatibility`

---

<a id="item-harness-arch-2"></a>
### [MCP servers v2.6.0 发布](https://github.com/modelcontextprotocol/servers/releases/tag/v2.6.0) ⭐️ 6.8/10

modelcontextprotocol/servers v2.6.0 是安全修复版本，修复 git、memory、fetch、filesystem 四个服务器的 8 个漏洞，完成 v2.5.0 遗留的 2 项修复。mcp-server-git 升至 2026.11.27，@modelcontextprotocol/server-memory 升至 2.2.2，mcp-server-fetch 升至 2026.11.27；Windows 平台还需将 @modelcontextprotocol/server-filesystem 升至 2.4.1。修复覆盖 Git LFS filter 程序执行、仓库路径遍历、环境变量泄露、凭据泄露、robots.txt 绕过及 Windows 目录 junction 检测等问题。

github · cliffhall · 11月27日 09:51

**「改了什么」** 修复 git 服务器的 Git LFS 程序执行、仓库路径遍历、环境变量泄露、凭据泄露、alternates 竞争条件及合并覆盖忽略文件等 6 个漏洞；完成 v2.5.0 遗留的仓库边界检查后置修复。修复 memory 服务器临时文件权限泄露、fetch 服务器 robots.txt 绕过，以及 Windows 平台 filesystem 服务器目录 junction 检测不足等问题。

**标签**: `#security`, `#mcp`, `#tools`, `#sandbox`

---

## Agent 工程师日报
{: #sec-agent-engineer .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-agent-engineer" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-agent-engineer-1"></a>
### [Google DeepCrossAttention 发布 推理快 3x](https://research.google/blog/supercharging-transformer-residual-connections/) ⭐️ 7.0/10

2026 年 11 月 27 日，Google Research 发布 DeepCrossAttention 优化方案，针对 transformer 残差连接结构进行调整，官方博客宣称该方案可实现最高 3 倍推理加速，且模型质量无显著损失。该消息由 Hacker News 用户转发官方公告传播，目前无公开的复现数据或详细基准测试细节。若效果属实，该优化将直接利好依赖 LLM 推理的 AI agent harness 开发者，可降低推理延迟与运营成本。

hackernews · ComputedCamp995 · 11月27日 23:06 · [社区讨论](https://news.ycombinator.com/item?id=50672565)

**「为什么重要」** 该优化针对 LLM 推理核心瓶颈，若效果属实可直接降低 agent 系统的推理延迟与成本；目前仅公开博客声明，无独立复现数据，实际收益尚未证实。

**「可关注」** 可关注：社区已开始讨论将 DeepCrossAttention 与 MTP、DFlash 等现有推理优化组合使用的可能性。

**「评论」** 社区讨论中，有用户猜测该优化可能与自己使用的 Gemini Neon 模型性价比提升有关；有用户质疑博客配图用折线图展示不同方法性能不合理，应使用柱状图；还有用户关注该优化与现有推理优化组合后的潜在收益。

**标签**: `#inference-optimization`, `#llm-architecture`, `#harness`

---

<a id="item-agent-engineer-2"></a>
### [OS-Omni 跨平台智能体基准发布](https://huggingface.co/papers/2611.34232) ⭐️ 7.0/10

2026 年 11 月 28 日，Hugging Face Daily Papers 发布首个跨平台长时序通用计算机使用智能体基准 OS-Omni，解决现有智能体基准平台割裂、无法评估跨系统长时序工作流的问题。v1 版本覆盖 Windows、Ubuntu、macOS、iOS、Android、Web 共 6 个平台，每个平台含 48 个任务，同时提供 12 组桌面与安卓配对的跨平台工作流。该基准面向计算机使用智能体评估系统的构建者，提供可复现的初始环境与版本化任务迭代机制。

rss · Hugging Face Daily Papers · 11月28日 04:28

**「为什么重要」** 现有智能体基准多局限于单一平台，无法验证通用智能体的跨系统长时序执行能力，OS-Omni 填补了这一空白，为后续不同智能体的跨平台能力对比提供了标准化依据。

**「可关注」** 可关注：OS-Omni v1 的 6 平台任务集与跨平台工作流规格，可直接用于现有计算机使用智能体的跨平台能力对齐测试。

**标签**: `#eval`, `#coding-agent`

---

<a id="item-agent-engineer-3"></a>
### [DRBench Pro 专业深度研究基准发布](https://huggingface.co/papers/2611.34852) ⭐️ 7.0/10

2026 年 11 月 28 日 Hugging Face Daily Papers 发布论文，提出面向专业深度研究 Agent 的知识中心化评测基准 DRBench Pro，解决现有深度研究 Agent 评测缺少结构化知识覆盖、探索深度评估维度的问题。其自动化评测流水线基于 Wikipedia 构建本地知识树，通过采样子图生成研究查询与证据 grounded 评分 rubric，每个 rubric 对应知识树中的关系，完整保留评估的知识结构，参与评测的 Agent 仅需接收研究查询。该基准目前仅覆盖基于 Wikipedia 的专业深度研究场景，未覆盖通用 Agent 或 coding Agent 的评测需求，主要服务于深度研究 Agent 的研发与评测团队。

rss · Hugging Face Daily Papers · 11月28日 04:28

**「为什么重要」** 它填补了当前深度研究 Agent 评测在结构化知识覆盖、探索深度维度的空白，提供的基于 Wikipedia 知识树的自动化评测流水线可直接用于相关 Agent 的能力校验与工具链优化，但适用场景相对垂直，暂不适用于通用 Agent 或 coding Agent 的通用评测需求。

**「可关注」** 可关注：其基于知识树关系生成证据 grounded 评分 rubric 的设计，可参考用于垂直领域 Agent 的结构化能力评测流水线搭建。

**标签**: `#eval`, `#deep-research-agent`

---

<a id="item-agent-engineer-4"></a>
### [HF 每日论文：AI 代理数据库损害归因](https://huggingface.co/papers/2611.30483) ⭐️ 7.0/10

2026 年 11 月 28 日 Hugging Face 每日论文收录一篇预注册实证研究，量化模型选择、数据库前置防护层、数据库引擎属性三类因素对 AI 代理错误数据库操作损害严重度的影响，该论文当前获 4 次 Hugging Face 每日论文点赞。实验分两层：Layer A 用 22 个标准化错误脚本（无模型参与）在 4 种关系型引擎、5 种权限方案、2 种恢复方案下测试，共 792 个测试单元、874 次恢复演练（含 10 分钟重复测试）；Layer B 用 6 个 4B 至 12B 参数开源小模型及 1 个 35B 参数 MoE 模型驱动极简工具调用代理执行同类测试（原文 Layer B 实验细节未完整提供）。研究覆盖权限配置、代理评测等 coding agent 与 harness 相关场景，结果面向数据库访问类 AI 代理的研发、安全与运维团队。

rss · Hugging Face Daily Papers · 11月28日 04:28

**「为什么重要」** 该研究针对 AI 代理误操作生产数据库的高影响运营风险，采用预注册、可复现的结构化实验设计，量化三类核心因素的影响，为数据库访问类代理的防护层设计、权限配置、评测集搭建提供可参考的量化依据。

**「可关注」** 可关注：研究公开的 22 个标准化数据库错误用例、多引擎多权限的实验框架，可直接复现用于数据库访问类代理的防护效果评测。

**标签**: `#permissions`, `#eval`, `#coding-agent`, `#harness`

---

<a id="item-agent-engineer-5"></a>
### [Coding Agents 视觉推理优于视频模型](https://huggingface.co/papers/2611.34813) ⭐️ 6.0/10

2026 年 11 月 28 日，Hugging Face Daily Papers 收录论文《Solve Vision with Code》，提出视觉推理基准 VBVR-Pro-Bench。研究在相同任务输入、输出规格与评估条件下，对比 coding agents 与视频生成模型的表现：前者通过代码渲染答案视频，后者直接生成视频，由同一规则评估器评分。结果显示 coding agents 是更可靠的视觉推理器，但现有材料仅含摘要片段，未披露具体性能指标、数据集规模或实现细节。该结果对 agent 评估与视觉推理 agent 开发有参考价值。

rss · Hugging Face Daily Papers · 11月28日 04:28

**「为什么重要」** 论文首次在控制条件下验证了代码生成视频相对于像素生成视频在视觉推理任务中的可靠性优势，直接挑战了“原生视觉推理更优”的假设。这为视觉推理 agent 的评估范式选择提供了实证依据。

**「可关注」** 可关注：VBVR-Pro-Bench 采用统一规则评估器对代码生成视频与视频生成模型输出进行评分，这种评估范式可提升结果可复现性。

**标签**: `#eval`, `#coding-agent`

---

## AI 日报
{: #sec-ai-daily .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-daily" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-daily-1"></a>
### [港科大混元开源 Rosetta 解决基模学新忘旧](https://mp.weixin.qq.com/s?__biz=MzA3MzI4MjgzMw==&amp;mid=2651076720&amp;idx=2&amp;sn=d375259d0dfaea462ea23093a9ae08bd) ⭐️ 5.0/10

港科大与腾讯混元联合提出的组合式原生多模态预训练方案 Rosetta 已被 NeurIPS 2026 接收，全套预训练、推理、评测代码及模型权重已全面开源，支持单卡至千卡集群部署。该方案针对基模增量学习新能力时的灾难性遗忘问题，无需从头重训基模即可实现能力扩展。对比现有主流方案，联合训练加入生图任务后，标准 MoE 出现路由坍缩，结构隔离的 MoT 方案的语言与代码能力（BBH、MBPP）直接跌至 0 分，而 Rosetta 在保持与标准 MoE 一致总参数预算的前提下，既保留原有基模能力，又实现跨模态协同。

rss · 机器之心 · 11月27日 09:00

**「为什么重要」** 当前原生多模态预训练长期存在「遗忘-协同」两难：现有方案要么在联合训练中丢失原有基模能力，要么通过结构隔离阻断跨模态协同，Rosetta 提供了可复用的通解，全栈开源也降低了开发者扩展基模能力的门槛。

**「可关注」** 可关注 Rosetta 统一注意力层、组合式 FFN 的架构设计，通过动量对齐梯度解决模态间冲突，在总参数预算与标准 MoE 一致的前提下实现能力扩展与跨模态协同，全栈开源资源已可获取。

**标签**: `#model`, `#open-source`, `#lab`, `#industry`

---

## AI 羊毛
{: #sec-ai-deals .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-deals" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-deals-1"></a>
### [NodeWarden 更新：Cloudflare 免费自建密码库](https://www.appinn.com/nodewarden-update-1/) ⭐️ 7.0/10

你看到的内容可能由第三方 AI 基于小众软件文章提炼总结而成，可能与原文真实意图存在偏差。不代表小众软件观点和立场。请&lt;a href=&quot;https://www.appinn.com/nodewarden-update-1/&quot; target=&quot;\_blank&quot;&gt;点击链接阅读原文&lt;/a&gt;细致比对和校验。&lt;br /&gt;&lt;br /&gt;开源密码管理器 NodeWarden 支持部署在 Cloudflare Workers 上，利用平台免费额度即可零成本自建兼容 Bitwarden 的私人密码库，无需自备服务器，支持 Bitwarden 官方客户端及自带网页密码库。本次更新新增离线使用、自动云备份、多用户管理、密码安全检测等功能，原 Bitwarden 付费的 TOTP 动态验证码生成功能也可免费使用，目前多用户支持暂不提供 Bitwarden 组织、共享集合功能。提供在线 DEMO 可无需部署体验，部署和升级方式无核心变化，老版本升级需注意保留原有 JWT\_SECRET、数据库及存储绑定，升级前需完整备份。NodeWarden 为独立第三方开源项目，与 Bitwarden 官方无关。

rss · 小众软件 · 11月27日 09:13

**「为什么重要」** 对于想零成本自建兼容 Bitwarden 私人密码库的用户，本次更新补齐了离线使用、自动云备份等核心功能短板，无需维护服务器即可获得原 Bitwarden 付费版才有的 TOTP 等能力，大幅降低自建门槛。

**「可关注」** 可关注：NodeWarden 部署于 Cloudflare Workers，升级老版本时需保留原有 JWT\_SECRET、数据库及 Durable Objects 绑定，避免数据丢失或服务异常。

**标签**: `#free-tier`, `#promo`, `#open-source`, `#self-hosted`

---

<a id="item-ai-deals-2"></a>
### [Google AI Pro 黑五开放新用户优惠](https://www.v2ex.com/t/1260358#reply54) ⭐️ 7.0/10

V2EX 用户 vlink 分享 Google AI Pro 黑五新用户优惠信息，新用户订阅价格为 120 美元，较同期老用户优惠高 20 美元；材料未提及该优惠的适用地区、有效期、领取限制等具体规则。

rss · V2EX Hot · 11月27日 08:13

**「可关注」** 可关注：新用户订阅 Google AI Pro 的黑五优惠价格为 120 美元，较同期老用户优惠高 20 美元。

**标签**: `#promo`, `#api`, `#limited-offer`

---