# ③ AI Builder 工作法：从模糊想法到可验收任务

状态：alpha

## 唯一承诺

把“我想做个东西”变成 Agent 能执行、学生能判断对错的第一段交付，而不是靠一句神 Prompt 碰运气。

## 节点与 lesson

| 节点 | 文件 |
|---|---|
| Alan 默认 0→1 工作流 | `../lessons/builder-method/00-alan-default-workflow.md` |
| 别从 Prompt 开始 | `../lessons/builder-method/01-problem-before-prompt.md` |
| GrillMe 需求访谈与 PRD v0 | `../lessons/builder-method/02-interview-to-project-card.md` |
| Design System、Lovable、PRD v1 与 Spec | `../lessons/builder-method/03-choose-technology.md` |
| 砍成第一刀 | `../lessons/builder-method/04-vertical-slice.md` |
| 把完成写成证据 | `../lessons/builder-method/05-acceptance-and-debug.md` |

## Alan 方法的接入

进入本课程先读取 `../alan-field-notes.md`。Alan 的默认顺序是 `GrillMe → PRD v0 → Design System → Lovable 原型 → PRD v1 → Spec → 敏捷 MVP → 可行性验证 → 工程质量与交叉 Review`。它是默认案例，不是强制所有项目使用 Lovable 或同一技术栈。

## 完成证据

- PRD v0：用户、问题、目标、非目标、核心流程和成功标准；
- Design System、一版可见原型，以及基于原型反写的 PRD v1；
- 由 AI 起草、学生确认的 Spec；
- 一个未参加前序讨论的 Agent 通过独立交接测试，能准确复述核心产品意图并给出大致收敛的实施计划；
- `DECISIONS.md`：方案理由、暂不需要什么和一个备选；
- `ACCEPTANCE.md`：至少三个具体样例，含一个失败或边界样例；
- 学生否决或修改过 Agent 的一项错误假设；
- 第一刀能在 30–60 分钟或一个短工作段内独立验收。
