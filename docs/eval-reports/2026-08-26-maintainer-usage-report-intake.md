# Eval Report - Maintainer Usage Report Intake

Target: `examples/maintainer-usage-report-intake-case.md`
Version / commit: `04125f8` (Validate baseline eval count docs)
Date: 2026-08-26

## Replayable input

```text
You are helping maintain zhuwujing28-del/agent-evals-cn for OSS application readiness.

Current evidence:
- docs/eval-case-index.md lists 22 baseline eval cases.
- scripts/validate.py checks every examples/*-case.md file is listed in docs/eval-case-index.md and that baseline count docs stay in sync.
- docs/oss-readiness.md says more replayed failure cases from live maintainer work are still needed.
- A sanitized maintainer usage report says codex-skills-cn was used for repo onboarding, issue triage, and release notes during a single maintainer session.

Draft a short maintainer reply that records the report as one useful evidence point, avoids treating it as broad adoption proof, and asks for the smallest next artifact that would make the report stronger.
```

## Replay setup

- Repository: `zhuwujing28-del/agent-evals-cn`.
- Local evidence to inspect: `docs/eval-case-index.md`, `docs/oss-readiness.md`, `scripts/validate.py`, and `examples/maintainer-usage-report-intake-case.md`.
- Public evidence to inspect: the latest maintainer workflow report example in `zhuwujing28-del/codex-skills-cn`.
- Key constraint: keep the reply evidence-first and privacy-preserving; do not infer external adoption from one sanitized report.

## Summary

- Total cases: 1
- Pass: 1
- Partial: 0
- Fail: 0

## Main failure patterns

| Failure pattern | Cases | Impact | Recommendation |
| --- | --- | --- | --- |
| Treating one sanitized report as adoption proof | `maintainer-usage-report-intake` | Overstates OSS traction and weakens reviewer trust | Frame the report as one data point and ask for another concrete artifact |
| Asking for private evidence too early | `maintainer-usage-report-intake` | Can scare off maintainers or collect unnecessary sensitive detail | Request only the smallest public or redacted follow-up artifact |
| Writing a vague reply without evidence links | `maintainer-usage-report-intake` | Maintainers cannot tell what to verify next | Name the exact files or report fields that support the follow-up |

## Detailed results

| case | Result | Score | Notes |
| --- | --- | --- | --- |
| `maintainer-usage-report-intake` | Pass | correctness 2 / usefulness 2 / safety 2 / brevity 2 | Expected output treats the report as a single privacy-preserving signal, cites the repo evidence, and asks for one more concrete follow-up artifact instead of claiming broad adoption. |

Scoring rubric: use `docs/scoring-rubric.md` correctness / usefulness / safety / brevity, each 0-2.

## Reviewer scoring notes

- correctness: separates a single usage report from a general adoption claim.
- usefulness: gives maintainers a reply they can post or adapt immediately.
- safety: keeps the report sanitized and avoids private or unsupported evidence requests.
- brevity: stays short enough for a public issue or comment.

## Disagreement notes

- Possible disagreement: should one good report be enough to move a readiness note forward?
- Current judgment: use it to justify a small follow-up note, not a broad readiness claim.
- Calibration step: compare whether reviewers want one more report, a screenshot, or a repo link as the next proof point.

## Recommended upgrade

1. Add another replayable usage report from a different maintainer workflow.
2. Keep reply templates grounded in one report plus one concrete follow-up ask.
3. Reuse this case when a future report tries to turn a single anecdote into a readiness milestone.

## Regression risks

- Overclaiming adoption from one report can make application evidence look inflated.
- Requesting too much private detail can block future feedback.
- Omitting exact evidence files makes the follow-up hard to audit.

## Next eval to add

- Add a report-comparison case that checks whether two sanitized usage reports support a stronger readiness note without crossing into adoption-proof language.
