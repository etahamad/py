name = 'hamad'

print(name[:])
print(name[:len(name)])

quote = 'if you are reading this you are stalking me'

print(quote.capitalize())
print(quote.upper())

# returns the index of the first occurrence of the substring
print(quote.find('you'))
print(quote.replace('stalking me', 'a good person'))

print(quote)

'''
still the same? why?
strings are immutable, they can not be changed
we can overwrite them if we want but we don't change them
'''

# let's try something else
quote2 = quote.replace('stalking me', 'a good person in quote 2')
print(quote2)
