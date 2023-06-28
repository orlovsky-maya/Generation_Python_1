# Substring replacement

s = input()
print(s.replace('1', 'one'))

# Deleting a character

s = input()
print(s.replace('@', ''))

# Replacing inside a fragment

s = input()
first = s.find('h')
last = s.rfind('h')
slc = s[first + 1:last]
print(s[:first + 1] + slc.replace('h', 'H') + s[last:])

# Delete every third character

s = input()

for i in range(len(s)):
    if i % 3 == 0:
        s = s.replace(s[i], '1', 1)
print(s.replace('1', ''))
