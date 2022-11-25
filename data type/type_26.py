# a = float(input())
# b = float(input())
# c = float(input())
# d = b ** 2 - 4 * a * c
# if d > 0:
#     from math import *
#     x_1 = (-b + sqrt(d)) / (2 * a)
#     x_2 = (-b - sqrt(d)) / (2 * a)
#     if x_1 < x_2:
#         print(x_1)
#         print(x_2)
#     else:
#         print(x_2)
#         print(x_1)
# elif d == 0:
#     from math import *
#     x_3 = -b / (2 * a)
#     print(x_3)
# else:
#     print('Нет корней')



a = float(input())
b = float(input())
c = float(input())
d = b ** 2 - 4 * a * c
if d > 0:
    from math import *
    x_1 = (-b + sqrt(d)) / (2 * a)
    x_2 = (-b - sqrt(d)) / (2 * a)
    print(min(x_1, x_2))
    print(max(x_1, x_2))
elif d == 0:
    from math import *
    x_3 = -b / (2 * a)
    print(x_3)
else:
    print('Нет корней')
