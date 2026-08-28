# 来源权威分层

日报要看起来像官方新闻（公司博客 / GitHub Release），而不是 Reddit、Google News 或微信科技媒体的二手噪音。

Horizon 的 `data/config.json` 禁止未知字段（`extra=forbid`），所以旋钮不写进主配置，而在 [`data/source_tiers.json`](../data/source_tiers.json)。分析提示会偏向官方源；**真正卡线的是分析之后的确定性调分**（`scripts/apply_source_tiers.py`，Actions 里由 `patches/apply_source_tiers.py` 挂到 Horizon）。

## 分层

| 层 | 典型来源 | 调分 |
| --- | --- | --- |
| `official` | GitHub `repo_releases`；公司/实验室/工程博客 RSS | `score + official_boost`（默认 +0.8，上限 10） |
| `practitioner` | 个人技术博客、The Batch / Import AI 等 | 不调 |
| `deals` | 少数派 / 小众软件 / V2EX / Product Hunt / 爱范儿 / HN credits | 不调（羊毛栏单独走 `ai-deals`） |
| `community` | Reddit、X follow-list / X Hot、HN / Lobsters、OSSInsight、GitHub Trending、HF Daily Papers / Trending Models | 没有官方一手 URL 时封顶并可能丢弃 |
| `secondary` | Google News；量子位 / 新智元 / 机器之心 / 夕小瑶 / PaperWeekly | 没有官方一手 URL 时封顶并可能丢弃 |

「官方一手 URL」：条目链接或正文里出现公司/实验室域名，或 `github.com/<已跟踪 owner>/...`。Google News、Reddit、微信 `mp.weixin.qq.com`、HN 本身不算一手。

## 旋钮（`data/source_tiers.json`）

| 字段 | 默认 | 作用 |
| --- | --- | --- |
| `official_boost` | `0.8` | 官方源分数上浮 |
| `secondary_without_primary.score_cap` | `5.5` | 二手且无一手链接时的分数上限（「记一笔」） |
| `secondary_without_primary.min_score_to_keep` | `6.5` | 二手且无一手链接时，低于此分直接丢弃。默认 **cap < min**，等于无一手链接的二手稿不会进日报 |
| `community_without_primary.score_cap` | `6.0` | 社区帖无一手链接时的上限 |
| `community_without_primary.min_score_to_keep` | `6.5` | 社区帖无一手链接时的过线分。默认同样进不了日报 |
| `official_rss_names` / `secondary_rss_names` / … | 见 JSON | 按 RSS `feed_name` 分层；新增官方博客时两边一起改 |
| `official_github_owners` | 已跟踪的 harness / agent 仓库 owner | 判断 GitHub URL 算不算一手 |
| `official_hosts` | 公司/实验室域名 | 判断正文/链接算不算一手 |

有官方一手 URL 的二手或社区稿**不封顶、不丢弃**，和从业者稿一样按模型分竞争；官方原文仍多 0.8 分，topic_dedup 时更容易留下原文。

## 本地 / Actions

分析之后、按 profile 阈值筛选之前执行。分数被降到 0 的条目过不了现有阈值（`harness-arch` 5.0、`agent-engineer` 5.5、`ai-daily` 5.0、`ai-deals` 4.5）。

```bash
python3 scripts/test_source_tiers.py
python3 scripts/test_scrape_hot.py
python3 scripts/apply_source_tiers.py --policy data/source_tiers.json
python3 scripts/scrape_no_rss.py --out /tmp/scraped-feeds --print-items
```

Actions 在 `daily.yml` 里把 `source_tiers.json` 和脚本拷进 Horizon，再打 orchestrator 补丁。本地跑也要同样做一遍，见仓库 README。

## 以后可以做（本 PR 不做）

- 跨日 URL 历史库，避免同一公告连着两天出现
- 同一产品同一天多包 Release（例如 Cline SDK / CLI / desktop / extension）折成一条
