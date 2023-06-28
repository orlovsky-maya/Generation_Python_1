# Slice 1

s = "In 2010, someone paid 10k Bitcoin for two pizzas."
print(s[:12])

# Slice 2

s = "In 2010, someone paid 10k Bitcoin for two pizzas."
print(s[-9:])

# Slice 3

s = "In 2010, someone paid 10k Bitcoin for two pizzas."
print(s[::7])

# Slice 4

s = "In 2010, someone paid 10k Bitcoin for two pizzas."
print(s[::-1])

# Palindrome

s = input()

if s[:] == s[::-1]:
    print('YES')
else:
    print('NO')