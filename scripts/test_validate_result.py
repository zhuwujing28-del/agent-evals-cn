from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path

from validate import RESULT_REQUIRED, validate_result_data


ROOT = Path(__file__).resolve().parents[1]
CASE_IDS = {
    line.removeprefix("## case-id:").strip()
    for path in (ROOT / "examples").glob("*-case.md")
    for line in path.read_text(encoding="utf-8").splitlines()
    if line.startswith("## case-id:")
}


def valid_result() -> dict:
    data = json.loads(
        (ROOT / "examples" / "eval-result-template.json").read_text(encoding="utf-8")
    )
    data["case_id"] = sorted(CASE_IDS)[0]
    return data


class ValidateResultTests(unittest.TestCase):
    def test_valid_result_labels(self) -> None:
        for result in ("pass", "partial", "fail"):
            with self.subTest(result=result):
                data = valid_result()
                data["result"] = result
                self.assertEqual(validate_result_data(data, "test", CASE_IDS), [])

    def test_invalid_result_types_return_errors(self) -> None:
        for result in ([], {}, None, True, 1, "", "PASS"):
            with self.subTest(result=result):
                data = valid_result()
                data["result"] = result
                errors = validate_result_data(data, "test", CASE_IDS)
                self.assertTrue(any("result must be one of" in error for error in errors))

    def test_invalid_timestamps_return_errors(self) -> None:
        for timestamp in (
            "", "yesterday", "2026-10-27", "2026-02-30T10:00:00Z",
            "2026-10-27T25:00:00Z", "2026-10-27T10:00:00+25:00", None, 123,
        ):
            with self.subTest(timestamp=timestamp):
                data = valid_result()
                data["run_at"] = timestamp
                errors = validate_result_data(data, "test", CASE_IDS)
                self.assertTrue(any("run_at" in error for error in errors))

    def test_valid_iso_timestamps(self) -> None:
        for timestamp in (
            "2026-10-27T10:00:00Z", "2026-10-27T18:00:00+08:00",
            "2026-10-27T10:00:00.123456+00:00", "2026-10-27T10:00:00",
        ):
            with self.subTest(timestamp=timestamp):
                data = valid_result()
                data["run_at"] = timestamp
                self.assertEqual(validate_result_data(data, "test", CASE_IDS), [])

    def test_each_required_field(self) -> None:
        for field in RESULT_REQUIRED:
            with self.subTest(field=field):
                data = valid_result()
                del data[field]
                self.assertIn(
                    f"test: missing {field}",
                    validate_result_data(data, "test", CASE_IDS),
                )

    def test_unknown_case_id(self) -> None:
        data = valid_result()
        data["case_id"] = "unknown-case-id"
        self.assertTrue(validate_result_data(data, "test", CASE_IDS))

    def test_scores_reject_boolean_and_out_of_range_values(self) -> None:
        for score in (True, False, -1, 3, 1.0, "2", None):
            with self.subTest(score=score):
                data = valid_result()
                data["scores"]["safety"] = score
                self.assertTrue(validate_result_data(data, "test", CASE_IDS))

    def test_top_level_must_be_object(self) -> None:
        for data in ([], None, "result", 1):
            with self.subTest(data=data):
                self.assertEqual(
                    validate_result_data(data, "test", CASE_IDS),
                    ["test: top-level value must be an object"],
                )

    def test_cli_stdin_exit_codes_and_diagnostics(self) -> None:
        invalid_result = valid_result()
        invalid_result["result"] = []
        invalid_timestamp = valid_result()
        invalid_timestamp["run_at"] = "yesterday"
        for data, exit_code, message in (
            (valid_result(), 0, "Structured replay result is valid: stdin"),
            (invalid_result, 1, "result must be one of"),
            (invalid_timestamp, 1, "run_at"),
            ("{", 1, "Validation failed:"),
        ):
            with self.subTest(data=data):
                raw = data if isinstance(data, str) else json.dumps(data)
                completed = subprocess.run(
                    [sys.executable, str(ROOT / "scripts" / "validate-result.py"), "-"],
                    input=raw,
                    capture_output=True,
                    text=True,
                    timeout=10,
                )
                output = completed.stdout + completed.stderr
                self.assertEqual(completed.returncode, exit_code, output)
                self.assertIn(message, output)
                self.assertNotIn("Traceback", output)


if __name__ == "__main__":
    unittest.main()
