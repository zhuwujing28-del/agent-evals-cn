# Public Issue Triage - 2026-07-20

This note reconciles the currently open public GitHub issues with the eval
coverage, scoring docs, and validation checks that already exist on `main`. It
is intended as maintainer evidence for closing stale roadmap items, keeping real
limitations visible, and avoiding noisy follow-up commits that do not improve
open-source readiness.

## Snapshot

- Repository: `zhuwujing28-del/agent-evals-cn`
- Public check time: 2026-07-20
- Local state checked before this note: clean `main`, aligned with `origin/main`
- Public open issues checked through the GitHub API: 2
- Latest public commits checked:
  - `8cf888a` - baseline count alignment
  - `dfffbff` - scoring calibration notes
  - `5848df4` - validation evidence reporting eval

## Recommended issue actions

| Issue | Topic | Evidence on `main` | Suggested action |
| --- | --- | --- | --- |
| #1 | Expand baseline eval cases to 10+ | [`eval-case-index.md`](eval-case-index.md) lists 13 baseline cases and `scripts/validate.py` checks that every case is indexed. | Close as completed after posting the index link and current case count. |
| #2 | Evals are still manually judged | [`scoring-rubric.md`](scoring-rubric.md), [`scoring-calibration.md`](scoring-calibration.md), and [`human-eval-review-runbook.md`](human-eval-review-runbook.md) reduce reviewer drift, but manual judgment remains an honest limitation. | Keep open as a known limitation until at least one repeatable report corpus or automation path exists. |

## Suggested maintainer replies

### Baseline expansion issue (#1)

```text
已完成第一阶段 baseline 扩展：当前 main 有 13 个 baseline eval case，并通过 docs/eval-case-index.md 维护覆盖范围。scripts/validate.py 也会检查每个 case 是否被索引，避免后续遗漏。这个 issue 可以按已完成关闭；新的 case 请求可以继续用 eval_case 模板单独提交。
```

### Manual judging limitation issue (#2)

```text
这个限制仍然存在，但 main 已经补充了 docs/scoring-rubric.md、docs/scoring-calibration.md 和 docs/human-eval-review-runbook.md，用来降低人工评分漂移。建议保留该 issue，后续用真实报告样本或可重复的半自动检查来逐步收敛，而不是现在宣称已经自动化解决。
```

## Next maintenance focus

Do not add more baseline cases only to increase the count. The next useful step
is to collect one replayable eval report that includes raw prompt, sanitized
model output, reviewer scores, and disagreement notes. If the report exposes a
repeated failure mode, add one targeted eval case or validation check from that
evidence.

