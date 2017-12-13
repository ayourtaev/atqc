from core.fibonacci import fibonacci_math


def args_print(func):
    def wrapper(*args, **kwargs):
        print 'args: {args}\nkwargs: {kwargs}\n'.format(
            args=args, kwargs=kwargs)
        return func(*args, **kwargs)

    return wrapper


@args_print
def how_many_fibo_do_u_want(n):
    return [fibonacci_math(_) for _ in range(n)]


@args_print
def make_permutation_uniq(lst):
    [lst.remove(item) for item in lst if (item[1], item[0],) in lst]
    return lst
