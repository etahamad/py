def factorial(n):
    if n != 0:
        return n * factorial(n-1)
    return 1


# n * factorial(n-1) = 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1 = 40320
print(factorial(8))
