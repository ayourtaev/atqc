import pytest

from core.fibonacci import fibonacci_math
from utils import how_many_fibo_do_u_want


@pytest.mark.parametrize('actual,expected', [
    (fibonacci_math(0), 0),
    (fibonacci_math(1), 1),
    (fibonacci_math(2), 1),
    (fibonacci_math(3), 2),
    (fibonacci_math(4), 3),
    (fibonacci_math(5), 5),
    (fibonacci_math(6), 8),
])
def test_fibo(actual, expected):
    assert actual == expected


@pytest.mark.parametrize('actual,expected', [
    (how_many_fibo_do_u_want(7), [0, 1, 1, 2, 3, 5, 8])
])
def test_fibo_lst(actual, expected):
    assert actual == expected