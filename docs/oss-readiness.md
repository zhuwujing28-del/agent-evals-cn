# OSS Readiness Tracker

This tracker keeps `agent-evals-cn` honest as an open-source project. The goal is not to inflate activity, but to collect durable signals that the project is useful and maintainable.

## Current strengths

- Clear niche: Chinese AI agent, Codex skill, and prompt workflow evals.
- A reusable core skill with safety boundaries and validation guidance.
- Baseline examples for PR review, issue triage, OpenAI docs answers, and web extraction boundaries.
- GitHub Actions validation for repository structure.
- Issue templates for eval cases and skill upgrades.

## Current gaps

- More real-world eval cases are needed, especially cases replayed from failed runs.
- No external issues or PRs yet.
- No tagged release yet.
- No CI badge in README yet.

## Near-term checklist

- [ ] Add 10 baseline eval cases. Current: 4.
- [x] Add `CHANGELOG.md`.
- [ ] Add a README CI badge after the first workflow run is visible.
- [x] Add one usage report from applying the skill to `codex-skills-cn`.
- [ ] Tag `v0.1.0` after the baseline set is stable.

## Quality bar for new eval cases

Every new eval case should include:

- A concrete target capability.
- A realistic Chinese user request or maintainer scenario.
- Expected behavior.
- Failure criteria.
- Safety notes if the case touches logs, accounts, private repos, or API docs.

## Application narrative

`agent-evals-cn` helps Chinese-speaking open-source maintainers improve Codex skills and agent workflows through reusable eval cases, regression checks, and versioned upgrade plans. It is designed to make agent quality less subjective and more maintainable.
