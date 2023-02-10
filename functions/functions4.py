def a_not_zero(a):
    return a != 0


def get_det(a, b, c):
    return (b ** 2) - (4 * a * c)


def det_pos(a, b, c):
    return get_det(a, b, c) >= 0


def quadratic_equation(a, b, c):
    if not a_not_zero(a):
        return "Error: division by zero"
    elif not det_pos(a, b, c):
        return "Negative det"
    else:
        return {"x1": (-1 * b + get_det(a, b, c) / (2 * a)), "x2": (-1 * b - +get_det(a, b, c) / (2 * a))}


print(quadratic_equation(1, 2, -3))
