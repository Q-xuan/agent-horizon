# 今日公众号原料

GitHub Actions 只出日报，不推微信草稿箱。

- 中文日报：`_posts/2026-08-23-summary-zh.md`
- 写法：[wechat/STYLE.md](https://github.com/Q-xuan/agent-horizon/blob/main/wechat/STYLE.md)
- 本地成稿：`python3 wechat/scripts/write_from_digest.py --digest <日报.md>`
- 先看成稿。再在固定 IP 机器上：`python3 wechat/scripts/push_draft.py wechat/posts/YYYY-MM-DD.md --cover wechat/cover.png`
