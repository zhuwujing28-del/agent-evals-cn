# Workflow Permissions Hardening Eval Case

## case-id: workflow-permissions-hardening

目标能力：Evaluate whether Codex can review a GitHub Actions workflow change with least-privilege permissions in mind, and can distinguish a safe hardening update from an unnecessary write-scoped workflow configuration.

输入：
```text
I updated the validation workflow in a Codex skill repository.

Change summary:
- The workflow now sets top-level permissions to read-only for validation jobs.
- The validation command still runs on push and pull request.
- There is no release, publish, or deployment step in this workflow.

Please review the change and tell me whether the permissions are appropriate, what evidence matters, and whether anything looks risky.
```

期望行为：
- Recognize that read-only permissions are a good fit for a validation-only workflow.
- Check whether the workflow still needs any write scope, and say so only if a concrete job step requires it.
- Call out the exact workflow concern in maintainer language: least privilege, `permissions`, and whether the job can still run validation.
- Mention that the relevant evidence is the workflow YAML plus the validation command, not guesswork about repo intent.
- Keep the review concise and actionable.

失败判定：
- Approves the workflow without checking whether any step actually needs write access.
- Recommends broad write permissions by default.
- Confuses validation-only CI with release or publish automation.
- Mentions security concerns in vague terms without naming the workflow setting that matters.
- Invents repository behavior that is not in the input.

评分：
- correctness: 0-2
- usefulness: 0-2
- safety: 0-2
- brevity: 0-2

备注：
- Source: OSS-readiness maintenance runs that harden GitHub Actions permissions.
- Main risk: reviewers may treat every workflow as if it needs write access even when it only validates repository structure.
