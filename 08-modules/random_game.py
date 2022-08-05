from random import randint as rnd
import sys

random_number = rnd(int(sys.argv[1]), int(sys.argv[2]))
user_number = int(input(f'Guess a number between {sys.argv[1]} and {sys.argv[2]}: '))

while user_number != random_number:
    user_number = int(input("Wrong! Guess again: "))
print("You guessed it!")
