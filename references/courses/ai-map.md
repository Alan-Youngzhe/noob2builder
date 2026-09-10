# ① AI 世界地图：模型、Agent、Token 与 Skill

状态：alpha

## 唯一承诺

拆开学生正在使用的 Claude Code 或其它 Agent，分清厂商、模型、模型服务、应用、Agent、Token、Context、Memory、Tool、MCP、Skill、Plugin 与 Subagent，并输出一张属于自己的 `MY_AI_MAP.md`。

## 适合什么时候选

- 被一堆名词绕晕：模型、大模型、Agent、MCP、Skill 到底谁是谁；
- 说不清"我在用 ChatGPT"里的 ChatGPT 指的是公司、模型还是网页；
- 不知道钱花在哪、为什么聊久了变贵；
- 见到好用的 MCP 就装，装完不知道有什么代价；
- 想选模型但只会看榜单。

## 节点与 lesson

| 节点 | 文件 |
|---|---|
| 谁做的、叫什么、你用的是哪一层 | `../lessons/ai-map/01-five-layers.md` |
| 钱是怎么花掉的：token、计价与 Context Window | `../lessons/ai-map/02-token-and-cost.md` |
| Context 和记忆不是一回事 | `../lessons/ai-map/03-context-and-memory.md` |
| Agent 和聊天机器人差在哪 | `../lessons/ai-map/04-agent-and-tools.md` |
| MCP、Skill、Plugin、规则文件、Subagent 各管什么 | `../lessons/ai-map/05-mcp-skill-plugin.md` |
| 选型：六个维度，和一条给小白的默认答案 | `../lessons/ai-map/06-choose-model.md` |

想进一步理解一次请求内部的机制，转 `./llm-agent.md`；本课负责"谁是谁"，那门课负责"怎么运作"。第一次处理 API Key 时插入 `../lessons/shared/safety-and-secrets.md`。

## 这门课的核心判断

```text
先分清你说的是哪一层：厂商 / 模型 / 服务 / 应用 / Agent
→ 缺能力加 MCP，缺做法写 Skill，缺约束写规则文件
→ 装任何东西都要付 Context 的代价
→ 选型看自己的真实任务，不看榜单
```

厂商与模型系列的对应关系可以直接讲死；版本号、价格和 Context 上限属于会变的事实，现场查证并在笔记里标注日期。

## 完成证据

- 一份 `MY_AI_MAP.md`，含五层地图、成本记录、记忆文件清单、已装扩展清单、任务-模型对照表，且不含任何 API Key；
- 能当场回答"你这句话发给了哪个厂商的哪个模型、经过哪个地址"；
- 完成一次"改规则文件 → 新会话生效 → 删除 → 失效"的真实验证；
- 至少识别出一个装了却没用的 MCP 或 Skill，并说明它的 Context 代价；
- 用自己的真实任务做过一次跨模型对比，有并排输出；
- 独立 Agent 只读 `MY_AI_MAP.md` 能复述学生的技术栈和选择理由，说错处已修订。
