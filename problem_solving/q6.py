from math import sqrt
# Question:
# Write a program that calculates and prints the value according to the given formula:
# Q = Square root of [(2 _ C _ D)/H]
# Following are the fixed values of C and H:
# C is 50. H is 30.
# D is the variable whose values should be input to your program in a comma-separated sequence.
# For example Let us assume the following comma separated input sequence is given to the program:
# 100,150,180
# The output of the program should be:
# 18,22,24


def main():
    D = input("Enter a sequence of numbers: ")
    D = D.split(",")
    C, H, Q = 50, 30, []
    for i in D:
        Q.append(round(sqrt((2 * C * float(i)) / H)))
    print(Q)


main()
