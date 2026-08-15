# ⑨ LLM 与 Agent 原理：从接下一个 Token 到调用工具

状态：beta

## 唯一承诺

沿一次真实请求理解 LLM 怎样逐 token 生成、Context 怎样随请求发送、Agent 怎样提出并执行工具调用，以及 KV Cache 为什么不是长期记忆。

## 教学节点

1. LLM 的基础动作是预测下一个 token，但能力不等于随机接词；
2. User Prompt、System Prompt 与一次请求；
3. Context、Memory、KV Cache 与 Prompt Cache；
4. 中转层、模型服务和数据路径；
5. Search、RAG 与私有资料；
6. Function Calling、ReAct、MCP、Skill 和 Subagent；
7. 2022–2026 Agent 系统能力如何随模型和工程共同演化。

## 最小实验

比较无工具回答、搜索回答和私有资料回答，观察一次可见的工具调用循环，输出 `MY_REQUEST_FLOW.md`。

## 完成证据

学生能画出自己的请求链路，并解释缓存、记忆和资料检索的区别。本课程正在拆分独立 lesson。
