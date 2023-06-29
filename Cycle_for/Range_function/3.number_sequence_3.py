m = int(input())
n = int(input())
for i in range(m % 2 + m - 1, n - 1, -2):
    print(i)

# Second solution

m = int(input())
n = int(input())
for i in range(m, n - 1, -1):
    if i % 2 != 0:
        print(i)
