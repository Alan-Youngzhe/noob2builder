# ② Git & GitHub：让作品有记忆、能协作

状态：alpha

## 唯一承诺

学生不必背命令，但能让 Agent 安全获得 Git、看懂一次 diff 和 commit、理解 Issue/PR，并完成一次真实 GitHub 贡献。

## 节点与 lesson

| 节点 | 文件 | 依赖 |
|---|---|---|
| Git 是项目的时光机 | `../lessons/git-github/01-git-as-memory.md` | 无 |
| 让 Agent 检查并安装 Git | `../lessons/git-github/02-install-and-verify.md` | 安全节点 |
| 改一次、看一次、回一次 | `../lessons/git-github/03-diff-commit-restore.md` | Git 可用 |
| GitHub 是协作现场 | `../lessons/git-github/04-issue-pr-review.md` | 网络与账号按需 |
| 第一次真实 PR | `../lessons/git-github/05-school-pr.md` | 前四节或已有经验 |

## 动态排课

- 完全不会：按表中顺序。
- Git 已安装但不会使用：从第三节开始。
- 会 Git 不会协作：从第四节开始。
- 熟练开发者：直接第五节，用实际 PR 暴露缺口。

## 完成证据

- `git --version` 真实输出；
- 一个练习仓库、至少两个有意义的 commit；
- 学生能从 diff 指出实际变化；
- 学校仓库 Issue 和 PR 已创建；
- PR 中没有密钥和隐私数据。

创建 PR 即完成课程动作；合并由维护者审核。
