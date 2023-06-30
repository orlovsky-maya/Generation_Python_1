# объявление функции
def solve(a, b, c):
    from math import sqrt
    d = b ** 2 - 4 * a * c
    x_1 = (-b + sqrt(d)) / (2 * a)
    x_2 = (-b - sqrt(d)) / (2 * a)
    if x_1 < x_2:
        return x_1, x_2
    else:
        return x_2, x_1


# считываем данные
a, b, c = int(input()), int(input()), int(input())

# вызываем функцию
x1, x2 = solve(a, b, c)
print(x1, x2)
