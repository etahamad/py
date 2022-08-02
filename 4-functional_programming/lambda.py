from functools import reduce

my_list = [1, 2, 3]
unsorted_list = [(0, 2), (4, 3), (9, 9), (10, -1)]


print(list(map(lambda i: i * 2, my_list)))
print(list(filter(lambda i: i % 2 != 0, my_list)))
print(reduce(lambda acc, i: acc + i, my_list))
print(list(map(lambda i: i ** 2, my_list)))

# sort based on the second element
print(sorted(unsorted_list, key=lambda i: i[1]))
