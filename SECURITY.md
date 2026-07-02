# Security Policy

`agent-evals-cn` 维护中文 agent / prompt / Codex skill 的 eval 方法、案例和报告模板。Eval 内容经常引用失败样例、日志摘要或工具输出，因此安全重点是脱敏、边界清晰和避免把不安全行为固化成回归用例。

## Supported Scope

Please report security-sensitive issues when an eval case, template, or workflow:

- includes real API keys, cookies, tokens, credentials, personal data, private repository details, or unredacted logs;
- encourages agents to bypass access controls, paywalls, CAPTCHAs, login restrictions, or site terms;
- uses vulnerability details, exploit steps, or private incident data without clear minimization and redaction;
- defines success criteria that reward unsafe behavior, over-collection, privacy leakage, or unsupported security claims;
- weakens boundaries around web extraction, authenticated services, account actions, dependency risk, or security advisory triage.

普通 eval 质量问题可以直接提交 issue 或 PR。涉及密钥、漏洞、私有日志或未脱敏案例的问题，请先使用私下渠道联系维护者，避免公开扩散。

## Reporting

If you find a security-sensitive problem:

1. Share the affected file path and section.
2. Explain the unsafe behavior or data exposure risk.
3. Provide a redacted reproduction or safer replacement text when possible.
4. Do not paste live credentials, private logs, exploit payloads, customer data, or private repository contents into public issues.

## Maintainer Response

Maintainers should handle security-sensitive eval issues before expanding the baseline set. A typical response is:

1. remove exposed sensitive data or unsafe instructions immediately;
2. preserve the regression value with synthetic or redacted inputs when possible;
3. tighten the relevant failure criteria, safety boundary, or template guidance;
4. document public-facing changes in `CHANGELOG.md`.

## Non-Goals

This repository is not a place to publish exploit walkthroughs, private incident reports, non-consensual data collection methods, or tests that require unauthorized access to third-party systems.
