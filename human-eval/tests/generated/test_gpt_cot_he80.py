# AUTO-GENERATED: simple per-assert tests
import pytest
from gpt_cot.he80 import is_happy


def test_gpt_cot_he80_1():
    assert is_happy("a") == False , "a"

def test_gpt_cot_he80_2():
    assert is_happy("aa") == False , "aa"

def test_gpt_cot_he80_3():
    assert is_happy("abcd") == True , "abcd"

def test_gpt_cot_he80_4():
    assert is_happy("aabb") == False , "aabb"

def test_gpt_cot_he80_5():
    assert is_happy("adb") == True , "adb"

def test_gpt_cot_he80_6():
    assert is_happy("xyy") == False , "xyy"

def test_gpt_cot_he80_7():
    assert is_happy("iopaxpoi") == True , "iopaxpoi"

def test_gpt_cot_he80_8():
    assert is_happy("iopaxioi") == False , "iopaxioi"

