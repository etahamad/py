from datetime import date

birthYear = input('Birth year: ')

currentYear = date.today().year
age = currentYear - int(birthYear)

print(f'You are approximately {age} years old.')
