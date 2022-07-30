basket = ['a', 'b', 'x', 'c', 'd', 'e', 'd']

# basket.sort() # sorting the original list

newBasket = basket.copy()
newBasket.sort()
newBasket.reverse()
print(newBasket)

print(sorted(basket)) # creats a new copy of the list and sorts it
print(basket)
