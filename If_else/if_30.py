a = int(input())
b = int(input())
c = int(input())
d = int(input())
if (a + b) % 2 == 0 and (c + d) % 2 == 0:
    print('YES')
elif (a + b) % 2 != 0 and (c + d) % 2 != 0:
    print('YES')
else:
    print('NO')


a1 = int(input())
a2 = int(input())
b1 = int(input())
b2 = int(input())
if (a1 + a2 + b1 + b2) % 2 == 0:
    print('YES')
else:
    print('NO')