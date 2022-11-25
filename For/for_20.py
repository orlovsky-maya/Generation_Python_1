# n = int(input())
# a = 1
# b = 1
#
# print(1, end=' ')
# for i in range(n - 1):
#     print(b, end=' ')
#     a, b = b, a + b
# #

# n = int(input())
# a = 1
# b = 1
#
# print(a, end=' ')
# print(b, end=' ')
#
# for i in range(n - 2):
#     a, b = b, a + b
#     print(b, end=' ')


n = int(input())
a, b = 1, 1

for i in range(n):
    print(a, end=' ')
    a, b = b, a + b
