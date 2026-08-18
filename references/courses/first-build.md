# ④ 做出并发布你的第一个东西

状态：alpha

## 唯一承诺

学生带自己的想法入场，自由选择作品和技术，完整走完澄清、选型、原型、实现、验证、交付、反馈和证据发布。

## 固定的是循环，不是技术栈

| 节点 | 文件 |
|---|---|
| 找到值得做的一件小事 | `../lessons/first-build/01-find-a-real-problem.md` |
| brainstorming 发散、GrillMe 访谈与 PRD v0 | `../lessons/first-build/02-project-map.md` |
| Design System、Lovable 原型、PRD v1 与 Spec | `../lessons/first-build/03-visible-prototype.md` |
| 敏捷开发一个端到端 MVP | `../lessons/first-build/04-build-a-slice.md` |
| 可行性门、工程质量、交叉 Review 与发布 | `../lessons/first-build/05-verify-publish-feedback.md` |

## 技术选择

Agent 根据作品类型调查方案：静态网页、Web 应用、脚本、数据工具、机器人、Skill、桌面工具或开源贡献都可以。推荐必须包含：为什么适合、暂不需要什么、一个备选和第一段可验收成果。Web 产品默认在 PRD v0 后先构思 Design System，再用 Lovable 验证方向；原型不自动成为最终工程代码。

只有作品确实需要持久化、登录、多人共享数据或跨进程访问时，才插入 `../lessons/shared/database-and-data-authority.md`。先画数据权威源与访问链路，再讨论数据库产品；不能因为示例常用 Supabase 就默认给所有项目加数据库。

MVP 通过可行性门后，如果要系统补测试层级、回归和 CI，转入 `../courses/testing-verification.md`；MVP 阶段仍保留核心路径 smoke 验收。

Supabase、Vercel、Lovable、baoyu-design、Figma MCP、Pencil MCP、shadcn/ui 是 Alan 的经验选项，不是必选项。需要 Web 概念时插入共享节点。

## 完成证据

- 项目说明和技术决策；
- 可读版本历史；
- 三个真实验收样例；
- 一次失败与修复闭环；
- 一次 MVP 可行性判断和一次独立交叉 Review；
- 别人可以获得或使用的交付物；
- 至少一名目标用户的真实反馈；
- Builder 证据卡。
