# Changelog

All notable changes to `agent-evals-cn` are documented here.

This project follows a lightweight 0.x release process while the eval method, templates, and baseline cases are still stabilizing.

## Unreleased

### Added

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
