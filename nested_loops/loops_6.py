# n = int(input())
#
# total_fak_num = 0
#
# for n in range(1, n + 1):
#     fak_num = 1
#     for num in range(1, n + 1):
#         fak_num *= num
#     total_fak_num += fak_num
# print(total_fak_num)


n = int(input())

total = 0
from math import factorial

for n in range(1, n + 1):
    total += factorial(n)
print(total)


n = int(input())
a = 1
b = 0
for i in range(1, n + 1):
    a *= i
    b += a
print(b)