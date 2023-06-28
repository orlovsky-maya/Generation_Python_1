from math import ceil

h = int(input())
a = int(input())
b = int(input())

q = h - a
w = a - b
e = ceil(q / w)
print(e + 1)