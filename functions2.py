def power(num1, num2):
    temp = num1
    for i in range(num2-1):
        num1 *= temp
    return num1


print(power(2, 3))
