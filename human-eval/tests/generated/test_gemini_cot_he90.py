# AUTO-GENERATED: simple per-assert tests
import pytest
from gemini_cot.he90 import next_smallest


def test_gemini_cot_he90_1():
    assert next_smallest([1, 2, 3, 4, 5]) == 2

def test_gemini_cot_he90_2():
    assert next_smallest([5, 1, 4, 3, 2]) == 2

def test_gemini_cot_he90_3():
    assert next_smallest([]) == None

def test_gemini_cot_he90_4():
    assert next_smallest([1, 1]) == None

def test_gemini_cot_he90_5():
    assert next_smallest([1,1,1,1,0]) == 1

def test_gemini_cot_he90_6():
    assert next_smallest([1, 0**0]) == None

def test_gemini_cot_he90_7():
    assert next_smallest([-35, 34, 12, -45]) == -35

