---
layout: default
title: "Horizon Summary: 2026-10-16 (ZH)"
date: 2026-10-16
lang: zh
---

> 从 206 条内容中筛选出 16 条重要资讯。

<nav id="ah-toc" class="ah-toc" aria-label="目录"><span class="ah-toc-title">目录</span><ul><li><a href="#sec-harness-arch"><span class="ah-toc-name">Harness 架构</span><span class="ah-toc-count">3条</span></a></li><li><a href="#sec-agent-engineer"><span class="ah-toc-name">Agent 工程师日报</span><span class="ah-toc-count">6条</span></a></li><li><a href="#sec-ai-daily"><span class="ah-toc-name">AI 日报</span><span class="ah-toc-count">6条</span></a></li><li><a href="#sec-ai-deals"><span class="ah-toc-name">AI 羊毛</span><span class="ah-toc-count">1条</span></a></li></ul></nav>

---

**[Harness 架构](#sec-harness-arch)**
1. [Codex rust-v0.163.0 发布](#item-harness-arch-1) ⭐️ 7.8/10
2. [openai-agents-python v0.24.0 发布](#item-harness-arch-2) ⭐️ 7.8/10
3. [Agent Framework 1.22.0](#item-harness-arch-3) ⭐️ 7.8/10

**[Agent 工程师日报](#sec-agent-engineer)**
1. [Granite Switch 4.1 发布](#item-agent-engineer-1) ⭐️ 7.8/10
2. [Meta Muse Spark Open 开源](#item-agent-engineer-2) ⭐️ 7.8/10
3. [Player-1 游戏 agent 训练框架](#item-agent-engineer-3) ⭐️ 7.0/10
4. [Doc2Harness 编码 Agent 基准发布](#item-agent-engineer-4) ⭐️ 7.0/10
5. [HF Daily Papers: 智能体 RL 自蒸馏现实检验](#item-agent-engineer-5) ⭐️ 7.0/10
6. [CLASHarness 论文：多智能体冲突可控制生成框架](#item-agent-engineer-6) ⭐️ 7.0/10

**[AI 日报](#sec-ai-daily)**
1. [Anthropic 推进第三方模型独立评估](#item-ai-daily-1) ⭐️ 8.3/10
2. [OpenAI 推出 Rosalind 学术计划](#item-ai-daily-2) ⭐️ 7.8/10
3. [GitHub 共享组织安全自动化实践公开](#item-ai-daily-3) ⭐️ 7.8/10
4. [Claude Code Review 正式 GA](#item-ai-daily-4) ⭐️ 7.8/10
5. [Google 发布 AI 智能体评估指南](#item-ai-daily-5) ⭐️ 7.8/10
6. [Google OAuth 支持 DPoP 保护刷新令牌](#item-ai-daily-6) ⭐️ 7.8/10

**[AI 羊毛](#sec-ai-deals)**
1. [OpenCode 免费开放 DeepSeek V4.1 Flash](#item-ai-deals-1) ⭐️ 7.0/10

---

## Harness 架构
{: #sec-harness-arch .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-harness-arch" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-harness-arch-1"></a>
### [Codex rust-v0.163.0 发布](https://github.com/openai/codex/releases/tag/rust-v0.163.0) ⭐️ 7.8/10

OpenAI Codex agent harness 发布 rust-v0.163.0。核心运行时新增独立只读工具并行执行、响应中中断并终止嵌套工具调用、托管守护进程重启与自动重连。配置层支持 \`/config\` 实时搜索偏好并即时生效、\`/keymap\` 自定义 leader key、\`/daemon\` 管理后台服务。网络代理增加权限前置检查，沙箱层引入 bubblewrap 与 Seatbelt 完整性校验，Daybreak 默认启用。

github · github-actions\[bot\] · 10月15日 21:30

**「设计要点」** 工具层支持按只读属性并行调度 skill、memory、history 查询，减少串行等待。中断机制在响应流中插入停止点，可终止 Code Mode 内嵌工具调用链。网络代理在 DNS 解析前执行权限校验，沙箱在命令与文件系统操作前运行完整性检查。

**「改了什么」** 新增独立只读工具并行执行、响应中中断并停止嵌套工具调用、托管守护进程重启警告与自动重连。\`/config\` 支持跨类别搜索偏好并即时生效，\`/keymap\` 新增 leader key 配置。不再打包 patched zsh，改用标准 shell executor。

**标签**: `#runtime`, `#tools`, `#memory`

---

<a id="item-harness-arch-2"></a>
### [openai-agents-python v0.24.0 发布](https://github.com/openai/openai-agents-python/releases/tag/v0.24.0) ⭐️ 7.8/10

openai-agents-python 是 OpenAI 开源的 Python agent harness。v0.24.0 于 2026-10-15 发布，新增 MCP 转换工具注解暴露与全局工具异常格式化能力，修复会话写入 API 限流批处理及待审批时上下文提前压缩问题，同时升级多项依赖。

github · openai-sdks\[bot\] · 10月15日 02:20

**「设计要点」** 工具层通过注解暴露 MCP 元数据，支持 run-wide 异常格式化；会话写入改为 API 限流内批处理；待审批场景下延迟自动压缩；Redis compaction history 采用原子替换；运行上下文过滤不可序列化 dataclass；sandbox  redaction 保留调用方异常。

**「改了什么」** 相对 v0.23.1，新增 MCP 注解透传和全局工具异常格式化；修复会话写入超限、待审批时误压缩上下文及 sandbox  redaction 异常保留问题；Redis 历史压缩改为原子操作；省略不可序列化运行上下文；升级 fastapi、grpcio、redis、temporalio 等依赖。

**标签**: `#mcp`, `#tools`, `#runtime`, `#memory`

---

<a id="item-harness-arch-3"></a>
### [Agent Framework 1.22.0](https://github.com/microsoft/agent-framework/releases/tag/python-1.22.0) ⭐️ 7.8/10

Microsoft Agent Framework Python 1.22.0 正式发布。核心框架与根包 \`agent-framework\` 新增 Python 3.15 运行时支持，但部分包、可选 extra 及功能因上游依赖限制暂未覆盖，升级前需查阅各包 README 确认限制。持久化状态格式发生兼容性变更：1.22 可读取旧版写入的记录，但旧版运行时无法解析包含 \`hosted\` 或 \`merge\_mode\` 字段的新记录；涉及聊天历史、会话存储、工作流检查点中的序列化 Content 与流式响应更新。本次更新同时统一内容身份、托管执行、协议元数据、重放及流合并语义，并在 AG-UI、Declarative 等模块引入多项 breaking changes。

github · eavanvalkenburg · 10月15日 09:53

**「设计要点」** 持久化层采用向前兼容读取、向后不兼容写入策略，要求滚动部署期间新旧 worker 不得共用同一受影响的存储实例。AG-UI 模块实施故障关闭（fail-closed）请求信任边界，将工作流继续与中断绑定至解析后的线程 ID，并隔离客户端共享状态对工具批准状态的篡改风险。

**「改了什么」** 新增 Cosmos memory provider 专属 User-Agent token、OAuth consent 请求在非流式响应中暴露、Ollama 与 OpenAI chat client 可配置服务 URL、Oracle 连接池配置透传。多项 breaking changes 统一跨提供商内容与流语义，AG-UI 强化线程级信任边界与状态隔离，Declarative 为 HTTP 响应体与压缩解码增加可配置上限。

**标签**: `#runtime`, `#memory`

---

## Agent 工程师日报
{: #sec-agent-engineer .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-agent-engineer" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-agent-engineer-1"></a>
### [Granite Switch 4.1 发布](https://huggingface.co/blog/ibm-granite/granite-switch-4-1) ⭐️ 7.8/10

IBM 于 2026 年 10 月 15 日发布 Granite Switch 4.1，推出 8B 与 30B 两个版本，集成了通用决策 aLoRA、安全决策 Guardian aLoRA、语音转录 Granite-Speech-5.0-Turbo-CTC 三类适配器，单模型覆盖对话、决策、语音能力，其中 Guardian aLoRA 在安全相关决策任务上的平均表现优于 Jev 1.13、Microsoft-Decision-1、GPT-Luna-Decisions、Clef-Flash 等基线模型。该模型采用缓存高效的 Activated LoRAs 架构，总 VRAM 占用与基座 Granite 模型相当，基座生成的 KV 缓存可跨适配器复用，同时整合了 vLLM 对低秩适配器推理的优化。官方测试显示 Granite-Switch-4.1-30B 在 5 步 RAG 工作流中完成速度快于 Jev-27B，目前部分性能细节尚未公开，官方称后续数周会补充更多数据。

rss · Hugging Face Blog · 10月15日 20:34

**「为什么重要」** 该发布验证了多能力单模型部署的硬件可行性，通过 KV 缓存复用与低秩适配器优化，降低了同时支持对话、决策、语音场景的部署成本。目前社区自定义适配器生态、官方 Adapter SDK 与 Mellea 训练教程均未落地，实际扩展效果与第三方适配器兼容性待验证。

**「可关注」** 可关注：Activated LoRAs 的 KV 缓存跨适配器复用机制，可降低多任务 Agent 的部署显存成本。

**标签**: `#architecture`, `#memory`, `#orchestration`, `#efficiency`, `#model-release`

---

<a id="item-agent-engineer-2"></a>
### [Meta Muse Spark Open 开源](https://huggingface.co/blog/meta-muse-spark-open) ⭐️ 7.8/10

2026 年 10 月 15 日 Hugging Face 官方博客发布 Meta 开源模型 Muse Spark Open，这是 Meta 针对 agentic coding 场景优化的开源权重多模态 MoE 模型，总参数量约 816B，每 token 激活参数量约 42B，每层 MoE 块含 256 个专家、每 token 选 8 个，支持文本、图像、音频、视频输入，上下文窗口达 1M tokens，提供 BF16（约 1.5TB safetensors 格式）和 NVFP4 两种检查点，前者需 4 个 8 卡 H200 节点（TP=32）部署，后者针对 NVIDIA Blackwell GPU 优化，可单 B200 节点运行。Meta 将其描述为目前能力最强的美国开源权重模型，配套了部署、微调指南及编码 agent 用例参考。该模型属于 Meta Muse 系列，此前已发布同系列小型密集模型 Muse Glimmer，二者使用相同 tokenizer 与词汇表，聊天模板在 Muse Glimmer 基础上新增多模态支持，直接面向构建 coding agent 系统的工程师群体开放。

rss · Hugging Face Blog · 10月15日 00:00

**「为什么重要」** 这是目前少数同时覆盖多模态输入、针对编码工作流优化、且开源权重的超大规模 MoE 模型，配套的部署和微调指南可降低 coding agent 系统的集成成本；但模型实际编码任务表现、推理效率等仍需社区验证。

**「可关注」** 可关注：Muse Spark Open 的 MoE 架构实现全量参数驻留内存、每 token 仅激活 42B 参数，部署时需优先评估显存容量与推理速度的平衡，NVFP4 量化版可大幅降低硬件门槛。

**标签**: `#coding-agent`, `#harness`

---

<a id="item-agent-engineer-3"></a>
### [Player-1 游戏 agent 训练框架](https://huggingface.co/papers/2610.20584) ⭐️ 7.0/10

2026-10-15 HF Daily Papers 收录论文《Player-1: Learning to Play from Synthetic Experience》，提出游戏控制 agent 的 post-training 框架 Player-1，支持 agent 从合成经验学习，替代传统仅依赖大规模演示的训练模式；框架扩展计算机操作动作空间，新增相对指针移动、持续输入、复合动作三类能力；监督初始化阶段在 6044 条 curated 数据上微调计算机操作模型。

rss · Hugging Face Daily Papers · 10月15日 00:00

**「为什么重要」** 该框架针对游戏 agent 训练中演示复盖动态游戏状态不足的行业痛点提供解决路径，其扩展的动作空间与合成经验训练范式，对构建 computer-use、游戏类 agent 的工程师有直接参考价值。

**「可关注」** 可关注：Player-1 扩展的计算机操作动作空间（相对指针移动、持续输入、复合动作）与合成经验训练范式，可对应到现有游戏、computer-use agent 的训练流程优化。

**标签**: `#coding-agent`, `#orchestration`, `#eval`

---

<a id="item-agent-engineer-4"></a>
### [Doc2Harness 编码 Agent 基准发布](https://huggingface.co/papers/2610.20344) ⭐️ 7.0/10

2026 年 10 月 15 日，Hugging Face Daily Papers 发布论文提出 Doc2Harness 两阶段基准，用于直接评估大模型在编码 Agent 上的长期 Harness 工程能力，填补了现有基准仅评估固定 Harness 下下游任务表现、未覆盖 Harness 工程本身的空白。Stage1 中，构建模型在固定构建 Harness 内接收仅接口的合同骨架与整合 12 个前沿 Harness 行为的开发文档，在隔离容器中生成完整候选 Harness；Stage2 将冻结的候选 Harness 部署于独立容器运行，目前仅公开论文摘要，未披露完整评测结果。

rss · Hugging Face Daily Papers · 10月15日 00:00

**「为什么重要」** 当前编码 Agent 落地过程中，Harness 工程设计能力长期缺乏量化评测手段，该基准直接针对这一空白设计，可支撑后续 Harness 工程能力的标准化评估，但完整评测结果尚未公开，实际对工程实践的指导价值待验证。

**「可关注」** 可关注该基准的两阶段设计逻辑，以及其整合的 12 个前沿 Harness 行为文档对 Harness 工程实践的参考意义。

**标签**: `#harness`, `#eval`, `#coding-agent`

---

<a id="item-agent-engineer-5"></a>
### [HF Daily Papers: 智能体 RL 自蒸馏现实检验](https://huggingface.co/papers/2610.19789) ⭐️ 7.0/10

2026 年 10 月 15 日，Hugging Face Daily Papers 收录论文《More Methods, Better Agents? A Reality Check on Self-Distillation in Agentic Reinforcement Learning》，该研究开展大规模受控对比实验，将 10 种智能体强化学习自蒸馏方法与 GRPO 对比，覆盖 ALFWorld、ScienceWorld、Search-QA、WebShop 4 个基准、3 种模型尺寸，总计 132 次训练运行、12124.4 条记录的 H800 GPU 小时，旨在解决现有评估基线报告不一致、同期方法直接对比少、训练稳定性与计算成本分析不足的问题，为智能体训练工程师提供共同比较基础。

rss · Hugging Face Daily Papers · 10月15日 00:00

**「为什么重要」** 该研究填补了现有智能体强化学习自蒸馏方法评估的核心 gap，为高成本的智能体训练提供了受控对比的基础数据；目前尚未证实具体方法的最优性，但可减少工程师选型时的基线不一致干扰。

**「可关注」** 可关注：现有智能体 RL 自蒸馏方法的评估基线不统一、训练稳定性与计算成本分析不足，该研究提供的受控对比数据可作为方法选型的参考基准。

**标签**: `#eval`, `#coding-agent`

---

<a id="item-agent-engineer-6"></a>
### [CLASHarness 论文：多智能体冲突可控制生成框架](https://huggingface.co/papers/2610.19128) ⭐️ 7.0/10

Hugging Face Daily Papers 于 2026-10-15 介绍预印本 CLASHarness（Conflict-Loaded Agent Scenario Harness）。该框架提供可控 pipeline，用于生成和评测多智能体在计算机使用中的冲突场景，填补现有基准仅假设合作环境的空白。现有手动编写方案无法扩展，无约束 LLM 生成则产生叙事漂移、答案泄露和不可满足的评分标准。该工作直接影响构建或评估多智能体自动化系统的工程师。

rss · Hugging Face Daily Papers · 10月15日 00:00

**「为什么重要」** 多智能体冲突场景是当前计算机使用基准的测试盲区，CLASHarness 首次提供可控生成与验证的评测框架。该预印本尚未经过同行评审，其生成 pipeline 的可控性和评分标准有效性仍需社区验证。

**「可关注」** 可关注：现有计算机使用基准多假设合作环境，CLASHarness 针对信息不一致、矛盾指令、权限竞争等冲突场景提供可控生成与评测框架，可补充多智能体系统的评估盲区。

**标签**: `#eval`, `#harness`, `#permissions`

---

## AI 日报
{: #sec-ai-daily .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-daily" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-daily-1"></a>
### [Anthropic 推进第三方模型独立评估](https://www.anthropic.com/news/an-update-on-independent-evaluators) ⭐️ 8.3/10

Anthropic 宣布推进模型独立第三方评估工作，已向非营利评估机构 METR 开放员工级访问权限，6 名 METR 员工获得公司硬件、办公空间及内部工具访问权，仅客户数据、律师-客户特权信息、模型架构信息等少数预定义类别可要求红删，METR 评估结果发布权不受 Anthropic 否决，过去一年双方已合作完成多轮风险报告评审。同时 Anthropic 正与 SecureBio、Accenture、Faculty 开展评估合作，与 Hugging Face 等机构处于早期洽谈阶段，相关推进对应其此前签署白宫超级智能协议的承诺。

rss · Anthropic News · 10月15日 00:00

**「为什么重要」** 这是前沿 AI 公司首次公开推进分级独立评估嵌入机制，为行业安全监督提供了可参考的实践样本，也对应了白宫超级智能协议中&quot;与独立外部审计方合作&quot;的承诺履行。

**「可关注」** 可关注：Anthropic 设计的评估方三级访问体系，以及 METR 评估结果发布不受 Anthropic 否决、仅可对预定义类别要求红删的约束机制。

**标签**: `#lab`, `#policy`, `#eval`

---

<a id="item-ai-daily-2"></a>
### [OpenAI 推出 Rosalind 学术计划](https://openai.com/index/introducing-the-rosalind-academic-plan) ⭐️ 7.8/10

2026 年 10 月 15 日 OpenAI 官方博客宣布推出 Rosalind 学术计划，为符合条件的高校生命科学研究实验室提供赞助，可免费使用 GPT-Rosalind 及相关生命科学工具，用于推进生命科学研究。

rss · OpenAI Blog · 10月15日 19:00

**「为什么重要」** 该计划降低了高校生命科学研究团队使用前沿 AI 生命科学工具的门槛，有望加速相关领域的研究进展。

**「可关注」** 符合条件的高校生命科学研究实验室可申请该计划的赞助权益。

**标签**: `#model`, `#lab`, `#product`, `#industry`

---

<a id="item-ai-daily-3"></a>
### [GitHub 共享组织安全自动化实践公开](https://github.blog/engineering/platform-security/staying-evergreen-how-we-automated-secure-access-and-repo-hygiene-in-a-shared-org/) ⭐️ 7.8/10

GitHub 官方博客于 2026 年 10 月 15 日发布工程实践文章，公开其通过原生 GitHub 平台功能，自动化实现共享组织内外部协作者访问自动审查、过期仓库自动归档的方案，未披露具体实施规模与性能指标。

rss · GitHub Blog · 10月15日 18:00

**「为什么重要」** 该内容为 GitHub 官方公开的内部平台安全工程实践，为同类共享组织的访问管控与仓库卫生管理提供了可复用的原生功能方案参考。

**「可关注」** 可关注：使用原生 GitHub 功能即可实现共享组织的外部协作者访问自动审查与过期仓库自动归档，无需额外自研工具。

**标签**: `#industry`, `#product`, `#security`

---

<a id="item-ai-daily-4"></a>
### [Claude Code Review 正式 GA](https://claude.com/resources/articles/code-review-is-now-generally-available) ⭐️ 7.8/10

Anthropic 宣布 Claude Code Review 结束研究预览阶段，正式向 Team 及 Enterprise 组织开放。本次 GA 带来三项核心优化：多数审查耗时从约 20 分钟降至 6–10 分钟，提速约 3 倍；优化缺陷识别能力，输出更简洁清晰的审查结论；管理员可按仓库选择 Quick、Standard、Deep 三种审查模式。此外，符合资格的 Claude Enterprise 组织可在 2027 年 1 月 15 日前申请至少 10000 美元的 Code Review 信用额度，额度在申领后 30 天内过期。

rss · Claude Blog · 10月15日 00:00

**「为什么重要」** 当前 AI 编码助手普及但代码审查瓶颈未明显缓解，Claude Code Review 正式 GA 为团队提供了可直接落地的自动化审查方案，配套的企业信用额度激励也降低了试用成本。

**「可关注」** 可关注：Claude Code Review 支持管理员按仓库选择 Quick、Standard、Deep 三级审查模式，开发者无需额外配置即可自动对新 PR 执行审查。

**标签**: `#product`, `#industry`, `#lab`

---

<a id="item-ai-daily-5"></a>
### [Google 发布 AI 智能体评估指南](https://developers.googleblog.com/evaluating-ai-agents-moving-past-the-vibe-check/) ⭐️ 7.8/10

Google Developers AI 发布官方 AI 智能体评估指南，指出 informal vibe check 测试无法捕捉智能体循环、token 浪费、幻觉输出等隐藏故障。指南提供构建可靠评估管道的实操方案，明确评估是渐进式过程，无需初期搭建复杂自动化架构，可从简单可重复的检查起步。方案包含基于关键用户旅程（CUJ）定义评估标准、用合成用户生成测试场景、分层四类检查、冻结黄金数据集避免基线失效等具体指导，并提到生产级智能体质量通常需要 50 至 60 次小迭代完成。

rss · Google Developers AI · 10月15日 00:00

**「为什么重要」** 当前多数团队仍通过人工跑少量 prompt、 eyeball 输出的方式测试智能体，无法发现循环、冗余调用等隐藏故障。该指南提供了可直接落地的评估框架，降低智能体生产化的测试门槛。

**「可关注」** 可关注：评估初期无需搭建复杂自动化架构，先从基于关键用户旅程的简单可重复检查起步，逐步迭代框架。

**标签**: `#lab`, `#eval`, `#industry`

---

<a id="item-ai-daily-6"></a>
### [Google OAuth 支持 DPoP 保护刷新令牌](https://developers.googleblog.com/announcing-dpop-support-for-google-oauth-securing-refresh-tokens/) ⭐️ 7.8/10

Google 宣布其 OAuth 平台正式支持 DPoP（RFC 9449），仅对刷新令牌做客户端非对称密钥对的加密绑定，短时效访问令牌仍为标准 Bearer 令牌。该设计将长时效刷新令牌与客户端生成的密钥对绑定，可防止令牌被盗后的重放攻击，抵御 Infostealer 恶意软件、AiTM 攻击的利用；同时避免高 QPS 的 Google API（如 Gmail、Calendar、Drive）每请求验证 DPoP 签名带来的巨大计算开销，访问令牌有效期通常不超过 1 小时。DPoP 不保护 Web 应用会话 cookie，多代理链场景下需通过 Google Cloud STS 完成令牌委派，Google 还提供了 DPoP adoption SKILL.md 辅助开发者实现。

rss · Google Developers AI · 10月15日 00:00

**「为什么重要」** 随着自主 AI 代理、MCP 架构的普及，API 令牌安全成为关键需求；Google 作为主流 OAuth 服务商落地 DPoP，为行业提供了可参考的大规模落地实践，同时其针对刷新令牌的约束设计平衡了安全性与性能，适合高吞吐 API 场景。

**「可关注」** 可关注：DPoP 实现需处理客户端密钥生成、时间戳/nonce 校验、DPoP 证明 JWT 构造等逻辑；多代理/多跳 MCP 场景可优先选用 DPoP 替代 mTLS，跨代理委派需通过 Google Cloud STS 完成。

**标签**: `#policy`, `#product`, `#industry`

---

## AI 羊毛
{: #sec-ai-deals .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-deals" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-deals-1"></a>
### [OpenCode 免费开放 DeepSeek V4.1 Flash](https://www.appinn.com/opencode-free-deepseek-v4-1-flash/) ⭐️ 7.0/10

OpenCode 宣布免费提供 DeepSeek V4.1 Flash 模型使用权限，用户更新 OpenCode 程序后，通过输入 /model 命令切换模型即可使用，该模型仅支持 200KB 上下文，材料未标注领取截止时间。

rss · 小众软件 · 10月15日 09:48

**「为什么重要」** 该模型无额外付费门槛，OpenCode 用户更新后即可直接调用，可满足轻量文本处理的零成本试用需求。

**「可关注」** 可关注：该模型仅支持 200KB 上下文，长文本处理场景需注意上下文长度限制，仅适合短输入任务。

**标签**: `#free-tier`, `#promo`, `#limited-free`, `#api`

---