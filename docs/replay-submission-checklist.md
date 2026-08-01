# Replay Submission Checklist

Use this checklist before opening an `eval-report` review issue. It keeps
external evidence small, replayable, and easy for a maintainer to verify.

## Before running

- Choose an existing `case-id` from [`docs/eval-case-index.md`](eval-case-index.md).
- Record the skill or workflow version, commit SHA, model/tool environment, and date.
- Remove tokens, cookies, API keys, private repository content, and unsanitized logs.
- Keep the input and context to the smallest excerpt that still reproduces the behavior.

## During the run

- Capture the exact input and relevant setup, including unavailable tools or special flags.
- Preserve the output excerpt needed to judge correctness, usefulness, safety, and brevity.
- Score each rubric dimension with one concrete evidence sentence.
- Mark `pass`, `partial`, or `fail`; record disagreement points instead of hiding uncertainty.

## Before opening the issue

- Compare the result with [`docs/scoring-rubric.md`](scoring-rubric.md) and [`docs/scoring-calibration.md`](scoring-calibration.md).
- Choose one smallest follow-up: update the skill, update the case, add a replayable report, improve docs, or record a limitation.
- Paste the sanitized material into the [eval report review template](../.github/ISSUE_TEMPLATE/eval_report_review.md).
