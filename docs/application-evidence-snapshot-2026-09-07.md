# OSS Application Evidence Snapshot — 2026-09-07

这份快照记录两个公开仓库在 2026 年 9 月 7 日检查到的可复核证据。它
区分公开提交、本地校验和历史计数，不把这些信号包装成广泛采用或生产
可靠性。

## Public repository state

| Repository | Evidence commit observed before this refresh | Latest push observed | Stars / forks / open issues |
| --- | --- | --- | ---: |
| `zhuwujing28-del/agent-evals-cn` | `6d137a2` — Refresh application evidence snapshot | 2026-09-07, confirmed with GitHub REST metadata and public refs | 1 / 0 / 2 |
| `zhuwujing28-del/codex-skills-cn` | `11d7957` — Refresh application evidence snapshot | 2026-09-07, confirmed with GitHub REST metadata and public refs | 1 / 0 / 7 |

Repository counts are the latest successful public metadata observation from
2026-09-07. The commits above are the validated evidence commits observed
before this documentation refresh, not a self-referential claim that this file's
own commit is already independently validated.

## Validation evidence

- Local `scripts\validate.py` passes for `agent-evals-cn`.
- Local `scripts\validate-skills.py` reports 12 skills for `codex-skills-cn`.
- Both worktrees are clean and aligned with their public `origin/main` heads.
- The newly published `6d137a2` refreshes the current application snapshot and
  retains the previously documented independent-replay protocol.

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
- Do not treat the published replay reports as independent external validation;
  the tracker still records that no different maintainer or environment has
  submitted an accepted independent replay.

## Next evidence step

Accept the first independently replayed report from a different maintainer or
environment, including the evaluated commit, environment, scores, and evidence
required by [`independent-replay-protocol.md`](independent-replay-protocol.md).
