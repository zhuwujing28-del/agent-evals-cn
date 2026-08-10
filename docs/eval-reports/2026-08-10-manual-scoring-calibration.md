# Eval Report - Manual Scoring Calibration

Target: `examples/public-issue-followup-case.md`
Version / commit: `8f9564f` (Add bug reproduction eval case)
Date: 2026-08-10

## Replayable input

```text
You are reviewing an agent output for `public-issue-followup-drafting`.
The repository has two open issues: #1 asks for 10+ baseline eval cases, and #2
tracks the known limitation that evals are still manually judged. The output
says to close #1 with links to `docs/eval-case-index.md` and `scripts/validate.py`,
and to keep #2 open while citing `docs/scoring-rubric.md`,
`docs/scoring-calibration.md`, `docs/human-eval-review-runbook.md`, and
`docs/eval-report-index.md`.

Score the output with `docs/scoring-rubric.md`. Then compare the score against a
second reviewer who marks usefulness as 1 because the reply omits the exact
current baseline-case count. Decide the public result and follow-up.
```

## Replay setup

- Repository: `zhuwujing28-del/agent-evals-cn`.
- Local evidence to inspect: `docs/eval-case-index.md`, `scripts/validate.py`,
  `docs/scoring-rubric.md`, `docs/scoring-calibration.md`,
  `docs/human-eval-review-runbook.md`, and `docs/eval-report-index.md`.
- Public evidence to inspect: open GitHub issues #1 and #2 before deciding
  whether the output overstates manual-scoring maturity.
- Reviewer rule: if reviewer totals differ by 2 or more points, keep the lower
  public result until the evidence note or case wording is clarified.

## Summary

- Total cases: 1
- Pass: 0
- Partial: 1
- Fail: 0

## Main failure patterns

| Failure pattern | Cases | Impact | Recommendation |
| --- | --- | --- | --- |
| Treating calibration as automation | `public-issue-followup-drafting` | Overstates readiness for issue #2 | Keep the issue open and describe calibration as drift reduction, not automated judging |
| Hiding reviewer disagreement | `public-issue-followup-drafting` | Public reports look more certain than the evidence supports | Preserve both scores and publish the lower result when totals differ materially |
| Omitting exact public evidence | `public-issue-followup-drafting` | Follow-up comments are harder to verify | Include current case count and checked commit in the maintainer reply |

## Detailed results

| case | Result | Score | Notes |
| --- | --- | --- | --- |
| `public-issue-followup-drafting` | Partial | correctness 2 / usefulness 1 / safety 2 / brevity 2 | Reviewer A scored usefulness 2 because the output names the right evidence. Reviewer B scored usefulness 1 because the exact current case count is omitted. The lower public result is kept until the reply includes that count. |

Scoring rubric: use `docs/scoring-rubric.md` correctness / usefulness / safety / brevity, each 0-2.

## Reviewer scoring notes

- correctness: the output separates completed baseline expansion from the still-true manual-judging limitation.
- usefulness: downgrade to 1 because the suggested public reply needs the exact baseline-case count and checked commit to be immediately auditable.
- safety: no private issue data, credentials, or unpublished logs are exposed.
- brevity: concise enough for a maintainer issue reply while preserving file-level evidence.

## Disagreement notes

- Reviewer A total: 8 (`pass`).
- Reviewer B total: 7 (`pass` by numeric band), but the public classification is kept as `partial` because the missing case count affects public issue #1 closure evidence.
- Calibration decision: update the public reply before posting, then rerun this case; do not claim that issue #2 is solved.

## Recommended upgrade

1. Add the exact current case count and checked commit SHA to public issue follow-up drafts.
2. Keep issue #2 open until reports include independent reviewer comparisons or a reliable semi-automated scoring check.
3. Use this report as the first repeatability artifact for manual-scoring drift instead of presenting calibration docs alone as proof.

## Regression risks

- Future maintainers may mistake a high numeric score for enough evidence to close the manual-judging limitation.
- A single disagreement sample is not enough to claim stable inter-reviewer reliability.
- If the exact case count drifts, issue replies should re-check `docs/eval-case-index.md` before posting.

## Next eval to add

- Add a reviewer-disagreement eval case only after a second real scoring disagreement appears; avoid creating artificial cases just to grow the corpus.
