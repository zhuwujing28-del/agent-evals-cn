from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "agent-evals-cn" / "SKILL.md"
EXAMPLES = ROOT / "examples"
CASE_INDEX = ROOT / "docs" / "eval-case-index.md"
MARKDOWN_LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
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


def validate_eval_case_index() -> list[str]:
    errors: list[str] = []
    case_paths = sorted(EXAMPLES.glob("*-case.md"))

    if not CASE_INDEX.exists():
        return [f"{CASE_INDEX.relative_to(ROOT)}: missing eval case index"]

    index_text = CASE_INDEX.read_text(encoding="utf-8")
    for path in case_paths:
        rel_path = path.relative_to(ROOT).as_posix()
        if rel_path not in index_text:
            errors.append(f"{CASE_INDEX.relative_to(ROOT)}: missing {rel_path}")

    return errors


def validate_markdown_links() -> list[str]:
    errors: list[str] = []
    for md_path in sorted(ROOT.rglob("*.md")):
        text = md_path.read_text(encoding="utf-8")
        for match in MARKDOWN_LINK_RE.finditer(text):
            target = match.group(1).strip()
            if (
                not target
                or target.startswith(("#", "http://", "https://", "mailto:"))
                or "://" in target
            ):
                continue

            link_path = target.split("#", 1)[0]
            if not link_path:
                continue

            resolved = (md_path.parent / link_path).resolve()
            try:
                resolved.relative_to(ROOT)
            except ValueError:
                continue

            if not resolved.exists():
                rel_md = md_path.relative_to(ROOT)
                errors.append(f"{rel_md}: broken local link {target}")

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

    index_errors = validate_eval_case_index()
    if index_errors:
        print("Validation failed:")
        for error in index_errors:
            print(f"- {error}")
        return 1

    link_errors = validate_markdown_links()
    if link_errors:
        print("Validation failed:")
        for error in link_errors:
            print(f"- {error}")
        return 1

    print("agent-evals-cn structure looks good.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
