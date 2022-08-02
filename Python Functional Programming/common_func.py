# map, filter, zip, and reduce
from functools import reduce

my_list = [1, 2, 3]
your_list = [10, 20, 30]
there_list = [5, 6, 7]


def multiply_by2(i):
    return i * 2


def only_odd(i):
    return i % 2 != 0


def accumulator(acc, i):
    print(acc, i)
    return acc + i


print(list(map(multiply_by2, my_list)))
print(list(filter(only_odd, my_list)))
print(list(zip(my_list, your_list, there_list)))
print(reduce(accumulator, my_list, 0))
