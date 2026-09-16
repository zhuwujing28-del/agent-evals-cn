from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from validate import validate_result_data


ROOT = Path(__file__).resolve().parents[1]
CASE_INDEX = ROOT / "docs" / "eval-case-index.md"


def load_case_ids() -> set[str]:
    return {
        line.removeprefix("## case-id:").strip()
        for path in sorted((ROOT / "examples").glob("*-case.md"))
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.startswith("## case-id:")
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate one structured agent-evals-cn replay result."
    )
    parser.add_argument(
        "result",
        help="JSON result path, or '-' to read JSON from stdin",
    )
    args = parser.parse_args()

    try:
        if args.result == "-":
            raw = sys.stdin.read()
            label = "stdin"
        else:
            path = Path(args.result)
            raw = path.read_text(encoding="utf-8")
            label = str(path)
        data = json.loads(raw)
    except (OSError, json.JSONDecodeError) as error:
        print(f"Validation failed: {error}", file=sys.stderr)
        return 1

    errors = validate_result_data(data, label, load_case_ids())
    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Structured replay result is valid: {label}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
