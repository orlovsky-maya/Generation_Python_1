n = int(input())
total = n
for i in range(1, n):
    if n % i == 0:
        total += i
print(total)