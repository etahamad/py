myList = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

tempDuplicates = []

def checkDup(listofItems):
    for i in listofItems:
        if listofItems.count(i) > 1:
            if i not in tempDuplicates:
                tempDuplicates.append(i)
    print(tempDuplicates)

checkDup(myList)
