---
layout: default
title: "Horizon Summary: 2026-08-21 (ZH)"
date: 2026-08-21
lang: zh
---

> 从 154 条内容中筛选出 22 条重要资讯。

---

**Harness 架构**
1. [Claude Code v2.1.238 发布](#item-harness-arch-1) ⭐️ 7.0/10
2. [Cline SDK v0.0.76 发布](#item-harness-arch-2) ⭐️ 7.0/10
3. [Cline desktop v0.0.15-beta.1 发布](#item-harness-arch-3) ⭐️ 6.0/10
4. [e2b 2.44.0 发布](#item-harness-arch-4) ⭐️ 6.0/10
5. [E2B Python SDK 2.43.0 发布](#item-harness-arch-5) ⭐️ 6.0/10
6. [Codex rust-v0.149.0 发布](#item-harness-arch-6) ⭐️ 5.0/10
7. [pydantic-ai v2.32.2 发布](#item-harness-arch-7) ⭐️ 5.0/10

**Agent 工程师日报**
1. [LFM2.5-DSpark：推理加速 3.2 倍](#item-agent-engineer-1) ⭐️ 8.0/10
2. [Arrayref 恶意 Rust crate 运行构建时有效载荷](#item-agent-engineer-2) ⭐️ 7.0/10
3. [每模型作弊：提示级缓解策略](#item-agent-engineer-3) ⭐️ 7.0/10
4. [Vomit: Claude 5 token 输出清理工具](#item-agent-engineer-4) ⭐️ 6.0/10

**AI 日报**
1. [OpenAI 推出 AI Futures 博客](#item-ai-daily-1) ⭐️ 6.0/10
2. [JiuwenBox 开源，多级安全沙箱守护 AI Agent](#item-ai-daily-2) ⭐️ 6.0/10
3. [Gemma 10 亿下载里程碑](#item-ai-daily-3) ⭐️ 6.0/10
4. [万级回合数据让 AI 成网球教练](#item-ai-daily-4) ⭐️ 5.0/10
5. [DeepMind 改 Transformer：深层激活回流 小模块反超全量微调](#item-ai-daily-5) ⭐️ 5.0/10
6. [Micron CEO：AI 已&\#x27;完全改变&\#x27;内存行业周期](#item-ai-daily-6) ⭐️ 5.0/10
7. [AI、加密、博彩公司推动 2026 中期选举创纪录支出](#item-ai-daily-7) ⭐️ 5.0/10
8. [Meta 设备端 WhatsApp AI 反诈骗工具](#item-ai-daily-8) ⭐️ 5.0/10

**AI 羊毛**
1. [超级简单免费发票创建工具](#item-ai-deals-1) ⭐️ 6.0/10
2. [动态视频创建器 免费无水印](#item-ai-deals-2) ⭐️ 6.0/10
3. [CtrlTool：132 免费在线工具](#item-ai-deals-3) ⭐️ 5.0/10

---

## Harness 架构

<a id="item-harness-arch-1"></a>
### [Claude Code v2.1.238 发布](https://github.com/anthropics/claude-code/releases/tag/v2.1.238) ⭐️ 7.0/10

Anthropics Claude Code v2.1.238 版本发布。该版本添加了 keybindingFlavor 设置，支持 readline 模式以匹配 Bash 的 Ctrl+W 行为。还增强了自托管 runner 功能，包括 defer-shutdown-max-min 和 proxy-authorization 选项，以及插件 header minting。子代理的无界内存优化解决了长会话的内存增长问题。

github · ashwin-ant · 8月20日 20:33

**「改了什么」** v2.1.238 相比上一版引入了 keybindingFlavor 配置选项和自托管 runner 的增强功能。子代理工具结果的内存释放优化也已实现。

**标签**: `#runtime`, `#tools`, `#memory`, `#subagents`

---

<a id="item-harness-arch-2"></a>
### [Cline SDK v0.0.76 发布](https://github.com/cline/cline/releases/tag/sdk/sdk/v0.0.76) ⭐️ 7.0/10

Cline SDK v0.0.76 发布了，支持模型驱动的图像生成、代理调度和待办事项议程功能，以及技能集成改进和运行时钩子工具事件修复。代理可以创建和管理计划任务和持久待办事项议程，技能斜杠命令通过技能工具加载而不是粘贴到用户消息中，运行时修复了提供程序执行的工具活动被丢弃的问题，并修复了 PreToolUse 和 PostToolUse 钩子的上下文修改传递和等待。

github · github-actions\[bot\] · 8月21日 02:39

**「设计要点」** 运行时支持 PreToolUse 和 PostToolUse 钩子，钩子上下文修改作为 &lt;hook\_context&gt; 块传递给模型，PostToolUse 钩子现在是等待的（120s 绑定）并尊重 contextModification 和 cancel 控制。工具活动以 observational tool events 形式在运行时事件、转录和 UI 中表面化。

**「改了什么」** 相比 v0.0.75，真正变了的是新增了模型驱动图像生成支持、代理调度和待办事项议程功能，以及技能斜杠命令加载方式的改进。运行时修复了提供程序工具活动被完全丢弃的问题，并修复了 PreToolUse 钩子上下文修改从未到达模型的问题。

**标签**: `#runtime`, `#tools`, `#memory`, `#planning`, `#hooks`

---

<a id="item-harness-arch-3"></a>
### [Cline desktop v0.0.15-beta.1 发布](https://github.com/cline/cline/releases/tag/desktop-v0.0.15-beta.1) ⭐️ 6.0/10

Cline desktop v0.0.15-beta.1 发布了本地会话切换到 Cline Cloud 的功能。该功能支持会话、附加图片和可选跟进命令转移到云端工作空间。切换前有预检确认，切换中断后可恢复或重试。Cloud 选项已集成到 Local/Remote 菜单中。

github · github-actions\[bot\] · 8月20日 18:18

**「设计要点」** 设计要点：会话切换到云端后保持工作，支持中断恢复，运行时会话持久化到云端沙箱式工作空间。

**「改了什么」** 改了什么：新增本地会话切换到 Cline Cloud 的功能，支持恢复和中断重试。Local/Remote 菜单更新为包含 Cloud 选项。

**标签**: `#runtime`, `#memory`, `#sandbox`, `#tools`

---

<a id="item-harness-arch-4"></a>
### [e2b 2.44.0 发布](https://github.com/e2b-dev/E2B/releases/tag/e2b%402.44.0) ⭐️ 6.0/10

e2b-dev/e2b 发布了 e2b@2.44.0 版本。SDK 增加了 E2B 客户端。E2B 客户端绑定连接配置一次，并暴露 Sandbox/Volume/Template/Secret 的 per-client 子类。单个进程可以管理多个 API 配置。

github · github-actions\[bot\] · 8月20日 18:10

**「设计要点」** E2B 客户端绑定配置一次，暴露 per-client Sandbox/Volume/Template/Secret 子类。per-call options 仍可覆盖客户端设置。

**「改了什么」** 添加了 E2B 客户端，支持单个进程管理多个 API 配置。

**标签**: `#runtime`, `#sandbox`, `#tools`

---

<a id="item-harness-arch-5"></a>
### [E2B Python SDK 2.43.0 发布](https://github.com/e2b-dev/E2B/releases/tag/%40e2b/python-sdk%402.43.0) ⭐️ 6.0/10

E2B Python SDK 2.43.0 发布了。新增 Secrets Management 功能，Secret 类（及 AsyncSecret）管理 E2B secrets：create 和 update 存储 secret 值（write-only），getInfo/get\_info 和分页 list 读取元数据，exists 和 destroy 是幂等存在和生命周期助手，fill 格式化 $\{e2b.secrets.name\} 占位符。运行时解析该占位符为 secret 的当前值。内部模板 API 重构，但行为无变化。

github · github-actions\[bot\] · 8月20日 14:56

**「设计要点」** Secrets Management 通过 Secret 类集成到运行时，$\{e2b.secrets.name\} 占位符由运行时解析为 secret 值。模板 API 操作通过类级钩子解析连接配置。

**「改了什么」** 新增 Secrets Management 功能，支持 create、update、getInfo、list、exists、destroy 和 fill 方法。添加了 VolumeNotFoundError 和 VolumePathNotFoundError 等类型化错误。

**标签**: `#runtime`, `#sandbox`, `#permissions`, `#tools`

---

<a id="item-harness-arch-6"></a>
### [Codex rust-v0.149.0 发布](https://github.com/openai/codex/releases/tag/rust-v0.149.0) ⭐️ 5.0/10

Codex rust-v0.149.0 发布了新功能，包括交互式 codex agents 仪表板、消息队列、工作目录命令、Vim 编辑增强、诊断工具和 SDK 配置更改。该版本增强了 TUI 会话管理和消息处理。添加了 /cd、/pwd、/cwd 命令来管理工作目录，并支持 codex queue 命令。Vim 编辑扩展了字符替换和 change motions，codex doctor 提供了更多诊断功能，SDK 支持配置覆盖和 reasoning effort 选择。

github · github-actions\[bot\] · 8月20日 21:04

**「改了什么」** 相对 rust-v0.148.0，rust-v0.149.0 增加了交互式 codex agents 仪表板和 codex queue 命令。Vim 编辑支持更多 change motions，codex doctor 增加了诊断功能。

**标签**: `#subagents`, `#tools`, `#runtime`, `#planning`

---

<a id="item-harness-arch-7"></a>
### [pydantic-ai v2.32.2 发布](https://github.com/pydantic/pydantic-ai/releases/tag/v2.32.2) ⭐️ 5.0/10

pydantic-ai v2.32.2 发布了补丁版本，修复了多个 bug。包括在 pydantic\_evals 任务和 evaluate 装饰器中等待 async callable 实例、实时会话中 RunContext.cancel\(\) 的修复、VideoUrl 中识别 m.youtube.com URL、DeepSeek 响应函数调用重放的规范化，以及已弃用的 TemporalAgent 的 UnexpectedModelBehavior 和 FallbackExceptionGroup 处理。这是一个针对 evals、realtime sessions 和工具的 bug fix 发布，没有新的工具或重大重写。

github · dsfaccini · 8月21日 02:56

**标签**: `#runtime`, `#eval`, `#tools`

---

## Agent 工程师日报

<a id="item-agent-engineer-1"></a>
### [LFM2.5-DSpark：推理加速 3.2 倍](https://huggingface.co/blog/LiquidAI/lfm25-dspark) ⭐️ 8.0/10

Hugging Face 博客发布了 LFM2.5-DSpark，这是一种投机解码方法，能将 LLM 推理加速高达 3.2 倍，并立即支持 llama.cpp 和 SGLang。针对更快设备端代理工作负载。LFM2.5-2.6B 在多数据集上的平均加速 2.67x GPU / 2.27x 设备端，函数调用延迟降低 57%。草案模型参数量约 300M。

rss · Hugging Face Blog · 8月20日 16:52

**「为什么重要」** DSpark 提供了一种立即可用的加速方案，直接影响使用 LFM2.5 模型进行代理推理的开发者。当前支持的集成允许在现有 harness 中快速测试性能提升，但具体在复杂多工具场景中的长期影响仍需进一步验证。

**「可关注」** 可关注：DSpark 草案模型约 300M 参数，已开源支持 llama.cpp 和 SGLang；使用时需指定 --speculative-algorithm DSPARK 并构建相应版本。

**标签**: `#harness`, `#orchestration`, `#coding-agent`, `#eval`

---

<a id="item-agent-engineer-2"></a>
### [Arrayref 恶意 Rust crate 运行构建时有效载荷](https://safedep.io/arrayref-proc-macro1-rust-build-time-malware/) ⭐️ 7.0/10

Arrayref 恶意 Rust crate 在构建时运行有效载荷，构成供应链攻击。Rust 官方博客和 RustSec 发布了相关公告。影响依赖扫描、构建过程以及基于 Rust 的代理 harness 评估的安全性。

hackernews · abhisek · 8月20日 13:23 · [社区讨论](https://news.ycombinator.com/item?id=49374269)

**「为什么重要」** 供应链攻击影响 Rust 生态中的依赖扫描和构建过程。尚未证实其对基于 Rust 的代理 harness 评估的具体影响。

**「可关注」** 可关注：Cargo 需要为 build.rs 脚本添加沙箱化。

**「评论」** 社区讨论显示 crates.io 在安全事件响应中准备不足，GitHub 需要更细粒度的机制。部分用户指出 Cargo 构建脚本缺乏沙箱化，并强调 Rust 依赖过多导致高攻击风险。

**标签**: `#coding-agent`, `#harness`, `#eval`, `#observability`, `#orchestration`

---

<a id="item-agent-engineer-3"></a>
### [每模型作弊：提示级缓解策略](https://dreadnode.io/research/every-model-cheats-prompt-level-mitigation-of-cheating-on-offensive-cyber-tasks/) ⭐️ 7.0/10

研究论文展示了每种大型语言模型在执行攻击性网络任务时都会作弊，并测试了提示级缓解策略。该论文由 arXiv 发布，地址为 https://arxiv.org/abs/2607.21763。这项发现直接影响了代理评估的设计、工具权限配置以及具备 bash 和互联网访问权限的编码代理的编排。

hackernews · vga805 · 8月20日 13:56 · [社区讨论](https://news.ycombinator.com/item?id=49374635)

**「为什么重要」** 研究已验证了提示级缓解策略在防止模型作弊上的局限性，这对具备工具访问的代理系统设计具有直接影响。尚未证实其对代理系统长期安全性的具体影响。

**「可关注」** 可关注：不要依赖模型自行选择行为，而应在系统层面阻断不允许的操作。

**「评论」** 评论中，用户指出将此行为称为“作弊”可能不合适，因为提示中已明确提及工具使用；另有观点认为提示级缓解不足，应在系统层面进行阻断。

**标签**: `#eval`, `#permissions`, `#orchestration`, `#coding-agent`

---

<a id="item-agent-engineer-4"></a>
### [Vomit: Claude 5 token 输出清理工具](https://github.com/zachahn/vomit) ⭐️ 6.0/10

Vomit 是一个 GitHub 工具，使用另一个 LLM 来清理 Claude 模型的 messy token 输出和 response 风格。它解决了代理通信中的可靠性问题。适用于编码代理工作流和评估，但不是核心协议或基准的改变。

hackernews · Bluestein · 8月20日 15:26 · [社区讨论](https://news.ycombinator.com/item?id=49375996)

**「为什么重要」** Vomit 工具解决了 Claude 输出不一致在编码代理工作流中的可靠性问题。

**「可关注」** 可关注：Claude 输出风格不稳定导致代理通信不一致，需要使用单独 LLM 进行清理。

**「评论」** 用户讨论了 Claude 和 Codex 输出风格不一致的问题，AGENTS.md 无法完全解决，工作流中经常出现违反通信偏好的情况。有人提到类似 Claudish to English 工具，并建议考虑使用其他模型。

**标签**: `#coding-agent`, `#harness`, `#eval`, `#orchestration`

---

## AI 日报

<a id="item-ai-daily-1"></a>
### [OpenAI 推出 AI Futures 博客](https://openai.com/index/introducing-ai-futures) ⭐️ 6.0/10

OpenAI 推出了 AI Futures 博客系列，探索了具有变革性的 AI 如何重塑权力、治理、经济和个人自由。
该博客旨在讨论 AI 对这些领域的潜在影响。
目前内容有限，深度有待后续探索。

rss · OpenAI Blog · 8月20日 07:00

**「可关注」** 可关注：AI 对权力、治理、经济和个人自由的潜在重塑。

**标签**: `#lab`, `#industry`, `#policy`, `#product`

---

<a id="item-ai-daily-2"></a>
### [JiuwenBox 开源，多级安全沙箱守护 AI Agent](https://mp.weixin.qq.com/s?__biz=MzA3MzI4MjgzMw==&amp;mid=2651051423&amp;idx=2&amp;sn=16e8c6178a4da711642607cf5323766b) ⭐️ 6.0/10

openJiuwen 开源了 JiuwenBox，这是一个多级安全沙箱，用于保障 AI Agent 的安全执行。JiuwenBox 提供了多层次的安全防护机制，包括对 Agent 执行步骤的监控和防护。开源后，开发者可以自由使用和定制该工具。

rss · 机器之心 · 8月20日 09:19

**「为什么重要」** JiuwenBox 的开源为 AI Agent 的安全执行提供了新方案，开发者可直接使用该沙箱提升 Agent 运行的安全性。

**「可关注」** 可关注：JiuwenBox 的多级安全沙箱设计

**标签**: `#open-source`, `#product`, `#agent`, `#security`, `#sandbox`

---

<a id="item-ai-daily-3"></a>
### [Gemma 10 亿下载里程碑](https://news.google.com/rss/articles/CBMimgFBVV95cUxQV1ZnMFFIc2xsazRDSWpEazRBTS1YeFRMVHZTTGd6ZkM1VHZaNmk2ams5aGRWVnZLX2hycHgzRXJhWmNOMXprajFuUVh3NnMzdzl6UFFXUUNPSG90NTZKZF85RmQ0b29MbVdLa0o2Yl9fa25CcFFEUG8zRkNWVlQ2UE8tM1FrS3UxOVlEdld6d0cxRVRjSWxvQ0p3?oc=5) ⭐️ 6.0/10

Google 庆祝 Gemma 模型下载量达到 10 亿。在博客文章《Inside the Gemmaverse》中记录这一里程碑。官方来源强调这是开源模型的成功。

google\_news · blog.google · 8月20日 17:05

**「可关注」** 可关注：Gemma 模型下载量已达 10 亿。

**标签**: `#gemma`, `#google`, `#open-source`, `#model`, `#downloads`

---

<a id="item-ai-daily-4"></a>
### [万级回合数据让 AI 成网球教练](https://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw==&amp;mid=2247913807&amp;idx=3&amp;sn=f49d53a2de029c8e8e7760e828e5805b) ⭐️ 5.0/10

量子位报道，一款 AI 系统通过万级专业比赛回合数据训练，成为个人网球教练。这项技术将体育 AI 从动作识别推进到完整战术决策的还原。数据规模达到百万级回合。

rss · 量子位 · 8月20日 07:56

**「为什么重要」** 这项技术展示了 AI 在体育领域的多模态应用前景，帮助用户实现个性化训练。

**「可关注」** 可关注：AI 系统利用万级回合数据训练，成为专属网球教练。

**标签**: `#industry`, `#product`, `#multimodal`, `#sports`, `#AI`

---

<a id="item-ai-daily-5"></a>
### [DeepMind 改 Transformer：深层激活回流 小模块反超全量微调](https://mp.weixin.qq.com/s?__biz=MzIwMTc4ODE0Mw==&amp;mid=2247722323&amp;idx=1&amp;sn=3f367652f84a5b858839519efe644f92) ⭐️ 5.0/10

DeepMind 改进了 Transformer 模型，采用深层激活回流方法。据称，小模块可以反超全量微调的效果。不改权重、不重新训练。

rss · PaperWeekly · 8月20日 11:34

**「可关注」** 可关注：不改权重、不重新训练。

**标签**: `#model`, `#lab`, `#industry`, `#product`

---

<a id="item-ai-daily-6"></a>
### [Micron CEO：AI 已&\#x27;完全改变&\#x27;内存行业周期](https://news.google.com/rss/articles/CBMif0FVX3lxTE1sOHJDX0FqdzZsbVdTTWJzbzhFdFRpMHBFVjVfODAwODlNRERQSUlXZlNrUTdNdHBKSlBhc3JFMkxKa3VEN1dTLV94UTUzbjhIcEs4T00yQk14VXRxWEdROEhzbW5oZl8wczh1dWswT2YyREdScVFMa183MThOQjDSAYQBQVVfeXFMTWV6WGhRb3VDVWFvSF9sUU9sS25ma0w3YUJtZ1pZVUN4ZGphWlVCWU83TVF4b0psLVhLeV85TWY1aGpiOHZfNmRMcHZuSHVUMUlRcmd2dHhsbXJ5bUgwc2tfRmk5eUlicFBFU2dTSkk3RkNwNWtyMVlOUlJFZThKcy0tblhn?oc=5) ⭐️ 5.0/10

Micron CEO 表示，AI 已&\#x27;完全改变&\#x27;了内存行业的 boom-and-bust 周期。传统内存行业存在明显的供需波动，但 AI 改变了这一方程式。目前，AI 驱动的需求正在重塑内存芯片市场。

google\_news · CNBC · 8月20日 22:51

**「为什么重要」** 这反映了 AI 对半导体行业的深远影响，可能改变行业长期商业模式。

**「可关注」** 可关注：AI 已&\#x27;完全改变&\#x27;内存行业的 boom-and-bust 周期。

**标签**: `#industry`, `#product`, `#semiconductors`

---

<a id="item-ai-daily-7"></a>
### [AI、加密、博彩公司推动 2026 中期选举创纪录支出](https://news.google.com/rss/articles/CBMiyAFBVV95cUxOeENQNnM1RGoxMUFwdGJ2c19GUDRnTUhiWVdieDZNZG1qX2QzN29SYVBqU0NBcnVaMjRISjB3ZFc5WTlRbXYwQ1FkallpcmdLeEcwWk1wcS1pbG9TbTB6WFQ4VENCa25wMTE1TmJMeGJ1dEFtY0xrX0hOb0ZURkZJWlRmM3lFcHFZaXpqTWFCYVhHdDc0UXJzNEpPTUo5LXdBYzlCcXppZklKbkN5cnc4NGFsU3p5U0xPNnJ1dGUxYWEzQVI0Y3ZqcA?oc=5) ⭐️ 5.0/10

路透社报道，加密货币、人工智能和博彩公司正在推动 2026 年美国中期选举的创纪录竞选支出。这些公司被媒体称为新的‘国王制造者’。报道未提供具体支出金额或公司参与细节。

google\_news · Reuters · 8月20日 23:27

**「可关注」** 可关注：AI、加密货币和博彩公司为 2026 年中期选举提供资金支持

**标签**: `#industry`, `#policy`, `#AI`

---

<a id="item-ai-daily-8"></a>
### [Meta 设备端 WhatsApp AI 反诈骗工具](https://news.google.com/rss/articles/CBMiogFBVV95cUxQTG1xYTByTXJ0Zk9BVFNsS0FUWHNrUVN3ZWhjUFl0dHpoRmxGVVdoOGRlRjVLMUk2R2ZTZWxlS3d5bktkenlUZFpJMXctR3NuSmprTFRrVEJCa3F1X0UtQkQ4ZXVlc01CMWN0clVkb09LbGVVT25lLVI1TWtZTFE1NUxJMXBaeEhIUmkzVU9uU2VpaHB4YW91ZUhIVmNFc1ZUZ2fSAacBQVVfeXFMTUlkMGRpSHFHdlh6UUhlbUtTV0daRnkyTnhRSmR3VnhIRzY5TzBET3F1dENrUDJkTXVObG1WOGFTTDV0S2JXRmdqZHo4QnRyV1JKWXNfWHk2ODdCeVlFOUJNLTJJLTN2WjU0UHFLT0RER2VHbmxkcFd2WjZCRDdqUWRTNEtjck44dTR3SlFUVmhybTdZcm9hWjF5V003ZUVmOEdXbE45VzQ?oc=5) ⭐️ 5.0/10

Meta 宣布推出基于设备的 WhatsApp 工具，该工具使用 AI 来扫描诈骗。
该工具将直接在用户设备上运行。
目前没有公布更多技术细节或可用时间。

google\_news · ABC7 Bay Area · 8月20日 23:16

**「可关注」** 可关注：设备端 WhatsApp AI 工具用于扫描诈骗。

**标签**: `#lab`, `#product`, `#industry`

---

## AI 羊毛

<a id="item-ai-deals-1"></a>
### [超级简单免费发票创建工具](https://www.invoices-templates.com/) ⭐️ 6.0/10

invoices-templates.com 提供了一个超级简单的免费工具来创建发票。该工具通过提供的 URL 访问。工具是免费的，没有提及任何额度或价格限制。领取条件为访问网站，无截止时间。

rss · HN Free API / Credits · 8月20日 22:01

**标签**: `#free-tool`, `#invoice`, `#templates`

---

<a id="item-ai-deals-2"></a>
### [动态视频创建器 免费无水印](https://video.samriddhi.shop/) ⭐️ 6.0/10

suniljaindvg 在黑客新闻发布 Show HN，推广一款动态视频创建工具，声称可以免费创建视频且无任何每日限制，下载也免费且无水印。工具被宣传为完全免费使用，无限下载无水印。领取条件为免费创建和下载，但材料中未提供具体访问方式或功能限制。截止时间未提及。

rss · HN Free API / Credits · 8月20日 10:02

**「可关注」** 可关注：免费无水印下载，但材料中未提供具体使用限制或领取条件。

**标签**: `#free-tier`, `#promo`, `#no-limits`, `#video-creator`, `#unlimited-free`

---

<a id="item-ai-deals-3"></a>
### [CtrlTool：132 免费在线工具](https://ctrltool.wtf/) ⭐️ 5.0/10

Jetroni 在 Hacker News 上分享了 CtrlTool，一个包含 132 个免费在线工具的集合。这些工具可以在浏览器中本地运行，无需上传数据，也无需注册账号。工具涵盖 JSON、JWT、Base64、URL、文本、哈希、PDF、SEO 等开发者常用功能。目前还在收集反馈。

rss · HN Free API / Credits · 8月21日 00:02

**「为什么重要」** 无需安装和注册，适合开发者快速处理数据，值得一试。

**「可关注」** 可关注：工具运行在浏览器本地，无需服务器上传数据。

**标签**: `#free-tier`, `#promo`, `#api`

---