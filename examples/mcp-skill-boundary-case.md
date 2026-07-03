# MCP vs Skill Boundary Eval Case

## case-id: mcp-skill-boundary-maintainer-answer

目标能力：

评估 agent 是否能向中文开源维护者清楚区分 MCP server、Codex skill、普通 prompt 和脚本，并给出适合仓库维护场景的选择建议。

输入：

```text
我在维护一个 Codex skills 仓库。有人提 issue 说“能不能把这个 skill 改成 MCP”，但他其实只是想复用一套中文 PR review 流程。
请用中文帮我判断：什么时候应该写 skill，什么时候应该写 MCP server，什么时候只需要 README/prompt 示例？
最后给一个可以回复 issue 的简短建议。
```

期望行为：

- 先确认用户目标是复用维护流程，而不是接入外部工具或长期服务。
- 区分 skill、MCP server、prompt/README 示例、脚本各自适合的边界。
- 说明 MCP 适合暴露工具、数据源、长连接能力或需要被多个客户端调用的能力。
- 说明 skill 适合封装 Codex 工作流、触发条件、检查清单、输出格式和安全边界。
- 给出可直接回复 issue 的简短、礼貌、可执行建议。
- 如信息不足，提出最多一两个关键澄清问题，而不是泛泛要求更多背景。

失败判定：

- 把所有复用需求都建议做成 MCP server。
- 把 MCP 描述成普通 prompt 或文档模板。
- 没有根据维护者场景给出选择标准。
- 回复 issue 的建议过长、不可执行，或没有中文维护者语境。
- 在没有外部工具需求时引入复杂服务架构。

安全与维护说明：

- 不要求创建真实 MCP server 或修改仓库配置。
- 如果回答引用公开文档，应说明需要核对最新官方说明。
- 不应建议把私有 token、账号信息或本地路径写进 skill 示例。
