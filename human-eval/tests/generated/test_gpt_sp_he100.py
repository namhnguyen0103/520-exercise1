# AUTO-GENERATED: simple per-assert tests
import pytest
from gpt_sp.he100 import make_a_pile


def test_gpt_sp_he100_1():
    assert make_a_pile(3) == [3, 5, 7], "Test 3"

def test_gpt_sp_he100_2():
    assert make_a_pile(4) == [4,6,8,10], "Test 4"

def test_gpt_sp_he100_3():
    assert make_a_pile(5) == [5, 7, 9, 11, 13]

def test_gpt_sp_he100_4():
    assert make_a_pile(6) == [6, 8, 10, 12, 14, 16]

def test_gpt_sp_he100_5():
    assert make_a_pile(8) == [8, 10, 12, 14, 16, 18, 20, 22]

