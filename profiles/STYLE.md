# 日报中文规范

读者是做 coding agent / harness 的人。中文日报不是英译稿，是用中文把事实说清楚。

## 小标题用这些，不要另起

模型会给每个区块起标题。必须用下面这套，禁止「洞见」「赋能」「观察」「启示」。

| 区块 | 中文小标题 | 不要写成 |
| --- | --- | --- |
| `summary` | （主文，不要小标题） | 摘要、概述 |
| `why_it_matters` | 为什么重要 | 价值、意义、值得关注 |
| `engineer_takeaway` | 可关注 | 工程师洞见、Takeaway、启示 |
| `architecture_note` | 设计要点 | 架构说明、架构洞察 |
| `what_changed` | 改了什么 | 变更、Release Notes |
| `community_discussion` | 评论 | 社区声音、热议 |

渲染时写成 `**可关注** 正文`，不要加书名号「」。

## 专有名词

不译：Codex、Claude Code、OpenHands、Goose、Cline、Roo、Aider、Continue、SWE-agent、MCP、Bedrock、AppWorld、WebSocket、Zod。

仓库、包名、版本号、命令原样保留：`openai/codex`、`rust-v0.148.0`、`codex exec fork`。

人名、机构名：常见中文名可用（Hugging Face、Cloudflare 可保留英文）。

## 句子

- 完整中文句子。短，像跟同事讲，不要书面腔。
- 一条一事。数字、限制、对比基线、不确定处都留下。
- 已发生的变化和还没证实的影响要分开写。
- 证据不够就省略那个区块，不要用空话撑着。

## 禁止

洞见、赋能、浪潮、抓手、闭环、落地、值得关注的是、总而言之、作为一名、在…背景下、重磅、必看、引领。

不要把公司宣传写成客观事实。不要预测必然结果。不要为了中文化而硬译英文标题。

## 标题

中文标题不超过 22 个字。带上系统名和版本（如果有）。可以中英混排：`Codex rust-v0.148.0 发布`。不要用「重磅更新」「全面升级」。
