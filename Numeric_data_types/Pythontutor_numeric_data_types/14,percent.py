from math import floor

p = int(input())
x = int(input())
y = int(input())
r = x * p / 100 + x
k = y * p / 100 + y
k_s = r * 100 + k
r_2 = floor(k_s / 100)
k_2 = floor(k_s - r_2 * 100)
print(r_2, k_2)

