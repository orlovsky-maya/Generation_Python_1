s = input()
counter = 0
for c in s:
    if c in '0123456789':
        counter += 1
print(counter)

# Second solution

s = input()
counter = 0
for i in range(10):
    counter += s.count(str(i))
print(counter)
