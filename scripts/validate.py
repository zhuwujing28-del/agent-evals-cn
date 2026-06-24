from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "agent-evals-cn" / "SKILL.md"
REQUIRED = [
    "name: agent-evals-cn",
    "description:",
    "## 适用场景",
    "## 不适用场景",
    "## 工作流",
    "## 安全边界",
    "## 验证方式",
]


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

    print("agent-evals-cn structure looks good.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
