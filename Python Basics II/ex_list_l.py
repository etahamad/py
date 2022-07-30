listOfL = [
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0],
    [0,0,0,1,1,1,1,1,1,1,1]
]

print()
fill, empty = '*', ' '
for row in listOfL:
    for col in row:
        if (col):
            print(fill, end='')
        else:
            print(empty, end='')
    print()
