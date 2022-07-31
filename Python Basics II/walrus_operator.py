longString = "this is a long string"

if ((longStringLen := len(longString)) > 10):
    print(f'too long {longStringLen} elements')

while ((longStringLen := len(longString)) > 1):
    print(longStringLen)
    longString = longString[:-1]

print(longString) # t....his is a long string
