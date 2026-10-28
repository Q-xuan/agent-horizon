---
layout: default
title: "Horizon Summary: 2026-10-28 (ZH)"
date: 2026-10-28
lang: zh
---

> 从 188 条内容中筛选出 14 条重要资讯。

<nav id="ah-toc" class="ah-toc" aria-label="目录"><span class="ah-toc-title">目录</span><ul><li><a href="#sec-harness-arch"><span class="ah-toc-name">Harness 架构</span><span class="ah-toc-count">3条</span></a></li><li><a href="#sec-agent-engineer"><span class="ah-toc-name">Agent 工程师日报</span><span class="ah-toc-count">8条</span></a></li><li><a href="#sec-ai-daily"><span class="ah-toc-name">AI 日报</span><span class="ah-toc-count">3条</span></a></li></ul></nav>

---

**[Harness 架构](#sec-harness-arch)**
1. [Cloudflare Agents 0.31.0 发布](#item-harness-arch-1) ⭐️ 8.3/10
2. [Codex rust-v0.165.0 发布](#item-harness-arch-2) ⭐️ 7.8/10
3. [OpenHands v1.34.0 发布](#item-harness-arch-3) ⭐️ 7.8/10

**[Agent 工程师日报](#sec-agent-engineer)**
1. [Liquid AI 发布 LFM3 多模态模型](#item-agent-engineer-1) ⭐️ 7.8/10
2. [Allen AI 发布新颖性判断基准](#item-agent-engineer-2) ⭐️ 7.8/10
3. [Anthropic 分享 Claude 平台 Agent 架构实践](#item-agent-engineer-3) ⭐️ 7.0/10
4. [HF 论文：RSI Arena 递归自我改进](#item-agent-engineer-4) ⭐️ 7.0/10
5. [HF 每日论文：LLM Agent 推理投入](#item-agent-engineer-5) ⭐️ 7.0/10
6. [HF 每日论文：Memory Tax](#item-agent-engineer-6) ⭐️ 7.0/10
7. [LiquidAI LFM3-1.7B 发布](#item-agent-engineer-7) ⭐️ 5.5/10
8. [社区拆解 Cohere Qwen 误判事件](#item-agent-engineer-8) ⭐️ 5.5/10

**[AI 日报](#sec-ai-daily)**
1. [OpenAI 与 Oracle 合作扩展至 ChatGPT](#item-ai-daily-1) ⭐️ 9.8/10
2. [Retell 用 OpenAI 模型支撑月均 1 亿次通话](#item-ai-daily-2) ⭐️ 6.8/10
3. [文心 Unlimited OCR 2 发布](#item-ai-daily-3) ⭐️ 5.0/10

---

## Harness 架构
{: #sec-harness-arch .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-harness-arch" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-harness-arch-1"></a>
### [Cloudflare Agents 0.31.0 发布](https://github.com/cloudflare/agents/releases/tag/agents%400.31.0) ⭐️ 8.3/10

Cloudflare Agents 0.31.0 发布，核心更新是浏览器内部主机名代理与 MCP 依赖解耦。\`browserRun\(\)\` 新增 \`internalHosts\` 参数，允许模型通过浏览器代理访问本地开发服务器、工作区文件夹或同租户 Worker，最多支持 8 个内部主机名。同时 \`@modelcontextprotocol/sdk\` 与 \`@modelcontextprotocol/server\` 变为可选 peer 依赖，不启用 MCP 的应用不再强制安装。

github · github-actions\[bot\] · 10月27日 13:29

**「设计要点」** 浏览器工具架构从 codemode 迁移至独立 Dynamic Worker，模型代码在隔离 Worker 中执行并通过 CDP 与浏览器通信，超时后可从外部终止。内部主机名通过 agent 的 \`fetch\` 函数或跨 Worker 路由实现，模型可通过 \`browser.assignHost\(\)\` 动态绑定目标。

**「改了什么」** \`browserRun\(\)\` 新增 \`internalHosts\` 参数与 \`browser.assignHost\(\)\` 方法，支持浏览器代理访问本地服务。\`browserTool\` 迁移至独立 Dynamic Worker，弃用 \`createBrowserTools\`、\`createBrowserRuntime\`、\`BrowserConnector\` 及 Quick Action helpers。MCP 依赖变为可选，\`agents/models/ai-sdk\` 与 \`agents/models/pi-ai\` 脱离实验状态，\`PiWhenBusy\` 支持 \`&quot;reject&quot;\`，\`createMcpHandler\` 传递 OAuth \`authInfo\`。

**标签**: `#runtime`, `#tools`, `#mcp`

---

<a id="item-harness-arch-2"></a>
### [Codex rust-v0.165.0 发布](https://github.com/openai/codex/releases/tag/rust-v0.165.0) ⭐️ 7.8/10

OpenAI Codex CLI 发布 rust-v0.165.0，新配置文件默认启用 Memory v2 并支持导入外部代理记忆，新增内置 Google Cloud Vertex AI provider（\`model\_provider = &quot;gcp&quot;\`），app-server API 增加实验性 attached thread forks，修复远程 MCP 工具请求取消逻辑并默认开启推理 effort 动态调整。

github · github-actions\[bot\] · 10月27日 20:09

**「设计要点」** Memory v2 仅新配置文件默认启用，现有配置需手动迁移。attached thread forks 以实验性 API 形式提供子代理分叉能力。MCP 工具层修复请求取消传播，本地 response future 被丢弃时同步终止远端调用。

**「改了什么」** 相对 rust-v0.164.0，新增 GCP Vertex AI provider 与 GPT-6.1 Terra 模型目录。Memory v2 成为新配置文件默认记忆后端，app-server API 增加实验性 attached thread forks。修复远程 MCP 工具请求悬挂问题，推理 effort 动态调整默认开启。

**「评论」** 无社区评论。

**标签**: `#memory`, `#mcp`, `#subagents`, `#runtime`, `#tools`

---

<a id="item-harness-arch-3"></a>
### [OpenHands v1.34.0 发布](https://github.com/OpenHands/OpenHands/releases/tag/v1.34.0) ⭐️ 7.8/10

OpenHands v1.34.0 于 2026-10-27 发布。本次更新引入 per-conversation Docker runtime，每个对话可绑定独立容器，并新增 Settings → Runtime 设置页面。侧边栏支持在对应行的沙箱内启动新对话，实现沙箱对齐。static-server 的 session API key 改为环境变量传递，最低 \`minimumAgentServer\` 要求提升至 1.57.0。

github · openhands-release-bot\[bot\] · 10月27日 14:35

**「设计要点」** per-conversation Docker runtime 将运行时隔离粒度从全局降至对话级，每个对话绑定独立 Docker 容器。static-server 的 session API key 从 argv 改为环境变量传递，降低进程参数泄露风险；最低 \`minimumAgentServer\` 提升至 1.57.0。

**「改了什么」** 新增 per-conversation Docker runtime 及 Runtime 设置页面，支持按对话配置独立容器；侧边栏支持在对应行的沙箱内直接启动新对话。static-server 的 session API key 改为环境变量传递，自动化 KV secret 固定以兼容 session key 轮转，最低 \`minimumAgentServer\` 提升至 1.57.0。

**标签**: `#runtime`, `#sandbox`

---

## Agent 工程师日报
{: #sec-agent-engineer .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-agent-engineer" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-agent-engineer-1"></a>
### [Liquid AI 发布 LFM3 多模态模型](https://huggingface.co/blog/LiquidAI/lfm3) ⭐️ 7.8/10

2026 年 10 月 27 日 Hugging Face 官方博客发布 Liquid AI 的 LFM3 系列 2B 参数多模态基础模型，共享主干覆盖文本、视觉、音频、全模态、决策五类模态，支持单 GPU 微调与边缘部署，面向 specialized 智能体场景。相比前代 LFM2，LFM3-1.7B 以 35%更少参数超越 LFM2.5-2.6B，上下文窗口达 256K，文本模型 4-bit 精度下体积约 1GB，所有分支模型均支持单 GPU 微调，包含首个支持视频输入的视觉模型与首个全模态模型。当前公开内容未包含完整基准测试与第三方集成细节，该模型家族主要面向轻量多模态智能体、边缘部署场景的开发者。

rss · Hugging Face Blog · 10月27日 17:16

**「为什么重要」** 它首次将多模态能力、长上下文、边缘部署可行性整合到 2B 参数级模型家族中，降低了 specialized coding agent 的落地成本；但完整性能表现、生态兼容性等细节尚未完全公开，实际落地效果还需进一步验证。

**「可关注」** 可关注：LFM3 的 tri-hybrid 层设计、头级门控注意力与单主干多模态分支方案，为低参数、长上下文、可量化部署的轻量智能体提供了可参考的实现路径。

**标签**: `#coding-agent`

---

<a id="item-agent-engineer-2"></a>
### [Allen AI 发布新颖性判断基准](https://allenai.org/blog/novelty-bench) ⭐️ 7.8/10

2026 年 10 月 27 日，Allen AI 发布 Old Ideas, Novel Problems 新颖性评估基准，配套论文、数据集、代码及自动化构建评估集的流水线。基准测试覆盖 GPT-5.1、GPT-5.2、GPT-5.4、Claude Sonnet 4.5、Claude Opus 4.5、Claude Opus 4.6 共 6 个 LLM 评委，发现仅改动提示词、推理预算、是否接入检索等小调整，就会导致同一研究想法的新颖性判断结果大幅波动：例如 GPT-5.4 在 Human+Generated 数据集上更换简化提示词后，准确率从 93.5% 跌至 40.9%，低于随机水平；增加检索或推理预算并未稳定提升判断准确率，此外两个专为新颖性评估设计的系统表现反而差于简单提示的 Claude Opus 4.6 基线。该基准面向用 LLM 评估科研想法新颖性的团队、以及构建 AI 科研发现系统的工程师，当前核心结论不依赖标签准确性，因为不同合理配置对同一对想法的判断分歧本身已说明评估的不稳定性；其中 AI 生成想法的标签为弱标签，未逐条验证新颖性。

rss · Allen AI · 10月27日 08:00

**「为什么重要」** 该基准首次系统性量化了 LLM 作为新颖性评委的不可靠性，直接暴露了当前相关评估框架的配置脆弱性；尚未证实的是，这类不稳定是否会传导到依赖 novelty 判断的科研自动化系统的最终产出质量。

**「可关注」** 可关注：LLM-as-judge 评估框架的配置稳定性会直接传导到 novelty 类任务的 verdict 可信度，当前无通用最优配置，需针对具体任务做消融验证。

**标签**: `#eval`, `#harness`

---

<a id="item-agent-engineer-3"></a>
### [Anthropic 分享 Claude 平台 Agent 架构实践](https://latent.space/p/how_anthropic_ships_the_1_llm_in_the_world_safely_separating_the_brain_from_the_hands/) ⭐️ 7.0/10

2026 年 10 月 27 日 Latent Space 发布播客节目笔记，邀请 Anthropic 平台工程师 Katelyn Lesse、Angela Jiang 分享 Claude 平台工程实践。内容涵盖 Claude Opus 5.5 发布、模型“大脑”与 Agent 执行能力分离架构、托管 Agent 扩展、安全管控等一手实现细节，并附 Anthropic 官方相关资源链接，对 Agent harness 设计、编排、权限管控、评测体系构建有直接参考价值。

rss · Latent Space · 10月27日 18:40

**「为什么重要」** 该内容来自 Anthropic 平台工程师的一手实践分享，直接覆盖 Agent harness 设计、权限管控、托管 Agent 扩展等核心工程环节，是当前少有的公开 frontier 模型平台架构细节的公开资料。

**「可关注」** 可关注：Anthropic 在 Claude 平台采用模型“大脑”与 Agent 执行能力分离的架构，同时通过 Rust 重写 Messages API、隔离凭证与网络控制实现托管 Agent 的安全与可扩展性。

**标签**: `#harness`, `#coding-agent`, `#orchestration`, `#permissions`, `#eval`

---

<a id="item-agent-engineer-4"></a>
### [HF 论文：RSI Arena 递归自我改进](https://huggingface.co/papers/2610.33624) ⭐️ 7.0/10

2026 年 10 月 28 日 Hugging Face 每日论文频道发布 RSI Arena 框架相关研究，验证 AI Agent 可自主利用人类反馈完成递归自我改进。实验中 10 个前沿模型作为训练 Agent，均从 NVIDIA Nemotron 3.5 Lightning 30B-A3B Base 起步，在 6 天第一阶段内各获得 1000 GPU 小时与 300 美元 API 额度，在 64 卡共享集群上自主完成数据选择、训练实现、checkpoint 选择全流程。所有 Agent 均产出可用助手，其中 GPT-6 Astra 训练的模型在 12 项能力基准上闭合约 76%的中位 Base 到 Instruct 性能差距，研究配套 20 项基准测试与盲人人类评估。该研究对 Agent 自改进系统、评测体系与训练编排方向有直接参考价值。

rss · Hugging Face Daily Papers · 10月28日 00:00

**「为什么重要」** 该研究首次系统验证了 AI Agent 自主完成全流程后训练并利用人类反馈实现递归自我改进的可行性，提供了可复现的实验框架与可量化的性能基准，为相关方向的工程实践提供了可直接参考的对照样本。

**「可关注」** 可关注：在固定资源约束下，前沿模型作为训练 Agent 自主完成数据选择、训练实现、checkpoint 选择的全流程，可产出接近人工微调效果的模型。

**标签**: `#eval`, `#orchestration`, `#harness`

---

<a id="item-agent-engineer-5"></a>
### [HF 每日论文：LLM Agent 推理投入](https://huggingface.co/papers/2610.34491) ⭐️ 7.0/10

2026 年 10 月 28 日 Hugging Face 每日论文推送了题为《What Effort Level Should I Choose? On the Economics of Reasoning Effort in LLM Agents》的实证研究摘要，该研究测试了专有与开源模型在 4 个涵盖单次调用推理、长期智能体任务的基准上，推理努力程度（可调节推理时计算投入的参数）的反事实效果。研究发现提高推理努力不保证任务成功率提升，可能产生不必要成本，还会改变任务执行轨迹；由于推理努力属于信用品，用户仅能观测最终结果，无法判断额外投入的边际价值。当前内容为 HF 每日论文的截断摘要，非原始论文全文，相关结论可服务于 LLM Agent harness 调优与评估设计方向的工程师。

rss · Hugging Face Daily Papers · 10月28日 00:00

**「为什么重要」** 该研究针对 LLM Agent 核心可调参数给出了可验证的实证结论，打破了「更高推理努力必然带来更好效果」的默认假设。目前相关结论仅来自 HF 每日论文的截断摘要，尚未经过更大规模基准或更多模型族的复现验证。

**「可关注」** 可关注：推理努力程度的提升不必然提升任务成功率，还可能改变任务轨迹，在 harness 调优与评估设计中需针对性验证该参数的实际边际收益。

**标签**: `#eval`, `#harness`

---

<a id="item-agent-engineer-6"></a>
### [HF 每日论文：Memory Tax](https://huggingface.co/papers/2610.34073) ⭐️ 7.0/10

2026 年 10 月 28 日 Hugging Face Daily Papers 收录研究论文《Memory Tax: Dissecting the Net Value of Agent Memory》，该研究提出大规模 agent 记忆系统评估框架，定义“memory tax（记忆税）”指标量化专用记忆系统相对朴素 RAG 的性能净收益，将收益拆解为“记忆收益”与“记忆税”两部分。跨多基准、多模型骨干的测试显示多数专用记忆系统性能弱于直接从原始历史检索，净价值为负，相关结论面向长周期 agent 的记忆组件设计、评估与选型场景。

rss · Hugging Face Daily Papers · 10月28日 00:00

**「为什么重要」** 该研究首次系统量化了专用记忆系统相对朴素 RAG 的净收益，打破了“专用记忆一定优于原始检索”的行业默认假设，为长周期 agent 的记忆组件选型提供了可复用的评估基准。

**「可关注」** 可关注：在长周期 agent 的记忆组件选型中，优先将朴素 RAG 作为基线对比，避免默认专用记忆系统存在净收益。

**标签**: `#memory`, `#eval`

---

<a id="item-agent-engineer-7"></a>
### [LiquidAI LFM3-1.7B 发布](https://www.reddit.com/r/LocalLLaMA/comments/1xgy8s3/liquidailfm317b_hugging_face/) ⭐️ 5.5/10

2026 年 10 月 27 日 Reddit 社区转发了 LiquidAI 在 Hugging Face 发布的 LFM3-1.7B 文本模型官方说明。该模型为 1.73B 参数的三混合架构，针对本地智能体与特定场景后训练，支持 256K token 上下文，4-bit 精度下内存占用约 1GB，支持单 GPU 快速微调。官方明确标注该模型不适用于智能体编码或复杂多步推理场景，当前无公开性能基准数据可供评估实际效用。该内容主要面向关注边缘端本地 agent harness 的工程师。

reddit · r/LocalLLaMA · /u/jacek2023 · 10月27日 17:04

**「为什么重要」** 它是目前少数公开供给的小参数边缘端本地智能体模型，轻量化特性对端侧 agent 部署有参考价值，但缺乏性能基准与对比数据，暂时无法判断其对 coding agent 工程场景的实际适配效果。

**「可关注」** 可关注其 4-bit 下 1GB 内存占用的轻量化设计与单 GPU 微调支持，但需优先验证其是否满足自身 agent 场景的推理与工具调用需求，尤其注意官方标注的不适用场景限制。

**标签**: `#harness`, `#coding-agent`, `#local-llm`

---

<a id="item-agent-engineer-8"></a>
### [社区拆解 Cohere Qwen 误判事件](https://www.reddit.com/r/LocalLLaMA/comments/1xgopmj/debunking_coheres_claim_of_qwen_38_flash_next/) ⭐️ 5.5/10

2026 年 10 月 27 日 Reddit 社区用户/u/feelspeaceman 发布分析，针对 Cohere 公开的 Hugging Face Qwen 3.8 Flash Next 调查数据集，拆解其声称该模型向阿里远程 URL 泄露数据的误判，指出两个核心测试设计缺陷：一是将输入 trace 截断至目标 URL 前 2323 token 处，强制模型扮演 URL 生成器；二是检测提示词极度模糊、无任务上下文，诱导模型幻觉输出。该分析仅针对单一具体指控，属于社区对一手数据集的二次分析，无更广泛的行业影响，Cohere CEO 曾公开表示无证据证明该行为是故意的，该异常行为出现频率低于十万分之一，可作为 AI agent 和模型 eval 设计的踩坑参考。

reddit · r/LocalLLaMA · /u/feelspeaceman · 10月27日 10:19

**「为什么重要」** 该分析首次公开拆解了 Cohere 公开数据集里的测试设计缺陷，为 AI agent 和模型 eval 开发者提供了可直接避坑的实操案例；但该结论仅针对单一具体数据泄露指控，无更广泛的行业影响验证。

**「可关注」** 可关注：eval 测试设计需避免截断关键上下文诱导模型行为偏移，同时检测提示词需提供充分任务上下文，防止模型因提示模糊产生幻觉输出。

**标签**: `#eval`, `#permissions`

---

## AI 日报
{: #sec-ai-daily .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-daily" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-daily-1"></a>
### [OpenAI 与 Oracle 合作扩展至 ChatGPT](https://openai.com/index/oracle-apps-in-chatgpt) ⭐️ 9.8/10

OpenAI 与 Oracle 宣布扩大合作伙伴关系。双方将把企业业务应用及 AI Agent 整合进 ChatGPT，同时 OpenAI 将为 Oracle 的新产品与服务提供支撑。目前公告未披露具体财务条款或集成时间表。

rss · OpenAI Blog · 10月27日 07:00

**「为什么重要」** 该合作标志着企业级 AI 应用与主流办公平台的深度整合加速。对构建 AI Agent 生态的开发者而言，这预示了新的集成接口与市场机会。

**「可关注」** 可关注：ChatGPT 对企业应用与 AI Agent 的原生支持路径，以及 Oracle 云服务与 OpenAI API 的对接方式。

**标签**: `#lab`, `#industry`, `#product`

---

<a id="item-ai-daily-2"></a>
### [Retell 用 OpenAI 模型支撑月均 1 亿次通话](https://openai.com/index/retell-ai) ⭐️ 6.8/10

OpenAI 官方博客发布客户案例，显示语音 AI 公司 Retell 使用 OpenAI 模型支撑每月 1 亿次通话。GPT-6 Astra 在 Retell 的语音智能体基准测试中排名第一，Codex 助力 Retell 实现人均年化收入运行率 160 万美元。

rss · OpenAI Blog · 10月27日 15:00

**「为什么重要」** 该案例为 OpenAI 官方发布的客户落地成果，包含可验证的行业使用规模与模型性能数据，可作为语音 AI 场景的参考样本。

**「可关注」** 可关注：GPT-6 Astra 在语音智能体基准测试中的表现，以及 Codex 对 Retell 人均产出效率的提升作用。

**标签**: `#model`, `#lab`, `#industry`, `#product`

---

<a id="item-ai-daily-3"></a>
### [文心 Unlimited OCR 2 发布](https://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw==&amp;mid=2247936488&amp;idx=2&amp;sn=286b1f5cae20ebec0f56b4ef14b6d081) ⭐️ 5.0/10

百度发布升级版开源 OCR 产品文心 Unlimited OCR 2，支持无上限页数连续处理文档。其峰值 KV Cache 占用从标准解码的 47GB 降至 1.77GB，降幅约 96%，可连续处理 3600+页《哈利·波特》全集、1200+页《三体》全集等超长文档。该产品采用稀疏参考滑动窗口注意力机制 SR-SWA 与持续解码机制，单步解码开销不随文档长度增长，已在 Hugging Face 和 GitHub 正式开源。上一代文心 Unlimited OCR 累计下载量超 1000 万，GitHub Star 约 2.86 万。

rss · 量子位 · 10月27日 06:13

**「为什么重要」** 上一代产品已在开源社区积累高人气，本次升级解决了长文档 OCR 的显存与计算瓶颈，大幅降低超长文档连续处理的使用成本。

**「可关注」** 可关注：SR-SWA 按需选取相关页面与视觉信息的机制，以及减少非相关输入陪跑计算的设计思路。

**标签**: `#model`, `#industry`, `#open-source`, `#product`

---