---
layout: default
title: "Horizon Summary: 2026-10-21 (EN)"
date: 2026-10-21
lang: en
---

> From 194 items, 13 important content pieces were selected

---

**Agent Harness Architecture**
1. [Think 0.21.0 发布](#item-harness-arch-1) ⭐️ 7.8/10
2. [OpenAI Agents JS 0.21.0](#item-harness-arch-2) ⭐️ 7.3/10
3. [OpenHands v1.29.0 发布](#item-harness-arch-3) ⭐️ 6.8/10

**AI Agent Engineer**
1. [ALTK-Evolve 登 τ²-bench 榜首](#item-agent-engineer-1) ⭐️ 7.8/10
2. [DeepInfer 推理框架开源发布](#item-agent-engineer-2) ⭐️ 7.0/10
3. [eMudhra 中间 CA 私钥泄露](#item-agent-engineer-3) ⭐️ 7.0/10
4. [决策模型用于 Eval 实践指南](#item-agent-engineer-4) ⭐️ 7.0/10
5. [FairStress 发布：LLM 决策公平性评测](#item-agent-engineer-5) ⭐️ 6.8/10
6. [FairStress 基准揭示 LLM 决策公平性](#item-agent-engineer-6) ⭐️ 6.3/10
7. [llm-public-ai 0.1 发布 支持 Public AI](#item-agent-engineer-7) ⭐️ 5.8/10
8. [ISTA-DASLab Qwen3 NVFP4 预填充演示](#item-agent-engineer-8) ⭐️ 5.5/10

**AI Daily**
1. [ChatGPT Work 缩短菜单改价 95% 耗时](#item-ai-daily-1) ⭐️ 6.8/10

**AI Deals**
1. [腾讯WorkBuddy教育公益版向教师发放1 年免费使用权](#item-ai-deals-1) ⭐️ 8.0/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [Think 0.21.0 发布](https://github.com/cloudflare/agents/releases/tag/%40cloudflare/think%400.21.0) ⭐️ 7.8/10

@cloudflare/think 0.21.0 将工作区工具统一为 @cloudflare/computer 的 createAITools，移除 createWorkspaceTools、workspaceBash 及 @cloudflare/think/tools/workspace。workspace 属性改为 @cloudflare/computer 的 Workspace 实例，新增该包为对等依赖。执行工具移除 @cloudflare/shell 依赖及 state 选项；createExecuteTool 与 createExecuteRuntime 废弃，改用 exec 的 ws:tools 模块。聊天恢复在连续 chatRecovery.maxInterruptedAttempts（默认 5）次中断后封存回合，替代 maxOomRetries。

github · github-actions\[bot\] · Oct 20, 15:20

**「设计要点」** 工具层直接复用 @cloudflare/computer 的 Workspace 与 createAITools，@cloudflare/think 不再维护独立工作区实现。新增对等依赖要求宿主项目必须同时安装 @cloudflare/computer。

**「改了什么」** 工作区工具 API 整体迁移至 @cloudflare/computer，遗留入口与 @cloudflare/shell 依赖被清除。执行工具调用改为 exec 的 ws:tools 模块，聊天恢复策略从 OOM 重试改为固定中断次数上限。

**Tags**: `#tools`, `#runtime`, `#dependencies`

---

<a id="item-harness-arch-2"></a>
### [OpenAI Agents JS 0.21.0](https://github.com/openai/openai-agents-js/releases/tag/%40openai/agents-core%400.21.0) ⭐️ 7.3/10

OpenAI Agents JS @openai/agents-core 0.21.0 removes the Runloop sandbox provider as a breaking change and fixes token usage breakdown preservation for streamed runs. The release updates run state schema to 1.23 while maintaining backward compatibility with earlier snapshots.

github · openai-sdks\[bot\] · Oct 20, 22:07

**「Key Design」** The runtime persists bounded nested numeric token usage breakdowns across streamed runs and saved state, requiring explicit narrowing to numbers before arithmetic. Removing the Runloop sandbox provider simplifies the extension model; users migrate via the provided guide.

**「What Changed」** Removed the Runloop sandbox provider and its public API. Fixed token usage accounting to preserve breakdowns across streamed runs and persisted state \(schema 1.23\). Updated sandbox dynamic compaction thresholds to recognize GPT-6 Astra, Sol, Luna, and GPT-6.1 Sol.

**「Community Discussion」** No community comments available.

**Tags**: `#sandbox`, `#runtime`

---

<a id="item-harness-arch-3"></a>
### [OpenHands v1.29.0 发布](https://github.com/OpenHands/OpenHands/releases/tag/v1.29.0) ⭐️ 6.8/10

OpenHands v1.29.0 于 2026-10-20 发布，新增按 agent profile 配置技能、上下文压缩器、验证策略及模型路由选择的能力。后端选择器改为显示完整组织名称，启动器支持从 bundled extensions 包加载公共技能。本次更新包含多项 UI 与体验修复，如浅色主题 git 图标、聊天模型追赶延迟降至 1 秒、云会话仓库关联保存等，未宣布重大架构变更或破坏性更新。

github · openhands-release-bot\[bot\] · Oct 20, 22:22

**「改了什么」** 相对 v1.28.1，新增按 agent profile 配置技能、上下文压缩器、验证策略及模型路由的能力，启动器支持从 bundled extensions 加载公共技能，后端选择器显示完整组织名称。修复涵盖云会话仓库保存、浅色主题图标、聊天模型追赶延迟（1 秒内）、onboarding 流程、LLM 提供者筛选排序，以及将 uvx 锁定至 Python 3.12-3.14。

**Tags**: `#agent-profiles`, `#tools`, `#memory`, `#runtime`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [ALTK-Evolve 登 τ²-bench 榜首](https://huggingface.co/blog/ibm-research/altk-evolve-bc) ⭐️ 7.8/10

IBM Research 2026-10-20 博客介绍 ALTK-Evolve。该方法用 GPT-4.1 在 τ²-bench retail 达到 67.5% Pass^4，登上 2026-10-12 排行榜首位。它不改模型权重，仅将训练轨迹蒸馏成的行为准则追加到 stock ReAct scaffold 的 system prompt。零售 Pass^4 从 57.5% 升至 67.5%，航空 sup3 配置从 35.0% 升至 45.0%；零售 lossless 配置每对话成本增 65%，对话轮数未变。

rss · Hugging Face Blog · Oct 20, 15:19

**「为什么重要」** 这证明 prompt 级 learned memory 可超越微调或前沿模型。Pass^4 与 Mean Accuracy 增长不同步，guideline 剂量需按领域调整。

**「可关注」** 可关注：guideline 的 support count 阈值需按领域单独调整，零售取 lossless、航空取 sup3 时 Pass^4 增益最大。

**Tags**: `#memory`, `#eval`, `#harness`

---

<a id="item-agent-engineer-2"></a>
### [DeepInfer 推理框架开源发布](https://github.com/deepseek-ai/DeepInfer) ⭐️ 7.0/10

2026年10月20日，DeepSeek AI 官方开源面向自身模型家族的高性能推理框架 DeepInfer。社区引用的生产指标显示，该框架支撑 DeepSeek V4.1 Flash 实现单集群 155 万亿 token/天的吞吐量，单卡非高峰定价下每小时收入 38 美元。当前未公开框架完整技术架构与实现细节，直接影响 AI agent 工程师构建模型 harness 与服务工具链的工作。

hackernews · ggcr · Oct 20, 09:08 · [Discussion](https://news.ycombinator.com/item?id=50163277)

**「为什么重要」** 这是 DeepSeek 首次官方开源自有模型推理框架，附带可验证的生产级吞吐与成本指标，为 agent 工程师优化模型服务链路提供了可直接参考的第一方基准。

**「可关注」** 可关注：DeepInfer 已开源支持华为昇腾 950 NPU 的推理代码，若后续补充完整架构文档，可评估其作为非英伟达硬件下 agent 模型服务栈的可行性。

**「评论」** 社区讨论存在多个方向：部分用户引用知乎文章确认框架的生产级吞吐指标；另有用户关联美国 DHS 2026 年 7 月发布的 DeepSeek 相关禁令，推测此次开源是提前筹备的 timed 发布；还有用户关注其对华为昇腾硬件的支持，认为可能冲击英伟达在推理硬件市场的垄断地位。

**Tags**: `#harness`

---

<a id="item-agent-engineer-3"></a>
### [eMudhra 中间 CA 私钥泄露](https://simonwillison.net/2026/Oct/20/emudhra-certificates/) ⭐️ 7.0/10

2026-10-20，eMudhra 八枚中间 CA 私钥遭泄露，其证书链至 Mozilla、Microsoft、Apple、Chrome 根程序信任的根证书。所有捆绑信任证书列表的软件需更新信任库。Linux 发行版需更新 ca-certificates 包；Python 工具链中 uv 0.13.4、pip 26.2.2、certifi 2026.10.19 已发布含升级证书列表的版本。该事件污染了主流平台与开发工具链的 TLS 信任根。

rss · Simon Willison · Oct 20, 23:50

**「为什么重要」** 这是 PKI 基础设施层面的严重事件，根证书信任链被污染，影响范围覆盖主流操作系统与开发工具。对依赖 TLS 校验的 agent 工具链而言，存在中间人攻击风险，需立即响应。

**「可关注」** 可关注：立即升级 uv、pip、certifi 及系统 ca-certificates，并确认 agent 运行时实际加载的信任库已纳入补丁，避免继续使用受污染证书链。

**Tags**: `#security`, `#toolchain`, `#certificates`, `#trust-store`, `#python`

---

<a id="item-agent-engineer-4"></a>
### [决策模型用于 Eval 实践指南](https://hamel.dev/blog/posts/decision-model-evals/) ⭐️ 7.0/10

2026-10-20 发布实践指南，对比 Jev 1.13、Perplexity Decider 1.1 27B、Liquid d1/d1-ultra、Cloudflare Clef Flash、OpenAI Decisions \(GPT-6 Luna\) 等决策模型作为 LLM judge 的低成本替代方案。基于 100 条公寓租赁 agent 轨迹的二元 pass/fail 测试，发现默认 0.50 阈值常导致次优性能，需按任务调优。调优后 OpenAI Decisions 达到 F1 0.87，成本 3.72 美分/100 次；Perplexity Decider 成本 0.82 美分/100 次，F1 0.79。概率校准显示模型分数作为置信度估计时需谨慎，实验未提供延迟数据。

rss · Hamel Husain · Oct 20, 07:00

**「为什么重要」** 该指南提供可复用的阈值调优 prompt 和成本-性能对比基线，直接服务于 eval harness 工程师的工具选型。但结论基于单一租赁场景的 100 条轨迹，泛化性未验证。

**「可关注」** 可关注：二元 pass/fail 标签比细粒度评分更易对齐人类偏好，且决策模型阈值需通过分层五折交叉验证在训练集上调优，而非直接使用默认 0.50。

**Tags**: `#eval`, `#harness`

---

<a id="item-agent-engineer-5"></a>
### [FairStress 发布：LLM 决策公平性评测](https://huggingface.co/blog/allenai/fairstress) ⭐️ 6.8/10

Hugging Face Blog 2026-10-20 发布 FairStress 公平性基准，测量 LLM 在高风险决策中的 demographic 公平性，超越仅看最终选择的传统方法。该基准含 300 个双候选人场景，覆盖 29 个领域，通过对抗性前缀测试决策稳定性，已集成 Olmo-eval。实验覆盖 15 个模型（Olmo、Llama、Qwen、Gemma、Claude、GPT 系列等）。无身份信息时模型选择几乎对称；但当论据支持少数群体编码候选人时，模型更易放弃证据更强的选择，明确身份条件下平均差距 9.3 个百分点。原文内容截断，技术深度受限。

rss · Hugging Face Blog · Oct 20, 16:09

**「为什么重要」** 该基准揭示的 &quot;反刻板印象过度纠正&quot; 现象表明，demographic 信息显性化时模型对证据的遵循度出现系统性偏差，直接影响招聘、信贷、医疗等高风险自动化决策的可靠性。测试覆盖从隐式到显式的身份呈现梯度，可验证现有对齐策略是否在不同显性度下产生非预期反转。

**「可关注」** 可关注：对抗性前缀与 demographic 编码的组合测试显示，模型在明确身份条件下的决策稳定性显著弱于无身份信息场景，当前公平性优化可能引入对少数群体候选人的非对称宽容，证据遵循度与群体对称性存在张力。

**Tags**: `#eval`, `#fairness`, `#benchmark`

---

<a id="item-agent-engineer-6"></a>
### [FairStress 基准揭示 LLM 决策公平性](https://allenai.org/blog/fairstress) ⭐️ 6.3/10

Allen AI 于 2026-10-20 发布 FairStress 基准。该基准测试揭示 LLM 在辩护和解释决策时存在人口统计差异，即使最终选择看似公平。当前仅公开高层概述，未提供技术细节、性能数据或实施指导。影响范围涵盖 LLM 公平性评估、agent 评估及可观测性工作流。

rss · Allen AI · Oct 20, 08:00

**「为什么重要」** 该基准将公平性评估从最终输出扩展到决策解释层，为检测隐性偏差提供新维度。对需要审计决策过程的 agent 系统尤其相关。

**「可关注」** 可关注：现有 eval 流程若仅校验最终输出，可能遗漏决策解释层的人口统计偏差。

**Tags**: `#eval`, `#observability`

---

<a id="item-agent-engineer-7"></a>
### [llm-public-ai 0.1 发布 支持 Public AI](https://github.com/simonw/llm-public-ai/releases/tag/0.1) ⭐️ 5.8/10

2026年10月20日，开发者simonw发布\`llm-public-ai\` 0.1初始版本，该版本为LLM工具新增了对Public AI托管模型的接入支持。当前仅公开了初始发布的核心信息，未披露具体适配细节、性能数据或兼容范围。该更新仅对使用LLM工具链且需接入Public AI模型的工程师有直接参考价值。

github · simonw · Oct 20, 15:45

**「为什么重要」** 该版本是\`llm-public-ai\`的首次正式发布，填补了LLM工具链接入Public AI托管模型的官方插件空白，但当前公开信息有限，暂未体现对更广泛agent/harness/评测工作流的影响。

**「可关注」** 可关注：若你正在使用LLM工具链且需接入Public AI托管模型，可验证该插件的基础调用兼容性。

**Tags**: `#toolchain`, `#llm-plugin`, `#model-integration`

---

<a id="item-agent-engineer-8"></a>
### [ISTA-DASLab Qwen3 NVFP4 预填充演示](https://www.reddit.com/r/LocalLLaMA/comments/1xao7kx/improve_qwen3827b_low_quants_by_using_a_prefiller/) ⭐️ 5.5/10

2026年10月20日，Reddit用户/u/magnus-m分享了ISTA-DASLab的推理优化演示，该方案通过从SSD流式加载NVFP4量化的Qwen3 8B/27B预填充模型，在保持低显存占用与快速解码的同时恢复低精度量化模型的准确率。该方案仅支持Nvidia Blackwell GPU，分享者未实际测试；演示数据显示上下文长度超过约4k token时无额外速度损失，性能以MMLU-Pro准确率为基准。

reddit · r/LocalLLaMA · /u/magnus-m · Oct 20, 10:09

**「为什么重要」** 该方案为本地量化大模型推理提供了新的优化思路，对低资源环境部署coding agent有潜在参考价值。但当前仅支持小众的Nvidia Blackwell GPU，无官方公告与生产级性能数据，实际落地效果尚未验证。

**「可关注」** 可关注NVFP4量化模型搭配SSD流式预填充的推理优化路径，但需注意当前方案硬件兼容性有限，尚无生产环境验证数据。

**Tags**: `#coding-agent`

---

## AI Daily

<a id="item-ai-daily-1"></a>
### [ChatGPT Work 缩短菜单改价 95% 耗时](https://openai.com/index/ted-taylor-restaurant) ⭐️ 6.8/10

OpenAI 官方博客发布案例研究，独立运营的 Schlotzsky&\#x27;s 与 Cinnabon 加盟商使用 ChatGPT Work 后，菜单改价耗时缩短 95%，搭建的工作流预计可释放约 10 万美元现金流。

rss · OpenAI Blog · Oct 20, 10:00

**「为什么重要」** 该案例为 OpenAI 官方发布的真实中小商家落地实践，给出了 ChatGPT Work 在餐饮运营场景下的具体降本数据，可参考其实际落地效果。

**Tags**: `#product`, `#industry`

---

## AI Deals

<a id="item-ai-deals-1"></a>
### [腾讯WorkBuddy教育公益版向教师发放1 年免费使用权](https://www.appinn.com/workbuddy-education/) ⭐️ 8.0/10

10月19日，腾讯正式发布WorkBuddy教育公益版，面向全国在职教师发放1 年免费使用权，可支持AI备课、制作课件、设计作业、家校沟通、学情分析等教学场景。

rss · 小众软件 · Oct 20, 13:57

**「可关注」** 可关注：全国在职教师可申领WorkBuddy教育公益版1 年免费使用权，该产品由腾讯SSV数字教育实验室与WorkBuddy团队联合研发，预置多类教学场景。

**Tags**: `#student`, `#free-tier`, `#promo`, `#limited-free`

---