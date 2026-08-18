# 开发到产物：Vite 与构建

## 目标

学生理解"开发时写的代码"和"浏览器实际跑的代码"之间有一道构建工序，能用 Vite 起项目、看懂 dev server 和 `dist/` 产物的区别。

## 讲授

浏览器只认 HTML、CSS、JS，但现代项目写的是模块化的 `.js/.ts/.vue/.tsx` 文件，还要压缩、打包、处理静态资源。Vite 是完成这道工序的构建工具：`npm run dev` 起一个开发服务器，改代码页面即时更新（热更新）；`npm run build` 产出 `dist/`——一堆压缩过的静态文件，部署就是把它们放上一个能被访问的服务器。

这也解释了 localhost：`npm run dev` 给出的 `http://localhost:5173` 只有本机可见，要让真实用户访问必须构建 + 部署。

常见误区：把源码目录直接丢到服务器；dev 能跑就以为 build 也能过（类型错误、未使用的导入常常只在 build 时炸）；在 dev server 里验收性能。

## 实验

1. `npm create vite@latest vite-lab -- --template vanilla`（若交互提示不可用则让 Agent 手动搭一个等价结构），进入后 `npm install`；
2. `npm run dev`，浏览器打开，改一行文字确认热更新；
3. `npm run build`，打开 `dist/` 看产物：文件名带 hash 的压缩 JS/CSS；
4. 用 `npm run preview` 或任意静态服务器访问构建产物，确认和 dev 行为一致；
5. 让学生画一张链路：源码 → dev server（开发用）/ build → dist（部署用）→ 用户浏览器。

## 证据

`dev` 和 `build` 的真实终端输出；`dist/` 目录截图；学生能回答"部署上去的是哪个目录、为什么"。
