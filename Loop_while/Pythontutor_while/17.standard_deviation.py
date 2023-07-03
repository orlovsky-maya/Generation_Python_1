from math import sqrt

x = int(input())

total = 0
total_squares = 0

n = 0
while x != 0:
    n += 1
    total += x
    total_squares += x ** 2
    x = int(input())
print(sqrt((total_squares - total ** 2 / n) / (n - 1)))
