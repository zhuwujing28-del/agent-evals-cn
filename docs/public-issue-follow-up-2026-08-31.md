# Cross-repo Public Issue Follow-up - 2026-08-31

This note reconciles the open public issues in `codex-skills-cn` and
`agent-evals-cn` with the documentation, examples, and validation evidence
currently published on `main`. It gives maintainers a small, evidence-linked
follow-up plan without treating repository activity as external adoption.

## Snapshot

- Public check date: 2026-08-31
- `codex-skills-cn`: 1 star, 0 forks, 7 open issues; latest public head is
  `40bd1ba` (`Refresh skills roadmap`)
- `agent-evals-cn`: 1 star, 0 forks, 2 open issues; latest public head is
  `357a786` (`Refresh eval roadmap`)
- Both repositories' latest public validation workflows succeeded.
- `agent-evals-cn` currently indexes and validates 22 baseline eval cases.

## Recommended issue actions

### `codex-skills-cn`

| Issues | Current evidence | Suggested action |
| --- | --- | --- |
| #1 and #3, installation tutorial | [`codex-skill-installation.md`](https://github.com/zhuwujing28-del/codex-skills-cn/blob/main/docs/codex-skill-installation.md) covers Windows and PowerShell installation, bulk copy, updates, verification, and troubleshooting. | Treat as completed scope; post the guide link and close or consolidate the duplicate requests. |
| #4, skill / MCP boundary | [`codex-extension-boundaries.md`](https://github.com/zhuwujing28-del/codex-skills-cn/blob/main/docs/codex-extension-boundaries.md) documents skill, MCP, plugin, and personal-settings boundaries. | Treat as completed scope; keep a narrower issue only if a concrete missing scenario is reported. |
| #2 and #5, more workflow examples | [`example-index.md`](https://github.com/zhuwujing28-del/codex-skills-cn/blob/main/docs/example-index.md) and the published examples cover triage, review, onboarding, dependency upgrades, release notes, and maintainer feedback. | Consolidate the duplicate requests; keep #6 as the v0.2 umbrella for new evidence-backed examples. |
| #6, v0.2 maintainer examples | [`maintainer-workflow-session.md`](https://github.com/zhuwujing28-del/codex-skills-cn/blob/main/docs/examples/maintainer-workflow-session.md) is a current multi-skill example. | Keep open for additional real or sanitized maintainer sessions. |
| #7, maintainer feedback | [`maintainer_feedback_request.md`](https://github.com/zhuwujing28-del/codex-skills-cn/blob/main/.github/ISSUE_TEMPLATE/maintainer_feedback_request.md) provides a structured intake path. | Keep open and request one sanitized, reproducible workflow report per follow-up. |

### `agent-evals-cn`

| Issue | Current evidence | Suggested action |
| --- | --- | --- |
| #1, expand baseline eval cases to 10+ | [`eval-case-index.md`](eval-case-index.md) lists 22 cases, and `scripts/validate.py` checks case structure and index coverage. | Treat the original 10+ target as completed; close it or replace it with a narrower case request. |
| #2, manual judging limitation | [`scoring-rubric.md`](scoring-rubric.md), [`scoring-calibration.md`](scoring-calibration.md), [`human-eval-review-runbook.md`](human-eval-review-runbook.md), and the replay reports reduce reviewer drift, but results remain manually judged. | Keep open as an honest limitation until a repeatable semi-automated comparison path is published. |

## Suggested maintainer replies

### Completed scope

```text
这个需求对应的文档和验证证据已经发布，链接见本条 issue 的说明。为了避免重复维护，建议关闭当前重复请求；如果仍有缺口，请补充一个具体场景、输入材料和期望输出。
```

### Still-open roadmap or limitation

```text
这个方向仍然保留。当前仓库已经有对应的示例、验证命令和证据记录，但还需要真实或脱敏的后续反馈来缩小范围。欢迎提交一个可复现的小案例，而不是泛化的采用结论。
```

## Next maintenance focus

Do not add another baseline case or duplicate installation guide solely to
reduce the issue count. The next high-value signal is one externally submitted
or independently replayed maintainer report with a sanitized prompt/output,
reviewer score, and one concrete follow-up action.
