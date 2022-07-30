basket = ['a', 'b', 'x', 'c', 'd', 'e', 'd']

basket.sort()
basket.reverse()
print(basket[::-1])
print(basket)

print(list(range(101)))

# sentence = ' '
# newSentence = sentence.join(['This', 'is', 'a', 'join', 'test'])

newSentence = ' '.join(['This', 'is', 'a', 'join', 'test'])

print(newSentence)

# notes: basket[::-1] is not the same as basket.reverse()
#      basket[::-1] is a slice of the list which "copies" the list and reverses it
#      basket.reverse() is a method of the list which reverses the original list
