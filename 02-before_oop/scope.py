num = 1


def parent():
    num = 2

    def child():
        return num, sum  # sum is for testing built-in functions inside a scope
    return child()


print(parent())
print(num)
