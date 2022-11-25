# a = int(input())
# b = int(input())
# for i in range(a % 2 + a - 1, b - 1,  -2):
#     print(i, end=' ')

# total = 0
# for i in range(10):
#     num = int(input())
#     total += num
# print(total)

# n = int(input())
# total = 0
# for i in range(n):
#     num = int(input())
#     total += num
# print(total)

# n = int(input())
# total = 0
# for i in range(1, n + 1):
#     total += i ** 3
# print(total)

# n = int(input())
# total = 1
# for i in range(1, n + 1):
#     total *= i
# print(total)

# n = int(input())
# f = 1
# total = 0
# for i in range(1, n + 1):
#    f *= i
#    total += f
# print(total)

# n = int(input())
# counter = 0
# for i in range(n):
#     num = int(input())
#     if num == 0:
#         counter += 1
# print(counter)3
#
n = int(input())

for row in range(1, n + 1):
    for j in range(1, row + 1):
        print(j, end='')
    print()







