# agent-evals-cn

[![validate](https://github.com/zhuwujing28-del/agent-evals-cn/actions/workflows/validate.yml/badge.svg)](https://github.com/zhuwujing28-del/agent-evals-cn/actions/workflows/validate.yml)

面向中文开发者的 AI Agent / Codex skill / prompt 工作流评测与迭代仓库。

现在大家都在做 agent、MCP、Codex skills、自动化工作流，但很多项目的问题不是“能不能跑一次”，而是：

- 改了 prompt 后有没有退化？
- skill 触发是否稳定？
- 中文场景是否真的覆盖？
- 失败案例有没有沉淀成回归测试？
- 升级是不是靠感觉，而不是靠证据？

`agent-evals-cn` 试图把这些问题变成一套轻量、中文友好、可维护的评测方法。

## 当前内容

| 内容 | 说明 |
| --- | --- |
| `skills/agent-evals-cn` | 核心 Codex skill |
| `examples/eval-case-template.md` | 单个 eval case 模板 |
| `examples/eval-report-template.md` | 评测报告模板 |
| `examples/ci-failure-diagnosis-case.md` | GitHub Actions 失败诊断 eval case |
| `examples/release-readiness-case.md` | skill 仓库发布准备 eval case |
| `docs/maintenance.md` | 维护和升级流程 |
| `docs/oss-readiness.md` | 开源维护和申请准备度追踪 |
| `docs/eval-coverage-map.md` | 评测覆盖分组映射 |
| `docs/replay-submission-checklist.md` | 外部 replay 报告提交前的脱敏、评分和证据检查 |
| `docs/independent-replay-protocol.md` | 不同环境复现已有 case 的最小证据包和复核边界 |
| `docs/public-issue-follow-up-2026-08-31.md` | 跨仓库公开 issue 的当前证据和维护动作 |
| `docs/application-evidence-snapshot-2026-09-07.md` | 2026-09-07 的定点公开状态、校验和申请证据边界快照，使用前需重新核对当前 GitHub 状态 |
| `docs/usage-reports/` | 真实使用记录和跨仓库评测报告 |
| `scripts/validate.py` | 基础结构校验 |
| `APPLICATION.md` | Codex for Open Source 申请说明 |

## 为什么这个项目值得维护

- 这是一个真实会反复升级的工作流，而不是一次性提示词。
- 每次改 prompt、改 skill、改 agent 流程，都可以复用同一套 eval 思路。
- 中文场景很多，失败也很多，特别适合沉淀成回归集。
- 这个仓库本身也能被 Codex 维护，形成“自己评自己、自己升级自己”的闭环。

## 适合谁

- 正在写 Codex skills 的开发者。
- 正在维护 agent prompt / workflow 的团队。
- 想给中文 agent 场景建立回归集的开源维护者。
- 不想再靠“这次回答看起来不错”来判断质量的人。

## 安装

复制 skill 目录到 Codex skills 目录：

```powershell
Copy-Item -Recurse .\skills\agent-evals-cn $HOME\.codex\skills\
```

重启 Codex 后即可使用。

## 使用示例

你可以这样触发：

```text
帮我给这个 skill 设计 8 个中文 eval cases，并输出失败判定标准
```

```text
用 agent-evals-cn 看一下这次 prompt 升级有没有回归风险
```

```text
把这 3 次失败整理成回归 eval，并给出下一版升级计划
```

## 项目原则

- 小任务优先，而不是大而空的综合评测。
- 失败案例必须进入回归集。
- 中文场景是一等公民。
- 不用真实隐私数据做 eval。
- 不把 eval 分数包装成绝对可靠性。

## 路线图

### 已完成

- 已建立 22 个中文 baseline eval cases，并用 case index 和 coverage map 维护覆盖范围。
- 已加入 GitHub Actions、结构校验、治理文件检查和本地 Markdown 链接检查。
- 已覆盖 PR review、issue triage、CI 失败诊断、发布准备、OpenAI 文档、网页提取、
  MCP 边界、安装完整性和 OSS 申请证据等场景。
- 已提供 Markdown 评测报告模板、评分 rubric、校准说明、人工复核 runbook 和 replay 报告索引。
- 已加入 changelog、版本升级记录及 `v0.1.1` 发布准备文档。

### 近期

- 收集更多可公开、可脱敏、可复现的失败 replay 报告。
- 根据真实维护反馈补充回归 case，并记录评分分歧和后续修复。
- 持续检查 case index、coverage map、报告索引和申请材料之间的一致性。
- 用最近一次已归档的 [application evidence snapshot](docs/application-evidence-snapshot-2026-09-07.md)
  复核申请证据结构；其中的仓库状态和 CI 记录是 2026-09-07 的定点观察，
  使用前需按当前日期重新核对 GitHub。

### 中长期

- 在保持人工复核可审计的前提下，探索 JSON/Markdown 双格式报告。
- 建立跨 skill、prompt 和 agent workflow 的长期回归基线。
- 沉淀有公开证据支撑的中文 Agent/Codex 评测最佳实践。

## License

MIT
