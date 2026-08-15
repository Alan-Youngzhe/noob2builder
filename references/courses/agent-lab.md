# ⑩ Agent 构建实验室：从 ReAct 到可验收 Agent

状态：alpha

## 唯一承诺

学生不必先手写 Agent 框架，但能看懂一次 Agent Loop，让 Agent 帮他实现真实工具调用，并用任务集验证它不是“看起来聪明”。

## 节点与 lesson

| 节点 | 文件 |
|---|---|
| 拆开 Agent Loop | `../lessons/agent-lab/01-agent-loop.md` |
| 给 Agent 一个真实工具 | `../lessons/agent-lab/02-tool-calling.md` |
| Context、Memory 与资料 | `../lessons/agent-lab/03-context-memory-rag.md` |
| Eval：故意让它失败 | `../lessons/agent-lab/04-evaluate-and-repair.md` |

## 教学边界

- Hello Agents 是外部参考教材，不整章复制；来源和许可见 `../sources.md`。
- Python、低代码平台或 Agent 框架均按任务选择，不做统一要求。
- Agentic RL、多智能体社会模拟和自研完整框架不进入 Alpha 主线。
- 不需要从头啃文档，但必须让 Agent 查权威文档、标出版本，并通过实际运行验证。

## 完成证据

- 一张可解释的 Agent Loop 图；
- 至少一个真实工具调用；
- 五条最小任务集，包含成功、缺 Context、工具失败和错误输出；
- 至少修复一个真实失败并重跑；
- 一个别人可以触发的 Agent、Skill 或工作流入口。
