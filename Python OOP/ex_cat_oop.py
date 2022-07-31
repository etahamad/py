# Given the below class:
class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
light_fury = Cat('Light Fury', 2)
samia = Cat('Samia', 1)
katosa = Cat('Katosa', 3)

# 2 Create a function that finds the oldest cat


def oldest_cat(*args):
    return max(args)


# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
print(f'The oldest cat is {oldest_cat(light_fury.age, samia.age, katosa.age)} years old.')
