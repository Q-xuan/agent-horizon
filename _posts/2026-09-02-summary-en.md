---
layout: default
title: "Horizon Summary: 2026-09-02 (EN)"
date: 2026-09-02
lang: en
---

> From 210 items, 19 important content pieces were selected

---

**Agent Harness Architecture**
1. [LangChain 1.4.0a3 发布](#item-harness-arch-1) ⭐️ 7.8/10
2. [Graphiti mcp-v1.1.0 发布](#item-harness-arch-2) ⭐️ 7.8/10
3. [Claude Code 2.1.257 Released](#item-harness-arch-3) ⭐️ 7.8/10
4. [Codex rust-v0.152.0 发布](#item-harness-arch-4) ⭐️ 6.8/10
5. [Pydantic AI v2.37.0 Released](#item-harness-arch-5) ⭐️ 6.8/10
6. [Gemini CLI v0.59.0-preview.0 released](#item-harness-arch-6) ⭐️ 6.8/10
7. [Cline desktop-v0.0.22-beta.1 released](#item-harness-arch-7) ⭐️ 5.8/10
8. [browser-use/video-use GitHub trending](#item-harness-arch-8) ⭐️ 5.0/10

**AI Agent Engineer**
1. [BenchMIRT: What are LLM benchmarks actually measuring?](#item-agent-engineer-1) ⭐️ 7.8/10
2. [@huggingface/kernels: 200+ WebGPU Kernels for Local AI](#item-agent-engineer-2) ⭐️ 7.8/10
3. [Claude Fable 5.1 和 Claude Mythos 5.1 发布](#item-agent-engineer-3) ⭐️ 7.0/10
4. [CogEvol: 高效可靠学习环境生成](#item-agent-engineer-4) ⭐️ 7.0/10
5. [Lies We Can See: Joint Verbal and Non-Verbal Deception by VLM Agents](#item-agent-engineer-5) ⭐️ 7.0/10
6. [Super Library Agent 论文](#item-agent-engineer-6) ⭐️ 6.0/10
7. [Gemini agentic video understanding 发布](#item-agent-engineer-7) ⭐️ 5.8/10

**AI Daily**
1. [Anthropic Announces Enterprise Frontier Safeguards](#item-ai-daily-1) ⭐️ 8.8/10
2. [Astra 首达关键网络安全能力门槛](#item-ai-daily-2) ⭐️ 7.8/10
3. [ChatGPT Connects to EHR and Healthcare Data](#item-ai-daily-3) ⭐️ 7.8/10
4. [AI-Native Companies Turn Workflows Into Operating Capability](#item-ai-daily-4) ⭐️ 6.8/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [LangChain 1.4.0a3 发布](https://github.com/langchain-ai/langchain/releases/tag/langchain%3D%3D1.4.0a3) ⭐️ 7.8/10

LangChain 1.4.0a3 is the third alpha of the 1.4.0 line. It adds \`langchain.mcp\` to adapt MCP servers into LangChain tools. \`MCPAdapter\` wraps any target \`fastmcp.Client\` accepts \(URL, local script, in-process server, \`MCPConfig\`, or a pre-built client\) and a FastMCP \`ClientGroup\` for a fleet of servers. This is a pre-release: \`pip install --pre &quot;langchain==1.4.0a3&quot;\`; the \`mcp\` extra \(\`pip install &quot;langchain\[mcp\]&quot;\`\) and \`fastmcp&gt;=4.0.0\` are required.

github · github-actions\[bot\] · Sep 1, 17:19

**「设计要点」** \`MCPAdapter.list\_tools\(\*, cache\_mode=&quot;use&quot;\)\` discovers and adapts tools with optional client-side caching \(SEP-2549\): \`use\` serves a cached list within the server TTL hint, \`refresh\` repopulates it, \`bypass\` skips it. MCP fields are grouped under \`metadata\[&quot;mcp&quot;\]\` \(annotations in snake\_case and \`\_meta\` at \`tool\`, server identity at \`server\`\); \`as\_langchain\_tool\` converts a single tool when the caller owns the client, and \`elicitation=&quot;interrupt&quot;\` surfaces mid-call questions as LangGraph interrupts so a human answers and the run resumes.

**「改了什么」** This alpha introduces the \`langchain.mcp\` namespace: \`MCPAdapter\`, cached \`list\_tools\`, \`as\_langchain\_tool\`, grouped \`mcp\` metadata, and LangGraph interrupt elicitation. The notes do not list other deltas versus earlier 1.4.0 alphas.

**Tags**: `#mcp`, `#tools`, `#runtime`

---

<a id="item-harness-arch-2"></a>
### [Graphiti mcp-v1.1.0 发布](https://github.com/getzep/graphiti/releases/tag/mcp-v1.1.0) ⭐️ 7.8/10

getzep/graphiti mcp-v1.1.0 released. The MCP server now consistently uses the configured Neo4j database for all operations. Self-hosted deployments with custom database names must set NEO4J\_DATABASE explicitly. The graphiti-core dependency bumped to 0.30.1.

github · mehulp93 · Sep 1, 23:09

**「设计要点」** The MCP server routes all database operations to the NEO4J\_DATABASE setting from .env or config.yaml.

**「改了什么」** It fixes Neo4j database routing to honor the configured database name. graphiti-core updated to 0.30.1.

**「评论」** No community comments available.

**Tags**: `#mcp`, `#runtime`, `#memory`

---

<a id="item-harness-arch-3"></a>
### [Claude Code 2.1.257 Released](https://code.claude.com/docs/en/changelog#2-1-257) ⭐️ 7.8/10

Claude Code 2.1.257 is released. It adds subagent model forcing via the CLAUDE\_CODE\_SUBAGENT\_MODEL\_FORCE environment variable. It adds containment escape rules to auto mode for permissions and metadata handling. It also adds timestamp configuration options for timeFormat and timeZone plus a /doctor warning for stale sandbox mask files.

rss · Claude Code Changelog · Sep 1, 18:00

**「改了什么」** Claude Code 2.1.257 adds subagent model forcing, containment escape rules in auto mode, sandbox mask warnings, and timestamp configuration options.

**Tags**: `#subagents`, `#sandbox`, `#permissions`, `#runtime`

---

<a id="item-harness-arch-4"></a>
### [Codex rust-v0.152.0 发布](https://github.com/openai/codex/releases/tag/rust-v0.152.0) ⭐️ 6.8/10

OpenAI Codex rust-v0.152.0 is released. It adds Vim search support for drafts, rate-limit action banners, enhanced MCP server name handling with package-style names, and configurable timeouts for app-server clients and shell commands.

github · github-actions\[bot\] · Sep 1, 01:58

**「改了什么」** This release adds Vim search motions in drafts, per-tool MCP output limits, rate-limit banners, and configurable timeouts for clients and shell commands. It also includes bug fixes for Vim mode initialization, Guardian review message preservation, and Windows sandbox execution.

**Tags**: `#mcp`, `#runtime`, `#tools`

---

<a id="item-harness-arch-5"></a>
### [Pydantic AI v2.37.0 Released](https://github.com/pydantic/pydantic-ai/releases/tag/v2.37.0) ⭐️ 6.8/10

Pydantic AI v2.37.0 released. Adds glm-5.3-flash model support. Reworks Z.AI test suite onto cassettes. Includes bug fixes for tracing, tool calls, and model routing.

github · dsfaccini · Sep 1, 01:48

**「Changed What」** Added glm-5.3-flash model support. Reworked Z.AI test suite onto cassettes. Fixed tracing span queries, non-standard finish\_reason mapping, AG-UI tool call emission, Vertex-Gemini routing, capability hooks, model context management, DBOS capabilities, Prefect tool discovery, and unmanaged model rebuilds.

**「Comments」** No community comments available.

**Tags**: `#runtime`, `#tools`, `#fix`

---

<a id="item-harness-arch-6"></a>
### [Gemini CLI v0.59.0-preview.0 released](https://github.com/google-gemini/gemini-cli/releases/tag/v0.59.0-preview.0) ⭐️ 6.8/10

google-gemini/gemini-cli v0.59.0-preview.0 is released. The update includes a security fix preventing SSRF in MCP OAuth metadata discovery and authentication. It also enforces fail-closed workspace trust and filters mcpServers in restricted mode. This is a protocol-related change with no new capabilities or major rewrites.

github · gemini-cli-robot · Sep 1, 20:19

**「What Changed」** Fixed SSRF in MCP OAuth metadata discovery and authentication. Enforced fail-closed workspace trust and filtered mcpServers in restricted mode.

**Tags**: `#mcp`, `#sandbox`, `#permissions`, `#runtime`, `#fix`

---

<a id="item-harness-arch-7"></a>
### [Cline desktop-v0.0.22-beta.1 released](https://github.com/cline/cline/releases/tag/desktop-v0.0.22-beta.1) ⭐️ 5.8/10

Cline desktop v0.0.22-beta.1 enables Composio connectors to register tools directly in the packaged desktop runtime for eligible internal accounts. Web search is enabled by default for new desktop sessions. It bundles all stable improvements through v0.0.21 including the two-pane Marketplace explorer, reliable cancellation of child agents and teammates, full-composer attachment drops, live Cline model catalog refreshes, and clearer provider authentication errors.

github · github-actions\[bot\] · Sep 1, 22:39

**「Design points」** Composio connectors register tools directly in the packaged desktop runtime for eligible internal accounts.

**「What changed」** Composio connectors now register tools directly in the packaged desktop runtime for eligible internal accounts with safer OAuth revocation and more resilient connect, disconnect, and reconciliation behavior. Web search is enabled by default for new desktop sessions.

**Tags**: `#runtime`, `#tools`, `#subagents`, `#permissions`

---

<a id="item-harness-arch-8"></a>
### [browser-use/video-use GitHub trending](https://github.com/browser-use/video-use) ⭐️ 5.0/10

browser-use/video-use is an open-source tool for editing videos with Claude Code. Drop raw footage in a folder and chat with the agent to get a final.mp4 file. It automatically cuts filler words and dead space between takes, and applies auto color grading to every segment. The tool works for any content type including talking heads, montages, tutorials, travel, and interviews without presets or menus.

rss · GitHub Trending Daily · Sep 1, 23:24

**Tags**: `#tools`, `#subagents`, `#sandbox`

---

## AI Agent Engineer

<a id="item-agent-engineer-1"></a>
### [BenchMIRT: What are LLM benchmarks actually measuring?](https://huggingface.co/blog/allenai/benchmirt) ⭐️ 7.8/10

AllenAI introduces BenchMIRT, a prompt-level auditing technique for LLM benchmarks using multidimensional Item Response Theory \(MIRT\). It separates signals of safety and general reasoning across 100 LLMs on 16 benchmarks with over 34K questions. BBQ aligns more strongly with reasoning than safety, and HarmBench mixes different signals. BenchMIRT can preserve model rankings with 10% of questions and predict held-out answers 79% of the time.

rss · Hugging Face Blog · Sep 1, 21:39

**「Why It Matters」** BenchMIRT helps disentangle mixed capabilities in benchmarks, improving the reliability of LLM evaluations for safety and reasoning.

**「Engineer Takeaway」** Focus on: Using BenchMIRT to select informative questions and predict model performance on unseen items without full evaluations.

**Tags**: `#eval`, `#harness`, `#benchmark`, `#llm`, `#auditing`

---

<a id="item-agent-engineer-2"></a>
### [@huggingface/kernels: 200+ WebGPU Kernels for Local AI](https://huggingface.co/blog/webgpu-kernels) ⭐️ 7.8/10

Hugging Face released @huggingface/kernels, a library with 207 WebGPU kernels for local AI. Each kernel is published as a versioned package on the Hub with its interface, WGSL shaders, correctness tests, benchmark cases, and usage examples. The release includes Fleet, a browser-based GPU benchmarking suite that crowdsources performance and correctness data from real hardware. On an Apple M4 GPU, the kernels delivered 2.57x geometric mean speedup and 1.90x median speedup over ORT WebGPU across 809 comparable test cases.

rss · Hugging Face Blog · Sep 1, 00:00

**「Why It Matters」** The library and Fleet give developers a portable, versioned foundation for browser-based inference while enabling community-driven kernel improvements through crowdsourced evidence.

**「Engineer Takeaway」** Observe: Each kernel repository ships manifest.json for the operation contract, test.json for correctness cases, bench.json for workloads, and parameterized \*.wgsl.jinja files for device-specific variants.

**Tags**: `#eval`, `#orchestration`, `#harness`

---

<a id="item-agent-engineer-3"></a>
### [Claude Fable 5.1 和 Claude Mythos 5.1 发布](https://www.anthropic.com/claude-fable-and-mythos-5-1) ⭐️ 7.0/10

Anthropic released Claude Fable 5.1 and Claude Mythos 5.1. The models feature a more natural writing style and reduced cache costs. Cache read pricing dropped from $1/M to $0.25/M. New developer tools support recording and visualizing LLM thinking effort levels. A system card PDF is available.

hackernews · denysvitali · Sep 1, 17:53 · [Discussion](https://news.ycombinator.com/item?id=49525378)

**「为什么重要」** These changes improve model writing style and lower cache costs for LLM applications. The visualization tools provide better observability for agent harnesses.

**「可关注」** Pay attention to: Simon Willison&\#x27;s Pelican tool for recording and visualizing different levels of LLM thinking effort.

**「评论」** Comments praise the natural writing style of Fable 5.1. Simon Willison shared his Pelican tool for visualizing reasoning traces. Some users note the cache price reduction benefits.

**Tags**: `#coding-agent`, `#harness`, `#observability`, `#eval`, `#orchestration`

---

<a id="item-agent-engineer-4"></a>
### [CogEvol: 高效可靠学习环境生成](https://huggingface.co/papers/2608.30968) ⭐️ 7.0/10

CogEvol is a family of models trained for Learning Environment Generation, turning course briefs into structured-JSON slides or self-contained interactive HTML pages in a single pass. Across 220k production requests, it completes a slide in a median of 17 seconds and an interactive page in 59 seconds, replacing minutes-long multi-turn agent scaffolding. A production-grounded data pipeline creates 53,687 verified SFT samples from real failures, and a hybrid rule-plus-VLM reward with GRPO RL ensures reliability after fixing a reward-hacking issue. CogEvol-27B scores 83.7 on slide quality and 63.7 on a 500-case interactive-HTML benchmark.

rss · Hugging Face Daily Papers · Sep 1, 00:00

**「为什么重要」** This single-pass approach with production-grounded training and RL provides efficient and reliable generation of learning artifacts, impacting agent orchestration by replacing multi-turn scaffolding and improving eval harnesses for content generation.

**「可关注」** Single-pass generation using verified SFT and RL reduces scaffolding complexity while enforcing reliability through data verification and reward hardening.

**「评论」** No community comments available.

**Tags**: `#harness`, `#eval`, `#orchestration`

---

<a id="item-agent-engineer-5"></a>
### [Lies We Can See: Joint Verbal and Non-Verbal Deception by VLM Agents](https://huggingface.co/papers/2608.30428) ⭐️ 7.0/10

The paper introduces MineAmongUs, a 3D multimodal Among Us sandbox. Imposter agents must deceive crewmates through joint verbal and non-verbal actions. It also proposes ARIA, a configurable VLM-agent harness that exposes cognitive capabilities for multi-agent social deduction games. This addresses gaps in existing text-only testbeds that overlook non-verbal sensorimotor channels and use single fixed agent configurations.

rss · Hugging Face Daily Papers · Sep 1, 00:00

**「Why It Matters」** MineAmongUs and ARIA provide new tools for evaluating VLM agents in embodied social interactions. The work directly supports agent evals and harness architecture.

**「What to Watch」** ARIA harness exposes cognitive capabilities for testing joint verbal and non-verbal deception by VLM agents.

**Tags**: `#harness`, `#eval`, `#orchestration`, `#coding-agent`

---

<a id="item-agent-engineer-6"></a>
### [Super Library Agent 论文](https://huggingface.co/papers/2608.29310) ⭐️ 6.0/10

论文提出 Super Library Agent 问题，LLM 代理顺序生成 N 个相关应用程序，同时维护共享的 Super Library 以包含可重用的跨应用程序组件。最小顺序脚手架可提取共享代码并将应用程序迁移到演变中的库中。这避免了共享逻辑在多个代码库中的重复，并减少了代理维护过程中的冗余和结构侵蚀。提供了与编码代理编排和内存相关的架构细节，但未提供代码、实验、轨迹或评估基准。

rss · Hugging Face Daily Papers · Sep 1, 00:00

**「为什么重要」** 该框架对于使用 LLM 编码代理管理相关应用程序组合的组织具有重要意义，因为它解决了共享组件维护的挑战。

**「可关注」** 可关注：使用最小顺序脚手架从多个应用程序中提取共享代码并迁移到共享超级库中。

**Tags**: `#coding-agent`, `#orchestration`, `#memory`

---

<a id="item-agent-engineer-7"></a>
### [Gemini agentic video understanding 发布](https://deepmind.google/blog/introducing-agentic-video-in-gemini/) ⭐️ 5.8/10

Google DeepMind 发布了 Gemini 的 agentic video understanding 能力。博客文章介绍了这一新特性。Gemini 现在支持 agentic 方式理解视频。影响 AI Agent 工程师在视频理解任务中的使用。

rss · Google DeepMind · Sep 1, 17:08

**「为什么重要」** Gemini 的 agentic video understanding 能力已发布。这项功能为 AI 代理提供了视频理解的新方式。尚未有关于其在生产环境中的实际影响数据。

**「可关注」** 可关注：Gemini agentic video understanding 能力

**Tags**: `#coding-agent`, `#orchestration`

---

## AI Daily

<a id="item-ai-daily-1"></a>
### [Anthropic Announces Enterprise Frontier Safeguards](https://www.anthropic.com/news/enterprise-frontier-safeguards) ⭐️ 8.8/10

Anthropic announces Enterprise Frontier Safeguards \(EFS\), a solution that combines zero data retention privacy with state-of-the-art misuse safeguards. EFS stores data in customer-controlled cloud infrastructure, not Anthropic&\#x27;s. The solution was developed with over 100 customers and partners at AWS, Google Cloud, and Microsoft Azure. Phased rollout starts later this fall.

rss · Anthropic News · Sep 1, 00:00

**「Why it matters」** This enables regulated enterprises to use frontier models while meeting privacy and security standards through customer-controlled data storage and automated monitoring.

**「Key takeaway」** Key takeaway: Customers control data storage and receive automated signals of potential misuse directly for their review, with no Anthropic human review required.

**Tags**: `#lab`, `#product`, `#industry`, `#policy`

---

<a id="item-ai-daily-2"></a>
### [Astra 首达关键网络安全能力门槛](https://openai.com/index/path-to-astra) ⭐️ 7.8/10

OpenAI 宣布 Astra 是首个达到 Preparedness Framework 关键网络安全能力门槛的模型，并加强了发布时的安全措施。

rss · OpenAI Blog · Sep 1, 13:00

**「可关注」** 可关注：Astra 是首个达到 Preparedness Framework 关键网络安全能力门槛的模型。

**Tags**: `#model`, `#lab`, `#policy`, `#product`

---

<a id="item-ai-daily-3"></a>
### [ChatGPT Connects to EHR and Healthcare Data](https://openai.com/index/chatgpt-connects-health-records-and-healthcare-sources) ⭐️ 7.8/10

OpenAI announced that ChatGPT can now connect to trusted healthcare data sources. This allows clinicians to securely access patient context, medical research, and more. The integration supports EHR systems and additional industry data for healthcare organizations.

rss · OpenAI Blog · Sep 1, 12:00

**「Why It Matters」** This enables secure access to patient information and research for clinicians using ChatGPT.

**「Takeaway」** Takeaway: Clinicians can securely access patient context and medical research through ChatGPT&\#x27;s integration with EHR and healthcare sources.

**Tags**: `#lab`, `#industry`, `#product`

---

<a id="item-ai-daily-4"></a>
### [AI-Native Companies Turn Workflows Into Operating Capability](https://openai.com/index/ai-native-company-workflows) ⭐️ 6.8/10

OpenAI blog post explains how AI-native companies use AI agents to improve onboarding, account management, and developer integrations. Basis, Clay, and Exa Labs provide concrete examples. Enterprise leaders can apply these approaches.

rss · OpenAI Blog · Sep 1, 17:00

**「Why It Matters」** These examples demonstrate practical ways AI agents can transform workflows into operating capabilities for enterprises.

**「Key Takeaway」** Key Takeaway: AI agents improve onboarding, account management, and developer integrations.

**Tags**: `#lab`, `#industry`, `#product`

---