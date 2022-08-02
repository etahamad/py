# list, set, dict

my_list = [char for char in 'hello']
my_list2 = [num for num in range(0, 10)]
my_list3 = [num * 2 for num in range(0, 10)]
my_list4 = [num ** 2 for num in range(0, 10)]
my_list5 = [num ** 2 for num in range(0, 10) if num % 2 == 0]

my_set = {char for char in 'hello'}

my_dict = {num: num ** 2 for num in range(0, 10) if num % 2 == 0}

print(my_list)
print(my_list2)
print(my_list3)
print(my_list4)
print(my_list5)

print(my_set)

print(my_dict)
