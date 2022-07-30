# Touple is immutable list
myTouple = (1, 2, 3, 4, 5, 5)
print(myTouple)

user = {
    (1, 2, 3): [1, 2, 3],
    'age': 21,
    'username': 'etahamad'
}

print(user[(1, 2, 3)])

newTouple = myTouple[1:4]
print(newTouple)

x, y, z, *other = (1, 2, 3, 4, 5)

print(other)

print(myTouple.count(5))
print(myTouple.index(5))
print(len(myTouple))
