import io
import json
import runpy
import sys
from pathlib import Path

import pytest

# Where your APPS JSON problems live
PROBLEMS_DIR = Path("problems")

# Your solution folders (these are filesystem paths, hyphens are OK)
SOLUTION_DIRS = ["gemini-cot", "gemini-sp", "gpt-cot", "gpt-sp"]
# SOLUTION_DIRS = ["gpt-sp"]

# If your files are named like "<problem_id>.py" inside each solution dir:
FILENAME_PATTERN = "apps{problem_id}.py"

# Optional: per-case timeout (requires pytest-timeout plugin if you want hard timeouts)
DEFAULT_TIMEOUT_S = 5


def discover_cases():
    """
    Yields tuples:
      (solution_dir, problem_id, case_index, input_text, expected_output, solution_path)
    Skips (marks) any case where the corresponding solution file does not exist.
    """
    params = []
    ids = []
    for json_path in sorted(PROBLEMS_DIR.glob("problem_*.json")):
        data = json.loads(json_path.read_text())
        problem_id = str(data.get("problem_id") or json_path.stem.split("_")[-1])
        inputs = data["input_output"]["inputs"]
        outputs = data["input_output"]["outputs"]

        assert len(inputs) == len(outputs), f"Mismatch IO lengths in {json_path}"

        for sol_dir in SOLUTION_DIRS:
            sol_path = Path(sol_dir) / FILENAME_PATTERN.format(problem_id=problem_id)
            if not sol_path.exists():
                # Mark a single skip for this problem/solution pair
                params.append(pytest.param(sol_dir, problem_id, None, None, None, sol_path,
                                           marks=pytest.mark.skip(reason=f"missing {sol_path}")))
                ids.append(f"{sol_dir}::{problem_id}::missing")
                continue

            for idx, (inp, out) in enumerate(zip(inputs, outputs)):
                params.append((sol_dir, problem_id, idx, inp, out, sol_path))
                ids.append(f"{sol_dir}::{problem_id}::case{idx}")
    return params, ids


def _normalize_text(s: str) -> str:
    """
    Normalize both expected and actual outputs:
    - trim only final newline bouquet
    - strip trailing spaces on each line
    - ensure single trailing newline for exact comparison
    """
    lines = s.rstrip("\n").splitlines()
    lines = [ln.rstrip() for ln in lines]
    return "\n".join(lines) + ("\n" if lines else "")


def _run_script_with_stdin(pyfile: Path, stdin_text: str) -> str:
    """
    Execute a script file in-process (so coverage counts), feeding stdin_text,
    and capture stdout as returned string.
    """
    # Backup stdio
    old_stdin, old_stdout = sys.stdin, sys.stdout
    try:
        sys.stdin = io.StringIO(stdin_text)
        out_buf = io.StringIO()
        sys.stdout = out_buf

        # Run as a "program": this executes top-level code (like Codeforces scripts)
        # Using run_name="__main__" emulates execution as a script.
        runpy.run_path(str(pyfile), run_name="__main__")

        return out_buf.getvalue()
    finally:
        sys.stdin, sys.stdout = old_stdin, old_stdout


# Build parameter list once
_PARAMS, _IDS = discover_cases()


@pytest.mark.parametrize(
    "solution_dir,problem_id,case_index,input_text,expected_output,solution_path",
    _PARAMS,
    ids=_IDS
)
def test_apps_case(solution_dir, problem_id, case_index, input_text, expected_output, solution_path):
    # Skipped items (missing solution) never reach here
    # OPTIONAL: enforce per-case timeout with pytest-timeout (uncomment if you use it)
    # pytest.timeout(DEFAULT_TIMEOUT_S)

    actual = _run_script_with_stdin(solution_path, input_text)
    assert _normalize_text(actual) == _normalize_text(expected_output), (
        f"\n=== Mismatch ===\n"
        f"solution: {solution_dir}/{problem_id}.py\n"
        f"case: {case_index}\n"
        f"--- input ---\n{input_text}\n"
        f"--- expected ---\n{expected_output}\n"
        f"--- actual ---\n{actual}\n"
    )
