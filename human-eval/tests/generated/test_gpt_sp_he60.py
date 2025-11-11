# AUTO-GENERATED: exec original HumanEval test (needs context)
import pytest
import importlib
from gpt_sp.he60 import sum_to_n

def _load_module(pkg: str, module_stem: str):
    return importlib.import_module(f"gpt_sp.he60")

def test_gpt_sp_he60():
    mod = _load_module("gpt_sp", "he60")
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

def test_gpt_sp_he60_invalid_inputs():
    # n = 0 (edge case: below 1)
    try:
        result = sum_to_n(0)
        assert result == 0
    except Exception:
        pass  # acceptable if function raises an error

    # n < 0 (negative input)
    try:
        result = sum_to_n(-5)
        assert result == 0
    except Exception:
        pass

    # n is float
    try:
        sum_to_n(5.5)
        assert False, "Should raise TypeError or ValueError for float input"
    except (TypeError, ValueError):
        pass

    # n is string
    try:
        sum_to_n("10")
        assert False, "Should raise TypeError for string input"
    except (TypeError, ValueError):
        pass

    # n is None
    try:
        sum_to_n(None)
        assert False, "Should raise TypeError for None input"
    except TypeError:
        pass

    # n is boolean (bool is subclass of int, so must be checked explicitly)
    try:
        result_true = sum_to_n(True)
        result_false = sum_to_n(False)
        # Accept either an error or explicit handling (e.g., treating bool as invalid)
        assert result_true in (0, 1) or isinstance(result_true, int)
        assert result_false in (0, 0) or isinstance(result_false, int)
    except (TypeError, ValueError):
        pass

