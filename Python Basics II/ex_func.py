def heighestEven(li):
    evenList = []
    for i in li:
        if i % 2 == 0:
            evenList.append(i)
    return max(evenList)

print(heighestEven([1,2,2,3,3,4,4,5,6,7,8,9,10,11]))
