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
  "courses": {},
  "current_project": null,
  "evidence": [],
  "unverified": [],
  "questions": [],
  "next_recommended": null,
  "log": []
}
```

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
