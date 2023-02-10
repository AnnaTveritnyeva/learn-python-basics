import sys

num1 = int(input("Please enter first num: \n"))
num2 = int(input("Please enter second num: \n"))
digit = int(input("Please enter 1 or 2: \n"))

if digit == 1:
    print("num1 + num2 = " + str(num1 + num2))
elif digit == 2:
    print("num1 - num2 = " + str(num1 - num2))
else:
    sys.exit(0)
