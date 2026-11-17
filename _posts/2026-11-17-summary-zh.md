---
layout: default
title: "Horizon Summary: 2026-11-17 (ZH)"
date: 2026-11-17
lang: zh
---

> 从 208 条内容中筛选出 16 条重要资讯。

<nav id="ah-toc" class="ah-toc" aria-label="目录"><span class="ah-toc-title">目录</span><ul><li><a href="#sec-harness-arch"><span class="ah-toc-name">Harness 架构</span><span class="ah-toc-count">3条</span></a></li><li><a href="#sec-agent-engineer"><span class="ah-toc-name">Agent 工程师日报</span><span class="ah-toc-count">6条</span></a></li><li><a href="#sec-ai-daily"><span class="ah-toc-name">AI 日报</span><span class="ah-toc-count">7条</span></a></li></ul></nav>

---

**[Harness 架构](#sec-harness-arch)**
1. [OpenHands v1.41.0 发布](#item-harness-arch-1) ⭐️ 7.8/10
2. [pydantic-ai v2.69.0 发布](#item-harness-arch-2) ⭐️ 7.8/10
3. [openai-agents-js v0.22.0-alpha.3 发布](#item-harness-arch-3) ⭐️ 7.8/10

**[Agent 工程师日报](#sec-agent-engineer)**
1. [OpenAI 儿童安全政策更新](#item-agent-engineer-1) ⭐️ 7.0/10
2. [MIRIX-2.0 多智能体记忆系统发布](#item-agent-engineer-2) ⭐️ 7.0/10
3. [Mobile AI Factory 论文发布](#item-agent-engineer-3) ⭐️ 7.0/10
4. [external-sandbox-quicksand 0.2.0 发布](#item-agent-engineer-4) ⭐️ 6.8/10
5. [Gamer 通用游戏智能体框架发布](#item-agent-engineer-5) ⭐️ 6.0/10
6. [VibePrevisBench 基准发布](#item-agent-engineer-6) ⭐️ 6.0/10

**[AI 日报](#sec-ai-daily)**
1. [OpenAI 启动首阶段嵌入式评估](#item-ai-daily-1) ⭐️ 8.8/10
2. [OpenAI 扩展学术研究者免费访问计划](#item-ai-daily-2) ⭐️ 7.8/10
3. [OpenAI 发布 1800+科研人员 ChatGPT 调研](#item-ai-daily-3) ⭐️ 7.8/10
4. [LVMH 媒体部与 OpenAI 达成战略合作](#item-ai-daily-4) ⭐️ 7.8/10
5. [OpenAI 推进医疗团队 computer-use agent 能力](#item-ai-daily-5) ⭐️ 7.8/10
6. [ChatGPT 医疗功能扩展](#item-ai-daily-6) ⭐️ 7.8/10
7. [OpenAI 宣布儿童安全新工具](#item-ai-daily-7) ⭐️ 6.8/10

---

## Harness 架构
{: #sec-harness-arch .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-harness-arch" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-harness-arch-1"></a>
### [OpenHands v1.41.0 发布](https://github.com/OpenHands/OpenHands/releases/tag/v1.41.0) ⭐️ 7.8/10

OpenHands v1.41.0 于 2026-11-16 发布。本次更新扩展 ACP 协议支持，允许从 agent 报告动态选择 reasoning effort；改进 harness hook 系统，在 Available Hooks 对话框中支持命名 workspace 和 user hook 文件；增强 secret 管理，支持重用 profile secret consent 自动启用 managed App，并允许安全替换请求的 secrets。此外，verify-openhands 测试场景扩展至非 happy path、map controls 和 browser timezone，自动化功能新增 dashboard 按 tag 分组及 assisted templates 集成。

github · openhands-release-bot\[bot\] · 11月16日 20:46

**「设计要点」** OpenHands 作为 agent harness，通过 hook 文件命名提升可扩展性；ACP 协议引入动态 reasoning effort 选择，secret 管理复用 profile consent，MCP OAuth callback 回退至浏览器后端 URL，分别强化协议适配、权限简化与环境兼容。

**「改了什么」** ACP 协议新增从 agent 报告动态选择 reasoning effort 的能力；hook 系统支持在 Available Hooks 对话框中命名 workspace 和 user hook 文件；secret 管理支持重用 profile secret consent 自动启用 managed App，并允许安全替换请求的 secrets；verify-openhands 测试覆盖扩展至非 happy path、map controls 和 browser timezone；自动化 dashboard 支持按 tag 分组，assisted templates 集成到 setup view。

**标签**: `#OpenHands Release`, `#ACP Protocol Update`, `#Harness Hook System`, `#Agent Testing`, `#Secret Management`

---

<a id="item-harness-arch-2"></a>
### [pydantic-ai v2.69.0 发布](https://github.com/pydantic/pydantic-ai/releases/tag/v2.69.0) ⭐️ 7.8/10

pydantic-ai v2.69.0 发布，核心变更包括工具调用处理架构的破坏性调整、Gemini 4 与 Groq 服务层级支持，以及流式传输循环检测。将 \`RequestInput\` 合并入 \`HandleDeferredToolCalls\`，其处理器可接受恢复令牌；新增 \`tool\_call\_ids\_are\_response\_scoped\` 配置标志，泛化响应级工具调用 ID。harness 层重命名 \`subagents\`、\`filesystem\`、\`spend\` 等包名，\`DockerSandbox\` 改为 \`DockerContainer\`，新增 \`KubernetesSandbox\` 与 \`WindowsWorkspace\`。

github · dsfaccini · 11月17日 01:03

**「设计要点」** 运行时采用分层工具调用与流式检测机制，\`DetectLoops\` 覆盖思维、文本与工具参数循环。记忆层将已解决子代理任务历史持久化至文件而非集中内存，沙箱层扩展 Kubernetes 与 Windows 支持。

**「改了什么」** 破坏性变更：\`RequestInput\` 并入 \`HandleDeferredToolCalls\`，\`Advisor\` 弃用 \`mode\` 改用 \`native=\`/\`local=\`，harness 包名与错误类名对齐能力命名。新增 Gemini 4 Hydrogen、Groq \`service\_tier\`、Anthropic 数据驻留设置，流式传输增加循环检测，子代理任务历史改为文件持久化。

**标签**: `#tools`, `#runtime`, `#breaking-change`

---

<a id="item-harness-arch-3"></a>
### [openai-agents-js v0.22.0-alpha.3 发布](https://github.com/openai/openai-agents-js/releases/tag/v0.22.0-alpha.3) ⭐️ 7.8/10

这是 OpenAI 开源的 JS Agents SDK（openai-agents-js）v0.22.0-alpha.3 的 alpha 预发布。本次发布引入类型化的 Agent 决策与 handoff 逻辑（\`agent.decide\(\)\`、\`ctx.decide\(\)\`、\`OpenAIDecisions\`、\`DecisionHandoff\`）、可插拔模型后端适配器（\`ResponsesModel\`、\`ChatCompletionsModel\`、\`AiSdkModel\`）、跨运行时语音支持（Node.js、浏览器、React Native、Workers），以及增强的本地记忆与执行器权限控制。该版本要求 Node.js 24 运行入门示例，Linux 捆绑包需 glibc 2.39+ 与 OpenSSL 3，Windows x64 需 Visual C++ Redistributable。

github · markstuart-oai · 11月16日 21:06

**「设计要点」** SDK 采用分层架构：运行时层覆盖 Node.js、浏览器、React Native 与 Workers；工具层支持命名空间、并发限制、调用者限制与 MCP 发现过滤器。记忆层提供 LocalStorage 命名配置文件、历史查询与沙盒工件辅助；执行器层通过 \`trusted\_workspace\_write\` 与 \`AGENTS.md\` 发现实现细粒度权限控制。

**「改了什么」** 相对上一版，工具回调默认改为并发 admission，需显式设置 \`maxFunctionConcurrency: 1\` 保持串行；\`Session.enqueue\(\)\` 开始拒绝忙碌时的 \`ifBusy\` 选项。\`AgentOptions\` 为非字符串 Output 类型强制要求 \`outputType\`；序列化 sandbox 恢复与检查点恢复新增可信绑定与版本对齐要求；新增 \`beforeComplete\` 钩子与 \`turn.acceptedText\(\)\` 用于输出控制。

**标签**: `#runtime`, `#subagents`, `#memory`, `#planning`

---

## Agent 工程师日报
{: #sec-agent-engineer .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-agent-engineer" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-agent-engineer-1"></a>
### [OpenAI 儿童安全政策更新](https://openai.com/index/strengthening-online-child-safety/) ⭐️ 7.0/10

2026 年 11 月 16 日 OpenAI 发布官方儿童安全政策更新。HN 社区披露至少 1 个生产环境自主 agent 本应使用本地模型执行 CSAM 分类，误切换为 OpenAI 图像 API 处理用户上传内容，累计处理超 10 万张图像后账号被永久封禁，申诉未获额外信息。同期 OpenRouter 在零数据保留端点新增 CSAM 筛查机制。事件影响使用 OpenAI、OpenRouter API 部署自主 agent 的工程师及合规团队。

hackernews · rossant · 11月16日 18:12 · [社区讨论](https://news.ycombinator.com/item?id=50520804)

**「为什么重要」** 政策更新明确了 API 调用方的合规责任边界，社区案例验证了误用内容分类接口的封号风险，OpenRouter 的筛查扩展了零数据保留端点的合规约束。目前公开信息未披露该类筛查对 agent 工作流的具体影响范围。

**「可关注」** 可关注：agent 工具链切换时需校验接口合规用途，避免误用内容分类接口触发封号，同时需确认零数据保留端点的实际筛查规则是否匹配业务场景。

**「评论」** 社区确认了生产 agent 因 CSAM 分类调用 OpenAI API 被封号的真实案例，用户反馈申诉流程无透明反馈通道。同时讨论涉及 AI 生成儿童色情内容的伦理框架争议，以及 NCMEC 联动执法的高效性。

**标签**: `#permissions`, `#observability`

---

<a id="item-agent-engineer-2"></a>
### [MIRIX-2.0 多智能体记忆系统发布](https://huggingface.co/papers/2611.12068) ⭐️ 7.0/10

Hugging Face Daily Papers 于 2026-11-17 介绍 MIRIX-2.0 多智能体记忆系统论文。该系统在五分之四的 QA 基准上达到最准确结果，LoCoMo 得分 91.4%，LongMemEval-S 得分 72.6%，领先最强基线 14.3 分。关闭 AutoDream 后，单跳与多跳文档 QA 分别超越 HyperMem 31.0 与 22.0 分。作为程序记忆，它在 ALFWorld 与 WebShop 上取得最高平均成功率，MetaClaw-Bench 达 49.2%，对比基线 44（原文截断）。该结果对 agent memory 与 eval 开发有直接关联，但当前材料截断，缺乏完整技术实现细节。

rss · Hugging Face Daily Papers · 11月17日 04:55

**「为什么重要」** 该论文提供了 agent memory 与 eval 开发的可比基准数据，其中 LongMemEval-S 与文档 QA 的显著提升，为记忆系统选型提供了量化参考。但 benchmark 表现与真实 agent harness 中的工程效果之间尚未建立直接验证关系。

**「可关注」** 可关注：MIRIX-2.0 在 LongMemEval-S 上相对基线的 14.3 分提升，以及关闭 AutoDream 后文档 QA 的显著增益，说明其记忆检索与整合机制可能值得在 agent harness 中复现验证。

**标签**: `#memory`, `#eval`, `#multi-agent`

---

<a id="item-agent-engineer-3"></a>
### [Mobile AI Factory 论文发布](https://huggingface.co/papers/2611.13509) ⭐️ 7.0/10

2026 年 11 月 17 日，Hugging Face Daily Papers 收录论文《Mobile AI Factory: Building Specialized Language Models for Your Mobile Device》（地址：https://huggingface.co/papers/2611.13509）并获 19 次用户点赞，提出同名智能体系统，可针对指定移动任务和目标设备端到端自动化生成微调、量化后的小语言模型（SLM）。系统由编排 LLM 决策工作流步骤（包括调整超参、挖掘真实数据、生成合成样本），设置基于准确率的回滚规则，会从小模型到大模型跨基座模型与量化方案搜索，并适配目标设备的推理引擎实测数据调整准确率目标。当前公开内容片段未包含完整性能基准测试数据，该研究面向端侧 AI 工具链与智能体编排设计场景。

rss · Hugging Face Daily Papers · 11月17日 04:55

**「为什么重要」** 该研究已实现将真实设备推理实测纳入端侧 SLM 自动化优化流程的智能体编排参考方案，为边缘 AI 工具链设计提供了可复用的流程思路；但当前公开内容缺少完整性能基准数据，实际应用效果尚未得到充分验证。

**「可关注」** 可关注：端侧 SLM 优化场景中，采用编排 LLM 做工作流决策、结合真实设备推理实测与准确率回滚规则的自动化流程设计。

**标签**: `#orchestration`, `#eval`, `#on-device-ai`, `#agentic-workflow`, `#model-optimization`

---

<a id="item-agent-engineer-4"></a>
### [external-sandbox-quicksand 0.2.0 发布](https://github.com/prime-radiant-inc/external-sandbox-quicksand/releases/tag/0.2.0) ⭐️ 6.8/10

Simon Willison 于 2026-11-16 发布 prime-radiant-inc/external-sandbox-quicksand 0.2.0。本次更新新增 \`--proxy\` 选项，以 deny-all 模式启动 HTTP\(S\) 代理，允许通过 \`/proxy\` 页面添加 allow rules，\`--proxy-config FILE\` 仍可在启动时注入策略且优先级更高。代理改用 truststore 库验证上游 TLS 证书 against OS trust store，修复了主机浏览器与 curl 可接受但代理返回 502 的问题。日志层面，客户端中途断开连接不再记为 502，而是记为 \`allowed\` 并附带 \`client\_disconnected\` 原因；证书失败则记录为 \`upstream\_certificate\_not\_verified\`。

github · simonw · 11月16日 22:24

**「为什么重要」** 对于构建 coding agent 沙箱网络的工程师，deny-all 默认模式简化了初始白名单配置，OS trust store 集成减少了 TLS 证书配置摩擦。这两项变更直接作用于代理层的网络权限控制与可观测性，但 minor version bump 和 narrow scope 限制了更广泛的影响面。

**「可关注」** 可关注：deny-all 默认代理模式与 \`/proxy\` 页面动态加白名单的组合，可能降低策略文件维护成本；TLS 验证切换到 OS trust store 后，需确认目标环境 trust store 的覆盖范围是否满足业务需求。

**标签**: `#sandbox`, `#proxy`, `#permissions`, `#observability`, `#tooling`

---

<a id="item-agent-engineer-5"></a>
### [Gamer 通用游戏智能体框架发布](https://huggingface.co/papers/2611.18397) ⭐️ 6.0/10

2026 年 11 月 17 日 Hugging Face Daily Papers 更新了一篇 arXiv 预印本，介绍通用视觉-语言-动作基础模型 Gamer，面向长时序实时游戏智能体场景，该预印本当前获得 93 次社区点赞。该模型采用端到端架构，整合感知、记忆管理与多步推理能力，支持 2D 图形界面与 3D 模拟世界的交互。训练阶段先使用数万小时真实设备键盘鼠标交互数据继续预训练，再通过稀疏思维指令调优降低冗余计算。当前仅公开截断摘要，未披露性能基准与可复现细节，泛用性待完整论文验证。

rss · Hugging Face Daily Papers · 11月17日 04:55

**「为什么重要」** 该工作首次将端到端感知-记忆-推理架构、真实设备交互预训练与稀疏思维调优整合到游戏智能体框架中，为长时序交互智能体设计提供了新参考。但当前公开内容缺少性能基准与可复现信息，对通用智能体系统的适用性尚未得到验证。

**「可关注」** 可关注：真实设备交互数据预训练与稀疏思维调优的组合，是否为长时序交互智能体提供了可复用的效率优化路径。

**标签**: `#memory`, `#eval`

---

<a id="item-agent-engineer-6"></a>
### [VibePrevisBench 基准发布](https://huggingface.co/papers/2611.15789) ⭐️ 6.0/10

HF 每日论文 2026 年 11 月 17 日发布新基准 VibePrevisBench，用于评估能根据 brief 生成可执行 4D Blender 场景的编码智能体。该基准包含 242 个任务，覆盖脚本、照片、续写、参考视频 4 类输入，采用基于规则的场景检查（重跑代码后对比隐藏真实值的 9 个维度）与 VLM 驱动的屏幕检查（视觉语言模型判断渲染画面符合度）双评估维度。该资源主要面向 3D/4D 工具类编码智能体、专用智能体评估方向的工程师，目前仅覆盖细分场景，不针对通用编码智能体能力评估。

rss · Hugging Face Daily Papers · 11月17日 04:55

**「为什么重要」** 该基准填补了 4D Blender 场景生成类编码智能体的专用评估空白，为相关方向的工程师提供了可复用的任务集与评估框架；但因其仅针对细分使用场景，对通用编码智能体能力评估无直接参考价值。

**「可关注」** 可关注：VibePrevisBench 的 242 个任务覆盖 4 类输入，双维度评估指标可直接复用于 3D/4D 工具类编码智能体的效果验证。

**标签**: `#eval`, `#coding-agent`

---

## AI 日报
{: #sec-ai-daily .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-ai-daily" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-ai-daily-1"></a>
### [OpenAI 启动首阶段嵌入式评估](https://openai.com/index/our-first-phase-of-embedded-assessments) ⭐️ 8.8/10

OpenAI 于 2026 年 11 月 16 日启动首阶段嵌入式评估项目，与 Apollo Research、METR、Transluce、Goodfire 四家独立研究机构合作，对模型对齐、安全防护及监控系统开展独立评估。该项目为 OpenAI 新推出的安全评估流程，目前未公开具体评估范围、时间线或结果披露计划。

rss · OpenAI Blog · 11月16日 08:00

**「为什么重要」** 这是主流 AI 实验室首次公开落地嵌入式外部评估机制，将独立第三方纳入安全评估流程，为行业对齐研究提供了可参考的实践样本。

**「可关注」** 可关注：后续评估的具体维度、执行流程及结果披露规则是否会向行业公开。

**标签**: `#lab`, `#eval`, `#policy`, `#industry`

---

<a id="item-ai-daily-2"></a>
### [OpenAI 扩展学术研究者免费访问计划](https://openai.com/index/expanding-chatgpt-for-academic-researchers) ⭐️ 7.8/10

OpenAI 宣布扩展 ChatGPT for Academic Researchers 项目，将为全球 20 万名研究者免费提供前沿模型访问权限。

rss · OpenAI Blog · 11月16日 17:00

**「为什么重要」** 该扩展降低了全球学术研究者的前沿 AI 工具使用门槛，有助于推动 AI 在科研场景的普及应用。

**「可关注」** 可关注：OpenAI 学术研究者免费访问计划的申请资格、覆盖模型范围及使用限制的具体规则。

**标签**: `#lab`, `#industry`, `#product`, `#policy`

---

<a id="item-ai-daily-3"></a>
### [OpenAI 发布 1800+科研人员 ChatGPT 调研](https://openai.com/index/science-at-the-frontier) ⭐️ 7.8/10

OpenAI 官方博客于 2026 年 11 月 16 日发布研究报告，披露对 1800 余名科学家使用 ChatGPT 开展科研的调研结果。报告覆盖科研工作流中的日常使用场景、科学家自报的生产力变化，以及对 AI 驱动科学发现的预期。

rss · OpenAI Blog · 11月16日 12:00

**「为什么重要」** 这是目前少有的面向科研群体的大规模 ChatGPT 使用实证调研，可补充行业对 AI 工具在专业领域落地效果的认知空白。

**「可关注」** 可关注：报告中披露的科研场景下 ChatGPT 高频使用场景与用户自报效率变化数据。

**标签**: `#lab`, `#industry`, `#product`

---

<a id="item-ai-daily-4"></a>
### [LVMH 媒体部与 OpenAI 达成战略合作](https://openai.com/index/lvmh-media-division-partnership) ⭐️ 7.8/10

2026 年 11 月 16 日，OpenAI 官方宣布与 LVMH 媒体部达成战略合作。合作核心目标为支持新闻业应用 AI 技术，同时让 LVMH 旗下出版物可通过 ChatGPT 访问。目前公开信息未披露具体技术实现细节与落地时间表。

rss · OpenAI Blog · 11月16日 09:00

**「为什么重要」** 这是头部 AI 实验室与大型媒体集团的公开合作，为 AI 在新闻采编、内容分发领域的落地提供了新的行业合作样本。

**「可关注」** 可关注头部 AI 公司与传统媒体在内容接入、采编辅助场景的合作落地进展。

**标签**: `#lab`, `#industry`, `#product`

---

<a id="item-ai-daily-5"></a>
### [OpenAI 推进医疗团队 computer-use agent 能力](https://openai.com/index/advancing-computer-use-for-healthcare-teams) ⭐️ 7.8/10

OpenAI 官方博客发布公告，宣布推进面向医疗团队场景的 computer-use agent 能力。当前公开材料未披露具体技术改进内容、性能指标、部署限制及与过往版本的差异。

rss · OpenAI Blog · 11月16日 06:00

**「为什么重要」** 该动向是 computer-use agent 技术在医疗垂直场景的明确行业应用推进，拓展了 AI 代理的落地场景范围。

**标签**: `#lab`, `#industry`, `#product`

---

<a id="item-ai-daily-6"></a>
### [ChatGPT 医疗功能扩展](https://openai.com/index/more-ways-to-move-care-forward-with-chatgpt-for-healthcare) ⭐️ 7.8/10

OpenAI 于 2026 年 11 月 16 日宣布扩展 ChatGPT 医疗场景功能，新增计算机使用代理、增强型临床回答能力，以及可跨医疗软件运行的医疗插件。三类功能均面向医疗工作流设计，目标是辅助完成实际医疗任务。

rss · OpenAI Blog · 11月16日 06:00

**「为什么重要」** 这是 OpenAI 将计算机使用代理、跨系统插件能力落地到医疗垂直场景的实质性产品扩展，标志着通用 AI 工具向专业行业工作流的渗透。

**「可关注」** 可关注：ChatGPT 医疗场景新增的计算机使用代理与跨平台插件能力，或为医疗系统自动化集成提供新接口。

**标签**: `#lab`, `#industry`, `#product`

---

<a id="item-ai-daily-7"></a>
### [OpenAI 宣布儿童安全新工具](https://openai.com/index/strengthening-online-child-safety) ⭐️ 6.8/10

OpenAI 于 2026-11-16 发布官方博文，宣布推出新工具、实践指导及合作伙伴关系，用于预防、检测和应对在线儿童性剥削与虐待。此次公告属于政策与行业合作范畴。但公开摘录未披露具体工具名称、技术架构或与既有安全措施的区别。

rss · OpenAI Blog · 11月16日 17:00

**标签**: `#policy`, `#industry`, `#lab`

---