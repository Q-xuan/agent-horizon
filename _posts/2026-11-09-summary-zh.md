---
layout: default
title: "Horizon Summary: 2026-11-09 (ZH)"
date: 2026-11-09
lang: zh
---

> 从 148 条内容中筛选出 7 条重要资讯。

<nav id="ah-toc" class="ah-toc" aria-label="目录"><span class="ah-toc-title">目录</span><ul><li><a href="#sec-harness-arch"><span class="ah-toc-name">Harness 架构</span><span class="ah-toc-count">4条</span></a></li><li><a href="#sec-agent-engineer"><span class="ah-toc-name">Agent 工程师日报</span><span class="ah-toc-count">2条</span></a></li><li><a href="#sec-ai-daily"><span class="ah-toc-name">AI 日报</span><span class="ah-toc-count">1条</span></a></li></ul></nav>

---

**[Harness 架构](#sec-harness-arch)**
1. [openai-agents-js v0.22.0-alpha.2 发布](#item-harness-arch-1) ⭐️ 8.3/10
2. [Agents SDK alpha.7 发布](#item-harness-arch-2) ⭐️ 7.8/10
3. [Anthropic Agent Skills 仓库 trending](#item-harness-arch-3) ⭐️ 5.0/10
4. [Cloudflare security-audit-skill 开源](#item-harness-arch-4) ⭐️ 5.0/10

**[Agent 工程师日报](#sec-agent-engineer)**
1. [SQLite parse\_number 扩展 C/Rust 性能对比](#item-agent-engineer-1) ⭐️ 7.0/10
2. [Mihail Eric 谈 Stanford CS146S 与 Monaco AI](#item-agent-engineer-2) ⭐️ 7.0/10

**[AI 日报](#sec-ai-daily)**
1. [Claude 误删芝大教授全年讲义](#item-ai-daily-1) ⭐️ 5.0/10

---

## Harness 架构
{: #sec-harness-arch .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-harness-arch" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-harness-arch-1"></a>
### [openai-agents-js v0.22.0-alpha.2 发布](https://github.com/openai/openai-agents-js/releases/tag/v0.22.0-alpha.2) ⭐️ 8.3/10

这是 OpenAI JS agents SDK 的 v0.22.0-alpha.2 预览版本，新增原生 fileSearch、codeInterpreter、imageGeneration 工具、A2A 1.0 协议连接、应用托管 SessionStore 会话持久化、RunBudget 运行预算控制等核心能力。该预览版本暂不支持 MCP、手动工具、环境、原生子代理、目标、可移植检查点等特性，升级时需保持 5 个 bundled SDK 包版本一致，替换已移除的 SDKRunner 桥接与迁移导入。

github · markstuart-oai · 11月8日 08:27

**「设计要点」** 原生运行时拆分至独立@openai/agents-codex 包，原生与经典代理、状态完全隔离；A2A 1.0 适配器的授权、持久化、执行与不确定变更调和由应用自行负责；新环境默认开启 strict 写入策略，仅允许工作区写入与显式授予的 writableRoots。

**「改了什么」** 新增原生 fileSearch\(\)、codeInterpreter\(\)、imageGeneration\(\)工具，webSearch\(\)补充过滤、位置、工具选择与引用详情能力；新增 A2A 1.0 连接、应用托管 SessionStore（含 fileSessionStore 本地适配器）、RunBudget、turn 精确控制等原生运行时能力；移除实验性 SDKRunner 桥接与@openai/agents/migration 导入，原生与经典工作流正式分离。

**「评论」** 暂无社区评论内容。

**标签**: `#runtime`, `#tools`, `#a2a`, `#memory`, `#sandbox`

---

<a id="item-harness-arch-2"></a>
### [Agents SDK alpha.7 发布](https://github.com/openai/openai-agents-python/releases/tag/v0.24.0-alpha.7) ⭐️ 7.8/10

OpenAI 官方发布 Python Agents SDK v0.24.0-alpha.7，首次同时支持 Classic 与 native 双运行时。新增自定义持久化会话存储、托管工具（FileSearch、CodeInterpreter、ImageGeneration）、上下文与完成钩子、使用预算（RunBudget）以及本地执行能力。环境写入策略默认改为 strict，影响跨平台兼容性与沙箱隔离。

github · markstuart-oai · 11月8日 07:05

**「设计要点」** 运行时采用 Classic 与 native 双轨架构，通过 \`agents.classic\` 保留 v0 工作流；存储层支持 \`CustomStorage\` 但初始排除原生工具、 Environments 与子代理的自动持久化；执行环境默认 strict 写入策略仅开放工作目录，托管工具依赖标准 Responses 提供商与 API-key 认证。

**「改了什么」** 环境写入策略默认从 legacy 改为 strict，模型目录中 gpt-6-astra、gpt-6.1-sol、gpt-5.6-sol 默认推理努力从 low 升至 medium；MCP 批准模式重命名（auto→native，approve→preapproved），\`NativeAgents.before\_step\` 回调签名变更，\`ElicitationRequest\` 拆分为 \`FormRequest\` 与 \`UrlRequest\`，同时新增 \`SessionStore\`、\`SQLiteSessionStore\`、\`RunBudget\`、\`project\_glob\`/\`project\_grep\` 及 \`NativeSessionVoiceWorkflow\`。

**标签**: `#runtime`, `#tools`, `#storage`, `#sandbox`

---

<a id="item-harness-arch-3"></a>
### [Anthropic Agent Skills 仓库 trending](https://github.com/anthropics/skills) ⭐️ 5.0/10

这是 Anthropic 官方为 Claude 实现的 Agent Skills 系统，以 \`anthropics/skills\` 公共仓库形式出现在 GitHub trending。Skills 是 Claude 动态加载的指令、脚本和资源文件夹，用于提升专门任务的性能，并以可重复方式完成特定任务。当前公开内容仅提供高层概述，缺乏技术实现细节、接口规范或版本信息，无法用于 agent harness 架构评估。

rss · GitHub Trending Daily · 11月9日 02:18

**标签**: `#tools`, `#runtime`

---

<a id="item-harness-arch-4"></a>
### [Cloudflare security-audit-skill 开源](https://github.com/cloudflare/security-audit-skill) ⭐️ 5.0/10

Cloudflare 开源了面向 coding-agent 的安全审计 skill，可将普通 agent 转化为安全审计员。该 skill 通过编排隔离子 agent 完成多阶段安全审计流程，是 Cloudflare 漏洞发现 harness 的基础组件，当前公开内容仅包含高层能力描述，未披露技术实现细节、接口与版本信息。

rss · GitHub Trending Daily · 11月9日 02:18

**「设计要点」** 运行时通过编排独立隔离的子 agent 执行多阶段审计流程，阶段覆盖侦察、覆盖引导狩猎、候选验证、结构化输出、独立记录验证与目标中性报告，作为 Cloudflare 漏洞发现 harness 的底层能力基础。

**「改了什么」** 该 skill 此前为 Cloudflare 内部漏洞发现 harness 的专属组件，本次为首次公开开源，当前仅披露高层能力边界，未开放技术实现细节与使用接口。

**标签**: `#tools`, `#subagents`, `#sandbox`, `#planning`

---

## Agent 工程师日报
{: #sec-agent-engineer .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-agent-engineer" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-agent-engineer-1"></a>
### [SQLite parse\_number 扩展 C/Rust 性能对比](https://simonwillison.net/2026/Nov/8/sqlite-parse-number-c-vs-rust/) ⭐️ 7.0/10

2026 年 11 月 8 日，Simon Willison 发布 SQLite parse\_number\(\)扩展的 C 与 Rust 实现对比研究，使用 Claude Opus 5.5 辅助完成开发与迭代。研究对比两类实现的性能、代码复杂度与二进制体积：初始 C 实现仅 14KB，Rust 实现（rusqlite 321KB、sqlite-loadable-rs 298KB）体积远大于 C，但性能更高，原因是 Rust 的 strtod 等价实现速度是 C 标准库的两倍；后续优化 C 实现后，混合数据、整数、小数场景的每行处理耗时分别为 19ns、16ns、18ns，均优于 Rust 实现的 41-55ns、32-36ns、47-55ns。该研究面向构建 SQLite 扩展与使用 AI 辅助底层工具开发的工程师提供可参考基准。

rss · Simon Willison · 11月8日 22:26

**「为什么重要」** 该研究首次提供 SQLite 自定义函数 C/Rust 实现的量化性能与体积对比基准，同时展示 AI 辅助完成底层 C/Rust 工具开发与迭代的可行工作流；目前对比结论仅针对 parse\_number\(\)扩展，其他类型扩展的适用性尚未验证。

**「可关注」** 可关注：SQLite 扩展开发中，Rust 实现初始性能占优但二进制体积远大于 C，经优化后的 C 实现可在性能与体积维度同时胜出，AI 辅助可大幅降低两类实现的对比与迭代成本。

**标签**: `#toolchain`, `#coding-agent`, `#performance`

---

<a id="item-agent-engineer-2"></a>
### [Mihail Eric 谈 Stanford CS146S 与 Monaco AI](https://latent.space/p/one_million_ai_engineer_special_how_stanford_teaches_ai-native_engineering_mihail_eric_monaco/) ⭐️ 7.0/10

2026 年 11 月 8 日，Latent.Space 发布对 Mihail Eric 的访谈，后者是 Stanford CS146S《The Modern Software Developer》课程讲师、Monaco AI 负责人。访谈披露 Stanford CS146S 第二期因 coding agent 可一键完成往年作业，调整课程设计，将开源项目真实贡献纳入作业，由对应开源维护者评审学生补丁；同时披露 Monaco 工程团队的 agent 落地实践，包括为每个 agent 建独立工作区、采购代码审查工具、给 on-call agent 开放 Datadog 与 GitHub 权限，以及「采购用于学习、自研用于留存」的工具决策框架。本次内容为 AI agent 工程师、coding harness 构建者、高校计算机教育从业者提供了一手参考，但材料仅为访谈内容，无官方发布文档或深度性能基准数据，相关细节以访谈披露内容为准。

rss · Latent Space · 11月8日 21:23

**「为什么重要」** 本次访谈是少有的同时覆盖高校 AI 原生工程课程设计、企业级 coding agent 工具链落地实践的亲历者分享，为构建 coding agent harness、编排工具链、设计 eval 的工程师提供了可参考的决策逻辑；目前无公开性能基准数据验证相关课程效果与 Monaco 工具链的实际效率提升。

**「可关注」** 可关注：Mihail Eric 提出的「采购用于学习、自研用于留存」的工具决策框架，Monaco 为 on-call agent 开放 Datadog、GitHub 权限的落地实践，以及 Stanford CS146S 将开源项目真实贡献纳入作业的课程设计思路。

**标签**: `#coding-agent`, `#harness`, `#orchestration`, `#eval`

---

## AI 日报
{: #sec-ai-daily .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-daily" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-daily-1"></a>
### [Claude 误删芝大教授全年讲义](https://mp.weixin.qq.com/s?__biz=MzI3MTA0MTk1MA==&amp;mid=2652741306&amp;idx=2&amp;sn=ca3a968dc876193340e7e0975c1248e5) ⭐️ 5.0/10

芝加哥大学法学院教授 William Baude 委托 Claude 更新旧讲义页码，仅吃午饭的间隙，Claude 误删了他一年的宪法课讲义及本学期教学大纲。Claude 自查发现引用页码存在 485 页与 484 页的偏差，承认误删是自身粗心导致。最终被删文件通过 Dropbox 恢复功能找回。该事件来自新智元转载报道，无官方一手来源可核对。

rss · 新智元 · 11月8日 09:47

**「为什么重要」** 该事件暴露了 AI 代理执行文件操作时的容错缺陷，对日常使用 AI 处理文档的用户、开发 coding agent 的团队均有警示意义。

**「可关注」** 可关注：AI 代理执行文件修改类任务时，需配套操作确认与备份机制，降低误删核心文件的风险。

**「评论」** 网友调侃 AI 成为新版「作业被狗吃了」的借口，也有声音吐槽 Claude 回应「你生气有道理」像是在批准用户情绪，还有用户建议将 Dropbox 接入 AI 代理以实现全文件操作。

**标签**: `#model`, `#industry`, `#product`

---