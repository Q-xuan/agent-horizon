# 评估目标

评估一条信息对关注 agent harness 架构的工程师有多重要。读者想知道：这个系统怎么跑、改了什么、值不值得对照自己的实现。

# 评分标准

- **9–10：架构级。** 新的开源 harness、重大运行时重写、工具/权限/记忆模型变化，或带细节的设计分享。
- **7–8：该跟版本。** 重要 Release、协议更新、评测方法变化，有足够技术细节。
- **5–6：记一笔。** 小但具体的能力（新工具、新 sandbox 选项、新 eval），或中等质量的架构笔记。
- **3–4：可忽略。** 无说明的小版本、重复转发、缺少技术内容。
- **0–2：噪音。** 纯宣传、改名、和 harness 无关。

# 来源权威

官方 GitHub Release 和公司/工程博客高于 Reddit、Google News、二手科技媒体。

- **官方一手**（harness 仓库 Release、Anthropic / OpenAI / Cursor / Aider 等工程博客）：按变更本身给分。
- **二手/传闻**（没有官方 Release / changelog / 工程博客 URL）：分数封顶 **5.5**，只记一笔，不要当架构新闻。
- **社区**（Reddit、X）：没有一手链接时不要用热度抬分。
- 同一天已有官方 Release 时，二手 5.x 不要占 harness 栏。

# 评估要求

看变更说明、PR、架构图、代码路径和限制条件。没有技术细节就不要高分。给出 3–5 个标签，优先：runtime、tools、mcp、sandbox、memory、subagents、eval、permissions、planning。
