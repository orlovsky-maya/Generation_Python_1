# 1

s = 'Python rocks!'
print(len(s))

# 2

s = 'Python rocks!'
print(s[3])

# 3

s = 'Python rocks!'
print(s[1:5])

# 4

s = '    Python rocks!     '
print(s.strip())

# 5

s = 'Python rocks!'
print(s.upper())

# 6

s = 'Python rocks!'
print(s.replace('o', '@'))

# 7

s = input()
for i in range(len(s)):
    if i % 3 != 0:
        print(s[i], end='')

# 8

s = input()
print(s.replace('1', 'one'))

# 9

s = input()
print(s.replace('@', ''))

