---
layout: default
title: "Horizon Summary: 2026-10-21 (ZH)"
date: 2026-10-21
lang: zh
---

> 从 194 条内容中筛选出 13 条重要资讯。

<nav id="ah-toc" class="ah-toc" aria-label="目录"><span class="ah-toc-title">目录</span><ul><li><a href="#sec-harness-arch"><span class="ah-toc-name">Harness 架构</span><span class="ah-toc-count">3条</span></a></li><li><a href="#sec-agent-engineer"><span class="ah-toc-name">Agent 工程师日报</span><span class="ah-toc-count">8条</span></a></li><li><a href="#sec-ai-daily"><span class="ah-toc-name">AI 日报</span><span class="ah-toc-count">1条</span></a></li><li><a href="#sec-ai-deals"><span class="ah-toc-name">AI 羊毛</span><span class="ah-toc-count">1条</span></a></li></ul></nav>

---

**[Harness 架构](#sec-harness-arch)**
1. [@cloudflare/think 0.21.0 发布](#item-harness-arch-1) ⭐️ 7.8/10
2. [openai-agents-js 0.21.0 发布](#item-harness-arch-2) ⭐️ 7.3/10
3. [OpenHands v1.29.0 发布](#item-harness-arch-3) ⭐️ 6.8/10

**[Agent 工程师日报](#sec-agent-engineer)**
1. [ALTK-Evolve 登顶 τ²-bench 零售榜](#item-agent-engineer-1) ⭐️ 7.8/10
2. [DeepInfer 推理框架开源发布](#item-agent-engineer-2) ⭐️ 7.0/10
3. [eMudhra 8 枚中间 CA 私钥泄露](#item-agent-engineer-3) ⭐️ 7.0/10
4. [决策模型做 Eval 实践指南](#item-agent-engineer-4) ⭐️ 7.0/10
5. [FairStress 公平基准发布](#item-agent-engineer-5) ⭐️ 6.8/10
6. [Allen AI 推出 FairStress](#item-agent-engineer-6) ⭐️ 6.3/10
7. [llm-public-ai 0.1 发布 支持 Public AI](#item-agent-engineer-7) ⭐️ 5.8/10
8. [Qwen3 8B/27B 低精度量化优化](#item-agent-engineer-8) ⭐️ 5.5/10

**[AI 日报](#sec-ai-daily)**
1. [ChatGPT Work 餐饮特许经营案例发布](#item-ai-daily-1) ⭐️ 6.8/10

**[AI 羊毛](#sec-ai-deals)**
1. [WorkBuddy 教师公益版开放申领](#item-ai-deals-1) ⭐️ 8.0/10

---

## Harness 架构
{: #sec-harness-arch .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-harness-arch" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-harness-arch-1"></a>
### [@cloudflare/think 0.21.0 发布](https://github.com/cloudflare/agents/releases/tag/%40cloudflare/think%400.21.0) ⭐️ 7.8/10

@cloudflare/think 0.21.0 将 workspace 工具层统一替换为 @cloudflare/computer 的 createAITools，并移除 legacy workspace tool API。新增 @cloudflare/computer 作为 workspace 功能的强制 peer dependency，同时弃用 @cloudflare/shell 依赖及 execute tool 的 state 选项。Chat recovery 机制引入 maxInterruptedAttempts（默认 5）限制，防止 Durable Object 内存超限的 turn 无限重试。

github · github-actions\[bot\] · 10月20日 15:20

**「设计要点」** 运行时依赖从 @cloudflare/shell 迁移至 @cloudflare/computer，workspace 实现直接复用 Computer 的 Workspace 类。工具调用路径统一通过 exec 的 ws:tools 模块暴露，替代原有的 createExecuteTool 与 createExecuteRuntime 入口。

**「改了什么」** workspace 工具从自研实现切换为 @cloudflare/computer 的 createAITools，移除 createWorkspaceTools、workspaceBash 与 @cloudflare/think/tools/workspace；@cloudflare/shell 依赖及 execute tool 的 state 选项被清除，createExecuteTool 与 createExecuteRuntime 弃用。Chat recovery 新增 maxInterruptedAttempts 上限（默认 5）并弃用 maxOomRetries，调度任务改用单例 Intl.DateTimeFormat 降低 CPU 开销。

**「评论」** 无社区评论。

**标签**: `#tools`, `#runtime`, `#dependencies`

---

<a id="item-harness-arch-2"></a>
### [openai-agents-js 0.21.0 发布](https://github.com/openai/openai-agents-js/releases/tag/%40openai/agents-core%400.21.0) ⭐️ 7.3/10

openai/openai-agents-js 发布 @openai/agents-core@0.21.0。本次移除 Runloop sandbox provider 及其公共 API，属破坏性变更。修复流式运行中 token 使用明细的保留与状态持久化，schema 升级至 1.23 并保持向后兼容读取早期快照。新增对 GPT-6 Astra、Sol、Luna 及 GPT-6.1 Sol 的沙箱动态压缩阈值识别。

github · openai-sdks\[bot\] · 10月20日 22:07

**「设计要点」** 运行时层采用 schema 1.23 持久化 token 使用明细，向后兼容早期快照读取。沙箱层移除 Runloop provider，改由扩展机制提供替代实现。

**「改了什么」** 移除 Runloop sandbox provider 及公共 API，需按迁移指南切换替代方案。修复流式运行、使用统计与保存运行状态中的有界嵌套数字 token 使用明细保留，schema 升至 1.23，并新增 GPT-6 Astra、Sol、Luna 与 GPT-6.1 Sol 的沙箱动态压缩阈值识别。

**标签**: `#sandbox`, `#runtime`

---

<a id="item-harness-arch-3"></a>
### [OpenHands v1.29.0 发布](https://github.com/OpenHands/OpenHands/releases/tag/v1.29.0) ⭐️ 6.8/10

OpenHands v1.29.0 于 2026-10-20 发布，核心新增 per-agent-profile 配置能力。现在可为每个 profile 独立选择 skills、调整 context condenser 与 verification 设置、指定 Model Router。后端选择器开始显示完整组织名称，bundled extensions 包中的 public skills 可被自动加载。此版本未引入重大架构变更或破坏性更新。

github · openhands-release-bot\[bot\] · 10月20日 22:22

**「改了什么」** 相对 v1.28.1，新增 per-agent-profile 细粒度配置（skills、condenser、verification、model router）。修复 chat 模型同步延迟从 10 秒降至 1 秒，uvx 启动器临时限制 Python 3.12-3.14 范围。macOS 桌面版在发布页明确提示 Gatekeeper quarantine 清除命令。

**标签**: `#agent-profiles`, `#tools`, `#memory`, `#runtime`

---

## Agent 工程师日报
{: #sec-agent-engineer .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-agent-engineer" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-agent-engineer-1"></a>
### [ALTK-Evolve 登顶 τ²-bench 零售榜](https://huggingface.co/blog/ibm-research/altk-evolve-bc) ⭐️ 7.8/10

IBM Research 2026 年 10 月 20 日公开 ALTK-Evolve 方法，这是其此前在编程 agent 上验证过的蒸馏试错轨迹生成系统提示准则思路的首次客服场景落地，在不做模型微调、不使用前沿推理模型、无需人工标注的前提下，让配 GPT-4.1 的 agent 在τ²-bench 零售任务上取得 67.5%的 Pass^4，登顶 2026 年 10 月 12 日的该赛道排行榜。Pass^4 为单任务 4 次独立尝试全部成功的占比，是τ²-bench 排行榜的核心指标，该方法仅修改τ²-bench 官方 ReAct 框架的系统提示，其余策略、工具、框架均保持默认，用户模拟器为 GPT-5.5。对比基线，Pass^4 从 57.5%提升 10 个百分点，Mean Accuracy 从 78.1%提升至 82.5%，结果适用于做客服 agent、agent 记忆优化与 eval harness 的工程师。

rss · Hugging Face Blog · 10月20日 15:19

**「为什么重要」** 它证明此前在编程 agent 上验证过的记忆蒸馏思路可迁移至客服场景，且不更换基础模型、不做权重更新就能在标准 eval 上取得 SOTA，打破了提升 agent 性能必须依赖更大推理模型的常见路径。目前该方法仅在τ²-bench 的零售、航空客服场景验证，其他 domain 的泛化效果尚未公开。

**「可关注」** 可关注：蒸馏出的系统提示准则存在 domain 差异，零售场景适合用全量高泛化准则，航空场景少量高支持度核心准则的可靠性更高，且准则增加仅推高输入 token 成本、不增加对话轮数。

**标签**: `#memory`, `#eval`, `#harness`

---

<a id="item-agent-engineer-2"></a>
### [DeepInfer 推理框架开源发布](https://github.com/deepseek-ai/DeepInfer) ⭐️ 7.0/10

2026 年 10 月 20 日，DeepSeek AI 官方开源了面向自身模型家族的高性能推理框架 DeepInfer，仓库地址为 https://github.com/deepseek-ai/DeepInfer。社区转述的公开信息显示，基于该框架的 DeepSeek V4.1 Flash 单集群服务吞吐达 155 万亿 token/天，单卡非高峰定价下每小时收入为 38 美元。当前公开材料未披露框架的技术架构、实现细节，也未给出官方直接验证的性能基准数据，相关指标来自第三方社区转述。该框架主要面向构建 AI agent 工具链、模型服务 harness 的工程师群体。

hackernews · ggcr · 10月20日 09:08 · [社区讨论](https://news.ycombinator.com/item?id=50163277)

**「为什么重要」** 这是 DeepSeek AI 首次官方开源自有模型专属推理框架，直接填补了其模型生态在官方推理工具链层面的空白，对构建 DeepSeek 模型服务 harness 的工程师有直接参考价值。社区提及的硬件兼容性扩展若落地，可能对现有 AI 推理硬件市场格局产生影响，但该影响尚未得到官方证实。

**「可关注」** 可关注：DeepInfer 作为 DeepSeek 第一方官方推理框架，其硬件兼容性范围、与现有开源推理工具链的集成成本，是构建 DeepSeek 模型服务 harness 的工程师可优先验证的项。

**「评论」** 社区评论存在明显分歧：部分观点认为该开源是 DeepSeek 针对美国相关禁令的战术发布，也有观点认为其支持华为升腾 NPU 的规划可能冲击英伟达在推理硬件市场的垄断地位，还有评论聚焦于开源模型对全球 AI 产业经济模式的长期影响。

**标签**: `#harness`

---

<a id="item-agent-engineer-3"></a>
### [eMudhra 8 枚中间 CA 私钥泄露](https://simonwillison.net/2026/Oct/20/emudhra-certificates/) ⭐️ 7.0/10

2026 年 10 月 20 日曝出 eMudhra 8 枚中间 CA 私钥遭泄露，相关中间 CA 证书链至 Mozilla、微软、苹果、Chrome 根程序信任的根证书，覆盖大量下游信任库。Linux 发行版需更新 ca-certificates 包，Python 生态的 uv 0.13.4、pip 26.2.2、certifi 2026.10.19 已发布含更新证书列表的版本，所有依赖 TLS 校验的软件（包括 AI Agent 工具链）均需完成信任库更新以规避风险。

rss · Simon Willison · 10月20日 23:50

**「为什么重要」** 该事件属于影响主流根程序的高危 PKI 安全事件，已确认需要所有捆绑信任证书列表的软件完成更新；若未及时更新，依赖 TLS 校验的 Agent 工具链存在被伪造证书绕过安全校验的潜在风险。

**「可关注」** 可关注：及时更新本机 ca-certificates 包，以及 Python 生态下的 uv、pip、certifi 至已发布的安全版本，确保 TLS 校验链路可信。

**标签**: `#security`, `#toolchain`, `#certificates`, `#trust-store`, `#python`

---

<a id="item-agent-engineer-4"></a>
### [决策模型做 Eval 实践指南](https://hamel.dev/blog/posts/decision-model-evals/) ⭐️ 7.0/10

2026 年 10 月 20 日发布的实践指南，对比了 Jev 1.13、Perplexity Decider 1.1 27B、Liquid d1/d1-ultra、Cloudflare Clef Flash、OpenAI Decisions \(GPT-6 Luna\)共 6 款决策模型，在 100 条公寓租赁对话 trace 的失败检测任务上的性能与成本表现，给出阈值调优、分数校准的实操方法。实验以人工标注结果为基准，未覆盖延迟维度，默认 0.50 阈值普遍不适用，调优后仅 3 款模型达到 80%精度与召回的最低要求。

rss · Hamel Husain · 10月20日 07:00

**「为什么重要」** 该指南直接面向构建自动化 eval 系统的工程师，填补了决策模型在 eval 场景下的选型、调优方法空白。文中提出的默认阈值陷阱、成本-性能权衡框架、校准方法，都是当前社区实践里缺乏的标准化参考。

**「可关注」** 可关注：用决策模型做 eval 时，需基于自身任务的精度/召回要求调优阈值，不能直接使用默认 0.50 阈值；若需将模型输出作为置信度依据，需额外验证概率校准效果。

**标签**: `#eval`, `#harness`

---

<a id="item-agent-engineer-5"></a>
### [FairStress 公平基准发布](https://huggingface.co/blog/allenai/fairstress) ⭐️ 6.8/10

2026 年 10 月 20 日 Hugging Face Blog 发布 FairStress 公平基准，用于测量 LLM 在高风险决策场景中的人口统计公平性，评估维度覆盖最终决策选择及决策被说服时的稳定性，已集成至 Olmo-eval 评估框架。该基准包含 300 个跨招聘、医疗、信贷等 29 个领域的双候选人决策场景，经身份与对抗前缀变体扩展后形成超 1300 万测试用例，另有基于项目反应理论筛选的 5 万项轻量子集 FairStress-Core，可降低评估算力成本。测试 Olmo、Llama、Qwen、Gemma、Claude、GPT 系列等开源及前沿模型后发现，模型存在反刻板印象过度修正现象：当论据支持少数群体编码候选人时，模型放弃正确决策的概率显著更高，明确身份标签下的平均差距达 9.3 个百分点。当前公开内容存在截断，技术深度有限，且该基准未覆盖基于公平等替代公平性定义。

rss · Hugging Face Blog · 10月20日 16:09

**「为什么重要」** 现有主流公平性基准仅校验最终决策输出的人口统计对称性，FairStress 补充了决策稳定性维度的评估，可暴露隐藏的偏见；但目前仅完成部分模型测试，其对高风险场景实际部署的改进价值尚未得到广泛验证。

**「可关注」** 可关注：若 LLM 公平性评估仅校验最终输出对称性，可能漏掉决策被对抗前缀影响时的隐藏偏差，需补充稳定性维度的测试。

**标签**: `#eval`, `#fairness`, `#benchmark`

---

<a id="item-agent-engineer-6"></a>
### [Allen AI 推出 FairStress](https://allenai.org/blog/fairstress) ⭐️ 6.3/10

2026 年 10 月 20 日，Allen AI 正式发布 LLM 公平性评估基准 FairStress，该基准可揭示大模型在决策解释与辩护环节的群体差异，即便最终决策输出表面公平。当前公开材料仅包含高层概述，未披露技术细节、性能数据或实现指引。该基准面向 LLM 决策公平性评估、agent 可观测性相关的研究者与工程团队。

rss · Allen AI · 10月20日 08:00

**「为什么重要」** 现有 LLM 公平性评估多聚焦最终输出结果，FairStress 补充了决策过程公平性的评估维度，对 agent 可观测性与决策审计场景有参考价值。但当前无公开技术细节，其实际可用性尚未证实。

**「可关注」** 可关注：FairStress 后续公开的技术细节与实现方式，评估其能否接入现有 agent 公平性评估流程。

**标签**: `#eval`, `#observability`

---

<a id="item-agent-engineer-7"></a>
### [llm-public-ai 0.1 发布 支持 Public AI](https://github.com/simonw/llm-public-ai/releases/tag/0.1) ⭐️ 5.8/10

2026 年 10 月 20 日，开发者 simonw 发布 llm-public-ai 0.1 初始版本，该版本为 LLM 工具新增了对 Public AI 托管模型的支持能力。当前无公开的性能数据、额外技术细节或对通用 agent/harness 工作流的影响说明，仅对需接入 Public AI 模型的 LLM 工具用户有直接参考价值。

github · simonw · 10月20日 15:45

**「为什么重要」** 该版本是 llm-public-ai 的首个正式发布，仅拓展了 LLM 工具对 Public AI 托管模型的接入能力，暂未看到对通用 AI 工程工作流的额外价值。

**「可关注」** 可关注：若你使用 LLM 工具且需接入 Public AI 托管模型，可验证该插件是否满足你的接入需求。

**标签**: `#toolchain`, `#llm-plugin`, `#model-integration`

---

<a id="item-agent-engineer-8"></a>
### [Qwen3 8B/27B 低精度量化优化](https://www.reddit.com/r/LocalLLaMA/comments/1xao7kx/improve_qwen3827b_low_quants_by_using_a_prefiller/) ⭐️ 5.5/10

2026 年 10 月 20 日，Reddit 用户/u/magnus-m 分享 ISTA-DASLab 的 Qwen3 量化优化演示：针对 Qwen3 8B/27B 的 NVFP4 低精度量化模型，通过从 SSD 流式加载预填充模型恢复准确率，同时保留低显存占用与快速解码特性。可验证关键细节：上下文长度超过约 4k token 时无速度损耗，对比基线为无预填充模型的同量化方案；当前限制为仅支持 Nvidia Blackwell GPU，发帖人未实际测试，无官方公告、深度技术细节或生产环境性能数据。该方案面向本地部署量化大模型的工程师，尤其是持有 Nvidia Blackwell GPU 的开发者。

reddit · r/LocalLLaMA · /u/magnus-m · 10月20日 10:09

**「为什么重要」** 该方案为低精度量化大模型的精度损失问题提供了新的优化思路，但当前硬件门槛高、无公开实测数据，实际落地价值仍需验证。

**「可关注」** 可关注：NVFP4 量化 Qwen3 模型的精度损失可通过 SSD 流式预填充模型缓解，但该方案目前仅支持 Nvidia Blackwell GPU 且无公开实测数据。

**标签**: `#coding-agent`

---

## AI 日报
{: #sec-ai-daily .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-daily" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-daily-1"></a>
### [ChatGPT Work 餐饮特许经营案例发布](https://openai.com/index/ted-taylor-restaurant) ⭐️ 6.8/10

OpenAI 博客发布客户案例研究：独立运营 Schlotzsky&\#x27;s 与 Cinnabon 的特许经营商使用 ChatGPT Work 后，菜单重定价时间缩短 95%，现金对账时间缩短 94%。其搭建的相关工作流预计可释放约 10 万美元现金流。

rss · OpenAI Blog · 10月20日 10:00

**「为什么重要」** 该案例为 OpenAI 官方发布的实体线下经营场景落地成果，提供了可量化的效率提升指标，可作为同类餐饮经营场景的工作流改造参考。

**「可关注」** 可关注：ChatGPT Work 在餐饮特许经营场景的重复性经营工作流中的效率提升路径。

**标签**: `#product`, `#industry`

---

## AI 羊毛
{: #sec-ai-deals .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-deals" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-deals-1"></a>
### [WorkBuddy 教师公益版开放申领](https://www.appinn.com/workbuddy-education/) ⭐️ 8.0/10

腾讯向全国在职教师发放 WorkBuddy 教育公益版 1 年免费使用权。该 AI 教学助手支持 AI 备课、制作课件、设计作业、家校沟通、学情分析等教学场景，由腾讯 SSV 数字教育实验室与 WorkBuddy 团队联合研发。

rss · 小众软件 · 10月20日 13:57

**「为什么重要」** 该权益为腾讯刚推出的教师专属公益福利，未标注明确截止时间，当前申领即可覆盖全年教学场景的 AI 辅助需求。

**「可关注」** 可关注：该权益仅面向全国在职教师开放，需核验教师身份后方可使用，无其他公开领取渠道。

**标签**: `#student`, `#free-tier`, `#promo`, `#limited-free`

---