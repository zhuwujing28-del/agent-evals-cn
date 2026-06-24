# agent-evals-cn

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
| `docs/maintenance.md` | 维护和升级流程 |
| `scripts/validate.py` | 基础结构校验 |

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

- 增加 GitHub Action，自动校验 skill 结构。
- 增加更多 eval case 示例：PR review、issue triage、OpenAI API 问答、网页提取。
- 增加 JSON/Markdown 双格式评测报告。
- 增加 changelog 和版本升级记录。

## License

MIT
