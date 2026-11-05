---
layout: default
title: "Horizon Summary: 2026-11-05 (EN)"
date: 2026-11-05
lang: en
---

> From 202 items, 17 important content pieces were selected

---

**Agent Harness Architecture**
1. [Mastra core 1.82.0 发布](#item-harness-arch-1) ⭐️ 7.8/10
2. [pydantic-ai v2.66.0 安全修复发布](#item-harness-arch-2) ⭐️ 6.8/10
3. [gemini-cli v0.67.0 Released](#item-harness-arch-3) ⭐️ 6.8/10

**AI Agent Engineer**
1. [Anthropic 发布 LLM 可证明推理研究](#item-agent-engineer-1) ⭐️ 8.0/10
2. [Cognition 发布 SWE-2 Flash 编码模型](#item-agent-engineer-2) ⭐️ 7.8/10
3. [Kimi K3.1 Pro 权重发布](#item-agent-engineer-3) ⭐️ 7.0/10
4. [ToolSpace 提出工具中心 MCP 环境合成框架](#item-agent-engineer-4) ⭐️ 7.0/10
5. [YANAMI 多模态多轮有状态基准发布](#item-agent-engineer-5) ⭐️ 7.0/10
6. [Dharma 字段提取器 2B 发布](#item-agent-engineer-6) ⭐️ 6.8/10
7. [Route Anything 模型路由框架](#item-agent-engineer-7) ⭐️ 6.0/10
8. [LoCo 本地偏好学习减少推理过度思考](#item-agent-engineer-8) ⭐️ 6.0/10
9. [OpenAI 拟收购 Pierre Computer](#item-agent-engineer-9) ⭐️ 5.5/10

**AI Daily**
1. [OpenAI 自主流水线修复 948 个 Linux 内核提权漏洞](#item-ai-daily-1) ⭐️ 8.8/10
2. [OpenAI 收购 Pierre Computer Co](#item-ai-daily-2) ⭐️ 7.8/10
3. [Daybreak Red 登陆 AWS GovCloud \(US-East\)](#item-ai-daily-3) ⭐️ 6.8/10
4. [Lion-ER-35B-A3B 具身模型发布](#item-ai-daily-4) ⭐️ 5.0/10
5. [ReTerm 探索失败驱动 Code Agent RSI](#item-ai-daily-5) ⭐️ 5.0/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [Mastra core 1.82.0 发布](https://github.com/mastra-ai/mastra/releases/tag/%40mastra/core%401.82.0) ⭐️ 7.8/10

Mastra core 1.82.0 发布，核心升级 Knowledge v2 页面树模型。新增 knowledge.upsertPage\(\)、removePage\(\) 等服务端同步 API，支持向量/混合搜索与长页面分块嵌入。配套只读 Knowledge HTTP 路由、SSE 变更流及 @mastra/client-js 匹配 API，采用 scope/FGA 权限控制。事件化持久化代理修复 API 重启中断问题，后台任务支持断点续传，可观测性新增流式延迟指标。

github · PaulieScanlon · Nov 4, 10:59

**「设计要点」** Knowledge 升级为一级页面树，支持链接索引与分块嵌入。持久化代理跨进程连续性依赖支持 run fencing 的共享存储（如 @mastra/pg 的 PostgresStore）及共享 pubsub，只读 Knowledge 路由采用 scope/FGA 权限门控。

**「改了什么」** Knowledge v2 引入 pages/notes/pins 页面树模型，新增 upsertPage/removePage 等服务端同步 API 及可选向量/混合搜索。事件化持久化代理修复 API 重启中断问题，需共享存储实现跨进程连续性；移除实验性 subconscious 与 knowledge.reindex\(\)，@mastra/temporal 步骤默认校验输入模式。

**Tags**: `#memory`, `#tools`, `#permissions`

---

<a id="item-harness-arch-2"></a>
### [pydantic-ai v2.66.0 安全修复发布](https://github.com/pydantic/pydantic-ai/releases/tag/v2.66.0) ⭐️ 6.8/10

pydantic-ai v2.66.0 发布，核心为 8 项安全修复（2 高危、5 中危、1 低危）及沙箱/记忆/持久化功能扩展。高危修复针对 \`web\_fetch\_tool\` 本地回退的事件循环内存耗尽（GHSA-m5vj-8mcw-82qx）和 harness \`private\_key\` 正则回溯（GHSA-mfx5-pc32-32m8）；中危修复覆盖腾讯云元数据泄露、OpenTelemetry 凭据暴露、AG-UI/DecisionModel schema 指数膨胀、适配器二次复杂度、反序列化文件类型混淆及 allowlist DNS 泄露。新功能包括 \`OpenSandbox\`、\`RenderSandbox\` 自托管工作区，\`Pydantic AI Harness\` 的 Azure Durable Task 持久化，\`Pixeltable\` 工具与记忆存储，\`MCP\` 能力 \`include\_instructions\` 选项，以及 xAI Grok Voice \`output\_speech\_timestamps\` 报告。兼容性变更涉及 Anthropic web 工具直接调用、\`FunctionToolset\(requires\_approval=True\)\` 应用于 \`Tool\` 实例、实时会话指令每轮重新解析及 \`SummarizingCompaction\` 副本识别。

github · adtyavrdhn · Nov 4, 11:51

**「设计要点」** 多个修复指向事件循环阻塞模式：JSON 重缩进、正则回溯、schema 内联展开及二次复杂度均在事件循环同步执行，导致内存或 CPU 耗尽。AG-UI、Vercel AI 适配器及 Temporal/DBOS/Prefect 持久执行是受影响的集成点。

**「改了什么」** v2.66.0 以安全补丁为主：修复 \`web\_fetch\_tool\` 本地回退在事件循环重缩进 JSON 导致的内存耗尽（GHSA-m5vj-8mcw-82qx），以及 harness \`private\_key\` 正则回溯（GHSA-mfx5-pc32-32m8）；同时新增 \`OpenSandbox\`、\`RenderSandbox\` 自托管工作区，\`Pydantic AI Harness\` 的 Azure Durable Task 持久化，\`Pixeltable\` 工具与记忆存储，\`MCP\` 能力 \`include\_instructions\` 选项。

**Tags**: `#tools`, `#permissions`

---

<a id="item-harness-arch-3"></a>
### [gemini-cli v0.67.0 Released](https://github.com/google-gemini/gemini-cli/releases/tag/v0.67.0) ⭐️ 6.8/10

Official release of \`google-gemini/gemini-cli\` v0.67.0. Introduces a bridge between the IDE companion and container sandboxes over exec stdio. Fixes duplicate agent loading when the workspace is the home directory, excludes IDE settings and \`GEMINI.md\` from open file context, and scopes untrusted flag checks to external output. Also addresses A2A server route registration order, RFC 9110 header splitting, and CLI signal handling stability.

github · gemini-cli-robot · Nov 4, 20:27

**「Architecture Note」** The exec stdio bridge lets the IDE companion run inside container sandboxes without opening extra network surfaces. Untrusted flag checks now only fire on external output, and approved flags are remembered for the session, reducing permission prompt noise.

**「What Changed」** Added IDE companion to container sandbox bridging via exec stdio. Fixed duplicate agent loading in home directory workspaces. Excluded IDE settings and \`GEMINI.md\` from open file context. Scoped untrusted flag checks to external output and persisted approvals. Fixed A2A server middleware ordering and RFC 9110 custom header tokenization. Improved atomic \`writeTextFile\` to respect read-only files and hard links.

**Tags**: `#sandbox`, `#runtime`, `#permissions`, `#memory`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [Anthropic 发布 LLM 可证明推理研究](https://www.anthropic.com/research/provable-inference) ⭐️ 8.0/10

2026 年 11 月 4 日，Anthropic 发布基于零知识证明的 LLM 可证明推理研究。社区讨论援引的具体参数包括：90–100 倍计算开销、约 6.5 MB 的承诺文件（有效期约 1600 万次请求）、证明验证在 24 线程下需 17 秒、单线程 21 秒。有评论者指出该工作基于此前 VerInf 项目且引用不足，并对比认为闭源模型提供方采用四家独立推理的概率性证明成本更低，而开源权重模型通过确定性重算仍更快更便宜。

hackernews · ltononro · Nov 4, 17:17 · [Discussion](https://news.ycombinator.com/item?id=50368626)

**「为什么重要」** 该研究提供了闭源 LLM 可证明推理的首批具体性能基准，直接影响 agent 系统对模型输出的验证策略选择。但秒级验证延迟与近百倍计算开销表明，当前方案更适用于离线审计而非实时推理链路。

**「可关注」** 闭源模型可证明推理当前需承受 90–100 倍计算开销与约 17 秒验证延迟，而开源权重模型通过确定性重算仍保持更优成本。

**「评论」** 社区出现对 VerInf 前期工作引用不足的争议，同时就闭源与开源模型验证路径形成技术分歧：一方认为多独立提供方概率证明更廉价，另一方指出开源模型重算无需复杂密码学且速度更快。

**Tags**: `#observability`, `#eval`, `#harness`

---

<a id="item-agent-engineer-2"></a>
### [Cognition 发布 SWE-2 Flash 编码模型](https://cognition.ai/blog/swe-2-flash) ⭐️ 7.8/10

2026年11月4日，Cognition AI 发布编码模型 SWE-2 Flash，基于 Thinking Machines 的 Inkling-Small（276B 总参数、12B 激活参数），首次在训练流程中加入强化学习前的中间训练阶段。官方自测显示，该模型在 Terminal-Bench 4.0 上的得分从基线的 0.9% 提升至 20.0%，FrontierCode 2.0 从 3.2% 提升至 24.0%，网络安全基准 ExploitBench 得分从 11.3% 提升至 34.8%，超过所有美国开源权重模型，甚至性能优于 3 倍参数量的模型。SWE-2 Flash 目前已上线 Devin Desktop 和 CLI，价格为更大模型 SWE-2 的 1/5，速度为 3 倍，但权重暂不公开，仅计划向可信行业伙伴和研究机构安全共享，相关 benchmark 结果尚未经第三方验证。

rss · Cognition Blog · Nov 4, 18:00

**「为什么重要」** 该模型首次在编码模型训练中落地中间训练阶段，官方自测显示其软件工程与网络安全能力均达到当前美国开源模型前列，为编码智能体的模型选型提供了新选项；但相关性能数据尚未经第三方验证，权重共享方案也还未正式落地。

**「可关注」** 可关注：SWE-2 Flash 通过中间训练阶段迭代数据混合、扩充高质量多样化强化学习任务实现性能提升，其训练流程设计可作为编码模型优化的参考。

**Tags**: `#coding-agent`, `#eval`, `#training`, `#llm`

---

<a id="item-agent-engineer-3"></a>
### [Kimi K3.1 Pro 权重发布](https://huggingface.co/moonshotai/Kimi-K3.1-Pro) ⭐️ 7.0/10

2026年11月4日，Moonshot AI在HuggingFace发布Kimi K3.1 Pro开源模型权重，该模型发布后成为HuggingFace热门趋势模型，trendingScore达534，获546个赞。社区讨论围绕本地部署硬件成本、第三方推理服务商吞吐差异、与DeepSeek、Claude的基准对比展开，影响本地模型部署者、推理服务优化者及coding agent研发人员。目前该模型无公开技术报告、架构细节或可复现的评估突破数据。

hackernews · Hugging Face Trending Models · Nov 4, 15:30 · [Discussion](https://news.ycombinator.com/item?id=50366999)

**「为什么重要」** 该模型是近期新发布的开权重大模型，社区已开始围绕实际部署与推理成本展开讨论，但缺乏可复现的评估数据，暂时无法判断其对coding agent等场景的实质提升。

**「可关注」** 可关注：第三方推理服务商（Together、Modal、OpenRouter）的吞吐优化空间，以及该模型在coding agent场景下的实际基准表现，目前尚无公开可复现的评估数据。

**「评论」** 社区观点存在分歧，部分用户质疑其“开源权重”属性，也有用户认为该模型存在刷榜嫌疑，性能未明显超过DeepSeekV4.1-Flash；也有实测用户反馈其作为开源模型表现强劲，适配多数场景；同时讨论指出本地部署需8xB300级别硬件，也有用户通过双RTX PRO 4000搭配NVFP4量化版本运行450k上下文，第三方推理服务商存在明显吞吐差异。

**Tags**: `#coding-agent`, `#eval`, `#orchestration`

---

<a id="item-agent-engineer-4"></a>
### [ToolSpace 提出工具中心 MCP 环境合成框架](https://huggingface.co/papers/2611.05036) ⭐️ 7.0/10

2026-11-05，Hugging Face Daily Papers 推介 arXiv 论文《ToolSpace: Scaling Tool-Centric Environment Synthesis for Long-Horizon Agents》。该论文提出以工具为中心的 MCP 环境合成框架，逆转现有以数据为中心的方法顺序：从真实 MCP 服务执行轨迹与开放智能体语料库中，使用确定性规则挖掘相邻调用的数据、状态与重试依赖，构建加权工具组合图并聚类为环境，再反向合成数据库。相比现有方法，ToolSpace 旨在解决工具接口不匹配、工具组合未基于实际执行、任务难以跨环境等问题。当前摘要内容不完整，未提供性能验证或实现细节，实际效果待确认。

rss · Hugging Face Daily Papers · Nov 5, 03:01

**「为什么重要」** 该框架直接针对 MCP 工具链、agent 评估与长程编排中的环境缩放痛点，但摘要未给出实验数据，实际收益尚未证实。

**「可关注」** 可关注：ToolSpace 用确定性规则从执行轨迹挖掘工具依赖，而非依赖 LLM 生成，这可能降低合成环境中工具接口失配风险。

**Tags**: `#mcp`, `#eval`, `#orchestration`

---

<a id="item-agent-engineer-5"></a>
### [YANAMI 多模态多轮有状态基准发布](https://huggingface.co/papers/2611.05280) ⭐️ 7.0/10

2026年11月5日，Hugging Face Daily Papers发布YANAMI相关论文，这是首个面向多模态多轮有状态交互的大规模数据集与基准，包含YANAMI-400K（40万条多轮多模态对话）和YANAMI-Bench两部分，该论文当日获得27次点赞。现有统一多模态数据集与基准多聚焦单轮任务，即便部分多轮数据集也无需跨轮跟踪信息，无法满足多模态有状态交互对模型理解、维护、更新对话状态的要求。该资源面向构建或评估多轮有状态（尤其是多模态）AI Agent能力的工程师。

rss · Hugging Face Daily Papers · Nov 5, 03:01

**「为什么重要」** 它填补了现有多模态基准在跨轮对话状态跟踪评估上的空白，为AI Agent工程师评估多轮有状态交互能力提供了可用的公开资源。

**「可关注」** 可关注：当前统一多模态模型的评估体系尚未覆盖跨轮对话状态跟踪需求，YANAMI可作为对应能力的验证参考。

**Tags**: `#eval`, `#memory`

---

<a id="item-agent-engineer-6"></a>
### [Dharma 字段提取器 2B 发布](https://huggingface.co/blog/Dharma-AI/dharma-field-extractor) ⭐️ 6.8/10

Hugging Face 的 Dharma AI 团队于 2026-11-04 发布 Dharma Field Extractor，一个 20 亿参数的文档字段提取模型。该模型基于 DharmaOCR-LITE v1.1，通过 LoRA 适配器在 43,384 个训练样本上训练，支持开放提取和 schema 定向提取两种模式，输出结构化 JSON。官方博客称其在 546 份文档、1,638 个测试用例的基准上取得 0.834 的字段级 F1 分数，高于测试的 Claude Opus 5（0.816）和 GPT-5.6 Luna（0.741），单 L40S 上运行成本据称为 frontier API 的 1/6 到 1/147。材料未提供完整技术细节、独立复现数据或生产环境部署指南，性能声明仅基于官方自测基准。

rss · Hugging Face Blog · Nov 4, 17:50

**「为什么重要」** 该模型将文档字段提取从通用 LLM 调用拆分为专用小模型任务，对需要高吞吐、低延迟文档处理的 agent 流水线是可行选项。但成本对比基于自托管 GPU 时间与 API 定价的估算，实际生产环境中的延迟、吞吐和硬件利用率尚未有第三方验证。

**「可关注」** 官方自测显示 2B 参数模型在字段提取任务上质量高于测试的 frontier LLM 且成本更低，但基准方法和自托管成本估算需独立验证。

**Tags**: `#eval`, `#tooling`, `#document-extraction`

---

<a id="item-agent-engineer-7"></a>
### [Route Anything 模型路由框架](https://huggingface.co/papers/2611.05275) ⭐️ 6.0/10

2026-11-05，Hugging Face Daily Papers 收录论文《Route Anything: A Study of Model and Policy Routing for General-Purpose AI Systems》（arXiv:2611.05275）。该论文提出 Route Anything 统一框架，旨在为通用 AI 系统动态选择与协调专门模型、工具和策略，在性能与计算成本间取得平衡。当前材料仅为截断摘要，未披露具体技术细节、性能数据或实现参考，影响做 agent 编排与任务特定资源选择的工程师。需完整论文审查后方可提取可落地的工程见解。

rss · Hugging Face Daily Papers · Nov 5, 03:01

**「为什么重要」** 该论文直接针对 agent orchestration 中的核心张力：如何在异构候选池中动态路由。目前仅确认理论框架存在，尚未证实其在实际系统中的性能收益或部署可行性。

**「可关注」** 可关注：当前公开材料仅包含理论框架描述，无可用代码、基准测试或成本-质量权衡的具体数值，不宜立即纳入生产路由设计。

**Tags**: `#orchestration`

---

<a id="item-agent-engineer-8"></a>
### [LoCo 本地偏好学习减少推理过度思考](https://huggingface.co/papers/2611.04814) ⭐️ 6.0/10

2026 年 11 月 5 日，Hugging Face Daily Papers 收录 arXiv 论文《Think Less, Locally: Local Preference Learning for Reasoning Compression》，提出 LoCo 方法。LoCo 从模型自身推理轨迹中检测候选过度思考状态，冻结对应前缀，重新生成较短验证延续，并以状态条件偏好对通过 DPO 训练，旨在减少长链式思考后的不必要推理。当前公开内容仅为截断摘要，未披露具体性能基准、实现细节或消融实验，因此对 coding agent 推理效率的实际提升幅度尚未证实。

rss · Hugging Face Daily Papers · Nov 5, 03:01

**「为什么重要」** 该工作直接针对 LLM 推理中的过度思考问题，若验证有效，可降低 coding agent 等应用的推理成本。但目前仅见方法框架，缺乏可复现的 benchmark 数据，实际收益仍不确定。

**「可关注」** 可关注：状态条件 DPO 偏好对构造方式，以及冻结前缀与重新生成短延续的具体实现细节，这些将决定该方法在 agent 场景中的可迁移性。

**Tags**: `#coding-agent`, `#reasoning-compression`, `#dpo`

---

<a id="item-agent-engineer-9"></a>
### [OpenAI 拟收购 Pierre Computer](https://openai.com/index/openai-to-acquire-pierre/) ⭐️ 5.5/10

2026年11月4日Hacker News出现二手报道，称OpenAI可能收购运营Code.Storage的Pierre Computer Company，该基础设施被Lovable、Bolt等编码代理用于git格式的代码与产物存储，目前仅有一条推文作为信源，无官方确认。

hackernews · itunpredictable · Nov 4, 15:21 · [Discussion](https://news.ycombinator.com/item?id=50366863)

**「为什么重要」** 若收购落地，OpenAI将直接获得支撑大规模编码代理工作负载的git基础设施能力，可能改变编码代理生态的存储服务供给格局；但目前仅为未证实的传闻，无官方动作。

**「可关注」** 可关注OpenAI后续是否公开git基础设施相关技术规划，以及依赖Code.Storage的编码代理需提前评估服务商变更的合规与可用性风险。

**「评论」** 社区讨论将该传闻与OpenAI此前发布的git扩容文章关联，提及Pierre由Bootstrap原始开发者创立、其diff库获得好评，同时有人关注大厂收购小型工具团队是否是为了获取产品开发过程数据集。

**Tags**: `#coding-agent`, `#harness`, `#orchestration`, `#memory`

---

## AI Daily

<a id="item-ai-daily-1"></a>
### [OpenAI 自主流水线修复 948 个 Linux 内核提权漏洞](https://openai.com/index/a-thousand-fewer-paths-to-root) ⭐️ 8.8/10

OpenAI 宣布构建了一套自主流水线，可自动完成 Linux 内核本地权限提升漏洞的发现、验证与补丁生成。该流水线共处理了 948 个漏洞。这一成果由 OpenAI 官方博客发布，属于实验室向产业输出的技术案例。

rss · OpenAI Blog · Nov 4, 08:00

**「为什么重要」** 这展示了 AI 在自动化安全漏洞修复流程中的端到端能力，从发现到补丁生成无需人工介入。对于维护大规模基础设施的团队，这类自动化工具可显著缩短漏洞响应周期。

**「可关注」** 可关注：自主流水线在 Linux 内核安全维护中实现了漏洞发现、验证、补丁生成的全链路自动化。

**Tags**: `#lab`, `#industry`

---

<a id="item-ai-daily-2"></a>
### [OpenAI 收购 Pierre Computer Co](https://openai.com/index/openai-to-acquire-pierre) ⭐️ 7.8/10

OpenAI 宣布将收购 Pierre Computer Company, Inc.，以扩展 Codex 在代码构建、理解和审查方面的工具能力。目前公开细节有限，仅确认了收购意向与战略方向。

rss · OpenAI Blog · Nov 4, 14:30

**「为什么重要」** 这宗收购表明 OpenAI 正在加码代码 AI 工具链的垂直整合。对做 coding agent 的团队而言，需关注 Codex 能力边界后续如何变化。

**「可关注」** 可关注：Codex 工具链后续的集成节奏与 API 兼容性变化。

**Tags**: `#lab`, `#industry`, `#product`

---

<a id="item-ai-daily-3"></a>
### [Daybreak Red 登陆 AWS GovCloud \(US-East\)](https://openai.com/index/daybreak-red-aws-govcloud) ⭐️ 6.8/10

OpenAI 的 Daybreak Red 服务现已登陆 AWS GovCloud \(US-East\)。客户可通过 Amazon Bedrock 调用 GPT-5.6 Cyber，但需事先获得 OpenAI 批准。该服务仅限用于授权网络安全用途。

rss · OpenAI Blog · Nov 4, 07:00

**「可关注」** 可关注：Daybreak Red 在 AWS GovCloud 的调用入口为 Amazon Bedrock，使用前需完成 OpenAI 客户审批，且模型输出仅适用于预先授权的网络安全工作负载。

**Tags**: `#model`, `#lab`, `#product`, `#industry`

---

<a id="item-ai-daily-4"></a>
### [Lion-ER-35B-A3B 具身模型发布](https://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw==&amp;mid=2247939340&amp;idx=2&amp;sn=25a664251ec6cb5820f1268911de9141) ⭐️ 5.0/10

2026年11月4日，招商局先进技术研究院下属狮子山人工智能实验室发布具身推理视觉语言模型「驭物™ Lion-ER-35B-A3B」。该模型采用MoE混合专家架构，总参数约35B，每Token仅激活约3B参数，研发方宣称其在十项主流具身相关基准上实现全部指标上涨，走不堆砌训练数据的技术路线。当前仅能获取二手报道内容，缺乏官方一手发布信息及可核对的核心细节（如具体基准名称、与同类模型的具体对比数据等）。

rss · 量子位 · Nov 4, 05:33

**「为什么重要」** 具身推理是机器人落地现实场景的核心能力瓶颈，该模型宣称的低激活参数、不依赖海量数据堆砌的技术路线，若验证属实，或为行业提供新的研发思路。

**「可关注」** 可关注：该模型采用的「能力牵引数据闭环迭代」研发路线，以及MoE架构在具身推理场景下的低激活参数表现。

**Tags**: `#model`, `#lab`, `#industry`

---

<a id="item-ai-daily-5"></a>
### [ReTerm 探索失败驱动 Code Agent RSI](https://mp.weixin.qq.com/s?__biz=MzA3MzI4MjgzMw==&amp;mid=2651072104&amp;idx=3&amp;sn=72caa8c3d846ccf53820d188e298acec) ⭐️ 5.0/10

机器之心2026年11月4日发布报道，介绍复旦大学、香港中文大学MMLab、上海交通大学联合提出的ReTerm方法，探索失败驱动的递归自我改进（RSI）路径，使Code Agent可从自身执行错误中进化。该报道为二手行业资讯，暂无官方一手来源可核对。ReTerm核心包含两部分设计：一是构建含约1万条恢复轨迹的ReTerm-10K数据集，由强教师模型在基础模型失败现场生成恢复示范用于冷启动；二是提出ReTerm-GRPO框架，让Agent从自身失败现场尝试多种修复方案，依据任务验证器结果更新参数，形成「遇错-恢复-学习」闭环。在覆盖终端操作与软件工程的三个主要评测中，ReTerm-9B相比基础模型提升超13个百分点。

rss · 机器之心 · Nov 4, 04:00

**「为什么重要」** 当前Code Agent在复杂终端任务中遇错后易陷入重复无效操作，ReTerm的失败驱动RSI路径绕开了人工注入错误、干净环境学习覆盖度不足的问题，为终端智能体自主进化提供了可参考的技术方向。

**「可关注」** 可关注：ReTerm 以 Agent 自身失败现场为训练起点，通过教师模型恢复示范冷启动、在线强化学习迭代的闭环设计，实现终端任务错误恢复能力的持续提升。

**Tags**: `#industry`, `#model`, `#eval`

---