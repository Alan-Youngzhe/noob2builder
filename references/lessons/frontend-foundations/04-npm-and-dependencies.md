# 依赖从哪来：npm 与 package.json

## 目标

学生理解现代前端项目不是一堆文件而是"声明 + 依赖"：能看懂 `package.json`，知道 `node_modules`、锁文件和语义化版本各自的作用，能判断一条 `npm install` 做了什么。

## 讲授

npm 是 JavaScript 的包管理器。`package.json` 是项目的身份证：名字、脚本（`scripts`）、依赖清单（`dependencies` 运行时要用，`devDependencies` 只有开发时要用）。`npm install` 按清单把依赖下载到 `node_modules`——这个目录通常巨大且不进 Git，因为它可以随时按清单重建。

锁文件（`package-lock.json`）记录每个包实际装的是哪个精确版本，保证学生和 Agent、CI 装出同一棵树。版本号 `^1.4.2` 的 `^` 表示"兼容更新"，这是"昨天还好好的"最常见的来源之一。

`npm run xxx` 执行 `scripts` 里定义的命令，比如 `dev`、`build`、`test`——Agent 说"跑一下"时，学生要知道跑的是哪条。

常见误区：把 `node_modules` 提交进 Git；删了锁文件"重装试试"；分不清全局安装和项目安装。

## 实验

在有 Node.js 的机器上（没有就先装并验证 `node --version`）：

1. `mkdir npm-lab && cd npm-lab && npm init -y`，打开生成的 `package.json` 逐字段讲一遍；
2. 装一个小依赖（如 `npm install dayjs`），观察 `package.json` 多了什么、`node_modules` 和锁文件出现了；
3. 删掉 `node_modules`，跑 `npm install`，确认它按锁文件完整恢复；
4. 在 `scripts` 里加一条 `"hello": "echo hi"`，用 `npm run hello` 执行。

## 证据

学生能回答三个问题：换一台电脑怎么还原一模一样的依赖？`^` 和锁文件谁说了算？`npm run dev` 实际执行了什么？附真实命令输出。
