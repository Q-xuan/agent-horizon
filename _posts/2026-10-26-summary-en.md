---
layout: default
title: "Horizon Summary: 2026-10-26 (EN)"
date: 2026-10-26
lang: en
---

> From 150 items, 1 important content pieces were selected

---

**Agent Harness Architecture**
1. [MCP servers v2.1.0 安全修复发布](#item-harness-arch-1) ⭐️ 7.8/10

---

## Agent Harness Architecture

<a id="item-harness-arch-1"></a>
### [MCP servers v2.1.0 安全修复发布](https://github.com/modelcontextprotocol/servers/releases/tag/v2.1.0) ⭐️ 7.8/10

Model Context Protocol servers 官方发布 v2.1.0，修复 3 个服务器中的 8 个关键安全漏洞。\`@modelcontextprotocol/server-filesystem\` 和 \`@modelcontextprotocol/server-everything\` 升级至 2.0.1，\`mcp-server-fetch\` 升级至 2026.10.24。filesystem 服务器修复了符号链接竞争条件、路径检查绕过和目录列表信息泄露；everything 服务器修复了 HTTP/SSE 传输的跨域请求问题；fetch 服务器修复了 SSRF 和 robots.txt 检查绕过。注意：npm 上使用日期版本的包管理器不会自动将 2.0.1 视为升级，需显式安装。

github · cliffhall · Oct 25, 00:03

**「改了什么」** filesystem 服务器修复符号链接竞争条件、路径检查绕过（尾部引号/空格）、大小写不敏感卷回归及目录列表信息泄露；everything 服务器为 HTTP/SSE 传输添加 Origin 检查，阻断跨域工具调用；fetch 服务器统一地址检查与连接主机名、拒绝 NAT64 封装私有地址、重定向后重检 robots.txt。

**Tags**: `#mcp`, `#tools`, `#sandbox`, `#permissions`

---