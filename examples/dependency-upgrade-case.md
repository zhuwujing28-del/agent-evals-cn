# Dependency Upgrade Eval Case

## case-id: major-upgrade-with-breaking-change

目标能力：

评估一个依赖 major upgrade PR，识别 breaking change、验证计划和合并风险。

输入：

```text
Dependabot 提了一个 PR，把 build tool 从 4.x 升到 5.x。
lockfile 改动很多，CI 目前只有 lint 通过，测试还没跑。
请用中文 review 这个升级 PR，判断能不能合并。
```

期望行为：

- 识别 major upgrade 不能仅凭 lint 通过合并。
- 要求查看 changelog / migration guide / breaking changes。
- 建议运行最小相关测试、build、typecheck 或 smoke test。
- 检查 lockfile 变化是否异常扩大。
- 输出 merge / request changes / hold 建议。

失败判定：

- 只说“Dependabot PR 可以自动合并”。
- 没有提 breaking changes 或 migration guide。
- 没有验证计划。
- 忽略 lockfile 风险。
