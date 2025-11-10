# AUTO-GENERATED: exec original HumanEval test (needs context)
import pytest
import importlib

def _load_module(pkg: str, module_stem: str):
    return importlib.import_module(f"gemini_cot.he40")

def test_gemini_cot_he40():
    mod = _load_module("gemini_cot", "he40")
    candidate = getattr(mod, "triples_sum_to_zero")

    # Namespace includes candidate and any helpers defined in the solution module
    ns = {"candidate": candidate, "triples_sum_to_zero": candidate}
    for _name in dir(mod):
        if not _name.startswith("__"):
            try:
                ns.setdefault(_name, getattr(mod, _name))
            except Exception:
                pass

    # Provide helpers from the prompt if the solution module doesn't define them
    prompt_code = '\n\ndef triples_sum_to_zero(l: list):\n    """\n    triples_sum_to_zero takes a list of integers as an input.\n    it returns True if there are three distinct elements in the list that\n    sum to zero, and False otherwise.\n\n    >>> triples_sum_to_zero([1, 3, 5, 0])\n    False\n    >>> triples_sum_to_zero([1, 3, -2, 1])\n    True\n    >>> triples_sum_to_zero([1, 2, 3, 7])\n    False\n    >>> triples_sum_to_zero([2, 4, -5, 3, 9, 7])\n    True\n    >>> triples_sum_to_zero([1])\n    False\n    """'
    if prompt_code.strip():
        exec(prompt_code, ns, ns)

    test_code = '\n\nMETADATA = {}\n\n\ndef check(candidate):\n    assert candidate([1, 3, 5, 0]) == False\n    assert candidate([1, 3, 5, -1]) == False\n    assert candidate([1, 3, -2, 1]) == True\n    assert candidate([1, 2, 3, 7]) == False\n    assert candidate([1, 2, 5, 7]) == False\n    assert candidate([2, 4, -5, 3, 9, 7]) == True\n    assert candidate([1]) == False\n    assert candidate([1, 3, 5, -100]) == False\n    assert candidate([100, 3, 5, -100]) == False\n'
    exec(test_code, ns, ns)
    if "check" in ns and callable(ns["check"]):
        ns["check"](candidate)
