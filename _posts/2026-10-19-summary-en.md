---
layout: default
title: "Horizon Summary: 2026-10-19 (EN)"
date: 2026-10-19
lang: en
---

> From 159 items, 4 important content pieces were selected

---

**Agent Harness Architecture**
1. [vLLM v0.32.0 发布](#item-harness-arch-1) ⭐️ 7.8/10
2. [fastmcp v4.1.1 安全修复](#item-harness-arch-2) ⭐️ 5.3/10

**AI Agent Engineer**
1. [DeepSeek 搜索 API 定价 $0.75/千次](#item-agent-engineer-1) ⭐️ 7.0/10
2. [llm-echo 0.5 发布](#item-agent-engineer-2) ⭐️ 6.3/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [vLLM v0.32.0 发布](https://github.com/vllm-project/vllm/releases/tag/v0.32.0) ⭐️ 7.8/10

vLLM v0.32.0 正式发布，新增结构化输出端点 \`POST /v1/systemone\`，支持 \`choice\`、\`noul\`、\`score\` 三类决策问题。通用工具与推理解析器（\`--tool-call-parser hf\`、\`--reasoning-parser hf\`）通过读取 checkpoint 的 \`response\_template\` 消除模型专属配置，同时覆盖 Python 与 Rust 前端。低精度 KV 缓存扩展至 NVFP4 支持 SM8x、SM12x、SM90、SM100，ROCm 新增 4-bit \`ultraquant\_4bit\` KV 缓存，GLM-5.x 在 SM100 默认启用 FP8 KV 缓存。Model Runner V2 成为 ROCm 默认运行时，本次发布同时移除 Python 3.10 支持并收紧默认 CORS 策略。

github · khluu · Oct 18, 06:50

**「设计要点」** Model Runner V2 在 ROCm 上成为默认运行时并移除模型专属 MRV1 例外，同时引入 GPU n-gram 推测器与 Elastic EP。服务层通过共享内存张量 arena 向 worker 广播多模态张量，仅需一次拷贝；API 服务器计数大于 1 时采用最少负载连接调度，短请求吞吐提升 43–85%。

**「改了什么」** 新增 \`POST /v1/systemone\` 端点，默认提供结构化决策服务。通用 \`hf\` 解析器覆盖 \`Cloudflare/clef-omni\`、\`LiquidAI/d1-3B\`、DiffusionGemma 等模型，无需模型专属配置。NVFP4 KV 缓存扩展至 SM8x、SM12x、SM90、SM100 及 MiniMax-M3 稀疏注意力，ROCm 获得约 2x 于 FP8 的 4-bit KV 缓存密度。Model Runner V2 成为 ROCm 默认，Python 3.10 支持终止，默认 CORS 来源受限，\`transformers&gt;=5.16.1,&lt;5.20.0\` 与 \`tokenizers&gt;=0.23.2\` 成为硬依赖，\`cascade attention\` 与 \`mamba\_cache\_mode=&quot;all&quot;\` 被移除。

**Tags**: `#runtime`, `#tools`, `#prefix-cache`

---

<a id="item-harness-arch-2"></a>
### [fastmcp v4.1.1 安全修复](https://github.com/PrefectHQ/fastmcp/releases/tag/v4.1.1) ⭐️ 5.3/10

fastmcp v4.1.1 是 PrefectHQ 针对 4.x 系列发布的补丁版本，重点加固安全并修复回归问题。正则工具搜索增加 1000 字符长度上限和约 1 秒执行超时，防止正则表达式拒绝服务攻击。SkillsDirectoryProvider 恢复对链接技能文件夹的发现能力，允许链接指向技能根目录外部，但技能自身文件仍需在链接目标文件夹内解析。其余修复包括：无法解析的代理设置不再中止更新检查，JWKS 刷新锁不再被子类属性干扰。

github · zzstoatzz · Oct 18, 02:12

**「改了什么」** 相对 v4.1.0，本次补丁为 regex 工具搜索增加长度与时间边界，恢复链接技能文件夹发现能力，修复代理设置解析失败中断更新检查，以及 JWKS 刷新锁继承问题。

**Tags**: `#tools`, `#permissions`, `#mcp`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [DeepSeek 搜索 API 定价 $0.75/千次](https://api-docs.deepseek.com/guides/search/) ⭐️ 7.0/10

DeepSeek 官方发布 Search and Fetch API 文档，定价为每 1000 次成功请求 0.75 美元，面向 AI agent 提供网页搜索与抓取能力。该定价显著低于同期付费搜索 API 提供商 Brave（$5/千次）和 Kagi（$12/千次）。目前仅公开定价与接口基础信息，未披露请求限制、可用区域、结果质量等其他细节，对做 coding agent 工具链的工程师而言是新增的低成本网页搜索选项。

hackernews · fagnerbrack · Oct 18, 06:50 · [Discussion](https://news.ycombinator.com/item?id=50138531)

**「为什么重要」** 已发生的变化是提供了比现有主流付费搜索 API 低 85% 以上的成本选项，可直接接入 agent 网页搜索工具链；尚未证实的影响是该 API 的实际请求稳定性、搜索结果相关性、合规性均无公开验证，成本优势能否落地到实际生产环境还需进一步测试。

**「可关注」** 可关注：该 API 的请求成功率统计规则、返回结果的结构化程度，以及是否支持自定义爬取规则，这些参数会直接决定接入现有 agent 工具链的改造成本。

**「评论」** 评论中部分用户认为自托管方案（如 searxng-ai-kit）无需付费且更灵活，是更优替代；也有用户推测未来搜索 API 价格可能走低甚至出现厂商付费提供接口的竞争局面；另有用户指出这类付费搜索服务存在的前提是谷歌未开放付费搜索 API。

**Tags**: `#coding-agent`, `#orchestration`, `#permissions`

---

<a id="item-agent-engineer-2"></a>
### [llm-echo 0.5 发布](https://github.com/simonw/llm-echo/releases/tag/0.5) ⭐️ 6.3/10

2026年10月18日，simonw发布llm-echo 0.5版本，该版本最低依赖LLM &gt;= 0.36，新增对reasoning tokens的支持，同时更新模拟token计数逻辑，将tool calls、reasoning text、system prompts纳入统计范围。

github · simonw · Oct 18, 23:16

**「为什么重要」** 该更新完善了无真实LLM调用的调试场景下的token统计维度，可辅助开发者更准确估算包含工具调用、推理过程的prompt总消耗，对agent可观测性与成本预估有参考价值。

**「可关注」** 可关注无真实LLM参与的调试场景下，模拟token统计规则与真实计费规则的差异，避免估算偏差。

**Tags**: `#observability`, `#eval`, `#coding-agent`

---