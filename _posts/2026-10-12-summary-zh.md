---
layout: default
title: "Horizon Summary: 2026-10-12 (ZH)"
date: 2026-10-12
lang: zh
---

> 从 135 条内容中筛选出 2 条重要资讯。

<nav id="ah-toc" class="ah-toc" aria-label="目录"><span class="ah-toc-title">目录</span><ul><li><a href="#sec-harness-arch"><span class="ah-toc-name">Harness 架构</span><span class="ah-toc-count">2条</span></a></li></ul></nav>

---

**[Harness 架构](#sec-harness-arch)**
1. [MCP 参考服务 v1.0.0 发布](#item-harness-arch-1) ⭐️ 7.3/10
2. [Anthropic 开源知识工作插件仓库](#item-harness-arch-2) ⭐️ 5.0/10

---

## Harness 架构
{: #sec-harness-arch .ah-section}

<p class="ah-sec-meta"><a class="ah-anchor" href="#sec-harness-arch" aria-label="链接到本节">#</a><a class="ah-back" href="#ah-toc">↑ 回到目录</a></p>

<a id="item-harness-arch-1"></a>
### [MCP 参考服务 v1.0.0 发布](https://github.com/modelcontextprotocol/servers/releases/tag/v1.0.0) ⭐️ 7.3/10

Model Context Protocol 官方参考服务端仓库发布 v1.0.0。核心 TypeScript 服务包（everything、filesystem、memory、sequential-thinking）正式推至 1.0.0，Python 实现包（fetch、git、time）同步发布 2026.10.10 版本。本次面向 SDK 1.x 分支完成发布审计，将多包版本发布收拢至 changesets 管理。

github · cliffhall · 10月11日 02:40

**「设计要点」** filesystem 服务在执行工具前建立根目录同步屏障，严格拦截未经许可的 UNC 路径并校验 Unicode 规范化格式。memory 服务将图谱写入操作串行化以规避并发写竞争，同时在磁盘加载阶段强制校验知识图谱实体与悬挂关系合法性。

**「改了什么」** 规范化工具契约与传输清理，filesystem 所有工具显式声明 JSON Schema 2020-12，编辑文件时保留原始换行符与缩进；everything 服务支持会话断开后自动注销订阅、修复未知与重复 HTTP+SSE 会话处理，并隔离会话级资源；CI 增加单文件 90% 覆盖率门禁与 Windows 运行环境测试。

**标签**: `#mcp`, `#tools`, `#runtime`

---

<a id="item-harness-arch-2"></a>
### [Anthropic 开源知识工作插件仓库](https://github.com/anthropics/knowledge-work-plugins) ⭐️ 5.0/10

Anthropic 开源 knowledge-work-plugins 仓库。该插件集面向 Claude Cowork 设计，同时兼容 Claude Code。插件支持配置数据拉取源、指定角色工具、处理关键业务工作流，并注册自定义斜杠命令。

rss · GitHub Trending Daily · 10月11日 23:46

**「设计要点」** 通过绑定外部数据源、工具集与斜杠命令，插件在应用层为通用运行时注入岗位角色约束与工作流编排规则。

**标签**: `#tools`, `#runtime`, `#planning`

---