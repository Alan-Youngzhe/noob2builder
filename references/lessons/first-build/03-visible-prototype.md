# Design System、Lovable 原型、PRD v1 与 Spec

## 目标

先给产品一套轻量设计约束，再生成可见原型、纠正需求，并把拍板结果沉淀成 PRD v1 和 Spec。

## 讲授

原型不是为了先把页面画漂亮，而是为了发现需求。Alan 的 Web 默认顺序是：

```text
PRD v0
→ Design System
→ Lovable 原型
→ 原型 Review
→ 反写 PRD v1
→ AI 产出 Spec
```

Design System 先确定产品语气、颜色角色、字体层级、间距、圆角、组件规则和关键交互状态，避免 Lovable 无约束地拼出一套随机界面。第一版保持轻量，不写成庞大的品牌手册。

Lovable 把抽象需求变成可以判断的页面。学生不用手画，但必须真实查看原型，逐项反馈和拍板。方向确定后，Agent 把原型中的产品决策反写为 PRD v1，再根据 PRD v1、Design System 和原型产出 Spec。原型代码不自动等于生产代码。

好的 PRD v1 要让团队实现收敛：即使是单人开发，也把 AI 当成另一个开发者。把同一份 PRD v1、Design System 和原型交给不同开发者或 AI，他们的技术实现可以不同，但对用户、核心流程、范围、关键交互状态和完成标准的理解应当大差不差。

## 实验

1. 收集 2–3 个相关参考，注明喜欢的是结构、交互还是视觉，不整站抄袭。
2. 从 PRD v0 和参考生成最小 `DESIGN_SYSTEM.md`。
3. 把 PRD v0 与 Design System 交给 Lovable，生成核心流程原型；无法使用时选 baoyu-design 或合适替代。
4. 检查 Default、Hover/Focus、Loading、Empty、Success、Error、Disabled 中真正相关的状态。
5. 学生标记保留、删除、修改和新增；让目标用户或同学尝试一次。
6. Agent 输出 PRD v1 和 v0 → v1 变更摘要。
7. 让一个未参加前序讨论的独立 Agent 只读 PRD v1、Design System 和原型，复述产品意图、提出实施计划和必须澄清的问题；仍需猜核心决策就继续反写 PRD。
8. 交接测试通过后，AI 输出 `SPEC.md`：技术方案、数据、接口、约束、验收、风险、非目标与备选。

## 证据

Design System、原型地址或本地文件、一次方向修改、PRD v1、独立交接测试、Spec 和拍板记录。不同 Agent 对核心产品行为的理解大致收敛。
