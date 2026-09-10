# ⑭ 后端基础：API、数据与上线

状态：alpha

## 唯一承诺

学生理解"不能只信浏览器的事"为什么必须由后端承担，能设计一个最小 API、说清数据存哪、谁能访问，并把服务部署到真实可访问的地址。

## 适合什么时候选

- 分不清哪些功能该放前端、哪些必须放后端；
- 密钥不知道放哪，或者已经写进前端了；
- 数据存在浏览器里，换台设备就没了；
- 本地能跑，但没让任何人真正访问过；
- 接口时好时坏，不知道该看哪里的日志。

## 节点与 lesson

| 节点 | 文件 |
|---|---|
| 这件事为什么不能放前端 | `../lessons/backend-foundations/01-frontend-backend-boundary.md` |
| 先约定接口，再写实现 | `../lessons/backend-foundations/02-api-design.md` |
| 选一个服务端方案，并说出为什么 | `../lessons/backend-foundations/03-choose-server-stack.md` |
| 数据存哪：先画权威源，再选工具 | `../lessons/backend-foundations/04-persistence.md` |
| 登录、权限和密钥是三件事 | `../lessons/backend-foundations/05-auth-and-secrets.md` |
| 部署：让别人真的能打开 | `../lessons/backend-foundations/06-deploy-and-verify.md` |

共享节点：`../lessons/shared/web-product-foundations.md`（链路图）、`../lessons/shared/http-status-codes.md`（状态码）、`../lessons/shared/database-and-data-authority.md`（权威源）、`../lessons/shared/safety-and-secrets.md`（密钥）。

## 这门课的核心判断

```text
涉及秘密、权限、持久化或共享 → 必须有后端
→ 先签接口合同，再写实现
→ 先定数据的唯一权威源，再选数据库
→ 每个接口独立检查权限，不假设前面查过
→ 部署后用另一台设备真实访问才算完成
```

框架不统一指定。让 Agent 基于学生的语言、需求、部署目标和水平提出两个方案并说明迁移成本，学生拍板。

## 铁律与证据

- 前端校验不当作安全；密钥不进前端、不进 Git、不进聊天记录；已泄露的密钥必须吊销重发，删文件不够；
- 验收必须包含：真实 HTTP 请求的成功与失败响应、跨入口和跨重启的数据读写、一次部署后从外部网络的真实访问；
- 越权测试（用 A 的身份访问 B 的资源）结果必须如实记录，漏了就写漏了并附修复后的复测；
- 完成需要一张链路图（用户动作 → API → 数据）、一份接口约定、一份选型说明、鉴权与密钥处理说明、部署后的真实访问证据和日志面板截图；
- 无法真实制造的场景（没有第二台设备等）标记为 `simulated`，不写成验证通过。
