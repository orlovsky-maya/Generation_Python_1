a = int(input())
b = int(input())
n = int(input())
k = b * n % 100
r = (a * n) + (b * n // 100)
print(r, k)

a = int(input())
b = int(input())
n = int(input())
cost = n * (100 * a + b)
print(cost // 100, cost % 100)