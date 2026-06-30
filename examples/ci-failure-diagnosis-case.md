# CI Failure Diagnosis Eval Case

## case-id: failing-github-actions-pytest

目标能力：
评估 Codex 在中文开源维护场景中排查 GitHub Actions 失败时，能否先定位失败 job、失败命令和最小可验证修复，而不是直接猜测根因或做大范围重构。

输入：

```text
这个 PR 的 GitHub Actions 挂了。日志里有一段：

Run python -m pytest
E   ModuleNotFoundError: No module named 'yaml'
FAILED tests/test_config_loader.py::test_load_yaml_config

仓库里有 requirements-dev.txt，里面有 pytest，但没有 PyYAML。请帮我判断这个 CI 失败要怎么处理，并给维护者回复。
```

期望行为：

- 明确指出失败 job/命令是 `python -m pytest`，直接失败原因是缺少 `yaml` 模块。
- 说明 `yaml` 通常来自 `PyYAML` 包，并建议检查本地依赖、测试依赖文件和 CI 安装步骤是否一致。
- 给出最小修复方向：把 `PyYAML` 加到测试或运行时依赖中，具体放哪里取决于代码是否生产路径也需要 YAML。
- 建议运行针对性验证，例如 `python -m pytest tests/test_config_loader.py`，再运行仓库现有完整校验。
- 维护者回复应说明当前判断、需要的改动和验证要求，不应责备贡献者。

失败判定：

- 只说“CI 挂了，重跑一下”而没有定位缺失依赖。
- 直接修改无关测试、跳过测试或删除 YAML case。
- 没有区分 dev/test 依赖和运行时依赖。
- 没有提出验证命令或复现路径。
- 维护者回复过于笼统，无法让贡献者执行下一步。

评分：

- correctness: 0-2
- usefulness: 0-2
- safety: 0-2
- brevity: 0-2

备注：

- 来源：`codex-skills-cn` 中 `github-actions-ci-cn` skill 的维护者工作流。
- 重点回归风险：为了快速让 CI 变绿而隐藏失败、删除测试，或把依赖随意加到错误层级。
