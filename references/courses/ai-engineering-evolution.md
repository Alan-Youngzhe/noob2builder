# ⑥ 从 Prompt 到 Graph：AI Engineering 演化史

状态：alpha

## 唯一承诺

拆开 Prompt、Context、Harness、Loop、Graph 五个流行词，用同一个真实任务逐层实验，判断它们各自在补什么能力短板，以及什么时候只是包装。

## 适合什么时候选

- 被"多 Agent""自主循环""Agent 编排"之类的词弄糊涂；
- 提示词越写越长，效果却没见好；
- 想做一个 AI 工作流但不知道该做到多复杂；
- 想判断一个 AI 产品宣传的架构是真有用还是在包装。

## 节点与 lesson

| 节点 | 文件 |
|---|---|
| 第一层：Prompt 能解决什么，不能解决什么 | `../lessons/ai-engineering-evolution/01-prompt.md` |
| 第二层：Context 解决"它不知道" | `../lessons/ai-engineering-evolution/02-context.md` |
| 第三层：Harness 让环境替你守规矩 | `../lessons/ai-engineering-evolution/03-harness.md` |
| 第四层：Loop 什么时候值得，什么时候是烧钱 | `../lessons/ai-engineering-evolution/04-loop.md` |
| 第五层：Graph 和多 Agent，多数时候你不需要 | `../lessons/ai-engineering-evolution/05-graph.md` |
| 收尾：最小充分架构 | `../lessons/ai-engineering-evolution/06-minimum-sufficient.md` |

五节课共用**同一个真实任务和同一组 5 个样本**，第一节选定后不换，每一层都和前一层对比数据。

## 五层判断

- Prompt：把意图表达成模型更容易完成的输入；
- Context：准备任务所需的正确资料、状态、工具和约束；
- Harness：让环境提供稳定规则、命令、权限、验证和恢复；
- Loop：对可重复、可评分、可恢复的任务自动迭代；
- Graph：当多个节点存在明确依赖、共享状态和不同验证器时显式编排。

```text
从 Prompt 往上逐层加
→ 每加一层都要指出上一层解决不了的具体问题
→ 加到正确率满足需求就停
→ 去掉某层不会坏的，就该去掉
```

## 完成证据

- 一个真实任务、5 个真实样本，以及贯穿五层的正确率和成本数据；
- 一份可执行的验证脚本，及其与人工判断的一致率；
- Loop 层的人工复核记录，含"验证通过但实际错误"的案例（如有）；
- 一份最小充分架构说明，按该架构重跑的结果，以及独立 Agent 的交接测试；
- 一份用五层框架对真实 AI 产品的拆解；
- 学生能用自己的数据说清为什么"多 Agent""循环十次"或"画成图"不自动提升质量。
