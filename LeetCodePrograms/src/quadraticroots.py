import math


def solve_quadratics(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        return "No real roots"
    elif discriminant == 0:
        root = -b / (2 * a)
        return root
    else:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return root1, root2


a, b, c = 1, -3, 2
roots = solve_quadratics(a, b, c)
print(roots)
