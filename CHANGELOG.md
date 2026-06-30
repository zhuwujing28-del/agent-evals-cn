# Changelog

All notable changes to `agent-evals-cn` are documented here.

This project follows a lightweight 0.x release process while the eval method, templates, and baseline cases are still stabilizing.

## Unreleased

### Added

- Core `agent-evals-cn` Codex skill for Chinese agent, prompt, and workflow evaluation.
- Baseline examples for PR review, issue triage, and OpenAI docs answer evaluation.
- Reusable eval case and eval report templates.
- Repository validation script and GitHub Actions workflow for structure checks.
- Issue templates for eval case proposals and skill upgrade requests.
- OSS readiness tracker for application and maintenance planning.
- Usage report applying `agent-evals-cn` to `codex-skills-cn` maintainer skills.
- Baseline eval case for GitHub Actions CI failure diagnosis.

### Changed

- Established a maintenance flow that requires real failure cases, baseline reruns, and documented limitations before upgrades.

### Pending Before v0.1.0

- Add more baseline eval cases across at least three maintainer workflows.
- Add a README CI badge after confirming the public workflow status.
- Tag `v0.1.0` only after the baseline set is stable enough to rerun.
