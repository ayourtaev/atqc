from core.fibonacci import fibonacci_math


def how_many_fibo_do_u_want(n):
    return [fibonacci_math(_) for _ in range(n)]


def make_permutation_uniq(lst):
    [lst.remove(item) for item in lst if (item[1], item[0] in lst)]
    return lst






