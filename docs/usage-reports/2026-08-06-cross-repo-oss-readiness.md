# Usage Report: Cross-repo OSS readiness snapshot

Date: 2026-08-06

Target repositories:

- `zhuwujing28-del/agent-evals-cn`
- `zhuwujing28-del/codex-skills-cn`

Evaluator: `agent-evals-cn`

## Goal

Record a compact, replayable readiness snapshot for the two related public repositories before the next Codex for Open Source application pass. The snapshot focuses on maintainer evidence, not repository activity volume.

## Public state checked

| Repository | Public `main` head | Last public push | Open issues | Stars | Forks |
| --- | --- | --- | ---: | ---: | ---: |
| `agent-evals-cn` | `54ad3be` | 2026-08-03 16:56 UTC | 2 | 1 | 0 |
| `codex-skills-cn` | `cecd563` | 2026-08-01 21:47 UTC | 7 | 1 | 0 |

Open issues reviewed:

- `agent-evals-cn#1`: expand the baseline eval set.
- `agent-evals-cn#2`: manual judging limitation.
- `codex-skills-cn#6`: v0.2 maintainer workflow examples.
- `codex-skills-cn#7`: Chinese-speaking OSS maintainer feedback request.

## Local state checked

Both local working trees were clean before this report was added. Both local `main` branches matched `origin/main` at the public heads listed above.

## Readiness findings

### What is already strong

1. The repositories now tell a coherent story:
   - `codex-skills-cn` provides Chinese maintainer workflow skills and examples.
   - `agent-evals-cn` provides eval cases, scoring guidance, replay submission checks, and report review templates.
2. The public application evidence is concrete enough to cite:
   - validation workflows are present in both repositories;
   - changelogs describe shipped maintainer-facing improvements;
   - issue templates support structured external feedback;
   - examples cover PR review, CI diagnosis, dependency upgrades, release notes, and public issue handling.
3. Recent commits are scoped and maintainer-oriented instead of noisy bulk generation.

### Gaps to keep visible

1. External usage is still early: open issues and reports mostly document planned or self-run maintainer workflows.
2. Manual eval judging remains a known limitation, even with scoring calibration and review templates.
3. `codex-skills-cn` still has duplicate historical installation/example issues that could be closed or consolidated once maintainers are ready to manage public issue state.

## Recommended next OSS-readiness action

Prefer one of these next actions over adding more skills immediately:

1. Add a small `v0.2` release readiness note after one more real or replayed maintainer workflow report.
2. Close or reply to duplicate historical `codex-skills-cn` issues with links to the shipped docs and examples.
3. Run one fresh manual eval report against a recently added `codex-skills-cn` example, then record the result under `docs/eval-reports/`.

## Application relevance

This snapshot gives the application packet a dated, evidence-based status checkpoint. It shows active maintenance across both repositories, identifies honest adoption limits, and names the next concrete work without inflating the project scope.
