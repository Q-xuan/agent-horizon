---
layout: default
title: "Horizon Summary: 2026-10-26 (ZH)"
date: 2026-10-26
lang: zh
---

> 从 150 条内容中筛选出 1 条重要资讯。

<nav id="ah-toc" class="ah-toc" aria-label="目录"><span class="ah-toc-title">目录</span><ul><li><a href="#sec-harness-arch"><span class="ah-toc-name">Harness 架构</span><span class="ah-toc-count">1条</span></a></li></ul></nav>

---

**[Harness 架构](#sec-harness-arch)**
1. [MCP Servers v2.1.0 安全修复发布](#item-harness-arch-1) ⭐️ 7.8/10

---

## Harness 架构
{: #sec-harness-arch .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-harness-arch" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-harness-arch-1"></a>
### [MCP Servers v2.1.0 安全修复发布](https://github.com/modelcontextprotocol/servers/releases/tag/v2.1.0) ⭐️ 7.8/10

MCP Servers v2.1.0 修复三个服务器的 8 个安全漏洞。@modelcontextprotocol/server-filesystem 2.0.1 堵住符号链接竞争条件、路径遍历和目录列表信息泄露，Windows 平台仅部分修复；@modelcontextprotocol/server-everything 2.0.1 阻断 HTTP/SSE 传输的跨域工具调用；mcp-server-fetch 2026.10.24 修复 SSRF 相关的地址校验缺陷。TypeScript 服务器已迁移到语义版本，包管理器不会自动从日期版本升级到 2.0.1，需手动指定版本安装。

github · cliffhall · 10月25日 00:03

**「设计要点」** 文件系统服务器在权限检查与写操作间保持路径字符串一致性，防止父目录被替换为符号链接导致的目录逃逸。传输层通过 Origin 头校验和移除通配符 CSP 隔离跨域来源，抓取服务器统一地址分类与连接使用的 hostname 形式。

**「改了什么」** 文件系统服务器新增：写操作前重新验证父目录未替换为符号链接；路径检查保留尾部空白与引号差异；大小写敏感文件系统上区分符号链接大小写；目录列表前过滤符号链接。抓取服务器统一 IDNA 主机名校验与连接、阻断 NAT64 包装的私有 IPv4 地址、每次重定向后重新检查 robots.txt。

**标签**: `#mcp`, `#tools`, `#sandbox`, `#permissions`

---