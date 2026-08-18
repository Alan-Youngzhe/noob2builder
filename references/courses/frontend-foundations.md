# ⑫ 前端基础：三件套与工程化

状态：alpha

## 唯一承诺

学生不再把 Agent 生成的网页当成黑盒：能看懂 HTML、CSS、JavaScript 各自负责什么，能用 npm 装依赖、用 Vite 起项目、看懂构建产物，并能用 TypeScript 类型指出 Agent 代码里的真实错误。

## 节点与 lesson

| 节点 | 文件 |
|---|---|
| 网页是怎么来的：HTML 与 DOM | `../lessons/frontend-foundations/01-html-and-dom.md` |
| 样式与布局：CSS | `../lessons/frontend-foundations/02-css-and-layout.md` |
| 让页面动起来：JavaScript 与 fetch | `../lessons/frontend-foundations/03-javascript-and-fetch.md` |
| 依赖从哪来：npm 与 package.json | `../lessons/frontend-foundations/04-npm-and-dependencies.md` |
| 开发到产物：Vite 与构建 | `../lessons/frontend-foundations/05-vite-and-build.md` |
| 写给 Agent 看的规格：TypeScript | `../lessons/frontend-foundations/06-typescript.md` |

## 教学边界

- 目标不是手写代码能力，而是"看得懂、改得动、验得出"。学生可以让 Agent 写代码，但必须能解释每一层在做什么。
- 不要求背标签、属性或 API；要求会用浏览器开发者工具查证。
- Node.js 安装按学生环境处理；安装或网络不可用时，前三个 lesson（纯浏览器即可完成）不受影响，后三个降级为纸面链路并标记 `simulated`。
- 这里只到"能跑起来的工程化前端"，组件化、框架和路由属于 `../courses/frontend-framework.md`。

## 完成证据

- 一个手写（可借助 Agent）的三件套页面，学生能在 DevTools 里指出结构、样式和脚本各自的位置；
- 一个 `npm init` + Vite 创建的真实项目，`npm run dev` 和 `npm run build` 都真实运行过，学生能说清 `node_modules`、`package-lock.json` 和 `dist/` 是什么；
- 至少一处 TypeScript 类型错误被学生（而非 Agent 悄悄改掉）定位并解释；
- 每个实验的真实命令输出或截图，不接受 Agent 自述完成。
