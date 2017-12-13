import itertools


def find_pairs(lst, key):
    """
    return pairs of numbers which sum is = key for a given collection of numbers.
    :param lst: collection of elements
    :param key: sum of pairs that should be
    :return: tuple ( pairs of numbers into lst, which sum == key )
    """
    return [(a, b) for a, b in itertools.permutations(lst, 2) if a + b == key]
