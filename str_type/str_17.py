# s = input()
# print(s[2])
# print(s[-2])
# print(s[:5])
# print(s[:-2])
# print(s[0::2])
# print(s[1::2])
# print(s[::-1])
# print(s[::-2])
# print(len(s))


# s = input()
# print(s.count(' ') + 1)

# from math import ceil
# s = input()
#
# first_part = ceil(len(s) / 2)
# print(s[first_part:] + s[:first_part])

s = input()
i = s.find(' ')
print(s[i + 1:], s[:i])