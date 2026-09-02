# Structured Replay Results

`examples/eval-result-template.json` is a small machine-readable companion to
the Markdown replay reports. It makes the stable parts of a replay easy to
compare or validate without forcing subjective rubric notes into a rigid format.

## Required fields

- `schema_version`: currently `0.1`.
- `case_id`: an existing ID from [`docs/eval-case-index.md`](eval-case-index.md).
- `evaluated_commit`: the commit that was evaluated.
- `run_at`: an ISO 8601 timestamp.
- `environment`: model and tools used, with secrets removed.
- `result`: `pass`, `partial`, or `fail`.
- `scores`: integer 0-2 values for correctness, usefulness, safety, and brevity.
- `evidence`: one or more short observations that support the result.
- `follow_up`: the smallest next action or an explicit no-action note.

## Recommended workflow

1. Copy the template and replace every placeholder.
2. Keep the JSON result next to the Markdown report or attach it to the same
   review issue.
3. Keep disagreement explanations and nuanced failure analysis in Markdown.
4. Run `python .\scripts\validate.py`; the validator checks that the template
   remains valid JSON and retains the required fields and result values.

The JSON envelope improves repeatability; it does not turn manually judged
scores into objective measurements or claim external adoption.
