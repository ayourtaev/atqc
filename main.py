from core.numbers_pairs import find_pairs
from utils import make_permutation_uniq, how_many_fibo_do_u_want

if __name__ == '__main__':
    # Write a function which prints pairs of numbers which sum is = 10
    # for a given collection of numbers.
    print(make_permutation_uniq(find_pairs([1, 2, 3, 4, 5, 6, 7, 8, 9], 10)))

    # Write a function which prints desired count of fibonacci numbers.
    print(how_many_fibo_do_u_want(7))
