# Eval Report Index

This index tracks replayable eval reports that maintainers can rerun when
checking release readiness, reviewer consistency, or OSS application evidence.

## Replayable reports

| Date | Report | Primary case | What it proves |
| --- | --- | --- | --- |
| 2026-07-22 | [`docs/eval-reports/2026-07-22-oss-maintainer-cadence.md`](eval-reports/2026-07-22-oss-maintainer-cadence.md) | `oss-maintainer-cadence-check` | The recurring OSS-maintainer automation inspects local/public state first, prefers no-op over filler, and records validation/push evidence separately. |

## Maintenance rule

When adding a new file under `docs/eval-reports/`, update this index in the
same change. `python scripts/validate.py` checks that every replayable report is
listed here and includes the core replay/evidence sections.
