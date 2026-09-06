# OSS Application Evidence Snapshot — 2026-09-06

这份快照记录 `agent-evals-cn` 及其配套仓库在 2026 年 9 月 6 日检查到的公开证据。它只描述可复核的仓库状态，不把一次本地运行、一次 replay 或 GitHub 计数包装成广泛采用或生产可靠性。

## Public repository state

| Repository | Public head | Latest push observed | Stars | Forks | Open issues |
| --- | --- | --- | ---: | ---: | ---: |
| `zhuwujing28-del/agent-evals-cn` | `d93b892` — Add independent replay protocol | 2026-09-05 14:48 UTC | 1 | 0 | 2 |
| `zhuwujing28-del/codex-skills-cn` | `132f68c` — Refresh application evidence snapshot | 2026-09-05 23:22 UTC | 1 | 0 | 7 |

Observed through the GitHub repository API on 2026-09-06. Open issues are
backlog signals only; they are not evidence of active adoption.

## Validation evidence

- Local `python .\scripts\validate.py` passes for `agent-evals-cn`.
- Local `python .\scripts\validate-skills.py` reports 12 skills for
  `codex-skills-cn`.
- GitHub Actions validation passed for `agent-evals-cn` run `#68` on
  `d93b892`.
- GitHub Actions validation passed for `codex-skills-cn` run `#55` on
  `132f68c`.
- The repositories were clean and aligned with `origin/main` when this
  snapshot was prepared.

## Evidence currently supported

- The companion projects are public, small, actively maintained repositories
  with repeatable structure checks.
- `agent-evals-cn` contains 22 baseline cases, replayable reports, a scoring
  rubric, a structured JSON result template, and an independent replay
  protocol.
- The two repositories form a documented loop: `codex-skills-cn` supplies
  maintainer-facing skills and `agent-evals-cn` supplies regression and replay
  methods.

## Claims to avoid

- Do not claim broad external adoption, active outside contributors, or
  production reliability from these counts.
- Do not treat the three published replay reports as independent external
  validation; the current tracker still records that no different maintainer
  or environment has submitted an accepted independent replay.
- Do not infer user numbers, impact, or quality from stars, forks, issue counts,
  or successful CI runs.

## Next evidence step

The highest-value next step remains accepting the first independently replayed
report from a different maintainer or environment, with the input, evaluated
commit, environment, scores, and evidence required by
[`independent-replay-protocol.md`](independent-replay-protocol.md).
