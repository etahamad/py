def sum(num1, num2):
    def secondSum(n1, n2):
        return n1 + n2
    return secondSum(num1, num2)


total = sum(10, 20)
print(total)
