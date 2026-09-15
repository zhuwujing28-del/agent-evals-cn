# OSS Application Evidence Snapshot — 2026-09-15

This dated snapshot records the public evidence observed for both companion
repositories on September 15, 2026. It separates repository-maintainer
validation from claims about external adoption.

## Public repository state

| Repository | Evidence commit observed before this refresh | Latest push observed | Latest validate run | Stars / forks / open issues |
| --- | --- | --- | --- | ---: |
| `zhuwujing28-del/agent-evals-cn` | `a3a5a30` — Clarify application evidence snapshot freshness | 2026-09-12, confirmed with GitHub REST metadata and public refs | success, run `#72`, `a3a5a30` | 1 / 0 / 2 |
| `zhuwujing28-del/codex-skills-cn` | `6998bea` — Clarify application evidence snapshot freshness | 2026-09-12, confirmed with GitHub REST metadata and public refs | success, run `#59`, `6998bea` | 1 / 0 / 7 |

The commits above are the validated evidence commits observed before this
documentation refresh, not a self-referential claim that this file's own
commit is already independently validated.

## Validation evidence

- Local `scripts\validate.py` passes for `agent-evals-cn`.
- Local `scripts\validate-skills.py` reports 12 skills for
  `codex-skills-cn`.
- `scripts\validate-cross-repo.ps1` runs both validators when the repositories
  are checked out together.
- Public validation was successful on both evidence commits listed above.

## Evidence currently supported

- Both companion projects are public, small repositories with repeatable
  structure validation.
- `agent-evals-cn` contains 22 baseline cases, replayable reports, a scoring
  rubric, a structured JSON result template, and an independent replay
  protocol.
- `codex-skills-cn` supplies maintainer-facing skills while this repository
  supplies regression and replay methods.

## Claims to avoid

- Do not claim broad external adoption, active outside contributors, or
  production reliability from stars, forks, issue counts, or local validation.
- Do not treat published replay reports as independent external validation;
  the tracker still records that no different maintainer or environment has
  submitted an accepted independent replay.

## Next evidence step

Accept the first independently replayed report from a different maintainer or
environment, including the evaluated commit, environment, scores, and evidence
required by [`independent-replay-protocol.md`](independent-replay-protocol.md).
