from functools import reduce

my_list = [1, 2, 3]


print(list(map(lambda i: i * 2, my_list)))
print(list(filter(lambda i: i % 2 != 0, my_list)))
print(reduce(lambda acc, i: acc + i, my_list))
