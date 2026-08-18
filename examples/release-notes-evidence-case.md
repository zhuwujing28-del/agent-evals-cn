# Release notes evidence eval case

## case-id: release-notes-from-maintainer-diff

目标能力：检查 agent 是否能从 maintainer-facing commits、diff 和验证证据中生成清晰、克制、可发布的中文 release notes。

输入：

```text
请根据最近 4 个 commit 为 v0.2.0 写中文 release notes。

commit 摘要：
- Add repo-onboarding-cn sample output
- Add bug-reproduction-cn maintainer skill
- Fix maintainer feedback template encoding
- Refresh OSS application skill coverage

已验证：python scripts/validate-skills.py；git diff --check。
目标读者：中文 OSS 维护者。
注意：不要夸大为稳定版，不要声称已有外部用户采纳。
```

期望行为：

- 先把输入中的 commit、验证命令、目标读者和限制条件复述成写作边界。
- 输出面向用户的 release notes，至少包含：新增、修复、文档/申请材料、验证、升级提示。
- 明确区分“已经发布的变化”和“仍需真实维护者反馈验证的假设”。
- 使用中文维护者能直接发布的语气，避免营销化、绝对化或超出证据的表述。
- 如果验证证据不完整，应把缺口写进“发布前确认”，而不是假装已通过。

失败判定：

- 把输入没有提供的外部采纳、性能提升、稳定性结论写成事实。
- 只复述 commit 列表，没有把变化整理成读者可理解的发布说明。
- 遗漏验证状态、升级提示或限制条件。
- 把 v0.2.0 包装成成熟稳定版，而不是 0.x 阶段的维护者工作流改进。
- 没有保留人工发布前需要确认的风险或待办。

## 评分提示

- `pass`：release notes 可直接进入 PR/release draft，且所有 claims 都能追溯到输入证据。
- `partial`：结构基本可用，但有少量泛化、缺少验证说明，或升级提示不够明确。
- `fail`：生成宣传稿、虚构采用证据，或忽略 maintainer-facing 读者目标。

## 回归价值

这个 case 对应 `codex-skills-cn` 的 `release-notes-cn` skill 和样例输出，防止后续 prompt 升级把 release notes 变成“总结 commit”或“营销包装”。它也补齐 Open Source 申请材料中的发布沟通证据：每次公开变更都应能说明 shipped 内容、验证方式和仍待反馈的边界。
