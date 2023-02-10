def power(num1, num2):
    temp = 1
    for i in range(num2):
        temp *= num1
    return temp


print(power(2, 3))
