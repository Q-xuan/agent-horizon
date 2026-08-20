# 公众号草稿

从每日雷达里勾几条，补上你的判断，再推进微信草稿箱。正式群发还是你在后台点。

## 链接为什么会丢

推草稿时正文已经是 HTML，不是 markdown。微信发布时会洗掉普通 `<a href="https://...">文字</a>`，所以之前那种「markdown 链转成裸 `<a>`」的稿，发布后链接全没了。

`scripts/push_draft.py` 必须把 `[文字](https://...)` 收成编辑器形态：

```html
<a target="_blank" href="https://..." textvalue="..." data-linktype="2">
```

只允许 `https://` 进 `href`。标签和 URL 都要转义。不要改回裸 `<a href>`。

订阅号上最稳的外链是文末「阅读原文」。脚本会写进草稿字段 `content_source_url`：

1. frontmatter 的 `source:`（必须是 `https://`）
2. 否则正文第一条 `原文：[标题](https://...)`
3. 再否则正文第一条 `https://`

有出处的条目结尾必须写成 `原文：[标题](https://...)`，不要裸 URL，不要空的「我的疑问」。详见 [STYLE.md](STYLE.md)。

不要把 `WECHAT_SECRET` 写进仓库。不要在 GitHub Actions 里调微信接口（出口 IP 会变，也不该把密钥交给 CI）。

## 微信侧怎么开权限

认证过的公众号即可调草稿箱接口。要放行的是**实际发请求这台机器**的公网 IP，不是 GitHub Actions。

现在这台机器的出口 IP：`104.30.175.37`

1. 打开 [微信开发者平台](https://developers.weixin.qq.com/platform/) ，扫码登录
2. 我的业务 → 公众号 → 基础信息 → 开发信息
3. 把 `104.30.175.37` 加进 **API IP 白名单**
4. 同一页确认 AppID / AppSecret（AppID 已是 `wxf44969be51cccc30`）

旧后台路径也行：mp.weixin.qq.com → 开发 → 基本配置 → IP 白名单。

第一次用新 IP 调接口，管理员微信可能收到确认模板（错误码 89503）。点允许之后再推一次。

只写草稿箱，不群发。

## 本地变量

写在 `wechat/.env.local`（已 gitignore），不要进仓库：

```bash
WECHAT_APPID=wxf44969be51cccc30
WECHAT_SECRET=...
```

推草稿前先 `set -a; . wechat/.env.local; set +a`，或自行 export。脚本只读环境变量，不把密钥写进 git。

## 流程

1. 当天日报出来（`docs/` 或 Horizon 的 `data/summaries/`）
2. `python3 wechat/scripts/build_from_digest.py --digest <日报.md> --pick 1,3,5`
3. 打开 `wechat/posts/YYYY-MM-DD.md`：每条有出处的结尾必须是 `原文：[标题](https://...)`；有判断再写，不要留空的「我的疑问」
4. `python3 wechat/scripts/push_draft.py wechat/posts/YYYY-MM-DD.md --cover wechat/cover.png`

生成稿和手写稿都用 [template.md](template.md) 的 `原文：` 行。改渲染器或写新脚本时，先跑 `python3 wechat/scripts/test_wechat_links.py`，确认不会退回裸 `<a href>`。
