# ⑪ 测试与验证：让 Agent 的“完成”变成证据

状态：beta

## 唯一承诺

学生能从 PRD 和真实风险出发，选择合适的测试层级，写出并实际运行单元测试、集成测试、冒烟测试和关键 E2E；知道测试结果的边界，不再把 Agent 的“测试通过”当成事实。

## 适合什么时候选

- 项目已经能跑，但不敢让 Agent 继续改；
- 不知道单元、集成、冒烟和 E2E 的区别；
- 测试很多却仍然经常回归；
- 想把项目接入 `verify`、CI 或独立 Review；
- 需要为数据库、权限、支付、删除或外部服务建立证据。

不要求先固定测试框架。让 Agent 先识别仓库已有的 runner 和命令，再采用项目最小可用方案。

## 节点与 lesson

| 节点 | 文件 |
|---|---|
| 为什么测试：Agent 的肯定句不是证据 | `../lessons/testing-verification/01-tests-as-evidence.md` |
| 测试层级与测试矩阵 | `../lessons/testing-verification/02-layers-and-matrix.md` |
| 单元测试：保护纯逻辑 | `../lessons/testing-verification/03-unit-tests.md` |
| 集成测试：保护模块边界 | `../lessons/testing-verification/04-integration-tests.md` |
| 冒烟与 E2E：保护真实路径 | `../lessons/testing-verification/05-smoke-and-e2e.md` |
| 回归、Mock、Flaky Test 与覆盖率 | `../lessons/testing-verification/06-regression-and-misconceptions.md` |
| `verify`、CI 与独立 Review | `../lessons/testing-verification/07-ci-and-review.md` |

## 测试层级的核心判断

```text
尽量在最便宜、最稳定的层验证
→ 低层无法证明时再上移
→ 发布前用少量冒烟确认系统还活着
→ 关键用户旅程用 E2E 保护
```

测试数量和覆盖率不是目标。关键行为、历史 Bug、权限、数据、金钱、删除和外部依赖才是优先级。

## 完成证据

- 一张从验收标准生成的风险与测试矩阵；
- 至少一个单元测试、一个集成测试、一组冒烟检查和一个关键 E2E 或等价用户行为验收；
- 一次真实的 RED → 修复 → GREEN 回归闭环；
- 测试命令、退出码、环境、未覆盖风险和失败原因都有记录；
- 没有使用生产数据、真实密钥或不可控的第三方副作用；
- 独立 Agent 能根据 PRD、diff 和测试结果指出至少一个风险或确认没有可行动问题。
