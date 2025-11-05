import pytest
from calculator import add, multiply

def test_add_positive():
    assert add(2, 3) == 5

def test_add_negative():
    assert add(-1, 1) == 0

def test_add_zero():
    assert add(0, 5) == 5

def test_multiply_positive():
    assert multiply(2, 3) == 6

def test_multiply_zero():
    assert multiply(0, 5) == 0

def test_multiply_negative():
    assert multiply(-2, 3) == -6
