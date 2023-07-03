n = int(input())
f = 1
total = 0
for i in range(1, n + 1):
    f *= i
    total += f
print(total)
