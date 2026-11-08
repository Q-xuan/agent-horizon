---
layout: default
title: "Horizon Summary: 2026-11-09 (ZH)"
date: 2026-11-09
lang: zh
---

> 从 133 条内容中筛选出 7 条重要资讯。

<nav id="ah-toc" class="ah-toc" aria-label="目录"><span class="ah-toc-title">目录</span><ul><li><a href="#sec-harness-arch"><span class="ah-toc-name">Harness 架构</span><span class="ah-toc-count">4条</span></a></li><li><a href="#sec-agent-engineer"><span class="ah-toc-name">Agent 工程师日报</span><span class="ah-toc-count">3条</span></a></li></ul></nav>

---

**[Harness 架构](#sec-harness-arch)**
1. [agents-js v0.22.0 发布](#item-harness-arch-1) ⭐️ 8.8/10
2. [Agents SDK v0.24.0 发布](#item-harness-arch-2) ⭐️ 7.8/10
3. [Google 官方 agent skills 仓库 google/skills 上线](#item-harness-arch-3) ⭐️ 5.0/10
4. [Cloudflare security-audit-skill 上 GitHub Trending](#item-harness-arch-4) ⭐️ 5.0/10

**[Agent 工程师日报](#sec-agent-engineer)**
1. [斯坦福 CS146S 课程 Monaco 实践](#item-agent-engineer-1) ⭐️ 7.0/10
2. [SQLite parse\_number\(\) C vs Rust 对比](#item-agent-engineer-2) ⭐️ 6.0/10
3. [Kimi-K3.1-Pro-Coder 2.8T 社区 56% 量化实验](#item-agent-engineer-3) ⭐️ 5.5/10

---

## Harness 架构
{: #sec-harness-arch .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-harness-arch" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-harness-arch-1"></a>
### [agents-js v0.22.0 发布](https://github.com/openai/openai-agents-js/releases/tag/v0.22.0-alpha.2) ⭐️ 8.8/10

openai/openai-agents-js 发布 v0.22.0-alpha.2，引入原生运行时架构。新增 fileSearch\(\)、codeInterpreter\(\)、imageGeneration\(\) 原生工具及 webSearch\(\) 过滤能力；支持 RunBudget、maxModelSteps 和 turn.steerExact\(\) 运行控制；提供应用拥有的 SessionStore 与会话恢复；新增 A2A 1.0 协议适配器与语音工作流。当前预览不支持 MCP、手动工具、环境、原生子代理、目标或便携检查点。

github · markstuart-oai · 11月8日 08:27

**「设计要点」** 原生运行时由 @openai/agents-codex 包承载，与经典代理状态分离。应用层拥有授权、持久存储、执行及不确定突变的协调权。执行器写入策略默认 strict，仅允许工作区写入和显式声明的 writableRoots。

**「改了什么」** 相对上一版，新增原生工具执行链、基于步数和预算的运行门控、应用托管会话持久化、A2A 1.0 远程代理连接，以及沙箱环境与项目搜索集成。移除实验性 SDKRunner 桥接，强制迁移至原生或 classic API。

**标签**: `#runtime`, `#tools`, `#a2a`, `#memory`, `#sandbox`

---

<a id="item-harness-arch-2"></a>
### [Agents SDK v0.24.0 发布](https://github.com/openai/openai-agents-python/releases/tag/v0.24.0-alpha.7) ⭐️ 7.8/10

OpenAI Agents Python SDK v0.24.0-alpha.7 发布。该版本支持 Classic 工作流与原生执行并行，新增 \`CustomStorage\` 应用自持会话存储、\`FileSearch\`/\`CodeInterpreter\`/\`ImageGeneration\` 托管工具，以及默认 \`write\_policy=&quot;strict&quot;\` 环境写入策略。技术上引入上下文转换钩子、完成前审查钩子、\`RunBudget\` 使用预算、MCP 资源访问和本地执行能力。

github · markstuart-oai · 11月8日 07:05

**「设计要点」** 运行时支持 Classic 与 Native 双路径，通过 \`agents.classic\` 保留 v0 运行时；存储层新增 \`CustomStorage\` 接口并默认启用严格沙箱写入策略；工具层集成需 API-key 认证的 provider-hosted 工具。

**「改了什么」** 相对 v0.24.0-alpha.6，新增 Classic 并行执行、\`CustomStorage\`/\`SQLiteSessionStore\` 会话持久化、\`FileSearch\`/\`CodeInterpreter\`/\`ImageGeneration\` 托管工具、\`RunBudget\` 预算控制、\`before\_compact\`/\`before\_complete\` 钩子、\`Environment.local\(\)\` 本地执行及语音工作流。MCP 审批模式重命名，\`NativeAgents.before\_step\` 回调签名变更，部分模型默认 reasoning effort 从 \`low\` 提升至 \`medium\`。

**标签**: `#runtime`, `#tools`, `#sandbox`, `#memory`

---

<a id="item-harness-arch-3"></a>
### [Google 官方 agent skills 仓库 google/skills 上线](https://github.com/google/skills) ⭐️ 5.0/10

这是 Google 官方发布的预置 agent skills 仓库，覆盖 Google 产品及技术（含 Google Cloud）。用户可通过\`npx skills add google/skills\`完成安装，支持选择单技能或全量、指定目标 agent、设置项目级或全局安装范围，也支持通过 npx 更新已安装技能；若环境无 npx，需先安装包含 npm 与 npx 的 Node.js。目前公开内容未披露技能架构、harness 集成方式、实现细节及权限模型等技术信息。

rss · GitHub Trending Daily · 11月8日 23:00

**「改了什么」** 新增 Google 官方预置 agent skills 仓库，提供面向 Google 产品的预置技能包，支持通过 npx 完成安装、更新与安装范围配置。

**标签**: `#tools`, `#skills`

---

<a id="item-harness-arch-4"></a>
### [Cloudflare security-audit-skill 上 GitHub Trending](https://github.com/cloudflare/security-audit-skill) ⭐️ 5.0/10

这是 Cloudflare 开源的 coding agent 安全审计 skill，于 2026 年 11 月 8 日登上 GitHub Trending。它通过多阶段编排隔离子代理完成漏洞发现，输出可机器读取、经独立验证的安全发现结果，是 Cloudflare 生产级漏洞发现 harness 的雏形，相关设计记录在《Build your own vulnerability harness》中。当前公开内容仅提供高层功能描述，缺乏可供 harness 实现参考的技术细节。

rss · GitHub Trending Daily · 11月8日 23:00

**「设计要点」** 该 skill 采用隔离子代理多阶段编排架构，依次执行侦察、覆盖导向狩猎、候选验证、结构化输出、独立记录验证、目标中性报告六个环节，最终生成可复用的安全审计结果。

**标签**: `#subagents`, `#sandbox`, `#tools`, `#planning`

---

## Agent 工程师日报
{: #sec-agent-engineer .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-agent-engineer" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-agent-engineer-1"></a>
### [斯坦福 CS146S 课程 Monaco 实践](https://latent.space/p/one_million_ai_engineer_special_how_stanford_teaches_ai-native_engineering_mihail_eric_monaco/) ⭐️ 7.0/10

2026 年 11 月 8 日发布的 Latent.Space 访谈中，斯坦福 CS146S 授课教师、Monaco AI 负责人 Mihail Eric 分享了两类实践：一是斯坦福 CS146S 第二次开课时，因学生普遍用 coding agent 可一键完成往年作业，将部分作业调整为向不熟悉的开源项目提交补丁，由项目维护者评审学生提交的修改及解释；二是 Monaco 的 AI agent 落地细节，包括为每个 agent 建独立工作区、代码审查工具采用买断方案、on-call agent 接入 Datadog 与 GitHub，工具选型遵循“买来学习、自研留存”原则。内容直接面向 AI agent 工程师、coding agent 评估与工具链开发者。

rss · Latent Space · 11月8日 21:23

**「为什么重要」** 这类未经过度包装的一手实践分享，既提供了高校应对 coding agent 普及的课程设计实证，也给出了生产环境 agent 工具链选型、on-call agent 集成的可落地参考，填补了学术课程设计与工业实践之间的细节空白。

**「可关注」** 可关注：传统 coding 能力评估在 agent 普及下失效时，可转向真实开源社区贡献流程设计评估；生产 agent 工具链选型可参考“买来学习、自研留存”的决策逻辑，优先验证外部工具价值再决定是否自研。

**标签**: `#coding-agent`, `#eval`, `#harness`

---

<a id="item-agent-engineer-2"></a>
### [SQLite parse\_number\(\) C vs Rust 对比](https://simonwillison.net/2026/Nov/8/sqlite-parse-number-c-vs-rust/) ⭐️ 6.0/10

Simon Willison 于 2026-11-08 发布研究，记录使用 Claude Opus 5.5 辅助开发 SQLite parse\_number\(\) 扩展的过程，对比 C 与 Rust 实现的性能及代码复杂度。测试基于 200 万行数据，对比基线包括初始 C 实现、优化后 C 实现、rusqlite 及 sqlite-loadable-rs 实现。优化后 C 实现每行净成本最低（混合数据 19 ns、纯整数 16 ns、纯小数 18 ns），优于 Rust 实现（rusqlite：46 ns/36 ns/55 ns；sqlite-loadable：41 ns/32 ns/47 ns）。二进制体积方面，C 扩展仅 14 KB，而 Rust 扩展分别为 321 KB 与 298 KB。测试结果受具体硬件与数据分布影响，实际收益需结合部署场景评估。

rss · Simon Willison · 11月8日 22:26

**「为什么重要」** 该研究提供了 SQLite 扩展开发的量化对比基准，证明在文本解析场景下，手写优化 C 代码可同时实现更低延迟与更小二进制体积，但 Rust 生态仍具备快速迭代优势。

**「可关注」** 可关注：SQLite 扩展开发中，Rust 生态（rusqlite、sqlite-loadable-rs）可快速产出功能正确的实现，但若追求极致单行性能与最小二进制体积，仍需手写优化 C 代码。

**标签**: `#coding-agent`, `#tooling`, `#performance`

---

<a id="item-agent-engineer-3"></a>
### [Kimi-K3.1-Pro-Coder 2.8T 社区 56% 量化实验](https://www.reddit.com/r/LocalLLaMA/comments/1xr777l/kimik31procoder_28t_177_tb_775_gb_56_368_tps/) ⭐️ 5.5/10

2026 年 11 月 8 日，Reddit 用户 /u/Grawnch 发布未经验证的社区实验：对 2.8T 参数的 Kimi-K3.1-Pro-Coder MoE 模型做三层分级量化，体积从原生 1.77TB 降至 775GB，降幅 56%。量化方案将 384 个路由专家分为 3 档（2.81/2.56/1.44 bpw，平均约 1.92bpw），共享专家、注意力层与嵌入层保留 BF16/F32 精度；配套开发 Strata 三级卸载引擎（分热 GPU 显存、温 pinned 内存、冷 NVMe mmap，路由器预取有效命中率 97.9%）与 dr-triton 融合反量化内核。测试环境为单块 RTX PRO 6000 Blackwell（96GB 显存）+ 176GB 内存的 Colab 实例，批量吞吐 36.8 TPS，单流解码 10.8 TPS；AIME 2025 与 LiveCodeBench 得分均为 96.7%，与原生 1.77TB 基座模型完全一致，困惑度仅上升 1.01%~2.67%。该实验仅适用于有自定义推理 pipeline 的用户，权重无法直接接入 llama.cpp、vLLM 等通用框架，且无官方来源佐证相关数据。

reddit · r/LocalLLaMA · /u/Grawnch · 11月8日 19:45

**「为什么重要」** 本次社区实验验证了大参数 MoE 模型可通过分层量化+三级卸载在单卡+系统内存+NVMe 环境下运行，且 coding/math 推理性能几乎无损失，为资源有限的超大参数模型部署提供了新思路。但该方案为社区单方面发布，尚未有第三方复现验证，通用性与硬件适配性仍不明确。

**「可关注」** 访问频率不均的 MoE 路由专家适合做分层量化，配合预取卸载可降低单卡运行门槛，但自定义权重重排的模型无法直接接入通用推理框架，需配套自定义加载与反量化内核。

**标签**: `#coding-agent`, `#eval`

---