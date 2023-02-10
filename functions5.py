import math
import sys

# doesn't work

number1 = int(input("Please enter number1"))
number2 = int(input("Please enter number2"))


def menu(char):
    if char == 'a':
        return math.gcd(number1, number2)
    if char == 'b':
        return 1
    if char == 'c':
        return number1 ** number2
    if char == 'd':
        return math.sqrt(number1) - math.sqrt(number2)
    if char == 'e':
        sys.exit()


print(menu('a'), "\n", menu('b'), "\n", menu('c'), "\n", menu('d'), "\n", menu('e'))
