# Table 1

n = int(input())

for i in range(n):
    for j in range(3):
        print(n, end=' ')
    print()

# Table 2

n = int(input())

for i in range(1, n + 1):
    for j in range(5):
        print(i, end=' ')
    print()

# Table 3

n = int(input())

for i in range(1, n + 1):
    for j in range(1, 10):
        print(i, '+', j, '=', i + j)
    print()

# Star triangle

n = int(input())

for i in range(n // 2 + 1):
    for j in range(i + 1):
        print('*', end=' ')
    print()
for k in range(n // 2, 0, -1):
    for _ in range(k):
        print('*', end=' ')
    print()

# Star triangle second solution

n = int(input())

for i in range(1, n + 1):
    for j in range(i):
        if i + j <= n:
            print('*', end='')

    print()

# Number Triangle 1

n = int(input())

for i in range(n):
    for j in range(i + 1):
        print(i + 1, end='')
    print()
