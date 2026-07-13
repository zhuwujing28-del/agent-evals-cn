# Post-v0.1.0 Audit - 2026-07-13

This note records the state of the public `v0.1.0` tag after later eval-readiness work landed on `main`.

## Tag status

- Published tag: `v0.1.0`
- Tag target: `0d93cde` (`Prepare agent evals application materials`)
- Current `main` during audit: `182b3b1` (`Prepare v0.1.0 changelog`)
- Latest public validation run checked: `validate` on `182b3b1`, successful on 2026-07-08

## Changes after the tag

The current `main` branch includes useful readiness work that is not part of the published `v0.1.0` tag:

- eval PR template,
- security redaction and unsafe-eval boundary policy,
- context budget eval case,
- MCP vs Codex skill boundary eval case,
- scoring rubric,
- CI readiness badge,
- release checklist,
- baseline eval case ID and required-section validation,
- prepared `v0.1.0` changelog.

## Maintainer decision

Do not move or force-update the existing public `v0.1.0` tag. Treat it as the first application-materials baseline.

Use the current `main` branch as the candidate for a follow-up patch tag, likely `v0.1.1`, after one final validation run and changelog update.

## Recommended next release steps

1. Run `python scripts/validate.py`.
2. Confirm the public `validate` workflow remains green on current `main`.
3. Add a `v0.1.1` changelog entry summarizing post-`v0.1.0` eval hardening.
4. Create an annotated `v0.1.1` tag from current `main`.
