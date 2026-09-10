# ⑧ 计算机与网络基础：看懂 Agent 正在做什么

状态：alpha

## 唯一承诺

不学计算机专业，也能看懂 Agent 正在操作的文件、终端、权限、进程、URL、端口、localhost 和网络访问，并知道问题大致发生在哪一层。

## 适合什么时候选

- 不敢碰终端，看到黑框就想关掉；
- Agent 说"改好了"，但不知道它改的是哪个文件；
- 本地跑起来了，发给别人却打不开；
- 一报错就把整段错误甩给 Agent，然后陪它盲试；
- 分不清 localhost、端口、域名和 IP。

## 节点与 lesson

| 节点 | 文件 |
|---|---|
| Agent 在动哪个文件：目录、路径与扩展名 | `../lessons/computer-network/01-files-and-paths.md` |
| 终端、命令与进程：Agent 的手在哪里 | `../lessons/computer-network/02-terminal-and-processes.md` |
| URL、DNS、IP 与端口：地址怎么找到机器 | `../lessons/computer-network/03-url-dns-port-localhost.md` |
| 本地能跑不等于别人能访问：可达性、代理与边界 | `../lessons/computer-network/04-reachability-and-boundaries.md` |
| Agent 更容易吃什么：格式、结构与输入方式 | `../lessons/computer-network/05-agent-friendly-input.md` |
| 出问题先分层：请求、状态码与诊断卡 | `../lessons/computer-network/06-layered-diagnosis.md` |

第一次遇到危险命令或密钥时插入 `../lessons/shared/safety-and-secrets.md`；第一次看到 HTTP 状态码时插入 `../lessons/shared/http-status-codes.md`。

## 这门课的核心判断

```text
先确定问题在哪一层
→ 再选查这一层最便宜的命令
→ 用真实输出确认或推翻判断
→ 判断错了就回上一步重新分层，而不是继续猜
```

不要求背命令。要求学生能解释 Agent 刚才改了什么、在哪里、怎样恢复。

## 完成证据

- 能说出一个 Agent 刚操作过的文件的绝对路径，并确认它是不是自己以为的那个；
- 完成一次"启动服务 → 确认在跑 → 停止 → 确认停了"的真实闭环；
- 能解释"本地运行不等于别人可访问"，并指出自己这次卡在链路的哪一层；
- 至少把一份真实资料转成 Markdown/CSV/JSON，并说明为什么比原格式好用；
- 提交 `MY_DIAGNOSIS_CARD.md`，包含真实的 2xx、4xx 以及一次失败请求的输出；
- 无法真实制造的场景标记为 `simulated`，不写成验证通过。
