# Human Eval Review Runbook

This runbook keeps manually judged eval reports consistent enough to be useful across releases. It does not replace reviewer judgment; it makes the judgment easier to audit.

Use it when:

- adding a new baseline eval case,
- rerunning the baseline before a release tag,
- comparing two versions of a skill or prompt,
- or turning a failed real run into a regression case.

## Inputs

Prepare these files or links before scoring:

- the eval case file from `examples/`,
- the tested skill, prompt, or workflow version,
- the model and tool environment used for the run,
- the raw agent output,
- any redacted logs needed to understand the failure,
- and the scoring rubric in [`scoring-rubric.md`](scoring-rubric.md).

Do not include private repository contents, secrets, customer data, access tokens, private issue links, or non-public logs in the public report.

## Review Steps

1. Confirm the case is valid.

   Check that the case has a stable `case-id`, concrete target capability, realistic Chinese input, expected behavior, failure criteria, and safety notes where needed.

2. Capture the run context.

   Record the tested version, commit SHA if available, date, model/tool surface, and any constraints that affected the run. If a tool was unavailable, say so instead of normalizing the output.

3. Score against the rubric.

   Use [`scoring-rubric.md`](scoring-rubric.md) as the main source of truth. Prefer short evidence bullets over broad impressions. Quote only the minimum text needed to support the score.
   For release or public application evidence, use [`scoring-calibration.md`](scoring-calibration.md) to compare scores against shared anchors before publishing.

4. Classify the result.

   Use one of:

   - `pass`: meets the expected behavior and avoids listed failure criteria.
   - `partial`: useful but misses one non-blocking requirement or needs reviewer cleanup.
   - `fail`: misses a core requirement, violates safety boundaries, fabricates evidence, or cannot be reproduced.

5. Decide the follow-up.

   Every `partial` or `fail` report should end with one concrete next action: update the skill, revise the eval case, add a regression case, improve documentation, or record a known limitation.

## Two-Reviewer Spot Check

Use a second reviewer when:

- the result gates a release tag,
- the case touches security, privacy, accounts, or scraped web data,
- the score changed from `pass` to `fail`,
- or the run is being used as public application evidence.

The second reviewer should focus on whether the evidence supports the classification, not on rewriting the report style.

## Report Checklist

Before publishing or committing a report, confirm:

- [ ] The input and output are redacted.
- [ ] The tested version is identified.
- [ ] The case ID is included.
- [ ] The result is `pass`, `partial`, or `fail`.
- [ ] Each score has evidence.
- [ ] Safety issues are called out explicitly.
- [ ] Follow-up work is concrete and scoped.
- [ ] Public links point only to public resources.

## Release Use

Before tagging a release, rerun only the baseline cases that cover changed behavior unless the release changes the core eval method. Record skipped cases and why they were not affected.

For `v0.1.1`, use this runbook with [`v0.1.1-release-checklist.md`](v0.1.1-release-checklist.md) to verify the hardened baseline without rewriting the existing `v0.1.0` tag.
