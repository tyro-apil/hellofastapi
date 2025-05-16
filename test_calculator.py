import pytest

from calculator import calculate


def test_add():
    assert calculate("add", 5, 3) == 8


def test_subtract():
    assert calculate("subtract", 10, 4) == 6


def test_multiply():
    assert calculate("multiply", 2, 6) == 12


def test_divide():
    assert calculate("divide", 15, 3) == 5


def test_divide_by_zero():
    assert calculate("divide", 10, 0) == "Cannot divide by zero"


def test_invalid_operation():
    with pytest.raises(ValueError, match="Invalid operation: invalid"):
        calculate("invalid", 5, 2)
