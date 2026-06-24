---
name: agent-evals-cn
description: Use when designing, reviewing, or improving AI agent, Codex skill, prompt, or workflow quality through Chinese eval tasks, failure analysis, regression checks, and versioned upgrade plans.
---

# Agent Evals CN

面向中文开发者的 AI Agent / Codex skill / prompt 工作流评测 skill。目标不是“感觉更好”，而是用一组小而稳定的任务，判断一次 agent 改动是否真的更可靠。

## 适用场景

- 用户要优化一个 Codex skill、agent prompt、system prompt、workflow 或自动化脚本。
- 用户说“这个 skill 靠不靠谱”“怎么评测 agent”“升级后会不会退化”。
- 需要为开源项目维护一套中文 agent evals。
- 需要把失败案例整理成可复现任务和升级计划。

## 不适用场景

- 用户只想马上完成一次普通代码修改。
- 没有可评测的任务目标、输入或期望行为。
- 评测需要真实用户隐私数据且未脱敏。
- 高风险领域结论，例如医疗、法律、金融判断质量，除非只评估工程流程。

## 核心原则

1. 小任务优先。
   - 每个 eval case 只测一个能力或一个失败模式。
   - 不用大而全的“综合测试”掩盖问题。

2. 可复现优先。
   - 固定输入、上下文、期望输出和判分标准。
   - 把“我觉得不对”转成可复现失败。

3. 回归优先。
   - 每次升级前后跑同一组 cases。
   - 新增失败案例要进入回归集。

4. 中文场景优先。
   - 覆盖中文需求、中文文件名、中英混写、中文技术表达、国内开发者常见环境。

5. 不追求一次满分。
   - 先识别高价值失败模式，再小步升级 skill 或 prompt。

## 工作流

1. 明确评测对象。
   - 是 skill、prompt、agent workflow、自动化脚本，还是模型调用链？
   - 记录版本、入口文件、关键规则和预期用户。

2. 建立 eval 任务集。
   - 选 5-12 个代表性任务。
   - 至少包含：正常路径、边界输入、信息不足、冲突指令、安全边界、中文表达。
   - 每个 case 写清输入、期望行为、失败判定。

3. 选择评分方式。
   - 确定性任务：用脚本、diff、测试、结构化字段判分。
   - 文本任务：用 rubric 判分，至少包含 correctness、usefulness、safety、brevity。
   - 不要只用“看起来不错”。

4. 跑 baseline。
   - 先评当前版本，不要边跑边改。
   - 记录通过、失败、部分通过和失败原因。

5. 分析失败模式。
   - 按类别归因：触发不准、上下文不足、步骤缺失、边界不清、输出格式漂移、过度执行、安全风险。
   - 找重复出现的失败，不被单个偶然案例带偏。

6. 制定升级计划。
   - 每次只改 1-3 个主要问题。
   - 修改后重跑相同 evals。
   - 如果修复 A 导致 B 退化，优先记录并缩小改动。

7. 版本化维护。
   - 把新增 eval case、失败模式、升级记录写入仓库。
   - release note 要说明新增能力和已知限制。

## Eval Case 模板

```md
## case-id: short-name

目标能力：

输入：
```text
...
```

期望行为：
- ...

失败判定：
- ...

评分：
- correctness: 0-2
- usefulness: 0-2
- safety: 0-2
- brevity: 0-2
```

## 输出格式

评测后输出：

```text
评测对象：
任务数量：
通过 / 部分通过 / 失败：

主要失败模式：
- ...

建议升级：
1. ...
2. ...
3. ...

回归风险：
- ...

下一轮 eval 应新增：
- ...
```

## 安全边界

- 不要用真实密钥、cookie、个人身份信息、未脱敏日志做 eval。
- 不要为了让分数变好而删除困难案例。
- 不要把模型主观偏好当成唯一评分依据。
- 不要声称“通过 eval = 绝对可靠”；eval 只能覆盖已设计场景。

## 验证方式

- 每个升级建议都应对应至少一个失败 case。
- 修改后应重跑 baseline cases。
- 如果不能实际运行 eval，输出可执行的 eval plan，并说明未运行原因。
