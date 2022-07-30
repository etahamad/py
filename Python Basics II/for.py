user = {
    'name': 'Omar',
    'age': 21,
    'canSwim': True
}

for key, value in user.items():
    print(key, value)

for i in user.values():
    print(i)

for i in user.keys():
    print(i)

# ex: counter
myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 

counter = 0
for i in myList:
    counter += i
print(counter)

for i in range(0, 11, 1):
    print(i)

for i in range(10, 0, -2): # range(10, 0) will do noting!
    print(i)

for i in range(2):
    print(list(range(10)))

for i, char in enumerate('hello'):
    print(i, char)

for i, num in enumerate([1, 2, 3, 4, 5]):
    print(i, num)

for i, num in enumerate((1, 2, 3, 4, 5)):
    print(i, num)

for i, num in enumerate(list(range(100))):
    if num == 50:
        print(f'50 is at index {i}')
