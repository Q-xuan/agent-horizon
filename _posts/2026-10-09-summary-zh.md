---
layout: default
title: "Horizon Summary: 2026-10-09 (ZH)"
date: 2026-10-09
lang: zh
---

> 从 192 条内容中筛选出 17 条重要资讯。

---

**Harness 架构**
1. [openai-agents-js 0.20.0 发布](#item-harness-arch-1) ⭐️ 8.1/10
2. [Codex rust-v0.162.0 发布](#item-harness-arch-2) ⭐️ 8.0/10
3. [FastMCP v4.1.0 发布](#item-harness-arch-3) ⭐️ 7.8/10
4. [Claude Code 2.1.281 发布](#item-harness-arch-4) ⭐️ 7.8/10
5. [Claude Code v2.1.295 发布](#item-harness-arch-5) ⭐️ 7.6/10
6. [OpenHands v1.26.0 发布](#item-harness-arch-6) ⭐️ 6.8/10
7. [agent-framework 1.21.0](#item-harness-arch-7) ⭐️ 6.8/10
8. [Anthropic 开源知识工作插件集](#item-harness-arch-8) ⭐️ 5.2/10

**Agent 工程师日报**
1. [AgentMonBench 与 EBG：长程 Agent 行为监管](#item-agent-engineer-1) ⭐️ 7.2/10
2. [TestPrism 提出多候选测试评测基准](#item-agent-engineer-2) ⭐️ 7.0/10
3. [Trace2Env：基于历史 Trace 模拟交互环境](#item-agent-engineer-3) ⭐️ 6.0/10
4. [ttok 1.0 发布](#item-agent-engineer-4) ⭐️ 5.8/10
5. [ttok 0.4 发布](#item-agent-engineer-5) ⭐️ 5.8/10
6. [Learn2Play Bench 评测 Agent 经验学习能力](#item-agent-engineer-6) ⭐️ 5.8/10

**AI 日报**
1. [LegalOn 削减 Codex 日常预估成本 65%](#item-ai-daily-1) ⭐️ 5.8/10
2. [Oracle 接入 ChatGPT 与 Codex 加速工作流](#item-ai-daily-2) ⭐️ 5.3/10
3. [OpenAI 公布数学证明与多款开源模型发布](#item-ai-daily-3) ⭐️ 5.0/10

---

## Harness 架构

<a id="item-harness-arch-1"></a>
### [openai-agents-js 0.20.0 发布](https://github.com/openai/openai-agents-js/releases/tag/%40openai/agents-core%400.20.0) ⭐️ 8.1/10

OpenAI 发布 @openai/agents-core@0.20.0。该版本将人工审批恢复后的模型调用纳入 maxTurns 计数，避免执行轮数失控。系统同时强化了本地文件工具的 Unix 权限隔离与硬链接保护，并为 MCP 工具自动发现设置了 64 页默认上限。

github · github-actions\[bot\] · 10月8日 23:04

**「设计要点」** 运行时收紧了审批流程与主循环步数的一致性，防止审批恢复绕过步数限制。工具层通过硬链接隔离与父目录写权限校验加固宿主机文件系统，并把多轮并发 run 下的 computer 工具执行严格串行化。

**「改了什么」** 审批恢复后的调用开始扣减 maxTurns 配额，达到上限后必须显式调大参数。MCP 工具自动发现默认限制为 64 页，超大列表需配置 maxListPages。Unix 本地文件工具强制要求可信 Python 3，遵循 runAs 配置，编辑文件时解除硬链接关联以防越权修改，并保留目录 sticky 权限位。已取消会话生成的检查点会自动脱敏未校验的终端输出。

**标签**: `#runtime`, `#tools`, `#mcp`, `#permissions`, `#sandbox`

---

<a id="item-harness-arch-2"></a>
### [Codex rust-v0.162.0 发布](https://github.com/openai/codex/releases/tag/rust-v0.162.0) ⭐️ 8.0/10

OpenAI 发布 Codex rust-v0.162.0。更新引入受信任本地项目的 Git worktree 管理工具，并在 Code Mode 增加可选的排序工具搜索。针对自定义 Responses 兼容模型提供方，新版本支持配置实时联网访问与远程上下文压缩能力。

github · github-actions\[bot\] · 10月8日 18:55

**「设计要点」** 沙箱收紧 Linux 启动时的 deny-glob 掩码逻辑，拒绝可写的沙箱构建可执行文件；网络层支持遵循服务端 Retry-After 标头处理重试逻辑。

**「改了什么」** 支持受信任项目内创建与列出 Git worktree，并允许在 Code Mode 中流式输出已结算的 Promise 结果。修复 Windows 10 盘符访问与沙箱临时目录权限，默认保留 apply\_patch 的 CRLF 换行符。

**标签**: `#runtime`, `#tools`, `#sandbox`, `#mcp`

---

<a id="item-harness-arch-3"></a>
### [FastMCP v4.1.0 发布](https://github.com/PrefectHQ/fastmcp/releases/tag/v4.1.0) ⭐️ 7.8/10

FastMCP 发布 v4.1.0 维护版本，补齐 Python 3.15 支持并集中修复 OpenAPI、代理与鉴权边界。版本引入多项输入收紧策略：恢复 MCP SDK 默认的 30 分钟 HTTP 空闲会话超时，限制技能文件必须在配置目录内解析，OpenAPI 路径参数拒绝 \`.\` 与 \`..\` 片段。MultiAuth 调整客户端 ID 归属隔离，升级需提前清空挂起任务。

github · jlowin · 10月8日 22:56

**「设计要点」** MultiAuth 增加来源限定（source qualification），隔断既有客户端会话与任务归属域。工具搜索正则引擎换用 Pydantic 实现，直接禁用前瞻断言与后向引用。

**「改了什么」** HTTP 会话从永不过期恢复为 30 分钟空闲超时。CodeMode 依赖升至 Monty 1.1 并将 \`max\_duration\_secs\` 参数更名为 \`max\_feed\_duration\_secs\`。CLI 端增加加密 OAuth 凭据持久化存储。

**标签**: `#mcp`, `#tools`, `#permissions`, `#runtime`

---

<a id="item-harness-arch-4"></a>
### [Claude Code 2.1.281 发布](https://code.claude.com/docs/en/changelog#2-1-281) ⭐️ 7.8/10

Claude Code 2.1.281 发布，集中强化应用网关的权限策略与云端合规集成。网关新增 blockReadsOutsideWorkingDirectories 与 disableBypassPermissionsMode 桌面策略，同时在 Amazon Bedrock 上游支持通过 STS 动态委派 IAM 角色 assume\_role 与挂载 Guardrail 护栏。此外，自托管运行环境将超长系统提示词调整为私有文件传递，Auto 模式收紧了沙箱命令的服务端审查门槛。

rss · Claude Code Changelog · 10月8日 19:00

**「设计要点」** 网关层实现细粒度管控，限制跨工作目录读取并支持按开发者会话委派 STS 跨账号角色。Command 与 HTTP 钩子引入 onFailure: &quot;block&quot;，钩子启动失败、超时或异常退出时直接阻断后续执行，杜绝静默穿透。

**「改了什么」** 自托管 runner 将系统提示词参数由命令行明文改为 --system-prompt-file 文件传递，解决超长 prompt 导致启动崩溃问题。Auto 模式对只读和沙箱 shell 命令同样强制等待服务端分类审核，危险 rm 指令等待 2 分钟超时后自动拒绝并给出改写建议。

**标签**: `#permissions`, `#sandbox`, `#runtime`

---

<a id="item-harness-arch-5"></a>
### [Claude Code v2.1.295 发布](https://github.com/anthropics/claude-code/releases/tag/v2.1.295) ⭐️ 7.6/10

Claude Code 发布 v2.1.295。新版为命令与 HTTP hook 增加 fail-closed 阻断模式，支持终端 OSC 7501 状态协议，并为应用网关补齐 upstream 首包耗时控制与模型路由白名单。无人值守重试机制同步补充超时上限参数，控制 429 与 529 异常下的等待周期。

github · ashwin-ant · 10月8日 19:48

**「设计要点」** 安全策略从默认放行转向确定性阻断，配置 \`onFailure: &quot;block&quot;\` 后 hook 启动失败、超时或异常退出均直接拦截调用。网关层引入 \`timeouts.upstream\_ttfb\_ms\` 控制 Bedrock 与 Vertex 等云端 upstream 首包时延，超时自动触发故障切换或返回 502。

**「改了什么」** 新增 hook 失败阻断策略与终端 OSC 7501 状态汇报，网关 upstream 增加 \`models\` 过滤与 TTFB 超时配置。修复远程 MCP 断连死循环重试，并将 \`CLAUDE\_AUTO\_BACKGROUND\_TASKS\` 导致子 agent 与后续命令竞争执行的问题修正。

**标签**: `#runtime`, `#permissions`, `#tools`

---

<a id="item-harness-arch-6"></a>
### [OpenHands v1.26.0 发布](https://github.com/OpenHands/OpenHands/releases/tag/v1.26.0) ⭐️ 6.8/10

OpenHands 发布 v1.26.0，引入系统行为验证工具链 verify-openhands 与 control-openhands CLI。新版本在后端增加了挂起工作区的状态解释与切换路径，同时将聊天交互中的空响应纠偏提示调整为弱提醒展示。

github · openhands-release-bot\[bot\] · 10月8日 20:36

**「设计要点」** 新增的 verify-openhands 将端到端测试拆分为具体的行为映射表与可复现 recipe，通过 harness 直接驱动 CLI 验证并复现缺陷。工作区生命周期管理补齐了挂起态处理，避免连接失效时直接抛错中断。

**「改了什么」** 上线 control-openhands CLI 与日常回归套件，扩充了 20 项核心行为映射。修复了 MCP 服务在重复进行 STDIO 安装时丢失 Catalog 标识的问题，并移除了 stdio 探测失败时不适用的 URL 提示。

**标签**: `#runtime`, `#tools`, `#eval`

---

<a id="item-harness-arch-7"></a>
### [agent-framework 1.21.0](https://github.com/microsoft/agent-framework/releases/tag/python-1.21.0) ⭐️ 6.8/10

microsoft/agent-framework 发布 Python 1.21.0。核心运行时新增工具结果常驻指引（standing guidance）、暴露重写后的变量展开参数，并在流式响应中支持全缓冲的 Purview 策略评估。OpenAI 模块增加最大推理强度配置，并新增 Oracle 原生向量存储 Alpha 连接器。

github · jpalvarezl · 10月8日 10:27

**「设计要点」** 智能体作为工具被嵌套调用时，运行时对 Provider 服务会话状态实施严格隔离，阻断跨层级状态污染。核心调度器在混合同级工具批处理时串行化共享文件写入，并在流式消费提前终止时自动回收 Provider 代理流与会话锁。

**「改了什么」** Anthropic SDK 升级至 1.11 并适配 Bedrock 客户端，修复 Bedrock 跨工具调用丢失 extended-thinking 推理上下文的缺陷。CodeAct 运行时针对缺少 FIDES 安全策略增加告警，并规范 Foundry Agent 工具的生命周期管理。

**标签**: `#runtime`, `#tools`, `#memory`, `#subagents`

---

<a id="item-harness-arch-8"></a>
### [Anthropic 开源知识工作插件集](https://github.com/anthropics/knowledge-work-plugins) ⭐️ 5.2/10

Anthropic 开源 knowledge-work-plugins 仓库。该项目提供面向特定岗位与团队的工作流插件集合，主打 Claude Cowork 并兼容 Claude Code。插件通过定制斜杠命令、工具调用规则与数据源接入，将通用模型调整为垂直岗位助手。

rss · GitHub Trending Daily · 10月9日 05:59

**「设计要点」** 插件规范同时对齐面向办公协作的 Claude Cowork 和面向工程终端的 Claude Code。其交互层依赖斜杠命令分发任务，运行时复用两端既有的工具调用与上下文注入机制。

**标签**: `#tools`, `#subagents`, `#planning`

---

## Agent 工程师日报

<a id="item-agent-engineer-1"></a>
### [AgentMonBench 与 EBG：长程 Agent 行为监管](https://huggingface.co/papers/2610.06406) ⭐️ 7.2/10

该研究针对长程任务中 Agent 动作冗长、证据分散导致的人工核验困难，提出监管基准 AgentMonBench 与无监督结构 EBG。AgentMonBench 面向软件工程场景，划分三个子集，测试需求行为对齐度与关键自主决策识别能力。配套的证据行为图 EBG（Evidence-Grounded Behavior Graph）无需训练，将挂钩源码的证据聚合成行为节点，协助定位需要人工干预的节点。

rss · Hugging Face Daily Papers · 10月9日 00:00

**「为什么重要」** 长程 coding agent 执行数十步操作后，人工逐行审查日志成本过高，全部放行又存在破坏性改动风险。将散落的工具调用与改动聚合为可溯源证据图，能把人工确认范围收敛到高风险决策点，为 harness 的可观测性设计提供了评测标准与实现思路。

**「可关注」** 可关注：构建 human-in-the-loop 拦截机制时，可尝试用免训练的行为图结构聚合底层工具轨迹，替代原始日志流来辅助人工判断。

**标签**: `#observability`, `#eval`, `#coding-agent`, `#harness`

---

<a id="item-agent-engineer-2"></a>
### [TestPrism 提出多候选测试评测基准](https://huggingface.co/papers/2610.12289) ⭐️ 7.0/10

TestPrism 论文指出仅依赖单一参考实现评测测试生成，会显著虚高测试质量。研究团队构建了涵盖 17 个来源、300 个任务及 3000 个候选实现（有效与无效各占半数）的基准，并提出 Joint Success Function 指标：要求生成的测试用例在初始状态报错、放行全部有效实现并拦截全部无效实现。在 14 种 coding agent 配置下，单参考实现的通过率为 59.67%，而 Joint Success Function 仅为 28.00%。

rss · Hugging Face Daily Papers · 10月9日 00:00

**「为什么重要」** 现有测试生成 harness 普遍将单一参考解视作唯一真值，容易漏判过拟合或断言不当的测试。引入正反多候选实现检验后，成功率指标腰斩，暴露了当前 Agent 评测体系的虚高偏差。

**「可关注」** 可关注：构建代码或测试评测 harness 时，引入多种等价解与故障变异体交叉运行，避免用单实现衡量测试集完备性。

**标签**: `#eval`, `#coding-agent`, `#harness`

---

<a id="item-agent-engineer-3"></a>
### [Trace2Env：基于历史 Trace 模拟交互环境](https://huggingface.co/papers/2610.06100) ⭐️ 6.0/10

论文提出 Trace2Env 框架，尝试用语言世界模型 Agent 代替传统可执行环境，实现交互式仿真。在原始系统无法访问但留存交互 Trace 的场景下，该方案无需额外训练，将历史日志重构为包含环境 Schema、事实证据与行为知识的 Worldbook。运行时世界模型 Agent 结合持久化状态检索 Worldbook，为 Task Agent 提供具有状态的模拟交互。

rss · Hugging Face Daily Papers · 10月9日 00:00

**「为什么重要」** Agent 评测常受制于外部真实系统不可复现或调用受限。Trace2Env 探索了直接从历史日志提取环境规则并由模型模拟环境的技术路径，有助于降低离线评测环境的搭建门槛。

**「可关注」** 可关注：从历史交互 Trace 中提取环境 Schema 与状态转移逻辑的做法，评估其在低成本离线 Eval Harness 中的可行性。

**标签**: `#eval`, `#harness`, `#orchestration`

---

<a id="item-agent-engineer-4"></a>
### [ttok 1.0 发布](https://github.com/simonw/ttok/releases/tag/1.0) ⭐️ 5.8/10

Simon Willison 发布 CLI 计数工具 ttok 1.0。新版本将默认 tokenizer 切换为 GPT-5 与 GPT-6 系列使用的 o200k\_base。同时，ttok --list-models 命令开始展示底层 tiktoken 库对 gpt-5\* 等模型前缀的处理方式。

github · simonw · 10月9日 00:34

**「可关注」** 可关注：若在本地脚本或评测 harness 中直接调用 ttok 估算长度，升级 1.0 后默认分词基线会变更为 o200k\_base，需防范与旧模型计数产生偏差。

**标签**: `#harness`, `#observability`, `#eval`

---

<a id="item-agent-engineer-5"></a>
### [ttok 0.4 发布](https://github.com/simonw/ttok/releases/tag/0.4) ⭐️ 5.8/10

Simon Willison 发布命令行分词工具 ttok 0.4 版本。新版允许在计数与截断时直接使用 \`--allow-special\` 参数，方便配合 \`files-to-prompt\` 等输入流水线；新增 \`ttok --list-models\` 列出本地 \`tiktoken\` 支持的模型。运行环境要求提升至 Python 3.10+，打包配置迁移至 \`pyproject.toml\`，文档同步补充了使用 \`o200k\_base\` 编码的较新模型列表。

github · simonw · 10月8日 23:34

**「为什么重要」** 在命令行拼接代码库并估算 token 时，代码内的特殊标记常导致分词器报错退出。计数与截断支持 \`--allow-special\` 后，上下文管道无需前置清洗即可平滑处理特殊文本。

**「可关注」** 若在本地自动化工作流或 CI 中调用 \`ttok\` 控制上下文窗口截断，升级可避免特殊 token 导致的异常中断，但需注意 Python 运行环境是否满足 3.10+ 要求。

**标签**: `#harness`, `#coding-agent`, `#observability`

---

<a id="item-agent-engineer-6"></a>
### [Learn2Play Bench 评测 Agent 经验学习能力](https://huggingface.co/papers/2610.08215) ⭐️ 5.8/10

研究人员提出文本游戏评测基准 Learn2Play Bench，用于评估 LLM Agent 在陌生环境中的经验学习能力。现有基准通常直接在提示词中提供任务规则，或依赖预训练已覆盖的常识，导致难以区分模型是在交互中获取新知还是调用已有先验。该基准通过设计包含全新规则与反直觉机制的文本游戏，并提供可复现的环境反馈，强制 Agent 必须通过交互探索完成学习。

rss · Hugging Face Daily Papers · 10月9日 00:00

**「为什么重要」** 这项工作切断了预训练模型依赖的世界常识先验，为隔离评测 Agent 的上下文探索能力与记忆更新机制提供了受控环境。

**「可关注」** 可关注：构建针对 Agent 探索与适应逻辑的测试集时，可引入反直觉规则作为负例，防止模型仅凭预训练先验“蒙对”执行链路。

**标签**: `#eval`, `#memory`, `#orchestration`

---

## AI 日报

<a id="item-ai-daily-1"></a>
### [LegalOn 削减 Codex 日常预估成本 65%](https://openai.com/index/legalon-halves-codex-costs) ⭐️ 5.8/10

OpenAI 博客披露 LegalOn 的落地案例。LegalOn 在维持开发速度的同时，将日常 Codex 预估成本降低了 65%。团队将 Astra、Sol 与 Luna 等模型按任务匹配分流，并实施了策略性预算管理。

rss · OpenAI Blog · 10月8日 12:00

**「为什么重要」** 案例表明按任务复杂度分流模型并引入预算控制，能在不牺牲研发吞吐的前提下大幅压缩大模型调用开销。

**「可关注」** 可关注：按任务类型将 Astra、Sol 与 Luna 梯队化分流，配合预算管理控制日常推断成本。

**标签**: `#product`, `#industry`, `#lab`

---

<a id="item-ai-daily-2"></a>
### [Oracle 接入 ChatGPT 与 Codex 加速工作流](https://openai.com/index/oracle) ⭐️ 5.3/10

OpenAI 博客发布 Oracle 客户案例。Oracle 在招聘、工程和运营等业务中采用 ChatGPT Work 与 Codex，称其把专业知识沉淀为可复用的工作流，将部分任务耗时从数天压缩至数分钟。该文属于企业合作宣传，未披露具体的技术集成架构与独立评估数据。

rss · OpenAI Blog · 10月8日 16:00

**标签**: `#product`, `#industry`, `#lab`

---

<a id="item-ai-daily-3"></a>
### [OpenAI 公布数学证明与多款开源模型发布](https://lastweekin.ai/p/last-week-in-ai-346-719-math-manuscripts) ⭐️ 5.0/10

Last Week in AI 发布第 346 期周报。OpenAI 公布了来自未发布前沿模型的 719 份数学证明手稿。同时，Mistral 与 Reflection AI 推出开源权重模型，此外行业内再增一起安全团队离职事件。

rss · Last Week in AI · 10月9日 05:06

**「可关注」** 可关注：OpenAI 未发布模型在复杂数学推理上的表现，以及 Mistral 与 Reflection AI 新开源模型的实测基准。

**标签**: `#model`, `#open-source`, `#lab`, `#industry`

---