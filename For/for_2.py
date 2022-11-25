# text = input()
# for i in range(10):
#     print(i, text)
#
# n = int(input())
# for i in range(n):
#     print('Квадрат числа', i, 'равен', i * i)
# for i in range(1):
#     print('Квадрат числа', n, 'равен', n * n)

# n = int(input())
# for i in range(n):
#     print(-1 * (i - n) * '*')
#
# n = int(input())
# for i in range(n):
#     print('*' * (n - i))


# m = int(input())
# p = int(input())
# n = int(input())
# for i in range(1):
#     print(i + 1, m)
# for i in range(n - 1):
#     print(i + 2, ((1 + p / 100) ** (i + 1) * m))

m = int(input())
p = int(input())
n = int(input())
for i in range(n):
    print(i + 1, m * (p / 100 + 1) ** i)