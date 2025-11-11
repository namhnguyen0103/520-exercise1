# AUTO-GENERATED: simple per-assert tests
import pytest
from gemini_sp.he100 import make_a_pile


def test_gemini_sp_he100_1():
    assert make_a_pile(3) == [3, 5, 7], "Test 3"

def test_gemini_sp_he100_2():
    assert make_a_pile(4) == [4,6,8,10], "Test 4"

def test_gemini_sp_he100_3():
    assert make_a_pile(5) == [5, 7, 9, 11, 13]

def test_gemini_sp_he100_4():
    assert make_a_pile(6) == [6, 8, 10, 12, 14, 16]

def test_gemini_sp_he100_5():
    assert make_a_pile(8) == [8, 10, 12, 14, 16, 18, 20, 22]

def test_gemini_sp_he100_invalid_inputs():
    # Non-integer inputs
    try:
        make_a_pile(3.5)
    except Exception:
        pass  # acceptable behavior: should raise an error
    else:
        # if no exception, it must return an empty list or handle gracefully
        assert make_a_pile(3.5) in ([], None)

    try:
        make_a_pile("4")
    except Exception:
        pass
    else:
        assert make_a_pile("4") in ([], None)

    try:
        make_a_pile([5])
    except Exception:
        pass
    else:
        assert make_a_pile([5]) in ([], None)

def test_gemini_sp_he100_non_positive():
    # Zero or negative inputs
    try:
        make_a_pile(0)
    except Exception:
        pass
    else:
        assert make_a_pile(0) in ([], None)

    try:
        make_a_pile(-3)
    except Exception:
        pass
    else:
        assert make_a_pile(-3) in ([], None)