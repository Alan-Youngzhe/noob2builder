# Noob2Builder · AI Builder School

一所由 Agent 亲自带学的学校。不是文档合集，而是导师在主对话里讲清原理，带你操作真实文件、运行真实命令，直到你做出并发布第一个可验收的作品。

适合纯小白，也适合已有项目、想从 vibe coding 进阶到 agentic engineering 的学习者。

## 理念

- **全选修**——编号是稳定 ID，不代表必修顺序；按你的目标选课
- **真实操**——每节课都有真实实验和可检查的产物，不接受"Agent 说完成就算完成"
- **学完有证据**——本地学习存档记录每个节点的完成证据、未验证项和下一步
- **随时打断**——学生随时可以提问，答完回到主线

## 课程

| ID | 课程 | 内容 |
|---|---|---|
| `computer-network` | 计算机与网络基础 | 看懂 Agent 正在做什么 |
| `ai-map` | AI 世界地图 | 建立对 AI 领域的整体认知 |
| `llm-agent` | LLM 与 Agent 原理 | token、context、Agent、MCP、Skill 是什么 |
| `git-github` | Git & GitHub | 从安装到完成第一次真实 PR |
| `builder-method` | AI Builder 工作法 | 问题先于 prompt，从访谈到垂直切片 |
| `first-build` | 做出并发布第一个东西 | 找到真实问题，做出可验收的作品并发布 |
| `agentic-engineering` | 从 Vibe Coding 到 Agentic Engineering | 为项目补上测试、验证门禁和 Review |
| `testing-verification` | 测试与验证 | 单元、集成、冒烟、E2E、回归、CI 和独立 Review |
| `ai-engineering-evolution` | 从 Prompt 到 Graph | AI 工程方法的演进路径 |
| `ai-product-sense` | AI 产品 Sense | 建立 AI 产品的判断力 |
| `agent-lab` | Agent 构建实验室 | 亲手构建带工具调用和验收的 Agent |

## 怎么开始

1. 将本仓库作为 Skill 安装到你的 Agent 环境（如 Claude Code 的 `~/.claude/skills/`）
2. 对 Agent 说：**"带我学 AI"**、**"我想做第一个作品"** 或 **"教我 Git/GitHub"**
3. 导师会展示课程目录，根据你的目标推荐选课

## 校友墙

完成任意一项里程碑（第一个 PR、第一个发布的作品、第一个 Agent、一次 agentic 改造），欢迎向 [WALL.md](WALL.md) 提交 PR，留下你的证据和一句话复盘。

## 项目结构

```
SKILL.md            教务处：导师的工作规则与课程路由
manifest.json       版本与文件清单
references/
  catalog.md        课程目录
  pedagogy.md       教学法细则
  courses/          11 门课程的教案
  lessons/          各课程的具体课节与实验
  lessons/shared/   安全、Web、数据库、HTTP 状态码与证据卡等共享节点
WALL.md             校友墙
```

## 状态

Alpha (v0.5.0)。课程内容持续迭代中，欢迎 Issue 和 PR。
