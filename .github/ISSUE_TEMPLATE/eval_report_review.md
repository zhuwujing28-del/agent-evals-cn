---
name: Eval report review
about: Submit a replayable eval run for maintainer review
title: "[Eval Report] "
labels: eval-report
assignees: ""
---

## 评测对象

请填写被评测的 skill、prompt、agent workflow 或自动化任务。

## 对应 case-id

请填写 `examples/*-case.md` 中的稳定 `case-id`。如果这是新场景，请先提交 eval case。

## 版本 / commit

请填写被测版本、commit SHA、模型/工具环境，以及是否有工具不可用。

## 可复跑输入

请粘贴脱敏后的用户请求、上下文摘要、文件片段或命令。不要包含 token、cookie、API key、私有仓库内容或未脱敏日志。

## 实际输出摘要

请概述 agent 的关键行为。只引用判断分数所需的最小输出片段。

## 评分

请按 `docs/scoring-rubric.md` 和 `docs/scoring-calibration.md` 给出证据化评分。

| 维度 | 分数 | 证据 |
| --- | --- | --- |
| correctness |  |  |
| usefulness |  |  |
| safety |  |  |
| brevity |  |  |

## 结果判定

请选择一个并说明理由：

- [ ] pass
- [ ] partial
- [ ] fail

## 分歧或不确定点

如果需要第二位 reviewer，请说明争议点、缺失证据或需要复跑的条件。

## 建议后续

请选择一个最小后续动作：更新 skill、修订 eval case、补充 replayable report、改进文档，或记录 known limitation。
