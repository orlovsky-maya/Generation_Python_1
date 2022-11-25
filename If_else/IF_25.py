d1 = int(input())
d2 = int(input())
s = input()
if s == '+':
    print(d1 + d2)
elif s == '-':
    print(d1 - d2)
elif s == '*':
    print(d1 * d2)
elif s == '/' and d2 != 0:
    print(d1 / d2)
elif d2 == 0 and s == '/' :
    print('На ноль делить нельзя!')
else:
    print('Неверная операция')



a, b = int(input()), int(input())
s = input()
if s == '+':
    print(a + b)
elif s == '-':
    print(a - b)
elif s == '*':
    print(a * b)
elif s == '/':
    if b == 0:
        print('На ноль делить нельзя!')
    else:
        print(a / b)
else:
    print('Неверная операция')