mySet = {1, 2, 3, 4, 5}
yourSet = {4, 5, 6, 7, 8, 9, 10}
testSet = {11}
testSubSet = {4, 5, 6}

print('difference: ' + str(mySet.difference(yourSet)))
print('discard: ' + str(mySet.discard(4)))
print('mySet: ' + str(mySet))

print('difference_update: ' + str(mySet.difference_update(yourSet)))
print('mySet: ' + str(mySet))

print('intersection: ' + str(mySet.intersection(yourSet)))
print('intersection with &: ' + str(mySet & yourSet))
print('isdisjoint: ' + str(mySet.isdisjoint(yourSet)))
print('isdisjoint: ' + str(mySet.isdisjoint(testSet)))

print('union: ' + str(mySet.union(yourSet)))
print('union with |: ' + str(mySet | yourSet))

print('issubset: ' + str(testSubSet.issubset(yourSet)))
print('issuperset: ' + str(yourSet.issuperset(testSubSet)))
