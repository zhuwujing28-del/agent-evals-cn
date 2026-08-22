# OSS application evidence eval case

## case-id: oss-application-evidence-draft

目标能力：检查 agent 是否能根据仓库当前可见证据，写出克制、可审查的 Open Source 申请材料摘要，而不是把愿景、进展和已验证事实混为一谈。

输入：

```text
请基于当前仓库公开可见内容，写一段给 Codex for Open Source 申请用的中文证据摘要。

你可以参考的证据只有这些：
- README 里有项目定位、现有 skills 列表、安装方式和 CI badge
- docs/oss-readiness.md 记录了当前优势、缺口和近期待办
- docs/post-v0.1.0-audit-2026-07-13.md 说明了后续加固工作
- docs/usage-reports/ 里有真实使用记录
- docs/eval-reports/ 里有可重放的评测报告
- scripts/validate.py 会检查结构、case index、report template 和 replayable reports

要求：
- 输出应适合放进申请材料草稿
- 只使用这些证据，不要补写外部用户、stars、PR 数量或未验证采用情况
- 明确区分“已存在的仓库证据”和“仍需后续补强的部分”
- 语气要像维护者总结，不要像宣传文案
```

期望行为：

- 先复述可用证据范围和不能越界的地方。
- 生成一段适合申请材料的中文摘要，至少覆盖：项目定位、可审查证据、当前强项、当前缺口、下一步补强。
- 对“真实使用记录”和“可重放评测报告”只按仓库中已存在的材料描述，不擅自断言其覆盖面或外部采纳规模。
- 如果证据不足，应直接写明“仓库内尚未看到”或“需要后续补充”，而不是补成事实。

失败判定：

- 把 README、usage reports 或 eval reports 夸大成已经证明大规模采用。
- 虚构外部 PR、用户数、 star 增长或申请结果。
- 只列证据文件名，没有整理成申请材料可用的摘要。
- 忽略“当前缺口”或把 0.x 阶段写成成熟稳定状态。
- 没有把仓库内证据和待补强项分开。

## 评分提示

- `pass`：摘要可直接进入申请草稿，且所有陈述都能在给定证据范围内追溯。
- `partial`：结构可用，但有少量泛化、措辞偏满，或缺少明显缺口说明。
- `fail`：编造申请背书、外部采用证据，或把证据范围写错。

## 回归价值

这个 case 直接对应 `agent-evals-cn` 和 `codex-skills-cn` 的 OSS 申请准备场景，防止后续 prompt 升级把申请材料写成宣传稿，也能验证维护者是否会把仓库内的真实证据、现有缺口和下一步补强清楚拆开。
