# 公众号草稿

从每日雷达里勾几条，补上你的疑问和判断，再推进微信草稿箱。正式群发还是你在后台点。

## 微信侧怎么开权限

认证过的公众号即可调草稿箱接口。要放行的是**实际发请求这台机器**的公网 IP，不是 GitHub Actions（出口会变）。

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

## 流程

1. 当天日报出来
2. `python3 wechat/scripts/polish_post.py --digest <日报.md>`
3. 打开 `wechat/posts/YYYY-MM-DD.md`，补「我的疑问」「我的判断」
4. `python3 wechat/scripts/push_draft.py wechat/posts/YYYY-MM-DD.md --cover wechat/cover.png`
