# Making slices

s = input()
print(s[2])
print(s[-2])
print(s[:5])
print(s[:-2])
print(s[0::2])
print(s[1::2])
print(s[::-1])
print(s[::-2])
print(len(s))

# Number of words

s = input()
print(s.count(' ') + 1)

# Two halves

from math import ceil
s = input()

first_part = ceil(len(s) / 2)
print(s[first_part:] + s[:first_part])

# Two halves

s = input()
i = s.find(' ')
print(s[i + 1:], s[:i])