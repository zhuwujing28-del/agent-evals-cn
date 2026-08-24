# Eval Coverage Map

This map groups the baseline eval cases by maintainer workflow so contributors
can see what the repository already exercises and where replay evidence is still
thin.

## Coverage snapshot

| Workflow area | Representative cases | Notes |
| --- | --- | --- |
| Triage and debugging | `failing-github-actions-pytest`, `vague-bug-report-minimal-repro`, `incomplete-bug-report`, `public-issue-followup-drafting` | Covers diagnosis, repro requests, and issue follow-up without inventing missing evidence. |
| Review and change control | `stale-state-update`, `major-upgrade-with-breaking-change`, `skill-repo-pre-release-check`, `release-notes-from-maintainer-diff`, `skill-contribution-review` | Checks whether the agent respects review evidence, breaking changes, and release discipline. |
| OSS operations | `oss-maintainer-cadence-check`, `maintainer-usage-report-intake`, `repo-onboarding-first-pass-map`, `oss-application-evidence-draft`, `workflow-permissions-hardening` | Focuses on recurring maintainer work, public reporting, and application readiness. |
| Agent boundaries and tooling | `mcp-skill-boundary-maintainer-answer`, `latest-model-choice`, `lawful-scraping-boundary`, `recurring-automation-memory-continuity`, `long-pr-review-context-trimming` | Exercises scope control, freshness, lawful extraction, memory continuity, and context management. |
| Validation and installability | `validation-evidence-reporting`, `skill-installation-integrity-check`, `release-notes-from-maintainer-diff` | Makes sure claims about checks, installs, and release evidence stay grounded. |

## What is still thin

- Replayed cases from live regressions are still the strongest missing piece.
- Public issue and release evidence exists, but more first-hand maintainer traces would make the baseline harder to game.
- The current set is broad enough for OSS application materials, but it still benefits from new cases whenever a real failure mode repeats.

## Related index

- [`docs/eval-case-index.md`](eval-case-index.md)
- [`docs/oss-readiness.md`](oss-readiness.md)
