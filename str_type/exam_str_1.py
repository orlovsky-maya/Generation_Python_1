# s = 'Python rocks!'
# print(len(s))

# s = 'Python rocks!'
# print(s[3])

#
# s = 'Python rocks!'
# print(s[1:5])


# s = '    Python rocks!     '
# print(s.strip())


# s = 'Python rocks!'
# print(s.upper())

#
# s = 'Python rocks!'
# print(s.replace('o', '@'))

# s = input()
# for i in range(len(s)):
#     if i % 3 != 0:
#         print(s[i], end='')


# s = input()
# print(s.replace('1', 'one'))
#
# s = input()
# print(s.replace('@', ''))


# s = input()
#
# if s.count('f') == 0:
#     print(-2)
# elif s.count('f') == 1:
#     print(-1)
# else:
#     s = s.replace('f', '1', 1)
#     print(s.find('f'))

s = input()
first = s.find('h')
last = s.rfind('h')
srez = s[first:last + 1]
print(s[:first] + srez[::-1] + s[last + 1:])
