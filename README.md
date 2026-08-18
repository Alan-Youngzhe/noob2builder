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
| `frontend-foundations` | 前端基础：三件套与工程化 | HTML/CSS/JS、npm、Vite、TypeScript，看懂 Agent 生成的前端 |
| `frontend-framework` | 前端框架：组件化与项目结构 | Vue/React、组件化、TSX、路由、项目结构与有证据的重构 |
| `backend-foundations` | 后端基础：API、数据与上线 | API 设计、鉴权、数据持久化与真实部署 |

## 怎么开始

先用 CC Quick Installer 安装并验证 Claude Code，再安装 Noob2Builder。Claude Code 官方个人 Skill 目录是 `~/.claude/skills/<skill-name>/`。

### 推荐：直接让 Claude Code 安装

打开 Claude Code，把下面整段发给它：

```text
请先运行 git --version 检查 Git；没有就帮我安装并验证。
然后把 https://github.com/Alan-Youngzhe/noob2builder.git
安装到 ~/.claude/skills/noob2builder。
如果目录已经存在，先检查本地修改，不要覆盖；只有干净的 Git 仓库才执行 git pull --ff-only。
最后运行 python3 ~/.claude/skills/noob2builder/scripts/validate_school.py 验证，并告诉我真实输出。
```

### macOS / Linux 一行安装或更新

```bash
curl -fsSL https://raw.githubusercontent.com/Alan-Youngzhe/noob2builder/main/scripts/install.sh | bash
```

### Windows PowerShell 一行安装或更新

```powershell
irm https://raw.githubusercontent.com/Alan-Youngzhe/noob2builder/main/scripts/install.ps1 | iex
```

只从本仓库官方地址运行脚本；想先检查内容时，打开对应脚本链接阅读后再执行。安装器不会覆盖本地修改：目标目录不是 Git 仓库或存在未提交变化时会停止。

### 验证并入学

1. 新开一个 Claude Code 会话；
2. 输入 `/noob2builder 带我看选修课`，或直接说“带我学 AI”；
3. 确认导师展示课程目录，而不是只回答一段通用 AI 介绍；
4. 更新时重复运行同一个安装命令，再检查 `manifest.json` 版本。

## 校友墙

完成任意一项里程碑（第一个 PR、第一个发布作品、第一个 Agent、一次测试闭环或 agentic 改造），先创建“加入校友墙” Issue，再向 [WALL.md](WALL.md) 提交 PR，留下证据和一句话复盘。

## 项目结构

```
SKILL.md            教务处：导师的工作规则与课程路由
manifest.json       版本与文件清单
references/
  catalog.md        课程目录
  pedagogy.md       教学法细则
  courses/          14 门课程的教案
  lessons/          各课程的具体课节与实验
  lessons/shared/   安全、Web、数据库、HTTP 状态码与证据卡等共享节点
WALL.md             校友墙
```

## 状态

Alpha (v0.6.0)。课程内容持续迭代中，欢迎 Issue 和 PR。

## 许可

- 课程 Markdown：[`CC BY-NC-SA 4.0`](https://creativecommons.org/licenses/by-nc-sa/4.0/)，允许署名、非商业、相同方式共享的学习与改编；
- 代码与自动化：MIT；
- 第三方材料仍遵循各自许可。

完整边界见 [LICENSE](LICENSE)。
