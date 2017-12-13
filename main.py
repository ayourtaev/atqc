import argparse

from core.numbers_pairs import find_pairs
from utils import make_permutation_uniq, how_many_fibo_do_u_want

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="This app prints a number to the output")
    group = parser.add_argument_group("Parameters")
    group.add_argument("--num", "-n", action='store_true',
                       help="Run the function that will find a pairs in a common collection")
    group.add_argument("--fib", "-f", action='store',
                       help="Run the fibonacci function and set how many fibo value u want to get", type=int)
    args = parser.parse_args()
    if args.fib:
        print(how_many_fibo_do_u_want(args.fib))

    if args.num:
        print(make_permutation_uniq(find_pairs([1, 2, 3, 4, 5, 6, 7, 8, 9], 10)))
