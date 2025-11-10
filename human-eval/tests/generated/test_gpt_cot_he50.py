# AUTO-GENERATED: exec original HumanEval test (needs context)
import pytest
import importlib

def _load_module(pkg: str, module_stem: str):
    return importlib.import_module(f"gpt_cot.he50")

def test_gpt_cot_he50():
    mod = _load_module("gpt_cot", "he50")
    candidate = getattr(mod, "decode_shift")

    # Namespace includes candidate and any helpers defined in the solution module
    ns = {"candidate": candidate, "decode_shift": candidate}
    for _name in dir(mod):
        if not _name.startswith("__"):
            try:
                ns.setdefault(_name, getattr(mod, _name))
            except Exception:
                pass

    # Provide helpers from the prompt if the solution module doesn't define them
    prompt_code = '\n\ndef encode_shift(s: str):\n    """\n    returns encoded string by shifting every character by 5 in the alphabet.\n    """\n    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])\n\n\ndef decode_shift(s: str):\n    """\n    takes as input string encoded with encode_shift function. Returns decoded string.\n    """'
    if prompt_code.strip():
        exec(prompt_code, ns, ns)

    test_code = "\n\nMETADATA = {}\n\n\ndef check(candidate):\n    from random import randint, choice\n    import copy\n    import string\n\n    letters = string.ascii_lowercase\n    for _ in range(100):\n        str = ''.join(choice(letters) for i in range(randint(10, 20)))\n        encoded_str = encode_shift(str)\n        assert candidate(copy.deepcopy(encoded_str)) == str\n"
    exec(test_code, ns, ns)
    if "check" in ns and callable(ns["check"]):
        ns["check"](candidate)
