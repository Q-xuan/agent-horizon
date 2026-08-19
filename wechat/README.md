# 公众号草稿

从每日雷达里勾几条，补上你的疑问和判断，再推进微信草稿箱。正式群发还是你在后台点。

## 流程

1. 当天日报出来（`docs/` 或 Horizon 的 `data/summaries/`）
2. 选出要写的条目
3. 生成稿：`python3 wechat/scripts/build_from_digest.py --digest <日报.md> --pick 1,3,5`
4. 打开 `wechat/posts/YYYY-MM-DD.md`，把「我的疑问」「我的判断」写成你的话
5. 推草稿（二选一）：
   - [md2wechat](https://github.com/geekjourneyx/md2wechat-skill)：`md2wechat convert wechat/posts/YYYY-MM-DD.md --draft --cover wechat/cover.png`
   - 本仓库脚本：`python3 wechat/scripts/push_draft.py wechat/posts/YYYY-MM-DD.md --cover wechat/cover.png`

CLI 只写草稿箱，不群发。

## 微信侧要准备的

认证过的公众号，在[微信开发者平台](https://developers.weixin.qq.com/platform)拿 AppID / AppSecret，并把**实际发请求那台机器**的公网 IP 加到 IP 白名单。

GitHub Actions 出口 IP 会变，不适合直接调微信。草稿推送在本地或一台固定 IP 的机器上跑。

环境变量（不要提交到 Git）：

```bash
export WECHAT_APPID=...
export WECHAT_SECRET=...
```

md2wechat 也可以写到 `~/.config/md2wechat/config.yaml`。
