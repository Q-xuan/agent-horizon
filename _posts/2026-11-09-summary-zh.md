---
layout: default
title: "Horizon Summary: 2026-11-09 (ZH)"
date: 2026-11-09
lang: zh
---

> 从 150 条内容中筛选出 6 条重要资讯。

<nav id="ah-toc" class="ah-toc" aria-label="目录"><span class="ah-toc-title">目录</span><ul><li><a href="#sec-harness-arch"><span class="ah-toc-name">Harness 架构</span><span class="ah-toc-count">3条</span></a></li><li><a href="#sec-agent-engineer"><span class="ah-toc-name">Agent 工程师日报</span><span class="ah-toc-count">3条</span></a></li></ul></nav>

---

**[Harness 架构](#sec-harness-arch)**
1. [OpenAI Agents SDK v0.24.0-alpha.7 发布](#item-harness-arch-1) ⭐️ 8.8/10
2. [openai-agents-js v0.22.0-alpha.2 发布](#item-harness-arch-2) ⭐️ 7.8/10
3. [Cloudflare 安全审计工具开源](#item-harness-arch-3) ⭐️ 5.5/10

**[Agent 工程师日报](#sec-agent-engineer)**
1. [Stanford CS146S 谈 AI 原生工程教学](#item-agent-engineer-1) ⭐️ 6.0/10
2. [Sketchpad：VLM 精确算术验证](#item-agent-engineer-2) ⭐️ 6.0/10
3. [Kimi K3.1 Pro Coder 775GB 量化版公开](#item-agent-engineer-3) ⭐️ 6.0/10

---

## Harness 架构
{: #sec-harness-arch .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-harness-arch" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-harness-arch-1"></a>
### [OpenAI Agents SDK v0.24.0-alpha.7 发布](https://github.com/openai/openai-agents-python/releases/tag/v0.24.0-alpha.7) ⭐️ 8.8/10

OpenAI Agents SDK v0.24.0-alpha.7 引入 classic/native 运行时分裂，执行器写入策略默认改为 strict，新增 CustomStorage 持久化会话，并集成 FileSearch、CodeInterpreter、ImageGeneration 等托管工具。该版本包含多项破坏性变更，包括 MCP 审批模式重命名、子步骤回调签名调整，以及 ElicitationRequest 类型拆分，升级前需审查环境兼容性。

github · markstuart-oai · 11月8日 07:05

**「设计要点」** 运行时拆分为 classic 与 native 双线，classic 通过 agents.classic 保留 v0 行为。执行器层默认启用 strict 写入策略，仅工作目录可写，需通过 writable\_roots 扩展。存储层新增 CustomStorage 接口支持应用自有持久化，托管工具通过兼容的 Responses provider 提供，与本地执行和经典对象保持隔离。

**「改了什么」** 相对 v0.24.0-alpha.6，新增 classic 运行时导入路径、strict 默认写入策略、CustomStorage/SQLiteSessionStore、托管工具集成、语音工作流、RunBudget 使用预算、MCP 资源与提示读取、本地执行支持。破坏性变更包括：approval\_mode 的 auto/approve 重命名为 native/preapproved，NativeAgents.before\_step 参数改为 ChildStepContext，ElicitationRequest 拆分为 FormRequest 与 UrlRequest。

**标签**: `#runtime`, `#tools`, `#memory`, `#sandbox`, `#permissions`

---

<a id="item-harness-arch-2"></a>
### [openai-agents-js v0.22.0-alpha.2 发布](https://github.com/openai/openai-agents-js/releases/tag/v0.22.0-alpha.2) ⭐️ 7.8/10

openai-agents-js v0.22.0-alpha.2 是 OpenAI 发布的 JavaScript SDK 预览版本。该版本引入原生工具（fileSearch\(\)、codeInterpreter\(\)、imageGeneration\(\)）与 A2A 1.0 协议支持，新增 RunBudget 和 maxModelSteps 运行控制，以及应用拥有的 SessionStore 会话持久化。当前预览版明确限制不支持 MCP、手动工具、环境、原生子代理、目标或可移植检查点。升级需同步更新五个 bundled SDK 包，并替换已移除的 SDKRunner bridge。

github · markstuart-oai · 11月8日 08:27

**「设计要点」** 原生运行时迁移至独立的 @openai/agents-codex 包，应用层仍通过 @openai/agents 统一导入。原生与经典代理状态相互隔离，应用负责授权、持久存储、执行及不确定突变的协调；新环境默认启用 writePolicy: &\#x27;strict&\#x27; 执行策略。

**「改了什么」** 新增 fileSearch\(\)、codeInterpreter\(\)、imageGeneration\(\) 原生工具及 webSearch\(\) 增强，支持流式进度与保留结果。引入 maxModelSteps 精确步进控制、RunBudget 资源限制、应用拥有的 SessionStore 持久化，以及基于 JSON-RPC 轮询的 A2A 1.0 远程代理通信。

**标签**: `#runtime`, `#tools`, `#memory`, `#permissions`, `#a2a`

---

<a id="item-harness-arch-3"></a>
### [Cloudflare 安全审计工具开源](https://github.com/cloudflare/security-audit-skill) ⭐️ 5.5/10

这是 Cloudflare 于 2026-11-09 登上 GitHub Trending 的开源编码代理安全审计工具。该工具可将普通编码代理转化为安全审计器，通过多阶段流程编排隔离子代理完成审计任务，输出经独立验证、机器可读的标准化安全发现，是其内部漏洞发现 harness 的基础组件。

rss · GitHub Trending Daily · 11月9日 02:48

**「设计要点」** 该工具采用分阶段编排隔离子代理的架构，审计流程覆盖侦察、覆盖引导狩猎、候选验证、结构化输出、独立记录验证、目标中性报告六个环节，最终输出可被机器解析的审计结果。

**「改了什么」** 本次为 Cloudflare 首次将该工具开源，此前该工具仅作为内部漏洞发现 harness 的基础组件使用，未对外公开。

**标签**: `#subagents`, `#eval`, `#planning`, `#tools`

---

## Agent 工程师日报
{: #sec-agent-engineer .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-agent-engineer" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-agent-engineer-1"></a>
### [Stanford CS146S 谈 AI 原生工程教学](https://latent.space/p/cs146s/) ⭐️ 6.0/10

2026 年 11 月 8 日，Latent Space 发布对 Stanford CS146S（AI 原生工程课程）讲师、Monaco AI 负责人 Mihail Eric 的访谈，分享 AI 原生工程的教学思路与工业界实践。CS146S 上一轮授课时已发现绝大多数学生日常使用 coding agent，本轮课程将部分作业调整为向开源项目提交 PR 并由维护者评审，要求学员补全 agent 难以独立完成的需求沟通、影响面评估等环节；Monaco 团队评估后保留 Devin 承担代码评审，自研 agent 专属工作区用于运行产品、复现故障和测试补丁，同时搭建 Hal 系统同时服务工程师排查故障和销售向客户解释产品逻辑。目前未公开该课程调整或 Monaco 自研工具的具体效果数据，相关经验主要面向 AI agent 工程师、coding agent 教学者提供参考。

rss · Latent Space · 11月8日 21:41

**「为什么重要」** 这是高校首次系统性将 coding agent 使用、开源协作能力纳入 AI 原生工程核心课程体系，同时工业界给出了「采购工具学习、自研工具留存」的 coding agent 选型逻辑，对 AI agent 工程师的工具选型和能力建设有直接参考价值；但这些经验是否能适配不同规模、不同领域的工程团队，目前没有公开的跨场景验证数据。

**「可关注」** 可关注：用可视化 diff 讲解工具验证 agent 产出的逻辑合理性，以及为 agent 搭建可运行、可复现故障的专属工作区，都是当前教学和工业场景中已验证的落地方向。

**标签**: `#coding-agent`, `#orchestration`, `#eval`, `#harness`

---

<a id="item-agent-engineer-2"></a>
### [Sketchpad：VLM 精确算术验证](https://huggingface.co/papers/2611.04434) ⭐️ 6.0/10

2026-11-09，Hugging Face Daily Papers 收录预印本 Sketchpad，提出用小型 VLM 实现精确算术的形式化验证方法，区别于普通语言模型的无保证准确与工具调用的计算外移。该方法以 Qwen3.5-0.8B 加 low-rank adapter 在渲染 sheet 上执行算术，每次前向传播仅读取三单元有界外部工作记忆视图，并输出一步（数字、进位或借位、下一操作），固定运行时移动视图且不写入结果数字。研究者在 Lean 中证明：模型在所有长度输入上精确，当且仅当它在有限视图集上精确。该工作目前仅覆盖算术任务，尚无生产工具或对 agent 工程工作流的直接变更，需进一步适配才能对多数 agent 开发者产生可操作影响。

rss · Hugging Face Daily Papers · 11月9日 00:00

**「为什么重要」** 该工作将可验证逐步推理从算术扩展到 agent 设计的潜在原理，但当前证据仅支持算术场景，尚未证实对通用 agent 工作流的实际增益。

**「可关注」** 可关注：有界外部工作记忆视图将模型精确性转化为有限可检查属性，这一机制或可迁移到 agent 记忆设计与逐步推理评估。

**标签**: `#eval`, `#memory`

---

<a id="item-agent-engineer-3"></a>
### [Kimi K3.1 Pro Coder 775GB 量化版公开](https://www.reddit.com/r/LocalLLaMA/comments/1xr777l/kimik31procoder_28t_177_tb_775_gb_56_368_tps/) ⭐️ 6.0/10

2026 年 11 月 8 日，Reddit 用户 Grawnch 公开了 2.8T 参数 Kimi K3.1 Pro Coder MoE 模型的实验性 3 层量化方案，将模型体积从原生 1.77TB 压缩至 775GB，支持单 GPU+系统 RAM+NVMe 运行。方案对每层 384 个路由专家做 3 档量化（2.81/2.56/1.44 bpw，平均约 1.92bpw），共享专家、注意力层、嵌入层保留 BF16/F32 精度，配套自研 Strata 三级卸载引擎和 dr-triton 融合反量化内核，路由器预取有效命中率达 97.9%。发布者自报告在单张 RTX PRO 6000 Blackwell（96GB 显存）+176GB RAM 环境下，该量化版与原生 1.77TB 版本的 AIME 2025、LiveCodeBench 评测得分完全一致（均为 96.67%），Batch 吞吐量 36.8 TPS、单流解码吞吐量 10.8 TPS。该方案为实验性实现，未获官方验证，自定义路由专家张量布局无法直接兼容 llama.cpp、vLLM 等主流推理框架。

reddit · r/LocalLLaMA · /u/Grawnch · 11月8日 19:45

**「为什么重要」** 这是目前公开的首个将 2.8T 级 MoE coding 模型压缩至单卡可运行体量的实验方案，验证了分层专家量化+三级卸载在 coding/math 推理场景的可行性。但该方案的复现性、长期稳定性以及对其他 MoE coding 模型的迁移效果尚未得到社区验证。

**「可关注」** 可关注：该方案的自定义路由专家张量布局无法直接接入 llama.cpp、vLLM 等主流推理框架，但可单独复用 dr-triton 反量化模块适配自定义推理管线，且三级卸载的显存/内存/NVMe 分配比例可根据硬件配置调整。

**标签**: `#eval`, `#coding-agent`, `#model-quantization`

---