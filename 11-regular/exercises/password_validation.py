import re

pattern = re.compile(r"[a-zA-Z0-9@#$%]{8,}\d$")
password = 'asdasdD#$321'

check = pattern.fullmatch(password)
print(check)
