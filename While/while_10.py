# n = int(input())
#
# for i in range(2, n + 1):
#     if n % i == 0:
#         print(i)
#         break
#
# n = int(input())
# i = 2
# while n % i != 0:
#     i += 1
# else:
#     print(i)


n = int(input())
i = 1
while i ** 2 <= n:
    print(i ** 2)
    i += 1
