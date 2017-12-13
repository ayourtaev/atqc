import pytest

from core.numbers_pairs import find_pairs
from utils import make_permutation_uniq


@pytest.mark.parametrize('actual',
                         find_pairs([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10))
def test_pairs_func(actual, expected=10):
    assert actual[0] + actual[1] == expected


def test_uniq_paris():
    actual_lst = make_permutation_uniq(find_pairs([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10))
    for pair in actual_lst:
        assert (pair[1], pair[0]) not in actual_lst

