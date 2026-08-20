# 公众号草稿

日报在 GitHub Actions 上出。成稿按 [STYLE.md](STYLE.md) 写。先把成稿给人看。微信草稿箱只在固定 IP 的机器上推。

正式群发还是你在后台点。

## 流程

1. Actions 跑出当天中文日报（`gh-pages` 的 `_posts/YYYY-MM-DD-summary-zh.md`，或本地 Horizon 的 `data/summaries/`）。路径也会写在 Pages 的 `wechat-latest.md`。
2. 按 [STYLE.md](STYLE.md) 写成稿。人写，或：

   ```bash
   python3 wechat/scripts/write_from_digest.py --digest <日报.md>
   ```

   只抽条目、还不写时：

   ```bash
   python3 wechat/scripts/build_from_digest.py --digest <日报.md>
   # 或：python3 wechat/scripts/polish_post.py --digest <日报.md>
   ```

3. 打开 `wechat/posts/YYYY-MM-DD.md`，先看这篇。不要补「我的疑问」。
4. 看过之后，在**固定公网 IP** 的机器上：

   ```bash
   python3 wechat/scripts/push_draft.py wechat/posts/YYYY-MM-DD.md --cover wechat/cover.png
   ```

GitHub Actions 不推微信。出口 IP 会变，过不了白名单。

写稿用的模型和网关跟日报一样，读 `data/config.github.json` 的 `ai.provider` / `ai.model` / `ai.base_url`，密钥只从环境变量或 `wechat/.env.local` 读。

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
# 本地用 write_from_digest.py 时，跟日报同一把网关密钥
OPENAI_API_KEY=...
```
