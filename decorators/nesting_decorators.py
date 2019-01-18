from decorators import cast_to_int, timer
from functools import reduce


def sum(func):
    def wrapper(*args):
        sum_ = reduce(lambda a, b: a + b, args)
        return func(sum_)

    return wrapper


@cast_to_int
@sum
@timer
def add_list_elements(str_list):
    print(str_list)


add_list_elements("10", '20', '30', '40')  # timer(sum(cast_to_int(add_list_elements(elements))))
