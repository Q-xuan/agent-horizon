# Agent Horizon

给 AI Agent 工程师的每日雷达。引擎用 [Horizon](https://github.com/Thysrael/Horizon)，信息源和打分按 **coding agent / harness 架构** 收窄。

每天早上（北京时间约 7 点）GitHub Actions 会：

1. 抓 HN、RSS、Reddit、GitHub Release、OSSInsight、Google News
2. 去重，用 `agent-engineer` / `harness-arch` 两个 profile 打分过滤
3. 生成中英双语日报，发布到 GitHub Pages

## 日报看什么

- **Harness / 架构**：Claude Code、Codex、OpenHands、Goose、Cline、Roo、Aider、Continue、SWE-agent、MCP、新 harness 设计
- **Agent 工程师该盯的**：框架、评测、工具协议、产品能力变化、可复核的论文
- **Release**：上面这些仓库的新版本

故意丢掉：消费级 ChatGPT 八卦、生图、融资传闻、纯提示词清单。

## 本地跑一次

```bash
# 1. 拉 Horizon 引擎
git clone --depth 1 https://github.com/Thysrael/Horizon.git /tmp/horizon
cp -R data profiles /tmp/horizon/
cp data/config.json /tmp/horizon/data/config.json

# 2. 密钥
cp .env.example /tmp/horizon/.env
# 填 OPENAI_API_KEY（当前模型 grok-4.6，接口见 config.json 的 ai.base_url）

# 3. 跑
cd /tmp/horizon
uv sync
uv run horizon --hours 24
```

日报写在 Horizon 的 `data/summaries/`，并复制到 `docs/`。

## GitHub 上每天跑

仓库里的 `.github/workflows/daily.yml` 会 checkout 本仓库 + Horizon，套上这份配置后跑，再把 `docs/` 推到 `gh-pages`。

需要在仓库 Settings → Secrets 里加 **一个** 模型密钥，和 `data/config.github.json` 里的 `api_key_env` 对上。当前用 OpenAI 兼容网关 + `grok-4.6`：

- `OPENAI_API_KEY`

接口地址在 `ai.base_url`，默认 `https://ai.aruyx.com/v1`。

然后：

1. Settings → Pages → Source 选 `gh-pages` 分支
2. Actions 里手动跑一次 **Daily Agent Digest**，确认通了
3. 之后每天 UTC 23:00（北京时间次日 7:00）自动出报

## 改源

编辑 `data/config.json`（本地）和 `data/config.github.json`（Actions）。两边建议保持同源。

打分阈值在 `processing.profile_settings`：

- `agent-engineer.threshold`：默认 6.5，偏「今天该不该看」
- `harness-arch.threshold`：默认 5.5，Release 和架构文稍松一点

## 许可

配置和 profile 属于本仓库。运行时引擎是 Horizon，[MIT](https://github.com/Thysrael/Horizon/blob/main/LICENSE)。


## 公众号

日报是原料。选出几条，补上疑问和判断，再推进草稿箱。见 [wechat/README.md](wechat/README.md)。
