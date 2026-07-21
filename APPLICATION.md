# Codex for Open Source Application Notes

`agent-evals-cn` is a companion project for evaluating and improving Chinese Codex skills, prompts, and agent workflows.

## One-line summary

`agent-evals-cn` helps Chinese-speaking open-source maintainers evaluate Codex skills and agent workflows with reusable eval cases, failure analysis, regression checks, and versioned upgrade plans.

## Why this project matters

As more maintainers use Codex for PR review, issue triage, CI diagnosis, dependency upgrades, release notes, and documentation, the hard problem becomes quality control:

- Did the skill actually improve?
- Did a prompt update introduce regressions?
- Are Chinese maintainer workflows covered?
- Are failure cases preserved as reusable tests?

This project provides a lightweight eval method for those questions.

## Current status

- Core `agent-evals-cn` skill.
- 14 baseline eval cases across maintainer workflows.
- Eval case and report templates.
- GitHub Actions validation.
- Changelog, OSS readiness tracker, and usage report.
- Usage report evaluating `codex-skills-cn` maintainer skills.

## Relationship to codex-skills-cn

`codex-skills-cn` provides reusable Chinese Codex skills for open-source maintainers.

`agent-evals-cn` provides the evaluation loop that helps keep those skills reliable:

- design eval cases,
- record failure modes,
- run baseline checks,
- document upgrade plans,
- and avoid regressions.

Together they form a small but focused ecosystem for Chinese-speaking maintainers using Codex.

## How Codex helps this project

Codex is used to:

- turn real maintainer scenarios into eval cases,
- maintain examples and templates,
- update changelog and readiness notes,
- review skill quality,
- and generate practical improvement plans.

## Honest scope

This is an early-stage evaluation project. It does not claim broad adoption yet. Its value is in creating a repeatable quality-control layer for Chinese Codex skills and OSS maintainer workflows.
