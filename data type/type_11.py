num = int(input())
a = num % 10
b = (num // 10) % 10
c = num // 100
d = max(a, b, c)
e = min(a, b, c)
f = (a + b + c) - (d + e)
if d - e == f:
    print('Число интересное')
else:
    print('Число неинтересное')