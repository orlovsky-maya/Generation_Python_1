# In column 1

s = input()
for i in range(len(s)):
    if i % 2 == 0:
        print(s[i])

# In column 2

s = input()
for i in range(len(s) - 1, -1, -1):
    print(s[i])

# Full name

name = input()
surname = input()
patronymic = input()
print(surname[0] + name[0] + patronymic[0])

# Number 1

s = input()
total = 0
for c in s:
    total += int(c)
print(total)
