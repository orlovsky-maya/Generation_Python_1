# Making slices 1

s = input()
print(len(s))
print(s * 3)
print(s[0])
print(s[:3])
print(s[-3:])
print(s[::-1])
print(s[1: -1])

# Making slices 2

s = input()
print(s[2])
print(s[-2])
print(s[:5])
print(s[:-2])
print(s[0::2])
print(s[1::2])
print(s[::-1])
print(s[::-2])

# Two halves

from math import ceil
s = input()
s_1 = ceil(len(s) / 2)
print(s[s_1:] + s[:s_1])