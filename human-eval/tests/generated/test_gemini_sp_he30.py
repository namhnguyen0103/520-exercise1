# AUTO-GENERATED: exec original HumanEval test (needs context)
import pytest
import importlib

def _load_module(pkg: str, module_stem: str):
    return importlib.import_module(f"gemini_sp.he30")

def test_gemini_sp_he30():
    mod = _load_module("gemini_sp", "he30")
    candidate = getattr(mod, "get_positive")

    # Namespace includes candidate and any helpers defined in the solution module
    ns = {"candidate": candidate, "get_positive": candidate}
    for _name in dir(mod):
        if not _name.startswith("__"):
            try:
                ns.setdefault(_name, getattr(mod, _name))
            except Exception:
                pass

    # Provide helpers from the prompt if the solution module doesn't define them
    prompt_code = '\n\ndef get_positive(l: list):\n    """Return only positive numbers in the list.\n    >>> get_positive([-1, 2, -4, 5, 6])\n    [2, 5, 6]\n    >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])\n    [5, 3, 2, 3, 9, 123, 1]\n    """'
    if prompt_code.strip():
        exec(prompt_code, ns, ns)

    test_code = '\n\nMETADATA = {}\n\n\ndef check(candidate):\n    assert candidate([-1, -2, 4, 5, 6]) == [4, 5, 6]\n    assert candidate([5, 3, -5, 2, 3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 3, 9, 123, 1]\n    assert candidate([-1, -2]) == []\n    assert candidate([]) == []\n'
    exec(test_code, ns, ns)
    if "check" in ns and callable(ns["check"]):
        ns["check"](candidate)
