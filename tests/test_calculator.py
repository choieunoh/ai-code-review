import pytest
from src.calculator import calculate_average


def test_average():
    assert calculate_average([10, 20, 30]) == 20


def test_empty_list():
    with pytest.raises(ValueError):
        calculate_average([])
