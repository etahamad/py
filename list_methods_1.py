basket = [1, 2, 3, 4, 5]

newBasket = basket.extend([6, 7, 8, 9, 10, 69])
# print(basket)
# print(newBasket)

print(basket)
newBasket = basket.pop(2)
basket.remove(69)
basket.pop()
basket.pop(0)
print(newBasket)

newBasket = basket.clear()
print(basket)
