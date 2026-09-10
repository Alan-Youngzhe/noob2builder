# 学习存档结构

默认文件：`~/.noob2builder/me.json`。

```json
{
  "schema_version": "1.0",
  "handle": "me",
  "last_seen": "2026-08-15",
  "current_course": null,
  "current_lesson": null,
  "ability_profile": {
    "computer": "unknown",
    "agent": "beginner",
    "git": "unknown",
    "builder": "unknown"
  },
  "learner_profile": {
    "field": null,
    "role": null,
    "daily_tools": [],
    "analogy_mode": "ask",
    "working_analogies": [],
    "failed_analogies": []
  },
  "courses": {},
  "current_project": null,
  "evidence": [],
  "unverified": [],
  "questions": [],
  "next_recommended": null,
  "log": []
}
```

## 学习者背景

开课前的简短开场用来填这一段，学生可以拒答或随时修改。

```json
{
  "field": "护理 | 建筑施工 | 会计 | 电商运营 | 高中语文 | null",
  "role": "学生在这个领域实际干的活，一句话",
  "daily_tools": ["他每天真在用的软件或系统"],
  "analogy_mode": "ask | on | off",
  "working_analogies": [
    { "concept": "context", "analogy": "交班时必须写全的交接单", "verified_by": "学生自己复述正确" }
  ],
  "failed_analogies": [
    { "concept": "token", "analogy": "记账凭证", "reason": "学生反而以为 token 有金额面值" }
  ]
}
```

- `analogy_mode` 为 `ask` 时，开场问一次；`on` 表示学生同意用本行业说法讲；`off` 表示他要求用标准术语，之后不再问。
- `working_analogies` 只记录**学生自己复述正确过**的类比，没验证过的不写。
- `failed_analogies` 同样重要：类比误导过学生就必须记下来，后面的课不许再用。
- 这一段只存学习相关背景，不存单位名称、职务、同事姓名、客户信息或任何可定位到具体个人的内容。

## 课程记录

```json
{
  "status": "available | in-progress | paused | completed",
  "lessons": {
    "lesson-id": {
      "status": "not-started | in-progress | completed | simulated | blocked",
      "comprehension": "unknown | shaky | working | solid",
      "artifacts": [],
      "evidence": [],
      "failures": [],
      "unverified": []
    }
  }
}
```

## 写入规则

- 每完成一个动作就安全地覆盖写入合法 JSON；写入后重新读取确认。
- 不记录 API Key、账号密码、客户原始数据、完整隐私信息或未经授权的仓库内容。
- 未真实运行的实验只能标 `simulated` 或 `blocked`。
- 学生可以随时要求查看、修改或删除存档。
- 没有统一学分、必修课或总完成率；每门课独立记录。
