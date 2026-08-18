# Eval Case Index

This index gives maintainers a quick coverage map for the baseline eval cases.
It is intentionally lightweight: each entry should point to a concrete case,
state the capability under test, and name the primary failure mode it catches.

## Baseline cases

| Case ID | File | Capability | Primary failure mode |
| --- | --- | --- | --- |
| `failing-github-actions-pytest` | [`examples/ci-failure-diagnosis-case.md`](../examples/ci-failure-diagnosis-case.md) | GitHub Actions failure diagnosis | Fixing symptoms without reading the failing job evidence |
| `long-pr-review-context-trimming` | [`examples/context-budget-case.md`](../examples/context-budget-case.md) | Long-context review compression | Dropping constraints, user changes, or unresolved risks |
| `major-upgrade-with-breaking-change` | [`examples/dependency-upgrade-case.md`](../examples/dependency-upgrade-case.md) | Dependency upgrade review | Treating a breaking major upgrade as routine |
| `incomplete-bug-report` | [`examples/issue-triage-case.md`](../examples/issue-triage-case.md) | Issue triage | Inventing details instead of requesting missing repro evidence |
| `oss-maintainer-cadence-check` | [`examples/maintainer-cadence-case.md`](../examples/maintainer-cadence-case.md) | Recurring OSS maintenance cadence | Committing noisy changes without inspecting state or choosing no-op |
| `mcp-skill-boundary-maintainer-answer` | [`examples/mcp-skill-boundary-case.md`](../examples/mcp-skill-boundary-case.md) | MCP vs skill boundary decisions | Recommending the wrong extension surface |
| `latest-model-choice` | [`examples/openai-docs-case.md`](../examples/openai-docs-case.md) | Current OpenAI docs answers | Answering from stale memory instead of official docs |
| `stale-state-update` | [`examples/pr-review-case.md`](../examples/pr-review-case.md) | PR review | Missing a user-visible stale state regression |
| `skill-repo-pre-release-check` | [`examples/release-readiness-case.md`](../examples/release-readiness-case.md) | Release readiness review | Tagging without validation or scoped release notes |
| `release-notes-from-maintainer-diff` | [`examples/release-notes-evidence-case.md`](../examples/release-notes-evidence-case.md) | Release notes drafting | Turning sparse commit evidence into hype, unverifiable claims, or reader-hostile notes |
| `skill-installation-integrity-check` | [`examples/skill-installation-integrity-case.md`](../examples/skill-installation-integrity-case.md) | Skill installation readiness | Claiming installability without checking package shape and fresh-clone docs |
| `recurring-automation-memory-continuity` | [`examples/automation-memory-continuity-case.md`](../examples/automation-memory-continuity-case.md) | Recurring automation memory continuity | Repeating prior work or committing without reading automation memory |
| `vague-bug-report-minimal-repro` | [`examples/bug-reproduction-minimal-case.md`](../examples/bug-reproduction-minimal-case.md) | Minimal bug reproduction planning | Confirming a regression without repro evidence |
| `public-issue-followup-drafting` | [`examples/public-issue-followup-case.md`](../examples/public-issue-followup-case.md) | Public issue follow-up drafting | Closing completed issues or limitations without matching evidence |
| `repo-onboarding-first-pass-map` | [`examples/repo-onboarding-first-pass-case.md`](../examples/repo-onboarding-first-pass-case.md) | Repository onboarding and first-pass maintainer mapping | Inventing setup, architecture, or readiness claims without inspecting repo evidence |
| `private-vulnerability-report` | [`examples/security-advisory-triage-case.md`](../examples/security-advisory-triage-case.md) | Security advisory triage | Exposing private vulnerability details |
| `skill-contribution-review` | [`examples/skill-contribution-review-case.md`](../examples/skill-contribution-review-case.md) | Skill contribution review | Approving plausible skills without checking risk and evidence |
| `validation-evidence-reporting` | [`examples/validation-evidence-reporting-case.md`](../examples/validation-evidence-reporting-case.md) | Validation evidence reporting | Claiming checks passed without preserving command/output evidence |
| `lawful-scraping-boundary` | [`examples/web-extraction-boundary-case.md`](../examples/web-extraction-boundary-case.md) | Web extraction boundary setting | Encouraging access-control bypass or ToS-unsafe scraping |

## Maintenance rule

When adding a new `examples/*-case.md` file, update this index in the same
change. `python scripts/validate.py` checks that every baseline case is listed
here so coverage cannot drift silently.