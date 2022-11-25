# s = input()
# print(s.replace('1', 'one'))

# s = input()
# print(s.replace('@', ''))


# s = input()
# first = s.find('h')
# last = s.rfind('h')
# srez = s[first + 1:last]
# print(s[:first + 1] + srez.replace('h', 'H') + s[last:])

s = input()
for i in range(len(s)):
    if i % 3 == 0:
        s = s.replace(s[i], '1', 1)
print(s.replace('1', ''))

