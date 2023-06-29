n = int(input())
total = 0
for i in range(1, n + 1):
    total += i
for j in range(n - 1):
    num = int(input())
    total -= num
print(total)
