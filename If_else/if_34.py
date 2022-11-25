a = int(input())
b = int(input())
c = int(input())
d = int(input())
if (a - c) ** 2 == (b - d) ** 2:
    print('YES')
else:
    print('NO')


x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())

if (x1 - y1 == x2 - y2) or (x1 + y1 == x2 + y2):
    print('YES')
else:
    print('NO')