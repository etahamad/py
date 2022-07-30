amazonCart = [
    'milk',
    'bread',
    'eggs',
    'apples',
    'bananas'
]


newCart = amazonCart[:] # copy list
newCart[0] = 'laptop'
print(newCart)
print(amazonCart)

# VS

newCart = amazonCart # modify original list
newCart[0] = 'laptop'
print(newCart)
print(amazonCart)
