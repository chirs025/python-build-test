"""pytest unit tests for the calculator functions."""

import pytest

from ci_math import add, subtract, multiply, divide


@pytest.mark.parametrize("a,b,expected", [(1, 2, 3), (-2, -3, -5), (0, 0, 0)])
def test_add(a, b, expected):
    assert add(a, b) == expected


def test_subtract():
    assert subtract(9, 4) == 5


def test_multiply():
    assert multiply(3, -2) == -6


def test_divide():
    assert divide(8, 2) == 4


def test_divide_fraction():
    assert divide(1, 2) == 0.5


def test_divide_by_zero_raises_error():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)
