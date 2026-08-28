# Agent Horizon

给 AI Agent 工程师的每日雷达。引擎用 [Horizon](https://github.com/Thysrael/Horizon)，信息源和打分按 **coding agent / harness 架构** 收窄。

每天早上（北京时间约 7 点）GitHub Actions 会：

1. 抓 HN、RSS、Reddit、GitHub Release、OSSInsight、Google News
2. 去重，用 profile 打分；再按 [来源权威分层](docs/source-tiers.md) 上调官方源、压掉无一手链接的二手/社区稿
3. 生成中英双语日报，发布到 GitHub Pages

## 日报看什么

- **Harness / 架构**：Claude Code、Codex、OpenHands、Goose、Cline、Roo、Aider、Continue、SWE-agent、MCP、新 harness 设计
- **Agent 工程师该盯的**：框架、评测、工具协议、产品能力变化、可复核的论文
- **Release**：上面这些仓库的新版本

故意丢掉：消费级 ChatGPT 八卦、生图、融资传闻、纯提示词清单。少数派 / 小众软件 / V2EX Hot / Product Hunt / 爱范儿 / HN credits 会收 AI 羊毛，仍靠打分过滤。

## 本地跑一次

```bash
# 1. 拉 Horizon 引擎
git clone --depth 1 https://github.com/Thysrael/Horizon.git /tmp/horizon
cp -R data profiles /tmp/horizon/
cp data/config.json /tmp/horizon/data/config.json
cp data/source_tiers.json /tmp/horizon/data/source_tiers.json
cp scripts/apply_source_tiers.py /tmp/horizon/src/apply_source_tiers.py
python3 patches/grok_reasoning_effort.py /tmp/horizon/src/ai/client.py
python3 patches/shanghai_digest_date.py /tmp/horizon/src/orchestrator.py
python3 patches/apply_source_tiers.py /tmp/horizon/src/orchestrator.py

# 2. 密钥
cp .env.example /tmp/horizon/.env
# 填 OPENAI_API_KEY（当前模型 grok-4.6，reasoning_effort=xhigh，接口见 config.json 的 ai.base_url）

# 3. 跑
cd /tmp/horizon
uv sync
uv run horizon --hours 24
```

日报写在 Horizon 的 `data/summaries/`，并复制到 `docs/`。

## GitHub 上每天跑

仓库里的 `.github/workflows/daily.yml` 会 checkout 本仓库 + Horizon，套上这份配置后跑，再把 `docs/` 推到 `gh-pages`。

需要在仓库 Settings → Secrets 里加 **一个** 模型密钥，和 `data/config.github.json` 里的 `api_key_env` 对上。当前用 OpenAI 兼容网关 + `grok-4.6`（`reasoning_effort=xhigh`）：

- `OPENAI_API_KEY`

接口地址在 `ai.base_url`，默认 `https://ai.aruyx.com/v1`。

然后：

1. Settings → Pages → Source 选 `gh-pages` 分支
2. Actions 里手动跑一次 **Daily Agent Digest**，确认通了
3. 之后每天 UTC 23:00（北京时间次日 7:00）自动出报；23:30 再试一次（GitHub 可能因 main 空闲跳过定时，gh-pages 提交保不了 main）

## 改源

编辑 `data/config.json`（本地）和 `data/config.github.json`（Actions）。两边建议保持同源。

X 用 Horizon 自带 Apify 抓指定账号；需要仓库 secret APIFY_TOKEN；打分过滤。

中文小标题和用词见 [`profiles/STYLE.md`](profiles/STYLE.md)。

打分阈值在 `processing.profile_settings`（`config.json` 与 `config.github.json` 保持一致）：

- `harness-arch.threshold`：`5.0`
- `agent-engineer.threshold`：`5.5`
- `ai-daily.threshold`：`5.0`
- `ai-deals.threshold`：`4.5`

谁能留下，主要看来源权威，不靠再抬这些阈值。旋钮在 `data/source_tiers.json`，说明见 [`docs/source-tiers.md`](docs/source-tiers.md)：

- `official_boost`：官方 GitHub Release / 公司工程博客 `+0.5`
- `secondary_without_primary`：Google News、微信科技媒体等没有官方一手 URL 时，封顶 `5.5` 且默认直接丢弃
- `community_without_primary`：Reddit / X / HN 讨论同样；正文若链到官方 Release 或公司博客则不卡

## 许可

配置和 profile 属于本仓库。运行时引擎是 Horizon，[MIT](https://github.com/Thysrael/Horizon/blob/main/LICENSE)。


## 公众号

日报是原料。GitHub Actions 只出日报。成稿按 [wechat/STYLE.md](wechat/STYLE.md) 写，先给人看，再在固定 IP 的机器上推草稿箱。见 [wechat/README.md](wechat/README.md)。
