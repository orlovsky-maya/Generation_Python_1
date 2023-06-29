# Repeat after me 2

text = input()
for i in range(10):
    print(i, text)
# Number square

n = int(input())
for i in range(n):
    print('Квадрат числа', i, 'равен', i * i)
for i in range(1):
    print('Квадрат числа', n, 'равен', n * n)


# Star triangle 1

n = int(input())
for i in range(n):
    print(-1 * (i - n) * '*')

# Star triangle 2

n = int(input())
for i in range(n):
    print('*' * (n - i))

# Population

m = int(input())
p = int(input())
n = int(input())
for i in range(1):
    print(i + 1, m)
for i in range(n - 1):
    print(i + 2, ((1 + p / 100) ** (i + 1) * m))

