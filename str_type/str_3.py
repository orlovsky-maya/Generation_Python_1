s = input()
counter_plus = 0
counter_star = 0

for c in s:
    if c == '+':
        counter_plus += 1
    if c == '*':
        counter_star += 1
print('Символ + встречается', counter_plus, 'раз')
print('Символ * встречается', counter_star, 'раз')
