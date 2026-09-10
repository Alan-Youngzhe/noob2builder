# ⑤ 从 Vibe Coding 到 Agentic Engineering

状态：alpha

## 唯一承诺

带一个已经能跑但不敢改的项目入场，为它补上规格、测试、机器门禁、独立 Review 和上线观察，让 Agent 可以继续在上面工作而你不再赌。

## 适合什么时候选

- 项目能跑，但你不敢让 Agent 继续改；
- 它一次改十五个文件，你不知道哪个改坏了；
- 有些代码连你自己都说不清是干嘛的；
- 每次上线都靠"应该没问题"；
- 想让 Agent 更自主地干活，但不知道怎么给它设护栏。

## 节点与 lesson

| 节点 | 文件 |
|---|---|
| 先给项目做体检，别急着改 | `../lessons/agentic-engineering/01-project-checkup.md` |
| 什么叫"好代码"：五个可检查的标准 | `../lessons/agentic-engineering/02-code-qualities.md` |
| 从行为清单生成测试矩阵 | `../lessons/agentic-engineering/03-test-matrix.md` |
| 一次真实的 RED → 修复 → GREEN | `../lessons/agentic-engineering/04-regression-test.md` |
| 小切片、小 diff、验证、commit | `../lessons/agentic-engineering/05-agent-loop.md` |
| 一条 verify 命令，和一道机器门禁 | `../lessons/agentic-engineering/06-verify-and-ci.md` |
| 独立 Review、上线观察与经验回流 | `../lessons/agentic-engineering/07-review-and-observe.md` |

需要系统补测试概念时转 `./testing-verification.md`；涉及持久化、多进程或多端时插入 `../lessons/shared/database-and-data-authority.md`；处理密钥时插入 `../lessons/shared/safety-and-secrets.md`。

## 这门课的核心判断

```text
先把未知变成清单，体检期间不改代码
→ 按风险排序，不按难度排序
→ 每轮改动小到能看懂、能验证、能回退
→ 检查合成一条 verify，交给机器守
→ Review 必须换上下文，自查不算
→ 上线后用真实信号确认，经验必须回流
```

测试数量和覆盖率不是目标。关键行为、历史 Bug、权限、数据、金钱、删除和外部副作用才是。

## 完成证据

- 四张体检清单，未知清单不少于 5 条，体检期间 `git status` 干净；
- 一张从行为和风险生成的测试矩阵，含至少 3 条显式的"不测"及理由；
- 一次完整的 RED → 修复 → GREEN 记录，**RED 的失败输出必须在场**，只有 GREEN 不予认可；
- 一串小 commit，含至少一次 diff 审查发现"Agent 做了没要求的事"的记录，和一次触发止损线的回退；
- 一条 `verify` 命令，成功与失败两次输出俱全；CI 真实拦截过一次红色 PR，分支保护已开启；
- 一次换上下文的独立 Review，含误报记录和至少一个被发现并修复的真问题；
- 上线后 24 小时观察记录、一条真实用户反馈、本轮回流的具体产物；
- 涉及数据库时还需要一张进程/数据流图和明确的逻辑权威源。
