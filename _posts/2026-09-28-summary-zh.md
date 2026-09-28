---
layout: default
title: "Horizon Summary: 2026-09-28 (ZH)"
date: 2026-09-28
lang: zh
---

> 从 152 条内容中筛选出 2 条重要资讯。

---

**Harness 架构**
1. [Claude Code 官方插件目录上线](#item-harness-arch-1) ⭐️ 5.0/10

**AI 羊毛**
1. [echelongraph-mcp 免密钥查漏洞](#item-ai-deals-1) ⭐️ 5.0/10

---

## Harness 架构

<a id="item-harness-arch-1"></a>
### [Claude Code 官方插件目录上线](https://github.com/anthropics/claude-plugins-official) ⭐️ 5.0/10

Anthropic 在 GitHub 上线官方插件目录 anthropics/claude-plugins-official，集中策展高质量 Claude Code 插件。目录明确声明 Anthropic 不控制插件内的 MCP server、文件或其他软件，无法验证其行为或保证不变。安装、更新或使用前，用户需自行确认插件来源可信。

rss · GitHub Trending Daily · 9月28日 01:57

**「设计要点」** 插件体系将第三方 MCP server 与本地文件操作交由用户侧信任决策，Anthropic 仅提供目录索引，不承担运行时安全验证责任。

**标签**: `#tools`, `#mcp`, `#permissions`

---

## AI 羊毛

<a id="item-ai-deals-1"></a>
### [echelongraph-mcp 免密钥查漏洞](https://news.ycombinator.com/item?id=49863302) ⭐️ 5.0/10

echelongraph 发布 echelongraph-mcp，一个免费、无需 API key 和注册的 MCP 服务器。用户可在 Claude、Cursor 等 MCP 客户端中查询 CVE 数据，并查看给定 CVE 的互联网暴露服务数量。配置方法为在 MCP 客户端配置中添加 npx -y echelongraph-mcp。

rss · HN Free API / Credits · 9月27日 04:13

**「为什么重要」** 对需要核对漏洞暴露面的开发者，可零成本接入现有 MCP 客户端，无需注册或管理密钥。

**「可关注」** 可关注：echelongraph-mcp 提供免密钥 CVE 查询，适合在 Claude、Cursor 等 MCP 客户端中快速核对漏洞暴露面；但暴露面数据以其 radar 记录为限。

**标签**: `#free-tier`, `#api`, `#mcp`

---