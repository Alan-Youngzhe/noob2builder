# ⑬ 前端框架：组件化与项目结构

状态：alpha

## 唯一承诺

学生拿到 Agent 生成的一个 React 或 Vue 项目不再发怵：能解释组件、props、state、TSX 和路由各是什么，能判断项目结构是否合理，并能指挥一次"行为不变"的重构并用证据验收。

## 节点与 lesson

| 节点 | 文件 |
|---|---|
| 为什么需要框架 | `../lessons/frontend-framework/01-why-frameworks.md` |
| 组件化：props、state 与组合 | `../lessons/frontend-framework/02-components.md` |
| Vue 与 React：同一功能写两遍 | `../lessons/frontend-framework/03-vue-and-react.md` |
| TSX 与模板：类型安全的 UI | `../lessons/frontend-framework/04-tsx-and-templates.md` |
| 路由与页面组织 | `../lessons/frontend-framework/05-routing.md` |
| 项目结构与一次真实重构 | `../lessons/frontend-framework/06-project-structure-refactor.md` |

## 教学边界

- Vue 和 React 都教概念、各写一遍最小实现，但深入实操的项目由学生选一个；不做统一要求，也不比较"哪个更好"。
- 前置是 `../courses/frontend-foundations.md` 的 npm、Vite、TypeScript；学生缺哪块就回去补哪块，不重讲。
- 不讲框架源码、虚拟 DOM 原理、状态管理库选型；学生在真实项目撞上时再按需展开。
- 界面状态与验收沿用 `../lessons/shared/web-product-foundations.md` 的标准，本课程只补充"代码怎么组织"。

## 完成证据

- 同一个小组件（如计数器）的原生 JS 版与框架版各一份，学生能讲清两者状态管理的差异；
- 一个用学生选定框架搭的多页面小应用：至少两个路由页面、三个以上组件、TSX/模板里有真实类型标注；
- 一次真实重构记录：重构前后行为对比证据（截图或测试），diff 可读；
- 学生能画出自己项目的目录结构图并说明"新功能该加在哪、为什么"。
