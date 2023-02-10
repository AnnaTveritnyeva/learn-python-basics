import math


# doesn't work

def a_not_zero(a):
    return a != 0


def sqrt(a, b, c):
    return math.sqrt((b ** 2) - (4 * a * c))


def quadratic_equation(a, b, c):
    if a_not_zero(a):
        return {"x1": (-1 * b + sqrt(a, b, c)) / (2 * a), "x2": (-1 * b - sqrt(a, b, c)) / (2 * a)}
    return "Error: division by zero"


print(quadratic_equation(2, 5, 6))
