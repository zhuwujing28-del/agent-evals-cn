# Changelog

All notable changes to `agent-evals-cn` are documented here.

This project follows a lightweight 0.x release process while the eval method, templates, and baseline cases are still stabilizing.

## Unreleased

_No unreleased changes._

## v0.1.0 - 2026-07-08

The first tagged release includes the baseline Chinese eval set, reusable templates, validation, and release-readiness documentation.

### Added

- Added `APPLICATION.md` for Codex for Open Source application preparation.
- Added context budget eval case for long PR review context trimming.
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
- Baseline eval case for MCP vs Codex skill boundary decisions.
- Security policy for redaction, unsafe eval boundaries, and maintainer response.
- Lightweight scoring rubric for consistent human-reviewed eval reports.
- README validation badge for visible CI status.
- `v0.1.0` release checklist for tag readiness review.

### Changed

- Established a maintenance flow that requires real failure cases, baseline reruns, and documented limitations before upgrades.
- Strengthened validation so every baseline eval case needs a unique `case-id` and core review sections.

### Release status

- Ready for an annotated `v0.1.0` tag once the public `main` workflow is confirmed green.
