from collections import Counter, defaultdict

li = [1, 2, 3, 4, 5, 6, 7, 7]
sentence = 'blah blah blah'
print(Counter(li))
print(Counter(sentence))

dictinoary = defaultdict(lambda: 'doesn\'t exist', {'a': 1, 'b': 2, 'c': 3})
print(dictinoary['d'])
