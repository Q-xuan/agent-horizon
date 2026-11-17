---
layout: default
title: "Horizon Summary: 2026-11-17 (EN)"
date: 2026-11-17
lang: en
---

> From 226 items, 19 important content pieces were selected

---

**Agent Harness Architecture**
1. [pydantic-ai v2.69.0 发布](#item-harness-arch-1) ⭐️ 8.3/10
2. [openai-agents-js v0.22 发布](#item-harness-arch-2) ⭐️ 7.8/10
3. [adk-go v2.8.0 发布](#item-harness-arch-3) ⭐️ 7.8/10

**AI Agent Engineer**
1. [OpenAI 儿童安全政策收紧](#item-agent-engineer-1) ⭐️ 7.0/10
2. [HF 每日论文：Mobile AI Factory](#item-agent-engineer-2) ⭐️ 7.0/10
3. [WebArena-Pro Benchmark Released](#item-agent-engineer-3) ⭐️ 7.0/10
4. [Clover 2 公开 27.8B 动态路由](#item-agent-engineer-4) ⭐️ 7.0/10
5. [quicksand 0.2.0 发布](#item-agent-engineer-5) ⭐️ 6.8/10
6. [external-sandbox-container 0.2.0 发布](#item-agent-engineer-6) ⭐️ 6.3/10
7. [MIRIX-2.0 多智能体记忆系统论文收录](#item-agent-engineer-7) ⭐️ 6.0/10
8. [HF Daily Paper: 多智能体对齐研究](#item-agent-engineer-8) ⭐️ 6.0/10

**AI Daily**
1. [OpenAI 扩展 ChatGPT 学术研究者项目](#item-ai-daily-1) ⭐️ 8.8/10
2. [OpenAI 推进医疗 agent 技术](#item-ai-daily-2) ⭐️ 8.8/10
3. [LVMH媒体部门与OpenAI达成战略合作](#item-ai-daily-3) ⭐️ 8.3/10
4. [OpenAI 发布科研用 ChatGPT 使用报告](#item-ai-daily-4) ⭐️ 7.8/10
5. [OpenAI 启动首阶段嵌入式评估](#item-ai-daily-5) ⭐️ 7.8/10
6. [ChatGPT Healthcare 功能扩展](#item-ai-daily-6) ⭐️ 7.8/10

**AI Deals**
1. [BrowserPod 4.0 浏览器MicroVM免费开放](#item-ai-deals-1) ⭐️ 6.0/10
2. [Supabase Free 周备份工具开源](#item-ai-deals-2) ⭐️ 5.0/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [pydantic-ai v2.69.0 发布](https://github.com/pydantic/pydantic-ai/releases/tag/v2.69.0) ⭐️ 8.3/10

pydantic-ai v2.69.0 发布。版本将 \`RequestInput\` 合并入 \`HandleDeferredToolCalls\` 并支持 resume token（破坏性变更），通过 \`tool\_call\_ids\_are\_response\_scoped\` profile 标志泛化响应级工具调用 ID。\`DetectLoops\` 新增流式思维、文本及工具参数的循环检测。模型支持扩展至 Gemini 4 Hydrogen 与 Groq \`service\_tier\`，harness 层重构包名与类名并新增 \`WindowsWorkspace\`、\`KubernetesSandbox\` 及 \`Peers\` 对等消息能力。

github · dsfaccini · Nov 17, 01:03

**「设计要点」** harness 层将 \`subagents\`、\`filesystem\`、\`spend\` 包重命名为能力名，并对齐 store、\`ACP\*\` 及 \`\*Error\` 类名，工具层向能力导向架构迁移。子代理任务历史从 \`DelegationTasks\` 所有者内存移至保存文件，调整内存持有方式；\`DockerSandbox\` 重命名为 \`DockerContainer\`，\`BubblewrapSandbox\` 重命名为 \`BubblewrappedWorkspace\`，统一运行时沙箱抽象。

**「改了什么」** 破坏性变更：\`RequestInput\` 并入 \`HandleDeferredToolCalls\`，处理器可接收 resume token；响应级工具调用 ID 由 \`tool\_call\_ids\_are\_response\_scoped\` profile 标志控制。新增流式循环检测（\`DetectLoops\`）。模型支持增加 Gemini 4 Hydrogen 与 Groq \`service\_tier\`。harness 包与类名重构，新增 \`WindowsWorkspace\`、\`KubernetesSandbox\` 及 \`Peers\` 对等消息。

**Tags**: `#tools`, `#runtime`

---

<a id="item-harness-arch-2"></a>
### [openai-agents-js v0.22 发布](https://github.com/openai/openai-agents-js/releases/tag/v0.22.0-alpha.3) ⭐️ 7.8/10

OpenAI released openai-agents-js v0.22.0-alpha.3, introducing typed Decisions APIs \(\`agent.decide\(\)\`, \`ctx.decide\(\)\`, \`DecisionHandoff\`, \`OpenAIDecisions\`\) for agent routing and handoffs, pluggable model backend adapters \(\`ResponsesModel\`, \`ChatCompletionsModel\`, \`AiSdkModel\`\) with streaming support, and cross-platform native voice/Realtime capabilities across Node.js, browsers, React Native, and Workers. The release expands local executor permissions via \`trusted\_workspace\_write\` and \`AGENTS.md\` discovery, adds named profiles and history forking to LocalStorage, and requires \`openai\` 7.30.0 or later for decision adapters. Starter bundles target Linux x64/ARM64, macOS Apple silicon, and Windows x64, requiring glibc 2.39+, OpenSSL 3, and Node.js 24.

github · markstuart-oai · Nov 16, 21:06

**「设计要点」** Typed Decisions make handoff control flow explicit and injectable by harnesses. Model backends abstract Responses, Chat Completions, and AI SDK into unified streaming adapters. Local executors separate write grants from snapshot trust via \`trusted\_workspace\_write\` and \`resumeAuthority\` declarations, while \`AGENTS.md\` enables project-level guidance discovery.

**「改了什么」** Tool callbacks now overlap by default; set \`maxFunctionConcurrency: 1\` to serialize per turn. \`Session.enqueue\(\)\` rejects the \`ifBusy\` option instead of ignoring it. \`AgentOptions\` enforces matching \`outputType\` for non-string outputs. Sandbox resume requires trusted bindings and aligned package versions. Native tools gain namespaces, concurrency limits, caller restrictions, managed approvals, client-side search, and configurable error formatting.

**Tags**: `#runtime`, `#planning`, `#memory`, `#subagents`

---

<a id="item-harness-arch-3"></a>
### [adk-go v2.8.0 发布](https://github.com/google/adk-go/releases/tag/v2.8.0) ⭐️ 7.8/10

google/adk-go v2.8.0 正式发布。本次更新包含破坏性配置路径解析变更：工作流边引用不再接受绝对 config\_path，且配置目录内任何符号链接均被拒绝，影响 Kubernetes ConfigMap、Bazel runfiles 及 Nix store 路径，需复制为真实文件目录（如 cp -rL）后使用。功能新增内存 artifact:// 引用、服务端 OAuth2 同意流、工具触发终端用户登录、Agent Engine 部署配置、Agent Runtime 流式查询客户端、MCP 工具转换与名称前缀、Vertex AI RAG 记忆、BigQuery 工具集及 OTLP 遥测导出。错误修复涵盖 adka2a 空文本转换与 panic 防护、adkrest 事件序列化与会话处理、agentengine 时间戳小数秒保留。

github · adk-go-bot · Nov 16, 15:05

**「设计要点」** Go 运行时在内存服务中新增 artifact 引用支持。权限层新增服务端 OAuth2 同意流与工具触发终端用户登录能力；记忆层支持增量事件写入、adk-python 搜索规则对齐及 Vertex AI RAG 服务；工具层新增 MCP 工具转换（ToMCPTool）、名称前缀及 BigQuery 工具集；遥测层新增 OTLP 与 Google Cloud 导出的 MeterProvider。

**「改了什么」** v2.8.0 引入破坏性配置路径解析变更：工作流边引用拒绝绝对路径与配置目录内符号链接，需将 K8s ConfigMap、Bazel runfiles 等挂载复制为真实文件目录后使用。同时新增内存 artifact 引用、服务端 OAuth2 同意流、工具触发终端用户登录、Agent Engine 部署配置、Agent Runtime 流式查询客户端、MCP 工具转换与前缀、Vertex AI RAG 记忆、BigQuery 工具集及 OTLP 遥测导出，并修复 adka2a 空文本转换与 panic、adkrest 事件序列化及 agentengine 时间戳精度问题。

**Tags**: `#runtime`, `#permissions`, `#memory`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [OpenAI 儿童安全政策收紧](https://openai.com/index/strengthening-online-child-safety/) ⭐️ 7.0/10

OpenAI 2026-11-16 发布儿童安全保护声明。社区报告至少三类直接影响：生产环境自主 agent 调用 OpenAI 图像分类 API 处理用户上传内容，累计处理超 100,000 张图片后账号被封禁，申诉未获事件详情；Claude 调用 GPT 图像生成时，涉及儿童场景的提示词触发安全过滤，多次拒绝生成；OpenRouter 对 Zero Data Retention 端点执行 CSAM 扫描与留存，改变 API 数据保留承诺。这些事件涉及 agent 权限设计、工具链配置和合规边界。

hackernews · rossant · Nov 16, 18:12 · [Discussion](https://news.ycombinator.com/item?id=50520804)

**「为什么重要」** 这些事件显示儿童安全过滤已从模型输出层延伸到 API 调用层和数据留存层。agent 工程师需重新评估工具权限边界与第三方 API 的数据处理承诺，避免生产环境意外触发合规封禁。

**「可关注」** 可关注：自主 agent 调用第三方图像分类或生成 API 时，需显式验证对方安全策略与数据留存承诺，防止批量处理触发账号封禁或合规风险。

**「评论」** 社区共识集中在生产环境 agent 缺乏对第三方安全策略的可见性，导致意外封禁；分歧在于 OpenRouter 对 ZDR 端点的扫描是否违反零数据保留承诺。

**Tags**: `#permissions`, `#safety`, `#observability`, `#toolchain`, `#coding-agent`

---

<a id="item-agent-engineer-2"></a>
### [HF 每日论文：Mobile AI Factory](https://huggingface.co/papers/2611.13509) ⭐️ 7.0/10

2026年11月17日Hugging Face每日论文收录介绍Mobile AI Factory的论文，该系统是面向移动设备的自动化智能体系统，可端到端生成针对特定任务和目标手机定制化、量化后的小语言模型（SLM）。关键设计包括：由编排LLM决策调超参、挖掘真实数据或生成合成样本，设置基于准确率的规则化回滚机制，跨基础模型与量化方案做自适应搜索，并接入目标手机的真实推理测量。当前公开内容仅为截断摘要，未提供性能基准数据。

rss · Hugging Face Daily Papers · Nov 17, 05:34

**「为什么重要」** 该论文公开了端侧SLM自动化生产的完整智能体编排、评估与回滚设计，对自动化ML harness与agent orchestration工程师有直接参考价值；但目前仅公开截断摘要，无性能基准，实际效果尚未得到验证。

**「可关注」** 可关注：其编排LLM搭配规则化准确率回滚、跨模型/量化自适应搜索并结合真实端侧推理测量的系统设计，对自动化ML流水线与agent orchestration工程有直接参考价值。

**Tags**: `#orchestration`, `#eval`, `#harness`

---

<a id="item-agent-engineer-3"></a>
### [WebArena-Pro Benchmark Released](https://huggingface.co/papers/2611.17955) ⭐️ 7.0/10

Hugging Face Daily Papers announced the WebArena-Pro reproducible multimodal web agent benchmark on November 17, 2026. The benchmark includes 300 tasks across 20 self-hosted web applications in 6 domain categories. It addresses core limitations of existing web agent evaluation tools: narrow application coverage, text/vision-only modality, irreproducibility of live benchmarks, and lack of audio/video content evaluation. It targets engineers building or evaluating web agents, with the underlying research accessible via the linked arXiv preprint. The associated paper has received 12 upvotes on Hugging Face Daily Papers.

rss · Hugging Face Daily Papers · Nov 17, 05:34

**「为什么重要」** Existing web agent evaluation benchmarks suffer from insufficient application coverage, single modality, and irreproducible live scenarios. WebArena-Pro directly fixes these gaps to offer a more realistic evaluation standard for relevant engineers. It is not yet confirmed whether this benchmark will be widely adopted as a universal industry standard.

**「可关注」** 可关注：Existing reproducible web agent benchmarks have narrow application coverage, text/vision-only modality, and irreproducible live scenarios, while WebArena-Pro&\#x27;s self-hosted multimodal design can directly fill gaps in current evaluation workflows.

**Tags**: `#eval`, `#web-agent`, `#benchmark`, `#multimodal`, `#reproducibility`

---

<a id="item-agent-engineer-4"></a>
### [Clover 2 公开 27.8B 动态路由](https://www.reddit.com/r/LocalLLaMA/comments/1xyb7jw/clover_2_dense_278b_base_7_lora_experts_routed/) ⭐️ 7.0/10

Clover 2 团队于 2026-11-17 公开 27.8B base 模型及 7 个任务专用 LoRA 适配器，推理时通过训练好的路由器按 token 动态路由，null slot 回退 base 模型，实现非静态混合。配套 vLLM 插件支持真实 per-token 行为，所有组件均已公开。相比 untouched base，GSM8K/MATH-500/GSM-Hard、LongBench-v2 及创意写作任务基准有提升。因混合注意力架构，llama.cpp 支持仍处实验阶段，无 GGUF，vLLM 为官方路径。

reddit · r/LocalLLaMA · /u/bakatristan · Nov 17, 04:35

**「为什么重要」** 该发布包含 per-token 路由器、7 个 LoRA 适配器及 vLLM 插件的完整公开实现，相比静态合并方案，为 LoRA 编排和 agent harness 提供了可验证的工程参考。

**「可关注」** vLLM 为当前唯一官方支持路径，GGUF 及 llama.cpp 集成仍处实验阶段，自托管部署需评估格式兼容性。

**Tags**: `#orchestration`, `#eval`, `#harness`

---

<a id="item-agent-engineer-5"></a>
### [quicksand 0.2.0 发布](https://github.com/prime-radiant-inc/external-sandbox-quicksand/releases/tag/0.2.0) ⭐️ 6.8/10

simonw 于 2026-11-16 发布 prime-radiant-inc/external-sandbox-quicksand 0.2.0。新增 \`--proxy\` 选项以 deny-all 模式启动 HTTP\(S\) 代理，支持通过 \`/proxy\` 网页界面添加白名单；\`--proxy-config FILE\` 仍可提供启动策略，且两者同时存在时后者优先。代理改用 \`truststore\` 库验证上游 TLS 证书 against 操作系统信任库，修复主机浏览器和 \`curl\` 接受的站点此前返回 502 的问题。日志调整：客户端中途断连记录为 \`allowed\` 并附带 \`client\_disconnected\` 原因，证书失败记录为 \`upstream\_certificate\_not\_verified\`。

github · simonw · Nov 16, 22:24

**「为什么重要」** 该版本引入交互式网页白名单代理模式，改变 agent 网络权限配置方式。TLS 信任库验证修复减少外部访问误报 502，提升代理可靠性。但作为 0.2.0 细分工具更新，影响目前限于该工具用户群体。

**「可关注」** 可关注：代理默认 deny-all 并支持网页白名单，TLS 验证改用系统 trust store，日志区分客户端断开与上游证书错误。

**Tags**: `#permissions`, `#observability`, `#harness`

---

<a id="item-agent-engineer-6"></a>
### [external-sandbox-container 0.2.0 发布](https://github.com/prime-radiant-inc/external-sandbox-container/releases/tag/0.2.0) ⭐️ 6.3/10

simonw 于 2026-11-16 发布 external-sandbox-container 0.2.0。本次小版本新增 \`--proxy\` 选项，以 deny-all 模式启动托管 HTTP\(S\) 代理，支持在 \`/proxy\` 页面添加允许规则。集成 truststore 库后，上游 TLS 证书验证改用操作系统信任库，避免主机浏览器与 curl 接受的站点返回 502。沙箱客户端中途断开连接时，日志从 502 改为记录为 \`allowed\`，并附加上游状态与 \`client\_disconnected\` 原因；证书失败则记录为 \`upstream\_certificate\_not\_verified\`。该变更面向 agent 沙箱与网络权限控制开发者，未引入破坏性变更。

github · simonw · Nov 16, 22:24

**「为什么重要」** deny-all 默认模式降低网络策略配置门槛，系统信任库集成减少误 502。但影响范围限于该容器的代理与日志行为，尚未证实对上层 agent 框架的连锁效应。

**「可关注」** 可关注：\`--proxy\` 与 \`--proxy-config\` 同时提供时后者优先，以及客户端断连日志语义从 502 改为 \`client\_disconnected\` 后，现有告警规则需同步调整。

**Tags**: `#sandbox`, `#proxy`, `#permissions`, `#observability`, `#security`

---

<a id="item-agent-engineer-7"></a>
### [MIRIX-2.0 多智能体记忆系统论文收录](https://huggingface.co/papers/2611.12068) ⭐️ 6.0/10

2026年11月17日Hugging Face Daily Papers收录arXiv预印本论文《MIRIX-2.0: Multi-Agent Memory System》，该论文提出面向LLM智能体的多智能体记忆系统MIRIX-2.0，旨在同时实现实用性、准确性与效率。在对比系统中，MIRIX-2.0在4/5的QA基准上准确率最高，LoCoMo基准得分91.4%，LongMemEval-S基准得分72.6%，领先最强基线14.3分；关闭AutoDream功能后，其在单跳和多跳文档QA上分别比HyperMem高31.0和22.0分；作为程序记忆时，其在ALFWorld、WebShop和MetaClaw-Bench基准上的平均成功率高于对比的其他记忆方法。该成果目前仅为预印本，非生产就绪工具，完整技术细节与结果可复现性需查阅原论文验证，暂无社区公开讨论。

rss · Hugging Face Daily Papers · Nov 17, 05:34

**「为什么重要」** 该预印本针对LLM智能体长期记忆存在的参数记忆需训练、记忆整合易丢失细节、全量存储检索成本高的痛点，提出了新的多智能体记忆方案，在多个主流智能体记忆与QA基准上取得领先成绩；目前该成果仅为预印本，实际工程落地效果、技术细节可复现性还需原论文进一步验证，对当前coding agent工程的直接参考价值有限。

**「可关注」** 可关注：该预印本提出的多智能体记忆方案在主流智能体记忆基准上表现领先，待原论文公开完整技术细节后可评估其对现有智能体记忆模块的参考价值。

**Tags**: `#memory`, `#eval`

---

<a id="item-agent-engineer-8"></a>
### [HF Daily Paper: 多智能体对齐研究](https://huggingface.co/papers/2611.17820) ⭐️ 6.0/10

Hugging Face Daily Papers 于 2026-11-17 聚合了一篇多智能体 LLM 对齐迁移研究的截断摘要。该研究在脓毒症分诊、新闻推荐及咨询提案生成任务上发现：\(1\) 单智能体与团队的安全差距与模型能力无明确趋势，Anthropic Mythos Preview 在部分任务上差距最大、在另一些任务上最小；\(2\) 互评、群聊等自然干预无法可靠地将团队行为拉回单智能体对齐水平；\(3\) 第三个发现被截断。摘要未提供完整实验规模、统计显著性及技术细节，限制了直接工程应用。

rss · Hugging Face Daily Papers · Nov 17, 05:34

**「为什么重要」** 该研究提供了实验证据，表明单智能体对齐向多智能体团队的迁移存在系统性失效风险。由于摘要被截断且缺乏完整技术细节，这些发现对当前工程实践的具体影响尚未完全明确。

**「可关注」** 可关注：互评与群聊等常见多智能体协调机制在实验中未稳定恢复单智能体对齐行为，提示单智能体安全干预向团队场景的迁移存在失效风险。

**Tags**: `#eval`, `#orchestration`

---

## AI Daily

<a id="item-ai-daily-1"></a>
### [OpenAI 扩展 ChatGPT 学术研究者项目](https://openai.com/index/expanding-chatgpt-for-academic-researchers) ⭐️ 8.8/10

OpenAI has officially announced the expansion of its ChatGPT for Academic Researchers program, granting 200,000 researchers worldwide free access to its frontier models. The program previously operated at a limited scale, and this expansion marks a significant increase in access coverage.

rss · OpenAI Blog · Nov 16, 17:00

**「为什么重要」** This is the first large-scale expansion of the academic program, directly lowering the cost barrier for global researchers to access frontier AI models, a privilege previously restricted to a much smaller group of academic users.

**「可关注」** 可关注：The specific model coverage, call quotas and detailed usage restriction rules for this free academic access program.

**Tags**: `#lab`, `#product`, `#policy`

---

<a id="item-ai-daily-2"></a>
### [OpenAI 推进医疗 agent 技术](https://openai.com/index/advancing-computer-use-for-healthcare-teams) ⭐️ 8.8/10

OpenAI 于 2026-11-16 发布官方博客，宣布其 computer-use agent 技术取得进展，拟部署至医疗团队。该信息来自 OpenAI 官方 RSS 源，标签为 lab、product、industry。现有材料未包含具体技术细节、性能指标或版本号。

rss · OpenAI Blog · Nov 16, 06:00

**「为什么重要」** 该公告涉及 AI agent 在医疗行业的应用，医疗场景自动化需求高且监管严格。OpenAI 作为领先实验室向该领域推进，显示技术应用转向高门槛行业。

**「可关注」** 可关注：OpenAI 官方公告了面向医疗团队的 computer-use agent 进展，但未披露具体实现、基准数据或限制条件。

**Tags**: `#lab`, `#product`, `#industry`

---

<a id="item-ai-daily-3"></a>
### [LVMH媒体部门与OpenAI达成战略合作](https://openai.com/index/lvmh-media-division-partnership) ⭐️ 8.3/10

2026年11月16日，LVMH媒体部门与OpenAI官方宣布达成战略合作。合作核心包含两项内容：一是共同以AI技术支持新闻业发展，二是LVMH旗下出版物将可通过ChatGPT更便捷地触达用户。

rss · OpenAI Blog · Nov 16, 09:00

**「为什么重要」** 这是奢侈品集团媒体板块与头部AI实验室的首次公开战略合作，为AI在新闻业的内容生产、分发场景提供了可参考的落地样本。

**「可关注」** 可关注：LVMH旗下出版物接入ChatGPT的具体交互规则，以及新闻业场景下AI生成内容的合规边界。

**Tags**: `#industry`, `#lab`, `#product`

---

<a id="item-ai-daily-4"></a>
### [OpenAI 发布科研用 ChatGPT 使用报告](https://openai.com/index/science-at-the-frontier) ⭐️ 7.8/10

OpenAI官方博客发布科研场景ChatGPT使用报告，披露1800余名科学家的相关调研发现。报告覆盖日常科研流程、报告生产力提升情况以及对科研发现的预期三个核心维度。

rss · OpenAI Blog · Nov 16, 12:00

**「为什么重要」** 该报告提供了AI在科研场景落地的明确一手数据，是当前AI行业应用动态中值得参考的样本。

**Tags**: `#lab`, `#industry`, `#product`, `#research`

---

<a id="item-ai-daily-5"></a>
### [OpenAI 启动首阶段嵌入式评估](https://openai.com/index/our-first-phase-of-embedded-assessments) ⭐️ 7.8/10

OpenAI 启动嵌入式评估第一阶段，与 Apollo Research、METR、Transluce 及 Goodfire 合作，独立评估模型对齐、安全措施与监控系统。这是 OpenAI 首次将外部研究机构嵌入内部评估流程。

rss · OpenAI Blog · Nov 16, 08:00

**「为什么重要」** 这是 OpenAI 首次联合外部研究机构独立评估模型对齐、安全措施与监控系统。

**「可关注」** 可关注：OpenAI 与 Apollo Research、METR、Transluce、Goodfire 合作开展独立评估。

**Tags**: `#lab`, `#eval`, `#policy`, `#industry`

---

<a id="item-ai-daily-6"></a>
### [ChatGPT Healthcare 功能扩展](https://openai.com/index/more-ways-to-move-care-forward-with-chatgpt-for-healthcare) ⭐️ 7.8/10

OpenAI 宣布扩展 ChatGPT 的医疗保健功能，新增 computer-use agents、增强临床答案质量，以及可跨医疗软件运行的互操作插件。这些功能旨在帮助用户在医疗软件中完成实际工作。公告未披露具体性能指标或上线时间。

rss · OpenAI Blog · Nov 16, 06:00

**「为什么重要」** 医疗保健领域对 AI 工具的集成度要求较高，此次扩展的 agent 与插件能力直接针对实际工作流场景。

**「可关注」** 可关注：ChatGPT 新增 computer-use agents 与跨医疗软件互操作插件。

**Tags**: `#lab`, `#product`, `#industry`

---

## AI Deals

<a id="item-ai-deals-1"></a>
### [BrowserPod 4.0 浏览器MicroVM免费开放](https://browserpod.io/blog/browserpod-40/) ⭐️ 6.0/10

BrowserPod 官方宣布 4.0 版本浏览器端 MicroVM 现已免费开放任意使用。当前未明确具体有效期、使用限制、地区限制等规则。

rss · HN Free API / Credits · Nov 16, 12:41

**「为什么重要」** 该工具为面向开发者的浏览器端 MicroVM 工具，免费开放可降低本地运行轻量虚拟机的门槛，但当前规则未完全公开，需留意后续官方说明。

**「可关注」** 可关注：该工具面向开发者提供浏览器端 MicroVM 能力，当前免费规则细节未公开，使用前建议确认官方最新条款。

**Tags**: `#free-tier`, `#dev-tool`, `#promo`

---

<a id="item-ai-deals-2"></a>
### [Supabase Free 周备份工具开源](https://github.com/liulewis/supabase-free-backup-lite) ⭐️ 5.0/10

社区开发者 agricalc 开源 supabase-free-backup-lite 工具，面向 Supabase Free 层项目提供每周自动数据库备份能力，通过 pg\_dump 将备份存储至 Cloudflare R2。工具本身无使用费用，需用户自行托管部署，且需持有独立的 Cloudflare R2 账户，无官方服务背书，无可直接领取的免费额度。

rss · HN Free API / Credits · Nov 17, 01:13

**「为什么重要」** Supabase Free 层官方未提供自动备份功能，该工具可填补该需求空白，但需用户自行承担部署、配置及 R2 存储的相关成本。

**「可关注」** 可关注：仅适合具备自托管能力且已持有 Cloudflare R2 账户的用户使用，无官方支持，需自行处理配置与运维问题。

**Tags**: `#limited-free`, `#free-tier`, `#open-source`

---