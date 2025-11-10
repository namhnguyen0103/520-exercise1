"""
Summarize baseline coverage results for each problem & solution.

Inputs (produce these first with pytest):
  - coverage.xml         (pytest --cov-report=xml:coverage.xml)
  - pytest-report.xml    (pytest --junitxml=pytest-report.xml)

Output:
  - summary.md
"""

from pathlib import Path
from collections import defaultdict
import xml.etree.ElementTree as ET

COVERAGE_XML = Path("coverage.xml")
PYTEST_XML = Path("pytest-report.xml")
OUTPUT = Path("summary.md")

PKGS = ["gemini_cot", "gemini_sp", "gpt_cot", "gpt_sp"]

def parse_coverage():
    """
    Return dict[(pkg, problem)] -> (line%, branch%) using coverage.py XML.
    Works even if the XML structure varies slightly.
    """
    res = {}
    if not COVERAGE_XML.exists():
        return res

    tree = ET.parse(COVERAGE_XML)
    root = tree.getroot()

    # coverage.py typically has: coverage -> packages -> package -> classes -> class
    # but ".//class" is safest; still we’ll also look for <package> aggregates if needed.
    classes = list(root.findall(".//class"))
    if not classes:
        # Some versions only expose rates on <package> (folder) level
        # but that’s rare; we’ll bail out gracefully if nothing is present.
        return res

    for cls in classes:
        filename = cls.get("filename") or ""
        # Expect "gemini_cot/he30.py" etc.
        parts = filename.split("/")
        if len(parts) != 2:
            continue
        pkg, fname = parts
        if pkg not in PKGS:
            continue
        if not fname.endswith(".py"):
            continue
        problem = fname[:-3]  # he30
        # line/branch rates are floats in [0,1]
        try:
            line_rate = float(cls.get("line-rate", "0"))
        except Exception:
            line_rate = 0.0
        try:
            branch_rate = float(cls.get("branch-rate", "0"))
        except Exception:
            branch_rate = 0.0
        res[(pkg, problem)] = (round(line_rate * 100, 1), round(branch_rate * 100, 1))

    return res

def parse_pytest():
    """
    Return dict[(pkg, problem)] -> tests_passed (0/1) and also a set of all problems seen.
    We expect our generated tests to be named like: test_{pkg}_{heXX}
    """
    passes = defaultdict(int)
    problems_seen = set()

    if not PYTEST_XML.exists():
        return passes, problems_seen

    tree = ET.parse(PYTEST_XML)
    root = tree.getroot()

    # Each <testcase name="test_gemini_cot_he30"> ...
    for case in root.iter("testcase"):
        name = case.get("name", "")
        # try to parse "test_{pkg}_{heXX}"
        # split only on first two underscores after "test_"
        if not name.startswith("test_"):
            continue
        parts = name[len("test_"):].split("_")
        if len(parts) < 2:
            continue
        # pkg may itself contain underscores (gemini_cot), so join all except last as pkg
        pkg = "_".join(parts[:-1])
        problem = parts[-1]
        problems_seen.add(problem)
        if pkg not in PKGS:
            continue
        failed = (case.find("failure") is not None) or (case.find("error") is not None)
        skipped = (case.find("skipped") is not None)
        passes[(pkg, problem)] = 0 if (failed or skipped) else 1

    return passes, problems_seen

def interpret(line_pct, branch_pct, passed):
    if passed == 0:
        return "❌ test failed"
    if line_pct < 100 and branch_pct < 100:
        return "⚠️ partial line & branch coverage"
    if line_pct < 100:
        return "⚠️ partial line coverage — unexecuted code"
    if branch_pct < 100:
        return "⚠️ low branch coverage — some conditionals untested"
    return "✅ fully covered"

def main():
    cov = parse_coverage()
    tests, problems_from_tests = parse_pytest()

    # Build the set of problems to report: prefer what coverage saw; fall back to pytest names.
    problems = sorted({prob for (_, prob) in cov.keys()} | problems_from_tests,
                      key=lambda s: (len(s), s))

    lines = []
    lines.append("# Baseline Coverage Summary\n")

    if not problems:
        lines.append("> No problems found. Make sure you ran pytest with:")
        lines.append("> `--cov-report=xml:coverage.xml --junitxml=pytest-report.xml` from the repo root.")
        OUTPUT.write_text("\n".join(lines))
        print(f"⚠️  No problems found. Wrote {OUTPUT} with a hint.")
        return

    # Per-problem section
    for prob in problems:
        lines.append(f"## {prob}\n")
        lines.append("| Solution | Tests Passed | Line % | Branch % | Notes |")
        lines.append("|-----------|-------------:|------:|---------:|-------|")
        for pkg in PKGS:
            line_pct, branch_pct = cov.get((pkg, prob), (0.0, 0.0))
            passed = tests.get((pkg, prob), 0)
            note = interpret(line_pct, branch_pct, passed)
            lines.append(f"| `{pkg}` | {passed} | {line_pct:.1f} | {branch_pct:.1f} | {note} |")
        lines.append("")

    # Overall table (averages across solutions)
    lines.append("## Overall Summary (average across solutions)\n")
    lines.append("| Problem | Avg Line % | Avg Branch % | Notes |")
    lines.append("|---------|-----------:|-------------:|-------|")
    for prob in problems:
        line_vals = [cov.get((pkg, prob), (0.0, 0.0))[0] for pkg in PKGS]
        branch_vals = [cov.get((pkg, prob), (0.0, 0.0))[1] for pkg in PKGS]
        avg_line = sum(line_vals) / len(PKGS)
        avg_branch = sum(branch_vals) / len(PKGS)
        note = "branch gaps" if (avg_line - avg_branch) > 15 else ""
        lines.append(f"| {prob} | {avg_line:.1f} | {avg_branch:.1f} | {note} |")

    OUTPUT.write_text("\n".join(lines))
    print(f"✅ Wrote {OUTPUT} ({len(problems)} problems)")

if __name__ == "__main__":
    main()
