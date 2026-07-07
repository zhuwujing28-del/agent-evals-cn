from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "agent-evals-cn" / "SKILL.md"
EXAMPLES = ROOT / "examples"
REQUIRED = [
    "name: agent-evals-cn",
    "description:",
    "## 适用场景",
    "## 不适用场景",
    "## 工作流",
    "## 安全边界",
    "## 验证方式",
]
CASE_REQUIRED = [
    "目标能力：",
    "输入：",
    "期望行为：",
    "失败判定：",
]


def validate_eval_cases() -> list[str]:
    errors: list[str] = []
    case_ids: dict[str, Path] = {}

    case_paths = sorted(EXAMPLES.glob("*-case.md"))
    if not case_paths:
        return ["examples: no eval case files found"]

    for path in case_paths:
        text = path.read_text(encoding="utf-8")
        rel_path = path.relative_to(ROOT)

        case_id = None
        for line in text.splitlines():
            if line.startswith("## case-id:"):
                case_id = line.removeprefix("## case-id:").strip()
                break

        if not case_id:
            errors.append(f"{rel_path}: missing ## case-id")
        elif case_id in case_ids:
            first = case_ids[case_id].relative_to(ROOT)
            errors.append(f"{rel_path}: duplicate case-id {case_id} already used by {first}")
        else:
            case_ids[case_id] = path

        for item in CASE_REQUIRED:
            if item not in text:
                errors.append(f"{rel_path}: missing {item}")

    return errors


def main() -> int:
    if not SKILL.exists():
        print(f"Missing {SKILL}")
        return 1

    text = SKILL.read_text(encoding="utf-8")
    missing = [item for item in REQUIRED if item not in text]
    if missing:
        print("Validation failed:")
        for item in missing:
            print(f"- missing {item}")
        return 1

    case_errors = validate_eval_cases()
    if case_errors:
        print("Validation failed:")
        for error in case_errors:
            print(f"- {error}")
        return 1

    print("agent-evals-cn structure looks good.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
