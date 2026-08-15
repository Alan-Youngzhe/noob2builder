# ③ AI Builder 工作法：从模糊想法到可验收任务

状态：alpha

## 唯一承诺

把“我想做个东西”变成 Agent 能执行、学生能判断对错的第一段交付，而不是靠一句神 Prompt 碰运气。

## 节点与 lesson

| 节点 | 文件 |
|---|---|
| 别从 Prompt 开始 | `../lessons/builder-method/01-problem-before-prompt.md` |
| 让 Agent 采访你 | `../lessons/builder-method/02-interview-to-project-card.md` |
| 让 Agent 调查技术方案 | `../lessons/builder-method/03-choose-technology.md` |
| 砍成第一刀 | `../lessons/builder-method/04-vertical-slice.md` |
| 把完成写成证据 | `../lessons/builder-method/05-acceptance-and-debug.md` |

## Alan 方法的接入

按需读取 `../alan-field-notes.md`。小项目使用一页项目卡；只有存在数据库且跨多个工程期次时，才建议拆 PRD 与 Spec。`project-template` 是进阶参考，不是固定栈。

## 完成证据

- `PROJECT.md`：用户、场景、问题、输入、输出、非目标；
- `DECISIONS.md`：推荐方案、理由、暂不需要什么和一个备选；
- `ACCEPTANCE.md`：至少三个具体样例，含一个失败或边界样例；
- 学生否决或修改过 Agent 的一项错误假设；
- 第一刀能在 30–60 分钟或一个短工作段内独立验收。
