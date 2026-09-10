# ⑨ LLM 与 Agent 原理：从接下一个 Token 到调用工具

状态：alpha

## 唯一承诺

沿一次真实请求理解 LLM 怎样逐 token 生成、Context 怎样随请求发送、Agent 怎样提出并执行工具调用，以及缓存为什么不是长期记忆。

## 适合什么时候选

- 不知道自己每次对话到底发出去了什么；
- 搞不清 Context、记忆和缓存的区别；
- 想知道"它为什么会编造一个不存在的函数"；
- 分不清 MCP、Skill、Tool 和 Subagent；
- 在意自己的代码和数据流向了哪里。

## 节点与 lesson

| 节点 | 文件 |
|---|---|
| 基础动作是接下一个 token，但不是随机接词 | `../lessons/llm-agent/01-next-token.md` |
| 一次请求里到底发生了什么 | `../lessons/llm-agent/02-one-request.md` |
| Context、Memory 与缓存：三个常被混为一谈的东西 | `../lessons/llm-agent/03-context-memory-cache.md` |
| 你的数据走了哪条路：中转层、模型服务与合规边界 | `../lessons/llm-agent/04-data-path.md` |
| 它凭什么知道：训练、搜索与私有资料 | `../lessons/llm-agent/05-search-and-rag.md` |
| 从"会说"到"会做"：工具调用、ReAct 与 MCP | `../lessons/llm-agent/06-tools-and-agents.md` |

第一次处理 API Key 或私有数据时插入 `../lessons/shared/safety-and-secrets.md`。

## 这门课的核心判断

```text
模型只负责输出下一个 token
→ 它能做的事，取决于宿主给了什么工具
→ 它知道的事，取决于这次 Context 里放了什么
→ 所以"它怎么不记得 / 怎么不会"要先查请求里有没有，再怀疑模型
```

事实性内容中，厂商与模型系列的对应关系可以直接讲死；版本号、价格、Context 上限和缓存时长属于会变的部分，现场查证并标注时效。

## 完成证据

- 一份 `MY_REQUEST_FLOW.md`，画出学生自己的真实请求链路：system、历史、资料、工具调用、执行、结果回灌；
- 至少一次亲手抓到的模型编造，附完整报错原文；
- 三种"知道"的对照实验记录，其中一条经学生亲自核实；
- 一次真实工具调用记录，能逐步指出哪一步是模型、哪一步是宿主；
- 能不用比喻说清 Tool、MCP、Skill、Subagent 各自解决什么问题；
- 能指出本机真实承担 Memory 角色的文件，并完成一次"改文件 → 新会话生效"的验证。
