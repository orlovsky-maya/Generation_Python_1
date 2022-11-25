# n = int(input())
#
# for i in range(n):
#     for j in range(3):
#         print(n, end=' ')
#     print()
#
#
# n = int(input())
#
# for i in range(1, n + 1):
#     for j in range(5):
#         print(i, end=' ')
#     print()


# n = int(input())
#
# for i in range(1, n + 1):
#     for j in range(1, 10):
#         print(i, '+', j, '=', i + j)
#     print()


# n = int(input())
#
# for i in range(n // 2 + 1):
#     for j in range(i + 1):
#         print('*', end=' ')
#     print()
# for k in range(n // 2, 0, -1):
#     for l in range(k):
#         print('*', end=' ')
#     print()


# n = int(input())
#
# for i in range(1, n + 1):
#     for j in range(i):
#         if i + j <= n:
#             print('*', end='')
#
#     print()


n = int(input())

for i in range(n):
    for j in range(i + 1):
        print(i + 1, end='')
    print()