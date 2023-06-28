# Capital letters

s = input()
name_last_name = s.title()
if s == name_last_name:
    print('YES')
else:
    print('NO')

# sWAP cASE

s = input()
print(s.swapcase())

# Good shade

s = input()
if 'хорош' in s.lower():
    print('YES')
else:
    print('NO')

# Lower case

s = input()
counter = 0
for c in s:
    if c not in '123456789':
        if c.lower() == c:
            counter += 1
print(counter)