import re

pattern = re.compile('search for a substring in a string substring')
string = 'search for a substring in a string substring Omar'

a = pattern.search(string)
b = pattern.findall(string)
c = pattern.fullmatch(string)
d = pattern.match(string)
print(d)
