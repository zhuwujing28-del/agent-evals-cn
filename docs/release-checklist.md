# v0.1.0 Release Checklist

Use this checklist before tagging the first public baseline release.

## Preconditions

- `docs/oss-readiness.md` shows the baseline eval set as complete.
- `CHANGELOG.md` summarizes the skills, templates, examples, and CI status included in the release.
- `python scripts/validate.py` passes locally.
- The public `validate` GitHub Actions workflow is green on `main`.
- No private logs, customer data, access tokens, or unpublished repo details appear in examples or usage reports.

## Release steps

1. Review the current baseline cases under `examples/` and confirm they still represent maintainer workflows worth rerunning.
2. Run `python scripts/validate.py`.
3. Check the README badge links to the public workflow page.
4. Update `CHANGELOG.md` by moving relevant `Unreleased` notes under `v0.1.0`.
5. Create an annotated tag:

   ```powershell
   git tag -a v0.1.0 -m "agent-evals-cn v0.1.0"
   git push origin v0.1.0
   ```

6. Confirm the GitHub release or tag page renders README links, examples, and documentation correctly.

## Do not release if

- A baseline case is only a placeholder and cannot be judged by a maintainer.
- The validation workflow is failing or missing from the public repository.
- The changelog claims automated scoring that the project does not provide.
- A usage report depends on private data that cannot be safely reviewed.
