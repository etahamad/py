myList = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = []
for i in myList:
    if myList.count(i) > 1:
        if i not in duplicates:
            duplicates.append(i)
print(duplicates)
