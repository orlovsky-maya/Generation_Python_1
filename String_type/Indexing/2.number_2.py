s = input()
flag = False

for i in s:
    for j in range(10):
        if i == str(j):
            flag = True
            break
if flag:
    print('Цифра')
else:
    print('Цифр нет')

# Second solution

s = input()

for i in s:
    if i in '0123456789':
        print('Цифра')
        break
else:
    print('Цифр нет')

