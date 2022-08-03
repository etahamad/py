li = []


def using_for(n1, n2):
    for i in range(n1, n2):
        if i % 7 == 0 and i % 5 != 0:
            li.append(i)
    print(li)


print(f'Using for loop: ')
using_for(2000, 3200)

li = [i for i in range(2000, 3201) if i % 7 == 0 and i % 5 != 0]
print('Using list comprehension: ', li)
