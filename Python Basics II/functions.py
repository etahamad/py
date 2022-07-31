def sum(num1, num2):
    def secondSum(num1, num2):
        return num1 + num2
    return secondSum(num1, num2)

total = sum(10,20)
print (total)
