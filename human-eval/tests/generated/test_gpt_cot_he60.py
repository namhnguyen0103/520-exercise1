# AUTO-GENERATED: exec original HumanEval test (needs context)
import pytest
import importlib

def _load_module(pkg: str, module_stem: str):
    return importlib.import_module(f"gpt_cot.he60")

def test_gpt_cot_he60():
    mod = _load_module("gpt_cot", "he60")
    candidate = getattr(mod, "sum_to_n")

    # Namespace includes candidate and any helpers defined in the solution module
    ns = {"candidate": candidate, "sum_to_n": candidate}
    for _name in dir(mod):
        if not _name.startswith("__"):
            try:
                ns.setdefault(_name, getattr(mod, _name))
            except Exception:
                pass

    # Provide helpers from the prompt if the solution module doesn't define them
    prompt_code = '\n\ndef sum_to_n(n: int):\n    """sum_to_n is a function that sums numbers from 1 to n.\n    >>> sum_to_n(30)\n    465\n    >>> sum_to_n(100)\n    5050\n    >>> sum_to_n(5)\n    15\n    >>> sum_to_n(10)\n    55\n    >>> sum_to_n(1)\n    1\n    """'
    if prompt_code.strip():
        exec(prompt_code, ns, ns)

    test_code = '\n\nMETADATA = {}\n\n\ndef check(candidate):\n    assert candidate(1) == 1\n    assert candidate(6) == 21\n    assert candidate(11) == 66\n    assert candidate(30) == 465\n    assert candidate(100) == 5050\n'
    exec(test_code, ns, ns)
    if "check" in ns and callable(ns["check"]):
        ns["check"](candidate)
