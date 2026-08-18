# Changelog

All notable changes to `agent-evals-cn` are documented here.

This project follows a lightweight 0.x release process while the eval method, templates, and baseline cases are still stabilizing.

## Unreleased

### Added

- Added a release-notes evidence eval case that checks commit-grounded Chinese release notes, validation status, and claim boundaries.

- Added a repository onboarding eval case that checks first-pass repo maps, validation commands, and application-readiness risks against inspected evidence.
- Added a manual-scoring calibration eval report that records reviewer disagreement and keeps the manual-judging limitation auditable.
- Added a minimal bug reproduction eval case that pairs with `codex-skills-cn` `bug-reproduction-cn` and checks evidence-based repro planning before confirming regressions.
- Added an automation memory continuity eval case for recurring OSS maintenance runs that must read prior memory, inspect public state, and avoid duplicate commits.
- Added a dated cross-repo OSS readiness usage report that records public GitHub state, open issue follow-ups, and next application-focused actions.
- Added a repository `CODEOWNERS` entry so public eval, documentation, and validation changes have an explicit maintainer review owner.
- Added a replay submission checklist that makes external eval evidence easier to sanitize, reproduce, and review.
- Added a skill contribution review eval case for maintainer PR decisions that must check risk, docs, and validation evidence before merge.
- Added validation for the eval report review issue template so external replay submissions keep case IDs, version evidence, rubric links, scoring dimensions, and pass/partial/fail decisions.
- Added an eval report review issue template for external replayable manual-scoring evidence.
- Added a replayable eval report corpus starter for the recurring OSS maintainer cadence case.
- Added an eval report index and validation for replayable report sections so public evidence stays rerunnable and auditable.
- Added a public issue follow-up eval case for evidence-based close/keep-open maintainer replies.
- Added a public issue triage note mapping the open baseline-expansion and manual-judging issues to current evidence and next actions.
- Corrected application and readiness notes to reflect the current 13-case baseline eval set.
- Added scoring calibration notes for manual eval reports that gate releases or public application evidence.
- Added a validation evidence reporting eval case for final updates that must separate local checks, CI evidence, and push/credential status.
- Added a skill installation integrity eval case for fresh-clone readiness review.
- Added a maintainer cadence eval case for recurring OSS-readiness automations that must inspect state first, choose no-op when appropriate, and avoid noisy commits.
- Added validation for the eval report template so published reports keep required release-evidence fields and rubric references.

## v0.1.1 - 2026-07-15

### Added

- Added a human eval review runbook for repeatable manual scoring, release spot checks, and follow-up decisions.
- Added a baseline eval case index that maps each case to its tested capability and primary failure mode.
- Added a `v0.1.1` patch-release checklist for packaging post-`v0.1.0` eval hardening without moving the published tag.
- Added a post-`v0.1.0` audit documenting the published tag target and follow-up patch-release path.
- Added local Markdown link validation for repository documentation.
- Added context budget and MCP vs Codex skill boundary eval cases.
- Added security policy for redaction, unsafe eval boundaries, and maintainer response.
- Added a lightweight scoring rubric for consistent human-reviewed eval reports.
- Added README validation badge and a `v0.1.0` release checklist for tag readiness review.

### Changed

- Strengthened validation so every baseline eval case needs a unique `case-id` and core review sections.
- Strengthened validation so every baseline eval case must be listed in the eval case index.
- Added release-readiness docs for the hardened post-tag baseline.

## v0.1.0 - 2026-07-08

The first public tag captured the early application-materials baseline. Later eval, validation, CI, security, and release-readiness hardening was packaged in the `v0.1.1` patch tag.

### Added

- Added `APPLICATION.md` for Codex for Open Source application preparation.
- Core `agent-evals-cn` Codex skill for Chinese agent, prompt, and workflow evaluation.
- Baseline examples for PR review, issue triage, and OpenAI docs answer evaluation.
- Reusable eval case and eval report templates.
- Repository validation script and GitHub Actions workflow for structure checks.
- Issue templates for eval case proposals and skill upgrade requests.
- OSS readiness tracker for application and maintenance planning.
- Usage report applying `agent-evals-cn` to `codex-skills-cn` maintainer skills.
- Baseline eval case for GitHub Actions CI failure diagnosis.
- Baseline eval case for Codex skill repository release readiness.
- Baseline eval case for dependency upgrade review.
- Baseline eval case for security advisory triage.

### Changed

- Established a maintenance flow that requires real failure cases, baseline reruns, and documented limitations before upgrades.

### Release status

- Published as the historical `v0.1.0` tag. Do not move or rewrite this tag.
