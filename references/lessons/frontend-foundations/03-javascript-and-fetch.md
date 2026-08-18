# 让页面动起来：JavaScript 与 fetch

## 目标

学生理解 JS 通过"事件 → 改 DOM → 页面变化"工作，知道 `fetch` 是前端向外界要数据的入口，并能在 Network 面板里看到一次真实请求。

## 讲授

JavaScript 是页面里唯一的编程语言。核心循环：用户操作触发事件（click、input），事件处理函数修改数据或 DOM，页面随之更新。`document.querySelector` 找到元素，`addEventListener` 挂上响应，`textContent` 改掉内容——三板斧覆盖了大多数交互。

`fetch(url)` 发起 HTTP 请求拿回数据（通常是 JSON）。它是异步的：请求发出去页面不卡住，数据到了才执行后续。请求失败、返回错误状态码、返回空数据是三种不同情况，界面应分别解释。看到状态码时分不清含义，加载 `../shared/http-status-codes.md`。

常见误区：以为 JS 改了数据 HTML 文件就会变；把 API Key 写进前端代码（应加载 `../shared/safety-and-secrets.md`）；请求失败时页面毫无提示。

## 实验

给页面加上交互：点击按钮，用 `fetch` 调一个公开 API（如 `https://api.github.com/zen` 或任一无鉴权接口），把返回文本追加到列表里。然后：

1. 打开 Network 面板，点按钮，找到这次请求，看状态码和响应体；
2. 断网再点一次，观察控制台报错，让 Agent 补一个失败提示，学生复测；
3. 学生在 Console 里手动执行一次 `document.querySelector('h1').textContent = '改过'`。

## 证据

Network 面板里一次成功请求和一次失败请求的截图；页面在断网时有可见的失败提示而非静默。
