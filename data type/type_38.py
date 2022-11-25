# p = int(input())
# x = int(input())
# y = int(input())
# r_1 = p * x / 100 + x
# k_1 = p * y / 100 + y
# k_2 = (r_1 - int(r_1)) * 100 + k_1
# k_3 = int(k_2) % 100
# r_2 = round(k_2) // 100 + r_1
# print(int(r_2), k_3)

# p = int(input())
# x = int(input())
# y = int(input())
# r_1 = p * x / 100 + x
# k_1 = p * y / 100 + y
# k_2 = (r_1 - int(r_1)) * 100 + k_1
# k_3 = k_2 % 100
# r_2 = k_2 // 100 + r_1
# print(int(r_2), int(k_3))

from math import floor, ceil

p = int(input())
x = int(input())
y = int(input())
money_after = ((x * 100 + y) * p / 100)  # summa in kop + %
r = s_k / 100 + x  # summa rub + %
k = r % 100 ??
print(floor(r), ceil(k))

# from math import floor
#
# p = int(input())
# x = int(input())
# y = int(input())
# r = x * p / 100 + x
# k = y * p / 100 + y
# k_s = r * 100 + k
# r_2 = floor(k_s / 100)
# k_2 = floor(k_s - r_2 * 100)
# print(r_2, k_2)
#
# print(101.79 % 100)
