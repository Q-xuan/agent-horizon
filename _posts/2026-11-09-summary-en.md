---
layout: default
title: "Horizon Summary: 2026-11-09 (EN)"
date: 2026-11-09
lang: en
---

> From 148 items, 7 important content pieces were selected

---

**Agent Harness Architecture**
1. [openai-agents-js v0.22.0-alpha.2 发布](#item-harness-arch-1) ⭐️ 8.3/10
2. [openai-agents-python v0.24.0-alpha.7 发布](#item-harness-arch-2) ⭐️ 7.8/10
3. [anthropics/skills 仓库 trending](#item-harness-arch-3) ⭐️ 5.0/10
4. [Cloudflare 开源 security-audit-skill 技能](#item-harness-arch-4) ⭐️ 5.0/10

**AI Agent Engineer**
1. [SQLite parse\_number\(\) C 与 Rust 对比](#item-agent-engineer-1) ⭐️ 7.0/10
2. [Stanford CS146S 调整作业应对编码代理](#item-agent-engineer-2) ⭐️ 7.0/10

**AI Daily**
1. [芝大教授用Claude改页码丢讲义](#item-ai-daily-1) ⭐️ 5.0/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [openai-agents-js v0.22.0-alpha.2 发布](https://github.com/openai/openai-agents-js/releases/tag/v0.22.0-alpha.2) ⭐️ 8.3/10

openai-agents-js v0.22.0-alpha.2 是预览版发布，引入原生工具链（fileSearch、codeInterpreter、imageGeneration）、A2A 1.0 协议连接、应用管理的 SessionStore 持久化以及 RunBudget 运行预算控制。该版本将原生运行时移至 @openai/agents-codex 包，同时移除实验性 SDKRunner 桥接，原生与经典工作流正式分离。当前预览版暂不支持 MCP、手动工具、环境、原生子代理、目标及可移植检查点。

github · markstuart-oai · Nov 8, 08:27

**「设计要点」** 原生运行时独立为 @openai/agents-codex 包，应用层仍通过 @openai/agents 统一导入。A2A 适配器采用 JSON-RPC 轮询，授权、持久化、执行及不确定变更协调均由应用侧负责。执行器写入策略默认升级为 strict，仅允许工作区写入和显式声明的 writableRoots。

**「改了什么」** 新增 fileSearch\(\)、codeInterpreter\(\)、imageGeneration\(\) 原生工具及增强版 webSearch\(\)。新增 turn.steerExact\(\)、maxModelSteps 和 RunBudget 运行控制。新增应用管理的 SessionStore 与 fileSessionStore\(\) 本地适配器，支持对话恢复与工具调用记录持久化。新增 @openai/agents/a2a 模块实现 A2A 1.0 远程代理调用。移除 SDKRunner 桥接与 @openai/agents/migration 导入，执行器写入策略默认改为 strict。

**「评论」** 无社区评论。

**Tags**: `#runtime`, `#tools`, `#a2a`, `#memory`, `#sandbox`

---

<a id="item-harness-arch-2"></a>
### [openai-agents-python v0.24.0-alpha.7 发布](https://github.com/openai/openai-agents-python/releases/tag/v0.24.0-alpha.7) ⭐️ 7.8/10

openai-agents-python v0.24.0-alpha.7 released. This alpha adds dual Classic/native runtime support via agents.classic, durable root Sessions with CustomStorage/SQLiteSessionStore, hosted tools \(FileSearch, CodeInterpreter, ImageGeneration\), context control hooks \(transform\_context, before\_compact, before\_complete\), and RunBudget for usage limits. Breaking changes include default environment write\_policy=&quot;strict&quot;, renamed MCP approval modes, changed NativeAgents.before\_step signature, and split ElicitationRequest types.

github · markstuart-oai · Nov 8, 07:05

**「设计要点」** Runtime splits into Classic and native tracks with separate objects and checkpoints. Environment write policy defaults to strict for local execution, while writable\_roots extends remote writable directories. Session storage supports application-owned CustomStorage, initially excluding native tools, Environments, children, and portable checkpoints.

**「改了什么」** This release adds agents.classic import for parallel Classic/native execution, CustomStorage/SQLiteSessionStore for durable session persistence with uncertain tool reconciliation, hosted tools \(FileSearch, CodeInterpreter, ImageGeneration\) via compatible Responses providers, context hooks \(transform\_context, before\_compact, before\_complete\), and RunBudget for usage limits. It changes default environment write\_policy to strict \(requiring Linux/macOS executor, with writable\_roots for extra directories\), renames MCP approval modes \(&quot;auto&quot;→&quot;native&quot;, &quot;approve&quot;→&quot;preapproved&quot;\), changes NativeAgents.before\_step to accept ChildStepContext, splits ElicitationRequest into FormRequest\|UrlRequest, adds timeout\_behavior=&quot;error\_as\_result&quot;, and introduces buffered NativeProvider response mode with experimental CodexLogin reuse.

**Tags**: `#runtime`, `#tools`, `#storage`, `#sandbox`

---

<a id="item-harness-arch-3"></a>
### [anthropics/skills 仓库 trending](https://github.com/anthropics/skills) ⭐️ 5.0/10

Anthropic 官方仓库 anthropics/skills 登上 GitHub trending。该仓库实现 Agent Skills 机制，允许 Claude 动态加载包含指令、脚本和资源的文件夹，以可重复方式完成专门任务。公开内容仅提供高层概述，未披露具体接口规范、版本号或集成细节，不足以支撑 agent harness 架构评估。

rss · GitHub Trending Daily · Nov 9, 02:18

**Tags**: `#tools`, `#runtime`

---

<a id="item-harness-arch-4"></a>
### [Cloudflare 开源 security-audit-skill 技能](https://github.com/cloudflare/security-audit-skill) ⭐️ 5.0/10

这是Cloudflare面向coding-agent开源的安全审计技能，可将普通agent转化为安全审计器。它通过编排隔离子代理完成侦察、覆盖引导狩猎、候选验证、结构化输出、独立记录校验与目标中立报告等多阶段审计流程，输出机器可读的审计结果，也是Cloudflare漏洞发现harness的初始基础。

rss · GitHub Trending Daily · Nov 9, 02:18

**Tags**: `#tools`, `#subagents`, `#sandbox`, `#planning`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [SQLite parse\_number\(\) C 与 Rust 对比](https://simonwillison.net/2026/Nov/8/sqlite-parse-number-c-vs-rust/) ⭐️ 7.0/10

Simon Willison 2026-11-08 发布 SQLite parse\_number\(\) 扩展的 C 与 Rust 对比研究。他使用 Claude Opus 5.5 辅助开发，对比性能、代码复杂度与二进制大小。初始 Rust 版本（rusqlite 321 KB，sqlite-loadable-rs 298 KB）大于 C 版本（14 KB），但 Rust 解析更快。优化 C 实现后，在 200 万行数据集上，混合数据场景 C 达 19 ns/行，优于 rusqlite 的 46 ns 和 sqlite-loadable 的 41 ns；整数场景 C 为 16 ns；纯小数场景 C 为 18 ns。研究代码已公开。

rss · Simon Willison · Nov 8, 22:26

**「为什么重要」** 这为工程师构建 SQLite 扩展时提供了 C 与 Rust 的可比数据。性能差距并非单向：手写优化 C 可击败 Rust 标准解析例程，尽管 Rust 在二进制体积与安全性上占优。

**「可关注」** SQLite 扩展的数值解析热点路径上，手写 C 仍可压过 Rust 标准库实现；AI 能快速产出可运行原型，但极致性能仍需人工调优。

**Tags**: `#toolchain`, `#coding-agent`, `#performance`

---

<a id="item-agent-engineer-2"></a>
### [Stanford CS146S 调整作业应对编码代理](https://latent.space/p/one_million_ai_engineer_special_how_stanford_teaches_ai-native_engineering_mihail_eric_monaco/) ⭐️ 7.0/10

2026-11-08，Latent.Space 发布 Stanford CS146S 讲师 Mihail Eric 访谈。Stanford 第二次开设《The Modern Software Developer》课程时，因编码代理可一键完成去年作业，将部分作业改为向开源仓库提交补丁并由维护者评审。Monaco 自建 agent workspace，采购代码评审工具，给 on-call agent 开放 Datadog 与 GitHub 访问权限，采用「buy to learn, build to keep」的工具决策框架。课程还覆盖大代码库上下文工程、diff 理解、MCP portals 等主题。

rss · Latent Space · Nov 8, 21:23

**「为什么重要」** 这期访谈提供 Stanford 应对编码代理冲击的课程改课决策，以及 Monaco 生产 agent 工具链的选型逻辑，对设计 coding agent harness、eval 或工作流的工程师有直接参考价值。材料未附性能基准或官方发布文档，实际效果需自行验证。

**「可关注」** Stanford 将作业从「实现功能」改为「提交补丁并由维护者评审」，要求学员理解仓库上下文、解释 patch 意图并预测影响，这提示 coding agent 的 eval 设计可参考该维度补充评估指标。

**Tags**: `#coding-agent`, `#harness`, `#orchestration`, `#eval`

---

## AI Daily

<a id="item-ai-daily-1"></a>
### [芝大教授用Claude改页码丢讲义](https://mp.weixin.qq.com/s?__biz=MzI3MTA0MTk1MA==&amp;mid=2652741306&amp;idx=2&amp;sn=ca3a968dc876193340e7e0975c1248e5) ⭐️ 5.0/10

芝加哥大学法学院教授William Baude委托Claude更新旧讲义页码，Claude在核查页码时误删其2023年宪法课全年讲义，以及本学期Fall 2026教学大纲；后续通过Dropbox恢复了被删文件，Baude发帖旨在提醒用户注意AI文件操作的风险。

rss · 新智元 · Nov 8, 09:47

**「为什么重要」** 该事件是AI代理无确认执行删除操作的典型 mishap，反映出当前AI工具操作本地/云端文件时缺乏必要风控环节的问题，Baude公开事件意在提醒用户对AI的文件操作保持备份意识，降低数据损失风险。

**「可关注」** 可关注：AI代理执行文件删除、修改类操作时需增加用户确认环节，避免无监督操作造成数据损失。

**「评论」** 网友调侃AI删除文件已成为“作业丢失”的新借口；有网友吐槽Claude回应“你生气有道理”仿佛需要模型批准用户情绪；还有网友建议将Dropbox接入AI方案以统一管理文件操作。

**Tags**: `#model`, `#industry`, `#product`

---