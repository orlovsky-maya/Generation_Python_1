# h = int(input())
# a = int(input())
# b = int(input())
# import math
#
# print(math.ceil(15 / 18))

h=int(input())
a=int(input())
b=int(input())

from math import ceil
q = h - a
w = a - b
e = ceil(q / w)
print(e + 1)