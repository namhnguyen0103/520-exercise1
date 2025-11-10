# tools/gen_tests_from_jsonl.py
import json
import re
from pathlib import Path

PROBLEM_DIR = Path("problem")
OUT_ROOT = Path("tests/generated")
PACKAGES = ["gemini_cot", "gemini_sp", "gpt_cot", "gpt_sp"]

# Heuristic: if we see these tokens, the test likely needs its setup/loop/random context.
NEEDS_CONTEXT_TOKENS = ("random", "randint", "choice", "for _ in range", "copy", "string.")

ASSERT_LINE_RE = re.compile(r"^\s*assert\s+candidate\((?P<args>.*)\)\s*(?P<op>==|in|!=|<=|>=|<|>)\s*(?P<rhs>.+?)\s*$")

def strip_main_block(code: str) -> str:
    lines = code.splitlines()
    out, skipping, base_indent = [], False, 0
    for line in lines:
        if not skipping and re.match(r'\s*if\s+__name__\s*==\s*[\'"]__main__[\'"]\s*:', line):
            skipping = True
            base_indent = len(line) - len(line.lstrip())
            continue
        if skipping:
            if line.strip() and (len(line) - len(line.lstrip())) <= base_indent:
                skipping = False
            else:
                continue
        if not skipping:
            out.append(line)
    return "\n".join(out)

def looks_like_needs_context(test_code: str) -> bool:
    code = test_code.replace(" ", "")
    for token in NEEDS_CONTEXT_TOKENS:
        if token.replace(" ", "") in code:
            return True
    # Also if there is any assignment before an assert that might be used inside asserts.
    # Quick heuristic: if there's '=' on a non-def line before any assert lines.
    for line in test_code.splitlines():
        s = line.strip()
        if not s or s.startswith("#"):
            continue
        if s.startswith("assert "):
            break
        if "=" in s and not s.startswith(("def ", "class ")):
            return True
    return False

def extract_assert_lines(test_code: str):
    """Return list of (args, op, rhs) for simple 'assert candidate(args) OP rhs' lines."""
    out = []
    for line in test_code.splitlines():
        m = ASSERT_LINE_RE.match(line.strip())
        if m:
            out.append((m.group("args"), m.group("op"), m.group("rhs")))
    return out

# --------- generation templates ----------

SIMPLE_TEST_TEMPLATE = """\
# AUTO-GENERATED: simple per-assert tests
import pytest
from {pkg}.{module_stem} import {entry_point}
{maybe_prompt_import}

{per_assert_tests}
"""

SIMPLE_ASSERT_FN = """\
def test_{pkg}_{module_stem}_{idx}():
    assert {entry_point}({args}) {op} {rhs}
"""

EXEC_TEST_TEMPLATE = """\
# AUTO-GENERATED: exec original HumanEval test (needs context)
import pytest
import importlib

def _load_module(pkg: str, module_stem: str):
    return importlib.import_module(f"{pkg}.{module_stem}")

def test_{pkg}_{module_stem}():
    mod = _load_module("{pkg}", "{module_stem}")
    candidate = getattr(mod, "{entry_point}")

    # Namespace includes candidate and any helpers defined in the solution module
    ns = {{"candidate": candidate, "{entry_point}": candidate}}
    for _name in dir(mod):
        if not _name.startswith("__"):
            try:
                ns.setdefault(_name, getattr(mod, _name))
            except Exception:
                pass

    # Provide helpers from the prompt if the solution module doesn't define them
    prompt_code = {prompt_code!r}
    if prompt_code.strip():
        exec(prompt_code, ns, ns)

    test_code = {test_code!r}
    exec(test_code, ns, ns)
    if "check" in ns and callable(ns["check"]):
        ns["check"](candidate)
"""

def main():
    OUT_ROOT.mkdir(parents=True, exist_ok=True)

    # Clean old generated tests (avoid stale module name clashes)
    for p in OUT_ROOT.glob("test_*_he*.py"):
        p.unlink()

    jsonls = sorted(PROBLEM_DIR.glob("he*.jsonl"))
    if not jsonls:
        print("No problem/he*.jsonl files found.")
        return

    for jsonl_path in jsonls:
        rec = None
        for line in jsonl_path.read_text().splitlines():
            s = line.strip()
            if s:
                rec = json.loads(s)
        if rec is None:
            continue

        module_stem = jsonl_path.stem
        entry_point  = rec["entry_point"]
        prompt_code  = strip_main_block(rec.get("prompt", ""))
        test_code    = strip_main_block(rec["test"])

        # Try to build per-assert tests if safe
        per_asserts = extract_assert_lines(test_code)
        do_simple = bool(per_asserts) and not looks_like_needs_context(test_code)

        for pkg in PACKAGES:
            out_path = OUT_ROOT / f"test_{pkg}_{module_stem}.py"
            if do_simple:
                # Optionally exec prompt to define helpers used in RHS?
                # For simple asserts, we assume no helper needed. If you have a rare case, switch to exec template.
                maybe_prompt_import = ""  # keep simple & fast
                tests_src = []
                for idx, (args, op, rhs) in enumerate(per_asserts, 1):
                    tests_src.append(SIMPLE_ASSERT_FN.format(
                        pkg=pkg, module_stem=module_stem, idx=idx,
                        entry_point=entry_point, args=args, op=op, rhs=rhs
                    ))
                code = SIMPLE_TEST_TEMPLATE.format(
                    pkg=pkg, module_stem=module_stem,
                    entry_point=entry_point, maybe_prompt_import=maybe_prompt_import,
                    per_assert_tests="\n".join(tests_src)
                )
            else:
                # Fallback: execute original test with full context (works for he50 & random/loop tests)
                code = EXEC_TEST_TEMPLATE.format(
                    pkg=pkg, module_stem=module_stem, entry_point=entry_point,
                    prompt_code=prompt_code, test_code=test_code
                )
            out_path.write_text(code)
            print(f"✅ Generated {out_path} ({'per-assert' if do_simple else 'exec'})")

if __name__ == "__main__":
    main()
