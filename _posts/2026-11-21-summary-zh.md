---
layout: default
title: "Horizon Summary: 2026-11-21 (ZH)"
date: 2026-11-21
lang: zh
---

> 从 181 条内容中筛选出 14 条重要资讯。

<nav id="ah-toc" class="ah-toc" aria-label="目录"><span class="ah-toc-title">目录</span><ul><li><a href="#sec-harness-arch"><span class="ah-toc-name">Harness 架构</span><span class="ah-toc-count">3条</span></a></li><li><a href="#sec-agent-engineer"><span class="ah-toc-name">Agent 工程师日报</span><span class="ah-toc-count">6条</span></a></li><li><a href="#sec-ai-daily"><span class="ah-toc-name">AI 日报</span><span class="ah-toc-count">2条</span></a></li><li><a href="#sec-ai-deals"><span class="ah-toc-name">AI 羊毛</span><span class="ah-toc-count">3条</span></a></li></ul></nav>

---

**[Harness 架构](#sec-harness-arch)**
1. [agents@0.34.0 发布](#item-harness-arch-1) ⭐️ 8.8/10
2. [openai-agents-python v1.0.0-alpha.1 发布](#item-harness-arch-2) ⭐️ 7.8/10
3. [browser-use 1.0.8rc1 发布](#item-harness-arch-3) ⭐️ 5.5/10

**[Agent 工程师日报](#sec-agent-engineer)**
1. [LLM 自改权重论文引争议](#item-agent-engineer-1) ⭐️ 7.0/10
2. [Inkling 2 Mini 开源发布](#item-agent-engineer-2) ⭐️ 7.0/10
3. [TuringSpace 交互式 CAPTCHA 基准发布](#item-agent-engineer-3) ⭐️ 7.0/10
4. [Fragments 11-20：代码质量影响 Agent 成本](#item-agent-engineer-4) ⭐️ 7.0/10
5. [AltRA-Test 提出无共享标注者 LLM 评判验证](#item-agent-engineer-5) ⭐️ 6.0/10
6. [ZeroVLN 免微调 VLM 导航框架提出](#item-agent-engineer-6) ⭐️ 5.5/10

**[AI 日报](#sec-ai-daily)**
1. [OpenAI 公布对抗性蒸馏分层防御方案](#item-ai-daily-1) ⭐️ 6.8/10
2. [上海 AI Lab 开源 Sage S2.1 Flash 技术报告](#item-ai-daily-2) ⭐️ 5.5/10

**[AI 羊毛](#sec-ai-deals)**
1. [Epic 本周免费领两款游戏](#item-ai-deals-1) ⭐️ 8.0/10
2. [波波小红书获客助手 送 30 天激活码](#item-ai-deals-2) ⭐️ 8.0/10
3. [Ferry 免费 iOS 远程桌面发布](#item-ai-deals-3) ⭐️ 7.0/10

---

## Harness 架构
{: #sec-harness-arch .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-harness-arch" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-harness-arch-1"></a>
### [agents@0.34.0 发布](https://github.com/cloudflare/agents/releases/tag/agents%400.34.0) ⭐️ 8.8/10

agents@0.34.0 发布，核心升级至 Pi 1.6 运行时。Pi harness 与 pi-ai 模型层支持工具挂起等待、子 agent 通知唤醒、从历史记录初始化会话。MCP 客户端增加重新授权错误类型，失败请求默认不再向客户端暴露错误详情，需通过 \`onFetchError\` 显式处理。

github · github-actions\[bot\] · 11月20日 15:56

**「设计要点」** Pi 1.6 运行时引入 park/wait 原语，使 agent 能在工具等待外部信号时释放执行上下文，通过 \`harness.signal\(\)\` 和 \`notify\` 参数实现跨会话协调。MCP 客户端将授权失败与网络错误分离，\`onFetchError\` 钩子把错误响应定制权交还应用层。

**「改了什么」** Pi 1.6 支持工具非阻塞等待与子 agent 协调，\`harness.signal\(\)\` 替代旧信号发送方式，\`submit\(\)\` 与 \`continue\(\)\` 新增 \`notify\` 与 \`onAbort: &quot;keep&quot;\` 参数，会话可通过 \`init\` 从历史记录创建。MCP 客户端抛出 \`MCPAuthorizationRequiredError\` 处理重新授权，失败请求默认返回通用 500 或 WebSocket 1011，需显式实现 \`onFetchError\` 保留旧错误详情；Pi 1.5 不再支持且无法回滚。

**标签**: `#runtime`, `#tools`, `#mcp`, `#subagents`

---

<a id="item-harness-arch-2"></a>
### [openai-agents-python v1.0.0-alpha.1 发布](https://github.com/openai/openai-agents-python/releases/tag/v1.0.0-alpha.1) ⭐️ 7.8/10

openai-agents-python 发布 v1.0.0-alpha.1，将 Codex 作为可选模型提供商嵌入 Python SDK。通过 PyO3 直接嵌入 Codex Core rust-v0.166.0，消除 JSON-RPC app-server 层开销。支持按运行选择 CodexProvider，复用 ThreadManager，使用 SDK sessions 管理历史。wheel 仅通过 GitHub Releases 分发，支持 CPython 3.10-3.14。

github · markstuart-oai · 11月20日 20:51

**「设计要点」** 运行时通过 PyO3 将 Rust 版 Codex Core 直接嵌入 CPython 进程，跳过 app-server 和 JSON-RPC。Provider 复用单一 ThreadManager，每次调用获取新线程；SDK session 负责历史记录，需显式 aclose 释放。

**「改了什么」** 新增 CodexProvider 可选模型提供商，支持 RunConfig 按运行切换，通过 PyO3 嵌入 Codex Core rust-v0.166.0 消除 JSON-RPC app-server 开销；修复会话压缩本地历史、沙箱清单二进制保留。从 v0.24.0-alpha.8 迁移需改用 Runner.run\(\) 并新建 SDK session，原 SessionState 格式不兼容。

**标签**: `#runtime`, `#tools`

---

<a id="item-harness-arch-3"></a>
### [browser-use 1.0.8rc1 发布](https://github.com/browser-use/browser-use/releases/tag/1.0.8rc1) ⭐️ 5.5/10

这是 browser-use 1.0.8rc1 候选发布，面向浏览器自动化 agent 系统提供 6 项具体改进，覆盖运行时、工具行为、安全三个方向，所有改动均附对应 PR 编号。关键更新包括：judge 请求复用缓存 run 避免重复计费；无头/SSH 场景新增跨设备 API 密钥审批流；支持 DeepSeek、Qwen thinking 模式在步数限制下的非强制重试；bu.type 不再输出密码字段值；Browser\(cdp\_url=...\)正确附加已有页面而非新建空白标签页；网关输出 token 预留从 32768 降至 16384，避免小额余额中途中断运行。可通过 pip install &\#x27;browser-use==1.0.8rc1&\#x27;安装该版本。

github · gregpr07 · 11月20日 22:48

**「设计要点」** 运行时层新增 judge 请求缓存复用机制，避免重复对同一 run 计费；网关调整输出 token 预留阈值至 16384，适配小额余额场景；无头/SSH 环境新增跨设备 API 密钥审批流，脱离本地终端限制。

**「改了什么」** 相对上一版本，本次更新共 6 项具体改动：1. judge 请求复用缓存 run，不再重复计费；2. 无头/SSH 场景支持跨设备审批 API 密钥；3. 支持 DeepSeek、Qwen thinking 模式在步数限制下的非强制重试；4. bu.type 命令不再输出密码字段值；5. Browser\(cdp\_url=...\)正确附加已有页面而非新建空白标签页；6. 网关输出 token 预留从 32768 降至 16384，避免小额余额中途中断运行。

**「评论」** 暂无社区评论可用。

**标签**: `#runtime`, `#tools`, `#permissions`

---

## Agent 工程师日报
{: #sec-agent-engineer .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-agent-engineer" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-agent-engineer-1"></a>
### [LLM 自改权重论文引争议](https://arxiv.org/abs/2611.21885) ⭐️ 7.0/10

2026 年 11 月 20 日，arXiv 发布论文《Language Models Can Rewrite Their Own Weights》，提出语言模型可通过自主推理重写自身权重实现性能提升，无需梯度与训练流程，论文称八轮连续迭代后准确率持续上升。社区讨论指出其实际改进仅体现为缩短推理轨迹以规避 token 限制，与近期 weight-space 编程研究、Google sleep 框架结论相似。该研究同时引发了自主运行大模型安全对齐风险的讨论。

hackernews · lwhsiao · 11月20日 16:29 · [社区讨论](https://news.ycombinator.com/item?id=50577265)

**「为什么重要」** 该论文直接关联 AI Agent 自改进能力，社区对其改进幅度的质疑提供了可验证的对照视角；其引发的自主模型安全风险讨论目前尚无实际案例支撑。

**「可关注」** 可关注：该论文宣称的无训练自改权重结论，与社区观察到的“仅缩短推理轨迹规避 token 限制”的实际效果存在张力，可结合原文验证技术细节与真实改进幅度。

**「评论」** 社区共识为实际改进幅度有限，仅能缩短推理轨迹规避 token 限制，与 weight-space 编程、Google sleep 框架的研究结论相似；分歧点在于部分用户担忧该研究会加剧自主 LLM 消除安全对齐的风险，另有用户对其“无训练”的表述提出质疑，认为迭代提交有效修改的过程本质仍属于训练。

**标签**: `#orchestration`, `#eval`, `#harness`

---

<a id="item-agent-engineer-2"></a>
### [Inkling 2 Mini 开源发布](https://thinkingmachines.ai/news/inkling-2-mini/) ⭐️ 7.0/10

2026 年 11 月 20 日，Thinking Machines 开源发布 Inkling 2 Mini，这是一款开权重的循环 Transformer 架构模型，官方称其性能对标 Qwen3.8-27B 级别，针对本地推理优化，公开了 llama.cpp Vulkan、Apple Silicon 平台的本地推理基准，训练全程采用 nvfp4 精度。社区实测显示，该模型在 Ryzen 395 平台跑 llama.cpp Vulkan 解码速度达 27 tokens/s，M1 Pro 32GB 设备跑 q4\_xl 量化版约 10 tokens/s，可完成简单编程任务，但复杂任务表现不稳定；社区还整理了编号为 32694、32657、32429、32704 的未合并优化补丁，可带来约 30% 的速度提升。

hackernews · jasondavies · 11月20日 20:12 · [社区讨论](https://news.ycombinator.com/item?id=50581260)

**「为什么重要」** 它首次公开了开源的循环 Transformer 架构模型权重及本地推理基准，为本地 coding agent 部署提供了新的技术选项；但其宣称的对标大参数模型性能是否在复杂真实场景下稳定成立，以及循环架构对模型安全可解释性的影响，目前尚无公开验证。

**「可关注」** 可关注：Inkling 2 Mini 的循环 Transformer 架构在本地推理场景的实际性能表现，以及社区已公开的 llama.cpp 优化补丁对推理速度的提升效果。

**「评论」** 社区普遍认可该模型的本地推理效率，认为循环 Transformer 是值得跟进的技术方向；但部分用户实测发现其在复杂任务（如图像识别类任务）上表现不稳定，官方宣称的对标大模型性能仍需更多真实场景验证，此外还有研究者希望获得更高量级的测试权限以开展 harness 调优。

**标签**: `#coding-agent`, `#eval`, `#orchestration`

---

<a id="item-agent-engineer-3"></a>
### [TuringSpace 交互式 CAPTCHA 基准发布](https://huggingface.co/papers/2611.25387) ⭐️ 7.0/10

2026-11-21，Hugging Face Daily Papers 收录论文《TuringSpace: Grounding Spatial Intelligence in Action with Interactive CAPTCHAs》。该论文提出 TuringSpace：一个含 125 个交互式 CAPTCHA 的合成网络环境，覆盖五种空间能力，要求模型通过点击和拖拽完成任务。每个任务均为生成新实例的程序，内置 checker 与 oracle，构成可扩展训练 gym。该工作针对现有 CAPTCHA 基准大多已解决且很少涉及空间、空间基准很少需要行动的局限。主要受众为 AI agent 工程师与多模态大语言模型研究者。

rss · Hugging Face Daily Papers · 11月21日 03:42

**「为什么重要」** TuringSpace 填补了现有 benchmark 在空间推理与物理行动结合上的空白。对构建 GUI 操作或具身 agent 的团队，它提供了程序化评估与训练一体的框架。

**「可关注」** 可关注：TuringSpace 的每个 CAPTCHA 均为带 checker 和 oracle 的程序化任务，这种评估与训练一体的 gym 结构可直接复用于 agent 训练环境搭建。

**标签**: `#eval`, `#spatial-reasoning`, `#agent-evaluation`

---

<a id="item-agent-engineer-4"></a>
### [Fragments 11-20：代码质量影响 Agent 成本](https://martinfowler.com/fragments/2026-11-20.html) ⭐️ 7.0/10

2026 年 11 月 20 日，Martin Fowler 在其 Fragments 专栏分享了 Marcus Borg 转述的 CodeScene 实证实验：实验覆盖 246 个开源仓库的 465 个 PR，使用 3 个 LLM 运行 5 智能体的审查修复流水线，对比 CodeHealth 得分 2.8（不健康）与 9.7（健康）的 PR，发现不健康代码会让多智能体代码审查流水线的 token 成本高出 22%至 35%，其中 Complex Method 与 Complex Conditional 是核心成本驱动代码坏味。该结论直接影响 coding agent、agent 评估系统及智能体工程流程的工程师。

rss · Martin Fowler · 11月20日 18:38

**「为什么重要」** 此前代码质量对智能体工作流成本的影响多为定性推断，该实验首次给出可量化的实证数据，明确了代码健康度与 token 成本的直接关联。目前该结论的普适性尚未验证，即是否可推广到代码生成、调试等其他智能体场景仍需更多实验支撑。

**「可关注」** 可关注：多智能体代码工作流中，Complex Method 与 Complex Conditional 是 token 成本的明确驱动因素，当前智能体工程的核心瓶颈已从代码生成转向验证环节。

**标签**: `#coding-agent`, `#eval`, `#orchestration`

---

<a id="item-agent-engineer-5"></a>
### [AltRA-Test 提出无共享标注者 LLM 评判验证](https://huggingface.co/papers/2611.26073) ⭐️ 6.0/10

2026 年 11 月 21 日 Hugging Face Daily Papers 收录论文《AltRA-Test: An Alternative Annotator Test for LLM Judges Without Shared Annotators》，提出 AltRA-Test 统计测试方法，用于验证 LLM 作为评判者的性能。该方法针对大规模标注场景中不同标注项由不同标注者子集标注的稀疏情况，解决了此前 Alt-Test 要求所有标注项由统一标注者覆盖的局限。AltRA-Test 通过 bootstrap 重采样标注项、每项抽取 k 条人类标注并替换其中 1 条为 LLM 标注，生成配对全人类与混合标注数据。当前公开内容未包含实验性能数据，适用场景相对局限于标注与评估用例。

rss · Hugging Face Daily Papers · 11月21日 03:42

**「为什么重要」** 该方法直接针对依赖 LLM-as-judge 工作流的 AI Agent 评估流水线痛点，提供了现有验证方法的可行替代方案，但当前未公开实验性能数据，实际效果尚未得到验证。

**「可关注」** 可关注：依赖 LLM-as-judge 的评估流水线若遇到大规模稀疏标注场景，可跟进该方法的实验验证进展，替代现有受标注者覆盖限制的 Alt-Test 方案。

**标签**: `#eval`

---

<a id="item-agent-engineer-6"></a>
### [ZeroVLN 免微调 VLM 导航框架提出](https://huggingface.co/papers/2611.26414) ⭐️ 5.5/10

2026 年 11 月 21 日，Hugging Face Daily Papers 收录视觉语言导航（VLN）领域论文，公开 ZeroVLN 慢速-快速导航框架设计。该框架无需对 VLM 主干做导航领域监督微调（SFT），改为给 VLM 配备语义工具调用接口，以自然语言向独立动作专家传递移动决策，先适配动作专家执行请求，再联合优化两者协同。当前公开内容存在截断，缺少完整技术细节与性能数据，该方向主要面向低成本 Agent 设计研究者，当前获 21 次 upvote。

rss · Hugging Face Daily Papers · 11月21日 03:42

**「为什么重要」** 该框架绕开 VLM 主干微调的设计思路，为低成本 Agent 的视觉导航模块设计提供了可参考的替代路径。但当前公开内容不完整，实际效果与泛化能力尚未得到充分验证。

**「可关注」** 可关注：通过语义工具调用接口将领域决策委托给独立专家、避免大模型微调的 Agent 模块拆分思路，可参考用于降低视觉导航模块的适配成本。

**标签**: `#orchestration`, `#vlm-agent`, `#tool-calling`

---

## AI 日报
{: #sec-ai-daily .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-daily" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-daily-1"></a>
### [OpenAI 公布对抗性蒸馏分层防御方案](https://openai.com/index/combatting-adversarial-distillation) ⭐️ 6.8/10

OpenAI 官方博客公布用于对抗对抗性蒸馏与能力提取的分层防御方案，覆盖模型训练、安全防护、检测、执法四个层面。当前公开内容未披露具体技术细节与防护效果数据。

rss · OpenAI Blog · 11月20日 10:00

**「为什么重要」** 该方案是行业针对模型能力非法提取风险公开的系统性防御框架，对 AI 安全防护工作有参考价值。

**「可关注」** 可关注：分层防御框架中模型训练、安全防护、检测、执法四个环节的具体落地实现。

**标签**: `#model`, `#lab`, `#industry`, `#policy`

---

<a id="item-ai-daily-2"></a>
### [上海 AI Lab 开源 Sage S2.1 Flash 技术报告](https://mp.weixin.qq.com/s?__biz=MzA3MzI4MjgzMw==&amp;mid=2651075493&amp;idx=3&amp;sn=63643451e794a6d8ac3dbb423d7f460d) ⭐️ 5.5/10

上海 AI Lab 联合复旦大学、中科院软件所等多家高校及科研机构发布 Sage S2.1 Flash 技术报告，开源总参数量达 320B 的混合专家（MoE）模型，披露完整训练流程与技术细节。该模型在四项智能体基准上达到 SOTA，采用统一科学多模态架构，支持处理文本、图像、科学数据，可完成工具调用、操作 3D Slicer 等专业软件、处理分子与光谱等科学数据的任务。

rss · 机器之心 · 11月20日 03:58

**「为什么重要」** 该模型首次将科学多模态感知能力融入通用智能体架构，同时覆盖工具调用、专业软件操作等实用场景，为通用智能体在医疗、科研等专业领域的落地提供了可参考的技术路径。

**「可关注」** 可关注其统一多模态主干架构设计，以及动态专家路由搭配稀疏注意力与线性注意力的长上下文处理方案。

**标签**: `#model`, `#lab`, `#open-source`, `#eval`

---

## AI 羊毛
{: #sec-ai-deals .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-deals" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-deals-1"></a>
### [Epic 本周免费领两款游戏](https://www.appinn.com/eggs-261120/) ⭐️ 8.0/10

你看到的内容可能由第三方 AI 基于小众软件文章提炼总结而成，可能与原文真实意图存在偏差。不代表小众软件观点和立场。请&lt;a href=&quot;https://www.appinn.com/eggs-261120/&quot; target=&quot;\_blank&quot;&gt;点击链接阅读原文&lt;/a&gt;细致比对和校验。&lt;br /&gt;&lt;br /&gt;Epic Games 本周（11.20~11.26）开展限时免费游戏福利，PC 端可领取海盗题材单人动作冒险游戏《深渊之印 / Mark of the Deep》，移动端（Android、iOS）可领取无战斗解谜生活模拟游戏《Lonesome Village》，两款游戏均支持中文，需在对应平台 Epic 商店完成领取。

rss · 小众软件 · 11月20日 07:21

**「可关注」** 可关注：Epic 本周限免游戏按平台区分领取对象，PC 端对应《深渊之印》，移动端对应《Lonesome Village》，需前往对应平台 Epic 商店操作。

**标签**: `#limited-free`, `#promo`

---

<a id="item-ai-deals-2"></a>
### [波波小红书获客助手 送 30 天激活码](https://www.v2ex.com/t/1258559#reply40) ⭐️ 8.0/10

V2EX 用户 gybin02 开展波波小红书获客助手送码活动，前 50 条符合要求的有效回帖可领取 30 天版激活码。领取需在回帖中提供邮箱（支持 Base64 编码防爬）并回答「现在怎么找小红书上的意向客户、回评论，最烦的是哪一步」，一人仅认第一条回帖，多账号仅算一个。激活码将发送至预留邮箱，激活后绑定设备可使用 30 天，到期后可选择 19.9 元买断永久版，无自动扣费。

rss · V2EX Hot · 11月20日 07:04

**「为什么重要」** 该活动为限量前 50 份的免费试用资格，无额外领取成本，可体验开发者自用的 AI 评论、线索导出等核心功能，适合有小红书运营获客需求的用户试用。

**「可关注」** 可关注：该工具为 Chrome/Edge 浏览器扩展，AI 评论的发送间隔、上限、关键词过滤等参数可自行调整，建议初始使用调低频率避免触发平台规则。

**标签**: `#promo`, `#limited-free`, `#coupon`

---

<a id="item-ai-deals-3"></a>
### [Ferry 免费 iOS 远程桌面发布](https://www.v2ex.com/t/1258592#reply25) ⭐️ 7.0/10

开发者 reallinzc1 发布免费的 iOS/iPadOS 远程桌面应用 Ferry，无广告无内购、无需注册，可通过 App Store 和 TestFlight 下载。该应用逆向实现了 macOS 14 及以上系统屏幕共享的高性能模式，支持 Apple 芯片 Mac 远程控制，Windows / Linux 设备仅支持传统 VNC 连接。使用需满足 Apple 芯片 Mac、macOS 14+、开启系统屏幕共享且用 Mac 账户密码登录的条件，Mac 端无需安装额外软件，连接期间 Mac 自身屏幕会熄灭，断开后自动恢复。

rss · V2EX Hot · 11月20日 08:10

**「为什么重要」** 当前主流远程工具 UU 远程 12 月起将限制免费版为 1080p 30 帧、虚拟屏功能需会员，Ferry 完全免费，其高性能模式实测局域网帧率达 57 帧、Tailscale 直连 48 帧，显著高于传统 VNC 的 23 帧，可满足 iPad/iPhone 远程控制 Mac 的日常需求。

**「可关注」** 可关注：仅 Apple 芯片 Mac 搭配 macOS 14+ 可使用高性能模式，且需用 Mac 账户密码登录（仅设置 VNC 密码无法启用）；若网络经过中继、SSH 隧道或代理，会自动退回无声音的普通 VNC 模式。

**标签**: `#free-tier`, `#apple-app`, `#testflight`, `#remote-desktop`, `#no-registration`

---